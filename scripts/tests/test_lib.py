from dataclasses import dataclass, field
from pathlib import Path

import pytest

from scripts.lib import (
    Context,
    Result,
    ValidatedContent,
    is_non_empty_content,
    is_valid_project_root,
)


class TestIsValidProjectRoot:
    def test_valid_when_cv_exists(self, tmp_path: Path):
        (tmp_path / "src").mkdir()
        (tmp_path / "src" / "cv.typ").touch()
        assert is_valid_project_root(tmp_path) is True

    def test_invalid_when_cv_missing(self, tmp_path: Path):
        assert is_valid_project_root(tmp_path) is False

    def test_invalid_when_src_missing(self, tmp_path: Path):
        (tmp_path / "cv.typ").touch()
        assert is_valid_project_root(tmp_path) is False


class TestIsNonEmptyContent:
    def test_valid_with_content(self):
        assert is_non_empty_content("hello") is True

    def test_invalid_when_empty(self):
        assert is_non_empty_content("") is False

    def test_invalid_when_whitespace_only(self):
        assert is_non_empty_content("   \n\t  ") is False


class TestResult:
    def test_default_values(self):
        result: Result[str] = Result(success=True)
        assert result.success is True
        assert result.data is None
        assert result.errors == []
        assert result.warnings == []

    def test_with_data(self):
        result: Result[int] = Result(success=True, data=42)
        assert result.data == 42

    def test_add_error_sets_success_false(self):
        result: Result[str] = Result(success=True)
        result.add_error("une erreur")
        assert result.success is False
        assert "une erreur" in result.errors

    def test_add_error_returns_self(self):
        result: Result[str] = Result(success=True)
        returned = result.add_error("erreur")
        assert returned is result

    def test_add_warning_keeps_success(self):
        result: Result[str] = Result(success=True)
        result.add_warning("attention")
        assert result.success is True
        assert "attention" in result.warnings

    def test_add_warning_returns_self(self):
        result: Result[str] = Result(success=True)
        returned = result.add_warning("warning")
        assert returned is result

    def test_chained_operations(self):
        result: Result[str] = Result(success=True)
        result.add_warning("w1").add_warning("w2").add_error("e1")
        assert result.warnings == ["w1", "w2"]
        assert result.errors == ["e1"]
        assert result.success is False


@dataclass
class MockResult:
    success: bool
    errors: list[str] = field(default_factory=list)


@dataclass
class MockContext(Context[str, MockResult]):
    pass


class TestContext:
    def test_bind_executes_on_success(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def add_suffix(c: MockContext) -> MockContext:
            c.data = c.data + "_modified"
            return c

        result = ctx.bind(add_suffix)
        assert result.data == "test_modified"

    def test_bind_short_circuits_on_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=False))

        def should_not_run(c: MockContext) -> MockContext:
            c.data = "should not appear"
            return c

        result = ctx.bind(should_not_run)
        assert result.data == "test"

    def test_map_always_executes(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def transform(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        result = ctx.map(transform)
        assert result.data == "TEST"

    def test_map_executes_even_on_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=False))

        def transform(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        result = ctx.map(transform)
        assert result.data == "TEST"

    def test_chained_bind_stops_after_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def fail_step(c: MockContext) -> MockContext:
            c.result.success = False
            c.data = c.data + "_failed"
            return c

        def should_not_run(c: MockContext) -> MockContext:
            c.data = c.data + "_after"
            return c

        result = ctx.bind(fail_step).bind(should_not_run)
        assert result.data == "test_failed"
        assert "_after" not in result.data

    def test_chained_map_always_runs(self):
        ctx = MockContext(data="a", result=MockResult(success=True))

        result = (
            ctx.map(lambda c: MockContext(data=c.data + "b", result=c.result))
            .map(lambda c: MockContext(data=c.data + "c", result=c.result))
            .map(lambda c: MockContext(data=c.data + "d", result=c.result))
        )
        assert result.data == "abcd"

    def test_mixed_bind_and_map(self):
        ctx = MockContext(data="start", result=MockResult(success=True))

        def fail_bind(c: MockContext) -> MockContext:
            c.result.success = False
            c.result.errors.append("failed")
            return c

        def map_upper(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        def bind_after(c: MockContext) -> MockContext:
            c.data = c.data + "_bound"
            return c

        result = ctx.map(map_upper).bind(fail_bind).bind(bind_after).map(map_upper)
        assert result.result.success is False
        assert "failed" in result.result.errors
        assert "_bound" not in result.data


class TestValidatedContentType:
    def test_can_create_validated_content(self):
        content = ValidatedContent("some content")
        assert content == "some content"

    def test_validated_content_is_str(self):
        content = ValidatedContent("test")
        assert isinstance(content, str)

import re
from pathlib import Path
from datetime import datetime, timedelta

tasks_dir = Path('.tasks/tasks')

# List of task IDs to analyze (excluding completed tasks)
task_ids = ['CNT-004', 'CNT-005', 'CNT-006', 'CNT-008', 'CNT-009',
            'CNT-010', 'CNT-014', 'CNT-015', 'TPL-001', 'QUA-001', 'TPL-002',
            'PIP-001', 'INF-001']

priority_scores = {'🔴 Haute': 10, '🟡 Moyenne': 5, '🟢 Basse': 2}
default_times = {'🔴 Haute': 8, '🟡 Moyenne': 4, '🟢 Basse': 2}

tasks_data = []
today = datetime(2025, 11, 16)

for task_id in task_ids:
    task_files = list(tasks_dir.glob(f'{task_id}-*.md'))
    if not task_files:
        continue

    content = task_files[0].read_text()

    # Extract metadata
    priority_match = re.search(r'\| \*\*Priorité\*\* \| (.*?) \|', content)
    time_match = re.search(r'\| \*\*Temps estimé\*\* \| (.*?) \|', content)
    created_match = re.search(r'\| \*\*Créé le\*\* \| (.*?) \|', content)
    target_match = re.search(r'\| \*\*Cible\*\* \| (.*?) \|', content)
    title_match = re.search(r'\| \*\*Titre\*\* \| (.*?) \|', content)

    priority = priority_match.group(1).strip() if priority_match else '🟡 Moyenne'
    time_str = time_match.group(1).strip() if time_match else ''
    created = created_match.group(1).strip() if created_match else ''
    target = target_match.group(1).strip() if target_match else '-'
    title = title_match.group(1).strip() if title_match else task_id

    # Parse time estimate
    time_hours = None
    if time_str:
        # Extract first number from patterns like "0.25 heures", "2-3 heures", "2 heures"
        numbers = re.findall(r'(\d+\.?\d*)', time_str)
        if numbers:
            time_hours = float(numbers[0])

    if time_hours is None:
        time_hours = default_times.get(priority, 4)

    # Calculate value
    priority_value = priority_scores.get(priority, 5)

    # Urgency
    urgency = 0
    if target != '-':
        try:
            target_date = datetime.strptime(target, '%Y-%m-%d')
            days_until = (target_date - today).days
            if days_until < 0:
                urgency = 10  # Overdue
            elif days_until < 7:
                urgency = 5
            elif days_until < 30:
                urgency = 2
        except:
            pass

    # Age
    age_value = 0
    if created:
        try:
            created_date = datetime.strptime(created, '%Y-%m-%d')
            days_old = (today - created_date).days
            age_value = min(days_old / 10, 5)
        except:
            pass

    total_value = priority_value + urgency + age_value
    score = total_value / time_hours

    tasks_data.append({
        'id': task_id,
        'title': title,
        'priority': priority,
        'time': time_hours,
        'value': total_value,
        'score': score,
        'priority_val': priority_value,
        'urgency': urgency,
        'age': age_value
    })

# Sort by score descending
tasks_data.sort(key=lambda x: x['score'], reverse=True)

# Display top 3
print("🔍 Analyse des tâches (méthode: valeur/temps)\n")
print(f"Tâches analysées: {len(tasks_data)}\n")

for i, task in enumerate(tasks_data[:5], 1):
    print(f"{i}. {task['id']} - {task['title'][:50]}")
    print(f"   {task['priority']} | ⏱️  {task['time']}h | Score: {task['score']:.2f}")
    print(f"   Valeur: {task['value']:.1f} (Prio={task['priority_val']}, Urgence={task['urgency']:.0f}, Âge={task['age']:.1f})")
    print()

if tasks_data:
    print(f"💡 Suggestion: {tasks_data[0]['id']}")
    print(f"   {tasks_data[0]['title']}")
    print(f"   Score: {tasks_data[0]['score']:.2f} ({tasks_data[0]['priority']}, {tasks_data[0]['time']}h)")
else:
    print("⚠️  Aucune tâche à faire trouvée")

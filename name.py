el = [
    {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
    {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 90},
    {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 100},
    {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
    {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
]
sum1 = 0
for i in el:
    task = i['tasks_completed']
    sum1 = sum1 + task
print(sum1)

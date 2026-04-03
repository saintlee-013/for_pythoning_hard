"""
Given a list of dictionaries representing employees where each dictionary contains the keys employee_id, tasks_completed, and hours_worked
write a function that does the following based on the given task:

total_tasks_completed: Compute the total number of tasks completed by all employees combined.

most_efficient_employee: Determine the id of the employee with the highest ratio of tasks_completed to hours_worked. If there are ties, break by the highest number of tasks completed.

sort_by_hours_worked: Get the list of employee ids sorted by the number of hours worked from the highest to the lowest and break ties using the highest number of tasks completed.

productive_team_members: Filter and return a list of employee ids of employees who have completed 20 or more tasks in the order that they are present in the employee list.
"""
def process_employees(employee_list: list, request: str):
    """
    Process the employee list as per the request.
    
    Args:
        employee_list (list[dict]): List of dictionaries with the keys
            "employee_id", "tasks_completed", and "hours_worked".
        request (str): One of the following options:
            - 'total_tasks_completed'
            - 'most_efficient_employee'
            - 'sort_by_hours_worked'
            - 'productive_team_members'.
        
    Returns:
        The output corresponding to the request.
    """
employee_list = [
    {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
    {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 90},
    {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 100},
    {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
    {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30}, ]
sum_of_task_complete = 0
if (request == "total_tasks_completed"):
 for items in employee_list:
        sum_of_task_complete = sum_of_task_complete + items['tasks_completed']
        return(sum_of_task_complete)
if(request == "most_efficient_employee"):    
   most_efficient_employee = max(employee_list, key=lambda emp: (emp['tasks_completed'] / emp['hours_worked'], emp['tasks_completed'] ))

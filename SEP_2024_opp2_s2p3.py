def process_call_logs(call_logs, task):
    """
    Processes a list of call log dictionaries based on the specified task,
    using only standard Python dictionaries.

    Args:
        call_logs (list): A list of dictionaries, each with 'name' (str) and
                          'duration' (int) keys.
        task (str): The specific analysis task to perform.
                    Options: 'get_call_counts', 'get_total_call_durations',
                             'most_frequent_caller'.

    Returns:
        dict or str: The result of the requested task.
    """
    
    # Initialize standard dictionaries for aggregation
    call_counts = {}
    total_durations = {}

    # --- Aggregation Step ---
    for log in call_logs:
        name = log["name"]
        duration = log["duration"]
        
        # Aggregate call counts
        # Use .get() method to safely handle keys that might not exist yet
        call_counts[name] = call_counts.get(name, 0) + 1
        
        # Aggregate total durations
        total_durations[name] = total_durations.get(name, 0) + duration

    # --- Execution Step ---
    if task == 'get_call_counts':
        return call_counts
    
    elif task == 'get_total_call_durations':
        return total_durations
    
    elif task == 'most_frequent_caller':
        if not call_logs:
            return None

        best_caller = None
        max_count = -1
        max_duration = -1

        # Iterate through all unique callers
        for name in call_counts:
            count = call_counts[name]
            duration = total_durations[name]
            
            # Check for highest number of calls
            if count > max_count:
                max_count = count
                max_duration = duration
                best_caller = name
            
            # Handle tie: check for highest duration among tied counts
            elif count == max_count:
                if duration > max_duration:
                    max_duration = duration
                    best_caller = name
        
        return best_caller
    
    else:
        # Handle invalid task input
        return f"Error: Invalid task '{task}' specified."

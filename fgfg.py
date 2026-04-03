a = []
numeric_values = []
while True:
    try:
        s = input()
    except EOFError:
        break
    clean_s = s.strip()
    a = []
    if clean_s == "":
        # 2. Ignore empty lines
        continue
        
    elif clean_s == "stop":
        # 3. Terminate the loop ONLY on "stop"
        break
        
    else:
        # 4. Filter for ANY number using try-except (This is the most robust step)
        try:
            # Attempt to convert the cleaned line to an integer
            value = int(clean_s) 
            
            # If successful, append the integer
            numeric_values.append(value)
        except ValueError:
            # This catches any non-numeric input (e.g., "hello", "10a", "10 dollars")
            # The input is ignored, and the loop continues to the next line.
            continue

num_collected = len(numeric_values)

# Loop through the list, taking steps of 2
for i in range(0, num_collected, 2):
    
    if i + 1 < num_collected:
        # Process Pair
        num1 = numeric_values[i]
        num2 = numeric_values[i+1]
        average = (num1 + num2) / 2
        
        # Round to 2 decimal places and print
        print(round(average, 2))
        
    else:
        # Process Single Last Element (Odd total count)
        last_value = numeric_values[i]
        print(last_value)
        

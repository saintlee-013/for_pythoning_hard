obs = input("Paste your data: ")

# New, robust cleaning step: No need for .replace, just split by any whitespace!
lobsf = [] # Initialize list for numbers

# Use .split() with no argument to split by ANY whitespace and discard empty results
lobs = obs.split() 

# Convert to float (using the loop for clarity and error detection)
sumtotal = 0 
for number_string in lobs:
    try:
        number = float(number_string)
        lobsf.append(number)
        sumtotal += number
    except ValueError:
        print(f"Skipping invalid item: '{number_string}'")

count = len(lobsf)

if count != 0:
    avg = sumtotal / count
    print(f"\nTotal Valid Observations: {count}")
    print(f"The Mean is: {avg:.10f}")
else:
    print("No valid numbers were found.")

obs = input("Paste your data: ")

# 1. Use .split() with NO argument. It handles ALL whitespace as separators 
#    (including the ones you were trying to replace) AND filters empty strings.
#    This makes the original .replace line unnecessary!
lobs = obs.split() 

# 2. Proceed with calculation (using the error-handling loop for safety)
lobsf = []
sumtotal = 0 
for number_string in lobs:
    try:
        number = float(number_string)
        lobsf.append(number)
        sumtotal += number
    except ValueError:
        # If any item couldn't be converted, it will be skipped and reported.
        print(f"Skipping invalid item: '{number_string}'")

count = len(lobsf)

if count != 0:
    avg = sumtotal / count
    print(f"\nTotal Valid Observations: {count}")
    print(f"The Mean is: {avg:.10f}")
else:
    print("No valid numbers were found.")

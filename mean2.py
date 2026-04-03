obs = input("Paste your data: ")
obsclean = obs.replace('\n', ' ').replace(',', ' ').replace('\r', ' ')
lobs = [ob for ob in obsclean.split(' ') if ob]
lobsf = [] # Initialize a clean list for floats

# --- ADD ERROR HANDLING HERE ---
print("\n--- Validating Data ---")
for ob in lobs:
    try:
        # Try to convert the string to a float
        lobsf.append(float(ob))
    except ValueError:
        # If the conversion fails, print the bad data and skip it
        print(f"Skipping invalid data point: '{ob}'")

# --- CONTINUE CALCULATION ---
sumtotal = sum(lobsf)
count = len(lobsf)

if count != 0:
    avg = sumtotal / count
    print(f"\nTotal Valid Observations: {count}")
    print(f"The Mean is: {avg:.4f}")
else:
    print("No valid numbers were found after filtering.")

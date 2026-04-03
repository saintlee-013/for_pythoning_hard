# The print statement serves as a prompt to the user
print("Enter potential 1 (V1), potential 2 (V2) separated by a comma (e.g., 5.0, 3.2):")

# Get user input for potentials, split the string, and convert to float
# The input() function reads a string. We must assign its result to a variable.
try:
    V_input = input()
    V1_str, V2_str = V_input.split(',')
    V1 = float(V1_str.strip())
    V2 = float(V2_str.strip())
except ValueError:
    print("Error: Invalid input for potentials. Please enter two numbers separated by a comma.")
    # You might want to exit the script here or loop back for correct input
    exit()

print("Enter frequency 1 (n1), frequency 2 (n2) separated by a comma (e.g., 8.0e14, 6.0e14):")

# Get user input for frequencies, split the string, and convert to float
try:
    n_input = input()
    n1_str, n2_str = n_input.split(',')
    n1 = float(n1_str.strip())
    n2 = float(n2_str.strip())
except ValueError:
    print("Error: Invalid input for frequencies. Please enter two numbers separated by a comma.")
    exit()

# Calculation part
# Calculate the absolute difference in potential
diffp = abs(V1 - V2)
# Calculate the absolute difference in frequency
diffn = abs(n1 - n2)

print("\n--- Results ---")
print(f"Difference in potential (V1 - V2): {diffp} V")
print(f"Difference in frequency (Δn): {diffn:.4e} Hz") # Display in scientific notation

# The formula for Planck's constant (h) using the photoelectric effect is:
# h = (e * (V1 - V2)) / (n1 - n2)
# Where 'e' is the elementary charge (approx. 1.602 x 10^-19 Coulombs)

# Assuming the constant 1.6 in your original code is the elementary charge * 10^14
# e = 1.602e-19 C (Elementary Charge)
ELEMENTARY_CHARGE = 1.602e-19 # Use a more accurate and standard value

if diffn == 0:
    print("Error: Difference in frequency is zero. Cannot divide by zero.")
else:
    # Calculation: (e * diffp) / diffn
    h_value = (ELEMENTARY_CHARGE * diffp) / diffn

    # Your original code was: prod = ((1.6) * diffp) / diffn
    # This suggests the final result should be formatted to show 10^-33
    # Let's format the actual Planck's constant value to see if it matches the expected experiment result

    # Standard Planck's Constant h ≈ 6.626 x 10^-34 J·s
    # The expected result of an experiment like this is typically around 10^-34

    # Format the result to match the user's expected output format of "times 10^-33"
    # To represent h_value as X * 10^-33, we calculate X = h_value / 10^-33 = h_value * 10^33
    h_formatted = h_value * 1e33

    print(f"Calculated Planck's constant (h): {h_value:.3e} J·s")
    print(f"h = {h_formatted:.4f} times 10^-33 J·s (Formatted to match your original output style)")

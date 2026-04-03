# Write your code to read the file and print the result.
# use the variable filename for the name of the file.

# --- Start of Solution (No imports, no try/except) ---

# Open the file in read mode
# Assuming 'filename' is defined and the file exists.
f = open(filename, 'r')
lines = f.readlines()
f.close()

if not lines:
    # Cannot use sys.exit(0) without importing sys. The program will simply end.
    pass

# The last line contains the order indices
order_line = lines[-1].strip()

# The preceding lines are the text content, stripped of trailing newlines/whitespace
text_lines = [line.strip() for line in lines[:-1]]

# 1. Parse the comma-separated order indices
order_indices = []
order_items = order_line.split(',')

for item in order_items:
    stripped_item = item.strip()
    
    # Check if the item is not empty
    if stripped_item:
        # Check if the item is a valid integer string.
        # We must rely on string methods since we cannot use try/except.
        is_digit = stripped_item.isdigit()
        
        if is_digit:
            index = int(stripped_item)
            order_indices.append(index)
        
        # Note: If the input might contain negative indices, the logic needs 
        # a slightly more complex string check, but based on the example, we 
        # assume simple positive 1-based indices.

# 2. Reorder the lines based on the 1-based indices
reordered_lines = []
num_text_lines = len(text_lines)

for index in order_indices:
    # Convert 1-based index to 0-based index
    zero_based_index = index - 1
    
    # Explicit check for bounds
    if 0 <= zero_based_index < num_text_lines:
        line_to_print = text_lines[zero_based_index]
        reordered_lines.append(line_to_print)

# 3. Print the reordered lines
for line in reordered_lines:
    print(line)

# --- End of Solution ---

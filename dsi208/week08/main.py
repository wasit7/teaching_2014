def display_min_steps_tree(n, indent="", is_last=True, min_path=[]):
    # Base case: when n is 1, we've reached the end
    if n == 1:
        print(f"{indent}{'└─ ' if is_last else '├─ '}1")
        return
    
    # Determine if this step is part of the pre-determined minimum path
    is_min_path = n == min_path[0]
    if is_min_path:
        min_path_indicator = " *[min path]"
        min_path.pop(0)
        # print(min_path)
    else:
        min_path_indicator = ""
    
    # Print the current number with or without the minimum path indicator
    print(f"{indent}{'└─ ' if is_last else '├─ '}{n}{min_path_indicator}")
    
    # Adjust indent for the next level
    new_indent = indent + ("    " if is_last else "│   ")
    
    # Decide the order of operations based on what's possible
    operations = []
    if n % 3 == 0:
        operations.append(n // 3)
    if n % 2 == 0:
        operations.append(n // 2)
    operations.append(n - 1)  # Always possible
    
    # Recursive calls for each possible operation, ensuring the last operation updates indentation correctly
    for i, op in enumerate(operations):
        display_min_steps_tree(op, new_indent, i == len(operations) - 1, min_path)

def find_min_path(n):
    # please implement this function
    return [6,2,1]

if __name__ == "__main__":
    # Display the tree for n=7
    n = 6
    print(f"Minimizing steps tree for n={n}:")
    display_min_steps_tree(n=n, min_path=find_min_path(n))

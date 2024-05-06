from main import display_min_steps_tree, find_min_path
def calculate_min_steps_and_path(n):
    # Initialize arrays to store the minimum steps and predecessors
    min_steps = [float('inf')] * (n + 1)
    predecessor = [-1] * (n + 1)
    
    # Base case
    min_steps[1] = 0
    
    # Calculate min steps and predecessors
    for i in range(2, n + 1):
        # Check divide by 3
        if i % 3 == 0 and min_steps[i // 3] + 1 < min_steps[i]:
            min_steps[i] = min_steps[i // 3] + 1
            predecessor[i] = i // 3

               
        # Check divide by 2
        if i % 2 == 0 and min_steps[i // 2] + 1 < min_steps[i]:
            min_steps[i] = min_steps[i // 2] + 1
            predecessor[i] = i // 2
        
        # Check subtract 1
        if min_steps[i - 1] + 1 < min_steps[i]:
            min_steps[i] = min_steps[i - 1] + 1
            predecessor[i] = i - 1
            
    # Reconstruct the path from n to 1
    path = []
    while n > 0:
        path.append(n)
        n = predecessor[n]
    
    #path.reverse()  # Reverse to start from n down to 1
    return min_steps[-1], path

# Example usage
n=5
n = int(input("Enter your number: "))
min_steps, min_path = calculate_min_steps_and_path(n)
print(f"Minimum steps to reduce {n} to 1: {min_steps}")
print(f"Path: {min_path}")
display_min_steps_tree(n=n, min_path=min_path)

# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8



def fib (num):
    # base case 
    if num < 2:
        return 1
    else:
    
        return (fib(num-1) + fib(num-2))
    
print(f"Iteration 0: {fib(1)}")
print(f"Iteration 1: {fib(1)}")
print(f"Iteration 2: {fib(2)}")
print(f"Iteration 3: {fib(3)}")
print(f"Iteration 4: {fib(4)}")
print(f"Iteration 5: {fib(5)}")
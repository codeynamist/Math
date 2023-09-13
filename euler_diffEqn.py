import numpy as np

def euler_method(func, x0, y0, h, x_target):
    x_values = [x0]
    y_values = [y0]
    
    while x_values[-1] < x_target:
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * func(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

def user_input():
    def func(x, y):
        # The function you want to solve
        return x**2 + y**2  # Replace with your own function
    
    x0 = float(input("Enter the initial x-value (x0): "))
    y0 = float(input("Enter the initial y-value (y0): "))
    h = float(input("Enter the step size (height, h): "))
    x_target = float(input("Enter the target x-value: "))
    
    x_values, y_values = euler_method(func, x0, y0, h, x_target)
    
    return x_values, y_values

# Main program
if __name__ == "__main__":
    x_values, y_values = user_input()
    
    # Display the results
    print("\nResults:")
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.4f}, y = {y:.4f}")

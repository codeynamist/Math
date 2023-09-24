def runge_kutta_4th_order(func, x0, y0, h, x_target):
    x_values = [x0]
    y_values = [y0]
    
    while x_values[-1] < x_target:
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = h * func(x, y)
        k2 = h * func(x + h/2, y + k1/2)
        k3 = h * func(x + h/2, y + k2/2)
        k4 = h * func(x + h, y + k3)
        
        x_new = x + h
        y_new = y + (k1 + 2*k2 + 2*k3 + k4)/6
        
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

def user_input():
    def func(x, y):
        return x**2 + y**2 #Your Function Here
    
    x0 = float(input("Enter the initial x-value (x0): "))
    y0 = float(input("Enter the initial y-value (y0): "))
    h = float(input("Enter the step size (h): "))
    x_target = float(input("Enter the target x-value: "))
    
    x_values, y_values = runge_kutta_4th_order(func, x0, y0, h, x_target)
    
    return x_values, y_values

# Main program
if __name__ == "__main__":
    x_values, y_values = user_input()
    
    # Display the results
    print("\nResults:")
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.4f}, y = {y:.4f}")

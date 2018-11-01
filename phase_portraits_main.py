import numpy as np
import cust_input
import phase_portraits as pp

#variant #37:
#x_dot = x^2 - y
#y_dot = (x - y)*(x - y + 2)

print("1 - Constant alphas\n2 - Alphas, varying by exponential law\n3 - Alphas, varying by normalized law\n")

key = cust_input.int_input(1, 3, "")

N = 100000

if key == 1:
    alpha_x = cust_input.float_input(0.0000001, 0.1, "Enter alpha_x(step parameter in x direction, from 0.0000001 to 0.1): \n")
    alpha_y = cust_input.float_input(0.0000001, 0.1, "Enter alpha_y(step parameter in y direction, from 0.0000001 to 0.1): \n")

n = cust_input.int_input(1, 20, "Enter the number of starting points you need: \n")

x = np.zeros([n, N])
y = np.zeros([n, N])

i = 0
for i in range(n):
    print("\nEnter point #", i + 1, ":")
    x[i, 0] = cust_input.float_input(-1000000000, 1000000000, "Enter x0(from -1000000000 to 1000000000): \n")
    y[i, 0] = cust_input.float_input(-1000000000, 1000000000, "Enter y0(from -1000000000 to 1000000000): \n")

if key == 1:
    pp.get_phase_portrait_const(n, N, x, y, alpha_x, alpha_y)
elif key == 2:
    pp.get_phase_portrait_var_exp(n, N, x, y)
elif key == 3:
    pp.get_phase_portrait_var_norm(n, N, x, y)
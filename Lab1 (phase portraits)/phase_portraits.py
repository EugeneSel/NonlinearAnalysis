import matplotlib.pyplot as plt
import numpy as np

def P(x, y):
    return x ** 2 - y

def Q(x, y):
    return (x - y) * (x - y + 2)

def Vx_wave(Vx, Vy):
    return Vx/np.sqrt(Vx ** 2 + Vy ** 2)

def Vy_wave(Vx, Vy):
    return Vy/np.sqrt(Vx ** 2 + Vy ** 2)

def get_phase_portrait_const(n, N, x, y, alpha_x, alpha_y): # for constant alphas case
    for i in range(n):
        for k in range(N-1):
            Vx = P(x[i, k], y[i, k])
            Vy = Q(x[i, k], y[i, k])
            x[i, k + 1] = x[i, k] + alpha_x * Vx_wave(Vx, Vy)
            y[i, k + 1] = y[i, k] + alpha_y * Vy_wave(Vx, Vy)
        plt.plot(x[i], y[i], 'b')
    plt.axis([-3, 8, -3, 8])
    plt.show()

def get_phase_portrait_var_exp(n, N, x, y): # for alphas, varying by exponential law case
    for i in range(n):
        alpha = 0.001
        for k in range(N-1):
            Vx = P(x[i, k], y[i, k])
            Vy = Q(x[i, k], y[i, k])
            if k >= 1:
                alpha *= np.exp(np.abs((x[i, k] - x[i, k-1]) ** 2 + (y[i, k] - y[i, k-1]) ** 2))
            x[i, k + 1] = x[i, k] + alpha * Vx_wave(Vx, Vy)
            y[i, k + 1] = y[i, k] + alpha * Vy_wave(Vx, Vy)
        plt.plot(x[i], y[i], 'b')
    plt.axis([-3, 8, -3, 8])
    plt.show()

def get_phase_portrait_var_norm(n, N, x, y): # for alphas, varying by normalized law case
    for i in range(n):
        alpha = 0.001
        for k in range(N-1):
            Vx = P(x[i, k], y[i, k])
            Vy = Q(x[i, k], y[i, k])
            if k >= 2:
                alpha += np.sqrt((x[i, k] - x[i, k-1]) ** 2 + (y[i, k] - y[i, k-1]) ** 2) - np.sqrt((x[i, k-1] - x[i, k-2]) ** 2 + (y[i, k-1] - y[i, k-2]) ** 2)
            x[i, k + 1] = x[i, k] + alpha * Vx_wave(Vx, Vy)
            y[i, k + 1] = y[i, k] + alpha * Vy_wave(Vx, Vy)
        plt.plot(x[i], y[i], 'b')
    plt.axis([-3, 8, -3, 8])
    plt.show()

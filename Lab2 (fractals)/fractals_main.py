import matplotlib.pyplot as plt
from fractals import mandelbrot_set, julia_set, mandelbrot_set_trig
import numpy as np

# Mandelbrot fractals for power functions:
for i in range(2, 7):
    result = mandelbrot_set(256, 10, -2, 2, -1.5, 1.5, 640, 480, i)

# Mandelbrot fractals for trigonometric functions:
result = mandelbrot_set_trig(256, 10, 0, 8, -3, 3, 640, 480, np.sin)
result = mandelbrot_set_trig(256, 10, -2, 7, -3, 3, 640, 480, np.cos)
plt.show()

# variant 37:
# c = –0,711 + 0,571*i
# Julia fractals for power functions:
for i in range(2, 6):
    result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, i, -0.711, 0.571)

result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, 2, -0.711, 0)
result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, 5, 0, 0.571)

result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, 5, None, 0.571)
result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, 3, -0.711, None)
result = julia_set(256, 10, -2.5, 2.5, -2, 2, 640, 480, 4, None, None)
plt.show()

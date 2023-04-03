import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the potential function and the length of the well
def V(x):
    return 0.0 if 0 <= x <= L else np.inf

L = 1.0

# Define the time-independent part of the wave function
def psi_n(n, x):
    return np.sqrt(2/L) * np.sin(n * np.pi * x/L)

# Define the time-dependent part of the wave function
def phi_n(n, t):
    return np.exp(-1j * E_n(n) * t / hbar)

# Define the energy of the n-th energy state
def E_n(n):
    return (n**2 * np.pi**2 * hbar**2)/(2 * m * L**2)

# Define the time evolution of the wave function
def psi(x, t):
    return sum(psi_n(n, x) * phi_n(n, t) for n in range(1, N+1))

# Set up the animation
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1, 1)
ax.set_xlabel('x')
ax.set_ylabel('Probability density')
ax.set_title('Time evolution of a particle in an infinite square well potential')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = frame * dt
    y = np.abs(psi(x, t))**2
    line.set_data(x, y)
    return line,

# Set up the simulation parameters
N = 100
m = 1.0
hbar = 1.0
n_frames = 100
dt = 0.1
x = np.linspace(0, L, 1000)

# Create the animation
ani = FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True, repeat=False)

# Display the animation
plt.show()

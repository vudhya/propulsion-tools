# ============================================
# Day 6 Exercise: Parametric Nozzle Study
# ============================================
# Combine NumPy, Matplotlib, and functions to
# perform a real engineering parametric study.
# ============================================

import numpy as np
import matplotlib.pyplot as plt

# =============================================
# THE PROBLEM
# =============================================
# You are designing a rocket nozzle. You want to understand
# how Isp and exhaust velocity depend on TWO parameters:
#   1. Chamber pressure (Pc) — ranging from 20 to 300 bar
#   2. Gamma — ranging from 1.1 to 1.4
#      (different propellants have different gamma)
#
# Fixed values: R = 370 J/kg·K, Tc = 3500 K, Pe = 1 bar, g0 = 9.81

R = 370
Tc = 3500
Pe = 1      # bar
g0 = 9.81

# =============================================
# PART A: Write a function using NumPy
# =============================================

# Write a function: compute_isp(Pc, gamma, R, Tc, Pe)
# 
# This function should accept Pc as a NumPy ARRAY
# (not just a single number) and return an ARRAY of Isp values.
#
# This means: if you pass in an array of 50 pressures,
# you get back an array of 50 Isp values. No loops.
#
# The formula is the same as Day 1, but now it works on arrays.
# NumPy handles the array math automatically.

# YOUR CODE HERE

def compute_isp(Pc, gamma, R, Tc, Pe):
    term = (1 - (Pe/Pc)**((gamma-1)/gamma))
    Ve = np.sqrt((2*gamma/(gamma-1)) * R * Tc * term)
    Isp = Ve / g0
    return Isp


# =============================================
# PART B: Line Plot — Isp vs Pc for different gamma
# =============================================

# Create an array of Pc from 20 to 300 bar (100 points).
# For each gamma in [1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4]:
#   - Call your function to get the Isp array
#   - Plot Isp vs Pc with a label showing the gamma value
#
# HINT: Use a for loop over gamma values, not over Pc values.
# The NumPy function handles all Pc values at once.
#
# Add: xlabel, ylabel, title, legend, grid
# Save as 'isp_vs_pc.png'

# YOUR CODE HERE
Pc = np.linspace(20, 300, 100)
for gamma in [1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4]:
    Isp = compute_isp(Pc, gamma, R, Tc, Pe)
    plt.plot(Pc, Isp, label = f'gamma={gamma:.2f}')
plt.xlabel('Chamber Pressure (bar)')
plt.ylabel('Specific Impulse (s)')
plt.title('Isp vs Chamber Pressure for Different Gamma')
plt.legend(fontsize=8)
plt.grid(True)
plt.savefig('isp_vs_pc.png', dpi=200)
plt.show()


# =============================================
# PART C: Contour Plot — Isp as a function of both Pc AND gamma
# =============================================
# A contour plot shows a 2D map where color represents a third variable.
# Think of it as a topographic map, but instead of elevation,
# the color shows Isp.
#
# STEPS:
# 1. Create 1D arrays:
#    Pc_range = np.linspace(20, 300, 100)
#    gamma_range = np.linspace(1.1, 1.4, 100)
#
# 2. Create a 2D grid using np.meshgrid:
#    Pc_grid, gamma_grid = np.meshgrid(Pc_range, gamma_range)
#    This creates two 100x100 arrays. Every combination of Pc and gamma
#    is represented somewhere in these grids.
#
# 3. Compute Isp for the entire grid:
#    Isp_grid = compute_isp(Pc_grid, gamma_grid, R, Tc, Pe)
#    This works because NumPy does element-wise operations on arrays
#    of ANY shape — not just 1D.
#
# 4. Plot the contour:
#    plt.figure(figsize=(10, 7))
#    contour = plt.contourf(Pc_grid, gamma_grid, Isp_grid, levels=20, cmap='viridis')
#    plt.colorbar(contour, label='Isp (s)')
#    plt.xlabel('Chamber Pressure (bar)')
#    plt.ylabel('Gamma')
#    plt.title('Specific Impulse Map')
#    plt.savefig('isp_contour.png', dpi=200)
#    plt.show()
#
# 'cmap' is the color scheme. Try: 'viridis', 'plasma', 'inferno', 'coolwarm'
# 'levels=20' means 20 contour levels (more = smoother)

# YOUR CODE HERE
Pc_range = np.linspace(20, 200, 100)
gamma_range = np.linspace(1.1, 1.4, 100)
Pc_grid, gamma_grid = np.meshgrid(Pc_range, gamma_range)
Isp_grid = compute_isp(Pc_grid, gamma_grid, R, Tc, Pe)
plt.figure(figsize=(10, 7))
contour = plt.contourf(Pc_grid, gamma_grid, Isp_grid, levels = 20, cmap = 'viridis')
plt.colorbar(contour, label = 'Isp (s)')
plt.xlabel('Chamber Pressure (bar)')
plt.ylabel('Gamma')
plt.title('Specific Impulse Map')
plt.savefig('isp_contour.png', dpi=200)
plt.show()

# =============================================
# PART D: Find and mark the optimum
# =============================================
# After plotting the contour, find the maximum Isp in your grid.
#
# USEFUL NUMPY FUNCTIONS:
#   np.max(Isp_grid)               — maximum value in the entire grid
#   np.argmax(Isp_grid)            — index of the maximum (flattened)
#   np.unravel_index(flat_index, shape) — convert flat index to 2D index
#
# Example:
#   flat_idx = np.argmax(Isp_grid)
#   row, col = np.unravel_index(flat_idx, Isp_grid.shape)
#   best_Pc = Pc_grid[row, col]
#   best_gamma = gamma_grid[row, col]
#   best_Isp = Isp_grid[row, col]
#
# Print: "Maximum Isp = ??? s at Pc = ??? bar, gamma = ???"
#
# BONUS: Replot the contour and add a star marker at the optimum:
#   plt.plot(best_Pc, best_gamma, 'w*', markersize=15)  # white star

# YOUR CODE HERE
flat_idx = np.argmax(Isp_grid)
row, col = np.unravel_index(flat_idx, Isp_grid.shape)
best_Pc = Pc_grid[row, col]
best_gamma = gamma_grid[row, col]
best_Isp = Isp_grid[row, col]
print(f"Maximum Isp = {best_Isp:.2f} s at Pc = {best_Pc:.2f} bar, gamma = {best_gamma:.2f}")
plt.figure(figsize = (10, 7))
contour = plt.contourf(Pc_grid, gamma_grid, Isp_grid, levels = 20, cmap = 'viridis')
plt.colorbar(contour, label = 'Isp (s)')
plt.xlabel('Chamber Pressure (bar)')
plt.ylabel('Gamma')
plt.title('Specific Impulse Map')
plt.plot(best_Pc, best_gamma, 'w*', markersize = 15)
plt.savefig('isp_contour_optimum.png', dpi=200)
plt.show()


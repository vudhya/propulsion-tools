# ============================================
# Day 5 Exercise: NumPy + Matplotlib
# ============================================
# Rewrite your isentropic table using NumPy
# (no loops!) and then plot the results.
# ============================================

import numpy as np  # type: ignore[import]
import matplotlib.pyplot as plt  # type: ignore[import]

gamma = 1.4

# =============================================
# PART A: NumPy — Isentropic Table Without Loops
# =============================================

# --- Step 1: Create a Mach number array ---
# Remember Day 2? You used a while loop and .append() to build
# a list of 30 Mach numbers. With NumPy, it's one line:
#
# M = np.linspace(start, stop, number_of_points)

M = np.linspace(0.1, 3.0, 30)


# --- Step 2: Compute all four ratios — NO LOOPS ---
# On Day 2, you looped through each M and appended results.
# With NumPy, you write the formula ONCE and it computes
# for ALL 30 Mach numbers simultaneously.
#
# Example:
#   term = 1 + (gamma - 1) / 2 * M**2
# This creates an ARRAY of 30 values — one 'term' per Mach number.
# Then:
#   T_ratio = term ** (-1)
# This also creates an array of 30 values. No loop needed.

# YOUR CODE HERE
term = 1 + (gamma-1)/2 * M**2
T_ratio = term ** (-1)
P_ratio = term ** (-gamma/(gamma-1))
rho_ratio = term ** (-1/(gamma-1))
A_ratio = (1/M) * ((2/(gamma+1)) * term) ** ((gamma+1)/(2*(gamma-1)))


# --- Step 3: Print the table ---
# NumPy arrays support indexing just like lists.
# Loop through using: for i in range(len(M)):
# Print each row with M[i], T_ratio[i], etc.
#
# This part still uses a loop — but only for PRINTING.
# The COMPUTATION above had no loops. That's the key difference.

# YOUR CODE HERE
for i in range(len(M)):
    print(f"{M[i]:.1f} {T_ratio[i]:.4f} {P_ratio[i]:.4f} {rho_ratio[i]:.4f} {A_ratio[i]:.4f}")
    if M[i] == 1.0:
        print("-" * 40)  # Print a separator after M=1.0
    

# =============================================
# PART B: Matplotlib — Plotting
# =============================================

# --- Plot 1: All ratios on one plot ---
# Plot T/T0, P/P0, and rho/rho0 vs Mach number.
# (Don't include A/A* here — its scale is too different.)
#
# Requirements:
#   - Each line should have a label (for the legend)
#   - Add xlabel, ylabel, title
#   - Add legend
#   - Add grid
#   - Save the figure as 'isentropic_ratios.png'
#   - Then show it: plt.show()
#
# SYNTAX REMINDER:
#   plt.plot(x_array, y_array, label='name')
#   plt.xlabel('text')
#   plt.ylabel('text')
#   plt.title('text')
#   plt.legend()
#   plt.grid(True)
#   plt.savefig('filename.png', dpi=150)
#   plt.show()

# YOUR CODE HERE
plt.plot(M, T_ratio, label = 'T/T0')
plt.plot(M, P_ratio, label = 'P/P0')
plt.plot(M, rho_ratio, label = 'rho/rho0')
plt.xlabel('Mach')
plt.ylabel('Ratio')
plt.title('Isentropic Ratios vs Mach Number')
plt.legend()
plt.grid(True)
plt.savefig('isentropic_ratios.png', dpi=200)
plt.show()

# --- Plot 2: A/A* on a separate plot ---
# A/A* has a very different scale (goes up to ~5).
# Give it its own plot.
# Mark the minimum point (M=1, A/A*=1) with a red dot.
#
# SYNTAX for a single point:
#   plt.plot(x_value, y_value, 'ro', markersize=8)
#   ('ro' means red color, circle marker)

# YOUR CODE HERE
plt.plot(M, A_ratio, label = 'A/A*')
plt.plot(1, 1, 'ro', markersize = 8)
plt.xlabel('Mach')
plt.ylabel('A/A*')
plt.title('Area Ratio vs Mach Number')
plt.grid(True)
plt.savefig('area_ratio.png', dpi=200)
plt.show()

# --- Plot 3: 2x2 Subplot (all four ratios) ---
# Create a figure with 4 subplots arranged in a 2x2 grid.
# Each subplot shows ONE ratio vs Mach number.
#
# SYNTAX:
#   fig, axes = plt.subplots(2, 2, figsize=(10, 8))
#   
#   axes[0, 0].plot(M, T_ratio)        # top-left
#   axes[0, 0].set_title('T/T₀')
#   axes[0, 0].set_xlabel('Mach')
#   axes[0, 0].grid(True)
#
#   axes[0, 1].plot(M, P_ratio)        # top-right
#   axes[0, 1].set_title('P/P₀')
#   ...
#
#   axes[1, 0].plot(...)               # bottom-left
#   axes[1, 1].plot(...)               # bottom-right
#
#   plt.tight_layout()                 # prevents labels from overlapping
#   plt.savefig('isentropic_subplots.png', dpi=150)
#   plt.show()

# YOUR CODE HERE
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(M, T_ratio)
axes[0, 0].set_title('T/T0')
axes[0, 0].set_xlabel('Mach')
axes[0, 0].grid(True)

axes[0, 1].plot(M, P_ratio)
axes[0, 1].set_title('P/P0')
axes[0, 1].set_xlabel('Mach')
axes[0, 1].grid(True)

axes[1, 0].plot(M, rho_ratio)
axes[1, 0].set_title('rho/rho0')
axes[1, 0].set_xlabel('Mach')
axes[1, 0].grid(True)

axes[1, 1].plot(M, A_ratio)
axes[1, 1].set_title('A/A*')
axes[1, 1].set_xlabel('Mach')
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig('isentropic_subplots.png', dpi=200)
plt.show()
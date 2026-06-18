# ============================================
# Phase 1, Exercise 2: Parametric Study
# ============================================
# Calculate and plot the Adiabatic Flame Temperature (AFT)
# as a function of the Equivalence Ratio (phi).
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')

# Parametric Sweep: phi from 0.5 (lean) to 2.0 (rich)
phi_values = np.linspace(0.5, 2.0, 50)
T_aft = []

# Loop over equivalence ratios and equilibrate
for phi in phi_values:
    gas.set_equivalence_ratio(phi, 'CH4', 'O2:1.0, N2:3.76')
    gas.TP = 300, ct.one_atm
    gas.equilibrate('HP')
    T_aft.append(gas.T)

# Plot the Results
plt.figure(figsize=(8, 6))
plt.plot(phi_values, T_aft, marker='o', linestyle='-', color='b')
plt.xlabel('Equivalence Ratio (phi)')
plt.ylabel('Adiabatic Flame Temperature (K)')
plt.title('Adiabatic Flame Temperature vs Equivalence Ratio')
plt.grid()
plt.savefig('aft_vs_phi.png')
plt.show()

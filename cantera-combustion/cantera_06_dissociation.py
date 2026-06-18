# ============================================
# Phase 1: Species Dissociation
# ============================================
# Plot the equilibrium mole fractions of CO2, CO, and OH
# as a function of temperature to visualize dissociation.
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
T_list = np.linspace(1000, 3500, 50)
Temperature_axis = []
CO2_mole_fractions = []
CO_mole_fractions = []
OH_mole_fractions = []

for T in T_list:
    gas.TPX = T, ct.one_atm, 'CH4:1, O2:2, N2:7.52'
    gas.equilibrate('TP')
    
    x_co2 = gas.X[gas.species_index('CO2')]
    x_co = gas.X[gas.species_index('CO')]
    x_oh = gas.X[gas.species_index('OH')]
    
    Temperature_axis.append(T)
    CO2_mole_fractions.append(x_co2)
    CO_mole_fractions.append(x_co)
    OH_mole_fractions.append(x_oh)

plt.figure(figsize=(8, 6))
plt.plot(Temperature_axis, CO2_mole_fractions, label='CO2', linewidth=2)
plt.plot(Temperature_axis, CO_mole_fractions, label='CO', linewidth=2)
plt.plot(Temperature_axis, OH_mole_fractions, label='OH', linewidth=2)
plt.xlabel('Temperature (K)')
plt.ylabel('Mole Fraction')
plt.title('Equilibrium Mole Fractions vs Temperature')
plt.grid(True)
plt.legend()
plt.savefig('dissociation.png')

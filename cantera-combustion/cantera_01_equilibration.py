# ============================================
# Phase 1: Cantera Basics
# ============================================
# Computes the adiabatic flame temperature and 
# equilibrium composition of a stoichiometric 
# Methane-Air mixture at 1 atm and 300 K.
# ============================================

import cantera as ct

gas = ct.Solution('gri30.yaml')

# Print the number of species to verify it loaded correctly
print(f"Loaded mechanism with {gas.n_species} species.")

# Set the initial state (Stoichiometric Methane-Air)
gas.TPX = 300, ct.one_atm, 'CH4:1, O2:2, N2:7.52'

print("\n--- Initial State ---")
print(f"Temperature: {gas.T:.2f} K")
print(f"Pressure: {gas.P:.2f} Pa")
gas()

# Equilibrate holding Enthalpy (H) and Pressure (P) constant
gas.equilibrate('HP')

print("\n--- Burned State (Equilibrium) ---")
print(f"Adiabatic Flame Temperature: {gas.T:.2f} K")
print(f"Pressure: {gas.P:.2f} Pa")
gas()

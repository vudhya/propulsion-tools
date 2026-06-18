# ============================================
# Phase 1: Rocket Engine Specific Impulse
# ============================================
# Simulates a LOX/Methane engine (SpaceX Raptor specs).
# Calculates Chamber Temperature via HP equilibration,
# and Nozzle Exit parameters via Isentropic (SP) expansion.
# ============================================

import cantera as ct
import math

# Engine Parameters
Pc = 300 * 100000  # Chamber pressure in Pa
Pe = 1 * 100000    # Exit pressure in Pa
O_F_ratio = 3.6    # Oxidizer to Fuel mass ratio

gas = ct.Solution('gri30.yaml')

# Set mass fractions
Y_O2 = O_F_ratio / (O_F_ratio + 1)
Y_CH4 = 1 / (O_F_ratio + 1)

gas.TPY = 300, Pc, f"CH4:{Y_CH4}, O2:{Y_O2}"

# --- Combustion Chamber (Constant Enthalpy & Pressure) ---
gas.equilibrate('HP')

Tc = gas.T
hc = gas.enthalpy_mass  

print(f"--- Combustion Chamber ---")
print(f"Temperature (Tc): {Tc:.2f} K")
print(f"Enthalpy (hc): {hc:.2f} J/kg")

# --- Nozzle Expansion (Isentropic: Constant Entropy) ---
gas.SP = gas.entropy_mass, Pe
gas.equilibrate('SP')

Te = gas.T
he = gas.enthalpy_mass

print(f"\n--- Nozzle Exit ---")
print(f"Temperature (Te): {Te:.2f} K")
print(f"Enthalpy (he): {he:.2f} J/kg")

# --- Engine Performance ---
g = 9.81
V_exit = math.sqrt(2 * (hc - he))
Isp = V_exit / g

print(f"\n--- Engine Performance ---")
print(f"Exhaust Velocity (V_exit): {V_exit:.2f} m/s")
print(f"Specific Impulse (Isp): {Isp:.2f} s")

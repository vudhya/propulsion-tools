# ============================================
# Phase 1: 1D Laminar Flame Speed
# ============================================
# Simulates a 1D freely propagating flame to find
# the laminar flame speed of Methane-Air.
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
gas.TPX = 300, ct.one_atm, 'CH4:1, O2:2, N2:7.52'

flame = ct.FreeFlame(gas, width=0.03)
flame.set_refine_criteria(ratio=3, slope=0.06, curve=0.12)

flame.solve(loglevel=1, auto=True)

Su = flame.velocity[0]
x_grid = flame.grid
T_profile = flame.T

print(f"Laminar Flame Speed (Su): {Su * 100:.2f} cm/s")

plt.figure(figsize=(8, 6))
plt.plot(x_grid * 100, T_profile, color='m')
plt.xlabel('Distance (cm)')
plt.ylabel('Temperature (K)')
plt.title('1D Laminar Flame Profile')
plt.grid(True)
plt.savefig('flame_profile.png')

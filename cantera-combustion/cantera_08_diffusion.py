# ============================================
# Phase 1: Counterflow Diffusion Flame
# ============================================
# Simulate a non-premixed flame where fuel and oxidizer
# are injected from opposite sides (e.g. Rocket Injector).
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
gas.TP = 300, ct.one_atm
flame = ct.CounterflowDiffusionFlame(gas, width=0.02)

flame.fuel_inlet.mdot = 0.2
flame.fuel_inlet.X = 'CH4:1.0'
flame.fuel_inlet.T = 300

flame.oxidizer_inlet.mdot = 0.2
flame.oxidizer_inlet.X = 'O2:1.0'
flame.oxidizer_inlet.T = 300

flame.set_refine_criteria(ratio=3, slope=0.05, curve=0.05)
flame.solve(loglevel=1, auto=True)

x_grid = flame.grid * 100
T_profile = flame.T

plt.figure(figsize=(8, 6))
plt.plot(x_grid, T_profile, color='orange', linewidth=2)
plt.xlabel('Distance (cm)')
plt.ylabel('Temperature (K)')
plt.title('Counterflow Diffusion Flame Temperature Profile')
plt.grid(True)
plt.savefig('diffusion_flame.png')

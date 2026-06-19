# ============================================
# Phase 1: The Arrhenius Curve
# ============================================
# Calculate ignition delay across multiple temperatures
# and plot log(delay) vs 1000/T to find the global
# activation energy slope.
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
T_initial = np.linspace(1000, 1500, 10)
ignition_delays = []

for T in T_initial:
    gas.TPX = T, ct.one_atm, 'CH4:1, O2:2, N2:7.52'
    reactor = ct.IdealGasConstPressureReactor(gas)
    sim = ct.ReactorNet([reactor])
    
    current_time = 0.0
    while gas.T < (T + 400):
        current_time = sim.step()
        
    ignition_delays.append(current_time)

inverse_T = 1000.0 / T_initial
log_delay = np.log10(ignition_delays)

plt.figure(figsize=(8, 6))
plt.plot(inverse_T, log_delay, marker='o', linestyle='-', linewidth=2)
plt.xlabel('1000 / T (1/K)')
plt.ylabel('log10(Ignition Delay [s])')
plt.title('Arrhenius Plot of Ignition Delay')
plt.grid(True)
plt.savefig('arrhenius.png')

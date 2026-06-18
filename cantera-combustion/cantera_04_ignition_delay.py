# ============================================
# Phase 1: Ignition Delay Time
# ============================================
# Simulates a constant-pressure reactor over time
# to determine the ignition delay of a mixture
# using finite-rate chemical kinetics.
# ============================================

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
gas.TPX = 1000, ct.one_atm, 'CH4:1, O2:2, N2:7.52'

reactor = ct.IdealGasConstPressureReactor(gas)
sim = ct.ReactorNet([reactor])

times = np.linspace(0, 3.0, 1000)
time_history = []
temp_history = []

for current_time in times:
    sim.advance(current_time)
    time_history.append(current_time)
    temp_history.append(gas.T)

plt.figure(figsize=(8, 6))
plt.plot(time_history, temp_history, color='r')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Ignition Delay Simulation')
plt.grid(True)
plt.savefig('ignition_delay.png')

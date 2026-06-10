# ============================================
# Day 1 Exercise: Rocket Exhaust Velocity
# ============================================
# Calculate the ideal exhaust velocity of a
# converging-diverging nozzle and the specific
# impulse (Isp).
# ============================================

# Given values for a LOX/methane-like engine
gamma = 1.3         # ratio of specific heats (dimensionless)
R = 360             # specific gas constant (J/kg·K)
Tc = 3500           # chamber temperature (K)
Pc = 70             # chamber pressure (bar)
Pe = 1              # exit pressure (bar)
g0 = 9.81           # gravitational acceleration (m/s²)

b1 = 2 * gamma / (gamma - 1)
b2 = R * Tc
pressure_ratio = Pe / Pc
exponent = (gamma - 1) / gamma
bracket_term = 1 - (pressure_ratio ** exponent)
Ve = (b1 * b2 * bracket_term) ** 0.5
Isp = Ve / g0
print(f"Exhaust Velocity: {Ve:.2f} m/s")
print(f"Specific Impulse: {Isp:.2f} s")

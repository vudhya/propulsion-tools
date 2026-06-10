# ============================================
# Day 1 Exercise: Rocket Exhaust Velocity
# ============================================
# Calculate the ideal exhaust velocity of a
# converging-diverging nozzle and the specific
# impulse (Isp).
# ============================================

# --- Step 1: Define your variables ---
# Given values for a LOX/methane-like engine
gamma = 1.3         # ratio of specific heats (dimensionless)
R = 360             # specific gas constant (J/kg·K)
Tc = 3500           # chamber temperature (K)
Pc = 70             # chamber pressure (bar)
Pe = 1              # exit pressure (bar)
g0 = 9.81           # gravitational acceleration (m/s²)

# --- Step 2: Compute the exhaust velocity ---
# The formula:
# Ve = sqrt( (2*gamma/(gamma-1)) * R * Tc * (1 - (Pe/Pc)**((gamma-1)/gamma)) )
#
# HINT: Break it into parts. For example:
#   pressure_ratio = Pe / Pc
#   exponent = ???
#   bracket_term = ???
#   Ve = ???

# YOUR CODE HERE — replace the lines below
b1 = 2 * gamma / (gamma - 1)
b2 = R * Tc
pressure_ratio = Pe / Pc
exponent = (gamma - 1) / gamma
bracket_term = 1 - (pressure_ratio ** exponent)
Ve = (b1 * b2 * bracket_term) ** 0.5

# --- Step 3: Compute specific impulse ---
# Isp = Ve / g0

# YOUR CODE HERE
Isp = Ve / g0


# --- Step 4: Print the results ---
# Use f-strings to print Ve and Isp with units, 2 decimal places
# Example: print(f"Exhaust Velocity: {Ve:.2f} m/s")

# YOUR CODE HERE
print(f"Exhaust Velocity: {Ve:.2f} m/s")
print(f"Specific Impulse: {Isp:.2f} s")

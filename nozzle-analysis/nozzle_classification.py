# ============================================
# Day 1 Exercise 2: Nozzle Flow Classification
# ============================================
# For a range of exit pressures, compute the
# pressure ratio and classify the flow regime.
# ============================================

# --- Given ---
Pc = 70     # chamber pressure (bar)
gamma = 1.4 # ratio of specific heats

# Critical pressure ratio (for choked flow):
# P_star / Pc = (2 / (gamma + 1)) ** (gamma / (gamma - 1))
# Compute this value and store it as 'critical_ratio'

# YOUR CODE HERE
coeff = (2 / (gamma + 1))
exponent = (gamma / (gamma - 1))
critical_ratio = coeff ** exponent  # P_star / Pc

# --- Loop through these exit pressures ---
exit_pressures = [70, 50, 40, 37, 20, 10, 5, 1, 0.5]

# For each Pe in the list:
#   1. Compute the pressure ratio: ratio = Pe / Pc
#   2. Compare with critical_ratio to classify:
#      - If ratio == 1.0     → print "No flow"
#      - If ratio > critical_ratio → print "Subsonic (not choked)"
#      - If ratio is approximately equal to critical_ratio (within 0.01) → print "Choked (M=1 at throat)"
#      - If ratio < critical_ratio → print "Supersonic (choked + expansion)"
#   3. Print: Pe, ratio (4 decimal places), and the classification
#
# Expected output format:
#   Pe = 70.0 bar | Pe/Pc = 1.0000 | No flow
#   Pe = 50.0 bar | Pe/Pc = 0.7143 | Subsonic (not choked)
#   ...

for Pe in exit_pressures:
    ratio = Pe / Pc
    if ratio == 1:
        print(f"Pe = {Pe: .1f} bar | Pe/Pc = {ratio: .4f} | No flow")
    elif abs(ratio - critical_ratio) <= 0.01:
        print(f"Pe = {Pe: .1f} bar | Pe/Pc = {ratio: .4f} | Choked (M=1 at throat)")
    elif ratio > critical_ratio:
        print(f"Pe = {Pe: .1f} bar | Pe/Pc = {ratio: .4f} | Subsonic (not choked)")
    else:
        print(f"Pe = {Pe: .1f} bar | Pe/Pc = {ratio: .4f} | Supersonic (choked + expansion)")



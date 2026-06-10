# ============================================
# Day 1 Exercise 2: Nozzle Flow Classification
# ============================================
# For a range of exit pressures, compute the
# pressure ratio and classify the flow regime.
# ============================================

# --- Given ---
Pc = 70     # chamber pressure (bar)
gamma = 1.4 # ratio of specific heats

coeff = (2 / (gamma + 1))
exponent = (gamma / (gamma - 1))
critical_ratio = coeff ** exponent  # P_star / Pc
exit_pressures = [70, 50, 40, 37, 20, 10, 5, 1, 0.5]

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



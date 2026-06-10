# ============================================
# Day 2 Exercise: Isentropic Flow Table Generator
# ============================================
# Generate a complete isentropic flow properties
# table, like the ones in your gas dynamics textbook.
# ============================================

# --- Given ---
gamma = 1.4

# --- Step 1: Create a list of Mach numbers ---
# You need Mach numbers from 0.1 to 3.0 in steps of 0.1
# 
# You can't just write all 30 numbers by hand. Use a loop:
#   mach_numbers = []
#   start with M = 0.1
#   keep adding 0.1 until you reach 3.0
#   append each M to the list
#
# (In Week 3 you'll learn np.arange() which does this in one line.
#  For now, build the list with a loop — understand the manual way first.)

mach_numbers = []
for i in range(1,31):
    M = i * 0.1
    mach_numbers.append(M)



# --- Step 2: For each Mach number, compute these ratios ---
# Store each result in its own list.
#
# T/T0 = (1 + (gamma-1)/2 * M^2) ^ (-1)
# P/P0 = (1 + (gamma-1)/2 * M^2) ^ (-gamma/(gamma-1))
# rho/rho0 = (1 + (gamma-1)/2 * M^2) ^ (-1/(gamma-1))
# A/A* = (1/M) * ((2/(gamma+1)) * (1 + (gamma-1)/2 * M^2)) ^ ((gamma+1)/(2*(gamma-1)))
#
# HINT: The term (1 + (gamma-1)/2 * M^2) appears in ALL four formulas.
#       Compute it once, store it, reuse it. Don't repeat yourself.

T_ratios = []
P_ratios = []
rho_ratios = []
A_ratios = []
for M in mach_numbers:
    term = (1 + (gamma -1)/2 * M**2)
    T_ratio = term ** (-1)
    P_ratio = term ** (-gamma/(gamma-1))
    rho_ratio = term ** (-1/(gamma-1))
    A_ratio = (1/M) * ((2/(gamma+1)) * term) ** ((gamma+1)/(2*(gamma-1)))
    T_ratios.append(T_ratio)
    P_ratios.append(P_ratio)
    rho_ratios.append(rho_ratio)
    A_ratios.append(A_ratio)



# --- Step 3: Print a formatted table ---
# Header:
#   M       T/T0     P/P0     rho/rho0   A/A*
#   -----   ------   ------   --------   ------
# Then each row with proper alignment and 4 decimal places.
#
# HINT: You'll need to loop through all lists at the same time.
#       Use: for i in range(len(mach_numbers)):
#       Then access mach_numbers[i], T_ratio[i], etc.
print(f"{'M':<8} {'T/T0':<8} {'P/P0':<8} {'rho/rho0':<10} {'A/A*':<8}")
print("-" * 40)

for i in range(len(mach_numbers)):
    print(f"{mach_numbers[i]:<8.1f} {T_ratios[i]:<8.4f} {P_ratios[i]:<8.4f} {rho_ratios[i]:<10.4f} {A_ratios[i]:<8.4f}")
    if mach_numbers[i] == 1.0:
        print(f"At M=1.0: T/T0={T_ratios[i]:.4f}, P/P0={P_ratios[i]:.4f}, rho/rho0={rho_ratios[i]:.4f}")



# --- Step 4: Find and print the values at M = 1.0 ---
# At M = 1.0 (the critical condition), print T*/T0, P*/P0, rho*/rho0
# These are the critical ratios you should know from your coursework.
#
# To find M=1.0 in your list, loop through and check.
# (Week 3 will teach you cleaner ways to do this.)




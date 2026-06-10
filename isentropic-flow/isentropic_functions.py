# ============================================
# Day 3 Exercise: Functions — Isentropic Flow
# ============================================
# Refactor your isentropic table code into
# reusable functions. Then use them to solve
# actual engineering problems.
# ============================================

# --- Part A: Write the functions ---

# Function 1: isentropic_ratios(M, gamma)
# Takes: Mach number and gamma
# Returns: T_ratio, P_ratio, rho_ratio, A_ratio (all four)
#
# SYNTAX for returning multiple values:
#   def my_function(x, y):
#       a = x + y
#       b = x * y
#       return a, b
#
# SYNTAX for receiving multiple values:
#   sum_val, product_val = my_function(3, 4)

def isentropic_ratios(M, gamma):
    term = (1 + (gamma -1)/2 * M**2)
    T_ratio = term**(-1)
    P_ratio = term**(-gamma/(gamma-1))
    rho_ratio = term**(-1/(gamma-1))
    A_ratio = (1/M) * ((2/(gamma+1)) * term) ** ((gamma+1)/(2*(gamma-1)))
    return T_ratio, P_ratio, rho_ratio, A_ratio


    


# Function 2: mach_from_area_ratio(A_ratio, gamma, supersonic=False)
# Takes: A/A* ratio and gamma
# Returns: the Mach number
#
# This is the INVERSE problem — given A/A*, find M.
# There is no clean algebraic solution, so use ITERATION:
#
#   Start with a guess for M (0.01 for subsonic, 1.5 for supersonic)
#   Compute A/A* for that guess using your function from Part A
#   If the computed A/A* is too high, adjust M
#   If too low, adjust the other way
#   Repeat until the error is small enough (< 0.0001)
#
# Use BISECTION METHOD:
#   - For subsonic: M is between 0.01 and 1.0
#   - For supersonic: M is between 1.0 and 50.0
#   - Midpoint: M_mid = (M_low + M_high) / 2
#   - If A/A* at M_mid is too high → adjust M_low or M_high
#   - Repeat until |computed_A - target_A| < 0.0001
#
# HINT: A/A* DECREASES from M=0 to M=1, then INCREASES from M=1 onward.
#       So the bisection logic is different for subsonic vs supersonic.
#
# This function uses a "default argument": supersonic=False
# Call it as: mach_from_area_ratio(2.0, 1.4)               → subsonic M
# Or:         mach_from_area_ratio(2.0, 1.4, supersonic=True) → supersonic M

def mach_from_area_ratio(A_ratio, gamma, supersonic=False):
    if supersonic:
        M_low = 1.0
        M_high = 50.0
    else:
        M_low = 0.01
        M_high = 1.0
    while True:
        M_mid = (M_low + M_high)/2
        _, _, _, A_mid = isentropic_ratios(M_mid, gamma)
        if abs(A_mid - A_ratio) < 0.0001:
            return M_mid
        if supersonic:
            if A_mid > A_ratio:
                M_high = M_mid
            else:
                M_low = M_mid
        else:
            if A_mid > A_ratio:
                M_low = M_mid
            else:
                M_high = M_mid
    return M_mid  # This line is never reached, but it satisfies the function syntax
print(mach_from_area_ratio(2.0, 1.4))  # Should give subsonic M
print(mach_from_area_ratio(2.0, 1.4, supersonic=True))  # Should give supersonic M





# --- Part B: Use your functions to solve problems ---

gamma = 1.4

# Problem 1: A nozzle has a throat area of 0.5 m² and an exit area of 1.5 m².
# What is A/A*? What are the two possible exit Mach numbers (subsonic and supersonic)?
# For each, compute all isentropic ratios.

throat_area = 0.5
exit_area = 1.5
A_ratio = exit_area / throat_area
M_sub = mach_from_area_ratio(A_ratio, gamma)
M_sup = mach_from_area_ratio(A_ratio, gamma, supersonic=True)
print(f"A/A* = {A_ratio:.4f}")
print(f"Subsonic M = {M_sub:.4f}")
print(f"Supersonic M = {M_sup:.4f}")
T_sub, P_sub, rho_sub, _ = isentropic_ratios(M_sub, gamma)
T_sup, P_sup, rho_sup, _ = isentropic_ratios(M_sup, gamma)
print(f"Subsonic ratios: T/T0={T_sub:.4f}, P/P0={P_sub:.4f}, rho/rho0={rho_sub:.4f}")
print(f"Supersonic ratios: T/T0={T_sup:.4f}, P/P0={P_sup:.4f}, rho/rho0={rho_sup:.4f}")



# Problem 2: A wind tunnel needs to produce M = 2.5 flow in the test section.
# If the test section area is 1.0 m², what must the throat area be?
# What are the pressure and temperature in the test section if the
# stagnation conditions are T0 = 300 K and P0 = 5 atm?

test_section_area = 1.0
M_test = 2.5
T0 = 300 #K
P0 = 5 #atm
T_ratio_test, P_ratio_test, rho_ratio_test, A_ratio_test = isentropic_ratios(M_test, gamma)
throat_area_test = test_section_area / A_ratio_test
T_test = T_ratio_test * T0   # Concise way of writing is: T_ratio_test *= T0
P_test = P_ratio_test * P0
print(f"Throat area needed: {throat_area_test:.4f} m²")
print(f"Test section conditions: T={T_test:.2f} K, P={P_test:.2f} atm")


# Problem 3: Print a mini-table for these specific area ratios: 1.0, 1.5, 2.0, 3.0, 5.0
# For each, show both the subsonic AND supersonic Mach numbers.
# Format:
#   A/A*    M_sub    M_sup
#   1.000   1.0000   1.0000
#   1.500   ???      ???
#   ...

area_ratios = [1.0, 1.5, 2.0, 3.0, 5.0]
print(f"{ 'A/A*':<8} {'M_sub':<8} {'M_sup':<8}")
print("-" * 24)
for A_ratio in area_ratios:
    M_sub = mach_from_area_ratio(A_ratio, gamma)
    M_sup = mach_from_area_ratio(A_ratio, gamma, supersonic=True)
    print(f"{A_ratio:<8.3f} {M_sub:<8.4f} {M_sup:<8.4f}")
    


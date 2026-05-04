# ── REAL SUPPLY CHAIN EXAMPLE ──
# Minimize procurement cost across 3 suppliers
# meeting demand of 1000 units

from scipy.optimize import linprog

# Cost per unit from each supplier
# Supplier A: $10, B: $12, C: $9
costs = [10, 12, 9]

# Constraints:
# 1. Total supply must meet demand: A + B + C >= 1000
# 2. Supplier A max capacity: A <= 400
# 3. Supplier B max capacity: B <= 500
# 4. Supplier C max capacity: C <= 300

# For >= constraint negate it
constraints_ub = [
    [-1, -1, -1],  # -(A+B+C) <= -1000 (demand)
    [1,  0,  0],   # A <= 400
    [0,  1,  0],   # B <= 500
    [0,  0,  1],   # C <= 300
]

rhs = [-1000, 400, 500, 300]

bounds = [(0, None), (0, None), (0, None)]

result = linprog(
    c=costs,
    A_ub=constraints_ub,
    b_ub=rhs,
    bounds=bounds,
    method='highs'
)

print(f"Minimum Cost:     ${result.fun:.2f}")
print(f"Order from A:     {result.x[0]:.0f} units")
print(f"Order from B:     {result.x[1]:.0f} units")
print(f"Order from C:     {result.x[2]:.0f} units")
print(f"Total units:      {sum(result.x):.0f} units")
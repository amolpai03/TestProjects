# ── LINEAR PROGRAMMING ──
# Using scipy.optimize.linprog
from scipy.optimize import linprog

# Problem:
# Maximize: 5A + 4B (profit)
# Subject to:
#   6A + 4B <= 24  (machine hours)
#   1A + 2B <= 6   (labor hours)
#   A, B >= 0

# NOTE: linprog MINIMIZES by default
# So negate the objective to maximize
objective = [-5, -4]  # negated for maximization

# Constraint matrix (left hand side)
constraints = [
    [6, 4],   # machine hours
    [1, 2]    # labor hours
]

# Right hand side
rhs = [24, 6]

# Bounds for variables (>= 0)
bounds = [(0, None), (0, None)]

# Solve
result = linprog(
    c=objective,
    A_ub=constraints,
    b_ub=rhs,
    bounds=bounds,
    method='highs'
)

# Results
print(f"Status:           {result.message}")
print(f"Max Profit:       ${-result.fun:.2f}")  # negate back
print(f"Units Product A:  {result.x[0]:.2f}")
print(f"Units Product B:  {result.x[1]:.2f}")
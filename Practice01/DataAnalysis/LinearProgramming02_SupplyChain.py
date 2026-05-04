# ── REAL SUPPLY CHAIN EXAMPLE USING PuLP ──
# Minimize procurement cost across 3 suppliers
# meeting demand of 1000 units

from pulp import *

# Create problem
prob = LpProblem("Minimize_Procurement_Cost", LpMinimize)

# Decision variables — units to order from each supplier
A = LpVariable("Supplier_A", lowBound=0)
B = LpVariable("Supplier_B", lowBound=0)
C = LpVariable("Supplier_C", lowBound=0)

# Objective function — minimize total cost
prob += 10*A + 12*B + 9*C

# Constraints
prob += A + B + C >= 1000   # must meet total demand
prob += A <= 400             # Supplier A max capacity
prob += B <= 500             # Supplier B max capacity
prob += C <= 300             # Supplier C max capacity

# Solve
prob.solve(PULP_CBC_CMD(msg=0))

# Results
print(f"Status:        {LpStatus[prob.status]}")
print(f"Minimum Cost:  ${value(prob.objective):,.2f}")
print(f"Order from A:  {value(A):.0f} units @ $10/unit")
print(f"Order from B:  {value(B):.0f} units @ $12/unit")
print(f"Order from C:  {value(C):.0f} units @ $9/unit")
print(f"Total units:   {value(A) + value(B) + value(C):.0f} units")
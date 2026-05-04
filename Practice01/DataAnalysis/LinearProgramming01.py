# Install first
# pip install pulp

from pulp import *

# Create problem
prob = LpProblem("Maximize_Profit", LpMaximize)

# Decision variables
A = LpVariable("Product_A", lowBound=0)
B = LpVariable("Product_B", lowBound=0)

# Objective function (maximize)
prob += 5*A + 4*B

# Constraints
prob += 6*A + 4*B <= 24   # machine hours
prob += 1*A + 2*B <= 6    # labor hours

# Solve
prob.solve(PULP_CBC_CMD(msg=0))

# Results
print(f"Status:          {LpStatus[prob.status]}")
print(f"Max Profit:      ${value(prob.objective):.2f}")
print(f"Units Product A: {value(A):.2f}")
print(f"Units Product B: {value(B):.2f}")
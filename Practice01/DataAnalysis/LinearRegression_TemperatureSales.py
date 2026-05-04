# ── SIMPLE LINEAR REGRESSION ──
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
temperature = [60, 65, 70, 75, 80, 85, 90, 95]
sales       = [100, 120, 140, 160, 200, 220, 260, 280]

# Create dataframe
df = pd.DataFrame({'temperature': temperature, 'sales': sales})

# Print data to verify
print("Data:")
print(df)

# Features and target
X = df[['temperature']]  # DataFrame — keeps column name
y = df['sales']

# Build model
model = LinearRegression()
model.fit(X, y)

# Results
print(f"\nIntercept:   {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"R-squared:   {model.score(X, y):.4f}")

# Predict at 88 degrees
# ✅ Use DataFrame to avoid warning
new_data = pd.DataFrame({'temperature': [88]})
predicted = model.predict(new_data)
print(f"Predicted sales at 88F: {predicted[0]:.1f} units")

# Plot
plt.scatter(temperature, sales, color='blue', label='Actual', s=100)
plt.plot(temperature, model.predict(X), color='red',
         label='Regression Line', linewidth=2)
plt.xlabel('Temperature (F)')
plt.ylabel('Sales (units)')
plt.title('Sales vs Temperature — Linear Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
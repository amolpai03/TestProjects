# ── MULTIPLE REGRESSION ──
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Sample data
data = pd.DataFrame({
    'sales':       [100, 150, 200, 180, 220, 300, 250, 190],  # ← add 8th row
    'temperature': [60,  70,  80,  75,  85,  90,  88,  72],
    'promotion':   [0,   0,   1,   0,   1,   1,   0,   0],
    'weekend':     [0,   1,   0,   1,   0,   1,   1,   0]
})

# Features and target
X = data[['temperature', 'promotion', 'weekend']]
y = data['sales']

# Using statsmodels for detailed output (like R's summary)
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const).fit()

# Detailed summary
print(model.summary())

# Predict: 85 degrees, promotion on, weekend
new = pd.DataFrame({
    'const':       [1],
    'temperature': [85],
    'promotion':   [1],
    'weekend':     [1]
})
prediction = model.predict(new)
print(f"\nPredicted sales: {prediction[0]:.1f} units")
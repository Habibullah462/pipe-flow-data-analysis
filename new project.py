import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. read the experimental data ---
data = pd.read_csv("flow_data.csv")
x = data["flow_rate_m3s"]
y = data["pressure_drop_Pa"]

# --- 2. fit a model: pressure drop is expected to go as k * Q^2 ---
# we fit y = k * x^2 by least squares (find the k that best fits the data)
k = np.sum(x**2 * y) / np.sum(x**4)      # least-squares fit for y = k*x^2
y_fit = k * x**2                          # predicted pressure drop from the fit

# --- 3. measure how good the fit is (R-squared) ---
ss_res = np.sum((y - y_fit)**2)           # leftover error
ss_tot = np.sum((y - np.mean(y))**2)      # total spread in the data
r_squared = 1 - ss_res / ss_tot

# --- 4. plot measured data vs fitted model ---
x_line = np.linspace(x.min(), x.max(), 100)   # smooth x values for the curve
y_line = k * x_line**2

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="black", label="Measured data")
plt.plot(x_line, y_line, color="red", label=f"Fit: ΔP = {k:.0f}·Q²")
plt.xlabel("Flow rate, Q (m³/s)")
plt.ylabel("Pressure drop, ΔP (Pa)")
plt.title("Pressure drop vs flow rate — measured vs fitted model")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("pressure_drop_plot.png", dpi=150, bbox_inches="tight")
plt.show()

# --- 5. print a short summary ---
print(f"Fitted coefficient k = {k:.1f} Pa·s²/m⁶")
print(f"R-squared = {r_squared:.4f}")
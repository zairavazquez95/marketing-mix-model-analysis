import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load data
df = pd.read_csv("marketing_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Features
X = df[["paid_social_spend", "search_spend", "display_spend", "audio_spend"]]

# Target
y = df["conversions"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Get coefficients
coefficients = pd.DataFrame({
    "Channel": X.columns,
    "Impact_on_Conversions": model.coef_
})

print("\nChannel Impact:")
print(coefficients)

# Predict conversions
df["predicted_conversions"] = model.predict(X)

print("\nSample Predictions:")
print(df[["conversions", "predicted_conversions"]].head())

# Total spend + CPA
df["total_spend"] = (
    df["paid_social_spend"] +
    df["search_spend"] +
    df["display_spend"] +
    df["audio_spend"]
)

df["CPA"] = df["total_spend"] / df["conversions"]

print("\nAverage CPA:")
print(round(df["CPA"].mean(), 2))

# Budget scenario based on your actual results:
# Audio and Paid Social had the strongest impact
scenario = X.copy()
scenario["audio_spend"] = scenario["audio_spend"] * 1.15
scenario["paid_social_spend"] = scenario["paid_social_spend"] * 1.10
scenario["search_spend"] = scenario["search_spend"] * 0.90
scenario["display_spend"] = scenario["display_spend"] * 0.90

scenario_predictions = model.predict(scenario)

original_conversions = df["conversions"].sum()
new_predicted_conversions = scenario_predictions.sum()
lift = ((new_predicted_conversions - original_conversions) / original_conversions) * 100

print("\nBudget Reallocation Scenario:")
print("Original total conversions:", round(original_conversions, 2))
print("New predicted conversions:", round(new_predicted_conversions, 2))
print("Predicted lift:", round(lift, 2), "%")

# Chart 1: Actual vs Predicted
plt.figure()
plt.plot(df.index + 1, df["conversions"], marker="o", label="Actual Conversions")
plt.plot(df.index + 1, df["predicted_conversions"], marker="o", label="Predicted Conversions")
plt.title("Actual vs Predicted Conversions")
plt.xlabel("Day")
plt.ylabel("Conversions")
plt.legend()
plt.tight_layout()
plt.savefig("images/actual_vs_predicted_conversions.png")
plt.close()

# Chart 2: Channel Impact
plt.figure()
plt.bar(coefficients["Channel"], coefficients["Impact_on_Conversions"])
plt.title("Estimated Channel Impact on Conversions")
plt.xlabel("Channel")
plt.ylabel("Regression Coefficient")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("images/channel_impact.png")
plt.close()

# Chart 3: CPA Over Time
plt.figure()
plt.plot(df.index + 1, df["CPA"], marker="o")
plt.title("CPA Over Time")
plt.xlabel("Day")
plt.ylabel("CPA")
plt.tight_layout()
plt.savefig("images/cpa_over_time.png")
plt.close()

# Export files
df.to_csv("campaign_performance_output.csv", index=False)
coefficients.to_csv("channel_impact_output.csv", index=False)

print("\nFiles created:")
print("- images/actual_vs_predicted_conversions.png")
print("- images/channel_impact.png")
print("- images/cpa_over_time.png")
print("- campaign_performance_output.csv")
print("- channel_impact_output.csv")
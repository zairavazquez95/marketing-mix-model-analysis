# Marketing Mix Model (MMM-lite)

## Overview  
I built this project to better understand how different marketing channels contribute to conversions beyond just looking at spend.

The goal was to simulate a simplified Marketing Mix Model and use it to evaluate channel performance, identify inefficiencies, and explore how budget decisions could impact results.

---

## The Question  
Which channels are driving conversions, and where are we potentially overspending?

---

## Data  
The dataset includes daily spend across:
- Paid Social  
- Search  
- Display  
- Audio  

along with total conversions.

---

## What I Did  

I started by analyzing overall campaign performance:
- total spend  
- CPA trends  
- conversion patterns over time  

From there, I built a regression model to estimate how each channel’s spend relates to conversions and to get a directional sense of impact.

To make the analysis more actionable, I tested a budget reallocation scenario by increasing investment in higher-impact channels and reducing spend in lower-impact ones.

---

## What I Found  

- Audio showed the strongest relationship with conversions, followed by Paid Social  
- Search and Display contributed to overall spend but showed lower marginal impact in this model  
- The model was able to closely approximate actual conversions, suggesting a reasonable fit for directional analysis  

> Based on this dataset, reallocating budget toward higher-impact channels like Audio and Paid Social would likely improve overall conversion efficiency.

---

## Takeaway  

The analysis suggests an opportunity to rebalance spend toward higher-performing channels. In this case, Audio and Paid Social appear to drive the strongest conversion impact, while Search and Display may be candidates for optimization or reduced allocation.

---

## Outputs  

The analysis generates:
- Actual vs. predicted conversions  
- Estimated channel impact (regression coefficients)  
- CPA trends over time  
- Budget reallocation scenario and projected lift  

### Channel Impact  
<img width="640" height="480" alt="channel_impact" src="https://github.com/user-attachments/assets/47365722-74ad-4432-83ba-a8b5a1ca6b93" />



### Actual vs Predicted Conversions  
<img width="640" height="480" alt="actual_vs_predicted_conversions" src="https://github.com/user-attachments/assets/d08337fb-7d3d-49fd-9753-82759dae9705" />


### CPA Over Time  
<img width="640" height="480" alt="cpa_over_time" src="https://github.com/user-attachments/assets/102f6052-ccad-4c65-8bc9-c3c3b9ce12fc" />


---

## Tools  
- Python  
- Pandas  
- scikit-learn  
- Matplotlib  

---

## How to run  

Install dependencies:

    pip install -r requirements.txt

Run the analysis:

    python mmm_analysis.py

---

## Limitations  

- This is a simplified model and does not account for seasonality or external factors  
- Results should be interpreted as directional rather than causal  
- The dataset is synthetic and used for demonstration purposes  

---

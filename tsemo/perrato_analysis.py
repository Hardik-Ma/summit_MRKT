import pandas as pd
import matplotlib.pyplot as plt
from summit.utils.multiobjective import pareto_efficient

# Load your results
df = pd.read_csv('results/repeat_3.csv')

# Calculate Pareto front
objectives = df[['sty', 'e_factor']].to_numpy()
pareto_mask, indices = pareto_efficient(objectives, maximize=[True, False])
pareto_front = df.iloc[indices]

print("=== PARETO OPTIMAL SOLUTIONS ===")
print(pareto_front[['res_time', 'equiv', 'conc_dfnb', 'temp', 'sty', 'e_factor']])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['sty'], df['e_factor'], alpha=0.6, label='All experiments')
plt.scatter(pareto_front['sty'], pareto_front['e_factor'], color='red', s=100, label='Pareto front')
plt.xlabel('STY')
plt.ylabel('E-factor')
plt.title('Pareto Front')
plt.legend()
plt.savefig('pareto_front.png', dpi=300, bbox_inches='tight')
plt.show()

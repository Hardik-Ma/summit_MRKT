import json
import pandas as pd

# Load the JSON file
with open('results/repeat_1.json', 'r') as f:
    data = json.load(f)

# Extract all experiments
experiments_data = data['experiment']['data']['data']
columns = [col[0] for col in data['experiment']['data']['columns']]
df = pd.DataFrame(experiments_data, columns=columns)

print("All experiments from JSON:")
print(df[['res_time', 'equiv', 'conc_dfnb', 'temp', 'sty', 'e_factor']])
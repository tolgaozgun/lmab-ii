import numpy as np
import pandas as pd

# Data setup
data = {
    'Untested_Ship (Ethanol_1)': [0.0627, 0.1096, 0.1088, 0.0459, 0.0401, 0.043],
    'Hit (Ethanol_2)': [0.5666, 0.5169, 0.7725, 0.6168, 0.6952, 0.694],
    'Untested_Empty (NaCl_1)': [0.0366, 0.0468, 0.0384, 0.0396, 0.0422, 0.042],
    'Miss (NaCl_2)': [0.1568, 0.1504, 0.1169, 0.2565, 0.1495, 0.1727]
}

df = pd.DataFrame(data)

# Function to calculate Z' factor
def calculate_z_prime(control1, control2):
    mean1, std1 = np.mean(control1), np.std(control1, ddof=1)
    mean2, std2 = np.mean(control2), np.std(control2, ddof=1)
    
    z_prime = 1 - (3 * (std1 + std2) / abs(mean1 - mean2))
    return z_prime

# Calculate Z' values
z_prime_results = {}

# Comparing Untested_Ship vs Hit
z_prime_results['Untested_Ship vs Hit'] = calculate_z_prime(df['Untested_Ship (Ethanol_1)'], df['Hit (Ethanol_2)'])

# Comparing Untested_Ship vs Untested_Empty
z_prime_results['Untested_Ship vs Untested_Empty'] = calculate_z_prime(df['Untested_Ship (Ethanol_1)'], df['Untested_Empty (NaCl_1)'])

# Comparing Untested_Ship vs Miss
z_prime_results['Untested_Ship vs Miss'] = calculate_z_prime(df['Untested_Ship (Ethanol_1)'], df['Miss (NaCl_2)'])

# Comparing Hit vs Untested_Empty
z_prime_results['Hit vs Untested_Empty'] = calculate_z_prime(df['Hit (Ethanol_2)'], df['Untested_Empty (NaCl_1)'])

# Comparing Hit vs Miss
z_prime_results['Hit vs Miss'] = calculate_z_prime(df['Hit (Ethanol_2)'], df['Miss (NaCl_2)'])

# Comparing Untested_Empty vs Miss
z_prime_results['Untested_Empty vs Miss'] = calculate_z_prime(df['Untested_Empty (NaCl_1)'], df['Miss (NaCl_2)'])

# Display results
for comparison, z_prime in z_prime_results.items():
    print(f"Z' for {comparison}: {z_prime:.4f}")

import numpy as np
import pandas as pd

# Data setup
data = {
    'Untested_Ship (Ethanol)': [0.0475, 0.0465, 0.047, 0.039, 0.0612, 0.0451, 0.0415],
    'Hit (Ethanol + DMEM)': [0.7145, 0.6763, 0.6625, 0.7294, 0.8099, 0.6432, 0.5507],
    'Untested_Empty (Bleach)': [0.0375, 0.0384, 0.0387, 0.0418, 0.0387, 0.0506, 0.0459],
    'Miss (Bleach + DMEM)': [0.1689, 0.2393, 0.1924, 0.2779, 0.1852, 0.265, 0.2155]
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
z_prime_results['Untested_Ship vs Hit'] = calculate_z_prime(df['Untested_Ship (Ethanol)'], df['Hit (Ethanol + DMEM)'])

# Comparing Untested_Ship vs Untested_Empty
z_prime_results['Untested_Ship vs Untested_Empty'] = calculate_z_prime(df['Untested_Ship (Ethanol)'], df['Untested_Empty (Bleach)'])

# Comparing Untested_Ship vs Miss
z_prime_results['Untested_Ship vs Miss'] = calculate_z_prime(df['Untested_Ship (Ethanol)'], df['Miss (Bleach + DMEM)'])

# Comparing Hit vs Untested_Empty
z_prime_results['Hit vs Untested_Empty'] = calculate_z_prime(df['Hit (Ethanol + DMEM)'], df['Untested_Empty (Bleach)'])

# Comparing Hit vs Miss
z_prime_results['Hit vs Miss'] = calculate_z_prime(df['Hit (Ethanol + DMEM)'], df['Miss (Bleach + DMEM)'])

# Comparing Untested_Empty vs Miss
z_prime_results['Untested_Empty vs Miss'] = calculate_z_prime(df['Untested_Empty (Bleach)'], df['Miss (Bleach + DMEM)'])

# Display results
for comparison, z_prime in z_prime_results.items():
    print(f"Z' for {comparison}: {z_prime:.4f}")

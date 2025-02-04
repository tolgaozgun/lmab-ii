import numpy as np
import pandas as pd
import sys

def calculate_z_prime(control1, control2):
    """Calculate Z' factor between two controls."""
    mean1, std1 = np.mean(control1), np.std(control1, ddof=1)
    mean2, std2 = np.mean(control2), np.std(control2, ddof=1)
    
    z_prime = 1 - (3 * (std1 + std2) / abs(mean1 - mean2))
    return z_prime

def process_data(input_file, output_file):
    # Read data from input file
    df = pd.read_csv(input_file, header=0)
    
    # Calculate Z' values
    z_prime_results = {}
    columns = df.columns.tolist()
    
    # Get column names for easier reference
    untested_ship = columns[0]
    hit = columns[1]
    untested_empty = columns[2]
    miss = columns[3]
    
    # Calculate all Z' value combinations
    comparisons = [
        (untested_ship, hit, 'Untested_Ship vs Hit'),
        (untested_ship, untested_empty, 'Untested_Ship vs Untested_Empty'),
        (untested_ship, miss, 'Untested_Ship vs Miss'),
        (hit, untested_empty, 'Hit vs Untested_Empty'),
        (hit, miss, 'Hit vs Miss'),
        (untested_empty, miss, 'Untested_Empty vs Miss')
    ]
    
    # Write results to output file
    with open(output_file, 'w') as f:
        f.write(f"Results for {input_file}:\n")
        f.write("-" * 50 + "\n")
        
        for col1, col2, label in comparisons:
            z_prime = calculate_z_prime(df[col1], df[col2])
            result_line = f"Z' for {label}: {z_prime:.4f}\n"
            f.write(result_line)
        
        f.write("-" * 50 + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python absorbance_ztest.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_data(input_file, output_file)

if __name__ == "__main__":
    main() 
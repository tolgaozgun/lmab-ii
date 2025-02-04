# Lab 4: Z-Prime Factor Analysis

This directory contains scripts and data for calculating Z-prime factors for different assay conditions.

## Files

- `absorbance_ztest.py`: Main script for Z-prime factor calculations
- `old_data.in`: Data from ethanol/NaCl assay
- `new_data.in`: Data from ethanol-DMEM/bleach assay
- `requirements.txt`: Python package dependencies

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the analysis on either dataset using:

```bash
python absorbance_ztest.py <input_file> <output_file>
```

Example:

```bash
python absorbance_ztest.py old_data.in old_results.out
python absorbance_ztest.py new_data.in new_results.out
```

## Data Format

Input files should be CSV format with:

- Header row containing condition names
- Each subsequent row containing absorbance measurements
- Four columns representing:
  1. Untested Ship control
  2. Hit condition
  3. Untested Empty control
  4. Miss condition

### Data Sets

1. Old Data (Ethanol/NaCl assay):

   - Untested Ship: Ethanol_1
   - Hit: Ethanol_2
   - Untested Empty: NaCl_1
   - Miss: NaCl_2

2. New Data (Ethanol-DMEM/Bleach assay):
   - Untested Ship: Ethanol
   - Hit: Ethanol + DMEM
   - Untested Empty: Bleach
   - Miss: Bleach + DMEM

## Output

The script saves Z-prime values for all possible comparisons between conditions to the specified output file. Values are formatted to 4 decimal places. The output file includes:

- A header indicating the input file name
- Z-prime values for each comparison
- Decorative separators for readability

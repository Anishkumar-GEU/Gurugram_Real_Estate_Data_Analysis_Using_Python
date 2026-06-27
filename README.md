# Gurugram Real Estate Data Analysis

A comprehensive Python-based analysis of real estate properties in Gurugram, exploring pricing trends, property characteristics, and market dynamics.

## Overview

This project analyzes a dataset of residential properties in Gurugram to answer key questions about the real estate market, including pricing patterns, location premiums, property status impacts, and builder comparisons.

## Questions Answered

1. **Costliest Property**: Identifies the most expensive flat in the dataset
2. **Best Locality by Average Price**: Determines which locality commands the highest average price
3. **Highest Rate per Square Feet**: Finds the locality with the best (highest) rate per square foot
4. **Ready-to-Move vs Under-Construction**: Compares average prices between property statuses
5. **RERA Approval Premium**: Analyzes if RERA-approved properties command a price premium
6. **Area vs Price Impact**: Evaluates how property area affects pricing
7. **Most Expensive BHK Configuration**: Identifies the priciest BHK type by rate per sqft
8. **Costliest Property Type**: Determines which property type (Apartment, Plot, etc.) is most expensive
9. **Builder Price Comparison**: Ranks top 5 builders by average rate per square foot
10. **Area vs Rate per SqFt**: Analyzes whether larger homes command higher per-square-foot prices

## Project Structure

```
.
├── README.md              # Project documentation
├── main.py               # Main analysis script
├── data.csv              # Dataset containing real estate properties
```

## Dataset Features

The dataset includes the following columns:

- **Price**: Property price in currency units
- **Status**: Property status (Ready to move / Under Construction)
- **Area**: Property area in square feet
- **Rate per sqft**: Price per square foot
- **Property Type**: Type of property (Apartment, Plot, etc.)
- **Locality**: Geographic locality in Gurugram
- **Builder Name**: Name of the builder/developer
- **RERA Approval**: RERA approval status (Approved by RERA / Not approved by RERA)
- **BHK_Count**: Number of bedrooms
- **Society**: Society/Complex name
- **Company Name**: Company/Builder abbreviation
- **Flat Type**: Type of flat (Apartment, etc.)

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn

### Installation

```bash
pip install pandas matplotlib seaborn
```

## Usage

### Running the Analysis

```bash
python main.py
```

The script will:
1. Load the CSV dataset
2. Clean and normalize the data (columns, formats, data types)
3. Remove duplicate entries
4. Execute all 10 analysis questions
5. Print results to console
6. Display visualizations

### Output

The script generates:
- Console output with analysis results
- Matplotlib visualizations comparing price per sqft vs area
- Statistical insights about the real estate market

## Data Cleaning

The script performs the following data cleaning operations:

- **Column normalization**: Converts column names to lowercase with underscores
- **Numeric columns**: Removes commas from price, area, and rate_per_sqft and converts to appropriate numeric types
- **Categorical columns**: Strips whitespace, converts to lowercase, and standardizes values
- **RERA mapping**: Converts approval status to boolean values
- **Deduplication**: Removes duplicate rows

## Key Findings

- Analyzes average price differences between ready-to-move and under-construction properties
- Identifies RERA approval impact on property pricing
- Compares pricing across different localities and builder names
- Examines the relationship between property area and pricing

## Future Improvements

- Add error handling and data validation
- Refactor into modular functions
- Add more statistical tests (t-tests, correlation analysis)
- Generate exportable reports (PDF/HTML)
- Add more visualization types (boxplots, heatmaps)
- Implement outlier detection
- Add configuration management

## License

Proprietary - For educational purposes

## Author

Data Analysis Project

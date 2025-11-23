# Maryland Data Analysis Project

## ⚠️ Disclaimer

**This is a personal learning project and is not intended for business use or meaningful public consumption. The analyses, code, and findings are for educational purposes only. Use at your own risk. No warranties or guarantees are provided regarding the accuracy, completeness, or reliability of any information or code in this repository.**

## Overview
This project contains data analysis and visualization work for Maryland state data, including operating budget analysis, grant and loan data, and per capita personal income studies.

## Project Structure

### Operating Budget
- **Maryland Operating Budget.ipynb** - Main operating budget analysis
- **Migration.ipynb** - Data migration and processing notebook
- **Operating Budget Exploratory Analysis.ipynb** - Exploratory data analysis of budget data
- **Per Capita Personal Income.ipynb** - Personal income analysis
- **Per Capita Personal Income EDA.ipynb** - Exploratory data analysis of income data

### Grant and Loan Data
Contains analysis of Maryland grant and loan programs.

## Setup

### Prerequisites
- Python 3.x
- Jupyter Notebook/Lab

### Installation

1. Clone this repository
```bash
git clone https://github.com/fewstack/Maryland.git
cd Maryland
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Create a `.env` file for sensitive configuration (see `.env.example` if provided)

## Usage

Launch Jupyter Notebook to explore the analysis:
```bash
jupyter notebook
```

Navigate to the `Operating Budget` folder to access the various analysis notebooks.

## Data

Data files are stored in the `Data` folder (not included in version control). Please ensure you have the necessary data files before running the notebooks.

## Contributing

Please ensure all sensitive data and credentials are kept in `.env` files and never committed to the repository.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

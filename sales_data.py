# -*- coding: utf-8 -*-
"""sales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qir5IGnaRh4QK9zWlT-A588RmXzk5b3b
"""

import pandas as pd

def load_sales_data(file_path):
    """Load sales data from CSV or JSON."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or JSON.")
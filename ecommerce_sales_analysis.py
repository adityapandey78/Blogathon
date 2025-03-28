# ecommerce_sales_analysis.py
# Unraveling our online sales data mysteries!

import fireducks.pandas as pd
import numpy as np

def analyze_sales_performance():
    """
    Deep dive into our e-commerce sales performance
    """
    # Simulated e-commerce sales data
    sales_data = pd.DataFrame({
        'product_category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing', 'Books'],
        'sales': [1200, 750, 450, 1500, 600, 350],
        'profit_margin': [0.25, 0.40, 0.35, 0.30, 0.45, 0.20]
    })

    # Quick sales insights
    category_performance = sales_data.groupby('product_category').agg({
        'sales': ['sum', 'mean'],
        'profit_margin': 'mean'
    })

    print("Category Performance Report:")
    print(category_performance)

    # Identify top-performing categories
    top_categories = category_performance['sales']['sum'].nlargest(2)
    print("\nTop 2 Categories by Total Sales:")
    print(top_categories)

    return sales_data, category_performance

# Run the analysis if script is executed directly
if __name__ == "__main__":
    analyze_sales_performance()

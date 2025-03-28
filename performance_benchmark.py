# performance_benchmark.py
# A real-world speed test for FireDucks

import fireducks.pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def generate_sales_data(rows):
    """
    Generate realistic e-commerce sales simulation
    
    Args:
        rows (int): Number of data points to generate
    
    Returns:
        pd.DataFrame: Simulated sales dataset
    """
    # Realistic data generation with some randomness
    product_categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    return pd.DataFrame({
        'product_category': np.random.choice(product_categories, rows),
        'region': np.random.choice(regions, rows),
        'sales_amount': np.random.normal(500, 200, rows),  # Mean $500, std dev $200
        'discount_applied': np.random.choice([True, False], rows, p=[0.3, 0.7])
    })

def performance_analysis(df):
    """
    Conduct deep dive performance analysis
    
    Args:
        df (pd.DataFrame): Input sales dataframe
    
    Returns:
        pd.DataFrame: Aggregated performance metrics
    """
    # Multiple aggregations to simulate real-world complexity
    return df.groupby(['product_category', 'region']).agg({
        'sales_amount': ['sum', 'mean', 'count'],
        'discount_applied': 'mean'
    })

def benchmark_fireducks(data_sizes):
    """
    Benchmark FireDucks performance across different data sizes
    
    Args:
        data_sizes (list): List of data sizes to test
    
    Returns:
        dict: Performance timings for each data size
    """
    performance_results = {}
    
    for size in data_sizes:
        # Generate data
        sales_data = generate_sales_data(size)
        
        # Time the analysis
        start_time = time.time()
        result = performance_analysis(sales_data)
        end_time = time.time()
        
        performance_results[size] = end_time - start_time
        print(f"Data Size: {size:,} rows | Processing Time: {end_time - start_time:.4f} seconds")
    
    return performance_results

# Actual benchmarking
def main():
    print("🚀 FireDucks Performance Benchmark 🚀")
    
    # Test different data sizes
    data_sizes = [100_000, 500_000, 1_000_000, 2_000_000]
    results = benchmark_fireducks(data_sizes)
    
    # Optional visualization (if matplotlib is available)
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(list(results.keys()), list(results.values()), marker='o')
        plt.title('FireDucks Performance: Processing Time vs Dataset Size')
        plt.xlabel('Number of Rows')
        plt.ylabel('Processing Time (seconds)')
        plt.tight_layout()
        plt.savefig('performance_benchmark.png')
        plt.close()
    except Exception as e:
        print(f"Visualization failed: {e}")

if __name__ == "__main__":
    main()

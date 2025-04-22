# performance_benchmark.py
# A real-world speed test for FireDucks with proper evaluation
import fireducks.pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def evaluate(df):
    """
    Force evaluation for FireDucks dataframes
    """
    try:
        df._evaluate()  # Force evaluation for FireDucks
    except AttributeError:
        pass
    return df

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
    
    df = pd.DataFrame({
        'product_category': np.random.choice(product_categories, rows),
        'region': np.random.choice(regions, rows),
        'sales_amount': np.random.normal(500, 200, rows),  # Mean $500, std dev $200
        'discount_applied': np.random.choice([True, False], rows, p=[0.3, 0.7])
    })
    return evaluate(df)  # Ensure data is evaluated

def performance_analysis(df):
    """
    Conduct deep dive performance analysis
    
    Args:
        df (pd.DataFrame): Input sales dataframe
    
    Returns:
        pd.DataFrame: Aggregated performance metrics
    """
    # Multiple aggregations to simulate real-world complexity
    result = df.groupby(['product_category', 'region']).agg({
        'sales_amount': ['sum', 'mean', 'count'],
        'discount_applied': 'mean'
    })
    return evaluate(result)  # Ensure result is evaluated

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
        print(f"Generating dataset with {size:,} rows...")
        sales_data = generate_sales_data(size)
        
        # Time the analysis
        print(f"Running analysis on {size:,} rows...")
        start_time = time.time()
        result = performance_analysis(sales_data)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        performance_results[size] = elapsed_time
        print(f"Data Size: {size:,} rows | Processing Time: {elapsed_time:.4f} seconds")
        
        # Display a sample of the results (first 5 rows)
        print("\nSample of analysis results:")
        print(result.head(5))
        print("\n" + "-"*60 + "\n")
    
    return performance_results

# Actual benchmarking
def main():
    print("🚀 FireDucks Performance Benchmark 🚀")
    
    # Test different data sizes - using smaller sizes for demonstration
    data_sizes = [10_000, 50_000, 100_000, 200_000]
    results = benchmark_fireducks(data_sizes)
    
    # Print summary table
    print("\nPerformance Summary:")
    print("-" * 40)
    print(f"{'Data Size':>12} | {'Processing Time':>20}")
    print("-" * 40)
    for size, time_taken in results.items():
        print(f"{size:>12,} | {time_taken:>20.4f} seconds")
    
    # Visualization
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(list(results.keys()), list(results.values()), marker='o', linewidth=2)
        plt.title('FireDucks Performance: Processing Time vs Dataset Size')
        plt.xlabel('Number of Rows')
        plt.ylabel('Processing Time (seconds)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(list(results.keys()))
        plt.ticklabel_format(style='plain', axis='x')
        
        # Add data point labels
        for size, time_taken in results.items():
            plt.annotate(f"{time_taken:.2f}s", 
                        (size, time_taken),
                        textcoords="offset points", 
                        xytext=(0,10), 
                        ha='center')
            
        plt.tight_layout()
        plt.savefig('performance_benchmark.png')
        print("\nPerformance visualization saved as 'performance_benchmark.png'")
        
        # Display the plot
        plt.show()
    except Exception as e:
        print(f"Visualization failed: {e}")

if __name__ == "__main__":
    main()

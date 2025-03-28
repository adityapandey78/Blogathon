# FireDucks Performance Demonstration

## Overview

This repository accompanies the Blogathon article "Why Everyone is talking about FireDucks?" and provides practical demonstrations of FireDucks, a high-performance Python library developed by NEC for accelerating data analysis.

## 🚀 About FireDucks

FireDucks is a cutting-edge Python library designed to address performance limitations in pandas, offering:
- Lazy Evaluation
- Parallel Processing
- High Compatibility with pandas
- Significant performance improvements (up to 16x faster)

## 🔧 Installation

```bash
pip install fireducks
```

## 📊 Usage Examples

### 1. Import Hook Method

The import hook method allows seamless replacement of pandas with FireDucks:

```python
# Method 1: Using python3 command
# python3 -m fireducks.pandas your_script.py

# Method 2: IPython/Jupyter Extension
# %load_ext fireducks.pandas

import pandas as pd  # This now uses FireDucks under the hood

# Create a sample DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 75000, 90000]
})

# Perform operations
filtered_df = df[df['age'] > 30]
grouped = df.groupby('age')['salary'].mean()

print("Filtered DataFrame:")
print(filtered_df)
print("\nGrouped Salary by Age:")
print(grouped)
```

### 2. Explicit Import Method

Direct import of FireDucks for more explicit control:

```python
import fireducks.pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'value': [10, 20, 15, 25, 30, 12]
})

# Perform complex operations
result = df.groupby('category').agg({
    'value': ['mean', 'max', 'min']
})

print("\nAggregated Results:")
print(result)
```

## 🏎️ Performance Benchmarks

Key performance highlights from our blog:
- Up to 16x faster execution for certain operations
- Average 5x speedup
- TPC-H Benchmark: 141x speedup over pandas (excluding I/O)

## 📁 Repository Structure

```
fireducks-performance-demo/
│
├── README.md                  # This file
├── requirements.txt           # Project dependencies
│
├── notebooks/
│   ├── import_hook_demo.ipynb  # Jupyter notebook for import hook method
│   └── explicit_import_demo.ipynb  # Jupyter notebook for explicit import
│
└── scripts/
    ├── performance_benchmark.py  # Detailed performance comparison
    └── data_processing_example.py  # Real-world data processing example
```

## 🔬 Performance Benchmark Script

```python
import fireducks.pandas as pd
import numpy as np
import time

def create_large_dataframe(rows=1_000_000):
    return pd.DataFrame({
        'category': np.random.choice(['A', 'B', 'C'], rows),
        'value': np.random.randn(rows)
    })

def benchmark_groupby(df):
    start_time = time.time()
    result = df.groupby('category')['value'].agg(['mean', 'max', 'min'])
    end_time = time.time()
    return end_time - start_time

# Benchmark demonstration
large_df = create_large_dataframe()
processing_time = benchmark_groupby(large_df)
print(f"Processing Time: {processing_time:.4f} seconds")
```

## 🚧 Limitations

- Currently supports Linux (manylinux) on x86_64
- Python versions >3.8 and <=3.13
- Windows and macOS support in development

## 📚 Resources

- [FireDucks PyPI Page](https://pypi.org/project/fireducks/)
- [TPC-H Benchmark Details](https://fireducks-dev.github.io/db-benchmark/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

Distributed under the 3-Clause BSD License.

## 🙏 Acknowledgments

- NEC for developing FireDucks
- The open-source community

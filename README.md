# NumPy-Based Data Manipulation and Statistical Analysis

## Problem Statement
Modern data science workflows rely heavily on efficient numerical computation and structured data manipulation. High-dimensional datasets must be processed, indexed, filtered, and transformed before they can be used for machine learning or statistical modelling.

The objective of this project is to demonstrate fundamental array operations using NumPy that form the basis of data preprocessing pipelines. The project implements array creation, indexing, slicing, copying, statistical computation, subsetting, reshaping, and flattening operations.

These operations simulate the initial stages of a typical machine learning pipeline where raw numerical data is transformed into structured feature matrices suitable for downstream modelling tasks.
## Dataset Description
A synthetic dataset is constructed to represent environmental observations.

Each row represents an observation and each column corresponds to a measured variable.

| Feature     | Description             | Unit |
| ----------- | ----------------------- | ---- |
| Temperature | Atmospheric temperature | °C   |
| Humidity    | Relative humidity       | %    |
| Wind Speed  | Wind velocity           | km/h |
# Expected output:
[
 [25, 60, 12],
 [30, 65, 10],
 [28, 70, 14],
 [32, 55, 9]
]

Structure:

Number of observations: 4

Number of features: 3

Data type: integer numerical matrix

Matrix representation:

𝑋
∈
𝑅
4
×
3
X∈R
4×3
## Data Processing Pipeline
A simplified data science pipeline implemented in this project is shown below.

Data Acquisition
      ↓
Data Representation (NumPy arrays)
      ↓
Statistical Analysis
      ↓
Array Manipulation
      ↓
Feature Extraction
      ↓
Visualization

NumPy enables vectorized operations which significantly improve computational efficiency compared to iterative Python loops.

## Results
Statistical results obtained from the dataset:

| Metric             | Value |
| ------------------ | ----- |
| Mean Temperature   | 28.75 |
| Mean Humidity      | 62.5  |
| Mean Wind Speed    | 11.25 |
| Maximum Humidity   | 70    |
| Minimum Wind Speed | 9     |
The operations successfully demonstrate:

Efficient numerical computation

Array indexing and slicing

Conditional filtering

Data reshaping and flattening

These operations form the basis for preprocessing tasks in machine learning pipelines.

## Visualization


## Reproducibility Instructions
Step 1 — Install dependencies
pip install numpy matplotlib
Step 2 — Run the program
python main.py

## Project Structure
numpy-data-science-project/
│
├── data/
│
├── notebooks/
│
├── src/
│   └── main.py
│
├── figures/
│
├── README.md
│
├── requirements.txt
│
└── .gitignore

## Conclusion
This project demonstrates fundamental numerical computing operations used in data science pipelines. Using NumPy's vectorized operations allows efficient handling of multidimensional datasets while minimizing computational overhead. Such techniques are widely used in feature engineering, statistical analysis, and machine learning preprocessing tasks.

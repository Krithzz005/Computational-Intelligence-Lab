[23bcs074@mepcolinux ex3]$cat fin.py
import csv
import math
from collections import Counter

# -------------------------------
# Read CSV (Handles N features)
# -------------------------------
def read_csv(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:

            features = [float(x) for x in row[:-1]]
            label = row[-1]
            data.append(features + [label])
    return data

# -------------------------------
# Normalization (Min-Max)
# -------------------------------
def normalization(dataset):
    num_features = len(dataset[0]) - 1
    bounds = []

    # Logic for Z-Score Normalization (Standardization):
    # mean = sum(values) / len(values)
    # std_dev = math.sqrt(sum((x - mean)**2) / len(values))
    # norm_val = (val - mean) / std_dev

    for i in range(num_features):
        col_values = [row[i] for row in dataset]
        bounds.append((min(col_values), max(col_values)))

    norm_ds = []
    for row in dataset:
        n_row = []
        for i in range(num_features):
            mi, ma = bounds[i]
            n_val = (row[i] - mi) / (ma - mi) if ma != mi else 0
            n_row.append(n_val)
        norm_ds.append(n_row + [row[-1]])

    return norm_ds, bounds

# -------------------------------
# Generic Distance Metric (Minkowski)
# -------------------------------
def distance_metric(point1, point2, r):
    # Works for N dimensions via zip
    sum_diff = sum(abs(p1 - p2)**r for p1, p2 in zip(point1, point2))
    return sum_diff**(1/r)

# -------------------------------
# Process Table
# -------------------------------
def process_table(dataset, norm_ds, u_point, r_val, bounds):

    n_u_point = []
    for i in range(len(u_point)):
        mi, ma = bounds[i]
        n_u_point.append((u_point[i] - mi) / (ma - mi) if ma != mi else 0)

    full_table = []
    for i in range(len(dataset)):
        orig_features = dataset[i][:-1]
        norm_features = norm_ds[i][:-1]
        label = dataset[i][-1]

        dist = distance_metric(norm_features, n_u_point, r_val)
        full_table.append([orig_features, norm_features, dist, label])

    full_table.sort(key=lambda x: x[2])
    for idx, row in enumerate(full_table):
        row.insert(3, idx + 1)
    return full_table

# -------------------------------
# Display Functions
# -------------------------------
def print_intermediate(table):
    for r in table:
        orig_str = str([round(x, 2) for x in r[0]])
        norm_str = str([round(x, 2) for x in r[1]])

def print_final(table, k, knn_type):
    print(f"\nFINAL TABLE (K={k} Neighbors)")
    print("-" * 100)
    neighbors = table[:k]
    for r in neighbors:
        orig_str = str([round(x, 2) for x in r[0]])
        norm_str = str([round(x, 2) for x in r[1]])
        print(f"{orig_str:<25} {norm_str:<25} {round(r[2],4):<10} {r[3]:<6} {r[4]}")

    if knn_type == 1:
        classes = [r[4] for r in neighbors]
        return Counter(classes).most_common(1)[0][0]
    else:
        weights = {}
        for r in neighbors:
            label, d = r[4], r[2]
            w = 1 / (d + 0.0001) # Epsilon added to prevent division by zero
            weights[label] = weights.get(label, 0) + w
        return max(weights, key=weights.get)

# -------------------------------
# Main Program
# -------------------------------
filename = input("Enter CSV file name: ")
orig_dataset = read_csv(filename)
norm_dataset, bounds = normalization(orig_dataset)

num_features = len(orig_dataset[0]) - 1
print(f"Detected {num_features} dimensions.")

print ("="*50)

print("BLOOD TRANSFUSION DATASET")

print ("="*50)

print("The dimensions are recency,frequency,monetary,time.")
u_point = []
for i in range(num_features):
    u_point.append(float(input(f"Enter value for Dimension {i+1}: ")))

r_val = float(input("Enter distance metric r (1: Manhattan, 2: Euclidean): "))

table = process_table(orig_dataset, norm_dataset, u_point, r_val, bounds)
print_intermediate(table)
while True:
    k_input = input("\nEnter value of K (or 'q' to quit): ")
    if k_input.lower() == 'q': break
    k = int(k_input)

    print("KNN Type: 1. Unweighted  2. Weighted")
    knn_type = int(input("Choice: "))

    result = print_final(table, k, knn_type)
    print(f"\nResult: Point {u_point} classified as: {result}")

[23bcs074@mepcolinux ex3]$python3 fin.py
Enter CSV file name: transfusion.csv
Detected 4 dimensions.
==================================================
BLOOD TRANSFUSION DATASET
==================================================
The dimensions are recency,frequency,monetary,time.
Enter value for Dimension 1: 2
Enter value for Dimension 2: 48
Enter value for Dimension 3: 2500
Enter value for Dimension 4: 10
Enter distance metric r (1: Manhattan, 2: Euclidean): 2

Enter value of K (or 'q' to quit): 3
KNN Type: 1. Unweighted  2. Weighted
Choice: 2

FINAL TABLE (K=3 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 3
KNN Type: 1. Unweighted  2. Weighted
Choice: 1

FINAL TABLE (K=3 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 5
KNN Type: 1. Unweighted  2. Weighted
Choice: 1

FINAL TABLE (K=5 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 5
KNN Type: 1. Unweighted  2. Weighted
Choice: 2

FINAL TABLE (K=5 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 7
KNN Type: 1. Unweighted  2. Weighted
Choice: 1

FINAL TABLE (K=7 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1
[2.0, 21.0, 5250.0, 52.0] [0.03, 0.41, 0.41, 0.52]  0.7385     6      1
[0.0, 13.0, 3250.0, 28.0] [0.0, 0.24, 0.24, 0.27]   0.7415     7      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 7
KNN Type: 1. Unweighted  2. Weighted
Choice: 2

FINAL TABLE (K=7 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1
[2.0, 21.0, 5250.0, 52.0] [0.03, 0.41, 0.41, 0.52]  0.7385     6      1
[0.0, 13.0, 3250.0, 28.0] [0.0, 0.24, 0.24, 0.27]   0.7415     7      1

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 15
KNN Type: 1. Unweighted  2. Weighted
Choice: 1

FINAL TABLE (K=15 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1
[2.0, 21.0, 5250.0, 52.0] [0.03, 0.41, 0.41, 0.52]  0.7385     6      1
[0.0, 13.0, 3250.0, 28.0] [0.0, 0.24, 0.24, 0.27]   0.7415     7      1
[3.0, 14.0, 3500.0, 35.0] [0.04, 0.27, 0.27, 0.34]  0.7457     8      0
[2.0, 13.0, 3250.0, 32.0] [0.03, 0.24, 0.24, 0.31]  0.7526     9      1
[4.0, 23.0, 5750.0, 58.0] [0.05, 0.45, 0.45, 0.58]  0.7625     10     0
[4.0, 14.0, 3500.0, 40.0] [0.05, 0.27, 0.27, 0.4]   0.7658     11     0
[2.0, 11.0, 2750.0, 23.0] [0.03, 0.2, 0.2, 0.22]    0.7674     12     0
[2.0, 11.0, 2750.0, 26.0] [0.03, 0.2, 0.2, 0.25]    0.7735     13     0
[4.0, 12.0, 3000.0, 34.0] [0.05, 0.22, 0.22, 0.33]  0.7776     14     1
[2.0, 11.0, 2750.0, 28.0] [0.03, 0.2, 0.2, 0.27]    0.7783     15     0

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): 15
KNN Type: 1. Unweighted  2. Weighted
Choice: 2

FINAL TABLE (K=15 Neighbors)
----------------------------------------------------------------------------------------------------
[6.0, 22.0, 5500.0, 28.0] [0.08, 0.43, 0.43, 0.27]  0.6161     1      1
[3.0, 21.0, 5250.0, 42.0] [0.04, 0.41, 0.41, 0.42]  0.6821     2      1
[2.0, 20.0, 5000.0, 45.0] [0.03, 0.39, 0.39, 0.45]  0.7079     3      1
[1.0, 16.0, 4000.0, 35.0] [0.01, 0.31, 0.31, 0.34]  0.7138     4      1
[4.0, 16.0, 4000.0, 38.0] [0.05, 0.31, 0.31, 0.38]  0.7261     5      1
[2.0, 21.0, 5250.0, 52.0] [0.03, 0.41, 0.41, 0.52]  0.7385     6      1
[0.0, 13.0, 3250.0, 28.0] [0.0, 0.24, 0.24, 0.27]   0.7415     7      1
[3.0, 14.0, 3500.0, 35.0] [0.04, 0.27, 0.27, 0.34]  0.7457     8      0
[2.0, 13.0, 3250.0, 32.0] [0.03, 0.24, 0.24, 0.31]  0.7526     9      1
[4.0, 23.0, 5750.0, 58.0] [0.05, 0.45, 0.45, 0.58]  0.7625     10     0
[4.0, 14.0, 3500.0, 40.0] [0.05, 0.27, 0.27, 0.4]   0.7658     11     0
[2.0, 11.0, 2750.0, 23.0] [0.03, 0.2, 0.2, 0.22]    0.7674     12     0
[2.0, 11.0, 2750.0, 26.0] [0.03, 0.2, 0.2, 0.25]    0.7735     13     0
[4.0, 12.0, 3000.0, 34.0] [0.05, 0.22, 0.22, 0.33]  0.7776     14     1
[2.0, 11.0, 2750.0, 28.0] [0.03, 0.2, 0.2, 0.27]    0.7783     15     0

Result: Point [2.0, 48.0, 2500.0, 10.0] classified as: 1

Enter value of K (or 'q' to quit): q
[23bcs074@mepcolinux ex3]$exit
exit


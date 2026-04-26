[23bcs074@mepcolinux ex4]$cat deci.py
import math

# -----------------------------
# Load dataset from file
# -----------------------------
def load_data(filename):
    dataset = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                row = line.split(',')
                dataset.append(row)
    return dataset


# Load data
data = load_data("play_tennis.txt")

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
target_index = 4


# -----------------------------
# Frequency Table
# -----------------------------
def frequency_table(dataset, column_index):
    freq = {}

    for row in dataset:
        value = row[column_index]
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1

    print(f"\nFrequency Table (Column {column_index}) = {freq}")
    return freq


# -----------------------------
# Entropy Calculation
# -----------------------------
def entropy(dataset):
    freq = frequency_table(dataset, target_index)
    total = len(dataset)
    ent = 0

    print("\nCalculating Entropy")

    for label in freq:
        p = freq[label] / total
        value = -p * math.log2(p)
        ent += value

        print(f"P({label}) = {freq[label]}/{total} = {p:.4f}")
        print(f"-P({label}) log2(P({label})) = {value:.4f}")

    print(f"Total Entropy = {ent:.4f}")
    return ent


# -----------------------------
# Weighted Entropy
# -----------------------------
def weighted_entropy(dataset, attribute_index):

    total = len(dataset)
    subsets = {}

    for row in dataset:
        key = row[attribute_index]
        if key not in subsets:
            subsets[key] = []
        subsets[key].append(row)

    w_ent = 0

    print(f"\nWeighted Entropy for {attributes[attribute_index]}")

    for value in subsets:

        subset = subsets[value]
        subset_size = len(subset)

        print(f"\nSubset where {attributes[attribute_index]} = {value}")
        print(f"Subset Size = {subset_size}")

        subset_entropy = entropy(subset)

        weight = subset_size / total
        contribution = weight * subset_entropy

        print(f"Weight = {subset_size}/{total} = {weight:.4f}")
        print(f"Contribution = {contribution:.4f}")

        w_ent += contribution

    print(f"\nTotal Weighted Entropy = {w_ent:.4f}")
    return w_ent


# -----------------------------
# Information Gain
# -----------------------------
def information_gain(dataset, attribute_index):

    print("\n----------------------------------")
    print(f"Information Gain for {attributes[attribute_index]}")

    total_ent = entropy(dataset)
    w_ent = weighted_entropy(dataset, attribute_index)

    gain = total_ent - w_ent

    print(f"\nGain = {total_ent:.4f} - {w_ent:.4f}")
    print(f"Information Gain ({attributes[attribute_index]}) = {gain:.4f}")

    return gain


# -----------------------------
# Build Decision Tree (ID3)
# -----------------------------
def build_tree(dataset, attrs):

    labels = [row[target_index] for row in dataset]

    # Case 1: Pure node
    if labels.count(labels[0]) == len(labels):
        print(f"\nLeaf Node {labels[0]}")
        return labels[0]

    # Case 2: No attributes left
    if len(attrs) == 0:
        majority = max(set(labels), key=labels.count)
        print(f"\nMajority Class {majority}")
        return majority

    gains = {}

    print("\nCalculating Information Gain for attributes")

    for attr in attrs:
        index = attributes.index(attr)
        gains[attr] = information_gain(dataset, index)

    # Select best attribute
    best_attr = max(gains, key=gains.get)
    best_index = attributes.index(best_attr)

    print(f"\nBest Attribute Selected {best_attr}")

    tree = {best_attr: {}}

    values = set([row[best_index] for row in dataset])

    for value in values:

        print(f"\nBranch: {best_attr} = {value}")

        subset = [row for row in dataset if row[best_index] == value]

        if not subset:
            majority = max(set(labels), key=labels.count)
            tree[best_attr][value] = majority
        else:
            new_attrs = attrs.copy()
            new_attrs.remove(best_attr)

            subtree = build_tree(subset, new_attrs)
            tree[best_attr][value] = subtree

    return tree


# -----------------------------
# MAIN PROGRAM
# -----------------------------
print("\n========== DECISION TREE ==========")

print("\nDataset Loaded from File:")
for row in data:
    print(row)

print("\nCalculating Total Entropy...")
total_entropy = entropy(data)

print("\n\n========== BUILDING DECISION TREE ==========")

decision_tree = build_tree(data, attributes)

print("\n\nFinal Decision Tree:")
print(decision_tree)

print("\n===================================")
[23bcs074@mepcolinux ex4]$python3 deci.py

========== DECISION TREE ==========

Dataset Loaded from File:
['Sunny', 'Hot', 'High', 'Weak', 'No']
['Sunny', 'Hot', 'High', 'Strong', 'No']
['Overcast', 'Hot', 'High', 'Weak', 'Yes']
['Rain', 'Mild', 'High', 'Weak', 'Yes']
['Rain', 'Cool', 'Normal', 'Weak', 'Yes']
['Rain', 'Cool', 'Normal', 'Strong', 'No']
['Overcast', 'Mild', 'Normal', 'Strong', 'Yes']
['Sunny', 'Cool', 'High', 'Weak', 'No']
['Sunny', 'Mild', 'Normal', 'Weak', 'Yes']
['Rain', 'Mild', 'Normal', 'Strong', 'Yes']

Calculating Total Entropy...

Frequency Table (Column 4) = {'No': 4, 'Yes': 6}

Calculating Entropy
P(No) = 4/10 = 0.4000
-P(No) log2(P(No)) = 0.5288
P(Yes) = 6/10 = 0.6000
-P(Yes) log2(P(Yes)) = 0.4422
Total Entropy = 0.9710


========== BUILDING DECISION TREE ==========

Calculating Information Gain for attributes

----------------------------------
Information Gain for Outlook

Frequency Table (Column 4) = {'No': 4, 'Yes': 6}

Calculating Entropy
P(No) = 4/10 = 0.4000
-P(No) log2(P(No)) = 0.5288
P(Yes) = 6/10 = 0.6000
-P(Yes) log2(P(Yes)) = 0.4422
Total Entropy = 0.9710

Weighted Entropy for Outlook

Subset where Outlook = Sunny
Subset Size = 4

Frequency Table (Column 4) = {'No': 3, 'Yes': 1}

Calculating Entropy
P(No) = 3/4 = 0.7500
-P(No) log2(P(No)) = 0.3113
P(Yes) = 1/4 = 0.2500
-P(Yes) log2(P(Yes)) = 0.5000
Total Entropy = 0.8113
Weight = 4/10 = 0.4000
Contribution = 0.3245

Subset where Outlook = Overcast
Subset Size = 2

Frequency Table (Column 4) = {'Yes': 2}

Calculating Entropy
P(Yes) = 2/2 = 1.0000
-P(Yes) log2(P(Yes)) = -0.0000
Total Entropy = 0.0000
Weight = 2/10 = 0.2000
Contribution = 0.0000

Subset where Outlook = Rain
Subset Size = 4

Frequency Table (Column 4) = {'Yes': 3, 'No': 1}

Calculating Entropy
P(Yes) = 3/4 = 0.7500
-P(Yes) log2(P(Yes)) = 0.3113
P(No) = 1/4 = 0.2500
-P(No) log2(P(No)) = 0.5000
Total Entropy = 0.8113
Weight = 4/10 = 0.4000
Contribution = 0.3245

Total Weighted Entropy = 0.6490

Gain = 0.9710 - 0.6490
Information Gain (Outlook) = 0.3219

----------------------------------
Information Gain for Temperature

Frequency Table (Column 4) = {'No': 4, 'Yes': 6}

Calculating Entropy
P(No) = 4/10 = 0.4000
-P(No) log2(P(No)) = 0.5288
P(Yes) = 6/10 = 0.6000
-P(Yes) log2(P(Yes)) = 0.4422
Total Entropy = 0.9710

Weighted Entropy for Temperature

Subset where Temperature = Hot
Subset Size = 3

Frequency Table (Column 4) = {'No': 2, 'Yes': 1}

Calculating Entropy
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
Total Entropy = 0.9183
Weight = 3/10 = 0.3000
Contribution = 0.2755

Subset where Temperature = Mild
Subset Size = 4

Frequency Table (Column 4) = {'Yes': 4}

Calculating Entropy
P(Yes) = 4/4 = 1.0000
-P(Yes) log2(P(Yes)) = -0.0000
Total Entropy = 0.0000
Weight = 4/10 = 0.4000
Contribution = 0.0000

Subset where Temperature = Cool
Subset Size = 3

Frequency Table (Column 4) = {'Yes': 1, 'No': 2}

Calculating Entropy
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
Total Entropy = 0.9183
Weight = 3/10 = 0.3000
Contribution = 0.2755

Total Weighted Entropy = 0.5510

Gain = 0.9710 - 0.5510
Information Gain (Temperature) = 0.4200

----------------------------------
Information Gain for Humidity

Frequency Table (Column 4) = {'No': 4, 'Yes': 6}

Calculating Entropy
P(No) = 4/10 = 0.4000
-P(No) log2(P(No)) = 0.5288
P(Yes) = 6/10 = 0.6000
-P(Yes) log2(P(Yes)) = 0.4422
Total Entropy = 0.9710

Weighted Entropy for Humidity

Subset where Humidity = High
Subset Size = 5

Frequency Table (Column 4) = {'No': 3, 'Yes': 2}

Calculating Entropy
P(No) = 3/5 = 0.6000
-P(No) log2(P(No)) = 0.4422
P(Yes) = 2/5 = 0.4000
-P(Yes) log2(P(Yes)) = 0.5288
Total Entropy = 0.9710
Weight = 5/10 = 0.5000
Contribution = 0.4855

Subset where Humidity = Normal
Subset Size = 5

Frequency Table (Column 4) = {'Yes': 4, 'No': 1}

Calculating Entropy
P(Yes) = 4/5 = 0.8000
-P(Yes) log2(P(Yes)) = 0.2575
P(No) = 1/5 = 0.2000
-P(No) log2(P(No)) = 0.4644
Total Entropy = 0.7219
Weight = 5/10 = 0.5000
Contribution = 0.3610

Total Weighted Entropy = 0.8464

Gain = 0.9710 - 0.8464
Information Gain (Humidity) = 0.1245

----------------------------------
Information Gain for Wind

Frequency Table (Column 4) = {'No': 4, 'Yes': 6}

Calculating Entropy
P(No) = 4/10 = 0.4000
-P(No) log2(P(No)) = 0.5288
P(Yes) = 6/10 = 0.6000
-P(Yes) log2(P(Yes)) = 0.4422
Total Entropy = 0.9710

Weighted Entropy for Wind

Subset where Wind = Weak
Subset Size = 6

Frequency Table (Column 4) = {'No': 2, 'Yes': 4}

Calculating Entropy
P(No) = 2/6 = 0.3333
-P(No) log2(P(No)) = 0.5283
P(Yes) = 4/6 = 0.6667
-P(Yes) log2(P(Yes)) = 0.3900
Total Entropy = 0.9183
Weight = 6/10 = 0.6000
Contribution = 0.5510

Subset where Wind = Strong
Subset Size = 4

Frequency Table (Column 4) = {'No': 2, 'Yes': 2}

Calculating Entropy
P(No) = 2/4 = 0.5000
-P(No) log2(P(No)) = 0.5000
P(Yes) = 2/4 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
Total Entropy = 1.0000
Weight = 4/10 = 0.4000
Contribution = 0.4000

Total Weighted Entropy = 0.9510

Gain = 0.9710 - 0.9510
Information Gain (Wind) = 0.0200

Best Attribute Selected Temperature

Branch: Temperature = Mild

Leaf Node Yes

Branch: Temperature = Hot

Calculating Information Gain for attributes

----------------------------------
Information Gain for Outlook

Frequency Table (Column 4) = {'No': 2, 'Yes': 1}

Calculating Entropy
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
Total Entropy = 0.9183

Weighted Entropy for Outlook

Subset where Outlook = Sunny
Subset Size = 2

Frequency Table (Column 4) = {'No': 2}

Calculating Entropy
P(No) = 2/2 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 2/3 = 0.6667
Contribution = 0.0000

Subset where Outlook = Overcast
Subset Size = 1

Frequency Table (Column 4) = {'Yes': 1}

Calculating Entropy
P(Yes) = 1/1 = 1.0000
-P(Yes) log2(P(Yes)) = -0.0000
Total Entropy = 0.0000
Weight = 1/3 = 0.3333
Contribution = 0.0000

Total Weighted Entropy = 0.0000

Gain = 0.9183 - 0.0000
Information Gain (Outlook) = 0.9183

----------------------------------
Information Gain for Humidity

Frequency Table (Column 4) = {'No': 2, 'Yes': 1}

Calculating Entropy
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
Total Entropy = 0.9183

Weighted Entropy for Humidity

Subset where Humidity = High
Subset Size = 3

Frequency Table (Column 4) = {'No': 2, 'Yes': 1}

Calculating Entropy
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
Total Entropy = 0.9183
Weight = 3/3 = 1.0000
Contribution = 0.9183

Total Weighted Entropy = 0.9183

Gain = 0.9183 - 0.9183
Information Gain (Humidity) = 0.0000

----------------------------------
Information Gain for Wind

Frequency Table (Column 4) = {'No': 2, 'Yes': 1}

Calculating Entropy
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
Total Entropy = 0.9183

Weighted Entropy for Wind

Subset where Wind = Weak
Subset Size = 2

Frequency Table (Column 4) = {'No': 1, 'Yes': 1}

Calculating Entropy
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
Total Entropy = 1.0000
Weight = 2/3 = 0.6667
Contribution = 0.6667

Subset where Wind = Strong
Subset Size = 1

Frequency Table (Column 4) = {'No': 1}

Calculating Entropy
P(No) = 1/1 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 1/3 = 0.3333
Contribution = 0.0000

Total Weighted Entropy = 0.6667

Gain = 0.9183 - 0.6667
Information Gain (Wind) = 0.2516

Best Attribute Selected Outlook

Branch: Outlook = Sunny

Leaf Node No

Branch: Outlook = Overcast

Leaf Node Yes

Branch: Temperature = Cool

Calculating Information Gain for attributes

----------------------------------
Information Gain for Outlook

Frequency Table (Column 4) = {'Yes': 1, 'No': 2}

Calculating Entropy
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
Total Entropy = 0.9183

Weighted Entropy for Outlook

Subset where Outlook = Rain
Subset Size = 2

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000
Weight = 2/3 = 0.6667
Contribution = 0.6667

Subset where Outlook = Sunny
Subset Size = 1

Frequency Table (Column 4) = {'No': 1}

Calculating Entropy
P(No) = 1/1 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 1/3 = 0.3333
Contribution = 0.0000

Total Weighted Entropy = 0.6667

Gain = 0.9183 - 0.6667
Information Gain (Outlook) = 0.2516

----------------------------------
Information Gain for Humidity

Frequency Table (Column 4) = {'Yes': 1, 'No': 2}

Calculating Entropy
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
Total Entropy = 0.9183

Weighted Entropy for Humidity

Subset where Humidity = Normal
Subset Size = 2

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000
Weight = 2/3 = 0.6667
Contribution = 0.6667

Subset where Humidity = High
Subset Size = 1

Frequency Table (Column 4) = {'No': 1}

Calculating Entropy
P(No) = 1/1 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 1/3 = 0.3333
Contribution = 0.0000

Total Weighted Entropy = 0.6667

Gain = 0.9183 - 0.6667
Information Gain (Humidity) = 0.2516

----------------------------------
Information Gain for Wind

Frequency Table (Column 4) = {'Yes': 1, 'No': 2}

Calculating Entropy
P(Yes) = 1/3 = 0.3333
-P(Yes) log2(P(Yes)) = 0.5283
P(No) = 2/3 = 0.6667
-P(No) log2(P(No)) = 0.3900
Total Entropy = 0.9183

Weighted Entropy for Wind

Subset where Wind = Weak
Subset Size = 2

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000
Weight = 2/3 = 0.6667
Contribution = 0.6667

Subset where Wind = Strong
Subset Size = 1

Frequency Table (Column 4) = {'No': 1}

Calculating Entropy
P(No) = 1/1 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 1/3 = 0.3333
Contribution = 0.0000

Total Weighted Entropy = 0.6667

Gain = 0.9183 - 0.6667
Information Gain (Wind) = 0.2516

Best Attribute Selected Outlook

Branch: Outlook = Sunny

Leaf Node No

Branch: Outlook = Rain

Calculating Information Gain for attributes

----------------------------------
Information Gain for Humidity

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000

Weighted Entropy for Humidity

Subset where Humidity = Normal
Subset Size = 2

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000
Weight = 2/2 = 1.0000
Contribution = 1.0000

Total Weighted Entropy = 1.0000

Gain = 1.0000 - 1.0000
Information Gain (Humidity) = 0.0000

----------------------------------
Information Gain for Wind

Frequency Table (Column 4) = {'Yes': 1, 'No': 1}

Calculating Entropy
P(Yes) = 1/2 = 0.5000
-P(Yes) log2(P(Yes)) = 0.5000
P(No) = 1/2 = 0.5000
-P(No) log2(P(No)) = 0.5000
Total Entropy = 1.0000

Weighted Entropy for Wind

Subset where Wind = Weak
Subset Size = 1

Frequency Table (Column 4) = {'Yes': 1}

Calculating Entropy
P(Yes) = 1/1 = 1.0000
-P(Yes) log2(P(Yes)) = -0.0000
Total Entropy = 0.0000
Weight = 1/2 = 0.5000
Contribution = 0.0000

Subset where Wind = Strong
Subset Size = 1

Frequency Table (Column 4) = {'No': 1}

Calculating Entropy
P(No) = 1/1 = 1.0000
-P(No) log2(P(No)) = -0.0000
Total Entropy = 0.0000
Weight = 1/2 = 0.5000
Contribution = 0.0000

Total Weighted Entropy = 0.0000

Gain = 1.0000 - 0.0000
Information Gain (Wind) = 1.0000

Best Attribute Selected Wind

Branch: Wind = Weak

Leaf Node Yes

Branch: Wind = Strong

Leaf Node No


Final Decision Tree:
{'Temperature': {'Mild': 'Yes', 'Hot': {'Outlook': {'Sunny': 'No', 'Overcast': 'Yes'}}, 'Cool': {'Outlook': {'Sunny': 'No', 'Rain': {'Wind': {'Weak': 'Yes', 'Strong': 'No'}}}}}}

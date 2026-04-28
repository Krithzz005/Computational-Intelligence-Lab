[23bcs074@mepcolinux steps]$cat bayes.py
print("--- Bayes Theorem ---")
pa = float(input("Enter P(A): "))
pbgna = float(input("Enter P(B|A): "))
pb = float(input("Enter P(B): "))

if pb == 0:
    print("Error: Division by zero is not possible.")
else:
    # Step 1: Logic
    p_a_given_b = (pbgna * pa) / pb

    print(f"\nStep 1: Calculate P(A|B)")
    print(f"Formula: P(A|B) = (P(B|A) * P(A)) / P(B)")
    print(f"Calculation: ({pbgna} * {pa}) / {pb}")
    print(f"Result: P(A|B) = {p_a_given_b:.4f}")

[23bcs074@mepcolinux steps]$python3 bayes.py
--- Bayes Theorem ---
Enter P(A): 0.3
Enter P(B|A): 0.8
Enter P(B): 0.5

Step 1: Calculate P(A|B)
Formula: P(A|B) = (P(B|A) * P(A)) / P(B)
Calculation: (0.8 * 0.3) / 0.5
Result: P(A|B) = 0.4800
[23bcs074@mepcolinux steps]$cat dices.py
def dice_probability():
    print("--- Dice Probability ---")
    t = int(input("Enter target sum (2-12): "))
    total_outcomes = 36
    favorable = []

    # Simple nested loop for 2 dice
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == t:
                favorable.append((i, j))

    p = len(favorable) / total_outcomes

    print(f"\nStep 1: Identify Favorable Outcomes")
    print(f"Outcomes: {favorable}")
    print(f"Count (n): {len(favorable)}")

    print(f"\nStep 2: Calculate Probability")
    print(f"Formula: P = Favorable Outcomes / Total Outcomes (36)")
    print(f"Calculation: {len(favorable)} / {total_outcomes}")
    print(f"Result: Probability = {p:.4f}")

dice_probability()

[23bcs074@mepcolinux steps]$python3 dices.py
--- Dice Probability ---
Enter target sum (2-12): 7

Step 1: Identify Favorable Outcomes
Outcomes: [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
Count (n): 6

Step 2: Calculate Probability
Formula: P = Favorable Outcomes / Total Outcomes (36)
Calculation: 6 / 36
Result: Probability = 0.1667
[23bcs074@mepcolinux steps]$cat fjoint.py
import csv

print("--- Joint Probability (A, B, C) ---")
p = {}

# Take CSV file path from user
file_path = input("Enter CSV file path: ")

# Expected CSV format:
# A,B,C,P
# 0,0,0,0.1
# 0,0,1,0.05
# ... (all 8 rows)

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        a = int(row['A'])
        b = int(row['B'])
        c = int(row['C'])
        prob = float(row['P'])
        p[(a, b, c)] = prob

# (Rest of your code EXACTLY SAME)

while True:
    print("\n--- Extended Menu ---")
    print("1. Find Joint Probability P(A,B,C)")
    print("2. Find Marginal Probability (e.g., P(A), P(B), or P(C))")
    print("3. Find Conditional Probability P(A | B,C)")
    print("4. Find Conditional Probability P(B | A,C)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        ta, tb, tc = map(int, input("Enter values for A, B, C (e.g., 1 0 1): ").split())
        print(f"Result: P(A={ta}, B={tb}, C={tc}) = {p[(ta, tb, tc)]}")

    elif choice == '2':
        var = input("Which variable's marginal probability? (A/B/C): ").upper()
        val = int(input(f"Value for {var} (0 or 1): "))

        if var == 'A':
            components = [p[(val, b, c)] for b in [0, 1] for c in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nFormula: P(A={val}) = Summation P(A={val}, B, C)")
            print(f"Calculation: {detail_str}")
        elif var == 'B':
            components = [p[(a, val, c)] for a in [0, 1] for c in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nFormula: P(B={val}) = Summation P(A, B={val}, C)")
            print(f"Calculation: {detail_str}")
        else:
            components = [p[(a, b, val)] for a in [0, 1] for b in [0, 1]]
            res = sum(components)
            detail_str = " + ".join([str(v) for v in components])
            print(f"\nFormula: P(C={val}) = Summation P(A, B, C={val})")
            print(f"Calculation: {detail_str}")

        print(f"Result: Marginal P({var}={val}) = {res:.4f}")

    elif choice == '3':
        ta, tb, tc = map(int, input("Enter target A, B, C (e.g., 1 1 0): ").split())
        p_abc = p[(ta, tb, tc)]
        v1, v2 = p[(0, tb, tc)], p[(1, tb, tc)]
        p_bc = v1 + v2

        print(f"\nFormula: P(A|B,C) = P(A,B,C) / P(B,C)")
        print(f"Step 1: Numerator P(A={ta}, B={tb}, C={tc}) = {p_abc}")
        print(f"Step 2: Denominator P(B={tb}, C={tc}) = {v1} + {v2} = {p_bc}")
        print(f"Step 3: {p_abc} / {p_bc}")
        print(f"Result: P(A={ta}|B={tb},C={tc}) = {p_abc/p_bc if p_bc > 0 else 0:.4f}")

    elif choice == '4':
        ta, tb, tc = map(int, input("Enter values for A, B, C (e.g., 0 1 1): ").split())
        p_abc = p[(ta, tb, tc)]
        v1, v2 = p[(ta, 0, tc)], p[(ta, 1, tc)]
        p_ac = v1 + v2

        print(f"\nFormula: P(B|A,C) = P(A,B,C) / P(A,C)")
        print(f"Step 1: Numerator P(A={ta}, B={tb}, C={tc}) = {p_abc}")
        print(f"Step 2: Denominator P(A={ta}, C={tc}) = {v1} + {v2} = {p_ac}")
        print(f"Step 3: {p_abc} / {p_ac}")
        print(f"Result: P(B={tb}|A={ta},C={tc}) = {p_abc/p_ac if p_ac > 0 else 0:.4f}")

    elif choice == '5':
        print("Bye!")
        break
    else:
        print("Invalid Choice!")
[23bcs074@mepcolinux steps]$cat ip1.csv
A,B,C,P
0,0,0,0.1
0,0,1,0.05
0,1,0,0.1
0,1,1,0.15
1,0,0,0.1
1,0,1,0.1
1,1,0,0.2
1,1,1,0.2
[23bcs074@mepcolinux steps]$python3 fjoint.py
--- Joint Probability (A, B, C) ---
Enter CSV file path: ip1.csv

--- Extended Menu ---
1. Find Joint Probability P(A,B,C)
2. Find Marginal Probability (e.g., P(A), P(B), or P(C))
3. Find Conditional Probability P(A | B,C)
4. Find Conditional Probability P(B | A,C)
5. Exit
Enter choice (1-5): 1
Enter values for A, B, C (e.g., 1 0 1): 1 1 1
Result: P(A=1, B=1, C=1) = 0.2

--- Extended Menu ---
1. Find Joint Probability P(A,B,C)
2. Find Marginal Probability (e.g., P(A), P(B), or P(C))
3. Find Conditional Probability P(A | B,C)
4. Find Conditional Probability P(B | A,C)
5. Exit
Enter choice (1-5): 2
Which variable's marginal probability? (A/B/C): a
Value for A (0 or 1): 1

Formula: P(A=1) = Summation P(A=1, B, C)
Calculation: 0.1 + 0.1 + 0.2 + 0.2
Result: Marginal P(A=1) = 0.6000

--- Extended Menu ---
1. Find Joint Probability P(A,B,C)
2. Find Marginal Probability (e.g., P(A), P(B), or P(C))
3. Find Conditional Probability P(A | B,C)
4. Find Conditional Probability P(B | A,C)
5. Exit
Enter choice (1-5): 3
Enter target A, B, C (e.g., 1 1 0): 1 1 0

Formula: P(A|B,C) = P(A,B,C) / P(B,C)
Step 1: Numerator P(A=1, B=1, C=0) = 0.2
Step 2: Denominator P(B=1, C=0) = 0.1 + 0.2 = 0.30000000000000004
Step 3: 0.2 / 0.30000000000000004
Result: P(A=1|B=1,C=0) = 0.6667

--- Extended Menu ---
1. Find Joint Probability P(A,B,C)
2. Find Marginal Probability (e.g., P(A), P(B), or P(C))
3. Find Conditional Probability P(A | B,C)
4. Find Conditional Probability P(B | A,C)
5. Exit
Enter choice (1-5): 4
Enter values for A, B, C (e.g., 0 1 1): 0 1 1

Formula: P(B|A,C) = P(A,B,C) / P(A,C)
Step 1: Numerator P(A=0, B=1, C=1) = 0.15
Step 2: Denominator P(A=0, C=1) = 0.05 + 0.15 = 0.2
Step 3: 0.15 / 0.2
Result: P(B=1|A=0,C=1) = 0.7500

--- Extended Menu ---
1. Find Joint Probability P(A,B,C)
2. Find Marginal Probability (e.g., P(A), P(B), or P(C))
3. Find Conditional Probability P(A | B,C)
4. Find Conditional Probability P(B | A,C)
5. Exit
Enter choice (1-5): 5
Bye!
[23bcs074@mepcolinux ex9]$exit
exit

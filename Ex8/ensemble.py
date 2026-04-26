[23bcs074@mepcolinux ex8]$cat ens.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from tabulate import tabulate

# -------------------------------
# 1. LOAD DATA
# -------------------------------
data = np.loadtxt("sonar.csv", delimiter=",", dtype=str)

X = data[:, :-1].astype(float)
y = data[:, -1]

y = np.where(y == 'R', 0, 1)

# -------------------------------
# FUNCTION TO RUN MODEL
# -------------------------------
def run_model(test_size):
    print(f"\n===== Split {int((1-test_size)*100)}-{int(test_size*100)} =====")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:\n", cm)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\nMetrics:")
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    return [f"{int((1-test_size)*100)}-{int(test_size*100)}",
            accuracy, precision, recall, f1]

# -------------------------------
# 2. RUN FOR ALL SPLITS
# -------------------------------
results = []
results.append(run_model(0.2))   # 80-20
results.append(run_model(0.3))   # 70-30
results.append(run_model(0.35))  # 65-35

# -------------------------------
# 3. FINAL COMPARISON TABLE
# -------------------------------
print("\n===== FINAL COMPARISON =====\n")

print(tabulate(results,
               headers=["Split", "Accuracy", "Precision", "Recall", "F1 Score"],
               tablefmt="grid"))
[23bcs074@mepcolinux ex8]$python3 ens.py
===== Split 80-20 =====

Training Samples: 166
Testing Samples : 42

Confusion Matrix:
 [[14  2]
 [ 4 22]]

Metrics:
Accuracy : 0.8571428571428571
Precision: 0.9166666666666666
Recall   : 0.8461538461538461
F1 Score : 0.88

===== Split 70-30 =====

Training Samples: 145
Testing Samples : 63

Confusion Matrix:
 [[25  3]
 [ 6 29]]

Metrics:
Accuracy : 0.8571428571428571
Precision: 0.90625
Recall   : 0.8285714285714286
F1 Score : 0.8656716417910447

===== Split 65-35 =====

Training Samples: 135
Testing Samples : 73

Confusion Matrix:
 [[28  6]
 [ 6 33]]

Metrics:
Accuracy : 0.8356164383561644
Precision: 0.8461538461538461
Recall   : 0.8461538461538461
F1 Score : 0.8461538461538461

===== FINAL COMPARISON =====

+---------+------------+-------------+----------+------------+
| Split   |   Accuracy |   Precision |   Recall |   F1 Score |
+=========+============+=============+==========+============+
| 80-20   |   0.857143 |    0.916667 | 0.846154 |   0.88     |
+---------+------------+-------------+----------+------------+
| 70-30   |   0.857143 |    0.90625  | 0.828571 |   0.865672 |
+---------+------------+-------------+----------+------------+
| 65-35   |   0.835616 |    0.846154 | 0.846154 |   0.846154 |
+---------+------------+-------------+----------+------------+
[23bcs074@mepcolinux ex8]$exit
exit

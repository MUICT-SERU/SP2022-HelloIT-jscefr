import json
import os
from scipy import stats
import pandas as pd
from scipy.stats import normaltest, mannwhitneyu, ttest_ind, shapiro
import numpy as np
from cliffs_delta import cliffs_delta
import sys

PROJECT = str(sys.argv[1])
SCORING_SYSTEM = str(sys.argv[2])
TYPE = "TEST"

all_test_dataset = []
all_non_test_dataset = []
df = pd.DataFrame(columns=["project", "stat", "p_val", "is_diff"])
# for project in PROJECT:
f = open(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/TEST/dim_x.json')
test_dataset = json.loads(f.read())
all_test_dataset.append(test_dataset)
f.close()
f = open(f'processed_data/{SCORING_SYSTEM}/{PROJECT}/TEST/dim_y.json')
non_test_dataset = json.loads(f.read())
all_non_test_dataset.append(non_test_dataset)
f.close()

print(f"{PROJECT} x: {len(test_dataset)}, y: {len(non_test_dataset)}")
isnormal = normaltest(test_dataset).pvalue >= 0.005 and normaltest(
    non_test_dataset).pvalue >= 0.005

stat, p_val, r = 0, 0, 0

if isnormal:
    stat, p_val = ttest_ind(
        test_dataset, non_test_dataset, alternative='two-sided', trim=0)
    print('ttest')
else:
    stat, p_val = mannwhitneyu(
        test_dataset, non_test_dataset, method="auto")
    n1, n2 = len(test_dataset), len(non_test_dataset)
    # r = np.sqrt(stat / (n1 * n2))
    # d = (2 * r) / np.sqrt(1 - r**2)
    # d = 1 - (2*stat)/(n1*n2)
    d = cliffs_delta(test_dataset, non_test_dataset)

    print("Effect size (r):", d)
    print('mannwhitneyu')

new_line = {"project": PROJECT, "stat": stat, "p_val": p_val,
            "effect_size": d, "is_diff": p_val < 0.05}
df = pd.concat([df, pd.DataFrame([new_line])], ignore_index=True)

# flatten_all_test_dataset = [
#     item for sublist in all_test_dataset for item in sublist]
# flatten_all_non_test_dataset = [
#     item for sublist in all_non_test_dataset for item in sublist]
# isnormal = normaltest(flatten_all_test_dataset).pvalue >= 0.005 and normaltest(
#     flatten_all_non_test_dataset).pvalue >= 0.005

# print(f"x: {len(flatten_all_test_dataset)}, y: {len(flatten_all_non_test_dataset)}")
# stat, p_val, eff = 0, 0, 0

# if isnormal:
#     stat, p_val = ttest_ind(flatten_all_test_dataset, flatten_all_non_test_dataset,
#                             alternative='two-sided', trim=0)
#     print('ttest')
# else:
#     stat, p_val = mannwhitneyu(
#         flatten_all_test_dataset, flatten_all_non_test_dataset, method="auto")
#     n1, n2 = len(flatten_all_test_dataset), len(flatten_all_non_test_dataset)
#     # r = np.sqrt(stat / (n1 * n2))
#     # d = (2 * r) / np.sqrt(1 - r**2)
#     # d = 1 - (2*stat)/(n1*n2)
#     d = cliffs_delta(test_dataset, non_test_dataset)

#     print("Effect size (r):", d)
#     # print('mannwhitneyu', eff)

# new_line = {"project": "all", "stat": stat,
#             "p_val": p_val, "effect_size": d, "is_diff": p_val < 0.05}
# df = pd.concat([df, pd.DataFrame([new_line])], ignore_index=True)
df.to_csv(f"summary/{PROJECT}/TEST.csv", index=False)

# with open(f'summary/{SCORING_SYSTEM}/raw_test.csv', 'w') as f:
#     f.write('x,\n')
#     for x in flatten_all_test_dataset:
#         f.write(f'{x}\n')

# with open(f'summary/{SCORING_SYSTEM}/raw_non_test.csv', 'w') as f:
#     f.write('y,\n')
#     for y in flatten_all_non_test_dataset:
#         f.write(f'{y}\n')

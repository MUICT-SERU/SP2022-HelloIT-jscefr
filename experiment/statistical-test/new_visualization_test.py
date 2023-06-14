import json
import os
from scipy import stats
from scipy.stats import normaltest, mannwhitneyu, ttest_ind, shapiro
import scipy
import numpy as np
import matplotlib.pyplot as plt
import datashader as ds
from datashader.mpl_ext import dsshow
import pandas as pd
import sys

# PROJECT = ["next", "react", "sveltekit"]
TYPE = ["LAYER", "LENGTH"]
# SCORING_TYPE = "MAX"

PROJECT = str(sys.argv[1])
SCORING_TYPE = str(sys.argv[2])

test_dataset = []
non_test_dataset = []

f = open(f'processed_data/{SCORING_TYPE}/{PROJECT}/TEST/dim_x.json')
dataset_1 = json.loads(f.read())
test_dataset.extend(dataset_1)
f.close()

f = open(f'processed_data/{SCORING_TYPE}/{PROJECT}/TEST/dim_y.json')
dataset_2 = json.loads(f.read())
non_test_dataset.extend(dataset_2)
f.close()

# Violin plot
bars = ['Test', 'Non-Test']
figure, axe = plt.subplots(nrows=1,
                            ncols=2,
                            figsize=(8, 4),
                            sharey=True)

figure.suptitle(f"({PROJECT}) test and non-test file", fontsize=14)
plt.ylim(0.5, 6.5)
axe[0].set_title('Test file', fontsize=14)
axe[0].set_ylabel('Competency Level', fontsize=14)
axe[0].yaxis.set_ticks([1, 2, 3, 4, 5, 6])
axe[0].yaxis.set_ticklabels(
    ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
axe[0].violinplot(dataset_1, showmedians=True)

axe[1].set_title('Non-test file', fontsize=14)
axe[1].yaxis.set_ticks([1, 2, 3, 4, 5, 6])
# axe[1].set_ylabel('Competency Level', fontsize=12)
axe[1].yaxis.set_ticklabels(
    ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
axe[1].violinplot(dataset_2, showmedians=True)
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/violin-{PROJECT}-test.pdf", bbox_inches='tight', dpi=150)
plt.close('all')

# Box plot
plt.ylim(0.5, 6.5)
plt.xlabel(f'competency level distribution ({PROJECT})', fontsize=14)
plt.ylabel('Competency Level', fontsize=14)
plt.yticks([1, 2, 3, 4, 5, 6], ['A1', 'A2',
                                'B1', 'B2', 'C1', 'C2'], fontsize=12)
plt.xticks([1, 2], bars, fontsize=14)
plt.boxplot([dataset_1, dataset_2], labels=bars, showmeans=True)
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/box-{PROJECT}-test.pdf", bbox_inches='tight', dpi=150)
plt.close('all')

# Histogram
plt.xlabel('Competency Level', fontsize=14)
plt.ylabel('Code construct count', fontsize=14)
plt.title(f'Non-test files ({PROJECT})', fontsize=14)
plt.grid(True)
header = [
    "A1",
    "A2",
    "B1",
    "B2",
    "C1",
    "C2",
]

plt.hist(np.array(dataset_2), bins=range(1, 8), align='left', rwidth=0.5)

plt.xticks(np.arange(1, 7), ['A1', 'A2', 'B1',
            'B2', 'C1', 'C2'], fontsize=12)
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/hist-{PROJECT}-nontestfile.pdf",
            bbox_inches='tight', dpi=150)
plt.close('all')

# Histogram
plt.xlabel('Competency Level', fontsize=14)
plt.ylabel('Code construct count', fontsize=14)
plt.title(f'Test files ({PROJECT})', fontsize=14)
plt.grid(True)
header = [
    "A1",
    "A2",
    "B1",
    "B2",
    "C1",
    "C2",
]

plt.hist(np.array(dataset_1), bins=range(1, 8), align='left', rwidth=0.5)

plt.xticks(np.arange(1, 7), ['A1', 'A2', 'B1',
            'B2', 'C1', 'C2'], fontsize=12)
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/hist-{PROJECT}-testfile.pdf",
            bbox_inches='tight', dpi=150)
plt.close('all')

import json
import os
import shutil
from scipy import stats
from scipy.stats import normaltest, mannwhitneyu, ttest_ind, shapiro
import scipy
import numpy as np
import matplotlib.pyplot as plt
import datashader as ds
from datashader.mpl_ext import dsshow
import pandas as pd
import sys


def using_datashader(ax, x, y):
    df = pd.DataFrame(dict(x=x, y=y))
    # print(df)
    dsartist = dsshow(
        df,
        ds.Point("x", "y"),
        ds.count(),
        # legend_font_size=16,
        # vmin=0,
        # vmax=100,
        # norm="linear",
        norm="log",
        aspect="auto",
        ax=ax,
        width_scale=0.05,
        height_scale=0.05,
    )

    plt.colorbar(dsartist)


PROJECT = str(sys.argv[1])
SCORING_TYPE = str(sys.argv[2])
TYPE = ["LAYER", "LENGTH"]

try:
    shutil.rmtree(f'fig/{PROJECT}/{SCORING_TYPE}')
except FileNotFoundError:
    pass

os.makedirs(f'fig/{PROJECT}/{SCORING_TYPE}')

data_x = []
data_y = []

for ttype in TYPE:
    # data_type_x = []
    # data_type_y = []
    # for project in PROJECT:
    f = open(
        f'processed_data/{SCORING_TYPE}/{PROJECT}/{ttype}/dim_x.json')
    dataset_1 = json.loads(f.read())
    # data_type_x.append(dataset_1)
    f.close()
    f = open(
        f'processed_data/{SCORING_TYPE}/{PROJECT}/{ttype}/dim_y.json')
    dataset_2 = json.loads(f.read())
    # data_type_y.append(dataset_2)
    f.close()

    fig, ax = plt.subplots()
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    ax.yaxis.set_ticks([1, 2, 3, 4, 5, 6])
    ax.yaxis.set_ticklabels(
        ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
    title = f"File Depth ({PROJECT})" if ttype == 'LAYER' else f"Filename Length ({PROJECT})"
    ax.set_title(title, fontsize=14)
    plt.ylabel('Competency Level', fontsize=14)
    if ttype == 'LAYER':
        plt.xlabel('File Depth', fontsize=14)
    else:
        plt.xlabel(f'Filename Length', fontsize=14)
    x = np.random.normal(size=100000)
    y = x * 3 + np.random.normal(size=100000)
    using_datashader(ax, dataset_1, dataset_2)
    # using_datashader(ax, x, y)
    # plt.show()
    plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/scatter-{PROJECT}-{ttype}.pdf",
                bbox_inches='tight', dpi=150)
        # break
    # flatten_x = [item for sublist in data_type_x for item in sublist]
    # flatten_y = [item for sublist in data_type_y for item in sublist]
    # fig, ax = plt.subplots()
    # plt.xticks(fontsize=12)
    # plt.yticks(fontsize=12)
    # ax.yaxis.set_ticks([0, 1, 2, 3, 4, 5, 6, 7])
    # ax.yaxis.set_ticklabels(
    #     ['', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', ''], fontsize=12)
    # title = f"All project with File Depth" if ttype == 'LAYER' else f"All project with Filename Length"
    # ax.set_title(title, fontsize=14)
    # plt.ylabel('Competency Level', fontsize=14)
    # if ttype == 'LAYER':
    #     plt.xlabel('File Depth', fontsize=14)
    # else:
    #     plt.xlabel(f'Filename Length', fontsize=14)
    # using_datashader(ax, flatten_x, flatten_y)
    # # using_datashader(ax, x, y)
    # # plt.show()
    # plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/scatter-all-{ttype}.pdf",
    #             bbox_inches='tight', dpi=150)
    # plt.close('all')
    # # break
    # data_x.append(data_type_x)
    # data_y.append(data_type_y)

# for score in ["MAX", "ALL"]:
    for project in PROJECT:
        f = open(f'processed_data/{SCORING_TYPE}/{PROJECT}/LAYER/dim_y.json')
        dataset_1 = json.loads(f.read())
        # data_type_y.append(dataset_1)
        f.close()
        # Fixing random state for reproducibility
        # np.random.seed(19680801)

        # mu, sigma = 100, 15
        # x = mu + sigma * np.random.randn(10000)

        # the histogram of the data
        # print(react_dataset)
        # narray = np.array(dataset_1)
        # n, bins, patches = plt.hist(narray)

        # plt.axis([0, 6, 0, 1800])
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.xlabel('Competency Level', fontsize=14)
        label = "Code Construct Count" if SCORING_TYPE == "ALL" else "File Count"
        plt.ylabel(label, fontsize=14)
        title = f' Compentency in each code construct ({PROJECT})' if SCORING_TYPE == "ALL" else f' Compentency in each file ({PROJECT})'
        plt.title(title, fontsize=14)
        # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        # plt.xlim(40, 160)
        # plt.ylim(0, 0.03)
        plt.grid(True)

        header = [
            "A1",
            "A2",
            "B1",
            "B2",
            "C1",
            "C2",
        ]

        plt.hist(np.array(dataset_1), bins=range(
            1, 8), align='left', rwidth=0.5)

        # Set the x-axis tick labels
        plt.xticks(np.arange(1, 7), [
            'A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
        # plt.hist(np.array(dataset_1), bins=range(1,8),  align='left', rwidth=0.5)
        # plt.show()
        plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/hist-{PROJECT}-{SCORING_TYPE}.pdf",
                    bbox_inches='tight', dpi=150)
        plt.close('all')

# Violin plot
# project = 'all'
bars = ['Test', 'Non-Test']
figure, axe = plt.subplots(nrows=1,
                           ncols=2,
                           figsize=(8, 4),
                           sharey=True)

# figure.suptitle(f"({PROJECT}) test and non-test file", fontsize=14)

axe[0].set_title('Test file', fontsize=14)
axe[0].set_ylabel('Competency Level', fontsize=14)
axe[0].yaxis.set_ticks([1, 2, 3, 4, 5, 6])
axe[0].yaxis.set_ticklabels(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
axe[0].violinplot(dataset_1, showmedians=True)

axe[1].set_title('Non-test file', fontsize=14)
axe[1].yaxis.set_ticks([1, 2, 3, 4, 5, 6])
# axe[1].set_ylabel('Competency Level', fontsize=12)
axe[1].yaxis.set_ticklabels(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], fontsize=12)
axe[1].violinplot(dataset_2, showmedians=True)
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/violin-{PROJECT}-test.pdf",
            bbox_inches='tight', dpi=150)
plt.close('all')

# Box plot
# plt.ylim(0.5, 6.5)
# plt.xlabel(f'competency level distribution ({PROJECT})', fontsize=14)
# plt.ylabel('Competency Level', fontsize=14)
# plt.yticks([1, 2, 3, 4, 5, 6], ['A1', 'A2',
#                                 'B1', 'B2', 'C1', 'C2'], fontsize=14)
# plt.xticks([1, 2], bars, fontsize=14)
# plt.boxplot([dataset_1, dataset_2], labels=bars, showmeans=True)
# plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/box-all-test.png", bbox_inches='tight', dpi=150)
# plt.close('all')

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

plt.xticks(np.arange(1, 7), ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/hist-{PROJECT}-testfile.pdf",
            bbox_inches='tight', dpi=150)
plt.close('all')

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

plt.xticks(np.arange(1, 7), ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
plt.savefig(f"fig/{PROJECT}/{SCORING_TYPE}/hist-{PROJECT}-nontestfile.pdf",
            bbox_inches='tight', dpi=150)

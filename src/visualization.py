import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_heatmap(data, filename="heatmap.png"):
    """
    data: numpy array 或 pandas DataFrame
    输出: 保存热力图到 output/figures/
    """
    plt.figure(figsize=(8, 6))

    # 使用 seaborn 画热力图
    sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)

    plt.title("Heatmap of Scores")
    plt.xlabel("Feature Index")
    plt.ylabel("Sample Index")

    plt.savefig(f"output/figures/{filename}", dpi=300)
    plt.close()

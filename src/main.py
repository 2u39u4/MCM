import numpy as np
from visualization import plot_heatmap

if __name__ == "__main__":
    # 模拟数据：10 个样本，3 个指标
    data = np.random.rand(10, 3) * 10

    # 输出前 5 行看看
    print("Sample data:\n", data[:5])

    # 画热力图
    plot_heatmap(data)
    print("Heatmap saved to output/figures/heatmap.png")

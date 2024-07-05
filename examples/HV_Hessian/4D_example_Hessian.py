import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from hvd import HypervolumeDerivatives

sns.set(font_scale=1.3, rc={"text.usetex": True})

ref = np.array([17, 35, 7, 10])
hvh = HypervolumeDerivatives(4, 4, ref, minimization=True)
X = np.array([(16, 23, 1, 8), (14, 32, 2, 5), (12, 27, 3, 1), (10, 21, 4, 9), (8, 33, 5, 3)])
out = hvh._compute_hessian(X)

assert np.all(
    out["HVdY2"]
    == np.array(
        [
            [0, 9, 24, 37, 0, -2, -6, 0, 0, -5, -10, 0, 0, 0, -4, -12, 0, -0, -0, 0],
            [9, 0, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -3, 0, 0, 0, 0],
            [24, 2, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [37, 6, 12, 0, 0, -1, -3, 0, 0, -4, -5, 0, 0, 0, 0, 0, 0, -0, -0, 0],
            [0, 0, 0, 0, 0, 5, 15, 3, 0, 0, -15, 0, 0, 0, 0, -0, 0, -0, 0, 0],
            [-2, 0, 0, -1, 5, 0, 13, 3, 0, 0, -13, 0, 0, 0, 0, -0, 0, 0, 0, 0],
            [-6, 0, 0, -3, 15, 13, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 3, 9, 0, 0, 0, -9, 0, 0, 0, 0, 0, 0, -0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 72, 32, 0, 0, -8, -20, 0, -12, -12, -4],
            [-5, 0, 0, -4, 0, 0, 0, 0, 33, 0, 43, 20, 0, 0, -4, -12, 0, 0, 0, 0],
            [-10, 0, 0, -5, -15, -13, 0, -9, 72, 43, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 32, 20, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 14, 38, 0, -2, -2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 7, 21, 0, 0, 0, 0],
            [-4, -1, 0, 0, -0, -0, 0, 0, -8, -4, 0, 0, 14, 7, 0, 54, 0, 0, 0, 0],
            [-12, -3, 0, 0, -0, -0, 0, 0, -20, -12, 0, 0, 38, 21, 54, 0, 0, -4, -4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 14, 4],
            [0, 0, 0, -0, 0, 0, 0, -0, -12, 0, 0, 0, -2, 0, 0, -4, 14, 0, 26, 8],
            [0, 0, 0, -0, 0, 0, 0, -0, -12, 0, 0, 0, -2, 0, 0, -4, 14, 26, 0, 8],
            [0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 0, 0, 4, 8, 8, 0],
        ]
    )
)

H = out["HVdY2"]
H[H == 0] = 0
s = [f"$y_{i}^" + "{" + f"({j})" + "}$" for j in range(1, 6) for i in range(1, 5)]
df = pd.DataFrame(H, columns=s, index=s)

fig, ax = plt.subplots(1, 1, figsize=(9, 7.2), sharex=True, sharey=True)
plot = sns.heatmap(df, annot=True, center=0, cmap="bwr", linewidths=1, linecolor="k", ax=ax)
plt.tight_layout()
# fig.savefig("example4.pdf")
plt.show()

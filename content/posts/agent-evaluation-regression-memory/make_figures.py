from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
BLUE = "#4C72B0"
RED = "#C44E52"
GRAY = "#8C8C8C"
DARK = "#2F3337"


def configure() -> None:
    plt.rcParams.update(
        {
            "figure.figsize": (7, 4.5),
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "font.size": 10,
            "axes.titlesize": 14,
            "axes.labelsize": 10,
            "axes.edgecolor": "#D0D3D6",
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "grid.color": "#E6E8EA",
            "grid.linewidth": 0.8,
            "legend.frameon": False,
        }
    )


def save(fig: plt.Figure, stem: str) -> None:
    fig.tight_layout(pad=1.4)
    fig.savefig(ASSETS / f"{stem}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(ASSETS / f"{stem}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def benchmark_gap() -> None:
    names = ["WebArena", "OSWorld"]
    agent = np.array([14.41, 12.24])
    human = np.array([78.24, 72.36])
    y = np.arange(len(names))
    height = 0.28

    fig, ax = plt.subplots()
    ax.barh(y - height / 2, agent, height, color=BLUE, label="Best reported agent")
    ax.barh(y + height / 2, human, height, color=GRAY, label="Human")
    for values, offsets in ((agent, y - height / 2), (human, y + height / 2)):
        for value, pos in zip(values, offsets):
            ax.text(value + 1.2, pos, f"{value:.2f}%", va="center", color=DARK)

    ax.set_yticks(y, names)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 20))
    ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    ax.set_xlabel("Task success rate")
    ax.set_title("Early agent benchmarks exposed a large reliability gap", loc="left")
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.legend(loc="center right")
    save(fig, "figure_benchmark_gap")


def reliability_divergence() -> None:
    p = 0.75
    k = np.arange(1, 11)
    pass_at_k = 1 - (1 - p) ** k
    pass_to_k = p**k

    fig, ax = plt.subplots()
    ax.plot(k, pass_at_k * 100, marker="o", color=BLUE, linewidth=2.4, label="pass@k: at least one success")
    ax.plot(k, pass_to_k * 100, marker="o", color=RED, linewidth=2.4, label="pass^k: all attempts succeed")
    ax.axhline(75, color=GRAY, linestyle="--", linewidth=1)
    ax.text(9.9, 77.2, "per-trial p = 75%", color=GRAY, ha="right", va="bottom")
    ax.set_xticks(k)
    ax.set_ylim(0, 104)
    ax.set_xlabel("Number of attempts, k")
    ax.set_ylabel("Probability")
    ax.set_title("Discovery and reliability diverge as attempts increase", loc="left")
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    ax.legend(loc="center right")
    save(fig, "figure_reliability_divergence")


def paired_gate() -> None:
    labels = ["PASS", "INCONCLUSIVE\n(worked example)", "FAIL"]
    estimates = np.array([-0.5, -3.75, -5.0])
    lower = np.array([-1.5, -8.6, -7.0])
    upper = np.array([0.5, 1.1, -3.0])
    colors = [BLUE, GRAY, RED]
    y = np.arange(3)[::-1]

    fig, ax = plt.subplots()
    ax.axvspan(-10, -2, color=RED, alpha=0.07)
    ax.axvline(-2, color=RED, linestyle="--", linewidth=1.5)
    ax.axvline(0, color=GRAY, linewidth=1)
    for idx, pos in enumerate(y):
        ax.errorbar(
            estimates[idx],
            pos,
            xerr=[[estimates[idx] - lower[idx]], [upper[idx] - estimates[idx]]],
            fmt="o",
            color=colors[idx],
            ecolor=colors[idx],
            capsize=5,
            linewidth=2.2,
            markersize=7,
        )
    ax.set_yticks(y, labels)
    ax.set_xlim(-10, 3)
    ax.set_ylim(-0.7, 2.7)
    ax.text(-9.7, 2.45, "loss exceeds budget", color=RED, va="center")
    ax.text(-1.8, 2.45, "within budget", color=DARK, va="center")
    ax.text(-1.85, -0.45, "margin = -2 pp", color=RED, va="center")
    ax.set_xlabel("Paired success-rate difference: candidate - baseline (pp)")
    ax.set_title("Non-inferiority gates need three verdicts", loc="left")
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    save(fig, "figure_paired_gate")


if __name__ == "__main__":
    configure()
    ASSETS.mkdir(exist_ok=True)
    benchmark_gap()
    reliability_divergence()
    paired_gate()

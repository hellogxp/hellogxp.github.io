"""Fix Figure 4 — match Figure 5 style (wide canvas, small refined fonts)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent / "figures_preview"

# Colors matching the blue family from Figure 5
GREY = "#B0B0B0"
BLUE_LIGHT = "#A5C8E1"
BLUE_MID = "#6FA8D6"
BLUE_MAIN = "#4A90C4"
RED = "#D62728"


def main():
    methods = ["Simple\nScaling", "ITI\n(top_k=10)", "CAA\n(top_k=10)", "DoLa\n(dynamic)"]
    scores = [0.2215, 0.2437, 0.2558, 0.2778]
    baseline = 0.2215
    deltas = [f"+{(s / baseline - 1) * 100:.1f}%" for s in scores]
    colors = [GREY, BLUE_LIGHT, BLUE_MID, BLUE_MAIN]

    fig, ax = plt.subplots(figsize=(7, 3.5))
    bars = ax.bar(range(4), scores, width=0.4, color=colors,
                  edgecolor="white", linewidth=0.5)

    ax.axhline(y=baseline, color=RED, linewidth=0.5, linestyle="--", alpha=0.3)
    ax.text(3.4, baseline + 0.0003, f"Baseline = {baseline}", fontsize=5.5,
            color=RED, alpha=0.4, va="bottom")

    for bar, d in zip(bars, deltas):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.001,
                d, ha="center", va="bottom", fontsize=6, fontweight="bold",
                color="#333333")

    ax.set_xticks(range(4))
    ax.set_xticklabels(methods, fontsize=6.5)
    ax.set_ylabel("MC1 Score", fontsize=7)
    ax.set_title("Intervention Hierarchy Explained by Late Crystallization\n"
                 "(Qwen2.5-7B, TruthfulQA)",
                 fontsize=8, pad=8)
    ax.set_ylim(0.20, 0.29)
    ax.tick_params(axis="both", labelsize=6)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_linewidth(0.4)
    ax.spines["bottom"].set_linewidth(0.4)
    ax.grid(axis="y", alpha=0.15, linewidth=0.3)
    ax.set_axisbelow(True)
    plt.tight_layout()

    OUT.mkdir(exist_ok=True)
    out = OUT / "fig4_preview.png"
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

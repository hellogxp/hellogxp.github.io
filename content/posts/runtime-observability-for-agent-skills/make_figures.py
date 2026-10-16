from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

BLUE = "#4C72B0"
BLUE_DARK = "#2C3E50"
RED = "#C44E52"
GRAY = "#8C8C8C"
LIGHT_GRAY = "#D9DEE3"


def finish(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def style_axis(ax):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.grid(axis="y", alpha=0.22, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=10)


def adapter_profiles():
    agents = ["Codex", "OpenCode", "Qoder"]
    skill_runs = np.array([0, 42, 42])
    failure_events = np.array([0, 0, 24])
    clean_events = np.array([0, 0, 6])
    exact_boundary = np.array([0, 0, 6])

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    x = np.arange(len(agents))
    bars = axes[0].bar(x, skill_runs, color=[GRAY, BLUE, BLUE_DARK], width=0.55)
    axes[0].set_title("Reconstructed Skill runs", fontsize=13)
    axes[0].set_ylim(0, 46)
    axes[0].set_ylabel("Sessions (out of 42)", fontsize=11)
    axes[0].set_xticks(x, agents)
    for bar, value in zip(bars, skill_runs):
        axes[0].text(bar.get_x() + bar.get_width() / 2, value + 1.0, f"{value}/42",
                     ha="center", va="bottom", fontsize=9)
    style_axis(axes[0])

    width = 0.34
    bars_a = axes[1].bar(x - width / 2, failure_events, width, color=BLUE,
                         label="Operational failure")
    bars_b = axes[1].bar(x + width / 2, clean_events, width, color=RED, alpha=0.72,
                         label="Clean")
    axes[1].set_title("Sessions with failure-like events", fontsize=13)
    axes[1].set_ylim(0, 27)
    axes[1].set_ylabel("Sessions", fontsize=11)
    axes[1].set_xticks(x, agents)
    axes[1].legend(frameon=False, fontsize=9, loc="upper left")
    for bars, denoms in [(bars_a, [24, 24, 24]), (bars_b, [6, 6, 6])]:
        for bar, denom in zip(bars, denoms):
            value = int(bar.get_height())
            axes[1].text(bar.get_x() + bar.get_width() / 2, value + 0.6,
                         f"{value}/{denom}", ha="center", va="bottom", fontsize=9)
    style_axis(axes[1])

    bars = axes[2].bar(x, exact_boundary, color=[GRAY, GRAY, BLUE_DARK], width=0.55)
    axes[2].set_title("Exact injected boundary", fontsize=13)
    axes[2].set_ylim(0, 27)
    axes[2].set_ylabel("Operational failures (out of 24)", fontsize=11)
    axes[2].set_xticks(x, agents)
    for bar, value in zip(bars, exact_boundary):
        axes[2].text(bar.get_x() + bar.get_width() / 2, value + 0.6, f"{value}/24",
                     ha="center", va="bottom", fontsize=9)
    style_axis(axes[2])

    finish(fig, "figure_adapter_profiles")


def diagnostic_views():
    views = ["Raw", "Semantic\naliases", "Panorama", "Rule graph", "Graph +\nmodel"]
    exact = np.array([72, 49, 82, 126, 125])
    boundary = np.array([72, 108, 108, 126, 125])
    status = np.array([99, 49, 100, 126, 126])
    entailment = np.array([62, 26, 46, 126, 89])

    fig, axes = plt.subplots(1, 2, figsize=(14, 4.5))
    x = np.arange(len(views))
    width = 0.36

    bars_a = axes[0].bar(x - width / 2, boundary, width, color=BLUE, label="Boundary")
    bars_b = axes[0].bar(x + width / 2, status, width, color=BLUE, alpha=0.42,
                         label="Status")
    axes[0].set_title("A single score hides different error signatures", fontsize=13)
    axes[0].set_ylabel("Correct cases (out of 126)", fontsize=11)
    axes[0].set_ylim(0, 138)
    axes[0].set_xticks(x, views)
    axes[0].legend(frameon=False, fontsize=9, loc="upper left")
    for bars in (bars_a, bars_b):
        for bar in bars:
            value = int(bar.get_height())
            axes[0].text(bar.get_x() + bar.get_width() / 2, value + 2, str(value),
                         ha="center", va="bottom", fontsize=9)
    style_axis(axes[0])

    bars_a = axes[1].bar(x - width / 2, exact, width, color=BLUE_DARK, label="Exact answer")
    bars_b = axes[1].bar(x + width / 2, entailment, width, color=RED, alpha=0.78,
                         label="Entailed citation")
    axes[1].set_title("Answer quality and evidence quality diverge", fontsize=13)
    axes[1].set_ylabel("Cases (out of 126)", fontsize=11)
    axes[1].set_ylim(0, 138)
    axes[1].set_xticks(x, views)
    axes[1].legend(frameon=False, fontsize=9, loc="upper left")
    for bars in (bars_a, bars_b):
        for bar in bars:
            value = int(bar.get_height())
            axes[1].text(bar.get_x() + bar.get_width() / 2, value + 2, str(value),
                         ha="center", va="bottom", fontsize=9)
    style_axis(axes[1])

    finish(fig, "figure_diagnostic_views")


if __name__ == "__main__":
    adapter_profiles()
    diagnostic_views()

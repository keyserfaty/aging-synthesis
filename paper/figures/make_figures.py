"""Generate the two paper figures from verdict-table.csv."""
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.family"] = "DejaVu Serif"
mpl.rcParams["axes.spines.top"] = False
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["axes.edgecolor"] = "#444"
mpl.rcParams["axes.labelcolor"] = "#1a1a1a"
mpl.rcParams["xtick.color"] = "#1a1a1a"
mpl.rcParams["ytick.color"] = "#1a1a1a"

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "verdict-table.csv"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

BAND_ORDER = [
    "Strong",
    "Probable",
    "Suggestive",
    "Mixed",
    "Mostly hype",
    "Insufficient evidence",
]
BAND_COLORS = {
    "Strong": "#1d6638",
    "Probable": "#3d8a4f",
    "Suggestive": "#a07f1f",
    "Mixed": "#a85a1a",
    "Mostly hype": "#9a2a2a",
    "Insufficient evidence": "#5a5a5a",
}


def primary_band(verdict_field: str) -> str:
    """Map a possibly-stratified verdict cell to a single primary band."""
    v = verdict_field.lower()
    # Treat the strongest claim in a stratified verdict as the primary band
    if "strong" in v:
        return "Strong"
    if "probable" in v:
        return "Probable"
    if "suggestive" in v:
        return "Suggestive"
    if "mixed" in v:
        return "Mixed"
    if "mostly hype" in v:
        return "Mostly hype"
    if "insufficient" in v:
        return "Insufficient evidence"
    return "Insufficient evidence"


def load() -> list[dict]:
    rows = []
    with CSV.open() as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def figure_1_distribution(rows: list[dict]):
    """Bar chart: count of interventions per primary verdict band."""
    interventions = [r for r in rows if r["kind"] == "intervention"]
    counts = Counter(primary_band(r["verdict"]) for r in interventions)
    bands = BAND_ORDER
    values = [counts.get(b, 0) for b in bands]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(
        bands,
        values,
        color=[BAND_COLORS[b] for b in bands],
        edgecolor="white",
        linewidth=0.6,
    )
    ax.invert_yaxis()
    ax.set_xlabel("Number of interventions (n=49 verdict assignments across 38 pages)")
    ax.set_title(
        "Distribution of verdict bands across the synthesis",
        fontsize=12,
        loc="left",
        pad=10,
    )
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_width() + 0.2,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            fontsize=10,
            color="#1a1a1a",
        )
    ax.set_xlim(0, max(values) + 3)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    fig.savefig(OUT / "figure1-distribution.png", dpi=160, bbox_inches="tight")
    fig.savefig(OUT / "figure1-distribution.svg", bbox_inches="tight")
    print(f"Wrote figure1: {dict(counts)}")


def figure_2_discourse_vs_evidence():
    """Side-by-side comparison: where popular discourse and methodology diverge."""
    rows = [
        # (intervention, popular framing band, methodology band)
        ("Metformin (longevity)", "Probable", "Mixed"),
        ("Time-restricted eating", "Probable", "Mixed"),
        ("Resveratrol", "Probable", "Mostly hype"),
        ("Taurine", "Probable", "Suggestive (↓)"),
        ("Spermidine (cognition)", "Probable", "Suggestive"),
        ("Zone 2 (specific protocol)", "Strong", "Mixed"),
        ("HBOT (anti-aging)", "Probable", "Mixed"),
        ("Acarbose", "Suggestive", "Probable"),
        ("Sauna", "Suggestive", "Probable"),
        ("Resistance training (longevity)", "Suggestive", "Strong"),
    ]
    band_to_x = {
        "Insufficient evidence": 0,
        "Mostly hype": 1,
        "Mixed": 2,
        "Suggestive": 3,
        "Suggestive (↓)": 3,
        "Probable": 4,
        "Strong": 5,
    }
    interventions = [r[0] for r in rows]
    pop_x = [band_to_x[r[1]] for r in rows]
    meth_x = [band_to_x[r[2]] for r in rows]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    y = list(range(len(rows)))
    for yi, p, m, label in zip(y, pop_x, meth_x, interventions):
        color = "#9a2a2a" if m < p else "#1d6638" if m > p else "#5a5a5a"
        ax.annotate(
            "",
            xy=(m, yi),
            xytext=(p, yi),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=2.0, mutation_scale=14),
        )
        ax.scatter([p], [yi], color="#5a5a5a", zorder=5, s=44, marker="o")
        ax.scatter([m], [yi], color=color, zorder=6, s=64, marker="s")

    ax.set_yticks(y)
    ax.set_yticklabels(interventions, fontsize=10)
    ax.invert_yaxis()
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(
        ["Insuff.", "Mostly\nhype", "Mixed", "Suggest.", "Probable", "Strong"],
        fontsize=9,
    )
    ax.set_xlim(-0.5, 5.5)
    ax.grid(axis="x", linestyle=":", color="#cccbc0", alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_title(
        "Where popular discourse diverges from the methodology's verdict",
        fontsize=12,
        loc="left",
        pad=10,
    )
    # Legend
    from matplotlib.lines import Line2D

    legend_elems = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#5a5a5a", markersize=8, label="Popular framing"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor="#1d6638", markersize=9, label="Methodology rates higher"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor="#9a2a2a", markersize=9, label="Methodology rates lower"),
    ]
    ax.legend(handles=legend_elems, loc="lower right", frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "figure2-discourse-vs-evidence.png", dpi=160, bbox_inches="tight")
    fig.savefig(OUT / "figure2-discourse-vs-evidence.svg", bbox_inches="tight")
    print("Wrote figure2")


if __name__ == "__main__":
    rows = load()
    figure_1_distribution(rows)
    figure_2_discourse_vs_evidence()

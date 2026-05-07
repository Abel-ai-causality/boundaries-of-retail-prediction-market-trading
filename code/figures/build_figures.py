"""Regenerate figures 1, 2, 5 for the v0.2 manuscript.

Inputs (relative to repo root):
- data/anc/alternative-routes.jsonl  (for fig 2 outcome counts)
- data/per-campaign-summary.csv      (for fig 2 promoted-forward total)

Outputs (overwrites):
- latex/figures/fig1_four_gates_minimal.{pdf,png}
- latex/figures/fig2_route_ledger_refined.{pdf,png}
- latex/figures/fig5_ceiling_pin_refined.{pdf,png}

Run from the repo root:
    python3 code/figures/build_figures.py
"""

from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# Palette (Tableau-10 muted, hand-picked to match the v0.2 brand)
PALETTE = {
    "gray":   {"edge": "#7A8693", "fill": "#E5E7EB", "text": "#1F2937"},
    "teal":   {"edge": "#0F9C8F", "fill": "#D7F2EE", "text": "#0F766E"},
    "blue":   {"edge": "#2774AE", "fill": "#DBEAFE", "text": "#1D4ED8"},
    "orange": {"edge": "#E68A2E", "fill": "#FEF3C7", "text": "#B45309"},
    "purple": {"edge": "#8B5CF6", "fill": "#EDE9FE", "text": "#6D28D9"},
    "red":    {"edge": "#DC2626", "fill": "#FEE2E2", "text": "#991B1B"},
    "green":  {"edge": "#16A34A", "fill": "#DCFCE7", "text": "#166534"},
}

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "latex" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def _save(fig: plt.Figure, stem: str) -> None:
    """Save both PDF (vector) and PNG (raster preview) at consistent dimensions."""
    fig.savefig(FIG_DIR / f"{stem}.pdf", bbox_inches="tight", pad_inches=0.15)
    fig.savefig(FIG_DIR / f"{stem}.png", bbox_inches="tight", pad_inches=0.15, dpi=180)
    plt.close(fig)


def _rounded_box(ax, xy, width, height, color_key, label, sublabel=None, idx=None):
    """Place a rounded box with bold label + optional sublabel and small index."""
    palette = PALETTE[color_key]
    box = FancyBboxPatch(
        xy, width, height,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        linewidth=2.2, edgecolor=palette["edge"], facecolor=palette["fill"],
    )
    ax.add_patch(box)
    cx, cy = xy[0] + width / 2, xy[1] + height / 2
    if idx is not None:
        ax.text(xy[0] + 0.10, xy[1] + height - 0.18, str(idx),
                fontsize=10, fontweight="bold", color=palette["text"])
    if sublabel:
        ax.text(cx, cy + 0.10, label, ha="center", va="center",
                fontsize=11.5, fontweight="bold", color=palette["text"], wrap=True)
        ax.text(cx, cy - 0.18, sublabel, ha="center", va="center",
                fontsize=9.5, color=palette["text"])
    else:
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=11.5, fontweight="bold", color=palette["text"], wrap=True)


# ---------------------------------------------------------------------------
# Figure 1 — four-gate funnel (5 boxes wide enough that long labels fit)
# ---------------------------------------------------------------------------

def build_fig1() -> None:
    fig, ax = plt.subplots(figsize=(11.0, 2.6))
    ax.set_xlim(0, 17.0)
    ax.set_ylim(0, 4.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # Five boxes; box width 2.6 leaves room for the longest label ("LLM-readable").
    box_w, box_h = 2.6, 2.0
    gap = 0.50
    x0 = 0.20
    y0 = 1.20

    boxes = [
        ("gray",   "LLM-readable\nroute",  None, "0"),
        ("teal",   "Sourceability",        None, "1"),
        ("blue",   "Fillability",          None, "2"),
        ("orange", "Capacity",             None, "3"),
        ("purple", "Anchor\nstability",    None, "4"),
    ]
    centers = []
    for i, (color, label, sub, idx) in enumerate(boxes):
        x = x0 + i * (box_w + gap)
        _rounded_box(ax, (x, y0), box_w, box_h, color, label, sub, idx)
        centers.append((x + box_w / 2, y0 + box_h / 2))

    # Arrows between boxes
    for i in range(len(boxes) - 1):
        x_from = x0 + i * (box_w + gap) + box_w
        x_to = x_from + gap
        y = y0 + box_h / 2
        ax.add_patch(FancyArrowPatch(
            (x_from + 0.04, y), (x_to - 0.04, y),
            arrowstyle="-|>", mutation_scale=14, linewidth=1.6, color="#94A3B8",
        ))

    # Subtitle
    ax.text(8.5, 0.30,
            "Observed boundary: 0 / 11 trading-focused campaigns cleared all four gates",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color="#1F2937")

    _save(fig, "fig1_four_gates_minimal")


# ---------------------------------------------------------------------------
# Figure 2 — route ledger (no in-figure caption that overlaps the axis)
# ---------------------------------------------------------------------------

def _route_outcomes() -> tuple[Counter[str], int]:
    """Return (ultimate_outcome counter, count of promoted_to_next_round=True).

    Both counts come from data/anc/alternative-routes.jsonl so they share
    the same denominator (n=225).  `alternative_routes_count` in
    per-campaign-summary.csv is the per-campaign total of alternative-route
    rows (228) — a different metric, not the "promoted forward" count.
    """
    routes_path = REPO_ROOT / "data" / "anc" / "alternative-routes.jsonl"
    outcomes: Counter[str] = Counter()
    promoted = 0
    with routes_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            outcomes[obj.get("ultimate_outcome", "?")] += 1
            if obj.get("promoted_to_next_round") is True:
                promoted += 1
    return outcomes, promoted


def build_fig2() -> None:
    outcomes, promoted = _route_outcomes()

    fig, ax = plt.subplots(figsize=(10.5, 3.8))

    # Single panel, 4 horizontal bars.  Layout (top -> bottom):
    #   Promoted forward (orthogonal axis, separated by a row gap)
    #   --- gap ---
    #   Rejected / Selected / Deferred  (recovered-ledger outcomes)
    rows_top = [("Promoted forward", promoted, "orange")]
    rows_bot = [
        ("Rejected", outcomes.get("rejected", 0), "red"),
        ("Selected", outcomes.get("selected", 0), "teal"),
        ("Deferred", outcomes.get("deferred", 0), "gray"),
    ]
    rows_all = rows_top + rows_bot
    labels = [r[0] for r in rows_all]
    values = [r[1] for r in rows_all]
    colors = [PALETTE[r[2]]["edge"] for r in rows_all]

    # y positions (top = highest y).  Big gap (0.9) between promoted and outcomes rows.
    y_pos = [4.0, 2.6, 1.8, 1.0]  # promoted at top, then 3 outcomes
    bars = ax.barh(y_pos, values, color=colors, edgecolor="white", linewidth=1.0, height=0.65)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11)
    ax.set_xlim(0, 175)
    ax.set_ylim(0.4, 4.7)
    ax.set_xlabel("routes", fontsize=11)
    ax.set_title("Alternative-route ledger", fontsize=13.5, fontweight="bold", pad=10)

    for bar, v in zip(bars, values):
        ax.text(v + 5, bar.get_y() + bar.get_height() / 2, str(v),
                va="center", fontsize=11, fontweight="bold", color="#1F2937")

    # Italic annotation next to the top (orthogonal-axis) bar — placed AFTER
    # the "79" data label so they don't overlap.
    ax.text(values[0] + 18, y_pos[0],
            "orthogonal axis: routes promoted into\n"
            "the next round's candidate pool",
            fontsize=9.5, color=PALETTE["orange"]["text"], style="italic", va="center")

    # Bracket + label on the left for the 3-outcome group
    bracket_y_top, bracket_y_bot = y_pos[1] + 0.40, y_pos[3] - 0.40
    bracket = ax.plot([-18, -18], [bracket_y_bot, bracket_y_top],
                      color="#94A3B8", linewidth=1.4)
    for line in bracket:
        line.set_clip_on(False)
    txt = ax.text(-26, (bracket_y_top + bracket_y_bot) / 2,
                  "recovered-\nledger\noutcomes\n(n = 225)",
                  ha="right", va="center", fontsize=9.5, color="#475569")
    txt.set_clip_on(False)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="-", linewidth=0.5, color="#E5E7EB")
    ax.set_axisbelow(True)

    _save(fig, "fig2_route_ledger_refined")


# ---------------------------------------------------------------------------
# Figure 5 — ceiling-pin layer migration (depicts the *migration*, not just 3 boxes)
# ---------------------------------------------------------------------------

def build_fig5() -> None:
    fig, ax = plt.subplots(figsize=(11.0, 4.6))
    ax.set_xlim(0, 16.0)
    ax.set_ylim(0, 7.0)
    ax.set_aspect("equal")
    ax.axis("off")

    box_w, box_h = 3.4, 1.6

    # State A — before tightening: defect lives at L1 (rubric)
    ax.text(0.10, 6.40, "Before tightening", fontsize=11, fontweight="bold", color="#1F2937")
    _rounded_box(ax, (0.20, 4.80), box_w, box_h, "red",  "Rubric layer",      "field-count score",  "L1")
    _rounded_box(ax, (4.30, 4.80), box_w, box_h, "gray", "Prompt / output",   "plausible text",     "L2")
    _rounded_box(ax, (8.40, 4.80), box_w, box_h, "gray", "External verifier", "source object",      "L3")
    ax.text(2.00, 4.55, "defect lives here", ha="center", fontsize=9.5,
            color=PALETTE["red"]["text"], style="italic")
    ax.add_patch(FancyArrowPatch((3.65, 5.60), (4.35, 5.60),
                                 arrowstyle="-|>", mutation_scale=12, linewidth=1.4, color="#94A3B8"))
    ax.add_patch(FancyArrowPatch((7.75, 5.60), (8.45, 5.60),
                                 arrowstyle="-|>", mutation_scale=12, linewidth=1.4, color="#94A3B8"))

    # Migration arrow — curved, from L1-after to L2-after
    ax.annotate(
        "tighten rubric ⇒ defect migrates",
        xy=(5.20, 2.95), xytext=(2.70, 3.95),
        fontsize=10, fontweight="bold", color=PALETTE["red"]["text"], ha="center",
        arrowprops=dict(arrowstyle="-|>", color=PALETTE["red"]["edge"],
                        connectionstyle="arc3,rad=-0.35", linewidth=1.8),
    )

    # State B — after tightening: defect migrated to L2 (prompt/output); only L3 is stable
    ax.text(0.10, 2.30, "After tightening", fontsize=11, fontweight="bold", color="#1F2937")
    _rounded_box(ax, (0.20, 0.70), box_w, box_h, "gray",  "Rubric layer",      "stricter score",     "L1")
    _rounded_box(ax, (4.30, 0.70), box_w, box_h, "red",   "Prompt / output",   "answer-shape passes","L2")
    _rounded_box(ax, (8.40, 0.70), box_w, box_h, "green", "External verifier", "checks source span", "L3")
    ax.text(6.00, 0.45, "defect migrated here", ha="center", fontsize=9.5,
            color=PALETTE["red"]["text"], style="italic")
    ax.text(10.10, 0.45, "stable repair", ha="center", fontsize=9.5,
            color=PALETTE["green"]["text"], style="italic", fontweight="bold")
    ax.add_patch(FancyArrowPatch((3.65, 1.50), (4.35, 1.50),
                                 arrowstyle="-|>", mutation_scale=12, linewidth=1.4, color="#94A3B8"))
    ax.add_patch(FancyArrowPatch((7.75, 1.50), (8.45, 1.50),
                                 arrowstyle="-|>", mutation_scale=12, linewidth=1.4, color="#94A3B8"))

    # Side panel: gate rule (right of state A)
    ax.text(13.20, 5.60, "Gate rule",
            ha="center", fontsize=11.5, fontweight="bold", color="#1F2937")
    ax.text(13.20, 4.90,
            "Score the external\nobject, not the\nmodel output.",
            ha="center", va="center", fontsize=10.5, color="#1F2937")
    ax.text(13.20, 1.50,
            "Tightening L1 ⇒\ndefect moves to L2.\nOnly L3 kills it.",
            ha="center", va="center", fontsize=10.5, color="#1F2937")

    _save(fig, "fig5_ceiling_pin_refined")


def main() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })
    build_fig1()
    build_fig2()
    build_fig5()
    print("regenerated:", sorted(p.name for p in FIG_DIR.glob("fig[125]_*.pdf")))


if __name__ == "__main__":
    main()

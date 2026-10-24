"""Plotting utilities for Distributions in Practice."""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Consistent color palette used across all notebooks
PALETTE = {
    "primary": "#2b5c8f",
    "secondary": "#d95f02",
    "accent": "#7570b3",
    "fill": "#a6cee3",
    "grid": "#e0e0e0",
}


def set_style():
    """Apply a clean, publication-ready style to all matplotlib figures."""
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams.update(
        {
            "figure.figsize": (8, 4.5),
            "figure.dpi": 150,
            "axes.titlesize": 13,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "grid.color": PALETTE["grid"],
            "grid.alpha": 0.6,
        }
    )


def plot_pmf(x, pmf, title="Probability Mass Function", xlabel="k", ylabel="P(X = k)", ax=None):
    """Plot a discrete Probability Mass Function (PMF) as a stem/lollipop plot."""
    if ax is None:
        fig, ax = plt.subplots()

    markerline, stemlines, baseline = ax.stem(x, pmf, basefmt=" ")
    plt.setp(markerline, color=PALETTE["primary"], markersize=6)
    plt.setp(stemlines, color=PALETTE["primary"], linewidth=1.8)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(bottom=0)
    return ax


def plot_pdf(x, pdf, title="Probability Density Function", xlabel="x", ylabel="f(x)", fill=True, ax=None):
    """Plot a continuous Probability Density Function (PDF) with optional shading."""
    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(x, pdf, color=PALETTE["primary"], linewidth=2.2, label="PDF")
    if fill:
        ax.fill_between(x, pdf, alpha=0.35, color=PALETTE["fill"])

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(bottom=0)
    return ax


def plot_cdf(x, cdf, is_discrete=False, title="Cumulative Distribution Function", xlabel="x", ylabel="F(x) = P(X ≤ x)", ax=None):
    """Plot a Cumulative Distribution Function (CDF) as a step function or smooth curve."""
    if ax is None:
        fig, ax = plt.subplots()

    if is_discrete:
        ax.step(x, cdf, where="post", color=PALETTE["secondary"], linewidth=2.0, label="CDF")
    else:
        ax.plot(x, cdf, color=PALETTE["secondary"], linewidth=2.0, label="CDF")

    ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.9, alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(-0.02, 1.05)
    return ax


def plot_sample_vs_theory(samples, x_theory, y_theory, is_discrete=False, title="Simulation vs Theoretical Distribution", xlabel="Value", ax=None):
    """Overlay empirical sample data against the theoretical distribution."""
    if ax is None:
        fig, ax = plt.subplots()

    if is_discrete:
        bins = np.arange(min(samples) - 0.5, max(samples) + 1.5, 1)
        ax.hist(samples, bins=bins, density=True, alpha=0.5, color=PALETTE["fill"], edgecolor="black", label="Empirical (Simulated)")
        markerline, stemlines, _ = ax.stem(x_theory, y_theory, basefmt=" ", label="Theoretical PMF")
        plt.setp(markerline, color=PALETTE["primary"], markersize=5)
        plt.setp(stemlines, color=PALETTE["primary"], linewidth=1.5)
    else:
        ax.hist(samples, bins=40, density=True, alpha=0.5, color=PALETTE["fill"], edgecolor="white", label="Empirical (Simulated)")
        ax.plot(x_theory, y_theory, color=PALETTE["primary"], linewidth=2.2, label="Theoretical PDF")

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Density / Relative Frequency")
    ax.legend(frameon=True)
    return ax


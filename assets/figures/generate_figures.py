#!/usr/bin/env python3
"""Generate the physics figures embedded in the module notes.

Run from the repo root:  python3 assets/figures/generate_figures.py
Produces self-contained SVGs (white card background so they read in both the
light and dark site themes). Each figure is intentionally schematic — axes are
in natural/dimensionless units to illustrate the shape of the result.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.size": 12, "axes.linewidth": 1.0, "svg.fonttype": "none"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), format="svg", bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close(fig)
    print("wrote", name)


def minkowski_light_cone():
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    x = np.linspace(-2, 2, 2)
    ax.fill_between([-2, 0, 2], [2, 0, 2], 2, color="#cfe3ff", zorder=0)      # future
    ax.fill_between([-2, 0, 2], [-2, 0, -2], -2, color="#cfe3ff", zorder=0)   # past
    ax.plot([-2, 2], [-2, 2], color="#d8861f", lw=2)
    ax.plot([-2, 2], [2, -2], color="#d8861f", lw=2)
    ax.annotate("future\n($s^2>0$)", (0, 1.3), ha="center", color="#1f4e9c")
    ax.annotate("past", (0, -1.45), ha="center", color="#1f4e9c")
    ax.annotate("elsewhere\n($s^2<0$)", (1.45, 0), ha="center", va="center", color="#555")
    ax.annotate("elsewhere", (-1.45, 0), ha="center", va="center", color="#555")
    ax.annotate("light cone\n$ct=\\pm x$", (-1.25, 1.35), ha="center", color="#a8650f", fontsize=9.5)
    # a timelike worldline
    t = np.linspace(-1.8, 1.8, 100)
    ax.plot(0.5 * np.tanh(t), t, color="#c0392b", lw=2, ls="--")
    ax.annotate("worldline", (0.62, 1.2), color="#c0392b", fontsize=10)
    ax.axhline(0, color="#888", lw=0.8); ax.axvline(0, color="#888", lw=0.8)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_xlabel("$x$"); ax.set_ylabel("$ct$")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    ax.set_title("Minkowski spacetime: the light cone")
    save(fig, "minkowski-light-cone.svg")


def phonon_dispersion():
    a = 1.0
    k = np.linspace(-np.pi / a, np.pi / a, 400)
    w = 2 * np.abs(np.sin(k * a / 2))  # in units of sqrt(K/M)
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.plot(k, w, color="#1f6fb4", lw=2.2)
    ax.plot(k, np.abs(k), color="#888", lw=1.2, ls=":")
    ax.annotate("linear (sound)\n$\\omega\\approx v_s|k|$", (0.35, 1.35), color="#555", fontsize=10)
    ax.annotate("zone boundary\n$\\omega_{\\max}=2\\sqrt{K/M}$", (np.pi - 0.05, 2.02),
                ha="right", color="#1f6fb4", fontsize=10)
    ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels(["$-\\pi/a$", "0", "$\\pi/a$"])
    ax.set_xlabel("wavevector $k$"); ax.set_ylabel("$\\omega(k)\\;/\\;\\sqrt{K/M}$")
    ax.set_ylim(0, 2.3); ax.set_title("Phonon dispersion of the 1D monatomic chain")
    ax.grid(alpha=0.25)
    save(fig, "phonon-dispersion.svg")


def tight_binding_band():
    a = 1.0
    k = np.linspace(-np.pi / a, np.pi / a, 400)
    E = -2 * np.cos(k * a)  # E0=0, t=1, in units of t
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.plot(k, E, color="#7a3fa0", lw=2.2)
    ax.axhspan(-2, 2, color="#efe7f6", zorder=0)
    ax.annotate("bandwidth $W=4t$", (0, 0), ha="center", va="center", color="#7a3fa0", fontsize=11)
    ax.annotate("$E(k)=E_0-2t\\cos(ka)$", (0, 1.55), ha="center", color="#555", fontsize=11)
    ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels(["$-\\pi/a$", "0", "$\\pi/a$"])
    ax.set_yticks([-2, 0, 2]); ax.set_yticklabels(["$E_0-2t$", "$E_0$", "$E_0+2t$"])
    ax.set_xlabel("wavevector $k$"); ax.set_ylabel("energy $E(k)$")
    ax.set_ylim(-2.6, 2.6); ax.set_title("Tight-binding band (1D)")
    ax.grid(alpha=0.25)
    save(fig, "tight-binding-band.svg")


def landau_free_energy():
    eta = np.linspace(-1.3, 1.3, 400)
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    for a, c, lab in [(1.0, "#1f6fb4", "$T>T_c$ ($a>0$)"),
                      (0.0, "#888888", "$T=T_c$ ($a=0$)"),
                      (-1.0, "#c0392b", "$T<T_c$ ($a<0$)")]:
        F = a * eta**2 + 0.6 * eta**4
        ax.plot(eta, F, color=c, lw=2.2, label=lab)
    # mark the broken-symmetry minima for T<Tc:  eta^2 = -a/(2b) = 1/1.2
    em = np.sqrt(1 / 1.2)
    Fm = -1 * em**2 + 0.6 * em**4
    ax.plot([-em, em], [Fm, Fm], "o", color="#c0392b")
    ax.annotate("$\\pm\\eta_0\\propto(T_c-T)^{1/2}$", (0, Fm - 0.12), ha="center", color="#c0392b", fontsize=10, va="center")
    ax.axhline(0, color="#888", lw=0.8); ax.axvline(0, color="#888", lw=0.8)
    ax.set_xlabel("order parameter $\\eta$"); ax.set_ylabel("free energy $F(\\eta)-F_0$")
    ax.set_title("Landau free energy: $F=a(T)\\,\\eta^2+b\\,\\eta^4$")
    ax.legend(fontsize=10, loc="upper center"); ax.set_xticks([]); ax.set_yticks([])
    save(fig, "landau-free-energy.svg")


if __name__ == "__main__":
    minkowski_light_cone()
    phonon_dispersion()
    tight_binding_band()
    landau_free_energy()
    print("done")

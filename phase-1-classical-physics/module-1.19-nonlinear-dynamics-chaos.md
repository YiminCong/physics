# Module 1.19 — Nonlinear Dynamics & Chaos

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Phase Space, Fixed Points & Bifurcations

**Definition.** A dynamical system is a set of first-order equations ẋ = F(x) on a **phase space** (the q–p plane of Module 1.4 is the canonical example). **Fixed points** F(x*) = 0 are equilibria; linearizing about them classifies their stability (stable/unstable nodes, saddles, spirals, centres) from the eigenvalues of the Jacobian (Module 0.2). A **bifurcation** is a qualitative change in this structure as a control parameter is varied.

**Demonstration.** The damped pendulum θ̈ + γθ̇ + ω₀² sin θ = 0 has a stable fixed point at the bottom and an unstable saddle at the top; in phase space, trajectories spiral into the stable point. As driving is increased, period-doubling bifurcations cascade — the route to chaos.

**Application.** Nonlinearity is the rule, not the exception: most real systems (pendulums at large amplitude, populations, circuits, lasers) are nonlinear, and the linear oscillators of Module 1.6 are only the small-amplitude limit.

## 2. Chaos & Sensitive Dependence

**Definition.** **Deterministic chaos** is bounded, aperiodic motion in a deterministic system showing **sensitive dependence on initial conditions**: nearby trajectories diverge exponentially, ‖δx(t)‖ ~ ‖δx(0)‖ e^{λt}, with **λ the (positive) Lyapunov exponent**. Dissipative chaotic systems settle onto **strange attractors** of fractal dimension.

**Demonstration.** The **logistic map** xₙ₊₁ = r xₙ(1 − xₙ) — a one-line iteration — period-doubles into chaos as r increases, with the universal **Feigenbaum constant** δ ≈ 4.669 governing the cascade. The **Lorenz system**, a 3-variable truncation of convection, produces the iconic butterfly attractor and coined the "butterfly effect."

**Application.** Chaos sets a horizon on predictability — most famously in **weather** (the high-Reynolds turbulence of Module 1.17 is spatiotemporal chaos). The *universality* of the period-doubling route — different systems share the same Feigenbaum constant — foreshadows the universality of critical phenomena and the renormalization group (Module 6.6).

---

**Self-test (blank page)**

1. Sketch the phase portrait of a damped pendulum and classify its two fixed points.
2. Define the Lyapunov exponent and explain what its sign tells you about long-term predictability.
3. Iterate the logistic map at r = 3.2 and at r = 4 (a few steps each) and describe qualitatively what differs.
4. What does it mean that the period-doubling route to chaos is "universal," and what later concept does this anticipate?

---

← Previous: [Module 1.18 — Continuum Mechanics & Elasticity](./module-1.18-continuum-mechanics-elasticity.md) · [Phase 1 index](./README.md)

# Module 2.3 — Free Energy & Phase Transitions ⭐

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. First- and Second-Order Transitions

**Definition.** A system at fixed T and P minimizes its Gibbs free energy G (Module 2.2). A **phase transition** occurs when competing phases become degenerate in G, and the equilibrium state changes discontinuously or continuously in some property. Transitions are classified by behavior at the transition temperature T_c:

- **First-order**: G is continuous but its first derivatives (S = −(∂G/∂T)_P and V = (∂G/∂P)_T) are discontinuous. A latent heat L = T_c ΔS is released, and the two phases coexist. Examples: melting, boiling.
- **Second-order (continuous)**: G and its first derivatives are continuous, but second derivatives (heat capacity C, compressibility κ, susceptibility χ) diverge. No latent heat; no phase coexistence. Examples: the ferromagnetic Curie point, the superfluid transition, the superconducting transition.

**Demonstration.** Near a first-order transition, plotting G(T) for each phase shows two branches that cross at T_c; the equilibrium state jumps between branches, causing the discontinuity in entropy (hence latent heat). At a second-order transition, the branches merge tangentially, so S is continuous but C = T(∂S/∂T)_P diverges — this shows up as a cusp or lambda anomaly in heat capacity measurements.

**Application.** The classification determines experimental signatures: calorimetry detects latent heat for first-order transitions; diverging susceptibility and power-law scaling of thermodynamic quantities near T_c signal second-order transitions, and their critical exponents are the central objects of renormalization-group theory (Module 6.6).

---

## 2. Landau Theory and the Order Parameter

**Definition.** Landau theory provides a unified framework for second-order (and weakly first-order) transitions by expanding the free energy as a power series in an **order parameter** η, a field that is zero in the disordered phase and non-zero in the ordered phase (e.g., magnetization M for a ferromagnet, superfluid density ψ for a superfluid). Symmetry constrains which powers appear. For a system with η → −η symmetry (even powers only):

F(T, η) = F₀ + a(T) η² + b η⁴ + …

with b > 0 for stability and a(T) = a₀(T − T_c) changing sign at T_c (a₀ > 0). Minimizing ∂F/∂η = 0 gives:

- T > T_c: a > 0, unique minimum at η = 0 (disordered phase).
- T < T_c: a < 0, double-well with minima at η = ±√(−a/2b) ∝ (T_c − T)^{1/2}.

**Demonstration.** The mean-field critical exponent for the order parameter is β = 1/2 from η ∝ (T_c − T)^{1/2}. The heat capacity has a discontinuity ΔC = a₀²/(2b) at T_c with no latent heat, confirming the second-order character. Including a symmetry-breaking external field h adds a term −hη, giving a susceptibility χ = (∂η/∂h)_{h→0} ∝ |T − T_c|^{−1} (exponent γ = 1 in mean field).

If b < 0 (with a stabilizing c η⁶ term), the potential develops a secondary minimum before a = 0 is reached, and the transition becomes first-order — the order parameter jumps discontinuously at T_c. This explains how Landau theory captures both orders of transition in a single framework.

**Application.** Landau theory is a template that recurs throughout condensed-matter and particle physics:

- **Ginzburg–Landau theory** (Module 5.3) identifies η with the complex superconducting order parameter ψ and adds gradient and electromagnetic coupling terms — giving the full phenomenology of type-I and type-II superconductors.
- The **Higgs mechanism** (Module 8.4) is the relativistic field-theory version of the same double-well potential: the Mexican-hat potential for a complex scalar field, with the Goldstone direction becoming the longitudinal gauge boson.
- **Renormalization group** (Module 6.6) explains why mean-field exponents (β = 1/2, γ = 1) are wrong near T_c in low dimensions: fluctuations in η, ignored by the saddle-point minimization, become dominant and shift the exponents to universal, dimension-dependent values.

---

## Self-test (blank page)

1. Sketch F(η) for the Landau free energy F = a(T)η² + bη⁴ at T > T_c, T = T_c, and T < T_c. Mark the equilibrium η in each case.
2. Show that minimizing F = a₀(T − T_c)η² + bη⁴ gives η ∝ (T_c − T)^{1/2} below T_c. What is the mean-field exponent β?
3. Explain in one sentence the physical difference between a first-order and a second-order phase transition. Which has a latent heat?
4. Name two later modules where the Landau free-energy expansion reappears, and identify the order parameter in each case.

---

← Previous: [Module 2.2 — Thermodynamic Potentials & Maxwell Relations](./module-2.2-thermodynamic-potentials.md) · [Phase 2 index](./README.md) · Next: [Module 2.4 — Classical Statistical Mechanics](./module-2.4-classical-statistical-mechanics.md) →

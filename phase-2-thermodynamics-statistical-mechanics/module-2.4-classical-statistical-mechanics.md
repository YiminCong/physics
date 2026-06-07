# Module 2.4 — Classical Statistical Mechanics

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Microstates, Ensembles, and the Boltzmann Factor

**Definition.** A **microstate** is a complete specification of a system (positions and momenta of all particles); a **macrostate** is a coarse description by a few thermodynamic variables (U, T, V, N). Statistical mechanics connects these levels via the **fundamental postulate**: in an isolated system at equilibrium, all accessible microstates are equally probable. The number of microstates consistent with a macrostate is Ω, and Boltzmann's entropy is

S = k_B ln Ω.

Three standard **ensembles** cover different physical situations:

- **Microcanonical** (fixed E, V, N): isolated system; Ω counts states at energy E.
- **Canonical** (fixed T, V, N): system in thermal contact with a reservoir at temperature T. The probability of a microstate with energy E_i is the Boltzmann weight p_i = e^{−E_i/k_BT} / Z.
- **Grand canonical** (fixed T, V, μ): system can exchange both energy and particles with a reservoir; particle number N fluctuates. The probability of a state with energy E_i and particle number N_i is p_i ∝ e^{−(E_i − μ N_i)/k_BT}.

**Demonstration.** In the canonical ensemble, the normalization condition Σ p_i = 1 defines the **partition function**

Z = Σ_i e^{−E_i/k_BT},

where the sum runs over all microstates. All thermodynamic quantities follow from Z:

- F = −k_B T ln Z     (Helmholtz free energy; the bridge formula)
- U = −∂(ln Z)/∂β,   β = 1/k_BT
- S = −(∂F/∂T)_V = k_B (ln Z + β U)
- P = −(∂F/∂V)_T

**Application.** The **equipartition theorem** follows immediately: for any degree of freedom whose energy is quadratic (½ k q²), the average energy is ½ k_B T. A monatomic ideal gas has 3 translational degrees of freedom, giving U = (3/2) N k_B T and C_V = (3/2) N k_B, matching experiment at high temperature. Failures of equipartition at low T (frozen-out vibrational modes, electronic heat capacity) are the first sign that quantum statistics is needed — taken up in Module 2.5.

---

## 2. The Partition Function as a Generating Function

**Definition.** For a system of N independent, distinguishable particles each with single-particle partition function z = Σ_α e^{−ε_α/k_BT}, the total partition function factorizes: Z = z^N. For **indistinguishable** classical particles, overcounting by N! must be corrected: Z = z^N / N!, which is the Gibbs correction. This prefactor is essential for the entropy to be extensive (the Gibbs paradox without it is that mixing identical gases appears to increase entropy).

**Demonstration.** For the monatomic ideal gas in a box of volume V, the single-particle partition function is z = V (2π m k_B T / h²)^{3/2} (the thermal de Broglie volume). Using Z = z^N / N! and the Stirling approximation, the Sackur–Tetrode equation for entropy follows:

S = N k_B [ ln(V/N) + (3/2) ln(k_B T) + const ],

which is correctly extensive and has a well-defined T → 0 limit connecting to the Third Law.

**Application.** The partition function encodes everything: it gives the equation of state PV = N k_B T for the ideal gas, heat capacities, fluctuations (⟨E²⟩ − ⟨E⟩² = k_B T² C_V), and — through the grand canonical extension — chemical equilibrium constants. In quantum statistical mechanics (Module 2.5), the same logic applies but the sum over states respects Fermi–Dirac or Bose–Einstein statistics, fundamentally altering which microstates are accessible.

---

## Self-test (blank page)

1. State the fundamental postulate of statistical mechanics. How does it lead to S = k_B ln Ω?
2. Derive the average energy U = −∂(ln Z)/∂β from the definition Z = Σ e^{−β E_i} and the expression ⟨E⟩ = Σ p_i E_i.
3. Apply the equipartition theorem to a diatomic gas with 3 translational + 2 rotational + 2 vibrational (kinetic + potential) degrees of freedom. What is C_V per molecule?
4. Why must Z be divided by N! for identical classical particles? What paradox does this resolve?

---

← Previous: [Module 2.3 — Free Energy & Phase Transitions](./module-2.3-free-energy-phase-transitions.md) · [Phase 2 index](./README.md) · Next: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) →

# Module 2.5 — Quantum Statistics ⭐

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Indistinguishability and the Two Distributions

**Definition.** Quantum mechanics forces a radical revision of how microstates are counted. Identical particles are truly indistinguishable: swapping two particles cannot produce a new state (Module 3.5). The symmetry of the many-body wavefunction under particle exchange splits all particles into two classes:

- **Fermions** (half-integer spin): wavefunction is antisymmetric. No two fermions can occupy the same single-particle state — the **Pauli exclusion principle**. The mean occupation number of a state with energy ε is the **Fermi–Dirac distribution**:

  n_FD(ε) = 1 / (e^{(ε − μ)/k_BT} + 1)

- **Bosons** (integer spin): wavefunction is symmetric. Any number of bosons can occupy the same state. The mean occupation number is the **Bose–Einstein distribution**:

  n_BE(ε) = 1 / (e^{(ε − μ)/k_BT} − 1)

In both cases, μ is the **chemical potential**, determined by the condition that Σ n(ε) = N (total particle number). At high temperature or low density (e^{(ε − μ)/k_BT} ≫ 1 for all occupied states), both distributions reduce to the classical Maxwell–Boltzmann result n ∝ e^{−ε/k_BT}.

**Demonstration.** These distributions are derived in the grand canonical ensemble (Module 2.4). For fermions, each single-particle state α is an independent sub-system that can hold 0 or 1 particle; its grand canonical partition function is

z_α = 1 + e^{−(ε_α − μ)/k_BT},

and the mean occupation is ⟨n_α⟩ = −∂(k_BT ln z_α)/∂ε_α = n_FD(ε_α). For bosons the state can hold 0, 1, 2, … particles; the geometric series gives z_α = 1/(1 − e^{−(ε_α − μ)/k_BT}) and ⟨n_α⟩ = n_BE(ε_α). The denominator sign difference — plus for fermions, minus for bosons — encodes the entire distinction between the two statistics.

**Application.** The Fermi–Dirac distribution at T = 0 is a step function: all states up to the **Fermi energy** E_F are fully occupied, all above are empty. E_F is set by filling N states in order of increasing energy:

E_F = (ℏ²/2m)(3π² n)^{2/3}     (free electron gas in 3D, n = N/V).

This defines the Fermi surface in momentum space — the central object of electronic structure, conductivity, and superconductivity (Phases 4–5). For bosons, μ must remain below the ground-state energy; when μ → 0 as T is lowered, macroscopic occupation of the ground state (Bose–Einstein condensation) occurs — see Module 2.6.

---

## 2. Chemical Potential and the Pauli Principle in Practice

**Definition.** The chemical potential μ is the free-energy cost of adding one particle at fixed T and V: μ = (∂F/∂N)_{T,V}. At T = 0 for fermions, μ = E_F exactly. At finite T, μ shifts slightly below E_F (for a metal, the shift is of order (k_BT)²/E_F — tiny at room temperature since k_BT ≈ 0.025 eV while E_F ≈ 5–10 eV). For bosons in three dimensions, μ < ε_0 (ground-state energy) at all T above the condensation temperature T_BEC.

**Demonstration.** The Sommerfeld expansion expresses any Fermi–Dirac integral as a low-temperature series. For the average energy of a 3D free Fermi gas:

U(T) ≈ U(0) + (π²/6)(k_BT)² g(E_F) + …

where g(E_F) is the density of states at the Fermi level. Differentiating gives the electronic heat capacity

C_el = (π²/3) k_B² T g(E_F) ∝ T,

which is far smaller than the classical equipartition value (3/2)N k_B because only the fraction ∼ k_BT/E_F of electrons near the Fermi surface are thermally active. This T-linear heat capacity is a direct signature of Fermi statistics, measured in metals and discussed further in Module 4.1.

**Application.** Quantum statistics permeates condensed matter and beyond:

- **Electron gas** in metals: Fermi–Dirac statistics explains the small electronic heat capacity, electrical conductivity, and the existence of a Fermi surface (Module 4.5).
- **Phonons and photons**: both are bosons (integer spin). Their chemical potential is zero (they are not conserved), so n_BE(ε) = 1/(e^{ε/k_BT} − 1) directly gives the Planck distribution for photons and the Bose occupation of phonon modes — governing black-body radiation and lattice heat capacity (Module 2.6, Module 4.3).
- **Superconductivity**: Cooper pairs are composite bosons; their condensation is enabled by Fermi-surface instabilities described by BCS theory (Phase 5).

---

## Self-test (blank page)

1. Write down both quantum distribution functions and state which applies to electrons, photons, and helium-4 atoms. What is the classical limit?
2. Explain in one sentence why the electronic heat capacity C_el ∝ T rather than the classical value (3/2)N k_B. Which electrons contribute?
3. For a free Fermi gas at T = 0, derive the Fermi energy E_F in terms of the number density n, using the condition that all states below E_F are filled.
4. Why must the chemical potential for bosons satisfy μ < ε_0 (the ground-state energy)? What happens when μ → ε_0?

---

← Previous: [Module 2.4 — Classical Statistical Mechanics](./module-2.4-classical-statistical-mechanics.md) · [Phase 2 index](./README.md) · Next: [Module 2.6 — Quantum Gases & Applications](./module-2.6-quantum-gases-applications.md) →

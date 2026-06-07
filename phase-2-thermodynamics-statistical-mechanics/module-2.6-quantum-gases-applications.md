# Module 2.6 — Quantum Gases & Applications

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Degenerate Fermi Gas and Black-Body Radiation

**Definition.** A **quantum gas** is one where quantum statistics — not classical phase-space counting — determines the thermodynamic properties. Two limiting cases dominate applications:

**Degenerate Fermi gas** (T ≪ T_F = E_F/k_B): electrons in a metal at room temperature satisfy k_BT ≪ E_F, so the Fermi–Dirac distribution is nearly a step function. The density of states in 3D is g(ε) ∝ ε^{1/2}, so the total energy and heat capacity follow from the Sommerfeld expansion (Module 2.5):

C_el = (π²/2) N k_B (k_BT/E_F) ∝ T.

This linear-T electronic heat capacity is far below the classical equipartition value, explaining why the electron gas does not swamp the lattice contribution at low temperatures.

**Black-body radiation** (photon gas): photons are massless spin-1 bosons with μ = 0 (photon number is not conserved). The mean occupation of a mode at frequency ν is the **Planck distribution**:

n(ν) = 1 / (e^{hν/k_BT} − 1).

Summing over all modes in a cavity gives the spectral energy density

u(ν, T) = (8πh/c³) ν³ / (e^{hν/k_BT} − 1),

and integrating over ν gives the Stefan–Boltzmann law: total radiated power ∝ T⁴. The Rayleigh–Jeans law (classical equipartition) predicts u ∝ ν²T with no cut-off — the ultraviolet catastrophe — which Planck's quantized modes resolve.

**Demonstration.** The electronic heat capacity is extracted from total measured C(T) = γT + AT³ at low temperature: the linear term isolates C_el = γT with γ = (π²/3) k_B² g(E_F), directly measuring the density of states at the Fermi level. For copper, E_F ≈ 7 eV gives T_F ≈ 81 000 K, so at 300 K the ratio k_BT/E_F ≈ 0.004 — confirming deep degeneracy and explaining why only ∼ 0.4% of electrons are thermally active.

**Application.** The T-linear electronic heat capacity (Module 4.1) and the Fermi surface structure (Module 4.5) are the direct experimental fingerprints of Fermi statistics. The Planck distribution underpins astrophysics (cosmic microwave background), photovoltaics, and the calibration of all thermal radiation detectors.

---

## 2. Bose–Einstein Condensation and Lattice Heat Capacity

**Definition.** For a gas of N non-interacting bosons in 3D with a fixed number (e.g., ⁸⁷Rb atoms), the chemical potential μ increases toward the ground-state energy ε_0 as T decreases. At the **condensation temperature**

T_BEC = (2πℏ²/mk_B) (n / ζ(3/2))^{2/3},

where ζ(3/2) ≈ 2.612, the normal states are saturated — they can hold no more bosons — and any additional particles macroscopically occupy the single ground state. Below T_BEC, the condensate fraction is

N_0/N = 1 − (T/T_BEC)³.

The **Debye model** treats lattice vibrations (phonons) as a gas of bosons with μ = 0 (like photons, phonons are not conserved). The key modification over the Einstein model is a realistic linear dispersion ω ∝ k up to a cut-off frequency ω_D set by the condition that the total mode count equals 3N (three degrees of freedom per atom). The resulting heat capacity at low T is the **Debye T³ law**:

C_Debye ≈ (12π⁴/5) N k_B (T/T_D)³     (T ≪ T_D),

where T_D = ℏω_D/k_B is the Debye temperature (∼ 100–1000 K for typical solids).

**Demonstration.** At very low temperatures, the total heat capacity of a metal is

C(T) = γT + βT³,

where the first term is electronic (Fermi gas) and the second is phononic (Debye). Plotting C/T vs T² gives a straight line with intercept γ and slope β — a standard cryogenic measurement that independently determines both the Fermi-level density of states and the Debye temperature. The Debye T³ law arises because low-energy phonons obey Bose–Einstein statistics and their number scales as T³, dominating at T ≪ T_D.

**Application.** These results directly feed into Module 4.1 (heat capacity of solids): the Debye model supersedes the classical Dulong–Petit value C = 3Nk_B (correct only at high T where every mode is classically active) and explains the observed fall-off at low temperatures. Module 4.3 (phonons) extends this to the full phonon dispersion and phonon–phonon interactions. Bose–Einstein condensation, first achieved with dilute alkali gases in 1995, has become a laboratory for quantum many-body physics, superfluidity, and precision measurement.

---

## Self-test (blank page)

1. Sketch the Planck distribution u(ν, T) and identify where the Rayleigh–Jeans and Wien limits apply. What quantity does integrating u over ν give?
2. Explain why the electronic heat capacity of a metal is ∝ T rather than constant, and estimate the ratio C_el / C_classical for copper at 300 K (use E_F ≈ 7 eV).
3. State the condition for Bose–Einstein condensation and explain physically why macroscopic ground-state occupation occurs below T_BEC.
4. How does the Debye model improve on the Einstein model for lattice heat capacity? What is the low-T prediction, and which experimental measurement confirms it?

---

← Previous: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) · [Phase 2 index](./README.md) · Next: [Module 2.7 — Kinetic Theory & Transport](./module-2.7-kinetic-theory-and-transport.md) →

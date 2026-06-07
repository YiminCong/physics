# Module 6.2 — Green's Functions & Propagators ⭐

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Single-Particle Green's Function

**Definition.** The retarded single-particle Green's function is G^R(x,t; x',t') = −i θ(t−t') ⟨{ψ(x,t), ψ†(x',t')}⟩, where ψ(x,t) is the field operator in the Heisenberg picture (Module 3.10), θ is the Heaviside step, and the average is over the ground state (T = 0) or the thermal ensemble. In momentum-frequency space for a translationally invariant system, G^R(k,ω) encodes everything about single-particle excitations: its poles locate quasiparticle energies, and its imaginary part gives the quasiparticle lifetime.

For a free Fermi gas, G⁰(k,ω) = 1/(ω − ε_k/ℏ + iη) where η → 0⁺ ensures causality (retarded boundary condition). The pole at ω = ε_k/ℏ is a sharp quasiparticle. Interactions broaden it: the self-energy Σ(k,ω) (Module 6.3) shifts and smears the pole.

**Demonstration.** The spectral function A(k,ω) = −(1/π) Im G^R(k,ω) is a real, positive-definite density of states in (k,ω) space. For the free gas, A(k,ω) = δ(ω − ε_k/ℏ): a delta function on the bare dispersion. With interactions, A(k,ω) acquires a Lorentzian width Γ = Im Σ/ℏ — the inverse quasiparticle lifetime. The spectral sum rule ∫ dω A(k,ω) = 1 (per spin) is exact and provides a consistency check.

The analytic structure follows from causality (Module 0.4): G^R(k,ω) is analytic in the upper half ω-plane. The Kramers–Kronig relations then link Re G^R and Im G^R: Re G^R(k,ω) = (1/π) P ∫ dω' Im G^R(k,ω')/(ω'−ω), directly analogous to the dielectric function dispersions encountered in electrodynamics. These relations are a consequence of causality alone, not of any specific model.

**Application.** Angle-resolved photoemission spectroscopy (ARPES) directly images A(k,ω): a photon ejects an electron with momentum k and energy ω, and the intensity is proportional to A(k,ω) f(ω) where f is the Fermi function. ARPES data on cuprate superconductors and Fermi liquids are interpreted almost entirely via G(k,ω).

---

## 2. Nambu–Gor'kov Green's Function and BCS

**Definition.** For a superconductor, a single Green's function is insufficient because the BCS ground state mixes particles and holes via the anomalous average F(k) = ⟨c_{−k↓}c_{k↑}⟩ ≠ 0. Nambu and Gor'kov (following Fetter & Walecka) promote the spinor Ψ_k = (c_{k↑}, c†_{−k↓})^T and define the 2×2 matrix Green's function Ĝ(k,ω) = −i ⟨T Ψ_k(t) Ψ†_k(0)⟩. Its diagonal elements are the normal G(k,ω), and its off-diagonal elements are the anomalous F(k,ω) which carry the pairing information.

**Demonstration.** Inverting the Dyson equation (Module 6.3) in Nambu space gives Ĝ(k,ω) = (ω − ξ_k τ_z − Δ τ_x)^{−1} where τ are Pauli matrices in particle-hole space, ξ_k = ε_k − μ, and Δ is the BCS gap. The poles of det Ĝ = 0 give ω = ±E_k, E_k = √(ξ²_k + Δ²) — the Bogoliubov quasiparticle spectrum derived here from Green's function poles rather than the canonical Bogoliubov transformation.

**Application.** The Nambu–Gor'kov formalism is the foundation of modern superconductivity theory: it allows systematic diagrammatic calculation of Δ (self-consistently), the density of states N(ω) ∝ |ω|/√(ω²−Δ²) (measured by tunneling spectroscopy), and the response functions needed for transport. It generalizes cleanly to unconventional superconductors (d-wave, etc.) and to Nambu spinors in topological systems.

---

## Self-test (blank page)

1. Write down G⁰(k,ω) for a free Fermi gas. Where are its poles? How does switching on an interaction Σ(k,ω) move or broaden them?
2. State the Kramers–Kronig relation for G^R(k,ω) and explain which physical principle it encodes.
3. What is the anomalous Green's function F(k,ω) and why is it zero in a normal metal but nonzero in a BCS superconductor?

---

← Previous: [Module 6.1 — Second Quantization & the Many-Body Problem](./module-6.1-second-quantization.md) · [Phase 6 index](./README.md) · Next: [Module 6.3 — Feynman Diagrams & Perturbation Theory](./module-6.3-feynman-diagrams.md) →

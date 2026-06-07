# Module 6.5 — Canonical Quantization of Fields ⭐

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. From Classical Fields to Quantum Operators

**Definition.** Canonical quantization promotes a classical field to a quantum operator by imposing equal-time commutation (bosons) or anticommutation (fermions) relations, exactly as position and momentum were promoted in ordinary QM. Starting from a classical Lagrangian density L(φ, ∂_μ φ), the canonical momentum is π(x) = ∂L/∂(∂_t φ), and the equal-time commutator [φ(x,t), π(x',t)] = iℏ δ³(x − x') (compare [q, p] = iℏ). This procedure works for any Lorentz-covariant field theory.

For the real scalar (Klein–Gordon) field, L = ½(∂_μ φ)² − ½m²φ² (natural units ℏ = c = 1 here). The equation of motion is the Klein–Gordon equation (∂² + m²)φ = 0, with plane-wave solutions of frequency ω_k = √(k² + m²). Expanding in modes: φ(x,t) = ∫ d³k/(2π)³ 1/√(2ω_k) [a_k e^{i(k·x − ω_k t)} + a†_k e^{−i(k·x − ω_k t)}]. Imposing [φ, π] = iδ³ forces [a_k, a†_{k'}] = δ³(k−k'): the mode operators are bosonic creation/annihilation operators (Module 6.1). Each mode k is a harmonic oscillator; particles are its quanta.

**Demonstration.** The Hamiltonian is H = ∫ d³k/(2π)³ ω_k (a†_k a_k + ½). The ½ per mode sums to the zero-point energy of the field — infinite in the continuum, and the first ultraviolet divergence of QFT. In curved spacetime or between conducting plates (Casimir effect) this zero-point energy has measurable consequences. Normal-ordering :H: = ∫ d³k ω_k a†_k a_k subtracts it by convention in flat-space QFT. The particle interpretation is now transparent: a†_k|0⟩ is a one-particle state of momentum k and energy ω_k, and |0⟩ (no quanta in any mode) is the vacuum.

The Dirac field (for spin-½ particles) requires Lorentz covariance from Special Relativity (Modules 1.13–1.15). The Lagrangian L = ψ̄(iγ^μ ∂_μ − m)ψ, where γ^μ are the 4×4 Dirac matrices satisfying {γ^μ, γ^ν} = 2g^{μν}, and ψ̄ = ψ†γ⁰. The equation of motion is the Dirac equation (iγ^μ ∂_μ − m)ψ = 0. Expanding ψ in plane-wave spinors u^s(k), v^s(k) and quantizing with anticommutators {b^s_k, b†s'_{k'}} = δ^{ss'} δ³(k−k') gives particles (b†) and antiparticles (d†) as distinct quanta. The anticommutation is required by the spin-statistics theorem: integer-spin fields commute (bosons), half-integer fields anticommute (fermions).

**Application.** The quantized electromagnetic field A^μ(x) yields photons as its quanta. In Coulomb gauge ∇·A = 0, the two transverse polarization modes are quantized as bosons with [a^λ_k, a†λ'_{k'}] = δ^{λλ'} δ³(k−k'). Photons are massless (ω_k = |k|c), have two helicities, and the field-theoretic description of their interaction with charged fermions is QED (Phase 8). Historically, canonical quantization of the EM field by Dirac (1927) was the birth of QFT. The framework extends directly to the W and Z bosons and gluons of the Standard Model (Phase 8), and underlies the gauge-field quantization in Module 8.1.

---

## 2. Particles, Antiparticles, and the Vacuum

**Definition.** For a complex scalar or Dirac field, charge conjugation maps particles to antiparticles: the field φ has quanta of charge +e, and φ† has quanta of charge −e (antiparticles). This is distinct from the real scalar field where particle and antiparticle are identical. The CPT theorem — a consequence of Lorentz invariance, locality, and unitarity alone — guarantees that particles and antiparticles have equal mass and opposite charge; it is among the most precisely tested results in physics.

**Demonstration.** The Feynman propagator for the scalar field G_F(x−x') = ⟨0|T φ(x)φ†(x')|0⟩ equals ∫ d⁴k/(2π)⁴ i/(k²−m²+iε) e^{ik·(x−x')}. The iε prescription (Feynman prescription) selects the propagation of positive-frequency modes (particles) forward in time and negative-frequency modes (antiparticles) backward in time. This is the propagator that appears in Feynman rules (Module 6.3) and connects the diagrammatic expansion directly to canonical quantization.

**Application.** Canonical field quantization is relativistic QFT proper. Every prediction of QED — the anomalous magnetic moment of the electron g−2 = α/π + … (matching experiment to 12 significant figures), the Lamb shift, Compton scattering — follows from quantizing the Dirac and Maxwell fields and computing Feynman diagrams in this framework. The same procedure, applied to non-Abelian gauge fields (Phase 8), gives the electroweak theory and QCD. In condensed matter, the non-relativistic limit (|k| ≪ mc/ℏ) recovers the field operators of Module 6.1, confirming that second quantization is simply canonical QFT at low energies.

---

## Self-test (blank page)

1. Starting from the Klein–Gordon Lagrangian density, derive the canonical momentum π(x) and write down the equal-time commutation relation [φ(x,t), π(x',t)]. Show that this forces [a_k, a†_{k'}] = δ³(k−k').
2. Why must the Dirac field be quantized with anticommutators rather than commutators? State the spin-statistics theorem.
3. What is an antiparticle in terms of the field expansion? How does the Feynman iε prescription encode the particle/antiparticle interpretation of the propagator?

---

← Previous: [Module 6.4 — Path Integrals & Field Theory](./module-6.4-path-integrals.md) · [Phase 6 index](./README.md) · Next: [Module 6.6 — Renormalization & the Renormalization Group](./module-6.6-renormalization.md) →

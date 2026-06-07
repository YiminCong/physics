# Module 8.2 — Quantum Electrodynamics (QED) ⭐

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The U(1) Gauge Theory of Light and Matter

**Definition.** **Quantum Electrodynamics** is the quantum field theory of electrons (and other charged leptons) interacting via photons. Its Lagrangian is the one derived in Module 8.1 by demanding local U(1) invariance: ℒ_QED = ψ̄(iγμDμ − m)ψ − (1/4)FμνFμν, where Dμ = ∂μ − ieAμ. The single free parameter is the electric charge e, equivalently the **fine-structure constant** α = e²/(4πε₀ℏc) ≈ 1/137 at low energies. The theory was completed by Feynman, Schwinger, and Tomonaga in the late 1940s using the renormalization procedure developed systematically in Module 6.6.

**Demonstration.** The Feynman rules of QED reduce every S-matrix element to a sum over diagrams. Each internal photon line contributes a propagator −igμν/q², each electron line i(γμpμ + m)/(p² − m²), and each electron–photon **vertex** contributes −ieγμ — the fundamental three-point interaction where a fermion emits or absorbs a photon. At tree level (no loops), the cross-section for **e⁺e⁻ → μ⁺μ⁻** through a virtual photon is σ = (4πα²)/(3s), where s = (2E)² is the center-of-mass energy squared. This is the flagship QED prediction for lepton colliders and agrees with experiment to better than 1%.

**Application.** QED is the **most precisely tested theory in physics**. The anomalous magnetic moment of the electron, g − 2, has been calculated through five-loop QED (∼10 000 Feynman diagrams) and measured to 13 significant figures; theory and experiment agree. The Lamb shift in hydrogen (splitting of 2S₁/₂ and 2P₁/₂) was the first triumph of renormalization and is reproduced to parts per million. These precision tests also probe for new physics: any discrepancy would signal physics beyond the Standard Model.

---

## 2. Running Coupling and the Limits of QED

**Definition.** The coupling α is not truly constant: loop corrections (vacuum polarization — virtual e⁺e⁻ pairs screening the bare charge) make it **energy-dependent**. This is the running of the coupling, derived in Module 6.6. In QED α increases logarithmically with energy: α(mZ) ≈ 1/128, compared to α(0) ≈ 1/137 at atomic energies. The energy scale at which α formally diverges (the **Landau pole**) is ∼10^{286} eV — far beyond any physics, so QED is self-consistent up to any accessible scale. This running is the opposite of QCD (Module 8.3), where the coupling decreases at high energy.

**Demonstration.** The one-loop renormalization group equation for QED is dα/d(ln μ) = α²/(3π), with β-function coefficient +1/3π > 0 (the positive sign means the coupling grows with scale — **screening**). Integrating gives 1/α(μ) = 1/α(μ₀) − (1/3π) ln(μ/μ₀). Setting μ₀ = mₑ reproduces the measured values: at μ = mZ ≈ 91 GeV, ln(mZ/mₑ) ≈ 12.5, giving Δ(1/α) ≈ −1.4, consistent with the observed change from 137 to ≈ 128.

**Application.** The running coupling is the prototype for understanding all gauge-theory couplings. In the Standard Model, the three coupling constants of SU(3)×SU(2)×U(1) run with energy and — if extended to a supersymmetric spectrum — meet at a single point near 10^{16} GeV, the tantalizing hint of **grand unification** (Module 8.5). The precision of this meeting depends on the accuracy of α measured by QED tests.

---

## Self-test (blank page)

1. Write the QED Lagrangian and identify the gauge-invariant kinetic term, the fermion mass term, and the interaction vertex. What is the Feynman rule for the vertex?
2. Derive the tree-level cross-section for e⁺e⁻ → μ⁺μ⁻ in terms of α and s using dimensional analysis or the known result; explain physically why it falls as 1/s.
3. Explain the physical origin of the running of α in QED. Why does α increase with energy (screening), and how does this differ from QCD?

---

← Previous: [Module 8.1 — Symmetries & Gauge Theory](./module-8.1-symmetries-and-gauge-theory.md) · [Phase 8 index](./README.md) · Next: [Module 8.3 — The Strong Interaction (QCD)](./module-8.3-quantum-chromodynamics.md) →

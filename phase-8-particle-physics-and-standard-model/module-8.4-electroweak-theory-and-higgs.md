# Module 8.4 — Electroweak Theory & the Higgs ⭐⭐

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Unifying Electromagnetism and the Weak Force

**Definition.** The **electroweak theory** (Glashow, Salam, Weinberg, 1967–68) unifies electromagnetism and the weak nuclear force in a single gauge theory with group SU(2)_L × U(1)_Y. The SU(2)_L factor acts only on left-handed fermion doublets (e.g., (ν_e, e)_L and (u, d)_L), with three gauge fields Wμ^{1,2,3}. The U(1)_Y factor introduces a single field Bμ associated with **weak hypercharge** Y. These four gauge fields mix: the physical mass eigenstates are the charged W± = (Wμ^1 ∓ iWμ^2)/√2, the neutral Z⁰ = Wμ^3 cos θ_W − Bμ sin θ_W, and the photon Aμ = Wμ^3 sin θ_W + Bμ cos θ_W, where θ_W ≈ 28.7° is the **Weinberg angle**. The electric charge is e = g sin θ_W = g' cos θ_W, with g, g' the SU(2) and U(1) couplings. Without additional ingredients the symmetry is exact and all gauge bosons are massless — contradicting the observed short range of the weak force.

**Demonstration.** The weak force is mediated by W± (charge-changing, e.g., n → p + e⁻ + ν̄_e in β-decay) and Z⁰ (neutral-current, e.g., νμ e⁻ → νμ e⁻). At low energies q² ≪ m_W², the W propagator reduces to a contact interaction with Fermi constant G_F/√2 = g²/(8m_W²) ≈ 1.17 × 10⁻⁵ GeV⁻². The short range r ~ ℏ/(m_W c) ~ 10⁻¹⁸ m follows directly from the large W mass (m_W ≈ 80.4 GeV, m_Z ≈ 91.2 GeV). These masses must be generated without breaking gauge invariance — the job of the Higgs mechanism.

**Application.** The SU(2) × U(1) structure unifies two of the four fundamental forces: at energies well above m_Z the electromagnetic and weak interactions have comparable strength. The W± and Z⁰ bosons were discovered at CERN in 1983 with precisely the predicted masses. The electroweak sector of the Standard Model is tested to sub-percent precision at LEP and the LHC, making it as well-confirmed as QED.

---

## 2. Spontaneous Symmetry Breaking and the Higgs Mechanism

**Definition.** The **Higgs mechanism** is spontaneous symmetry breaking (Module 2.3) applied to the gauge symmetry of the electroweak vacuum. A complex scalar doublet φ = (φ⁺, φ⁰) with SU(2)_L × U(1)_Y quantum numbers is added to the theory with a **Mexican-hat potential** V(φ) = −μ²φ†φ + λ(φ†φ)². For μ² > 0 the minimum is at |φ|² = v²/2 with v = √(μ²/λ) ≈ 246 GeV — the **vacuum expectation value**. The vacuum picks a direction ⟨φ⟩ = (0, v/√2), spontaneously breaking SU(2)_L × U(1)_Y down to U(1)_EM. This is identical in mathematics to the Ginzburg–Landau free energy (Module 5.3) and the Anderson mechanism in superconductors (Module 5.3): the photon acquires a mass inside a superconductor; here the W± and Z⁰ acquire mass in the vacuum of the universe.

**Demonstration.** Expanding φ around the minimum, φ = (0, (v + h)/√2), and inserting into the gauge-kinetic term |Dμφ|², the terms quadratic in the gauge fields produce masses: m_W = gv/2 and m_Z = √(g² + g'²) v/2 = m_W/cos θ_W. The three Goldstone modes (would-be massless scalars from the broken SU(2) directions) are absorbed as the longitudinal polarizations of W± and Z⁰ — the gauge-boson degrees of freedom increase from 2 (transverse) to 3 (transverse + longitudinal) each, accounting for the "eaten" scalars. One real scalar degree of freedom remains: the **Higgs boson h**, with mass m_h = √(2μ²) = √(2λ) v. Fermion masses arise from Yukawa couplings ℒ_Yukawa = −y_f ψ̄_L φ ψ_R + h.c., giving m_f = y_f v/√2 after symmetry breaking; the top quark has y_t ≈ 1.

**Application.** The Higgs boson was discovered at CERN's LHC in 2012 (ATLAS and CMS), with mass m_h ≈ 125 GeV — a triumph of the Standard Model developed 45 years earlier. Its couplings to W, Z, and fermions scale with mass exactly as predicted. The Higgs mechanism is the single most elegant cross-link in the curriculum: the same spontaneous-symmetry-breaking mathematics that explains the Meissner effect in a superconductor (Phase 5) explains why the weak force is short-ranged and why all elementary particles have mass.

---

## Self-test (blank page)

1. Explain why a non-zero vacuum expectation value ⟨φ⟩ = v/√2 gives masses to the W± and Z⁰ but leaves the photon massless. Which symmetry is preserved?
2. Draw the Mexican-hat potential. Identify the Goldstone modes and the Higgs direction. Explain where the longitudinal polarizations of the W and Z come from.
3. Write the Yukawa coupling for the top quark and show how it generates a Dirac mass m_t = y_t v/√2. Why is the top mass large compared to the electron mass in this framework?

---

← Previous: [Module 8.3 — The Strong Interaction (QCD)](./module-8.3-quantum-chromodynamics.md) · [Phase 8 index](./README.md) · Next: [Module 8.5 — The Standard Model & Beyond](./module-8.5-standard-model-and-beyond.md) →

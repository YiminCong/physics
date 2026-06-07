# Module 8.3 — The Strong Interaction (QCD)

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Color Charge and the SU(3) Gauge Theory

**Definition.** **Quantum Chromodynamics** is the SU(3) Yang–Mills gauge theory describing the strong nuclear force. The fundamental matter fields are **quarks** — spin-½ Dirac fermions in the fundamental (triplet) representation of SU(3), carrying one of three **color charges**: red, green, blue. The eight gauge bosons are **gluons**, valued in the adjoint representation; they carry color themselves, unlike photons. The QCD Lagrangian is ℒ_QCD = Σ_f ψ̄_f(iγμDμ − m_f)ψ_f − (1/4)Fμν^a F^{aμν}, summed over quark flavors f = u, d, s, c, b, t, with Dμ = ∂μ − ig_s Aμ^a T^a (T^a = λ^a/2 are the eight Gell-Mann matrices). The strong coupling at low energies is αs = g_s²/(4π) ≈ 0.1–1.

**Demonstration.** The SU(3) structure constants f^{abc} generate three-gluon and four-gluon vertices in the Lagrangian — gluons interact with each other. The one-loop β-function for QCD is β(αs) = −(b₀/2π)αs² with b₀ = 11 − 2n_f/3, positive for n_f ≤ 16 active quark flavors. The negative sign means αs **decreases** with increasing energy: **asymptotic freedom** (Gross, Politzer, Wilczek, 1973 Nobel Prize). The running: αs(mZ) ≈ 0.118, αs(1 GeV) ≈ 0.4. At low energies αs ∼ 1 and perturbation theory breaks down; quarks become strongly coupled and the theory is non-perturbative.

**Application.** Asymptotic freedom explains why quarks inside a proton, probed at short distances (high energy), behave nearly as free particles — as seen in deep inelastic scattering experiments at SLAC in the 1960s–70s. At large distances, the coupling grows and quark-antiquark pairs are produced before a quark can escape, so only **color-singlet** hadrons are observed (confinement). The proton's mass (938 MeV) is ∼99% from the QCD field energy of three confined quarks — the dominant source of visible mass in the universe, illustrating that E = mc² runs in reverse: fields generate mass.

---

## 2. Hadron Structure and Color Confinement

**Definition.** **Confinement** is the empirical fact that no free quark or gluon has ever been detected: the strong force does not diminish with distance (unlike 1/r² for electromagnetism), so the energy stored in the color flux tube between separating quarks grows linearly: V(r) ≈ σr for r ≳ 1 fm, with the **string tension** σ ≈ 0.9 GeV/fm. When the stored energy exceeds the threshold for a quark–antiquark pair (∼2m_π), the string "breaks" and new hadrons are produced. **Hadrons** are color-singlet composites: **mesons** (quark–antiquark, qq̄) and **baryons** (three quarks, qqq with colors summing to a singlet via the antisymmetric ε^{abc} tensor).

**Demonstration.** Color-singlet projection: a meson's color wavefunction is (rr̄ + gḡ + bb̄)/√3 — the unique SU(3) singlet in 3 ⊗ 3̄. A baryon's color wavefunction is ε^{abc}|r_a g_b b_c⟩ — the singlet in 3 ⊗ 3 ⊗ 3. Physical states must also satisfy Fermi statistics: the overall baryon wavefunction (color × spin × flavor × space) must be antisymmetric. Since ε^{abc} is totally antisymmetric in color, the remaining spin-flavor-space part must be symmetric — this forces the lowest baryons to have spin-3/2 (the Δ resonance) or specific flavor-spin correlations (the proton/neutron). Lattice QCD — QCD simulated on a discrete spacetime grid — directly confirms confinement and predicts the hadron mass spectrum to a few percent.

**Application.** The structure of protons and neutrons, and hence all nuclear physics, emerges from QCD. The **nuclear force** between hadrons (responsible for binding atomic nuclei) is a residual color force — the van der Waals analogue for color-neutral objects — mediated at long range by pion exchange. QCD also predicts **quark-gluon plasma** at temperatures T ≳ 150 MeV (attained in heavy-ion collisions at RHIC and the LHC), reconstructing the conditions of the universe microseconds after the Big Bang (Module 8.6).

---

## Self-test (blank page)

1. State the QCD β-function and explain why its sign differs from QED. What are asymptotic freedom and confinement, and how are they related to the running of αs?
2. Explain why isolated quarks are never observed. Describe what happens when two quarks are pulled apart, and how color-singlet hadrons form.
3. Identify the color wavefunction of a meson and a baryon, and explain why the Fermi statistics constraint forces a specific relationship between spin, flavor, and color quantum numbers in the ground-state baryons.

---

← Previous: [Module 8.2 — Quantum Electrodynamics (QED)](./module-8.2-quantum-electrodynamics.md) · [Phase 8 index](./README.md) · Next: [Module 8.4 — Electroweak Theory & the Higgs](./module-8.4-electroweak-theory-and-higgs.md) →

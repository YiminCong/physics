# Module 8.1 — Symmetries & Gauge Theory ⭐

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Global and Local Symmetry

**Definition.** A **global symmetry** transforms every point in spacetime by the same phase or group element: e.g., ψ → e^{iα}ψ with α constant. A **local (gauge) symmetry** promotes α to an arbitrary function α(x) of position and time. Demanding that the Lagrangian remain invariant under this x-dependent transformation forces the introduction of a **gauge field** — a connection Aμ(x) — whose job is to compensate the extra derivative term ∂μα that would otherwise spoil invariance. The gauge field transforms as Aμ → Aμ + ∂μα (for U(1)), exactly matching the covariant EM potential rule derived in Module 1.15.

**Demonstration.** Start with the free Dirac Lagrangian ℒ = ψ̄(iγμ∂μ − m)ψ, which is globally U(1)-invariant. Under ψ → e^{iα(x)}ψ the derivative picks up ψ̄γμ(∂μα)ψ — a failure of local invariance. Replace ∂μ → Dμ = ∂μ − ieAμ (the **covariant derivative**); then Dμψ → e^{iα(x)}Dμψ and the Lagrangian is restored. Adding the kinetic term −(1/4)FμνFμν for the gauge field, with Fμν = ∂μAν − ∂νAμ, yields the full QED Lagrangian. The same logic applied to a non-abelian group G replaces Aμ with a Lie-algebra-valued field Aμ = Aμ^a T^a (generators T^a), and produces self-interacting gauge bosons (Yang–Mills theory, 1954).

**Application.** This "gauge principle" is the architectural rule of the Standard Model. Every fundamental force corresponds to demanding local invariance under a group: U(1) → electromagnetism, SU(2) → weak force, SU(3) → strong force. Noether's theorem (Module 1.4) ties each continuous symmetry to a conserved current; gauge invariance specifically ties global conservation laws (charge, color, weak isospin) to the existence of force-carrier bosons.

---

## 2. Yang–Mills Theory and Non-Abelian Gauge Groups

**Definition.** In **Yang–Mills theory** the gauge group G is non-abelian (SU(N) for N ≥ 2). The field-strength tensor generalizes to Fμν^a = ∂μAν^a − ∂νAμ^a + gf^{abc}Aμ^b Aν^c, where f^{abc} are the structure constants of the Lie algebra and g is the coupling. The cubic and quartic terms in f^{abc} mean gauge bosons carry their own charge — they self-interact, unlike photons. This self-interaction has dramatic physical consequences: asymptotic freedom (QCD) and the non-perturbative vacuum structure that drives confinement.

**Demonstration.** For G = SU(2) there are three generators T^a = σ^a/2 (Pauli matrices) and three gauge fields Wμ^a. The field strength picks up the commutator term [Aμ, Aν] ∝ ε^{abc}Wμ^b Wν^c. The resulting equations of motion are non-linear: ∂^νFμν^a + gf^{abc}A^νb Fμνc = j_μ^a. Even in vacuum (jμ = 0) the equations are non-trivial; they admit topological solutions (instantons) absent in abelian theory.

**Application.** Yang–Mills theory underpins both QCD (SU(3)) and the electroweak sector (SU(2)×U(1)). The self-coupling of gluons is responsible for confinement and for the bulk of visible mass via the QCD vacuum energy. The same mathematical framework describes every force except gravity — and even gravity has a gauge-theory interpretation (diffeomorphism invariance), connecting back to Phase 7.

---

## Self-test (blank page)

1. Starting from the free Dirac Lagrangian, show step by step why local U(1) invariance requires a gauge field and derive its transformation law.
2. Explain what Noether's theorem (Module 1.4) says about the conserved current associated with global U(1) symmetry. What is the analogous statement for color SU(3)?
3. What new interaction terms appear in the Yang–Mills Lagrangian that are absent in Maxwell theory, and what physical consequence do they have?

---

← [Phase 8 index](./README.md) · Next: [Module 8.2 — Quantum Electrodynamics (QED)](./module-8.2-quantum-electrodynamics.md) →

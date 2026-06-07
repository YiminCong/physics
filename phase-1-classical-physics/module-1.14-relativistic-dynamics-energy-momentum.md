# Module 1.14 — Relativistic Dynamics & E = mc² ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Four-Vectors and Relativistic Momentum

**Definition.** A **four-vector** is a set of four quantities that transforms under a Lorentz boost exactly like (ct, x, y, z). The **proper time** τ is the Lorentz-invariant time measured by a co-moving clock, related to coordinate time by dτ = dt/γ. The **four-velocity** is U^μ = dx^μ/dτ = γ(c, v), with U^μ U_μ = c² (constant). The **four-momentum** is:

p^μ = m U^μ = (E/c, p_x, p_y, p_z),

where m is the **rest mass** (Lorentz scalar), the spatial part is the relativistic momentum p = γmv, and the time component gives the **relativistic energy** E = γmc². The invariant magnitude is:

p^μ p_μ = (E/c)² − |p|² = (mc)²,

or equivalently **E² = (pc)² + (mc²)²**. For a photon m = 0, so E = pc = hν (with the quantum relation, Module 3.1).

**Demonstration.** Low-velocity limit: E = γmc² = mc² + ½mv² + O(v⁴/c²). The first term is the **rest energy** E₀ = mc², the second is the familiar kinetic energy. At v = 0 the energy is not zero but mc² — a prediction with no classical counterpart. For an ultra-relativistic particle (v → c, pc ≫ mc²), E ≈ pc: the particle behaves like a massless particle.

**Application.** Mass–energy equivalence E = mc² quantifies the energy released in nuclear reactions and particle–antiparticle annihilation. In fission of ²³⁵U, roughly 0.1% of rest mass converts to energy — the basis of nuclear power. The four-momentum is the fundamental kinematic quantity in all of particle physics (Phase 8): invariant mass m² = (Σ p_i)² / c² identifies particles, and four-momentum conservation (replacing the separate non-relativistic conservation laws for mass, momentum, and energy) constrains every scattering and decay process.

## 2. Relativistic Dynamics and Force

**Definition.** The relativistic equation of motion is **f^μ = dp^μ/dτ**, where f^μ is the **four-force**. The spatial part gives dp/dt = F (three-force), with p = γmv; the time component gives dE/dt = F · v (power). For a particle in an electromagnetic field, the four-force is f^μ = q F^{μν} U_ν (the Lorentz force in covariant form, linking to Module 1.15). Newton's three laws are recovered in the limit v ≪ c: F = dp/dt ≈ ma.

**Demonstration.** A particle accelerated from rest through potential difference V gains kinetic energy K = qV = (γ − 1)mc². For an electron (mc² = 0.511 MeV) accelerated through V = 1 MV, γ = 1 + 1/0.511 ≈ 2.96, v/c = √(1 − 1/γ²) ≈ 0.94c. Non-relativistic treatment would give v/c ≈ 1.98 — faster than light, which is impossible. Relativistic treatment is mandatory.

**Application.** Relativistic kinematics underpins every calculation in high-energy physics. The threshold energy for particle production (e.g. e⁺e⁻ → μ⁺μ⁻ requires E_cm ≥ 2m_μ c²), invariant mass reconstruction of short-lived particles, and the kinematics of particle decays all use E² = (pc)² + (mc²)² and four-momentum conservation. The Lorentz-covariant formulation connects directly to quantum field theory (Phase 6) and the Standard Model (Phase 8).

---

**Self-test (blank page)**

1. Show that the four-momentum p^μ p_μ = m²c² is Lorentz-invariant, and derive E² = (pc)² + (mc²)² from this relation.
2. A pion (m = 135 MeV/c²) at rest decays to two photons. Using four-momentum conservation, find the energy and momentum of each photon in the pion rest frame.
3. An electron is accelerated from rest through 2 MV. Find its final γ, speed v/c, and kinetic energy. Compare the relativistic and non-relativistic results.
4. Explain why "F = ma" must be modified in special relativity. Write the correct relativistic equation of motion and recover Newton's law in the non-relativistic limit.

---

← Previous: [Module 1.13 — Special Relativity — Kinematics](./module-1.13-special-relativity-kinematics.md) · [Phase 1 index](./README.md) · Next: [Module 1.15 — Covariant Electromagnetism](./module-1.15-covariant-electromagnetism.md) →

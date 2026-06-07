# Module 1.9 — Magnetostatics

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Biot–Savart Law, Ampère's Law, and the Vector Potential

**Definition.** A steady current density J(r) produces a magnetic field B(r) given by the **Biot–Savart law**:

B(r) = (μ₀/4π) ∫ J(r′) × (r − r′) / |r − r′|³ dV′.

The static Maxwell equations for B are:

∇ · B = 0   (no magnetic monopoles),
∇ × B = μ₀ J   (Ampère's law, static).

Because ∇ · B = 0, one can always write **B = ∇ × A**, where A is the **magnetic vector potential**. A is not unique — the gauge transformation A → A + ∇χ leaves B unchanged. In the **Coulomb gauge** ∇ · A = 0, Ampère's law reduces to ∇²A = −μ₀ J, a vector Poisson equation solved by the same Green's function as electrostatics.

**Demonstration.** For an infinite straight wire carrying current I along the z-axis, Ampère's law applied to a circular loop of radius r gives B = μ₀ I / (2πr) φ̂. The same calculation in integral form demonstrates the power of symmetry: the field is tangential and constant on the loop, making the line integral trivial.

**Application.** The vector potential A is not merely a mathematical convenience — in quantum mechanics it enters the Hamiltonian directly as (p − qA)²/2m (the minimal coupling prescription), and the Aharonov–Bohm effect shows that A has physical consequences even where B = 0. This gauge freedom is the classical seed of gauge field theory (Phase 8). The magnetic dipole moment m = ½ ∫ r × J dV appears in NMR, magnetism, and the interaction of particles with external fields.

## 2. Magnetic Dipoles and Magnetic Materials

**Definition.** A small current loop of area a carrying current I has a **magnetic dipole moment** m = I a n̂. At large distances r ≫ loop size, the field is a magnetic dipole: B_dip = (μ₀/4π r³)(2m cos θ r̂ + m sin θ θ̂). The energy of a dipole in an external field is U = −m · B, and the torque is τ = m × B. For a magnetic medium, the macroscopic fields H and B are related by B = μ₀(H + M), where M is the magnetisation density.

**Demonstration.** A proton in a magnetic field B₀ ẑ has a magnetic moment m = γ_p L (where γ_p is the gyromagnetic ratio). In equilibrium it precesses about ẑ at the **Larmor frequency** ω_L = γ_p B₀. Driving with a transverse oscillating field at ω_L produces magnetic resonance — the basis of NMR and MRI.

**Application.** Magnetostatics feeds directly into electrodynamics (Module 1.10): Faraday's law of induction is the time-varying generalisation of the static Biot–Savart/Ampère framework. The gauge structure of A prefigures the four-potential A^μ in covariant electromagnetism (Module 1.15) and QED (Phase 8).

---

**Self-test (blank page)**

1. Use Ampère's law to find B inside and outside a long solenoid of n turns per unit length carrying current I.
2. Define the magnetic vector potential A. Show that the gauge transformation A → A + ∇χ leaves B unchanged. What is the Coulomb gauge condition?
3. A circular loop of radius R carries current I. Find the magnetic field on the axis at distance z from the centre using the Biot–Savart law.
4. What is the Aharonov–Bohm effect, and why does it demonstrate that A (not just B) is physically meaningful in quantum mechanics?

---

← Previous: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) · [Phase 1 index](./README.md) · Next: [Module 1.10 — Electrodynamics & Maxwell's Equations](./module-1.10-electrodynamics-maxwell-equations.md) →

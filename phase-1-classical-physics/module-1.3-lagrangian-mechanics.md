# Module 1.3 — Lagrangian Mechanics & the Variational Principle ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Principle of Least Action and Euler–Lagrange Equations

**Definition.** Choose any set of **generalised coordinates** q_i that uniquely specify the configuration of a system (they need not be Cartesian). Define the **Lagrangian** L(q, q̇, t) = T − V, where T is kinetic and V is potential energy. The **action** is the functional S[q] = ∫ L(q, q̇, t) dt integrated over the time interval [t₁, t₂]. The **principle of least action** (Hamilton's principle) asserts that the physical trajectory is the one for which S is stationary under all variations δq that vanish at the endpoints: δS = 0. Applying the calculus of variations (Module 0.1) yields one **Euler–Lagrange equation** per generalised coordinate:

d/dt (∂L/∂q̇_i) − ∂L/∂q_i = 0.

A coordinate q_i that does not appear explicitly in L is **cyclic**; its conjugate momentum p_i = ∂L/∂q̇_i is then automatically conserved.

**Demonstration.** A simple pendulum of length ℓ: choose θ as the single generalised coordinate. T = ½mℓ²θ̇², V = mgℓ(1 − cos θ), so L = ½mℓ²θ̇² − mgℓ(1 − cos θ). The Euler–Lagrange equation gives ℓθ̈ + g sin θ = 0, the exact pendulum equation, with no need to decompose tension into components.

**Application.** The Lagrangian formalism handles constrained systems and curvilinear coordinates elegantly — constraint forces never appear. The variational idea itself is the unifying thread across physics: the QM variational method (Module 3.7) minimises the energy functional; Ginzburg–Landau theory (Module 5.3) minimises a free-energy functional; and the path integral (Modules 3.10, 6.4) is a sum over all paths, each weighted by e^{iS/ℏ}, with the classical trajectory recovered as the stationary phase.

## 2. Generalised Coordinates and Constraints

**Definition.** For a system with N particles in 3D and k holonomic constraints, the number of degrees of freedom is n = 3N − k. Generalised coordinates q_1, …, q_n parametrise the **configuration space** exactly, automatically satisfying all constraints. **Generalised forces** Q_i = Σ_α F_α · ∂r_α/∂q_i appear in the equations of motion if non-conservative forces are present.

**Demonstration.** Two masses on a rod constrained to move on a frictionless horizontal surface — choosing the rod angle and centre-of-mass position as generalised coordinates reduces 4 Cartesian equations plus 2 constraint equations to 2 clean Euler–Lagrange equations.

**Application.** This coordinate freedom becomes indispensable in the central-force problem (Module 1.5) where polar coordinates reduce a 2D problem to 1D, and in rigid-body dynamics (Module 1.7) where Euler angles are the natural generalised coordinates.

---

**Self-test (blank page)**

1. Write down the Lagrangian for a particle of mass m moving in a 2D central potential V(r) using polar coordinates (r, φ). Identify the cyclic coordinate and state the conserved quantity.
2. Derive the Euler–Lagrange equation for a mass m on a spring (V = ½kx²) and confirm you recover F = ma.
3. What does it mean for the action to be "stationary"? Why is "least action" a slight misnomer?
4. How does the Lagrangian method handle a bead constrained to move on a wire, compared with Newton's approach?

---

← Previous: [Module 1.2 — Conservation Laws](./module-1.2-conservation-laws.md) · [Phase 1 index](./README.md) · Next: [Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem](./module-1.4-hamiltonian-mechanics-noether.md) →

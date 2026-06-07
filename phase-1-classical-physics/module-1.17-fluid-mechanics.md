# Module 1.17 — Fluid Mechanics

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Ideal Fluids: Continuity, Euler & Bernoulli

**Definition.** A **fluid** is a continuous medium described by fields: density ρ(r,t), pressure P(r,t), and velocity **v**(r,t). Mass conservation is the **continuity equation** ∂ρ/∂t + ∇·(ρ**v**) = 0. For an ideal (inviscid) fluid, Newton's second law per unit volume is **Euler's equation** ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇P + ρ**g**.

**Demonstration.** For steady, incompressible, irrotational flow, integrating Euler's equation along a streamline gives **Bernoulli's theorem** P + ½ρv² + ρgh = constant — faster flow means lower pressure. This explains lift on a wing, the lift in a Venturi tube, and why a shower curtain billows inward.

**Application.** The continuity equation is the prototype **conservation law** (Module 1.2) in field form, reused for charge (Module 1.10) and probability (Module 3.1). The nonlinear convective term (**v**·∇)**v** is the seed of turbulence (below) and the source of much of the difficulty in physics.

## 2. Viscosity, the Navier–Stokes Equation & Turbulence

**Definition.** A real fluid resists shear through **viscosity** η. Adding the viscous force η∇²**v** to Euler's equation gives the **Navier–Stokes equation** ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇P + η∇²**v** + ρ**g** — the master equation of fluid dynamics. The dimensionless **Reynolds number** Re = ρvL/η measures the ratio of inertial to viscous forces.

**Demonstration.** At low Re (≪1) viscous forces dominate: smooth **laminar** flow, e.g. Poiseuille flow in a pipe with a parabolic velocity profile. At high Re the nonlinear term dominates and the flow becomes **turbulent** — chaotic, eddying, and effectively unpredictable in detail (a manifestation of the chaos of Module 1.19). **Vorticity** ω = ∇×**v** quantifies local rotation.

**Application.** Navier–Stokes governs weather, ocean currents, blood flow, aerodynamics, and plasma. Whether its 3D solutions always remain smooth is an unsolved Clay Millennium Problem. Fluid ideas also reappear as analogies in physics: the **superfluid** and the dissipationless flow of a superconductor (Phase 5) are quantum fluids whose flow is constrained by a macroscopic phase.

---

**Self-test (blank page)**

1. Derive the continuity equation from conservation of mass in a fixed control volume.
2. Use Bernoulli's theorem to estimate the lift pressure difference across a wing given top/bottom speeds.
3. What does the Reynolds number compare? Estimate Re for water flowing at 1 m/s through a 1 cm pipe (η/ρ ≈ 10⁻⁶ m²/s).
4. Identify the single term in Navier–Stokes responsible for turbulence and explain why it makes the equation nonlinear.

---

← Previous: [Module 1.16 — Mechanical Waves & Acoustics](./module-1.16-mechanical-waves-acoustics.md) · [Phase 1 index](./README.md) · Next: [Module 1.18 — Continuum Mechanics & Elasticity](./module-1.18-continuum-mechanics-elasticity.md) →

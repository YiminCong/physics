# Module 1.2 — Conservation Laws

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Energy: Work–Energy Theorem and Potential Energy

**Definition.** The **work** done by a force F along a path is W = ∫ F · dr. The **work–energy theorem** states that the net work equals the change in kinetic energy: W_net = ΔKE = Δ(½mv²). A force is **conservative** if the work it does is path-independent, equivalently if ∇ × F = 0. For conservative forces one defines a **potential energy** V such that F = −∇V; the **total mechanical energy** E = ½mv² + V is then constant: dE/dt = 0.

**Demonstration.** For a mass on a spring (F = −kx, V = ½kx²), energy conservation gives ½mv² + ½kx² = const. Maximising kinetic energy (at x = 0) and potential energy (at maximum displacement A) yields v_max = A√(k/m) = Aω, the familiar result for simple harmonic motion.

**Application.** Energy methods often bypass solving the full ODE. Knowing V(x), one can read off turning points (V = E), classifying bound vs. unbound orbits without integrating the equation of motion. This potential-landscape thinking recurs throughout quantum mechanics (Module 3.2) and field theory.

## 2. Linear Momentum, Angular Momentum, and Collisions

**Definition.** **Linear momentum** p = mv is conserved whenever the net external force is zero (F_ext = dp/dt). **Angular momentum** about an origin is L = r × p; it is conserved when the net external torque τ = r × F vanishes — for example in any central-force problem. In a **collision**, total momentum is always conserved (assuming negligible external forces during impact); kinetic energy is also conserved only in elastic collisions.

**Demonstration.** In a 1D elastic collision between mass m₁ (velocity u₁) and stationary m₂, conservation of momentum and kinetic energy gives v₁ = (m₁ − m₂)/(m₁ + m₂) u₁ and v₂ = 2m₁/(m₁ + m₂) u₁. The special case m₁ = m₂ yields complete velocity exchange — billiard-ball behaviour.

**Application.** Conserved quantities are far more fundamental than the forces that produce them: each conservation law reflects a symmetry of nature. This is made precise by **Noether's theorem** (Module 1.4): time-translation symmetry → energy conservation, spatial-translation symmetry → momentum conservation, rotational symmetry → angular momentum conservation. The pattern of symmetries and conservation laws organises all of modern physics through gauge theory (Phase 8).

---

**Self-test (blank page)**

1. A 2 kg block slides from rest down a frictionless curved ramp of height h = 5 m. What is its speed at the bottom?
2. Derive the velocity of the centre of mass of a two-body system and show it moves uniformly if no external forces act.
3. A 3 kg ball moving at 4 m/s collides elastically head-on with a 1 kg ball at rest. Find both final velocities.
4. Why is angular momentum conserved for a planet orbiting the Sun? Use this to derive Kepler's second law (equal areas in equal times).

---

← Previous: [Module 1.1 — Newtonian Mechanics](./module-1.1-newtonian-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.3 — Lagrangian Mechanics & the Variational Principle](./module-1.3-lagrangian-mechanics.md) →

# Module 1.1 — Newtonian Mechanics

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Newton's Laws and Equations of Motion

**Definition.** Classical mechanics rests on Newton's three laws. (1) **Inertia**: a body remains at rest or in uniform motion unless acted on by a net force. (2) **Second law**: the net force equals the rate of change of momentum, **F = ma** (for constant mass). (3) **Action–reaction**: forces come in equal and opposite pairs. An **inertial frame** is one in which the first law holds; all inertial frames are related by Galilean transformations (v ≪ c). A **force** is any interaction that causes acceleration; common examples are gravity (F = mg near the surface), spring restoring force (F = −kx), normal force, tension, and friction.

**Demonstration.** Consider a block of mass m on a frictionless surface connected by a string over a pulley to a hanging mass M. Writing Newton's second law for each body and eliminating the tension T gives a = Mg/(m + M), the standard Atwood result. The method — isolate the body, identify all forces, apply F = ma along each axis, solve the coupled algebraic or differential equations — is the universal template.

**Application.** Every subsequent reformulation of mechanics is built on the same physics encoded here. The Lagrangian approach (Module 1.3) re-derives the same trajectories without resolving constraint forces; the Hamiltonian approach (Module 1.4) recasts the same dynamics in phase space. Knowing Newton's laws is therefore knowing what the more powerful formalisms must reproduce.

## 2. Solving Equations of Motion

**Definition.** Newton's second law is a second-order ordinary differential equation (ODE) in the position vector r(t): m r̈ = F(r, ṙ, t). The general solution contains two integration constants fixed by initial conditions r(0) and ṙ(0) = v₀.

**Demonstration.** Projectile motion under constant gravity: ẍ = 0, ÿ = −g. Integrating twice gives x(t) = v₀ cos θ · t, y(t) = v₀ sin θ · t − ½gt². The range is R = v₀² sin 2θ / g, maximised at θ = 45°.

**Application.** The same ODE machinery applies to planetary orbits (Module 1.5), coupled oscillators (Module 1.6), and charged-particle motion in EM fields — all reduce to solving or approximating Newton's equations in appropriate coordinates. ODEs of this type are treated systematically in Module 0.3.

---

**Self-test (blank page)**

1. State Newton's three laws and give one everyday example of each.
2. An object of mass m slides down a frictionless incline of angle θ. Derive its acceleration along the slope using Newton's second law.
3. Two blocks of masses m₁ and m₂ are connected by a light string over a frictionless pulley. Find the tension in the string.
4. Why must Newton's laws be stated in an inertial frame? How would F = ma appear to an observer in an accelerating car?

---

[Phase 1 index](./README.md) · Next: [Module 1.2 — Conservation Laws](./module-1.2-conservation-laws.md) →

# Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Hamiltonian and Hamilton's Equations

**Definition.** Given the Lagrangian L(q, q̇, t), define the **conjugate momentum** p_i = ∂L/∂q̇_i. The **Hamiltonian** is obtained by a Legendre transform: H(q, p, t) = Σ_i p_i q̇_i − L. For systems with time-independent, velocity-independent potentials, H = T + V = total energy. **Hamilton's equations** replace the n second-order Euler–Lagrange equations with 2n first-order equations:

q̇_i = ∂H/∂p_i,   ṗ_i = −∂H/∂q_i.

The state of the system is a point in **phase space** (q, p), and Hamilton's equations describe the flow of that point. The **Poisson bracket** of two observables f, g is {f, g} = Σ_i (∂f/∂q_i ∂g/∂p_i − ∂f/∂p_i ∂g/∂q_i). In particular {q_i, p_j} = δ_{ij}, and the equation of motion for any observable is ḟ = {f, H} + ∂f/∂t.

**Demonstration.** For the 1D harmonic oscillator H = p²/2m + ½mω²q². Hamilton's equations give q̇ = p/m and ṗ = −mω²q, which combine to q̈ = −ω²q. Phase-space trajectories are ellipses in the (q, p) plane with area 2πE/ω, an adiabatic invariant.

**Application.** Poisson brackets are the classical skeleton of quantum **commutators**: the canonical quantisation rule replaces {q, p} = 1 with [q̂, p̂] = iℏ (Module 3.3). The Hamiltonian generates time evolution both classically (via Poisson brackets) and quantum mechanically (via the Schrödinger equation, Module 3.10). Phase-space thinking underlies statistical mechanics (Phase 2) through Liouville's theorem (phase-space volume is conserved).

## 2. Noether's Theorem: Symmetry → Conservation Law

**Definition.** **Noether's theorem** (1915) states that every continuous (differentiable) symmetry of the action S = ∫L dt corresponds to a conserved quantity. Formally, if L is invariant under a one-parameter family of transformations q_i → q_i + ε δq_i (to first order in ε), the **Noether charge** Q = Σ_i (∂L/∂q̇_i) δq_i is conserved: dQ/dt = 0.

**Demonstration.** Three canonical examples: (1) L independent of time t → H conserved (energy). (2) L independent of a spatial translation x → p_x conserved (linear momentum). (3) L independent of a rotation angle φ → L_z = mr²φ̇ conserved (angular momentum). Each follows from the cyclic-coordinate argument in Module 1.3 applied to the appropriate generalised coordinate.

**Application.** Noether's theorem is arguably the deepest organising principle in all of physics. In field theory, local (gauge) symmetries produce the conservation of charge and the existence of force-carrying bosons (Phase 8). The global U(1) symmetry of quantum mechanics produces charge conservation; SU(2) and SU(3) gauge symmetries produce the weak and strong forces. Every fundamental interaction is a consequence of a symmetry — the logic that starts here.

---

**Self-test (blank page)**

1. Starting from L = ½mq̇² − V(q), perform the Legendre transform to obtain H and write down Hamilton's equations.
2. Compute the Poisson bracket {L_x, L_y} for a 3D particle, where L = r × p. What does the result tell you about angular momentum components?
3. Show, using Noether's theorem, that if V depends only on the distance |r₁ − r₂| between two particles, total momentum is conserved.
4. What is the quantum analogue of the classical Poisson bracket {q, p} = 1, and why is it physically significant?

---

← Previous: [Module 1.3 — Lagrangian Mechanics & the Variational Principle](./module-1.3-lagrangian-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.5 — Central-Force Problem & Kepler](./module-1.5-central-force-kepler.md) →

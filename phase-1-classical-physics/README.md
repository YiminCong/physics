# Phase 1 — Classical Physics

Classical physics encompasses Newtonian and analytical mechanics, electromagnetism, and their relativistic completion in special relativity — the indispensable foundation on which all of modern physics is built. Each module follows the **Definition → Demonstration → Application** format: a precise statement of the core idea, a worked or illustrative example that makes it concrete, and a signpost to where the idea recurs at deeper levels.

## Prerequisites

A working knowledge of **Phase 0** is assumed throughout, especially:
- **Module 0.1** — Calculus & Taylor Series (variational calculus, Taylor-expanding potentials)
- **Module 0.3** — Differential Equations (equations of motion, boundary-value problems)
- **Module 0.6** — Vector Calculus & Tensors (∇, ∇·, ∇×; index notation for relativistic modules)

Fourier methods (Module 0.5) are needed for optics and waves; linear algebra (Module 0.2) for normal modes and the inertia tensor.

## Modules

### Mechanics (1.1–1.7)

| Module | Title | Notes |
|--------|-------|-------|
| [1.1](./module-1.1-newtonian-mechanics.md) | Newtonian Mechanics | F = ma, inertial frames, equations of motion |
| [1.2](./module-1.2-conservation-laws.md) | Conservation Laws | Energy, momentum, angular momentum, collisions |
| [1.3](./module-1.3-lagrangian-mechanics.md) | Lagrangian Mechanics & the Variational Principle ⭐ | Action S = ∫L dt, Euler–Lagrange, generalised coordinates |
| [1.4](./module-1.4-hamiltonian-mechanics-noether.md) | Hamiltonian Mechanics, Action & Noether's Theorem ⭐ | H(q,p), Hamilton's equations, Poisson brackets, symmetry → conservation |
| [1.5](./module-1.5-central-force-kepler.md) | Central-Force Problem & Kepler | Reduced mass, effective potential, Kepler's laws |
| [1.6](./module-1.6-small-oscillations-coupled-oscillators.md) | Small Oscillations & Coupled Oscillators ⭐ | SHO, resonance, normal modes, eigenvalue problem |
| [1.7](./module-1.7-rigid-body-non-inertial-frames.md) | Rigid-Body Dynamics & Non-Inertial Frames | Inertia tensor, Euler's equations, Coriolis force |

### Electromagnetism (1.8–1.12)

| Module | Title | Notes |
|--------|-------|-------|
| [1.8](./module-1.8-electrostatics-boundary-value-problems.md) | Electrostatics & Boundary-Value Problems ⭐ | Gauss's law, Poisson/Laplace, separation of variables |
| [1.9](./module-1.9-magnetostatics.md) | Magnetostatics | Biot–Savart, Ampère, vector potential A |
| [1.10](./module-1.10-electrodynamics-maxwell-equations.md) | Electrodynamics & Maxwell's Equations ⭐ | Faraday, displacement current, all four Maxwell equations |
| [1.11](./module-1.11-em-waves-radiation.md) | Electromagnetic Waves & Radiation | Wave equation, c = 1/√(μ₀ε₀), Poynting vector, Larmor formula |
| [1.12](./module-1.12-optics-interference.md) | Optics & Interference | Geometric optics, Huygens, double-slit, diffraction as Fourier transform |

### Special Relativity (1.13–1.15)

| Module | Title | Notes |
|--------|-------|-------|
| [1.13](./module-1.13-special-relativity-kinematics.md) | Special Relativity — Kinematics ⭐ | Einstein's postulates, Lorentz transformation, Minkowski spacetime, s² |
| [1.14](./module-1.14-relativistic-dynamics-energy-momentum.md) | Relativistic Dynamics & E = mc² ⭐ | Four-vectors, p^μ, E² = (pc)² + (mc²)², relativistic force |
| [1.15](./module-1.15-covariant-electromagnetism.md) | Covariant Electromagnetism | Four-potential A^μ, field tensor Fμν, covariant Maxwell equations |

## Phase 1 Checkpoint (blank page)

Work through these without notes — they span the whole phase.

1. A particle moves in a central potential V(r) = −k/r. Using the Lagrangian in polar coordinates, find the equations of motion and derive Kepler's orbit equation r(φ) = p/(1 + ε cos φ).
2. State Noether's theorem. Apply it to show that invariance of the Lagrangian under spatial translation implies conservation of total linear momentum.
3. Write down all four Maxwell equations. Take the curl of Faraday's law, substitute Ampère–Maxwell, and derive the wave equation for E in free space. Identify the speed of propagation.
4. Define the electromagnetic field tensor F^{μν}. Write Maxwell's inhomogeneous equations in covariant form and show that charge conservation ∂_μ J^μ = 0 is automatic.
5. An electron and positron (each mass m = 0.511 MeV/c²) annihilate at rest to produce two photons. Using four-momentum conservation, find the frequency of each photon.
6. A pendulum of length ℓ and mass m is released from small angle θ₀. Use the Hamiltonian formalism to show the phase-space orbit is an ellipse and identify the adiabatic invariant.
7. Two masses m connected to fixed walls and each other by identical springs of constant k form a symmetric coupled oscillator. Find the normal mode frequencies and sketch the corresponding motions.
8. Explain physically why a purely electric Coulomb field in the rest frame of a charge acquires a magnetic component in a frame where the charge moves. Which transformation law makes this precise?

---

→ Continue to **[Phase 2 — Thermodynamics & Statistical Mechanics](../phase-2-thermodynamics-statistical-mechanics/)**.

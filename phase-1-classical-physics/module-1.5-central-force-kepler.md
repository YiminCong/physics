# Module 1.5 — Central-Force Problem & Kepler

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Reduction to a One-Dimensional Problem

**Definition.** A **central force** depends only on the separation r = |r₁ − r₂| and points along the line joining two bodies: F = F(r) r̂. Introducing the **reduced mass** μ = m₁m₂/(m₁ + m₂), the two-body problem reduces to the one-body problem of a particle of mass μ in the potential V(r). Since F is central, angular momentum L = μr²φ̇ is conserved (Noether, Module 1.4), and motion is confined to a plane. Writing the total energy in polar coordinates and eliminating φ̇ via L introduces the **effective potential**:

V_eff(r) = V(r) + L²/(2μr²).

The second term is the centrifugal barrier. Radial motion satisfies ½μṙ² + V_eff(r) = E, a one-dimensional energy equation. Turning points (ṙ = 0) occur where E = V_eff(r).

**Demonstration.** For gravity V(r) = −Gm₁m₂/r, the effective potential has a minimum (stable circular orbit) at r₀ = L²/(Gμ²m_total). Integrating the orbit equation d²u/dφ² + u = −μ/(L²) · F(1/u) (where u = 1/r) for the 1/r force gives a conic section: r = p/(1 + ε cos φ), where p = L²/(Gμ²m_total) is the semi-latus rectum and ε is the eccentricity. Ellipses (ε < 1), parabolas (ε = 1), and hyperbolas (ε > 1) correspond to E < 0, E = 0, E > 0.

**Application.** Kepler's three laws follow directly. (1) Orbits are ellipses with the Sun at one focus (ε < 1 solutions). (2) Equal areas in equal times — this is simply conservation of L: dA/dt = L/(2μ) = const. (3) T² ∝ a³, where a is the semi-major axis, follows from integrating the period using the ellipse geometry.

## 2. Connection to the Quantum Hydrogen Atom

**Definition.** The quantum version of the central-force problem replaces the classical orbit with the Schrödinger equation in spherical symmetry. The −k/r potential of the hydrogen atom (k = e²/4πε₀) is the quantum analogue of the gravitational −Gm₁m₂/r, with L replaced by the quantum number ℓ and the discrete energy levels E_n = −13.6 eV/n².

**Application.** The classical analysis here — reduction by angular-momentum conservation, effective potential, energy classification of orbits — maps directly onto the quantum treatment of the hydrogen atom (Module 3.4). Understanding Kepler's problem in classical terms builds the geometric and physical intuition needed for that quantum solution.

---

**Self-test (blank page)**

1. Write down the effective potential for a particle in the gravitational field V(r) = −k/r. Sketch V_eff(r) and identify the radius of a circular orbit.
2. Derive Kepler's second law (equal areas in equal times) as a direct consequence of angular momentum conservation.
3. What determines whether a gravitational orbit is an ellipse, parabola, or hyperbola? Give the condition in terms of total energy E.
4. How does the reduced-mass trick allow you to treat a two-body problem as a one-body problem? What is the reduced mass of the Earth–Sun system?

---

← Previous: [Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem](./module-1.4-hamiltonian-mechanics-noether.md) · [Phase 1 index](./README.md) · Next: [Module 1.6 — Small Oscillations & Coupled Oscillators](./module-1.6-small-oscillations-coupled-oscillators.md) →

# Module 1.8 — Electrostatics & Boundary-Value Problems ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Electric Field, Gauss's Law, and the Potential

**Definition.** The **electric field** E(r) is the force per unit charge exerted on a stationary test charge. For a point charge q at the origin, Coulomb's law gives E = q/(4πε₀) · r̂/r². For a continuous charge distribution ρ(r), the field obeys **Gauss's law** in integral and differential forms:

∮ E · dA = Q_enc / ε₀   ⟺   ∇ · E = ρ / ε₀.

Since ∇ × E = 0 for static fields, E = −∇φ, where the **electric potential** φ satisfies **Poisson's equation**:

∇²φ = −ρ / ε₀.

In charge-free regions this reduces to **Laplace's equation** ∇²φ = 0.

**Demonstration.** Gauss's law applied to a sphere of radius r around a point charge q gives E = q/(4πε₀r²) r̂ — Coulomb's law recovered. For an infinite line charge λ (C/m), a cylindrical Gaussian surface of radius r and length L gives E = λ/(2πε₀r), pointing radially outward.

**Application.** The potential energy of a charge distribution encodes screening, capacitance, and the forces governing atomic structure. Gauss's law is the first of Maxwell's equations (Module 1.10). The Laplace/Poisson structure recurs throughout physics: gravity (∇²φ_grav = 4πGρ), diffusion, and the time-independent Schrödinger equation in certain limits all share this form.

## 2. Boundary-Value Problems: Separation of Variables

**Definition.** Solving ∇²φ = 0 in a region with specified boundary conditions is a **boundary-value problem**. The uniqueness theorem guarantees that specifying φ (Dirichlet) or ∂φ/∂n (Neumann) on the boundary determines φ uniquely. In Cartesian, cylindrical, or spherical coordinates, Laplace's equation separates into ODEs (Module 0.3). In spherical coordinates the solutions are **spherical harmonics** Y_ℓ^m(θ, φ) multiplied by r^ℓ or r^{−(ℓ+1)}.

**Demonstration.** For a grounded conducting sphere of radius R in a uniform external field E₀ ẑ, separation of variables gives φ_out = −E₀ r cos θ + E₀ R³ cos θ / r². The second term is a dipole field; its coefficient is fixed by the boundary condition φ(R) = 0. The induced surface charge density is σ = 3ε₀ E₀ cos θ.

**Application.** Boundary-value methods determine the capacitance of arbitrary geometries, the fields inside waveguides, and the electrostatic energy of molecular charge distributions. The method of images provides elegant shortcuts for planar and spherical conductors. The spherical-harmonic solutions here are identical to the angular wavefunctions of the hydrogen atom (Module 3.4), making this a direct classical foundation for quantum central-force problems.

---

**Self-test (blank page)**

1. State Gauss's law in both integral and differential forms. Use the integral form to find E at distance r from an infinite uniformly charged plane with surface charge density σ.
2. A solid sphere of radius R carries uniform charge density ρ. Find φ(r) everywhere by solving Poisson's equation with appropriate boundary conditions.
3. What is the uniqueness theorem for electrostatic boundary-value problems, and why is it practically important?
4. Explain why ∇ × E = 0 in electrostatics allows you to introduce a scalar potential. What breaks this and what replaces it in electrodynamics (Module 1.10)?

---

← Previous: [Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames](./module-1.7-rigid-body-non-inertial-frames.md) · [Phase 1 index](./README.md) · Next: [Module 1.9 — Magnetostatics](./module-1.9-magnetostatics.md) →

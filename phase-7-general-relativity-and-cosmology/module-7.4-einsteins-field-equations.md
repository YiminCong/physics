# Module 7.4 — Einstein's Field Equations ⭐⭐

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Stress–Energy Tensor and the Field Equations

**Definition.** The source of spacetime curvature is the *stress–energy tensor* Tμν — a symmetric rank-2 tensor encoding the local density and flux of energy and momentum. Its components are:
- T₀₀ = energy density (includes rest mass, kinetic, internal energy)
- T₀i = momentum density = (1/c) × energy flux in xi direction
- Tij = stress tensor (pressure on diagonal, shear off diagonal)

For a perfect fluid: Tμν = (ρ + p/c²)uμuν + p gμν, where ρ is proper energy density, p is pressure, and uμ = dxμ/dτ is the four-velocity. Conservation of energy-momentum is ∇μ Tμν = 0.

Einstein's field equations (EFE) are:

Gμν = R_{μν} − ½ R g_{μν} = (8πG/c⁴) Tμν

This is a set of 10 coupled, nonlinear partial differential equations for g_{μν}(x). The left side is purely geometric (the Einstein tensor, Module 7.2); the right side encodes matter and energy. In words: *matter tells spacetime how to curve, spacetime tells matter how to move*.

With the *cosmological constant* Λ (reintroduced for dark energy; see Module 7.6):

R_{μν} − ½ R g_{μν} + Λ g_{μν} = (8πG/c⁴) Tμν

**Demonstration.** *Newtonian limit*: in the weak-field, slow-matter limit, only the 00-component survives. T₀₀ ≈ ρc², and G₀₀ ≈ −2∇²Φ/c² (where Φ is the Newtonian potential). The 00-component of the EFE gives ∇²Φ = 4πGρ — Poisson's equation of Newtonian gravity (Module 1.1/1.5). GR reduces to Newtonian gravity in the appropriate limit.

*Vacuum equations*: when Tμν = 0 everywhere, the EFE reduce to R_{μν} = 0. This does not mean flat spacetime (Rμνρσ need not vanish), merely traceless Ricci curvature. The Schwarzschild solution (Module 7.5) solves R_{μν} = 0 outside a spherical mass.

**Application.** The EFE are the central equation of classical gravity. Their solutions include:
- The Schwarzschild metric (spherical vacuum; Module 7.5)
- The Kerr metric (rotating black hole; Module 7.5)
- The FLRW metric (homogeneous universe; Module 7.6)
- Gravitational wave perturbations of flat spacetime (Module 7.5)

The coefficient 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J makes gravity extraordinarily weak: enormous energy densities produce tiny metric perturbations in ordinary conditions.

---

## 2. The Einstein–Hilbert Action

**Definition.** Like all fundamental laws in physics, the EFE follow from a variational principle (Module 1.3). The *Einstein–Hilbert action* is:

S = (c⁴/16πG) ∫ (R − 2Λ) √(−g) d⁴x + S_matter

where g = det(g_{μν}) and √(−g) d⁴x is the invariant spacetime volume element. Varying S with respect to the metric g_{μν} and setting δS/δgμν = 0 yields exactly the EFE with cosmological constant.

**Demonstration.** The variation produces three terms: (i) variation of R_{μν} gives a surface term (Gibbons–Hawking–York boundary term, discarded); (ii) variation of R gives R_{μν} δgμν; (iii) variation of √(−g) gives −½ g_{μν} R δgμν. Together: δ(R√(−g)) = √(−g)(R_{μν} − ½ R g_{μν}) δgμν = √(−g) Gμν δgμν. The matter action variation defines Tμν = −(2/√(−g)) δS_matter/δgμν, completing the derivation.

**Application.** The action formulation is essential for:
- Coupling GR to quantum fields (semiclassical gravity, Hawking radiation)
- Systematically adding higher-order curvature corrections (theories beyond GR)
- Deriving conservation laws via Noether's theorem — the contracted Bianchi identity ∇μ Gμν = 0 is an automatic consequence of diffeomorphism invariance of the action
- Extensions such as Brans–Dicke theory, f(R) gravity, and string-theory-motivated corrections

The EFE, derived from the simplest possible covariant action linear in R, are arguably the most elegant fundamental law in physics.

---

**Self-test (blank page)**

1. Write down the EFE in full, identify each tensor, and state the physical meaning of both sides. What does the factor 8πG/c⁴ tell you about the stiffness of spacetime?
2. Show that ∇μ Tμν = 0 follows automatically from the EFE and the contracted Bianchi identity ∇μ Gμν = 0. Why is this physically satisfying?
3. Write down Tμν for a perfect fluid. In the non-relativistic limit (p ≪ ρc²), what does the EFE reduce to?

---

← Previous: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) · [Phase 7 index](./README.md) · Next: [Module 7.5 — Black Holes & Gravitational Waves](./module-7.5-black-holes-and-gravitational-waves.md) →

# Module 7.2 — Tensors, the Metric & Curvature ⭐

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Metric Tensor and the Line Element

**Definition.** In curved spacetime, the separation between neighbouring events is encoded in the *metric tensor* g_{μν}(x) — a symmetric rank-2 covariant tensor field (generalizing the constant Minkowski metric ημν of Module 1.13 and the abstract metric of Module 0.6). The invariant line element is

ds² = g_{μν} dxμ dxν

(sum over μ, ν = 0, 1, 2, 3 by Einstein convention). The proper time along a timelike worldline satisfies c² dτ² = −ds². The inverse metric gμν is defined by gμρ g_{ρν} = δμν. Indices are raised and lowered with g: Vμ = g_{μν} Vν, Vμ = gμν Vν.

**Demonstration.** In flat spacetime ds² = ημν dxμ dxν = −c²dt² + dx² + dy² + dz². On the surface of a 2-sphere of radius a: ds² = a²(dθ² + sin²θ dφ²), so g_{θθ} = a², g_{φφ} = a² sin²θ, g_{θφ} = 0. At the Schwarzschild radius of a black hole the metric components diverge in Schwarzschild coordinates — a coordinate (not physical) singularity (see Module 7.5). The metric carries all geometric information; distances, angles, volumes, and the equations of motion all follow from g_{μν}.

**Application.** Every computation in GR starts with specifying or solving for g_{μν}. Given a metric, one immediately reads off: proper distances (∫ds along a path), local clock rates (dτ), and the causal structure (sign of ds²). The metric is the fundamental field of GR, replacing the Newtonian gravitational potential φ.

---

## 2. Connection, Covariant Derivative, and Curvature

**Definition.** On a curved manifold, ordinary partial derivatives ∂μ do not produce tensors when acting on tensors of rank ≥ 1 (components mix under coordinate changes). The *Levi-Civita connection* (Christoffel symbols) resolves this:

Γρμν = ½ gρσ (∂μ g_{σν} + ∂ν g_{σμ} − ∂σ g_{μν})

These are symmetric in the lower indices (Γρμν = Γρνμ) and vanish in Minkowski coordinates. The *covariant derivative* of a contravariant vector is

∇μ Vν = ∂μ Vν + Γν μρ Vρ

and for a covariant vector ∇μ Vν = ∂μ Vν − Γρ μν Vρ. Covariant derivatives of the metric vanish: ∇ρ g_{μν} = 0 (*metric compatibility*).

The *Riemann curvature tensor* measures the failure of covariant derivatives to commute:

[∇μ, ∇ν] Vρ = Rρ σμν Vσ

with components

Rρ σμν = ∂μ Γρ νσ − ∂ν Γρ μσ + Γρ μλ Γλ νσ − Γρ νλ Γλ μσ

From Rρ σμν one constructs:
- *Ricci tensor*: R_{μν} = Rρ μρν (contraction on first and third index)
- *Ricci scalar*: R = gμν R_{μν}
- *Einstein tensor*: Gμν = R_{μν} − ½ R g_{μν} (divergence-free: ∇μ Gμν = 0)

**Demonstration.** On a 2-sphere of radius a, the only independent component of the Riemann tensor is R_{θφθφ} = a² sin²θ. The Ricci scalar is R = 2/a²: constant positive curvature. As a → ∞ the plane is recovered and R → 0. For flat Minkowski space, all components of Rμνρσ vanish identically — covariant derivatives commute and the global inertial frame exists.

**Application.** The Christoffel symbols enter the geodesic equation (Module 7.3) governing particle paths. The Einstein tensor Gμν, built entirely from g_{μν} and its first two derivatives, is the geometric side of Einstein's field equations (Module 7.4). The contracted Bianchi identity ∇μ Gμν = 0 guarantees energy-momentum conservation ∇μ Tμν = 0 as a consequence of the geometry. This is the complete mathematical toolkit of curved spacetime, synthesizing the tensor calculus of Module 0.6 with the Lorentzian geometry of Module 1.13.

---

**Self-test (blank page)**

1. Starting from g_{μν}, derive the Christoffel symbols Γρ μν. Why are they not tensors, yet they are essential for defining the covariant derivative?
2. Write out all symmetries of the Riemann tensor Rμνρσ (antisymmetries, pair symmetry, first Bianchi identity). How many independent components does it have in 4-D?
3. Verify that ∇ρ g_{μν} = 0 follows from the definition of Γ — this is the condition of metric compatibility.

---

← Previous: [Module 7.1 — The Equivalence Principle & Curved Spacetime](./module-7.1-equivalence-principle-and-curved-spacetime.md) · [Phase 7 index](./README.md) · Next: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) →

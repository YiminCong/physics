# Module 0.6 — Vector Calculus, Tensors & Differential Forms

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Vector calculus is the native language of fields — electric, magnetic, gravitational. Tensors extend that language to curved spacetime, and differential forms give it a coordinate-free elegance that pays off in general relativity and advanced electrodynamics.

---

## 1. Grad, Div, Curl & the Integral Theorems

**Definition.** The **gradient** ∇f of a scalar field is a vector pointing in the direction of steepest increase, with magnitude equal to that rate of increase. The **divergence** ∇·F of a vector field measures the net outward flux per unit volume — how much the field "spreads out" from a point. The **curl** ∇×F measures the rotation or circulation per unit area around a point. The **Laplacian** ∇²f = ∇·(∇f) combines both, giving the rate at which f differs from its local average.

Two integral theorems convert between volume/surface integrals and boundary integrals:
- **Divergence theorem (Gauss):** ∫_V (∇·F) dV = ∮_S F·dA — total divergence inside equals flux through the boundary.
- **Stokes' theorem:** ∫_S (∇×F)·dA = ∮_C F·dl — total curl through a surface equals circulation around its boundary.

**Demonstration.** Maxwell's equations illustrate every operator at once. In differential form: ∇·E = ρ/ε₀ (divergence of E equals charge density), ∇·B = 0 (no magnetic monopoles), ∇×E = −∂B/∂t (curl of E driven by changing B), ∇×B = μ₀J + μ₀ε₀ ∂E/∂t (curl of B driven by current and changing E). In spherical coordinates, ∇² = (1/r²) ∂/∂r(r² ∂/∂r) + (1/r² sin θ) ∂/∂θ(sin θ ∂/∂θ) + (1/r² sin²θ) ∂²/∂φ², the form needed for the hydrogen atom's Schrödinger equation.

**Application.** Gauss's law in integral form — ∮ E·dA = Q_enc/ε₀ — follows from the divergence theorem applied to ∇·E = ρ/ε₀, and it is the standard route to the Coulomb field of a point charge (Module 1.8). Stokes' theorem relates Faraday's law in integral and differential form (Module 1.10). The Laplacian ∇²φ = 0 is Laplace's equation for the electrostatic potential in charge-free regions (Module 1.8).

---

## 2. Tensors & Index Notation

**Definition.** A **scalar** is a rank-0 tensor (one component), a **vector** is rank-1 (one index), and a general **tensor** T^{μν} is rank-2 (two indices, transforming as a product of two vectors under coordinate changes). **Einstein summation convention**: a repeated index — one upper, one lower — is summed over all values, e.g. A^μ B_μ = Σ_μ A^μ B_μ.

The **metric tensor** g_{μν} encodes the geometry of the space: the invariant interval (distance) between two nearby events is ds² = g_{μν} dx^μ dx^ν. In flat spacetime with signature (−,+,+,+), g_{μν} = diag(−1, 1, 1, 1) (the Minkowski metric η_{μν}). The metric **raises and lowers indices**: V_μ = g_{μν} V^ν, so it converts between contravariant (upper) and covariant (lower) components.

**Differential forms** give an index-free, coordinate-independent framework: a p-form is an antisymmetric rank-p covariant tensor. The exterior derivative d maps p-forms to (p+1)-forms and satisfies d² = 0 — a generalization of ∇×(∇f) = 0 and ∇·(∇×F) = 0. Maxwell's equations in this language compress to dF = 0 and d★F = J, where F is the 2-form Faraday tensor and ★ is the Hodge dual.

**Demonstration.** In special relativity, the four-momentum is p^μ = (E/c, pₓ, p_y, p_z). Its Lorentz-invariant magnitude is p^μ p_μ = g_{μν} p^μ p^ν = −E²/c² + |p|² = −(mc)², recovering E² = (pc)² + (mc²)² — an entirely index-based derivation.

**Application.** Vector calculus (∇, ∇·, ∇×) is the language of all classical electromagnetism in Modules 1.8–1.11. Tensor index notation and the metric g_{μν} are indispensable for covariant electrodynamics (Module 1.15) and are the entire technical foundation of general relativity (Phase 7), where g_{μν} becomes dynamical — the field itself. Differential forms give the most compact statement of Maxwell's equations and appear in the geometric formulation of gauge theories (Phase 6).

---

## Module 0.6 Self-Test (blank page)

1. State the physical meaning of ∇·F and ∇×F; give one Maxwell equation illustrating each.
2. State the divergence theorem and Stokes' theorem; explain which Maxwell equation each converts between integral and differential form.
3. Write the Laplacian in spherical coordinates and identify where it appears in the hydrogen-atom Schrödinger equation.
4. Define the Einstein summation convention; write the invariant interval ds² using g_{μν}.
5. Show that p^μ p_μ = −(mc)² for a relativistic particle and interpret the result.
6. State what a differential form is and what d² = 0 generalizes.

---

← Previous: [Module 0.5 — Fourier Analysis & Probability](./module-0.5-fourier-analysis-and-probability.md) · [Phase 0 index](./README.md)

# Module 1.18 — Continuum Mechanics & Elasticity

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Stress and Strain

**Definition.** Continuum mechanics treats a deformable solid as a continuous field rather than discrete atoms. Internal forces are encoded in the **stress tensor** σ_{ij} (the i-component of force per unit area on a surface with normal in the j-direction); deformation is encoded in the **strain tensor** ε_{ij} = ½(∂u_i/∂x_j + ∂u_j/∂x_i), built from the displacement field **u**(r). Both are rank-2 tensors (Module 0.6).

**Demonstration.** For small deformations of an isotropic solid, stress is linear in strain — **Hooke's law** in tensor form σ_{ij} = λ (tr ε) δ_{ij} + 2μ ε_{ij}, with the **Lamé coefficients** λ and μ (shear modulus). In 1D this reduces to the familiar σ = E ε with **Young's modulus** E; a hanging rod stretches by ΔL/L = σ/E.

**Application.** This is the engineering foundation for beams, bridges, and materials science, and the static limit of the dynamic theory below. The same tensor bookkeeping (stress–energy) reappears as the *source* of gravity in general relativity (Module 7.4).

## 2. Elastic Waves & the Continuum Limit

**Definition.** Newton's second law for a continuous medium, ρ ∂²u_i/∂t² = ∂σ_{ij}/∂x_j, combined with Hooke's law gives the **elastic wave equation**. An isotropic solid supports two wave types: **longitudinal (P) waves** (compression) and **transverse (S) waves** (shear), travelling at different speeds set by the elastic moduli and density.

**Demonstration.** A crystal is *not* truly continuous; on the scale of the lattice spacing the continuum description breaks down and waves become the discrete normal modes of coupled atoms (Module 1.6). The long-wavelength acoustic phonons of a solid (Module 4.3) are exactly these elastic waves; the continuum theory is their k → 0 limit.

**Application.** Elastic waves are the basis of **seismology** — P and S waves from earthquakes probe the Earth's interior, and the S-wave shadow zone revealed the liquid outer core. The continuum-to-lattice connection is the bridge from this classical module to the phonons that drive heat capacity and superconductivity (Phases 4–5).

---

**Self-test (blank page)**

1. Define the stress and strain tensors and explain why each is symmetric.
2. Write Hooke's law for an isotropic solid and reduce it to σ = Eε in one dimension.
3. Name the two types of elastic wave in a solid and state physically why they travel at different speeds.
4. Explain how the acoustic phonon branch of a crystal relates to the classical elastic wave equation.

---

← Previous: [Module 1.17 — Fluid Mechanics](./module-1.17-fluid-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.19 — Nonlinear Dynamics & Chaos](./module-1.19-nonlinear-dynamics-chaos.md) →

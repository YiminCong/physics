# Module 1.15 — Covariant Electromagnetism

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Four-Potential and the Field Tensor

**Definition.** The scalar potential φ and vector potential A (Module 1.10) combine into the **four-potential**:

A^μ = (φ/c, A_x, A_y, A_z).

The **gauge transformation** A^μ → A^μ + ∂^μ χ (where ∂^μ = (∂_t/c, −∇)) leaves all physical fields unchanged — the covariant statement of gauge invariance. From A^μ one constructs the **electromagnetic field tensor** (an antisymmetric rank-2 tensor):

F^{μν} = ∂^μ A^ν − ∂^ν A^μ.

Its components are: F^{0i} = E_i/c and F^{ij} = −ε_{ijk} B_k. Explicitly, the six independent components of F^{μν} encode all three components of E and all three of B — the electric and magnetic fields are not separate objects but two faces of a single relativistic entity.

**Demonstration.** Under a Lorentz boost with velocity v along the x-axis, the field tensor transforms as F^{μν} → Λ^μ_α Λ^ν_β F^{αβ}. Reading off the components: E_x′ = E_x (parallel component unchanged), E_y′ = γ(E_y − vB_z), E_z′ = γ(E_z + vB_y), B_x′ = B_x, B_y′ = γ(B_y + vE_z/c²), B_z′ = γ(B_z − vE_y/c²). A purely electric field in one frame (e.g. the Coulomb field of a charge at rest) acquires a magnetic component in a frame where the charge is moving — magnetism is a relativistic effect of electricity.

**Application.** Two Lorentz scalars are built from F^{μν}: F^{μν} F_{μν} = 2(B² − E²/c²) and ε_{μνρσ} F^{μν} F^{ρσ} ∝ E · B. These are invariant under all Lorentz transformations and appear in the electromagnetic Lagrangian density L_EM = −(1/4μ₀) F^{μν} F_{μν}, which quantised gives QED (Phase 8).

## 2. Maxwell's Equations in Covariant Form

**Definition.** The full set of Maxwell's equations compresses into two covariant equations. The **inhomogeneous equations** (Gauss electric + Ampère–Maxwell) become:

∂_μ F^{μν} = μ₀ J^ν,

where J^ν = (cρ, J) is the **four-current** and ∂_μ = (∂_t/c, ∇). The **homogeneous equations** (Gauss magnetic + Faraday), which follow automatically from F^{μν} = ∂^μ A^ν − ∂^ν A^μ, are:

∂_μ F̃^{μν} = 0,   where F̃^{μν} = ½ ε^{μνρσ} F_{ρσ} is the dual tensor.

Charge conservation ∂_μ J^μ = 0 follows from the antisymmetry of F^{μν}: ∂_ν ∂_μ F^{μν} = 0 automatically. In the Lorenz gauge ∂_μ A^μ = 0, the inhomogeneous Maxwell equation becomes □² A^ν = μ₀ J^ν.

**Demonstration.** In a region with J^ν = 0, the equation ∂_μ F^{μν} = 0 with Lorenz gauge gives □²A^ν = 0 — the wave equation for each component of the four-potential. The solution A^ν ∝ ε^ν e^{ik_μ x^μ} with k^μ k_μ = 0 (null four-vector) represents a photon with polarisation four-vector ε^μ. The condition k · ε = 0 (from the Lorenz gauge) removes one polarisation degree of freedom; a further gauge freedom removes a second, leaving the two physical transverse polarisations of Module 1.11.

**Application.** Covariant electromagnetism is the prototype of a **relativistic gauge field theory**. The pattern — an antisymmetric field tensor F^{μν} derived from a gauge potential A^μ, with field equations ∂_μ F^{μν} = J^ν — is the template for: QED (replace U(1) gauge group, add quantum fields, Phase 8.2); the Yang–Mills theories of the weak and strong force (replace U(1) with SU(2) and SU(3), Phase 8.1); and canonical field quantisation (Module 6.5). The electromagnetic field tensor Fμν and its action −¼ F^{μν} F_{μν} are the starting point that the entire Standard Model generalises.

---

**Self-test (blank page)**

1. Write down the four-potential A^μ and the field tensor F^{μν} = ∂^μ A^ν − ∂^ν A^μ. Show how E and B are encoded in the components of F^{μν}.
2. Apply the Lorentz transformation of F^{μν} to find E′ and B′ for a charge q at rest in frame S. Verify that in frame S′ (moving at velocity v relative to S), the transformed B′ matches the Biot–Savart result for a moving charge.
3. Write Maxwell's inhomogeneous equations in covariant form ∂_μ F^{μν} = μ₀ J^ν and expand the ν = 0 and ν = 1 components explicitly to recover the familiar 3D Maxwell equations.
4. What are the two independent Lorentz scalars constructed from F^{μν}? What are their physical meanings, and why must they be invariant?

---

← Previous: [Module 1.14 — Relativistic Dynamics & E = mc²](./module-1.14-relativistic-dynamics-energy-momentum.md) · [Phase 1 index](./README.md) · Next: [Module 1.16 — Mechanical Waves & Acoustics](./module-1.16-mechanical-waves-acoustics.md) →

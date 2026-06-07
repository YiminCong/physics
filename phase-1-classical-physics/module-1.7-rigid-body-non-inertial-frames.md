# Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Rigid-Body Rotation and Euler's Equations

**Definition.** A **rigid body** is an extended object with fixed inter-particle distances. Its configuration requires six parameters: three for the centre-of-mass position and three for orientation (e.g., Euler angles — natural generalised coordinates in the sense of Module 1.3). The rotational kinetic energy is T_rot = ½ ω · I · ω, where ω is the angular velocity vector and **I** is the **moment of inertia tensor**, with components I_{ij} = Σ_α m_α (|r_α|²δ_{ij} − r_{αi}r_{αj}). In the **principal-axis frame**, I is diagonal with eigenvalues I₁, I₂, I₃. Angular momentum is L = I · ω; note L and ω are generally not parallel unless ω is along a principal axis.

The torque equation in the body frame (rotating with angular velocity ω) yields **Euler's equations**:

I₁ ω̇₁ − (I₂ − I₃) ω₂ ω₃ = τ₁   (and cyclic permutations).

**Demonstration.** For a torque-free symmetric top (I₁ = I₂ ≠ I₃, τ = 0), Euler's equations give uniform precession of ω about the symmetry axis with **body-frame frequency** Ω = ω₃(I₃ − I₁)/I₁. In the lab frame the angular momentum L is fixed, and the body precesses around it — the physics of a wobbling football or the Earth's Chandler wobble.

**Application.** The moment of inertia tensor is a rank-2 symmetric tensor (Module 0.6) diagonalised by the same eigenvalue problem as coupled oscillators (Module 1.6). Gyroscopes and precession underpin navigation instruments, NMR pulse sequences, and the stability analysis of rotating spacecraft.

## 2. Non-Inertial Frames: Centrifugal and Coriolis Forces

**Definition.** In a frame rotating with angular velocity Ω relative to an inertial frame, Newton's second law acquires fictitious (pseudo) forces. For a particle of mass m at position r with velocity v_rot in the rotating frame:

m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r) − m Ω̇ × r.

The three extra terms are: **Coriolis force** (−2m Ω × v_rot), **centrifugal force** (−m Ω × (Ω × r) = mω²r_⊥ outward), and an angular-acceleration term (usually zero for constant Ω). An accelerating (non-rotating) frame introduces a uniform fictitious force −m a_frame (the "g-force" felt in a lift).

**Demonstration.** On Earth's surface (Ω ≈ 7.3 × 10⁻⁵ rad/s), the Coriolis force deflects a freely-falling object eastward and causes large-scale atmospheric circulation to be clockwise in the Northern Hemisphere (low-pressure cyclones). The Foucault pendulum rotates its plane of oscillation with period T_F = 24 h / sin λ at latitude λ, directly demonstrating Earth's rotation.

**Application.** Non-inertial-frame analysis is essential in geophysics (weather patterns, ocean currents), aerospace (guidance systems), and classical chaos (the restricted three-body problem in the rotating frame). The mathematical structure — transforming derivatives between frames — is the precursor to the covariant derivative in general relativity (Phase 7).

---

**Self-test (blank page)**

1. Define the moment of inertia tensor I_{ij}. For a uniform solid sphere of mass m and radius R, what are the principal moments?
2. Write Euler's equations for a torque-free rigid body. Explain qualitatively why a rotation about the intermediate principal axis is unstable (the "tennis racket theorem").
3. Derive the expression for the Coriolis force on a particle moving with velocity v in a frame rotating at angular velocity Ω. In which direction does it deflect a horizontally-moving object in the Northern Hemisphere?
4. A Foucault pendulum at latitude 45°N completes one full precession cycle in how many hours? Show your reasoning.

---

← Previous: [Module 1.6 — Small Oscillations & Coupled Oscillators](./module-1.6-small-oscillations-coupled-oscillators.md) · [Phase 1 index](./README.md) · Next: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) →

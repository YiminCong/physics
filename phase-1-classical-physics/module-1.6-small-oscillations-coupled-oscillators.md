# Module 1.6 — Small Oscillations & Coupled Oscillators ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Simple, Damped, and Driven Harmonic Motion

**Definition.** A system displaced slightly from a stable equilibrium experiences a restoring force linear in the displacement. Writing V(x) ≈ V(0) + ½V″(0)x², Newton's second law gives ẍ + ω₀²x = 0 with ω₀ = √(V″/m) — the **simple harmonic oscillator** (SHO). Adding a damping force −bẋ and a periodic drive F₀ cos(ωt) yields the **driven damped oscillator**:

m ẍ + b ẋ + kx = F₀ cos(ωt).

Define the damping ratio γ = b/2m and quality factor Q = ω₀/2γ. The steady-state amplitude is A(ω) = (F₀/m) / √((ω₀² − ω²)² + 4γ²ω²), which peaks near ω ≈ ω₀ — **resonance**. The width of the resonance peak is Δω ≈ 2γ = ω₀/Q; high Q means sharp resonance and slow energy decay.

**Demonstration.** At exact resonance (ω = ω₀, underdamped), the amplitude grows as A = F₀t / (2mγ) if γ → 0, revealing secular growth — the energy pumped in per cycle exactly equals the work done against damping at the peak. The phase of the response shifts by π across the resonance: the oscillator lags the drive by 90° exactly at ω₀.

**Application.** Resonance is universal: mechanical bridges (Tacoma Narrows), electrical LC circuits, nuclear magnetic resonance, and atomic spectral lines all exploit or must guard against it. The SHO is the universal local approximation to any potential near a minimum — hence "every physicist's best friend."

## 2. Normal Modes of Coupled Oscillators

**Definition.** For a system of n coupled oscillators with coordinates x_i, the equations of motion take matrix form M ẍ = −K x, where M is the mass matrix and K is the stiffness matrix (both symmetric, M positive definite). Seeking solutions of the form x(t) = A e^{iωt} converts this to the **generalised eigenvalue problem**:

K A = ω² M A.

The n solutions (ω_r², A_r) give n **normal modes**: collective motions in which every part oscillates at the same frequency ω_r. Any general motion is a superposition of normal modes.

**Demonstration.** Two equal masses m connected by springs k to fixed walls and coupled by spring κ. The eigenvalue problem yields two normal modes: (1) symmetric (both masses move together), ω₁² = k/m; (2) antisymmetric (masses move oppositely), ω₂² = (k + 2κ)/m. The general solution is a superposition; beats appear when the initial conditions excite both modes.

**Application.** A crystal lattice is a chain of coupled oscillators — taking the continuum limit gives phonon dispersion relations (Module 4.3). Quantising these collective modes yields **phonons**, the quanta of lattice vibration. The quantum harmonic oscillator (Module 3.2) is the single-mode version of this; second quantisation (Module 3.12) systematises the many-mode generalisation. The eigenvalue structure here is a direct application of linear algebra (Module 0.2).

---

**Self-test (blank page)**

1. A mass m on a spring k is driven at frequency ω. Write the steady-state solution and find the frequency at which the amplitude is maximum (to leading order in γ).
2. Define the quality factor Q and explain what it tells you physically about the sharpness of resonance and the rate of energy decay.
3. Two equal masses coupled by three identical springs (in the symmetric configuration) have normal mode frequencies ω₁ and ω₂. Derive them and sketch the normal-mode motions.
4. How does the normal-mode problem for n coupled oscillators map onto an eigenvalue problem? What plays the role of the matrix to be diagonalised?

---

← Previous: [Module 1.5 — Central-Force Problem & Kepler](./module-1.5-central-force-kepler.md) · [Phase 1 index](./README.md) · Next: [Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames](./module-1.7-rigid-body-non-inertial-frames.md) →

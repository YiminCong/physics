# Module 1.11 — Electromagnetic Waves & Radiation

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Wave Equation and Plane Waves

**Definition.** In free space (ρ = 0, J = 0) Maxwell's equations yield the **wave equation** for each component of E and B:

∇²E = μ₀ε₀ ∂²E/∂t²,   ∇²B = μ₀ε₀ ∂²B/∂t².

The **speed of light** is c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s. A **plane wave** propagating in direction k̂ takes the form E = E₀ e^{i(k·r − ωt)}, B = B₀ e^{i(k·r − ωt)}, with the dispersion relation ω = c|k|. From the Maxwell curl equations: (i) k · E₀ = 0 and k · B₀ = 0 (E, B transverse to propagation), (ii) B₀ = (k̂ × E₀)/c (E and B mutually perpendicular), (iii) |E₀| = c|B₀|. **Polarisation** refers to the direction of E; for circular polarisation, E₀ is a complex vector with equal-amplitude perpendicular components differing by π/2 in phase.

**Demonstration.** A linearly polarised wave in vacuum: E = E₀ cos(kz − ωt) x̂, B = (E₀/c) cos(kz − ωt) ŷ. The **Poynting vector** S = (1/μ₀) E × B = (E₀²/μ₀c) cos²(kz − ωt) ẑ gives the energy flux (W/m²). Time-averaging gives ⟨S⟩ = E₀²/(2μ₀c) = ½ε₀c E₀² — the **intensity** of the wave.

**Application.** The electromagnetic spectrum from radio waves to gamma rays is all the same physics at different frequencies. The wave equation reappears in acoustics, quantum mechanics (the free-particle Schrödinger equation in the high-frequency limit), and field theory. The Poynting vector generalises to a stress-energy tensor in both relativity (Phase 7) and field theory (Phase 6).

## 2. Radiation from Accelerating Charges

**Definition.** An accelerating point charge radiates electromagnetic energy. The total power radiated by a charge q with acceleration a is given by the **Larmor formula**:

P = q² a² / (6πε₀ c³)   (SI units).

For a charge undergoing simple harmonic oscillation (a **Hertzian dipole**), P ∝ ω⁴ |p|², where p is the dipole moment amplitude. The far-field radiation pattern goes as sin²θ (maximum perpendicular to the oscillation axis, zero along it), with the electric field E_rad ∝ (a/rc²) sin θ falling off as 1/r.

**Demonstration.** A dipole antenna of length d oscillating at angular frequency ω has time-averaged radiated power P ∝ (d/λ)² c ε₀ E₀². The ω⁴ frequency dependence explains why the sky is blue: Rayleigh scattering of sunlight by atmospheric molecules scales as ω⁴, scattering blue (high-ω) light far more efficiently than red.

**Application.** Larmor radiation imposes a fundamental limit on classical atomic models — an orbiting electron would spiral inward in ~10⁻¹¹ s, the crisis that quantum mechanics (Module 3.1) resolves. Synchrotron radiation from relativistic charged particles (the relativistic generalisation, where P = q²c γ⁴ a⊥²/(6πε₀(m c²)²)) powers modern X-ray light sources. Quantising the radiation field yields photons and QED (Phase 6, Phase 8).

---

**Self-test (blank page)**

1. Starting from Maxwell's equations in free space, derive the wave equation for E. Identify the speed of the wave.
2. For a plane EM wave, show that E and B are perpendicular to each other and to the direction of propagation. What is the ratio |E|/|B|?
3. Define the Poynting vector and explain its physical meaning. Compute the time-averaged intensity of a plane wave with peak electric field amplitude E₀.
4. State the Larmor formula. Use it to explain why classical Bohr orbits are unstable, and what physics is missing.

---

← Previous: [Module 1.10 — Electrodynamics & Maxwell's Equations](./module-1.10-electrodynamics-maxwell-equations.md) · [Phase 1 index](./README.md) · Next: [Module 1.12 — Optics & Interference](./module-1.12-optics-interference.md) →

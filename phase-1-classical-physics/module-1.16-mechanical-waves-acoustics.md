# Module 1.16 — Mechanical Waves & Acoustics

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Wave Equation

**Definition.** A **mechanical wave** is a disturbance that propagates through a medium, transporting energy and momentum without net transport of matter. Small disturbances obey the **wave equation** ∂²u/∂t² = c²∂²u/∂x² (or ∂²u/∂t² = c²∇²u in 3D), a PDE solved by separation of variables (Module 0.3). Its general 1D solution is **d'Alembert's form** u(x,t) = f(x − ct) + g(x + ct): arbitrary right- and left-moving profiles at speed c.

**Demonstration.** A string of tension T and linear density μ supports transverse waves with **c = √(T/μ)**. A continuous chain of masses and springs (the continuum limit of the coupled oscillators of Module 1.6) reproduces exactly this equation — the wave is the collective normal mode of infinitely many oscillators. Harmonic solutions u = A cos(kx − ωt) give the **dispersion relation** ω = ck, with wavelength λ = 2π/k and frequency f = ω/2π.

**Application.** Any superposition of normal modes is itself a solution; decomposing a disturbance into its harmonic components is **Fourier analysis** (Module 0.5). Standing waves on a bounded string quantize into harmonics fₙ = n c/2L — the same boundary-value logic that quantizes energy in the infinite square well (Module 3.2).

## 2. Sound, Energy & Wave Phenomena

**Definition.** **Sound** is a longitudinal pressure wave in a fluid, with speed **c = √(B/ρ)** (B = bulk modulus, ρ = density). Waves carry energy flux (intensity ∝ amplitude²) and exhibit **reflection, refraction, interference, and diffraction**; a moving source or observer produces the **Doppler shift** f′ = f (c ± v_obs)/(c ∓ v_src).

**Demonstration.** Two waves of nearby frequency superpose into **beats** at frequency |f₁ − f₂|; a wave meeting a boundary partially reflects with a phase flip at a fixed end. Group velocity v_g = dω/dk governs how a wave *packet* (and its energy) actually travels when the medium is dispersive.

**Application.** Acoustics underlies musical instruments, ultrasound imaging, sonar, and seismology. The wave equation and its dispersion/group-velocity machinery carry over directly to electromagnetic waves (Module 1.11), lattice waves and phonons (Module 4.3), and the matter waves of quantum mechanics (Module 3.1).

---

**Self-test (blank page)**

1. Derive c = √(T/μ) for a string from Newton's second law applied to a small element.
2. Write d'Alembert's solution and use it to describe a pulse reflecting off a fixed end.
3. A 1 m string fixed at both ends has c = 200 m/s. Find its three lowest standing-wave frequencies.
4. Explain the difference between phase velocity and group velocity, and when they differ.

---

← Previous: [Module 1.15 — Covariant Electromagnetism](./module-1.15-covariant-electromagnetism.md) · [Phase 1 index](./README.md) · Next: [Module 1.17 — Fluid Mechanics](./module-1.17-fluid-mechanics.md) →

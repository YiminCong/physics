# Module 1.12 — Optics & Interference

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Geometric Optics and Huygens' Principle

**Definition.** **Geometric (ray) optics** applies when the wavelength λ is much smaller than all relevant length scales. Light travels in straight rays; the fundamental laws are: (i) **reflection**: angle of incidence equals angle of reflection; (ii) **Snell's law of refraction**: n₁ sin θ₁ = n₂ sin θ₂, where n = c/v is the refractive index. **Total internal reflection** occurs for θ₁ > θ_c = arcsin(n₂/n₁) when n₁ > n₂. Thin-lens optics gives the **lens equation** 1/f = 1/d_o + 1/d_i and magnification M = −d_i/d_o.

**Huygens' principle** states that every point on a wavefront acts as a secondary source of spherical wavelets; the new wavefront is the envelope of these wavelets. This semi-geometrical picture correctly reproduces reflection and refraction, and provides the seed for the full wave theory of diffraction.

**Demonstration.** Snell's law from Huygens: a plane wave hits an interface at angle θ₁. The wavelet from the leading edge of the wavefront travels distance v₂ t in medium 2 while the trailing edge travels v₁ t in medium 1. Geometry gives sin θ₁/v₁ = sin θ₂/v₂, i.e. n₁ sin θ₁ = n₂ sin θ₂.

**Application.** Ray optics designs lenses, mirrors, optical fibres, and telescopes. Its breakdown — when λ is not negligible — signals the onset of wave phenomena treated in Section 2.

## 2. Interference and Diffraction

**Definition.** **Interference** arises when two or more coherent waves superpose. For two slits separated by distance d, illuminated by wavelength λ at normal incidence, the path difference Δ = d sin θ. **Constructive interference** (bright fringes) at d sin θ = mλ; **destructive interference** at d sin θ = (m + ½)λ. The **single-slit diffraction** intensity envelope is I(θ) = I₀ sinc²(πa sin θ / λ), where a is the slit width. **Diffraction gratings** with N slits produce sharp principal maxima at d sin θ = mλ with resolving power R = mN.

**Demonstration.** Double-slit experiment (Young, 1801): two slits, separation d = 0.1 mm, λ = 500 nm, screen at L = 1 m. Fringe spacing Δy = λL/d = 5 mm — directly measurable with a ruler. The same experiment performed one photon at a time still builds up the interference pattern, a key demonstration of wave–particle duality (Phase 3).

**Application.** Diffraction is fundamentally a **Fourier phenomenon** (Module 0.5): the far-field (Fraunhofer) diffraction pattern of an aperture function f(x) is its Fourier transform F̃(k_x). The diffraction grating is a Fourier analyser of wavelengths; X-ray diffraction from crystals (Bragg's law: 2d sin θ = mλ) is Fourier analysis of the lattice, the basis of crystallography and protein structure determination. Interference also underlies interferometric sensors (LIGO gravitational wave detection) with sensitivity far below λ.

---

**Self-test (blank page)**

1. State Snell's law and derive it using Huygens' principle. What is the critical angle for glass (n = 1.5) in air?
2. In a double-slit experiment with slit separation d and wavelength λ, find the angular positions of the first three bright fringes. How does fringe spacing change if d is halved?
3. Explain why single-slit diffraction produces a central maximum of width 2λ/a and progressively weaker subsidiary maxima. How is this pattern related to the Fourier transform of the aperture?
4. What is the resolving power of a diffraction grating, and what determines it? How does this relate to the Rayleigh criterion for angular resolution?

---

← Previous: [Module 1.11 — Electromagnetic Waves & Radiation](./module-1.11-em-waves-radiation.md) · [Phase 1 index](./README.md) · Next: [Module 1.13 — Special Relativity — Kinematics](./module-1.13-special-relativity-kinematics.md) →

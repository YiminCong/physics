# Module 7.3 — Geodesics & the Motion of Particles

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Geodesic Equation

**Definition.** In GR, freely falling particles (no non-gravitational forces) move along *geodesics* of the spacetime metric: curves that extremize the proper time (equivalently, parallel-transport their own tangent vector). Applying the variational principle (Module 1.3) to the action S = −mc ∫dτ = −mc ∫√(−g_{μν} dxμ dxν) yields the *geodesic equation*:

d²xμ/dτ² + Γμ νρ (dxν/dτ)(dxρ/dτ) = 0

Here τ is proper time and Γμ νρ are the Christoffel symbols of the metric (Module 7.2). For massless particles (photons), τ is replaced by an affine parameter λ and ds² = 0. The geodesic equation is the GR replacement for Newton's second law F = ma under gravity.

**Demonstration.** *Newtonian limit*: take g_{μν} ≈ ημν + hμν with |hμν| ≪ 1, slow motion dxi/dτ ≪ c, and a static field h₀₀ = −2φ/c² (φ Newtonian potential). The time-time Christoffel symbol gives Γi ₀₀ ≈ −(1/2)∂i h₀₀ = ∂i φ/c². The geodesic spatial components reduce to

d²xi/dt² = −∂i φ

which is precisely Newton's law of gravity (Module 1.1). The geometry reproduces Newtonian gravity in the appropriate limit.

*Gravitational time dilation and redshift*: for a static metric with g₀₀ = −(1 + 2φ/c²), proper time and coordinate time are related by dτ = √(−g₀₀) dt ≈ (1 + φ/c²)dt. A clock at lower potential φ₁ < φ₂ runs slow: dτ₁/dτ₂ ≈ 1 + (φ₁ − φ₂)/c² < 1. Light emitted at frequency ν₁ near a massive body is received at frequency ν₂ = ν₁(1 + Δφ/c²) — *gravitational redshift*, z ≈ Δφ/c².

**Application.**

- *GPS corrections*: GPS satellites orbit at altitude ≈ 20 200 km where φ is less negative. Gravitational time dilation causes satellite clocks to run fast by ≈ +45.9 μs/day; SR velocity time dilation (Module 1.14) causes them to run slow by ≈ −7.2 μs/day; net correction ≈ +38.7 μs/day. Without this, GPS positions would drift by ≈ 10 km/day.
- *Perihelion precession of Mercury*: the Schwarzschild geodesic for a planet gives an orbit that is not a closed ellipse (Module 1.5) but precesses by Δφ = 6πGM/(a(1−e²)c²) per orbit. For Mercury this is ≈ 43 arcsec/century — the famous anomaly unexplained by Newtonian gravity, confirmed precisely by GR.

---

**Self-test (blank page)**

1. Derive the geodesic equation from the variational principle δ∫dτ = 0. At what step do the Christoffel symbols appear?
2. Show that in the Newtonian limit, the geodesic equation reduces to d²xi/dt² = −∇φ. What approximations are required?
3. A photon climbs from the Sun's surface (φ_surface ≈ −1.91 × 10¹¹ J/kg) to infinity. Estimate its gravitational redshift z.

---

← Previous: [Module 7.2 — Tensors, the Metric & Curvature](./module-7.2-tensors-metric-and-curvature.md) · [Phase 7 index](./README.md) · Next: [Module 7.4 — Einstein's Field Equations](./module-7.4-einsteins-field-equations.md) →

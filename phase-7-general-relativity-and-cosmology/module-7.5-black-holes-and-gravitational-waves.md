# Module 7.5 — Black Holes & Gravitational Waves ⭐

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Black Holes: Schwarzschild, Event Horizons, and Kerr

**Definition.** The simplest exact solution to the vacuum Einstein equations (R_{μν} = 0, Module 7.4) for a static, spherically symmetric spacetime is the *Schwarzschild metric* (1916):

ds² = −(1 − r_s/r) c²dt² + (1 − r_s/r)⁻¹ dr² + r² dΩ²

where dΩ² = dθ² + sin²θ dφ² is the metric on the unit 2-sphere, and the *Schwarzschild radius* is r_s = 2GM/c². At r = r_s, the coefficient g₀₀ vanishes and g_{rr} diverges — but this is a *coordinate singularity*: in Kruskal–Szekeres coordinates the metric is smooth there. At r = 0 the curvature invariant Rμνρσ R^{μνρσ} diverges — a genuine *physical singularity* signalling the breakdown of classical GR.

The surface r = r_s is the *event horizon*: a null hypersurface from which no causal signal (including light) can escape to r → ∞. An observer freely falling through the horizon notices nothing locally (by the equivalence principle; Module 7.1), but a distant observer sees the infalling observer's signals redshift and freeze at the horizon.

For a rotating mass (angular momentum J), the unique vacuum solution is the *Kerr metric* (1963), characterised by M and the spin parameter a = J/(Mc). It introduces an *ergosphere* — a region outside the horizon where spacetime is dragged so severely that no observer can remain stationary — enabling the Penrose process to extract rotational energy.

**Demonstration.** The Schwarzschild radius for the Sun: r_s = 2GM_☉/c² ≈ 2 × (6.67 × 10⁻¹¹)(2 × 10³⁰)/(9 × 10¹⁶) ≈ 2.95 km. The Sun would have to be compressed to under 3 km radius to form a black hole. For a stellar-mass black hole (M ≈ 10 M_☉), r_s ≈ 30 km; for the supermassive black hole at the centre of M87 (M ≈ 6.5 × 10⁹ M_☉), r_s ≈ 19 billion km ≈ 19 AU.

The geodesic equation (Module 7.3) applied to the Schwarzschild metric yields the innermost stable circular orbit (ISCO) at r = 3r_s = 6GM/c² — inside this radius, no stable circular orbit exists and matter spirals inward. Photon orbits are at r = (3/2)r_s (the photon sphere). These results follow purely from the metric; no additional physics is needed.

**Application.** Astrophysical black holes are observed across a wide mass range:
- *Stellar-mass* (5–100 M_☉): endpoints of massive-star collapse, detected in X-ray binaries and via gravitational waves.
- *Supermassive* (10⁶–10¹⁰ M_☉): reside in galactic nuclei; directly imaged by the Event Horizon Telescope (M87*, 2019; Sgr A*, 2022).
- Hawking radiation (semiclassical GR, not covered here) predicts black holes slowly evaporate with temperature T_H = ℏc³/(8πGMk_B), relevant only for primordial or microscopic black holes.

---

## 2. Linearized Gravity and Gravitational Waves

**Definition.** Far from sources or for weak fields, write g_{μν} = ημν + hμν with |hμν| ≪ 1. Expanding the EFE to first order in hμν and choosing *Lorenz gauge* (∂^μ h̄_{μν} = 0, where h̄_{μν} = hμν − ½ ημν h is the trace-reversed perturbation) gives:

□ h̄_{μν} = −(16πG/c⁴) Tμν

where □ = −(1/c²)∂²_t + ∇² is the flat-space d'Alembertian. In vacuum (Tμν = 0) this is a wave equation: gravitational perturbations propagate at speed c. These are *gravitational waves* (GWs).

In transverse-traceless (TT) gauge (the radiation gauge), only the spatial transverse components survive. A wave propagating in the z-direction has two independent polarizations:

h_{μν}^{TT} = [ h₊ (x̂⊗x̂ − ŷ⊗ŷ) + h_× (x̂⊗ŷ + ŷ⊗x̂) ] cos(kz − ωt)

The + polarization stretches space in x and squeezes in y (and vice versa); the × polarization does the same at 45°. The strain h = ΔL/L measures the fractional change in proper distance between free-falling test masses — the observable quantity.

**Demonstration.** The *quadrupole formula* gives the leading GW power emitted by a source with time-varying quadrupole moment Q_{ij}:

P = (G/5c⁵) ⟨ d³Q_{ij}/dt³ · d³Q^{ij}/dt³ ⟩

For two equal masses M in circular orbit of separation 2r and orbital frequency Ω: P = (32G⁴M⁵)/(5c⁵r⁵). As energy is radiated the orbit decays — the *inspiral*. For the Hulse–Taylor binary pulsar (1974), this orbital decay matched the quadrupole prediction to ≈ 0.1%, providing indirect evidence for GWs 40 years before direct detection.

LIGO's first detection (GW150914, September 2015) observed h ∼ 10⁻²¹ from a binary black hole merger (≈ 36 M_☉ + 29 M_☉ at ≈ 410 Mpc). The strain implied ΔL ∼ 10⁻¹⁸ m — a thousandth of a proton radius — over a 4 km baseline, detected by laser interferometry.

**Application.**
- *Multi-messenger astronomy*: GW170817 (2017) detected GWs from a binary neutron star merger simultaneously with a short gamma-ray burst and optical/X-ray/radio afterglow — the first multi-messenger GW event. It constrained the neutron star equation of state and the Hubble constant.
- *Parameter estimation*: GW signals encode the chirp mass M_c = (M₁M₂)^{3/5}/(M₁+M₂)^{1/5}, luminosity distance, and spin parameters — allowing population studies of compact objects.
- *Future detectors*: LISA (space-based, launch ~2035) will access millihertz GWs from supermassive black hole mergers and galactic binaries; Einstein Telescope will improve sensitivity by an order of magnitude.

---

**Self-test (blank page)**

1. Derive the Schwarzschild radius r_s = 2GM/c² from dimensional analysis and the condition that the escape velocity equals c. Why is r_s = r_s(M) a coordinate singularity rather than a physical one?
2. A gravitational wave passes Earth with strain h = 5 × 10⁻²². What is the fractional change in distance between two free-falling mirrors separated by L = 4 km? How does LIGO's Fabry–Pérot cavity improve sensitivity?
3. State the two GW polarizations in TT gauge. How does a ring of free-falling test particles respond to each polarization over one GW cycle?

---

← Previous: [Module 7.4 — Einstein's Field Equations](./module-7.4-einsteins-field-equations.md) · [Phase 7 index](./README.md) · Next: [Module 7.6 — Cosmology](./module-7.6-cosmology.md) →

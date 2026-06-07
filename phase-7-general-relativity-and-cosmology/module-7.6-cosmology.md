# Module 7.6 — Cosmology

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The FLRW Metric and the Expanding Universe

**Definition.** The *cosmological principle* asserts that the universe is, on the largest scales, spatially homogeneous (no preferred location) and isotropic (no preferred direction). The unique metric consistent with these symmetries is the *Friedmann–Lemaître–Robertson–Walker (FLRW) metric*:

ds² = −c²dt² + a(t)² [ dr²/(1 − kr²) + r² dΩ² ]

where a(t) is the dimensionless *scale factor* (normalized to a(t₀) = 1 today), t is cosmic time, and k = +1, 0, −1 for a spatially closed, flat, or open universe respectively. Physical distances scale as d(t) = a(t) d_comoving. The recession velocity of a comoving object is v = ȧ d = H(t) d, where H(t) = ȧ/a is the *Hubble parameter*; today H₀ ≈ 67–73 km s⁻¹ Mpc⁻¹ (the "Hubble tension").

The *cosmological redshift* of light emitted at scale factor a_e and received at a_0 = 1 is z = 1/a_e − 1; it is a consequence of the expansion stretching photon wavelengths, not a Doppler shift in the usual sense.

**Demonstration.** Substituting the FLRW metric and a perfect-fluid Tμν (ρ, p) into the Einstein field equations (Module 7.4) yields the *Friedmann equations*:

(ȧ/a)² = (8πG/3)ρ − kc²/a² + Λc²/3

ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3

The first equation relates the expansion rate to the energy density, curvature, and cosmological constant. The second governs acceleration: ordinary matter and radiation (ρ + 3p/c² > 0) cause deceleration; Λ causes acceleration (effective p_Λ = −ρ_Λ c²). The *continuity equation* ρ̇ + 3H(ρ + p/c²) = 0 follows from ∇μ Tμν = 0.

Key solutions (k = 0, Λ = 0):
- *Matter dominated* (p = 0): a(t) ∝ t^{2/3}, ρ_m ∝ a⁻³
- *Radiation dominated* (p = ρc²/3): a(t) ∝ t^{1/2}, ρ_r ∝ a⁻⁴
- *Λ dominated* (ρ_Λ = Λc²/8πG = const): a(t) ∝ e^{Ht} (de Sitter expansion)

**Application.** The observed universe began in an extremely hot, dense state — the *Big Bang* — approximately t₀ ≈ 13.8 Gyr ago. The sequence of epochs: Planck era → inflation → radiation domination (quarks, leptons, nucleosynthesis) → matter domination (structure formation) → dark-energy domination (present accelerated expansion). The *cosmic microwave background* (CMB), emitted at recombination (z ≈ 1100, t ≈ 380 000 yr), is the earliest electromagnetic snapshot of the universe; its near-perfect blackbody spectrum at T₀ ≈ 2.725 K and tiny anisotropies (ΔT/T ∼ 10⁻⁵) encode the seeds of all large-scale structure.

---

## 2. Dark Matter, Dark Energy, and the Fate of the Universe

**Definition.** The energy budget of the universe (from CMB + baryon acoustic oscillations + supernovae) is:
- *Baryonic matter*: Ω_b ≈ 0.049 (atoms, stars, gas)
- *Cold dark matter* (CDM): Ω_c ≈ 0.265 — non-luminous, non-baryonic, gravitationally clustering matter inferred from galaxy rotation curves, gravitational lensing, and structure formation. Its particle identity is unknown (WIMPs, axions, and sterile neutrinos are leading candidates; see Module 8.6).
- *Dark energy* (Λ): Ω_Λ ≈ 0.685 — the energy of the quantum vacuum or a dynamical field (quintessence), driving the accelerated expansion discovered via Type Ia supernovae in 1998. Geometrically it enters as the cosmological constant Λ in the EFE (Module 7.4).

The total Ω = Ω_b + Ω_c + Ω_Λ ≈ 1.000, implying k = 0: a spatially flat universe.

**Demonstration.** Galaxy rotation curves: Newtonian gravity (Module 1.5) predicts orbital velocity v(r) = √(GM(r)/r) falling as r⁻¹/² beyond the visible disk. Observations show v(r) ≈ const ("flat rotation curves") to large r, implying M(r) ∝ r — an unseen *dark matter halo* extending far beyond the luminous galaxy. The required mass-to-light ratio is 5–10× the baryonic value.

The Friedmann equation with Ω_m + Ω_Λ = 1 predicts deceleration (ä < 0) for Ω_Λ < Ω_m/2, and acceleration (ä > 0) otherwise. The transition to acceleration occurred at z ≈ 0.4 (about 5 Gyr ago). Future: continued exponential expansion; galaxies beyond the Local Group will eventually redshift out of causal contact (cosmological event horizon).

**Application.**
- *Big Bang nucleosynthesis* (BBN, t ≈ 1–200 s): the baryon-to-photon ratio η fixes the primordial abundances of ¹H, ²H, ³He, ⁴He, ⁷Li. Agreement between BBN predictions and observations spanning nine orders of magnitude in abundance is one of the strongest tests of the hot Big Bang model.
- *Structure formation*: quantum fluctuations during inflation are stretched to macroscopic scales, seeding the CMB anisotropies that gravitationally collapse (with CDM providing the potential wells) into the cosmic web of filaments, voids, clusters, and galaxies.
- *Connection to particle physics*: the early universe at T ≳ 100 GeV probed physics at the electroweak scale and beyond (Module 8.6). Dark matter candidates, baryogenesis, and leptogenesis are active frontiers linking cosmology and the Standard Model.

---

**Self-test (blank page)**

1. Derive the first Friedmann equation from the 00-component of the EFE applied to the FLRW metric. Identify the contributions from curvature, matter, and Λ.
2. Show that the continuity equation ρ̇ + 3H(ρ + p/c²) = 0 gives ρ_m ∝ a⁻³ for dust and ρ_r ∝ a⁻⁴ for radiation. Why does radiation dilute faster?
3. Explain why a cosmological constant Λ > 0 acts as a fluid with equation of state w = p/(ρc²) = −1. How does this cause accelerated expansion?

---

← Previous: [Module 7.5 — Black Holes & Gravitational Waves](./module-7.5-black-holes-and-gravitational-waves.md) · [Phase 7 index](./README.md)

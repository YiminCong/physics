# Module 1.10 — Electrodynamics & Maxwell's Equations ⭐

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Faraday's Law, Displacement Current, and the Full Maxwell Set

**Definition.** Two additional laws complete electromagnetism from the static picture. **Faraday's law of induction**: a time-varying magnetic flux through a loop induces an EMF, or in differential form:

∇ × E = −∂B/∂t.

This breaks the electrostatic condition ∇ × E = 0. Maxwell observed that Ampère's static law ∇ × B = μ₀ J is inconsistent with charge conservation (∇ · J = −∂ρ/∂t ≠ 0 in general) and added the **displacement current** ε₀ ∂E/∂t. The complete **Maxwell's equations** in differential form are:

∇ · E = ρ / ε₀             (Gauss — electric),
∇ · B = 0                  (Gauss — magnetic, no monopoles),
∇ × E = −∂B/∂t            (Faraday),
∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t  (Ampère–Maxwell).

Charge continuity ∂ρ/∂t + ∇ · J = 0 follows automatically from the curl equations — it is not an independent law but a consistency condition.

**Demonstration.** Taking the curl of Faraday's law and substituting Ampère–Maxwell (in vacuum, ρ = J = 0):

∇ × (∇ × E) = −∂/∂t (∇ × B) = −μ₀ε₀ ∂²E/∂t².

Using the vector identity ∇ × (∇ × E) = ∇(∇ · E) − ∇²E and ∇ · E = 0, this gives the wave equation:

∇²E − μ₀ε₀ ∂²E/∂t² = 0.

An identical equation holds for B. This is derived more fully in Module 1.11.

**Application.** Maxwell's equations unify electricity, magnetism, and optics — one of the great syntheses in physics. They predict electromagnetic waves propagating at speed c = 1/√(μ₀ε₀), identified immediately with light. Written in covariant form (Module 1.15), they are manifestly Lorentz-invariant and the prototype for all relativistic gauge field theories. Their quantisation produces photons and quantum electrodynamics (Phase 6, Phase 8).

## 2. The Electromagnetic Potentials

**Definition.** From ∇ · B = 0 write B = ∇ × A. Faraday's law then gives ∇ × (E + ∂A/∂t) = 0, so E + ∂A/∂t = −∇φ, i.e.

E = −∇φ − ∂A/∂t,   B = ∇ × A.

The gauge transformations φ → φ − ∂χ/∂t, A → A + ∇χ leave E and B unchanged. The **Lorenz gauge** ∇ · A + (1/c²) ∂φ/∂t = 0 decouples the potentials into two wave equations: □²φ = −ρ/ε₀ and □²A = −μ₀ J, where □² = ∇² − (1/c²)∂²/∂t² is the d'Alembertian.

**Application.** The potentials (φ, A) unify naturally into the four-potential A^μ of special relativity (Module 1.15), making gauge invariance manifestly covariant. They enter quantum mechanics directly — the canonical momentum of a charged particle is p − qA — and are the fundamental objects of gauge field theory (Phase 8).

---

**Self-test (blank page)**

1. Write all four Maxwell equations in differential form. Identify which two are "source equations" and which two are "curl equations." Derive the continuity equation ∂ρ/∂t + ∇ · J = 0 from them.
2. Why did Maxwell add the displacement current term ε₀ ∂E/∂t to Ampère's law? Show that without it, charge conservation would be violated.
3. Show that E = −∇φ − ∂A/∂t and B = ∇ × A satisfy Faraday's law and the no-monopole condition identically.
4. In the Lorenz gauge, write the wave equations for φ and A. What is the d'Alembertian □²?

---

← Previous: [Module 1.9 — Magnetostatics](./module-1.9-magnetostatics.md) · [Phase 1 index](./README.md) · Next: [Module 1.11 — Electromagnetic Waves & Radiation](./module-1.11-em-waves-radiation.md) →

# Module 2.7 — Kinetic Theory & Transport

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Maxwell–Boltzmann Distribution & Mean Free Path

**Definition.** Kinetic theory derives the macroscopic properties of a gas from the statistics of its molecules. In equilibrium, molecular speeds follow the **Maxwell–Boltzmann distribution** f(v) ∝ v² e^{−mv²/2k_BT} (the Boltzmann factor of Module 2.4 applied to kinetic energy). The **mean free path** ℓ = 1/(√2 n σ) is the average distance between collisions (n = number density, σ = collision cross-section).

**Demonstration.** Averaging molecular momentum transfer to the walls reproduces the **ideal gas law** PV = N k_BT and identifies temperature with mean kinetic energy: ½m⟨v²⟩ = (3/2)k_BT. The rms speed is v_rms = √(3k_BT/m) — hundreds of m/s for air at room temperature.

**Application.** Kinetic theory is the microscopic justification of thermodynamics for dilute gases, and it fixes the equipartition result C_V = (3/2)Nk_B for a monatomic gas (Module 2.4).

## 2. The Boltzmann Equation & Transport Coefficients

**Definition.** Out of equilibrium, the distribution f(r,v,t) evolves by the **Boltzmann transport equation** ∂f/∂t + **v**·∇_r f + **F**/m·∇_v f = (∂f/∂t)_coll. In the **relaxation-time approximation** the collision term is −(f − f₀)/τ, which linearizes the problem and yields the **transport coefficients**.

**Demonstration.** A gradient drives a flux proportional to it: **diffusion** (Fick's law, flux ∝ −∇n), **viscosity** (momentum transport, giving the η of Navier–Stokes, Module 1.17), and **thermal conductivity** (heat flux ∝ −∇T). Each coefficient comes out ∝ n v̄ ℓ ∝ √T for a classical gas. Applied to the electron gas in a metal with a relaxation time τ, the same logic gives the **Drude conductivity** σ = ne²τ/m and Ohm's law (Module 4.1).

**Application.** Transport theory connects equilibrium statistical mechanics to the *dynamics* of real materials — electrical and thermal conductivity, diffusion, and viscosity. The Boltzmann equation remains the workhorse for electron and phonon transport in solids (Phase 4) and for plasmas, and it supplies the dissipative coefficients that the macroscopic Navier–Stokes equation (Module 1.17) takes as inputs.

---

**Self-test (blank page)**

1. Sketch the Maxwell–Boltzmann speed distribution and mark v_rms; explain how it shifts as T increases.
2. Derive PV = N k_BT by computing the momentum flux of molecules onto a wall.
3. Define the mean free path and explain how it enters the transport coefficients.
4. Starting from the relaxation-time Boltzmann equation, sketch how the Drude conductivity σ = ne²τ/m arises.

---

← Previous: [Module 2.6 — Quantum Gases & Applications](./module-2.6-quantum-gases-applications.md) · [Phase 2 index](./README.md) · Next: [Module 2.8 — Brownian Motion & the Einstein Relation](./module-2.8-brownian-motion-and-the-einstein-relation.md) →

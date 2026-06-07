# Module 2.8 — Brownian Motion & the Einstein Relation

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Brownian Motion

**Definition.** **Brownian motion** is the incessant random jittering of a microscopic particle (a pollen grain, a colloid) suspended in a fluid, caused by unbalanced collisions with the fluid's molecules. **Einstein (1905)** modelled it as a random walk and showed the **mean-square displacement grows linearly in time**: ⟨x²⟩ = 2Dt (in one dimension), where D is the **diffusion coefficient**. The particle drifts nowhere on average, but spreads diffusively.

**Demonstration.** Einstein connected this microscopic randomness to a measurable macroscopic coefficient via the **Einstein relation** D = μ k_B T, where μ is the particle's mobility (drift velocity per unit force). For a sphere of radius r in a fluid of viscosity η, Stokes' law gives μ = 1/(6πηr), so **D = k_B T / (6πηr)** (the Stokes–Einstein relation). Measuring D and η therefore yields **Avogadro's number** — exactly what **Perrin's experiments (1908)** did, giving the decisive proof that atoms are real.

## 2. Fluctuation–Dissipation

**Definition.** The Einstein relation D = μ k_B T is the first instance of the **fluctuation–dissipation theorem**: the random fluctuations of a system (diffusion D) are tied to its dissipative response (mobility/friction μ), both rooted in the same molecular collisions.

**Application.** Beyond confirming atomism, this launched the theory of **stochastic processes** — the Langevin equation, random walks, and noise. The same logic gives **Johnson–Nyquist thermal noise** in electrical circuits and underpins the transport coefficients of Module 2.7. It remains the workhorse for modelling everything from colloids and polymers to financial time series.

---

**Self-test (blank page)**

1. Write Einstein's result ⟨x²⟩ = 2Dt and contrast diffusive spreading with ballistic motion.
2. State the Einstein relation D = μ k_B T and the Stokes–Einstein form; explain how it yields Avogadro's number.
3. What does the fluctuation–dissipation theorem connect, and why are the two sides linked?

---

← Previous: [Module 2.7 — Kinetic Theory & Transport](./module-2.7-kinetic-theory-and-transport.md) · [Phase 2 index](./README.md)

# Module 6.3 — Feynman Diagrams & Perturbation Theory

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Wick's Theorem and the Diagrammatic Expansion

**Definition.** Perturbation theory for the interacting Green's function G starts from the interaction picture, expanding the S-matrix in powers of the interaction H_int. The key tool is Wick's theorem: a time-ordered product of operators in the free vacuum equals a sum over all possible pairwise contractions. A contraction of ψ(x) with ψ†(x') is precisely the free Green's function G⁰(x,x'). Wick's theorem thus converts operator algebra into combinatorics.

Each term in the expansion is labeled by a Feynman diagram: a directed line represents G⁰(k,ω), a wavy or dashed line represents the interaction vertex U(q), and the rules for reading off the algebraic value of a diagram are the Feynman rules. The diagrammatic expansion is an organized, pictorial bookkeeping for the infinite perturbative series.

**Demonstration.** Consider electrons interacting via a two-body potential U(q) (e.g., screened Coulomb). At first order, the Hartree diagram contributes a constant energy shift (tadpole: a loop closed on itself) and the Fock (exchange) diagram contributes the exchange self-energy Σ_F(k) = −Σ_q U(q) G⁰(k−q). These correct the single-particle dispersion already at first order. Crucially, the linked-cluster theorem guarantees that all disconnected (vacuum) diagrams cancel in ratios like G = ⟨T ψ ψ†⟩ / ⟨0|S|0⟩, so only connected diagrams contribute to physical quantities.

**Application.** The self-energy Σ(k,ω) collects all one-particle-irreducible (1PI) insertions — diagrams that cannot be split by cutting a single G⁰ line. The Dyson equation then resums the entire perturbative series exactly: G(k,ω) = G⁰(k,ω) + G⁰(k,ω) Σ(k,ω) G(k,ω), which solves to G(k,ω) = 1/(ω − ε_k/ℏ − Σ(k,ω)). This is the master equation linking the diagrammatic expansion to measurable quasiparticle properties (Module 6.2).

---

## 2. Screening and the Random-Phase Approximation

**Definition.** The bare Coulomb interaction U(q) = e²/ε₀q² is long-ranged and its direct use in perturbation theory gives logarithmically divergent results at every order. Screening — the rearrangement of the electron gas to reduce the effective interaction — must be summed to all orders in a class of diagrams. The random-phase approximation (RPA) sums the infinite series of bubble diagrams: one interaction line, then one interaction line with a particle-hole bubble inserted, then two bubbles, and so on.

**Demonstration.** Each bubble (polarization insertion) contributes a factor of Π⁰(q,ω) = −2i ∫ dk dε/(2π)⁴ G⁰(k+q,ω+ε)G⁰(k,ε), the Lindhard function (factor of 2 for spin). The geometric series gives the RPA-screened interaction W(q,ω) = U(q) / (1 − U(q)Π⁰(q,ω)) = U(q)/ε(q,ω) where ε(q,ω) is the dielectric function. At q → 0, ω = 0, this gives static Thomas–Fermi screening: W(q→0) ≈ e²/(ε₀(q² + k²_TF)) with k_TF the Thomas–Fermi screening wave vector, a finite-range interaction.

**Application.** The RPA is simultaneously the simplest consistent approximation for the interacting electron gas and the derivation of plasmons: poles of W(q,ω) at ε(q,ω) = 0 are collective charge oscillations. The same diagrammatic logic — identify the relevant class of diagrams, sum them, read off the physics — is the everyday currency of condensed matter and particle physics. Altland & Simons "Condensed Matter Field Theory" builds much of the second half of the book on exactly this framework.

---

## Self-test (blank page)

1. State Wick's theorem. Why does it allow operator expectation values to be expressed as sums over free Green's functions?
2. Draw and label the Hartree and Fock self-energy diagrams. Write the algebraic expression for the Fock self-energy Σ_F(k) in terms of U(q) and G⁰.
3. Write the Dyson equation G = G⁰ + G⁰ Σ G and solve it for G(k,ω). What does a large Im Σ imply for the quasiparticle?

---

← Previous: [Module 6.2 — Green's Functions & Propagators](./module-6.2-greens-functions.md) · [Phase 6 index](./README.md) · Next: [Module 6.4 — Path Integrals & Field Theory](./module-6.4-path-integrals.md) →

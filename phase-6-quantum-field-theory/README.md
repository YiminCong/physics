# Phase 6 — Quantum Field Theory & Many-Body Physics

This phase delivers the research-level toolkit that underpins both modern condensed matter physics and high-energy particle physics. It extends second quantization with the full apparatus of Green's functions, Feynman diagrams, path integrals, canonical field quantization, and the renormalization group — the shared language in which superconductivity, the Standard Model, and critical phenomena are all written. Each module follows the Definition → Demonstration → Application format: precise definitions first, then a worked derivation or key result, then contact with experiment or the broader theoretical framework.

## Prerequisites

- **Phase 3** (Quantum Mechanics), especially Module 3.10 (Heisenberg picture, propagators, and the path integral) and Module 3.12 (second quantization, creation/annihilation operators, anticommutators).
- **Phase 1** Special Relativity and covariant electrodynamics (Modules 1.13–1.15) are essential for Module 6.5 (canonical quantization of relativistic fields).
- **Phase 2** statistical mechanics, particularly Module 2.3 (Landau–Ginzburg free energy), provides the bridge between QFT and critical phenomena exploited in Module 6.6.
- Familiarity with Phase 5 (Superconductivity), especially Module 5.5 (BCS Hamiltonian), enriches Modules 6.1 and 6.2 substantially.

## Modules

| Module | Title | Stars |
|--------|-------|-------|
| [6.1](./module-6.1-second-quantization.md) | Second Quantization & the Many-Body Problem | ⭐ |
| [6.2](./module-6.2-greens-functions.md) | Green's Functions & Propagators | ⭐ |
| [6.3](./module-6.3-feynman-diagrams.md) | Feynman Diagrams & Perturbation Theory | |
| [6.4](./module-6.4-path-integrals.md) | Path Integrals & Field Theory | ⭐ |
| [6.5](./module-6.5-canonical-quantization.md) | Canonical Quantization of Fields | ⭐ |
| [6.6](./module-6.6-renormalization.md) | Renormalization & the Renormalization Group | ⭐⭐ |
| [6.7](./module-6.7-exactly-solvable-models-and-long-range-order.md) | Exactly Solvable Models & Long-Range Order | |

## Further Reading

- **Coleman, S.** — *Introduction to Many-Body Physics* (lecture notes): the clearest entry point for non-relativistic field theory from a condensed matter perspective.
- **Fetter, A. L. & Walecka, J. D.** — *Quantum Theory of Many-Particle Systems*: definitive treatment of Green's functions and the Nambu–Gor'kov formalism for superconductivity.
- **Altland, A. & Simons, B.** — *Condensed Matter Field Theory* (2nd ed.): path integrals, Hubbard–Stratonovich, RG, and the bridge to statistical field theory; the standard graduate condensed-matter QFT text.
- **Peskin, M. E. & Schroeder, D. V.** — *An Introduction to Quantum Field Theory*: canonical quantization, Feynman rules, renormalization, and QED from the particle-physics side; pairs naturally with Module 6.5 and 6.6.

## Phase 6 Checkpoint (blank page)

1. Write the field operator ψ(x) in terms of single-particle orbitals φ_k(x) and mode operators c_k. Derive the equal-time anticommutator {ψ(x), ψ†(x')} = δ(x − x').
2. Sketch A(k,ω) for (a) a free Fermi gas and (b) a Fermi liquid with weak interactions. What does the width of the quasiparticle peak represent physically?
3. State the Dyson equation G = G⁰ + G⁰ Σ G and solve for G(k,ω). Draw the 1PI self-energy insertion Σ at the Hartree–Fock level.
4. Explain how Wick-rotating the quantum partition function Z = Tr e^{−βĤ} to imaginary time connects quantum field theory to classical statistical mechanics in d+1 dimensions.
5. What is the spin-statistics theorem? Give one consequence for the zero-point energy of a bosonic field versus a fermionic field (Bose versus Fermi statistics of the vacuum).
6. A ferromagnet and a liquid near its critical point exhibit the same critical exponent ν. Use the language of RG fixed points and universality classes to explain why microscopically different systems can share identical critical exponents.

---

→ Continue to **[Phase 7 — General Relativity & Cosmology](../phase-7-general-relativity-and-cosmology/)**, or apply this toolkit to **[Phase 8 — Particle Physics](../phase-8-particle-physics-and-standard-model/)**.

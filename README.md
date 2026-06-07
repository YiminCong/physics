# Physics Study Notes — From Classical Mechanics to the Standard Model

A complete self-study curriculum that builds from mathematical foundations all the way to
the frontier of modern physics — **classical mechanics, electromagnetism, special and
general relativity, thermodynamics, the full course of quantum mechanics, condensed matter,
superconductivity, quantum field theory, and the Standard Model of particle physics.**

Every note follows one consistent format — **Definition → Demonstration → Application** —
so you always see *what* a concept is, *how* it works on a concrete example, and *where* it
is used later. Modules marked ⭐ are load-bearing for what follows; ⭐⭐ are pivotal.

The curriculum is organized into **9 phases**, each a directory; each **module** is its own
file. There are **81 modules** in total.

---

## How to use these notes

- **Follow the [Recommended Learning Path](#recommended-learning-path) below** — it threads
  the 9 phases in dependency order.
- Each phase folder has a **README** with the phase's modules, its **prerequisites**, and a
  **blank-page checkpoint** (self-test). Pass the checkpoint before moving on.
- Each module ends with **prev / next navigation** so you can read a phase straight through.
- Keep the **[bilingual glossary (English ｜ 中文)](./GLOSSARY.md)** open as you read — it lists the key terminology of every phase with Chinese equivalents and short definitions.
- **Re-derive the ⭐ results by hand** — that's where real understanding comes from.

---

## Recommended Learning Path

> The phase numbers also *are* the learning order — read them 0 → 8 from top to bottom.
> Special Relativity lives at the end of Phase 1 (it is the relativistic completion of
> classical electromagnetism), so every prerequisite is satisfied in order: relativity
> before field theory, field theory before the Standard Model.

```
Phase 0  Mathematical Foundations
   │     calculus · linear algebra · ODEs · complex analysis · Fourier · tensors
   ▼
Phase 1  Classical Physics
   │     mechanics → Lagrangian/Hamiltonian → electromagnetism → special relativity
   ▼
Phase 2  Thermodynamics & Statistical Mechanics
   │     entropy · free energy · partition function · quantum statistics
   ▼
Phase 3  Quantum Mechanics  ◀── the core
   │     wave function → formalism → 3D/spin → identical particles → second quantization
   ├─────────────► Phase 4  Condensed Matter ──► Phase 5  Superconductivity
   ▼
Phase 6  Quantum Field Theory & Many-Body Physics
   │     second quantization → Green's functions → path integrals → renormalization
   ├─────────────► Phase 8  Particle Physics & the Standard Model
   ▼
Phase 7  General Relativity & Cosmology
         curved spacetime → Einstein's equations → black holes → the expanding universe
```

A few **threads worth watching** across the whole curriculum:

- **The harmonic oscillator** (1.6 → 3.2 → 4.3 → 6.1) becomes coupled oscillators, then
  the quantum oscillator, then phonons, then quantum fields.
- **The variational / free-energy principle** (1.3 → 2.3 → 3.7 → 5.3 → 7.4 → 8.4) reappears
  as least action, free-energy minimization, the QM variational method, Ginzburg–Landau
  theory, the Einstein–Hilbert action, and the Higgs mechanism.
- **Symmetry → conservation** (Noether, 1.4) grows into gauge theory and the Standard Model.
- **The complex phase** (0.4) carries interference, supercurrents, and the Josephson effect.
- **Spontaneous symmetry breaking** is *literally the same mechanism* in a superconductor
  (5.3) and in the Higgs sector of particle physics (8.4) — the Anderson–Higgs link.

---

## The Curriculum

### [Phase 0 — Mathematical Foundations](./phase-0-mathematical-foundations/)
The toolkit for everything that follows.
| # | Module | |
|---|--------|---|
| 0.1 | [Calculus & Taylor Series](./phase-0-mathematical-foundations/module-0.1-calculus-and-taylor-series.md) | |
| 0.2 | [Linear Algebra](./phase-0-mathematical-foundations/module-0.2-linear-algebra.md) | ⭐ |
| 0.3 | [Differential Equations](./phase-0-mathematical-foundations/module-0.3-differential-equations.md) | |
| 0.4 | [Complex Analysis](./phase-0-mathematical-foundations/module-0.4-complex-analysis.md) | ⭐ |
| 0.5 | [Fourier Analysis & Probability](./phase-0-mathematical-foundations/module-0.5-fourier-analysis-and-probability.md) | ⭐ |
| 0.6 | [Vector Calculus, Tensors & Differential Forms](./phase-0-mathematical-foundations/module-0.6-vector-calculus-tensors-and-differential-forms.md) | |

### [Phase 1 — Classical Physics](./phase-1-classical-physics/)
Mechanics, electromagnetism, waves & fluids, nonlinear dynamics, and special relativity.
| # | Module | |
|---|--------|---|
| 1.1 | [Newtonian Mechanics](./phase-1-classical-physics/module-1.1-newtonian-mechanics.md) | |
| 1.2 | [Conservation Laws](./phase-1-classical-physics/module-1.2-conservation-laws.md) | |
| 1.3 | [Lagrangian Mechanics & the Variational Principle](./phase-1-classical-physics/module-1.3-lagrangian-mechanics.md) | ⭐ |
| 1.4 | [Hamiltonian Mechanics, Action & Noether's Theorem](./phase-1-classical-physics/module-1.4-hamiltonian-mechanics-noether.md) | ⭐ |
| 1.5 | [Central-Force Problem & Kepler](./phase-1-classical-physics/module-1.5-central-force-kepler.md) | |
| 1.6 | [Small Oscillations & Coupled Oscillators](./phase-1-classical-physics/module-1.6-small-oscillations-coupled-oscillators.md) | ⭐ |
| 1.7 | [Rigid-Body Dynamics & Non-Inertial Frames](./phase-1-classical-physics/module-1.7-rigid-body-non-inertial-frames.md) | |
| 1.8 | [Electrostatics & Boundary-Value Problems](./phase-1-classical-physics/module-1.8-electrostatics-boundary-value-problems.md) | ⭐ |
| 1.9 | [Magnetostatics](./phase-1-classical-physics/module-1.9-magnetostatics.md) | |
| 1.10 | [Electrodynamics & Maxwell's Equations](./phase-1-classical-physics/module-1.10-electrodynamics-maxwell-equations.md) | ⭐ |
| 1.11 | [Electromagnetic Waves & Radiation](./phase-1-classical-physics/module-1.11-em-waves-radiation.md) | |
| 1.12 | [Optics & Interference](./phase-1-classical-physics/module-1.12-optics-interference.md) | |
| 1.13 | [Special Relativity — Kinematics](./phase-1-classical-physics/module-1.13-special-relativity-kinematics.md) | ⭐ |
| 1.14 | [Relativistic Dynamics & E = mc²](./phase-1-classical-physics/module-1.14-relativistic-dynamics-energy-momentum.md) | ⭐ |
| 1.15 | [Covariant Electromagnetism](./phase-1-classical-physics/module-1.15-covariant-electromagnetism.md) | |
| 1.16 | [Mechanical Waves & Acoustics](./phase-1-classical-physics/module-1.16-mechanical-waves-acoustics.md) | |
| 1.17 | [Fluid Mechanics](./phase-1-classical-physics/module-1.17-fluid-mechanics.md) | |
| 1.18 | [Continuum Mechanics & Elasticity](./phase-1-classical-physics/module-1.18-continuum-mechanics-elasticity.md) | |
| 1.19 | [Nonlinear Dynamics & Chaos](./phase-1-classical-physics/module-1.19-nonlinear-dynamics-chaos.md) | |

### [Phase 2 — Thermodynamics & Statistical Mechanics](./phase-2-thermodynamics-statistical-mechanics/)
From heat engines to quantum statistics.
| # | Module | |
|---|--------|---|
| 2.1 | [The Laws of Thermodynamics](./phase-2-thermodynamics-statistical-mechanics/module-2.1-laws-of-thermodynamics.md) | |
| 2.2 | [Thermodynamic Potentials & Maxwell Relations](./phase-2-thermodynamics-statistical-mechanics/module-2.2-thermodynamic-potentials.md) | |
| 2.3 | [Free Energy & Phase Transitions](./phase-2-thermodynamics-statistical-mechanics/module-2.3-free-energy-phase-transitions.md) | ⭐ |
| 2.4 | [Classical Statistical Mechanics](./phase-2-thermodynamics-statistical-mechanics/module-2.4-classical-statistical-mechanics.md) | |
| 2.5 | [Quantum Statistics](./phase-2-thermodynamics-statistical-mechanics/module-2.5-quantum-statistics.md) | ⭐ |
| 2.6 | [Quantum Gases & Applications](./phase-2-thermodynamics-statistical-mechanics/module-2.6-quantum-gases-applications.md) | |
| 2.7 | [Kinetic Theory & Transport](./phase-2-thermodynamics-statistical-mechanics/module-2.7-kinetic-theory-and-transport.md) | |
| 2.8 | [Brownian Motion & the Einstein Relation](./phase-2-thermodynamics-statistical-mechanics/module-2.8-brownian-motion-and-the-einstein-relation.md) | |

### [Phase 3 — Quantum Mechanics](./phase-3-quantum-mechanics/)
The core of modern physics. Modules 3.1–3.12.
| # | Module | |
|---|--------|---|
| 3.0 | [Old Quantum Theory & the Photoelectric Effect](./phase-3-quantum-mechanics/module-3.0-old-quantum-theory-and-photoelectric-effect.md) | |
| 3.1 | [The Wave Function](./phase-3-quantum-mechanics/module-3.1-the-wave-function.md) | |
| 3.2 | [Time-Independent Schrödinger Equation](./phase-3-quantum-mechanics/module-3.2-time-independent-schrodinger-equation.md) | ⭐ |
| 3.3 | [Formalism](./phase-3-quantum-mechanics/module-3.3-formalism.md) | ⭐ |
| 3.4 | [Quantum Mechanics in 3D](./phase-3-quantum-mechanics/module-3.4-quantum-mechanics-in-3d.md) | ⭐ |
| 3.5 | [Identical Particles](./phase-3-quantum-mechanics/module-3.5-identical-particles.md) | ⭐ |
| 3.6 | [Time-Independent Perturbation Theory](./phase-3-quantum-mechanics/module-3.6-time-independent-perturbation-theory.md) | |
| 3.7 | [Variational & WKB Methods](./phase-3-quantum-mechanics/module-3.7-variational-and-wkb-methods.md) | |
| 3.8 | [Time-Dependent Perturbation Theory & Scattering](./phase-3-quantum-mechanics/module-3.8-time-dependent-perturbation-theory-and-scattering.md) | |
| 3.9 | [Fundamental Concepts (Sakurai)](./phase-3-quantum-mechanics/module-3.9-fundamental-concepts.md) | |
| 3.10 | [Quantum Dynamics](./phase-3-quantum-mechanics/module-3.10-quantum-dynamics.md) | ⭐ |
| 3.11 | [Angular Momentum, Advanced](./phase-3-quantum-mechanics/module-3.11-angular-momentum-advanced.md) | ⭐ |
| 3.12 | [Symmetry, Identical Particles & Second Quantization](./phase-3-quantum-mechanics/module-3.12-second-quantization.md) | ⭐⭐ |
| 3.13 | [Entanglement, EPR & Bell's Theorem](./phase-3-quantum-mechanics/module-3.13-entanglement-epr-and-bell.md) | ⭐ |

### [Phase 4 — Condensed Matter / Solid State](./phase-4-condensed-matter/)
Electrons and phonons in a crystal. Modules 4.1–4.5.
| # | Module | |
|---|--------|---|
| 4.1 | [Electrons and Heat in Solids](./phase-4-condensed-matter/module-4.1-electrons-and-heat-in-solids.md) | |
| 4.2 | [Crystal Structure & Reciprocal Space](./phase-4-condensed-matter/module-4.2-crystal-structure-and-reciprocal-space.md) | ⭐ |
| 4.3 | [Lattice Vibrations & Phonons](./phase-4-condensed-matter/module-4.3-lattice-vibrations-and-phonons.md) | ⭐ |
| 4.4 | [Electrons in a Periodic Potential](./phase-4-condensed-matter/module-4.4-electrons-in-a-periodic-potential.md) | ⭐ |
| 4.5 | [Fermi Surface & Electron–Phonon Coupling](./phase-4-condensed-matter/module-4.5-fermi-surface-and-electron-phonon-coupling.md) | ⭐ |

### [Phase 5 — Superconductivity](./phase-5-superconductivity/)
Where it all converges. Modules 5.1–5.9.
| # | Module | |
|---|--------|---|
| 5.1 | [Phenomenology](./phase-5-superconductivity/module-5.1-phenomenology.md) | |
| 5.2 | [London Theory](./phase-5-superconductivity/module-5.2-london-theory.md) | ⭐ |
| 5.3 | [Ginzburg–Landau Theory](./phase-5-superconductivity/module-5.3-ginzburg-landau-theory.md) | ⭐⭐ |
| 5.4 | [The Cooper Problem](./phase-5-superconductivity/module-5.4-the-cooper-problem.md) | ⭐ |
| 5.5 | [BCS Theory](./phase-5-superconductivity/module-5.5-bcs-theory.md) | ⭐⭐ |
| 5.6 | [Tunneling & the Gap](./phase-5-superconductivity/module-5.6-tunneling-and-the-gap.md) | |
| 5.7 | [Type II Superconductors & Vortices](./phase-5-superconductivity/module-5.7-type-ii-superconductors-and-vortices.md) | ⭐ |
| 5.8 | [Josephson Effects](./phase-5-superconductivity/module-5.8-josephson-effects.md) | ⭐ |
| 5.9 | [Unconventional & High-Tᶜ Superconductors](./phase-5-superconductivity/module-5.9-unconventional-and-high-tc-superconductors.md) | |

### [Phase 6 — Quantum Field Theory & Many-Body Physics](./phase-6-quantum-field-theory/)
The modern research toolkit; the shared language of condensed matter and particle physics.
| # | Module | |
|---|--------|---|
| 6.1 | [Second Quantization & the Many-Body Problem](./phase-6-quantum-field-theory/module-6.1-second-quantization.md) | ⭐ |
| 6.2 | [Green's Functions & Propagators](./phase-6-quantum-field-theory/module-6.2-greens-functions.md) | ⭐ |
| 6.3 | [Feynman Diagrams & Perturbation Theory](./phase-6-quantum-field-theory/module-6.3-feynman-diagrams.md) | |
| 6.4 | [Path Integrals & Field Theory](./phase-6-quantum-field-theory/module-6.4-path-integrals.md) | ⭐ |
| 6.5 | [Canonical Quantization of Fields](./phase-6-quantum-field-theory/module-6.5-canonical-quantization.md) | ⭐ |
| 6.6 | [Renormalization & the Renormalization Group](./phase-6-quantum-field-theory/module-6.6-renormalization.md) | ⭐⭐ |
| 6.7 | [Exactly Solvable Models & Long-Range Order](./phase-6-quantum-field-theory/module-6.7-exactly-solvable-models-and-long-range-order.md) | |

### [Phase 7 — General Relativity & Cosmology](./phase-7-general-relativity-and-cosmology/)
Gravity as the geometry of spacetime.
| # | Module | |
|---|--------|---|
| 7.1 | [The Equivalence Principle & Curved Spacetime](./phase-7-general-relativity-and-cosmology/module-7.1-equivalence-principle-and-curved-spacetime.md) | ⭐ |
| 7.2 | [Tensors, the Metric & Curvature](./phase-7-general-relativity-and-cosmology/module-7.2-tensors-metric-and-curvature.md) | ⭐ |
| 7.3 | [Geodesics & the Motion of Particles](./phase-7-general-relativity-and-cosmology/module-7.3-geodesics-and-motion-of-particles.md) | |
| 7.4 | [Einstein's Field Equations](./phase-7-general-relativity-and-cosmology/module-7.4-einsteins-field-equations.md) | ⭐⭐ |
| 7.5 | [Black Holes & Gravitational Waves](./phase-7-general-relativity-and-cosmology/module-7.5-black-holes-and-gravitational-waves.md) | ⭐ |
| 7.6 | [Cosmology](./phase-7-general-relativity-and-cosmology/module-7.6-cosmology.md) | |

### [Phase 8 — Particle Physics & the Standard Model](./phase-8-particle-physics-and-standard-model/)
The quantum field theory of the fundamental particles and forces.
| # | Module | |
|---|--------|---|
| 8.1 | [Symmetries & Gauge Theory](./phase-8-particle-physics-and-standard-model/module-8.1-symmetries-and-gauge-theory.md) | ⭐ |
| 8.2 | [Quantum Electrodynamics (QED)](./phase-8-particle-physics-and-standard-model/module-8.2-quantum-electrodynamics.md) | ⭐ |
| 8.3 | [The Strong Interaction (QCD)](./phase-8-particle-physics-and-standard-model/module-8.3-quantum-chromodynamics.md) | |
| 8.4 | [Electroweak Theory & the Higgs](./phase-8-particle-physics-and-standard-model/module-8.4-electroweak-theory-and-higgs.md) | ⭐⭐ |
| 8.5 | [The Standard Model & Beyond](./phase-8-particle-physics-and-standard-model/module-8.5-standard-model-and-beyond.md) | |
| 8.6 | [Particle Physics & Cosmology](./phase-8-particle-physics-and-standard-model/module-8.6-particle-physics-and-cosmology.md) | |
| 8.7 | [Parity Violation & the Weak Interaction (Lee–Yang)](./phase-8-particle-physics-and-standard-model/module-8.7-parity-violation-and-the-weak-interaction.md) | |

---

## Phase dependency reference

| Phase | Prerequisites |
|-------|---------------|
| 0 — Mathematical Foundations | none |
| 1 — Classical Physics | 0 |
| 2 — Thermodynamics & Stat. Mech. | 0, 1 |
| 3 — Quantum Mechanics | 0, 1, 2 |
| 4 — Condensed Matter | 2, 3 |
| 5 — Superconductivity | 2, 3, 4 |
| 6 — Quantum Field Theory | 1 (incl. special relativity), 2, 3 |
| 7 — General Relativity & Cosmology | 0.6, 1.13–1.15 |
| 8 — Particle Physics & Standard Model | 1.13–1.15, 3, 6 |

*From the calculus of Module 0.1 to the Higgs mechanism of Module 8.4, every step is a
prerequisite for the next. Pass each blank-page checkpoint and you will genuinely understand
how the pieces of modern physics fit together.*

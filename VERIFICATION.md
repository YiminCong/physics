# Verification Status · 校验状态


**120 / 120 derivation files verified.**

> ✅ = derivation reviewed line-by-line and confirmed (or corrected) against standard results. Most were verified on **2026-06-08**; files revised later carry a newer date in their badge.

Each verified `*-derivations.md` file carries a green-check badge near the top with a machine-readable anchor `<!-- verified:DATE -->`.

**To re-verify only what changed later**, skip any file whose `verified:` date is newer than its last git modification:

```bash
for f in $(git ls-files '*-derivations.md'); do
  vdate=$(grep -o "verified:[0-9-]*" "$f" | head -1 | cut -d: -f2)
  mdate=$(git log -1 --format=%cs -- "$f")
  [ -n "$vdate" ] && [ "$mdate" \> "$vdate" ] && echo "NEEDS RE-CHECK: $f"
done
```


## Phase 0 Mathematical Foundations

- ✅ [`0.1`](phase-0-mathematical-foundations/module-0.1-calculus-and-taylor-series-derivations.md) — Calculus & Taylor Series
- ✅ [`0.2`](phase-0-mathematical-foundations/module-0.2-linear-algebra-derivations.md) — Linear Algebra
- ✅ [`0.3`](phase-0-mathematical-foundations/module-0.3-differential-equations-derivations.md) — Differential Equations
- ✅ [`0.4`](phase-0-mathematical-foundations/module-0.4-complex-analysis-derivations.md) — Complex Analysis
- ✅ [`0.5`](phase-0-mathematical-foundations/module-0.5-fourier-analysis-and-probability-derivations.md) — Fourier Analysis & Probability
- ✅ [`0.6`](phase-0-mathematical-foundations/module-0.6-vector-calculus-tensors-and-differential-forms-derivations.md) — Vector Calculus, Tensors & Differential Forms
- ✅ [`0.7`](phase-0-mathematical-foundations/module-0.7-group-theory-and-lie-algebras-derivations.md) — Group Theory & Lie Algebras

## Phase 1 Classical Physics

- ✅ [`1.1`](phase-1-classical-physics/module-1.1-newtonian-mechanics-derivations.md) — Newtonian Mechanics
- ✅ [`1.2`](phase-1-classical-physics/module-1.2-conservation-laws-derivations.md) — Conservation Laws
- ✅ [`1.3`](phase-1-classical-physics/module-1.3-lagrangian-mechanics-derivations.md) — Lagrangian Mechanics
- ✅ [`1.4`](phase-1-classical-physics/module-1.4-hamiltonian-mechanics-noether-derivations.md) — Hamiltonian Mechanics & Noether's Theorem
- ✅ [`1.5`](phase-1-classical-physics/module-1.5-central-force-kepler-derivations.md) — Central Force & Kepler
- ✅ [`1.6`](phase-1-classical-physics/module-1.6-small-oscillations-coupled-oscillators-derivations.md) — Small Oscillations & Coupled Oscillators
- ✅ [`1.7`](phase-1-classical-physics/module-1.7-rigid-body-non-inertial-frames-derivations.md) — Rigid-Body Dynamics & Non-Inertial Frames
- ✅ [`1.8`](phase-1-classical-physics/module-1.8-electrostatics-boundary-value-problems-derivations.md) — Electrostatics & Boundary-Value Problems
- ✅ [`1.9`](phase-1-classical-physics/module-1.9-magnetostatics-derivations.md) — Magnetostatics
- ✅ [`1.10`](phase-1-classical-physics/module-1.10-electrodynamics-maxwell-equations-derivations.md) — Electrodynamics & Maxwell's Equations
- ✅ [`1.11`](phase-1-classical-physics/module-1.11-em-waves-radiation-derivations.md) — Electromagnetic Waves & Radiation
- ✅ [`1.12`](phase-1-classical-physics/module-1.12-optics-interference-derivations.md) — Optics & Interference
- ✅ [`1.13`](phase-1-classical-physics/module-1.13-special-relativity-kinematics-derivations.md) — Special Relativity — Kinematics
- ✅ [`1.14`](phase-1-classical-physics/module-1.14-relativistic-dynamics-energy-momentum-derivations.md) — Relativistic Dynamics & E = mc²
- ✅ [`1.15`](phase-1-classical-physics/module-1.15-covariant-electromagnetism-derivations.md) — Covariant Electromagnetism
- ✅ [`1.16`](phase-1-classical-physics/module-1.16-mechanical-waves-acoustics-derivations.md) — Mechanical Waves & Acoustics
- ✅ [`1.17`](phase-1-classical-physics/module-1.17-fluid-mechanics-derivations.md) — Fluid Mechanics
- ✅ [`1.18`](phase-1-classical-physics/module-1.18-continuum-mechanics-elasticity-derivations.md) — Continuum Mechanics & Elasticity
- ✅ [`1.19`](phase-1-classical-physics/module-1.19-nonlinear-dynamics-chaos-derivations.md) — Nonlinear Dynamics & Chaos
- ✅ [`1.20`](phase-1-classical-physics/module-1.20-canonical-transformations-hamilton-jacobi-derivations.md) — Canonical Transformations, Hamilton–Jacobi & Action–Angle
- ✅ [`1.21`](phase-1-classical-physics/module-1.21-classical-scattering-derivations.md) — Classical Scattering Theory
- ✅ [`1.22`](phase-1-classical-physics/module-1.22-retarded-potentials-radiation-reaction-derivations.md) — Retarded Potentials, Multipole Radiation & Radiation Reaction
- ✅ [`1.23`](phase-1-classical-physics/module-1.23-waveguides-cavities-transmission-lines-derivations.md) — Waveguides, Cavity Resonators & Transmission Lines

## Phase 10 Strings And Quantum Gravity

- ✅ [`10.1`](phase-10-strings-and-quantum-gravity/module-10.1-derivations.md) — String Theory & Superstrings
- ✅ [`10.2`](phase-10-strings-and-quantum-gravity/module-10.2-derivations.md) — Quantum Gravity & Holography

## Phase 2 Thermodynamics Statistical Mechanics

- ✅ [`2.1`](phase-2-thermodynamics-statistical-mechanics/module-2.1-derivations.md) — The Laws of Thermodynamics
- ✅ [`2.2`](phase-2-thermodynamics-statistical-mechanics/module-2.2-derivations.md) — Thermodynamic Potentials & Maxwell Relations
- ✅ [`2.3`](phase-2-thermodynamics-statistical-mechanics/module-2.3-derivations.md) — Free Energy & Phase Transitions
- ✅ [`2.4`](phase-2-thermodynamics-statistical-mechanics/module-2.4-derivations.md) — Classical Statistical Mechanics
- ✅ [`2.5`](phase-2-thermodynamics-statistical-mechanics/module-2.5-derivations.md) — Quantum Statistics
- ✅ [`2.6`](phase-2-thermodynamics-statistical-mechanics/module-2.6-derivations.md) — Quantum Gases & Applications
- ✅ [`2.7`](phase-2-thermodynamics-statistical-mechanics/module-2.7-derivations.md) — Kinetic Theory & Transport
- ✅ [`2.8`](phase-2-thermodynamics-statistical-mechanics/module-2.8-derivations.md) — Brownian Motion & the Einstein Relation

## Phase 3 Quantum Mechanics

- ✅ [`3.0`](phase-3-quantum-mechanics/module-3.0-derivations.md) — Old Quantum Theory & the Photoelectric Effect
- ✅ [`3.1`](phase-3-quantum-mechanics/module-3.1-derivations.md) — The Wave Function
- ✅ [`3.2`](phase-3-quantum-mechanics/module-3.2-derivations.md) — Time-Independent Schrödinger Equation
- ✅ [`3.3`](phase-3-quantum-mechanics/module-3.3-derivations.md) — Formalism
- ✅ [`3.4`](phase-3-quantum-mechanics/module-3.4-derivations.md) — Quantum Mechanics in 3D
- ✅ [`3.5`](phase-3-quantum-mechanics/module-3.5-derivations.md) — Identical Particles
- ✅ [`3.6`](phase-3-quantum-mechanics/module-3.6-derivations.md) — Time-Independent Perturbation Theory
- ✅ [`3.7`](phase-3-quantum-mechanics/module-3.7-derivations.md) — Variational & WKB Methods
- ✅ [`3.8`](phase-3-quantum-mechanics/module-3.8-derivations.md) — Time-Dependent Perturbation Theory & Scattering
- ✅ [`3.9`](phase-3-quantum-mechanics/module-3.9-derivations.md) — Fundamental Concepts (Sakurai)
- ✅ [`3.10`](phase-3-quantum-mechanics/module-3.10-derivations.md) — Quantum Dynamics
- ✅ [`3.11`](phase-3-quantum-mechanics/module-3.11-derivations.md) — Angular Momentum (Addition & Spin)
- ✅ [`3.12`](phase-3-quantum-mechanics/module-3.12-derivations.md) — Second Quantization
- ✅ [`3.13`](phase-3-quantum-mechanics/module-3.13-derivations.md) — Entanglement, EPR & Bell's Theorem
- ✅ [`3.14`](phase-3-quantum-mechanics/module-3.14-density-matrix-and-open-quantum-systems-derivations.md) — Density Matrix & Open Quantum Systems
- ✅ [`3.15`](phase-3-quantum-mechanics/module-3.15-relativistic-quantum-mechanics-derivations.md) — Relativistic Quantum Mechanics
- ✅ [`3.16`](phase-3-quantum-mechanics/module-3.16-quantum-computation-and-information-derivations.md) — Quantum Computation & Information
- ✅ [`3.17`](phase-3-quantum-mechanics/module-3.17-quantum-algorithms-and-error-correction-derivations.md) — Quantum Algorithms & Error Correction
- ✅ [`3.18`](phase-3-quantum-mechanics/module-3.18-quantum-scattering-theory-derivations.md) — Quantum Scattering Theory

## Phase 4 Condensed Matter

- ✅ [`4.1`](phase-4-condensed-matter/module-4.1-derivations.md) — Electrons and Heat in Solids
- ✅ [`4.2`](phase-4-condensed-matter/module-4.2-derivations.md) — Crystal Structure & Reciprocal Space
- ✅ [`4.3`](phase-4-condensed-matter/module-4.3-derivations.md) — Lattice Vibrations & Phonons
- ✅ [`4.4`](phase-4-condensed-matter/module-4.4-derivations.md) — Electrons in a Periodic Potential
- ✅ [`4.5`](phase-4-condensed-matter/module-4.5-derivations.md) — Fermi Surface & Electron–Phonon Coupling
- ✅ [`4.6`](phase-4-condensed-matter/module-4.6-derivations.md) — Magnetism & Spin Waves
- ✅ [`4.7`](phase-4-condensed-matter/module-4.7-derivations.md) — Semiconductor Physics
- ✅ [`4.8`](phase-4-condensed-matter/module-4.8-derivations.md) — Quantum Hall Effect
- ✅ [`4.9`](phase-4-condensed-matter/module-4.9-derivations.md) — Topological Matter & Berry Phase
- ✅ [`4.10`](phase-4-condensed-matter/module-4.10-landau-fermi-liquid-theory-derivations.md) — Landau Fermi-Liquid Theory
- ✅ [`4.11`](phase-4-condensed-matter/module-4.11-linear-response-and-transport-derivations.md) — Linear Response, Transport & the Kubo Formula
- ✅ [`4.12`](phase-4-condensed-matter/module-4.12-hubbard-model-and-mott-insulators-derivations.md) — The Hubbard Model & Mott Insulators

## Phase 5 Superconductivity

- ✅ [`5.1`](phase-5-superconductivity/module-5.1-phenomenology-derivations.md) — Phenomenology of Superconductivity
- ✅ [`5.2`](phase-5-superconductivity/module-5.2-london-theory-derivations.md) — London Theory
- ✅ [`5.3`](phase-5-superconductivity/module-5.3-ginzburg-landau-theory-derivations.md) — Ginzburg–Landau Theory
- ✅ [`5.4`](phase-5-superconductivity/module-5.4-the-cooper-problem-derivations.md) — The Cooper Problem
- ✅ [`5.5`](phase-5-superconductivity/module-5.5-bcs-theory-derivations.md) — BCS Theory
- ✅ [`5.6`](phase-5-superconductivity/module-5.6-tunneling-and-the-gap-derivations.md) — Tunneling & the Gap
- ✅ [`5.7`](phase-5-superconductivity/module-5.7-type-ii-superconductors-and-vortices-derivations.md) — Type II Superconductors & Vortices
- ✅ [`5.8`](phase-5-superconductivity/module-5.8-josephson-effects-derivations.md) — Josephson Effects
- ✅ [`5.9`](phase-5-superconductivity/module-5.9-unconventional-and-high-tc-superconductors-derivations.md) — Unconventional & High-Tᶜ Superconductors
- ✅ [`5.10`](phase-5-superconductivity/module-5.10-bogoliubov-de-gennes-and-andreev-reflection-derivations.md) — Bogoliubov–de Gennes & Andreev Reflection
- ✅ [`5.11`](phase-5-superconductivity/module-5.11-topological-superconductivity-and-majorana-derivations.md) — Topological Superconductivity & Majorana Modes

## Phase 6 Quantum Field Theory

- ✅ [`6.1`](phase-6-quantum-field-theory/module-6.1-second-quantization-derivations.md) — Second Quantization & the Many-Body Problem
- ✅ [`6.2`](phase-6-quantum-field-theory/module-6.2-greens-functions-derivations.md) — Green's Functions & Propagators
- ✅ [`6.3`](phase-6-quantum-field-theory/module-6.3-feynman-diagrams-derivations.md) — Feynman Diagrams & Perturbation Theory
- ✅ [`6.4`](phase-6-quantum-field-theory/module-6.4-path-integrals-derivations.md) — Path Integrals & Field Theory
- ✅ [`6.5`](phase-6-quantum-field-theory/module-6.5-canonical-quantization-derivations.md) — Canonical Quantization of Fields
- ✅ [`6.6`](phase-6-quantum-field-theory/module-6.6-renormalization-derivations.md) — Renormalization & the Renormalization Group
- ✅ [`6.7`](phase-6-quantum-field-theory/module-6.7-exactly-solvable-models-and-long-range-order-derivations.md) — Exactly Solvable Models & Long-Range Order
- ✅ [`6.8`](phase-6-quantum-field-theory/module-6.8-scattering-s-matrix-and-lsz-derivations.md) — Scattering, the S-Matrix & LSZ Reduction
- ✅ [`6.9`](phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft-derivations.md) — Anomalies & Non-Perturbative QFT
- ✅ [`6.10`](phase-6-quantum-field-theory/module-6.10-spontaneous-symmetry-breaking-and-goldstone-derivations.md) — Spontaneous Symmetry Breaking & Goldstone's Theorem
- ✅ [`6.11`](phase-6-quantum-field-theory/module-6.11-effective-field-theory-and-the-renormalization-group-derivations.md) — Effective Field Theory & the Wilsonian Renormalization Group
- ✅ [`6.12`](phase-6-quantum-field-theory/module-6.12-finite-temperature-field-theory-derivations.md) — Finite-Temperature Field Theory

## Phase 7 General Relativity And Cosmology

- ✅ [`7.1`](phase-7-general-relativity-and-cosmology/module-7.1-equivalence-principle-and-curved-spacetime-derivations.md) — The Equivalence Principle & Curved Spacetime
- ✅ [`7.2`](phase-7-general-relativity-and-cosmology/module-7.2-tensors-metric-and-curvature-derivations.md) — Tensors, the Metric & Curvature
- ✅ [`7.3`](phase-7-general-relativity-and-cosmology/module-7.3-geodesics-and-motion-of-particles-derivations.md) — Geodesics & the Motion of Particles
- ✅ [`7.4`](phase-7-general-relativity-and-cosmology/module-7.4-einsteins-field-equations-derivations.md) — Einstein's Field Equations
- ✅ [`7.5`](phase-7-general-relativity-and-cosmology/module-7.5-black-holes-and-gravitational-waves-derivations.md) — Black Holes & Gravitational Waves
- ✅ [`7.6`](phase-7-general-relativity-and-cosmology/module-7.6-cosmology-derivations.md) — Cosmology
- ✅ [`7.7`](phase-7-general-relativity-and-cosmology/module-7.7-tests-of-gr-and-gravitational-wave-astronomy-derivations.md) — Tests of GR & Gravitational-Wave Astronomy
- ✅ [`7.8`](phase-7-general-relativity-and-cosmology/module-7.8-global-structure-and-singularity-theorems-derivations.md) — Global Structure & Singularity Theorems

## Phase 8 Particle Physics And Standard Model

- ✅ [`8.1`](phase-8-particle-physics-and-standard-model/module-8.1-derivations.md) — Symmetries & Gauge Theory
- ✅ [`8.2`](phase-8-particle-physics-and-standard-model/module-8.2-derivations.md) — Quantum Electrodynamics (QED)
- ✅ [`8.3`](phase-8-particle-physics-and-standard-model/module-8.3-derivations.md) — Quantum Chromodynamics (QCD)
- ✅ [`8.4`](phase-8-particle-physics-and-standard-model/module-8.4-derivations.md) — Electroweak Theory & the Higgs
- ✅ [`8.5`](phase-8-particle-physics-and-standard-model/module-8.5-derivations.md) — The Standard Model & Beyond
- ✅ [`8.6`](phase-8-particle-physics-and-standard-model/module-8.6-derivations.md) — Particle Physics & Cosmology
- ✅ [`8.7`](phase-8-particle-physics-and-standard-model/module-8.7-derivations.md) — Parity Violation & the Weak Interaction
- ✅ [`8.8`](phase-8-particle-physics-and-standard-model/module-8.8-quark-model-and-hadron-spectroscopy-derivations.md) — The Quark Model & Hadron Spectroscopy
- ✅ [`8.9`](phase-8-particle-physics-and-standard-model/module-8.9-deep-inelastic-scattering-and-partons-derivations.md) — Deep Inelastic Scattering & Partons
- ✅ [`8.10`](phase-8-particle-physics-and-standard-model/module-8.10-neutrino-physics-and-experiment-derivations.md) — Neutrino Physics & Experimental Particle Physics

## Phase 9 Applied And Specialized Physics

- ✅ [`9.1`](phase-9-applied-and-specialized-physics/module-9.1-electronics-derivations.md) — Electronics
- ✅ [`9.2`](phase-9-applied-and-specialized-physics/module-9.2-atomic-and-molecular-physics-derivations.md) — Atomic & Molecular Physics
- ✅ [`9.3`](phase-9-applied-and-specialized-physics/module-9.3-nuclear-physics-derivations.md) — Nuclear Physics
- ✅ [`9.4`](phase-9-applied-and-specialized-physics/module-9.4-plasma-physics-derivations.md) — Plasma Physics
- ✅ [`9.5`](phase-9-applied-and-specialized-physics/module-9.5-nuclear-reactions-and-astrophysics-derivations.md) — Nuclear Reactions & Astrophysics
- ✅ [`9.6`](phase-9-applied-and-specialized-physics/module-9.6-quantum-optics-and-lasers-derivations.md) — Quantum Optics & Laser Physics
- ✅ [`9.7`](phase-9-applied-and-specialized-physics/module-9.7-atoms-in-external-fields-derivations.md) — Atoms in External Fields & Precision Spectroscopy
- ✅ [`9.8`](phase-9-applied-and-specialized-physics/module-9.8-stellar-structure-and-compact-objects-derivations.md) — Stellar Structure & Compact Objects

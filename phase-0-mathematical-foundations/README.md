# Phase 0 — Mathematical Foundations

This phase assembles the toolkit that every later phase draws on. All six modules follow the **Definition → Demonstration → Application** format — each section builds the idea, shows it working, and points forward to the physics that depends on it.

## Modules

| # | Title | Notes |
|---|-------|-------|
| 0.1 | [Calculus & Taylor Series](./module-0.1-calculus-and-taylor-series.md) | Derivatives, integrals, FTC; Taylor series as the universal approximation tool |
| 0.2 | [Linear Algebra](./module-0.2-linear-algebra.md) ⭐ | Vector spaces, inner products, eigenvalues; the Pauli matrices; QM is this |
| 0.3 | [Differential Equations](./module-0.3-differential-equations.md) | First- and second-order ODEs, series solutions, PDEs and separation of variables |
| 0.4 | [Complex Analysis](./module-0.4-complex-analysis.md) ⭐ | Euler's formula, analytic functions, contour integration; phase drives superconductivity |
| 0.5 | [Fourier Analysis & Probability](./module-0.5-fourier-analysis-and-probability.md) ⭐ | Fourier transform, Dirac delta, convolution; mean, variance, Gaussian, CLT |
| 0.6 | [Vector Calculus, Tensors & Differential Forms](./module-0.6-vector-calculus-tensors-and-differential-forms.md) | ∇, ∇·, ∇×, integral theorems; index notation, the metric tensor; Maxwell in a line |

## Why these matter downstream

- **0.1** — the self-referential property eˣ = d/dx(eˣ) seeds every constant-coefficient ODE solution and, via iθ substitution, Euler's formula in 0.4.
- **0.2** — quantum mechanics is linear algebra in Hilbert space; Hermitian operators give measurement outcomes, unitary operators give time evolution (Phase 3).
- **0.3** — the second-order linear ODE is the time-independent Schrödinger equation in disguise; special functions (Hermite, Legendre, Laguerre) are the wavefunctions of the oscillator, angular momentum, and hydrogen (Phase 3).
- **0.4** — complex amplitudes underlie all of QM; the phase φ of the order parameter ψ = |ψ|e^{iφ} drives supercurrents and the Josephson effect (Phase 5).
- **0.5** — position and momentum are Fourier conjugates, making the uncertainty principle a theorem; the reciprocal lattice is the FT of the crystal (Phase 4).
- **0.6** — vector calculus is the native language of electromagnetism (Phase 1); the metric tensor g_{μν} is the central object of general relativity (Phase 7).

## Phase 0 Checkpoint (blank page)

Work through these without notes. If any answer is unclear, revisit the corresponding module before moving on.

1. (0.1) Expand sin x and cos x as Taylor series; use them to derive Euler's formula e^{iθ} = cos θ + i sin θ.
2. (0.2) State the spectral theorem for Hermitian operators. Find the eigenvalues and eigenvectors of σ_y.
3. (0.3) Solve y″ + 2γy′ + ω₀²y = 0; identify the three damping regimes. How does separation of variables apply to the Schrödinger equation?
4. (0.4) Evaluate ∮ dz / (z² + 1) around a contour enclosing z = i using residues.
5. (0.5) Why is the Fourier transform of a Gaussian another Gaussian, and how does this become the Heisenberg uncertainty principle?
6. (0.6) Write Maxwell's four equations in differential form, naming the operator (∇·, ∇×) in each, and state the integral theorem that converts each to its integral form.

---

→ Continue to **[Phase 1 — Classical Physics](../phase-1-classical-physics/)**.

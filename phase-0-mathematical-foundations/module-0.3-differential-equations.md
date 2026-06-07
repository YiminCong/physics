# Module 0.3 — Differential Equations

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Physics is written in differential equations. The second-order linear ODE in particular
is *the* equation you'll meet again and again — oscillators, waves, and the Schrödinger
equation are all this one form.

---

## 1. First-Order ODEs

**Definition.** A first-order ODE relates a function y to its first derivative y′. Two solvable types:
- **Separable:** dy/dx = g(x)h(y) → rearrange to ∫ dy/h(y) = ∫ g(x) dx.
- **Linear:** y′ + p(x)y = q(x), solved with the **integrating factor** μ = e^{∫p dx}.

**Demonstration.** Solve dy/dx = −k y (separable):

  ∫ dy/y = ∫ −k dx → ln y = −kx + C → **y = y₀ e^{−kx}** (exponential decay).

**Application.** Radioactive decay, RC-circuit discharge, Newton's law of cooling. This is your first encounter with the exponential — the function that dominates physics because it's its own derivative.

---

## 2. Second-Order Linear ODEs with Constant Coefficients ⭐

**Definition.** The equation a y″ + b y′ + c y = 0. Guess y = e^{rt}; substituting gives the **characteristic equation** a r² + b r + c = 0. The roots determine behavior:
- two real roots → exponential (overdamped),
- a repeated root → critical damping,
- complex roots → oscillation.

**Demonstration.** The undamped oscillator y″ + ω²y = 0. Characteristic equation r² + ω² = 0 → r = ±iω, so

  **y(t) = A cos ωt + B sin ωt.**

Add damping: y″ + 2γy′ + ω₀²y = 0 gives decaying oscillations when γ < ω₀.

**Application.** This single equation is simple harmonic motion, the damped/driven oscillator (Phase 1), AC circuits, and — most importantly — the **time-independent Schrödinger equation** for constant-potential regions is exactly this form (Phase 3). If you own one ODE, own this one.

---

## 3. Series Solutions & Special Functions

**Definition.** When coefficients vary with x, you can't guess e^{rt}. Instead substitute a power series y = Σ aₙ xⁿ and solve a **recursion** for the coefficients (the Frobenius method). Specific physics equations generate named **special functions**: Legendre polynomials, Hermite polynomials, Bessel functions, Laguerre polynomials.

**Demonstration.** Substituting y = Σ aₙxⁿ into an equation like y″ − 2x y′ + 2n y = 0 (Hermite's equation) yields a recursion aₖ₊₂ = [2(k−n)/((k+1)(k+2))] aₖ that terminates into polynomials — the Hermite polynomials.

**Application.** These aren't abstract: **Hermite polynomials are the quantum harmonic oscillator wavefunctions**, **Legendre polynomials/spherical harmonics describe angular momentum**, and **Laguerre polynomials appear in the hydrogen atom's radial part** (all Phase 3). Meeting them now means recognizing them later instead of being ambushed.

---

## 4. Partial Differential Equations & Separation of Variables ⭐

**Definition.** A PDE involves partial derivatives in several variables. The workhorse technique is **separation of variables**: assume the solution factorizes, e.g. u(x,t) = X(x)T(t), turning one PDE into several ODEs. The three canonical PDEs of physics:
- **Wave equation:** ∂²u/∂t² = c²∇²u
- **Heat/diffusion equation:** ∂u/∂t = D∇²u
- **Laplace's equation:** ∇²u = 0

**Demonstration.** Heat equation on a rod, u(x,t) = X(x)T(t):

  X T′ = D X″ T → T′/(D T) = X″/X = −λ (a constant).

This splits into T′ = −Dλ T (giving T ∝ e^{−Dλt}) and X″ = −λX (giving sines/cosines). The full solution is a superposition of modes e^{−Dλt} sin(√λ x).

**Application.** The **Schrödinger equation separates** into a spatial part (the time-independent Schrödinger equation) and a temporal part e^{−iEt/ℏ} by exactly this method (Phase 3). **Laplace's equation** is the electrostatics boundary-value problem you'll solve in Phase 1. The same separation logic recurs throughout the curriculum.

---

## Module 0.3 Self-Test (blank page)

1. Solve dy/dx = −ky and identify the physical situations it models.
2. Solve y″ + ω²y = 0 and y″ + 2γy′ + ω₀²y = 0; classify the damping regimes.
3. Name the special functions tied to the oscillator, angular momentum, and hydrogen.
4. Separate the heat equation into ODEs and write the mode solution.
5. Explain how separation of variables applies to the Schrödinger equation.

If solid, advance to **[Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md)**.

---

← *Phase 0 index: [Mathematical Foundations](./README.md)* · Next: [Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md) →

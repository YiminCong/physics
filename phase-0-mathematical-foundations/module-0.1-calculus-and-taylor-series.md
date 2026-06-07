# Module 0.1 — Calculus & Taylor Series

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Calculus is the grammar of change; Taylor series is the art of approximation. Together they underlie every equation of motion, every wave function, and every thermodynamic identity in the curriculum.

---

## 1. Differentiation & Integration

**Definition.** The **derivative** f′(x) = lim_{h→0} [f(x+h) − f(x)] / h measures the instantaneous rate of change of f — geometrically, the slope of the tangent. The **integral** ∫_a^b f(x) dx is the signed area under the curve, defined as a limit of Riemann sums. The **Fundamental Theorem of Calculus** links them: if F′ = f, then ∫_a^b f(x) dx = F(b) − F(a). Differentiation and integration are inverse operations.

**Demonstration.** Differentiate f(x) = xⁿ by the power rule: f′(x) = n xⁿ⁻¹. Integrate: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C (n ≠ −1). For exponentials: d/dx(eˣ) = eˣ — the defining self-referential property that makes exponentials central to all of physics.

**Application.** Newton's second law F = ma is a second-order ODE: knowing the force means integrating twice to find position. The work–energy theorem ΔKE = ∫ F·dx is the Fundamental Theorem applied to mechanics. Accumulation — of charge, probability, heat — is always an integral. Rate of change — of momentum, entropy, field — is always a derivative.

---

## 2. Taylor Series ⭐

This is one of the most load-bearing tools in the entire curriculum. Virtually every approximation scheme in physics — small oscillations, weak fields, perturbation theory — is a Taylor expansion in disguise.

**Definition.** Any sufficiently smooth function can be expanded around a point a as

  f(x) = Σ_{n=0}^{∞} f⁽ⁿ⁾(a) (x−a)ⁿ / n!

The most important special cases (all expanded around 0):

| Function | Series |
|----------|--------|
| eˣ | 1 + x + x²/2! + x³/3! + … = Σ xⁿ/n! |
| sin x | x − x³/3! + x⁵/5! − … |
| cos x | 1 − x²/2! + x⁴/4! − … |
| (1+x)ⁿ | 1 + nx + n(n−1)x²/2! + … ≈ 1 + nx for |x| ≪ 1 |
| ln(1+x) | x − x²/2 + x³/3 − … |

**Demonstration.** The **small-angle approximation**: for θ ≪ 1 (in radians), sin θ = θ − θ³/6 + … ≈ θ. This single truncation turns the nonlinear pendulum equation θ″ + (g/L) sin θ = 0 into the solvable linear equation θ″ + (g/L) θ = 0. Similarly cos θ ≈ 1 − θ²/2, used constantly in optics and relativity. **Linearization** — retaining only first-order terms — is how physicists convert hard problems into tractable ones.

**Application.** The series eˣ = Σ xⁿ/n! is its own derivative term-by-term, confirming d/dx(eˣ) = eˣ — this feeds directly into every ODE whose solution is exponential (Module 0.3) and, via substitution of iθ, into Euler's formula e^{iθ} = cos θ + i sin θ that anchors complex analysis (Module 0.4). The **Gaussian integral** ∫_{−∞}^{∞} e^{−x²} dx = √π is a cornerstone result: it underpins the normalization of wave packets and probability distributions (Module 0.5) and recurs throughout statistical mechanics and QFT. The binomial expansion (1+x)ⁿ ≈ 1 + nx for |x| ≪ 1 appears in special relativity when v/c ≪ 1, in perturbation theory, and in weak-field expansions of the metric (Phase 7).

---

## Module 0.1 Self-Test (blank page)

1. State the Fundamental Theorem of Calculus and use it to evaluate ∫_0^1 3x² dx.
2. Differentiate e^{ax} sin(bx) using the product rule.
3. Write the Taylor expansion of eˣ, sin x, and cos x to three non-zero terms.
4. Use the small-angle approximation to linearize the pendulum equation and state its solution.
5. Explain why d/dx(eˣ) = eˣ makes exponentials the natural solutions to constant-coefficient ODEs, and name the other module that builds directly on eˣ via substitution of iθ.

---

← [Phase 0 index](./README.md) · Next: [Module 0.2 — Linear Algebra](./module-0.2-linear-algebra.md) →

# Module 0.4 — Complex Analysis ⭐

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Complex numbers aren't a mathematical curiosity in physics — quantum amplitudes are
intrinsically complex, and the *phase* of a complex number is what carries interference,
currents, and (in Phase 5) superconductivity itself.

---

## 1. Complex Numbers

**Definition.** A complex number is z = a + bi, where i² = −1; a is the real part, b the imaginary part. The **complex conjugate** is z* = a − bi, and the **modulus** is |z| = √(a² + b²), with |z|² = z z*.

**Demonstration.** (1 + i)(2 − i) = 2 − i + 2i − i² = 2 + i + 1 = **3 + i**. And |3 + 4i| = √(9 + 16) = **5**.

**Application.** Quantum probability **amplitudes** are complex numbers; the physically observable probability is |amplitude|² = (amplitude)(amplitude)*. Complex conjugation is built into the QM inner product.

---

## 2. Euler's Formula ⭐

**Definition.** The bridge between exponentials and trigonometry:

  **e^{iθ} = cos θ + i sin θ.**

This gives the **polar form** z = r e^{iθ}, where r = |z| and θ is the phase angle. A famous special case: e^{iπ} + 1 = 0.

**Demonstration.** From the Taylor series (Module 0.1): substitute iθ into eˣ = Σ xⁿ/n!. The real terms reassemble into cos θ and the imaginary terms into i sin θ. Multiplication then **adds phases**: (r₁e^{iθ₁})(r₂e^{iθ₂}) = r₁r₂ e^{i(θ₁+θ₂)}.

**Application.** Plane-wave wavefunctions are written e^{i(kx − ωt)} — the phase encodes momentum and energy (Phase 3). In superconductivity the **order parameter** is ψ = |ψ| e^{iφ}; the *rigidity of that phase φ* across the material is precisely what drives dissipationless supercurrents and the Josephson effect (Phase 5). Phase is not optional bookkeeping — it's physics.

---

## 3. Functions of a Complex Variable & Analyticity

**Definition.** A function f(z) is **analytic** (holomorphic) in a region if it is complex-differentiable there. Writing f = u(x,y) + i v(x,y), analyticity requires the **Cauchy–Riemann equations**: ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. Analytic functions are extraordinarily well-behaved (infinitely differentiable, determined by their values on a boundary).

**Demonstration.** Check f(z) = z² = (x² − y²) + i(2xy). Here u = x²−y², v = 2xy. Then ∂u/∂x = 2x = ∂v/∂y, and ∂u/∂y = −2y = −∂v/∂x. Cauchy–Riemann satisfied → z² is analytic.

**Application.** Analyticity underlies **response functions** and **dispersion relations** in many-body physics: the fact that a system can't respond before it's perturbed (causality) forces the response function to be analytic in the upper half-plane, which links its real and imaginary parts (Phase 6).

---

## 4. Contour Integration & the Residue Theorem

**Definition.** Integrals along paths ("contours") in the complex plane. The **residue theorem** states that a closed-contour integral equals 2πi times the sum of **residues** (coefficients of the 1/(z−z₀) term) at the poles enclosed:

  ∮_C f(z) dz = 2πi Σ Res(f, zₖ).

**Demonstration.** ∮ dz/z around a loop enclosing the origin: the residue of 1/z at z = 0 is 1, so the integral is **2πi**. This trick converts many hard *real* integrals into simple residue sums.

**Application.** Contour integration is the standard tool for evaluating integrals in quantum field theory and many-body physics, and it's how **Green's functions** and the **Kramers–Kronig relations** are handled (Phase 6). You won't need it heavily until the advanced phase, but recognizing it now pays off.

---

## Module 0.4 Self-Test (blank page)

1. Multiply two complex numbers and compute a modulus.
2. State Euler's formula and derive it from Taylor series; show that multiplication adds phases.
3. Write a plane wave in complex form and explain what its phase encodes.
4. Verify the Cauchy–Riemann equations for f(z) = z².
5. Evaluate ∮ dz/z around the origin using residues.

If solid, advance to **Module 0.5 — Fourier Analysis & Probability**.

---

← Previous: [Module 0.3 — Differential Equations](./module-0.3-differential-equations.md) · *Phase 0 index: [Mathematical Foundations](./README.md)*

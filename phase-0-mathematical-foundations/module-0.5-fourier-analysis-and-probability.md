# Module 0.5 — Fourier Analysis & Probability ⭐

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application

Fourier analysis decomposes complexity into frequencies; probability quantifies uncertainty. In quantum mechanics these two ideas merge — the Fourier relationship between position and momentum *is* the uncertainty principle, and probability amplitudes *are* the quantities being decomposed.

---

## 1. Fourier Series & Transforms

**Definition.** Any periodic function f(x) of period L can be written as a **Fourier series** — a superposition of sines and cosines (or complex exponentials):

  f(x) = Σ_{n=−∞}^{∞} cₙ e^{i 2πnx/L},   cₙ = (1/L) ∫_0^L f(x) e^{−i 2πnx/L} dx.

For non-periodic functions on the full real line, the discrete sum becomes a continuous integral — the **Fourier transform** and its inverse:

  f̃(k) = ∫_{−∞}^{∞} f(x) e^{−ikx} dx,   f(x) = (1/2π) ∫_{−∞}^{∞} f̃(k) e^{ikx} dk.

The **Dirac delta** δ(x) is the identity element of this transform: δ̃(k) = 1, meaning it contains all frequencies equally. It satisfies ∫ δ(x−a) f(x) dx = f(a) and can be represented as δ(x) = (1/2π) ∫ eⁱᵏˣ dk. The **convolution theorem** states that (f * g)~ = f̃ · g̃: convolution in real space is pointwise multiplication in frequency space, and vice versa.

**Demonstration.** The Fourier transform of a **Gaussian** f(x) = e^{−x²/2σ²} is another Gaussian:

  f̃(k) = σ√(2π) e^{−σ²k²/2}.

When σ is large (broad in x), f̃ is narrow in k. When σ is small (narrow in x), f̃ is wide in k. Quantitatively, Δx · Δk ≥ 1/2. This **reciprocal spread** is a mathematical identity of Fourier pairs — it has nothing to do with measurement disturbance yet. Its physical interpretation arrives in Module 3.1.

**Application.** In quantum mechanics, the momentum-space wavefunction ψ̃(p) is exactly the Fourier transform of the position-space wavefunction ψ(x), with k = p/ℏ (Module 3.1). The Gaussian demonstration above is then the Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2. In condensed matter, the **reciprocal lattice** is the Fourier transform of the crystal's Bravais lattice, and Bragg diffraction is Fourier analysis of the charge density (Module 4.2). The convolution theorem underpins how detectors and sources broaden spectral lines.

---

## 2. Probability

**Definition.** A **random variable** X has a **probability density** p(x) (with p(x) ≥ 0 and ∫p(x)dx = 1). The **mean** (expectation value) and **variance** are:

  ⟨x⟩ = ∫ x p(x) dx,   σ² = ⟨(x − ⟨x⟩)²⟩ = ⟨x²⟩ − ⟨x⟩².

The standard deviation σ = √(⟨x²⟩ − ⟨x⟩²) measures the spread. The **Gaussian (normal) distribution** with mean μ and standard deviation σ is

  p(x) = (1/σ√(2π)) e^{−(x−μ)²/2σ²}.

It is its own Fourier transform (up to rescaling), normalized to 1, and maximizes entropy for fixed mean and variance. The **central limit theorem** states that the sum of many independent random variables — regardless of their individual distributions — converges in distribution to a Gaussian.

**Application.** In quantum mechanics, |ψ(x)|² is a probability density: the expectation value of position is ⟨x⟩ = ∫ x|ψ|² dx and the uncertainty Δx = √(⟨x²⟩ − ⟨x⟩²) is exactly the standard deviation applied to |ψ|² (Module 3.1). The central limit theorem explains why the Gaussian appears in thermal noise, diffusion, and the ground-state wavefunction of the harmonic oscillator. The **density of states** — the probability density of finding an energy level near E — feeds directly into Fermi's golden rule for transition rates (Module 3.8) and into the Fermi–Dirac and Bose–Einstein distributions in statistical mechanics.

---

## Module 0.5 Self-Test (blank page)

1. Write the Fourier transform pair and state the convolution theorem.
2. Show that the FT of a Gaussian is a Gaussian and explain the reciprocal-spread result.
3. Define ⟨x⟩, ⟨x²⟩, and σ² for a continuous distribution; compute them for p(x) = e^{−x} on [0,∞).
4. Explain in one sentence how the Gaussian FT result becomes the Heisenberg uncertainty principle.
5. State the central limit theorem and give two physics contexts where it explains a Gaussian appearing.

---

← Previous: [Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md) · [Phase 0 index](./README.md) · Next: [Module 0.6 — Vector Calculus, Tensors & Differential Forms](./module-0.6-vector-calculus-tensors-and-differential-forms.md) →

# Module 0.5 — Fourier Analysis & Probability ⭐
**模块 0.5 — 傅里叶分析与概率 ⭐**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用

Fourier analysis decomposes complexity into frequencies; probability quantifies uncertainty. In quantum mechanics these two ideas merge — the Fourier relationship between position and momentum *is* the uncertainty principle, and probability amplitudes *are* the quantities being decomposed.

傅里叶分析将复杂性分解为频率成分；概率论量化不确定性。在量子力学中，这两个概念合而为一——位置与动量之间的傅里叶关系*就是*不确定性原理，而概率幅*正是*被分解的量。

---

## 1. Fourier Series & Transforms · 傅里叶级数与傅里叶变换

**Definition.** Any periodic function f(x) of period L can be written as a **Fourier series** — a superposition of sines and cosines (or complex exponentials):

**定义。** 任何周期为 L 的周期函数 f(x) 都可以写成**傅里叶级数**——正弦和余弦（或复指数）的叠加：

  f(x) = Σ_{n=−∞}^{∞} cₙ e^{i 2πnx/L},   cₙ = (1/L) ∫_0^L f(x) e^{−i 2πnx/L} dx.

For non-periodic functions on the full real line, the discrete sum becomes a continuous integral — the **Fourier transform** and its inverse:

对于全实数轴上的非周期函数，离散求和变为连续积分——即**傅里叶变换**及其逆变换：

  f̃(k) = ∫_{−∞}^{∞} f(x) e^{−ikx} dx,   f(x) = (1/2π) ∫_{−∞}^{∞} f̃(k) e^{ikx} dk.

The **Dirac delta** δ(x) is the identity element of this transform: δ̃(k) = 1, meaning it contains all frequencies equally. It satisfies ∫ δ(x−a) f(x) dx = f(a) and can be represented as δ(x) = (1/2π) ∫ eⁱᵏˣ dk. The **convolution theorem** states that (f * g)~ = f̃ · g̃: convolution in real space is pointwise multiplication in frequency space, and vice versa.

**狄拉克 delta 函数** δ(x) 是该变换的恒等元素：δ̃(k) = 1，意味着它均匀地包含所有频率。它满足 ∫ δ(x−a) f(x) dx = f(a)，可以表示为 δ(x) = (1/2π) ∫ eⁱᵏˣ dk。**卷积定理**指出 (f * g)~ = f̃ · g̃：实空间中的卷积对应频率空间中的逐点相乘，反之亦然。

**Demonstration.** The Fourier transform of a **Gaussian** f(x) = e^{−x²/2σ²} is another Gaussian:

**演示。** **高斯函数** f(x) = e^{−x²/2σ²} 的傅里叶变换仍是高斯函数：

  f̃(k) = σ√(2π) e^{−σ²k²/2}.

When σ is large (broad in x), f̃ is narrow in k. When σ is small (narrow in x), f̃ is wide in k. Quantitatively, Δx · Δk ≥ 1/2. This **reciprocal spread** is a mathematical identity of Fourier pairs — it has nothing to do with measurement disturbance yet. Its physical interpretation arrives in Module 3.1.

当 σ 较大（x 空间中较宽）时，f̃ 在 k 空间中较窄。当 σ 较小（x 空间中较窄）时，f̃ 在 k 空间中较宽。定量地，Δx · Δk ≥ 1/2。这一**互反展宽**是傅里叶变换对的数学恒等式——与测量扰动无关。其物理解释将在模块 3.1 中给出。

**Application.** In quantum mechanics, the momentum-space wavefunction ψ̃(p) is exactly the Fourier transform of the position-space wavefunction ψ(x), with k = p/ℏ (Module 3.1). The Gaussian demonstration above is then the Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2. In condensed matter, the **reciprocal lattice** is the Fourier transform of the crystal's Bravais lattice, and Bragg diffraction is Fourier analysis of the charge density (Module 4.2). The convolution theorem underpins how detectors and sources broaden spectral lines.

**应用。** 在量子力学中，动量空间波函数 ψ̃(p) 恰好是位置空间波函数 ψ(x) 的傅里叶变换，其中 k = p/ℏ（模块 3.1）。上述高斯函数演示由此成为海森堡不确定性原理 ΔxΔp ≥ ℏ/2。在凝聚态物理中，**倒格子**是晶体布拉维格子的傅里叶变换，布拉格衍射是对电荷密度进行傅里叶分析（模块 4.2）。卷积定理是探测器和光源展宽谱线的基本原理。

---

## 2. Probability · 概率

**Definition.** A **random variable** X has a **probability density** p(x) (with p(x) ≥ 0 and ∫p(x)dx = 1). The **mean** (expectation value) and **variance** are:

**定义。** **随机变量** X 具有**概率密度** p(x)（满足 p(x) ≥ 0 且 ∫p(x)dx = 1）。**均值**（期望值）和**方差**为：

  ⟨x⟩ = ∫ x p(x) dx,   σ² = ⟨(x − ⟨x⟩)²⟩ = ⟨x²⟩ − ⟨x⟩².

The standard deviation σ = √(⟨x²⟩ − ⟨x⟩²) measures the spread. The **Gaussian (normal) distribution** with mean μ and standard deviation σ is

标准差 σ = √(⟨x²⟩ − ⟨x⟩²) 衡量分布的展宽。均值为 μ、标准差为 σ 的**高斯（正态）分布**为

  p(x) = (1/σ√(2π)) e^{−(x−μ)²/2σ²}.

It is its own Fourier transform (up to rescaling), normalized to 1, and maximizes entropy for fixed mean and variance. The **central limit theorem** states that the sum of many independent random variables — regardless of their individual distributions — converges in distribution to a Gaussian.

它是自身的傅里叶变换（相差一个缩放因子），归一化为 1，并且在固定均值和方差的条件下使熵最大。**中心极限定理**指出，许多独立随机变量之和——无论各自的分布如何——在分布上收敛到高斯分布。

**Application.** In quantum mechanics, |ψ(x)|² is a probability density: the expectation value of position is ⟨x⟩ = ∫ x|ψ|² dx and the uncertainty Δx = √(⟨x²⟩ − ⟨x⟩²) is exactly the standard deviation applied to |ψ|² (Module 3.1). The central limit theorem explains why the Gaussian appears in thermal noise, diffusion, and the ground-state wavefunction of the harmonic oscillator. The **density of states** — the probability density of finding an energy level near E — feeds directly into Fermi's golden rule for transition rates (Module 3.8) and into the Fermi–Dirac and Bose–Einstein distributions in statistical mechanics.

**应用。** 在量子力学中，|ψ(x)|² 是概率密度：位置的期望值为 ⟨x⟩ = ∫ x|ψ|² dx，不确定度 Δx = √(⟨x²⟩ − ⟨x⟩²) 恰好是对 |ψ|² 应用的标准差（模块 3.1）。中心极限定理解释了为何高斯分布出现在热噪声、扩散以及谐振子基态波函数中。**态密度**——在能量 E 附近找到能级的概率密度——直接进入费米黄金规则（模块 3.8）以及统计力学中的费米–狄拉克和玻色–爱因斯坦分布。

---

## Module 0.5 Self-Test (blank page)

1. Write the Fourier transform pair and state the convolution theorem.
2. Show that the FT of a Gaussian is a Gaussian and explain the reciprocal-spread result.
3. Define ⟨x⟩, ⟨x²⟩, and σ² for a continuous distribution; compute them for p(x) = e^{−x} on [0,∞).
4. Explain in one sentence how the Gaussian FT result becomes the Heisenberg uncertainty principle.
5. State the central limit theorem and give two physics contexts where it explains a Gaussian appearing.

**自测（空白页）**

1. 写出傅里叶变换对，并陈述卷积定理。
2. 证明高斯函数的傅里叶变换仍是高斯函数，并解释互反展宽结果。
3. 为连续分布定义 ⟨x⟩、⟨x²⟩ 和 σ²；对 [0,∞) 上的 p(x) = e^{−x} 计算它们。
4. 用一句话解释高斯函数的傅里叶变换结果如何成为海森堡不确定性原理。
5. 陈述中心极限定理，并给出两个物理情景，说明其中高斯分布为何出现。

---

← Previous: [Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md) · [Phase 0 index](./README.md) · Next: [Module 0.6 — Vector Calculus, Tensors & Differential Forms](./module-0.6-vector-calculus-tensors-and-differential-forms.md) →

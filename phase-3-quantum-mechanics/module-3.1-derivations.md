# Derivations — Module 3.1: The Wave Function
# 推导 — 模块 3.1：波函数

> Companion to [Module 3.1](./module-3.1-the-wave-function.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.1](./module-3.1-the-wave-function.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Continuity Equation: ∂|ψ|²/∂t + ∂j/∂x = 0 · 连续性方程

**Claim.** From the Schrödinger equation iℏ ∂ψ/∂t = −(ℏ²/2m)∂²ψ/∂x² + Vψ (with V real), the probability density ρ = |ψ|² and the probability current j = (ℏ/2mi)(ψ* ∂ψ/∂x − ψ ∂ψ*/∂x) satisfy the local conservation law ∂ρ/∂t + ∂j/∂x = 0.

**命题。** 由薛定谔方程 iℏ ∂ψ/∂t = −(ℏ²/2m)∂²ψ/∂x² + Vψ（V 为实数），概率密度 ρ = |ψ|² 与概率流密度 j = (ℏ/2mi)(ψ* ∂ψ/∂x − ψ ∂ψ*/∂x) 满足局域守恒律 ∂ρ/∂t + ∂j/∂x = 0。

**Step 1 — Write down the Schrödinger equation and its complex conjugate.** Let Ĥ = −(ℏ²/2m)∂²/∂x² + V(x,t). The Schrödinger equation and its complex conjugate are (using real V):

**第 1 步 — 写出薛定谔方程及其复共轭。** 令 Ĥ = −(ℏ²/2m)∂²/∂x² + V(x,t)。薛定谔方程及其复共轭为（利用 V 为实数）：

  iℏ ∂ψ/∂t = −(ℏ²/2m) ψ_xx + V ψ,                … (SE)
  −iℏ ∂ψ*/∂t = −(ℏ²/2m) ψ*_xx + V ψ*.              … (SE*)

**Step 2 — Differentiate ρ = ψ*ψ with respect to t.**

**第 2 步 — 对 ρ = ψ*ψ 关于 t 求导。**

  ∂ρ/∂t = ∂(ψ*ψ)/∂t = (∂ψ*/∂t)ψ + ψ*(∂ψ/∂t).

From (SE): ∂ψ/∂t = (1/iℏ)[−(ℏ²/2m)ψ_xx + Vψ] = (iℏ/2m)ψ_xx − (iV/ℏ)ψ.
From (SE*): ∂ψ*/∂t = −(iℏ/2m)ψ*_xx + (iV/ℏ)ψ*.

由 (SE)：∂ψ/∂t = (iℏ/2m)ψ_xx − (iV/ℏ)ψ。
由 (SE*)：∂ψ*/∂t = −(iℏ/2m)ψ*_xx + (iV/ℏ)ψ*。

**Step 3 — Substitute.** Insert these into ∂ρ/∂t:

**第 3 步 — 代入。** 将它们代入 ∂ρ/∂t：

  ∂ρ/∂t = [(−iℏ/2m)ψ*_xx + (iV/ℏ)ψ*]ψ + ψ*[(iℏ/2m)ψ_xx − (iV/ℏ)ψ].

The potential terms cancel (V is real):

势能项消去（V 为实数）：

  ∂ρ/∂t = (iℏ/2m)(ψ* ψ_xx − ψ*_xx ψ).

**Step 4 — Recognize a divergence.** Notice that:

**第 4 步 — 识别散度结构。** 注意到：

  ∂/∂x (ψ* ψ_x − ψ*_x ψ) = ψ*_x ψ_x + ψ* ψ_xx − ψ*_xx ψ − ψ*_x ψ_x = ψ* ψ_xx − ψ*_xx ψ.

Therefore:

因此：

  ∂ρ/∂t = (iℏ/2m) ∂/∂x (ψ* ψ_x − ψ*_x ψ) = −∂j/∂x,

where we define:

其中定义：

  **j = −(iℏ/2m)(ψ* ∂ψ/∂x − ψ ∂ψ*/∂x) = (ℏ/2mi)(ψ* ψ_x − ψ*_x ψ)**.

(Note: the two forms are identical since 1/(2mi) = −i/(2m) = −(i/2m).)

（注：两种形式等价，因为 1/(2mi) = −i/(2m) = −(i/2m)。）

**Step 5 — Write the continuity equation.**

**第 5 步 — 写出连续性方程。**

  **∂ρ/∂t + ∂j/∂x = 0**. ∎

**Step 6 — Global conservation (normalization is preserved).** Integrate over all x:

**第 6 步 — 整体守恒（归一化守恒）。** 对全空间积分：

  d/dt ∫₋∞^∞ |ψ|² dx = −[j]₋∞^∞ = 0,

since ψ → 0 as |x| → ∞ for normalizable states, so j → 0. Thus if ∫|ψ|² dx = 1 at t = 0, it remains 1 for all t. ∎

因为对可归一化的态，当 |x| → ∞ 时 ψ → 0，所以 j → 0。因此若 ∫|ψ|² dx = 1 在 t = 0 时成立，则对所有 t 均成立。∎

---

## B. Ehrenfest Theorem: d⟨x⟩/dt = ⟨p⟩/m · 埃伦费斯特定理

**Claim.** For a particle governed by the Schrödinger equation, d⟨x⟩/dt = ⟨p̂⟩/m, where ⟨x⟩ = ∫ ψ* x ψ dx and ⟨p̂⟩ = ∫ ψ* (−iℏ ∂/∂x) ψ dx.

**命题。** 对由薛定谔方程控制的粒子，d⟨x⟩/dt = ⟨p̂⟩/m，其中 ⟨x⟩ = ∫ ψ* x ψ dx，⟨p̂⟩ = ∫ ψ* (−iℏ ∂/∂x) ψ dx。

**Step 1 — Differentiate ⟨x⟩ under the integral sign.**

**第 1 步 — 在积分号下对 ⟨x⟩ 求导。**

  d⟨x⟩/dt = d/dt ∫ ψ* x ψ dx = ∫ (∂ψ*/∂t · x ψ + ψ* · x · ∂ψ/∂t) dx.

**Step 2 — Use the Schrödinger equation.** Substitute ∂ψ/∂t = (iℏ/2m)ψ_xx − (i/ℏ)Vψ and ∂ψ*/∂t = −(iℏ/2m)ψ*_xx + (i/ℏ)Vψ*:

**第 2 步 — 利用薛定谔方程。** 代入 ∂ψ/∂t = (iℏ/2m)ψ_xx − (i/ℏ)Vψ 和 ∂ψ*/∂t = −(iℏ/2m)ψ*_xx + (i/ℏ)Vψ*：

  d⟨x⟩/dt = ∫ [−(iℏ/2m)ψ*_xx + (i/ℏ)Vψ*] x ψ dx
             + ∫ ψ* x [(iℏ/2m)ψ_xx − (i/ℏ)Vψ] dx.

The potential terms ±(i/ℏ)V |ψ|² cancel (V is real):

势能项 ±(i/ℏ)V |ψ|² 消去（V 为实数）：

  d⟨x⟩/dt = (iℏ/2m) ∫ x (ψ* ψ_xx − ψ*_xx ψ) dx.

**Step 3 — Integrate by parts.** Integrate the term ∫ x ψ*_xx ψ dx by parts twice. First integration by parts on ∫ x ψ*_xx ψ dx (integrate ψ*_xx, differentiate xψ):

**第 3 步 — 分部积分。** 对 ∫ x ψ*_xx ψ dx 进行两次分部积分。第一次分部积分（对 ψ*_xx 积分，对 xψ 微分）：

  ∫ x ψ*_xx ψ dx = [x ψ*_x ψ]₋∞^∞ − ∫ ψ*_x (ψ + x ψ_x) dx = − ∫ ψ*_x ψ dx − ∫ x ψ*_x ψ_x dx.

Similarly, integrate by parts on ∫ x ψ* ψ_xx dx (integrate ψ_xx, differentiate xψ*):

类似地，对 ∫ x ψ* ψ_xx dx 分部积分（对 ψ_xx 积分，对 xψ* 微分）：

  ∫ x ψ* ψ_xx dx = [x ψ* ψ_x]₋∞^∞ − ∫ ψ_x (ψ* + x ψ*_x) dx = − ∫ ψ_x ψ* dx − ∫ x ψ*_x ψ_x dx.

(Boundary terms vanish for normalizable ψ.)

（对可归一化的 ψ，边界项为零。）

Therefore:

因此：

  ψ* ψ_xx − ψ*_xx ψ integrated against x gives:

  ∫ x (ψ* ψ_xx − ψ*_xx ψ) dx = (−∫ ψ_x ψ* dx − ∫ x ψ*_x ψ_x dx) − (−∫ ψ*_x ψ dx − ∫ x ψ*_x ψ_x dx)

  = −∫ ψ* ψ_x dx + ∫ ψ*_x ψ dx = ∫ (ψ*_x ψ − ψ* ψ_x) dx.

**Step 4 — Further simplification.** Note that ∫ ψ*_x ψ dx = −∫ ψ* ψ_x dx by integration by parts (boundary term = 0):

**第 4 步 — 进一步化简。** 注意通过分部积分 ∫ ψ*_x ψ dx = −∫ ψ* ψ_x dx（边界项 = 0）：

  ∫ (ψ*_x ψ − ψ* ψ_x) dx = −∫ ψ* ψ_x dx − ∫ ψ* ψ_x dx = −2 ∫ ψ* ψ_x dx.

Therefore:

因此：

  d⟨x⟩/dt = (iℏ/2m)(−2) ∫ ψ* ψ_x dx = −(iℏ/m) ∫ ψ* (∂ψ/∂x) dx.

Recognizing p̂ = −iℏ ∂/∂x:

识别 p̂ = −iℏ ∂/∂x：

  d⟨x⟩/dt = (1/m) ∫ ψ* (−iℏ ∂ψ/∂x) dx = **⟨p̂⟩/m**. ∎

---

## C. Expectation Value and Uncertainty: ⟨Q⟩ and ΔQ · 期望值与不确定性：⟨Q⟩ 与 ΔQ

**Claim.** For any observable Q with operator Q̂, ⟨Q⟩ = ∫ ψ* Q̂ ψ dx is a real number (for Hermitian Q̂), and the spread ΔQ = √(⟨Q²⟩ − ⟨Q⟩²) is well-defined and non-negative.

**命题。** 对任意可观测量 Q（算符 Q̂），⟨Q⟩ = ∫ ψ* Q̂ ψ dx 是实数（对厄米 Q̂），散布 ΔQ = √(⟨Q²⟩ − ⟨Q⟩²) 定义良好且非负。

**Step 1 — Reality of ⟨Q⟩.** Q̂ is Hermitian means ⟨φ|Q̂ψ⟩ = ⟨Q̂φ|ψ⟩ for all φ, ψ in the domain. Take φ = ψ:

**第 1 步 — ⟨Q⟩ 的实性。** Q̂ 是厄米的意味着对定义域内所有 φ、ψ 有 ⟨φ|Q̂ψ⟩ = ⟨Q̂φ|ψ⟩。取 φ = ψ：

  ⟨Q⟩ = ∫ ψ* Q̂ ψ dx = ⟨ψ|Q̂ψ⟩ = ⟨Q̂ψ|ψ⟩ = (∫ ψ* Q̂ ψ dx)* = ⟨Q⟩*.

Therefore ⟨Q⟩ is real. ∎

因此 ⟨Q⟩ 为实数。∎

**Step 2 — Non-negativity of ΔQ.** Compute ⟨Q²⟩ − ⟨Q⟩²:

**第 2 步 — ΔQ 的非负性。** 计算 ⟨Q²⟩ − ⟨Q⟩²：

  ΔQ² = ⟨Q²⟩ − ⟨Q⟩² = ⟨(Q̂ − ⟨Q⟩)²⟩ = ⟨ψ|(Q̂ − ⟨Q⟩)²|ψ⟩.

Define the shifted operator Q̃ = Q̂ − ⟨Q⟩ (which is also Hermitian). Then:

定义移位算符 Q̃ = Q̂ − ⟨Q⟩（它也是厄米的）。则：

  ΔQ² = ⟨ψ|Q̃²|ψ⟩ = ⟨ψ|Q̃†Q̃|ψ⟩ = ⟨Q̃ψ|Q̃ψ⟩ = ‖Q̃ψ‖² ≥ 0.

(Used Q̃† = Q̃ and the definition of inner product.) Therefore ΔQ = ‖Q̃ψ‖ ≥ 0. ∎

（利用了 Q̃† = Q̃ 和内积的定义。）因此 ΔQ = ‖Q̃ψ‖ ≥ 0。∎

---

## D. Gaussian Wave Packet Saturates the Uncertainty Principle · 高斯波包使不确定性原理取等

**Claim.** For the normalized Gaussian wave function ψ(x) = (2πσ²)^{−1/4} exp(−x²/(4σ²)) exp(ip₀x/ℏ), we have ⟨x⟩ = 0, ⟨p⟩ = p₀, Δx = σ, Δp = ℏ/(2σ), and hence Δx·Δp = ℏ/2 — the minimum uncertainty state.

**命题。** 对于归一化高斯波函数 ψ(x) = (2πσ²)^{−1/4} exp(−x²/(4σ²)) exp(ip₀x/ℏ)，有 ⟨x⟩ = 0、⟨p⟩ = p₀、Δx = σ、Δp = ℏ/(2σ)，从而 Δx·Δp = ℏ/2——最小不确定性态。

**Step 1 — Normalization check.** With ρ(x) = |ψ(x)|² = (2πσ²)^{−1/2} exp(−x²/(2σ²)):

**第 1 步 — 归一化验证。** 以 ρ(x) = |ψ(x)|² = (2πσ²)^{−1/2} exp(−x²/(2σ²))：

  ∫₋∞^∞ ρ dx = (2πσ²)^{−1/2} ∫₋∞^∞ e^{−x²/(2σ²)} dx = (2πσ²)^{−1/2} · √(2πσ²) = 1. ✓

(Used the Gaussian integral ∫₋∞^∞ e^{−ax²} dx = √(π/a) with a = 1/(2σ²).)

（利用高斯积分 ∫₋∞^∞ e^{−ax²} dx = √(π/a)，取 a = 1/(2σ²)。）

**Step 2 — Position expectation.** Since |ψ|² is symmetric (even function of x):

**第 2 步 — 位置期望值。** 由于 |ψ|² 是对称函数（x 的偶函数）：

  ⟨x⟩ = ∫ x |ψ|² dx = 0  (odd integrand over symmetric domain).

**第 2 步 — 位置期望值。** ⟨x⟩ = 0（被积函数为奇函数，积分区间对称）。

**Step 3 — ⟨x²⟩.** Using the Gaussian moment integral ∫₋∞^∞ x² e^{−x²/(2σ²)} dx = σ² √(2πσ²):

**第 3 步 — ⟨x²⟩。** 利用高斯矩积分 ∫₋∞^∞ x² e^{−x²/(2σ²)} dx = σ² √(2πσ²)：

  ⟨x²⟩ = (2πσ²)^{−1/2} ∫ x² e^{−x²/(2σ²)} dx = (2πσ²)^{−1/2} · σ²√(2πσ²) = σ².

Therefore Δx = √(⟨x²⟩ − ⟨x⟩²) = √(σ² − 0) = **σ**. ∎

**Step 4 — Momentum expectation.** Apply p̂ = −iℏ ∂/∂x:

**第 4 步 — 动量期望值。** 应用 p̂ = −iℏ ∂/∂x：

  ∂ψ/∂x = ψ · [−x/(2σ²) + ip₀/ℏ].

  ⟨p̂⟩ = ∫ ψ* (−iℏ) ψ · [−x/(2σ²) + ip₀/ℏ] dx
        = −iℏ · [−1/(2σ²) ∫ x|ψ|² dx + ip₀/ℏ ∫ |ψ|² dx]
        = −iℏ · [0 + ip₀/ℏ · 1] = p₀. ∎

**Step 5 — ⟨p̂²⟩.** Compute ∂²ψ/∂x²:

**第 5 步 — ⟨p̂²⟩。** 计算 ∂²ψ/∂x²：

  ∂ψ/∂x = ψ·(−x/(2σ²) + ip₀/ℏ),

  ∂²ψ/∂x² = ∂ψ/∂x·(−x/(2σ²) + ip₀/ℏ) + ψ·(−1/(2σ²))
            = ψ·(−x/(2σ²) + ip₀/ℏ)² + ψ·(−1/(2σ²)).

  ⟨p̂²⟩ = ∫ ψ*(−ℏ²) ∂²ψ/∂x² dx = −ℏ² ∫ |ψ|² [(−x/(2σ²) + ip₀/ℏ)² − 1/(2σ²)] dx.

Expand (−x/(2σ²) + ip₀/ℏ)² = x²/(4σ⁴) − ix·p₀/(σ²ℏ) − p₀²/ℏ²:

展开 (−x/(2σ²) + ip₀/ℏ)² = x²/(4σ⁴) − ix·p₀/(σ²ℏ) − p₀²/ℏ²：

  ⟨p̂²⟩ = −ℏ² [⟨x²⟩/(4σ⁴) − i·p₀·⟨x⟩/(σ²ℏ) − p₀²/ℏ² − 1/(2σ²)]
         = −ℏ² [σ²/(4σ⁴) − 0 − p₀²/ℏ² − 1/(2σ²)]
         = −ℏ² [1/(4σ²) − p₀²/ℏ² − 1/(2σ²)]
         = −ℏ² [−1/(4σ²) − p₀²/ℏ²]
         = ℏ²/(4σ²) + p₀².

**Step 6 — Δp and the product.** 

**第 6 步 — Δp 与不确定度积。**

  Δp² = ⟨p̂²⟩ − ⟨p̂⟩² = ℏ²/(4σ²) + p₀² − p₀² = ℏ²/(4σ²).

  Δp = ℏ/(2σ).

  **Δx · Δp = σ · ℏ/(2σ) = ℏ/2**. ∎

This is the absolute minimum allowed by the uncertainty principle (proven in Module 3.3-derivations). The Gaussian packet is the unique state that saturates Δx·Δp = ℏ/2.

这是不确定性原理所允许的绝对最小值（在模块 3.3 推导中证明）。高斯波包是使 Δx·Δp = ℏ/2 取等的唯一态。∎

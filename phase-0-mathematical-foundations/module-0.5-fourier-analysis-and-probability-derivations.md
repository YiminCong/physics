# Derivations — Module 0.5: Fourier Analysis & Probability
# 推导 — 模块 0.5：傅里叶分析与概率

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.5](./module-0.5-fourier-analysis-and-probability.md). Full step-by-step proofs of every non-trivial result: derivation of Fourier coefficients via orthogonality; the Fourier transform of a Gaussian is a Gaussian (completing the square); the convolution theorem; the Dirac delta as a Fourier representation; Var = ⟨x²⟩ − ⟨x⟩²; and the central limit theorem via characteristic functions. English first, then 中文.
> [模块 0.5](./module-0.5-fourier-analysis-and-probability.md) 的配套文档：对每一个非平凡结果进行完整逐步证明：通过正交性推导傅里叶系数；高斯函数的傅里叶变换仍是高斯函数（配方法）；卷积定理；狄拉克 delta 函数的傅里叶表示；Var = ⟨x²⟩ − ⟨x⟩²；以及通过特征函数的中心极限定理。先英文，后中文。

---

## A. Fourier Coefficients from Orthogonality · 从正交性推导傅里叶系数

**Claim.** For a periodic function f(x) of period L, the Fourier coefficients in the expansion f(x) = Σ_{n=−∞}^{∞} cₙ e^{i2πnx/L} are given by

**命题。** 对于周期为 L 的周期函数 f(x)，展开式 f(x) = Σ_{n=−∞}^{∞} cₙ e^{i2πnx/L} 中的傅里叶系数为

  cₙ = (1/L) ∫_0^L f(x) e^{−i2πnx/L} dx.

**Step 1 — Orthogonality of the exponential basis.** The key is the integral

**第 1 步 — 指数基的正交性。** 关键是以下积分

  ∫_0^L e^{i2πmx/L} e^{−i2πnx/L} dx = ∫_0^L e^{i2π(m−n)x/L} dx.

For m = n: the integrand is e⁰ = 1, so the integral equals L.

当 m = n 时：被积函数为 e⁰ = 1，故积分等于 L。

For m ≠ n: let k = m − n ≠ 0. Then

当 m ≠ n 时：令 k = m − n ≠ 0，则

  ∫_0^L e^{i2πkx/L} dx = [L/(i2πk)] e^{i2πkx/L} |_0^L = (L/(i2πk))(e^{i2πk} − 1) = (L/(i2πk))(1 − 1) = 0.

(Here we used e^{i2πk} = 1 for integer k.)

（此处用到整数 k 满足 e^{i2πk} = 1。）

In summary: ∫_0^L e^{i2πmx/L} e^{−i2πnx/L} dx = L δₘₙ.

综上：∫_0^L e^{i2πmx/L} e^{−i2πnx/L} dx = L δₘₙ。

**Step 2 — Extract cₙ.** Multiply both sides of f(x) = Σₘ cₘ e^{i2πmx/L} by e^{−i2πnx/L} and integrate over one period:

**第 2 步 — 提取 cₙ。** 将 f(x) = Σₘ cₘ e^{i2πmx/L} 两端乘以 e^{−i2πnx/L}，并对一个周期积分：

  ∫_0^L f(x) e^{−i2πnx/L} dx = Σₘ cₘ ∫_0^L e^{i2π(m−n)x/L} dx = Σₘ cₘ · L δₘₙ = L cₙ.

(Interchange of sum and integral justified by uniform convergence of the Fourier series on L².)

（求和与积分的交换由傅里叶级数在 L² 上的一致收敛性保证。）

**Step 3 — Solve for cₙ.**

**第 3 步 — 解出 cₙ。**

  **cₙ = (1/L) ∫_0^L f(x) e^{−i2πnx/L} dx.** ∎

**Physical interpretation.** The coefficient cₙ is the "projection" of f onto the n-th mode e^{i2πnx/L}, measuring how much of the frequency 2πn/L is present in f. In quantum mechanics, the same orthogonality argument gives the expansion coefficients of a state in any orthonormal basis.

**物理解释。** 系数 cₙ 是 f 在第 n 个模式 e^{i2πnx/L} 上的"投影"，衡量 f 中频率 2πn/L 的含量。在量子力学中，同样的正交性论证给出态在任意正交归一基下的展开系数。

---

## B. The Fourier Transform of a Gaussian Is a Gaussian · 高斯函数的傅里叶变换仍是高斯函数

**Claim.** For f(x) = e^{−x²/(2σ²)} (a Gaussian with width σ), the Fourier transform is

**命题。** 对 f(x) = e^{−x²/(2σ²)}（宽度为 σ 的高斯函数），傅里叶变换为

  f̃(k) = ∫_{−∞}^{∞} e^{−x²/(2σ²)} e^{−ikx} dx = σ√(2π) e^{−σ²k²/2}.

**Step 1 — Write the integral.** We need to evaluate

**第 1 步 — 写出积分。** 需要计算

  f̃(k) = ∫_{−∞}^{∞} e^{−x²/(2σ²) − ikx} dx.

**Step 2 — Complete the square in the exponent.** The exponent is

**第 2 步 — 对指数配方。** 指数为

  −x²/(2σ²) − ikx = −(1/(2σ²))[x² + 2iσ²kx].

Complete the square inside the bracket:

对方括号内配方：

  x² + 2iσ²kx = (x + iσ²k)² − (iσ²k)² = (x + iσ²k)² + σ⁴k².

So the exponent becomes:

故指数变为：

  −(1/(2σ²))[(x + iσ²k)² + σ⁴k²] = −(x + iσ²k)²/(2σ²) − σ²k²/2.

**Step 3 — Factor out the k-dependent term.**

**第 3 步 — 提取 k 相关项。**

  f̃(k) = e^{−σ²k²/2} ∫_{−∞}^{∞} e^{−(x + iσ²k)²/(2σ²)} dx.

**Step 4 — Shift the contour.** Let u = x + iσ²k (a shift by the purely imaginary constant iσ²k). Then du = dx, and as x ranges over ℝ, u ranges over the horizontal line Im(u) = σ²k in ℂ. By Cauchy's theorem, since e^{−u²/(2σ²)} is analytic everywhere, the integral along this shifted line equals the integral along the real axis:

**第 4 步 — 平移围道。** 令 u = x + iσ²k（平移纯虚常数 iσ²k）。则 du = dx，当 x 遍历 ℝ 时，u 遍历 ℂ 中虚部为 σ²k 的水平线。由柯西定理，由于 e^{−u²/(2σ²)} 处处解析，沿此平移直线的积分等于沿实轴的积分：

  ∫_{−∞+iσ²k}^{∞+iσ²k} e^{−u²/(2σ²)} du = ∫_{−∞}^{∞} e^{−u²/(2σ²)} du.

(The vertical pieces of the rectangular contour [−R, R] → [−R+iσ²k, R+iσ²k] vanish as R → ∞ because the Gaussian decays faster than any polynomial in Re(u).)

（矩形围道的竖直段 [−R, R] → [−R+iσ²k, R+iσ²k] 在 R → ∞ 时趋于零，因为高斯函数随 Re(u) 的增长衰减速度超过任何多项式。）

**Step 5 — Evaluate the Gaussian integral.** Substituting v = u/σ√2 (so that u²/(2σ²) = v²):

**第 5 步 — 计算高斯积分。** 令 v = u/σ√2（使 u²/(2σ²) = v²）：

  ∫_{−∞}^{∞} e^{−u²/(2σ²)} du = σ√2 ∫_{−∞}^{∞} e^{−v²} dv = σ√2 · √π = σ√(2π).

(Using the Gaussian integral ∫e^{−v²}dv = √π from Module 0.1.)

（利用模块 0.1 中的高斯积分 ∫e^{−v²}dv = √π。）

**Step 6 — Assemble the result.**

**第 6 步 — 组合结果。**

  **f̃(k) = e^{−σ²k²/2} · σ√(2π) = σ√(2π) e^{−σ²k²/2}.** ∎

The result is indeed a Gaussian in k with width 1/σ: as σ increases (broad x-distribution), the k-distribution narrows, and vice versa. Setting σ_k = 1/σ_x, we get the **uncertainty product** σ_x · σ_k = 1. With k = p/ℏ this becomes Δx · Δp = ℏ, the Heisenberg uncertainty principle.

结果确实是 k 中宽度为 1/σ 的高斯函数：随着 σ 增大（x 分布变宽），k 分布变窄，反之亦然。令 σ_k = 1/σ_x，得**不确定积** σ_x · σ_k = 1。令 k = p/ℏ，即得 Δx · Δp = ℏ，即海森堡不确定性原理。

---

## C. The Convolution Theorem · 卷积定理

**Claim.** If (f * g)(x) = ∫_{−∞}^{∞} f(y) g(x − y) dy is the convolution of f and g, and f̃, g̃ are their Fourier transforms, then

**命题。** 若 (f * g)(x) = ∫_{−∞}^{∞} f(y) g(x − y) dy 是 f 与 g 的卷积，f̃, g̃ 是它们的傅里叶变换，则

  **FT[f * g](k) = f̃(k) · g̃(k).**

**Step 1 — Write the Fourier transform of the convolution.**

**第 1 步 — 写出卷积的傅里叶变换。**

  FT[f*g](k) = ∫_{−∞}^{∞} (f*g)(x) e^{−ikx} dx = ∫_{−∞}^{∞} [∫_{−∞}^{∞} f(y) g(x−y) dy] e^{−ikx} dx.

**Step 2 — Interchange the order of integration.** (Justified by absolute integrability — Fubini's theorem, valid when f, g ∈ L¹(ℝ) ∩ L²(ℝ).)

**第 2 步 — 交换积分次序。**（由绝对可积性——Fubini 定理保证，当 f, g ∈ L¹(ℝ) ∩ L²(ℝ) 时成立。）

  FT[f*g](k) = ∫_{−∞}^{∞} f(y) [∫_{−∞}^{∞} g(x−y) e^{−ikx} dx] dy.

**Step 3 — Shift the inner integral.** Let u = x − y (so x = u + y, dx = du):

**第 3 步 — 对内层积分做平移。** 令 u = x − y（则 x = u + y，dx = du）：

  ∫_{−∞}^{∞} g(x−y) e^{−ikx} dx = ∫_{−∞}^{∞} g(u) e^{−ik(u+y)} du = e^{−iky} ∫_{−∞}^{∞} g(u) e^{−iku} du = e^{−iky} g̃(k).

**Step 4 — Reassemble.**

**第 4 步 — 重新组合。**

  FT[f*g](k) = ∫_{−∞}^{∞} f(y) e^{−iky} g̃(k) dy = g̃(k) ∫_{−∞}^{∞} f(y) e^{−iky} dy = g̃(k) · f̃(k).

Therefore **FT[f * g] = f̃ · g̃**. ∎

因此 **FT[f * g] = f̃ · g̃**。∎

**Inverse direction.** By taking the inverse Fourier transform: FT⁻¹[f̃ · g̃] = f * g. So convolution in real space ↔ pointwise multiplication in frequency space. This duality is extremely powerful: convolutions that are hard to compute directly become simple multiplications in Fourier space.

**逆方向。** 取逆傅里叶变换：FT⁻¹[f̃ · g̃] = f * g。即实空间中的卷积↔频率空间中的逐点乘积。这种对偶性极为有用：直接计算困难的卷积在傅里叶空间中变为简单的乘法。

**Physical applications.** In quantum mechanics, the probability of measuring a system in a particular state after preparation is a convolution of the apparatus resolution function with the state's probability distribution — the convolution theorem explains spectral line broadening. In signal processing, filtering is multiplication in frequency space (convolution in time domain).

**物理应用。** 在量子力学中，制备后测量系统处于特定态的概率是仪器分辨函数与态的概率分布的卷积——卷积定理解释了谱线展宽。在信号处理中，滤波是频率空间中的乘法（时域中的卷积）。

---

## D. The Dirac Delta as a Fourier Representation · 狄拉克 Delta 函数的傅里叶表示

**Claim.** The Dirac delta satisfies

**命题。** 狄拉克 delta 函数满足

  δ(x) = (1/2π) ∫_{−∞}^{∞} e^{ikx} dk.

**Step 1 — Compute the Fourier transform of δ.** Using the defining property ∫ δ(x) e^{−ikx} dx = e^{−ik·0} = 1:

**第 1 步 — 计算 δ 的傅里叶变换。** 利用定义性质 ∫ δ(x) e^{−ikx} dx = e^{−ik·0} = 1：

  δ̃(k) = ∫_{−∞}^{∞} δ(x) e^{−ikx} dx = **1**.

The Dirac delta transforms to the constant function 1 — it contains all frequencies with equal amplitude (a "white noise" in frequency space).

狄拉克 delta 变换为常数函数 1——它以相同振幅包含所有频率（频率空间中的"白噪声"）。

**Step 2 — Apply the inverse Fourier transform.** The inverse transform pair reads f(x) = (1/2π) ∫ f̃(k) e^{ikx} dk. Applying this to f̃(k) = 1:

**第 2 步 — 应用逆傅里叶变换。** 逆变换对为 f(x) = (1/2π) ∫ f̃(k) e^{ikx} dk。对 f̃(k) = 1 应用此公式：

  δ(x) = (1/2π) ∫_{−∞}^{∞} 1 · e^{ikx} dk = (1/2π) ∫_{−∞}^{∞} e^{ikx} dk. ∎

**Rigorous interpretation.** The integral (1/2π)∫e^{ikx}dk does not converge in the ordinary sense (the integrand has modulus 1 everywhere). It must be interpreted as a limit:

**严格解释。** 积分 (1/2π)∫e^{ikx}dk 在通常意义下不收敛（被积函数的模处处为 1）。必须理解为极限：

  δ(x) = lim_{K→∞} (1/2π) ∫_{−K}^{K} e^{ikx} dk = lim_{K→∞} sin(Kx) / (πx).

This is the **Dirichlet kernel**, which concentrates at x = 0 and has unit area for all K. In the theory of distributions (generalized functions), δ(x) is defined as a linear functional δ[f] = f(0), and the representation (1/2π)∫e^{ikx}dk is an identity in the distributional sense.

这是**狄利克雷核**，它在 x = 0 处集中，对所有 K 面积为 1。在广义函数理论中，δ(x) 定义为线性泛函 δ[f] = f(0)，而表达式 (1/2π)∫e^{ikx}dk 是广义函数意义下的恒等式。

**Step 3 — Verify the sifting property.** Using the representation:

**第 3 步 — 验证筛选性质。** 利用上述表示：

  ∫ δ(x−a) f(x) dx = ∫ [(1/2π) ∫ e^{ik(x−a)} dk] f(x) dx
                    = (1/2π) ∫ e^{−ika} [∫ f(x) e^{ikx} dx] dk
                    = (1/2π) ∫ e^{−ika} f̃(−k) dk = f(a). ✓

The last step uses the inverse Fourier transform evaluated at x = a.

最后一步利用逆傅里叶变换在 x = a 处的取值。

---

## E. Variance Formula: Var(x) = ⟨x²⟩ − ⟨x⟩² · 方差公式

**Claim.** For a random variable with probability density p(x),

**命题。** 对于概率密度为 p(x) 的随机变量，

  σ² ≡ ⟨(x − ⟨x⟩)²⟩ = ⟨x²⟩ − ⟨x⟩².

**Step 1 — Expand the square.**

**第 1 步 — 展开平方。**

  σ² = ⟨(x − ⟨x⟩)²⟩ = ∫ (x − ⟨x⟩)² p(x) dx = ∫ [x² − 2x⟨x⟩ + ⟨x⟩²] p(x) dx.

**Step 2 — Distribute the integral.** Using linearity of the integral:

**第 2 步 — 分配积分。** 利用积分的线性性：

  σ² = ∫ x² p(x) dx − 2⟨x⟩ ∫ x p(x) dx + ⟨x⟩² ∫ p(x) dx.

**Step 3 — Identify the terms.** By definition, ∫ x² p(x) dx = ⟨x²⟩, ∫ x p(x) dx = ⟨x⟩, and ∫ p(x) dx = 1 (normalization):

**第 3 步 — 识别各项。** 由定义，∫ x² p(x) dx = ⟨x²⟩，∫ x p(x) dx = ⟨x⟩，∫ p(x) dx = 1（归一化）：

  σ² = ⟨x²⟩ − 2⟨x⟩ · ⟨x⟩ + ⟨x⟩² · 1 = ⟨x²⟩ − 2⟨x⟩² + ⟨x⟩² = **⟨x²⟩ − ⟨x⟩²**. ∎

**Physical significance.** In quantum mechanics with |ψ(x)|² as the probability density, this gives Δx² = ⟨x²⟩ − ⟨x⟩², the quantum uncertainty in position. The same formula applies to momentum: Δp² = ⟨p²⟩ − ⟨p⟩². Together these satisfy the Heisenberg uncertainty principle Δx · Δp ≥ ℏ/2.

**物理意义。** 在量子力学中以 |ψ(x)|² 为概率密度，此式给出 Δx² = ⟨x²⟩ − ⟨x⟩²，即位置的量子不确定度。同样的公式适用于动量：Δp² = ⟨p²⟩ − ⟨p⟩²。二者共同满足海森堡不确定性原理 Δx · Δp ≥ ℏ/2。

**Non-negativity.** Since σ² = ⟨x²⟩ − ⟨x⟩² and also σ² = ⟨(x−⟨x⟩)²⟩ ≥ 0 (as the integral of a non-negative function times a non-negative density), we have **⟨x²⟩ ≥ ⟨x⟩²** — the Cauchy–Schwarz inequality for probability theory.

**非负性。** 由于 σ² = ⟨x²⟩ − ⟨x⟩²，同时 σ² = ⟨(x−⟨x⟩)²⟩ ≥ 0（非负函数乘以非负密度的积分），故 **⟨x²⟩ ≥ ⟨x⟩²**——这是概率论中的柯西–施瓦茨不等式。

---

## F. The Central Limit Theorem via Characteristic Functions · 通过特征函数的中心极限定理

**Claim.** Let X₁, X₂, …, Xₙ be i.i.d. random variables with mean μ and variance σ² < ∞. Define the standardized sum

**命题。** 设 X₁, X₂, …, Xₙ 是具有均值 μ 和有限方差 σ² 的独立同分布随机变量。定义标准化和

  Zₙ = (X₁ + X₂ + … + Xₙ − nμ) / (σ√n).

Then as n → ∞, Zₙ converges in distribution to the standard normal N(0,1):

当 n → ∞ 时，Zₙ 在分布意义上收敛于标准正态分布 N(0,1)：

  P(Zₙ ≤ z) → (1/√(2π)) ∫_{−∞}^z e^{−t²/2} dt.

**Step 1 — Define the characteristic function.** For a random variable X with density p(x), the **characteristic function** (Fourier transform of p) is

**第 1 步 — 定义特征函数。** 对具有密度 p(x) 的随机变量 X，**特征函数**（p 的傅里叶变换）为

  φ_X(t) = ⟨e^{itX}⟩ = ∫ e^{itx} p(x) dx.

Note: φ_X(t) = p̃(−t) in the Fourier convention of Module 0.5.

注：在模块 0.5 的傅里叶约定下，φ_X(t) = p̃(−t)。

**Step 2 — Characteristic function of a sum.** For independent X₁, X₂, the density of X₁ + X₂ is the convolution p₁ * p₂. By the convolution theorem (Section C):

**第 2 步 — 和的特征函数。** 对独立的 X₁, X₂，X₁ + X₂ 的密度是卷积 p₁ * p₂。由卷积定理（C 节）：

  φ_{X₁+X₂}(t) = φ_{X₁}(t) · φ_{X₂}(t).

More generally, for a sum of n i.i.d. copies: φ_{ΣXᵢ}(t) = [φ_X(t)]ⁿ.

更一般地，对 n 个独立同分布副本之和：φ_{ΣXᵢ}(t) = [φ_X(t)]ⁿ。

**Step 3 — Characteristic function of the centered, scaled variable.** Define Y = (X − μ)/σ, so Y has mean 0 and variance 1. Then Zₙ = (Y₁ + … + Yₙ)/√n, and

**第 3 步 — 中心化、缩放变量的特征函数。** 定义 Y = (X − μ)/σ，则 Y 的均值为 0，方差为 1。则 Zₙ = (Y₁ + … + Yₙ)/√n，

  φ_{Zₙ}(t) = φ_{ΣYᵢ/√n}(t) = φ_{ΣYᵢ}(t/√n) = [φ_Y(t/√n)]ⁿ.

**Step 4 — Expand φ_Y for small argument.** Using the Taylor expansion of e^{itY}:

**第 4 步 — 展开小参数处的 φ_Y。** 利用 e^{itY} 的泰勒展开：

  φ_Y(s) = ⟨e^{isY}⟩ = ⟨1 + isY + (isY)²/2! + …⟩ = 1 + is⟨Y⟩ + (is)²⟨Y²⟩/2 + O(s³).

Since ⟨Y⟩ = 0 and ⟨Y²⟩ = Var(Y) = 1 (by construction):

由于 ⟨Y⟩ = 0，⟨Y²⟩ = Var(Y) = 1（由构造）：

  φ_Y(s) = 1 − s²/2 + O(s³).

**Step 5 — Take the n-th power with s = t/√n.**

**第 5 步 — 令 s = t/√n 并取 n 次幂。**

  φ_{Zₙ}(t) = [φ_Y(t/√n)]ⁿ = [1 − t²/(2n) + O(n^{−3/2})]ⁿ.

**Step 6 — Take n → ∞.** Using the standard limit lim_{n→∞} (1 + a/n)ⁿ = eᵃ with a = −t²/2:

**第 6 步 — 令 n → ∞。** 利用标准极限 lim_{n→∞} (1 + a/n)ⁿ = eᵃ，其中 a = −t²/2：

  lim_{n→∞} φ_{Zₙ}(t) = lim_{n→∞} [1 − t²/(2n)]ⁿ = **e^{−t²/2}**.

**Step 7 — Identify the limit.** The function e^{−t²/2} is exactly the characteristic function of the standard normal distribution N(0,1) — by Section B, the Fourier transform of (1/√(2π)) e^{−x²/2} is e^{−t²/2} (with σ = 1). Since convergence of characteristic functions implies convergence in distribution (Lévy's continuity theorem):

**第 7 步 — 识别极限。** 函数 e^{−t²/2} 恰好是标准正态分布 N(0,1) 的特征函数——由 B 节，(1/√(2π)) e^{−x²/2} 的傅里叶变换为 e^{−t²/2}（σ = 1）。由于特征函数的收敛等价于分布的收敛（Lévy 连续性定理）：

  **Zₙ → N(0,1) in distribution.** ∎

**Physical significance.** The CLT explains why Gaussian distributions are ubiquitous in physics:
- **Thermal fluctuations**: energy of a macroscopic system is a sum of contributions from ~10²³ microscopic degrees of freedom — by the CLT, the fluctuations are Gaussian.
- **Quantum ground states**: the harmonic oscillator ground state ψ₀ ∝ e^{−mωx²/2ℏ} is Gaussian because the oscillator potential is the simplest smooth potential and the Gaussian is the "minimum uncertainty" state (it saturates the Heisenberg bound Δx Δp = ℏ/2).
- **Measurement noise**: any detector output that aggregates many small independent errors follows the CLT → Gaussian noise.

**物理意义。** 中心极限定理解释了高斯分布在物理学中普遍存在的原因：
- **热涨落**：宏观系统的能量是约 10²³ 个微观自由度贡献之和——由中心极限定理，涨落是高斯型的。
- **量子基态**：谐振子基态 ψ₀ ∝ e^{−mωx²/2ℏ} 是高斯型的，因为谐振子势是最简单的光滑势，而高斯态是"最小不确定性"态（它饱和海森堡界 Δx Δp = ℏ/2）。
- **测量噪声**：任何聚合许多小的独立误差的探测器输出均遵循中心极限定理 → 高斯噪声。

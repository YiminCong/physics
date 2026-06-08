# Derivations — Module 0.4: Complex Analysis
# 推导 — 模块 0.4：复分析

> Companion to [Module 0.4](./module-0.4-complex-analysis.md). Full step-by-step proofs of every non-trivial result stated there: Euler's formula from the Taylor series; the Cauchy–Riemann equations as necessary conditions for analyticity; the residue theorem for a simple pole, including the key integral ∮dz/(z−z₀) = 2πi; and evaluation of a real integral by residues. English first, then 中文.
> [模块 0.4](./module-0.4-complex-analysis.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：从泰勒级数推导欧拉公式；柯西–黎曼方程是解析性的必要条件；简单极点的留数定理（包括关键积分 ∮dz/(z−z₀) = 2πi）；以及用留数定理计算实数积分。先英文，后中文。

---

## A. Euler's Formula from the Taylor Series · 从泰勒级数推导欧拉公式

**Claim.** For any real θ,  e^{iθ} = cos θ + i sin θ.

**命题。** 对任意实数 θ，e^{iθ} = cos θ + i sin θ。

**Step 1 — Substitute iθ into the exponential series.** From Module 0.1 the Taylor series for eˣ converges absolutely for all x ∈ ℂ (the ratio test gives the same bound). Setting x = iθ:

**第 1 步 — 将 iθ 代入指数级数。** 由模块 0.1，eˣ 的泰勒级数对所有 x ∈ ℂ 绝对收敛（比值审敛法给出相同界）。令 x = iθ：

  e^{iθ} = Σ_{n=0}^{∞} (iθ)ⁿ / n! = Σ_{n=0}^{∞} iⁿ θⁿ / n!.

**Step 2 — Separate even and odd terms.** The powers of i cycle with period 4: i⁰ = 1, i¹ = i, i² = −1, i³ = −i, i⁴ = 1, … Split the sum into even (n = 2m) and odd (n = 2m+1) terms:

**第 2 步 — 分离偶数项与奇数项。** i 的幂次以 4 为周期循环：i⁰ = 1, i¹ = i, i² = −1, i³ = −i, i⁴ = 1, …。将级数拆分为偶数项（n = 2m）和奇数项（n = 2m+1）：

  Even terms: Σ_{m=0}^{∞} i^{2m} θ^{2m} / (2m)! = Σ_{m=0}^{∞} (−1)ᵐ θ^{2m} / (2m)!,
  Odd terms:  Σ_{m=0}^{∞} i^{2m+1} θ^{2m+1} / (2m+1)! = i Σ_{m=0}^{∞} (−1)ᵐ θ^{2m+1} / (2m+1)!.

  偶数项：Σ_{m=0}^{∞} i^{2m} θ^{2m} / (2m)! = Σ_{m=0}^{∞} (−1)ᵐ θ^{2m} / (2m)!，
  奇数项：Σ_{m=0}^{∞} i^{2m+1} θ^{2m+1} / (2m+1)! = i Σ_{m=0}^{∞} (−1)ᵐ θ^{2m+1} / (2m+1)!。

**Step 3 — Recognize the cosine and sine series.** Comparing with the series from Module 0.1:

**第 3 步 — 识别余弦和正弦级数。** 与模块 0.1 的级数对照：

  cos θ = Σ_{m=0}^{∞} (−1)ᵐ θ^{2m} / (2m)!,   sin θ = Σ_{m=0}^{∞} (−1)ᵐ θ^{2m+1} / (2m+1)!.

Therefore:

因此：

  e^{iθ} = cos θ + i sin θ. ∎

**Corollary 1 — Polar form.** Any complex number z = a + bi can be written z = r e^{iθ} where r = |z| = √(a² + b²) and θ = arg(z) = arctan(b/a). Multiplication adds phases: (r₁e^{iθ₁})(r₂e^{iθ₂}) = r₁r₂ e^{i(θ₁+θ₂)}.

**推论 1 — 极坐标形式。** 任意复数 z = a + bi 可写成 z = r e^{iθ}，其中 r = |z| = √(a² + b²)，θ = arg(z) = arctan(b/a)。乘法叠加相位：(r₁e^{iθ₁})(r₂e^{iθ₂}) = r₁r₂ e^{i(θ₁+θ₂)}。

**Corollary 2 — Euler's identity.** Setting θ = π: e^{iπ} = cos π + i sin π = −1 + 0 = −1, i.e., **e^{iπ} + 1 = 0**.

**推论 2 — 欧拉恒等式。** 令 θ = π：e^{iπ} = cos π + i sin π = −1 + 0 = −1，即 **e^{iπ} + 1 = 0**。

**Corollary 3 — Inverse relations.** Adding and subtracting e^{iθ} = cos θ + i sin θ and e^{−iθ} = cos θ − i sin θ:

**推论 3 — 逆关系。** 将 e^{iθ} = cos θ + i sin θ 与 e^{−iθ} = cos θ − i sin θ 相加减：

  cos θ = (e^{iθ} + e^{−iθ}) / 2,   sin θ = (e^{iθ} − e^{−iθ}) / (2i).

These are the standard complex representations of the real trigonometric functions, central to Fourier analysis.

这是实三角函数的标准复数表示，是傅里叶分析的核心。

---

## B. The Cauchy–Riemann Equations as Necessary Conditions for Analyticity · 柯西–黎曼方程是解析性的必要条件

**Claim.** If f(z) = u(x, y) + i v(x, y) is complex-differentiable at z₀ = x₀ + iy₀, then at that point:

**命题。** 若 f(z) = u(x, y) + i v(x, y) 在 z₀ = x₀ + iy₀ 处复可微，则在该点：

  ∂u/∂x = ∂v/∂y   and   ∂u/∂y = −∂v/∂x.

**Step 1 — Definition of complex differentiability.** f is complex-differentiable at z₀ if the limit

**第 1 步 — 复可微性的定义。** f 在 z₀ 处复可微是指以下极限存在：

  f′(z₀) = lim_{Δz→0} [f(z₀ + Δz) − f(z₀)] / Δz

exists and is the same regardless of the direction in which Δz → 0 in ℂ.

且该极限与 Δz → 0 在 ℂ 中的趋近方向无关。

**Step 2 — Approach along the real axis.** Let Δz = Δx (real), so Δz → 0 means Δx → 0:

**第 2 步 — 沿实轴趋近。** 令 Δz = Δx（实数），则 Δz → 0 等价于 Δx → 0：

  f′(z₀) = lim_{Δx→0} [u(x₀+Δx, y₀) − u(x₀,y₀)] / Δx  +  i lim_{Δx→0} [v(x₀+Δx, y₀) − v(x₀,y₀)] / Δx
          = ∂u/∂x + i ∂v/∂x.

**Step 3 — Approach along the imaginary axis.** Let Δz = i Δy (purely imaginary), so Δz → 0 means Δy → 0:

**第 3 步 — 沿虚轴趋近。** 令 Δz = i Δy（纯虚数），则 Δz → 0 等价于 Δy → 0：

  f′(z₀) = lim_{Δy→0} [u(x₀, y₀+Δy) − u(x₀,y₀)] / (iΔy)  +  i lim_{Δy→0} [v(x₀, y₀+Δy) − v(x₀,y₀)] / (iΔy)
          = (1/i) ∂u/∂y + (i/i) ∂v/∂y
          = −i ∂u/∂y + ∂v/∂y.

(Using 1/i = −i.)

（利用 1/i = −i。）

**Step 4 — Equate real and imaginary parts.** Since f′(z₀) must be the same from both approaches, set the two expressions equal:

**第 4 步 — 令实部和虚部相等。** 由于 f′(z₀) 从两个方向趋近必须相同，令两式相等：

  ∂u/∂x + i ∂v/∂x = ∂v/∂y − i ∂u/∂y.

Equating real parts: **∂u/∂x = ∂v/∂y**. Equating imaginary parts: **∂v/∂x = −∂u/∂y**. ∎

比较实部：**∂u/∂x = ∂v/∂y**。比较虚部：**∂v/∂x = −∂u/∂y**。∎

**Remark — Sufficient conditions.** The Cauchy–Riemann equations are necessary but not sufficient on their own. If additionally u and v have continuous first partial derivatives in a neighborhood of z₀ (which holds for all analytic functions), then the Cauchy–Riemann equations are also sufficient for complex differentiability there.

**说明——充分条件。** 柯西–黎曼方程是必要条件但本身不充分。若 u 和 v 在 z₀ 的某邻域内还具有连续一阶偏导数（这对所有解析函数均成立），则柯西–黎曼方程也是该点复可微的充分条件。

**Corollary — Both u and v are harmonic.** From the C–R equations, ∂²u/∂x² = ∂/∂x(∂v/∂y) = ∂/∂y(∂v/∂x) = −∂²u/∂y² (if second partials exist and are continuous), so ∂²u/∂x² + ∂²u/∂y² = 0. Hence ∇²u = 0 — u is harmonic, and similarly for v. Every analytic function generates a pair of harmonic conjugates, a fact used extensively in electrostatics (Module 1.8).

**推论——u 和 v 均为调和函数。** 由柯西–黎曼方程，∂²u/∂x² = ∂/∂x(∂v/∂y) = ∂/∂y(∂v/∂x) = −∂²u/∂y²（若二阶偏导数存在且连续），故 ∂²u/∂x² + ∂²u/∂y² = 0，即 ∇²u = 0——u 是调和函数，v 同理。每个解析函数生成一对调和共轭，这一事实在静电学（模块 1.8）中被广泛使用。

---

## C. The Fundamental Integral ∮ dz/(z − z₀) = 2πi · 基本积分 ∮ dz/(z − z₀) = 2πi

**Claim.** Let C be a simple closed contour traversed counterclockwise that encloses the point z₀. Then

**命题。** 设 C 是沿逆时针方向绕行的简单闭合围道，包围点 z₀。则

  ∮_C dz/(z − z₀) = 2πi.

**Step 1 — Parametrize C by a circle.** Because the integrand 1/(z − z₀) is analytic everywhere except at z₀, and by Cauchy's deformation theorem the integral is unchanged if we deform C to any other simple closed contour enclosing z₀, we may take C to be the circle of radius ε > 0 centered at z₀:

**第 1 步 — 用圆来参数化 C。** 由于被积函数 1/(z − z₀) 除 z₀ 外处处解析，由柯西变形定理，将 C 变形为包围 z₀ 的任意简单闭合围道时积分不变，故可取 C 为以 z₀ 为圆心、半径为 ε > 0 的圆：

  z(θ) = z₀ + ε e^{iθ},   θ ∈ [0, 2π].

**Step 2 — Compute dz.** Differentiating:

**第 2 步 — 计算 dz。** 求导：

  dz = iε e^{iθ} dθ.

**Step 3 — Substitute.**

**第 3 步 — 代入。**

  ∮_C dz/(z − z₀) = ∫_0^{2π} 1/(ε e^{iθ}) · iε e^{iθ} dθ = ∫_0^{2π} i dθ = i · 2π = **2πi**. ∎

The factors ε e^{iθ} cancel exactly, so the result is independent of the radius ε. This is the fundamental reason why residues (which capture the behavior near a pole) control contour integrals.

因子 ε e^{iθ} 恰好约去，故结果与半径 ε 无关。这正是留数（捕捉极点附近行为）控制围道积分的根本原因。

---

## D. The Residue Theorem for a Simple Pole · 简单极点的留数定理

**Setup.** Let f(z) have a simple pole at z₀ (meaning f(z) = g(z)/(z − z₀) where g is analytic in a neighborhood of z₀ with g(z₀) ≠ 0). The **residue** of f at z₀ is defined as

**准备工作。** 设 f(z) 在 z₀ 处有简单极点（即 f(z) = g(z)/(z − z₀)，其中 g 在 z₀ 的某邻域内解析且 g(z₀) ≠ 0）。f 在 z₀ 处的**留数**定义为

  Res(f, z₀) = lim_{z→z₀} (z − z₀) f(z) = g(z₀).

**Claim (Residue Theorem — simple pole version).** Let C be a simple closed counterclockwise contour enclosing only the simple pole at z₀. Then

**命题（留数定理——简单极点版本）。** 设 C 是逆时针方向的简单闭合围道，仅包围 z₀ 处的简单极点。则

  ∮_C f(z) dz = 2πi · Res(f, z₀).

**Step 1 — Laurent expansion.** Since g(z) is analytic at z₀, it has a Taylor series: g(z) = g(z₀) + g′(z₀)(z − z₀) + …. Therefore

**第 1 步 — 洛朗展开。** 由于 g(z) 在 z₀ 处解析，它有泰勒展开：g(z) = g(z₀) + g′(z₀)(z − z₀) + …。因此

  f(z) = g(z₀)/(z − z₀) + g′(z₀) + g″(z₀)(z−z₀)/2! + …
       = Res(f,z₀)/(z − z₀) + h(z),

where h(z) = g′(z₀) + g″(z₀)(z−z₀)/2! + … is analytic at z₀.

其中 h(z) = g′(z₀) + g″(z₀)(z−z₀)/2! + … 在 z₀ 处解析。

**Step 2 — Integrate term by term.** Split the contour integral:

**第 2 步 — 逐项积分。** 拆分围道积分：

  ∮_C f(z) dz = Res(f,z₀) ∮_C dz/(z − z₀)  +  ∮_C h(z) dz.

**Step 3 — Apply Cauchy's theorem to the analytic part.** Since h(z) is analytic everywhere inside and on C (it has no pole), Cauchy's integral theorem gives ∮_C h(z) dz = 0.

**第 3 步 — 对解析部分应用柯西定理。** 由于 h(z) 在 C 内部及其上处处解析（无极点），柯西积分定理给出 ∮_C h(z) dz = 0。

**Step 4 — Apply the fundamental integral.** From Section C, ∮_C dz/(z − z₀) = 2πi. Therefore:

**第 4 步 — 应用基本积分。** 由 C 节，∮_C dz/(z − z₀) = 2πi。因此：

  **∮_C f(z) dz = Res(f, z₀) · 2πi = 2πi · g(z₀).** ∎

**General statement.** If C encloses finitely many poles z₁, z₂, …, zₙ, by summing the contributions from each and applying Cauchy's theorem to the remaining analytic part:

**一般陈述。** 若 C 包围有限个极点 z₁, z₂, …, zₙ，对每个极点的贡献求和，并对其余解析部分应用柯西定理：

  ∮_C f(z) dz = 2πi Σₖ Res(f, zₖ).

---

## E. Evaluating ∮ dz/z = 2πi Directly · 直接计算 ∮ dz/z = 2πi

**Claim.** ∮_C dz/z = 2πi where C is any simple closed counterclockwise contour enclosing the origin.

**命题。** ∮_C dz/z = 2πi，其中 C 是任意包围原点的逆时针简单闭合围道。

This is the case z₀ = 0 of Section C (set g(z) = 1, Res(1/z, 0) = 1), so the result follows immediately. Alternatively, by direct parametrization with z = e^{iθ}, dz = ie^{iθ} dθ:

这是 C 节中 z₀ = 0 的特例（令 g(z) = 1，Res(1/z, 0) = 1），结果立即得到。另外，直接用 z = e^{iθ}，dz = ie^{iθ} dθ 参数化：

  ∮ dz/z = ∫_0^{2π} (ie^{iθ}/e^{iθ}) dθ = i ∫_0^{2π} dθ = **2πi**. ∎

**Contrast with ∮ zⁿ dz for n ≠ −1.** Parametrizing with z = ε e^{iθ}:

**与 n ≠ −1 时的 ∮ zⁿ dz 对比。** 用 z = ε e^{iθ} 参数化：

  ∮ zⁿ dz = ∫_0^{2π} εⁿ e^{inθ} · iε e^{iθ} dθ = iε^{n+1} ∫_0^{2π} e^{i(n+1)θ} dθ.

For integer n ≠ −1, e^{i(n+1)θ} completes a whole number of full cycles over [0, 2π], so the integral is zero. This is the reason why only the 1/(z−z₀) term in the Laurent expansion contributes — the residue.

对整数 n ≠ −1，e^{i(n+1)θ} 在 [0, 2π] 上完成整数圈，故积分为零。这就是为什么洛朗展开中只有 1/(z−z₀) 项有贡献——即留数。

---

## F. A Real Integral by Residues · 用留数定理计算实数积分

**Claim.** ∫_{−∞}^{∞} dx/(1 + x²) = π.

**命题。** ∫_{−∞}^{∞} dx/(1 + x²) = π。

**Step 1 — Identify the complex function.** Consider f(z) = 1/(1 + z²) = 1/[(z + i)(z − i)]. The poles are at z = ±i.

**第 1 步 — 确定复变函数。** 考虑 f(z) = 1/(1 + z²) = 1/[(z + i)(z − i)]，极点在 z = ±i。

**Step 2 — Choose a contour.** Take C_R = [−R, R] ∪ Γ_R, where Γ_R is the semicircle of radius R in the upper half-plane (Im(z) ≥ 0), traversed counterclockwise. For large R this encloses the pole at z = +i but not z = −i.

**第 2 步 — 选择围道。** 取 C_R = [−R, R] ∪ Γ_R，其中 Γ_R 是上半平面（Im(z) ≥ 0）中半径为 R 的半圆弧，逆时针绕行。对大 R，此围道包围极点 z = +i，但不包围 z = −i。

**Step 3 — Compute the residue at z = i.** Since the pole is simple:

**第 3 步 — 计算 z = i 处的留数。** 由于是简单极点：

  Res(f, i) = lim_{z→i} (z − i) · 1/[(z+i)(z−i)] = 1/(i + i) = 1/(2i).

**Step 4 — Residue theorem gives the contour integral.**

**第 4 步 — 留数定理给出围道积分。**

  ∮_{C_R} f(z) dz = 2πi · Res(f, i) = 2πi · 1/(2i) = π.

**Step 5 — Show the semicircle arc vanishes as R → ∞.** On Γ_R, z = Re^{iθ}, |z| = R, so |f(z)| = |1/(1+z²)| ≤ 1/(R² − 1) → 0. The length of Γ_R is πR. By the ML inequality (|∫_Γ f dz| ≤ max|f| · length):

**第 5 步 — 证明半圆弧在 R → ∞ 时趋于零。** 在 Γ_R 上，z = Re^{iθ}，|z| = R，故 |f(z)| = |1/(1+z²)| ≤ 1/(R² − 1) → 0。Γ_R 的长度为 πR。由 ML 不等式（|∫_Γ f dz| ≤ max|f| · 长度）：

  |∫_{Γ_R} f(z) dz| ≤ πR/(R² − 1) → 0 as R → ∞.

**Step 6 — Conclude.**

**第 6 步 — 结论。**

  π = ∮_{C_R} f(z) dz = ∫_{−R}^{R} dx/(1+x²) + ∫_{Γ_R} f(z) dz.

Taking R → ∞:

令 R → ∞：

  **∫_{−∞}^{∞} dx/(1 + x²) = π.** ∎

**Verification.** By elementary calculus, ∫ dx/(1+x²) = arctan(x) + C, and arctan(+∞) − arctan(−∞) = π/2 − (−π/2) = π. ✓ The residue method and elementary methods agree.

**验证。** 用初等微积分，∫ dx/(1+x²) = arctan(x) + C，而 arctan(+∞) − arctan(−∞) = π/2 − (−π/2) = π。✓ 留数法与初等方法结果一致。

**Physical context.** Integrals of this type — integrals of rational functions over the entire real line — appear in response functions, Green's functions, and Kramers–Kronig dispersion relations (Phase 6), where the poles in the complex plane encode causal structure and physical resonances.

**物理背景。** 这类积分——有理函数在整个实轴上的积分——出现在响应函数、格林函数和克喇末–克朗尼希色散关系中（第 6 阶段），其中复平面上的极点编码了因果结构和物理共振。

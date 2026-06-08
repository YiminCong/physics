# Derivations — Module 0.1: Calculus & Taylor Series
# 推导 — 模块 0.1：微积分与泰勒级数

> Companion to [Module 0.1](./module-0.1-calculus-and-taylor-series.md). Full step-by-step proofs of every non-trivial result stated there: the Taylor theorem with Lagrange remainder, the standard series for eˣ / sin / cos / (1+x)ⁿ / ln(1+x), the identity d/dx(eˣ) = eˣ from the series, and the Gaussian integral ∫_{−∞}^{∞} e^{−x²} dx = √π. English first, then 中文.
> [模块 0.1](./module-0.1-calculus-and-taylor-series.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：带拉格朗日余项的泰勒定理、eˣ / sin / cos / (1+x)ⁿ / ln(1+x) 的标准级数、从级数推导 d/dx(eˣ) = eˣ，以及高斯积分 ∫_{−∞}^{∞} e^{−x²} dx = √π。先英文，后中文。

---

## A. Taylor's Theorem with Lagrange Remainder · 带拉格朗日余项的泰勒定理

**Claim.** Let f be (n+1)-times continuously differentiable on an open interval containing a and x. Then

**命题。** 设 f 在包含 a 和 x 的开区间上 (n+1) 次连续可微。则

  f(x) = Σ_{k=0}^{n} f⁽ᵏ⁾(a) (x−a)ᵏ / k!  +  Rₙ(x),

where the **Lagrange remainder** is  Rₙ(x) = f⁽ⁿ⁺¹⁾(c) (x−a)ⁿ⁺¹ / (n+1)!  for some c strictly between a and x.

其中**拉格朗日余项**为  Rₙ(x) = f⁽ⁿ⁺¹⁾(c) (x−a)ⁿ⁺¹ / (n+1)!，c 严格介于 a 与 x 之间。

**Step 1 — Introduce an auxiliary function.** Fix x ≠ a and define

**第 1 步 — 引入辅助函数。** 固定 x ≠ a，定义

  g(t) = f(x) − Σ_{k=0}^{n} f⁽ᵏ⁾(t) (x−t)ᵏ / k!

on [a, x] (or [x, a] if x < a). This function measures the error that the n-th order Taylor polynomial at t makes when approximating f(x).

在 [a, x]（若 x < a 则为 [x, a]）上。此函数衡量以 t 为展开点的 n 阶泰勒多项式近似 f(x) 时的误差。

**Step 2 — Evaluate at the endpoints.** At t = x:

**第 2 步 — 计算端点处的值。** 在 t = x 处：

  g(x) = f(x) − f(x) = 0.

At t = a:

在 t = a 处：

  g(a) = f(x) − Σ_{k=0}^{n} f⁽ᵏ⁾(a) (x−a)ᵏ / k! = Rₙ(x).

**Step 3 — Differentiate g with respect to t.** Using the product rule on each term f⁽ᵏ⁾(t)(x−t)ᵏ/k!:

**第 3 步 — 对 g 关于 t 求导。** 对每一项 f⁽ᵏ⁾(t)(x−t)ᵏ/k! 使用乘积法则：

  d/dt [f⁽ᵏ⁾(t)(x−t)ᵏ/k!] = f⁽ᵏ⁺¹⁾(t)(x−t)ᵏ/k!  −  f⁽ᵏ⁾(t) k(x−t)ᵏ⁻¹/k!
                              = f⁽ᵏ⁺¹⁾(t)(x−t)ᵏ/k!  −  f⁽ᵏ⁾(t)(x−t)ᵏ⁻¹/(k−1)!.

Summing from k = 0 to n, consecutive terms telescope: the −f⁽ᵏ⁾(t)(x−t)ᵏ⁻¹/(k−1)! at step k cancels the +f⁽ᵏ⁾(t)(x−t)ᵏ⁻¹/(k−1)! at step k−1. Only the last term survives:

从 k = 0 到 n 求和，相邻项相消：第 k 步的 −f⁽ᵏ⁾(t)(x−t)ᵏ⁻¹/(k−1)! 与第 k−1 步的 +f⁽ᵏ⁾(t)(x−t)ᵏ⁻¹/(k−1)! 对消。只剩最后一项：

  g′(t) = −f⁽ⁿ⁺¹⁾(t)(x−t)ⁿ / n!.

**Step 4 — Introduce h(t) to apply Cauchy's mean-value theorem.** Let h(t) = (x−t)ⁿ⁺¹. Then h(x) = 0, h(a) = (x−a)ⁿ⁺¹, and h′(t) = −(n+1)(x−t)ⁿ. By the **Cauchy mean-value theorem**, there exists c ∈ (a, x) such that

**第 4 步 — 引入 h(t) 应用柯西中值定理。** 令 h(t) = (x−t)ⁿ⁺¹。则 h(x) = 0，h(a) = (x−a)ⁿ⁺¹，h′(t) = −(n+1)(x−t)ⁿ。由**柯西中值定理**，存在 c ∈ (a, x) 使得

  [g(x) − g(a)] / [h(x) − h(a)] = g′(c) / h′(c).

Substituting:

代入：

  [0 − Rₙ(x)] / [0 − (x−a)ⁿ⁺¹] = [−f⁽ⁿ⁺¹⁾(c)(x−c)ⁿ / n!] / [−(n+1)(x−c)ⁿ].

The (x−c)ⁿ factors cancel (c ≠ x), giving

因子 (x−c)ⁿ 约去（c ≠ x），得

  Rₙ(x) / (x−a)ⁿ⁺¹ = f⁽ⁿ⁺¹⁾(c) / (n+1)!.

**Step 5 — Conclude.** Therefore

**第 5 步 — 结论。** 因此

  **Rₙ(x) = f⁽ⁿ⁺¹⁾(c) (x−a)ⁿ⁺¹ / (n+1)!** for some c between a and x.

Since |Rₙ(x)| ≤ M |x−a|ⁿ⁺¹ / (n+1)! where M = max|f⁽ⁿ⁺¹⁾| on the interval, Rₙ(x) → 0 as n → ∞ whenever |x−a| is within the radius of convergence, establishing that the infinite Taylor series converges to f(x) on that interval. ∎

由于 |Rₙ(x)| ≤ M |x−a|ⁿ⁺¹ / (n+1)!，其中 M = 区间上 |f⁽ⁿ⁺¹⁾| 的上界，故当 |x−a| 在收敛半径内时 Rₙ(x) → 0（n → ∞），从而证明无穷泰勒级数在该区间上收敛于 f(x)。∎

---

## B. Taylor Series for eˣ, sin x, cos x · eˣ、sin x、cos x 的泰勒级数

**Claim.** For all x ∈ ℝ:

**命题。** 对所有 x ∈ ℝ：

  eˣ = Σ_{n=0}^{∞} xⁿ/n!,   sin x = Σ_{n=0}^{∞} (−1)ⁿ x^{2n+1}/(2n+1)!,   cos x = Σ_{n=0}^{∞} (−1)ⁿ x^{2n}/(2n)!.

**Step 1 — Compute the derivatives of eˣ.** Let f(x) = eˣ. Then f⁽ⁿ⁾(x) = eˣ for all n. At a = 0: f⁽ⁿ⁾(0) = 1 for all n. The remainder |Rₙ(x)| ≤ eˣ |x|ⁿ⁺¹/(n+1)!. Since n! grows faster than any power, |x|ⁿ⁺¹/(n+1)! → 0, so the series converges absolutely for all x:

**第 1 步 — 计算 eˣ 的各阶导数。** 令 f(x) = eˣ。则 f⁽ⁿ⁾(x) = eˣ 对所有 n 成立。在 a = 0 处：f⁽ⁿ⁾(0) = 1 对所有 n 成立。余项 |Rₙ(x)| ≤ eˣ |x|ⁿ⁺¹/(n+1)!。由于 n! 的增长速度超过任何幂次，|x|ⁿ⁺¹/(n+1)! → 0，故级数对所有 x 绝对收敛：

  **eˣ = 1 + x + x²/2! + x³/3! + … = Σ_{n=0}^{∞} xⁿ/n!.**

**Step 2 — Compute the derivatives of sin x.** The derivatives cycle with period 4: sin x, cos x, −sin x, −cos x, … At a = 0 the values are 0, 1, 0, −1, 0, 1, … Only odd-indexed terms survive:

**第 2 步 — 计算 sin x 的各阶导数。** 导数以 4 为周期循环：sin x, cos x, −sin x, −cos x, …。在 a = 0 处取值为 0, 1, 0, −1, 0, 1, …。只有奇数阶项非零：

  **sin x = x − x³/3! + x⁵/5! − … = Σ_{n=0}^{∞} (−1)ⁿ x^{2n+1}/(2n+1)!.**

The remainder |Rₙ| ≤ |x|ⁿ⁺¹/(n+1)! → 0, so the series converges for all x ∈ ℝ.

余项 |Rₙ| ≤ |x|ⁿ⁺¹/(n+1)! → 0，故级数对所有 x ∈ ℝ 收敛。

**Step 3 — Compute the derivatives of cos x.** Similarly the derivatives cycle 4-periodically, and at a = 0 only even-indexed terms survive:

**第 3 步 — 计算 cos x 的各阶导数。** 类似地，导数以 4 为周期循环，在 a = 0 处只有偶数阶项非零：

  **cos x = 1 − x²/2! + x⁴/4! − … = Σ_{n=0}^{∞} (−1)ⁿ x^{2n}/(2n)!.** ∎

---

## C. Taylor Series for (1+x)ⁿ and ln(1+x) · (1+x)ⁿ 与 ln(1+x) 的泰勒级数

**Claim (Binomial Series).** For real exponent α and |x| < 1:

**命题（二项式级数）。** 对实数指数 α 及 |x| < 1：

  (1+x)^α = Σ_{k=0}^{∞} C(α,k) xᵏ,   where C(α,k) = α(α−1)…(α−k+1)/k!.

In particular for |x| ≪ 1 the leading approximation is (1+x)^α ≈ 1 + αx.

特别地，当 |x| ≪ 1 时，领头近似为 (1+x)^α ≈ 1 + αx。

**Step 1 — Compute derivatives at 0.** Let f(x) = (1+x)^α. Then f′(x) = α(1+x)^{α−1}, f″(x) = α(α−1)(1+x)^{α−2}, and by induction f⁽ᵏ⁾(x) = α(α−1)…(α−k+1)(1+x)^{α−k}. At x = 0: f⁽ᵏ⁾(0) = α(α−1)…(α−k+1) = k! C(α,k).

**第 1 步 — 计算 0 处的导数。** 令 f(x) = (1+x)^α。则 f′(x) = α(1+x)^{α−1}，f″(x) = α(α−1)(1+x)^{α−2}，由归纳法 f⁽ᵏ⁾(x) = α(α−1)…(α−k+1)(1+x)^{α−k}。在 x = 0 处：f⁽ᵏ⁾(0) = α(α−1)…(α−k+1) = k! C(α,k)。

**Step 2 — Radius of convergence.** By the ratio test, |C(α,k+1) xᵏ⁺¹| / |C(α,k) xᵏ| = |(α−k)/(k+1)| |x| → |x| as k → ∞. So the series converges absolutely for |x| < 1. (At the endpoints |x| = 1 the behavior depends on α.) The Taylor formula then gives

**第 2 步 — 收敛半径。** 由比值审敛法，|C(α,k+1) xᵏ⁺¹| / |C(α,k) xᵏ| = |(α−k)/(k+1)| |x| → |x|（k → ∞）。故级数对 |x| < 1 绝对收敛（在端点 |x| = 1 处的行为取决于 α）。泰勒公式给出

  **(1+x)^α = Σ_{k=0}^{∞} C(α,k) xᵏ for |x| < 1.** ∎

**Claim (Logarithm Series).** For |x| < 1:

**命题（对数级数）。** 对 |x| < 1：

  ln(1+x) = x − x²/2 + x³/3 − x⁴/4 + … = Σ_{n=1}^{∞} (−1)ⁿ⁺¹ xⁿ/n.

**Step 3 — Integrate the geometric series.** The geometric series gives, for |x| < 1:

**第 3 步 — 对等比级数积分。** 对 |x| < 1，等比级数给出：

  1/(1+t) = Σ_{n=0}^{∞} (−t)ⁿ = 1 − t + t² − t³ + …

Integrate both sides from 0 to x (term-by-term integration is valid within |x| < 1 by uniform convergence):

两端从 0 积到 x（在 |x| < 1 内由一致收敛性，逐项积分有效）：

  ∫_0^x 1/(1+t) dt = Σ_{n=0}^{∞} (−1)ⁿ ∫_0^x tⁿ dt = Σ_{n=0}^{∞} (−1)ⁿ xⁿ⁺¹/(n+1).

The left-hand side equals ln(1+x). Re-indexing with m = n+1:

左侧等于 ln(1+x)。令 m = n+1 重新标记：

  **ln(1+x) = Σ_{m=1}^{∞} (−1)^{m+1} xᵐ/m = x − x²/2 + x³/3 − …** for |x| < 1. ∎

---

## D. Proof that d/dx(eˣ) = eˣ from the Series · 从级数证明 d/dx(eˣ) = eˣ

**Claim.** The function defined by eˣ = Σ_{n=0}^{∞} xⁿ/n! satisfies d/dx(eˣ) = eˣ.

**命题。** 由 eˣ = Σ_{n=0}^{∞} xⁿ/n! 定义的函数满足 d/dx(eˣ) = eˣ。

**Step 1 — Differentiate term by term.** Because the power series Σ xⁿ/n! converges absolutely for all x ∈ ℝ (established in Section B), it converges uniformly on every closed bounded interval, so term-by-term differentiation is valid:

**第 1 步 — 逐项求导。** 由于幂级数 Σ xⁿ/n! 对所有 x ∈ ℝ 绝对收敛（见 B 节），它在每个有界闭区间上一致收敛，故逐项求导合法：

  d/dx(eˣ) = d/dx Σ_{n=0}^{∞} xⁿ/n! = Σ_{n=0}^{∞} d/dx [xⁿ/n!] = Σ_{n=1}^{∞} n xⁿ⁻¹/n! = Σ_{n=1}^{∞} xⁿ⁻¹/(n−1)!.

**Step 2 — Re-index.** Let m = n − 1:

**第 2 步 — 重新标记。** 令 m = n − 1：

  Σ_{n=1}^{∞} xⁿ⁻¹/(n−1)! = Σ_{m=0}^{∞} xᵐ/m! = eˣ.

Therefore **d/dx(eˣ) = eˣ**. ∎

因此 **d/dx(eˣ) = eˣ**。∎

**Physical significance.** Any first-order ODE of the form dy/dt = λy has solution y(t) = y(0) eˡᵗ. This single fact underlies radioactive decay, RC-circuit discharge, the time factor e^{−iEt/ℏ} in quantum mechanics, and the Boltzmann factor e^{−E/kT} in statistical mechanics.

**物理意义。** 任何形如 dy/dt = λy 的一阶常微分方程的解为 y(t) = y(0) eˡᵗ。这一事实奠定了放射性衰变、RC 电路放电、量子力学中的时间因子 e^{−iEt/ℏ}，以及统计力学中玻尔兹曼因子 e^{−E/kT} 的基础。

---

## E. The Gaussian Integral · 高斯积分

**Claim.** ∫_{−∞}^{∞} e^{−x²} dx = √π.

**命题。** ∫_{−∞}^{∞} e^{−x²} dx = √π。

**Step 1 — Define I and form I².** The integrand e^{−x²} is positive and continuous; the improper integral converges absolutely (since e^{−x²} < e^{−|x|} for |x| > 1). Let I = ∫_{−∞}^{∞} e^{−x²} dx. Square it, using an independent dummy variable y for the second copy:

**第 1 步 — 定义 I 并构造 I²。** 被积函数 e^{−x²} 为正且连续；广义积分绝对收敛（因为当 |x| > 1 时 e^{−x²} < e^{−|x|}）。令 I = ∫_{−∞}^{∞} e^{−x²} dx。对其平方，用独立哑变量 y 表示第二个因子：

  I² = [∫_{−∞}^{∞} e^{−x²} dx] · [∫_{−∞}^{∞} e^{−y²} dy] = ∫_{−∞}^{∞} ∫_{−∞}^{∞} e^{−(x²+y²)} dx dy.

**Step 2 — Switch to polar coordinates.** Set x = r cos θ, y = r sin θ, with Jacobian dx dy = r dr dθ. The entire plane is covered by r ∈ [0, ∞) and θ ∈ [0, 2π):

**第 2 步 — 转换到极坐标。** 令 x = r cos θ，y = r sin θ，雅可比行列式 dx dy = r dr dθ。整个平面由 r ∈ [0, ∞)，θ ∈ [0, 2π) 覆盖：

  I² = ∫_0^{2π} ∫_0^∞ e^{−r²} r dr dθ.

**Step 3 — Evaluate the r integral.** Let u = r², du = 2r dr:

**第 3 步 — 计算 r 方向的积分。** 令 u = r²，du = 2r dr：

  ∫_0^∞ e^{−r²} r dr = (1/2) ∫_0^∞ e^{−u} du = (1/2) [−e^{−u}]_0^∞ = (1/2)(0 − (−1)) = 1/2.

**Step 4 — Evaluate the θ integral.**

**第 4 步 — 计算 θ 方向的积分。**

  I² = ∫_0^{2π} dθ · (1/2) = 2π · (1/2) = π.

**Step 5 — Conclude.** Since I > 0,

**第 5 步 — 结论。** 由于 I > 0，

  **I = √π,**  i.e. ∫_{−∞}^{∞} e^{−x²} dx = √π. ∎

**Corollary.** By the substitution x → x/σ√2, ∫_{−∞}^{∞} e^{−x²/(2σ²)} dx = σ√(2π). This normalization factor is what appears in the Gaussian probability distribution (1/σ√(2π)) e^{−x²/2σ²} and in the ground-state wavefunction of the harmonic oscillator.

**推论。** 通过代换 x → x/σ√2，得 ∫_{−∞}^{∞} e^{−x²/(2σ²)} dx = σ√(2π)。此归一化因子出现在高斯概率分布 (1/σ√(2π)) e^{−x²/2σ²} 和谐振子基态波函数中。

---

## F. Convergence of the Taylor Series: Domain Conditions · 泰勒级数的收敛性：定义域条件

**Summary of convergence.** The results above establish:

**收敛性总结。** 上述结果表明：

- eˣ: converges for all x ∈ ℝ (the remainder Rₙ → 0 by the ratio test on n!).
- sin x, cos x: converge for all x ∈ ℝ (derivatives bounded by 1 in modulus).
- (1+x)^α: converges absolutely for |x| < 1; at the boundary the behavior depends on α (e.g. for α = 1 the series terminates to 1 + x; for α = −1 it diverges at x = −1 and converges conditionally at x = 1 by the alternating series test).
- ln(1+x): converges for −1 < x ≤ 1 (at x = 1 it converges to ln 2 by Abel's theorem; at x = −1 it diverges).

- eˣ：对所有 x ∈ ℝ 收敛（余项 Rₙ 由 n! 的比值法趋于 0）。
- sin x，cos x：对所有 x ∈ ℝ 收敛（导数的模以 1 为界）。
- (1+x)^α：对 |x| < 1 绝对收敛；在边界处的行为取决于 α（例如 α = 1 时级数有限终止为 1 + x；α = −1 时在 x = −1 处发散，在 x = 1 处由交错级数判别法条件收敛）。
- ln(1+x)：对 −1 < x ≤ 1 收敛（在 x = 1 处由阿贝尔定理收敛于 ln 2；在 x = −1 处发散）。

**Physical relevance.** In physics one nearly always works within the radius of convergence, where the expansion is not only valid but where truncating to finitely many terms gives quantitatively accurate approximations — the foundation of perturbation theory.

**物理意义。** 在物理学中几乎总是在收敛半径内工作，此时展开不仅有效，截取有限项即可给出定量准确的近似——这正是微扰论的基础。

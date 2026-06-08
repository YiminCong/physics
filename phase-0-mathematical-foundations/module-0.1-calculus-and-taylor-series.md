# Module 0.1 — Calculus & Taylor Series
**模块 0.1 — 微积分与泰勒级数**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用

Calculus is the grammar of change; Taylor series is the art of approximation. Together they underlie every equation of motion, every wave function, and every thermodynamic identity in the curriculum.

微积分是描述变化的语言；泰勒级数是近似的艺术。二者共同奠定了课程中每一个运动方程、每一个波函数以及每一个热力学恒等式的基础。

---

## 1. Differentiation & Integration · 微分与积分

**Definition.** The **derivative** f′(x) = lim_{h→0} [f(x+h) − f(x)] / h measures the instantaneous rate of change of f — geometrically, the slope of the tangent. The **integral** ∫_a^b f(x) dx is the signed area under the curve, defined as a limit of Riemann sums. The **Fundamental Theorem of Calculus** links them: if F′ = f, then ∫_a^b f(x) dx = F(b) − F(a). Differentiation and integration are inverse operations.

**定义。** **导数** f′(x) = lim_{h→0} [f(x+h) − f(x)] / h 衡量 f 的瞬时变化率——几何上即切线的斜率。**积分** ∫_a^b f(x) dx 是曲线下方的有符号面积，定义为黎曼和的极限。**微积分基本定理**将二者联系起来：若 F′ = f，则 ∫_a^b f(x) dx = F(b) − F(a)。微分与积分互为逆运算。

**Demonstration.** Differentiate f(x) = xⁿ by the power rule: f′(x) = n xⁿ⁻¹. Integrate: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C (n ≠ −1). For exponentials: d/dx(eˣ) = eˣ — the defining self-referential property that makes exponentials central to all of physics.

**演示。** 对 f(x) = xⁿ 用幂次法则求导：f′(x) = n xⁿ⁻¹。积分：∫ xⁿ dx = xⁿ⁺¹/(n+1) + C（n ≠ −1）。对指数函数：d/dx(eˣ) = eˣ——这一自指性质使指数函数在整个物理学中居于核心地位。

**Application.** Newton's second law F = ma is a second-order ODE: knowing the force means integrating twice to find position. The work–energy theorem ΔKE = ∫ F·dx is the Fundamental Theorem applied to mechanics. Accumulation — of charge, probability, heat — is always an integral. Rate of change — of momentum, entropy, field — is always a derivative.

**应用。** 牛顿第二定律 F = ma 是一个二阶常微分方程：已知力就意味着对其积分两次以求得位置。功能定理 ΔKE = ∫ F·dx 是微积分基本定理在力学中的应用。电荷、概率、热量等的累积始终是积分；动量、熵、场等的变化率始终是导数。

---

## 2. Taylor Series ⭐ · 泰勒级数 ⭐

This is one of the most load-bearing tools in the entire curriculum. Virtually every approximation scheme in physics — small oscillations, weak fields, perturbation theory — is a Taylor expansion in disguise.

这是整个课程中最核心的工具之一。物理学中几乎每一种近似方案——小振动、弱场、微扰论——本质上都是泰勒展开。

**Definition.** Any sufficiently smooth function can be expanded around a point a as

**定义。** 任何足够光滑的函数都可以在点 a 附近展开为

  f(x) = Σ_{n=0}^{∞} f⁽ⁿ⁾(a) (x−a)ⁿ / n!

The most important special cases (all expanded around 0):

最重要的几个特殊情形（均在 0 处展开）：

| Function | Series |
|----------|--------|
| eˣ | 1 + x + x²/2! + x³/3! + … = Σ xⁿ/n! |
| sin x | x − x³/3! + x⁵/5! − … |
| cos x | 1 − x²/2! + x⁴/4! − … |
| (1+x)ⁿ | 1 + nx + n(n−1)x²/2! + … ≈ 1 + nx for |x| ≪ 1 |
| ln(1+x) | x − x²/2 + x³/3 − … |

| 函数 | 级数 |
|----------|--------|
| eˣ | 1 + x + x²/2! + x³/3! + … = Σ xⁿ/n! |
| sin x | x − x³/3! + x⁵/5! − … |
| cos x | 1 − x²/2! + x⁴/4! − … |
| (1+x)ⁿ | 1 + nx + n(n−1)x²/2! + … ≈ 1 + nx，当 |x| ≪ 1 |
| ln(1+x) | x − x²/2 + x³/3 − … |

**Demonstration.** The **small-angle approximation**: for θ ≪ 1 (in radians), sin θ = θ − θ³/6 + … ≈ θ. This single truncation turns the nonlinear pendulum equation θ″ + (g/L) sin θ = 0 into the solvable linear equation θ″ + (g/L) θ = 0. Similarly cos θ ≈ 1 − θ²/2, used constantly in optics and relativity. **Linearization** — retaining only first-order terms — is how physicists convert hard problems into tractable ones.

**演示。** **小角近似**：当 θ ≪ 1（弧度）时，sin θ = θ − θ³/6 + … ≈ θ。这一截断将非线性摆方程 θ″ + (g/L) sin θ = 0 转化为可解的线性方程 θ″ + (g/L) θ = 0。类似地，cos θ ≈ 1 − θ²/2，在光学和相对论中频繁使用。**线性化**——只保留一阶项——是物理学家将难题转化为可处理问题的方法。

**Application.** The series eˣ = Σ xⁿ/n! is its own derivative term-by-term, confirming d/dx(eˣ) = eˣ — this feeds directly into every ODE whose solution is exponential (Module 0.3) and, via substitution of iθ, into Euler's formula e^{iθ} = cos θ + i sin θ that anchors complex analysis (Module 0.4). The **Gaussian integral** ∫_{−∞}^{∞} e^{−x²} dx = √π is a cornerstone result: it underpins the normalization of wave packets and probability distributions (Module 0.5) and recurs throughout statistical mechanics and QFT. The binomial expansion (1+x)ⁿ ≈ 1 + nx for |x| ≪ 1 appears in special relativity when v/c ≪ 1, in perturbation theory, and in weak-field expansions of the metric (Phase 7).

**应用。** 级数 eˣ = Σ xⁿ/n! 逐项求导后仍为其本身，从而验证 d/dx(eˣ) = eˣ——这直接推动了所有解为指数函数的常微分方程（模块 0.3），并通过代入 iθ 得出欧拉公式 e^{iθ} = cos θ + i sin θ，奠定了复分析的基础（模块 0.4）。**高斯积分** ∫_{−∞}^{∞} e^{−x²} dx = √π 是一个基石性结果：它支撑了波包和概率分布的归一化（模块 0.5），并贯穿统计力学和量子场论。二项式展开 (1+x)ⁿ ≈ 1 + nx（当 |x| ≪ 1）出现在 v/c ≪ 1 的狭义相对论、微扰论以及度规的弱场展开中（第 7 阶段）。

---

## Module 0.1 Self-Test (blank page)

1. State the Fundamental Theorem of Calculus and use it to evaluate ∫_0^1 3x² dx.
2. Differentiate e^{ax} sin(bx) using the product rule.
3. Write the Taylor expansion of eˣ, sin x, and cos x to three non-zero terms.
4. Use the small-angle approximation to linearize the pendulum equation and state its solution.
5. Explain why d/dx(eˣ) = eˣ makes exponentials the natural solutions to constant-coefficient ODEs, and name the other module that builds directly on eˣ via substitution of iθ.

**自测（空白页）**

1. 陈述微积分基本定理，并用它计算 ∫_0^1 3x² dx。
2. 用乘积法则对 e^{ax} sin(bx) 求导。
3. 写出 eˣ、sin x 和 cos x 的泰勒展开式至三个非零项。
4. 用小角近似对摆方程进行线性化，并写出其解。
5. 解释为何 d/dx(eˣ) = eˣ 使指数函数成为常系数常微分方程的自然解，并指出通过代入 iθ 直接依赖 eˣ 的另一个模块。

---

← [Phase 0 index](./README.md) · Next: [Module 0.2 — Linear Algebra](./module-0.2-linear-algebra.md) →

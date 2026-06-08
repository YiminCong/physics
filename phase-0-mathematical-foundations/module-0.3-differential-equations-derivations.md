# Derivations — Module 0.3: Differential Equations
# 推导 — 模块 0.3：微分方程

> Companion to [Module 0.3](./module-0.3-differential-equations.md). Full step-by-step proofs and derivations: the integrating factor for the first-order linear ODE; the general solution of the second-order constant-coefficient ODE for all three root cases; the Hermite recursion relation derived from series substitution, with the termination argument; and complete separation of the heat equation. English first, then 中文.
> [模块 0.3](./module-0.3-differential-equations.md) 的配套文档：完整逐步证明与推导：一阶线性常微分方程的积分因子法；常系数二阶线性常微分方程在三种根情形下的通解；由级数代入推导厄米递推关系及其终止论证；以及热传导方程的完整分离变量过程。先英文，后中文。

---

## A. The Integrating Factor for the First-Order Linear ODE · 一阶线性常微分方程的积分因子

**Claim.** The equation y′ + p(x) y = q(x) has the general solution

**命题。** 方程 y′ + p(x) y = q(x) 的通解为

  y(x) = (1/μ(x)) [∫ μ(x) q(x) dx + C],   where μ(x) = e^{∫p(x) dx}.

**Step 1 — Motivation: seek a function μ(x) that makes the left side a perfect derivative.** If we multiply both sides of y′ + p(x)y = q(x) by an unknown function μ(x), we obtain

**第 1 步 — 动机：寻找使左侧成为完全导数的函数 μ(x)。** 将方程 y′ + p(x)y = q(x) 两端乘以未知函数 μ(x)，得

  μ y′ + μ p y = μ q.

We want the left side to equal d/dx(μ y). Expanding d/dx(μ y) = μ y′ + μ′ y. Matching coefficients of y:

我们希望左侧等于 d/dx(μ y)。展开 d/dx(μ y) = μ y′ + μ′ y，比较 y 的系数：

  μ p = μ′,   i.e.   μ′/μ = p(x).

**Step 2 — Solve for μ.** The equation μ′ = p(x) μ is separable:

**第 2 步 — 求 μ。** 方程 μ′ = p(x) μ 是可分离的：

  dμ/μ = p(x) dx  →  ln μ = ∫ p(x) dx  →  **μ(x) = e^{∫ p(x) dx}**.

(We take the particular antiderivative without the integration constant C, since multiplying by a constant would cancel out.)

（取特定原函数，不加积分常数 C，因为乘以常数会被约去。）

**Step 3 — Rewrite and integrate.** With this μ, the original equation becomes

**第 3 步 — 改写并积分。** 有了此 μ，原方程变为

  d/dx(μ y) = μ q.

Integrate both sides:

两端积分：

  μ(x) y(x) = ∫ μ(x) q(x) dx + C.

**Step 4 — Solve for y.**

**第 4 步 — 解出 y。**

  **y(x) = (1/μ(x)) [∫ μ(x) q(x) dx + C].** ∎

**Domain condition.** The solution is valid on any interval where p(x) and q(x) are continuous. The constant C is fixed by one initial condition y(x₀) = y₀.

**定义域条件。** 解在 p(x) 和 q(x) 连续的任何区间上有效。常数 C 由一个初始条件 y(x₀) = y₀ 确定。

**Example: exponential decay.** y′ + k y = 0. Here p = k, q = 0, μ = eᵏˣ. Then y = e^{−kx} [∫ 0 dx + C] = C e^{−kx}. With y(0) = y₀: **y = y₀ e^{−kx}**.

**示例：指数衰减。** y′ + k y = 0。此时 p = k, q = 0, μ = eᵏˣ。则 y = e^{−kx} [∫ 0 dx + C] = C e^{−kx}。由 y(0) = y₀：**y = y₀ e^{−kx}**。

---

## B. Second-Order Linear ODE with Constant Coefficients — All Three Cases · 常系数二阶线性常微分方程——三种情形

**Setup.** We solve ay″ + by′ + cy = 0 with a ≠ 0. The substitution y = e^{rt} converts the equation into a(r² e^{rt}) + b(r e^{rt}) + c(e^{rt}) = 0; since e^{rt} ≠ 0, this gives the **characteristic equation**:

**准备工作。** 求解 ay″ + by′ + cy = 0，a ≠ 0。代入 y = e^{rt}，得 a(r² e^{rt}) + b(r e^{rt}) + c(e^{rt}) = 0；由于 e^{rt} ≠ 0，得**特征方程**：

  **a r² + b r + c = 0**,   roots  r = (−b ± √(b² − 4ac)) / (2a).

The discriminant Δ = b² − 4ac determines three cases.

判别式 Δ = b² − 4ac 决定三种情形。

---

### B.1 — Case 1: Two Distinct Real Roots (Δ > 0) · 情形 1：两个不同实根（Δ > 0）

**Step 1 — Two independent solutions.** For roots r₁ ≠ r₂ (both real), both y₁ = e^{r₁t} and y₂ = e^{r₂t} satisfy the ODE. They are linearly independent because e^{r₁t}/e^{r₂t} = e^{(r₁−r₂)t} is non-constant (r₁ ≠ r₂).

**第 1 步 — 两个独立解。** 对于 r₁ ≠ r₂（均为实数），y₁ = e^{r₁t} 和 y₂ = e^{r₂t} 均满足常微分方程。它们线性无关，因为 e^{r₁t}/e^{r₂t} = e^{(r₁−r₂)t} 非常数（r₁ ≠ r₂）。

**Step 2 — General solution by superposition.**

**第 2 步 — 由叠加原理得通解。**

  **y(t) = C₁ e^{r₁t} + C₂ e^{r₂t}.**

**Step 3 — Physical example: overdamped oscillator.** For y″ + 2γy′ + ω₀²y = 0 with γ > ω₀ > 0, the roots r = −γ ± √(γ² − ω₀²) are both real and negative. The general solution is a sum of two decaying exponentials with no oscillation — the system returns to equilibrium monotonically.

**第 3 步 — 物理示例：过阻尼振子。** 对 y″ + 2γy′ + ω₀²y = 0，γ > ω₀ > 0，根 r = −γ ± √(γ² − ω₀²) 均为实数且为负。通解是两个衰减指数之和，无振荡——系统单调地返回平衡。

The general solution y(t) = C₁ e^{r₁t} + C₂ e^{r₂t} with C₁, C₂ determined by initial conditions y(0) and y′(0). ∎

通解 y(t) = C₁ e^{r₁t} + C₂ e^{r₂t}，C₁, C₂ 由初始条件 y(0) 和 y′(0) 确定。∎

---

### B.2 — Case 2: Repeated Real Root (Δ = 0) · 情形 2：重实根（Δ = 0）

**Step 1 — Only one exponential.** When Δ = 0, there is only one root r = −b/(2a). The function y₁ = e^{rt} is one solution, but we need two linearly independent solutions.

**第 1 步 — 只有一个指数解。** 当 Δ = 0 时，只有一个根 r = −b/(2a)。函数 y₁ = e^{rt} 是一个解，但我们需要两个线性无关的解。

**Step 2 — Reduction of order.** Try y₂ = v(t) e^{rt} for some function v(t). Compute:

**第 2 步 — 降阶法。** 尝试 y₂ = v(t) e^{rt}，v(t) 为待定函数。计算：

  y₂′ = v′ e^{rt} + r v e^{rt},
  y₂″ = v″ e^{rt} + 2r v′ e^{rt} + r² v e^{rt}.

Substitute into ay″ + by′ + cy = 0:

代入 ay″ + by′ + cy = 0：

  e^{rt} [a v″ + (2ar + b) v′ + (ar² + br + c) v] = 0.

Since r = −b/(2a), we have 2ar + b = 0. And since r is a root, ar² + br + c = 0. The equation reduces to:

由于 r = −b/(2a)，有 2ar + b = 0。又因 r 是根，ar² + br + c = 0。方程化为：

  a v″ = 0  →  v″ = 0  →  v(t) = At + B.

**Step 3 — Linearly independent second solution.** Take B = 0, A = 1: v(t) = t. So

**第 3 步 — 线性无关的第二个解。** 取 B = 0, A = 1：v(t) = t，故

  y₂ = t e^{rt}.

This is linearly independent from y₁ = e^{rt} (their ratio is t, non-constant).

它与 y₁ = e^{rt} 线性无关（比值为 t，非常数）。

**Step 4 — General solution.**

**第 4 步 — 通解。**

  **y(t) = (C₁ + C₂ t) e^{rt}.** ∎

**Physical example: critical damping.** For γ = ω₀, r = −γ (repeated), and y(t) = (C₁ + C₂t) e^{−γt}. This returns to zero the fastest among all non-oscillatory solutions — the design goal of shock absorbers and door closers.

**物理示例：临界阻尼。** 当 γ = ω₀ 时，r = −γ（重根），y(t) = (C₁ + C₂t) e^{−γt}。在所有非振荡解中，这是返回零最快的——这是减震器和门闩器的设计目标。

---

### B.3 — Case 3: Complex Conjugate Roots (Δ < 0) · 情形 3：复共轭根（Δ < 0）

**Step 1 — Complex roots.** When Δ < 0, the roots are r = α ± iβ where α = −b/(2a) and β = √(4ac − b²)/(2a) > 0. The complex solutions are e^{(α+iβ)t} and e^{(α−iβ)t}.

**第 1 步 — 复数根。** 当 Δ < 0 时，根为 r = α ± iβ，其中 α = −b/(2a)，β = √(4ac − b²)/(2a) > 0。复数解为 e^{(α+iβ)t} 和 e^{(α−iβ)t}。

**Step 2 — Construct real solutions using Euler's formula.** Since the ODE has real coefficients, the real and imaginary parts of any complex solution are themselves real solutions. Applying Euler's formula:

**第 2 步 — 用欧拉公式构造实数解。** 由于常微分方程系数为实数，任何复数解的实部和虚部各自也是实数解。应用欧拉公式：

  e^{(α+iβ)t} = e^{αt}(cos βt + i sin βt).

Real part: y₁ = e^{αt} cos βt. Imaginary part: y₂ = e^{αt} sin βt.

实部：y₁ = e^{αt} cos βt。虚部：y₂ = e^{αt} sin βt。

**Step 3 — Linear independence.** y₁/y₂ = cos βt / sin βt = cot βt is non-constant (β ≠ 0), so y₁ and y₂ are linearly independent.

**第 3 步 — 线性无关性。** y₁/y₂ = cos βt / sin βt = cot βt 非常数（β ≠ 0），故 y₁ 和 y₂ 线性无关。

**Step 4 — General solution.**

**第 4 步 — 通解。**

  **y(t) = e^{αt}(C₁ cos βt + C₂ sin βt).**

Equivalently, y(t) = R e^{αt} cos(βt − φ) where R = √(C₁² + C₂²) and tan φ = C₂/C₁. ∎

等价地，y(t) = R e^{αt} cos(βt − φ)，其中 R = √(C₁² + C₂²)，tan φ = C₂/C₁。∎

**Physical examples.** (i) Undamped oscillator (α = 0, a = 1, b = 0, c = ω²): r = ±iω, giving **y(t) = C₁ cos ωt + C₂ sin ωt** — simple harmonic motion. (ii) Underdamped oscillator (α = −γ < 0, β = √(ω₀² − γ²)): **y(t) = e^{−γt}(C₁ cos βt + C₂ sin βt)** — decaying oscillations. (iii) The TISE −(ℏ²/2m)ψ″ = Eψ for a free particle: same equation, solutions e^{±ikx} with k = √(2mE)/ℏ.

**物理示例。** (i) 无阻尼振子（α = 0, a = 1, b = 0, c = ω²）：r = ±iω，给出 **y(t) = C₁ cos ωt + C₂ sin ωt**——简谐运动。(ii) 欠阻尼振子（α = −γ < 0, β = √(ω₀² − γ²)）：**y(t) = e^{−γt}(C₁ cos βt + C₂ sin βt)**——衰减振荡。(iii) 自由粒子的定态薛定谔方程 −(ℏ²/2m)ψ″ = Eψ：同一方程，解为 e^{±ikx}，k = √(2mE)/ℏ。

---

## C. The Hermite Recursion from Series Substitution · 从级数代入推导厄米递推关系

**Setup.** The **Hermite equation** in the form arising from the quantum harmonic oscillator (after dimensional reduction) is

**准备工作。** 量子谐振子（经过量纲约化后）导出的**厄米方程**为

  y″ − 2x y′ + 2n y = 0,

where n is a non-negative integer (the quantum number). We seek polynomial solutions.

其中 n 为非负整数（量子数）。我们寻求多项式解。

**Step 1 — Substitute a power series.** Let y = Σ_{k=0}^{∞} aₖ xᵏ. Then:

**第 1 步 — 代入幂级数。** 令 y = Σ_{k=0}^{∞} aₖ xᵏ，则：

  y′ = Σ_{k=1}^{∞} k aₖ xᵏ⁻¹ = Σ_{k=0}^{∞} (k+1) aₖ₊₁ xᵏ,
  y″ = Σ_{k=2}^{∞} k(k−1) aₖ xᵏ⁻² = Σ_{k=0}^{∞} (k+2)(k+1) aₖ₊₂ xᵏ.

**Step 2 — Substitute into the equation.** The equation y″ − 2x y′ + 2n y = 0 becomes:

**第 2 步 — 代入方程。** 方程 y″ − 2x y′ + 2n y = 0 变为：

  Σ_{k=0}^{∞} (k+2)(k+1) aₖ₊₂ xᵏ − 2x Σ_{k=0}^{∞} (k+1) aₖ₊₁ xᵏ + 2n Σ_{k=0}^{∞} aₖ xᵏ = 0.

Rewrite the middle term: −2x · Σ (k+1) aₖ₊₁ xᵏ = −2 Σ (k+1) aₖ₊₁ xᵏ⁺¹ = −2 Σ_{k=1}^{∞} k aₖ xᵏ = −2 Σ_{k=0}^{∞} k aₖ xᵏ (the k=0 term vanishes).

改写中间项：−2x · Σ (k+1) aₖ₊₁ xᵏ = −2 Σ (k+1) aₖ₊₁ xᵏ⁺¹ = −2 Σ_{k=1}^{∞} k aₖ xᵏ = −2 Σ_{k=0}^{∞} k aₖ xᵏ（k=0 项为零）。

Collecting all terms at order xᵏ:

汇总 xᵏ 阶项：

  [(k+2)(k+1) aₖ₊₂ − 2k aₖ + 2n aₖ] xᵏ = 0  for all k ≥ 0.

**Step 3 — Extract the recursion.** Setting the coefficient of xᵏ to zero:

**第 3 步 — 提取递推关系。** 令 xᵏ 的系数为零：

  (k+2)(k+1) aₖ₊₂ = 2(k − n) aₖ.

Solving for aₖ₊₂:

解出 aₖ₊₂：

  **aₖ₊₂ = [2(k − n) / ((k+1)(k+2))] aₖ.**

This is the **Hermite recursion relation**. It shows that the coefficients of even and odd powers decouple: a₀ and a₂, a₄, … form one chain; a₁ and a₃, a₅, … form another. The two free parameters a₀ and a₁ correspond to the two linearly independent solutions.

这就是**厄米递推关系**。它表明偶次幂和奇次幂的系数相互解耦：a₀ 与 a₂, a₄, … 构成一条链；a₁ 与 a₃, a₅, … 构成另一条链。两个自由参数 a₀ 和 a₁ 对应两个线性无关的解。

**Step 4 — Termination argument.** For large k, aₖ₊₂/aₖ ≈ 2/k, the same ratio as in the series for e^{x²} = Σ x^{2m}/m!. If the series does not terminate, then y(x) ~ e^{x²} for large |x|. In the quantum oscillator context, the full wavefunction is ψ(x) = y(x) e^{−x²/2}; if y ~ e^{x²}, then ψ ~ e^{x²/2} which is not normalizable (not in L²(ℝ)). We therefore require the series to terminate.

**第 4 步 — 终止论证。** 对大 k，aₖ₊₂/aₖ ≈ 2/k，与 e^{x²} = Σ x^{2m}/m! 的级数比值相同。若级数不终止，则对大 |x| 有 y(x) ~ e^{x²}。在量子谐振子中，完整波函数为 ψ(x) = y(x) e^{−x²/2}；若 y ~ e^{x²}，则 ψ ~ e^{x²/2}，不可归一化（不属于 L²(ℝ)）。因此要求级数终止。

**Step 5 — Termination condition.** From the recursion aₖ₊₂ = [2(k − n)/((k+1)(k+2))] aₖ: the numerator 2(k − n) vanishes when k = n. If n is a non-negative integer and we choose the "chain" (even or odd) that contains the term k = n, then aₙ₊₂ = 0 and all subsequent terms vanish. Setting the other chain's starting coefficient to zero (a₁ = 0 for even-n polynomial, a₀ = 0 for odd-n), we obtain a terminating polynomial of degree n — the **n-th Hermite polynomial** Hₙ(x).

**第 5 步 — 终止条件。** 由递推关系 aₖ₊₂ = [2(k − n)/((k+1)(k+2))] aₖ：当 k = n 时，分子 2(k − n) 为零。若 n 是非负整数，且我们选择包含 k = n 项的"链"（偶次或奇次），则 aₙ₊₂ = 0，此后所有项均为零。令另一条链的起始系数为零（n 为偶数时令 a₁ = 0，n 为奇数时令 a₀ = 0），得到一个 n 次终止多项式——**第 n 阶厄米多项式** Hₙ(x)。

**Step 6 — First few Hermite polynomials.** From the recursion:

**第 6 步 — 前几个厄米多项式。** 由递推关系：

  n=0: a₀ = 1, all odd terms zero → H₀(x) = 1.
  n=1: a₁ = 1 (set a₀ = 0), a₃ = 0 → H₁(x) = 2x (with physicist's normalization).
  n=2: a₀ = 1, a₂ = [2(0−2)/(1·2)] a₀ = −2, a₄ = 0 → H₂(x) = 4x² − 2.
  n=3: a₁ = 1, a₃ = [2(1−3)/(2·3)] a₁ = −2/3 → H₃(x) = 8x³ − 12x.

  n=0：a₀ = 1，所有奇数项为零 → H₀(x) = 1。
  n=1：a₁ = 1（令 a₀ = 0），a₃ = 0 → H₁(x) = 2x（物理学家归一化）。
  n=2：a₀ = 1，a₂ = [2(0−2)/(1·2)] a₀ = −2，a₄ = 0 → H₂(x) = 4x² − 2。
  n=3：a₁ = 1，a₃ = [2(1−3)/(2·3)] a₁ = −2/3 → H₃(x) = 8x³ − 12x。

The quantum harmonic oscillator wavefunctions are ψₙ(x) ∝ Hₙ(√(mω/ℏ) x) e^{−mωx²/2ℏ}, normalized in L²(ℝ). ∎

量子谐振子波函数为 ψₙ(x) ∝ Hₙ(√(mω/ℏ) x) e^{−mωx²/2ℏ}，在 L²(ℝ) 中归一化。∎

---

## D. Separation of Variables for the Heat Equation · 热传导方程的分离变量

**Setup.** Consider the heat equation on a rod of length L with Dirichlet boundary conditions (temperature fixed to zero at the ends):

**准备工作。** 考虑长度为 L 的杆上的热传导方程，满足狄利克雷边界条件（两端温度固定为零）：

  ∂u/∂t = D ∂²u/∂x²,   u(0, t) = u(L, t) = 0,   u(x, 0) = f(x).

**Step 1 — Assume a separated solution.** Let u(x, t) = X(x) T(t) with X, T not identically zero.

**第 1 步 — 假设可分离解。** 令 u(x, t) = X(x) T(t)，X, T 不恒为零。

**Step 2 — Substitute into the PDE.**

**第 2 步 — 代入偏微分方程。**

  X(x) T′(t) = D X″(x) T(t).

Divide both sides by D X(x) T(t) (valid where neither X nor T is zero):

两端除以 D X(x) T(t)（在 X 和 T 均不为零处有效）：

  T′(t) / (D T(t)) = X″(x) / X(x).

**Step 3 — Separation constant.** The left side depends only on t and the right side only on x. Since they are equal for all (x, t), both sides must equal a common constant, which we call −λ (the sign choice anticipates physical solutions):

**第 3 步 — 分离常数。** 左侧只依赖 t，右侧只依赖 x。由于对所有 (x, t) 均相等，两侧必须等于同一常数，记为 −λ（负号的选取预示物理解的形式）：

  T′/(DT) = X″/X = −λ.

This gives two separate ODEs:

由此得到两个独立的常微分方程：

  **T′ = −D λ T**  (in t),
  **X″ = −λ X**  (in x).

**Step 4 — Solve the spatial ODE with boundary conditions.** The equation X″ = −λX with X(0) = X(L) = 0.

**第 4 步 — 结合边界条件求解空间常微分方程。** 方程 X″ = −λX，边界条件 X(0) = X(L) = 0。

Case λ ≤ 0: If λ = 0, then X″ = 0, giving X = Ax + B; boundary conditions force A = B = 0, so X ≡ 0 (trivial). If λ < 0 (set λ = −μ² with μ > 0), then X″ = μ²X, giving X = Ae^{μx} + Be^{−μx}; boundary conditions again force A = B = 0. So λ must be positive.

λ ≤ 0 的情形：若 λ = 0，则 X″ = 0，给出 X = Ax + B；边界条件迫使 A = B = 0，故 X ≡ 0（平凡解）。若 λ < 0（令 λ = −μ²，μ > 0），则 X″ = μ²X，给出 X = Ae^{μx} + Be^{−μx}；边界条件再次迫使 A = B = 0。因此 λ 必须为正数。

Case λ > 0 (set λ = k²): X″ = −k²X has general solution X(x) = A sin(kx) + B cos(kx). From X(0) = 0: B = 0. From X(L) = 0: A sin(kL) = 0. Non-trivial solution requires sin(kL) = 0, i.e., kL = nπ for n = 1, 2, 3, …

λ > 0 的情形（令 λ = k²）：X″ = −k²X 的通解为 X(x) = A sin(kx) + B cos(kx)。由 X(0) = 0：B = 0。由 X(L) = 0：A sin(kL) = 0。非平凡解要求 sin(kL) = 0，即 kL = nπ，n = 1, 2, 3, …

The **eigenvalues** are λₙ = (nπ/L)² and the **eigenfunctions** are Xₙ(x) = sin(nπx/L).

**本征值**为 λₙ = (nπ/L)²，**本征函数**为 Xₙ(x) = sin(nπx/L)。

**Step 5 — Solve the temporal ODE.** For each n:

**第 5 步 — 求解时间常微分方程。** 对每个 n：

  T′ = −Dλₙ T  →  Tₙ(t) = e^{−Dλₙ t} = e^{−D(nπ/L)² t}.

**Step 6 — Superpose the modes.** The general solution satisfying the PDE and boundary conditions is

**第 6 步 — 叠加各模式。** 满足偏微分方程和边界条件的通解为

  **u(x, t) = Σ_{n=1}^{∞} Bₙ sin(nπx/L) e^{−D(nπ/L)² t}.**

**Step 7 — Apply the initial condition.** At t = 0:

**第 7 步 — 应用初始条件。** 在 t = 0 处：

  u(x, 0) = Σ_{n=1}^{∞} Bₙ sin(nπx/L) = f(x).

This is a Fourier sine series. Using orthogonality ∫₀ᴸ sin(mπx/L) sin(nπx/L) dx = (L/2) δₘₙ:

这是傅里叶正弦级数。利用正交性 ∫₀ᴸ sin(mπx/L) sin(nπx/L) dx = (L/2) δₘₙ：

  **Bₙ = (2/L) ∫₀ᴸ f(x) sin(nπx/L) dx.** ∎

**Physical interpretation.** Each mode decays at rate Dλₙ = D(nπ/L)². High-frequency modes (large n) decay rapidly; low-frequency modes persist longest. This is why temperature profiles eventually smooth out — a direct consequence of the Fourier structure of the heat equation.

**物理解释。** 每个模式以速率 Dλₙ = D(nπ/L)² 衰减。高频模式（大 n）衰减快；低频模式持续最长。这正是温度分布最终趋于平滑的原因——这是热传导方程傅里叶结构的直接结果。

**Existence and uniqueness.** The series solution converges in L²([0,L]) for any square-integrable initial condition f(x) (by Parseval's theorem). If f is also continuous and piecewise smooth, the series converges pointwise. Uniqueness follows from the energy estimate: if u₁ and u₂ are two solutions, their difference w = u₁ − u₂ satisfies w_t = D w_{xx} with zero boundary and initial conditions; then d/dt ∫₀ᴸ w² dx = −2D ∫₀ᴸ (w_x)² dx ≤ 0, forcing ∫w² dx → 0.

**存在性与唯一性。** 对任意平方可积初始条件 f(x)（由帕塞瓦尔定理），级数解在 L²([0,L]) 中收敛。若 f 还连续且分段光滑，则级数逐点收敛。唯一性由能量估计得出：若 u₁ 和 u₂ 是两个解，其差 w = u₁ − u₂ 满足 w_t = D w_{xx}，边界和初始条件均为零；则 d/dt ∫₀ᴸ w² dx = −2D ∫₀ᴸ (w_x)² dx ≤ 0，迫使 ∫w² dx → 0。

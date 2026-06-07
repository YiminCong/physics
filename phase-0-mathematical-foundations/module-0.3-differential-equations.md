# Module 0.3 — Differential Equations · 微分方程

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

Physics is written in differential equations. The second-order linear ODE in particular is *the* equation you'll meet again and again — oscillators, waves, and the Schrödinger equation are all this one form.

</td>
<td>

物理学是用微分方程写成的。二阶线性常微分方程尤为关键，是你将一再遇到的方程——振子、波以及薛定谔方程，本质上都是这同一种形式。

</td>
</tr>
</table>

---

## 1. First-Order ODEs · 一阶常微分方程

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** A first-order ODE relates a function y to its first derivative y′. Two solvable types:
- **Separable:** dy/dx = g(x)h(y) → rearrange to ∫ dy/h(y) = ∫ g(x) dx.
- **Linear:** y′ + p(x)y = q(x), solved with the **integrating factor** μ = e^{∫p dx}.

</td>
<td>

**定义。** 一阶常微分方程将函数 y 与其一阶导数 y′ 联系起来。两种可求解的类型：
- **可分离型：** dy/dx = g(x)h(y) → 整理为 ∫ dy/h(y) = ∫ g(x) dx。
- **线性型：** y′ + p(x)y = q(x)，用**积分因子** μ = e^{∫p dx} 求解。

</td>
</tr>
<tr>
<td>

**Demonstration.** Solve dy/dx = −k y (separable):

  ∫ dy/y = ∫ −k dx → ln y = −kx + C → **y = y₀ e^{−kx}** (exponential decay).

</td>
<td>

**演示。** 求解 dy/dx = −k y（可分离型）：

  ∫ dy/y = ∫ −k dx → ln y = −kx + C → **y = y₀ e^{−kx}**（指数衰减）。

</td>
</tr>
<tr>
<td>

**Application.** Radioactive decay, RC-circuit discharge, Newton's law of cooling. This is your first encounter with the exponential — the function that dominates physics because it's its own derivative.

</td>
<td>

**应用。** 放射性衰变、RC 电路放电、牛顿冷却定律。这是你与指数函数的首次相遇——它在物理学中无处不在，正因为它是自身的导数。

</td>
</tr>
</table>

---

## 2. Second-Order Linear ODEs with Constant Coefficients ⭐ · 常系数二阶线性常微分方程

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** The equation a y″ + b y′ + c y = 0. Guess y = e^{rt}; substituting gives the **characteristic equation** a r² + b r + c = 0. The roots determine behavior:
- two real roots → exponential (overdamped),
- a repeated root → critical damping,
- complex roots → oscillation.

</td>
<td>

**定义。** 方程 a y″ + b y′ + c y = 0。令 y = e^{rt}，代入得**特征方程** a r² + b r + c = 0。根的类型决定行为：
- 两个实根 → 指数型（过阻尼），
- 重根 → 临界阻尼，
- 复数根 → 振荡。

</td>
</tr>
<tr>
<td>

**Demonstration.** The undamped oscillator y″ + ω²y = 0. Characteristic equation r² + ω² = 0 → r = ±iω, so

  **y(t) = A cos ωt + B sin ωt.**

Add damping: y″ + 2γy′ + ω₀²y = 0 gives decaying oscillations when γ < ω₀.

</td>
<td>

**演示。** 无阻尼振子 y″ + ω²y = 0。特征方程 r² + ω² = 0 → r = ±iω，故

  **y(t) = A cos ωt + B sin ωt。**

加入阻尼：y″ + 2γy′ + ω₀²y = 0，当 γ < ω₀ 时给出衰减振荡。

</td>
</tr>
<tr>
<td>

**Application.** This single equation is simple harmonic motion, the damped/driven oscillator (Phase 1), AC circuits, and — most importantly — the **time-independent Schrödinger equation** for constant-potential regions is exactly this form (Phase 3). If you own one ODE, own this one.

</td>
<td>

**应用。** 这一个方程就是简谐运动、阻尼/受驱振子（第 1 阶段）、交流电路，以及——最重要的——常势能区域的**定态薛定谔方程**恰好是这种形式（第 3 阶段）。如果你只掌握一个常微分方程，就掌握这一个。

</td>
</tr>
</table>

---

## 3. Series Solutions & Special Functions · 级数解与特殊函数

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** When coefficients vary with x, you can't guess e^{rt}. Instead substitute a power series y = Σ aₙ xⁿ and solve a **recursion** for the coefficients (the Frobenius method). Specific physics equations generate named **special functions**: Legendre polynomials, Hermite polynomials, Bessel functions, Laguerre polynomials.

</td>
<td>

**定义。** 当系数随 x 变化时，无法猜测 e^{rt}。此时代入幂级数 y = Σ aₙ xⁿ，并对系数求解**递推关系**（Frobenius 方法）。特定的物理方程会生成有名字的**特殊函数**：勒让德多项式、厄米多项式、贝塞尔函数、拉盖尔多项式。

</td>
</tr>
<tr>
<td>

**Demonstration.** Substituting y = Σ aₙxⁿ into an equation like y″ − 2x y′ + 2n y = 0 (Hermite's equation) yields a recursion aₖ₊₂ = [2(k−n)/((k+1)(k+2))] aₖ that terminates into polynomials — the Hermite polynomials.

</td>
<td>

**演示。** 将 y = Σ aₙxⁿ 代入方程 y″ − 2x y′ + 2n y = 0（厄米方程），得到递推关系 aₖ₊₂ = [2(k−n)/((k+1)(k+2))] aₖ，该递推在有限项处截断，给出多项式——即厄米多项式。

</td>
</tr>
<tr>
<td>

**Application.** These aren't abstract: **Hermite polynomials are the quantum harmonic oscillator wavefunctions**, **Legendre polynomials/spherical harmonics describe angular momentum**, and **Laguerre polynomials appear in the hydrogen atom's radial part** (all Phase 3). Meeting them now means recognizing them later instead of being ambushed.

</td>
<td>

**应用。** 这些并非抽象概念：**厄米多项式是量子谐振子的波函数**，**勒让德多项式／球谐函数描述角动量**，**拉盖尔多项式出现在氢原子径向部分**（均见第 3 阶段）。现在认识它们，意味着之后能够识别，而非措手不及。

</td>
</tr>
</table>

---

## 4. Partial Differential Equations & Separation of Variables ⭐ · 偏微分方程与分离变量法

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

**Definition.** A PDE involves partial derivatives in several variables. The workhorse technique is **separation of variables**: assume the solution factorizes, e.g. u(x,t) = X(x)T(t), turning one PDE into several ODEs. The three canonical PDEs of physics:
- **Wave equation:** ∂²u/∂t² = c²∇²u
- **Heat/diffusion equation:** ∂u/∂t = D∇²u
- **Laplace's equation:** ∇²u = 0

</td>
<td>

**定义。** 偏微分方程含有多个变量的偏导数。核心技巧是**分离变量法**：假设解可因式分解，如 u(x,t) = X(x)T(t)，从而将一个偏微分方程化为多个常微分方程。物理学中三类典型偏微分方程：
- **波动方程：** ∂²u/∂t² = c²∇²u
- **热传导／扩散方程：** ∂u/∂t = D∇²u
- **拉普拉斯方程：** ∇²u = 0

</td>
</tr>
<tr>
<td>

**Demonstration.** Heat equation on a rod, u(x,t) = X(x)T(t):

  X T′ = D X″ T → T′/(D T) = X″/X = −λ (a constant).

This splits into T′ = −Dλ T (giving T ∝ e^{−Dλt}) and X″ = −λX (giving sines/cosines). The full solution is a superposition of modes e^{−Dλt} sin(√λ x).

</td>
<td>

**演示。** 对杆上的热方程令 u(x,t) = X(x)T(t)：

  X T′ = D X″ T → T′/(D T) = X″/X = −λ（常数）。

这分离为 T′ = −Dλ T（给出 T ∝ e^{−Dλt}）和 X″ = −λX（给出正弦／余弦）。完整解是各模式 e^{−Dλt} sin(√λ x) 的叠加。

</td>
</tr>
<tr>
<td>

**Application.** The **Schrödinger equation separates** into a spatial part (the time-independent Schrödinger equation) and a temporal part e^{−iEt/ℏ} by exactly this method (Phase 3). **Laplace's equation** is the electrostatics boundary-value problem you'll solve in Phase 1. The same separation logic recurs throughout the curriculum.

</td>
<td>

**应用。** **薛定谔方程**正是用这一方法**分离**为空间部分（定态薛定谔方程）和时间部分 e^{−iEt/ℏ}（第 3 阶段）。**拉普拉斯方程**是第 1 阶段将要求解的静电学边值问题。同样的分离逻辑贯穿整个课程。

</td>
</tr>
</table>

---

## Module 0.3 Self-Test (blank page) · 模块 0.3 自测（空白页）

<table>
<tr><th>English</th><th>中文</th></tr>
<tr>
<td>

1. Solve dy/dx = −ky and identify the physical situations it models.
2. Solve y″ + ω²y = 0 and y″ + 2γy′ + ω₀²y = 0; classify the damping regimes.
3. Name the special functions tied to the oscillator, angular momentum, and hydrogen.
4. Separate the heat equation into ODEs and write the mode solution.
5. Explain how separation of variables applies to the Schrödinger equation.

</td>
<td>

1. 求解 dy/dx = −ky，并指出它所描述的物理情景。
2. 求解 y″ + ω²y = 0 和 y″ + 2γy′ + ω₀²y = 0；对阻尼状态进行分类。
3. 说出与谐振子、角动量和氢原子分别对应的特殊函数。
4. 对热方程进行变量分离，写出各模式解。
5. 解释分离变量法如何应用于薛定谔方程。

</td>
</tr>
</table>

---

← Previous: [Module 0.2 — Linear Algebra](./module-0.2-linear-algebra.md) · [Phase 0 index](./README.md) · Next: [Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md) →

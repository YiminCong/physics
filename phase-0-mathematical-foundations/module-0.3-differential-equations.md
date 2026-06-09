---
title: "Module 0.3 — Differential Equations"
parent: "Phase 0 — Mathematical Foundations"
nav_order: 3
---

# Module 0.3 — Differential Equations
**模块 0.3 — 微分方程**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-0.3-differential-equations-derivations.md)

Physics is written in differential equations. The second-order linear ODE in particular
is *the* equation you'll meet again and again — oscillators, waves, and the Schrödinger
equation are all this one form.

物理学用微分方程书写。二阶线性常微分方程尤为重要，它是你将一再遇到的方程——振子、波以及薛定谔方程都属于这同一种形式。

---

## 1. First-Order ODEs · 一阶常微分方程

**Definition.** A first-order ODE relates a function $y$ to its first derivative $y'$. Two solvable types:
- **Separable:** $dy/dx = g(x)h(y)$ → rearrange to $\int dy/h(y) = \int g(x)\, dx$.
- **Linear:** $y' + p(x)y = q(x)$, solved with the **integrating factor** $\mu = e^{\int p\, dx}$.

**定义。** 一阶常微分方程将函数 $y$ 与其一阶导数 $y'$ 联系起来。两类可解类型：
- **可分离方程：** $dy/dx = g(x)h(y)$ → 整理为 $\int dy/h(y) = \int g(x)\, dx$。
- **线性方程：** $y' + p(x)y = q(x)$，用**积分因子** $\mu = e^{\int p\, dx}$ 求解。

**Demonstration.** Solve $dy/dx = -k y$ (separable):

**演示。** 求解 $dy/dx = -k y$（可分离方程）：

$$ \int \frac{dy}{y} = \int -k\, dx \implies \ln y = -kx + C \implies y = y_0\, e^{-kx} \quad (\text{exponential decay}). $$

**Application.** Radioactive decay, RC-circuit discharge, Newton's law of cooling. This is your first encounter with the exponential — the function that dominates physics because it's its own derivative.

**应用。** 放射性衰变、RC 电路放电、牛顿冷却定律。这是你第一次遇到指数函数——因为它是自身的导数，所以在物理学中无处不在。

---

## 2. Second-Order Linear ODEs with Constant Coefficients ⭐ · 常系数二阶线性常微分方程 ⭐

**Definition.** The equation $a y'' + b y' + c y = 0$. Guess $y = e^{rt}$; substituting gives the **characteristic equation** $a r^2 + b r + c = 0$. The roots determine behavior:
- two real roots → exponential (overdamped),
- a repeated root → critical damping,
- complex roots → oscillation.

**定义。** 方程 $a y'' + b y' + c y = 0$。猜测 $y = e^{rt}$；代入后得到**特征方程** $a r^2 + b r + c = 0$。根的类型决定行为：
- 两个实根 → 指数型（过阻尼），
- 重根 → 临界阻尼，
- 复数根 → 振荡。

**Demonstration.** The undamped oscillator $y'' + \omega^2 y = 0$. Characteristic equation $r^2 + \omega^2 = 0 \implies r = \pm i\omega$, so

**演示。** 无阻尼振子 $y'' + \omega^2 y = 0$。特征方程 $r^2 + \omega^2 = 0 \implies r = \pm i\omega$，因此

$$ y(t) = A \cos \omega t + B \sin \omega t. $$

Add damping: $y'' + 2\gamma y' + \omega_0^2 y = 0$ gives decaying oscillations when $\gamma < \omega_0$.

加入阻尼：当 $\gamma < \omega_0$ 时，$y'' + 2\gamma y' + \omega_0^2 y = 0$ 给出衰减振荡。

**Application.** This single equation is simple harmonic motion, the damped/driven oscillator (Phase 1), AC circuits, and — most importantly — the **time-independent Schrödinger equation** for constant-potential regions is exactly this form (Phase 3). If you own one ODE, own this one.

**应用。** 这一个方程就是简谐运动、阻尼/驱动振子（第 1 阶段）、交流电路，以及——最重要的是——常势区域的**定态薛定谔方程**恰好就是这种形式（第 3 阶段）。如果只能掌握一个常微分方程，就掌握这个。

---

## 3. Series Solutions & Special Functions · 级数解与特殊函数

**Definition.** When coefficients vary with $x$, you can't guess $e^{rt}$. Instead substitute a power series $y = \sum a_n x^n$ and solve a **recursion** for the coefficients (the Frobenius method). Specific physics equations generate named **special functions**: Legendre polynomials, Hermite polynomials, Bessel functions, Laguerre polynomials.

**定义。** 当系数随 $x$ 变化时，无法猜测 $e^{rt}$。应代入幂级数 $y = \sum a_n x^n$，并对系数建立**递推关系**（弗罗贝尼乌斯方法）。特定物理方程会生成具名的**特殊函数**：勒让德多项式、厄米多项式、贝塞尔函数、拉盖尔多项式。

**Demonstration.** Substituting $y = \sum a_n x^n$ into an equation like $y'' - 2x y' + 2n y = 0$ (Hermite's equation) yields a recursion $a_{k+2} = [2(k-n)/((k+1)(k+2))]\, a_k$ that terminates into polynomials — the Hermite polynomials.

**演示。** 将 $y = \sum a_n x^n$ 代入 $y'' - 2x y' + 2n y = 0$（厄米方程）等方程，得到递推关系 $a_{k+2} = [2(k-n)/((k+1)(k+2))]\, a_k$，该递推在有限步终止，给出多项式——即厄米多项式。

**Application.** These aren't abstract: **Hermite polynomials are the quantum harmonic oscillator wavefunctions**, **Legendre polynomials/spherical harmonics describe angular momentum**, and **Laguerre polynomials appear in the hydrogen atom's radial part** (all Phase 3). Meeting them now means recognizing them later instead of being ambushed.

**应用。** 这些并非抽象概念：**厄米多项式是量子谐振子的波函数**，**勒让德多项式/球谐函数描述角动量**，**拉盖尔多项式出现在氢原子的径向部分**（均见第 3 阶段）。现在接触它们，意味着以后遇到时能一眼识别，而不是措手不及。

---

## 4. Partial Differential Equations & Separation of Variables ⭐ · 偏微分方程与分离变量法 ⭐

**Definition.** A PDE involves partial derivatives in several variables. The workhorse technique is **separation of variables**: assume the solution factorizes, e.g. u(x,t) = X(x)T(t), turning one PDE into several ODEs. The three canonical PDEs of physics:
- **Wave equation:** $\partial^2 u/\partial t^2 = c^2 \nabla^2 u$
- **Heat/diffusion equation:** $\partial u/\partial t = D \nabla^2 u$
- **Laplace's equation:** $\nabla^2 u = 0$

**定义。** 偏微分方程涉及多个变量的偏导数。主要求解技巧是**分离变量法**：假设解可以因式分解，例如 $u(x,t) = X(x)T(t)$，从而将一个偏微分方程化为若干常微分方程。物理中三类典型偏微分方程：
- **波动方程：** $\partial^2 u/\partial t^2 = c^2 \nabla^2 u$
- **热传导/扩散方程：** $\partial u/\partial t = D \nabla^2 u$
- **拉普拉斯方程：** $\nabla^2 u = 0$

**Demonstration.** Heat equation on a rod, $u(x,t) = X(x)T(t)$:

**演示。** 杆上的热传导方程，$u(x,t) = X(x)T(t)$：

$$ X T' = D X'' T \implies \frac{T'}{D T} = \frac{X''}{X} = -\lambda \quad (\text{a constant}). $$

This splits into $T' = -D\lambda T$ (giving $T \propto e^{-D\lambda t}$) and $X'' = -\lambda X$ (giving sines/cosines). The full solution is a superposition of modes $e^{-D\lambda t} \sin(\sqrt{\lambda}\, x)$.

这分裂为 $T' = -D\lambda T$（给出 $T \propto e^{-D\lambda t}$）和 $X'' = -\lambda X$（给出正弦/余弦）。完整解是各模式 $e^{-D\lambda t} \sin(\sqrt{\lambda}\, x)$ 的叠加。

**Application.** The **Schrödinger equation separates** into a spatial part (the time-independent Schrödinger equation) and a temporal part $e^{-iEt/\hbar}$ by exactly this method (Phase 3). **Laplace's equation** is the electrostatics boundary-value problem you'll solve in Phase 1. The same separation logic recurs throughout the curriculum.

**应用。** **薛定谔方程**正是用这种方法分离为空间部分（定态薛定谔方程）和时间部分 $e^{-iEt/\hbar}$（第 3 阶段）。**拉普拉斯方程**是第 1 阶段将要求解的静电学边值问题。同样的分离变量逻辑贯穿整个课程。

---

## Module 0.3 Self-Test (blank page)

1. Solve $dy/dx = -ky$ and identify the physical situations it models.
2. Solve $y'' + \omega^2 y = 0$ and $y'' + 2\gamma y' + \omega_0^2 y = 0$; classify the damping regimes.
3. Name the special functions tied to the oscillator, angular momentum, and hydrogen.
4. Separate the heat equation into ODEs and write the mode solution.
5. Explain how separation of variables applies to the Schrödinger equation.

If solid, advance to **[Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md)**.

**自测（空白页）**

1. 求解 $dy/dx = -ky$，并说明它所模拟的物理情景。
2. 求解 $y'' + \omega^2 y = 0$ 和 $y'' + 2\gamma y' + \omega_0^2 y = 0$；对各阻尼情形进行分类。
3. 写出与谐振子、角动量和氢原子相关的特殊函数名称。
4. 对热传导方程进行变量分离，写出模式解。
5. 解释分离变量法如何应用于薛定谔方程。

---

← *Phase 0 index: [Mathematical Foundations](./README.md)* · Next: [Module 0.4 — Complex Analysis](./module-0.4-complex-analysis.md) →

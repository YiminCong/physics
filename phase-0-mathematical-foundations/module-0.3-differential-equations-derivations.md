---
title: "Derivations — Module 0.3: Differential Equations"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 0.3: Differential Equations
# 推导 — 模块 0.3：微分方程

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.3](./module-0.3-differential-equations.md). Full step-by-step proofs and derivations: the integrating factor for the first-order linear ODE; the general solution of the second-order constant-coefficient ODE for all three root cases; the Hermite recursion relation derived from series substitution, with the termination argument; and complete separation of the heat equation. English first, then 中文.
> [模块 0.3](./module-0.3-differential-equations.md) 的配套文档：完整逐步证明与推导：一阶线性常微分方程的积分因子法；常系数二阶线性常微分方程在三种根情形下的通解；由级数代入推导厄米递推关系及其终止论证；以及热传导方程的完整分离变量过程。先英文，后中文。

---

## A. The Integrating Factor for the First-Order Linear ODE · 一阶线性常微分方程的积分因子

**Claim.** The equation $y' + p(x) y = q(x)$ has the general solution

**命题。** 方程 $y' + p(x) y = q(x)$ 的通解为

$$ y(x) = \frac{1}{\mu(x)}\left[\int \mu(x) q(x)\,dx + C\right], \quad \text{where } \mu(x) = e^{\int p(x)\,dx}. $$

**Step 1 — Motivation: seek a function $\mu(x)$ that makes the left side a perfect derivative.** If we multiply both sides of $y' + p(x)y = q(x)$ by an unknown function $\mu(x)$, we obtain

**第 1 步 — 动机：寻找使左侧成为完全导数的函数 $\mu(x)$。** 将方程 $y' + p(x)y = q(x)$ 两端乘以未知函数 $\mu(x)$，得

$$ \mu y' + \mu p y = \mu q. $$

We want the left side to equal $\frac{d}{dx}(\mu y)$. Expanding $\frac{d}{dx}(\mu y) = \mu y' + \mu' y$. Matching coefficients of $y$:

我们希望左侧等于 $\frac{d}{dx}(\mu y)$。展开 $\frac{d}{dx}(\mu y) = \mu y' + \mu' y$，比较 $y$ 的系数：

$$ \mu p = \mu', \quad \text{i.e.} \quad \mu'/\mu = p(x). $$

**Step 2 — Solve for $\mu$.** The equation $\mu' = p(x) \mu$ is separable:

**第 2 步 — 求 $\mu$。** 方程 $\mu' = p(x) \mu$ 是可分离的：

$$ \frac{d\mu}{\mu} = p(x)\,dx \;\to\; \ln \mu = \int p(x)\,dx \;\to\; \boxed{\,\mu(x) = e^{\int p(x)\,dx}\,}. $$

(We take the particular antiderivative without the integration constant $C$, since multiplying by a constant would cancel out.)

（取特定原函数，不加积分常数 $C$，因为乘以常数会被约去。）

**Step 3 — Rewrite and integrate.** With this $\mu$, the original equation becomes

**第 3 步 — 改写并积分。** 有了此 $\mu$，原方程变为

$$ \frac{d}{dx}(\mu y) = \mu q. $$

Integrate both sides:

两端积分：

$$ \mu(x) y(x) = \int \mu(x) q(x)\,dx + C. $$

**Step 4 — Solve for $y$.**

**第 4 步 — 解出 $y$。**

$$ \boxed{\, y(x) = \frac{1}{\mu(x)}\left[\int \mu(x) q(x)\,dx + C\right]. \,} \qquad \blacksquare $$

**Domain condition.** The solution is valid on any interval where $p(x)$ and $q(x)$ are continuous. The constant $C$ is fixed by one initial condition $y(x_0) = y_0$.

**定义域条件。** 解在 $p(x)$ 和 $q(x)$ 连续的任何区间上有效。常数 $C$ 由一个初始条件 $y(x_0) = y_0$ 确定。

**Example: exponential decay.** $y' + k y = 0$. Here $p = k$, $q = 0$, $\mu = e^{kx}$. Then $y = e^{-kx}\left[\int 0\,dx + C\right] = C e^{-kx}$. With $y(0) = y_0$: $\boldsymbol{y = y_0 e^{-kx}}$.

**示例：指数衰减。** $y' + k y = 0$。此时 $p = k, q = 0, \mu = e^{kx}$。则 $y = e^{-kx}\left[\int 0\,dx + C\right] = C e^{-kx}$。由 $y(0) = y_0$：$\boldsymbol{y = y_0 e^{-kx}}$。

---

## B. Second-Order Linear ODE with Constant Coefficients — All Three Cases · 常系数二阶线性常微分方程——三种情形

**Setup.** We solve $ay'' + by' + cy = 0$ with $a \ne 0$. The substitution $y = e^{rt}$ converts the equation into $a(r^2 e^{rt}) + b(r e^{rt}) + c(e^{rt}) = 0$; since $e^{rt} \ne 0$, this gives the **characteristic equation**:

**准备工作。** 求解 $ay'' + by' + cy = 0$，$a \ne 0$。代入 $y = e^{rt}$，得 $a(r^2 e^{rt}) + b(r e^{rt}) + c(e^{rt}) = 0$；由于 $e^{rt} \ne 0$，得**特征方程**：

$$ \boldsymbol{a r^2 + b r + c = 0}, \quad \text{roots} \quad r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}. $$

The discriminant $\Delta = b^2 - 4ac$ determines three cases.

判别式 $\Delta = b^2 - 4ac$ 决定三种情形。

---

### B.1 — Case 1: Two Distinct Real Roots ($\Delta > 0$) · 情形 1：两个不同实根（$\Delta > 0$）

**Step 1 — Two independent solutions.** For roots $r_1 \ne r_2$ (both real), both $y_1 = e^{r_1 t}$ and $y_2 = e^{r_2 t}$ satisfy the ODE. They are linearly independent because $e^{r_1 t}/e^{r_2 t} = e^{(r_1 - r_2)t}$ is non-constant ($r_1 \ne r_2$).

**第 1 步 — 两个独立解。** 对于 $r_1 \ne r_2$（均为实数），$y_1 = e^{r_1 t}$ 和 $y_2 = e^{r_2 t}$ 均满足常微分方程。它们线性无关，因为 $e^{r_1 t}/e^{r_2 t} = e^{(r_1 - r_2)t}$ 非常数（$r_1 \ne r_2$）。

**Step 2 — General solution by superposition.**

**第 2 步 — 由叠加原理得通解。**

$$ \boldsymbol{y(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}.} $$

**Step 3 — Physical example: overdamped oscillator.** For $y'' + 2\gamma y' + \omega_0^2 y = 0$ with $\gamma > \omega_0 > 0$, the roots $r = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$ are both real and negative. The general solution is a sum of two decaying exponentials with no oscillation — the system returns to equilibrium monotonically.

**第 3 步 — 物理示例：过阻尼振子。** 对 $y'' + 2\gamma y' + \omega_0^2 y = 0$，$\gamma > \omega_0 > 0$，根 $r = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$ 均为实数且为负。通解是两个衰减指数之和，无振荡——系统单调地返回平衡。

The general solution $y(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$ with $C_1, C_2$ determined by initial conditions $y(0)$ and $y'(0)$. $\blacksquare$

通解 $y(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$，$C_1, C_2$ 由初始条件 $y(0)$ 和 $y'(0)$ 确定。$\blacksquare$

---

### B.2 — Case 2: Repeated Real Root ($\Delta = 0$) · 情形 2：重实根（$\Delta = 0$）

**Step 1 — Only one exponential.** When $\Delta = 0$, there is only one root $r = -b/(2a)$. The function $y_1 = e^{rt}$ is one solution, but we need two linearly independent solutions.

**第 1 步 — 只有一个指数解。** 当 $\Delta = 0$ 时，只有一个根 $r = -b/(2a)$。函数 $y_1 = e^{rt}$ 是一个解，但我们需要两个线性无关的解。

**Step 2 — Reduction of order.** Try $y_2 = v(t) e^{rt}$ for some function $v(t)$. Compute:

**第 2 步 — 降阶法。** 尝试 $y_2 = v(t) e^{rt}$，$v(t)$ 为待定函数。计算：

$$ \begin{aligned} y_2' &= v' e^{rt} + r v e^{rt}, \\ y_2'' &= v'' e^{rt} + 2r v' e^{rt} + r^2 v e^{rt}. \end{aligned} $$

Substitute into $ay'' + by' + cy = 0$:

代入 $ay'' + by' + cy = 0$：

$$ e^{rt}\left[a v'' + (2ar + b) v' + (ar^2 + br + c) v\right] = 0. $$

Since $r = -b/(2a)$, we have $2ar + b = 0$. And since $r$ is a root, $ar^2 + br + c = 0$. The equation reduces to:

由于 $r = -b/(2a)$，有 $2ar + b = 0$。又因 $r$ 是根，$ar^2 + br + c = 0$。方程化为：

$$ a v'' = 0 \;\to\; v'' = 0 \;\to\; v(t) = At + B. $$

**Step 3 — Linearly independent second solution.** Take $B = 0$, $A = 1$: $v(t) = t$. So

**第 3 步 — 线性无关的第二个解。** 取 $B = 0, A = 1$：$v(t) = t$，故

$$ y_2 = t e^{rt}. $$

This is linearly independent from $y_1 = e^{rt}$ (their ratio is $t$, non-constant).

它与 $y_1 = e^{rt}$ 线性无关（比值为 $t$，非常数）。

**Step 4 — General solution.**

**第 4 步 — 通解。**

$$ \boldsymbol{y(t) = (C_1 + C_2 t) e^{rt}.} \qquad \blacksquare $$

**Physical example: critical damping.** For $\gamma = \omega_0$, $r = -\gamma$ (repeated), and $y(t) = (C_1 + C_2 t) e^{-\gamma t}$. This returns to zero the fastest among all non-oscillatory solutions — the design goal of shock absorbers and door closers.

**物理示例：临界阻尼。** 当 $\gamma = \omega_0$ 时，$r = -\gamma$（重根），$y(t) = (C_1 + C_2 t) e^{-\gamma t}$。在所有非振荡解中，这是返回零最快的——这是减震器和门闩器的设计目标。

---

### B.3 — Case 3: Complex Conjugate Roots ($\Delta < 0$) · 情形 3：复共轭根（$\Delta < 0$）

**Step 1 — Complex roots.** When $\Delta < 0$, the roots are $r = \alpha \pm i\beta$ where $\alpha = -b/(2a)$ and $\beta = \sqrt{4ac - b^2}/(2a) > 0$. The complex solutions are $e^{(\alpha+i\beta)t}$ and $e^{(\alpha-i\beta)t}$.

**第 1 步 — 复数根。** 当 $\Delta < 0$ 时，根为 $r = \alpha \pm i\beta$，其中 $\alpha = -b/(2a)$，$\beta = \sqrt{4ac - b^2}/(2a) > 0$。复数解为 $e^{(\alpha+i\beta)t}$ 和 $e^{(\alpha-i\beta)t}$。

**Step 2 — Construct real solutions using Euler's formula.** Since the ODE has real coefficients, the real and imaginary parts of any complex solution are themselves real solutions. Applying Euler's formula:

**第 2 步 — 用欧拉公式构造实数解。** 由于常微分方程系数为实数，任何复数解的实部和虚部各自也是实数解。应用欧拉公式：

$$ e^{(\alpha+i\beta)t} = e^{\alpha t}(\cos \beta t + i \sin \beta t). $$

Real part: $y_1 = e^{\alpha t} \cos \beta t$. Imaginary part: $y_2 = e^{\alpha t} \sin \beta t$.

实部：$y_1 = e^{\alpha t} \cos \beta t$。虚部：$y_2 = e^{\alpha t} \sin \beta t$。

**Step 3 — Linear independence.** $y_1/y_2 = \cos \beta t / \sin \beta t = \cot \beta t$ is non-constant ($\beta \ne 0$), so $y_1$ and $y_2$ are linearly independent.

**第 3 步 — 线性无关性。** $y_1/y_2 = \cos \beta t / \sin \beta t = \cot \beta t$ 非常数（$\beta \ne 0$），故 $y_1$ 和 $y_2$ 线性无关。

**Step 4 — General solution.**

**第 4 步 — 通解。**

$$ \boldsymbol{y(t) = e^{\alpha t}(C_1 \cos \beta t + C_2 \sin \beta t).} $$

Equivalently, $y(t) = R e^{\alpha t} \cos(\beta t - \varphi)$ where $R = \sqrt{C_1^2 + C_2^2}$ and $\tan \varphi = C_2/C_1$. $\blacksquare$

等价地，$y(t) = R e^{\alpha t} \cos(\beta t - \varphi)$，其中 $R = \sqrt{C_1^2 + C_2^2}$，$\tan \varphi = C_2/C_1$。$\blacksquare$

**Physical examples.** (i) Undamped oscillator ($\alpha = 0$, $a = 1$, $b = 0$, $c = \omega^2$): $r = \pm i\omega$, giving $\boldsymbol{y(t) = C_1 \cos \omega t + C_2 \sin \omega t}$ — simple harmonic motion. (ii) Underdamped oscillator ($\alpha = -\gamma < 0$, $\beta = \sqrt{\omega_0^2 - \gamma^2}$): $\boldsymbol{y(t) = e^{-\gamma t}(C_1 \cos \beta t + C_2 \sin \beta t)}$ — decaying oscillations. (iii) The TISE $-(\hbar^2/2m)\psi'' = E\psi$ for a free particle: same equation, solutions $e^{\pm ikx}$ with $k = \sqrt{2mE}/\hbar$.

**物理示例。** (i) 无阻尼振子（$\alpha = 0$, $a = 1$, $b = 0$, $c = \omega^2$）：$r = \pm i\omega$，给出 $\boldsymbol{y(t) = C_1 \cos \omega t + C_2 \sin \omega t}$——简谐运动。(ii) 欠阻尼振子（$\alpha = -\gamma < 0$, $\beta = \sqrt{\omega_0^2 - \gamma^2}$）：$\boldsymbol{y(t) = e^{-\gamma t}(C_1 \cos \beta t + C_2 \sin \beta t)}$——衰减振荡。(iii) 自由粒子的定态薛定谔方程 $-(\hbar^2/2m)\psi'' = E\psi$：同一方程，解为 $e^{\pm ikx}$，$k = \sqrt{2mE}/\hbar$。

---

## C. The Hermite Recursion from Series Substitution · 从级数代入推导厄米递推关系

**Setup.** The **Hermite equation** in the form arising from the quantum harmonic oscillator (after dimensional reduction) is

**准备工作。** 量子谐振子（经过量纲约化后）导出的**厄米方程**为

$$ y'' - 2x y' + 2n y = 0, $$

where $n$ is a non-negative integer (the quantum number). We seek polynomial solutions.

其中 $n$ 为非负整数（量子数）。我们寻求多项式解。

**Step 1 — Substitute a power series.** Let $y = \sum_{k=0}^{\infty} a_k x^k$. Then:

**第 1 步 — 代入幂级数。** 令 $y = \sum_{k=0}^{\infty} a_k x^k$，则：

$$ \begin{aligned} y' &= \sum_{k=1}^{\infty} k a_k x^{k-1} = \sum_{k=0}^{\infty} (k+1) a_{k+1} x^k, \\ y'' &= \sum_{k=2}^{\infty} k(k-1) a_k x^{k-2} = \sum_{k=0}^{\infty} (k+2)(k+1) a_{k+2} x^k. \end{aligned} $$

**Step 2 — Substitute into the equation.** The equation $y'' - 2x y' + 2n y = 0$ becomes:

**第 2 步 — 代入方程。** 方程 $y'' - 2x y' + 2n y = 0$ 变为：

$$ \sum_{k=0}^{\infty} (k+2)(k+1) a_{k+2} x^k - 2x \sum_{k=0}^{\infty} (k+1) a_{k+1} x^k + 2n \sum_{k=0}^{\infty} a_k x^k = 0. $$

Rewrite the middle term: $-2x \cdot \sum (k+1) a_{k+1} x^k = -2 \sum (k+1) a_{k+1} x^{k+1} = -2 \sum_{k=1}^{\infty} k a_k x^k = -2 \sum_{k=0}^{\infty} k a_k x^k$ (the $k=0$ term vanishes).

改写中间项：$-2x \cdot \sum (k+1) a_{k+1} x^k = -2 \sum (k+1) a_{k+1} x^{k+1} = -2 \sum_{k=1}^{\infty} k a_k x^k = -2 \sum_{k=0}^{\infty} k a_k x^k$（$k=0$ 项为零）。

Collecting all terms at order $x^k$:

汇总 $x^k$ 阶项：

$$ \left[(k+2)(k+1) a_{k+2} - 2k a_k + 2n a_k\right] x^k = 0 \quad \text{for all } k \ge 0. $$

**Step 3 — Extract the recursion.** Setting the coefficient of $x^k$ to zero:

**第 3 步 — 提取递推关系。** 令 $x^k$ 的系数为零：

$$ (k+2)(k+1) a_{k+2} = 2(k - n) a_k. $$

Solving for $a_{k+2}$:

解出 $a_{k+2}$：

$$ \boxed{\, a_{k+2} = \frac{2(k - n)}{(k+1)(k+2)}\, a_k. \,} $$

This is the **Hermite recursion relation**. It shows that the coefficients of even and odd powers decouple: $a_0$ and $a_2, a_4, \ldots$ form one chain; $a_1$ and $a_3, a_5, \ldots$ form another. The two free parameters $a_0$ and $a_1$ correspond to the two linearly independent solutions.

这就是**厄米递推关系**。它表明偶次幂和奇次幂的系数相互解耦：$a_0$ 与 $a_2, a_4, \ldots$ 构成一条链；$a_1$ 与 $a_3, a_5, \ldots$ 构成另一条链。两个自由参数 $a_0$ 和 $a_1$ 对应两个线性无关的解。

**Step 4 — Termination argument.** For large $k$, $a_{k+2}/a_k \approx 2/k$, the same ratio as in the series for $e^{x^2} = \sum x^{2m}/m!$. If the series does not terminate, then $y(x) \sim e^{x^2}$ for large $|x|$. In the quantum oscillator context, the full wavefunction is $\psi(x) = y(x) e^{-x^2/2}$; if $y \sim e^{x^2}$, then $\psi \sim e^{x^2/2}$ which is not normalizable (not in $L^2(\mathbb{R})$). We therefore require the series to terminate.

**第 4 步 — 终止论证。** 对大 $k$，$a_{k+2}/a_k \approx 2/k$，与 $e^{x^2} = \sum x^{2m}/m!$ 的级数比值相同。若级数不终止，则对大 $|x|$ 有 $y(x) \sim e^{x^2}$。在量子谐振子中，完整波函数为 $\psi(x) = y(x) e^{-x^2/2}$；若 $y \sim e^{x^2}$，则 $\psi \sim e^{x^2/2}$，不可归一化（不属于 $L^2(\mathbb{R})$）。因此要求级数终止。

**Step 5 — Termination condition.** From the recursion $a_{k+2} = \frac{2(k - n)}{(k+1)(k+2)} a_k$: the numerator $2(k - n)$ vanishes when $k = n$. If $n$ is a non-negative integer and we choose the "chain" (even or odd) that contains the term $k = n$, then $a_{n+2} = 0$ and all subsequent terms vanish. Setting the other chain's starting coefficient to zero ($a_1 = 0$ for even-$n$ polynomial, $a_0 = 0$ for odd-$n$), we obtain a terminating polynomial of degree $n$ — the **$n$-th Hermite polynomial** $H_n(x)$.

**第 5 步 — 终止条件。** 由递推关系 $a_{k+2} = \frac{2(k - n)}{(k+1)(k+2)} a_k$：当 $k = n$ 时，分子 $2(k - n)$ 为零。若 $n$ 是非负整数，且我们选择包含 $k = n$ 项的"链"（偶次或奇次），则 $a_{n+2} = 0$，此后所有项均为零。令另一条链的起始系数为零（$n$ 为偶数时令 $a_1 = 0$，$n$ 为奇数时令 $a_0 = 0$），得到一个 $n$ 次终止多项式——**第 $n$ 阶厄米多项式** $H_n(x)$。

**Step 6 — First few Hermite polynomials.** From the recursion:

**第 6 步 — 前几个厄米多项式。** 由递推关系：

$$ \begin{aligned} n=0:&\quad a_0 = 1, \text{ all odd terms zero} \to H_0(x) = 1. \\ n=1:&\quad a_1 = 1 \;(\text{set } a_0 = 0),\; a_3 = 0 \to H_1(x) = 2x \text{ (with physicist's normalization)}. \\ n=2:&\quad a_0 = 1,\; a_2 = \tfrac{2(0-2)}{1\cdot 2} a_0 = -2,\; a_4 = 0 \to H_2(x) = 4x^2 - 2. \\ n=3:&\quad a_1 = 1,\; a_3 = \tfrac{2(1-3)}{2\cdot 3} a_1 = -\tfrac23 \to H_3(x) = 8x^3 - 12x. \end{aligned} $$

$$ \begin{aligned} n=0:&\quad a_0 = 1\text{，所有奇数项为零} \to H_0(x) = 1\text{。} \\ n=1:&\quad a_1 = 1\;(\text{令 } a_0 = 0),\; a_3 = 0 \to H_1(x) = 2x\text{（物理学家归一化）}\text{。} \\ n=2:&\quad a_0 = 1,\; a_2 = \tfrac{2(0-2)}{1\cdot 2} a_0 = -2,\; a_4 = 0 \to H_2(x) = 4x^2 - 2\text{。} \\ n=3:&\quad a_1 = 1,\; a_3 = \tfrac{2(1-3)}{2\cdot 3} a_1 = -\tfrac23 \to H_3(x) = 8x^3 - 12x\text{。} \end{aligned} $$

The quantum harmonic oscillator wavefunctions are $\psi_n(x) \propto H_n(\sqrt{m\omega/\hbar}\, x)\, e^{-m\omega x^2/2\hbar}$, normalized in $L^2(\mathbb{R})$. $\blacksquare$

量子谐振子波函数为 $\psi_n(x) \propto H_n(\sqrt{m\omega/\hbar}\, x)\, e^{-m\omega x^2/2\hbar}$，在 $L^2(\mathbb{R})$ 中归一化。$\blacksquare$

---

## D. Separation of Variables for the Heat Equation · 热传导方程的分离变量

**Setup.** Consider the heat equation on a rod of length $L$ with Dirichlet boundary conditions (temperature fixed to zero at the ends):

**准备工作。** 考虑长度为 $L$ 的杆上的热传导方程，满足狄利克雷边界条件（两端温度固定为零）：

$$ \frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}, \quad u(0, t) = u(L, t) = 0, \quad u(x, 0) = f(x). $$

**Step 1 — Assume a separated solution.** Let $u(x, t) = X(x) T(t)$ with $X, T$ not identically zero.

**第 1 步 — 假设可分离解。** 令 $u(x, t) = X(x) T(t)$，$X, T$ 不恒为零。

**Step 2 — Substitute into the PDE.**

**第 2 步 — 代入偏微分方程。**

$$ X(x) T'(t) = D X''(x) T(t). $$

Divide both sides by $D X(x) T(t)$ (valid where neither $X$ nor $T$ is zero):

两端除以 $D X(x) T(t)$（在 $X$ 和 $T$ 均不为零处有效）：

$$ \frac{T'(t)}{D T(t)} = \frac{X''(x)}{X(x)}. $$

**Step 3 — Separation constant.** The left side depends only on $t$ and the right side only on $x$. Since they are equal for all $(x, t)$, both sides must equal a common constant, which we call $-\lambda$ (the sign choice anticipates physical solutions):

**第 3 步 — 分离常数。** 左侧只依赖 $t$，右侧只依赖 $x$。由于对所有 $(x, t)$ 均相等，两侧必须等于同一常数，记为 $-\lambda$（负号的选取预示物理解的形式）：

$$ \frac{T'}{DT} = \frac{X''}{X} = -\lambda. $$

This gives two separate ODEs:

由此得到两个独立的常微分方程：

$$ \boldsymbol{T' = -D \lambda T} \;\text{ (in } t\text{)}, \qquad \boldsymbol{X'' = -\lambda X} \;\text{ (in } x\text{)}. $$

**Step 4 — Solve the spatial ODE with boundary conditions.** The equation $X'' = -\lambda X$ with $X(0) = X(L) = 0$.

**第 4 步 — 结合边界条件求解空间常微分方程。** 方程 $X'' = -\lambda X$，边界条件 $X(0) = X(L) = 0$。

Case $\lambda \le 0$: If $\lambda = 0$, then $X'' = 0$, giving $X = Ax + B$; boundary conditions force $A = B = 0$, so $X \equiv 0$ (trivial). If $\lambda < 0$ (set $\lambda = -\mu^2$ with $\mu > 0$), then $X'' = \mu^2 X$, giving $X = Ae^{\mu x} + Be^{-\mu x}$; boundary conditions again force $A = B = 0$. So $\lambda$ must be positive.

$\lambda \le 0$ 的情形：若 $\lambda = 0$，则 $X'' = 0$，给出 $X = Ax + B$；边界条件迫使 $A = B = 0$，故 $X \equiv 0$（平凡解）。若 $\lambda < 0$（令 $\lambda = -\mu^2$，$\mu > 0$），则 $X'' = \mu^2 X$，给出 $X = Ae^{\mu x} + Be^{-\mu x}$；边界条件再次迫使 $A = B = 0$。因此 $\lambda$ 必须为正数。

Case $\lambda > 0$ (set $\lambda = k^2$): $X'' = -k^2 X$ has general solution $X(x) = A \sin(kx) + B \cos(kx)$. From $X(0) = 0$: $B = 0$. From $X(L) = 0$: $A \sin(kL) = 0$. Non-trivial solution requires $\sin(kL) = 0$, i.e., $kL = n\pi$ for $n = 1, 2, 3, \ldots$

$\lambda > 0$ 的情形（令 $\lambda = k^2$）：$X'' = -k^2 X$ 的通解为 $X(x) = A \sin(kx) + B \cos(kx)$。由 $X(0) = 0$：$B = 0$。由 $X(L) = 0$：$A \sin(kL) = 0$。非平凡解要求 $\sin(kL) = 0$，即 $kL = n\pi$，$n = 1, 2, 3, \ldots$

The **eigenvalues** are $\lambda_n = (n\pi/L)^2$ and the **eigenfunctions** are $X_n(x) = \sin(n\pi x/L)$.

**本征值**为 $\lambda_n = (n\pi/L)^2$，**本征函数**为 $X_n(x) = \sin(n\pi x/L)$。

**Step 5 — Solve the temporal ODE.** For each $n$:

**第 5 步 — 求解时间常微分方程。** 对每个 $n$：

$$ T' = -D\lambda_n T \;\to\; T_n(t) = e^{-D\lambda_n t} = e^{-D(n\pi/L)^2 t}. $$

**Step 6 — Superpose the modes.** The general solution satisfying the PDE and boundary conditions is

**第 6 步 — 叠加各模式。** 满足偏微分方程和边界条件的通解为

$$ \boldsymbol{u(x, t) = \sum_{n=1}^{\infty} B_n \sin\!\big(n\pi x/L\big)\, e^{-D(n\pi/L)^2 t}.} $$

**Step 7 — Apply the initial condition.** At $t = 0$:

**第 7 步 — 应用初始条件。** 在 $t = 0$ 处：

$$ u(x, 0) = \sum_{n=1}^{\infty} B_n \sin(n\pi x/L) = f(x). $$

This is a Fourier sine series. Using orthogonality $\int_0^L \sin(m\pi x/L) \sin(n\pi x/L)\,dx = (L/2) \delta_{mn}$:

这是傅里叶正弦级数。利用正交性 $\int_0^L \sin(m\pi x/L) \sin(n\pi x/L)\,dx = (L/2) \delta_{mn}$：

$$ \boxed{\, B_n = \frac{2}{L} \int_0^L f(x) \sin(n\pi x/L)\,dx. \,} \qquad \blacksquare $$

**Physical interpretation.** Each mode decays at rate $D\lambda_n = D(n\pi/L)^2$. High-frequency modes (large $n$) decay rapidly; low-frequency modes persist longest. This is why temperature profiles eventually smooth out — a direct consequence of the Fourier structure of the heat equation.

**物理解释。** 每个模式以速率 $D\lambda_n = D(n\pi/L)^2$ 衰减。高频模式（大 $n$）衰减快；低频模式持续最长。这正是温度分布最终趋于平滑的原因——这是热传导方程傅里叶结构的直接结果。

**Existence and uniqueness.** The series solution converges in $L^2([0,L])$ for any square-integrable initial condition $f(x)$ (by Parseval's theorem). If $f$ is also continuous and piecewise smooth, the series converges pointwise. Uniqueness follows from the energy estimate: if $u_1$ and $u_2$ are two solutions, their difference $w = u_1 - u_2$ satisfies $w_t = D w_{xx}$ with zero boundary and initial conditions; then $\frac{d}{dt} \int_0^L w^2\,dx = -2D \int_0^L (w_x)^2\,dx \le 0$, forcing $\int w^2\,dx \to 0$.

**存在性与唯一性。** 对任意平方可积初始条件 $f(x)$（由帕塞瓦尔定理），级数解在 $L^2([0,L])$ 中收敛。若 $f$ 还连续且分段光滑，则级数逐点收敛。唯一性由能量估计得出：若 $u_1$ 和 $u_2$ 是两个解，其差 $w = u_1 - u_2$ 满足 $w_t = D w_{xx}$，边界和初始条件均为零；则 $\frac{d}{dt} \int_0^L w^2\,dx = -2D \int_0^L (w_x)^2\,dx \le 0$，迫使 $\int w^2\,dx \to 0$。

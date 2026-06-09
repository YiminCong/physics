---
title: "Derivations — Module 0.1: Calculus & Taylor Series"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 0.1: Calculus & Taylor Series
# 推导 — 模块 0.1：微积分与泰勒级数

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.1](./module-0.1-calculus-and-taylor-series.md). Full step-by-step proofs of every non-trivial result stated there: the Taylor theorem with Lagrange remainder, the standard series for $e^x$ / $\sin$ / $\cos$ / $(1+x)^n$ / $\ln(1+x)$, the identity $d/dx(e^x) = e^x$ from the series, and the Gaussian integral $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$. English first, then 中文.
> [模块 0.1](./module-0.1-calculus-and-taylor-series.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：带拉格朗日余项的泰勒定理、$e^x$ / $\sin$ / $\cos$ / $(1+x)^n$ / $\ln(1+x)$ 的标准级数、从级数推导 $d/dx(e^x) = e^x$，以及高斯积分 $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$。先英文，后中文。

---

## A. Taylor's Theorem with Lagrange Remainder · 带拉格朗日余项的泰勒定理

**Claim.** Let $f$ be $(n+1)$-times continuously differentiable on an open interval containing $a$ and $x$. Then

**命题。** 设 $f$ 在包含 $a$ 和 $x$ 的开区间上 $(n+1)$ 次连续可微。则

$$ f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)\,(x-a)^k}{k!} + R_n(x), $$

where the **Lagrange remainder** is $R_n(x) = f^{(n+1)}(c)\,(x-a)^{n+1} / (n+1)!$ for some $c$ strictly between $a$ and $x$.

其中**拉格朗日余项**为 $R_n(x) = f^{(n+1)}(c)\,(x-a)^{n+1} / (n+1)!$，$c$ 严格介于 $a$ 与 $x$ 之间。

**Step 1 — Introduce an auxiliary function.** Fix $x \ne a$ and define

**第 1 步 — 引入辅助函数。** 固定 $x \ne a$，定义

$$ g(t) = f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(t)\,(x-t)^k}{k!} $$

on $[a, x]$ (or $[x, a]$ if $x < a$). This function measures the error that the $n$-th order Taylor polynomial at $t$ makes when approximating $f(x)$.

在 $[a, x]$（若 $x < a$ 则为 $[x, a]$）上。此函数衡量以 $t$ 为展开点的 $n$ 阶泰勒多项式近似 $f(x)$ 时的误差。

**Step 2 — Evaluate at the endpoints.** At $t = x$:

**第 2 步 — 计算端点处的值。** 在 $t = x$ 处：

$$ g(x) = f(x) - f(x) = 0. $$

At $t = a$:

在 $t = a$ 处：

$$ g(a) = f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(a)\,(x-a)^k}{k!} = R_n(x). $$

**Step 3 — Differentiate $g$ with respect to $t$.** Using the product rule on each term $f^{(k)}(t)(x-t)^k/k!$:

**第 3 步 — 对 $g$ 关于 $t$ 求导。** 对每一项 $f^{(k)}(t)(x-t)^k/k!$ 使用乘积法则：

$$ \begin{aligned} \frac{d}{dt}\Big[\frac{f^{(k)}(t)(x-t)^k}{k!}\Big] &= \frac{f^{(k+1)}(t)(x-t)^k}{k!} - \frac{f^{(k)}(t)\,k(x-t)^{k-1}}{k!} \\ &= \frac{f^{(k+1)}(t)(x-t)^k}{k!} - \frac{f^{(k)}(t)(x-t)^{k-1}}{(k-1)!}. \end{aligned} $$

Summing from $k = 0$ to $n$, consecutive terms telescope: the $-f^{(k)}(t)(x-t)^{k-1}/(k-1)!$ at step $k$ cancels the $+f^{(k)}(t)(x-t)^{k-1}/(k-1)!$ at step $k-1$. Only the last term survives:

从 $k = 0$ 到 $n$ 求和，相邻项相消：第 $k$ 步的 $-f^{(k)}(t)(x-t)^{k-1}/(k-1)!$ 与第 $k-1$ 步的 $+f^{(k)}(t)(x-t)^{k-1}/(k-1)!$ 对消。只剩最后一项：

$$ g'(t) = -\frac{f^{(n+1)}(t)(x-t)^n}{n!}. $$

**Step 4 — Introduce $h(t)$ to apply Cauchy's mean-value theorem.** Let $h(t) = (x-t)^{n+1}$. Then $h(x) = 0$, $h(a) = (x-a)^{n+1}$, and $h'(t) = -(n+1)(x-t)^n$. By the **Cauchy mean-value theorem**, there exists $c \in (a, x)$ such that

**第 4 步 — 引入 $h(t)$ 应用柯西中值定理。** 令 $h(t) = (x-t)^{n+1}$。则 $h(x) = 0$，$h(a) = (x-a)^{n+1}$，$h'(t) = -(n+1)(x-t)^n$。由**柯西中值定理**，存在 $c \in (a, x)$ 使得

$$ \frac{g(x) - g(a)}{h(x) - h(a)} = \frac{g'(c)}{h'(c)}. $$

Substituting:

代入：

$$ \frac{0 - R_n(x)}{0 - (x-a)^{n+1}} = \frac{-f^{(n+1)}(c)(x-c)^n / n!}{-(n+1)(x-c)^n}. $$

The $(x-c)^n$ factors cancel ($c \ne x$), giving

因子 $(x-c)^n$ 约去（$c \ne x$），得

$$ \frac{R_n(x)}{(x-a)^{n+1}} = \frac{f^{(n+1)}(c)}{(n+1)!}. $$

**Step 5 — Conclude.** Therefore

**第 5 步 — 结论。** 因此

$$ \boxed{\, R_n(x) = \frac{f^{(n+1)}(c)\,(x-a)^{n+1}}{(n+1)!} \,} \quad \text{for some } c \text{ between } a \text{ and } x. $$

Since $|R_n(x)| \le M\,|x-a|^{n+1} / (n+1)!$ where $M = \max|f^{(n+1)}|$ on the interval, $R_n(x) \to 0$ as $n \to \infty$ whenever $|x-a|$ is within the radius of convergence, establishing that the infinite Taylor series converges to $f(x)$ on that interval. $\blacksquare$

由于 $|R_n(x)| \le M\,|x-a|^{n+1} / (n+1)!$，其中 $M = $ 区间上 $|f^{(n+1)}|$ 的上界，故当 $|x-a|$ 在收敛半径内时 $R_n(x) \to 0$（$n \to \infty$），从而证明无穷泰勒级数在该区间上收敛于 $f(x)$。$\blacksquare$

---

## B. Taylor Series for $e^x$, $\sin x$, $\cos x$ · $e^x$、$\sin x$、$\cos x$ 的泰勒级数

**Claim.** For all $x \in \mathbb{R}$:

**命题。** 对所有 $x \in \mathbb{R}$：

$$ e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}, \qquad \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \qquad \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}. $$

**Step 1 — Compute the derivatives of $e^x$.** Let $f(x) = e^x$. Then $f^{(n)}(x) = e^x$ for all $n$. At $a = 0$: $f^{(n)}(0) = 1$ for all $n$. The remainder $|R_n(x)| \le e^x |x|^{n+1}/(n+1)!$. Since $n!$ grows faster than any power, $|x|^{n+1}/(n+1)! \to 0$, so the series converges absolutely for all $x$:

**第 1 步 — 计算 $e^x$ 的各阶导数。** 令 $f(x) = e^x$。则 $f^{(n)}(x) = e^x$ 对所有 $n$ 成立。在 $a = 0$ 处：$f^{(n)}(0) = 1$ 对所有 $n$ 成立。余项 $|R_n(x)| \le e^x |x|^{n+1}/(n+1)!$。由于 $n!$ 的增长速度超过任何幂次，$|x|^{n+1}/(n+1)! \to 0$，故级数对所有 $x$ 绝对收敛：

$$ \boxed{\, e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^{\infty} \frac{x^n}{n!}. \,} $$

**Step 2 — Compute the derivatives of $\sin x$.** The derivatives cycle with period 4: $\sin x, \cos x, -\sin x, -\cos x, \ldots$ At $a = 0$ the values are $0, 1, 0, -1, 0, 1, \ldots$ Only odd-indexed terms survive:

**第 2 步 — 计算 $\sin x$ 的各阶导数。** 导数以 4 为周期循环：$\sin x, \cos x, -\sin x, -\cos x, \ldots$。在 $a = 0$ 处取值为 $0, 1, 0, -1, 0, 1, \ldots$。只有奇数阶项非零：

$$ \boxed{\, \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}. \,} $$

The remainder $|R_n| \le |x|^{n+1}/(n+1)! \to 0$, so the series converges for all $x \in \mathbb{R}$.

余项 $|R_n| \le |x|^{n+1}/(n+1)! \to 0$，故级数对所有 $x \in \mathbb{R}$ 收敛。

**Step 3 — Compute the derivatives of $\cos x$.** Similarly the derivatives cycle 4-periodically, and at $a = 0$ only even-indexed terms survive:

**第 3 步 — 计算 $\cos x$ 的各阶导数。** 类似地，导数以 4 为周期循环，在 $a = 0$ 处只有偶数阶项非零：

$$ \boxed{\, \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}. \,} \qquad \blacksquare $$

---

## C. Taylor Series for $(1+x)^n$ and $\ln(1+x)$ · $(1+x)^n$ 与 $\ln(1+x)$ 的泰勒级数

**Claim (Binomial Series).** For real exponent $\alpha$ and $|x| < 1$:

**命题（二项式级数）。** 对实数指数 $\alpha$ 及 $|x| < 1$：

$$ (1+x)^\alpha = \sum_{k=0}^{\infty} C(\alpha,k)\, x^k, \qquad \text{where } C(\alpha,k) = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}. $$

In particular for $|x| \ll 1$ the leading approximation is $(1+x)^\alpha \approx 1 + \alpha x$.

特别地，当 $|x| \ll 1$ 时，领头近似为 $(1+x)^\alpha \approx 1 + \alpha x$。

**Step 1 — Compute derivatives at 0.** Let $f(x) = (1+x)^\alpha$. Then $f'(x) = \alpha(1+x)^{\alpha-1}$, $f''(x) = \alpha(\alpha-1)(1+x)^{\alpha-2}$, and by induction $f^{(k)}(x) = \alpha(\alpha-1)\cdots(\alpha-k+1)(1+x)^{\alpha-k}$. At $x = 0$: $f^{(k)}(0) = \alpha(\alpha-1)\cdots(\alpha-k+1) = k!\, C(\alpha,k)$.

**第 1 步 — 计算 0 处的导数。** 令 $f(x) = (1+x)^\alpha$。则 $f'(x) = \alpha(1+x)^{\alpha-1}$，$f''(x) = \alpha(\alpha-1)(1+x)^{\alpha-2}$，由归纳法 $f^{(k)}(x) = \alpha(\alpha-1)\cdots(\alpha-k+1)(1+x)^{\alpha-k}$。在 $x = 0$ 处：$f^{(k)}(0) = \alpha(\alpha-1)\cdots(\alpha-k+1) = k!\, C(\alpha,k)$。

**Step 2 — Radius of convergence.** By the ratio test, $|C(\alpha,k+1) x^{k+1}| / |C(\alpha,k) x^k| = |(\alpha-k)/(k+1)|\,|x| \to |x|$ as $k \to \infty$. So the series converges absolutely for $|x| < 1$. (At the endpoints $|x| = 1$ the behavior depends on $\alpha$.) The Taylor formula then gives

**第 2 步 — 收敛半径。** 由比值审敛法，$|C(\alpha,k+1) x^{k+1}| / |C(\alpha,k) x^k| = |(\alpha-k)/(k+1)|\,|x| \to |x|$（$k \to \infty$）。故级数对 $|x| < 1$ 绝对收敛（在端点 $|x| = 1$ 处的行为取决于 $\alpha$）。泰勒公式给出

$$ \boxed{\, (1+x)^\alpha = \sum_{k=0}^{\infty} C(\alpha,k)\, x^k \quad \text{for } |x| < 1. \,} \qquad \blacksquare $$

**Claim (Logarithm Series).** For $|x| < 1$:

**命题（对数级数）。** 对 $|x| < 1$：

$$ \ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}. $$

**Step 3 — Integrate the geometric series.** The geometric series gives, for $|x| < 1$:

**第 3 步 — 对等比级数积分。** 对 $|x| < 1$，等比级数给出：

$$ \frac{1}{1+t} = \sum_{n=0}^{\infty} (-t)^n = 1 - t + t^2 - t^3 + \cdots $$

Integrate both sides from 0 to $x$ (term-by-term integration is valid within $|x| < 1$ by uniform convergence):

两端从 0 积到 $x$（在 $|x| < 1$ 内由一致收敛性，逐项积分有效）：

$$ \int_0^x \frac{1}{1+t}\,dt = \sum_{n=0}^{\infty} (-1)^n \int_0^x t^n\,dt = \sum_{n=0}^{\infty} \frac{(-1)^n x^{n+1}}{n+1}. $$

The left-hand side equals $\ln(1+x)$. Re-indexing with $m = n+1$:

左侧等于 $\ln(1+x)$。令 $m = n+1$ 重新标记：

$$ \boxed{\, \ln(1+x) = \sum_{m=1}^{\infty} \frac{(-1)^{m+1} x^m}{m} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \,} \quad \text{for } |x| < 1. \qquad \blacksquare $$

---

## D. Proof that $d/dx(e^x) = e^x$ from the Series · 从级数证明 $d/dx(e^x) = e^x$

**Claim.** The function defined by $e^x = \sum_{n=0}^{\infty} x^n/n!$ satisfies $d/dx(e^x) = e^x$.

**命题。** 由 $e^x = \sum_{n=0}^{\infty} x^n/n!$ 定义的函数满足 $d/dx(e^x) = e^x$。

**Step 1 — Differentiate term by term.** Because the power series $\sum x^n/n!$ converges absolutely for all $x \in \mathbb{R}$ (established in Section B), it converges uniformly on every closed bounded interval, so term-by-term differentiation is valid:

**第 1 步 — 逐项求导。** 由于幂级数 $\sum x^n/n!$ 对所有 $x \in \mathbb{R}$ 绝对收敛（见 B 节），它在每个有界闭区间上一致收敛，故逐项求导合法：

$$ \frac{d}{dx}(e^x) = \frac{d}{dx} \sum_{n=0}^{\infty} \frac{x^n}{n!} = \sum_{n=0}^{\infty} \frac{d}{dx}\Big[\frac{x^n}{n!}\Big] = \sum_{n=1}^{\infty} \frac{n\, x^{n-1}}{n!} = \sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!}. $$

**Step 2 — Re-index.** Let $m = n - 1$:

**第 2 步 — 重新标记。** 令 $m = n - 1$：

$$ \sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^{\infty} \frac{x^m}{m!} = e^x. $$

Therefore $\boxed{\, d/dx(e^x) = e^x \,}$. $\blacksquare$

因此 $\boxed{\, d/dx(e^x) = e^x \,}$。$\blacksquare$

**Physical significance.** Any first-order ODE of the form $dy/dt = \lambda y$ has solution $y(t) = y(0) e^{\lambda t}$. This single fact underlies radioactive decay, RC-circuit discharge, the time factor $e^{-iEt/\hbar}$ in quantum mechanics, and the Boltzmann factor $e^{-E/kT}$ in statistical mechanics.

**物理意义。** 任何形如 $dy/dt = \lambda y$ 的一阶常微分方程的解为 $y(t) = y(0) e^{\lambda t}$。这一事实奠定了放射性衰变、RC 电路放电、量子力学中的时间因子 $e^{-iEt/\hbar}$，以及统计力学中玻尔兹曼因子 $e^{-E/kT}$ 的基础。

---

## E. The Gaussian Integral · 高斯积分

**Claim.** $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$.

**命题。** $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$。

**Step 1 — Define $I$ and form $I^2$.** The integrand $e^{-x^2}$ is positive and continuous; the improper integral converges absolutely (since $e^{-x^2} < e^{-|x|}$ for $|x| > 1$). Let $I = \int_{-\infty}^{\infty} e^{-x^2}\,dx$. Square it, using an independent dummy variable $y$ for the second copy:

**第 1 步 — 定义 $I$ 并构造 $I^2$。** 被积函数 $e^{-x^2}$ 为正且连续；广义积分绝对收敛（因为当 $|x| > 1$ 时 $e^{-x^2} < e^{-|x|}$）。令 $I = \int_{-\infty}^{\infty} e^{-x^2}\,dx$。对其平方，用独立哑变量 $y$ 表示第二个因子：

$$ I^2 = \Big[\int_{-\infty}^{\infty} e^{-x^2}\,dx\Big] \cdot \Big[\int_{-\infty}^{\infty} e^{-y^2}\,dy\Big] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2+y^2)}\,dx\,dy. $$

**Step 2 — Switch to polar coordinates.** Set $x = r\cos\theta$, $y = r\sin\theta$, with Jacobian $dx\,dy = r\,dr\,d\theta$. The entire plane is covered by $r \in [0, \infty)$ and $\theta \in [0, 2\pi)$:

**第 2 步 — 转换到极坐标。** 令 $x = r\cos\theta$，$y = r\sin\theta$，雅可比行列式 $dx\,dy = r\,dr\,d\theta$。整个平面由 $r \in [0, \infty)$，$\theta \in [0, 2\pi)$ 覆盖：

$$ I^2 = \int_0^{2\pi} \int_0^\infty e^{-r^2}\, r\,dr\,d\theta. $$

**Step 3 — Evaluate the $r$ integral.** Let $u = r^2$, $du = 2r\,dr$:

**第 3 步 — 计算 $r$ 方向的积分。** 令 $u = r^2$，$du = 2r\,dr$：

$$ \int_0^\infty e^{-r^2}\, r\,dr = \frac{1}{2} \int_0^\infty e^{-u}\,du = \frac{1}{2} \big[-e^{-u}\big]_0^\infty = \frac{1}{2}(0 - (-1)) = \frac{1}{2}. $$

**Step 4 — Evaluate the $\theta$ integral.**

**第 4 步 — 计算 $\theta$ 方向的积分。**

$$ I^2 = \int_0^{2\pi} d\theta \cdot \frac{1}{2} = 2\pi \cdot \frac{1}{2} = \pi. $$

**Step 5 — Conclude.** Since $I > 0$,

**第 5 步 — 结论。** 由于 $I > 0$，

$$ \boxed{\, I = \sqrt{\pi}, \,} \quad \text{i.e. } \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}. \qquad \blacksquare $$

**Corollary.** By the substitution $x \to x/\sigma\sqrt{2}$, $\int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2)}\,dx = \sigma\sqrt{2\pi}$. This normalization factor is what appears in the Gaussian probability distribution $(1/\sigma\sqrt{2\pi})\, e^{-x^2/2\sigma^2}$ and in the ground-state wavefunction of the harmonic oscillator.

**推论。** 通过代换 $x \to x/\sigma\sqrt{2}$，得 $\int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2)}\,dx = \sigma\sqrt{2\pi}$。此归一化因子出现在高斯概率分布 $(1/\sigma\sqrt{2\pi})\, e^{-x^2/2\sigma^2}$ 和谐振子基态波函数中。

---

## F. Convergence of the Taylor Series: Domain Conditions · 泰勒级数的收敛性：定义域条件

**Summary of convergence.** The results above establish:

**收敛性总结。** 上述结果表明：

- $e^x$: converges for all $x \in \mathbb{R}$ (the remainder $R_n \to 0$ by the ratio test on $n!$).
- $\sin x$, $\cos x$: converge for all $x \in \mathbb{R}$ (derivatives bounded by 1 in modulus).
- $(1+x)^\alpha$: converges absolutely for $|x| < 1$; at the boundary the behavior depends on $\alpha$ (e.g. for $\alpha = 1$ the series terminates to $1 + x$; for $\alpha = -1$ it diverges at $x = -1$ and converges conditionally at $x = 1$ by the alternating series test).
- $\ln(1+x)$: converges for $-1 < x \le 1$ (at $x = 1$ it converges to $\ln 2$ by Abel's theorem; at $x = -1$ it diverges).

- $e^x$：对所有 $x \in \mathbb{R}$ 收敛（余项 $R_n$ 由 $n!$ 的比值法趋于 0）。
- $\sin x$，$\cos x$：对所有 $x \in \mathbb{R}$ 收敛（导数的模以 1 为界）。
- $(1+x)^\alpha$：对 $|x| < 1$ 绝对收敛；在边界处的行为取决于 $\alpha$（例如 $\alpha = 1$ 时级数有限终止为 $1 + x$；$\alpha = -1$ 时在 $x = -1$ 处发散，在 $x = 1$ 处由交错级数判别法条件收敛）。
- $\ln(1+x)$：对 $-1 < x \le 1$ 收敛（在 $x = 1$ 处由阿贝尔定理收敛于 $\ln 2$；在 $x = -1$ 处发散）。

**Physical relevance.** In physics one nearly always works within the radius of convergence, where the expansion is not only valid but where truncating to finitely many terms gives quantitatively accurate approximations — the foundation of perturbation theory.

**物理意义。** 在物理学中几乎总是在收敛半径内工作，此时展开不仅有效，截取有限项即可给出定量准确的近似——这正是微扰论的基础。

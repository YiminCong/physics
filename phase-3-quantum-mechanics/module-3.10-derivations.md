---
title: "Derivations — Module 3.10: Quantum Dynamics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.10: Quantum Dynamics
# 推导 — 模块 3.10：量子动力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.10](./module-3.10-quantum-dynamics.md). Full step-by-step proofs of the time-evolution operator, its unitarity, the Heisenberg equation of motion, the harmonic-oscillator solution $a(t) = a(0)e^{-i\omega t}$, the free-particle propagator, and the path-integral sketch. English first, then 中文.
> [模块 3.10](./module-3.10-quantum-dynamics.md) 的配套文档：时间演化算符、其幺正性、海森堡运动方程、谐振子解 $a(t) = a(0)e^{-i\omega t}$、自由粒子传播子与路径积分概述的完整逐步证明。先英文，后中文。

---

## A. The Time-Evolution Operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ · 时间演化算符

**Claim.** For a time-independent Hamiltonian $\hat{H}$, the unique unitary operator satisfying the Schrödinger equation $i\hbar\, d/dt|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$ with initial condition $|\psi(0)\rangle$ given is $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$. Moreover $\hat{U}(t)$ is unitary: $\hat{U}^\dagger(t)\hat{U}(t) = \hat{1}$.

**命题。** 对于与时间无关的哈密顿量 $\hat{H}$，满足薛定谔方程 $i\hbar\, d/dt|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$ 及初始条件 $|\psi(0)\rangle$ 的唯一幺正算符为 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$。而且 $\hat{U}(t)$ 是幺正的：$\hat{U}^\dagger(t)\hat{U}(t) = \hat{1}$。

**Step 1 — Derivation as operator exponential.** Define $\hat{U}(t)$ by its formal power series (valid via the spectral theorem for self-adjoint $\hat{H}$):

**第 1 步 — 作为算符指数的推导。** 通过形式幂级数定义 $\hat{U}(t)$（由自伴 $\hat{H}$ 的谱定理保证有效）：

$$ \hat{U}(t) = e^{-i\hat{H}t/\hbar} = \sum_{n=0}^{\infty} \frac{1}{n!} \Big(\frac{-i\hat{H}t}{\hbar}\Big)^n = \hat{1} - \frac{it}{\hbar}\hat{H} + \frac{1}{2!}\Big(\frac{-it}{\hbar}\Big)^2\hat{H}^2 + \dots $$

**Step 2 — Verify it solves the Schrödinger equation.** Differentiate the power series term by term (justified because $\hat{H}$ is bounded on each energy eigenspace, and the series converges):

**第 2 步 — 验证它满足薛定谔方程。** 逐项对幂级数求导（由于 $\hat{H}$ 在每个能量本征空间上有界，级数收敛，此操作合理）：

$$ \begin{aligned} \frac{d}{dt} \hat{U}(t) &= \sum_{n=1}^{\infty} \frac{1}{n!} \Big(\frac{-i}{\hbar}\Big)^n n\, t^{n-1}\, \hat{H}^n \\ &= \frac{-i\hat{H}}{\hbar} \sum_{n=1}^{\infty} \frac{1}{(n-1)!} \Big(\frac{-i\hat{H}t}{\hbar}\Big)^{n-1} \\ &= \frac{-i\hat{H}}{\hbar} e^{-i\hat{H}t/\hbar} = \frac{-i\hat{H}}{\hbar} \hat{U}(t). \end{aligned} $$

Multiplying by $i\hbar$: $i\hbar\, d/dt\, \hat{U}(t) = \hat{H}\, \hat{U}(t)$. Acting on the initial state $|\psi(0)\rangle$ and using $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$:

两边乘以 $i\hbar$：$i\hbar\, d/dt\, \hat{U}(t) = \hat{H}\, \hat{U}(t)$。作用于初态 $|\psi(0)\rangle$，利用 $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$：

$$ i\hbar \frac{d}{dt} |\psi(t)\rangle = \hat{H}\, \hat{U}(t)|\psi(0)\rangle = \hat{H}|\psi(t)\rangle. \quad \checkmark $$

**Step 3 — Initial condition.** $\hat{U}(0) = e^{0} = \hat{1}$, so $|\psi(0)\rangle = \hat{U}(0)|\psi(0)\rangle = |\psi(0)\rangle$. $\checkmark$

**第 3 步 — 初始条件。** $\hat{U}(0) = e^{0} = \hat{1}$，故 $|\psi(0)\rangle = \hat{U}(0)|\psi(0)\rangle = |\psi(0)\rangle$。$\checkmark$

**Step 4 — Uniqueness.** Suppose $\hat{U}_1$ and $\hat{U}_2$ both satisfy $d/dt\, \hat{U} = (-i\hat{H}/\hbar)\hat{U}$ with $\hat{U}(0) = \hat{1}$. Then for $W = \hat{U}_1 - \hat{U}_2$, $d/dt\, W = (-i\hat{H}/\hbar)W$ and $W(0) = 0$. The norm satisfies $d/dt\, \|W|\psi_0\rangle\|^2 = 2\,\operatorname{Re}\langle W\psi_0|\tfrac{d}{dt}W\psi_0\rangle = 2\operatorname{Re}\langle W\psi_0|(-i\hat{H}/\hbar)W\psi_0\rangle = 0$ (since $\hat{H}$ is Hermitian, the expectation of $-i\hat{H}/\hbar$ is purely imaginary). Starting from zero, the norm remains zero, so $\hat{U}_1 = \hat{U}_2$.

**第 4 步 — 唯一性。** 设 $\hat{U}_1$ 和 $\hat{U}_2$ 都满足 $d/dt\, \hat{U} = (-i\hat{H}/\hbar)\hat{U}$，$\hat{U}(0) = \hat{1}$。令 $W = \hat{U}_1 - \hat{U}_2$，则 $d/dt\, W = (-i\hat{H}/\hbar)W$，$W(0) = 0$。范数满足 $d/dt\, \|W|\psi_0\rangle\|^2 = 2\operatorname{Re}\langle W\psi_0|(-i\hat{H}/\hbar)W\psi_0\rangle = 0$（因 $\hat{H}$ 为厄米算符，$-i\hat{H}/\hbar$ 的期望值为纯虚数）。从零出发范数保持为零，故 $\hat{U}_1 = \hat{U}_2$。

**Step 5 — Unitarity.** Since $\hat{H}$ is self-adjoint ($\hat{H}^\dagger = \hat{H}$):

**第 5 步 — 幺正性。** 由于 $\hat{H}$ 是自伴的（$\hat{H}^\dagger = \hat{H}$）：

$$ \hat{U}^\dagger(t) = (e^{-i\hat{H}t/\hbar})^\dagger = e^{(-i\hat{H}t/\hbar)^\dagger} = e^{i\hat{H}^\dagger t/\hbar} = e^{i\hat{H}t/\hbar}. $$

(The dagger reverses operator order and takes complex conjugate; the series is absolutely convergent so the dagger passes through.) Therefore:

（取伴随后逆转算符顺序并取复共轭；级数绝对收敛故伴随可穿过。）因此：

$$ \hat{U}^\dagger(t)\, \hat{U}(t) = e^{i\hat{H}t/\hbar} e^{-i\hat{H}t/\hbar} = e^{0} = \hat{1}, $$

and similarly $\hat{U}(t)\hat{U}^\dagger(t) = \hat{1}$. (The two exponentials commute because they are functions of the same operator $\hat{H}$.) Hence $\hat{U}$ is **unitary**. $\blacksquare$

类似地 $\hat{U}(t)\hat{U}^\dagger(t) = \hat{1}$。（两个指数可交换，因为它们是同一算符 $\hat{H}$ 的函数。）故 $\hat{U}$ 是**幺正**的。$\blacksquare$

**Physical meaning.** Unitarity ensures $\langle\psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{U}|\psi(0)\rangle = \langle\psi(0)|\psi(0)\rangle = 1$: total probability is conserved.

**物理含义。** 幺正性确保 $\langle\psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{U}|\psi(0)\rangle = \langle\psi(0)|\psi(0)\rangle = 1$：总概率守恒。

---

## B. The Heisenberg Equation of Motion · 海森堡运动方程

**Claim.** In the Heisenberg picture, where operators carry the time dependence and states are fixed, a Heisenberg-picture operator $\hat{A}_H(t) = \hat{U}^\dagger(t)\, \hat{A}_S\, \hat{U}(t)$ satisfies the equation of motion:

**命题。** 在海森堡绘景中，算符携带时间依赖性而态保持固定，海森堡绘景算符 $\hat{A}_H(t) = \hat{U}^\dagger(t)\, \hat{A}_S\, \hat{U}(t)$ 满足运动方程：

$$ \frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \Big(\frac{\partial\hat{A}_S}{\partial t}\Big)_H. $$

For operators with no explicit time dependence ($\partial\hat{A}_S/\partial t = 0$):

对于没有显式时间依赖性的算符（$\partial\hat{A}_S/\partial t = 0$）：

$$ \frac{d\hat{A}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H]. $$

**Step 1 — Differentiate the definition.** Using $d/dt\, \hat{U} = (-i\hat{H}/\hbar)\hat{U}$ and $d/dt\, \hat{U}^\dagger = (i\hat{H}/\hbar)\hat{U}^\dagger$ (from Step 2 above, taking the adjoint):

**第 1 步 — 对定义求导。** 利用 $d/dt\, \hat{U} = (-i\hat{H}/\hbar)\hat{U}$ 以及 $d/dt\, \hat{U}^\dagger = (i\hat{H}/\hbar)\hat{U}^\dagger$（由上文第 2 步取伴随得到）：

$$ \begin{aligned} \frac{d\hat{A}_H}{dt} &= \Big(\frac{d}{dt}\hat{U}^\dagger\Big) \hat{A}_S \hat{U} + \hat{U}^\dagger \hat{A}_S \Big(\frac{d}{dt}\hat{U}\Big) + \hat{U}^\dagger\Big(\frac{\partial\hat{A}_S}{\partial t}\Big)\hat{U} \\ &= \frac{i\hat{H}}{\hbar}\hat{U}^\dagger \hat{A}_S \hat{U} + \hat{U}^\dagger \hat{A}_S \frac{-i\hat{H}}{\hbar}\hat{U} + \hat{U}^\dagger\Big(\frac{\partial\hat{A}_S}{\partial t}\Big)\hat{U}. \end{aligned} $$

Note $\hat{H} = \hat{U}^\dagger\hat{H}\hat{U}$ (since $\hat{H}$ commutes with its own exponential, $\hat{H}$ is the same in both pictures when the Hamiltonian does not depend explicitly on time):

注意 $\hat{H} = \hat{U}^\dagger\hat{H}\hat{U}$（因为 $\hat{H}$ 与其自身的指数对易，当哈密顿量不显含时间时 $\hat{H}$ 在两种绘景中相同）：

$$ \begin{aligned} \frac{d\hat{A}_H}{dt} &= \frac{i}{\hbar} \hat{H} \hat{A}_H - \frac{i}{\hbar} \hat{A}_H \hat{H} + \Big(\frac{\partial\hat{A}_S}{\partial t}\Big)_H \\ &= \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \Big(\frac{\partial\hat{A}_S}{\partial t}\Big)_H. \qquad \blacksquare \end{aligned} $$

This is the operator analogue of Hamilton's equations in classical mechanics (Poisson brackets $\{A, H\}$ correspond to commutators $(i/\hbar)[\hat{H}, \hat{A}]$).

这是经典力学中哈密顿方程的算符类比（泊松括号 $\{A, H\}$ 对应对易子 $(i/\hbar)[\hat{H}, \hat{A}]$）。$\blacksquare$

---

## C. Harmonic Oscillator in the Heisenberg Picture · 海森堡绘景中的谐振子

**Claim.** For the quantum harmonic oscillator $\hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \tfrac12)$, the Heisenberg-picture lowering operator satisfies $\hat{a}(t) = \hat{a}(0)\, e^{-i\omega t}$.

**命题。** 对量子谐振子 $\hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \tfrac12)$，海森堡绘景中的降算符满足 $\hat{a}(t) = \hat{a}(0)\, e^{-i\omega t}$。

**Step 1 — Compute the commutator $[\hat{H}, \hat{a}]$.** Using $\hat{H} = \hbar\omega(\hat{N} + \tfrac12)$ with $\hat{N} = \hat{a}^\dagger\hat{a}$, and the result $[\hat{N}, \hat{a}] = -\hat{a}$ from Module 3.2:

**第 1 步 — 计算对易子 $[\hat{H}, \hat{a}]$。** 利用 $\hat{H} = \hbar\omega(\hat{N} + \tfrac12)$，$\hat{N} = \hat{a}^\dagger\hat{a}$，以及模块 3.2 中的结果 $[\hat{N}, \hat{a}] = -\hat{a}$：

$$ [\hat{H}, \hat{a}] = \hbar\omega[\hat{N} + \tfrac12, \hat{a}] = \hbar\omega([\hat{N}, \hat{a}] + [\tfrac12, \hat{a}]) = \hbar\omega(-\hat{a} + 0) = -\hbar\omega\, \hat{a}. $$

**Step 2 — Write the Heisenberg equation.** With $\partial\hat{a}/\partial t = 0$ (no explicit time dependence in the Schrödinger picture):

**第 2 步 — 写出海森堡方程。** 由于 $\partial\hat{a}/\partial t = 0$（薛定谔绘景中无显式时间依赖性）：

$$ \frac{d\hat{a}(t)}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{a}(t)] = \frac{i}{\hbar}(-\hbar\omega)\, \hat{a}(t) = -i\omega\, \hat{a}(t). $$

**Step 3 — Solve the ODE.** This is a simple first-order linear ODE $d\hat{a}/dt = -i\omega\, \hat{a}$ with solution:

**第 3 步 — 求解常微分方程。** 这是简单的一阶线性常微分方程 $d\hat{a}/dt = -i\omega\, \hat{a}$，其解为：

$$ \hat{a}(t) = \hat{a}(0)\, e^{-i\omega t}. $$

Similarly, taking the adjoint: $\hat{a}^\dagger(t) = \hat{a}^\dagger(0)\, e^{+i\omega t}$.

类似地，取伴随得：$\hat{a}^\dagger(t) = \hat{a}^\dagger(0)\, e^{+i\omega t}$。

**Step 4 — Position and momentum in the Heisenberg picture.** Recalling $\hat{x} = \sqrt{\hbar/2m\omega}(\hat{a} + \hat{a}^\dagger)$ and $\hat{p} = i\sqrt{m\hbar\omega/2}(\hat{a}^\dagger - \hat{a})$:

**第 4 步 — 海森堡绘景中的位置和动量。** 回顾 $\hat{x} = \sqrt{\hbar/2m\omega}(\hat{a} + \hat{a}^\dagger)$，$\hat{p} = i\sqrt{m\hbar\omega/2}(\hat{a}^\dagger - \hat{a})$：

$$ \begin{aligned} \hat{x}(t) &= \sqrt{\frac{\hbar}{2m\omega}}\, (\hat{a}(0)e^{-i\omega t} + \hat{a}^\dagger(0)e^{i\omega t}) \\ &= \hat{x}(0) \cos(\omega t) + \frac{\hat{p}(0)}{m\omega} \sin(\omega t). \end{aligned} $$

$$ \begin{aligned} \hat{p}(t) &= i\sqrt{\frac{m\hbar\omega}{2}}\, (\hat{a}^\dagger(0)e^{i\omega t} - \hat{a}(0)e^{-i\omega t}) \\ &= \hat{p}(0) \cos(\omega t) - m\omega\, \hat{x}(0) \sin(\omega t). \end{aligned} $$

These are exactly the classical equations of motion for a harmonic oscillator, with operator coefficients — the quantum Ehrenfest theorem is manifest. $\blacksquare$

这正是谐振子的经典运动方程，只是系数为算符——量子埃伦费斯特定理在此清晰呈现。$\blacksquare$

---

## D. The Free-Particle Propagator · 自由粒子传播子

**Claim.** For a free particle ($V = 0$) with Hamiltonian $\hat{H} = \hat{p}^2/2m$, the propagator (position-space matrix element of the time-evolution operator) is:

**命题。** 对自由粒子（$V = 0$），哈密顿量 $\hat{H} = \hat{p}^2/2m$，传播子（时间演化算符的坐标空间矩阵元）为：

$$ K(x', t; x, 0) = \langle x'|\hat{U}(t)|x\rangle = \sqrt{\frac{m}{2\pi i\hbar t}}\, \exp\!\Big[\frac{im(x'-x)^2}{2\hbar t}\Big]. $$

**Step 1 — Insert momentum resolution of identity.** Between $\langle x'|$ and $\hat{U}(t)|x\rangle$, insert $\int|p\rangle\langle p|\, dp = \hat{1}$:

**第 1 步 — 插入动量单位分解。** 在 $\langle x'|$ 与 $\hat{U}(t)|x\rangle$ 之间插入 $\int|p\rangle\langle p|\, dp = \hat{1}$：

$$ K(x', t; x, 0) = \int \langle x'|\hat{U}(t)|p\rangle\langle p|x\rangle\, dp. $$

Since $|p\rangle$ is an eigenstate of $\hat{H} = \hat{p}^2/2m$ with eigenvalue $p^2/2m$, $\hat{U}(t)|p\rangle = e^{-ip^2 t/2m\hbar}|p\rangle$:

由于 $|p\rangle$ 是 $\hat{H} = \hat{p}^2/2m$ 的本征态，本征值为 $p^2/2m$，故 $\hat{U}(t)|p\rangle = e^{-ip^2 t/2m\hbar}|p\rangle$：

$$ \begin{aligned} K &= \int \langle x'|p\rangle\, e^{-ip^2 t/2m\hbar}\, \langle p|x\rangle\, dp \\ &= \int \frac{e^{ipx'/\hbar}}{\sqrt{2\pi\hbar}}\, e^{-ip^2 t/2m\hbar}\, \frac{e^{-ipx/\hbar}}{\sqrt{2\pi\hbar}}\, dp \\ &= \frac{1}{2\pi\hbar} \int_{-\infty}^{\infty} e^{ip(x'-x)/\hbar - ip^2 t/2m\hbar}\, dp. \end{aligned} $$

**Step 2 — Complete the square.** Let $\Delta x = x' - x$. Rewrite the exponent:

**第 2 步 — 配方。** 令 $\Delta x = x' - x$。重写指数：

$$ \begin{aligned} \frac{ip\,\Delta x}{\hbar} - \frac{ip^2 t}{2m\hbar} &= -\frac{it}{2m\hbar}\Big[p^2 - \frac{2mp\,\Delta x}{t}\Big] \\ &= -\frac{it}{2m\hbar}\Big[p - \frac{m\,\Delta x}{t}\Big]^2 + \frac{it}{2m\hbar} \cdot \frac{m^2\,\Delta x^2}{t^2} \\ &= -\frac{it}{2m\hbar}\Big(p - \frac{m\,\Delta x}{t}\Big)^2 + \frac{im\,\Delta x^2}{2\hbar t}. \end{aligned} $$

**Step 3 — Gaussian integral.** Substituting $u = p - m\,\Delta x/t$:

**第 3 步 — 高斯积分。** 令 $u = p - m\,\Delta x/t$：

$$ K = \frac{1}{2\pi\hbar} e^{im\,\Delta x^2/2\hbar t} \int_{-\infty}^{\infty} e^{-(it/2m\hbar)u^2}\, du. $$

The integral $\int_{-\infty}^{\infty} e^{-\alpha u^2}\, du = \sqrt{\pi/\alpha}$ for $\operatorname{Re}(\alpha) > 0$. Here $\alpha = it/(2m\hbar)$ has $\operatorname{Re}(\alpha) = 0$, but the integral is defined by analytic continuation (or equivalently by adding a small positive real part to $t$, i.e., $t \to t - i\varepsilon$, and then taking $\varepsilon \to 0^+$). The result is:

积分 $\int_{-\infty}^{\infty} e^{-\alpha u^2}\, du = \sqrt{\pi/\alpha}$ 对 $\operatorname{Re}(\alpha) > 0$ 成立。这里 $\alpha = it/(2m\hbar)$ 的实部为 0，但积分通过解析延拓定义（等价地，令 $t \to t - i\varepsilon$ 再取 $\varepsilon \to 0^+$）。结果为：

$$ \int_{-\infty}^{\infty} e^{-(it/2m\hbar)u^2}\, du = \sqrt{\frac{\pi}{it/2m\hbar}} = \sqrt{\frac{2\pi m\hbar}{it}} = \sqrt{2\pi m\hbar} \cdot \frac{e^{-i\pi/4}}{\sqrt{t}}, $$

where we used $1/\sqrt{i} = e^{-i\pi/4} = (1-i)/\sqrt2$. More directly, $\sqrt{1/i} = \sqrt{-i} = e^{-i\pi/4}$, so:

其中使用了 $1/\sqrt{i} = e^{-i\pi/4} = (1-i)/\sqrt2$。更直接地，$\sqrt{1/i} = e^{-i\pi/4}$，故：

$$ \int_{-\infty}^{\infty} e^{-(it/2m\hbar)u^2}\, du = \sqrt{\frac{2\pi m\hbar}{it}}. $$

**Step 4 — Assemble the result.**

**第 4 步 — 整合结果。**

$$ \begin{aligned} K &= \frac{1}{2\pi\hbar} \cdot e^{im(x'-x)^2/2\hbar t} \cdot \sqrt{\frac{2\pi m\hbar}{it}} \\ &= \frac{1}{2\pi\hbar} \cdot \sqrt{\frac{2\pi m\hbar}{it}} \cdot e^{im(x'-x)^2/2\hbar t} \\ &= \sqrt{\frac{m}{2\pi i\hbar t}} \cdot e^{im(x'-x)^2/(2\hbar t)}. \end{aligned} $$

Here $\sqrt{1/(it)} = e^{-i\pi/4}/\sqrt{t}$, giving the factor $\sqrt{m/(2\pi i\hbar t)}$. $\blacksquare$

其中 $\sqrt{1/(it)} = e^{-i\pi/4}/\sqrt{t}$，给出因子 $\sqrt{m/(2\pi i\hbar t)}$。$\blacksquare$

**Physical meaning.** The propagator $K(x', t; x, 0)$ is the probability amplitude for a particle at $x$ at time $0$ to be found at $x'$ at time $t$. It is a Gaussian with width $\sim \sqrt{\hbar t/m}$ that spreads in time — the quantum spreading of a free wave packet.

**物理含义。** 传播子 $K(x', t; x, 0)$ 是粒子在 $t = 0$ 时刻位于 $x$、在 $t$ 时刻被发现于 $x'$ 的概率振幅。它是宽度 $\sim \sqrt{\hbar t/m}$ 随时间扩展的高斯函数——自由波包的量子扩展。

---

## E. The Path Integral (Sketch) · 路径积分（概述）

**Claim.** The propagator can be written as a sum over all paths from $(x, 0)$ to $(x', t)$, weighted by $e^{iS[\text{path}]/\hbar}$ where $S$ is the classical action:

**命题。** 传播子可以写作从 $(x, 0)$ 到 $(x', t)$ 的所有路径的求和，权重为 $e^{iS[\text{路径}]/\hbar}$，其中 $S$ 为经典作用量：

$$ K(x', t; x, 0) = \int \mathcal{D}x(\tau) \cdot e^{iS[x(\tau)]/\hbar}, $$

where $S[x(\tau)] = \int_0^t L(x, \dot{x})\, d\tau = \int_0^t [\tfrac12 m\dot{x}^2 - V(x)]\, d\tau$.

其中 $S[x(\tau)] = \int_0^t L(x, \dot{x})\, d\tau = \int_0^t [\tfrac12 m\dot{x}^2 - V(x)]\, d\tau$。

**Step 1 — Divide the time interval.** Split $[0, t]$ into $N$ equal slices of width $\varepsilon = t/N$. By the composition property of the evolution operator, $\hat{U}(t) = [\hat{U}(\varepsilon)]^N$:

**第 1 步 — 划分时间区间。** 将 $[0, t]$ 分成 $N$ 个宽度为 $\varepsilon = t/N$ 的等份。由演化算符的复合性质，$\hat{U}(t) = [\hat{U}(\varepsilon)]^N$：

$$ \begin{aligned} K(x', t; x, 0) &= \langle x'|\hat{U}(\varepsilon)^N|x\rangle \\ &= \int\dots\int \langle x'|\hat{U}(\varepsilon)|x_{N-1}\rangle\langle x_{N-1}|\hat{U}(\varepsilon)|x_{N-2}\rangle\dots\langle x_1|\hat{U}(\varepsilon)|x\rangle\, dx_1\dots dx_{N-1}, \end{aligned} $$

inserting $(N-1)$ resolutions of identity $\int|x_j\rangle\langle x_j|\, dx_j = \hat{1}$.

插入 $(N-1)$ 个单位分解 $\int|x_j\rangle\langle x_j|\, dx_j = \hat{1}$。

**Step 2 — Short-time propagator.** For small $\varepsilon$, using $\hat{H} = \hat{p}^2/2m + V(\hat{x})$ and the Trotter product formula $e^{-i\hat{H}\varepsilon/\hbar} \approx e^{-i\hat{p}^2\varepsilon/2m\hbar} e^{-iV(\hat{x})\varepsilon/\hbar}$ (valid to first order in $\varepsilon$):

**第 2 步 — 短时传播子。** 对小 $\varepsilon$，利用 $\hat{H} = \hat{p}^2/2m + V(\hat{x})$ 与 Trotter 乘积公式 $e^{-i\hat{H}\varepsilon/\hbar} \approx e^{-i\hat{p}^2\varepsilon/2m\hbar} e^{-iV(\hat{x})\varepsilon/\hbar}$（对 $\varepsilon$ 一阶成立）：

$$ \langle x_{j+1}|\hat{U}(\varepsilon)|x_j\rangle \approx \langle x_{j+1}|e^{-i\hat{p}^2\varepsilon/2m\hbar}|x_j\rangle \cdot e^{-iV(x_j)\varepsilon/\hbar}. $$

The first factor is the free-particle propagator for time $\varepsilon$ (from Section D):

第一个因子是 $\varepsilon$ 时间的自由粒子传播子（来自 D 节）：

$$ \langle x_{j+1}|e^{-i\hat{p}^2\varepsilon/2m\hbar}|x_j\rangle = \sqrt{\frac{m}{2\pi i\hbar\varepsilon}}\, \exp\!\Big[\frac{im(x_{j+1}-x_j)^2}{2\hbar\varepsilon}\Big]. $$

So the short-time factor is:

故短时因子为：

$$ \begin{aligned} \langle x_{j+1}|\hat{U}(\varepsilon)|x_j\rangle &\approx \sqrt{\frac{m}{2\pi i\hbar\varepsilon}}\, \exp\!\Big\{\frac{i\varepsilon}{\hbar}\Big[\frac{m(x_{j+1}-x_j)^2}{2\varepsilon^2} - V(x_j)\Big]\Big\} \\ &= \sqrt{\frac{m}{2\pi i\hbar\varepsilon}}\, \exp\!\Big\{\frac{i\varepsilon}{\hbar}\Big[\tfrac12 m\dot{x}_j^2 - V(x_j)\Big]\Big\}, \end{aligned} $$

where $\dot{x}_j = (x_{j+1}-x_j)/\varepsilon$ is the discrete velocity.

其中 $\dot{x}_j = (x_{j+1}-x_j)/\varepsilon$ 为离散速度。

**Step 3 — Assemble and take $N \to \infty$.** Multiplying all $N$ short-time factors and taking $N \to \infty$ ($\varepsilon \to 0$):

**第 3 步 — 组合并取 $N \to \infty$。** 将所有 $N$ 个短时因子相乘，取 $N \to \infty$（$\varepsilon \to 0$）：

$$ \begin{aligned} K &= \lim_{N\to\infty} \Big(\frac{m}{2\pi i\hbar\varepsilon}\Big)^{N/2} \int\dots\int \exp\!\Big\{\frac{i}{\hbar} \sum_j \big[\tfrac12 m\dot{x}_j^2 - V(x_j)\big]\varepsilon\Big\}\, dx_1\dots dx_{N-1} \\ &\equiv \int \mathcal{D}x(\tau)\, \exp\!\Big\{\frac{i}{\hbar} \int_0^t \big[\tfrac12 m\dot{x}^2 - V(x)\big]\, d\tau\Big\} \\ &= \int \mathcal{D}x(\tau)\, e^{iS[x(\tau)]/\hbar}. \end{aligned} $$

The sum in the exponent converges to the action $S = \int L\, d\tau$.

指数中的求和收敛到作用量 $S = \int L\, d\tau$。

**Step 4 — Classical limit ($\hbar \to 0$).** When $\hbar \to 0$, the oscillatory integral is dominated by the path(s) of stationary phase: $\delta S = 0$. This is exactly the **principle of stationary action** (Hamilton's principle) that gives the classical equations of motion — the Euler–Lagrange equations. Thus the classical trajectory is the path of stationary phase in the quantum path integral, and quantum mechanics is seen as a sum over all histories weighted by $e^{iS/\hbar}$, reducing to the classical path in the $\hbar \to 0$ limit. $\blacksquare$

**第 4 步 — 经典极限（$\hbar \to 0$）。** 当 $\hbar \to 0$ 时，振荡积分由稳相点主导：$\delta S = 0$。这正是给出经典运动方程——欧拉–拉格朗日方程——的**最小作用量原理**（哈密顿原理）。因此经典轨迹是量子路径积分中的稳相路径，量子力学表现为以 $e^{iS/\hbar}$ 为权重的所有历史求和，在 $\hbar \to 0$ 极限下退化到经典路径。$\blacksquare$

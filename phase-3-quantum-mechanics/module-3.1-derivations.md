# Derivations — Module 3.1: The Wave Function
# 推导 — 模块 3.1：波函数

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.1](./module-3.1-the-wave-function.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.1](./module-3.1-the-wave-function.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Continuity Equation: $\partial|\psi|^2/\partial t + \partial j/\partial x = 0$ · 连续性方程

**Claim.** From the Schrödinger equation $i\hbar\,\partial\psi/\partial t = -(\hbar^2/2m)\partial^2\psi/\partial x^2 + V\psi$ (with $V$ real), the probability density $\rho = |\psi|^2$ and the probability current $j = (\hbar/2mi)(\psi^* \partial\psi/\partial x - \psi\,\partial\psi^*/\partial x)$ satisfy the local conservation law $\partial\rho/\partial t + \partial j/\partial x = 0$.

**命题。** 由薛定谔方程 $i\hbar\,\partial\psi/\partial t = -(\hbar^2/2m)\partial^2\psi/\partial x^2 + V\psi$（$V$ 为实数），概率密度 $\rho = |\psi|^2$ 与概率流密度 $j = (\hbar/2mi)(\psi^* \partial\psi/\partial x - \psi\,\partial\psi^*/\partial x)$ 满足局域守恒律 $\partial\rho/\partial t + \partial j/\partial x = 0$。

**Step 1 — Write down the Schrödinger equation and its complex conjugate.** Let $\hat{H} = -(\hbar^2/2m)\partial^2/\partial x^2 + V(x,t)$. The Schrödinger equation and its complex conjugate are (using real $V$):

**第 1 步 — 写出薛定谔方程及其复共轭。** 令 $\hat{H} = -(\hbar^2/2m)\partial^2/\partial x^2 + V(x,t)$。薛定谔方程及其复共轭为（利用 $V$ 为实数）：

$$ i\hbar\,\partial\psi/\partial t = -(\hbar^2/2m)\,\psi_{xx} + V\psi, \qquad \text{(SE)} $$

$$ -i\hbar\,\partial\psi^*/\partial t = -(\hbar^2/2m)\,\psi^*_{xx} + V\psi^*. \qquad \text{(SE*)} $$

**Step 2 — Differentiate $\rho = \psi^*\psi$ with respect to $t$.**

**第 2 步 — 对 $\rho = \psi^*\psi$ 关于 $t$ 求导。**

$$ \frac{\partial\rho}{\partial t} = \frac{\partial(\psi^*\psi)}{\partial t} = \Big(\frac{\partial\psi^*}{\partial t}\Big)\psi + \psi^*\Big(\frac{\partial\psi}{\partial t}\Big). $$

From (SE): $\partial\psi/\partial t = (1/i\hbar)[-(\hbar^2/2m)\psi_{xx} + V\psi] = (i\hbar/2m)\psi_{xx} - (iV/\hbar)\psi$.
From (SE*): $\partial\psi^*/\partial t = -(i\hbar/2m)\psi^*_{xx} + (iV/\hbar)\psi^*$.

由 (SE)：$\partial\psi/\partial t = (i\hbar/2m)\psi_{xx} - (iV/\hbar)\psi$。
由 (SE*)：$\partial\psi^*/\partial t = -(i\hbar/2m)\psi^*_{xx} + (iV/\hbar)\psi^*$。

**Step 3 — Substitute.** Insert these into $\partial\rho/\partial t$:

**第 3 步 — 代入。** 将它们代入 $\partial\rho/\partial t$：

$$ \frac{\partial\rho}{\partial t} = \big[(-i\hbar/2m)\psi^*_{xx} + (iV/\hbar)\psi^*\big]\psi + \psi^*\big[(i\hbar/2m)\psi_{xx} - (iV/\hbar)\psi\big]. $$

The potential terms cancel ($V$ is real):

势能项消去（$V$ 为实数）：

$$ \frac{\partial\rho}{\partial t} = (i\hbar/2m)(\psi^* \psi_{xx} - \psi^*_{xx} \psi). $$

**Step 4 — Recognize a divergence.** Notice that:

**第 4 步 — 识别散度结构。** 注意到：

$$ \frac{\partial}{\partial x}(\psi^* \psi_x - \psi^*_x \psi) = \psi^*_x \psi_x + \psi^* \psi_{xx} - \psi^*_{xx} \psi - \psi^*_x \psi_x = \psi^* \psi_{xx} - \psi^*_{xx} \psi. $$

Therefore:

因此：

$$ \frac{\partial\rho}{\partial t} = (i\hbar/2m)\,\frac{\partial}{\partial x}(\psi^* \psi_x - \psi^*_x \psi) = -\frac{\partial j}{\partial x}, $$

where we define:

其中定义：

$$ \mathbf{j} = -(i\hbar/2m)(\psi^* \partial\psi/\partial x - \psi\,\partial\psi^*/\partial x) = (\hbar/2mi)(\psi^* \psi_x - \psi^*_x \psi). $$

(Note: the two forms are identical since $1/(2mi) = -i/(2m) = -(i/2m)$.)

（注：两种形式等价，因为 $1/(2mi) = -i/(2m) = -(i/2m)$。）

**Step 5 — Write the continuity equation.**

**第 5 步 — 写出连续性方程。**

$$ \boxed{\,\frac{\partial\rho}{\partial t} + \frac{\partial j}{\partial x} = 0\,} \qquad \blacksquare $$

**Step 6 — Global conservation (normalization is preserved).** Integrate over all $x$:

**第 6 步 — 整体守恒（归一化守恒）。** 对全空间积分：

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\psi|^2\, dx = -[j]_{-\infty}^{\infty} = 0, $$

since $\psi \to 0$ as $|x| \to \infty$ for normalizable states, so $j \to 0$. Thus if $\int|\psi|^2\, dx = 1$ at $t = 0$, it remains $1$ for all $t$. $\blacksquare$

因为对可归一化的态，当 $|x| \to \infty$ 时 $\psi \to 0$，所以 $j \to 0$。因此若 $\int|\psi|^2\, dx = 1$ 在 $t = 0$ 时成立，则对所有 $t$ 均成立。$\blacksquare$

---

## B. Ehrenfest Theorem: $d\langle x\rangle/dt = \langle p\rangle/m$ · 埃伦费斯特定理

**Claim.** For a particle governed by the Schrödinger equation, $d\langle x\rangle/dt = \langle \hat{p}\rangle/m$, where $\langle x\rangle = \int \psi^* x \psi\, dx$ and $\langle \hat{p}\rangle = \int \psi^* (-i\hbar\,\partial/\partial x) \psi\, dx$.

**命题。** 对由薛定谔方程控制的粒子，$d\langle x\rangle/dt = \langle \hat{p}\rangle/m$，其中 $\langle x\rangle = \int \psi^* x \psi\, dx$，$\langle \hat{p}\rangle = \int \psi^* (-i\hbar\,\partial/\partial x) \psi\, dx$。

**Step 1 — Differentiate $\langle x\rangle$ under the integral sign.**

**第 1 步 — 在积分号下对 $\langle x\rangle$ 求导。**

$$ \frac{d\langle x\rangle}{dt} = \frac{d}{dt}\int \psi^* x \psi\, dx = \int \Big(\frac{\partial\psi^*}{\partial t}\cdot x\psi + \psi^*\cdot x\cdot\frac{\partial\psi}{\partial t}\Big) dx. $$

**Step 2 — Use the Schrödinger equation.** Substitute $\partial\psi/\partial t = (i\hbar/2m)\psi_{xx} - (i/\hbar)V\psi$ and $\partial\psi^*/\partial t = -(i\hbar/2m)\psi^*_{xx} + (i/\hbar)V\psi^*$:

**第 2 步 — 利用薛定谔方程。** 代入 $\partial\psi/\partial t = (i\hbar/2m)\psi_{xx} - (i/\hbar)V\psi$ 和 $\partial\psi^*/\partial t = -(i\hbar/2m)\psi^*_{xx} + (i/\hbar)V\psi^*$：

$$ \frac{d\langle x\rangle}{dt} = \int \big[-(i\hbar/2m)\psi^*_{xx} + (i/\hbar)V\psi^*\big] x \psi\, dx + \int \psi^* x \big[(i\hbar/2m)\psi_{xx} - (i/\hbar)V\psi\big] dx. $$

The potential terms $\pm(i/\hbar)V |\psi|^2$ cancel ($V$ is real):

势能项 $\pm(i/\hbar)V |\psi|^2$ 消去（$V$ 为实数）：

$$ \frac{d\langle x\rangle}{dt} = (i\hbar/2m) \int x (\psi^* \psi_{xx} - \psi^*_{xx} \psi)\, dx. $$

**Step 3 — Integrate by parts.** Integrate the term $\int x \psi^*_{xx} \psi\, dx$ by parts twice. First integration by parts on $\int x \psi^*_{xx} \psi\, dx$ (integrate $\psi^*_{xx}$, differentiate $x\psi$):

**第 3 步 — 分部积分。** 对 $\int x \psi^*_{xx} \psi\, dx$ 进行两次分部积分。第一次分部积分（对 $\psi^*_{xx}$ 积分，对 $x\psi$ 微分）：

$$ \int x \psi^*_{xx} \psi\, dx = [x \psi^*_x \psi]_{-\infty}^{\infty} - \int \psi^*_x (\psi + x \psi_x)\, dx = -\int \psi^*_x \psi\, dx - \int x \psi^*_x \psi_x\, dx. $$

Similarly, integrate by parts on $\int x \psi^* \psi_{xx}\, dx$ (integrate $\psi_{xx}$, differentiate $x\psi^*$):

类似地，对 $\int x \psi^* \psi_{xx}\, dx$ 分部积分（对 $\psi_{xx}$ 积分，对 $x\psi^*$ 微分）：

$$ \int x \psi^* \psi_{xx}\, dx = [x \psi^* \psi_x]_{-\infty}^{\infty} - \int \psi_x (\psi^* + x \psi^*_x)\, dx = -\int \psi_x \psi^*\, dx - \int x \psi^*_x \psi_x\, dx. $$

(Boundary terms vanish for normalizable $\psi$.)

（对可归一化的 $\psi$，边界项为零。）

Therefore:

因此：

$\psi^* \psi_{xx} - \psi^*_{xx} \psi$ integrated against $x$ gives:

$$ \int x (\psi^* \psi_{xx} - \psi^*_{xx} \psi)\, dx = \Big(-\int \psi_x \psi^*\, dx - \int x \psi^*_x \psi_x\, dx\Big) - \Big(-\int \psi^*_x \psi\, dx - \int x \psi^*_x \psi_x\, dx\Big) $$

$$ = -\int \psi^* \psi_x\, dx + \int \psi^*_x \psi\, dx = \int (\psi^*_x \psi - \psi^* \psi_x)\, dx. $$

**Step 4 — Further simplification.** Note that $\int \psi^*_x \psi\, dx = -\int \psi^* \psi_x\, dx$ by integration by parts (boundary term $= 0$):

**第 4 步 — 进一步化简。** 注意通过分部积分 $\int \psi^*_x \psi\, dx = -\int \psi^* \psi_x\, dx$（边界项 $= 0$）：

$$ \int (\psi^*_x \psi - \psi^* \psi_x)\, dx = -\int \psi^* \psi_x\, dx - \int \psi^* \psi_x\, dx = -2 \int \psi^* \psi_x\, dx. $$

Therefore:

因此：

$$ \frac{d\langle x\rangle}{dt} = (i\hbar/2m)(-2) \int \psi^* \psi_x\, dx = -(i\hbar/m) \int \psi^* (\partial\psi/\partial x)\, dx. $$

Recognizing $\hat{p} = -i\hbar\,\partial/\partial x$:

识别 $\hat{p} = -i\hbar\,\partial/\partial x$：

$$ \frac{d\langle x\rangle}{dt} = (1/m) \int \psi^* (-i\hbar\,\partial\psi/\partial x)\, dx = \boxed{\,\langle \hat{p}\rangle/m\,} \qquad \blacksquare $$

---

## C. Expectation Value and Uncertainty: $\langle Q\rangle$ and $\Delta Q$ · 期望值与不确定性：$\langle Q\rangle$ 与 $\Delta Q$

**Claim.** For any observable $Q$ with operator $\hat{Q}$, $\langle Q\rangle = \int \psi^* \hat{Q} \psi\, dx$ is a real number (for Hermitian $\hat{Q}$), and the spread $\Delta Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$ is well-defined and non-negative.

**命题。** 对任意可观测量 $Q$（算符 $\hat{Q}$），$\langle Q\rangle = \int \psi^* \hat{Q} \psi\, dx$ 是实数（对厄米 $\hat{Q}$），散布 $\Delta Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$ 定义良好且非负。

**Step 1 — Reality of $\langle Q\rangle$.** $\hat{Q}$ is Hermitian means $\langle\varphi|\hat{Q}\psi\rangle = \langle\hat{Q}\varphi|\psi\rangle$ for all $\varphi, \psi$ in the domain. Take $\varphi = \psi$:

**第 1 步 — $\langle Q\rangle$ 的实性。** $\hat{Q}$ 是厄米的意味着对定义域内所有 $\varphi$、$\psi$ 有 $\langle\varphi|\hat{Q}\psi\rangle = \langle\hat{Q}\varphi|\psi\rangle$。取 $\varphi = \psi$：

$$ \langle Q\rangle = \int \psi^* \hat{Q} \psi\, dx = \langle\psi|\hat{Q}\psi\rangle = \langle\hat{Q}\psi|\psi\rangle = \Big(\int \psi^* \hat{Q} \psi\, dx\Big)^* = \langle Q\rangle^*. $$

Therefore $\langle Q\rangle$ is real. $\blacksquare$

因此 $\langle Q\rangle$ 为实数。$\blacksquare$

**Step 2 — Non-negativity of $\Delta Q$.** Compute $\langle Q^2\rangle - \langle Q\rangle^2$:

**第 2 步 — $\Delta Q$ 的非负性。** 计算 $\langle Q^2\rangle - \langle Q\rangle^2$：

$$ \Delta Q^2 = \langle Q^2\rangle - \langle Q\rangle^2 = \langle(\hat{Q} - \langle Q\rangle)^2\rangle = \langle\psi|(\hat{Q} - \langle Q\rangle)^2|\psi\rangle. $$

Define the shifted operator $\tilde{Q} = \hat{Q} - \langle Q\rangle$ (which is also Hermitian). Then:

定义移位算符 $\tilde{Q} = \hat{Q} - \langle Q\rangle$（它也是厄米的）。则：

$$ \Delta Q^2 = \langle\psi|\tilde{Q}^2|\psi\rangle = \langle\psi|\tilde{Q}^\dagger\tilde{Q}|\psi\rangle = \langle\tilde{Q}\psi|\tilde{Q}\psi\rangle = \|\tilde{Q}\psi\|^2 \ge 0. $$

(Used $\tilde{Q}^\dagger = \tilde{Q}$ and the definition of inner product.) Therefore $\Delta Q = \|\tilde{Q}\psi\| \ge 0$. $\blacksquare$

（利用了 $\tilde{Q}^\dagger = \tilde{Q}$ 和内积的定义。）因此 $\Delta Q = \|\tilde{Q}\psi\| \ge 0$。$\blacksquare$

---

## D. Gaussian Wave Packet Saturates the Uncertainty Principle · 高斯波包使不确定性原理取等

**Claim.** For the normalized Gaussian wave function $\psi(x) = (2\pi\sigma^2)^{-1/4} \exp(-x^2/(4\sigma^2)) \exp(ip_0 x/\hbar)$, we have $\langle x\rangle = 0$, $\langle p\rangle = p_0$, $\Delta x = \sigma$, $\Delta p = \hbar/(2\sigma)$, and hence $\Delta x\cdot\Delta p = \hbar/2$ — the minimum uncertainty state.

**命题。** 对于归一化高斯波函数 $\psi(x) = (2\pi\sigma^2)^{-1/4} \exp(-x^2/(4\sigma^2)) \exp(ip_0 x/\hbar)$，有 $\langle x\rangle = 0$、$\langle p\rangle = p_0$、$\Delta x = \sigma$、$\Delta p = \hbar/(2\sigma)$，从而 $\Delta x\cdot\Delta p = \hbar/2$——最小不确定性态。

**Step 1 — Normalization check.** With $\rho(x) = |\psi(x)|^2 = (2\pi\sigma^2)^{-1/2} \exp(-x^2/(2\sigma^2))$:

**第 1 步 — 归一化验证。** 以 $\rho(x) = |\psi(x)|^2 = (2\pi\sigma^2)^{-1/2} \exp(-x^2/(2\sigma^2))$：

$$ \int_{-\infty}^{\infty} \rho\, dx = (2\pi\sigma^2)^{-1/2} \int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2)}\, dx = (2\pi\sigma^2)^{-1/2}\cdot\sqrt{2\pi\sigma^2} = 1. \;\checkmark $$

(Used the Gaussian integral $\int_{-\infty}^{\infty} e^{-ax^2}\, dx = \sqrt{\pi/a}$ with $a = 1/(2\sigma^2)$.)

（利用高斯积分 $\int_{-\infty}^{\infty} e^{-ax^2}\, dx = \sqrt{\pi/a}$，取 $a = 1/(2\sigma^2)$。）

**Step 2 — Position expectation.** Since $|\psi|^2$ is symmetric (even function of $x$):

**第 2 步 — 位置期望值。** 由于 $|\psi|^2$ 是对称函数（$x$ 的偶函数）：

$$ \langle x\rangle = \int x |\psi|^2\, dx = 0 \quad (\text{odd integrand over symmetric domain}). $$

**第 2 步 — 位置期望值。** $\langle x\rangle = 0$（被积函数为奇函数，积分区间对称）。

**Step 3 — $\langle x^2\rangle$.** Using the Gaussian moment integral $\int_{-\infty}^{\infty} x^2 e^{-x^2/(2\sigma^2)}\, dx = \sigma^2 \sqrt{2\pi\sigma^2}$:

**第 3 步 — $\langle x^2\rangle$。** 利用高斯矩积分 $\int_{-\infty}^{\infty} x^2 e^{-x^2/(2\sigma^2)}\, dx = \sigma^2 \sqrt{2\pi\sigma^2}$：

$$ \langle x^2\rangle = (2\pi\sigma^2)^{-1/2} \int x^2 e^{-x^2/(2\sigma^2)}\, dx = (2\pi\sigma^2)^{-1/2}\cdot\sigma^2\sqrt{2\pi\sigma^2} = \sigma^2. $$

Therefore $\Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{\sigma^2 - 0} = \boxed{\,\sigma\,}$. $\blacksquare$

**Step 4 — Momentum expectation.** Apply $\hat{p} = -i\hbar\,\partial/\partial x$:

**第 4 步 — 动量期望值。** 应用 $\hat{p} = -i\hbar\,\partial/\partial x$：

$$ \partial\psi/\partial x = \psi\cdot[-x/(2\sigma^2) + ip_0/\hbar]. $$

$$ \begin{aligned} \langle \hat{p}\rangle &= \int \psi^* (-i\hbar) \psi\cdot[-x/(2\sigma^2) + ip_0/\hbar]\, dx \\ &= -i\hbar\cdot\big[-1/(2\sigma^2) \int x|\psi|^2\, dx + ip_0/\hbar \int |\psi|^2\, dx\big] \\ &= -i\hbar\cdot[0 + ip_0/\hbar\cdot 1] = p_0. \end{aligned} $$

$\blacksquare$

**Step 5 — $\langle \hat{p}^2\rangle$.** Compute $\partial^2\psi/\partial x^2$:

**第 5 步 — $\langle \hat{p}^2\rangle$。** 计算 $\partial^2\psi/\partial x^2$：

$$ \partial\psi/\partial x = \psi\cdot(-x/(2\sigma^2) + ip_0/\hbar), $$

$$ \partial^2\psi/\partial x^2 = \partial\psi/\partial x\cdot(-x/(2\sigma^2) + ip_0/\hbar) + \psi\cdot(-1/(2\sigma^2)) = \psi\cdot(-x/(2\sigma^2) + ip_0/\hbar)^2 + \psi\cdot(-1/(2\sigma^2)). $$

$$ \langle \hat{p}^2\rangle = \int \psi^*(-\hbar^2) \partial^2\psi/\partial x^2\, dx = -\hbar^2 \int |\psi|^2 [(-x/(2\sigma^2) + ip_0/\hbar)^2 - 1/(2\sigma^2)]\, dx. $$

Expand $(-x/(2\sigma^2) + ip_0/\hbar)^2 = x^2/(4\sigma^4) - ix\cdot p_0/(\sigma^2\hbar) - p_0^2/\hbar^2$:

展开 $(-x/(2\sigma^2) + ip_0/\hbar)^2 = x^2/(4\sigma^4) - ix\cdot p_0/(\sigma^2\hbar) - p_0^2/\hbar^2$：

$$ \begin{aligned} \langle \hat{p}^2\rangle &= -\hbar^2 [\langle x^2\rangle/(4\sigma^4) - i\cdot p_0\cdot\langle x\rangle/(\sigma^2\hbar) - p_0^2/\hbar^2 - 1/(2\sigma^2)] \\ &= -\hbar^2 [\sigma^2/(4\sigma^4) - 0 - p_0^2/\hbar^2 - 1/(2\sigma^2)] \\ &= -\hbar^2 [1/(4\sigma^2) - p_0^2/\hbar^2 - 1/(2\sigma^2)] \\ &= -\hbar^2 [-1/(4\sigma^2) - p_0^2/\hbar^2] \\ &= \hbar^2/(4\sigma^2) + p_0^2. \end{aligned} $$

**Step 6 — $\Delta p$ and the product.**

**第 6 步 — $\Delta p$ 与不确定度积。**

$$ \Delta p^2 = \langle \hat{p}^2\rangle - \langle \hat{p}\rangle^2 = \hbar^2/(4\sigma^2) + p_0^2 - p_0^2 = \hbar^2/(4\sigma^2). $$

$$ \Delta p = \hbar/(2\sigma). $$

$$ \boxed{\,\Delta x\cdot\Delta p = \sigma\cdot\hbar/(2\sigma) = \hbar/2\,} \qquad \blacksquare $$

This is the absolute minimum allowed by the uncertainty principle (proven in Module 3.3-derivations). The Gaussian packet is the unique state that saturates $\Delta x\cdot\Delta p = \hbar/2$.

这是不确定性原理所允许的绝对最小值（在模块 3.3 推导中证明）。高斯波包是使 $\Delta x\cdot\Delta p = \hbar/2$ 取等的唯一态。$\blacksquare$

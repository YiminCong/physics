# Derivations — Module 3.7: Variational & WKB Methods
# 推导 — 模块 3.7：变分法与 WKB 方法

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.7](./module-3.7-variational-and-wkb-methods.md). Full step-by-step proofs of the variational theorem, the WKB wavefunction, the tunneling factor, and the Bohr–Sommerfeld quantization condition. English first, then 中文.
> [模块 3.7](./module-3.7-variational-and-wkb-methods.md) 的配套文档：变分定理、WKB 波函数、隧穿因子与玻尔–索末菲量子化条件的完整逐步证明。先英文，后中文。

---

## A. The Variational Theorem · 变分定理

**Claim.** For any normalized trial state $|\psi_\text{trial}\rangle$, the expectation value of the Hamiltonian satisfies $\langle\psi_\text{trial}|\hat{H}|\psi_\text{trial}\rangle \ge E_0$, where $E_0$ is the true ground-state energy.

**命题。** 对于任意归一化试探态 $|\psi_\text{trial}\rangle$，哈密顿量的期望值满足 $\langle\psi_\text{trial}|\hat{H}|\psi_\text{trial}\rangle \ge E_0$，其中 $E_0$ 为真实基态能量。

**Step 1 — Expand in the energy eigenbasis.** Assume $\hat{H}$ has a complete orthonormal set of eigenstates $\{|n\rangle\}$ with $\hat{H}|n\rangle = E_n|n\rangle$ and $E_0 \le E_1 \le E_2 \le \dots$. (By the spectral theorem for self-adjoint operators on $L^2$, such a basis exists whenever $\hat{H}$ has a purely discrete spectrum; in the general case with continuous spectrum the sum becomes an integral and the argument is unchanged in substance.) Expand the trial state as:

**第 1 步 — 在能量本征基中展开。** 假设 $\hat{H}$ 有完备正交归一本征态集 $\{|n\rangle\}$，满足 $\hat{H}|n\rangle = E_n|n\rangle$，$E_0 \le E_1 \le E_2 \le \dots$。（由 $L^2$ 上自伴算符的谱定理，当 $\hat{H}$ 具有纯离散谱时此类基存在；一般连续谱情形下求和变为积分，论证实质不变。）将试探态展开为：

$$ |\psi_\text{trial}\rangle = \sum_n c_n |n\rangle, \qquad c_n = \langle n|\psi_\text{trial}\rangle. $$

**Step 2 — Normalization constraint.** The normalization condition $\langle\psi_\text{trial}|\psi_\text{trial}\rangle = 1$ gives, using orthonormality $\langle m|n\rangle = \delta_{mn}$:

**第 2 步 — 归一化约束。** 归一化条件 $\langle\psi_\text{trial}|\psi_\text{trial}\rangle = 1$，利用正交归一性 $\langle m|n\rangle = \delta_{mn}$，得：

$$ \langle\psi_\text{trial}|\psi_\text{trial}\rangle = \sum_n |c_n|^2 = 1. $$

**Step 3 — Compute the expectation value.** Insert the expansion and act with $\hat{H}$:

**第 3 步 — 计算期望值。** 代入展开式，用 $\hat{H}$ 作用：

$$ \begin{aligned} \langle\psi_\text{trial}|\hat{H}|\psi_\text{trial}\rangle &= \Big(\sum_m c_m^* \langle m|\Big) \hat{H} \Big(\sum_n c_n |n\rangle\Big) \\ &= \sum_m \sum_n c_m^* c_n \langle m|\hat{H}|n\rangle \\ &= \sum_m \sum_n c_m^* c_n E_n \langle m|n\rangle \\ &= \sum_n |c_n|^2 E_n. \end{aligned} $$

**Step 4 — Apply the ground-state lower bound.** Since $E_n \ge E_0$ for all $n$, we may replace each $E_n$ in the sum by $E_0$ (making the sum smaller or equal):

**第 4 步 — 应用基态下界。** 由于对所有 $n$ 均有 $E_n \ge E_0$，可在求和中将每个 $E_n$ 替换为 $E_0$（使求和值减小或不变）：

$$ \sum_n |c_n|^2 E_n \ge \sum_n |c_n|^2 E_0 = E_0 \sum_n |c_n|^2 = E_0 \cdot 1 = E_0. $$

**Step 5 — Conclude.** Combining Steps 3 and 4:

**第 5 步 — 结论。** 综合第 3、4 步：

$$ \langle\psi_\text{trial}|\hat{H}|\psi_\text{trial}\rangle = \sum_n |c_n|^2 E_n \ge E_0. $$

Equality holds if and only if $c_n = 0$ for all $n$ with $E_n > E_0$, i.e. if and only if the trial state lies entirely within the ground-state eigenspace. Therefore minimizing $\langle\hat{H}\rangle$ over any family of trial states yields an upper bound on $E_0$ that approaches the true value as the family becomes more flexible. $\blacksquare$

等号成立当且仅当对所有 $E_n > E_0$ 的 $n$ 均有 $c_n = 0$，即试探态完全落在基态本征空间内。因此，在任意一族试探态上最小化 $\langle\hat{H}\rangle$ 给出 $E_0$ 的上界，随着该族函数越来越灵活，上界趋近真实值。$\blacksquare$

---

## B. The WKB Wavefunction · WKB 波函数

**Claim.** In the semiclassical limit $\hbar \to 0$ with the de Broglie wavelength varying slowly compared to its own length scale, the Schrödinger equation $-(\hbar^2/2m)\psi'' + V(x)\psi = E\psi$ admits the approximate solution $\psi(x) \approx \frac{C}{\sqrt{p(x)}} \exp\!\big[\frac{i}{\hbar}\int^x p(x')\,dx'\big]$, where $p(x) = \sqrt{2m(E - V(x))}$ is the local classical momentum.

**命题。** 在半经典极限 $\hbar \to 0$ 下，当德布罗意波长的变化相对自身长度可以忽略时，薛定谔方程 $-(\hbar^2/2m)\psi'' + V(x)\psi = E\psi$ 有近似解 $\psi(x) \approx \frac{C}{\sqrt{p(x)}} \exp\!\big[\frac{i}{\hbar}\int^x p(x')\,dx'\big]$，其中 $p(x) = \sqrt{2m(E - V(x))}$ 为局域经典动量。

**Step 1 — WKB ansatz.** Write the wavefunction as $\psi(x) = \exp[iS(x)/\hbar]$, where $S(x)$ is a complex-valued function (the "eikonal"). This is motivated by the plane-wave solution in the uniform case $V = \text{const}$, where $S = px - Et$ (classical action). Substituting into the Schrödinger equation:

**第 1 步 — WKB 拟设。** 将波函数写为 $\psi(x) = \exp[iS(x)/\hbar]$，其中 $S(x)$ 是复值函数（"程函"）。这受均匀情形 $V = \text{const}$ 下平面波解 $S = px - Et$（经典作用量）的启发。代入薛定谔方程：

$$ -\frac{\hbar^2}{2m} \Big(\frac{iS''}{\hbar} - \frac{(S')^2}{\hbar^2}\Big) \psi = (E - V)\,\psi. $$

Dividing both sides by $\psi$ (which is nowhere zero in the classically allowed region):

两边除以 $\psi$（在经典允许区域不为零）：

$$ \frac{(S')^2}{2m} - \frac{i\hbar S''}{2m} = E - V = \frac{p^2}{2m}. $$

**Step 2 — Expand in powers of $\hbar$.** Write $S = S_0 + (\hbar/i)S_1 + (\hbar/i)^2 S_2 + \dots$ and collect terms order by order.

**第 2 步 — 按 $\hbar$ 幂次展开。** 令 $S = S_0 + (\hbar/i)S_1 + (\hbar/i)^2 S_2 + \dots$，逐阶收集各项。

Order $\hbar^0$: $(S_0')^2 = p^2$, so $S_0' = \pm p(x)$, giving $S_0 = \pm\int^x p(x')\,dx'$.

$\hbar^0$ 阶：$(S_0')^2 = p^2$，故 $S_0' = \pm p(x)$，得 $S_0 = \pm\int^x p(x')\,dx'$。

Order $\hbar^1$ (taking the $+$ sign): $2S_0' S_1' = S_0''$, so $S_1' = S_0''/(2S_0') = p'/(2p)$. Integrating: $S_1 = \tfrac12\ln(p) + \text{const}$.

$\hbar^1$ 阶（取正号）：$2S_0' S_1' = S_0''$，故 $S_1' = S_0''/(2S_0') = p'/(2p)$。积分得：$S_1 = \tfrac12\ln(p) + \text{const}$。

**Step 3 — Reconstruct the wavefunction.** Inserting back into $\psi = \exp[iS/\hbar] = \exp[iS_0/\hbar]\cdot\exp[-S_1 + O(\hbar)]$:

**第 3 步 — 重构波函数。** 代回 $\psi = \exp[iS/\hbar] = \exp[iS_0/\hbar]\cdot\exp[-S_1 + O(\hbar)]$：

$$ \begin{aligned} \psi(x) &\approx \exp[-\tfrac12\ln p]\cdot\exp\!\Big[\frac{i}{\hbar}\int^x p\,dx'\Big] \\ &= \frac{1}{\sqrt{p(x)}}\cdot\exp\!\Big[\frac{i}{\hbar}\int^x p(x')\,dx'\Big]. \end{aligned} $$

Including both sign choices and absorbing the normalization constants $A$, $B$:

包含两种符号选择，将归一化常数记为 $A$、$B$：

$$ \psi(x) \approx \frac{A}{\sqrt{p(x)}}\exp\!\Big[\frac{i}{\hbar}\int^x p\,dx'\Big] + \frac{B}{\sqrt{p(x)}}\exp\!\Big[-\frac{i}{\hbar}\int^x p\,dx'\Big]. $$

**Step 4 — Validity condition.** The expansion is valid when higher-order terms are small, i.e. $|\hbar\,d\lambda/dx| \ll 1$, where $\lambda = h/p$ is the de Broglie wavelength. Equivalently:

**第 4 步 — 有效条件。** 展开有效的条件是高阶项很小，即 $|\hbar\,d\lambda/dx| \ll 1$，其中 $\lambda = h/p$ 为德布罗意波长。等价地：

$$ |dp/dx| \ll p^2/\hbar, \qquad \text{i.e.} \qquad |d(\hbar/p)/dx| \ll 1. $$

This fails near classical turning points where $p \to 0$. There the WKB approximation breaks down and connection formulae (involving Airy functions) must be used to match solutions across the turning point. $\blacksquare$

这在经典转折点附近 $p \to 0$ 处失效。在转折点处 WKB 近似失效，必须使用联结公式（涉及艾里函数）将两侧的解匹配起来。$\blacksquare$

---

## C. The WKB Tunneling Factor · WKB 隧穿因子

**Claim.** For a classically forbidden region $x_1 \le x \le x_2$ where $E < V(x)$ (so the local momentum is imaginary, $p(x) = i|p(x)|$ with $|p(x)| = \sqrt{2m(V(x) - E)}$), the WKB transmission amplitude is exponentially suppressed, giving a tunneling probability:

**命题。** 对于经典禁区 $x_1 \le x \le x_2$，其中 $E < V(x)$（局域动量为虚数，$p(x) = i|p(x)|$，$|p(x)| = \sqrt{2m(V(x) - E)}$），WKB 透射振幅呈指数衰减，隧穿概率为：

$$ T \approx \exp\!\Big[-\frac{2}{\hbar}\int_{x_1}^{x_2} |p(x)|\,dx\Big]. $$

**Step 1 — WKB in the forbidden region.** When $E < V(x)$, define $\kappa(x) = \sqrt{2m(V(x) - E)}/\hbar > 0$. The local "momentum" becomes purely imaginary: $p = i\hbar\kappa$. The WKB ansatz gives:

**第 1 步 — 禁区中的 WKB。** 当 $E < V(x)$ 时，定义 $\kappa(x) = \sqrt{2m(V(x) - E)}/\hbar > 0$。局域"动量"变为纯虚数：$p = i\hbar\kappa$。WKB 拟设给出：

$$ \psi(x) \approx \frac{C}{\sqrt{\kappa(x)}}\exp\!\Big[-\int_{x_1}^{x} \kappa(x')\,dx'\Big] + \frac{D}{\sqrt{\kappa(x)}}\exp\!\Big[+\int_{x_1}^{x} \kappa(x')\,dx'\Big]. $$

The growing exponential ($D$ term) must be set to zero for a bound tunneling problem (or matched via connection formulae to an outgoing wave on the right); the decaying exponential is the tunneling solution.

增长指数项（$D$ 项）在束缚隧穿问题中必须为零（或通过联结公式与右侧出射波匹配）；衰减指数项即隧穿解。

**Step 2 — Amplitude ratio across the barrier.** The amplitude of the transmitted wave at $x_2$ relative to the incident wave at $x_1$ is:

**第 2 步 — 势垒两侧振幅比。** 在 $x_2$ 处透射波振幅与 $x_1$ 处入射波振幅之比为：

$$ \frac{\psi(x_2)}{\psi(x_1)} = \exp\!\Big[-\int_{x_1}^{x_2} \kappa(x)\,dx\Big] = \exp\!\Big[-\frac{1}{\hbar}\int_{x_1}^{x_2} \sqrt{2m(V-E)}\,dx\Big]. $$

**Step 3 — Transmission probability.** The transmission coefficient $T$ is the ratio of transmitted to incident probability current $j = (\hbar/m)\,\text{Im}(\psi^* \,d\psi/dx)$. Since the probability current is proportional to $|\psi|^2$ times the velocity in the WKB approximation, $T \approx |\psi(x_2)/\psi(x_1)|^2$, giving:

**第 3 步 — 透射概率。** 透射系数 $T$ 是透射概率流与入射概率流之比 $j = (\hbar/m)\,\text{Im}(\psi^* \,d\psi/dx)$。在 WKB 近似中概率流正比于 $|\psi|^2$ 乘以速度，故 $T \approx |\psi(x_2)/\psi(x_1)|^2$，得：

$$ T \approx \exp\!\Big[-\frac{2}{\hbar}\int_{x_1}^{x_2} |p(x)|\,dx\Big], $$

where $|p(x)| = \sqrt{2m(V(x) - E)} = \hbar\kappa(x)$. $\blacksquare$

其中 $|p(x)| = \sqrt{2m(V(x) - E)} = \hbar\kappa(x)$。$\blacksquare$

**Physical interpretation.** The exponent is the "WKB integral" or "tunneling integral." For alpha decay, the barrier is the Coulomb potential; this integral gives the Gamow factor explaining the enormous range of decay rates (factor of $10^{20}$) by modest variation in alpha-particle energy.

**物理诠释。** 指数中的量为"WKB 积分"或"隧穿积分"。对于 $\alpha$ 衰变，势垒为库仑势；此积分给出伽莫夫因子，解释了衰变率极大范围的变化（相差 $10^{20}$ 倍）如何由 $\alpha$ 粒子能量的适度变化产生。

---

## D. Bohr–Sommerfeld Quantization · 玻尔–索末菲量子化

**Claim.** For a classically allowed region between two turning points $x_1$ and $x_2$, the WKB quantization condition is $\oint p\,dx = (n + \tfrac12)h$, where the integral is over one complete classical oscillation and $n = 0, 1, 2, \dots$

**命题。** 对于两个转折点 $x_1$ 和 $x_2$ 之间的经典允许区域，WKB 量子化条件为 $\oint p\,dx = (n + \tfrac12)h$，其中积分取一个完整经典振荡，$n = 0, 1, 2, \dots$

**Step 1 — WKB solution in the classically allowed region.** Between the turning points, $p(x) = \sqrt{2m(E - V(x))} > 0$. The general WKB solution is:

**第 1 步 — 经典允许区域中的 WKB 解。** 在转折点之间，$p(x) = \sqrt{2m(E - V(x))} > 0$。一般 WKB 解为：

$$ \psi(x) = \frac{A}{\sqrt{p}}\exp\!\Big[\frac{i}{\hbar}\int_{x_1}^{x} p\,dx'\Big] + \frac{B}{\sqrt{p}}\exp\!\Big[-\frac{i}{\hbar}\int_{x_1}^{x} p\,dx'\Big]. $$

**Step 2 — Connection formulae at turning points.** Near a left turning point $x_1$ (where $V(x_1) = E$ and $p \to 0$ from the right), the exact solution is an Airy function. Matching the WKB forms across $x_1$ gives the connection:

**第 2 步 — 转折点处的联结公式。** 在左转折点 $x_1$（其中 $V(x_1) = E$，$p$ 从右侧趋向 0）附近，精确解为艾里函数。在 $x_1$ 两侧匹配 WKB 形式给出联结公式：

$$ \text{Decaying side: } \frac{C}{\sqrt{\kappa}}\exp\!\Big[-\int\kappa\,dx\Big] \;\leftrightarrow\; \text{Oscillating side: } \frac{2C}{\sqrt{p}}\cos\!\Big[\frac{1}{\hbar}\int_{x_1}^{x} p\,dx' - \frac{\pi}{4}\Big]. $$

The phase shift of $-\pi/4$ arises from the asymptotic behavior of the Airy function $\text{Ai}(z) \sim \tfrac12 z^{-1/4}\exp(-\tfrac23 z^{3/2})$ for $z \to +\infty$ and $\text{Ai}(z) \sim z^{-1/4}\sin(\tfrac23|z|^{3/2} + \tfrac{\pi}{4})$ for $z \to -\infty$.

$-\pi/4$ 的相移来自艾里函数 $\text{Ai}(z)$ 的渐近行为：当 $z \to +\infty$ 时 $\text{Ai}(z) \sim \tfrac12 z^{-1/4}\exp(-\tfrac23 z^{3/2})$；当 $z \to -\infty$ 时 $\text{Ai}(z) \sim z^{-1/4}\sin(\tfrac23|z|^{3/2} + \tfrac{\pi}{4})$。

Similarly, at the right turning point $x_2$, matching gives a phase shift of $-\pi/4$ from that end.

类似地，在右转折点 $x_2$ 处，匹配给出来自该端 $-\pi/4$ 的相移。

**Step 3 — Impose single-valuedness.** The WKB wavefunction in the interior must match at both ends simultaneously. Working from the left connection formula:

**第 3 步 — 施加单值性条件。** 内部的 WKB 波函数必须同时与两端匹配。从左端联结公式出发：

$$ \psi \propto \cos\!\Big[\frac{1}{\hbar}\int_{x_1}^{x} p\,dx' - \frac{\pi}{4}\Big]. $$

Working from the right connection formula, the solution from the right must be:

从右端联结公式出发，从右侧得到的解必须为：

$$ \psi \propto \cos\!\Big[\frac{1}{\hbar}\int_{x}^{x_2} p\,dx' - \frac{\pi}{4}\Big]. $$

Using $\cos\theta = \cos(-\theta)$, write the right-derived solution as:

利用 $\cos\theta = \cos(-\theta)$，将右侧推导的解写为：

$$ \begin{aligned} \psi &\propto \cos\!\Big[-\frac{1}{\hbar}\int_{x}^{x_2} p\,dx' + \frac{\pi}{4}\Big] \\ &= \cos\!\Big[\frac{1}{\hbar}\int_{x_1}^{x} p\,dx' - \frac{1}{\hbar}\int_{x_1}^{x_2} p\,dx' + \frac{\pi}{4}\Big]. \end{aligned} $$

**Step 4 — Matching condition.** For the two expressions to represent the same function (up to an overall sign), their arguments must differ by a multiple of $\pi$:

**第 4 步 — 匹配条件。** 为使两个表达式表示同一函数（相差整体符号），其自变量必须相差 $\pi$ 的整数倍：

$$ \Big[\frac{1}{\hbar}\int_{x_1}^{x} p\,dx' - \frac{\pi}{4}\Big] - \Big[\frac{1}{\hbar}\int_{x_1}^{x} p\,dx' - \frac{1}{\hbar}\Phi + \frac{\pi}{4}\Big] = n\pi, $$

where $\Phi = \int_{x_1}^{x_2} p\,dx$. Simplifying:

其中 $\Phi = \int_{x_1}^{x_2} p\,dx$。化简：

$$ \frac{1}{\hbar}\Phi - \frac{\pi}{2} = n\pi, \qquad n = 0, 1, 2, \dots $$

$$ \frac{1}{\hbar}\int_{x_1}^{x_2} p\,dx = (n + \tfrac12)\pi. $$

**Step 5 — Bohr–Sommerfeld condition.** Multiplying both sides by $2\hbar$ and noting that one full oscillation $= 2 \times (x_1 \text{ to } x_2)$:

**第 5 步 — 玻尔–索末菲条件。** 两边乘以 $2\hbar$，注意一次完整振荡 $= 2 \times (x_1 \text{ 到 } x_2)$：

$$ \oint p\,dx = 2\int_{x_1}^{x_2} p\,dx = (2n + 1)\pi\hbar = (n + \tfrac12)h, \qquad n = 0, 1, 2, \dots $$

The $\tfrac12$ (the "Maslov correction" from the two $\pi/4$ phase shifts at the turning points) is essential: it gives the correct zero-point energy for the harmonic oscillator ($n = 0$ gives $E_0 = \tfrac12\hbar\omega$, not zero). $\blacksquare$

其中 $\tfrac12$（来自两个转折点处 $\pi/4$ 相移的"马斯洛夫修正"）至关重要：它给出谐振子正确的零点能（$n = 0$ 给出 $E_0 = \tfrac12\hbar\omega$，而非零）。$\blacksquare$

**Check — Harmonic oscillator.** For $V = \tfrac12 m\omega^2 x^2$, the turning points satisfy $\tfrac12 m\omega^2 x_{1,2}^2 = E$, so $x_{1,2} = \mp\sqrt{2E/m\omega^2}$. The integral is $\int_{x_1}^{x_2} p\,dx = \pi E/\omega$ (the area of an ellipse in phase space). The Bohr–Sommerfeld condition gives $2(\pi E/\omega) = (n + \tfrac12)h$, so $E = (n + \tfrac12)\hbar\omega$ — exact agreement with the ladder-operator result.

**验证——谐振子。** 对 $V = \tfrac12 m\omega^2 x^2$，转折点满足 $\tfrac12 m\omega^2 x_{1,2}^2 = E$，故 $x_{1,2} = \mp\sqrt{2E/m\omega^2}$。积分为 $\int_{x_1}^{x_2} p\,dx = \pi E/\omega$（相空间中椭圆的面积）。玻尔–索末菲条件给出 $2(\pi E/\omega) = (n + \tfrac12)h$，故 $E = (n + \tfrac12)\hbar\omega$——与梯形算符结果完全一致。

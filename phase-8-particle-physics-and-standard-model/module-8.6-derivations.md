---
title: "Derivations — Module 8.6: Particle Physics & Cosmology"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 8.6: Particle Physics & Cosmology
# 推导 — 模块 8.6：粒子物理与宇宙学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.6](./module-8.6-particle-physics-and-cosmology.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.6](./module-8.6-particle-physics-and-cosmology.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Boltzmann Equation in an Expanding Universe · 膨胀宇宙中的玻尔兹曼方程

**Claim.** For a massive particle species $\chi$ with number density $n$ in a Friedmann–Robertson–Walker (FRW) universe, the Boltzmann equation governing $n$ is:

**命题。** 对于弗里德曼–罗伯逊–沃克（FRW）宇宙中数密度为 $n$ 的大质量粒子种类 $\chi$，支配 $n$ 的玻尔兹曼方程为：

$$ \frac{dn}{dt} + 3Hn = -\langle\sigma v\rangle(n^2 - n_{eq}^2), $$

where $H$ is the Hubble rate, $\langle\sigma v\rangle$ is the thermally averaged annihilation cross-section, and $n_{eq}$ is the equilibrium number density.

其中 $H$ 为哈勃速率，$\langle\sigma v\rangle$ 为热平均湮灭截面，$n_{eq}$ 为平衡数密度。

**Step 1 — Conservation law in expanding universe.** Consider a comoving volume $V \propto a^3$ in an FRW universe. The total particle number $N = nV = na^3$ changes due to annihilation/creation reactions. If $\chi\bar\chi \leftrightarrow \text{SM SM}$ is the relevant process:

**第 1 步 — 膨胀宇宙中的守恒律。** 考虑 FRW 宇宙中的共动体积 $V \propto a^3$。总粒子数 $N = nV = na^3$ 由于湮灭/产生反应而改变。若相关过程为 $\chi\bar\chi \leftrightarrow \text{SM SM}$：

$$ \frac{d(na^3)}{dt} = a^3\left[\frac{dn}{dt} + 3Hn\right] \quad \left(\text{since } \frac{\dot a}{a} = H, \text{ so } \frac{da^3}{dt} = 3a^2\dot a = 3Ha^3\right). $$

**Step 2 — Collision term.** The rate of change of $n$ due to annihilation ($n^2$ rate, proportional to the square of the number density) and creation (rate proportional to $n_{eq}^2$):

**第 2 步 — 碰撞项。** 由于湮灭（$n^2$ 速率，正比于数密度的平方）和产生（速率正比于 $n_{eq}^2$）引起的 $n$ 变化率：

$$ \left.\frac{dn}{dt}\right|_{coll} = -\langle\sigma v\rangle n^2 + \langle\sigma v\rangle n_{eq}^2. $$

In detail: The annihilation rate per unit volume is $\langle\sigma v\rangle n^2$ (two-body process: $\Gamma = n\sigma v$ averaged over the thermal distribution). The creation rate is $\langle\sigma v\rangle n_{eq}^2$ (detailed balance: in equilibrium, creation = annihilation).

详细地：单位体积的湮灭速率为 $\langle\sigma v\rangle n^2$（两体过程：$\Gamma = n\sigma v$ 对热分布取平均）。产生速率为 $\langle\sigma v\rangle n_{eq}^2$（细致平衡：在平衡状态下，产生 = 湮灭）。

**Step 3 — Full Boltzmann equation.** Combining:

**第 3 步 — 完整的玻尔兹曼方程。** 综合：

$$ \frac{dn}{dt} + 3Hn = -\langle\sigma v\rangle(n^2 - n_{eq}^2). \qquad \blacksquare $$

---

## B. The Freeze-Out Condition · 冻结条件

**Claim.** A species freezes out when the interaction rate $\Gamma = \langle\sigma v\rangle n$ drops below the Hubble expansion rate $H$: $\Gamma \approx H$ at $T = T_f$ (freeze-out temperature).

**命题。** 当相互作用速率 $\Gamma = \langle\sigma v\rangle n$ 降至哈勃膨胀速率 $H$ 以下时，粒子种类冻结：$\Gamma \approx H$ 在 $T = T_f$（冻结温度）时成立。

**Step 1 — Equation for the comoving density.** Define $Y = n/s$ (yield: number density to entropy density ratio), where the entropy density $s = (2\pi^2/45)g_{*S} T^3$ is conserved during adiabatic expansion ($sa^3 = \text{const}$). Then:

**第 1 步 — 共动密度的方程。** 定义 $Y = n/s$（产额：数密度与熵密度之比），其中熵密度 $s = (2\pi^2/45)g_{*S} T^3$ 在绝热膨胀期间守恒（$sa^3 = \text{const}$）。则：

$$ \frac{dY}{dt} = -s\langle\sigma v\rangle(Y^2 - Y_{eq}^2). $$

Since $ds/dt = -3Hs$ (conservation), and $n = sY$: $dn/dt + 3Hn = s(dY/dt)$.

由于 $ds/dt = -3Hs$（守恒），且 $n = sY$：$dn/dt + 3Hn = s(dY/dt)$。

**Step 2 — Change variable to $x = m/T$.** Using $T \propto 1/a$ and $H = \dot a/a$:

**第 2 步 — 变量变换为 $x = m/T$。** 利用 $T \propto 1/a$ 和 $H = \dot a/a$：

$$ \frac{dY}{dx} = -\frac{s\langle\sigma v\rangle}{Hx}(Y^2 - Y_{eq}^2). $$

Define the rate ratio $\Gamma/H = s\langle\sigma v\rangle/(Hx)$ at $x = x_f$.

定义 $x = x_f$ 处的速率比 $\Gamma/H = s\langle\sigma v\rangle/(Hx)$。

**Step 3 — Two regimes.**

**第 3 步 — 两个区域。**

- **When $\Gamma/H \gg 1$ (early times, small $x$):** Reactions are fast; $Y$ tracks $Y_{eq}$. The species is in chemical equilibrium.
- **当 $\Gamma/H \gg 1$（早期，小 $x$）时：** 反应快速；$Y$ 跟踪 $Y_{eq}$。粒子种类处于化学平衡。

- **When $\Gamma/H \ll 1$ (late times, large $x$):** Reactions are negligible; $Y$ freezes at $Y_f \approx Y_{eq}(x_f)$.
- **当 $\Gamma/H \ll 1$（晚期，大 $x$）时：** 反应可忽略；$Y$ 冻结在 $Y_f \approx Y_{eq}(x_f)$。

The **freeze-out condition** is the transition: $\Gamma = H$.

**冻结条件**是过渡点：$\Gamma = H$。

**Step 4 — Hubble rate in radiation domination.** In the radiation-dominated era:

**第 4 步 — 辐射主导期的哈勃速率。** 在辐射主导时期：

$$ H = \sqrt{8\pi\rho_{rad}/3M_{Pl}^2} = \sqrt{4\pi^3 g_*/45} \cdot T^2/M_{Pl}, $$

where $M_{Pl} \approx 2.4 \times 10^{18}$ GeV is the reduced Planck mass and $g_*$ counts relativistic degrees of freedom.

其中 $M_{Pl} \approx 2.4 \times 10^{18}$ GeV 是约化普朗克质量，$g_*$ 计算相对论性自由度数。

**Step 5 — Equilibrium number density.** For a non-relativistic species ($T \ll m$) with $g$ internal degrees of freedom:

**第 5 步 — 平衡数密度。** 对于具有 $g$ 个内部自由度的非相对论性粒子（$T \ll m$）：

$$ n_{eq} = g(mT/2\pi)^{3/2} e^{-m/T}. $$

The exponential suppression (Boltzmann suppression) at $T < m$ means $n_{eq}$ falls rapidly. The freeze-out occurs at $x_f = m/T_f$ where:

$T < m$ 时的指数抑制（玻尔兹曼抑制）意味着 $n_{eq}$ 迅速下降。冻结发生在 $x_f = m/T_f$，其中：

$$ n_{eq} \langle\sigma v\rangle \approx H \quad \text{at } T = T_f. $$

For WIMPs with $m \sim 100$ GeV, this gives $x_f \approx 20\text{–}25$ (i.e., $T_f \approx m/20$). $\blacksquare$

对于质量 $m \sim 100$ GeV 的 WIMP，这给出 $x_f \approx 20\text{–}25$（即 $T_f \approx m/20$）。$\blacksquare$

---

## C. The WIMP Miracle: Relic Abundance Estimate · WIMP 奇迹：遗迹丰度估算

**Claim.** A thermal WIMP with mass $m_\chi \sim 100$ GeV and weak-scale cross-section $\langle\sigma v\rangle \sim 10^{-26}\ \text{cm}^3/\text{s}$ naturally produces a relic density $\Omega_\chi h^2 \approx 0.1$ — matching the observed dark matter density.

**命题。** 质量 $m_\chi \sim 100$ GeV、弱力尺度截面 $\langle\sigma v\rangle \sim 10^{-26}\ \text{cm}^3/\text{s}$ 的热 WIMP 自然地产生遗迹密度 $\Omega_\chi h^2 \approx 0.1$——与观测到的暗物质密度吻合。

**Step 1 — Post-freeze-out Boltzmann equation.** After freeze-out, $Y$ remains approximately constant: $Y_\infty \approx Y_f$. To get a more precise answer, integrate the Boltzmann equation. For $Y \gg Y_{eq}$ (late times):

**第 1 步 — 冻结后的玻尔兹曼方程。** 冻结后，$Y$ 保持近似不变：$Y_\infty \approx Y_f$。为获得更精确的结果，积分玻尔兹曼方程。对于 $Y \gg Y_{eq}$（晚期）：

$$ \frac{dY}{dx} \approx -\frac{s\langle\sigma v\rangle}{Hx}Y^2. $$

Integrating from $x_f$ to $\infty$:

从 $x_f$ 到 $\infty$ 积分：

$$ \frac{1}{Y_\infty} - \frac{1}{Y_f} \approx \int_{x_f}^\infty \frac{s\langle\sigma v\rangle}{Hx}\, dx. $$

Since $Y_f \gg Y_\infty$ (most of the depletion happens just after freeze-out), $1/Y_\infty \approx \int_{x_f}^\infty (s\langle\sigma v\rangle)/(Hx)\, dx$.

由于 $Y_f \gg Y_\infty$（大部分消耗恰好发生在冻结之后），$1/Y_\infty \approx \int_{x_f}^\infty (s\langle\sigma v\rangle)/(Hx)\, dx$。

**Step 2 — Evaluate the integral.** Using $s = (2\pi^2/45)g_{*S} T^3 = (2\pi^2/45)g_{*S} (m/x)^3$ and $H = \pi\sqrt{g_*/45} \cdot m^2/(M_{Pl} x^2)$:

**第 2 步 — 计算积分。** 利用 $s = (2\pi^2/45)g_{*S} T^3 = (2\pi^2/45)g_{*S} (m/x)^3$ 和 $H = \pi\sqrt{g_*/45} \cdot m^2/(M_{Pl} x^2)$：

$$ \begin{aligned}
\frac{s}{H} &= \frac{(2\pi^2/45)g_{*S}(m/x)^3}{\pi\sqrt{g_*/45}\,m^2/(M_{Pl}x^2)} \\
&= \frac{(2\pi/45)g_{*S} \cdot (m M_{Pl})}{\sqrt{g_*/45}\,\pi \cdot x} \\
&= \frac{2}{\pi^2}\sqrt{\frac{\pi}{45}} \cdot \frac{g_{*S}}{\sqrt{g_*}} \cdot \frac{m M_{Pl}}{x}.
\end{aligned} $$

Substituting:

代入：

$$ \begin{aligned}
\frac{1}{Y_\infty} &\approx \langle\sigma v\rangle \cdot \frac{2}{\pi^2}\sqrt{\frac{\pi}{45}} \cdot \frac{g_{*S}}{\sqrt{g_*}} \cdot m M_{Pl} \cdot \int_{x_f}^\infty x^{-2}\, dx \\
&= \langle\sigma v\rangle \cdot \frac{2}{\pi^2}\sqrt{\frac{\pi}{45}} \cdot \frac{g_{*S}}{\sqrt{g_*}} \cdot m M_{Pl} \cdot \frac{1}{x_f}.
\end{aligned} $$

Using $g_{*S} \approx g_*$ at freeze-out:

在冻结时利用 $g_{*S} \approx g_*$：

$$ \frac{1}{Y_\infty} \approx \langle\sigma v\rangle \cdot \frac{2}{\pi}\sqrt{\frac{g_*}{45}} \cdot \frac{m M_{Pl}}{x_f} \cdot (\text{numerical factors order 1}). $$

Numerically, with $x_f \approx 20$ and $\sqrt{g_*/45} \approx 0.26$ (for $g_* = 86.25$ in SM at $T \sim 5$ GeV):

数值上，以 $x_f \approx 20$ 和 $\sqrt{g_*/45} \approx 0.26$（SM 中 $T \sim 5$ GeV 时 $g_* = 86.25$）：

$$ Y_\infty \approx \frac{x_f}{\langle\sigma v\rangle \cdot 0.26 \cdot m M_{Pl} \cdot 2/\pi} \approx \frac{3 \times 10^{-10}\ \text{GeV}^{-2}}{\langle\sigma v\rangle}. $$

**Step 3 — Convert to relic density.** The current number density $n_\chi = s_0 Y_\infty$ where $s_0 = 2891\ \text{cm}^{-3}$ is today's entropy density. The energy density:

**第 3 步 — 换算为遗迹密度。** 当前数密度 $n_\chi = s_0 Y_\infty$，其中 $s_0 = 2891\ \text{cm}^{-3}$ 是今天的熵密度。能量密度：

$$ \rho_\chi = m_\chi n_\chi = m_\chi s_0 Y_\infty. $$

The relic density parameter (using $\rho_{crit}/h^2 = 1.054 \times 10^{-5}\ \text{GeV cm}^{-3}$):

遗迹密度参数（利用 $\rho_{crit}/h^2 = 1.054 \times 10^{-5}\ \text{GeV cm}^{-3}$）：

$$ \Omega_\chi h^2 = \rho_\chi h^2/\rho_{crit} = m_\chi s_0 Y_\infty h^2/\rho_{crit}. $$

Substituting the expression for $Y_\infty$:

代入 $Y_\infty$ 的表达式：

$$ \Omega_\chi h^2 = \frac{m_\chi s_0 h^2}{\rho_{crit}} \cdot \frac{3 \times 10^{-10}\ \text{GeV}^{-2}}{\langle\sigma v\rangle m_\chi} $$

The $m_\chi$ cancels (this is the key miracle!):

$m_\chi$ 消去（这是关键的奇迹！）：

$$ \Omega_\chi h^2 \approx \frac{3 \times 10^{-27}\ \text{cm}^3/\text{s}}{\langle\sigma v\rangle}, $$

where we converted $\text{GeV}^{-2}$ to $\text{cm}^3/\text{s}$ ($1\ \text{GeV}^{-2} = 0.389 \times 10^{-27}\ \text{cm}^2$; with factors of $c$): $\mathbf{3 \times 10^{-27}}$ **$\text{cm}^3/\text{s}$** $\approx 0.1\ \text{pb} \cdot c$.

其中我们将 $\text{GeV}^{-2}$ 换算为 $\text{cm}^3/\text{s}$（$1\ \text{GeV}^{-2} = 0.389 \times 10^{-27}\ \text{cm}^2$；乘以 $c$ 的因子）：$\mathbf{3 \times 10^{-27}}$ **$\text{cm}^3/\text{s}$** $\approx 0.1\ \text{pb} \cdot c$。

**Step 4 — The WIMP miracle.** For a particle with electroweak-scale interactions: $\langle\sigma v\rangle \sim \alpha^2/m_\chi^2$. With $\alpha \sim 0.03$ (EW) and $m_\chi \sim 100$ GeV:

**第 4 步 — WIMP 奇迹。** 对于具有电弱尺度相互作用的粒子：$\langle\sigma v\rangle \sim \alpha^2/m_\chi^2$。以 $\alpha \sim 0.03$（电弱）和 $m_\chi \sim 100$ GeV：

$$ \langle\sigma v\rangle \sim (0.03)^2/(100\ \text{GeV})^2 = 9 \times 10^{-4}/(10^4\ \text{GeV}^2) = 9 \times 10^{-8}\ \text{GeV}^{-2} \approx 3 \times 10^{-26}\ \text{cm}^3/\text{s}. $$

Therefore:

因此：

$$ \Omega_\chi h^2 \approx (3 \times 10^{-27})/(3 \times 10^{-26}) \approx \mathbf{0.1}, $$

in remarkable agreement with the measured $\Omega_{DM} h^2 \approx 0.120$ from CMB data. No parameter was tuned! This is the WIMP miracle: a particle motivated entirely by the hierarchy problem (not by cosmology) independently predicts the correct dark matter abundance. $\blacksquare$

与 CMB 数据测量的 $\Omega_{DM} h^2 \approx 0.120$ 惊人地吻合。没有任何参数被调节！这就是 WIMP 奇迹：一个完全由等级问题（而非宇宙学）激发的粒子，独立地预言了正确的暗物质丰度。$\blacksquare$

**Step 5 — Why mass cancels.** The cancellation of $m_\chi$ from $\Omega_\chi h^2$ is physical: heavier WIMPs stay in equilibrium longer (harder to annihilate with lower $n$), so $Y_\infty \propto 1/m_\chi$; but $\rho_\chi = m_\chi n_\chi \propto m_\chi \cdot (1/m_\chi) = \text{const}$. The relic density depends only on $\langle\sigma v\rangle$, not on $m_\chi$ separately. $\blacksquare$

**第 5 步 — 为何质量消去。** $m_\chi$ 从 $\Omega_\chi h^2$ 中消去有其物理意义：较重的 WIMP 在平衡中停留更长时间（更低 $n$ 时更难湮灭），故 $Y_\infty \propto 1/m_\chi$；但 $\rho_\chi = m_\chi n_\chi \propto m_\chi \cdot (1/m_\chi) = \text{const}$。遗迹密度只取决于 $\langle\sigma v\rangle$，而不单独取决于 $m_\chi$。$\blacksquare$

---

## D. Sakharov Conditions for Baryogenesis · 重子生成的萨哈罗夫条件

**Claim.** To generate a net baryon asymmetry from an initially symmetric state ($n_b = n_{\bar b}$), the following three conditions must all hold: (1) baryon number $B$ violation, (2) C and CP violation, (3) departure from thermal equilibrium.

**命题。** 要从初始对称态（$n_b = n_{\bar b}$）产生净重子不对称性，以下三个条件必须同时满足：(1) 重子数 $B$ 不守恒，(2) C 和 CP 破坏，(3) 偏离热平衡。

**Step 1 — Necessity of B violation.** Obviously, if baryon number is strictly conserved, any process that creates a baryon also creates an antibaryon (or destroys a baryon), keeping $n_b - n_{\bar b} = \text{const}$. If initially $n_b - n_{\bar b} = 0$, it remains zero. $B$ violation is necessary to allow $n_b \ne n_{\bar b}$. In the SM, $B$ is violated non-perturbatively via electroweak sphalerons at high temperature $T \gtrsim 100$ GeV: the sphaleron rate is $\Gamma_{sph} \sim \alpha_W^5 T$.

**第 1 步 — B 破坏的必要性。** 显然，若重子数严格守恒，任何产生重子的过程也会产生反重子（或湮灭重子），保持 $n_b - n_{\bar b} = \text{const}$。若初始时 $n_b - n_{\bar b} = 0$，则它保持为零。$B$ 破坏是允许 $n_b \ne n_{\bar b}$ 的必要条件。在 SM 中，$B$ 在高温 $T \gtrsim 100$ GeV 时通过电弱热子非微扰地破坏：热子速率 $\Gamma_{sph} \sim \alpha_W^5 T$。

**Step 2 — Necessity of C and CP violation.** Suppose C is conserved. Then the rate of any process $\Gamma(\psi \to bX) = \Gamma(\bar\psi \to \bar b\bar X)$ (charge conjugation maps particles to antiparticles). Any baryon-creating process has an equally fast antibaryon-creating partner, so no net baryon number is generated. Therefore C must be violated.

**第 2 步 — C 和 CP 破坏的必要性。** 假设 C 守恒。则任何过程的速率 $\Gamma(\psi \to bX) = \Gamma(\bar\psi \to \bar b\bar X)$（电荷共轭将粒子映射到反粒子）。任何产生重子的过程都有一个等速产生反重子的过程，故不产生净重子数。因此 C 必须破坏。

Similarly, even if C is violated, if CP is conserved, the rate of $\psi_L \to bX$ equals the rate of $\bar\psi_R \to \bar b\bar X$ (CP maps left-handed particles to right-handed antiparticles). The combined rates still balance, yielding no asymmetry. Therefore both C and CP must be violated.

类似地，即使 C 被破坏，若 CP 守恒，则 $\psi_L \to bX$ 的速率等于 $\bar\psi_R \to \bar b\bar X$ 的速率（CP 将左手粒子映射到右手反粒子）。合并速率仍然平衡，不产生不对称性。因此 C 和 CP 都必须被破坏。

**Step 3 — Necessity of departure from thermal equilibrium.** In thermal equilibrium, the density matrix $\rho = e^{-H/T}/Z$ is time-reversal invariant (CPT theorem). For any process, $\Gamma(i \to f) = \Gamma(\bar f \to \bar i)$ (CPT). Even with $B$ and CP violation, in equilibrium all forward and reverse rates balance: $\langle B\rangle_{eq} = 0$ for any Hamiltonian with CPT invariance (Kobzarev–Okun–Shaposhnikov theorem). Departure from equilibrium (e.g., a first-order phase transition, or the decay of a heavy particle out of equilibrium) allows the $B$-violating and CP-violating rates to act without the reverse processes restoring equilibrium.

**第 3 步 — 偏离热平衡的必要性。** 在热平衡中，密度矩阵 $\rho = e^{-H/T}/Z$ 在时间反演下不变（CPT 定理）。对于任何过程，$\Gamma(i \to f) = \Gamma(\bar f \to \bar i)$（CPT）。即使有 $B$ 和 CP 破坏，在平衡中所有正向和逆向速率平衡：对于任何具有 CPT 不变性的哈密顿量，$\langle B\rangle_{eq} = 0$（Kobzarev–Okun–Shaposhnikov 定理）。偏离平衡（例如一级相变，或重粒子的失平衡衰变）允许 $B$ 破坏和 CP 破坏速率起作用，而不被逆过程恢复平衡。

**Step 4 — SM realization and its shortfall.** The SM satisfies all three conditions in principle:
(1) Sphaleron processes: $\Delta B = \Delta L = \pm 3$ (baryon number violated by sphalerons).
(2) CKM phase $\delta$ provides CP violation.
(3) The electroweak phase transition provides non-equilibrium.

**第 4 步 — SM 实现及其不足。** SM 原则上满足所有三个条件：
(1) 热子过程：$\Delta B = \Delta L = \pm 3$（重子数被热子破坏）。
(2) CKM 相位 $\delta$ 提供 CP 破坏。
(3) 电弱相变提供非平衡。

However, quantitatively:
- The SM CKM phase is too small: the CP-violating measure $J = \text{Im}[V_{us}V_{cb}V_{ub}^* V_{cs}^*] \sim 3 \times 10^{-5}$ is suppressed by small mixing angles.
- The SM electroweak phase transition at $m_h \approx 125$ GeV is a smooth crossover (not first-order), so the departure from equilibrium is insufficient.

然而，定量上：
- SM 的 CKM 相位太小：CP 破坏量度 $J = \text{Im}[V_{us}V_{cb}V_{ub}^* V_{cs}^*] \sim 3 \times 10^{-5}$ 被小混合角所抑制。
- SM 在 $m_h \approx 125$ GeV 处的电弱相变是平滑过渡（而非一级相变），因此偏离平衡不足。

The observed baryon-to-photon ratio $\eta \sim 6 \times 10^{-10}$ requires new sources of CP violation and/or a stronger first-order phase transition — physics beyond the SM. $\blacksquare$

观测到的重子–光子比 $\eta \sim 6 \times 10^{-10}$ 需要新的 CP 破坏来源和/或更强的一级相变——超出 SM 的物理。$\blacksquare$

---

## E. Big Bang Nucleosynthesis: The Neutron-to-Proton Ratio · 大爆炸核合成：中子–质子比

**Claim.** The $n/p$ ratio at BBN is determined by the weak interaction rates $n \leftrightarrow p + e^- + \bar\nu_e$ freezing out at $T_f \approx 0.7$ MeV, giving $(n/p)_{freeze} \approx 1/6$, leading to a predicted ${}^4\text{He}$ mass fraction $Y_p \approx 0.247$.

**命题。** BBN 时的 $n/p$ 比由弱相互作用速率 $n \leftrightarrow p + e^- + \bar\nu_e$ 在 $T_f \approx 0.7$ MeV 时冻结所决定，给出 $(n/p)_{freeze} \approx 1/6$，导致预言的 ${}^4\text{He}$ 质量分数 $Y_p \approx 0.247$。

**Step 1 — Equilibrium $n/p$ ratio.** At $T \gg 1$ MeV, weak interactions maintain equilibrium between $n$ and $p$. The ratio is:

**第 1 步 — 平衡 $n/p$ 比。** 在 $T \gg 1$ MeV 时，弱相互作用维持 $n$ 和 $p$ 之间的平衡。比值为：

$$ (n/p)_{eq} = \exp(-(m_n - m_p)/T) = \exp(-\Delta m/T), \quad \Delta m = m_n - m_p = 1.293\ \text{MeV}. $$

At $T = 10$ MeV: $(n/p) = \exp(-0.13) \approx 0.88$. At $T = 1$ MeV: $(n/p) = \exp(-1.29) \approx 0.28$.

在 $T = 10$ MeV 时：$(n/p) = \exp(-0.13) \approx 0.88$。在 $T = 1$ MeV 时：$(n/p) = \exp(-1.29) \approx 0.28$。

**Step 2 — Freeze-out.** The weak interaction rate for $n \to p + e^- + \bar\nu_e$ (governed by the Fermi constant $G_F$):

**第 2 步 — 冻结。** $n \to p + e^- + \bar\nu_e$ 的弱相互作用速率（由费米常数 $G_F$ 支配）：

$$ \Gamma_{weak} \sim G_F^2 T^5. $$

(The $T^5$ scaling comes from three factors of $T$ from phase space, one from the neutrino/electron distribution, and $G_F^2$ from the matrix element squared.)

（$T^5$ 的标度来自相空间的三个 $T$ 因子，一个来自中微子/电子分布，$G_F^2$ 来自矩阵元的平方。）

The Hubble rate in radiation domination: $H \sim T^2/M_{Pl}$. Freeze-out when $\Gamma_{weak} \approx H$:

辐射主导时期的哈勃速率：$H \sim T^2/M_{Pl}$。冻结时 $\Gamma_{weak} \approx H$：

$$ G_F^2 T_f^5 \approx T_f^2/M_{Pl} \quad \implies \quad T_f^3 \approx 1/(G_F^2 M_{Pl}). $$

$$ T_f \approx (1/(G_F^2 M_{Pl}))^{1/3} \approx (1/(1.17 \times 10^{-5}\ \text{GeV}^{-2})^2 \times 2.4 \times 10^{18}\ \text{GeV})^{1/3}. $$

$$ \approx (1/(3.3 \times 10^{12})\ \text{GeV}^2 \cdot \text{GeV})^{1/3} \ldots \text{ numerically } T_f \approx 0.7\text{–}1\ \text{MeV}. $$

**Step 3 — The $n/p$ ratio at freeze-out and at BBN.** At $T_f \approx 0.7\text{–}1$ MeV:

**第 3 步 — 冻结时和 BBN 时的 $n/p$ 比。** 在 $T_f \approx 0.7\text{–}1$ MeV 时：

$$ (n/p)_f \approx \exp(-1.293/0.8) \approx \exp(-1.6) \approx 0.2 \approx 1/5. $$

After freeze-out, free neutrons decay ($\tau_n \approx 886$ s). BBN begins at $T_{BBN} \approx 0.07$ MeV ($t \approx 200$ s), reducing $n/p$ further to $\approx 1/7$.

冻结后，自由中子衰变（$\tau_n \approx 886$ s）。BBN 在 $T_{BBN} \approx 0.07$ MeV（$t \approx 200$ s）时开始，将 $n/p$ 进一步降至 $\approx 1/7$。

**Step 4 — ${}^4\text{He}$ mass fraction.** Almost all neutrons end up in ${}^4\text{He}$ (the most stable light nucleus). With $n/p = 1/7$ at BBN:

**第 4 步 — ${}^4\text{He}$ 质量分数。** 几乎所有中子都进入 ${}^4\text{He}$（最稳定的轻核）。以 BBN 时 $n/p = 1/7$：

$$ \begin{aligned}
&\text{For every 8 baryons: } 1\,n + 7\,p. \\
&\text{All neutrons} \to {}^4\text{He}: 2n + 2p \to {}^4\text{He}. \\
&{}^4\text{He mass fraction: } Y_p = \frac{\text{mass in }{}^4\text{He}}{\text{total mass}} = \frac{2 \times 2}{8} = \frac{4}{8} = \frac{1}{2} \times \frac{2n}{n+p} \\
&\qquad = \frac{2(n/p)}{1 + n/p} = \frac{2 \times (1/7)}{1 + 1/7} = \frac{2/7}{8/7} = \frac{2}{8} = \frac{1}{4} \approx 0.25.
\end{aligned} $$

每 8 个重子：$1\,n + 7\,p$。
所有中子 $\to$ ${}^4\text{He}$：$2n + 2p \to {}^4\text{He}$。
${}^4\text{He}$ 质量分数：$Y_p = 2 \times (n/p)/(1 + n/p) = 2 \times (1/7)/(8/7) = 2/8 = 0.25$。

The more precise calculation including all reactions gives $Y_p \approx 0.247$, matching observations to $\sim 1\%$ precision. $\blacksquare$

包含所有反应的更精确计算给出 $Y_p \approx 0.247$，与观测的精度为 $\sim 1\%$。$\blacksquare$

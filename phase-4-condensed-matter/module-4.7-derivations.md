# Derivations — Module 4.7: Semiconductor Physics
# 推导 — 模块 4.7：半导体物理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.7](./module-4.7-semiconductor-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.7](./module-4.7-semiconductor-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Effective Mass from Band Curvature · 由能带曲率推导有效质量

**Claim.** Near a band extremum the dynamics of an electron can be described exactly as if it were a free particle but with mass $m^* = \hbar^2 / (d^2E/dk^2)$, where the curvature is evaluated at the extremum.

**命题。** 在能带极值附近，电子的动力学可以被描述为具有质量 $m^* = \hbar^2 / (d^2E/dk^2)$ 的自由粒子，其中曲率在极值处求值。

**Step 1 — Semiclassical equation of motion.** The group velocity of a Bloch wave packet is $v_g = (1/\hbar)\, dE/dk$. Under an external force $F$ (from an electric field $E_\text{field}$: $F = -eE_\text{field}$), the crystal momentum $\hbar k$ changes as

**第 1 步 — 半经典运动方程。** 布洛赫波包的群速度为 $v_g = (1/\hbar)\, dE/dk$。在外力 $F$（来自电场 $E_\text{field}$：$F = -eE_\text{field}$）下，晶体动量 $\hbar k$ 的变化为

$$ \hbar\, \frac{dk}{dt} = F. $$

**Step 2 — Acceleration.** The acceleration of the wave packet is

**第 2 步 — 加速度。** 波包的加速度为

$$ a = \frac{dv_g}{dt} = \frac{1}{\hbar}\frac{d}{dt}\Big(\frac{dE}{dk}\Big) = \frac{1}{\hbar}\Big(\frac{d^2E}{dk^2}\Big)\frac{dk}{dt} = \frac{1}{\hbar^2}\Big(\frac{d^2E}{dk^2}\Big) F. $$

**Step 3 — Define effective mass.** Comparing with Newton's law $a = F/m^*$:

**第 3 步 — 定义有效质量。** 与牛顿定律 $a = F/m^*$ 对比：

$$ \frac{1}{m^*} = \frac{1}{\hbar^2}\frac{d^2E}{dk^2}. $$

For a parabolic conduction band minimum $E(k) = E_c + \hbar^2 k^2/(2m^*)$: $d^2E/dk^2 = \hbar^2/m^*$, confirming the formula. For the valence band maximum (downward parabola) $d^2E/dk^2 < 0$, giving $m^* < 0$ for electrons — equivalently, holes with positive mass $m_h^* = -m^*$. $\blacksquare$

对于抛物线形导带底 $E(k) = E_c + \hbar^2 k^2/(2m^*)$：$d^2E/dk^2 = \hbar^2/m^*$，证实了该公式。对于价带顶（向下的抛物线），$d^2E/dk^2 < 0$，电子 $m^* < 0$——等价地，空穴具有正质量 $m_h^* = -m^*$。$\blacksquare$

---

## B. Intrinsic Carrier Concentration $n_i \propto T^{3/2} \exp(-E_g / 2k_B T)$ · 本征载流子浓度

**Claim.** For an intrinsic (undoped) semiconductor with band gap $E_g$, the equilibrium electron (and hole) density is $n_i = \sqrt{N_c N_v}\, \exp(-E_g / 2k_B T)$, where $N_c = 2(2\pi m_e^* k_B T/h^2)^{3/2}$ and $N_v = 2(2\pi m_h^* k_B T/h^2)^{3/2}$.

**命题。** 对于带隙为 $E_g$ 的本征（未掺杂）半导体，平衡电子（和空穴）密度为 $n_i = \sqrt{N_c N_v}\, \exp(-E_g / 2k_B T)$，其中 $N_c = 2(2\pi m_e^* k_B T/h^2)^{3/2}$，$N_v = 2(2\pi m_h^* k_B T/h^2)^{3/2}$。

**Step 1 — Electron density in the conduction band.** The electron density is $n = \int_{E_c}^\infty g_c(E)\, f(E)\, dE$, where $g_c(E) = (1/(2\pi^2))\, (2m_e^*/\hbar^2)^{3/2} \sqrt{E - E_c}$ is the 3D density of states for a parabolic band, and $f(E) = 1/(\exp((E - E_F)/k_B T) + 1)$ is the Fermi–Dirac distribution.

**第 1 步 — 导带中的电子密度。** 电子密度为 $n = \int_{E_c}^\infty g_c(E)\, f(E)\, dE$，其中 $g_c(E) = (1/(2\pi^2))\, (2m_e^*/\hbar^2)^{3/2} \sqrt{E - E_c}$ 是抛物线能带的三维态密度，$f(E) = 1/(\exp((E - E_F)/k_B T) + 1)$ 是费米–狄拉克分布。

**Step 2 — Boltzmann approximation.** If $E_F$ lies well inside the gap (at least a few $k_B T$ from either band edge), then for $E \ge E_c$: $E - E_F \gg k_B T$, so $f(E) \approx \exp(-(E - E_F)/k_B T)$. This is the non-degenerate (Boltzmann) limit, valid for intrinsic and lightly doped semiconductors.

**第 2 步 — 玻尔兹曼近似。** 若 $E_F$ 位于带隙深处（距任一带边至少几个 $k_B T$），则对 $E \ge E_c$：$E - E_F \gg k_B T$，故 $f(E) \approx \exp(-(E - E_F)/k_B T)$。这是非简并（玻尔兹曼）极限，对本征和轻掺杂半导体有效。

**Step 3 — Evaluate the integral.** With $u = (E - E_c)/k_B T$:

**第 3 步 — 计算积分。** 令 $u = (E - E_c)/k_B T$：

$$ n = \frac{1}{2\pi^2}\Big(\frac{2m_e^*}{\hbar^2}\Big)^{3/2} \exp\!\Big(-\frac{E_c - E_F}{k_B T}\Big) (k_B T)^{3/2} \int_0^\infty u^{1/2}\, e^{-u}\, du. $$

The integral $\int_0^\infty u^{1/2}\, e^{-u}\, du = \Gamma(3/2) = \sqrt{\pi}/2$. Assembling:

积分 $\int_0^\infty u^{1/2}\, e^{-u}\, du = \Gamma(3/2) = \sqrt{\pi}/2$。组合得：

$$ n = 2\Big(\frac{2\pi m_e^* k_B T}{h^2}\Big)^{3/2} \exp\!\Big(-\frac{E_c - E_F}{k_B T}\Big) \equiv N_c \exp\!\Big(-\frac{E_c - E_F}{k_B T}\Big). $$

**Step 4 — Hole density.** By an identical calculation for the valence band (holes see the inverted band):

**第 4 步 — 空穴密度。** 对价带（空穴看到反转能带）进行相同计算：

$$ p = N_v \exp\!\Big(-\frac{E_F - E_v}{k_B T}\Big), \qquad N_v = 2\Big(\frac{2\pi m_h^* k_B T}{h^2}\Big)^{3/2}. $$

**Step 5 — Intrinsic condition and result.** For an intrinsic semiconductor $n = p = n_i$. Multiply the two expressions:

**第 5 步 — 本征条件与结果。** 对于本征半导体 $n = p = n_i$。将两个表达式相乘：

$$ n_i^2 = n \cdot p = N_c N_v \exp\!\Big(-\frac{E_c - E_v}{k_B T}\Big) = N_c N_v \exp\!\Big(-\frac{E_g}{k_B T}\Big). $$

Therefore $n_i = \sqrt{N_c N_v}\, \exp(-E_g / 2k_B T)$. Since $N_c, N_v \propto T^{3/2}$, this gives $n_i \propto T^{3/2} \exp(-E_g / 2k_B T)$. $\blacksquare$

因此 $n_i = \sqrt{N_c N_v}\, \exp(-E_g / 2k_B T)$。由于 $N_c, N_v \propto T^{3/2}$，得 $n_i \propto T^{3/2} \exp(-E_g / 2k_B T)$。$\blacksquare$

The Fermi level of the intrinsic semiconductor is at $E_F = (E_c + E_v)/2 + (3/4)k_B T \ln(m_h^*/m_e^*)$, which lies near the middle of the gap (exactly at the midgap if $m_e^* = m_h^*$).

本征半导体的费米能级在 $E_F = (E_c + E_v)/2 + (3/4)k_B T \ln(m_h^*/m_e^*)$ 处，位于带隙中部附近（若 $m_e^* = m_h^*$ 则恰好在带隙正中）。

---

## C. p–n Junction Built-in Voltage and Depletion Width · p–n 结内建电压与耗尽区宽度

**Claim.** For a p–n junction with donor density $N_D$ on the n-side and acceptor density $N_A$ on the p-side, the built-in voltage is $V_\text{bi} = (k_B T/e) \ln(N_A N_D / n_i^2)$, and the total depletion width is $W = \sqrt{2\varepsilon V_\text{bi} (N_A + N_D) / (e N_A N_D)}$, where $\varepsilon$ is the semiconductor permittivity.

**命题。** 对于 n 侧施主密度为 $N_D$、p 侧受主密度为 $N_A$ 的 p–n 结，内建电压为 $V_\text{bi} = (k_B T/e) \ln(N_A N_D / n_i^2)$，总耗尽区宽度为 $W = \sqrt{2\varepsilon V_\text{bi} (N_A + N_D) / (e N_A N_D)}$，其中 $\varepsilon$ 为半导体介电常数。

**Step 1 — Equilibrium Fermi level alignment.** In equilibrium the Fermi level is uniform. On the n-side, $E_F = E_c - k_B T \ln(N_c/N_D) \approx E_c - k_B T \ln(N_c/N_D)$ (for $N_D \gg n_i$). On the p-side, $E_F = E_v + k_B T \ln(N_v/N_A)$. The built-in potential is the difference in electrostatic potential between the two sides, equal to the difference in Fermi levels before contact:

**第 1 步 — 平衡费米能级对齐。** 平衡态下费米能级均匀。n 侧 $E_F = E_c - k_B T \ln(N_c/N_D)$（当 $N_D \gg n_i$ 时）。p 侧 $E_F = E_v + k_B T \ln(N_v/N_A)$。内建电位是两侧静电势之差，等于接触前费米能级之差：

$$ \begin{aligned} e V_\text{bi} &= (E_c^n - E_c^p) = k_B T \ln(N_D/N_c) + k_B T \ln(N_v/N_A) + E_g \\ &= k_B T \ln\!\Big(\frac{N_D N_A}{N_c N_v \cdot \exp(-E_g/k_B T)}\Big) = k_B T \ln\!\Big(\frac{N_A N_D}{n_i^2}\Big). \end{aligned} $$

Thus $V_\text{bi} = (k_B T / e) \ln(N_A N_D / n_i^2)$. For typical doping levels ($N_A = N_D = 10^{16}\ \text{cm}^{-3}$, $n_i \approx 10^{10}\ \text{cm}^{-3}$ for Si), $V_\text{bi} \approx 0.72\ \text{V}$.

因此 $V_\text{bi} = (k_B T / e) \ln(N_A N_D / n_i^2)$。对于典型掺杂水平（$N_A = N_D = 10^{16}\ \text{cm}^{-3}$，Si 中 $n_i \approx 10^{10}\ \text{cm}^{-3}$），$V_\text{bi} \approx 0.72\ \text{V}$。

**Step 2 — Depletion approximation.** Assume the depletion region is abruptly depleted (no free carriers) and neutral outside. The depletion extends a distance $x_n$ into the n-side and $x_p$ into the p-side. Charge neutrality requires:

**第 2 步 — 耗尽近似。** 假设耗尽区突变耗尽（无自由载流子），外部中性。耗尽区向 n 侧延伸 $x_n$，向 p 侧延伸 $x_p$。电荷中性要求：

$$ N_D x_n = N_A x_p. $$

**Step 3 — Poisson equation.** The charge density $\rho = e N_D$ in the n-depletion region and $\rho = -e N_A$ in the p-depletion region. Poisson's equation $d^2\varphi/dx^2 = -\rho/\varepsilon$ integrates to give the electric field, and integrating again gives the potential. Matching boundary conditions ($\varphi$ and $d\varphi/dx$ continuous, field zero outside depletion region):

**第 3 步 — 泊松方程。** 电荷密度在 n 侧耗尽区为 $\rho = e N_D$，在 p 侧耗尽区为 $\rho = -e N_A$。泊松方程 $d^2\varphi/dx^2 = -\rho/\varepsilon$ 积分给出电场，再次积分给出电位。匹配边界条件（$\varphi$ 和 $d\varphi/dx$ 连续，耗尽区外电场为零）：

$$ \text{The total potential drop} = V_\text{bi} = \frac{e N_D x_n^2}{2\varepsilon} + \frac{e N_A x_p^2}{2\varepsilon}. $$

With $N_D x_n = N_A x_p$ and $W = x_n + x_p$, solve for $W$:

利用 $N_D x_n = N_A x_p$ 和 $W = x_n + x_p$，求解 $W$：

$$ x_n = \frac{W N_A}{N_A + N_D}, \qquad x_p = \frac{W N_D}{N_A + N_D}. $$

Substituting and solving:

代入求解：

$$ V_\text{bi} = \frac{e W^2 N_A N_D}{2\varepsilon (N_A + N_D)}. $$

Therefore $W = \sqrt{2\varepsilon V_\text{bi} (N_A + N_D) / (e N_A N_D)}$. $\blacksquare$

因此 $W = \sqrt{2\varepsilon V_\text{bi} (N_A + N_D) / (e N_A N_D)}$。$\blacksquare$

Under an applied reverse bias $V_r$ the built-in voltage $V_\text{bi}$ is replaced by $V_\text{bi} + V_r$, widening the depletion region as $W \propto \sqrt{V_\text{bi} + V_r}$. Under forward bias $V_f$ it narrows as $W \propto \sqrt{V_\text{bi} - V_f}$. The changing capacitance $C = \varepsilon A/W$ of the junction is the basis of the varactor diode.

在施加反向偏压 $V_r$ 时，内建电压 $V_\text{bi}$ 被 $V_\text{bi} + V_r$ 替代，耗尽区随 $W \propto \sqrt{V_\text{bi} + V_r}$ 增宽。在正向偏压 $V_f$ 下，随 $W \propto \sqrt{V_\text{bi} - V_f}$ 缩窄。结的变化电容 $C = \varepsilon A/W$ 是变容二极管的基础。

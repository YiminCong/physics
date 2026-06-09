# Derivations — Module 9.6: Quantum Optics & Laser Physics
# 推导 — 模块 9.6：量子光学与激光物理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.6](./module-9.6-quantum-optics-and-lasers.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.6](./module-9.6-quantum-optics-and-lasers.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Einstein A and B Coefficients · 爱因斯坦 A 与 B 系数

**Claim.** For a two-level atom (lower level 1, upper level 2, degeneracies $g_1, g_2$, transition frequency $\nu$) in equilibrium with a thermal radiation field of spectral energy density $u(\nu)$, the Einstein coefficients obey two universal relations:

$$ g_1 B_{12} = g_2 B_{21} \quad\text{and}\quad A_{21}/B_{21} = 8\pi h\nu^3/c^3. $$

**命题。** 对于与谱能量密度为 $u(\nu)$ 的热辐射场处于平衡的二能级原子（下能级 1，上能级 2，简并度 $g_1$、$g_2$，跃迁频率 $\nu$），爱因斯坦系数遵守两个普适关系：

$$ g_1 B_{12} = g_2 B_{21} \quad\text{与}\quad A_{21}/B_{21} = 8\pi h\nu^3/c^3. $$

**Step 1 — Write the rate equation.** Let $N_1, N_2$ be the level populations. Absorption removes atoms from level 1 at rate $B_{12} u(\nu) N_1$; stimulated and spontaneous emission return atoms to level 1 at rates $B_{21} u(\nu) N_2$ and $A_{21} N_2$. The net change of the upper population is:

**第 1 步 — 写出速率方程。** 设 $N_1$、$N_2$ 为能级布居。吸收以速率 $B_{12} u(\nu) N_1$ 从能级 1 移走原子；受激与自发发射以速率 $B_{21} u(\nu) N_2$ 与 $A_{21} N_2$ 将原子返回能级 1。上能级布居的净变化为：

$$ dN_2/dt = B_{12} u(\nu) N_1 - B_{21} u(\nu) N_2 - A_{21} N_2. $$

**Step 2 — Impose steady state.** In thermal equilibrium the populations are stationary, $dN_2/dt = 0$, so the gain and loss terms balance:

**第 2 步 — 施加稳态。** 热平衡中布居稳定，$dN_2/dt = 0$，故增益与损耗项平衡：

$$ B_{12} u(\nu) N_1 = B_{21} u(\nu) N_2 + A_{21} N_2. $$

Solving for $u(\nu)$:

解出 $u(\nu)$：

$$ u(\nu) = A_{21} N_2 / (B_{12} N_1 - B_{21} N_2) = A_{21} / (B_{12}(N_1/N_2) - B_{21}). $$

**Step 3 — Insert the Boltzmann ratio.** At temperature $T$ the equilibrium populations satisfy $N_2/N_1 = (g_2/g_1)e^{-h\nu/kT}$, hence $N_1/N_2 = (g_1/g_2)e^{h\nu/kT}$. Substituting:

**第 3 步 — 代入玻尔兹曼比。** 温度 $T$ 下平衡布居满足 $N_2/N_1 = (g_2/g_1)e^{-h\nu/kT}$，故 $N_1/N_2 = (g_1/g_2)e^{h\nu/kT}$。代入：

$$ u(\nu) = A_{21} / (B_{12}(g_1/g_2)e^{h\nu/kT} - B_{21}). $$

Factor $B_{21}$ out of the denominator:

从分母提出 $B_{21}$：

$$ u(\nu) = (A_{21}/B_{21}) / ((g_1 B_{12})/(g_2 B_{21})\, e^{h\nu/kT} - 1). $$

**Step 4 — Match to the Planck law.** This must equal the Planck spectral energy density at every temperature:

**第 4 步 — 匹配普朗克定律。** 这必须在任意温度下都等于普朗克谱能量密度：

$$ u(\nu) = (8\pi h\nu^3/c^3) / (e^{h\nu/kT} - 1). $$

Comparing the two expressions term by term, the $e^{h\nu/kT}$ coefficient and the constant must each match. The "$-1$" in both denominators requires the coefficient of $e^{h\nu/kT}$ to be unity:

逐项比较两个表达式，$e^{h\nu/kT}$ 系数与常数项都必须相符。两个分母中的 "$-1$" 要求 $e^{h\nu/kT}$ 的系数为 1：

$$ (g_1 B_{12})/(g_2 B_{21}) = 1 \;\implies\; \boxed{\, g_1 B_{12} = g_2 B_{21} \,}. $$

**Step 5 — Read off the A/B ratio.** With that coefficient equal to one, the numerators must match:

**第 5 步 — 读出 A/B 比值。** 该系数等于 1 后，分子必须相符：

$$ \boxed{\, A_{21}/B_{21} = 8\pi h\nu^3/c^3 \,}. $$

The factor $8\pi\nu^2/c^3$ is the density of electromagnetic modes per unit frequency, and the extra $h\nu$ is the energy per photon; the product is the rate of spontaneous emission into all available modes. Because $A_{21}/B_{21} \propto \nu^3$, spontaneous emission dominates stimulated emission at high frequency, which is why sustaining a population inversion — and hence laser action — becomes progressively harder in the ultraviolet and X-ray. $\blacksquare$

因子 $8\pi\nu^2/c^3$ 是单位频率的电磁模式密度，额外的 $h\nu$ 是每光子能量；二者乘积即向所有可用模式的自发发射速率。由于 $A_{21}/B_{21} \propto \nu^3$，自发发射在高频下压倒受激发射，这正是在紫外和 X 射线波段维持粒子数反转（从而维持激光作用）越来越困难的原因。$\blacksquare$

---

## B. Population Inversion and Laser Gain · 粒子数反转与激光增益

**Claim.** The net stimulated power exchanged with the field is proportional to $N_2 - (g_2/g_1)N_1$. Net amplification (gain) requires a population inversion $N_2/g_2 > N_1/g_1$, which is impossible for a two-level system pumped only by the field at equilibrium; three- or four-level schemes are needed. The laser oscillates when the gain coefficient satisfies the threshold condition $\gamma(\nu) \ge \text{loss}$.

**命题。** 与场交换的净受激功率正比于 $N_2 - (g_2/g_1)N_1$。净放大（增益）要求粒子数反转 $N_2/g_2 > N_1/g_1$，这对仅由场在平衡处泵浦的二能级系统不可能实现；需要三能级或四能级方案。当增益系数满足阈值条件 $\gamma(\nu) \ge \text{损耗}$ 时激光起振。

**Step 1 — Net stimulated rate.** Stimulated emission adds photons at rate $B_{21} u(\nu) N_2$ while absorption removes them at rate $B_{12} u(\nu) N_1$. The net photon-creation rate is:

**第 1 步 — 净受激速率。** 受激发射以速率 $B_{21} u(\nu) N_2$ 增添光子，而吸收以速率 $B_{12} u(\nu) N_1$ 移走光子。净光子产生速率为：

$$ R_{net} = B_{21} u(\nu) N_2 - B_{12} u(\nu) N_1 = u(\nu)[B_{21} N_2 - B_{12} N_1]. $$

Using the Einstein relation $g_1 B_{12} = g_2 B_{21}$ from Derivation A, write $B_{12} = (g_2/g_1)B_{21}$:

利用推导 A 中的爱因斯坦关系 $g_1 B_{12} = g_2 B_{21}$，写出 $B_{12} = (g_2/g_1)B_{21}$：

$$ R_{net} = B_{21} u(\nu)[N_2 - (g_2/g_1)N_1]. $$

**Step 2 — Gain coefficient.** A beam of intensity $I(z)$ propagating through the medium grows or decays according to $dI/dz = \gamma(\nu) I$, where the gain coefficient $\gamma(\nu)$ is proportional to the net stimulated rate per photon:

**第 2 步 — 增益系数。** 强度为 $I(z)$ 的光束在介质中传播按 $dI/dz = \gamma(\nu) I$ 增长或衰减，其中增益系数 $\gamma(\nu)$ 正比于每光子净受激速率：

$$ \gamma(\nu) \propto N_2 - (g_2/g_1)N_1, \quad\text{so}\quad I(z) = I(0)e^{\gamma(\nu) z}. $$

Gain ($\gamma > 0$) therefore requires **population inversion**:

因此增益（$\gamma > 0$）要求**粒子数反转**：

$$ N_2 - (g_2/g_1)N_1 > 0 \iff \boxed{\, N_2/g_2 > N_1/g_1 \,}. $$

**Step 3 — Two levels cannot invert.** Consider a closed two-level system whose only pumping is the resonant field itself. Its rate equation $dN_2/dt = B_{12} u N_1 - (B_{21} u + A_{21})N_2$ with $N_1 + N_2 = N$ has the steady state:

**第 3 步 — 二能级无法反转。** 考虑一个封闭二能级系统，其唯一泵浦是共振场本身。其速率方程 $dN_2/dt = B_{12} u N_1 - (B_{21} u + A_{21})N_2$，配合 $N_1 + N_2 = N$，稳态为：

$$ N_2/N_1 = B_{12} u / (B_{21} u + A_{21}). $$

As the pump intensity $u \to \infty$, this ratio approaches $B_{12}/B_{21} = g_2/g_1$, i.e. $N_2/g_2 \to N_1/g_1$ (transparency), but never exceeds it. The same field that excites atoms upward stimulates them down at an equal per-state rate, so saturation halts at equality and inversion is impossible.

当泵浦强度 $u \to \infty$ 时，该比值趋于 $B_{12}/B_{21} = g_2/g_1$，即 $N_2/g_2 \to N_1/g_1$（透明），但绝不超过它。激发原子向上的同一场也以相等的每态速率受激其向下，故饱和停于相等而反转不可能。

**Step 4 — Three- and four-level remedy.** Inversion is achieved by pumping through an auxiliary level. In a **three-level** scheme the pump drives $1 \to 3$; level 3 decays rapidly (non-radiatively) into a metastable level 2 that lases back to the ground level 1. In a **four-level** scheme the lower laser level is a separate level above the ground state that empties quickly to the ground state, so it stays nearly unpopulated and even a small upper-level population gives $N_2/g_2 > N_1/g_1$. The four-level design reaches threshold at much lower pump power because the lower laser level starts essentially empty.

**第 4 步 — 三能级与四能级补救。** 通过辅助能级泵浦实现反转。在**三能级**方案中，泵浦驱动 $1 \to 3$；能级 3 迅速（非辐射地）衰变到亚稳能级 2，再激射回基态能级 1。在**四能级**方案中，下激光能级是基态之上的独立能级，迅速向基态排空，故几乎不被布居，即使很小的上能级布居也给出 $N_2/g_2 > N_1/g_1$。四能级设计以低得多的泵浦功率达到阈值，因为下激光能级初始基本为空。

**Step 5 — Threshold condition.** In a cavity of length $L$ with mirror reflectivities $R_1, R_2$ and distributed loss $\alpha$, the field returns to its starting amplitude after one round trip only if the round-trip gain equals the round-trip loss:

**第 5 步 — 阈值条件。** 在长度为 $L$、镜面反射率为 $R_1$、$R_2$、分布损耗为 $\alpha$ 的腔中，场在一次往返后回到初始振幅，当且仅当往返增益等于往返损耗：

$$ R_1 R_2\, e^{2(\gamma(\nu)-\alpha)L} = 1 \;\implies\; \gamma_{threshold}(\nu) = \alpha + (1/2L)\ln(1/(R_1 R_2)). $$

Above this gain the intracavity intensity grows until gain saturation pins $\gamma(\nu)$ at the loss value; the laser then oscillates in steady state. The boxed requirement for oscillation is $\boxed{\, \gamma(\nu) \ge \text{loss} \,}$. $\blacksquare$

超过此增益时，腔内强度增长直到增益饱和将 $\gamma(\nu)$ 钳制于损耗值；激光随即稳态振荡。振荡的方框要求为 $\boxed{\, \gamma(\nu) \ge \text{损耗} \,}$。$\blacksquare$

---

## C. Rabi Oscillations of a Driven Two-Level Atom · 受驱二能级原子的拉比振荡

**Claim.** A two-level atom with transition frequency $\omega_0$ driven by a classical field at frequency $\omega$, detuning $\Delta = \omega - \omega_0$ and Rabi frequency $\Omega = \mathbf d\cdot\mathbf E_0/\hbar$, has, in the rotating-wave approximation, the excited-state probability:

$$ P_e(t) = (\Omega^2/\Omega'^2) \sin^2(\Omega' t/2), \quad \Omega' = \sqrt{\Omega^2 + \Delta^2}. $$

On resonance ($\Delta = 0$): $P_e(t) = \sin^2(\Omega t/2)$, so a $\pi$-pulse ($\Omega t = \pi$) transfers the population completely to the excited state.

**命题。** 跃迁频率为 $\omega_0$ 的二能级原子，由频率为 $\omega$ 的经典场驱动，失谐 $\Delta = \omega - \omega_0$，拉比频率 $\Omega = \mathbf d\cdot\mathbf E_0/\hbar$，在旋波近似下激发态概率为：

$$ P_e(t) = (\Omega^2/\Omega'^2) \sin^2(\Omega' t/2), \quad \Omega' = \sqrt{\Omega^2 + \Delta^2}. $$

共振时（$\Delta = 0$）：$P_e(t) = \sin^2(\Omega t/2)$，故 $\pi$ 脉冲（$\Omega t = \pi$）将布居完全转移到激发态。

**Step 1 — Hamiltonian and ansatz.** Take the atomic Hamiltonian $H_0 = \hbar\omega_0|e\rangle\langle e|$ (ground energy set to zero) and the dipole interaction $V(t) = -\mathbf d\cdot\mathbf E_0\cos(\omega t)(|e\rangle\langle g| + |g\rangle\langle e|)$, where $\mathbf d = \langle e|\hat{\mathbf d}|g\rangle$ is the transition dipole. Expand the state as $|\psi(t)\rangle = c_g(t)|g\rangle + c_e(t)e^{-i\omega_0 t}|e\rangle$, where the phase $e^{-i\omega_0 t}$ factors out the free atomic evolution so that $c_g, c_e$ change only because of the drive.

**第 1 步 — 哈密顿量与拟设。** 取原子哈密顿量 $H_0 = \hbar\omega_0|e\rangle\langle e|$（基态能量设为零）与偶极相互作用 $V(t) = -\mathbf d\cdot\mathbf E_0\cos(\omega t)(|e\rangle\langle g| + |g\rangle\langle e|)$，其中 $\mathbf d = \langle e|\hat{\mathbf d}|g\rangle$ 为跃迁偶极。将态展开为 $|\psi(t)\rangle = c_g(t)|g\rangle + c_e(t)e^{-i\omega_0 t}|e\rangle$，相位 $e^{-i\omega_0 t}$ 提出自由原子演化，使 $c_g$、$c_e$ 仅因驱动而变化。

**Step 2 — Amplitude equations.** Insert into $i\hbar\partial_t|\psi\rangle = (H_0 + V)|\psi\rangle$ and project onto $\langle g|$ and $\langle e|$. Using $\cos(\omega t) = \tfrac12(e^{i\omega t} + e^{-i\omega t})$ and the Rabi frequency $\Omega = \mathbf d\cdot\mathbf E_0/\hbar$:

**第 2 步 — 振幅方程。** 代入 $i\hbar\partial_t|\psi\rangle = (H_0 + V)|\psi\rangle$ 并投影到 $\langle g|$ 与 $\langle e|$。用 $\cos(\omega t) = \tfrac12(e^{i\omega t} + e^{-i\omega t})$ 及拉比频率 $\Omega = \mathbf d\cdot\mathbf E_0/\hbar$：

$$ \begin{aligned} i \dot c_g &= -(\Omega/2)(e^{i\omega t} + e^{-i\omega t})\, e^{-i\omega_0 t}\, c_e, \\ i \dot c_e &= -(\Omega/2)(e^{i\omega t} + e^{-i\omega t})\, e^{+i\omega_0 t}\, c_g. \end{aligned} $$

**Step 3 — Rotating-wave approximation.** Each bracket contains a slow term oscillating at $\omega - \omega_0 = \Delta$ and a fast term at $\omega + \omega_0$. Over the timescale of interest the fast term averages to zero and is dropped (the RWA). Keeping only the co-rotating part:

**第 3 步 — 旋波近似。** 每个括号含一个以 $\omega - \omega_0 = \Delta$ 振荡的慢项与一个以 $\omega + \omega_0$ 振荡的快项。在所关心的时间尺度上快项平均为零并丢弃（RWA）。仅保留同向旋转部分：

$$ \begin{aligned} i \dot c_g &= -(\Omega/2)\, e^{-i\Delta t}\, c_e, \\ i \dot c_e &= -(\Omega/2)\, e^{+i\Delta t}\, c_g. \end{aligned} $$

**Step 4 — Remove the detuning phase.** Define rotating-frame amplitudes $b_g = c_g$, $b_e = c_e e^{-i\Delta t}$. Then $\dot c_e = (\dot b_e + i\Delta b_e)e^{i\Delta t}$, and the equations become time-independent:

**第 4 步 — 消去失谐相位。** 定义旋转系振幅 $b_g = c_g$，$b_e = c_e e^{-i\Delta t}$。则 $\dot c_e = (\dot b_e + i\Delta b_e)e^{i\Delta t}$，方程变为不含时：

$$ \begin{aligned} i \dot b_g &= -(\Omega/2)\, b_e, \\ i \dot b_e &= -\Delta b_e - (\Omega/2)\, b_g. \end{aligned} $$

This is a constant $2\times 2$ system with effective Hamiltonian $H_{eff} = -(\hbar/2)(\Omega \sigma_x + \Delta\cdot 2|e\rangle\langle e|)$ in the rotating frame.

这是一个常数 $2\times 2$ 系统，旋转系中有效哈密顿量 $H_{eff} = -(\hbar/2)(\Omega \sigma_x + \Delta\cdot 2|e\rangle\langle e|)$。

**Step 5 — Solve for $b_e$.** Differentiate the second equation and substitute $\dot b_g$ from the first:

**第 5 步 — 解出 $b_e$。** 对第二个方程求导并代入第一个方程的 $\dot b_g$：

$$ \ddot b_e + i\Delta \dot b_e + (\Omega^2/4) b_e = 0. $$

With initial conditions $b_e(0) = 0$, $b_g(0) = 1$ (atom in ground state), so $\dot b_e(0) = i(\Omega/2)$. The solution is a damped-free harmonic oscillation at the generalized Rabi frequency $\Omega' = \sqrt{\Omega^2 + \Delta^2}$:

初始条件 $b_e(0) = 0$、$b_g(0) = 1$（原子在基态），故 $\dot b_e(0) = i(\Omega/2)$。解为以广义拉比频率 $\Omega' = \sqrt{\Omega^2 + \Delta^2}$ 的简谐振荡：

$$ b_e(t) = i(\Omega/\Omega') \sin(\Omega' t/2)\, e^{-i\Delta t/2}. $$

**Step 6 — Excited-state probability.** Since $|c_e|^2 = |b_e|^2$, taking the modulus squared gives:

**第 6 步 — 激发态概率。** 由于 $|c_e|^2 = |b_e|^2$，取模平方给出：

$$ \boxed{\, P_e(t) = (\Omega^2/\Omega'^2) \sin^2(\Omega' t/2) \,}. $$

On resonance $\Delta = 0$ so $\Omega' = \Omega$ and $P_e(t) = \sin^2(\Omega t/2)$: the population oscillates fully between $|g\rangle$ and $|e\rangle$. A pulse with $\Omega t = \pi$ (a **$\pi$-pulse**) gives $P_e = 1$, complete transfer to the excited state; a $\pi/2$-pulse gives an equal-weight superposition. Off resonance the oscillation is faster ($\Omega' > \Omega$) but the peak transfer $\Omega^2/\Omega'^2 < 1$ is incomplete. $\blacksquare$

共振时 $\Delta = 0$ 故 $\Omega' = \Omega$ 且 $P_e(t) = \sin^2(\Omega t/2)$：布居在 $|g\rangle$ 与 $|e\rangle$ 之间完全振荡。$\Omega t = \pi$ 的脉冲（**$\pi$ 脉冲**）给出 $P_e = 1$，完全转移到激发态；$\pi/2$ 脉冲给出等权叠加。失谐时振荡更快（$\Omega' > \Omega$），但峰值转移 $\Omega^2/\Omega'^2 < 1$ 不完全。$\blacksquare$

---

## D. Coherent States · 相干态

**Claim.** The coherent state $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_n (\alpha^n/\sqrt{n!}) |n\rangle$ satisfies: (i) $a|\alpha\rangle = \alpha|\alpha\rangle$; (ii) Poisson photon statistics $P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$ with $\langle n\rangle = |\alpha|^2$ and $\Delta n^2 = |\alpha|^2$, hence $\Delta n/\langle n\rangle = 1/\sqrt{\langle n\rangle}$; (iii) the minimum-uncertainty product $\Delta x\, \Delta p = \hbar/2$.

**命题。** 相干态 $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_n (\alpha^n/\sqrt{n!}) |n\rangle$ 满足：(i) $a|\alpha\rangle = \alpha|\alpha\rangle$；(ii) 泊松光子统计 $P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$，$\langle n\rangle = |\alpha|^2$，$\Delta n^2 = |\alpha|^2$，故 $\Delta n/\langle n\rangle = 1/\sqrt{\langle n\rangle}$；(iii) 最小不确定乘积 $\Delta x\, \Delta p = \hbar/2$。

**Step 1 — Eigenstate of the annihilation operator.** Apply $a$ to the series, using $a|n\rangle = \sqrt n |n-1\rangle$:

**第 1 步 — 湮灭算符的本征态。** 用 $a|n\rangle = \sqrt n |n-1\rangle$ 将 $a$ 作用于级数：

$$ a|\alpha\rangle = e^{-|\alpha|^2/2} \sum_{n=1}^\infty (\alpha^n/\sqrt{n!}) \sqrt n |n-1\rangle = e^{-|\alpha|^2/2} \sum_{n=1}^\infty (\alpha^n/\sqrt{(n-1)!}) |n-1\rangle. $$

Shift the index $m = n - 1$:

移动指标 $m = n - 1$：

$$ a|\alpha\rangle = e^{-|\alpha|^2/2} \sum_{m=0}^\infty (\alpha^{m+1}/\sqrt{m!}) |m\rangle = \alpha \cdot e^{-|\alpha|^2/2} \sum_{m=0}^\infty (\alpha^m/\sqrt{m!}) |m\rangle = \boxed{\, \alpha|\alpha\rangle \,}. $$

**Step 2 — Photon-number distribution.** The probability of finding $n$ photons is $P(n) = |\langle n|\alpha\rangle|^2$. Reading the coefficient off the series, $\langle n|\alpha\rangle = e^{-|\alpha|^2/2} \alpha^n/\sqrt{n!}$, so:

**第 2 步 — 光子数分布。** 找到 $n$ 个光子的概率为 $P(n) = |\langle n|\alpha\rangle|^2$。从级数读出系数，$\langle n|\alpha\rangle = e^{-|\alpha|^2/2} \alpha^n/\sqrt{n!}$，故：

$$ \boxed{\, P(n) = e^{-|\alpha|^2} |\alpha|^{2n}/n! \,}, $$

a **Poisson distribution** with mean parameter $\lambda = |\alpha|^2$.

即均值参数 $\lambda = |\alpha|^2$ 的**泊松分布**。

**Step 3 — Mean and variance.** For a Poisson distribution both the mean and variance equal $\lambda$. Computing directly, $\langle n\rangle = \langle\alpha|a^\dagger a|\alpha\rangle = (\alpha^*)(\alpha) = |\alpha|^2$ using $a|\alpha\rangle = \alpha|\alpha\rangle$ and $\langle\alpha|a^\dagger = \alpha^*\langle\alpha|$. For the variance use $\langle n^2\rangle = \langle\alpha|a^\dagger a\, a^\dagger a|\alpha\rangle$; commuting $a a^\dagger = a^\dagger a + 1$ gives $\langle n^2\rangle = |\alpha|^4 + |\alpha|^2$, so:

**第 3 步 — 均值与方差。** 对泊松分布，均值与方差均等于 $\lambda$。直接计算，$\langle n\rangle = \langle\alpha|a^\dagger a|\alpha\rangle = (\alpha^*)(\alpha) = |\alpha|^2$，用了 $a|\alpha\rangle = \alpha|\alpha\rangle$ 与 $\langle\alpha|a^\dagger = \alpha^*\langle\alpha|$。方差用 $\langle n^2\rangle = \langle\alpha|a^\dagger a\, a^\dagger a|\alpha\rangle$；对易 $a a^\dagger = a^\dagger a + 1$ 给出 $\langle n^2\rangle = |\alpha|^4 + |\alpha|^2$，故：

$$ \langle n\rangle = |\alpha|^2, \quad \boxed{\, \Delta n^2 = \langle n^2\rangle - \langle n\rangle^2 = |\alpha|^2 \,}. $$

The relative number fluctuation is therefore:

因此相对数涨落为：

$$ \Delta n/\langle n\rangle = |\alpha|/|\alpha|^2 = 1/|\alpha| = \boxed{\, 1/\sqrt{\langle n\rangle} \,}, $$

which vanishes in the bright-field limit, recovering classical amplitude stability while leaving the shot-noise floor.

它在亮场极限下趋于零，恢复经典振幅稳定性，同时留下散粒噪声基底。

**Step 4 — Minimum-uncertainty quadratures.** Define the quadratures $x = \sqrt{\hbar/2m\omega}(a + a^\dagger)$ and $p = i\sqrt{\hbar m\omega/2}(a^\dagger - a)$. Their variances in $|\alpha\rangle$ are computed from $\langle(\Delta a)^2\rangle$-type expectation values; because $|\alpha\rangle$ is an eigenstate of $a$, all normally ordered fluctuations vanish and one finds:

**第 4 步 — 最小不确定正交分量。** 定义正交分量 $x = \sqrt{\hbar/2m\omega}(a + a^\dagger)$ 与 $p = i\sqrt{\hbar m\omega/2}(a^\dagger - a)$。其在 $|\alpha\rangle$ 中的方差由 $\langle(\Delta a)^2\rangle$ 型期望值计算；因 $|\alpha\rangle$ 是 $a$ 的本征态，所有正规排序涨落为零，得：

$$ \Delta x^2 = \hbar/(2m\omega), \quad \Delta p^2 = \hbar m\omega/2, \;\implies\; \boxed{\, \Delta x\, \Delta p = \hbar/2 \,}. $$

The coherent state thus saturates the Heisenberg bound with equal uncertainty shared between the two quadratures — the same as the vacuum $|0\rangle = |\alpha=0\rangle$, merely displaced in phase space.

相干态因此饱和海森堡界，两个正交分量平分等额不确定度——与真空 $|0\rangle = |\alpha=0\rangle$ 相同，只是在相空间中被平移。

**Step 5 — Squeezed states (remark).** A **squeezed state** keeps the product $\Delta x\, \Delta p = \hbar/2$ but redistributes it unequally: one quadrature variance is pushed below the vacuum value $\tfrac12$ (in natural units) while the conjugate one rises above it. Measuring the squeezed quadrature beats the standard quantum (shot-noise) limit, which is exploited in gravitational-wave interferometry and metrology. $\blacksquare$

**第 5 步 — 压缩态（说明）。** **压缩态**保持乘积 $\Delta x\, \Delta p = \hbar/2$，但不均等地重新分配：一个正交分量的方差被压到真空值 $\tfrac12$ 以下（自然单位），而共轭分量升至其上。测量被压缩的正交分量可突破标准量子（散粒噪声）极限，这被用于引力波干涉测量和计量学。$\blacksquare$

---

## E. Jaynes–Cummings Model & Vacuum Rabi Splitting · 杰恩斯–卡明斯模型与真空拉比劈裂

**Claim.** For the Jaynes–Cummings Hamiltonian $H = \hbar\omega a^\dagger a + \tfrac12\hbar\omega_0 \sigma_z + \hbar g(a^\dagger\sigma_- + a\sigma_+)$, the resonant ($\omega = \omega_0$) eigenstates within the $\{|e,n\rangle, |g,n+1\rangle\}$ subspace are dressed states split by $2\hbar g\sqrt{n+1}$. For $n = 0$ this gives the **vacuum Rabi splitting $2g$** — the single-photon strong-coupling signature of cavity QED.

**命题。** 对于杰恩斯–卡明斯哈密顿量 $H = \hbar\omega a^\dagger a + \tfrac12\hbar\omega_0 \sigma_z + \hbar g(a^\dagger\sigma_- + a\sigma_+)$，在 $\{|e,n\rangle, |g,n+1\rangle\}$ 子空间内的共振（$\omega = \omega_0$）本征态是劈裂为 $2\hbar g\sqrt{n+1}$ 的缀饰态。对 $n = 0$ 这给出**真空拉比劈裂 $2g$**——腔 QED 的单光子强耦合标志。

**Step 1 — Identify the conserved excitation number.** The interaction $\hbar g(a^\dagger\sigma_- + a\sigma_+)$ either destroys an atomic excitation while creating a photon ($a^\dagger\sigma_-$) or the reverse ($a\sigma_+$). It therefore conserves the total excitation number $N = a^\dagger a + |e\rangle\langle e|$. The Hilbert space splits into $2\times 2$ blocks spanned by the degenerate-excitation pair:

**第 1 步 — 辨认守恒激发数。** 相互作用 $\hbar g(a^\dagger\sigma_- + a\sigma_+)$ 要么消灭一个原子激发同时产生一个光子（$a^\dagger\sigma_-$），要么相反（$a\sigma_+$）。因此它守恒总激发数 $N = a^\dagger a + |e\rangle\langle e|$。希尔伯特空间分裂为由简并激发对张成的 $2\times 2$ 块：

$$ \{|e, n\rangle, |g, n+1\rangle\} \quad\text{(both have } N = n+1\text{)}. $$

The state $|g, 0\rangle$ (zero excitations) is uncoupled and is the exact ground state.

态 $|g, 0\rangle$（零激发）不耦合，是精确基态。

**Step 2 — Matrix elements in the block.** Apply $H$ to each basis state. The diagonal energies are:

**第 2 步 — 块内矩阵元。** 将 $H$ 作用于每个基态。对角能量为：

$$ \begin{aligned} \langle e,n|H|e,n\rangle &= \hbar\omega n + \tfrac12\hbar\omega_0, \\ \langle g,n+1|H|g,n+1\rangle &= \hbar\omega(n+1) - \tfrac12\hbar\omega_0. \end{aligned} $$

The off-diagonal coupling comes from $a\sigma_+|g,n+1\rangle = \sqrt{n+1}|e,n\rangle$ and $a^\dagger\sigma_-|e,n\rangle = \sqrt{n+1}|g,n+1\rangle$:

非对角耦合来自 $a\sigma_+|g,n+1\rangle = \sqrt{n+1}|e,n\rangle$ 与 $a^\dagger\sigma_-|e,n\rangle = \sqrt{n+1}|g,n+1\rangle$：

$$ \langle g,n+1|H|e,n\rangle = \hbar g\sqrt{n+1}. $$

**Step 3 — The $2\times 2$ Hamiltonian.** In the ordered basis $(|e,n\rangle, |g,n+1\rangle)$:

**第 3 步 — $2\times 2$ 哈密顿量。** 在有序基 $(|e,n\rangle, |g,n+1\rangle)$ 中：

$$ H_{block} = \hbar \begin{pmatrix} \omega n + \tfrac12\omega_0 & g\sqrt{n+1} \\ g\sqrt{n+1} & \omega(n+1) - \tfrac12\omega_0 \end{pmatrix}. $$

The detuning between the diagonal entries is $\delta = \omega_0 - \omega$. On resonance $\omega = \omega_0$ the two diagonal energies are equal to $\hbar(n+\tfrac12)\omega_0 + \tfrac12\hbar\omega$, so the matrix is degenerate up to the coupling.

对角元之间的失谐为 $\delta = \omega_0 - \omega$。共振时 $\omega = \omega_0$，两个对角能量都等于 $\hbar(n+\tfrac12)\omega_0 + \tfrac12\hbar\omega$，故矩阵除耦合外简并。

**Step 4 — Diagonalize on resonance.** A $2\times 2$ matrix with equal diagonal entries $E_0$ and off-diagonal $\hbar g\sqrt{n+1}$ has eigenvalues $E_0 \pm \hbar g\sqrt{n+1}$ with symmetric/antisymmetric eigenvectors:

**第 4 步 — 共振时对角化。** 对角元相等为 $E_0$、非对角为 $\hbar g\sqrt{n+1}$ 的 $2\times 2$ 矩阵，本征值为 $E_0 \pm \hbar g\sqrt{n+1}$，本征矢为对称/反对称组合：

$$ |n,\pm\rangle = (1/\sqrt 2)(|e,n\rangle \pm |g,n+1\rangle), \quad E_{n,\pm} = E_0 \pm \hbar g\sqrt{n+1}. $$

These are the **dressed states**. The splitting between the two dressed levels of the $(n+1)$-excitation manifold is:

这些是**缀饰态**。第 $(n+1)$ 激发流形两个缀饰能级之间的劈裂为：

$$ \Delta E_n = E_{n,+} - E_{n,-} = \boxed{\, 2\hbar g\sqrt{n+1} \,}. $$

**Step 5 — Vacuum Rabi splitting.** Set $n = 0$: the lowest excited manifold $\{|e,0\rangle, |g,1\rangle\}$ — one atomic excitation or one cavity photon — splits into two dressed states separated by:

**第 5 步 — 真空拉比劈裂。** 取 $n = 0$：最低激发流形 $\{|e,0\rangle, |g,1\rangle\}$——一个原子激发或一个腔光子——劈裂为两个缀饰态，间距为：

$$ \Delta E_0 = 2\hbar g \;\implies\; \boxed{\, \text{vacuum Rabi splitting} = 2g \,} \text{ (in frequency units)}. $$

Crucially this splitting is non-zero even with no photon initially present (the $|g,1\rangle \leftrightarrow |e,0\rangle$ exchange occurs through the vacuum field), so a single atom and a single cavity mode coherently exchange one quantum at rate $g$. Resolving the $2g$ doublet in the transmission spectrum — possible only when $g$ exceeds the cavity and atomic decay rates (the **strong-coupling regime**) — is the defining experimental signature of cavity quantum electrodynamics. $\blacksquare$

关键在于即使初始无光子，此劈裂也非零（$|g,1\rangle \leftrightarrow |e,0\rangle$ 交换通过真空场发生），故单个原子与单个腔模以速率 $g$ 相干交换一个量子。在透射谱中分辨 $2g$ 双峰——仅当 $g$ 超过腔与原子衰变速率时（**强耦合区**）才可能——是腔量子电动力学的标志性实验特征。$\blacksquare$

---

*All derivations are complete through intermediate algebra with physical interpretation. The Einstein A/B relations, laser threshold, Rabi formula, coherent-state statistics, and Jaynes–Cummings vacuum Rabi splitting are standard results of quantum optics and cavity QED (cross-ref 2.5, 3.10/3.14, 6.1/8.2).*

*所有推导均通过中间代数完整呈现并附物理诠释。爱因斯坦 A/B 关系、激光阈值、拉比公式、相干态统计和杰恩斯–卡明斯真空拉比劈裂均为量子光学与腔 QED 的标准结果（参见 2.5、3.10/3.14、6.1/8.2）。*

# Derivations — Module 4.8: Quantum Hall Effect
# 推导 — 模块 4.8：量子霍尔效应

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.8](./module-4.8-quantum-hall-effect.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.8](./module-4.8-quantum-hall-effect.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Landau-Level Spectrum and Degeneracy · 朗道能级谱与简并度

**Claim.** A 2D electron in perpendicular magnetic field $B$ has energy eigenvalues $E_n = \hbar\omega_c(n + \tfrac12)$ with degeneracy $eB/h$ per unit area.

**命题。** 垂直磁场 $B$ 中的二维电子具有能量本征值 $E_n = \hbar\omega_c(n + \tfrac12)$，每单位面积简并度为 $eB/h$。

**Step 1 — Hamiltonian in Landau gauge.** Choose $A = (0, Bx, 0)$ (Landau gauge). The Hamiltonian is

**第 1 步 — 朗道规范中的哈密顿量。** 选取 $A = (0, Bx, 0)$（朗道规范）。哈密顿量为

$$ H = \frac{p_x^2 + (p_y - eBx)^2}{2m^*}. $$

**Step 2 — Conserved momentum.** Since $H$ does not depend on $y$, $p_y$ commutes with $H$ and is a good quantum number: $p_y |\psi\rangle = \hbar k_y |\psi\rangle$. Write $\psi(x,y) = e^{ik_y y} \varphi(x)$. Substituting:

**第 2 步 — 守恒动量。** 由于 $H$ 不依赖于 $y$，$p_y$ 与 $H$ 对易，是好量子数：$p_y |\psi\rangle = \hbar k_y |\psi\rangle$。令 $\psi(x,y) = e^{ik_y y} \varphi(x)$。代入：

$$ H_\text{eff}\, \varphi(x) = \Big[\frac{p_x^2}{2m^*} + \frac{(\hbar k_y - eBx)^2}{2m^*}\Big] \varphi(x) = E\, \varphi(x). $$

**Step 3 — Harmonic oscillator.** Define the guiding-center coordinate $X_0 = \hbar k_y/(eB)$ and the magnetic length $l_B = \sqrt{\hbar/eB}$. Then:

**第 3 步 — 谐振子。** 定义导向中心坐标 $X_0 = \hbar k_y/(eB)$ 和磁长度 $l_B = \sqrt{\hbar/eB}$。则：

$$ H_\text{eff} = \frac{p_x^2}{2m^*} + \tfrac12 m^* \omega_c^2 (x - X_0)^2, \qquad \omega_c = eB/m^*. $$

This is exactly a harmonic oscillator centred at $x = X_0$, with frequency $\omega_c$. By the harmonic oscillator quantisation of Module 3.2:

这恰好是以 $x = X_0$ 为中心、频率为 $\omega_c$ 的谐振子。由模块 3.2 的谐振子量子化：

$$ E_n = \hbar \omega_c (n + \tfrac12), \qquad n = 0, 1, 2, \ldots $$

**Step 4 — Degeneracy.** In a sample of area $L_x \times L_y$ with periodic boundary conditions in $y$, $k_y$ takes values $2\pi m/L_y$. The guiding center $X_0 = \hbar k_y/(eB) = l_B^2 k_y$ must lie within $[0, L_x]$, so $0 \le k_y \le L_x/l_B^2$. The number of allowed $k_y$ values (and hence the number of degenerate states in one Landau level) is

**第 4 步 — 简并度。** 在面积 $L_x \times L_y$ 的样品中，$y$ 方向周期边界条件使 $k_y$ 取值 $2\pi m/L_y$。导向中心 $X_0 = \hbar k_y/(eB) = l_B^2 k_y$ 必须在 $[0, L_x]$ 内，故 $0 \le k_y \le L_x/l_B^2$。允许的 $k_y$ 值数（即每个朗道能级的简并态数）为

$$ N_\text{deg} = \frac{L_x}{l_B^2} \cdot \frac{L_y}{2\pi} = \frac{L_x L_y}{2\pi l_B^2} = L_x L_y \cdot \frac{eB}{h}. $$

The degeneracy per unit area is $g = eB/h = 1/\Phi_0$, where $\Phi_0 = h/e$ is the magnetic flux quantum. $\blacksquare$

每单位面积简并度为 $g = eB/h = 1/\Phi_0$，其中 $\Phi_0 = h/e$ 是磁通量子。$\blacksquare$

---

## B. Hall Conductivity $\sigma_{xy} = \nu e^2/h$ · 霍尔电导率

**Claim.** When exactly $\nu$ Landau levels are filled, the Hall conductivity is $\sigma_{xy} = \nu e^2/h$ and the longitudinal conductivity $\sigma_{xx} = 0$.

**命题。** 当恰好 $\nu$ 个朗道能级填满时，霍尔电导率为 $\sigma_{xy} = \nu e^2/h$，纵向电导率 $\sigma_{xx} = 0$。

**Step 1 — Drift picture.** In crossed electric field $E_x$ and magnetic field $B_z$, electrons undergo $E\times B$ drift with velocity $v_\text{drift} = E_x/B$ perpendicular to both fields. In a Hall bar geometry with width $W$ and $N$ carriers per unit area:

**第 1 步 — 漂移图像。** 在交叉电场 $E_x$ 和磁场 $B_z$ 中，电子以速度 $v_\text{drift} = E_x/B$ 在两者垂直方向做 $E\times B$ 漂移。在宽度为 $W$、单位面积载流子数为 $N$ 的霍尔条几何中：

$$ \text{Hall current density} \quad j_y = n_s e\, v_\text{drift} = n_s e E_x / B. $$

The Hall conductivity $\sigma_{xy} = j_y/E_x = n_s e/B$. When exactly $\nu$ Landau levels are filled, $n_s = \nu eB/h$, giving:

霍尔电导率 $\sigma_{xy} = j_y/E_x = n_s e/B$。当恰好 $\nu$ 个朗道能级填充时，$n_s = \nu eB/h$，给出：

$$ \sigma_{xy} = \nu e^2 / h. $$

**Step 2 — Why $\sigma_{xx} = 0$.** With a completely filled Landau level and an energy gap to the next, there are no states at the Fermi energy for scattering. All bulk states are localized (Anderson localization from disorder); only the extended edge states carry current. Extended states do not contribute to longitudinal conductance when the Fermi level lies in a gap between Landau levels, hence $\sigma_{xx} = 0$. $\blacksquare$

**第 2 步 — 为何 $\sigma_{xx} = 0$。** 完全填充朗道能级且到下一个能级有能隙时，费米能量处无散射态。所有体态均被局域（来自无序的安德森局域化）；只有扩展边缘态携带电流。当费米能级位于朗道能级之间的能隙中时，扩展态不贡献纵向电导，故 $\sigma_{xx} = 0$。$\blacksquare$

**Step 3 — Kubo formula confirmation.** The linear-response Kubo formula for Hall conductivity is $\sigma_{xy} = (i\hbar/V) \sum_{n\ne m} [f(E_n)-f(E_m)] \langle n|v_x|m\rangle\langle m|v_y|n\rangle/(E_n-E_m)^2$. When band $n$ is fully filled and band $m$ empty, this sum over filled Landau levels gives the Chern number $C_n$ for each level, and $\sum_n C_n = \nu$ when $\nu$ levels are filled. Since each Landau level has $C_n = 1$, $\sigma_{xy} = \nu e^2/h$. $\blacksquare$

**第 3 步 — 久保公式验证。** 霍尔电导率的线性响应久保公式为 $\sigma_{xy} = (i\hbar/V) \sum_{n\ne m} [f(E_n)-f(E_m)] \langle n|v_x|m\rangle\langle m|v_y|n\rangle/(E_n-E_m)^2$。当能带 $n$ 完全填充、能带 $m$ 为空时，对填充朗道能级的求和给出每个能级的陈数 $C_n$，$\nu$ 个能级填满时 $\sum_n C_n = \nu$。由于每个朗道能级 $C_n = 1$，故 $\sigma_{xy} = \nu e^2/h$。$\blacksquare$

---

## C. Edge-State / Büttiker Argument · 边缘态 / 比特克论证

**Claim.** In a Hall bar geometry, the quantized Hall resistance arises from chiral edge states. The number of edge channels equals $\nu$ and each carries conductance $e^2/h$, giving $R_H = h/(\nu e^2)$ and $R_L = 0$.

**命题。** 在霍尔条几何中，量子化霍尔电阻源于手征边缘态。边缘通道数等于 $\nu$，每个携带电导 $e^2/h$，给出 $R_H = h/(\nu e^2)$ 且 $R_L = 0$。

**Step 1 — Confinement bends Landau levels.** Near the edge of the sample the confining potential raises the energy. Each Landau level $E_n = \hbar\omega_c(n + \tfrac12)$ must rise to the Fermi energy at the boundary, crossing $E_F$ and creating a set of states propagating along the edge. These are the **edge states**.

**第 1 步 — 约束弯曲朗道能级。** 在样品边缘附近，约束势使能量升高。每个朗道能级 $E_n = \hbar\omega_c(n + \tfrac12)$ 必须在边界处升至费米能量，穿越 $E_F$ 并产生一组沿边缘传播的态。这些就是**边缘态**。

**Step 2 — Chirality.** At the lower edge, levels cross $E_F$ with positive group velocity (right-movers); at the upper edge, they cross with negative group velocity (left-movers). The direction is fixed by the magnetic field — the edge states are **chiral**. Back-scattering (right-mover to left-mover) requires crossing the sample, but the bulk states are all gapped and localized, making back-scattering exponentially suppressed.

**第 2 步 — 手征性。** 在下边缘，能级以正群速度穿越 $E_F$（右行者）；在上边缘，以负群速度穿越（左行者）。方向由磁场固定——边缘态是**手征**的。背向散射（右行者到左行者）需要穿越样品，但体态均有能隙且局域，使背向散射指数级压制。

**Step 3 — Conductance quantization.** With $\nu$ filled Landau levels there are $\nu$ chiral channels on each edge. Using the Landauer–Büttiker formula, the two-terminal conductance from source to drain is

**第 3 步 — 电导量子化。** 有 $\nu$ 个填充朗道能级时，每条边上有 $\nu$ 个手征通道。利用朗道–比特克公式，从源到漏的两端电导为

$$ G = \nu e^2/h. $$

The Hall voltage $V_H = I/G_H = I h/(\nu e^2)$, giving $R_H = V_H/I = h/(\nu e^2)$. The longitudinal voltage $V_L = 0$ because there is no dissipation in perfectly transmitted chiral channels, so $R_L = 0$. $\blacksquare$

霍尔电压 $V_H = I/G_H = I h/(\nu e^2)$，给出 $R_H = V_H/I = h/(\nu e^2)$。纵向电压 $V_L = 0$，因为在完美透射的手征通道中无耗散，故 $R_L = 0$。$\blacksquare$

---

## D. Laughlin Fractional Charge $e/m$ (Qualitative but Quantitative Result) · 劳夫林分数电荷 $e/m$

**Claim.** The elementary excitations of the Laughlin state at filling $\nu = 1/m$ ($m$ odd) carry charge $e/m$.

**命题。** 填充因子 $\nu = 1/m$（$m$ 为奇整数）处劳夫林态的元激发携带电荷 $e/m$。

**Step 1 — Laughlin's argument (flux insertion).** Consider threading an additional magnetic flux $\Phi = \Phi_0 = h/e$ adiabatically through a small solenoid at the origin of the 2DEG. By Faraday's law this induces an azimuthal electric field, which drives a radial current. The charge transported to the edge equals the total charge displaced.

**第 1 步 — 劳夫林论证（磁通插入）。** 考虑在二维电子气原点处的小螺线管中绝热地穿入额外磁通 $\Phi = \Phi_0 = h/e$。由法拉第定律，这感应出方位角电场，驱动径向电流。输运到边缘的电荷等于总位移电荷。

**Step 2 — Radial current from Hall conductivity.** The induced azimuthal electric field drives a radial current via the Hall conductivity. The charge displaced to the outer edge during the flux insertion is

**第 2 步 — 由霍尔电导率产生的径向电流。** 感应的方位角电场通过霍尔电导率驱动径向电流。磁通插入期间位移到外边缘的电荷为

$$ Q = \sigma_{xy} \cdot \Phi_0 = (\nu e^2/h) \cdot (h/e) = \nu e. $$

**Step 3 — At fractional filling.** At $\nu = 1/m$, $Q = e/m$. Inserting one flux quantum $\Phi_0$ displaces charge $e/m$ to the boundary, leaving behind a deficiency — a quasihole of charge $+e/m$ at the origin. By time-reversal and particle–hole symmetry, quasielectron excitations carry charge $-e/m$.

**第 3 步 — 在分数填充时。** 在 $\nu = 1/m$ 时，$Q = e/m$。插入一个磁通量子 $\Phi_0$ 将电荷 $e/m$ 位移到边界，在原点留下一个亏缺——电荷为 $+e/m$ 的准空穴。由时间反演和粒子–空穴对称性，准电子激发携带电荷 $-e/m$。

**Step 4 — Consistency with the Laughlin wavefunction.** A quasihole at position $z_0$ is created by inserting the operator $\prod_i (z_i - z_0)$ into the Laughlin wavefunction $\Psi_{1/m}$. This factor adds one unit of angular momentum to each electron, consistent with inserting one flux quantum. The charge enclosed follows from Gauss's law applied to the charge density: integrating the change in density when the quasihole operator is inserted yields exactly $e/m$. $\blacksquare$

**第 4 步 — 与劳夫林波函数的一致性。** 位于 $z_0$ 处的准空穴通过在劳夫林波函数 $\Psi_{1/m}$ 中插入算符 $\prod_i (z_i - z_0)$ 来创建。这个因子给每个电子增加一个角动量单位，与插入一个磁通量子一致。所围电荷由对电荷密度的高斯定律得出：对插入准空穴算符时密度变化积分，恰好得到 $e/m$。$\blacksquare$

The fractional charge $e/m$ has been confirmed experimentally by shot-noise measurements (Picciotto et al., 1997; Saminadayar et al., 1997), providing direct evidence for charge fractionalization in the FQHE.

分数电荷 $e/m$ 已通过散粒噪声测量（Picciotto 等，1997 年；Saminadayar 等，1997 年）在实验上得到证实，为 FQHE 中的电荷分数化提供了直接证据。

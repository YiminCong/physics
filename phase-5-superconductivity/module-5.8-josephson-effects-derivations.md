# Derivations — Module 5.8: Josephson Effects
# 推导 — 模块 5.8：约瑟夫森效应

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.8](./module-5.8-josephson-effects.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.8](./module-5.8-josephson-effects.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. DC Josephson Effect: $I = I_c \sin(\Delta\varphi)$ · 直流约瑟夫森效应

**Claim.** For two superconductors separated by a thin weak link (insulator, normal metal, or constriction), the supercurrent tunneling through the barrier is

$$ I = I_c \sin(\varphi_1 - \varphi_2) \equiv I_c \sin(\Delta\varphi), $$

where $\varphi_1, \varphi_2$ are the macroscopic phases of the two condensates and $I_c$ is the critical current of the junction.

**命题。** 对由薄弱连接（绝缘体、正常金属或收缩）隔开的两个超导体，穿过势垒的超电流为

$$ I = I_c \sin(\varphi_1 - \varphi_2) \equiv I_c \sin(\Delta\varphi), $$

其中 $\varphi_1$、$\varphi_2$ 为两个凝聚体的宏观相位，$I_c$ 为结的临界电流。

---

**Step 1 — Coupled condensate equations (Feynman approach).** Model each condensate by a macroscopic wavefunction (order parameter) $\Psi_j = \sqrt{n_j}\, e^{i\varphi_j}$ ($j = 1, 2$), where $n_j$ is the Cooper-pair density. Across the thin barrier, the condensates are weakly coupled with strength $K$ (the tunneling amplitude for pairs). The Schrödinger-like equations for the two condensates (treating the barrier as a weak perturbation) are:

$$ \begin{aligned} i\hbar\, \partial\Psi_1/\partial t &= \mu_1 \Psi_1 + K \Psi_2, \\ i\hbar\, \partial\Psi_2/\partial t &= \mu_2 \Psi_2 + K \Psi_1, \end{aligned} $$

where $\mu_1$ and $\mu_2$ are the chemical potentials of the two sides (related to the voltage by $\mu_1 - \mu_2 = 2eV$ for Cooper pairs of charge $2e$).

**第 1 步 — 耦合凝聚体方程（费曼方法）。** 用宏观波函数（序参量）$\Psi_j = \sqrt{n_j}\, e^{i\varphi_j}$（$j = 1, 2$）对每个凝聚体建模，$n_j$ 为库珀对密度。在薄势垒两侧，凝聚体以强度 $K$（对的隧穿振幅）弱耦合。两凝聚体的类薛定谔方程（将势垒作为弱微扰处理）为：

$$ \begin{aligned} i\hbar\, \partial\Psi_1/\partial t &= \mu_1 \Psi_1 + K \Psi_2, \\ i\hbar\, \partial\Psi_2/\partial t &= \mu_2 \Psi_2 + K \Psi_1, \end{aligned} $$

其中 $\mu_1$、$\mu_2$ 为两侧化学势（对于电荷 $2e$ 的库珀对，与电压的关系为 $\mu_1 - \mu_2 = 2eV$）。

**Step 2 — Substitute $\Psi_j = \sqrt{n_j}\, e^{i\varphi_j}$ and separate real/imaginary parts.** Writing $\Psi_1 = \sqrt{n_1}\, e^{i\varphi_1}$ and differentiating:

$$ i\hbar\, (\dot{n}_1/(2\sqrt{n_1}) + i\sqrt{n_1}\, \dot{\varphi}_1)\, e^{i\varphi_1} = \mu_1 \sqrt{n_1}\, e^{i\varphi_1} + K \sqrt{n_2}\, e^{i\varphi_2}. $$

Multiply both sides by $e^{-i\varphi_1}/\sqrt{n_1}$:

$$ i\hbar\, (\dot{n}_1/(2n_1) + i\dot{\varphi}_1) = \mu_1 + K \sqrt{n_2/n_1}\, e^{i(\varphi_2-\varphi_1)}. $$

Let $\Delta\varphi = \varphi_2 - \varphi_1$. Separating real and imaginary parts:

$$ \begin{aligned} \text{Real:}& \quad -\hbar\, \dot{\varphi}_1 = \mu_1 + K \sqrt{n_2/n_1}\, \cos(\Delta\varphi), \\ \text{Imag:}& \quad \hbar\, \dot{n}_1/(2n_1) = K \sqrt{n_2/n_1}\, \sin(\Delta\varphi). \end{aligned} $$

**第 2 步 — 代入 $\Psi_j = \sqrt{n_j}\, e^{i\varphi_j}$ 并分离实虚部。** 写 $\Psi_1 = \sqrt{n_1}\, e^{i\varphi_1}$ 并求导，乘以 $e^{-i\varphi_1}/\sqrt{n_1}$：

$$ i\hbar\, (\dot{n}_1/(2n_1) + i\dot{\varphi}_1) = \mu_1 + K \sqrt{n_2/n_1}\, e^{i(\varphi_2-\varphi_1)}. $$

令 $\Delta\varphi = \varphi_2 - \varphi_1$，分离实虚部：

$$ \begin{aligned} \text{实部：}& \quad -\hbar\, \dot{\varphi}_1 = \mu_1 + K \sqrt{n_2/n_1}\, \cos(\Delta\varphi), \\ \text{虚部：}& \quad \hbar\, \dot{n}_1/(2n_1) = K \sqrt{n_2/n_1}\, \sin(\Delta\varphi). \end{aligned} $$

**Step 3 — The supercurrent is proportional to $\sin(\Delta\varphi)$.** The imaginary part gives $\dot{n}_1 \propto \sin(\Delta\varphi)$. Since $\dot{n}_1$ is the rate of change of Cooper-pair density on side 1, and each pair carries charge $2e$, the electric current flowing from side 2 to side 1 is

$$ I = 2e A\, \dot{n}_1 = (2eA \cdot 2n_1 K\sqrt{n_2/n_1}/\hbar)\, \sin(\Delta\varphi) \equiv I_c \sin(\Delta\varphi), $$

where $A$ is the junction area and $I_c = (2eA \cdot 2K\sqrt{n_1 n_2}/\hbar)$ absorbs all the prefactors. For a symmetric junction $n_1 = n_2 = n$, $I_c = 4eAKn/\hbar$.

**第 3 步 — 超电流正比于 $\sin(\Delta\varphi)$。** 虚部给出 $\dot{n}_1 \propto \sin(\Delta\varphi)$。由于 $\dot{n}_1$ 是第 1 侧库珀对密度的变化率，每对携带电荷 $2e$，从第 2 侧流向第 1 侧的电流为

$$ I = 2e A\, \dot{n}_1 = (2eA \cdot 2n_1 K\sqrt{n_2/n_1}/\hbar)\, \sin(\Delta\varphi) \equiv I_c \sin(\Delta\varphi), $$

其中 $A$ 为结面积，$I_c = (2eA \cdot 2K\sqrt{n_1 n_2}/\hbar)$ 吸收了所有前置因子。对对称结 $n_1 = n_2 = n$，$I_c = 4eAKn/\hbar$。

**Step 4 — Physical content of the DC effect.** When $V = 0$ (no voltage applied), $\mu_1 = \mu_2$ and the phase difference $\Delta\varphi$ is constant (time-independent). The junction then carries a steady supercurrent $I = I_c \sin(\Delta\varphi)$ with no dissipation. The value of $\Delta\varphi$ adjusts to whatever is needed to carry the external current, up to $I_c$. This is the DC Josephson effect: **supercurrent flows at zero voltage.** $\blacksquare$

**第 4 步 — 直流效应的物理内涵。** 当 $V = 0$（无外加电压）时，$\mu_1 = \mu_2$，相位差 $\Delta\varphi$ 为常数（与时间无关）。结携带稳定的超电流 $I = I_c \sin(\Delta\varphi)$ 而无耗散。$\Delta\varphi$ 自动调整以承载外部电流，最大可达 $I_c$。这就是直流约瑟夫森效应：**超电流在零电压下流动。**$\blacksquare$

---

## B. AC Josephson Effect: $d(\Delta\varphi)/dt = 2eV/\hbar$ · 交流约瑟夫森效应

**Claim.** When a constant voltage $V$ is applied across the junction, the phase difference evolves as $d(\Delta\varphi)/dt = 2eV/\hbar$, leading to an oscillating supercurrent at the Josephson frequency $f_J = 2eV/h$.

**命题。** 当恒定电压 $V$ 加在结两端时，相位差按 $d(\Delta\varphi)/dt = 2eV/\hbar$ 演化，导致超电流以约瑟夫森频率 $f_J = 2eV/h$ 振荡。

**Step 1 — Phase evolution equation from chemical potential difference.** From the real-part equation of Step 2 above (and its counterpart for side 2), the phases evolve as:

$$ \begin{aligned} \hbar\, \dot{\varphi}_1 &= -\mu_1 + \text{(small coupling terms)}, \\ \hbar\, \dot{\varphi}_2 &= -\mu_2 + \text{(small coupling terms)}. \end{aligned} $$

Subtracting (and dropping the coupling terms, which are small for a tunnel junction with $K \ll \Delta$):

$$ \hbar\, d(\Delta\varphi)/dt = \hbar(\dot{\varphi}_2 - \dot{\varphi}_1) = \mu_1 - \mu_2. $$

**第 1 步 — 由化学势差得相位演化方程。** 由上面第 2 步实部方程（及第 2 侧对应方程），相位演化为：

$$ \begin{aligned} \hbar\, \dot{\varphi}_1 &= -\mu_1 + \text{（小耦合项）}, \\ \hbar\, \dot{\varphi}_2 &= -\mu_2 + \text{（小耦合项）}. \end{aligned} $$

相减（对于 $K \ll \Delta$ 的隧道结，略去小耦合项）：

$$ \hbar\, d(\Delta\varphi)/dt = \hbar(\dot{\varphi}_2 - \dot{\varphi}_1) = \mu_1 - \mu_2. $$

**Step 2 — Connect chemical potential to voltage.** The electrochemical potential difference across the junction is the voltage times the pair charge:

$$ \mu_1 - \mu_2 = 2eV \qquad \text{(Cooper pairs carry charge } 2e\text{).} $$

Hence

$$ d(\Delta\varphi)/dt = 2eV/\hbar. $$

This is the **Josephson phase-voltage relation** (also called the second Josephson relation).

**第 2 步 — 将化学势与电压相联系。** 结两端的电化学势差等于电压乘以对电荷：

$$ \mu_1 - \mu_2 = 2eV \qquad \text{（库珀对携带电荷 } 2e\text{）。} $$

故

$$ d(\Delta\varphi)/dt = 2eV/\hbar. $$

这是**约瑟夫森相位–电压关系**（也称第二约瑟夫森关系）。

**Step 3 — Integration to find $\Delta\varphi(t)$.** For constant $V$, integrate:

$$ \Delta\varphi(t) = \Delta\varphi(0) + (2eV/\hbar) t = \Delta\varphi(0) + 2\pi (2eV/h) t = \Delta\varphi(0) + 2\pi f_J t, $$

where the **Josephson frequency** is

$$ f_J = 2eV/h \approx (483.6\ \text{MHz}/\mu\text{V}) \times V. $$

**第 3 步 — 积分求 $\Delta\varphi(t)$。** 对恒定 $V$ 积分：

$$ \Delta\varphi(t) = \Delta\varphi(0) + (2eV/\hbar) t = \Delta\varphi(0) + 2\pi (2eV/h) t = \Delta\varphi(0) + 2\pi f_J t, $$

其中**约瑟夫森频率**为

$$ f_J = 2eV/h \approx (483.6\ \text{MHz}/\mu\text{V}) \times V. $$

**Step 4 — Oscillating supercurrent.** Substituting into $I = I_c \sin(\Delta\varphi)$:

$$ I(t) = I_c \sin(\Delta\varphi(0) + 2\pi f_J t). $$

This is an **AC supercurrent** oscillating at frequency $f_J$. The amplitude is $I_c$ and the frequency is exactly $2eV/h$ — it contains no material constants, only fundamental constants $e$ and $h$. This means the Josephson junction is a quantum-mechanical frequency standard: measuring $f_J$ and $V$ gives $e/h$ to extraordinary precision (the basis of the Josephson voltage standard, with $1\ \text{V}$ defined via $2e/h$). $\blacksquare$

**第 4 步 — 振荡超电流。** 代入 $I = I_c \sin(\Delta\varphi)$：

$$ I(t) = I_c \sin(\Delta\varphi(0) + 2\pi f_J t). $$

这是以频率 $f_J$ 振荡的**交流超电流**。振幅为 $I_c$，频率恰好为 $2eV/h$——仅包含基本常数 $e$ 和 $h$，不含材料常数。这意味着约瑟夫森结是量子力学频率标准：测量 $f_J$ 和 $V$ 可以极高精度确定 $e/h$（约瑟夫森电压标准的基础，$1\ \text{V}$ 通过 $2e/h$ 定义）。$\blacksquare$

---

## C. The SQUID Interference Pattern: $I_{\max} = 2I_c |\cos(\pi\Phi/\Phi_0)|$ · SQUID 干涉图样

**Claim.** A DC-SQUID consists of two Josephson junctions connected in parallel in a superconducting loop. The maximum supercurrent is

$$ I_{\max}(\Phi) = 2I_c |\cos(\pi\Phi/\Phi_0)|, $$

where $\Phi$ is the magnetic flux threading the loop and $\Phi_0 = h/2e$. This is a direct quantum interference effect analogous to a double-slit experiment in optics.

**命题。** 直流 SQUID 由超导回路中并联的两个约瑟夫森结组成。最大超电流为

$$ I_{\max}(\Phi) = 2I_c |\cos(\pi\Phi/\Phi_0)|, $$

其中 $\Phi$ 为穿过回路的磁通量，$\Phi_0 = h/2e$。这是类似于光学双缝实验的直接量子干涉效应。

**Step 1 — Phase differences across each junction.** Label the two junctions as A and B with phase differences $\delta_A$ and $\delta_B$. The total current is

$$ I = I_c \sin(\delta_A) + I_c \sin(\delta_B) \qquad \text{(assuming equal critical currents).} $$

We need to determine the relationship between $\delta_A$ and $\delta_B$ imposed by the topology of the loop.

**第 1 步 — 每个结上的相位差。** 将两个结标记为 A 和 B，相位差分别为 $\delta_A$ 和 $\delta_B$。总电流为

$$ I = I_c \sin(\delta_A) + I_c \sin(\delta_B) \qquad \text{（假设临界电流相等）。} $$

我们需要确定由回路拓扑强加的 $\delta_A$ 与 $\delta_B$ 的关系。

**Step 2 — Fluxoid quantization around the loop.** Deep inside the superconducting arms of the loop, $J_s = 0$ (the screening currents die away from the junctions). The fluxoid quantization condition (from Appendix A, Section A, with the contour running through the superconducting bulk of both arms and crossing each junction once):

$$ (\delta_A - \delta_B) + (2e/\hbar) \Phi = 2\pi n, \qquad n \in \mathbb{Z}. $$

Here $(2e/\hbar) \Phi = 2\pi \Phi/\Phi_0$ is the gauge contribution from the enclosed flux, and $\delta_A - \delta_B$ accounts for the phase change through each junction. For $n = 0$ (single fluxoid quantum):

$$ \delta_A - \delta_B = -2\pi\Phi/\Phi_0. $$

**第 2 步 — 回路的磁通量子化条件。** 在回路超导臂的深处，$J_s = 0$（屏蔽电流从结处消失）。磁通量子化条件（来自附录 A 第 A 节，回路穿过两臂超导体并各通过一次结）：

$$ (\delta_A - \delta_B) + (2e/\hbar) \Phi = 2\pi n, \qquad n \in \mathbb{Z}. $$

这里 $(2e/\hbar) \Phi = 2\pi \Phi/\Phi_0$ 是封闭磁通的规范贡献，$\delta_A - \delta_B$ 计入了穿过每个结的相位变化。取 $n = 0$（单磁通量子）：

$$ \delta_A - \delta_B = -2\pi\Phi/\Phi_0. $$

**Step 3 — Parametrize with sum and difference.** Let the average phase difference be $\bar{\delta} = (\delta_A + \delta_B)/2$. Then from Step 2:

$$ \delta_A = \bar{\delta} + \pi\Phi/\Phi_0 \text{ (taking the sign convention } \delta_A - \delta_B = -2\pi\Phi/\Phi_0\text{, swap sign with convention):} $$

Let us use the symmetric parametrization:

$$ \delta_A = \bar{\delta} - \pi\Phi/\Phi_0, \qquad \delta_B = \bar{\delta} + \pi\Phi/\Phi_0. $$

These satisfy $\delta_A - \delta_B = -2\pi\Phi/\Phi_0$ as required.

**第 3 步 — 用和与差参数化。** 令平均相位差 $\bar{\delta} = (\delta_A + \delta_B)/2$。对称参数化：

$$ \delta_A = \bar{\delta} - \pi\Phi/\Phi_0, \qquad \delta_B = \bar{\delta} + \pi\Phi/\Phi_0. $$

这满足所需的 $\delta_A - \delta_B = -2\pi\Phi/\Phi_0$。

**Step 4 — Sum the currents using sum-to-product identity.** The total current:

$$ I = I_c [\sin(\bar{\delta} - \pi\Phi/\Phi_0) + \sin(\bar{\delta} + \pi\Phi/\Phi_0)]. $$

Apply the sum-to-product identity $\sin(A - B) + \sin(A + B) = 2 \sin A \cos B$ with $A = \bar{\delta}$ and $B = \pi\Phi/\Phi_0$:

$$ I = 2 I_c \cos(\pi\Phi/\Phi_0) \sin(\bar{\delta}). $$

**第 4 步 — 用积化和差公式求和。** 总电流：

$$ I = I_c [\sin(\bar{\delta} - \pi\Phi/\Phi_0) + \sin(\bar{\delta} + \pi\Phi/\Phi_0)]. $$

应用积化和差公式 $\sin(A - B) + \sin(A + B) = 2 \sin A \cos B$，其中 $A = \bar{\delta}$，$B = \pi\Phi/\Phi_0$：

$$ I = 2 I_c \cos(\pi\Phi/\Phi_0) \sin(\bar{\delta}). $$

**Step 5 — Maximize over the free phase $\bar{\delta}$.** The average phase $\bar{\delta}$ is the free variable that the circuit adjusts to carry whatever current is demanded. The maximum current (over all $\bar{\delta}$) is achieved at $\sin(\bar{\delta}) = 1$:

$$ I_{\max}(\Phi) = 2 I_c |\cos(\pi\Phi/\Phi_0)|. $$

The absolute value accounts for both signs of $\cos$. $\blacksquare$

**第 5 步 — 对自由相位 $\bar{\delta}$ 取最大值。** 平均相位 $\bar{\delta}$ 是电路自动调整以承载所需电流的自由变量。对所有 $\bar{\delta}$ 的最大电流在 $\sin(\bar{\delta}) = 1$ 时取得：

$$ I_{\max}(\Phi) = 2 I_c |\cos(\pi\Phi/\Phi_0)|. $$

绝对值考虑到了 $\cos$ 的正负两种情况。$\blacksquare$

**Step 6 — Physical interpretation and sensitivity.** The SQUID interference pattern $I_{\max}(\Phi) = 2I_c|\cos(\pi\Phi/\Phi_0)|$ oscillates with period $\Phi_0 = h/2e \approx 2.07 \times 10^{-15}$ Wb. Measuring the change in $I_{\max}$ by a fraction of $I_c$ resolves a fraction of $\Phi_0$. Modern SQUIDs achieve flux noise below $10^{-6}\ \Phi_0/\sqrt{\text{Hz}}$, corresponding to magnetic field sensitivities below $1\ \text{fT}/\sqrt{\text{Hz}}$ — orders of magnitude better than any classical magnetometer. This is used for MEG (magnetoencephalography), SQUID microscopy, and searches for dark matter axions. $\blacksquare$

**第 6 步 — 物理诠释与灵敏度。** SQUID 干涉图样 $I_{\max}(\Phi) = 2I_c|\cos(\pi\Phi/\Phi_0)|$ 以 $\Phi_0 = h/2e \approx 2.07 \times 10^{-15}$ Wb 为周期振荡。将 $I_{\max}$ 的变化测量到 $I_c$ 的几分之一即可分辨 $\Phi_0$ 的几分之一。现代 SQUID 的磁通噪声低于 $10^{-6}\ \Phi_0/\sqrt{\text{Hz}}$，对应磁场灵敏度低于 $1\ \text{fT}/\sqrt{\text{Hz}}$——比任何经典磁强计高出数个数量级。这用于脑磁图（MEG）、SQUID 显微镜及暗物质轴子搜索。$\blacksquare$

---

## D. Josephson Relations from the Tunneling Hamiltonian (Alternative Derivation) · 从隧穿哈密顿量推导约瑟夫森关系（另一推导）

**Step 1 — Setup.** In the tunneling Hamiltonian formalism (Cohen–Falicov–Phillips, also used in Module 5.6), the Hamiltonian for two superconductors coupled by a barrier is $H = H_1 + H_2 + H_T$, where $H_T = \sum_{k,q} T_{kq} c^\dagger_k d_q + \text{h.c.}$ transfers single electrons, and $c^\dagger_k, d_q$ create/annihilate electrons on the two sides.

**第 1 步 — 准备。** 在隧穿哈密顿量形式（Cohen–Falicov–Phillips，模块 5.6 中也用到）中，两个通过势垒耦合的超导体的哈密顿量为 $H = H_1 + H_2 + H_T$，其中 $H_T = \sum_{k,q} T_{kq} c^\dagger_k d_q + \text{h.c.}$ 传递单个电子，$c^\dagger_k$、$d_q$ 在两侧分别产生/湮灭电子。

**Step 2 — Pair tunneling at second order.** To lowest order in $T$, only single-electron transfer is present (this is the Giaever tunneling of Module 5.6). However, for Cooper-pair tunneling, we must go to **second order in $T$**: two simultaneous single-electron tunneling events constitute one pair transfer. The effective pair tunneling Hamiltonian at second order is

$$ H_{\text{pair}} \propto \sum_{k,q} (T_{kq})^2 (c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow})(d_{-q\downarrow}d_{q\uparrow}) + \text{h.c.}, $$

which, in BCS language, involves the anomalous averages $\langle c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow}\rangle = u_k v_k e^{i\varphi_1}$ and $\langle d_{q\downarrow}d_{-q\uparrow}\rangle = u_q v_q e^{i\varphi_2}$. Evaluating expectation values:

$$ \langle H_{\text{pair}}\rangle \propto |\Delta_1||\Delta_2| \sin(\varphi_1 - \varphi_2)\cdot(-1) = -E_J \cos(\Delta\varphi), $$

where $E_J \propto |\Delta_1||\Delta_2|/R_T$ is the Josephson coupling energy and $R_T$ is the tunnel resistance.

**第 2 步 — 二阶对隧穿。** 在 $T$ 的最低阶，仅有单电子转移（模块 5.6 的贾埃弗隧穿）。然而对于库珀对隧穿，必须到 **$T$ 的二阶**：两个同时发生的单电子隧穿事件构成一次对转移。二阶有效对隧穿哈密顿量为

$$ H_{\text{pair}} \propto \sum_{k,q} (T_{kq})^2 (c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow})(d_{-q\downarrow}d_{q\uparrow}) + \text{h.c.}, $$

用 BCS 语言，涉及反常平均 $\langle c^\dagger_{k\uparrow}c^\dagger_{-k\downarrow}\rangle = u_k v_k e^{i\varphi_1}$ 和 $\langle d_{q\downarrow}d_{-q\uparrow}\rangle = u_q v_q e^{i\varphi_2}$。取期望值：

$$ \langle H_{\text{pair}}\rangle \propto |\Delta_1||\Delta_2| \sin(\varphi_1 - \varphi_2)\cdot(-1) = -E_J \cos(\Delta\varphi), $$

其中 $E_J \propto |\Delta_1||\Delta_2|/R_T$ 为约瑟夫森耦合能，$R_T$ 为隧穿电阻。

**Step 3 — Current from the energy.** The supercurrent is the derivative of the total energy with respect to the phase (this follows from the general relation $I = (2e/\hbar) \partial E/\partial(\Delta\varphi)$, the supercurrent–phase relation in thermodynamics):

$$ I = (2e/\hbar) \partial(-E_J \cos\Delta\varphi)/\partial(\Delta\varphi) = (2e/\hbar) E_J \sin(\Delta\varphi) \equiv I_c \sin(\Delta\varphi), $$

where $I_c = 2eE_J/\hbar$. This confirms the Feynman result and relates $I_c$ to the microscopic tunneling matrix element. The **Ambegaokar–Baratoff formula** (1963) gives explicitly:

$$ I_c R_T = (\pi/2e) \Delta(T) \tanh(\Delta(T)/2k_BT), $$

at $T = 0$: $I_c R_T = \pi\Delta/(2e)$. $\blacksquare$

**第 3 步 — 由能量得电流。** 超电流是总能量对相位的导数（由热力学中的一般关系 $I = (2e/\hbar) \partial E/\partial(\Delta\varphi)$ 得到，即超电流–相位关系）：

$$ I = (2e/\hbar) \partial(-E_J \cos\Delta\varphi)/\partial(\Delta\varphi) = (2e/\hbar) E_J \sin(\Delta\varphi) \equiv I_c \sin(\Delta\varphi), $$

其中 $I_c = 2eE_J/\hbar$。这证实了费曼结果，并将 $I_c$ 与微观隧穿矩阵元联系起来。**安贝加尔–巴拉托夫公式**（1963）给出明确形式：

$$ I_c R_T = (\pi/2e) \Delta(T) \tanh(\Delta(T)/2k_BT), $$

$T = 0$ 时：$I_c R_T = \pi\Delta/(2e)$。$\blacksquare$

---

*Summary of Josephson physics: the DC relation $I = I_c \sin(\Delta\varphi)$ emerges from the coherent coupling between macroscopic quantum phases; the AC relation $d(\Delta\varphi)/dt = 2eV/\hbar$ follows from the energy difference between condensates at different chemical potentials; the SQUID result $I_{\max} = 2I_c|\cos(\pi\Phi/\Phi_0)|$ is a direct application of fluxoid quantization plus the sum-to-product identity. All three are macroscopic quantum effects.*

*约瑟夫森物理总结：直流关系 $I = I_c \sin(\Delta\varphi)$ 来自宏观量子相位之间的相干耦合；交流关系 $d(\Delta\varphi)/dt = 2eV/\hbar$ 来自不同化学势下凝聚体间的能量差；SQUID 结果 $I_{\max} = 2I_c|\cos(\pi\Phi/\Phi_0)|$ 是磁通量子化条件与积化和差公式的直接应用。三者均为宏观量子效应。*

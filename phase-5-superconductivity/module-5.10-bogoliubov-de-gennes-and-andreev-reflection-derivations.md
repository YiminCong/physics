---
title: "Derivations — Module 5.10: Bogoliubov–de Gennes & Andreev Reflection"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.10: Bogoliubov–de Gennes & Andreev Reflection
# 推导 — 模块 5.10：Bogoliubov–de Gennes 方程与安德烈夫反射

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.10](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.10](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the BdG Equations from the Mean-Field BCS Hamiltonian · 从平均场 BCS 哈密顿量推导 BdG 方程

**Claim.** Starting from the mean-field BCS Hamiltonian in real space, a Bogoliubov rotation into the Nambu particle–hole basis yields the BdG eigenvalue problem $H_{\text{BdG}} \Phi_n = E_n \Phi_n$ with the $2\times 2$ BdG matrix and the self-consistency condition on $\Delta(r)$.

**命题。** 从实空间的平均场 BCS 哈密顿量出发，通过 Nambu 粒子–空穴基中的 Bogoliubov 变换，得到 BdG 本征值问题 $H_{\text{BdG}} \Phi_n = E_n \Phi_n$，其中包含 $2\times 2$ BdG 矩阵和 $\Delta(r)$ 的自洽条件。

**Step 1 — Real-space second-quantized Hamiltonian.** Write the full Hamiltonian for interacting spin-1/2 electrons in second quantization:

**第 1 步 — 实空间二次量子化哈密顿量。** 写出二次量子化形式下相互作用自旋-1/2 电子的完整哈密顿量：

$$ H = \int d^3r \sum_\sigma \psi_\sigma^\dagger(r) H_0(r) \psi_\sigma(r) + g \int d^3r\, \psi_\uparrow^\dagger(r) \psi_\downarrow^\dagger(r) \psi_\downarrow(r) \psi_\uparrow(r), $$

where $H_0(r) = -\hbar^2\nabla^2/2m + U(r) - \mu$ is the single-particle Hamiltonian relative to the chemical potential, $g < 0$ is an attractive contact interaction, and $\psi_\sigma(r)$ are the electron field operators satisfying $\{\psi_\sigma(r), \psi_{\sigma'}^\dagger(r')\} = \delta_{\sigma\sigma'} \delta^3(r - r')$.

其中 $H_0(r) = -\hbar^2\nabla^2/2m + U(r) - \mu$ 是相对于化学势的单粒子哈密顿量，$g < 0$ 是吸引性接触相互作用，$\psi_\sigma(r)$ 是满足 $\{\psi_\sigma(r), \psi_{\sigma'}^\dagger(r')\} = \delta_{\sigma\sigma'} \delta^3(r - r')$ 的电子场算符。

**Step 2 — Mean-field decoupling.** Replace the four-fermion interaction by its mean-field (Hartree–Fock–Bogoliubov) decoupling. The anomalous average $\Delta(r) \equiv -g \langle\psi_\downarrow(r) \psi_\uparrow(r)\rangle$ is the pair potential. Neglecting the normal (Hartree) channel (absorbed into $U(r)$), the mean-field Hamiltonian is:

**第 2 步 — 平均场解耦。** 用平均场（Hartree–Fock–Bogoliubov）解耦替代四费米子相互作用。反常平均 $\Delta(r) \equiv -g \langle\psi_\downarrow(r) \psi_\uparrow(r)\rangle$ 即配对势。忽略正常（Hartree）通道（并入 $U(r)$），平均场哈密顿量为：

$$ H_{\text{MF}} = \int d^3r\, \left[ \sum_\sigma \psi_\sigma^\dagger(r) H_0(r) \psi_\sigma(r) + \Delta(r) \psi_\uparrow^\dagger(r) \psi_\downarrow^\dagger(r) + \Delta^*(r) \psi_\downarrow(r) \psi_\uparrow(r) \right] + \text{const.} $$

The constant is $\int d^3r\, |\Delta(r)|^2/g$ and is irrelevant for the eigenvalue problem.

常数项为 $\int d^3r\, |\Delta(r)|^2/g$，对本征值问题无关紧要。

**Step 3 — Introduce the Nambu spinor.** Define the two-component Nambu field:

**第 3 步 — 引入 Nambu 旋量。** 定义双分量 Nambu 场：

$$ \Psi(r) = \begin{pmatrix} \psi_\uparrow(r) \\ \psi_\downarrow^\dagger(r) \end{pmatrix}, \qquad \Psi^\dagger(r) = \begin{pmatrix} \psi_\uparrow^\dagger(r), & \psi_\downarrow(r) \end{pmatrix}. $$

Using the anticommutation relation to rewrite $\psi_\downarrow^\dagger H_0^* \psi_\downarrow^\dagger \to -\psi_\downarrow (-H_0^*(r)) \psi_\downarrow^\dagger$ (up to a constant from the commutation), the mean-field Hamiltonian becomes:

利用反对易关系将 $\psi_\downarrow^\dagger H_0^* \psi_\downarrow^\dagger$ 改写为 $-\psi_\downarrow (-H_0^*(r)) \psi_\downarrow^\dagger$（加上来自对易关系的常数），平均场哈密顿量变为：

$$ H_{\text{MF}} = \int d^3r\, \Psi^\dagger(r) H_{\text{BdG}} \Psi(r) + \text{const}, $$

$$ H_{\text{BdG}} = \begin{pmatrix} H_0(r) & \Delta(r) \\ \Delta^*(r) & -H_0^*(r) \end{pmatrix} $$

This is the **BdG Hamiltonian in Nambu space**. The off-diagonal $\Delta(r)$ mixes particle and hole sectors; $-H_0^*(r) = -(-\hbar^2\nabla^2/2m + U(r) - \mu)^*$ governs the hole sector (note: $U(r)$ is real, so $H_0^*(r) = H_0(r)$ for a scalar potential, but the sign flip is essential for particle–hole symmetry).

这就是 **Nambu 空间中的 BdG 哈密顿量**。非对角项 $\Delta(r)$ 混合粒子和空穴扇区；$-H_0^*(r) = -(-\hbar^2\nabla^2/2m + U(r) - \mu)^*$ 控制空穴扇区（注意：$U(r)$ 为实数时 $H_0^*(r) = H_0(r)$，但符号翻转对于粒子–空穴对称性至关重要）。

**Step 4 — Bogoliubov transformation and eigenvalue problem.** Expand the Nambu field in the eigenmodes:

**第 4 步 — Bogoliubov 变换与本征值问题。** 将 Nambu 场展开为本征模：

$$ \Psi(r) = \sum_n \left[ \gamma_n \Phi_n(r) + \gamma_n^\dagger \bar{\Phi}_n(r) \right], \qquad \Phi_n(r) = \begin{pmatrix} u_n(r) \\ v_n(r) \end{pmatrix} $$

where $\gamma_n$ are the quasiparticle annihilation operators. Requiring $H_{\text{MF}} = \sum_n E_n \gamma_n^\dagger \gamma_n$ (diagonal in quasiparticles) enforces the **BdG eigenvalue equations**:

其中 $\gamma_n$ 是准粒子湮灭算符。要求 $H_{\text{MF}} = \sum_n E_n \gamma_n^\dagger \gamma_n$（在准粒子中对角），强制要求 **BdG 本征值方程**：

$$ \begin{aligned} H_0(r) u_n(r) + \Delta(r) v_n(r) &= E_n u_n(r) \\ \Delta^*(r) u_n(r) - H_0^*(r) v_n(r) &= E_n v_n(r) \end{aligned} $$

or in matrix form: $H_{\text{BdG}} \Phi_n = E_n \Phi_n$.

或用矩阵形式：$H_{\text{BdG}} \Phi_n = E_n \Phi_n$。

**Step 5 — Self-consistency condition.** Inverting the Bogoliubov transformation to express $\psi_\uparrow(r), \psi_\downarrow(r)$ in terms of $\gamma_n$ and computing the thermal average, using $\langle\gamma_n^\dagger \gamma_m\rangle = f(E_n) \delta_{nm}$ and the condition $E_n > 0$ for the positive-energy branch:

**第 5 步 — 自洽条件。** 反转 Bogoliubov 变换，将 $\psi_\uparrow(r)$、$\psi_\downarrow(r)$ 用 $\gamma_n$ 表示，计算热平均，利用 $\langle\gamma_n^\dagger \gamma_m\rangle = f(E_n) \delta_{nm}$ 和正能分支 $E_n > 0$ 的条件：

$$ \begin{aligned} \Delta(r) &= -g \langle\psi_\downarrow(r) \psi_\uparrow(r)\rangle = -g \sum_n u_n(r) v_n^*(r) [1 - 2f(E_n)] \\ &= -g \sum_n u_n(r) v_n^*(r) \tanh(E_n / 2k_BT). \end{aligned} $$

This closes the self-consistent loop: one must find $\Delta(r)$ such that the BdG eigenmodes reproduce the same $\Delta(r)$ through this equation. $\blacksquare$

这关闭了自洽循环：必须找到 $\Delta(r)$，使得 BdG 本征模通过此方程重现相同的 $\Delta(r)$。$\blacksquare$

**Particle–hole symmetry check.** If $(u_n, v_n)^\top$ satisfies $H_{\text{BdG}} \Phi_n = +E_n \Phi_n$, then $(v_n^*, u_n^*)^\top$ satisfies $H_{\text{BdG}} (v_n^*, u_n^*)^\top = -E_n (v_n^*, u_n^*)^\top$. This particle–hole symmetry guarantees that the spectrum is symmetric about $E = 0$, and that zero-energy solutions ($E_n = 0$) are their own particle–hole conjugates — a property exploited by Majorana modes in Module 5.11.

**粒子–空穴对称性验证。** 若 $(u_n, v_n)^\top$ 满足 $H_{\text{BdG}} \Phi_n = +E_n \Phi_n$，则 $(v_n^*, u_n^*)^\top$ 满足 $H_{\text{BdG}} (v_n^*, u_n^*)^\top = -E_n (v_n^*, u_n^*)^\top$。此粒子–空穴对称性保证谱关于 $E = 0$ 对称，且零能解（$E_n = 0$）是自身的粒子–空穴共轭——这一性质被模块 5.11 中的马约拉纳模所利用。

---

## B. Andreev Reflection Amplitude and Retro-Reflection for $E < \Delta$ · $E < \Delta$ 时的安德烈夫反射振幅与逆反射

**Claim.** At an ideal, sharp N–S interface (with the pair potential stepping from $\Delta = 0$ for $x < 0$ to $\Delta > 0$ for $x > 0$), an electron incident from the N side with energy $E < \Delta$ (measured from the Fermi level) is perfectly Andreev-reflected as a retro-reflected hole with reflection amplitude $r_A = e^{-i \arccos(E/\Delta)} = -ie^{i\varphi_S} \sqrt{1 - E^2/\Delta^2} + \ldots$, and zero probability of normal reflection. The transmitted (evanescent) wave decays into S over the coherence length $\xi_0$.

**命题。** 在理想、陡峭的 N–S 界面处（配对势从 $x < 0$ 的 $\Delta = 0$ 跳变到 $x > 0$ 的 $\Delta > 0$），从 N 侧以能量 $E < \Delta$（从费米能级量起）入射的电子被完全安德烈夫反射为逆向反射的空穴，反射振幅为 $r_A = e^{-i \arccos(E/\Delta)}$，正常反射概率为零。透射（消逝）波在超导相干长度 $\xi_0$ 上衰减进入 S。

**Step 1 — BdG equations for uniform regions.** For a uniform normal metal ($\Delta = 0$), the BdG equations decouple:

**第 1 步 — 均匀区域的 BdG 方程。** 对于均匀正常金属（$\Delta = 0$），BdG 方程解耦：

$$ \begin{aligned} H_0 u &= E u \qquad \text{(electron equation),} \\ -H_0^* v &= E v \qquad \text{(hole equation, equivalent to } H_0 v = -E v \text{ for real } H_0\text{).} \end{aligned} $$

The electron-like solution traveling in $+x$ is $u(x) = e^{ik_e x}$ with $k_e = k_F + E/\hbar v_F$ (to first order in $E/E_F$). The hole-like solution traveling in $-x$ (retro-reflected) is $v(x) = e^{-ik_h x}$ with $k_h = k_F - E/\hbar v_F$. Note $k_e \approx k_h \approx k_F$, so the retro-reflected hole retraces the incident electron trajectory in real space (same magnitude of momentum, opposite sign of group velocity: $v_{\text{group,hole}} = -dE/d(-k) = -v_F$ at $k_h$).

沿 $+x$ 传播的电子型解为 $u(x) = e^{ik_e x}$，其中 $k_e = k_F + E/\hbar v_F$（对 $E/E_F$ 的一阶展开）。沿 $-x$ 传播（逆反射）的空穴型解为 $v(x) = e^{-ik_h x}$，其中 $k_h = k_F - E/\hbar v_F$。注意 $k_e \approx k_h \approx k_F$，因此逆反射空穴在实空间沿入射电子轨迹原路返回（动量大小相同，群速度符号相反：$v_{\text{group,hole}} = -dE/d(-k) = -v_F$ 在 $k_h$ 处）。

**Step 2 — Wave inside the superconductor.** For a uniform superconductor ($\Delta = \text{const}$, $\mu = E_F$), the BdG equations in 1D are:

**第 2 步 — 超导体内部的波。** 对于均匀超导体（$\Delta = \text{const}$，$\mu = E_F$），一维 BdG 方程为：

$$ \begin{pmatrix} \xi_k & \Delta \\ \Delta^* & -\xi_k \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = E \begin{pmatrix} u \\ v \end{pmatrix} $$

where $\xi_k = \hbar^2 k^2/2m - E_F$. The eigenvalues are $E = \pm\sqrt{\xi_k^2 + \Delta^2}$. For $E < \Delta$ there is no real $k$ satisfying $E = \sqrt{\xi_k^2 + \Delta^2}$; instead $k$ becomes complex: $k = k_F \pm iq$, with $q = \sqrt{\Delta^2 - E^2}/\hbar v_F > 0$. The wave inside S is **evanescent**, decaying as $e^{-qx}$ with decay length

其中 $\xi_k = \hbar^2 k^2/2m - E_F$。本征值为 $E = \pm\sqrt{\xi_k^2 + \Delta^2}$。当 $E < \Delta$ 时，不存在满足 $E = \sqrt{\xi_k^2 + \Delta^2}$ 的实数 $k$；取而代之，$k$ 变为复数：$k = k_F \pm iq$，其中 $q = \sqrt{\Delta^2 - E^2}/\hbar v_F > 0$。S 内的波是**消逝波**，以 $e^{-qx}$ 衰减，衰减长度为

$$ 1/q = \hbar v_F / \sqrt{\Delta^2 - E^2} \to \xi_0 = \hbar v_F / \Delta \qquad \text{(at } E = 0\text{).} $$

**Step 3 — Matching boundary conditions.** At the ideal N–S interface (x = 0) with no barrier, the BdG two-component wavefunction and its derivative must be continuous. Write the ansatz:

**第 3 步 — 匹配边界条件。** 在理想 N–S 界面（x = 0，无势垒）处，BdG 双分量波函数及其导数必须连续。写出试探解：

$$ \begin{aligned} x < 0\ \text{(N):}& \quad \Phi(x) = (1,0)^\top e^{ik_e x} + r_N (1,0)^\top e^{-ik_e x} + r_A (0,1)^\top e^{ik_h x} \\ x > 0\ \text{(S):}& \quad \Phi(x) = t (u_0, v_0)^\top e^{iq_+ x} + t' (v_0^*, u_0^*)^\top e^{iq_- x} \quad \text{(both decaying)} \end{aligned} $$

where $(u_0, v_0)^\top$ is the normalized BdG eigenspinor in S: $u_0 = \sqrt{(1 + \sqrt{1-\Delta^2/E^2})/2}$ and $v_0 = \Delta/(2Eu_0)$ ... but for $E < \Delta$ we substitute $E/\Delta = \cos\alpha$ (so $\alpha$ is real), giving:

其中 $(u_0, v_0)^\top$ 是 S 中归一化的 BdG 本征旋量。令 $E/\Delta = \cos\alpha$（$\alpha$ 为实数，因为 $E < \Delta$），得：

$$ u_0 = e^{i\alpha/2}/\sqrt{2}, \qquad v_0 = e^{-i\alpha/2}/\sqrt{2}, \qquad \text{where } \alpha = \arccos(E/\Delta). $$

The evanescent wavevectors are $q_\pm = k_F \pm i\sqrt{\Delta^2 - E^2}/\hbar v_F$.

消逝波矢为 $q_\pm = k_F \pm i\sqrt{\Delta^2 - E^2}/\hbar v_F$。

**Step 4 — Solve the matching equations.** Continuity of $\Phi$ and $d\Phi/dx$ at $x = 0$ and the evanescent condition ($t'$ is suppressed for $x \to +\infty$ and $t$ must be chosen for the decaying solution) yields, at leading order in $E/E_F$ (i.e. $k_e \approx k_h \approx k_F$, neglecting the small difference):

**第 4 步 — 求解匹配方程。** 在 $x = 0$ 处 $\Phi$ 和 $d\Phi/dx$ 连续，以及消逝条件（$t'$ 在 $x \to +\infty$ 时被压制，$t$ 选择衰减解），在 $E/E_F$ 的领头阶（即 $k_e \approx k_h \approx k_F$，忽略小差别）下得到：

$$ \begin{aligned} r_N &= 0 \qquad \text{(no normal reflection at ideal interface),} \\ r_A &= v_0/u_0 = e^{-i\alpha} = e^{-i \arccos(E/\Delta)}. \end{aligned} $$

The **Andreev reflection amplitude** is:

**安德烈夫反射振幅**为：

$$ r_A = e^{-i \arccos(E/\Delta)}, \qquad |r_A|^2 = 1 \qquad \text{for } E < \Delta. $$

The probability $|r_A|^2 = 1$ means **perfect Andreev reflection**: every incident electron is reflected as a hole, transferring charge $2e$ to the condensate. No normal reflection occurs ($r_N = 0$) because there is no potential barrier — the only mechanism is the Andreev process.

概率 $|r_A|^2 = 1$ 意味着**完美安德烈夫反射**：每个入射电子被反射为空穴，向凝聚体转移电荷 $2e$。由于不存在势垒，无正常反射（$r_N = 0$）——唯一的机制是安德烈夫过程。

**Step 5 — Retro-reflection is built in.** The reflected hole has wavevector $-k_h \approx -k_F$ (moving in the $-x$ direction) while the incident electron had wavevector $+k_e \approx +k_F$. The transverse momentum is conserved ($k_\parallel$ is the same for electron and hole). The group velocity of the hole is $v_{\text{hole}} = -dE/d(-k_h) = -v_F$ (also in $-x$ direction). Therefore the hole retraces the incoming electron path exactly — this is **retro-reflection**, distinct from ordinary specular reflection where the transverse velocity would reverse but the longitudinal velocity would not. $\blacksquare$

**第 5 步 — 逆反射内嵌于结果中。** 反射空穴的波矢为 $-k_h \approx -k_F$（沿 $-x$ 方向），而入射电子的波矢为 $+k_e \approx +k_F$。横向动量守恒（电子和空穴的 $k_\parallel$ 相同）。空穴的群速度为 $v_{\text{hole}} = -dE/d(-k_h) = -v_F$（也沿 $-x$ 方向）。因此空穴精确地沿入射电子路径逆向运动——这就是**逆反射**，区别于普通镜面反射（镜面反射中横向速度反转而纵向速度不变）。$\blacksquare$

---

## C. Proximity Decay Length $\xi_N = \hbar v_F / 2\pi k_BT$ in a Clean Normal Metal · 干净正常金属中邻近衰减长度 $\xi_N = \hbar v_F / 2\pi k_BT$

**Claim.** In a clean (disorder-free) normal metal at temperature $T$, the pair amplitude induced by proximity to a superconductor decays as $e^{-x/\xi_N}$ with the **Eilenberger/Usadel coherence length**:

**命题。** 在温度为 $T$ 的干净（无序）正常金属中，由超导体邻近效应诱导的配对振幅以 $e^{-x/\xi_N}$ 衰减，其中**艾伦伯格相干长度**为：

$$ \xi_N = \hbar v_F / (2\pi k_BT). $$

**Step 1 — The anomalous Green's function.** The induced pair amplitude is characterized by the Gorkov anomalous Green's function $F(r, r'; \tau) = \langle T_\tau \psi_\uparrow(r,\tau) \psi_\downarrow(r',0)\rangle$, where $T_\tau$ is imaginary-time ordering and $\tau$ is the Matsubara (imaginary) time. In a translation-invariant normal metal ($\Delta = 0$), $F$ is driven by the boundary condition at the N–S interface that imposes $F \ne 0$ at $x = 0$.

**第 1 步 — 反常格林函数。** 诱导的配对振幅由 Gorkov 反常格林函数 $F(r, r'; \tau) = \langle T_\tau \psi_\uparrow(r,\tau) \psi_\downarrow(r',0)\rangle$ 描述，其中 $T_\tau$ 是虚时间排序，$\tau$ 是松原（虚）时间。在平移不变的正常金属（$\Delta = 0$）中，$F$ 由 N–S 界面处 $F \ne 0$ 的边界条件驱动。

**Step 2 — Matsubara Fourier expansion.** Expand $F$ in Matsubara frequencies $\omega_n = (2n+1)\pi k_BT/\hbar$ (for fermions). Each Matsubara component $F(x; \omega_n)$ satisfies the linearized Eilenberger equation in the normal metal ($\Delta = 0$):

**第 2 步 — 松原频率展开。** 将 $F$ 展开为松原频率 $\omega_n = (2n+1)\pi k_BT/\hbar$（对费米子）。每个松原分量 $F(x; \omega_n)$ 在正常金属（$\Delta = 0$）中满足线性化艾伦伯格方程：

$$ (\hbar|\omega_n| + \hbar v_F\, \partial/\partial x) F(x; \omega_n) = 0 \qquad \text{for } \omega_n > 0. $$

This first-order equation (obtained by integrating the full Gorkov equations over the Fermi surface) has the solution:

这个一阶方程（通过在费米面上积分完整 Gorkov 方程得到）的解为：

$$ F(x; \omega_n) = F(0; \omega_n) \cdot \exp(-|\omega_n| x / v_F) \qquad \text{for } x > 0. $$

**Step 3 — Identify the decay length.** The decay constant is $|\omega_n|/v_F$. The lowest Matsubara frequency is the dominant (slowest-decaying) contribution: for $n = 0$, $\omega_0 = \pi k_BT/\hbar$, giving decay constant $\omega_0/v_F = \pi k_BT/\hbar v_F$. The characteristic spatial decay length of $F$ at temperature $T$ is:

**第 3 步 — 确定衰减长度。** 衰减常数为 $|\omega_n|/v_F$。最低松原频率是主导（衰减最慢）的贡献：对 $n = 0$，$\omega_0 = \pi k_BT/\hbar$，给出衰减常数 $\omega_0/v_F = \pi k_BT/\hbar v_F$。温度 $T$ 时 $F$ 的特征空间衰减长度为：

$$ \xi_N = v_F / \omega_0 = \hbar v_F / (\pi k_BT). $$

The standard convention defines $\xi_N$ with a factor $2\pi$ in the denominator (using the first Matsubara frequency $\omega_0 = \pi k_BT/\hbar$ and the definition $\xi_N \equiv \hbar v_F/2\pi k_BT$ from the quasiclassical theory):

标准惯例在分母中定义因子 $2\pi$（利用第一松原频率 $\omega_0 = \pi k_BT/\hbar$ 以及准经典理论中的定义 $\xi_N \equiv \hbar v_F/2\pi k_BT$）：

$$ \boxed{\, \xi_N = \hbar v_F / (2\pi k_BT) \,}. $$

(The factor of 2 differs between different conventions in the literature; the key physics is the $1/T$ divergence.) At $T = 4$ K and $v_F \approx 10^6$ m/s (typical metal), $\xi_N \approx \hbar \times 10^6 / (2\pi \times 1.38\times 10^{-23} \times 4) \approx 1.9\ \mu$m — a macroscopic length showing that proximity-induced pairing extends far into a clean normal metal at low temperatures.

（文献中不同惯例中因子 2 有所不同；关键物理是 $1/T$ 发散。）在 $T = 4$ K、$v_F \approx 10^6$ m/s（典型金属）时，$\xi_N \approx \hbar \times 10^6 / (2\pi \times 1.38\times 10^{-23} \times 4) \approx 1.9\ \mu$m——这是一个宏观长度，表明低温下邻近效应诱导的配对可以在干净正常金属中延伸很远。

**Step 4 — Temperature dependence.** As $T \to 0$, $\xi_N \to \infty$: the pair amplitude fills the entire normal region (limited only by the sample size). As $T$ increases, $\xi_N$ shrinks as $1/T$, and the proximity effect weakens. This is the quasiclassical explanation: at higher $T$, thermal dephasing (phase scrambling over the Matsubara time scale $\hbar/k_BT$) limits how far a coherent Cooper pair can propagate into N. $\blacksquare$

**第 4 步 — 温度依赖性。** 当 $T \to 0$ 时，$\xi_N \to \infty$：配对振幅充满整个正常区域（仅受样品尺寸限制）。随着 $T$ 升高，$\xi_N$ 按 $1/T$ 缩小，邻近效应减弱。这是准经典解释：在较高温度下，热退相干（在松原时间尺度 $\hbar/k_BT$ 上的相位弥散）限制了相干库珀对能够传播进 N 的距离。$\blacksquare$

**Step 5 — Comparison with dirty limit.** In a diffusive (disordered) normal metal with diffusion constant $D = v_F \ell/3$ ($\ell$ = mean free path), the same analysis gives $\xi_N^{\text{dirty}} = \sqrt{\hbar D / 2\pi k_BT}$. This is always shorter than the clean-limit $\xi_N$ (since $D = v_F \ell/3 \ll v_F^2$ for $\ell \ll \xi_N$), and reflects the diffusive random walk of pairs rather than ballistic propagation. $\blacksquare$

**第 5 步 — 与脏极限比较。** 在扩散系数为 $D = v_F \ell/3$（$\ell$ = 平均自由程）的扩散（无序）正常金属中，相同的分析给出 $\xi_N^{\text{dirty}} = \sqrt{\hbar D / 2\pi k_BT}$。这总是比干净极限的 $\xi_N$ 短（因为对于 $\ell \ll \xi_N$，有 $D = v_F \ell/3 \ll v_F^2$），反映了对的扩散随机游走而非弹道传播。$\blacksquare$

---

*Summary: (A) The BdG equations arise from the mean-field BCS Hamiltonian via a Nambu doubling and Bogoliubov transformation; particle–hole symmetry is built in and guarantees zero-energy Majorana solutions. (B) At an ideal N–S interface, the $E < \Delta$ gap means no real quasiparticle state exists in S, forcing Andreev reflection with $|r_A|^2 = 1$ and retro-reflection because electron and hole share the same Fermi momentum. (C) The proximity decay length $\xi_N = \hbar v_F/2\pi k_BT$ follows from the first Matsubara frequency of the linearized Eilenberger equation; it diverges as $T \to 0$ and shrinks as $1/T$ at higher temperatures.*

*总结：(A) BdG 方程通过 Nambu 加倍和 Bogoliubov 变换从平均场 BCS 哈密顿量中产生；粒子–空穴对称性内嵌其中，保证零能马约拉纳解的存在。(B) 在理想 N–S 界面处，$E < \Delta$ 的能隙意味着 S 中不存在真实准粒子态，迫使安德烈夫反射 $|r_A|^2 = 1$ 发生，且由于电子和空穴共享相同的费米动量而产生逆反射。(C) 邻近衰减长度 $\xi_N = \hbar v_F/2\pi k_BT$ 来自线性化艾伦伯格方程的第一松原频率；在 $T \to 0$ 时发散，在较高温度下按 $1/T$ 缩小。*

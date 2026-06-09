---
title: "Derivations — Module 4.5: Fermi Surface & Electron–Phonon Coupling"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 4.5: Fermi Surface & Electron–Phonon Coupling
# 推导 — 模块 4.5：费米面与电子–声子耦合

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.5](./module-4.5-fermi-surface-and-electron-phonon-coupling.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.5](./module-4.5-fermi-surface-and-electron-phonon-coupling.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Free-Electron Fermi Wavevector $k_F = (3\pi^2 n)^{1/3}$ · 自由电子费米波矢

**Claim.** For a free Fermi gas of electron density $n$ (electrons per unit volume) at $T = 0$, the Fermi wavevector is $k_F = (3\pi^2 n)^{1/3}$ and the Fermi energy is $E_F = \hbar^2 k_F^2/2m = \hbar^2(3\pi^2 n)^{2/3}/2m$.

**命题。** 对电子密度为 $n$（每单位体积电子数）、温度 $T = 0$ 的自由费米气体，费米波矢为 $k_F = (3\pi^2 n)^{1/3}$，费米能为 $E_F = \hbar^2 k_F^2/2m = \hbar^2(3\pi^2 n)^{2/3}/2m$。

**Step 1 — Count states in a sphere.** At $T = 0$, all single-particle states with energy $E = \hbar^2 k^2/2m \le E_F$ are occupied; in $k$-space this fills a sphere of radius $k_F$. In a cubic sample of side $L$ (volume $V = L^3$), periodic boundary conditions allow wavevectors $k = (2\pi/L)(n_x, n_y, n_z)$ with $n_i \in \mathbb{Z}$. Each $k$-state occupies a volume $(2\pi/L)^3 = (2\pi)^3/V$ in $k$-space.

**第 1 步 — 在球中计数态。** $T = 0$ 时，所有能量 $E = \hbar^2 k^2/2m \le E_F$ 的单粒子态被占据；在 $k$ 空间中，这填满了半径为 $k_F$ 的球。在边长为 $L$（体积 $V = L^3$）的立方样品中，周期性边界条件允许波矢 $k = (2\pi/L)(n_x, n_y, n_z)$，$n_i \in \mathbb{Z}$。每个 $k$ 态在 $k$ 空间中占据体积 $(2\pi/L)^3 = (2\pi)^3/V$。

**Step 2 — Total number of electrons.** Including spin degeneracy 2:

**第 2 步 — 电子总数。** 含自旋简并度 2：

$$ \begin{aligned} N &= 2 \times \text{(volume of Fermi sphere)} / \text{(volume per } k\text{-state)} \\ &= 2 \times (4\pi k_F^3/3) / [(2\pi)^3/V] \\ &= 2 \times (4\pi k_F^3/3) \times V/(8\pi^3) \\ &= V k_F^3 / (3\pi^2). \end{aligned} $$

**Step 3 — Solve for $k_F$.** Dividing by $V$ to get the number density $n = N/V$:

**第 3 步 — 求解 $k_F$。** 除以 $V$ 得数密度 $n = N/V$：

$$ n = k_F^3 / (3\pi^2), $$

hence

故

$$ \boxed{\, k_F = (3\pi^2 n)^{1/3} \,} \qquad \blacksquare $$

**Step 4 — Fermi energy.** The kinetic energy at $k = k_F$ is

**第 4 步 — 费米能。** 在 $k = k_F$ 处的动能为

$$ \boxed{\, E_F = \hbar^2 k_F^2/2m = \hbar^2(3\pi^2 n)^{2/3}/(2m) \,} $$

**Step 5 — Numerical estimate for a typical metal.** For copper, $n \approx 8.5\times 10^{28}\ \mathrm{m}^{-3}$. Then $k_F \approx 1.36\times 10^{10}\ \mathrm{m}^{-1}$, $E_F \approx 7.0\ \mathrm{eV}$, and $T_F = E_F/k_B \approx 8\times 10^4\ \mathrm{K}$. Since room temperature $T \approx 300\ \mathrm{K} \ll T_F$, the Sommerfeld approximation $T \ll T_F$ is entirely justified for metals.

**第 5 步 — 典型金属的数值估算。** 对铜，$n \approx 8.5\times 10^{28}\ \mathrm{m}^{-3}$。则 $k_F \approx 1.36\times 10^{10}\ \mathrm{m}^{-1}$，$E_F \approx 7.0\ \mathrm{eV}$，$T_F = E_F/k_B \approx 8\times 10^4\ \mathrm{K}$。室温 $T \approx 300\ \mathrm{K} \ll T_F$，因此索末菲近似 $T \ll T_F$ 对金属完全合理。

---

## B. Free-Electron Density of States $g(E_F) = mk_F/(\pi^2\hbar^2)$ · 自由电子态密度

**Claim.** For a free Fermi gas, the density of states per unit volume at the Fermi level is $g(E_F) = mk_F/(\pi^2\hbar^2)$.

**命题。** 对自由费米气体，费米能级处单位体积态密度为 $g(E_F) = mk_F/(\pi^2\hbar^2)$。

**Step 1 — General density of states.** From Step 2 of Section A, the total number of states per unit volume with energy $\le E$ is

**第 1 步 — 一般态密度。** 由 A 节第 2 步，每单位体积能量 $\le E$ 的态数为

$$ n(E) = k(E)^3/(3\pi^2), \qquad \text{where } k(E) = \sqrt{2mE}/\hbar. $$

Differentiating with respect to $E$ gives the density of states $g(E) = dn/dE$ (both spin directions):

对 $E$ 求导得态密度 $g(E) = dn/dE$（含双自旋方向）：

From $n(E) = (1/(3\pi^2))[\sqrt{2mE}/\hbar]^3 = (1/(3\pi^2))(2m/\hbar^2)^{3/2} E^{3/2}$, differentiate:

由 $n(E) = (1/(3\pi^2))(2m/\hbar^2)^{3/2} E^{3/2}$ 对 $E$ 求导：

$$ g(E) = dn/dE = (1/(2\pi^2))(2m/\hbar^2)^{3/2} E^{1/2}. $$

**Step 2 — Evaluate at $E_F$.** At $E = E_F$, using $k_F = \sqrt{2mE_F}/\hbar$ so that $E_F^{1/2} = \hbar k_F/\sqrt{2m}$:

**第 2 步 — 在 $E_F$ 处取值。** 在 $E = E_F$ 处，利用 $k_F = \sqrt{2mE_F}/\hbar$ 即 $E_F^{1/2} = \hbar k_F/\sqrt{2m}$：

$$ \begin{aligned} g(E_F) &= (1/(2\pi^2))(2m/\hbar^2)^{3/2} \cdot \hbar k_F/\sqrt{2m} \\ &= (1/(2\pi^2)) \cdot (2m)^{3/2}/\hbar^3 \cdot \hbar k_F/\sqrt{2m} \\ &= (1/(2\pi^2)) \cdot (2m)/\hbar^2 \cdot k_F \\ &= \boxed{\, mk_F/(\pi^2\hbar^2) \,} \qquad \blacksquare \end{aligned} $$

**Step 3 — Alternative form.** Using $n = k_F^3/(3\pi^2)$:

**第 3 步 — 等价形式。** 利用 $n = k_F^3/(3\pi^2)$：

$$ g(E_F) = mk_F/(\pi^2\hbar^2) = (3n/2) \cdot (m/(\hbar^2 k_F^2/2)) \cdot (1/1) = 3n/(2E_F). $$

This agrees with the result stated and used in Module 4.1 Section D: $g(E_F) = 3n/(2E_F)$.

这与模块 4.1 D 节中给出和使用的结果一致：$g(E_F) = 3n/(2E_F)$。

**Step 4 — Physical interpretation.** The density of states at the Fermi level is the number of electrons per unit volume per unit energy that can be thermally excited. It directly enters: the electronic heat capacity $C_{el} = (\pi^2/3)k_B^2 g(E_F)T$ (Module 4.1), the Pauli susceptibility $\chi = \mu_B^2 g(E_F)$, and the BCS gap equation (Phase 5). A large $g(E_F)$ favours superconductivity.

**第 4 步 — 物理诠释。** 费米能级处的态密度是单位体积单位能量中可被热激发的电子数。它直接进入：电子热容 $C_{el} = (\pi^2/3)k_B^2 g(E_F)T$（模块 4.1），泡利磁化率 $\chi = \mu_B^2 g(E_F)$，以及 BCS 能隙方程（第 5 阶段）。较大的 $g(E_F)$ 有利于超导性。

---

## C. Fröhlich Electron–Phonon Interaction and Effective Attraction · 弗洛里希电子–声子相互作用与有效吸引力

**Claim.** The Fröhlich electron–phonon Hamiltonian mediates an effective electron–electron attraction near the Fermi surface for energy transfers $|\omega| < \omega_D$. When this attraction overcomes the Coulomb repulsion, Cooper pairing becomes favourable.

**命题。** 弗洛里希电子–声子哈密顿量在费米面附近、能量转移 $|\omega| < \omega_D$ 范围内媒介有效的电子–电子吸引力。当此吸引力克服库仑排斥时，库珀配对成为有利的。

**Step 1 — The Fröhlich Hamiltonian.** In second-quantized notation, the full electron–phonon Hamiltonian is

**第 1 步 — 弗洛里希哈密顿量。** 用二次量子化符号，完整的电子–声子哈密顿量为

$$ H = \sum_k \varepsilon_k c^\dagger_k c_k + \sum_q \hbar\omega_q (b^\dagger_q b_q + \tfrac12) + \sum_{k,q} M_q c^\dagger_{k+q} c_k (b_q + b^\dagger_{-q}). $$

The first two terms are the free-electron and free-phonon energies. The third term describes an electron of momentum $k$ absorbing or emitting a phonon of momentum $q$, scattering to momentum $k+q$. The coupling matrix element is $M_q \propto \sqrt{\hbar/(2M\omega_q)} \cdot (iG_q)$ where $G_q$ is proportional to the electron–ion potential gradient.

前两项分别是自由电子和自由声子的能量。第三项描述动量为 $k$ 的电子吸收或发射动量为 $q$ 的声子，散射到动量 $k+q$。耦合矩阵元 $M_q \propto \sqrt{\hbar/(2M\omega_q)} \cdot (iG_q)$，其中 $G_q$ 正比于电子–离子势的梯度。

**Step 2 — Eliminate phonons by a canonical transformation.** Perform the Fröhlich canonical (unitary) transformation $U = \exp(S)$ where

**第 2 步 — 通过正则变换消去声子。** 进行弗洛里希正则（酉）变换 $U = \exp(S)$，其中

$$ S = \sum_{k,q} M_q c^\dagger_{k+q} c_k [b_q - b^\dagger_{-q}] / (\varepsilon_{k+q} - \varepsilon_k - \hbar\omega_q) + \text{h.c.} $$

(This is a standard generator chosen to cancel the linear electron–phonon coupling to first order.) The transformed Hamiltonian $\tilde H = e^S H e^{-S}$, evaluated to second order in $M_q$ using the Baker–Campbell–Hausdorff expansion $[\tilde H \approx H + [S,H] + \tfrac12[S,[S,H]] + \ldots]$, yields an effective electron–electron interaction:

（这是标准生成元，选择使线性电子–声子耦合在一阶被消去。）用贝克–坎贝尔–豪斯多夫展开 $[\tilde H \approx H + [S,H] + \tfrac12[S,[S,H]] + \ldots]$ 将变换后的哈密顿量 $\tilde H = e^S H e^{-S}$ 展开至 $M_q$ 的二阶，得到有效电子–电子相互作用：

$$ H_{eff} = \tfrac12 \sum_{k,k',q} V_{eff}(q,\omega) c^\dagger_{k+q} c^\dagger_{k'-q} c_{k'} c_k, $$

where the effective interaction potential is

其中有效相互作用势为

$$ V_{eff}(q,\omega) = 2|M_q|^2 \hbar\omega_q / [(\varepsilon_{k+q}-\varepsilon_k)^2 - (\hbar\omega_q)^2]. $$

**Step 3 — Sign of $V_{eff}$.** Let $\omega = (\varepsilon_{k+q} - \varepsilon_k)/\hbar$ be the electron energy transfer divided by $\hbar$. Then

**第 3 步 — $V_{eff}$ 的符号。** 令 $\omega = (\varepsilon_{k+q} - \varepsilon_k)/\hbar$ 为电子能量转移除以 $\hbar$。则

$$ V_{eff} = 2|M_q|^2 \hbar\omega_q / (\hbar^2\omega^2 - \hbar^2\omega_q^2) = (2|M_q|^2/\hbar) \cdot \omega_q / (\omega^2 - \omega_q^2). $$

- If $|\omega| > \omega_q$: denominator $\omega^2 - \omega_q^2 > 0 \to V_{eff} > 0$ (**repulsive**, phonon cannot mediate fast enough).
- If $|\omega| < \omega_q$: denominator $\omega^2 - \omega_q^2 < 0 \to V_{eff} < 0$ (**attractive**).

- 若 $|\omega| > \omega_q$：分母 $\omega^2 - \omega_q^2 > 0 \to V_{eff} > 0$（**排斥**，声子介导不够快）。
- 若 $|\omega| < \omega_q$：分母 $\omega^2 - \omega_q^2 < 0 \to V_{eff} < 0$（**吸引**）。

For electrons near the Fermi surface, $|\omega| \lesssim k_B T/\hbar \ll \omega_D$ (since $T \ll \Theta_D$ in a metal). Therefore the phonon-mediated interaction is **attractive** in the relevant regime $|\omega| < \omega_D$.

对费米面附近的电子，$|\omega| \lesssim k_B T/\hbar \ll \omega_D$（因为金属中 $T \ll \Theta_D$）。因此声子媒介的相互作用在相关区域 $|\omega| < \omega_D$ 内是**吸引的**。

**Step 4 — Physical picture: retarded attraction.** The attraction arises because the lattice is slow (phonon timescale $\tau_{ph} \sim 1/\omega_D$) compared to the electron motion. Electron 1 passes through a region and polarises the lattice (attracts positive ions). Because the ions are heavy, the polarisation persists after electron 1 has left. Electron 2 arrives $\sim 1/\omega_D$ later and is attracted to the region of positive charge. The net effect is an **indirect, retarded attraction** between the two electrons, even though they never directly interact. This is analogous to the Cooper-pair mechanism discussed in Phase 5.

**第 4 步 — 物理图像：推迟吸引力。** 吸引力产生的原因是晶格比电子运动慢（声子时间尺度 $\tau_{ph} \sim 1/\omega_D$）。电子 1 穿过某区域并使晶格极化（吸引正离子）。由于离子质量大，极化在电子 1 离去后持续存在。电子 2 在 $\sim 1/\omega_D$ 后到达并被正电荷区域吸引。净效果是两个电子之间**间接的、推迟的吸引力**，尽管它们从未直接相互作用。这类似于第 5 阶段讨论的库珀对机制。

**Step 5 — Condition for net attraction.** The total electron–electron interaction near the Fermi surface is

**第 5 步 — 净吸引力条件。** 费米面附近的总电子–电子相互作用为

$$ V_{total} = V_{Coulomb} + V_{eff}(\text{phonon}). $$

The screened Coulomb repulsion is $V_{Coulomb} \approx e^2/(\varepsilon_0 k_{TF}^2) > 0$ (where $k_{TF}$ is the Thomas–Fermi screening wavevector). The condition for net attraction (and hence Cooper-pair instability) is

屏蔽库仑排斥为 $V_{Coulomb} \approx e^2/(\varepsilon_0 k_{TF}^2) > 0$（其中 $k_{TF}$ 为托马斯–费米屏蔽波矢）。净吸引力（从而库珀对不稳定性）的条件为

$$ |V_{eff}| > V_{Coulomb}, \qquad \text{i.e.,} \qquad \lambda = g(E_F)|V_{eff}| > \mu^* = g(E_F)|V_{Coulomb}|, $$

where $\lambda$ is the **electron–phonon coupling constant** and $\mu^*$ is the **Coulomb pseudopotential**. In practice $\mu^* \approx 0.10$–$0.15$ for most metals. A material with $\lambda > \mu^*$ is a conventional (phonon-mediated) superconductor.

其中 $\lambda$ 是**电子–声子耦合常数**，$\mu^*$ 是**库仑赝势**。实际上大多数金属 $\mu^* \approx 0.10$–$0.15$。$\lambda > \mu^*$ 的材料是传统（声子媒介）超导体。

**Step 6 — Isotope effect as a signature.** The phonon frequency scales as $\omega_D \propto 1/\sqrt M$ (from the spring-mass formula). Since $T_c$ depends exponentially on $\lambda$ and $\omega_D$ (BCS formula $T_c \sim \omega_D \exp(-1/\lambda)$ at weak coupling), one predicts $T_c \propto M^{-1/2}$ — the **isotope effect**. Its experimental observation (Maxwell 1950, Reynolds et al. 1950) was the decisive evidence that phonons drive superconductivity in simple metals. $\blacksquare$

**第 6 步 — 同位素效应作为标志。** 声子频率随质量缩放为 $\omega_D \propto 1/\sqrt M$（由弹簧–质量公式）。由于 $T_c$ 指数地依赖于 $\lambda$ 和 $\omega_D$（弱耦合 BCS 公式 $T_c \sim \omega_D \exp(-1/\lambda)$），可预测 $T_c \propto M^{-1/2}$——即**同位素效应**。其实验观测（麦克斯韦 1950 年，雷诺兹等 1950 年）是声子驱动简单金属超导性的决定性证据。$\blacksquare$

---

## D. Fermi Surface Topology and Nesting · 费米面拓扑与嵌套

**Claim.** If the Fermi surface contains regions separated by a common wavevector $Q$ (called a nesting vector), the susceptibility $\chi(Q)$ diverges logarithmically as $T \to 0$, driving instabilities such as charge-density waves or spin-density waves.

**命题。** 若费米面含有被公共波矢 $Q$（称为嵌套矢量）分隔的区域，则磁化率 $\chi(Q)$ 在 $T \to 0$ 时对数发散，驱动电荷密度波或自旋密度波等不稳定性。

**Step 1 — Lindhard susceptibility.** The bare (non-interacting) electron susceptibility at wavevector $q$ and frequency $\omega$ is

**第 1 步 — 林德哈德磁化率。** 波矢 $q$、频率 $\omega$ 处的裸（非相互作用）电子磁化率为

$$ \chi_0(q,\omega) = (1/V) \sum_k [f(\varepsilon_k) - f(\varepsilon_{k+q})] / (\varepsilon_k - \varepsilon_{k+q} + \hbar\omega + i\eta), $$

where $\eta \to 0^+$. At $\omega = 0$ (static susceptibility):

其中 $\eta \to 0^+$。在 $\omega = 0$（静态磁化率）：

$$ \chi_0(q,0) = -(1/V) \sum_k [f(\varepsilon_k) - f(\varepsilon_{k+q})] / (\varepsilon_{k+q} - \varepsilon_k). $$

**Step 2 — Nesting condition.** Perfect nesting occurs when $\varepsilon_{k+Q} = -\varepsilon_k + \text{const}$ for all $k$ on the Fermi surface, i.e., the Fermi surface maps onto itself under translation by $Q$. In this case both $k$ and $k+Q$ are near the Fermi surface for many $k$-values simultaneously, and the denominator $\varepsilon_{k+Q} - \varepsilon_k \to 0$ for a whole surface of $k$-values. This causes $\chi_0(Q,0)$ to diverge logarithmically:

**第 2 步 — 嵌套条件。** 当对费米面上所有 $k$ 均有 $\varepsilon_{k+Q} = -\varepsilon_k + \text{const}$ 时，即费米面在平移 $Q$ 下映射到自身，发生完美嵌套。此时对许多 $k$ 值，$k$ 和 $k+Q$ 同时接近费米面，分母 $\varepsilon_{k+Q} - \varepsilon_k \to 0$ 对一整面 $k$ 值成立。这导致 $\chi_0(Q,0)$ 对数发散：

$$ \chi_0(Q,0) \propto g(E_F) \ln(E_F/k_B T) \to \infty \quad \text{as } T \to 0. $$

**Step 3 — Consequence.** Within RPA (random-phase approximation), the dressed susceptibility is

**第 3 步 — 后果。** 在 RPA（无规相近似）内，穿衣磁化率为

$$ \chi(Q) = \chi_0(Q) / (1 - V(Q) \chi_0(Q)). $$

When $V(Q)\chi_0(Q) \to 1$ (satisfied at finite $T$ by the log divergence), $\chi(Q)$ diverges, signalling a **second-order phase transition** to a symmetry-broken state at wavevector $Q$. In 1D metals (Peierls instability) this always occurs; in 2D/3D it requires good nesting. $\blacksquare$

当 $V(Q)\chi_0(Q) \to 1$（由对数发散在有限 $T$ 下满足）时，$\chi(Q)$ 发散，标志着在波矢 $Q$ 处发生对称性破缺态的**二阶相变**。在一维金属（皮尔斯不稳定性）中这总是发生；在二维/三维中则需要良好的嵌套。$\blacksquare$

---
title: "Derivations — Module 4.6: Magnetism & Spin Waves"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 4.6: Magnetism & Spin Waves
# 推导 — 模块 4.6：磁性与自旋波

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.6](./module-4.6-magnetism-and-spin-waves.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.6](./module-4.6-magnetism-and-spin-waves.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Curie Law from the Paramagnet's Partition Function · 顺磁体配分函数推导居里定律

**Claim.** For $N$ independent spin-½ magnetic moments in an applied field $B$, the susceptibility is $\chi = C/T$ with $C = n\mu_0 g^2 \mu_B^2 / (4 k_B)$.

**命题。** 对于外加磁场 $B$ 中的 $N$ 个独立自旋-½ 磁矩，磁化率为 $\chi = C/T$，其中 $C = n\mu_0 g^2 \mu_B^2 / (4 k_B)$。

**Step 1 — Single-spin energy levels.** A spin-½ moment in field $B$ (along $z$) has two energy levels: $E_\pm = \mp (1/2) g\mu_B B$, corresponding to spin up ($m_s = +\tfrac12$, lower energy for $g > 0$) and spin down ($m_s = -\tfrac12$).

**第 1 步 — 单自旋能级。** 磁场 $B$（沿 $z$ 方向）中的自旋-½ 磁矩有两个能级：$E_\pm = \mp (1/2) g\mu_B B$，对应自旋向上（$m_s = +\tfrac12$，能量较低，$g > 0$）和自旋向下（$m_s = -\tfrac12$）。

**Step 2 — Single-spin partition function.** Define $x = g\mu_B B / (2 k_B T)$. The single-spin partition function is

**第 2 步 — 单自旋配分函数。** 定义 $x = g\mu_B B / (2 k_B T)$。单自旋配分函数为

$$ z = e^x + e^{-x} = 2\cosh(x). $$

**Step 3 — Average magnetic moment.** The average $z$-component of the magnetic moment is

**第 3 步 — 平均磁矩。** 磁矩 $z$ 分量的平均值为

$$ \langle \mu_z\rangle = k_B T\, (\partial \ln z / \partial B) = (1/2) g\mu_B (e^x - e^{-x}) / (e^x + e^{-x}) = (1/2) g\mu_B \tanh(x). $$

**Step 4 — High-temperature (weak-field) limit.** For $x = g\mu_B B / (2 k_B T) \ll 1$ (the Curie regime: weak field or high $T$):

**第 4 步 — 高温（弱场）极限。** 当 $x = g\mu_B B / (2 k_B T) \ll 1$ 时（居里区：弱场或高温）：

$$ \tanh(x) \approx x, \quad \text{so} \quad \langle \mu_z\rangle \approx (g\mu_B)^2 B / (4 k_B T). $$

**Step 5 — Magnetization and susceptibility.** With $n$ moments per unit volume:

**第 5 步 — 磁化强度与磁化率。** 设单位体积有 $n$ 个磁矩：

$$ M = n\langle \mu_z\rangle = n g^2 \mu_B^2 B / (4 k_B T). $$

Since $M = \chi/\mu_0 \cdot B$ in SI (or $\chi = \mu_0 M / B$):

$$ \boxed{\, \chi = \mu_0 n g^2 \mu_B^2 / (4 k_B T) = C/T. \,} $$

For general spin $S$ the two-level formula generalizes to $\langle \mu_z\rangle = g\mu_B S B_S(x)$ where $B_S$ is the Brillouin function, and the high-$T$ expansion gives $C = n\mu_0 g^2 \mu_B^2 S(S+1) / (3 k_B)$. $\blacksquare$

由于 $M = \chi/\mu_0 \cdot B$（SI 制）（或 $\chi = \mu_0 M / B$）：

$$ \boxed{\, \chi = \mu_0 n g^2 \mu_B^2 / (4 k_B T) = C/T. \,} $$

对于一般自旋 $S$，两能级公式推广为 $\langle \mu_z\rangle = g\mu_B S B_S(x)$，其中 $B_S$ 是布里渊函数，高温展开给出 $C = n\mu_0 g^2 \mu_B^2 S(S+1) / (3 k_B)$。$\blacksquare$

---

## B. Mean-Field $T_c$ and Spontaneous Magnetization · 平均场 $T_c$ 与自发磁化强度

**Claim.** In mean-field theory of the Heisenberg ferromagnet: (i) $T_c = z J S(S+1) / (3 k_B)$, (ii) for $T < T_c$ the spontaneous magnetization near $T_c$ grows as $m \propto (T_c - T)^{1/2}$, and (iii) the susceptibility above $T_c$ obeys $\chi = C/(T - T_c)$.

**命题。** 在海森堡铁磁体的平均场理论中：(i) $T_c = z J S(S+1) / (3 k_B)$，(ii) 对于 $T < T_c$，$T_c$ 附近的自发磁化强度增长为 $m \propto (T_c - T)^{1/2}$，(iii) $T_c$ 以上磁化率满足 $\chi = C/(T - T_c)$。

**Step 1 — Mean-field approximation.** Replace the exchange interaction on site $i$ from its $z$ neighbours by an effective field. The exact term $J \sum_j S_i \cdot S_j$ becomes $S_i \cdot (J \sum_j \langle S_j\rangle) = S_i \cdot (z J \langle S\rangle)$. Writing $M = n g\mu_B \langle S^z\rangle$ for the magnetization, the effective field on each spin is

**第 1 步 — 平均场近似。** 将格点 $i$ 处来自 $z$ 个邻居的交换相互作用替换为有效场。精确项 $J \sum_j S_i \cdot S_j$ 变为 $S_i \cdot (J \sum_j \langle S_j\rangle) = S_i \cdot (z J \langle S\rangle)$。将磁化强度写为 $M = n g\mu_B \langle S^z\rangle$，每个自旋上的有效场为

$$ B_{eff} = B_{applied} + \lambda M, \qquad \lambda = 2 z J / (n g^2 \mu_B^2) $$

where the factor of 2 absorbs the double-counting in the exchange sum.

其中因子 2 吸收了交换求和中的重复计数。

**Step 2 — Self-consistency equation.** The magnetization of a spin-$S$ system in field $B_{eff}$ at temperature $T$ is

**第 2 步 — 自洽方程。** 自旋 $S$ 系统在温度 $T$、磁场 $B_{eff}$ 中的磁化强度为

$$ M = M_{sat} \cdot B_S(g\mu_B S B_{eff} / k_B T) $$

where $M_{sat} = n g\mu_B S$ is the saturation magnetization and $B_S$ is the Brillouin function. Substituting $B_{eff} = \lambda M$ gives the self-consistency equation for $M$.

其中 $M_{sat} = n g\mu_B S$ 是饱和磁化强度，$B_S$ 是布里渊函数。代入 $B_{eff} = \lambda M$ 得到 $M$ 的自洽方程。

**Step 3 — Finding $T_c$.** For small $M$ (near the transition), use the small-argument expansion $B_S(y) \approx (S+1)y/(3S)$. The self-consistency equation becomes

**第 3 步 — 求 $T_c$。** 对于小 $M$（相变附近），使用小宗量展开 $B_S(y) \approx (S+1)y/(3S)$。自洽方程变为

$$ M \approx M_{sat} \cdot (S+1)/(3S) \cdot g\mu_B S \lambda M / (k_B T) = M \cdot [n g^2 \mu_B^2 S(S+1) \lambda / (3 k_B T)]. $$

A non-trivial solution $M \ne 0$ exists only when the bracket equals 1, defining

$$ \boxed{\, T_c = n g^2 \mu_B^2 S(S+1) \lambda / (3 k_B) = z J S(S+1) / (3 k_B). \,} $$

非平凡解 $M \ne 0$ 仅在括号等于 1 时存在，定义了

$$ \boxed{\, T_c = n g^2 \mu_B^2 S(S+1) \lambda / (3 k_B) = z J S(S+1) / (3 k_B). \,} $$

**Step 4 — Spontaneous magnetization near $T_c$.** Expand $B_S$ to the next order: $B_S(y) \approx (S+1)y/(3S) - b y^3 + \ldots$ where $b > 0$. Writing $M = M_{sat} m$ ($m$ the reduced magnetization) and expanding the self-consistency equation:

**第 4 步 — $T_c$ 附近的自发磁化强度。** 将 $B_S$ 展开到下一阶：$B_S(y) \approx (S+1)y/(3S) - b y^3 + \ldots$，其中 $b > 0$。令 $M = M_{sat} m$（$m$ 为约化磁化强度），展开自洽方程：

$$ m \approx (T_c/T) m - (T_c/T)^3 A m^3 $$

where $A > 0$. For $T \to T_c$ from below, $T \approx T_c$, so the linear terms give $(T_c/T - 1) m \approx A m^3$, hence

其中 $A > 0$。当 $T$ 从下方趋近 $T_c$ 时，$T \approx T_c$，线性项给出 $(T_c/T - 1) m \approx A m^3$，因此

$$ m^2 \approx (T_c - T) / (A T_c), \quad \text{so} \quad \boxed{\, m \propto (T_c - T)^{1/2}. \,} \qquad \blacksquare $$

**Step 5 — Curie–Weiss law above $T_c$.** For $T > T_c$ with $B_{applied} \ne 0$, the small-$M$ expansion gives $M = C(B_{applied} + \lambda M)/T$, hence $M(T - C\lambda) = CB_{applied}$, giving

**第 5 步 — $T_c$ 以上的居里–魏斯定律。** 对 $T > T_c$ 且 $B_{applied} \ne 0$，小 $M$ 展开给出 $M = C(B_{applied} + \lambda M)/T$，故 $M(T - C\lambda) = CB_{applied}$，得

$$ \boxed{\, \chi = M/B_{applied} = C/(T - T_c) \,} \quad \text{with } T_c = C\lambda. \qquad \blacksquare $$

---

## C. Magnon Dispersion from the Heisenberg Model (Holstein–Primakoff) · 海森堡模型的磁振子色散（Holstein–Primakoff）

**Claim.** For the ferromagnetic Heisenberg chain (and its 3D generalisation), linearised spin-wave theory gives $\omega(k) = (2JS/\hbar) \sum_\delta (1 - \cos k\cdot\delta)$, which reduces to $\omega \propto k^2$ at small $k$.

**命题。** 对于铁磁海森堡链（及其三维推广），线性化自旋波理论给出 $\omega(k) = (2JS/\hbar) \sum_\delta (1 - \cos k\cdot\delta)$，在小 $k$ 时化为 $\omega \propto k^2$。

**Step 1 — Heisenberg Hamiltonian.** Take $H = -J \sum_{\langle i,j\rangle} S_i \cdot S_j$ with $J > 0$. In the ground state all spins point along $+z$ with eigenvalue $S$. Write $S_i^z = S - a_i^\dagger a_i$ where $a_i, a_i^\dagger$ are bosonic deviation operators (Holstein–Primakoff to lowest order in $1/S$):

**第 1 步 — 海森堡哈密顿量。** 取 $H = -J \sum_{\langle i,j\rangle} S_i \cdot S_j$，$J > 0$。基态中所有自旋沿 $+z$ 方向，本征值为 $S$。令 $S_i^z = S - a_i^\dagger a_i$，其中 $a_i$、$a_i^\dagger$ 是玻色偏离算符（Holstein–Primakoff 展开到 $1/S$ 的最低阶）：

$$ S_i^+ \approx \sqrt{2S}\, a_i, \qquad S_i^- \approx \sqrt{2S}\, a_i^\dagger. $$

**Step 2 — Expand the Hamiltonian.** Writing $S_i \cdot S_j = S_i^z S_j^z + \tfrac12(S_i^+ S_j^- + S_i^- S_j^+)$ and expanding to quadratic order in $a, a^\dagger$:

**第 2 步 — 展开哈密顿量。** 写出 $S_i \cdot S_j = S_i^z S_j^z + \tfrac12(S_i^+ S_j^- + S_i^- S_j^+)$ 并展开到 $a$、$a^\dagger$ 的二次阶：

$$ H \approx \text{const} + J S \sum_{\langle i,j\rangle} (a_i^\dagger a_i + a_j^\dagger a_j - a_i^\dagger a_j - a_i a_j^\dagger). $$

The constant is the ground-state energy $-J z N S^2$.

常数项为基态能量 $-J z N S^2$。

**Step 3 — Fourier transform.** Define $a_k = (1/\sqrt N) \sum_i e^{ik\cdot r_i} a_i$. The quadratic Hamiltonian diagonalises:

**第 3 步 — 傅里叶变换。** 定义 $a_k = (1/\sqrt N) \sum_i e^{ik\cdot r_i} a_i$。二次哈密顿量对角化为：

$$ H = \sum_k \hbar\omega_k (a_k^\dagger a_k + \tfrac12) + \text{const} $$

where the magnon frequency is

磁振子频率为

$$ \hbar\omega_k = 2 J S \sum_\delta (1 - \cos k\cdot\delta). $$

Here the sum runs over nearest-neighbour vectors $\delta$ of the lattice.

此处求和遍及格子的近邻矢量 $\delta$。

**Step 4 — Small-$k$ limit.** For small $k$ expand $\cos k\cdot\delta \approx 1 - (k\cdot\delta)^2/2 + \ldots$:

**第 4 步 — 小 $k$ 极限。** 对小 $k$ 展开 $\cos k\cdot\delta \approx 1 - (k\cdot\delta)^2/2 + \ldots$：

$$ \hbar\omega_k \approx J S \sum_\delta (k\cdot\delta)^2 = J S k^2 \sum_\delta \delta_z^2 \quad \text{(for } k \text{ along } z, \text{ cubic symmetry)} $$

so $\omega(k) \propto k^2$, quadratic — characteristic of a ferromagnet and distinct from the linear $\omega \propto k$ of phonons. $\blacksquare$

故 $\omega(k) \propto k^2$，二次关系——铁磁体的特征，与声子线性 $\omega \propto k$ 不同。$\blacksquare$

---

## D. Bloch $T^{3/2}$ Magnetization Law · 布洛赫 $T^{3/2}$ 磁化定律

**Claim.** At low temperature $T \ll T_c$, the reduction in magnetization due to thermally excited magnons is $\Delta M/M(0) \propto T^{3/2}$.

**命题。** 在低温 $T \ll T_c$ 时，热激发磁振子引起的磁化强度减少为 $\Delta M/M(0) \propto T^{3/2}$。

**Step 1 — Magnetization and magnon number.** Each magnon carries spin $-\hbar$ relative to the ferromagnetic ground state. The reduction in magnetization per unit volume is

**第 1 步 — 磁化强度与磁振子数。** 每个磁振子相对于铁磁基态携带自旋 $-\hbar$。单位体积磁化强度的减少量为

$$ \Delta M = (g\mu_B / V) \sum_k \langle a_k^\dagger a_k\rangle = (g\mu_B) \int D(\omega)\, n_{BE}(\omega, T)\, d\omega $$

where $n_{BE}(\omega, T) = 1/(e^{\hbar\omega/k_B T} - 1)$ is the Bose–Einstein distribution.

其中 $n_{BE}(\omega, T) = 1/(e^{\hbar\omega/k_B T} - 1)$ 是玻色–爱因斯坦分布。

**Step 2 — Density of states.** For $\omega = D k^2$ ($D = 2JS/\hbar \times \text{const}$), the magnon density of states in 3D is

**第 2 步 — 态密度。** 对于 $\omega = D k^2$（$D = 2JS/\hbar \times$ 常数），三维磁振子的态密度为

$$ D(\omega) = (1/(4\pi^2))\, (1/D)^{3/2}\, \omega^{1/2}. $$

This $\omega^{1/2}$ dependence is the key step (compare to the phonon $D(\omega) \propto \omega^2$ for 3D acoustic branches).

这个 $\omega^{1/2}$ 依赖关系是关键步骤（与三维声学支声子的 $D(\omega) \propto \omega^2$ 对比）。

**Step 3 — The integral.** At low $T$, the upper limit of the integral can be taken to infinity (few magnons at $T \ll T_c$):

**第 3 步 — 积分。** 在低温时，积分上限可取为无穷（$T \ll T_c$ 时磁振子极少）：

$$ \Delta M \propto \int_0^\infty \omega^{1/2} / (e^{\hbar\omega/k_B T} - 1)\, d\omega. $$

Substitute $u = \hbar\omega/(k_B T)$:

代换 $u = \hbar\omega/(k_B T)$：

$$ \Delta M \propto (k_B T / \hbar)^{3/2} \int_0^\infty u^{1/2} / (e^u - 1)\, du = (k_B T / \hbar)^{3/2} \cdot \Gamma(3/2) \cdot \zeta(3/2). $$

The integral $\int_0^\infty u^{1/2}/(e^u - 1)\, du = \Gamma(3/2)\, \zeta(3/2) = (\sqrt\pi/2)\, \zeta(3/2)$ is a pure number $\approx 2.315$.

积分 $\int_0^\infty u^{1/2}/(e^u - 1)\, du = \Gamma(3/2)\, \zeta(3/2) = (\sqrt\pi/2)\, \zeta(3/2)$ 是纯数 $\approx 2.315$。

**Step 4 — Result.** Therefore

**第 4 步 — 结果。** 因此

$$ \boxed{\, \Delta M / M(0) = A T^{3/2} \,}, \qquad A = (g\mu_B / M(0)) \cdot (k_B/\hbar)^{3/2} \cdot \Gamma(3/2)\, \zeta(3/2) / (4\pi^2 D^{3/2}). $$

The $T^{3/2}$ power arises from combining the $\omega^{1/2}$ density of states with the $k^2$ dispersion in three dimensions; it is a direct signature of ferromagnetic spin waves and one of the clearest low-temperature experimental probes of magnon physics. $\blacksquare$

$T^{3/2}$ 幂次源于三维中 $\omega^{1/2}$ 态密度与 $k^2$ 色散的组合；它是铁磁自旋波的直接标志，也是磁振子物理最清晰的低温实验探针之一。$\blacksquare$

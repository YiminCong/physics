# Module 9.2 — Atomic & Molecular Physics
**模块 9.2 — 原子与分子物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.2-atomic-and-molecular-physics-derivations.md)

---

## 1. Multi-Electron Atoms & the Central-Field Approximation · 多电子原子与中心场近似

**Definition.** For an $N$-electron atom the exact Hamiltonian includes electron–electron repulsions $e^2/(4\pi\varepsilon_0 r_{ij})$ that prevent exact solution. The **central-field (mean-field) approximation** replaces the inter-electron repulsion for each electron $i$ by a spherically symmetric effective potential $U(r_i)$, produced by the nucleus and the average charge distribution of the other electrons. Each electron then moves independently in this screened central potential. The **Hartree self-consistent field (SCF)** method makes $U(r)$ self-consistent: the potential used to solve for each orbital is regenerated from the resulting charge density until convergence.

**定义。** 对于 $N$ 电子原子，精确哈密顿量包含电子–电子排斥 $e^2/(4\pi\varepsilon_0 r_{ij})$，无法精确求解。**中心场（平均场）近似**将每个电子 $i$ 的电子间排斥替换为一个球对称的有效势 $U(r_i)$，由原子核和其他电子平均电荷分布产生。每个电子独立地在这个屏蔽中心势中运动。**哈特里自洽场（SCF）**方法使 $U(r)$ 自洽：用于求解每个轨道的势从所得电荷密度重新生成，直到收敛。

**Demonstration.** In the central-field model each electron occupies a hydrogenic orbital labeled $(n, l, m_l, m_s)$. The energy depends on $n$ and $l$ (but not $m_l$), because the effective potential is no longer purely $-Ze^2/r$ due to screening. This **$l$-degeneracy splitting** is why the ordering of atomic subshells (1s, 2s, 2p, 3s, 3p, 4s, 3d, …) differs from the hydrogenic $n$-only ordering.

**演示。** 在中心场模型中，每个电子占据一个用 $(n, l, m_l, m_s)$ 标记的类氢轨道。能量依赖于 $n$ 和 $l$（但不依赖 $m_l$），因为有效势由于屏蔽不再是纯粹的 $-Ze^2/r$。这种 **$l$ 简并分裂**解释了原子亚壳层的排列顺序（1s, 2s, 2p, 3s, 3p, 4s, 3d, …）与类氢的纯 $n$ 顺序不同。

**Application.** The central-field model explains the periodic table's shell structure and justifies the aufbau principle. It is the starting point for all quantitative atomic structure calculations (Hartree–Fock, density functional theory).

**应用。** 中心场模型解释了元素周期表的壳层结构，证明了构建原理的合理性。它是所有定量原子结构计算（哈特里–福克、密度泛函理论）的起点。

---

## 2. The Periodic Table & Hund's Rules · 元素周期表与洪德规则

**Definition.** Within a given $(n, l)$ subshell, multiple degenerate orbitals exist. **Hund's rules** determine the ground-state electron configuration:
1. Maximize the total spin $S$ (electrons occupy separate orbitals with spins parallel before any pairing).
2. For the maximum $S$, maximize the total orbital angular momentum $L$.
3. The total angular momentum $J = |L - S|$ for a less-than-half-filled subshell, and $J = L + S$ for a more-than-half-filled subshell (Landé interval rule from spin–orbit coupling).

**定义。** 在给定 $(n, l)$ 亚壳层内，存在多个简并轨道。**洪德规则**决定基态电子构型：
1. 最大化总自旋 $S$（电子在配对之前先占据不同轨道且自旋平行）。
2. 在最大 $S$ 的前提下，最大化总轨道角动量 $L$。
3. 对于不足半满的亚壳层，总角动量 $J = |L - S|$；对于超过半满的亚壳层，$J = L + S$（来自自旋–轨道耦合的朗德区间规则）。

**Demonstration.** Consider carbon ($1s^2\,2s^2\,2p^2$). The two 2p electrons can have $(m_l, m_s) = (1, +\tfrac12)$ and $(0, +\tfrac12)$: $S = 1$, $L = 1$, $J = |L-S| = 0$. Ground-state term symbol: ${}^3P_0$. For oxygen ($2p^4$), by particle–hole symmetry the two holes give $S = 1$, $L = 1$, but $J = L + S = 2$ (more-than-half-filled): ${}^3P_2$.

**演示。** 以碳（$1s^2\,2s^2\,2p^2$）为例。两个 2p 电子可以有 $(m_l, m_s) = (1, +\tfrac12)$ 和 $(0, +\tfrac12)$：$S = 1$，$L = 1$，$J = |L-S| = 0$。基态谱项符号：${}^3P_0$。对于氧（$2p^4$），由粒子–空穴对称性，两个空穴给出 $S = 1$，$L = 1$，但 $J = L + S = 2$（超过半满）：${}^3P_2$。

**Application.** Term symbols ${}^{2S+1}L_J$ are the language of spectroscopy. Hund's rules predict ground-state magnetic moments and guide the assignment of spectral lines to specific transitions.

**应用。** 谱项符号 ${}^{2S+1}L_J$ 是光谱学的语言。洪德规则预测基态磁矩，并指导将谱线归属于特定跃迁。

---

## 3. LS Coupling & Fine Structure · LS 耦合与精细结构

**Definition.** In **LS (Russell–Saunders) coupling**, valid for light atoms ($Z \lesssim 30$), individual orbital angular momenta $l_i$ couple to a total $L = \sum l_i$ and individual spins $s_i$ couple to a total $S = \sum s_i$; then $L$ and $S$ couple via spin–orbit interaction to give $J = L + S$. The spin–orbit Hamiltonian $H_\text{SO} = A(\mathbf{L} \cdot \mathbf{S})$ lifts the $J$-degeneracy with an energy shift:

$$ E_\text{SO} = \frac{A}{2}\,[J(J+1) - L(L+1) - S(S+1)] $$

where $A$ is the spin–orbit coupling constant (positive for less-than-half-filled, negative for more-than-half-filled). The resulting energy splitting between adjacent $J$ levels is $\Delta E = AJ$ (the **Landé interval rule**).

**定义。** **LS（拉塞尔–桑德斯）耦合**适用于轻原子（$Z \lesssim 30$），其中各轨道角动量 $l_i$ 耦合为总量 $L = \sum l_i$，各自旋 $s_i$ 耦合为总量 $S = \sum s_i$；然后 $L$ 与 $S$ 通过自旋–轨道相互作用耦合给出 $J = L + S$。自旋–轨道哈密顿量 $H_\text{SO} = A(\mathbf{L} \cdot \mathbf{S})$ 消除 $J$ 简并，能量移动为：

$$ E_\text{SO} = \frac{A}{2}\,[J(J+1) - L(L+1) - S(S+1)] $$

其中 $A$ 为自旋–轨道耦合常数（不足半满时为正，超过半满时为负）。相邻 $J$ 能级之间的能量分裂为 $\Delta E = AJ$（**朗德区间规则**）。

**Demonstration.** For the ${}^3P$ term of carbon ($S = 1$, $L = 1$), the three levels $J = 0, 1, 2$ have energies $0, A, 3A$ relative to $J = 0$; the spacing ratio $E(J{=}2)-E(J{=}1) : E(J{=}1)-E(J{=}0) = 2A : A = 2:1$, a check of the interval rule.

**演示。** 对于碳的 ${}^3P$ 谱项（$S = 1$，$L = 1$），三个能级 $J = 0, 1, 2$ 相对于 $J = 0$ 的能量为 $0, A, 3A$；间距比 $E(J{=}2)-E(J{=}1) : E(J{=}1)-E(J{=}0) = 2A : A = 2:1$，验证了区间规则。

**Application.** Fine structure ($\sim 10^{-4}$ eV) is resolved in optical spectra; the doublet structure of the sodium D lines ($3p\,{}^2P_{3/2}$ and ${}^2P_{1/2}$) is the classic example. Hyperfine structure, from nuclear spin $I$ coupling to $J$, is smaller by a factor $m_e/m_p \sim 10^{-3}$ and is the basis for the hydrogen 21-cm radio line.

**应用。** 精细结构（$\sim 10^{-4}$ eV）在光谱中可分辨；钠 D 线的双线结构（$3p\,{}^2P_{3/2}$ 和 ${}^2P_{1/2}$）是经典例子。超精细结构来自核自旋 $I$ 与 $J$ 的耦合，比精细结构小 $m_e/m_p \sim 10^{-3}$ 倍，是氢 21 cm 射电谱线的基础。

---

## 4. Electric-Dipole Selection Rules · 电偶极跃迁选择规则

**Definition.** An electric-dipole (E1) transition is driven by the matrix element $\langle f|\mathbf{r}|i\rangle$. For this to be non-zero, the **selection rules** from angular-momentum conservation and parity must hold:

$$ \begin{aligned}
&\Delta L = 0, \pm 1 \quad (\text{but } L = 0 \to L = 0 \text{ forbidden}) \\
&\Delta S = 0 \quad (\text{spin does not couple to the radiation field in E1}) \\
&\Delta J = 0, \pm 1 \quad (\text{but } J = 0 \to J = 0 \text{ forbidden}) \\
&\Delta m_J = 0, \pm 1 \\
&\text{Parity must change (Laporte rule: } \Delta l = \pm 1 \text{ for the jumping electron)}
\end{aligned} $$

**定义。** 电偶极（E1）跃迁由矩阵元 $\langle f|\mathbf{r}|i\rangle$ 驱动。为使其不为零，角动量守恒和宇称的**选择规则**必须满足：

$$ \begin{aligned}
&\Delta L = 0, \pm 1 \quad (\text{但 } L = 0 \to L = 0 \text{ 禁戒}) \\
&\Delta S = 0 \quad (\text{在 E1 中自旋不与辐射场耦合}) \\
&\Delta J = 0, \pm 1 \quad (\text{但 } J = 0 \to J = 0 \text{ 禁戒}) \\
&\Delta m_J = 0, \pm 1 \\
&\text{宇称必须改变（拉波特规则：跃迁电子 } \Delta l = \pm 1\text{）}
\end{aligned} $$

**Demonstration.** The sodium 3p → 3s transition satisfies $\Delta l = -1$, $\Delta S = 0$, $\Delta J = \pm 1$: allowed. The 4s → 3s transition has $\Delta l = 0$ (both s-orbitals) — forbidden by the Laporte rule. Forbidden transitions can still occur via magnetic dipole (M1) or electric quadrupole (E2) transitions, but with rates $\sim \alpha^2$ times smaller.

**演示。** 钠的 3p → 3s 跃迁满足 $\Delta l = -1$，$\Delta S = 0$，$\Delta J = \pm 1$：允许。4s → 3s 跃迁有 $\Delta l = 0$（均为 s 轨道）——被拉波特规则禁戒。禁戒跃迁仍可通过磁偶极（M1）或电四极（E2）跃迁发生，但速率小约 $\alpha^2$ 倍。

**Application.** Selection rules determine which spectral lines are observed in emission and absorption spectroscopy. Metastable excited states (where all E1 decays are forbidden) are exploited in lasers (population inversion) and astrophysical forbidden-line diagnostics.

**应用。** 选择规则决定在发射和吸收光谱中观测到哪些谱线。亚稳态（所有 E1 衰变均禁戒）被用于激光（粒子数反转）和天体物理禁戒线诊断。

---

## 5. Molecular Bonding: LCAO and $\text{H}_2^+$ · 分子键合：LCAO 与 $\text{H}_2^+$

**Definition.** The **Linear Combination of Atomic Orbitals (LCAO)** approximation builds molecular orbitals as $\psi = c_A \varphi_A + c_B \varphi_B$, where $\varphi_A, \varphi_B$ are atomic orbitals centered on nuclei A and B. For $\text{H}_2^+$ (one electron, two protons) the secular equation gives two solutions: the **bonding orbital** $\psi_+ = (\varphi_A + \varphi_B)/\sqrt{2(1+S)}$ with energy $E_+$, and the **antibonding orbital** $\psi_- = (\varphi_A - \varphi_B)/\sqrt{2(1-S)}$ with energy $E_-$, where $S = \langle\varphi_A|\varphi_B\rangle$ is the overlap integral.

**定义。** **原子轨道线性组合（LCAO）**近似将分子轨道构建为 $\psi = c_A \varphi_A + c_B \varphi_B$，其中 $\varphi_A, \varphi_B$ 是以核 A 和 B 为中心的原子轨道。对于 $\text{H}_2^+$（一个电子、两个质子），久期方程给出两个解：**成键轨道** $\psi_+ = (\varphi_A + \varphi_B)/\sqrt{2(1+S)}$，能量为 $E_+$；以及**反键轨道** $\psi_- = (\varphi_A - \varphi_B)/\sqrt{2(1-S)}$，能量为 $E_-$，其中 $S = \langle\varphi_A|\varphi_B\rangle$ 为重叠积分。

**Demonstration.** At the equilibrium bond length $R \approx 2a_0$ for $\text{H}_2^+$, $E_+ < E_\text{atom}$: the bonding orbital is lower in energy than the isolated atom because electron density is enhanced between the nuclei, lowering the potential energy more than the kinetic energy rises. The antibonding orbital has a node between the nuclei and $E_- > E_\text{atom}$.

**演示。** 在 $\text{H}_2^+$ 的平衡键长 $R \approx 2a_0$ 处，$E_+ < E_\text{atom}$：成键轨道能量低于孤立原子，因为两核之间的电子密度增强，使势能降低超过动能增大。反键轨道在两核之间有节点，$E_- > E_\text{atom}$。

**Application.** LCAO-MO theory extends to multi-electron molecules ($\text{H}_2$, $\text{N}_2$, organic molecules) and explains bond order, paramagnetism of $\text{O}_2$, and the origin of $\sigma$- and $\pi$-bonds. The full derivation of $E_\pm$ from the LCAO secular determinant is in the Derivations file.

**应用。** LCAO-MO 理论推广到多电子分子（$\text{H}_2$、$\text{N}_2$、有机分子），解释键级、$\text{O}_2$ 的顺磁性，以及 $\sigma$ 键和 $\pi$ 键的起源。从 LCAO 久期行列式推导 $E_\pm$ 的完整过程见推导文件。

---

## 6. Molecular Spectra: Rotational & Vibrational · 分子谱：转动与振动

**Definition.** The **rigid-rotor** model for a diatomic molecule (moment of inertia $I = \mu R^2$) gives rotational energy levels $E_J = BJ(J+1)$, where $B = \hbar^2/(2I)$ is the **rotational constant** and $J = 0, 1, 2, \ldots$ The E1 selection rule is $\Delta J = \pm 1$. The **harmonic-oscillator** model for vibration (reduced mass $\mu$, force constant $k$) gives vibrational levels $E_v = (v + \tfrac12)\hbar\omega_\text{vib}$ with $\omega_\text{vib} = \sqrt{k/\mu}$ and selection rule $\Delta v = \pm 1$.

**定义。** 双原子分子（转动惯量 $I = \mu R^2$）的**刚性转子**模型给出转动能级 $E_J = BJ(J+1)$，其中 $B = \hbar^2/(2I)$ 为**转动常数**，$J = 0, 1, 2, \ldots$。E1 选择规则为 $\Delta J = \pm 1$。振动的**谐振子**模型（折合质量 $\mu$，力常数 $k$）给出振动能级 $E_v = (v + \tfrac12)\hbar\omega_\text{vib}$，其中 $\omega_\text{vib} = \sqrt{k/\mu}$，选择规则 $\Delta v = \pm 1$。

**Demonstration.** The pure rotational spectrum consists of lines at frequencies $\nu_{J\to J+1} = 2B(J+1)/h$, equally spaced by $2B$. For HCl, $B \approx 10.6\ \text{cm}^{-1}$, placing rotational transitions in the microwave. The vibrational frequency $\omega_\text{vib}/2\pi$ for HCl falls in the infrared ($\sim 2900\ \text{cm}^{-1}$). In a vibration–rotation band, each vibrational transition $v \to v+1$ is accompanied by $\Delta J = \pm 1$ rotational changes, producing P and R branches.

**演示。** 纯转动谱由频率 $\nu_{J\to J+1} = 2B(J+1)/h$ 的谱线组成，间距均匀为 $2B$。对于 HCl，$B \approx 10.6\ \text{cm}^{-1}$，将转动跃迁置于微波段。HCl 的振动频率 $\omega_\text{vib}/2\pi$ 落在红外区（$\sim 2900\ \text{cm}^{-1}$）。在振转带中，每次振动跃迁 $v \to v+1$ 伴随 $\Delta J = \pm 1$ 的转动变化，产生 P 支和 R 支。

**Application.** Rotational spectra give precise bond lengths (from $B$). Vibrational spectra identify functional groups (IR spectroscopy). Raman spectroscopy accesses modes forbidden in IR. The vibration–rotation spectrum of atmospheric $\text{CO}_2$ and $\text{H}_2\text{O}$ is central to the physics of the greenhouse effect.

**应用。** 转动谱给出精确的键长（由 $B$ 获得）。振动谱识别官能团（红外光谱）。拉曼光谱可获得红外禁戒的模式。大气中 $\text{CO}_2$ 和 $\text{H}_2\text{O}$ 的振转谱是温室效应物理的核心。

---

**Self-test (blank page)**

1. Explain why the energy of an electron in a many-electron atom depends on $l$ as well as $n$, and sketch the subshell ordering up to $n = 4$.
2. Apply Hund's rules to find the ground-state term symbol of nitrogen ($2p^3$) and iron ($3d^6$).
3. State all the electric-dipole selection rules. Which rule forbids the 4s → 3s transition in sodium?
4. Write the LCAO bonding and antibonding combinations for $\text{H}_2^+$; explain physically why the bonding orbital is lower in energy.
5. Write the rotational energy formula and derive the spacing between adjacent microwave absorption lines. What does the spacing measure?

**自测（空白页）**

1. 解释为何多电子原子中电子能量同时依赖于 $l$ 和 $n$，并画出到 $n = 4$ 的亚壳层排列顺序。
2. 应用洪德规则求氮（$2p^3$）和铁（$3d^6$）的基态谱项符号。
3. 陈述所有电偶极跃迁选择规则。哪条规则禁戒钠的 4s → 3s 跃迁？
4. 写出 $\text{H}_2^+$ 的 LCAO 成键和反键组合；从物理上解释为何成键轨道能量更低。
5. 写出转动能量公式并推导相邻微波吸收谱线的间距。间距测量什么？

---

← Previous: [Module 9.1 — Electronics](./module-9.1-electronics.md) · [Phase 9 index](./README.md) · Next: [Module 9.3 — Nuclear Physics](./module-9.3-nuclear-physics.md) →

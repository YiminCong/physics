# Module 9.7 — Atoms in External Fields & Precision Spectroscopy
**模块 9.7 — 外场中的原子与精密光谱学**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.7-atoms-in-external-fields-derivations.md)

---

## 1. Fine Structure of Hydrogen · 氢原子的精细结构

**Definition.** The Bohr energies $E_n = -13.6\ \text{eV}/n^2$ ignore relativistic effects. At order $\alpha^4$ (where $\alpha \approx 1/137$ is the fine-structure constant) three corrections to the hydrogen Hamiltonian appear, all of relative size $\sim \alpha^2 \sim 10^{-4}$: (i) the **relativistic kinetic correction** $H_\text{rel} = -p^4/(8m^3c^2)$, from expanding the relativistic energy; (ii) the **spin–orbit coupling** $H_\text{SO} = \frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\,\mathbf{S}\cdot\mathbf{L}$, from the electron's spin interacting with the magnetic field of its orbital motion (with the Thomas factor $\tfrac12$); and (iii) the **Darwin term** $H_D \propto \delta^3(\mathbf{r})$, affecting only $l = 0$ states (Zitterbewegung smearing of the electron over a Compton wavelength). Treated together by degenerate perturbation theory, they yield the fine structure of the levels.

**定义。** 玻尔能量 $E_n = -13.6\ \text{eV}/n^2$ 忽略了相对论效应。在 $\alpha^4$ 阶（$\alpha \approx 1/137$ 为精细结构常数），氢原子哈密顿量出现三项修正，相对大小均为 $\sim \alpha^2 \sim 10^{-4}$：(i) **相对论动能修正** $H_\text{rel} = -p^4/(8m^3c^2)$，来自相对论能量的展开；(ii) **自旋–轨道耦合** $H_\text{SO} = \frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\,\mathbf{S}\cdot\mathbf{L}$，来自电子自旋与其轨道运动磁场的相互作用（含托马斯因子 $\tfrac12$）；(iii) **达尔文项** $H_D \propto \delta^3(\mathbf{r})$，仅影响 $l = 0$ 态（电子在康普顿波长尺度上的颤动弥散）。用简并微扰论一并处理，它们给出能级的精细结构。

**Demonstration.** The remarkable result is that the three $O(\alpha^4)$ shifts combine into a single formula depending only on the principal quantum number $n$ and the total angular momentum $j = l \pm \tfrac12$ — not on $l$ separately:

$$ E_{nj} = -\frac{13.6\ \text{eV}}{n^2}\left[ 1 + \frac{\alpha^2}{n^2}\left(\frac{n}{j+\tfrac12} - \frac{3}{4}\right) \right]. $$

For $n = 2$, the levels $2s_{1/2}$ and $2p_{1/2}$ (both $j = \tfrac12$) are degenerate, while $2p_{3/2}$ ($j = \tfrac32$) lies higher. The fine-structure splitting scales as $\alpha^2 \times \text{Bohr} \sim 10^{-4}$ eV, matching the same result obtained exactly from the Dirac equation (Module 3.15).

**演示。** 值得注意的结果是：三项 $O(\alpha^4)$ 移动合并为一个仅依赖于主量子数 $n$ 和总角动量 $j = l \pm \tfrac12$（而不单独依赖 $l$）的公式：

$$ E_{nj} = -\frac{13.6\ \text{eV}}{n^2}\left[ 1 + \frac{\alpha^2}{n^2}\left(\frac{n}{j+\tfrac12} - \frac{3}{4}\right) \right]. $$

对于 $n = 2$，能级 $2s_{1/2}$ 与 $2p_{1/2}$（均 $j = \tfrac12$）简并，而 $2p_{3/2}$（$j = \tfrac32$）较高。精细结构分裂的标度为 $\alpha^2 \times \text{玻尔} \sim 10^{-4}$ eV，与直接由狄拉克方程（模块 3.15）得到的精确结果一致。

**Application.** The fine-structure formula explains the doublet structure of spectral lines (e.g. the sodium D lines, 9.2) and is the baseline against which the Lamb shift and hyperfine structure are measured. It established the value of $\alpha$ and remains a benchmark for relativistic atomic theory.

**应用。** 精细结构公式解释了谱线的双线结构（如钠 D 线，见 9.2），并且是测量兰姆移位和超精细结构的基线。它确立了 $\alpha$ 的值，至今仍是相对论原子理论的标杆。

---

## 2. The Zeeman Effect · 塞曼效应

**Definition.** In an external magnetic field $B$ (taken along $\hat{z}$), the atomic magnetic moment couples to the field via $H_Z = (\mu_B/\hbar)\, B\, (L_z + 2S_z)$, where $\mu_B = e\hbar/2m$ is the Bohr magneton and the factor 2 is the electron g-factor. The observed splitting depends on the relative size of $B$ versus the fine structure. In the **weak-field (anomalous Zeeman)** regime, the fine structure dominates and $j, m_j$ remain good quantum numbers; in the **strong-field (Paschen–Back)** regime, $B$ dominates and $m_l, m_s$ decouple.

**定义。** 在外磁场 $B$（取沿 $\hat{z}$）中，原子磁矩通过 $H_Z = (\mu_B/\hbar)\, B\, (L_z + 2S_z)$ 与场耦合，其中 $\mu_B = e\hbar/2m$ 为玻尔磁子，因子 2 为电子 g 因子。观测到的分裂取决于 $B$ 相对于精细结构的大小。在**弱场（反常塞曼）**区，精细结构占主导，$j$、$m_j$ 仍是好量子数；在**强场（帕邢–巴克）**区，$B$ 占主导，$m_l$、$m_s$ 解耦。

**Demonstration.** Weak field: in the $|n, j, m_j\rangle$ basis, projecting $\mathbf{L} + 2\mathbf{S} = \mathbf{J} + \mathbf{S}$ onto $\mathbf{J}$ (the Wigner–Eckart / projection theorem, Module 3.11) gives the splitting

$$ \Delta E = g_J \mu_B B\, m_j, \qquad g_J = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2j(j+1)}, $$

where $g_J$ is the **Landé g-factor**. Each fine-structure level splits into $2j+1$ equally spaced sublevels. Strong field: $L_z$ and $S_z$ are independently sharp, so $\Delta E = \mu_B B (m_l + 2m_s)$. The **normal Zeeman triplet** is the special case $s = 0$ (so $g_J = 1$): a line splits into three components spaced by $\mu_B B$, recovering the classical Lorentz result.

**演示。** 弱场：在 $|n, j, m_j\rangle$ 基中，将 $\mathbf{L} + 2\mathbf{S} = \mathbf{J} + \mathbf{S}$ 投影到 $\mathbf{J}$ 上（维格纳–埃卡特/投影定理，模块 3.11）给出分裂

$$ \Delta E = g_J \mu_B B\, m_j, \qquad g_J = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2j(j+1)}, $$

其中 $g_J$ 为**朗德 g 因子**。每个精细结构能级分裂为 $2j+1$ 个等间距子能级。强场：$L_z$ 和 $S_z$ 各自确定，因此 $\Delta E = \mu_B B (m_l + 2m_s)$。**正常塞曼三重线**是 $s = 0$ 的特例（故 $g_J = 1$）：一条谱线分裂为间距 $\mu_B B$ 的三个分量，重现经典洛伦兹结果。

**Application.** The Zeeman effect measures magnetic fields remotely — solar and stellar magnetic fields from line splitting, laboratory field calibration, and magnetic-resonance techniques. The $g_J$ factor identifies the term (${}^{2S+1}L_J$) of an emitting state, a key tool in atomic spectroscopy.

**应用。** 塞曼效应可远程测量磁场——由谱线分裂测定太阳和恒星磁场、实验室磁场校准以及磁共振技术。$g_J$ 因子识别发射态的谱项（${}^{2S+1}L_J$），是原子光谱学的关键工具。

---

## 3. The Stark Effect, Hyperfine Structure & the Lamb Shift · 斯塔克效应、超精细结构与兰姆移位

**Definition.** An external electric field $E$ couples via $H_S = e\mathbf{E}\cdot\mathbf{r} = eEz$ (field along $\hat{z}$). For a **non-degenerate** state (e.g. the hydrogen ground state) the linear shift vanishes by parity and the leading effect is the **quadratic Stark shift** $\Delta E = -\tfrac12 \alpha_p E^2$, with polarizability $\alpha_p$ (for the H ground state $\alpha_p = \tfrac92(4\pi\varepsilon_0)a_0^3$). For a **degenerate** manifold (e.g. $n = 2$ of hydrogen, where 2s and 2p share an energy), degenerate perturbation theory gives a **linear Stark effect**. Separately, the nuclear magnetic moment couples to the electron as $H_\text{hf} \propto \mathbf{I}\cdot\mathbf{J}$, producing **hyperfine structure** with total $\mathbf{F} = \mathbf{I} + \mathbf{J}$; and QED vacuum fluctuations produce the **Lamb shift** between levels Dirac theory predicts to be degenerate.

**定义。** 外电场 $E$ 通过 $H_S = e\mathbf{E}\cdot\mathbf{r} = eEz$（场沿 $\hat{z}$）耦合。对于**非简并**态（如氢基态），线性移动因宇称为零，主导效应为**二次斯塔克移动** $\Delta E = -\tfrac12 \alpha_p E^2$，极化率 $\alpha_p$（氢基态 $\alpha_p = \tfrac92(4\pi\varepsilon_0)a_0^3$）。对于**简并**流形（如氢的 $n = 2$，其中 2s 与 2p 能量相同），简并微扰论给出**线性斯塔克效应**。另外，核磁矩与电子耦合为 $H_\text{hf} \propto \mathbf{I}\cdot\mathbf{J}$，产生总角动量 $\mathbf{F} = \mathbf{I} + \mathbf{J}$ 的**超精细结构**；而 QED 真空涨落产生**兰姆移位**，使狄拉克理论预言简并的能级分裂。

**Demonstration.** Linear Stark ($n = 2$ hydrogen): diagonalizing $eEz$ in the degenerate $\{2s, 2p_{m=0}\}$ space gives shifts

$$ \Delta E = \pm 3\, e\, a_0\, E \quad (\text{and } 0 \text{ for the two } m = \pm 1 \text{ states}), $$

a splitting linear in $E$ — unique to the Coulomb ($l$-)degeneracy. Hyperfine (H 1s, Fermi contact term): with $I = \tfrac12$ (proton) and $J = \tfrac12$, the $\mathbf{I}\cdot\mathbf{J}$ energy is

$$ E_F = \frac{A}{2}[F(F+1) - I(I+1) - J(J+1)], $$

so the interval $F = 1 \leftrightarrow F = 0$ is $\Delta E = A$. This **21-cm line** sits at $\nu = 1420$ MHz, $\lambda = 21$ cm; hyperfine $\sim (m_e/m_p) \times$ fine structure. Lamb shift: $2s_{1/2}$ and $2p_{1/2}$, exactly degenerate in Dirac theory, are split by $\approx 1057$ MHz, the 2s state pushed up by the electron being "smeared" by zero-point field fluctuations (electron self-energy + vacuum polarization, derived in QED, Module 8.2).

**演示。** 线性斯塔克（氢 $n = 2$）：在简并 $\{2s, 2p_{m=0}\}$ 空间对角化 $eEz$ 给出移动

$$ \Delta E = \pm 3\, e\, a_0\, E \quad (\text{两个 } m = \pm 1 \text{ 态为 } 0), $$

一个对 $E$ 线性的分裂——为库仑（$l$）简并所独有。超精细（氢 1s，费米接触项）：$I = \tfrac12$（质子）、$J = \tfrac12$，$\mathbf{I}\cdot\mathbf{J}$ 能量为

$$ E_F = \frac{A}{2}[F(F+1) - I(I+1) - J(J+1)], $$

故 $F = 1 \leftrightarrow F = 0$ 的间隔为 $\Delta E = A$。此 **21 cm 线**位于 $\nu = 1420$ MHz、$\lambda = 21$ cm；超精细 $\sim (m_e/m_p) \times$ 精细结构。兰姆移位：$2s_{1/2}$ 与 $2p_{1/2}$ 在狄拉克理论中精确简并，却被分裂约 1057 MHz，2s 态因电子被零点场涨落"弥散"而上移（电子自能 + 真空极化，由 QED 推导，模块 8.2）。

**Application.** The quadratic Stark effect underlies atomic clock shifts and Rydberg-atom field sensors. The linear Stark effect enables electric-field control of cold atoms. The 21-cm line maps neutral hydrogen across the galaxy and into the cosmological dark ages. The Lamb shift was the first triumph of QED and remains a precision test of the theory.

**应用。** 二次斯塔克效应是原子钟频移和里德伯原子电场传感器的基础。线性斯塔克效应实现冷原子的电场操控。21 cm 线绘制银河系乃至宇宙黑暗时代的中性氢分布。兰姆移位是 QED 的首个胜利，至今仍是该理论的精密检验。

---

**Self-test (blank page)**

1. List the three $O(\alpha^4)$ corrections to the hydrogen levels and state which acts only on $l = 0$. Write the fine-structure formula $E_{nj}$ and explain why it depends on $j$ but not $l$.
2. Derive the Landé g-factor and state the weak-field splitting $\Delta E = g_J \mu_B B\, m_j$. What does it become in the Paschen–Back limit, and in the normal-Zeeman ($s = 0$) case?
3. Distinguish the quadratic Stark effect of the hydrogen ground state from the linear Stark effect of the $n = 2$ manifold. Why is the linear effect unique to hydrogen?
4. Explain the origin of the 21-cm line, write $E_F$ for the $\mathbf{I}\cdot\mathbf{J}$ coupling, and state how hyperfine structure compares in size to fine structure. What is the Lamb shift and what causes it?

**自测（空白页）**

1. 列出氢能级的三项 $O(\alpha^4)$ 修正，并指出哪一项仅作用于 $l = 0$。写出精细结构公式 $E_{nj}$ 并解释为何它依赖 $j$ 而不依赖 $l$。
2. 推导朗德 g 因子并陈述弱场分裂 $\Delta E = g_J \mu_B B\, m_j$。在帕邢–巴克极限和正常塞曼（$s = 0$）情形下它变为什么？
3. 区分氢基态的二次斯塔克效应与 $n = 2$ 流形的线性斯塔克效应。为何线性效应为氢所独有？
4. 解释 21 cm 线的起源，写出 $\mathbf{I}\cdot\mathbf{J}$ 耦合的 $E_F$，并说明超精细结构与精细结构的大小关系。兰姆移位是什么，由什么引起？

---

← Previous: [Module 9.6 — Quantum Optics & Laser Physics](./module-9.6-quantum-optics-and-lasers.md) · [Phase 9 index](./README.md) · Next: [Module 9.8 — Stellar Structure & Compact Objects](./module-9.8-stellar-structure-and-compact-objects.md) →

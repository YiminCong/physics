# Module 9.7 — Atoms in External Fields & Precision Spectroscopy
**模块 9.7 — 外场中的原子与精密光谱学**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.7-atoms-in-external-fields-derivations.md)

---

## 1. Fine Structure of Hydrogen · 氢原子的精细结构

**Definition.** The Bohr energies E_n = −13.6 eV/n² ignore relativistic effects. At order α⁴ (where α ≈ 1/137 is the fine-structure constant) three corrections to the hydrogen Hamiltonian appear, all of relative size ~ α² ~ 10⁻⁴: (i) the **relativistic kinetic correction** H_rel = −p⁴/(8m³c²), from expanding the relativistic energy; (ii) the **spin–orbit coupling** H_SO = (1/2m²c²)(1/r)(dV/dr) S·L, from the electron's spin interacting with the magnetic field of its orbital motion (with the Thomas factor ½); and (iii) the **Darwin term** H_D ∝ δ³(r), affecting only l = 0 states (Zitterbewegung smearing of the electron over a Compton wavelength). Treated together by degenerate perturbation theory, they yield the fine structure of the levels.

**定义。** 玻尔能量 E_n = −13.6 eV/n² 忽略了相对论效应。在 α⁴ 阶（α ≈ 1/137 为精细结构常数），氢原子哈密顿量出现三项修正，相对大小均为 ~ α² ~ 10⁻⁴：(i) **相对论动能修正** H_rel = −p⁴/(8m³c²)，来自相对论能量的展开；(ii) **自旋–轨道耦合** H_SO = (1/2m²c²)(1/r)(dV/dr) S·L，来自电子自旋与其轨道运动磁场的相互作用（含托马斯因子 ½）；(iii) **达尔文项** H_D ∝ δ³(r)，仅影响 l = 0 态（电子在康普顿波长尺度上的颤动弥散）。用简并微扰论一并处理，它们给出能级的精细结构。

**Demonstration.** The remarkable result is that the three O(α⁴) shifts combine into a single formula depending only on the principal quantum number n and the total angular momentum j = l ± ½ — not on l separately:

  E_{nj} = −(13.6 eV/n²)[ 1 + (α²/n²)(n/(j+½) − ¾) ].

For n = 2, the levels 2s₁/₂ and 2p₁/₂ (both j = ½) are degenerate, while 2p₃/₂ (j = 3/₂) lies higher. The fine-structure splitting scales as α² × Bohr ~ 10⁻⁴ eV, matching the same result obtained exactly from the Dirac equation (Module 3.15).

**演示。** 值得注意的结果是：三项 O(α⁴) 移动合并为一个仅依赖于主量子数 n 和总角动量 j = l ± ½（而不单独依赖 l）的公式：

  E_{nj} = −(13.6 eV/n²)[ 1 + (α²/n²)(n/(j+½) − ¾) ]。

对于 n = 2，能级 2s₁/₂ 与 2p₁/₂（均 j = ½）简并，而 2p₃/₂（j = 3/₂）较高。精细结构分裂的标度为 α² × 玻尔 ~ 10⁻⁴ eV，与直接由狄拉克方程（模块 3.15）得到的精确结果一致。

**Application.** The fine-structure formula explains the doublet structure of spectral lines (e.g. the sodium D lines, 9.2) and is the baseline against which the Lamb shift and hyperfine structure are measured. It established the value of α and remains a benchmark for relativistic atomic theory.

**应用。** 精细结构公式解释了谱线的双线结构（如钠 D 线，见 9.2），并且是测量兰姆移位和超精细结构的基线。它确立了 α 的值，至今仍是相对论原子理论的标杆。

---

## 2. The Zeeman Effect · 塞曼效应

**Definition.** In an external magnetic field B (taken along ẑ), the atomic magnetic moment couples to the field via H_Z = (μ_B/ℏ) B (L_z + 2S_z), where μ_B = eℏ/2m is the Bohr magneton and the factor 2 is the electron g-factor. The observed splitting depends on the relative size of B versus the fine structure. In the **weak-field (anomalous Zeeman)** regime, the fine structure dominates and j, m_j remain good quantum numbers; in the **strong-field (Paschen–Back)** regime, B dominates and m_l, m_s decouple.

**定义。** 在外磁场 B（取沿 ẑ）中，原子磁矩通过 H_Z = (μ_B/ℏ) B (L_z + 2S_z) 与场耦合，其中 μ_B = eℏ/2m 为玻尔磁子，因子 2 为电子 g 因子。观测到的分裂取决于 B 相对于精细结构的大小。在**弱场（反常塞曼）**区，精细结构占主导，j、m_j 仍是好量子数；在**强场（帕邢–巴克）**区，B 占主导，m_l、m_s 解耦。

**Demonstration.** Weak field: in the |n, j, m_j⟩ basis, projecting L + 2S = J + S onto J (the Wigner–Eckart / projection theorem, Module 3.11) gives the splitting

  ΔE = g_J μ_B B m_j,    g_J = 1 + [j(j+1) + s(s+1) − l(l+1)] / [2j(j+1)],

where g_J is the **Landé g-factor**. Each fine-structure level splits into 2j+1 equally spaced sublevels. Strong field: L_z and S_z are independently sharp, so ΔE = μ_B B (m_l + 2m_s). The **normal Zeeman triplet** is the special case s = 0 (so g_J = 1): a line splits into three components spaced by μ_B B, recovering the classical Lorentz result.

**演示。** 弱场：在 |n, j, m_j⟩ 基中，将 L + 2S = J + S 投影到 J 上（维格纳–埃卡特/投影定理，模块 3.11）给出分裂

  ΔE = g_J μ_B B m_j，   g_J = 1 + [j(j+1) + s(s+1) − l(l+1)] / [2j(j+1)]，

其中 g_J 为**朗德 g 因子**。每个精细结构能级分裂为 2j+1 个等间距子能级。强场：L_z 和 S_z 各自确定，因此 ΔE = μ_B B (m_l + 2m_s)。**正常塞曼三重线**是 s = 0 的特例（故 g_J = 1）：一条谱线分裂为间距 μ_B B 的三个分量，重现经典洛伦兹结果。

**Application.** The Zeeman effect measures magnetic fields remotely — solar and stellar magnetic fields from line splitting, laboratory field calibration, and magnetic-resonance techniques. The g_J factor identifies the term (²S⁺¹L_J) of an emitting state, a key tool in atomic spectroscopy.

**应用。** 塞曼效应可远程测量磁场——由谱线分裂测定太阳和恒星磁场、实验室磁场校准以及磁共振技术。g_J 因子识别发射态的谱项（²S⁺¹L_J），是原子光谱学的关键工具。

---

## 3. The Stark Effect, Hyperfine Structure & the Lamb Shift · 斯塔克效应、超精细结构与兰姆移位

**Definition.** An external electric field E couples via H_S = eE·r = eEz (field along ẑ). For a **non-degenerate** state (e.g. the hydrogen ground state) the linear shift vanishes by parity and the leading effect is the **quadratic Stark shift** ΔE = −½ α_p E², with polarizability α_p (for the H ground state α_p = (9/2)(4πε₀)a₀³). For a **degenerate** manifold (e.g. n = 2 of hydrogen, where 2s and 2p share an energy), degenerate perturbation theory gives a **linear Stark effect**. Separately, the nuclear magnetic moment couples to the electron as H_hf ∝ I·J, producing **hyperfine structure** with total F = I + J; and QED vacuum fluctuations produce the **Lamb shift** between levels Dirac theory predicts to be degenerate.

**定义。** 外电场 E 通过 H_S = eE·r = eEz（场沿 ẑ）耦合。对于**非简并**态（如氢基态），线性移动因宇称为零，主导效应为**二次斯塔克移动** ΔE = −½ α_p E²，极化率 α_p（氢基态 α_p = (9/2)(4πε₀)a₀³）。对于**简并**流形（如氢的 n = 2，其中 2s 与 2p 能量相同），简并微扰论给出**线性斯塔克效应**。另外，核磁矩与电子耦合为 H_hf ∝ I·J，产生总角动量 F = I + J 的**超精细结构**；而 QED 真空涨落产生**兰姆移位**，使狄拉克理论预言简并的能级分裂。

**Demonstration.** Linear Stark (n = 2 hydrogen): diagonalizing eEz in the degenerate {2s, 2p_{m=0}} space gives shifts

  ΔE = ±3 e a₀ E   (and 0 for the two m = ±1 states),

a splitting linear in E — unique to the Coulomb (l-)degeneracy. Hyperfine (H 1s, Fermi contact term): with I = ½ (proton) and J = ½, the I·J energy is

  E_F = (A/2)[F(F+1) − I(I+1) − J(J+1)],

so the interval F = 1 ↔ F = 0 is ΔE = A. This **21-cm line** sits at ν = 1420 MHz, λ = 21 cm; hyperfine ~ (m_e/m_p) × fine structure. Lamb shift: 2s₁/₂ and 2p₁/₂, exactly degenerate in Dirac theory, are split by ≈ 1057 MHz, the 2s state pushed up by the electron being "smeared" by zero-point field fluctuations (electron self-energy + vacuum polarization, derived in QED, Module 8.2).

**演示。** 线性斯塔克（氢 n = 2）：在简并 {2s, 2p_{m=0}} 空间对角化 eEz 给出移动

  ΔE = ±3 e a₀ E   （两个 m = ±1 态为 0），

一个对 E 线性的分裂——为库仑（l）简并所独有。超精细（氢 1s，费米接触项）：I = ½（质子）、J = ½，I·J 能量为

  E_F = (A/2)[F(F+1) − I(I+1) − J(J+1)]，

故 F = 1 ↔ F = 0 的间隔为 ΔE = A。此 **21 cm 线**位于 ν = 1420 MHz、λ = 21 cm；超精细 ~ (m_e/m_p) × 精细结构。兰姆移位：2s₁/₂ 与 2p₁/₂ 在狄拉克理论中精确简并，却被分裂约 1057 MHz，2s 态因电子被零点场涨落"弥散"而上移（电子自能 + 真空极化，由 QED 推导，模块 8.2）。

**Application.** The quadratic Stark effect underlies atomic clock shifts and Rydberg-atom field sensors. The linear Stark effect enables electric-field control of cold atoms. The 21-cm line maps neutral hydrogen across the galaxy and into the cosmological dark ages. The Lamb shift was the first triumph of QED and remains a precision test of the theory.

**应用。** 二次斯塔克效应是原子钟频移和里德伯原子电场传感器的基础。线性斯塔克效应实现冷原子的电场操控。21 cm 线绘制银河系乃至宇宙黑暗时代的中性氢分布。兰姆移位是 QED 的首个胜利，至今仍是该理论的精密检验。

---

**Self-test (blank page)**

1. List the three O(α⁴) corrections to the hydrogen levels and state which acts only on l = 0. Write the fine-structure formula E_{nj} and explain why it depends on j but not l.
2. Derive the Landé g-factor and state the weak-field splitting ΔE = g_J μ_B B m_j. What does it become in the Paschen–Back limit, and in the normal-Zeeman (s = 0) case?
3. Distinguish the quadratic Stark effect of the hydrogen ground state from the linear Stark effect of the n = 2 manifold. Why is the linear effect unique to hydrogen?
4. Explain the origin of the 21-cm line, write E_F for the I·J coupling, and state how hyperfine structure compares in size to fine structure. What is the Lamb shift and what causes it?

**自测（空白页）**

1. 列出氢能级的三项 O(α⁴) 修正，并指出哪一项仅作用于 l = 0。写出精细结构公式 E_{nj} 并解释为何它依赖 j 而不依赖 l。
2. 推导朗德 g 因子并陈述弱场分裂 ΔE = g_J μ_B B m_j。在帕邢–巴克极限和正常塞曼（s = 0）情形下它变为什么？
3. 区分氢基态的二次斯塔克效应与 n = 2 流形的线性斯塔克效应。为何线性效应为氢所独有？
4. 解释 21 cm 线的起源，写出 I·J 耦合的 E_F，并说明超精细结构与精细结构的大小关系。兰姆移位是什么，由什么引起？

---

← Previous: [Module 9.6 — Quantum Optics & Laser Physics](./module-9.6-quantum-optics-and-lasers.md) · [Phase 9 index](./README.md) · Next: [Module 9.8 — Stellar Structure & Compact Objects](./module-9.8-stellar-structure-and-compact-objects.md) →

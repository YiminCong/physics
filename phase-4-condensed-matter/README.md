# Phase 4 — Condensed Matter / Solid State
**第 4 阶段 — 凝聚态 / 固体物理**

Modules 4.1–4.12, in **Definition → Demonstration → Application** format. This phase builds
the stage on which superconductivity happens: electrons and phonons in a crystal, magnetic
order, semiconductor devices, and topological states of matter. Almost everything here is
⭐ load-bearing.

模块 4.1–4.9，采用**定义 → 演示 → 应用**格式。本阶段构建超导发生的舞台：晶体中的电子与声子、磁有序、半导体器件以及物质的拓扑态。这里几乎所有内容都是 ⭐ 承重性的。

## Modules · 模块

| # | Title · 标题 | |
|---|-------|---|
| 4.1 | [Electrons and Heat in Solids](./module-4.1-electrons-and-heat-in-solids.md) · 固体中的电子与热 | |
| 4.2 | [Crystal Structure & Reciprocal Space](./module-4.2-crystal-structure-and-reciprocal-space.md) · 晶体结构与倒格子空间 | ⭐ |
| 4.3 | [Lattice Vibrations & Phonons](./module-4.3-lattice-vibrations-and-phonons.md) · 晶格振动与声子 | ⭐ |
| 4.4 | [Electrons in a Periodic Potential](./module-4.4-electrons-in-a-periodic-potential.md) · 周期势中的电子 | ⭐ |
| 4.5 | [Fermi Surface & Electron–Phonon Coupling](./module-4.5-fermi-surface-and-electron-phonon-coupling.md) · 费米面与电子–声子耦合 | ⭐ |
| 4.6 | [Magnetism & Spin Waves](./module-4.6-magnetism-and-spin-waves.md) · 磁性与自旋波 | ⭐ |
| 4.7 | [Semiconductor Physics](./module-4.7-semiconductor-physics.md) · 半导体物理 | ⭐ |
| 4.8 | [Quantum Hall Effect](./module-4.8-quantum-hall-effect.md) · 量子霍尔效应 | ⭐ |
| 4.9 | [Topological Matter & Berry Phase](./module-4.9-topological-matter-and-berry-phase.md) · 拓扑物质与贝里相位 | ⭐ |
| 4.10 | [Landau Fermi-Liquid Theory](./module-4.10-landau-fermi-liquid-theory.md) · 朗道费米液体理论 | ⭐ |
| 4.11 | [Linear Response, Transport & the Kubo Formula](./module-4.11-linear-response-and-transport.md) · 线性响应、输运与久保公式 | |
| 4.12 | [The Hubbard Model & Mott Insulators](./module-4.12-hubbard-model-and-mott-insulators.md) · 哈伯德模型与莫特绝缘体 | ⭐ |

## Phase 4 Checkpoint (blank page)

1. Explain why the electronic heat capacity is linear in $T$ and small; write $C = \gamma T + \beta T^3$ and say what each term probes.
2. Construct the reciprocal lattice and first Brillouin zone for a simple lattice; state the Bragg condition.
3. Derive the monatomic-chain phonon dispersion; distinguish acoustic vs optical branches; explain the isotope effect.
4. State Bloch's theorem; show how a gap opens at the zone boundary; give the tight-binding band $E(k) = E_0 - 2t \cos(ka)$; classify metal/insulator/semiconductor by band filling.
5. Define the Fermi surface and $g(E_F)$; explain the phonon-mediated electron–electron attraction and why only electrons near $E_F$ matter.
6. State the Curie law and derive it from a spin partition function; write the Heisenberg model $H = -J \sum \mathbf{S}_i\cdot\mathbf{S}_j$ and give mean-field $T_c = zJS(S+1)/(3k_B)$; state the Bloch $T^{3/2}$ law for magnons and explain why it is $T^{3/2}$.
7. Define effective mass $m^* = \hbar^2/(d^2E/dk^2)$ and holes; write $n_i \propto T^{3/2} \exp(-E_g/2k_BT)$ for intrinsic carriers; describe the p–n junction built-in voltage and the Shockley diode equation.
8. Derive the Landau level spectrum $E_n = \hbar\omega_c(n+\tfrac12)$ and give the degeneracy $eB/h$ per unit area; state the IQHE result $\sigma_{xy} = \nu e^2/h$ and explain it via chiral edge states; describe the Laughlin state and its fractional charge $e/m$.
9. Define the Berry connection $\mathbf{A}(\mathbf{k}) = i\langle u|\nabla_{\mathbf{k}}|u\rangle$ and Chern number $C = (1/2\pi)\int\Omega\,d^2k$; explain why $C$ is an integer; give the SSH winding number and explain why $|t_2| > |t_1|$ leads to protected zero-energy edge states.

**自测（空白页）**

1. 解释为何电子热容对温度 $T$ 呈线性关系且数值较小；写出 $C = \gamma T + \beta T^3$ 并说明每项探测的物理量。
2. 为简单格子构造倒格子和第一布里渊区；陈述布拉格条件。
3. 推导单原子链的声子色散关系；区分声学支与光学支；解释同位素效应。
4. 陈述布洛赫定理；说明能隙如何在区边界打开；给出紧束缚能带 $E(k) = E_0 - 2t \cos(ka)$；按能带填充对金属/绝缘体/半导体分类。
5. 定义费米面和 $g(E_F)$；解释声子媒介的电子–电子吸引以及为何只有费米面附近的电子才起作用。
6. 陈述居里定律并由自旋配分函数推导；写出海森堡模型 $H = -J \sum \mathbf{S}_i\cdot\mathbf{S}_j$ 并给出平均场 $T_c = zJS(S+1)/(3k_B)$；陈述磁振子的布洛赫 $T^{3/2}$ 定律并解释为何是 $T^{3/2}$。
7. 定义有效质量 $m^* = \hbar^2/(d^2E/dk^2)$ 与空穴；写出本征载流子浓度 $n_i \propto T^{3/2} \exp(-E_g/2k_BT)$；描述 p–n 结内建电压与肖克利二极管方程。
8. 推导朗道能级谱 $E_n = \hbar\omega_c(n+\tfrac12)$ 并给出每单位面积简并度 $eB/h$；陈述 IQHE 结果 $\sigma_{xy} = \nu e^2/h$ 并用手征边缘态解释；描述劳夫林态及其分数电荷 $e/m$。
9. 定义贝里联络 $\mathbf{A}(\mathbf{k}) = i\langle u|\nabla_{\mathbf{k}}|u\rangle$ 和陈数 $C = (1/2\pi)\int\Omega\,d^2k$；解释 $C$ 为何是整数；给出 SSH 缠绕数，并解释为何 $|t_2| > |t_1|$ 导致受保护的零能边缘态。

When the Fermi-surface picture and the electron–phonon attraction feel solid, you're ready
for **[Phase 5 — Superconductivity](../phase-5-superconductivity/)**, where all of this
finally pays off.

当费米面图像和电子–声子吸引力的概念扎实之后，你就准备好迎接**[第 5 阶段 — 超导](../phase-5-superconductivity/)**了，那里所有这些积累终将开花结果。

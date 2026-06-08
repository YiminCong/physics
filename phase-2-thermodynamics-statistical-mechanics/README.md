# Phase 2 — Thermodynamics & Statistical Mechanics
**第 2 阶段 — 热力学与统计力学**

This phase builds the two pillars that support all subsequent condensed-matter and quantum physics: the macroscopic laws of thermodynamics (laws, potentials, phase transitions) and the statistical mechanics that derives them from counting microstates. Every module follows the Definition → Demonstration → Application format, emphasizing the free-energy minimization principle (which re-emerges in Ginzburg–Landau theory, Module 5.3) and the quantum distribution functions (Fermi–Dirac and Bose–Einstein) that govern virtually every phenomenon in Phases 4 and 5.

本阶段构建支撑后续凝聚态物理和量子物理的两大支柱：热力学宏观定律（定律、热力学势、相变）以及通过统计微观态数目来推导这些规律的统计力学。每个模块均遵循定义 → 演示 → 应用的格式，重点强调自由能极小化原理（该原理在金兹堡–朗道理论，模块 5.3 中再次出现）以及几乎支配第 4、5 阶段所有现象的量子分布函数（费米–狄拉克分布和玻色–爱因斯坦分布）。

## Prerequisites · 预备知识

- **Phase 0** — especially Module 0.5 (probability, mean/variance, Gaussian distributions), which underpins the probabilistic foundations of statistical mechanics.
- **第 0 阶段** — 尤其是模块 0.5（概率、均值/方差、高斯分布），它支撑着统计力学的概率论基础。
- **Phase 1** — Module 1.2 (conservation laws) and Module 1.6 (oscillators), used when counting degrees of freedom and treating lattice vibrations.
- **第 1 阶段** — 模块 1.2（守恒定律）和模块 1.6（振子），在计算自由度和处理晶格振动时会用到。
- This phase is also helpful background for **Phase 3** (Quantum Mechanics), and is assumed knowledge from Phase 3 onward.
- 本阶段也是**第 3 阶段**（量子力学）的有益背景知识，并将作为第 3 阶段及以后的已知内容。

## Modules · 模块

| # | Title · 标题 | |
|---|-------|-|
| [2.1](./module-2.1-laws-of-thermodynamics.md) | The Laws of Thermodynamics · 热力学定律 | |
| [2.2](./module-2.2-thermodynamic-potentials.md) | Thermodynamic Potentials & Maxwell Relations · 热力学势与麦克斯韦关系 | |
| [2.3](./module-2.3-free-energy-phase-transitions.md) | Free Energy & Phase Transitions · 自由能与相变 | ⭐ |
| [2.4](./module-2.4-classical-statistical-mechanics.md) | Classical Statistical Mechanics · 经典统计力学 | |
| [2.5](./module-2.5-quantum-statistics.md) | Quantum Statistics · 量子统计 | ⭐ |
| [2.6](./module-2.6-quantum-gases-applications.md) | Quantum Gases & Applications · 量子气体与应用 | |
| [2.7](./module-2.7-kinetic-theory-and-transport.md) | Kinetic Theory & Transport · 动理论与输运 | |
| [2.8](./module-2.8-brownian-motion-and-the-einstein-relation.md) | Brownian Motion & the Einstein Relation · 布朗运动与爱因斯坦关系 | |

## Phase 2 Checkpoint (blank page) · 第 2 阶段检查点（空白页）

Work through these without notes before moving on.

在继续之前，不看笔记完成以下题目。

1. State the First and Second Laws in differential form. What distinguishes δQ and δW from dU, and why does the distinction matter?
2. Starting from dU = T dS − P dV, derive the Helmholtz free energy F and write down the Maxwell relation it generates. What constraint does F being minimized correspond to?
3. Sketch the Landau free energy F = a(T)η² + bη⁴ for T above, at, and below T_c. Show that η ∝ (T_c − T)^{1/2} below T_c. Name one later module where this same expansion appears.
4. Define the canonical partition function Z, and show how F = −k_BT ln Z connects it to thermodynamics. Apply the equipartition theorem to find U and C_V for a monatomic ideal gas.
5. Write down both the Fermi–Dirac and Bose–Einstein distributions. Explain why the Pauli principle forces the +1 in the denominator for fermions, and what happens when μ → ε_0 for bosons.
6. A metal at low temperature has heat capacity C(T) = γT + βT³. Identify the physical origin of each term and state which phase of this curriculum each term connects to.
7. Sketch the Maxwell–Boltzmann speed distribution and define the mean free path. Starting from the relaxation-time Boltzmann equation, outline how the Drude conductivity σ = ne²τ/m and Ohm's law emerge.

**自测（空白页）**

1. 以微分形式陈述热力学第一定律和第二定律。δQ 和 δW 与 dU 有何区别，这一区别为何重要？
2. 从 dU = T dS − P dV 出发，推导亥姆霍兹自由能 F，并写出由此得到的麦克斯韦关系。F 极小对应什么约束条件？
3. 分别在 T 高于、等于、低于 T_c 时，画出朗道自由能 F = a(T)η² + bη⁴ 的草图。证明在 T < T_c 时 η ∝ (T_c − T)^{1/2}。指出后续哪个模块再次用到该展开。
4. 定义正则配分函数 Z，并说明 F = −k_BT ln Z 如何将其与热力学联系起来。对单原子理想气体运用能均分定理求 U 和 C_V。
5. 写出费米–狄拉克分布和玻色–爱因斯坦分布。解释为什么泡利原理迫使费米子分母中出现 +1，以及当玻色子的 μ → ε_0 时会发生什么。
6. 低温金属的热容为 C(T) = γT + βT³。指出每一项的物理来源，并说明课程中哪个阶段对应每一项。
7. 画出麦克斯韦–玻尔兹曼速率分布草图，定义平均自由程。从弛豫时间玻尔兹曼方程出发，概述德鲁德电导率 σ = ne²τ/m 和欧姆定律是如何得出的。

---

→ Continue to **[Phase 3 — Quantum Mechanics](../phase-3-quantum-mechanics/)**.

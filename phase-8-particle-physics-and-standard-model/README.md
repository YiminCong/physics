# Phase 8 — Particle Physics & the Standard Model
**第 8 阶段 — 粒子物理与标准模型**

Phase 8 develops the quantum field theory of the fundamental particles and forces, building on the gauge-symmetry principle and the machinery of QFT (Phase 6) to construct the Standard Model: QED, QCD, and the electroweak theory, culminating in the Higgs mechanism and the open frontiers beyond. Each module follows the **Definition → Demonstration → Application** format — a tight revision-sheet structure that moves from the core idea, through a worked calculation or derivation, to physical consequences and experimental tests.

第 8 阶段发展基本粒子与基本力的量子场论，以规范对称性原理和量子场论（第 6 阶段）的机制为基础，构建标准模型：量子电动力学、量子色动力学以及电弱理论，最终涵盖希格斯机制与超越标准模型的开放前沿。每个模块遵循**定义 → 演示 → 应用**格式——一种紧凑的复习提纲结构，从核心概念出发，经过具体计算或推导，到达物理后果与实验检验。

---

## Prerequisites · 预备知识

- **Phase 6 — Quantum Field Theory**, especially Module 6.5 (canonical quantization of the Dirac and electromagnetic fields) and Module 6.6 (renormalization and running couplings): the language of Feynman diagrams, propagators, and the renormalization group is used throughout.
- **第 6 阶段 — 量子场论**，尤其是模块 6.5（狄拉克场与电磁场的正则量子化）和模块 6.6（重整化与跑动耦合常数）：费曼图、传播子和重整化群的语言贯穿始终。
- **Phase 1 — Classical Physics**, Modules 1.13–1.15 (special relativity, covariant electromagnetism, the field tensor Fμν): the relativistic and covariant notation underpins every Lagrangian written here.
- **第 1 阶段 — 经典物理**，模块 1.13–1.15（狭义相对论、协变电磁学、场张量 Fμν）：相对论性和协变记号是本阶段所有拉格朗日量的基础。
- **Phase 3 — Quantum Mechanics**, especially Module 3.4 (spin) and Module 3.11 (angular momentum addition): spin-½ fermions, Dirac spinors, and representation theory of SU(2) are assumed.
- **第 3 阶段 — 量子力学**，尤其是模块 3.4（自旋）和模块 3.11（角动量耦合）：自旋 ½ 费米子、狄拉克旋量以及 SU(2) 的表示论均视为已知。

---

## Modules · 模块列表

| Module | Title · 标题 | Priority |
|--------|-------------|----------|
| [8.1](./module-8.1-symmetries-and-gauge-theory.md) | Symmetries & Gauge Theory · 对称性与规范理论 | ⭐ |
| [8.2](./module-8.2-quantum-electrodynamics.md) | Quantum Electrodynamics (QED) · 量子电动力学 | ⭐ |
| [8.3](./module-8.3-quantum-chromodynamics.md) | The Strong Interaction (QCD) · 强相互作用（量子色动力学） | |
| [8.4](./module-8.4-electroweak-theory-and-higgs.md) | Electroweak Theory & the Higgs · 电弱理论与希格斯机制 | ⭐⭐ |
| [8.5](./module-8.5-standard-model-and-beyond.md) | The Standard Model & Beyond · 标准模型及其超越 | |
| [8.6](./module-8.6-particle-physics-and-cosmology.md) | Particle Physics & Cosmology · 粒子物理与宇宙学 | |
| [8.7](./module-8.7-parity-violation-and-the-weak-interaction.md) | Parity Violation & the Weak Interaction (Lee–Yang) · 宇称不守恒与弱相互作用（李–杨） | |

---

## The Central Cross-Link: Higgs = Anderson–Ginzburg–Landau · 核心交叉联系：希格斯 = 安德森–金兹堡–朗道

The single most elegant conceptual thread in the curriculum runs from Phase 2 through Phase 5 to Phase 8. The Landau theory of phase transitions (Module 2.3) introduces spontaneous symmetry breaking via a Mexican-hat free energy. The Ginzburg–Landau theory of superconductivity (Module 5.3) applies this to a charged order parameter, and the Anderson mechanism shows that the photon acquires a mass inside the superconductor — the Meissner effect is a gauge-boson mass. The **Higgs mechanism** (Module 8.4) is precisely this Anderson–Ginzburg–Landau construction applied to the electroweak vacuum: the Higgs field plays the role of the superconducting order parameter, and the W± and Z⁰ acquire mass by "eating" the Goldstone modes, exactly as the photon does inside a superconductor. This is not an analogy — it is the same mathematics, the same symmetry-breaking pattern, and historically the same chain of ideas.

课程中最优美的概念主线从第 2 阶段贯穿第 5 阶段直至第 8 阶段。朗道相变理论（模块 2.3）通过墨西哥帽自由能引入了自发对称性破缺。超导体的金兹堡–朗道理论（模块 5.3）将此应用于带电序参量，安德森机制表明光子在超导体内部获得了质量——迈斯纳效应正是规范玻色子的质量。**希格斯机制**（模块 8.4）正是将这一安德森–金兹堡–朗道构造应用于电弱真空：希格斯场扮演了超导序参量的角色，W± 和 Z⁰ 通过"吃掉"戈德斯通模式而获得质量，与光子在超导体内部的机制完全相同。这不是类比——它们是同一套数学、同一种对称性破缺模式，在历史上也是同一条思想链。

---

## Phase 8 Checkpoint (blank page) · 第 8 阶段检查点（空白页）

1. State the gauge principle. Starting from a free Dirac Lagrangian, derive the QED Lagrangian by demanding local U(1) invariance, and identify every new term introduced.
2. Compare the β-functions of QED and QCD: one has a positive sign, the other negative. Explain the physical origin of each sign and state the physical consequences (screening vs. anti-screening, confinement vs. asymptotic freedom).
3. Explain the Higgs mechanism in the electroweak theory. Which symmetry is broken, what are the Goldstone modes, where do the W± and Z⁰ masses come from, and what is the single remaining physical scalar?
4. What are the three Sakharov conditions? Does the Standard Model satisfy them? If so, why is additional baryogenesis physics required?
5. What is the hierarchy problem, and how does supersymmetry address it? What does the absence of LHC superpartner signals up to ∼ 2 TeV imply?
6. Sketch how the three Standard Model gauge couplings run with energy. What happens at ∼ 10^{16} GeV in a supersymmetric extension, and why is this significant?

**自测（空白页）**

1. 陈述规范原理。从自由狄拉克拉格朗日量出发，通过要求局域 U(1) 不变性推导量子电动力学拉格朗日量，并指出每个新引入的项。
2. 比较量子电动力学与量子色动力学的 β 函数：一个为正，另一个为负。解释每个符号的物理起源，并阐述其物理后果（屏蔽 vs. 反屏蔽，夸克禁闭 vs. 渐近自由）。
3. 解释电弱理论中的希格斯机制。哪个对称性被破缺，戈德斯通模式是什么，W± 和 Z⁰ 的质量从何而来，剩余的单一物理标量是什么？
4. 萨哈罗夫的三个条件是什么？标准模型满足这些条件吗？若满足，为何还需要额外的重子生成物理？
5. 等级问题是什么，超对称如何解决它？大型强子对撞机未能在 ∼ 2 TeV 以下发现超对称伴子意味着什么？
6. 描绘标准模型三个规范耦合常数随能量的跑动情况。在超对称扩展中，∼ 10^{16} GeV 处发生了什么，这为何具有重要意义？

---

Phase 8 stands at the frontier of the curriculum: the Standard Model is the most thoroughly tested physical theory ever constructed, yet it leaves gravity, dark matter, the matter–antimatter asymmetry, and the origin of the fermion mass hierarchy unexplained — making it simultaneously a pinnacle and a signpost toward the next revolution in fundamental physics.

第 8 阶段站在课程的前沿：标准模型是人类有史以来构建的经过最严格检验的物理理论，然而它留下了引力、暗物质、物质–反物质不对称性以及费米子质量等级起源等未解之谜——使其既是一座顶峰，又是通向基础物理学下一场革命的路标。

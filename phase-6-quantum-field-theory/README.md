# Phase 6 — Quantum Field Theory & Many-Body Physics
**第 6 阶段 — 量子场论与多体物理**

This phase delivers the research-level toolkit that underpins both modern condensed matter physics and high-energy particle physics. It extends second quantization with the full apparatus of Green's functions, Feynman diagrams, path integrals, canonical field quantization, and the renormalization group — the shared language in which superconductivity, the Standard Model, and critical phenomena are all written. Each module follows the Definition → Demonstration → Application format: precise definitions first, then a worked derivation or key result, then contact with experiment or the broader theoretical framework.

本阶段提供支撑现代凝聚态物理和高能粒子物理的研究级工具包。它以格林函数、费曼图、路径积分、正则场量子化和重整化群的完整体系扩展二次量子化——这是超导性、标准模型和临界现象共同书写的语言。每个模块遵循定义 → 演示 → 应用的格式：先给出精确定义，再给出推导或关键结果，最后联系实验或更广泛的理论框架。

## Prerequisites · 预备知识

- **Phase 3** (Quantum Mechanics), especially Module 3.10 (Heisenberg picture, propagators, and the path integral) and Module 3.12 (second quantization, creation/annihilation operators, anticommutators).
- **第 3 阶段**（量子力学），尤其是模块 3.10（海森堡绘景、传播子和路径积分）和模块 3.12（二次量子化、产生/湮灭算符、反对易关系）。
- **Phase 1** Special Relativity and covariant electrodynamics (Modules 1.13–1.15) are essential for Module 6.5 (canonical quantization of relativistic fields).
- **第 1 阶段**狭义相对论与协变电动力学（模块 1.13–1.15）是模块 6.5（相对论场的正则量子化）的必备基础。
- **Phase 2** statistical mechanics, particularly Module 2.3 (Landau–Ginzburg free energy), provides the bridge between QFT and critical phenomena exploited in Module 6.6.
- **第 2 阶段**统计力学，尤其是模块 2.3（朗道–金兹堡自由能），提供了模块 6.6 中所利用的 QFT 与临界现象之间的桥梁。
- Familiarity with Phase 5 (Superconductivity), especially Module 5.5 (BCS Hamiltonian), enriches Modules 6.1 and 6.2 substantially.
- 熟悉第 5 阶段（超导性），尤其是模块 5.5（BCS 哈密顿量），将极大地丰富对模块 6.1 和 6.2 的理解。

## Modules · 模块

| Module | Title · 标题 | Stars |
|--------|-------|-------|
| [6.1](./module-6.1-second-quantization.md) | Second Quantization & the Many-Body Problem · 二次量子化与多体问题 | ⭐ |
| [6.2](./module-6.2-greens-functions.md) | Green's Functions & Propagators · 格林函数与传播子 | ⭐ |
| [6.3](./module-6.3-feynman-diagrams.md) | Feynman Diagrams & Perturbation Theory · 费曼图与微扰论 | |
| [6.4](./module-6.4-path-integrals.md) | Path Integrals & Field Theory · 路径积分与场论 | ⭐ |
| [6.5](./module-6.5-canonical-quantization.md) | Canonical Quantization of Fields · 场的正则量子化 | ⭐ |
| [6.6](./module-6.6-renormalization.md) | Renormalization & the Renormalization Group · 重整化与重整化群 | ⭐⭐ |
| [6.7](./module-6.7-exactly-solvable-models-and-long-range-order.md) | Exactly Solvable Models & Long-Range Order · 精确可解模型与长程序 | |

## Further Reading · 延伸阅读

- **Coleman, S.** — *Introduction to Many-Body Physics* (lecture notes): the clearest entry point for non-relativistic field theory from a condensed matter perspective.
- **Coleman, S.** — *Introduction to Many-Body Physics*（讲义）：从凝聚态物理视角切入非相对论场论最清晰的入门材料。
- **Fetter, A. L. & Walecka, J. D.** — *Quantum Theory of Many-Particle Systems*: definitive treatment of Green's functions and the Nambu–Gor'kov formalism for superconductivity.
- **Fetter, A. L. & Walecka, J. D.** — *Quantum Theory of Many-Particle Systems*：格林函数和超导 Nambu–Gor'kov 形式主义的权威处理。
- **Altland, A. & Simons, B.** — *Condensed Matter Field Theory* (2nd ed.): path integrals, Hubbard–Stratonovich, RG, and the bridge to statistical field theory; the standard graduate condensed-matter QFT text.
- **Altland, A. & Simons, B.** — *Condensed Matter Field Theory*（第 2 版）：路径积分、Hubbard–Stratonovich 变换、重整化群及其与统计场论的桥梁；凝聚态 QFT 研究生标准教材。
- **Peskin, M. E. & Schroeder, D. V.** — *An Introduction to Quantum Field Theory*: canonical quantization, Feynman rules, renormalization, and QED from the particle-physics side; pairs naturally with Module 6.5 and 6.6.
- **Peskin, M. E. & Schroeder, D. V.** — *An Introduction to Quantum Field Theory*：从粒子物理角度讲述正则量子化、费曼规则、重整化和 QED；与模块 6.5 和 6.6 自然配对。

## Phase 6 Checkpoint (blank page) · 第 6 阶段检查点（空白页）

1. Write the field operator ψ(x) in terms of single-particle orbitals φ_k(x) and mode operators c_k. Derive the equal-time anticommutator {ψ(x), ψ†(x')} = δ(x − x').
2. Sketch A(k,ω) for (a) a free Fermi gas and (b) a Fermi liquid with weak interactions. What does the width of the quasiparticle peak represent physically?
3. State the Dyson equation G = G⁰ + G⁰ Σ G and solve for G(k,ω). Draw the 1PI self-energy insertion Σ at the Hartree–Fock level.
4. Explain how Wick-rotating the quantum partition function Z = Tr e^{−βĤ} to imaginary time connects quantum field theory to classical statistical mechanics in d+1 dimensions.
5. What is the spin-statistics theorem? Give one consequence for the zero-point energy of a bosonic field versus a fermionic field (Bose versus Fermi statistics of the vacuum).
6. A ferromagnet and a liquid near its critical point exhibit the same critical exponent ν. Use the language of RG fixed points and universality classes to explain why microscopically different systems can share identical critical exponents.

**自测（空白页）**

1. 用单粒子轨道 φ_k(x) 和模式算符 c_k 写出场算符 ψ(x)。推导等时反对易子 {ψ(x), ψ†(x')} = δ(x − x')。
2. 分别画出 (a) 自由费米气体和 (b) 弱相互作用费米液体的谱函数 A(k,ω)。准粒子峰的宽度在物理上代表什么？
3. 陈述戴森方程 G = G⁰ + G⁰ Σ G 并求解 G(k,ω)。在 Hartree–Fock 水平画出单粒子不可约自能插入 Σ。
4. 解释将量子配分函数 Z = Tr e^{−βĤ} 维克转动到虚时间后，如何将量子场论与 d+1 维的经典统计力学联系起来。
5. 什么是自旋-统计定理？给出玻色场与费米场零点能的一个区别（真空的玻色统计与费米统计）。
6. 铁磁体和临界点附近的液体表现出相同的临界指数 ν。用重整化群不动点和普适类的语言解释为什么微观物理完全不同的系统能共享相同的临界指数。

---

→ Continue to **[Phase 7 — General Relativity & Cosmology](../phase-7-general-relativity-and-cosmology/)**, or apply this toolkit to **[Phase 8 — Particle Physics](../phase-8-particle-physics-and-standard-model/)**.

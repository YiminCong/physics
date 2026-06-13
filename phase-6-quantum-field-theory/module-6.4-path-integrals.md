# Module 6.4 — Path Integrals & Field Theory ⭐
**模块 6.4 — 路径积分与场论 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.4-path-integrals-derivations.md)

---

## 1. Feynman's Sum Over Histories · 费曼历史求和

**Definition.** The Feynman path integral (introduced in Module 3.10) expresses the quantum amplitude for a particle to travel from $x_i$ to $x_f$ in time $T$ as a sum over every classical path: $\langle x_f|e^{-i\hat{H}T/\hbar}|x_i\rangle = \int D[x(t)]\, e^{iS[x]/\hbar}$, where $S[x] = \int_0^T dt\, L(x, \dot{x})$ is the classical action (Module 1.3) and $D[x(t)]$ denotes the functional measure — integration over the infinite-dimensional space of all paths. Each path carries a phase $e^{iS/\hbar}$; paths near the classical trajectory ($\delta S = 0$) interfere constructively and dominate in the $\hbar \to 0$ limit, recovering classical mechanics.

**定义。** 费曼路径积分（模块 3.10 中引入）将粒子在时间 $T$ 内从 $x_i$ 传播到 $x_f$ 的量子幅度表示为所有经典路径的求和：$\langle x_f|e^{-i\hat{H}T/\hbar}|x_i\rangle = \int D[x(t)]\, e^{iS[x]/\hbar}$，其中 $S[x] = \int_0^T dt\, L(x, \dot{x})$ 是经典作用量（模块 1.3），$D[x(t)]$ 表示泛函测度——对所有路径所张的无穷维空间的积分。每条路径携带相位 $e^{iS/\hbar}$；经典轨迹（$\delta S = 0$）附近的路径相长干涉，在 $\hbar \to 0$ 极限下占主导，从而还原经典力学。

Passing to a field theory, $x(t)$ is replaced by a field configuration $\phi(x,t)$. The quantum amplitude becomes a functional integral $\int D\phi\, e^{iS[\phi]/\hbar}$ over all field histories. This is the foundation of modern quantum field theory and of the field-theoretic formulation of statistical mechanics.

推广到场论，$x(t)$ 被场构型 $\phi(x,t)$ 取代。量子幅度变成对所有场历史的泛函积分 $\int D\phi\, e^{iS[\phi]/\hbar}$。这是现代量子场论和统计力学场论表述的基础。

**Demonstration.** Performing a Wick rotation $t \to -i\tau$ (imaginary time, $\tau \in [0, \hbar\beta]$ where $\beta = 1/k_B T$) converts the oscillatory factor $e^{iS/\hbar} \to e^{-S_E/\hbar}$, where $S_E$ is the Euclidean action. The quantum partition function becomes $Z = \mathrm{Tr}\, e^{-\beta\hat{H}} = \int_\text{periodic} D\phi\, e^{-S_E[\phi]/\hbar}$ with fields obeying periodic (bosons) or antiperiodic (fermions) boundary conditions in $\tau$. This is formally identical to a classical statistical mechanics partition function in $d+1$ dimensions with inverse temperature $\beta$ playing the role of the imaginary-time extent. The analogy is exact and powerful: finite-temperature QFT and classical statistical field theory are the same mathematical object.

**演示。** 进行维克转动 $t \to -i\tau$（虚时间，$\tau \in [0, \hbar\beta]$，其中 $\beta = 1/k_B T$），将振荡因子 $e^{iS/\hbar} \to e^{-S_E/\hbar}$，其中 $S_E$ 是欧几里得作用量。量子配分函数变为 $Z = \mathrm{Tr}\, e^{-\beta\hat{H}} = \int_\text{periodic} D\phi\, e^{-S_E[\phi]/\hbar}$，场在 $\tau$ 方向满足周期（玻色子）或反周期（费米子）边界条件。这在形式上与 $d+1$ 维的经典统计力学配分函数完全等同，逆温度 $\beta$ 扮演虚时间范围的角色。这一类比是精确而有力的：有限温度 QFT 与经典统计场论是同一数学对象。

**Application.** The effective action $\Gamma[\phi_\text{cl}]$ is defined as the Legendre transform of $\ln Z$ with respect to an external source $J$: it is the generating functional for one-particle-irreducible (1PI) diagrams, and its saddle point $\delta\Gamma/\delta\phi_\text{cl} = 0$ reproduces the classical equations of motion at the quantum level. Expanding $\Gamma$ around a uniform saddle recovers Landau–Ginzburg theory (Module 2.3 and Module 5.3) as the leading approximation; loop corrections give quantum and thermal fluctuations. Altland & Simons "Condensed Matter Field Theory" develops this connection systematically throughout.

**应用。** 有效作用量 $\Gamma[\phi_\text{cl}]$ 定义为 $\ln Z$ 关于外源 $J$ 的勒让德变换：它是单粒子不可约（1PI）图的生成泛函，其鞍点 $\delta\Gamma/\delta\phi_\text{cl} = 0$ 在量子层面重现经典运动方程。将 $\Gamma$ 在均匀鞍点附近展开，以领头近似还原朗道–金兹堡理论（模块 2.3 和模块 5.3）；圈修正给出量子和热涨落。Altland & Simons 的 "Condensed Matter Field Theory" 系统地贯穿全书地发展了这一联系。

---

## 2. Field Integrals for Fermions and Bosons · 费米子与玻色子的场积分

**Definition.** Fermionic field integrals require Grassmann variables — anticommuting numbers $\eta, \bar\eta$ with $\{\eta_i, \eta_j\} = 0$ — because ordinary c-numbers cannot satisfy fermionic statistics. The Gaussian Grassmann integral $\int D\bar\eta\, D\eta\, e^{-\bar\eta A \eta} = \det A$ (note: determinant in the numerator, not denominator as for bosons where $\int D\phi^*\, D\phi\, e^{-\phi^* A \phi} = (\det A)^{-1}$). This sign reversal is the path-integral avatar of Fermi statistics and underlies the fermion determinant in lattice gauge theory and condensed matter calculations. Boson coherent-state path integrals use ordinary complex fields $\phi, \phi^*$.

**定义。** 费米子场积分需要 Grassmann 变量——反对易数 $\eta$、$\bar\eta$，满足 $\{\eta_i, \eta_j\} = 0$——因为普通 c 数无法满足费米统计。高斯 Grassmann 积分为 $\int D\bar\eta\, D\eta\, e^{-\bar\eta A \eta} = \det A$（注意：行列式在分子，而非玻色子情形的分母，玻色子情形 $\int D\phi^*\, D\phi\, e^{-\phi^* A \phi} = (\det A)^{-1}$）。这一符号反转是费米统计在路径积分中的体现，支撑着格规范理论和凝聚态计算中的费米子行列式。玻色子相干态路径积分使用普通复数场 $\phi$、$\phi^*$。

**Demonstration.** For free fermions, integrating out the fermionic fields produces a factor $\det[\partial_\tau - H] = \exp \mathrm{Tr} \ln[\partial_\tau - H]$, which upon expanding $\mathrm{Tr} \ln$ in powers of $H$ generates exactly the linked-cluster expansion of connected Green's functions — the same combinatorics encoded in Feynman diagrams (Module 6.3) but derived here from a single Gaussian integral. The connection is not coincidental: Wick's theorem is the statement that a Gaussian functional integral has only pairwise contractions.

**演示。** 对于自由费米子，积掉费米子场产生因子 $\det[\partial_\tau - H] = \exp \mathrm{Tr} \ln[\partial_\tau - H]$，将 $\mathrm{Tr} \ln$ 按 $H$ 的幂次展开，恰好生成连通格林函数的连通集团展开——与费曼图（模块 6.3）所编码的组合学相同，但这里从单个高斯积分推导出来。这种联系并非巧合：Wick 定理正是高斯泛函积分只有两两缩并这一陈述。

**Application.** The path-integral language is the shared vocabulary of condensed matter and particle physics. In condensed matter: the Hubbard–Stratonovich transformation decouples four-fermion interactions (like BCS pairing) by introducing a bosonic auxiliary field $\Delta(x,\tau)$, and the saddle point of the resulting bosonic action recovers the BCS gap equation; fluctuations around the saddle give Goldstone modes and the Ginzburg–Landau effective theory (Module 5.3). In particle physics: the path integral over gauge fields defines QED and the Standard Model (Phase 8), and the Fadeev–Popov procedure handles gauge redundancy.

**应用。** 路径积分语言是凝聚态与粒子物理的共同词汇。在凝聚态中：Hubbard–Stratonovich 变换通过引入玻色辅助场 $\Delta(x,\tau)$ 解耦四费米子相互作用（如 BCS 配对），所得玻色作用量的鞍点还原 BCS 能隙方程；鞍点附近的涨落给出 Goldstone 模式和金兹堡–朗道有效理论（模块 5.3）。在粒子物理中：对规范场的路径积分定义了 QED 和标准模型（第 8 阶段），Fadeev–Popov 程序处理规范冗余。

## Key results · 核心结果

- $\langle f|i\rangle = \int\mathcal{D}\phi\; e^{iS[\phi]/\hbar}$ — sum over histories · 历史求和
- Stationary phase $\delta S = 0$ recovers the classical path · 稳相近似给出经典路径
- Wick rotation to imaginary time ($\beta = 1/k_B T$) links QFT to statistical mechanics · 虚时间将场论与统计力学相连
- Fermions need anticommuting Grassmann fields · 费米子需反对易的格拉斯曼场

---

## Self-test (blank page) · 自测（空白页）

1. Write the path-integral expression for $\langle x_f|e^{-i\hat{H}T/\hbar}|x_i\rangle$ and explain why the classical path dominates in the $\hbar \to 0$ limit.
2. Perform a Wick rotation $t \to -i\tau$. Show that the quantum partition function $Z = \mathrm{Tr}\, e^{-\beta\hat{H}}$ becomes a Euclidean functional integral. What boundary conditions do bosonic and fermionic fields obey?
3. Why must Grassmann variables be used in the fermionic path integral? How does the Gaussian Grassmann integral differ in sign from the bosonic case, and what physical principle does this reflect?

**自测（空白页）**

1. 写出 $\langle x_f|e^{-i\hat{H}T/\hbar}|x_i\rangle$ 的路径积分表达式，并解释为何经典路径在 $\hbar \to 0$ 极限下占主导。
2. 进行维克转动 $t \to -i\tau$。证明量子配分函数 $Z = \mathrm{Tr}\, e^{-\beta\hat{H}}$ 变成欧几里得泛函积分。玻色子场和费米子场各满足什么边界条件？
3. 为什么费米子路径积分必须使用 Grassmann 变量？高斯 Grassmann 积分与玻色子情形在符号上有何不同，这反映了什么物理原理？

---

← Previous: [Module 6.3 — Feynman Diagrams & Perturbation Theory](./module-6.3-feynman-diagrams.md) · [Phase 6 index](./README.md) · Next: [Module 6.5 — Canonical Quantization of Fields](./module-6.5-canonical-quantization.md) →

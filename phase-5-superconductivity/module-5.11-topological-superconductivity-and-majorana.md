# Module 5.11 — Topological Superconductivity & Majorana Modes
**模块 5.11 — 拓扑超导与马约拉纳模**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.11-topological-superconductivity-and-majorana-derivations.md)

---

## 1. Majorana Fermions & the Kitaev Chain · 马约拉纳费米子与基塔耶夫链

**Definition.** A **Majorana fermion** is a particle that is its own antiparticle. In the condensed-matter context this means a quasiparticle mode described by a Hermitian operator γ satisfying:

**定义。** **马约拉纳费米子**是自身的反粒子。在凝聚态语境中，这意味着由满足如下条件的厄米算符 γ 描述的准粒子模：

  γ = γ†,    {γ_i, γ_j} = 2δ_{ij}.

Unlike an ordinary complex fermion c (with c ≠ c†), a Majorana mode is "half a fermion" — it carries no well-defined charge and its occupation is not a meaningful quantum number by itself. Two Majorana operators γ₁ and γ₂ can be combined into one ordinary fermion: f = (γ₁ + iγ₂)/2, f† = (γ₁ − iγ₂)/2, with {f, f†} = 1. The two degenerate ground states |0⟩ and f†|0⟩ = |1⟩ differ in fermion parity but are energetically degenerate — this is the **topological ground-state degeneracy** that makes Majorana modes interesting for quantum computation.

与普通复费米子 c（c ≠ c†）不同，马约拉纳模是"半个费米子"——它不携带明确定义的电荷，其本身的占据数也不是有意义的量子数。两个马约拉纳算符 γ₁ 和 γ₂ 可以组合成一个普通费米子：f = (γ₁ + iγ₂)/2，f† = (γ₁ − iγ₂)/2，满足 {f, f†} = 1。两个简并基态 |0⟩ 和 f†|0⟩ = |1⟩ 具有不同的费米子宇称，但能量简并——这就是使马约拉纳模在量子计算中引人注目的**拓扑基态简并**。

**The Kitaev chain.** Alexei Kitaev (2001) proposed the minimal model: a 1D lattice of N spinless fermion sites with nearest-neighbor hopping t, p-wave pairing Δ, and chemical potential μ. The Hamiltonian is:

**基塔耶夫链。** Alexei Kitaev（2001 年）提出了最简模型：N 个格点上的一维无自旋费米子格链，具有最近邻跳跃 t、p 波配对 Δ 和化学势 μ。哈密顿量为：

  H = −μ Σ_j c_j† c_j  −  t Σ_j (c_j† c_{j+1} + h.c.)  +  Δ Σ_j (c_j c_{j+1} + h.c.)

where c_j, c_j† are spinless fermion operators on site j. The key feature is the **p-wave** (odd-parity) pairing term c_j c_{j+1}: unlike s-wave pairing c_j↑ c_j↓ between opposite spins on the same site, p-wave pairing pairs fermions on adjacent sites.

其中 c_j、c_j† 是格点 j 上的无自旋费米子算符。关键特征是 **p 波**（奇宇称）配对项 c_j c_{j+1}：不同于 s 波配对（同一格点上自旋相反的 c_j↑ c_j↓），p 波配对将相邻格点上的费米子配对。

**Topological vs trivial phases.** The phase diagram is controlled by the ratio |μ|/2t:

**拓扑相与平庸相。** 相图由比值 |μ|/2t 控制：

- **Trivial phase** (|μ| > 2t): the chain is gapped, no end modes, the ground state is unique. Every site is paired locally.
- **Topological phase** (|μ| < 2t): the chain has a **bulk gap** and **two unpaired Majorana zero modes** γ_L and γ_R localized at the two ends. The ground state is **two-fold degenerate** (the delocalized fermion f = (γ_L + iγ_R)/2 can be empty or filled at zero energy cost).

- **平庸相**（|μ| > 2t）：链有能隙，无端模，基态唯一。每个格点局域配对。
- **拓扑相**（|μ| < 2t）：链具有**体能隙**和两个局域在两端的**未配对马约拉纳零模** γ_L 和 γ_R。基态**二度简并**（非局域费米子 f = (γ_L + iγ_R)/2 以零能代价可以为空或占据）。

The special point Δ = t, μ = 0 has exact Majorana end modes with zero correlation between the two ends, making the physics transparent (see Derivations).

特殊点 Δ = t，μ = 0 具有精确的马约拉纳端模，两端之间零关联，使物理图像变得透明（见推导）。

**Demonstration.** Rewrite the Kitaev chain in Majorana operators γ_{j,A} = c_j + c_j† and γ_{j,B} = i(c_j† − c_j). At the special point t = Δ > 0 and μ = 0, the Hamiltonian becomes (see Derivations A):

**演示。** 用马约拉纳算符 γ_{j,A} = c_j + c_j† 和 γ_{j,B} = i(c_j† − c_j) 改写基塔耶夫链。在特殊点 t = Δ > 0 且 μ = 0 处，哈密顿量变为（见推导 A）：

  H = −it Σ_{j=1}^{N−1} γ_{j,B} γ_{j+1,A}

This pairs γ_{j,B} on site j with γ_{j+1,A} on site j+1, leaving **γ_{1,A}** (left end) and **γ_{N,B}** (right end) completely absent from H: they cost no energy. These two unpaired Majorana operators are the end modes. The bulk modes form pairs (γ_{j,B}, γ_{j+1,A}) → ordinary fermions with gap 2t.

这将格点 j 上的 γ_{j,B} 与格点 j+1 上的 γ_{j+1,A} 配对，使 **γ_{1,A}**（左端）和 **γ_{N,B}**（右端）完全不出现在 H 中：它们不需要任何能量。这两个未配对的马约拉纳算符就是端模。体模形成 (γ_{j,B}, γ_{j+1,A}) 对 → 普通费米子，能隙为 2t。

**Application.** The Kitaev chain is the universal toy model for **topological superconductivity**. Its topological invariant is a Z₂ index (the Pfaffian invariant / Majorana number): trivial when the bulk Hamiltonian has no winding in the Brillouin zone, non-trivial (= −1) in the topological phase. The phase boundary |μ| = 2t is a bulk gap-closing transition (a topological phase transition).

**应用。** 基塔耶夫链是**拓扑超导**的通用玩具模型。其拓扑不变量是 Z₂ 指标（普法夫指标/马约拉纳数）：当体哈密顿量在布里渊区中无绕数时为平庸，拓扑相中为非平庸（= −1）。相边界 |μ| = 2t 是体能隙关闭的相变（拓扑相变）。

---

## 2. Realizations & Applications · 实现与应用

**Definition.** Physical electrons carry spin, so a **spinless** p-wave superconductor must be engineered. The **Lutchyn–Oreg proposal** (2010) achieves this in a semiconductor nanowire:

**定义。** 物理电子携带自旋，因此**无自旋** p 波超导体必须被人工构造。**Lutchyn–Oreg 方案**（2010 年）在半导体纳米线中实现了这一点：

1. **Semiconductor nanowire** (e.g. InAs or InSb) with strong spin–orbit coupling (Rashba effect), which splits the spin subbands in k-space.
2. **Proximity-coupled s-wave superconductor** (e.g. Al), which induces a pairing gap Δ_ind via the proximity effect (Module 5.10).
3. **Zeeman field** B applied along the wire axis, which Zeeman-splits the spin subbands by V_Z = g μ_B B/2.

1. **半导体纳米线**（如 InAs 或 InSb），具有强自旋轨道耦合（拉什巴效应），在 k 空间中分裂自旋子带。
2. **邻近耦合 s 波超导体**（如 Al），通过邻近效应（模块 5.10）诱导配对能隙 Δ_ind。
3. 沿线轴施加的**塞曼场** B，使自旋子带产生塞曼分裂 V_Z = g μ_B B/2。

When V_Z > √(Δ_ind² + μ²), the system enters a **topological superconducting phase**: the lowest transverse subband is effectively spinless (its two spin components are hybridized by spin–orbit coupling into one chiral mode), and the proximity-induced pairing acts as p-wave pairing on this spinless band. The two ends of the wire host Majorana zero modes.

当 V_Z > √(Δ_ind² + μ²) 时，系统进入**拓扑超导相**：最低横向子带有效上是无自旋的（其两个自旋分量通过自旋轨道耦合混合为一个手征模），邻近诱导的配对在该无自旋能带上表现为 p 波配对。纳米线两端寄宿马约拉纳零模。

**The zero-bias conductance peak.** A normal-metal tunneling contact to one end of the topological wire measures the local density of states. A Majorana zero mode at the tip produces a **zero-bias peak** (ZBP) in the differential conductance dI/dV at V = 0, with quantized height 2e²/h (the Majorana conductance quantum from perfect Andreev reflection). This peak appears when B exceeds the topological threshold and disappears when the wire is driven back to the trivial phase.

**零偏置电导峰。** 拓扑线一端的正常金属隧穿接触测量局域态密度。端部马约拉纳零模在微分电导 dI/dV 的 V = 0 处产生**零偏置峰**（ZBP），高度量子化为 2e²/h（来自完美安德烈夫反射的马约拉纳电导量子）。当 B 超过拓扑阈值时此峰出现，当线驱动回平庸相时消失。

**Demonstration.** Mourik et al. (Science, 2012) observed a zero-bias peak in InSb nanowire / Al devices evolving with magnetic field precisely as predicted for Majorana modes: the peak emerges above a threshold field and is robust over a range of gate voltages (which tune μ). Subsequent experiments mapped the peak's evolution across multiple devices and parameter ranges, while also identifying trivial mechanisms (e.g. disorder-induced Andreev bound states) that can mimic ZBPs — distinguishing these from true Majorana modes remains an active experimental challenge.

**演示。** Mourik 等人（《科学》，2012 年）在 InSb 纳米线/Al 器件中观察到零偏置峰随磁场的演化，与马约拉纳模的预测完全一致：峰在超过阈值磁场后出现，在一定栅极电压范围内（调节 μ）保持稳定。后续实验在多个器件和参数范围内映射了峰值的演化，同时也识别出能够模仿 ZBP 的平庸机制（如无序诱导的安德烈夫束缚态）——将这些与真正的马约拉纳模区分开来仍然是一个活跃的实验挑战。

**Non-Abelian exchange statistics.** Ordinary fermions and bosons acquire a phase ±1 under particle exchange. In 2+1 dimensions (or effectively 1D topological wires arranged in T-junction networks), Majorana modes obey **non-Abelian statistics**: exchanging (braiding) two Majorana modes γ_i and γ_j applies the unitary transformation:

**非阿贝尔交换统计。** 普通费米子和玻色子在粒子交换下获得相位 ±1。在 2+1 维（或等效地，排列成 T 结网络的一维拓扑线中），马约拉纳模遵从**非阿贝尔统计**：交换（编织）两个马约拉纳模 γ_i 和 γ_j 施加酉变换：

  U_{ij} = exp(π γ_i γ_j / 4) = (1 + γ_i γ_j) / √2.

Because these transformations do not commute (U_{12} U_{23} ≠ U_{23} U_{12}), sequential braidings can perform universal quantum gates on the degenerate ground-state subspace. This is the basis for **topological quantum computation**: braiding Majorana modes is inherently fault-tolerant because the quantum information is stored nonlocally (split between the two end modes) and local perturbations cannot distinguish the two ground states.

由于这些变换不对易（U_{12} U_{23} ≠ U_{23} U_{12}），序贯编织可以在简并基态子空间上执行通用量子门。这是**拓扑量子计算**的基础：编织马约拉纳模本身具有容错性，因为量子信息是非局域存储的（分散在两个端模之间），局域扰动无法区分两个基态。

**Application.** Topological qubits based on Majorana modes are a central target of quantum computing research (notably Microsoft's Station Q program). The non-Abelian braiding operations, once demonstrated, would implement quantum gates at the hardware level with intrinsic protection against decoherence — a fundamentally different approach from error-corrected qubits in superconducting or trapped-ion platforms.

**应用。** 基于马约拉纳模的拓扑量子比特是量子计算研究的核心目标（尤其是微软 Station Q 项目）。一旦得到演示，非阿贝尔编织操作将在硬件层面实现量子门，具有对退相干的本征保护——这是与超导或囚禁离子平台中纠错量子比特根本不同的方法。

---

**Self-test (blank page)**

1. Define a Majorana fermion operator and explain in what sense it is "half a fermion." Show how two Majorana operators γ₁, γ₂ combine into one ordinary fermion.
2. Write the Kitaev chain Hamiltonian and state the condition on μ and t that places it in the topological phase.
3. Describe what happens to the Kitaev chain Hamiltonian at the special point t = Δ, μ = 0 when rewritten in Majorana operators. Which modes are unpaired?
4. Explain the Lutchyn–Oreg proposal: which three physical ingredients are needed, and what is the topological criterion in terms of V_Z, Δ_ind, and μ?
5. What is a zero-bias conductance peak, and why does a Majorana zero mode produce one with height 2e²/h?
6. State the braiding rule for two Majorana modes and explain why non-Abelian statistics enables fault-tolerant quantum computation.

**自测（空白页）**

1. 定义马约拉纳费米子算符，并解释它在何种意义上是"半个费米子"。说明两个马约拉纳算符 γ₁、γ₂ 如何组合为一个普通费米子。
2. 写出基塔耶夫链哈密顿量，并给出使其处于拓扑相的 μ 与 t 的条件。
3. 描述基塔耶夫链哈密顿量在特殊点 t = Δ、μ = 0 处用马约拉纳算符改写后的情况。哪些模未被配对？
4. 解释 Lutchyn–Oreg 方案：需要哪三种物理成分？用 V_Z、Δ_ind 和 μ 表达拓扑判据。
5. 什么是零偏置电导峰？为何马约拉纳零模产生高度为 2e²/h 的零偏置峰？
6. 陈述两个马约拉纳模的编织规则，并解释非阿贝尔统计如何实现容错量子计算。

---

← Previous: [Module 5.10 — Bogoliubov–de Gennes & Andreev Reflection](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection.md) · [Phase 5 index](./README.md) · Next: [Phase 6 — Quantum Field Theory & Many-Body Physics](../phase-6-quantum-field-theory/README.md) →

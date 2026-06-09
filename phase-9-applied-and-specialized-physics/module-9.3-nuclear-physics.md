---
title: "Module 9.3 — Nuclear Physics"
parent: "Phase 9 — Applied & Specialized Physics"
nav_order: 3
---

# Module 9.3 — Nuclear Physics
**模块 9.3 — 核物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.3-nuclear-physics-derivations.md)

---

## 1. The Nuclear Force & Binding Energy · 核力与结合能

**Definition.** The **nuclear force** (residual strong interaction) is short-ranged ($\sim 1\text{–}2$ fm), charge-independent, and strongly attractive at 1–2 fm but repulsive at shorter range (hard core). The **binding energy** $B(Z, N)$ of a nucleus with $Z$ protons and $N$ neutrons is the energy required to disassemble it into free nucleons:

$$ B(Z, N) = [Z m_p + N m_n - M(Z, N)]\, c^2, $$

where $M(Z, N)$ is the nuclear mass. The **binding energy per nucleon** $B/A$ ($A = Z + N$) peaks near $A \approx 56$ (iron group) at about 8.8 MeV/nucleon, with lighter and heavier nuclei being less tightly bound.

**定义。** **核力**（残余强相互作用）是短程的（$\sim 1\text{–}2$ fm），与电荷无关，在 1–2 fm 处强烈吸引，在更短距离处排斥（硬核）。质子数 $Z$、中子数 $N$ 的核的**结合能** $B(Z, N)$ 是将其拆解为自由核子所需的能量：

$$ B(Z, N) = [Z m_p + N m_n - M(Z, N)]\, c^2, $$

其中 $M(Z, N)$ 为核质量。**每核子结合能** $B/A$（$A = Z + N$）在 $A \approx 56$（铁族）附近取最大值约 8.8 MeV/核子，较轻和较重的核结合得不那么紧密。

**Demonstration.** The binding energy curve explains why fusion of light nuclei (H → He) and fission of heavy nuclei (${}^{235}\text{U} \to$ fission products) both release energy — both move nuclei toward the $B/A$ maximum. The binding energy of ${}^4\text{He}$ (alpha particle) is 28.3 MeV, giving $B/A = 7.07$ MeV — notably high for such a light nucleus, reflecting the closed-shell (magic number) stability.

**演示。** 结合能曲线解释了为何轻核聚变（H → He）和重核裂变（${}^{235}\text{U} \to$ 裂变产物）都释放能量——两者都将核移向 $B/A$ 最大值。${}^4\text{He}$（$\alpha$ 粒子）的结合能为 28.3 MeV，给出 $B/A = 7.07$ MeV——对如此轻的核来说特别高，反映了闭壳层（幻数）稳定性。

**Application.** The binding energy curve is the thermodynamic basis of nuclear power and nuclear weapons. Precision measurements of nuclear masses (by mass spectrometry or trap experiments) directly probe nuclear structure through $B(Z, N)$.

**应用。** 结合能曲线是核能和核武器的热力学基础。核质量的精密测量（通过质谱仪或离子阱实验）通过 $B(Z, N)$ 直接探测核结构。

---

## 2. The Semi-Empirical Mass Formula (Bethe–Weizsäcker) · 半经验质量公式（贝特–魏茨泽克）

**Definition.** The **semi-empirical mass formula (SEMF)** models $B(Z, N)$ with five terms inspired by the liquid-drop analogy and quantum-mechanical corrections:

$$ B(Z, N) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(N-Z)^2}{4A} + \delta(A, Z) $$

where:
- **Volume term** $a_V A$: each nucleon is bound by its neighbors (like bulk liquid).
- **Surface term** $-a_S A^{2/3}$: surface nucleons have fewer neighbors (reduces binding).
- **Coulomb term** $-a_C Z(Z-1)/A^{1/3}$: proton–proton electrostatic repulsion.
- **Asymmetry term** $-a_A(N-Z)^2/(4A)$: Pauli principle penalizes unequal $N$ and $Z$.
- **Pairing term** $\delta$: $+a_P/A^{1/2}$ (even–even), $0$ (odd-$A$), $-a_P/A^{1/2}$ (odd–odd).

Fitted values: $a_V \approx 15.8$ MeV, $a_S \approx 18.3$ MeV, $a_C \approx 0.72$ MeV, $a_A \approx 23.2$ MeV, $a_P \approx 12$ MeV.

**定义。** **半经验质量公式（SEMF）**用受液滴类比和量子力学修正启发的五项来模拟 $B(Z, N)$：

$$ B(Z, N) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}} - a_A \frac{(N-Z)^2}{4A} + \delta(A, Z) $$

其中：
- **体积项** $a_V A$：每个核子被其邻居束缚（类似体相液体）。
- **表面项** $-a_S A^{2/3}$：表面核子邻居较少（减少结合）。
- **库仑项** $-a_C Z(Z-1)/A^{1/3}$：质子–质子静电排斥。
- **不对称项** $-a_A(N-Z)^2/(4A)$：泡利原理惩罚不相等的 $N$ 和 $Z$。
- **配对项** $\delta$：$+a_P/A^{1/2}$（偶–偶），$0$（奇 $A$），$-a_P/A^{1/2}$（奇–奇）。

拟合值：$a_V \approx 15.8$ MeV，$a_S \approx 18.3$ MeV，$a_C \approx 0.72$ MeV，$a_A \approx 23.2$ MeV，$a_P \approx 12$ MeV。

**Demonstration.** Maximizing $B(Z, N)$ at fixed $A$ over $Z$ gives the stability valley: $Z_\text{stable} \approx A/(2 + 0.015A^{2/3})$, which approaches $Z = N$ for light nuclei and shifts toward $N > Z$ for heavy nuclei (where Coulomb repulsion pushes stability toward more neutrons). The formula reproduces the observed binding energies to within $\sim 1\%$ for most nuclei.

**演示。** 在固定 $A$ 下对 $Z$ 最大化 $B(Z, N)$ 给出稳定性谷：$Z_\text{stable} \approx A/(2 + 0.015A^{2/3})$，对轻核趋近于 $Z = N$，对重核向 $N > Z$ 偏移（库仑排斥推动稳定性向更多中子方向）。该公式对大多数核的结合能精度在 $\sim 1\%$ 以内。

**Application.** The SEMF predicts which nuclei undergo alpha or beta decay (from the stability valley), estimates fission energy release $Q$, and guides nuclear structure models. The full derivation of all five terms appears in the Derivations file.

**应用。** SEMF 预测哪些核发生 $\alpha$ 或 $\beta$ 衰变（来自稳定性谷），估算裂变能量释放 $Q$，并指导核结构模型。所有五项的完整推导见推导文件。

---

## 3. The Nuclear Shell Model & Magic Numbers · 核壳层模型与幻数

**Definition.** The **nuclear shell model** treats each nucleon as moving independently in an average potential (Woods–Saxon potential, plus a strong spin–orbit term $V_\text{SO} \propto \mathbf{L} \cdot \mathbf{S}$). The resulting single-particle energy levels group into shells separated by gaps. Nuclei with **magic numbers** of protons or neutrons (2, 8, 20, 28, 50, 82, 126) are especially tightly bound because these numbers correspond to closed shells.

**定义。** **核壳层模型**将每个核子视为在平均势（伍兹–萨克森势加上强自旋–轨道项 $V_\text{SO} \propto \mathbf{L} \cdot \mathbf{S}$）中独立运动。所得单粒子能级分组成被能隙分隔的壳层。质子或中子数为**幻数**（2、8、20、28、50、82、126）的核特别稳定，因为这些数字对应于闭壳层。

**Demonstration.** The spin–orbit term (much stronger than in atomic physics, with opposite sign convention) splits each $(n, l)$ level into two: $j = l + \tfrac12$ and $j = l - \tfrac12$. The $1f_{7/2}$ level is pushed down by the spin–orbit interaction, creating the gap at $N = 28$. Without the spin–orbit term the predicted magic numbers (2, 8, 20, 40, …) do not match observation beyond 20.

**演示。** 自旋–轨道项（比原子物理中强得多，且符号约定相反）将每个 $(n, l)$ 能级分裂为两个：$j = l + \tfrac12$ 和 $j = l - \tfrac12$。自旋–轨道相互作用将 $1f_{7/2}$ 能级向下推，在 $N = 28$ 处产生能隙。没有自旋–轨道项，预测的幻数（2、8、20、40、…）在 20 以上与实验不符。

**Application.** Magic-number nuclei have anomalously high binding energy, low neutron-capture cross sections, and are the endpoints of many decay chains. Doubly magic nuclei (${}^4\text{He}$, ${}^{16}\text{O}$, ${}^{40}\text{Ca}$, ${}^{48}\text{Ca}$, ${}^{132}\text{Sn}$, ${}^{208}\text{Pb}$) are of particular experimental interest.

**应用。** 幻数核具有异常高的结合能、低中子俘获截面，并且是许多衰变链的终点。双幻数核（${}^4\text{He}$、${}^{16}\text{O}$、${}^{40}\text{Ca}$、${}^{48}\text{Ca}$、${}^{132}\text{Sn}$、${}^{208}\text{Pb}$）具有特别重要的实验意义。

---

## 4. Radioactive Decay Law · 放射性衰变定律

**Definition.** Radioactive decay is a quantum tunneling or weak-interaction process that is **random and memoryless**: the probability of decay per unit time is a constant $\lambda$ (the **decay constant**), independent of the age of the nucleus. If $N(t)$ is the number of undecayed nuclei, then:

$$ \frac{dN}{dt} = -\lambda N \quad\Longrightarrow\quad N(t) = N_0\, e^{-\lambda t}. $$

The **half-life** $t_{1/2} = \ln 2 / \lambda$ is the time for $N$ to fall to $N_0/2$. The **activity** $A = \lambda N$ gives the decay rate (SI unit: becquerel, $\text{Bq} = 1$ decay/s).

**定义。** 放射性衰变是一个量子隧穿或弱相互作用过程，是**随机且无记忆的**：单位时间内衰变的概率是常数 $\lambda$（**衰变常数**），与核的"年龄"无关。若 $N(t)$ 为未衰变核数，则：

$$ \frac{dN}{dt} = -\lambda N \quad\Longrightarrow\quad N(t) = N_0\, e^{-\lambda t}. $$

**半衰期** $t_{1/2} = \ln 2 / \lambda$ 是 $N$ 降至 $N_0/2$ 所需的时间。**活度** $A = \lambda N$ 给出衰变率（SI 单位：贝可，$\text{Bq} = 1$ 次衰变/s）。

**Demonstration.** Carbon-14 has $t_{1/2} = 5730$ years ($\lambda = 1.21 \times 10^{-4}\ \text{yr}^{-1}$). A sample whose ${}^{14}\text{C}$ activity is 25% of the living reference value has decayed for $2t_{1/2} \approx 11\,460$ years. This is **radiocarbon dating**. The decay law derivation and half-life formula are in the Derivations file.

**演示。** 碳-14 的 $t_{1/2} = 5730$ 年（$\lambda = 1.21 \times 10^{-4}\ \text{yr}^{-1}$）。${}^{14}\text{C}$ 活度为活体参考值 25% 的样品已衰变了 $2t_{1/2} \approx 11\,460$ 年。这就是**放射性碳定年法**。衰变定律的推导和半衰期公式见推导文件。

**Application.** Radioactive decay chains (uranium series: ${}^{238}\text{U} \to \ldots \to {}^{206}\text{Pb}$) are used for geochronology and cosmochemistry. The secular equilibrium condition ($\lambda_1 N_1 = \lambda_2 N_2 = \ldots$) describes multi-step chains in steady state.

**应用。** 放射性衰变链（铀系：${}^{238}\text{U} \to \ldots \to {}^{206}\text{Pb}$）用于地质年代学和宇宙化学。长期平衡条件（$\lambda_1 N_1 = \lambda_2 N_2 = \ldots$）描述多步链的稳态。

---

## 5. Alpha, Beta, and Gamma Decay · $\alpha$、$\beta$ 和 $\gamma$ 衰变

**Definition.** The three main decay modes are:
- **$\alpha$ decay**: nucleus emits a ${}^4\text{He}$ nucleus. Requires quantum tunneling through the Coulomb barrier (Gamow factor). Decay energy $Q_\alpha = B(\text{daughter}) + B(\alpha) - B(\text{parent})$.
- **$\beta$ decay**: a neutron converts to a proton ($\beta^-$, via $W^-$ boson: $n \to p + e^- + \bar{\nu}_e$) or vice versa ($\beta^+$, or electron capture). Governed by the weak interaction.
- **$\gamma$ decay**: nucleus in an excited state emits a photon, transitioning to a lower nuclear state; electromagnetic, governed by selection rules analogous to atomic E1, M1, E2 transitions.

**定义。** 三种主要衰变方式为：
- **$\alpha$ 衰变**：核发射一个 ${}^4\text{He}$ 核。需要通过库仑势垒的量子隧穿（伽莫夫因子）。衰变能 $Q_\alpha = B(\text{子核}) + B(\alpha) - B(\text{母核})$。
- **$\beta$ 衰变**：中子转变为质子（$\beta^-$，通过 $W^-$ 玻色子：$n \to p + e^- + \bar{\nu}_e$）或反之（$\beta^+$，或电子俘获）。由弱相互作用支配。
- **$\gamma$ 衰变**：处于激发态的核发射光子，跃迁到较低核态；电磁性质，由类似于原子 E1、M1、E2 跃迁的选择规则支配。

**Demonstration.** For ${}^{226}\text{Ra} \to {}^{222}\text{Rn} + {}^4\text{He}$, $Q_\alpha = 4.87\ \text{MeV} > 0$ (energetically allowed) yet the half-life is 1600 years — the Coulomb barrier ($\sim 30$ MeV peak) is far higher than $Q_\alpha$, so the alpha must tunnel. The exponential sensitivity of the tunneling probability to $Q$ explains the enormous range of alpha half-lives ($10^{-7}$ s to $10^{10}$ yr) with only modest variation in $Q$ (4–9 MeV) — the **Geiger–Nuttall law**.

**演示。** 对于 ${}^{226}\text{Ra} \to {}^{222}\text{Rn} + {}^4\text{He}$，$Q_\alpha = 4.87\ \text{MeV} > 0$（能量上允许），但半衰期为 1600 年——库仑势垒峰值（$\sim 30$ MeV）远高于 $Q_\alpha$，因此 $\alpha$ 粒子必须隧穿。隧穿概率对 $Q$ 的指数级敏感性解释了 $\alpha$ 半衰期的巨大范围（$10^{-7}$ s 到 $10^{10}$ yr），而 $Q$ 的变化仅很适中（4–9 MeV）——**盖革–纳托尔定律**。

**Application.** Alpha emitters are used in smoke detectors (${}^{241}\text{Am}$), radioisotope thermoelectric generators, and targeted cancer therapy. Beta decay enables nuclear medicine (PET imaging uses $\beta^+$ emitters). The Gamow factor connects nuclear physics to stellar nucleosynthesis rates.

**应用。** $\alpha$ 发射体用于烟雾探测器（${}^{241}\text{Am}$）、放射性同位素热电发生器和靶向癌症治疗。$\beta$ 衰变支撑核医学（PET 成像使用 $\beta^+$ 发射体）。伽莫夫因子将核物理与恒星核合成速率联系起来。

---

## 6. Fission, Fusion, and Q-Values · 裂变、聚变与 Q 值

**Definition.** The **Q-value** of a nuclear reaction is the energy released ($Q > 0$) or absorbed ($Q < 0$):

$$ Q = \left(\sum m_\text{initial} - \sum m_\text{final}\right) c^2 = B(\text{products}) - B(\text{reactants}). $$

**Fission**: a heavy nucleus ($A \sim 240$) splits into two medium-mass fragments; $Q \sim 200$ MeV per fission event (e.g., ${}^{235}\text{U} + n \to {}^{141}\text{Ba} + {}^{92}\text{Kr} + 3n$, $Q \approx 173$ MeV prompt). **Fusion**: two light nuclei merge; e.g., $\text{D} + \text{T} \to {}^4\text{He} + n$, $Q = 17.6$ MeV — a much higher $Q$ per nucleon than fission.

**定义。** 核反应的 **Q 值**是释放（$Q > 0$）或吸收（$Q < 0$）的能量：

$$ Q = \left(\sum m_\text{初始} - \sum m_\text{末态}\right) c^2 = B(\text{产物}) - B(\text{反应物}). $$

**裂变**：重核（$A \sim 240$）分裂成两个中等质量碎片；每次裂变事件 $Q \sim 200$ MeV（例如，${}^{235}\text{U} + n \to {}^{141}\text{Ba} + {}^{92}\text{Kr} + 3n$，瞬发 $Q \approx 173$ MeV）。**聚变**：两个轻核合并；例如，$\text{D} + \text{T} \to {}^4\text{He} + n$，$Q = 17.6$ MeV——每核子的 Q 值远高于裂变。

**Demonstration.** The SEMF gives $Q$ for symmetric fission of ${}^{236}\text{U}^*$ by comparing $B({}^{236}\text{U})$ to $2\times B({}^{118}\text{Pd})$: the surface-energy cost of splitting one large drop into two smaller ones is more than offset by the Coulomb energy released, making fission exothermic above $A \sim 90$. The critical condition for a self-sustaining chain reaction is $k = 1$ (criticality), where $k$ is the neutron multiplication factor.

**演示。** SEMF 通过比较 $B({}^{236}\text{U})$ 与 $2\times B({}^{118}\text{Pd})$ 给出 ${}^{236}\text{U}^*$ 对称裂变的 $Q$：将一个大液滴分裂成两个小液滴的表面能代价被释放的库仑能量所抵消，使得 $A \sim 90$ 以上的裂变放热。自持链式反应的临界条件为 $k = 1$（临界度），其中 $k$ 为中子增殖因子。

**Application.** Nuclear reactors exploit fission (with controlled $k < 1$ for power, $k = 1$ for steady operation). Fusion reactors (ITER, tokamaks) aim for the Lawson criterion $n\tau_E > $ threshold for D-T plasma ignition. Stellar energy production (pp chain in the Sun) is fusion at astrophysical conditions.

**应用。** 核反应堆利用裂变（$k < 1$ 用于调控功率，$k = 1$ 用于稳定运行）。聚变反应堆（ITER、托卡马克）旨在满足 D-T 等离子体点火的劳森判据 $n\tau_E > $ 阈值。恒星能量产生（太阳中的 pp 链）是在天体物理条件下的聚变。

---

**Self-test (blank page)**

1. Define binding energy per nucleon; sketch its curve versus $A$ and explain why both fusion and fission can release energy.
2. Write all five terms of the Bethe–Weizsäcker formula and give the physical origin of each.
3. State the magic numbers; explain how the nuclear spin–orbit term generates the gap at $N = 28$.
4. Derive $N(t) = N_0\, e^{-\lambda t}$ from the memoryless decay assumption, and express $t_{1/2}$ in terms of $\lambda$.
5. Explain why alpha decay has an exponentially long half-life despite being energetically allowed; name the physical mechanism (Gamow tunneling) and state how the half-life depends on $Q_\alpha$.

**自测（空白页）**

1. 定义每核子结合能；画出其随 $A$ 变化的曲线，并解释为何聚变和裂变都能释放能量。
2. 写出贝特–魏茨泽克公式的全部五项，并给出每项的物理起源。
3. 陈述幻数；解释核自旋–轨道项如何在 $N = 28$ 处产生能隙。
4. 从无记忆衰变假设推导 $N(t) = N_0\, e^{-\lambda t}$，并用 $\lambda$ 表达 $t_{1/2}$。
5. 解释为何 $\alpha$ 衰变尽管在能量上允许却有指数级长的半衰期；说明物理机制（伽莫夫隧穿）并陈述半衰期如何依赖于 $Q_\alpha$。

---

← Previous: [Module 9.2 — Atomic & Molecular Physics](./module-9.2-atomic-and-molecular-physics.md) · [Phase 9 index](./README.md) · Next: [Module 9.4 — Plasma Physics](./module-9.4-plasma-physics.md) →

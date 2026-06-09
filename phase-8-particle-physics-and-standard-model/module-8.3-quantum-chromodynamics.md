---
title: "Module 8.3 — The Strong Interaction (QCD)"
parent: "Phase 8 — Particle Physics & the Standard Model"
nav_order: 3
---

# Module 8.3 — The Strong Interaction (QCD)
**模块 8.3 — 强相互作用（量子色动力学）**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.3-derivations.md)

---

## 1. Color Charge and the SU(3) Gauge Theory · 色荷与 SU(3) 规范理论

**Definition.** **Quantum Chromodynamics** is the $SU(3)$ Yang–Mills gauge theory describing the strong nuclear force. The fundamental matter fields are **quarks** — spin-$\tfrac12$ Dirac fermions in the fundamental (triplet) representation of $SU(3)$, carrying one of three **color charges**: red, green, blue. The eight gauge bosons are **gluons**, valued in the adjoint representation; they carry color themselves, unlike photons. The QCD Lagrangian is $\mathcal{L}_\text{QCD} = \sum_f \bar\psi_f(i\gamma^\mu D_\mu - m_f)\psi_f - \tfrac14 F_{\mu\nu}^a F^{a\mu\nu}$, summed over quark flavors $f = u, d, s, c, b, t$, with $D_\mu = \partial_\mu - ig_s A_\mu^a T^a$ ($T^a = \lambda^a/2$ are the eight Gell-Mann matrices). The strong coupling at low energies is $\alpha_s = g_s^2/(4\pi) \approx 0.1\text{–}1$.

**定义。** **量子色动力学**是描述强核力的 $SU(3)$ 杨–米尔斯规范理论。基本物质场是**夸克**——处于 $SU(3)$ 基本（三重态）表示中的自旋 $\tfrac12$ 狄拉克费米子，携带三种**色荷**之一：红、绿、蓝。八个规范玻色子是**胶子**，取值于伴随表示；与光子不同，它们自身携带色荷。量子色动力学拉格朗日量为 $\mathcal{L}_\text{QCD} = \sum_f \bar\psi_f(i\gamma^\mu D_\mu - m_f)\psi_f - \tfrac14 F_{\mu\nu}^a F^{a\mu\nu}$，对夸克味 $f = u, d, s, c, b, t$ 求和，其中 $D_\mu = \partial_\mu - ig_s A_\mu^a T^a$（$T^a = \lambda^a/2$ 为八个盖尔曼矩阵）。低能下强耦合常数 $\alpha_s = g_s^2/(4\pi) \approx 0.1\text{–}1$。

**Demonstration.** The $SU(3)$ structure constants $f^{abc}$ generate three-gluon and four-gluon vertices in the Lagrangian — gluons interact with each other. The one-loop $\beta$-function for QCD is $\beta(\alpha_s) = -(b_0/2\pi)\alpha_s^2$ with $b_0 = 11 - 2n_f/3$, positive for $n_f \leq 16$ active quark flavors. The negative sign means $\alpha_s$ **decreases** with increasing energy: **asymptotic freedom** (Gross, Politzer, Wilczek, 1973 Nobel Prize). The running: $\alpha_s(m_Z) \approx 0.118$, $\alpha_s(1\text{ GeV}) \approx 0.4$. At low energies $\alpha_s \sim 1$ and perturbation theory breaks down; quarks become strongly coupled and the theory is non-perturbative.

**演示。** $SU(3)$ 结构常数 $f^{abc}$ 在拉格朗日量中生成三胶子和四胶子顶角——胶子相互作用。量子色动力学的单圈 $\beta$ 函数为 $\beta(\alpha_s) = -(b_0/2\pi)\alpha_s^2$，其中 $b_0 = 11 - 2n_f/3$，对于 $n_f \leq 16$ 个活跃夸克味为正。负号意味着 $\alpha_s$ 随能量升高而**减小**：**渐近自由**（格罗斯、波利策、威尔切克，1973 年诺贝尔奖）。跑动关系：$\alpha_s(m_Z) \approx 0.118$，$\alpha_s(1\text{ GeV}) \approx 0.4$。在低能下 $\alpha_s \sim 1$，微扰论失效；夸克强耦合，理论呈非微扰性质。

**Application.** Asymptotic freedom explains why quarks inside a proton, probed at short distances (high energy), behave nearly as free particles — as seen in deep inelastic scattering experiments at SLAC in the 1960s–70s. At large distances, the coupling grows and quark-antiquark pairs are produced before a quark can escape, so only **color-singlet** hadrons are observed (confinement). The proton's mass (938 MeV) is $\sim 99\%$ from the QCD field energy of three confined quarks — the dominant source of visible mass in the universe, illustrating that $E = mc^2$ runs in reverse: fields generate mass.

**应用。** 渐近自由解释了为何质子内部的夸克在短距离（高能）探测下表现得几乎像自由粒子——正如 20 世纪 60–70 年代 SLAC 的深度非弹性散射实验所见。在大距离下，耦合增大，夸克逃逸之前便产生了夸克–反夸克对，因此只能观测到**色单态**强子（夸克禁闭）。质子的质量（938 MeV）约有 99% 来自三个被禁闭夸克的量子色动力学场能——宇宙中可见质量的主要来源，说明 $E = mc^2$ 可以"反向运行"：场产生质量。

---

## 2. Hadron Structure and Color Confinement · 强子结构与色禁闭

**Definition.** **Confinement** is the empirical fact that no free quark or gluon has ever been detected: the strong force does not diminish with distance (unlike $1/r^2$ for electromagnetism), so the energy stored in the color flux tube between separating quarks grows linearly: $V(r) \approx \sigma r$ for $r \gtrsim 1$ fm, with the **string tension** $\sigma \approx 0.9$ GeV/fm. When the stored energy exceeds the threshold for a quark–antiquark pair ($\sim 2m_\pi$), the string "breaks" and new hadrons are produced. **Hadrons** are color-singlet composites: **mesons** (quark–antiquark, $q\bar q$) and **baryons** (three quarks, $qqq$ with colors summing to a singlet via the antisymmetric $\varepsilon^{abc}$ tensor).

**定义。** **夸克禁闭**是一个经验事实：从未探测到自由夸克或自由胶子。强力不随距离减弱（不同于电磁力的 $1/r^2$），因此分离夸克之间色通量管中储存的能量线性增长：$V(r) \approx \sigma r$（$r \gtrsim 1$ fm），**弦张力** $\sigma \approx 0.9$ GeV/fm。当储存的能量超过夸克–反夸克对的阈值（$\sim 2m_\pi$）时，弦"断裂"并产生新的强子。**强子**是色单态复合体：**介子**（夸克–反夸克，$q\bar q$）和**重子**（三个夸克，$qqq$，通过反对称 $\varepsilon^{abc}$ 张量使色荷之和为单态）。

**Demonstration.** Color-singlet projection: a meson's color wavefunction is $(r\bar r + g\bar g + b\bar b)/\sqrt3$ — the unique $SU(3)$ singlet in $3 \otimes \bar 3$. A baryon's color wavefunction is $\varepsilon^{abc}|r_a g_b b_c\rangle$ — the singlet in $3 \otimes 3 \otimes 3$. Physical states must also satisfy Fermi statistics: the overall baryon wavefunction (color $\times$ spin $\times$ flavor $\times$ space) must be antisymmetric. Since $\varepsilon^{abc}$ is totally antisymmetric in color, the remaining spin-flavor-space part must be symmetric — this forces the lowest baryons to have spin-$\tfrac32$ (the $\Delta$ resonance) or specific flavor-spin correlations (the proton/neutron). Lattice QCD — QCD simulated on a discrete spacetime grid — directly confirms confinement and predicts the hadron mass spectrum to a few percent.

**演示。** 色单态投影：介子的色波函数为 $(r\bar r + g\bar g + b\bar b)/\sqrt3$——$3 \otimes \bar 3$ 中唯一的 $SU(3)$ 单态。重子的色波函数为 $\varepsilon^{abc}|r_a g_b b_c\rangle$——$3 \otimes 3 \otimes 3$ 中的单态。物理态还必须满足费米统计：重子的总波函数（色 $\times$ 自旋 $\times$ 味 $\times$ 空间）必须是反对称的。由于 $\varepsilon^{abc}$ 在色指标上完全反对称，其余的自旋–味–空间部分必须是对称的——这迫使最低重子具有自旋 $\tfrac32$（$\Delta$ 共振态）或特定的味–自旋关联（质子/中子）。格点量子色动力学——在离散时空格点上模拟的量子色动力学——直接证实了夸克禁闭，并以百分之几的精度预测了强子质量谱。

**Application.** The structure of protons and neutrons, and hence all nuclear physics, emerges from QCD. The **nuclear force** between hadrons (responsible for binding atomic nuclei) is a residual color force — the van der Waals analogue for color-neutral objects — mediated at long range by pion exchange. QCD also predicts **quark-gluon plasma** at temperatures $T \gtrsim 150$ MeV (attained in heavy-ion collisions at RHIC and the LHC), reconstructing the conditions of the universe microseconds after the Big Bang (Module 8.6).

**应用。** 质子和中子的结构，乃至所有核物理，均从量子色动力学中涌现。强子之间的**核力**（负责束缚原子核）是一种剩余色力——色中性物体之间的范德华力类比——在长程由 $\pi$ 介子交换传递。量子色动力学还预言在温度 $T \gtrsim 150$ MeV 下（在 RHIC 和大型强子对撞机的重离子碰撞中实现）存在**夸克–胶子等离子体**，再现了大爆炸后数微秒内宇宙的状态（模块 8.6）。

---

## Self-test (blank page)

1. State the QCD $\beta$-function and explain why its sign differs from QED. What are asymptotic freedom and confinement, and how are they related to the running of $\alpha_s$?
2. Explain why isolated quarks are never observed. Describe what happens when two quarks are pulled apart, and how color-singlet hadrons form.
3. Identify the color wavefunction of a meson and a baryon, and explain why the Fermi statistics constraint forces a specific relationship between spin, flavor, and color quantum numbers in the ground-state baryons.

**自测（空白页）**

1. 陈述量子色动力学的 $\beta$ 函数，并解释其符号为何与量子电动力学不同。渐近自由和夸克禁闭是什么，它们与 $\alpha_s$ 的跑动有何关系？
2. 解释为何从未观测到孤立的夸克。描述两个夸克被拉开时发生了什么，以及色单态强子如何形成。
3. 指出介子和重子的色波函数，并解释为何费米统计约束在基态重子中迫使自旋、味和色量子数之间存在特定关系。

---

← Previous: [Module 8.2 — Quantum Electrodynamics (QED)](./module-8.2-quantum-electrodynamics.md) · [Phase 8 index](./README.md) · Next: [Module 8.4 — Electroweak Theory & the Higgs](./module-8.4-electroweak-theory-and-higgs.md) →

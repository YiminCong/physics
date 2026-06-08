# Module 2.4 — Classical Statistical Mechanics
**模块 2.4 — 经典统计力学**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.4-derivations.md)

---

## 1. Microstates, Ensembles, and the Boltzmann Factor · 微观态、系综与玻尔兹曼因子

**Definition.** A **microstate** is a complete specification of a system (positions and momenta of all particles); a **macrostate** is a coarse description by a few thermodynamic variables (U, T, V, N). Statistical mechanics connects these levels via the **fundamental postulate**: in an isolated system at equilibrium, all accessible microstates are equally probable. The number of microstates consistent with a macrostate is Ω, and Boltzmann's entropy is

**定义。** **微观态**是对系统的完整描述（所有粒子的位置和动量）；**宏观态**是用少数热力学变量（U、T、V、N）进行的粗粒描述。统计力学通过**基本假设**将两个层次联系起来：在平衡态的孤立系统中，所有可及的微观态等概率出现。与某宏观态相符的微观态数目为 Ω，玻尔兹曼熵为

S = k_B ln Ω.

Three standard **ensembles** cover different physical situations:

三种标准**系综**覆盖不同的物理情形：

- **Microcanonical** (fixed E, V, N): isolated system; Ω counts states at energy E.
- **Canonical** (fixed T, V, N): system in thermal contact with a reservoir at temperature T. The probability of a microstate with energy E_i is the Boltzmann weight p_i = e^{−E_i/k_BT} / Z.
- **Grand canonical** (fixed T, V, μ): system can exchange both energy and particles with a reservoir; particle number N fluctuates. The probability of a state with energy E_i and particle number N_i is p_i ∝ e^{−(E_i − μ N_i)/k_BT}.

- **微正则系综**（固定 E、V、N）：孤立系统；Ω 统计能量为 E 时的状态数。
- **正则系综**（固定 T、V、N）：系统与温度为 T 的热库热接触。能量为 E_i 的微观态的概率为玻尔兹曼权重 p_i = e^{−E_i/k_BT} / Z。
- **巨正则系综**（固定 T、V、μ）：系统可与热库交换能量和粒子；粒子数 N 涨落。能量为 E_i、粒子数为 N_i 的态的概率为 p_i ∝ e^{−(E_i − μ N_i)/k_BT}。

**Demonstration.** In the canonical ensemble, the normalization condition Σ p_i = 1 defines the **partition function**

**演示。** 在正则系综中，归一化条件 Σ p_i = 1 定义了**配分函数**

Z = Σ_i e^{−E_i/k_BT},

where the sum runs over all microstates. All thermodynamic quantities follow from Z:

其中求和遍及所有微观态。所有热力学量均由 Z 导出：

- F = −k_B T ln Z     (Helmholtz free energy; the bridge formula)
- U = −∂(ln Z)/∂β,   β = 1/k_BT
- S = −(∂F/∂T)_V = k_B (ln Z + β U)
- P = −(∂F/∂V)_T

**Application.** The **equipartition theorem** follows immediately: for any degree of freedom whose energy is quadratic (½ k q²), the average energy is ½ k_B T. A monatomic ideal gas has 3 translational degrees of freedom, giving U = (3/2) N k_B T and C_V = (3/2) N k_B, matching experiment at high temperature. Failures of equipartition at low T (frozen-out vibrational modes, electronic heat capacity) are the first sign that quantum statistics is needed — taken up in Module 2.5.

**应用。** **能均分定理**随即得出：对于能量为二次型（½ k q²）的任意自由度，平均能量为 ½ k_B T。单原子理想气体有 3 个平动自由度，给出 U = (3/2) N k_B T 和 C_V = (3/2) N k_B，与高温实验吻合。低温时能均分定理的失效（振动模式冻结、电子热容）是需要量子统计的最初信号——在模块 2.5 中讨论。

---

## 2. The Partition Function as a Generating Function · 配分函数作为生成函数

**Definition.** For a system of N independent, distinguishable particles each with single-particle partition function z = Σ_α e^{−ε_α/k_BT}, the total partition function factorizes: Z = z^N. For **indistinguishable** classical particles, overcounting by N! must be corrected: Z = z^N / N!, which is the Gibbs correction. This prefactor is essential for the entropy to be extensive (the Gibbs paradox without it is that mixing identical gases appears to increase entropy).

**定义。** 对于 N 个独立可分辨粒子组成的系统，每个粒子的单粒子配分函数为 z = Σ_α e^{−ε_α/k_BT}，总配分函数可分解：Z = z^N。对于经典的**不可分辨**粒子，必须修正 N! 的重复计数：Z = z^N / N!，这是吉布斯修正。该前因子对于熵的广延性至关重要（若无此修正，吉布斯佯谬是：混合相同气体看似增加了熵）。

**Demonstration.** For the monatomic ideal gas in a box of volume V, the single-particle partition function is z = V (2π m k_B T / h²)^{3/2} (the thermal de Broglie volume). Using Z = z^N / N! and the Stirling approximation, the Sackur–Tetrode equation for entropy follows:

**演示。** 对于体积为 V 的箱中的单原子理想气体，单粒子配分函数为 z = V (2π m k_B T / h²)^{3/2}（热德布罗意体积）。利用 Z = z^N / N! 和斯特林近似，得到萨库尔–特特罗德熵方程：

S = N k_B [ ln(V/N) + (3/2) ln(k_B T) + const ],

which is correctly extensive and has a well-defined T → 0 limit connecting to the Third Law.

它具有正确的广延性，且在 T → 0 时有明确的极限，与第三定律相衔接。

**Application.** The partition function encodes everything: it gives the equation of state PV = N k_B T for the ideal gas, heat capacities, fluctuations (⟨E²⟩ − ⟨E⟩² = k_B T² C_V), and — through the grand canonical extension — chemical equilibrium constants. In quantum statistical mechanics (Module 2.5), the same logic applies but the sum over states respects Fermi–Dirac or Bose–Einstein statistics, fundamentally altering which microstates are accessible.

**应用。** 配分函数编码了一切：它给出理想气体的状态方程 PV = N k_B T、热容、涨落（⟨E²⟩ − ⟨E⟩² = k_B T² C_V），以及——通过巨正则推广——化学平衡常数。在量子统计力学（模块 2.5）中，同样的逻辑适用，但对态的求和须遵守费米–狄拉克或玻色–爱因斯坦统计，从根本上改变了哪些微观态可以被占据。

---

## Self-test (blank page) · 自测（空白页）

1. State the fundamental postulate of statistical mechanics. How does it lead to S = k_B ln Ω?
2. Derive the average energy U = −∂(ln Z)/∂β from the definition Z = Σ e^{−β E_i} and the expression ⟨E⟩ = Σ p_i E_i.
3. Apply the equipartition theorem to a diatomic gas with 3 translational + 2 rotational + 2 vibrational (kinetic + potential) degrees of freedom. What is C_V per molecule?
4. Why must Z be divided by N! for identical classical particles? What paradox does this resolve?

**自测（空白页）**

1. 陈述统计力学的基本假设。它如何导出 S = k_B ln Ω？
2. 由定义 Z = Σ e^{−β E_i} 和表达式 ⟨E⟩ = Σ p_i E_i，推导平均能量 U = −∂(ln Z)/∂β。
3. 对具有 3 个平动 + 2 个转动 + 2 个振动（动能 + 势能）自由度的双原子气体应用能均分定理。每个分子的 C_V 是多少？
4. 为什么对于经典全同粒子，Z 必须除以 N!？这解决了什么佯谬？

---

← Previous: [Module 2.3 — Free Energy & Phase Transitions](./module-2.3-free-energy-phase-transitions.md) · [Phase 2 index](./README.md) · Next: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) →

# Module 2.4 — Classical Statistical Mechanics
**模块 2.4 — 经典统计力学**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.4-derivations.md)

---

## 1. Microstates, Ensembles, and the Boltzmann Factor · 微观态、系综与玻尔兹曼因子

**Definition.** A **microstate** is a complete specification of a system (positions and momenta of all particles); a **macrostate** is a coarse description by a few thermodynamic variables ($U$, $T$, $V$, $N$). Statistical mechanics connects these levels via the **fundamental postulate**: in an isolated system at equilibrium, all accessible microstates are equally probable. The number of microstates consistent with a macrostate is $\Omega$, and Boltzmann's entropy is

**定义。** **微观态**是对系统的完整描述（所有粒子的位置和动量）；**宏观态**是用少数热力学变量（$U$、$T$、$V$、$N$）进行的粗粒描述。统计力学通过**基本假设**将两个层次联系起来：在平衡态的孤立系统中，所有可及的微观态等概率出现。与某宏观态相符的微观态数目为 $\Omega$，玻尔兹曼熵为

$$ S = k_B \ln \Omega. $$

Three standard **ensembles** cover different physical situations:

三种标准**系综**覆盖不同的物理情形：

- **Microcanonical** (fixed $E$, $V$, $N$): isolated system; $\Omega$ counts states at energy $E$.
- **Canonical** (fixed $T$, $V$, $N$): system in thermal contact with a reservoir at temperature $T$. The probability of a microstate with energy $E_i$ is the Boltzmann weight $p_i = e^{-E_i/k_B T} / Z$.
- **Grand canonical** (fixed $T$, $V$, $\mu$): system can exchange both energy and particles with a reservoir; particle number $N$ fluctuates. The probability of a state with energy $E_i$ and particle number $N_i$ is $p_i \propto e^{-(E_i - \mu N_i)/k_B T}$.

- **微正则系综**（固定 $E$、$V$、$N$）：孤立系统；$\Omega$ 统计能量为 $E$ 时的状态数。
- **正则系综**（固定 $T$、$V$、$N$）：系统与温度为 $T$ 的热库热接触。能量为 $E_i$ 的微观态的概率为玻尔兹曼权重 $p_i = e^{-E_i/k_B T} / Z$。
- **巨正则系综**（固定 $T$、$V$、$\mu$）：系统可与热库交换能量和粒子；粒子数 $N$ 涨落。能量为 $E_i$、粒子数为 $N_i$ 的态的概率为 $p_i \propto e^{-(E_i - \mu N_i)/k_B T}$。

**Demonstration.** In the canonical ensemble, the normalization condition $\sum_i p_i = 1$ defines the **partition function**

**演示。** 在正则系综中，归一化条件 $\sum_i p_i = 1$ 定义了**配分函数**

$$ Z = \sum_i e^{-E_i/k_B T}, $$

where the sum runs over all microstates. All thermodynamic quantities follow from $Z$:

其中求和遍及所有微观态。所有热力学量均由 $Z$ 导出：

- $F = -k_B T \ln Z$     (Helmholtz free energy; the bridge formula)
- $U = -\partial(\ln Z)/\partial\beta$,   $\beta = 1/k_B T$
- $S = -\left(\frac{\partial F}{\partial T}\right)_V = k_B (\ln Z + \beta U)$
- $P = -\left(\frac{\partial F}{\partial V}\right)_T$

**Application.** The **equipartition theorem** follows immediately: for any degree of freedom whose energy is quadratic ($\tfrac12 k q^2$), the average energy is $\tfrac12 k_B T$. A monatomic ideal gas has 3 translational degrees of freedom, giving $U = \tfrac32 N k_B T$ and $C_V = \tfrac32 N k_B$, matching experiment at high temperature. Failures of equipartition at low $T$ (frozen-out vibrational modes, electronic heat capacity) are the first sign that quantum statistics is needed — taken up in Module 2.5.

**应用。** **能均分定理**随即得出：对于能量为二次型（$\tfrac12 k q^2$）的任意自由度，平均能量为 $\tfrac12 k_B T$。单原子理想气体有 3 个平动自由度，给出 $U = \tfrac32 N k_B T$ 和 $C_V = \tfrac32 N k_B$，与高温实验吻合。低温时能均分定理的失效（振动模式冻结、电子热容）是需要量子统计的最初信号——在模块 2.5 中讨论。

---

## 2. The Partition Function as a Generating Function · 配分函数作为生成函数

**Definition.** For a system of $N$ independent, distinguishable particles each with single-particle partition function $z = \sum_\alpha e^{-\varepsilon_\alpha/k_B T}$, the total partition function factorizes: $Z = z^N$. For **indistinguishable** classical particles, overcounting by $N!$ must be corrected: $Z = z^N / N!$, which is the Gibbs correction. This prefactor is essential for the entropy to be extensive (the Gibbs paradox without it is that mixing identical gases appears to increase entropy).

**定义。** 对于 $N$ 个独立可分辨粒子组成的系统，每个粒子的单粒子配分函数为 $z = \sum_\alpha e^{-\varepsilon_\alpha/k_B T}$，总配分函数可分解：$Z = z^N$。对于经典的**不可分辨**粒子，必须修正 $N!$ 的重复计数：$Z = z^N / N!$，这是吉布斯修正。该前因子对于熵的广延性至关重要（若无此修正，吉布斯佯谬是：混合相同气体看似增加了熵）。

**Demonstration.** For the monatomic ideal gas in a box of volume $V$, the single-particle partition function is $z = V (2\pi m k_B T / h^2)^{3/2}$ (the thermal de Broglie volume). Using $Z = z^N / N!$ and the Stirling approximation, the Sackur–Tetrode equation for entropy follows:

**演示。** 对于体积为 $V$ 的箱中的单原子理想气体，单粒子配分函数为 $z = V (2\pi m k_B T / h^2)^{3/2}$（热德布罗意体积）。利用 $Z = z^N / N!$ 和斯特林近似，得到萨库尔–特特罗德熵方程：

$$ S = N k_B \left[ \ln(V/N) + \tfrac32 \ln(k_B T) + \text{const} \right], $$

which is correctly extensive and has a well-defined $T \to 0$ limit connecting to the Third Law.

它具有正确的广延性，且在 $T \to 0$ 时有明确的极限，与第三定律相衔接。

**Application.** The partition function encodes everything: it gives the equation of state $PV = N k_B T$ for the ideal gas, heat capacities, fluctuations ($\langle E^2\rangle - \langle E\rangle^2 = k_B T^2 C_V$), and — through the grand canonical extension — chemical equilibrium constants. In quantum statistical mechanics (Module 2.5), the same logic applies but the sum over states respects Fermi–Dirac or Bose–Einstein statistics, fundamentally altering which microstates are accessible.

**应用。** 配分函数编码了一切：它给出理想气体的状态方程 $PV = N k_B T$、热容、涨落（$\langle E^2\rangle - \langle E\rangle^2 = k_B T^2 C_V$），以及——通过巨正则推广——化学平衡常数。在量子统计力学（模块 2.5）中，同样的逻辑适用，但对态的求和须遵守费米–狄拉克或玻色–爱因斯坦统计，从根本上改变了哪些微观态可以被占据。

## Key results · 核心结果

- $S=k_B\ln\Omega$ (Boltzmann) · 玻尔兹曼熵
- Partition function $Z=\sum_i e^{-E_i/k_BT}$; Boltzmann factor $e^{-E_i/k_BT}$ · 配分函数
- $U=-\partial\ln Z/\partial\beta$, $F=-k_BT\ln Z$ · 由 $Z$ 得热力学量
- Gibbs $1/N!$ for indistinguishability (Sackur–Tetrode entropy) · 吉布斯 $1/N!$

---

## Self-test (blank page) · 自测（空白页）

1. State the fundamental postulate of statistical mechanics. How does it lead to $S = k_B \ln \Omega$?
2. Derive the average energy $U = -\partial(\ln Z)/\partial\beta$ from the definition $Z = \sum e^{-\beta E_i}$ and the expression $\langle E\rangle = \sum p_i E_i$.
3. Apply the equipartition theorem to a diatomic gas with 3 translational + 2 rotational + 2 vibrational (kinetic + potential) degrees of freedom. What is $C_V$ per molecule?
4. Why must $Z$ be divided by $N!$ for identical classical particles? What paradox does this resolve?

**自测（空白页）**

1. 陈述统计力学的基本假设。它如何导出 $S = k_B \ln \Omega$？
2. 由定义 $Z = \sum e^{-\beta E_i}$ 和表达式 $\langle E\rangle = \sum p_i E_i$，推导平均能量 $U = -\partial(\ln Z)/\partial\beta$。
3. 对具有 3 个平动 + 2 个转动 + 2 个振动（动能 + 势能）自由度的双原子气体应用能均分定理。每个分子的 $C_V$ 是多少？
4. 为什么对于经典全同粒子，$Z$ 必须除以 $N!$？这解决了什么佯谬？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Postulate: all accessible microstates of an isolated system are equally probable; the entropy is the log of their number, $S=k_B\ln\Omega$. · 等概率假设给 $S=k_B\ln\Omega$。
**2.** With $p_i=e^{-\beta E_i}/Z$, $U=\sum p_i E_i=\tfrac1Z\sum E_i e^{-\beta E_i}=-\tfrac1Z\partial_\beta Z=-\partial_\beta\ln Z$. · $U=-\partial_\beta\ln Z$。
**3.** Equipartition gives $\tfrac12 k_B$ per quadratic degree of freedom; $3+2+2=7$ → $C_V=\tfrac72 k_B$ per molecule (high $T$). · 能量均分 $C_V=\tfrac72 k_B$。
**4.** The $1/N!$ corrects overcounting of permutations of identical particles, resolving the Gibbs paradox (spurious mixing entropy). · $1/N!$ 解决吉布斯佯谬。

</details>

---

← Previous: [Module 2.3 — Free Energy & Phase Transitions](./module-2.3-free-energy-phase-transitions.md) · [Phase 2 index](./README.md) · Next: [Module 2.5 — Quantum Statistics](./module-2.5-quantum-statistics.md) →

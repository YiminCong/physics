---
title: "Module 2.5 — Quantum Statistics"
parent: "Phase 2 — Thermodynamics & Statistical Mechanics"
nav_order: 5
---

# Module 2.5 — Quantum Statistics ⭐
**模块 2.5 — 量子统计 ⭐**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.5-derivations.md)

---

## 1. Indistinguishability and the Two Distributions · 不可分辨性与两种分布

**Definition.** Quantum mechanics forces a radical revision of how microstates are counted. Identical particles are truly indistinguishable: swapping two particles cannot produce a new state (Module 3.5). The symmetry of the many-body wavefunction under particle exchange splits all particles into two classes:

**定义。** 量子力学迫使我们从根本上修正微观态的计数方式。全同粒子是真正不可分辨的：交换两个粒子不能产生新状态（模块 3.5）。多体波函数在粒子交换下的对称性将所有粒子分为两类：

- **Fermions** (half-integer spin): wavefunction is antisymmetric. No two fermions can occupy the same single-particle state — the **Pauli exclusion principle**. The mean occupation number of a state with energy $\varepsilon$ is the **Fermi–Dirac distribution**:

  $$ n_\text{FD}(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/k_B T} + 1} $$

- **Bosons** (integer spin): wavefunction is symmetric. Any number of bosons can occupy the same state. The mean occupation number is the **Bose–Einstein distribution**:

  $$ n_\text{BE}(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/k_B T} - 1} $$

- **费米子**（半整数自旋）：波函数反对称。没有两个费米子可以占据同一单粒子态——**泡利不相容原理**。能量为 $\varepsilon$ 的态的平均占据数为**费米–狄拉克分布**：

  $$ n_\text{FD}(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/k_B T} + 1} $$

- **玻色子**（整数自旋）：波函数对称。任意数目的玻色子可以占据同一态。平均占据数为**玻色–爱因斯坦分布**：

  $$ n_\text{BE}(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/k_B T} - 1} $$

In both cases, $\mu$ is the **chemical potential**, determined by the condition that $\sum n(\varepsilon) = N$ (total particle number). At high temperature or low density ($e^{(\varepsilon - \mu)/k_B T} \gg 1$ for all occupied states), both distributions reduce to the classical Maxwell–Boltzmann result $n \propto e^{-\varepsilon/k_B T}$.

两种情况下，$\mu$ 均为**化学势**，由条件 $\sum n(\varepsilon) = N$（总粒子数）确定。在高温或低密度下（对所有占据态有 $e^{(\varepsilon - \mu)/k_B T} \gg 1$），两种分布均退化为经典麦克斯韦–玻尔兹曼结果 $n \propto e^{-\varepsilon/k_B T}$。

**Demonstration.** These distributions are derived in the grand canonical ensemble (Module 2.4). For fermions, each single-particle state $\alpha$ is an independent sub-system that can hold 0 or 1 particle; its grand canonical partition function is

**演示。** 这些分布在巨正则系综（模块 2.4）中推导。对于费米子，每个单粒子态 $\alpha$ 是一个可容纳 0 或 1 个粒子的独立子系统；其巨正则配分函数为

$$ z_\alpha = 1 + e^{-(\varepsilon_\alpha - \mu)/k_B T}, $$

and the mean occupation is $\langle n_\alpha\rangle = -\partial(k_B T \ln z_\alpha)/\partial\varepsilon_\alpha = n_\text{FD}(\varepsilon_\alpha)$. For bosons the state can hold $0, 1, 2, \dots$ particles; the geometric series gives $z_\alpha = 1/(1 - e^{-(\varepsilon_\alpha - \mu)/k_B T})$ and $\langle n_\alpha\rangle = n_\text{BE}(\varepsilon_\alpha)$. The denominator sign difference — plus for fermions, minus for bosons — encodes the entire distinction between the two statistics.

平均占据数为 $\langle n_\alpha\rangle = -\partial(k_B T \ln z_\alpha)/\partial\varepsilon_\alpha = n_\text{FD}(\varepsilon_\alpha)$。对于玻色子，该态可容纳 $0, 1, 2, \dots$ 个粒子；等比级数给出 $z_\alpha = 1/(1 - e^{-(\varepsilon_\alpha - \mu)/k_B T})$，$\langle n_\alpha\rangle = n_\text{BE}(\varepsilon_\alpha)$。分母符号之差——费米子为加，玻色子为减——编码了两种统计之间的全部区别。

**Application.** The Fermi–Dirac distribution at $T = 0$ is a step function: all states up to the **Fermi energy** $E_F$ are fully occupied, all above are empty. $E_F$ is set by filling $N$ states in order of increasing energy:

**应用。** $T = 0$ 时的费米–狄拉克分布是一个阶跃函数：所有低于**费米能** $E_F$ 的态完全被占据，所有高于 $E_F$ 的态为空。$E_F$ 由按能量从低到高填充 $N$ 个态确定：

$$ E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3} \qquad \text{(free electron gas in 3D, } n = N/V\text{)}. $$

This defines the Fermi surface in momentum space — the central object of electronic structure, conductivity, and superconductivity (Phases 4–5). For bosons, $\mu$ must remain below the ground-state energy; when $\mu \to 0$ as $T$ is lowered, macroscopic occupation of the ground state (Bose–Einstein condensation) occurs — see Module 2.6.

这定义了动量空间中的费米面——电子结构、电导率和超导性（第 4–5 阶段）的核心对象。对于玻色子，$\mu$ 必须保持低于基态能量；当温度降低使 $\mu \to 0$ 时，基态的宏观占据（玻色–爱因斯坦凝聚）发生——见模块 2.6。

---

## 2. Chemical Potential and the Pauli Principle in Practice · 化学势与泡利原理的实际应用

**Definition.** The chemical potential $\mu$ is the free-energy cost of adding one particle at fixed $T$ and $V$: $\mu = \left(\frac{\partial F}{\partial N}\right)_{T,V}$. At $T = 0$ for fermions, $\mu = E_F$ exactly. At finite $T$, $\mu$ shifts slightly below $E_F$ (for a metal, the shift is of order $(k_B T)^2/E_F$ — tiny at room temperature since $k_B T \approx 0.025$ eV while $E_F \approx 5$–$10$ eV). For bosons in three dimensions, $\mu < \varepsilon_0$ (ground-state energy) at all $T$ above the condensation temperature $T_\text{BEC}$.

**定义。** 化学势 $\mu$ 是在固定 $T$ 和 $V$ 下添加一个粒子的自由能代价：$\mu = \left(\frac{\partial F}{\partial N}\right)_{T,V}$。对于费米子，$T = 0$ 时 $\mu = E_F$。在有限温度下，$\mu$ 略微低于 $E_F$（对于金属，偏移量约为 $(k_B T)^2/E_F$——在室温下很小，因为 $k_B T \approx 0.025$ eV 而 $E_F \approx 5$–$10$ eV）。对于三维玻色子，在所有高于凝聚温度 $T_\text{BEC}$ 的温度下均有 $\mu < \varepsilon_0$（基态能量）。

**Demonstration.** The Sommerfeld expansion expresses any Fermi–Dirac integral as a low-temperature series. For the average energy of a 3D free Fermi gas:

**演示。** 索末菲展开将任意费米–狄拉克积分表示为低温级数。对于三维自由费米气体的平均能量：

$$ U(T) \approx U(0) + \frac{\pi^2}{6}(k_B T)^2 g(E_F) + \dots $$

where $g(E_F)$ is the density of states at the Fermi level. Differentiating gives the electronic heat capacity

其中 $g(E_F)$ 是费米能级处的态密度。求导得到电子热容

$$ C_\text{el} = \frac{\pi^2}{3} k_B^2 T\, g(E_F) \propto T, $$

which is far smaller than the classical equipartition value $\tfrac32 N k_B$ because only the fraction $\sim k_B T/E_F$ of electrons near the Fermi surface are thermally active. This $T$-linear heat capacity is a direct signature of Fermi statistics, measured in metals and discussed further in Module 4.1.

它远小于经典能均分值 $\tfrac32 N k_B$，因为只有费米面附近约 $\sim k_B T/E_F$ 比例的电子是热活跃的。这个与 $T$ 成正比的热容是费米统计的直接特征，在金属中可测量，并在模块 4.1 中进一步讨论。

**Application.** Quantum statistics permeates condensed matter and beyond:

**应用。** 量子统计渗透凝聚态物理及更广泛的领域：

- **Electron gas** in metals: Fermi–Dirac statistics explains the small electronic heat capacity, electrical conductivity, and the existence of a Fermi surface (Module 4.5).
- **Phonons and photons**: both are bosons (integer spin). Their chemical potential is zero (they are not conserved), so $n_\text{BE}(\varepsilon) = 1/(e^{\varepsilon/k_B T} - 1)$ directly gives the Planck distribution for photons and the Bose occupation of phonon modes — governing black-body radiation and lattice heat capacity (Module 2.6, Module 4.3).
- **Superconductivity**: Cooper pairs are composite bosons; their condensation is enabled by Fermi-surface instabilities described by BCS theory (Phase 5).

- 金属中的**电子气**：费米–狄拉克统计解释了小的电子热容、电导率以及费米面的存在（模块 4.5）。
- **声子和光子**：两者均为玻色子（整数自旋）。它们的化学势为零（不守恒），故 $n_\text{BE}(\varepsilon) = 1/(e^{\varepsilon/k_B T} - 1)$ 直接给出光子的普朗克分布和声子模式的玻色占据——支配黑体辐射和晶格热容（模块 2.6、模块 4.3）。
- **超导性**：库珀对是复合玻色子；它们的凝聚由 BCS 理论描述的费米面不稳定性所驱动（第 5 阶段）。

---

## Self-test (blank page) · 自测（空白页）

1. Write down both quantum distribution functions and state which applies to electrons, photons, and helium-4 atoms. What is the classical limit?
2. Explain in one sentence why the electronic heat capacity $C_\text{el} \propto T$ rather than the classical value $\tfrac32 N k_B$. Which electrons contribute?
3. For a free Fermi gas at $T = 0$, derive the Fermi energy $E_F$ in terms of the number density $n$, using the condition that all states below $E_F$ are filled.
4. Why must the chemical potential for bosons satisfy $\mu < \varepsilon_0$ (the ground-state energy)? What happens when $\mu \to \varepsilon_0$?

**自测（空白页）**

1. 写出两种量子分布函数，并说明哪种适用于电子、光子和氦-4 原子。经典极限是什么？
2. 用一句话解释为什么电子热容 $C_\text{el} \propto T$ 而非经典值 $\tfrac32 N k_B$。哪些电子有贡献？
3. 对于 $T = 0$ 的自由费米气体，利用所有低于 $E_F$ 的态均被填满的条件，推导用数密度 $n$ 表示的费米能 $E_F$。
4. 为什么玻色子的化学势必须满足 $\mu < \varepsilon_0$（基态能量）？当 $\mu \to \varepsilon_0$ 时会发生什么？

---

← Previous: [Module 2.4 — Classical Statistical Mechanics](./module-2.4-classical-statistical-mechanics.md) · [Phase 2 index](./README.md) · Next: [Module 2.6 — Quantum Gases & Applications](./module-2.6-quantum-gases-applications.md) →

# Module 4.1 — Electrons and Heat in Solids
**模块 4.1 — 固体中的电子与热**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.1-derivations.md)

---

## 1. From Drude to Sommerfeld · 从德鲁德到索末菲

**Definition.** The **Drude model** treats conduction electrons as a classical gas — it gets Ohm's law right but predicts a far-too-large electronic heat capacity. The **Sommerfeld model** fixes this by treating electrons as a quantum **free Fermi gas** obeying Fermi–Dirac statistics (Module 2.5).

**定义。** **德鲁德模型**将传导电子视为经典气体——它能正确给出欧姆定律，但预言的电子热容过大。**索末菲模型**通过将电子视为服从费米–狄拉克统计（模块 2.5）的量子**自由费米气体**来修正这一问题。

**Demonstration.** Because only electrons within $\sim k T$ of the Fermi energy can be thermally excited, the electronic heat capacity is $C_{\mathrm{el}} = \gamma T \propto T$ (linear, and small), with $\gamma$ proportional to the density of states at the Fermi level.

**演示。** 由于只有费米能附近约 $\sim k T$ 范围内的电子可以被热激发，电子热容为 $C_{\mathrm{el}} = \gamma T \propto T$（线性且数值小），其中 $\gamma$ 正比于费米能级处的态密度。

## 2. Lattice Heat Capacity · 晶格热容

**Definition.** The **Einstein** and **Debye** models quantize lattice vibrations. Debye correctly gives $C_{\mathrm{lattice}} \propto T^3$ at low temperature.

**定义。** **爱因斯坦**和**德拜**模型对晶格振动进行量子化处理。德拜模型正确给出低温下 $C_{\mathrm{lattice}} \propto T^3$ 的结果。

**Application.** Total low-T heat capacity $C = \gamma T + \beta T^3$: the linear term probes electrons, the cubic term probes phonons. Measuring $\gamma$ gives the density of states at $E_F$ — and the **jump in heat capacity at $T_c$** is one of the classic fingerprints of the superconducting transition (Phase 5).

**应用。** 低温总热容 $C = \gamma T + \beta T^3$：线性项探测电子，三次方项探测声子。测量 $\gamma$ 可以得到 $E_F$ 处的态密度——而 **$T_c$ 处热容的跳跃**是超导转变的经典特征之一（第 5 阶段）。

## Key results · 核心结果

- Sommerfeld electronic heat capacity $C_\text{el}=\gamma T$, with $\gamma\propto g(E_F)$ · 索末菲电子热容
- Low-$T$ total $C=\gamma T+\beta T^3$ (electrons + Debye phonons) · 低温总热容
- Fermi statistics suppress $C_\text{el}$ by $\sim T/T_F$ vs the classical value · 费米统计压低电子热容
- $\Delta C/\gamma T_c\approx1.43$ jump at the superconducting $T_c$ · 超导转变处的比热跳变

---

**Self-test (blank page)**

1. State the Sommerfeld result for the electronic heat capacity. Why is it linear in $T$, and what does the coefficient $\gamma$ measure?
2. Write down the low-temperature total heat capacity $C = \gamma T + \beta T^3$. Explain the physical origin of each term and how you would extract $\gamma$ and $\beta$ from a measurement.
3. The Drude model and the Sommerfeld model both give Ohm's law, but differ sharply on heat capacity. What physical ingredient does Sommerfeld add, and why does it reduce the electronic heat capacity by a factor of order $T/T_F$?
4. The jump in heat capacity at the superconducting transition temperature $T_c$ is a key experimental signature. What does its magnitude, relative to $\gamma T_c$, tell you about the nature of the transition?

**自测（空白页）**

1. 写出索末菲模型给出的电子热容表达式，解释为何它正比于 $T$，以及系数 $\gamma$ 测量什么物理量。
2. 写出低温总热容 $C = \gamma T + \beta T^3$，分别解释两项的物理来源，并说明如何从实验数据中提取 $\gamma$ 和 $\beta$。
3. 德鲁德模型与索末菲模型都能给出欧姆定律，但在热容上差别很大。索末菲模型加入了什么关键物理成分？为何它使电子热容减小了量级为 $T/T_F$ 的因子？
4. 在超导转变温度 $T_c$ 处热容发生跳跃是重要的实验特征。其大小（相对于 $\gamma T_c$）能告诉我们关于转变本质的什么信息？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $C_\text{el}=\gamma T=\tfrac{\pi^2}{3}k_B^2 g(E_F)T$: linear because only the fraction $\sim k_BT/E_F$ of electrons near $E_F$ are thermally active (Pauli); $\gamma$ measures $g(E_F)$. · 线性正比 $T$,$\gamma$ 测 $g(E_F)$。
**2.** $C=\gamma T+\beta T^3$: $\gamma T$ electronic, $\beta T^3$ Debye phonons. Plot $C/T$ vs $T^2$ — intercept $\gamma$, slope $\beta$. · 画 $C/T$–$T^2$ 提取 $\gamma,\beta$。
**3.** Sommerfeld adds Fermi–Dirac statistics; only $\sim T/T_F$ of electrons near $E_F$ contribute, reducing $C_\text{el}$ by that factor vs the classical $\tfrac32 Nk_B$. · 费米统计,压低因子 $\sim T/T_F$。
**4.** $\Delta C/\gamma T_c\approx1.43$ (universal BCS), signalling a second-order transition into a gapped paired state. · 跳变 1.43,二阶相变。

</details>

---

← *Phase 4 index: [Condensed Matter](./README.md)* · Next: [Module 4.2 — Crystal Structure & Reciprocal Space](./module-4.2-crystal-structure-and-reciprocal-space.md) →

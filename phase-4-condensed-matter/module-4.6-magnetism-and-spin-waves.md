# Module 4.6 — Magnetism & Spin Waves
**模块 4.6 — 磁性与自旋波**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.6-derivations.md)

---

## 1. Origin of Magnetism & the Exchange Interaction · 磁性的起源与交换相互作用

**Definition.** Magnetism in solids arises from electronic spin and orbital angular momentum. In an external field **B**, a material develops a magnetization **M** = χ**H** where χ is the magnetic susceptibility. **Diamagnets** (χ < 0) weakly repel fields; **paramagnets** (χ > 0) weakly attract them. Paramagnetism from localized magnetic moments obeys the **Curie law**:

  χ = C/T,   C = n μ₀ μ_eff²/k_B

where n is the moment density and μ_eff is the effective magnetic moment per site.

**定义。** 固体中的磁性来源于电子自旋和轨道角动量。在外场 **B** 中，材料产生磁化强度 **M** = χ**H**，其中 χ 为磁化率。**抗磁体**（χ < 0）微弱排斥磁场；**顺磁体**（χ > 0）微弱吸引磁场。局域磁矩的顺磁性服从**居里定律**：

  χ = C/T，C = n μ₀ μ_eff²/k_B

其中 n 为磁矩密度，μ_eff 为每个格点的有效磁矩。

**Demonstration.** The Curie law follows directly from the two-level partition function for a spin-½ moment in a field (see Derivations A). For S = ½ in field B, the partition function Z = 2 cosh(μ_B B/k_B T) gives M = n μ_B tanh(μ_B B/k_B T). In the high-temperature (weak-field) limit μ_B B ≪ k_B T, tanh(x) ≈ x and χ ∝ 1/T.

**演示。** 居里定律直接来源于自旋-½ 磁矩在磁场中的两态配分函数（见推导 A）。对于 S = ½ 在磁场 B 中，配分函数 Z = 2 cosh(μ_B B/k_B T) 给出 M = n μ_B tanh(μ_B B/k_B T)。在高温（弱场）极限 μ_B B ≪ k_B T 下，tanh(x) ≈ x，从而 χ ∝ 1/T。

**Definition.** The **exchange interaction** is a quantum-mechanical effect combining the Coulomb repulsion of electrons with the Pauli exclusion principle: two electrons in overlapping orbitals must antisymmetrize their spatial wavefunction, which effectively couples their spins. This gives the **Heisenberg model**:

  H = −J Σ_{⟨i,j⟩} **S**_i · **S**_j

where J is the exchange constant and the sum is over nearest-neighbor pairs. J > 0 favors parallel spins → **ferromagnetism**; J < 0 favors antiparallel spins → **antiferromagnetism**. The simpler **Ising model** replaces the dot product with Sᵢᶻ Sⱼᶻ (scalar spins).

**定义。** **交换相互作用**是将电子间库仑排斥与泡利不相容原理相结合的量子力学效应：两个处于重叠轨道的电子必须将其空间波函数反对称化，这有效地耦合了它们的自旋。由此给出**海森堡模型**：

  H = −J Σ_{⟨i,j⟩} **S**_i · **S**_j

其中 J 为交换常数，求和遍历最近邻对。J > 0 有利于自旋平行 → **铁磁性**；J < 0 有利于自旋反平行 → **反铁磁性**。更简单的**伊辛模型**将点积替换为 Sᵢᶻ Sⱼᶻ（标量自旋）。

**Application — Mean-field theory & the Curie–Weiss law.** Replace the interactions on site i by an effective molecular field proportional to the mean magnetization m = ⟨Sᶻ⟩. Self-consistency gives a critical temperature

  T_c = z J S(S+1) / (3 k_B)

(where z is the coordination number) and the **Curie–Weiss law** above T_c:

  χ = C / (T − T_c).

Below T_c a spontaneous magnetization m(T) > 0 appears, vanishing near T_c as m ∝ (T_c − T)^{1/2} (mean-field critical exponent β = 1/2). See Derivations B for the full mean-field calculation.

**应用——平均场理论与居里–外斯定律。** 将格点 i 上的相互作用替换为正比于平均磁化强度 m = ⟨Sᶻ⟩ 的有效分子场。自洽条件给出临界温度

  T_c = z J S(S+1) / (3 k_B)

（z 为配位数），以及 T_c 以上的**居里–外斯定律**：

  χ = C / (T − T_c)。

T_c 以下出现自发磁化 m(T) > 0，在 T_c 附近趋向零时 m ∝ (T_c − T)^{1/2}（平均场临界指数 β = 1/2）。完整平均场计算见推导 B。

---

## 2. Spin Waves & Magnons · 自旋波与磁振子

**Definition.** In an ordered magnet, the ground state has all spins aligned. A **spin wave** is a collective, wavelike deviation of the spins from their ordered direction. Upon quantization, each spin-wave mode carries a quantum of energy: the **magnon**, the magnetic analogue of the phonon. The magnon is the elementary excitation of an ordered magnetic phase.

**定义。** 在有序磁体中，基态所有自旋都沿同一方向排列。**自旋波**是自旋偏离其有序方向的集体波动式偏转。量子化后，每个自旋波模式携带一个能量量子：**磁振子**，即声子在磁学中的类比。磁振子是有序磁相的元激发。

**Demonstration — Ferromagnetic dispersion.** Starting from the Heisenberg Hamiltonian and using the Holstein–Primakoff transformation (see Derivations C), the magnon dispersion for a simple cubic ferromagnet is

  ℏω_k = 4 J S (3 − cos k_x a − cos k_y a − cos k_z a).

For long wavelengths (ka ≪ 1) this reduces to

  ℏω_k ≈ 2 J S a² k²   →   ω ∝ k².

This **quadratic dispersion** (contrasting with the linear acoustic-phonon dispersion ω ∝ k) is a hallmark of ferromagnetic magnons.

**演示——铁磁色散。** 从海森堡哈密顿量出发，利用霍尔斯坦–普里马科夫变换（见推导 C），简单立方铁磁体的磁振子色散为

  ℏω_k = 4 J S (3 − cos k_x a − cos k_y a − cos k_z a)。

在长波极限（ka ≪ 1）下，化简为

  ℏω_k ≈ 2 J S a² k²   →   ω ∝ k²。

这种**二次型色散**（与线性声学声子色散 ω ∝ k 形成对比）是铁磁磁振子的标志。

**Application — The Bloch T^{3/2} law.** The magnon occupation follows the Bose–Einstein distribution. At low T, integrating over the magnon density of states (which scales as ω^{1/2} dω for a ω ∝ k² dispersion in 3D) gives the thermally excited magnon density ∝ T^{3/2}. Each excited magnon flips one spin, reducing the magnetization:

  M(T) = M(0) [ 1 − A T^{3/2} + … ]   (Bloch law)

where A is a material-dependent constant. See Derivations D for the full calculation.

**应用——布洛赫 T^{3/2} 定律。** 磁振子占据数服从玻色–爱因斯坦分布。在低温下，对磁振子态密度积分（对三维空间 ω ∝ k² 色散，态密度 ∝ ω^{1/2} dω）给出热激发磁振子密度 ∝ T^{3/2}。每个激发磁振子翻转一个自旋，从而降低磁化强度：

  M(T) = M(0) [ 1 − A T^{3/2} + … ]   （布洛赫定律）

其中 A 为与材料有关的常数。完整计算见推导 D。

**Definition — Antiferromagnetism & Néel order.** When J < 0 the spins on the two sublattices (call them A and B) align antiparallel below the **Néel temperature** T_N. The **Néel state** has zero net magnetization but a staggered magnetization (the **order parameter**). Antiferromagnetic magnons have **linear** dispersion ω ∝ k at long wavelengths — a key distinction from the ferromagnetic ω ∝ k² — and form two branches due to the two-sublattice structure.

**定义——反铁磁性与奈尔有序。** 当 J < 0 时，两个子晶格（记为 A 和 B）上的自旋在**奈尔温度** T_N 以下反平行排列。**奈尔态**具有零净磁化强度，但有交错磁化强度（**序参量**）。反铁磁磁振子在长波极限下具有**线性**色散 ω ∝ k——这是与铁磁性 ω ∝ k² 的关键区别——并因双子晶格结构而形成两个支。

---

**Self-test (blank page)**

1. State the Curie law and derive it qualitatively from the energy scale of a spin in a field versus the thermal energy k_B T.
2. Write down the Heisenberg Hamiltonian; explain how J > 0 and J < 0 lead to different ordered states below a critical temperature.
3. What is a magnon? State the ferromagnetic magnon dispersion relation and explain why it is quadratic, not linear.
4. State the Bloch T^{3/2} law and explain its physical origin in terms of magnon statistics.
5. How does the magnon dispersion of an antiferromagnet differ from that of a ferromagnet, and why?

**自测（空白页）**

1. 陈述居里定律，并从自旋在磁场中的能量标度与热能 k_B T 的比较中定性推导它。
2. 写出海森堡哈密顿量；解释 J > 0 和 J < 0 如何在临界温度以下导致不同的有序态。
3. 什么是磁振子？写出铁磁磁振子色散关系，并解释为何它是二次型而非线性的。
4. 陈述布洛赫 T^{3/2} 定律，并从磁振子统计的角度解释其物理起源。
5. 反铁磁体的磁振子色散与铁磁体有何不同，原因是什么？

---

← Previous: [Module 4.5 — Fermi Surface & Electron–Phonon Coupling](./module-4.5-fermi-surface-and-electron-phonon-coupling.md) · [Phase 4 index](./README.md) · Next: [Module 4.7 — Semiconductor Physics](./module-4.7-semiconductor-physics.md) →

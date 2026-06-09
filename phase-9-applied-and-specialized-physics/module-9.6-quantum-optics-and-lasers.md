# Module 9.6 — Quantum Optics & Laser Physics
**模块 9.6 — 量子光学与激光物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.6-quantum-optics-and-lasers-derivations.md)

---

## 1. Einstein A & B Coefficients · 爱因斯坦 A 与 B 系数

**Definition.** Einstein (1917) described the interaction of a two-level atom (energies E₁ < E₂, degeneracies g₁, g₂, transition frequency ν = (E₂−E₁)/h) with a thermal radiation field of spectral energy density u(ν) by three rates. **Absorption** lifts atoms from level 1 to level 2 at rate B₁₂ u(ν) N₁. **Stimulated emission** drives 2 → 1 at rate B₂₁ u(ν) N₂, producing a photon coherent with the driving field. **Spontaneous emission** drives 2 → 1 at rate A₂₁ N₂ independent of the field. Demanding thermal equilibrium with the Planck law forces two universal relations: g₁B₁₂ = g₂B₂₁ and A₂₁/B₂₁ = 8πhν³/c³.

**定义。** 爱因斯坦（1917）用三个速率描述了二能级原子（能量 E₁ < E₂，简并度 g₁、g₂，跃迁频率 ν = (E₂−E₁)/h）与谱能量密度为 u(ν) 的热辐射场的相互作用。**吸收**以速率 B₁₂ u(ν) N₁ 将原子从能级 1 提升到能级 2。**受激发射**以速率 B₂₁ u(ν) N₂ 驱动 2 → 1，产生与驱动场相干的光子。**自发发射**以与场无关的速率 A₂₁ N₂ 驱动 2 → 1。要求与普朗克定律热平衡，强制给出两个普适关系：g₁B₁₂ = g₂B₂₁ 与 A₂₁/B₂₁ = 8πhν³/c³。

**Demonstration.** In steady state the upward and downward rates balance: B₁₂ u N₁ = A₂₁ N₂ + B₂₁ u N₂. Solving for u(ν) and inserting the Boltzmann ratio N₂/N₁ = (g₂/g₁)e^{−hν/kT} reproduces the Planck spectrum only if the two coefficient relations hold; the full algebra is in Derivation A. The ratio A₂₁/B₂₁ ∝ ν³ means spontaneous emission grows steeply with frequency relative to the stimulated process.

**演示。** 稳态下向上与向下速率平衡：B₁₂ u N₁ = A₂₁ N₂ + B₂₁ u N₂。解出 u(ν) 并代入玻尔兹曼比 N₂/N₁ = (g₂/g₁)e^{−hν/kT}，仅当两个系数关系成立时才重现普朗克谱；完整代数见推导 A。比值 A₂₁/B₂₁ ∝ ν³ 意味着自发发射相对受激过程随频率陡峭增长。

**Application.** The ν³ scaling explains why coherent light sources are easy in the microwave (masers, 1954) but hard in the X-ray and γ-ray: at high frequency spontaneous emission rapidly depopulates the upper level before stimulated emission can build up a coherent field. The A/B relation also underlies the radiative lifetime τ = 1/A₂₁ that sets natural linewidths and is the QED rate computed in Modules 6.1/8.2.

**应用。** ν³ 标度解释了为何相干光源在微波段容易实现（脉泽，1954），而在 X 射线和 γ 射线段困难：在高频下，自发发射在受激发射能建立相干场之前迅速耗尽上能级。A/B 关系还给出辐射寿命 τ = 1/A₂₁，它确定了自然线宽，即模块 6.1/8.2 中计算的 QED 速率。

---

## 2. Population Inversion & Laser Gain · 粒子数反转与激光增益

**Definition.** When radiation of density u(ν) passes through the medium, the net rate of photons added to the field by the 2 ↔ 1 transition is proportional to N₂ B₂₁ − N₁ B₁₂ = B₂₁(N₂ − (g₂/g₁)N₁). Amplification (net stimulated emission exceeding absorption) therefore requires a **population inversion**: N₂/g₂ > N₁/g₁. The beam grows as I(z) = I(0) e^{γ(ν)z} with **gain coefficient** γ(ν) ∝ (N₂ − (g₂/g₁)N₁). Lasing starts when the round-trip gain exceeds the round-trip cavity loss (the **threshold condition**).

**定义。** 当密度为 u(ν) 的辐射通过介质时，2 ↔ 1 跃迁向场净增添光子的速率正比于 N₂ B₂₁ − N₁ B₁₂ = B₂₁(N₂ − (g₂/g₁)N₁)。因此放大（净受激发射超过吸收）要求**粒子数反转**：N₂/g₂ > N₁/g₁。光束按 I(z) = I(0) e^{γ(ν)z} 增长，**增益系数** γ(ν) ∝ (N₂ − (g₂/g₁)N₁)。当往返增益超过往返腔损耗时起振（**阈值条件**）。

**Demonstration.** Using the Einstein relation g₁B₁₂ = g₂B₂₁, the net stimulated power per atom is ∝ B₂₁(N₂ − (g₂/g₁)N₁). In a closed two-level system pumped by radiation alone, equilibrium can at best saturate to N₂/g₂ = N₁/g₁ (transparency) but never invert, because the same field that pumps up also stimulates down — shown in Derivation B. Inversion therefore requires auxiliary levels: a three-level scheme (ruby) or a four-level scheme (Nd:YAG, He-Ne) where fast non-radiative decay keeps the lower laser level nearly empty.

**演示。** 利用爱因斯坦关系 g₁B₁₂ = g₂B₂₁，每个原子的净受激功率 ∝ B₂₁(N₂ − (g₂/g₁)N₁)。在仅由辐射泵浦的封闭二能级系统中，平衡最多饱和到 N₂/g₂ = N₁/g₁（透明）而永不反转，因为泵浦向上的同一场也受激向下——见推导 B。因此反转需要辅助能级：三能级方案（红宝石）或四能级方案（Nd:YAG、He-Ne），其中快速非辐射衰变使下激光能级几乎为空。

**Application.** The threshold condition γ(ν)L ≥ loss per pass fixes the minimum pump power of every laser. Four-level lasers reach threshold far more easily than three-level lasers because the lower level starts empty, so even a small upper-level population gives inversion. This logic — pump, invert, place in a resonant cavity above threshold — is the operating principle of every laser from laboratory diode lasers to fusion-driver glass amplifiers.

**应用。** 阈值条件 γ(ν)L ≥ 每程损耗确定了每台激光器的最小泵浦功率。四能级激光器比三能级激光器更易达到阈值，因为下能级初始为空，故即使很小的上能级布居也能给出反转。这一逻辑——泵浦、反转、置于阈值以上的谐振腔中——是从实验室二极管激光器到聚变驱动玻璃放大器的每台激光器的工作原理。

---

## 3. Coherent States & the Quantized Light Field · 相干态与量子化光场

**Definition.** Quantizing a single field mode gives a harmonic oscillator with number states |n⟩, raising/lowering operators a†, a, and Hamiltonian H = ℏω(a†a + ½). The **coherent state** |α⟩ = e^{−|α|²/2} Σₙ (αⁿ/√(n!)) |n⟩ is the eigenstate of the annihilation operator, a|α⟩ = α|α⟩, and is the quantum state that most closely behaves like a classical monochromatic wave of complex amplitude α. Its photon number is **Poisson-distributed**, P(n) = e^{−|α|²}|α|^{2n}/n!, with ⟨n⟩ = |α|² and variance Δn² = |α|², and it saturates the **minimum-uncertainty** bound Δx Δp = ℏ/2.

**定义。** 量子化单个场模式给出一个具有数态 |n⟩、升降算符 a†、a 以及哈密顿量 H = ℏω(a†a + ½) 的谐振子。**相干态** |α⟩ = e^{−|α|²/2} Σₙ (αⁿ/√(n!)) |n⟩ 是湮灭算符的本征态，a|α⟩ = α|α⟩，是最接近经典复振幅为 α 的单色波行为的量子态。其光子数服从**泊松分布**，P(n) = e^{−|α|²}|α|^{2n}/n!，⟨n⟩ = |α|²，方差 Δn² = |α|²，且饱和**最小不确定**界 Δx Δp = ℏ/2。

**Demonstration.** Acting with a on the series and shifting the summation index confirms a|α⟩ = α|α⟩; reading off |⟨n|α⟩|² gives the Poisson law, from which ⟨n⟩ = |α|² and Δn² = |α|² follow immediately, so the relative fluctuation Δn/⟨n⟩ = 1/√⟨n⟩ vanishes in the bright-field limit (Derivation D). Writing the quadratures x ∝ (a + a†), p ∝ (a − a†)/i shows each has the vacuum variance, giving Δx Δp = ℏ/2. A **squeezed state** redistributes this product, pushing one quadrature variance below the vacuum value ½ at the expense of the other.

**演示。** 用 a 作用于级数并移动求和指标确认 a|α⟩ = α|α⟩；读出 |⟨n|α⟩|² 给出泊松定律，由此立即得到 ⟨n⟩ = |α|² 与 Δn² = |α|²，故相对涨落 Δn/⟨n⟩ = 1/√⟨n⟩ 在亮场极限下趋于零（推导 D）。写出正交分量 x ∝ (a + a†)、p ∝ (a − a†)/i，表明每个都具有真空方差，给出 Δx Δp = ℏ/2。**压缩态**重新分配这一乘积，将一个正交分量的方差压到真空值 ½ 以下，以另一个为代价。

**Application.** A laser well above threshold emits a coherent state, so the √⟨n⟩ Poisson noise is the **shot noise** limiting all classical optical measurements. Squeezed light beats this limit and is injected into LIGO/Virgo to improve gravitational-wave strain sensitivity. The single-mode field coupled to one atom is described by the Jaynes–Cummings model (Derivation E), whose vacuum Rabi splitting 2g is the defining signature of cavity quantum electrodynamics.

**应用。** 远高于阈值的激光器发射相干态，故 √⟨n⟩ 泊松噪声是限制所有经典光学测量的**散粒噪声**。压缩光突破此极限，被注入 LIGO/Virgo 以提高引力波应变灵敏度。耦合到单个原子的单模场由杰恩斯–卡明斯模型描述（推导 E），其真空拉比劈裂 2g 是腔量子电动力学的标志性特征。

---

**Self-test (blank page)**

1. Write the three Einstein rate processes and derive both coefficient relations g₁B₁₂ = g₂B₂₁ and A₂₁/B₂₁ = 8πhν³/c³ by imposing the Planck law. Why does the ν³ factor make X-ray lasers hard?
2. State the population-inversion condition and explain why a purely radiatively pumped two-level system can never lase. How do three- and four-level schemes fix this?
3. For a two-level atom driven on resonance, sketch P_e(t). What is a π-pulse and what does it do to the population?
4. Define the coherent state |α⟩, prove it is an eigenstate of a, and derive its photon-number statistics, ⟨n⟩, and Δn².

**自测（空白页）**

1. 写出三个爱因斯坦速率过程，并通过施加普朗克定律推导两个系数关系 g₁B₁₂ = g₂B₂₁ 与 A₂₁/B₂₁ = 8πhν³/c³。为何 ν³ 因子使 X 射线激光器困难？
2. 陈述粒子数反转条件，并解释为何纯辐射泵浦的二能级系统永不能激射。三能级与四能级方案如何解决此问题？
3. 对共振驱动的二能级原子，画出 P_e(t)。什么是 π 脉冲，它对布居做什么？
4. 定义相干态 |α⟩，证明它是 a 的本征态，并推导其光子数统计、⟨n⟩ 和 Δn²。

---

← Previous: [Module 9.5 — Nuclear Reactions & Astrophysics](./module-9.5-nuclear-reactions-and-astrophysics.md) · [Phase 9 index](./README.md) · Next: [Module 9.7 — Atoms in External Fields & Precision Spectroscopy](./module-9.7-atoms-in-external-fields.md) →

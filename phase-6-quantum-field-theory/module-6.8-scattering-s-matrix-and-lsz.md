# Module 6.8 — Scattering, the S-Matrix & LSZ Reduction
**模块 6.8 — 散射、S 矩阵与 LSZ 约化**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.8-scattering-s-matrix-and-lsz-derivations.md)

---

## 1. The S-Matrix & Cross Sections · S 矩阵与截面

**Definition.** Scattering is encoded in the **S-matrix** S_{fi} = ⟨f, out|i, in⟩ = ⟨f|T exp(−i∫Ĥ_int dt)|i⟩, the unitary operator mapping free in-states to free out-states. Writing S = 1 + iT isolates the interacting part; momentum conservation factors out an amplitude ℳ via ⟨f|iT|i⟩ = (2π)⁴δ⁴(Σp) · iℳ. Observable **cross sections** dσ and **decay rates** dΓ are |ℳ|² times kinematic phase space.

**定义。** 散射由 **S 矩阵** S_{fi} = ⟨f, out|i, in⟩ = ⟨f|T exp(−i∫Ĥ_int dt)|i⟩ 编码,它是把自由入态映为自由出态的幺正算符。写成 S = 1 + iT 可分离出相互作用部分;动量守恒提出振幅 ℳ:⟨f|iT|i⟩ = (2π)⁴δ⁴(Σp) · iℳ。可观测的**截面** dσ 与**衰变率** dΓ 均为 |ℳ|² 乘以运动学相空间。

**Demonstration.** Expanding the time-ordered exponential gives the **Dyson series** — order by order, the terms are exactly the Feynman diagrams of Module 6.3. For 2→2 scattering the invariants are the **Mandelstam variables** s = (p₁+p₂)², t = (p₁−p₃)², u = (p₁−p₄)², with s+t+u = Σm². Unitarity S†S = 1 implies the **optical theorem**: Im ℳ(forward) ∝ σ_total.

**演示。** 展开编时指数给出 **戴森级数**——逐阶各项正是模块 6.3 的费曼图。对 2→2 散射,不变量为 **曼德尔斯坦变量** s = (p₁+p₂)²、t = (p₁−p₃)²、u = (p₁−p₄)²,满足 s+t+u = Σm²。幺正性 S†S = 1 给出**光学定理**:Im ℳ(前向) ∝ σ_总。

## 2. LSZ Reduction · LSZ 约化

**Definition.** The **LSZ (Lehmann–Symanzik–Zimmermann) reduction formula** connects S-matrix elements to the time-ordered correlation functions (Green's functions, Module 6.2) of the theory: each external particle contributes a factor that **amputates** the corresponding propagator leg and puts it **on-shell** (p² = m²), with a field-strength renormalization √Z per leg.

**定义。** **LSZ(莱曼–西曼齐克–齐默曼)约化公式**把 S 矩阵元与理论的编时关联函数(格林函数,模块 6.2)联系起来:每个外部粒子贡献一个因子,**截去**相应的传播子外腿并令其**在壳**(p² = m²),每条外腿带一个场强重整化因子 √Z。

**Application.** LSZ is the rigorous bridge from the *off-shell* correlation functions one computes with Feynman diagrams (6.3) and path integrals (6.4) to the *on-shell* amplitudes one measures. Every cross-section calculation — including the QED process e⁺e⁻→μ⁺μ⁻ of Module 8.2 — rests on it.

**应用。** LSZ 是从用费曼图(6.3)和路径积分(6.4)计算的*离壳*关联函数,通向可测量的*在壳*振幅的严格桥梁。每一个截面计算——包括模块 8.2 的 QED 过程 e⁺e⁻→μ⁺μ⁻——都以它为基础。

---

**Self-test (blank page)**

1. Define the S-matrix and write S = 1 + iT; how do dσ and dΓ relate to |ℳ|²?
2. State the Mandelstam variables and the constraint s+t+u = Σm².
3. State the optical theorem and trace it to unitarity S†S = 1.
4. What does the LSZ formula do to each external leg, and why is the factor √Z needed?

**自测（空白页）**

1. 定义 S 矩阵并写出 S = 1 + iT;dσ 与 dΓ 如何与 |ℳ|² 相关?
2. 写出曼德尔斯坦变量及约束 s+t+u = Σm²。
3. 陈述光学定理并追溯到幺正性 S†S = 1。
4. LSZ 公式对每条外腿做了什么?为何需要因子 √Z?

---

← Previous: [Module 6.7 — Exactly Solvable Models & Long-Range Order](./module-6.7-exactly-solvable-models-and-long-range-order.md) · [Phase 6 index](./README.md) · Next: [Module 6.9 — Anomalies & Non-Perturbative QFT](./module-6.9-anomalies-and-nonperturbative-qft.md) →

---
title: "Module 6.8 — Scattering, the S-Matrix & LSZ Reduction"
parent: "Phase 6 — Quantum Field Theory & Many-Body Physics"
nav_order: 8
---

# Module 6.8 — Scattering, the S-Matrix & LSZ Reduction
**模块 6.8 — 散射、S 矩阵与 LSZ 约化**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.8-scattering-s-matrix-and-lsz-derivations.md)

---

## 1. The S-Matrix & Cross Sections · S 矩阵与截面

**Definition.** Scattering is encoded in the **S-matrix** $S_{fi} = \langle f, \text{out}|i, \text{in}\rangle = \langle f|T \exp(-i\int \hat{H}_{\text{int}}\, dt)|i\rangle$, the unitary operator mapping free in-states to free out-states. Writing $S = 1 + iT$ isolates the interacting part; momentum conservation factors out an amplitude $\mathcal{M}$ via $\langle f|iT|i\rangle = (2\pi)^4 \delta^4(\Sigma p) \cdot i\mathcal{M}$. Observable **cross sections** $d\sigma$ and **decay rates** $d\Gamma$ are $|\mathcal{M}|^2$ times kinematic phase space.

**定义。** 散射由 **S 矩阵** $S_{fi} = \langle f, \text{out}|i, \text{in}\rangle = \langle f|T \exp(-i\int \hat{H}_{\text{int}}\, dt)|i\rangle$ 编码,它是把自由入态映为自由出态的幺正算符。写成 $S = 1 + iT$ 可分离出相互作用部分;动量守恒提出振幅 $\mathcal{M}$:$\langle f|iT|i\rangle = (2\pi)^4 \delta^4(\Sigma p) \cdot i\mathcal{M}$。可观测的**截面** $d\sigma$ 与**衰变率** $d\Gamma$ 均为 $|\mathcal{M}|^2$ 乘以运动学相空间。

**Demonstration.** Expanding the time-ordered exponential gives the **Dyson series** — order by order, the terms are exactly the Feynman diagrams of Module 6.3. For $2\to 2$ scattering the invariants are the **Mandelstam variables** $s = (p_1+p_2)^2$, $t = (p_1-p_3)^2$, $u = (p_1-p_4)^2$, with $s+t+u = \Sigma m^2$. Unitarity $S^\dagger S = 1$ implies the **optical theorem**: $\operatorname{Im}\mathcal{M}(\text{forward}) \propto \sigma_{\text{total}}$.

**演示。** 展开编时指数给出 **戴森级数**——逐阶各项正是模块 6.3 的费曼图。对 $2\to 2$ 散射,不变量为 **曼德尔斯坦变量** $s = (p_1+p_2)^2$、$t = (p_1-p_3)^2$、$u = (p_1-p_4)^2$,满足 $s+t+u = \Sigma m^2$。幺正性 $S^\dagger S = 1$ 给出**光学定理**:$\operatorname{Im}\mathcal{M}(\text{前向}) \propto \sigma_{\text{总}}$。

## 2. LSZ Reduction · LSZ 约化

**Definition.** The **LSZ (Lehmann–Symanzik–Zimmermann) reduction formula** connects S-matrix elements to the time-ordered correlation functions (Green's functions, Module 6.2) of the theory: each external particle contributes a factor that **amputates** the corresponding propagator leg and puts it **on-shell** ($p^2 = m^2$), with a field-strength renormalization $\sqrt{Z}$ per leg.

**定义。** **LSZ(莱曼–西曼齐克–齐默曼)约化公式**把 S 矩阵元与理论的编时关联函数(格林函数,模块 6.2)联系起来:每个外部粒子贡献一个因子,**截去**相应的传播子外腿并令其**在壳**($p^2 = m^2$),每条外腿带一个场强重整化因子 $\sqrt{Z}$。

**Application.** LSZ is the rigorous bridge from the *off-shell* correlation functions one computes with Feynman diagrams (6.3) and path integrals (6.4) to the *on-shell* amplitudes one measures. Every cross-section calculation — including the QED process $e^+e^-\to\mu^+\mu^-$ of Module 8.2 — rests on it.

**应用。** LSZ 是从用费曼图(6.3)和路径积分(6.4)计算的*离壳*关联函数,通向可测量的*在壳*振幅的严格桥梁。每一个截面计算——包括模块 8.2 的 QED 过程 $e^+e^-\to\mu^+\mu^-$——都以它为基础。

---

**Self-test (blank page)**

1. Define the S-matrix and write $S = 1 + iT$; how do $d\sigma$ and $d\Gamma$ relate to $|\mathcal{M}|^2$?
2. State the Mandelstam variables and the constraint $s+t+u = \Sigma m^2$.
3. State the optical theorem and trace it to unitarity $S^\dagger S = 1$.
4. What does the LSZ formula do to each external leg, and why is the factor $\sqrt{Z}$ needed?

**自测（空白页）**

1. 定义 S 矩阵并写出 $S = 1 + iT$;$d\sigma$ 与 $d\Gamma$ 如何与 $|\mathcal{M}|^2$ 相关?
2. 写出曼德尔斯坦变量及约束 $s+t+u = \Sigma m^2$。
3. 陈述光学定理并追溯到幺正性 $S^\dagger S = 1$。
4. LSZ 公式对每条外腿做了什么?为何需要因子 $\sqrt{Z}$?

---

← Previous: [Module 6.7 — Exactly Solvable Models & Long-Range Order](./module-6.7-exactly-solvable-models-and-long-range-order.md) · [Phase 6 index](./README.md) · Next: [Module 6.9 — Anomalies & Non-Perturbative QFT](./module-6.9-anomalies-and-nonperturbative-qft.md) →

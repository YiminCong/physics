# Module 6.5 — Canonical Quantization of Fields ⭐
**模块 6.5 — 场的正则量子化 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**

---

## 1. From Classical Fields to Quantum Operators · 从经典场到量子算符

**Definition.** Canonical quantization promotes a classical field to a quantum operator by imposing equal-time commutation (bosons) or anticommutation (fermions) relations, exactly as position and momentum were promoted in ordinary QM. Starting from a classical Lagrangian density L(φ, ∂_μ φ), the canonical momentum is π(x) = ∂L/∂(∂_t φ), and the equal-time commutator [φ(x,t), π(x',t)] = iℏ δ³(x − x') (compare [q, p] = iℏ). This procedure works for any Lorentz-covariant field theory.

**定义。** 正则量子化通过施加等时对易（玻色子）或反对易（费米子）关系，将经典场提升为量子算符，这与普通量子力学中位置和动量的提升完全类似。从经典拉格朗日密度 L(φ, ∂_μ φ) 出发，正则动量为 π(x) = ∂L/∂(∂_t φ)，等时对易子为 [φ(x,t), π(x',t)] = iℏ δ³(x − x')（对比 [q, p] = iℏ）。该程序适用于任何洛伦兹协变场论。

For the real scalar (Klein–Gordon) field, L = ½(∂_μ φ)² − ½m²φ² (natural units ℏ = c = 1 here). The equation of motion is the Klein–Gordon equation (∂² + m²)φ = 0, with plane-wave solutions of frequency ω_k = √(k² + m²). Expanding in modes: φ(x,t) = ∫ d³k/(2π)³ 1/√(2ω_k) [a_k e^{i(k·x − ω_k t)} + a†_k e^{−i(k·x − ω_k t)}]. Imposing [φ, π] = iδ³ forces [a_k, a†_{k'}] = δ³(k−k'): the mode operators are bosonic creation/annihilation operators (Module 6.1). Each mode k is a harmonic oscillator; particles are its quanta.

对于实标量（克莱因–戈登）场，L = ½(∂_μ φ)² − ½m²φ²（这里使用自然单位 ℏ = c = 1）。运动方程为克莱因–戈登方程 (∂² + m²)φ = 0，频率为 ω_k = √(k² + m²) 的平面波是其解。按模式展开：φ(x,t) = ∫ d³k/(2π)³ 1/√(2ω_k) [a_k e^{i(k·x − ω_k t)} + a†_k e^{−i(k·x − ω_k t)}]。施加 [φ, π] = iδ³ 强制 [a_k, a†_{k'}] = δ³(k−k')：模式算符是玻色子产生/湮灭算符（模块 6.1）。每个模式 k 是一个谐振子；粒子是其量子。

**Demonstration.** The Hamiltonian is H = ∫ d³k/(2π)³ ω_k (a†_k a_k + ½). The ½ per mode sums to the zero-point energy of the field — infinite in the continuum, and the first ultraviolet divergence of QFT. In curved spacetime or between conducting plates (Casimir effect) this zero-point energy has measurable consequences. Normal-ordering :H: = ∫ d³k ω_k a†_k a_k subtracts it by convention in flat-space QFT. The particle interpretation is now transparent: a†_k|0⟩ is a one-particle state of momentum k and energy ω_k, and |0⟩ (no quanta in any mode) is the vacuum.

**演示。** 哈密顿量为 H = ∫ d³k/(2π)³ ω_k (a†_k a_k + ½)。每个模式的 ½ 求和给出场的零点能——在连续极限下为无穷大，这是 QFT 的第一个紫外发散。在弯曲时空中或导体板之间（卡西米尔效应），零点能有可测量的后果。正规序 :H: = ∫ d³k ω_k a†_k a_k 按惯例在平直时空 QFT 中将其减去。粒子诠释现在是透明的：a†_k|0⟩ 是动量为 k、能量为 ω_k 的单粒子态，|0⟩（任何模式中均无量子）是真空。

The Dirac field (for spin-½ particles) requires Lorentz covariance from Special Relativity (Modules 1.13–1.15). The Lagrangian L = ψ̄(iγ^μ ∂_μ − m)ψ, where γ^μ are the 4×4 Dirac matrices satisfying {γ^μ, γ^ν} = 2g^{μν}, and ψ̄ = ψ†γ⁰. The equation of motion is the Dirac equation (iγ^μ ∂_μ − m)ψ = 0. Expanding ψ in plane-wave spinors u^s(k), v^s(k) and quantizing with anticommutators {b^s_k, b†s'_{k'}} = δ^{ss'} δ³(k−k') gives particles (b†) and antiparticles (d†) as distinct quanta. The anticommutation is required by the spin-statistics theorem: integer-spin fields commute (bosons), half-integer fields anticommute (fermions).

狄拉克场（自旋-½ 粒子）需要来自狭义相对论的洛伦兹协变性（模块 1.13–1.15）。拉格朗日量 L = ψ̄(iγ^μ ∂_μ − m)ψ，其中 γ^μ 是满足 {γ^μ, γ^ν} = 2g^{μν} 的 4×4 狄拉克矩阵，ψ̄ = ψ†γ⁰。运动方程是狄拉克方程 (iγ^μ ∂_μ − m)ψ = 0。将 ψ 按平面波旋量 u^s(k)、v^s(k) 展开，并用反对易子 {b^s_k, b†s'_{k'}} = δ^{ss'} δ³(k−k') 量子化，给出粒子（b†）和反粒子（d†）作为不同的量子。反对易化是自旋-统计定理的要求：整数自旋场对易（玻色子），半整数自旋场反对易（费米子）。

**Application.** The quantized electromagnetic field A^μ(x) yields photons as its quanta. In Coulomb gauge ∇·A = 0, the two transverse polarization modes are quantized as bosons with [a^λ_k, a†λ'_{k'}] = δ^{λλ'} δ³(k−k'). Photons are massless (ω_k = |k|c), have two helicities, and the field-theoretic description of their interaction with charged fermions is QED (Phase 8). Historically, canonical quantization of the EM field by Dirac (1927) was the birth of QFT. The framework extends directly to the W and Z bosons and gluons of the Standard Model (Phase 8), and underlies the gauge-field quantization in Module 8.1.

**应用。** 量子化的电磁场 A^μ(x) 以光子为其量子。在库仑规范 ∇·A = 0 中，两个横向极化模式以玻色子方式量子化，满足 [a^λ_k, a†λ'_{k'}] = δ^{λλ'} δ³(k−k')。光子是无质量的（ω_k = |k|c），有两个螺旋度，它们与带电费米子相互作用的场论描述就是 QED（第 8 阶段）。历史上，狄拉克（1927 年）对电磁场的正则量子化是 QFT 的诞生。该框架直接推广到标准模型的 W 玻色子、Z 玻色子和胶子（第 8 阶段），并支撑模块 8.1 中的规范场量子化。

---

## 2. Particles, Antiparticles, and the Vacuum · 粒子、反粒子与真空

**Definition.** For a complex scalar or Dirac field, charge conjugation maps particles to antiparticles: the field φ has quanta of charge +e, and φ† has quanta of charge −e (antiparticles). This is distinct from the real scalar field where particle and antiparticle are identical. The CPT theorem — a consequence of Lorentz invariance, locality, and unitarity alone — guarantees that particles and antiparticles have equal mass and opposite charge; it is among the most precisely tested results in physics.

**定义。** 对于复标量场或狄拉克场，电荷共轭将粒子映射到反粒子：场 φ 的量子带电荷 +e，φ† 的量子带电荷 −e（反粒子）。这与实标量场不同，在实标量场中粒子与反粒子是相同的。CPT 定理——仅由洛伦兹不变性、局域性和幺正性推导出——保证粒子和反粒子具有相同的质量和相反的电荷；它是物理学中经受检验最精确的结果之一。

**Demonstration.** The Feynman propagator for the scalar field G_F(x−x') = ⟨0|T φ(x)φ†(x')|0⟩ equals ∫ d⁴k/(2π)⁴ i/(k²−m²+iε) e^{ik·(x−x')}. The iε prescription (Feynman prescription) selects the propagation of positive-frequency modes (particles) forward in time and negative-frequency modes (antiparticles) backward in time. This is the propagator that appears in Feynman rules (Module 6.3) and connects the diagrammatic expansion directly to canonical quantization.

**演示。** 标量场的费曼传播子 G_F(x−x') = ⟨0|T φ(x)φ†(x')|0⟩ 等于 ∫ d⁴k/(2π)⁴ i/(k²−m²+iε) e^{ik·(x−x')}。iε 处方（费曼处方）选择正频模式（粒子）向前传播和负频模式（反粒子）向后传播。这是出现在费曼规则（模块 6.3）中的传播子，将图展开直接联系到正则量子化。

**Application.** Canonical field quantization is relativistic QFT proper. Every prediction of QED — the anomalous magnetic moment of the electron g−2 = α/π + … (matching experiment to 12 significant figures), the Lamb shift, Compton scattering — follows from quantizing the Dirac and Maxwell fields and computing Feynman diagrams in this framework. The same procedure, applied to non-Abelian gauge fields (Phase 8), gives the electroweak theory and QCD. In condensed matter, the non-relativistic limit (|k| ≪ mc/ℏ) recovers the field operators of Module 6.1, confirming that second quantization is simply canonical QFT at low energies.

**应用。** 正则场量子化是真正的相对论 QFT。QED 的每一个预言——电子反常磁矩 g−2 = α/π + …（与实验符合到 12 位有效数字）、兰姆移位、康普顿散射——都来自于量子化狄拉克场和麦克斯韦场并在此框架内计算费曼图。同样的程序应用于非阿贝尔规范场（第 8 阶段），给出电弱理论和量子色动力学（QCD）。在凝聚态物理中，非相对论极限（|k| ≪ mc/ℏ）还原了模块 6.1 的场算符，证实二次量子化就是低能下的正则 QFT。

---

## Self-test (blank page) · 自测（空白页）

1. Starting from the Klein–Gordon Lagrangian density, derive the canonical momentum π(x) and write down the equal-time commutation relation [φ(x,t), π(x',t)]. Show that this forces [a_k, a†_{k'}] = δ³(k−k').
2. Why must the Dirac field be quantized with anticommutators rather than commutators? State the spin-statistics theorem.
3. What is an antiparticle in terms of the field expansion? How does the Feynman iε prescription encode the particle/antiparticle interpretation of the propagator?

**自测（空白页）**

1. 从克莱因–戈登拉格朗日密度出发，推导正则动量 π(x) 并写出等时对易关系 [φ(x,t), π(x',t)]。证明这强制 [a_k, a†_{k'}] = δ³(k−k')。
2. 为什么狄拉克场必须用反对易子而非对易子量子化？陈述自旋-统计定理。
3. 从场的展开来看，什么是反粒子？费曼 iε 处方如何编码传播子的粒子/反粒子诠释？

---

← Previous: [Module 6.4 — Path Integrals & Field Theory](./module-6.4-path-integrals.md) · [Phase 6 index](./README.md) · Next: [Module 6.6 — Renormalization & the Renormalization Group](./module-6.6-renormalization.md) →

# Module 6.2 — Green's Functions & Propagators ⭐
**模块 6.2 — 格林函数与传播子 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.2-greens-functions-derivations.md)

---

## 1. The Single-Particle Green's Function · 单粒子格林函数

**Definition.** The retarded single-particle Green's function is G^R(x,t; x',t') = −i θ(t−t') ⟨{ψ(x,t), ψ†(x',t')}⟩, where ψ(x,t) is the field operator in the Heisenberg picture (Module 3.10), θ is the Heaviside step, and the average is over the ground state (T = 0) or the thermal ensemble. In momentum-frequency space for a translationally invariant system, G^R(k,ω) encodes everything about single-particle excitations: its poles locate quasiparticle energies, and its imaginary part gives the quasiparticle lifetime.

**定义。** 推迟单粒子格林函数为 G^R(x,t; x',t') = −i θ(t−t') ⟨{ψ(x,t), ψ†(x',t')}⟩，其中 ψ(x,t) 是海森堡绘景中的场算符（模块 3.10），θ 是 Heaviside 阶跃函数，平均取自基态（T = 0）或热系综。对于平移不变系统，动量-频率空间中的 G^R(k,ω) 编码了单粒子激发的全部信息：其极点定位准粒子能量，虚部给出准粒子寿命。

For a free Fermi gas, G⁰(k,ω) = 1/(ω − ε_k/ℏ + iη) where η → 0⁺ ensures causality (retarded boundary condition). The pole at ω = ε_k/ℏ is a sharp quasiparticle. Interactions broaden it: the self-energy Σ(k,ω) (Module 6.3) shifts and smears the pole.

对于自由费米气体，G⁰(k,ω) = 1/(ω − ε_k/ℏ + iη)，其中 η → 0⁺ 保证因果性（推迟边界条件）。ω = ε_k/ℏ 处的极点是一个尖锐准粒子。相互作用使其展宽：自能 Σ(k,ω)（模块 6.3）移动并模糊该极点。

**Demonstration.** The spectral function A(k,ω) = −(1/π) Im G^R(k,ω) is a real, positive-definite density of states in (k,ω) space. For the free gas, A(k,ω) = δ(ω − ε_k/ℏ): a delta function on the bare dispersion. With interactions, A(k,ω) acquires a Lorentzian width Γ = Im Σ/ℏ — the inverse quasiparticle lifetime. The spectral sum rule ∫ dω A(k,ω) = 1 (per spin) is exact and provides a consistency check.

**演示。** 谱函数 A(k,ω) = −(1/π) Im G^R(k,ω) 是 (k,ω) 空间中实的、正定的态密度。对于自由气体，A(k,ω) = δ(ω − ε_k/ℏ)：裸色散关系上的一个 δ 函数。加入相互作用后，A(k,ω) 获得洛伦兹宽度 Γ = Im Σ/ℏ——即准粒子寿命的倒数。谱函数求和规则 ∫ dω A(k,ω) = 1（每个自旋）是精确的，可作为一致性检验。

The analytic structure follows from causality (Module 0.4): G^R(k,ω) is analytic in the upper half ω-plane. The Kramers–Kronig relations then link Re G^R and Im G^R: Re G^R(k,ω) = (1/π) P ∫ dω' Im G^R(k,ω')/(ω'−ω), directly analogous to the dielectric function dispersions encountered in electrodynamics. These relations are a consequence of causality alone, not of any specific model.

解析结构源于因果性（模块 0.4）：G^R(k,ω) 在 ω 平面的上半平面解析。克喇末–克朗尼希关系将 Re G^R 与 Im G^R 联系起来：Re G^R(k,ω) = (1/π) P ∫ dω' Im G^R(k,ω')/(ω'−ω)，与电动力学中遇到的介电函数色散关系直接类比。这些关系仅是因果性的推论，与具体模型无关。

**Application.** Angle-resolved photoemission spectroscopy (ARPES) directly images A(k,ω): a photon ejects an electron with momentum k and energy ω, and the intensity is proportional to A(k,ω) f(ω) where f is the Fermi function. ARPES data on cuprate superconductors and Fermi liquids are interpreted almost entirely via G(k,ω).

**应用。** 角分辨光电子能谱（ARPES）直接成像谱函数 A(k,ω)：一个光子将动量为 k、能量为 ω 的电子弹出，强度正比于 A(k,ω) f(ω)，其中 f 是费米函数。铜氧化物超导体和费米液体的 ARPES 数据几乎完全通过 G(k,ω) 来解释。

---

## 2. Nambu–Gor'kov Green's Function and BCS · Nambu–Gor'kov 格林函数与 BCS

**Definition.** For a superconductor, a single Green's function is insufficient because the BCS ground state mixes particles and holes via the anomalous average F(k) = ⟨c_{−k↓}c_{k↑}⟩ ≠ 0. Nambu and Gor'kov (following Fetter & Walecka) promote the spinor Ψ_k = (c_{k↑}, c†_{−k↓})^T and define the 2×2 matrix Green's function Ĝ(k,ω) = −i ⟨T Ψ_k(t) Ψ†_k(0)⟩. Its diagonal elements are the normal G(k,ω), and its off-diagonal elements are the anomalous F(k,ω) which carry the pairing information.

**定义。** 对于超导体，单个格林函数是不够的，因为 BCS 基态通过反常平均值 F(k) = ⟨c_{−k↓}c_{k↑}⟩ ≠ 0 将粒子与空穴混合。Nambu 和 Gor'kov（参照 Fetter & Walecka）引入旋量 Ψ_k = (c_{k↑}, c†_{−k↓})^T，并定义 2×2 矩阵格林函数 Ĝ(k,ω) = −i ⟨T Ψ_k(t) Ψ†_k(0)⟩。其对角元为正常格林函数 G(k,ω)，非对角元为携带配对信息的反常格林函数 F(k,ω)。

**Demonstration.** Inverting the Dyson equation (Module 6.3) in Nambu space gives Ĝ(k,ω) = (ω − ξ_k τ_z − Δ τ_x)^{−1} where τ are Pauli matrices in particle-hole space, ξ_k = ε_k − μ, and Δ is the BCS gap. The poles of det Ĝ = 0 give ω = ±E_k, E_k = √(ξ²_k + Δ²) — the Bogoliubov quasiparticle spectrum derived here from Green's function poles rather than the canonical Bogoliubov transformation.

**演示。** 在 Nambu 空间中对戴森方程（模块 6.3）求逆，得到 Ĝ(k,ω) = (ω − ξ_k τ_z − Δ τ_x)^{−1}，其中 τ 是粒子-空穴空间中的泡利矩阵，ξ_k = ε_k − μ，Δ 是 BCS 能隙。det Ĝ = 0 的极点给出 ω = ±E_k，E_k = √(ξ²_k + Δ²)——这里从格林函数极点而非正则 Bogoliubov 变换推导出了 Bogoliubov 准粒子谱。

**Application.** The Nambu–Gor'kov formalism is the foundation of modern superconductivity theory: it allows systematic diagrammatic calculation of Δ (self-consistently), the density of states N(ω) ∝ |ω|/√(ω²−Δ²) (measured by tunneling spectroscopy), and the response functions needed for transport. It generalizes cleanly to unconventional superconductors (d-wave, etc.) and to Nambu spinors in topological systems.

**应用。** Nambu–Gor'kov 形式主义是现代超导理论的基础：它允许系统地用图的方法自洽地计算 Δ、态密度 N(ω) ∝ |ω|/√(ω²−Δ²)（由隧道谱测量）以及输运所需的响应函数。它可以直接推广到非常规超导体（d 波等）和拓扑系统中的 Nambu 旋量。

---

## Self-test (blank page) · 自测（空白页）

1. Write down G⁰(k,ω) for a free Fermi gas. Where are its poles? How does switching on an interaction Σ(k,ω) move or broaden them?
2. State the Kramers–Kronig relation for G^R(k,ω) and explain which physical principle it encodes.
3. What is the anomalous Green's function F(k,ω) and why is it zero in a normal metal but nonzero in a BCS superconductor?

**自测（空白页）**

1. 写出自由费米气体的 G⁰(k,ω)。其极点在哪里？引入相互作用 Σ(k,ω) 后，极点如何移动或展宽？
2. 陈述 G^R(k,ω) 的克喇末–克朗尼希关系，并解释它编码了哪条物理原理。
3. 反常格林函数 F(k,ω) 是什么？为什么它在正常金属中为零，而在 BCS 超导体中不为零？

---

← Previous: [Module 6.1 — Second Quantization & the Many-Body Problem](./module-6.1-second-quantization.md) · [Phase 6 index](./README.md) · Next: [Module 6.3 — Feynman Diagrams & Perturbation Theory](./module-6.3-feynman-diagrams.md) →

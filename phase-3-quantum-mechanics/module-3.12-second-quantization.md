# Module 3.12 — Symmetry, Identical Particles & Second Quantization ⭐⭐
**模块 3.12 — 对称性、全同粒子与二次量子化 ⭐⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.12-derivations.md)

---

## 1. Discrete Symmetries · 离散对称性

**Definition.** Beyond continuous symmetries (Module 1.4), discrete ones matter: **parity** (spatial inversion) and **time reversal** classify states and constrain dynamics.

**定义。** 除连续对称性（模块 1.4）之外，离散对称性同样重要：**宇称**（空间反演）和**时间反演**对态进行分类并约束动力学。

## 2. Second Quantization — the key tool for what's ahead · 二次量子化——前方最重要的工具

**Definition.** Instead of tracking labeled particles, track **occupation numbers** of single-particle states. Introduce **creation/annihilation operators**: bosons aₖ†, aₖ with [aₖ, aₖ′†] = δₖₖ′; fermions cₖ†, cₖ with the **anticommutator** {cₖ, cₖ′†} = δₖₖ′. The number operator is n̂ₖ = cₖ†cₖ.

**定义。** 不追踪有标记的粒子，而是追踪单粒子态的**占据数**。引入**产生/湮灭算符**：玻色子 aₖ†、aₖ 满足 [aₖ, aₖ′†] = δₖₖ′；费米子 cₖ†、cₖ 满足**反对易子** {cₖ, cₖ′†} = δₖₖ′。粒子数算符为 n̂ₖ = cₖ†cₖ。

**Demonstration.** A many-fermion state is built by acting creation operators on the vacuum: |Ψ⟩ = c₁† c₂† … |0⟩. The anticommutation {c₁†, c₂†} = 0 automatically enforces antisymmetry and the Pauli principle — c²† = 0 means you can't create two fermions in the same state. This is just the harmonic-oscillator ladder algebra (3.2) promoted to "one oscillator per mode."

**演示。** 多费米子态通过对真空作用产生算符来构建：|Ψ⟩ = c₁† c₂† … |0⟩。反对易关系 {c₁†, c₂†} = 0 自动强制满足反对称性和泡利不相容原理——c²† = 0 意味着不能在同一态中产生两个费米子。这正是谐振子梯形代数（3.2）推广为"每个模式一个振子"的结果。

**Application.** **This is the single most important tool to carry into superconductivity.** The BCS Hamiltonian (Phase 5) is written entirely in terms of cₖ† and cₖ; Cooper pairing is the operator c_{k↑}† c_{−k↓}†; and the whole machinery of condensed-matter field theory (Phase 6) is second quantization. If only one module of Phase 3 must be airtight, make it this one (alongside 3.2 and 3.5, which it builds on).

**应用。** **这是进入超导性最重要的单一工具。** BCS 哈密顿量（第 5 阶段）完全用 cₖ† 和 cₖ 书写；库珀配对即算符 c_{k↑}† c_{−k↓}†；凝聚态场论的全部机制（第 6 阶段）都是二次量子化。若第 3 阶段只能有一个模块做到炉火纯青，就是这个（以及它所依赖的 3.2 和 3.5）。

---

← Previous: [Module 3.11 — Angular Momentum, Advanced](./module-3.11-angular-momentum-advanced.md) · [Phase 3 index](./README.md) · Next: [Module 3.13 — Entanglement, EPR & Bell's Theorem](./module-3.13-entanglement-epr-and-bell.md) →

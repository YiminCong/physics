# Module 3.3 — Formalism ⭐
**模块 3.3 — 形式化框架 ⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**

---

## 1. Hilbert Space & Dirac Notation · 希尔伯特空间与狄拉克符号

**Definition.** States are vectors |ψ⟩ in a complex **Hilbert space**; ⟨φ|ψ⟩ is the inner product (Module 0.2). Observables are **Hermitian operators**; their real eigenvalues are the possible measurement outcomes, and their orthonormal eigenstates form a basis.

**定义。** 态是复**希尔伯特空间**中的向量 |ψ⟩；⟨φ|ψ⟩ 是内积（模块 0.2）。可观测量是**厄米算符**；其实数本征值是可能的测量结果，正交归一本征态构成一组基。

## 2. Measurement, Commutators & Uncertainty · 测量、对易子与不确定性

**Definition.** Expand |ψ⟩ = Σ cₙ|n⟩ with cₙ = ⟨n|ψ⟩; the probability of measuring eigenvalue λₙ is |cₙ|². Two observables are **compatible** (simultaneously measurable) iff their commutator [Â,B̂] = ÂB̂ − B̂Â vanishes.

**定义。** 展开 |ψ⟩ = Σ cₙ|n⟩，其中 cₙ = ⟨n|ψ⟩；测量到本征值 λₙ 的概率为 |cₙ|²。两个可观测量**相容**（可同时测量）当且仅当它们的对易子 [Â,B̂] = ÂB̂ − B̂Â 为零。

**Demonstration.** [x̂, p̂] = iℏ (nonzero) → x and p cannot be sharply defined together; the generalized uncertainty relation ΔA ΔB ≥ ½|⟨[Â,B̂]⟩| then yields Δx Δp ≥ ℏ/2.

**演示。** [x̂, p̂] = iℏ（非零）→ x 和 p 不能同时精确确定；广义不确定性关系 ΔA ΔB ≥ ½|⟨[Â,B̂]⟩| 给出 Δx Δp ≥ ℏ/2。

**Application.** This is the rigorous skeleton of QM — linear algebra (Module 0.2) with physical meaning. Hermitian = real measurements; commutators = uncertainty and conservation.

**应用。** 这是量子力学的严格骨架——具有物理意义的线性代数（模块 0.2）。厄米性 = 实数测量；对易子 = 不确定性与守恒。

---

← Previous: [Module 3.2 — Time-Independent Schrödinger Equation](./module-3.2-time-independent-schrodinger-equation.md) · [Phase 3 index](./README.md) · Next: [Module 3.4 — Quantum Mechanics in 3D](./module-3.4-quantum-mechanics-in-3d.md) →

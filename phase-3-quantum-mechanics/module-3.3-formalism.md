---
title: "Module 3.3 — Formalism"
parent: "Phase 3 — Quantum Mechanics (the core)"
nav_order: 3
---

# Module 3.3 — Formalism ⭐
**模块 3.3 — 形式化框架 ⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.3-derivations.md)

---

## 1. Hilbert Space & Dirac Notation · 希尔伯特空间与狄拉克符号

**Definition.** States are vectors $|\psi\rangle$ in a complex **Hilbert space**; $\langle\phi|\psi\rangle$ is the inner product (Module 0.2). Observables are **Hermitian operators**; their real eigenvalues are the possible measurement outcomes, and their orthonormal eigenstates form a basis.

**定义。** 态是复**希尔伯特空间**中的向量 $|\psi\rangle$；$\langle\phi|\psi\rangle$ 是内积（模块 0.2）。可观测量是**厄米算符**；其实数本征值是可能的测量结果，正交归一本征态构成一组基。

## 2. Measurement, Commutators & Uncertainty · 测量、对易子与不确定性

**Definition.** Expand $|\psi\rangle = \sum_n c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$; the probability of measuring eigenvalue $\lambda_n$ is $|c_n|^2$. Two observables are **compatible** (simultaneously measurable) iff their commutator $[\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ vanishes.

**定义。** 展开 $|\psi\rangle = \sum_n c_n|n\rangle$，其中 $c_n = \langle n|\psi\rangle$；测量到本征值 $\lambda_n$ 的概率为 $|c_n|^2$。两个可观测量**相容**（可同时测量）当且仅当它们的对易子 $[\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ 为零。

**Demonstration.** $[\hat{x}, \hat{p}] = i\hbar$ (nonzero) $\Rightarrow$ $x$ and $p$ cannot be sharply defined together; the generalized uncertainty relation $\Delta A\,\Delta B \geq \tfrac12|\langle[\hat{A},\hat{B}]\rangle|$ then yields $\Delta x\,\Delta p \geq \hbar/2$.

**演示。** $[\hat{x}, \hat{p}] = i\hbar$（非零）$\Rightarrow$ $x$ 和 $p$ 不能同时精确确定；广义不确定性关系 $\Delta A\,\Delta B \geq \tfrac12|\langle[\hat{A},\hat{B}]\rangle|$ 给出 $\Delta x\,\Delta p \geq \hbar/2$。

**Application.** This is the rigorous skeleton of QM — linear algebra (Module 0.2) with physical meaning. Hermitian = real measurements; commutators = uncertainty and conservation.

**应用。** 这是量子力学的严格骨架——具有物理意义的线性代数（模块 0.2）。厄米性 = 实数测量；对易子 = 不确定性与守恒。

---

**Self-test (blank page)**

1. Why must observables be represented by Hermitian operators? What is special about the eigenvalues and eigenstates of a Hermitian operator?
2. If a state $|\psi\rangle = \sum_n c_n|n\rangle$ is expanded in the eigenbasis of an observable, what is the probability of obtaining eigenvalue $\lambda_n$ in a measurement, and what happens to the state immediately after?
3. Compute the commutator $[\hat{x}, \hat{p}]$ and state what its non-zero value implies about simultaneously measuring position and momentum. Derive the resulting uncertainty relation $\Delta x\,\Delta p \geq \hbar/2$ from the general form $\Delta A\,\Delta B \geq \tfrac12|\langle[\hat{A},\hat{B}]\rangle|$.

**自测（空白页）**

1. 为什么可观测量必须用厄米算符表示？厄米算符的本征值和本征态有何特殊性质？
2. 若态 $|\psi\rangle = \sum_n c_n|n\rangle$ 展开于某可观测量的本征基，测量得到本征值 $\lambda_n$ 的概率是多少？测量后态立即变为什么？
3. 计算对易子 $[\hat{x}, \hat{p}]$，并说明其非零结果对同时测量位置和动量意味着什么。由广义不确定关系 $\Delta A\,\Delta B \geq \tfrac12|\langle[\hat{A},\hat{B}]\rangle|$ 推导出 $\Delta x\,\Delta p \geq \hbar/2$。

---

← Previous: [Module 3.2 — Time-Independent Schrödinger Equation](./module-3.2-time-independent-schrodinger-equation.md) · [Phase 3 index](./README.md) · Next: [Module 3.4 — Quantum Mechanics in 3D](./module-3.4-quantum-mechanics-in-3d.md) →

# Module 3.5 — Identical Particles ⭐
**模块 3.5 — 全同粒子 ⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.5-derivations.md)

---

## 1. Symmetrization & the Pauli Principle · 对称化与泡利不相容原理

**Definition.** Identical quantum particles are indistinguishable, so swapping two must leave $|\psi|^2$ unchanged. This forces the total wave function to be either **symmetric** (bosons) or **antisymmetric** (fermions) under exchange. Antisymmetry gives the **Pauli exclusion principle**: no two fermions in the same state.

**定义。** 全同量子粒子是不可分辨的，因此交换两个粒子必须保持 $|\psi|^2$ 不变。这迫使总波函数在交换下为**对称**（玻色子）或**反对称**（费米子）。反对称性给出**泡利不相容原理**：没有两个费米子处于相同的态。

## 2. Many-Fermion Systems · 多费米子系统

**Demonstration.** Two particles: symmetric $\psi_S \propto \psi_a(1)\psi_b(2) + \psi_a(2)\psi_b(1)$; antisymmetric $\psi_A \propto \psi_a(1)\psi_b(2) - \psi_a(2)\psi_b(1)$, which vanishes if $a = b$ (exclusion). For many electrons, the antisymmetric state is a **Slater determinant**, and electrons fill levels up to the Fermi energy.

**演示。** 两个粒子：对称态 $\psi_S \propto \psi_a(1)\psi_b(2) + \psi_a(2)\psi_b(1)$；反对称态 $\psi_A \propto \psi_a(1)\psi_b(2) - \psi_a(2)\psi_b(1)$，当 $a = b$ 时为零（不相容原理）。对于多电子体系，反对称态为**斯莱特行列式**，电子填充至费米能级。

**Application.** The bridge to solids and superconductivity: the **free electron gas**, band filling, and the **Fermi surface** (Phase 4) all follow from this. And a **Cooper pair** (Phase 5) is two fermions bound into a composite that behaves bosonically — the exchange rules here are what make that special.

**应用。** 通往固体和超导性的桥梁：**自由电子气**、能带填充和**费米面**（第 4 阶段）都由此而来。**库珀对**（第 5 阶段）是两个费米子结合成表现出玻色子行为的复合体——正是这里的交换规则使其特殊。

## Key results · 核心结果

- $\psi_S \propto \psi_a(1)\psi_b(2) + \psi_a(2)\psi_b(1)$ (bosons) vs $\psi_A \propto \psi_a(1)\psi_b(2) - \psi_a(2)\psi_b(1)$ (fermions) · 对称／反对称波函数
- Pauli exclusion: two fermions cannot share a state ($\psi_A \to 0$) · 泡利不相容
- Exchange symmetry produces an effective exchange force · 交换对称性给出交换力
- Many-fermion states ⟶ Slater determinant ⟶ second quantization (3.12) · 通往斯莱特行列式与二次量子化

---

**Self-test (blank page)**

1. Why must the wave function of identical particles be either symmetric or antisymmetric under particle exchange? Which symmetry applies to bosons and which to fermions?
2. Write the two-particle antisymmetric state $\psi_A$ for fermions in single-particle states $\psi_a$ and $\psi_b$. Show explicitly that $\psi_A$ vanishes when $a = b$, thereby deriving the Pauli exclusion principle.
3. What is a Slater determinant, and how does it generalize the two-particle antisymmetric state to $N$ fermions?

**自测（空白页）**

1. 为什么全同粒子的波函数在粒子交换下必须是对称的或反对称的？哪种对称性对应玻色子，哪种对应费米子？
2. 写出费米子处于单粒子态 $\psi_a$ 和 $\psi_b$ 时的两粒子反对称态 $\psi_A$。明确证明当 $a = b$ 时 $\psi_A$ 为零，从而推导出泡利不相容原理。
3. 什么是斯莱特行列式？它如何将两粒子反对称态推广到 $N$ 个费米子的情形？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Identical particles are indistinguishable, so exchanging them leaves $|\psi|^2$ unchanged; the exchange operator has eigenvalue $\pm1$. Symmetric ($+$) states are bosons (integer spin), antisymmetric ($-$) are fermions (half-integer spin) — the spin-statistics connection. · 交换不改变 $|\psi|^2$,本征值 $\pm1$:对称为玻色子,反对称为费米子。

**2.** $\psi_A=\tfrac{1}{\sqrt2}[\psi_a(1)\psi_b(2)-\psi_a(2)\psi_b(1)]$. Setting $a=b$ gives $\psi_A=0$: two fermions cannot occupy the same single-particle state — the Pauli exclusion principle. · 令 $a=b$ 得 $\psi_A=0$,即泡利不相容。

**3.** A Slater determinant writes the $N$-fermion state as $\det[\psi_i(j)]/\sqrt{N!}$. Swapping two particles swaps two columns (sign flip ⟹ antisymmetry); two identical states give two equal rows ⟹ determinant $=0$ ⟹ Pauli. · 斯莱特行列式 $\det[\psi_i(j)]/\sqrt{N!}$ 自动反对称,两态相同则为零。

</details>

---

← Previous: [Module 3.4 — Quantum Mechanics in 3D](./module-3.4-quantum-mechanics-in-3d.md) · [Phase 3 index](./README.md) · Next: [Module 3.6 — Time-Independent Perturbation Theory](./module-3.6-time-independent-perturbation-theory.md) →

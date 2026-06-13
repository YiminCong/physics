# Module 3.4 — Quantum Mechanics in 3D (Angular Momentum, Hydrogen, Spin) ⭐
**模块 3.4 — 三维量子力学（角动量、氢原子、自旋）⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.4-derivations.md)

---

## 1. The 3D Schrödinger Equation & Angular Momentum · 三维薛定谔方程与角动量

**Definition.** In spherical coordinates the equation separates into radial and angular parts. The angular part is solved by **spherical harmonics** $Y_\ell^m(\theta,\phi)$, eigenfunctions of $\hat{L}^2$ (eigenvalue $\hbar^2\ell(\ell+1)$) and $\hat{L}_z$ (eigenvalue $m\hbar$).

**定义。** 在球坐标中，方程分离为径向部分和角向部分。角向部分由**球谐函数** $Y_\ell^m(\theta,\phi)$ 求解，它们是 $\hat{L}^2$（本征值 $\hbar^2\ell(\ell+1)$）和 $\hat{L}_z$（本征值 $m\hbar$）的本征函数。

## 2. Hydrogen & Spin · 氢原子与自旋

**Demonstration.**
- **Hydrogen atom** ($-e^2/r$ potential, the quantum central-force problem of Module 1.5): **$E_n = -13.6\ \text{eV} / n^2$**, with quantum numbers $n$ (energy), $\ell$ (orbital angular momentum), $m$ (orientation).
- **Spin-$\tfrac12$**: an intrinsic two-state angular momentum described by the Pauli matrices (Module 0.2); $S_z$ eigenvalues $\pm\hbar/2$ ("up"/"down").

**演示。**
- **氢原子**（$-e^2/r$ 势，模块 1.5 中的量子中心力问题）：**$E_n = -13.6\ \text{eV} / n^2$**，量子数 $n$（能量）、$\ell$（轨道角动量）、$m$（取向）。
- **自旋-$\tfrac12$**：一种本征的两态角动量，由泡利矩阵（模块 0.2）描述；$S_z$ 本征值 $\pm\hbar/2$（"上"/"下"）。

**Application.** Atomic structure and the periodic table; the angular-momentum machinery recurs everywhere; **spin is essential** for the Pauli principle (3.5) and the singlet structure of Cooper pairs (Phase 5).

**应用。** 原子结构与元素周期表；角动量机制在各处反复出现；**自旋对于**泡利不相容原理（3.5）和库珀对的单态结构（第 5 阶段）**至关重要**。

## Key results · 核心结果

- $\hat{L}^2$ eigenvalue $\hbar^2\ell(\ell+1)$, $\hat{L}_z$ eigenvalue $m\hbar$ — quantized angular momentum · 角动量量子化
- Hydrogen $E_n = -13.6\,\text{eV}/n^2$ · 氢原子能级
- Spin-$\tfrac12$ adds a two-state degree of freedom; state labels $(n,\ell,m,m_s)$ · 自旋与量子数
- Spherical harmonics $Y_\ell^m$ separate angular from radial physics · 球谐函数分离角向与径向

---

**Self-test (blank page)**

1. State the eigenvalue equations for $\hat{L}^2$ and $\hat{L}_z$ acting on the spherical harmonics $Y_\ell^m(\theta,\phi)$. What are the allowed values of $\ell$ and $m$?
2. Write the energy levels $E_n$ of the hydrogen atom and identify the three quantum numbers ($n$, $\ell$, $m$) and their allowed ranges.
3. Describe spin-$\tfrac12$: what are the eigenvalues of $\hat{S}_z$, and how are spin states represented using Pauli matrices?

**自测（空白页）**

1. 写出 $\hat{L}^2$ 和 $\hat{L}_z$ 作用于球谐函数 $Y_\ell^m(\theta,\phi)$ 的本征值方程，$\ell$ 和 $m$ 的允许取值是什么？
2. 写出氢原子的能级 $E_n$，并说明三个量子数 ($n$, $\ell$, $m$) 及其取值范围。
3. 描述自旋-$\tfrac12$：$\hat{S}_z$ 的本征值是什么？如何用泡利矩阵表示自旋态？

---

← Previous: [Module 3.3 — Formalism](./module-3.3-formalism.md) · [Phase 3 index](./README.md) · Next: [Module 3.5 — Identical Particles](./module-3.5-identical-particles.md) →

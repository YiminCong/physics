---
title: "Module 3.2 — Time-Independent Schrödinger Equation"
parent: "Phase 3 — Quantum Mechanics (the core)"
nav_order: 2
---

# Module 3.2 — Time-Independent Schrödinger Equation ⭐
**模块 3.2 — 定态薛定谔方程 ⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.2-derivations.md)

---

## 1. Stationary States · 定态

**Definition.** Separating variables $\psi(x,t) = \psi(x)e^{-iEt/\hbar}$ turns the Schrödinger equation into the **time-independent Schrödinger equation (TISE)** $\hat{H}\psi = E\psi$ — an eigenvalue problem (Module 0.2). Solutions $\psi_n$ are stationary states; general states are superpositions $\sum_n c_n \psi_n e^{-iE_n t/\hbar}$.

**定义。** 分离变量 $\psi(x,t) = \psi(x)e^{-iEt/\hbar}$ 将薛定谔方程转化为**定态薛定谔方程（TISE）** $\hat{H}\psi = E\psi$——一个本征值问题（模块 0.2）。解 $\psi_n$ 称为定态；一般态为叠加态 $\sum_n c_n \psi_n e^{-iE_n t/\hbar}$。

## 2. The Canonical Solvable Systems · 典型可解系统

**Demonstration.**
- **Infinite square well** (width $L$): $\psi_n = \sqrt{2/L}\,\sin(n\pi x/L)$, **$E_n = n^2\pi^2\hbar^2/(2mL^2)$** — energy is quantized by boundary conditions.
- **Harmonic oscillator**, solved with **ladder operators** $a = \sqrt{m\omega/2\hbar}\,(\hat{x} + i\hat{p}/m\omega)$ and $a^\dagger$: the spectrum is **$E_n = (n + \tfrac12)\hbar\omega$**, with $a^\dagger$ raising and $a$ lowering the state. Note the zero-point energy $\tfrac12\hbar\omega$.
- **Barrier**: a particle can **tunnel** through a region where $E < V$, with exponentially small transmission.

**演示。**
- **无限深方势阱**（宽度 $L$）：$\psi_n = \sqrt{2/L}\,\sin(n\pi x/L)$，**$E_n = n^2\pi^2\hbar^2/(2mL^2)$**——能量由边界条件量子化。
- **谐振子**，用**梯形算符** $a = \sqrt{m\omega/2\hbar}\,(\hat{x} + i\hat{p}/m\omega)$ 和 $a^\dagger$ 求解：能谱为 **$E_n = (n + \tfrac12)\hbar\omega$**，$a^\dagger$ 升态，$a$ 降态。注意零点能 $\tfrac12\hbar\omega$。
- **势垒**：粒子可以**隧穿**过 $E < V$ 的区域，透射率指数级小。

**Application.** The oscillator ladder operators reappear *verbatim* as phonon operators (Phase 4) and in the BCS Hamiltonian (Phase 5). Quantized levels and tunneling are the bread and butter of all that follows.

**应用。** 谐振子梯形算符*原封不动地*作为声子算符重现于第 4 阶段，并出现在 BCS 哈密顿量（第 5 阶段）中。量子化能级和隧穿效应是后续所有内容的基础。

---

**Self-test (blank page)**

1. Explain separation of variables for the Schrödinger equation: what form does $\psi(x,t)$ take, and what eigenvalue equation does the spatial part satisfy?
2. State the energy eigenvalues $E_n$ and normalized eigenfunctions $\psi_n$ for the infinite square well of width $L$.
3. Define the ladder operators $a$ and $a^\dagger$ for the harmonic oscillator and state the energy spectrum $E_n$. Why is the zero-point energy $\tfrac12\hbar\omega$ physically significant?
4. Describe quantum tunneling qualitatively: how can a particle penetrate a barrier where $E < V$, and what determines the transmission probability?

**自测（空白页）**

1. 解释薛定谔方程的分离变量法：$\psi(x,t)$ 取什么形式？空间部分满足什么本征值方程？
2. 写出宽度为 $L$ 的无限深方势阱的能量本征值 $E_n$ 和归一化本征函数 $\psi_n$。
3. 定义谐振子的梯形算符 $a$ 和 $a^\dagger$，并写出能谱 $E_n$。为什么零点能 $\tfrac12\hbar\omega$ 在物理上有重要意义？
4. 定性描述量子隧穿：粒子如何能穿透 $E < V$ 的势垒区域？什么决定透射概率？

---

← Previous: [Module 3.1 — The Wave Function](./module-3.1-the-wave-function.md) · [Phase 3 index](./README.md) · Next: [Module 3.3 — Formalism](./module-3.3-formalism.md) →

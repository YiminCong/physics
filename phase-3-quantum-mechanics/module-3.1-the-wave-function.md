---
title: "Module 3.1 — The Wave Function"
parent: "Phase 3 — Quantum Mechanics (the core)"
nav_order: 1
---

# Module 3.1 — The Wave Function
**模块 3.1 — 波函数**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.1-derivations.md)

---

## 1. State, the Born Rule & the Schrödinger Equation · 态、玻恩定则与薛定谔方程

**Definition.** A particle's state is a complex **wave function** $\psi(x,t)$. The **Born rule**: $|\psi(x,t)|^2$ is the probability *density* of finding the particle at $x$, so $\int|\psi|^2\,dx = 1$ (normalization). Evolution obeys the **Schrödinger equation** $i\hbar\,\partial\psi/\partial t = \hat{H}\psi$, with $\hat{H} = -(\hbar^2/2m)\partial^2/\partial x^2 + V(x)$. Operators: $\hat{x} = x$, $\hat{p} = -i\hbar\,\partial/\partial x$.

**定义。** 粒子的态是一个复数**波函数** $\psi(x,t)$。**玻恩定则**：$|\psi(x,t)|^2$ 是在 $x$ 处找到粒子的概率*密度*，因此 $\int|\psi|^2\,dx = 1$（归一化）。演化遵从**薛定谔方程** $i\hbar\,\partial\psi/\partial t = \hat{H}\psi$，其中 $\hat{H} = -(\hbar^2/2m)\partial^2/\partial x^2 + V(x)$。算符：$\hat{x} = x$，$\hat{p} = -i\hbar\,\partial/\partial x$。

## 2. Expectation Values & Uncertainty · 期望值与不确定性

**Definition.** $\langle Q\rangle = \int \psi^* \hat{Q} \psi\,dx$; spread $\Delta Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$.

**定义。** $\langle Q\rangle = \int \psi^* \hat{Q} \psi\,dx$；散布 $\Delta Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$。

**Demonstration.** For a Gaussian packet, the position/momentum integrals (Module 0.1) give $\Delta x\cdot\Delta p = \hbar/2$ — saturating the **Heisenberg uncertainty principle** $\Delta x\cdot\Delta p \geq \hbar/2$.

**演示。** 对于高斯波包，位置/动量积分（模块 0.1）给出 $\Delta x\cdot\Delta p = \hbar/2$——达到**海森堡不确定性原理** $\Delta x\cdot\Delta p \geq \hbar/2$ 的下限。

**Application.** The probabilistic layer of all QM; expectation/uncertainty are just the mean/variance of Module 0.5 applied to $|\psi|^2$.

**应用。** 所有量子力学的概率层；期望值/不确定性就是模块 0.5 中的均值/方差应用于 $|\psi|^2$。

---

**Self-test (blank page)**

1. State the Born rule: what physical quantity does $|\psi(x,t)|^2$ represent, and what normalization condition must $\psi$ satisfy?
2. Write down the time-dependent Schrödinger equation and identify the kinetic-energy and potential-energy terms in the Hamiltonian $\hat{H}$ for a particle in one dimension.
3. Define the expectation value $\langle Q\rangle$ of an observable $\hat{Q}$ and the associated uncertainty $\Delta Q$ in terms of $\psi$. Then state the Heisenberg uncertainty principle for position and momentum.

**自测（空白页）**

1. 陈述玻恩定则：$|\psi(x,t)|^2$ 代表什么物理量？波函数 $\psi$ 必须满足怎样的归一化条件？
2. 写出含时薛定谔方程，并指出一维粒子哈密顿量 $\hat{H}$ 中的动能项和势能项。
3. 用 $\psi$ 定义可观测量 $\hat{Q}$ 的期望值 $\langle Q\rangle$ 及其不确定度 $\Delta Q$，再陈述位置与动量的海森堡不确定性原理。

---

← Previous: [Module 3.0 — Old Quantum Theory & the Photoelectric Effect](./module-3.0-old-quantum-theory-and-photoelectric-effect.md) · [Phase 3 index](./README.md) · Next: [Module 3.2 — Time-Independent Schrödinger Equation](./module-3.2-time-independent-schrodinger-equation.md) →

# Module 3.7 — Variational & WKB Methods
**模块 3.7 — 变分法与 WKB 方法**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.7-derivations.md)

---

## 1. The Variational Principle · 变分原理

**Definition.** For *any* trial state $\psi_\text{trial}$, $\langle \hat{H} \rangle \geq E_\text{ground}$. Minimizing $\langle \hat{H} \rangle$ over adjustable parameters gives an upper-bound estimate of the ground-state energy.

**定义。** 对于*任意*试探态 $\psi_\text{trial}$，均有 $\langle \hat{H} \rangle \geq E_\text{ground}$。对可调参数最小化 $\langle \hat{H} \rangle$ 给出基态能量的上界估计。

**Demonstration.** A trial Gaussian for the helium ground state (or for a particle in an unfamiliar potential) yields a remarkably good energy estimate after minimizing over its width.

**演示。** 用高斯函数作为氦原子基态（或粒子在陌生势中）的试探态，对其宽度最小化后得到非常精确的能量估计。

## 2. The WKB Approximation · WKB 近似

**Definition.** For slowly varying potentials, $\psi \approx \exp[(i/\hbar)\int p(x)\,dx]$, a semiclassical form. It gives quantization conditions and **tunneling rates**: transmission $\propto \exp[-(2/\hbar)\int|p|\,dx]$ across a barrier.

**定义。** 对于缓慢变化的势，$\psi \approx \exp[(i/\hbar)\int p(x)\,dx]$，这是一种半经典形式。它给出量子化条件和**隧穿率**：穿越势垒的透射率 $\propto \exp[-(2/\hbar)\int|p|\,dx]$。

**Application.** Variational methods underlie quantum chemistry and trial-state approaches (including the BCS variational ground state, Phase 5). WKB tunneling explains $\alpha$ decay, scanning tunneling microscopy, and the tunneling that probes the superconducting gap (Phase 5).

**应用。** 变分法是量子化学和试探态方法的基础（包括 BCS 变分基态，第 5 阶段）。WKB 隧穿解释了 $\alpha$ 衰变、扫描隧道显微镜，以及探测超导能隙的隧道效应（第 5 阶段）。

## Key results · 核心结果

- Variational: $E_0\le\dfrac{\langle\psi|\hat H|\psi\rangle}{\langle\psi|\psi\rangle}$ for any trial $\psi$ · 变分原理
- Optimize the trial-function parameter to get the best bound · 优化试探参数
- WKB $\psi\sim p^{-1/2}\exp(\pm\tfrac{i}{\hbar}\int p\,dx)$ · WKB 近似
- Tunneling $T\sim\exp[-\tfrac{2}{\hbar}\int_a^b|p|\,dx]$ · 隧穿透射

---

**Self-test (blank page)**

1. State the variational principle as an inequality. Why does it provide an upper bound on the ground-state energy rather than an exact value?
2. Describe how to use a Gaussian trial wave function with an adjustable width parameter $\alpha$ to estimate the ground-state energy of a given potential. What is the optimization step?
3. Write the WKB form for the wave function and the tunneling transmission formula $T \propto \exp[-(2/\hbar)\int|p(x)|\,dx]$. Identify the integration limits and explain what determines the tunneling rate.

**自测（空白页）**

1. 以不等式形式陈述变分原理。为什么它给出的是基态能量的上界而非精确值？
2. 描述如何用含可调宽度参数 $\alpha$ 的高斯试探波函数估计给定势的基态能量，优化步骤是什么？
3. 写出 WKB 波函数形式和隧穿透射公式 $T \propto \exp[-(2/\hbar)\int|p(x)|\,dx]$，指出积分上下限，并解释什么决定隧穿率。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $E_0\le\langle\psi|\hat H|\psi\rangle/\langle\psi|\psi\rangle$ for any trial state. It is an upper bound because any trial $\psi$ is a superposition of the true eigenstates, and the excited states ($E>E_0$) only raise the average. · 任意试探态给上界。
**2.** Take a Gaussian $\psi_\alpha\propto e^{-\alpha x^2}$, compute $E(\alpha)=\langle\hat H\rangle$, then minimize: $dE/d\alpha=0$ gives the best width and the variational estimate. · 高斯试探,$dE/d\alpha=0$。
**3.** $\psi\sim p^{-1/2}\exp(\pm\tfrac{i}{\hbar}\int p\,dx)$; tunneling $T\sim\exp[-\tfrac{2}{\hbar}\int_a^b|p(x)|\,dx]$ between the classical turning points $a,b$ (where $E=V$). The rate is set by the barrier "area" $\int|p|\,dx$. · 积分限为经典转折点,速率由势垒面积决定。

</details>

---

← Previous: [Module 3.6 — Time-Independent Perturbation Theory](./module-3.6-time-independent-perturbation-theory.md) · [Phase 3 index](./README.md) · Next: [Module 3.8 — Time-Dependent Perturbation Theory & Scattering](./module-3.8-time-dependent-perturbation-theory-and-scattering.md) →

# Module 3.9 — Fundamental Concepts (Graduate, Sakurai)
**模块 3.9 — 基本概念（研究生，樱井）**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.9-derivations.md)

---

## 1. The Abstract Formalism · 抽象形式体系

**Definition.** Build QM from kets $|\alpha\rangle$, bras $\langle\alpha|$, and operators acting on an abstract state space — *before* choosing a representation. Measurement projects onto eigenkets; the position and momentum "wavefunctions" are just the components $\langle x|\psi\rangle$ and $\langle p|\psi\rangle$ in particular bases.

**定义。** 从右矢 $|\alpha\rangle$、左矢 $\langle\alpha|$ 以及作用于抽象态空间的算符出发构建量子力学——*在*选择表象*之前*。测量将态投影到本征右矢；位置和动量"波函数"只是在特定基下的分量 $\langle x|\psi\rangle$ 和 $\langle p|\psi\rangle$。

**Demonstration.** The Stern–Gerlach / spin-$\tfrac12$ system is the cleanest arena: base kets $|+\rangle$, $|-\rangle$, operators as $2\times 2$ matrices, and sequential measurements illustrate incompatibility directly.

**演示。** 斯特恩–盖拉赫 / 自旋-$\tfrac12$ 系统是最简洁的舞台：基右矢 $|+\rangle$、$|-\rangle$，算符以 $2\times 2$ 矩阵表示，序列测量直接展示不相容性。

**Application.** This basis-independent language is how serious QM and quantum field theory are written; it makes changes of representation (position ↔ momentum) trivial and prepares you for second quantization (3.12).

**应用。** 这种与基无关的语言是严格量子力学和量子场论的书写方式；它使表象变换（位置 ↔ 动量）变得平凡，并为二次量子化（3.12）做好准备。

## Key results · 核心结果

- Ket $|\psi\rangle$, dual bra $\langle\psi|$; inner product $\langle\varphi|\psi\rangle\in\mathbb C$ · 右矢、左矢与内积
- Wave function $\psi(x)=\langle x|\psi\rangle$ (components in the position basis) · 波函数为位置基分量
- Observables = Hermitian operators; non-commuting ones are incompatible · 可观测量为厄米算符
- Basis-independent formalism makes representation changes trivial · 基无关形式

---

**Self-test (blank page)**

1. Explain the bra–ket notation: what is the relationship between a ket $|\psi\rangle$, its dual bra $\langle\psi|$, and the inner product $\langle\varphi|\psi\rangle$? How do position-space wave functions emerge from this abstract formalism?
2. Using the spin-$\tfrac12$ system as an example, show how a measurement in sequence (first along $z$, then along $x$) illustrates the incompatibility of non-commuting observables.
3. Why is the abstract, basis-independent formulation of QM preferable to working directly with wave functions when changing representations? Give a specific example of a representation change.

**自测（空白页）**

1. 解释右矢–左矢符号：右矢 $|\psi\rangle$、其对偶左矢 $\langle\psi|$ 与内积 $\langle\varphi|\psi\rangle$ 之间的关系是什么？位置空间波函数如何从这一抽象形式体系中得到？
2. 以自旋-$\tfrac12$ 系统为例，说明序列测量（先沿 $z$ 轴，再沿 $x$ 轴）如何展示不对易可观测量的不相容性。
3. 为什么在表象变换时抽象的、与基无关的量子力学表述优于直接使用波函数？请给出一个具体的表象变换例子。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** The bra $\langle\psi|$ is the dual (conjugate transpose) of the ket $|\psi\rangle$; $\langle\varphi|\psi\rangle$ is their inner product (a complex number). Wave functions are components in the position basis, $\psi(x)=\langle x|\psi\rangle$. · 左矢为右矢对偶;$\psi(x)=\langle x|\psi\rangle$。
**2.** Measure $S_z$ → collapse to $|\!\uparrow\rangle=(|\!\rightarrow\rangle+|\!\leftarrow\rangle)/\sqrt2$; a subsequent $S_x$ measurement gives 50/50, and re-measuring $S_z$ is again random — because $[S_z,S_x]\neq0$. · 非对易可观测量相互干扰。
**3.** The abstract formulation makes basis changes trivial: the same $|\psi\rangle$ is $\langle x|\psi\rangle=\psi(x)$ in position space and $\langle p|\psi\rangle=\tilde\psi(p)$ in momentum space, related by a Fourier transform. · 基无关,位置↔动量由傅里叶变换联系。

</details>

---

← Previous: [Module 3.8 — Time-Dependent Perturbation Theory & Scattering](./module-3.8-time-dependent-perturbation-theory-and-scattering.md) · [Phase 3 index](./README.md) · Next: [Module 3.10 — Quantum Dynamics](./module-3.10-quantum-dynamics.md) →

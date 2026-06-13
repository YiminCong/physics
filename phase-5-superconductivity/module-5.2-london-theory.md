# Module 5.2 — London Theory ⭐
**模块 5.2 — 伦敦理论 ⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.2-london-theory-derivations.md)

---

## 1. Electrodynamics of the Superconductor · 超导体的电动力学

**Definition.** The **London equations** replace Ohm's law inside a superconductor, relating supercurrent directly to the fields. Their key consequence is that magnetic field cannot penetrate deeply.

**定义。** **伦敦方程**在超导体内部取代了欧姆定律，将超电流直接与磁场联系起来。其关键推论是磁场无法深入穿透超导体。

**Demonstration.** Combining the second London equation with Ampère's law gives $\nabla^2 \mathbf{B} = \mathbf{B}/\lambda_L^2$, whose solution is $\mathbf{B}(x) = \mathbf{B}_0\, e^{-x/\lambda_L}$ — the field decays exponentially over the **London penetration depth** $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$, where $n_s$ is the superconducting electron density.

**演示。** 将第二伦敦方程与安培定律联立，得到 $\nabla^2 \mathbf{B} = \mathbf{B}/\lambda_L^2$，其解为 $\mathbf{B}(x) = \mathbf{B}_0\, e^{-x/\lambda_L}$——磁场在**伦敦穿透深度** $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$ 的尺度上指数衰减，其中 $n_s$ 为超导电子密度。

**Application.** This is the quantitative Meissner effect: field is excluded except within a thin surface layer of thickness $\lambda$. $\lambda$ is one of the **two fundamental length scales** of superconductivity (the other is the coherence length, next module).

**应用。** 这是迈斯纳效应的定量描述：磁场被排斥在厚度为 $\lambda$ 的薄表面层之外。$\lambda$ 是超导性的**两个基本长度尺度**之一（另一个是相干长度，见下一模块）。

## Key results · 核心结果

- $\nabla^2\mathbf{B} = \mathbf{B}/\lambda_L^2$ ⟹ $\mathbf{B}(x) = \mathbf{B}_0\,e^{-x/\lambda_L}$ — the Meissner effect · 迈斯纳效应
- $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$ — London penetration depth · 伦敦穿透深度
- The field is expelled; superconductivity is more than perfect conductivity · 磁场被排出,超导不只是完美导电
- A phenomenological warm-up for Ginzburg–Landau (5.3) · 金兹堡–朗道的唯象前奏

---

**Self-test (blank page)**

1. Write the solution $B(x) = B_0\, e^{-x/\lambda_L}$ for the magnetic field inside a superconductor and state the formula for the London penetration depth $\lambda_L$ in terms of the superconducting carrier density $n_s$, mass $m$, and charge $e$.
2. Derive qualitatively how the second London equation combined with Ampère's law leads to $\nabla^2 B = B/\lambda_L^2$. What does this tell you about how magnetic field behaves inside the bulk?
3. How does $\lambda_L$ depend on temperature as $T \to T_c$? What happens to the Meissner effect as you approach the transition?
4. $\lambda_L$ is one of the two fundamental length scales of superconductivity. Name the other, state what physical length it characterises, and explain why their ratio determines the type of superconductor.

**自测（空白页）**

1. 写出超导体内磁场的解 $B(x) = B_0\, e^{-x/\lambda_L}$，并写出伦敦穿透深度 $\lambda_L$ 关于超导载流子密度 $n_s$、质量 $m$ 和电荷 $e$ 的表达式。
2. 定性推导第二伦敦方程与安培定律联立如何给出 $\nabla^2 B = B/\lambda_L^2$。这告诉我们磁场在超导体内部如何变化？
3. 当 $T \to T_c$ 时 $\lambda_L$ 如何随温度变化？趋近转变温度时迈斯纳效应发生什么变化？
4. $\lambda_L$ 是超导性的两个基本长度尺度之一。写出另一个，说明它描述什么物理长度，并解释二者之比如何决定超导体的类型。

---

← Previous: [Module 5.1 — Phenomenology](./module-5.1-phenomenology.md) · [Phase 5 index](./README.md) · Next: [Module 5.3 — Ginzburg–Landau Theory](./module-5.3-ginzburg-landau-theory.md) →

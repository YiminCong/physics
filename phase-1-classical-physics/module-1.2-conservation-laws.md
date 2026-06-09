---
title: "Module 1.2 — Conservation Laws"
parent: "Phase 1 — Classical Physics"
nav_order: 2
---

# Module 1.2 — Conservation Laws
**模块 1.2 — 守恒定律**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.2-conservation-laws-derivations.md)

---

## 1. Energy: Work–Energy Theorem and Potential Energy · 能量：功能定理与势能

**Definition.** The **work** done by a force $\mathbf{F}$ along a path is $W = \int \mathbf{F} \cdot d\mathbf{r}$. The **work–energy theorem** states that the net work equals the change in kinetic energy: $W_\text{net} = \Delta KE = \Delta(\tfrac12 m v^2)$. A force is **conservative** if the work it does is path-independent, equivalently if $\nabla \times \mathbf{F} = 0$. For conservative forces one defines a **potential energy** $V$ such that $\mathbf{F} = -\nabla V$; the **total mechanical energy** $E = \tfrac12 m v^2 + V$ is then constant: $dE/dt = 0$.

**定义。** 力 $\mathbf{F}$ 沿路径所做的**功**为 $W = \int \mathbf{F} \cdot d\mathbf{r}$。**功能定理**指出，合力做的净功等于动能的变化：$W_\text{net} = \Delta KE = \Delta(\tfrac12 m v^2)$。若一个力所做的功与路径无关（等价地，$\nabla \times \mathbf{F} = 0$），则称该力为**保守力**。对于保守力，可定义**势能** $V$ 使得 $\mathbf{F} = -\nabla V$；此时**总机械能** $E = \tfrac12 m v^2 + V$ 为常数：$dE/dt = 0$。

**Demonstration.** For a mass on a spring ($F = -kx$, $V = \tfrac12 k x^2$), energy conservation gives $\tfrac12 m v^2 + \tfrac12 k x^2 = \text{const}$. Maximising kinetic energy (at $x = 0$) and potential energy (at maximum displacement $A$) yields $v_\text{max} = A\sqrt{k/m} = A\omega$, the familiar result for simple harmonic motion.

**演示。** 对于弹簧上的质量（$F = -kx$，$V = \tfrac12 k x^2$），能量守恒给出 $\tfrac12 m v^2 + \tfrac12 k x^2 = \text{常数}$。在 $x = 0$ 处动能最大，在最大位移 $A$ 处势能最大，从而得到 $v_\text{max} = A\sqrt{k/m} = A\omega$，即简谐运动的熟知结果。

**Application.** Energy methods often bypass solving the full ODE. Knowing $V(x)$, one can read off turning points ($V = E$), classifying bound vs. unbound orbits without integrating the equation of motion. This potential-landscape thinking recurs throughout quantum mechanics (Module 3.2) and field theory.

**应用。** 能量方法往往可以绕过求解完整的常微分方程。已知 $V(x)$，便可直接读出转折点（$V = E$），无需积分运动方程即可区分束缚轨道与非束缚轨道。这种势能图景的思维在量子力学（模块 3.2）和场论中反复出现。

## 2. Linear Momentum, Angular Momentum, and Collisions · 线动量、角动量与碰撞

**Definition.** **Linear momentum** $\mathbf{p} = m\mathbf{v}$ is conserved whenever the net external force is zero ($\mathbf{F}_\text{ext} = d\mathbf{p}/dt$). **Angular momentum** about an origin is $\mathbf{L} = \mathbf{r} \times \mathbf{p}$; it is conserved when the net external torque $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ vanishes — for example in any central-force problem. In a **collision**, total momentum is always conserved (assuming negligible external forces during impact); kinetic energy is also conserved only in elastic collisions.

**定义。** 当合外力为零时（$\mathbf{F}_\text{ext} = d\mathbf{p}/dt$），**线动量** $\mathbf{p} = m\mathbf{v}$ 守恒。关于某点的**角动量**为 $\mathbf{L} = \mathbf{r} \times \mathbf{p}$；当合外力矩 $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ 为零时守恒——例如任何有心力问题中均如此。在**碰撞**中，总动量始终守恒（假设碰撞期间外力可忽略）；只有弹性碰撞中动能也守恒。

**Demonstration.** In a 1D elastic collision between mass $m_1$ (velocity $u_1$) and stationary $m_2$, conservation of momentum and kinetic energy gives $v_1 = (m_1 - m_2)/(m_1 + m_2)\, u_1$ and $v_2 = 2m_1/(m_1 + m_2)\, u_1$. The special case $m_1 = m_2$ yields complete velocity exchange — billiard-ball behaviour.

**演示。** 在质量 $m_1$（速度 $u_1$）与静止质量 $m_2$ 的一维弹性碰撞中，动量守恒和动能守恒给出 $v_1 = (m_1 - m_2)/(m_1 + m_2)\, u_1$ 和 $v_2 = 2m_1/(m_1 + m_2)\, u_1$。特殊情形 $m_1 = m_2$ 产生完全速度交换——台球行为。

**Application.** Conserved quantities are far more fundamental than the forces that produce them: each conservation law reflects a symmetry of nature. This is made precise by **Noether's theorem** (Module 1.4): time-translation symmetry → energy conservation, spatial-translation symmetry → momentum conservation, rotational symmetry → angular momentum conservation. The pattern of symmetries and conservation laws organises all of modern physics through gauge theory (Phase 8).

**应用。** 守恒量比产生它们的力要基本得多：每条守恒定律都反映了自然界的一种对称性。这一点由**诺特定理**（模块 1.4）精确阐述：时间平移对称性 → 能量守恒，空间平移对称性 → 动量守恒，旋转对称性 → 角动量守恒。对称性与守恒定律的规律通过规范理论（第 8 阶段）组织了整个现代物理学。

---

**Self-test (blank page)**

1. A 2 kg block slides from rest down a frictionless curved ramp of height h = 5 m. What is its speed at the bottom?
2. Derive the velocity of the centre of mass of a two-body system and show it moves uniformly if no external forces act.
3. A 3 kg ball moving at 4 m/s collides elastically head-on with a 1 kg ball at rest. Find both final velocities.
4. Why is angular momentum conserved for a planet orbiting the Sun? Use this to derive Kepler's second law (equal areas in equal times).

**自测（空白页）**

1. 一个 2 kg 的滑块从高度 h = 5 m 的无摩擦弯曲坡道上从静止开始下滑。求其到达底部时的速度。
2. 推导两体系统质心的速度，并证明在无外力作用时质心匀速运动。
3. 一个 3 kg 的球以 4 m/s 速度与静止的 1 kg 球发生弹性正碰。求两球的末速度。
4. 为什么行星绕太阳运动时角动量守恒？利用此推导开普勒第二定律（等面积定律）。

---

← Previous: [Module 1.1 — Newtonian Mechanics](./module-1.1-newtonian-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.3 — Lagrangian Mechanics & the Variational Principle](./module-1.3-lagrangian-mechanics.md) →

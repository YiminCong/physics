# Module 1.17 — Fluid Mechanics
**模块 1.17 — 流体力学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.17-fluid-mechanics-derivations.md)

---

## 1. Ideal Fluids: Continuity, Euler & Bernoulli · 理想流体：连续方程、欧拉方程与伯努利定理

**Definition.** A **fluid** is a continuous medium described by fields: density $\rho(\mathbf{r},t)$, pressure $P(\mathbf{r},t)$, and velocity $\mathbf{v}(\mathbf{r},t)$. Mass conservation is the **continuity equation** $\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{v}) = 0$. For an ideal (inviscid) fluid, Newton's second law per unit volume is **Euler's equation** $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \rho\mathbf{g}$.

**定义。** **流体**是由场描述的连续介质：密度 $\rho(\mathbf{r},t)$、压强 $P(\mathbf{r},t)$ 和速度 $\mathbf{v}(\mathbf{r},t)$。质量守恒是**连续性方程** $\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{v}) = 0$。对于理想（无粘）流体，单位体积的牛顿第二定律是**欧拉方程** $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \rho\mathbf{g}$。

**Demonstration.** For steady, incompressible, irrotational flow, integrating Euler's equation along a streamline gives **Bernoulli's theorem** $P + \tfrac12\rho v^2 + \rho g h = \text{constant}$ — faster flow means lower pressure. This explains lift on a wing, the lift in a Venturi tube, and why a shower curtain billows inward.

**演示。** 对于定常、不可压缩、无旋流动，沿流线积分欧拉方程给出**伯努利定理** $P + \tfrac12\rho v^2 + \rho g h = \text{常数}$——流速越快压强越低。这解释了机翼的升力、文丘里管中的升力，以及为什么浴帘会向内鼓起。

**Application.** The continuity equation is the prototype **conservation law** (Module 1.2) in field form, reused for charge (Module 1.10) and probability (Module 3.1). The nonlinear convective term $(\mathbf{v}\cdot\nabla)\mathbf{v}$ is the seed of turbulence (below) and the source of much of the difficulty in physics.

**应用。** 连续性方程是场形式的原型**守恒定律**（模块 1.2），在电荷（模块 1.10）和概率（模块 3.1）中重复使用。非线性对流项 $(\mathbf{v}\cdot\nabla)\mathbf{v}$ 是湍流（见下）的种子，也是物理学中许多困难的根源。

## 2. Viscosity, the Navier–Stokes Equation & Turbulence · 粘性、纳维–斯托克斯方程与湍流

**Definition.** A real fluid resists shear through **viscosity** $\eta$. Adding the viscous force $\eta\nabla^2\mathbf{v}$ to Euler's equation gives the **Navier–Stokes equation** $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \eta\nabla^2\mathbf{v} + \rho\mathbf{g}$ — the master equation of fluid dynamics. The dimensionless **Reynolds number** $\mathrm{Re} = \rho v L/\eta$ measures the ratio of inertial to viscous forces.

**定义。** 真实流体通过**粘度** $\eta$ 抵抗剪切。在欧拉方程中加入粘性力 $\eta\nabla^2\mathbf{v}$，得到**纳维–斯托克斯方程** $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \eta\nabla^2\mathbf{v} + \rho\mathbf{g}$——流体动力学的主方程。无量纲的**雷诺数** $\mathrm{Re} = \rho v L/\eta$ 衡量惯性力与粘性力之比。

**Demonstration.** At low $\mathrm{Re}$ ($\ll 1$) viscous forces dominate: smooth **laminar** flow, e.g. Poiseuille flow in a pipe with a parabolic velocity profile. At high $\mathrm{Re}$ the nonlinear term dominates and the flow becomes **turbulent** — chaotic, eddying, and effectively unpredictable in detail (a manifestation of the chaos of Module 1.19). **Vorticity** $\boldsymbol{\omega} = \nabla\times\mathbf{v}$ quantifies local rotation.

**演示。** 在低雷诺数（$\ll 1$）时粘性力主导：平滑的**层流**，例如管内具有抛物线速度剖面的泊肃叶流。在高雷诺数时非线性项主导，流动变为**湍流**——混沌、涡旋，细节实际上不可预测（模块 1.19 混沌的表现）。**涡度** $\boldsymbol{\omega} = \nabla\times\mathbf{v}$ 量化局部旋转。

**Application.** Navier–Stokes governs weather, ocean currents, blood flow, aerodynamics, and plasma. Whether its 3D solutions always remain smooth is an unsolved Clay Millennium Problem. Fluid ideas also reappear as analogies in physics: the **superfluid** and the dissipationless flow of a superconductor (Phase 5) are quantum fluids whose flow is constrained by a macroscopic phase.

**应用。** 纳维–斯托克斯方程支配天气、洋流、血流、空气动力学和等离子体。其三维解是否始终保持光滑是一个未解决的克雷千禧年大奖问题。流体思想在物理学中也作为类比重现：**超流体**和超导体的无耗散流动（第 5 阶段）是量子流体，其流动受宏观相位约束。

---

**Self-test (blank page)**

1. Derive the continuity equation from conservation of mass in a fixed control volume.
2. Use Bernoulli's theorem to estimate the lift pressure difference across a wing given top/bottom speeds.
3. What does the Reynolds number compare? Estimate $\mathrm{Re}$ for water flowing at 1 m/s through a 1 cm pipe ($\eta/\rho \approx 10^{-6}$ m$^2$/s).
4. Identify the single term in Navier–Stokes responsible for turbulence and explain why it makes the equation nonlinear.

**自测（空白页）**

1. 从固定控制体积中的质量守恒推导连续性方程。
2. 已知机翼上下表面速度，用伯努利定理估算升力压差。
3. 雷诺数比较什么？估算水以 1 m/s 流过直径 1 cm 管道时的 $\mathrm{Re}$（$\eta/\rho \approx 10^{-6}$ m$^2$/s）。
4. 指出纳维–斯托克斯方程中引起湍流的那一项，并解释为什么它使方程非线性。

---

← Previous: [Module 1.16 — Mechanical Waves & Acoustics](./module-1.16-mechanical-waves-acoustics.md) · [Phase 1 index](./README.md) · Next: [Module 1.18 — Continuum Mechanics & Elasticity](./module-1.18-continuum-mechanics-elasticity.md) →

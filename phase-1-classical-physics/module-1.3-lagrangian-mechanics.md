# Module 1.3 — Lagrangian Mechanics & the Variational Principle ⭐
**模块 1.3 — 拉格朗日力学与变分原理 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.3-lagrangian-mechanics-derivations.md)

---

## 1. The Principle of Least Action and Euler–Lagrange Equations · 最小作用量原理与欧拉–拉格朗日方程

**Definition.** Choose any set of **generalised coordinates** q_i that uniquely specify the configuration of a system (they need not be Cartesian). Define the **Lagrangian** L(q, q̇, t) = T − V, where T is kinetic and V is potential energy. The **action** is the functional S[q] = ∫ L(q, q̇, t) dt integrated over the time interval [t₁, t₂]. The **principle of least action** (Hamilton's principle) asserts that the physical trajectory is the one for which S is stationary under all variations δq that vanish at the endpoints: δS = 0. Applying the calculus of variations (Module 0.1) yields one **Euler–Lagrange equation** per generalised coordinate:

**定义。** 选取任意一组**广义坐标** q_i 以唯一描述系统的构型（无需为笛卡尔坐标）。定义**拉格朗日量** L(q, q̇, t) = T − V，其中 T 为动能，V 为势能。**作用量**是在时间区间 [t₁, t₂] 上对泛函 S[q] = ∫ L(q, q̇, t) dt 的积分。**最小作用量原理**（哈密顿原理）断言，物理轨迹是在端点处变分 δq 为零的所有变分中使 S 取驻值的那条：δS = 0。应用变分法（模块 0.1）对每个广义坐标给出一个**欧拉–拉格朗日方程**：

d/dt (∂L/∂q̇_i) − ∂L/∂q_i = 0.

A coordinate q_i that does not appear explicitly in L is **cyclic**; its conjugate momentum p_i = ∂L/∂q̇_i is then automatically conserved.

若坐标 q_i 不显含于 L 中，则称其为**循环坐标**；其共轭动量 p_i = ∂L/∂q̇_i 自动守恒。

**Demonstration.** A simple pendulum of length ℓ: choose θ as the single generalised coordinate. T = ½mℓ²θ̇², V = mgℓ(1 − cos θ), so L = ½mℓ²θ̇² − mgℓ(1 − cos θ). The Euler–Lagrange equation gives ℓθ̈ + g sin θ = 0, the exact pendulum equation, with no need to decompose tension into components.

**演示。** 长为 ℓ 的单摆：选 θ 为唯一广义坐标。T = ½mℓ²θ̇²，V = mgℓ(1 − cos θ)，故 L = ½mℓ²θ̇² − mgℓ(1 − cos θ)。欧拉–拉格朗日方程给出 ℓθ̈ + g sin θ = 0，即精确的单摆方程，无需将张力分解为分量。

**Application.** The Lagrangian formalism handles constrained systems and curvilinear coordinates elegantly — constraint forces never appear. The variational idea itself is the unifying thread across physics: the QM variational method (Module 3.7) minimises the energy functional; Ginzburg–Landau theory (Module 5.3) minimises a free-energy functional; and the path integral (Modules 3.10, 6.4) is a sum over all paths, each weighted by e^{iS/ℏ}, with the classical trajectory recovered as the stationary phase.

**应用。** 拉格朗日形式体系优雅地处理受约束系统和曲线坐标——约束力从不出现。变分思想本身是贯穿物理学的统一线索：量子力学变分方法（模块 3.7）最小化能量泛函；金兹堡–朗道理论（模块 5.3）最小化自由能泛函；路径积分（模块 3.10、6.4）是对所有路径的求和，每条路径权重为 e^{iS/ℏ}，经典轨迹在驻相近似下得以恢复。

## 2. Generalised Coordinates and Constraints · 广义坐标与约束

**Definition.** For a system with N particles in 3D and k holonomic constraints, the number of degrees of freedom is n = 3N − k. Generalised coordinates q_1, …, q_n parametrise the **configuration space** exactly, automatically satisfying all constraints. **Generalised forces** Q_i = Σ_α F_α · ∂r_α/∂q_i appear in the equations of motion if non-conservative forces are present.

**定义。** 对于三维空间中有 N 个粒子和 k 个完整约束的系统，自由度数为 n = 3N − k。广义坐标 q_1, …, q_n 精确参数化**构型空间**，自动满足所有约束。若存在非保守力，**广义力** Q_i = Σ_α F_α · ∂r_α/∂q_i 出现在运动方程中。

**Demonstration.** Two masses on a rod constrained to move on a frictionless horizontal surface — choosing the rod angle and centre-of-mass position as generalised coordinates reduces 4 Cartesian equations plus 2 constraint equations to 2 clean Euler–Lagrange equations.

**演示。** 约束在无摩擦水平面上运动的杆上两个质点——选取杆的角度和质心位置作为广义坐标，将 4 个笛卡尔方程加 2 个约束方程化简为 2 个简洁的欧拉–拉格朗日方程。

**Application.** This coordinate freedom becomes indispensable in the central-force problem (Module 1.5) where polar coordinates reduce a 2D problem to 1D, and in rigid-body dynamics (Module 1.7) where Euler angles are the natural generalised coordinates.

**应用。** 这种坐标自由度在有心力问题（模块 1.5）中不可或缺——极坐标将二维问题化为一维；在刚体动力学（模块 1.7）中，欧拉角是自然的广义坐标。

---

**Self-test (blank page)**

1. Write down the Lagrangian for a particle of mass m moving in a 2D central potential V(r) using polar coordinates (r, φ). Identify the cyclic coordinate and state the conserved quantity.
2. Derive the Euler–Lagrange equation for a mass m on a spring (V = ½kx²) and confirm you recover F = ma.
3. What does it mean for the action to be "stationary"? Why is "least action" a slight misnomer?
4. How does the Lagrangian method handle a bead constrained to move on a wire, compared with Newton's approach?

**自测（空白页）**

1. 用极坐标 (r, φ) 写出质量为 m 的粒子在二维有心势 V(r) 中运动的拉格朗日量。辨识循环坐标并陈述对应的守恒量。
2. 推导弹簧上质量为 m 的质点（V = ½kx²）的欧拉–拉格朗日方程，并确认能够恢复 F = ma。
3. 作用量"取驻值"是什么意思？为什么"最小作用量"这一说法略有误导？
4. 与牛顿方法相比，拉格朗日方法如何处理约束在导线上运动的珠子？

---

← Previous: [Module 1.2 — Conservation Laws](./module-1.2-conservation-laws.md) · [Phase 1 index](./README.md) · Next: [Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem](./module-1.4-hamiltonian-mechanics-noether.md) →

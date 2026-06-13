# Module 1.3 — Lagrangian Mechanics & the Variational Principle ⭐
**模块 1.3 — 拉格朗日力学与变分原理 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.3-lagrangian-mechanics-derivations.md)

---

## 1. The Principle of Least Action and Euler–Lagrange Equations · 最小作用量原理与欧拉–拉格朗日方程

**Definition.** Choose any set of **generalised coordinates** $q_i$ that uniquely specify the configuration of a system (they need not be Cartesian). Define the **Lagrangian** $L(q, \dot{q}, t) = T - V$, where $T$ is kinetic and $V$ is potential energy. The **action** is the functional $S[q] = \int L(q, \dot{q}, t)\, dt$ integrated over the time interval $[t_1, t_2]$. The **principle of least action** (Hamilton's principle) asserts that the physical trajectory is the one for which $S$ is stationary under all variations $\delta q$ that vanish at the endpoints: $\delta S = 0$. Applying the calculus of variations (Module 0.1) yields one **Euler–Lagrange equation** per generalised coordinate:

**定义。** 选取任意一组**广义坐标** $q_i$ 以唯一描述系统的构型（无需为笛卡尔坐标）。定义**拉格朗日量** $L(q, \dot{q}, t) = T - V$，其中 $T$ 为动能，$V$ 为势能。**作用量**是在时间区间 $[t_1, t_2]$ 上对泛函 $S[q] = \int L(q, \dot{q}, t)\, dt$ 的积分。**最小作用量原理**（哈密顿原理）断言，物理轨迹是在端点处变分 $\delta q$ 为零的所有变分中使 $S$ 取驻值的那条：$\delta S = 0$。应用变分法（模块 0.1）对每个广义坐标给出一个**欧拉–拉格朗日方程**：

$$ \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = 0. $$

A coordinate $q_i$ that does not appear explicitly in $L$ is **cyclic**; its conjugate momentum $p_i = \partial L/\partial \dot{q}_i$ is then automatically conserved.

若坐标 $q_i$ 不显含于 $L$ 中，则称其为**循环坐标**；其共轭动量 $p_i = \partial L/\partial \dot{q}_i$ 自动守恒。

**Demonstration.** A simple pendulum of length $\ell$: choose $\theta$ as the single generalised coordinate. $T = \tfrac12 m\ell^2\dot{\theta}^2$, $V = mg\ell(1 - \cos\theta)$, so $L = \tfrac12 m\ell^2\dot{\theta}^2 - mg\ell(1 - \cos\theta)$. The Euler–Lagrange equation gives $\ell\ddot{\theta} + g\sin\theta = 0$, the exact pendulum equation, with no need to decompose tension into components.

**演示。** 长为 $\ell$ 的单摆：选 $\theta$ 为唯一广义坐标。$T = \tfrac12 m\ell^2\dot{\theta}^2$，$V = mg\ell(1 - \cos\theta)$，故 $L = \tfrac12 m\ell^2\dot{\theta}^2 - mg\ell(1 - \cos\theta)$。欧拉–拉格朗日方程给出 $\ell\ddot{\theta} + g\sin\theta = 0$，即精确的单摆方程，无需将张力分解为分量。

**Application.** The Lagrangian formalism handles constrained systems and curvilinear coordinates elegantly — constraint forces never appear. The variational idea itself is the unifying thread across physics: the QM variational method (Module 3.7) minimises the energy functional; Ginzburg–Landau theory (Module 5.3) minimises a free-energy functional; and the path integral (Modules 3.10, 6.4) is a sum over all paths, each weighted by $e^{iS/\hbar}$, with the classical trajectory recovered as the stationary phase.

**应用。** 拉格朗日形式体系优雅地处理受约束系统和曲线坐标——约束力从不出现。变分思想本身是贯穿物理学的统一线索：量子力学变分方法（模块 3.7）最小化能量泛函；金兹堡–朗道理论（模块 5.3）最小化自由能泛函；路径积分（模块 3.10、6.4）是对所有路径的求和，每条路径权重为 $e^{iS/\hbar}$，经典轨迹在驻相近似下得以恢复。

## 2. Generalised Coordinates and Constraints · 广义坐标与约束

**Definition.** For a system with $N$ particles in 3D and $k$ holonomic constraints, the number of degrees of freedom is $n = 3N - k$. Generalised coordinates $q_1, \ldots, q_n$ parametrise the **configuration space** exactly, automatically satisfying all constraints. **Generalised forces** $Q_i = \sum_\alpha \mathbf{F}_\alpha \cdot \partial\mathbf{r}_\alpha/\partial q_i$ appear in the equations of motion if non-conservative forces are present.

**定义。** 对于三维空间中有 $N$ 个粒子和 $k$ 个完整约束的系统，自由度数为 $n = 3N - k$。广义坐标 $q_1, \ldots, q_n$ 精确参数化**构型空间**，自动满足所有约束。若存在非保守力，**广义力** $Q_i = \sum_\alpha \mathbf{F}_\alpha \cdot \partial\mathbf{r}_\alpha/\partial q_i$ 出现在运动方程中。

**Demonstration.** Two masses on a rod constrained to move on a frictionless horizontal surface — choosing the rod angle and centre-of-mass position as generalised coordinates reduces 4 Cartesian equations plus 2 constraint equations to 2 clean Euler–Lagrange equations.

**演示。** 约束在无摩擦水平面上运动的杆上两个质点——选取杆的角度和质心位置作为广义坐标，将 4 个笛卡尔方程加 2 个约束方程化简为 2 个简洁的欧拉–拉格朗日方程。

**Application.** This coordinate freedom becomes indispensable in the central-force problem (Module 1.5) where polar coordinates reduce a 2D problem to 1D, and in rigid-body dynamics (Module 1.7) where Euler angles are the natural generalised coordinates.

**应用。** 这种坐标自由度在有心力问题（模块 1.5）中不可或缺——极坐标将二维问题化为一维；在刚体动力学（模块 1.7）中，欧拉角是自然的广义坐标。

## Key results · 核心结果

- $S = \int L\, dt$, $L = T - V$; $\delta S = 0$ — principle of least action · 最小作用量原理
- $\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial \dot q_i}\right) - \dfrac{\partial L}{\partial q_i} = 0$ — Euler–Lagrange equations · 欧拉–拉格朗日方程
- Generalized coordinates handle constraints automatically · 广义坐标自动处理约束
- The action principle recurs everywhere: QM path integrals, field theory, GR · 作用量原理贯穿路径积分、场论、广义相对论

---

**Self-test (blank page)**

1. Write down the Lagrangian for a particle of mass $m$ moving in a 2D central potential $V(r)$ using polar coordinates $(r, \phi)$. Identify the cyclic coordinate and state the conserved quantity.
2. Derive the Euler–Lagrange equation for a mass $m$ on a spring ($V = \tfrac12 kx^2$) and confirm you recover $F = ma$.
3. What does it mean for the action to be "stationary"? Why is "least action" a slight misnomer?
4. How does the Lagrangian method handle a bead constrained to move on a wire, compared with Newton's approach?

**自测（空白页）**

1. 用极坐标 $(r, \phi)$ 写出质量为 $m$ 的粒子在二维有心势 $V(r)$ 中运动的拉格朗日量。辨识循环坐标并陈述对应的守恒量。
2. 推导弹簧上质量为 $m$ 的质点（$V = \tfrac12 kx^2$）的欧拉–拉格朗日方程，并确认能够恢复 $F = ma$。
3. 作用量"取驻值"是什么意思？为什么"最小作用量"这一说法略有误导？
4. 与牛顿方法相比，拉格朗日方法如何处理约束在导线上运动的珠子？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $L=\tfrac12 m(\dot r^2+r^2\dot\phi^2)-V(r)$. $\phi$ is cyclic ($\partial L/\partial\phi=0$), so $p_\phi=mr^2\dot\phi$ — the angular momentum — is conserved. · $\phi$ 为循环坐标,角动量 $mr^2\dot\phi$ 守恒。

**2.** $L=\tfrac12 m\dot x^2-\tfrac12 kx^2$; Euler–Lagrange $\tfrac{d}{dt}(m\dot x)+kx=0\Rightarrow m\ddot x=-kx=F$. ✓ · 回到 $m\ddot x=-kx=F$。

**3.** "Stationary" means $\delta S=0$ to first order — the action is an extremum *or* saddle, not necessarily a minimum, so "least action" is a slight misnomer. · 平稳即 $\delta S=0$(极值/鞍点),「最小」是不严格的说法。

**4.** Generalized coordinates automatically respect the constraint (one coordinate along the wire), so no constraint forces appear — unlike Newton, which needs the explicit normal force. · 广义坐标自动满足约束,无需约束力。

</details>

---

← Previous: [Module 1.2 — Conservation Laws](./module-1.2-conservation-laws.md) · [Phase 1 index](./README.md) · Next: [Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem](./module-1.4-hamiltonian-mechanics-noether.md) →

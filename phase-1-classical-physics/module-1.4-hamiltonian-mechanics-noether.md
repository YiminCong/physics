# Module 1.4 — Hamiltonian Mechanics, Action & Noether's Theorem ⭐
**模块 1.4 — 哈密顿力学、作用量与诺特定理 ⭐**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.4-hamiltonian-mechanics-noether-derivations.md)

---

## 1. The Hamiltonian and Hamilton's Equations · 哈密顿量与哈密顿方程

**Definition.** Given the Lagrangian $L(q, \dot{q}, t)$, define the **conjugate momentum** $p_i = \partial L/\partial \dot{q}_i$. The **Hamiltonian** is obtained by a Legendre transform: $H(q, p, t) = \sum_i p_i \dot{q}_i - L$. For systems with time-independent, velocity-independent potentials, $H = T + V$ = total energy. **Hamilton's equations** replace the $n$ second-order Euler–Lagrange equations with $2n$ first-order equations:

**定义。** 给定拉格朗日量 $L(q, \dot{q}, t)$，定义**共轭动量** $p_i = \partial L/\partial \dot{q}_i$。**哈密顿量**由勒让德变换得到：$H(q, p, t) = \sum_i p_i \dot{q}_i - L$。对于势能不依赖时间和速度的系统，$H = T + V$ = 总能量。**哈密顿方程**将 $n$ 个二阶欧拉–拉格朗日方程替换为 $2n$ 个一阶方程：

$$ \dot{q}_i = \frac{\partial H}{\partial p_i}, \qquad \dot{p}_i = -\frac{\partial H}{\partial q_i}. $$

The state of the system is a point in **phase space** $(q, p)$, and Hamilton's equations describe the flow of that point. The **Poisson bracket** of two observables $f, g$ is $\{f, g\} = \sum_i (\partial f/\partial q_i\, \partial g/\partial p_i - \partial f/\partial p_i\, \partial g/\partial q_i)$. In particular $\{q_i, p_j\} = \delta_{ij}$, and the equation of motion for any observable is $\dot{f} = \{f, H\} + \partial f/\partial t$.

系统的状态是**相空间** $(q, p)$ 中的一个点，哈密顿方程描述该点的流动。两个可观测量 $f$、$g$ 的**泊松括号**为 $\{f, g\} = \sum_i (\partial f/\partial q_i\, \partial g/\partial p_i - \partial f/\partial p_i\, \partial g/\partial q_i)$。特别地，$\{q_i, p_j\} = \delta_{ij}$，任何可观测量的运动方程为 $\dot{f} = \{f, H\} + \partial f/\partial t$。

**Demonstration.** For the 1D harmonic oscillator $H = p^2/2m + \tfrac12 m\omega^2 q^2$. Hamilton's equations give $\dot{q} = p/m$ and $\dot{p} = -m\omega^2 q$, which combine to $\ddot{q} = -\omega^2 q$. Phase-space trajectories are ellipses in the $(q, p)$ plane with area $2\pi E/\omega$, an adiabatic invariant.

**演示。** 对于一维谐振子 $H = p^2/2m + \tfrac12 m\omega^2 q^2$，哈密顿方程给出 $\dot{q} = p/m$ 和 $\dot{p} = -m\omega^2 q$，两者合并得 $\ddot{q} = -\omega^2 q$。相空间轨迹是 $(q, p)$ 平面上面积为 $2\pi E/\omega$ 的椭圆，这是一个绝热不变量。

**Application.** Poisson brackets are the classical skeleton of quantum **commutators**: the canonical quantisation rule replaces $\{q, p\} = 1$ with $[\hat{q}, \hat{p}] = i\hbar$ (Module 3.3). The Hamiltonian generates time evolution both classically (via Poisson brackets) and quantum mechanically (via the Schrödinger equation, Module 3.10). Phase-space thinking underlies statistical mechanics (Phase 2) through Liouville's theorem (phase-space volume is conserved).

**应用。** 泊松括号是量子**对易子**的经典骨架：正则量子化规则将 $\{q, p\} = 1$ 替换为 $[\hat{q}, \hat{p}] = i\hbar$（模块 3.3）。哈密顿量在经典力学（通过泊松括号）和量子力学（通过薛定谔方程，模块 3.10）中均生成时间演化。相空间思维通过刘维尔定理（相空间体积守恒）支撑着统计力学（第 2 阶段）。

## 2. Noether's Theorem: Symmetry → Conservation Law · 诺特定理：对称性 → 守恒定律

**Definition.** **Noether's theorem** (1915) states that every continuous (differentiable) symmetry of the action $S = \int L\, dt$ corresponds to a conserved quantity. Formally, if $L$ is invariant under a one-parameter family of transformations $q_i \to q_i + \varepsilon\, \delta q_i$ (to first order in $\varepsilon$), the **Noether charge** $Q = \sum_i (\partial L/\partial \dot{q}_i)\, \delta q_i$ is conserved: $dQ/dt = 0$.

**定义。** **诺特定理**（1915 年）指出，作用量 $S = \int L\, dt$ 的每一个连续（可微）对称性对应一个守恒量。形式上，若 $L$ 在单参数变换族 $q_i \to q_i + \varepsilon\, \delta q_i$（对 $\varepsilon$ 一阶近似）下不变，则**诺特荷** $Q = \sum_i (\partial L/\partial \dot{q}_i)\, \delta q_i$ 守恒：$dQ/dt = 0$。

**Demonstration.** Three canonical examples: (1) $L$ independent of time $t$ → $H$ conserved (energy). (2) $L$ independent of a spatial translation $x$ → $p_x$ conserved (linear momentum). (3) $L$ independent of a rotation angle $\phi$ → $L_z = mr^2\dot{\phi}$ conserved (angular momentum). Each follows from the cyclic-coordinate argument in Module 1.3 applied to the appropriate generalised coordinate.

**演示。** 三个典型例子：(1) $L$ 不显含时间 $t$ → $H$ 守恒（能量）。(2) $L$ 不显含空间平移坐标 $x$ → $p_x$ 守恒（线动量）。(3) $L$ 不显含转角 $\phi$ → $L_z = mr^2\dot{\phi}$ 守恒（角动量）。每一个都源于模块 1.3 中循环坐标论证应用于适当广义坐标的结果。

**Application.** Noether's theorem is arguably the deepest organising principle in all of physics. In field theory, local (gauge) symmetries produce the conservation of charge and the existence of force-carrying bosons (Phase 8). The global U(1) symmetry of quantum mechanics produces charge conservation; SU(2) and SU(3) gauge symmetries produce the weak and strong forces. Every fundamental interaction is a consequence of a symmetry — the logic that starts here.

**应用。** 诺特定理可以说是整个物理学中最深刻的组织原理。在场论中，局域（规范）对称性产生电荷守恒和传力玻色子的存在（第 8 阶段）。量子力学的整体 U(1) 对称性产生电荷守恒；SU(2) 和 SU(3) 规范对称性产生弱力和强力。每一种基本相互作用都是某种对称性的结果——这一逻辑从这里开始。

---

**Self-test (blank page)**

1. Starting from $L = \tfrac12 m\dot{q}^2 - V(q)$, perform the Legendre transform to obtain $H$ and write down Hamilton's equations.
2. Compute the Poisson bracket $\{L_x, L_y\}$ for a 3D particle, where $\mathbf{L} = \mathbf{r} \times \mathbf{p}$. What does the result tell you about angular momentum components?
3. Show, using Noether's theorem, that if $V$ depends only on the distance $|\mathbf{r}_1 - \mathbf{r}_2|$ between two particles, total momentum is conserved.
4. What is the quantum analogue of the classical Poisson bracket $\{q, p\} = 1$, and why is it physically significant?

**自测（空白页）**

1. 从 $L = \tfrac12 m\dot{q}^2 - V(q)$ 出发，通过勒让德变换求 $H$，并写出哈密顿方程。
2. 对三维粒子（$\mathbf{L} = \mathbf{r} \times \mathbf{p}$）计算泊松括号 $\{L_x, L_y\}$。结果告诉你关于角动量分量的什么信息？
3. 利用诺特定理证明：若 $V$ 仅依赖两粒子间距 $|\mathbf{r}_1 - \mathbf{r}_2|$，则总动量守恒。
4. 经典泊松括号 $\{q, p\} = 1$ 的量子对应是什么？为什么它在物理上意义重大？

---

← Previous: [Module 1.3 — Lagrangian Mechanics & the Variational Principle](./module-1.3-lagrangian-mechanics.md) · [Phase 1 index](./README.md) · Next: [Module 1.5 — Central-Force Problem & Kepler](./module-1.5-central-force-kepler.md) →

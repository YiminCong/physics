# Module 1.19 — Nonlinear Dynamics & Chaos
**模块 1.19 — 非线性动力学与混沌**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.19-nonlinear-dynamics-chaos-derivations.md)

---

## 1. Phase Space, Fixed Points & Bifurcations · 相空间、不动点与分岔

**Definition.** A dynamical system is a set of first-order equations ẋ = F(x) on a **phase space** (the q–p plane of Module 1.4 is the canonical example). **Fixed points** F(x*) = 0 are equilibria; linearizing about them classifies their stability (stable/unstable nodes, saddles, spirals, centres) from the eigenvalues of the Jacobian (Module 0.2). A **bifurcation** is a qualitative change in this structure as a control parameter is varied.

**定义。** 动力学系统是**相空间**上一组一阶方程 ẋ = F(x)（模块 1.4 的 q–p 平面是典型例子）。**不动点** F(x*) = 0 是平衡态；通过雅可比矩阵（模块 0.2）的特征值对其线性化，可以分类其稳定性（稳定/不稳定节点、鞍点、螺旋点、中心）。**分岔**是随控制参数变化，这一结构发生的定性改变。

**Demonstration.** The damped pendulum θ̈ + γθ̇ + ω₀² sin θ = 0 has a stable fixed point at the bottom and an unstable saddle at the top; in phase space, trajectories spiral into the stable point. As driving is increased, period-doubling bifurcations cascade — the route to chaos.

**演示。** 阻尼单摆 θ̈ + γθ̇ + ω₀² sin θ = 0 在底部有稳定不动点，在顶部有不稳定鞍点；在相空间中，轨迹螺旋进入稳定点。随着驱动增大，倍周期分岔级联出现——通往混沌的路径。

**Application.** Nonlinearity is the rule, not the exception: most real systems (pendulums at large amplitude, populations, circuits, lasers) are nonlinear, and the linear oscillators of Module 1.6 are only the small-amplitude limit.

**应用。** 非线性是规律，而非例外：大多数真实系统（大振幅摆、种群、电路、激光器）都是非线性的，模块 1.6 的线性振子只是小振幅极限。

## 2. Chaos & Sensitive Dependence · 混沌与初值敏感性

**Definition.** **Deterministic chaos** is bounded, aperiodic motion in a deterministic system showing **sensitive dependence on initial conditions**: nearby trajectories diverge exponentially, ‖δx(t)‖ ~ ‖δx(0)‖ e^{λt}, with **λ the (positive) Lyapunov exponent**. Dissipative chaotic systems settle onto **strange attractors** of fractal dimension.

**定义。** **确定性混沌**是确定性系统中有界、非周期的运动，表现出**对初始条件的敏感依赖性**：邻近轨迹指数发散，‖δx(t)‖ ~ ‖δx(0)‖ e^{λt}，其中 **λ 是（正的）李雅普诺夫指数**。耗散混沌系统趋于分形维数的**奇异吸引子**。

**Demonstration.** The **logistic map** xₙ₊₁ = r xₙ(1 − xₙ) — a one-line iteration — period-doubles into chaos as r increases, with the universal **Feigenbaum constant** δ ≈ 4.669 governing the cascade. The **Lorenz system**, a 3-variable truncation of convection, produces the iconic butterfly attractor and coined the "butterfly effect."

**演示。** **逻辑斯蒂映射** xₙ₊₁ = r xₙ(1 − xₙ)——一行迭代——随 r 增大通过倍周期分岔进入混沌，普适的**费根鲍姆常数** δ ≈ 4.669 支配这一级联过程。**洛伦兹系统**，对流的三变量截断，产生标志性的蝴蝶吸引子，并创造了"蝴蝶效应"一词。

**Application.** Chaos sets a horizon on predictability — most famously in **weather** (the high-Reynolds turbulence of Module 1.17 is spatiotemporal chaos). The *universality* of the period-doubling route — different systems share the same Feigenbaum constant — foreshadows the universality of critical phenomena and the renormalization group (Module 6.6).

**应用。** 混沌为可预测性设定了极限——最著名的是**天气**（模块 1.17 的高雷诺数湍流是时空混沌）。倍周期路径的*普适性*——不同系统共享同一费根鲍姆常数——预示了临界现象的普适性和重整化群（模块 6.6）。

---

**Self-test (blank page)**

1. Sketch the phase portrait of a damped pendulum and classify its two fixed points.
2. Define the Lyapunov exponent and explain what its sign tells you about long-term predictability.
3. Iterate the logistic map at r = 3.2 and at r = 4 (a few steps each) and describe qualitatively what differs.
4. What does it mean that the period-doubling route to chaos is "universal," and what later concept does this anticipate?

**自测（空白页）**

1. 画出阻尼单摆的相图，并对其两个不动点进行分类。
2. 定义李雅普诺夫指数，解释其符号告诉你关于长期可预测性的什么。
3. 在 r = 3.2 和 r = 4 处各迭代逻辑斯蒂映射几步，定性描述两者有何不同。
4. 通往混沌的倍周期路径是"普适"的，这意味着什么？它预示了哪个后续概念？

---

← Previous: [Module 1.18 — Continuum Mechanics & Elasticity](./module-1.18-continuum-mechanics-elasticity.md) · [Phase 1 index](./README.md) · Next: [Module 1.20 — Canonical Transformations & Hamilton–Jacobi](./module-1.20-canonical-transformations-hamilton-jacobi.md) →

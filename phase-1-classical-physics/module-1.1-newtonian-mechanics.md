---
title: "Module 1.1 — Newtonian Mechanics"
parent: "Phase 1 — Classical Physics"
nav_order: 1
---

# Module 1.1 — Newtonian Mechanics
**模块 1.1 — 牛顿力学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.1-newtonian-mechanics-derivations.md)

---

## 1. Newton's Laws and Equations of Motion · 牛顿定律与运动方程

**Definition.** Classical mechanics rests on Newton's three laws. (1) **Inertia**: a body remains at rest or in uniform motion unless acted on by a net force. (2) **Second law**: the net force equals the rate of change of momentum, $\mathbf{F} = m\mathbf{a}$ (for constant mass). (3) **Action–reaction**: forces come in equal and opposite pairs. An **inertial frame** is one in which the first law holds; all inertial frames are related by Galilean transformations ($v \ll c$). A **force** is any interaction that causes acceleration; common examples are gravity ($F = mg$ near the surface), spring restoring force ($F = -kx$), normal force, tension, and friction.

**定义。** 经典力学建立在牛顿三定律之上。(1) **惯性定律**：物体静止或匀速运动，除非受到合力的作用。(2) **第二定律**：合力等于动量的变化率，$\mathbf{F} = m\mathbf{a}$（质量恒定时）。(3) **作用与反作用定律**：力成对出现，大小相等、方向相反。**惯性系**是第一定律成立的参考系；所有惯性系通过伽利略变换相联系（$v \ll c$）。**力**是引起加速度的任何相互作用；常见例子有重力（近地面 $F = mg$）、弹簧恢复力（$F = -kx$）、法向力、张力和摩擦力。

**Demonstration.** Consider a block of mass $m$ on a frictionless surface connected by a string over a pulley to a hanging mass $M$. Writing Newton's second law for each body and eliminating the tension $T$ gives $a = Mg/(m + M)$, the standard Atwood result. The method — isolate the body, identify all forces, apply $\mathbf{F} = m\mathbf{a}$ along each axis, solve the coupled algebraic or differential equations — is the universal template.

**演示。** 考虑质量为 $m$ 的滑块在无摩擦表面上，通过绳子绕过滑轮连接到悬挂质量 $M$。对每个物体写出牛顿第二定律并消去张力 $T$，得 $a = Mg/(m + M)$，即标准的阿特伍德机结果。该方法——隔离物体、辨识所有力、沿各轴应用 $\mathbf{F} = m\mathbf{a}$、求解耦合代数或微分方程——是通用模板。

**Application.** Every subsequent reformulation of mechanics is built on the same physics encoded here. The Lagrangian approach (Module 1.3) re-derives the same trajectories without resolving constraint forces; the Hamiltonian approach (Module 1.4) recasts the same dynamics in phase space. Knowing Newton's laws is therefore knowing what the more powerful formalisms must reproduce.

**应用。** 力学的每一种后续表述都建立在这里编码的同一物理之上。拉格朗日方法（模块 1.3）无需分解约束力便能重新推导出相同的轨迹；哈密顿方法（模块 1.4）将同样的动力学转化到相空间中。因此，了解牛顿定律就是了解更强大形式体系所必须重现的内容。

## 2. Solving Equations of Motion · 求解运动方程

**Definition.** Newton's second law is a second-order ordinary differential equation (ODE) in the position vector $\mathbf{r}(t)$: $m\ddot{\mathbf{r}} = \mathbf{F}(\mathbf{r}, \dot{\mathbf{r}}, t)$. The general solution contains two integration constants fixed by initial conditions $\mathbf{r}(0)$ and $\dot{\mathbf{r}}(0) = \mathbf{v}_0$.

**定义。** 牛顿第二定律是位置向量 $\mathbf{r}(t)$ 的二阶常微分方程：$m\ddot{\mathbf{r}} = \mathbf{F}(\mathbf{r}, \dot{\mathbf{r}}, t)$。通解包含两个由初始条件 $\mathbf{r}(0)$ 和 $\dot{\mathbf{r}}(0) = \mathbf{v}_0$ 确定的积分常数。

**Demonstration.** Projectile motion under constant gravity: $\ddot{x} = 0$, $\ddot{y} = -g$. Integrating twice gives $x(t) = v_0 \cos\theta \cdot t$, $y(t) = v_0 \sin\theta \cdot t - \tfrac12 g t^2$. The range is $R = v_0^2 \sin 2\theta / g$, maximised at $\theta = 45^\circ$.

**演示。** 匀重力场中的抛体运动：$\ddot{x} = 0$，$\ddot{y} = -g$。积分两次得 $x(t) = v_0 \cos\theta \cdot t$，$y(t) = v_0 \sin\theta \cdot t - \tfrac12 g t^2$。射程为 $R = v_0^2 \sin 2\theta / g$，在 $\theta = 45^\circ$ 时最大。

**Application.** The same ODE machinery applies to planetary orbits (Module 1.5), coupled oscillators (Module 1.6), and charged-particle motion in EM fields — all reduce to solving or approximating Newton's equations in appropriate coordinates. ODEs of this type are treated systematically in Module 0.3.

**应用。** 同样的常微分方程机制适用于行星轨道（模块 1.5）、耦合振子（模块 1.6）以及带电粒子在电磁场中的运动——所有这些都归结为在适当坐标系下求解或近似牛顿方程。此类常微分方程在模块 0.3 中有系统处理。

---

**Self-test (blank page)**

1. State Newton's three laws and give one everyday example of each.
2. An object of mass $m$ slides down a frictionless incline of angle $\theta$. Derive its acceleration along the slope using Newton's second law.
3. Two blocks of masses $m_1$ and $m_2$ are connected by a light string over a frictionless pulley. Find the tension in the string.
4. Why must Newton's laws be stated in an inertial frame? How would $\mathbf{F} = m\mathbf{a}$ appear to an observer in an accelerating car?

**自测（空白页）**

1. 陈述牛顿三定律，并各举一个日常生活中的例子。
2. 质量为 $m$ 的物体沿倾角为 $\theta$ 的无摩擦斜面下滑。用牛顿第二定律推导其沿斜面的加速度。
3. 质量分别为 $m_1$ 和 $m_2$ 的两个滑块通过轻绳绕过无摩擦滑轮相连。求绳中张力。
4. 为什么牛顿定律必须在惯性系中陈述？在加速行驶的汽车中，$\mathbf{F} = m\mathbf{a}$ 对于观察者会呈现出怎样的形式？

---

[Phase 1 index](./README.md) · Next: [Module 1.2 — Conservation Laws](./module-1.2-conservation-laws.md) →

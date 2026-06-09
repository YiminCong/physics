---
title: "Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames"
parent: "Phase 1 — Classical Physics"
nav_order: 7
---

# Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames
**模块 1.7 — 刚体动力学与非惯性系**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.7-rigid-body-non-inertial-frames-derivations.md)

---

## 1. Rigid-Body Rotation and Euler's Equations · 刚体转动与欧拉方程

**Definition.** A **rigid body** is an extended object with fixed inter-particle distances. Its configuration requires six parameters: three for the centre-of-mass position and three for orientation (e.g., Euler angles — natural generalised coordinates in the sense of Module 1.3). The rotational kinetic energy is $T_\text{rot} = \tfrac12\, \boldsymbol{\omega} \cdot \mathbf{I} \cdot \boldsymbol{\omega}$, where $\boldsymbol{\omega}$ is the angular velocity vector and $\mathbf{I}$ is the **moment of inertia tensor**, with components $I_{ij} = \sum_\alpha m_\alpha (|\mathbf{r}_\alpha|^2\delta_{ij} - r_{\alpha i} r_{\alpha j})$. In the **principal-axis frame**, $\mathbf{I}$ is diagonal with eigenvalues $I_1, I_2, I_3$. Angular momentum is $\mathbf{L} = \mathbf{I} \cdot \boldsymbol{\omega}$; note $\mathbf{L}$ and $\boldsymbol{\omega}$ are generally not parallel unless $\boldsymbol{\omega}$ is along a principal axis.

**定义。** **刚体**是粒子间距固定的扩展物体。其构型需要六个参数：三个描述质心位置，三个描述方向（例如欧拉角——模块 1.3 意义下的自然广义坐标）。转动动能为 $T_\text{rot} = \tfrac12\, \boldsymbol{\omega} \cdot \mathbf{I} \cdot \boldsymbol{\omega}$，其中 $\boldsymbol{\omega}$ 为角速度向量，$\mathbf{I}$ 为**惯量张量**，分量为 $I_{ij} = \sum_\alpha m_\alpha (|\mathbf{r}_\alpha|^2\delta_{ij} - r_{\alpha i} r_{\alpha j})$。在**主轴系**中，$\mathbf{I}$ 为对角矩阵，特征值为 $I_1$、$I_2$、$I_3$。角动量为 $\mathbf{L} = \mathbf{I} \cdot \boldsymbol{\omega}$；注意 $\mathbf{L}$ 和 $\boldsymbol{\omega}$ 一般不平行，除非 $\boldsymbol{\omega}$ 沿主轴方向。

The torque equation in the body frame (rotating with angular velocity $\boldsymbol{\omega}$) yields **Euler's equations**:

体坐标系（随角速度 $\boldsymbol{\omega}$ 转动）中的力矩方程给出**欧拉方程**：

$$ I_1 \dot{\omega}_1 - (I_2 - I_3)\, \omega_2 \omega_3 = \tau_1 \qquad \text{(and cyclic permutations).} $$

**Demonstration.** For a torque-free symmetric top ($I_1 = I_2 \ne I_3$, $\tau = 0$), Euler's equations give uniform precession of $\boldsymbol{\omega}$ about the symmetry axis with **body-frame frequency** $\Omega = \omega_3(I_3 - I_1)/I_1$. In the lab frame the angular momentum $\mathbf{L}$ is fixed, and the body precesses around it — the physics of a wobbling football or the Earth's Chandler wobble.

**演示。** 对于无力矩对称陀螺（$I_1 = I_2 \ne I_3$，$\tau = 0$），欧拉方程给出 $\boldsymbol{\omega}$ 绕对称轴的匀速进动，**体坐标系频率**为 $\Omega = \omega_3(I_3 - I_1)/I_1$。在实验室系中角动量 $\mathbf{L}$ 固定，刚体绕其进动——这是摇晃橄榄球或地球钱德勒摆动的物理。

**Application.** The moment of inertia tensor is a rank-2 symmetric tensor (Module 0.6) diagonalised by the same eigenvalue problem as coupled oscillators (Module 1.6). Gyroscopes and precession underpin navigation instruments, NMR pulse sequences, and the stability analysis of rotating spacecraft.

**应用。** 惯量张量是 2 阶对称张量（模块 0.6），由与耦合振子（模块 1.6）相同的特征值问题对角化。陀螺仪和进动是导航仪器、核磁共振脉冲序列以及旋转航天器稳定性分析的基础。

## 2. Non-Inertial Frames: Centrifugal and Coriolis Forces · 非惯性系：离心力与科里奥利力

**Definition.** In a frame rotating with angular velocity $\boldsymbol{\Omega}$ relative to an inertial frame, Newton's second law acquires fictitious (pseudo) forces. For a particle of mass $m$ at position $\mathbf{r}$ with velocity $\mathbf{v}_\text{rot}$ in the rotating frame:

**定义。** 在相对于惯性系以角速度 $\boldsymbol{\Omega}$ 转动的参考系中，牛顿第二定律引入了惯性（虚）力。对于质量为 $m$、在转动系中位置为 $\mathbf{r}$、速度为 $\mathbf{v}_\text{rot}$ 的粒子：

$$ m\mathbf{a}_\text{rot} = \mathbf{F} - 2m\,\boldsymbol{\Omega} \times \mathbf{v}_\text{rot} - m\,\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) - m\,\dot{\boldsymbol{\Omega}} \times \mathbf{r}. $$

The three extra terms are: **Coriolis force** ($-2m\,\boldsymbol{\Omega} \times \mathbf{v}_\text{rot}$), **centrifugal force** ($-m\,\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = m\omega^2 \mathbf{r}_\perp$ outward), and an angular-acceleration term (usually zero for constant $\boldsymbol{\Omega}$). An accelerating (non-rotating) frame introduces a uniform fictitious force $-m\,\mathbf{a}_\text{frame}$ (the "g-force" felt in a lift).

三个额外项分别是：**科里奥利力**（$-2m\,\boldsymbol{\Omega} \times \mathbf{v}_\text{rot}$）、**离心力**（$-m\,\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = m\omega^2 \mathbf{r}_\perp$ 向外）以及角加速度项（对于恒定 $\boldsymbol{\Omega}$ 通常为零）。加速（非转动）参考系引入均匀虚力 $-m\,\mathbf{a}_\text{frame}$（电梯中感受到的"g 力"）。

**Demonstration.** On Earth's surface ($\Omega \approx 7.3 \times 10^{-5}\,\text{rad/s}$), the Coriolis force deflects a freely-falling object eastward and causes large-scale atmospheric circulation to be clockwise in the Northern Hemisphere (low-pressure cyclones). The Foucault pendulum rotates its plane of oscillation with period $T_F = 24\,\text{h} / \sin\lambda$ at latitude $\lambda$, directly demonstrating Earth's rotation.

**演示。** 在地球表面（$\Omega \approx 7.3 \times 10^{-5}\,\text{rad/s}$），科里奥利力使自由落体向东偏转，并使北半球的大尺度大气环流呈顺时针方向（低压气旋）。傅科摆在纬度 $\lambda$ 处以周期 $T_F = 24\,\text{h} / \sin\lambda$ 转动其振荡平面，直接演示了地球的自转。

**Application.** Non-inertial-frame analysis is essential in geophysics (weather patterns, ocean currents), aerospace (guidance systems), and classical chaos (the restricted three-body problem in the rotating frame). The mathematical structure — transforming derivatives between frames — is the precursor to the covariant derivative in general relativity (Phase 7).

**应用。** 非惯性系分析在地球物理学（天气模式、洋流）、航空航天（导航系统）以及经典混沌（转动系中的限制性三体问题）中不可或缺。其数学结构——在参考系间变换导数——是广义相对论（第 7 阶段）协变导数的先驱。

---

**Self-test (blank page)**

1. Define the moment of inertia tensor $I_{ij}$. For a uniform solid sphere of mass $m$ and radius $R$, what are the principal moments?
2. Write Euler's equations for a torque-free rigid body. Explain qualitatively why a rotation about the intermediate principal axis is unstable (the "tennis racket theorem").
3. Derive the expression for the Coriolis force on a particle moving with velocity $\mathbf{v}$ in a frame rotating at angular velocity $\boldsymbol{\Omega}$. In which direction does it deflect a horizontally-moving object in the Northern Hemisphere?
4. A Foucault pendulum at latitude $45^\circ$N completes one full precession cycle in how many hours? Show your reasoning.

**自测（空白页）**

1. 定义惯量张量 $I_{ij}$。对于质量为 $m$、半径为 $R$ 的均匀实心球，主转动惯量是多少？
2. 写出无力矩刚体的欧拉方程。定性解释为什么绕中间主轴的转动是不稳定的（"网球拍定理"）。
3. 推导在角速度为 $\boldsymbol{\Omega}$ 的转动系中以速度 $\mathbf{v}$ 运动的粒子所受科里奥利力的表达式。在北半球，它使水平运动物体向哪个方向偏转？
4. 北纬 $45^\circ$ 处的傅科摆完成一次完整进动需要多少小时？展示你的推理过程。

---

← Previous: [Module 1.6 — Small Oscillations & Coupled Oscillators](./module-1.6-small-oscillations-coupled-oscillators.md) · [Phase 1 index](./README.md) · Next: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) →

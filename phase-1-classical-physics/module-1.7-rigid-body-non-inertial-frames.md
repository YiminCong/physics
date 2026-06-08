# Module 1.7 — Rigid-Body Dynamics & Non-Inertial Frames
**模块 1.7 — 刚体动力学与非惯性系**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**

---

## 1. Rigid-Body Rotation and Euler's Equations · 刚体转动与欧拉方程

**Definition.** A **rigid body** is an extended object with fixed inter-particle distances. Its configuration requires six parameters: three for the centre-of-mass position and three for orientation (e.g., Euler angles — natural generalised coordinates in the sense of Module 1.3). The rotational kinetic energy is T_rot = ½ ω · I · ω, where ω is the angular velocity vector and **I** is the **moment of inertia tensor**, with components I_{ij} = Σ_α m_α (|r_α|²δ_{ij} − r_{αi}r_{αj}). In the **principal-axis frame**, I is diagonal with eigenvalues I₁, I₂, I₃. Angular momentum is L = I · ω; note L and ω are generally not parallel unless ω is along a principal axis.

**定义。** **刚体**是粒子间距固定的扩展物体。其构型需要六个参数：三个描述质心位置，三个描述方向（例如欧拉角——模块 1.3 意义下的自然广义坐标）。转动动能为 T_rot = ½ ω · I · ω，其中 ω 为角速度向量，**I** 为**惯量张量**，分量为 I_{ij} = Σ_α m_α (|r_α|²δ_{ij} − r_{αi}r_{αj})。在**主轴系**中，I 为对角矩阵，特征值为 I₁、I₂、I₃。角动量为 L = I · ω；注意 L 和 ω 一般不平行，除非 ω 沿主轴方向。

The torque equation in the body frame (rotating with angular velocity ω) yields **Euler's equations**:

体坐标系（随角速度 ω 转动）中的力矩方程给出**欧拉方程**：

I₁ ω̇₁ − (I₂ − I₃) ω₂ ω₃ = τ₁   (and cyclic permutations).

**Demonstration.** For a torque-free symmetric top (I₁ = I₂ ≠ I₃, τ = 0), Euler's equations give uniform precession of ω about the symmetry axis with **body-frame frequency** Ω = ω₃(I₃ − I₁)/I₁. In the lab frame the angular momentum L is fixed, and the body precesses around it — the physics of a wobbling football or the Earth's Chandler wobble.

**演示。** 对于无力矩对称陀螺（I₁ = I₂ ≠ I₃，τ = 0），欧拉方程给出 ω 绕对称轴的匀速进动，**体坐标系频率**为 Ω = ω₃(I₃ − I₁)/I₁。在实验室系中角动量 L 固定，刚体绕其进动——这是摇晃橄榄球或地球钱德勒摆动的物理。

**Application.** The moment of inertia tensor is a rank-2 symmetric tensor (Module 0.6) diagonalised by the same eigenvalue problem as coupled oscillators (Module 1.6). Gyroscopes and precession underpin navigation instruments, NMR pulse sequences, and the stability analysis of rotating spacecraft.

**应用。** 惯量张量是 2 阶对称张量（模块 0.6），由与耦合振子（模块 1.6）相同的特征值问题对角化。陀螺仪和进动是导航仪器、核磁共振脉冲序列以及旋转航天器稳定性分析的基础。

## 2. Non-Inertial Frames: Centrifugal and Coriolis Forces · 非惯性系：离心力与科里奥利力

**Definition.** In a frame rotating with angular velocity Ω relative to an inertial frame, Newton's second law acquires fictitious (pseudo) forces. For a particle of mass m at position r with velocity v_rot in the rotating frame:

**定义。** 在相对于惯性系以角速度 Ω 转动的参考系中，牛顿第二定律引入了惯性（虚）力。对于质量为 m、在转动系中位置为 r、速度为 v_rot 的粒子：

m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r) − m Ω̇ × r.

The three extra terms are: **Coriolis force** (−2m Ω × v_rot), **centrifugal force** (−m Ω × (Ω × r) = mω²r_⊥ outward), and an angular-acceleration term (usually zero for constant Ω). An accelerating (non-rotating) frame introduces a uniform fictitious force −m a_frame (the "g-force" felt in a lift).

三个额外项分别是：**科里奥利力**（−2m Ω × v_rot）、**离心力**（−m Ω × (Ω × r) = mω²r_⊥ 向外）以及角加速度项（对于恒定 Ω 通常为零）。加速（非转动）参考系引入均匀虚力 −m a_frame（电梯中感受到的"g 力"）。

**Demonstration.** On Earth's surface (Ω ≈ 7.3 × 10⁻⁵ rad/s), the Coriolis force deflects a freely-falling object eastward and causes large-scale atmospheric circulation to be clockwise in the Northern Hemisphere (low-pressure cyclones). The Foucault pendulum rotates its plane of oscillation with period T_F = 24 h / sin λ at latitude λ, directly demonstrating Earth's rotation.

**演示。** 在地球表面（Ω ≈ 7.3 × 10⁻⁵ rad/s），科里奥利力使自由落体向东偏转，并使北半球的大尺度大气环流呈顺时针方向（低压气旋）。傅科摆在纬度 λ 处以周期 T_F = 24 h / sin λ 转动其振荡平面，直接演示了地球的自转。

**Application.** Non-inertial-frame analysis is essential in geophysics (weather patterns, ocean currents), aerospace (guidance systems), and classical chaos (the restricted three-body problem in the rotating frame). The mathematical structure — transforming derivatives between frames — is the precursor to the covariant derivative in general relativity (Phase 7).

**应用。** 非惯性系分析在地球物理学（天气模式、洋流）、航空航天（导航系统）以及经典混沌（转动系中的限制性三体问题）中不可或缺。其数学结构——在参考系间变换导数——是广义相对论（第 7 阶段）协变导数的先驱。

---

**Self-test (blank page)**

1. Define the moment of inertia tensor I_{ij}. For a uniform solid sphere of mass m and radius R, what are the principal moments?
2. Write Euler's equations for a torque-free rigid body. Explain qualitatively why a rotation about the intermediate principal axis is unstable (the "tennis racket theorem").
3. Derive the expression for the Coriolis force on a particle moving with velocity v in a frame rotating at angular velocity Ω. In which direction does it deflect a horizontally-moving object in the Northern Hemisphere?
4. A Foucault pendulum at latitude 45°N completes one full precession cycle in how many hours? Show your reasoning.

**自测（空白页）**

1. 定义惯量张量 I_{ij}。对于质量为 m、半径为 R 的均匀实心球，主转动惯量是多少？
2. 写出无力矩刚体的欧拉方程。定性解释为什么绕中间主轴的转动是不稳定的（"网球拍定理"）。
3. 推导在角速度为 Ω 的转动系中以速度 v 运动的粒子所受科里奥利力的表达式。在北半球，它使水平运动物体向哪个方向偏转？
4. 北纬 45° 处的傅科摆完成一次完整进动需要多少小时？展示你的推理过程。

---

← Previous: [Module 1.6 — Small Oscillations & Coupled Oscillators](./module-1.6-small-oscillations-coupled-oscillators.md) · [Phase 1 index](./README.md) · Next: [Module 1.8 — Electrostatics & Boundary-Value Problems](./module-1.8-electrostatics-boundary-value-problems.md) →

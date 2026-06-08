# Derivations — Module 1.7: Rigid-Body Dynamics & Non-Inertial Frames
# 推导 — 模块 1.7：刚体动力学与非惯性系

> Companion to [Module 1.7](./module-1.7-rigid-body-non-inertial-frames.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.7](./module-1.7-rigid-body-non-inertial-frames.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Inertia Tensor · 惯量张量

**Claim.** The angular momentum of a rigid body rotating with angular velocity ω is L = I · ω, where the inertia tensor has components:

  I_{ij} = Σ_α m_α (|r_α|² δ_{ij} − r_{αi} r_{αj}).

The rotational kinetic energy is T_rot = ½ ω · I · ω = ½ Σ_{ij} I_{ij} ωᵢ ωⱼ.

**命题。** 以角速度 ω 旋转的刚体的角动量为 L = I · ω，其中惯量张量的分量为：

  I_{ij} = Σ_α m_α (|r_α|² δ_{ij} − r_{αi} r_{αj})。

转动动能为 T_rot = ½ ω · I · ω = ½ Σ_{ij} I_{ij} ωᵢ ωⱼ。

**Step 1 — Velocity of a particle in a rotating body.** For a rigid body rotating with angular velocity ω, the velocity of particle α at position r_α (relative to the body's reference point) is:

**第 1 步 — 旋转刚体中粒子的速度。** 对于以角速度 ω 旋转的刚体，位置为 r_α（相对于刚体参考点）的粒子 α 的速度为：

  v_α = ω × r_α.

**Step 2 — Write the angular momentum.** L = Σ_α m_α r_α × v_α:

**第 2 步 — 写出角动量。** L = Σ_α m_α r_α × v_α：

  L = Σ_α m_α r_α × (ω × r_α).

**Step 3 — Expand using the BAC–CAB rule.** The vector identity A × (B × C) = B(A·C) − C(A·B) gives:

**第 3 步 — 用 BAC–CAB 规则展开。** 向量恒等式 A × (B × C) = B(A·C) − C(A·B) 给出：

  r_α × (ω × r_α) = ω (r_α · r_α) − r_α (r_α · ω) = ω |r_α|² − r_α (r_α · ω).

**Step 4 — Write in component form.** The i-th component of L is:

**第 4 步 — 写成分量形式。** L 的第 i 个分量为：

  Lᵢ = Σ_α m_α [|r_α|² ωᵢ − r_{αi} (Σⱼ r_{αj} ωⱼ)]
     = Σⱼ [Σ_α m_α (|r_α|² δ_{ij} − r_{αi} r_{αj})] ωⱼ
     = Σⱼ I_{ij} ωⱼ.

So **Lᵢ = Σⱼ I_{ij} ωⱼ**, i.e. **L = I · ω**, with I_{ij} = Σ_α m_α(|r_α|² δ_{ij} − r_{αi}r_{αj}). ∎

故 **Lᵢ = Σⱼ I_{ij} ωⱼ**，即 **L = I · ω**，其中 I_{ij} = Σ_α m_α(|r_α|² δ_{ij} − r_{αi}r_{αj})。∎

**Step 5 — Rotational kinetic energy.** T_rot = ½ Σ_α m_α |v_α|² = ½ Σ_α m_α |ω × r_α|². Using the result from Step 3:

**第 5 步 — 转动动能。** T_rot = ½ Σ_α m_α |v_α|² = ½ Σ_α m_α |ω × r_α|²。利用第 3 步的结果：

  T_rot = ½ Σ_α m_α ω · [ω|r_α|² − r_α(r_α · ω)] = ½ ω · L = ½ ω · I · ω. ∎

  T_rot = ½ Σ_α m_α ω · [ω|r_α|² − r_α(r_α · ω)] = ½ ω · L = ½ ω · I · ω。∎

---

## B. Euler's Equations from dL/dt in the Body Frame · 从体坐标系 dL/dt 推导欧拉方程

**Claim.** In the body frame (principal-axis frame), the torque equation τ = dL/dt (in the inertial lab frame) becomes the three **Euler equations**:

  I₁ ω̇₁ − (I₂ − I₃) ω₂ ω₃ = τ₁,
  I₂ ω̇₂ − (I₃ − I₁) ω₃ ω₁ = τ₂,
  I₃ ω̇₃ − (I₁ − I₂) ω₁ ω₂ = τ₃.

**命题。** 在体坐标系（主轴坐标系）中，力矩方程 τ = dL/dt（在惯性实验室系中）变为三个**欧拉方程**：

  I₁ ω̇₁ − (I₂ − I₃) ω₂ ω₃ = τ₁，
  I₂ ω̇₂ − (I₃ − I₁) ω₃ ω₁ = τ₂，
  I₃ ω̇₃ − (I₁ − I₂) ω₁ ω₂ = τ₃。

**Step 1 — Relate time derivatives in the body frame to the lab frame.** For any vector V, the time derivative in the lab frame and in the body frame (rotating at ω) are related by:

**第 1 步 — 将体坐标系中的时间导数与实验室系联系起来。** 对任意向量 V，实验室系和体坐标系（以 ω 旋转）中的时间导数满足：

  (dV/dt)_lab = (dV/dt)_body + ω × V.

This is the **transport theorem** for rotating frames.

这是旋转系的**输运定理**。

**Step 2 — Apply to L.** The torque equation in the lab frame is τ = (dL/dt)_lab. Using the transport theorem:

**第 2 步 — 应用于 L。** 实验室系中的力矩方程为 τ = (dL/dt)_lab。利用输运定理：

  τ = (dL/dt)_body + ω × L.

**Step 3 — Evaluate in the principal-axis frame.** In the body frame with principal axes, L = (I₁ω₁, I₂ω₂, I₃ω₃). Since the principal moments Iᵢ are constant in the body frame:

**第 3 步 — 在主轴坐标系中计算。** 在主轴体坐标系中，L = (I₁ω₁, I₂ω₂, I₃ω₃)。由于主转动惯量 Iᵢ 在体坐标系中为常数：

  (dL/dt)_body = (I₁ω̇₁, I₂ω̇₂, I₃ω̇₃).

**Step 4 — Compute the cross product ω × L.**

**第 4 步 — 计算叉积 ω × L。**

  ω × L = (ω₁, ω₂, ω₃) × (I₁ω₁, I₂ω₂, I₃ω₃)
         = (ω₂ I₃ω₃ − ω₃ I₂ω₂,  ω₃ I₁ω₁ − ω₁ I₃ω₃,  ω₁ I₂ω₂ − ω₂ I₁ω₁).

**Step 5 — Assemble Euler's equations.** The i-th component of τ = (dL/dt)_body + ω × L gives:

**第 5 步 — 组合欧拉方程。** τ = (dL/dt)_body + ω × L 的第 i 个分量给出：

Component 1: τ₁ = I₁ω̇₁ + (I₃ − I₂)ω₂ω₃.

Rearranging: **I₁ω̇₁ − (I₂ − I₃)ω₂ω₃ = τ₁.** ∎₁

分量 1：τ₁ = I₁ω̇₁ + (I₃ − I₂)ω₂ω₃。整理：**I₁ω̇₁ − (I₂ − I₃)ω₂ω₃ = τ₁。** ∎₁

Component 2: τ₂ = I₂ω̇₂ + (I₁ − I₃)ω₃ω₁ = I₂ω̇₂ − (I₃ − I₁)ω₃ω₁.

Rearranging: **I₂ω̇₂ − (I₃ − I₁)ω₃ω₁ = τ₂.** ∎₂

分量 2：τ₂ = I₂ω̇₂ + (I₁ − I₃)ω₃ω₁ = I₂ω̇₂ − (I₃ − I₁)ω₃ω₁。整理：**I₂ω̇₂ − (I₃ − I₁)ω₃ω₁ = τ₂。** ∎₂

Component 3: τ₃ = I₃ω̇₃ + (I₂ − I₁)ω₁ω₂.

Rearranging: **I₃ω̇₃ − (I₁ − I₂)ω₁ω₂ = τ₃.** ∎₃

分量 3：τ₃ = I₃ω̇₃ + (I₂ − I₁)ω₁ω₂。整理：**I₃ω̇₃ − (I₁ − I₂)ω₁ω₂ = τ₃。** ∎₃

---

## C. Torque-Free Symmetric Top — Precession Rate · 无力矩对称陀螺的进动速率

**Claim.** For a torque-free symmetric top (I₁ = I₂ ≡ I_⊥, I₃ the symmetry-axis moment, τ = 0), Euler's equations yield uniform precession of ω about the symmetry axis (ê₃) at the body-frame rate:

  Ω = ω₃ (I₃ − I_⊥) / I_⊥.

**命题。** 对于无力矩对称陀螺（I₁ = I₂ ≡ I_⊥，I₃ 为对称轴转动惯量，τ = 0），欧拉方程给出 ω 绕对称轴（ê₃）的匀速进动，体坐标系频率为：

  Ω = ω₃ (I₃ − I_⊥) / I_⊥。

**Step 1 — Write Euler's equations with τ = 0 and I₁ = I₂ = I_⊥.**

**第 1 步 — 写出 τ = 0、I₁ = I₂ = I_⊥ 时的欧拉方程。**

  I_⊥ ω̇₁ − (I_⊥ − I₃) ω₂ ω₃ = 0,   … (1)
  I_⊥ ω̇₂ − (I₃ − I_⊥) ω₃ ω₁ = 0,   … (2)
  I₃ ω̇₃ − (I_⊥ − I_⊥) ω₁ ω₂ = 0   ⟹   ω̇₃ = 0.   … (3)

**Step 2 — Establish that ω₃ is constant.** Equation (3) gives ω₃ = const. ∎_3

**第 2 步 — 确定 ω₃ 为常数。** 方程 (3) 给出 ω₃ = 常数。∎_3

**Step 3 — Define the precession frequency.** Let Ω = ω₃(I₃ − I_⊥)/I_⊥. Rewrite equations (1) and (2):

**第 3 步 — 定义进动频率。** 令 Ω = ω₃(I₃ − I_⊥)/I_⊥。改写方程 (1) 和 (2)：

  From (1): ω̇₁ = −[(I_⊥ − I₃)/I_⊥] ω₃ ω₂ = +Ω ω₂.
  From (2): ω̇₂ = +[(I₃ − I_⊥)/I_⊥] ω₃ ω₁ = −Ω ω₁.

由 (1)：ω̇₁ = −[(I_⊥ − I₃)/I_⊥] ω₃ ω₂ = +Ω ω₂。
由 (2)：ω̇₂ = +[(I₃ − I_⊥)/I_⊥] ω₃ ω₁ = −Ω ω₁。

**Step 4 — Solve the coupled ODEs.** Define the complex variable η = ω₁ + i ω₂:

**第 4 步 — 求解耦合常微分方程。** 定义复变量 η = ω₁ + i ω₂：

  η̇ = ω̇₁ + i ω̇₂ = Ω ω₂ + i(−Ω ω₁) = −iΩ(ω₁ + i ω₂) = −iΩ η.

This is a simple ODE with solution η(t) = η(0) e^{−iΩt}.

这是一个简单的常微分方程，解为 η(t) = η(0) e^{−iΩt}。

**Step 5 — Interpret the solution.** Writing η(0) = ω_⊥ (the initial transverse angular speed, real and positive):

**第 5 步 — 解释解。** 令 η(0) = ω_⊥（初始横向角速度，实数且为正）：

  ω₁(t) = ω_⊥ cos(Ωt),   ω₂(t) = −ω_⊥ sin(Ωt).

The transverse component of ω precesses uniformly around the symmetry axis ê₃ at angular frequency |Ω| = |ω₃(I₃ − I_⊥)/I_⊥|.

ω 的横向分量以角频率 |Ω| = |ω₃(I₃ − I_⊥)/I_⊥| 绕对称轴 ê₃ 匀速进动。

Therefore, in the body frame ω traces out a cone around ê₃, completing one revolution in time T = 2π/|Ω|. This is **Eulerian (body-frame) precession**.

因此，在体坐标系中 ω 绕 ê₃ 描出一个锥，在时间 T = 2π/|Ω| 内完成一圈。这就是**欧拉（体坐标系）进动**。

**Precession rate:**

**进动速率：**

  **Ω = ω₃ (I₃ − I_⊥) / I_⊥.** ∎

  **Ω = ω₃ (I₃ − I_⊥) / I_⊥。** ∎

**Physical note.** For a prolate body (I₃ < I_⊥, e.g. a football), Ω < 0: ω precesses in the opposite sense to ω₃. For an oblate body (I₃ > I_⊥, e.g. a frisbee), Ω > 0: precession is in the same sense. The Earth, slightly oblate (I₃ − I_⊥ ≈ 3 × 10⁻³ I_⊥), exhibits the **Chandler wobble** with a period of ≈ 14 months (Earth's period in the body frame; ≈ 305 days, close to the observed 433 days — the discrepancy is due to Earth's non-rigidity).

**物理说明。** 对于长椭球体（I₃ < I_⊥，如橄榄球），Ω < 0：ω 进动方向与 ω₃ 相反。对于扁椭球体（I₃ > I_⊥，如飞盘），Ω > 0：进动方向相同。地球略为扁椭球（I₃ − I_⊥ ≈ 3 × 10⁻³ I_⊥），体坐标系周期约 305 天（接近观测值 433 天——差异源于地球的非刚性），产生**钱德勒摆动**，周期约 14 个月。

---

## D. Transport Theorem and Rotating-Frame Forces (Derivation of Coriolis and Centrifugal) · 输运定理与转动系惯性力（科里奥利力与离心力的推导）

**Claim.** In a frame rotating at angular velocity Ω relative to an inertial frame, a particle of mass m at position r with velocity v_rot (in the rotating frame) satisfies:

  m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r).

The three terms on the right are: the real force F, the **Coriolis force** −2m Ω × v_rot, and the **centrifugal force** −m Ω × (Ω × r).

**命题。** 在相对于惯性系以角速度 Ω 旋转的参考系中，质量为 m、位置为 r、速度（在转动系中）为 v_rot 的粒子满足：

  m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r)。

右侧三项分别为：真实力 F、**科里奥利力** −2m Ω × v_rot 以及**离心力** −m Ω × (Ω × r)。

**Step 1 — Transport theorem.** For any vector V, its time derivative in the inertial frame and in the rotating frame are related by:

**第 1 步 — 输运定理。** 对任意向量 V，其在惯性系和转动系中的时间导数满足：

  (dV/dt)_inertial = (dV/dt)_rot + Ω × V.

*Derivation of the transport theorem:* Decompose V in the rotating-frame basis {ê₁, ê₂, ê₃}: V = Σᵢ Vᵢ êᵢ. The inertial-frame derivative is:

*输运定理的推导：* 在转动系基矢 {ê₁, ê₂, ê₃} 中分解 V：V = Σᵢ Vᵢ êᵢ。惯性系导数为：

  (dV/dt)_inertial = Σᵢ V̇ᵢ êᵢ + Σᵢ Vᵢ (dêᵢ/dt)_inertial.

The first sum is (dV/dt)_rot. For a basis vector rotating with the frame: (dêᵢ/dt)_inertial = Ω × êᵢ. Therefore:

第一个和式为 (dV/dt)_rot。对于随系旋转的基矢：(dêᵢ/dt)_inertial = Ω × êᵢ。因此：

  (dV/dt)_inertial = (dV/dt)_rot + Σᵢ Vᵢ Ω × êᵢ = (dV/dt)_rot + Ω × V. ∎_transport

**Step 2 — Apply to position to get velocity.** Let V = r: r_inertial = r_rot (same position vector). Apply the transport theorem:

**第 2 步 — 应用于位置以得速度。** 令 V = r：r_inertial = r_rot（相同位置矢量）。应用输运定理：

  v_inertial = v_rot + Ω × r.

**Step 3 — Apply the transport theorem again to get acceleration.** Apply the theorem to v_inertial:

**第 3 步 — 再次应用输运定理以得加速度。** 对 v_inertial 应用定理：

  a_inertial = (d v_inertial /dt)_rot + Ω × v_inertial.

Substitute v_inertial = v_rot + Ω × r:

代入 v_inertial = v_rot + Ω × r：

  a_inertial = (d/dt)_rot(v_rot + Ω × r) + Ω × (v_rot + Ω × r)
             = a_rot + (dΩ/dt)_rot × r + Ω × ṙ_rot + Ω × v_rot + Ω × (Ω × r).

For constant Ω: (dΩ/dt)_rot = 0. Also ṙ_rot = v_rot:

对于恒定 Ω：(dΩ/dt)_rot = 0。且 ṙ_rot = v_rot：

  a_inertial = a_rot + 2 Ω × v_rot + Ω × (Ω × r).

**Step 4 — Newton's second law.** In the inertial frame: m a_inertial = F. Therefore:

**第 4 步 — 牛顿第二定律。** 在惯性系中：m a_inertial = F。因此：

  m [a_rot + 2 Ω × v_rot + Ω × (Ω × r)] = F.

Solving for a_rot:

解出 a_rot：

  **m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r).** ∎

  **m a_rot = F − 2m Ω × v_rot − m Ω × (Ω × r)。** ∎

The term −2m Ω × v_rot is the **Coriolis force** (depends on velocity in the rotating frame) and −m Ω × (Ω × r) = mΩ² r_⊥ (pointing outward from the rotation axis) is the **centrifugal force**.

项 −2m Ω × v_rot 为**科里奥利力**（依赖于转动系中的速度），−m Ω × (Ω × r) = mΩ² r_⊥（指向旋转轴外侧）为**离心力**。

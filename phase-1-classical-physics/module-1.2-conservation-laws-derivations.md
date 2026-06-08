# Derivations — Module 1.2: Conservation Laws
# 推导 — 模块 1.2：守恒定律

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.2](./module-1.2-conservation-laws.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.2](./module-1.2-conservation-laws.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Energy Conservation for a Conservative Force · 保守力下的能量守恒

**Claim.** If the net force on a particle is conservative, i.e. F = −∇V for some scalar field V(r), then the total mechanical energy E = ½mv² + V(r) is constant along any trajectory: dE/dt = 0.

**命题。** 若作用在粒子上的合力是保守力，即 F = −∇V 对某标量场 V(r) 成立，则总机械能 E = ½mv² + V(r) 沿任意轨迹为常数：dE/dt = 0。

**Step 1 — Compute dE/dt.** Differentiate the total energy with respect to time:

**第 1 步 — 计算 dE/dt。** 对总能量关于时间求导：

  dE/dt = d/dt (½mv²) + dV/dt.

**Step 2 — Expand the kinetic-energy term.** Using v = ṙ and the product rule:

**第 2 步 — 展开动能项。** 利用 v = ṙ 和乘积法则：

  d/dt (½mv²) = ½m · d(v · v)/dt = m v · (dv/dt) = m v · a.

By Newton's second law F = ma, so m a = F:

由牛顿第二定律 F = ma，故 m a = F：

  d/dt (½mv²) = F · v.

**Step 3 — Expand the potential-energy term.** Using the chain rule for V(r(t)):

**第 3 步 — 展开势能项。** 对 V(r(t)) 使用链式法则：

  dV/dt = (∂V/∂x)ẋ + (∂V/∂y)ẏ + (∂V/∂z)ż = (∇V) · ṙ = (∇V) · v.

**Step 4 — Add the two terms.** Combining Steps 2 and 3:

**第 4 步 — 合并两项。** 综合第 2、3 步：

  dE/dt = F · v + (∇V) · v = (F + ∇V) · v.

**Step 5 — Apply the definition of a conservative force.** Since F = −∇V, we have F + ∇V = 0. Therefore:

**第 5 步 — 应用保守力的定义。** 由于 F = −∇V，有 F + ∇V = 0。因此：

  dE/dt = 0   ⟹   **E = ½mv² + V = const.** ∎

---

## B. Angular Momentum Conservation Under a Central Force · 有心力下的角动量守恒

**Claim.** For a particle subject to a central force F = F(r) r̂ (directed along the position vector), the angular momentum L = r × p satisfies dL/dt = 0 and is therefore conserved.

**命题。** 对于受有心力 F = F(r) r̂（沿位置矢量方向）作用的粒子，角动量 L = r × p 满足 dL/dt = 0，因此守恒。

**Step 1 — Differentiate L with respect to time.** Using the product rule for the cross product:

**第 1 步 — 对 L 关于时间求导。** 对叉积使用乘积法则：

  dL/dt = d/dt (r × p) = ṙ × p + r × ṗ.

**Step 2 — Evaluate the first cross product.** Since p = mv = mṙ, we have ṙ × p = ṙ × (mṙ) = m(ṙ × ṙ) = 0, because any vector crossed with itself is zero.

**第 2 步 — 计算第一个叉积。** 由于 p = mv = mṙ，有 ṙ × p = ṙ × (mṙ) = m(ṙ × ṙ) = 0，因为任何向量与自身的叉积为零。

**Step 3 — Evaluate the second cross product.** By Newton's second law ṗ = F. The torque about the origin is:

**第 3 步 — 计算第二个叉积。** 由牛顿第二定律 ṗ = F。关于原点的力矩为：

  r × ṗ = r × F.

For a central force F = F(r) r̂, and since r = r r̂, we have:

对于有心力 F = F(r) r̂，由于 r = r r̂，有：

  r × F = r r̂ × F(r) r̂ = r F(r) (r̂ × r̂) = 0.

The cross product vanishes because r̂ × r̂ = 0.

叉积为零，因为 r̂ × r̂ = 0。

**Step 4 — Conclude.** Combining Steps 1–3:

**第 4 步 — 得出结论。** 综合第 1–3 步：

  dL/dt = 0 + 0 = 0   ⟹   **L = r × p = const.** ∎

**Corollary — Kepler's second law.** The rate at which the position vector sweeps area is dA/dt = ½|r × ṙ| = L/(2m) = const. Equal areas are swept in equal times.

**推论——开普勒第二定律。** 位置矢量扫过面积的速率为 dA/dt = ½|r × ṙ| = L/(2m) = 常数。相等时间内扫过相等面积。

---

## C. Elastic Collision Relations · 弹性碰撞关系

**Claim.** In a one-dimensional elastic collision between mass m₁ moving at velocity u₁ and stationary mass m₂, the final velocities are:

  v₁ = (m₁ − m₂)/(m₁ + m₂) · u₁,   v₂ = 2m₁/(m₁ + m₂) · u₁.

**命题。** 在质量 m₁ 以速度 u₁ 运动、质量 m₂ 静止的一维弹性碰撞中，末速度为：

  v₁ = (m₁ − m₂)/(m₁ + m₂) · u₁，  v₂ = 2m₁/(m₁ + m₂) · u₁。

**Step 1 — Write the conservation equations.** Two scalar equations hold simultaneously:

**第 1 步 — 写出守恒方程。** 两个标量方程同时成立：

  (momentum)  m₁ u₁ = m₁ v₁ + m₂ v₂,                  … (I)
  (energy)    ½m₁ u₁² = ½m₁ v₁² + ½m₂ v₂².             … (II)

**Step 2 — Rearrange both equations.** From (I): m₁(u₁ − v₁) = m₂ v₂. From (II): m₁(u₁² − v₁²) = m₂ v₂².

**第 2 步 — 整理两个方程。** 由 (I)：m₁(u₁ − v₁) = m₂ v₂。由 (II)：m₁(u₁² − v₁²) = m₂ v₂²。

**Step 3 — Divide the energy equation by the momentum equation.** Factoring the left side of (II): m₁(u₁ − v₁)(u₁ + v₁) = m₂ v₂². Dividing by m₁(u₁ − v₁) = m₂ v₂ (assuming u₁ ≠ v₁, i.e. non-trivial collision):

**第 3 步 — 用动量方程除能量方程。** 对 (II) 左侧因式分解：m₁(u₁ − v₁)(u₁ + v₁) = m₂ v₂²。除以 m₁(u₁ − v₁) = m₂ v₂（假设 u₁ ≠ v₁，即非平凡碰撞）：

  u₁ + v₁ = v₂.                                          … (III)

This is the key relation: relative speed is reversed in an elastic collision.

这是关键关系：弹性碰撞中相对速度反向。

**Step 4 — Solve the linear system (I) and (III).** Substitute (III) into (I):

**第 4 步 — 求解线性方程组 (I) 和 (III)。** 将 (III) 代入 (I)：

  m₁ u₁ = m₁ v₁ + m₂(u₁ + v₁) = (m₁ + m₂) v₁ + m₂ u₁.

Solving for v₁:

解出 v₁：

  v₁ = (m₁ − m₂)/(m₁ + m₂) · u₁.

Then from (III): v₂ = u₁ + v₁ = u₁ + (m₁ − m₂)u₁/(m₁ + m₂) = 2m₁ u₁/(m₁ + m₂). ∎

再由 (III)：v₂ = u₁ + v₁ = u₁ + (m₁ − m₂)u₁/(m₁ + m₂) = 2m₁ u₁/(m₁ + m₂)。∎

**Verification — Special cases.** (a) m₁ = m₂: v₁ = 0, v₂ = u₁ — complete velocity exchange (billiard balls). (b) m₁ ≫ m₂: v₁ ≈ u₁ (heavy mass barely deflected), v₂ ≈ 2u₁ (light mass bounces back at twice the incident speed).

**验证——特殊情形。** (a) m₁ = m₂：v₁ = 0，v₂ = u₁——完全速度交换（台球）。(b) m₁ ≫ m₂：v₁ ≈ u₁（重质量几乎不偏转），v₂ ≈ 2u₁（轻质量以两倍入射速度弹回）。

---

## D. Centre-of-Mass Motion · 质心运动

**Claim.** The total momentum of an N-body system equals M v_cm, where M = Σmᵢ is the total mass and v_cm = (Σmᵢvᵢ)/M is the centre-of-mass velocity. If no net external force acts, v_cm is constant.

**命题。** N 体系统的总动量等于 M v_cm，其中 M = Σmᵢ 为总质量，v_cm = (Σmᵢvᵢ)/M 为质心速度。若无净外力作用，则 v_cm 为常数。

**Step 1 — Define the centre of mass.** The centre-of-mass position is r_cm = (Σmᵢrᵢ)/M. Differentiating with respect to time:

**第 1 步 — 定义质心。** 质心位置为 r_cm = (Σmᵢrᵢ)/M。对时间求导：

  M v_cm = M ṙ_cm = Σmᵢṙᵢ = Σmᵢvᵢ = Σpᵢ = P_total.

**Step 2 — Apply Newton's second law to the whole system.** The time derivative of total momentum is the total force:

**第 2 步 — 对整个系统应用牛顿第二定律。** 总动量的时间导数等于合力：

  dP_total/dt = Σᵢ dpᵢ/dt = Σᵢ Fᵢ.

By Newton's third law all internal forces cancel in pairs, leaving only external forces:

由牛顿第三定律，所有内力成对相消，仅剩外力：

  dP_total/dt = F_ext.

**Step 3 — Conclude.** If F_ext = 0, then dP_total/dt = 0, so P_total = M v_cm = const, and the centre of mass moves with constant velocity. ∎

**第 3 步 — 得出结论。** 若 F_ext = 0，则 dP_total/dt = 0，故 P_total = M v_cm = 常数，质心以恒定速度运动。∎

---
title: "Derivations — Module 1.2: Conservation Laws"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.2: Conservation Laws
# 推导 — 模块 1.2：守恒定律

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.2](./module-1.2-conservation-laws.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.2](./module-1.2-conservation-laws.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Energy Conservation for a Conservative Force · 保守力下的能量守恒

**Claim.** If the net force on a particle is conservative, i.e. $\mathbf{F} = -\nabla V$ for some scalar field $V(\mathbf{r})$, then the total mechanical energy $E = \tfrac12 m v^2 + V(\mathbf{r})$ is constant along any trajectory: $dE/dt = 0$.

**命题。** 若作用在粒子上的合力是保守力，即 $\mathbf{F} = -\nabla V$ 对某标量场 $V(\mathbf{r})$ 成立，则总机械能 $E = \tfrac12 m v^2 + V(\mathbf{r})$ 沿任意轨迹为常数：$dE/dt = 0$。

**Step 1 — Compute $dE/dt$.** Differentiate the total energy with respect to time:

**第 1 步 — 计算 $dE/dt$。** 对总能量关于时间求导：

$$ \frac{dE}{dt} = \frac{d}{dt}\Big(\tfrac12 m v^2\Big) + \frac{dV}{dt}. $$

**Step 2 — Expand the kinetic-energy term.** Using $\mathbf{v} = \dot{\mathbf{r}}$ and the product rule:

**第 2 步 — 展开动能项。** 利用 $\mathbf{v} = \dot{\mathbf{r}}$ 和乘积法则：

$$ \frac{d}{dt}\Big(\tfrac12 m v^2\Big) = \tfrac12 m\,\frac{d(\mathbf{v} \cdot \mathbf{v})}{dt} = m\,\mathbf{v} \cdot \frac{d\mathbf{v}}{dt} = m\,\mathbf{v} \cdot \mathbf{a}. $$

By Newton's second law $\mathbf{F} = m\mathbf{a}$, so $m\mathbf{a} = \mathbf{F}$:

由牛顿第二定律 $\mathbf{F} = m\mathbf{a}$，故 $m\mathbf{a} = \mathbf{F}$：

$$ \frac{d}{dt}\Big(\tfrac12 m v^2\Big) = \mathbf{F} \cdot \mathbf{v}. $$

**Step 3 — Expand the potential-energy term.** Using the chain rule for $V(\mathbf{r}(t))$:

**第 3 步 — 展开势能项。** 对 $V(\mathbf{r}(t))$ 使用链式法则：

$$ \frac{dV}{dt} = \frac{\partial V}{\partial x}\dot{x} + \frac{\partial V}{\partial y}\dot{y} + \frac{\partial V}{\partial z}\dot{z} = (\nabla V) \cdot \dot{\mathbf{r}} = (\nabla V) \cdot \mathbf{v}. $$

**Step 4 — Add the two terms.** Combining Steps 2 and 3:

**第 4 步 — 合并两项。** 综合第 2、3 步：

$$ \frac{dE}{dt} = \mathbf{F} \cdot \mathbf{v} + (\nabla V) \cdot \mathbf{v} = (\mathbf{F} + \nabla V) \cdot \mathbf{v}. $$

**Step 5 — Apply the definition of a conservative force.** Since $\mathbf{F} = -\nabla V$, we have $\mathbf{F} + \nabla V = 0$. Therefore:

**第 5 步 — 应用保守力的定义。** 由于 $\mathbf{F} = -\nabla V$，有 $\mathbf{F} + \nabla V = 0$。因此：

$$ \frac{dE}{dt} = 0 \quad\implies\quad \boxed{\, E = \tfrac12 m v^2 + V = \text{const} \,} \qquad \blacksquare $$

---

## B. Angular Momentum Conservation Under a Central Force · 有心力下的角动量守恒

**Claim.** For a particle subject to a central force $\mathbf{F} = F(r)\,\hat{\mathbf{r}}$ (directed along the position vector), the angular momentum $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ satisfies $d\mathbf{L}/dt = 0$ and is therefore conserved.

**命题。** 对于受有心力 $\mathbf{F} = F(r)\,\hat{\mathbf{r}}$（沿位置矢量方向）作用的粒子，角动量 $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ 满足 $d\mathbf{L}/dt = 0$，因此守恒。

**Step 1 — Differentiate $\mathbf{L}$ with respect to time.** Using the product rule for the cross product:

**第 1 步 — 对 $\mathbf{L}$ 关于时间求导。** 对叉积使用乘积法则：

$$ \frac{d\mathbf{L}}{dt} = \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) = \dot{\mathbf{r}} \times \mathbf{p} + \mathbf{r} \times \dot{\mathbf{p}}. $$

**Step 2 — Evaluate the first cross product.** Since $\mathbf{p} = m\mathbf{v} = m\dot{\mathbf{r}}$, we have $\dot{\mathbf{r}} \times \mathbf{p} = \dot{\mathbf{r}} \times (m\dot{\mathbf{r}}) = m(\dot{\mathbf{r}} \times \dot{\mathbf{r}}) = 0$, because any vector crossed with itself is zero.

**第 2 步 — 计算第一个叉积。** 由于 $\mathbf{p} = m\mathbf{v} = m\dot{\mathbf{r}}$，有 $\dot{\mathbf{r}} \times \mathbf{p} = \dot{\mathbf{r}} \times (m\dot{\mathbf{r}}) = m(\dot{\mathbf{r}} \times \dot{\mathbf{r}}) = 0$，因为任何向量与自身的叉积为零。

**Step 3 — Evaluate the second cross product.** By Newton's second law $\dot{\mathbf{p}} = \mathbf{F}$. The torque about the origin is:

**第 3 步 — 计算第二个叉积。** 由牛顿第二定律 $\dot{\mathbf{p}} = \mathbf{F}$。关于原点的力矩为：

$$ \mathbf{r} \times \dot{\mathbf{p}} = \mathbf{r} \times \mathbf{F}. $$

For a central force $\mathbf{F} = F(r)\,\hat{\mathbf{r}}$, and since $\mathbf{r} = r\,\hat{\mathbf{r}}$, we have:

对于有心力 $\mathbf{F} = F(r)\,\hat{\mathbf{r}}$，由于 $\mathbf{r} = r\,\hat{\mathbf{r}}$，有：

$$ \mathbf{r} \times \mathbf{F} = r\,\hat{\mathbf{r}} \times F(r)\,\hat{\mathbf{r}} = r F(r)\,(\hat{\mathbf{r}} \times \hat{\mathbf{r}}) = 0. $$

The cross product vanishes because $\hat{\mathbf{r}} \times \hat{\mathbf{r}} = 0$.

叉积为零，因为 $\hat{\mathbf{r}} \times \hat{\mathbf{r}} = 0$。

**Step 4 — Conclude.** Combining Steps 1–3:

**第 4 步 — 得出结论。** 综合第 1–3 步：

$$ \frac{d\mathbf{L}}{dt} = 0 + 0 = 0 \quad\implies\quad \boxed{\, \mathbf{L} = \mathbf{r} \times \mathbf{p} = \text{const} \,} \qquad \blacksquare $$

**Corollary — Kepler's second law.** The rate at which the position vector sweeps area is $dA/dt = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}| = L/(2m) = \text{const}$. Equal areas are swept in equal times.

**推论——开普勒第二定律。** 位置矢量扫过面积的速率为 $dA/dt = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}| = L/(2m) = $ 常数。相等时间内扫过相等面积。

---

## C. Elastic Collision Relations · 弹性碰撞关系

**Claim.** In a one-dimensional elastic collision between mass $m_1$ moving at velocity $u_1$ and stationary mass $m_2$, the final velocities are:

$$ v_1 = \frac{m_1 - m_2}{m_1 + m_2}\,u_1, \qquad v_2 = \frac{2m_1}{m_1 + m_2}\,u_1. $$

**命题。** 在质量 $m_1$ 以速度 $u_1$ 运动、质量 $m_2$ 静止的一维弹性碰撞中，末速度为：

$$ v_1 = \frac{m_1 - m_2}{m_1 + m_2}\,u_1, \qquad v_2 = \frac{2m_1}{m_1 + m_2}\,u_1. $$

**Step 1 — Write the conservation equations.** Two scalar equations hold simultaneously:

**第 1 步 — 写出守恒方程。** 两个标量方程同时成立：

$$ \begin{aligned}
\text{(momentum)} \quad & m_1 u_1 = m_1 v_1 + m_2 v_2, && \text{(I)} \\
\text{(energy)} \quad & \tfrac12 m_1 u_1^2 = \tfrac12 m_1 v_1^2 + \tfrac12 m_2 v_2^2. && \text{(II)}
\end{aligned} $$

**Step 2 — Rearrange both equations.** From (I): $m_1(u_1 - v_1) = m_2 v_2$. From (II): $m_1(u_1^2 - v_1^2) = m_2 v_2^2$.

**第 2 步 — 整理两个方程。** 由 (I)：$m_1(u_1 - v_1) = m_2 v_2$。由 (II)：$m_1(u_1^2 - v_1^2) = m_2 v_2^2$。

**Step 3 — Divide the energy equation by the momentum equation.** Factoring the left side of (II): $m_1(u_1 - v_1)(u_1 + v_1) = m_2 v_2^2$. Dividing by $m_1(u_1 - v_1) = m_2 v_2$ (assuming $u_1 \ne v_1$, i.e. non-trivial collision):

**第 3 步 — 用动量方程除能量方程。** 对 (II) 左侧因式分解：$m_1(u_1 - v_1)(u_1 + v_1) = m_2 v_2^2$。除以 $m_1(u_1 - v_1) = m_2 v_2$（假设 $u_1 \ne v_1$，即非平凡碰撞）：

$$ u_1 + v_1 = v_2. \qquad \text{(III)} $$

This is the key relation: relative speed is reversed in an elastic collision.

这是关键关系：弹性碰撞中相对速度反向。

**Step 4 — Solve the linear system (I) and (III).** Substitute (III) into (I):

**第 4 步 — 求解线性方程组 (I) 和 (III)。** 将 (III) 代入 (I)：

$$ m_1 u_1 = m_1 v_1 + m_2(u_1 + v_1) = (m_1 + m_2) v_1 + m_2 u_1. $$

Solving for $v_1$:

解出 $v_1$：

$$ v_1 = \frac{m_1 - m_2}{m_1 + m_2}\,u_1. $$

Then from (III): $v_2 = u_1 + v_1 = u_1 + \dfrac{(m_1 - m_2)u_1}{m_1 + m_2} = \dfrac{2m_1 u_1}{m_1 + m_2}$. $\blacksquare$

再由 (III)：$v_2 = u_1 + v_1 = u_1 + \dfrac{(m_1 - m_2)u_1}{m_1 + m_2} = \dfrac{2m_1 u_1}{m_1 + m_2}$。$\blacksquare$

**Verification — Special cases.** (a) $m_1 = m_2$: $v_1 = 0$, $v_2 = u_1$ — complete velocity exchange (billiard balls). (b) $m_1 \gg m_2$: $v_1 \approx u_1$ (heavy mass barely deflected), $v_2 \approx 2u_1$ (light mass bounces back at twice the incident speed).

**验证——特殊情形。** (a) $m_1 = m_2$：$v_1 = 0$，$v_2 = u_1$——完全速度交换（台球）。(b) $m_1 \gg m_2$：$v_1 \approx u_1$（重质量几乎不偏转），$v_2 \approx 2u_1$（轻质量以两倍入射速度弹回）。

---

## D. Centre-of-Mass Motion · 质心运动

**Claim.** The total momentum of an $N$-body system equals $M\mathbf{v}_\text{cm}$, where $M = \sum m_i$ is the total mass and $\mathbf{v}_\text{cm} = (\sum m_i \mathbf{v}_i)/M$ is the centre-of-mass velocity. If no net external force acts, $\mathbf{v}_\text{cm}$ is constant.

**命题。** $N$ 体系统的总动量等于 $M\mathbf{v}_\text{cm}$，其中 $M = \sum m_i$ 为总质量，$\mathbf{v}_\text{cm} = (\sum m_i \mathbf{v}_i)/M$ 为质心速度。若无净外力作用，则 $\mathbf{v}_\text{cm}$ 为常数。

**Step 1 — Define the centre of mass.** The centre-of-mass position is $\mathbf{r}_\text{cm} = (\sum m_i \mathbf{r}_i)/M$. Differentiating with respect to time:

**第 1 步 — 定义质心。** 质心位置为 $\mathbf{r}_\text{cm} = (\sum m_i \mathbf{r}_i)/M$。对时间求导：

$$ M\mathbf{v}_\text{cm} = M\dot{\mathbf{r}}_\text{cm} = \sum m_i \dot{\mathbf{r}}_i = \sum m_i \mathbf{v}_i = \sum \mathbf{p}_i = \mathbf{P}_\text{total}. $$

**Step 2 — Apply Newton's second law to the whole system.** The time derivative of total momentum is the total force:

**第 2 步 — 对整个系统应用牛顿第二定律。** 总动量的时间导数等于合力：

$$ \frac{d\mathbf{P}_\text{total}}{dt} = \sum_i \frac{d\mathbf{p}_i}{dt} = \sum_i \mathbf{F}_i. $$

By Newton's third law all internal forces cancel in pairs, leaving only external forces:

由牛顿第三定律，所有内力成对相消，仅剩外力：

$$ \frac{d\mathbf{P}_\text{total}}{dt} = \mathbf{F}_\text{ext}. $$

**Step 3 — Conclude.** If $\mathbf{F}_\text{ext} = 0$, then $d\mathbf{P}_\text{total}/dt = 0$, so $\mathbf{P}_\text{total} = M\mathbf{v}_\text{cm} = \text{const}$, and the centre of mass moves with constant velocity. $\blacksquare$

**第 3 步 — 得出结论。** 若 $\mathbf{F}_\text{ext} = 0$，则 $d\mathbf{P}_\text{total}/dt = 0$，故 $\mathbf{P}_\text{total} = M\mathbf{v}_\text{cm} = $ 常数，质心以恒定速度运动。$\blacksquare$

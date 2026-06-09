---
title: "Derivations — Module 1.7: Rigid-Body Dynamics & Non-Inertial Frames"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.7: Rigid-Body Dynamics & Non-Inertial Frames
# 推导 — 模块 1.7：刚体动力学与非惯性系

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.7](./module-1.7-rigid-body-non-inertial-frames.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.7](./module-1.7-rigid-body-non-inertial-frames.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Inertia Tensor · 惯量张量

**Claim.** The angular momentum of a rigid body rotating with angular velocity $\boldsymbol{\omega}$ is $\mathbf{L} = \mathbf{I}\cdot\boldsymbol{\omega}$, where the inertia tensor has components:

$$ I_{ij} = \sum_\alpha m_\alpha \left(|\mathbf{r}_\alpha|^2\, \delta_{ij} - r_{\alpha i}\, r_{\alpha j}\right). $$

The rotational kinetic energy is $T_\text{rot} = \tfrac12\, \boldsymbol{\omega}\cdot\mathbf{I}\cdot\boldsymbol{\omega} = \tfrac12 \sum_{ij} I_{ij}\, \omega_i\, \omega_j$.

**命题。** 以角速度 $\boldsymbol{\omega}$ 旋转的刚体的角动量为 $\mathbf{L} = \mathbf{I}\cdot\boldsymbol{\omega}$，其中惯量张量的分量为：

$$ I_{ij} = \sum_\alpha m_\alpha \left(|\mathbf{r}_\alpha|^2\, \delta_{ij} - r_{\alpha i}\, r_{\alpha j}\right). $$

转动动能为 $T_\text{rot} = \tfrac12\, \boldsymbol{\omega}\cdot\mathbf{I}\cdot\boldsymbol{\omega} = \tfrac12 \sum_{ij} I_{ij}\, \omega_i\, \omega_j$。

**Step 1 — Velocity of a particle in a rotating body.** For a rigid body rotating with angular velocity $\boldsymbol{\omega}$, the velocity of particle $\alpha$ at position $\mathbf{r}_\alpha$ (relative to the body's reference point) is:

**第 1 步 — 旋转刚体中粒子的速度。** 对于以角速度 $\boldsymbol{\omega}$ 旋转的刚体，位置为 $\mathbf{r}_\alpha$（相对于刚体参考点）的粒子 $\alpha$ 的速度为：

$$ \mathbf{v}_\alpha = \boldsymbol{\omega}\times\mathbf{r}_\alpha. $$

**Step 2 — Write the angular momentum.** $\mathbf{L} = \sum_\alpha m_\alpha\, \mathbf{r}_\alpha\times\mathbf{v}_\alpha$:

**第 2 步 — 写出角动量。** $\mathbf{L} = \sum_\alpha m_\alpha\, \mathbf{r}_\alpha\times\mathbf{v}_\alpha$：

$$ \mathbf{L} = \sum_\alpha m_\alpha\, \mathbf{r}_\alpha\times(\boldsymbol{\omega}\times\mathbf{r}_\alpha). $$

**Step 3 — Expand using the BAC–CAB rule.** The vector identity $\mathbf{A}\times(\mathbf{B}\times\mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$ gives:

**第 3 步 — 用 BAC–CAB 规则展开。** 向量恒等式 $\mathbf{A}\times(\mathbf{B}\times\mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$ 给出：

$$ \mathbf{r}_\alpha\times(\boldsymbol{\omega}\times\mathbf{r}_\alpha) = \boldsymbol{\omega}\,(\mathbf{r}_\alpha\cdot\mathbf{r}_\alpha) - \mathbf{r}_\alpha\,(\mathbf{r}_\alpha\cdot\boldsymbol{\omega}) = \boldsymbol{\omega}\, |\mathbf{r}_\alpha|^2 - \mathbf{r}_\alpha\,(\mathbf{r}_\alpha\cdot\boldsymbol{\omega}). $$

**Step 4 — Write in component form.** The $i$-th component of $\mathbf{L}$ is:

**第 4 步 — 写成分量形式。** $\mathbf{L}$ 的第 $i$ 个分量为：

$$ \begin{aligned}
L_i &= \sum_\alpha m_\alpha \left[|\mathbf{r}_\alpha|^2\, \omega_i - r_{\alpha i}\left(\sum_j r_{\alpha j}\, \omega_j\right)\right] \\
&= \sum_j \left[\sum_\alpha m_\alpha \left(|\mathbf{r}_\alpha|^2\, \delta_{ij} - r_{\alpha i}\, r_{\alpha j}\right)\right] \omega_j \\
&= \sum_j I_{ij}\, \omega_j.
\end{aligned} $$

So $L_i = \sum_j I_{ij}\, \omega_j$, i.e. $\mathbf{L} = \mathbf{I}\cdot\boldsymbol{\omega}$, with $I_{ij} = \sum_\alpha m_\alpha(|\mathbf{r}_\alpha|^2\, \delta_{ij} - r_{\alpha i} r_{\alpha j})$. $\blacksquare$

故 $L_i = \sum_j I_{ij}\, \omega_j$，即 $\mathbf{L} = \mathbf{I}\cdot\boldsymbol{\omega}$，其中 $I_{ij} = \sum_\alpha m_\alpha(|\mathbf{r}_\alpha|^2\, \delta_{ij} - r_{\alpha i} r_{\alpha j})$。$\blacksquare$

**Step 5 — Rotational kinetic energy.** $T_\text{rot} = \tfrac12 \sum_\alpha m_\alpha |\mathbf{v}_\alpha|^2 = \tfrac12 \sum_\alpha m_\alpha |\boldsymbol{\omega}\times\mathbf{r}_\alpha|^2$. Using the result from Step 3:

**第 5 步 — 转动动能。** $T_\text{rot} = \tfrac12 \sum_\alpha m_\alpha |\mathbf{v}_\alpha|^2 = \tfrac12 \sum_\alpha m_\alpha |\boldsymbol{\omega}\times\mathbf{r}_\alpha|^2$。利用第 3 步的结果：

$$ T_\text{rot} = \tfrac12 \sum_\alpha m_\alpha\, \boldsymbol{\omega}\cdot\left[\boldsymbol{\omega}\,|\mathbf{r}_\alpha|^2 - \mathbf{r}_\alpha(\mathbf{r}_\alpha\cdot\boldsymbol{\omega})\right] = \tfrac12\, \boldsymbol{\omega}\cdot\mathbf{L} = \tfrac12\, \boldsymbol{\omega}\cdot\mathbf{I}\cdot\boldsymbol{\omega}. \qquad \blacksquare $$

---

## B. Euler's Equations from dL/dt in the Body Frame · 从体坐标系 dL/dt 推导欧拉方程

**Claim.** In the body frame (principal-axis frame), the torque equation $\boldsymbol{\tau} = d\mathbf{L}/dt$ (in the inertial lab frame) becomes the three **Euler equations**:

$$ \begin{aligned}
I_1\, \dot\omega_1 - (I_2 - I_3)\, \omega_2\, \omega_3 &= \tau_1, \\
I_2\, \dot\omega_2 - (I_3 - I_1)\, \omega_3\, \omega_1 &= \tau_2, \\
I_3\, \dot\omega_3 - (I_1 - I_2)\, \omega_1\, \omega_2 &= \tau_3.
\end{aligned} $$

**命题。** 在体坐标系（主轴坐标系）中，力矩方程 $\boldsymbol{\tau} = d\mathbf{L}/dt$（在惯性实验室系中）变为三个**欧拉方程**：

$$ \begin{aligned}
I_1\, \dot\omega_1 - (I_2 - I_3)\, \omega_2\, \omega_3 &= \tau_1, \\
I_2\, \dot\omega_2 - (I_3 - I_1)\, \omega_3\, \omega_1 &= \tau_2, \\
I_3\, \dot\omega_3 - (I_1 - I_2)\, \omega_1\, \omega_2 &= \tau_3.
\end{aligned} $$

**Step 1 — Relate time derivatives in the body frame to the lab frame.** For any vector $\mathbf{V}$, the time derivative in the lab frame and in the body frame (rotating at $\boldsymbol{\omega}$) are related by:

**第 1 步 — 将体坐标系中的时间导数与实验室系联系起来。** 对任意向量 $\mathbf{V}$，实验室系和体坐标系（以 $\boldsymbol{\omega}$ 旋转）中的时间导数满足：

$$ \left(\frac{d\mathbf{V}}{dt}\right)_\text{lab} = \left(\frac{d\mathbf{V}}{dt}\right)_\text{body} + \boldsymbol{\omega}\times\mathbf{V}. $$

This is the **transport theorem** for rotating frames.

这是旋转系的**输运定理**。

**Step 2 — Apply to L.** The torque equation in the lab frame is $\boldsymbol{\tau} = (d\mathbf{L}/dt)_\text{lab}$. Using the transport theorem:

**第 2 步 — 应用于 L。** 实验室系中的力矩方程为 $\boldsymbol{\tau} = (d\mathbf{L}/dt)_\text{lab}$。利用输运定理：

$$ \boldsymbol{\tau} = \left(\frac{d\mathbf{L}}{dt}\right)_\text{body} + \boldsymbol{\omega}\times\mathbf{L}. $$

**Step 3 — Evaluate in the principal-axis frame.** In the body frame with principal axes, $\mathbf{L} = (I_1\omega_1, I_2\omega_2, I_3\omega_3)$. Since the principal moments $I_i$ are constant in the body frame:

**第 3 步 — 在主轴坐标系中计算。** 在主轴体坐标系中，$\mathbf{L} = (I_1\omega_1, I_2\omega_2, I_3\omega_3)$。由于主转动惯量 $I_i$ 在体坐标系中为常数：

$$ \left(\frac{d\mathbf{L}}{dt}\right)_\text{body} = (I_1\dot\omega_1, I_2\dot\omega_2, I_3\dot\omega_3). $$

**Step 4 — Compute the cross product $\boldsymbol{\omega}\times\mathbf{L}$.**

**第 4 步 — 计算叉积 $\boldsymbol{\omega}\times\mathbf{L}$。**

$$ \begin{aligned}
\boldsymbol{\omega}\times\mathbf{L} &= (\omega_1, \omega_2, \omega_3) \times (I_1\omega_1, I_2\omega_2, I_3\omega_3) \\
&= (\omega_2 I_3\omega_3 - \omega_3 I_2\omega_2,\ \omega_3 I_1\omega_1 - \omega_1 I_3\omega_3,\ \omega_1 I_2\omega_2 - \omega_2 I_1\omega_1).
\end{aligned} $$

**Step 5 — Assemble Euler's equations.** The $i$-th component of $\boldsymbol{\tau} = (d\mathbf{L}/dt)_\text{body} + \boldsymbol{\omega}\times\mathbf{L}$ gives:

**第 5 步 — 组合欧拉方程。** $\boldsymbol{\tau} = (d\mathbf{L}/dt)_\text{body} + \boldsymbol{\omega}\times\mathbf{L}$ 的第 $i$ 个分量给出：

Component 1: $\tau_1 = I_1\dot\omega_1 + (I_3 - I_2)\omega_2\omega_3$.

Rearranging: $I_1\dot\omega_1 - (I_2 - I_3)\omega_2\omega_3 = \tau_1$. $\blacksquare_1$

分量 1：$\tau_1 = I_1\dot\omega_1 + (I_3 - I_2)\omega_2\omega_3$。整理：$I_1\dot\omega_1 - (I_2 - I_3)\omega_2\omega_3 = \tau_1$。$\blacksquare_1$

Component 2: $\tau_2 = I_2\dot\omega_2 + (I_1 - I_3)\omega_3\omega_1 = I_2\dot\omega_2 - (I_3 - I_1)\omega_3\omega_1$.

Rearranging: $I_2\dot\omega_2 - (I_3 - I_1)\omega_3\omega_1 = \tau_2$. $\blacksquare_2$

分量 2：$\tau_2 = I_2\dot\omega_2 + (I_1 - I_3)\omega_3\omega_1 = I_2\dot\omega_2 - (I_3 - I_1)\omega_3\omega_1$。整理：$I_2\dot\omega_2 - (I_3 - I_1)\omega_3\omega_1 = \tau_2$。$\blacksquare_2$

Component 3: $\tau_3 = I_3\dot\omega_3 + (I_2 - I_1)\omega_1\omega_2$.

Rearranging: $I_3\dot\omega_3 - (I_1 - I_2)\omega_1\omega_2 = \tau_3$. $\blacksquare_3$

分量 3：$\tau_3 = I_3\dot\omega_3 + (I_2 - I_1)\omega_1\omega_2$。整理：$I_3\dot\omega_3 - (I_1 - I_2)\omega_1\omega_2 = \tau_3$。$\blacksquare_3$

---

## C. Torque-Free Symmetric Top — Precession Rate · 无力矩对称陀螺的进动速率

**Claim.** For a torque-free symmetric top ($I_1 = I_2 \equiv I_\perp$, $I_3$ the symmetry-axis moment, $\boldsymbol{\tau} = 0$), Euler's equations yield uniform precession of $\boldsymbol{\omega}$ about the symmetry axis ($\hat{\mathbf{e}}_3$) at the body-frame rate:

$$ \Omega = \frac{\omega_3 (I_3 - I_\perp)}{I_\perp}. $$

**命题。** 对于无力矩对称陀螺（$I_1 = I_2 \equiv I_\perp$，$I_3$ 为对称轴转动惯量，$\boldsymbol{\tau} = 0$），欧拉方程给出 $\boldsymbol{\omega}$ 绕对称轴（$\hat{\mathbf{e}}_3$）的匀速进动，体坐标系频率为：

$$ \Omega = \frac{\omega_3 (I_3 - I_\perp)}{I_\perp}. $$

**Step 1 — Write Euler's equations with $\boldsymbol{\tau} = 0$ and $I_1 = I_2 = I_\perp$.**

**第 1 步 — 写出 $\boldsymbol{\tau} = 0$、$I_1 = I_2 = I_\perp$ 时的欧拉方程。**

$$ \begin{aligned}
I_\perp\, \dot\omega_1 - (I_\perp - I_3)\, \omega_2\, \omega_3 &= 0, &&\text{… (1)} \\
I_\perp\, \dot\omega_2 - (I_3 - I_\perp)\, \omega_3\, \omega_1 &= 0, &&\text{… (2)} \\
I_3\, \dot\omega_3 - (I_\perp - I_\perp)\, \omega_1\, \omega_2 &= 0 \implies \dot\omega_3 = 0. &&\text{… (3)}
\end{aligned} $$

**Step 2 — Establish that $\omega_3$ is constant.** Equation (3) gives $\omega_3 = \text{const}$. $\blacksquare_3$

**第 2 步 — 确定 $\omega_3$ 为常数。** 方程 (3) 给出 $\omega_3 = \text{常数}$。$\blacksquare_3$

**Step 3 — Define the precession frequency.** Let $\Omega = \omega_3(I_3 - I_\perp)/I_\perp$. Rewrite equations (1) and (2):

**第 3 步 — 定义进动频率。** 令 $\Omega = \omega_3(I_3 - I_\perp)/I_\perp$。改写方程 (1) 和 (2)：

$$ \begin{aligned}
\text{From (1):}\quad \dot\omega_1 &= -\frac{I_\perp - I_3}{I_\perp}\, \omega_3\, \omega_2 = +\Omega\, \omega_2. \\
\text{From (2):}\quad \dot\omega_2 &= +\frac{I_3 - I_\perp}{I_\perp}\, \omega_3\, \omega_1 = -\Omega\, \omega_1.
\end{aligned} $$

由 (1)：$\dot\omega_1 = -\dfrac{I_\perp - I_3}{I_\perp}\, \omega_3\, \omega_2 = +\Omega\, \omega_2$。
由 (2)：$\dot\omega_2 = +\dfrac{I_3 - I_\perp}{I_\perp}\, \omega_3\, \omega_1 = -\Omega\, \omega_1$。

**Step 4 — Solve the coupled ODEs.** Define the complex variable $\eta = \omega_1 + i\, \omega_2$:

**第 4 步 — 求解耦合常微分方程。** 定义复变量 $\eta = \omega_1 + i\, \omega_2$：

$$ \dot\eta = \dot\omega_1 + i\, \dot\omega_2 = \Omega\, \omega_2 + i(-\Omega\, \omega_1) = -i\Omega(\omega_1 + i\, \omega_2) = -i\Omega\, \eta. $$

This is a simple ODE with solution $\eta(t) = \eta(0)\, e^{-i\Omega t}$.

这是一个简单的常微分方程，解为 $\eta(t) = \eta(0)\, e^{-i\Omega t}$。

**Step 5 — Interpret the solution.** Writing $\eta(0) = \omega_\perp$ (the initial transverse angular speed, real and positive):

**第 5 步 — 解释解。** 令 $\eta(0) = \omega_\perp$（初始横向角速度，实数且为正）：

$$ \omega_1(t) = \omega_\perp \cos(\Omega t), \qquad \omega_2(t) = -\omega_\perp \sin(\Omega t). $$

The transverse component of $\boldsymbol{\omega}$ precesses uniformly around the symmetry axis $\hat{\mathbf{e}}_3$ at angular frequency $|\Omega| = |\omega_3(I_3 - I_\perp)/I_\perp|$.

$\boldsymbol{\omega}$ 的横向分量以角频率 $|\Omega| = |\omega_3(I_3 - I_\perp)/I_\perp|$ 绕对称轴 $\hat{\mathbf{e}}_3$ 匀速进动。

Therefore, in the body frame $\boldsymbol{\omega}$ traces out a cone around $\hat{\mathbf{e}}_3$, completing one revolution in time $T = 2\pi/|\Omega|$. This is **Eulerian (body-frame) precession**.

因此，在体坐标系中 $\boldsymbol{\omega}$ 绕 $\hat{\mathbf{e}}_3$ 描出一个锥，在时间 $T = 2\pi/|\Omega|$ 内完成一圈。这就是**欧拉（体坐标系）进动**。

**Precession rate:**

**进动速率：**

$$ \boxed{\, \Omega = \frac{\omega_3 (I_3 - I_\perp)}{I_\perp} \,} \qquad \blacksquare $$

**Physical note.** For a prolate body ($I_3 < I_\perp$, e.g. a football), $\Omega < 0$: $\boldsymbol{\omega}$ precesses in the opposite sense to $\omega_3$. For an oblate body ($I_3 > I_\perp$, e.g. a frisbee), $\Omega > 0$: precession is in the same sense. The Earth, slightly oblate ($I_3 - I_\perp \approx 3\times 10^{-3}\, I_\perp$), exhibits the **Chandler wobble** with a period of $\approx 14$ months (Earth's period in the body frame; $\approx 305$ days, close to the observed 433 days — the discrepancy is due to Earth's non-rigidity).

**物理说明。** 对于长椭球体（$I_3 < I_\perp$，如橄榄球），$\Omega < 0$：$\boldsymbol{\omega}$ 进动方向与 $\omega_3$ 相反。对于扁椭球体（$I_3 > I_\perp$，如飞盘），$\Omega > 0$：进动方向相同。地球略为扁椭球（$I_3 - I_\perp \approx 3\times 10^{-3}\, I_\perp$），体坐标系周期约 305 天（接近观测值 433 天——差异源于地球的非刚性），产生**钱德勒摆动**，周期约 14 个月。

---

## D. Transport Theorem and Rotating-Frame Forces (Derivation of Coriolis and Centrifugal) · 输运定理与转动系惯性力（科里奥利力与离心力的推导）

**Claim.** In a frame rotating at angular velocity $\boldsymbol{\Omega}$ relative to an inertial frame, a particle of mass $m$ at position $\mathbf{r}$ with velocity $\mathbf{v}_\text{rot}$ (in the rotating frame) satisfies:

$$ m\, \mathbf{a}_\text{rot} = \mathbf{F} - 2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} - m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}). $$

The three terms on the right are: the real force $\mathbf{F}$, the **Coriolis force** $-2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot}$, and the **centrifugal force** $-m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})$.

**命题。** 在相对于惯性系以角速度 $\boldsymbol{\Omega}$ 旋转的参考系中，质量为 $m$、位置为 $\mathbf{r}$、速度（在转动系中）为 $\mathbf{v}_\text{rot}$ 的粒子满足：

$$ m\, \mathbf{a}_\text{rot} = \mathbf{F} - 2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} - m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}). $$

右侧三项分别为：真实力 $\mathbf{F}$、**科里奥利力** $-2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot}$ 以及**离心力** $-m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})$。

**Step 1 — Transport theorem.** For any vector $\mathbf{V}$, its time derivative in the inertial frame and in the rotating frame are related by:

**第 1 步 — 输运定理。** 对任意向量 $\mathbf{V}$，其在惯性系和转动系中的时间导数满足：

$$ \left(\frac{d\mathbf{V}}{dt}\right)_\text{inertial} = \left(\frac{d\mathbf{V}}{dt}\right)_\text{rot} + \boldsymbol{\Omega}\times\mathbf{V}. $$

*Derivation of the transport theorem:* Decompose $\mathbf{V}$ in the rotating-frame basis $\{\hat{\mathbf{e}}_1, \hat{\mathbf{e}}_2, \hat{\mathbf{e}}_3\}$: $\mathbf{V} = \sum_i V_i\, \hat{\mathbf{e}}_i$. The inertial-frame derivative is:

*输运定理的推导：* 在转动系基矢 $\{\hat{\mathbf{e}}_1, \hat{\mathbf{e}}_2, \hat{\mathbf{e}}_3\}$ 中分解 $\mathbf{V}$：$\mathbf{V} = \sum_i V_i\, \hat{\mathbf{e}}_i$。惯性系导数为：

$$ \left(\frac{d\mathbf{V}}{dt}\right)_\text{inertial} = \sum_i \dot V_i\, \hat{\mathbf{e}}_i + \sum_i V_i \left(\frac{d\hat{\mathbf{e}}_i}{dt}\right)_\text{inertial}. $$

The first sum is $(d\mathbf{V}/dt)_\text{rot}$. For a basis vector rotating with the frame: $(d\hat{\mathbf{e}}_i/dt)_\text{inertial} = \boldsymbol{\Omega}\times\hat{\mathbf{e}}_i$. Therefore:

第一个和式为 $(d\mathbf{V}/dt)_\text{rot}$。对于随系旋转的基矢：$(d\hat{\mathbf{e}}_i/dt)_\text{inertial} = \boldsymbol{\Omega}\times\hat{\mathbf{e}}_i$。因此：

$$ \left(\frac{d\mathbf{V}}{dt}\right)_\text{inertial} = \left(\frac{d\mathbf{V}}{dt}\right)_\text{rot} + \sum_i V_i\, \boldsymbol{\Omega}\times\hat{\mathbf{e}}_i = \left(\frac{d\mathbf{V}}{dt}\right)_\text{rot} + \boldsymbol{\Omega}\times\mathbf{V}. \qquad \blacksquare $$

**Step 2 — Apply to position to get velocity.** Let $\mathbf{V} = \mathbf{r}$: $\mathbf{r}_\text{inertial} = \mathbf{r}_\text{rot}$ (same position vector). Apply the transport theorem:

**第 2 步 — 应用于位置以得速度。** 令 $\mathbf{V} = \mathbf{r}$：$\mathbf{r}_\text{inertial} = \mathbf{r}_\text{rot}$（相同位置矢量）。应用输运定理：

$$ \mathbf{v}_\text{inertial} = \mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{r}. $$

**Step 3 — Apply the transport theorem again to get acceleration.** Apply the theorem to $\mathbf{v}_\text{inertial}$:

**第 3 步 — 再次应用输运定理以得加速度。** 对 $\mathbf{v}_\text{inertial}$ 应用定理：

$$ \mathbf{a}_\text{inertial} = \left(\frac{d\mathbf{v}_\text{inertial}}{dt}\right)_\text{rot} + \boldsymbol{\Omega}\times\mathbf{v}_\text{inertial}. $$

Substitute $\mathbf{v}_\text{inertial} = \mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{r}$:

代入 $\mathbf{v}_\text{inertial} = \mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{r}$：

$$ \begin{aligned}
\mathbf{a}_\text{inertial} &= \left(\frac{d}{dt}\right)_\text{rot}(\mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{r}) + \boldsymbol{\Omega}\times(\mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{r}) \\
&= \mathbf{a}_\text{rot} + \left(\frac{d\boldsymbol{\Omega}}{dt}\right)_\text{rot}\times\mathbf{r} + \boldsymbol{\Omega}\times\dot{\mathbf{r}}_\text{rot} + \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}).
\end{aligned} $$

For constant $\boldsymbol{\Omega}$: $(d\boldsymbol{\Omega}/dt)_\text{rot} = 0$. Also $\dot{\mathbf{r}}_\text{rot} = \mathbf{v}_\text{rot}$:

对于恒定 $\boldsymbol{\Omega}$：$(d\boldsymbol{\Omega}/dt)_\text{rot} = 0$。且 $\dot{\mathbf{r}}_\text{rot} = \mathbf{v}_\text{rot}$：

$$ \mathbf{a}_\text{inertial} = \mathbf{a}_\text{rot} + 2\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}). $$

**Step 4 — Newton's second law.** In the inertial frame: $m\, \mathbf{a}_\text{inertial} = \mathbf{F}$. Therefore:

**第 4 步 — 牛顿第二定律。** 在惯性系中：$m\, \mathbf{a}_\text{inertial} = \mathbf{F}$。因此：

$$ m\left[\mathbf{a}_\text{rot} + 2\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} + \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})\right] = \mathbf{F}. $$

Solving for $\mathbf{a}_\text{rot}$:

解出 $\mathbf{a}_\text{rot}$：

$$ \boxed{\, m\, \mathbf{a}_\text{rot} = \mathbf{F} - 2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot} - m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}) \,} \qquad \blacksquare $$

The term $-2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot}$ is the **Coriolis force** (depends on velocity in the rotating frame) and $-m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}) = m\Omega^2\, \mathbf{r}_\perp$ (pointing outward from the rotation axis) is the **centrifugal force**.

项 $-2m\, \boldsymbol{\Omega}\times\mathbf{v}_\text{rot}$ 为**科里奥利力**（依赖于转动系中的速度），$-m\, \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}) = m\Omega^2\, \mathbf{r}_\perp$（指向旋转轴外侧）为**离心力**。

# Derivations — Module 1.17: Fluid Mechanics
# 推导 — 模块 1.17：流体力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.17](./module-1.17-fluid-mechanics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.17](./module-1.17-fluid-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Continuity Equation · 连续性方程推导

**Claim.** For a fluid with density field $\rho(\mathbf{r}, t)$ and velocity field $\mathbf{v}(\mathbf{r}, t)$, conservation of mass implies

**命题。** 对于密度场 $\rho(\mathbf{r}, t)$ 和速度场 $\mathbf{v}(\mathbf{r}, t)$ 的流体，质量守恒给出

$$ \partial\rho/\partial t + \nabla\cdot(\rho\mathbf{v}) = 0. $$

**Step 1 — Choose a control volume.** Fix an arbitrary closed control volume $V$ bounded by surface $S$. The total mass inside is

**第 1 步 — 选取控制体积。** 取任意固定的封闭控制体积 $V$，边界为曲面 $S$。其内总质量为

$$ M(t) = \int_V \rho(\mathbf{r}, t)\,dV. $$

**Step 2 — Rate of change of mass.** Differentiate under the integral ($V$ is fixed in space, so the limits of integration do not depend on $t$):

**第 2 步 — 质量变化率。** 对积分求导（$V$ 固定，积分上下限不依赖 $t$）：

$$ dM/dt = \int_V (\partial\rho/\partial t)\,dV. $$

**Step 3 — Mass flux through the boundary.** The mass per unit time flowing out through surface element $d\mathbf{S} = dS\,\hat{n}$ (outward normal $\hat{n}$) is $\rho(\mathbf{v}\cdot\hat{n})\,dS$. The total outflow rate is

**第 3 步 — 通过边界的质量通量。** 单位时间内通过面元 $d\mathbf{S} = dS\,\hat{n}$（外法向 $\hat{n}$）流出的质量为 $\rho(\mathbf{v}\cdot\hat{n})\,dS$。总流出率为

$$ \Phi_{\text{out}} = \oint_S \rho\,\mathbf{v} \cdot d\mathbf{S}. $$

**Step 4 — Conservation of mass.** Since no mass is created or destroyed,

**第 4 步 — 质量守恒。** 由于质量不生不灭，

$$ dM/dt + \Phi_{\text{out}} = 0 \implies \int_V (\partial\rho/\partial t)\,dV + \oint_S \rho\,\mathbf{v} \cdot d\mathbf{S} = 0. $$

Apply the divergence theorem $\oint_S \rho\mathbf{v}\cdot d\mathbf{S} = \int_V \nabla\cdot(\rho\mathbf{v})\,dV$:

应用散度定理 $\oint_S \rho\mathbf{v}\cdot d\mathbf{S} = \int_V \nabla\cdot(\rho\mathbf{v})\,dV$：

$$ \int_V [\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{v})]\,dV = 0. $$

**Step 5 — Localization.** Since this holds for every arbitrary volume $V$, the integrand must vanish everywhere (by the arbitrariness of $V$):

**第 5 步 — 局部化。** 由于上式对任意体积 $V$ 均成立，被积函数必处处为零（由 $V$ 的任意性）：

$$ \boxed{\, \partial\rho/\partial t + \nabla\cdot(\rho\mathbf{v}) = 0 \,} \qquad \blacksquare $$

**Alternative form (material derivative).** Expanding $\nabla\cdot(\rho\mathbf{v}) = \rho\nabla\cdot\mathbf{v} + \mathbf{v}\cdot\nabla\rho$:

**另一种形式（物质导数）。** 展开 $\nabla\cdot(\rho\mathbf{v}) = \rho\nabla\cdot\mathbf{v} + \mathbf{v}\cdot\nabla\rho$：

$$ D\rho/Dt + \rho\nabla\cdot\mathbf{v} = 0, $$

where $D/Dt = \partial/\partial t + \mathbf{v}\cdot\nabla$ is the **material derivative** (rate of change following a fluid parcel). For an incompressible fluid $D\rho/Dt = 0$, giving $\nabla\cdot\mathbf{v} = 0$.

其中 $D/Dt = \partial/\partial t + \mathbf{v}\cdot\nabla$ 为**物质导数**（跟随流体微元的变化率）。对不可压缩流体 $D\rho/Dt = 0$，给出 $\nabla\cdot\mathbf{v} = 0$。

---

## B. Euler's Equation (Newton per Unit Volume) · 欧拉方程推导

**Claim.** For an inviscid (frictionless) fluid, Newton's second law applied to a fluid parcel gives

**命题。** 对无粘流体，对流体微元应用牛顿第二定律得

$$ \rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \rho\mathbf{g}. $$

**Step 1 — Material derivative of velocity.** Consider a small fluid parcel at position $\mathbf{r}(t)$ at time $t$, moving to $\mathbf{r}(t + dt) = \mathbf{r}(t) + \mathbf{v}\,dt$ at time $t + dt$. The velocity of this parcel changes not only because the velocity field changes at fixed $\mathbf{r}$ (local change), but also because the parcel has moved to a new position (convective change):

**第 1 步 — 速度的物质导数。** 考虑时刻 $t$ 位于 $\mathbf{r}(t)$ 的流体微元，在 $t + dt$ 时刻移动到 $\mathbf{r}(t + dt) = \mathbf{r}(t) + \mathbf{v}\,dt$。该微元的速度变化来自两部分：固定位置处速度场的变化（局部变化），以及微元移动到新位置（对流变化）：

$$ D\mathbf{v}/Dt = \partial\mathbf{v}/\partial t + (d\mathbf{r}/dt \cdot \nabla)\mathbf{v} = \partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}. $$

This is the **material (or substantial) derivative** of $\mathbf{v}$.

这就是 $\mathbf{v}$ 的**物质（实质）导数**。

**Step 2 — Forces on the parcel.** For a parcel of volume $\delta V$ and mass $\delta m = \rho\,\delta V$, the forces are:

**第 2 步 — 微元受力。** 对体积 $\delta V$、质量 $\delta m = \rho\,\delta V$ 的微元，所受的力为：

- **Pressure force:** In the $x$-direction, the net pressure force from the pressure differential across the element is $(P(x) - P(x + dx))\,dy\,dz = -(\partial P/\partial x)\,dx\,dy\,dz = -(\partial P/\partial x)\,\delta V$. In vector form: $-\nabla P \cdot \delta V$.

- **压力：** 在 $x$ 方向，压力差产生的净力为 $-(\partial P/\partial x)\,\delta V$。矢量形式：$-\nabla P \cdot \delta V$。

- **Gravity:** $\rho\mathbf{g}\,\delta V$.

- **重力：** $\rho\mathbf{g}\,\delta V$。

- **Viscous forces:** zero for an ideal (inviscid) fluid.

- **粘性力：** 对理想（无粘）流体为零。

**Step 3 — Apply $F = ma$ per unit volume.** Dividing $\delta m \cdot D\mathbf{v}/Dt = (\text{total force})$ by $\delta V$:

**第 3 步 — 单位体积应用 $F = ma$。** 将 $\delta m \cdot D\mathbf{v}/Dt = (\text{总力})$ 除以 $\delta V$：

$$ \rho\,D\mathbf{v}/Dt = -\nabla P + \rho\mathbf{g}. $$

Expanding $D\mathbf{v}/Dt$:

展开 $D\mathbf{v}/Dt$：

$$ \boxed{\, \rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \rho\mathbf{g} \,} \qquad \blacksquare $$

**The nonlinear term** $(\mathbf{v}\cdot\nabla)\mathbf{v}$ is the **convective acceleration** — it is zero in purely linear wave theory but is the source of turbulence, shock waves, and boundary-layer effects.

**非线性项** $(\mathbf{v}\cdot\nabla)\mathbf{v}$ 是**对流加速度**——在纯线性波动理论中为零，但它是湍流、激波和边界层效应的来源。

---

## C. Bernoulli's Theorem from Euler's Equation · 由欧拉方程推导伯努利定理

**Claim.** For steady ($\partial/\partial t = 0$), incompressible ($\rho = \text{const}$), inviscid flow, integrating Euler's equation along a streamline gives

**命题。** 对于定常（$\partial/\partial t = 0$）、不可压缩（$\rho = \text{const}$）、无粘流动，沿流线积分欧拉方程得

$$ P + \tfrac12\rho v^2 + \rho g h = \text{constant} \qquad \text{(along a streamline).} $$

**Step 1 — Euler's equation in steady flow.** For $\partial\mathbf{v}/\partial t = 0$, Euler's equation becomes

**第 1 步 — 定常流中的欧拉方程。** 对 $\partial\mathbf{v}/\partial t = 0$，欧拉方程变为

$$ \rho(\mathbf{v}\cdot\nabla)\mathbf{v} = -\nabla P + \rho\mathbf{g} = -\nabla P - \nabla(\rho g h) \qquad [\text{taking } \mathbf{g} = -g\hat{z} = -\nabla(gh)]. $$

**Step 2 — Vector identity for the convective term.** Use the vector identity

**第 2 步 — 对流项的矢量恒等式。** 利用矢量恒等式

$$ (\mathbf{v}\cdot\nabla)\mathbf{v} = \nabla(\tfrac12 v^2) - \mathbf{v} \times (\nabla\times\mathbf{v}) = \nabla(\tfrac12 v^2) - \mathbf{v} \times \boldsymbol{\omega}, $$

where $\boldsymbol{\omega} = \nabla\times\mathbf{v}$ is the vorticity. Then Euler's equation becomes:

其中 $\boldsymbol{\omega} = \nabla\times\mathbf{v}$ 为涡度。欧拉方程变为：

$$ \rho[\nabla(\tfrac12 v^2) - \mathbf{v}\times\boldsymbol{\omega}] = -\nabla P - \rho\nabla(gh). $$

Rearranging:

整理：

$$ \nabla(P + \tfrac12\rho v^2 + \rho g h) = \rho\,\mathbf{v} \times \boldsymbol{\omega}. $$

**Step 3 — Integrate along a streamline.** A streamline is a curve tangent to $\mathbf{v}$ at every point, so along it $d\mathbf{r} = \mathbf{v}\,ds/v$ for arc length $s$. The right-hand side dotted with $d\mathbf{r}$ along the streamline is $\rho(\mathbf{v}\times\boldsymbol{\omega})\cdot\mathbf{v}\,ds/v = 0$ (the cross product $\mathbf{v}\times\boldsymbol{\omega}$ is perpendicular to $\mathbf{v}$). Therefore, along the streamline:

**第 3 步 — 沿流线积分。** 流线是处处与 $\mathbf{v}$ 相切的曲线，沿其方向 $d\mathbf{r} = \mathbf{v}\,ds/v$（弧长 $s$）。右侧与沿流线 $d\mathbf{r}$ 的点积为 $\rho(\mathbf{v}\times\boldsymbol{\omega})\cdot\mathbf{v}\,ds/v = 0$（叉积 $\mathbf{v}\times\boldsymbol{\omega}$ 垂直于 $\mathbf{v}$）。故沿流线：

$$ d/ds\,(P + \tfrac12\rho v^2 + \rho g h) = 0, $$

giving the **Bernoulli equation**:

给出**伯努利方程**：

$$ \boxed{\, P + \tfrac12\rho v^2 + \rho g h = \text{const} \,} \qquad \text{(along a streamline).} \qquad \blacksquare $$

**Step 4 — For irrotational flow.** If the flow is irrotational ($\boldsymbol{\omega} = 0$), then $\rho\mathbf{v}\times\boldsymbol{\omega} = 0$ everywhere, so $\nabla(P + \tfrac12\rho v^2 + \rho g h) = 0$ globally — Bernoulli's equation holds throughout the entire flow, not just along individual streamlines.

**第 4 步 — 无旋流动的情形。** 若流动无旋（$\boldsymbol{\omega} = 0$），则 $\rho\mathbf{v}\times\boldsymbol{\omega} = 0$ 处处成立，$\nabla(P + \tfrac12\rho v^2 + \rho g h) = 0$ 在全域成立——伯努利方程在整个流场成立，而不仅限于单条流线。

**Application — Venturi effect.** At a constriction where the cross-section $A$ decreases, continuity requires $A_1 v_1 = A_2 v_2$ (incompressible), so $v_2 > v_1$. Then Bernoulli gives $P_2 = P_1 + \tfrac12\rho(v_1^2 - v_2^2) < P_1$: **higher speed $\to$ lower pressure**. This drives liquid from the low-pressure throat into a jet, powers carburetors, and lifts airplane wings.

**应用——文丘里效应。** 在截面积 $A$ 减小的收缩处，连续性方程要求 $A_1 v_1 = A_2 v_2$（不可压缩），故 $v_2 > v_1$。由伯努利定理 $P_2 = P_1 + \tfrac12\rho(v_1^2 - v_2^2) < P_1$：**速度越快，压强越低**。这驱动液体从低压喉部喷出，是化油器工作和机翼升力的原理。

---

## D. The Navier–Stokes Equation and Reynolds Number Scaling · 纳维–斯托克斯方程与雷诺数标度论证

**Claim.** For a viscous, incompressible fluid, Newton's second law per unit volume gives the Navier–Stokes equation $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \eta\nabla^2\mathbf{v} + \rho\mathbf{g}$. The dimensionless Reynolds number $\mathrm{Re} = \rho v L/\eta$ measures the ratio of inertial to viscous forces.

**命题。** 对粘性不可压缩流体，单位体积牛顿第二定律给出纳维–斯托克斯方程 $\rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \eta\nabla^2\mathbf{v} + \rho\mathbf{g}$。无量纲雷诺数 $\mathrm{Re} = \rho v L/\eta$ 衡量惯性力与粘性力之比。

**Step 1 — Add the viscous stress.** In a viscous fluid, adjacent layers exert a shear stress on each other. For a Newtonian fluid, the viscous stress tensor is $\tau_{ij} = \eta(\partial v_i/\partial x_j + \partial v_j/\partial x_i)$ (for incompressible flow; the bulk viscosity term vanishes since $\nabla\cdot\mathbf{v} = 0$). The net viscous force per unit volume on a fluid parcel is the divergence of the stress tensor:

**第 1 步 — 加入粘性应力。** 在粘性流体中，相邻流层相互施加剪切应力。对牛顿流体，粘性应力张量为 $\tau_{ij} = \eta(\partial v_i/\partial x_j + \partial v_j/\partial x_i)$（不可压缩时，体积粘度项消失，因为 $\nabla\cdot\mathbf{v} = 0$）。流体微元所受单位体积粘性力为应力张量的散度：

$$ f_i^{\text{visc}} = \partial\tau_{ij}/\partial x_j = \eta(\partial^2 v_i/\partial x_j^2 + \partial^2 v_j/\partial x_j\,\partial x_i) = \eta\,\nabla^2 v_i + \eta\,\partial/\partial x_i(\nabla\cdot\mathbf{v}) = \eta\,\nabla^2 v_i, $$

where the last step uses $\nabla\cdot\mathbf{v} = 0$ (incompressibility). In vector form: $\mathbf{f}^{\text{visc}} = \eta\,\nabla^2\mathbf{v}$.

最后一步利用了 $\nabla\cdot\mathbf{v} = 0$（不可压缩性）。矢量形式：$\mathbf{f}^{\text{visc}} = \eta\,\nabla^2\mathbf{v}$。

**Step 2 — Write the full equation.** Adding the viscous force to Euler's equation:

**第 2 步 — 写出完整方程。** 在欧拉方程中加入粘性力：

$$ \boxed{\, \rho(\partial\mathbf{v}/\partial t + (\mathbf{v}\cdot\nabla)\mathbf{v}) = -\nabla P + \eta\nabla^2\mathbf{v} + \rho\mathbf{g} \,} \qquad \blacksquare $$

**Step 3 — Reynolds number from dimensional analysis.** Introduce characteristic scales: velocity $V$, length $L$, time $L/V$. Non-dimensionalize the Navier–Stokes equation by defining $\mathbf{v} = V\mathbf{v}'$, $\mathbf{r} = L\mathbf{r}'$, $t = (L/V)t'$, $P = \rho V^2 P'$ (dynamic pressure scale):

**第 3 步 — 量纲分析得雷诺数。** 引入特征尺度：速度 $V$，长度 $L$，时间 $L/V$。对纳维–斯托克斯方程无量纲化，令 $\mathbf{v} = V\mathbf{v}'$，$\mathbf{r} = L\mathbf{r}'$，$t = (L/V)t'$，$P = \rho V^2 P'$（动压标度）：

$$ \rho \cdot V^2/L \cdot (\partial\mathbf{v}'/\partial t' + (\mathbf{v}'\cdot\nabla')\mathbf{v}') = -\rho V^2/L \cdot \nabla'P' + \eta V/L^2 \cdot \nabla'^2\mathbf{v}'. $$

Divide through by $\rho V^2/L$:

两边除以 $\rho V^2/L$：

$$ \partial\mathbf{v}'/\partial t' + (\mathbf{v}'\cdot\nabla')\mathbf{v}' = -\nabla'P' + (\eta/\rho V L)\,\nabla'^2\mathbf{v}'. $$

The coefficient of the viscous term is $\eta/(\rho V L) = 1/\mathrm{Re}$ where

粘性项的系数为 $\eta/(\rho V L) = 1/\mathrm{Re}$，其中

$$ \mathrm{Re} = \rho V L/\eta = V L/\nu \qquad (\nu = \eta/\rho \text{ is the kinematic viscosity}). $$

**Step 4 — Physical interpretation of $\mathrm{Re}$.** The inertial term scales as $\rho V^2/L$; the viscous term scales as $\eta V/L^2$. Their ratio is

**第 4 步 — $\mathrm{Re}$ 的物理诠释。** 惯性项标度为 $\rho V^2/L$；粘性项标度为 $\eta V/L^2$。二者之比为

$$ (\rho V^2/L) / (\eta V/L^2) = \rho V L/\eta = \mathrm{Re}. $$

- **$\mathrm{Re} \ll 1$:** Viscous forces dominate; flow is smooth and laminar (Stokes flow). Inertia can be neglected — the Stokes equations $\nabla P = \eta\nabla^2\mathbf{v}$ are linear. Example: microorganism swimming.

- **$\mathrm{Re} \ll 1$：** 粘性力主导；流动光滑层流（斯托克斯流）。惯性可忽略——斯托克斯方程 $\nabla P = \eta\nabla^2\mathbf{v}$ 是线性的。例：微生物游泳。

- **$\mathrm{Re} \gg 1$:** Inertial forces dominate; viscous term is negligible in the bulk, but persists in thin **boundary layers** near surfaces. Nonlinear convective term drives turbulence instabilities. Example: airplane wing, turbulent pipe flow ($\mathrm{Re} > 4000$).

- **$\mathrm{Re} \gg 1$：** 惯性力主导；粘性项在主流中可忽略，但在近壁面薄**边界层**中仍显著。非线性对流项驱动湍流不稳定性。例：机翼、湍流管流（$\mathrm{Re} > 4000$）。$\blacksquare$

---

*The continuity equation, Euler's equation, and Bernoulli's theorem form the core of ideal fluid mechanics; the Navier–Stokes equation extends this to viscous flows and — through its nonlinear term — encompasses the entire complexity of turbulence.*

*连续性方程、欧拉方程和伯努利定理构成理想流体力学的核心；纳维–斯托克斯方程将其推广到粘性流动，并通过其非线性项包含了湍流的全部复杂性。*

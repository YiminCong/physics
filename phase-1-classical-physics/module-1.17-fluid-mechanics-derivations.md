# Derivations — Module 1.17: Fluid Mechanics
# 推导 — 模块 1.17：流体力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.17](./module-1.17-fluid-mechanics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.17](./module-1.17-fluid-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Continuity Equation · 连续性方程推导

**Claim.** For a fluid with density field ρ(**r**, t) and velocity field **v**(**r**, t), conservation of mass implies

**命题。** 对于密度场 ρ(**r**, t) 和速度场 **v**(**r**, t) 的流体，质量守恒给出

  ∂ρ/∂t + ∇·(ρ**v**) = 0.

**Step 1 — Choose a control volume.** Fix an arbitrary closed control volume V bounded by surface S. The total mass inside is

**第 1 步 — 选取控制体积。** 取任意固定的封闭控制体积 V，边界为曲面 S。其内总质量为

  M(t) = ∫_V ρ(**r**, t) dV.

**Step 2 — Rate of change of mass.** Differentiate under the integral (V is fixed in space, so the limits of integration do not depend on t):

**第 2 步 — 质量变化率。** 对积分求导（V 固定，积分上下限不依赖 t）：

  dM/dt = ∫_V (∂ρ/∂t) dV.

**Step 3 — Mass flux through the boundary.** The mass per unit time flowing out through surface element dS = dS n̂ (outward normal n̂) is ρ(**v**·n̂) dS. The total outflow rate is

**第 3 步 — 通过边界的质量通量。** 单位时间内通过面元 dS = dS n̂（外法向 n̂）流出的质量为 ρ(**v**·n̂) dS。总流出率为

  Φ_out = ∮_S ρ **v** · dS.

**Step 4 — Conservation of mass.** Since no mass is created or destroyed,

**第 4 步 — 质量守恒。** 由于质量不生不灭，

  dM/dt + Φ_out = 0   ⟹   ∫_V (∂ρ/∂t) dV + ∮_S ρ **v** · dS = 0.

Apply the divergence theorem ∮_S ρ**v**·dS = ∫_V ∇·(ρ**v**) dV:

应用散度定理 ∮_S ρ**v**·dS = ∫_V ∇·(ρ**v**) dV：

  ∫_V [∂ρ/∂t + ∇·(ρ**v**)] dV = 0.

**Step 5 — Localization.** Since this holds for every arbitrary volume V, the integrand must vanish everywhere (by the arbitrariness of V):

**第 5 步 — 局部化。** 由于上式对任意体积 V 均成立，被积函数必处处为零（由 V 的任意性）：

  **∂ρ/∂t + ∇·(ρv) = 0**. ∎

**Alternative form (material derivative).** Expanding ∇·(ρ**v**) = ρ∇·**v** + **v**·∇ρ:

**另一种形式（物质导数）。** 展开 ∇·(ρ**v**) = ρ∇·**v** + **v**·∇ρ：

  Dρ/Dt + ρ∇·**v** = 0,

where D/Dt = ∂/∂t + **v**·∇ is the **material derivative** (rate of change following a fluid parcel). For an incompressible fluid Dρ/Dt = 0, giving **∇·v = 0**.

其中 D/Dt = ∂/∂t + **v**·∇ 为**物质导数**（跟随流体微元的变化率）。对不可压缩流体 Dρ/Dt = 0，给出 **∇·v = 0**。

---

## B. Euler's Equation (Newton per Unit Volume) · 欧拉方程推导

**Claim.** For an inviscid (frictionless) fluid, Newton's second law applied to a fluid parcel gives

**命题。** 对无粘流体，对流体微元应用牛顿第二定律得

  ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇P + ρ**g**.

**Step 1 — Material derivative of velocity.** Consider a small fluid parcel at position **r**(t) at time t, moving to **r**(t + dt) = **r**(t) + **v** dt at time t + dt. The velocity of this parcel changes not only because the velocity field changes at fixed **r** (local change), but also because the parcel has moved to a new position (convective change):

**第 1 步 — 速度的物质导数。** 考虑时刻 t 位于 **r**(t) 的流体微元，在 t + dt 时刻移动到 **r**(t + dt) = **r**(t) + **v** dt。该微元的速度变化来自两部分：固定位置处速度场的变化（局部变化），以及微元移动到新位置（对流变化）：

  D**v**/Dt = ∂**v**/∂t + (d**r**/dt · ∇)**v** = ∂**v**/∂t + (**v**·∇)**v**.

This is the **material (or substantial) derivative** of **v**.

这就是 **v** 的**物质（实质）导数**。

**Step 2 — Forces on the parcel.** For a parcel of volume δV and mass δm = ρ δV, the forces are:

**第 2 步 — 微元受力。** 对体积 δV、质量 δm = ρ δV 的微元，所受的力为：

- **Pressure force:** In the x-direction, the net pressure force from the pressure differential across the element is (P(x) − P(x + dx)) dy dz = −(∂P/∂x) dx dy dz = −(∂P/∂x) δV. In vector form: −∇P · δV.

- **压力：** 在 x 方向，压力差产生的净力为 −(∂P/∂x) δV。矢量形式：−∇P · δV。

- **Gravity:** ρ**g** δV.

- **重力：** ρ**g** δV。

- **Viscous forces:** zero for an ideal (inviscid) fluid.

- **粘性力：** 对理想（无粘）流体为零。

**Step 3 — Apply F = ma per unit volume.** Dividing δm · D**v**/Dt = (total force) by δV:

**第 3 步 — 单位体积应用 F = ma。** 将 δm · D**v**/Dt = (总力) 除以 δV：

  ρ D**v**/Dt = −∇P + ρ**g**.

Expanding D**v**/Dt:

展开 D**v**/Dt：

  **ρ(∂v/∂t + (v·∇)v) = −∇P + ρg**. ∎

**The nonlinear term** (**v**·∇)**v** is the **convective acceleration** — it is zero in purely linear wave theory but is the source of turbulence, shock waves, and boundary-layer effects.

**非线性项** (**v**·∇)**v** 是**对流加速度**——在纯线性波动理论中为零，但它是湍流、激波和边界层效应的来源。

---

## C. Bernoulli's Theorem from Euler's Equation · 由欧拉方程推导伯努利定理

**Claim.** For steady (∂/∂t = 0), incompressible (ρ = const), inviscid flow, integrating Euler's equation along a streamline gives

**命题。** 对于定常（∂/∂t = 0）、不可压缩（ρ = const）、无粘流动，沿流线积分欧拉方程得

  P + ½ρv² + ρgh = constant   (along a streamline).

**Step 1 — Euler's equation in steady flow.** For ∂**v**/∂t = 0, Euler's equation becomes

**第 1 步 — 定常流中的欧拉方程。** 对 ∂**v**/∂t = 0，欧拉方程变为

  ρ(**v**·∇)**v** = −∇P + ρ**g** = −∇P − ∇(ρgh)   [taking **g** = −g ẑ = −∇(gh)].

**Step 2 — Vector identity for the convective term.** Use the vector identity

**第 2 步 — 对流项的矢量恒等式。** 利用矢量恒等式

  (**v**·∇)**v** = ∇(½v²) − **v** × (∇×**v**) = ∇(½v²) − **v** × **ω**,

where **ω** = ∇×**v** is the vorticity. Then Euler's equation becomes:

其中 **ω** = ∇×**v** 为涡度。欧拉方程变为：

  ρ[∇(½v²) − **v**×**ω**] = −∇P − ρ∇(gh).

Rearranging:

整理：

  ∇(P + ½ρv² + ρgh) = ρ **v** × **ω**.

**Step 3 — Integrate along a streamline.** A streamline is a curve tangent to **v** at every point, so along it **dr** = **v** ds/v for arc length s. The right-hand side dotted with d**r** along the streamline is ρ(**v**×**ω**)·**v** ds/v = 0 (the cross product **v**×**ω** is perpendicular to **v**). Therefore, along the streamline:

**第 3 步 — 沿流线积分。** 流线是处处与 **v** 相切的曲线，沿其方向 **dr** = **v** ds/v（弧长 s）。右侧与沿流线 d**r** 的点积为 ρ(**v**×**ω**)·**v** ds/v = 0（叉积 **v**×**ω** 垂直于 **v**）。故沿流线：

  d/ds (P + ½ρv² + ρgh) = 0,

giving the **Bernoulli equation**:

给出**伯努利方程**：

  **P + ½ρv² + ρgh = const**   (along a streamline). ∎

**Step 4 — For irrotational flow.** If the flow is irrotational (**ω** = 0), then ρ**v**×**ω** = 0 everywhere, so ∇(P + ½ρv² + ρgh) = 0 globally — Bernoulli's equation holds throughout the entire flow, not just along individual streamlines.

**第 4 步 — 无旋流动的情形。** 若流动无旋（**ω** = 0），则 ρ**v**×**ω** = 0 处处成立，∇(P + ½ρv² + ρgh) = 0 在全域成立——伯努利方程在整个流场成立，而不仅限于单条流线。

**Application — Venturi effect.** At a constriction where the cross-section A decreases, continuity requires A₁v₁ = A₂v₂ (incompressible), so v₂ > v₁. Then Bernoulli gives P₂ = P₁ + ½ρ(v₁² − v₂²) < P₁: **higher speed → lower pressure**. This drives liquid from the low-pressure throat into a jet, powers carburetors, and lifts airplane wings.

**应用——文丘里效应。** 在截面积 A 减小的收缩处，连续性方程要求 A₁v₁ = A₂v₂（不可压缩），故 v₂ > v₁。由伯努利定理 P₂ = P₁ + ½ρ(v₁² − v₂²) < P₁：**速度越快，压强越低**。这驱动液体从低压喉部喷出，是化油器工作和机翼升力的原理。

---

## D. The Navier–Stokes Equation and Reynolds Number Scaling · 纳维–斯托克斯方程与雷诺数标度论证

**Claim.** For a viscous, incompressible fluid, Newton's second law per unit volume gives the Navier–Stokes equation ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇P + η∇²**v** + ρ**g**. The dimensionless Reynolds number Re = ρvL/η measures the ratio of inertial to viscous forces.

**命题。** 对粘性不可压缩流体，单位体积牛顿第二定律给出纳维–斯托克斯方程 ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇P + η∇²**v** + ρ**g**。无量纲雷诺数 Re = ρvL/η 衡量惯性力与粘性力之比。

**Step 1 — Add the viscous stress.** In a viscous fluid, adjacent layers exert a shear stress on each other. For a Newtonian fluid, the viscous stress tensor is τ_{ij} = η(∂v_i/∂x_j + ∂v_j/∂x_i) (for incompressible flow; the bulk viscosity term vanishes since ∇·**v** = 0). The net viscous force per unit volume on a fluid parcel is the divergence of the stress tensor:

**第 1 步 — 加入粘性应力。** 在粘性流体中，相邻流层相互施加剪切应力。对牛顿流体，粘性应力张量为 τ_{ij} = η(∂v_i/∂x_j + ∂v_j/∂x_i)（不可压缩时，体积粘度项消失，因为 ∇·**v** = 0）。流体微元所受单位体积粘性力为应力张量的散度：

  f_i^{visc} = ∂τ_{ij}/∂x_j = η(∂²v_i/∂x_j² + ∂²v_j/∂x_j ∂x_i) = η ∇²v_i + η ∂/∂x_i(∇·**v**) = η ∇²v_i,

where the last step uses ∇·**v** = 0 (incompressibility). In vector form: **f**^{visc} = η ∇²**v**.

最后一步利用了 ∇·**v** = 0（不可压缩性）。矢量形式：**f**^{visc} = η ∇²**v**。

**Step 2 — Write the full equation.** Adding the viscous force to Euler's equation:

**第 2 步 — 写出完整方程。** 在欧拉方程中加入粘性力：

  **ρ(∂v/∂t + (v·∇)v) = −∇P + η∇²v + ρg**. ∎

**Step 3 — Reynolds number from dimensional analysis.** Introduce characteristic scales: velocity V, length L, time L/V. Non-dimensionalize the Navier–Stokes equation by defining **v** = V **v**′, **r** = L **r**′, t = (L/V) t′, P = ρV² P′ (dynamic pressure scale):

**第 3 步 — 量纲分析得雷诺数。** 引入特征尺度：速度 V，长度 L，时间 L/V。对纳维–斯托克斯方程无量纲化，令 **v** = V **v**′，**r** = L **r**′，t = (L/V) t′，P = ρV² P′（动压标度）：

  ρ · V²/L · (∂**v**′/∂t′ + (**v**′·∇′)**v**′) = −ρV²/L · ∇′P′ + ηV/L² · ∇′²**v**′.

Divide through by ρV²/L:

两边除以 ρV²/L：

  ∂**v**′/∂t′ + (**v**′·∇′)**v**′ = −∇′P′ + (η/ρVL) ∇′²**v**′.

The coefficient of the viscous term is η/(ρVL) = 1/Re where

粘性项的系数为 η/(ρVL) = 1/Re，其中

  **Re = ρVL/η = VL/ν**   (ν = η/ρ is the kinematic viscosity).

**Step 4 — Physical interpretation of Re.** The inertial term scales as ρV²/L; the viscous term scales as ηV/L². Their ratio is

**第 4 步 — Re 的物理诠释。** 惯性项标度为 ρV²/L；粘性项标度为 ηV/L²。二者之比为

  (ρV²/L) / (ηV/L²) = ρVL/η = Re.

- **Re ≪ 1:** Viscous forces dominate; flow is smooth and laminar (Stokes flow). Inertia can be neglected — the Stokes equations ∇P = η∇²**v** are linear. Example: microorganism swimming.

- **Re ≪ 1：** 粘性力主导；流动光滑层流（斯托克斯流）。惯性可忽略——斯托克斯方程 ∇P = η∇²**v** 是线性的。例：微生物游泳。

- **Re ≫ 1:** Inertial forces dominate; viscous term is negligible in the bulk, but persists in thin **boundary layers** near surfaces. Nonlinear convective term drives turbulence instabilities. Example: airplane wing, turbulent pipe flow (Re > 4000).

- **Re ≫ 1：** 惯性力主导；粘性项在主流中可忽略，但在近壁面薄**边界层**中仍显著。非线性对流项驱动湍流不稳定性。例：机翼、湍流管流（Re > 4000）。∎

---

*The continuity equation, Euler's equation, and Bernoulli's theorem form the core of ideal fluid mechanics; the Navier–Stokes equation extends this to viscous flows and — through its nonlinear term — encompasses the entire complexity of turbulence.*

*连续性方程、欧拉方程和伯努利定理构成理想流体力学的核心；纳维–斯托克斯方程将其推广到粘性流动，并通过其非线性项包含了湍流的全部复杂性。*

# Derivations — Module 7.1: The Equivalence Principle & Curved Spacetime
# 推导 — 模块 7.1：等效原理与弯曲时空

> Companion to [Module 7.1](./module-7.1-equivalence-principle-and-curved-spacetime.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.1](./module-7.1-equivalence-principle-and-curved-spacetime.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Gravitational Redshift from the Equivalence Principle · 从等效原理推导引力红移

**Claim.** A photon emitted with frequency ν at the bottom of a uniform gravitational field of strength g, and received at a height h above the emitter, is observed at a lower frequency ν′ = ν(1 − gh/c²), giving a fractional redshift Δν/ν = −gh/c².

**命题。** 在均匀引力场（场强 g）底部以频率 ν 发射的光子，在高于发射点 h 处被接收时，观测频率为 ν′ = ν(1 − gh/c²)，分数红移为 Δν/ν = −gh/c²。

**Step 1 — Replace gravity by acceleration (equivalence principle).** By the strong equivalence principle, a laboratory in a uniform gravitational field g (pointing downward) is physically equivalent, for all local experiments, to a laboratory that accelerates upward with acceleration a = g in empty space. We work in the accelerating frame.

**第 1 步 — 用加速度替换引力（等效原理）。** 根据强等效原理，处于均匀引力场 g（向下）中的实验室，对所有局域实验而言，在物理上等效于在空旷空间中以 a = g 向上加速运动的实验室。我们在加速参考系中分析问题。

**Step 2 — Set up the rocket geometry.** A rocket accelerates upward at a = g. Emitter E sits at the bottom of the rocket (floor), receiver R sits at the top, separated by proper length h (measured at one instant in the rocket frame). At t = 0, E emits a photon upward. The photon travels the length of the rocket.

**第 2 步 — 建立火箭几何。** 火箭以 a = g 向上加速。发射器 E 在火箭底部（地板），接收器 R 在顶部，瞬时固有间距为 h。在 t = 0 时刻，E 向上发射一个光子。光子穿越火箭全长。

**Step 3 — Time for the photon to traverse the rocket.** In an inertial frame instantaneously co-moving with the rocket at t = 0, the rocket is momentarily at rest. The photon, travelling at speed c, takes time Δt ≈ h/c to travel from floor to ceiling (to lowest order in v/c, which is valid provided the velocity gained during transit is small compared with c).

**第 3 步 — 光子穿越火箭的时间。** 在 t = 0 时刻与火箭瞬时共动的惯性系中，火箭暂时静止。光子以速度 c 运动，从地板到天花板所需时间为 Δt ≈ h/c（在 v/c 的最低阶近似下，在此期间获得的速度远小于 c，近似成立）。

**Step 4 — Velocity acquired by the receiver during transit.** During the time Δt = h/c the rocket accelerates at g, so the receiver R acquires an additional velocity (relative to the inertial frame) of

**第 4 步 — 接收器在传播期间获得的速度。** 在 Δt = h/c 的时间内，火箭以 g 加速，因此接收器 R 相对于该惯性系获得了额外速度

  Δv = g Δt = gh/c.

**Step 5 — Doppler shift.** Because R is moving away from E (in the direction of the photon's travel) at speed Δv = gh/c when the photon arrives, there is a classical Doppler redshift. To first order in Δv/c:

**第 5 步 — 多普勒频移。** 由于光子到达时，R 正以速度 Δv = gh/c 沿光子传播方向（远离 E）运动，产生经典多普勒红移。在 Δv/c 一阶近似下：

  ν′ = ν (1 − Δv/c) = ν (1 − gh/c²).

**Step 6 — Identify the redshift.** The fractional change in frequency is

**第 6 步 — 识别红移。** 频率的分数变化为

  Δν/ν ≡ (ν′ − ν)/ν = −gh/c².

The negative sign means the received frequency is lower: the photon is redshifted. The result is exact to first order in gh/c² and holds for any uniform (or locally uniform) gravitational field.

负号表示接收频率更低：光子发生红移。结果在 gh/c² 一阶精度下是精确的，适用于任何均匀（或局域均匀）的引力场。

**Step 7 — Express in terms of potential.** For a uniform field, the Newtonian potential difference between floor and ceiling is Δφ = φ(h) − φ(0) = gh (taking φ increasing upward). Therefore

**第 7 步 — 用势能表达。** 对于均匀场，地板到天花板的牛顿引力势差为 Δφ = φ(h) − φ(0) = gh（取 φ 向上增大）。因此

  Δν/ν = −Δφ/c²,

or equivalently the frequency ratio is ν′/ν = 1 + Δφ/c² (where Δφ > 0 for emission from a deeper potential to a shallower one). This is the **gravitational redshift formula**. ∎

等价地，频率比为 ν′/ν = 1 + Δφ/c²（其中从较深势向较浅势发射时 Δφ > 0）。这就是**引力红移公式**。∎

---

## B. Heuristic Estimate of Light Deflection · 光线偏折的启发式估算

**Claim.** A photon passing at impact parameter b past a mass M is deflected by an angle δ ≈ 2GM/(bc²) when only gravitational time dilation (i.e. the equivalence-principle result) is taken into account — the full GR result is exactly twice this, δ_GR = 4GM/(bc²), the factor-of-2 difference arising from spatial curvature.

**命题。** 以碰撞参数 b 掠过质量 M 的光子，若只考虑引力时间膨胀（即等效原理结果），偏折角为 δ ≈ 2GM/(bc²)——完整广义相对论结果恰好是此值的两倍，δ_GR = 4GM/(bc²)，系数 2 的差异来自空间曲率的贡献。

**Step 1 — The equivalence principle predicts bending.** Inside an accelerating rocket, a horizontal light beam (perpendicular to the acceleration) is deflected downward: in time Δt = L/c to traverse length L, the rocket moves up by ½g(Δt)² = gL²/(2c²), so the beam appears to curve downward. By equivalence, gravity must bend light too.

**第 1 步 — 等效原理预言光线弯曲。** 在加速火箭内，水平光束（垂直于加速方向）向下弯曲：在穿越长度 L 所需的时间 Δt = L/c 内，火箭向上运动 ½g(Δt)² = gL²/(2c²)，光束因此显得向下弯曲。根据等效原理，引力同样必须使光线弯曲。

**Step 2 — Model the gravitational field.** Treat the Sun (mass M) as a point mass. A photon travels along an approximately straight path with closest approach b (the impact parameter). The transverse (perpendicular to the path) component of the gravitational acceleration at position x along the path (with the Sun at x = 0) is

**第 2 步 — 建立引力场模型。** 将太阳（质量 M）视为点质量。光子沿近似直线路径运动，最近距离为 b（碰撞参数）。在路径上位置 x 处（太阳位于 x = 0），引力加速度的横向（垂直于路径）分量为

  g_⊥(x) = (GM/r²) sin θ = GM b / (b² + x²)^{3/2},

where r = (b² + x²)^{1/2} is the distance to the Sun and sin θ = b/r.

其中 r = (b² + x²)^{1/2} 是到太阳的距离，sin θ = b/r。

**Step 3 — Accumulate the deflection.** The total transverse impulse per unit mass (treating the photon as moving at speed c along x) is

**第 3 步 — 累积偏折。** 单位质量的总横向冲量（将光子视为以速度 c 沿 x 方向匀速运动）为

  Δv_⊥ = ∫_{-∞}^{+∞} g_⊥ (dx/c) = (GMb/c) ∫_{-∞}^{+∞} (b² + x²)^{-3/2} dx.

Evaluating the integral: let x = b tan θ, dx = b sec²θ dθ, (b² + x²)^{3/2} = b³ sec³θ. Then

计算积分：令 x = b tan θ，dx = b sec²θ dθ，(b² + x²)^{3/2} = b³ sec³θ，则

  ∫_{-∞}^{+∞} (b² + x²)^{-3/2} dx = (1/b²) ∫_{-π/2}^{π/2} cos θ dθ = 2/b².

Therefore Δv_⊥ = (GMb/c) · (2/b²) = 2GM/(bc).

因此 Δv_⊥ = (GMb/c) · (2/b²) = 2GM/(bc)。

**Step 4 — Compute the deflection angle.** The deflection angle is δ = Δv_⊥/c (ratio of transverse kick to forward speed):

**第 4 步 — 计算偏折角。** 偏折角为 δ = Δv_⊥/c（横向冲量与前向速度之比）：

  δ_Newt = 2GM/(bc²).

This is the **Newtonian (equivalence-principle) estimate**. The full GR calculation adds an equal contribution from spatial metric curvature, doubling the result:

这是**牛顿（等效原理）估算**值。完整广义相对论计算还有空间度规曲率的等量贡献，使结果加倍：

  δ_GR = 4GM/(bc²).

For the Sun: b = R_☉ ≈ 6.96 × 10⁸ m, M = M_☉ ≈ 1.99 × 10³⁰ kg, giving δ_GR ≈ 8.48 × 10⁻⁶ rad ≈ 1.75 arcseconds — confirmed by Eddington in 1919. ∎

对于太阳：b = R_☉ ≈ 6.96 × 10⁸ m，M = M_☉ ≈ 1.99 × 10³⁰ kg，得 δ_GR ≈ 8.48 × 10⁻⁶ rad ≈ 1.75 角秒——1919 年由爱丁顿证实。∎

---

## C. Gravitational Time Dilation: dτ = √(−g₀₀) dt · 引力时间膨胀：dτ = √(−g₀₀) dt

**Claim.** For a static observer (dx^i/dt = 0) in a spacetime with metric g_{μν}, the relationship between proper time τ and coordinate time t is dτ = √(−g₀₀) dt. In a weak Newtonian field g₀₀ = −(1 + 2φ/c²), this gives dτ = (1 + φ/c²) dt, so clocks run slower in deeper gravitational potentials.

**命题。** 对于时空度规为 g_{μν} 中的静止观察者（dx^i/dt = 0），固有时 τ 与坐标时 t 的关系为 dτ = √(−g₀₀) dt。在弱牛顿场 g₀₀ = −(1 + 2φ/c²) 中，dτ = (1 + φ/c²) dt，即引力势较深处的时钟走得更慢。

**Step 1 — Start from the invariant interval.** The proper time elapsed along a worldline is defined by

**第 1 步 — 从不变间隔出发。** 沿世界线的固有时由下式定义

  c² dτ² = −ds² = −g_{μν} dx^μ dx^ν.

**Step 2 — Apply the static-observer condition.** A static observer has dx^i = 0 (i = 1, 2, 3). All spatial differentials vanish, leaving only the time-time component:

**第 2 步 — 应用静止观察者条件。** 静止观察者满足 dx^i = 0（i = 1, 2, 3）。所有空间微分项消失，只剩时间-时间分量：

  c² dτ² = −g_{00} (dx^0)² = −g_{00} c² dt²,

where we used x^0 = ct (so dx^0 = c dt).

其中用到 x^0 = ct（故 dx^0 = c dt）。

**Step 3 — Solve for dτ.** Dividing both sides by c²:

**第 3 步 — 求解 dτ。** 两边除以 c²：

  dτ² = −g_{00} dt²   ⟹   dτ = √(−g_{00}) dt.

(Since g₀₀ < 0 for a physical, timelike metric, −g₀₀ > 0 and the square root is real.)

（由于物理类时度规 g₀₀ < 0，故 −g₀₀ > 0，平方根为实数。）

**Step 4 — Weak-field limit.** In the Newtonian limit, the metric perturbation due to a gravitational potential φ (with φ → 0 at infinity, φ < 0 near a mass) is h₀₀ = −2φ/c², giving

**第 4 步 — 弱场极限。** 在牛顿极限下，引力势 φ（无穷远处 φ → 0，质量附近 φ < 0）引起的度规扰动为 h₀₀ = −2φ/c²，给出

  g₀₀ = −(1 + 2φ/c²).

Therefore

因此

  dτ = √(1 + 2φ/c²) dt ≈ (1 + φ/c²) dt   (to first order in φ/c²).

**Step 5 — Physical interpretation.** Since φ < 0 near a massive body, we have dτ < dt: proper time runs slower than coordinate time. A clock at potential φ₁ (lower, more negative) runs at rate dτ₁/dt = 1 + φ₁/c², and a clock at φ₂ > φ₁ runs at rate dτ₂/dt = 1 + φ₂/c². The ratio of their rates is

**第 5 步 — 物理诠释。** 由于在大质量天体附近 φ < 0，故 dτ < dt：固有时比坐标时走得慢。势为 φ₁（较低，更负）处的时钟以速率 dτ₁/dt = 1 + φ₁/c² 走动，势为 φ₂ > φ₁ 处的时钟以速率 dτ₂/dt = 1 + φ₂/c² 走动。两者的速率之比为

  dτ₁/dτ₂ ≈ 1 + (φ₁ − φ₂)/c² < 1,

confirming that the clock in the deeper potential runs slow. For the GPS problem: φ_satellite − φ_surface = +g_eff · h with h ≈ 20 200 km, giving a rate difference of Δ(dτ)/dt ≈ +5.1 × 10⁻¹⁰ (≈ +45 μs/day), exactly matching the observed correction. ∎

这证实了势较深处的时钟走得更慢。对于 GPS 问题：φ_卫星 − φ_地面 = +g_eff · h，其中 h ≈ 20 200 km，速率差为 Δ(dτ)/dt ≈ +5.1 × 10⁻¹⁰（≈ +45 μs/天），与观测到的修正完全吻合。∎

---

## D. Self-consistency: The Redshift from the Metric · 自洽性：从度规推导红移

**Claim.** The gravitational redshift Δν/ν = Δφ/c² derived heuristically in Section A is also an exact consequence of the metric formula dτ = √(−g₀₀) dt derived in Section C, and both results are mutually consistent.

**命题。** A 节中启发式推导的引力红移 Δν/ν = Δφ/c² 也是 C 节中度规公式 dτ = √(−g₀₀) dt 的精确推论，两个结果相互一致。

**Step 1 — Frequency is the inverse of period.** The frequency ν measured by a static observer at position x is the inverse of the proper time between successive wave crests: ν = 1/dτ (in units where one period is the time interval between crests).

**第 1 步 — 频率是周期的倒数。** 位置 x 处的静止观察者测量的频率 ν 是连续波峰之间固有时的倒数：ν = 1/dτ（在一个周期等于波峰间时间间隔的单位中）。

**Step 2 — Coordinate-time interval is the same at both points.** For a static metric, the coordinate time Δt between crests is the same everywhere along the photon path (the metric coefficients do not depend on t, so a stationary wave pattern in coordinate time propagates self-similarly). Therefore Δt is the same at emission (position 1) and reception (position 2).

**第 2 步 — 坐标时间间隔在两点处相同。** 对于静态度规，波峰之间的坐标时间 Δt 沿光子路径处处相同（度规系数不依赖于 t，因此坐标时中的稳定波型以自相似方式传播）。因此 Δt 在发射点（位置 1）和接收点（位置 2）处相同。

**Step 3 — Relate proper-time intervals.** From dτ = √(−g₀₀) dt:

**第 3 步 — 关联固有时间隔。** 由 dτ = √(−g₀₀) dt：

  dτ₁ = √(−g₀₀(x₁)) Δt,    dτ₂ = √(−g₀₀(x₂)) Δt.

**Step 4 — Frequency ratio.** Since ν ∝ 1/dτ:

**第 4 步 — 频率比。** 由于 ν ∝ 1/dτ：

  ν₂/ν₁ = dτ₁/dτ₂ = √(−g₀₀(x₁)) / √(−g₀₀(x₂)).

In the weak-field limit, −g₀₀ ≈ 1 + 2φ/c²:

在弱场极限下，−g₀₀ ≈ 1 + 2φ/c²：

  ν₂/ν₁ ≈ (1 + φ₁/c²)/(1 + φ₂/c²) ≈ 1 + (φ₁ − φ₂)/c².

So Δν/ν ≡ (ν₂ − ν₁)/ν₁ ≈ (φ₁ − φ₂)/c² = −Δφ/c² (with Δφ = φ₂ − φ₁ > 0 for upward emission). This recovers the result of Section A exactly. The two derivation routes are consistent. ∎

故 Δν/ν ≡ (ν₂ − ν₁)/ν₁ ≈ (φ₁ − φ₂)/c² = −Δφ/c²（向上发射时 Δφ = φ₂ − φ₁ > 0）。这精确还原了 A 节的结果。两种推导途径完全一致。∎

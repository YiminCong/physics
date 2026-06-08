# Derivations — Module 1.5: Central Force & Kepler
# 推导 — 模块 1.5：有心力与开普勒定律

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.5](./module-1.5-central-force-kepler.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.5](./module-1.5-central-force-kepler.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Two-Body Reduction to One-Body with Reduced Mass · 二体问题化为约化质量单体问题

**Claim.** The two-body problem with positions r₁, r₂ and masses m₁, m₂ interacting through V(|r₁ − r₂|) separates into (i) free motion of the centre of mass, and (ii) one-body motion in V(r) with reduced mass μ = m₁m₂/(m₁ + m₂) and relative coordinate r = r₁ − r₂.

**命题。** 位置为 r₁、r₂，质量为 m₁、m₂，通过 V(|r₁ − r₂|) 相互作用的二体问题可分离为：(i) 质心的自由运动；(ii) 相对坐标 r = r₁ − r₂ 在势 V(r) 中以约化质量 μ = m₁m₂/(m₁ + m₂) 运动的单体问题。

**Step 1 — Define the coordinates.** Introduce the centre-of-mass position R and relative coordinate r:

**第 1 步 — 定义坐标。** 引入质心位置 R 和相对坐标 r：

  R = (m₁r₁ + m₂r₂)/(m₁ + m₂),   r = r₁ − r₂.

The inverse relations: r₁ = R + (m₂/M) r,  r₂ = R − (m₁/M) r,  where M = m₁ + m₂.

逆关系：r₁ = R + (m₂/M) r，r₂ = R − (m₁/M) r，其中 M = m₁ + m₂。

**Step 2 — Write the kinetic energy in new coordinates.** Compute ṙ₁ and ṙ₂:

**第 2 步 — 用新坐标写动能。** 计算 ṙ₁ 和 ṙ₂：

  ṙ₁ = Ṙ + (m₂/M) ṙ,   ṙ₂ = Ṙ − (m₁/M) ṙ.

The total kinetic energy T = ½m₁|ṙ₁|² + ½m₂|ṙ₂|²:

总动能 T = ½m₁|ṙ₁|² + ½m₂|ṙ₂|²：

  T = ½m₁|Ṙ + (m₂/M)ṙ|² + ½m₂|Ṙ − (m₁/M)ṙ|²
    = ½(m₁ + m₂)|Ṙ|² + ½ m₁(m₂/M)² |ṙ|² + ½ m₂(m₁/M)² |ṙ|²
      + (cross terms: m₁(m₂/M) − m₂(m₁/M)) Ṙ · ṙ.

The cross terms vanish because m₁(m₂/M) − m₂(m₁/M) = 0. The second and third terms combine:

交叉项消失，因为 m₁(m₂/M) − m₂(m₁/M) = 0。第二、三项合并：

  m₁(m₂/M)² + m₂(m₁/M)² = (m₁m₂/M²)(m₂ + m₁) = m₁m₂/M = μ.

Therefore:

因此：

  **T = ½M|Ṙ|² + ½μ|ṙ|².**

**Step 3 — Write the Lagrangian.** Since V depends only on r = |r|:

**第 3 步 — 写出拉格朗日量。** 由于 V 仅依赖 r = |r|：

  L = T − V = ½MṘ² + ½μṙ² − V(r).

The Lagrangian separates: the R degrees of freedom give free CM motion (∂L/∂R = 0 ⟹ MR̈ = 0), and the r degrees of freedom give a one-body problem:

拉格朗日量分离：R 自由度给出 CM 自由运动（∂L/∂R = 0 ⟹ MR̈ = 0），r 自由度给出单体问题：

  μr̈ = −∇ᵣV(r).

This is exactly Newton's equation for a particle of mass μ in potential V(r). ∎

这恰好是质量为 μ 的粒子在势 V(r) 中的牛顿方程。∎

---

## B. Effective Potential and Radial Equation · 有效势与径向方程

**Claim.** For a particle of mass μ moving under central force V(r), the radial motion is governed by the one-dimensional equation ½μṙ² + V_eff(r) = E, where V_eff(r) = V(r) + L²/(2μr²) and L = μr²φ̇ is the conserved angular momentum.

**命题。** 对于质量为 μ 的粒子在有心力 V(r) 下运动，径向运动由一维方程 ½μṙ² + V_eff(r) = E 控制，其中 V_eff(r) = V(r) + L²/(2μr²)，L = μr²φ̇ 为守恒角动量。

**Step 1 — Write kinetic energy in polar coordinates.** In the orbital plane:

**第 1 步 — 用极坐标写动能。** 在轨道平面内：

  T = ½μ(ṙ² + r²φ̇²).

**Step 2 — Eliminate φ̇ using angular momentum conservation.** From L = μr²φ̇:

**第 2 步 — 利用角动量守恒消去 φ̇。** 由 L = μr²φ̇：

  φ̇ = L/(μr²).

Substitute into T:

代入 T：

  T = ½μṙ² + ½μr² · L²/(μ²r⁴) = ½μṙ² + L²/(2μr²).

**Step 3 — Write the total energy.** E = T + V:

**第 3 步 — 写出总能量。** E = T + V：

  E = ½μṙ² + L²/(2μr²) + V(r) = ½μṙ² + V_eff(r),

where **V_eff(r) = V(r) + L²/(2μr²)**. The term L²/(2μr²) acts as a centrifugal barrier repelling the particle from the origin. ∎

其中 **V_eff(r) = V(r) + L²/(2μr²)**。项 L²/(2μr²) 作为离心势垒使粒子远离原点。∎

---

## C. Orbit Equation via Binet Substitution · 通过比内代换推导轨道方程

**Claim.** For the gravitational potential V(r) = −GMμ/r, the orbit equation in polar coordinates is the conic section r(φ) = p/(1 + ε cos φ), where p = L²/(GMμ²) is the semi-latus rectum and ε is the eccentricity determined by the energy.

**命题。** 对于引力势 V(r) = −GMμ/r，极坐标中的轨道方程为圆锥曲线 r(φ) = p/(1 + ε cos φ)，其中 p = L²/(GMμ²) 为半通径，ε 为由能量决定的离心率。

**Step 1 — Set up the orbit equation.** We want r as a function of φ. Use the Binet substitution u = 1/r. Compute dr/dt in terms of dφ/dt:

**第 1 步 — 建立轨道方程。** 我们求 r 作为 φ 的函数。使用比内代换 u = 1/r。用 dφ/dt 计算 dr/dt：

  ṙ = dr/dt = (dr/dφ)(dφ/dt) = (dr/dφ) · (L/(μr²)).

Since r = 1/u: dr/dφ = −(1/u²)(du/dφ) = −r²(du/dφ). Therefore:

由于 r = 1/u：dr/dφ = −(1/u²)(du/dφ) = −r²(du/dφ)。因此：

  ṙ = −r² (du/dφ) · L/(μr²) = −(L/μ)(du/dφ).

**Step 2 — Compute r̈.** Differentiate ṙ with respect to t:

**第 2 步 — 计算 r̈。** 对 ṙ 关于 t 求导：

  r̈ = −(L/μ)(d²u/dφ²)(dφ/dt) = −(L/μ)(d²u/dφ²)(Lu²/μ) = −(L²u²/μ²)(d²u/dφ²).

**Step 3 — Write the radial equation of motion.** From μ(r̈ − rφ̇²) = F(r) = −dV/dr = −GMμu²:

**第 3 步 — 写出径向运动方程。** 由 μ(r̈ − rφ̇²) = F(r) = −dV/dr = −GMμu²：

  μ[−(L²u²/μ²)(d²u/dφ²) − (1/u)(Lu²/μ)²] = −GMμu².

Simplify each term. The second term: −(1/u)(L²u⁴/μ²) = −L²u³/μ². Divide the entire equation by −μL²u²/μ²= −L²u²/μ:

化简每项。第二项：−(1/u)(L²u⁴/μ²) = −L²u³/μ²。将整个方程除以 −μL²u²/μ²= −L²u²/μ：

  d²u/dφ² + u = GMμ²/L².

**Step 4 — Solve the ODE.** This is a harmonic oscillator ODE with a constant forcing term. The general solution is:

**第 4 步 — 求解常微分方程。** 这是带常数强迫项的谐振子方程。通解为：

  u(φ) = GMμ²/L² + A cos(φ − φ₀).

Choose the orientation so that φ₀ = 0 (periapsis at φ = 0). Then u = (1/p)(1 + ε cos φ), where p = L²/(GMμ²) and ε = A p.

选取方向使得 φ₀ = 0（近心点在 φ = 0 处）。则 u = (1/p)(1 + ε cos φ)，其中 p = L²/(GMμ²)，ε = A p。

**Step 5 — Recover r(φ).** Since r = 1/u:

**第 5 步 — 还原 r(φ)。** 由于 r = 1/u：

  **r(φ) = p/(1 + ε cos φ).** ∎

  **r(φ) = p/(1 + ε cos φ)。** ∎

This is a **conic section** with focus at the origin, semi-latus rectum p, and eccentricity ε. It is an ellipse (ε < 1), parabola (ε = 1), or hyperbola (ε > 1).

这是以原点为焦点的**圆锥曲线**，半通径为 p，离心率为 ε。ε < 1 为椭圆，ε = 1 为抛物线，ε > 1 为双曲线。

---

## D. The Three Kepler Laws · 开普勒三定律

### D.1 Kepler's First Law — Elliptical Orbits · 第一定律——椭圆轨道

The orbit equation r = p/(1 + ε cos φ) is an ellipse for ε < 1, with the centre of force (Sun) at one focus. This was derived in Section C above. For bound orbits E < 0, the eccentricity is:

轨道方程 r = p/(1 + ε cos φ) 在 ε < 1 时为椭圆，力心（太阳）在一个焦点处。这已在第 C 节推导。对于束缚轨道 E < 0，离心率为：

  ε = √(1 + 2EL²/(G²M²μ³)).

When E < 0: ε < 1, confirming an ellipse. ∎

当 E < 0 时：ε < 1，确认为椭圆。∎

### D.2 Kepler's Second Law — Equal Areas in Equal Times · 第二定律——等面积定律

**Claim.** The line from the Sun to the planet sweeps equal areas in equal times: dA/dt = L/(2μ) = const.

**命题。** 从太阳到行星的连线在相等时间内扫过相等面积：dA/dt = L/(2μ) = 常数。

**Proof.** In time dt, the position vector r sweeps out a triangle of area dA = ½|r × dr| = ½|r × ṙ dt| = ½|r × ṙ| dt. Therefore:

**证明。** 在时间 dt 内，位置矢量 r 扫过面积 dA = ½|r × dr| = ½|r × ṙ dt| = ½|r × ṙ| dt。因此：

  dA/dt = ½|r × ṙ| = ½|L/μ| = L/(2μ) = const,

since L is conserved for a central force (proved in Module 1.2 derivations). ∎

由于 L 对有心力守恒（已在模块 1.2 推导中证明）。∎

### D.3 Kepler's Third Law — T² = 4π²a³/(GM) · 第三定律——T² = 4π²a³/(GM)

**Claim.** The orbital period T and semi-major axis a satisfy T² = 4π²a³/(GM).

**命题。** 轨道周期 T 与半长轴 a 满足 T² = 4π²a³/(GM)。

**Step 1 — Relate the period to the area.** The total area swept per orbit is the area of the ellipse: A_ellipse = πab, where a is the semi-major axis and b is the semi-minor axis. Using dA/dt = L/(2μ):

**第 1 步 — 将周期与面积联系起来。** 每个轨道扫过的总面积是椭圆面积：A_ellipse = πab，其中 a 为半长轴，b 为半短轴。利用 dA/dt = L/(2μ)：

  T = A_ellipse / (dA/dt) = πab / (L/(2μ)) = 2πμab/L.

**Step 2 — Express b and p in terms of a and ε.** For an ellipse with semi-major axis a and eccentricity ε:

**第 2 步 — 用 a 和 ε 表示 b 和 p。** 对于半长轴为 a、离心率为 ε 的椭圆：

  b = a√(1 − ε²),   p = b²/a = a(1 − ε²).

**Step 3 — Substitute into the period formula.**

**第 3 步 — 代入周期公式。**

  T = 2πμab/L = 2πμ · a · a√(1 − ε²) / L = 2πμa²√(1 − ε²) / L.

**Step 4 — Use the relation p = L²/(GMμ²).** From Step 2, p = a(1 − ε²), so:

**第 4 步 — 利用关系 p = L²/(GMμ²)。** 由第 2 步，p = a(1 − ε²)，故：

  L² = GMμ² p = GMμ² a(1 − ε²).

Therefore L = μ√(GMa(1 − ε²)).

因此 L = μ√(GMa(1 − ε²))。

**Step 5 — Compute T².** Substituting into Step 3:

**第 5 步 — 计算 T²。** 代入第 3 步：

  T = 2πμa²√(1 − ε²) / [μ√(GMa(1 − ε²))]
    = 2πa²√(1 − ε²) / √(GMa(1 − ε²))
    = 2πa² / √(GMa)
    = 2π a^{3/2} / √(GM).

Squaring:

平方：

  **T² = 4π² a³ / (GM).** ∎

  **T² = 4π² a³ / (GM)。** ∎

The period depends only on the semi-major axis and the total mass, independent of eccentricity and the planet's mass (since μ ≈ m_planet ≪ M_Sun).

周期只依赖于半长轴和总质量，与离心率和行星质量无关（因为 μ ≈ m_planet ≪ M_Sun）。

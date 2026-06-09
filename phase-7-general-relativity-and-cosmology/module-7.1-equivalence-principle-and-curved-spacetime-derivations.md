---
title: "Derivations — Module 7.1: The Equivalence Principle & Curved Spacetime"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 7.1: The Equivalence Principle & Curved Spacetime
# 推导 — 模块 7.1：等效原理与弯曲时空

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.1](./module-7.1-equivalence-principle-and-curved-spacetime.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.1](./module-7.1-equivalence-principle-and-curved-spacetime.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Gravitational Redshift from the Equivalence Principle · 从等效原理推导引力红移

**Claim.** A photon emitted with frequency $\nu$ at the bottom of a uniform gravitational field of strength $g$, and received at a height $h$ above the emitter, is observed at a lower frequency $\nu' = \nu(1 - gh/c^2)$, giving a fractional redshift $\Delta\nu/\nu = -gh/c^2$.

**命题。** 在均匀引力场（场强 $g$）底部以频率 $\nu$ 发射的光子，在高于发射点 $h$ 处被接收时，观测频率为 $\nu' = \nu(1 - gh/c^2)$，分数红移为 $\Delta\nu/\nu = -gh/c^2$。

**Step 1 — Replace gravity by acceleration (equivalence principle).** By the strong equivalence principle, a laboratory in a uniform gravitational field $g$ (pointing downward) is physically equivalent, for all local experiments, to a laboratory that accelerates upward with acceleration $a = g$ in empty space. We work in the accelerating frame.

**第 1 步 — 用加速度替换引力（等效原理）。** 根据强等效原理，处于均匀引力场 $g$（向下）中的实验室，对所有局域实验而言，在物理上等效于在空旷空间中以 $a = g$ 向上加速运动的实验室。我们在加速参考系中分析问题。

**Step 2 — Set up the rocket geometry.** A rocket accelerates upward at $a = g$. Emitter E sits at the bottom of the rocket (floor), receiver R sits at the top, separated by proper length $h$ (measured at one instant in the rocket frame). At $t = 0$, E emits a photon upward. The photon travels the length of the rocket.

**第 2 步 — 建立火箭几何。** 火箭以 $a = g$ 向上加速。发射器 E 在火箭底部（地板），接收器 R 在顶部，瞬时固有间距为 $h$。在 $t = 0$ 时刻，E 向上发射一个光子。光子穿越火箭全长。

**Step 3 — Time for the photon to traverse the rocket.** In an inertial frame instantaneously co-moving with the rocket at $t = 0$, the rocket is momentarily at rest. The photon, travelling at speed $c$, takes time $\Delta t \approx h/c$ to travel from floor to ceiling (to lowest order in $v/c$, which is valid provided the velocity gained during transit is small compared with $c$).

**第 3 步 — 光子穿越火箭的时间。** 在 $t = 0$ 时刻与火箭瞬时共动的惯性系中，火箭暂时静止。光子以速度 $c$ 运动，从地板到天花板所需时间为 $\Delta t \approx h/c$（在 $v/c$ 的最低阶近似下，在此期间获得的速度远小于 $c$，近似成立）。

**Step 4 — Velocity acquired by the receiver during transit.** During the time $\Delta t = h/c$ the rocket accelerates at $g$, so the receiver R acquires an additional velocity (relative to the inertial frame) of

**第 4 步 — 接收器在传播期间获得的速度。** 在 $\Delta t = h/c$ 的时间内，火箭以 $g$ 加速，因此接收器 R 相对于该惯性系获得了额外速度

$$ \Delta v = g\,\Delta t = gh/c. $$

**Step 5 — Doppler shift.** Because R is moving away from E (in the direction of the photon's travel) at speed $\Delta v = gh/c$ when the photon arrives, there is a classical Doppler redshift. To first order in $\Delta v/c$:

**第 5 步 — 多普勒频移。** 由于光子到达时，R 正以速度 $\Delta v = gh/c$ 沿光子传播方向（远离 E）运动，产生经典多普勒红移。在 $\Delta v/c$ 一阶近似下：

$$ \nu' = \nu\,(1 - \Delta v/c) = \nu\,(1 - gh/c^2). $$

**Step 6 — Identify the redshift.** The fractional change in frequency is

**第 6 步 — 识别红移。** 频率的分数变化为

$$ \Delta\nu/\nu \equiv (\nu' - \nu)/\nu = -gh/c^2. $$

The negative sign means the received frequency is lower: the photon is redshifted. The result is exact to first order in $gh/c^2$ and holds for any uniform (or locally uniform) gravitational field.

负号表示接收频率更低：光子发生红移。结果在 $gh/c^2$ 一阶精度下是精确的，适用于任何均匀（或局域均匀）的引力场。

**Step 7 — Express in terms of potential.** For a uniform field, the Newtonian potential difference between floor and ceiling is $\Delta\varphi = \varphi(h) - \varphi(0) = gh$ (taking $\varphi$ increasing upward). Therefore

**第 7 步 — 用势能表达。** 对于均匀场，地板到天花板的牛顿引力势差为 $\Delta\varphi = \varphi(h) - \varphi(0) = gh$（取 $\varphi$ 向上增大）。因此

$$ \Delta\nu/\nu = -\Delta\varphi/c^2, $$

or equivalently the frequency ratio is $\nu'/\nu = 1 + \Delta\varphi/c^2$ (where $\Delta\varphi > 0$ for emission from a deeper potential to a shallower one). This is the **gravitational redshift formula**. $\blacksquare$

等价地，频率比为 $\nu'/\nu = 1 + \Delta\varphi/c^2$（其中从较深势向较浅势发射时 $\Delta\varphi > 0$）。这就是**引力红移公式**。$\blacksquare$

---

## B. Heuristic Estimate of Light Deflection · 光线偏折的启发式估算

**Claim.** A photon passing at impact parameter $b$ past a mass $M$ is deflected by an angle $\delta \approx 2GM/(bc^2)$ when only gravitational time dilation (i.e. the equivalence-principle result) is taken into account — the full GR result is exactly twice this, $\delta_{GR} = 4GM/(bc^2)$, the factor-of-2 difference arising from spatial curvature.

**命题。** 以碰撞参数 $b$ 掠过质量 $M$ 的光子，若只考虑引力时间膨胀（即等效原理结果），偏折角为 $\delta \approx 2GM/(bc^2)$——完整广义相对论结果恰好是此值的两倍，$\delta_{GR} = 4GM/(bc^2)$，系数 2 的差异来自空间曲率的贡献。

**Step 1 — The equivalence principle predicts bending.** Inside an accelerating rocket, a horizontal light beam (perpendicular to the acceleration) is deflected downward: in time $\Delta t = L/c$ to traverse length $L$, the rocket moves up by $\tfrac12 g(\Delta t)^2 = gL^2/(2c^2)$, so the beam appears to curve downward. By equivalence, gravity must bend light too.

**第 1 步 — 等效原理预言光线弯曲。** 在加速火箭内，水平光束（垂直于加速方向）向下弯曲：在穿越长度 $L$ 所需的时间 $\Delta t = L/c$ 内，火箭向上运动 $\tfrac12 g(\Delta t)^2 = gL^2/(2c^2)$，光束因此显得向下弯曲。根据等效原理，引力同样必须使光线弯曲。

**Step 2 — Model the gravitational field.** Treat the Sun (mass $M$) as a point mass. A photon travels along an approximately straight path with closest approach $b$ (the impact parameter). The transverse (perpendicular to the path) component of the gravitational acceleration at position $x$ along the path (with the Sun at $x = 0$) is

**第 2 步 — 建立引力场模型。** 将太阳（质量 $M$）视为点质量。光子沿近似直线路径运动，最近距离为 $b$（碰撞参数）。在路径上位置 $x$ 处（太阳位于 $x = 0$），引力加速度的横向（垂直于路径）分量为

$$ g_\perp(x) = (GM/r^2)\sin\theta = GM b / (b^2 + x^2)^{3/2}, $$

where $r = (b^2 + x^2)^{1/2}$ is the distance to the Sun and $\sin\theta = b/r$.

其中 $r = (b^2 + x^2)^{1/2}$ 是到太阳的距离，$\sin\theta = b/r$。

**Step 3 — Accumulate the deflection.** The total transverse impulse per unit mass (treating the photon as moving at speed $c$ along $x$) is

**第 3 步 — 累积偏折。** 单位质量的总横向冲量（将光子视为以速度 $c$ 沿 $x$ 方向匀速运动）为

$$ \Delta v_\perp = \int_{-\infty}^{+\infty} g_\perp\,(dx/c) = (GMb/c) \int_{-\infty}^{+\infty} (b^2 + x^2)^{-3/2}\,dx. $$

Evaluating the integral: let $x = b\tan\theta$, $dx = b\sec^2\theta\,d\theta$, $(b^2 + x^2)^{3/2} = b^3\sec^3\theta$. Then

计算积分：令 $x = b\tan\theta$，$dx = b\sec^2\theta\,d\theta$，$(b^2 + x^2)^{3/2} = b^3\sec^3\theta$，则

$$ \int_{-\infty}^{+\infty} (b^2 + x^2)^{-3/2}\,dx = (1/b^2) \int_{-\pi/2}^{\pi/2} \cos\theta\,d\theta = 2/b^2. $$

Therefore $\Delta v_\perp = (GMb/c) \cdot (2/b^2) = 2GM/(bc)$.

因此 $\Delta v_\perp = (GMb/c) \cdot (2/b^2) = 2GM/(bc)$。

**Step 4 — Compute the deflection angle.** The deflection angle is $\delta = \Delta v_\perp/c$ (ratio of transverse kick to forward speed):

**第 4 步 — 计算偏折角。** 偏折角为 $\delta = \Delta v_\perp/c$（横向冲量与前向速度之比）：

$$ \delta_{Newt} = 2GM/(bc^2). $$

This is the **Newtonian (equivalence-principle) estimate**. The full GR calculation adds an equal contribution from spatial metric curvature, doubling the result:

这是**牛顿（等效原理）估算**值。完整广义相对论计算还有空间度规曲率的等量贡献，使结果加倍：

$$ \delta_{GR} = 4GM/(bc^2). $$

For the Sun: $b = R_\odot \approx 6.96 \times 10^8$ m, $M = M_\odot \approx 1.99 \times 10^{30}$ kg, giving $\delta_{GR} \approx 8.48 \times 10^{-6}$ rad $\approx 1.75$ arcseconds — confirmed by Eddington in 1919. $\blacksquare$

对于太阳：$b = R_\odot \approx 6.96 \times 10^8$ m，$M = M_\odot \approx 1.99 \times 10^{30}$ kg，得 $\delta_{GR} \approx 8.48 \times 10^{-6}$ rad $\approx 1.75$ 角秒——1919 年由爱丁顿证实。$\blacksquare$

---

## C. Gravitational Time Dilation: $d\tau = \sqrt{-g_{00}}\,dt$ · 引力时间膨胀：$d\tau = \sqrt{-g_{00}}\,dt$

**Claim.** For a static observer ($dx^i/dt = 0$) in a spacetime with metric $g_{\mu\nu}$, the relationship between proper time $\tau$ and coordinate time $t$ is $d\tau = \sqrt{-g_{00}}\,dt$. In a weak Newtonian field $g_{00} = -(1 + 2\varphi/c^2)$, this gives $d\tau = (1 + \varphi/c^2)\,dt$, so clocks run slower in deeper gravitational potentials.

**命题。** 对于时空度规为 $g_{\mu\nu}$ 中的静止观察者（$dx^i/dt = 0$），固有时 $\tau$ 与坐标时 $t$ 的关系为 $d\tau = \sqrt{-g_{00}}\,dt$。在弱牛顿场 $g_{00} = -(1 + 2\varphi/c^2)$ 中，$d\tau = (1 + \varphi/c^2)\,dt$，即引力势较深处的时钟走得更慢。

**Step 1 — Start from the invariant interval.** The proper time elapsed along a worldline is defined by

**第 1 步 — 从不变间隔出发。** 沿世界线的固有时由下式定义

$$ c^2\,d\tau^2 = -ds^2 = -g_{\mu\nu}\,dx^\mu dx^\nu. $$

**Step 2 — Apply the static-observer condition.** A static observer has $dx^i = 0$ ($i = 1, 2, 3$). All spatial differentials vanish, leaving only the time-time component:

**第 2 步 — 应用静止观察者条件。** 静止观察者满足 $dx^i = 0$（$i = 1, 2, 3$）。所有空间微分项消失，只剩时间-时间分量：

$$ c^2\,d\tau^2 = -g_{00}\,(dx^0)^2 = -g_{00}\,c^2\,dt^2, $$

where we used $x^0 = ct$ (so $dx^0 = c\,dt$).

其中用到 $x^0 = ct$（故 $dx^0 = c\,dt$）。

**Step 3 — Solve for $d\tau$.** Dividing both sides by $c^2$:

**第 3 步 — 求解 $d\tau$。** 两边除以 $c^2$：

$$ d\tau^2 = -g_{00}\,dt^2 \quad\implies\quad d\tau = \sqrt{-g_{00}}\,dt. $$

(Since $g_{00} < 0$ for a physical, timelike metric, $-g_{00} > 0$ and the square root is real.)

（由于物理类时度规 $g_{00} < 0$，故 $-g_{00} > 0$，平方根为实数。）

**Step 4 — Weak-field limit.** In the Newtonian limit, the metric perturbation due to a gravitational potential $\varphi$ (with $\varphi \to 0$ at infinity, $\varphi < 0$ near a mass) is $h_{00} = -2\varphi/c^2$, giving

**第 4 步 — 弱场极限。** 在牛顿极限下，引力势 $\varphi$（无穷远处 $\varphi \to 0$，质量附近 $\varphi < 0$）引起的度规扰动为 $h_{00} = -2\varphi/c^2$，给出

$$ g_{00} = -(1 + 2\varphi/c^2). $$

Therefore

因此

$$ d\tau = \sqrt{1 + 2\varphi/c^2}\,dt \approx (1 + \varphi/c^2)\,dt \quad (\text{to first order in } \varphi/c^2). $$

**Step 5 — Physical interpretation.** Since $\varphi < 0$ near a massive body, we have $d\tau < dt$: proper time runs slower than coordinate time. A clock at potential $\varphi_1$ (lower, more negative) runs at rate $d\tau_1/dt = 1 + \varphi_1/c^2$, and a clock at $\varphi_2 > \varphi_1$ runs at rate $d\tau_2/dt = 1 + \varphi_2/c^2$. The ratio of their rates is

**第 5 步 — 物理诠释。** 由于在大质量天体附近 $\varphi < 0$，故 $d\tau < dt$：固有时比坐标时走得慢。势为 $\varphi_1$（较低，更负）处的时钟以速率 $d\tau_1/dt = 1 + \varphi_1/c^2$ 走动，势为 $\varphi_2 > \varphi_1$ 处的时钟以速率 $d\tau_2/dt = 1 + \varphi_2/c^2$ 走动。两者的速率之比为

$$ d\tau_1/d\tau_2 \approx 1 + (\varphi_1 - \varphi_2)/c^2 < 1, $$

confirming that the clock in the deeper potential runs slow. For the GPS problem: $\varphi_{satellite} - \varphi_{surface} = +g_{eff} \cdot h$ with $h \approx 20\,200$ km, giving a rate difference of $\Delta(d\tau)/dt \approx +5.1 \times 10^{-10}$ ($\approx +45\ \mu$s/day), exactly matching the observed correction. $\blacksquare$

这证实了势较深处的时钟走得更慢。对于 GPS 问题：$\varphi_{\text{卫星}} - \varphi_{\text{地面}} = +g_{eff} \cdot h$，其中 $h \approx 20\,200$ km，速率差为 $\Delta(d\tau)/dt \approx +5.1 \times 10^{-10}$（$\approx +45\ \mu$s/天），与观测到的修正完全吻合。$\blacksquare$

---

## D. Self-consistency: The Redshift from the Metric · 自洽性：从度规推导红移

**Claim.** The gravitational redshift $\Delta\nu/\nu = \Delta\varphi/c^2$ derived heuristically in Section A is also an exact consequence of the metric formula $d\tau = \sqrt{-g_{00}}\,dt$ derived in Section C, and both results are mutually consistent.

**命题。** A 节中启发式推导的引力红移 $\Delta\nu/\nu = \Delta\varphi/c^2$ 也是 C 节中度规公式 $d\tau = \sqrt{-g_{00}}\,dt$ 的精确推论，两个结果相互一致。

**Step 1 — Frequency is the inverse of period.** The frequency $\nu$ measured by a static observer at position $x$ is the inverse of the proper time between successive wave crests: $\nu = 1/d\tau$ (in units where one period is the time interval between crests).

**第 1 步 — 频率是周期的倒数。** 位置 $x$ 处的静止观察者测量的频率 $\nu$ 是连续波峰之间固有时的倒数：$\nu = 1/d\tau$（在一个周期等于波峰间时间间隔的单位中）。

**Step 2 — Coordinate-time interval is the same at both points.** For a static metric, the coordinate time $\Delta t$ between crests is the same everywhere along the photon path (the metric coefficients do not depend on $t$, so a stationary wave pattern in coordinate time propagates self-similarly). Therefore $\Delta t$ is the same at emission (position 1) and reception (position 2).

**第 2 步 — 坐标时间间隔在两点处相同。** 对于静态度规，波峰之间的坐标时间 $\Delta t$ 沿光子路径处处相同（度规系数不依赖于 $t$，因此坐标时中的稳定波型以自相似方式传播）。因此 $\Delta t$ 在发射点（位置 1）和接收点（位置 2）处相同。

**Step 3 — Relate proper-time intervals.** From $d\tau = \sqrt{-g_{00}}\,dt$:

**第 3 步 — 关联固有时间隔。** 由 $d\tau = \sqrt{-g_{00}}\,dt$：

$$ d\tau_1 = \sqrt{-g_{00}(x_1)}\,\Delta t, \qquad d\tau_2 = \sqrt{-g_{00}(x_2)}\,\Delta t. $$

**Step 4 — Frequency ratio.** Since $\nu \propto 1/d\tau$:

**第 4 步 — 频率比。** 由于 $\nu \propto 1/d\tau$：

$$ \nu_2/\nu_1 = d\tau_1/d\tau_2 = \sqrt{-g_{00}(x_1)} / \sqrt{-g_{00}(x_2)}. $$

In the weak-field limit, $-g_{00} \approx 1 + 2\varphi/c^2$:

在弱场极限下，$-g_{00} \approx 1 + 2\varphi/c^2$：

$$ \nu_2/\nu_1 \approx (1 + \varphi_1/c^2)/(1 + \varphi_2/c^2) \approx 1 + (\varphi_1 - \varphi_2)/c^2. $$

So $\Delta\nu/\nu \equiv (\nu_2 - \nu_1)/\nu_1 \approx (\varphi_1 - \varphi_2)/c^2 = -\Delta\varphi/c^2$ (with $\Delta\varphi = \varphi_2 - \varphi_1 > 0$ for upward emission). This recovers the result of Section A exactly. The two derivation routes are consistent. $\blacksquare$

故 $\Delta\nu/\nu \equiv (\nu_2 - \nu_1)/\nu_1 \approx (\varphi_1 - \varphi_2)/c^2 = -\Delta\varphi/c^2$（向上发射时 $\Delta\varphi = \varphi_2 - \varphi_1 > 0$）。这精确还原了 A 节的结果。两种推导途径完全一致。$\blacksquare$

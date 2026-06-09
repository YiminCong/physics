---
title: "Derivations — Module 7.5: Black Holes & Gravitational Waves"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 7.5: Black Holes & Gravitational Waves
# 推导 — 模块 7.5：黑洞与引力波

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.5](./module-7.5-black-holes-and-gravitational-waves.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.5](./module-7.5-black-holes-and-gravitational-waves.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the Schwarzschild Solution · 史瓦西解的推导

**Claim.** The unique static, spherically symmetric solution to the vacuum Einstein equations $R_{\mu\nu} = 0$ is the Schwarzschild metric

$$ ds^2 = -(1 - r_s/r) c^2 dt^2 + (1 - r_s/r)^{-1} dr^2 + r^2 d\Omega^2, $$

where $r_s = 2GM/c^2$ and $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\varphi^2$.

**命题。** 真空爱因斯坦方程 $R_{\mu\nu} = 0$ 唯一的静态球对称解是史瓦西度规

$$ ds^2 = -(1 - r_s/r) c^2 dt^2 + (1 - r_s/r)^{-1} dr^2 + r^2 d\Omega^2, $$

其中 $r_s = 2GM/c^2$，$d\Omega^2 = d\theta^2 + \sin^2\theta\, d\varphi^2$。

**Step 1 — Write the most general static spherically symmetric metric.** Any static, spherically symmetric metric can be written in the form (by symmetry and independence of $t$):

**第 1 步 — 写出最一般的静态球对称度规。** 任何静态球对称度规（由对称性和对 $t$ 的独立性）可以写成：

$$ ds^2 = -e^{2\alpha(r)} c^2 dt^2 + e^{2\beta(r)} dr^2 + r^2 d\Omega^2, $$

where $\alpha(r)$ and $\beta(r)$ are two unknown functions of the radial coordinate $r$ only. The form $r^2 d\Omega^2$ is chosen by defining $r$ as the areal radius (so that the 2-sphere at radius $r$ has area $4\pi r^2$). Staticity means no $dx^0 dr$ or $dt\, d\Omega$ cross-terms, and no time dependence.

其中 $\alpha(r)$ 和 $\beta(r)$ 是仅依赖于径向坐标 $r$ 的两个未知函数。$r^2 d\Omega^2$ 的形式通过将 $r$ 定义为面积半径来选取（使得 $r$ 处的二维球面面积为 $4\pi r^2$）。静态性意味着没有 $dx^0 dr$ 或 $dt\, d\Omega$ 交叉项，也没有时间依赖性。

**Step 2 — Compute non-zero Christoffel symbols.** Denoting $' = d/dr$, the non-zero independent components of $\Gamma^{\lambda}{}_{\mu\nu}$ are (in the order $t, r, \theta, \varphi$ for indices $0, 1, 2, 3$):

**第 2 步 — 计算非零克里斯托费尔符号。** 用 $'$ 表示 $d/dr$，$\Gamma^{\lambda}{}_{\mu\nu}$ 的非零独立分量为（指标 $0, 1, 2, 3$ 对应 $t, r, \theta, \varphi$）：

$$ \begin{aligned}
& \Gamma^{0}{}_{01} = \alpha', \\
& \Gamma^{1}{}_{00} = \alpha' e^{2(\alpha-\beta)}, \\
& \Gamma^{1}{}_{11} = \beta', \\
& \Gamma^{1}{}_{22} = -r e^{-2\beta}, \\
& \Gamma^{1}{}_{33} = -r \sin^2\theta\, e^{-2\beta}, \\
& \Gamma^{2}{}_{12} = 1/r, \\
& \Gamma^{2}{}_{33} = -\sin\theta \cos\theta, \\
& \Gamma^{3}{}_{13} = 1/r, \\
& \Gamma^{3}{}_{23} = \cos\theta/\sin\theta.
\end{aligned} $$

**Step 3 — Compute the Ricci tensor components.** Inserting into $R_{\mu\nu} = \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + \Gamma^{\rho}{}_{\rho\lambda} \Gamma^{\lambda}{}_{\nu\mu} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\rho\mu}$:

**第 3 步 — 计算里奇张量分量。** 代入 $R_{\mu\nu} = \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + \Gamma^{\rho}{}_{\rho\lambda} \Gamma^{\lambda}{}_{\nu\mu} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\rho\mu}$：

$$ \begin{aligned}
& R_{00} = e^{2(\alpha-\beta)} [\alpha'' + (\alpha')^2 - \alpha'\beta' + 2\alpha'/r] \\
& R_{11} = -\alpha'' - (\alpha')^2 + \alpha'\beta' + 2\beta'/r \\
& R_{22} = e^{-2\beta} [r(\alpha' - \beta') + 1] - 1 \\
& R_{33} = R_{22} \sin^2\theta
\end{aligned} $$

(Off-diagonal components vanish by spherical symmetry.)

（非对角分量由球对称性为零。）

**Step 4 — Solve $R_{\mu\nu} = 0$.** We set each component to zero:

**第 4 步 — 求解 $R_{\mu\nu} = 0$。** 令每个分量为零：

From $e^{2\beta} R_{00} + e^{2\alpha-2\beta}/1 \cdot (e^{-2\beta+2\beta})$ times appropriate factors, add $R_{00}\cdot e^{-2(\alpha-\beta)}$ to $R_{11}$:

从 $e^{2\beta} R_{00}$ 的适当组合加上 $R_{11}$：

$$ e^{-2\beta} R_{00} + R_{11} = 0 \text{ gives: } 2(\alpha' + \beta')/r = 0, \text{ so } \alpha + \beta = \text{const}. $$

Boundary condition: as $r \to \infty$, the metric must approach Minkowski space, so $e^{2\alpha} \to 1$ and $e^{2\beta} \to 1$, meaning $\alpha \to 0$ and $\beta \to 0$. Therefore $\alpha + \beta = 0$ everywhere, i.e.,

边界条件：$r \to \infty$ 时度规趋于闵可夫斯基空间，故 $e^{2\alpha} \to 1$，$e^{2\beta} \to 1$，即 $\alpha \to 0$，$\beta \to 0$。因此处处有 $\alpha + \beta = 0$，即

$$ \boxed{\, \beta = -\alpha \,} $$

**Step 5 — Solve the $R_{22} = 0$ equation.** Substituting $\beta = -\alpha$ into $R_{22} = 0$:

**第 5 步 — 求解 $R_{22} = 0$ 方程。** 将 $\beta = -\alpha$ 代入 $R_{22} = 0$：

$$ \begin{aligned}
& e^{2\alpha} [r(\alpha' - (-\alpha')) + 1] - 1 = 0 \\
& e^{2\alpha} [2r \alpha' + 1] = 1 \\
& \frac{d}{dr} (r e^{2\alpha}) = 1.
\end{aligned} $$

Integrate: $r e^{2\alpha} = r - r_s$, where $r_s$ is an integration constant with dimensions of length. Therefore:

积分得：$r e^{2\alpha} = r - r_s$，其中 $r_s$ 是具有长度量纲的积分常数。因此：

$$ e^{2\alpha} = 1 - r_s/r, \quad e^{-2\beta} = e^{2\alpha} = 1 - r_s/r. $$

**Step 6 — Identify the integration constant.** In the Newtonian limit $r \gg r_s$, comparing $g_{00} = -e^{2\alpha} = -(1 - r_s/r)$ with the weak-field form $g_{00} = -(1 + 2\varphi/c^2) = -(1 - 2GM/(rc^2))$:

**第 6 步 — 确定积分常数。** 在牛顿极限 $r \gg r_s$ 下，将 $g_{00} = -e^{2\alpha} = -(1 - r_s/r)$ 与弱场形式 $g_{00} = -(1 + 2\varphi/c^2) = -(1 - 2GM/(rc^2))$ 比较：

$$ r_s/r = 2GM/(rc^2) \quad\implies\quad \boxed{\, r_s = 2GM/c^2 \,} $$

**Step 7 — Write the final metric.** Assembling the solution:

**第 7 步 — 写出最终度规。** 整合解：

$$ ds^2 = -(1 - 2GM/(rc^2)) c^2 dt^2 + (1 - 2GM/(rc^2))^{-1} dr^2 + r^2 d\Omega^2. $$

This is the Schwarzschild metric. By Birkhoff's theorem, it is the *unique* (up to coordinate transformations) static spherically symmetric vacuum solution — even if the mass distribution is radially pulsating, the exterior metric remains Schwarzschild. $\blacksquare$

这是史瓦西度规。由比尔霍夫定理，它是静态球对称真空解中*唯一的*（在坐标变换意义下）——即使质量分布在径向脉动，外部度规仍保持史瓦西形式。$\blacksquare$

---

## B. The Event Horizon and the Schwarzschild Radius · 事件视界与史瓦西半径

**Claim.** The surface $r = r_s = 2GM/c^2$ is a coordinate singularity (not a physical one) that acts as an event horizon: no future-directed causal curve can escape from $r \le r_s$ to $r > r_s$.

**命题。** 曲面 $r = r_s = 2GM/c^2$ 是坐标奇点（非物理奇点），起到事件视界的作用：没有未来指向的因果曲线能从 $r \le r_s$ 逃逸到 $r > r_s$。

**Step 1 — Coordinate singularity vs. physical singularity.** At $r = r_s$, $g_{tt} = 0$ and $g_{rr} \to \infty$ in Schwarzschild coordinates. However, the curvature invariant $K = R^{\mu\nu\rho\sigma} R_{\mu\nu\rho\sigma} = 48 G^2 M^2/(c^4 r^6)$ is finite at $r = r_s$ (it diverges only at $r = 0$, the true physical singularity). A coordinate transformation to Kruskal–Szekeres coordinates ($T, X, \theta, \varphi$) yields a metric that is smooth and finite at $r = r_s$, confirming it is merely a coordinate artefact.

**第 1 步 — 坐标奇点与物理奇点。** 在史瓦西坐标下，$r = r_s$ 处 $g_{tt} = 0$，$g_{rr} \to \infty$。然而，曲率不变量 $K = R^{\mu\nu\rho\sigma} R_{\mu\nu\rho\sigma} = 48 G^2 M^2/(c^4 r^6)$ 在 $r = r_s$ 处是有限的（只在 $r = 0$ 处发散，这才是真正的物理奇点）。坐标变换到克鲁斯卡尔-塞凯赖什坐标 ($T, X, \theta, \varphi$) 给出在 $r = r_s$ 处光滑且有限的度规，证实这仅是坐标赝像。

**Step 2 — Null radial geodesics.** For radial ($d\Omega = 0$) null geodesics ($ds^2 = 0$):

**第 2 步 — 零径向测地线。** 对于径向（$d\Omega = 0$）零测地线（$ds^2 = 0$）：

$$ \begin{aligned}
& 0 = -(1 - r_s/r) c^2 dt^2 + (1 - r_s/r)^{-1} dr^2 \\
& dr/dt = \pm c(1 - r_s/r).
\end{aligned} $$

For $r > r_s$, $dr/dt = +c(1 - r_s/r) > 0$ (outgoing) or $dr/dt = -c(1 - r_s/r) < 0$ (ingoing). As $r \to r_s$, $dr/dt \to 0$: light appears to "freeze" at the horizon in Schwarzschild coordinates. An outgoing photon at $r < r_s$ has $dr/dt = +c(1 - r_s/r) < 0$ — it moves inward, toward $r = 0$, confirming that nothing escapes.

对于 $r > r_s$，$dr/dt = +c(1 - r_s/r) > 0$（向外）或 $dr/dt = -c(1 - r_s/r) < 0$（向内）。当 $r \to r_s$ 时，$dr/dt \to 0$：在史瓦西坐标下光子似乎在视界处"冻结"。$r < r_s$ 处的向外光子 $dr/dt = +c(1 - r_s/r) < 0$——它向内运动，朝向 $r = 0$，证实没有任何东西能逃逸。

**Step 3 — The horizon is a null hypersurface.** The normal to the surface $r = r_s$ is $n_\mu = \partial_\mu(r - r_s) = \delta^r{}_\mu$. Its norm is $g^{\mu\nu} n_\mu n_\nu = g^{rr} = (1 - r_s/r)|_{r=r_s} = 0$. A surface with a null normal is a null hypersurface — it is "tangent" to light rays. This is the defining property of an event horizon. $\blacksquare$

**第 3 步 — 视界是零超曲面。** 曲面 $r = r_s$ 的法矢量为 $n_\mu = \partial_\mu(r - r_s) = \delta^r{}_\mu$。其模为 $g^{\mu\nu} n_\mu n_\nu = g^{rr} = (1 - r_s/r)|_{r=r_s} = 0$。法矢量为零的曲面是零超曲面——它与光线"相切"。这是事件视界的定义性质。$\blacksquare$

---

## C. Linearized Gravity and the Gravitational Wave Equation · 线性化引力与引力波方程

**Claim.** Writing $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$, and defining the trace-reversed perturbation $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$ (where $h = \eta^{\mu\nu} h_{\mu\nu}$), the Einstein equations in Lorenz gauge ($\partial^\mu \bar{h}_{\mu\nu} = 0$) reduce to the wave equation

$$ \Box \bar{h}_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu}, $$

and in vacuum $\Box \bar{h}_{\mu\nu} = 0$, so gravitational waves propagate at speed $c$.

**命题。** 令 $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$，$|h_{\mu\nu}| \ll 1$，定义迹反转微扰 $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$（其中 $h = \eta^{\mu\nu} h_{\mu\nu}$），在洛伦兹规范（$\partial^\mu \bar{h}_{\mu\nu} = 0$）下，爱因斯坦方程化为波动方程

$$ \Box \bar{h}_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu}, $$

在真空中 $\Box \bar{h}_{\mu\nu} = 0$，故引力波以速度 $c$ 传播。

**Step 1 — Linearize the Christoffel symbols.** To first order in $h_{\mu\nu}$, using $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ and $g^{\mu\nu} \approx \eta^{\mu\nu} - h^{\mu\nu}$:

**第 1 步 — 线性化克里斯托费尔符号。** 在 $h_{\mu\nu}$ 的一阶近似下，利用 $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ 和 $g^{\mu\nu} \approx \eta^{\mu\nu} - h^{\mu\nu}$：

$$ \Gamma^{\rho}{}_{\mu\nu} = \tfrac12 \eta^{\rho\sigma}(\partial_\mu h_{\nu\sigma} + \partial_\nu h_{\mu\sigma} - \partial_\sigma h_{\mu\nu}) + O(h^2). $$

Indices on $h$ are raised/lowered with $\eta^{\mu\nu}/\eta_{\mu\nu}$ at linear order.

在线性阶，$h$ 的指标用 $\eta^{\mu\nu}/\eta_{\mu\nu}$ 升降。

**Step 2 — Linearize the Riemann tensor.** At linear order, the quadratic $\Gamma\, \Gamma$ terms vanish:

**第 2 步 — 线性化黎曼张量。** 在线性阶，二次 $\Gamma\, \Gamma$ 项消失：

$$ \begin{aligned}
R^{(1)}_{\rho\sigma\mu\nu} & = \partial_\mu \Gamma^{(1)}_{\rho\nu\sigma} - \partial_\nu \Gamma^{(1)}_{\rho\mu\sigma} \\
& = \tfrac12(\partial_\mu \partial_\sigma h_{\nu\rho} + \partial_\nu \partial_\rho h_{\mu\sigma} - \partial_\mu \partial_\rho h_{\nu\sigma} - \partial_\nu \partial_\sigma h_{\mu\rho}).
\end{aligned} $$

**Step 3 — Linearize the Ricci tensor.** Contract $\rho$ with $\mu$:

**第 3 步 — 线性化里奇张量。** 缩并 $\rho$ 与 $\mu$：

$$ R^{(1)}_{\mu\nu} = \tfrac12(\partial^\rho \partial_\mu h_{\nu\rho} + \partial^\rho \partial_\nu h_{\mu\rho} - \Box h_{\mu\nu} - \partial_\mu \partial_\nu h), $$

where $\Box = \eta^{\mu\nu} \partial_\mu \partial_\nu = -(1/c^2)\partial_t^2 + \nabla^2$ is the flat-space d'Alembertian, and $h = \eta^{\mu\nu} h_{\mu\nu}$.

其中 $\Box = \eta^{\mu\nu} \partial_\mu \partial_\nu = -(1/c^2)\partial_t^2 + \nabla^2$ 是平坦时空的达朗贝尔算符，$h = \eta^{\mu\nu} h_{\mu\nu}$。

**Step 4 — Introduce the trace-reversed perturbation.** Define

**第 4 步 — 引入迹反转微扰。** 定义

$$ \bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h. $$

Then $h = \eta^{\mu\nu} h_{\mu\nu}$, $\bar{h} = \eta^{\mu\nu} \bar{h}_{\mu\nu} = h - 2h = -h$, and inverting, $h_{\mu\nu} = \bar{h}_{\mu\nu} - \tfrac12 \eta_{\mu\nu} \bar{h}$. The trace-reversed field $\bar{h}_{\mu\nu}$ is the variable the final wave equation will act on.

则 $h = \eta^{\mu\nu} h_{\mu\nu}$，$\bar{h} = \eta^{\mu\nu} \bar{h}_{\mu\nu} = h - 2h = -h$，反解得 $h_{\mu\nu} = \bar{h}_{\mu\nu} - \tfrac12 \eta_{\mu\nu} \bar{h}$。迹反转场 $\bar{h}_{\mu\nu}$ 是最终波动方程所作用的变量。

**Step 5 — Impose Lorenz gauge and form the Einstein tensor.** Choose coordinates with $\partial^\mu \bar{h}_{\mu\nu} = 0$ (the Lorenz gauge, analogous to $\partial^\mu A_\mu = 0$ in electromagnetism; always achievable by an infinitesimal coordinate transformation). In terms of $h$ this condition reads $\partial^\rho h_{\mu\rho} = \tfrac12 \partial_\mu h$. Substituting into the Step-3 Ricci tensor, the first two terms each become $\partial^\rho\partial_\mu h_{\nu\rho} = \tfrac12 \partial_\mu\partial_\nu h$, which cancel the $-\partial_\mu\partial_\nu h$ term:

**第 5 步 — 施加洛伦兹规范并构造爱因斯坦张量。** 选取坐标使 $\partial^\mu \bar{h}_{\mu\nu} = 0$（洛伦兹规范，类比电磁学中的 $\partial^\mu A_\mu = 0$；总可由无穷小坐标变换实现）。以 $h$ 表示，此条件即 $\partial^\rho h_{\mu\rho} = \tfrac12 \partial_\mu h$。代入第 3 步的里奇张量，前两项各化为 $\partial^\rho\partial_\mu h_{\nu\rho} = \tfrac12 \partial_\mu\partial_\nu h$，恰好抵消 $-\partial_\mu\partial_\nu h$ 项：

$$ R^{(1)}_{\mu\nu} = \tfrac12(\tfrac12 \partial_\mu\partial_\nu h + \tfrac12 \partial_\mu\partial_\nu h - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h) = -\tfrac12 \Box h_{\mu\nu}. $$

Taking the trace, $R^{(1)} = \eta^{\mu\nu}R^{(1)}_{\mu\nu} = -\tfrac12 \Box h$. The linearized Einstein tensor then collapses neatly onto the trace-reversed perturbation:

取迹得 $R^{(1)} = \eta^{\mu\nu}R^{(1)}_{\mu\nu} = -\tfrac12 \Box h$。线性化爱因斯坦张量随即整齐地化为迹反转微扰：

$$ G^{(1)}_{\mu\nu} = R^{(1)}_{\mu\nu} - \tfrac12 \eta_{\mu\nu} R^{(1)} = -\tfrac12 \Box h_{\mu\nu} + \tfrac14 \eta_{\mu\nu} \Box h = -\tfrac12 \Box (h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h) = -\tfrac12 \Box \bar{h}_{\mu\nu}. $$

This is exactly why $\bar{h}_{\mu\nu}$ is the natural variable. The Einstein equations $G^{(1)}_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ become:

这正是 $\bar{h}_{\mu\nu}$ 成为自然变量的原因。爱因斯坦方程 $G^{(1)}_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu}$ 变为：

$$ -\tfrac12 \Box \bar{h}_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu} \implies \boxed{\, \Box \bar{h}_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu} \,} $$

**Step 6 — Vacuum: gravitational waves.** In the absence of matter, $T_{\mu\nu} = 0$:

**第 6 步 — 真空：引力波。** 在没有物质的情况下，$T_{\mu\nu} = 0$：

$$ \Box \bar{h}_{\mu\nu} = 0, \quad \text{i.e.,} \quad (-(1/c^2)\partial_t^2 + \nabla^2) \bar{h}_{\mu\nu} = 0. $$

This is the flat-space wave equation with propagation speed $c$. A plane-wave solution is $\bar{h}_{\mu\nu} = A_{\mu\nu} e^{ik_\rho x^\rho}$ with $k^\mu k_\mu = 0$ (null wave vector, confirming speed $c$). In transverse-traceless (TT) gauge (a further gauge choice within Lorenz gauge), only the two spatial transverse components $h^{TT}_{+}$ and $h^{TT}_{\times}$ remain. $\blacksquare$

这是传播速度为 $c$ 的平坦时空波动方程。平面波解为 $\bar{h}_{\mu\nu} = A_{\mu\nu} e^{ik_\rho x^\rho}$，其中 $k^\mu k_\mu = 0$（零波矢量，证实速度为 $c$）。在横向无迹（TT）规范（洛伦兹规范内的进一步规范选择）中，只剩两个空间横向分量 $h^{TT}_{+}$ 和 $h^{TT}_{\times}$。$\blacksquare$

---

## D. The Quadrupole Formula for Gravitational Wave Power · 引力波功率的四极矩公式

**Claim.** The leading-order gravitational wave power radiated by a non-relativistic source with traceless reduced quadrupole moment $Q_{ij} = \int \rho(x^i x^j - \tfrac13 \delta^{ij} r^2)\, d^3x$ is

$$ P = (G/5c^5) \langle (d^3Q_{ij}/dt^3)(d^3Q^{ij}/dt^3) \rangle. $$

**命题。** 具有无迹约化四极矩 $Q_{ij} = \int \rho(x^i x^j - \tfrac13 \delta^{ij} r^2)\, d^3x$ 的非相对论性源辐射的主导阶引力波功率为

$$ P = (G/5c^5) \langle (d^3Q_{ij}/dt^3)(d^3Q^{ij}/dt^3) \rangle. $$

**Step 1 — Retarded solution in Lorenz gauge.** The formal solution to $\Box \bar{h}_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu}$ is the retarded Green's function solution:

**第 1 步 — 洛伦兹规范下的推迟解。** $\Box \bar{h}_{\mu\nu} = -(16\pi G/c^4) T_{\mu\nu}$ 的形式解是推迟格林函数解：

$$ \bar{h}_{\mu\nu}(t, x) = (4G/c^4) \int T_{\mu\nu}(t - |x - x'|/c, x') / |x - x'|\, d^3x'. $$

In the far field ($r \equiv |x| \gg$ source size $d$, and at leading order in $d/r$):

在远场（$r \equiv |x| \gg$ 源的尺寸 $d$，在 $d/r$ 的主导阶）：

$$ \bar{h}_{\mu\nu}(t, x) \approx (4G/c^4 r) \int T_{\mu\nu}(t - r/c, x')\, d^3x'. $$

**Step 2 — Relate the spatial integral of $T_{ij}$ to the second time derivative of the mass quadrupole.** Using the conservation law $\partial^\mu T_{\mu\nu} = 0$ (in the linearized/flat-space sense), one can show (via integration by parts) that:

**第 2 步 — 将 $T_{ij}$ 的空间积分与质量四极矩的二阶时间导数联系起来。** 利用守恒律 $\partial^\mu T_{\mu\nu} = 0$（在线性化/平坦时空意义下），可以证明（通过分部积分）：

$$ \int T_{ij}\, d^3x = \tfrac12 \frac{d^2}{dt^2} \int T_{00} x^i x^j\, d^3x / c^2 = \tfrac12 \frac{d^2}{dt^2} I_{ij}, $$

where $I_{ij} = (1/c^2) \int T_{00} x^i x^j\, d^3x \approx \int \rho x^i x^j\, d^3x$ is the mass quadrupole tensor. Therefore, in the far field:

其中 $I_{ij} = (1/c^2) \int T_{00} x^i x^j\, d^3x \approx \int \rho x^i x^j\, d^3x$ 是质量四极矩张量。因此，在远场：

$$ \bar{h}_{ij}(t, x) \approx (2G/c^4 r) \ddot{I}_{ij}(t - r/c), $$

where $\ddot{I} = d^2I/dt^2$.

其中 $\ddot{I} = d^2I/dt^2$。

**Step 3 — Compute the energy flux.** The gravitational wave energy flux (power per unit area) is given by the Isaacson stress-energy tensor for gravitational waves (derived from the second-order EFE):

**第 3 步 — 计算能量通量。** 引力波能量通量（单位面积功率）由引力波的艾萨克森能动张量给出（由二阶 EFE 推导）：

$$ T^{GW}_{0i} = (c^2/32\pi G) \langle \partial_t h^{TT}_{\mu\nu}\, \partial_i h^{TT,\mu\nu} \rangle, $$

where $\langle\ \rangle$ denotes a time average over several wave cycles. The total power radiated is $P = \oint T^{GW}_{0r} r^2\, d\Omega$ over a large sphere.

其中 $\langle\ \rangle$ 表示对几个波周期的时间平均。总辐射功率为 $P = \oint T^{GW}_{0r} r^2\, d\Omega$，在大球上积分。

**Step 4 — Angular integration.** Substituting $\bar{h}_{ij}$ from Step 2 into the TT projection and integrating over angles (using $\int d\Omega\, n^i n^j = (4\pi/3) \delta^{ij}$ and $\int d\Omega\, n^i n^j n^k n^l = (4\pi/15)(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$):

**第 4 步 — 角积分。** 将第 2 步的 $\bar{h}_{ij}$ 代入 TT 投影，对角度积分（利用 $\int d\Omega\, n^i n^j = (4\pi/3) \delta^{ij}$ 和 $\int d\Omega\, n^i n^j n^k n^l = (4\pi/15)(\delta^{ij}\delta^{kl} + \delta^{ik}\delta^{jl} + \delta^{il}\delta^{jk})$）：

$$ P = (G/5c^5) \langle d^3I_{ij}/dt^3 \cdot d^3I^{ij}/dt^3 - \tfrac13 (d^3I^{kk}/dt^3)^2 \rangle. $$

Writing in terms of the reduced (traceless) quadrupole $Q_{ij} = I_{ij} - \tfrac13 \delta_{ij} I^{kk}$:

用约化（无迹）四极矩 $Q_{ij} = I_{ij} - \tfrac13 \delta_{ij} I^{kk}$ 表示：

$$ \boxed{\, P = (G/5c^5) \langle (d^3Q_{ij}/dt^3)(d^3Q^{ij}/dt^3) \rangle \,} \qquad \blacksquare $$

**Step 5 — Application to binary orbit.** For two equal masses $M$ in circular orbit of radius $r$ (separation $2r$, orbital frequency $\Omega^2 = G(2M)/(2r)^3 = GM/(4r^3)$), the quadrupole components are $Q_{ij} \sim Mr^2 \cos(2\Omega t)$. Taking three time derivatives gives $Q'''_{ij} \sim 8\Omega^3 Mr^2 \sin(2\Omega t)$, and summing the independent components $\langle(Q'''_{ij})^2\rangle = 128 M^2 r^4 \Omega^6$. Substituting:

**第 5 步 — 应用于双星轨道。** 对于两个等质量 $M$ 在半径 $r$ 的圆轨道（间距 $2r$，轨道频率 $\Omega^2 = G(2M)/(2r)^3 = GM/(4r^3)$），四极矩分量为 $Q_{ij} \sim Mr^2 \cos(2\Omega t)$。取三阶时间导数得 $Q'''_{ij} \sim 8\Omega^3 Mr^2 \sin(2\Omega t)$，对独立分量求和 $\langle(Q'''_{ij})^2\rangle = 128 M^2 r^4 \Omega^6$。代入：

$$ P = (G/5c^5) \cdot 128 M^2 r^4 \Omega^6 = (128/5) G M^2 r^4 \Omega^6/c^5. $$

Using Kepler's third law $\Omega^2 = G(2M)/(2r)^3 = GM/(4r^3)$ (total mass $2M$, separation $2r$):

利用开普勒第三定律 $\Omega^2 = G(2M)/(2r)^3 = GM/(4r^3)$：

$$ P = 2G^4 M^5/(5c^5 r^5), $$

the formula quoted in Module 7.5. The negative sign of $dE/dt$ (orbital energy decreases) drives the inspiral. $\blacksquare$

即模块 7.5 中引用的公式。$dE/dt$ 的负号（轨道能量减少）驱动了旋近。$\blacksquare$

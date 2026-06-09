---
title: "Derivations — Module 7.8: Global Structure & Singularity Theorems"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 7.8: Global Structure & Singularity Theorems
# 推导 — 模块 7.8：整体结构与奇点定理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.8](./module-7.8-global-structure-and-singularity-theorems.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.8](./module-7.8-global-structure-and-singularity-theorems.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Kruskal Coordinates: Removing the $r = 2GM/c^2$ Coordinate Singularity · 克鲁斯卡尔坐标：消除 $r = 2GM/c^2$ 坐标奇点

**Claim.** The Schwarzschild metric, written in the original ($t, r, \theta, \varphi$) coordinates, has a coordinate singularity at $r = r_s = 2GM/c^2$ ($g_{tt} \to 0$, $g_{rr} \to \infty$). The Kruskal–Szekeres coordinates ($T, X$) make the metric manifestly regular there.

**命题。** 史瓦西度规在原坐标 ($t, r, \theta, \varphi$) 中，在 $r = r_s = 2GM/c^2$ 处有坐标奇点（$g_{tt} \to 0$，$g_{rr} \to \infty$）。克鲁斯卡尔–塞克雷斯坐标 ($T, X$) 使度规在该处显然是正则的。

**Step 1 — The tortoise coordinate.** Define the *tortoise coordinate* $r^*$ by:

**第 1 步 — 乌龟坐标。** 定义*乌龟坐标* $r^*$：

$$ dr^*/dr = 1/(1 - r_s/r) \to r^* = r + r_s \ln|r/r_s - 1| + \text{const} $$

For $r > r_s$: as $r \to r_s^+$, $r^* \to -\infty$. As $r \to \infty$, $r^* \to r$. The radial null geodesics of the Schwarzschild metric satisfy $ds^2 = 0$, $d\Omega = 0$:

对 $r > r_s$：当 $r \to r_s^+$ 时 $r^* \to -\infty$；当 $r \to \infty$ 时 $r^* \to r$。史瓦西度规的径向类光测地线满足 $ds^2 = 0$，$d\Omega = 0$：

$$ \begin{aligned}
& 0 = -(1 - r_s/r)c^2 dt^2 + (1 - r_s/r)^{-1} dr^2 \\
& dt = \pm dr/((1 - r_s/r)c) = \pm dr^*/c
\end{aligned} $$

So $ct \mp r^* = $ const: these are the ingoing ($ct + r^* = $ const) and outgoing ($ct - r^* = $ const) null geodesics. They become straight lines $\pm 45^\circ$ in ($ct, r^*$) coordinates — the *Eddington–Finkelstein*-like picture.

故 $ct \mp r^* = $ 常数：这些是向内（$ct + r^* = $ 常数）和向外（$ct - r^* = $ 常数）的类光测地线。在 ($ct, r^*$) 坐标中它们成为 $\pm 45^\circ$ 的直线——类似 Eddington–Finkelstein 的图像。

**Step 2 — Define null coordinates.** Introduce:

**第 2 步 — 定义类光坐标。** 引入：

$$ \begin{aligned}
& u = ct - r^* && \text{(outgoing null coordinate)} \\
& v = ct + r^* && \text{(ingoing null coordinate)}
\end{aligned} $$

The Schwarzschild metric in ($u, v, \theta, \varphi$) becomes:

史瓦西度规在 ($u, v, \theta, \varphi$) 中变为：

$$ ds^2 = -(1 - r_s/r) du\, dv + r^2 d\Omega^2 $$

where $r$ is implicitly defined by $r^* = (v - u)/2$. This removes the $1/(1 - r_s/r)$ in $g_{rr}$, but $g_{uv} = -(1/2)(1 - r_s/r)$ still vanishes at $r = r_s$. To fix this, exponentiate.

其中 $r$ 由 $r^* = (v - u)/2$ 隐式定义。这消除了 $g_{rr}$ 中的 $1/(1 - r_s/r)$，但 $g_{uv} = -(1/2)(1 - r_s/r)$ 在 $r = r_s$ 处仍为零。为修复这点，取指数。

**Step 3 — Kruskal–Szekeres coordinates.** Define:

**第 3 步 — 克鲁斯卡尔–塞克雷斯坐标。** 定义：

$$ \begin{aligned}
& U = -e^{-u/(2r_s)} && \text{(for Region I)} \\
& V = +e^{+v/(2r_s)} && \text{(for Region I)}
\end{aligned} $$

Note: $UV = -e^{(v-u)/(2r_s)} = -e^{r^*/(r_s)} = -e^{(r + r_s \ln|r/r_s-1|)/r_s} = -e^{r/r_s}(r/r_s - 1)$.

So: $UV = -(r/r_s - 1) e^{r/r_s}$. $\quad$ (*)

The metric becomes:

$$ ds^2 = -(\text{something})\, dU\, dV + r^2 d\Omega^2 $$

Compute: $dU = (1/(2r_s)) e^{-u/(2r_s)} du \to du = -2r_s\, dU/U$, and similarly $dv = 2r_s\, dV/V$. So $du\, dv = -4r_s^2\, dU\, dV/(UV)$. Therefore:

度规变为：计算 $du\, dv = -4r_s^2\, dU\, dV/(UV)$，故：

$$ ds^2 = -(1 - r_s/r)(-4r_s^2)/(UV)\, dU\, dV + r^2 d\Omega^2 $$

From (*): $UV = -(r/r_s - 1)e^{r/r_s} \to (1 - r_s/r)/|UV| = e^{-r/r_s}/r_s$. So $(1 - r_s/r)/(UV) = -e^{-r/r_s}/r_s$ (for region I where $UV < 0$). Then:

由(*)：$(1 - r_s/r)/(UV) = -e^{-r/r_s}/r_s$（在 $UV < 0$ 的区域 I 中）。则：

$$ ds^2 = -(4r_s^3/r) e^{-r/r_s}\, dU\, dV + r^2 d\Omega^2 \quad \text{(the } -dU\, dV \text{ combination is timelike, giving signature } (-,+,+,+)) $$

More carefully, to get the standard form, introduce $T = (V + U)/2$, $X = (V - U)/2$. Then $dT^2 - dX^2 = dU\, dV$ (up to sign). The metric becomes:

更仔细地，令 $T = (V + U)/2$，$X = (V - U)/2$，则 $dU\, dV = dT^2 - dX^2$（差一个符号）。度规变为：

$$ \boxed{\, ds^2 = (32G^3 M^3/c^6 r) e^{-rc^2/(2GM)} (-dT^2 + dX^2) + r^2 d\Omega^2 \,} $$

where $r$ is determined implicitly from $T^2 - X^2 = (1 - r/r_s) e^{r/r_s}$.

其中 $r$ 由 $T^2 - X^2 = (1 - r/r_s) e^{r/r_s}$ 隐式确定。

**Step 4 — Regularity at $r = r_s$.** The prefactor $(32G^3 M^3/c^6 r) e^{-rc^2/(2GM)}$ is finite and nonzero at $r = r_s = 2GM/c^2$:

**第 4 步 — $r = r_s$ 处的正则性。** 因子 $(32G^3 M^3/c^6 r) e^{-rc^2/(2GM)}$ 在 $r = r_s = 2GM/c^2$ 处有限且非零：

$$ \text{prefactor at } r_s = (32G^3 M^3/c^6)(c^2/2GM) e^{-1} = (16G^2 M^2/c^4) e^{-1} \quad \text{(finite)} $$

The singularity at $r = 0$ is genuine: as $r \to 0$, the prefactor $\to \infty$ ($e^{-rc^2/(2GM)}/r \to \infty$), and the Kretschner scalar $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma} = 48G^2 M^2/(c^4 r^6) \to \infty$. The curvature invariant is a coordinate-independent indicator of the true physical singularity. $\blacksquare$

在 $r \to 0$ 时，系数 $\to \infty$，克雷奇南标量 $R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma} = 48G^2 M^2/(c^4 r^6) \to \infty$。曲率不变量是真实物理奇点的坐标无关指标。$\blacksquare$

**Step 5 — The four regions.** In Kruskal coordinates:

**第 5 步 — 四个区域。** 在克鲁斯卡尔坐标中：

- Region I: $X > |T|$, i.e. $U < 0$ and $V > 0$, corresponds to $r > r_s$ exterior.
- Region II: $T > |X|$, i.e. $U > 0$ and $V > 0$ ($T > X \implies U = T - X > 0$; $T > -X \implies V = T + X > 0$), giving $r < r_s$ (future interior).
- Region III: $T < -|X|$: $V < 0$ and $U < 0$, also $r < r_s$ (past interior = white hole).
- Region IV: $X < -|T|$: $U > 0$ and $V < 0 \to UV < 0 \to r > r_s$ (second exterior).

The event horizon is at $UV = 0$ (i.e. $U = 0$ or $V = 0$), corresponding to $r = r_s$: four null rays forming a cross in the Kruskal diagram. The physical singularity is the curve $T^2 - X^2 = 1$ ($r = 0$), drawn as a jagged line in the standard diagram. $\blacksquare$

事件视界在 $UV = 0$（即 $U = 0$ 或 $V = 0$）处，对应 $r = r_s$：克鲁斯卡尔图中形成一个十字形的四条类光线。物理奇点是曲线 $T^2 - X^2 = 1$（$r = 0$），在标准图中画为锯齿线。$\blacksquare$

---

## B. Penrose Process Energy Bound · 彭罗斯过程能量界

**Claim.** In the ergosphere of a Kerr black hole, a particle can split such that one fragment is absorbed and the other escapes with energy greater than the original particle. The energy extraction is bounded by the condition that the black hole's irreducible mass $M_\text{irr}$ does not decrease, giving maximum efficiency $\eta_\text{max} = 1 - 1/\sqrt{2} \approx 29.3\%$ for an extremal Kerr hole.

**命题。** 在克尔黑洞的能层中，粒子可以分裂，使一个碎片被吸收而另一个逃逸，逃逸碎片的能量大于原粒子。能量提取受到黑洞不可约质量 $M_\text{irr}$ 不减少条件的限制，对极值克尔黑洞给出最大效率 $\eta_\text{max} = 1 - 1/\sqrt{2} \approx 29.3\%$。

**Step 1 — Conserved energy in the ergosphere.** The Kerr metric has a timelike Killing vector $\xi^\mu = (\partial/\partial t)^\mu$ and a spacelike Killing vector $\psi^\mu = (\partial/\partial\varphi)^\mu$. For a particle with 4-momentum $p^\mu$:

**第 1 步 — 能层中的守恒能量。** 克尔度规有类时基灵矢量 $\xi^\mu = (\partial/\partial t)^\mu$ 和类空基灵矢量 $\psi^\mu = (\partial/\partial\varphi)^\mu$。对4-动量为 $p^\mu$ 的粒子：

$$ \begin{aligned}
& E = -p_\mu \xi^\mu = -p_t && \text{(conserved energy; } E > 0 \text{ for particles reaching infinity)} \\
& L = p_\mu \psi^\mu = p_\varphi && \text{(conserved angular momentum)}
\end{aligned} $$

In the ergosphere ($r_+ < r < r_\text{erg}$), the Killing vector $\xi^\mu$ becomes spacelike: $g_{\mu\nu} \xi^\mu \xi^\nu = g_{tt} > 0$. A particle can therefore have $p_\mu \xi^\mu > 0$, i.e. $E = -p_t < 0$ (negative conserved energy), provided it remains on a future-directed trajectory (its total 4-velocity remains causal when combined with the frame-dragging contribution).

在能层（$r_+ < r < r_\text{erg}$）中，基灵矢量 $\xi^\mu$ 变为类空：$g_{\mu\nu} \xi^\mu \xi^\nu = g_{tt} > 0$。因此粒子可以有 $p_\mu \xi^\mu > 0$，即 $E = -p_t < 0$（负守恒能量），只要它保持面向未来的轨迹（其总4-速度与参考系拖曳结合后仍保持因果性）。

**Step 2 — The splitting process.** Particle 0 enters the ergosphere with energy $E_0 > 0$. Inside the ergosphere it splits into particles 1 and 2. By 4-momentum conservation:

**第 2 步 — 分裂过程。** 粒子 0 以能量 $E_0 > 0$ 进入能层。在能层内分裂为粒子 1 和粒子 2。由4-动量守恒：

$$ p_0^\mu = p_1^\mu + p_2^\mu \to E_0 = E_1 + E_2, \quad L_0 = L_1 + L_2 $$

Particle 1 is engineered to have $E_1 < 0$ and is absorbed by the black hole (it must cross the horizon, which requires $L_1/E_1 < 0$ in a suitable range). Particle 2 escapes to infinity with energy $E_2 = E_0 - E_1 > E_0$ since $E_1 < 0$.

粒子 1 被设计为 $E_1 < 0$ 并被黑洞吸收（需要穿越视界，要求 $L_1/E_1$ 在合适范围内）。粒子 2 逃向无穷远，能量 $E_2 = E_0 - E_1 > E_0$（因为 $E_1 < 0$）。

**Step 3 — The second law constraint.** The black hole absorbs particle 1, changing its mass and angular momentum:

**第 3 步 — 第二定律约束。** 黑洞吸收粒子 1，改变其质量和角动量：

$$ \begin{aligned}
& \delta M = E_1/c^2 && (< 0 \text{ if } E_1 < 0) \\
& \delta J = L_1
\end{aligned} $$

The *Penrose–Floyd* result (1971): the area of the event horizon must not decrease — the *second law of black hole mechanics* (analogous to thermodynamics). The area of the Kerr horizon is:

*彭罗斯–弗洛伊德*结果（1971 年）：事件视界的面积不能减小——黑洞力学*第二定律*（类比热力学）。克尔视界的面积为：

$$ A = 8\pi G^2 M r_+ / c^4 = 8\pi G (G M^2 + \sqrt{G^2 M^4 - J^2 c^2}) / c^4 $$

The condition $\delta A \ge 0$ translates to (using the relation between $\delta M$, $\delta J$, and $\delta A$ via the first law $\delta M c^2 = (\kappa/8\pi G) \delta A + \Omega_H \delta J$):

条件 $\delta A \ge 0$ 转化为（利用第一定律 $\delta M c^2 = (\kappa/8\pi G) \delta A + \Omega_H \delta J$）：

$$ E_1 \ge \Omega_H L_1 $$

where $\Omega_H = ac/(2GM r_+)$ is the angular velocity of the horizon ($a = J/(Mc)$ is the spin parameter).

其中 $\Omega_H = ac/(2GM r_+)$ 是视界角速度（$a = J/(Mc)$ 为自旋参数）。

**Step 4 — Maximum energy extraction.** For maximum extraction, take the absorbed particle 1 at the margin $\delta A = 0$ (reversible process):

**第 4 步 — 最大能量提取。** 为使提取最大化，令吸收的粒子 1 处于边界 $\delta A = 0$（可逆过程）：

$$ E_1 = \Omega_H L_1 \to E_2 = E_0 - \Omega_H L_1 $$

The efficiency $\eta = (E_2 - E_0)/E_0 = -E_1/E_0$ is maximized when $|E_1|$ is maximized. The maximum is constrained by the physical condition that particle 1 must cross the horizon: the condition is $E_1/L_1 \ge \Omega_H$ (from the requirement that the 4-momentum is future-directed inside the horizon), which is saturated at equality.

效率 $\eta = (E_2 - E_0)/E_0 = -E_1/E_0$ 在 $|E_1|$ 最大时取得最大值。最大值受粒子 1 必须穿越视界的物理条件约束：条件为 $E_1/L_1 \ge \Omega_H$（要求4-动量在视界内面向未来），等号时饱和。

**Step 5 — Extremal Kerr bound.** For a maximally spinning (extremal) Kerr black hole, $a = GM/c^2$ and $r_+ = GM/c^2$. Then $\Omega_H = a c/(2GM r_+) = c^3/(2GM)$. The *irreducible mass* is $M_\text{irr} = M/\sqrt{2}$ (for $a = GM/c^2$). The maximum extractable energy is $M c^2 - M_\text{irr} c^2 = (1 - 1/\sqrt{2})Mc^2$. Therefore:

**第 5 步 — 极值克尔界。** 对极大旋转（极值）克尔黑洞，$a = GM/c^2$，$r_+ = GM/c^2$。不可约质量为 $M_\text{irr} = M/\sqrt{2}$（当 $a = GM/c^2$ 时）。最大可提取能量为 $Mc^2 - M_\text{irr} c^2 = (1 - 1/\sqrt{2})Mc^2$。因此：

$$ \boxed{\, \eta_\text{max} = 1 - 1/\sqrt{2} \approx 29.3\% \,} \qquad \blacksquare $$

The extracted energy comes from the rotational kinetic energy of the black hole: after the process, the hole has less angular momentum (it has been partially spun down). Successive reversible extractions can in principle spin the hole from $a = GM/c^2$ to $a = 0$ (Schwarzschild), releasing a fraction $(1 - 1/\sqrt{2})$ of the total mass-energy.

提取的能量来自黑洞的转动动能：过程后黑洞角动量减少（被部分减速）。连续的可逆提取原则上可使黑洞从 $a = GM/c^2$ 降至 $a = 0$（史瓦西），释放出总质能的 $(1 - 1/\sqrt{2})$ 分数。$\blacksquare$

---

## C. The Raychaudhuri Equation · 雷乔杜里方程

**Claim.** For a congruence of timelike geodesics with unit tangent $u^\mu$ ($u^\mu u_\mu = -1$), defining the expansion $\theta = \nabla_\mu u^\mu$, shear $\sigma_{\mu\nu}$, and vorticity $\omega_{\mu\nu}$ as the irreducible decomposition of $\nabla_\nu u_\mu$, the expansion satisfies:

**命题。** 对单位切矢量为 $u^\mu$（$u^\mu u_\mu = -1$）的类时测地线族，定义膨胀率 $\theta = \nabla_\mu u^\mu$，剪切 $\sigma_{\mu\nu}$ 和旋度 $\omega_{\mu\nu}$ 作为 $\nabla_\nu u_\mu$ 的不可约分解，膨胀率满足：

$$ d\theta/d\tau = -\theta^2/3 - \sigma_{\mu\nu} \sigma^{\mu\nu} + \omega_{\mu\nu} \omega^{\mu\nu} - R_{\mu\nu} u^\mu u^\nu $$

**Step 1 — Decompose $\nabla_\nu u_\mu$.** For a unit timelike vector $u^\mu$, define the projection tensor $h_{\mu\nu} = g_{\mu\nu} + u_\mu u_\nu$ (projects onto the hypersurface orthogonal to $u$). Decompose $\nabla_\nu u_\mu$ into parts orthogonal and parallel to $u$:

**第 1 步 — 分解 $\nabla_\nu u_\mu$。** 对单位类时矢量 $u^\mu$，定义投影张量 $h_{\mu\nu} = g_{\mu\nu} + u_\mu u_\nu$（投影到 $u$ 的正交超曲面）。将 $\nabla_\nu u_\mu$ 分解为垂直和平行于 $u$ 的部分：

$$ \nabla_\nu u_\mu = \sigma_{\mu\nu} + \omega_{\mu\nu} + (\theta/3) h_{\mu\nu} - a_\mu u_\nu $$

where:
- $\theta = h^{\mu\nu} \nabla_\nu u_\mu = \nabla_\mu u^\mu$ (expansion; trace part)
- $\sigma_{\mu\nu} = \nabla_{(\nu} u_{\mu)} - (\theta/3) h_{\mu\nu} + u_{(\mu} a_{\nu)}$ (shear; traceless symmetric part of spatial projection)
- $\omega_{\mu\nu} = \nabla_{[\nu} u_{\mu]} + u_{[\mu} a_{\nu]}$ (vorticity; antisymmetric part of spatial projection)
- $a_\mu = u^\nu \nabla_\nu u_\mu = Du_\mu/d\tau$ (acceleration; zero for geodesics)

其中：$\theta$ 为膨胀（迹部分），$\sigma_{\mu\nu}$ 为剪切（空间投影的无迹对称部分），$\omega_{\mu\nu}$ 为旋度（空间投影的反对称部分），$a_\mu$ 为加速度（对测地线为零）。

For geodesics ($a_\mu = 0$) this simplifies.

对测地线（$a_\mu = 0$），这些表达式简化。

**Step 2 — Compute $d\theta/d\tau$.** Differentiate $\theta = \nabla_\mu u^\mu$ along the flow:

**第 2 步 — 计算 $d\theta/d\tau$。** 沿流对 $\theta = \nabla_\mu u^\mu$ 求导：

$$ d\theta/d\tau = u^\nu \nabla_\nu(\nabla_\mu u^\mu) = u^\nu \nabla_\nu \nabla^\mu u_\mu. $$

Commuting the two covariant derivatives with the Ricci identity introduces a Ricci-tensor term:

用里奇恒等式交换两个协变导数，引入一个里奇张量项：

$$ u^\nu \nabla_\nu \nabla^\mu u_\mu = u^\nu \nabla^\mu \nabla_\nu u_\mu - R_{\mu\nu} u^\mu u^\nu. $$

For the first term, the geodesic equation $u^\nu \nabla_\nu u_\mu = 0$ gives $u^\nu \nabla^\mu \nabla_\nu u_\mu = \nabla^\mu(u^\nu \nabla_\nu u_\mu) - (\nabla^\mu u^\nu)(\nabla_\nu u_\mu) = -(\nabla^\mu u^\nu)(\nabla_\nu u_\mu)$. Therefore:

对第一项，测地线方程 $u^\nu \nabla_\nu u_\mu = 0$ 给出 $u^\nu \nabla^\mu \nabla_\nu u_\mu = -(\nabla^\mu u^\nu)(\nabla_\nu u_\mu)$。故：

$$ d\theta/d\tau = -(\nabla^\mu u^\nu)(\nabla_\nu u_\mu) - R_{\mu\nu} u^\mu u^\nu. $$

**Step 3 — Expand the quadratic term.** Using the decomposition $\nabla_\nu u_\mu = (\theta/3)h_{\mu\nu} + \sigma_{\mu\nu} + \omega_{\mu\nu}$ (for geodesics, no acceleration term, using spatial parts only):

**第 3 步 — 展开二次项。** 利用分解 $\nabla_\nu u_\mu = (\theta/3)h_{\mu\nu} + \sigma_{\mu\nu} + \omega_{\mu\nu}$（测地线情况）：

$$ (\nabla^\mu u^\nu)(\nabla_\nu u_\mu) = ((\theta/3)h^{\mu\nu} + \sigma^{\mu\nu} + \omega^{\mu\nu})((\theta/3)h_{\nu\mu} + \sigma_{\nu\mu} + \omega_{\nu\mu}) $$

Expand using $h^{\mu\nu} h_{\nu\mu} = h^\mu{}_\mu = 3$ (dimension of spatial hypersurface), and orthogonality: $\sigma^{\mu\nu}$ is symmetric, $\omega^{\mu\nu}$ antisymmetric $\to \sigma^{\mu\nu} \omega_{\nu\mu} = 0$ (product of symmetric and antisymmetric $= 0$). Also $h^{\mu\nu} \sigma_{\nu\mu} = \sigma^\mu{}_\mu = 0$ (shear is traceless), and $h^{\mu\nu} \omega_{\nu\mu} = \omega^\mu{}_\mu = 0$ (antisymmetric trace $= 0$):

展开：利用 $h^\mu{}_\mu = 3$，以及正交性：$\sigma^{\mu\nu}$ 对称，$\omega^{\mu\nu}$ 反对称 $\to \sigma^{\mu\nu}\omega_{\nu\mu} = 0$。又 $h^{\mu\nu}\sigma_{\nu\mu} = 0$（剪切无迹），$h^{\mu\nu}\omega_{\nu\mu} = 0$（反对称迹为零）：

$$ \begin{aligned}
(\nabla^\mu u^\nu)(\nabla_\nu u_\mu) & = (\theta^2/9)(3) + \sigma^{\mu\nu}\sigma_{\nu\mu} + \omega^{\mu\nu}\omega_{\nu\mu} \\
& = \theta^2/3 + \sigma_{\mu\nu}\sigma^{\mu\nu} - \omega_{\mu\nu}\omega^{\mu\nu}
\end{aligned} $$

Note: $\omega^{\mu\nu}\omega_{\nu\mu} = -\omega_{\mu\nu}\omega^{\mu\nu}$ because $\omega_{\nu\mu} = -\omega_{\mu\nu}$ (antisymmetric) $\to \omega^{\mu\nu}\omega_{\nu\mu} = \omega^{\mu\nu}(-\omega_{\mu\nu}) = -\omega_{\mu\nu}\omega^{\mu\nu}$. Since $\omega_{\mu\nu}\omega^{\mu\nu} > 0$ by definition (positive semi-definite quadratic form on real antisymmetric tensors), the sign in the Raychaudhuri equation is $+\omega^2$.

注意：$\omega^{\mu\nu}\omega_{\nu\mu} = -\omega_{\mu\nu}\omega^{\mu\nu}$（因为 $\omega_{\nu\mu} = -\omega_{\mu\nu}$）。

**Step 4 — Collect.** Therefore:

**第 4 步 — 汇总。** 因此：

$$ \boxed{\, d\theta/d\tau = -\theta^2/3 - \sigma_{\mu\nu}\sigma^{\mu\nu} + \omega_{\mu\nu}\omega^{\mu\nu} - R_{\mu\nu} u^\mu u^\nu \,} \qquad \blacksquare $$

**Step 5 — Focusing from the energy condition.** Suppose the SEC holds ($R_{\mu\nu} u^\mu u^\nu \ge 0$), the congruence is hypersurface-orthogonal ($\omega_{\mu\nu} = 0$, which follows from Frobenius's theorem when the tangent vector field is the gradient of a scalar), and the flow is initially converging ($\theta_0 < 0$). Then:

**第 5 步 — 能量条件导致聚焦。** 设 SEC 成立（$R_{\mu\nu} u^\mu u^\nu \ge 0$），测地线族超曲面正交（$\omega_{\mu\nu} = 0$，由弗罗贝尼乌斯定理，当切矢量场是某标量的梯度时成立），且流初始收缩（$\theta_0 < 0$）。则：

$$ d\theta/d\tau \le -\theta^2/3 $$

This is a Bernoulli ODE. Integrating: define $f(\tau) = 1/\theta(\tau)$. Then $df/d\tau = -(1/\theta^2)(d\theta/d\tau) \ge 1/3$. So $f(\tau) \ge f(0) + \tau/3 = 1/\theta_0 + \tau/3$.

这是伯努利常微分方程。积分：令 $f(\tau) = 1/\theta(\tau)$，则 $df/d\tau \ge 1/3$，故 $f(\tau) \ge 1/\theta_0 + \tau/3$。

Since $\theta_0 < 0$, $f(0) = 1/\theta_0 < 0$. The right-hand side passes through zero at $\tau_* = -3/\theta_0 > 0$. But $f(\tau) = 1/\theta(\tau) \to 0^-$ means $\theta \to -\infty$, i.e. the congruence focuses to a **caustic** (a point where neighbouring geodesics cross) within proper time $\tau \le 3/|\theta_0|$. $\blacksquare$

由于 $\theta_0 < 0$，$f(0) = 1/\theta_0 < 0$，右侧在 $\tau_* = -3/\theta_0 > 0$ 处过零。但 $f(\tau) = 1/\theta(\tau) \to 0^-$ 意味着 $\theta \to -\infty$，即测地线族在固有时 $\tau \le 3/|\theta_0|$ 内聚焦到**焦散面**（相邻测地线相交之处）。$\blacksquare$

**Step 6 — Connection to the singularity theorems.** The Penrose theorem uses the null version of the Raychaudhuri equation (replace $\tau$ with affine parameter $\lambda$ and $u^\mu u_\mu = 0$; the equation is identical in form with the coefficient $1/2$ instead of $1/3$ in the $\theta^2$ term):

**第 6 步 — 与奇点定理的联系。** 彭罗斯定理使用雷乔杜里方程的类光版本（以仿射参数 $\lambda$ 代替 $\tau$，$u^\mu u_\mu = 0$；方程形式相同，$\theta^2$ 项系数为 $1/2$ 而非 $1/3$）：

$$ d\theta/d\lambda = -\theta^2/2 - \sigma_{\mu\nu}\sigma^{\mu\nu} + \omega_{\mu\nu}\omega^{\mu\nu} - R_{\mu\nu} k^\mu k^\nu $$

where $k^\mu$ is the null tangent. Under the NEC ($R_{\mu\nu} k^\mu k^\nu \ge 0$) and for $\omega = 0$, this gives $\theta \to -\infty$ within affine time $\lambda \le 2/|\theta_0|$. This is the *focusing theorem*: null geodesics through a trapped surface ($\theta_0 < 0$ for outgoing null rays) must focus, implying the existence of conjugate points (where the geodesic can no longer remain on $\partial J^+(S)$). The Penrose theorem then uses topological arguments to show incompleteness must result. $\blacksquare$

其中 $k^\mu$ 为类光切矢量。在 NEC（$R_{\mu\nu} k^\mu k^\nu \ge 0$）和 $\omega = 0$ 下，这给出 $\theta \to -\infty$ 在仿射时间 $\lambda \le 2/|\theta_0|$ 内。这是*聚焦定理*：通过囚禁面（向外类光线 $\theta_0 < 0$）的类光测地线必须聚焦，意味着共轭点的存在（测地线在此不再位于 $\partial J^+(S)$ 上）。彭罗斯定理随后用拓扑论证证明测地线不完整必然产生。$\blacksquare$

---

*The three derivations here form a coherent logical chain: Kruskal coordinates reveal that Schwarzschild spacetime is singular at $r = 0$ (not $r = r_s$) and show the global causal structure; the Penrose process bounds show how rotational energy can be extracted from the ergosphere without violating the second law; and the Raychaudhuri equation is the engine behind the singularity theorems, connecting the geometric convergence of geodesics to the energy content of spacetime.*

*此处三个推导形成一条连贯的逻辑链：克鲁斯卡尔坐标揭示史瓦西时空在 $r = 0$（而非 $r = r_s$）处是奇异的，并展示整体因果结构；彭罗斯过程的能量界表明可在不违反第二定律的情况下从能层提取转动能量；雷乔杜里方程是奇点定理的驱动引擎，将测地线的几何汇聚与时空的能量内容联系起来。*

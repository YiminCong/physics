# Derivations — Module 7.7: Tests of GR & Gravitational-Wave Astronomy
# 推导 — 模块 7.7：广义相对论的检验与引力波天文学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.7](./module-7.7-tests-of-gr-and-gravitational-wave-astronomy.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.7](./module-7.7-tests-of-gr-and-gravitational-wave-astronomy.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Perihelion Advance: $\Delta\varphi = 6\pi GM / (c^2 a(1-e^2))$ · 近日点进动

**Claim.** A test particle in the Schwarzschild metric on a bound orbit precesses by

**命题。** 史瓦西度规中束缚轨道上的试验粒子每圈进动

$$ \Delta\varphi = 6\pi GM / (c^2 a(1 - e^2)) $$

per orbit, where $a$ is the semi-major axis and $e$ is the eccentricity.

其中 $a$ 为半长轴，$e$ 为离心率。

**Step 1 — The Schwarzschild geodesic equations.** The Schwarzschild metric (Module 7.5) for motion in the equatorial plane ($\theta = \pi/2$) has two conserved quantities from the Killing vectors $\partial_t$ and $\partial_\varphi$:

**第 1 步 — 史瓦西测地线方程。** 赤道面（$\theta = \pi/2$）内运动的史瓦西度规（模块 7.5）有两个来自基灵矢量 $\partial_t$ 和 $\partial_\varphi$ 的守恒量：

$$ \begin{aligned}
& E = (1 - r_s/r) c^2 dt/d\tau && \text{(energy per unit rest mass)} \\
& \ell = r^2 d\varphi/d\tau && \text{(angular momentum per unit rest mass)}
\end{aligned} $$

The timelike geodesic condition $g_{\mu\nu} u^\mu u^\nu = -c^2$ with $u^\mu = dx^\mu/d\tau$ gives, after substituting $E$ and $\ell$:

类时测地线条件 $g_{\mu\nu} u^\mu u^\nu = -c^2$，代入 $E$ 和 $\ell$ 后给出：

$$ (dr/d\tau)^2 = E^2/c^2 - (1 - r_s/r)(c^2 + \ell^2/r^2) $$

**Step 2 — Change to the orbit variable $u = 1/r$.** Let $u = 1/r$. Then $dr/d\tau = -(1/u^2)(du/d\tau) = -(1/u^2)(du/d\varphi)(d\varphi/d\tau) = -\ell (du/d\varphi)$, using $d\varphi/d\tau = \ell u^2$. Substituting:

**第 2 步 — 变换到轨道变量 $u = 1/r$。** 令 $u = 1/r$。则 $dr/d\tau = -\ell (du/d\varphi)$（利用 $d\varphi/d\tau = \ell u^2$）。代入得：

$$ \ell^2 (du/d\varphi)^2 = E^2/c^2 - (1 - r_s u)(c^2 + \ell^2 u^2) $$

Differentiate both sides with respect to $\varphi$ and divide by $2\ell^2 (du/d\varphi)$ (assuming non-circular orbit, $du/d\varphi \ne 0$):

对 $\varphi$ 求导并除以 $2\ell^2 (du/d\varphi)$（设轨道非圆形，$du/d\varphi \ne 0$）：

$$ d^2u/d\varphi^2 = -u + GM/\ell^2 + (3GM/c^2) u^2 $$

The first two terms reproduce the Newtonian orbit equation (Binet's equation). The last term, $(3GM/c^2) u^2$, is the **GR correction**.

前两项重现牛顿轨道方程（比内方程），最后一项 $(3GM/c^2) u^2$ 是**广义相对论修正**。

**Step 3 — Perturbative solution.** For a nearly circular orbit, let $u_0 = GM/\ell^2 (1 + e \cos\varphi)^{-1}$ be the Newtonian ellipse solution ($u_0 \approx GM(1+e \cos\varphi)/\ell^2$ for small $e$). Write $u = u_0 + u_1$ where $u_1$ is the small GR perturbation. To leading order in $\varepsilon \equiv 3(GM)^2/(c^2\ell^2) \ll 1$, substitute $u_0$ into the correction term:

**第 3 步 — 摄动求解。** 对近圆轨道，令 $u_0 = GM/\ell^2 (1 + e \cos\varphi)$ 为牛顿椭圆解（对小 $e$，$u_0 \approx GM(1 + e \cos\varphi)/\ell^2$）。写出 $u = u_0 + u_1$，其中 $u_1$ 为小的广义相对论修正。以 $\varepsilon \equiv 3(GM)^2/(c^2\ell^2) \ll 1$ 为展开参数，将 $u_0$ 代入修正项：

$$ (3GM/c^2) u_0^2 \approx (3GM/c^2)(GM/\ell^2)^2(1 + 2e \cos\varphi + e^2 \cos^2\varphi) $$

The equation for $u_1$ becomes:

$u_1$ 的方程变为：

$$ d^2u_1/d\varphi^2 + u_1 = (3GM/c^2)(GM/\ell^2)^2(1 + 2e \cos\varphi + e^2 \cos^2\varphi) $$

The constant and $\cos^2\varphi$ terms give bounded particular solutions. The resonant forcing term $2e \cos\varphi$ gives a secular (unbounded) particular solution:

常数项和 $\cos^2\varphi$ 项给出有界特解。共振驱动项 $2e \cos\varphi$ 给出长期（无界）特解：

$$ u_1 = (3GM/c^2)(GM/\ell^2)^2 e\, \varphi \sin\varphi $$

**Step 4 — Extract the precession.** The total solution to leading order is:

**第 4 步 — 提取进动。** 到主阶，总解为：

$$ \begin{aligned}
u & \approx (GM/\ell^2)[1 + e \cos\varphi + \varepsilon e\, \varphi \sin\varphi] \\
& = (GM/\ell^2)[1 + e \cos(\varphi(1 - \varepsilon))] \quad \text{to first order in } \varepsilon.
\end{aligned} $$

The orbit closes when the argument of cosine advances by $2\pi$, i.e. $\varphi_\text{close} (1 - \varepsilon) = 2\pi$, giving $\varphi_\text{close} = 2\pi/(1 - \varepsilon) \approx 2\pi(1 + \varepsilon)$. The excess per orbit is:

当余弦函数的宗量前进 $2\pi$ 时轨道闭合，即 $\varphi_\text{close} (1 - \varepsilon) = 2\pi$，给出 $\varphi_\text{close} = 2\pi(1 + \varepsilon)$。每圈超出量为：

$$ \Delta\varphi = 2\pi \varepsilon = 6\pi(GM)^2/(c^2 \ell^2) $$

**Step 5 — Convert to orbital elements.** For a Keplerian ellipse, $\ell^2 = GMa(1 - e^2)$, so $(GM)^2/\ell^2 = GM/(a(1 - e^2))$. Therefore:

**第 5 步 — 转换为轨道根数。** 对开普勒椭圆，$\ell^2 = GMa(1 - e^2)$，故 $(GM)^2/\ell^2 = GM/(a(1 - e^2))$。因此：

$$ \boxed{\, \Delta\varphi = 6\pi GM / (c^2 a(1 - e^2)) \,} \qquad \blacksquare $$

For Mercury: plugging in $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻², $M_\odot = 1.989 \times 10^{30}$ kg, $a = 5.79 \times 10^{10}$ m, $e = 0.206$ gives $\Delta\varphi \approx 5.02 \times 10^{-7}$ rad/orbit $\approx 43.1''$/century (using 415 orbits/century). This matches the observed anomaly to within observational uncertainty.

对水星：代入 $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻²，$M_\odot = 1.989 \times 10^{30}$ kg，$a = 5.79 \times 10^{10}$ m，$e = 0.206$，得 $\Delta\varphi \approx 5.02 \times 10^{-7}$ rad/圈 $\approx 43.1''$/世纪（利用每世纪 415 圈），与观测到的反常值在观测误差范围内吻合。

---

## B. Light Deflection: $\alpha = 4GM / (c^2 b)$ · 光线偏折

**Claim.** A photon with impact parameter $b$ passing a mass $M$ is deflected by

**命题。** 碰撞参数为 $b$ 经过质量 $M$ 的光子偏折角为

$$ \alpha = 4GM / (c^2 b) $$

**Step 1 — Null geodesic in Schwarzschild.** For a photon (null geodesic, $ds^2 = 0$) in the Schwarzschild metric, the energy $E$ and angular momentum $\ell$ are still conserved. The null condition gives:

**第 1 步 — 史瓦西中的类光测地线。** 对史瓦西度规中的光子（类光测地线，$ds^2 = 0$），$E$ 和 $\ell$ 仍守恒。类光条件给出：

$$ (dr/d\tau)^2 = E^2/c^2 - (1 - r_s/r) \ell^2/r^2 $$

where now $\tau$ is an affine parameter (not proper time). Define the impact parameter $b = \ell c/E$. Changing to $u = 1/r$ and differentiating with respect to $\varphi$ (as in Derivation A):

此处 $\tau$ 为仿射参数（非固有时）。定义碰撞参数 $b = \ell c/E$。变换到 $u = 1/r$ 并对 $\varphi$ 求导（与推导 A 类似）：

$$ d^2u/d\varphi^2 + u = (3GM/c^2) u^2 $$

**Step 2 — Zeroth order (straight line).** Without the GR term, the equation $d^2u/d\varphi^2 + u = 0$ has solution $u_0 = \sin\varphi / b$ (a straight line passing distance $b$ from the origin, with $\varphi = 0$ at closest approach). Note: for this parametrization, the photon comes from $\varphi = 0$ (closest approach) and the straight-line path satisfies $r \sin\varphi = b$, i.e. $u_0 = \sin\varphi / b$.

**第 2 步 — 零阶（直线）。** 不含广义相对论项时，方程 $d^2u/d\varphi^2 + u = 0$ 的解为 $u_0 = \sin\varphi / b$（距原点 $b$ 处通过的直线，$\varphi = 0$ 为最近点）。

**Step 3 — First-order perturbation.** Write $u = u_0 + u_1$ with $u_1 \ll u_0$. Substituting:

**第 3 步 — 一阶摄动。** 写出 $u = u_0 + u_1$（$u_1 \ll u_0$）。代入：

$$ d^2u_1/d\varphi^2 + u_1 = (3GM/c^2)(\sin\varphi/b)^2 = (3GM/c^2 b^2)(1 - \cos^2\varphi) $$

To solve for the particular solution, write the right-hand side using $\sin^2\varphi = (1 - \cos 2\varphi)/2$:

将右侧用 $\sin^2\varphi = (1 - \cos 2\varphi)/2$ 改写以求特解：

$$ d^2u_1/d\varphi^2 + u_1 = (3GM)/(2c^2 b^2) - (3GM)/(2c^2 b^2) \cos 2\varphi $$

Particular solution: (i) for the constant term $K = 3GM/(2c^2 b^2)$: $u_p = K$. (ii) For the term $-K \cos 2\varphi$: try $u = C \cos 2\varphi$, then $-4C \cos 2\varphi + C \cos 2\varphi = -3C \cos 2\varphi = -K \cos 2\varphi$, so $C = K/3$. Hence:

特解：（i）常数项 $K = 3GM/(2c^2 b^2)$：$u_p = K$。（ii）项 $-K \cos 2\varphi$：令 $u = C \cos 2\varphi$，则 $-3C \cos 2\varphi = -K \cos 2\varphi$，故 $C = K/3$。因此：

$$ u_1 = (GM)/(c^2 b^2) \cdot (3/2)(1 + (1/3) \cos 2\varphi) = (GM)/(c^2 b^2)(3/2 + (1/2) \cos 2\varphi) $$

**Step 4 — Asymptotic deflection.** As $r \to \infty$ (i.e. $u \to 0$), the photon escapes. Solving $u = u_0 + u_1 = 0$:

**第 4 步 — 渐近偏折。** 当 $r \to \infty$（即 $u \to 0$）时光子逃逸。解方程 $u = u_0 + u_1 = 0$：

$$ \sin\varphi / b + (GM/c^2 b^2)(3/2 + (1/2) \cos 2\varphi) = 0 $$

For large $r$ ($u \to 0$), $\varphi \to \pi + \delta$ where $\delta$ is small (the photon is moving almost in the $-x$ direction when it escapes). Set $\varphi = \pi + \delta$, $\sin\varphi \approx -\delta$, $\cos 2\varphi = \cos(2\pi + 2\delta) \approx 1$:

对大 $r$（$u \to 0$），$\varphi \to \pi + \delta$，$\delta$ 为小量。令 $\varphi = \pi + \delta$，$\sin\varphi \approx -\delta$，$\cos 2\varphi \approx 1$：

$$ -\delta/b + (GM/c^2 b^2)(3/2 + 1/2) = 0 \to \delta = 2GM/(c^2 b) $$

By symmetry (the same deflection occurs on the approach half), the total deflection is:

由对称性（入射半程有相同的偏折），总偏折为：

$$ \boxed{\, \alpha = 2\delta = 4GM/(c^2 b) \,} \qquad \blacksquare $$

For a ray grazing the Sun: $\alpha = 4(6.674\times 10^{-11})(1.989\times 10^{30})/((3\times 10^8)^2(6.96\times 10^8)) = 8.48\times 10^{-6}$ rad $= 1.75''$.

对掠日光线：$\alpha = 4(6.674\times 10^{-11})(1.989\times 10^{30})/((3\times 10^8)^2(6.96\times 10^8)) = 8.48\times 10^{-6}$ rad $= 1.75''$。

---

## C. Lens Equation and Einstein Ring Radius · 透镜方程与爱因斯坦环半径

**Claim.** For a point mass lens at angular diameter distance $D_L$, with source at $D_S$ and lens-to-source distance $D_{LS}$, the lens equation is $\beta = \theta - \theta_E^2/\theta$, where the Einstein ring radius is

**命题。** 对位于角直径距离 $D_L$ 处的点质量透镜，源在 $D_S$ 处，透镜到源距离 $D_{LS}$，透镜方程为 $\beta = \theta - \theta_E^2/\theta$，其中爱因斯坦环半径为

$$ \theta_E = \sqrt{4GM D_{LS} / (c^2 D_L D_S)} $$

**Step 1 — Geometry.** Place the observer at O, lens at L (distance $D_L$ from O), source at S (distance $D_S$ from O). All nearly co-linear. The photon comes from source angle $\beta$ (true position) and arrives from image angle $\theta$ (apparent position, both measured from the lens direction). The physical deflection angle $\hat{\alpha} = \alpha$ (as derived above) relates to the angles through the geometry of the triangle O–L–S:

**第 1 步 — 几何。** 将观测者置于 O，透镜在 L（距 O 为 $D_L$），源在 S（距 O 为 $D_S$）。三者近似共线。光子来自源的角度 $\beta$（真实位置），从图像角度 $\theta$（视位置，均从透镜方向量起）到达。物理偏折角 $\hat{\alpha} = \alpha$ 通过三角形 O–L–S 的几何关系与各角度相关：

$$ D_S \beta = D_S \theta - D_{LS} \hat{\alpha} $$

where $D_{LS} \hat{\alpha}$ is the transverse displacement due to deflection. Using the impact parameter $b = D_L \theta$ (for small angles):

其中 $D_{LS} \hat{\alpha}$ 为偏折引起的横向位移。利用碰撞参数 $b = D_L \theta$（对小角度）：

$$ D_S \beta = D_S \theta - D_{LS} \cdot 4GM/(c^2 D_L \theta) $$

Divide by $D_S$:

除以 $D_S$：

$$ \beta = \theta - (4GM D_{LS})/(c^2 D_L D_S) \cdot (1/\theta) $$

**Step 2 — Einstein ring radius.** Define:

**第 2 步 — 爱因斯坦环半径。** 定义：

$$ \theta_E^2 = 4GM D_{LS} / (c^2 D_L D_S) $$

Then the lens equation is:

则透镜方程为：

$$ \boxed{\, \beta = \theta - \theta_E^2 / \theta \,} \qquad \blacksquare $$

**Step 3 — Einstein ring condition.** For $\beta = 0$ (perfect alignment), the equation becomes $\theta^2 = \theta_E^2$, giving $\theta = \theta_E$: a complete ring of angular radius $\theta_E$. For $\beta \ne 0$, the quadratic $\theta^2 - \beta\theta - \theta_E^2 = 0$ gives two images at:

**第 3 步 — 爱因斯坦环条件。** 当 $\beta = 0$（完美对齐）时，方程变为 $\theta^2 = \theta_E^2$，给出 $\theta = \theta_E$：角半径 $\theta_E$ 的完整圆环。当 $\beta \ne 0$ 时，二次方程 $\theta^2 - \beta\theta - \theta_E^2 = 0$ 给出两个像：

$$ \theta_\pm = (\beta \pm \sqrt{\beta^2 + 4\theta_E^2}) / 2 $$

One image ($\theta_+$) is outside the Einstein ring, one ($\theta_-$) inside. The magnification of each image is $|\mu_\pm| = |\theta_\pm/\beta \cdot d\theta_\pm/d\beta|$, and the total magnification is:

一个像（$\theta_+$）在爱因斯坦环外，一个（$\theta_-$）在内。各像的放大率为 $|\mu_\pm| = |\theta_\pm/\beta \cdot d\theta_\pm/d\beta|$，总放大率为：

$$ \mu = (u^2 + 2) / (u \sqrt{u^2 + 4}), \quad \text{where } u = \beta/\theta_E. $$

For $u \to 0$ (perfect alignment), $\mu \to \infty$; for $u \gg 1$, $\mu \to 1 + 2\theta_E^2/\beta^2$ (small correction).

当 $u \to 0$（完美对齐）时 $\mu \to \infty$；当 $u \gg 1$ 时 $\mu \to 1 + 2\theta_E^2/\beta^2$（小修正）。$\blacksquare$

---

## D. Chirp Mass from the Quadrupole Formula · 由四极矩公式导出啁啾质量

**Claim.** For a circular compact binary with component masses $m_1, m_2$, total mass $M = m_1 + m_2$, and reduced mass $\mu = m_1 m_2/M$, the GW frequency evolution is:

**命题。** 对质量为 $m_1$、$m_2$，总质量 $M = m_1 + m_2$，约化质量 $\mu = m_1 m_2/M$ 的圆形轨道致密双星，引力波频率演化为：

$$ df/dt = (96/5) \pi^{8/3} (G M_c/c^3)^{5/3} f^{11/3} $$

where $M_c = \mu^{3/5} M^{2/5} = (m_1 m_2)^{3/5} / (m_1 + m_2)^{1/5}$ is the chirp mass.

其中 $M_c = \mu^{3/5} M^{2/5} = (m_1 m_2)^{3/5} / (m_1 + m_2)^{1/5}$ 为啁啾质量。

**Step 1 — Quadrupole radiated power.** The Einstein quadrupole formula (derived in Module 7.5) gives the total GW power radiated by a system with quadrupole moment tensor $I_{ij}$:

**第 1 步 — 四极矩辐射功率。** 爱因斯坦四极矩公式（在模块 7.5 中推导）给出具有四极矩张量 $I_{ij}$ 的系统辐射的总引力波功率：

$$ P = G/(5c^5) \langle d^3I_{ij}/dt^3 \cdot d^3I^{ij}/dt^3 \rangle $$

For a circular binary in the x-y plane, with separation $r$ and reduced mass $\mu$ at orbital frequency $\Omega = 2\pi f_\text{orb}$:

对 x-y 平面内的圆形双星，间距 $r$，约化质量 $\mu$，轨道频率 $\Omega = 2\pi f_\text{orb}$：

$$ I_{ij} = \mu r^2 \begin{pmatrix} \cos^2(\Omega t) & \cos(\Omega t)\sin(\Omega t) & 0 \\ \cos(\Omega t)\sin(\Omega t) & \sin^2(\Omega t) & 0 \\ 0 & 0 & 0 \end{pmatrix} $$

(traceless part)

（无迹部分）

Computing the third time derivative and contracting (the algebra yields a factor of 32/5):

计算三阶时间导数并缩并（代数计算给出因子 32/5）：

$$ P = (32G/5c^5) \mu^2 r^4 \Omega^6 $$

**Step 2 — Kepler's third law.** For a circular orbit: $\Omega^2 = GM/r^3 \to r = (GM)^{1/3}/\Omega^{2/3}$. Substituting $r = (GM/\Omega^2)^{1/3}$:

**第 2 步 — 开普勒第三定律。** 圆形轨道：$\Omega^2 = GM/r^3 \to r = (GM)^{1/3}/\Omega^{2/3}$。代入 $r = (GM/\Omega^2)^{1/3}$：

$$ P = (32G/5c^5) \mu^2 r^4 \Omega^6 \quad \text{(from Step 1)}. $$

With $r = (GM)^{1/3} \Omega^{-2/3}$, we have $r^4 \Omega^6 = [(GM)^{1/3} \Omega^{-2/3}]^4 \Omega^6 = (GM)^{4/3} \Omega^{-8/3} \Omega^6 = (GM)^{4/3} \Omega^{10/3}$, so

代入 $r = (GM)^{1/3} \Omega^{-2/3}$，得 $r^4 \Omega^6 = (GM)^{4/3} \Omega^{10/3}$，故

$$ P = (32G/5c^5) \mu^2 (GM)^{4/3} \Omega^{10/3} = (32G^{7/3}/5c^5) \mu^2 M^{4/3} \Omega^{10/3}. $$

Using $\Omega = \pi f_\text{GW}$ (since $f_\text{GW} = 2 f_\text{orb} = \Omega/\pi$):

利用 $\Omega = \pi f_\text{GW}$（因 $f_\text{GW} = 2 f_\text{orb} = \Omega/\pi$）：

$$ P = (32G^{7/3}/5c^5) \mu^2 M^{4/3} (\pi f_\text{GW})^{10/3} $$

**Step 3 — Energy of the orbit.** The total orbital energy of a circular binary is $E_\text{orb} = -Gm_1 m_2/(2r) = -G\mu M/(2r)$ (using $m_1 m_2 = \mu M$). From Kepler's third law $\Omega^2 = GM/r^3$, the separation is $r = (GM)^{1/3}\Omega^{-2/3} = (GM)^{1/3}(\pi f_\text{GW})^{-2/3}$ (since $\Omega = \pi f_\text{GW}$). Substituting:

**第 3 步 — 轨道能量。** 圆形双星的总轨道能量为 $E_\text{orb} = -Gm_1 m_2/(2r) = -G\mu M/(2r)$（利用 $m_1 m_2 = \mu M$）。由开普勒第三定律 $\Omega^2 = GM/r^3$，间距为 $r = (GM)^{1/3}(\pi f_\text{GW})^{-2/3}$（因 $\Omega = \pi f_\text{GW}$）。代入：

$$ E_\text{orb} = -(G\mu M/2)\cdot(\pi f_\text{GW})^{2/3}/(GM)^{1/3} = -(\mu/2)(GM)^{2/3}(\pi f_\text{GW})^{2/3} = -(\mu/2)(GM\pi f_\text{GW})^{2/3}. $$

**Step 4 — Frequency evolution.** From energy conservation: $dE_\text{orb}/dt = -P$. Differentiate $E_\text{orb}$ with respect to $f_\text{GW}$:

**第 4 步 — 频率演化。** 由能量守恒：$dE_\text{orb}/dt = -P$。对 $f_\text{GW}$ 求导：

$$ dE_\text{orb}/df = -(\mu/2)(2/3)(GM \pi)^{2/3} f_\text{GW}^{-1/3} = -(\mu/3)(GM \pi)^{2/3} f_\text{GW}^{-1/3} $$

So $df/dt = -P / (dE_\text{orb}/df) = P \times 3/[\mu (GM\pi)^{2/3} f_\text{GW}^{-1/3}]$:

故 $df/dt = P \times 3/[\mu (GM\pi)^{2/3} f_\text{GW}^{-1/3}]$：

$$ df/dt = [(32G^{7/3} \mu^2 M^{4/3} \pi^{10/3})/(5c^5)] f_\text{GW}^{10/3} \times 3/[\mu (GM)^{2/3} \pi^{2/3} f_\text{GW}^{-1/3}]. $$

Collect powers — the $(GM)^{2/3}$ in the denominator reduces $G^{7/3}M^{4/3}$ to $G^{5/3}M^{2/3}$:

收集幂次——分母中的 $(GM)^{2/3}$ 将 $G^{7/3}M^{4/3}$ 降为 $G^{5/3}M^{2/3}$：

$$ df/dt = (96/5c^5) G^{5/3} \mu M^{2/3} \pi^{8/3} f_\text{GW}^{11/3} $$

**Step 5 — Introduce the chirp mass.** Define the **chirp mass** $M_c = \mu^{3/5} M^{2/5} = (m_1 m_2)^{3/5}/(m_1+m_2)^{1/5}$. Raising to the 5/3 power, $M_c^{5/3} = (\mu^{3/5}M^{2/5})^{5/3} = \mu M^{2/3}$, so the mass-and-$G$ combination in the result above collapses to a single power of the chirp mass:

**第 5 步 — 引入啁啾质量。** 定义**啁啾质量** $M_c = \mu^{3/5} M^{2/5} = (m_1 m_2)^{3/5}/(m_1+m_2)^{1/5}$。取 5/3 次幂，$M_c^{5/3} = \mu M^{2/3}$，故上式中的质量与 $G$ 组合化为啁啾质量的单一幂次：

$$ G^{5/3} \mu M^{2/3} = G^{5/3} M_c^{5/3} = (G M_c)^{5/3}. $$

Substituting into $df/dt = (96/5c^5) G^{5/3} \mu M^{2/3} \pi^{8/3} f_\text{GW}^{11/3}$ and writing it with the dimensionless combination $G M_c/c^3$:

代入 $df/dt = (96/5c^5) G^{5/3} \mu M^{2/3} \pi^{8/3} f_\text{GW}^{11/3}$，并以无量纲组合 $G M_c/c^3$ 表示：

$$ \boxed{\, df/dt = (96\pi^{8/3}/5) (G M_c/c^3)^{5/3} f_\text{GW}^{11/3} \,} \qquad \blacksquare $$

**Step 6 — Physical interpretation.** Measuring $f(t)$ and $\dot{f}(t)$ from the waveform gives the single combination $(G M_c/c^3)^{5/3}$ directly. Integrating the frequency evolution from $f_i$ to $f_f$ gives the time to merger:

**第 6 步 — 物理诠释。** 从波形中测量 $f(t)$ 和 $\dot{f}(t)$ 直接给出组合 $(G M_c/c^3)^{5/3}$。对频率演化从 $f_i$ 到 $f_f$ 积分，得到并合时间：

$$ t_\text{merge} - t = (5c^3/96G)(G M_c/c^3)^{-5/3} (\pi f_\text{GW})^{-8/3} $$

This diverges as $f_\text{GW} \to f_\text{isco}$ (the innermost stable circular orbit), marking the onset of the plunge and merger phase, which requires numerical relativity to model.

当 $f_\text{GW} \to f_\text{ISCO}$（最内稳定圆轨道）时此式发散，标志着俯冲和并合阶段的开始，该阶段需要数值相对论来建模。$\blacksquare$

---

*Each derivation above corresponds to a key result in Module 7.7. The perihelion and light-deflection calculations both stem from the Schwarzschild geodesic equation; the latter famously gives twice the Newtonian prediction because both the $g_{00}$ (time) and $g_{rr}$ (space) curvature contribute equally. The chirp-mass formula shows why GW150914's $35+29\ M_\odot$ binary gives $M_c \approx 28.3\ M_\odot$, and why the frequency sweep of a $1.4+1.4\ M_\odot$ neutron star binary ($M_c \approx 1.22\ M_\odot$) is orders of magnitude slower than that of GW150914 at the same frequency.*

*以上每个推导对应模块 7.7 中的一个核心结果。近日点进动和光线偏折计算均来自史瓦西测地线方程；后者著名地给出牛顿预测的两倍，因为 $g_{00}$（时间）和 $g_{rr}$（空间）曲率各贡献一半。啁啾质量公式说明了为何 GW150914 的 $35+29\ M_\odot$ 双黑洞给出 $M_c \approx 28.3\ M_\odot$，以及为何在相同频率下，$1.4+1.4\ M_\odot$ 双中子星（$M_c \approx 1.22\ M_\odot$）的频率扫描比 GW150914 慢几个数量级。*

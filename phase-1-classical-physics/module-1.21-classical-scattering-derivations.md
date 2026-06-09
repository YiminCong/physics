---
title: "Derivations — Module 1.21: Classical Scattering Theory"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.21: Classical Scattering Theory
# 推导 — 模块 1.21：经典散射理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.21](./module-1.21-classical-scattering.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.21](./module-1.21-classical-scattering.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Differential Cross Section from the Impact Parameter · 由瞄准距离给出微分散射截面

**Claim.** For scattering off a central potential $U(r)$, the scattering angle $\theta$ is a single-valued function of the impact parameter $b$. Conservation of particle number then gives the differential cross section

**命题。** 对中心势 $U(r)$ 的散射，散射角 $\theta$ 是瞄准距离 $b$ 的单值函数。粒子数守恒给出微分散射截面

$$ \frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right|. $$

**Step 1 — Set up the incident flux.** A uniform parallel beam strikes the target with **flux** $n$ (number of particles crossing unit cross-sectional area per unit time). By symmetry about the beam axis, all particles with impact parameter between $b$ and $b + db$ form an annular ring of area $d\sigma = 2\pi b\,db$. The number of particles passing through this ring per unit time is

**第 1 步 — 设定入射通量。** 一束均匀平行束以**通量** $n$（单位时间穿过单位横截面积的粒子数）射向靶。绕束轴对称，所有瞄准距离介于 $b$ 与 $b + db$ 之间的粒子构成面积为 $d\sigma = 2\pi b\,db$ 的环带。单位时间穿过此环带的粒子数为

$$ dN = n \cdot d\sigma = n \cdot 2\pi b\,db. $$

**Step 2 — Map the ring onto the detector.** Because $\theta$ depends only on $b$ for a central potential, every particle entering the ring $[b, b + db]$ emerges into the cone of scattering angles $[\theta, \theta + d\theta]$. This cone subtends a solid angle (an annulus on the unit sphere) of

**第 2 步 — 将环带映射到探测器。** 由于对中心势 $\theta$ 只依赖于 $b$，进入环带 $[b, b + db]$ 的每个粒子都散射到角度区间 $[\theta, \theta + d\theta]$ 的圆锥中。此圆锥（单位球面上的圆环带）所张的立体角为

$$ d\Omega = 2\pi \sin\theta\,d\theta. $$

**Step 3 — Define the differential cross section.** The differential cross section $d\sigma/d\Omega$ is defined so that the number scattered into $d\Omega$ equals the incident flux times the effective target area:

**第 3 步 — 定义微分散射截面。** 微分散射截面 $d\sigma/d\Omega$ 的定义使得散射进 $d\Omega$ 的粒子数等于入射通量乘以有效靶面积：

$$ dN = n \cdot \frac{d\sigma}{d\Omega}\,d\Omega. $$

The same particles cross the entrance ring and exit through $d\Omega$, so equate the two expressions for $dN$:

同一批粒子穿过入射环带并从 $d\Omega$ 出射，故令 $dN$ 的两个表达式相等：

$$ n \cdot 2\pi b\,db = n \cdot \frac{d\sigma}{d\Omega} \cdot 2\pi \sin\theta\,d\theta. $$

**Step 4 — Solve and insert the absolute value.** Cancelling $n \cdot 2\pi$ and rearranging:

**第 4 步 — 求解并加入绝对值。** 约去 $n \cdot 2\pi$ 并整理：

$$ \frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\frac{db}{d\theta}. $$

For a typical repulsive (or attractive monotonic) potential a smaller impact parameter produces a larger deflection, so $b$ is a **decreasing** function of $\theta$ and $db/d\theta < 0$. The cross section, an area, must be positive, so we take the magnitude:

对典型排斥（或单调吸引）势，较小的瞄准距离产生较大的偏转，故 $b$ 是 $\theta$ 的**递减**函数，$db/d\theta < 0$。截面作为面积必须为正，故取其绝对值：

$$ \boxed{\, \frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right| \,} \qquad \blacksquare $$

---

## B. Deflection Angle for a Central Force · 中心力的偏转角

**Claim.** A particle of mass $m$, energy $E$, and angular momentum $\ell = b\sqrt{2mE} = m v_\infty b$ scattering off the central potential $U(r)$ emerges with scattering angle

**命题。** 质量为 $m$、能量为 $E$、角动量 $\ell = b\sqrt{2mE} = m v_\infty b$ 的粒子被中心势 $U(r)$ 散射后，散射角为

$$ \theta = \pi - 2\varphi_0, \qquad \varphi_0 = \int_{r_{\min}}^\infty \frac{(\ell/r^2)\,dr}{\sqrt{2m(E - U(r)) - \ell^2/r^2}}. $$

**Step 1 — Conserved quantities far away.** Far from the target $U \to 0$, so the asymptotic speed $v_\infty$ obeys $E = \tfrac12 m v_\infty^2$, giving $v_\infty = \sqrt{2E/m}$. The angular momentum about the target is the asymptotic momentum times the perpendicular distance $b$:

**第 1 步 — 远处的守恒量。** 远离靶时 $U \to 0$，故渐近速率 $v_\infty$ 满足 $E = \tfrac12 m v_\infty^2$，给出 $v_\infty = \sqrt{2E/m}$。绕靶的角动量等于渐近动量乘以垂直距离 $b$：

$$ \ell = m v_\infty b = m b \sqrt{2E/m} = b \sqrt{2mE}. $$

**Step 2 — Energy conservation in the orbit.** Using polar coordinates $(r, \varphi)$ centred on the target, the energy and angular momentum are

**第 2 步 — 轨道中的能量守恒。** 以靶为中心用极坐标 $(r, \varphi)$，能量与角动量为

$$ E = \tfrac12 m(\dot{r}^2 + r^2\dot{\varphi}^2) + U(r), \qquad \ell = m r^2\dot{\varphi}. $$

Eliminate $\dot{\varphi} = \ell/(m r^2)$ to obtain the radial energy equation:

消去 $\dot{\varphi} = \ell/(m r^2)$，得径向能量方程：

$$ E = \tfrac12 m\dot{r}^2 + \frac{\ell^2}{2m r^2} + U(r) \implies \dot{r} = \pm\sqrt{\frac{2}{m}(E - U(r)) - \frac{\ell^2}{m^2 r^2}}. $$

**Step 3 — The orbit equation $d\varphi/dr$.** Divide $\dot{\varphi}$ by $\dot{r}$ to remove time:

**第 3 步 — 轨道方程 $d\varphi/dr$。** 用 $\dot{\varphi}$ 除以 $\dot{r}$ 以消去时间：

$$ \frac{d\varphi}{dr} = \frac{\dot{\varphi}}{\dot{r}} = \frac{\ell/(m r^2)}{\pm\sqrt{\frac{2}{m}(E - U) - \frac{\ell^2}{m^2 r^2}}}. $$

Multiplying numerator and denominator inside the root by $m^2$ gives the standard form:

将根号内的分子与分母同乘 $m^2$，得标准形式：

$$ \frac{d\varphi}{dr} = \frac{\ell/r^2}{\sqrt{2m(E - U(r)) - \ell^2/r^2}}. $$

**Step 4 — The angle swept to the turning point.** The distance of closest approach $r_{\min}$ is the turning point where $\dot{r} = 0$, i.e. the largest root of $2m(E - U(r)) - \ell^2/r^2 = 0$. The angle $\varphi_0$ swept as the particle travels in from $r = \infty$ to $r = r_{\min}$ is the integral of $d\varphi/dr$:

**第 4 步 — 扫过至最近点的角度。** 最近距离 $r_{\min}$ 是转折点，满足 $\dot{r} = 0$，即 $2m(E - U(r)) - \ell^2/r^2 = 0$ 的最大根。粒子从 $r = \infty$ 运动到 $r = r_{\min}$ 扫过的角度 $\varphi_0$ 为 $d\varphi/dr$ 的积分：

$$ \varphi_0 = \int_{r_{\min}}^\infty \frac{(\ell/r^2)\,dr}{\sqrt{2m(E - U(r)) - \ell^2/r^2}}. $$

**Step 5 — Symmetry gives the scattering angle.** The orbit is symmetric about the line through $r_{\min}$ (the apsidal line): the incoming and outgoing branches each sweep the same angle $\varphi_0$. The total angle between the two asymptotes is therefore $2\varphi_0$. The scattering angle $\theta$ is the supplement of this — the angle by which the outgoing asymptote is rotated from the straight-through direction:

**第 5 步 — 对称性给出散射角。** 轨道关于过 $r_{\min}$ 的直线（拱点线）对称：入射与出射两支各扫过相同的角度 $\varphi_0$。故两条渐近线之间的总角度为 $2\varphi_0$。散射角 $\theta$ 是其补角——即出射渐近线相对于直穿方向转过的角度：

$$ \boxed{\, \theta = \pi - 2\varphi_0 \,} \qquad \blacksquare $$

---

## C. Rutherford Scattering · 卢瑟福散射

**Claim.** For the repulsive Coulomb potential $U(r) = k/r$ with $k = q_1 q_2/(4\pi\varepsilon_0)$, the impact parameter and scattering angle obey

**命题。** 对排斥性库仑势 $U(r) = k/r$，其中 $k = q_1 q_2/(4\pi\varepsilon_0)$，瞄准距离与散射角满足

$$ b = \frac{k}{2E}\cot(\theta/2), $$

and the differential cross section is the **Rutherford formula**

且微分散射截面为**卢瑟福公式**

$$ \frac{d\sigma}{d\Omega} = \frac{(k/4E)^2}{\sin^4(\theta/2)} = \frac{[q_1 q_2/(16\pi\varepsilon_0 E)]^2}{\sin^4(\theta/2)}. $$

**Step 1 — Reduce the orbit integral.** From Section B with $U = k/r$,

**第 1 步 — 化简轨道积分。** 由 B 节，取 $U = k/r$，

$$ \varphi_0 = \int_{r_{\min}}^\infty \frac{(\ell/r^2)\,dr}{\sqrt{2m(E - k/r) - \ell^2/r^2}}. $$

Substitute $u = 1/r$, so $du = -dr/r^2$ and the limits run from $u = 0$ ($r = \infty$) to $u = u_{\max} = 1/r_{\min}$:

代换 $u = 1/r$，则 $du = -dr/r^2$，积分限从 $u = 0$（$r = \infty$）到 $u = u_{\max} = 1/r_{\min}$：

$$ \varphi_0 = \int_0^{u_{\max}} \frac{\ell\,du}{\sqrt{2mE - 2mk u - \ell^2 u^2}}. $$

**Step 2 — Complete the square.** Write the radicand as a downward parabola in $u$. Factor out $\ell^2$:

**第 2 步 — 配方。** 将根式内写为关于 $u$ 的开口向下的抛物线。提出 $\ell^2$：

$$ 2mE - 2mk u - \ell^2 u^2 = \ell^2\left[\frac{2mE}{\ell^2} - \frac{2mk}{\ell^2} u - u^2\right]. $$

Completing the square in $u$ with centre $u_0 = mk/\ell^2$:

对 $u$ 配方，中心为 $u_0 = mk/\ell^2$：

$$ = \ell^2\left[\left(\frac{2mE}{\ell^2} + \frac{m^2 k^2}{\ell^4}\right) - \left(u + \frac{mk}{\ell^2}\right)^2\right] = \ell^2\left[A^2 - (u + u_0)^2\right], $$

where $A^2 = 2mE/\ell^2 + m^2 k^2/\ell^4$. The integral becomes a standard arccosine form:

其中 $A^2 = 2mE/\ell^2 + m^2 k^2/\ell^4$。积分化为标准反余弦形式：

$$ \varphi_0 = \int_0^{u_{\max}} \frac{du}{\sqrt{A^2 - (u + u_0)^2}} = \left[\arccos\!\left(\frac{u + u_0}{A}\right)\right] \text{ evaluated between limits.} $$

**Step 3 — Evaluate at the limits.** The turning point $u_{\max}$ is the positive root of the radicand, i.e. where $A^2 - (u_{\max} + u_0)^2 = 0$, so $(u_{\max} + u_0)/A = 1$ and $\arccos$ gives $0$ there. At $u = 0$, $(0 + u_0)/A = u_0/A$. Hence

**第 3 步 — 代入积分限。** 转折点 $u_{\max}$ 是根式的正根，即 $A^2 - (u_{\max} + u_0)^2 = 0$，故 $(u_{\max} + u_0)/A = 1$，其反余弦为 $0$。在 $u = 0$ 处，$(0 + u_0)/A = u_0/A$。故

$$ \varphi_0 = \arccos\!\left(\frac{u_0}{A}\right) \implies \cos\varphi_0 = \frac{u_0}{A} = \frac{mk/\ell^2}{\sqrt{2mE/\ell^2 + m^2 k^2/\ell^4}}. $$

**Step 4 — Simplify $\cos\varphi_0$.** Multiply numerator and denominator by $\ell^2$:

**第 4 步 — 化简 $\cos\varphi_0$。** 分子与分母同乘 $\ell^2$：

$$ \cos\varphi_0 = \frac{mk}{\sqrt{2mE\ell^2 + m^2 k^2}} = \frac{mk}{\sqrt{m^2 k^2 + 2mE\ell^2}}. $$

Divide top and bottom by $mk$:

上下同除以 $mk$：

$$ \cos\varphi_0 = \frac{1}{\sqrt{1 + 2E\ell^2/(m k^2)}}. $$

Now insert $\ell^2 = 2mE b^2$ (from Section B, $\ell = b\sqrt{2mE}$):

代入 $\ell^2 = 2mE b^2$（由 B 节，$\ell = b\sqrt{2mE}$）：

$$ \frac{2E\ell^2}{m k^2} = \frac{2E \cdot 2mE b^2}{m k^2} = \left(\frac{2E b}{k}\right)^2. $$

Therefore

故

$$ \cos\varphi_0 = \frac{1}{\sqrt{1 + (2E b/k)^2}}. $$

**Step 5 — Convert to the scattering angle.** From $\theta = \pi - 2\varphi_0$ we have $\varphi_0 = \pi/2 - \theta/2$, so $\cos\varphi_0 = \sin(\theta/2)$ and the relation reads

**第 5 步 — 转换为散射角。** 由 $\theta = \pi - 2\varphi_0$ 得 $\varphi_0 = \pi/2 - \theta/2$，故 $\cos\varphi_0 = \sin(\theta/2)$，关系式为

$$ \sin(\theta/2) = \frac{1}{\sqrt{1 + (2E b/k)^2}} \implies 1 + (2E b/k)^2 = \frac{1}{\sin^2(\theta/2)} = \csc^2(\theta/2). $$

Subtract 1 and use $\csc^2(\theta/2) - 1 = \cot^2(\theta/2)$:

减去 1 并利用 $\csc^2(\theta/2) - 1 = \cot^2(\theta/2)$：

$$ (2E b/k)^2 = \cot^2(\theta/2) \implies 2E b/k = \cot(\theta/2) \implies \boxed{\, b = \frac{k}{2E}\cot(\theta/2) \,}. $$

**Step 6 — Differentiate $b(\theta)$.** Using $\frac{d}{dx}[\cot x] = -\csc^2 x$:

**第 6 步 — 对 $b(\theta)$ 求导。** 利用 $\frac{d}{dx}[\cot x] = -\csc^2 x$：

$$ \frac{db}{d\theta} = \frac{k}{2E} \cdot (-\csc^2(\theta/2)) \cdot \frac{1}{2} = -\frac{k}{4E}\csc^2(\theta/2). $$

So $|db/d\theta| = (k/4E)\csc^2(\theta/2) = (k/4E)/\sin^2(\theta/2)$.

故 $|db/d\theta| = (k/4E)\csc^2(\theta/2) = (k/4E)/\sin^2(\theta/2)$。

**Step 7 — Assemble the cross section.** Insert $b$ and $|db/d\theta|$ into $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$, and use the half-angle identity $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$:

**第 7 步 — 组装截面。** 将 $b$ 与 $|db/d\theta|$ 代入 $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$，并用半角恒等式 $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$：

$$ \frac{d\sigma}{d\Omega} = \left[\frac{k}{2E}\cot(\theta/2)\right] \cdot \left[\frac{1}{2\sin(\theta/2)\cos(\theta/2)}\right] \cdot \left[\frac{k/4E}{\sin^2(\theta/2)}\right]. $$

Write $\cot(\theta/2) = \cos(\theta/2)/\sin(\theta/2)$ and collect the prefactors $(k/2E)\cdot(k/4E) = k^2/(8E^2)$:

写 $\cot(\theta/2) = \cos(\theta/2)/\sin(\theta/2)$，并合并前因子 $(k/2E)\cdot(k/4E) = k^2/(8E^2)$：

$$ \frac{d\sigma}{d\Omega} = \frac{k^2}{8E^2} \cdot \left[\frac{\cos(\theta/2)}{\sin(\theta/2)}\right] \cdot \left[\frac{1}{2\sin(\theta/2)\cos(\theta/2)}\right] \cdot \left[\frac{1}{\sin^2(\theta/2)}\right]. $$

**Step 8 — Cancel cleanly.** The $\cos(\theta/2)$ in the numerator cancels the $\cos(\theta/2)$ in the denominator; the three $\sin(\theta/2)$ factors and the explicit $\sin^2(\theta/2)$ combine to $\sin^4(\theta/2)$; the factor 2 in the denominator turns $k^2/(8E^2)$ into $k^2/(16E^2)$:

**第 8 步 — 干净相消。** 分子的 $\cos(\theta/2)$ 与分母的 $\cos(\theta/2)$ 相消；三个 $\sin(\theta/2)$ 因子与显式的 $\sin^2(\theta/2)$ 合并为 $\sin^4(\theta/2)$；分母的因子 2 使 $k^2/(8E^2)$ 变为 $k^2/(16E^2)$：

$$ \frac{d\sigma}{d\Omega} = \frac{k^2}{16E^2} \cdot \frac{1}{\sin^4(\theta/2)} = \frac{(k/4E)^2}{\sin^4(\theta/2)}. $$

Finally substitute $k = q_1 q_2/(4\pi\varepsilon_0)$, giving $k/4E = q_1 q_2/(16\pi\varepsilon_0 E)$:

最后代入 $k = q_1 q_2/(4\pi\varepsilon_0)$，得 $k/4E = q_1 q_2/(16\pi\varepsilon_0 E)$：

$$ \boxed{\, \frac{d\sigma}{d\Omega} = \frac{(k/4E)^2}{\sin^4(\theta/2)} = \frac{[q_1 q_2/(16\pi\varepsilon_0 E)]^2}{\sin^4(\theta/2)} \,} \qquad \blacksquare $$

---

## D. Divergence of the Total Cross Section · 总截面的发散

**Claim.** The total cross section $\sigma_{\text{tot}} = \int(d\sigma/d\Omega)\,d\Omega$ for the Coulomb potential **diverges**, due to the dominant forward (small-$\theta$) scattering — a direct consequence of the infinite range of the $1/r$ potential. A screened or finite-range potential restores a finite $\sigma_{\text{tot}}$.

**命题。** 库仑势的总截面 $\sigma_{\text{tot}} = \int(d\sigma/d\Omega)\,d\Omega$ **发散**，源于主导的前向（小 $\theta$）散射——这是 $1/r$ 势无穷力程的直接后果。屏蔽势或有限力程势可恢复有限的 $\sigma_{\text{tot}}$。

**Step 1 — Write the total cross section integral.** Integrate the Rutherford cross section over all solid angles, $d\Omega = 2\pi \sin\theta\,d\theta$ (azimuthal symmetry):

**第 1 步 — 写出总截面积分。** 对所有立体角积分卢瑟福截面，$d\Omega = 2\pi \sin\theta\,d\theta$（方位对称）：

$$ \sigma_{\text{tot}} = \int \frac{d\sigma}{d\Omega}\,d\Omega = \int_0^\pi \frac{(k/4E)^2}{\sin^4(\theta/2)} \cdot 2\pi \sin\theta\,d\theta. $$

**Step 2 — Reduce the integrand.** Use $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$:

**第 2 步 — 化简被积函数。** 用 $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$：

$$ \sigma_{\text{tot}} = 2\pi(k/4E)^2 \int_0^\pi \frac{2\sin(\theta/2)\cos(\theta/2)}{\sin^4(\theta/2)}\,d\theta = 4\pi(k/4E)^2 \int_0^\pi \frac{\cos(\theta/2)}{\sin^3(\theta/2)}\,d\theta. $$

**Step 3 — Examine the small-angle behaviour.** As $\theta \to 0$, $\cos(\theta/2) \to 1$ and $\sin(\theta/2) \approx \theta/2$, so the integrand behaves like

**第 3 步 — 检查小角行为。** 当 $\theta \to 0$ 时，$\cos(\theta/2) \to 1$，$\sin(\theta/2) \approx \theta/2$，故被积函数表现为

$$ \frac{\cos(\theta/2)}{\sin^3(\theta/2)} \approx \frac{1}{(\theta/2)^3} = \frac{8}{\theta^3}. $$

The integral $\int_0 d\theta/\theta^3 \sim [-1/(2\theta^2)]$ diverges at the lower limit $\theta \to 0$. Equivalently, substituting $w = \sin(\theta/2)$, $dw = \tfrac12\cos(\theta/2)\,d\theta$, the integral becomes $2\int dw/w^3 = [-1/w^2]$, which diverges as $w \to 0$:

积分 $\int_0 d\theta/\theta^3 \sim [-1/(2\theta^2)]$ 在下限 $\theta \to 0$ 处发散。等价地，代换 $w = \sin(\theta/2)$，$dw = \tfrac12\cos(\theta/2)\,d\theta$，积分变为 $2\int dw/w^3 = [-1/w^2]$，当 $w \to 0$ 时发散：

$$ \sigma_{\text{tot}} \to \infty. $$

**Step 4 — Physical interpretation.** The divergence comes entirely from $\theta \to 0$, i.e. from arbitrarily **large impact parameters** $b \to \infty$. Because the Coulomb force $1/r^2$ never truly vanishes, even particles passing extremely far away are deflected by a tiny but nonzero angle; integrating their (large) cross-sectional contributions over all $b$ up to infinity diverges. There is no finite "size" to a pure Coulomb target.

**第 4 步 — 物理诠释。** 发散完全来自 $\theta \to 0$，即来自任意**大的瞄准距离** $b \to \infty$。由于库仑力 $1/r^2$ 从不真正消失，即便从极远处经过的粒子也被偏转一个微小但非零的角度；将它们（巨大的）截面贡献对所有直至无穷的 $b$ 积分便发散。纯库仑靶没有有限的"尺寸"。

**Step 5 — Screening restores finiteness.** A real charge is screened by surrounding charges, giving a finite-range Yukawa-type potential $U(r) = (k/r) e^{-r/a}$ with screening length $a$. Beyond $r \gtrsim a$ the potential is exponentially suppressed, so there is a minimum deflection angle $\theta_{\min} \sim k/(E a)$ below which particles are effectively undeflected. Cutting the integral off at $\theta_{\min}$ makes it convergent:

**第 5 步 — 屏蔽恢复有限性。** 真实电荷被周围电荷屏蔽，给出有限力程的汤川型势 $U(r) = (k/r) e^{-r/a}$，屏蔽长度为 $a$。当 $r \gtrsim a$ 时势被指数压低，故存在最小偏转角 $\theta_{\min} \sim k/(E a)$，低于此角粒子实际上不被偏转。在 $\theta_{\min}$ 处截断积分使其收敛：

$$ \sigma_{\text{tot}} \sim 4\pi(k/4E)^2 \int_{\theta_{\min}}^\pi \frac{\cos(\theta/2)}{\sin^3(\theta/2)}\,d\theta \sim 4\pi(k/4E)^2 \cdot \frac{1}{\sin^2(\theta_{\min}/2)} < \infty. $$

Hence the infinite cross section is a peculiarity of the strictly infinite-range Coulomb force; any finite-range (screened) interaction yields a finite total cross section of order $\pi a^2$. $\blacksquare$

故无穷大截面是严格无穷力程库仑力的特殊性质；任何有限力程（屏蔽）相互作用都给出量级为 $\pi a^2$ 的有限总截面。$\blacksquare$

---

*The classical Rutherford cross section $d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2)$ is one of the rare cases where the full quantum (Born-approximation) result coincides exactly with the classical one (Module 3.8) — the $1/\sin^4(\theta/2)$ law and its small-angle divergence survive the transition to wave mechanics. Historically (Module 9.3) the unexpected large-angle tail of this distribution revealed the atomic nucleus; at GeV energies the same large-angle excess in deep inelastic scattering (Module 8.9) revealed pointlike quarks inside the proton.*

*经典卢瑟福截面 $d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2)$ 是少数完整量子（玻恩近似）结果与经典结果完全一致的情形之一（模块 3.8）——$1/\sin^4(\theta/2)$ 定律及其小角发散在过渡到波动力学时依然成立。历史上（模块 9.3）这一分布出乎意料的大角度尾部揭示了原子核；在 GeV 能标下，深度非弹性散射（模块 8.9）中同样的大角度超出揭示了质子内部点状的夸克。*

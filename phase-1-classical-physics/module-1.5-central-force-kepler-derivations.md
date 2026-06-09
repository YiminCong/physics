---
title: "Derivations — Module 1.5: Central Force & Kepler"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.5: Central Force & Kepler
# 推导 — 模块 1.5：有心力与开普勒定律

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.5](./module-1.5-central-force-kepler.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.5](./module-1.5-central-force-kepler.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Two-Body Reduction to One-Body with Reduced Mass · 二体问题化为约化质量单体问题

**Claim.** The two-body problem with positions $\mathbf{r}_1, \mathbf{r}_2$ and masses $m_1, m_2$ interacting through $V(|\mathbf{r}_1 - \mathbf{r}_2|)$ separates into (i) free motion of the centre of mass, and (ii) one-body motion in $V(r)$ with reduced mass $\mu = m_1 m_2/(m_1 + m_2)$ and relative coordinate $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$.

**命题。** 位置为 $\mathbf{r}_1$、$\mathbf{r}_2$，质量为 $m_1$、$m_2$，通过 $V(|\mathbf{r}_1 - \mathbf{r}_2|)$ 相互作用的二体问题可分离为：(i) 质心的自由运动；(ii) 相对坐标 $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$ 在势 $V(r)$ 中以约化质量 $\mu = m_1 m_2/(m_1 + m_2)$ 运动的单体问题。

**Step 1 — Define the coordinates.** Introduce the centre-of-mass position $\mathbf{R}$ and relative coordinate $\mathbf{r}$:

**第 1 步 — 定义坐标。** 引入质心位置 $\mathbf{R}$ 和相对坐标 $\mathbf{r}$：

$$ \mathbf{R} = \frac{m_1\mathbf{r}_1 + m_2\mathbf{r}_2}{m_1 + m_2}, \qquad \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2. $$

The inverse relations: $\mathbf{r}_1 = \mathbf{R} + (m_2/M)\,\mathbf{r}$, $\mathbf{r}_2 = \mathbf{R} - (m_1/M)\,\mathbf{r}$, where $M = m_1 + m_2$.

逆关系：$\mathbf{r}_1 = \mathbf{R} + (m_2/M)\,\mathbf{r}$，$\mathbf{r}_2 = \mathbf{R} - (m_1/M)\,\mathbf{r}$，其中 $M = m_1 + m_2$。

**Step 2 — Write the kinetic energy in new coordinates.** Compute $\dot{\mathbf{r}}_1$ and $\dot{\mathbf{r}}_2$:

**第 2 步 — 用新坐标写动能。** 计算 $\dot{\mathbf{r}}_1$ 和 $\dot{\mathbf{r}}_2$：

$$ \dot{\mathbf{r}}_1 = \dot{\mathbf{R}} + (m_2/M)\,\dot{\mathbf{r}}, \qquad \dot{\mathbf{r}}_2 = \dot{\mathbf{R}} - (m_1/M)\,\dot{\mathbf{r}}. $$

The total kinetic energy $T = \tfrac12 m_1|\dot{\mathbf{r}}_1|^2 + \tfrac12 m_2|\dot{\mathbf{r}}_2|^2$:

总动能 $T = \tfrac12 m_1|\dot{\mathbf{r}}_1|^2 + \tfrac12 m_2|\dot{\mathbf{r}}_2|^2$：

$$ \begin{aligned}
T &= \tfrac12 m_1\big|\dot{\mathbf{R}} + (m_2/M)\dot{\mathbf{r}}\big|^2 + \tfrac12 m_2\big|\dot{\mathbf{R}} - (m_1/M)\dot{\mathbf{r}}\big|^2 \\
&= \tfrac12(m_1 + m_2)|\dot{\mathbf{R}}|^2 + \tfrac12 m_1(m_2/M)^2|\dot{\mathbf{r}}|^2 + \tfrac12 m_2(m_1/M)^2|\dot{\mathbf{r}}|^2 \\
&\quad + \big(m_1(m_2/M) - m_2(m_1/M)\big)\,\dot{\mathbf{R}} \cdot \dot{\mathbf{r}}.
\end{aligned} $$

The cross terms vanish because $m_1(m_2/M) - m_2(m_1/M) = 0$. The second and third terms combine:

交叉项消失，因为 $m_1(m_2/M) - m_2(m_1/M) = 0$。第二、三项合并：

$$ m_1(m_2/M)^2 + m_2(m_1/M)^2 = (m_1 m_2/M^2)(m_2 + m_1) = m_1 m_2/M = \mu. $$

Therefore:

因此：

$$ \boxed{\, T = \tfrac12 M|\dot{\mathbf{R}}|^2 + \tfrac12 \mu|\dot{\mathbf{r}}|^2 \,} $$

**Step 3 — Write the Lagrangian.** Since $V$ depends only on $r = |\mathbf{r}|$:

**第 3 步 — 写出拉格朗日量。** 由于 $V$ 仅依赖 $r = |\mathbf{r}|$：

$$ L = T - V = \tfrac12 M\dot{\mathbf{R}}^2 + \tfrac12 \mu\dot{\mathbf{r}}^2 - V(r). $$

The Lagrangian separates: the $\mathbf{R}$ degrees of freedom give free CM motion ($\partial L/\partial \mathbf{R} = 0 \implies M\ddot{\mathbf{R}} = 0$), and the $\mathbf{r}$ degrees of freedom give a one-body problem:

拉格朗日量分离：$\mathbf{R}$ 自由度给出 CM 自由运动（$\partial L/\partial \mathbf{R} = 0 \implies M\ddot{\mathbf{R}} = 0$），$\mathbf{r}$ 自由度给出单体问题：

$$ \mu\ddot{\mathbf{r}} = -\nabla_{\mathbf{r}}V(r). $$

This is exactly Newton's equation for a particle of mass $\mu$ in potential $V(r)$. $\blacksquare$

这恰好是质量为 $\mu$ 的粒子在势 $V(r)$ 中的牛顿方程。$\blacksquare$

---

## B. Effective Potential and Radial Equation · 有效势与径向方程

**Claim.** For a particle of mass $\mu$ moving under central force $V(r)$, the radial motion is governed by the one-dimensional equation $\tfrac12 \mu\dot{r}^2 + V_\text{eff}(r) = E$, where $V_\text{eff}(r) = V(r) + L^2/(2\mu r^2)$ and $L = \mu r^2\dot{\varphi}$ is the conserved angular momentum.

**命题。** 对于质量为 $\mu$ 的粒子在有心力 $V(r)$ 下运动，径向运动由一维方程 $\tfrac12 \mu\dot{r}^2 + V_\text{eff}(r) = E$ 控制，其中 $V_\text{eff}(r) = V(r) + L^2/(2\mu r^2)$，$L = \mu r^2\dot{\varphi}$ 为守恒角动量。

**Step 1 — Write kinetic energy in polar coordinates.** In the orbital plane:

**第 1 步 — 用极坐标写动能。** 在轨道平面内：

$$ T = \tfrac12 \mu(\dot{r}^2 + r^2\dot{\varphi}^2). $$

**Step 2 — Eliminate $\dot{\varphi}$ using angular momentum conservation.** From $L = \mu r^2\dot{\varphi}$:

**第 2 步 — 利用角动量守恒消去 $\dot{\varphi}$。** 由 $L = \mu r^2\dot{\varphi}$：

$$ \dot{\varphi} = \frac{L}{\mu r^2}. $$

Substitute into $T$:

代入 $T$：

$$ T = \tfrac12 \mu\dot{r}^2 + \tfrac12 \mu r^2 \cdot \frac{L^2}{\mu^2 r^4} = \tfrac12 \mu\dot{r}^2 + \frac{L^2}{2\mu r^2}. $$

**Step 3 — Write the total energy.** $E = T + V$:

**第 3 步 — 写出总能量。** $E = T + V$：

$$ E = \tfrac12 \mu\dot{r}^2 + \frac{L^2}{2\mu r^2} + V(r) = \tfrac12 \mu\dot{r}^2 + V_\text{eff}(r), $$

where $\boxed{\,V_\text{eff}(r) = V(r) + L^2/(2\mu r^2)\,}$. The term $L^2/(2\mu r^2)$ acts as a centrifugal barrier repelling the particle from the origin. $\blacksquare$

其中 $\boxed{\,V_\text{eff}(r) = V(r) + L^2/(2\mu r^2)\,}$。项 $L^2/(2\mu r^2)$ 作为离心势垒使粒子远离原点。$\blacksquare$

---

## C. Orbit Equation via Binet Substitution · 通过比内代换推导轨道方程

**Claim.** For the gravitational potential $V(r) = -GM\mu/r$, the orbit equation in polar coordinates is the conic section $r(\varphi) = p/(1 + \varepsilon \cos\varphi)$, where $p = L^2/(GM\mu^2)$ is the semi-latus rectum and $\varepsilon$ is the eccentricity determined by the energy.

**命题。** 对于引力势 $V(r) = -GM\mu/r$，极坐标中的轨道方程为圆锥曲线 $r(\varphi) = p/(1 + \varepsilon \cos\varphi)$，其中 $p = L^2/(GM\mu^2)$ 为半通径，$\varepsilon$ 为由能量决定的离心率。

**Step 1 — Set up the orbit equation.** We want $r$ as a function of $\varphi$. Use the Binet substitution $u = 1/r$. Compute $dr/dt$ in terms of $d\varphi/dt$:

**第 1 步 — 建立轨道方程。** 我们求 $r$ 作为 $\varphi$ 的函数。使用比内代换 $u = 1/r$。用 $d\varphi/dt$ 计算 $dr/dt$：

$$ \dot{r} = \frac{dr}{dt} = \frac{dr}{d\varphi}\frac{d\varphi}{dt} = \frac{dr}{d\varphi} \cdot \frac{L}{\mu r^2}. $$

Since $r = 1/u$: $dr/d\varphi = -(1/u^2)(du/d\varphi) = -r^2(du/d\varphi)$. Therefore:

由于 $r = 1/u$：$dr/d\varphi = -(1/u^2)(du/d\varphi) = -r^2(du/d\varphi)$。因此：

$$ \dot{r} = -r^2\frac{du}{d\varphi} \cdot \frac{L}{\mu r^2} = -\frac{L}{\mu}\frac{du}{d\varphi}. $$

**Step 2 — Compute $\ddot{r}$.** Differentiate $\dot{r}$ with respect to $t$:

**第 2 步 — 计算 $\ddot{r}$。** 对 $\dot{r}$ 关于 $t$ 求导：

$$ \ddot{r} = -\frac{L}{\mu}\frac{d^2u}{d\varphi^2}\frac{d\varphi}{dt} = -\frac{L}{\mu}\frac{d^2u}{d\varphi^2}\frac{Lu^2}{\mu} = -\frac{L^2u^2}{\mu^2}\frac{d^2u}{d\varphi^2}. $$

**Step 3 — Write the radial equation of motion.** From $\mu(\ddot{r} - r\dot{\varphi}^2) = F(r) = -dV/dr = -GM\mu u^2$:

**第 3 步 — 写出径向运动方程。** 由 $\mu(\ddot{r} - r\dot{\varphi}^2) = F(r) = -dV/dr = -GM\mu u^2$：

$$ \mu\Big[-\frac{L^2u^2}{\mu^2}\frac{d^2u}{d\varphi^2} - \frac{1}{u}\Big(\frac{Lu^2}{\mu}\Big)^2\Big] = -GM\mu u^2. $$

Simplify each term. The second term: $-(1/u)(L^2u^4/\mu^2) = -L^2u^3/\mu^2$. Divide the entire equation by $-\mu L^2u^2/\mu^2 = -L^2u^2/\mu$:

化简每项。第二项：$-(1/u)(L^2u^4/\mu^2) = -L^2u^3/\mu^2$。将整个方程除以 $-\mu L^2u^2/\mu^2 = -L^2u^2/\mu$：

$$ \frac{d^2u}{d\varphi^2} + u = \frac{GM\mu^2}{L^2}. $$

**Step 4 — Solve the ODE.** This is a harmonic oscillator ODE with a constant forcing term. The general solution is:

**第 4 步 — 求解常微分方程。** 这是带常数强迫项的谐振子方程。通解为：

$$ u(\varphi) = \frac{GM\mu^2}{L^2} + A\cos(\varphi - \varphi_0). $$

Choose the orientation so that $\varphi_0 = 0$ (periapsis at $\varphi = 0$). Then $u = (1/p)(1 + \varepsilon \cos\varphi)$, where $p = L^2/(GM\mu^2)$ and $\varepsilon = A p$.

选取方向使得 $\varphi_0 = 0$（近心点在 $\varphi = 0$ 处）。则 $u = (1/p)(1 + \varepsilon \cos\varphi)$，其中 $p = L^2/(GM\mu^2)$，$\varepsilon = A p$。

**Step 5 — Recover $r(\varphi)$.** Since $r = 1/u$:

**第 5 步 — 还原 $r(\varphi)$。** 由于 $r = 1/u$：

$$ \boxed{\, r(\varphi) = \frac{p}{1 + \varepsilon \cos\varphi} \,} \qquad \blacksquare $$

This is a **conic section** with focus at the origin, semi-latus rectum $p$, and eccentricity $\varepsilon$. It is an ellipse ($\varepsilon < 1$), parabola ($\varepsilon = 1$), or hyperbola ($\varepsilon > 1$).

这是以原点为焦点的**圆锥曲线**，半通径为 $p$，离心率为 $\varepsilon$。$\varepsilon < 1$ 为椭圆，$\varepsilon = 1$ 为抛物线，$\varepsilon > 1$ 为双曲线。

---

## D. The Three Kepler Laws · 开普勒三定律

### D.1 Kepler's First Law — Elliptical Orbits · 第一定律——椭圆轨道

The orbit equation $r = p/(1 + \varepsilon \cos\varphi)$ is an ellipse for $\varepsilon < 1$, with the centre of force (Sun) at one focus. This was derived in Section C above. For bound orbits $E < 0$, the eccentricity is:

轨道方程 $r = p/(1 + \varepsilon \cos\varphi)$ 在 $\varepsilon < 1$ 时为椭圆，力心（太阳）在一个焦点处。这已在第 C 节推导。对于束缚轨道 $E < 0$，离心率为：

$$ \varepsilon = \sqrt{1 + \frac{2EL^2}{G^2M^2\mu^3}}. $$

When $E < 0$: $\varepsilon < 1$, confirming an ellipse. $\blacksquare$

当 $E < 0$ 时：$\varepsilon < 1$，确认为椭圆。$\blacksquare$

### D.2 Kepler's Second Law — Equal Areas in Equal Times · 第二定律——等面积定律

**Claim.** The line from the Sun to the planet sweeps equal areas in equal times: $dA/dt = L/(2\mu) = \text{const}$.

**命题。** 从太阳到行星的连线在相等时间内扫过相等面积：$dA/dt = L/(2\mu) = $ 常数。

**Proof.** In time $dt$, the position vector $\mathbf{r}$ sweeps out a triangle of area $dA = \tfrac12|\mathbf{r} \times d\mathbf{r}| = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}\,dt| = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}|\,dt$. Therefore:

**证明。** 在时间 $dt$ 内，位置矢量 $\mathbf{r}$ 扫过面积 $dA = \tfrac12|\mathbf{r} \times d\mathbf{r}| = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}\,dt| = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}|\,dt$。因此：

$$ \frac{dA}{dt} = \tfrac12|\mathbf{r} \times \dot{\mathbf{r}}| = \tfrac12|L/\mu| = \frac{L}{2\mu} = \text{const}, $$

since $L$ is conserved for a central force (proved in Module 1.2 derivations). $\blacksquare$

由于 $L$ 对有心力守恒（已在模块 1.2 推导中证明）。$\blacksquare$

### D.3 Kepler's Third Law — $T^2 = 4\pi^2 a^3/(GM)$ · 第三定律——$T^2 = 4\pi^2 a^3/(GM)$

**Claim.** The orbital period $T$ and semi-major axis $a$ satisfy $T^2 = 4\pi^2 a^3/(GM)$.

**命题。** 轨道周期 $T$ 与半长轴 $a$ 满足 $T^2 = 4\pi^2 a^3/(GM)$。

**Step 1 — Relate the period to the area.** The total area swept per orbit is the area of the ellipse: $A_\text{ellipse} = \pi ab$, where $a$ is the semi-major axis and $b$ is the semi-minor axis. Using $dA/dt = L/(2\mu)$:

**第 1 步 — 将周期与面积联系起来。** 每个轨道扫过的总面积是椭圆面积：$A_\text{ellipse} = \pi ab$，其中 $a$ 为半长轴，$b$ 为半短轴。利用 $dA/dt = L/(2\mu)$：

$$ T = \frac{A_\text{ellipse}}{dA/dt} = \frac{\pi ab}{L/(2\mu)} = \frac{2\pi\mu ab}{L}. $$

**Step 2 — Express $b$ and $p$ in terms of $a$ and $\varepsilon$.** For an ellipse with semi-major axis $a$ and eccentricity $\varepsilon$:

**第 2 步 — 用 $a$ 和 $\varepsilon$ 表示 $b$ 和 $p$。** 对于半长轴为 $a$、离心率为 $\varepsilon$ 的椭圆：

$$ b = a\sqrt{1 - \varepsilon^2}, \qquad p = b^2/a = a(1 - \varepsilon^2). $$

**Step 3 — Substitute into the period formula.**

**第 3 步 — 代入周期公式。**

$$ T = \frac{2\pi\mu ab}{L} = \frac{2\pi\mu \cdot a \cdot a\sqrt{1 - \varepsilon^2}}{L} = \frac{2\pi\mu a^2\sqrt{1 - \varepsilon^2}}{L}. $$

**Step 4 — Use the relation $p = L^2/(GM\mu^2)$.** From Step 2, $p = a(1 - \varepsilon^2)$, so:

**第 4 步 — 利用关系 $p = L^2/(GM\mu^2)$。** 由第 2 步，$p = a(1 - \varepsilon^2)$，故：

$$ L^2 = GM\mu^2 p = GM\mu^2 a(1 - \varepsilon^2). $$

Therefore $L = \mu\sqrt{GMa(1 - \varepsilon^2)}$.

因此 $L = \mu\sqrt{GMa(1 - \varepsilon^2)}$。

**Step 5 — Compute $T^2$.** Substituting into Step 3:

**第 5 步 — 计算 $T^2$。** 代入第 3 步：

$$ \begin{aligned}
T &= \frac{2\pi\mu a^2\sqrt{1 - \varepsilon^2}}{\mu\sqrt{GMa(1 - \varepsilon^2)}} \\
&= \frac{2\pi a^2\sqrt{1 - \varepsilon^2}}{\sqrt{GMa(1 - \varepsilon^2)}} \\
&= \frac{2\pi a^2}{\sqrt{GMa}} \\
&= \frac{2\pi a^{3/2}}{\sqrt{GM}}.
\end{aligned} $$

Squaring:

平方：

$$ \boxed{\, T^2 = \frac{4\pi^2 a^3}{GM} \,} \qquad \blacksquare $$

The period depends only on the semi-major axis and the total mass, independent of eccentricity and the planet's mass (since $\mu \approx m_\text{planet} \ll M_\text{Sun}$).

周期只依赖于半长轴和总质量，与离心率和行星质量无关（因为 $\mu \approx m_\text{planet} \ll M_\text{Sun}$）。

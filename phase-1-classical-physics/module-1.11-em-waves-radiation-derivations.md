---
title: "Derivations — Module 1.11: Electromagnetic Waves & Radiation"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.11: Electromagnetic Waves & Radiation
# 推导 — 模块 1.11：电磁波与辐射

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.11](./module-1.11-em-waves-radiation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.11](./module-1.11-em-waves-radiation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Deriving the Wave Equation and $c = 1/\sqrt{\mu_0\epsilon_0}$ · 推导波动方程与 $c = 1/\sqrt{\mu_0\epsilon_0}$

**Claim.** From Maxwell's equations in vacuum ($\rho = 0$, $\mathbf{J} = 0$), $\mathbf{E}$ and $\mathbf{B}$ each satisfy the wave equation $\nabla^2\mathbf{F} = (1/c^2)\,\partial^2\mathbf{F}/\partial t^2$, with $c = 1/\sqrt{\mu_0\epsilon_0}$.

**命题。** 从真空中（$\rho = 0$，$\mathbf{J} = 0$）的麦克斯韦方程出发，$\mathbf{E}$ 和 $\mathbf{B}$ 各自满足波动方程 $\nabla^2\mathbf{F} = (1/c^2)\,\partial^2\mathbf{F}/\partial t^2$，其中 $c = 1/\sqrt{\mu_0\epsilon_0}$。

**Step 1 — Write the vacuum Maxwell equations.** Setting $\rho = 0$ and $\mathbf{J} = 0$:

**第 1 步 — 写出真空麦克斯韦方程。** 令 $\rho = 0$，$\mathbf{J} = 0$：

$$ \begin{aligned}
\text{(I)}\quad & \nabla\cdot\mathbf{E} = 0, \\
\text{(II)}\quad & \nabla\cdot\mathbf{B} = 0, \\
\text{(III)}\quad & \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}, \\
\text{(IV)}\quad & \nabla\times\mathbf{B} = \mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t}.
\end{aligned} $$

**Step 2 — Take the curl of Faraday's law.** Apply $\nabla\times$ to equation (III):

**第 2 步 — 对法拉第定律取旋度。** 对方程 (III) 施用 $\nabla\times$：

$$ \nabla\times(\nabla\times\mathbf{E}) = \nabla\times\!\left(-\frac{\partial\mathbf{B}}{\partial t}\right) = -\frac{\partial(\nabla\times\mathbf{B})}{\partial t}. $$

The right-hand side: substitute equation (IV), $\nabla\times\mathbf{B} = \mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$:

右侧：代入方程 (IV)，$\nabla\times\mathbf{B} = \mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$：

$$ -\frac{\partial(\nabla\times\mathbf{B})}{\partial t} = -\frac{\partial(\mu_0\epsilon_0\,\partial\mathbf{E}/\partial t)}{\partial t} = -\mu_0\epsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2}. $$

**Step 3 — Apply the vector identity for curl of curl.** For any vector field $\mathbf{F}$:

**第 3 步 — 应用旋度的旋度矢量恒等式。** 对任意矢量场 $\mathbf{F}$：

$$ \nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}. $$

Applying this to $\mathbf{E}$ and using $\nabla\cdot\mathbf{E} = 0$ (equation I):

将此应用于 $\mathbf{E}$，并利用 $\nabla\cdot\mathbf{E} = 0$（方程 I）：

$$ \nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = 0 - \nabla^2\mathbf{E} = -\nabla^2\mathbf{E}. $$

**Step 4 — Assemble the wave equation.** Equating the results of Steps 2 and 3:

**第 4 步 — 组装波动方程。** 将第 2、3 步的结果等同：

$$ -\nabla^2\mathbf{E} = -\mu_0\epsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2}, $$

$$ \boxed{\,\nabla^2\mathbf{E} - \mu_0\epsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2} = 0\,}, \qquad \text{i.e.}\quad \boxed{\,\nabla^2\mathbf{E} = \frac{1}{c^2}\frac{\partial^2\mathbf{E}}{\partial t^2}\,}, $$

where $c = 1/\sqrt{\mu_0\epsilon_0}$. Numerically, $\mu_0 = 4\pi\times 10^{-7}\ \mathrm{T\cdot m/A}$ and $\epsilon_0 = 8.854\times 10^{-12}\ \mathrm{C^2/(N\cdot m^2)}$, giving $c = 2.998\times 10^8\ \mathrm{m/s}$ — the measured speed of light.

其中 $c = 1/\sqrt{\mu_0\epsilon_0}$。数值上，$\mu_0 = 4\pi\times 10^{-7}\ \mathrm{T\cdot m/A}$，$\epsilon_0 = 8.854\times 10^{-12}\ \mathrm{C^2/(N\cdot m^2)}$，给出 $c = 2.998\times 10^8\ \mathrm{m/s}$——光速的测量值。

**Step 5 — Same equation for $\mathbf{B}$.** Taking $\nabla\times$ of Ampère–Maxwell and substituting Faraday's law:

**第 5 步 — $\mathbf{B}$ 满足相同方程。** 对安培–麦克斯韦方程取 $\nabla\times$，代入法拉第定律：

$$ \begin{aligned}
\nabla\times(\nabla\times\mathbf{B}) &= \nabla\times\!\left(\mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t}\right) = \mu_0\epsilon_0\,\frac{\partial(\nabla\times\mathbf{E})}{\partial t} = \mu_0\epsilon_0\,\frac{\partial(-\partial\mathbf{B}/\partial t)}{\partial t} = -\mu_0\epsilon_0\,\frac{\partial^2\mathbf{B}}{\partial t^2}. \\
\nabla(\nabla\cdot\mathbf{B}) - \nabla^2\mathbf{B} &= -\mu_0\epsilon_0\,\frac{\partial^2\mathbf{B}}{\partial t^2} \;\to\; \boxed{\,\nabla^2\mathbf{B} = \frac{1}{c^2}\frac{\partial^2\mathbf{B}}{\partial t^2}\,} \qquad \blacksquare
\end{aligned} $$

---

## B. Plane Wave Solutions and Transversality · 平面波解与横波性

**Claim.** The wave equation admits plane-wave solutions $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$, $\mathbf{B} = \mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$, with dispersion relation $\omega = c|\mathbf{k}|$, and the fields are transverse: $\mathbf{k}\cdot\mathbf{E}_0 = 0$, $\mathbf{k}\cdot\mathbf{B}_0 = 0$, with $\mathbf{B}_0 = (\hat{\mathbf{k}}\times\mathbf{E}_0)/c$.

**命题。** 波动方程允许平面波解 $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$，$\mathbf{B} = \mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$，色散关系为 $\omega = c|\mathbf{k}|$，且场是横向的：$\mathbf{k}\cdot\mathbf{E}_0 = 0$，$\mathbf{k}\cdot\mathbf{B}_0 = 0$，$\mathbf{B}_0 = (\hat{\mathbf{k}}\times\mathbf{E}_0)/c$。

**Step 1 — Dispersion relation.** Substitute $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$ into $\nabla^2\mathbf{E} = (1/c^2)\,\partial^2\mathbf{E}/\partial t^2$. The Laplacian gives $\nabla^2\mathbf{E} = -|\mathbf{k}|^2\mathbf{E}$, and $\partial^2\mathbf{E}/\partial t^2 = -\omega^2\mathbf{E}$:

**第 1 步 — 色散关系。** 将 $\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$ 代入 $\nabla^2\mathbf{E} = (1/c^2)\,\partial^2\mathbf{E}/\partial t^2$。拉普拉斯算子给出 $\nabla^2\mathbf{E} = -|\mathbf{k}|^2\mathbf{E}$，且 $\partial^2\mathbf{E}/\partial t^2 = -\omega^2\mathbf{E}$：

$$ -|\mathbf{k}|^2\mathbf{E} = \frac{1}{c^2}(-\omega^2)\mathbf{E} \;\to\; \boxed{\,\omega = c|\mathbf{k}|\,} \quad (\omega > 0) $$

**Step 2 — Transversality from $\nabla\cdot\mathbf{E} = 0$.** For the plane wave, $\nabla\cdot\mathbf{E} = i\mathbf{k}\cdot\mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)} = 0$, hence:

**第 2 步 — 由 $\nabla\cdot\mathbf{E} = 0$ 得横波性。** 对于平面波，$\nabla\cdot\mathbf{E} = i\mathbf{k}\cdot\mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)} = 0$，故：

$$ \boxed{\,\mathbf{k}\cdot\mathbf{E}_0 = 0\,} $$

$\mathbf{E}$ is perpendicular to the propagation direction $\mathbf{k}$. Similarly $\mathbf{k}\cdot\mathbf{B}_0 = 0$ from $\nabla\cdot\mathbf{B} = 0$.

$\mathbf{E}$ 垂直于传播方向 $\mathbf{k}$。类似地，由 $\nabla\cdot\mathbf{B} = 0$ 得 $\mathbf{k}\cdot\mathbf{B}_0 = 0$。

**Step 3 — Relation between $\mathbf{E}$ and $\mathbf{B}$.** From Faraday's law $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$:

**第 3 步 — $\mathbf{E}$ 与 $\mathbf{B}$ 的关系。** 由法拉第定律 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$：

$$ \begin{aligned}
i\mathbf{k}\times\mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)} &= -(-i\omega)\mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}, \\
\mathbf{k}\times\mathbf{E}_0 &= \omega\mathbf{B}_0, \\
\mathbf{B}_0 &= \frac{\mathbf{k}\times\mathbf{E}_0}{\omega} = \frac{\hat{\mathbf{k}}\times\mathbf{E}_0}{c} \quad (\text{using } \omega = c|\mathbf{k}|,\ \text{so } \mathbf{k}/\omega = \hat{\mathbf{k}}/c).
\end{aligned} $$

This confirms: $\mathbf{E}\perp\mathbf{B}\perp\mathbf{k}$ (mutually orthogonal), and $|\mathbf{B}_0| = |\mathbf{E}_0|/c$. $\blacksquare$

这确认了：$\mathbf{E}\perp\mathbf{B}\perp\mathbf{k}$（相互正交），且 $|\mathbf{B}_0| = |\mathbf{E}_0|/c$。$\blacksquare$

---

## C. The Poynting Theorem — Electromagnetic Energy Conservation · 坡印亭定理——电磁能量守恒

**Claim.** The energy density $u = \tfrac12(\epsilon_0 E^2 + B^2/\mu_0)$ and the Poynting vector $\mathbf{S} = (1/\mu_0)\,\mathbf{E}\times\mathbf{B}$ satisfy the energy continuity equation $\partial u/\partial t + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}$.

**命题。** 能量密度 $u = \tfrac12(\epsilon_0 E^2 + B^2/\mu_0)$ 与坡印亭矢量 $\mathbf{S} = (1/\mu_0)\,\mathbf{E}\times\mathbf{B}$ 满足能量连续性方程 $\partial u/\partial t + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}$。

**Step 1 — Start with $\mathbf{J}\cdot\mathbf{E}$ (power delivered to charges).** The power per unit volume delivered by the electromagnetic field to free charges is $\mathbf{J}\cdot\mathbf{E}$ (force per unit volume on charges is $\mathbf{J}\times\mathbf{B} + \rho\mathbf{E}$; the magnetic force does no work since it is perpendicular to the velocity, so only $\mathbf{E}$ contributes, giving $\mathbf{J}\cdot\mathbf{E}$).

**第 1 步 — 从 $\mathbf{J}\cdot\mathbf{E}$（传递给电荷的功率）出发。** 电磁场单位体积传递给自由电荷的功率为 $\mathbf{J}\cdot\mathbf{E}$（单位体积上的电磁力为 $\mathbf{J}\times\mathbf{B} + \rho\mathbf{E}$；磁力不做功，因为它垂直于速度，故只有 $\mathbf{E}$ 贡献，给出 $\mathbf{J}\cdot\mathbf{E}$）。

**Step 2 — Eliminate $\mathbf{J}$ using Ampère–Maxwell.** From $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$, solve for $\mathbf{J}$:

**第 2 步 — 用安培–麦克斯韦方程消去 $\mathbf{J}$。** 由 $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\,\partial\mathbf{E}/\partial t$ 解出 $\mathbf{J}$：

$$ \mu_0\mathbf{J} = \nabla\times\mathbf{B} - \mu_0\epsilon_0\,\frac{\partial\mathbf{E}}{\partial t}. $$

Dot with $\mathbf{E}$:

点乘 $\mathbf{E}$：

$$ \mu_0\,\mathbf{J}\cdot\mathbf{E} = \mathbf{E}\cdot(\nabla\times\mathbf{B}) - \mu_0\epsilon_0\,\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}. $$

**Step 3 — Use the product rule for divergence.** The identity $\nabla\cdot(\mathbf{E}\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{B})$ gives:

**第 3 步 — 利用散度乘法法则。** 恒等式 $\nabla\cdot(\mathbf{E}\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{B})$ 给出：

$$ \mathbf{E}\cdot(\nabla\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{E}) - \nabla\cdot(\mathbf{E}\times\mathbf{B}). $$

Substitute Faraday's law $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$:

代入法拉第定律 $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$：

$$ \mathbf{E}\cdot(\nabla\times\mathbf{B}) = \mathbf{B}\cdot\!\left(-\frac{\partial\mathbf{B}}{\partial t}\right) - \nabla\cdot(\mathbf{E}\times\mathbf{B}) = -\mathbf{B}\cdot\frac{\partial\mathbf{B}}{\partial t} - \nabla\cdot(\mathbf{E}\times\mathbf{B}). $$

**Step 4 — Assemble.** Substituting back into Step 2:

**第 4 步 — 综合。** 代回第 2 步：

$$ \mu_0\,\mathbf{J}\cdot\mathbf{E} = -\mathbf{B}\cdot\frac{\partial\mathbf{B}}{\partial t} - \nabla\cdot(\mathbf{E}\times\mathbf{B}) - \mu_0\epsilon_0\,\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}. $$

Note that $\mathbf{B}\cdot\partial\mathbf{B}/\partial t = \partial(B^2/2)/\partial t$ and $\mathbf{E}\cdot\partial\mathbf{E}/\partial t = \partial(E^2/2)/\partial t$. Dividing by $\mu_0$:

注意 $\mathbf{B}\cdot\partial\mathbf{B}/\partial t = \partial(B^2/2)/\partial t$，$\mathbf{E}\cdot\partial\mathbf{E}/\partial t = \partial(E^2/2)/\partial t$。除以 $\mu_0$：

$$ \mathbf{J}\cdot\mathbf{E} = -\frac{\partial(B^2/2\mu_0)}{\partial t} - \frac{1}{\mu_0}\nabla\cdot(\mathbf{E}\times\mathbf{B}) - \epsilon_0\,\frac{\partial(E^2/2)}{\partial t}. $$

Rearranging (and noting $\tfrac{\epsilon_0}{2}E^2 + \tfrac{B^2}{2\mu_0} = u$):

重排（注意 $\tfrac{\epsilon_0}{2}E^2 + \tfrac{B^2}{2\mu_0} = u$）：

$$ \boxed{\,\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}\,}, $$

where:

其中：

$$ \begin{aligned}
u &= \tfrac12\epsilon_0 E^2 + \frac{B^2}{2\mu_0} && \text{(electromagnetic energy density / 电磁能量密度)} \\
\mathbf{S} &= \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B} && \text{(Poynting vector / 坡印亭矢量)}
\end{aligned} $$

**Step 5 — Physical interpretation.** Integrating over volume $V$ with boundary $\partial V$:

**第 5 步 — 物理诠释。** 对体积 $V$ 积分，边界为 $\partial V$：

$$ \frac{d}{dt}\int_V u\,dV = -\oint_{\partial V}\mathbf{S}\cdot d\mathbf{A} - \int_V \mathbf{J}\cdot\mathbf{E}\,dV. $$

Rate of change of EM energy = (net inward Poynting flux) - (power dissipated to charges). This is the **electromagnetic energy conservation theorem**. $\blacksquare$

EM 能量的变化率 = （净向内坡印亭通量）-（传递给电荷的功率）。这是**电磁能量守恒定理**。$\blacksquare$

---

## D. The Larmor Radiation Formula $P = \mu_0 q^2 a^2/(6\pi c)$ · 拉莫尔辐射公式 $P = \mu_0 q^2 a^2/(6\pi c)$

**Claim.** A non-relativistic point charge $q$ with acceleration $a$ radiates power $P = \mu_0 q^2 a^2/(6\pi c)$.

**命题。** 具有加速度 $a$ 的非相对论性点电荷 $q$ 辐射功率 $P = \mu_0 q^2 a^2/(6\pi c)$。

**Step 1 — Radiation fields of an accelerating charge.** For a non-relativistic charge ($v\ll c$), the retarded electromagnetic fields have two components: a near-field (Coulomb) part falling off as $1/r^2$ and a radiation (far-field) part falling off as $1/r$. Only the radiation part contributes to energy transport to infinity. The radiation electric field is:

**第 1 步 — 加速电荷的辐射场。** 对于非相对论性电荷（$v\ll c$），推迟电磁场有两个成分：按 $1/r^2$ 衰减的近场（库仑）部分和按 $1/r$ 衰减的辐射（远场）部分。只有辐射部分对到无穷远处的能量传输有贡献。辐射电场为：

$$ \mathbf{E}_\text{rad}(\mathbf{r}, t) = \frac{q}{4\pi\epsilon_0 c^2}\cdot\frac{\hat{\mathbf{r}}\times(\hat{\mathbf{r}}\times\mathbf{a})}{r}, $$

where $\hat{\mathbf{r}}$ is the unit vector from the (retarded) position of the charge to the field point, and $\mathbf{a} = \mathbf{a}(t_\text{ret})$ is the acceleration at retarded time $t_\text{ret} = t - r/c$.

其中 $\hat{\mathbf{r}}$ 是从电荷（推迟）位置到场点的单位矢量，$\mathbf{a} = \mathbf{a}(t_\text{ret})$ 是推迟时刻 $t_\text{ret} = t - r/c$ 的加速度。

**Step 2 — Radiation magnetic field.** From the relation $\mathbf{B}_\text{rad} = (\hat{\mathbf{r}}\times\mathbf{E}_\text{rad})/c$:

**第 2 步 — 辐射磁场。** 由关系 $\mathbf{B}_\text{rad} = (\hat{\mathbf{r}}\times\mathbf{E}_\text{rad})/c$：

$$ \mathbf{B}_\text{rad} = \frac{\hat{\mathbf{r}}\times\mathbf{E}_\text{rad}}{c}, \qquad \text{so } |\mathbf{B}_\text{rad}| = |\mathbf{E}_\text{rad}|/c \quad (\mathbf{E}_\text{rad},\ \mathbf{B}_\text{rad},\ \text{and } \hat{\mathbf{r}}\ \text{are mutually orthogonal}). $$

Both fields have magnitude $|\mathbf{E}_\text{rad}| = (q a\sin\theta)/(4\pi\epsilon_0 c^2 r)$, where $\theta$ is the angle between $\mathbf{a}$ and $\hat{\mathbf{r}}$.

更直接地，两个场的大小均为 $|\mathbf{E}_\text{rad}| = (q a\sin\theta)/(4\pi\epsilon_0 c^2 r)$，其中 $\theta$ 是 $\mathbf{a}$ 与 $\hat{\mathbf{r}}$ 之间的夹角。

**Step 3 — Poynting vector and power per unit solid angle.** The time-averaged Poynting vector at distance $r$ is:

**第 3 步 — 坡印亭矢量与单位立体角功率。** 距离 $r$ 处的时间平均坡印亭矢量为：

$$ |\mathbf{S}| = \frac{|\mathbf{E}_\text{rad}|^2}{\mu_0 c} = \frac{q^2 a^2\sin^2\theta}{16\pi^2\epsilon_0 c^3 r^2}. $$

Power radiated per unit solid angle $d\Omega = \sin\theta\,d\theta\,d\phi$:

单位立体角辐射功率 $d\Omega = \sin\theta\,d\theta\,d\phi$：

$$ \frac{dP}{d\Omega} = r^2|\mathbf{S}| = \frac{q^2 a^2\sin^2\theta}{16\pi^2\epsilon_0 c^3}. $$

The $\sin^2\theta$ factor gives the characteristic **dipole radiation pattern**: zero along the acceleration axis, maximum perpendicular to it.

$\sin^2\theta$ 因子给出特征性的**偶极辐射方向图**：沿加速度轴方向为零，垂直方向最大。

**Step 4 — Integrate over all directions.** Total radiated power:

**第 4 步 — 对所有方向积分。** 总辐射功率：

$$ \begin{aligned}
P &= \int \frac{dP}{d\Omega}\,d\Omega = \int_0^{2\pi}d\phi\int_0^\pi d\theta\,\frac{q^2 a^2\sin^2\theta}{16\pi^2\epsilon_0 c^3}\sin\theta \\
&= \frac{q^2 a^2}{16\pi^2\epsilon_0 c^3}\cdot 2\pi\cdot\int_0^\pi \sin^3\theta\,d\theta.
\end{aligned} $$

Evaluate the angular integral: $\int_0^\pi \sin^3\theta\,d\theta = \int_0^\pi \sin\theta\,(1 - \cos^2\theta)\,d\theta = \left[-\cos\theta + \tfrac{\cos^3\theta}{3}\right]_0^\pi = (1 - \tfrac13) + (1 - \tfrac13) = \tfrac43$.

计算角积分：$\int_0^\pi \sin^3\theta\,d\theta = \int_0^\pi \sin\theta\,(1 - \cos^2\theta)\,d\theta = \left[-\cos\theta + \tfrac{\cos^3\theta}{3}\right]_0^\pi = (1 - \tfrac13) + (1 - \tfrac13) = \tfrac43$。

Therefore:

因此：

$$ P = \frac{q^2 a^2}{16\pi^2\epsilon_0 c^3}\cdot 2\pi\cdot\frac43 = \frac{q^2 a^2}{6\pi\epsilon_0 c^3}. $$

**Step 5 — Rewrite in terms of $\mu_0$.** Using $c = 1/\sqrt{\mu_0\epsilon_0}$, so $1/\epsilon_0 = \mu_0 c^2$:

**第 5 步 — 用 $\mu_0$ 改写。** 利用 $c = 1/\sqrt{\mu_0\epsilon_0}$，故 $1/\epsilon_0 = \mu_0 c^2$：

$$ P = \frac{q^2 a^2\mu_0 c^2}{6\pi c^3} = \boxed{\,\frac{\mu_0 q^2 a^2}{6\pi c}\,} \qquad \blacksquare $$

This is the **Larmor formula** in SI units. In Gaussian units it takes the form $P = q^2 a^2/(6\pi c^3)$. The formula immediately implies that a classically orbiting electron (centripetal acceleration $a\ne 0$) continuously radiates, losing energy on a timescale $\sim 10^{-11}\ \mathrm{s}$ — the radiation crisis that necessitates quantum mechanics.

这是 SI 单位制中的**拉莫尔公式**。在高斯单位制中，形式为 $P = q^2 a^2/(6\pi c^3)$。该公式立即意味着经典轨道电子（向心加速度 $a\ne 0$）持续辐射，在约 $10^{-11}\ \mathrm{s}$ 的时间尺度内损失能量——这一辐射危机使量子力学成为必要。

---

*The wave equation, Poynting theorem, and Larmor formula derived here provide the foundation for radiation theory (synchrotron radiation, antenna theory), the classical limit of QED, and the $\omega^4$ Rayleigh scattering that explains the blue sky.*

*此处推导的波动方程、坡印亭定理和拉莫尔公式为辐射理论（同步辐射、天线理论）、量子电动力学的经典极限以及解释蓝天的 $\omega^4$ 瑞利散射提供了基础。*

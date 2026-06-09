# Derivations — Module 1.9: Magnetostatics
# 推导 — 模块 1.9：静磁学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.9](./module-1.9-magnetostatics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.9](./module-1.9-magnetostatics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Biot–Savart Law · 毕奥–萨伐尔定律

**Claim.** The magnetic field produced by a steady current element $I\,d\boldsymbol{\ell}$ at a field point $\mathbf{r}$ is $d\mathbf{B} = (\mu_0/4\pi)\,I\,d\boldsymbol{\ell}\times\hat{\mathbf{r}}/r^2$, giving the full Biot–Savart law for an arbitrary current distribution.

**命题。** 稳恒电流元 $I\,d\boldsymbol{\ell}$ 在场点 $\mathbf{r}$ 处产生的磁场为 $d\mathbf{B} = (\mu_0/4\pi)\,I\,d\boldsymbol{\ell}\times\hat{\mathbf{r}}/r^2$，给出任意电流分布的完整毕奥–萨伐尔定律。

**Step 1 — Empirical basis and units.** Experiments on straight wires (Biot, Savart, 1820; Ampère, 1820–1826) established that the force per unit length between two parallel wires carrying currents $I_1$ and $I_2$ separated by distance $d$ is $F/L = \mu_0 I_1 I_2/(2\pi d)$, which defines $\mu_0$ (the permeability of free space). The magnetic constant $\mu_0 = 4\pi\times 10^{-7}\ \mathrm{T\cdot m/A}$ in SI. From this empirical basis one can show that the field from a current element $I\,d\boldsymbol{\ell}'$ at source point $\mathbf{r}'$ to field point $\mathbf{r}$ is:

**第 1 步 — 实验基础与单位。** 关于直导线的实验（毕奥、萨伐尔，1820 年；安培，1820–1826 年）确定，间距为 $d$ 的两平行导线携带电流 $I_1$ 和 $I_2$ 时，单位长度上的力为 $F/L = \mu_0 I_1 I_2/(2\pi d)$，由此定义 $\mu_0$（真空磁导率）。SI 单位中 $\mu_0 = 4\pi\times 10^{-7}\ \mathrm{T\cdot m/A}$。从这一实验基础可以证明，源点 $\mathbf{r}'$ 处的电流元 $I\,d\boldsymbol{\ell}'$ 在场点 $\mathbf{r}$ 处产生的磁场为：

$$ d\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\,\frac{I\,d\boldsymbol{\ell}'\times(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}. $$

**Step 2 — Full Biot–Savart law.** Integrating over the complete current loop $C$:

**第 2 步 — 完整毕奥–萨伐尔定律。** 对完整电流回路 $C$ 积分：

$$ \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\oint_C \frac{I\,d\boldsymbol{\ell}'\times(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}. $$

For a volume current density $\mathbf{J}(\mathbf{r}')$:

对于体电流密度 $\mathbf{J}(\mathbf{r}')$：

$$ \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{J}(\mathbf{r}')\times(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}\,dV'. $$

**Step 3 — Verification: infinite straight wire.** For a wire along the $z'$-axis carrying current $I$, let the field point be at distance $s$ from the wire (in the $xy$-plane at $z = 0$). Parameterise: $\mathbf{r}' = z'\hat{\mathbf{z}}$, $d\boldsymbol{\ell}' = dz'\,\hat{\mathbf{z}}$, $\mathbf{r} - \mathbf{r}' = s\hat{\mathbf{s}} - z'\hat{\mathbf{z}}$ where $\hat{\mathbf{s}}$ is the radial unit vector. Then:

**第 3 步 — 验证：无限长直导线。** 对于沿 $z'$ 轴流过电流 $I$ 的导线，设场点在距导线 $s$ 处（$xy$ 平面内 $z = 0$）。参数化：$\mathbf{r}' = z'\hat{\mathbf{z}}$，$d\boldsymbol{\ell}' = dz'\,\hat{\mathbf{z}}$，$\mathbf{r} - \mathbf{r}' = s\hat{\mathbf{s}} - z'\hat{\mathbf{z}}$，其中 $\hat{\mathbf{s}}$ 为径向单位矢量。则：

$$ d\boldsymbol{\ell}'\times(\mathbf{r} - \mathbf{r}') = dz'\,\hat{\mathbf{z}}\times(s\hat{\mathbf{s}} - z'\hat{\mathbf{z}}) = dz'\,(s\,\hat{\mathbf{z}}\times\hat{\mathbf{s}}) = dz'\,s\,\hat{\boldsymbol{\phi}}, $$

where $\hat{\boldsymbol{\phi}} = \hat{\mathbf{z}}\times\hat{\mathbf{s}}$ is the azimuthal direction. The magnitude $|\mathbf{r} - \mathbf{r}'|^3 = (s^2 + z'^2)^{3/2}$. Integrating from $-\infty$ to $+\infty$ using $\int_{-\infty}^{\infty} dz'/(s^2 + z'^2)^{3/2} = 2/s^2$:

其中 $\hat{\boldsymbol{\phi}} = \hat{\mathbf{z}}\times\hat{\mathbf{s}}$ 为方位角方向。$|\mathbf{r} - \mathbf{r}'|^3 = (s^2 + z'^2)^{3/2}$。从 $-\infty$ 到 $+\infty$ 积分，利用 $\int_{-\infty}^{\infty} dz'/(s^2 + z'^2)^{3/2} = 2/s^2$：

$$ \mathbf{B} = \frac{\mu_0 I}{4\pi}\,s\hat{\boldsymbol{\phi}}\cdot\frac{2}{s^2} = \boxed{\,\frac{\mu_0 I}{2\pi s}\,\hat{\boldsymbol{\phi}}\,} \qquad \blacksquare $$

---

## B. Ampère's Law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ from the Biot–Savart Law · 从毕奥–萨伐尔定律推导安培定律 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$

**Claim.** For a steady current density $\mathbf{J}$, the curl of the Biot–Savart field satisfies $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$.

**命题。** 对于稳恒电流密度 $\mathbf{J}$，毕奥–萨伐尔场的旋度满足 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$。

**Step 1 — Write $\mathbf{B}$ in terms of a Green's function.** The Biot–Savart field can be written as:

**第 1 步 — 用格林函数表示 $\mathbf{B}$。** 毕奥–萨伐尔场可写为：

$$ \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int \mathbf{J}(\mathbf{r}')\times\nabla\!\left(\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right) dV'\times(-1), $$

using $\nabla_r (1/|\mathbf{r} - \mathbf{r}'|) = -(\mathbf{r} - \mathbf{r}')/|\mathbf{r} - \mathbf{r}'|^3$. More conveniently, note that:

利用 $\nabla_r (1/|\mathbf{r} - \mathbf{r}'|) = -(\mathbf{r} - \mathbf{r}')/|\mathbf{r} - \mathbf{r}'|^3$。更方便地，注意到：

$$ \mathbf{B}(\mathbf{r}) = \nabla\times\mathbf{A}(\mathbf{r}), \qquad \text{where}\quad \mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|}\,dV'. $$

(This follows from the identity $\nabla\times(f\mathbf{J}) = f(\nabla\times\mathbf{J}) - \mathbf{J}\times\nabla f$ applied with $f = 1/|\mathbf{r} - \mathbf{r}'|$ and the fact that $\mathbf{J}$ depends only on $\mathbf{r}'$, not $\mathbf{r}$.)

（这由恒等式 $\nabla\times(f\mathbf{J}) = f(\nabla\times\mathbf{J}) - \mathbf{J}\times\nabla f$ 得到，取 $f = 1/|\mathbf{r} - \mathbf{r}'|$，并利用 $\mathbf{J}$ 仅依赖 $\mathbf{r}'$ 而非 $\mathbf{r}$ 的事实。）

**Step 2 — Compute $\nabla\times\mathbf{B}$ using the vector identity.** Apply $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$:

**第 2 步 — 用矢量恒等式计算 $\nabla\times\mathbf{B}$。** 应用 $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$：

$$ \nabla\times\mathbf{B} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}. $$

**Step 3 — Show $\nabla\cdot\mathbf{A} = 0$ in the Coulomb gauge.** For steady currents, $\nabla\cdot\mathbf{J} = 0$ (charge conservation: $\partial\rho/\partial t = 0$). Then:

**第 3 步 — 在库仑规范中证明 $\nabla\cdot\mathbf{A} = 0$。** 对于稳恒电流，$\nabla\cdot\mathbf{J} = 0$（电荷守恒：$\partial\rho/\partial t = 0$）。则：

$$ \nabla_r\cdot\mathbf{A} = \frac{\mu_0}{4\pi}\int \mathbf{J}(\mathbf{r}')\cdot\nabla_r\!\left(\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right) dV' = -\frac{\mu_0}{4\pi}\int \mathbf{J}(\mathbf{r}')\cdot\nabla_{r'}\!\left(\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right) dV'. $$

Integrating by parts (or using the identity $\nabla_{r'}\cdot(\mathbf{J}/|\mathbf{r}-\mathbf{r}'|) = (\nabla_{r'}\cdot\mathbf{J})/|\mathbf{r}-\mathbf{r}'| + \mathbf{J}\cdot\nabla_{r'}(1/|\mathbf{r}-\mathbf{r}'|)$), and the fact that $\mathbf{J}$ vanishes at infinity (localised current), the boundary term is zero and $\nabla_{r'}\cdot\mathbf{J} = 0$. Hence $\nabla\cdot\mathbf{A} = 0$.

分部积分（或利用恒等式 $\nabla_{r'}\cdot(\mathbf{J}/|\mathbf{r}-\mathbf{r}'|) = (\nabla_{r'}\cdot\mathbf{J})/|\mathbf{r}-\mathbf{r}'| + \mathbf{J}\cdot\nabla_{r'}(1/|\mathbf{r}-\mathbf{r}'|)$），以及 $\mathbf{J}$ 在无穷远处为零（局域电流），边界项为零且 $\nabla_{r'}\cdot\mathbf{J} = 0$。故 $\nabla\cdot\mathbf{A} = 0$。

**Step 4 — Evaluate $\nabla^2\mathbf{A}$ using the Green's function identity.** Using $\nabla^2(1/|\mathbf{r} - \mathbf{r}'|) = -4\pi\,\delta^3(\mathbf{r} - \mathbf{r}')$:

**第 4 步 — 用格林函数恒等式计算 $\nabla^2\mathbf{A}$。** 利用 $\nabla^2(1/|\mathbf{r} - \mathbf{r}'|) = -4\pi\,\delta^3(\mathbf{r} - \mathbf{r}')$：

$$ \nabla^2\mathbf{A} = \frac{\mu_0}{4\pi}\int \mathbf{J}(\mathbf{r}')\,\nabla^2\!\left(\frac{1}{|\mathbf{r} - \mathbf{r}'|}\right) dV' = \frac{\mu_0}{4\pi}\int \mathbf{J}(\mathbf{r}')\,(-4\pi\,\delta^3(\mathbf{r} - \mathbf{r}'))\,dV' = -\mu_0\mathbf{J}(\mathbf{r}). $$

**Step 5 — Assemble.** Since $\nabla(\nabla\cdot\mathbf{A}) = 0$:

**第 5 步 — 综合。** 由于 $\nabla(\nabla\cdot\mathbf{A}) = 0$：

$$ \boxed{\, \nabla\times\mathbf{B} = 0 - (-\mu_0\mathbf{J}) = \mu_0\mathbf{J} \,} \qquad \blacksquare $$

---

## C. $\nabla\cdot\mathbf{B} = 0$ and the Vector Potential $\mathbf{B} = \nabla\times\mathbf{A}$ · $\nabla\cdot\mathbf{B} = 0$ 与矢量势 $\mathbf{B} = \nabla\times\mathbf{A}$

**Claim.** The magnetic field has zero divergence everywhere, and can therefore be written as the curl of a vector potential $\mathbf{A}$.

**命题。** 磁场处处散度为零，因此可以写成矢量势 $\mathbf{A}$ 的旋度。

**Step 1 — Compute $\nabla\cdot\mathbf{B}$ from Biot–Savart.** From $\mathbf{B} = \nabla\times\mathbf{A}$ (established in Step 1 of Section B):

**第 1 步 — 从毕奥–萨伐尔定律计算 $\nabla\cdot\mathbf{B}$。** 由 $\mathbf{B} = \nabla\times\mathbf{A}$（B 节第 1 步已建立）：

$$ \nabla\cdot\mathbf{B} = \nabla\cdot(\nabla\times\mathbf{A}) = 0, $$

because the divergence of any curl is identically zero (a vector calculus identity: for any smooth vector field $\mathbf{A}$, $\nabla\cdot(\nabla\times\mathbf{A})\equiv 0$, proved by the symmetry of mixed partial derivatives — $\partial^2 A_j/\partial x_i\,\partial x_k - \partial^2 A_j/\partial x_k\,\partial x_i = 0$ by Schwarz's theorem).

因为任何旋度的散度恒为零（矢量分析恒等式：对任意光滑矢量场 $\mathbf{A}$，$\nabla\cdot(\nabla\times\mathbf{A})\equiv 0$，由混合偏导数的对称性证明——$\partial^2 A_j/\partial x_i\,\partial x_k - \partial^2 A_j/\partial x_k\,\partial x_i = 0$，由施瓦茨定理可得）。

**Step 2 — Physical meaning.** $\nabla\cdot\mathbf{B} = 0$ means there are no magnetic monopoles — magnetic field lines are always closed loops, never beginning or ending on a source. Integrating over any closed surface: $\oint_S \mathbf{B}\cdot d\mathbf{A} = 0$ — the magnetic flux through any closed surface is zero.

**第 2 步 — 物理意义。** $\nabla\cdot\mathbf{B} = 0$ 意味着没有磁单极——磁场线始终是闭合回路，从不在源处开始或结束。对任意闭合曲面积分：$\oint_S \mathbf{B}\cdot d\mathbf{A} = 0$——穿过任何闭合曲面的磁通量为零。

**Step 3 — Existence of $\mathbf{A}$.** By the converse of the Helmholtz theorem (on a simply-connected domain, a divergence-free field is a curl): since $\nabla\cdot\mathbf{B} = 0$, there exists $\mathbf{A}$ such that $\mathbf{B} = \nabla\times\mathbf{A}$. The vector potential $\mathbf{A}$ is not unique: $\mathbf{A}\to\mathbf{A} + \nabla\chi$ for any scalar $\chi$ leaves $\mathbf{B} = \nabla\times(\mathbf{A} + \nabla\chi) = \nabla\times\mathbf{A} + \nabla\times(\nabla\chi) = \nabla\times\mathbf{A}$ unchanged, since $\nabla\times\nabla\chi\equiv 0$ (the curl of a gradient vanishes identically). This is **gauge freedom**.

**第 3 步 — $\mathbf{A}$ 的存在性。** 由亥姆霍兹定理的逆定理（在单连通域上，无散场是某个场的旋度）：由于 $\nabla\cdot\mathbf{B} = 0$，存在 $\mathbf{A}$ 使得 $\mathbf{B} = \nabla\times\mathbf{A}$。矢量势 $\mathbf{A}$ 不唯一：对任意标量 $\chi$，$\mathbf{A}\to\mathbf{A} + \nabla\chi$ 不改变 $\mathbf{B} = \nabla\times(\mathbf{A} + \nabla\chi) = \nabla\times\mathbf{A} + \nabla\times(\nabla\chi) = \nabla\times\mathbf{A}$，因为 $\nabla\times\nabla\chi\equiv 0$（梯度的旋度恒为零）。这就是**规范自由度**。

**Step 4 — Coulomb gauge and the vector Poisson equation.** Choosing the gauge $\nabla\cdot\mathbf{A} = 0$ (Coulomb gauge), Ampère's law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ becomes (using $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$):

**第 4 步 — 库仑规范与矢量泊松方程。** 选择规范 $\nabla\cdot\mathbf{A} = 0$（库仑规范），安培定律 $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ 变为（利用 $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$）：

$$ \nabla(0) - \nabla^2\mathbf{A} = \mu_0\mathbf{J} \;\to\; \boxed{\,\nabla^2\mathbf{A} = -\mu_0\mathbf{J}\,}, $$

a vector Poisson equation with formal solution $\mathbf{A}(\mathbf{r}) = (\mu_0/4\pi)\int \mathbf{J}(\mathbf{r}')/|\mathbf{r} - \mathbf{r}'|\,dV'$, analogous to the electrostatic $\varphi(\mathbf{r}) = (1/4\pi\epsilon_0)\int \rho(\mathbf{r}')/|\mathbf{r} - \mathbf{r}'|\,dV'$. $\blacksquare$

矢量泊松方程，形式解为 $\mathbf{A}(\mathbf{r}) = (\mu_0/4\pi)\int \mathbf{J}(\mathbf{r}')/|\mathbf{r} - \mathbf{r}'|\,dV'$，类比静电学中的 $\varphi(\mathbf{r}) = (1/4\pi\epsilon_0)\int \rho(\mathbf{r}')/|\mathbf{r} - \mathbf{r}'|\,dV'$。$\blacksquare$

---

## D. Magnetic Dipole Field · 磁偶极子场

**Claim.** A magnetic dipole with moment $\mathbf{m} = m\,\hat{\mathbf{z}}$ (a small current loop of area $a$ carrying current $I$, with $m = Ia$) produces, at distances $r$ much larger than the loop size, the field:

**命题。** 磁矩为 $\mathbf{m} = m\,\hat{\mathbf{z}}$ 的磁偶极子（面积为 $a$ 载流 $I$ 的小电流环，$m = Ia$），在距离 $r$ 远大于环尺寸处，产生磁场：

$$ \mathbf{B}_\text{dip} = \frac{\mu_0}{4\pi r^3}\,(2m\cos\theta\,\hat{\mathbf{r}} + m\sin\theta\,\hat{\boldsymbol{\theta}}). $$

**Step 1 — Vector potential of a magnetic dipole.** In the Coulomb gauge, for a small current loop of area $a$ carrying current $I$ oriented in the $\hat{\mathbf{z}}$-direction, located at the origin, the vector potential can be derived from the Biot–Savart law. For a general current loop of moment $\mathbf{m} = Ia\,\hat{\mathbf{z}}$ in the limit of a small loop (magnetic dipole approximation):

**第 1 步 — 磁偶极子的矢量势。** 在库仑规范中，对于位于原点、沿 $\hat{\mathbf{z}}$ 方向定向的面积为 $a$ 载流 $I$ 的小电流环，矢量势可由毕奥–萨伐尔定律推导。对于矩为 $\mathbf{m} = Ia\,\hat{\mathbf{z}}$ 的一般电流环，在小环极限下（磁偶极近似）：

$$ \mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\,\frac{\mathbf{m}\times\mathbf{r}}{r^3} = \frac{\mu_0}{4\pi}\,\frac{m\sin\theta}{r^2}\,\hat{\boldsymbol{\phi}}. $$

This follows from expanding the Biot–Savart vector potential $\mathbf{A} = (\mu_0/4\pi)\oint I\,d\boldsymbol{\ell}'/|\mathbf{r} - \mathbf{r}'|$ in a multipole series and retaining the leading (dipole) term, analogous to the electric multipole expansion of Section D in Module 1.8.

这由展开毕奥–萨伐尔矢量势 $\mathbf{A} = (\mu_0/4\pi)\oint I\,d\boldsymbol{\ell}'/|\mathbf{r} - \mathbf{r}'|$ 的多极级数，保留主要（偶极）项得到，类比于模块 1.8 D 节的电多极展开。

**Step 2 — Compute $\mathbf{B} = \nabla\times\mathbf{A}$.** In spherical coordinates with only the $\hat{\boldsymbol{\phi}}$ component of $\mathbf{A}$ ($A_\phi = \mu_0 m\sin\theta/(4\pi r^2)$):

**第 2 步 — 计算 $\mathbf{B} = \nabla\times\mathbf{A}$。** 在球坐标中，$\mathbf{A}$ 只有 $\hat{\boldsymbol{\phi}}$ 分量（$A_\phi = \mu_0 m\sin\theta/(4\pi r^2)$）：

$$ \begin{aligned}
B_r &= \frac{1}{r\sin\theta}\frac{\partial(\sin\theta\cdot A_\phi)}{\partial\theta} = \frac{1}{r\sin\theta}\frac{\partial(\mu_0 m\sin^2\theta/(4\pi r^2))}{\partial\theta} \\
&= \frac{1}{r\sin\theta}\cdot\frac{\mu_0 m\cdot 2\sin\theta\cos\theta}{4\pi r^2} = \frac{\mu_0 m\cdot 2\cos\theta}{4\pi r^3}, \\[4pt]
B_\theta &= -\frac{1}{r}\frac{\partial(r A_\phi)}{\partial r} = -\frac{1}{r}\frac{\partial(\mu_0 m\sin\theta/(4\pi r))}{\partial r} \\
&= -\frac{1}{r}\left(-\frac{\mu_0 m\sin\theta}{4\pi r^2}\right) = \frac{\mu_0 m\sin\theta}{4\pi r^3}, \\[4pt]
B_\phi &= 0 \quad\text{(by azimuthal symmetry).}
\end{aligned} $$

**Step 3 — Final result.** Combining:

**第 3 步 — 最终结果。** 合并得：

$$ \boxed{\, \mathbf{B}_\text{dip} = \frac{\mu_0}{4\pi r^3}\,(2m\cos\theta\,\hat{\mathbf{r}} + m\sin\theta\,\hat{\boldsymbol{\theta}}) \,} $$

This is exactly analogous to the electric dipole field $\mathbf{E}_\text{dip} = (1/4\pi\epsilon_0 r^3)(2p\cos\theta\,\hat{\mathbf{r}} + p\sin\theta\,\hat{\boldsymbol{\theta}})$, with the replacement $p/\epsilon_0\leftrightarrow\mu_0 m$. $\blacksquare$

这与电偶极子场 $\mathbf{E}_\text{dip} = (1/4\pi\epsilon_0 r^3)(2p\cos\theta\,\hat{\mathbf{r}} + p\sin\theta\,\hat{\boldsymbol{\theta}})$ 完全类似，替换 $p/\epsilon_0\leftrightarrow\mu_0 m$。$\blacksquare$

**Step 4 — Compact tensor form.** The dipole field can be written in Cartesian form as:

**第 4 步 — 紧凑张量形式。** 偶极子场可用笛卡尔形式写为：

$$ \mathbf{B}_\text{dip}(\mathbf{r}) = \frac{\mu_0}{4\pi r^3}\big[3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{m}\big], $$

valid outside the source ($r\ne 0$). Inside ($r = 0$) there is an additional term $(2\mu_0/3)\,\mathbf{m}\,\delta^3(\mathbf{r})$ that ensures $\nabla\cdot\mathbf{B} = 0$ and $\nabla\times\mathbf{B} = 0$ are maintained in the distributional sense.

在源外（$r\ne 0$）有效。在内部（$r = 0$）还有附加项 $(2\mu_0/3)\,\mathbf{m}\,\delta^3(\mathbf{r})$，确保在分布意义下 $\nabla\cdot\mathbf{B} = 0$ 和 $\nabla\times\mathbf{B} = 0$ 保持成立。

---

*The vector potential, gauge invariance, and the dipole structure established here extend directly to covariant electromagnetism (Module 1.15), the Aharonov–Bohm effect (Phase 3), and gauge field theory (Phase 8).*

*此处建立的矢量势、规范不变性和偶极结构直接延伸到协变电磁学（模块 1.15）、阿哈罗诺夫–玻姆效应（第 3 阶段）和规范场论（第 8 阶段）。*

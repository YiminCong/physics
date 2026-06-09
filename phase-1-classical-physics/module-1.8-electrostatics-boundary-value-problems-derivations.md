# Derivations — Module 1.8: Electrostatics & Boundary-Value Problems
# 推导 — 模块 1.8：静电学与边值问题

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.8](./module-1.8-electrostatics-boundary-value-problems.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.8](./module-1.8-electrostatics-boundary-value-problems.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Gauss's Law from Coulomb's Law via Solid Angle and the Divergence Theorem · 从库仑定律经立体角与散度定理推导高斯定律

**Claim.** For any charge distribution $\rho(\mathbf{r})$, $\oint_S \mathbf{E}\cdot d\mathbf{A} = Q_\text{enc}/\epsilon_0$ and $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$.

**命题。** 对任意电荷分布 $\rho(\mathbf{r})$，$\oint_S \mathbf{E}\cdot d\mathbf{A} = Q_\text{enc}/\epsilon_0$ 且 $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$。

**Step 1 — Coulomb field of a point charge.** A point charge $q$ at the origin produces an electric field at position $\mathbf{r}$:

**第 1 步 — 点电荷的库仑场。** 位于原点的点电荷 $q$ 在位置 $\mathbf{r}$ 处产生电场：

$$ \mathbf{E}(\mathbf{r}) = \frac{q}{4\pi\epsilon_0}\,\frac{\hat{\mathbf{r}}}{r^2} = \frac{q}{4\pi\epsilon_0}\,\frac{\mathbf{r}}{r^3}. $$

This follows from Coulomb's force law $\mathbf{F} = qQ\,\hat{\mathbf{r}}/(4\pi\epsilon_0 r^2)$ by defining $\mathbf{E} = \mathbf{F}/Q$ for a test charge $Q\to 0$.

这由库仑力定律 $\mathbf{F} = qQ\,\hat{\mathbf{r}}/(4\pi\epsilon_0 r^2)$ 出发，对试验电荷 $Q\to 0$ 取极限定义 $\mathbf{E} = \mathbf{F}/Q$ 而得。

**Step 2 — Flux through an arbitrary closed surface enclosing $q$.** Consider the flux integral $\oint_S \mathbf{E}\cdot d\mathbf{A}$ over any smooth closed surface $S$ enclosing the charge. The area element $d\mathbf{A} = \hat{\mathbf{n}}\,dA$ has outward normal $\hat{\mathbf{n}}$. The integrand is:

**第 2 步 — 包围 $q$ 的任意闭合曲面上的通量。** 考虑包围电荷的任意光滑闭合曲面 $S$ 上的通量积分 $\oint_S \mathbf{E}\cdot d\mathbf{A}$。面积元 $d\mathbf{A} = \hat{\mathbf{n}}\,dA$，$\hat{\mathbf{n}}$ 为外法线方向。被积量为：

$$ \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\epsilon_0}\,\frac{\hat{\mathbf{r}}\cdot\hat{\mathbf{n}}}{r^2}\,dA. $$

The solid angle subtended at the charge by the area element $dA$ is $d\Omega = (\hat{\mathbf{r}}\cdot\hat{\mathbf{n}})\,dA/r^2$ (the projection of $dA$ perpendicular to the radial direction, divided by $r^2$). When the surface element faces the charge ($\hat{\mathbf{r}}\cdot\hat{\mathbf{n}} > 0$) the solid angle is positive; when it faces away ($\hat{\mathbf{r}}\cdot\hat{\mathbf{n}} < 0$), it is negative. Every line from $q$ pierces a closed surface an odd number of times (once for a convex surface, possibly more for a non-convex one, but algebraically the sum is $+1$ for a charge inside).

在电荷处，面积元 $dA$ 所张的立体角为 $d\Omega = (\hat{\mathbf{r}}\cdot\hat{\mathbf{n}})\,dA/r^2$（$dA$ 垂直于径向方向的投影除以 $r^2$）。当曲面元朝向电荷时（$\hat{\mathbf{r}}\cdot\hat{\mathbf{n}} > 0$），立体角为正；背向时（$\hat{\mathbf{r}}\cdot\hat{\mathbf{n}} < 0$）为负。从 $q$ 出发的每条直线穿过闭合曲面奇数次，代数求和结果对于内部电荷为 $+1$。

**Step 3 — Integration over the full solid angle.** Because a closed surface subtends the full $4\pi$ steradians of solid angle at any interior point:

**第 3 步 — 对全立体角积分。** 因为闭合曲面在任意内部点所张的全部立体角为 $4\pi$ 球面度：

$$ \oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{q}{4\pi\epsilon_0}\oint_S d\Omega = \frac{q}{4\pi\epsilon_0}\cdot 4\pi = \frac{q}{\epsilon_0}. $$

If the charge is outside $S$, every ray from $q$ enters and exits $S$ in pairs, so the net solid-angle integral is zero: $\oint_S \mathbf{E}\cdot d\mathbf{A} = 0$ for $q$ outside.

若电荷在 $S$ 外，则从 $q$ 出发的每条射线成对地穿入穿出 $S$，净立体角积分为零：$q$ 在外时 $\oint_S \mathbf{E}\cdot d\mathbf{A} = 0$。

**Step 4 — Superposition to the general case.** For a continuous charge distribution $\rho(\mathbf{r}')$, the total field is $\mathbf{E} = \int \mathbf{E}_{dq}$ over all charge elements. The flux integral is linear, so:

**第 4 步 — 叠加到一般情形。** 对于连续电荷分布 $\rho(\mathbf{r}')$，总场为 $\mathbf{E} = \int \mathbf{E}_{dq}$ 对所有电荷元的积分。通量积分是线性的，故：

$$ \oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{1}{\epsilon_0}\int_V \rho(\mathbf{r}')\,dV' = \frac{Q_\text{enc}}{\epsilon_0}. $$

This is **Gauss's law in integral form**.

这就是**积分形式的高斯定律**。

**Step 5 — Differential form via the Divergence Theorem.** The divergence theorem states $\oint_S \mathbf{E}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{E})\,dV$. Since the surface $S$ and enclosed volume $V$ are arbitrary:

**第 5 步 — 经散度定理得微分形式。** 散度定理表明 $\oint_S \mathbf{E}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{E})\,dV$。由于曲面 $S$ 和所围体积 $V$ 是任意的：

$$ \int_V (\nabla\cdot\mathbf{E})\,dV = \frac{1}{\epsilon_0}\int_V \rho\,dV, $$

and since this holds for every volume $V$, the integrands must be equal pointwise:

由于这对每个体积 $V$ 都成立，被积函数在每点处必须相等：

$$ \boxed{\, \nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0} \,} \qquad \blacksquare $$

---

## B. Poisson's Equation $\nabla^2\varphi = -\rho/\epsilon_0$ and Laplace's Equation · 泊松方程 $\nabla^2\varphi = -\rho/\epsilon_0$ 及拉普拉斯方程

**Claim.** In electrostatics the curl-free condition and Gauss's law together imply $\nabla^2\varphi = -\rho/\epsilon_0$, which reduces to $\nabla^2\varphi = 0$ in charge-free regions.

**命题。** 在静电学中，无旋条件与高斯定律共同意味着 $\nabla^2\varphi = -\rho/\epsilon_0$，在无电荷区域化为 $\nabla^2\varphi = 0$。

**Step 1 — Establish $\nabla\times\mathbf{E} = 0$.** For a static point charge $q$ at the origin, $\mathbf{E} = q\,\hat{\mathbf{r}}/(4\pi\epsilon_0 r^2)$. Computing the curl in spherical coordinates, or noting that $\mathbf{E} = -\nabla(q/(4\pi\epsilon_0 r))$, we have $\nabla\times\mathbf{E} = \nabla\times(-\nabla\varphi) = 0$ identically, since the curl of a gradient is always zero. By superposition this holds for any static charge distribution.

**第 1 步 — 建立 $\nabla\times\mathbf{E} = 0$。** 对于位于原点的静电点电荷 $q$，$\mathbf{E} = q\,\hat{\mathbf{r}}/(4\pi\epsilon_0 r^2)$。在球坐标中计算旋度，或注意到 $\mathbf{E} = -\nabla(q/(4\pi\epsilon_0 r))$，我们有 $\nabla\times\mathbf{E} = \nabla\times(-\nabla\varphi) = 0$，因为梯度的旋度恒为零。由叠加原理，这对任意静电荷分布均成立。

**Step 2 — Introduce the scalar potential.** Because $\nabla\times\mathbf{E} = 0$, by the Helmholtz theorem (or directly from vector calculus: a curl-free field on a simply-connected domain is a gradient), there exists a scalar field $\varphi(\mathbf{r})$ such that:

**第 2 步 — 引入标量电势。** 因为 $\nabla\times\mathbf{E} = 0$，由亥姆霍兹定理（或直接由向量分析：单连通域上的无旋场是梯度场），存在标量场 $\varphi(\mathbf{r})$，使得：

$$ \mathbf{E} = -\nabla\varphi. $$

The sign is chosen by convention so that the field points from high to low potential (analogous to a force pointing down a slope).

符号按惯例选取，使得场从高电势指向低电势（类比于力沿斜面向下）。

**Step 3 — Substitute into Gauss's law.** Insert $\mathbf{E} = -\nabla\varphi$ into $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$:

**第 3 步 — 代入高斯定律。** 将 $\mathbf{E} = -\nabla\varphi$ 代入 $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$：

$$ \begin{aligned}
\nabla\cdot(-\nabla\varphi) &= \frac{\rho}{\epsilon_0} \\
-\nabla^2\varphi &= \frac{\rho}{\epsilon_0} \\
\boxed{\,\nabla^2\varphi = -\frac{\rho}{\epsilon_0}\,} &\qquad \text{(Poisson's equation / 泊松方程)}
\end{aligned} $$

**Step 4 — Laplace's equation in charge-free regions.** Where $\rho = 0$:

**第 4 步 — 无电荷区域的拉普拉斯方程。** 在 $\rho = 0$ 处：

$$ \boxed{\,\nabla^2\varphi = 0\,} \qquad \text{(Laplace's equation / 拉普拉斯方程)} $$

Solutions are called **harmonic functions**; they satisfy the mean-value property (the value at any interior point equals the average over any surrounding sphere), which immediately implies the **maximum principle**: $\varphi$ can have no local maxima or minima in a charge-free region.

解被称为**调和函数**；它们满足平均值性质（任意内部点处的值等于任意外围球面的平均值），这立即意味着**最大值原理**：$\varphi$ 在无电荷区域内不能有局部极大或极小值。$\blacksquare$

---

## C. Separation of Variables — Grounded Conducting Sphere in a Uniform External Field · 分离变量法——均匀外场中的接地导体球

**Claim.** A grounded conducting sphere of radius $R$ placed in a uniform field $E_0\,\hat{\mathbf{z}}$ has the exterior potential $\varphi_\text{out}(r, \theta) = -E_0 r\cos\theta + E_0 R^3 \cos\theta / r^2$, and the induced surface charge density is $\sigma = 3\epsilon_0 E_0 \cos\theta$.

**命题。** 半径为 $R$ 的接地导体球置于均匀场 $E_0\,\hat{\mathbf{z}}$ 中，外部电势为 $\varphi_\text{out}(r, \theta) = -E_0 r\cos\theta + E_0 R^3 \cos\theta / r^2$，感应面电荷密度为 $\sigma = 3\epsilon_0 E_0 \cos\theta$。

**Step 1 — Set up Laplace's equation in spherical coordinates.** In the exterior region $r > R$, with no free charge, $\varphi$ satisfies $\nabla^2\varphi = 0$. In spherical coordinates with azimuthal symmetry (no $\phi$-dependence):

**第 1 步 — 在球坐标中建立拉普拉斯方程。** 在无自由电荷的外部区域 $r > R$，$\varphi$ 满足 $\nabla^2\varphi = 0$。在具有方位角对称性（无 $\phi$ 依赖）的球坐标中：

$$ \frac{1}{r^2}\frac{d}{dr}\!\left(r^2 \frac{d\varphi}{dr}\right) + \frac{1}{r^2\sin\theta}\frac{d}{d\theta}\!\left(\sin\theta\,\frac{d\varphi}{d\theta}\right) = 0. $$

**Step 2 — Separate variables.** Write $\varphi(r, \theta) = R(r)\,\Theta(\theta)$. Substituting and dividing by $R(r)\Theta(\theta)/r^2$:

**第 2 步 — 分离变量。** 令 $\varphi(r, \theta) = R(r)\,\Theta(\theta)$。代入并除以 $R(r)\Theta(\theta)/r^2$：

$$ \frac{1}{R}\frac{d}{dr}\!\left(r^2 \frac{dR}{dr}\right) = -\frac{1}{\Theta\sin\theta}\frac{d}{d\theta}\!\left(\sin\theta\,\frac{d\Theta}{d\theta}\right) = \ell(\ell+1), $$

where $\ell(\ell+1)$ is the separation constant (chosen in this form to give polynomial solutions in $\cos\theta$). The two separated ODEs are:

其中 $\ell(\ell+1)$ 为分离常数（选此形式使 $\cos\theta$ 的多项式解存在）。两个分离的常微分方程为：

$$ \begin{aligned}
\text{Radial:}\quad & \frac{d}{dr}\!\left(r^2 \frac{dR}{dr}\right) - \ell(\ell+1) R = 0 \;\to\; R(r) = A_\ell\, r^\ell + B_\ell\, r^{-(\ell+1)}, \\
\text{Angular:}\quad & \frac{1}{\sin\theta}\frac{d}{d\theta}\!\left(\sin\theta\,\frac{d\Theta}{d\theta}\right) + \ell(\ell+1)\,\Theta = 0 \;\to\; \Theta = P_\ell(\cos\theta),
\end{aligned} $$

where $P_\ell$ are the **Legendre polynomials**. For $\ell = 0$: $P_0 = 1$; $\ell = 1$: $P_1 = \cos\theta$; $\ell = 2$: $P_2 = (3\cos^2\theta - 1)/2$, etc.

其中 $P_\ell$ 为**勒让德多项式**。$\ell = 0$：$P_0 = 1$；$\ell = 1$：$P_1 = \cos\theta$；$\ell = 2$：$P_2 = (3\cos^2\theta - 1)/2$，等等。

**Step 3 — Apply boundary condition at $r\to\infty$.** Far from the sphere the field must reduce to the uniform external field $E_0\,\hat{\mathbf{z}}$, whose potential is $\varphi\to -E_0 r\cos\theta$ as $r\to\infty$. Therefore the only term that grows as $r\to\infty$ must match $-E_0 r\cos\theta$, which is the $\ell = 1$, $r^1$ term. All terms with $A_\ell$ for $\ell\ne 1$ must vanish, and $A_1 = -E_0$. The general exterior solution is:

**第 3 步 — 应用 $r\to\infty$ 处的边界条件。** 远离球体，场必须还原为均匀外场 $E_0\,\hat{\mathbf{z}}$，其电势为 $\varphi\to -E_0 r\cos\theta$（$r\to\infty$）。因此，随 $r\to\infty$ 增长的唯一项必须匹配 $-E_0 r\cos\theta$，即 $\ell = 1$，$r^1$ 项。所有 $\ell\ne 1$ 的 $A_\ell$ 项必须为零，且 $A_1 = -E_0$。一般外部解为：

$$ \varphi_\text{out} = -E_0 r\cos\theta + \sum_\ell B_\ell\, r^{-(\ell+1)} P_\ell(\cos\theta). $$

**Step 4 — Apply the grounded-sphere boundary condition $\varphi(R, \theta) = 0$.** Setting $r = R$:

**第 4 步 — 应用接地球面边界条件 $\varphi(R, \theta) = 0$。** 令 $r = R$：

$$ -E_0 R\cos\theta + \sum_\ell B_\ell\, R^{-(\ell+1)} P_\ell(\cos\theta) = 0. $$

By the orthogonality of Legendre polynomials, each coefficient must separately vanish. The only non-zero driving term is the $\ell = 1$ term ($-E_0 R\cos\theta = -E_0 R\, P_1$), so only $B_1$ is non-zero:

由勒让德多项式的正交性，每个系数必须分别为零。唯一非零的驱动项是 $\ell = 1$ 项（$-E_0 R\cos\theta = -E_0 R\, P_1$），所以只有 $B_1$ 非零：

$$ B_1\, R^{-2} = E_0 R \;\to\; B_1 = E_0 R^3. $$

All other $B_\ell = 0$. Therefore:

所有其他 $B_\ell = 0$。因此：

$$ \boxed{\, \varphi_\text{out}(r, \theta) = -E_0 r\cos\theta + \frac{E_0 R^3 \cos\theta}{r^2} \,} $$

**Step 5 — Physical interpretation.** The first term is the applied potential; the second is a dipole potential with effective dipole moment $\mathbf{p} = 4\pi\epsilon_0 R^3 E_0\,\hat{\mathbf{z}}$, arising from the induced surface charge. This is exactly the form of an electric dipole field (see Section D).

**第 5 步 — 物理诠释。** 第一项是外加电势；第二项是有效偶极矩 $\mathbf{p} = 4\pi\epsilon_0 R^3 E_0\,\hat{\mathbf{z}}$ 的偶极子电势，由感应面电荷产生。这正是电偶极子场的形式（见 D 节）。

**Step 6 — Surface charge density.** The radial component of $\mathbf{E}$ just outside a conductor equals $\sigma/\epsilon_0$. Computing $E_r = -\partial\varphi/\partial r$ at $r = R$:

**第 6 步 — 面电荷密度。** 导体外侧紧邻处 $\mathbf{E}$ 的径向分量等于 $\sigma/\epsilon_0$。在 $r = R$ 处计算 $E_r = -\partial\varphi/\partial r$：

$$ E_r\big|_{r=R} = E_0 \cos\theta + \frac{2 E_0 R^3 \cos\theta}{R^3} = 3 E_0 \cos\theta. $$

Hence $\boxed{\,\sigma = \epsilon_0 E_r\big|_{r=R} = 3\epsilon_0 E_0 \cos\theta\,}$ $\blacksquare$

故 $\boxed{\,\sigma = \epsilon_0 E_r\big|_{r=R} = 3\epsilon_0 E_0 \cos\theta\,}$ $\blacksquare$

**Step 7 — Uniqueness theorem (why this is the unique solution).** The uniqueness theorem for Laplace's equation states: given boundary conditions on $\varphi$ (Dirichlet) or $\partial\varphi/\partial n$ (Neumann) on a closed surface, the solution inside is unique. Proof sketch: suppose $\varphi_1$ and $\varphi_2$ are two solutions; let $u = \varphi_1 - \varphi_2$, which satisfies $\nabla^2 u = 0$ with $u = 0$ on the boundary (Dirichlet). Then $\int_V |\nabla u|^2\, dV = \oint_S u\,(\partial u/\partial n)\, dA = 0$ (by Green's first identity, with $u = 0$ on $S$). Since $|\nabla u|^2 \ge 0$, we must have $\nabla u = 0$ everywhere, so $u = \text{constant} = 0$. Hence $\varphi_1 = \varphi_2$.

**第 7 步 — 唯一性定理（为何此解是唯一的）。** 拉普拉斯方程的唯一性定理指出：给定闭合曲面上 $\varphi$ 的边界条件（狄利克雷）或 $\partial\varphi/\partial n$（诺依曼），内部解是唯一的。证明概要：设 $\varphi_1$ 和 $\varphi_2$ 是两个解；令 $u = \varphi_1 - \varphi_2$，满足 $\nabla^2 u = 0$，边界上 $u = 0$（狄利克雷）。则 $\int_V |\nabla u|^2\, dV = \oint_S u\,(\partial u/\partial n)\, dA = 0$（由格林第一恒等式，$S$ 上 $u = 0$）。由于 $|\nabla u|^2 \ge 0$，必有 $\nabla u = 0$ 处处成立，故 $u = \text{常数} = 0$。因此 $\varphi_1 = \varphi_2$。

---

## D. Multipole Expansion — Monopole, Dipole, and Quadrupole Terms · 多极展开——单极、偶极与四极项

**Claim.** At large distances from a bounded charge distribution $\rho(\mathbf{r}')$, the potential can be expanded in inverse powers of $r$, with the leading terms being the monopole ($1/r$), dipole ($1/r^2$), and quadrupole ($1/r^3$).

**命题。** 距有界电荷分布 $\rho(\mathbf{r}')$ 较远处，电势可展开为 $r$ 的负幂次，主要项依次为单极（$1/r$）、偶极（$1/r^2$）和四极（$1/r^3$）。

**Step 1 — Exact expression.** The potential at field point $\mathbf{r}$ due to a charge distribution $\rho(\mathbf{r}')$ confined near the origin is:

**第 1 步 — 精确表达式。** 场点 $\mathbf{r}$ 处由集中在原点附近的电荷分布 $\rho(\mathbf{r}')$ 产生的电势为：

$$ \varphi(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int \frac{\rho(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|}\,dV'. $$

**Step 2 — Expand $1/|\mathbf{r} - \mathbf{r}'|$ for $r' \ll r$.** Using the generating function for Legendre polynomials:

**第 2 步 — 展开 $r' \ll r$ 时的 $1/|\mathbf{r} - \mathbf{r}'|$。** 利用勒让德多项式的母函数：

$$ \frac{1}{|\mathbf{r} - \mathbf{r}'|} = \frac{1}{r}\sum_{\ell=0}^{\infty}\left(\frac{r'}{r}\right)^\ell P_\ell(\cos\alpha), $$

where $\alpha$ is the angle between $\mathbf{r}$ and $\mathbf{r}'$. This is exact when $r > r'$ (all charges inside a sphere of radius $r$).

其中 $\alpha$ 是 $\mathbf{r}$ 与 $\mathbf{r}'$ 之间的夹角。当 $r > r'$ 时（所有电荷在半径为 $r$ 的球内），此式精确成立。

**Step 3 — Identify each term.** Substituting:

**第 3 步 — 识别每一项。** 代入得：

$$ \varphi(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\sum_{\ell=0}^{\infty}\frac{1}{r^{\ell+1}}\int r'^\ell\, P_\ell(\cos\alpha)\,\rho(\mathbf{r}')\,dV'. $$

$$ \begin{aligned}
\ell = 0\ \text{(monopole):}\quad & \varphi_\text{mono} = \frac{1}{4\pi\epsilon_0}\frac{Q}{r}, && Q = \int \rho\,dV'. \\
\ell = 1\ \text{(dipole):}\quad & \varphi_\text{dip} = \frac{1}{4\pi\epsilon_0}\frac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^2}, && \mathbf{p} = \int \mathbf{r}'\,\rho(\mathbf{r}')\,dV'. \\
\ell = 2\ \text{(quadrupole):}\quad & \varphi_\text{quad} = \frac{1}{4\pi\epsilon_0}\frac{1}{r^3}\sum_{ij}\frac{Q_{ij}\,\hat{r}_i\,\hat{r}_j}{2}, &&
\end{aligned} $$

where $Q_{ij} = \int (3 r'_i r'_j - r'^2 \delta_{ij})\,\rho(\mathbf{r}')\,dV'$ is the quadrupole tensor.

其中 $Q_{ij} = \int (3 r'_i r'_j - r'^2 \delta_{ij})\,\rho(\mathbf{r}')\,dV'$ 是四极矩张量。

**Step 4 — Physical content.** If $Q\ne 0$, the monopole dominates at large $r$ (like a point charge). If $Q = 0$ but $\mathbf{p}\ne 0$ (e.g., equal and opposite charges separated by a distance), the dipole term dominates. Neutral atoms have $Q = 0$ and often $\mathbf{p} = 0$ (nonpolar), so their leading interaction at large distances is through the quadrupole or induced-dipole terms. The electric dipole field $\mathbf{E}_\text{dip} = (1/4\pi\epsilon_0 r^3)(3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p})$ is the far-field leading term for any neutral current-free source with a nonzero dipole moment. $\blacksquare$

**第 4 步 — 物理内涵。** 若 $Q\ne 0$，单极项在大 $r$ 处主导（如点电荷）。若 $Q = 0$ 但 $\mathbf{p}\ne 0$（例如等量异号电荷分开一段距离），偶极项主导。中性原子有 $Q = 0$，且通常 $\mathbf{p} = 0$（非极性），其在大距离处的主导相互作用通过四极矩或感应偶极矩项进行。电偶极子场 $\mathbf{E}_\text{dip} = (1/4\pi\epsilon_0 r^3)(3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p})$ 是任何偶极矩非零的中性无流源的远场主导项。$\blacksquare$

---

*All four Maxwell equations, boundary-value methods, and the multipole hierarchy developed here feed directly into Modules 1.9–1.11, the hydrogen atom (Module 3.4), and multipole radiation theory.*

*此处发展的所有四个麦克斯韦方程、边值方法和多极层次，直接支撑模块 1.9–1.11、氢原子（模块 3.4）和多极辐射理论。*

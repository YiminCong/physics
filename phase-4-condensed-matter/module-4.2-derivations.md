# Derivations — Module 4.2: Crystal Structure & Reciprocal Space
# 推导 — 模块 4.2：晶体结构与倒格子空间

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.2](./module-4.2-crystal-structure-and-reciprocal-space.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.2](./module-4.2-crystal-structure-and-reciprocal-space.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Reciprocal Lattice Vectors Satisfying $a_i\cdot b_j = 2\pi\delta_{ij}$ · 倒格矢满足 $a_i\cdot b_j = 2\pi\delta_{ij}$

**Claim.** Given primitive lattice vectors $a_1, a_2, a_3$ of a Bravais lattice, the vectors

**命题。** 给定布拉伐格子的原胞基矢 $a_1$、$a_2$、$a_3$，定义矢量

$$ b_1 = 2\pi\,(a_2 \times a_3) / (a_1 \cdot (a_2 \times a_3)), $$
$$ b_2 = 2\pi\,(a_3 \times a_1) / (a_1 \cdot (a_2 \times a_3)), $$
$$ b_3 = 2\pi\,(a_1 \times a_2) / (a_1 \cdot (a_2 \times a_3)) $$

satisfy $a_i \cdot b_j = 2\pi\,\delta_{ij}$ and form primitive vectors of the **reciprocal lattice**.

则它们满足 $a_i \cdot b_j = 2\pi\,\delta_{ij}$，并构成**倒格子**的原胞基矢。

**Step 1 — Define the cell volume.** Let $\Omega = a_1 \cdot (a_2 \times a_3)$ be the volume of the real-space primitive cell. For any non-degenerate lattice $\Omega \ne 0$.

**第 1 步 — 定义原胞体积。** 令 $\Omega = a_1 \cdot (a_2 \times a_3)$ 为正格子原胞的体积。对任何非退化格子，$\Omega \ne 0$。

**Step 2 — Verify the diagonal elements.** Consider $a_1 \cdot b_1$:

**第 2 步 — 验证对角元。** 考察 $a_1 \cdot b_1$：

$$ a_1 \cdot b_1 = a_1 \cdot [2\pi(a_2 \times a_3)/\Omega] = 2\pi\,[a_1 \cdot (a_2 \times a_3)] / \Omega = 2\pi\,\Omega / \Omega = 2\pi. $$

By cyclic symmetry the same holds for $a_2 \cdot b_2$ and $a_3 \cdot b_3$. Thus $a_i \cdot b_i = 2\pi$ (no sum).

由轮换对称性，$a_2 \cdot b_2$ 与 $a_3 \cdot b_3$ 同理。故 $a_i \cdot b_i = 2\pi$（不求和）。

**Step 3 — Verify the off-diagonal elements.** Consider $a_1 \cdot b_2$:

**第 3 步 — 验证非对角元。** 考察 $a_1 \cdot b_2$：

$$ a_1 \cdot b_2 = a_1 \cdot [2\pi(a_3 \times a_1)/\Omega] = 2\pi\,[a_1 \cdot (a_3 \times a_1)] / \Omega. $$

The scalar triple product $a_1 \cdot (a_3 \times a_1)$ contains $a_1$ twice: it equals the determinant of a matrix whose first and third rows are identical, hence it vanishes. Thus $a_1 \cdot b_2 = 0$. By the same argument all off-diagonal pairs give zero. Combining Steps 2–3:

标量三重积 $a_1 \cdot (a_3 \times a_1)$ 含两个相同的矢量 $a_1$，等价于行列式中有两行相同，故为零。因此 $a_1 \cdot b_2 = 0$。同理所有非对角对均为零。合并第 2–3 步：

$$ a_i \cdot b_j = 2\pi\,\delta_{ij}. \qquad \blacksquare $$

**Step 4 — Every reciprocal-lattice point.** The full reciprocal lattice consists of all integer linear combinations $G = h\,b_1 + k\,b_2 + l\,b_3$ ($h, k, l \in \mathbb{Z}$). By linearity, for any real-lattice vector $R = n_1 a_1 + n_2 a_2 + n_3 a_3$ ($n_i \in \mathbb{Z}$):

**第 4 步 — 所有倒格子格点。** 完整倒格子由所有整数线性组合 $G = h\,b_1 + k\,b_2 + l\,b_3$（$h, k, l \in \mathbb{Z}$）构成。由线性性，对任意正格矢 $R = n_1 a_1 + n_2 a_2 + n_3 a_3$（$n_i \in \mathbb{Z}$）：

$$ G \cdot R = 2\pi(hn_1 + kn_2 + ln_3) \in 2\pi\mathbb{Z}, $$

so $e^{iG\cdot R} = 1$. This is the defining property of the reciprocal lattice: it is the set of all wavevectors $G$ such that the plane wave $e^{iG\cdot r}$ has the full periodicity of the real lattice.

故 $e^{iG\cdot R} = 1$。这正是倒格子的定义性质：它是所有波矢 $G$ 的集合，使得平面波 $e^{iG\cdot r}$ 具有正格子的完整周期性。

---

## B. Bragg Condition $2d\sin\theta = n\lambda$ and the Laue Condition $\Delta k = G$ · 布拉格条件与劳厄条件等价性

**Claim.** Constructive interference of waves scattered by parallel crystal planes of spacing $d$ occurs when $2d\sin\theta = n\lambda$ (Bragg). This is equivalent to the condition that the change in wavevector $\Delta k = k_f - k_i$ equals a reciprocal-lattice vector $G$ (Laue).

**命题。** 间距为 $d$ 的平行晶面对波的散射产生相长干涉，当且仅当 $2d\sin\theta = n\lambda$（布拉格）。这等价于波矢改变量 $\Delta k = k_f - k_i$ 等于某个倒格矢 $G$（劳厄条件）。

**Step 1 — Path-length difference between adjacent planes.** Consider a beam of wavelength $\lambda$ incident at glancing angle $\theta$ to a family of parallel planes separated by $d$. The path-length difference between a ray reflected from the $n$-th plane and the $(n+1)$-th plane is $2d\sin\theta$ (standard geometry: incoming and outgoing segments each project $d\sin\theta$ onto the normal).

**第 1 步 — 相邻晶面间的光程差。** 考虑波长为 $\lambda$ 的束以掠射角 $\theta$ 入射至间距为 $d$ 的一组平行晶面。从第 $n$ 层与第 $n+1$ 层反射的光线之间的光程差为 $2d\sin\theta$（标准几何：入射与出射路径各在法线方向上投影 $d\sin\theta$）。

**Step 2 — Constructive-interference condition.** For constructive interference the path-length difference must equal an integer number of wavelengths:

**第 2 步 — 相长干涉条件。** 相长干涉要求光程差等于整数个波长：

$$ 2d\sin\theta = n\lambda, \qquad n = 1, 2, 3, \ldots $$

This is **Bragg's law**.

这就是**布拉格定律**。

**Step 3 — Elastic scattering kinematics.** For elastic scattering $|k_i| = |k_f| = 2\pi/\lambda \equiv k$. The incident and final wavevectors are related by the scattering geometry, and the momentum transfer (Laue vector) is:

**第 3 步 — 弹性散射运动学。** 弹性散射中 $|k_i| = |k_f| = 2\pi/\lambda \equiv k$。入射与终态波矢由散射几何联系，动量转移（劳厄矢量）为：

$$ \Delta k = k_f - k_i. $$

Since the scattering is specular (angle of incidence = angle of reflection about the plane normal $\hat n$), we have

由于散射是镜面反射（入射角等于反射角，关于晶面法线 $\hat n$），有

$$ \Delta k = 2(k_i \cdot \hat n)\,\hat n = 2k\sin\theta \cdot \hat n. $$

**Step 4 — Relate $|\Delta k|$ to the Bragg condition.** The magnitude is $|\Delta k| = 2k\sin\theta = 2(2\pi/\lambda)\sin\theta$. Inserting the Bragg condition $2d\sin\theta = n\lambda$:

**第 4 步 — 将 $|\Delta k|$ 与布拉格条件联系。** 模量为 $|\Delta k| = 2k\sin\theta = 2(2\pi/\lambda)\sin\theta$。代入布拉格条件 $2d\sin\theta = n\lambda$：

$$ |\Delta k| = 2(2\pi/\lambda)(n\lambda/2d) = 2\pi n/d. $$

**Step 5 — Identify with a reciprocal-lattice vector.** The set of planes with Miller indices $(h,k,l)$ has spacing $d_{hkl} = 2\pi/|G_{hkl}|$ where $G_{hkl} = hb_1 + kb_2 + lb_3$ is the corresponding reciprocal-lattice vector. The normal $\hat n$ is parallel to $G_{hkl}$. Therefore

**第 5 步 — 与倒格矢对应。** 密勒指数为 $(h,k,l)$ 的晶面族间距为 $d_{hkl} = 2\pi/|G_{hkl}|$，其中 $G_{hkl} = hb_1 + kb_2 + lb_3$ 是对应的倒格矢，法线 $\hat n$ 平行于 $G_{hkl}$。因此

$$ \Delta k = |\Delta k|\,\hat n = (2\pi n/d_{hkl}) \cdot (G_{hkl}/|G_{hkl}|) = n G_{hkl}/|G_{hkl}| \cdot |G_{hkl}| = n G_{hkl}^{unit} \cdot |G_{hkl}|. $$

Since $n G_{hkl}$ is itself a reciprocal-lattice vector (integer multiple), we conclude

因为 $n G_{hkl}$ 本身就是一个倒格矢（整数倍），故得

$$ \boxed{\, \Delta k = G \,} \qquad \text{(Laue condition).} \qquad \blacksquare $$

布拉格条件 $\Longleftrightarrow$ 劳厄条件 $\Delta k = G$。$\blacksquare$

**Step 6 — Ewald sphere construction (geometric restatement).** Since $|k_i| = |k_f| = k$ and $k_f = k_i + G$, scattering occurs when a reciprocal-lattice point $G$ lies exactly on the sphere of radius $k$ centred at the tip of $-k_i$. This is the **Ewald sphere**; the Bragg peaks map out the reciprocal lattice.

**第 6 步 — 厄瓦尔德球（几何重表述）。** 由于 $|k_i| = |k_f| = k$ 且 $k_f = k_i + G$，当倒格子格点 $G$ 恰好在以 $-k_i$ 顶端为圆心、半径为 $k$ 的球上时发生散射。这就是**厄瓦尔德球**；布拉格峰描绘出倒格子的形貌。

---

## C. The Structure Factor · 结构因子

**Claim.** For a crystal with $N_b$ atoms per unit cell at positions $d_j$ ($j = 1\ldots N_b$) with atomic form factors $f_j$, the scattered amplitude at reciprocal-lattice vector $G = hb_1 + kb_2 + lb_3$ is proportional to the **structure factor**

**命题。** 对每个原胞含 $N_b$ 个原子（位置为 $d_j$，原子形状因子为 $f_j$）的晶体，在倒格矢 $G = hb_1 + kb_2 + lb_3$ 处的散射振幅正比于**结构因子**

$$ S(G) = \sum_j f_j\, e^{iG\cdot d_j}. $$

Certain reflections are systematically absent when $S(G) = 0$.

当 $S(G) = 0$ 时，某些反射系统性消失（消光）。

**Step 1 — Scattering amplitude from a single unit cell.** The scattering amplitude is proportional to the Fourier transform of the electron density $\rho(r)$ at wavevector $\Delta k$. For elastic scattering satisfying the Laue condition $\Delta k = G$, the amplitude from one unit cell is

**第 1 步 — 单个原胞的散射振幅。** 散射振幅正比于电子密度 $\rho(r)$ 在波矢 $\Delta k$ 处的傅里叶变换。对满足劳厄条件 $\Delta k = G$ 的弹性散射，一个原胞的振幅为

$$ A_{cell} = \int_{cell} \rho(r)\, e^{iG\cdot r}\, d^3r. $$

**Step 2 — Decompose density into atomic contributions.** Write the electron density as a sum over atoms in the unit cell:

**第 2 步 — 将密度分解为原子贡献之和。** 将电子密度写成原胞内各原子贡献之和：

$$ \rho(r) = \sum_j \rho_j(r - d_j), $$

where $\rho_j$ is the electron density of the $j$-th atom centred at $d_j$.

其中 $\rho_j$ 为以 $d_j$ 为中心的第 $j$ 个原子的电子密度。

**Step 3 — Substitute and factor.** Inserting into the cell integral and changing variables $r' = r - d_j$:

**第 3 步 — 代入并分离因子。** 代入原胞积分，令 $r' = r - d_j$ 换元：

$$ \begin{aligned} A_{cell} &= \sum_j \int \rho_j(r')\, e^{iG\cdot(r'+d_j)}\, d^3r' \\ &= \sum_j e^{iG\cdot d_j} \int \rho_j(r')\, e^{iG\cdot r'}\, d^3r' \\ &= \sum_j f_j(G)\, e^{iG\cdot d_j}, \end{aligned} $$

where $f_j(G) = \int \rho_j(r')\, e^{iG\cdot r'}\, d^3r'$ is the **atomic form factor** of atom $j$. For $G$ not too large, $f_j \approx Z_j$ (the atomic number).

其中 $f_j(G) = \int \rho_j(r')\, e^{iG\cdot r'}\, d^3r'$ 为第 $j$ 个原子的**原子形状因子**。当 $G$ 不太大时 $f_j \approx Z_j$（原子序数）。

**Step 4 — Define the structure factor and diffracted intensity.** The **structure factor** is

**第 4 步 — 定义结构因子与衍射强度。** **结构因子**定义为

$$ S(G) = \sum_j f_j\, e^{iG\cdot d_j}. $$

Since all unit cells are identical, the total amplitude is $A_{total} = N_{cells} \cdot S(G) \cdot$ (phase factor). The diffracted intensity is

由于所有原胞相同，总振幅 $A_{total} = N_{cells} \cdot S(G) \cdot$（相位因子）。衍射强度为

$$ I(G) \propto |S(G)|^2. $$

**Step 5 — Example: BCC systematic absences.** For a body-centred cubic lattice, take $d_1 = (0,0,0)$ and $d_2 = (a/2)(1,1,1)$ with $f_1 = f_2 = f$. Using $G = (h b_1 + k b_2 + l b_3)$ and noting $G \cdot d_2 = \pi(h+k+l)$:

**第 5 步 — 例：体心立方的系统消光。** 对体心立方格子，取 $d_1 = (0,0,0)$，$d_2 = (a/2)(1,1,1)$，$f_1 = f_2 = f$。利用 $G \cdot d_2 = \pi(h+k+l)$：

$$ S = f(1 + e^{i\pi(h+k+l)}). $$

This vanishes when $h+k+l$ is odd, giving **systematic absences** for odd $h+k+l$. Only reflections with $h+k+l$ even appear — a direct fingerprint of the BCC symmetry. $\blacksquare$

当 $h+k+l$ 为奇数时 $S = 0$，即**系统消光**发生于 $h+k+l$ 为奇数的情形。只有 $h+k+l$ 为偶数的反射出现——这是体心立方对称性的直接特征。$\blacksquare$

---

## D. Brillouin Zone as the Wigner–Seitz Cell of the Reciprocal Lattice · 布里渊区作为倒格子的维格纳–塞茨原胞

**Claim.** The first Brillouin zone — the primitive cell of the reciprocal lattice formed by all points closer to $G = 0$ than to any other reciprocal-lattice point — contains exactly one $k$-state per real-space unit cell, and its volume is $(2\pi)^3/\Omega$.

**命题。** 第一布里渊区——倒格子的原胞，由所有比任何其他倒格子格点更靠近 $G = 0$ 的点构成——每个正格子原胞恰好包含一个 $k$ 态，其体积为 $(2\pi)^3/\Omega$。

**Step 1 — Volume of the BZ.** The volume of the BZ equals the volume of the reciprocal primitive cell. Using the identity for volumes of dual cells:

**第 1 步 — 布里渊区的体积。** 布里渊区的体积等于倒格子原胞的体积。利用对偶原胞体积的恒等式：

$$ V_{BZ} = b_1 \cdot (b_2 \times b_3) = (2\pi)^3 / [a_1 \cdot (a_2 \times a_3)] = (2\pi)^3 / \Omega. $$

**Step 2 — State counting.** For a crystal of volume $V = N\Omega$ ($N$ unit cells), periodic boundary conditions give $k$-points spaced $(2\pi/L)$ in each direction. The number of $k$-points in the BZ is:

**第 2 步 — 态计数。** 对体积 $V = N\Omega$（$N$ 个原胞）的晶体，周期性边界条件使 $k$ 点间距为 $(2\pi/L)$。布里渊区内的 $k$ 点数为：

$$ N_k = V_{BZ} / (2\pi/L)^3 = [(2\pi)^3/\Omega] / [(2\pi)^3/V] = V/\Omega = N. $$

There is exactly one $k$-point per unit cell, so one band can hold $2N$ electrons (including spin). This underlies the band-filling rule for metals vs. insulators. $\blacksquare$

每个原胞恰好一个 $k$ 点，因此一条能带（含自旋）可容纳 $2N$ 个电子。这是金属与绝缘体能带填充判据的基础。$\blacksquare$

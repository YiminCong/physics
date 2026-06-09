---
title: "Derivations — Module 6.7: Exactly Solvable Models & Long-Range Order"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 6.7: Exactly Solvable Models & Long-Range Order
# 推导 — 模块 6.7：精确可解模型与长程序

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.7](./module-6.7-exactly-solvable-models-and-long-range-order.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.7](./module-6.7-exactly-solvable-models-and-long-range-order.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Yang–Baxter Equation as the Factorization Condition · 杨–巴克斯特方程作为因式分解条件

**Claim.** Consider a 1D quantum system where particles interact pairwise via a two-body S-matrix $S_{12}(u)$. For the three-particle scattering to be consistent (i.e. for different orderings of two-body collisions to yield the same total S-matrix), the S-matrix must satisfy the **Yang–Baxter equation**:

$$ S_{12}(u-v)\, S_{13}(u)\, S_{23}(v) = S_{23}(v)\, S_{13}(u)\, S_{12}(u-v), $$

where the subscripts label which pair of particles scatter and $u, v$ are the rapidity variables (differences of particle momenta or spectral parameters).

**命题。** 考虑一个粒子通过两体 S 矩阵 $S_{12}(u)$ 成对相互作用的一维量子系统。为使三粒子散射自洽（即两体碰撞的不同顺序给出相同的总 S 矩阵），S 矩阵必须满足**杨–巴克斯特方程**：

$$ S_{12}(u-v)\, S_{13}(u)\, S_{23}(v) = S_{23}(v)\, S_{13}(u)\, S_{12}(u-v), $$

其中下标标记哪对粒子散射，$u$、$v$ 是快度变量（粒子动量差或谱参数）。

**Step 1 — Set up the three-particle scattering scenario.** Label three particles as 1, 2, 3 with rapidities $\theta_1 > \theta_2 > \theta_3$ (faster particles to the left in 1D). As time evolves, particles collide pairwise. There are two distinct sequences in which the three collisions 12, 13, 23 can occur, depending on the initial configuration:

  Ordering A: 1 first collides with 2, then 1 with 3, then 2 with 3.
  Ordering B: 2 first collides with 3, then 1 with 3, then 1 with 2.

**第 1 步 — 建立三粒子散射场景。** 标记三个粒子为 1、2、3，快度为 $\theta_1 > \theta_2 > \theta_3$（在一维中较快的粒子在左侧）。随着时间演化，粒子成对碰撞。三次碰撞 12、13、23 发生的顺序有两种不同方式，取决于初始构型：

  顺序 A：1 先与 2 碰撞，然后 1 与 3，然后 2 与 3。
  顺序 B：2 先与 3 碰撞，然后 1 与 3，然后 1 与 2。

**Step 2 — Write the S-matrix for each ordering.** Each two-body collision is described by the two-body S-matrix $S_{ij}(\theta_i - \theta_j)$ acting on the pair $(i,j)$ while being the identity on the remaining particle. All operators act on the three-particle space $V_1 \otimes V_2 \otimes V_3$.

$$ \text{Ordering A total S-matrix: } S_A = S_{23}(\theta_2-\theta_3) \cdot S_{13}(\theta_1-\theta_3) \cdot S_{12}(\theta_1-\theta_2). $$

$$ \text{Ordering B total S-matrix: } S_B = S_{12}(\theta_1-\theta_2) \cdot S_{13}(\theta_1-\theta_3) \cdot S_{23}(\theta_2-\theta_3). $$

**第 2 步 — 写出每种顺序的 S 矩阵。** 每次两体碰撞由两体 S 矩阵 $S_{ij}(\theta_i - \theta_j)$ 描述，作用于对 $(i,j)$，对剩余粒子为恒等。所有算符作用于三粒子空间 $V_1 \otimes V_2 \otimes V_3$。

$$ \text{顺序 A 的总 S 矩阵：} S_A = S_{23}(\theta_2-\theta_3) \cdot S_{13}(\theta_1-\theta_3) \cdot S_{12}(\theta_1-\theta_2). $$

$$ \text{顺序 B 的总 S 矩阵：} S_B = S_{12}(\theta_1-\theta_2) \cdot S_{13}(\theta_1-\theta_3) \cdot S_{23}(\theta_2-\theta_3). $$

**Step 3 — Demand factorization (integrability condition).** A theory is called **integrable** if the multi-particle S-matrix factorizes into a product of two-body S-matrices, independently of the collision ordering. This means the total scattering amplitude must be the same regardless of which sequence of two-body collisions occurs:

$$ S_A = S_B, $$

i.e.

$$ S_{23}(\theta_2-\theta_3)\, S_{13}(\theta_1-\theta_3)\, S_{12}(\theta_1-\theta_2) = S_{12}(\theta_1-\theta_2)\, S_{13}(\theta_1-\theta_3)\, S_{23}(\theta_2-\theta_3). $$

**第 3 步 — 要求因式分解（可积性条件）。** 若多粒子 S 矩阵因式分解为两体 S 矩阵之积，与碰撞顺序无关，则称理论为**可积**的。这意味着总散射幅必须与两体碰撞发生的顺序无关：

$$ S_A = S_B, $$

即

$$ S_{23}(\theta_2-\theta_3)\, S_{13}(\theta_1-\theta_3)\, S_{12}(\theta_1-\theta_2) = S_{12}(\theta_1-\theta_2)\, S_{13}(\theta_1-\theta_3)\, S_{23}(\theta_2-\theta_3). $$

**Step 4 — Rename to standard form.** Setting $u = \theta_1 - \theta_2$, $v = \theta_2 - \theta_3$ (so $\theta_1 - \theta_3 = u+v$) and using the notation $R_{12}(u)$ for the S-matrix (the conventional letter in the mathematics literature), the consistency condition becomes the **Yang–Baxter equation**:

$$ \boxed{\, R_{12}(u)\, R_{13}(u+v)\, R_{23}(v) = R_{23}(v)\, R_{13}(u+v)\, R_{12}(u) \,} \qquad \blacksquare $$

This equation is the central consistency condition of exactly solvable models. Its solutions — the R-matrices — classify all integrable systems. The Bethe ansatz wavefunction is the explicit eigenvector for any such R-matrix.

**第 4 步 — 改写为标准形式。** 令 $u = \theta_1 - \theta_2$，$v = \theta_2 - \theta_3$（故 $\theta_1 - \theta_3 = u+v$），并用数学文献中的惯例记号 $R_{12}(u)$ 表示 S 矩阵，相容性条件变为**杨–巴克斯特方程**：

$$ \boxed{\, R_{12}(u)\, R_{13}(u+v)\, R_{23}(v) = R_{23}(v)\, R_{13}(u+v)\, R_{12}(u) \,} \qquad \blacksquare $$

这个方程是精确可解模型的核心相容性条件。其解——R 矩阵——对所有可积系统进行分类。贝特拟设波函数是任意此类 R 矩阵的显式本征向量。

**Step 5 — Physical content: conservation of momenta.** The Yang–Baxter equation implies that the set of individual particle momenta $\{\theta_i\}$ is conserved in every scattering event: particles can only exchange momenta (no production or absorption). This is equivalent to the existence of an infinite tower of conserved charges $Q_n$ ($n = 1, 2, 3, \ldots$), which is the hallmark of integrability and the reason the Bethe ansatz gives exact eigenvalues for all energy levels.

**第 5 步 — 物理内容：动量守恒。** 杨–巴克斯特方程意味着每次散射中单个粒子动量集合 $\{\theta_i\}$ 守恒：粒子只能交换动量（没有产生或吸收）。这等价于无穷塔守恒荷 $Q_n$（$n = 1, 2, 3, \ldots$）的存在，这是可积性的标志，也是贝特拟设对所有能级给出精确本征值的原因。

---

## B. Lee–Yang Zeros and the Picture of a Phase Transition · 李–杨零点与相变图像

**Claim (Lee–Yang 1952).** The partition function $Z(z)$ of a lattice gas (or equivalently an Ising ferromagnet) is a polynomial in the fugacity $z = e^{\beta\mu}$. All zeros of $Z(z)$ lie on the unit circle $|z| = 1$ in the complex $z$-plane. In the thermodynamic limit, zeros condense into a continuous arc (the **Lee–Yang circle theorem**). A phase transition occurs exactly where a zero of $Z(z)$ pinches the real positive $z$-axis (the physical axis).

**命题（李–杨，1952）。** 格气（等价地，伊辛铁磁体）的配分函数 $Z(z)$ 是逸度 $z = e^{\beta\mu}$ 的多项式。$Z(z)$ 的所有零点都位于复 $z$ 平面的单位圆 $|z| = 1$ 上。在热力学极限下，零点凝聚成连续弧（**李–杨圆定理**）。相变恰好发生在 $Z(z)$ 的零点夹紧正实 $z$ 轴（物理轴）之处。

**Step 1 — Write the partition function as a polynomial in $z$.** For a lattice gas on $N$ sites with at most one particle per site and nearest-neighbor attractive interactions of strength $\varepsilon$, the grand-canonical partition function is

$$ Z(z) = \sum_{n=0}^{N} z^n \sum_{\text{configurations with } n \text{ particles}} e^{\beta\varepsilon \times (\text{number of nn pairs})}. $$

Since each configuration contributes a positive weight, $Z(z)$ is a polynomial of degree $N$ in $z$ with positive coefficients. It therefore has exactly $N$ zeros $z_1, \ldots, z_N$ in the complex plane:

$$ Z(z) = C \prod_{j=1}^{N} (z - z_j). $$

**第 1 步 — 将配分函数写成 $z$ 的多项式。** 对于每格点最多一个粒子、最近邻吸引相互作用强度为 $\varepsilon$ 的 $N$ 格点格气，巨正则配分函数为

$$ Z(z) = \sum_{n=0}^{N} z^n \sum_{n\text{粒子构型}} e^{\beta\varepsilon \times (\text{最近邻对数})}. $$

由于每个构型贡献正权重，$Z(z)$ 是 $z$ 的 $N$ 次多项式，系数为正。因此在复平面中恰好有 $N$ 个零点 $z_1, \ldots, z_N$：

$$ Z(z) = C \prod_{j=1}^{N} (z - z_j). $$

**Step 2 — Prove zeros lie on the unit circle (sketch of Lee–Yang circle theorem).** The Ising ferromagnet partition function at field $H \propto \ln z$ is symmetric under particle-hole symmetry $z \to 1/z$ combined with complex conjugation (for the specific choice of nearest-neighbor weights). Lee and Yang showed that this symmetry, combined with the positive-definiteness of the Boltzmann weights, forces all zeros to satisfy $|z_j| = 1$. The argument uses the fact that if $z_0$ is a zero, so is $1/z_0^*$; and the reflection symmetry combined with the positive-real-axis constraints confines all zeros to the unit circle. (A full proof requires the Heilmann–Lieb theorem on determinantal point processes; we state the result here.)

**第 2 步 — 证明零点位于单位圆上（李–杨圆定理概要）。** 在场 $H \propto \ln z$ 下的伊辛铁磁体配分函数在粒子-空穴对称性 $z \to 1/z$ 与复共轭联合作用下是对称的（对于特定的最近邻权重选取）。李和杨证明，这种对称性加上玻尔兹曼权重的正定性，迫使所有零点满足 $|z_j| = 1$。论证利用了若 $z_0$ 是零点则 $1/z_0^*$ 也是零点这一事实；反射对称性加上正实轴约束将所有零点限制在单位圆上。（完整证明需要 Heilmann–Lieb 关于行列式点过程的定理；此处陈述结论。）

**Step 3 — The thermodynamic limit and the Lee–Yang edge.** In the thermodynamic limit $N \to \infty$, the $N$ zeros on the unit circle become dense on some arc (or possibly the full circle). The free energy per site is

$$ f(z) = -\frac{1}{\beta N} \ln Z(z) = -\frac{1}{\beta} \int_{\text{circle}} d\nu(z')\, \ln|z - z'| + \text{const}, $$

where $d\nu$ is the limiting density of zeros. The **Lee–Yang edge singularity** is the endpoint of the zero arc — the point $z_e$ on the unit circle where the arc begins. As $z$ (from the real axis) approaches the real image of $z_e$, the free energy develops a branch-point singularity.

**第 3 步 — 热力学极限与李–杨边奇点。** 在热力学极限 $N \to \infty$ 中，单位圆上的 $N$ 个零点在某段弧上（或可能整个圆上）变得稠密。每格点自由能为

$$ f(z) = -\frac{1}{\beta N} \ln Z(z) = -\frac{1}{\beta} \int_{\text{circle}} d\nu(z')\, \ln|z - z'| + \text{const}, $$

其中 $d\nu$ 是零点的极限密度。**李–杨边奇点**是零点弧的端点——弧开始的单位圆上的点 $z_e$。当 $z$（从实轴趋近）接近 $z_e$ 的实轴投影时，自由能发展出分支点奇点。

**Step 4 — Phase transitions from the pinching condition.** For the physical fugacity $z > 0$ (real positive), the partition function $Z(z)$ has no zeros (all zeros are on the unit circle, not the positive real axis). Therefore, for any finite $N$, $\ln Z(z)$ is analytic on the positive real axis: **no phase transition at finite $N$** (Lee–Yang theorem, 1952). A phase transition occurs in the thermodynamic limit $N \to \infty$ when and only when the zero density $d\nu(z')$ is nonzero at a point $z' = 1$ (the unit circle intersects the physical axis), i.e. the arc of zeros reaches and pinches the real axis at $z = 1$. At that point, $\ln Z$ develops a non-analyticity: **a phase transition**. $\blacksquare$

**第 4 步 — 相变来自夹紧条件。** 对于物理逸度 $z > 0$（正实数），配分函数 $Z(z)$ 没有零点（所有零点在单位圆上，不在正实轴上）。因此，对任意有限 $N$，$\ln Z(z)$ 在正实轴上是解析的：**有限 $N$ 时无相变**（李–杨定理，1952）。相变仅在热力学极限 $N \to \infty$ 下发生，当且仅当零点密度 $d\nu(z')$ 在 $z' = 1$（单位圆与物理轴的交点）处非零，即零点弧到达并夹紧 $z = 1$ 处的实轴。在该点，$\ln Z$ 发展出非解析性：**相变**。$\blacksquare$

---

## C. Off-Diagonal Long-Range Order (ODLRO) · 非对角长程序（ODLRO）

**Claim (Yang 1962).** A many-body system exhibits **off-diagonal long-range order** if the two-particle reduced density matrix $\rho_2(x,y; x',y') = \langle \Psi^\dagger(x)\, \Psi^\dagger(y)\, \Psi(y')\, \Psi(x') \rangle$ does not vanish as $|x-x'| \to \infty$ (and similarly $|y-y'| \to \infty$):

$$ \rho_2(x,y; x',y') \to F^*(x,y)\, F(x',y') \quad \text{as} \quad |x-x'| \to \infty, $$

for some function $F$. For bosons (Bose–Einstein condensation), the analogous condition is on the one-body density matrix $\rho_1(x; x') = \langle \Psi^\dagger(x)\, \Psi(x') \rangle \to \varphi^*(x)\, \varphi(x')$ as $|x-x'| \to \infty$.

**命题（杨振宁，1962）。** 若两粒子约化密度矩阵 $\rho_2(x,y; x',y') = \langle \Psi^\dagger(x)\, \Psi^\dagger(y)\, \Psi(y')\, \Psi(x') \rangle$ 在 $|x-x'| \to \infty$（及类似 $|y-y'| \to \infty$）时不消失，则多体系统具有**非对角长程序**：

$$ \rho_2(x,y; x',y') \to F^*(x,y)\, F(x',y') \quad \text{当} \quad |x-x'| \to \infty \text{ 时}, $$

对某个函数 $F$。对于玻色子（玻色–爱因斯坦凝聚），类似条件作用于单体密度矩阵 $\rho_1(x; x') = \langle \Psi^\dagger(x)\, \Psi(x') \rangle \to \varphi^*(x)\, \varphi(x')$ 当 $|x-x'| \to \infty$ 时。

**Step 1 — Reduced density matrices.** In second quantization, the two-particle reduced density matrix (2-RDM) is

$$ \rho_2(x,y; x',y') = \langle \Psi_0 |\, \hat\Psi^\dagger(x)\, \hat\Psi^\dagger(y)\, \hat\Psi(y')\, \hat\Psi(x')\, | \Psi_0 \rangle, $$

where $|\Psi_0\rangle$ is the many-body ground state and $\hat\Psi(x)$ is the field operator. This object describes two-particle correlations: $\rho_2$ gives the probability amplitude for finding a particle at $x$ and one at $y$, and simultaneously a particle at $x'$ and one at $y'$.

**第 1 步 — 约化密度矩阵。** 在二次量子化中，两粒子约化密度矩阵（2-RDM）为

$$ \rho_2(x,y; x',y') = \langle \Psi_0 |\, \hat\Psi^\dagger(x)\, \hat\Psi^\dagger(y)\, \hat\Psi(y')\, \hat\Psi(x')\, | \Psi_0 \rangle, $$

其中 $|\Psi_0\rangle$ 是多体基态，$\hat\Psi(x)$ 是场算符。该对象描述两粒子关联：$\rho_2$ 给出在 $x$ 和 $y$ 处各找到一个粒子、同时在 $x'$ 和 $y'$ 处各找到一个粒子的概率幅。

**Step 2 — Normal state vs. ODLRO.** In a normal (non-condensed) state, correlations decay at large separations: $\rho_2(x,y; x',y') \to \rho_1(x; x')\, \rho_1(y; y') - \rho_1(x; y')\, \rho_1(y; x')$ (by cluster decomposition), and all one-body off-diagonal elements $\rho_1(x; x') \to 0$ as $|x-x'| \to \infty$. In a superconductor, the BCS ground state has a macroscopic occupation of Cooper pairs, and the anomalous average $\langle \hat\Psi(x)\, \hat\Psi(y) \rangle = F(x,y) \ne 0$ (the pair wavefunction). This means

$$ \rho_2(x,y; x',y') \to F^*(x,y)\, F(x',y') \quad \text{as} \quad |x-x'| \to \infty, $$

which does NOT go to zero — this is ODLRO. The name "off-diagonal" refers to the fact that $x \ne x'$ (and $y \ne y'$), i.e. the density matrix is large away from its diagonal.

**第 2 步 — 正常态与非对角长程序。** 在正常（非凝聚）态中，关联在大间隔处衰减：$\rho_2(x,y; x',y') \to \rho_1(x; x')\, \rho_1(y; y') - \rho_1(x; y')\, \rho_1(y; x')$（由团簇分解），且所有单体非对角元 $\rho_1(x; x') \to 0$ 当 $|x-x'| \to \infty$ 时。在超导体中，BCS 基态有库珀对的宏观占据，反常平均值 $\langle \hat\Psi(x)\, \hat\Psi(y) \rangle = F(x,y) \ne 0$（对波函数）。这意味着

$$ \rho_2(x,y; x',y') \to F^*(x,y)\, F(x',y') \quad \text{当} \quad |x-x'| \to \infty \text{ 时}, $$

这不趋于零——这就是非对角长程序。"非对角"之名指 $x \ne x'$（以及 $y \ne y'$），即密度矩阵在其对角线之外仍很大。

**Step 3 — Eigenvalue interpretation.** Diagonalize the 2-RDM as $\rho_2(x,y; x',y') = \sum_n \lambda_n\, \varphi_n^*(x,y)\, \varphi_n(x',y')$. ODLRO is the statement that the largest eigenvalue $\lambda_{\max}$ is macroscopic: $\lambda_{\max} = O(N^2)$ (for $N$ particles). This is the precise mathematical statement of **macroscopic quantum coherence**: the system has a macroscopic number of pairs described by the same two-particle wavefunction $\varphi_{\max}(x,y)$. In a BCS superconductor, $\varphi_{\max}(x,y) = F(x,y)$ is the Cooper pair wavefunction, and $\lambda_{\max} \approx (N/2)^2$ (all $N/2$ Cooper pairs in the same state).

**第 3 步 — 本征值诠释。** 将 2-RDM 对角化为 $\rho_2(x,y; x',y') = \sum_n \lambda_n\, \varphi_n^*(x,y)\, \varphi_n(x',y')$。非对角长程序的表述是最大本征值 $\lambda_{\max}$ 是宏观的：$\lambda_{\max} = O(N^2)$（对 $N$ 个粒子）。这是**宏观量子相干**的精确数学表述：系统有宏观数量的粒子对，由同一个两粒子波函数 $\varphi_{\max}(x,y)$ 描述。在 BCS 超导体中，$\varphi_{\max}(x,y) = F(x,y)$ 是库珀对波函数，$\lambda_{\max} \approx (N/2)^2$（所有 $N/2$ 个库珀对处于同一态）。

---

## D. The Byers–Yang Theorem and $h/2e$ Flux Quantization · Byers–Yang 定理与 $h/2e$ 磁通量子化

**Claim (Byers–Yang 1961).** For a superconducting ring threaded by magnetic flux $\Phi$, the physical observable quantities (energy, current, etc.) are periodic in $\Phi$ with period $h/2e$ (not $h/e$ as for a single electron). This factor of 2 is a direct signature of electron pairing (Cooper pairs of charge $2e$).

**命题（Byers–Yang，1961）。** 对于穿有磁通量 $\Phi$ 的超导环，物理可观测量（能量、电流等）关于 $\Phi$ 以 $h/2e$ 为周期（而非单电子的 $h/e$）。这个因子 2 是电子配对（电荷为 $2e$ 的库珀对）的直接标志。

**Step 1 — Gauge invariance under a flux insertion.** Consider a superconducting ring of circumference $L$ with a magnetic flux $\Phi$ through the ring (but the field $B = 0$ along the ring). The vector potential along the ring contributes a phase: the single-particle wavefunction picks up a phase $e^{i2\pi\Phi/\Phi_0}$ on going once around the ring (Aharonov–Bohm effect, Module 3.9), where $\Phi_0 = h/e$ is the single-electron flux quantum.

**第 1 步 — 插入磁通量下的规范不变性。** 考虑周长为 $L$ 的超导环，环中穿有磁通量 $\Phi$（但沿环的磁场 $B = 0$）。沿环的矢量势贡献一个相位：单粒子波函数绕环一周后获得相位 $e^{i2\pi\Phi/\Phi_0}$（阿哈罗诺夫–玻姆效应，模块 3.9），其中 $\Phi_0 = h/e$ 是单电子磁通量子。

**Step 2 — The Cooper pair wavefunction and the pairing phase.** In the BCS superconductor, the relevant degrees of freedom are Cooper pairs with charge $q = 2e$ (two electrons). The pair wavefunction $F(x,y) = \langle \hat\Psi(x)\, \hat\Psi(y) \rangle$ acquires a phase $e^{i2\pi(2e)/h \cdot \oint A\cdot dl} = e^{i4\pi\Phi/\Phi_0} = e^{i2\pi\Phi/(\Phi_0/2)}$ when the center of mass of the pair goes once around the ring.

For the physical state to be single-valued (required by quantum mechanics), the pair wavefunction must satisfy the boundary condition $F(x + L) = F(x)$. This gives:

$$ e^{i2\pi \Phi/(h/2e)} = 1 \implies \Phi = n \cdot h/(2e) \quad \text{for integer } n. $$

**第 2 步 — 库珀对波函数与配对相位。** 在 BCS 超导体中，相关自由度是电荷 $q = 2e$ 的库珀对（两个电子）。当对的质心绕环一周时，对波函数 $F(x,y) = \langle \hat\Psi(x)\, \hat\Psi(y) \rangle$ 获得相位 $e^{i2\pi(2e)/h \cdot \oint A\cdot dl} = e^{i4\pi\Phi/\Phi_0} = e^{i2\pi\Phi/(\Phi_0/2)}$。

为使物理态单值（量子力学要求），对波函数必须满足边界条件 $F(x + L) = F(x)$。这给出：

$$ e^{i2\pi \Phi/(h/2e)} = 1 \implies \Phi = n \cdot h/(2e), \quad n \text{ 为整数}. $$

**Step 3 — Formal derivation via gauge transformation.** More formally, consider the Hamiltonian with flux $\Phi$: $\hat H(\Phi)$ with minimal coupling $\partial_x \to \partial_x - iq A_x/\hbar$ ($q = 2e$ for pairs). A gauge transformation with parameter $\chi(x) = \Phi x/L$ (linear in $x$, which is single-valued only after going around the ring by one period that changes by $\Phi$) transforms $\hat H(\Phi) \to e^{iq \chi/\hbar}\, \hat H(0)\, e^{-iq \chi/\hbar}$, but the boundary conditions on the eigenfunctions pick up a phase $e^{iq\Phi L/\hbar L} = e^{i2e\Phi/\hbar} = e^{i4\pi\Phi/\Phi_0}$.

The transformed problem is equivalent to the zero-flux problem with twisted boundary conditions $\psi(L) = e^{i4\pi\Phi/\Phi_0}\, \psi(0)$. Demanding single-valuedness of all physical observables (which depend on products $\psi^*\psi$ or $F^*F$) requires the twist to be trivial modulo $2\pi$, which gives the flux quantum $h/(2e)$. Observables are periodic:

$$ \boxed{\, O(\Phi + h/2e) = O(\Phi) \,} \qquad \blacksquare $$

**第 3 步 — 通过规范变换的形式推导。** 更形式化地，考虑有磁通量 $\Phi$ 的哈密顿量：$\hat H(\Phi)$，带最小耦合 $\partial_x \to \partial_x - iq A_x/\hbar$（对于对，$q = 2e$）。参数为 $\chi(x) = \Phi x/L$（关于 $x$ 线性，仅在绕环一周改变 $\Phi$ 后才单值）的规范变换将 $\hat H(\Phi) \to e^{iq \chi/\hbar}\, \hat H(0)\, e^{-iq \chi/\hbar}$，但本征函数的边界条件获得相位 $e^{iq\Phi L/\hbar L} = e^{i2e\Phi/\hbar} = e^{i4\pi\Phi/\Phi_0}$。

变换后的问题等价于零磁通问题但有扭曲边界条件 $\psi(L) = e^{i4\pi\Phi/\Phi_0}\, \psi(0)$。要求所有物理可观测量（依赖于 $\psi^*\psi$ 或 $F^*F$ 之积）单值，需要扭曲量关于 $2\pi$ 是平凡的，这给出磁通量子 $h/(2e)$。可观测量是周期性的：

$$ \boxed{\, O(\Phi + h/2e) = O(\Phi) \,} \qquad \blacksquare $$

**Step 4 — Experimental significance.** The $h/2e$ periodicity of persistent currents and the Little–Parks oscillations in a superconducting cylinder were measured experimentally in the 1960s and confirmed the Cooper pair interpretation. For a normal metal (single-electron excitations, $q = e$), the periodicity would be $h/e$. The halving of the period is unambiguous evidence of pairing and cannot be explained by any single-electron theory. This connects ODLRO (the macroscopic pair wavefunction $F \ne 0$) directly to a macroscopically observable effect (flux quantization in units of $h/2e$). $\blacksquare$

**第 4 步 — 实验意义。** 持久电流的 $h/2e$ 周期性以及超导圆柱中的 Little–Parks 振荡在 20 世纪 60 年代被实验测量，证实了库珀对诠释。对于正常金属（单电子激发，$q = e$），周期将为 $h/e$。周期减半是配对的明确证据，任何单电子理论都无法解释。这将非对角长程序（宏观对波函数 $F \ne 0$）直接与宏观可观测效应（$h/2e$ 单位的磁通量子化）联系起来。$\blacksquare$

---

*The Yang–Baxter equation demonstrates that factorization is a theorem about consistency, not an approximation. The Lee–Yang picture makes the concept of a phase transition rigorous — it is a property of the thermodynamic limit, not of any finite system. ODLRO and Byers–Yang give the precise microscopic meaning of superconducting order and the mechanistic reason for flux quantization, connecting abstract field theory to direct experiment.*

*杨–巴克斯特方程表明因式分解是关于自洽性的定理，而非近似。李–杨图像使相变概念严格化——它是热力学极限的性质，而非任何有限系统的性质。非对角长程序和 Byers–Yang 给出超导序精确的微观含义以及磁通量子化的机制原因，将抽象场论与直接实验联系起来。*

# Derivations — Module 4.3: Lattice Vibrations & Phonons
# 推导 — 模块 4.3：晶格振动与声子

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.3](./module-4.3-lattice-vibrations-and-phonons.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.3](./module-4.3-lattice-vibrations-and-phonons.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Monatomic 1D Chain Dispersion $\omega(k) = 2\sqrt{K/M}\,|\sin(ka/2)|$ · 单原子一维链色散关系

**Claim.** For a 1D chain of identical atoms of mass $M$ connected by springs of constant $K$ with equilibrium spacing $a$, the normal-mode dispersion is $\omega(k) = 2\sqrt{K/M}\,|\sin(ka/2)|$, with $k \in (-\pi/a, \pi/a]$ (first Brillouin zone).

**命题。** 对质量为 $M$、平衡间距为 $a$、弹簧常数为 $K$ 的一维单原子链，简正模色散关系为 $\omega(k) = 2\sqrt{K/M}\,|\sin(ka/2)|$，$k \in (-\pi/a, \pi/a]$（第一布里渊区）。

**Step 1 — Set up the equation of motion.** Label atoms by integer $n$; let $u_n$ be the displacement from equilibrium. In the nearest-neighbour approximation, the force on atom $n$ comes from its two neighbours:

**第 1 步 — 建立运动方程。** 用整数 $n$ 标记原子；$u_n$ 为偏离平衡位置的位移。在最近邻近似下，作用在第 $n$ 个原子上的力来自其两侧邻居：

$$ M\ddot u_n = K(u_{n+1} - u_n) + K(u_{n-1} - u_n) = K(u_{n+1} + u_{n-1} - 2u_n). $$

This is Newton's second law applied to a harmonic chain. Each atom feels a restoring force proportional to the relative displacement from its neighbours.

这是对谐振子链应用牛顿第二定律。每个原子受到正比于其与邻居相对位移的恢复力。

**Step 2 — Plane-wave ansatz.** Try a travelling-wave solution of the form

**第 2 步 — 平面波拟设。** 尝试行波解

$$ u_n(t) = A\, e^{i(kna - \omega t)}, $$

where $k$ is the wavevector and $\omega$ is the angular frequency to be determined. This ansatz respects the discrete translational symmetry of the chain.

其中 $k$ 为波矢，$\omega$ 为待定角频率。此拟设尊重链的离散平移对称性。

**Step 3 — Substitute into the equation of motion.** Inserting $u_n = A\, e^{i(kna-\omega t)}$ into $M\ddot u_n = K(u_{n+1} + u_{n-1} - 2u_n)$:

**第 3 步 — 代入运动方程。** 将 $u_n = A\, e^{i(kna-\omega t)}$ 代入 $M\ddot u_n = K(u_{n+1} + u_{n-1} - 2u_n)$：

$$ M(-\omega^2)\, A\, e^{i(kna-\omega t)} = K A\, e^{i(kna-\omega t)}\, [e^{ika} + e^{-ika} - 2]. $$

Dividing both sides by $A\, e^{i(kna-\omega t)} \ne 0$:

两边除以 $A\, e^{i(kna-\omega t)} \ne 0$：

$$ -M\omega^2 = K(e^{ika} + e^{-ika} - 2) = K(2\cos(ka) - 2) = -4K\sin^2(ka/2). $$

Here we used $e^{ika} + e^{-ika} = 2\cos(ka)$ and $1 - \cos(ka) = 2\sin^2(ka/2)$.

这里用到 $e^{ika} + e^{-ika} = 2\cos(ka)$ 以及 $1 - \cos(ka) = 2\sin^2(ka/2)$。

**Step 4 — Solve for $\omega(k)$.**

**第 4 步 — 求解 $\omega(k)$。**

$$ \omega^2 = (4K/M)\sin^2(ka/2). $$

Taking the positive square root (physical frequencies $\omega \ge 0$):

取正平方根（物理频率 $\omega \ge 0$）：

$$ \omega(k) = 2\sqrt{K/M}\,|\sin(ka/2)|. $$

**Step 5 — First Brillouin zone and periodicity.** The dispersion is periodic: $\omega(k + 2\pi/a) = \omega(k)$. Values of $k$ differing by $2\pi/a$ describe the same physical mode (they produce identical displacements on all atoms). The independent modes are therefore restricted to the first Brillouin zone $k \in (-\pi/a, \pi/a]$, which contains exactly $N$ modes for a chain of $N$ atoms with periodic boundary conditions. $\blacksquare$

**第 5 步 — 第一布里渊区与周期性。** 色散关系是周期性的：$\omega(k + 2\pi/a) = \omega(k)$。相差 $2\pi/a$ 的 $k$ 值描述相同的物理模式（它们在所有原子上产生相同位移）。因此独立模式限制在第一布里渊区 $k \in (-\pi/a, \pi/a]$，对于周期性边界条件下 $N$ 个原子的链，恰好包含 $N$ 个模式。$\blacksquare$

**Step 6 — Physical limits.** (i) Long-wavelength (acoustic) limit $ka \ll 1$: $\sin(ka/2) \approx ka/2$, so $\omega \approx \sqrt{K/M} \cdot ka$ — linear dispersion, with sound velocity $v_s = a\sqrt{K/M}$. (ii) Zone-boundary $k = \pi/a$: $\omega_{max} = 2\sqrt{K/M}$ — the maximum frequency, corresponding to neighbouring atoms oscillating out of phase. (iii) Group velocity $v_g = d\omega/dk = a\sqrt{K/M}\cos(ka/2) \to 0$ at the zone boundary, indicating a standing wave.

**第 6 步 — 物理极限。** (i) 长波（声学）极限 $ka \ll 1$：$\sin(ka/2) \approx ka/2$，故 $\omega \approx \sqrt{K/M} \cdot ka$——线性色散，声速 $v_s = a\sqrt{K/M}$。(ii) 区边界 $k = \pi/a$：$\omega_{max} = 2\sqrt{K/M}$——最大频率，对应相邻原子反相振荡。(iii) 群速度 $v_g = d\omega/dk = a\sqrt{K/M}\cos(ka/2)$，在区边界趋于零，表明此处为驻波。

---

## B. Diatomic Chain: Acoustic and Optical Branches · 双原子链：声学支与光学支

**Claim.** A 1D diatomic chain with masses $M_1, M_2$ ($M_1 > M_2$) and spring constant $K$ has two branches: an **acoustic branch** $\omega_- \to 0$ as $k \to 0$ and an **optical branch** $\omega_+ \to \sqrt{2K/\mu}$ at $k = 0$, where $\mu = M_1 M_2/(M_1+M_2)$ is the reduced mass. A frequency gap opens at the zone boundary.

**命题。** 质量为 $M_1$、$M_2$（$M_1 > M_2$）、弹簧常数为 $K$ 的一维双原子链有两支：**声学支** $\omega_- \to 0$（$k \to 0$），和**光学支** $\omega_+ \to \sqrt{2K/\mu}$（$k = 0$），其中 $\mu = M_1 M_2/(M_1+M_2)$ 为约化质量。在区边界处打开频率隙。

**Step 1 — Equations of motion.** Label the unit cell by index $n$ with atoms of mass $M_1$ at position $na$ (displacement $u_n$) and $M_2$ at $na + d$ (displacement $v_n$):

**第 1 步 — 运动方程。** 用指数 $n$ 标记原胞：质量 $M_1$ 的原子在位置 $na$（位移 $u_n$），质量 $M_2$ 的原子在 $na + d$（位移 $v_n$）：

$$ \begin{aligned} M_1\ddot u_n &= K(v_n - u_n) + K(v_{n-1} - u_n) = K(v_n + v_{n-1} - 2u_n), \\ M_2\ddot v_n &= K(u_{n+1} - v_n) + K(u_n - v_n) = K(u_{n+1} + u_n - 2v_n). \end{aligned} $$

**Step 2 — Plane-wave ansatz.** Try

**第 2 步 — 平面波拟设。** 尝试

$$ u_n = U\, e^{i(kna-\omega t)}, \qquad v_n = V\, e^{i(kna-\omega t)}. $$

Substituting:

代入得：

$$ \begin{aligned} -M_1\omega^2 U &= K V(1 + e^{-ika}) - 2KU, \\ -M_2\omega^2 V &= K U(e^{ika} + 1) - 2KV. \end{aligned} $$

**Step 3 — Matrix eigenvalue problem.** Rewriting in matrix form:

**第 3 步 — 矩阵本征值问题。** 改写为矩阵形式：

$$ \begin{pmatrix} 2K - M_1\omega^2 & -K(1+e^{-ika}) \\ -K(1+e^{ika}) & 2K - M_2\omega^2 \end{pmatrix} \begin{pmatrix} U \\ V \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}. $$

For non-trivial solutions the determinant must vanish:

要有非平凡解，行列式须为零：

$$ (2K - M_1\omega^2)(2K - M_2\omega^2) - K^2|1 + e^{ika}|^2 = 0. $$

Note $|1 + e^{ika}|^2 = (1+\cos(ka))\cdot 2 = 4\cos^2(ka/2)$.

注意 $|1 + e^{ika}|^2 = 2(1 + \cos(ka)) = 4\cos^2(ka/2)$。

**Step 4 — Solve the secular equation.** Expanding:

**第 4 步 — 求解久期方程。** 展开：

$$ \begin{aligned} M_1 M_2\,\omega^4 - 2K(M_1+M_2)\omega^2 + 4K^2[1 - \cos^2(ka/2)] &= 0 \\ M_1 M_2\,\omega^4 - 2K(M_1+M_2)\omega^2 + 4K^2\sin^2(ka/2) &= 0. \end{aligned} $$

Using the quadratic formula with respect to $\omega^2$:

对 $\omega^2$ 用求根公式：

$$ \omega^2 = K(M_1+M_2)/(M_1 M_2) \pm K\sqrt{(M_1+M_2)^2/(M_1 M_2)^2 - 4\sin^2(ka/2)/(M_1 M_2)}. $$

**Step 5 — Two branches.** The $\pm$ sign gives two solutions:

**第 5 步 — 两支解。** $\pm$ 号给出两个解：

$$ \omega_\pm^2 = (K/\mu_r)[1 \pm \sqrt{1 - 4\mu_r^2\sin^2(ka/2)/M_1 M_2}], $$

where $\mu_r = M_1 M_2/(M_1+M_2)$ is the reduced mass and we used $M_1 M_2/(M_1+M_2) = \mu_r$. More explicitly:

其中 $\mu_r = M_1 M_2/(M_1+M_2)$ 为约化质量。更明确地：

$$ \omega^2_\pm = K(M_1+M_2)/(M_1 M_2) \pm K\sqrt{[(M_1+M_2)/(M_1 M_2)]^2 - 4\sin^2(ka/2)/(M_1 M_2)}. $$

**Step 6 — $k = 0$ limit.** At $k = 0$, $\sin(ka/2) = 0$:

**第 6 步 — $k = 0$ 极限。** 在 $k = 0$ 处，$\sin(ka/2) = 0$：

$$ \begin{aligned} \omega_-^2(0) &= 0 \quad \text{(acoustic branch, both atoms move in phase),} \\ \omega_+^2(0) &= 2K(M_1+M_2)/(M_1 M_2) = 2K/\mu_r \quad \text{(optical branch, atoms move out of phase).} \end{aligned} $$

The acoustic branch has a linear dispersion $\omega_- \approx v_s k$ near $k = 0$ (sound wave). The optical branch has a finite frequency at $k = 0$ and can be excited by light whose electric field drives the oppositely-charged sub-lattices against each other — hence "optical".

声学支在 $k = 0$ 附近有线性色散 $\omega_- \approx v_s k$（声波）。光学支在 $k = 0$ 处有有限频率，可被光的电场激发（光场驱动带异号电荷的子格子相向运动）——故称"光学"支。

**Step 7 — Zone-boundary gap.** At $k = \pi/a$:

**第 7 步 — 区边界频率隙。** 在 $k = \pi/a$ 处：

$$ \omega^2_+(\pi/a) = 2K/M_2, \qquad \omega^2_-(\pi/a) = 2K/M_1. $$

The frequency gap between the two branches is

两支之间的频率隙为

$$ \Delta\omega = \sqrt{2K/M_2} - \sqrt{2K/M_1} > 0 \quad \text{(since } M_1 > M_2\text{).} $$

No modes exist in this gap; it represents a phononic band gap. $\blacksquare$

此隙内无模式存在，即声子带隙。$\blacksquare$

---

## C. Quantization of a Normal Mode: Phonons · 简正模的量子化：声子

**Claim.** Each normal mode of the lattice is equivalent to a harmonic oscillator with frequency $\omega_k$. Quantizing it yields **phonons**: quanta of lattice vibration with energy $\hbar\omega_k$, zero-point energy $\tfrac12\hbar\omega_k$, and Bose–Einstein occupation number $\bar n_k = 1/(e^{\hbar\omega_k/k_B T} - 1)$.

**命题。** 晶格的每个简正模等价于频率为 $\omega_k$ 的谐振子。对其量子化得到**声子**：晶格振动的量子，能量为 $\hbar\omega_k$，零点能 $\tfrac12\hbar\omega_k$，玻色–爱因斯坦占据数 $\bar n_k = 1/(e^{\hbar\omega_k/k_B T} - 1)$。

**Step 1 — Normal coordinate transformation.** Introduce the normal coordinate $Q_k$ via the discrete Fourier transform

**第 1 步 — 简正坐标变换。** 通过离散傅里叶变换引入简正坐标 $Q_k$

$$ u_n = (1/\sqrt{NM}) \sum_k Q_k\, e^{ikna}, $$

where the sum runs over the $N$ allowed $k$-values in the first BZ. Under this transformation the Hamiltonian decouples:

其中求和遍历第一布里渊区内所有 $N$ 个允许的 $k$ 值。在此变换下哈密顿量解耦：

$$ H = \tfrac12 \sum_k [|\dot Q_k|^2 + \omega_k^2 |Q_k|^2]. $$

Each $k$-mode appears as an **independent harmonic oscillator** with mass 1 and frequency $\omega_k$.

每个 $k$ 模式表现为质量为 1、频率为 $\omega_k$ 的**独立谐振子**。

**Step 2 — Quantize each mode.** Following the ladder-operator procedure of Module 3.2 Section B, define for each $k$:

**第 2 步 — 对每个模式量子化。** 按模块 3.2 B 节的升降算符方法，对每个 $k$ 定义：

$$ \hat a_k = \sqrt{\omega_k/2\hbar}\,(Q_k + i P_k/\omega_k), \qquad \hat a^\dagger_k = \sqrt{\omega_k/2\hbar}\,(Q_k - i P_k/\omega_k), $$

where $P_k = \dot Q_k$ is the conjugate momentum. The canonical commutation relation $[Q_k, P_{k'}] = i\hbar\, \delta_{kk'}$ gives

其中 $P_k = \dot Q_k$ 为正则动量。正则对易关系 $[Q_k, P_{k'}] = i\hbar\, \delta_{kk'}$ 给出

$$ [\hat a_k, \hat a^\dagger_{k'}] = \delta_{kk'}. $$

**Step 3 — Hamiltonian in terms of phonon operators.** Rewriting in exact parallel with Module 3.2:

**第 3 步 — 用声子算符表示哈密顿量。** 与模块 3.2 完全平行地改写：

$$ H = \sum_k \hbar\omega_k\, (\hat a^\dagger_k \hat a_k + \tfrac12) = \sum_k \hbar\omega_k\, (\hat n_k + \tfrac12), $$

where $\hat n_k = \hat a^\dagger_k \hat a_k$ is the phonon number operator for mode $k$.

其中 $\hat n_k = \hat a^\dagger_k \hat a_k$ 为模式 $k$ 的声子数算符。

**Step 4 — Phonon spectrum.** The eigenvalues of $\hat n_k$ are non-negative integers $n_k = 0, 1, 2, \ldots,$ (proved exactly as in Module 3.2 Step 6 — the same boundedness argument applies). The energy eigenvalue for a given set of occupation numbers $\{n_k\}$ is

**第 4 步 — 声子谱。** $\hat n_k$ 的本征值为非负整数 $n_k = 0, 1, 2, \ldots$（证明与模块 3.2 第 6 步完全相同——相同的有界性论证适用）。给定一组占据数 $\{n_k\}$ 的能量本征值为

$$ E = \sum_k \hbar\omega_k\, (n_k + \tfrac12). $$

State $|n_{k_1}, n_{k_2}, \ldots\rangle$ contains $n_{k_j}$ phonons of mode $j$. Adding one phonon of mode $k$ costs energy $\hbar\omega_k$; this is the **phonon energy quantum**.

态 $|n_{k_1}, n_{k_2}, \ldots\rangle$ 含有模式 $j$ 的 $n_{k_j}$ 个声子。增加一个模式 $k$ 的声子耗能 $\hbar\omega_k$；这就是**声子能量量子**。

**Step 5 — Thermal occupation.** Phonons are bosons (integer spin, and the ladder-operator algebra produces a symmetric Fock space — no Pauli exclusion). At temperature $T$, each mode is in thermal equilibrium with the bath, and the mean occupation is given by the **Bose–Einstein distribution**:

**第 5 步 — 热占据。** 声子是玻色子（整数自旋，且升降算符代数产生对称福克空间——无泡利不相容）。在温度 $T$ 下，每个模式与热浴平衡，平均占据数由**玻色–爱因斯坦分布**给出：

$$ \bar n_k = \langle \hat n_k\rangle = 1/(e^{\hbar\omega_k/k_B T} - 1). $$

This follows from the partition function $Z_k = \sum_{n=0}^\infty e^{-\beta\hbar\omega_k n} = 1/(1 - e^{-\beta\hbar\omega_k})$, giving $\langle \hat n_k\rangle = -\partial(\ln Z_k)/\partial(\beta\hbar\omega_k)$.

这由配分函数 $Z_k = \sum_{n=0}^\infty e^{-\beta\hbar\omega_k n} = 1/(1 - e^{-\beta\hbar\omega_k})$ 推出，给出 $\langle \hat n_k\rangle = -\partial(\ln Z_k)/\partial(\beta\hbar\omega_k)$。

**Step 6 — Mean energy per mode and connection to the Debye model.** The mean energy of mode $k$ (including zero-point energy) is

**第 6 步 — 每个模式的平均能量与德拜模型的联系。** 模式 $k$ 的平均能量（含零点能）为

$$ \langle E_k\rangle = \hbar\omega_k(\bar n_k + \tfrac12) = \hbar\omega_k/2 + \hbar\omega_k/(e^{\hbar\omega_k/k_B T} - 1). $$

Summing over all $k$ modes and replacing the sum by an integral using the density of states $D(\omega)$ recovers the Debye-model energy integral of Module 4.1 Section B. $\blacksquare$

对所有 $k$ 模式求和，并用态密度 $D(\omega)$ 将求和替换为积分，即恢复模块 4.1 B 节的德拜模型能量积分。$\blacksquare$

---

## D. Rigorous Counting: $3N$ Normal Modes for $N$ Atoms · 严格计数：$N$ 个原子有 $3N$ 个简正模

**Claim.** A crystal of $N$ unit cells each containing $p$ atoms has $3pN$ normal modes total: 3 acoustic branches (with $\omega \to 0$ as $k \to 0$) and $3(p-1)$ optical branches, each branch contributing $N$ modes.

**命题。** 含 $N$ 个原胞、每个原胞含 $p$ 个原子的晶体共有 $3pN$ 个简正模：3 支声学支（$k \to 0$ 时 $\omega \to 0$）和 $3(p-1)$ 支光学支，每支贡献 $N$ 个模式。

**Step 1 — Degrees of freedom.** The system has $Np$ atoms $\times$ 3 directions $= 3Np$ degrees of freedom. The dynamical matrix $D(k)$ is a $3p \times 3p$ Hermitian matrix for each $k$, giving $3p$ eigenfrequencies $\omega_s(k)$ ($s = 1\ldots 3p$). With $N$ allowed $k$-points, the total number of modes is $3pN$. $\blacksquare$

**第 1 步 — 自由度。** 系统有 $Np$ 个原子 $\times$ 3 个方向 $= 3Np$ 个自由度。对每个 $k$，动力学矩阵 $D(k)$ 是 $3p \times 3p$ 的厄米矩阵，给出 $3p$ 个本征频率 $\omega_s(k)$（$s = 1\ldots 3p$）。$N$ 个允许的 $k$ 点，总模式数为 $3pN$。$\blacksquare$

**Step 2 — Acoustic branches.** For $s = 1, 2, 3$ (acoustic), $\omega_s \to 0$ as $k \to 0$ because a uniform translation of all atoms ($k = 0$ acoustic mode) costs zero energy — it corresponds to a rigid-body translation with no restoring force. The remaining $3(p-1)$ branches are optical with $\omega_s(0) > 0$.

**第 2 步 — 声学支。** 对 $s = 1, 2, 3$（声学支），$k \to 0$ 时 $\omega_s \to 0$，因为所有原子整体平移（$k = 0$ 的声学模式）不消耗能量——它对应无恢复力的刚体平移。其余 $3(p-1)$ 支为光学支，$\omega_s(0) > 0$。

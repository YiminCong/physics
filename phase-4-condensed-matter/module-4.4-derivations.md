---
title: "Derivations — Module 4.4: Electrons in a Periodic Potential"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 4.4: Electrons in a Periodic Potential
# 推导 — 模块 4.4：周期势中的电子

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.4](./module-4.4-electrons-in-a-periodic-potential.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.4](./module-4.4-electrons-in-a-periodic-potential.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Bloch's Theorem · 布洛赫定理

**Claim.** For a Hamiltonian $H = -\hbar^2\nabla^2/2m + V(r)$ with $V(r)$ periodic under the Bravais lattice ($V(r+R) = V(r)$ for all lattice vectors $R$), every eigenstate can be written as

**命题。** 对哈密顿量 $H = -\hbar^2\nabla^2/2m + V(r)$，其中 $V(r)$ 在布拉伐格子下是周期性的（对所有格矢 $R$ 有 $V(r+R) = V(r)$），每个本征态可以写成

$$ \psi_k(r) = e^{ik\cdot r}\, u_k(r), $$

where $u_k(r+R) = u_k(r)$ is periodic with the lattice periodicity, and $k$ is a good quantum number lying in the first Brillouin zone.

其中 $u_k(r+R) = u_k(r)$ 具有晶格周期性，$k$ 是位于第一布里渊区内的好量子数。

**Step 1 — Define the lattice-translation operator.** For each lattice vector $R$ define the unitary translation operator $T_R$ by its action on any function:

**第 1 步 — 定义晶格平移算符。** 对每个格矢 $R$，定义酉平移算符 $T_R$ 对任意函数的作用：

$$ (T_R f)(r) = f(r + R). $$

$T_R$ is unitary because it preserves the $L^2$ norm: $\int|f(r+R)|^2 d^3r = \int|f(r)|^2 d^3r$.

$T_R$ 是酉算符，因为它保持 $L^2$ 范数：$\int|f(r+R)|^2 d^3r = \int|f(r)|^2 d^3r$。

**Step 2 — $T_R$ commutes with $H$.** We verify $[H, T_R] = 0$. Acting on any $\psi$:

**第 2 步 — $T_R$ 与 $H$ 对易。** 验证 $[H, T_R] = 0$。作用在任意 $\psi$ 上：

$$ \begin{aligned} (T_R H \psi)(r) &= (H\psi)(r+R) = [-\hbar^2\nabla^2_{r+R}/(2m) + V(r+R)]\, \psi(r+R) \\ &= [-\hbar^2\nabla^2_r/(2m) + V(r)]\, (T_R \psi)(r) = H(T_R \psi)(r). \end{aligned} $$

Here we used $V(r+R) = V(r)$ (periodicity) and $\nabla^2_{r+R} = \nabla^2_r$ (the Laplacian is translation-invariant). Therefore $T_R H = H T_R$, i.e., $[H, T_R] = 0$.

这里用到 $V(r+R) = V(r)$（周期性）和 $\nabla^2_{r+R} = \nabla^2_r$（拉普拉斯算符对平移不变）。因此 $T_R H = H T_R$，即 $[H, T_R] = 0$。

**Step 3 — $T_R$ operators form an abelian group.** For any two lattice vectors $R, R'$:

**第 3 步 — $T_R$ 算符构成阿贝尔群。** 对任意两个格矢 $R$、$R'$：

$$ T_R T_{R'} = T_{R+R'} = T_{R'} T_R. $$

The set $\{T_R\}$ forms a commutative (abelian) group under composition, isomorphic to the Bravais lattice as a group under addition.

集合 $\{T_R\}$ 在复合运算下构成交换（阿贝尔）群，同构于加法意义下的布拉伐格子群。

**Step 4 — Simultaneous eigenstates.** Since $[H, T_R] = 0$ for all $R$, and all $T_R$ commute with each other, $H$ and the full set $\{T_R\}$ share a common eigenbasis (by the theorem that commuting Hermitian/unitary operators can be simultaneously diagonalized — proved by constructing the common eigenspace decomposition). There exist states $\psi$ satisfying simultaneously

**第 4 步 — 共同本征态。** 由于对所有 $R$ 有 $[H, T_R] = 0$，且所有 $T_R$ 相互对易，$H$ 与完整集合 $\{T_R\}$ 共享公共本征基（由对易厄米/酉算符可同时对角化的定理——通过构造公共本征空间分解来证明）。存在态 $\psi$ 同时满足

$$ H \psi = E \psi \quad \text{and} \quad T_R \psi = c(R) \psi \quad \text{for all } R. $$

**Step 5 — Determine the eigenvalues $c(R)$.** The group homomorphism property $T_R T_{R'} = T_{R+R'}$ requires

**第 5 步 — 确定本征值 $c(R)$。** 群同态性质 $T_R T_{R'} = T_{R+R'}$ 要求

$$ c(R)\, c(R') = c(R+R'). $$

Since $T_R$ is unitary, its eigenvalues lie on the unit circle: $|c(R)| = 1$. The unique continuous functions $c:$ Bravais lattice $\to U(1)$ satisfying the homomorphism condition are

由于 $T_R$ 是酉算符，其本征值在单位圆上：$|c(R)| = 1$。满足同态条件的唯一连续函数 $c:$ 布拉伐格子 $\to U(1)$ 为

$$ c(R) = e^{ik\cdot R} $$

for some vector $k$. This is because writing $R = n_1 a_1 + n_2 a_2 + n_3 a_3$ and $c(a_i) = e^{i\kappa_i}$, the homomorphism condition forces $c(R) = e^{i(n_1\kappa_1+n_2\kappa_2+n_3\kappa_3)} = e^{ik\cdot R}$ with $k_j$ defined via the reciprocal basis.

对某个矢量 $k$。这是因为写 $R = n_1 a_1 + n_2 a_2 + n_3 a_3$，令 $c(a_i) = e^{i\kappa_i}$，同态条件迫使 $c(R) = e^{i(n_1\kappa_1+n_2\kappa_2+n_3\kappa_3)} = e^{ik\cdot R}$，其中 $k_j$ 通过倒格基矢定义。

**Step 6 — Bloch form.** Since $T_R \psi_k(r) = e^{ik\cdot R} \psi_k(r)$, we have $\psi_k(r+R) = e^{ik\cdot R} \psi_k(r)$. Define $u_k(r) = e^{-ik\cdot r} \psi_k(r)$; then

**第 6 步 — 布洛赫形式。** 由 $T_R \psi_k(r) = e^{ik\cdot R} \psi_k(r)$，有 $\psi_k(r+R) = e^{ik\cdot R} \psi_k(r)$。定义 $u_k(r) = e^{-ik\cdot r} \psi_k(r)$，则

$$ u_k(r+R) = e^{-ik\cdot(r+R)} \psi_k(r+R) = e^{-ik\cdot r} e^{-ik\cdot R} \cdot e^{ik\cdot R} \psi_k(r) = e^{-ik\cdot r} \psi_k(r) = u_k(r). $$

So $u_k$ is periodic with the lattice period, and

故 $u_k$ 具有晶格周期性，且

$$ \boxed{\, \psi_k(r) = e^{ik\cdot r}\, u_k(r) \,} \qquad \blacksquare $$

**Step 7 — $k$ restricted to the first BZ.** Any $k' = k + G$ ($G$ a reciprocal-lattice vector) gives the same Bloch eigenvalue $e^{ik'\cdot R} = e^{ik\cdot R} e^{iG\cdot R} = e^{ik\cdot R}$ (since $e^{iG\cdot R} = 1$). So $k$ and $k+G$ label the same translation eigenvalue. The independent values of $k$ are restricted to one primitive cell of the reciprocal lattice — the first Brillouin zone.

**第 7 步 — $k$ 限制在第一布里渊区。** 任何 $k' = k + G$（$G$ 为倒格矢）给出相同的布洛赫本征值 $e^{ik'\cdot R} = e^{ik\cdot R} e^{iG\cdot R} = e^{ik\cdot R}$（因 $e^{iG\cdot R} = 1$）。故 $k$ 与 $k+G$ 标记相同的平移本征值。$k$ 的独立值限制在倒格子的一个原胞内——即第一布里渊区。

---

## B. Nearly-Free-Electron Model: Band Gap $= 2|V_G|$ at the Zone Boundary · 近自由电子模型：区边界处能隙 $= 2|V_G|$

**Claim.** For a weak periodic potential $V(r) = \sum_G V_G e^{iG\cdot r}$, degenerate perturbation theory at the zone boundary $k = G/2$ gives two energy levels split by $2|V_G|$, opening a **band gap** of width $2|V_G|$.

**命题。** 对弱周期势 $V(r) = \sum_G V_G e^{iG\cdot r}$，在区边界 $k = G/2$ 处的简并微扰论给出两个能级，劈裂为 $2|V_G|$，打开宽度为 $2|V_G|$ 的**能隙**。

**Step 1 — Unperturbed problem.** Without the periodic potential ($V = 0$), eigenstates are free-electron plane waves $|k\rangle = e^{ik\cdot r}/\sqrt V$ with energies $E^0_k = \hbar^2 k^2/2m$.

**第 1 步 — 无微扰问题。** 没有周期势（$V = 0$）时，本征态为自由电子平面波 $|k\rangle = e^{ik\cdot r}/\sqrt V$，能量 $E^0_k = \hbar^2 k^2/2m$。

**Step 2 — Degeneracy at the zone boundary.** At the zone boundary (in 1D: $k = \pm\pi/a$, i.e. $k = G/2$ and $k-G = -G/2$), the two plane waves $|k\rangle$ and $|k-G\rangle$ are exactly degenerate:

**第 2 步 — 区边界处的简并。** 在区边界（一维：$k = \pm\pi/a$，即 $k = G/2$ 且 $k-G = -G/2$），两个平面波 $|k\rangle$ 和 $|k-G\rangle$ 恰好简并：

$$ E^0_{G/2} = \hbar^2(G/2)^2/2m = \hbar^2(-G/2)^2/2m = E^0_{G/2-G}. $$

**Step 3 — Matrix element of $V$.** The Fourier expansion $V(r) = \sum_{G'} V_{G'} e^{iG'\cdot r}$ gives the matrix element between the two degenerate states:

**第 3 步 — $V$ 的矩阵元。** 傅里叶展开 $V(r) = \sum_{G'} V_{G'} e^{iG'\cdot r}$ 给出两简并态之间的矩阵元：

$$ \begin{aligned} \langle k|V|k-G\rangle &= (1/V) \int e^{-ik\cdot r} \Big[\sum_{G'} V_{G'} e^{iG'\cdot r}\Big] e^{i(k-G)\cdot r}\, d^3r \\ &= \sum_{G'} V_{G'}\, (1/V) \int e^{i(G'-G)\cdot r}\, d^3r \\ &= \sum_{G'} V_{G'}\, \delta_{G',G} = V_G. \end{aligned} $$

(Only the $G' = G$ term survives the integral, by orthogonality of plane waves.) Similarly $\langle k-G|V|k\rangle = V_{-G} = V_G^*$ (since $V(r)$ is real, $V_{-G} = V_G^*$).

（由平面波的正交性，积分中只有 $G' = G$ 项存活。）类似地 $\langle k-G|V|k\rangle = V_{-G} = V_G^*$（因 $V(r)$ 为实函数，$V_{-G} = V_G^*$）。

**Step 4 — Degenerate perturbation theory.** Restrict to the two-dimensional degenerate subspace $\{|k\rangle, |k-G\rangle\}$. The effective $2\times 2$ Hamiltonian matrix is:

**第 4 步 — 简并微扰论。** 限制在二维简并子空间 $\{|k\rangle, |k-G\rangle\}$。有效 $2\times 2$ 哈密顿量矩阵为：

$$ H_{eff} = \begin{pmatrix} E^0 & V_G \\ V_G^* & E^0 \end{pmatrix}. $$

(Both diagonal elements equal $E^0$ at $k = G/2$ exactly.) The secular equation $\det(H_{eff} - EI) = 0$ gives:

（在 $k = G/2$ 处两个对角元精确相等为 $E^0$。）久期方程 $\det(H_{eff} - EI) = 0$ 给出：

$$ (E^0 - E)^2 - |V_G|^2 = 0, $$

so

故

$$ E = E^0 \pm |V_G|. $$

**Step 5 — The gap.** The two energy levels are $E_+ = E^0 + |V_G|$ and $E_- = E^0 - |V_G|$. The energy gap between them is

**第 5 步 — 能隙。** 两个能级为 $E_+ = E^0 + |V_G|$ 和 $E_- = E^0 - |V_G|$。两者之间的能隙为

$$ \boxed{\, \Delta E = 2|V_G| \,} $$

No electron states exist with energies in the range $(E^0 - |V_G|, E^0 + |V_G|)$. $\blacksquare$

在能量范围 $(E^0 - |V_G|, E^0 + |V_G|)$ 内不存在电子态。$\blacksquare$

**Step 6 — Eigenstates at the gap.** The two eigenstates are $(\pm 1/\sqrt 2)(|k\rangle \pm e^{i\varphi_G}|k-G\rangle)$ where $e^{i\varphi_G} = V_G/|V_G|$. In position space these are standing waves proportional to $\cos(Gx/2)$ (lower energy, density concentrated at potential minima) and $\sin(Gx/2)$ (upper energy, density concentrated at potential maxima) — showing how the potential redistributes charge to split the degeneracy.

**第 6 步 — 能隙处的本征态。** 两个本征态为 $(\pm 1/\sqrt 2)(|k\rangle \pm e^{i\varphi_G}|k-G\rangle)$，其中 $e^{i\varphi_G} = V_G/|V_G|$。在坐标空间中，这些是正比于 $\cos(Gx/2)$（低能态，密度集中在势能极小值处）和 $\sin(Gx/2)$（高能态，密度集中在势能极大值处）的驻波——展示了势如何重新分布电荷以劈裂简并。

---

## C. Tight-Binding Band $E(k) = E_0 - 2t\cos(ka)$ in 1D · 一维紧束缚能带

**Claim.** For a 1D lattice of atoms with on-site energy $E_0$ and nearest-neighbour hopping amplitude $t$, the band dispersion is $E(k) = E_0 - 2t\cos(ka)$.

**命题。** 对具有在位能 $E_0$ 和最近邻跃迁振幅 $t$ 的一维原子格子，能带色散为 $E(k) = E_0 - 2t\cos(ka)$。

**Step 1 — Basis and ansatz.** Let $|n\rangle$ denote the atomic orbital (Wannier function) centred at site $n$. The tight-binding Hamiltonian is

**第 1 步 — 基矢与拟设。** 令 $|n\rangle$ 表示以格点 $n$ 为中心的原子轨道（万尼尔函数）。紧束缚哈密顿量为

$$ H = E_0 \sum_n |n\rangle\langle n| - t \sum_n (|n\rangle\langle n+1| + |n+1\rangle\langle n|). $$

The first term gives the atomic energy; the second describes hopping between adjacent sites ($t > 0$ by convention).

第一项给出原子能量；第二项描述相邻格点间的跃迁（约定 $t > 0$）。

**Step 2 — Bloch state ansatz.** By Bloch's theorem the eigenstates take the form

**第 2 步 — 布洛赫态拟设。** 由布洛赫定理，本征态取形式

$$ |k\rangle = (1/\sqrt N) \sum_n e^{ikna} |n\rangle. $$

This is a superposition of all site orbitals with phase factors $e^{ikna}$ consistent with the lattice periodicity.

这是所有格点轨道的叠加，相位因子 $e^{ikna}$ 与晶格周期性相符。

**Step 3 — Compute $\langle k|H|k\rangle$.** The on-site term:

**第 3 步 — 计算 $\langle k|H|k\rangle$。** 在位项：

$$ \langle k|E_0\textstyle\sum_n|n\rangle\langle n||k\rangle = E_0\, (1/N) \sum_{n,m} e^{i(m-n)ka} \langle m|n\rangle = E_0\, (1/N) \sum_{n,m} e^{i(m-n)ka} \delta_{mn} = E_0. $$

The hopping term:

跃迁项：

$$ \langle k|(-t)\textstyle\sum_n(|n\rangle\langle n+1|+\text{h.c.})|k\rangle = (-t)(1/N) \sum_{n,m} e^{i(m-n)ka}[\langle m|n\rangle\langle n+1|k\text{-basis}\rangle + \text{h.c.}] $$

More directly: apply $H$ to $|k\rangle$ and use $\langle k|H|k\rangle$:

更直接地：将 $H$ 作用在 $|k\rangle$ 上并利用 $\langle k|H|k\rangle$：

$$ H|k\rangle = E_0|k\rangle - (t/\sqrt N) \sum_n e^{ikna}(|n-1\rangle + |n+1\rangle). $$

Reindex each sum so the kets become $|n\rangle$ (shift $n\mp 1 \to n$), which collects the coefficient of each $|n\rangle$:

对每个求和重新编号使右矢变为 $|n\rangle$（移位 $n\mp 1 \to n$），收集每个 $|n\rangle$ 的系数：

$$ H|k\rangle = (1/\sqrt N) \sum_n [E_0 - t(e^{ika} + e^{-ika})]\, e^{ikna} |n\rangle = [E_0 - 2t\cos(ka)]\, |k\rangle. $$

**Step 4 — Read off the energy.**

**第 4 步 — 读出能量。**

$$ \boxed{\, E(k) = E_0 - 2t\cos(ka) \,} \qquad \blacksquare $$

**Step 5 — Properties of the band.** The bandwidth is $4t$ (from $E_0 - 2t$ at $k = 0$ to $E_0 + 2t$ at $k = \pi/a$). The minimum energy is at $k = 0$ (bottom of band, bonding character: all phases aligned) and the maximum at $k = \pi/a$ (top of band, antibonding character: alternating phases). For $t > 0$ the band has an inverted cosine shape. The effective mass at the band bottom is $m^* = \hbar^2/(2ta^2)$ (from expanding $E(k) \approx E_0 - 2t + ta^2 k^2$ for small $k$). Narrower bands (smaller $t$, more localized orbitals) give heavier effective masses.

**第 5 步 — 能带性质。** 带宽为 $4t$（从 $k = 0$ 处的 $E_0 - 2t$ 到 $k = \pi/a$ 处的 $E_0 + 2t$）。最低能量在 $k = 0$（带底，成键特性：所有相位对齐），最高能量在 $k = \pi/a$（带顶，反键特性：相位交替）。对 $t > 0$，能带呈倒余弦形状。带底有效质量 $m^* = \hbar^2/(2ta^2)$（对小 $k$ 展开 $E(k) \approx E_0 - 2t + ta^2 k^2$）。能带越窄（$t$ 越小，轨道越局域化），有效质量越大。

---

## D. Hermiticity and Completeness for Bloch Hamiltonians · 布洛赫哈密顿量的厄米性与完备性

**The reduced Hamiltonian.** Substituting the Bloch ansatz into $H\psi_k = E_k \psi_k$ gives the reduced ($k$-dependent) Hamiltonian

**约化哈密顿量。** 将布洛赫拟设代入 $H\psi_k = E_k \psi_k$ 给出约化（依赖 $k$ 的）哈密顿量

$$ H_k = e^{-ik\cdot r} H e^{ik\cdot r} = (\hbar^2/2m)(-i\nabla + k)^2 + V(r), $$

acting on periodic functions $u_k(r)$. $H_k$ is Hermitian on the space of periodic $L^2$ functions with the same lattice periodicity. For each $k$, $H_k$ has a discrete spectrum $E_n(k)$ ($n = 1, 2, \ldots,$ the band index) because the periodic boundary condition restricts $r$ to a compact domain. By the spectral theorem for compact-domain self-adjoint operators, the eigenfunctions $\{u_{n,k}\}$ form a complete orthonormal basis. The full Bloch states $\{\psi_{n,k} = e^{ik\cdot r}u_{n,k}\}$ then provide a complete basis for the single-particle Hilbert space. $\blacksquare$

作用在周期函数 $u_k(r)$ 上。$H_k$ 在具有相同晶格周期性的周期性 $L^2$ 函数空间上是厄米的。对每个 $k$，$H_k$ 有离散谱 $E_n(k)$（$n = 1, 2, \ldots$，能带指标），因为周期性边界条件将 $r$ 限制在紧致区域。由紧致区域自伴算符的谱定理，本征函数 $\{u_{n,k}\}$ 构成完备正交基。完整布洛赫态 $\{\psi_{n,k} = e^{ik\cdot r}u_{n,k}\}$ 构成单粒子希尔伯特空间的完备基。$\blacksquare$

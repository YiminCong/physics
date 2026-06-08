# Derivations — Module 4.4: Electrons in a Periodic Potential
# 推导 — 模块 4.4：周期势中的电子

> Companion to [Module 4.4](./module-4.4-electrons-in-a-periodic-potential.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.4](./module-4.4-electrons-in-a-periodic-potential.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Bloch's Theorem · 布洛赫定理

**Claim.** For a Hamiltonian H = −ℏ²∇²/2m + V(r) with V(r) periodic under the Bravais lattice (V(r+R) = V(r) for all lattice vectors R), every eigenstate can be written as

**命题。** 对哈密顿量 H = −ℏ²∇²/2m + V(r)，其中 V(r) 在布拉伐格子下是周期性的（对所有格矢 R 有 V(r+R) = V(r)），每个本征态可以写成

  ψ_k(r) = e^{ik·r} u_k(r),

where u_k(r+R) = u_k(r) is periodic with the lattice periodicity, and k is a good quantum number lying in the first Brillouin zone.

其中 u_k(r+R) = u_k(r) 具有晶格周期性，k 是位于第一布里渊区内的好量子数。

**Step 1 — Define the lattice-translation operator.** For each lattice vector R define the unitary translation operator T_R by its action on any function:

**第 1 步 — 定义晶格平移算符。** 对每个格矢 R，定义酉平移算符 T_R 对任意函数的作用：

  (T_R f)(r) = f(r + R).

T_R is unitary because it preserves the L² norm: ∫|f(r+R)|²d³r = ∫|f(r)|²d³r.

T_R 是酉算符，因为它保持 L² 范数：∫|f(r+R)|²d³r = ∫|f(r)|²d³r。

**Step 2 — T_R commutes with H.** We verify [H, T_R] = 0. Acting on any ψ:

**第 2 步 — T_R 与 H 对易。** 验证 [H, T_R] = 0。作用在任意 ψ 上：

  (T_R H ψ)(r) = (Hψ)(r+R) = [−ℏ²∇²_{r+R}/(2m) + V(r+R)] ψ(r+R)
               = [−ℏ²∇²_r/(2m) + V(r)] (T_R ψ)(r) = H(T_R ψ)(r).

Here we used V(r+R) = V(r) (periodicity) and ∇²_{r+R} = ∇²_r (the Laplacian is translation-invariant). Therefore T_R H = H T_R, i.e., **[H, T_R] = 0**.

这里用到 V(r+R) = V(r)（周期性）和 ∇²_{r+R} = ∇²_r（拉普拉斯算符对平移不变）。因此 T_R H = H T_R，即 **[H, T_R] = 0**。

**Step 3 — T_R operators form an abelian group.** For any two lattice vectors R, R′:

**第 3 步 — T_R 算符构成阿贝尔群。** 对任意两个格矢 R、R′：

  T_R T_{R′} = T_{R+R′} = T_{R′} T_R.

The set {T_R} forms a commutative (abelian) group under composition, isomorphic to the Bravais lattice as a group under addition.

集合 {T_R} 在复合运算下构成交换（阿贝尔）群，同构于加法意义下的布拉伐格子群。

**Step 4 — Simultaneous eigenstates.** Since [H, T_R] = 0 for all R, and all T_R commute with each other, H and the full set {T_R} share a common eigenbasis (by the theorem that commuting Hermitian/unitary operators can be simultaneously diagonalized — proved by constructing the common eigenspace decomposition). There exist states ψ satisfying simultaneously

**第 4 步 — 共同本征态。** 由于对所有 R 有 [H, T_R] = 0，且所有 T_R 相互对易，H 与完整集合 {T_R} 共享公共本征基（由对易厄米/酉算符可同时对角化的定理——通过构造公共本征空间分解来证明）。存在态 ψ 同时满足

  H ψ = E ψ   and   T_R ψ = c(R) ψ   for all R.

**Step 5 — Determine the eigenvalues c(R).** The group homomorphism property T_R T_{R′} = T_{R+R′} requires

**第 5 步 — 确定本征值 c(R)。** 群同态性质 T_R T_{R′} = T_{R+R′} 要求

  c(R) c(R′) = c(R+R′).

Since T_R is unitary, its eigenvalues lie on the unit circle: |c(R)| = 1. The unique continuous functions c: Bravais lattice → U(1) satisfying the homomorphism condition are

由于 T_R 是酉算符，其本征值在单位圆上：|c(R)| = 1。满足同态条件的唯一连续函数 c: 布拉伐格子 → U(1) 为

  c(R) = e^{ik·R}

for some vector k. This is because writing R = n₁a₁ + n₂a₂ + n₃a₃ and c(aᵢ) = e^{iκᵢ}, the homomorphism condition forces c(R) = e^{i(n₁κ₁+n₂κ₂+n₃κ₃)} = e^{ik·R} with kⱼ defined via the reciprocal basis.

对某个矢量 k。这是因为写 R = n₁a₁ + n₂a₂ + n₃a₃，令 c(aᵢ) = e^{iκᵢ}，同态条件迫使 c(R) = e^{i(n₁κ₁+n₂κ₂+n₃κ₃)} = e^{ik·R}，其中 kⱼ 通过倒格基矢定义。

**Step 6 — Bloch form.** Since T_R ψ_k(r) = e^{ik·R} ψ_k(r), we have ψ_k(r+R) = e^{ik·R} ψ_k(r). Define u_k(r) = e^{−ik·r} ψ_k(r); then

**第 6 步 — 布洛赫形式。** 由 T_R ψ_k(r) = e^{ik·R} ψ_k(r)，有 ψ_k(r+R) = e^{ik·R} ψ_k(r)。定义 u_k(r) = e^{−ik·r} ψ_k(r)，则

  u_k(r+R) = e^{−ik·(r+R)} ψ_k(r+R) = e^{−ik·r} e^{−ik·R} · e^{ik·R} ψ_k(r) = e^{−ik·r} ψ_k(r) = u_k(r).

So u_k is periodic with the lattice period, and

故 u_k 具有晶格周期性，且

  **ψ_k(r) = e^{ik·r} u_k(r)**.  ∎

**Step 7 — k restricted to the first BZ.** Any k′ = k + G (G a reciprocal-lattice vector) gives the same Bloch eigenvalue e^{ik′·R} = e^{ik·R} e^{iG·R} = e^{ik·R} (since e^{iG·R} = 1). So k and k+G label the same translation eigenvalue. The independent values of k are restricted to one primitive cell of the reciprocal lattice — the first Brillouin zone.

**第 7 步 — k 限制在第一布里渊区。** 任何 k′ = k + G（G 为倒格矢）给出相同的布洛赫本征值 e^{ik′·R} = e^{ik·R} e^{iG·R} = e^{ik·R}（因 e^{iG·R} = 1）。故 k 与 k+G 标记相同的平移本征值。k 的独立值限制在倒格子的一个原胞内——即第一布里渊区。

---

## B. Nearly-Free-Electron Model: Band Gap = 2|V_G| at the Zone Boundary · 近自由电子模型：区边界处能隙 = 2|V_G|

**Claim.** For a weak periodic potential V(r) = Σ_G V_G e^{iG·r}, degenerate perturbation theory at the zone boundary k = G/2 gives two energy levels split by 2|V_G|, opening a **band gap** of width 2|V_G|.

**命题。** 对弱周期势 V(r) = Σ_G V_G e^{iG·r}，在区边界 k = G/2 处的简并微扰论给出两个能级，劈裂为 2|V_G|，打开宽度为 2|V_G| 的**能隙**。

**Step 1 — Unperturbed problem.** Without the periodic potential (V = 0), eigenstates are free-electron plane waves |k⟩ = e^{ik·r}/√V with energies E⁰_k = ℏ²k²/2m.

**第 1 步 — 无微扰问题。** 没有周期势（V = 0）时，本征态为自由电子平面波 |k⟩ = e^{ik·r}/√V，能量 E⁰_k = ℏ²k²/2m。

**Step 2 — Degeneracy at the zone boundary.** At the zone boundary (in 1D: k = ±π/a, i.e. k = G/2 and k−G = −G/2), the two plane waves |k⟩ and |k−G⟩ are exactly degenerate:

**第 2 步 — 区边界处的简并。** 在区边界（一维：k = ±π/a，即 k = G/2 且 k−G = −G/2），两个平面波 |k⟩ 和 |k−G⟩ 恰好简并：

  E⁰_{G/2} = ℏ²(G/2)²/2m = ℏ²(−G/2)²/2m = E⁰_{G/2−G}.

**Step 3 — Matrix element of V.** The Fourier expansion V(r) = Σ_{G′} V_{G′} e^{iG′·r} gives the matrix element between the two degenerate states:

**第 3 步 — V 的矩阵元。** 傅里叶展开 V(r) = Σ_{G′} V_{G′} e^{iG′·r} 给出两简并态之间的矩阵元：

  ⟨k|V|k−G⟩ = (1/V) ∫ e^{−ik·r} [Σ_{G′} V_{G′} e^{iG′·r}] e^{i(k−G)·r} d³r
              = Σ_{G′} V_{G′} (1/V) ∫ e^{i(G′−G)·r} d³r
              = Σ_{G′} V_{G′} δ_{G′,G} = V_G.

(Only the G′ = G term survives the integral, by orthogonality of plane waves.) Similarly ⟨k−G|V|k⟩ = V_{−G} = V_G* (since V(r) is real, V_{−G} = V_G*).

（由平面波的正交性，积分中只有 G′ = G 项存活。）类似地 ⟨k−G|V|k⟩ = V_{−G} = V_G*（因 V(r) 为实函数，V_{−G} = V_G*）。

**Step 4 — Degenerate perturbation theory.** Restrict to the two-dimensional degenerate subspace {|k⟩, |k−G⟩}. The effective 2×2 Hamiltonian matrix is:

**第 4 步 — 简并微扰论。** 限制在二维简并子空间 {|k⟩, |k−G⟩}。有效 2×2 哈密顿量矩阵为：

  H_eff = | E⁰   V_G  |
          | V_G*  E⁰  |.

(Both diagonal elements equal E⁰ at k = G/2 exactly.) The secular equation det(H_eff − EI) = 0 gives:

（在 k = G/2 处两个对角元精确相等为 E⁰。）久期方程 det(H_eff − EI) = 0 给出：

  (E⁰ − E)² − |V_G|² = 0,

so

故

  E = E⁰ ± |V_G|.

**Step 5 — The gap.** The two energy levels are E₊ = E⁰ + |V_G| and E₋ = E⁰ − |V_G|. The energy gap between them is

**第 5 步 — 能隙。** 两个能级为 E₊ = E⁰ + |V_G| 和 E₋ = E⁰ − |V_G|。两者之间的能隙为

  **ΔE = 2|V_G|**.

No electron states exist with energies in the range (E⁰ − |V_G|, E⁰ + |V_G|). ∎

在能量范围 (E⁰ − |V_G|, E⁰ + |V_G|) 内不存在电子态。∎

**Step 6 — Eigenstates at the gap.** The two eigenstates are (±1/√2)(|k⟩ ± e^{iφ_G}|k−G⟩) where e^{iφ_G} = V_G/|V_G|. In position space these are standing waves proportional to cos(Gx/2) (lower energy, density concentrated at potential minima) and sin(Gx/2) (upper energy, density concentrated at potential maxima) — showing how the potential redistributes charge to split the degeneracy.

**第 6 步 — 能隙处的本征态。** 两个本征态为 (±1/√2)(|k⟩ ± e^{iφ_G}|k−G⟩)，其中 e^{iφ_G} = V_G/|V_G|。在坐标空间中，这些是正比于 cos(Gx/2)（低能态，密度集中在势能极小值处）和 sin(Gx/2)（高能态，密度集中在势能极大值处）的驻波——展示了势如何重新分布电荷以劈裂简并。

---

## C. Tight-Binding Band E(k) = E₀ − 2t cos(ka) in 1D · 一维紧束缚能带

**Claim.** For a 1D lattice of atoms with on-site energy E₀ and nearest-neighbour hopping amplitude t, the band dispersion is E(k) = E₀ − 2t cos(ka).

**命题。** 对具有在位能 E₀ 和最近邻跃迁振幅 t 的一维原子格子，能带色散为 E(k) = E₀ − 2t cos(ka)。

**Step 1 — Basis and ansatz.** Let |n⟩ denote the atomic orbital (Wannier function) centred at site n. The tight-binding Hamiltonian is

**第 1 步 — 基矢与拟设。** 令 |n⟩ 表示以格点 n 为中心的原子轨道（万尼尔函数）。紧束缚哈密顿量为

  H = E₀ Σ_n |n⟩⟨n| − t Σ_n (|n⟩⟨n+1| + |n+1⟩⟨n|).

The first term gives the atomic energy; the second describes hopping between adjacent sites (t > 0 by convention).

第一项给出原子能量；第二项描述相邻格点间的跃迁（约定 t > 0）。

**Step 2 — Bloch state ansatz.** By Bloch's theorem the eigenstates take the form

**第 2 步 — 布洛赫态拟设。** 由布洛赫定理，本征态取形式

  |k⟩ = (1/√N) Σ_n e^{ikna} |n⟩.

This is a superposition of all site orbitals with phase factors e^{ikna} consistent with the lattice periodicity.

这是所有格点轨道的叠加，相位因子 e^{ikna} 与晶格周期性相符。

**Step 3 — Compute ⟨k|H|k⟩.** The on-site term:

**第 3 步 — 计算 ⟨k|H|k⟩。** 在位项：

  ⟨k|E₀Σ_n|n⟩⟨n||k⟩ = E₀ (1/N) Σ_{n,m} e^{i(m−n)ka} ⟨m|n⟩ = E₀ (1/N) Σ_{n,m} e^{i(m−n)ka} δ_{mn} = E₀.

The hopping term:

跃迁项：

  ⟨k|(−t)Σ_n(|n⟩⟨n+1|+h.c.)|k⟩ = (−t)(1/N) Σ_{n,m} e^{i(m−n)ka}[⟨m|n⟩⟨n+1|k-basis⟩ + h.c.]

More directly: apply H to |k⟩ and use ⟨k|H|k⟩:

更直接地：将 H 作用在 |k⟩ 上并利用 ⟨k|H|k⟩：

  H|k⟩ = E₀|k⟩ − (t/√N) Σ_n e^{ikna}(|n−1⟩ + |n+1⟩)
        = E₀|k⟩ − (t/√N) Σ_n e^{ikna}(e^{−ika} + e^{ika})|n⟩ · (reindexing)

Wait — more carefully: collecting the |n⟩ coefficient:

仔细整理 |n⟩ 的系数：

  H|k⟩ = (1/√N) Σ_n [E₀ − t(e^{ika} + e^{−ika})] e^{ikna} |n⟩ = [E₀ − 2t cos(ka)] |k⟩.

**Step 4 — Read off the energy.**

**第 4 步 — 读出能量。**

  **E(k) = E₀ − 2t cos(ka)**.  ∎

**Step 5 — Properties of the band.** The bandwidth is 4t (from E₀ − 2t at k = 0 to E₀ + 2t at k = π/a). The minimum energy is at k = 0 (bottom of band, bonding character: all phases aligned) and the maximum at k = π/a (top of band, antibonding character: alternating phases). For t > 0 the band has an inverted cosine shape. The effective mass at the band bottom is m* = ℏ²/(2ta²) (from expanding E(k) ≈ E₀ − 2t + ta²k² for small k). Narrower bands (smaller t, more localized orbitals) give heavier effective masses.

**第 5 步 — 能带性质。** 带宽为 4t（从 k = 0 处的 E₀ − 2t 到 k = π/a 处的 E₀ + 2t）。最低能量在 k = 0（带底，成键特性：所有相位对齐），最高能量在 k = π/a（带顶，反键特性：相位交替）。对 t > 0，能带呈倒余弦形状。带底有效质量 m* = ℏ²/(2ta²)（对小 k 展开 E(k) ≈ E₀ − 2t + ta²k²）。能带越窄（t 越小，轨道越局域化），有效质量越大。

---

## D. Hermiticity and Completeness for Bloch Hamiltonians · 布洛赫哈密顿量的厄米性与完备性

**The reduced Hamiltonian.** Substituting the Bloch ansatz into Hψ_k = E_k ψ_k gives the reduced (k-dependent) Hamiltonian

**约化哈密顿量。** 将布洛赫拟设代入 Hψ_k = E_k ψ_k 给出约化（依赖 k 的）哈密顿量

  H_k = e^{−ik·r} H e^{ik·r} = (ℏ²/2m)(−i∇ + k)² + V(r),

acting on periodic functions u_k(r). H_k is Hermitian on the space of periodic L² functions with the same lattice periodicity. For each k, H_k has a discrete spectrum E_n(k) (n = 1, 2, …, the band index) because the periodic boundary condition restricts r to a compact domain. By the spectral theorem for compact-domain self-adjoint operators, the eigenfunctions {u_{n,k}} form a complete orthonormal basis. The full Bloch states {ψ_{n,k} = e^{ik·r}u_{n,k}} then provide a complete basis for the single-particle Hilbert space. ∎

作用在周期函数 u_k(r) 上。H_k 在具有相同晶格周期性的周期性 L² 函数空间上是厄米的。对每个 k，H_k 有离散谱 E_n(k)（n = 1, 2, …，能带指标），因为周期性边界条件将 r 限制在紧致区域。由紧致区域自伴算符的谱定理，本征函数 {u_{n,k}} 构成完备正交基。完整布洛赫态 {ψ_{n,k} = e^{ik·r}u_{n,k}} 构成单粒子希尔伯特空间的完备基。∎

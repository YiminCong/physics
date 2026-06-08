# Derivations — Module 4.3: Lattice Vibrations & Phonons
# 推导 — 模块 4.3：晶格振动与声子

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.3](./module-4.3-lattice-vibrations-and-phonons.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.3](./module-4.3-lattice-vibrations-and-phonons.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Monatomic 1D Chain Dispersion ω(k) = 2√(K/M)|sin(ka/2)| · 单原子一维链色散关系

**Claim.** For a 1D chain of identical atoms of mass M connected by springs of constant K with equilibrium spacing a, the normal-mode dispersion is ω(k) = 2√(K/M)|sin(ka/2)|, with k ∈ (−π/a, π/a] (first Brillouin zone).

**命题。** 对质量为 M、平衡间距为 a、弹簧常数为 K 的一维单原子链，简正模色散关系为 ω(k) = 2√(K/M)|sin(ka/2)|，k ∈ (−π/a, π/a]（第一布里渊区）。

**Step 1 — Set up the equation of motion.** Label atoms by integer n; let u_n be the displacement from equilibrium. In the nearest-neighbour approximation, the force on atom n comes from its two neighbours:

**第 1 步 — 建立运动方程。** 用整数 n 标记原子；u_n 为偏离平衡位置的位移。在最近邻近似下，作用在第 n 个原子上的力来自其两侧邻居：

  M ü_n = K(u_{n+1} − u_n) + K(u_{n-1} − u_n) = K(u_{n+1} + u_{n-1} − 2u_n).

This is Newton's second law applied to a harmonic chain. Each atom feels a restoring force proportional to the relative displacement from its neighbours.

这是对谐振子链应用牛顿第二定律。每个原子受到正比于其与邻居相对位移的恢复力。

**Step 2 — Plane-wave ansatz.** Try a travelling-wave solution of the form

**第 2 步 — 平面波拟设。** 尝试行波解

  u_n(t) = A e^{i(kna − ωt)},

where k is the wavevector and ω is the angular frequency to be determined. This ansatz respects the discrete translational symmetry of the chain.

其中 k 为波矢，ω 为待定角频率。此拟设尊重链的离散平移对称性。

**Step 3 — Substitute into the equation of motion.** Inserting u_n = A e^{i(kna−ωt)} into M ü_n = K(u_{n+1} + u_{n-1} − 2u_n):

**第 3 步 — 代入运动方程。** 将 u_n = A e^{i(kna−ωt)} 代入 M ü_n = K(u_{n+1} + u_{n-1} − 2u_n)：

  M(−ω²) A e^{i(kna−ωt)} = K A e^{i(kna−ωt)} [e^{ika} + e^{−ika} − 2].

Dividing both sides by A e^{i(kna−ωt)} ≠ 0:

两边除以 A e^{i(kna−ωt)} ≠ 0：

  −Mω² = K(e^{ika} + e^{−ika} − 2) = K(2cos(ka) − 2) = −4K sin²(ka/2).

Here we used e^{ika} + e^{−ika} = 2cos(ka) and 1 − cos(ka) = 2sin²(ka/2).

这里用到 e^{ika} + e^{−ika} = 2cos(ka) 以及 1 − cos(ka) = 2sin²(ka/2)。

**Step 4 — Solve for ω(k).**

**第 4 步 — 求解 ω(k)。**

  ω² = (4K/M) sin²(ka/2).

Taking the positive square root (physical frequencies ω ≥ 0):

取正平方根（物理频率 ω ≥ 0）：

  **ω(k) = 2√(K/M) |sin(ka/2)|**.

**Step 5 — First Brillouin zone and periodicity.** The dispersion is periodic: ω(k + 2π/a) = ω(k). Values of k differing by 2π/a describe the same physical mode (they produce identical displacements on all atoms). The independent modes are therefore restricted to the first Brillouin zone k ∈ (−π/a, π/a], which contains exactly N modes for a chain of N atoms with periodic boundary conditions. ∎

**第 5 步 — 第一布里渊区与周期性。** 色散关系是周期性的：ω(k + 2π/a) = ω(k)。相差 2π/a 的 k 值描述相同的物理模式（它们在所有原子上产生相同位移）。因此独立模式限制在第一布里渊区 k ∈ (−π/a, π/a]，对于周期性边界条件下 N 个原子的链，恰好包含 N 个模式。∎

**Step 6 — Physical limits.** (i) Long-wavelength (acoustic) limit ka ≪ 1: sin(ka/2) ≈ ka/2, so ω ≈ √(K/M) · ka — linear dispersion, with sound velocity v_s = a√(K/M). (ii) Zone-boundary k = π/a: ω_max = 2√(K/M) — the maximum frequency, corresponding to neighbouring atoms oscillating out of phase. (iii) Group velocity v_g = dω/dk = a√(K/M) cos(ka/2) → 0 at the zone boundary, indicating a standing wave.

**第 6 步 — 物理极限。** (i) 长波（声学）极限 ka ≪ 1：sin(ka/2) ≈ ka/2，故 ω ≈ √(K/M) · ka——线性色散，声速 v_s = a√(K/M)。(ii) 区边界 k = π/a：ω_max = 2√(K/M)——最大频率，对应相邻原子反相振荡。(iii) 群速度 v_g = dω/dk = a√(K/M) cos(ka/2)，在区边界趋于零，表明此处为驻波。

---

## B. Diatomic Chain: Acoustic and Optical Branches · 双原子链：声学支与光学支

**Claim.** A 1D diatomic chain with masses M₁, M₂ (M₁ > M₂) and spring constant K has two branches: an **acoustic branch** ω_− → 0 as k → 0 and an **optical branch** ω_+ → √(2K/μ) at k = 0, where μ = M₁M₂/(M₁+M₂) is the reduced mass. A frequency gap opens at the zone boundary.

**命题。** 质量为 M₁、M₂（M₁ > M₂）、弹簧常数为 K 的一维双原子链有两支：**声学支** ω_− → 0（k → 0），和**光学支** ω_+ → √(2K/μ)（k = 0），其中 μ = M₁M₂/(M₁+M₂) 为约化质量。在区边界处打开频率隙。

**Step 1 — Equations of motion.** Label the unit cell by index n with atoms of mass M₁ at position na (displacement u_n) and M₂ at na + d (displacement v_n):

**第 1 步 — 运动方程。** 用指数 n 标记原胞：质量 M₁ 的原子在位置 na（位移 u_n），质量 M₂ 的原子在 na + d（位移 v_n）：

  M₁ ü_n = K(v_n − u_n) + K(v_{n-1} − u_n) = K(v_n + v_{n-1} − 2u_n),
  M₂ v̈_n = K(u_{n+1} − v_n) + K(u_n − v_n) = K(u_{n+1} + u_n − 2v_n).

**Step 2 — Plane-wave ansatz.** Try

**第 2 步 — 平面波拟设。** 尝试

  u_n = U e^{i(kna−ωt)},   v_n = V e^{i(kna−ωt)}.

Substituting:

代入得：

  −M₁ω² U = K V(1 + e^{−ika}) − 2KU,
  −M₂ω² V = K U(e^{ika} + 1) − 2KV.

**Step 3 — Matrix eigenvalue problem.** Rewriting in matrix form:

**第 3 步 — 矩阵本征值问题。** 改写为矩阵形式：

  | 2K − M₁ω²      −K(1+e^{−ika}) | | U |   | 0 |
  | −K(1+e^{ika})   2K − M₂ω²     | | V | = | 0 |.

For non-trivial solutions the determinant must vanish:

要有非平凡解，行列式须为零：

  (2K − M₁ω²)(2K − M₂ω²) − K²|1 + e^{ika}|² = 0.

Note |1 + e^{ika}|² = (1+cos(ka))·2 = 4cos²(ka/2).

注意 |1 + e^{ika}|² = 2(1 + cos(ka)) = 4cos²(ka/2)。

**Step 4 — Solve the secular equation.** Expanding:

**第 4 步 — 求解久期方程。** 展开：

  M₁M₂ ω⁴ − 2K(M₁+M₂)ω² + 4K²[1 − cos²(ka/2)] = 0
  M₁M₂ ω⁴ − 2K(M₁+M₂)ω² + 4K² sin²(ka/2) = 0.

Using the quadratic formula with respect to ω²:

对 ω² 用求根公式：

  ω² = K(M₁+M₂)/(M₁M₂) ± K√[(M₁+M₂)²/(M₁M₂)² − 4sin²(ka/2)/(M₁M₂)].

**Step 5 — Two branches.** The ± sign gives two solutions:

**第 5 步 — 两支解。** ± 号给出两个解：

  ω_±² = (K/μ_r)[1 ± √(1 − 4μ_r²sin²(ka/2)/M₁M₂)],

where μ_r = M₁M₂/(M₁+M₂) is the reduced mass and we used M₁M₂/(M₁+M₂) = μ_r. More explicitly:

其中 μ_r = M₁M₂/(M₁+M₂) 为约化质量。更明确地：

  ω²_± = K(M₁+M₂)/(M₁M₂) ± K√{[(M₁+M₂)/(M₁M₂)]² − 4sin²(ka/2)/(M₁M₂)}.

**Step 6 — k = 0 limit.** At k = 0, sin(ka/2) = 0:

**第 6 步 — k = 0 极限。** 在 k = 0 处，sin(ka/2) = 0：

  ω_−²(0) = 0   (acoustic branch, both atoms move in phase),
  ω_+²(0) = 2K(M₁+M₂)/(M₁M₂) = 2K/μ_r   (optical branch, atoms move out of phase).

The acoustic branch has a linear dispersion ω_− ≈ vₛ k near k = 0 (sound wave). The optical branch has a finite frequency at k = 0 and can be excited by light whose electric field drives the oppositely-charged sub-lattices against each other — hence "optical".

声学支在 k = 0 附近有线性色散 ω_− ≈ vₛ k（声波）。光学支在 k = 0 处有有限频率，可被光的电场激发（光场驱动带异号电荷的子格子相向运动）——故称"光学"支。

**Step 7 — Zone-boundary gap.** At k = π/a:

**第 7 步 — 区边界频率隙。** 在 k = π/a 处：

  ω²_+(π/a) = 2K/M₂,   ω²_−(π/a) = 2K/M₁.

The frequency gap between the two branches is

两支之间的频率隙为

  Δω = √(2K/M₂) − √(2K/M₁) > 0   (since M₁ > M₂).

No modes exist in this gap; it represents a phononic band gap. ∎

此隙内无模式存在，即声子带隙。∎

---

## C. Quantization of a Normal Mode: Phonons · 简正模的量子化：声子

**Claim.** Each normal mode of the lattice is equivalent to a harmonic oscillator with frequency ω_k. Quantizing it yields **phonons**: quanta of lattice vibration with energy ℏω_k, zero-point energy ½ℏω_k, and Bose–Einstein occupation number n̄_k = 1/(e^{ℏω_k/k_BT} − 1).

**命题。** 晶格的每个简正模等价于频率为 ω_k 的谐振子。对其量子化得到**声子**：晶格振动的量子，能量为 ℏω_k，零点能 ½ℏω_k，玻色–爱因斯坦占据数 n̄_k = 1/(e^{ℏω_k/k_BT} − 1)。

**Step 1 — Normal coordinate transformation.** Introduce the normal coordinate Q_k via the discrete Fourier transform

**第 1 步 — 简正坐标变换。** 通过离散傅里叶变换引入简正坐标 Q_k

  u_n = (1/√(NM)) Σ_k Q_k e^{ikna},

where the sum runs over the N allowed k-values in the first BZ. Under this transformation the Hamiltonian decouples:

其中求和遍历第一布里渊区内所有 N 个允许的 k 值。在此变换下哈密顿量解耦：

  H = ½ Σ_k [|Q̇_k|² + ω_k² |Q_k|²].

Each k-mode appears as an **independent harmonic oscillator** with mass 1 and frequency ω_k.

每个 k 模式表现为质量为 1、频率为 ω_k 的**独立谐振子**。

**Step 2 — Quantize each mode.** Following the ladder-operator procedure of Module 3.2 Section B, define for each k:

**第 2 步 — 对每个模式量子化。** 按模块 3.2 B 节的升降算符方法，对每个 k 定义：

  â_k = √(ω_k/2ℏ)(Q_k + i P_k/ω_k),   â†_k = √(ω_k/2ℏ)(Q_k − i P_k/ω_k),

where P_k = Q̇_k is the conjugate momentum. The canonical commutation relation [Q_k, P_k′] = iℏ δ_{kk′} gives

其中 P_k = Q̇_k 为正则动量。正则对易关系 [Q_k, P_k′] = iℏ δ_{kk′} 给出

  [â_k, â†_{k′}] = δ_{kk′}.

**Step 3 — Hamiltonian in terms of phonon operators.** Rewriting in exact parallel with Module 3.2:

**第 3 步 — 用声子算符表示哈密顿量。** 与模块 3.2 完全平行地改写：

  H = Σ_k ℏω_k (â†_k â_k + ½) = Σ_k ℏω_k (n̂_k + ½),

where n̂_k = â†_k â_k is the phonon number operator for mode k.

其中 n̂_k = â†_k â_k 为模式 k 的声子数算符。

**Step 4 — Phonon spectrum.** The eigenvalues of n̂_k are non-negative integers n_k = 0, 1, 2, …, (proved exactly as in Module 3.2 Step 6 — the same boundedness argument applies). The energy eigenvalue for a given set of occupation numbers {n_k} is

**第 4 步 — 声子谱。** n̂_k 的本征值为非负整数 n_k = 0, 1, 2, …（证明与模块 3.2 第 6 步完全相同——相同的有界性论证适用）。给定一组占据数 {n_k} 的能量本征值为

  E = Σ_k ℏω_k (n_k + ½).

State |n_{k₁}, n_{k₂}, …⟩ contains n_{kⱼ} phonons of mode j. Adding one phonon of mode k costs energy ℏω_k; this is the **phonon energy quantum**.

态 |n_{k₁}, n_{k₂}, …⟩ 含有模式 j 的 n_{kⱼ} 个声子。增加一个模式 k 的声子耗能 ℏω_k；这就是**声子能量量子**。

**Step 5 — Thermal occupation.** Phonons are bosons (integer spin, and the ladder-operator algebra produces a symmetric Fock space — no Pauli exclusion). At temperature T, each mode is in thermal equilibrium with the bath, and the mean occupation is given by the **Bose–Einstein distribution**:

**第 5 步 — 热占据。** 声子是玻色子（整数自旋，且升降算符代数产生对称福克空间——无泡利不相容）。在温度 T 下，每个模式与热浴平衡，平均占据数由**玻色–爱因斯坦分布**给出：

  n̄_k = ⟨n̂_k⟩ = 1/(e^{ℏω_k/k_BT} − 1).

This follows from the partition function Z_k = Σ_{n=0}^∞ e^{−βℏω_k n} = 1/(1 − e^{−βℏω_k}), giving ⟨n̂_k⟩ = −∂(ln Z_k)/∂(βℏω_k).

这由配分函数 Z_k = Σ_{n=0}^∞ e^{−βℏω_k n} = 1/(1 − e^{−βℏω_k}) 推出，给出 ⟨n̂_k⟩ = −∂(ln Z_k)/∂(βℏω_k)。

**Step 6 — Mean energy per mode and connection to the Debye model.** The mean energy of mode k (including zero-point energy) is

**第 6 步 — 每个模式的平均能量与德拜模型的联系。** 模式 k 的平均能量（含零点能）为

  ⟨E_k⟩ = ℏω_k(n̄_k + ½) = ℏω_k/2 + ℏω_k/(e^{ℏω_k/k_BT} − 1).

Summing over all k modes and replacing the sum by an integral using the density of states D(ω) recovers the Debye-model energy integral of Module 4.1 Section B. ∎

对所有 k 模式求和，并用态密度 D(ω) 将求和替换为积分，即恢复模块 4.1 B 节的德拜模型能量积分。∎

---

## D. Rigorous Counting: 3N Normal Modes for N Atoms · 严格计数：N 个原子有 3N 个简正模

**Claim.** A crystal of N unit cells each containing p atoms has 3pN normal modes total: 3 acoustic branches (with ω → 0 as k → 0) and 3(p−1) optical branches, each branch contributing N modes.

**命题。** 含 N 个原胞、每个原胞含 p 个原子的晶体共有 3pN 个简正模：3 支声学支（k → 0 时 ω → 0）和 3(p−1) 支光学支，每支贡献 N 个模式。

**Step 1 — Degrees of freedom.** The system has Np atoms × 3 directions = 3Np degrees of freedom. The dynamical matrix D(k) is a 3p × 3p Hermitian matrix for each k, giving 3p eigenfrequencies ω_s(k) (s = 1…3p). With N allowed k-points, the total number of modes is 3pN. ∎

**第 1 步 — 自由度。** 系统有 Np 个原子 × 3 个方向 = 3Np 个自由度。对每个 k，动力学矩阵 D(k) 是 3p × 3p 的厄米矩阵，给出 3p 个本征频率 ω_s(k)（s = 1…3p）。N 个允许的 k 点，总模式数为 3pN。∎

**Step 2 — Acoustic branches.** For s = 1, 2, 3 (acoustic), ω_s → 0 as k → 0 because a uniform translation of all atoms (k = 0 acoustic mode) costs zero energy — it corresponds to a rigid-body translation with no restoring force. The remaining 3(p−1) branches are optical with ω_s(0) > 0.

**第 2 步 — 声学支。** 对 s = 1, 2, 3（声学支），k → 0 时 ω_s → 0，因为所有原子整体平移（k = 0 的声学模式）不消耗能量——它对应无恢复力的刚体平移。其余 3(p−1) 支为光学支，ω_s(0) > 0。

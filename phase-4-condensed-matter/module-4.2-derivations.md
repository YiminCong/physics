# Derivations — Module 4.2: Crystal Structure & Reciprocal Space
# 推导 — 模块 4.2：晶体结构与倒格子空间

> Companion to [Module 4.2](./module-4.2-crystal-structure-and-reciprocal-space.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.2](./module-4.2-crystal-structure-and-reciprocal-space.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Reciprocal Lattice Vectors Satisfying aᵢ·bⱼ = 2πδᵢⱼ · 倒格矢满足 aᵢ·bⱼ = 2πδᵢⱼ

**Claim.** Given primitive lattice vectors a₁, a₂, a₃ of a Bravais lattice, the vectors

**命题。** 给定布拉伐格子的原胞基矢 a₁、a₂、a₃，定义矢量

  b₁ = 2π (a₂ × a₃) / (a₁ · (a₂ × a₃)),
  b₂ = 2π (a₃ × a₁) / (a₁ · (a₂ × a₃)),
  b₃ = 2π (a₁ × a₂) / (a₁ · (a₂ × a₃))

satisfy aᵢ · bⱼ = 2π δᵢⱼ and form primitive vectors of the **reciprocal lattice**.

则它们满足 aᵢ · bⱼ = 2π δᵢⱼ，并构成**倒格子**的原胞基矢。

**Step 1 — Define the cell volume.** Let Ω = a₁ · (a₂ × a₃) be the volume of the real-space primitive cell. For any non-degenerate lattice Ω ≠ 0.

**第 1 步 — 定义原胞体积。** 令 Ω = a₁ · (a₂ × a₃) 为正格子原胞的体积。对任何非退化格子，Ω ≠ 0。

**Step 2 — Verify the diagonal elements.** Consider a₁ · b₁:

**第 2 步 — 验证对角元。** 考察 a₁ · b₁：

  a₁ · b₁ = a₁ · [2π(a₂ × a₃)/Ω] = 2π [a₁ · (a₂ × a₃)] / Ω = 2π Ω / Ω = 2π.

By cyclic symmetry the same holds for a₂ · b₂ and a₃ · b₃. Thus aᵢ · bᵢ = 2π (no sum).

由轮换对称性，a₂ · b₂ 与 a₃ · b₃ 同理。故 aᵢ · bᵢ = 2π（不求和）。

**Step 3 — Verify the off-diagonal elements.** Consider a₁ · b₂:

**第 3 步 — 验证非对角元。** 考察 a₁ · b₂：

  a₁ · b₂ = a₁ · [2π(a₃ × a₁)/Ω] = 2π [a₁ · (a₃ × a₁)] / Ω.

The scalar triple product a₁ · (a₃ × a₁) contains a₁ twice: it equals the determinant of a matrix whose first and third rows are identical, hence it vanishes. Thus a₁ · b₂ = 0. By the same argument all off-diagonal pairs give zero. Combining Steps 2–3:

标量三重积 a₁ · (a₃ × a₁) 含两个相同的矢量 a₁，等价于行列式中有两行相同，故为零。因此 a₁ · b₂ = 0。同理所有非对角对均为零。合并第 2–3 步：

  aᵢ · bⱼ = 2π δᵢⱼ.  ∎

**Step 4 — Every reciprocal-lattice point.** The full reciprocal lattice consists of all integer linear combinations G = h b₁ + k b₂ + l b₃ (h, k, l ∈ ℤ). By linearity, for any real-lattice vector R = n₁ a₁ + n₂ a₂ + n₃ a₃ (nᵢ ∈ ℤ):

**第 4 步 — 所有倒格子格点。** 完整倒格子由所有整数线性组合 G = h b₁ + k b₂ + l b₃（h, k, l ∈ ℤ）构成。由线性性，对任意正格矢 R = n₁ a₁ + n₂ a₂ + n₃ a₃（nᵢ ∈ ℤ）：

  G · R = 2π(hn₁ + kn₂ + ln₃) ∈ 2πℤ,

so e^{iG·R} = 1. This is the defining property of the reciprocal lattice: it is the set of all wavevectors G such that the plane wave e^{iG·r} has the full periodicity of the real lattice.

故 e^{iG·R} = 1。这正是倒格子的定义性质：它是所有波矢 G 的集合，使得平面波 e^{iG·r} 具有正格子的完整周期性。

---

## B. Bragg Condition 2d sinθ = nλ and the Laue Condition Δk = G · 布拉格条件与劳厄条件等价性

**Claim.** Constructive interference of waves scattered by parallel crystal planes of spacing d occurs when 2d sinθ = nλ (Bragg). This is equivalent to the condition that the change in wavevector Δk = k_f − k_i equals a reciprocal-lattice vector G (Laue).

**命题。** 间距为 d 的平行晶面对波的散射产生相长干涉，当且仅当 2d sinθ = nλ（布拉格）。这等价于波矢改变量 Δk = k_f − k_i 等于某个倒格矢 G（劳厄条件）。

**Step 1 — Path-length difference between adjacent planes.** Consider a beam of wavelength λ incident at glancing angle θ to a family of parallel planes separated by d. The path-length difference between a ray reflected from the n-th plane and the (n+1)-th plane is 2d sinθ (standard geometry: incoming and outgoing segments each project d sinθ onto the normal).

**第 1 步 — 相邻晶面间的光程差。** 考虑波长为 λ 的束以掠射角 θ 入射至间距为 d 的一组平行晶面。从第 n 层与第 n+1 层反射的光线之间的光程差为 2d sinθ（标准几何：入射与出射路径各在法线方向上投影 d sinθ）。

**Step 2 — Constructive-interference condition.** For constructive interference the path-length difference must equal an integer number of wavelengths:

**第 2 步 — 相长干涉条件。** 相长干涉要求光程差等于整数个波长：

  2d sinθ = nλ,   n = 1, 2, 3, …

This is **Bragg's law**.

这就是**布拉格定律**。

**Step 3 — Elastic scattering kinematics.** For elastic scattering |kᵢ| = |kf| = 2π/λ ≡ k. The incident and final wavevectors are related by the scattering geometry, and the momentum transfer (Laue vector) is:

**第 3 步 — 弹性散射运动学。** 弹性散射中 |kᵢ| = |kf| = 2π/λ ≡ k。入射与终态波矢由散射几何联系，动量转移（劳厄矢量）为：

  Δk = kf − kᵢ.

Since the scattering is specular (angle of incidence = angle of reflection about the plane normal n̂), we have

由于散射是镜面反射（入射角等于反射角，关于晶面法线 n̂），有

  Δk = 2(kᵢ · n̂) n̂ = 2k sinθ · n̂.

**Step 4 — Relate |Δk| to the Bragg condition.** The magnitude is |Δk| = 2k sinθ = 2(2π/λ) sinθ. Inserting the Bragg condition 2d sinθ = nλ:

**第 4 步 — 将 |Δk| 与布拉格条件联系。** 模量为 |Δk| = 2k sinθ = 2(2π/λ) sinθ。代入布拉格条件 2d sinθ = nλ：

  |Δk| = 2(2π/λ)(nλ/2d) = 2πn/d.

**Step 5 — Identify with a reciprocal-lattice vector.** The set of planes with Miller indices (h,k,l) has spacing d_{hkl} = 2π/|G_{hkl}| where G_{hkl} = hb₁ + kb₂ + lb₃ is the corresponding reciprocal-lattice vector. The normal n̂ is parallel to G_{hkl}. Therefore

**第 5 步 — 与倒格矢对应。** 密勒指数为 (h,k,l) 的晶面族间距为 d_{hkl} = 2π/|G_{hkl}|，其中 G_{hkl} = hb₁ + kb₂ + lb₃ 是对应的倒格矢，法线 n̂ 平行于 G_{hkl}。因此

  Δk = |Δk| n̂ = (2πn/d_{hkl}) · (G_{hkl}/|G_{hkl}|) = n G_{hkl}/|G_{hkl}| · |G_{hkl}| = n G_{hkl}^{unit} · |G_{hkl}|.

Since n G_{hkl} is itself a reciprocal-lattice vector (integer multiple), we conclude

因为 n G_{hkl} 本身就是一个倒格矢（整数倍），故得

  **Δk = G**  (Laue condition).  ∎

**布拉格条件 ⟺ 劳厄条件 Δk = G。∎**

**Step 6 — Ewald sphere construction (geometric restatement).** Since |kᵢ| = |kf| = k and kf = kᵢ + G, scattering occurs when a reciprocal-lattice point G lies exactly on the sphere of radius k centred at the tip of −kᵢ. This is the **Ewald sphere**; the Bragg peaks map out the reciprocal lattice.

**第 6 步 — 厄瓦尔德球（几何重表述）。** 由于 |kᵢ| = |kf| = k 且 kf = kᵢ + G，当倒格子格点 G 恰好在以 −kᵢ 顶端为圆心、半径为 k 的球上时发生散射。这就是**厄瓦尔德球**；布拉格峰描绘出倒格子的形貌。

---

## C. The Structure Factor · 结构因子

**Claim.** For a crystal with N_b atoms per unit cell at positions dⱼ (j = 1…N_b) with atomic form factors fⱼ, the scattered amplitude at reciprocal-lattice vector G = hb₁ + kb₂ + lb₃ is proportional to the **structure factor**

**命题。** 对每个原胞含 N_b 个原子（位置为 dⱼ，原子形状因子为 fⱼ）的晶体，在倒格矢 G = hb₁ + kb₂ + lb₃ 处的散射振幅正比于**结构因子**

  S(G) = Σⱼ fⱼ e^{iG·dⱼ}.

Certain reflections are systematically absent when S(G) = 0.

当 S(G) = 0 时，某些反射系统性消失（消光）。

**Step 1 — Scattering amplitude from a single unit cell.** The scattering amplitude is proportional to the Fourier transform of the electron density ρ(r) at wavevector Δk. For elastic scattering satisfying the Laue condition Δk = G, the amplitude from one unit cell is

**第 1 步 — 单个原胞的散射振幅。** 散射振幅正比于电子密度 ρ(r) 在波矢 Δk 处的傅里叶变换。对满足劳厄条件 Δk = G 的弹性散射，一个原胞的振幅为

  A_cell = ∫_{cell} ρ(r) e^{iG·r} d³r.

**Step 2 — Decompose density into atomic contributions.** Write the electron density as a sum over atoms in the unit cell:

**第 2 步 — 将密度分解为原子贡献之和。** 将电子密度写成原胞内各原子贡献之和：

  ρ(r) = Σⱼ ρⱼ(r − dⱼ),

where ρⱼ is the electron density of the j-th atom centred at dⱼ.

其中 ρⱼ 为以 dⱼ 为中心的第 j 个原子的电子密度。

**Step 3 — Substitute and factor.** Inserting into the cell integral and changing variables r′ = r − dⱼ:

**第 3 步 — 代入并分离因子。** 代入原胞积分，令 r′ = r − dⱼ 换元：

  A_cell = Σⱼ ∫ ρⱼ(r′) e^{iG·(r′+dⱼ)} d³r′
         = Σⱼ e^{iG·dⱼ} ∫ ρⱼ(r′) e^{iG·r′} d³r′
         = Σⱼ fⱼ(G) e^{iG·dⱼ},

where fⱼ(G) = ∫ ρⱼ(r′) e^{iG·r′} d³r′ is the **atomic form factor** of atom j. For G not too large, fⱼ ≈ Zⱼ (the atomic number).

其中 fⱼ(G) = ∫ ρⱼ(r′) e^{iG·r′} d³r′ 为第 j 个原子的**原子形状因子**。当 G 不太大时 fⱼ ≈ Zⱼ（原子序数）。

**Step 4 — Define the structure factor and diffracted intensity.** The **structure factor** is

**第 4 步 — 定义结构因子与衍射强度。** **结构因子**定义为

  S(G) = Σⱼ fⱼ e^{iG·dⱼ}.

Since all unit cells are identical, the total amplitude is A_total = N_cells · S(G) · (phase factor). The diffracted intensity is

由于所有原胞相同，总振幅 A_total = N_cells · S(G) · （相位因子）。衍射强度为

  I(G) ∝ |S(G)|².

**Step 5 — Example: BCC systematic absences.** For a body-centred cubic lattice, take d₁ = (0,0,0) and d₂ = (a/2)(1,1,1) with f₁ = f₂ = f. Using G = (h b₁ + k b₂ + l b₃) and noting G · d₂ = π(h+k+l):

**第 5 步 — 例：体心立方的系统消光。** 对体心立方格子，取 d₁ = (0,0,0)，d₂ = (a/2)(1,1,1)，f₁ = f₂ = f。利用 G · d₂ = π(h+k+l)：

  S = f(1 + e^{iπ(h+k+l)}).

This vanishes when h+k+l is odd, giving **systematic absences** for odd h+k+l. Only reflections with h+k+l even appear — a direct fingerprint of the BCC symmetry. ∎

当 h+k+l 为奇数时 S = 0，即**系统消光**发生于 h+k+l 为奇数的情形。只有 h+k+l 为偶数的反射出现——这是体心立方对称性的直接特征。∎

---

## D. Brillouin Zone as the Wigner–Seitz Cell of the Reciprocal Lattice · 布里渊区作为倒格子的维格纳–塞茨原胞

**Claim.** The first Brillouin zone — the primitive cell of the reciprocal lattice formed by all points closer to G = 0 than to any other reciprocal-lattice point — contains exactly one k-state per real-space unit cell, and its volume is (2π)³/Ω.

**命题。** 第一布里渊区——倒格子的原胞，由所有比任何其他倒格子格点更靠近 G = 0 的点构成——每个正格子原胞恰好包含一个 k 态，其体积为 (2π)³/Ω。

**Step 1 — Volume of the BZ.** The volume of the BZ equals the volume of the reciprocal primitive cell. Using the identity for volumes of dual cells:

**第 1 步 — 布里渊区的体积。** 布里渊区的体积等于倒格子原胞的体积。利用对偶原胞体积的恒等式：

  V_{BZ} = b₁ · (b₂ × b₃) = (2π)³ / [a₁ · (a₂ × a₃)] = (2π)³ / Ω.

**Step 2 — State counting.** For a crystal of volume V = NΩ (N unit cells), periodic boundary conditions give k-points spaced (2π/L) in each direction. The number of k-points in the BZ is:

**第 2 步 — 态计数。** 对体积 V = NΩ（N 个原胞）的晶体，周期性边界条件使 k 点间距为 (2π/L)。布里渊区内的 k 点数为：

  N_k = V_{BZ} / (2π/L)³ = [(2π)³/Ω] / [(2π)³/V] = V/Ω = N.

There is exactly one k-point per unit cell, so one band can hold 2N electrons (including spin). This underlies the band-filling rule for metals vs. insulators. ∎

每个原胞恰好一个 k 点，因此一条能带（含自旋）可容纳 2N 个电子。这是金属与绝缘体能带填充判据的基础。∎

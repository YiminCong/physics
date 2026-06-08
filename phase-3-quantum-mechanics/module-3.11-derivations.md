# Derivations — Module 3.11: Angular Momentum (Addition & Spin)
# 推导 — 模块 3.11：角动量（合成与自旋）

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.11](./module-3.11-angular-momentum-advanced.md). Full step-by-step proofs of the angular momentum commutation relations, the ladder-operator spectrum, the explicit ½⊗½ Clebsch–Gordan decomposition, and the Clebsch–Gordan table. English first, then 中文.
> [模块 3.11](./module-3.11-angular-momentum-advanced.md) 的配套文档：角动量对易关系、梯形算符谱、显式 ½⊗½ Clebsch–Gordan 分解与系数表的完整逐步证明。先英文，后中文。

---

## A. Angular Momentum Commutation Relations · 角动量对易关系

**Claim.** The angular momentum operators Ĵ_x, Ĵ_y, Ĵ_z (defined abstractly or as orbital r × p) satisfy [Ĵᵢ, Ĵⱼ] = iℏ ε_{ijk} Ĵₖ, i.e.

**命题。** 角动量算符 Ĵ_x, Ĵ_y, Ĵ_z（抽象定义或作为轨道 r × p）满足 [Ĵᵢ, Ĵⱼ] = iℏ ε_{ijk} Ĵₖ，即

  [Ĵ_x, Ĵ_y] = iℏ Ĵ_z,   [Ĵ_y, Ĵ_z] = iℏ Ĵ_x,   [Ĵ_z, Ĵ_x] = iℏ Ĵ_y.

**Step 1 — Definition of orbital angular momentum.** For orbital angular momentum L̂ = r̂ × p̂:

**第 1 步 — 轨道角动量的定义。** 对轨道角动量 L̂ = r̂ × p̂：

  L̂_x = ŷ p̂_z − ẑ p̂_y,   L̂_y = ẑ p̂_x − x̂ p̂_z,   L̂_z = x̂ p̂_y − ŷ p̂_x.

**Step 2 — Compute [L̂_x, L̂_y].** Expand using the canonical commutation relations [x̂ᵢ, p̂ⱼ] = iℏ δᵢⱼ and [x̂ᵢ, x̂ⱼ] = 0, [p̂ᵢ, p̂ⱼ] = 0:

**第 2 步 — 计算 [L̂_x, L̂_y]。** 利用正则对易关系 [x̂ᵢ, p̂ⱼ] = iℏ δᵢⱼ，[x̂ᵢ, x̂ⱼ] = 0，[p̂ᵢ, p̂ⱼ] = 0 展开：

  [L̂_x, L̂_y] = [ŷ p̂_z − ẑ p̂_y, ẑ p̂_x − x̂ p̂_z].

Expand using bilinearity of the commutator:

利用对易子的双线性展开：

  = [ŷ p̂_z, ẑ p̂_x] − [ŷ p̂_z, x̂ p̂_z] − [ẑ p̂_y, ẑ p̂_x] + [ẑ p̂_y, x̂ p̂_z].

Evaluate each term using [AB, CD] = A[B,C]D + AC[B,D] + [A,C]DB + C[A,D]B:

用 [AB,CD] = A[B,C]D + AC[B,D] + [A,C]DB + C[A,D]B 逐项计算：

  [ŷ p̂_z, ẑ p̂_x] = ŷ[p̂_z, ẑ]p̂_x + ŷ ẑ [p̂_z, p̂_x] + [ŷ, ẑ]p̂_z p̂_x + ẑ[ŷ, p̂_x]p̂_z
                   = ŷ(−iℏ)p̂_x + 0 + 0 + 0 = −iℏ ŷ p̂_x.

  [ŷ p̂_z, x̂ p̂_z] = ŷ[p̂_z, x̂]p̂_z + ŷ x̂[p̂_z, p̂_z] + [ŷ, x̂]p̂_z² + x̂[ŷ, p̂_z]p̂_z
                   = 0 + 0 + 0 + 0 = 0.   (all cross-commutators vanish)

  [ẑ p̂_y, ẑ p̂_x] = ẑ[p̂_y, ẑ]p̂_x + 0 + 0 + 0 = ẑ·0·p̂_x = 0.   (p̂_y and ẑ commute)

  [ẑ p̂_y, x̂ p̂_z] = ẑ[p̂_y, x̂]p̂_z + ẑ x̂[p̂_y, p̂_z] + [ẑ, x̂]p̂_y p̂_z + x̂[ẑ, p̂_z]p̂_y
                   = 0 + 0 + 0 + x̂(iℏ)p̂_y = iℏ x̂ p̂_y.

Adding all contributions:

将所有贡献相加：

  [L̂_x, L̂_y] = −iℏ ŷ p̂_x − 0 − 0 + iℏ x̂ p̂_y = iℏ(x̂ p̂_y − ŷ p̂_x) = iℏ L̂_z.

The other two relations follow by cyclic permutation x → y → z → x. ∎

其余两个关系由循环置换 x → y → z → x 得到。∎

**Note for spin and general angular momentum.** For spin operators defined by Ŝ = (ℏ/2)σ with Pauli matrices, one verifies [Ŝ_x, Ŝ_y] = iℏ Ŝ_z directly from the Pauli matrix algebra: σ_x σ_y − σ_y σ_x = 2iσ_z (multiply 2×2 matrices explicitly). The abstract angular momentum algebra is then the defining relation for any generator of rotations (by Noether's theorem and the Lie algebra so(3) ≅ su(2)).

**关于自旋和一般角动量的注记。** 对由泡利矩阵定义的自旋算符 Ŝ = (ℏ/2)σ，直接由泡利矩阵代数验证 [Ŝ_x, Ŝ_y] = iℏ Ŝ_z：σ_x σ_y − σ_y σ_x = 2iσ_z（显式相乘 2×2 矩阵）。抽象角动量代数于是成为任意转动生成元的定义关系（由诺特定理与李代数 so(3) ≅ su(2)）。

---

## B. Ladder Operators and the J Spectrum · 梯形算符与 J 谱

**Claim.** For an angular momentum operator satisfying the commutation relations above, with Ĵ² = Ĵ_x² + Ĵ_y² + Ĵ_z², and ladder operators Ĵ± = Ĵ_x ± iĴ_y:

**命题。** 对满足上述对易关系的角动量算符，令 Ĵ² = Ĵ_x² + Ĵ_y² + Ĵ_z²，梯形算符 Ĵ± = Ĵ_x ± iĴ_y：

(i) [Ĵ², Ĵᵢ] = 0 for i = x, y, z (Ĵ² is a Casimir operator).

(ii) The simultaneous eigenstates |j, m⟩ of Ĵ² and Ĵ_z satisfy Ĵ²|j,m⟩ = j(j+1)ℏ²|j,m⟩ and Ĵ_z|j,m⟩ = mℏ|j,m⟩, with j = 0, ½, 1, 3/2, … and m = −j, −j+1, …, j−1, j.

(iii) Ĵ±|j,m⟩ = ℏ√(j(j+1) − m(m±1)) |j, m±1⟩.

**Step 1 — Prove [Ĵ², Ĵ_z] = 0.** Write Ĵ² = Ĵ_x² + Ĵ_y² + Ĵ_z²:

**第 1 步 — 证明 [Ĵ², Ĵ_z] = 0。** 令 Ĵ² = Ĵ_x² + Ĵ_y² + Ĵ_z²：

  [Ĵ², Ĵ_z] = [Ĵ_x², Ĵ_z] + [Ĵ_y², Ĵ_z] + [Ĵ_z², Ĵ_z].

The last term is zero. For the first:

最后一项为零。对第一项：

  [Ĵ_x², Ĵ_z] = Ĵ_x[Ĵ_x, Ĵ_z] + [Ĵ_x, Ĵ_z]Ĵ_x = Ĵ_x(−iℏĴ_y) + (−iℏĴ_y)Ĵ_x = −iℏ(Ĵ_x Ĵ_y + Ĵ_y Ĵ_x).

For the second:

对第二项：

  [Ĵ_y², Ĵ_z] = Ĵ_y[Ĵ_y, Ĵ_z] + [Ĵ_y, Ĵ_z]Ĵ_y = Ĵ_y(iℏĴ_x) + (iℏĴ_x)Ĵ_y = iℏ(Ĵ_y Ĵ_x + Ĵ_x Ĵ_y).

Adding: [Ĵ², Ĵ_z] = −iℏ(Ĵ_x Ĵ_y + Ĵ_y Ĵ_x) + iℏ(Ĵ_y Ĵ_x + Ĵ_x Ĵ_y) = 0. ∎ (Cyclic permutation gives [Ĵ², Ĵ_x] = [Ĵ², Ĵ_y] = 0 similarly.)

相加：[Ĵ², Ĵ_z] = 0。∎（循环置换类似地给出 [Ĵ², Ĵ_x] = [Ĵ², Ĵ_y] = 0。）

**Step 2 — Ladder operator commutators.** Compute [Ĵ_z, Ĵ±]:

**第 2 步 — 梯形算符对易子。** 计算 [Ĵ_z, Ĵ±]：

  [Ĵ_z, Ĵ+] = [Ĵ_z, Ĵ_x + iĴ_y] = [Ĵ_z, Ĵ_x] + i[Ĵ_z, Ĵ_y]
              = iℏĴ_y + i(−iℏĴ_x) = iℏĴ_y + ℏĴ_x = ℏ(Ĵ_x + iĴ_y) = ℏĴ+.

Similarly [Ĵ_z, Ĵ−] = −ℏĴ−. Also [Ĵ+, Ĵ−] = 2ℏĴ_z (verified by direct expansion).

类似地 [Ĵ_z, Ĵ−] = −ℏĴ−。同样 [Ĵ+, Ĵ−] = 2ℏĴ_z（直接展开验证）。

**Step 3 — Ladder action.** If Ĵ_z|j,m⟩ = mℏ|j,m⟩, then:

**第 3 步 — 梯形作用。** 若 Ĵ_z|j,m⟩ = mℏ|j,m⟩，则：

  Ĵ_z (Ĵ+|j,m⟩) = (Ĵ+ Ĵ_z + [Ĵ_z, Ĵ+])|j,m⟩ = (Ĵ+ mℏ + ℏĴ+)|j,m⟩ = (m+1)ℏ (Ĵ+|j,m⟩).

So Ĵ+|j,m⟩ is an eigenstate of Ĵ_z with eigenvalue (m+1)ℏ — it raises m by 1. Similarly Ĵ− lowers m by 1.

故 Ĵ+|j,m⟩ 是 Ĵ_z 的本征态，本征值为 (m+1)ℏ——它将 m 升高 1。类似地 Ĵ− 将 m 降低 1。

**Step 4 — Spectrum is bounded.** The eigenvalue of Ĵ² is at least ℏ² times the square of any component's eigenvalue. Formally, for any state ⟨Ĵ²⟩ ≥ ⟨Ĵ_z²⟩, hence j(j+1) ≥ m². This bounds |m| ≤ j. The ladder must terminate: there exist states |j, m_max⟩ and |j, m_min⟩ with

**第 4 步 — 谱有界。** Ĵ² 的本征值至少是任意分量本征值平方的 ℏ² 倍。形式上，对任意态 ⟨Ĵ²⟩ ≥ ⟨Ĵ_z²⟩，故 j(j+1) ≥ m²。这限制了 |m| ≤ j。梯形必须终止：存在态 |j, m_max⟩ 和 |j, m_min⟩ 满足

  Ĵ+|j, m_max⟩ = 0,   Ĵ−|j, m_min⟩ = 0.

**Step 5 — Determine m_max and m_min.** Using Ĵ−Ĵ+ = Ĵ² − Ĵ_z² − ℏĴ_z:

**第 5 步 — 确定 m_max 和 m_min。** 利用 Ĵ−Ĵ+ = Ĵ² − Ĵ_z² − ℏĴ_z：

  ⟨j, m_max|Ĵ−Ĵ+|j, m_max⟩ = ‖Ĵ+|j, m_max⟩‖² = 0

  ⟹ [j(j+1) − m_max² − m_max]ℏ² = 0 ⟹ j(j+1) = m_max(m_max + 1) ⟹ m_max = j.

Similarly, using Ĵ+Ĵ− = Ĵ² − Ĵ_z² + ℏĴ_z, the termination of the lower ladder gives m_min = −j.

类似地，利用 Ĵ+Ĵ− = Ĵ² − Ĵ_z² + ℏĴ_z，下梯形终止给出 m_min = −j。

**Step 6 — Allowed values.** The integer steps from m_min = −j to m_max = j require 2j to be a non-negative integer, so j = 0, ½, 1, 3/2, 2, … and m = −j, −j+1, …, j−1, j.

**第 6 步 — 允许值。** 从 m_min = −j 到 m_max = j 整数步长要求 2j 为非负整数，故 j = 0, ½, 1, 3/2, 2, …，m = −j, −j+1, …, j−1, j。

**Step 7 — Normalize the ladder action.** Compute ‖Ĵ+|j,m⟩‖²:

**第 7 步 — 归一化梯形作用。** 计算 ‖Ĵ+|j,m⟩‖²：

  ‖Ĵ+|j,m⟩‖² = ⟨j,m|Ĵ−Ĵ+|j,m⟩ = ⟨j,m|(Ĵ² − Ĵ_z² − ℏĴ_z)|j,m⟩
              = [j(j+1) − m² − m]ℏ² = [j(j+1) − m(m+1)]ℏ².

Since Ĵ+|j,m⟩ is proportional to |j, m+1⟩ (proven to be an eigenstate in Step 3), writing Ĵ+|j,m⟩ = c|j, m+1⟩ and using ‖c|j,m+1⟩‖² = |c|²:

由于 Ĵ+|j,m⟩ 正比于 |j, m+1⟩（第 3 步已证），令 Ĵ+|j,m⟩ = c|j, m+1⟩，利用 ‖c|j,m+1⟩‖² = |c|²：

  |c|² = [j(j+1) − m(m+1)]ℏ²,   choosing c real and positive: c = ℏ√(j(j+1)−m(m+1)).

Therefore:

因此：

  **Ĵ+|j,m⟩ = ℏ√(j(j+1) − m(m+1)) |j, m+1⟩.**

For Ĵ−, by the same method (using ‖Ĵ−|j,m⟩‖² = [j(j+1)−m(m−1)]ℏ²):

对 Ĵ−，用相同方法（利用 ‖Ĵ−|j,m⟩‖² = [j(j+1)−m(m−1)]ℏ²）：

  **Ĵ−|j,m⟩ = ℏ√(j(j+1) − m(m−1)) |j, m−1⟩.**   ∎

These two formulas can be unified as Ĵ±|j,m⟩ = ℏ√(j(j+1) − m(m±1)) |j, m±1⟩.

这两个公式可以统一为 Ĵ±|j,m⟩ = ℏ√(j(j+1) − m(m±1)) |j, m±1⟩。∎

---

## C. Addition of Two Spin-½'s: Singlet and Triplet · 两个自旋-½ 的合成：单态与三重态

**Claim.** The tensor product space of two spin-½ particles (dimension 2⊗2 = 4) decomposes under the total angular momentum Ĵ = Ŝ₁ + Ŝ₂ into a triplet (j = 1, three states) and a singlet (j = 0, one state):

**命题。** 两个自旋-½ 粒子的张量积空间（维数 2⊗2 = 4）在总角动量 Ĵ = Ŝ₁ + Ŝ₂ 下分解为三重态（j = 1，三个态）和单态（j = 0，一个态）：

  Triplet: |1,+1⟩ = |+⟩|+⟩,
           |1, 0⟩ = (1/√2)(|+⟩|−⟩ + |−⟩|+⟩),
           |1,−1⟩ = |−⟩|−⟩.

  Singlet: |0, 0⟩ = (1/√2)(|+⟩|−⟩ − |−⟩|+⟩).

  三重态：|1,+1⟩ = |+⟩|+⟩，
          |1, 0⟩ = (1/√2)(|+⟩|−⟩ + |−⟩|+⟩)，
          |1,−1⟩ = |−⟩|−⟩。

  单态：|0, 0⟩ = (1/√2)(|+⟩|−⟩ − |−⟩|+⟩)。

Here |+⟩ ≡ |s=½, m=+½⟩ and |−⟩ ≡ |s=½, m=−½⟩.

此处 |+⟩ ≡ |s=½, m=+½⟩，|−⟩ ≡ |s=½, m=−½⟩。

**Step 1 — Identify the highest-weight state.** The state of maximum total m is m = m₁ + m₂ = ½ + ½ = 1. The only product state with m = 1 is |+⟩₁|+⟩₂. Since m = 1 implies j ≥ 1, and the total angular momentum of the combined system can be at most j = 1 (since each spin is ½), this must be |j = 1, m = 1⟩:

**第 1 步 — 确定最高权态。** 最大总 m 为 m = m₁ + m₂ = ½ + ½ = 1。m = 1 的唯一直积态为 |+⟩₁|+⟩₂。由于 m = 1 意味着 j ≥ 1，而合并系统的总角动量最大为 j = 1（每个自旋为 ½），故这必须是 |j=1, m=1⟩：

  |1, +1⟩ = |+⟩₁|+⟩₂.

**Step 2 — Apply Ĵ− to get |1, 0⟩.** The total lowering operator is Ĵ− = Ŝ₁− ⊗ 1̂₂ + 1̂₁ ⊗ Ŝ₂−. Using Ĵ−|j,m⟩ = ℏ√(j(j+1)−m(m−1))|j,m−1⟩ with j = m = 1:

**第 2 步 — 作用 Ĵ− 得 |1, 0⟩。** 总降算符为 Ĵ− = Ŝ₁− ⊗ 1̂₂ + 1̂₁ ⊗ Ŝ₂−。利用 Ĵ−|j,m⟩ = ℏ√(j(j+1)−m(m−1))|j,m−1⟩，取 j = m = 1：

  Ĵ−|1,+1⟩ = ℏ√(1·2 − 1·0)|1, 0⟩ = ℏ√2 |1, 0⟩.

The left-hand side acts on the product state:

左端作用于直积态：

  Ĵ−|+⟩₁|+⟩₂ = (Ŝ₁−|+⟩₁)|+⟩₂ + |+⟩₁(Ŝ₂−|+⟩₂).

Using Ŝ−|+⟩ = ℏ√(½·3/2 − ½(½−1))|−⟩ = ℏ√(¾−(−¼))|−⟩ = ℏ√1 |−⟩ = ℏ|−⟩:

利用 Ŝ−|+⟩ = ℏ√(½·3/2 − ½·(½−1))|−⟩ = ℏ|−⟩：

  Ĵ−|+⟩₁|+⟩₂ = ℏ|−⟩₁|+⟩₂ + ℏ|+⟩₁|−⟩₂.

Setting equal: ℏ√2 |1, 0⟩ = ℏ(|−⟩₁|+⟩₂ + |+⟩₁|−⟩₂), so

令两端相等：ℏ√2 |1,0⟩ = ℏ(|−⟩₁|+⟩₂ + |+⟩₁|−⟩₂)，故

  |1, 0⟩ = (1/√2)(|+⟩₁|−⟩₂ + |−⟩₁|+⟩₂).

**Step 3 — Apply Ĵ− again to get |1, −1⟩.** Apply Ĵ− to |1, 0⟩: Ĵ−|1,0⟩ = ℏ√(2−0)|1,−1⟩ = ℏ√2|1,−1⟩.

**第 3 步 — 再次作用 Ĵ− 得 |1, −1⟩。** 对 |1,0⟩ 作用 Ĵ−：Ĵ−|1,0⟩ = ℏ√(2−0)|1,−1⟩ = ℏ√2|1,−1⟩。

  Ĵ−((1/√2)(|+⟩₁|−⟩₂ + |−⟩₁|+⟩₂))
    = (1/√2)[(Ŝ₁−|+⟩₁)|−⟩₂ + |+⟩₁(Ŝ₂−|−⟩₂) + (Ŝ₁−|−⟩₁)|+⟩₂ + |−⟩₁(Ŝ₂−|+⟩₂)]
    = (1/√2)[ℏ|−⟩₁|−⟩₂ + 0 + 0 + ℏ|−⟩₁|−⟩₂]
    = (2ℏ/√2)|−⟩₁|−⟩₂ = ℏ√2 |−⟩₁|−⟩₂.

(Using Ŝ−|−⟩ = 0 since |−⟩ is already the lowest state.) Hence:

（利用 Ŝ−|−⟩ = 0，因为 |−⟩ 已是最低态。）故：

  |1, −1⟩ = |−⟩₁|−⟩₂.

**Step 4 — Find the singlet by orthogonality.** The remaining state in the m = 0 subspace must be orthogonal to |1, 0⟩. The general m = 0 state is α|+⟩₁|−⟩₂ + β|−⟩₁|+⟩₂. Requiring orthogonality to |1,0⟩ = (1/√2)(|+−⟩ + |−+⟩):

**第 4 步 — 由正交性求单态。** m = 0 子空间中剩余的态必须与 |1,0⟩ 正交。一般 m = 0 态为 α|+⟩₁|−⟩₂ + β|−⟩₁|+⟩₂。要求与 |1,0⟩ = (1/√2)(|+−⟩ + |−+⟩) 正交：

  ⟨1,0|(α|+−⟩ + β|−+⟩) = (1/√2)(α + β) = 0 ⟹ β = −α.

Normalizing: |α|² + |β|² = 2|α|² = 1, so |α| = 1/√2. Choosing α = 1/√2:

归一化：|α|² + |β|² = 2|α|² = 1，故 |α| = 1/√2。取 α = 1/√2：

  |0, 0⟩ = (1/√2)(|+⟩₁|−⟩₂ − |−⟩₁|+⟩₂).

**Step 5 — Verify |0,0⟩ is a j = 0 state.** Check Ĵ+|0,0⟩ = 0:

**第 5 步 — 验证 |0,0⟩ 是 j = 0 的态。** 验证 Ĵ+|0,0⟩ = 0：

  Ĵ+(1/√2)(|+−⟩ − |−+⟩)
    = (1/√2)[(Ŝ₁+|+⟩₁)|−⟩₂ + |+⟩₁(Ŝ₂+|−⟩₂) − (Ŝ₁+|−⟩₁)|+⟩₂ − |−⟩₁(Ŝ₂+|+⟩₂)]
    = (1/√2)[0 + ℏ|+⟩₁|+⟩₂ − ℏ|+⟩₁|+⟩₂ − 0] = 0. ✓

Also Ĵ_z|0,0⟩ = 0 (since both terms have total m = 0). And Ĵ²|0,0⟩ = 0 can be confirmed from Ĵ² = (Ĵ+Ĵ− + Ĵ−Ĵ+)/2 + Ĵ_z² acting term by term, giving 0. ∎

同样 Ĵ_z|0,0⟩ = 0（因为两项的总 m = 0）。Ĵ²|0,0⟩ = 0 可由 Ĵ² = (Ĵ+Ĵ− + Ĵ−Ĵ+)/2 + Ĵ_z² 逐项作用确认，结果为 0。∎

---

## D. Clebsch–Gordan Table for ½ ⊗ ½ · ½ ⊗ ½ 的 Clebsch–Gordan 系数表

The Clebsch–Gordan coefficients ⟨j₁, m₁; j₂, m₂ | J, M⟩ for j₁ = j₂ = ½ read off from the decomposition above:

从上述分解中读出的 j₁ = j₂ = ½ 的 Clebsch–Gordan 系数 ⟨j₁, m₁; j₂, m₂ | J, M⟩：

  |J = 1, M = +1⟩:   ⟨+½, +½ | 1, +1⟩ = 1.
  |J = 1, M =  0⟩:   ⟨+½, −½ | 1,  0⟩ = 1/√2,   ⟨−½, +½ | 1,  0⟩ = 1/√2.
  |J = 1, M = −1⟩:   ⟨−½, −½ | 1, −1⟩ = 1.
  |J = 0, M =  0⟩:   ⟨+½, −½ | 0,  0⟩ = 1/√2,   ⟨−½, +½ | 0,  0⟩ = −1/√2.

All other coefficients vanish (since the tensor product state must have m₁ + m₂ = M).

所有其他系数为零（因为张量积态必须满足 m₁ + m₂ = M）。

**Physical meaning.** The singlet (1/√2)(|+−⟩ − |−+⟩) is antisymmetric under exchange of the two particles' spin states, while all three triplet states are symmetric. This antisymmetric singlet is the building block of Cooper pairs in BCS superconductivity (two electrons with opposite spins and momenta).

**物理含义。** 单态 (1/√2)(|+−⟩ − |−+⟩) 在交换两粒子自旋态下是反对称的，而三个三重态均为对称的。这个反对称单态是 BCS 超导中库珀对的基本结构（两个自旋和动量相反的电子）。

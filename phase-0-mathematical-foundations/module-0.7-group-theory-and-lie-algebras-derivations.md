# Derivations — Module 0.7: Group Theory & Lie Algebras
# 推导 — 模块 0.7：群论与李代数

> Companion to [Module 0.7](./module-0.7-group-theory-and-lie-algebras.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 0.7](./module-0.7-group-theory-and-lie-algebras.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Rearrangement Theorem · 重排定理

**Claim.** Let G be a finite group of order |G|, and let g ∈ G be any fixed element. Then the map L_g : G → G defined by L_g(h) = g·h is a bijection. Equivalently, the multiset {g·h : h ∈ G} equals G as a set.

**命题。** 设 G 是阶为 |G| 的有限群，g ∈ G 为任意固定元素。则由 L_g(h) = g·h 定义的映射 L_g : G → G 是双射。等价地，多重集 {g·h : h ∈ G} 等于 G（作为集合）。

**Step 1 — Injectivity.** Suppose g·h₁ = g·h₂. Left-multiply both sides by g⁻¹ (which exists by the group axiom of inverses):

**第 1 步 — 单射性。** 设 g·h₁ = g·h₂。两侧同时左乘 g⁻¹（由逆元公理存在）：

  g⁻¹·(g·h₁) = g⁻¹·(g·h₂)
  (g⁻¹·g)·h₁ = (g⁻¹·g)·h₂   (associativity)
  e·h₁ = e·h₂                 (definition of inverse)
  h₁ = h₂.                    (definition of identity)

Hence L_g is injective.

故 L_g 是单射。

**Step 2 — Surjectivity.** For any target element k ∈ G, we need h such that g·h = k. Take h = g⁻¹·k, which lies in G by closure. Then g·h = g·(g⁻¹·k) = (g·g⁻¹)·k = e·k = k. So every element of G is hit — L_g is surjective.

**第 2 步 — 满射性。** 对任意目标元素 k ∈ G，需要找 h 使得 g·h = k。取 h = g⁻¹·k，由封闭性 h ∈ G。则 g·h = g·(g⁻¹·k) = (g·g⁻¹)·k = e·k = k。故 G 的每个元素都被取到——L_g 是满射。

**Step 3 — Conclusion.** L_g is both injective and surjective on a finite set, hence bijective. The set {g·h : h ∈ G} is the image of G under L_g, which equals G. ∎

**第 3 步 — 结论。** L_g 在有限集上既是单射又是满射，故为双射。集合 {g·h : h ∈ G} 是 G 在 L_g 下的像，等于 G。∎

**Remark.** The same argument applies to right multiplication R_g(h) = h·g. The rearrangement theorem is used in proving the orthogonality relations for characters: ∑_{g∈G} ρ_i(g)†_{mn} ρ_j(g)_{pq} = (|G|/d_i) δ_{ij} δ_{mp} δ_{nq}, where d_i is the dimension of irrep i.

**注记。** 同样的论证适用于右乘 R_g(h) = h·g。重排定理用于证明特征标的正交关系：∑_{g∈G} ρ_i(g)†_{mn} ρ_j(g)_{pq} = (|G|/d_i) δ_{ij} δ_{mp} δ_{nq}，其中 d_i 是不可约表示 i 的维数。

---

## B. Schur's Lemma · 舒尔引理

**Claim (Part 1).** Let ρ: G → GL(V) be an irreducible representation. If M: V → V is a linear map such that M ρ(g) = ρ(g) M for all g ∈ G, then M = λ I for some scalar λ ∈ C.

**命题（第 1 部分）。** 设 ρ: G → GL(V) 是不可约表示。若 M: V → V 是线性映射，对所有 g ∈ G 满足 M ρ(g) = ρ(g) M，则 M = λ I，λ ∈ C 为某标量。

**Step 1 — M has an eigenvalue.** Since V is a finite-dimensional complex vector space, the characteristic polynomial det(M − λ I) = 0 has at least one root λ ∈ C by the fundamental theorem of algebra. Let λ be such an eigenvalue.

**第 1 步 — M 有本征值。** 由于 V 是有限维复向量空间，特征多项式 det(M − λ I) = 0 由代数基本定理至少有一个根 λ ∈ C。设 λ 为此本征值。

**Step 2 — The kernel of (M − λI) is G-invariant.** Let W = ker(M − λ I) = {v ∈ V : Mv = λv} be the eigenspace. For any w ∈ W and any g ∈ G:

**第 2 步 — (M − λI) 的核是 G-不变的。** 设 W = ker(M − λ I) = {v ∈ V : Mv = λv} 为本征空间。对任意 w ∈ W 和任意 g ∈ G：

  M (ρ(g) w) = ρ(g) (M w)   (the intertwining condition)
             = ρ(g) (λ w)   (since w ∈ W)
             = λ (ρ(g) w).

So ρ(g)w ∈ W for every g. That is, W is a G-invariant subspace of V.

故 ρ(g)w ∈ W 对每个 g 成立。即 W 是 V 的 G-不变子空间。

**Step 3 — Irreducibility forces W = V.** Since ρ is irreducible, the only G-invariant subspaces of V are {0} and V itself. We have W ≠ {0} because eigenspaces are non-trivial. Therefore W = V, meaning M v = λ v for all v ∈ V, i.e. M = λ I. ∎

**第 3 步 — 不可约性迫使 W = V。** 由于 ρ 是不可约的，V 的唯一 G-不变子空间是 {0} 和 V 本身。我们有 W ≠ {0}，因为本征空间非平凡。故 W = V，即对所有 v ∈ V 有 M v = λ v，亦即 M = λ I。∎

**Claim (Part 2).** Let ρ_i: G → GL(V_i) and ρ_j: G → GL(V_j) be two irreducible representations that are not isomorphic. If M: V_j → V_i is a linear map such that M ρ_j(g) = ρ_i(g) M for all g ∈ G, then M = 0.

**命题（第 2 部分）。** 设 ρ_i: G → GL(V_i) 和 ρ_j: G → GL(V_j) 是两个不同构的不可约表示。若 M: V_j → V_i 是线性映射，对所有 g ∈ G 满足 M ρ_j(g) = ρ_i(g) M，则 M = 0。

**Step 1 — ker(M) is G-invariant in V_j.** For any w ∈ ker(M) and g ∈ G: M(ρ_j(g)w) = ρ_i(g)(Mw) = ρ_i(g)·0 = 0. So ρ_j(g)w ∈ ker(M), making ker(M) a G-invariant subspace of V_j.

**第 1 步 — ker(M) 在 V_j 中是 G-不变的。** 对任意 w ∈ ker(M) 和 g ∈ G：M(ρ_j(g)w) = ρ_i(g)(Mw) = ρ_i(g)·0 = 0。故 ρ_j(g)w ∈ ker(M)，使 ker(M) 成为 V_j 的 G-不变子空间。

**Step 2 — im(M) is G-invariant in V_i.** For any vector M(w) ∈ im(M) and g ∈ G: ρ_i(g)(Mw) = M(ρ_j(g)w) ∈ im(M). So im(M) is a G-invariant subspace of V_i.

**第 2 步 — im(M) 在 V_i 中是 G-不变的。** 对任意向量 M(w) ∈ im(M) 和 g ∈ G：ρ_i(g)(Mw) = M(ρ_j(g)w) ∈ im(M)。故 im(M) 是 V_i 的 G-不变子空间。

**Step 3 — Only two possibilities.** By irreducibility, ker(M) is either {0} or V_j, and im(M) is either {0} or V_i.

- If ker(M) = {0} and im(M) = V_i, then M is an isomorphism V_j → V_i, contradicting the assumption that ρ_i and ρ_j are non-isomorphic.
- Therefore at least one of ker(M) = V_j or im(M) = {0} must hold, both of which give M = 0. ∎

**第 3 步 — 只有两种可能。** 由不可约性，ker(M) 为 {0} 或 V_j，im(M) 为 {0} 或 V_i。

- 若 ker(M) = {0} 且 im(M) = V_i，则 M 是同构 V_j → V_i，与 ρ_i 和 ρ_j 不同构的假设矛盾。
- 因此 ker(M) = V_j 或 im(M) = {0} 中至少一个成立，两种情况都给出 M = 0。∎

---

## C. The su(2) Algebra and Classification of Its Irreps · su(2) 代数及其不可约表示的分类

**Claim.** The commutation relations [J_i, J_j] = i ε_{ijk} J_k (with ε_{ijk} the Levi-Civita symbol) define the Lie algebra su(2). The irreducible representations are labelled by j = 0, ½, 1, 3/2, …, have dimension 2j+1, and are uniquely characterized by the Casimir eigenvalue J² = j(j+1).

**命题。** 对易关系 [J_i, J_j] = i ε_{ijk} J_k（ε_{ijk} 为列维-奇维塔符号）定义了李代数 su(2)。不可约表示由 j = 0, ½, 1, 3/2, … 标记，维数为 2j+1，并由卡西米尔本征值 J² = j(j+1) 唯一刻画。

### C.1 Derivation of [J_i, J_j] = i ε_{ijk} J_k from the Pauli matrices · 从泡利矩阵推导 [J_i, J_j] = i ε_{ijk} J_k

**Step 1 — Define the generators.** Set J_i = σ_i / 2 where

**第 1 步 — 定义生成元。** 令 J_i = σ_i / 2，其中

  σ_1 = [[0, 1], [1, 0]],  σ_2 = [[0, −i], [i, 0]],  σ_3 = [[1, 0], [0, −1]].

**Step 2 — Compute the key product identity.** For any two Pauli matrices:

**第 2 步 — 计算关键乘积恒等式。** 对任意两个泡利矩阵：

  σ_i σ_j = δ_{ij} I + i ε_{ijk} σ_k.

Proof by explicit computation: σ_1 σ_2 = [[0,1],[1,0]][[0,−i],[i,0]] = [[i,0],[0,−i]] = i σ_3, which matches i ε_{12k} σ_k = i ε_{123} σ_3 = i σ_3. The other independent products follow by cyclic symmetry (1→2→3→1), and diagonal products: σ_1² = [[1,0],[0,1]] = I, confirming δ_{11} I = I.

通过显式计算证明：σ_1 σ_2 = [[0,1],[1,0]][[0,−i],[i,0]] = [[i,0],[0,−i]] = i σ_3，与 i ε_{12k} σ_k = i ε_{123} σ_3 = i σ_3 吻合。其余独立乘积由循环对称性（1→2→3→1）给出，对角乘积：σ_1² = I，确认 δ_{11} I = I。

**Step 3 — Extract the commutator.** The commutator [σ_i, σ_j] = σ_i σ_j − σ_j σ_i. Using Step 2:

**第 3 步 — 提取对易子。** 对易子 [σ_i, σ_j] = σ_i σ_j − σ_j σ_i。利用第 2 步：

  σ_i σ_j − σ_j σ_i = (δ_{ij} I + i ε_{ijk} σ_k) − (δ_{ji} I + i ε_{jik} σ_k)
                     = i ε_{ijk} σ_k − i ε_{jik} σ_k
                     = i (ε_{ijk} + ε_{ijk}) σ_k        (since ε_{jik} = −ε_{ijk})
                     = 2i ε_{ijk} σ_k.

So [σ_i, σ_j] = 2i ε_{ijk} σ_k, and dividing by 4 (since J_i = σ_i/2):

故 [σ_i, σ_j] = 2i ε_{ijk} σ_k，除以 4（因为 J_i = σ_i/2）：

  **[J_i, J_j] = i ε_{ijk} J_k**. ∎

### C.2 The Casimir Operator · 卡西米尔算符

**Step 1 — Define J² = J_1² + J_2² + J_3².** Compute [J², J_3]:

**第 1 步 — 定义 J² = J_1² + J_2² + J_3²。** 计算 [J², J_3]：

  [J², J_3] = [J_1², J_3] + [J_2², J_3] + [J_3², J_3].

Since [J_3², J_3] = 0, only the first two terms contribute. Use [AB, C] = A[B,C] + [A,C]B:

由于 [J_3², J_3] = 0，只有前两项有贡献。利用 [AB, C] = A[B,C] + [A,C]B：

  [J_1², J_3] = J_1[J_1, J_3] + [J_1, J_3]J_1 = J_1(−i J_2) + (−i J_2)J_1 = −i(J_1 J_2 + J_2 J_1)
  [J_2², J_3] = J_2[J_2, J_3] + [J_2, J_3]J_2 = J_2(i J_1) + (i J_1)J_2  = +i(J_2 J_1 + J_1 J_2).

Adding: [J², J_3] = −i(J_1 J_2 + J_2 J_1) + i(J_1 J_2 + J_2 J_1) = 0.

相加：[J², J_3] = 0。

The same calculation with cyclic relabelling gives [J², J_1] = [J², J_2] = 0. Therefore **[J², J_i] = 0 for all i**: J² is a Casimir operator.

对 J_1, J_2 的循环重标记给出同样结果，故 **[J², J_i] = 0** 对所有 i 成立：J² 是卡西米尔算符。

### C.3 Ladder operators and the irrep spectrum · 阶梯算符与不可约表示谱

**Step 1 — Define raising/lowering operators.** Let J_± = J_1 ± i J_2. Then:

**第 1 步 — 定义升降算符。** 令 J_± = J_1 ± i J_2。则：

  [J_3, J_+] = [J_3, J_1] + i[J_3, J_2] = i J_2 + i(−i J_1) = i J_2 + J_1 = J_+
  [J_3, J_−] = −J_−
  [J_+, J_−] = [J_1 + iJ_2, J_1 − iJ_2] = −i[J_1, J_2] + i[J_2, J_1] = −i(i J_3) + i(−i J_3) = 2J_3.

**Step 2 — Ladder action.** Let |j, m⟩ be a simultaneous eigenstate: J²|j,m⟩ = λ|j,m⟩ and J_3|j,m⟩ = m|j,m⟩. Then:

**第 2 步 — 阶梯作用。** 设 |j, m⟩ 是同时本征态：J²|j,m⟩ = λ|j,m⟩，J_3|j,m⟩ = m|j,m⟩。则：

  J_3 (J_+ |j,m⟩) = (J_+ J_3 + [J_3, J_+])|j,m⟩ = (m + 1)(J_+|j,m⟩).

So J_+ raises m by 1; similarly J_− lowers m by 1.

故 J_+ 将 m 提升 1；类似地 J_− 将 m 降低 1。

**Step 3 — The spectrum is bounded.** The norm of J_+|j,m⟩ satisfies

**第 3 步 — 谱有界。** J_+|j,m⟩ 的范数满足

  ‖J_+|j,m⟩‖² = ⟨j,m|J_−J_+|j,m⟩ = ⟨j,m|(J² − J_3² − J_3)|j,m⟩ = λ − m² − m ≥ 0

  ‖J_−|j,m⟩‖² = ⟨j,m|J_+J_−|j,m⟩ = ⟨j,m|(J² − J_3² + J_3)|j,m⟩ = λ − m² + m ≥ 0.

These two inequalities together require λ ≥ m² + |m|. So for fixed λ, the values of m are bounded above and below.

这两个不等式合在一起要求 λ ≥ m² + |m|。故对固定的 λ，m 的值有上下界。

**Step 4 — Termination conditions.** Let m_max be the maximum value of m. Then J_+|j, m_max⟩ = 0, so ‖J_+|j,m_max⟩‖² = λ − m_max² − m_max = 0, giving λ = m_max(m_max + 1). Similarly J_−|j, m_min⟩ = 0 gives λ = m_min(m_min − 1). Setting these equal: m_max(m_max + 1) = m_min(m_min − 1), which has the solution m_min = −m_max (discarding the extraneous root m_min = m_max + 1).

**第 4 步 — 终止条件。** 设 m_max 为 m 的最大值。则 J_+|j, m_max⟩ = 0，故 ‖J_+|j,m_max⟩‖² = λ − m_max² − m_max = 0，给出 λ = m_max(m_max + 1)。类似地 J_−|j, m_min⟩ = 0 给出 λ = m_min(m_min − 1)。令两者相等：m_max(m_max + 1) = m_min(m_min − 1)，解为 m_min = −m_max（舍去多余根 m_min = m_max + 1）。

**Step 5 — Quantization of j.** Since m steps by integers from m_min = −j to m_max = j (writing j ≡ m_max), the total number of steps j − (−j) = 2j must be a non-negative integer, so **j = 0, ½, 1, 3/2, …** The dimension of the irrep is the number of m values: **dim = 2j + 1**. The Casimir eigenvalue is **λ = j(j+1)**. ∎

**第 5 步 — j 的量子化。** 由于 m 从 m_min = −j 到 m_max = j（记 j ≡ m_max）以整数步长变化，步数总数 j − (−j) = 2j 必须是非负整数，故 **j = 0, ½, 1, 3/2, …** 不可约表示的维数是 m 值的个数：**dim = 2j + 1**。卡西米尔本征值为 **λ = j(j+1)**。∎

---

## D. The su(3) Gell-Mann Matrices and Structure Constants · su(3) 的 Gell-Mann 矩阵与结构常数

**Claim.** The Lie algebra su(3) has rank 2 and dimension 8. It is generated by eight traceless Hermitian 3×3 matrices λ_a (the Gell-Mann matrices) with commutation relations [λ_a/2, λ_b/2] = i f_{abc} λ_c/2, and possesses two independent Casimir operators.

**命题。** 李代数 su(3) 的秩为 2，维数为 8。它由八个无迹厄米 3×3 矩阵 λ_a（Gell-Mann 矩阵）生成，对易关系为 [λ_a/2, λ_b/2] = i f_{abc} λ_c/2，并具有两个独立的卡西米尔算符。

**Step 1 — Counting generators.** The Lie algebra su(n) consists of all n×n traceless skew-Hermitian matrices (equivalently, i times traceless Hermitian matrices). The dimension of su(n) is n² − 1 (the dimension of SU(n) as a manifold). For n = 3: dimension = 9 − 1 = **8 generators**.

**第 1 步 — 计算生成元数目。** 李代数 su(n) 由所有 n×n 无迹反厄米矩阵（等价地，i 乘以无迹厄米矩阵）组成。su(n) 的维数为 n² − 1（SU(n) 作为流形的维数）。对 n = 3：维数 = 9 − 1 = **8 个生成元**。

**Step 2 — The rank.** The rank of a Lie algebra is the dimension of a maximal abelian subalgebra (a Cartan subalgebra) of simultaneously diagonalizable generators. For su(3), two generators can be simultaneously diagonalized: λ_3 = diag(1,−1,0) and λ_8 = diag(1,1,−2)/√3. So **rank(su(3)) = 2**, and there are exactly **two Casimir operators**.

**第 2 步 — 秩。** 李代数的秩是可同时对角化生成元（嘉当子代数）的极大阿贝尔子代数的维数。对 su(3)，可同时对角化两个生成元：λ_3 = diag(1,−1,0) 和 λ_8 = diag(1,1,−2)/√3。故 **rank(su(3)) = 2**，恰好有**两个卡西米尔算符**。

**Step 3 — The eight Gell-Mann matrices.** An explicit basis of traceless Hermitian 3×3 matrices generalizing the Pauli matrices:

**第 3 步 — 八个 Gell-Mann 矩阵。** 推广泡利矩阵的无迹厄米 3×3 矩阵的显式基：

  λ_1 = [[0,1,0],[1,0,0],[0,0,0]]       λ_2 = [[0,−i,0],[i,0,0],[0,0,0]]
  λ_3 = [[1,0,0],[0,−1,0],[0,0,0]]      λ_4 = [[0,0,1],[0,0,0],[1,0,0]]
  λ_5 = [[0,0,−i],[0,0,0],[i,0,0]]      λ_6 = [[0,0,0],[0,0,1],[0,1,0]]
  λ_7 = [[0,0,0],[0,0,−i],[0,i,0]]      λ_8 = (1/√3) [[1,0,0],[0,1,0],[0,0,−2]]

They satisfy Tr(λ_a λ_b) = 2 δ_{ab}, the normalization condition. Note that λ_1, λ_2, λ_3 form an su(2) subalgebra (the isospin subgroup), and λ_4, …, λ_7 connect the third component.

它们满足 Tr(λ_a λ_b) = 2 δ_{ab}，即归一化条件。注意 λ_1, λ_2, λ_3 构成 su(2) 子代数（同位旋子群），λ_4, …, λ_7 连接第三分量。

**Step 4 — Structure constants from the commutators.** Compute [λ_a, λ_b] = 2i f_{abc} λ_c directly:

**第 4 步 — 从对易子得结构常数。** 直接计算 [λ_a, λ_b] = 2i f_{abc} λ_c：

  [λ_1, λ_2] = 2[[0,1,0],[1,0,0],[0,0,0]] [[0,−i,0],[i,0,0],[0,0,0]] − h.c. = 2i λ_3  →  f_{123} = 1
  [λ_1, λ_4] = 2i (½) λ_7  →  f_{147} = ½
  [λ_2, λ_6] = 2i (½) λ_7  →  f_{267} = ½  (and so on by explicit matrix multiplication)
  [λ_4, λ_5] = 2i (½) λ_3 + 2i (√3/2) λ_8  →  f_{458} = √3/2.

The non-zero independent values are: f_{123} = 1; f_{147} = f_{156} = f_{246} = f_{257} = f_{345} = f_{367} = ½ (with appropriate signs from antisymmetry); f_{458} = f_{678} = √3/2. All other f_{abc} are zero or related by total antisymmetry f_{abc} = −f_{bac} = −f_{acb}.

非零独立值为：f_{123} = 1；f_{147} = f_{156} = f_{246} = f_{257} = f_{345} = f_{367} = ½（考虑反对称性的正负号）；f_{458} = f_{678} = √3/2。其余 f_{abc} 为零或由全反对称性 f_{abc} = −f_{bac} = −f_{acb} 相关。

**Step 5 — The two Casimir operators.** The quadratic Casimir is

**第 5 步 — 两个卡西米尔算符。** 二次卡西米尔算符为

  C_2 = ∑_{a=1}^{8} (λ_a/2)²

and the cubic Casimir uses the symmetric structure constants d_{abc} defined by {λ_a, λ_b} = (4/3) δ_{ab} I + 2 d_{abc} λ_c:

三次卡西米尔算符使用对称结构常数 d_{abc}，由 {λ_a, λ_b} = (4/3) δ_{ab} I + 2 d_{abc} λ_c 定义：

  C_3 = ∑_{a,b,c} d_{abc} (λ_a/2)(λ_b/2)(λ_c/2).

On the fundamental representation 3: C_2 = (4/3) I. On the adjoint representation 8: C_2 = 3 I. By Schur's lemma each Casimir is a multiple of the identity on every irrep, and together (C_2, C_3) uniquely label the irrep (p, q). ∎

在基本表示 3 上：C_2 = (4/3) I。在伴随表示 8 上：C_2 = 3 I。由舒尔引理，每个卡西米尔算符在每个不可约表示上是单位矩阵的倍数，(C_2, C_3) 合在一起唯一标记不可约表示 (p, q)。∎

---

## E. The Exponential Map and Hermiticity of Generators · 指数映射与生成元的厄米性

**Claim.** For a Lie group G with unitary representations ρ(g)†ρ(g) = I, the generators T_a defined by ρ(exp(i θ_a T_a)) near the identity must satisfy T_a† = T_a (Hermitian). Conversely, any Hermitian matrix H generates a one-parameter unitary group exp(i t H).

**命题。** 对于具有酉表示 ρ(g)†ρ(g) = I 的李群 G，在单位元附近由 ρ(exp(i θ_a T_a)) 定义的生成元 T_a 必满足 T_a† = T_a（厄米性）。反之，任意厄米矩阵 H 生成单参数酉群 exp(i t H)。

**Step 1 — Parameterize near the identity.** Consider a one-parameter subgroup g(t) = exp(i t T) for a single generator T and real parameter t. At t = 0, g(0) = I. Differentiating:

**第 1 步 — 在单位元附近参数化。** 考虑单个生成元 T 和实参数 t 的单参数子群 g(t) = exp(i t T)。在 t = 0 时，g(0) = I。对 t 微分：

  d/dt [g(t)] |_{t=0} = i T.

**Step 2 — Unitarity constraint.** Require g(t)†g(t) = I for all t. Differentiate with respect to t and evaluate at t = 0:

**第 2 步 — 酉性约束。** 要求对所有 t 有 g(t)†g(t) = I。对 t 微分并在 t = 0 处求值：

  d/dt [g(t)† g(t)] |_{t=0} = (d/dt g(t)†)|_{t=0} · g(0) + g(0)† · (d/dt g(t))|_{t=0}
                             = (iT)† · I + I · (iT)
                             = −iT† + iT = 0.

Therefore **T† = T**: the generator is Hermitian.

故 **T† = T**：生成元是厄米的。

**Step 3 — Converse: Hermitian implies unitary.** Let T = T† be Hermitian. Then:

**第 3 步 — 逆命题：厄米蕴含酉性。** 设 T = T† 为厄米矩阵。则：

  (exp(i t T))† = exp(−i t T†) = exp(−i t T) = (exp(i t T))⁻¹.

(The first equality uses (e^A)† = e^{A†}, proved by taking the adjoint of the power series; the second uses T† = T; the third uses exp(A)exp(−A) = I.) Hence exp(i t T) is unitary for all real t.

（第一个等式利用 (e^A)† = e^{A†}，通过对幂级数取伴随证明；第二个利用 T† = T；第三个利用 exp(A)exp(−A) = I。）故对所有实数 t，exp(i t T) 是酉矩阵。

**Step 4 — Convergence and the Baker–Campbell–Hausdorff formula.** The matrix exponential exp(A) = ∑_{n=0}^∞ Aⁿ/n! converges absolutely for any finite-dimensional matrix A (since ‖Aⁿ‖ ≤ ‖A‖ⁿ and ∑ ‖A‖ⁿ/n! = exp(‖A‖) < ∞). For two generators, exp(i α T_a) exp(i β T_b) ≠ exp(i(α T_a + β T_b)) in general; the **Baker–Campbell–Hausdorff (BCH) formula** gives the correction:

**第 4 步 — 收敛性与 Baker–Campbell–Hausdorff 公式。** 矩阵指数 exp(A) = ∑_{n=0}^∞ Aⁿ/n! 对任意有限维矩阵 A 绝对收敛（因为 ‖Aⁿ‖ ≤ ‖A‖ⁿ，且 ∑ ‖A‖ⁿ/n! = exp(‖A‖) < ∞）。对两个生成元，一般有 exp(i α T_a) exp(i β T_b) ≠ exp(i(α T_a + β T_b))；**Baker–Campbell–Hausdorff (BCH) 公式**给出修正：

  exp(X) exp(Y) = exp(X + Y + ½[X,Y] + (1/12)([X,[X,Y]] − [Y,[X,Y]]) + …)

The key point is that the exponent involves only commutators (i.e., the Lie algebra structure), showing that the local group structure near the identity is entirely encoded in the Lie algebra. ∎

关键在于指数中仅涉及对易子（即李代数结构），表明单位元附近的局部群结构完全编码在李代数中。∎

---

*These derivations establish the algebraic foundations used in Module 3.11 (angular momentum), Module 8.1 (gauge theory), and Module 8.3 (QCD and the quark model).*

*这些推导确立了模块 3.11（角动量）、模块 8.1（规范理论）和模块 8.3（量子色动力学与夸克模型）所用的代数基础。*

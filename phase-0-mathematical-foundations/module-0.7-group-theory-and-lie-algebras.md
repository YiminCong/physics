# Module 0.7 — Group Theory & Lie Algebras ⭐
**模块 0.7 — 群论与李代数 ⭐**

> **Phase 0 — [Mathematical Foundations](./README.md)** · Format: Definition → Demonstration → Application
> **第 0 阶段 — 数学基础** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-0.7-group-theory-and-lie-algebras-derivations.md)

---

## 1. Groups & Representations · 群与表示

**Definition.** A **group** G is a set together with a binary operation · satisfying four axioms: (i) **closure** — for all a, b in G, a·b is in G; (ii) **associativity** — (a·b)·c = a·(b·c); (iii) **identity** — there exists e in G such that e·a = a·e = a for all a; (iv) **inverses** — for each a there exists a⁻¹ such that a·a⁻¹ = a⁻¹·a = e. If a·b = b·a for all elements, the group is **abelian** (commutative).

**定义。** **群** G 是一个配备了二元运算 · 的集合，满足四条公理：(i) **封闭性**——对所有 a, b ∈ G，a·b ∈ G；(ii) **结合律**——(a·b)·c = a·(b·c)；(iii) **单位元**——存在 e ∈ G，使得对所有 a 有 e·a = a·e = a；(iv) **逆元**——对每个 a 存在 a⁻¹，使得 a·a⁻¹ = a⁻¹·a = e。若对所有元素都有 a·b = b·a，则该群是**阿贝尔群**（交换群）。

Key examples: the **cyclic group** Z_n = {0, 1, …, n−1} under addition mod n (symmetry of a regular n-gon, abelian); the **permutation group** S_n of all n! bijections on n objects (non-abelian for n ≥ 3); the **special unitary groups** SU(2) (2×2 unitary matrices of determinant 1, the double cover of 3D rotations) and SU(3) (3×3 unitary matrices of determinant 1, the symmetry group of the strong force); and the **Lorentz group** O(1,3) of all linear transformations preserving the Minkowski interval ds² = −dt² + dx² + dy² + dz² (non-compact, non-abelian).

主要例子：**循环群** Z_n = {0, 1, …, n−1}，按模 n 加法运算（正 n 边形的对称性，阿贝尔群）；**置换群** S_n，包含 n 个对象上所有 n! 个双射（n ≥ 3 时非阿贝尔）；**特殊酉群** SU(2)（行列式为 1 的 2×2 酉矩阵，三维旋转的二重覆盖）和 SU(3)（行列式为 1 的 3×3 酉矩阵，强力的对称群）；以及**洛伦兹群** O(1,3)，包含所有保持闵可夫斯基间隔 ds² = −dt² + dx² + dy² + dz² 不变的线性变换（非紧致，非阿贝尔）。

A **representation** of G is a group homomorphism ρ: G → GL(V) — a map from G to invertible linear transformations on a vector space V — that respects the group structure: ρ(a·b) = ρ(a) ρ(b). An **irreducible representation** (irrep) cannot be decomposed into smaller invariant subspaces. The **character** of a representation is the function χ(g) = Tr[ρ(g)], which is class-function (constant on conjugacy classes) and completely classifies irreps up to equivalence. **Schur's lemma** gives the key constraint: any linear map that commutes with every element of an irrep must be a scalar multiple of the identity. Two corollaries follow: (1) a matrix commuting with all matrices of an irrep is λI; (2) homomorphisms between two inequivalent irreps are zero.

群 G 的**表示**是一个群同态 ρ: G → GL(V)——从 G 到向量空间 V 上可逆线性变换的映射——保持群结构：ρ(a·b) = ρ(a) ρ(b)。**不可约表示**（不可约表示）不能分解为更小的不变子空间。表示的**特征标**是函数 χ(g) = Tr[ρ(g)]，它是类函数（在共轭类上取常值），并完全将不可约表示分类至等价意义下。**舒尔引理**给出关键约束：与不可约表示每个元素对易的任意线性映射必为单位矩阵的标量倍。由此推出两个推论：(1) 与不可约表示所有矩阵对易的矩阵为 λI；(2) 两个不等价不可约表示之间的同态为零。

**Demonstration.** The rearrangement theorem states that multiplying every element of a group by a fixed element g merely permutes the list — the set {g·h : h ∈ G} equals G. This seemingly trivial fact underlies the proof of orthogonality relations for characters: ∑_{g∈G} χ_i(g)* χ_j(g) = |G| δ_{ij}, where the sum is over all group elements and i, j label irreps. For the group Z_3 = {e, r, r²} (cyclic, order 3), there are three one-dimensional irreps with characters χ_k(rⁿ) = e^{2πikn/3} for k = 0, 1, 2.

**演示。** 重排定理指出，用固定元素 g 乘以群的每个元素只是将列表重新排列——集合 {g·h : h ∈ G} 等于 G。这个看似简单的事实是特征标正交关系证明的基础：∑_{g∈G} χ_i(g)* χ_j(g) = |G| δ_{ij}，其中求和遍历所有群元素，i、j 标记不可约表示。对于群 Z_3 = {e, r, r²}（循环群，阶为 3），有三个一维不可约表示，特征标为 χ_k(rⁿ) = e^{2πikn/3}，k = 0, 1, 2。

**Application.** Representation theory dictates which physical states can mix and which selection rules forbid transitions. In atomic physics, the irreps of SO(3) (the rotation group) are labelled by integer angular momentum l, and their dimensions 2l+1 are the familiar degeneracy counts. The orthogonality of characters produces the selection rules ∆l = ±1 for electric-dipole transitions. The irreps of SU(3) classify the hadron multiplets (Module 8.3): the fundamental 3 and 3-bar, the adjoint 8, and the decuplet 10. Schur's lemma is invoked constantly — any operator that commutes with all generators of a symmetry group is a multiple of the identity on each irrep, making it the mathematical reason conserved quantities take definite values in symmetric states.

**应用。** 表示论决定了哪些物理态可以混合，哪些选择定则禁止跃迁。在原子物理中，SO(3)（旋转群）的不可约表示由整数角动量 l 标记，其维数 2l+1 是熟知的简并度计数。特征标的正交性产生电偶极跃迁的选择定则 ∆l = ±1。SU(3) 的不可约表示对强子多重态进行分类（模块 8.3）：基本表示 3 和反 3、伴随表示 8 以及十重态 10。舒尔引理被频繁引用——任何与对称群所有生成元对易的算符，在每个不可约表示上都是单位矩阵的倍数，这从数学上说明了为何守恒量在对称态中取确定值。

---

## 2. Lie Groups & Lie Algebras · 李群与李代数

**Definition.** A **Lie group** is a group that is simultaneously a smooth manifold, meaning the group operations (multiplication and inversion) are smooth maps. The physically important ones are **continuous symmetry groups**: SO(3) (3D rotations), SU(2), SU(3), and the Lorentz/Poincaré groups. Near the identity, any Lie group element can be written using **generators** T_a as

**定义。** **李群**是同时是光滑流形的群，这意味着群运算（乘法和求逆）是光滑映射。物理上重要的李群是**连续对称群**：SO(3)（三维旋转）、SU(2)、SU(3) 以及洛伦兹/庞加莱群。在单位元附近，任何李群元素都可以用**生成元** T_a 写成

  g = exp(i θ_a T_a)

where θ_a are real parameters (angles, rapidity, etc.) and the sum over a is implied. The generators T_a form the **Lie algebra** g of the group: a vector space equipped with the **Lie bracket** (commutator)

其中 θ_a 是实参数（角度、快度等），对 a 求和。生成元 T_a 构成群的**李代数** g：一个配备了**李括号**（对易子）的向量空间

  [T_a, T_b] = i f_{abc} T_c

where f_{abc} are the **structure constants** — real numbers that entirely determine the local structure of the group. The structure constants are totally antisymmetric: f_{abc} = −f_{bac}, and satisfy the **Jacobi identity** which follows from the associativity of the group.

其中 f_{abc} 是**结构常数**——完全决定群局部结构的实数。结构常数是全反对称的：f_{abc} = −f_{bac}，并满足**雅可比恒等式**，后者由群的结合律导出。

For **su(2)** — the Lie algebra of SU(2) — the generators are J_i = σ_i/2 where σ_i are the Pauli matrices (Module 0.2, Module 3.11):

  σ_1 = [[0,1],[1,0]],  σ_2 = [[0,−i],[i,0]],  σ_3 = [[1,0],[0,−1]]

The commutation relations are [J_i, J_j] = i ε_{ijk} J_k, where ε_{ijk} is the Levi-Civita symbol — so the structure constants of su(2) are f_{ijk} = ε_{ijk}. The **Casimir operator** J² = J_1² + J_2² + J_3² commutes with all generators, [J², J_i] = 0, and by Schur's lemma takes a fixed value on each irrep. The irreps of su(2) are labelled by j = 0, ½, 1, 3/2, …, with dimension 2j+1 and Casimir eigenvalue j(j+1). This is the entire algebraic theory of angular momentum (Module 3.11).

对于 **su(2)**——SU(2) 的李代数——生成元为 J_i = σ_i/2，其中 σ_i 是泡利矩阵（模块 0.2、模块 3.11）。对易关系为 [J_i, J_j] = i ε_{ijk} J_k，其中 ε_{ijk} 是列维-奇维塔符号——因此 su(2) 的结构常数为 f_{ijk} = ε_{ijk}。**卡西米尔算符** J² = J_1² + J_2² + J_3² 与所有生成元对易，[J², J_i] = 0，由舒尔引理在每个不可约表示上取固定值。su(2) 的不可约表示由 j = 0, ½, 1, 3/2, … 标记，维数为 2j+1，卡西米尔本征值为 j(j+1)。这就是角动量的完整代数理论（模块 3.11）。

For **su(3)** — the Lie algebra of SU(3) — there are eight generators λ_a/2, where λ_a are the **Gell-Mann matrices**: eight traceless Hermitian 3×3 matrices. The structure constants f_{abc} of su(3) are tabulated explicitly; the non-zero independent values include f_{123} = 1, f_{147} = f_{516} = f_{246} = f_{257} = f_{345} = ½, f_{458} = f_{678} = √3/2. The su(3) algebra has **two independent Casimir operators** (since its rank is 2): C_2 = ∑_a (λ_a/2)² and C_3 = ∑_{abc} d_{abc} (λ_a/2)(λ_b/2)(λ_c/2), where d_{abc} are the symmetric structure constants. The irreps of su(3) are labelled by two non-negative integers (p, q); the fundamental 3 is (1,0), its conjugate 3-bar is (0,1), and the adjoint 8 is (1,1).

对于 **su(3)**——SU(3) 的李代数——有八个生成元 λ_a/2，其中 λ_a 是 **Gell-Mann 矩阵**：八个无迹厄米 3×3 矩阵。su(3) 的结构常数 f_{abc} 有明确的列表；非零独立值包括 f_{123} = 1，f_{147} = f_{516} = f_{246} = f_{257} = f_{345} = ½，f_{458} = f_{678} = √3/2。su(3) 代数有**两个独立的卡西米尔算符**（因为其秩为 2）：C_2 = ∑_a (λ_a/2)² 和 C_3 = ∑_{abc} d_{abc} (λ_a/2)(λ_b/2)(λ_c/2)，其中 d_{abc} 是对称结构常数。su(3) 的不可约表示由两个非负整数 (p, q) 标记；基本表示 3 是 (1,0)，其共轭表示 3-bar 是 (0,1)，伴随表示 8 是 (1,1)。

The **exponential map** g = exp(i θ_a T_a) is the central bridge from the algebra to the group. For unitary representations (ρ(g)†ρ(g) = I for all g), differentiating at the identity forces the generators to be **Hermitian**: T_a† = T_a. This is why the Pauli matrices and Gell-Mann matrices are all Hermitian — any unitary matrix can be written as the exponential of i times a Hermitian matrix.

**指数映射** g = exp(i θ_a T_a) 是从代数到群的核心桥梁。对于酉表示（对所有 g 有 ρ(g)†ρ(g) = I），在单位元处微分迫使生成元必须是**厄米的**：T_a† = T_a。这就是为什么泡利矩阵和 Gell-Mann 矩阵都是厄米矩阵——任何酉矩阵都可以写成 i 乘以厄米矩阵的指数形式。

**Demonstration.** A finite rotation by angle θ about the z-axis in 3D is represented in SU(2) by the element exp(i θ J_3) = exp(i θ σ_3/2). Using σ_3² = I and expanding the exponential:

**演示。** 三维空间中绕 z 轴转动角度 θ 在 SU(2) 中由元素 exp(i θ J_3) = exp(i θ σ_3/2) 表示。利用 σ_3² = I 并展开指数：

  exp(i θ σ_3/2) = I cos(θ/2) + i σ_3 sin(θ/2) = [[e^{iθ/2}, 0], [0, e^{−iθ/2}]]

A full rotation θ = 2π gives exp(iπ σ_3) = −I, not +I — this is the famous spinor double-valuedness. A rotation by 4π is required to return to the identity, which is why spin-½ particles pick up a factor of −1 under a 2π rotation, observable in neutron interferometry.

完整旋转 θ = 2π 给出 exp(iπ σ_3) = −I，而非 +I——这就是著名的旋量双值性。需要旋转 4π 才能回到单位元，这就是为什么自旋 ½ 粒子在 2π 旋转下获得因子 −1，这在中子干涉测量中可以观测到。

**Application.** Group theory and Lie algebras are literally the language in which modern physics is written. **Angular momentum** (Module 3.11) is the representation theory of su(2): every spin-j multiplet is an irrep, addition of angular momenta is the tensor product of irreps, and Clebsch-Gordan coefficients are the decomposition. **Gauge theory** (Module 8.1) is built on Lie groups: the Standard Model gauge group is SU(3) × SU(2) × U(1), and the gauge bosons (gluons for SU(3), W/Z for SU(2)) live in the adjoint representations of their respective algebras. The Gell-Mann matrices of su(3) govern quantum chromodynamics (Module 8.3). The Lorentz group and its representations determine the spin content of all relativistic quantum fields (Module 6.2). Wherever a symmetry is continuous and exact, a Lie group is operating.

**应用。** 群论和李代数是现代物理学书写所用的语言。**角动量**（模块 3.11）就是 su(2) 的表示论：每个自旋 j 的多重态是一个不可约表示，角动量的合成是不可约表示的张量积，而克莱布施-高登系数是其分解。**规范理论**（模块 8.1）建立在李群之上：标准模型规范群为 SU(3) × SU(2) × U(1)，规范玻色子（SU(3) 的胶子，SU(2) 的 W/Z）处于各自代数的伴随表示中。su(3) 的 Gell-Mann 矩阵支配量子色动力学（模块 8.3）。洛伦兹群及其表示决定所有相对论量子场的自旋内容（模块 6.2）。只要对称性是连续且严格的，就有一个李群在运作。

---

## Module 0.7 Self-Test (blank page)

1. State the four group axioms. Verify that SU(2) satisfies them.
2. What is a group representation? What does "irreducible" mean?
3. State Schur's lemma (both parts) and give one consequence in physics.
4. Write the Lie algebra commutation relation [T_a, T_b] = i f_{abc} T_c and explain the role of the structure constants.
5. Write the su(2) commutation relations. What are the possible irreps and their dimensions?
6. What is the exponential map, and why must generators be Hermitian for unitary representations?
7. Name the Lie algebra of the Standard Model gauge group and identify which module covers each factor.

**自测（空白页）**

1. 陈述四条群公理。验证 SU(2) 满足它们。
2. 什么是群的表示？"不可约"是什么意思？
3. 陈述舒尔引理（两个部分），并给出一个物理中的推论。
4. 写出李代数对易关系 [T_a, T_b] = i f_{abc} T_c，并解释结构常数的作用。
5. 写出 su(2) 对易关系。可能的不可约表示有哪些，其维数是多少？
6. 什么是指数映射，为什么酉表示的生成元必须是厄米的？
7. 命名标准模型规范群的李代数，并指出哪个模块涵盖了每个因子。

---

← Previous: [Module 0.6 — Vector Calculus, Tensors & Differential Forms](./module-0.6-vector-calculus-tensors-and-differential-forms.md) · [Phase 0 index](./README.md)

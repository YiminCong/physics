# Derivations — Module 7.2: Tensors, the Metric & Curvature
# 推导 — 模块 7.2：张量、度规与曲率

> Companion to [Module 7.2](./module-7.2-tensors-metric-and-curvature.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.2](./module-7.2-tensors-metric-and-curvature.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Christoffel Symbols from Metric Compatibility and Torsion-Free Symmetry · 从度规相容性与无挠对称性推导克里斯托费尔符号

**Claim.** The unique connection compatible with the metric (∇_ρ g_{μν} = 0) and torsion-free (Γ^λ_{μν} = Γ^λ_{νμ}) is the Levi-Civita connection

  Γ^λ_{μν} = ½ g^{λσ}(∂_μ g_{νσ} + ∂_ν g_{μσ} − ∂_σ g_{μν}).

**命题。** 满足度规相容性（∇_ρ g_{μν} = 0）和无挠条件（Γ^λ_{μν} = Γ^λ_{νμ}）的唯一联络是列维-奇维塔联络

  Γ^λ_{μν} = ½ g^{λσ}(∂_μ g_{νσ} + ∂_ν g_{μσ} − ∂_σ g_{μν})。

**Step 1 — Write metric compatibility explicitly.** The covariant derivative of the metric tensor must vanish identically. For a (0,2) tensor, the covariant derivative is

**第 1 步 — 显式写出度规相容性。** 度规张量的协变导数必须恒为零。对于 (0,2) 型张量，协变导数为

  ∇_ρ g_{μν} = ∂_ρ g_{μν} − Γ^σ_{ρμ} g_{σν} − Γ^σ_{ρν} g_{μσ} = 0.

This single equation, written for all permutations of the indices (ρ, μ, ν), contains all the information needed to determine the connection uniquely once the torsion-free condition is imposed.

此方程对指标 (ρ, μ, ν) 的所有置换写出后，结合无挠条件，包含了唯一确定联络所需的全部信息。

**Step 2 — Write out three cyclic permutations.** Expand ∇_ρ g_{μν} = 0 for three distinct index assignments and label the results (I), (II), (III):

**第 2 步 — 写出三个循环置换。** 对三种不同的指标赋值展开 ∇_ρ g_{μν} = 0，将结果标记为 (I)、(II)、(III)：

  (I)   ∂_ρ g_{μν} − Γ^σ_{ρμ} g_{σν} − Γ^σ_{ρν} g_{μσ} = 0
  (II)  ∂_μ g_{νρ} − Γ^σ_{μν} g_{σρ} − Γ^σ_{μρ} g_{νσ} = 0
  (III) ∂_ν g_{ρμ} − Γ^σ_{νρ} g_{σμ} − Γ^σ_{νμ} g_{ρσ} = 0

**Step 3 — Use torsion-free symmetry.** The torsion tensor T^λ_{μν} = Γ^λ_{μν} − Γ^λ_{νμ} vanishes, so Γ^λ_{μν} = Γ^λ_{νμ} (symmetric in lower indices). Apply this throughout.

**第 3 步 — 使用无挠对称性。** 挠率张量 T^λ_{μν} = Γ^λ_{μν} − Γ^λ_{νμ} = 0，故 Γ^λ_{μν} = Γ^λ_{νμ}（关于下指标对称）。在整个推导中应用此条件。

**Step 4 — Linear combination: (II) + (III) − (I).** Compute (II) + (III) − (I):

**第 4 步 — 线性组合：(II) + (III) − (I)。** 计算 (II) + (III) − (I)：

  ∂_μ g_{νρ} + ∂_ν g_{ρμ} − ∂_ρ g_{μν}
  − Γ^σ_{μν} g_{σρ} − Γ^σ_{μρ} g_{νσ}
  − Γ^σ_{νρ} g_{σμ} − Γ^σ_{νμ} g_{ρσ}
  + Γ^σ_{ρμ} g_{σν} + Γ^σ_{ρν} g_{μσ} = 0.

Now apply the torsion-free condition: Γ^σ_{μν} = Γ^σ_{νμ}. The terms ±Γ^σ_{μρ} g_{νσ} and ±Γ^σ_{ρμ} g_{σν} cancel in pairs (since g_{σν} = g_{νσ}), as do ±Γ^σ_{νρ} g_{σμ} and ±Γ^σ_{ρν} g_{μσ}. What remains is:

现在应用无挠条件 Γ^σ_{μν} = Γ^σ_{νμ}。项 ±Γ^σ_{μρ} g_{νσ} 与 ±Γ^σ_{ρμ} g_{σν} 成对消去（因 g_{σν} = g_{νσ}），±Γ^σ_{νρ} g_{σμ} 与 ±Γ^σ_{ρν} g_{μσ} 同理消去。剩余项为：

  ∂_μ g_{νρ} + ∂_ν g_{ρμ} − ∂_ρ g_{μν} − 2 Γ^σ_{μν} g_{σρ} = 0.

**Step 5 — Isolate the Christoffel symbol.** Rearrange:

**第 5 步 — 分离克里斯托费尔符号。** 重新整理：

  2 Γ^σ_{μν} g_{σρ} = ∂_μ g_{νρ} + ∂_ν g_{ρμ} − ∂_ρ g_{μν}.

Multiply both sides by g^{ρλ} (the inverse metric, g^{ρλ} g_{σρ} = δ^λ_σ):

两边乘以 g^{ρλ}（逆度规，g^{ρλ} g_{σρ} = δ^λ_σ）：

  2 Γ^λ_{μν} = g^{ρλ}(∂_μ g_{νρ} + ∂_ν g_{ρμ} − ∂_ρ g_{μν}).

Relabeling the dummy index ρ → σ and dividing by 2:

将哑指标 ρ 重标记为 σ 并除以 2：

  **Γ^λ_{μν} = ½ g^{λσ}(∂_μ g_{νσ} + ∂_ν g_{μσ} − ∂_σ g_{μν}).**

**Step 6 — Uniqueness.** The derivation assumed only (a) ∇_ρ g_{μν} = 0 and (b) Γ^λ_{μν} = Γ^λ_{νμ}. Given these two conditions, the algebraic steps above are reversible: the Christoffel symbols are uniquely determined by the metric. This is the *fundamental theorem of Riemannian geometry*.

**第 6 步 — 唯一性。** 推导只用到了：(a) ∇_ρ g_{μν} = 0 和 (b) Γ^λ_{μν} = Γ^λ_{νμ}。给定这两个条件，上述代数步骤是可逆的：克里斯托费尔符号由度规唯一确定。这就是*黎曼几何基本定理*。

**Step 7 — Verify metric compatibility is satisfied.** Substitute the expression back into ∇_ρ g_{μν} = ∂_ρ g_{μν} − Γ^σ_{ρμ} g_{σν} − Γ^σ_{ρν} g_{μσ}. Inserting the Christoffel formula, the three derivative terms in each Γ produce six partial-derivative terms total; by direct cancellation using g^{σλ} g_{σν} = δ^λ_ν, all six cancel, confirming ∇_ρ g_{μν} = 0 identically. ∎

**第 7 步 — 验证度规相容性得到满足。** 将表达式代回 ∇_ρ g_{μν} = ∂_ρ g_{μν} − Γ^σ_{ρμ} g_{σν} − Γ^σ_{ρν} g_{μσ}。代入克里斯托费尔公式，每个 Γ 中的三个导数项共产生六个偏导数项；利用 g^{σλ} g_{σν} = δ^λ_ν 直接消去，所有六项相消，证实 ∇_ρ g_{μν} = 0 恒成立。∎

---

## B. The Riemann Tensor from the Commutator of Covariant Derivatives · 从协变导数对易子推导黎曼张量

**Claim.** For any contravariant vector V^ρ, the commutator of covariant derivatives satisfies

  [∇_μ, ∇_ν] V^ρ = R^ρ_{σμν} V^σ,

where the Riemann curvature tensor has components

  R^ρ_{σμν} = ∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} + Γ^ρ_{μλ} Γ^λ_{νσ} − Γ^ρ_{νλ} Γ^λ_{μσ}.

**命题。** 对任意逆变矢量 V^ρ，协变导数的对易子满足

  [∇_μ, ∇_ν] V^ρ = R^ρ_{σμν} V^σ，

其中黎曼曲率张量的分量为

  R^ρ_{σμν} = ∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} + Γ^ρ_{μλ} Γ^λ_{νσ} − Γ^ρ_{νλ} Γ^λ_{μσ}。

**Step 1 — Compute ∇_μ (∇_ν V^ρ).** Start from the definition of the covariant derivative of a (1,0) tensor:

**第 1 步 — 计算 ∇_μ (∇_ν V^ρ)。** 从 (1,0) 型张量的协变导数定义出发：

  ∇_ν V^ρ = ∂_ν V^ρ + Γ^ρ_{νσ} V^σ.

Now apply ∇_μ to this (1,1) tensor ∇_ν V^ρ. A (1,1) tensor W^ρ_ν has covariant derivative

  ∇_μ W^ρ_ν = ∂_μ W^ρ_ν + Γ^ρ_{μλ} W^λ_ν − Γ^λ_{μν} W^ρ_λ.

现在对 (1,1) 型张量 ∇_ν V^ρ 施加 ∇_μ。(1,1) 型张量 W^ρ_ν 的协变导数为

  ∇_μ W^ρ_ν = ∂_μ W^ρ_ν + Γ^ρ_{μλ} W^λ_ν − Γ^λ_{μν} W^ρ_λ。

Substituting W^ρ_ν = ∂_ν V^ρ + Γ^ρ_{νσ} V^σ:

代入 W^ρ_ν = ∂_ν V^ρ + Γ^ρ_{νσ} V^σ：

  ∇_μ ∇_ν V^ρ = ∂_μ(∂_ν V^ρ + Γ^ρ_{νσ} V^σ)
               + Γ^ρ_{μλ}(∂_ν V^λ + Γ^λ_{νσ} V^σ)
               − Γ^λ_{μν}(∂_λ V^ρ + Γ^ρ_{λσ} V^σ).

Expanding all terms:

展开所有项：

  = ∂_μ ∂_ν V^ρ + (∂_μ Γ^ρ_{νσ}) V^σ + Γ^ρ_{νσ} ∂_μ V^σ
  + Γ^ρ_{μλ} ∂_ν V^λ + Γ^ρ_{μλ} Γ^λ_{νσ} V^σ
  − Γ^λ_{μν} ∂_λ V^ρ − Γ^λ_{μν} Γ^ρ_{λσ} V^σ.

**Step 2 — Compute ∇_ν (∇_μ V^ρ) by swapping μ ↔ ν.** By identical algebra with μ and ν swapped:

**第 2 步 — 交换 μ ↔ ν 计算 ∇_ν (∇_μ V^ρ)。** 通过交换 μ 与 ν 的相同代数运算：

  ∇_ν ∇_μ V^ρ = ∂_ν ∂_μ V^ρ + (∂_ν Γ^ρ_{μσ}) V^σ + Γ^ρ_{μσ} ∂_ν V^σ
  + Γ^ρ_{νλ} ∂_μ V^λ + Γ^ρ_{νλ} Γ^λ_{μσ} V^σ
  − Γ^λ_{νμ} ∂_λ V^ρ − Γ^λ_{νμ} Γ^ρ_{λσ} V^σ.

**Step 3 — Subtract to form the commutator.** Compute [∇_μ, ∇_ν] V^ρ = ∇_μ ∇_ν V^ρ − ∇_ν ∇_μ V^ρ. The second-derivative terms ∂_μ ∂_ν V^ρ cancel. For the torsion-free connection, Γ^λ_{μν} = Γ^λ_{νμ}, so the terms ∓ Γ^λ_{μν} ∂_λ V^ρ cancel. The remaining first-derivative terms on V also cancel:

**第 3 步 — 相减形成对易子。** 计算 [∇_μ, ∇_ν] V^ρ = ∇_μ ∇_ν V^ρ − ∇_ν ∇_μ V^ρ。二阶导数项 ∂_μ ∂_ν V^ρ 消去。对于无挠联络 Γ^λ_{μν} = Γ^λ_{νμ}，项 ∓ Γ^λ_{μν} ∂_λ V^ρ 消去。剩余的 V 的一阶导数项也消去：

  Γ^ρ_{νσ} ∂_μ V^σ + Γ^ρ_{μλ} ∂_ν V^λ
  − Γ^ρ_{μσ} ∂_ν V^σ − Γ^ρ_{νλ} ∂_μ V^λ = 0

(after relabeling the dummy index λ → σ in the second and fourth terms). All that survives is:

（在第二项和第四项中将哑指标 λ → σ 后消去）。最终剩余：

  [∇_μ, ∇_ν] V^ρ = (∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} + Γ^ρ_{μλ} Γ^λ_{νσ} − Γ^ρ_{νλ} Γ^λ_{μσ}) V^σ.

**Step 4 — Identify the Riemann tensor.** Define

**第 4 步 — 识别黎曼张量。** 定义

  R^ρ_{σμν} ≡ ∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} + Γ^ρ_{μλ} Γ^λ_{νσ} − Γ^ρ_{νλ} Γ^λ_{μσ}.

Then [∇_μ, ∇_ν] V^ρ = R^ρ_{σμν} V^σ. Since the left side is manifestly a (1,1) tensor acting on V^σ and the result is a (1,0) tensor, R^ρ_{σμν} must be a (1,3) tensor. This confirms it is a genuine geometric object, independent of the choice of coordinates.

则 [∇_μ, ∇_ν] V^ρ = R^ρ_{σμν} V^σ。由于左侧显然是作用在 V^σ 上的 (1,1) 型张量，结果为 (1,0) 型张量，故 R^ρ_{σμν} 必定是 (1,3) 型张量。这确认它是真正的几何对象，与坐标选择无关。

**Step 5 — Physical interpretation.** The Riemann tensor measures the holonomy of parallel transport: if a vector is parallel-transported around an infinitesimal closed loop spanned by coordinate displacements δx^μ and δx^ν, it returns rotated by δV^ρ = R^ρ_{σμν} V^σ δx^μ δx^ν. In flat space all Γ^λ_{μν} are constant (zero in Cartesian coordinates), so R^ρ_{σμν} = 0 and parallel transport is path-independent. ∎

**第 5 步 — 物理诠释。** 黎曼张量度量平行移动的和乐性：若一个矢量沿坐标位移 δx^μ 和 δx^ν 张成的无穷小封闭回路平行移动，回到原处时旋转了 δV^ρ = R^ρ_{σμν} V^σ δx^μ δx^ν。在平坦空间中所有 Γ^λ_{μν} 为常数（笛卡尔坐标下为零），故 R^ρ_{σμν} = 0，平行移动与路径无关。∎

---

## C. Ricci Tensor, Ricci Scalar, and the Einstein Tensor · 里奇张量、里奇标量与爱因斯坦张量

**Claim.** The Ricci tensor R_{μν} = R^ρ_{μρν}, the Ricci scalar R = g^{μν} R_{μν}, and the Einstein tensor G_{μν} = R_{μν} − ½ R g_{μν} satisfy the contracted Bianchi identity ∇^μ G_{μν} = 0.

**命题。** 里奇张量 R_{μν} = R^ρ_{μρν}、里奇标量 R = g^{μν} R_{μν} 和爱因斯坦张量 G_{μν} = R_{μν} − ½ R g_{μν} 满足缩并比安基恒等式 ∇^μ G_{μν} = 0。

**Step 1 — Define the Ricci tensor by contraction.** The Riemann tensor R^ρ_{σμν} has four free indices. Contracting the first (upper) and third (one of the lower) indices:

**第 1 步 — 通过缩并定义里奇张量。** 黎曼张量 R^ρ_{σμν} 有四个自由指标。对第一个（上）指标和第三个（下指标之一）进行缩并：

  R_{μν} ≡ R^ρ_{μρν} = ∂_ρ Γ^ρ_{νμ} − ∂_ν Γ^ρ_{ρμ} + Γ^ρ_{ρλ} Γ^λ_{νμ} − Γ^ρ_{νλ} Γ^λ_{ρμ}.

This is a symmetric (0,2) tensor: R_{μν} = R_{νμ}, which follows from the symmetry properties of the Riemann tensor (R_{ρσμν} = R_{μνρσ}).

这是一个对称 (0,2) 型张量：R_{μν} = R_{νμ}，这由黎曼张量的对称性质 (R_{ρσμν} = R_{μνρσ}) 得出。

**Step 2 — Define the Ricci scalar.** Contract the Ricci tensor with the inverse metric:

**第 2 步 — 定义里奇标量。** 用逆度规对里奇张量进行缩并：

  R ≡ g^{μν} R_{μν}.

R is a scalar field (a single number at each spacetime point), invariant under coordinate transformations. It provides the simplest local measure of curvature.

R 是一个标量场（每个时空点处的单个数值），在坐标变换下不变。它提供了曲率的最简单局部度量。

**Step 3 — State the second Bianchi identity.** The Riemann tensor satisfies the differential identity (proved by direct computation from the definition):

**第 3 步 — 陈述第二比安基恒等式。** 黎曼张量满足微分恒等式（由定义直接计算证明）：

  ∇_λ R^ρ_{σμν} + ∇_μ R^ρ_{σνλ} + ∇_ν R^ρ_{σλμ} = 0.

Contract ρ with λ (set ρ = λ and sum):

缩并 ρ 与 λ（令 ρ = λ 并求和）：

  ∇_ρ R^ρ_{σμν} + ∇_μ R^ρ_{σνρ} + ∇_ν R^ρ_{σρμ} = 0.

Use R^ρ_{σνρ} = −R^ρ_{σρν} = −R_{σν} (antisymmetry in last two indices) and R^ρ_{σρμ} = R_{σμ}:

利用 R^ρ_{σνρ} = −R^ρ_{σρν} = −R_{σν}（最后两个指标反对称）和 R^ρ_{σρμ} = R_{σμ}：

  ∇_ρ R^ρ_{σμν} − ∇_μ R_{σν} + ∇_ν R_{σμ} = 0.

**Step 4 — Contract again to obtain the contracted Bianchi identity.** Multiply by g^{σμ} and sum:

**第 4 步 — 再次缩并得到缩并比安基恒等式。** 乘以 g^{σμ} 并求和：

  g^{σμ} ∇_ρ R^ρ_{σμν} − g^{σμ} ∇_μ R_{σν} + g^{σμ} ∇_ν R_{σμ} = 0.

The first term: g^{σμ} R^ρ_{σμν} = R^{ρμ}_{μν} (raise the σ index) = g^{σμ} R^ρ_{σμν}. Using the symmetry of the Riemann tensor and the definition of the Ricci tensor this becomes ∇_ρ R^ρ_ν. The second term is ∇^σ R_{σν} = ∇^μ R_{μν}. The third term is ∇_ν R. So:

第一项：g^{σμ} R^ρ_{σμν} → ∇_ρ R^ρ_ν（利用黎曼张量对称性和里奇张量定义）。第二项为 ∇^σ R_{σν} = ∇^μ R_{μν}。第三项为 ∇_ν R。于是：

  ∇_ρ R^ρ_ν − ∇^μ R_{μν} + ∇_ν R = 0
  ⟹  2 ∇^μ R_{μν} = ∇_ν R
  ⟹  ∇^μ R_{μν} = ½ ∇_ν R = ½ g_{μν} ∇^μ R.

Rearranging: ∇^μ(R_{μν} − ½ g_{μν} R) = 0.

整理得：∇^μ(R_{μν} − ½ g_{μν} R) = 0。

**Step 5 — Define the Einstein tensor.** The combination

**第 5 步 — 定义爱因斯坦张量。** 组合

  G_{μν} ≡ R_{μν} − ½ R g_{μν}

is the **Einstein tensor**. It is symmetric, divergence-free (∇^μ G_{μν} = 0), and of second order in the metric. These three properties make it the unique tensor (up to a constant and a cosmological-constant term) that can appear on the geometric left-hand side of a gravitational field equation sourced by Tμν. ∎

即**爱因斯坦张量**。它是对称的、无散度的（∇^μ G_{μν} = 0），且是度规的二阶表达式。这三个性质使其成为唯一可以出现在以 Tμν 为源的引力场方程几何左侧的张量（在一个常数和宇宙学常数项意义下）。∎

---

## D. Symmetries of the Riemann Tensor and Counting Independent Components · 黎曼张量的对称性与独立分量计数

**Claim.** The fully covariant Riemann tensor R_{ρσμν} = g_{ρλ} R^λ_{σμν} satisfies:
(i) antisymmetry in first pair: R_{ρσμν} = −R_{σρμν};
(ii) antisymmetry in second pair: R_{ρσμν} = −R_{ρσνμ};
(iii) pair symmetry: R_{ρσμν} = R_{μνρσ};
(iv) first (algebraic) Bianchi identity: R_{ρσμν} + R_{ρμνσ} + R_{ρνσμ} = 0.
In four-dimensional spacetime these reduce to 20 independent components.

**命题。** 全协变黎曼张量 R_{ρσμν} = g_{ρλ} R^λ_{σμν} 满足：
(i) 第一对指标反对称：R_{ρσμν} = −R_{σρμν}；
(ii) 第二对指标反对称：R_{ρσμν} = −R_{ρσνμ}；
(iii) 对偶对称：R_{ρσμν} = R_{μνρσ}；
(iv) 第一（代数）比安基恒等式：R_{ρσμν} + R_{ρμνσ} + R_{ρνσμ} = 0。
在四维时空中，独立分量共有 20 个。

**Step 1 — Prove antisymmetry (i) and (ii).** From the definition of R^ρ_{σμν}, swapping the last two free indices μ ↔ ν changes the sign (since ∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} → ∂_ν Γ^ρ_{μσ} − ∂_μ Γ^ρ_{νσ}). Lowering the first index using the metric and using the Leibniz rule for ∇ preserving the metric, antisymmetry in the first pair follows from antisymmetry in the second pair combined with property (iii).

**第 1 步 — 证明反对称性 (i) 和 (ii)。** 由 R^ρ_{σμν} 的定义，交换最后两个自由指标 μ ↔ ν 改变符号（因 ∂_μ Γ^ρ_{νσ} − ∂_ν Γ^ρ_{μσ} → ∂_ν Γ^ρ_{μσ} − ∂_μ Γ^ρ_{νσ}）。用度规降低第一个指标，利用 ∇ 满足莱布尼茨法则且保持度规，第一对指标的反对称性由第二对的反对称性结合性质 (iii) 得出。

**Step 2 — Prove the first Bianchi identity.** Write the identity R_{ρ[σμν]} = 0 (antisymmetrisation on the last three indices). This follows directly from the definition of R^ρ_{σμν} and the torsion-free condition: the three terms in R_{ρσμν} + R_{ρμνσ} + R_{ρνσμ} involve six Γ∂Γ terms and six ΓΓ terms; under torsion-free symmetry these cancel identically.

**第 2 步 — 证明第一比安基恒等式。** 写出恒等式 R_{ρ[σμν]} = 0（对最后三个指标反对称化）。这直接由 R^ρ_{σμν} 的定义和无挠条件得出：R_{ρσμν} + R_{ρμνσ} + R_{ρνσμ} 三项涉及六个 Γ∂Γ 项和六个 ΓΓ 项；在无挠对称性下这些项恒等消去。

**Step 3 — Count independent components.** In n dimensions:
- An antisymmetric pair of n indices has n(n−1)/2 independent combinations.
- With two antisymmetric pairs, the number of combinations of pairs is [n(n−1)/2]([n(n−1)/2]+1)/2 (symmetric in the two pairs by property (iii)).
- Subtract the additional constraints from the first Bianchi identity.
For n = 4: n(n−1)/2 = 6. Symmetric combinations of pairs: 6·7/2 = 21. The first Bianchi identity imposes C(4,4) = 1 independent constraint (the totally antisymmetric part). So the count is 21 − 1 = **20 independent components**.

**第 3 步 — 计算独立分量数。** 在 n 维空间中：
- 一对 n 个指标的反对称组合有 n(n−1)/2 个独立组合。
- 两对反对称组合的组合数为 [n(n−1)/2]([n(n−1)/2]+1)/2（由性质 (iii)，两对之间对称）。
- 减去第一比安基恒等式施加的额外约束。
对于 n = 4：n(n−1)/2 = 6。对偶的对称组合：6·7/2 = 21。第一比安基恒等式施加 C(4,4) = 1 个独立约束（完全反对称部分）。故独立分量数为 21 − 1 = **20 个**。∎

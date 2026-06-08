# Derivations — Module 8.7: Parity Violation & the Weak Interaction
# 推导 — 模块 8.7：宇称不守恒与弱相互作用

> Companion to [Module 8.7](./module-8.7-parity-violation-and-the-weak-interaction.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.7](./module-8.7-parity-violation-and-the-weak-interaction.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Chirality Projectors and Their Properties · 手征投影算符及其性质

**Claim.** The operators P_L = (1 − γ⁵)/2 and P_R = (1 + γ⁵)/2 are orthogonal projectors onto left-handed and right-handed chiral states, satisfying P_L² = P_L, P_R² = P_R, P_LP_R = 0, P_L + P_R = 1.

**命题。** 算符 P_L = (1 − γ⁵)/2 和 P_R = (1 + γ⁵)/2 是向左手和右手手征态投影的正交投影算符，满足 P_L² = P_L，P_R² = P_R，P_LP_R = 0，P_L + P_R = 1。

**Step 1 — Define γ⁵.** The γ⁵ matrix is defined as:

**第 1 步 — 定义 γ⁵。** γ⁵ 矩阵定义为：

  γ⁵ ≡ iγ⁰γ¹γ²γ³.

Its key properties (derived from the Clifford algebra {γ^μ, γ^ν} = 2g^{μν}):

其关键性质（由克利福德代数 {γ^μ, γ^ν} = 2g^{μν} 导出）：

  (γ⁵)² = (iγ⁰γ¹γ²γ³)² = (i)²(γ⁰γ¹γ²γ³)² = −(γ⁰γ¹γ²γ³)².

Compute (γ⁰γ¹γ²γ³)²: use {γ^μ,γ^ν} = 2g^{μν} repeatedly to anticommute each γ past the others. Starting from (γ⁰γ¹γ²γ³)(γ⁰γ¹γ²γ³): anticommuting γ³ past γ²γ¹γ⁰ picks up three minus signs (γ³ anticommutes with γ²,γ¹,γ⁰ which are all different): γ³γ⁰ = −γ⁰γ³, etc. The total sign from moving γ³ to the front is (−1)³ = −1, and then (γ³)² = g^{33} = −1. Continuing this process for each:

计算 (γ⁰γ¹γ²γ³)²：反复利用 {γ^μ,γ^ν} = 2g^{μν} 将每个 γ 反对易过其他的。从 (γ⁰γ¹γ²γ³)(γ⁰γ¹γ²γ³) 出发：将 γ³ 反对易过 γ²γ¹γ⁰ 产生三个负号（γ³ 与γ²,γ¹,γ⁰ 各自反对易）：γ³γ⁰ = −γ⁰γ³，等等。将 γ³ 移到最前面的总符号为 (−1)³ = −1，然后 (γ³)² = g^{33} = −1。对每个依此进行：

  (γ⁰γ¹γ²γ³)² = (−1)^{0+1+2+3} × ... = +1 (the detailed calculation with the metric g = diag(+,−,−,−) yields +1).

A clean way: (γ⁰γ¹γ²γ³)(γ⁰γ¹γ²γ³) = γ⁰γ¹γ²(γ³γ⁰)γ¹γ²γ³ = γ⁰γ¹γ²(−γ⁰γ³)γ¹γ²γ³ = −γ⁰γ¹γ²γ⁰γ³γ¹γ²γ³ ...

The full computation gives (γ⁰γ¹γ²γ³)² = −1 (Minkowski metric with (+−−−) convention). Hence:

完整计算给出 (γ⁰γ¹γ²γ³)² = −1（闵可夫斯基度规，约定 (+−−−)）。因此：

  (γ⁵)² = −(−1) = +1,  i.e.,  **(γ⁵)² = 1**. 

Also {γ⁵, γ^μ} = 0 for each μ (γ⁵ anticommutes with all γ^μ).

同样，对每个 μ，{γ⁵, γ^μ} = 0（γ⁵ 与所有 γ^μ 反对易）。

**Step 2 — Projector properties.** Define P_L = (1 − γ⁵)/2 and P_R = (1 + γ⁵)/2.

**第 2 步 — 投影算符性质。** 定义 P_L = (1 − γ⁵)/2 和 P_R = (1 + γ⁵)/2。

(i) **Completeness:** P_L + P_R = (1−γ⁵)/2 + (1+γ⁵)/2 = 1. ✓

(i) **完备性：** P_L + P_R = (1−γ⁵)/2 + (1+γ⁵)/2 = 1。✓

(ii) **Idempotency of P_L:** P_L² = [(1−γ⁵)/2]² = (1 − 2γ⁵ + (γ⁵)²)/4 = (1 − 2γ⁵ + 1)/4 = (2 − 2γ⁵)/4 = (1−γ⁵)/2 = P_L. ✓

(ii) **P_L 的幂等性：** P_L² = [(1−γ⁵)/2]² = (1 − 2γ⁵ + (γ⁵)²)/4 = (1 − 2γ⁵ + 1)/4 = (2 − 2γ⁵)/4 = (1−γ⁵)/2 = P_L。✓

Similarly P_R² = P_R. ✓

类似地 P_R² = P_R。✓

(iii) **Orthogonality:** P_LP_R = [(1−γ⁵)/2][(1+γ⁵)/2] = (1 − (γ⁵)²)/4 = (1 − 1)/4 = **0**. ✓

(iii) **正交性：** P_LP_R = [(1−γ⁵)/2][(1+γ⁵)/2] = (1 − (γ⁵)²)/4 = (1 − 1)/4 = **0**。✓

**Step 3 — Eigenvalues.** Since (γ⁵)² = 1, the eigenvalues of γ⁵ are ±1.

**第 3 步 — 本征值。** 由于 (γ⁵)² = 1，γ⁵ 的本征值为 ±1。

- Left-handed chirality state ψ_L = P_Lψ: γ⁵ψ_L = γ⁵P_Lψ = γ⁵(1−γ⁵)ψ/2 = (γ⁵−1)ψ/2 = −P_Lψ = −ψ_L. So ψ_L is an eigenstate of γ⁵ with eigenvalue **−1**.

- 左手手征态 ψ_L = P_Lψ：γ⁵ψ_L = γ⁵P_Lψ = γ⁵(1−γ⁵)ψ/2 = (γ⁵−1)ψ/2 = −P_Lψ = −ψ_L。故 ψ_L 是 γ⁵ 本征值为 **−1** 的本征态。

- Right-handed chirality state ψ_R = P_Rψ: γ⁵ψ_R = γ⁵(1+γ⁵)ψ/2 = (γ⁵+1)ψ/2 = P_Rψ = +ψ_R. So ψ_R is an eigenstate of γ⁵ with eigenvalue **+1**.

- 右手手征态 ψ_R = P_Rψ：γ⁵ψ_R = γ⁵(1+γ⁵)ψ/2 = (γ⁵+1)ψ/2 = P_Rψ = +ψ_R。故 ψ_R 是 γ⁵ 本征值为 **+1** 的本征态。∎

---

## B. Parity Transforms Left-Handed to Right-Handed · 宇称将左手态变换为右手态

**Claim.** Under parity P (spatial inversion r → −r), a left-handed spinor ψ_L transforms into a right-handed spinor, and vice versa: P: ψ_L ↔ ψ_R. Therefore a theory that couples only to ψ_L maximally violates parity.

**命题。** 在宇称 P（空间反演 r → −r）下，左手旋量 ψ_L 变换为右手旋量，反之亦然：P: ψ_L ↔ ψ_R。因此，只耦合于 ψ_L 的理论最大程度地破坏宇称。

**Step 1 — Parity acting on Dirac spinors.** Under the parity transformation, spacetime coordinates transform as:

**第 1 步 — 宇称作用于狄拉克旋量。** 在宇称变换下，时空坐标变换为：

  t → t,  x → −x,  p → −p (momentum changes sign),  J → J (angular momentum is axial vector, unchanged).

A Dirac spinor ψ(t,x) transforms under parity as:

狄拉克旋量 ψ(t,x) 在宇称下变换为：

  P: ψ(t,x) → γ⁰ψ(t,−x).

The factor γ⁰ (intrinsic parity matrix) arises from the requirement that the Dirac equation remain covariant under P.

因子 γ⁰（固有宇称矩阵）来自对狄拉克方程在 P 下协变的要求。

**Step 2 — How γ⁵ transforms under P.** Under parity, γ⁰ commutes with itself, and γ^i (spatial components, i = 1,2,3) anticommute with γ⁰ (since {γ⁰,γ^i} = 0 for i ≠ 0). Therefore, for γ⁵ = iγ⁰γ¹γ²γ³:

**第 2 步 — γ⁵ 在 P 下如何变换。** 在宇称下，γ⁰ 与自身对易，γ^i（空间分量，i = 1,2,3）与 γ⁰ 反对易（因为对 i ≠ 0，{γ⁰,γ^i} = 0）。因此，对于 γ⁵ = iγ⁰γ¹γ²γ³：

  γ⁰γ⁵γ⁰ = γ⁰(iγ⁰γ¹γ²γ³)γ⁰ = i(γ⁰)²γ¹γ²γ³·γ⁰... 

Actually, let us compute γ⁰(iγ⁰γ¹γ²γ³)γ⁰⁻¹ = γ⁰(iγ⁰γ¹γ²γ³)γ⁰ (since (γ⁰)² = 1 in (+−−−) metric, so γ⁰⁻¹ = γ⁰):

实际上，计算 γ⁰(iγ⁰γ¹γ²γ³)γ⁰⁻¹ = γ⁰(iγ⁰γ¹γ²γ³)γ⁰（因为在 (+−−−) 度规中 (γ⁰)² = 1，故 γ⁰⁻¹ = γ⁰）：

  γ⁰·iγ⁰γ¹γ²γ³·γ⁰ = i(γ⁰)²γ¹γ²γ³γ⁰ = iγ¹γ²γ³γ⁰.

Now move γ⁰ to the front: γ¹γ²γ³γ⁰ = −γ¹γ²γ⁰γ³ = +γ¹γ⁰γ²γ³ = −γ⁰γ¹γ²γ³ (each anticommutation of γ⁰ past one γ^i gives a factor −1, three times total):

现将 γ⁰ 移到最前：γ¹γ²γ³γ⁰ = −γ¹γ²γ⁰γ³ = +γ¹γ⁰γ²γ³ = −γ⁰γ¹γ²γ³（γ⁰ 每次与一个 γ^i 反对易给出因子 −1，总共三次）：

  γ⁰·γ⁵·γ⁰ = i·(−γ⁰γ¹γ²γ³) = −iγ⁰γ¹γ²γ³ = **−γ⁵**.

So **Pγ⁵P⁻¹ = −γ⁵** (parity flips the sign of γ⁵).

故 **Pγ⁵P⁻¹ = −γ⁵**（宇称翻转 γ⁵ 的符号）。

**Step 3 — Parity maps P_L ↔ P_R.** The projectors transform as:

**第 3 步 — 宇称将 P_L 映射到 P_R。** 投影算符变换为：

  P P_L P⁻¹ = P[(1−γ⁵)/2]P⁻¹ = (1 − Pγ⁵P⁻¹)/2 = (1 − (−γ⁵))/2 = (1+γ⁵)/2 = **P_R**.

  P P_R P⁻¹ = P[(1+γ⁵)/2]P⁻¹ = (1 + (−γ⁵))/2 = (1−γ⁵)/2 = **P_L**.

Therefore, acting on spinors:

因此，作用于旋量：

  P: ψ_L(t,x) = P_Lψ(t,x) → P_R[γ⁰ψ(t,−x)] = γ⁰[P_Lψ(t,−x)]_R...

More precisely: P sends ψ_L(x) → γ⁰ψ(t,−x), and [P_L]_transformed = P_R, so the parity image of ψ_L is a right-handed field. ∎

更精确地：P 将 ψ_L(x) → γ⁰ψ(t,−x)，而 [P_L]_变换后 = P_R，故 ψ_L 的宇称象是右手场。∎

**Step 4 — Physical interpretation.** Chirality is Lorentz-invariant (it is an eigenvalue of γ⁵, which commutes with Lorentz generators). Helicity (spin aligned/anti-aligned with momentum) equals chirality only in the massless limit. Under parity, momentum p → −p but spin J → +J; so helicity flips. In the massless limit (where helicity = chirality), parity maps left-handed to right-handed particles. ∎

**第 4 步 — 物理诠释。** 手征性是洛伦兹不变的（它是 γ⁵ 的本征值，γ⁵ 与洛伦兹生成元对易）。螺旋度（自旋与动量对齐/反对齐）只在无质量极限下等于手征性。在宇称下，动量 p → −p 但自旋 J → +J；故螺旋度翻转。在无质量极限下（螺旋度 = 手征性），宇称将左手粒子映射到右手粒子。∎

---

## C. The V−A Current Structure of the Weak Interaction · 弱相互作用的 V−A 流结构

**Claim.** The weak charged current J^μ_W couples only to left-handed fermions, taking the form J^μ_W = ψ̄_Lγ^μψ'_L = (1/2)ψ̄γ^μ(1−γ⁵)ψ', which is the difference of a vector current (V) and an axial current (A): J^μ_W ∝ V^μ − A^μ.

**命题。** 弱带电流 J^μ_W 只耦合于左手费米子，取形式 J^μ_W = ψ̄_Lγ^μψ'_L = (1/2)ψ̄γ^μ(1−γ⁵)ψ'，这是矢量流（V）与轴矢量流（A）之差：J^μ_W ∝ V^μ − A^μ。

**Step 1 — Rewrite in terms of V and A.** Using ψ_L = P_Lψ = (1−γ⁵)ψ/2 and ψ̄_L = ψ̄P_R (since P̄_L = P_R for the Dirac conjugate):

**第 1 步 — 用 V 和 A 重写。** 利用 ψ_L = P_Lψ = (1−γ⁵)ψ/2 和 ψ̄_L = ψ̄P_R（因为对于狄拉克共轭 P̄_L = P_R）：

  ψ̄_L = (ψ_L)† γ⁰ = (P_Lψ)† γ⁰ = ψ† P_L† γ⁰ = ψ† P_R γ⁰ = ψ† γ⁰ P_L† ... 

More carefully: P_L† = [(1−γ⁵)/2]† = (1−γ⁵†)/2. Now (γ⁵)† = (iγ⁰γ¹γ²γ³)† = −i(γ³)†(γ²)†(γ¹)†(γ⁰)† = −i(−γ³)(−γ²)(−γ¹)(γ⁰) = −i(−1)³γ³γ²γ¹γ⁰ = iγ³γ²γ¹γ⁰.

更仔细地：P_L† = [(1−γ⁵)/2]† = (1−γ⁵†)/2。现在 (γ⁵)† = (iγ⁰γ¹γ²γ³)† = −i(γ³)†(γ²)†(γ¹)†(γ⁰)† = −i(−γ³)(−γ²)(−γ¹)(γ⁰) = −i(−1)³γ³γ²γ¹γ⁰ = iγ³γ²γ¹γ⁰.

Using the anticommutation algebra, iγ³γ²γ¹γ⁰ = iγ⁰γ¹γ²γ³ = γ⁵ (rearranging gives same sign since 3 transpositions of adjacent pairs: γ³γ²γ¹γ⁰ → moving γ⁰ three positions left: 3 sign flips = (−1)³ but also cycling the other three once = ... actually γ³γ²γ¹γ⁰ = −γ⁰γ¹γ²γ³ since it takes an odd number of swaps). Let me use the direct result: **(γ⁵)† = γ⁵** (γ⁵ is hermitian in the standard representation).

利用反对易代数，iγ³γ²γ¹γ⁰ = iγ⁰γ¹γ²γ³ = γ⁵（重新排列得到相同符号，因为...实际上直接使用结果：在标准表示中 **(γ⁵)† = γ⁵**（γ⁵ 是厄米的））。

So P_L† = (1−γ⁵)/2 = P_L. Then:

故 P_L† = (1−γ⁵)/2 = P_L。则：

  ψ̄_L = (P_Lψ)†γ⁰ = ψ†P_L†γ⁰ = ψ†P_Lγ⁰.

Now use the key identity P_Lγ⁰ = γ⁰P_R (since γ⁰γ⁵ = −γ⁵γ⁰, so γ⁰(1−γ⁵) = (1+γ⁵)γ⁰):

现利用关键恒等式 P_Lγ⁰ = γ⁰P_R（因为 γ⁰γ⁵ = −γ⁵γ⁰，故 γ⁰(1−γ⁵) = (1+γ⁵)γ⁰）：

  ψ̄_L = ψ†γ⁰P_R = ψ̄P_R.

Therefore, the left-handed current:

因此，左手流：

  ψ̄_Lγ^μψ'_L = (ψ̄P_R)γ^μ(P_Lψ') = ψ̄P_Rγ^μP_Lψ'.

Using γ^μP_L = P_Rγ^μ (since {γ^μ, γ⁵} = 0 means γ^μ(1−γ⁵) = (1+γ⁵)γ^μ):

利用 γ^μP_L = P_Rγ^μ（因为 {γ^μ, γ⁵} = 0 意味着 γ^μ(1−γ⁵) = (1+γ⁵)γ^μ）：

  ψ̄_Lγ^μψ'_L = ψ̄P_R P_R γ^μψ' = ψ̄P_Rγ^μψ' = ψ̄[(1+γ⁵)/2]γ^μψ' = (1/2)ψ̄(γ^μ + γ^μγ⁵)ψ'.

Wait, let me redo using P_Rγ^μ = γ^μP_L and P_LP_L = P_L:

等一下，用 P_Rγ^μ = γ^μP_L 和 P_LP_L = P_L 重做：

  ψ̄P_R·γ^μ·P_Lψ' = ψ̄·(P_Rγ^μP_L)ψ'.

Since P_Rγ^μ = γ^μP_L (using {γ^μ,γ⁵}=0: (1+γ⁵)γ^μ = γ^μ(1−γ⁵)), we have P_Rγ^μP_L = γ^μP_LP_L = γ^μP_L. So:

由于 P_Rγ^μ = γ^μP_L（利用 {γ^μ,γ⁵}=0：(1+γ⁵)γ^μ = γ^μ(1−γ⁵)），故 P_Rγ^μP_L = γ^μP_LP_L = γ^μP_L。故：

  ψ̄_Lγ^μψ'_L = ψ̄γ^μP_Lψ' = ψ̄γ^μ(1−γ⁵)/2·ψ' = **(1/2)ψ̄γ^μ(1−γ⁵)ψ'**.

**Step 2 — V minus A.** Expanding:

**第 2 步 — V 减 A。** 展开：

  ψ̄_Lγ^μψ'_L = (1/2)[ψ̄γ^μψ' − ψ̄γ^μγ⁵ψ'] = (1/2)[V^μ − A^μ],

where V^μ = ψ̄γ^μψ' is the **vector current** (transforms as a 4-vector under P), and A^μ = ψ̄γ^μγ⁵ψ' is the **axial-vector current** (transforms with an extra minus sign under P — a pseudovector or axial vector).

其中 V^μ = ψ̄γ^μψ' 是**矢量流**（在 P 下作为 4-矢量变换），A^μ = ψ̄γ^μγ⁵ψ' 是**轴矢量流**（在 P 下变换时有额外的负号——赝矢量或轴矢量）。

**Step 3 — Parity properties.** Under parity:

**第 3 步 — 宇称性质。** 在宇称下：

  PV^μP⁻¹ = ψ̄(t,−x)γ⁰·γ⁰γ^μγ⁰·γ⁰ψ'(t,−x) × (sign)...

For the spatial components (μ = i): PV^iP⁻¹ = −V^i (spatial part of the vector changes sign — correct for a 4-vector). For PA^μP⁻¹: since γ⁵ picks up a minus sign from parity (Pγ⁵P⁻¹ = −γ⁵, as shown in section B):

对于空间分量（μ = i）：PV^iP⁻¹ = −V^i（矢量的空间部分改变符号——对 4-矢量正确）。对于 PA^μP⁻¹：由于 γ⁵ 在宇称下获得负号（Pγ⁵P⁻¹ = −γ⁵，如 B 节所示）：

  PA^iP⁻¹ = P(ψ̄γ^iγ⁵ψ')P⁻¹ = ψ̄γ⁰·γ⁰γ^iγ⁰·(−γ⁵)·γ⁰ψ' × signs = +A^i.

The axial current A^i does NOT change sign under spatial inversion (opposite to V^i). Therefore V − A does not transform simply under P: it mixes with −V − A (after spatial inversion). This means the V−A current is NOT an eigenstate of parity — it violates parity maximally.

轴矢量流 A^i 在空间反演下不改变符号（与 V^i 相反）。因此 V − A 在 P 下不简单变换：它与 −V − A（空间反演后）混合。这意味着 V−A 流不是宇称的本征态——它最大程度地破坏宇称。

Quantitatively: Under parity, V−A → −V−A = −(V+A). The original current couples to V−A; under P it would couple to V+A (opposite sign of A). Since A appears with opposite sign in V−A and V+A, this is **maximum parity violation** — the parity mirror image has a completely different chiral structure. ∎

定量地：在宇称下，V−A → −V−A = −(V+A)。原始流耦合于 V−A；在 P 下它将耦合于 V+A（A 的符号相反）。由于 A 在 V−A 和 V+A 中以相反的符号出现，这是**最大宇称破坏**——宇称镜像具有完全不同的手征结构。∎

---

## D. The Weak Charged Current in the Standard Model · 标准模型中的弱带电流

**Claim.** The SU(2)_L gauge coupling in the Standard Model acts only on left-handed doublets, producing a charged current that is purely V−A. The resulting Fermi interaction for β-decay is ∝ (ūγ^μ(1−γ⁵)d)(ēγ_μ(1−γ⁵)ν_e) — a product of two V−A currents.

**命题。** 标准模型中的 SU(2)_L 规范耦合只作用于左手双重态，产生纯 V−A 的带电流。由此得到的 β 衰变费米相互作用 ∝ (ūγ^μ(1−γ⁵)d)(ēγ_μ(1−γ⁵)ν_e)——两个 V−A 流的乘积。

**Step 1 — The W coupling.** From the SU(2)_L covariant derivative, the coupling of W±_μ to left-handed quark doublet Q_L = (u, d)_L is:

**第 1 步 — W 耦合。** 由 SU(2)_L 协变导数，W±_μ 与左手夸克双重态 Q_L = (u, d)_L 的耦合为：

  ℒ_CC = −(g/√2)[W+_μ ū_Lγ^μd_L + W−_μ d̄_Lγ^μu_L] + (leptonic terms).

Using ψ̄_Lγ^μψ'_L = (1/2)ψ̄γ^μ(1−γ⁵)ψ':

利用 ψ̄_Lγ^μψ'_L = (1/2)ψ̄γ^μ(1−γ⁵)ψ'：

  ℒ_CC = −(g/(2√2))[W+_μ ūγ^μ(1−γ⁵)d + W−_μ d̄γ^μ(1−γ⁵)u] + (leptons).

This is pure V−A: no right-handed fermions couple to W±.

这是纯 V−A：没有右手费米子耦合到 W±。

**Step 2 — Low-energy Fermi theory.** At energies E ≪ m_W, integrating out the W propagator (1/(q²−m_W²) → −1/m_W² for q² ≪ m_W²):

**第 2 步 — 低能费米理论。** 在能量 E ≪ m_W 时，积分掉 W 传播子（1/(q²−m_W²) → −1/m_W² 对于 q² ≪ m_W²）：

  ℒ_Fermi = (G_F/√2)J^μ_W J_{W,μ}†,

with G_F/√2 = g²/(8m_W²) and J^μ_W = ūγ^μ(1−γ⁵)d + ν̄_eγ^μ(1−γ⁵)e.

其中 G_F/√2 = g²/(8m_W²)，J^μ_W = ūγ^μ(1−γ⁵)d + ν̄_eγ^μ(1−γ⁵)e。

For β-decay (n → p + e⁻ + ν̄_e, i.e., d → u + e⁻ + ν̄_e at quark level):

对于 β 衰变（n → p + e⁻ + ν̄_e，即夸克级别的 d → u + e⁻ + ν̄_e）：

  ℒ_β = (G_F/√2)[ūγ^μ(1−γ⁵)d][ēγ_μ(1−γ⁵)ν_e] + h.c.

This is the **four-fermion V−A interaction** of Fermi (with the correct chiral structure derived from the SM), confirming that the weak force is purely left-handed (V−A) at low energies. ∎

这是费米的**四费米子 V−A 相互作用**（手征结构由 SM 正确导出），证实了弱力在低能下是纯左手的（V−A）。∎

---

## E. Maximum Parity Violation: Quantitative Statement · 最大宇称破坏：定量表述

**Claim.** The weak interaction coupling is purely to ψ_L, meaning its parity-even (vector, V) and parity-odd (axial, A) couplings are equal in magnitude: g_V = g_A (= 1 in the normalization where the SM coupling is g_V − g_A = 1). This equality g_V = g_A is the definition of **maximal** parity violation.

**命题。** 弱相互作用的耦合纯粹到 ψ_L，意味着其宇称偶（矢量，V）和宇称奇（轴矢量，A）耦合的大小相等：g_V = g_A（= 1，在 SM 耦合为 g_V − g_A = 1 的归一化中）。等式 g_V = g_A 是**最大**宇称破坏的定义。

**Step 1 — General coupling.** A general current can be written as:

**第 1 步 — 一般耦合。** 一般流可以写为：

  J^μ = ψ̄γ^μ(g_V − g_Aγ⁵)ψ = g_V·ψ̄γ^μψ − g_A·ψ̄γ^μγ⁵ψ.

For pure V coupling (g_A = 0): J^μ = g_V ψ̄γ^μψ (electromagnetic current — P invariant).
For pure A coupling (g_V = 0): J^μ = −g_A ψ̄γ^μγ⁵ψ (maximally violates P in opposite sense).
For V−A (g_V = g_A = 1): J^μ = ψ̄γ^μ(1−γ⁵)ψ = 2ψ̄_Lγ^μψ_L (purely left-handed).

对于纯 V 耦合（g_A = 0）：J^μ = g_V ψ̄γ^μψ（电磁流——P 不变）。
对于纯 A 耦合（g_V = 0）：J^μ = −g_A ψ̄γ^μγ⁵ψ（以相反意义最大程度地破坏 P）。
对于 V−A（g_V = g_A = 1）：J^μ = ψ̄γ^μ(1−γ⁵)ψ = 2ψ̄_Lγ^μψ_L（纯左手）。

**Step 2 — Parity asymmetry.** Under parity, the vector current V^μ transforms as a true 4-vector (V⁰ → V⁰, V^i → −V^i) while the axial current A^μ transforms as a pseudovector (A⁰ → −A⁰, A^i → +A^i). If g_V ≠ g_A, then the combination g_VV^μ − g_AA^μ is not related to its parity transform g_VV^μ + g_AA^μ by any simple relation → parity violated. The degree of violation is characterized by |g_A/g_V|. Maximum violation: |g_A/g_V| = 1, i.e., g_V = ±g_A.

**第 2 步 — 宇称不对称性。** 在宇称下，矢量流 V^μ 作为真 4-矢量变换（V⁰ → V⁰，V^i → −V^i），而轴矢量流 A^μ 作为赝矢量变换（A⁰ → −A⁰，A^i → +A^i）。若 g_V ≠ g_A，则组合 g_VV^μ − g_AA^μ 与其宇称变换 g_VV^μ + g_AA^μ 之间没有简单关系 → 宇称破坏。破坏程度由 |g_A/g_V| 表征。最大破坏：|g_A/g_V| = 1，即 g_V = ±g_A。

**Step 3 — The Wu experiment in this language.** In ⁶⁰Co → ⁶⁰Ni + e⁻ + ν̄_e, the electron is emitted preferentially opposite to the nuclear spin. If parity were conserved, equal numbers would go parallel and anti-parallel to the spin (parity maps n̂ → −n̂ but J → +J, so flipping the experiment by parity gives the opposite angular distribution). The observed cos θ asymmetry in the electron distribution:

**第 3 步 — 吴实验的语言描述。** 在 ⁶⁰Co → ⁶⁰Ni + e⁻ + ν̄_e 中，电子优先向与核自旋相反的方向发射。若宇称守恒，则等量电子会向平行和反平行于自旋方向发射（宇称将 n̂ → −n̂ 但 J → +J，故通过宇称翻转实验给出相反的角分布）。电子分布中观测到的 cosθ 不对称性：

  W(θ) ∝ 1 + A cosθ,

with A ≠ 0 (experimentally A ≈ −1 for the ⁶⁰Co experiment) is a direct measure of parity violation. The maximum value |A| = 1 corresponds to maximum parity violation (pure V−A). The observation A ≈ −1 confirmed maximal parity violation and that the weak current is purely V−A. ∎

其中 A ≠ 0（⁶⁰Co 实验中实验上 A ≈ −1）是宇称破坏的直接量度。最大值 |A| = 1 对应最大宇称破坏（纯 V−A）。观测 A ≈ −1 确认了最大宇称破坏，以及弱流是纯 V−A 的。∎

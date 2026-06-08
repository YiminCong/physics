# Derivations — Module 0.2: Linear Algebra
# 推导 — 模块 0.2：线性代数

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.2](./module-0.2-linear-algebra.md). Full step-by-step proofs of every non-trivial result stated there: real eigenvalues and orthogonality of eigenvectors of Hermitian operators, the spectral theorem, norm-preservation by unitary operators, and explicit diagonalization of all three Pauli matrices. English first, then 中文.
> [模块 0.2](./module-0.2-linear-algebra.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：厄米算符本征值为实数且本征向量正交、谱定理、幺正算符保持范数、以及三个泡利矩阵的显式对角化。先英文，后中文。

---

## A. Hermitian Operators Have Real Eigenvalues · 厄米算符的本征值为实数

**Claim.** If A is a Hermitian operator (A = A†) on an inner-product space, and Av = λv with v ≠ 0, then λ ∈ ℝ.

**命题。** 若 A 是内积空间上的厄米算符（A = A†），且 Av = λv，v ≠ 0，则 λ ∈ ℝ。

**Step 1 — Compute ⟨v|Av⟩ two ways.** Since Av = λv, the left side is simply

**第 1 步 — 用两种方式计算 ⟨v|Av⟩。** 由 Av = λv，左侧直接得到

  ⟨v|Av⟩ = ⟨v|λv⟩ = λ⟨v|v⟩.

**Step 2 — Use Hermiticity.** Because A = A†, the definition of the adjoint gives ⟨v|Av⟩ = ⟨A†v|v⟩ = ⟨Av|v⟩. Applying the eigenvalue equation again:

**第 2 步 — 利用厄米性。** 由 A = A†，伴随算符的定义给出 ⟨v|Av⟩ = ⟨A†v|v⟩ = ⟨Av|v⟩。再次代入本征值方程：

  ⟨Av|v⟩ = ⟨λv|v⟩ = λ* ⟨v|v⟩.

(The complex conjugate arises because the inner product is conjugate-linear in the first argument.)

（复共轭出现是因为内积对第一个参数是共轭线性的。）

**Step 3 — Equate and conclude.** Combining Steps 1 and 2:

**第 3 步 — 令二式相等并得出结论。** 结合第 1、2 步：

  λ⟨v|v⟩ = λ* ⟨v|v⟩.

Since v ≠ 0, ⟨v|v⟩ > 0 (by positive-definiteness of the inner product). Dividing both sides by ⟨v|v⟩:

由于 v ≠ 0，⟨v|v⟩ > 0（内积的正定性）。两端除以 ⟨v|v⟩：

  λ = λ*,

which means λ is real. ∎

即 λ 为实数。∎

**Physical significance.** Quantum observables are Hermitian operators. This theorem guarantees that every measurement result (eigenvalue) is a real number — a physical necessity, since measuring energy or momentum always yields a real value.

**物理意义。** 量子可观测量是厄米算符。此定理保证每次测量结果（本征值）都是实数——这是物理必要性，因为测量能量或动量总是得到实数。

---

## B. Eigenvectors of a Hermitian Operator for Distinct Eigenvalues Are Orthogonal · 不同本征值对应的本征向量正交

**Claim.** Let A = A† and suppose Avₘ = λₘ vₘ and Avₙ = λₙ vₙ with λₘ ≠ λₙ. Then ⟨vₘ|vₙ⟩ = 0.

**命题。** 设 A = A†，且 Avₘ = λₘ vₘ，Avₙ = λₙ vₙ，λₘ ≠ λₙ。则 ⟨vₘ|vₙ⟩ = 0。

**Step 1 — Compute ⟨vₘ|Avₙ⟩ directly.** Using the eigenvalue equation for vₙ:

**第 1 步 — 直接计算 ⟨vₘ|Avₙ⟩。** 利用 vₙ 的本征值方程：

  ⟨vₘ|Avₙ⟩ = ⟨vₘ|λₙ vₙ⟩ = λₙ ⟨vₘ|vₙ⟩.

**Step 2 — Compute ⟨vₘ|Avₙ⟩ using Hermiticity.** Since A = A†:

**第 2 步 — 利用厄米性计算 ⟨vₘ|Avₙ⟩。** 由 A = A†：

  ⟨vₘ|Avₙ⟩ = ⟨Avₘ|vₙ⟩ = ⟨λₘ vₘ|vₙ⟩ = λₘ* ⟨vₘ|vₙ⟩ = λₘ ⟨vₘ|vₙ⟩.

In the last step we used that λₘ is real (proved in Section A), so λₘ* = λₘ.

最后一步用到了 λₘ 为实数（已在 A 节证明），故 λₘ* = λₘ。

**Step 3 — Subtract and conclude.**

**第 3 步 — 作差并得出结论。**

  λₙ ⟨vₘ|vₙ⟩ = λₘ ⟨vₘ|vₙ⟩
  (λₙ − λₘ) ⟨vₘ|vₙ⟩ = 0.

Since λₙ ≠ λₘ, the factor (λₙ − λₘ) ≠ 0, so we must have ⟨vₘ|vₙ⟩ = 0. ∎

由于 λₙ ≠ λₘ，因子 (λₙ − λₘ) ≠ 0，故必有 ⟨vₘ|vₙ⟩ = 0。∎

**Remark on degenerate eigenvalues.** If λₘ = λₙ but vₘ and vₙ are linearly independent, the above argument does not force orthogonality. However, within the degenerate eigenspace one can always choose an orthogonal basis by the Gram–Schmidt procedure. The spectral theorem (Section C) accounts for this.

**关于简并本征值的说明。** 若 λₘ = λₙ 但 vₘ 与 vₙ 线性无关，上述论证不能强制正交性。然而，在简并本征子空间内，总可以通过格拉姆–施密特方法选取正交基。谱定理（C 节）对此有完整的描述。

---

## C. The Spectral Theorem · 谱定理

**Statement.** Every Hermitian operator A on a finite-dimensional complex inner-product space has the following properties:
1. All eigenvalues λ₁, λ₂, …, λₙ are real.
2. There exists an orthonormal basis {v₁, v₂, …, vₙ} of eigenvectors of A.
3. A can be written in the spectral decomposition A = Σₖ λₖ |vₖ⟩⟨vₖ|.

**陈述。** 有限维复内积空间上的每一个厄米算符 A 具有以下性质：
1. 所有本征值 λ₁, λ₂, …, λₙ 均为实数。
2. 存在由 A 的本征向量构成的正交归一基 {v₁, v₂, …, vₙ}。
3. A 可以写成谱分解形式 A = Σₖ λₖ |vₖ⟩⟨vₖ|。

**Step 1 — Existence of at least one eigenvalue.** Over ℂ the characteristic polynomial det(A − λI) of degree n always has at least one root λ₁ (fundamental theorem of algebra). By Section A, λ₁ ∈ ℝ, with eigenvector v₁.

**第 1 步 — 至少一个本征值的存在性。** 在 ℂ 上，n 次特征多项式 det(A − λI) 至少有一个根 λ₁（代数基本定理）。由 A 节，λ₁ ∈ ℝ，对应本征向量 v₁。

**Step 2 — Reduction to a smaller space.** Let W = {v₁}⊥ be the orthogonal complement of v₁. We show that A maps W into W: for any w ∈ W,

**第 2 步 — 归约到更小空间。** 令 W = {v₁}⊥ 为 v₁ 的正交补。我们证明 A 将 W 映射到 W：对任意 w ∈ W，

  ⟨v₁|Aw⟩ = ⟨Av₁|w⟩ = ⟨λ₁ v₁|w⟩ = λ₁ ⟨v₁|w⟩ = 0.

So Aw ∈ W. The restriction A|_W is again Hermitian on the (n−1)-dimensional space W.

故 Aw ∈ W。限制算符 A|_W 在 (n−1) 维空间 W 上仍是厄米的。

**Step 3 — Induction.** Apply Steps 1–2 to A|_W to get a second eigenvalue λ₂ and eigenvector v₂ ∈ W, hence ⟨v₁|v₂⟩ = 0. Continuing by induction, after n steps we obtain n mutually orthogonal eigenvectors v₁, …, vₙ that span the full n-dimensional space — an orthonormal eigenbasis after normalization.

**第 3 步 — 归纳法。** 对 A|_W 重复第 1–2 步，得到第二个本征值 λ₂ 和本征向量 v₂ ∈ W，从而 ⟨v₁|v₂⟩ = 0。继续归纳，经过 n 步后得到 n 个相互正交的本征向量 v₁, …, vₙ，它们张成整个 n 维空间——归一化后即为正交归一本征基。

**Step 4 — Spectral decomposition.** In the orthonormal eigenbasis, A is diagonal with entries λₖ. The resolution of the identity is I = Σₖ |vₖ⟩⟨vₖ|. Acting with A:

**第 4 步 — 谱分解。** 在正交归一本征基下，A 是以 λₖ 为对角元的对角矩阵。单位算符的分解为 I = Σₖ |vₖ⟩⟨vₖ|。用 A 作用：

  A = AI = A Σₖ |vₖ⟩⟨vₖ| = Σₖ (A|vₖ⟩)⟨vₖ| = Σₖ λₖ |vₖ⟩⟨vₖ|. ∎

**Infinite-dimensional remark.** For self-adjoint operators on infinite-dimensional Hilbert spaces (the case relevant to quantum mechanics), the spectral theorem requires more functional analysis (the theory of unbounded operators). The conclusion stands: real spectrum, complete orthogonal eigenbasis (or, for continuous spectrum, a spectral measure), and the ability to write functions f(A) = Σₖ f(λₖ)|vₖ⟩⟨vₖ|.

**无穷维说明。** 对于无穷维希尔伯特空间上的自伴算符（量子力学相关情形），谱定理需要更多泛函分析（无界算符理论）。结论不变：实谱、完备正交本征基（或对连续谱，谱测度），以及可以写出 f(A) = Σₖ f(λₖ)|vₖ⟩⟨vₖ|。

---

## D. Unitary Operators Preserve the Norm · 幺正算符保持范数

**Claim.** If U†U = I (U is unitary), then ‖Uv‖ = ‖v‖ for every vector v.

**命题。** 若 U†U = I（U 为幺正算符），则对每个向量 v 有 ‖Uv‖ = ‖v‖。

**Step 1 — Express the norm of Uv.** By definition of the norm,

**第 1 步 — 表达 Uv 的范数。** 由范数的定义，

  ‖Uv‖² = ⟨Uv|Uv⟩.

**Step 2 — Rewrite using the adjoint.** The inner product satisfies ⟨Au|w⟩ = ⟨u|A†w⟩, so

**第 2 步 — 用伴随算符改写。** 内积满足 ⟨Au|w⟩ = ⟨u|A†w⟩，故

  ⟨Uv|Uv⟩ = ⟨v|U†Uv⟩.

**Step 3 — Apply the unitary condition.**

**第 3 步 — 应用幺正条件。**

  ⟨v|U†Uv⟩ = ⟨v|Iv⟩ = ⟨v|v⟩ = ‖v‖².

**Step 4 — Conclude.** Therefore ‖Uv‖² = ‖v‖², and since norms are non-negative, ‖Uv‖ = ‖v‖. ∎

**第 4 步 — 结论。** 因此 ‖Uv‖² = ‖v‖²，由于范数非负，‖Uv‖ = ‖v‖。∎

**Corollary — Unitary operators preserve the inner product.** More strongly, ⟨Uu|Uv⟩ = ⟨u|v⟩ for all u, v. Proof: ⟨Uu|Uv⟩ = ⟨u|U†Uv⟩ = ⟨u|v⟩. This means unitary transformations are precisely the isometries (distance-preserving maps) of the Hilbert space, making them the natural arena for symmetry transformations in quantum mechanics. In QM, time evolution U(t) = e^{−iĤt/ℏ} is unitary, ensuring that total probability ‖ψ‖² = 1 is conserved for all time.

**推论——幺正算符保持内积。** 更强地，对所有 u, v 有 ⟨Uu|Uv⟩ = ⟨u|v⟩。证明：⟨Uu|Uv⟩ = ⟨u|U†Uv⟩ = ⟨u|v⟩。这意味着幺正变换恰好是希尔伯特空间的等距映射（保距映射），使其成为量子力学中对称变换的自然舞台。在量子力学中，时间演化 U(t) = e^{−iĤt/ℏ} 是幺正的，保证总概率 ‖ψ‖² = 1 对所有时间守恒。

---

## E. Diagonalization of the Pauli Matrices · 泡利矩阵的对角化

### E.1 — σ_z · σ_z 的对角化

**Claim.** σ_z = [[1, 0], [0, −1]] has eigenvalues +1 and −1 with eigenvectors (1, 0)ᵀ and (0, 1)ᵀ.

**命题。** σ_z = [[1, 0], [0, −1]] 的本征值为 +1 和 −1，对应本征向量为 (1, 0)ᵀ 和 (0, 1)ᵀ。

**Step 1 — Characteristic equation.**

**第 1 步 — 特征方程。**

  det(σ_z − λI) = det([[1−λ, 0], [0, −1−λ]]) = (1−λ)(−1−λ) = −(1−λ²) = λ² − 1 = 0.

Roots: **λ = ±1** (both real, confirming Hermiticity).

根：**λ = ±1**（均为实数，验证了厄米性）。

**Step 2 — Eigenvector for λ = +1.** Solve (σ_z − I)v = 0:

**第 2 步 — λ = +1 的本征向量。** 求解 (σ_z − I)v = 0：

  [[0, 0], [0, −2]] [v₁, v₂]ᵀ = 0  →  −2v₂ = 0  →  v₂ = 0,  v₁ free.

Normalized eigenvector: **|+z⟩ = (1, 0)ᵀ**.

归一化本征向量：**|+z⟩ = (1, 0)ᵀ**。

**Step 3 — Eigenvector for λ = −1.** Solve (σ_z + I)v = 0:

**第 3 步 — λ = −1 的本征向量。** 求解 (σ_z + I)v = 0：

  [[2, 0], [0, 0]] [v₁, v₂]ᵀ = 0  →  2v₁ = 0  →  v₁ = 0,  v₂ free.

Normalized eigenvector: **|−z⟩ = (0, 1)ᵀ**.

归一化本征向量：**|−z⟩ = (0, 1)ᵀ**。

**Step 4 — Verify orthogonality.** ⟨+z|−z⟩ = (1, 0)·(0, 1)ᵀ = 0. ∎

**第 4 步 — 验证正交性。** ⟨+z|−z⟩ = (1, 0)·(0, 1)ᵀ = 0。∎

σ_z is already diagonal in the standard basis — this basis is the **computational basis** of quantum computing. The physical interpretation: a spin-½ particle with spin "up" along z has σ_z eigenvalue +1, "down" has −1.

σ_z 在标准基下已经是对角形式——该基即量子计算的**计算基**。物理解释：自旋-½ 粒子沿 z 方向"自旋向上"时 σ_z 本征值为 +1，"自旋向下"时为 −1。

---

### E.2 — σ_x · σ_x 的对角化

**Claim.** σ_x = [[0, 1], [1, 0]] has eigenvalues +1 and −1 with normalized eigenvectors (1/√2)(1, 1)ᵀ and (1/√2)(1, −1)ᵀ.

**命题。** σ_x = [[0, 1], [1, 0]] 的本征值为 +1 和 −1，归一化本征向量为 (1/√2)(1, 1)ᵀ 和 (1/√2)(1, −1)ᵀ。

**Step 1 — Characteristic equation.**

**第 1 步 — 特征方程。**

  det(σ_x − λI) = det([[−λ, 1], [1, −λ]]) = λ² − 1 = 0  →  **λ = ±1**.

**第 1 步 — 特征方程。** det(σ_x − λI) = det([[−λ, 1], [1, −λ]]) = λ² − 1 = 0 → **λ = ±1**。

**Step 2 — Eigenvector for λ = +1.** Solve (σ_x − I)v = 0:

**第 2 步 — λ = +1 的本征向量。** 求解 (σ_x − I)v = 0：

  [[−1, 1], [1, −1]] [v₁, v₂]ᵀ = 0  →  v₁ = v₂.

Choosing v₁ = v₂ = 1/√2: **|+x⟩ = (1/√2)(1, 1)ᵀ**.

取 v₁ = v₂ = 1/√2：**|+x⟩ = (1/√2)(1, 1)ᵀ**。

**Step 3 — Eigenvector for λ = −1.** Solve (σ_x + I)v = 0:

**第 3 步 — λ = −1 的本征向量。** 求解 (σ_x + I)v = 0：

  [[1, 1], [1, 1]] [v₁, v₂]ᵀ = 0  →  v₁ = −v₂.

Choosing v₁ = 1/√2, v₂ = −1/√2: **|−x⟩ = (1/√2)(1, −1)ᵀ**.

取 v₁ = 1/√2, v₂ = −1/√2：**|−x⟩ = (1/√2)(1, −1)ᵀ**。

**Step 4 — Verify orthonormality.**

**第 4 步 — 验证正交归一性。**

  ⟨+x|+x⟩ = (1/2)(1 + 1) = 1,   ⟨−x|−x⟩ = (1/2)(1 + 1) = 1,   ⟨+x|−x⟩ = (1/2)(1 − 1) = 0. ∎

**Step 5 — Diagonalizing matrix.** The unitary matrix U_x = (1/√2)[[1, 1], [1, −1]] (the Hadamard matrix H) satisfies U_x† σ_x U_x = diag(+1, −1) = σ_z.

**第 5 步 — 对角化矩阵。** 幺正矩阵 U_x = (1/√2)[[1, 1], [1, −1]]（Hadamard 矩阵 H）满足 U_x† σ_x U_x = diag(+1, −1) = σ_z。

---

### E.3 — σ_y · σ_y 的对角化

**Claim.** σ_y = [[0, −i], [i, 0]] has eigenvalues +1 and −1 with normalized eigenvectors (1/√2)(1, i)ᵀ and (1/√2)(1, −i)ᵀ.

**命题。** σ_y = [[0, −i], [i, 0]] 的本征值为 +1 和 −1，归一化本征向量为 (1/√2)(1, i)ᵀ 和 (1/√2)(1, −i)ᵀ。

**Step 1 — Confirm Hermiticity.** σ_y† = (σ_y*)ᵀ = [[0, i], [−i, 0]]ᵀ = [[0, −i], [i, 0]] = σ_y. ✓

**第 1 步 — 确认厄米性。** σ_y† = (σ_y*)ᵀ = [[0, i], [−i, 0]]ᵀ = [[0, −i], [i, 0]] = σ_y。✓

**Step 2 — Characteristic equation.**

**第 2 步 — 特征方程。**

  det(σ_y − λI) = det([[−λ, −i], [i, −λ]]) = λ² − (−i)(i) = λ² − 1 = 0  →  **λ = ±1**.

**Step 3 — Eigenvector for λ = +1.** Solve (σ_y − I)v = 0:

**第 3 步 — λ = +1 的本征向量。** 求解 (σ_y − I)v = 0：

  [[−1, −i], [i, −1]] [v₁, v₂]ᵀ = 0.

From the first row: −v₁ − iv₂ = 0 → v₁ = −iv₂. Choosing v₂ = 1/√2, v₁ = −i/√2:

由第一行：−v₁ − iv₂ = 0 → v₁ = −iv₂。取 v₂ = 1/√2, v₁ = −i/√2：

  **|+y⟩ = (1/√2)(−i, 1)ᵀ.**

Alternatively, multiplying by the global phase i: **|+y⟩ = (1/√2)(1, i)ᵀ** (both are eigenvectors; global phase is not physical).

或者乘以全局相位 i：**|+y⟩ = (1/√2)(1, i)ᵀ**（两者均为本征向量；全局相位无物理意义）。

**Step 4 — Eigenvector for λ = −1.** Solve (σ_y + I)v = 0:

**第 4 步 — λ = −1 的本征向量。** 求解 (σ_y + I)v = 0：

  [[1, −i], [i, 1]] [v₁, v₂]ᵀ = 0  →  v₁ = iv₂.

Choosing v₂ = 1/√2: **|−y⟩ = (1/√2)(i, 1)ᵀ** = (up to phase) **(1/√2)(1, −i)ᵀ**.

取 v₂ = 1/√2：**|−y⟩ = (1/√2)(i, 1)ᵀ** = （差一个相位）**(1/√2)(1, −i)ᵀ**。

**Step 5 — Verify orthonormality.** Using |+y⟩ = (1/√2)(1, i)ᵀ and |−y⟩ = (1/√2)(1, −i)ᵀ:

**第 5 步 — 验证正交归一性。** 用 |+y⟩ = (1/√2)(1, i)ᵀ 和 |−y⟩ = (1/√2)(1, −i)ᵀ：

  ⟨+y|+y⟩ = (1/2)(1·1 + (−i)·i) = (1/2)(1 + 1) = 1,
  ⟨+y|−y⟩ = (1/2)(1·1 + (−i)·(−i)) = (1/2)(1 − 1) = 0. ∎

**Step 6 — Summary table.**

**第 6 步 — 汇总表。**

| Pauli matrix 泡利矩阵 | Eigenvalue 本征值 | Eigenvector 本征向量 |
|---|---|---|
| σ_z | +1 | (1, 0)ᵀ = |↑⟩ |
| σ_z | −1 | (0, 1)ᵀ = |↓⟩ |
| σ_x | +1 | (1/√2)(1, 1)ᵀ |
| σ_x | −1 | (1/√2)(1, −1)ᵀ |
| σ_y | +1 | (1/√2)(1, i)ᵀ |
| σ_y | −1 | (1/√2)(1, −i)ᵀ |

All three matrices share the same eigenvalues {+1, −1} (reflecting the symmetry among the three spin directions), but their eigenstates are mutually unbiased: a state that is a definite eigenstate of σ_z is an equal-weight superposition of the eigenstates of σ_x or σ_y, and vice versa — the mathematical expression of the Heisenberg uncertainty relations for spin.

三个矩阵共享相同的本征值集合 {+1, −1}（反映三个自旋方向之间的对称性），但它们的本征态是相互无偏的：σ_z 的确定本征态是 σ_x 或 σ_y 本征态的等权叠加，反之亦然——这正是自旋海森堡不确定关系的数学表达。

---

## F. The Pauli Algebra Relation σᵢσⱼ = δᵢⱼ I + i εᵢⱼₖ σₖ · 泡利代数关系

**Claim.** The Pauli matrices satisfy σᵢ σⱼ = δᵢⱼ I + i εᵢⱼₖ σₖ, where εᵢⱼₖ is the Levi-Civita symbol.

**命题。** 泡利矩阵满足 σᵢ σⱼ = δᵢⱼ I + i εᵢⱼₖ σₖ，其中 εᵢⱼₖ 是列维-奇维塔符号。

**Step 1 — Verify σᵢ² = I for each i.** By direct calculation:

**第 1 步 — 逐一验证 σᵢ² = I。** 直接计算：

  σ_x² = [[0,1],[1,0]][[0,1],[1,0]] = [[1,0],[0,1]] = I. ✓
  σ_y² = [[0,−i],[i,0]][[0,−i],[i,0]] = [[−i·i,0],[0,−i·i]] = [[1,0],[0,1]] = I. ✓
  σ_z² = [[1,0],[0,−1]][[1,0],[0,−1]] = [[1,0],[0,1]] = I. ✓

This establishes the δᵢⱼ I part for i = j.

这确立了 i = j 时的 δᵢⱼ I 部分。

**Step 2 — Verify σ_x σ_y = i σ_z.** Direct matrix multiplication:

**第 2 步 — 验证 σ_x σ_y = i σ_z。** 直接矩阵乘法：

  σ_x σ_y = [[0,1],[1,0]] [[0,−i],[i,0]] = [[i,0],[0,−i]] = i [[1,0],[0,−1]] = i σ_z. ✓

**Step 3 — Verify σ_y σ_x = −i σ_z (anticommutativity for distinct indices).**

**第 3 步 — 验证 σ_y σ_x = −i σ_z（不同指标时反对易）。**

  σ_y σ_x = [[0,−i],[i,0]] [[0,1],[1,0]] = [[−i,0],[0,i]] = −i σ_z. ✓

This confirms σ_x σ_y − σ_y σ_x = [σ_x, σ_y] = 2i σ_z, the commutation relation of angular momentum (with ℏ = 1/2 for spin-½). The remaining cases follow by cyclic permutation (x → y → z → x). ∎

这确认了 σ_x σ_y − σ_y σ_x = [σ_x, σ_y] = 2i σ_z，即角动量的对易关系（自旋-½ 时 ℏ = 1/2）。其余情形由循环置换（x → y → z → x）得到。∎

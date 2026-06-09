# Derivations — Module 0.2: Linear Algebra
# 推导 — 模块 0.2：线性代数

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.2](./module-0.2-linear-algebra.md). Full step-by-step proofs of every non-trivial result stated there: real eigenvalues and orthogonality of eigenvectors of Hermitian operators, the spectral theorem, norm-preservation by unitary operators, and explicit diagonalization of all three Pauli matrices. English first, then 中文.
> [模块 0.2](./module-0.2-linear-algebra.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：厄米算符本征值为实数且本征向量正交、谱定理、幺正算符保持范数、以及三个泡利矩阵的显式对角化。先英文，后中文。

---

## A. Hermitian Operators Have Real Eigenvalues · 厄米算符的本征值为实数

**Claim.** If $A$ is a Hermitian operator ($A = A^\dagger$) on an inner-product space, and $Av = \lambda v$ with $v \ne 0$, then $\lambda \in \mathbb{R}$.

**命题。** 若 $A$ 是内积空间上的厄米算符（$A = A^\dagger$），且 $Av = \lambda v$，$v \ne 0$，则 $\lambda \in \mathbb{R}$。

**Step 1 — Compute $\langle v|Av\rangle$ two ways.** Since $Av = \lambda v$, the left side is simply

**第 1 步 — 用两种方式计算 $\langle v|Av\rangle$。** 由 $Av = \lambda v$，左侧直接得到

$$ \langle v|Av\rangle = \langle v|\lambda v\rangle = \lambda\langle v|v\rangle. $$

**Step 2 — Use Hermiticity.** Because $A = A^\dagger$, the definition of the adjoint gives $\langle v|Av\rangle = \langle A^\dagger v|v\rangle = \langle Av|v\rangle$. Applying the eigenvalue equation again:

**第 2 步 — 利用厄米性。** 由 $A = A^\dagger$，伴随算符的定义给出 $\langle v|Av\rangle = \langle A^\dagger v|v\rangle = \langle Av|v\rangle$。再次代入本征值方程：

$$ \langle Av|v\rangle = \langle \lambda v|v\rangle = \lambda^* \langle v|v\rangle. $$

(The complex conjugate arises because the inner product is conjugate-linear in the first argument.)

（复共轭出现是因为内积对第一个参数是共轭线性的。）

**Step 3 — Equate and conclude.** Combining Steps 1 and 2:

**第 3 步 — 令二式相等并得出结论。** 结合第 1、2 步：

$$ \lambda\langle v|v\rangle = \lambda^* \langle v|v\rangle. $$

Since $v \ne 0$, $\langle v|v\rangle > 0$ (by positive-definiteness of the inner product). Dividing both sides by $\langle v|v\rangle$:

由于 $v \ne 0$，$\langle v|v\rangle > 0$（内积的正定性）。两端除以 $\langle v|v\rangle$：

$$ \lambda = \lambda^*, $$

which means $\lambda$ is real. $\blacksquare$

即 $\lambda$ 为实数。$\blacksquare$

**Physical significance.** Quantum observables are Hermitian operators. This theorem guarantees that every measurement result (eigenvalue) is a real number — a physical necessity, since measuring energy or momentum always yields a real value.

**物理意义。** 量子可观测量是厄米算符。此定理保证每次测量结果（本征值）都是实数——这是物理必要性，因为测量能量或动量总是得到实数。

---

## B. Eigenvectors of a Hermitian Operator for Distinct Eigenvalues Are Orthogonal · 不同本征值对应的本征向量正交

**Claim.** Let $A = A^\dagger$ and suppose $A v_m = \lambda_m v_m$ and $A v_n = \lambda_n v_n$ with $\lambda_m \ne \lambda_n$. Then $\langle v_m|v_n\rangle = 0$.

**命题。** 设 $A = A^\dagger$，且 $A v_m = \lambda_m v_m$，$A v_n = \lambda_n v_n$，$\lambda_m \ne \lambda_n$。则 $\langle v_m|v_n\rangle = 0$。

**Step 1 — Compute $\langle v_m|A v_n\rangle$ directly.** Using the eigenvalue equation for $v_n$:

**第 1 步 — 直接计算 $\langle v_m|A v_n\rangle$。** 利用 $v_n$ 的本征值方程：

$$ \langle v_m|A v_n\rangle = \langle v_m|\lambda_n v_n\rangle = \lambda_n \langle v_m|v_n\rangle. $$

**Step 2 — Compute $\langle v_m|A v_n\rangle$ using Hermiticity.** Since $A = A^\dagger$:

**第 2 步 — 利用厄米性计算 $\langle v_m|A v_n\rangle$。** 由 $A = A^\dagger$：

$$ \langle v_m|A v_n\rangle = \langle A v_m|v_n\rangle = \langle \lambda_m v_m|v_n\rangle = \lambda_m^* \langle v_m|v_n\rangle = \lambda_m \langle v_m|v_n\rangle. $$

In the last step we used that $\lambda_m$ is real (proved in Section A), so $\lambda_m^* = \lambda_m$.

最后一步用到了 $\lambda_m$ 为实数（已在 A 节证明），故 $\lambda_m^* = \lambda_m$。

**Step 3 — Subtract and conclude.**

**第 3 步 — 作差并得出结论。**

$$ \begin{aligned} \lambda_n \langle v_m|v_n\rangle &= \lambda_m \langle v_m|v_n\rangle \\ (\lambda_n - \lambda_m) \langle v_m|v_n\rangle &= 0. \end{aligned} $$

Since $\lambda_n \ne \lambda_m$, the factor $(\lambda_n - \lambda_m) \ne 0$, so we must have $\langle v_m|v_n\rangle = 0$. $\blacksquare$

由于 $\lambda_n \ne \lambda_m$，因子 $(\lambda_n - \lambda_m) \ne 0$，故必有 $\langle v_m|v_n\rangle = 0$。$\blacksquare$

**Remark on degenerate eigenvalues.** If $\lambda_m = \lambda_n$ but $v_m$ and $v_n$ are linearly independent, the above argument does not force orthogonality. However, within the degenerate eigenspace one can always choose an orthogonal basis by the Gram–Schmidt procedure. The spectral theorem (Section C) accounts for this.

**关于简并本征值的说明。** 若 $\lambda_m = \lambda_n$ 但 $v_m$ 与 $v_n$ 线性无关，上述论证不能强制正交性。然而，在简并本征子空间内，总可以通过格拉姆–施密特方法选取正交基。谱定理（C 节）对此有完整的描述。

---

## C. The Spectral Theorem · 谱定理

**Statement.** Every Hermitian operator $A$ on a finite-dimensional complex inner-product space has the following properties:
1. All eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$ are real.
2. There exists an orthonormal basis $\{v_1, v_2, \ldots, v_n\}$ of eigenvectors of $A$.
3. $A$ can be written in the spectral decomposition $A = \sum_k \lambda_k |v_k\rangle\langle v_k|$.

**陈述。** 有限维复内积空间上的每一个厄米算符 $A$ 具有以下性质：
1. 所有本征值 $\lambda_1, \lambda_2, \ldots, \lambda_n$ 均为实数。
2. 存在由 $A$ 的本征向量构成的正交归一基 $\{v_1, v_2, \ldots, v_n\}$。
3. $A$ 可以写成谱分解形式 $A = \sum_k \lambda_k |v_k\rangle\langle v_k|$。

**Step 1 — Existence of at least one eigenvalue.** Over $\mathbb{C}$ the characteristic polynomial $\det(A - \lambda I)$ of degree $n$ always has at least one root $\lambda_1$ (fundamental theorem of algebra). By Section A, $\lambda_1 \in \mathbb{R}$, with eigenvector $v_1$.

**第 1 步 — 至少一个本征值的存在性。** 在 $\mathbb{C}$ 上，$n$ 次特征多项式 $\det(A - \lambda I)$ 至少有一个根 $\lambda_1$（代数基本定理）。由 A 节，$\lambda_1 \in \mathbb{R}$，对应本征向量 $v_1$。

**Step 2 — Reduction to a smaller space.** Let $W = \{v_1\}^\perp$ be the orthogonal complement of $v_1$. We show that $A$ maps $W$ into $W$: for any $w \in W$,

**第 2 步 — 归约到更小空间。** 令 $W = \{v_1\}^\perp$ 为 $v_1$ 的正交补。我们证明 $A$ 将 $W$ 映射到 $W$：对任意 $w \in W$，

$$ \langle v_1|Aw\rangle = \langle A v_1|w\rangle = \langle \lambda_1 v_1|w\rangle = \lambda_1 \langle v_1|w\rangle = 0. $$

So $Aw \in W$. The restriction $A|_W$ is again Hermitian on the $(n-1)$-dimensional space $W$.

故 $Aw \in W$。限制算符 $A|_W$ 在 $(n-1)$ 维空间 $W$ 上仍是厄米的。

**Step 3 — Induction.** Apply Steps 1–2 to $A|_W$ to get a second eigenvalue $\lambda_2$ and eigenvector $v_2 \in W$, hence $\langle v_1|v_2\rangle = 0$. Continuing by induction, after $n$ steps we obtain $n$ mutually orthogonal eigenvectors $v_1, \ldots, v_n$ that span the full $n$-dimensional space — an orthonormal eigenbasis after normalization.

**第 3 步 — 归纳法。** 对 $A|_W$ 重复第 1–2 步，得到第二个本征值 $\lambda_2$ 和本征向量 $v_2 \in W$，从而 $\langle v_1|v_2\rangle = 0$。继续归纳，经过 $n$ 步后得到 $n$ 个相互正交的本征向量 $v_1, \ldots, v_n$，它们张成整个 $n$ 维空间——归一化后即为正交归一本征基。

**Step 4 — Spectral decomposition.** In the orthonormal eigenbasis, $A$ is diagonal with entries $\lambda_k$. The resolution of the identity is $I = \sum_k |v_k\rangle\langle v_k|$. Acting with $A$:

**第 4 步 — 谱分解。** 在正交归一本征基下，$A$ 是以 $\lambda_k$ 为对角元的对角矩阵。单位算符的分解为 $I = \sum_k |v_k\rangle\langle v_k|$。用 $A$ 作用：

$$ A = AI = A \sum_k |v_k\rangle\langle v_k| = \sum_k (A|v_k\rangle)\langle v_k| = \sum_k \lambda_k |v_k\rangle\langle v_k|. \qquad \blacksquare $$

**Infinite-dimensional remark.** For self-adjoint operators on infinite-dimensional Hilbert spaces (the case relevant to quantum mechanics), the spectral theorem requires more functional analysis (the theory of unbounded operators). The conclusion stands: real spectrum, complete orthogonal eigenbasis (or, for continuous spectrum, a spectral measure), and the ability to write functions $f(A) = \sum_k f(\lambda_k)|v_k\rangle\langle v_k|$.

**无穷维说明。** 对于无穷维希尔伯特空间上的自伴算符（量子力学相关情形），谱定理需要更多泛函分析（无界算符理论）。结论不变：实谱、完备正交本征基（或对连续谱，谱测度），以及可以写出 $f(A) = \sum_k f(\lambda_k)|v_k\rangle\langle v_k|$。

---

## D. Unitary Operators Preserve the Norm · 幺正算符保持范数

**Claim.** If $U^\dagger U = I$ ($U$ is unitary), then $\lVert Uv\rVert = \lVert v\rVert$ for every vector $v$.

**命题。** 若 $U^\dagger U = I$（$U$ 为幺正算符），则对每个向量 $v$ 有 $\lVert Uv\rVert = \lVert v\rVert$。

**Step 1 — Express the norm of $Uv$.** By definition of the norm,

**第 1 步 — 表达 $Uv$ 的范数。** 由范数的定义，

$$ \lVert Uv\rVert^2 = \langle Uv|Uv\rangle. $$

**Step 2 — Rewrite using the adjoint.** The inner product satisfies $\langle Au|w\rangle = \langle u|A^\dagger w\rangle$, so

**第 2 步 — 用伴随算符改写。** 内积满足 $\langle Au|w\rangle = \langle u|A^\dagger w\rangle$，故

$$ \langle Uv|Uv\rangle = \langle v|U^\dagger Uv\rangle. $$

**Step 3 — Apply the unitary condition.**

**第 3 步 — 应用幺正条件。**

$$ \langle v|U^\dagger Uv\rangle = \langle v|Iv\rangle = \langle v|v\rangle = \lVert v\rVert^2. $$

**Step 4 — Conclude.** Therefore $\lVert Uv\rVert^2 = \lVert v\rVert^2$, and since norms are non-negative, $\lVert Uv\rVert = \lVert v\rVert$. $\blacksquare$

**第 4 步 — 结论。** 因此 $\lVert Uv\rVert^2 = \lVert v\rVert^2$，由于范数非负，$\lVert Uv\rVert = \lVert v\rVert$。$\blacksquare$

**Corollary — Unitary operators preserve the inner product.** More strongly, $\langle Uu|Uv\rangle = \langle u|v\rangle$ for all $u, v$. Proof: $\langle Uu|Uv\rangle = \langle u|U^\dagger Uv\rangle = \langle u|v\rangle$. This means unitary transformations are precisely the isometries (distance-preserving maps) of the Hilbert space, making them the natural arena for symmetry transformations in quantum mechanics. In QM, time evolution $U(t) = e^{-i\hat H t/\hbar}$ is unitary, ensuring that total probability $\lVert\psi\rVert^2 = 1$ is conserved for all time.

**推论——幺正算符保持内积。** 更强地，对所有 $u, v$ 有 $\langle Uu|Uv\rangle = \langle u|v\rangle$。证明：$\langle Uu|Uv\rangle = \langle u|U^\dagger Uv\rangle = \langle u|v\rangle$。这意味着幺正变换恰好是希尔伯特空间的等距映射（保距映射），使其成为量子力学中对称变换的自然舞台。在量子力学中，时间演化 $U(t) = e^{-i\hat H t/\hbar}$ 是幺正的，保证总概率 $\lVert\psi\rVert^2 = 1$ 对所有时间守恒。

---

## E. Diagonalization of the Pauli Matrices · 泡利矩阵的对角化

### E.1 — $\sigma_z$ · $\sigma_z$ 的对角化

**Claim.** $\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ has eigenvalues $+1$ and $-1$ with eigenvectors $(1, 0)^\mathsf{T}$ and $(0, 1)^\mathsf{T}$.

**命题。** $\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ 的本征值为 $+1$ 和 $-1$，对应本征向量为 $(1, 0)^\mathsf{T}$ 和 $(0, 1)^\mathsf{T}$。

**Step 1 — Characteristic equation.**

**第 1 步 — 特征方程。**

$$ \det(\sigma_z - \lambda I) = \det\begin{pmatrix} 1-\lambda & 0 \\ 0 & -1-\lambda \end{pmatrix} = (1-\lambda)(-1-\lambda) = -(1-\lambda^2) = \lambda^2 - 1 = 0. $$

Roots: $\boldsymbol{\lambda = \pm 1}$ (both real, confirming Hermiticity).

根：$\boldsymbol{\lambda = \pm 1}$（均为实数，验证了厄米性）。

**Step 2 — Eigenvector for $\lambda = +1$.** Solve $(\sigma_z - I)v = 0$:

**第 2 步 — $\lambda = +1$ 的本征向量。** 求解 $(\sigma_z - I)v = 0$：

$$ \begin{pmatrix} 0 & 0 \\ 0 & -2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \;\to\; -2 v_2 = 0 \;\to\; v_2 = 0, \; v_1 \text{ free}. $$

Normalized eigenvector: $\boldsymbol{|{+}z\rangle = (1, 0)^\mathsf{T}}$.

归一化本征向量：$\boldsymbol{|{+}z\rangle = (1, 0)^\mathsf{T}}$。

**Step 3 — Eigenvector for $\lambda = -1$.** Solve $(\sigma_z + I)v = 0$:

**第 3 步 — $\lambda = -1$ 的本征向量。** 求解 $(\sigma_z + I)v = 0$：

$$ \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \;\to\; 2 v_1 = 0 \;\to\; v_1 = 0, \; v_2 \text{ free}. $$

Normalized eigenvector: $\boldsymbol{|{-}z\rangle = (0, 1)^\mathsf{T}}$.

归一化本征向量：$\boldsymbol{|{-}z\rangle = (0, 1)^\mathsf{T}}$。

**Step 4 — Verify orthogonality.** $\langle {+}z|{-}z\rangle = (1, 0)\cdot(0, 1)^\mathsf{T} = 0$. $\blacksquare$

**第 4 步 — 验证正交性。** $\langle {+}z|{-}z\rangle = (1, 0)\cdot(0, 1)^\mathsf{T} = 0$。$\blacksquare$

$\sigma_z$ is already diagonal in the standard basis — this basis is the **computational basis** of quantum computing. The physical interpretation: a spin-½ particle with spin "up" along $z$ has $\sigma_z$ eigenvalue $+1$, "down" has $-1$.

$\sigma_z$ 在标准基下已经是对角形式——该基即量子计算的**计算基**。物理解释：自旋-½ 粒子沿 $z$ 方向"自旋向上"时 $\sigma_z$ 本征值为 $+1$，"自旋向下"时为 $-1$。

---

### E.2 — $\sigma_x$ · $\sigma_x$ 的对角化

**Claim.** $\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $+1$ and $-1$ with normalized eigenvectors $(1/\sqrt2)(1, 1)^\mathsf{T}$ and $(1/\sqrt2)(1, -1)^\mathsf{T}$.

**命题。** $\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ 的本征值为 $+1$ 和 $-1$，归一化本征向量为 $(1/\sqrt2)(1, 1)^\mathsf{T}$ 和 $(1/\sqrt2)(1, -1)^\mathsf{T}$。

**Step 1 — Characteristic equation.**

**第 1 步 — 特征方程。**

$$ \det(\sigma_x - \lambda I) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = 0 \;\to\; \boldsymbol{\lambda = \pm 1}. $$

**第 1 步 — 特征方程。** $\det(\sigma_x - \lambda I) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = 0 \to \boldsymbol{\lambda = \pm 1}$。

**Step 2 — Eigenvector for $\lambda = +1$.** Solve $(\sigma_x - I)v = 0$:

**第 2 步 — $\lambda = +1$ 的本征向量。** 求解 $(\sigma_x - I)v = 0$：

$$ \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \;\to\; v_1 = v_2. $$

Choosing $v_1 = v_2 = 1/\sqrt2$: $\boldsymbol{|{+}x\rangle = (1/\sqrt2)(1, 1)^\mathsf{T}}$.

取 $v_1 = v_2 = 1/\sqrt2$：$\boldsymbol{|{+}x\rangle = (1/\sqrt2)(1, 1)^\mathsf{T}}$。

**Step 3 — Eigenvector for $\lambda = -1$.** Solve $(\sigma_x + I)v = 0$:

**第 3 步 — $\lambda = -1$ 的本征向量。** 求解 $(\sigma_x + I)v = 0$：

$$ \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \;\to\; v_1 = -v_2. $$

Choosing $v_1 = 1/\sqrt2$, $v_2 = -1/\sqrt2$: $\boldsymbol{|{-}x\rangle = (1/\sqrt2)(1, -1)^\mathsf{T}}$.

取 $v_1 = 1/\sqrt2, v_2 = -1/\sqrt2$：$\boldsymbol{|{-}x\rangle = (1/\sqrt2)(1, -1)^\mathsf{T}}$。

**Step 4 — Verify orthonormality.**

**第 4 步 — 验证正交归一性。**

$$ \langle {+}x|{+}x\rangle = \tfrac12(1 + 1) = 1, \quad \langle {-}x|{-}x\rangle = \tfrac12(1 + 1) = 1, \quad \langle {+}x|{-}x\rangle = \tfrac12(1 - 1) = 0. \qquad \blacksquare $$

**Step 5 — Diagonalizing matrix.** The unitary matrix $U_x = (1/\sqrt2)\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ (the Hadamard matrix $H$) satisfies $U_x^\dagger \sigma_x U_x = \operatorname{diag}(+1, -1) = \sigma_z$.

**第 5 步 — 对角化矩阵。** 幺正矩阵 $U_x = (1/\sqrt2)\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$（Hadamard 矩阵 $H$）满足 $U_x^\dagger \sigma_x U_x = \operatorname{diag}(+1, -1) = \sigma_z$。

---

### E.3 — $\sigma_y$ · $\sigma_y$ 的对角化

**Claim.** $\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ has eigenvalues $+1$ and $-1$ with normalized eigenvectors $(1/\sqrt2)(1, i)^\mathsf{T}$ and $(1/\sqrt2)(1, -i)^\mathsf{T}$.

**命题。** $\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ 的本征值为 $+1$ 和 $-1$，归一化本征向量为 $(1/\sqrt2)(1, i)^\mathsf{T}$ 和 $(1/\sqrt2)(1, -i)^\mathsf{T}$。

**Step 1 — Confirm Hermiticity.** $\sigma_y^\dagger = (\sigma_y^*)^\mathsf{T} = \begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}^\mathsf{T} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \sigma_y$. ✓

**第 1 步 — 确认厄米性。** $\sigma_y^\dagger = (\sigma_y^*)^\mathsf{T} = \begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}^\mathsf{T} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \sigma_y$。✓

**Step 2 — Characteristic equation.**

**第 2 步 — 特征方程。**

$$ \det(\sigma_y - \lambda I) = \det\begin{pmatrix} -\lambda & -i \\ i & -\lambda \end{pmatrix} = \lambda^2 - (-i)(i) = \lambda^2 - 1 = 0 \;\to\; \boldsymbol{\lambda = \pm 1}. $$

**Step 3 — Eigenvector for $\lambda = +1$.** Solve $(\sigma_y - I)v = 0$:

**第 3 步 — $\lambda = +1$ 的本征向量。** 求解 $(\sigma_y - I)v = 0$：

$$ \begin{pmatrix} -1 & -i \\ i & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0. $$

From the first row: $-v_1 - i v_2 = 0 \to v_1 = -i v_2$. Choosing $v_2 = 1/\sqrt2$, $v_1 = -i/\sqrt2$:

由第一行：$-v_1 - i v_2 = 0 \to v_1 = -i v_2$。取 $v_2 = 1/\sqrt2, v_1 = -i/\sqrt2$：

$$ \boldsymbol{|{+}y\rangle = (1/\sqrt2)(-i, 1)^\mathsf{T}.} $$

Alternatively, multiplying by the global phase $i$: $\boldsymbol{|{+}y\rangle = (1/\sqrt2)(1, i)^\mathsf{T}}$ (both are eigenvectors; global phase is not physical).

或者乘以全局相位 $i$：$\boldsymbol{|{+}y\rangle = (1/\sqrt2)(1, i)^\mathsf{T}}$（两者均为本征向量；全局相位无物理意义）。

**Step 4 — Eigenvector for $\lambda = -1$.** Solve $(\sigma_y + I)v = 0$:

**第 4 步 — $\lambda = -1$ 的本征向量。** 求解 $(\sigma_y + I)v = 0$：

$$ \begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \;\to\; v_1 = i v_2. $$

Choosing $v_2 = 1/\sqrt2$: $\boldsymbol{|{-}y\rangle = (1/\sqrt2)(i, 1)^\mathsf{T}}$ = (up to phase) $\boldsymbol{(1/\sqrt2)(1, -i)^\mathsf{T}}$.

取 $v_2 = 1/\sqrt2$：$\boldsymbol{|{-}y\rangle = (1/\sqrt2)(i, 1)^\mathsf{T}}$ = （差一个相位）$\boldsymbol{(1/\sqrt2)(1, -i)^\mathsf{T}}$。

**Step 5 — Verify orthonormality.** Using $|{+}y\rangle = (1/\sqrt2)(1, i)^\mathsf{T}$ and $|{-}y\rangle = (1/\sqrt2)(1, -i)^\mathsf{T}$:

**第 5 步 — 验证正交归一性。** 用 $|{+}y\rangle = (1/\sqrt2)(1, i)^\mathsf{T}$ 和 $|{-}y\rangle = (1/\sqrt2)(1, -i)^\mathsf{T}$：

$$ \begin{aligned} \langle {+}y|{+}y\rangle &= \tfrac12(1\cdot 1 + (-i)\cdot i) = \tfrac12(1 + 1) = 1, \\ \langle {+}y|{-}y\rangle &= \tfrac12(1\cdot 1 + (-i)\cdot(-i)) = \tfrac12(1 - 1) = 0. \end{aligned} \qquad \blacksquare $$

**Step 6 — Summary table.**

**第 6 步 — 汇总表。**

| Pauli matrix 泡利矩阵 | Eigenvalue 本征值 | Eigenvector 本征向量 |
|---|---|---|
| $\sigma_z$ | $+1$ | $(1, 0)^\mathsf{T} = \lvert{\uparrow}\rangle$ |
| $\sigma_z$ | $-1$ | $(0, 1)^\mathsf{T} = \lvert{\downarrow}\rangle$ |
| $\sigma_x$ | $+1$ | $(1/\sqrt2)(1, 1)^\mathsf{T}$ |
| $\sigma_x$ | $-1$ | $(1/\sqrt2)(1, -1)^\mathsf{T}$ |
| $\sigma_y$ | $+1$ | $(1/\sqrt2)(1, i)^\mathsf{T}$ |
| $\sigma_y$ | $-1$ | $(1/\sqrt2)(1, -i)^\mathsf{T}$ |

All three matrices share the same eigenvalues $\{+1, -1\}$ (reflecting the symmetry among the three spin directions), but their eigenstates are mutually unbiased: a state that is a definite eigenstate of $\sigma_z$ is an equal-weight superposition of the eigenstates of $\sigma_x$ or $\sigma_y$, and vice versa — the mathematical expression of the Heisenberg uncertainty relations for spin.

三个矩阵共享相同的本征值集合 $\{+1, -1\}$（反映三个自旋方向之间的对称性），但它们的本征态是相互无偏的：$\sigma_z$ 的确定本征态是 $\sigma_x$ 或 $\sigma_y$ 本征态的等权叠加，反之亦然——这正是自旋海森堡不确定关系的数学表达。

---

## F. The Pauli Algebra Relation $\sigma_i\sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k$ · 泡利代数关系

**Claim.** The Pauli matrices satisfy $\sigma_i \sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k$, where $\varepsilon_{ijk}$ is the Levi-Civita symbol.

**命题。** 泡利矩阵满足 $\sigma_i \sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k$，其中 $\varepsilon_{ijk}$ 是列维-奇维塔符号。

**Step 1 — Verify $\sigma_i^2 = I$ for each $i$.** By direct calculation:

**第 1 步 — 逐一验证 $\sigma_i^2 = I$。** 直接计算：

$$ \begin{aligned} \sigma_x^2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I, \quad\checkmark \\ \sigma_y^2 &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} -i\cdot i & 0 \\ 0 & -i\cdot i \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I, \quad\checkmark \\ \sigma_z^2 &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I. \quad\checkmark \end{aligned} $$

This establishes the $\delta_{ij} I$ part for $i = j$.

这确立了 $i = j$ 时的 $\delta_{ij} I$ 部分。

**Step 2 — Verify $\sigma_x \sigma_y = i \sigma_z$.** Direct matrix multiplication:

**第 2 步 — 验证 $\sigma_x \sigma_y = i \sigma_z$。** 直接矩阵乘法：

$$ \sigma_x \sigma_y = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = i \sigma_z. \quad\checkmark $$

**Step 3 — Verify $\sigma_y \sigma_x = -i \sigma_z$ (anticommutativity for distinct indices).**

**第 3 步 — 验证 $\sigma_y \sigma_x = -i \sigma_z$（不同指标时反对易）。**

$$ \sigma_y \sigma_x = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = -i \sigma_z. \quad\checkmark $$

This confirms $\sigma_x \sigma_y - \sigma_y \sigma_x = [\sigma_x, \sigma_y] = 2i \sigma_z$, the commutation relation of angular momentum (with $\hbar = 1/2$ for spin-½). The remaining cases follow by cyclic permutation ($x \to y \to z \to x$). $\blacksquare$

这确认了 $\sigma_x \sigma_y - \sigma_y \sigma_x = [\sigma_x, \sigma_y] = 2i \sigma_z$，即角动量的对易关系（自旋-½ 时 $\hbar = 1/2$）。其余情形由循环置换（$x \to y \to z \to x$）得到。$\blacksquare$

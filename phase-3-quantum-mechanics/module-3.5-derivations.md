# Derivations — Module 3.5: Identical Particles
# 推导 — 模块 3.5：全同粒子

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.5](./module-3.5-identical-particles.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.5](./module-3.5-identical-particles.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Exchange Operator Has Eigenvalues $\pm1$ and Is Conserved · 交换算符的本征值为 $\pm1$ 且守恒

**Claim.** The exchange operator $\hat{P}_{12}$ defined by $\hat{P}_{12}\,\psi(1,2) = \psi(2,1)$ has eigenvalues $\pm1$. Moreover, if $[\hat{H}, \hat{P}_{12}] = 0$ (which holds whenever particles 1 and 2 are identical), then $\hat{P}_{12}$ is a conserved quantity: a state symmetric (antisymmetric) under exchange remains so for all time.

**命题。** 由 $\hat{P}_{12}\,\psi(1,2) = \psi(2,1)$ 定义的交换算符 $\hat{P}_{12}$ 的本征值为 $\pm1$。此外，若 $[\hat{H}, \hat{P}_{12}] = 0$（当粒子 1 和 2 全同时总成立），则 $\hat{P}_{12}$ 是守恒量：在交换下对称（反对称）的态将始终保持对称（反对称）。

**Step 1 — $\hat{P}_{12}$ is its own inverse.** Applying the exchange operator twice returns to the original state:

**第 1 步 — $\hat{P}_{12}$ 是自身的逆。** 两次应用交换算符回到原始态：

$$ \hat{P}_{12}^2\,\psi(1,2) = \hat{P}_{12}\,\psi(2,1) = \psi(1,2). $$

So $\hat{P}_{12}^2 = \hat{1}$ (the identity operator).

故 $\hat{P}_{12}^2 = \hat{1}$（恒等算符）。

**Step 2 — $\hat{P}_{12}$ is Hermitian.** For any two-particle states $\varphi$ and $\psi$:

**第 2 步 — $\hat{P}_{12}$ 是厄米的。** 对任意两粒子态 $\varphi$ 和 $\psi$：

$$ \langle\varphi|\hat{P}_{12}|\psi\rangle = \int\!\!\int \varphi^*(1,2)\,\psi(2,1)\,d1\,d2. $$

Rename integration variables ($1 \leftrightarrow 2$) — this is just relabeling dummy variables:

重命名积分变量（$1 \leftrightarrow 2$）——这只是重新标记哑变量：

$$ = \int\!\!\int \varphi^*(2,1)\,\psi(1,2)\,d1\,d2 = \langle\hat{P}_{12}\varphi|\psi\rangle. $$

So $\hat{P}_{12}^\dagger = \hat{P}_{12}$ — $\hat{P}_{12}$ is Hermitian (in fact, unitary and Hermitian, hence $\hat{P}_{12}^2 = 1$ is consistent). $\blacksquare$

故 $\hat{P}_{12}^\dagger = \hat{P}_{12}$——$\hat{P}_{12}$ 是厄米的（实际上是幺正且厄米的，因此 $\hat{P}_{12}^2 = 1$ 是自洽的）。$\blacksquare$

**Step 3 — Eigenvalues.** Let $\hat{P}_{12}|\psi\rangle = \lambda|\psi\rangle$. From $\hat{P}_{12}^2 = \hat{1}$:

**第 3 步 — 本征值。** 设 $\hat{P}_{12}|\psi\rangle = \lambda|\psi\rangle$。由 $\hat{P}_{12}^2 = \hat{1}$：

$$ \hat{P}_{12}^2|\psi\rangle = \lambda^2|\psi\rangle = 1\cdot|\psi\rangle, $$

so $\lambda^2 = 1$, giving $\lambda = +1$ (symmetric) or $\lambda = -1$ (antisymmetric). $\blacksquare$

故 $\lambda^2 = 1$，即 $\lambda = +1$（对称）或 $\lambda = -1$（反对称）。$\blacksquare$

**Step 4 — Conservation: $[\hat{H}, \hat{P}_{12}] = 0$ for identical particles.** The Hamiltonian of two identical particles has the form $\hat{H} = \hat{T}_1 + \hat{T}_2 + \hat{V}(1,2)$, where $\hat{V}(1,2) = \hat{V}(2,1)$ (the interaction is symmetric — swapping identical particles cannot change physics). Also $\hat{T}_1 + \hat{T}_2$ is symmetric. Therefore:

**第 4 步 — 守恒：全同粒子的 $[\hat{H}, \hat{P}_{12}] = 0$。** 两个全同粒子的哈密顿量形如 $\hat{H} = \hat{T}_1 + \hat{T}_2 + \hat{V}(1,2)$，其中 $\hat{V}(1,2) = \hat{V}(2,1)$（相互作用是对称的——交换全同粒子不改变物理）。$\hat{T}_1 + \hat{T}_2$ 也是对称的。因此：

$$ \hat{P}_{12}\,\hat{H}\,\psi(1,2) = \hat{H}(2,1)\,\psi(2,1), \qquad \text{and} \qquad \hat{H}\,\hat{P}_{12}\,\psi(1,2) = \hat{H}(1,2)\,\psi(2,1). $$

Since $\hat{H}(1,2) = \hat{H}(2,1)$ for identical particles, $[\hat{H}, \hat{P}_{12}] = 0$.

由于对全同粒子 $\hat{H}(1,2) = \hat{H}(2,1)$，故 $[\hat{H}, \hat{P}_{12}] = 0$。

**Step 5 — Conservation in time.** From the Schrödinger equation, the time evolution of $\langle\hat{P}_{12}\rangle$ obeys:

**第 5 步 — 时间守恒。** 由薛定谔方程，$\langle\hat{P}_{12}\rangle$ 的时间演化满足：

$$ d\langle\hat{P}_{12}\rangle/dt = (i/\hbar)\langle[\hat{H}, \hat{P}_{12}]\rangle + \partial\langle\hat{P}_{12}\rangle/\partial t = 0 + 0 = 0. $$

($\hat{P}_{12}$ has no explicit time dependence.) More concretely, if $\psi(t=0) = \hat{P}_{12}\,\psi(t=0)$ (symmetric), then:

（$\hat{P}_{12}$ 没有显式时间依赖。）更具体地，若 $\psi(t=0) = \hat{P}_{12}\,\psi(t=0)$（对称），则：

$$ \hat{P}_{12}\,\psi(t) = \hat{P}_{12}\,e^{-i\hat{H}t/\hbar}\,\psi(0) = e^{-i\hat{H}t/\hbar}\,\hat{P}_{12}\,\psi(0) = e^{-i\hat{H}t/\hbar}\,\psi(0) = \psi(t). $$

The symmetry character (bosonic or fermionic) is preserved for all time. $\blacksquare$

对称性（玻色子或费米子特性）对所有时刻都保持不变。$\blacksquare$

---

## B. Symmetric and Antisymmetric Two-Particle States · 对称与反对称两粒子态

**Claim.** From any two single-particle states $|a\rangle$ and $|b\rangle$, one can construct properly symmetrized and antisymmetrized two-particle states.

**命题。** 从任意两个单粒子态 $|a\rangle$ 和 $|b\rangle$，可以构造恰当的对称化和反对称化两粒子态。

**Step 1 — The unsymmetrized product.** The naive product state $|a\rangle_1|b\rangle_2 = \psi_a(1)\psi_b(2)$ is generally neither symmetric nor antisymmetric under exchange (unless $a = b$):

**第 1 步 — 未对称化的乘积态。** 朴素乘积态 $|a\rangle_1|b\rangle_2 = \psi_a(1)\psi_b(2)$ 在交换下通常既不对称也不反对称（除非 $a = b$）：

$$ \hat{P}_{12}\,[\psi_a(1)\psi_b(2)] = \psi_a(2)\psi_b(1) \ne \pm\psi_a(1)\psi_b(2) \quad (\text{in general}). $$

**Step 2 — Symmetrization and antisymmetrization.** Project onto the eigenspaces of $\hat{P}_{12}$:

**第 2 步 — 对称化与反对称化。** 投影到 $\hat{P}_{12}$ 的本征子空间：

Symmetric (bosons, eigenvalue $+1$):

对称（玻色子，本征值 $+1$）：

$$ \psi_S(1,2) = (1/\sqrt{2})\,[\psi_a(1)\psi_b(2) + \psi_a(2)\psi_b(1)]. $$

Antisymmetric (fermions, eigenvalue $-1$):

反对称（费米子，本征值 $-1$）：

$$ \psi_A(1,2) = (1/\sqrt{2})\,[\psi_a(1)\psi_b(2) - \psi_a(2)\psi_b(1)]. $$

**Step 3 — Verify the symmetry.** For $\psi_S$:

**第 3 步 — 验证对称性。** 对 $\psi_S$：

$$ \hat{P}_{12}\,\psi_S(1,2) = (1/\sqrt{2})[\psi_a(2)\psi_b(1) + \psi_a(1)\psi_b(2)] = \psi_S(1,2). \;\checkmark $$

For $\psi_A$:

对 $\psi_A$：

$$ \hat{P}_{12}\,\psi_A(1,2) = (1/\sqrt{2})[\psi_a(2)\psi_b(1) - \psi_a(1)\psi_b(2)] = -\psi_A(1,2). \;\checkmark $$

**Step 4 — Normalization.** For $a \ne b$ and $\langle a|b\rangle = 0$ (orthonormal single-particle states):

**第 4 步 — 归一化。** 对 $a \ne b$ 且 $\langle a|b\rangle = 0$（正交归一单粒子态）：

$$ \int\!\!\int|\psi_S|^2\,d1\,d2 = \tfrac12\int\!\!\int[|\psi_a(1)|^2|\psi_b(2)|^2 + \psi_a^*(1)\psi_b(1)\psi_a(2)\psi_b^*(2) + \text{c.c.} + |\psi_a(2)|^2|\psi_b(1)|^2]\,d1\,d2. $$

The cross terms integrate to $\langle a|b\rangle\langle b|a\rangle = 0$ (by orthogonality). The remaining terms give:

交叉项积分为 $\langle a|b\rangle\langle b|a\rangle = 0$（由正交性）。剩余项给出：

$$ \tfrac12(1\cdot1 + 1\cdot1) = 1. \;\checkmark $$

Similarly $\|\psi_A\|^2 = 1$. $\blacksquare$

类似地 $\|\psi_A\|^2 = 1$。$\blacksquare$

---

## C. Pauli Exclusion: Antisymmetric State Vanishes When $a = b$ · 泡利不相容：当 $a = b$ 时反对称态为零

**Claim.** If the two single-particle states are the same ($a = b$), the antisymmetric state $\psi_A$ vanishes identically.

**命题。** 若两个单粒子态相同（$a = b$），则反对称态 $\psi_A$ 恒等于零。

**Proof.** Set $a = b$ in the expression for $\psi_A$:

**证明。** 在 $\psi_A$ 的表达式中令 $a = b$：

$$ \psi_A(1,2) = (1/\sqrt{2})[\psi_a(1)\psi_a(2) - \psi_a(2)\psi_a(1)] = (1/\sqrt{2})\cdot 0 = 0. \qquad \blacksquare $$

**Physical meaning.** A state in which both fermions are in the same single-particle state $a$ does not exist — the antisymmetric wave function that would describe it is identically zero. This is the **Pauli exclusion principle**: no two identical fermions can occupy the same quantum state.

**物理意义。** 两个费米子都处于同一单粒子态 $a$ 的态不存在——描述它的反对称波函数恒等于零。这就是**泡利不相容原理**：没有两个全同费米子可以占据同一量子态。$\blacksquare$

---

## D. Slater Determinant and Its Antisymmetry · 斯莱特行列式及其反对称性

**Claim.** For $N$ fermions, the antisymmetric $N$-particle wave function is the Slater determinant:

**命题。** 对 $N$ 个费米子，反对称的 $N$ 粒子波函数是斯莱特行列式：

$$ \Psi(1,2,\ldots,N) = (1/\sqrt{N!})\,\det[\psi_{a_i}(j)] $$

where the $(i,j)$ element of the $N\times N$ matrix is $\psi_{a_i}(j)$ (particle $j$ in state $a_i$). This is antisymmetric under exchange of any two particles.

其中 $N\times N$ 矩阵的 $(i,j)$ 元为 $\psi_{a_i}(j)$（粒子 $j$ 处于态 $a_i$）。在任意两粒子交换下此态是反对称的。

**Step 1 — Write the determinant explicitly.** The Slater determinant is:

**第 1 步 — 明确写出行列式。** 斯莱特行列式为：

$$ \Psi(1,\ldots,N) = \frac{1}{\sqrt{N!}}\begin{vmatrix} \psi_{a_1}(1) & \psi_{a_1}(2) & \cdots & \psi_{a_1}(N) \\ \psi_{a_2}(1) & \psi_{a_2}(2) & \cdots & \psi_{a_2}(N) \\ \vdots & \vdots & \ddots & \vdots \\ \psi_{a_N}(1) & \psi_{a_N}(2) & \cdots & \psi_{a_N}(N) \end{vmatrix} $$

By the Leibniz formula: $\det[\psi_{a_i}(j)] = \sum_{\sigma\in S_N} \mathrm{sgn}(\sigma) \prod_i \psi_{a_i}(\sigma(i))$, summing over all $N!$ permutations $\sigma$ of $\{1,\ldots,N\}$ with sign $\mathrm{sgn}(\sigma) = \pm1$.

由莱布尼茨公式：$\det[\psi_{a_i}(j)] = \sum_{\sigma\in S_N} \mathrm{sgn}(\sigma) \prod_i \psi_{a_i}(\sigma(i))$，对 $\{1,\ldots,N\}$ 的所有 $N!$ 个置换 $\sigma$ 求和，$\mathrm{sgn}(\sigma) = \pm1$。

**Step 2 — Antisymmetry under exchange of particles $k$ and $\ell$.** Exchanging particles $k$ and $\ell$ means the wave function evaluated at the swapped arguments $\Psi(1,\ldots,\ell,\ldots,k,\ldots,N)$. In the matrix, this swaps columns $k$ and $\ell$. A column transposition changes the sign of a determinant:

**第 2 步 — 粒子 $k$ 与 $\ell$ 交换下的反对称性。** 交换粒子 $k$ 与 $\ell$ 意味着波函数在交换参数处取值 $\Psi(1,\ldots,\ell,\ldots,k,\ldots,N)$。在矩阵中，这交换了第 $k$ 列和第 $\ell$ 列。列对换改变行列式的符号：

$$ \Psi(1,\ldots,\ell,\ldots,k,\ldots,N) = (1/\sqrt{N!})\det[\text{swap cols } k,\ell] = -(1/\sqrt{N!})\det[\text{original}] = -\Psi(1,\ldots,k,\ldots,\ell,\ldots,N). $$

Therefore **$\Psi$ is antisymmetric under any transposition of particle labels**. Since every permutation is a product of transpositions, $\Psi$ acquires the signature of the permutation:

因此 **$\Psi$ 在任意粒子标签对换下是反对称的**。由于每个置换是对换的乘积，$\Psi$ 得到置换的符号：

$$ \Psi(\sigma(1),\ldots,\sigma(N)) = \mathrm{sgn}(\sigma)\cdot\Psi(1,\ldots,N). \qquad \blacksquare $$

**Step 3 — Pauli exclusion from the determinant.** If any two states are the same, say $a_i = a_j$ for $i \ne j$, then two rows of the matrix are identical. A matrix with two identical rows has zero determinant:

**第 3 步 — 行列式给出泡利不相容原理。** 若任意两个态相同，设 $a_i = a_j$（$i \ne j$），则矩阵有两行相同。具有两行相同的矩阵行列式为零：

$$ \det[\ldots\text{identical rows}\ldots] = 0 \to \Psi = 0. \qquad \blacksquare $$

No two fermions can occupy the same single-particle state. This is the Pauli exclusion principle, now derived directly from the antisymmetry of the Slater determinant. $\blacksquare$

没有两个费米子可以占据同一单粒子态。这就是泡利不相容原理，现在直接从斯莱特行列式的反对称性推导而来。$\blacksquare$

**Step 4 — Normalization.** For an orthonormal set of single-particle states $\langle a_i|a_j\rangle = \delta_{ij}$:

**第 4 步 — 归一化。** 对正交归一的单粒子态集 $\langle a_i|a_j\rangle = \delta_{ij}$：

$$ \langle\Psi|\Psi\rangle = (1/N!)\sum_\sigma\sum_\tau \mathrm{sgn}(\sigma)\mathrm{sgn}(\tau)\prod_i \langle\psi_{a_i}(\sigma(i))|\psi_{a_i}(\tau(i))\rangle. $$

Orthonormality forces $\sigma(i) = \tau(i)$ for all $i$, i.e., $\sigma = \tau$. There are $N!$ such terms, each contributing $\mathrm{sgn}(\sigma)^2 = 1$:

正交归一性迫使对所有 $i$ 有 $\sigma(i) = \tau(i)$，即 $\sigma = \tau$。这样的项有 $N!$ 个，每个贡献 $\mathrm{sgn}(\sigma)^2 = 1$：

$$ \langle\Psi|\Psi\rangle = (1/N!)\cdot N!\cdot 1 = 1. \qquad \blacksquare $$

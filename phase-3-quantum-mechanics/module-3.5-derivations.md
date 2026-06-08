# Derivations — Module 3.5: Identical Particles
# 推导 — 模块 3.5：全同粒子

> Companion to [Module 3.5](./module-3.5-identical-particles.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.5](./module-3.5-identical-particles.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Exchange Operator Has Eigenvalues ±1 and Is Conserved · 交换算符的本征值为 ±1 且守恒

**Claim.** The exchange operator P̂₁₂ defined by P̂₁₂ ψ(1,2) = ψ(2,1) has eigenvalues ±1. Moreover, if [Ĥ, P̂₁₂] = 0 (which holds whenever particles 1 and 2 are identical), then P̂₁₂ is a conserved quantity: a state symmetric (antisymmetric) under exchange remains so for all time.

**命题。** 由 P̂₁₂ ψ(1,2) = ψ(2,1) 定义的交换算符 P̂₁₂ 的本征值为 ±1。此外，若 [Ĥ, P̂₁₂] = 0（当粒子 1 和 2 全同时总成立），则 P̂₁₂ 是守恒量：在交换下对称（反对称）的态将始终保持对称（反对称）。

**Step 1 — P̂₁₂ is its own inverse.** Applying the exchange operator twice returns to the original state:

**第 1 步 — P̂₁₂ 是自身的逆。** 两次应用交换算符回到原始态：

  P̂₁₂² ψ(1,2) = P̂₁₂ ψ(2,1) = ψ(1,2).

So **P̂₁₂² = 1̂** (the identity operator).

故 **P̂₁₂² = 1̂**（恒等算符）。

**Step 2 — P̂₁₂ is Hermitian.** For any two-particle states φ and ψ:

**第 2 步 — P̂₁₂ 是厄米的。** 对任意两粒子态 φ 和 ψ：

  ⟨φ|P̂₁₂|ψ⟩ = ∫∫ φ*(1,2) ψ(2,1) d1 d2.

Rename integration variables (1 ↔ 2) — this is just relabeling dummy variables:

重命名积分变量（1 ↔ 2）——这只是重新标记哑变量：

  = ∫∫ φ*(2,1) ψ(1,2) d1 d2 = ⟨P̂₁₂φ|ψ⟩.

So P̂₁₂† = P̂₁₂ — P̂₁₂ is Hermitian (in fact, unitary and Hermitian, hence P̂₁₂² = 1 is consistent). ∎

故 P̂₁₂† = P̂₁₂——P̂₁₂ 是厄米的（实际上是幺正且厄米的，因此 P̂₁₂² = 1 是自洽的）。∎

**Step 3 — Eigenvalues.** Let P̂₁₂|ψ⟩ = λ|ψ⟩. From P̂₁₂² = 1̂:

**第 3 步 — 本征值。** 设 P̂₁₂|ψ⟩ = λ|ψ⟩。由 P̂₁₂² = 1̂：

  P̂₁₂²|ψ⟩ = λ²|ψ⟩ = 1·|ψ⟩,

so **λ² = 1**, giving **λ = +1** (symmetric) or **λ = −1** (antisymmetric). ∎

故 **λ² = 1**，即 **λ = +1**（对称）或 **λ = −1**（反对称）。∎

**Step 4 — Conservation: [Ĥ, P̂₁₂] = 0 for identical particles.** The Hamiltonian of two identical particles has the form Ĥ = T̂₁ + T̂₂ + V̂(1,2), where V̂(1,2) = V̂(2,1) (the interaction is symmetric — swapping identical particles cannot change physics). Also T̂₁ + T̂₂ is symmetric. Therefore:

**第 4 步 — 守恒：全同粒子的 [Ĥ, P̂₁₂] = 0。** 两个全同粒子的哈密顿量形如 Ĥ = T̂₁ + T̂₂ + V̂(1,2)，其中 V̂(1,2) = V̂(2,1)（相互作用是对称的——交换全同粒子不改变物理）。T̂₁ + T̂₂ 也是对称的。因此：

  P̂₁₂ Ĥ ψ(1,2) = Ĥ(2,1) ψ(2,1),  and Ĥ P̂₁₂ ψ(1,2) = Ĥ(1,2) ψ(2,1).

Since Ĥ(1,2) = Ĥ(2,1) for identical particles, [Ĥ, P̂₁₂] = 0.

由于对全同粒子 Ĥ(1,2) = Ĥ(2,1)，故 [Ĥ, P̂₁₂] = 0。

**Step 5 — Conservation in time.** From the Schrödinger equation, the time evolution of ⟨P̂₁₂⟩ obeys:

**第 5 步 — 时间守恒。** 由薛定谔方程，⟨P̂₁₂⟩ 的时间演化满足：

  d⟨P̂₁₂⟩/dt = (i/ℏ)⟨[Ĥ, P̂₁₂]⟩ + ∂⟨P̂₁₂⟩/∂t = 0 + 0 = 0.

(P̂₁₂ has no explicit time dependence.) More concretely, if ψ(t=0) = P̂₁₂ ψ(t=0) (symmetric), then:

（P̂₁₂ 没有显式时间依赖。）更具体地，若 ψ(t=0) = P̂₁₂ ψ(t=0)（对称），则：

  P̂₁₂ ψ(t) = P̂₁₂ e^{−iĤt/ℏ} ψ(0) = e^{−iĤt/ℏ} P̂₁₂ ψ(0) = e^{−iĤt/ℏ} ψ(0) = ψ(t).

The symmetry character (bosonic or fermionic) is preserved for all time. ∎

对称性（玻色子或费米子特性）对所有时刻都保持不变。∎

---

## B. Symmetric and Antisymmetric Two-Particle States · 对称与反对称两粒子态

**Claim.** From any two single-particle states |a⟩ and |b⟩, one can construct properly symmetrized and antisymmetrized two-particle states.

**命题。** 从任意两个单粒子态 |a⟩ 和 |b⟩，可以构造恰当的对称化和反对称化两粒子态。

**Step 1 — The unsymmetrized product.** The naive product state |a⟩₁|b⟩₂ = ψₐ(1)ψ_b(2) is generally neither symmetric nor antisymmetric under exchange (unless a = b):

**第 1 步 — 未对称化的乘积态。** 朴素乘积态 |a⟩₁|b⟩₂ = ψₐ(1)ψ_b(2) 在交换下通常既不对称也不反对称（除非 a = b）：

  P̂₁₂ [ψₐ(1)ψ_b(2)] = ψₐ(2)ψ_b(1) ≠ ±ψₐ(1)ψ_b(2)  (in general).

**Step 2 — Symmetrization and antisymmetrization.** Project onto the eigenspaces of P̂₁₂:

**第 2 步 — 对称化与反对称化。** 投影到 P̂₁₂ 的本征子空间：

Symmetric (bosons, eigenvalue +1):

对称（玻色子，本征值 +1）：

  ψ_S(1,2) = (1/√2) [ψₐ(1)ψ_b(2) + ψₐ(2)ψ_b(1)].

Antisymmetric (fermions, eigenvalue −1):

反对称（费米子，本征值 −1）：

  ψ_A(1,2) = (1/√2) [ψₐ(1)ψ_b(2) − ψₐ(2)ψ_b(1)].

**Step 3 — Verify the symmetry.** For ψ_S:

**第 3 步 — 验证对称性。** 对 ψ_S：

  P̂₁₂ ψ_S(1,2) = (1/√2)[ψₐ(2)ψ_b(1) + ψₐ(1)ψ_b(2)] = ψ_S(1,2). ✓

For ψ_A:

对 ψ_A：

  P̂₁₂ ψ_A(1,2) = (1/√2)[ψₐ(2)ψ_b(1) − ψₐ(1)ψ_b(2)] = −ψ_A(1,2). ✓

**Step 4 — Normalization.** For a ≠ b and ⟨a|b⟩ = 0 (orthonormal single-particle states):

**第 4 步 — 归一化。** 对 a ≠ b 且 ⟨a|b⟩ = 0（正交归一单粒子态）：

  ∫∫|ψ_S|² d1 d2 = ½ ∫∫[|ψₐ(1)|²|ψ_b(2)|² + ψₐ*(1)ψ_b(1)ψₐ(2)ψ_b*(2) + c.c. + |ψₐ(2)|²|ψ_b(1)|²] d1 d2.

The cross terms integrate to ⟨a|b⟩⟨b|a⟩ = 0 (by orthogonality). The remaining terms give:

交叉项积分为 ⟨a|b⟩⟨b|a⟩ = 0（由正交性）。剩余项给出：

  ½(1·1 + 1·1) = 1. ✓

Similarly ‖ψ_A‖² = 1. ∎

类似地 ‖ψ_A‖² = 1。∎

---

## C. Pauli Exclusion: Antisymmetric State Vanishes When a = b · 泡利不相容：当 a = b 时反对称态为零

**Claim.** If the two single-particle states are the same (a = b), the antisymmetric state ψ_A vanishes identically.

**命题。** 若两个单粒子态相同（a = b），则反对称态 ψ_A 恒等于零。

**Proof.** Set a = b in the expression for ψ_A:

**证明。** 在 ψ_A 的表达式中令 a = b：

  ψ_A(1,2) = (1/√2)[ψₐ(1)ψₐ(2) − ψₐ(2)ψₐ(1)] = (1/√2) · 0 = **0**. ∎

**Physical meaning.** A state in which both fermions are in the same single-particle state a does not exist — the antisymmetric wave function that would describe it is identically zero. This is the **Pauli exclusion principle**: no two identical fermions can occupy the same quantum state.

**物理意义。** 两个费米子都处于同一单粒子态 a 的态不存在——描述它的反对称波函数恒等于零。这就是**泡利不相容原理**：没有两个全同费米子可以占据同一量子态。∎

---

## D. Slater Determinant and Its Antisymmetry · 斯莱特行列式及其反对称性

**Claim.** For N fermions, the antisymmetric N-particle wave function is the Slater determinant:

**命题。** 对 N 个费米子，反对称的 N 粒子波函数是斯莱特行列式：

  Ψ(1,2,…,N) = (1/√(N!)) det[ψₐᵢ(j)]

where the (i,j) element of the N×N matrix is ψₐᵢ(j) (particle j in state aᵢ). This is antisymmetric under exchange of any two particles.

其中 N×N 矩阵的 (i,j) 元为 ψₐᵢ(j)（粒子 j 处于态 aᵢ）。在任意两粒子交换下此态是反对称的。

**Step 1 — Write the determinant explicitly.** The Slater determinant is:

**第 1 步 — 明确写出行列式。** 斯莱特行列式为：

  Ψ(1,…,N) = (1/√(N!)) |ψₐ₁(1)  ψₐ₁(2)  …  ψₐ₁(N)|
                          |ψₐ₂(1)  ψₐ₂(2)  …  ψₐ₂(N)|
                          |  ⋮         ⋮       ⋱    ⋮    |
                          |ψₐN(1)  ψₐN(2)  …  ψₐN(N)|

By the Leibniz formula: det[ψₐᵢ(j)] = Σ_{σ∈Sₙ} sgn(σ) ∏ᵢ ψₐᵢ(σ(i)), summing over all N! permutations σ of {1,…,N} with sign sgn(σ) = ±1.

由莱布尼茨公式：det[ψₐᵢ(j)] = Σ_{σ∈Sₙ} sgn(σ) ∏ᵢ ψₐᵢ(σ(i))，对 {1,…,N} 的所有 N! 个置换 σ 求和，sgn(σ) = ±1。

**Step 2 — Antisymmetry under exchange of particles k and ℓ.** Exchanging particles k and ℓ means the wave function evaluated at the swapped arguments Ψ(1,…,ℓ,…,k,…,N). In the matrix, this swaps columns k and ℓ. A column transposition changes the sign of a determinant:

**第 2 步 — 粒子 k 与 ℓ 交换下的反对称性。** 交换粒子 k 与 ℓ 意味着波函数在交换参数处取值 Ψ(1,…,ℓ,…,k,…,N)。在矩阵中，这交换了第 k 列和第 ℓ 列。列对换改变行列式的符号：

  Ψ(1,…,ℓ,…,k,…,N) = (1/√(N!)) det[swap cols k,ℓ] = −(1/√(N!)) det[original] = −Ψ(1,…,k,…,ℓ,…,N).

Therefore **Ψ is antisymmetric under any transposition of particle labels**. Since every permutation is a product of transpositions, Ψ acquires the signature of the permutation:

因此 **Ψ 在任意粒子标签对换下是反对称的**。由于每个置换是对换的乘积，Ψ 得到置换的符号：

  Ψ(σ(1),…,σ(N)) = sgn(σ) · Ψ(1,…,N). ∎

**Step 3 — Pauli exclusion from the determinant.** If any two states are the same, say aᵢ = aⱼ for i ≠ j, then two rows of the matrix are identical. A matrix with two identical rows has zero determinant:

**第 3 步 — 行列式给出泡利不相容原理。** 若任意两个态相同，设 aᵢ = aⱼ（i ≠ j），则矩阵有两行相同。具有两行相同的矩阵行列式为零：

  det[…identical rows…] = 0 → **Ψ = 0**. ∎

No two fermions can occupy the same single-particle state. This is the Pauli exclusion principle, now derived directly from the antisymmetry of the Slater determinant. ∎

没有两个费米子可以占据同一单粒子态。这就是泡利不相容原理，现在直接从斯莱特行列式的反对称性推导而来。∎

**Step 4 — Normalization.** For an orthonormal set of single-particle states ⟨aᵢ|aⱼ⟩ = δᵢⱼ:

**第 4 步 — 归一化。** 对正交归一的单粒子态集 ⟨aᵢ|aⱼ⟩ = δᵢⱼ：

  ⟨Ψ|Ψ⟩ = (1/N!) ΣΣ_{σ,τ} sgn(σ)sgn(τ) ∏ᵢ ⟨ψₐᵢ(σ(i))|ψₐᵢ(τ(i))⟩.

Orthonormality forces σ(i) = τ(i) for all i, i.e., σ = τ. There are N! such terms, each contributing sgn(σ)² = 1:

正交归一性迫使对所有 i 有 σ(i) = τ(i)，即 σ = τ。这样的项有 N! 个，每个贡献 sgn(σ)² = 1：

  ⟨Ψ|Ψ⟩ = (1/N!) · N! · 1 = **1**. ∎

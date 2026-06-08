# Derivations — Module 3.3: Formalism
# 推导 — 模块 3.3：形式化框架

> Companion to [Module 3.3](./module-3.3-formalism.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.3](./module-3.3-formalism.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Canonical Commutator: [x̂, p̂] = iℏ · 正则对易子：[x̂, p̂] = iℏ

**Claim.** The operators x̂ (multiply by x) and p̂ = −iℏ ∂/∂x satisfy [x̂, p̂] = iℏ.

**命题。** 算符 x̂（乘以 x）与 p̂ = −iℏ ∂/∂x 满足 [x̂, p̂] = iℏ。

**Step 1 — Definition of the commutator.** [x̂, p̂] is the operator defined by its action on an arbitrary test function f(x):

**第 1 步 — 对易子的定义。** [x̂, p̂] 是通过其对任意测试函数 f(x) 的作用来定义的算符：

  [x̂, p̂] f(x) = x̂(p̂ f) − p̂(x̂ f).

**Step 2 — Compute each term.**

**第 2 步 — 计算每一项。**

  p̂ f = −iℏ ∂f/∂x = −iℏ f′,

  x̂(p̂ f) = x · (−iℏ f′) = −iℏ x f′.

  x̂ f = x f,

  p̂(x̂ f) = −iℏ ∂(xf)/∂x = −iℏ (f + x f′) = −iℏ f − iℏ x f′.

**Step 3 — Subtract.**

**第 3 步 — 相减。**

  [x̂, p̂] f = (−iℏ x f′) − (−iℏ f − iℏ x f′)
             = −iℏ x f′ + iℏ f + iℏ x f′
             = iℏ f.

Since this holds for all f, [x̂, p̂] = iℏ as an operator identity. ∎

由于对所有 f 成立，作为算符恒等式 [x̂, p̂] = iℏ。∎

---

## B. Hermitian Operators: Real Eigenvalues and Orthogonal Eigenstates · 厄米算符：实本征值与正交本征态

**Claim.** If  is Hermitian (⟨φ|Âψ⟩ = ⟨Âφ|ψ⟩ for all φ, ψ in the domain), then (i) all eigenvalues of  are real, and (ii) eigenstates corresponding to distinct eigenvalues are orthogonal.

**命题。** 若 Â 是厄米的（对定义域内所有 φ、ψ 有 ⟨φ|Âψ⟩ = ⟨Âφ|ψ⟩），则 (i) Â 的所有本征值为实数，(ii) 对应不同本征值的本征态互相正交。

**Step 1 — Reality of eigenvalues.** Let Â|a⟩ = a|a⟩ with |a⟩ ≠ 0. Compute ⟨a|Â|a⟩ two ways. First:

**第 1 步 — 本征值的实性。** 设 Â|a⟩ = a|a⟩，|a⟩ ≠ 0。用两种方法计算 ⟨a|Â|a⟩。首先：

  ⟨a|Â|a⟩ = ⟨a|(a|a⟩) = a⟨a|a⟩.

Second, using Hermiticity ⟨a|Â = ⟨Â†a| = ⟨Âa| = a*⟨a|:

其次，利用厄米性 ⟨a|Â = ⟨Â†a| = ⟨Âa| = a*⟨a|：

  ⟨a|Â|a⟩ = (⟨a|Â†)|a⟩ = a*⟨a|a⟩.

Equating: a⟨a|a⟩ = a*⟨a|a⟩. Since |a⟩ ≠ 0, we have ⟨a|a⟩ > 0, so:

令二者相等：a⟨a|a⟩ = a*⟨a|a⟩。因 |a⟩ ≠ 0，⟨a|a⟩ > 0，故：

  **a = a***, i.e., a is real. ∎

**Step 2 — Orthogonality of eigenstates.** Let Â|a⟩ = a|a⟩ and Â|b⟩ = b|b⟩ with a ≠ b (both real by Step 1). Consider the inner product ⟨a|Â|b⟩:

**第 2 步 — 本征态的正交性。** 设 Â|a⟩ = a|a⟩ 且 Â|b⟩ = b|b⟩，a ≠ b（由第 1 步均为实数）。考虑内积 ⟨a|Â|b⟩：

From the right: ⟨a|Â|b⟩ = ⟨a|(b|b⟩) = b⟨a|b⟩.

从右边：⟨a|Â|b⟩ = ⟨a|(b|b⟩) = b⟨a|b⟩。

From the left (using Hermiticity): ⟨a|Â|b⟩ = ⟨Âa|b⟩ = ⟨a|a⟩* ⟨a|b⟩ = a*⟨a|b⟩ = a⟨a|b⟩.

从左边（利用厄米性）：⟨a|Â|b⟩ = ⟨Âa|b⟩ = a*⟨a|b⟩ = a⟨a|b⟩（因 a 为实数）。

Equating: b⟨a|b⟩ = a⟨a|b⟩, so (a − b)⟨a|b⟩ = 0. Since a ≠ b:

令二者相等：b⟨a|b⟩ = a⟨a|b⟩，故 (a − b)⟨a|b⟩ = 0。因 a ≠ b：

  **⟨a|b⟩ = 0** — the eigenstates are orthogonal. ∎

  **⟨a|b⟩ = 0** ——本征态互相正交。∎

---

## C. Spectral Expansion: |ψ⟩ = Σcₙ|n⟩ with cₙ = ⟨n|ψ⟩ · 谱展开：|ψ⟩ = Σcₙ|n⟩ 与 cₙ = ⟨n|ψ⟩

**Claim.** If {|n⟩} is a complete orthonormal basis of the Hilbert space (∑ₙ|n⟩⟨n| = 1̂, ⟨m|n⟩ = δ_{mn}), then any state |ψ⟩ can be expanded as |ψ⟩ = Σₙ cₙ|n⟩ with cₙ = ⟨n|ψ⟩, and Σₙ|cₙ|² = 1 (normalization).

**命题。** 若 {|n⟩} 是希尔伯特空间的完备正交归一基（∑ₙ|n⟩⟨n| = 1̂，⟨m|n⟩ = δ_{mn}），则任意态 |ψ⟩ 可展开为 |ψ⟩ = Σₙ cₙ|n⟩，其中 cₙ = ⟨n|ψ⟩，且 Σₙ|cₙ|² = 1（归一化）。

**Step 1 — Insert the resolution of the identity.** The completeness relation Σₙ|n⟩⟨n| = 1̂ means that for any |ψ⟩:

**第 1 步 — 插入单位分解。** 完备性关系 Σₙ|n⟩⟨n| = 1̂ 意味着对任意 |ψ⟩：

  |ψ⟩ = 1̂|ψ⟩ = (Σₙ|n⟩⟨n|)|ψ⟩ = Σₙ|n⟩⟨n|ψ⟩ = Σₙ cₙ|n⟩,

where **cₙ = ⟨n|ψ⟩**.

其中 **cₙ = ⟨n|ψ⟩**。

**Step 2 — Normalization.** Take ⟨ψ|ψ⟩ = 1:

**第 2 步 — 归一化。** 取 ⟨ψ|ψ⟩ = 1：

  1 = ⟨ψ|ψ⟩ = ⟨ψ|(Σₙ cₙ|n⟩) = Σₙ cₙ ⟨ψ|n⟩ = Σₙ cₙ c*ₙ = **Σₙ|cₙ|²**. ∎

**Step 3 — Probability interpretation.** When the observable  with eigenvalues aₙ and eigenstates |n⟩ is measured, the probability of obtaining aₙ is:

**第 3 步 — 概率诠释。** 当测量本征值为 aₙ、本征态为 |n⟩ 的可观测量 Â 时，得到 aₙ 的概率为：

  P(aₙ) = |⟨n|ψ⟩|² = |cₙ|².

Completeness ensures Σₙ P(aₙ) = 1 — some outcome always occurs. ∎

完备性确保 Σₙ P(aₙ) = 1——某个结果必然发生。∎

---

## D. Generalized Uncertainty Principle: ΔAΔB ≥ ½|⟨[Â,B̂]⟩| · 广义不确定性关系

**Claim.** For any two Hermitian observables Â and B̂ in state |ψ⟩:

**命题。** 对任意态 |ψ⟩ 中的两个厄米可观测量 Â 和 B̂：

  **ΔAΔB ≥ ½|⟨[Â, B̂]⟩|**.

**Step 1 — Define shifted operators.** Let α = ⟨Â⟩ and β = ⟨B̂⟩. Define:

**第 1 步 — 定义移位算符。** 令 α = ⟨Â⟩，β = ⟨B̂⟩。定义：

  Ã = Â − α,   B̃ = B̂ − β.

Both Ã and B̃ are Hermitian (subtracting a real number from a Hermitian operator preserves Hermiticity). Also:

Ã 和 B̃ 均为厄米的（从厄米算符减去实数保持厄米性）。还有：

  ΔA² = ⟨Ã²⟩ = ⟨ψ|Ã²|ψ⟩ = ‖Ã|ψ⟩‖²,   ΔB² = ⟨B̃²⟩ = ‖B̃|ψ⟩‖².

Note also [Ã, B̃] = [Â, B̂] (constants commute with everything).

注意 [Ã, B̃] = [Â, B̂]（常数与所有算符对易）。

**Step 2 — Apply the Cauchy–Schwarz inequality.** For any two vectors |f⟩ and |g⟩ in a Hilbert space, the Cauchy–Schwarz inequality states:

**第 2 步 — 应用柯西–施瓦茨不等式。** 对希尔伯特空间中任意两个向量 |f⟩ 和 |g⟩，柯西–施瓦茨不等式表明：

  ⟨f|f⟩ · ⟨g|g⟩ ≥ |⟨f|g⟩|².

Set |f⟩ = Ã|ψ⟩ and |g⟩ = B̃|ψ⟩. Then:

取 |f⟩ = Ã|ψ⟩，|g⟩ = B̃|ψ⟩。则：

  ‖Ã|ψ⟩‖² · ‖B̃|ψ⟩‖² ≥ |⟨Ã ψ|B̃ ψ⟩|²,

  ΔA² · ΔB² ≥ |⟨ψ|Ã B̃|ψ⟩|².    … (*)

**Step 3 — Decompose Ã B̃ into Hermitian and anti-Hermitian parts.** Write:

**第 3 步 — 将 Ã B̃ 分解为厄米与反厄米部分。** 写成：

  ÃB̃ = ½(ÃB̃ + B̃Ã) + ½(ÃB̃ − B̃Ã).

The first part is the **anticommutator** {Ã, B̃}/2 — a Hermitian operator (its expectation is real). The second part involves the **commutator** [Ã, B̃]/2 = [Â, B̂]/2. Since Ã and B̃ are Hermitian, [Ã, B̃] is anti-Hermitian (satisfies ([Ã,B̃])† = [B̃†,Ã†] = [B̃,Ã] = −[Ã,B̃]), so its expectation value is purely imaginary (or zero).

第一部分是**反对易子** {Ã, B̃}/2——厄米算符（其期望值为实数）。第二部分涉及**对易子** [Ã, B̃]/2 = [Â, B̂]/2。由于 Ã 和 B̃ 是厄米的，[Ã, B̃] 是反厄米的（满足 ([Ã,B̃])† = [B̃†,Ã†] = [B̃,Ã] = −[Ã,B̃]），故其期望值为纯虚数（或零）。

Therefore ⟨ÃB̃⟩ = (real part) + i(imaginary part), and:

因此 ⟨ÃB̃⟩ = (实部) + i(虚部)，且：

  |⟨ÃB̃⟩|² = |Re⟨ÃB̃⟩|² + |Im⟨ÃB̃⟩|² ≥ |Im⟨ÃB̃⟩|².

Now Im⟨ÃB̃⟩ = Im[½⟨{Ã,B̃}⟩ + ½⟨[Â,B̂]⟩]. The anticommutator term is real, so it contributes nothing to the imaginary part:

现在 Im⟨ÃB̃⟩ = Im[½⟨{Ã,B̃}⟩ + ½⟨[Â,B̂]⟩]。反对易子项为实数，对虚部无贡献：

  Im⟨ÃB̃⟩ = ½ Im⟨[Â,B̂]⟩.

But [Â,B̂] is anti-Hermitian, so ⟨[Â,B̂]⟩ is purely imaginary: ⟨[Â,B̂]⟩ = i·K for some real K. Therefore Im⟨ÃB̃⟩ = K/2, and:

但 [Â,B̂] 是反厄米的，故 ⟨[Â,B̂]⟩ 为纯虚数：⟨[Â,B̂]⟩ = i·K，K 为实数。因此 Im⟨ÃB̃⟩ = K/2，且：

  |⟨ÃB̃⟩|² ≥ (K/2)² = ¼|⟨[Â,B̂]⟩|².

**Step 4 — Assemble the inequality.** Substituting back into (*):

**第 4 步 — 组合不等式。** 代回 (*)：

  ΔA² · ΔB² ≥ ¼|⟨[Â,B̂]⟩|².

Taking the positive square root (ΔA, ΔB ≥ 0):

取正平方根（ΔA、ΔB ≥ 0）：

  **ΔA · ΔB ≥ ½|⟨[Â,B̂]⟩|**. ∎

---

## E. Position–Momentum Uncertainty: Δx·Δp ≥ ℏ/2 · 位置–动量不确定性

**Claim.** For x̂ and p̂, the generalized uncertainty relation gives Δx·Δp ≥ ℏ/2.

**命题。** 对 x̂ 和 p̂，广义不确定性关系给出 Δx·Δp ≥ ℏ/2。

**Step 1.** From Section A, [x̂, p̂] = iℏ.

**第 1 步。** 由第 A 节，[x̂, p̂] = iℏ。

**Step 2.** ⟨[x̂, p̂]⟩ = ⟨iℏ⟩ = iℏ (since iℏ is a scalar, its expectation value in any state is iℏ).

**第 2 步。** ⟨[x̂, p̂]⟩ = ⟨iℏ⟩ = iℏ（因为 iℏ 是标量，在任何态中其期望值均为 iℏ）。

**Step 3.** Apply the generalized uncertainty relation:

**第 3 步。** 应用广义不确定性关系：

  Δx · Δp ≥ ½|⟨[x̂, p̂]⟩| = ½|iℏ| = **ℏ/2**. ∎

The equality Δx·Δp = ℏ/2 is saturated when the Cauchy–Schwarz inequality is an equality (|f⟩ ∝ |g⟩) and the real part of ⟨f|g⟩ vanishes. These conditions together force ψ to be a Gaussian, confirming the result of Module 3.1 Derivation D.

当柯西–施瓦茨不等式取等（|f⟩ ∝ |g⟩）且 ⟨f|g⟩ 的实部为零时，等号 Δx·Δp = ℏ/2 成立。这两个条件共同迫使 ψ 为高斯函数，与模块 3.1 推导 D 的结果一致。∎

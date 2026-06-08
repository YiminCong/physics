# Derivations — Module 6.1: Second Quantization & the Many-Body Problem
# 推导 — 模块 6.1：二次量子化与多体问题

> Companion to [Module 6.1](./module-6.1-second-quantization.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.1](./module-6.1-second-quantization.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Field Operators and Their Anticommutation Relation · 场算符及其反对易关系

**Claim.** Define the fermionic field operator ψ̂(x) = Σ_k φ_k(x) ĉ_k, where {φ_k} is any complete orthonormal set of single-particle orbitals and {ĉ_k, ĉ†_{k'}} = δ_{kk'}, {ĉ_k, ĉ_{k'}} = 0. Then

  {ψ̂(x), ψ̂†(x')} = δ(x − x').

**命题。** 定义费米子场算符 ψ̂(x) = Σ_k φ_k(x) ĉ_k，其中 {φ_k} 是任意完备正交归一单粒子轨道组，{ĉ_k, ĉ†_{k'}} = δ_{kk'}，{ĉ_k, ĉ_{k'}} = 0。则

  {ψ̂(x), ψ̂†(x')} = δ(x − x')。

**Step 1 — Write out both operators explicitly.**

  ψ̂(x) = Σ_k φ_k(x) ĉ_k,     ψ̂†(x') = Σ_{k'} φ*_{k'}(x') ĉ†_{k'}.

**第 1 步 — 显式写出两个算符。**

  ψ̂(x) = Σ_k φ_k(x) ĉ_k，     ψ̂†(x') = Σ_{k'} φ*_{k'}(x') ĉ†_{k'}。

**Step 2 — Expand the anticommutator.** Since φ_k(x) and φ*_{k'}(x') are c-numbers (ordinary complex numbers), they pass through anticommutators freely:

  {ψ̂(x), ψ̂†(x')} = Σ_k Σ_{k'} φ_k(x) φ*_{k'}(x') {ĉ_k, ĉ†_{k'}}.

**第 2 步 — 展开反对易子。** 由于 φ_k(x) 和 φ*_{k'}(x') 是 c 数（普通复数），它们可以自由穿过反对易子：

  {ψ̂(x), ψ̂†(x')} = Σ_k Σ_{k'} φ_k(x) φ*_{k'}(x') {ĉ_k, ĉ†_{k'}}。

**Step 3 — Use the mode anticommutator.** The fundamental fermionic anticommutator gives {ĉ_k, ĉ†_{k'}} = δ_{kk'}, so the double sum collapses to a single sum:

  {ψ̂(x), ψ̂†(x')} = Σ_k φ_k(x) φ*_k(x') · δ_{kk'} → Σ_k φ_k(x) φ*_k(x').

**第 3 步 — 使用模式反对易子。** 基本费米子反对易子给出 {ĉ_k, ĉ†_{k'}} = δ_{kk'}，因此双重求和化为单重求和：

  {ψ̂(x), ψ̂†(x')} = Σ_k φ_k(x) φ*_k(x') · δ_{kk'} → Σ_k φ_k(x) φ*_k(x')。

**Step 4 — Invoke the completeness relation.** Because {φ_k} is a complete orthonormal set on the single-particle Hilbert space, the completeness (resolution of the identity) relation reads

  Σ_k φ_k(x) φ*_k(x') = δ(x − x').

This is the continuum analogue of the matrix identity Σ_k |k⟩⟨k| = 1. Inserting it gives

  {ψ̂(x), ψ̂†(x')} = δ(x − x').    ∎

**第 4 步 — 引用完备性关系。** 由于 {φ_k} 是单粒子希尔伯特空间上的完备正交归一集，其完备性（单位算符的分解）关系为

  Σ_k φ_k(x) φ*_k(x') = δ(x − x')。

这是矩阵恒等式 Σ_k |k⟩⟨k| = 1 的连续类比。代入得

  {ψ̂(x), ψ̂†(x')} = δ(x − x')。    ∎

**Step 5 — The other anticommutator vanishes.** Similarly,

  {ψ̂(x), ψ̂(x')} = Σ_k Σ_{k'} φ_k(x) φ_{k'}(x') {ĉ_k, ĉ_{k'}} = 0,

since {ĉ_k, ĉ_{k'}} = 0 by the fermionic mode algebra. So particle annihilation operators anticommute — the algebraic form of the Pauli exclusion principle.

**第 5 步 — 另一个反对易子为零。** 类似地，

  {ψ̂(x), ψ̂(x')} = Σ_k Σ_{k'} φ_k(x) φ_{k'}(x') {ĉ_k, ĉ_{k'}} = 0，

因为费米子模式代数给出 {ĉ_k, ĉ_{k'}} = 0。故粒子湮灭算符反对易——这是泡利不相容原理的代数形式。

---

## B. One-Body Operators in Second-Quantized Form · 单体算符的二次量子化形式

**Claim.** Let ô be a single-particle operator (acting on one particle at a time). Then the corresponding many-body operator is

  Ô = ∫ ψ̂†(x) ô ψ̂(x) dx,

where ô acts on x. In the mode basis this equals Σ_{kk'} ⟨k|ô|k'⟩ ĉ†_k ĉ_{k'}.

**命题。** 设 ô 是单粒子算符（每次作用于一个粒子）。则对应的多体算符为

  Ô = ∫ ψ̂†(x) ô ψ̂(x) dx，

其中 ô 作用于 x。在模式基底中，这等于 Σ_{kk'} ⟨k|ô|k'⟩ ĉ†_k ĉ_{k'}。

**Step 1 — Insert the mode expansion of ψ̂ and ψ̂†.**

  Ô = ∫ (Σ_{k'} φ*_{k'}(x) ĉ†_{k'}) ô (Σ_k φ_k(x) ĉ_k) dx.

Since ĉ†_{k'} and ĉ_k are mode operators (independent of x), they factor out of the spatial integral:

  Ô = Σ_{k'} Σ_k ĉ†_{k'} (∫ φ*_{k'}(x) ô φ_k(x) dx) ĉ_k.

**第 1 步 — 代入 ψ̂ 和 ψ̂† 的模式展开。**

  Ô = ∫ (Σ_{k'} φ*_{k'}(x) ĉ†_{k'}) ô (Σ_k φ_k(x) ĉ_k) dx。

由于 ĉ†_{k'} 和 ĉ_k 是模式算符（与 x 无关），它们可从空间积分中提取：

  Ô = Σ_{k'} Σ_k ĉ†_{k'} (∫ φ*_{k'}(x) ô φ_k(x) dx) ĉ_k。

**Step 2 — Identify the matrix element.** The integral ∫ φ*_{k'}(x) ô φ_k(x) dx is precisely the matrix element ⟨k'|ô|k⟩ of the single-particle operator in the orbital basis. Therefore

  Ô = Σ_{kk'} ⟨k'|ô|k⟩ ĉ†_{k'} ĉ_k.

Relabeling k ↔ k' gives the standard form Σ_{kk'} ⟨k|ô|k'⟩ ĉ†_k ĉ_{k'}. ∎

**第 2 步 — 识别矩阵元。** 积分 ∫ φ*_{k'}(x) ô φ_k(x) dx 恰好是单粒子算符在轨道基底中的矩阵元 ⟨k'|ô|k⟩。因此

  Ô = Σ_{kk'} ⟨k'|ô|k⟩ ĉ†_{k'} ĉ_k。

将 k ↔ k' 重新标记得标准形式 Σ_{kk'} ⟨k|ô|k'⟩ ĉ†_k ĉ_{k'}。∎

**Step 3 — Diagonal case: the kinetic energy.** For a diagonal operator ô = −ℏ²∇²/2m in the momentum eigenstate basis φ_k(x) = e^{ik·x}/√V, the matrix element is ⟨k|ô|k'⟩ = (ℏ²k²/2m) δ_{kk'}, so

  T̂ = Σ_k (ℏ²k²/2m) ĉ†_k ĉ_k = Σ_k ε_k n̂_k,

where ε_k = ℏ²k²/2m is the single-particle dispersion and n̂_k = ĉ†_k ĉ_k is the occupation number operator.

**第 3 步 — 对角情形：动能。** 对于在动量本征态基底 φ_k(x) = e^{ik·x}/√V 中的对角算符 ô = −ℏ²∇²/2m，矩阵元为 ⟨k|ô|k'⟩ = (ℏ²k²/2m) δ_{kk'}，因此

  T̂ = Σ_k (ℏ²k²/2m) ĉ†_k ĉ_k = Σ_k ε_k n̂_k，

其中 ε_k = ℏ²k²/2m 是单粒子色散关系，n̂_k = ĉ†_k ĉ_k 是占据数算符。

---

## C. Two-Body Operators in Second-Quantized Form · 两体算符的二次量子化形式

**Claim.** A two-body interaction V̂ = ½ Σ_{i≠j} U(x_i − x_j) is represented in Fock space as

  V̂ = ½ ∫∫ ψ̂†(x) ψ̂†(x') U(x − x') ψ̂(x') ψ̂(x) dx dx'.

In the mode basis: V̂ = ½ Σ_{kk'qq'} ⟨k,k'|U|q,q'⟩ ĉ†_k ĉ†_{k'} ĉ_{q'} ĉ_q.

**命题。** 两体相互作用 V̂ = ½ Σ_{i≠j} U(x_i − x_j) 在 Fock 空间中表示为

  V̂ = ½ ∫∫ ψ̂†(x) ψ̂†(x') U(x − x') ψ̂(x') ψ̂(x) dx dx'。

在模式基底中：V̂ = ½ Σ_{kk'qq'} ⟨k,k'|U|q,q'⟩ ĉ†_k ĉ†_{k'} ĉ_{q'} ĉ_q。

**Step 1 — Insert mode expansions.** Substitute ψ̂†(x) = Σ_k φ*_k(x) ĉ†_k and ψ̂(x) = Σ_q φ_q(x) ĉ_q (and similarly for the x' variables). The spatial integrals produce the two-body matrix element

  ⟨k,k'|U|q,q'⟩ = ∫∫ φ*_k(x) φ*_{k'}(x') U(x−x') φ_{q'}(x') φ_q(x) dx dx'.

**第 1 步 — 代入模式展开。** 代入 ψ̂†(x) = Σ_k φ*_k(x) ĉ†_k 和 ψ̂(x) = Σ_q φ_q(x) ĉ_q（以及 x' 变量的类似展开）。空间积分产生两体矩阵元

  ⟨k,k'|U|q,q'⟩ = ∫∫ φ*_k(x) φ*_{k'}(x') U(x−x') φ_{q'}(x') φ_q(x) dx dx'。

**Step 2 — Operator ordering enforces antisymmetry.** The ordering ψ̂†(x) ψ̂†(x') ψ̂(x') ψ̂(x) (note the reversed order of destruction operators compared to creation) is precisely the normal-ordered, antisymmetrized two-body operator. For fermions, swapping any two ψ̂ picks up a minus sign; this antisymmetry is automatically encoded in the anticommutation relations without manual Slater-determinant bookkeeping.

**第 2 步 — 算符排序强制反对称性。** 排序 ψ̂†(x) ψ̂†(x') ψ̂(x') ψ̂(x)（注意湮灭算符的顺序与产生算符相反）恰好是正规序的、反对称化的两体算符。对于费米子，交换任意两个 ψ̂ 产生一个负号；这种反对称性通过反对易关系自动编码，无需手工处理 Slater 行列式。

**Step 3 — Momentum conservation for a uniform system.** If U depends only on x − x', then in momentum space U(x−x') = Σ_q U_q e^{iq·(x−x')}. Performing the spatial integrals selects k = q + p, k' = q' − p (momentum-transfer q conserved), giving

  V̂ = ½ Σ_{k,k',q} U_q ĉ†_{k+q} ĉ†_{k'−q} ĉ_{k'} ĉ_k,

the familiar Coulomb interaction vertex used in Feynman diagrams. ∎

**第 3 步 — 均匀系统中的动量守恒。** 若 U 仅依赖于 x − x'，则在动量空间 U(x−x') = Σ_q U_q e^{iq·(x−x')}。执行空间积分后选出 k = q + p，k' = q' − p（动量转移 q 守恒），得

  V̂ = ½ Σ_{k,k',q} U_q ĉ†_{k+q} ĉ†_{k'−q} ĉ_{k'} ĉ_k，

这是费曼图中熟悉的库仑相互作用顶点。∎

---

## D. The Fock-Space Number Operator and Occupation Numbers · Fock 空间数算符与占据数

**Claim.** For fermions, n̂_k = ĉ†_k ĉ_k satisfies n̂²_k = n̂_k, so its eigenvalues are 0 or 1 (Pauli exclusion). For bosons, n̂_k = â†_k â_k has eigenvalues 0, 1, 2, … (unrestricted).

**命题。** 对于费米子，n̂_k = ĉ†_k ĉ_k 满足 n̂²_k = n̂_k，故其本征值为 0 或 1（泡利不相容）。对于玻色子，n̂_k = â†_k â_k 的本征值为 0, 1, 2, …（无限制）。

**Step 1 — Fermionic idempotency.** Compute n̂²_k = ĉ†_k ĉ_k ĉ†_k ĉ_k. Use the anticommutator {ĉ_k, ĉ†_k} = 1, i.e. ĉ_k ĉ†_k = 1 − ĉ†_k ĉ_k:

  n̂²_k = ĉ†_k (ĉ_k ĉ†_k) ĉ_k = ĉ†_k (1 − ĉ†_k ĉ_k) ĉ_k = ĉ†_k ĉ_k − ĉ†_k ĉ†_k ĉ_k ĉ_k.

Now {ĉ_k, ĉ_k} = 0 ⟹ 2ĉ_k ĉ_k = 0 ⟹ ĉ_k ĉ_k = 0 (and similarly ĉ†_k ĉ†_k = 0). Therefore

  n̂²_k = ĉ†_k ĉ_k = n̂_k.

An operator satisfying P² = P is a projector, and its only eigenvalues are 0 and 1. ∎

**第 1 步 — 费米子幂等性。** 计算 n̂²_k = ĉ†_k ĉ_k ĉ†_k ĉ_k。利用反对易子 {ĉ_k, ĉ†_k} = 1，即 ĉ_k ĉ†_k = 1 − ĉ†_k ĉ_k：

  n̂²_k = ĉ†_k (ĉ_k ĉ†_k) ĉ_k = ĉ†_k (1 − ĉ†_k ĉ_k) ĉ_k = ĉ†_k ĉ_k − ĉ†_k ĉ†_k ĉ_k ĉ_k。

现在 {ĉ_k, ĉ_k} = 0 ⟹ 2ĉ_k ĉ_k = 0 ⟹ ĉ_k ĉ_k = 0（类似地 ĉ†_k ĉ†_k = 0）。因此

  n̂²_k = ĉ†_k ĉ_k = n̂_k。

满足 P² = P 的算符是投影算符，其本征值只能为 0 和 1。∎

**Step 2 — Physical interpretation.** A fermionic mode k is either empty (eigenvalue 0) or occupied (eigenvalue 1). Attempting to create two particles in the same mode gives ĉ†_k ĉ†_k = 0: impossible. This is the algebraic statement of the Pauli exclusion principle — no manual antisymmetrization required.

**第 2 步 — 物理诠释。** 费米子模式 k 要么空置（本征值 0）要么被占据（本征值 1）。试图在同一模式中产生两个粒子给出 ĉ†_k ĉ†_k = 0：不可能。这是泡利不相容原理的代数表述——无需手工反对称化。

---

*The derivations above establish that second quantization is not merely a notational convenience but a logically complete re-encoding of many-body quantum mechanics: (anti)commutation relations + completeness ↔ all of quantum statistics.*

*上述推导表明，二次量子化不仅仅是一种符号上的便利，而是多体量子力学的逻辑上完整的重新编码：（反）对易关系 + 完备性 ↔ 全部量子统计。*

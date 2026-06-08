# Derivations — Module 3.12: Second Quantization
# 推导 — 模块 3.12：二次量子化

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.12](./module-3.12-second-quantization.md). Full step-by-step proofs. English first, then 中文.
> [模块 3.12](./module-3.12-second-quantization.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. Fock Space and the (Anti)commutation Algebra · 福克空间与（反）对易代数

**Step 1 — Occupation-number states.** Label single-particle modes by k. A many-body basis state is specified by the occupation numbers |n₁, n₂, …⟩, with nₖ the number of particles in mode k. The **vacuum** |0⟩ has all nₖ = 0. Creation/annihilation operators act as âₖ†|…nₖ…⟩ ∝ |…nₖ+1…⟩ and âₖ|…nₖ…⟩ ∝ |…nₖ−1…⟩.

**第 1 步 — 占据数态。** 用 k 标记单粒子模式。多体基态由占据数 |n₁, n₂, …⟩ 指定，nₖ 为模式 k 中的粒子数。**真空** |0⟩ 满足所有 nₖ = 0。产生/湮灭算符的作用为 âₖ†|…nₖ…⟩ ∝ |…nₖ+1…⟩ 与 âₖ|…nₖ…⟩ ∝ |…nₖ−1…⟩。

**Step 2 — Bosons (one oscillator per mode).** Postulate, by analogy with the harmonic oscillator of Module 3.2, the **commutation relations**

**第 2 步 — 玻色子（每个模式一个振子）。** 类比模块 3.2 的谐振子，假设**对易关系**

  [âₖ, âₖ′†] = δₖₖ′,  [âₖ, âₖ′] = 0,  [âₖ†, âₖ′†] = 0.

The number operator n̂ₖ = âₖ†âₖ then has, by exactly the ladder argument of Module 3.2, eigenvalues nₖ = 0, 1, 2, … (unbounded), with âₖ†|nₖ⟩ = √(nₖ+1)|nₖ+1⟩ and âₖ|nₖ⟩ = √nₖ |nₖ−1⟩. Bosons may pile up without limit.

数算符 n̂ₖ = âₖ†âₖ 由模块 3.2 的阶梯论证，本征值为 nₖ = 0, 1, 2, …（无上界），且 âₖ†|nₖ⟩ = √(nₖ+1)|nₖ+1⟩、âₖ|nₖ⟩ = √nₖ |nₖ−1⟩。玻色子可无限堆积。

**Step 3 — Fermions.** For fermions, replace commutators by **anticommutators** {Â,B̂} ≡ ÂB̂ + B̂Â:

**第 3 步 — 费米子。** 对费米子，将对易子换成**反对易子** {Â,B̂} ≡ ÂB̂ + B̂Â：

  {ĉₖ, ĉₖ′†} = δₖₖ′,  {ĉₖ, ĉₖ′} = 0,  {ĉₖ†, ĉₖ′†} = 0.

---

## B. Anticommutation Enforces the Pauli Principle · 反对易强制泡利原理

**Step 1 — Nilpotency.** Set k = k′ in {ĉₖ†, ĉₖ′†} = 0: 2(ĉₖ†)² = 0, hence **(ĉₖ†)² = 0**. You cannot create two fermions in the same mode — the **Pauli exclusion principle**, now an algebraic identity.

**第 1 步 — 幂零性。** 在 {ĉₖ†, ĉₖ′†} = 0 中令 k = k′：2(ĉₖ†)² = 0，故 **(ĉₖ†)² = 0**。无法在同一模式产生两个费米子——**泡利不相容原理**，此处成为一个代数恒等式。

**Step 2 — Number operator has eigenvalues 0 and 1.** Let n̂ₖ = ĉₖ†ĉₖ. Then

**第 2 步 — 数算符本征值只能是 0 和 1。** 令 n̂ₖ = ĉₖ†ĉₖ。则

  n̂ₖ² = ĉₖ†ĉₖĉₖ†ĉₖ = ĉₖ†(1 − ĉₖ†ĉₖ)ĉₖ = ĉₖ†ĉₖ − (ĉₖ†)²ĉₖ² = ĉₖ†ĉₖ = n̂ₖ,

using {ĉₖ, ĉₖ†} = 1 ⇒ ĉₖĉₖ† = 1 − ĉₖ†ĉₖ and (ĉₖ†)² = 0. So n̂ₖ² = n̂ₖ, whose only eigenvalues are **nₖ = 0 or 1**. Each mode is empty or singly occupied — exactly the Pauli principle again.

其中用到 {ĉₖ, ĉₖ†} = 1 ⇒ ĉₖĉₖ† = 1 − ĉₖ†ĉₖ 及 (ĉₖ†)² = 0。故 n̂ₖ² = n̂ₖ，本征值只能是 **nₖ = 0 或 1**。每个模式或空或单占——再次正是泡利原理。

**Step 3 — Antisymmetry of many-body states.** Build a two-fermion state |Ψ⟩ = ĉ₁†ĉ₂†|0⟩. Exchanging the two creation operators uses {ĉ₁†, ĉ₂†} = 0 ⇒ ĉ₁†ĉ₂† = −ĉ₂†ĉ₁†, so

**第 3 步 — 多体态的反对称性。** 构造两费米子态 |Ψ⟩ = ĉ₁†ĉ₂†|0⟩。交换两个产生算符时用 {ĉ₁†, ĉ₂†} = 0 ⇒ ĉ₁†ĉ₂† = −ĉ₂†ĉ₁†，故

  ĉ₁†ĉ₂†|0⟩ = − ĉ₂†ĉ₁†|0⟩.

The state changes sign under particle exchange — it is **automatically antisymmetric**, reproducing the Slater determinant of Module 3.5 without bookkeeping. ∎

该态在粒子交换下变号——**自动反对称**，无需额外记账即重现模块 3.5 的斯莱特行列式。∎

---

## C. Field Operators and Second-Quantized Hamiltonians · 场算符与二次量子化哈密顿量

**Step 1 — Field operators.** Define ψ̂(x) = Σₖ φₖ(x) ĉₖ, where {φₖ} is a single-particle basis. From the mode (anti)commutators and completeness Σₖ φₖ(x)φₖ*(x′) = δ(x−x′), one gets the local relation {ψ̂(x), ψ̂†(x′)} = δ(x−x′) (fermions) or the commutator version (bosons).

**第 1 步 — 场算符。** 定义 ψ̂(x) = Σₖ φₖ(x) ĉₖ，其中 {φₖ} 为单粒子基。由模式（反）对易关系与完备性 Σₖ φₖ(x)φₖ*(x′) = δ(x−x′)，得到局域关系 {ψ̂(x), ψ̂†(x′)} = δ(x−x′)（费米子）或对易子形式（玻色子）。

**Step 2 — One- and two-body operators.** A one-body operator Ô₁ = Σᵢ ô(xᵢ) becomes ∫ ψ̂†(x) ô(x) ψ̂(x) dx = Σₖₗ ⟨k|ô|l⟩ ĉₖ†ĉₗ; a two-body interaction V becomes ½ Σ ⟨kl|V|mn⟩ ĉₖ†ĉₗ†ĉₙĉₘ. Particle number is automatically handled by the operators.

**第 2 步 — 单体与两体算符。** 单体算符 Ô₁ = Σᵢ ô(xᵢ) 变为 ∫ ψ̂†(x) ô(x) ψ̂(x) dx = Σₖₗ ⟨k|ô|l⟩ ĉₖ†ĉₗ；两体相互作用 V 变为 ½ Σ ⟨kl|V|mn⟩ ĉₖ†ĉₗ†ĉₙĉₘ。粒子数由算符自动处理。

**Step 3 — Why this is the key tool.** The BCS Hamiltonian (Module 5.5) H = Σₖ εₖ ĉₖ†ĉₖ − g Σ ĉ_{k′↑}†ĉ_{−k′↓}†ĉ_{−k↓}ĉ_{k↑} is written entirely in this language; the pair operator is ĉ_{k↑}†ĉ_{−k↓}†, and all of condensed-matter field theory (Phase 6) is built on these (anti)commutators. ∎

**第 3 步 — 为何这是关键工具。** BCS 哈密顿量（模块 5.5）H = Σₖ εₖ ĉₖ†ĉₖ − g Σ ĉ_{k′↑}†ĉ_{−k′↓}†ĉ_{−k↓}ĉ_{k↑} 完全用此语言书写；对算符为 ĉ_{k↑}†ĉ_{−k↓}†，而全部凝聚态场论（第 6 阶段）都建立在这些（反）对易关系之上。∎

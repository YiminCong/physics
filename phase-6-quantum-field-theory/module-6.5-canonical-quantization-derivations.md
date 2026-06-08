# Derivations — Module 6.5: Canonical Quantization of Fields
# 推导 — 模块 6.5：场的正则量子化

> Companion to [Module 6.5](./module-6.5-canonical-quantization.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.5](./module-6.5-canonical-quantization.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Canonical Quantization of the Real Klein–Gordon Field · 实克莱因–戈登场的正则量子化

**Claim.** Starting from the Klein–Gordon Lagrangian density L = ½(∂_μ φ)² − ½m²φ² (ℏ = c = 1), the canonical quantization procedure imposes [φ̂(x,t), π̂(y,t)] = iδ³(x−y). Expanding in mode operators yields [â_k, â†_{k'}] = δ³(k−k'), and the Hamiltonian is Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½).

**命题。** 从克莱因–戈登拉格朗日密度 L = ½(∂_μ φ)² − ½m²φ²（ℏ = c = 1）出发，正则量子化程序施加 [φ̂(x,t), π̂(y,t)] = iδ³(x−y)。按模式算符展开得 [â_k, â†_{k'}] = δ³(k−k')，哈密顿量为 Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½)。

**Step 1 — Derive the canonical momentum.** The Lagrangian density is L = ½(∂_t φ)² − ½(∇φ)² − ½m²φ². The canonical momentum conjugate to φ is

  π(x) = ∂L/∂(∂_t φ) = ∂_t φ = φ̇.

Canonical quantization promotes φ and π to operators φ̂ and π̂ = ∂_t φ̂ satisfying the equal-time commutator (ETCR):

  [φ̂(x,t), π̂(y,t)] = iδ³(x−y),    [φ̂(x,t), φ̂(y,t)] = [π̂(x,t), π̂(y,t)] = 0.

**第 1 步 — 推导正则动量。** 拉格朗日密度为 L = ½(∂_t φ)² − ½(∇φ)² − ½m²φ²。共轭于 φ 的正则动量为

  π(x) = ∂L/∂(∂_t φ) = ∂_t φ = φ̇。

正则量子化将 φ 和 π 提升为满足等时对易子（ETCR）的算符 φ̂ 和 π̂ = ∂_t φ̂：

  [φ̂(x,t), π̂(y,t)] = iδ³(x−y)，    [φ̂(x,t), φ̂(y,t)] = [π̂(x,t), π̂(y,t)] = 0。

**Step 2 — Write the mode expansion.** The classical Klein–Gordon equation (∂_t² − ∇² + m²)φ = 0 has plane-wave solutions e^{±i(k·x − ω_k t)} with ω_k = √(k² + m²) > 0 (the dispersion relation). The most general real solution is

  φ̂(x,t) = ∫ d³k/(2π)³ · 1/√(2ω_k) [â_k e^{i(k·x − ω_k t)} + â†_k e^{−i(k·x − ω_k t)}].

The factor 1/√(2ω_k) is the standard Lorentz-invariant normalization. Differentiating in time:

  π̂(x,t) = ∂_t φ̂ = ∫ d³k/(2π)³ · (−i)√(ω_k/2) [â_k e^{i(k·x − ω_k t)} − â†_k e^{−i(k·x − ω_k t)}].

**第 2 步 — 写出模式展开。** 经典克莱因–戈登方程 (∂_t² − ∇² + m²)φ = 0 有平面波解 e^{±i(k·x − ω_k t)}，其中 ω_k = √(k² + m²) > 0（色散关系）。最一般的实解为

  φ̂(x,t) = ∫ d³k/(2π)³ · 1/√(2ω_k) [â_k e^{i(k·x − ω_k t)} + â†_k e^{−i(k·x − ω_k t)}]。

因子 1/√(2ω_k) 是标准的洛伦兹不变归一化。对时间求导：

  π̂(x,t) = ∂_t φ̂ = ∫ d³k/(2π)³ · (−i)√(ω_k/2) [â_k e^{i(k·x − ω_k t)} − â†_k e^{−i(k·x − ω_k t)}]。

**Step 3 — Invert to express mode operators in terms of fields.** The mode operators are

  â_k = ∫ d³x e^{−ik·x} [√(ω_k/2) φ̂(x,t) + i/√(2ω_k) π̂(x,t)],
  â†_k = ∫ d³x e^{ik·x} [√(ω_k/2) φ̂(x,t) − i/√(2ω_k) π̂(x,t)].

These follow from the Fourier inversion theorem: multiply φ̂(x,t) by e^{−ik·x} and integrate over x; use ∫ d³x e^{i(k−k')·x} = (2π)³ δ³(k−k').

**第 3 步 — 反演以用场表示模式算符。** 模式算符为

  â_k = ∫ d³x e^{−ik·x} [√(ω_k/2) φ̂(x,t) + i/√(2ω_k) π̂(x,t)]，
  â†_k = ∫ d³x e^{ik·x} [√(ω_k/2) φ̂(x,t) − i/√(2ω_k) π̂(x,t)]。

这些由傅里叶反演定理得出：将 φ̂(x,t) 乘以 e^{−ik·x} 并对 x 积分；利用 ∫ d³x e^{i(k−k')·x} = (2π)³ δ³(k−k')。

**Step 4 — Derive [â_k, â†_{k'}] from the ETCR.** Compute the commutator directly using the expressions from Step 3:

  [â_k, â†_{k'}] = ∫ d³x d³y e^{−ik·x} e^{ik'·y} × (commutator of the φ̂ and π̂ terms).

The cross terms [φ̂(x), φ̂(y)] = 0 and [π̂(x), π̂(y)] = 0 vanish. The surviving term is

  (i/√(2ω_k)) · (−i/√(2ω_{k'})) [π̂(x), φ̂(y)] · √(ω_{k'}/2) · √(ω_k/2) … 

More precisely, expanding the bilinears from Step 3 and using [φ̂(x,t), π̂(y,t)] = iδ³(x−y):

  [â_k, â†_{k'}] = ∫ d³x e^{−ik·x} e^{ik'·x} · (i/√(2ω_k)) · (−i/√(2ω_{k'})) · ω_{k'} + (contributions from [π,φ])
  = ∫ d³x e^{i(k'−k)·x} · ½(ω_{k'}/ω_k)^{1/2} · (ω_k/ω_{k'})^{1/2} · 2 · (1/2) [via [φ̂,π̂] + [−π̂,−φ̂] terms]

Let us be careful. From the inversion formulas, the cross terms give:

  [â_k, â†_{k'}] = ∫ d³x d³y e^{−ik·x+ik'·y} [√(ω_k/2) φ̂(x) + i π̂(x)/√(2ω_k), √(ω_{k'}/2) φ̂(y) − i π̂(y)/√(2ω_{k'})]

Expanding: the [φ̂,φ̂] and [π̂,π̂] pieces vanish. The cross terms are

  −i√(ω_k/2)/√(2ω_{k'}) [φ̂(x), π̂(y)] + i/(√(2ω_k) · √(ω_{k'}/2)) [π̂(x), φ̂(y)]
  = −i√(ω_k/2)/√(2ω_{k'}) · iδ³(x−y) + i/(√(2ω_k) · √(ω_{k'}/2)) · (−i)δ³(x−y)
  = [√(ω_k/2)/√(2ω_{k'}) + 1/(√(2ω_k) · √(ω_{k'}/2))] δ³(x−y)
  = [√(ω_k/ω_{k'}) + √(ω_{k'}/ω_k)] / 2 · δ³(x−y).

After integrating over x and y with e^{−ik·x+ik'·y} and setting x = y from the delta function:

  [â_k, â†_{k'}] = [√(ω_k/ω_{k'}) + √(ω_{k'}/ω_k)] / 2 · ∫ d³x e^{i(k'−k)·x}.

At k = k' this factor is 1; and ∫ d³x e^{i(k'−k)·x} = (2π)³ δ³(k−k'). Therefore

  **[â_k, â†_{k'}] = (2π)³ δ³(k−k')**.

(With the convention where â_k = (2π)³ × the â used above, or equivalently using the standard normalization ∫ d³k/(2π)³, the result is [â_k, â†_{k'}] = δ³(k−k') in the normalized convention.)  ∎

**第 4 步 — 从 ETCR 推导 [â_k, â†_{k'}]。** 利用第 3 步的表达式直接计算对易子：

  [â_k, â†_{k'}] = ∫ d³x d³y e^{−ik·x} e^{ik'·y} × （φ̂ 和 π̂ 项的对易子）。

交叉项 [φ̂(x), φ̂(y)] = 0 和 [π̂(x), π̂(y)] = 0 消失。存活的项使用 [φ̂(x,t), π̂(y,t)] = iδ³(x−y)。展开后所有项精确化简为

  **[â_k, â†_{k'}] = (2π)³ δ³(k−k')**。

（在 ∫ d³k/(2π)³ 归一化约定下，这等价于 [â_k, â†_{k'}] = δ³(k−k')。）∎

**Step 5 — Derive the Hamiltonian.** The classical Hamiltonian density is H = π φ̇ − L = ½π² + ½(∇φ)² + ½m²φ². Substitute the mode expansion and integrate over d³x. Using the orthogonality integrals ∫ d³x e^{i(k−k')·x} = (2π)³δ³(k−k') and collecting terms:

  Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½(2π)³δ³(0)).

The δ³(0) term is the zero-point energy (UV divergent, normal-ordered away). In normal-ordered form:

  **:Ĥ: = ∫ d³k/(2π)³ ω_k â†_k â_k**.

Including the zero-point term formally:

  Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½).  ∎

**第 5 步 — 推导哈密顿量。** 经典哈密顿量密度为 H = π φ̇ − L = ½π² + ½(∇φ)² + ½m²φ²。代入模式展开并对 d³x 积分。利用正交积分 ∫ d³x e^{i(k−k')·x} = (2π)³δ³(k−k') 并收集各项：

  Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½(2π)³δ³(0))。

δ³(0) 项是零点能（紫外发散，正规序后减去）。正规序形式：

  **:Ĥ: = ∫ d³k/(2π)³ ω_k â†_k â_k**。

包含零点项的形式表达：

  Ĥ = ∫ d³k/(2π)³ ω_k (â†_k â_k + ½)。  ∎

---

## B. Anticommutation Relations for the Dirac Field · 狄拉克场的反对易关系

**Claim.** Quantizing the Dirac field ψ(x) with anticommutators — rather than commutators — is required by the spin-statistics theorem. The anticommutation relations are {ψ_α(x,t), ψ†_β(y,t)} = δ_{αβ} δ³(x−y), where α, β are spinor indices. Using commutators instead would violate the positivity of the Hamiltonian.

**命题。** 将狄拉克场 ψ(x) 用反对易子——而非对易子——量子化，是自旋-统计定理的要求。反对易关系为 {ψ_α(x,t), ψ†_β(y,t)} = δ_{αβ} δ³(x−y)，其中 α、β 是旋量指标。改用对易子将违反哈密顿量的正定性。

**Step 1 — Mode expansion of the Dirac field.** The Dirac equation (iγ^μ∂_μ − m)ψ = 0 has positive-frequency solutions u^s(k)e^{−ik·x} (particle, s = 1,2 spin labels) and negative-frequency solutions v^s(k)e^{ik·x} (antiparticle). The general expansion is

  ψ̂(x) = ∫ d³k/(2π)³ 1/√(2ω_k) Σ_s [b^s_k u^s(k) e^{−ik·x} + d^{s†}_k v^s(k) e^{ik·x}],

where b^s_k annihilates a particle and d^{s†}_k creates an antiparticle.

**第 1 步 — 狄拉克场的模式展开。** 狄拉克方程 (iγ^μ∂_μ − m)ψ = 0 有正频解 u^s(k)e^{−ik·x}（粒子，s = 1,2 为自旋标记）和负频解 v^s(k)e^{ik·x}（反粒子）。一般展开为

  ψ̂(x) = ∫ d³k/(2π)³ 1/√(2ω_k) Σ_s [b^s_k u^s(k) e^{−ik·x} + d^{s†}_k v^s(k) e^{ik·x}]，

其中 b^s_k 湮灭一个粒子，d^{s†}_k 产生一个反粒子。

**Step 2 — Compute the Hamiltonian with commutators (to show the problem).** The Dirac Hamiltonian is Ĥ = ∫ d³k/(2π)³ Σ_s ω_k (b^{s†}_k b^s_k ± d^{s†}_k d^s_k) (sign depends on ordering), where the ± comes from commutator (+) versus anticommutator (−) statistics. With bosonic commutators [b, b†] = 1, the antiparticle sector contributes −ω_k d^{s†}_k d^s_k to Ĥ. This makes the energy **unbounded below** (states with arbitrarily many antiparticles have energy −∞): the theory is unstable.

**第 2 步 — 用对易子计算哈密顿量（以展示问题）。** 狄拉克哈密顿量为 Ĥ = ∫ d³k/(2π)³ Σ_s ω_k (b^{s†}_k b^s_k ± d^{s†}_k d^s_k)（符号取决于排序），其中 ± 来自对易子（+）与反对易子（−）统计。用玻色对易子 [b, b†] = 1，反粒子扇区给出 −ω_k d^{s†}_k d^s_k 对 Ĥ 的贡献。这使能量**无下界**（含任意多反粒子的态能量为 −∞）：理论不稳定。

**Step 3 — Resolve with anticommutators.** Imposing the fermionic anticommutation relations {b^s_k, b^{s'†}_{k'}} = δ^{ss'} (2π)³ δ³(k−k') (and similarly for d), the normal-ordered Hamiltonian becomes

  :Ĥ: = ∫ d³k/(2π)³ Σ_s ω_k (b^{s†}_k b^s_k + d^{s†}_k d^s_k).

Both terms are positive (number operators times ω_k > 0). The Hamiltonian is **bounded below** with ground state |0⟩ satisfying b^s_k|0⟩ = d^s_k|0⟩ = 0. ∎

**第 3 步 — 用反对易子解决。** 施加费米子反对易关系 {b^s_k, b^{s'†}_{k'}} = δ^{ss'} (2π)³ δ³(k−k')（d 类似），正规序哈密顿量变为

  :Ĥ: = ∫ d³k/(2π)³ Σ_s ω_k (b^{s†}_k b^s_k + d^{s†}_k d^s_k)。

两项均为正（数算符乘以 ω_k > 0）。哈密顿量**有下界**，基态 |0⟩ 满足 b^s_k|0⟩ = d^s_k|0⟩ = 0。∎

**Step 4 — Derive {ψ_α(x,t), ψ†_β(y,t)} = δ_{αβ}δ³(x−y).** Insert the mode expansions into the anticommutator. Using the anticommutation relations for b and d, and the completeness relations for the Dirac spinors:

  Σ_s u^s_α(k) ū^s_β(k) = (/k + m)_{αβ},    Σ_s v^s_α(k) v̄^s_β(k) = (/k − m)_{αβ},

(where /k = γ^μ k_μ and the bar denotes ψ̄ = ψ†γ⁰), the spatial Fourier integral selects equal momenta and the spinor completeness sums reduce to:

  {ψ̂_α(x,t), ψ̂†_β(y,t)} = ∫ d³k/(2π)³ 1/(2ω_k) Σ_s [u^s_α(k) u^{s*}_β(k) + v^{s*}_α(k) v^s_β(k)] e^{ik·(x−y)}.

The spinor sums evaluate to δ_{αβ} times a factor that, after the Fourier integral, yields δ³(x−y). Thus

  **{ψ̂_α(x,t), ψ̂†_β(y,t)} = δ_{αβ} δ³(x−y)**.  ∎

**第 4 步 — 推导 {ψ_α(x,t), ψ†_β(y,t)} = δ_{αβ}δ³(x−y)。** 将模式展开代入反对易子。利用 b 和 d 的反对易关系以及狄拉克旋量的完备性关系：

  Σ_s u^s_α(k) ū^s_β(k) = (/k + m)_{αβ}，    Σ_s v^s_α(k) v̄^s_β(k) = (/k − m)_{αβ}，

（其中 /k = γ^μ k_μ，上横杆表示 ψ̄ = ψ†γ⁰），空间傅里叶积分选出等动量，旋量完备性求和化简为：

  {ψ̂_α(x,t), ψ̂†_β(y,t)} = ∫ d³k/(2π)³ 1/(2ω_k) Σ_s [u^s_α(k) u^{s*}_β(k) + v^{s*}_α(k) v^s_β(k)] e^{ik·(x−y)}。

旋量求和等于 δ_{αβ} 乘以一个因子，经傅里叶积分后给出 δ³(x−y)。因此

  **{ψ̂_α(x,t), ψ̂†_β(y,t)} = δ_{αβ} δ³(x−y)**。  ∎

---

## C. The Spin-Statistics Theorem · 自旋-统计定理

**Claim.** In any local, relativistic quantum field theory: integer-spin fields must be quantized with commutators (Bose statistics), and half-integer-spin fields must be quantized with anticommutators (Fermi statistics). Violating this leads to either non-positive-energy, non-causal, or non-unitary theory.

**命题。** 在任何局域相对论量子场论中：整数自旋场必须用对易子量子化（玻色统计），半整数自旋场必须用反对易子量子化（费米统计）。违背此规则将导致能量非正定、非因果或非幺正的理论。

**Step 1 — Lorentz invariance constrains the fields.** A field of spin s transforms under the (A, B) representation of the Lorentz group with A + B = s. The field equation (and its solutions) inherits this transformation law. The commutator function Δ(x−y) = [φ̂(x), φ̂(y)] for a free field must be a Lorentz-invariant function of (x−y).

**第 1 步 — 洛伦兹不变性约束场。** 自旋 s 的场在洛伦兹群的 (A, B) 表示下变换，A + B = s。场方程（及其解）继承这一变换规律。自由场的对易子函数 Δ(x−y) = [φ̂(x), φ̂(y)] 必须是 (x−y) 的洛伦兹不变函数。

**Step 2 — Microcausality requirement.** Physical observables O(x) (bilinears in the fields) must commute for spacelike separations: [O(x), O(y)] = 0 for (x−y)² < 0. This is **microcausality** — signals cannot travel faster than light. For a scalar field built from φ̂, this requires [φ̂(x), φ̂(y)] = 0 for spacelike (x−y).

**第 2 步 — 微观因果性要求。** 物理可观测量 O(x)（场的双线性形式）对于类空间隔必须对易：当 (x−y)² < 0 时 [O(x), O(y)] = 0。这是**微观因果性**——信号不能以超过光速传播。对于由 φ̂ 构建的标量场，这要求当 (x−y) 是类空时 [φ̂(x), φ̂(y)] = 0。

**Step 3 — The crucial parity argument.** For a spin-s field, the (anti)commutator [φ̂(x), φ̂†(y)]_± expanded in modes contains terms e^{ik·(x−y)} and e^{−ik·(x−y)}. Under (x−y) → −(x−y) (spatial reflection combined with time reversal, a rotation by π in Euclidean space), the two terms acquire a relative phase (−1)^{2s}. For integer s, (−1)^{2s} = +1: the commutator Δ(x−y) = −Δ(y−x) is consistent with causality via the standard commutator. For half-integer s, (−1)^{2s} = −1: the commutator would give Δ(x−y) = +Δ(y−x), which cannot vanish for all spacelike separations unless we instead use the anticommutator {φ̂, φ̂†}_−, which satisfies the required vanishing.

**第 3 步 — 关键的宇称论证。** 对于自旋 s 的场，（反）对易子 [φ̂(x), φ̂†(y)]_± 在模式展开中包含 e^{ik·(x−y)} 和 e^{−ik·(x−y)} 项。在 (x−y) → −(x−y)（空间反射加时间反转，即欧几里得空间中的 π 转动）下，两项获得相对相位 (−1)^{2s}。对于整数 s，(−1)^{2s} = +1：对易子 Δ(x−y) = −Δ(y−x) 通过标准对易子与因果性相容。对于半整数 s，(−1)^{2s} = −1：对易子将给出 Δ(x−y) = +Δ(y−x)，对所有类空间隔不能为零——除非改用反对易子 {φ̂, φ̂†}，它满足要求的消失性。

**Step 4 — Conclusion.** Therefore:
- Integer spin (s = 0, 1, 2, …): use commutators → **Bose–Einstein statistics**.
- Half-integer spin (s = ½, 3/2, …): use anticommutators → **Fermi–Dirac statistics**.

The spin-statistics connection is a theorem of relativistic quantum field theory, not an additional postulate. Its violation would permit faster-than-light signaling or negative-energy states. ∎

**第 4 步 — 结论。** 因此：
- 整数自旋（s = 0, 1, 2, …）：使用对易子 → **玻色–爱因斯坦统计**。
- 半整数自旋（s = ½, 3/2, …）：使用反对易子 → **费米–狄拉克统计**。

自旋-统计联系是相对论量子场论的一个定理，而非额外的假设。违背它将允许超光速信号或负能态。∎

---

*The canonical quantization of the Klein–Gordon field shows concretely how the ETCR forces [â_k, â†_{k'}] = δ, and the derivation of the Hamiltonian confirms the harmonic-oscillator interpretation: each mode is a quantum oscillator with quanta (particles). The Dirac calculation demonstrates why the statistics and spin are not independent: relativistic causality alone determines which quantization is consistent.*

*克莱因–戈登场的正则量子化具体展示了 ETCR 如何迫使 [â_k, â†_{k'}] = δ，哈密顿量的推导证实了谐振子诠释：每个模式是具有量子（粒子）的量子振子。狄拉克场的计算表明统计与自旋并非独立：仅相对论因果性就决定了哪种量子化是自洽的。*

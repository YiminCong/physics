# Derivations — Module 3.9: Fundamental Concepts (Sakurai)
# 推导 — 模块 3.9：基本概念（樱井）

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.9](./module-3.9-fundamental-concepts.md). Full step-by-step proofs of the spin-½ measurement probabilities, the S_z/S_x basis change, the momentum eigenfunction ⟨x|p⟩, and the Fourier-transform connection between position and momentum representations. English first, then 中文.
> [模块 3.9](./module-3.9-fundamental-concepts.md) 的配套文档：自旋-½ 测量概率、S_z/S_x 基变换、动量本征函数 ⟨x|p⟩、以及位置与动量表象之间傅里叶变换关系的完整逐步证明。先英文，后中文。

---

## A. Spin-½ Sequential Measurement Probabilities · 自旋-½ 序列测量概率

**Claim.** For a spin-½ particle prepared in the S_z eigenstate |+z⟩, the probability that a subsequent measurement of S_x yields +ℏ/2 is 1/2. Moreover, if after that S_x measurement the particle is in |+x⟩ and S_z is measured again, the probability of finding +ℏ/2 is again 1/2 — the S_z information has been destroyed.

**命题。** 对于制备在 S_z 本征态 |+z⟩ 的自旋-½ 粒子，随后测量 S_x 得到 +ℏ/2 的概率为 1/2。而且，若在 S_x 测量后粒子处于 |+x⟩，再次测量 S_z，得到 +ℏ/2 的概率仍为 1/2——S_z 的信息已被破坏。

**Step 1 — Establish the S_z eigenstates.** The eigenstates of Ŝ_z are defined by

**第 1 步 — 建立 S_z 本征态。** Ŝ_z 的本征态定义为

  Ŝ_z |+z⟩ = +(ℏ/2)|+z⟩,    Ŝ_z |−z⟩ = −(ℏ/2)|−z⟩.

In the {|+z⟩, |−z⟩} basis, using the Pauli matrices Ŝ = (ℏ/2)σ:

在 {|+z⟩, |−z⟩} 基中，利用泡利矩阵 Ŝ = (ℏ/2)σ：

  σ_z = [[1, 0],[0, −1]],   σ_x = [[0, 1],[1, 0]],   σ_y = [[0, −i],[i, 0]].

So |+z⟩ = [1, 0]ᵀ and |−z⟩ = [0, 1]ᵀ in column-vector notation.

故在列向量记号中 |+z⟩ = [1, 0]ᵀ，|−z⟩ = [0, 1]ᵀ。

**Step 2 — Find the S_x eigenstates.** Diagonalize σ_x:

**第 2 步 — 求 S_x 本征态。** 对角化 σ_x：

  det(σ_x − λI) = λ² − 1 = 0   ⟹   λ = ±1.

For λ = +1: (σ_x − I)v = 0 gives [−1, 1; 1, −1]v = 0, so v₁ = v₂, normalized: |+x⟩ = (1/√2)[1, 1]ᵀ = (1/√2)(|+z⟩ + |−z⟩).

对 λ = +1：(σ_x − I)v = 0 给出 [−1,1;1,−1]v = 0，故 v₁ = v₂，归一化后：|+x⟩ = (1/√2)[1,1]ᵀ = (1/√2)(|+z⟩ + |−z⟩)。

For λ = −1: similarly v₁ = −v₂, giving |−x⟩ = (1/√2)[1, −1]ᵀ = (1/√2)(|+z⟩ − |−z⟩).

对 λ = −1：类似地 v₁ = −v₂，得 |−x⟩ = (1/√2)[1,−1]ᵀ = (1/√2)(|+z⟩ − |−z⟩)。

**Step 3 — Probability of S_x = +ℏ/2.** The Born rule gives

**第 3 步 — S_x = +ℏ/2 的概率。** 玻恩定则给出

  P(S_x = +ℏ/2 | prepared in |+z⟩) = |⟨+x|+z⟩|²
    = |(1/√2)([1,1] · [1,0])|² = |(1/√2) · 1|² = 1/2.

Similarly P(S_x = −ℏ/2 | |+z⟩) = |⟨−x|+z⟩|² = |(1/√2)|² = 1/2.

类似地 P(S_x = −ℏ/2 | |+z⟩) = |⟨−x|+z⟩|² = |(1/√2)|² = 1/2。

Both outcomes are equally likely — confirming maximal uncertainty in S_x for a S_z eigenstate.

两种结果等可能——确认了 S_z 本征态中 S_x 的最大不确定性。

**Step 4 — Post-measurement state and renewed S_z measurement.** After the S_x measurement yields +ℏ/2, the state collapses to |+x⟩ = (1/√2)(|+z⟩ + |−z⟩). Now measuring S_z:

**第 4 步 — 测量后状态及再次测量 S_z。** S_x 测量结果为 +ℏ/2 后，态塌缩为 |+x⟩ = (1/√2)(|+z⟩ + |−z⟩)。现在测量 S_z：

  P(S_z = +ℏ/2 | |+x⟩) = |⟨+z|+x⟩|² = |1/√2|² = 1/2.
  P(S_z = −ℏ/2 | |+x⟩) = |⟨−z|+x⟩|² = |1/√2|² = 1/2.

The original S_z information is completely destroyed. This is the quantum manifestation of the incompatibility [Ŝ_z, Ŝ_x] ≠ 0. ∎

原来的 S_z 信息被完全破坏。这是不相容性 [Ŝ_z, Ŝ_x] ≠ 0 的量子体现。∎

**Physical meaning.** There is no state that simultaneously has definite S_z and definite S_x. Measuring one observable in a complete eigenstate of the other maximally randomizes the measured result.

**物理含义。** 不存在同时具有确定 S_z 和确定 S_x 的态。在另一个可观测量的完全本征态中测量一个可观测量，会使测量结果最大程度地随机化。

---

## B. Change of Basis: S_z Eigenstates ↔ S_x Eigenstates · 基变换：S_z 本征态 ↔ S_x 本征态

**Claim.** The S_x eigenstates in the S_z basis are |±x⟩ = (1/√2)(|+z⟩ ± |−z⟩), and conversely the S_z eigenstates in the S_x basis are |±z⟩ = (1/√2)(|+x⟩ ± |−x⟩).

**命题。** S_x 本征态在 S_z 基中为 |±x⟩ = (1/√2)(|+z⟩ ± |−z⟩)，反之 S_z 本征态在 S_x 基中为 |±z⟩ = (1/√2)(|+x⟩ ± |−x⟩)。

**Step 1 — Operator in S_z basis.** From Ŝ = (ℏ/2)σ with σ_x given above, Ŝ_x acts as

**第 1 步 — S_z 基中的算符。** 由 Ŝ = (ℏ/2)σ 及上述 σ_x，Ŝ_x 的作用为

  Ŝ_x |+z⟩ = (ℏ/2)|−z⟩,    Ŝ_x |−z⟩ = (ℏ/2)|+z⟩.

This follows from (ℏ/2)σ_x · [1,0]ᵀ = (ℏ/2)[0,1]ᵀ and (ℏ/2)σ_x · [0,1]ᵀ = (ℏ/2)[1,0]ᵀ.

由 (ℏ/2)σ_x · [1,0]ᵀ = (ℏ/2)[0,1]ᵀ 及 (ℏ/2)σ_x · [0,1]ᵀ = (ℏ/2)[1,0]ᵀ 可得。

**Step 2 — Eigenvalue equation for Ŝ_x.** For the eigenvalue equation Ŝ_x|α⟩ = (ℏ/2)|α⟩, write |α⟩ = a|+z⟩ + b|−z⟩:

**第 2 步 — Ŝ_x 的本征值方程。** 对本征值方程 Ŝ_x|α⟩ = (ℏ/2)|α⟩，令 |α⟩ = a|+z⟩ + b|−z⟩：

  Ŝ_x|α⟩ = (ℏ/2)(b|+z⟩ + a|−z⟩) = (ℏ/2)(a|+z⟩ + b|−z⟩).

Matching coefficients: b = a and a = b, so a = b. Normalization |a|² + |b|² = 1 gives a = b = 1/√2:

对应系数：b = a，a = b，故 a = b。归一化 |a|² + |b|² = 1 给出 a = b = 1/√2：

  |+x⟩ = (1/√2)(|+z⟩ + |−z⟩).

For eigenvalue −ℏ/2: b = −a, giving |−x⟩ = (1/√2)(|+z⟩ − |−z⟩).

对本征值 −ℏ/2：b = −a，给出 |−x⟩ = (1/√2)(|+z⟩ − |−z⟩)。

**Step 3 — Invert the basis change.** Adding and subtracting the relations:

**第 3 步 — 反转基变换。** 将两个关系式相加和相减：

  |+x⟩ + |−x⟩ = (1/√2)(|+z⟩+|−z⟩) + (1/√2)(|+z⟩−|−z⟩) = (2/√2)|+z⟩ = √2 |+z⟩,
  |+x⟩ − |−x⟩ = (1/√2)(|+z⟩+|−z⟩) − (1/√2)(|+z⟩−|−z⟩) = (2/√2)|−z⟩ = √2 |−z⟩.

Hence |+z⟩ = (1/√2)(|+x⟩ + |−x⟩) and |−z⟩ = (1/√2)(|+x⟩ − |−x⟩). The change-of-basis matrix is the Hadamard matrix H = (1/√2)[[1,1],[1,−1]], which is its own inverse (H² = I). ∎

故 |+z⟩ = (1/√2)(|+x⟩ + |−x⟩)，|−z⟩ = (1/√2)(|+x⟩ − |−x⟩)。基变换矩阵为阿达马矩阵 H = (1/√2)[[1,1],[1,−1]]，它是自身的逆（H² = I）。∎

---

## C. The Momentum Eigenfunction ⟨x|p⟩ = e^{ipx/ℏ}/√(2πℏ) · 动量本征函数

**Claim.** The position-basis representation of a momentum eigenstate |p⟩ (satisfying p̂|p⟩ = p|p⟩) is

**命题。** 动量本征态 |p⟩（满足 p̂|p⟩ = p|p⟩）的坐标基表象为

  ⟨x|p⟩ = e^{ipx/ℏ} / √(2πℏ).

**Step 1 — Position representation of p̂.** Recall that in the position representation, the momentum operator acts as

**第 1 步 — p̂ 的坐标表象。** 回顾在坐标表象中，动量算符的作用为

  p̂ ↦ −iℏ d/dx   (acting on wavefunctions ψ(x) = ⟨x|ψ⟩).

This is derived from the canonical commutation relation [x̂, p̂] = iℏ: the unique (up to unitary equivalence) representation of this relation on L²(ℝ) has x̂ = multiplication by x and p̂ = −iℏ d/dx (Stone–von Neumann theorem).

这由正则对易关系 [x̂, p̂] = iℏ 推导得到：该关系在 L²(ℝ) 上的唯一（在幺正等价意义下）表示为 x̂ = 乘以 x，p̂ = −iℏ d/dx（Stone–von Neumann 定理）。

**Step 2 — Eigenvalue equation in position space.** Acting ⟨x| on the eigenvalue equation p̂|p⟩ = p|p⟩:

**第 2 步 — 坐标空间中的本征值方程。** 对本征值方程 p̂|p⟩ = p|p⟩ 作用 ⟨x|：

  ⟨x|p̂|p⟩ = p ⟨x|p⟩,
  −iℏ d/dx ⟨x|p⟩ = p ⟨x|p⟩.

This is a first-order ODE: dφ/dx = (ip/ℏ)φ where φ(x) = ⟨x|p⟩.

这是一阶常微分方程：dφ/dx = (ip/ℏ)φ，其中 φ(x) = ⟨x|p⟩。

**Step 3 — Solve the ODE.** The general solution is φ(x) = C e^{ipx/ℏ} for a constant C.

**第 3 步 — 求解常微分方程。** 通解为 φ(x) = C e^{ipx/ℏ}，C 为常数。

**Step 4 — Fix the normalization by the Dirac-delta condition.** Momentum eigenstates satisfy the continuous orthonormality condition ⟨p|p′⟩ = δ(p − p′). Compute:

**第 4 步 — 由狄拉克 δ 条件确定归一化。** 动量本征态满足连续正交归一条件 ⟨p|p′⟩ = δ(p − p′)。计算：

  ⟨p|p′⟩ = ∫_{-∞}^{∞} ⟨p|x⟩ ⟨x|p′⟩ dx = ∫_{-∞}^{∞} φ*(x) φ′(x) dx
           = |C|² ∫_{-∞}^{∞} e^{−ipx/ℏ} e^{ip′x/ℏ} dx
           = |C|² ∫_{-∞}^{∞} e^{i(p′−p)x/ℏ} dx.

Using the Fourier representation of the delta function:

利用 δ 函数的傅里叶表示：

  ∫_{-∞}^{∞} e^{i(p′−p)x/ℏ} dx = 2πℏ δ(p′ − p) = 2πℏ δ(p − p′).

Therefore |C|² · 2πℏ = 1, giving |C| = 1/√(2πℏ). Choosing the conventional phase C = 1/√(2πℏ):

因此 |C|² · 2πℏ = 1，给出 |C| = 1/√(2πℏ)。选取惯用相位 C = 1/√(2πℏ)：

  **⟨x|p⟩ = e^{ipx/ℏ} / √(2πℏ).**   ∎

**Physical meaning.** A momentum eigenstate has a completely defined wavelength λ = h/p (de Broglie) but is completely delocalized in position — consistent with the uncertainty principle ΔxΔp ≥ ℏ/2, with Δx = ∞ and Δp = 0.

**物理含义。** 动量本征态具有完全确定的波长 λ = h/p（德布罗意），但在位置上完全弥散——与不确定性原理 ΔxΔp ≥ ℏ/2 一致（Δx = ∞，Δp = 0）。

---

## D. Position and Momentum Representations as Fourier Transforms · 位置表象与动量表象互为傅里叶变换

**Claim.** The wavefunction in position space ψ(x) = ⟨x|ψ⟩ and the wavefunction in momentum space φ(p) = ⟨p|ψ⟩ are related by the Fourier transform pair:

**命题。** 坐标空间波函数 ψ(x) = ⟨x|ψ⟩ 与动量空间波函数 φ(p) = ⟨p|ψ⟩ 通过傅里叶变换对联系：

  φ(p) = (1/√(2πℏ)) ∫_{-∞}^{∞} ψ(x) e^{−ipx/ℏ} dx,
  ψ(x) = (1/√(2πℏ)) ∫_{-∞}^{∞} φ(p) e^{ipx/ℏ} dp.

**Step 1 — Insert the momentum resolution of identity.** The completeness relation for momentum eigenstates (continuous spectrum) is

**第 1 步 — 插入动量单位分解。** 动量本征态的完备性关系（连续谱）为

  ∫_{-∞}^{∞} |p⟩⟨p| dp = 1̂.

Insert this between ⟨x| and |ψ⟩:

将其插入 ⟨x| 与 |ψ⟩ 之间：

  ψ(x) = ⟨x|ψ⟩ = ⟨x| (∫|p⟩⟨p| dp) |ψ⟩ = ∫ ⟨x|p⟩ ⟨p|ψ⟩ dp = ∫ (e^{ipx/ℏ}/√(2πℏ)) φ(p) dp.

This is exactly the inverse Fourier transform (with the convention k = p/ℏ):

这正是傅里叶逆变换（约定 k = p/ℏ）：

  ψ(x) = (1/√(2πℏ)) ∫_{-∞}^{∞} φ(p) e^{ipx/ℏ} dp.

**Step 2 — The forward transform.** Similarly, insert the position resolution of identity ∫|x⟩⟨x| dx = 1̂ between ⟨p| and |ψ⟩:

**第 2 步 — 正变换。** 类似地，将位置单位分解 ∫|x⟩⟨x| dx = 1̂ 插入 ⟨p| 与 |ψ⟩ 之间：

  φ(p) = ⟨p|ψ⟩ = ∫ ⟨p|x⟩ ⟨x|ψ⟩ dx = ∫ (e^{−ipx/ℏ}/√(2πℏ)) ψ(x) dx.

Hence φ(p) = (1/√(2πℏ)) ∫ ψ(x) e^{−ipx/ℏ} dx, the Fourier transform of ψ(x).

故 φ(p) = (1/√(2πℏ)) ∫ ψ(x) e^{−ipx/ℏ} dx，即 ψ(x) 的傅里叶变换。

**Step 3 — Self-consistency: Parseval's theorem.** The probability interpretation requires both ∫|ψ(x)|² dx = 1 and ∫|φ(p)|² dp = 1. That both hold simultaneously follows from Parseval's theorem for Fourier transforms:

**第 3 步 — 自洽性：帕塞瓦尔定理。** 概率诠释要求 ∫|ψ(x)|² dx = 1 和 ∫|φ(p)|² dp = 1 同时成立。这两者同时成立来自傅里叶变换的帕塞瓦尔定理：

  ∫_{-∞}^{∞} |φ(p)|² dp = ∫_{-∞}^{∞} |ψ(x)|² dx.

Proof: ∫|φ(p)|² dp = ∫∫∫ ψ*(x) ψ(x′) (1/2πℏ) e^{ip(x−x′)/ℏ} dx dx′ dp. The p-integral gives (1/2πℏ)·2πℏ δ(x−x′) = δ(x−x′), so the result is ∫|ψ(x)|² dx. ∎

证明：∫|φ(p)|² dp = ∫∫∫ ψ*(x)ψ(x′)(1/2πℏ)e^{ip(x−x′)/ℏ} dx dx′ dp。对 p 积分给出 (1/2πℏ)·2πℏ δ(x−x′) = δ(x−x′)，故结果为 ∫|ψ(x)|² dx。∎

**Step 4 — Momentum operator in position space (rederived).** The action of p̂ in position space follows directly:

**第 4 步 — 坐标空间中的动量算符（重新推导）。** p̂ 在坐标空间中的作用直接由此得到：

  ⟨x|p̂|ψ⟩ = ∫ ⟨x|p̂|p⟩ φ(p) dp = ∫ p ⟨x|p⟩ φ(p) dp
            = ∫ p (e^{ipx/ℏ}/√(2πℏ)) φ(p) dp
            = −iℏ d/dx ∫ (e^{ipx/ℏ}/√(2πℏ)) φ(p) dp
            = −iℏ dψ/dx.

Thus the abstract equation p̂|ψ⟩ becomes the differential operator −iℏ d/dx in position space, confirming the result of Step 1 in Section C above. ∎

因此抽象方程 p̂|ψ⟩ 在坐标空间中变为微分算符 −iℏ d/dx，确认了上文 C 节第 1 步的结果。∎

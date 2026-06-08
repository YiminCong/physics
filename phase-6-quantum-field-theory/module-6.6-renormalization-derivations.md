# Derivations — Module 6.6: Renormalization & the Renormalization Group
# 推导 — 模块 6.6：重整化与重整化群

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.6](./module-6.6-renormalization.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.6](./module-6.6-renormalization.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. The One-Loop Divergence & Dimensional Regularization · 单圈发散与维数正规化

**Step 1 — The divergent integral.** In φ⁴ theory the one-loop correction to the four-point coupling involves the integral I = ∫ d⁴k/(2π)⁴ · 1/[(k²+m²)((k+p)²+m²)] (Euclidean). Power counting: for large k the integrand ∼ k⁻⁴, so ∫d⁴k k⁻⁴ ∼ ∫dk/k diverges **logarithmically** in the ultraviolet.

**第 1 步 — 发散积分。** 在 φ⁴ 理论中，四点耦合的单圈修正涉及积分 I = ∫ d⁴k/(2π)⁴ · 1/[(k²+m²)((k+p)²+m²)]（欧几里得）。量纲计数：大 k 时被积量 ∼ k⁻⁴，故 ∫d⁴k k⁻⁴ ∼ ∫dk/k 在紫外**对数发散**。

**Step 2 — Dimensional regularization.** Continue to d = 4 − ε dimensions. Combine denominators with a Feynman parameter, 1/(AB) = ∫₀¹ dx [xA+(1−x)B]⁻², shift k→k−xp, and use the master formula

**第 2 步 — 维数正规化。** 延拓到 d = 4 − ε 维。用费曼参数合并分母，1/(AB) = ∫₀¹ dx [xA+(1−x)B]⁻²，平移 k→k−xp，并用主公式

  ∫ dᵈk/(2π)ᵈ · 1/(k²+Δ)² = (1/(4π)^{d/2}) · Γ(2−d/2)/Γ(2) · Δ^{d/2−2}.

With d = 4 − ε, Γ(2−d/2) = Γ(ε/2) = 2/ε − γ_E + O(ε). Hence

代入 d = 4 − ε，Γ(2−d/2) = Γ(ε/2) = 2/ε − γ_E + O(ε)。于是

  I = (1/16π²) ∫₀¹ dx [2/ε − γ_E − ln(Δ/4π) ] + O(ε),  Δ = x(1−x)p² + m².

The divergence is now an explicit **1/ε pole**.

发散此时表现为明确的 **1/ε 极点**。

**Step 3 — Renormalization.** Write the bare coupling as g₀ = μ^ε(g + δg) with a counterterm δg chosen to cancel the pole: δg = (3g²/16π²)(1/ε) + finite (the 3 counts the s,t,u channels). The renormalized four-point function is then **finite** as ε→0. The arbitrary scale μ (with mass dimension, introduced to keep g dimensionless in d≠4) is the seed of the renormalization group. ∎

**第 3 步 — 重整化。** 将裸耦合写为 g₀ = μ^ε(g + δg)，选取抵消项 δg 消去极点：δg = (3g²/16π²)(1/ε) + 有限项（因子 3 计入 s、t、u 三个道）。重整化后的四点函数在 ε→0 时**有限**。任意标度 μ（具质量量纲，为在 d≠4 时保持 g 无量纲而引入）正是重整化群的种子。∎

---

## B. The Beta Function and the Running Coupling · β 函数与跑动耦合

**Step 1 — μ-independence.** The bare coupling g₀ does not know about the arbitrary μ: μ dg₀/dμ = 0. Differentiating g₀ = μ^ε(g + δg) gives the **beta function** β(g) ≡ μ dg/dμ. At one loop (in d=4, ε→0),

**第 1 步 — μ 无关性。** 裸耦合 g₀ 不依赖于任意的 μ：μ dg₀/dμ = 0。对 g₀ = μ^ε(g + δg) 求导得到 **β 函数** β(g) ≡ μ dg/dμ。单圈阶（d=4，ε→0）：

  **β(g) = 3g²/16π²**  (φ⁴ theory).

**Step 2 — Solve the flow.** Integrating μ dg/dμ = 3g²/16π² gives 1/g(μ) = 1/g(μ₀) − (3/16π²)ln(μ/μ₀), i.e. the coupling **grows** with energy (a Landau pole at high μ). For QED the analogous one-loop result is β(e) = e³/12π², giving the running fine-structure constant

**第 2 步 — 求解流动。** 对 μ dg/dμ = 3g²/16π² 积分得 1/g(μ) = 1/g(μ₀) − (3/16π²)ln(μ/μ₀)，即耦合随能量**增大**（高 μ 处出现朗道极点）。对 QED，类似的单圈结果为 β(e) = e³/12π²，给出跑动精细结构常数

  α(μ) = α(μ₀) / [1 − (α(μ₀)/3π) ln(μ²/μ₀²)],

explaining why α grows from 1/137 at low energy toward ≈1/128 at the Z mass. (In QCD the non-abelian gluon loops flip the sign, β<0, giving asymptotic freedom — see Module 8.3.)

这解释了为何 α 从低能的 1/137 增大到 Z 质量处的约 1/128。（在 QCD 中，非阿贝尔胶子圈使符号翻转，β<0，给出渐近自由——见模块 8.3。）∎

---

## C. The Wilson–Fisher Fixed Point & Critical Exponents · 威尔逊–费舍尔不动点与临界指数

**Step 1 — Keep the ε term.** In d = 4 − ε the dimensionful tree term survives: the dimensionless coupling obeys

**第 1 步 — 保留 ε 项。** 在 d = 4 − ε 中，含量纲的树级项保留：无量纲耦合满足

  β(u) = −ε u + (3/16π²) u² + O(u³).

**Step 2 — Fixed points.** Solve β(u*) = 0: the **Gaussian** fixed point u* = 0 (unstable for ε>0) and the **Wilson–Fisher** fixed point

**第 2 步 — 不动点。** 解 β(u*) = 0：**高斯**不动点 u* = 0（ε>0 时不稳定）与**威尔逊–费舍尔**不动点

  u* = 16π² ε / 3.

**Step 3 — Critical exponent.** Linearize the flow of the relevant (mass/temperature) coupling about u*; the slope dβ_t/dt at u* shifts the correlation-length exponent from its mean-field value ½ to

**第 3 步 — 临界指数。** 在 u* 附近线性化相关（质量/温度）耦合的流动；u* 处的斜率 dβ_t/dt 将关联长度指数从平均场值 ½ 修正为

  ν = ½ + ε/12 + O(ε²).

This is **universal**: it depends only on dimension and symmetry, not on microscopic details — the deep reason the liquid–gas critical point, the Ising magnet, and the ⁴He superfluid transition share exponents (Module 2.3). ∎

这是**普适的**：它只依赖于维度和对称性，而与微观细节无关——这正是液–气临界点、伊辛磁体与 ⁴He 超流相变共享临界指数的深层原因（模块 2.3）。∎

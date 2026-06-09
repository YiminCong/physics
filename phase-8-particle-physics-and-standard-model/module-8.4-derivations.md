# Derivations — Module 8.4: Electroweak Theory & the Higgs
# 推导 — 模块 8.4：电弱理论与希格斯机制

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.4](./module-8.4-electroweak-theory-and-higgs.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.4](./module-8.4-electroweak-theory-and-higgs.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. SU(2)×U(1) Gauge Fields and the Weinberg Angle · SU(2)×U(1) 规范场与温伯格角

**Claim.** The four gauge fields W^{1,2,3}_μ (SU(2)_L) and B_μ (U(1)_Y) mix to form the mass eigenstates W±_μ, Z⁰_μ, A_μ via the Weinberg angle θ_W, with the electric charge satisfying e = g sinθ_W = g' cosθ_W.

**命题。** 四个规范场 W^{1,2,3}_μ（SU(2)_L）和 B_μ（U(1)_Y）通过温伯格角 θ_W 混合形成质量本征态 W±_μ、Z⁰_μ、A_μ，电荷满足 e = g sinθ_W = g' cosθ_W。

**Step 1 — The gauge structure.** The electroweak gauge group is SU(2)_L × U(1)_Y with gauge fields W^a_μ (a = 1,2,3) for SU(2)_L (coupling g) and B_μ for U(1)_Y (coupling g'). The covariant derivative acting on a left-handed doublet L = (ν_L, e_L) with weak hypercharge Y_L = −1/2 is:

**第 1 步 — 规范结构。** 电弱规范群为 SU(2)_L × U(1)_Y，规范场为 SU(2)_L 的 W^a_μ（a = 1,2,3，耦合常数 g）和 U(1)_Y 的 B_μ（耦合常数 g'）。作用于弱超荷 Y_L = −1/2 的左手双重态 L = (ν_L, e_L) 的协变导数为：

  D_μL = (∂_μ − ig(σ^a/2)W^a_μ − ig'Y_LB_μ)L = (∂_μ − ig(σ^a/2)W^a_μ + (ig'/2)B_μ)L.

For right-handed singlets (e.g., e_R with Y = −1): D_μe_R = (∂_μ + ig'B_μ)e_R.

对于右手单态（例如 Y = −1 的 e_R）：D_μe_R = (∂_μ + ig'B_μ)e_R。

**Step 2 — Charged gauge bosons.** The charged vector bosons W± couple to the raising/lowering generators T± = (T^1 ± iT^2)/√2 = (σ^1 ± iσ^2)/(2√2). Explicitly:

**第 2 步 — 带电规范玻色子。** 带电矢量玻色子 W± 耦合于升/降算符 T± = (T^1 ± iT^2)/√2 = (σ^1 ± iσ^2)/(2√2)。显式地：

  gW^a_μT^a = g[(W^1_μσ^1 + W^2_μσ^2)/2 + W^3_μσ^3/2].

Define:

定义：

  W±_μ = (W^1_μ ∓ iW^2_μ)/√2.

Then:

则：

  g(W^1_μT^1 + W^2_μT^2) = (g/√2)[W+_μT+ + W−_μT−],

where T± = (σ^1 ± iσ^2)/2 are the SU(2) raising/lowering operators. These are the physical W boson fields.

其中 T± = (σ^1 ± iσ^2)/2 是 SU(2) 升/降算符。这些是物理 W 玻色子场。

**Step 3 — Neutral gauge boson mixing.** The neutral sector involves W^3_μ and B_μ. Define the rotation:

**第 3 步 — 中性规范玻色子混合。** 中性部分涉及 W^3_μ 和 B_μ。定义旋转：

  Z_μ = W^3_μ cosθ_W − B_μ sinθ_W  (massive Z⁰ boson),
  A_μ = W^3_μ sinθ_W + B_μ cosθ_W  (massless photon).

This is an orthogonal rotation in (W^3, B) space by angle θ_W (the Weinberg/weak mixing angle).

这是在 (W^3, B) 空间中的正交旋转，旋转角为 θ_W（温伯格/弱混合角）。

**Step 4 — Condition on the electric charge.** The electromagnetic coupling to the electron (charge −e) must emerge correctly. The electron's coupling to W^3_μ and B_μ (from the covariant derivative with I^3 = −1/2 for e_L and Y = −1/2 for L):

**第 4 步 — 电荷条件。** 到电子的电磁耦合（电荷 −e）必须正确涌现。电子到 W^3_μ 和 B_μ 的耦合（来自协变导数，e_L 的 I^3 = −1/2，L 的 Y = −1/2）：

  Coupling of e_L to W^3_μ: gI^3 = g·(−1/2) = −g/2   (from the covariant-derivative term gI^3 W^3_μ, with I^3 = −1/2 for e_L).
  Coupling of e_L to B_μ: g'Y = g'·(−1/2) = −g'/2.

In the rotated (A, Z) basis, the photon A_μ = W^3_μsinθ_W + B_μcosθ_W couples to e_L with:

在旋转的 (A, Z) 基中，光子 A_μ = W^3_μsinθ_W + B_μcosθ_W 与 e_L 的耦合为：

  e_L coupling to A_μ = (gI^3)sinθ_W + (g'Y)cosθ_W = −(g/2)sinθ_W − (g'/2)cosθ_W.

Requiring the photon to couple to every field as eQ = e(I^3 + Y) (so that e_L, with Q = −1, has coupling −e), the I^3 and Y pieces must match *separately* (not just their sum for e_L):

要求光子对每个场的耦合为 eQ = e(I^3 + Y)（使得 Q = −1 的 e_L 耦合为 −e），I^3 与 Y 两部分必须*分别*相等（而非仅对 e_L 的和相等）：

  g sinθ_W = e   (coefficient of I^3),    g' cosθ_W = e   (coefficient of Y).

But the electric charge is Q = I^3 + Y, so for e_L: Q = −1/2 + (−1/2) = −1. The photon coupling is:

但电荷为 Q = I^3 + Y，故对 e_L：Q = −1/2 + (−1/2) = −1。光子耦合为：

  e_L–A coupling = (g sinθ_W)I^3 + (g' cosθ_W)Y = e(I^3 + Y) = eQ.

For this to work with Q = I^3 + Y for all particles, we need:

为使此对所有粒子（Q = I^3 + Y）均成立，需要：

  **g sinθ_W = g' cosθ_W = e**.

This is the fundamental relation of the electroweak theory. It determines θ_W: tanθ_W = g'/g. ∎

这是电弱理论的基本关系。它确定了 θ_W：tanθ_W = g'/g。∎

---

## B. Higgs Potential, VEV, and Spontaneous Symmetry Breaking · 希格斯势、VEV 与自发对称性破缺

**Claim.** The Higgs potential V(φ) = −μ²φ†φ + λ(φ†φ)² (with μ² > 0, λ > 0) has a minimum at |φ|² = v²/2 with v = √(μ²/λ), and the vacuum ⟨φ⟩ = (0, v/√2) spontaneously breaks SU(2)_L × U(1)_Y → U(1)_EM.

**命题。** 希格斯势 V(φ) = −μ²φ†φ + λ(φ†φ)²（μ² > 0，λ > 0）的极小值在 |φ|² = v²/2 处，v = √(μ²/λ)，真空 ⟨φ⟩ = (0, v/√2) 将 SU(2)_L × U(1)_Y 自发破缺至 U(1)_EM。

**Step 1 — Minimize the potential.** Writing ρ = φ†φ ≥ 0:

**第 1 步 — 极小化势。** 令 ρ = φ†φ ≥ 0：

  V = −μ²ρ + λρ².

  dV/dρ = −μ² + 2λρ = 0  ⟹  ρ_min = μ²/(2λ).

  d²V/dρ² = 2λ > 0  (minimum, not maximum, since λ > 0).

So the minimum is at φ†φ = μ²/(2λ) = v²/2, where v ≡ √(μ²/λ).

故极小值在 φ†φ = μ²/(2λ) = v²/2 处，其中 v ≡ √(μ²/λ)。

**Step 2 — Degeneracy: the Mexican hat.** The condition φ†φ = v²/2 defines a circle (or higher-dimensional sphere) of degenerate minima. The potential has a U(1)-symmetric "Mexican hat" shape: flat along the orbit of minima, with a curvature upward in the radial direction.

**第 2 步 — 简并性：墨西哥帽。** 条件 φ†φ = v²/2 定义了一个简并极小值的圆（或更高维球面）。势具有 U(1) 对称的"墨西哥帽"形状：沿极小值轨道方向平坦，在径向方向向上弯曲。

**Step 3 — Choosing the vacuum.** By SU(2)_L × U(1)_Y gauge freedom, we can always rotate φ so that:

**第 3 步 — 选择真空。** 利用 SU(2)_L × U(1)_Y 规范自由度，我们总可以将 φ 旋转至：

  ⟨φ⟩ = (0, v/√2),  i.e., ⟨φ⁺⟩ = 0, ⟨φ⁰⟩ = v/√2.

This choice preserves the U(1)_EM symmetry: the generator Q = I^3 + Y acting on ⟨φ⟩ gives Q⟨φ⟩ = (I^3 + Y)⟨φ⟩ = (−1/2 + 1/2)⟨φ⟩ = 0. So the photon remains massless.

这一选择保留了 U(1)_EM 对称性：作用于 ⟨φ⟩ 的生成元 Q = I^3 + Y 给出 Q⟨φ⟩ = (I^3 + Y)⟨φ⟩ = (−1/2 + 1/2)⟨φ⟩ = 0。故光子保持无质量。

The three generators that do NOT annihilate ⟨φ⟩ are T^1, T^2, and (T^3 − Y), corresponding to W^1, W^2, and Z — these become massive.

不湮灭 ⟨φ⟩ 的三个生成元是 T^1、T^2 和 (T^3 − Y)，对应于 W^1、W^2 和 Z——这些获得质量。

**Step 4 — Goldstone boson counting.** The original SU(2)_L × U(1)_Y has 3 + 1 = 4 generators. The residual U(1)_EM has 1 generator. So 4 − 1 = **3 Goldstone bosons** are generated — exactly absorbed as the longitudinal modes of W+, W−, Z⁰. ∎

**第 4 步 — 戈德斯通玻色子计数。** 原始的 SU(2)_L × U(1)_Y 有 3 + 1 = 4 个生成元。剩余 U(1)_EM 有 1 个生成元。故产生 4 − 1 = **3 个戈德斯通玻色子**——正好被吸收为 W+、W−、Z⁰ 的纵向模式。∎

---

## C. Gauge Boson Masses from the Higgs Mechanism · 由希格斯机制获得规范玻色子质量

**Claim.** Inserting φ = (0, (v+h)/√2) into |D_μφ|², one obtains masses m_W = gv/2 and m_Z = √(g²+g'²)v/2 = m_W/cosθ_W, with the photon remaining massless.

**命题。** 将 φ = (0, (v+h)/√2) 代入 |D_μφ|²，得到质量 m_W = gv/2 和 m_Z = √(g²+g'²)v/2 = m_W/cosθ_W，光子保持无质量。

**Step 1 — Expand around the vacuum.** Write the Higgs field as a perturbation around the vacuum, in unitary gauge (Goldstone bosons set to zero):

**第 1 步 — 在真空附近展开。** 在幺正规范（戈德斯通玻色子设为零）中将希格斯场写为真空附近的扰动：

  φ = (0, (v+h)/√2),  where h(x) is the physical Higgs boson field.

**Step 2 — Gauge kinetic term.** Compute D_μφ with D_μ = ∂_μ − ig(σ^a/2)W^a_μ − ig'YB_μ (Y_φ = +1/2 for the Higgs doublet):

**第 2 步 — 规范动能项。** 用 D_μ = ∂_μ − ig(σ^a/2)W^a_μ − ig'YB_μ（希格斯双重态的 Y_φ = +1/2）计算 D_μφ：

  D_μφ = ∂_μφ − ig(σ^a/2)W^a_μφ − (ig'/2)B_μφ.

At zeroth order in h (setting h = 0 to find mass terms, then h enters as interactions):

在 h 的零阶（令 h = 0 找到质量项，h 之后进入相互作用）：

  D_μ⟨φ⟩ = −ig(σ^a/2)W^a_μ(0, v/√2) − (ig'/2)B_μ(0, v/√2).

**Step 3 — Compute σ^a acting on ⟨φ⟩.** Using the Pauli matrices:

**第 3 步 — 计算 σ^a 作用于 ⟨φ⟩。** 利用泡利矩阵：

For the doublet φ = (φ^+, φ^0) = (0, v/√2):

对于双重态 φ = (φ^+, φ^0) = (0, v/√2)：

  σ^1φ = (0,1;1,0)(0; v/√2) = (v/√2; 0),  so (σ^1/2)φ = (v/(2√2); 0),
  σ^2φ = (0,−i;i,0)(0; v/√2) = (−iv/√2; 0),  so (σ^2/2)φ = (−iv/(2√2); 0),
  σ^3φ = (1,0;0,−1)(0; v/√2) = (0; −v/√2),  so (σ^3/2)φ = (0; −v/(2√2)).

Therefore:

因此：

  D_μ⟨φ⟩ = −ig[W^1_μ(v/(2√2); 0) + W^2_μ(−iv/(2√2); 0) + W^3_μ(0; −v/(2√2))] − (ig'/2)B_μ(0; v/√2).

**Step 4 — |D_μφ|² at zeroth order in h.** The mass terms come from |(D_μ⟨φ⟩)|²:

**第 4 步 — |D_μφ|² 的 h 零阶。** 质量项来自 |(D_μ⟨φ⟩)|²：

Introduce the charged W bosons W±_μ = (W^1_μ ∓ iW^2_μ)/√2. Inverting:

引入带电 W 玻色子 W±_μ = (W^1_μ ∓ iW^2_μ)/√2。反解：

  W^1_μ = (W+_μ + W−_μ)/√2,  W^2_μ = i(W+_μ − W−_μ)/√2.

Upper component of D_μ⟨φ⟩:

D_μ⟨φ⟩ 的上分量：

  = −ig/(2√2) · (W^1_μ − iW^2_μ) · v = −ig/(2√2) · √2 W+_μ · v = −igv W+_μ/2.

Lower component:

下分量：

  = −ig(−v/(2√2))W^3_μ − (ig'/2)(v/√2)B_μ = (igv/2√2)W^3_μ − ig'v/(2√2)B_μ
  = (iv/(2√2))(gW^3_μ − g'B_μ).

Magnitude squared:

模的平方：

Compute it term by term. The upper component squared:

逐项计算。上分量的平方：

  |upper|² = (g²v²/4)|W+_μ|² = (g²v²/4)W+_μW−^μ.

This gives a mass term (g²v²/4)W+W−, identifying:

这给出质量项 (g²v²/4)W+W−，从而：

  ℒ_mass ⊃ (g²v²/4)W+_μW−^μ = m²_W W+_μW−^μ  ⟹  **m_W = gv/2**.

The lower component squared:

下分量的平方：

  |lower|² = (v²/8)(gW^3_μ − g'B_μ)².

The combination gW^3_μ − g'B_μ = √(g²+g'²) Z_μ (the Weinberg rotation Z_μ = (gW^3_μ − g'B_μ)/√(g²+g'²)), so |lower|² = (v²/8)(g²+g'²) Z_μZ^μ.

组合 gW^3_μ − g'B_μ = √(g²+g'²) Z_μ（温伯格旋转 Z_μ = (gW^3_μ − g'B_μ)/√(g²+g'²)），故 |lower|² = (v²/8)(g²+g'²) Z_μZ^μ。

  ℒ_mass ⊃ (v²/8)(g²+g'²)Z_μZ^μ = (1/2)m²_Z Z_μZ^μ  ⟹  **m_Z = v√(g²+g'²)/2**.

The orthogonal combination A_μ = (g'W^3_μ + gB_μ)/√(g²+g'²) does NOT appear in |D_μ⟨φ⟩|² → **m_A = 0** (massless photon). ∎

正交组合 A_μ = (g'W^3_μ + gB_μ)/√(g²+g'²) 不出现在 |D_μ⟨φ⟩|² 中 → **m_A = 0**（无质量光子）。∎

**Step 5 — Weinberg angle and mass ratio.** From the definitions:

**第 5 步 — 温伯格角与质量比。** 由定义：

  cosθ_W = g/√(g²+g'²),  sinθ_W = g'/√(g²+g'²).

Therefore:

因此：

  m_Z = v√(g²+g'²)/2 = v·g/(2cosθ_W) = m_W/cosθ_W.

And e = g sinθ_W: At tree level, the **ρ parameter** ρ = m²_W/(m²_Z cos²θ_W) = 1 (exactly), a tree-level prediction of the Standard Model. Experimentally ρ ≈ 1.0004 (the small deviation comes from loop corrections). ∎

而 e = g sinθ_W：在树图阶，**ρ 参数** ρ = m²_W/(m²_Z cos²θ_W) = 1（精确地），这是标准模型的树图预言。实验上 ρ ≈ 1.0004（小偏差来自圈图修正）。∎

---

## D. The Higgs Boson Mass · 希格斯玻色子质量

**Claim.** Expanding φ = (0, (v+h)/√2) and substituting into V(φ) = −μ²φ†φ + λ(φ†φ)², the physical Higgs boson has mass m_h = √(2μ²) = √(2λ)·v.

**命题。** 展开 φ = (0, (v+h)/√2) 并代入 V(φ) = −μ²φ†φ + λ(φ†φ)²，物理希格斯玻色子的质量为 m_h = √(2μ²) = √(2λ)·v。

**Step 1 — Expand V around the minimum.** With φ†φ = (v+h)²/2:

**第 1 步 — 在极小值附近展开 V。** 以 φ†φ = (v+h)²/2：

  V = −μ²(v+h)²/2 + λ(v+h)⁴/4.

Expand (v+h)² = v² + 2vh + h² and (v+h)⁴ = v⁴ + 4v³h + 6v²h² + 4vh³ + h⁴:

展开 (v+h)² = v² + 2vh + h² 和 (v+h)⁴ = v⁴ + 4v³h + 6v²h² + 4vh³ + h⁴：

  V = −(μ²/2)(v² + 2vh + h²) + (λ/4)(v⁴ + 4v³h + 6v²h² + 4vh³ + h⁴).

**Step 2 — Vacuum energy (constant term).** The h-independent part:

**第 2 步 — 真空能（常数项）。** h 无关的部分：

Using v² = μ²/λ:

  V_0 = −μ²v²/2 + λv⁴/4 = −μ⁴/(2λ) + μ⁴/(4λ) = −μ⁴/(4λ) < 0   (the Mexican-hat bottom is below zero).

利用 v² = μ²/λ：V_0 = −μ²v²/2 + λv⁴/4 = −μ⁴/(2λ) + μ⁴/(4λ) = −μ⁴/(4λ) < 0（墨西哥帽底部低于零）。

**Step 3 — Linear term (must vanish at minimum).** The coefficient of h:

**第 3 步 — 线性项（在极小值处必须消失）。** h 的系数：

  V_linear = h(−μ²v + λv³) = hv(−μ² + λv²) = 0,

since v² = μ²/λ. Good — confirms v is the minimum.

因为 v² = μ²/λ。很好——确认 v 是极小值。

**Step 4 — Quadratic term → Higgs mass.** The coefficient of h²/2:

**第 4 步 — 二次项 → 希格斯质量。** h²/2 的系数：

  V_quadratic = (h²/2)(−μ² + 3λv²) = (h²/2)(−μ² + 3μ²) = (h²/2)(2μ²) = μ²h².

The mass is identified from ℒ ⊃ −(1/2)m²_h h²:

质量由 ℒ ⊃ −(1/2)m²_h h² 辨识：

  m²_h = 2μ² = 2λv²  ⟹  **m_h = √(2μ²) = √(2λ)·v**. ∎

**Step 5 — Cubic and quartic terms.** These give the Higgs self-interactions:

**第 5 步 — 三次项和四次项。** 这些给出希格斯自相互作用：

  V ⊃ λvh³ + (λ/4)h⁴.

The trilinear coupling λv = m²_h/(2v) and quartic coupling λ = m²_h/(2v²) are fully determined by m_h and v — a key prediction of the SM Higgs sector, tested at the LHC. ∎

三线耦合 λv = m²_h/(2v) 和四次耦合 λ = m²_h/(2v²) 完全由 m_h 和 v 确定——这是标准模型希格斯部分的关键预言，在大型强子对撞机上接受检验。∎

---

## E. Goldstone Modes Are Eaten · 戈德斯通模式被"吃掉"

**Claim.** The three Goldstone bosons (massless modes from SSB) are absorbed as the longitudinal polarizations of W±, Z⁰ — the degrees of freedom are conserved.

**命题。** 三个戈德斯通玻色子（来自自发对称性破缺的无质量模式）被吸收为 W±、Z⁰ 的纵向极化——自由度守恒。

**Step 1 — General parameterization.** Before fixing unitary gauge, write the four-component Higgs doublet in the most general way:

**第 1 步 — 一般参数化。** 在固定幺正规范之前，以最一般的方式写出四分量希格斯双重态：

  φ(x) = exp(iπ^a(x)σ^a/(2v)) · (0, (v+h(x))/√2).

Here π^a(x) (a = 1,2,3) are the three Goldstone fields (the angular directions in field space), and h(x) is the radial Higgs field.

这里 π^a(x)（a = 1,2,3）是三个戈德斯通场（场空间中的角向方向），h(x) 是径向希格斯场。

**Step 2 — Goldstones as longitudinal modes.** Under a SU(2)_L gauge transformation U(x) = exp(iα^a(x)σ^a/2):

**第 2 步 — 戈德斯通玻色子作为纵向模式。** 在 SU(2)_L 规范变换 U(x) = exp(iα^a(x)σ^a/2) 下：

  φ → Uφ = exp(i(π^a+α^a)σ^a/(2v))·(0, (v+h)/√2).

By choosing α^a(x) = −π^a(x)/v, we can set the Goldstone fields to zero (unitary gauge). In this gauge, φ = (0, (v+h)/√2).

通过选择 α^a(x) = −π^a(x)/v，我们可以将戈德斯通场设为零（幺正规范）。在此规范中，φ = (0, (v+h)/√2)。

**Step 3 — Degree of freedom count.**

**第 3 步 — 自由度计数。**

Before SSB: φ has 4 real degrees of freedom. The 4 gauge bosons (W^1, W^2, W^3, B) each have 2 transverse polarizations → 4 × 2 = 8 degrees of freedom. Total: 4 + 8 = 12.

自发对称性破缺前：φ 有 4 个实自由度。4 个规范玻色子（W^1、W^2、W^3、B）各有 2 个横向极化 → 4 × 2 = 8 个自由度。总计：4 + 8 = 12。

After SSB: W± and Z⁰ each have 3 polarizations (massive: 2 transverse + 1 longitudinal) → 3 × 3 = 9. The photon has 2 transverse. The Higgs h has 1. Total: 9 + 2 + 1 = 12. ∎

自发对称性破缺后：W± 和 Z⁰ 各有 3 个极化（有质量：2 横向 + 1 纵向）→ 3 × 3 = 9。光子有 2 个横向。希格斯 h 有 1 个。总计：9 + 2 + 1 = 12。∎

---

## F. Fermion Masses from Yukawa Couplings · 由汤川耦合获得费米子质量

**Claim.** The Yukawa coupling ℒ_Y = −y_f(ψ̄_Lφψ_R + h.c.) generates a fermion mass m_f = y_fv/√2 after spontaneous symmetry breaking.

**命题。** 汤川耦合 ℒ_Y = −y_f(ψ̄_Lφψ_R + h.c.) 在自发对称性破缺后产生费米子质量 m_f = y_fv/√2。

**Step 1 — The Yukawa term.** For the electron, L = (ν_e, e)_L and R = e_R:

**第 1 步 — 汤川项。** 对于电子，L = (ν_e, e)_L，R = e_R：

  ℒ_Y = −y_e(L̄φe_R + h.c.) = −y_e[(ν̄_L, ē_L)·(0; (v+h)/√2)·e_R + h.c.]
       = −y_e[(v+h)/√2]ē_Le_R + h.c.

**Step 2 — Mass term.** At zeroth order in h (replacing h → 0):

**第 2 步 — 质量项。** 在 h 的零阶（令 h → 0）：

  ℒ_Y ⊃ −y_e v/√2 · ē_Le_R + h.c. = −m_e(ē_Le_R + ē_Re_L) = −m_eēe,

with **m_e = y_ev/√2** (Dirac mass). The Yukawa coupling y_e is a free parameter; m_e is not predicted by the SM.

其中 **m_e = y_ev/√2**（狄拉克质量）。汤川耦合常数 y_e 是自由参数；m_e 不被标准模型预言。

**Step 3 — Higgs coupling to fermions.** The h-dependent part gives:

**第 3 步 — 希格斯对费米子的耦合。** h 依赖部分给出：

  ℒ_Y ⊃ −(y_e/√2)h·ēe = −(m_e/v)h·ēe.

The coupling of the Higgs to each fermion is m_f/v — proportional to mass. This is the key prediction: heavier fermions couple more strongly to the Higgs. For the top quark (m_t ≈ 173 GeV, v ≈ 246 GeV): y_t = m_t√2/v ≈ 1. ∎

希格斯对每种费米子的耦合为 m_f/v——正比于质量。这是关键预言：较重的费米子与希格斯的耦合更强。对于顶夸克（m_t ≈ 173 GeV，v ≈ 246 GeV）：y_t = m_t√2/v ≈ 1。∎

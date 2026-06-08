# Derivations — Module 8.5: The Standard Model & Beyond
# 推导 — 模块 8.5：标准模型及其超越

> Companion to [Module 8.5](./module-8.5-standard-model-and-beyond.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.5](./module-8.5-standard-model-and-beyond.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Seesaw Mechanism for Neutrino Masses · 中微子质量的跷跷板机制

**Claim.** Adding a right-handed neutrino N_R with Majorana mass M ≫ v to the Standard Model generates light neutrino masses m_ν ≈ m_D²/M (type-I seesaw), where m_D = y_ν v/√2 is the Dirac mass from the Yukawa coupling.

**命题。** 在标准模型中添加具有马约拉纳质量 M ≫ v 的右手中微子 N_R，产生轻中微子质量 m_ν ≈ m_D²/M（I 型跷跷板），其中 m_D = y_ν v/√2 是来自汤川耦合的狄拉克质量。

**Step 1 — The neutrino mass Lagrangian.** After electroweak symmetry breaking, the most general neutrino mass terms are:

**第 1 步 — 中微子质量拉格朗日量。** 电弱对称性破缺后，最一般的中微子质量项为：

  ℒ_ν mass = −m_D ν̄_L N_R − (M/2) N̄^c_R N_R + h.c.,

where ν_L is the left-handed neutrino (Standard Model field), N_R is the right-handed neutrino (SM singlet), m_D is the Dirac mass (from Yukawa coupling y_ν after SSB: m_D = y_ν⟨φ⟩ = y_νv/√2), and M is the Majorana mass of N_R (not protected by any SM symmetry, so M can be very large). N^c_R = C(N̄_R)^T is the charge conjugate.

其中 ν_L 是左手中微子（标准模型场），N_R 是右手中微子（SM 单态），m_D 是狄拉克质量（来自自发对称性破缺后的汤川耦合 y_ν：m_D = y_νv/√2），M 是 N_R 的马约拉纳质量（不受任何 SM 对称性保护，故 M 可以很大）。N^c_R = C(N̄_R)^T 是电荷共轭。

**Step 2 — Matrix form.** In the basis Ψ = (ν_L, N^c_R)^T, the mass Lagrangian takes the form:

**第 2 步 — 矩阵形式。** 在基底 Ψ = (ν_L, N^c_R)^T 中，质量拉格朗日量取形式：

  ℒ_mass = −(1/2)Ψ^T C M_ν Ψ + h.c.,

where the **mass matrix** is:

其中**质量矩阵**为：

  M_ν = ( 0   m_D )
        ( m_D   M  ).

The zero in the (1,1) position is because ν_L has no Majorana mass (it would break SU(2)_L × U(1)_Y). The off-diagonal m_D connects the left and right sectors.

(1,1) 位置的零是因为 ν_L 没有马约拉纳质量（它会破坏 SU(2)_L × U(1)_Y）。非对角元 m_D 连接左手和右手部分。

**Step 3 — Diagonalize the mass matrix.** The eigenvalues of M_ν are found from det(M_ν − λI) = 0:

**第 3 步 — 对角化质量矩阵。** M_ν 的本征值由 det(M_ν − λI) = 0 求得：

  det(−λ     m_D  ) = −λ(M − λ) − m_D² = λ² − Mλ − m_D² = 0.
     (m_D   M − λ)

Using the quadratic formula:

利用求根公式：

  λ = [M ± √(M² + 4m_D²)] / 2.

**Step 4 — Approximate in the seesaw limit M ≫ m_D.** Factor out M from the square root:

**第 4 步 — 在跷跷板极限 M ≫ m_D 下近似。** 从平方根中提出 M：

  √(M² + 4m_D²) = M√(1 + 4m_D²/M²) ≈ M(1 + 2m_D²/M²) = M + 2m_D²/M.

The two eigenvalues are:

两个本征值为：

  λ₊ = [M + M + 2m_D²/M]/2 = M + m_D²/M ≈ M  (heavy neutrino, mass ≈ M),
  λ₋ = [M − M − 2m_D²/M]/2 = −m_D²/M  (light neutrino, |mass| = m_D²/M).

The physical masses are the absolute values:

物理质量为绝对值：

  m_heavy ≈ M,  **m_light ≈ m_D²/M**.

**Step 5 — Physical interpretation.** The light eigenvalue m_ν = m_D²/M has the "seesaw" property: as M increases, m_ν decreases. For m_D ∼ y_ν · 174 GeV (electroweak scale) and m_ν ∼ 0.05 eV (atmospheric neutrino oscillations):

**第 5 步 — 物理诠释。** 轻本征值 m_ν = m_D²/M 具有"跷跷板"特性：随着 M 增大，m_ν 减小。对于 m_D ∼ y_ν · 174 GeV（电弱尺度）和 m_ν ∼ 0.05 eV（大气中微子振荡）：

  M ≈ m_D²/m_ν ∼ (y_ν · 174 GeV)² / (0.05 eV).

For y_ν ∼ 1 (top-quark-scale Yukawa):

对于 y_ν ∼ 1（顶夸克尺度汤川耦合）：

  M ∼ (174 GeV)² / (0.05 × 10⁻⁹ GeV) ∼ 3 × 10²¹ GeV / 5 × 10⁻¹¹ ∼ 6 × 10¹⁴ GeV ≈ 10¹⁴ GeV.

For y_ν ∼ m_e/v ∼ 2 × 10⁻⁶ (electron-scale): M ∼ 10³ GeV (TeV scale).

对于 y_ν ∼ m_e/v ∼ 2 × 10⁻⁶（电子尺度）：M ∼ 10³ GeV（TeV 尺度）。

The "natural" choice is y_ν ∼ O(1), placing M near the GUT scale ∼ 10¹⁴–10¹⁵ GeV — a remarkable hint of unification! ∎

"自然"选择是 y_ν ∼ O(1)，将 M 置于大统一理论尺度 ∼ 10¹⁴–10¹⁵ GeV 附近——这是统一的绝妙暗示！∎

---

## B. Two-Flavor Neutrino Oscillation Probability · 两味中微子振荡概率

**Claim.** For two neutrino flavors ν_e and ν_μ with a mixing angle θ and mass-squared difference Δm² = m²₂ − m²₁, the oscillation probability is:

**命题。** 对于具有混合角 θ 和质量平方差 Δm² = m²₂ − m²₁ 的两味中微子 ν_e 和 ν_μ，振荡概率为：

  P(ν_e → ν_μ; L) = sin²(2θ) · sin²(Δm²L / 4E).

**Step 1 — Mass and flavor eigenstates.** The flavor eigenstates (ν_e, ν_μ) produced by weak interactions are related to mass eigenstates (ν₁, ν₂) via the mixing matrix:

**第 1 步 — 质量本征态与味本征态。** 弱相互作用产生的味本征态（ν_e, ν_μ）通过混合矩阵与质量本征态（ν₁, ν₂）相关：

  |ν_e⟩ = cosθ |ν₁⟩ + sinθ |ν₂⟩,
  |ν_μ⟩ = −sinθ |ν₁⟩ + cosθ |ν₂⟩.

Inverted:

反转：

  |ν₁⟩ = cosθ |ν_e⟩ − sinθ |ν_μ⟩,
  |ν₂⟩ = sinθ |ν_e⟩ + cosθ |ν_μ⟩.

**Step 2 — Time evolution of mass eigenstates.** Mass eigenstates evolve with definite energy. For an ultrarelativistic neutrino with momentum p ≈ E:

**第 2 步 — 质量本征态的时间演化。** 质量本征态以确定能量演化。对于动量 p ≈ E 的超相对论中微子：

  E_i = √(p² + m²_i) ≈ p + m²_i/(2p) ≈ E + m²_i/(2E)  (for m_i ≪ E).

The state at time t (and distance L = ct ≈ t in natural units):

在时间 t（距离 L = ct ≈ t，自然单位）时的态：

  |ν_i(t)⟩ = e^{−iE_it} |ν_i⟩ ≈ e^{−iEt} e^{−im²_i L/(2E)} |ν_i⟩.

The overall phase e^{−iEt} is common to both and drops out of probabilities.

总体相位 e^{−iEt} 对两者相同，在概率中消去。

**Step 3 — Time-evolved flavor state.** A ν_e produced at L = 0 evolves as:

**第 3 步 — 时间演化的味态。** 在 L = 0 处产生的 ν_e 演化为：

  |ν_e(L)⟩ = cosθ · e^{−im²₁L/(2E)} |ν₁⟩ + sinθ · e^{−im²₂L/(2E)} |ν₂⟩.

Express back in the flavor basis using |ν₁⟩ = cosθ|ν_e⟩ − sinθ|ν_μ⟩ and |ν₂⟩ = sinθ|ν_e⟩ + cosθ|ν_μ⟩:

用 |ν₁⟩ = cosθ|ν_e⟩ − sinθ|ν_μ⟩ 和 |ν₂⟩ = sinθ|ν_e⟩ + cosθ|ν_μ⟩ 变换回味本征态：

  |ν_e(L)⟩ = [cos²θ e^{−iφ₁} + sin²θ e^{−iφ₂}]|ν_e⟩ + sinθcosθ[−e^{−iφ₁} + e^{−iφ₂}]|ν_μ⟩,

where φ_i = m²_i L/(2E).

其中 φ_i = m²_i L/(2E)。

**Step 4 — Transition amplitude.** The amplitude for ν_e → ν_μ is:

**第 4 步 — 跃迁振幅。** ν_e → ν_μ 的振幅为：

  A(ν_e → ν_μ) = ⟨ν_μ|ν_e(L)⟩ = sinθ cosθ(e^{−iφ₂} − e^{−iφ₁}).

**Step 5 — Probability.** The oscillation probability:

**第 5 步 — 概率。** 振荡概率：

  P(ν_e → ν_μ) = |A|² = sin²θcos²θ · |e^{−iφ₂} − e^{−iφ₁}|².

Compute the modulus squared:

计算模的平方：

  |e^{−iφ₂} − e^{−iφ₁}|² = (e^{−iφ₂} − e^{−iφ₁})(e^{+iφ₂} − e^{+iφ₁})
                            = 2 − 2cos(φ₂ − φ₁) = 2 − 2cos(Δφ),

where Δφ = φ₂ − φ₁ = (m²₂ − m²₁)L/(2E) = Δm²L/(2E).

其中 Δφ = φ₂ − φ₁ = (m²₂ − m²₁)L/(2E) = Δm²L/(2E)。

Using the identity 2 − 2cosθ = 4sin²(θ/2):

利用恒等式 2 − 2cosθ = 4sin²(θ/2)：

  |e^{−iφ₂} − e^{−iφ₁}|² = 4sin²(Δm²L/(4E)).

Therefore:

因此：

  P(ν_e → ν_μ) = 4sin²θcos²θ · sin²(Δm²L/(4E)) = **sin²(2θ) · sin²(Δm²L/(4E))**,

using 4sin²θcos²θ = sin²(2θ). ∎

利用 4sin²θcos²θ = sin²(2θ)。∎

**Step 6 — Survival probability.** By probability conservation P(ν_e → ν_e) + P(ν_e → ν_μ) = 1 (no other flavors in 2-flavor case):

**第 6 步 — 存活概率。** 由概率守恒 P(ν_e → ν_e) + P(ν_e → ν_μ) = 1（两味情形无其他味）：

  P(ν_e → ν_e) = 1 − sin²(2θ)sin²(Δm²L/(4E)).

**Step 7 — Oscillation length.** The oscillation probability is maximal (fully converted) when sin²(Δm²L/4E) = 1, i.e., Δm²L/(4E) = π/2. The oscillation length is:

**第 7 步 — 振荡长度。** 当 sin²(Δm²L/4E) = 1 时，即 Δm²L/(4E) = π/2，振荡概率最大（完全转换）。振荡长度为：

  L_osc = 4πE/Δm².

In practical units (E in GeV, Δm² in eV², L in km):

在实用单位中（E 单位 GeV，Δm² 单位 eV²，L 单位 km）：

  L_osc = 2.47 km × (E/GeV) / (Δm²/eV²). ∎

---

## C. GUT Coupling Unification Logic · 大统一理论耦合统一的逻辑

**Claim.** The three gauge couplings g₃ (SU(3)), g₂ (SU(2)), g₁ (U(1)) run logarithmically with energy scale μ according to:

**命题。** 三个规范耦合常数 g₃（SU(3)）、g₂（SU(2)）、g₁（U(1)）按如下规律随能量标度 μ 对数跑动：

  d(1/α_i)/d(ln μ) = −b_i/(2π),

and if SM particle content is extended to a SUSY spectrum, the three α_i meet at a single point near μ_GUT ∼ 10¹⁶ GeV.

若 SM 粒子内容扩展到超对称谱，三个 α_i 在 μ_GUT ∼ 10¹⁶ GeV 附近汇聚于一点。

**Step 1 — General RGE for gauge couplings.** The one-loop β function for a gauge theory with coupling constant g_i is:

**第 1 步 — 规范耦合常数的一般重整化群方程。** 耦合常数为 g_i 的规范理论的单圈 β 函数为：

  μ dg_i/dμ = −b_i g_i³/(16π²),

or equivalently, for α_i = g_i²/(4π):

或等价地，对于 α_i = g_i²/(4π)：

  μ d(1/α_i)/dμ = b_i/(2π).

**Step 2 — The b_i coefficients for the SM.** For the gauge group G_i with n_s complex scalars and n_f Weyl fermions in representations R_s, R_f:

**第 2 步 — SM 的 b_i 系数。** 对于规范群 G_i，有 n_s 个复标量和 n_f 个外尔费米子分别处于表示 R_s、R_f：

  b_i = −(11/3)C₂(G) + (2/3)Σ_f T(R_f) + (1/3)Σ_s T(R_s).

For the Standard Model:

对于标准模型：

  b₃ (SU(3)): gauge + ghost contribution −(11/3)C_A = −11 (with C_A = 3); quark contribution +(4/3)T_F n_f = +(2/3)n_f (with T_F = 1/2 per Dirac flavor). For n_f = 6 active flavors:

  b₃ = −11 + (2/3)·n_f = −11 + (2/3)(6) = −11 + 4 = −7.

  b₃ (SU(3))：规范 + 鬼粒子贡献 −(11/3)C_A = −11（C_A = 3）；夸克贡献 +(4/3)T_F n_f = +(2/3)n_f（每个狄拉克味 T_F = 1/2）。对于 n_f = 6 个活跃味：b₃ = −11 + (2/3)(6) = −11 + 4 = −7。

The standard SM one-loop coefficients (normalized so that b_i > 0 means asymptotic freedom):

标准 SM 单圈系数（归一化使得 b_i > 0 意味着渐近自由）：

  b₃ = −7,  b₂ = −19/6,  b₁ = +41/10  (SM, n_f = 6, one Higgs doublet).

(Using the convention μ d(g²/4π)/d(lnμ) = −b_i(g²/4π)²/2π.)

The SU(3) coupling is asymptotically free (b₃ < 0 in some conventions); SU(2) and U(1) have different signs.

**Step 3 — Integrate the RGE.** From μ₀ (low energy, with measured values) to μ (high energy):

**第 3 步 — 积分重整化群方程。** 从 μ₀（低能，具有测量值）到 μ（高能）：

  1/α_i(μ) = 1/α_i(μ₀) + (b_i/2π)ln(μ/μ₀).

The three lines in 1/α_i vs. ln μ space have slopes b_i/2π. With SM values at μ₀ = m_Z:

在 1/α_i 对 ln μ 的空间中，三条直线的斜率为 b_i/2π。以 μ₀ = m_Z 处的 SM 值：

  α₁(m_Z)⁻¹ ≈ 59.0,  α₂(m_Z)⁻¹ ≈ 29.6,  α₃(m_Z)⁻¹ ≈ 8.5.

**Step 4 — SM does not unify; SUSY does.** With SM particle content (b₁,b₂,b₃) the three lines do NOT pass through a common point — they form a triangle. With a complete SUSY spectrum (each SM particle has a superpartner), the β-function coefficients shift:

**第 4 步 — SM 不统一；超对称统一。** 以 SM 粒子内容（b₁,b₂,b₃）的三条直线不通过公共点——它们形成三角形。以完整的超对称谱（每个 SM 粒子有一个超伴子），β 函数系数改变为：

  b₃ = −3,  b₂ = +1,  b₁ = +33/5  (MSSM).

With these coefficients, the three lines do meet at:

以这些系数，三条直线确实在以下处相交：

  μ_GUT ≈ 2 × 10¹⁶ GeV,  α_GUT ≈ 1/25.

This near-perfect unification (at the ∼ few-percent level in 1/α_i) is one of the strongest quantitative hints for supersymmetry and grand unification. ∎

这种近乎完美的统一（在 1/α_i 的约几个百分点的水平）是超对称和大统一理论最强的定量暗示之一。∎

---

## D. CP Violation and the CKM Matrix · CP 破坏与 CKM 矩阵

**Claim.** The CKM (Cabibbo–Kobayashi–Maskawa) matrix V relating weak-eigenstate quarks (d', s', b') to mass eigenstates (d, s, b) is a 3 × 3 unitary matrix. For N generations, the minimum number of irreducible phases is (N−1)(N−2)/2 = 1 for N = 3 — one phase δ that generates CP violation.

**命题。** CKM（卡比博–小林–益川）矩阵 V 将弱本征态夸克（d', s', b'）与质量本征态（d, s, b）相关联，是一个 3 × 3 酉矩阵。对于 N 代，不可约相位的最小数目为 (N−1)(N−2)/2，N = 3 时为 1——一个产生 CP 破坏的相位 δ。

**Step 1 — Parameter counting.** A general N × N unitary matrix U has N² real parameters: N² = N(N−1)/2 angles + N(N+1)/2 phases.

**第 1 步 — 参数计数。** 一般的 N × N 酉矩阵 U 有 N² 个实参数：N² = N(N−1)/2 个角 + N(N+1)/2 个相位。

Not all phases are physical: we can absorb 2N − 1 phases by rephasing the 2N quark fields (one overall phase is common and cancels). So physical phases = N(N+1)/2 − (2N−1) = (N−1)(N−2)/2.

并非所有相位都是物理的：通过对 2N 个夸克场重新定义相位可以吸收 2N − 1 个相位（一个总体相位是公共的并消去）。故物理相位数 = N(N+1)/2 − (2N−1) = (N−1)(N−2)/2。

For N = 3: angles = 3, physical phases = 1. This single phase δ is the source of all CP violation in quark mixing within the Standard Model. For N = 2 (two generations, Cabibbo): phases = 0 → no CP violation (historically realized only one generation mixing was insufficient to explain CP violation). ∎

对于 N = 3：角 = 3，物理相位 = 1。这个单一相位 δ 是标准模型中夸克混合中所有 CP 破坏的来源。对于 N = 2（两代，卡比博）：相位 = 0 → 无 CP 破坏（历史上认识到仅一代混合不足以解释 CP 破坏）。∎

**Step 2 — Standard parameterization.** The standard (PDG) parameterization uses three angles θ₁₂, θ₁₃, θ₂₃ and one phase δ₁₃:

**第 2 步 — 标准参数化。** 标准（PDG）参数化使用三个角 θ₁₂、θ₁₃、θ₂₃ 和一个相位 δ₁₃：

  V_CKM = (c₁₂c₁₃          s₁₂c₁₃          s₁₃e^{−iδ})
           (−s₁₂c₂₃−c₁₂s₂₃s₁₃e^{iδ}   c₁₂c₂₃−s₁₂s₂₃s₁₃e^{iδ}   s₂₃c₁₃  )
           (s₁₂s₂₃−c₁₂c₂₃s₁₃e^{iδ}   −c₁₂s₂₃−s₁₂c₂₃s₁₃e^{iδ}   c₂₃c₁₃  ),

where c_{ij} = cosθ_{ij}, s_{ij} = sinθ_{ij}. The phase δ ≠ 0, π is the source of CP violation; it enters because V ≠ V*. ∎

其中 c_{ij} = cosθ_{ij}，s_{ij} = sinθ_{ij}。相位 δ ≠ 0, π 是 CP 破坏的来源；它的出现是因为 V ≠ V*。∎

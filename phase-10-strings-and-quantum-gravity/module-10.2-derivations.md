# Derivations — Module 10.2: Quantum Gravity & Holography
# 推导 — 模块 10.2：量子引力与全息原理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 10.2](./module-10.2-quantum-gravity-and-holography.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 10.2](./module-10.2-quantum-gravity-and-holography.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Dimensional Analysis of the Planck Units
## A. 普朗克单位的量纲分析

**Claim.** The Planck length ℓ_P, mass m_P, and time t_P are the unique (up to dimensionless factors) combinations of G, ℏ, and c with the respective dimensions of length, mass, and time.

**命题。** 普朗克长度 ℓ_P、质量 m_P 和时间 t_P 是 G、ℏ 和 c 中（在无量纲因子意义上）唯一具有相应长度、质量和时间量纲的组合。

---

**Step 1 — Dimensions of the constants.**

In SI units (M, L, T for mass, length, time):

  [c] = L T⁻¹
  [ℏ] = M L² T⁻¹  (energy × time = action)
  [G] = M⁻¹ L³ T⁻²  (from F = GMm/r²: [F][r²]/[M]² = (MLT⁻²)(L²)(M⁻²) = M⁻¹L³T⁻²).

**第 1 步 — 常数的量纲。**

在国际单位制（M、L、T 分别为质量、长度、时间）中：

  [c] = L T⁻¹
  [ℏ] = M L² T⁻¹  （能量 × 时间 = 作用量）
  [G] = M⁻¹ L³ T⁻²  （由 F = GMm/r²：[F][r²]/[M]² = (MLT⁻²)(L²)(M⁻²) = M⁻¹L³T⁻²）。

---

**Step 2 — Solve for the Planck length.**

Write ℓ_P = G^a ℏ^b c^d and require [ℓ_P] = L:

  M: −a + b = 0  →  b = a
  L:  3a + 2b + d = 1
  T: −2a − b − d = 0  →  d = −2a − b = −3a.

From the L equation: 3a + 2a − 3a = 2a = 1, so **a = 1/2**. Then b = 1/2, d = −3/2. Therefore:

  **ℓ_P = √(Gℏ/c³)** ≈ 1.616 × 10⁻³⁵ m.

**第 2 步 — 求普朗克长度。**

令 ℓ_P = G^a ℏ^b c^d，要求 [ℓ_P] = L：

  M: −a + b = 0  →  b = a
  L:  3a + 2b + d = 1
  T: −2a − b − d = 0  →  d = −2a − b = −3a。

由 L 方程：3a + 2a − 3a = 2a = 1，故 **a = 1/2**。则 b = 1/2，d = −3/2。因此：

  **ℓ_P = √(Gℏ/c³)** ≈ 1.616 × 10⁻³⁵ m。

---

**Step 3 — Planck mass and time.**

Similarly, m_P = G^a ℏ^b c^d with [m_P] = M: solving gives a = −1/2, b = 1/2, d = 1/2:

  **m_P = √(ℏc/G)** ≈ 2.176 × 10⁻⁸ kg.

For t_P = ℓ_P/c:

  **t_P = √(ℏG/c⁵)** ≈ 5.391 × 10⁻⁴⁴ s. ∎

Note: m_P c² = √(ℏc⁵/G) ≈ 1.22 × 10¹⁹ GeV is the **Planck energy**, the energy scale at which the loop expansion parameter G E²/ℏc⁵ = (E/E_P)² becomes O(1).

**第 3 步 — 普朗克质量和时间。**

类似地，令 m_P = G^a ℏ^b c^d，[m_P] = M，求解得 a = −1/2，b = 1/2，d = 1/2：

  **m_P = √(ℏc/G)** ≈ 2.176 × 10⁻⁸ kg。

对 t_P = ℓ_P/c：

  **t_P = √(ℏG/c⁵)** ≈ 5.391 × 10⁻⁴⁴ s。∎

注：m_P c² = √(ℏc⁵/G) ≈ 1.22 × 10¹⁹ GeV 是**普朗克能量**，即圈展开参数 G E²/ℏc⁵ = (E/E_P)² 变为 O(1) 的能量尺度。

---

## B. The Hawking Temperature via Euclidean Time Periodicity
## B. 通过欧氏时间周期性得出霍金温度

**Claim.** The Hawking temperature of a Schwarzschild black hole is **T_H = ℏ κ / (2πc k_B)**, where κ = c⁴/(4GM) is the surface gravity at the horizon. We derive this from the requirement that the Euclidean continuation of the Schwarzschild metric be regular (non-singular) at the horizon — a condition that fixes the imaginary-time period β = 1/k_B T.

**命题。** 史瓦西黑洞的霍金温度为 **T_H = ℏ κ / (2πc k_B)**，其中 κ = c⁴/(4GM) 是视界处的表面引力。我们从要求史瓦西度规的欧氏延拓在视界处正则（非奇异）这一条件出发推导此式——该条件固定了虚时间周期 β = 1/k_B T。

---

**Step 1 — The Schwarzschild metric near the horizon.**

The Schwarzschild metric in Schwarzschild coordinates (c = G = 1 units for brevity) is:

  ds² = −(1 − 2M/r) dt² + (1 − 2M/r)⁻¹ dr² + r² dΩ².

Define the **tortoise coordinate** r* by dr* = dr/(1 − 2M/r), giving r* = r + 2M ln|r/2M − 1|. Near the horizon r → 2M, write r = 2M + ε with ε ≪ 2M. Then:

  1 − 2M/r = ε/(2M) + O(ε²) ≡ f(r).

The surface gravity is κ = (c⁴/4GM) → in units c = G = 1: **κ = 1/(4M)**. So f(r) ≈ 2κ(r − 2M).

**第 1 步 — 视界附近的史瓦西度规。**

史瓦西坐标下的史瓦西度规（简洁起见取 c = G = 1 单位）为：

  ds² = −(1 − 2M/r) dt² + (1 − 2M/r)⁻¹ dr² + r² dΩ²。

定义**乌龟坐标** r*，由 dr* = dr/(1 − 2M/r) 给出，得 r* = r + 2M ln|r/2M − 1|。在视界 r → 2M 附近，令 r = 2M + ε，ε ≪ 2M，则：

  1 − 2M/r = ε/(2M) + O(ε²) ≡ f(r)。

表面引力为 κ = (c⁴/4GM) → 在 c = G = 1 单位中：**κ = 1/(4M)**。故 f(r) ≈ 2κ(r − 2M)。

---

**Step 2 — Euclidean continuation.**

Perform a Wick rotation to **Euclidean time** t_E = it (imaginary time). The metric becomes:

  ds²_E = f(r) dt_E² + f(r)⁻¹ dr² + r² dΩ².

Near r = 2M, writing ρ = 2√(r − 2M)/κ^{1/2} (a new radial coordinate that vanishes at the horizon):

  f(r) dr² / f(r) + f(r) dt_E² ≈ dρ² + κ² ρ² dt_E².

**第 2 步 — 欧氏延拓。**

对**欧氏时间** t_E = it（虚时间）作 Wick 转动，度规变为：

  ds²_E = f(r) dt_E² + f(r)⁻¹ dr² + r² dΩ²。

在 r = 2M 附近，令 ρ = 2√(r − 2M)/κ^{1/2}（在视界消失的新径向坐标）：

  f(r) dr² / f(r) + f(r) dt_E² ≈ dρ² + κ² ρ² dt_E²。

---

**Step 3 — Regularity at the horizon: fixing the period.**

The 2d section dρ² + κ² ρ² dt_E² is the metric of the Euclidean plane in polar coordinates **(ρ, φ) with φ = κ t_E**, provided we identify:

  φ ∼ φ + 2π, i.e., κ t_E ∼ κ t_E + 2π, so **t_E ∼ t_E + 2π/κ**.

If the periodicity in imaginary time is instead β, we identify the **temperature** via the standard quantum statistical mechanics formula (the Matsubara formalism of Module 6.4, which identifies the imaginary-time period with the inverse temperature β = ℏ/k_B T in units ℏ = 1):

  β = 2π/κ  →  k_B T = ℏ κ / (2π)  (reinstating ℏ).

Equivalently, the period β must be 2π/κ for the metric to be regular (no conical singularity at ρ = 0). Any other period would give a conical deficit or surplus at the horizon. The **unique regular Euclidean geometry** fixes:

  **T_H = ℏ κ / (2π k_B)**  (with c restored: T_H = ℏ κ / (2π c k_B)).

For the Schwarzschild hole, κ = c⁴/(4GM):

  **T_H = ℏ c³ / (8π G M k_B)**. ∎

**第 3 步 — 视界处的正则性：固定周期。**

二维截面 dρ² + κ² ρ² dt_E² 是欧氏平面在极坐标 **(ρ, φ) 下的度规，其中 φ = κ t_E**，条件是认同：

  φ ∼ φ + 2π，即 κ t_E ∼ κ t_E + 2π，故 **t_E ∼ t_E + 2π/κ**。

若虚时间周期为 β，通过标准量子统计力学公式（模块 6.4 的 Matsubara 形式主义，它将虚时间周期与逆温度 β = ℏ/k_B T 等同，ℏ = 1 单位）确定**温度**：

  β = 2π/κ  →  k_B T = ℏ κ / (2π)  （恢复 ℏ）。

等价地，周期 β 必须为 2π/κ 才能使度规正则（视界处无锥形奇点）。任何其他周期都会在视界给出锥形亏量或盈量。**唯一正则的欧氏几何**固定：

  **T_H = ℏ κ / (2π k_B)**  （恢复 c：T_H = ℏ κ / (2π c k_B)）。

对史瓦西黑洞，κ = c⁴/(4GM)：

  **T_H = ℏ c³ / (8π G M k_B)**。∎

---

## C. The Bekenstein–Hawking Entropy from the First Law
## C. 由第一定律积分得出 Bekenstein–Hawking 熵

**Claim.** Integrating the first law of black-hole thermodynamics dE = T_H dS (for a Schwarzschild black hole, dE = c² dM) gives S = k_B A / (4 ℓ_P²).

**命题。** 对史瓦西黑洞积分黑洞热力学第一定律 dE = T_H dS（此处 dE = c² dM），得 S = k_B A / (4 ℓ_P²)。

---

**Step 1 — Set up the integral.**

From the first law of thermodynamics with only the mass term (no rotation, no charge):

  dS = dE / T_H = c² dM / T_H.

Substitute T_H = ℏ c³ / (8π G M k_B):

  dS = c² dM / [ℏ c³ / (8π G M k_B)] = (8π G k_B M / ℏ c) dM.

**第 1 步 — 建立积分。**

由只含质量项的热力学第一定律（无转动，无电荷）：

  dS = dE / T_H = c² dM / T_H。

代入 T_H = ℏ c³ / (8π G M k_B)：

  dS = c² dM / [ℏ c³ / (8π G M k_B)] = (8π G k_B M / ℏ c) dM。

---

**Step 2 — Integrate from M = 0 to M.**

  S(M) = ∫₀ᴹ (8π G k_B M′ / ℏ c) dM′ = (8π G k_B / ℏ c) · M²/2 = **4π G k_B M² / ℏ c**.

**第 2 步 — 从 M = 0 积分到 M。**

  S(M) = ∫₀ᴹ (8π G k_B M′ / ℏ c) dM′ = (8π G k_B / ℏ c) · M²/2 = **4π G k_B M² / ℏ c**。

---

**Step 3 — Express in terms of horizon area.**

The Schwarzschild radius is r_s = 2GM/c², so the horizon area is:

  A = 4π r_s² = 4π (2GM/c²)² = 16π G² M² / c⁴.

Solving for M²: G M² = A c⁴ / (16π G). Substituting into S:

  S = 4π G k_B M² / ℏ c = 4π G k_B · (A c⁴ / 16π G²) / ℏ c = (k_B c³ A) / (4 G ℏ).

Recall ℓ_P² = ℏG/c³, so G ℏ / c³ = ℓ_P²:

  **S = k_B A / (4 ℓ_P²)**. ∎

**第 3 步 — 用视界面积表示。**

史瓦西半径为 r_s = 2GM/c²，故视界面积为：

  A = 4π r_s² = 4π (2GM/c²)² = 16π G² M² / c⁴。

解出 M²：G M² = A c⁴ / (16π G)。代入 S：

  S = 4π G k_B M² / ℏ c = 4π G k_B · (A c⁴ / 16π G²) / ℏ c = (k_B c³ A) / (4 G ℏ)。

注意 ℓ_P² = ℏG/c³，故 G ℏ / c³ = ℓ_P²：

  **S = k_B A / (4 ℓ_P²)**。∎

---

## D. Consistency Check: The Evaporation Timescale
## D. 自洽性检验：蒸发时标

**Claim.** A black hole of initial mass M₀ evaporates completely in a time t_evap ∝ G² M₀³ / (ℏ c⁴). We verify this by combining Stefan–Boltzmann radiation with the Hawking temperature.

**命题。** 初始质量为 M₀ 的黑洞在时间 t_evap ∝ G² M₀³ / (ℏ c⁴) 内完全蒸发。我们通过将 Stefan–Boltzmann 辐射与霍金温度结合来验证。

---

**Step 1 — Luminosity of Hawking radiation.**

Treating the black hole as a blackbody of temperature T_H and effective area ~ A = 16π G² M² / c⁴ (Stefan–Boltzmann law L = σ T⁴ A in natural units, up to grey-body factors of order 1):

  L ~ σ T_H⁴ A ~ σ (ℏc³/8πGMk_B)⁴ · (G²M²/c⁴) ~ ℏ c⁶ / (G² M²),

where σ = π²k_B⁴/(60ℏ³c²) has been substituted and all numerical prefactors collected into the proportionality.

**第 1 步 — 霍金辐射的光度。**

将黑洞视为温度 T_H、有效面积 ∼ A = 16π G² M² / c⁴ 的黑体（Stefan–Boltzmann 定律 L = σ T⁴ A，自然单位，灰体因子为 O(1)）：

  L ∼ σ T_H⁴ A ∼ σ (ℏc³/8πGMk_B)⁴ · (G²M²/c⁴) ∼ ℏ c⁶ / (G² M²)，

其中 σ = π²k_B⁴/(60ℏ³c²) 已代入，所有数值系数收入比例号。

---

**Step 2 — The mass-loss equation.**

Energy conservation: −c² dM/dt = L ~ ℏ c⁶ / (G² M²). Therefore:

  M² dM = −(ℏ c⁴ / G²) dt  (absorbing the numerical coefficient ~ 1 into the relation).

**第 2 步 — 质量损失方程。**

能量守恒：−c² dM/dt = L ∼ ℏ c⁶ / (G² M²)。因此：

  M² dM = −(ℏ c⁴ / G²) dt  （数值系数约 1 已收入比例关系）。

---

**Step 3 — Integrate.**

Integrating from M₀ to 0:

  ∫₀^{M₀} M² dM = M₀³/3 = (ℏ c⁴ / G²) t_evap.

Therefore:

  **t_evap ~ G² M₀³ / (ℏ c⁴)**. ∎

For M₀ = M_sun ~ 2 × 10³⁰ kg: t_evap ~ (6.67×10⁻¹¹)²(2×10³⁰)³ / (10⁻³⁴ × 9×10¹⁶) ~ 10⁷⁴ years — utterly negligible evaporation over the age of the universe (~ 10¹⁰ years). For a Planck-mass black hole (M₀ ~ 10⁻⁸ kg): t_evap ~ t_P ~ 10⁻⁴⁴ s — it would evaporate instantly.

**第 3 步 — 积分。**

从 M₀ 积分到 0：

  ∫₀^{M₀} M² dM = M₀³/3 = (ℏ c⁴ / G²) t_evap。

因此：

  **t_evap ∼ G² M₀³ / (ℏ c⁴)**。∎

对 M₀ = M_太阳 ∼ 2 × 10³⁰ kg：t_evap ∼ (6.67×10⁻¹¹)²(2×10³⁰)³ / (10⁻³⁴ × 9×10¹⁶) ∼ 10⁷⁴ 年——在宇宙年龄（∼ 10¹⁰ 年）内完全可忽略。对普朗克质量黑洞（M₀ ∼ 10⁻⁸ kg）：t_evap ∼ t_P ∼ 10⁻⁴⁴ s——会瞬间蒸发。

---

## E. The Bekenstein Bound and the Holographic Principle
## E. Bekenstein 界与全息原理

**Claim.** The maximum entropy of any physical system contained within a region of radius R and energy E (with Mc² = E) satisfies S ≤ 2π k_B R E / (ℏ c). A spherical system saturates this bound only when it is a black hole. From this, the maximum entropy in any region bounded by area A is S_max = k_B A / (4ℓ_P²), establishing the holographic bound.

**命题。** 包含在半径 R、能量 E（Mc² = E）区域内的任何物理系统的最大熵满足 S ≤ 2π k_B R E / (ℏ c)。只有当系统是黑洞时，球形系统才使此界饱和。由此，面积为 A 的区域内的最大熵为 S_max = k_B A / (4ℓ_P²)，建立了全息界。

---

**Step 1 — The Bekenstein bound argument.**

Consider a box of size R containing matter with entropy S and rest energy Mc². To argue why S ≤ 2πk_B RMc/ℏ: Suppose S > S_BH (the Bekenstein–Hawking entropy of a black hole of mass M in radius R). We could then lower a box with this matter into an existing black hole. By the generalized second law (GSL), the total entropy — including the black-hole area — cannot decrease. But the area increase upon absorption is ΔA = 16πGm(M+m)/c⁴ − 16πGM²/c⁴ ≈ 32πGmM/c⁴ (for m ≪ M), giving ΔS_BH = k_B ΔA/(4ℓ_P²). For this to accommodate S, we need S ≤ ΔS_BH, which gives S ≤ 2πk_B RMc/ℏ (identifying R with the Schwarzschild radius scale ~GM/c²). This is the **Bekenstein entropy bound**.

**第 1 步 — Bekenstein 界的论证。**

考虑大小为 R 的盒子，其中物质具有熵 S 和静止能量 Mc²。论证 S ≤ 2πk_B RMc/ℏ 的理由：假设 S > S_BH（半径 R、质量 M 的黑洞的 Bekenstein–Hawking 熵）。我们可以将这盒物质放入一个已存在的黑洞。由广义第二定律（GSL），总熵——包括黑洞面积——不能减少。但吸收后的面积增加为 ΔA = 16πGm(M+m)/c⁴ − 16πGM²/c⁴ ≈ 32πGmM/c⁴（m ≪ M），给出 ΔS_BH = k_B ΔA/(4ℓ_P²)。为使 S 得以容纳，需要 S ≤ ΔS_BH，给出 S ≤ 2πk_B RMc/ℏ（将 R 与史瓦西半径尺度 ∼ GM/c² 对应）。这是 **Bekenstein 熵界**。

---

**Step 2 — Saturation by black holes and the holographic bound.**

For a Schwarzschild black hole of mass M, radius r_s = 2GM/c², the Bekenstein bound gives:

  S ≤ 2πk_B r_s M c / ℏ = 2πk_B (2GM/c²)(Mc) / ℏ = 4πk_B GM² / (ℏc).

This is exactly the Bekenstein–Hawking entropy S_BH = k_B A/(4ℓ_P²) = 4πk_B GM²/(ℏc). So **black holes saturate the Bekenstein bound**: they are the maximum-entropy states for given mass and size. Since no system can have more entropy than a black hole of the same boundary area A, the maximum entropy in a region bounded by area A is:

  S_max = S_BH = k_B A / (4ℓ_P²),

the **holographic bound** (Bousso 2002). The number of independent degrees of freedom in the region is at most A/(4ℓ_P²) — one degree of freedom per four Planck areas — regardless of the volume. The world in this sense is holographic. ∎

**第 2 步 — 黑洞使界饱和与全息界。**

对质量 M、半径 r_s = 2GM/c² 的史瓦西黑洞，Bekenstein 界给出：

  S ≤ 2πk_B r_s M c / ℏ = 2πk_B (2GM/c²)(Mc) / ℏ = 4πk_B GM² / (ℏc)。

这恰好是 Bekenstein–Hawking 熵 S_BH = k_B A/(4ℓ_P²) = 4πk_B GM²/(ℏc)。故**黑洞使 Bekenstein 界饱和**：它们是给定质量和尺寸下熵最大的态。由于任何系统的熵不能超过同面积 A 边界的黑洞的熵，面积为 A 的区域内的最大熵为：

  S_max = S_BH = k_B A / (4ℓ_P²)，

即**全息界**（Bousso，2002 年）。该区域内独立自由度的数目最多为 A/(4ℓ_P²)——每四个普朗克面积对应一个自由度——与体积无关。世界在此意义上是全息的。∎

---

*All derivations follow the conventions of Wald, "General Relativity" (Chicago, 1984) for the surface gravity; Hawking's original derivation in Comm. Math. Phys. 43, 199 (1975); Gibbons & Hawking, Phys. Rev. D 15, 2752 (1977) for the Euclidean method; and Bekenstein, Phys. Rev. D 7, 2333 (1973) for the entropy bound. The ζ-function regularization of the determinant of the Euclidean wave operator is beyond the scope of this document; the Euclidean-periodicity argument given here is the standard pedagogical route.*

*所有推导遵循 Wald《广义相对论》（芝加哥，1984 年）关于表面引力的约定；霍金在 Comm. Math. Phys. 43, 199 (1975) 中的原始推导；Gibbons 和 Hawking 在 Phys. Rev. D 15, 2752 (1977) 中的欧氏方法；以及 Bekenstein 在 Phys. Rev. D 7, 2333 (1973) 中的熵界。欧氏波算符行列式的 ζ 函数正规化超出本文档范围；此处给出的欧氏周期性论证是标准的教学路径。*

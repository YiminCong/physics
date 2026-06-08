# Derivations — Module 8.6: Particle Physics & Cosmology
# 推导 — 模块 8.6：粒子物理与宇宙学

> Companion to [Module 8.6](./module-8.6-particle-physics-and-cosmology.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.6](./module-8.6-particle-physics-and-cosmology.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Boltzmann Equation in an Expanding Universe · 膨胀宇宙中的玻尔兹曼方程

**Claim.** For a massive particle species χ with number density n in a Friedmann–Robertson–Walker (FRW) universe, the Boltzmann equation governing n is:

**命题。** 对于弗里德曼–罗伯逊–沃克（FRW）宇宙中数密度为 n 的大质量粒子种类 χ，支配 n 的玻尔兹曼方程为：

  dn/dt + 3Hn = −⟨σv⟩(n² − n_eq²),

where H is the Hubble rate, ⟨σv⟩ is the thermally averaged annihilation cross-section, and n_eq is the equilibrium number density.

其中 H 为哈勃速率，⟨σv⟩ 为热平均湮灭截面，n_eq 为平衡数密度。

**Step 1 — Conservation law in expanding universe.** Consider a comoving volume V ∝ a³ in an FRW universe. The total particle number N = nV = na³ changes due to annihilation/creation reactions. If χχ̄ ↔ SM SM is the relevant process:

**第 1 步 — 膨胀宇宙中的守恒律。** 考虑 FRW 宇宙中的共动体积 V ∝ a³。总粒子数 N = nV = na³ 由于湮灭/产生反应而改变。若相关过程为 χχ̄ ↔ SM SM：

  d(na³)/dt = a³[dn/dt + 3Hn]  (since ȧ/a = H, so da³/dt = 3a²ȧ = 3Ha³).

**Step 2 — Collision term.** The rate of change of n due to annihilation (n² rate, proportional to the square of the number density) and creation (rate proportional to n_eq²):

**第 2 步 — 碰撞项。** 由于湮灭（n² 速率，正比于数密度的平方）和产生（速率正比于 n_eq²）引起的 n 变化率：

  (dn/dt)|_coll = −⟨σv⟩n² + ⟨σv⟩n_eq².

In detail: The annihilation rate per unit volume is ⟨σv⟩n² (two-body process: Γ = nσv averaged over the thermal distribution). The creation rate is ⟨σv⟩n_eq² (detailed balance: in equilibrium, creation = annihilation).

详细地：单位体积的湮灭速率为 ⟨σv⟩n²（两体过程：Γ = nσv 对热分布取平均）。产生速率为 ⟨σv⟩n_eq²（细致平衡：在平衡状态下，产生 = 湮灭）。

**Step 3 — Full Boltzmann equation.** Combining:

**第 3 步 — 完整的玻尔兹曼方程。** 综合：

  dn/dt + 3Hn = −⟨σv⟩(n² − n_eq²). ∎

---

## B. The Freeze-Out Condition · 冻结条件

**Claim.** A species freezes out when the interaction rate Γ = ⟨σv⟩n drops below the Hubble expansion rate H: Γ ≈ H at T = T_f (freeze-out temperature).

**命题。** 当相互作用速率 Γ = ⟨σv⟩n 降至哈勃膨胀速率 H 以下时，粒子种类冻结：Γ ≈ H 在 T = T_f（冻结温度）时成立。

**Step 1 — Equation for the comoving density.** Define Y = n/s (yield: number density to entropy density ratio), where the entropy density s = (2π²/45)g_*S T³ is conserved during adiabatic expansion (sa³ = const). Then:

**第 1 步 — 共动密度的方程。** 定义 Y = n/s（产额：数密度与熵密度之比），其中熵密度 s = (2π²/45)g_*S T³ 在绝热膨胀期间守恒（sa³ = const）。则：

  dY/dt = −s⟨σv⟩(Y² − Y_eq²).

Since ds/dt = −3Hs (conservation), and n = sY: dn/dt + 3Hn = s(dY/dt).

由于 ds/dt = −3Hs（守恒），且 n = sY：dn/dt + 3Hn = s(dY/dt)。

**Step 2 — Change variable to x = m/T.** Using T ∝ 1/a and H = ȧ/a:

**第 2 步 — 变量变换为 x = m/T。** 利用 T ∝ 1/a 和 H = ȧ/a：

  dY/dx = −(s⟨σv⟩/Hx)(Y² − Y_eq²).

Define the rate ratio Γ/H = s⟨σv⟩/(Hx) at x = x_f.

定义 x = x_f 处的速率比 Γ/H = s⟨σv⟩/(Hx)。

**Step 3 — Two regimes.** 

**第 3 步 — 两个区域。**

- **When Γ/H ≫ 1 (early times, small x):** Reactions are fast; Y tracks Y_eq. The species is in chemical equilibrium.
- **当 Γ/H ≫ 1（早期，小 x）时：** 反应快速；Y 跟踪 Y_eq。粒子种类处于化学平衡。

- **When Γ/H ≪ 1 (late times, large x):** Reactions are negligible; Y freezes at Y_f ≈ Y_eq(x_f).
- **当 Γ/H ≪ 1（晚期，大 x）时：** 反应可忽略；Y 冻结在 Y_f ≈ Y_eq(x_f)。

The **freeze-out condition** is the transition: Γ = H.

**冻结条件**是过渡点：Γ = H。

**Step 4 — Hubble rate in radiation domination.** In the radiation-dominated era:

**第 4 步 — 辐射主导期的哈勃速率。** 在辐射主导时期：

  H = √(8πρ_rad/3M_Pl²) = √(4π³g_*/45) · T²/M_Pl,

where M_Pl ≈ 2.4 × 10¹⁸ GeV is the reduced Planck mass and g_* counts relativistic degrees of freedom.

其中 M_Pl ≈ 2.4 × 10¹⁸ GeV 是约化普朗克质量，g_* 计算相对论性自由度数。

**Step 5 — Equilibrium number density.** For a non-relativistic species (T ≪ m) with g internal degrees of freedom:

**第 5 步 — 平衡数密度。** 对于具有 g 个内部自由度的非相对论性粒子（T ≪ m）：

  n_eq = g(mT/2π)^{3/2} e^{−m/T}.

The exponential suppression (Boltzmann suppression) at T < m means n_eq falls rapidly. The freeze-out occurs at x_f = m/T_f where:

T < m 时的指数抑制（玻尔兹曼抑制）意味着 n_eq 迅速下降。冻结发生在 x_f = m/T_f，其中：

  n_eq ⟨σv⟩ ≈ H  at T = T_f.

For WIMPs with m ∼ 100 GeV, this gives x_f ≈ 20–25 (i.e., T_f ≈ m/20). ∎

对于质量 m ∼ 100 GeV 的 WIMP，这给出 x_f ≈ 20–25（即 T_f ≈ m/20）。∎

---

## C. The WIMP Miracle: Relic Abundance Estimate · WIMP 奇迹：遗迹丰度估算

**Claim.** A thermal WIMP with mass m_χ ∼ 100 GeV and weak-scale cross-section ⟨σv⟩ ∼ 10⁻²⁶ cm³/s naturally produces a relic density Ω_χh² ≈ 0.1 — matching the observed dark matter density.

**命题。** 质量 m_χ ∼ 100 GeV、弱力尺度截面 ⟨σv⟩ ∼ 10⁻²⁶ cm³/s 的热 WIMP 自然地产生遗迹密度 Ω_χh² ≈ 0.1——与观测到的暗物质密度吻合。

**Step 1 — Post-freeze-out Boltzmann equation.** After freeze-out, Y remains approximately constant: Y_∞ ≈ Y_f. To get a more precise answer, integrate the Boltzmann equation. For Y ≫ Y_eq (late times):

**第 1 步 — 冻结后的玻尔兹曼方程。** 冻结后，Y 保持近似不变：Y_∞ ≈ Y_f。为获得更精确的结果，积分玻尔兹曼方程。对于 Y ≫ Y_eq（晚期）：

  dY/dx ≈ −(s⟨σv⟩/Hx)Y².

Integrating from x_f to ∞:

从 x_f 到 ∞ 积分：

  1/Y_∞ − 1/Y_f ≈ ∫_{x_f}^∞ (s⟨σv⟩)/(Hx) dx.

Since Y_f ≫ Y_∞ (most of the depletion happens just after freeze-out), 1/Y_∞ ≈ ∫_{x_f}^∞ (s⟨σv⟩)/(Hx) dx.

由于 Y_f ≫ Y_∞（大部分消耗恰好发生在冻结之后），1/Y_∞ ≈ ∫_{x_f}^∞ (s⟨σv⟩)/(Hx) dx。

**Step 2 — Evaluate the integral.** Using s = (2π²/45)g_*S T³ = (2π²/45)g_*S (m/x)³ and H = π√(g_*/45) · m²/(M_Pl x²):

**第 2 步 — 计算积分。** 利用 s = (2π²/45)g_*S T³ = (2π²/45)g_*S (m/x)³ 和 H = π√(g_*/45) · m²/(M_Pl x²)：

  s/H = [(2π²/45)g_*S(m/x)³] / [π√(g_*/45)m²/(M_Plx²)]
      = (2π/45)g_*S · (m M_Pl) / (√(g_*/45)π · x)
      = (2/π²)√(π/45) · g_*S/√(g_*) · mM_Pl/x.

Substituting:

代入：

  1/Y_∞ ≈ ⟨σv⟩ · (2/π²)√(π/45) · (g_*S/√g_*) · mM_Pl · ∫_{x_f}^∞ x⁻² dx
          = ⟨σv⟩ · (2/π²)√(π/45) · (g_*S/√g_*) · mM_Pl · (1/x_f).

Using g_*S ≈ g_* at freeze-out:

在冻结时利用 g_*S ≈ g_*：

  1/Y_∞ ≈ ⟨σv⟩ · (2/π)√(g_*/45) · mM_Pl/x_f · (numerical factors order 1).

Numerically, with x_f ≈ 20 and √(g_*/45) ≈ 0.26 (for g_* = 86.25 in SM at T ∼ 5 GeV):

数值上，以 x_f ≈ 20 和 √(g_*/45) ≈ 0.26（SM 中 T ∼ 5 GeV 时 g_* = 86.25）：

  Y_∞ ≈ x_f / (⟨σv⟩ · 0.26 · mM_Pl · 2/π) ≈ (3 × 10⁻¹⁰ GeV⁻²)/⟨σv⟩.

**Step 3 — Convert to relic density.** The current number density n_χ = s₀Y_∞ where s₀ = 2891 cm⁻³ is today's entropy density. The energy density:

**第 3 步 — 换算为遗迹密度。** 当前数密度 n_χ = s₀Y_∞，其中 s₀ = 2891 cm⁻³ 是今天的熵密度。能量密度：

  ρ_χ = m_χ n_χ = m_χ s₀ Y_∞.

The relic density parameter (using ρ_crit/h² = 1.054 × 10⁻⁵ GeV cm⁻³):

遗迹密度参数（利用 ρ_crit/h² = 1.054 × 10⁻⁵ GeV cm⁻³）：

  Ω_χh² = ρ_χ h²/ρ_crit = m_χ s₀ Y_∞ h²/ρ_crit.

Substituting the expression for Y_∞:

代入 Y_∞ 的表达式：

  Ω_χh² = m_χ s₀ h²/(ρ_crit) · (3 × 10⁻¹⁰ GeV⁻²)/(⟨σv⟩ m_χ) 

The m_χ cancels (this is the key miracle!):

m_χ 消去（这是关键的奇迹！）：

  Ω_χh² ≈ (3 × 10⁻²⁷ cm³/s) / ⟨σv⟩,

where we converted GeV⁻² to cm³/s (1 GeV⁻² = 0.389 × 10⁻²⁷ cm²; with factors of c): **3 × 10⁻²⁷ cm³/s** ≈ 0.1 pb·c.

其中我们将 GeV⁻² 换算为 cm³/s（1 GeV⁻² = 0.389 × 10⁻²⁷ cm²；乘以 c 的因子）：**3 × 10⁻²⁷ cm³/s** ≈ 0.1 pb·c。

**Step 4 — The WIMP miracle.** For a particle with electroweak-scale interactions: ⟨σv⟩ ∼ α²/m_χ². With α ∼ 0.03 (EW) and m_χ ∼ 100 GeV:

**第 4 步 — WIMP 奇迹。** 对于具有电弱尺度相互作用的粒子：⟨σv⟩ ∼ α²/m_χ²。以 α ∼ 0.03（电弱）和 m_χ ∼ 100 GeV：

  ⟨σv⟩ ∼ (0.03)²/(100 GeV)² = 9 × 10⁻⁴/(10⁴ GeV²) = 9 × 10⁻⁸ GeV⁻² ≈ 3 × 10⁻²⁶ cm³/s.

Therefore:

因此：

  Ω_χh² ≈ (3 × 10⁻²⁷)/(3 × 10⁻²⁶) ≈ **0.1**,

in remarkable agreement with the measured Ω_DM h² ≈ 0.120 from CMB data. No parameter was tuned! This is the WIMP miracle: a particle motivated entirely by the hierarchy problem (not by cosmology) independently predicts the correct dark matter abundance. ∎

与 CMB 数据测量的 Ω_DM h² ≈ 0.120 惊人地吻合。没有任何参数被调节！这就是 WIMP 奇迹：一个完全由等级问题（而非宇宙学）激发的粒子，独立地预言了正确的暗物质丰度。∎

**Step 5 — Why mass cancels.** The cancellation of m_χ from Ω_χh² is physical: heavier WIMPs stay in equilibrium longer (harder to annihilate with lower n), so Y_∞ ∝ 1/m_χ; but ρ_χ = m_χn_χ ∝ m_χ · (1/m_χ) = const. The relic density depends only on ⟨σv⟩, not on m_χ separately. ∎

**第 5 步 — 为何质量消去。** m_χ 从 Ω_χh² 中消去有其物理意义：较重的 WIMP 在平衡中停留更长时间（更低 n 时更难湮灭），故 Y_∞ ∝ 1/m_χ；但 ρ_χ = m_χn_χ ∝ m_χ · (1/m_χ) = const。遗迹密度只取决于 ⟨σv⟩，而不单独取决于 m_χ。∎

---

## D. Sakharov Conditions for Baryogenesis · 重子生成的萨哈罗夫条件

**Claim.** To generate a net baryon asymmetry from an initially symmetric state (n_b = n_b̄), the following three conditions must all hold: (1) baryon number B violation, (2) C and CP violation, (3) departure from thermal equilibrium.

**命题。** 要从初始对称态（n_b = n_b̄）产生净重子不对称性，以下三个条件必须同时满足：(1) 重子数 B 不守恒，(2) C 和 CP 破坏，(3) 偏离热平衡。

**Step 1 — Necessity of B violation.** Obviously, if baryon number is strictly conserved, any process that creates a baryon also creates an antibaryon (or destroys a baryon), keeping n_b − n_b̄ = const. If initially n_b − n_b̄ = 0, it remains zero. B violation is necessary to allow n_b ≠ n_b̄. In the SM, B is violated non-perturbatively via electroweak sphalerons at high temperature T ≳ 100 GeV: the sphaleron rate is Γ_sph ∼ α_W⁵T.

**第 1 步 — B 破坏的必要性。** 显然，若重子数严格守恒，任何产生重子的过程也会产生反重子（或湮灭重子），保持 n_b − n_b̄ = const。若初始时 n_b − n_b̄ = 0，则它保持为零。B 破坏是允许 n_b ≠ n_b̄ 的必要条件。在 SM 中，B 在高温 T ≳ 100 GeV 时通过电弱热子非微扰地破坏：热子速率 Γ_sph ∼ α_W⁵T。

**Step 2 — Necessity of C and CP violation.** Suppose C is conserved. Then the rate of any process Γ(ψ → bX) = Γ(ψ̄ → b̄X̄) (charge conjugation maps particles to antiparticles). Any baryon-creating process has an equally fast antibaryoncreating partner, so no net baryon number is generated. Therefore C must be violated.

**第 2 步 — C 和 CP 破坏的必要性。** 假设 C 守恒。则任何过程的速率 Γ(ψ → bX) = Γ(ψ̄ → b̄X̄)（电荷共轭将粒子映射到反粒子）。任何产生重子的过程都有一个等速产生反重子的过程，故不产生净重子数。因此 C 必须破坏。

Similarly, even if C is violated, if CP is conserved, the rate of ψ_L → bX equals the rate of ψ̄_R → b̄X̄ (CP maps left-handed particles to right-handed antiparticles). The combined rates still balance, yielding no asymmetry. Therefore both C and CP must be violated.

类似地，即使 C 被破坏，若 CP 守恒，则 ψ_L → bX 的速率等于 ψ̄_R → b̄X̄ 的速率（CP 将左手粒子映射到右手反粒子）。合并速率仍然平衡，不产生不对称性。因此 C 和 CP 都必须被破坏。

**Step 3 — Necessity of departure from thermal equilibrium.** In thermal equilibrium, the density matrix ρ = e^{−H/T}/Z is time-reversal invariant (CPT theorem). For any process, Γ(i→f) = Γ(f̄→ī) (CPT). Even with B and CP violation, in equilibrium all forward and reverse rates balance: ⟨B⟩_eq = 0 for any Hamiltonian with CPT invariance (Kobzarev–Okun–Shaposhnikov theorem). Departure from equilibrium (e.g., a first-order phase transition, or the decay of a heavy particle out of equilibrium) allows the B-violating and CP-violating rates to act without the reverse processes restoring equilibrium.

**第 3 步 — 偏离热平衡的必要性。** 在热平衡中，密度矩阵 ρ = e^{−H/T}/Z 在时间反演下不变（CPT 定理）。对于任何过程，Γ(i→f) = Γ(f̄→ī)（CPT）。即使有 B 和 CP 破坏，在平衡中所有正向和逆向速率平衡：对于任何具有 CPT 不变性的哈密顿量，⟨B⟩_eq = 0（Kobzarev–Okun–Shaposhnikov 定理）。偏离平衡（例如一级相变，或重粒子的失平衡衰变）允许 B 破坏和 CP 破坏速率起作用，而不被逆过程恢复平衡。

**Step 4 — SM realization and its shortfall.** The SM satisfies all three conditions in principle:
(1) Sphaleron processes: ΔB = ΔL = ±3 (baryon number violated by sphalerons).
(2) CKM phase δ provides CP violation.
(3) The electroweak phase transition provides non-equilibrium.

**第 4 步 — SM 实现及其不足。** SM 原则上满足所有三个条件：
(1) 热子过程：ΔB = ΔL = ±3（重子数被热子破坏）。
(2) CKM 相位 δ 提供 CP 破坏。
(3) 电弱相变提供非平衡。

However, quantitatively:
- The SM CKM phase is too small: the CP-violating measure J = Im[V_{us}V_{cb}V_{ub}*V_{cs}*] ∼ 3 × 10⁻⁵ is suppressed by small mixing angles.
- The SM electroweak phase transition at m_h ≈ 125 GeV is a smooth crossover (not first-order), so the departure from equilibrium is insufficient.

然而，定量上：
- SM 的 CKM 相位太小：CP 破坏量度 J = Im[V_{us}V_{cb}V_{ub}*V_{cs}*] ∼ 3 × 10⁻⁵ 被小混合角所抑制。
- SM 在 m_h ≈ 125 GeV 处的电弱相变是平滑过渡（而非一级相变），因此偏离平衡不足。

The observed baryon-to-photon ratio η ∼ 6 × 10⁻¹⁰ requires new sources of CP violation and/or a stronger first-order phase transition — physics beyond the SM. ∎

观测到的重子–光子比 η ∼ 6 × 10⁻¹⁰ 需要新的 CP 破坏来源和/或更强的一级相变——超出 SM 的物理。∎

---

## E. Big Bang Nucleosynthesis: The Neutron-to-Proton Ratio · 大爆炸核合成：中子–质子比

**Claim.** The n/p ratio at BBN is determined by the weak interaction rates n ↔ p + e⁻ + ν̄_e freezing out at T_f ≈ 0.7 MeV, giving (n/p)_freeze ≈ 1/6, leading to a predicted ⁴He mass fraction Y_p ≈ 0.247.

**命题。** BBN 时的 n/p 比由弱相互作用速率 n ↔ p + e⁻ + ν̄_e 在 T_f ≈ 0.7 MeV 时冻结所决定，给出 (n/p)_freeze ≈ 1/6，导致预言的 ⁴He 质量分数 Y_p ≈ 0.247。

**Step 1 — Equilibrium n/p ratio.** At T ≫ 1 MeV, weak interactions maintain equilibrium between n and p. The ratio is:

**第 1 步 — 平衡 n/p 比。** 在 T ≫ 1 MeV 时，弱相互作用维持 n 和 p 之间的平衡。比值为：

  (n/p)_eq = exp(−(m_n − m_p)/T) = exp(−Δm/T),  Δm = m_n − m_p = 1.293 MeV.

At T = 10 MeV: (n/p) = exp(−0.13) ≈ 0.88. At T = 1 MeV: (n/p) = exp(−1.29) ≈ 0.28.

在 T = 10 MeV 时：(n/p) = exp(−0.13) ≈ 0.88。在 T = 1 MeV 时：(n/p) = exp(−1.29) ≈ 0.28。

**Step 2 — Freeze-out.** The weak interaction rate for n → p + e⁻ + ν̄_e (governed by the Fermi constant G_F):

**第 2 步 — 冻结。** n → p + e⁻ + ν̄_e 的弱相互作用速率（由费米常数 G_F 支配）：

  Γ_weak ∼ G_F² T⁵.

(The T⁵ scaling comes from three factors of T from phase space, one from the neutrino/electron distribution, and G_F² from the matrix element squared.)

（T⁵ 的标度来自相空间的三个 T 因子，一个来自中微子/电子分布，G_F² 来自矩阵元的平方。）

The Hubble rate in radiation domination: H ∼ T²/M_Pl. Freeze-out when Γ_weak ≈ H:

辐射主导时期的哈勃速率：H ∼ T²/M_Pl。冻结时 Γ_weak ≈ H：

  G_F² T_f⁵ ≈ T_f²/M_Pl  ⟹  T_f³ ≈ 1/(G_F² M_Pl).

  T_f ≈ (1/(G_F² M_Pl))^{1/3} ≈ (1/(1.17 × 10⁻⁵ GeV⁻²)² × 2.4 × 10¹⁸ GeV)^{1/3}.

  ≈ (1/(3.3 × 10¹²) GeV²·GeV)^{1/3} ... numerically T_f ≈ 0.7–1 MeV.

**Step 3 — The n/p ratio at freeze-out and at BBN.** At T_f ≈ 0.7–1 MeV:

**第 3 步 — 冻结时和 BBN 时的 n/p 比。** 在 T_f ≈ 0.7–1 MeV 时：

  (n/p)_f ≈ exp(−1.293/0.8) ≈ exp(−1.6) ≈ 0.2 ≈ 1/5.

After freeze-out, free neutrons decay (τ_n ≈ 886 s). BBN begins at T_BBN ≈ 0.07 MeV (t ≈ 200 s), reducing n/p further to ≈ 1/7.

冻结后，自由中子衰变（τ_n ≈ 886 s）。BBN 在 T_BBN ≈ 0.07 MeV（t ≈ 200 s）时开始，将 n/p 进一步降至 ≈ 1/7。

**Step 4 — ⁴He mass fraction.** Almost all neutrons end up in ⁴He (the most stable light nucleus). With n/p = 1/7 at BBN:

**第 4 步 — ⁴He 质量分数。** 几乎所有中子都进入 ⁴He（最稳定的轻核）。以 BBN 时 n/p = 1/7：

  For every 8 baryons: 1 n + 7 p.
  All neutrons → ⁴He: 2n + 2p → ⁴He.
  ⁴He mass fraction: Y_p = (mass in ⁴He)/(total mass) = 2×2/(8) = 4/8 = 1/2 × (2n/(n+p))
                   = 2(n/p)/(1 + n/p) = 2×(1/7)/(1 + 1/7) = (2/7)/(8/7) = 2/8 = 1/4 ≈ 0.25.

每 8 个重子：1 n + 7 p。
所有中子 → ⁴He：2n + 2p → ⁴He。
⁴He 质量分数：Y_p = 2×(n/p)/(1 + n/p) = 2×(1/7)/(8/7) = 2/8 = 0.25.

The more precise calculation including all reactions gives Y_p ≈ 0.247, matching observations to ∼ 1% precision. ∎

包含所有反应的更精确计算给出 Y_p ≈ 0.247，与观测的精度为 ∼ 1%。∎

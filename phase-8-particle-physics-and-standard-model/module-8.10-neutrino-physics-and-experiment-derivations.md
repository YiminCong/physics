# Derivations — Module 8.10: Neutrino Physics & Experimental Particle Physics
# 推导 — 模块 8.10：中微子物理与实验粒子物理

> Companion to [Module 8.10](./module-8.10-neutrino-physics-and-experiment.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.10](./module-8.10-neutrino-physics-and-experiment.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Two-Flavor Neutrino Oscillation Probability · 两味中微子振荡概率

**Claim.** For two neutrino flavors with mixing angle θ, mass eigenstates ν₁, ν₂ with masses m₁, m₂ (Δm² = m₂² − m₁²), and a neutrino produced as flavor α traveling a distance L at energy E ≫ mᵢ, the transition probability to the other flavor β is

  P(ν_α → ν_β) = sin²(2θ) sin²(Δm² L / 4E)   (ℏ = c = 1).

**命题。** 对于混合角为 θ 的两味中微子，质量本征态 ν₁、ν₂ 的质量为 m₁、m₂（Δm² = m₂² − m₁²），以味 α 产生、能量 E ≫ mᵢ、传播距离 L 的中微子，转变为另一味 β 的概率为

  P(ν_α → ν_β) = sin²(2θ) sin²(Δm² L / 4E)   （ℏ = c = 1）。

**Step 1 — Flavor–mass basis rotation.** The two-flavor PMNS matrix is a 2×2 real rotation by angle θ:

  |ν_e⟩ =  cos θ |ν₁⟩ + sin θ |ν₂⟩
  |ν_μ⟩ = −sin θ |ν₁⟩ + cos θ |ν₂⟩.

In matrix notation |ν_flavor⟩ = U |ν_mass⟩ with U = ((cos θ, sin θ), (−sin θ, cos θ)). The inverse is |ν_mass⟩ = U† |ν_flavor⟩, so

  |ν₁⟩ = cos θ |ν_e⟩ − sin θ |ν_μ⟩
  |ν₂⟩ = sin θ |ν_e⟩ + cos θ |ν_μ⟩.

**第 1 步 — 味–质量基底旋转。** 两味 PMNS 矩阵是以角 θ 旋转的 2×2 实矩阵：

  |ν_e⟩ =  cos θ |ν₁⟩ + sin θ |ν₂⟩
  |ν_μ⟩ = −sin θ |ν₁⟩ + cos θ |ν₂⟩。

矩阵表示为 |ν_味⟩ = U |ν_质⟩，U = ((cos θ, sin θ), (−sin θ, cos θ))。逆变换为 |ν_质⟩ = U† |ν_味⟩，即

  |ν₁⟩ = cos θ |ν_e⟩ − sin θ |ν_μ⟩
  |ν₂⟩ = sin θ |ν_e⟩ + cos θ |ν_μ⟩。

**Step 2 — Time evolution in the mass basis.** Mass eigenstates have definite energy Eᵢ = √(p² + mᵢ²) ≈ p + mᵢ²/(2p) ≈ E + mᵢ²/(2E) in the ultra-relativistic limit p ≈ E ≫ mᵢ, where E is the common beam energy. Each evolves as a plane wave:

  |νᵢ(t)⟩ = e^{−iEᵢt} |νᵢ⟩.

For ultra-relativistic neutrinos the travel time t ≈ L (in c = 1 units). So at distance L:

  |νᵢ(L)⟩ = e^{−iEᵢL} |νᵢ⟩ = e^{−i(E + mᵢ²/(2E))L} |νᵢ⟩.

**第 2 步 — 质量基中的时间演化。** 质量本征态具有确定的能量 Eᵢ = √(p² + mᵢ²) ≈ p + mᵢ²/(2p) ≈ E + mᵢ²/(2E)，在超相对论极限 p ≈ E ≫ mᵢ 下成立，E 为公共束能。每个态演化为平面波：

  |νᵢ(t)⟩ = e^{−iEᵢt} |νᵢ⟩。

对于超相对论中微子，传播时间 t ≈ L（c = 1 单位制）。故在距离 L 处：

  |νᵢ(L)⟩ = e^{−iEᵢL} |νᵢ⟩ = e^{−i(E + mᵢ²/(2E))L} |νᵢ⟩。

**Step 3 — State of the neutrino at distance L.** A neutrino produced at t = 0 as ν_e is initially

  |ν(0)⟩ = |ν_e⟩ = cos θ |ν₁⟩ + sin θ |ν₂⟩.

After traveling distance L, each mass component has evolved independently:

  |ν(L)⟩ = cos θ e^{−iE₁L} |ν₁⟩ + sin θ e^{−iE₂L} |ν₂⟩.

Factor out the common phase e^{−iEL} (which cancels in probabilities):

  |ν(L)⟩ = e^{−iEL} [ cos θ e^{−im₁²L/(2E)} |ν₁⟩ + sin θ e^{−im₂²L/(2E)} |ν₂⟩ ].

**第 3 步 — 距离 L 处中微子的状态。** 在 t = 0 以 ν_e 产生的中微子初始状态为

  |ν(0)⟩ = |ν_e⟩ = cos θ |ν₁⟩ + sin θ |ν₂⟩。

传播距离 L 后，每个质量分量独立演化：

  |ν(L)⟩ = cos θ e^{−iE₁L} |ν₁⟩ + sin θ e^{−iE₂L} |ν₂⟩。

提取公共相位因子 e^{−iEL}（在概率中约去）：

  |ν(L)⟩ = e^{−iEL} [ cos θ e^{−im₁²L/(2E)} |ν₁⟩ + sin θ e^{−im₂²L/(2E)} |ν₂⟩ ]。

**Step 4 — Project onto ν_μ.** Substitute back |ν₁⟩ = cos θ |ν_e⟩ − sin θ |ν_μ⟩ and |ν₂⟩ = sin θ |ν_e⟩ + cos θ |ν_μ⟩:

  |ν(L)⟩ ∝ cos θ e^{−iφ₁}(cos θ |ν_e⟩ − sin θ |ν_μ⟩) + sin θ e^{−iφ₂}(sin θ |ν_e⟩ + cos θ |ν_μ⟩)

where φᵢ = mᵢ²L/(2E). The amplitude to find ν_μ is

  A(ν_e → ν_μ) = ⟨ν_μ|ν(L)⟩ ∝ −cos θ sin θ e^{−iφ₁} + sin θ cos θ e^{−iφ₂}

  = sin θ cos θ (e^{−iφ₂} − e^{−iφ₁}).

**第 4 步 — 向 ν_μ 投影。** 代回 |ν₁⟩ = cos θ |ν_e⟩ − sin θ |ν_μ⟩ 和 |ν₂⟩ = sin θ |ν_e⟩ + cos θ |ν_μ⟩：

  |ν(L)⟩ ∝ cos θ e^{−iφ₁}(cos θ |ν_e⟩ − sin θ |ν_μ⟩) + sin θ e^{−iφ₂}(sin θ |ν_e⟩ + cos θ |ν_μ⟩)，

其中 φᵢ = mᵢ²L/(2E)。探测到 ν_μ 的振幅为

  A(ν_e → ν_μ) = ⟨ν_μ|ν(L)⟩ ∝ −cos θ sin θ e^{−iφ₁} + sin θ cos θ e^{−iφ₂}

  = sin θ cos θ (e^{−iφ₂} − e^{−iφ₁})。

**Step 5 — Compute the probability.** The probability is |A|²:

  P(ν_e → ν_μ) = sin²θ cos²θ |e^{−iφ₂} − e^{−iφ₁}|².

Expand the modulus squared:

  |e^{−iφ₂} − e^{−iφ₁}|² = (e^{−iφ₂} − e^{−iφ₁})(e^{+iφ₂} − e^{+iφ₁})
  = 2 − 2 cos(φ₂ − φ₁) = 4 sin²((φ₂ − φ₁)/2).

With φ₂ − φ₁ = (m₂² − m₁²)L/(2E) = Δm² L/(2E):

  P(ν_e → ν_μ) = sin²θ cos²θ · 4 sin²(Δm² L / 4E).

Use the double-angle identity sin²θ cos²θ = ¼ sin²(2θ):

  **P(ν_e → ν_μ) = sin²(2θ) sin²(Δm² L / 4E)**. ∎

**第 5 步 — 计算概率。** 概率为 |A|²：

  P(ν_e → ν_μ) = sin²θ cos²θ |e^{−iφ₂} − e^{−iφ₁}|²。

展开模的平方：

  |e^{−iφ₂} − e^{−iφ₁}|² = (e^{−iφ₂} − e^{−iφ₁})(e^{+iφ₂} − e^{+iφ₁})
  = 2 − 2 cos(φ₂ − φ₁) = 4 sin²((φ₂ − φ₁)/2)。

以 φ₂ − φ₁ = (m₂² − m₁²)L/(2E) = Δm² L/(2E) 代入：

  P(ν_e → ν_μ) = sin²θ cos²θ · 4 sin²(Δm² L / 4E)。

使用二倍角恒等式 sin²θ cos²θ = ¼ sin²(2θ)：

  **P(ν_e → ν_μ) = sin²(2θ) sin²(Δm² L / 4E)**。∎

---

## B. The Oscillation Length and L/E Dependence · 振荡长度与 L/E 依赖性

**Claim.** The oscillation has a characteristic length scale L_osc = 4πE/Δm², and the argument of the sine squared is π L/L_osc. In SI-convenient units:

  L_osc [km] = 2.48 · E [GeV] / (Δm² [eV²]).

**命题。** 振荡具有特征长度标度 L_osc = 4πE/Δm²，正弦平方的宗量为 π L/L_osc。在实用单位中：

  L_osc [km] = 2.48 · E [GeV] / (Δm² [eV²])。

**Step 1 — Restore ℏ and c.** In natural units (ℏ = c = 1), the argument of the oscillation is Δm² L/(4E). Restoring dimensions: energy E is in eV, mass-squared difference Δm² in eV², length L in meters, and using ℏc = 197.3 MeV·fm = 197.3 × 10⁻¹⁵ MeV·m:

  Δm² L / (4E) → Δm²[eV²] · L[m] / (4 E[eV] · ℏc[eV·m])

  with ℏc = 197.3 × 10⁻⁹ eV·m,

  = Δm²[eV²] · L[m] / (4 · E[eV] · 197.3 × 10⁻⁹ eV·m)

  = 1.267 · Δm²[eV²] · L[km] / E[GeV].

**第 1 步 — 还原 ℏ 和 c。** 在自然单位（ℏ = c = 1）中，振荡宗量为 Δm² L/(4E)。还原量纲：能量 E 以 eV 为单位，质量平方差 Δm² 以 eV² 为单位，长度 L 以米为单位，利用 ℏc = 197.3 × 10⁻¹⁵ MeV·m = 197.3 × 10⁻⁹ eV·m：

  Δm² L / (4E) → Δm²[eV²] · L[m] / (4 E[eV] · ℏc[eV·m])

  = Δm²[eV²] · L[m] / (4 · E[eV] · 197.3 × 10⁻⁹ eV·m)

  = 1.267 · Δm²[eV²] · L[km] / E[GeV]。

**Step 2 — Define the oscillation length.** The probability first reaches its maximum when sin²(1.267 Δm² L/E) = 1, i.e., 1.267 Δm²[eV²] L[km]/E[GeV] = π/2. Hence the oscillation length (the distance for one full oscillation cycle, sin² goes from 0 to 1 and back to 0) is

  L_osc = (π / 1.267) · E[GeV] / Δm²[eV²] km = 2.48 · E[GeV] / Δm²[eV²] km.

The probability can be written as P = sin²(2θ) sin²(π L / L_osc), confirming the periodic nature. The L/E ratio is the natural observable: experiments are most sensitive at L/E ≈ L_osc/2 (the oscillation maximum), and the observation of oscillatory L/E dependence is the definitive signature.

**第 2 步 — 定义振荡长度。** 概率首次达到最大值时，sin²(1.267 Δm² L/E) = 1，即 1.267 Δm²[eV²] L[km]/E[GeV] = π/2。故振荡长度（一个完整振荡周期的距离，sin² 从 0 到 1 再回到 0）为

  L_osc = (π / 1.267) · E[GeV] / Δm²[eV²] km = 2.48 · E[GeV] / Δm²[eV²] km。

概率可写为 P = sin²(2θ) sin²(π L / L_osc)，确认了周期性特征。L/E 比值是自然的可观测量：实验在 L/E ≈ L_osc/2（振荡极大处）最为灵敏，L/E 依赖性的振荡规律是决定性的特征标志。

**Step 3 — Numerical check for atmospheric and solar oscillations.**

Atmospheric: Δm²₂₃ ≈ 2.5 × 10⁻³ eV², E ~ 1 GeV (sub-GeV atmospheric ν): L_osc ≈ 2.48 × 1/0.0025 ≈ 990 km. The Earth's diameter is ~12,000 km, so upward-going atmospheric neutrinos (L ~ 10,000 km) have oscillated multiple times — consistent with the observed large deficit.

Solar: Δm²₁₂ ≈ 7.4 × 10⁻⁵ eV², E ~ 1 MeV: L_osc ≈ 2.48 × 10⁻³ / 7.4 × 10⁻⁵ ≈ 33,000 km. The Sun–Earth distance is ~1.5 × 10⁸ km, far exceeding L_osc, so the oscillations average out in vacuum. It is the MSW effect inside the Sun that drives the conversion, not vacuum oscillations.

**第 3 步 — 大气与太阳振荡的数值检验。**

大气：Δm²₂₃ ≈ 2.5 × 10⁻³ eV²，E ~ 1 GeV（次 GeV 大气中微子）：L_osc ≈ 2.48 × 1/0.0025 ≈ 990 km。地球直径约 12,000 km，故向上行大气中微子（L ~ 10,000 km）已振荡多次——与观测到的大亏缺一致。

太阳：Δm²₁₂ ≈ 7.4 × 10⁻⁵ eV²，E ~ 1 MeV：L_osc ≈ 2.48 × 10⁻³ / 7.4 × 10⁻⁵ ≈ 33,000 km。日地距离约 1.5 × 10⁸ km，远超 L_osc，故真空振荡在平均后消失。驱动转化的是太阳内部的 MSW 效应，而非真空振荡。

---

## C. The MSW Resonance Condition · MSW 共振条件

**Claim.** In matter of electron density n_e, the effective Hamiltonian for two-flavor (ν_e, ν_μ) propagation acquires a diagonal term V = √2 G_F n_e for ν_e (from charged-current forward scattering on electrons). Resonant flavor conversion — effective mixing angle in matter θ_m = π/4 (maximal mixing) — occurs when

  n_e^{res} = Δm² cos(2θ) / (2√2 G_F E).

**命题。** 在电子数密度为 n_e 的物质中，两味（ν_e, ν_μ）传播的有效哈密顿量获得 ν_e 特有的对角项 V = √2 G_F n_e（来自与电子的带电流前向散射）。共振味转换——物质中有效混合角 θ_m = π/4（最大混合）——发生在

  n_e^{res} = Δm² cos(2θ) / (2√2 G_F E)。

**Step 1 — Effective Hamiltonian in the flavor basis.** In vacuum the Hamiltonian in the flavor basis (ν_e, ν_μ) can be written (dropping a term proportional to the identity, which shifts all phases equally and cancels in oscillation probabilities) as

  H_vac = (Δm²/4E) U diag(−1, +1) U†

  = (Δm²/4E) (( −cos 2θ,  sin 2θ ),
                (  sin 2θ,  cos 2θ )).

In matter, charged-current forward scattering of ν_e on electrons adds V = √2 G_F n_e to the ν_e diagonal:

  H_mat = H_vac + diag(V, 0)

  = (Δm²/4E) (( −cos 2θ + A,  sin 2θ ),
               (  sin 2θ,      cos 2θ − A + ... )),

where A = 2√2 G_F n_e E / Δm² (the matter parameter, dimensionless in natural units).

**第 1 步 — 味基中的有效哈密顿量。** 在真空中，味基（ν_e, ν_μ）中的哈密顿量可写为（略去正比于单位矩阵的项，该项在振荡概率中消去）：

  H_vac = (Δm²/4E) U diag(−1, +1) U†

  = (Δm²/4E) (( −cos 2θ,  sin 2θ ),
                (  sin 2θ,  cos 2θ ))。

在物质中，ν_e 与电子的带电流前向散射在 ν_e 对角元上加入 V = √2 G_F n_e：

  H_mat = H_vac + diag(V, 0)

  = (Δm²/4E) (( −cos 2θ + A,  sin 2θ ),
               (  sin 2θ,      cos 2θ − A + ... ))，

其中 A = 2√2 G_F n_e E / Δm²（物质参数，自然单位中无量纲）。

**Step 2 — Effective mixing angle in matter.** The matter Hamiltonian H_mat is diagonalized by an effective mixing angle θ_m defined by

  tan(2θ_m) = sin(2θ) / (cos(2θ) − A).

The effective Δm²_m and θ_m satisfy

  sin²(2θ_m) = sin²(2θ) / [(cos 2θ − A)² + sin²(2θ)].

**第 2 步 — 物质中的有效混合角。** 物质哈密顿量 H_mat 由有效混合角 θ_m 对角化，其定义为

  tan(2θ_m) = sin(2θ) / (cos(2θ) − A)。

有效 Δm²_m 和 θ_m 满足

  sin²(2θ_m) = sin²(2θ) / [(cos 2θ − A)² + sin²(2θ)]。

**Step 3 — Resonance condition.** The effective mixing is maximal (sin²(2θ_m) = 1, i.e. θ_m = π/4) when the denominator is minimized, which requires

  cos(2θ) − A = 0  ⟹  A = cos(2θ)

  ⟹  2√2 G_F n_e^{res} E / Δm² = cos(2θ)

  ⟹  **n_e^{res} = Δm² cos(2θ) / (2√2 G_F E)**. ∎

At resonance the off-diagonal mixing completely dominates: even a small vacuum mixing angle θ ≪ 1 produces complete flavor conversion if the neutrino passes through the resonance density adiabatically. The adiabaticity condition (the density scale height ≫ the oscillation length at resonance) is satisfied in the Sun for Δm²₁₂ and the relevant solar neutrino energies.

**第 3 步 — 共振条件。** 有效混合最大化（sin²(2θ_m) = 1，即 θ_m = π/4）时，分母最小，需要

  cos(2θ) − A = 0  ⟹  A = cos(2θ)

  ⟹  2√2 G_F n_e^{res} E / Δm² = cos(2θ)

  ⟹  **n_e^{res} = Δm² cos(2θ) / (2√2 G_F E)**。∎

在共振处，非对角混合完全主导：即使真空混合角 θ ≪ 1，只要中微子绝热地穿越共振密度，就会发生完全的味转换。绝热性条件（密度标高 ≫ 共振处的振荡长度）对于 Δm²₁₂ 和相关太阳中微子能量在太阳中得到满足。

---

## D. Event Rate from Luminosity and Cross-Section · 由亮度和截面得到事例率

**Claim.** The number of signal events produced in a collider run is N = L_int · σ, where L_int is the integrated luminosity and σ is the production cross-section.

**命题。** 对撞机运行期间产生的信号事例数为 N = L_int · σ，其中 L_int 为积分亮度，σ 为产生截面。

**Step 1 — Instantaneous luminosity.** Consider two counter-rotating beams of N₁ and N₂ particles per bunch, with n_b bunches per beam, revolution frequency f_rev, and transverse Gaussian beam profiles of widths σ_x, σ_y. The beam overlap integral, assuming the bunches collide head-on, gives the number of collisions per unit time per unit cross-section:

  L = (N₁ N₂ n_b f_rev) / (4π σ_x σ_y).

The factor 4π σ_x σ_y is the effective transverse area A of the overlap.

**第 1 步 — 瞬时亮度。** 考虑两束反向运行的束流，每个束团粒子数分别为 N₁ 和 N₂，每束 n_b 个束团，回旋频率 f_rev，横向高斯束流轮廓宽度为 σ_x、σ_y。在束团正面对撞假设下，束流重叠积分给出单位时间单位截面的碰撞次数：

  L = (N₁ N₂ n_b f_rev) / (4π σ_x σ_y)。

4π σ_x σ_y 即重叠区的有效横截面积 A。

**Step 2 — Cross-section as the proportionality constant.** The rate of events of a given process is proportional to L: dN/dt = L · σ. Physically, σ is the effective area that one beam particle presents to the other for a given reaction. Integrating over a run:

  N = ∫ L(t) dt · σ = L_int · σ.

This relation holds because σ is a property of the process (fixed by the matrix element and phase space — Module 8.1 to 8.4), while L_int encodes the collider performance.

**第 2 步 — 截面作为比例系数。** 给定过程的事例率正比于 L：dN/dt = L · σ。在物理上，σ 是一个束流粒子对给定反应所呈现给另一束流粒子的有效面积。对一次运行积分：

  N = ∫ L(t) dt · σ = L_int · σ。

此关系成立是因为 σ 是过程的性质（由矩阵元和相空间固定——模块 8.1 至 8.4），而 L_int 编码了对撞机性能。

**Step 3 — Units.** Cross-sections are measured in **barns**: 1 b = 10⁻²⁴ cm². For weak processes and rare Standard Model processes, the relevant units are fb (femtobarn, 10⁻³⁹ cm²) or pb (picobarn, 10⁻³⁶ cm²). LHC luminosity is quoted in fb⁻¹: 1 fb⁻¹ of L_int times 1 fb cross-section gives exactly 1 event. The Higgs boson production cross-section at 13 TeV via gluon fusion is σ ≈ 48 pb; with L_int = 140 fb⁻¹, this gives N ≈ 6.7 × 10⁶ Higgs bosons produced, before branching fractions and detector acceptance.

**第 3 步 — 单位。** 截面以**靶恩（barn）**为单位：1 b = 10⁻²⁴ cm²。对于弱过程和罕见标准模型过程，常用单位为 fb（飞靶恩，10⁻³⁹ cm²）或 pb（皮靶恩，10⁻³⁶ cm²）。LHC 亮度以 fb⁻¹ 表示：L_int 为 1 fb⁻¹ 乘以截面 1 fb 恰好给出 1 个事例。13 TeV 时希格斯玻色子通过胶子融合产生的截面约 σ ≈ 48 pb；在 L_int = 140 fb⁻¹ 下，产生的希格斯玻色子数为 N ≈ 6.7 × 10⁶，这是在分支比和探测器接受度之前的数字。

---

## E. Invariant-Mass Reconstruction · 不变质量重建

**Claim.** If a resonance X decays to n particles with four-momenta pᵢ = (Eᵢ, **p**ᵢ), the invariant mass-squared of X is

  M²_X = (Σᵢ pᵢ)² = (Σᵢ Eᵢ)² − |Σᵢ **p**ᵢ|²   (c = 1).

**命题。** 若共振态 X 衰变为 n 个粒子，四动量为 pᵢ = (Eᵢ, **p**ᵢ)，则 X 的不变质量平方为

  M²_X = (Σᵢ pᵢ)² = (Σᵢ Eᵢ)² − |Σᵢ **p**ᵢ|²   （c = 1）。

**Step 1 — Lorentz invariance.** The four-momentum of the resonance before decay is P_X = (M_X, **0**) in its rest frame, so P_X² = M²_X. Since the four-momentum of the resonance equals the sum of the decay-product four-momenta (by four-momentum conservation at the decay vertex), P_X = Σᵢ pᵢ. Because P² is a Lorentz scalar, it takes the same value in every frame:

  M²_X = P_X² = (Σᵢ pᵢ)² = (Σᵢ Eᵢ)² − |Σᵢ **p**ᵢ|².

This is the definition of the **invariant mass**, and its value equals M²_X regardless of the frame in which the decay products are measured.

**第 1 步 — 洛伦兹不变性。** 在静止系中，共振态衰变前的四动量为 P_X = (M_X, **0**)，故 P_X² = M²_X。由于衰变顶点处四动量守恒，P_X = Σᵢ pᵢ。因为 P² 是洛伦兹标量，在任何参考系中取同一值：

  M²_X = P_X² = (Σᵢ pᵢ)² = (Σᵢ Eᵢ)² − |Σᵢ **p**ᵢ|²。

这就是**不变质量**的定义，其值等于 M²_X，与测量衰变产物的参考系无关。

**Step 2 — Two-body case.** For X → 1 + 2:

  M²_X = (E₁ + E₂)² − |**p**₁ + **p**₂|²
  = E₁² + E₂² + 2E₁E₂ − |**p**₁|² − |**p**₂|² − 2**p**₁·**p**₂
  = m₁² + m₂² + 2(E₁E₂ − **p**₁·**p**₂),

using Eᵢ² − |**p**ᵢ|² = mᵢ². In terms of the angle θ₁₂ between the two momenta:

  M²_X = m₁² + m₂² + 2E₁E₂(1 − β₁β₂ cos θ₁₂),

where βᵢ = |**p**ᵢ|/Eᵢ. For massless particles (e.g. two photons from H → γγ) with m₁ = m₂ = 0:

  M²_γγ = 2E₁E₂(1 − cos θ₁₂) = 4E₁E₂ sin²(θ₁₂/2).

**第 2 步 — 两体情形。** 对于 X → 1 + 2：

  M²_X = (E₁ + E₂)² − |**p**₁ + **p**₂|²
  = E₁² + E₂² + 2E₁E₂ − |**p**₁|² − |**p**₂|² − 2**p**₁·**p**₂
  = m₁² + m₂² + 2(E₁E₂ − **p**₁·**p**₂)，

利用 Eᵢ² − |**p**ᵢ|² = mᵢ²。以两动量间夹角 θ₁₂ 表示：

  M²_X = m₁² + m₂² + 2E₁E₂(1 − β₁β₂ cos θ₁₂)，

其中 βᵢ = |**p**ᵢ|/Eᵢ。对于无质量粒子（如 H → γγ 中的两个光子），m₁ = m₂ = 0：

  M²_γγ = 2E₁E₂(1 − cos θ₁₂) = 4E₁E₂ sin²(θ₁₂/2)。

**Step 3 — Breit–Wigner resonance peak.** Near the resonance, the production amplitude is dominated by the resonant propagator. The cross-section for X production (e.g. e⁺e⁻ → Z → ff̄) has a Breit–Wigner form

  σ(s) ∝ s · Γ_in · Γ_out / [(√s − M_X)² + Γ²/4],

where √s is the center-of-mass energy, Γ_in and Γ_out are the partial widths for the initial and final states, and Γ is the total width. In the invariant-mass spectrum of the decay products, this appears as a **peak at M_inv = M_X** with Lorentzian shape and FWHM = Γ. For the Z boson M_Z = 91.2 GeV, Γ_Z = 2.5 GeV; for the Higgs M_H = 125.1 GeV, Γ_H = 4 MeV (so narrow that the peak width is dominated by detector resolution, not the intrinsic width).

**第 3 步 — 布莱特–维格纳共振峰。** 在共振附近，产生振幅由共振传播子主导。X 产生（如 e⁺e⁻ → Z → ff̄）的截面具有布莱特–维格纳形式

  σ(s) ∝ s · Γ_in · Γ_out / [(√s − M_X)² + Γ²/4]，

其中 √s 为质心能量，Γ_in 和 Γ_out 为初末态的分波宽度，Γ 为总宽度。在衰变产物的不变质量谱中，这表现为**M_inv = M_X 处的峰值**，具有洛伦兹线型，半高全宽 = Γ。对于 Z 玻色子，M_Z = 91.2 GeV，Γ_Z = 2.5 GeV；对于希格斯玻色子，M_H = 125.1 GeV，Γ_H = 4 MeV（因此峰宽由探测器分辨率而非固有宽度主导）。∎

---

*All derivations follow the deep/rigorous standard: full intermediate algebra, dimensional analysis, physical interpretation, and bilingual presentation.*

*所有推导均遵循深度/严格标准：完整的中间代数、量纲分析、物理诠释和双语呈现。*

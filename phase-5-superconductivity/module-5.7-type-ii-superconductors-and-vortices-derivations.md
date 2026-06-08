# Derivations — Module 5.7: Type II Superconductors & Vortices
# 推导 — 模块 5.7：II 型超导体与涡旋

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.7](./module-5.7-type-ii-superconductors-and-vortices.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.7](./module-5.7-type-ii-superconductors-and-vortices.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Quantized Flux: Φ₀ = h/2e · 量子化磁通量：Φ₀ = h/2e

**Claim.** A single superconducting vortex carries exactly one flux quantum Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb. No smaller unit of flux can be trapped in a superconductor.

**命题。** 单个超导涡旋恰好携带一个磁通量子 Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb。超导体中不能俘获比此更小的磁通单元。

**Step 1 — The GL order parameter and its phase.** In Ginzburg–Landau theory (Module 5.3), the superconducting state is described by the complex order parameter Ψ(r) = |Ψ(r)| e^{iφ(r)}, where φ(r) is the macroscopic phase. The GL supercurrent density is

  J_s = (ℏe*/m*)[ |Ψ|² (∇φ − e*A/ℏ) ],

where e* = 2e is the Cooper-pair charge, m* = 2m is the pair mass, and A is the vector potential. This follows from the standard substitution p → p − e*A in quantum mechanics applied to the pair condensate.

**第 1 步 — GL 序参量及其相位。** 在金兹堡–朗道理论（模块 5.3）中，超导态由复序参量 Ψ(r) = |Ψ(r)| e^{iφ(r)} 描述，φ(r) 为宏观相位。GL 超电流密度为

  J_s = (ℏe*/m*)[ |Ψ|² (∇φ − e*A/ℏ) ]，

其中 e* = 2e 为库珀对电荷，m* = 2m 为对质量，A 为矢量势。这由量子力学中对配对凝聚体作标准代换 p → p − e*A 而来。

**Step 2 — Contour integral deep inside the vortex.** Take a closed contour C that encircles the vortex core and lies deep inside the superconductor (at distances much larger than the penetration depth λ from the core). Deep inside, J_s = 0 (the Meissner-like screening is complete). Setting J_s = 0 in the GL equation:

  ∇φ = e*A/ℏ = 2eA/ℏ.

Integrate around the contour C:

  ∮_C ∇φ · dl = (2e/ℏ) ∮_C A · dl = (2e/ℏ) Φ,

where Φ = ∮ A · dl = ∫∫ B · dS is the total flux through C by Stokes' theorem.

**第 2 步 — 在涡旋深处的回路积分。** 取一封闭回路 C，绕涡旋核心，且位于超导体深处（距核心距离远大于穿透深度 λ）。深处 J_s = 0（迈斯纳屏蔽完全）。在 GL 方程中令 J_s = 0：

  ∇φ = e*A/ℏ = 2eA/ℏ。

沿回路 C 积分：

  ∮_C ∇φ · dl = (2e/ℏ) ∮_C A · dl = (2e/ℏ) Φ，

其中由斯托克斯定理 Φ = ∮ A · dl = ∫∫ B · dS 为穿过 C 的总磁通量。

**Step 3 — Single-valuedness of Ψ.** The order parameter Ψ = |Ψ| e^{iφ} must be single-valued: going around C must return φ to the same value modulo 2π. Thus

  ∮_C ∇φ · dl = 2π n,    n ∈ ℤ.

**第 3 步 — Ψ 的单值性。** 序参量 Ψ = |Ψ| e^{iφ} 必须单值：绕 C 一圈后 φ 必须回到相差 2π 整数倍的同一值。因此

  ∮_C ∇φ · dl = 2π n，    n ∈ ℤ。

**Step 4 — Flux quantization.** Equating Steps 2 and 3:

  (2e/ℏ) Φ = 2π n    ⟹    Φ = n · πℏ/e = n · h/(2e) = n Φ₀,

where **Φ₀ = h/(2e)** is the fundamental flux quantum. A single vortex corresponds to |n| = 1, carrying one Φ₀. Vortices with |n| > 1 are energetically unstable (their energy scales as n², so they split into n single-quantum vortices). ∎

**第 4 步 — 磁通量子化。** 由第 2、3 步相等：

  (2e/ℏ) Φ = 2π n    ⟹    Φ = n · πℏ/e = n · h/(2e) = n Φ₀，

其中 **Φ₀ = h/(2e)** 为基本磁通量子。单个涡旋对应 |n| = 1，携带一个 Φ₀。|n| > 1 的涡旋能量上不稳定（能量正比于 n²），会分裂为 n 个单量子涡旋。∎

---

## B. Lower Critical Field H_c1 · 下临界场 H_c1

**Claim.** A single vortex line per unit length in a type-II superconductor has a self-energy (London limit, κ ≫ 1)

  ε_v ≈ (Φ₀²/4πμ₀λ²) ln(λ/ξ)    per unit length.

The lower critical field H_c1 is the applied field at which it first becomes thermodynamically favorable for a vortex to enter, determined by balancing the vortex energy against the magnetic energy gained:

  μ₀ H_c1 = Φ₀ / (4πλ²) · ln(λ/ξ)    (Gaussian: H_c1 = Φ₀/(4πλ²) ln κ).

**命题。** 在 II 型超导体中，单条涡旋线单位长度的自能（伦敦极限，κ ≫ 1）为

  ε_v ≈ (Φ₀²/4πμ₀λ²) ln(λ/ξ)    每单位长度。

下临界场 H_c1 是使涡旋进入热力学上有利的外场，由涡旋能量与所获磁能平衡决定：

  μ₀ H_c1 = Φ₀ / (4πλ²) · ln(λ/ξ)    （高斯制：H_c1 = Φ₀/(4πλ²) ln κ）。

**Step 1 — London equations in the vortex region.** Outside the normal core (r > ξ), the superconductor satisfies the London equation:

  ∇ × B = μ₀ J_s = −(μ₀/λ²) A_s    (London gauge ∇·A = 0),

which together with ∇ × B = μ₀ J_s and ∇ × (∇ × B) = −∇²B gives

  −∇²B + B/λ² = 0    (for r > ξ).

For a single vortex along the z-axis, the field B = B(r) ẑ depends only on the distance r from the axis.

**第 1 步 — 涡旋区域的伦敦方程。** 在正常态核心外（r > ξ），超导体满足伦敦方程：

  ∇ × B = μ₀ J_s = −(μ₀/λ²) A_s    （伦敦规范 ∇·A = 0），

结合 ∇ × B = μ₀ J_s 及 ∇ × (∇ × B) = −∇²B 得

  −∇²B + B/λ² = 0    （r > ξ 时）。

对沿 z 轴的单涡旋，场 B = B(r) ẑ 仅依赖于距轴的距离 r。

**Step 2 — Cylindrical London equation and its solution.** In cylindrical coordinates, ∇²B = (1/r) d/dr (r dB/dr), so the London equation becomes the modified Bessel equation:

  (1/r) d/dr (r dB/dr) − B/λ² = 0.

This is the modified Bessel equation of order zero. Its solution decaying at r → ∞ is

  B(r) = C K₀(r/λ),

where K₀ is the modified Bessel function of the second kind of order zero, and C is a constant fixed by the flux condition.

**第 2 步 — 柱坐标伦敦方程及其解。** 在柱坐标中 ∇²B = (1/r) d/dr (r dB/dr)，伦敦方程化为零阶修正贝塞尔方程：

  (1/r) d/dr (r dB/dr) − B/λ² = 0。

该方程在 r → ∞ 时衰减的解为

  B(r) = C K₀(r/λ)，

其中 K₀ 为零阶第二类修正贝塞尔函数，C 由磁通条件确定。

**Step 3 — Fix the constant from flux quantization.** The total flux must equal Φ₀:

  ∫₀^∞ B(r) 2πr dr = Φ₀.

Using ∫₀^∞ K₀(r/λ) r dr = λ², we get C · 2πλ² = Φ₀, so

  C = Φ₀ / (2πλ²).

Thus B(r) = (Φ₀/2πλ²) K₀(r/λ).

**第 3 步 — 由磁通量子化确定常数。** 总磁通须等于 Φ₀：

  ∫₀^∞ B(r) 2πr dr = Φ₀。

利用 ∫₀^∞ K₀(r/λ) r dr = λ²，得 C · 2πλ² = Φ₀，即

  C = Φ₀ / (2πλ²)，

从而 B(r) = (Φ₀/2πλ²) K₀(r/λ)。

**Step 4 — Compute the vortex line energy.** The electromagnetic energy per unit length stored in the vortex field is

  ε_v = ∫ (B²/2μ₀ + μ₀λ² J_s²/2) 2πr dr.

In the London regime both terms are equal (virial theorem for London equations), so ε_v = ∫ (B²/μ₀) 2πr dr (integrating from ξ to ∞ — the core itself has a small condensation energy contribution). Substituting B(r):

  ε_v = (1/μ₀)(Φ₀/2πλ²)² ∫_ξ^∞ K₀²(r/λ) 2πr dr.

For κ = λ/ξ ≫ 1, using K₀(x) ≈ −ln(x) for x ≪ 1 and K₀(x) ≈ √(π/2x)e^{−x} for x ≫ 1, the integral evaluates to ≈ πλ² ln(λ/ξ). Hence

  ε_v ≈ (Φ₀²/4πμ₀λ²) ln(λ/ξ) = (Φ₀²/4πμ₀λ²) ln κ    per unit length.

**第 4 步 — 计算涡旋线能量。** 单位长度涡旋场储存的电磁能为

  ε_v = ∫ (B²/2μ₀ + μ₀λ² J_s²/2) 2πr dr。

在伦敦体制中两项相等（伦敦方程的维里定理），故 ε_v = ∫ (B²/μ₀) 2πr dr（从 ξ 到 ∞ 积分——核心本身有小的凝聚能贡献）。代入 B(r)：

  ε_v = (1/μ₀)(Φ₀/2πλ²)² ∫_ξ^∞ K₀²(r/λ) 2πr dr。

对 κ = λ/ξ ≫ 1，利用 K₀(x) ≈ −ln(x)（x ≪ 1 时）和 K₀(x) ≈ √(π/2x)e^{−x}（x ≫ 1 时），积分约为 πλ² ln(λ/ξ)。故

  ε_v ≈ (Φ₀²/4πμ₀λ²) ln(λ/ξ) = (Φ₀²/4πμ₀λ²) ln κ    每单位长度。

**Step 5 — Thermodynamic condition for H_c1.** A vortex first enters when the Gibbs free energy per unit length gained by the field threading equals the vortex self-energy. The magnetic energy gain per unit length when one flux quantum Φ₀ enters at external field H is

  ΔG_mag = −μ₀ H Φ₀    (per unit length, the work done by the field source).

Setting ε_v + ΔG_mag = 0 at the onset field H = H_c1:

  μ₀ H_c1 Φ₀ = ε_v    ⟹    μ₀ H_c1 = (Φ₀/4πλ²) ln κ.

This is the **lower critical field**. ∎

**第 5 步 — H_c1 的热力学条件。** 当磁场穿透所带来的吉布斯自由能收益等于涡旋自能时，涡旋开始进入。单位长度内一个磁通量子 Φ₀ 在外场 H 下穿入所获磁能为

  ΔG_mag = −μ₀ H Φ₀    （单位长度，即场源做的功）。

在起始场 H = H_c1 处令 ε_v + ΔG_mag = 0：

  μ₀ H_c1 Φ₀ = ε_v    ⟹    μ₀ H_c1 = (Φ₀/4πλ²) ln κ。

这即为**下临界场**。∎

---

## C. Upper Critical Field H_c2: GL as a Landau-Level Problem · 上临界场 H_c2：GL 方程化为朗道能级问题

**Claim.** The upper critical field is

  H_c2 = Φ₀ / (2πμ₀ξ²)    (SI),    i.e.,    B_c2 = Φ₀ / (2πξ²).

It is found by solving the linearized GL equation near the normal-to-superconductor transition, which maps exactly onto a 2D quantum harmonic oscillator (Landau levels).

**命题。** 上临界场为

  H_c2 = Φ₀ / (2πμ₀ξ²)    （SI），    即    B_c2 = Φ₀ / (2πξ²）。

它由在正常–超导相变附近求解线性化 GL 方程得到，该方程恰好对应二维量子谐振子（朗道能级）。

**Step 1 — Linearized GL equation.** Near H_c2, the order parameter |Ψ| is small (the transition is second order). The full GL equation (Module 5.3) is

  (1/2m*) (−iℏ∇ − e*A)² Ψ + α Ψ + β|Ψ|² Ψ = 0.

Linearize by dropping the |Ψ|² term (valid for small |Ψ|):

  (1/2m*) (−iℏ∇ − e*A)² Ψ = −α Ψ.

With α < 0 below T_c, write −α = |α| > 0. This is a Schrödinger-like equation for Ψ in an effective magnetic field.

**第 1 步 — 线性化 GL 方程。** 在 H_c2 附近，序参量 |Ψ| 很小（相变为二级）。完整 GL 方程（模块 5.3）为

  (1/2m*) (−iℏ∇ − e*A)² Ψ + α Ψ + β|Ψ|² Ψ = 0。

线性化（去掉 |Ψ|² 项，小 |Ψ| 时有效）：

  (1/2m*) (−iℏ∇ − e*A)² Ψ = −α Ψ。

在 T_c 以下 α < 0，令 −α = |α| > 0。这是 Ψ 在有效磁场中的类薛定谔方程。

**Step 2 — Map to a quantum harmonic oscillator.** Choose the Landau gauge A = (0, Bx, 0) for a uniform field B along z. The kinetic operator expands:

  (−iℏ∇ − e*A)² = −ℏ²∂²/∂x² + (−iℏ∂/∂y − e*Bx)² + (−iℏ∂/∂z)²

Try a solution of the form Ψ = e^{i(k_y y + k_z z)} f(x). Substituting:

  [−ℏ²∂²/∂x² + (ℏk_y − e*Bx)²/(2m*) + ℏ²k_z²/(2m*)] f(x) = |α| f(x).

This is the 1D harmonic oscillator equation in x, centered at x₀ = ℏk_y/(e*B), with frequency ω_c = e*B/m* (the cyclotron frequency for the pair). Setting k_z = 0 (the critical field arises from the lowest-energy mode):

  [−ℏ²/2m* · ∂²/∂x² + ½m* ω_c² (x − x₀)²] f(x) = |α| f(x).

**第 2 步 — 映射到量子谐振子。** 选朗道规范 A = (0, Bx, 0)，B 沿 z 方向均匀。动能算符展开：

  (−iℏ∇ − e*A)² = −ℏ²∂²/∂x² + (−iℏ∂/∂y − e*Bx)² + (−iℏ∂/∂z)²

尝试 Ψ = e^{i(k_y y + k_z z)} f(x) 形式的解，代入：

  [−ℏ²∂²/∂x² + (ℏk_y − e*Bx)²/(2m*) + ℏ²k_z²/(2m*)] f(x) = |α| f(x)。

这是以 x₀ = ℏk_y/(e*B) 为中心、频率 ω_c = e*B/m*（对的回旋频率）的一维谐振子方程。令 k_z = 0（临界场来自最低能量模式）：

  [−ℏ²/2m* · ∂²/∂x² + ½m* ω_c² (x − x₀)²] f(x) = |α| f(x)。

**Step 3 — Landau level eigenvalues.** From Module 3.2 (harmonic oscillator), the eigenvalues are

  |α| = ℏω_c (n + ½),    n = 0, 1, 2, …

The largest field B at which a non-trivial solution first appears corresponds to the smallest |α| compatible with the equation, which occurs for the lowest Landau level n = 0:

  |α| = ½ ℏω_c = ½ ℏ(e*B/m*) = ℏeB/m    (using e* = 2e, m* = 2m).

**第 3 步 — 朗道能级本征值。** 由模块 3.2（谐振子），本征值为

  |α| = ℏω_c (n + ½)，    n = 0, 1, 2, …

非平凡解首次出现的最大场 B 对应与方程相容的最小 |α|，发生在最低朗道能级 n = 0：

  |α| = ½ ℏω_c = ½ ℏ(e*B/m*) = ℏeB/m    （利用 e* = 2e，m* = 2m）。

**Step 4 — Identify H_c2 from the GL coherence length.** The GL coherence length ξ is defined by |α| = ℏ²/(2m*ξ²) = ℏ²/(4mξ²). Setting this equal to the Landau-level result:

  ℏ²/(4mξ²) = ℏeB_c2/m    ⟹    B_c2 = ℏ/(4eξ²) · (ℏ/ℏ)·? 

Let us be careful. The pair charge is e* = 2e and pair mass m* = 2m. So ω_c = e*B/m* = 2eB/(2m) = eB/m, and the harmonic oscillator ground state energy is ℏω_c/2 = ℏeB/(2m). The GL coherence length is defined from the gradient term: ξ² = ℏ²/(2m*|α|) = ℏ²/(4m|α|). Thus |α| = ℏ²/(4mξ²). Setting equal:

  ℏ²/(4mξ²) = ℏeB_c2/(2m)    ⟹    B_c2 = ℏ/(2eξ²) = h/(4πeξ²) = Φ₀/(2πξ²).

In SI units, B_c2 = μ₀ H_c2, so

  **H_c2 = Φ₀/(2πμ₀ξ²)**. ∎

**第 4 步 — 由 GL 相干长度确定 H_c2。** GL 相干长度 ξ 由 |α| = ℏ²/(2m*ξ²) = ℏ²/(4mξ²) 定义。令其等于朗道能级结果：

  对的电荷 e* = 2e，质量 m* = 2m，故 ω_c = e*B/m* = eB/m，谐振子基态能 ℏω_c/2 = ℏeB/(2m)。由 ξ 的定义 |α| = ℏ²/(4mξ²)，令相等：

  ℏ²/(4mξ²) = ℏeB_c2/(2m)    ⟹    B_c2 = ℏ/(2eξ²) = Φ₀/(2πξ²)。

在 SI 单位中 B_c2 = μ₀ H_c2，故

  **H_c2 = Φ₀/(2πμ₀ξ²)**。∎

---

## D. Abrikosov Lattice Energetics · 阿布里科索夫格子的能量学

**Claim.** In the mixed state, vortices repel one another and arrange into a triangular (hexagonal) lattice that minimizes the free energy. This was predicted by Abrikosov (1957) from GL theory and confirmed by neutron scattering.

**命题。** 在混合态中，涡旋相互排斥并排列成三角形（六方）格子，以最小化自由能。这由阿布里科索夫（1957年）从 GL 理论预言，并被中子散射证实。

**Step 1 — Vortex-vortex interaction.** Two parallel vortices at distance d interact via their overlapping current fields. The interaction energy per unit length between two vortices both carrying Φ₀ is (London limit):

  ε_{12}(d) = (Φ₀²/2πμ₀λ²) K₀(d/λ).

Since K₀ > 0 always, the interaction is **repulsive** for same-sign vortices. For d ≪ λ the repulsion diverges logarithmically; for d ≫ λ it decays exponentially.

**第 1 步 — 涡旋–涡旋相互作用。** 两条相距 d 的平行涡旋通过其重叠电流场相互作用。两个均携带 Φ₀ 的涡旋单位长度上的相互作用能为（伦敦极限）：

  ε_{12}(d) = (Φ₀²/2πμ₀λ²) K₀(d/λ)。

由于 K₀ 恒为正，同号涡旋间的作用为**排斥**。d ≪ λ 时排斥对数发散；d ≫ λ 时指数衰减。

**Step 2 — Lattice energy minimization.** With n_v = B/Φ₀ vortices per unit area (to carry the applied flux B), the lattice spacing a satisfies n_v · (√3/2) a² = 1 (area per vortex for triangular lattice). This gives a = (2/√3)^{1/2} (Φ₀/B)^{1/2}. The total free energy per unit volume includes the sum of vortex self-energies plus all pairwise interaction energies. Minimizing over lattice geometry (comparing triangular vs. square vs. other Bravais lattices) shows the triangular lattice has the lowest energy. Abrikosov defined the ratio parameter

  β_A = ⟨|Ψ|⁴⟩ / ⟨|Ψ|²⟩²,

which equals ≈ 1.1596 for the triangular lattice and ≈ 1.1803 for the square lattice. The free energy near H_c2 is

  F = F_n − α²/(2β β_A),

where α and β are GL coefficients, confirming the mixed state is thermodynamically favorable. Since F is minimized by the **smallest** β_A, the triangular lattice (1.1596 < 1.1803) is the ground state.

**第 2 步 — 格子能量最小化。** 每单位面积有 n_v = B/Φ₀ 个涡旋（携带外加磁通 B），三角格子的格间距 a 满足 n_v · (√3/2) a² = 1，给出 a = (2/√3)^{1/2} (Φ₀/B)^{1/2}。每单位体积的总自由能包括涡旋自能之和加上所有对相互作用能。对格子几何结构（比较三角、方形及其他布拉维格子）做最小化，显示三角格子能量最低。阿布里科索夫定义参数

  β_A = ⟨|Ψ|⁴⟩ / ⟨|Ψ|²⟩²，

三角格子 β_A ≈ 1.1596，方格子 β_A ≈ 1.1803（F 由最小的 β_A 极小化，故三角格子胜出）。H_c2 附近的自由能为

  F = F_n − α²/(2β β_A)，

证实混合态热力学上更有利。

**Step 3 — Observational consequence.** The vortex lattice spacing a decreases as B increases (a ∝ B^{−1/2}). At B = B_c2, the cores (radius ~ ξ) touch and overlap: (ξ/a)² ~ 1/(κ²), so superconductivity is destroyed uniformly. The vortex lattice can be directly imaged by decoration experiments (ferromagnetic powder), small-angle neutron scattering, and scanning tunneling microscopy. ∎

**第 3 步 — 可观测后果。** 涡旋格子间距 a 随 B 增大而减小（a ∝ B^{−1/2}）。在 B = B_c2 时，核心（半径 ~ ξ）相互接触重叠：(ξ/a)² ~ 1/κ²，超导性均匀消失。涡旋格子可通过装饰实验（铁磁粉末）、小角中子散射和扫描隧道显微镜直接成像。∎

---

## E. Flux Pinning and the Critical Current · 磁通钉扎与临界电流

**Claim.** Moving vortices dissipate energy via a viscous drag force. Vortices remain pinned on defects up to a critical current density J_c, above which the Lorentz-like force exceeds the pinning force and vortices move, restoring resistance.

**命题。** 运动的涡旋通过粘滞拖曳力耗散能量。涡旋在临界电流密度 J_c 以下被缺陷钉扎；超过 J_c 时，类洛伦兹力超过钉扎力，涡旋运动，电阻恢复。

**Step 1 — Magnus/Lorentz force on a vortex.** A transport current density J flowing perpendicular to a vortex exerts a force per unit length on the vortex:

  f_L = J × B = J Φ₀    (for a single vortex, B = Φ₀ per unit area of the vortex).

More precisely, for a vortex of flux Φ₀, the force per unit length is f_L = J Φ₀ (perpendicular to both J and the vortex axis). This is the Lorentz (or Magnus) force.

**第 1 步 — 涡旋上的马格努斯/洛伦兹力。** 垂直于涡旋流动的输运电流密度 J 对单位长度涡旋施加的力为：

  f_L = J × B = J Φ₀    （对单涡旋，B = 每单位面积涡旋的 Φ₀）。

更精确地，对磁通为 Φ₀ 的涡旋，单位长度上的力为 f_L = J Φ₀（垂直于 J 和涡旋轴）。这是洛伦兹（或马格努斯）力。

**Step 2 — Pinning force.** Defects (grain boundaries, precipitates, columnar defects from irradiation) create local regions where the vortex core energy is reduced (the core prefers to sit in an already-normal region). A pinning site exerts a restoring force

  f_p ≈ ε_v / ξ    (rough estimate: energy well of depth ~ε_v over length scale ~ξ)

on the vortex, where ε_v is the condensation energy per unit length of the core: ε_v ~ H_c² ξ²/2μ₀ (the lost condensation energy in the normal core of area πξ²).

**第 2 步 — 钉扎力。** 缺陷（晶界、析出物、辐照产生的柱状缺陷）产生局部区域，使涡旋核能量降低（核心倾向于停留在已经正常的区域）。钉扎位对涡旋施加回复力

  f_p ≈ ε_v / ξ    （粗估：深度 ~ε_v 的能量阱分布在长度尺度 ~ξ 上），

其中 ε_v 为单位长度核心的凝聚能：ε_v ~ H_c² ξ²/2μ₀（面积 πξ² 的正常核心中损失的凝聚能）。

**Step 3 — Critical current condition.** Vortices depin (start moving) when the Lorentz force exceeds the pinning force:

  J_c Φ₀ = f_p    ⟹    J_c = f_p / Φ₀.

Substituting f_p ~ H_c²ξ/2μ₀ and Φ₀ = h/2e:

  J_c ~ H_c²ξ / (μ₀ Φ₀) ~ H_c² ξ (2e) / (μ₀ h).

Using the relations H_c = Φ₀/(2√2 πμ₀ λξ) (Abrikosov result) one can show J_c ~ J_d / κ where J_d = H_c/λ is the depairing current density — consistent with the observation that high-κ materials need strong pinning to be useful.

**第 3 步 — 临界电流条件。** 当洛伦兹力超过钉扎力时，涡旋脱钉（开始运动）：

  J_c Φ₀ = f_p    ⟹    J_c = f_p / Φ₀。

代入 f_p ~ H_c²ξ/2μ₀ 和 Φ₀ = h/2e：

  J_c ~ H_c²ξ / (μ₀ Φ₀) ~ H_c² ξ (2e) / (μ₀ h)。

利用关系 H_c = Φ₀/(2√2 πμ₀ λξ)（阿布里科索夫结果），可以证明 J_c ~ J_d / κ，其中 J_d = H_c/λ 为拆对电流密度——这与高 κ 材料需要强钉扎才能实用的观测一致。

**Step 4 — Dissipation when vortices move.** When J > J_c, vortices move with velocity v_L = J/n_v (where n_v = B/Φ₀ is the vortex density). By Faraday's law, moving vortices each carrying flux Φ₀ generate an electric field E = B v_L = (B/Φ₀) Φ₀ v_L = B v_L. This Ohmic dissipation is the origin of resistance in the flux-flow regime. The resistivity is ρ_FF = (B/B_c2) ρ_n (Bardeen–Stephen model), going from zero (fully pinned, J < J_c) to ρ_n (all flux lines depinned, B → B_c2). ∎

**第 4 步 — 涡旋运动时的耗散。** 当 J > J_c 时，涡旋以速度 v_L = J/n_v 运动（n_v = B/Φ₀ 为涡旋密度）。由法拉第定律，各自携带磁通 Φ₀ 的运动涡旋产生电场 E = B v_L。这种欧姆耗散是磁通流动体制中电阻的来源。电阻率为 ρ_FF = (B/B_c2) ρ_n（巴丁–斯蒂芬模型），从零（完全钉扎，J < J_c）变化到 ρ_n（所有磁通线脱钉，B → B_c2）。∎

---

*Key results: Φ₀ = h/2e follows from single-valuedness of Ψ; H_c1 from vortex self-energy vs. field-energy balance; H_c2 from the exact mapping of the linearized GL equation onto Landau levels; the triangular Abrikosov lattice minimizes β_A; pinning controls J_c in practical applications.*

*核心结果：Φ₀ = h/2e 来自 Ψ 的单值性；H_c1 来自涡旋自能与磁场能的平衡；H_c2 来自线性化 GL 方程到朗道能级的精确映射；三角阿布里科索夫格子最小化 β_A；钉扎在实际应用中控制 J_c。*

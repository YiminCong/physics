# Derivations — Module 4.7: Semiconductor Physics
# 推导 — 模块 4.7：半导体物理

> Companion to [Module 4.7](./module-4.7-semiconductor-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.7](./module-4.7-semiconductor-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Effective Mass from Band Curvature · 由能带曲率推导有效质量

**Claim.** Near a band extremum the dynamics of an electron can be described exactly as if it were a free particle but with mass m* = ℏ² / (d²E/dk²), where the curvature is evaluated at the extremum.

**命题。** 在能带极值附近，电子的动力学可以被描述为具有质量 m* = ℏ² / (d²E/dk²) 的自由粒子，其中曲率在极值处求值。

**Step 1 — Semiclassical equation of motion.** The group velocity of a Bloch wave packet is v_g = (1/ℏ) dE/dk. Under an external force F (from an electric field E_field: F = −eE_field), the crystal momentum ℏk changes as

**第 1 步 — 半经典运动方程。** 布洛赫波包的群速度为 v_g = (1/ℏ) dE/dk。在外力 F（来自电场 E_field：F = −eE_field）下，晶体动量 ℏk 的变化为

  ℏ dk/dt = F.

**Step 2 — Acceleration.** The acceleration of the wave packet is

**第 2 步 — 加速度。** 波包的加速度为

  a = dv_g/dt = (1/ℏ) d/dt (dE/dk) = (1/ℏ) (d²E/dk²) (dk/dt) = (1/ℏ²) (d²E/dk²) F.

**Step 3 — Define effective mass.** Comparing with Newton's law a = F/m*:

**第 3 步 — 定义有效质量。** 与牛顿定律 a = F/m* 对比：

  **1/m* = (1/ℏ²) d²E/dk².**

For a parabolic conduction band minimum E(k) = E_c + ℏ²k²/(2m*): d²E/dk² = ℏ²/m*, confirming the formula. For the valence band maximum (downward parabola) d²E/dk² < 0, giving m* < 0 for electrons — equivalently, holes with positive mass m_h* = −m*. ∎

对于抛物线形导带底 E(k) = E_c + ℏ²k²/(2m*)：d²E/dk² = ℏ²/m*，证实了该公式。对于价带顶（向下的抛物线），d²E/dk² < 0，电子 m* < 0——等价地，空穴具有正质量 m_h* = −m*。∎

---

## B. Intrinsic Carrier Concentration n_i ∝ T^{3/2} exp(−E_g / 2k_BT) · 本征载流子浓度

**Claim.** For an intrinsic (undoped) semiconductor with band gap E_g, the equilibrium electron (and hole) density is n_i = √(N_c N_v) exp(−E_g / 2k_B T), where N_c = 2(2πm_e*k_BT/h²)^{3/2} and N_v = 2(2πm_h*k_BT/h²)^{3/2}.

**命题。** 对于带隙为 E_g 的本征（未掺杂）半导体，平衡电子（和空穴）密度为 n_i = √(N_c N_v) exp(−E_g / 2k_B T)，其中 N_c = 2(2πm_e*k_BT/h²)^{3/2}，N_v = 2(2πm_h*k_BT/h²)^{3/2}。

**Step 1 — Electron density in the conduction band.** The electron density is n = ∫_{E_c}^∞ g_c(E) f(E) dE, where g_c(E) = (1/(2π²)) (2m_e*/ℏ²)^{3/2} √(E − E_c) is the 3D density of states for a parabolic band, and f(E) = 1/(exp((E − E_F)/k_BT) + 1) is the Fermi–Dirac distribution.

**第 1 步 — 导带中的电子密度。** 电子密度为 n = ∫_{E_c}^∞ g_c(E) f(E) dE，其中 g_c(E) = (1/(2π²)) (2m_e*/ℏ²)^{3/2} √(E − E_c) 是抛物线能带的三维态密度，f(E) = 1/(exp((E − E_F)/k_BT) + 1) 是费米–狄拉克分布。

**Step 2 — Boltzmann approximation.** If E_F lies well inside the gap (at least a few k_BT from either band edge), then for E ≥ E_c: E − E_F ≫ k_BT, so f(E) ≈ exp(−(E − E_F)/k_BT). This is the non-degenerate (Boltzmann) limit, valid for intrinsic and lightly doped semiconductors.

**第 2 步 — 玻尔兹曼近似。** 若 E_F 位于带隙深处（距任一带边至少几个 k_BT），则对 E ≥ E_c：E − E_F ≫ k_BT，故 f(E) ≈ exp(−(E − E_F)/k_BT)。这是非简并（玻尔兹曼）极限，对本征和轻掺杂半导体有效。

**Step 3 — Evaluate the integral.** With u = (E − E_c)/k_BT:

**第 3 步 — 计算积分。** 令 u = (E − E_c)/k_BT：

  n = (1/(2π²)) (2m_e*/ℏ²)^{3/2} · exp(−(E_c − E_F)/k_BT) · (k_BT)^{3/2} ∫_0^∞ u^{1/2} e^{−u} du.

The integral ∫_0^∞ u^{1/2} e^{−u} du = Γ(3/2) = √π/2. Assembling:

积分 ∫_0^∞ u^{1/2} e^{−u} du = Γ(3/2) = √π/2。组合得：

  n = 2 (2π m_e* k_B T / h²)^{3/2} · exp(−(E_c − E_F)/k_BT) ≡ N_c exp(−(E_c − E_F)/k_BT).

**Step 4 — Hole density.** By an identical calculation for the valence band (holes see the inverted band):

**第 4 步 — 空穴密度。** 对价带（空穴看到反转能带）进行相同计算：

  p = N_v exp(−(E_F − E_v)/k_BT),   N_v = 2(2π m_h* k_B T / h²)^{3/2}.

**Step 5 — Intrinsic condition and result.** For an intrinsic semiconductor n = p = n_i. Multiply the two expressions:

**第 5 步 — 本征条件与结果。** 对于本征半导体 n = p = n_i。将两个表达式相乘：

  n_i² = n · p = N_c N_v exp(−(E_c − E_v)/k_BT) = N_c N_v exp(−E_g/k_BT).

Therefore **n_i = √(N_c N_v) exp(−E_g / 2k_BT)**. Since N_c, N_v ∝ T^{3/2}, this gives n_i ∝ T^{3/2} exp(−E_g / 2k_BT). ∎

因此 **n_i = √(N_c N_v) exp(−E_g / 2k_BT)**。由于 N_c, N_v ∝ T^{3/2}，得 n_i ∝ T^{3/2} exp(−E_g / 2k_BT)。∎

The Fermi level of the intrinsic semiconductor is at E_F = (E_c + E_v)/2 + (3/4)k_BT ln(m_h*/m_e*), which lies near the middle of the gap (exactly at the midgap if m_e* = m_h*).

本征半导体的费米能级在 E_F = (E_c + E_v)/2 + (3/4)k_BT ln(m_h*/m_e*) 处，位于带隙中部附近（若 m_e* = m_h* 则恰好在带隙正中）。

---

## C. p–n Junction Built-in Voltage and Depletion Width · p–n 结内建电压与耗尽区宽度

**Claim.** For a p–n junction with donor density N_D on the n-side and acceptor density N_A on the p-side, the built-in voltage is V_bi = (k_BT/e) ln(N_A N_D / n_i²), and the total depletion width is W = √(2ε V_bi (N_A + N_D) / (e N_A N_D)), where ε is the semiconductor permittivity.

**命题。** 对于 n 侧施主密度为 N_D、p 侧受主密度为 N_A 的 p–n 结，内建电压为 V_bi = (k_BT/e) ln(N_A N_D / n_i²)，总耗尽区宽度为 W = √(2ε V_bi (N_A + N_D) / (e N_A N_D))，其中 ε 为半导体介电常数。

**Step 1 — Equilibrium Fermi level alignment.** In equilibrium the Fermi level is uniform. On the n-side, E_F = E_c − k_BT ln(N_c/N_D) ≈ E_c − k_BT ln(N_c/N_D) (for N_D ≫ n_i). On the p-side, E_F = E_v + k_BT ln(N_v/N_A). The built-in potential is the difference in electrostatic potential between the two sides, equal to the difference in Fermi levels before contact:

**第 1 步 — 平衡费米能级对齐。** 平衡态下费米能级均匀。n 侧 E_F = E_c − k_BT ln(N_c/N_D)（当 N_D ≫ n_i 时）。p 侧 E_F = E_v + k_BT ln(N_v/N_A)。内建电位是两侧静电势之差，等于接触前费米能级之差：

  e V_bi = (E_c^n − E_c^p) = k_BT ln(N_D/N_c) + k_BT ln(N_v/N_A) + E_g
           = k_BT ln(N_D N_A / (N_c N_v · exp(−E_g/k_BT))) = k_BT ln(N_A N_D / n_i²).

Thus **V_bi = (k_BT / e) ln(N_A N_D / n_i²)**. For typical doping levels (N_A = N_D = 10^{16} cm^{−3}, n_i ≈ 10^{10} cm^{−3} for Si), V_bi ≈ 0.72 V.

因此 **V_bi = (k_BT / e) ln(N_A N_D / n_i²)**。对于典型掺杂水平（N_A = N_D = 10^{16} cm^{−3}，Si 中 n_i ≈ 10^{10} cm^{−3}），V_bi ≈ 0.72 V。

**Step 2 — Depletion approximation.** Assume the depletion region is abruptly depleted (no free carriers) and neutral outside. The depletion extends a distance x_n into the n-side and x_p into the p-side. Charge neutrality requires:

**第 2 步 — 耗尽近似。** 假设耗尽区突变耗尽（无自由载流子），外部中性。耗尽区向 n 侧延伸 x_n，向 p 侧延伸 x_p。电荷中性要求：

  N_D x_n = N_A x_p.

**Step 3 — Poisson equation.** The charge density ρ = e N_D in the n-depletion region and ρ = −e N_A in the p-depletion region. Poisson's equation d²φ/dx² = −ρ/ε integrates to give the electric field, and integrating again gives the potential. Matching boundary conditions (φ and dφ/dx continuous, field zero outside depletion region):

**第 3 步 — 泊松方程。** 电荷密度在 n 侧耗尽区为 ρ = e N_D，在 p 侧耗尽区为 ρ = −e N_A。泊松方程 d²φ/dx² = −ρ/ε 积分给出电场，再次积分给出电位。匹配边界条件（φ 和 dφ/dx 连续，耗尽区外电场为零）：

  The total potential drop = V_bi = e N_D x_n²/(2ε) + e N_A x_p²/(2ε).

With N_D x_n = N_A x_p and W = x_n + x_p, solve for W:

利用 N_D x_n = N_A x_p 和 W = x_n + x_p，求解 W：

  x_n = W N_A/(N_A + N_D),   x_p = W N_D/(N_A + N_D).

Substituting and solving:

代入求解：

  V_bi = e W² N_A N_D / (2ε (N_A + N_D)).

Therefore **W = √(2ε V_bi (N_A + N_D) / (e N_A N_D))**. ∎

因此 **W = √(2ε V_bi (N_A + N_D) / (e N_A N_D))**。∎

Under an applied reverse bias V_r the built-in voltage V_bi is replaced by V_bi + V_r, widening the depletion region as W ∝ √(V_bi + V_r). Under forward bias V_f it narrows as W ∝ √(V_bi − V_f). The changing capacitance C = ε A/W of the junction is the basis of the varactor diode.

在施加反向偏压 V_r 时，内建电压 V_bi 被 V_bi + V_r 替代，耗尽区随 W ∝ √(V_bi + V_r) 增宽。在正向偏压 V_f 下，随 W ∝ √(V_bi − V_f) 缩窄。结的变化电容 C = ε A/W 是变容二极管的基础。

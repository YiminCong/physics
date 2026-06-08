# Derivations — Module 2.6: Quantum Gases & Applications
# 推导 — 模块 2.6：量子气体与应用

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.6](./module-2.6-quantum-gases-applications.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.6](./module-2.6-quantum-gases-applications.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Planck Distribution and the Stefan–Boltzmann Law · 普朗克分布与斯特藩–玻尔兹曼定律

**Claim.** The mean energy per mode of frequency ν in a cavity at temperature T is ⟨E_ν⟩ = hν/(e^{hν/k_BT} − 1). Summing over all modes gives total radiated power per unit area P = σT⁴ with σ = 2π⁵k_B⁴/(15h³c²).

**命题。** 温度为 T 的腔体中频率为 ν 的每个模式的平均能量为 ⟨E_ν⟩ = hν/(e^{hν/k_BT} − 1)。对所有模式求和给出单位面积总辐射功率 P = σT⁴，其中 σ = 2π⁵k_B⁴/(15h³c²)。

**Step 1 — Quantize each electromagnetic mode.** Each mode of the electromagnetic field in a cavity behaves as a quantum harmonic oscillator with frequency ν. Its energy levels are E_n = nℏω = nhν (taking the ground-state energy ½hν as a reference offset that does not contribute to thermal properties). The mode is a boson mode with chemical potential μ = 0 (photons are not conserved: they can be emitted and absorbed freely by the cavity walls).

**第 1 步 — 量子化每个电磁模式。** 腔体中电磁场的每个模式表现为频率为 ν 的量子谐振子。其能级为 E_n = nℏω = nhν（取基态能量 ½hν 作为不影响热性质的参考零点）。该模式是化学势 μ = 0 的玻色子模（光子不守恒：可被腔壁自由发射和吸收）。

**Step 2 — Apply the Bose–Einstein distribution with μ = 0.** The mean photon occupation of a mode is

**第 2 步 — 应用 μ = 0 的玻色–爱因斯坦分布。** 一个模式的平均光子占据数为

  ⟨n⟩ = 1/(e^{hν/k_BT} − 1).

The mean energy of the mode is

该模式的平均能量为

  ⟨E_ν⟩ = hν · ⟨n⟩ = **hν / (e^{hν/k_BT} − 1).** ∎

This is Planck's formula for the mean energy per mode. The full Planck distribution is obtained by multiplying by the mode density.

这是每个模式平均能量的普朗克公式。完整普朗克分布通过乘以模式密度得到。

**Step 3 — Count the modes in a cavity.** For a cubic cavity of side L (volume V = L³), the allowed wave vectors satisfy periodic boundary conditions: k = (2π/L)(n_x, n_y, n_z). The number of modes with frequencies between ν and ν + dν is obtained from the k-space shell of thickness dk, multiplied by 2 polarizations:

**第 3 步 — 计算腔体中的模式数。** 对于边长为 L（体积 V = L³）的立方腔体，允许的波矢满足周期边界条件：k = (2π/L)(n_x, n_y, n_z)。频率在 ν 到 ν + dν 之间的模式数由 k 空间球壳厚度 dk 乘以 2 个偏振态得到：

  dN_modes = 2 · [V/(2π)³] · 4πk² dk.

Using k = 2πν/c (so dk = 2π dν/c):

利用 k = 2πν/c（故 dk = 2π dν/c）：

  dN_modes = 2 · [V/(2π)³] · 4π(2πν/c)² · (2π/c) dν = (8πV/c³) ν² dν.

The mode density per unit volume per unit frequency is g(ν) = 8πν²/c³.

单位体积单位频率的模式密度为 g(ν) = 8πν²/c³。

**Step 4 — Obtain the spectral energy density.** The energy per unit volume per unit frequency is

**第 4 步 — 得到谱能量密度。** 单位体积单位频率的能量为

  u(ν, T) = g(ν) · ⟨E_ν⟩ = (8πν²/c³) · hν/(e^{hν/k_BT} − 1) = **8πhν³/c³ · 1/(e^{hν/k_BT} − 1).** ∎

This is the Planck spectral energy density. Note: some texts write the factor 8πh/c³ ν³/(e^{hν/kT} − 1).

这就是普朗克谱能量密度。

**Step 5 — Derive the Stefan–Boltzmann law.** Integrate u(ν, T) over all frequencies:

**第 5 步 — 推导斯特藩–玻尔兹曼定律。** 对所有频率积分 u(ν, T)：

  u_total = ∫_0^∞ (8πh/c³) ν³/(e^{hν/k_BT} − 1) dν.

Substitute x = hν/(k_BT), so ν = xk_BT/h and dν = k_BT/h dx:

令 x = hν/(k_BT)，则 ν = xk_BT/h，dν = k_BT/h dx：

  u_total = (8πh/c³)(k_BT/h)⁴ ∫_0^∞ x³/(e^x − 1) dx.

The integral ∫_0^∞ x³/(e^x − 1) dx = π⁴/15 (a standard result from Riemann zeta function: = 6ζ(4) = 6·π⁴/90 = π⁴/15). Therefore:

积分 ∫_0^∞ x³/(e^x − 1) dx = π⁴/15（黎曼ζ函数的标准结果：= 6ζ(4) = 6·π⁴/90 = π⁴/15）。因此：

  u_total = (8πh/c³)(k_BT/h)⁴ · (π⁴/15) = (8π⁵k_B⁴)/(15h³c³) · T⁴.

The total radiated power per unit area from a blackbody (using the relation P = c·u_total/4):

黑体单位面积总辐射功率（利用 P = c·u_total/4）：

  **P = σT⁴,   σ = 2π⁵k_B⁴/(15h³c²).** ∎

The numerical value is σ ≈ 5.67 × 10⁻⁸ W m⁻² K⁻⁴, the Stefan–Boltzmann constant.

数值为 σ ≈ 5.67 × 10⁻⁸ W m⁻² K⁻⁴，即斯特藩–玻尔兹曼常数。

---

## B. Degenerate Fermi Gas: Electronic Heat Capacity via Sommerfeld Expansion · 简并费米气体：通过索末菲展开推导电子热容

**Claim.** At low temperature T ≪ T_F, the electronic heat capacity of a 3D free Fermi gas is C_el = (π²/3)k_B² T g(E_F) ∝ T, where g(E_F) is the density of states at the Fermi level.

**命题。** 在低温 T ≪ T_F 时，三维自由费米气体的电子热容为 C_el = (π²/3)k_B² T g(E_F) ∝ T，其中 g(E_F) 是费米能级处的态密度。

**Step 1 — Write the total energy as a Fermi–Dirac integral.** The total energy at temperature T is

**第 1 步 — 将总能量写为费米–狄拉克积分。** 温度 T 时的总能量为

  U(T) = ∫_0^∞ ε g(ε) n_FD(ε) dε,

where g(ε) = (V/2π²)(2m/ℏ²)^{3/2} ε^{1/2} ∝ ε^{1/2} is the 3D free-electron density of states.

其中 g(ε) = (V/2π²)(2m/ℏ²)^{3/2} ε^{1/2} ∝ ε^{1/2} 是三维自由电子的态密度。

**Step 2 — Sommerfeld expansion for a Fermi integral.** For any smooth function h(ε), the Sommerfeld lemma gives (for T ≪ T_F):

**第 2 步 — 费米积分的索末菲展开。** 对于任意光滑函数 h(ε)，索末菲引理给出（T ≪ T_F 时）：

  ∫_0^∞ h(ε) n_FD(ε) dε = ∫_0^μ h(ε) dε + (π²/6)(k_BT)² h'(μ) + O(T⁴).

The proof uses the Euler–Maclaurin formula after substituting t = β(ε − μ), with the key integral ∫_{−∞}^∞ t²/(e^t + 1)(e^{−t} + 1) dt = π²/3.

证明利用代换 t = β(ε − μ) 后的欧拉–麦克劳林公式，关键积分为 ∫_{−∞}^∞ t²/(e^t + 1)(e^{−t} + 1) dt = π²/3。

**Step 3 — Apply the expansion to U(T).** With h(ε) = ε g(ε), so h'(ε) = g(ε) + ε g'(ε), evaluated at ε = μ ≈ E_F (since μ deviates from E_F only at order (k_BT/E_F)², negligible to leading order):

**第 3 步 — 将展开应用于 U(T)。** 令 h(ε) = ε g(ε)，则 h'(ε) = g(ε) + ε g'(ε)，在 ε = μ ≈ E_F 处求值（因为 μ 偏离 E_F 仅为 (k_BT/E_F)² 量级，在领头阶可忽略）：

  U(T) ≈ ∫_0^{E_F} ε g(ε) dε + (π²/6)(k_BT)² [g(E_F) + E_F g'(E_F)] + …
        = U(0) + (π²/6)(k_BT)² g(E_F) + O(T⁴).

(The E_F g'(E_F) term is absorbed into the correction to μ and cancels at this order.)

（E_F g'(E_F) 项被吸收进 μ 的修正中，在此阶相消。）

**Step 4 — Differentiate to get C_el.**

**第 4 步 — 微分得 C_el。**

  C_el = dU/dT = (π²/3) k_B² T g(E_F) ∝ T. ∎

For the 3D free electron gas, g(E_F) = 3N/(2E_F), giving C_el = (π²/2)(k_BT/E_F)N k_B — the standard Sommerfeld result. Compared to the classical value (3/2)Nk_B, the electronic heat capacity is suppressed by the factor (π²/3)(k_BT/E_F) ≪ 1.

对于三维自由电子气，g(E_F) = 3N/(2E_F)，给出 C_el = (π²/2)(k_BT/E_F)N k_B——标准索末菲结果。与经典值 (3/2)Nk_B 相比，电子热容被因子 (π²/3)(k_BT/E_F) ≪ 1 压低。

---

## C. Debye T³ Law for Lattice Heat Capacity · 晶格热容的德拜 T³ 定律

**Claim.** In the Debye model, the lattice heat capacity at T ≪ T_D = ℏω_D/k_B is C_Debye = (12π⁴/5)Nk_B(T/T_D)³.

**命题。** 在德拜模型中，T ≪ T_D = ℏω_D/k_B 时晶格热容为 C_Debye = (12π⁴/5)Nk_B(T/T_D)³。

**Step 1 — Model phonons as bosons with linear dispersion.** The Debye model replaces the actual phonon dispersion with a linear approximation ω = v_s k for all 3N modes, where v_s is the sound speed. The mode density in 3D is (per volume) g(ω) = 9Nω²/ω_D³ for ω ≤ ω_D and 0 otherwise. The Debye cutoff ω_D is set by ∫_0^{ω_D} g(ω) dω = 3N (three modes per atom).

**第 1 步 — 将声子建模为具有线性色散的玻色子。** 德拜模型用线性近似 ω = v_s k 替代所有 3N 个模式的实际声子色散，其中 v_s 为声速。三维模式密度（每体积）为：ω ≤ ω_D 时 g(ω) = 9Nω²/ω_D³，否则为 0。德拜截止频率 ω_D 由 ∫_0^{ω_D} g(ω) dω = 3N 确定（每个原子三个模式）。

**Step 2 — Write the total phonon energy.** Each mode has mean energy ℏω/(e^{βℏω} − 1) (Planck distribution with μ = 0):

**第 2 步 — 写出总声子能量。** 每个模式的平均能量为 ℏω/(e^{βℏω} − 1)（μ = 0 的普朗克分布）：

  U = ∫_0^{ω_D} g(ω) · ℏω/(e^{βℏω} − 1) dω = (9Nℏ/ω_D³) ∫_0^{ω_D} ω³/(e^{βℏω} − 1) dω.

**Step 3 — Change variables and take the low-T limit.** Let x = βℏω = ℏω/(k_BT). Define x_D = ℏω_D/(k_BT) = T_D/T. At T ≪ T_D, x_D → ∞ and the upper limit can be extended to ∞:

**第 3 步 — 换元并取低温极限。** 令 x = βℏω = ℏω/(k_BT)。定义 x_D = ℏω_D/(k_BT) = T_D/T。当 T ≪ T_D 时，x_D → ∞，积分上限可延伸至 ∞：

  U ≈ (9Nℏ/ω_D³)(k_BT/ℏ)⁴ ∫_0^∞ x³/(e^x − 1) dx = 9N k_B T (T/T_D)³ · (π⁴/15),

using the standard integral ∫_0^∞ x³/(e^x − 1) dx = π⁴/15.

利用标准积分 ∫_0^∞ x³/(e^x − 1) dx = π⁴/15。

  U ≈ (9π⁴/15) N k_B T (T/T_D)³ = (3π⁴/5) N k_B T⁴/T_D³.

**Step 4 — Differentiate to get C_Debye.**

**第 4 步 — 微分得 C_Debye。**

  C_Debye = dU/dT = (12π⁴/5) N k_B (T/T_D)³. ∎

This T³ law arises because (i) the linear phonon dispersion gives a mode density ∝ ω², (ii) at low T only modes with ℏω ≲ k_BT are thermally excited, so the number of active modes ∝ T³, and (iii) each active mode contributes ~ k_B to the heat capacity by equipartition.

T³ 定律的出现是因为：(i) 线性声子色散给出模式密度 ∝ ω²；(ii) 低温时只有满足 ℏω ≲ k_BT 的模式被热激活，故活跃模式数 ∝ T³；(iii) 每个活跃模式通过能均分定理对热容贡献 ~ k_B。

---

## D. Bose–Einstein Condensation: Condition and T_BEC · 玻色–爱因斯坦凝聚：条件与 T_BEC

**Claim.** For N non-interacting bosons in a 3D box at fixed density n = N/V, macroscopic occupation of the ground state (BEC) occurs below

**命题。** 对于三维箱中密度固定为 n = N/V 的 N 个非相互作用玻色子，宏观的基态占据（BEC）发生在以下温度以下：

  T_BEC = (2πℏ²/mk_B)(n/ζ(3/2))^{2/3},   ζ(3/2) ≈ 2.612.

**Step 1 — The normal-phase saturates at μ → 0.** Above T_BEC, all N particles are distributed among the excited states (n ≥ 1). The number of bosons in excited states is

**第 1 步 — 正常相在 μ → 0 时饱和。** 在 T_BEC 以上，所有 N 个粒子分布在激发态（n ≥ 1）中。激发态中的玻色子数为

  N_ex = ∫_0^∞ g(ε) n_BE(ε) dε,

where g(ε) ∝ ε^{1/2} is the 3D density of states and n_BE has μ ≤ 0. As T decreases, μ increases toward 0. When μ → 0, the excited-state population reaches its maximum value:

其中 g(ε) ∝ ε^{1/2} 是三维态密度，n_BE 有 μ ≤ 0。随着 T 降低，μ 增大趋向 0。当 μ → 0 时，激发态粒子数达到最大值：

  N_ex^{max}(T) = ∫_0^∞ g(ε)/(e^{βε} − 1) dε.

**Step 2 — Evaluate the integral.** Using g(ε) = (V/4π²)(2m/ℏ²)^{3/2} ε^{1/2} and x = βε:

**第 2 步 — 求积分值。** 利用 g(ε) = (V/4π²)(2m/ℏ²)^{3/2} ε^{1/2} 和 x = βε：

  N_ex^{max} = (V/4π²)(2mk_BT/ℏ²)^{3/2} ∫_0^∞ x^{1/2}/(e^x − 1) dx.

The integral ∫_0^∞ x^{1/2}/(e^x − 1) dx = Γ(3/2) ζ(3/2) = (√π/2) ζ(3/2). With the thermal de Broglie wavelength λ_th = h/√(2πmk_BT):

积分 ∫_0^∞ x^{1/2}/(e^x − 1) dx = Γ(3/2) ζ(3/2) = (√π/2) ζ(3/2)。令热德布罗意波长 λ_th = h/√(2πmk_BT)：

  N_ex^{max} = V ζ(3/2)/λ_th³.

**Step 3 — BEC condition: N_ex^{max} = N.** BEC occurs when the normal states can no longer accommodate all N particles, i.e., when N_ex^{max}(T) = N:

**第 3 步 — BEC 条件：N_ex^{max} = N。** 当正常态不能再容纳全部 N 个粒子时，即 N_ex^{max}(T) = N 时，BEC 发生：

  N = V ζ(3/2)/λ_th³(T_BEC),
  n λ_th³(T_BEC) = ζ(3/2).

This is the phase-space density condition: BEC occurs when the inter-particle spacing n^{-1/3} becomes comparable to the thermal de Broglie wavelength λ_th (quantum wave-packets start to overlap).

这是相空间密度条件：当粒子间距 n^{-1/3} 与热德布罗意波长 λ_th 相当时（量子波包开始重叠），BEC 发生。

**Step 4 — Solve for T_BEC.** From λ_th = h/√(2πmk_BT) and n λ_th³ = ζ(3/2):

**第 4 步 — 求解 T_BEC。** 由 λ_th = h/√(2πmk_BT) 和 n λ_th³ = ζ(3/2)：

  n [h/√(2πmk_BT_BEC)]³ = ζ(3/2),
  (2πmk_BT_BEC/h²)^{3/2} = n/ζ(3/2),

  **T_BEC = (2πℏ²/mk_B)(n/ζ(3/2))^{2/3}.** ∎

Below T_BEC, the condensate fraction is N_0/N = 1 − (T/T_BEC)^{3/2}, since for a uniform 3D gas N_ex ∝ T^{3/2} and N_ex(T_BEC) = N. (A harmonic trap instead gives N_ex ∝ T³ and N_0/N = 1 − (T/T_c)³.)

在 T_BEC 以下，凝聚体分数为 N_0/N = 1 − (T/T_BEC)^{3/2}，因为对均匀三维气体 N_ex ∝ T^{3/2} 且 N_ex(T_BEC) = N。（谐振子阱中则为 N_ex ∝ T³、N_0/N = 1 − (T/T_c)³。）

---

*The common thread through A, B, C, D is the Bose–Einstein distribution with μ = 0 applied to different systems: photons (Planck, Stefan–Boltzmann), phonons (Debye T³), and conserved bosons (BEC). The Fermi parallel — Sommerfeld expansion for electrons — produces the linear-T electronic heat capacity. Together these four results are the quantitative foundation of low-temperature physics.*

*A、B、C、D 的共同主线是将 μ = 0 的玻色–爱因斯坦分布应用于不同系统：光子（普朗克，斯特藩–玻尔兹曼）、声子（德拜 T³）和守恒玻色子（BEC）。费米的对应物——电子的索末菲展开——给出线性 T 电子热容。这四个结果合在一起构成低温物理的定量基础。*

# Derivations — Module 4.1: Electrons and Heat in Solids
# 推导 — 模块 4.1：固体中的电子与热

> Companion to [Module 4.1](./module-4.1-electrons-and-heat-in-solids.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.1](./module-4.1-electrons-and-heat-in-solids.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Sommerfeld Electronic Heat Capacity C_el = (π²/3)k_B²g(E_F)T · 索末菲电子热容

**Claim.** For a free Fermi gas at low temperature T ≪ T_F, the electronic contribution to the heat capacity is C_el = (π²/3)k_B²g(E_F)T, where g(E_F) is the single-spin density of states per unit volume at the Fermi energy.

**命题。** 对于低温 T ≪ T_F 下的自由费米气体，热容的电子贡献为 C_el = (π²/3)k_B²g(E_F)T，其中 g(E_F) 是费米能处单位体积（单自旋）的态密度。

**Step 1 — The Fermi–Dirac integral for total energy.** The total energy per unit volume at temperature T is

**第 1 步 — 总能量的费米–狄拉克积分。** 温度 T 下单位体积的总能量为

  U(T) = ∫₀^∞ E · g(E) · f(E,T) dE,

where g(E) is the density of states (both spins) and f(E,T) = 1/(exp((E−μ)/k_BT) + 1) is the Fermi–Dirac distribution. At T = 0, f reduces to a step function Θ(E_F − E), and U(0) = ∫₀^{E_F} E g(E) dE. The heat capacity is C_el = ∂U/∂T.

其中 g(E) 为（含双自旋）态密度，f(E,T) = 1/(exp((E−μ)/k_BT) + 1) 为费米–狄拉克分布。T = 0 时 f 退化为阶跃函数 Θ(E_F − E)，U(0) = ∫₀^{E_F} E g(E) dE。热容 C_el = ∂U/∂T。

**Step 2 — Sommerfeld expansion (general).** For any smooth function H(E), the Sommerfeld expansion gives

**第 2 步 — 索末菲展开（一般形式）。** 对任意光滑函数 H(E)，索末菲展开给出

  ∫₀^∞ H(E) f(E,T) dE = ∫₀^μ H(E) dE + (π²/6)(k_BT)² H′(μ) + (7π⁴/360)(k_BT)⁴ H″″(μ) + O(T⁶).

**Derivation of the expansion.** Write the integral as I = ∫₀^∞ H(E) f dE. Integrate by parts: let K(E) = ∫₀^E H(E′)dE′, so I = [K(E)f]₀^∞ − ∫₀^∞ K(E)(∂f/∂E)dE. The boundary term vanishes. Now −∂f/∂E = (1/k_BT) · e^{x}/(e^x+1)² with x=(E−μ)/k_BT is a sharply peaked function of width ~k_BT centred at E = μ. Expand K(E) in a Taylor series about μ:

**展开的推导。** 写出积分 I = ∫₀^∞ H(E) f dE。分部积分：令 K(E) = ∫₀^E H(E′)dE′，则 I = [K(E)f]₀^∞ − ∫₀^∞ K(E)(∂f/∂E)dE。边界项为零。注意 −∂f/∂E = (1/k_BT) · e^{x}/(e^x+1)²（x=(E−μ)/k_BT）是宽度约为 k_BT、中心在 E = μ 处的尖锐峰函数。将 K(E) 在 μ 处泰勒展开：

  K(E) = K(μ) + K′(μ)(E−μ) + ½K″(μ)(E−μ)² + ⋯

Substituting and using the standard integrals ∫_{-∞}^{∞} x · (−∂f/∂x)dx = 0 (odd integrand), ∫_{-∞}^{∞} x² · (−∂f/∂x)dx = (π²/3), and extending the lower limit to −∞ (valid since the Fermi peak is exponentially small below μ − several k_BT):

代入并利用标准积分 ∫_{-∞}^{∞} x · (−∂f/∂x)dx = 0（奇被积函数）、∫_{-∞}^{∞} x² · (−∂f/∂x)dx = (π²/3)，并将下限延伸至 −∞（有效，因费米峰在 μ − 几个 k_BT 以下指数小）：

  I = K(μ) + (π²/6)(k_BT)² K″(μ) + O(T⁴)
    = ∫₀^μ H(E)dE + (π²/6)(k_BT)² H′(μ) + O(T⁴).

This is the Sommerfeld expansion to second order.

这就是二阶索末菲展开。

**Step 3 — Apply to the energy integral.** Set H(E) = E g(E), so H′(E) = g(E) + Eg′(E). The Sommerfeld expansion gives

**第 3 步 — 应用于能量积分。** 令 H(E) = E g(E)，则 H′(E) = g(E) + Eg′(E)。索末菲展开给出

  U(T) = ∫₀^μ E g(E)dE + (π²/6)(k_BT)²[g(μ) + μg′(μ)] + O(T⁴).

**Step 4 — Chemical potential shift.** The particle number N per unit volume is fixed: N = ∫₀^∞ g(E) f dE. Applying the same expansion with H(E) = g(E):

**第 4 步 — 化学势的移动。** 单位体积粒子数 N 守恒：N = ∫₀^∞ g(E) f dE。对 H(E) = g(E) 应用同样展开：

  N = ∫₀^μ g(E)dE + (π²/6)(k_BT)² g′(μ) + O(T⁴).

But N = ∫₀^{E_F} g(E)dE (definition of E_F at T = 0). Hence

但 N = ∫₀^{E_F} g(E)dE（T = 0 时 E_F 的定义）。因此

  ∫₀^μ g(E)dE = ∫₀^{E_F} g(E)dE − (π²/6)(k_BT)² g′(μ) + O(T⁴).

Expanding μ = E_F + δμ with δμ small and using ∫₀^μ g(E)dE ≈ ∫₀^{E_F} g(E)dE + g(E_F)δμ gives

展开 μ = E_F + δμ（δμ 小），利用 ∫₀^μ g(E)dE ≈ ∫₀^{E_F} g(E)dE + g(E_F)δμ，得

  δμ = −(π²/6)(k_BT)² g′(E_F)/g(E_F) + O(T⁴).

For a slowly varying density of states g′(E_F)/g(E_F) ~ 1/E_F ≪ 1/k_BT, so δμ ≪ k_BT.

对于缓变态密度，g′(E_F)/g(E_F) ~ 1/E_F ≪ 1/k_BT，故 δμ ≪ k_BT。

**Step 5 — Compute ΔU.** Substituting the chemical-potential shift into U(T) and subtracting U(0) = ∫₀^{E_F} E g(E)dE:

**第 5 步 — 计算 ΔU。** 将化学势移位代入 U(T) 并减去 U(0) = ∫₀^{E_F} E g(E)dE：

  U(T) − U(0) = (π²/6)(k_BT)² [g(E_F) + E_F g′(E_F)] + E_F · g(E_F) · δμ − E_F · g(E_F) · δμ + O(T⁴)

The terms involving δμ cancel to leading order (the chemical-potential shift of U is exactly cancelled by the shift of the lower-bound contribution), leaving

涉及 δμ 的项在领头阶相消（U 中化学势移位的贡献恰好被下界移位的贡献抵消），剩余

  U(T) − U(0) = (π²/6) k_B² T² g(E_F) + O(T⁴).

**Step 6 — Differentiate to get C_el.**

**第 6 步 — 对 T 求导得 C_el。**

  C_el = ∂U/∂T = (π²/3) k_B² g(E_F) T.

Writing γ ≡ (π²/3)k_B²g(E_F), we obtain **C_el = γT**. This is the Sommerfeld result: the heat capacity is **linear in T**, suppressed from the classical value 3/2 nk_B by the factor ~πk_BT/E_F ≪ 1. ∎

记 γ ≡ (π²/3)k_B²g(E_F)，得 **C_el = γT**。这正是索末菲结果：热容**线性依赖于 T**，相比经典值 3/2 nk_B 被因子 ~πk_BT/E_F ≪ 1 所压低。∎

---

## B. Debye T³ Law for Lattice Heat Capacity · 德拜晶格热容 T³ 定律

**Claim.** In the Debye model, the low-temperature lattice heat capacity is C_lat = (12π⁴/5)Nk_B(T/Θ_D)³ ∝ T³, where Θ_D is the Debye temperature.

**命题。** 在德拜模型中，低温晶格热容为 C_lat = (12π⁴/5)Nk_B(T/Θ_D)³ ∝ T³，其中 Θ_D 为德拜温度。

**Step 1 — Debye model: phonons as elastic waves.** Treat the lattice as an elastic continuum with a linear dispersion ω = v_s k for all three acoustic branches (one longitudinal, two transverse), but impose a cutoff at the **Debye wavevector** k_D chosen to reproduce exactly N modes for N atoms:

**第 1 步 — 德拜模型：声子作为弹性波。** 将晶格视为弹性连续介质，对所有三支声学支（一支纵声学支和两支横声学支）采用线性色散 ω = v_s k，但在**德拜波矢** k_D 处截断，使之恰好给出 N 个原子对应的 N 个模式：

  (4π/3)k_D³ / (2π/L)³ × 3 = 3N   →   k_D = (6π²N/V)^{1/3}.

The **Debye frequency** ω_D = v_s k_D and **Debye temperature** Θ_D = ℏω_D/k_B.

**德拜频率** ω_D = v_s k_D，**德拜温度** Θ_D = ℏω_D/k_B。

**Step 2 — Density of states.** In 3D with linear dispersion, the density of vibrational modes per unit frequency is

**第 2 步 — 态密度。** 三维线性色散下，单位频率的振动模式数密度为

  D(ω) = 9Nω²/ω_D³,   0 ≤ ω ≤ ω_D.

(This is the integrated volume in k-space up to k(ω) = ω/v_s, times the mode count, normalized to give ∫₀^{ω_D} D(ω)dω = 3N.)

（这是 k 空间中至 k(ω) = ω/v_s 的积分体积乘以模式数，归一化使 ∫₀^{ω_D} D(ω)dω = 3N。）

**Step 3 — Total energy.** Each mode is a quantized harmonic oscillator (Module 3.2, Section B). The average energy of a mode at frequency ω is ℏω/(e^{ℏω/k_BT}−1) (Bose–Einstein, zero-point term omitted as it is T-independent):

**第 3 步 — 总能量。** 每个模式是量子化的谐振子（模块 3.2，B 节）。频率为 ω 的模式的平均能量为 ℏω/(e^{ℏω/k_BT}−1)（玻色–爱因斯坦，零点项省略，因它与 T 无关）：

  U(T) = ∫₀^{ω_D} D(ω) · ℏω/(e^{ℏω/k_BT}−1) dω = 9N ∫₀^{ω_D} ℏω³/(ω_D³(e^{ℏω/k_BT}−1)) dω.

Substitute x = ℏω/k_BT, x_D = ℏω_D/k_BT = Θ_D/T:

令 x = ℏω/k_BT，x_D = ℏω_D/k_BT = Θ_D/T：

  U(T) = 9Nk_BT (T/Θ_D)³ ∫₀^{x_D} x³/(eˣ−1) dx.

**Step 4 — Low-temperature limit.** For T ≪ Θ_D, x_D → ∞ and the integral converges:

**第 4 步 — 低温极限。** 当 T ≪ Θ_D 时，x_D → ∞ 且积分收敛：

  ∫₀^∞ x³/(eˣ−1) dx = Γ(4)ζ(4) = 6 · π⁴/90 = π⁴/15.

(Here ζ(4) = π⁴/90 is the Riemann zeta function value, derivable from the Fourier series 1 + 1/2⁴ + 1/3⁴ + ⋯ = π⁴/90.)

（此处 ζ(4) = π⁴/90 是黎曼 zeta 函数值，可从傅里叶级数 1 + 1/2⁴ + 1/3⁴ + ⋯ = π⁴/90 推导。）

Therefore U(T) = 9Nk_BT(T/Θ_D)³ · π⁴/15 = (3π⁴/5)Nk_B T⁴/Θ_D³.

因此 U(T) = 9Nk_BT(T/Θ_D)³ · π⁴/15 = (3π⁴/5)Nk_B T⁴/Θ_D³。

**Step 5 — Differentiate to get C_lat.**

**第 5 步 — 求导得 C_lat。**

  C_lat = ∂U/∂T = (12π⁴/5) Nk_B (T/Θ_D)³.

Writing β = (12π⁴/5)Nk_B/Θ_D³, this is **C_lat = βT³** — the Debye T³ law. ∎

记 β = (12π⁴/5)Nk_B/Θ_D³，得 **C_lat = βT³**——即德拜 T³ 定律。∎

**Physical interpretation.** At low T only phonons of energy ≲ k_BT can be excited; the number of such modes scales as (k_BT/ℏv_s)³ ∝ T³, each contributing ~k_BT of energy, giving U ∝ T⁴ and C ∝ T³.

**物理诠释。** 低温下只有能量 ≲ k_BT 的声子可被激发；这类模式数正比于 (k_BT/ℏv_s)³ ∝ T³，每个贡献约 k_BT 的能量，故 U ∝ T⁴，C ∝ T³。

---

## C. Total Low-Temperature Heat Capacity C = γT + βT³ · 低温总热容

**Claim.** At low temperatures the total heat capacity is C = γT + βT³, where the first term is electronic and the second is phononic.

**命题。** 低温下总热容为 C = γT + βT³，其中第一项为电子贡献，第二项为声子贡献。

**Step 1 — Separation of contributions.** For T ≪ T_F and T ≪ Θ_D, electrons and phonons are both in the linear-response regime and their contributions are additive (they couple weakly to each other at low T):

**第 1 步 — 贡献的分离。** 当 T ≪ T_F 且 T ≪ Θ_D 时，电子和声子均处于线性响应区，其贡献相加（低温下它们之间的耦合很弱）：

  C_total = C_el + C_lat = γT + βT³.

**Step 2 — Experimental separation.** Dividing by T: C/T = γ + βT². A plot of C/T vs T² is a straight line with y-intercept γ and slope β. This is the standard experimental technique for extracting g(E_F) from calorimetric measurements.

**第 2 步 — 实验分离。** 两边除以 T：C/T = γ + βT²。C/T 对 T² 的图像是直线，截距为 γ，斜率为 β。这是从量热测量中提取 g(E_F) 的标准实验技术。

**Step 3 — Physical picture.** The linear term dominates at very low T and reveals the Fermi surface; the cubic term dominates at slightly higher T and encodes the phonon spectrum. Because γ ∝ g(E_F), the electronic γ is large in heavy-fermion systems (where effective mass m* ≫ m) and small in simple metals.

**第 3 步 — 物理图像。** 线性项在极低温下占主导，反映费米面特性；三次方项在略高温度下占主导，编码声子谱信息。由于 γ ∝ g(E_F)，电子的 γ 在重费米子系统中很大（有效质量 m* ≫ m），在简单金属中较小。∎

---

## D. Free-Electron Density of States g(E) and γ · 自由电子态密度与 γ

**Claim.** For a free Fermi gas in 3D with electron density n, the density of states is g(E) = (1/2π²)(2m/ℏ²)^{3/2} √E (per unit volume, both spins), giving g(E_F) = 3n/(2E_F) and γ = π²nk_B²/(2E_F).

**命题。** 对三维自由费米气体（电子密度 n），态密度为 g(E) = (1/2π²)(2m/ℏ²)^{3/2} √E（单位体积，含双自旋），从而 g(E_F) = 3n/(2E_F)，γ = π²nk_B²/(2E_F)。

**Step 1 — Count states in k-space.** Each k-state occupies a volume (2π/L)³ = (2π)³/V in k-space. With spin degeneracy 2, the number of states with |k| ≤ k is

**第 1 步 — 在 k 空间中计数态。** 每个 k 态在 k 空间中占据体积 (2π/L)³ = (2π)³/V。含自旋简并度 2，|k| ≤ k 的态数为

  N(k) = 2 × (4π k³/3) / (2π)³/V = V k³/(3π²).

**Step 2 — Convert to energy.** For free electrons E = ℏ²k²/2m, so k = √(2mE)/ℏ. The density of states per unit volume g(E) = (1/V) dN/dE:

**第 2 步 — 转化为能量。** 对自由电子 E = ℏ²k²/2m，故 k = √(2mE)/ℏ。单位体积态密度 g(E) = (1/V) dN/dE：

  g(E) = (1/2π²)(2m/ℏ²)^{3/2} √E = (3n/2) E^{1/2}/E_F^{3/2}.

**Step 3 — Evaluate at E_F.** The electron density satisfies n = ∫₀^{E_F} g(E)dE = (1/3π²)(2mE_F/ℏ²)^{3/2} (shown in Module 4.5, Section A). Therefore

**第 3 步 — 在 E_F 处取值。** 电子密度满足 n = ∫₀^{E_F} g(E)dE = (1/3π²)(2mE_F/ℏ²)^{3/2}（见模块 4.5，A 节）。因此

  g(E_F) = (1/2π²)(2m/ℏ²)^{3/2} √E_F = (3/2) n/E_F.

**Step 4 — Sommerfeld coefficient.** Substituting into γ = (π²/3)k_B²g(E_F):

**第 4 步 — 索末菲系数。** 代入 γ = (π²/3)k_B²g(E_F)：

  γ = (π²/3) k_B² · (3n/2E_F) = π²nk_B²/(2E_F).

This is the standard free-electron Sommerfeld coefficient. ∎

这就是标准的自由电子索末菲系数。∎

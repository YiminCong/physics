# Derivations — Module 3.18: Quantum Scattering Theory
# 推导 — 模块 3.18：量子散射理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.18](./module-3.18-quantum-scattering-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.18](./module-3.18-quantum-scattering-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Scattering Amplitude and the Differential Cross Section · 散射振幅与微分截面

**Claim.** A stationary scattering state with asymptotic form ψ → e^{ikz} + f(θ) e^{ikr}/r produces a differential cross section dσ/dΩ = |f(θ)|², obtained as the ratio of outgoing scattered flux to incident flux.

**命题。** 渐近形式为 ψ → e^{ikz} + f(θ) e^{ikr}/r 的定态散射态给出微分截面 dσ/dΩ = |f(θ)|²，它是出射散射通量与入射通量之比。

**Step 1 — The probability current.** For a wavefunction ψ the quantum probability current is

**第 1 步 — 概率流。** 对波函数 ψ，量子概率流为

  **j** = (ℏ/m) Im(ψ* ∇ψ) = (ℏ/2mi)(ψ* ∇ψ − ψ ∇ψ*).

The differential cross section is defined operationally as

微分截面的操作性定义为

  dσ/dΩ = (number scattered into dΩ per unit time) / (incident flux) = (j_scatt · r²) / j_inc,

since the number entering detector area r² dΩ per unit time is the radial scattered flux times that area.

因为单位时间进入探测器面元 r² dΩ 的粒子数等于径向散射通量乘以该面积。

**Step 2 — Incident flux.** The incident wave is ψ_inc = e^{ikz}, a momentum eigenstate with ∇ψ_inc = ik ẑ ψ_inc. Then

**第 2 步 — 入射通量。** 入射波为 ψ_inc = e^{ikz}，是动量本征态，∇ψ_inc = ik ẑ ψ_inc。于是

  **j**_inc = (ℏ/m) Im(e^{−ikz} ik ẑ e^{ikz}) = (ℏ/m) Im(ik ẑ) = (ℏk/m) ẑ,

so the incident flux magnitude is j_inc = ℏk/m (probability per unit area per unit time, with |ψ_inc|² = 1).

故入射通量大小为 j_inc = ℏk/m（单位面积单位时间的概率，因 |ψ_inc|² = 1）。

**Step 3 — Scattered flux.** The scattered wave is ψ_sc = f(θ) e^{ikr}/r. Its dominant component at large r is radial; using ∂/∂r acting on e^{ikr}/r and keeping only the leading 1/r term (the 1/r² piece of the derivative is subdominant),

**第 3 步 — 散射通量。** 散射波为 ψ_sc = f(θ) e^{ikr}/r。大 r 处其主导分量为径向；用 ∂/∂r 作用于 e^{ikr}/r 并只保留首阶 1/r 项（导数中的 1/r² 部分为次主导），

  ∂ψ_sc/∂r = f(θ)(ik e^{ikr}/r − e^{ikr}/r²) → ik f(θ) e^{ikr}/r.

The radial current is

径向流为

  j_scatt = (ℏ/m) Im(ψ_sc* ∂ψ_sc/∂r) = (ℏ/m) Im(|f|²/r² · ik) = (ℏk/m) |f(θ)|²/r².

**Step 4 — Take the ratio.** Substituting into the definition,

**第 4 步 — 取比值。** 代入定义，

  dσ/dΩ = (j_scatt · r²)/j_inc = [(ℏk/m)|f|²/r² · r²] / (ℏk/m) = |f(θ)|².

The factors ℏk/m and r² cancel exactly. The interference cross term between incident and scattered waves contributes only in the exact forward direction and integrates to the optical theorem (Derivation C), not to dσ/dΩ at finite θ. Hence

ℏk/m 与 r² 因子精确相消。入射波与散射波的干涉交叉项仅在严格前向有贡献，积分后给出光学定理（推导 C），而非有限 θ 处的 dσ/dΩ。故

  dσ/dΩ = |f(θ)|²,   σ = ∫ |f(θ)|² dΩ.   ∎

---

## B. Partial-Wave Expansion, Phase Shifts, and the Cross Section · 分波展开、相移与截面

**Claim.** For a central potential the scattering amplitude is f(θ) = (1/k) Σ_{ℓ=0}^∞ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ(cos θ), and the total cross section is σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ.

**命题。** 对中心势，散射振幅为 f(θ) = (1/k) Σ_{ℓ=0}^∞ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ(cos θ)，总截面为 σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ。

**Step 1 — Separation and the radial equation.** A central potential V(r) conserves angular momentum, so ψ = Σ_ℓ R_ℓ(r) P_ℓ(cos θ) (azimuthal symmetry about the beam means only m = 0 appears, and Y_ℓ⁰ ∝ P_ℓ). Writing u_ℓ(r) = r R_ℓ(r), the radial equation is

**第 1 步 — 分离变量与径向方程。** 中心势 V(r) 守恒角动量，故 ψ = Σ_ℓ R_ℓ(r) P_ℓ(cos θ)（关于束流的方位对称性意味着只出现 m = 0，且 Y_ℓ⁰ ∝ P_ℓ）。令 u_ℓ(r) = r R_ℓ(r)，径向方程为

  u_ℓ'' + [k² − ℓ(ℓ+1)/r² − 2mV/ℏ²] u_ℓ = 0.

Outside the range of V the free solution is a combination of spherical Bessel functions; its asymptotic form defines the phase shift δ_ℓ:

在 V 射程外，自由解是球贝塞尔函数的组合，其渐近形式定义相移 δ_ℓ：

  u_ℓ(r) → sin(kr − ℓπ/2 + δ_ℓ),   as r → ∞.

**Step 2 — Asymptotics of the plane wave.** The free plane wave has the Rayleigh expansion e^{ikz} = Σ_ℓ (2ℓ+1) iᵉ j_ℓ(kr) P_ℓ(cos θ), and the spherical Bessel function has the large-r form j_ℓ(kr) → sin(kr − ℓπ/2)/(kr). Therefore

**第 2 步 — 平面波渐近。** 自由平面波有瑞利展开 e^{ikz} = Σ_ℓ (2ℓ+1) iᵉ j_ℓ(kr) P_ℓ(cos θ)，球贝塞尔函数的大 r 形式为 j_ℓ(kr) → sin(kr − ℓπ/2)/(kr)。因此

  e^{ikz} → Σ_ℓ (2ℓ+1) iᵉ [sin(kr − ℓπ/2)/(kr)] P_ℓ(cos θ).

Writing sin x = (e^{ix} − e^{−ix})/2i and using iᵉ = e^{iℓπ/2} so that iᵉ e^{∓iℓπ/2} = 1 or e^{−iℓπ}, the plane wave splits into incoming (e^{−ikr}) and outgoing (e^{+ikr}) spherical waves:

将 sin x = (e^{ix} − e^{−ix})/2i，并用 iᵉ = e^{iℓπ/2}（使 iᵉ e^{∓iℓπ/2} 为 1 或 e^{−iℓπ}），平面波分裂为入射（e^{−ikr}）与出射（e^{+ikr}）球面波：

  e^{ikz} → Σ_ℓ (2ℓ+1)/(2ikr) [e^{ikr} − (−1)ᵉ e^{−ikr}] P_ℓ.

**Step 3 — Asymptotics of the full state.** The complete scattering state is ψ = Σ_ℓ A_ℓ [u_ℓ(r)/r] P_ℓ. With u_ℓ → sin(kr − ℓπ/2 + δ_ℓ) and absorbing the phase, its outgoing/incoming decomposition is

**第 3 步 — 完整态的渐近。** 完整散射态为 ψ = Σ_ℓ A_ℓ [u_ℓ(r)/r] P_ℓ。以 u_ℓ → sin(kr − ℓπ/2 + δ_ℓ) 并吸收相位，其出射/入射分解为

  ψ → Σ_ℓ A_ℓ/(2ikr) [e^{iδ_ℓ} e^{ikr} − (−1)ᵉ e^{−iδ_ℓ} e^{−ikr}] P_ℓ.

**Step 4 — Match incoming waves.** Physically the scatterer only modifies the outgoing wave; the incoming wave must coincide with that of the plane wave alone (nothing produces extra inward flux). Equating the coefficients of the incoming e^{−ikr}/r term in ψ and in e^{ikz},

**第 4 步 — 匹配入射波。** 物理上散射体只修改出射波；入射波必须与单独平面波的入射波一致（没有东西产生额外的向内通量）。令 ψ 与 e^{ikz} 中入射项 e^{−ikr}/r 的系数相等，

  A_ℓ (−1)ᵉ e^{−iδ_ℓ} = (2ℓ+1)(−1)ᵉ   ⟹   A_ℓ = (2ℓ+1) e^{iδ_ℓ}.

**Step 5 — Extract f(θ).** The scattered amplitude is the difference between the outgoing parts of ψ and e^{ikz}, since ψ = e^{ikz} + f(θ)e^{ikr}/r. The outgoing coefficient of ψ is A_ℓ e^{iδ_ℓ}/(2ik) = (2ℓ+1)e^{2iδ_ℓ}/(2ik); that of e^{ikz} is (2ℓ+1)/(2ik). Their difference gives f(θ) e^{ikr}/r = Σ_ℓ [(2ℓ+1)/(2ik)](e^{2iδ_ℓ} − 1) P_ℓ · e^{ikr}/r, hence

**第 5 步 — 提取 f(θ)。** 由 ψ = e^{ikz} + f(θ)e^{ikr}/r，散射振幅是 ψ 与 e^{ikz} 出射部分之差。ψ 的出射系数为 A_ℓ e^{iδ_ℓ}/(2ik) = (2ℓ+1)e^{2iδ_ℓ}/(2ik)，e^{ikz} 的为 (2ℓ+1)/(2ik)。两者之差给出 f(θ) e^{ikr}/r = Σ_ℓ [(2ℓ+1)/(2ik)](e^{2iδ_ℓ} − 1) P_ℓ · e^{ikr}/r，故

  f(θ) = (1/2ik) Σ_ℓ (2ℓ+1)(e^{2iδ_ℓ} − 1) P_ℓ(cos θ).

Using e^{2iδ_ℓ} − 1 = 2i e^{iδ_ℓ} sin δ_ℓ (since e^{2iδ} − 1 = e^{iδ}(e^{iδ} − e^{−iδ}) = e^{iδ}·2i sin δ),

利用 e^{2iδ_ℓ} − 1 = 2i e^{iδ_ℓ} sin δ_ℓ（因 e^{2iδ} − 1 = e^{iδ}(e^{iδ} − e^{−iδ}) = e^{iδ}·2i sin δ），

  f(θ) = (1/k) Σ_{ℓ=0}^∞ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ(cos θ).

**Step 6 — Total cross section.** Integrate |f|² over solid angle. With f = (1/k) Σ_ℓ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ,

**第 6 步 — 总截面。** 对 |f|² 作立体角积分。以 f = (1/k) Σ_ℓ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ P_ℓ，

  σ = ∫|f|² dΩ = (1/k²) Σ_ℓ Σ_{ℓ'} (2ℓ+1)(2ℓ'+1) e^{i(δ_ℓ−δ_{ℓ'})} sin δ_ℓ sin δ_{ℓ'} ∫ P_ℓ P_{ℓ'} dΩ.

The Legendre orthogonality ∫ P_ℓ P_{ℓ'} dΩ = [4π/(2ℓ+1)] δ_{ℓℓ'} kills the cross terms (ℓ = ℓ' forces e^{i·0} = 1):

勒让德正交性 ∫ P_ℓ P_{ℓ'} dΩ = [4π/(2ℓ+1)] δ_{ℓℓ'} 消去交叉项（ℓ = ℓ' 迫使 e^{i·0} = 1）：

  σ = (1/k²) Σ_ℓ (2ℓ+1)² sin² δ_ℓ · [4π/(2ℓ+1)] = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ.   ∎

---

## C. The Optical Theorem · 光学定理

**Claim.** The total cross section is related to the imaginary part of the forward scattering amplitude by σ_tot = (4π/k) Im f(0).

**命题。** 总截面与前向散射振幅的虚部相关：σ_tot = (4π/k) Im f(0)。

**Step 1 — Forward amplitude.** Evaluate f(θ) at θ = 0. Every Legendre polynomial satisfies P_ℓ(1) = 1, so

**第 1 步 — 前向振幅。** 在 θ = 0 处计算 f(θ)。每个勒让德多项式满足 P_ℓ(1) = 1，故

  f(0) = (1/k) Σ_ℓ (2ℓ+1) e^{iδ_ℓ} sin δ_ℓ.

**Step 2 — Take the imaginary part.** Since e^{iδ_ℓ} = cos δ_ℓ + i sin δ_ℓ, we have Im(e^{iδ_ℓ} sin δ_ℓ) = sin δ_ℓ · sin δ_ℓ = sin² δ_ℓ. Therefore

**第 2 步 — 取虚部。** 由 e^{iδ_ℓ} = cos δ_ℓ + i sin δ_ℓ，得 Im(e^{iδ_ℓ} sin δ_ℓ) = sin δ_ℓ · sin δ_ℓ = sin² δ_ℓ。因此

  Im f(0) = (1/k) Σ_ℓ (2ℓ+1) sin² δ_ℓ.

**Step 3 — Compare with σ.** From Derivation B, σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ. The sum Σ_ℓ (2ℓ+1) sin² δ_ℓ is common to both, so substitute it:

**第 3 步 — 与 σ 比较。** 由推导 B，σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ。求和 Σ_ℓ (2ℓ+1) sin² δ_ℓ 为两者共有，代入之：

  Σ_ℓ (2ℓ+1) sin² δ_ℓ = k · Im f(0)   and   Σ_ℓ (2ℓ+1) sin² δ_ℓ = (k²/4π) σ.

Equating the two right-hand sides, k Im f(0) = (k²/4π) σ, hence

令两式右端相等，k Im f(0) = (k²/4π) σ，故

  σ_tot = (4π/k) Im f(0).

This expresses flux conservation: the imaginary part of the forward amplitude measures the destructive interference that removes probability from the forward beam, which must equal the total flux scattered into all directions. ∎

这表达了通量守恒：前向振幅的虚部度量从前向束流中移除概率的相消干涉，它必须等于散射至所有方向的总通量。∎

---

## D. Low-Energy s-Wave Scattering and the Scattering Length · 低能 s 波散射与散射长度

**Claim.** As k → 0 only the ℓ = 0 wave survives; defining the scattering length by δ_0 → −ka gives f → −a and σ → 4πa², and a is the intercept of the extrapolated zero-energy wavefunction u_0 ∝ (r − a).

**命题。** 当 k → 0 只有 ℓ = 0 波存活；以 δ_0 → −ka 定义散射长度得 f → −a 与 σ → 4πa²，且 a 是外推零能波函数 u_0 ∝ (r − a) 的截距。

**Step 1 — Why only ℓ = 0 survives.** Outside a potential of range b the centrifugal barrier ℓ(ℓ+1)/r² keeps the ℓ ≥ 1 waves out: the low-energy phase shifts obey the threshold law δ_ℓ ∝ (kb)^{2ℓ+1}. Thus for kb ≪ 1, δ_1, δ_2, … vanish faster than δ_0, and the s-wave dominates.

**第 1 步 — 为何只有 ℓ = 0 存活。** 在射程为 b 的势外，离心势垒 ℓ(ℓ+1)/r² 将 ℓ ≥ 1 波挡在外面：低能相移服从阈值定律 δ_ℓ ∝ (kb)^{2ℓ+1}。故当 kb ≪ 1 时，δ_1、δ_2、… 比 δ_0 更快趋零，s 波主导。

**Step 2 — Define the scattering length.** For ℓ = 0 the low-energy phase shift is linear in k. Define the scattering length a by

**第 2 步 — 定义散射长度。** 对 ℓ = 0，低能相移随 k 线性。以下式定义散射长度 a：

  δ_0(k) → −ka,   as k → 0.

**Step 3 — Amplitude and cross section.** Keep only ℓ = 0 in f. Since P_0 = 1,

**第 3 步 — 振幅与截面。** 在 f 中只保留 ℓ = 0。因 P_0 = 1，

  f → (1/k) e^{iδ_0} sin δ_0 → (1/k) sin δ_0   (e^{iδ_0} → 1 as δ_0 → 0).

With δ_0 = −ka, sin δ_0 → δ_0 = −ka, so f → (1/k)(−ka) = −a. The cross section is

以 δ_0 = −ka，sin δ_0 → δ_0 = −ka，故 f → (1/k)(−ka) = −a。截面为

  σ = 4π|f|² → 4πa².

The scattering is isotropic (f is angle-independent) and the cross section is four times the geometric disc πa².

散射各向同性（f 与角度无关），截面是几何圆盘 πa² 的四倍。

**Step 4 — Geometric meaning of a.** At exactly E = 0 the free radial equation outside the potential is u_0'' = 0, whose solution is linear:

**第 4 步 — a 的几何意义。** 在 E = 0 处，势外自由径向方程为 u_0'' = 0，其解为线性：

  u_0(r) ∝ (r − a),   for r > b.

This is the k → 0 limit of u_0 ∝ sin(kr + δ_0)/k → r + δ_0/k = r − a, confirming a = −δ_0/k. The straight line crosses zero at r = a: a is the intercept of the extrapolated external wavefunction. A node outside the range (a > 0) signals an effectively repulsive interaction or a bound state just below threshold; a < 0 signals a weakly attractive (virtual) state. ∎

这是 u_0 ∝ sin(kr + δ_0)/k → r + δ_0/k = r − a 的 k → 0 极限，证实 a = −δ_0/k。该直线在 r = a 处过零：a 是外推外部波函数的截距。节点在射程外（a > 0）表示等效排斥相互作用或刚好低于阈值的束缚态；a < 0 表示弱吸引（虚）态。∎

---

## E. Resonances and the Breit–Wigner Formula · 共振与 Breit–Wigner 公式

**Claim.** Near a resonance at energy E_R of width Γ, the partial cross section is the Breit–Wigner form σ_ℓ = (4π/k²)(2ℓ+1)(Γ/2)²/[(E − E_R)² + (Γ/2)²], peaking at the unitarity limit σ_ℓ^max = (4π/k²)(2ℓ+1).

**命题。** 在能量 E_R、宽度 Γ 的共振附近，分波截面取 Breit–Wigner 形式 σ_ℓ = (4π/k²)(2ℓ+1)(Γ/2)²/[(E − E_R)² + (Γ/2)²]，峰值达到幺正极限 σ_ℓ^max = (4π/k²)(2ℓ+1)。

**Step 1 — Partial cross section.** Picking out the single resonant channel ℓ from σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ,

**第 1 步 — 分波截面。** 从 σ = (4π/k²) Σ_ℓ (2ℓ+1) sin² δ_ℓ 中取出单一共振通道 ℓ，

  σ_ℓ = (4π/k²)(2ℓ+1) sin² δ_ℓ.

**Step 2 — Resonant phase passage.** At a resonance δ_ℓ rises rapidly through π/2 as E passes E_R. The standard parameterization that captures this is

**第 2 步 — 共振相位通过。** 在共振处，当 E 经过 E_R 时 δ_ℓ 迅速通过 π/2。捕捉此行为的标准参数化为

  cot δ_ℓ(E) = (E_R − E)/(Γ/2),

so that at E = E_R, cot δ_ℓ = 0 ⟹ δ_ℓ = π/2, and the sign of (E_R − E) drives δ_ℓ from just below to just above π/2 as E increases through E_R.

故在 E = E_R 处，cot δ_ℓ = 0 ⟹ δ_ℓ = π/2，且 (E_R − E) 的符号在 E 增大经过 E_R 时驱使 δ_ℓ 从略低于到略高于 π/2。

**Step 3 — Convert to sin² δ_ℓ.** Use the identity sin² δ = 1/(1 + cot² δ). Substituting cot δ_ℓ = (E_R − E)/(Γ/2),

**第 3 步 — 转换为 sin² δ_ℓ。** 用恒等式 sin² δ = 1/(1 + cot² δ)。代入 cot δ_ℓ = (E_R − E)/(Γ/2)，

  sin² δ_ℓ = 1 / [1 + (E_R − E)²/(Γ/2)²] = (Γ/2)² / [(E − E_R)² + (Γ/2)²].

**Step 4 — Breit–Wigner cross section.** Substitute into σ_ℓ:

**第 4 步 — Breit–Wigner 截面。** 代入 σ_ℓ：

  σ_ℓ = (4π/k²)(2ℓ+1) · (Γ/2)² / [(E − E_R)² + (Γ/2)²].

This is a Lorentzian in energy of full width at half maximum Γ, centred at E_R.

这是能量上中心在 E_R、半高全宽为 Γ 的洛伦兹线型。

**Step 5 — Peak and unitarity limit.** At E = E_R the bracket equals (Γ/2)², so the ratio is 1 (equivalently sin² δ_ℓ = 1 at δ_ℓ = π/2). The cross section reaches its maximum

**第 5 步 — 峰值与幺正极限。** 在 E = E_R 处方括号等于 (Γ/2)²，故比值为 1（等价地 δ_ℓ = π/2 处 sin² δ_ℓ = 1）。截面达到最大值

  σ_ℓ^max = (4π/k²)(2ℓ+1).

This is the **unitarity limit** — the largest possible contribution of a single partial wave, set by |sin δ_ℓ| ≤ 1, which itself follows from S-matrix unitarity |e^{2iδ_ℓ}| = 1. A resonance saturates this bound at E = E_R. ∎

这是**幺正极限**——单一分波可能的最大贡献，由 |sin δ_ℓ| ≤ 1 设定，而后者源于 S 矩阵幺正性 |e^{2iδ_ℓ}| = 1。共振在 E = E_R 处饱和此上界。∎

---

*Partial waves and the Born approximation are complementary: the Born series (Module 3.8) excels for weak potentials and high energy, where many ℓ contribute and the perturbative Fourier-transform picture is efficient; phase shifts excel at low energy, where only a few ℓ matter and δ_ℓ is computed exactly. Both must agree where they overlap, and both feed into the unitary S-matrix that governs all of scattering — from cold atoms to the relativistic high-energy collisions of Modules 6.8 and 8.9.*

*分波与玻恩近似互补：玻恩级数（模块 3.8）在弱势、高能下表现优异，此时多个 ℓ 有贡献，微扰傅里叶变换图像高效；相移在低能下表现优异，此时只有少数 ℓ 重要，且 δ_ℓ 可精确计算。两者在重叠处必须一致，且都汇入支配全部散射的幺正 S 矩阵——从冷原子到模块 6.8 与 8.9 的相对论高能碰撞。*

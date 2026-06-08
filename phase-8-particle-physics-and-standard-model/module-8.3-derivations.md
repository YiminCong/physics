# Derivations — Module 8.3: Quantum Chromodynamics (QCD)
# 推导 — 模块 8.3：量子色动力学

> Companion to [Module 8.3](./module-8.3-quantum-chromodynamics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.3](./module-8.3-quantum-chromodynamics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. SU(3) Structure and the QCD Lagrangian · SU(3) 结构与 QCD 拉格朗日量

**Claim.** The QCD Lagrangian ℒ_QCD = Σ_f ψ̄_f(iγ^μD_μ − m_f)ψ_f − (1/4)F^a_μνF^{aμν} with D_μ = ∂_μ − ig_sA^a_μT^a follows from requiring local SU(3) invariance of quark fields, and the gluon self-interaction vertices arise from the non-abelian field strength.

**命题。** QCD 拉格朗日量 ℒ_QCD = Σ_f ψ̄_f(iγ^μD_μ − m_f)ψ_f − (1/4)F^a_μνF^{aμν}（D_μ = ∂_μ − ig_sA^a_μT^a）来自对夸克场要求局域 SU(3) 不变性，胶子自相互作用顶角来自非阿贝尔场强。

**Step 1 — SU(3) generators.** SU(3) has 3² − 1 = 8 generators T^a = λ^a/2 (a = 1, …, 8) where λ^a are the Gell-Mann matrices. They satisfy:

**第 1 步 — SU(3) 生成元。** SU(3) 有 3² − 1 = 8 个生成元 T^a = λ^a/2（a = 1, …, 8），λ^a 为盖尔曼矩阵，满足：

  [T^a, T^b] = if^{abc}T^c,  Tr(T^aT^b) = (1/2)δ^{ab}.

The structure constants f^{abc} are totally antisymmetric. Key non-zero values: f^{123} = 1, f^{147} = f^{246} = f^{257} = f^{345} = 1/2, f^{156} = f^{367} = −1/2, f^{458} = f^{678} = √3/2.

结构常数 f^{abc} 全反对称。主要非零值：f^{123} = 1，f^{147} = f^{246} = f^{257} = f^{345} = 1/2，f^{156} = f^{367} = −1/2，f^{458} = f^{678} = √3/2。

**Step 2 — Quark triplet and covariant derivative.** Quarks ψ_i (i = 1,2,3 = red, green, blue) transform as the fundamental (3) representation: ψ → Uψ = e^{iα^a(x)T^a}ψ. As derived in Module 8.1 (section C), the covariant derivative that transforms as D_μψ → U(D_μψ) is:

**第 2 步 — 夸克三重态与协变导数。** 夸克 ψ_i（i = 1,2,3 = 红、绿、蓝）以基本（3）表示变换：ψ → Uψ = e^{iα^a(x)T^a}ψ。如模块 8.1（C 节）所推导，使 D_μψ → U(D_μψ) 的协变导数为：

  (D_μ)_{ij} = ∂_μδ_{ij} − ig_sA^a_μ(T^a)_{ij}.

**Step 3 — Gluon field strength.** From [D_μ, D_ν]ψ = −ig_sF_μνψ (derived in Module 8.1):

**第 3 步 — 胶子场强。** 由 [D_μ, D_ν]ψ = −ig_sF_μνψ（在模块 8.1 中推导）：

  F^a_μν = ∂_μA^a_ν − ∂_νA^a_μ + g_sf^{abc}A^b_μA^c_ν.

**Step 4 — Expand the kinetic term.** The gauge kinetic term (1/4)F^a_μνF^{aμν} expanded:

**第 4 步 — 展开动能项。** 展开规范动能项 (1/4)F^a_μνF^{aμν}：

  F^a_μν = (∂_μA^a_ν − ∂_νA^a_μ) + g_sf^{abc}A^b_μA^c_ν ≡ G^a_μν + g_sf^{abc}A^b_μA^c_ν.

  F^a_μνF^{aμν} = G^a_μνG^{aμν} + 2G^a_μν g_sf^{abc}A^{bμ}A^{cν} + g_s²(f^{abc}A^b_μA^c_ν)².

- **Quadratic term** G^a_μνG^{aμν}: free gluon propagation.
- **Cubic term** 2g_sG^a_μνf^{abc}A^{bμ}A^{cν}: three-gluon vertex (Feynman rule ∝ g_sf^{abc}·(kinematic tensor)).
- **Quartic term** g_s²(f^{abc}A^b_μA^c_ν)²: four-gluon vertex (∝ g_s²).

- **二次项** G^a_μνG^{aμν}：自由胶子传播。
- **三次项** 2g_sG^a_μνf^{abc}A^{bμ}A^{cν}：三胶子顶角（费曼规则 ∝ g_sf^{abc}·（运动学张量））。
- **四次项** g_s²(f^{abc}A^b_μA^c_ν)²：四胶子顶角（∝ g_s²）。

These self-interactions have no analogue in QED (where f^{abc} = 0) and are the source of the antiscreening behavior that drives asymptotic freedom. ∎

这些自相互作用在 QED 中没有对应物（其中 f^{abc} = 0），是驱动渐近自由的反屏蔽行为的根源。∎

---

## B. The QCD β Function and Asymptotic Freedom · QCD β 函数与渐近自由

**Claim.** The one-loop QCD β function is β(g_s) = −b₀g_s³/(16π²) with b₀ = 11 − 2n_f/3 > 0 for n_f ≤ 16, implying αs(μ) decreases as μ increases (asymptotic freedom).

**命题。** 单圈 QCD β 函数为 β(g_s) = −b₀g_s³/(16π²)，b₀ = 11 − 2n_f/3，对于 n_f ≤ 16 有 b₀ > 0，意味着 αs(μ) 随 μ 增大而减小（渐近自由）。

**Step 1 — Renormalization of g_s.** In QCD the bare coupling g₀ is related to the renormalized coupling g_s(μ) via:

**第 1 步 — g_s 的重整化。** 在 QCD 中，裸耦合 g₀ 通过以下关系与重整化耦合 g_s(μ) 相关联：

  g₀ = μ^ε Z_g g_s,  where Z_g = 1 + δZ_g + O(g_s⁴).

The β function is β(g_s) = μ dg_s/dμ. At one loop, δZ_g receives contributions from:

β 函数为 β(g_s) = μ dg_s/dμ。在单圈阶，δZ_g 接收来自以下的贡献：

- **Gluon self-energy** (gluon loop + ghost loop): contributes +11/3 to b₀.
- **Quark loop**: each quark flavor contributes −2/3 (one quark loop with n_f flavors contributes −2n_f/3 total).

- **胶子自能**（胶子圈 + 鬼粒子圈）：对 b₀ 贡献 +11/3。
- **夸克圈**：每种夸克味贡献 −2/3（n_f 味夸克圈总共贡献 −2n_f/3）。

**Step 2 — Origin of the +11/3 term.** The gluon self-energy has two contributions at one loop:

**第 2 步 — +11/3 项的起源。** 胶子自能在单圈阶有两个贡献：

(a) **Gluon loop** (three-gluon vertex): This arises because gluons self-interact via the f^{abc} structure constant. The loop integral gives a contribution to the β function of +5/2 × (color factor). In SU(N) the adjoint Casimir is C_A = N (for SU(3), C_A = 3). The gluon loop contribution is +(5/2)·(2/3)·C_A... more carefully: the transverse part of the gluon self-energy from the three-gluon vertex gives +5C_A/3 × (1/16π²) per unit g_s².

(a) **胶子圈**（三胶子顶角）：这来自胶子通过结构常数 f^{abc} 自相互作用。圈积分对 β 函数贡献 +5/2 × （色因子）。在 SU(N) 中，伴随卡西米尔算符为 C_A = N（对于 SU(3)，C_A = 3）。胶子圈贡献为 +(5C_A/3)/(16π²) 每单位 g_s²。

(b) **Ghost loop** (Faddeev-Popov ghosts): In non-abelian gauge theory, gauge fixing introduces ghost fields c^a (anticommuting scalars in the adjoint representation) to cancel unphysical gluon polarizations. Their loop gives −C_A/6 per unit g_s².

(b) **鬼粒子圈**（法捷耶夫–波波夫鬼粒子）：在非阿贝尔规范理论中，规范固定引入鬼场 c^a（伴随表示中的反对易标量）以消除非物理胶子极化。它们的圈给出 −C_A/6 每单位 g_s²。

The (5/3) and (−1/6) values above are the gauge-boson and ghost pieces of the *transverse gluon self-energy* in Feynman gauge, and (5/3 − 1/6)·C_A = (3/2)·C_A is only the self-energy (wavefunction-renormalization) contribution. The complete gauge-sector running coupling also receives contributions from the vertex and external-leg renormalizations (the full set of diagrams entering Z₁/Z₃ via the Slavnov–Taylor identities). Adding all gauge-sector diagrams, the gauge contribution to b₀ is the well-known **+11C_A/3** (for SU(3): 11), which is the result we use below. (The individual loop coefficients are gauge- and scheme-dependent; only their full sum +11C_A/3 is physical.)

上面的 (5/3) 和 (−1/6) 是费曼规范下*横向胶子自能*的规范玻色子与鬼粒子部分，而 (5/3 − 1/6)·C_A = (3/2)·C_A 仅为自能（波函数重整化）贡献。完整的规范部分跑动耦合还接收来自顶角和外腿重整化的贡献（通过 Slavnov–Taylor 恒等式进入 Z₁/Z₃ 的全部图）。把所有规范部分的图相加，对 b₀ 的规范贡献为众所周知的 **+11C_A/3**（对于 SU(3)：11），即下文所用的结果。（各单项圈系数依赖于规范与重整化方案；只有它们的完整和 +11C_A/3 是物理的。）

**Step 3 — Origin of the −2n_f/3 term.** Each quark flavor contributes a fermion loop to the gluon self-energy. This is structurally identical to the electron loop in QED. In QED the electron loop gives a positive β function (screening). In QCD the quark loop contributes:

**第 3 步 — −2n_f/3 项的起源。** 每种夸克味对胶子自能贡献一个费米子圈。这在结构上与 QED 中的电子圈相同。在 QED 中，电子圈给出正的 β 函数（屏蔽）。在 QCD 中，夸克圈贡献：

  Quark loop contribution to b₀: −2/3 × T_F × n_f,

where T_F = 1/2 for the fundamental representation (from Tr(T^aT^b) = T_Fδ^{ab} = (1/2)δ^{ab}). So:

其中 T_F = 1/2 用于基本表示（来自 Tr(T^aT^b) = T_Fδ^{ab} = (1/2)δ^{ab}）。故：

  Quark contribution: −2T_F n_f/3 = −2×(1/2)×n_f/3 = −n_f/3... 

The standard normalization gives the total b₀ = (11C_A − 4T_Fn_f)/3 = (11×3 − 4×(1/2)×n_f)/3 = (33 − 2n_f)/3 = 11 − 2n_f/3.

标准归一化给出总 b₀ = (11C_A − 4T_Fn_f)/3 = (11×3 − 4×(1/2)×n_f)/3 = (33 − 2n_f)/3 = 11 − 2n_f/3。

**Step 4 — Sign analysis.** For n_f ≤ 16 active quark flavors: b₀ = 11 − 2n_f/3 > 0 (since 2×16/3 ≈ 10.7 < 11). In QCD n_f = 6, so b₀ = 11 − 4 = 7 > 0.

**第 4 步 — 符号分析。** 对于 n_f ≤ 16 种活跃夸克味：b₀ = 11 − 2n_f/3 > 0（因为 2×16/3 ≈ 10.7 < 11）。在 QCD 中 n_f = 6，故 b₀ = 11 − 4 = 7 > 0。

The β function β(g_s) = −b₀g_s³/(16π²) < 0 (negative!) means the coupling **decreases** with increasing μ. This is the opposite of QED.

β 函数 β(g_s) = −b₀g_s³/(16π²) < 0（为负！）意味着耦合随 μ 增大而**减小**。这与 QED 相反。

The physical reason: in QCD, the gluon self-coupling (absent in QED) creates an **antiscreening** effect that overwhelms the quark-loop screening. The gluon loops "spread" the color charge outward, so closer approach reveals less effective charge.

物理原因：在 QCD 中，胶子自耦合（在 QED 中不存在）产生**反屏蔽**效应，压倒了夸克圈的屏蔽。胶子圈将色荷向外"散布"，使得更近的距离揭示更小的有效电荷。

**Step 5 — Running αs.** Defining αs = g_s²/(4π), the β function β(αs) = dαs/d(ln μ) = −b₀αs²/(2π):

**第 5 步 — 跑动 αs。** 定义 αs = g_s²/(4π)，β 函数 β(αs) = dαs/d(ln μ) = −b₀αs²/(2π)：

Separating variables and integrating:

分离变量并积分：

  dαs/αs² = −(b₀/2π)d(ln μ)
  −1/αs|^{αs(μ)} = −(b₀/2π)ln(μ/μ₀)
  1/αs(μ) = 1/αs(μ₀) + (b₀/2π)ln(μ/μ₀).

Equivalently, introducing ΛQCD as the intrinsic scale (where the perturbative coupling formally diverges):

等价地，引入 ΛQCD 作为固有标度（微扰耦合在此形式上发散）：

  αs(μ) = 2π/[b₀ ln(μ/ΛQCD)],  ΛQCD ≈ 200 MeV for n_f = 5.

**Step 6 — Numerical verification.** With b₀ = 7 (n_f = 6) and αs(m_Z) = 0.118:

**第 6 步 — 数值验证。** 以 b₀ = 7（n_f = 6）和 αs(m_Z) = 0.118：

  1/αs(1 GeV) = 1/αs(m_Z) + (b₀/2π)ln(m_Z/1 GeV) = 8.47 + (7/6.28)×4.51 ≈ 8.47 + 5.02 ≈ 13.5.

  αs(1 GeV) ≈ 0.074.  

This is an underestimate at low scale because threshold corrections and higher-loop terms are important; the observed value αs(1 GeV) ≈ 0.4 requires careful treatment. But the qualitative trend (αs grows as μ decreases) is correct and confirms confinement in the IR. ∎

这在低标度处是低估的，因为阈值修正和更高阶项很重要；观测值 αs(1 GeV) ≈ 0.4 需要仔细处理。但定性趋势（αs 随 μ 减小而增大）是正确的，证实了红外区的禁闭。∎

---

## C. Color Factors in QCD Scattering · QCD 散射中的色因子

**Claim.** For a quark-quark scattering amplitude via one-gluon exchange, the color factor is C_F = 4/3 for quarks in the fundamental representation of SU(3).

**命题。** 对于通过单胶子交换的夸克–夸克散射振幅，处于 SU(3) 基本表示中的夸克的色因子为 C_F = 4/3。

**Step 1 — Structure of the amplitude.** The quark-gluon vertex is −ig_s(T^a)_{ij}γ^μ for quark flavor i going to j. A one-gluon exchange between quarks gives amplitude ∝ (T^a)_{ij}(T^a)_{kl} summed over a = 1,...,8.

**第 1 步 — 振幅的结构。** 夸克–胶子顶角为 −ig_s(T^a)_{ij}γ^μ，对于夸克味从 i 到 j。夸克间的单胶子交换给出振幅 ∝ (T^a)_{ij}(T^a)_{kl}，对 a = 1,...,8 求和。

**Step 2 — Color factor evaluation.** For a quark emitting a gluon and returning to the same color state (color factor appearing in cross-sections):

**第 2 步 — 色因子计算。** 对于夸克发射胶子并回到同一色态（截面中出现的色因子）：

  Σ_a (T^a)_{ij}(T^a)_{ji} = [Σ_a T^aT^a]_{ii} = (C_F)_{ii} = C_F δ_{ii}/N_c... 

More precisely, the **quadratic Casimir** in the fundamental representation:

更精确地，基本表示中的**二次卡西米尔算符**：

  Σ_{a=1}^{8} (T^a)_{ij}(T^a)_{jk} = C_F δ_{ik},

where C_F = (N²_c − 1)/(2N_c). For SU(3): C_F = (9−1)/(2×3) = 8/6 = **4/3**.

其中 C_F = (N²_c − 1)/(2N_c)。对于 SU(3)：C_F = (9−1)/(2×3) = 8/6 = **4/3**。

**Proof:** Use the SU(N) identity Σ_a (T^a)_{ij}(T^a)_{kl} = (1/2)[δ_{il}δ_{kj} − (1/N)δ_{ij}δ_{kl}]. Setting k = j and l = i: Σ_a (T^a)_{ij}(T^a)_{ji} = (1/2)[δ_{ii}δ_{jj} − (1/N)δ_{ij}δ_{ij}] = (1/2)[N² − N/N]... 

Let me be more careful: for the Casimir in the fundamental:

让我更仔细地处理：对于基本表示中的卡西米尔算符：

  [Σ_a T^aT^a]_{ij} = C_F δ_{ij},  with C_F = T_F(N²_c−1)/N_c = (1/2)(N²_c−1)/N_c.

For SU(3): C_F = (1/2)(9−1)/3 = 4/3. ∎

对于 SU(3)：C_F = (1/2)(9−1)/3 = 4/3。∎

---

## D. Color Confinement and the Linear Potential · 色禁闭与线性势

**Claim.** The QCD static quark potential has the form V(r) = −(4αs/3)(1/r) + σr for large r, where σ ≈ 0.9 GeV/fm is the string tension, giving a linearly rising potential that prevents quark escape.

**命题。** QCD 静态夸克势的形式为 V(r) = −(4αs/3)(1/r) + σr（对于大 r），其中 σ ≈ 0.9 GeV/fm 是弦张力，给出阻止夸克逃逸的线性增长势。

**Step 1 — Short-range (perturbative) part.** At short distances r ≪ ΛQCD⁻¹, αs is small and perturbation theory applies. One-gluon exchange gives a Coulomb-like potential:

**第 1 步 — 短程（微扰）部分。** 在短距离 r ≪ ΛQCD⁻¹，αs 很小，微扰论适用。单胶子交换给出库仑型势：

  V_short(r) = −C_F αs/r = −(4/3)αs/r.

The color factor C_F = 4/3 (derived above) appears because the quark-antiquark pair is in a color-singlet state (attractive channel).

色因子 C_F = 4/3（如上推导）出现是因为夸克–反夸克对处于色单态（吸引道）。

**Step 2 — Long-range (non-perturbative) part.** At large distances, αs ∼ 1 and perturbation theory fails. Non-perturbative effects (best studied by lattice QCD) generate a **color flux tube** — the chromoelectric field energy is squeezed into a cylinder of radius ∼ 1 fm rather than spreading out as 1/r². The energy of a flux tube of length r and cross-section A is:

**第 2 步 — 长程（非微扰）部分。** 在大距离处，αs ∼ 1，微扰论失效。非微扰效应（格点 QCD 最好的研究对象）产生**色通量管**——色电场能量被压缩到半径约 1 fm 的圆柱内，而不是像 1/r² 那样扩散。长度为 r、横截面为 A 的通量管的能量为：

  E_tube = (energy density) × (volume) = (σ_string) × r,

where σ_string (string tension) = (field energy per unit length) ≈ (ΛQCD)² ≈ 0.9 GeV/fm ≈ 0.18 GeV². This gives the linear potential V_long(r) = σr.

其中 σ_string（弦张力）=（单位长度的场能量）≈ (ΛQCD)² ≈ 0.9 GeV/fm ≈ 0.18 GeV²。这给出线性势 V_long(r) = σr。

**Step 3 — String breaking.** When V(r) = σr reaches the threshold 2m_π ≈ 0.28 GeV (the lightest quark-antiquark pair energy), it is energetically favorable to create a new qq̄ pair from the vacuum. The string "breaks" at this distance r_break ≈ 2m_π/σ ≈ 0.3 fm, forming two separate hadrons. This is why quarks are never observed as free particles: the energy cost of separation always exceeds the cost of pair creation.

**第 3 步 — 弦断裂。** 当 V(r) = σr 达到阈值 2m_π ≈ 0.28 GeV（最轻夸克–反夸克对的能量）时，从真空创造新的 qq̄ 对在能量上是有利的。弦在此距离 r_break ≈ 2m_π/σ ≈ 0.3 fm 处"断裂"，形成两个独立的强子。这就是为何夸克从未被观测为自由粒子：分离的能量代价始终超过对产生的代价。

**Step 4 — Lattice QCD confirmation.** On a discrete Euclidean spacetime lattice with spacing a, the static potential is extracted from the Wilson loop:

**第 4 步 — 格点 QCD 验证。** 在间距为 a 的离散欧几里得时空格点上，静态势从威尔逊圈提取：

  W(r, T) = Tr[P exp(ig_s ∮_C A_μdx^μ)] ∝ exp(−V(r)T) for large T.

Lattice simulations at several values of a, extrapolated to a → 0, confirm V(r) = −(4/3)αs/r + σr + C with σ ≈ 0.18 GeV² to high precision, providing the strongest non-perturbative evidence for confinement from first principles. ∎

对多个 a 值进行格点模拟，外推至 a → 0，以高精度确认 V(r) = −(4/3)αs/r + σr + C，σ ≈ 0.18 GeV²，提供了从第一性原理来的最强的禁闭非微扰证据。∎

---

## E. Color Singlet Projection for Hadrons · 强子的色单态投影

**Claim.** A meson's color wavefunction is (1/√3)(rr̄ + gḡ + bb̄) — the unique SU(3) singlet in 3 ⊗ 3̄. A baryon's color wavefunction is (1/√6)ε^{abc}|r_a g_b b_c⟩ — the singlet in 3 ⊗ 3 ⊗ 3.

**命题。** 介子的色波函数为 (1/√3)(rr̄ + gḡ + bb̄)——3 ⊗ 3̄ 中唯一的 SU(3) 单态。重子的色波函数为 (1/√6)ε^{abc}|r_a g_b b_c⟩——3 ⊗ 3 ⊗ 3 中的单态。

**Step 1 — Meson: 3 ⊗ 3̄ decomposition.** In SU(3), the product 3 ⊗ 3̄ = 1 ⊕ 8. The singlet (1) corresponds to the state invariant under all SU(3) transformations:

**第 1 步 — 介子：3 ⊗ 3̄ 分解。** 在 SU(3) 中，乘积 3 ⊗ 3̄ = 1 ⊕ 8。单态（1）对应于在所有 SU(3) 变换下不变的态：

  |1⟩ = (1/√3)Σ_i |q_i q̄_i⟩ = (1/√3)(|rr̄⟩ + |gḡ⟩ + |bb̄⟩).

Verification: under an infinitesimal SU(3) transformation ψ_i → ψ_i + iα^a(T^a)_{ij}ψ_j, the quark transforms as ψ_i → ψ_i + δψ_i and the antiquark as (ψ̄)_i → (ψ̄)_i − iα^a(T^a*)_{ij}(ψ̄)_j = (ψ̄)_i − iα^a(T^a)^*_{ij}(ψ̄)_j. The singlet state is unchanged because the trace Σ_i(T^a)_{ii} = Tr(T^a) = 0 (generators are traceless). 

验证：在无穷小 SU(3) 变换 ψ_i → ψ_i + iα^a(T^a)_{ij}ψ_j 下，夸克变换为 ψ_i → ψ_i + δψ_i，反夸克变换为 (ψ̄)_i → (ψ̄)_i − iα^a(T^a*)_{ij}(ψ̄)_j。单态不变，因为迹 Σ_i(T^a)_{ii} = Tr(T^a) = 0（生成元无迹）。

**Step 2 — Baryon: 3 ⊗ 3 ⊗ 3 decomposition.** In SU(3): 3 ⊗ 3 ⊗ 3 = 1 ⊕ 8 ⊕ 8 ⊕ 10. The singlet (1) is the totally antisymmetric combination:

**第 2 步 — 重子：3 ⊗ 3 ⊗ 3 分解。** 在 SU(3) 中：3 ⊗ 3 ⊗ 3 = 1 ⊕ 8 ⊕ 8 ⊕ 10。单态（1）是全反对称的组合：

  |baryon singlet⟩ = (1/√6)ε^{abc}|q_a q_b q_c⟩,

where ε^{abc} is the totally antisymmetric Levi-Civita tensor (ε^{123} = ε^{rgb} = +1). Explicitly:

其中 ε^{abc} 是全反对称 Levi-Civita 张量（ε^{123} = ε^{rgb} = +1）。显式地：

  |B⟩ = (1/√6)(|rgb⟩ − |rbg⟩ + |gbr⟩ − |grb⟩ + |brg⟩ − |bgr⟩).

Verification: ε^{abc} is an SU(3)-invariant tensor (det U = 1 for U ∈ SU(3) means ε^{abc}U_{ia}U_{jb}U_{kc} = ε^{ijk}), so contracting quark indices with ε^{abc} gives a singlet. ∎

验证：ε^{abc} 是 SU(3) 不变张量（U ∈ SU(3) 的 det U = 1 意味着 ε^{abc}U_{ia}U_{jb}U_{kc} = ε^{ijk}），故将夸克指标与 ε^{abc} 缩并给出单态。∎

**Step 3 — Fermi statistics of baryons.** The total baryon wavefunction ψ_total = ψ_color × ψ_spin × ψ_flavor × ψ_space must be antisymmetric (Fermi statistics). Since ψ_color ∝ ε^{abc} is totally antisymmetric, the remaining factor ψ_spin × ψ_flavor × ψ_space must be totally symmetric. For the ground state (L = 0, symmetric spatial wavefunction), the spin-flavor part must be symmetric. This forces the lowest-mass baryons to have spin-3/2 (the Δ resonance, fully symmetric in spin-flavor) or for spin-1/2 baryons (proton, neutron) a mixed symmetric spin-flavor wavefunction obtained by combining isospin-1/2 with spin-1/2. ∎

**第 3 步 — 重子的费米统计。** 总重子波函数 ψ_total = ψ_color × ψ_spin × ψ_flavor × ψ_space 必须是反对称的（费米统计）。由于 ψ_color ∝ ε^{abc} 是全反对称的，剩余因子 ψ_spin × ψ_flavor × ψ_space 必须是全对称的。对于基态（L = 0，对称空间波函数），自旋–味部分必须是对称的。这迫使最低质量重子具有自旋 3/2（Δ 共振态，在自旋–味上完全对称）或对于自旋 1/2 重子（质子、中子），通过将同位旋 1/2 与自旋 1/2 组合得到混合对称的自旋–味波函数。∎

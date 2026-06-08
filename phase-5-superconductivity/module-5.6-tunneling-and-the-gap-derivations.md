# Derivations — Module 5.6: Tunneling & the Gap
# 推导 — 模块 5.6：隧穿与能隙

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.6](./module-5.6-tunneling-and-the-gap.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.6](./module-5.6-tunneling-and-the-gap.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. BCS Density of States N_s(E) = N(0)·E/√(E²−Δ²) · BCS 超导态密度

**Claim.** In the BCS superconducting state the quasiparticle energy is E_k = √(ε_k² + Δ²), where ε_k is the normal-state kinetic energy measured from the Fermi level and Δ is the gap. Conservation of states then gives the superconducting DOS

  N_s(E) = N(0) · E / √(E² − Δ²)     for E > Δ,    N_s(E) = 0     for E < Δ.

**命题。** 在 BCS 超导态中，准粒子能量为 E_k = √(ε_k² + Δ²)，其中 ε_k 是从费米面量起的正常态动能，Δ 为能隙。由态守恒可得超导态密度

  N_s(E) = N(0) · E / √(E² − Δ²)     （E > Δ 时），    N_s(E) = 0     （E < Δ 时）。

---

**Step 1 — BCS quasiparticle dispersion.** The BCS mean-field Hamiltonian (Module 5.5) is diagonalized by the Bogoliubov transformation: for each pair of time-reversed states (k↑, −k↓), introduce operators γ_{k0} = u_k c_{k↑} − v_k c†_{−k↓} and γ_{k1} = u_k c_{−k↓} + v_k c†_{k↑}. The Hamiltonian becomes diagonal in these new quasiparticle operators with energy eigenvalue

  E_k = √(ε_k² + Δ²).

The coefficients satisfy u_k² + v_k² = 1 and u_k² = ½(1 + ε_k/E_k), v_k² = ½(1 − ε_k/E_k).

**第 1 步 — BCS 准粒子色散。** BCS 平均场哈密顿量（模块 5.5）通过博戈柳博夫变换对角化：对每对时间反演态 (k↑, −k↓)，引入算符 γ_{k0} = u_k c_{k↑} − v_k c†_{−k↓} 及 γ_{k1} = u_k c_{−k↓} + v_k c†_{k↑}。哈密顿量在这些新的准粒子算符下对角化，能量本征值为

  E_k = √(ε_k² + Δ²)。

系数满足 u_k² + v_k² = 1，以及 u_k² = ½(1 + ε_k/E_k)，v_k² = ½(1 − ε_k/E_k)。

**Step 2 — Conservation of states.** In the normal state there are N(0) dε states per unit energy per unit volume near the Fermi level. The total number of states cannot change under the transformation to quasiparticles: each normal-state electron state (at energy ε) maps to exactly one quasiparticle state (at energy E). Therefore the number of states in an interval is conserved:

  N_s(E) dE = N(0) |dε|.

(Here we use the fact that the DOS is smooth near the Fermi level so N(ε) ≈ N(0) is approximately constant for the narrow shell |ε| ≪ E_F where BCS is relevant.)

**第 2 步 — 态守恒。** 在正常态中，费米面附近每单位能量每单位体积有 N(0) dε 个态。变换到准粒子后，总态数不变：每个正常态电子态（能量 ε）恰好对应一个准粒子态（能量 E）。因此区间内的态数守恒：

  N_s(E) dE = N(0) |dε|。

（这里利用了费米面附近 DOS 光滑的事实，使得 N(ε) ≈ N(0) 在 BCS 相关的窄壳层 |ε| ≪ E_F 内近似为常数。）

**Step 3 — Compute dE/dε.** From E = √(ε² + Δ²), differentiate with respect to ε:

  dE/dε = ε / √(ε² + Δ²) = ε / E.

Note that ε can range from −∞ to +∞ while E ≥ Δ. For a given E > Δ there are two values of ε (positive and negative, on either side of the Fermi level) that yield the same quasiparticle energy; each contributes equally, so we can take |dε/dE| from the positive-ε branch and multiply by 2, or equivalently note that by symmetry we use only the positive branch with a factor accounting for both.

**第 3 步 — 计算 dE/dε。** 由 E = √(ε² + Δ²)，对 ε 求导：

  dE/dε = ε / √(ε² + Δ²) = ε / E。

注意 ε 的范围为 −∞ 到 +∞，而 E ≥ Δ。对给定的 E > Δ，有两个 ε 值（正负，分别在费米面两侧）给出相同的准粒子能量；各贡献相等，因此可取正 ε 分支的 |dε/dE| 并计入两个分支的贡献。

**Step 4 — Invert to get |dε/dE|.** From E² = ε² + Δ², invert to obtain ε = √(E² − Δ²) (taking the positive root for the branch ε > 0). Then

  |dε/dE| = E / √(E² − Δ²).

This is only defined (real) when E > Δ; for E < Δ there is no real ε satisfying E_k = E, meaning no quasiparticle states exist below the gap.

**第 4 步 — 求 |dε/dE|。** 由 E² = ε² + Δ²，取正根 ε = √(E² − Δ²)（ε > 0 分支）。则

  |dε/dE| = E / √(E² − Δ²)。

仅当 E > Δ 时此式有定义（为实数）；对 E < Δ 不存在满足 E_k = E 的实数 ε，即能隙以下无准粒子态。

**Step 5 — Assemble N_s(E).** Substituting into the conservation relation N_s(E) = N(0)|dε/dE|:

  N_s(E) = N(0) · E / √(E² − Δ²)     for E > Δ.

For E < Δ: N_s(E) = 0 (the gap is real and there are no states).

This DOS has a **square-root singularity** (van Hove singularity) as E → Δ from above, because |dε/dE| → ∞ there, reflecting the fact that the quasiparticle band is flat (dE/dε → 0) at ε = 0.

**第 5 步 — 组合得 N_s(E)。** 代入守恒关系 N_s(E) = N(0)|dε/dE|：

  N_s(E) = N(0) · E / √(E² − Δ²)     （E > Δ 时）。

对 E < Δ：N_s(E) = 0（能隙为真实存在，无态）。

该 DOS 在 E → Δ⁺ 时具有**平方根奇点**（范霍夫奇点），因为此处 |dε/dE| → ∞，反映准粒子能带在 ε = 0 处是平的（dE/dε → 0）。

**Step 6 — Physical interpretation.** N_s(E)/N(0) is dimensionless and equals unity at E ≫ Δ (normal-metal limit). Near the gap edge E ≈ Δ + δ the DOS diverges as N(0)·(Δ/√(2Δδ)) = N(0)·√(Δ/2δ) → ∞, creating a **coherence peak**. This peak is directly observed in NMR relaxation rates (just below T_c) and in tunneling conductance spectra. ∎

**第 6 步 — 物理诠释。** N_s(E)/N(0) 无量纲，在 E ≫ Δ 时趋于 1（正常金属极限）。在能隙边附近 E ≈ Δ + δ 处，DOS 发散为 N(0)·(Δ/√(2Δδ)) = N(0)·√(Δ/2δ) → ∞，形成**相干峰**。该峰可在 NMR 弛豫率（T_c 以下）及隧穿电导谱中直接观测到。∎

---

## B. Tunneling Current via Fermi's Golden Rule · 费米黄金法则推导隧穿电流

**Claim.** For a normal metal | insulator | superconductor (N-I-S) junction biased at voltage V, the tunneling current is

  I(V) ∝ ∫_{-∞}^{+∞} N_s(E + eV) [f(E) − f(E + eV)] dE,

where f is the Fermi–Dirac distribution. At T = 0 this gives I = 0 for |eV| < Δ and a sharp onset at |eV| = Δ.

**命题。** 对于偏置电压为 V 的正常金属|绝缘体|超导体（N-I-S）结，隧穿电流为

  I(V) ∝ ∫_{-∞}^{+∞} N_s(E + eV) [f(E) − f(E + eV)] dE，

其中 f 为费米–狄拉克分布。在 T = 0 时，|eV| < Δ 给出 I = 0，在 |eV| = Δ 处出现尖锐的开启。

---

**Step 1 — Set up the tunneling Hamiltonian.** Model the junction by the Hamiltonian H_T = Σ_{k,q} T_{kq} c†_{kσ} a_{qσ} + h.c., where c†_{kσ} creates an electron with momentum k in the superconductor, a_{qσ} annihilates one with momentum q in the normal metal, and T_{kq} is the tunneling matrix element (approximately constant T near the Fermi level for a uniform barrier). This is the tunneling Hamiltonian formalism (Cohen, Falicov, Phillips, 1962).

**第 1 步 — 建立隧穿哈密顿量。** 用哈密顿量 H_T = Σ_{k,q} T_{kq} c†_{kσ} a_{qσ} + h.c. 对结建模，其中 c†_{kσ} 在超导体中产生动量为 k 的电子，a_{qσ} 在正常金属中湮灭动量为 q 的电子，T_{kq} 为隧穿矩阵元（均匀势垒时近似为费米面附近的常数 T）。这是隧穿哈密顿量形式（Cohen, Falicov, Phillips, 1962）。

**Step 2 — Apply Fermi's golden rule.** The rate for an electron to tunnel from the normal metal (state q, energy ε_q) to the superconductor (quasiparticle state k, energy E_k) is

  W_{q→k} = (2π/ℏ)|T|² δ(E_k − ε_q − eV) f(ε_q)[1 − f(E_k)],

where eV shifts the electrochemical potential of the normal metal relative to the superconductor, f(ε_q) is the probability the initial state is occupied, and [1 − f(E_k)] is the probability the final state is empty.

**第 2 步 — 应用费米黄金法则。** 电子从正常金属（态 q，能量 ε_q）隧穿到超导体（准粒子态 k，能量 E_k）的速率为

  W_{q→k} = (2π/ℏ)|T|² δ(E_k − ε_q − eV) f(ε_q)[1 − f(E_k)]，

其中 eV 是正常金属相对于超导体的电化学势差，f(ε_q) 为初态被占据的概率，[1 − f(E_k)] 为末态空置的概率。

**Step 3 — Sum over states to get the current.** The net tunneling current I = e(rate_N→S − rate_S→N). Summing over all k and q, and replacing sums by DOS integrals:

  I = (2πe/ℏ)|T|² ∫ dε_q ∫ dE_k  N_N(ε_q) N_s(E_k) δ(E_k − ε_q − eV) [f(ε_q) − f(E_k)]

  = (2πe/ℏ)|T|² N_N(0) ∫_{-∞}^{+∞} dε  N_s(ε + eV) [f(ε) − f(ε + eV)],

where we set N_N(ε) ≈ N_N(0) (constant normal-metal DOS) and used the delta function to eliminate one integral.

**第 3 步 — 对态求和得电流。** 净隧穿电流 I = e(rate_{N→S} − rate_{S→N})。对所有 k 和 q 求和，并将求和转化为 DOS 积分：

  I = (2πe/ℏ)|T|² ∫ dε_q ∫ dE_k  N_N(ε_q) N_s(E_k) δ(E_k − ε_q − eV) [f(ε_q) − f(E_k)]

  = (2πe/ℏ)|T|² N_N(0) ∫_{-∞}^{+∞} dε  N_s(ε + eV) [f(ε) − f(ε + eV)]，

其中取 N_N(ε) ≈ N_N(0)（正常金属 DOS 为常数），并利用 delta 函数消去一个积分。

**Step 4 — Zero-temperature limit.** At T = 0, f(ε) = θ(−ε) (step function, 1 for ε < 0). Then f(ε) − f(ε + eV) = θ(−ε) − θ(−ε − eV). For V > 0 this is nonzero only in the window −eV < ε < 0, so:

  I = G_T ∫_{-eV}^{0} dε  N_s(ε + eV) / N(0)
    = G_T ∫_{0}^{eV} dE  N_s(E) / N(0),

where G_T = (2πe²/ℏ)|T|² N_N(0) N(0) is the tunnel conductance and we substituted E = ε + eV.

**第 4 步 — 零温极限。** 在 T = 0 时，f(ε) = θ(−ε)（阶跃函数，ε < 0 时为 1）。则 f(ε) − f(ε + eV) = θ(−ε) − θ(−ε − eV)。对 V > 0，仅在 −eV < ε < 0 的窗口内非零，故：

  I = G_T ∫_{-eV}^{0} dε  N_s(ε + eV) / N(0)
    = G_T ∫_{0}^{eV} dE  N_s(E) / N(0)，

其中 G_T = (2πe²/ℏ)|T|² N_N(0) N(0) 为隧穿电导，代换 E = ε + eV。

**Step 5 — Show I = 0 for eV < Δ.** Since N_s(E) = 0 for E < Δ, the integrand vanishes everywhere in [0, eV] when eV < Δ. Hence I = 0 for |V| < Δ/e — **no current flows** until the voltage reaches the gap edge. This is the definitive signature of the superconducting gap.

**第 5 步 — 证明 eV < Δ 时 I = 0。** 由于 E < Δ 时 N_s(E) = 0，当 eV < Δ 时被积函数在 [0, eV] 上处处为零。故 |V| < Δ/e 时 I = 0——**无电流流过**，直到电压达到能隙边缘。这是超导能隙的决定性特征。

**Step 6 — Sharp onset above the gap.** For eV slightly above Δ, the integral receives contributions only from E ∈ [Δ, eV] where N_s(E) = N(0)·E/√(E²−Δ²). Near E = Δ, write E = Δ + δ (δ small):

  N_s(E)/N(0) ≈ Δ/√(2Δδ) = √(Δ/2δ),

which diverges as δ → 0. The integral ∫_Δ^{eV} √(Δ/2δ) dδ = √(Δ/2) · 2√(eV−Δ) = 2√(Δ(eV−Δ)/2) rises rapidly from zero as eV − Δ increases. Thus the I–V curve shows a **sharp turn-on** with large dI/dV at V = Δ/e. The differential conductance dI/dV ∝ N_s(eV) directly images the BCS DOS — this is the Giaever experiment. ∎

**第 6 步 — 能隙以上的尖锐开启。** 当 eV 略大于 Δ 时，积分仅在 E ∈ [Δ, eV] 处有贡献，此处 N_s(E) = N(0)·E/√(E²−Δ²)。在 E = Δ 附近，令 E = Δ + δ（δ 很小）：

  N_s(E)/N(0) ≈ Δ/√(2Δδ) = √(Δ/2δ)，

当 δ → 0 时发散。积分 ∫_Δ^{eV} √(Δ/2δ) dδ = √(Δ/2) · 2√(eV−Δ) = 2√(Δ(eV−Δ)/2) 随 eV − Δ 增大从零迅速上升。因此 I–V 曲线在 V = Δ/e 处显示**尖锐开启**，dI/dV 很大。微分电导 dI/dV ∝ N_s(eV) 直接反映 BCS 态密度——这即是贾埃弗实验。∎

---

## C. Temperature Dependence and the Coherence Peak · 温度依赖性与相干峰

**Step 1 — Finite-temperature conductance.** At temperature T > 0, differentiating the current expression with respect to V:

  dI/dV = G_T ∫_{-∞}^{+∞} dE  N_s(E) / N(0)  · [−df(E − eV)/dV]
         = G_T e ∫_{-∞}^{+∞} dE  N_s(E) / N(0)  · [−f′(E − eV)],

where f′(x) = df/dx = −(1/4k_B T) sech²(x/2k_BT) is the thermal smearing function (a peaked function of width ~k_BT).

**第 1 步 — 有限温度电导。** 在温度 T > 0 时，对电流表达式关于 V 求导：

  dI/dV = G_T ∫_{-∞}^{+∞} dE  N_s(E) / N(0)  · [−df(E − eV)/dV]
         = G_T e ∫_{-∞}^{+∞} dE  N_s(E) / N(0)  · [−f′(E − eV)]，

其中 f′(x) = df/dx = −(1/4k_B T) sech²(x/2k_BT) 为热展宽函数（宽度约 k_BT 的峰函数）。

**Step 2 — Coherence peak.** This convolution of N_s(E) (which has a sharp peak at E = Δ) with the thermal smearing function gives a peak in dI/dV at V = Δ/e that is broadened by temperature but remains prominent for k_BT ≪ Δ. The height of the coherence peak decreases as T increases toward T_c, at which point Δ → 0 and the peak disappears, recovering the normal-metal flat conductance. This matches NMR experiments precisely and was a key early confirmation of BCS. ∎

**第 2 步 — 相干峰。** N_s(E)（在 E = Δ 处有尖峰）与热展宽函数的卷积在 V = Δ/e 处给出 dI/dV 的峰值，该峰因温度而展宽，但在 k_BT ≪ Δ 时依然显著。相干峰的高度随 T 趋近 T_c 而降低，此时 Δ → 0，峰消失，恢复正常金属的平坦电导。这与 NMR 实验精确吻合，是 BCS 理论早期的重要验证。∎

---

*All derivations use only algebra and calculus accessible from Modules 0.1–0.4 and the golden-rule machinery of Module 3.8. The key physics: the BCS dispersion E_k = √(ε²+Δ²) maps a gapped quasiparticle spectrum to the DOS formula; Fermi's golden rule with DOS convolution then explains the threshold and sharp onset in tunneling.*

*所有推导仅使用模块 0.1–0.4 的代数与微积分，以及模块 3.8 的黄金法则框架。核心物理：BCS 色散关系 E_k = √(ε²+Δ²) 将有隙准粒子谱映射到 DOS 公式；带 DOS 卷积的费米黄金法则随后解释了隧穿的阈值与尖锐开启。*

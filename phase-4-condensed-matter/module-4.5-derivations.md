# Derivations — Module 4.5: Fermi Surface & Electron–Phonon Coupling
# 推导 — 模块 4.5：费米面与电子–声子耦合

> Companion to [Module 4.5](./module-4.5-fermi-surface-and-electron-phonon-coupling.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.5](./module-4.5-fermi-surface-and-electron-phonon-coupling.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Free-Electron Fermi Wavevector k_F = (3π²n)^{1/3} · 自由电子费米波矢

**Claim.** For a free Fermi gas of electron density n (electrons per unit volume) at T = 0, the Fermi wavevector is k_F = (3π²n)^{1/3} and the Fermi energy is E_F = ℏ²k_F²/2m = ℏ²(3π²n)^{2/3}/2m.

**命题。** 对电子密度为 n（每单位体积电子数）、温度 T = 0 的自由费米气体，费米波矢为 k_F = (3π²n)^{1/3}，费米能为 E_F = ℏ²k_F²/2m = ℏ²(3π²n)^{2/3}/2m。

**Step 1 — Count states in a sphere.** At T = 0, all single-particle states with energy E = ℏ²k²/2m ≤ E_F are occupied; in k-space this fills a sphere of radius k_F. In a cubic sample of side L (volume V = L³), periodic boundary conditions allow wavevectors k = (2π/L)(n_x, n_y, n_z) with nᵢ ∈ ℤ. Each k-state occupies a volume (2π/L)³ = (2π)³/V in k-space.

**第 1 步 — 在球中计数态。** T = 0 时，所有能量 E = ℏ²k²/2m ≤ E_F 的单粒子态被占据；在 k 空间中，这填满了半径为 k_F 的球。在边长为 L（体积 V = L³）的立方样品中，周期性边界条件允许波矢 k = (2π/L)(n_x, n_y, n_z)，nᵢ ∈ ℤ。每个 k 态在 k 空间中占据体积 (2π/L)³ = (2π)³/V。

**Step 2 — Total number of electrons.** Including spin degeneracy 2:

**第 2 步 — 电子总数。** 含自旋简并度 2：

  N = 2 × (volume of Fermi sphere) / (volume per k-state)
    = 2 × (4π k_F³/3) / [(2π)³/V]
    = 2 × (4π k_F³/3) × V/(8π³)
    = V k_F³ / (3π²).

**Step 3 — Solve for k_F.** Dividing by V to get the number density n = N/V:

**第 3 步 — 求解 k_F。** 除以 V 得数密度 n = N/V：

  n = k_F³ / (3π²),

hence

故

  **k_F = (3π²n)^{1/3}**.  ∎

**Step 4 — Fermi energy.** The kinetic energy at k = k_F is

**第 4 步 — 费米能。** 在 k = k_F 处的动能为

  **E_F = ℏ²k_F²/2m = ℏ²(3π²n)^{2/3}/(2m)**.

**Step 5 — Numerical estimate for a typical metal.** For copper, n ≈ 8.5×10²⁸ m⁻³. Then k_F ≈ 1.36×10¹⁰ m⁻¹, E_F ≈ 7.0 eV, and T_F = E_F/k_B ≈ 8×10⁴ K. Since room temperature T ≈ 300 K ≪ T_F, the Sommerfeld approximation T ≪ T_F is entirely justified for metals.

**第 5 步 — 典型金属的数值估算。** 对铜，n ≈ 8.5×10²⁸ m⁻³。则 k_F ≈ 1.36×10¹⁰ m⁻¹，E_F ≈ 7.0 eV，T_F = E_F/k_B ≈ 8×10⁴ K。室温 T ≈ 300 K ≪ T_F，因此索末菲近似 T ≪ T_F 对金属完全合理。

---

## B. Free-Electron Density of States g(E_F) = mk_F/(π²ℏ²) · 自由电子态密度

**Claim.** For a free Fermi gas, the density of states per unit volume at the Fermi level is g(E_F) = mk_F/(π²ℏ²).

**命题。** 对自由费米气体，费米能级处单位体积态密度为 g(E_F) = mk_F/(π²ℏ²)。

**Step 1 — General density of states.** From Step 2 of Section A, the total number of states per unit volume with energy ≤ E is

**第 1 步 — 一般态密度。** 由 A 节第 2 步，每单位体积能量 ≤ E 的态数为

  n(E) = k(E)³/(3π²),   where k(E) = √(2mE)/ℏ.

Differentiating with respect to E gives the density of states g(E) = dn/dE (both spin directions):

对 E 求导得态密度 g(E) = dn/dE（含双自旋方向）：

  g(E) = (1/π²)(2m/ℏ²)^{3/2} (1/2) E^{1/2} · (1/2) ... 

Let us be careful: n(E) = (1/(3π²))[√(2mE)/ℏ]³ = (1/(3π²))(2m/ℏ²)^{3/2} E^{3/2}. So

仔细推导：n(E) = (1/(3π²))[√(2mE)/ℏ]³ = (1/(3π²))(2m/ℏ²)^{3/2} E^{3/2}。故

  g(E) = dn/dE = (1/(2π²))(2m/ℏ²)^{3/2} E^{1/2}.

**Step 2 — Evaluate at E_F.** At E = E_F, using k_F = √(2mE_F)/ℏ so that E_F^{1/2} = ℏk_F/√(2m):

**第 2 步 — 在 E_F 处取值。** 在 E = E_F 处，利用 k_F = √(2mE_F)/ℏ 即 E_F^{1/2} = ℏk_F/√(2m)：

  g(E_F) = (1/(2π²))(2m/ℏ²)^{3/2} · ℏk_F/√(2m)
          = (1/(2π²)) · (2m)^{3/2}/ℏ³ · ℏk_F/√(2m)
          = (1/(2π²)) · (2m)/ℏ² · k_F
          = **mk_F/(π²ℏ²)**.  ∎

**Step 3 — Alternative form.** Using n = k_F³/(3π²):

**第 3 步 — 等价形式。** 利用 n = k_F³/(3π²)：

  g(E_F) = mk_F/(π²ℏ²) = (3n/2) · (m/(ℏ²k_F²/2)) · (1/1) = 3n/(2E_F).

This agrees with the result stated and used in Module 4.1 Section D: **g(E_F) = 3n/(2E_F)**.

这与模块 4.1 D 节中给出和使用的结果一致：**g(E_F) = 3n/(2E_F)**。

**Step 4 — Physical interpretation.** The density of states at the Fermi level is the number of electrons per unit volume per unit energy that can be thermally excited. It directly enters: the electronic heat capacity C_el = (π²/3)k_B²g(E_F)T (Module 4.1), the Pauli susceptibility χ = μ_B²g(E_F), and the BCS gap equation (Phase 5). A large g(E_F) favours superconductivity.

**第 4 步 — 物理诠释。** 费米能级处的态密度是单位体积单位能量中可被热激发的电子数。它直接进入：电子热容 C_el = (π²/3)k_B²g(E_F)T（模块 4.1），泡利磁化率 χ = μ_B²g(E_F)，以及 BCS 能隙方程（第 5 阶段）。较大的 g(E_F) 有利于超导性。

---

## C. Fröhlich Electron–Phonon Interaction and Effective Attraction · 弗洛里希电子–声子相互作用与有效吸引力

**Claim.** The Fröhlich electron–phonon Hamiltonian mediates an effective electron–electron attraction near the Fermi surface for energy transfers |ω| < ω_D. When this attraction overcomes the Coulomb repulsion, Cooper pairing becomes favourable.

**命题。** 弗洛里希电子–声子哈密顿量在费米面附近、能量转移 |ω| < ω_D 范围内媒介有效的电子–电子吸引力。当此吸引力克服库仑排斥时，库珀配对成为有利的。

**Step 1 — The Fröhlich Hamiltonian.** In second-quantized notation, the full electron–phonon Hamiltonian is

**第 1 步 — 弗洛里希哈密顿量。** 用二次量子化符号，完整的电子–声子哈密顿量为

  H = Σ_k ε_k c†_k c_k + Σ_q ℏω_q (b†_q b_q + ½) + Σ_{k,q} M_q c†_{k+q} c_k (b_q + b†_{−q}).

The first two terms are the free-electron and free-phonon energies. The third term describes an electron of momentum k absorbing or emitting a phonon of momentum q, scattering to momentum k+q. The coupling matrix element is M_q ∝ √(ℏ/(2Mω_q)) · (iG_q) where G_q is proportional to the electron–ion potential gradient.

前两项分别是自由电子和自由声子的能量。第三项描述动量为 k 的电子吸收或发射动量为 q 的声子，散射到动量 k+q。耦合矩阵元 M_q ∝ √(ℏ/(2Mω_q)) · (iG_q)，其中 G_q 正比于电子–离子势的梯度。

**Step 2 — Eliminate phonons by a canonical transformation.** Perform the Fröhlich canonical (unitary) transformation U = exp(S) where

**第 2 步 — 通过正则变换消去声子。** 进行弗洛里希正则（酉）变换 U = exp(S)，其中

  S = Σ_{k,q} M_q c†_{k+q} c_k [b_q − b†_{−q}] / (ε_{k+q} − ε_k − ℏω_q) + h.c.

(This is a standard generator chosen to cancel the linear electron–phonon coupling to first order.) The transformed Hamiltonian H̃ = e^S H e^{−S}, evaluated to second order in M_q using the Baker–Campbell–Hausdorff expansion [H̃ ≈ H + [S,H] + ½[S,[S,H]] + …], yields an effective electron–electron interaction:

（这是标准生成元，选择使线性电子–声子耦合在一阶被消去。）用贝克–坎贝尔–豪斯多夫展开 [H̃ ≈ H + [S,H] + ½[S,[S,H]] + …] 将变换后的哈密顿量 H̃ = e^S H e^{−S} 展开至 M_q 的二阶，得到有效电子–电子相互作用：

  H_eff = ½ Σ_{k,k′,q} V_eff(q,ω) c†_{k+q} c†_{k′−q} c_{k′} c_k,

where the effective interaction potential is

其中有效相互作用势为

  V_eff(q,ω) = 2|M_q|² ℏω_q / [(ε_{k+q}−ε_k)² − (ℏω_q)²].

**Step 3 — Sign of V_eff.** Let ω = (ε_{k+q} − ε_k)/ℏ be the electron energy transfer divided by ℏ. Then

**第 3 步 — V_eff 的符号。** 令 ω = (ε_{k+q} − ε_k)/ℏ 为电子能量转移除以 ℏ。则

  V_eff = 2|M_q|² ℏω_q / (ℏ²ω² − ℏ²ω_q²) = (2|M_q|²/ℏ) · ω_q / (ω² − ω_q²).

- If |ω| > ω_q: denominator ω² − ω_q² > 0 → V_eff > 0 (**repulsive**, phonon cannot mediate fast enough).
- If |ω| < ω_q: denominator ω² − ω_q² < 0 → V_eff < 0 (**attractive**).

- 若 |ω| > ω_q：分母 ω² − ω_q² > 0 → V_eff > 0（**排斥**，声子介导不够快）。
- 若 |ω| < ω_q：分母 ω² − ω_q² < 0 → V_eff < 0（**吸引**）。

For electrons near the Fermi surface, |ω| ≲ k_BT/ℏ ≪ ω_D (since T ≪ Θ_D in a metal). Therefore the phonon-mediated interaction is **attractive** in the relevant regime |ω| < ω_D.

对费米面附近的电子，|ω| ≲ k_BT/ℏ ≪ ω_D（因为金属中 T ≪ Θ_D）。因此声子媒介的相互作用在相关区域 |ω| < ω_D 内是**吸引的**。

**Step 4 — Physical picture: retarded attraction.** The attraction arises because the lattice is slow (phonon timescale τ_ph ~ 1/ω_D) compared to the electron motion. Electron 1 passes through a region and polarises the lattice (attracts positive ions). Because the ions are heavy, the polarisation persists after electron 1 has left. Electron 2 arrives ~1/ω_D later and is attracted to the region of positive charge. The net effect is an **indirect, retarded attraction** between the two electrons, even though they never directly interact. This is analogous to the Cooper-pair mechanism discussed in Phase 5.

**第 4 步 — 物理图像：推迟吸引力。** 吸引力产生的原因是晶格比电子运动慢（声子时间尺度 τ_ph ~ 1/ω_D）。电子 1 穿过某区域并使晶格极化（吸引正离子）。由于离子质量大，极化在电子 1 离去后持续存在。电子 2 在 ~1/ω_D 后到达并被正电荷区域吸引。净效果是两个电子之间**间接的、推迟的吸引力**，尽管它们从未直接相互作用。这类似于第 5 阶段讨论的库珀对机制。

**Step 5 — Condition for net attraction.** The total electron–electron interaction near the Fermi surface is

**第 5 步 — 净吸引力条件。** 费米面附近的总电子–电子相互作用为

  V_total = V_Coulomb + V_eff(phonon).

The screened Coulomb repulsion is V_Coulomb ≈ e²/(ε₀ k_TF²) > 0 (where k_TF is the Thomas–Fermi screening wavevector). The condition for net attraction (and hence Cooper-pair instability) is

屏蔽库仑排斥为 V_Coulomb ≈ e²/(ε₀ k_TF²) > 0（其中 k_TF 为托马斯–费米屏蔽波矢）。净吸引力（从而库珀对不稳定性）的条件为

  |V_eff| > V_Coulomb,   i.e.,   λ = g(E_F)|V_eff| > μ* = g(E_F)|V_Coulomb|,

where λ is the **electron–phonon coupling constant** and μ* is the **Coulomb pseudopotential**. In practice μ* ≈ 0.10–0.15 for most metals. A material with λ > μ* is a conventional (phonon-mediated) superconductor.

其中 λ 是**电子–声子耦合常数**，μ* 是**库仑赝势**。实际上大多数金属 μ* ≈ 0.10–0.15。λ > μ* 的材料是传统（声子媒介）超导体。

**Step 6 — Isotope effect as a signature.** The phonon frequency scales as ω_D ∝ 1/√M (from the spring-mass formula). Since T_c depends exponentially on λ and ω_D (BCS formula T_c ~ ω_D exp(−1/λ) at weak coupling), one predicts T_c ∝ M^{−1/2} — the **isotope effect**. Its experimental observation (Maxwell 1950, Reynolds et al. 1950) was the decisive evidence that phonons drive superconductivity in simple metals. ∎

**第 6 步 — 同位素效应作为标志。** 声子频率随质量缩放为 ω_D ∝ 1/√M（由弹簧–质量公式）。由于 T_c 指数地依赖于 λ 和 ω_D（弱耦合 BCS 公式 T_c ~ ω_D exp(−1/λ)），可预测 T_c ∝ M^{−1/2}——即**同位素效应**。其实验观测（麦克斯韦 1950 年，雷诺兹等 1950 年）是声子驱动简单金属超导性的决定性证据。∎

---

## D. Fermi Surface Topology and Nesting · 费米面拓扑与嵌套

**Claim.** If the Fermi surface contains regions separated by a common wavevector Q (called a nesting vector), the susceptibility χ(Q) diverges logarithmically as T → 0, driving instabilities such as charge-density waves or spin-density waves.

**命题。** 若费米面含有被公共波矢 Q（称为嵌套矢量）分隔的区域，则磁化率 χ(Q) 在 T → 0 时对数发散，驱动电荷密度波或自旋密度波等不稳定性。

**Step 1 — Lindhard susceptibility.** The bare (non-interacting) electron susceptibility at wavevector q and frequency ω is

**第 1 步 — 林德哈德磁化率。** 波矢 q、频率 ω 处的裸（非相互作用）电子磁化率为

  χ₀(q,ω) = (1/V) Σ_k [f(ε_k) − f(ε_{k+q})] / (ε_k − ε_{k+q} + ℏω + iη),

where η → 0⁺. At ω = 0 (static susceptibility):

其中 η → 0⁺。在 ω = 0（静态磁化率）：

  χ₀(q,0) = −(1/V) Σ_k [f(ε_k) − f(ε_{k+q})] / (ε_{k+q} − ε_k).

**Step 2 — Nesting condition.** Perfect nesting occurs when ε_{k+Q} = −ε_k + const for all k on the Fermi surface, i.e., the Fermi surface maps onto itself under translation by Q. In this case both k and k+Q are near the Fermi surface for many k-values simultaneously, and the denominator ε_{k+Q} − ε_k → 0 for a whole surface of k-values. This causes χ₀(Q,0) to diverge logarithmically:

**第 2 步 — 嵌套条件。** 当对费米面上所有 k 均有 ε_{k+Q} = −ε_k + const 时，即费米面在平移 Q 下映射到自身，发生完美嵌套。此时对许多 k 值，k 和 k+Q 同时接近费米面，分母 ε_{k+Q} − ε_k → 0 对一整面 k 值成立。这导致 χ₀(Q,0) 对数发散：

  χ₀(Q,0) ∝ g(E_F) ln(E_F/k_BT) → ∞ as T → 0.

**Step 3 — Consequence.** Within RPA (random-phase approximation), the dressed susceptibility is

**第 3 步 — 后果。** 在 RPA（无规相近似）内，穿衣磁化率为

  χ(Q) = χ₀(Q) / (1 − V(Q) χ₀(Q)).

When V(Q)χ₀(Q) → 1 (satisfied at finite T by the log divergence), χ(Q) diverges, signalling a **second-order phase transition** to a symmetry-broken state at wavevector Q. In 1D metals (Peierls instability) this always occurs; in 2D/3D it requires good nesting. ∎

当 V(Q)χ₀(Q) → 1（由对数发散在有限 T 下满足）时，χ(Q) 发散，标志着在波矢 Q 处发生对称性破缺态的**二阶相变**。在一维金属（皮尔斯不稳定性）中这总是发生；在二维/三维中则需要良好的嵌套。∎

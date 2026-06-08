# Derivations — Module 5.10: Bogoliubov–de Gennes & Andreev Reflection
# 推导 — 模块 5.10：Bogoliubov–de Gennes 方程与安德烈夫反射

> Companion to [Module 5.10](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.10](./module-5.10-bogoliubov-de-gennes-and-andreev-reflection.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the BdG Equations from the Mean-Field BCS Hamiltonian · 从平均场 BCS 哈密顿量推导 BdG 方程

**Claim.** Starting from the mean-field BCS Hamiltonian in real space, a Bogoliubov rotation into the Nambu particle–hole basis yields the BdG eigenvalue problem H_BdG Φ_n = E_n Φ_n with the 2×2 BdG matrix and the self-consistency condition on Δ(r).

**命题。** 从实空间的平均场 BCS 哈密顿量出发，通过 Nambu 粒子–空穴基中的 Bogoliubov 变换，得到 BdG 本征值问题 H_BdG Φ_n = E_n Φ_n，其中包含 2×2 BdG 矩阵和 Δ(r) 的自洽条件。

**Step 1 — Real-space second-quantized Hamiltonian.** Write the full Hamiltonian for interacting spin-1/2 electrons in second quantization:

**第 1 步 — 实空间二次量子化哈密顿量。** 写出二次量子化形式下相互作用自旋-1/2 电子的完整哈密顿量：

  H = ∫ d³r Σ_σ ψ_σ†(r) H₀(r) ψ_σ(r)  +  g ∫ d³r ψ↑†(r) ψ↓†(r) ψ↓(r) ψ↑(r),

where H₀(r) = −ℏ²∇²/2m + U(r) − μ is the single-particle Hamiltonian relative to the chemical potential, g < 0 is an attractive contact interaction, and ψ_σ(r) are the electron field operators satisfying {ψ_σ(r), ψ_{σ'}†(r')} = δ_{σσ'} δ³(r − r').

其中 H₀(r) = −ℏ²∇²/2m + U(r) − μ 是相对于化学势的单粒子哈密顿量，g < 0 是吸引性接触相互作用，ψ_σ(r) 是满足 {ψ_σ(r), ψ_{σ'}†(r')} = δ_{σσ'} δ³(r − r') 的电子场算符。

**Step 2 — Mean-field decoupling.** Replace the four-fermion interaction by its mean-field (Hartree–Fock–Bogoliubov) decoupling. The anomalous average Δ(r) ≡ −g ⟨ψ↓(r) ψ↑(r)⟩ is the pair potential. Neglecting the normal (Hartree) channel (absorbed into U(r)), the mean-field Hamiltonian is:

**第 2 步 — 平均场解耦。** 用平均场（Hartree–Fock–Bogoliubov）解耦替代四费米子相互作用。反常平均 Δ(r) ≡ −g ⟨ψ↓(r) ψ↑(r)⟩ 即配对势。忽略正常（Hartree）通道（并入 U(r)），平均场哈密顿量为：

  H_MF = ∫ d³r [ Σ_σ ψ_σ†(r) H₀(r) ψ_σ(r) + Δ(r) ψ↑†(r) ψ↓†(r) + Δ*(r) ψ↓(r) ψ↑(r) ] + const.

The constant is ∫ d³r |Δ(r)|²/g and is irrelevant for the eigenvalue problem.

常数项为 ∫ d³r |Δ(r)|²/g，对本征值问题无关紧要。

**Step 3 — Introduce the Nambu spinor.** Define the two-component Nambu field:

**第 3 步 — 引入 Nambu 旋量。** 定义双分量 Nambu 场：

  Ψ(r) = ( ψ↑(r)  ),    Ψ†(r) = ( ψ↑†(r),  ψ↓(r) ).
           ( ψ↓†(r) )

Using the anticommutation relation to rewrite ψ↓† H₀* ψ↓† → −ψ↓ (−H₀*(r)) ψ↓† (up to a constant from the commutation), the mean-field Hamiltonian becomes:

利用反对易关系将 ψ↓† H₀* ψ↓† 改写为 −ψ↓ (−H₀*(r)) ψ↓†（加上来自对易关系的常数），平均场哈密顿量变为：

  H_MF = ∫ d³r Ψ†(r) H_BdG Ψ(r) + const,

  H_BdG = ( H₀(r)     Δ(r)   )
           ( Δ*(r)    −H₀*(r) )

This is the **BdG Hamiltonian in Nambu space**. The off-diagonal Δ(r) mixes particle and hole sectors; −H₀*(r) = −(−ℏ²∇²/2m + U(r) − μ)* governs the hole sector (note: U(r) is real, so H₀*(r) = H₀(r) for a scalar potential, but the sign flip is essential for particle–hole symmetry).

这就是 **Nambu 空间中的 BdG 哈密顿量**。非对角项 Δ(r) 混合粒子和空穴扇区；−H₀*(r) = −(−ℏ²∇²/2m + U(r) − μ)* 控制空穴扇区（注意：U(r) 为实数时 H₀*(r) = H₀(r)，但符号翻转对于粒子–空穴对称性至关重要）。

**Step 4 — Bogoliubov transformation and eigenvalue problem.** Expand the Nambu field in the eigenmodes:

**第 4 步 — Bogoliubov 变换与本征值问题。** 将 Nambu 场展开为本征模：

  Ψ(r) = Σ_n [ γ_n Φ_n(r) + γ_n† Φ̄_n(r) ],    Φ_n(r) = ( u_n(r) )
                                                              ( v_n(r) )

where γ_n are the quasiparticle annihilation operators. Requiring H_MF = Σ_n E_n γ_n† γ_n (diagonal in quasiparticles) enforces the **BdG eigenvalue equations**:

其中 γ_n 是准粒子湮灭算符。要求 H_MF = Σ_n E_n γ_n† γ_n（在准粒子中对角），强制要求 **BdG 本征值方程**：

  H₀(r) u_n(r) + Δ(r) v_n(r) = E_n u_n(r)
  Δ*(r) u_n(r) − H₀*(r) v_n(r) = E_n v_n(r)

or in matrix form: H_BdG Φ_n = E_n Φ_n.

或用矩阵形式：H_BdG Φ_n = E_n Φ_n。

**Step 5 — Self-consistency condition.** Inverting the Bogoliubov transformation to express ψ↑(r), ψ↓(r) in terms of γ_n and computing the thermal average, using ⟨γ_n† γ_m⟩ = f(E_n) δ_{nm} and the condition E_n > 0 for the positive-energy branch:

**第 5 步 — 自洽条件。** 反转 Bogoliubov 变换，将 ψ↑(r)、ψ↓(r) 用 γ_n 表示，计算热平均，利用 ⟨γ_n† γ_m⟩ = f(E_n) δ_{nm} 和正能分支 E_n > 0 的条件：

  Δ(r) = −g ⟨ψ↓(r) ψ↑(r)⟩ = −g Σ_n u_n(r) v_n*(r) [1 − 2f(E_n)]
        = −g Σ_n u_n(r) v_n*(r) tanh(E_n / 2k_BT).

This closes the self-consistent loop: one must find Δ(r) such that the BdG eigenmodes reproduce the same Δ(r) through this equation. ∎

这关闭了自洽循环：必须找到 Δ(r)，使得 BdG 本征模通过此方程重现相同的 Δ(r)。∎

**Particle–hole symmetry check.** If (u_n, v_n)ᵀ satisfies H_BdG Φ_n = +E_n Φ_n, then (v_n*, u_n*)ᵀ satisfies H_BdG (v_n*, u_n*)ᵀ = −E_n (v_n*, u_n*)ᵀ. This particle–hole symmetry guarantees that the spectrum is symmetric about E = 0, and that zero-energy solutions (E_n = 0) are their own particle–hole conjugates — a property exploited by Majorana modes in Module 5.11.

**粒子–空穴对称性验证。** 若 (u_n, v_n)ᵀ 满足 H_BdG Φ_n = +E_n Φ_n，则 (v_n*, u_n*)ᵀ 满足 H_BdG (v_n*, u_n*)ᵀ = −E_n (v_n*, u_n*)ᵀ。此粒子–空穴对称性保证谱关于 E = 0 对称，且零能解（E_n = 0）是自身的粒子–空穴共轭——这一性质被模块 5.11 中的马约拉纳模所利用。

---

## B. Andreev Reflection Amplitude and Retro-Reflection for E < Δ · E < Δ 时的安德烈夫反射振幅与逆反射

**Claim.** At an ideal, sharp N–S interface (with the pair potential stepping from Δ = 0 for x < 0 to Δ > 0 for x > 0), an electron incident from the N side with energy E < Δ (measured from the Fermi level) is perfectly Andreev-reflected as a retro-reflected hole with reflection amplitude r_A = e^{−i arccos(E/Δ)} = −ie^{iφ_S} √(1 − E²/Δ²) + …, and zero probability of normal reflection. The transmitted (evanescent) wave decays into S over the coherence length ξ₀.

**命题。** 在理想、陡峭的 N–S 界面处（配对势从 x < 0 的 Δ = 0 跳变到 x > 0 的 Δ > 0），从 N 侧以能量 E < Δ（从费米能级量起）入射的电子被完全安德烈夫反射为逆向反射的空穴，反射振幅为 r_A = e^{−i arccos(E/Δ)}，正常反射概率为零。透射（消逝）波在超导相干长度 ξ₀ 上衰减进入 S。

**Step 1 — BdG equations for uniform regions.** For a uniform normal metal (Δ = 0), the BdG equations decouple:

**第 1 步 — 均匀区域的 BdG 方程。** 对于均匀正常金属（Δ = 0），BdG 方程解耦：

  H₀ u = E u    (electron equation),
  −H₀* v = E v  (hole equation, equivalent to H₀ v = −E v for real H₀).

The electron-like solution traveling in +x is u(x) = e^{ik_e x} with k_e = k_F + E/ℏv_F (to first order in E/E_F). The hole-like solution traveling in −x (retro-reflected) is v(x) = e^{−ik_h x} with k_h = k_F − E/ℏv_F. Note k_e ≈ k_h ≈ k_F, so the retro-reflected hole retraces the incident electron trajectory in real space (same magnitude of momentum, opposite sign of group velocity: v_group,hole = −dE/d(−k) = −v_F at k_h).

沿 +x 传播的电子型解为 u(x) = e^{ik_e x}，其中 k_e = k_F + E/ℏv_F（对 E/E_F 的一阶展开）。沿 −x 传播（逆反射）的空穴型解为 v(x) = e^{−ik_h x}，其中 k_h = k_F − E/ℏv_F。注意 k_e ≈ k_h ≈ k_F，因此逆反射空穴在实空间沿入射电子轨迹原路返回（动量大小相同，群速度符号相反：v_{group,hole} = −dE/d(−k) = −v_F 在 k_h 处）。

**Step 2 — Wave inside the superconductor.** For a uniform superconductor (Δ = const, μ = E_F), the BdG equations in 1D are:

**第 2 步 — 超导体内部的波。** 对于均匀超导体（Δ = const，μ = E_F），一维 BdG 方程为：

  ( ξ_k       Δ    ) ( u ) = E ( u )
  ( Δ*       −ξ_k  ) ( v )     ( v )

where ξ_k = ℏ²k²/2m − E_F. The eigenvalues are E = ±√(ξ_k² + Δ²). For E < Δ there is no real k satisfying E = √(ξ_k² + Δ²); instead k becomes complex: k = k_F ± iq, with q = √(Δ² − E²)/ℏv_F > 0. The wave inside S is **evanescent**, decaying as e^{−qx} with decay length

其中 ξ_k = ℏ²k²/2m − E_F。本征值为 E = ±√(ξ_k² + Δ²)。当 E < Δ 时，不存在满足 E = √(ξ_k² + Δ²) 的实数 k；取而代之，k 变为复数：k = k_F ± iq，其中 q = √(Δ² − E²)/ℏv_F > 0。S 内的波是**消逝波**，以 e^{−qx} 衰减，衰减长度为

  1/q = ℏv_F / √(Δ² − E²)  →  ξ₀ = ℏv_F / Δ    (at E = 0).

**Step 3 — Matching boundary conditions.** At the ideal N–S interface (x = 0) with no barrier, the BdG two-component wavefunction and its derivative must be continuous. Write the ansatz:

**第 3 步 — 匹配边界条件。** 在理想 N–S 界面（x = 0，无势垒）处，BdG 双分量波函数及其导数必须连续。写出试探解：

  x < 0 (N):  Φ(x) = (1,0)ᵀ e^{ik_e x}  +  r_N (1,0)ᵀ e^{−ik_e x}  +  r_A (0,1)ᵀ e^{ik_h x}
  x > 0 (S):  Φ(x) = t (u₀, v₀)ᵀ e^{iq_+ x}  +  t' (v₀*, u₀*)ᵀ e^{iq_- x}   (both decaying)

where (u₀, v₀)ᵀ is the normalized BdG eigenspinor in S: u₀ = √((1 + √(1−Δ²/E²))/2) and v₀ = Δ/(2Eu₀) ... but for E < Δ we substitute E/Δ = cos α (so α is real), giving:

其中 (u₀, v₀)ᵀ 是 S 中归一化的 BdG 本征旋量。令 E/Δ = cos α（α 为实数，因为 E < Δ），得：

  u₀ = e^{iα/2}/√2,    v₀ = e^{−iα/2}/√2,    where  α = arccos(E/Δ).

The evanescent wavevectors are q_± = k_F ± i√(Δ² − E²)/ℏv_F.

消逝波矢为 q_± = k_F ± i√(Δ² − E²)/ℏv_F。

**Step 4 — Solve the matching equations.** Continuity of Φ and dΦ/dx at x = 0 and the evanescent condition (t' is suppressed for x → +∞ and t must be chosen for the decaying solution) yields, at leading order in E/E_F (i.e. k_e ≈ k_h ≈ k_F, neglecting the small difference):

**第 4 步 — 求解匹配方程。** 在 x = 0 处 Φ 和 dΦ/dx 连续，以及消逝条件（t' 在 x → +∞ 时被压制，t 选择衰减解），在 E/E_F 的领头阶（即 k_e ≈ k_h ≈ k_F，忽略小差别）下得到：

  r_N = 0    (no normal reflection at ideal interface),
  r_A = v₀/u₀ = e^{−iα} = e^{−i arccos(E/Δ)}.

The **Andreev reflection amplitude** is:

**安德烈夫反射振幅**为：

  r_A = e^{−i arccos(E/Δ)},    |r_A|² = 1    for E < Δ.

The probability |r_A|² = 1 means **perfect Andreev reflection**: every incident electron is reflected as a hole, transferring charge 2e to the condensate. No normal reflection occurs (r_N = 0) because there is no potential barrier — the only mechanism is the Andreev process.

概率 |r_A|² = 1 意味着**完美安德烈夫反射**：每个入射电子被反射为空穴，向凝聚体转移电荷 2e。由于不存在势垒，无正常反射（r_N = 0）——唯一的机制是安德烈夫过程。

**Step 5 — Retro-reflection is built in.** The reflected hole has wavevector −k_h ≈ −k_F (moving in the −x direction) while the incident electron had wavevector +k_e ≈ +k_F. The transverse momentum is conserved (k_∥ is the same for electron and hole). The group velocity of the hole is v_hole = −dE/d(−k_h) = −v_F (also in −x direction). Therefore the hole retraces the incoming electron path exactly — this is **retro-reflection**, distinct from ordinary specular reflection where the transverse velocity would reverse but the longitudinal velocity would not. ∎

**第 5 步 — 逆反射内嵌于结果中。** 反射空穴的波矢为 −k_h ≈ −k_F（沿 −x 方向），而入射电子的波矢为 +k_e ≈ +k_F。横向动量守恒（电子和空穴的 k_∥ 相同）。空穴的群速度为 v_{hole} = −dE/d(−k_h) = −v_F（也沿 −x 方向）。因此空穴精确地沿入射电子路径逆向运动——这就是**逆反射**，区别于普通镜面反射（镜面反射中横向速度反转而纵向速度不变）。∎

---

## C. Proximity Decay Length ξ_N = ℏv_F / 2πk_BT in a Clean Normal Metal · 干净正常金属中邻近衰减长度 ξ_N = ℏv_F / 2πk_BT

**Claim.** In a clean (disorder-free) normal metal at temperature T, the pair amplitude induced by proximity to a superconductor decays as e^{−x/ξ_N} with the **Eilenberger/Usadel coherence length**:

**命题。** 在温度为 T 的干净（无序）正常金属中，由超导体邻近效应诱导的配对振幅以 e^{−x/ξ_N} 衰减，其中**艾伦伯格相干长度**为：

  ξ_N = ℏv_F / (2πk_BT).

**Step 1 — The anomalous Green's function.** The induced pair amplitude is characterized by the Gorkov anomalous Green's function F(r, r'; τ) = ⟨T_τ ψ↑(r,τ) ψ↓(r',0)⟩, where T_τ is imaginary-time ordering and τ is the Matsubara (imaginary) time. In a translation-invariant normal metal (Δ = 0), F is driven by the boundary condition at the N–S interface that imposes F ≠ 0 at x = 0.

**第 1 步 — 反常格林函数。** 诱导的配对振幅由 Gorkov 反常格林函数 F(r, r'; τ) = ⟨T_τ ψ↑(r,τ) ψ↓(r',0)⟩ 描述，其中 T_τ 是虚时间排序，τ 是松原（虚）时间。在平移不变的正常金属（Δ = 0）中，F 由 N–S 界面处 F ≠ 0 的边界条件驱动。

**Step 2 — Matsubara Fourier expansion.** Expand F in Matsubara frequencies ω_n = (2n+1)πk_BT/ℏ (for fermions). Each Matsubara component F(x; ω_n) satisfies the linearized Eilenberger equation in the normal metal (Δ = 0):

**第 2 步 — 松原频率展开。** 将 F 展开为松原频率 ω_n = (2n+1)πk_BT/ℏ（对费米子）。每个松原分量 F(x; ω_n) 在正常金属（Δ = 0）中满足线性化艾伦伯格方程：

  (ℏ|ω_n| + ℏv_F ∂/∂x) F(x; ω_n) = 0    for ω_n > 0.

This first-order equation (obtained by integrating the full Gorkov equations over the Fermi surface) has the solution:

这个一阶方程（通过在费米面上积分完整 Gorkov 方程得到）的解为：

  F(x; ω_n) = F(0; ω_n) · exp(−|ω_n| x / v_F)    for x > 0.

**Step 3 — Identify the decay length.** The decay constant is |ω_n|/v_F. The lowest Matsubara frequency is the dominant (slowest-decaying) contribution: for n = 0, ω_0 = πk_BT/ℏ, giving decay constant ω_0/v_F = πk_BT/ℏv_F. The characteristic spatial decay length of F at temperature T is:

**第 3 步 — 确定衰减长度。** 衰减常数为 |ω_n|/v_F。最低松原频率是主导（衰减最慢）的贡献：对 n = 0，ω_0 = πk_BT/ℏ，给出衰减常数 ω_0/v_F = πk_BT/ℏv_F。温度 T 时 F 的特征空间衰减长度为：

  ξ_N = v_F / ω_0 = ℏv_F / (πk_BT).

The standard convention defines ξ_N with a factor 2π in the denominator (using the first Matsubara frequency ω_0 = πk_BT/ℏ and the definition ξ_N ≡ ℏv_F/2πk_BT from the quasiclassical theory):

标准惯例在分母中定义因子 2π（利用第一松原频率 ω_0 = πk_BT/ℏ 以及准经典理论中的定义 ξ_N ≡ ℏv_F/2πk_BT）：

  **ξ_N = ℏv_F / (2πk_BT)**.

(The factor of 2 differs between different conventions in the literature; the key physics is the 1/T divergence.) At T = 4 K and v_F ≈ 10⁶ m/s (typical metal), ξ_N ≈ ℏ × 10⁶ / (2π × 1.38×10⁻²³ × 4) ≈ 1.9 μm — a macroscopic length showing that proximity-induced pairing extends far into a clean normal metal at low temperatures.

（文献中不同惯例中因子 2 有所不同；关键物理是 1/T 发散。）在 T = 4 K、v_F ≈ 10⁶ m/s（典型金属）时，ξ_N ≈ ℏ × 10⁶ / (2π × 1.38×10⁻²³ × 4) ≈ 1.9 μm——这是一个宏观长度，表明低温下邻近效应诱导的配对可以在干净正常金属中延伸很远。

**Step 4 — Temperature dependence.** As T → 0, ξ_N → ∞: the pair amplitude fills the entire normal region (limited only by the sample size). As T increases, ξ_N shrinks as 1/T, and the proximity effect weakens. This is the quasiclassical explanation: at higher T, thermal dephasing (phase scrambling over the Matsubara time scale ℏ/k_BT) limits how far a coherent Cooper pair can propagate into N. ∎

**第 4 步 — 温度依赖性。** 当 T → 0 时，ξ_N → ∞：配对振幅充满整个正常区域（仅受样品尺寸限制）。随着 T 升高，ξ_N 按 1/T 缩小，邻近效应减弱。这是准经典解释：在较高温度下，热退相干（在松原时间尺度 ℏ/k_BT 上的相位弥散）限制了相干库珀对能够传播进 N 的距离。∎

**Step 5 — Comparison with dirty limit.** In a diffusive (disordered) normal metal with diffusion constant D = v_F ℓ/3 (ℓ = mean free path), the same analysis gives ξ_N^{dirty} = √(ℏD / 2πk_BT). This is always shorter than the clean-limit ξ_N (since D = v_F ℓ/3 ≪ v_F² for ℓ ≪ ξ_N), and reflects the diffusive random walk of pairs rather than ballistic propagation. ∎

**第 5 步 — 与脏极限比较。** 在扩散系数为 D = v_F ℓ/3（ℓ = 平均自由程）的扩散（无序）正常金属中，相同的分析给出 ξ_N^{dirty} = √(ℏD / 2πk_BT)。这总是比干净极限的 ξ_N 短（因为对于 ℓ ≪ ξ_N，有 D = v_F ℓ/3 ≪ v_F²），反映了对的扩散随机游走而非弹道传播。∎

---

*Summary: (A) The BdG equations arise from the mean-field BCS Hamiltonian via a Nambu doubling and Bogoliubov transformation; particle–hole symmetry is built in and guarantees zero-energy Majorana solutions. (B) At an ideal N–S interface, the E < Δ gap means no real quasiparticle state exists in S, forcing Andreev reflection with |r_A|² = 1 and retro-reflection because electron and hole share the same Fermi momentum. (C) The proximity decay length ξ_N = ℏv_F/2πk_BT follows from the first Matsubara frequency of the linearized Eilenberger equation; it diverges as T → 0 and shrinks as 1/T at higher temperatures.*

*总结：(A) BdG 方程通过 Nambu 加倍和 Bogoliubov 变换从平均场 BCS 哈密顿量中产生；粒子–空穴对称性内嵌其中，保证零能马约拉纳解的存在。(B) 在理想 N–S 界面处，E < Δ 的能隙意味着 S 中不存在真实准粒子态，迫使安德烈夫反射 |r_A|² = 1 发生，且由于电子和空穴共享相同的费米动量而产生逆反射。(C) 邻近衰减长度 ξ_N = ℏv_F/2πk_BT 来自线性化艾伦伯格方程的第一松原频率；在 T → 0 时发散，在较高温度下按 1/T 缩小。*

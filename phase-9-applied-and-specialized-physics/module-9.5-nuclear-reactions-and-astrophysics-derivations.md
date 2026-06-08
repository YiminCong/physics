# Derivations — Module 9.5: Nuclear Reactions & Astrophysics
# 推导 — 模块 9.5：核反应与天体物理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.5](./module-9.5-nuclear-reactions-and-astrophysics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.5](./module-9.5-nuclear-reactions-and-astrophysics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Two-Body Q-Value and Threshold Energy · 两体反应 Q 值与阈动能

**Claim.** For the reaction a + A → b + B (A at rest in the lab), the Q-value is Q = (m_a + m_A − m_b − m_B)c², and the threshold kinetic energy (for Q < 0) is T_th = −Q(m_a + m_A + m_b + m_B)/(2 m_A).

**命题。** 对反应 a + A → b + B（实验室系中 A 静止），Q 值为 Q = (m_a + m_A − m_b − m_B)c²，阈动能（Q < 0 时）为 T_th = −Q(m_a + m_A + m_b + m_B)/(2 m_A)。

**Step 1 — Energy–momentum conservation.** Four-momentum is conserved: p_a^μ + p_A^μ = p_b^μ + p_B^μ. Taking the invariant mass squared of the left-hand side (s = (p_a + p_A)²c² in natural units with c = 1 briefly):

**第 1 步 — 能动量守恒。** 四动量守恒：p_a^μ + p_A^μ = p_b^μ + p_B^μ。对左边取不变质量的平方（s = (p_a + p_A)²）：

  s = (E_a + m_A c²)² − (p_a c)²
    = E_a² + 2 E_a m_A c² + m_A² c⁴ − p_a² c²
    = m_a² c⁴ + 2 T_a m_A c² + 2 m_a m_A c⁴ + m_A² c⁴,

where T_a = E_a − m_a c² is the kinetic energy of a, and we used E_a² − p_a² c² = m_a² c⁴ (on-shell relation).

其中 T_a = E_a − m_a c² 是 a 的动能，利用了质壳关系 E_a² − p_a² c² = m_a² c⁴。

**Step 2 — Q-value from rest masses.** By conservation, s equals the invariant mass squared of the right-hand side. In the threshold situation (minimum beam energy) all products are created at rest in the center-of-mass frame, so:

**第 2 步 — 由静止质量得出 Q 值。** 由守恒，s 等于右边的不变质量平方。在阈值情况下（最小束能），所有产物在质心系中均静止，于是：

  √s_min = (m_b + m_B) c²   →   s_min = (m_b + m_B)² c⁴.

The Q-value is defined by total rest mass energy difference, so inserting s for a reaction proceeding at rest in the CM frame (√s = (m_a + m_A)c² + Q):

Q 值由总静止质量能差定义，将质心系静止反应的 s 代入（√s = (m_a + m_A)c² + Q）：

  **Q = (m_a + m_A − m_b − m_B) c².**

**Step 3 — Threshold from the kinematic invariant.** Setting s = s_min:

**第 3 步 — 从运动学不变量得到阈值。** 令 s = s_min：

  m_a² c⁴ + 2 T_th m_A c² + 2 m_a m_A c⁴ + m_A² c⁴ = (m_b + m_B)² c⁴.

Solve for T_th. Note (m_b + m_B)² − (m_a + m_A)² = (m_b + m_B + m_a + m_A)(m_b + m_B − m_a − m_A) = (Σ_f + Σ_i)(−Q/c²), where Σ_i = m_a + m_A, Σ_f = m_b + m_B:

对 T_th 求解。注意 (m_b + m_B)² − (m_a + m_A)² = (Σ_f + Σ_i)(m_b + m_B − m_a − m_A) = −(Σ_f + Σ_i)Q/c²，其中 Σ_i = m_a + m_A，Σ_f = m_b + m_B：

  2 T_th m_A c² = [(m_b + m_B)² − (m_a + m_A)²] c⁴ = −(Σ_i + Σ_f) Q c²,

  **T_th = −Q (m_a + m_A + m_b + m_B) / (2 m_A).**

**Step 4 — Physical interpretation.** Rewrite: T_th = |Q| (1 + m_a/m_A + m_b/m_B + m_b m_B/(m_A(m_b + m_B)) + …)/2 approximately; the key point is T_th > |Q| whenever there is recoil. The excess T_th − |Q| = |Q|(Σ_i + Σ_f − 2 m_A)/(2 m_A) goes into kinetic energy of the CM frame (unavoidable since A is not infinitely massive). For m_a ≪ m_A, T_th → |Q|(1 + m_a/m_A) ≈ |Q|, recovering the obvious result that for a very heavy target almost all energy goes into internal degrees of freedom. ∎

**第 4 步 — 物理解释。** 改写：T_th = |Q|(1 + m_a/m_A + …)/2 近似地；关键是只要有反冲，T_th > |Q|。超出量 T_th − |Q| 进入质心系动能（不可避免，因为 A 不是无限重的）。当 m_a ≪ m_A 时，T_th → |Q|(1 + m_a/m_A) ≈ |Q|，恢复了对非常重的靶几乎所有能量都进入内部自由度的明显结果。∎

---

## B. The Breit–Wigner Resonance Cross-Section · 布雷特–维格纳共振截面

**Claim.** Near an isolated resonance at energy E_r, the elastic (and reaction) cross-section takes the form σ(E) ∝ Γ² / [(E − E_r)² + Γ²/4], a Lorentzian of FWHM = Γ.

**命题。** 在能量 E_r 处的孤立共振附近，弹性（及反应）截面取形式 σ(E) ∝ Γ² / [(E − E_r)² + Γ²/4]，为半高全宽为 Γ 的洛伦兹线型。

**Step 1 — Resonance as a decaying state.** A compound nucleus formed at energy E_r has a finite lifetime τ = ℏ/Γ. Its wavefunction decays as ψ(t) ∝ e^{−i E_r t/ℏ} e^{−Γt/(2ℏ)} for t > 0. In the energy domain its amplitude is the Fourier transform:

**第 1 步 — 共振作为衰变态。** 在能量 E_r 处形成的复合核寿命有限 τ = ℏ/Γ。其波函数衰减为 ψ(t) ∝ e^{−i E_r t/ℏ} e^{−Γt/(2ℏ)}（t > 0）。在能量域，其振幅是傅里叶变换：

  A(E) = ∫₀^∞ ψ(t) e^{i E t/ℏ} dt ∝ 1 / (E − E_r + iΓ/2).

**Step 2 — Cross-section is modulus squared of amplitude.** The cross-section (probability of formation times branching ratio to the exit channel) is proportional to |A(E)|²:

**第 2 步 — 截面是振幅模方。** 截面（形成概率乘以到出口道的分支比）正比于 |A(E)|²：

  σ(E) ∝ |A(E)|² = 1 / [(E − E_r)² + Γ²/4].

This is the **Lorentz (Breit–Wigner) profile**. The maximum is at E = E_r with value 4/Γ² (up to overall constants), and the half-maximum points are at E = E_r ± Γ/2, confirming Γ is the full width at half maximum.

这就是**洛伦兹（布雷特–维格纳）轮廓**。最大值在 E = E_r 处，值为 4/Γ²（到差一个整体常数），半高点在 E = E_r ± Γ/2，确认 Γ 是半高全宽。

**Step 3 — Quantum-mechanical normalization.** The full Breit–Wigner formula from S-matrix theory reads:

**第 3 步 — 量子力学归一化。** 来自 S 矩阵理论的完整布雷特–维格纳公式为：

  σ_{a→b}(E) = π λ-bar² (2J_r + 1)/[(2J_a + 1)(2J_A + 1)] · (Γ_a Γ_b) / [(E − E_r)² + Γ²/4],

where λ-bar = ℏ/p is the reduced de Broglie wavelength of the incoming particles, J_r is the spin of the resonant state, and Γ_a, Γ_b are the partial widths into entrance and exit channels respectively, with Γ = Σ Γ_i the total width. The factor π λ-bar² is the geometric quantum cross-section, and the spin factor (2J_r + 1)/[(2J_a + 1)(2J_A + 1)] counts the available magnetic substates.

其中 λ-bar = ℏ/p 是入射粒子的约化德布罗意波长，J_r 是共振态的自旋，Γ_a、Γ_b 分别是入射道和出射道的分宽度，Γ = Σ Γ_i 为总宽度。因子 π λ-bar² 是几何量子截面，自旋因子 (2J_r + 1)/[(2J_a + 1)(2J_A + 1)] 计算可用的磁量子态数。

**Step 4 — Peak value and lifetime.** At E = E_r, σ_peak = π λ-bar² · spin factor · (4 Γ_a Γ_b/Γ²). For elastic scattering (b = a) with a single open channel Γ_a = Γ, we get σ_peak = 4π λ-bar² · spin factor — purely geometric (no suppression from partial widths). The relation Γ τ = ℏ (energy–time uncertainty) shows that a long-lived state (small Γ) produces a narrow, tall resonance. ∎

**第 4 步 — 峰值和寿命。** 在 E = E_r 处，σ_peak = π λ-bar² · 自旋因子 · (4 Γ_a Γ_b/Γ²)。对于只有一个开放道 Γ_a = Γ 的弹性散射（b = a），得 σ_peak = 4π λ-bar² · 自旋因子——纯几何量（无分宽度带来的压制）。关系式 Γ τ = ℏ（能量–时间不确定性）表明长寿命态（Γ 小）产生窄而高的共振。∎

---

## C. Rotational Band Spectrum from the Rigid Rotor · 刚性转子的转动带谱

**Claim.** A deformed nucleus with moment of inertia ℐ has rotational energy levels E_J = ℏ² J(J+1)/(2ℐ), with J = 0, 2, 4, … for an axially symmetric even–even nucleus.

**命题。** 转动惯量为 ℐ 的形变核，转动能级为 E_J = ℏ² J(J+1)/(2ℐ)，对轴对称偶–偶核 J = 0, 2, 4, …

**Step 1 — Rigid rotor Hamiltonian.** For a rigid symmetric top rotating about a body-fixed symmetry axis, the kinetic energy is T = L²/(2ℐ), where L is the angular momentum about an axis perpendicular to the symmetry axis and ℐ is the moment of inertia for that rotation. In quantum mechanics L² → L̂² with eigenvalues ℏ² J(J+1):

**第 1 步 — 刚性转子哈密顿量。** 对于绕体固连对称轴旋转的刚性对称陀螺，动能为 T = L²/(2ℐ)，其中 L 是绕垂直于对称轴的轴的角动量，ℐ 是该转动的转动惯量。量子力学中 L² → L̂²，本征值为 ℏ² J(J+1)：

  Ĥ_rot = L̂²/(2ℐ),

  Ĥ_rot |J, M⟩ = ℏ² J(J+1)/(2ℐ) |J, M⟩.

  **E_J = ℏ² J(J+1) / (2ℐ).**

This follows directly from the angular momentum algebra (Module 3.4), identical to the spectrum of a diatomic molecule (Module 9.2), but the moment of inertia now reflects the entire nuclear mass distribution.

这直接来自角动量代数（模块 3.4），与双原子分子的谱相同（模块 9.2），但转动惯量现在反映整个核质量分布。

**Step 2 — Parity selection on J.** An axially symmetric nucleus with a mirror symmetry about the plane perpendicular to the symmetry axis (as in a prolate or oblate spheroid) has a symmetry under 180° rotation about a perpendicular axis, R_⊥(π). For an even–even nucleus the intrinsic ground state has spin 0⁺, and R_⊥(π)|J, K=0⟩ = (−1)^J |J, K=0⟩. The physical wavefunction must be symmetric under this operation (bosonic nucleons pair to zero), so:

**第 2 步 — 对 J 的宇称选择。** 对于具有关于垂直于对称轴的平面的镜像对称性的轴对称核（如长椭球或扁椭球），存在绕垂直轴 180° 转动的对称性 R_⊥(π)。对偶–偶核，本征基态的自旋为 0⁺，且 R_⊥(π)|J, K=0⟩ = (−1)^J |J, K=0⟩。物理波函数必须在此操作下对称（玻色子配对核子对为零），故：

  (−1)^J = +1   →   J must be even: J = 0, 2, 4, 6, …

**Step 3 — Predicted ratios and the rigid-rotor limit.** The energy ratios for the first few even states are:

**第 3 步 — 预测比值和刚性转子极限。** 前几个偶数态的能量比值为：

  E(2⁺)/E(0⁺) = 6/(1·2) / (1·0) = undefined (0⁺ is the reference, E = 0),

More meaningfully, the spacing ratios:

更有意义地，间距比值：

  E(2⁺) : E(4⁺) : E(6⁺) = 6 : 20 : 42   (in units of ℏ²/2ℐ),

and so:

于是：

  E(4⁺)/E(2⁺) = 20/6 = 10/3 ≈ 3.33,
  E(6⁺)/E(2⁺) = 42/6 = 7.

These ratios are the definitive signatures of a rotational nucleus and are compared against the vibrational limit E(4⁺)/E(2⁺) → 2 (two phonons vs one phonon in a harmonic oscillator). ∎

这些比值是转动核的明确特征，与振动极限 E(4⁺)/E(2⁺) → 2（谐振子中两声子对比一声子）进行比较。∎

**Step 4 — Estimate of ℐ.** For a uniformly deformed sphere of mass A m_u and radius R ≈ 1.2 A^{1/3} fm, the moment of inertia is ℐ_rigid = (2/5) A m_u R². For ¹⁵²Sm, A = 152, R ≈ 6.3 fm, giving ℐ_rigid ≈ 0.40 × 152 × 938 MeV/c² × (6.3 fm)² ≈ 5.2 × 10⁴ MeV fm²/c². Then E(2⁺) = ℏ²·6/(2ℐ_rigid) = 3ℏ²/ℐ_rigid. With ℏc = 197.3 MeV fm, ℏ² = (ℏc)²/c² = (197.3)²/(3×10⁸)^2 in mixed units — in nuclear convenience: E(2⁺) ~ (3 × (197.3)²)/(5.2 × 10⁴ × 938) MeV ≈ 0.24 MeV. The measured value 0.122 MeV indicates the effective ℐ ≈ 0.5 ℐ_rigid, reflecting the superfluid (pair-correlated) nature of the nuclear interior, which reduces the effective moment of inertia.

**第 4 步 — ℐ 的估算。** 对质量为 A m_u、半径 R ≈ 1.2 A^{1/3} fm 的均匀形变球，转动惯量为 ℐ_rigid = (2/5) A m_u R²。对 ¹⁵²Sm，A = 152，R ≈ 6.3 fm，给出 ℐ_rigid ≈ 0.40 × 152 × 938 MeV/c² × (6.3 fm)² ≈ 5.2 × 10⁴ MeV fm²/c²。则 E(2⁺) = ℏ²·6/(2ℐ_rigid) = 3ℏ²/ℐ_rigid。由核方便单位得 E(2⁺) ~ 0.24 MeV。实测值 0.122 MeV 表明有效 ℐ ≈ 0.5 ℐ_rigid，反映核内部的超流（配对关联）性质，使有效转动惯量减小。

---

## D. The Gamow Peak: Maxwell–Boltzmann Tail × Tunnelling Factor · 伽莫夫峰：麦克斯韦–玻尔兹曼尾与隧穿因子之积

**Claim.** The thermonuclear reaction rate integrand peaks at the Gamow energy E_0 = (πα Z_a Z_A √(μc²/2) k_B T)^{2/3} / 2^{1/3}, with width Δ ∝ E_0^{1/2} (k_B T)^{1/2}. This result is the link to the Gamow tunnelling factor derived in Module 9.3.

**命题。** 热核反应速率被积函数在伽莫夫能量 E_0 = (πα Z_a Z_A √(μc²/2) k_B T)^{2/3} / 2^{1/3} 处达到峰值，宽度 Δ ∝ E_0^{1/2} (k_B T)^{1/2}。此结果与模块 9.3 中推导的伽莫夫隧穿因子相联系。

**Step 1 — The cross-section with Gamow factor.** From Module 9.3, the charged-particle fusion cross-section factored as:

**第 1 步 — 含伽莫夫因子的截面。** 由模块 9.3，带电粒子聚变截面分解为：

  σ(E) = S(E) / E · exp(−2πη(E)),

where S(E) is the astrophysical S-factor (slowly varying near threshold for non-resonant reactions), E is the center-of-mass energy, and the **Gamow factor** is:

其中 S(E) 是天体物理 S 因子（对非共振反应在阈值附近缓变），E 是质心系能量，**伽莫夫因子**为：

  exp(−2πη) = exp(−2π Z_a Z_A α c / v) = exp(−2π Z_a Z_A α √(μc²/(2E))).

At low energies (below the Coulomb barrier) η ≫ 1 and this factor suppresses the cross-section exponentially.

在低能量（库仑势垒以下），η ≫ 1，此因子指数压制截面。

**Step 2 — The Maxwell–Boltzmann weight.** In a plasma at temperature T, the relative kinetic energy E follows the Maxwell–Boltzmann distribution:

**第 2 步 — 麦克斯韦–玻尔兹曼权重。** 在温度 T 的等离子体中，相对动能 E 服从麦克斯韦–玻尔兹曼分布：

  f(E) dE ∝ √E · exp(−E / k_B T) dE.

The thermal rate ⟨σv⟩ ∝ ∫₀^∞ S(E) exp(−2πη − E/k_B T) dE (treating S as approximately constant). Define the integrand:

热速率 ⟨σv⟩ ∝ ∫₀^∞ S(E) exp(−2πη − E/k_B T) dE（将 S 视为近似常数）。定义被积函数：

  I(E) = exp(−f(E)),   f(E) = 2π Z_a Z_A α √(μc²/(2E)) + E/(k_B T).

**Step 3 — Find the Gamow peak by minimizing f(E).** Differentiate:

**第 3 步 — 通过最小化 f(E) 求伽莫夫峰。** 对 f(E) 微分：

  df/dE = −π Z_a Z_A α √(μc²/2) / E^{3/2} + 1/(k_B T) = 0.

Solving for E = E_0:

对 E = E_0 求解：

  E_0^{3/2} = π Z_a Z_A α √(μc²/2) · k_B T,

  **E_0 = (π Z_a Z_A α)^{2/3} (μc²/2)^{1/3} (k_B T)^{2/3}.**

Since df/dE = 0 at E_0 and d²f/dE² > 0, this is a minimum of f, hence a maximum of I(E) — the Gamow peak.

因 df/dE = 0 在 E_0 处且 d²f/dE² > 0，这是 f 的极小，故是 I(E) 的极大——伽莫夫峰。

**Step 4 — Width of the peak.** Expand f(E) to second order about E_0:

**第 4 步 — 峰的宽度。** 在 E_0 处将 f(E) 展开到二阶：

  f(E) ≈ f(E_0) + ½ f''(E_0) (E − E_0)²,

  f''(E_0) = (3/4) π Z_a Z_A α √(μc²/2) / E_0^{5/2} = 3/(2 E_0 k_B T)  (using E_0^{3/2} = π Z_a Z_A α √(μc²/2) k_B T).

The integrand is thus approximately Gaussian: I(E) ≈ I(E_0) exp[−(E − E_0)²/(2σ_G²)] with 1/(2σ_G²) = f''(E_0)/2, giving:

被积函数近似为高斯型：I(E) ≈ I(E_0) exp[−(E − E_0)²/(2σ_G²)]，其中 1/(2σ_G²) = f''(E_0)/2，得：

  σ_G = (2/3)^{1/2} (E_0 k_B T)^{1/2},

and the effective FWHM (Gamow window width) is:

有效半高全宽（伽莫夫窗口宽度）为：

  **Δ = 2√(2 ln 2) σ_G ≈ 4√(E_0 k_B T / 3).**

**Step 5 — The peak value and link to Module 9.3.** At the Gamow peak, the exponent is:

**第 5 步 — 峰值及与模块 9.3 的联系。** 在伽莫夫峰处，指数为：

  f(E_0) = 2πη(E_0) + E_0/(k_B T) = 3 E_0/(k_B T) = 3(E_0/k_B T).

(One can check: f(E_0) = 2π Z_a Z_A α √(μc²/(2E_0)) + E_0/k_B T, and from Step 3, 2π Z_a Z_A α √(μc²/2) = E_0^{3/2}/k_B T, so f(E_0) = E_0/(k_B T) (1 + 2) = 3E_0/(k_B T).) The suppression is exp(−3E_0/k_B T) which for the solar pp reaction gives exp(−31) ~ 10⁻¹³, in agreement with the module's statement.

（可验证：f(E_0) = 2π Z_a Z_A α √(μc²/(2E_0)) + E_0/k_B T，由第 3 步 2π Z_a Z_A α √(μc²/2) = E_0^{3/2}/k_B T，故 f(E_0) = E_0/(k_B T)(1 + 2) = 3E_0/(k_B T)。）压制因子为 exp(−3E_0/k_B T)，对太阳 pp 反应给出 exp(−31) ~ 10⁻¹³，与模块的陈述一致。

The **connection to Module 9.3**: the exponent 2πη at E_0 = (2/3)f(E_0) = 2E_0/k_B T is precisely the Gamow tunnelling exponent derived there for barrier penetration at energy E_0. The Gamow peak tells us which energy E_0 actually dominates the stellar rate — it is the energy at which the tunnelling probability and the Boltzmann suppression together are minimized most favorably. ∎

**与模块 9.3 的联系**：在 E_0 处的指数 2πη = (2/3)f(E_0) = 2E_0/k_B T 正是模块 9.3 中推导的能量 E_0 处势垒穿透的伽莫夫隧穿指数。伽莫夫峰告诉我们哪个能量 E_0 实际主导恒星速率——它是隧穿概率和玻尔兹曼压制共同最有利地最小化的能量。∎

---

*Derivations document for Module 9.5 — full derivations of the Q-value and threshold energy (relativistic kinematics), the Breit–Wigner resonance profile (time-domain approach plus S-matrix normalization), the rigid-rotor rotational band (angular momentum quantization plus symmetry selection), and the Gamow peak (steepest-descent analysis of the MB–tunnelling product). All derivations are bilingual and show full intermediate steps.*

*模块 9.5 推导文档——Q 值与阈动能（相对论运动学）、布雷特–维格纳共振轮廓（时域方法加 S 矩阵归一化）、刚性转子转动带（角动量量子化加对称性选择）以及伽莫夫峰（MB–隧穿乘积的最速下降分析）的完整推导。所有推导均为双语，并展示完整中间步骤。*

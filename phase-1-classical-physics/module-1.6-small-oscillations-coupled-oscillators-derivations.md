# Derivations — Module 1.6: Small Oscillations & Coupled Oscillators
# 推导 — 模块 1.6：小振动与耦合振子

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.6](./module-1.6-small-oscillations-coupled-oscillators.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.6](./module-1.6-small-oscillations-coupled-oscillators.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Damped Harmonic Oscillator — All Regimes · 阻尼谐振子——所有阻尼情形

**Claim.** The equation of motion y″ + 2γy′ + ω₀²y = 0 (where γ = b/2m is the damping coefficient and ω₀ = √(k/m) is the natural frequency) has qualitatively different solutions in three regimes:
- Underdamped (γ < ω₀): y(t) = e^{−γt}[A cos(ω_d t) + B sin(ω_d t)], ω_d = √(ω₀² − γ²).
- Critically damped (γ = ω₀): y(t) = (A + Bt) e^{−γt}.
- Overdamped (γ > ω₀): y(t) = A e^{r₊ t} + B e^{r₋ t}, r± = −γ ± √(γ² − ω₀²).

**命题。** 运动方程 y″ + 2γy′ + ω₀²y = 0（γ = b/2m 为阻尼系数，ω₀ = √(k/m) 为固有频率）在三种情形下有定性不同的解：
- 欠阻尼（γ < ω₀）：y(t) = e^{−γt}[A cos(ω_d t) + B sin(ω_d t)]，ω_d = √(ω₀² − γ²)。
- 临界阻尼（γ = ω₀）：y(t) = (A + Bt) e^{−γt}。
- 过阻尼（γ > ω₀）：y(t) = A e^{r₊ t} + B e^{r₋ t}，r± = −γ ± √(γ² − ω₀²)。

**Step 1 — Characteristic equation.** Try y = e^{rt}. Substituting into y″ + 2γy′ + ω₀²y = 0:

**第 1 步 — 特征方程。** 尝试 y = e^{rt}，代入 y″ + 2γy′ + ω₀²y = 0：

  r²e^{rt} + 2γr e^{rt} + ω₀² e^{rt} = 0   ⟹   r² + 2γr + ω₀² = 0.

**Step 2 — Solve the characteristic equation by the quadratic formula.**

**第 2 步 — 用求根公式解特征方程。**

  r = (−2γ ± √(4γ² − 4ω₀²)) / 2 = −γ ± √(γ² − ω₀²).

The nature of the roots depends on the sign of γ² − ω₀².

根的性质取决于 γ² − ω₀² 的符号。

**Step 3a — Underdamped case (γ < ω₀).** Define ω_d = √(ω₀² − γ²) > 0. The roots are complex:

**第 3a 步 — 欠阻尼情形（γ < ω₀）。** 定义 ω_d = √(ω₀² − γ²) > 0。根为复数：

  r = −γ ± i ω_d.

The general real solution is:

实数通解为：

  y(t) = e^{−γt}[A cos(ω_d t) + B sin(ω_d t)].

The oscillation frequency ω_d < ω₀ is reduced by damping; the amplitude decays as e^{−γt}. ∎_a

振荡频率 ω_d < ω₀ 因阻尼而降低；振幅按 e^{−γt} 衰减。∎_a

**Step 3b — Critically damped case (γ = ω₀).** The characteristic equation has a repeated root r = −γ. For a repeated root, the two linearly independent solutions are e^{rt} and t e^{rt}:

**第 3b 步 — 临界阻尼情形（γ = ω₀）。** 特征方程有重根 r = −γ。对于重根，两个线性独立解为 e^{rt} 和 t e^{rt}：

  y(t) = (A + Bt) e^{−γt}.

(Verify: plugging into the ODE gives zero.) This case achieves the fastest return to equilibrium without oscillation. ∎_b

（验证：代入常微分方程得零。）此情形在无振荡条件下最快回到平衡位置。∎_b

**Step 3c — Overdamped case (γ > ω₀).** Define Γ = √(γ² − ω₀²) > 0. The roots are two distinct real negative numbers r± = −γ ± Γ. The general solution is:

**第 3c 步 — 过阻尼情形（γ > ω₀）。** 定义 Γ = √(γ² − ω₀²) > 0。根为两个不同的负实数 r± = −γ ± Γ。通解为：

  y(t) = A e^{(−γ+Γ)t} + B e^{(−γ−Γ)t}.

Both exponents are negative (since Γ < γ), so y → 0 exponentially without oscillation. The slower-decaying mode dominates at late times. ∎_c

两个指数均为负（因为 Γ < γ），故 y 指数衰减趋于 0，无振荡。较慢衰减模式在晚时支配。∎_c

---

## B. Driven Damped Oscillator — Steady-State Amplitude and Resonance · 受迫阻尼振子——稳态振幅与共振

**Claim.** For m ÿ + b ẏ + k y = F₀ cos(ωt), the steady-state amplitude is:

  A(ω) = (F₀/m) / √((ω₀² − ω²)² + 4γ²ω²),

which is maximised at ω_res = √(ω₀² − 2γ²) ≈ ω₀ for small damping.

**命题。** 对于 m ÿ + b ẏ + k y = F₀ cos(ωt)，稳态振幅为：

  A(ω) = (F₀/m) / √((ω₀² − ω²)² + 4γ²ω²)，

在小阻尼时在 ω_res = √(ω₀² − 2γ²) ≈ ω₀ 处取最大值。

**Step 1 — Use complex notation.** Write the drive as Re[F₀ e^{iωt}] and seek a steady-state solution of the form y_p = Re[C e^{iωt}]:

**第 1 步 — 使用复数记法。** 将驱动力写为 Re[F₀ e^{iωt}]，寻求形如 y_p = Re[C e^{iωt}] 的稳态解：

  m(iω)² C + b(iω) C + k C = F₀.

  C[(−ω² m + k) + iωb] = F₀.

  C = (F₀/m) / [(ω₀² − ω²) + 2iγω].

**Step 2 — Find the amplitude.** |C| gives the amplitude:

**第 2 步 — 求振幅。** |C| 给出振幅：

  A = |C| = (F₀/m) / |{(ω₀² − ω²) + 2iγω}|

  = **(F₀/m) / √((ω₀² − ω²)² + 4γ²ω²).** ∎_amplitude

**Step 3 — Find the resonant frequency.** Maximise A(ω) by minimising the denominator f(ω) = (ω₀² − ω²)² + 4γ²ω². Differentiate with respect to ω²; let u = ω²:

**第 3 步 — 求共振频率。** 最大化 A(ω) 即最小化分母 f(ω) = (ω₀² − ω²)² + 4γ²ω²。对 ω² 微分，令 u = ω²：

  df/du = −2(ω₀² − u) + 4γ² = 0   ⟹   ω₀² − u = 2γ²   ⟹   u = ω₀² − 2γ².

So the resonant frequency is:

故共振频率为：

  **ω_res = √(ω₀² − 2γ²).** ∎

For γ ≪ ω₀ (high-Q oscillator), ω_res ≈ ω₀, and the peak amplitude A(ω_res) ≈ F₀/(2mγω₀) = F₀ Q/(mω₀²).

对于 γ ≪ ω₀（高 Q 振子），ω_res ≈ ω₀，峰值振幅 A(ω_res) ≈ F₀/(2mγω₀) = F₀ Q/(mω₀²)。

---

## C. Normal Modes of Two Equal Masses and Three Springs · 两等质量三弹簧系统的简正模式

**Setup.** Two masses m are each connected to fixed walls by springs of stiffness k, and to each other by a spring of stiffness κ. Let x₁ and x₂ be the displacements from equilibrium.

**设置。** 两个质量 m 各通过刚度 k 的弹簧与固定墙相连，并通过刚度 κ 的弹簧相互连接。设 x₁ 和 x₂ 为偏离平衡位置的位移。

**Claim.** The system has two normal-mode frequencies:
- Symmetric mode: ω₁² = k/m (both masses move together).
- Antisymmetric mode: ω₂² = (k + 2κ)/m (masses move in opposite directions).

**命题。** 该系统有两个简正模式频率：
- 对称模式：ω₁² = k/m（两质量同向运动）。
- 反对称模式：ω₂² = (k + 2κ)/m（质量反向运动）。

**Step 1 — Write the equations of motion.** For mass 1: the left wall spring pulls with force −kx₁, the coupling spring pulls with force −κ(x₁ − x₂). Similarly for mass 2:

**第 1 步 — 写出运动方程。** 对质量 1：左壁弹簧施力 −kx₁，耦合弹簧施力 −κ(x₁ − x₂)。类似地对质量 2：

  m ẍ₁ = −kx₁ − κ(x₁ − x₂) = −(k + κ)x₁ + κx₂,
  m ẍ₂ = −kx₂ − κ(x₂ − x₁) = κx₁ − (k + κ)x₂.

**Step 2 — Matrix form.** Define x = (x₁, x₂)ᵀ. The system is m ẍ = −K x, where the stiffness matrix is:

**第 2 步 — 矩阵形式。** 定义 x = (x₁, x₂)ᵀ。系统为 m ẍ = −K x，刚度矩阵为：

      | k + κ   −κ  |
  K = |             |
      |  −κ   k + κ |

**Step 3 — Seek normal-mode solutions.** Substitute x = A e^{iωt} to get the eigenvalue problem:

**第 3 步 — 寻求简正模式解。** 代入 x = A e^{iωt} 得特征值问题：

  K A = mω² A,   i.e.   (K − mω² I) A = 0.

Non-trivial solutions require det(K − mω² I) = 0:

非平凡解要求 det(K − mω² I) = 0：

  det | k + κ − mω²    −κ         | = 0
      |   −κ        k + κ − mω²   |

  (k + κ − mω²)² − κ² = 0.

**Step 4 — Solve the characteristic equation.** Factoring:

**第 4 步 — 解特征方程。** 因式分解：

  [(k + κ − mω²) − κ][(k + κ − mω²) + κ] = 0,

  (k − mω²)(k + 2κ − mω²) = 0.

This gives two eigenvalues:

得两个特征值：

  mω₁² = k   ⟹   **ω₁² = k/m**,
  mω₂² = k + 2κ   ⟹   **ω₂² = (k + 2κ)/m.** ∎_frequencies

**Step 5 — Find the eigenvectors (normal mode shapes).** For ω₁² = k/m: substitute into (K − mω²I) A = 0:

**第 5 步 — 求特征向量（简正模式形状）。** 对 ω₁² = k/m：代入 (K − mω²I) A = 0：

  (κ − κ; −κ κ)(A₁; A₂) = 0   ⟹   κ(A₁ − A₂) = 0   ⟹   A₁ = A₂.

**Mode 1 (symmetric):** A₁ = (1, 1)ᵀ / √2. Both masses move in the same direction by the same amount. The coupling spring is unstretched; it contributes nothing, and the effective frequency is just k/m.

**模式 1（对称）：** A₁ = (1, 1)ᵀ / √2。两质量同向移动相同距离。耦合弹簧不伸缩，不起作用，有效频率仅为 k/m。

For ω₂² = (k + 2κ)/m: substitute into (K − mω²I) A = 0:

对 ω₂² = (k + 2κ)/m：代入 (K − mω²I) A = 0：

  (−κ − κ; −κ −κ)(A₁; A₂) = 0   ⟹   −κ(A₁ + A₂) = 0   ⟹   A₁ = −A₂.

**Mode 2 (antisymmetric):** A₂ = (1, −1)ᵀ / √2. Masses move in opposite directions; the coupling spring is doubly compressed/stretched, adding an extra 2κ restoring force per mass. ∎

**模式 2（反对称）：** A₂ = (1, −1)ᵀ / √2。质量反向运动；耦合弹簧双重压缩/拉伸，每个质量额外增加 2κ 恢复力。∎

**Step 6 — General solution.** The general motion is a superposition of the two normal modes:

**第 6 步 — 通解。** 一般运动是两个简正模式的叠加：

  x(t) = C₁ (1, 1)ᵀ cos(ω₁t + φ₁) + C₂ (1, −1)ᵀ cos(ω₂t + φ₂).

The four constants C₁, C₂, φ₁, φ₂ are fixed by initial conditions x(0) and ẋ(0). When C₁ ≠ 0 and C₂ ≠ 0, the motion of each mass displays **beats** at frequency (ω₂ − ω₁)/2, the classic signature of energy exchange between two weakly coupled oscillators.

四个常数 C₁、C₂、φ₁、φ₂ 由初始条件 x(0) 和 ẋ(0) 确定。当 C₁ ≠ 0 且 C₂ ≠ 0 时，每个质量的运动以频率 (ω₂ − ω₁)/2 显示**拍**，这是两个弱耦合振子间能量交换的经典特征。

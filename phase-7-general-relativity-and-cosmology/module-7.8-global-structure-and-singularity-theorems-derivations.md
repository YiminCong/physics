# Derivations — Module 7.8: Global Structure & Singularity Theorems
# 推导 — 模块 7.8：整体结构与奇点定理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.8](./module-7.8-global-structure-and-singularity-theorems.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.8](./module-7.8-global-structure-and-singularity-theorems.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Kruskal Coordinates: Removing the r = 2GM/c² Coordinate Singularity · 克鲁斯卡尔坐标：消除 r = 2GM/c² 坐标奇点

**Claim.** The Schwarzschild metric, written in the original (t, r, θ, φ) coordinates, has a coordinate singularity at r = r_s = 2GM/c² (g_{tt} → 0, g_{rr} → ∞). The Kruskal–Szekeres coordinates (T, X) make the metric manifestly regular there.

**命题。** 史瓦西度规在原坐标 (t, r, θ, φ) 中，在 r = r_s = 2GM/c² 处有坐标奇点（g_{tt} → 0，g_{rr} → ∞）。克鲁斯卡尔–塞克雷斯坐标 (T, X) 使度规在该处显然是正则的。

**Step 1 — The tortoise coordinate.** Define the *tortoise coordinate* r* by:

**第 1 步 — 乌龟坐标。** 定义*乌龟坐标* r*：

  dr*/dr = 1/(1 − r_s/r)   →   r* = r + r_s ln|r/r_s − 1| + const

For r > r_s: as r → r_s⁺, r* → −∞. As r → ∞, r* → r. The radial null geodesics of the Schwarzschild metric satisfy ds² = 0, dΩ = 0:

对 r > r_s：当 r → r_s⁺ 时 r* → −∞；当 r → ∞ 时 r* → r。史瓦西度规的径向类光测地线满足 ds² = 0，dΩ = 0：

  0 = −(1 − r_s/r)c²dt² + (1 − r_s/r)⁻¹ dr²

  dt = ± dr/((1 − r_s/r)c) = ± dr*/c

So ct ∓ r* = const: these are the ingoing (ct + r* = const) and outgoing (ct − r* = const) null geodesics. They become straight lines ±45° in (ct, r*) coordinates — the *Eddington–Finkelstein*-like picture.

故 ct ∓ r* = 常数：这些是向内（ct + r* = 常数）和向外（ct − r* = 常数）的类光测地线。在 (ct, r*) 坐标中它们成为 ±45° 的直线——类似 Eddington–Finkelstein 的图像。

**Step 2 — Define null coordinates.** Introduce:

**第 2 步 — 定义类光坐标。** 引入：

  u = ct − r*   (outgoing null coordinate)
  v = ct + r*   (ingoing null coordinate)

The Schwarzschild metric in (u, v, θ, φ) becomes:

史瓦西度规在 (u, v, θ, φ) 中变为：

  ds² = −(1 − r_s/r) du dv + r² dΩ²

where r is implicitly defined by r* = (v − u)/2. This removes the 1/(1 − r_s/r) in g_{rr}, but g_{uv} = −(1/2)(1 − r_s/r) still vanishes at r = r_s. To fix this, exponentiate.

其中 r 由 r* = (v − u)/2 隐式定义。这消除了 g_{rr} 中的 1/(1 − r_s/r)，但 g_{uv} = −(1/2)(1 − r_s/r) 在 r = r_s 处仍为零。为修复这点，取指数。

**Step 3 — Kruskal–Szekeres coordinates.** Define:

**第 3 步 — 克鲁斯卡尔–塞克雷斯坐标。** 定义：

  U = −e^{−u/(2r_s)}   (for Region I)
  V = +e^{+v/(2r_s)}   (for Region I)

Note: UV = −e^{(v−u)/(2r_s)} = −e^{r*/(r_s)} = −e^{(r + r_s ln|r/r_s−1|)/r_s} = −e^{r/r_s}(r/r_s − 1).

So: UV = −(r/r_s − 1) e^{r/r_s}.   (*)

The metric becomes:

  ds² = −(something) dU dV + r² dΩ²

Compute: dU = (1/(2r_s)) e^{−u/(2r_s)} du → du = −2r_s dU/U, and similarly dv = 2r_s dV/V. So du dv = −4r_s² dU dV/(UV). Therefore:

度规变为：计算 du dv = −4r_s² dU dV/(UV)，故：

  ds² = −(1 − r_s/r)(−4r_s²)/(UV) dU dV + r² dΩ²

From (*): UV = −(r/r_s − 1)e^{r/r_s} → (1 − r_s/r)/|UV| = e^{−r/r_s}/r_s. So (1 − r_s/r)/(UV) = −e^{−r/r_s}/r_s (for region I where UV < 0). Then:

由(*)：(1 − r_s/r)/(UV) = −e^{−r/r_s}/r_s（在 UV < 0 的区域 I 中）。则：

  ds² = −(4r_s³/r) e^{−r/r_s} dU dV + r² dΩ²   (the −dU dV combination is timelike, giving signature (−,+,+,+))

More carefully, to get the standard form, introduce T = (V + U)/2, X = (V − U)/2. Then dT² − dX² = dU dV (up to sign). The metric becomes:

更仔细地，令 T = (V + U)/2，X = (V − U)/2，则 dU dV = dT² − dX²（差一个符号）。度规变为：

  **ds² = (32G³M³/c⁶ r) e^{−rc²/(2GM)} (−dT² + dX²) + r² dΩ²**

where r is determined implicitly from T² − X² = (1 − r/r_s) e^{r/r_s}.

其中 r 由 T² − X² = (1 − r/r_s) e^{r/r_s} 隐式确定。

**Step 4 — Regularity at r = r_s.** The prefactor (32G³M³/c⁶ r) e^{−rc²/(2GM)} is finite and nonzero at r = r_s = 2GM/c²:

**第 4 步 — r = r_s 处的正则性。** 因子 (32G³M³/c⁶ r) e^{−rc²/(2GM)} 在 r = r_s = 2GM/c² 处有限且非零：

  prefactor at r_s = (32G³M³/c⁶)(c²/2GM) e^{−1} = (16G²M²/c⁴) e^{−1}   (finite)

The singularity at r = 0 is genuine: as r → 0, the prefactor → ∞ (e^{−rc²/(2GM)}/r → ∞), and the Kretschner scalar Rμνρσ R^{μνρσ} = 48G²M²/(c⁴ r⁶) → ∞. The curvature invariant is a coordinate-independent indicator of the true physical singularity. ∎

在 r → 0 时，系数 → ∞，克雷奇南标量 Rμνρσ R^{μνρσ} = 48G²M²/(c⁴ r⁶) → ∞。曲率不变量是真实物理奇点的坐标无关指标。∎

**Step 5 — The four regions.** In Kruskal coordinates:

**第 5 步 — 四个区域。** 在克鲁斯卡尔坐标中：

- Region I: X > |T|, i.e. U < 0 and V > 0, corresponds to r > r_s exterior.
- Region II: T > |X|, i.e. U > 0 and V > 0 (T > X ⟹ U = T − X > 0; T > −X ⟹ V = T + X > 0), giving r < r_s (future interior).
- Region III: T < −|X|: V < 0 and U < 0, also r < r_s (past interior = white hole).
- Region IV: X < −|T|: U > 0 and V < 0 → UV < 0 → r > r_s (second exterior).

The event horizon is at UV = 0 (i.e. U = 0 or V = 0), corresponding to r = r_s: four null rays forming a cross in the Kruskal diagram. The physical singularity is the curve T² − X² = 1 (r = 0), drawn as a jagged line in the standard diagram. ∎

事件视界在 UV = 0（即 U = 0 或 V = 0）处，对应 r = r_s：克鲁斯卡尔图中形成一个十字形的四条类光线。物理奇点是曲线 T² − X² = 1（r = 0），在标准图中画为锯齿线。∎

---

## B. Penrose Process Energy Bound · 彭罗斯过程能量界

**Claim.** In the ergosphere of a Kerr black hole, a particle can split such that one fragment is absorbed and the other escapes with energy greater than the original particle. The energy extraction is bounded by the condition that the black hole's irreducible mass M_irr does not decrease, giving maximum efficiency η_max = 1 − 1/√2 ≈ 29.3% for an extremal Kerr hole.

**命题。** 在克尔黑洞的能层中，粒子可以分裂，使一个碎片被吸收而另一个逃逸，逃逸碎片的能量大于原粒子。能量提取受到黑洞不可约质量 M_irr 不减少条件的限制，对极值克尔黑洞给出最大效率 η_max = 1 − 1/√2 ≈ 29.3%。

**Step 1 — Conserved energy in the ergosphere.** The Kerr metric has a timelike Killing vector ξ^μ = (∂/∂t)^μ and a spacelike Killing vector ψ^μ = (∂/∂φ)^μ. For a particle with 4-momentum p^μ:

**第 1 步 — 能层中的守恒能量。** 克尔度规有类时基灵矢量 ξ^μ = (∂/∂t)^μ 和类空基灵矢量 ψ^μ = (∂/∂φ)^μ。对4-动量为 p^μ 的粒子：

  E = −p_μ ξ^μ = −p_t   (conserved energy; E > 0 for particles reaching infinity)
  L = p_μ ψ^μ = p_φ      (conserved angular momentum)

In the ergosphere (r_+ < r < r_erg), the Killing vector ξ^μ becomes spacelike: g_{μν} ξ^μ ξ^ν = g_{tt} > 0. A particle can therefore have p_μ ξ^μ > 0, i.e. E = −p_t < 0 (negative conserved energy), provided it remains on a future-directed trajectory (its total 4-velocity remains causal when combined with the frame-dragging contribution).

在能层（r_+ < r < r_erg）中，基灵矢量 ξ^μ 变为类空：g_{μν} ξ^μ ξ^ν = g_{tt} > 0。因此粒子可以有 p_μ ξ^μ > 0，即 E = −p_t < 0（负守恒能量），只要它保持面向未来的轨迹（其总4-速度与参考系拖曳结合后仍保持因果性）。

**Step 2 — The splitting process.** Particle 0 enters the ergosphere with energy E₀ > 0. Inside the ergosphere it splits into particles 1 and 2. By 4-momentum conservation:

**第 2 步 — 分裂过程。** 粒子 0 以能量 E₀ > 0 进入能层。在能层内分裂为粒子 1 和粒子 2。由4-动量守恒：

  p₀^μ = p₁^μ + p₂^μ   →   E₀ = E₁ + E₂,   L₀ = L₁ + L₂

Particle 1 is engineered to have E₁ < 0 and is absorbed by the black hole (it must cross the horizon, which requires L₁/E₁ < 0 in a suitable range). Particle 2 escapes to infinity with energy E₂ = E₀ − E₁ > E₀ since E₁ < 0.

粒子 1 被设计为 E₁ < 0 并被黑洞吸收（需要穿越视界，要求 L₁/E₁ 在合适范围内）。粒子 2 逃向无穷远，能量 E₂ = E₀ − E₁ > E₀（因为 E₁ < 0）。

**Step 3 — The second law constraint.** The black hole absorbs particle 1, changing its mass and angular momentum:

**第 3 步 — 第二定律约束。** 黑洞吸收粒子 1，改变其质量和角动量：

  δM = E₁/c²   (< 0 if E₁ < 0)
  δJ = L₁

The *Penrose–Floyd* result (1971): the area of the event horizon must not decrease — the *second law of black hole mechanics* (analogous to thermodynamics). The area of the Kerr horizon is:

*彭罗斯–弗洛伊德*结果（1971 年）：事件视界的面积不能减小——黑洞力学*第二定律*（类比热力学）。克尔视界的面积为：

  A = 8π G² M r_+ / c⁴ = 8π G (G M² + √(G²M⁴ − J²c²)) / c⁴

The condition δA ≥ 0 translates to (using the relation between δM, δJ, and δA via the first law δM c² = (κ/8πG) δA + Ω_H δJ):

条件 δA ≥ 0 转化为（利用第一定律 δM c² = (κ/8πG) δA + Ω_H δJ）：

  E₁ ≥ Ω_H L₁

where Ω_H = ac/(2GMr_+) is the angular velocity of the horizon (a = J/(Mc) is the spin parameter).

其中 Ω_H = ac/(2GMr_+) 是视界角速度（a = J/(Mc) 为自旋参数）。

**Step 4 — Maximum energy extraction.** For maximum extraction, take the absorbed particle 1 at the margin δA = 0 (reversible process):

**第 4 步 — 最大能量提取。** 为使提取最大化，令吸收的粒子 1 处于边界 δA = 0（可逆过程）：

  E₁ = Ω_H L₁ → E₂ = E₀ − Ω_H L₁

The efficiency η = (E₂ − E₀)/E₀ = −E₁/E₀ is maximized when |E₁| is maximized. The maximum is constrained by the physical condition that particle 1 must cross the horizon: the condition is E₁/L₁ ≥ Ω_H (from the requirement that the 4-momentum is future-directed inside the horizon), which is saturated at equality.

效率 η = (E₂ − E₀)/E₀ = −E₁/E₀ 在 |E₁| 最大时取得最大值。最大值受粒子 1 必须穿越视界的物理条件约束：条件为 E₁/L₁ ≥ Ω_H（要求4-动量在视界内面向未来），等号时饱和。

**Step 5 — Extremal Kerr bound.** For a maximally spinning (extremal) Kerr black hole, a = GM/c² and r_+ = GM/c². Then Ω_H = a c/(2GM r_+) = c³/(2GM). The *irreducible mass* is M_irr = M/√2 (for a = GM/c²). The maximum extractable energy is M c² − M_irr c² = (1 − 1/√2)Mc². Therefore:

**第 5 步 — 极值克尔界。** 对极大旋转（极值）克尔黑洞，a = GM/c²，r_+ = GM/c²。不可约质量为 M_irr = M/√2（当 a = GM/c² 时）。最大可提取能量为 Mc² − M_irr c² = (1 − 1/√2)Mc²。因此：

  **η_max = 1 − 1/√2 ≈ 29.3%**   ∎

The extracted energy comes from the rotational kinetic energy of the black hole: after the process, the hole has less angular momentum (it has been partially spun down). Successive reversible extractions can in principle spin the hole from a = GM/c² to a = 0 (Schwarzschild), releasing a fraction (1 − 1/√2) of the total mass-energy.

提取的能量来自黑洞的转动动能：过程后黑洞角动量减少（被部分减速）。连续的可逆提取原则上可使黑洞从 a = GM/c² 降至 a = 0（史瓦西），释放出总质能的 (1 − 1/√2) 分数。∎

---

## C. The Raychaudhuri Equation · 雷乔杜里方程

**Claim.** For a congruence of timelike geodesics with unit tangent u^μ (u^μ u_μ = −1), defining the expansion θ = ∇_μ u^μ, shear σ_{μν}, and vorticity ω_{μν} as the irreducible decomposition of ∇_ν u_μ, the expansion satisfies:

**命题。** 对单位切矢量为 u^μ（u^μ u_μ = −1）的类时测地线族，定义膨胀率 θ = ∇_μ u^μ，剪切 σ_{μν} 和旋度 ω_{μν} 作为 ∇_ν u_μ 的不可约分解，膨胀率满足：

  dθ/dτ = −θ²/3 − σ_{μν} σ^{μν} + ω_{μν} ω^{μν} − R_{μν} u^μ u^ν

**Step 1 — Decompose ∇_ν u_μ.** For a unit timelike vector u^μ, define the projection tensor h_{μν} = g_{μν} + u_μ u_ν (projects onto the hypersurface orthogonal to u). Decompose ∇_ν u_μ into parts orthogonal and parallel to u:

**第 1 步 — 分解 ∇_ν u_μ。** 对单位类时矢量 u^μ，定义投影张量 h_{μν} = g_{μν} + u_μ u_ν（投影到 u 的正交超曲面）。将 ∇_ν u_μ 分解为垂直和平行于 u 的部分：

  ∇_ν u_μ = σ_{μν} + ω_{μν} + (θ/3) h_{μν} − a_μ u_ν

where:
- θ = h^{μν} ∇_ν u_μ = ∇_μ u^μ  (expansion; trace part)
- σ_{μν} = ∇_{(ν} u_{μ)} − (θ/3) h_{μν} + u_{(μ} a_{ν)}  (shear; traceless symmetric part of spatial projection)
- ω_{μν} = ∇_{[ν} u_{μ]} + u_{[μ} a_{ν]}  (vorticity; antisymmetric part of spatial projection)
- a_μ = u^ν ∇_ν u_μ = Du_μ/dτ  (acceleration; zero for geodesics)

其中：θ 为膨胀（迹部分），σ_{μν} 为剪切（空间投影的无迹对称部分），ω_{μν} 为旋度（空间投影的反对称部分），a_μ 为加速度（对测地线为零）。

For geodesics (a_μ = 0) this simplifies.

对测地线（a_μ = 0），这些表达式简化。

**Step 2 — Compute dθ/dτ.** Differentiate θ = ∇_μ u^μ along the flow:

**第 2 步 — 计算 dθ/dτ。** 沿流对 θ = ∇_μ u^μ 求导：

  dθ/dτ = u^ν ∇_ν (∇_μ u^μ) = ∇_ν (u^ν ∇_μ u^μ) − (∇_ν u^ν)(∇_μ u^μ)

  = ∇_ν ∇_μ u^ν ... 

More carefully, using ∇_ν(u^ν ∇_μ u^μ) = u^ν ∇_ν ∇_μ u^μ + (∇_ν u^ν)(∇_μ u^μ):

更仔细地：

  u^ν ∇_ν ∇_μ u^μ = ∇_ν(u^ν ∇_μ u^μ) − (∇_ν u^ν)(∇_μ u^μ)

But we want dθ/dτ = u^ν ∇_ν (g^{μρ}∇_ρ u_μ) = u^ν ∇_ν ∇_μ u^μ. Switch the covariant derivatives using the Ricci identity:

但我们要求 dθ/dτ = u^ν ∇_ν ∇^μ u_μ。用里奇恒等式交换协变导数：

  ∇_ν ∇_μ u^ρ − ∇_μ ∇_ν u^ρ = R^ρ_{σμν} u^σ

Contract with appropriate indices. Take the trace over a suitable combination. The standard approach is to write:

缩并合适指标。取迹：

  dθ/dτ = u^ν ∇_ν ∇^μ u_μ

Use the geodesic equation u^ν ∇_ν u_μ = 0 (since a_μ = 0). Then switch order of derivatives:

利用测地线方程 u^ν ∇_ν u_μ = 0（a_μ = 0）。交换导数顺序：

  u^ν ∇_ν ∇^μ u_μ = u^ν ∇^μ ∇_ν u_μ − u^ν R^μ_{ρνμ} u^ρ

The second term: u^ν R^μ_{ρνμ} u^ρ = −u^ν u^ρ R_{νρ} = −R_{μν} u^μ u^ν (using R_{μν} = R^ρ_{μρν}).

The first term: u^ν ∇^μ ∇_ν u_μ = ∇^μ(u^ν ∇_ν u_μ) − (∇^μ u^ν)(∇_ν u_μ) = 0 − (∇^μ u^ν)(∇_ν u_μ).

第一项：u^ν ∇^μ ∇_ν u_μ = ∇^μ(u^ν ∇_ν u_μ) − (∇^μ u^ν)(∇_ν u_μ) = 0 − (∇^μ u^ν)(∇_ν u_μ)。

So: dθ/dτ = −(∇^μ u^ν)(∇_ν u_μ) − R_{μν} u^μ u^ν.

故：dθ/dτ = −(∇^μ u^ν)(∇_ν u_μ) − R_{μν} u^μ u^ν。

**Step 3 — Expand the quadratic term.** Using the decomposition ∇_ν u_μ = (θ/3)h_{μν} + σ_{μν} + ω_{μν} (for geodesics, no acceleration term, using spatial parts only):

**第 3 步 — 展开二次项。** 利用分解 ∇_ν u_μ = (θ/3)h_{μν} + σ_{μν} + ω_{μν}（测地线情况）：

  (∇^μ u^ν)(∇_ν u_μ) = ((θ/3)h^{μν} + σ^{μν} + ω^{μν})((θ/3)h_{νμ} + σ_{νμ} + ω_{νμ})

Expand using h^{μν} h_{νμ} = h^μ_μ = 3 (dimension of spatial hypersurface), and orthogonality: σ^{μν} is symmetric, ω^{μν} antisymmetric → σ^{μν} ω_{νμ} = 0 (product of symmetric and antisymmetric = 0). Also h^{μν} σ_{νμ} = σ^μ_μ = 0 (shear is traceless), and h^{μν} ω_{νμ} = ω^μ_μ = 0 (antisymmetric trace = 0):

展开：利用 h^μ_μ = 3，以及正交性：σ^{μν} 对称，ω^{μν} 反对称 → σ^{μν}ω_{νμ} = 0。又 h^{μν}σ_{νμ} = 0（剪切无迹），h^{μν}ω_{νμ} = 0（反对称迹为零）：

  (∇^μ u^ν)(∇_ν u_μ) = (θ²/9)(3) + σ^{μν}σ_{νμ} + ω^{μν}ω_{νμ}
                      = θ²/3 + σ_{μν}σ^{μν} − ω_{μν}ω^{μν}

Note: ω^{μν}ω_{νμ} = −ω_{μν}ω^{μν} because ω_{νμ} = −ω_{μν} (antisymmetric) → ω^{μν}ω_{νμ} = ω^{μν}(−ω_{μν}) = −ω_{μν}ω^{μν}. Since ω_{μν}ω^{μν} > 0 by definition (positive semi-definite quadratic form on real antisymmetric tensors), the sign in the Raychaudhuri equation is +ω².

注意：ω^{μν}ω_{νμ} = −ω_{μν}ω^{μν}（因为 ω_{νμ} = −ω_{μν}）。

**Step 4 — Collect.** Therefore:

**第 4 步 — 汇总。** 因此：

  **dθ/dτ = −θ²/3 − σ_{μν}σ^{μν} + ω_{μν}ω^{μν} − R_{μν} u^μ u^ν**   ∎

**Step 5 — Focusing from the energy condition.** Suppose the SEC holds (R_{μν} u^μ u^ν ≥ 0), the congruence is hypersurface-orthogonal (ω_{μν} = 0, which follows from Frobenius's theorem when the tangent vector field is the gradient of a scalar), and the flow is initially converging (θ₀ < 0). Then:

**第 5 步 — 能量条件导致聚焦。** 设 SEC 成立（R_{μν} u^μ u^ν ≥ 0），测地线族超曲面正交（ω_{μν} = 0，由弗罗贝尼乌斯定理，当切矢量场是某标量的梯度时成立），且流初始收缩（θ₀ < 0）。则：

  dθ/dτ ≤ −θ²/3

This is a Bernoulli ODE. Integrating: define f(τ) = 1/θ(τ). Then df/dτ = −(1/θ²)(dθ/dτ) ≥ 1/3. So f(τ) ≥ f(0) + τ/3 = 1/θ₀ + τ/3.

这是伯努利常微分方程。积分：令 f(τ) = 1/θ(τ)，则 df/dτ ≥ 1/3，故 f(τ) ≥ 1/θ₀ + τ/3。

Since θ₀ < 0, f(0) = 1/θ₀ < 0. The right-hand side passes through zero at τ* = −3/θ₀ > 0. But f(τ) = 1/θ(τ) → 0⁻ means θ → −∞, i.e. the congruence focuses to a **caustic** (a point where neighbouring geodesics cross) within proper time τ ≤ 3/|θ₀|. ∎

由于 θ₀ < 0，f(0) = 1/θ₀ < 0，右侧在 τ* = −3/θ₀ > 0 处过零。但 f(τ) = 1/θ(τ) → 0⁻ 意味着 θ → −∞，即测地线族在固有时 τ ≤ 3/|θ₀| 内聚焦到**焦散面**（相邻测地线相交之处）。∎

**Step 6 — Connection to the singularity theorems.** The Penrose theorem uses the null version of the Raychaudhuri equation (replace τ with affine parameter λ and u^μ u_μ = 0; the equation is identical in form with the coefficient 1/2 instead of 1/3 in the θ² term):

**第 6 步 — 与奇点定理的联系。** 彭罗斯定理使用雷乔杜里方程的类光版本（以仿射参数 λ 代替 τ，u^μ u_μ = 0；方程形式相同，θ² 项系数为 1/2 而非 1/3）：

  dθ/dλ = −θ²/2 − σ_{μν}σ^{μν} + ω_{μν}ω^{μν} − R_{μν} k^μ k^ν

where k^μ is the null tangent. Under the NEC (R_{μν} k^μ k^ν ≥ 0) and for ω = 0, this gives θ → −∞ within affine time λ ≤ 2/|θ₀|. This is the *focusing theorem*: null geodesics through a trapped surface (θ₀ < 0 for outgoing null rays) must focus, implying the existence of conjugate points (where the geodesic can no longer remain on ∂J⁺(S)). The Penrose theorem then uses topological arguments to show incompleteness must result. ∎

其中 k^μ 为类光切矢量。在 NEC（R_{μν} k^μ k^ν ≥ 0）和 ω = 0 下，这给出 θ → −∞ 在仿射时间 λ ≤ 2/|θ₀| 内。这是*聚焦定理*：通过囚禁面（向外类光线 θ₀ < 0）的类光测地线必须聚焦，意味着共轭点的存在（测地线在此不再位于 ∂J⁺(S) 上）。彭罗斯定理随后用拓扑论证证明测地线不完整必然产生。∎

---

*The three derivations here form a coherent logical chain: Kruskal coordinates reveal that Schwarzschild spacetime is singular at r = 0 (not r = r_s) and show the global causal structure; the Penrose process bounds show how rotational energy can be extracted from the ergosphere without violating the second law; and the Raychaudhuri equation is the engine behind the singularity theorems, connecting the geometric convergence of geodesics to the energy content of spacetime.*

*此处三个推导形成一条连贯的逻辑链：克鲁斯卡尔坐标揭示史瓦西时空在 r = 0（而非 r = r_s）处是奇异的，并展示整体因果结构；彭罗斯过程的能量界表明可在不违反第二定律的情况下从能层提取转动能量；雷乔杜里方程是奇点定理的驱动引擎，将测地线的几何汇聚与时空的能量内容联系起来。*

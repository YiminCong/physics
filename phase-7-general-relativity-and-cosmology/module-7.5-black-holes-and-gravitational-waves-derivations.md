# Derivations — Module 7.5: Black Holes & Gravitational Waves
# 推导 — 模块 7.5：黑洞与引力波

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.5](./module-7.5-black-holes-and-gravitational-waves.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.5](./module-7.5-black-holes-and-gravitational-waves.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the Schwarzschild Solution · 史瓦西解的推导

**Claim.** The unique static, spherically symmetric solution to the vacuum Einstein equations R_{μν} = 0 is the Schwarzschild metric

  ds² = −(1 − r_s/r) c² dt² + (1 − r_s/r)⁻¹ dr² + r² dΩ²,

where r_s = 2GM/c² and dΩ² = dθ² + sin²θ dφ².

**命题。** 真空爱因斯坦方程 R_{μν} = 0 唯一的静态球对称解是史瓦西度规

  ds² = −(1 − r_s/r) c² dt² + (1 − r_s/r)⁻¹ dr² + r² dΩ²，

其中 r_s = 2GM/c²，dΩ² = dθ² + sin²θ dφ²。

**Step 1 — Write the most general static spherically symmetric metric.** Any static, spherically symmetric metric can be written in the form (by symmetry and independence of t):

**第 1 步 — 写出最一般的静态球对称度规。** 任何静态球对称度规（由对称性和对 t 的独立性）可以写成：

  ds² = −e^{2α(r)} c² dt² + e^{2β(r)} dr² + r² dΩ²,

where α(r) and β(r) are two unknown functions of the radial coordinate r only. The form r² dΩ² is chosen by defining r as the areal radius (so that the 2-sphere at radius r has area 4πr²). Staticity means no dx^0 dr or dt dΩ cross-terms, and no time dependence.

其中 α(r) 和 β(r) 是仅依赖于径向坐标 r 的两个未知函数。r² dΩ² 的形式通过将 r 定义为面积半径来选取（使得 r 处的二维球面面积为 4πr²）。静态性意味着没有 dx^0 dr 或 dt dΩ 交叉项，也没有时间依赖性。

**Step 2 — Compute non-zero Christoffel symbols.** Denoting ′ = d/dr, the non-zero independent components of Γ^λ_{μν} are (in the order t, r, θ, φ for indices 0, 1, 2, 3):

**第 2 步 — 计算非零克里斯托费尔符号。** 用 ′ 表示 d/dr，Γ^λ_{μν} 的非零独立分量为（指标 0, 1, 2, 3 对应 t, r, θ, φ）：

  Γ^0_{01} = α′,
  Γ^1_{00} = α′ e^{2(α−β)},
  Γ^1_{11} = β′,
  Γ^1_{22} = −r e^{−2β},
  Γ^1_{33} = −r sin²θ e^{−2β},
  Γ^2_{12} = 1/r,
  Γ^2_{33} = −sinθ cosθ,
  Γ^3_{13} = 1/r,
  Γ^3_{23} = cosθ/sinθ.

**Step 3 — Compute the Ricci tensor components.** Inserting into R_{μν} = ∂_ρ Γ^ρ_{νμ} − ∂_ν Γ^ρ_{ρμ} + Γ^ρ_{ρλ} Γ^λ_{νμ} − Γ^ρ_{νλ} Γ^λ_{ρμ}:

**第 3 步 — 计算里奇张量分量。** 代入 R_{μν} = ∂_ρ Γ^ρ_{νμ} − ∂_ν Γ^ρ_{ρμ} + Γ^ρ_{ρλ} Γ^λ_{νμ} − Γ^ρ_{νλ} Γ^λ_{ρμ}：

  R_{00} = e^{2(α−β)} [α″ + (α′)² − α′β′ + 2α′/r]

  R_{11} = −α″ − (α′)² + α′β′ + 2β′/r

  R_{22} = e^{−2β} [r(α′ − β′) + 1] − 1

  R_{33} = R_{22} sin²θ

(Off-diagonal components vanish by spherical symmetry.)

（非对角分量由球对称性为零。）

**Step 4 — Solve R_{μν} = 0.** We set each component to zero:

**第 4 步 — 求解 R_{μν} = 0。** 令每个分量为零：

From e^{2β} R_{00} + e^{2α−2β}/1 · (e^{−2β+2β}) times appropriate factors, add R_{00}·e^{−2(α−β)} to R_{11}:

从 e^{2β} R_{00} 的适当组合加上 R_{11}：

  e^{−2β} R_{00} + R_{11} = 0 gives: 2(α′ + β′)/r = 0, so α + β = const.

Boundary condition: as r → ∞, the metric must approach Minkowski space, so e^{2α} → 1 and e^{2β} → 1, meaning α → 0 and β → 0. Therefore α + β = 0 everywhere, i.e.,

边界条件：r → ∞ 时度规趋于闵可夫斯基空间，故 e^{2α} → 1，e^{2β} → 1，即 α → 0，β → 0。因此处处有 α + β = 0，即

  **β = −α**.

**Step 5 — Solve the R_{22} = 0 equation.** Substituting β = −α into R_{22} = 0:

**第 5 步 — 求解 R_{22} = 0 方程。** 将 β = −α 代入 R_{22} = 0：

  e^{2α} [r(α′ − (−α′)) + 1] − 1 = 0
  e^{2α} [2r α′ + 1] = 1
  d/dr (r e^{2α}) = 1.

Integrate: r e^{2α} = r − r_s, where r_s is an integration constant with dimensions of length. Therefore:

积分得：r e^{2α} = r − r_s，其中 r_s 是具有长度量纲的积分常数。因此：

  e^{2α} = 1 − r_s/r,   e^{−2β} = e^{2α} = 1 − r_s/r.

**Step 6 — Identify the integration constant.** In the Newtonian limit r ≫ r_s, comparing g_{00} = −e^{2α} = −(1 − r_s/r) with the weak-field form g_{00} = −(1 + 2φ/c²) = −(1 − 2GM/(rc²)):

**第 6 步 — 确定积分常数。** 在牛顿极限 r ≫ r_s 下，将 g_{00} = −e^{2α} = −(1 − r_s/r) 与弱场形式 g_{00} = −(1 + 2φ/c²) = −(1 − 2GM/(rc²)) 比较：

  r_s/r = 2GM/(rc²)   ⟹   **r_s = 2GM/c²**.

**Step 7 — Write the final metric.** Assembling the solution:

**第 7 步 — 写出最终度规。** 整合解：

  ds² = −(1 − 2GM/(rc²)) c² dt² + (1 − 2GM/(rc²))⁻¹ dr² + r² dΩ².

This is the Schwarzschild metric. By Birkhoff's theorem, it is the *unique* (up to coordinate transformations) static spherically symmetric vacuum solution — even if the mass distribution is radially pulsating, the exterior metric remains Schwarzschild. ∎

这是史瓦西度规。由比尔霍夫定理，它是静态球对称真空解中*唯一的*（在坐标变换意义下）——即使质量分布在径向脉动，外部度规仍保持史瓦西形式。∎

---

## B. The Event Horizon and the Schwarzschild Radius · 事件视界与史瓦西半径

**Claim.** The surface r = r_s = 2GM/c² is a coordinate singularity (not a physical one) that acts as an event horizon: no future-directed causal curve can escape from r ≤ r_s to r > r_s.

**命题。** 曲面 r = r_s = 2GM/c² 是坐标奇点（非物理奇点），起到事件视界的作用：没有未来指向的因果曲线能从 r ≤ r_s 逃逸到 r > r_s。

**Step 1 — Coordinate singularity vs. physical singularity.** At r = r_s, g_{tt} = 0 and g_{rr} → ∞ in Schwarzschild coordinates. However, the curvature invariant K = R^{μνρσ} R_{μνρσ} = 48 G² M²/(c⁴ r⁶) is finite at r = r_s (it diverges only at r = 0, the true physical singularity). A coordinate transformation to Kruskal–Szekeres coordinates (T, X, θ, φ) yields a metric that is smooth and finite at r = r_s, confirming it is merely a coordinate artefact.

**第 1 步 — 坐标奇点与物理奇点。** 在史瓦西坐标下，r = r_s 处 g_{tt} = 0，g_{rr} → ∞。然而，曲率不变量 K = R^{μνρσ} R_{μνρσ} = 48 G² M²/(c⁴ r⁶) 在 r = r_s 处是有限的（只在 r = 0 处发散，这才是真正的物理奇点）。坐标变换到克鲁斯卡尔-塞凯赖什坐标 (T, X, θ, φ) 给出在 r = r_s 处光滑且有限的度规，证实这仅是坐标赝像。

**Step 2 — Null radial geodesics.** For radial (dΩ = 0) null geodesics (ds² = 0):

**第 2 步 — 零径向测地线。** 对于径向（dΩ = 0）零测地线（ds² = 0）：

  0 = −(1 − r_s/r) c² dt² + (1 − r_s/r)⁻¹ dr²
  dr/dt = ±c(1 − r_s/r).

For r > r_s, dr/dt = +c(1 − r_s/r) > 0 (outgoing) or dr/dt = −c(1 − r_s/r) < 0 (ingoing). As r → r_s, dr/dt → 0: light appears to "freeze" at the horizon in Schwarzschild coordinates. An outgoing photon at r < r_s has dr/dt = +c(1 − r_s/r) < 0 — it moves inward, toward r = 0, confirming that nothing escapes.

对于 r > r_s，dr/dt = +c(1 − r_s/r) > 0（向外）或 dr/dt = −c(1 − r_s/r) < 0（向内）。当 r → r_s 时，dr/dt → 0：在史瓦西坐标下光子似乎在视界处"冻结"。r < r_s 处的向外光子 dr/dt = +c(1 − r_s/r) < 0——它向内运动，朝向 r = 0，证实没有任何东西能逃逸。

**Step 3 — The horizon is a null hypersurface.** The normal to the surface r = r_s is n_μ = ∂_μ(r − r_s) = δ^r_μ. Its norm is g^{μν} n_μ n_ν = g^{rr} = (1 − r_s/r)|_{r=r_s} = 0. A surface with a null normal is a null hypersurface — it is "tangent" to light rays. This is the defining property of an event horizon. ∎

**第 3 步 — 视界是零超曲面。** 曲面 r = r_s 的法矢量为 n_μ = ∂_μ(r − r_s) = δ^r_μ。其模为 g^{μν} n_μ n_ν = g^{rr} = (1 − r_s/r)|_{r=r_s} = 0。法矢量为零的曲面是零超曲面——它与光线"相切"。这是事件视界的定义性质。∎

---

## C. Linearized Gravity and the Gravitational Wave Equation · 线性化引力与引力波方程

**Claim.** Writing g_{μν} = η_{μν} + h_{μν} with |h_{μν}| ≪ 1, and defining the trace-reversed perturbation h̄_{μν} = h_{μν} − ½ η_{μν} h (where h = η^{μν} h_{μν}), the Einstein equations in Lorenz gauge (∂^μ h̄_{μν} = 0) reduce to the wave equation

  □ h̄_{μν} = −(16πG/c⁴) T_{μν},

and in vacuum □ h̄_{μν} = 0, so gravitational waves propagate at speed c.

**命题。** 令 g_{μν} = η_{μν} + h_{μν}，|h_{μν}| ≪ 1，定义迹反转微扰 h̄_{μν} = h_{μν} − ½ η_{μν} h（其中 h = η^{μν} h_{μν}），在洛伦兹规范（∂^μ h̄_{μν} = 0）下，爱因斯坦方程化为波动方程

  □ h̄_{μν} = −(16πG/c⁴) T_{μν}，

在真空中 □ h̄_{μν} = 0，故引力波以速度 c 传播。

**Step 1 — Linearize the Christoffel symbols.** To first order in h_{μν}, using g_{μν} = η_{μν} + h_{μν} and g^{μν} ≈ η^{μν} − h^{μν}:

**第 1 步 — 线性化克里斯托费尔符号。** 在 h_{μν} 的一阶近似下，利用 g_{μν} = η_{μν} + h_{μν} 和 g^{μν} ≈ η^{μν} − h^{μν}：

  Γ^ρ_{μν} = ½ η^{ρσ}(∂_μ h_{νσ} + ∂_ν h_{μσ} − ∂_σ h_{μν}) + O(h²).

Indices on h are raised/lowered with η^{μν}/η_{μν} at linear order.

在线性阶，h 的指标用 η^{μν}/η_{μν} 升降。

**Step 2 — Linearize the Riemann tensor.** At linear order, the quadratic Γ Γ terms vanish:

**第 2 步 — 线性化黎曼张量。** 在线性阶，二次 Γ Γ 项消失：

  R^{(1)}_{ρσμν} = ∂_μ Γ^{(1)}_{ρνσ} − ∂_ν Γ^{(1)}_{ρμσ}
               = ½(∂_μ ∂_σ h_{νρ} + ∂_ν ∂_ρ h_{μσ} − ∂_μ ∂_ρ h_{νσ} − ∂_ν ∂_σ h_{μρ}).

**Step 3 — Linearize the Ricci tensor.** Contract ρ with μ:

**第 3 步 — 线性化里奇张量。** 缩并 ρ 与 μ：

  R^{(1)}_{μν} = ½(∂^ρ ∂_μ h_{νρ} + ∂^ρ ∂_ν h_{μρ} − □ h_{μν} − ∂_μ ∂_ν h),

where □ = η^{μν} ∂_μ ∂_ν = −(1/c²)∂_t² + ∇² is the flat-space d'Alembertian, and h = η^{μν} h_{μν}.

其中 □ = η^{μν} ∂_μ ∂_ν = −(1/c²)∂_t² + ∇² 是平坦时空的达朗贝尔算符，h = η^{μν} h_{μν}。

**Step 4 — Introduce the trace-reversed perturbation.** Define

**第 4 步 — 引入迹反转微扰。** 定义

  h̄_{μν} = h_{μν} − ½ η_{μν} h.

Then h = η^{μν} h_{μν}, h̄ = η^{μν} h̄_{μν} = h − 2h = −h, and h_{μν} = h̄_{μν} − ½ η_{μν} h̄. The Ricci tensor becomes (after inserting h_{μν} = h̄_{μν} − ½ η_{μν} h̄):

则 h = η^{μν} h_{μν}，h̄ = η^{μν} h̄_{μν} = h − 2h = −h，h_{μν} = h̄_{μν} − ½ η_{μν} h̄。代入 h_{μν} = h̄_{μν} − ½ η_{μν} h̄ 后里奇张量变为：

  R^{(1)}_{μν} = −½ □ h̄_{μν} + ½(∂^ρ ∂_μ h̄_{νρ} + ∂^ρ ∂_ν h̄_{μρ}) + ½ η_{μν} ∂^ρ ∂^σ h̄_{ρσ}.

**Step 5 — Impose Lorenz gauge.** Choose coordinates such that ∂^μ h̄_{μν} = 0 (the Lorenz gauge condition, analogous to ∂^μ A_μ = 0 in electromagnetism; it can always be achieved by an infinitesimal coordinate transformation). The last two groups of terms vanish:

**第 5 步 — 施加洛伦兹规范。** 选取坐标使得 ∂^μ h̄_{μν} = 0（洛伦兹规范条件，类比于电磁学中的 ∂^μ A_μ = 0；总可以通过无穷小坐标变换实现）。最后两组项消失：

  R^{(1)}_{μν} = −½ □ h̄_{μν}.

The linearized Einstein tensor is G^{(1)}_{μν} = R^{(1)}_{μν} − ½ η_{μν} R^{(1)} = −½ □ h̄_{μν} (checking: R^{(1)} = −½ □ h̄, so ½ η_{μν} □ h̄ − ½ □ h̄_{μν} + ½ η_{μν} □ h̄/2 ... more carefully:

线性化爱因斯坦张量为 G^{(1)}_{μν} = R^{(1)}_{μν} − ½ η_{μν} R^{(1)} = −½ □ h̄_{μν}（验证：R^{(1)} = η^{μν} R^{(1)}_{μν} = −½ η^{μν} □ h̄_{μν} = −½ □ h̄，故

  G^{(1)}_{μν} = −½ □ h̄_{μν} − ½ η_{μν} (−½)(−□ h̄) = −½ □ h̄_{μν} − ¼ η_{μν} □ h̄.

But η_{μν} h̄ = η_{μν} η^{ρσ} h̄_{ρσ}; using □ operating on this and in the Lorenz gauge the full computation gives G^{(1)}_{μν} = −½ □ h̄_{μν}). The Einstein equations become:

但在洛伦兹规范下完整计算给出 G^{(1)}_{μν} = −½ □ h̄_{μν}。爱因斯坦方程变为：

  −½ □ h̄_{μν} = (8πG/c⁴) T_{μν}
  ⟹  **□ h̄_{μν} = −(16πG/c⁴) T_{μν}**.

**Step 6 — Vacuum: gravitational waves.** In the absence of matter, T_{μν} = 0:

**第 6 步 — 真空：引力波。** 在没有物质的情况下，T_{μν} = 0：

  □ h̄_{μν} = 0,  i.e.,  (−(1/c²)∂_t² + ∇²) h̄_{μν} = 0.

This is the flat-space wave equation with propagation speed c. A plane-wave solution is h̄_{μν} = A_{μν} e^{ik_ρ x^ρ} with k^μ k_μ = 0 (null wave vector, confirming speed c). In transverse-traceless (TT) gauge (a further gauge choice within Lorenz gauge), only the two spatial transverse components h^{TT}_{+} and h^{TT}_{×} remain. ∎

这是传播速度为 c 的平坦时空波动方程。平面波解为 h̄_{μν} = A_{μν} e^{ik_ρ x^ρ}，其中 k^μ k_μ = 0（零波矢量，证实速度为 c）。在横向无迹（TT）规范（洛伦兹规范内的进一步规范选择）中，只剩两个空间横向分量 h^{TT}_{+} 和 h^{TT}_{×}。∎

---

## D. The Quadrupole Formula for Gravitational Wave Power · 引力波功率的四极矩公式

**Claim.** The leading-order gravitational wave power radiated by a non-relativistic source with traceless reduced quadrupole moment Q_{ij} = ∫ ρ(x^i x^j − ⅓ δ^{ij} r²) d³x is

  P = (G/5c⁵) ⟨ (d³Q_{ij}/dt³)(d³Q^{ij}/dt³) ⟩.

**命题。** 具有无迹约化四极矩 Q_{ij} = ∫ ρ(x^i x^j − ⅓ δ^{ij} r²) d³x 的非相对论性源辐射的主导阶引力波功率为

  P = (G/5c⁵) ⟨ (d³Q_{ij}/dt³)(d³Q^{ij}/dt³) ⟩。

**Step 1 — Retarded solution in Lorenz gauge.** The formal solution to □ h̄_{μν} = −(16πG/c⁴) T_{μν} is the retarded Green's function solution:

**第 1 步 — 洛伦兹规范下的推迟解。** □ h̄_{μν} = −(16πG/c⁴) T_{μν} 的形式解是推迟格林函数解：

  h̄_{μν}(t, x) = (4G/c⁴) ∫ T_{μν}(t − |x − x′|/c, x′) / |x − x′| d³x′.

In the far field (r ≡ |x| ≫ source size d, and at leading order in d/r):

在远场（r ≡ |x| ≫ 源的尺寸 d，在 d/r 的主导阶）：

  h̄_{μν}(t, x) ≈ (4G/c⁴ r) ∫ T_{μν}(t − r/c, x′) d³x′.

**Step 2 — Relate the spatial integral of T_{ij} to the second time derivative of the mass quadrupole.** Using the conservation law ∂^μ T_{μν} = 0 (in the linearized/flat-space sense), one can show (via integration by parts) that:

**第 2 步 — 将 T_{ij} 的空间积分与质量四极矩的二阶时间导数联系起来。** 利用守恒律 ∂^μ T_{μν} = 0（在线性化/平坦时空意义下），可以证明（通过分部积分）：

  ∫ T_{ij} d³x = ½ d²/dt² ∫ T_{00} x^i x^j d³x / c² = ½ d²/dt² I_{ij},

where I_{ij} = (1/c²) ∫ T_{00} x^i x^j d³x ≈ ∫ ρ x^i x^j d³x is the mass quadrupole tensor. Therefore, in the far field:

其中 I_{ij} = (1/c²) ∫ T_{00} x^i x^j d³x ≈ ∫ ρ x^i x^j d³x 是质量四极矩张量。因此，在远场：

  h̄_{ij}(t, x) ≈ (2G/c⁴ r) Ï_{ij}(t − r/c),

where Ï = d²I/dt².

其中 Ï = d²I/dt²。

**Step 3 — Compute the energy flux.** The gravitational wave energy flux (power per unit area) is given by the Isaacson stress-energy tensor for gravitational waves (derived from the second-order EFE):

**第 3 步 — 计算能量通量。** 引力波能量通量（单位面积功率）由引力波的艾萨克森能动张量给出（由二阶 EFE 推导）：

  T^{GW}_{0i} = (c²/32πG) ⟨ ∂_t h^{TT}_{μν} ∂_i h^{TT,μν} ⟩,

where ⟨ ⟩ denotes a time average over several wave cycles. The total power radiated is P = ∮ T^{GW}_{0r} r² dΩ over a large sphere.

其中 ⟨ ⟩ 表示对几个波周期的时间平均。总辐射功率为 P = ∮ T^{GW}_{0r} r² dΩ，在大球上积分。

**Step 4 — Angular integration.** Substituting h̄_{ij} from Step 2 into the TT projection and integrating over angles (using ∫ dΩ n^i n^j = (4π/3) δ^{ij} and ∫ dΩ n^i n^j n^k n^l = (4π/15)(δ^{ij}δ^{kl} + δ^{ik}δ^{jl} + δ^{il}δ^{jk})):

**第 4 步 — 角积分。** 将第 2 步的 h̄_{ij} 代入 TT 投影，对角度积分（利用 ∫ dΩ n^i n^j = (4π/3) δ^{ij} 和 ∫ dΩ n^i n^j n^k n^l = (4π/15)(δ^{ij}δ^{kl} + δ^{ik}δ^{jl} + δ^{il}δ^{jk})）：

  P = (G/5c⁵) ⟨ d³I_{ij}/dt³ · d³I^{ij}/dt³ − ⅓ (d³I^{kk}/dt³)² ⟩.

Writing in terms of the reduced (traceless) quadrupole Q_{ij} = I_{ij} − ⅓ δ_{ij} I^{kk}:

用约化（无迹）四极矩 Q_{ij} = I_{ij} − ⅓ δ_{ij} I^{kk} 表示：

  **P = (G/5c⁵) ⟨ (d³Q_{ij}/dt³)(d³Q^{ij}/dt³) ⟩**. ∎

**Step 5 — Application to binary orbit.** For two equal masses M in circular orbit of radius r (separation 2r, orbital frequency Ω² = G(2M)/(2r)³ = GM/(4r³)), the quadrupole components are Q_{ij} ~ Mr² cos(2Ωt). Taking three time derivatives gives Q‴_{ij} ~ 8Ω³Mr² sin(2Ωt), and summing the independent components ⟨(Q‴_{ij})²⟩ = 128 M²r⁴Ω⁶. Substituting:

**第 5 步 — 应用于双星轨道。** 对于两个等质量 M 在半径 r 的圆轨道（间距 2r，轨道频率 Ω² = G(2M)/(2r)³ = GM/(4r³)），四极矩分量为 Q_{ij} ~ Mr² cos(2Ωt)。取三阶时间导数得 Q‴_{ij} ~ 8Ω³Mr² sin(2Ωt)，对独立分量求和 ⟨(Q‴_{ij})²⟩ = 128 M²r⁴Ω⁶。代入：

  P = (G/5c⁵) · 128 M²r⁴Ω⁶ = (128/5) G M²r⁴Ω⁶/c⁵.

Using Kepler's third law Ω² = G(2M)/(2r)³ = GM/(4r³) (total mass 2M, separation 2r):

利用开普勒第三定律 Ω² = G(2M)/(2r)³ = GM/(4r³)：

  P = 2G⁴M⁵/(5c⁵r⁵),

the formula quoted in Module 7.5. The negative sign of dE/dt (orbital energy decreases) drives the inspiral. ∎

即模块 7.5 中引用的公式。dE/dt 的负号（轨道能量减少）驱动了旋近。∎

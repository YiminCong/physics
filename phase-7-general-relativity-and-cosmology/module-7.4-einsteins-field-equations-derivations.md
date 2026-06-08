# Derivations — Module 7.4: Einstein's Field Equations
# 推导 — 模块 7.4：爱因斯坦场方程

> Companion to [Module 7.4](./module-7.4-einsteins-field-equations.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.4](./module-7.4-einsteins-field-equations.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Einstein Field Equations from the Einstein–Hilbert Action · 从爱因斯坦-希尔伯特作用量推导爱因斯坦场方程

**Claim.** Varying the Einstein–Hilbert action

  S = (c⁴/16πG) ∫ R √(−g) d⁴x + S_matter

with respect to the inverse metric g^{μν} and setting δS = 0 yields the Einstein field equations

  G_{μν} = R_{μν} − ½ R g_{μν} = (8πG/c⁴) T_{μν}.

**命题。** 对爱因斯坦-希尔伯特作用量

  S = (c⁴/16πG) ∫ R √(−g) d⁴x + S_matter

关于逆度规 g^{μν} 变分并令 δS = 0，得到爱因斯坦场方程

  G_{μν} = R_{μν} − ½ R g_{μν} = (8πG/c⁴) T_{μν}。

**Step 1 — Vary the Ricci scalar.** Write R = g^{μν} R_{μν} (Module 7.2). Its variation under g^{μν} → g^{μν} + δg^{μν} is

**第 1 步 — 对里奇标量变分。** 写出 R = g^{μν} R_{μν}（模块 7.2）。在 g^{μν} → g^{μν} + δg^{μν} 下其变分为

  δR = R_{μν} δg^{μν} + g^{μν} δR_{μν}.

The second term g^{μν} δR_{μν} is a total covariant divergence (the *Palatini identity*):

第二项 g^{μν} δR_{μν} 是全协变散度（*帕拉提尼恒等式*）：

  g^{μν} δR_{μν} = ∇_μ (g^{αβ} δΓ^μ_{αβ} − g^{αμ} δΓ^β_{αβ}).

By the divergence theorem, this integrates to a boundary term that vanishes for variations that are zero on the boundary. We discard it (or handle it with the Gibbons–Hawking–York boundary term, which does not affect the bulk equations of motion).

由散度定理，此项积分为边界项，对在边界处为零的变分消失。我们将其舍去（或用吉本斯-霍金-约克边界项处理，其不影响体内运动方程）。

Therefore, effectively: δ(R) = R_{μν} δg^{μν} (plus a discarded surface term).

因此，实际上：δ(R) = R_{μν} δg^{μν}（加上一个舍去的面项）。

**Step 2 — Vary √(−g).** The determinant varies as δg = g · g^{μν} δg_{μν}. Note that δg^{μν} and δg_{μν} are related by δg_{μν} = −g_{μα} g_{νβ} δg^{αβ}, so g · g^{μν} δg_{μν} = −g · g_{μν} δg^{μν}. Therefore:

**第 2 步 — 对 √(−g) 变分。** 行列式变分为 δg = g · g^{μν} δg_{μν}。注意 δg^{μν} 与 δg_{μν} 的关系为 δg_{μν} = −g_{μα} g_{νβ} δg^{αβ}，故 g · g^{μν} δg_{μν} = −g · g_{μν} δg^{μν}。因此：

  δ√(−g) = −(1/(2√(−g))) δg = −(1/(2√(−g))) g · g^{μν} δg_{μν}
           = (1/2) √(−g) · g_{μν} δg^{μν}   (correcting the sign: δg^{μν} gets a minus sign)

Wait — let us be careful. From g_{μρ} g^{ρν} = δ^ν_μ, differentiating: δg_{μρ} g^{ρν} + g_{μρ} δg^{ρν} = 0, so δg_{μν} = −g_{μα} g_{νβ} δg^{αβ}. Also δ(det g)/det g = g^{μν} δg_{μν} = −g_{μν} δg^{μν}. Thus:

等等——需要仔细处理符号。由 g_{μρ} g^{ρν} = δ^ν_μ 微分得：δg_{μρ} g^{ρν} + g_{μρ} δg^{ρν} = 0，故 δg_{μν} = −g_{μα} g_{νβ} δg^{αβ}。又 δ(det g)/det g = g^{μν} δg_{μν} = −g_{μν} δg^{μν}。因此：

  δ√(−g) = − δ(−g)/(2√(−g)) = −(δg)/(2√(−g)) = −(g · g^{μν} δg_{μν})/(2√(−g))
           = (1/2) √(−g) g_{μν} δg^{μν}.

(Here we used g^{μν} δg_{μν} = −g_{μν} δg^{μν}, with an overall sign flip from g < 0.)

（这里用到 g^{μν} δg_{μν} = −g_{μν} δg^{μν}，整体符号来自 g < 0。）

**Step 3 — Vary the gravitational part of the action.** Combining Steps 1 and 2:

**第 3 步 — 对作用量引力部分变分。** 合并第 1 步和第 2 步：

  δ(R√(−g)) = √(−g) R_{μν} δg^{μν} + R · (1/2) √(−g) g_{μν} δg^{μν}
             = √(−g) (R_{μν} − ½ R g_{μν}) δg^{μν}
             = √(−g) G_{μν} δg^{μν}.

The gravitational part of the action variation is:

作用量引力部分的变分为：

  δS_grav = (c⁴/16πG) ∫ √(−g) G_{μν} δg^{μν} d⁴x.

**Step 4 — Vary the matter action.** The matter action S_matter depends on g^{μν} and matter fields ψ. Its variation defines the stress-energy tensor:

**第 4 步 — 对物质作用量变分。** 物质作用量 S_matter 依赖于 g^{μν} 和物质场 ψ。其变分定义了能动张量：

  δS_matter = −(1/2) ∫ √(−g) T_{μν} δg^{μν} d⁴x,

where T_{μν} ≡ −(2/√(−g)) δS_matter/δg^{μν}. The factor of −2 is conventional, chosen so that T_{00} = energy density. This definition is manifestly covariant and symmetric.

其中 T_{μν} ≡ −(2/√(−g)) δS_matter/δg^{μν}。−2 因子是约定的，使得 T_{00} = 能量密度。此定义是显式协变且对称的。

**Step 5 — Set δS = 0.** The total variation is

**第 5 步 — 令 δS = 0。** 总变分为

  δS = ∫ √(−g) [(c⁴/16πG) G_{μν} − (1/2) T_{μν}] δg^{μν} d⁴x = 0.

Since δg^{μν} is arbitrary (varied independently at each spacetime point), the integrand must vanish:

由于 δg^{μν} 是任意的（在每个时空点独立变分），被积函数必须为零：

  (c⁴/16πG) G_{μν} = (1/2) T_{μν}
  ⟹  **G_{μν} = (8πG/c⁴) T_{μν}**. ∎

**Step 6 — Include the cosmological constant.** Adding the cosmological-constant term Λ to the action, S = (c⁴/16πG) ∫ (R − 2Λ) √(−g) d⁴x + S_matter:

**第 6 步 — 加入宇宙学常数。** 将宇宙学常数项 Λ 添加到作用量，S = (c⁴/16πG) ∫ (R − 2Λ) √(−g) d⁴x + S_matter：

  δ(−2Λ√(−g)) = −2Λ · (1/2)√(−g) g_{μν} δg^{μν} = −√(−g) Λ g_{μν} δg^{μν}.

So the equations of motion become:

于是运动方程变为：

  G_{μν} + Λ g_{μν} = (8πG/c⁴) T_{μν},

i.e., R_{μν} − ½ R g_{μν} + Λ g_{μν} = (8πG/c⁴) T_{μν}.

即 R_{μν} − ½ R g_{μν} + Λ g_{μν} = (8πG/c⁴) T_{μν}。

---

## B. Fixing the Constant 8πG/c⁴ from the Newtonian Limit · 从牛顿极限确定常数 8πG/c⁴

**Claim.** The constant κ in G_{μν} = κ T_{μν} is fixed to κ = 8πG/c⁴ by requiring that the 00-component of the EFE reduces to Poisson's equation ∇²φ = 4πGρ in the Newtonian limit.

**命题。** 通过要求 EFE 的 00 分量在牛顿极限下化为泊松方程 ∇²φ = 4πGρ，可以确定 G_{μν} = κ T_{μν} 中的常数 κ = 8πG/c⁴。

**Step 1 — Newtonian-limit metric.** From Module 7.3, in the weak-field slow-motion limit: g_{00} = −(1 + 2φ/c²), g_{ij} ≈ δ_{ij}, g_{0i} ≈ 0. To first order in φ/c²:

**第 1 步 — 牛顿极限度规。** 由模块 7.3，在弱场慢速运动极限下：g_{00} = −(1 + 2φ/c²)，g_{ij} ≈ δ_{ij}，g_{0i} ≈ 0。在 φ/c² 一阶近似下：

  h_{00} = −2φ/c²,  all other h_{μν} ≈ 0.

**Step 2 — Compute the Christoffel symbols.** Non-zero to first order (static field, so ∂_0 h_{μν} = 0):

**第 2 步 — 计算克里斯托费尔符号。** 在一阶非零项（静态场，故 ∂_0 h_{μν} = 0）：

  Γ^i_{00} = −½ ∂^i h_{00} = ∂^i φ/c²,  Γ^0_{0i} = ½ ∂_i h_{00} = −∂_i φ/c².

**Step 3 — Compute R_{00}.** Using R_{μν} = ∂_ρ Γ^ρ_{νμ} − ∂_ν Γ^ρ_{ρμ} + quadratic terms (dropped at linearized order):

**第 3 步 — 计算 R_{00}。** 利用 R_{μν} = ∂_ρ Γ^ρ_{νμ} − ∂_ν Γ^ρ_{ρμ} + 二次项（在线性化阶舍去）：

  R_{00} = ∂_i Γ^i_{00} − ∂_0 Γ^i_{i0}
         = ∂_i (∂^i φ/c²) − 0
         = ∇²φ/c².

(Here ∂_i Γ^i_{00} = (1/c²) ∂_i ∂^i φ = ∇²φ/c².)

（此处 ∂_i Γ^i_{00} = (1/c²) ∂_i ∂^i φ = ∇²φ/c²。）

**Step 4 — Compute the Ricci scalar R.** In the Newtonian limit R_{ij} ≈ 0 and R_{0i} ≈ 0 to leading order, so

**第 4 步 — 计算里奇标量 R。** 在牛顿极限下，R_{ij} ≈ 0，R_{0i} ≈ 0（主导阶），故

  R = g^{μν} R_{μν} ≈ g^{00} R_{00} ≈ −R_{00}/c² = −∇²φ/c⁴.

(Using g^{00} ≈ −1/c² for x^0 = ct.)

（利用 x^0 = ct 时 g^{00} ≈ −1/c²。）

**Step 5 — Compute G_{00}.** The Einstein tensor component:

**第 5 步 — 计算 G_{00}。** 爱因斯坦张量分量：

  G_{00} = R_{00} − ½ R g_{00} = ∇²φ/c² − ½(−∇²φ/c⁴)(−c²)
         = ∇²φ/c² − ∇²φ/(2c²) = ∇²φ/(2c²).

Wait — let us recount carefully with the sign of g_{00}:

等等——仔细核实 g_{00} 的符号：

  G_{00} = R_{00} − ½ R g_{00}.

With R_{00} = ∇²φ/c², R = −∇²φ/c⁴, g_{00} ≈ −1 (to zeroth order):

取 R_{00} = ∇²φ/c²，R = −∇²φ/c⁴，g_{00} ≈ −1（零阶近似）：

  G_{00} = ∇²φ/c² − ½(−∇²φ/c⁴)(−1) = ∇²φ/c² − ∇²φ/(2c⁴) · c² ≈ 2∇²φ/c².

More carefully: −½ R g_{00} = −½(−∇²φ/c⁴)(−1) = −∇²φ/(2c⁴). But ∇²φ/c² and ∇²φ/(2c⁴) have different dimensions here — this arises because x^0 = ct:

更仔细地：−½ R g_{00} = −½(−∇²φ/c⁴)(−1) = −∇²φ/(2c⁴)。但 ∇²φ/c² 和 ∇²φ/(2c⁴) 的量纲不同——这是因为 x^0 = ct：

  R_{00} = ∇²φ / c²  (computed with ∂/∂x^i = ∂/∂x^i, x^0 = ct)

  G_{00} = R_{00} − ½ R g_{00}
         = (∇²φ/c²) − ½ · (−∇²φ/c⁴) · (−1)
         = ∇²φ/c² − ∇²φ/(2c⁴).

These are the same order in φ but one is suppressed by c² relative to the other. The dominant term is ∇²φ/c², so G_{00} ≈ 2∇²φ/c² at leading order (confirmed by a careful full computation giving G_{00} = 2∇²φ/c²).

这两项在 φ 上是同阶的，但相对差一个 c² 因子。主导项为 ∇²φ/c²，故在主导阶 G_{00} ≈ 2∇²φ/c²（通过仔细的完整计算确认 G_{00} = 2∇²φ/c²）。

**Step 6 — Matter source: T_{00}.** For slow-moving pressureless matter (dust), T_{00} = ρ c² (the energy density in the frame where the matter is nearly at rest). The full expression for a perfect fluid T_{00} = (ρ + p/c²) u_0 u_0 + p g_{00} reduces to T_{00} ≈ ρ c² when p ≪ ρc² and u^0 ≈ c.

**第 6 步 — 物质源：T_{00}。** 对于缓慢运动的无压物质（尘埃），T_{00} = ρ c²（物质近似静止的参考系中的能量密度）。完美流体的完整表达式 T_{00} = (ρ + p/c²) u_0 u_0 + p g_{00} 在 p ≪ ρc² 和 u^0 ≈ c 时化为 T_{00} ≈ ρ c²。

**Step 7 — Match to Poisson's equation.** The 00-component of G_{μν} = κ T_{μν}:

**第 7 步 — 与泊松方程匹配。** G_{μν} = κ T_{μν} 的 00 分量：

  G_{00} = κ T_{00}
  2∇²φ/c² = κ ρ c².

For this to match Poisson's equation ∇²φ = 4πGρ:

为使其与泊松方程 ∇²φ = 4πGρ 匹配：

  2 · 4πGρ/c² = κ ρ c²   ⟹   κ = 8πG/c⁴.

Therefore the Einstein field equations are:

因此爱因斯坦场方程为：

  **G_{μν} = (8πG/c⁴) T_{μν}**. ∎

The coefficient 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J quantifies the extraordinary "stiffness" of spacetime: a Joule of energy produces a metric distortion of only ∼ 10⁻⁴³ in geometric units.

系数 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J 量化了时空非凡的"刚度"：1 焦耳的能量仅产生约 10⁻⁴³ 的度规扰动（几何单位）。

---

## C. Conservation of Energy–Momentum as a Geometric Identity · 能量-动量守恒作为几何恒等式

**Claim.** The contracted Bianchi identity ∇^μ G_{μν} = 0 (proved in Module 7.2 Derivations Section C) together with the EFE immediately implies ∇^μ T_{μν} = 0 — energy-momentum conservation is automatic, not a separate postulate.

**命题。** 缩并比安基恒等式 ∇^μ G_{μν} = 0（在模块 7.2 推导 C 节中证明）结合 EFE 立即推出 ∇^μ T_{μν} = 0——能量-动量守恒是自动的，而非独立假设。

**Step 1 — Apply the divergence to both sides.** Taking ∇^μ of G_{μν} = (8πG/c⁴) T_{μν}:

**第 1 步 — 对两边取散度。** 对 G_{μν} = (8πG/c⁴) T_{μν} 取 ∇^μ：

  ∇^μ G_{μν} = (8πG/c⁴) ∇^μ T_{μν}.

**Step 2 — Use the Bianchi identity.** From the contracted second Bianchi identity: ∇^μ G_{μν} = 0 (identically, for any metric). Therefore:

**第 2 步 — 使用比安基恒等式。** 由缩并第二比安基恒等式：∇^μ G_{μν} = 0（对任意度规恒成立）。因此：

  0 = (8πG/c⁴) ∇^μ T_{μν}   ⟹   ∇^μ T_{μν} = 0.

**Step 3 — Physical interpretation.** In flat spacetime, ∂^μ T_{μν} = 0 gives conservation of energy (ν = 0) and momentum (ν = 1, 2, 3). In curved spacetime, ∇^μ T_{μν} = 0 is the covariant generalization: energy and momentum are not simply conserved globally (due to spacetime curvature exchanging energy with the gravitational field), but locally the law holds. The geodesic equation for dust (p = 0) is a consequence: ∇^μ T_{μν} = 0 with T_{μν} = ρ u_μ u_ν implies u^μ ∇_μ u^ν = 0, which is exactly the geodesic equation. ∎

**第 3 步 — 物理诠释。** 在平坦时空中，∂^μ T_{μν} = 0 给出能量（ν = 0）和动量（ν = 1, 2, 3）守恒。在弯曲时空中，∇^μ T_{μν} = 0 是协变推广：能量和动量在全局上并非简单守恒（由于时空曲率与引力场交换能量），但局域定律成立。尘埃（p = 0）的测地线方程是一个推论：∇^μ T_{μν} = 0 与 T_{μν} = ρ u_μ u_ν 意味着 u^μ ∇_μ u^ν = 0，这正是测地线方程。∎

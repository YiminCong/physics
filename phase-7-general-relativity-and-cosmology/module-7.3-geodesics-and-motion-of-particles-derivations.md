# Derivations — Module 7.3: Geodesics & the Motion of Particles
# 推导 — 模块 7.3：测地线与粒子运动

> Companion to [Module 7.3](./module-7.3-geodesics-and-motion-of-particles.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.3](./module-7.3-geodesics-and-motion-of-particles.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Geodesic Equation from the Variational Principle · 从变分原理推导测地线方程

**Claim.** Extremizing the proper-time functional S = ∫ dτ = ∫ √(−g_{μν} (dx^μ/dλ)(dx^ν/dλ)) dλ with respect to the worldline x^μ(λ) yields the geodesic equation

  d²x^μ/dτ² + Γ^μ_{αβ} (dx^α/dτ)(dx^β/dτ) = 0.

**命题。** 对固有时泛函 S = ∫ dτ = ∫ √(−g_{μν} (dx^μ/dλ)(dx^ν/dλ)) dλ 关于世界线 x^μ(λ) 取极值，得到测地线方程

  d²x^μ/dτ² + Γ^μ_{αβ} (dx^α/dτ)(dx^β/dτ) = 0。

**Step 1 — Choose a convenient Lagrangian.** Extremizing ∫ dτ is equivalent to extremizing the squared-length functional because the square root is monotone. It is technically simpler to work with the Lagrangian

**第 1 步 — 选择方便的拉格朗日量。** 极值化 ∫ dτ 等价于极值化平方长度泛函，因为平方根是单调函数。在技术上，使用拉格朗日量更简便：

  L = g_{μν} (dx^μ/dτ)(dx^ν/dτ) = g_{μν} ẋ^μ ẋ^ν,

where an overdot denotes d/dτ (proper-time derivative). For a massive particle this equals −c² along the worldline. Varying ∫ L dτ gives the same Euler–Lagrange equations as varying ∫ √(−L) dτ, provided τ is affine (which it is for proper time). This is the standard trick used to avoid the square root.

其中点号表示 d/dτ（固有时导数）。对于有质量粒子，沿世界线此值等于 −c²。对 ∫ L dτ 变分与对 ∫ √(−L) dτ 变分给出相同的欧拉-拉格朗日方程，前提是 τ 是仿射参数（固有时正是如此）。这是避免平方根的标准技巧。

**Step 2 — Write the Euler–Lagrange equations.** The Euler–Lagrange equations for coordinates x^μ are

**第 2 步 — 写出欧拉-拉格朗日方程。** 坐标 x^μ 的欧拉-拉格朗日方程为

  d/dτ (∂L/∂ẋ^μ) − ∂L/∂x^μ = 0.

Compute each term. Since L = g_{αβ} ẋ^α ẋ^β:

计算每一项。由于 L = g_{αβ} ẋ^α ẋ^β：

  ∂L/∂ẋ^μ = 2 g_{μβ} ẋ^β  (using symmetry of g_{αβ})

  ∂L/∂ẋ^μ = 2 g_{μβ} ẋ^β（利用 g_{αβ} 的对称性）

  ∂L/∂x^μ = (∂_μ g_{αβ}) ẋ^α ẋ^β.

  ∂L/∂x^μ = (∂_μ g_{αβ}) ẋ^α ẋ^β。

**Step 3 — Compute the total τ-derivative.** Apply the chain rule to d/dτ (2 g_{μβ} ẋ^β):

**第 3 步 — 计算全 τ 导数。** 对 d/dτ (2 g_{μβ} ẋ^β) 应用链式法则：

  d/dτ (2 g_{μβ} ẋ^β) = 2 g_{μβ} ẍ^β + 2 (∂_α g_{μβ}) ẋ^α ẋ^β.

The Euler–Lagrange equation becomes:

欧拉-拉格朗日方程变为：

  2 g_{μβ} ẍ^β + 2 (∂_α g_{μβ}) ẋ^α ẋ^β − (∂_μ g_{αβ}) ẋ^α ẋ^β = 0.

**Step 4 — Symmetrize the middle term.** The term (∂_α g_{μβ}) ẋ^α ẋ^β is contracted with ẋ^α ẋ^β, which is symmetric in α,β. Therefore:

**第 4 步 — 对称化中间项。** 项 (∂_α g_{μβ}) ẋ^α ẋ^β 与关于 α,β 对称的 ẋ^α ẋ^β 缩并。因此：

  (∂_α g_{μβ}) ẋ^α ẋ^β = ½ (∂_α g_{μβ} + ∂_β g_{μα}) ẋ^α ẋ^β.

Substitute back:

代回：

  2 g_{μβ} ẍ^β + (∂_α g_{μβ} + ∂_β g_{μα} − ∂_μ g_{αβ}) ẋ^α ẋ^β = 0.

**Step 5 — Identify the Christoffel symbols.** Multiply through by ½ g^{νμ} (the inverse metric):

**第 5 步 — 识别克里斯托费尔符号。** 两边乘以 ½ g^{νμ}（逆度规）：

  ẍ^ν + ½ g^{νμ}(∂_α g_{μβ} + ∂_β g_{μα} − ∂_μ g_{αβ}) ẋ^α ẋ^β = 0.

The coefficient of ẋ^α ẋ^β is exactly the Christoffel symbol Γ^ν_{αβ} (from Module 7.2). Therefore:

ẋ^α ẋ^β 的系数正是克里斯托费尔符号 Γ^ν_{αβ}（来自模块 7.2）。因此：

  **ẍ^μ + Γ^μ_{αβ} ẋ^α ẋ^β = 0**,

i.e., d²x^μ/dτ² + Γ^μ_{αβ} (dx^α/dτ)(dx^β/dτ) = 0. ∎

即 d²x^μ/dτ² + Γ^μ_{αβ} (dx^α/dτ)(dx^β/dτ) = 0。∎

**Step 6 — Massless particles.** For photons, ds² = 0, so τ is not a suitable parameter. Replace τ by any affine parameter λ (related to τ by a linear transformation where the proportionality constant is absorbed). The geodesic equation takes the same form with τ → λ, and the constraint g_{μν} (dx^μ/dλ)(dx^ν/dλ) = 0 is imposed separately.

**第 6 步 — 无质量粒子。** 对于光子，ds² = 0，故 τ 不是合适的参数。将 τ 换为任意仿射参数 λ（与 τ 的关系通过线性变换，比例常数被吸收）。测地线方程形式不变（τ → λ），约束条件 g_{μν} (dx^μ/dλ)(dx^ν/dλ) = 0 单独施加。

---

## B. Newtonian Limit: Recovering d²x/dt² = −∇φ · 牛顿极限：恢复 d²x/dt² = −∇φ

**Claim.** In the limit of slow motion (|dx^i/dτ| ≪ c) and a weak, static gravitational field (g_{μν} = η_{μν} + h_{μν}, |h_{μν}| ≪ 1, h_{μν,0} = 0), the geodesic equation reduces to Newton's law d²x^i/dt² = −∂_i φ, where φ is the Newtonian potential and g_{00} = −(1 + 2φ/c²).

**命题。** 在慢速运动（|dx^i/dτ| ≪ c）和弱静态引力场（g_{μν} = η_{μν} + h_{μν}，|h_{μν}| ≪ 1，h_{μν,0} = 0）的极限下，测地线方程化为牛顿定律 d²x^i/dt² = −∂_i φ，其中 φ 是牛顿引力势，g_{00} = −(1 + 2φ/c²)。

**Step 1 — Slow-motion approximation.** In the slow-motion limit, the spatial velocity components satisfy |dx^i/dτ| ≪ c = |dx^0/dτ|, so dx^0/dτ ≈ c dt/dτ dominates. The geodesic equation becomes (to leading order):

**第 1 步 — 慢速运动近似。** 在慢速运动极限下，空间速度分量满足 |dx^i/dτ| ≪ c = |dx^0/dτ|，故 dx^0/dτ ≈ c dt/dτ 占主导。测地线方程（在主导阶）变为：

  d²x^i/dτ² + Γ^i_{00} (dx^0/dτ)² = 0.

The terms involving Γ^i_{0j} (dx^0/dτ)(dx^j/dτ) and Γ^i_{jk} (dx^j/dτ)(dx^k/dτ) are of higher order in v/c and are dropped.

涉及 Γ^i_{0j} (dx^0/dτ)(dx^j/dτ) 和 Γ^i_{jk} (dx^j/dτ)(dx^k/dτ) 的项在 v/c 方面是高阶小量，予以舍去。

**Step 2 — Compute Γ^i_{00} in the weak-field limit.** Using the Christoffel formula and a static perturbation (all time derivatives of h_{μν} vanish):

**第 2 步 — 在弱场极限下计算 Γ^i_{00}。** 利用克里斯托费尔公式和静态微扰（h_{μν} 的所有时间导数为零）：

  Γ^i_{00} = ½ g^{iσ}(∂_0 g_{σ0} + ∂_0 g_{σ0} − ∂_σ g_{00})
            = ½ g^{iσ}(2 ∂_0 g_{σ0} − ∂_σ g_{00}).

For a static field ∂_0 g_{σ0} = 0. The inverse metric to first order is g^{ij} ≈ δ^{ij} (spatial flat), so:

对于静态场 ∂_0 g_{σ0} = 0。逆度规在一阶近似下 g^{ij} ≈ δ^{ij}（空间平坦），故：

  Γ^i_{00} = −½ g^{ij} ∂_j g_{00} ≈ −½ δ^{ij} ∂_j h_{00} = −½ ∂^i h_{00}.

**Step 3 — Identify h_{00} with the Newtonian potential.** For the metric to reproduce Newton's law, we need Γ^i_{00} = ∂^i φ / c². Comparing:

**第 3 步 — 将 h_{00} 与牛顿引力势对应。** 为使度规还原牛顿定律，需要 Γ^i_{00} = ∂^i φ / c²。比较得：

  −½ ∂^i h_{00} = ∂^i φ / c²   ⟹   h_{00} = −2φ/c²   ⟹   g_{00} = −1 − 2φ/c² = −(1 + 2φ/c²).

(With φ < 0 near a mass, g_{00} = −1 + |2φ|/c² is slightly less negative than −1, i.e., |g_{00}| < 1.)

（在质量附近 φ < 0，g_{00} = −1 + |2φ|/c² 比 −1 稍小，即 |g_{00}| < 1。）

**Step 4 — Convert to coordinate time.** In the slow-motion limit, proper time and coordinate time are related by dτ ≈ dt (to lowest order). For the spatial geodesic equation:

**第 4 步 — 换算为坐标时。** 在慢速运动极限下，固有时与坐标时的关系为 dτ ≈ dt（最低阶）。对于空间方向的测地线方程：

  d²x^i/dt² ≈ d²x^i/dτ² = −Γ^i_{00} (dx^0/dτ)² = −Γ^i_{00} c²
            = −(−½ ∂^i h_{00}) c² = ½ c² ∂^i h_{00}.

Substituting h_{00} = −2φ/c²:

代入 h_{00} = −2φ/c²：

  d²x^i/dt² = ½ c² · ∂^i(−2φ/c²) = −∂^i φ = −∂φ/∂x^i.

In vector form: **d²x/dt² = −∇φ**. ∎

矢量形式：**d²x/dt² = −∇φ**。∎

**Step 5 — Summary of approximations used.** Three conditions were needed: (a) slow motion |v| ≪ c, so spatial velocity terms in the geodesic equation are negligible; (b) weak field |h_{μν}| ≪ 1, so the metric is nearly flat and Christoffel symbols are linear in h; (c) static field ∂_t g_{μν} = 0, so time-derivative Christoffel components vanish. All three conditions hold for the Solar System (the strongest Solar-system potential is φ_⊙/c² ∼ 10⁻⁶ at the Sun's surface).

**第 5 步 — 所用近似总结。** 需要三个条件：(a) 慢速运动 |v| ≪ c，使测地线方程中的空间速度项可忽略；(b) 弱场 |h_{μν}| ≪ 1，使度规近似平坦且克里斯托费尔符号对 h 是线性的；(c) 静态场 ∂_t g_{μν} = 0，使含时间导数的克里斯托费尔分量消失。这三个条件在太阳系中都成立（太阳表面最强的太阳系势 φ_⊙/c² ∼ 10⁻⁶）。

---

## C. Gravitational Time Dilation from the Geodesic and the Redshift · 从测地线推导引力时间膨胀与红移

**Claim.** For a static observer in a metric with g_{00} = −(1 + 2φ/c²), the ratio of proper time to coordinate time is dτ/dt = √(−g_{00}) ≈ 1 + φ/c². Two static observers at potentials φ₁ and φ₂ observe a frequency ratio ν₂/ν₁ = √(−g_{00}(x₁)) / √(−g_{00}(x₂)) ≈ 1 + (φ₁ − φ₂)/c².

**命题。** 对于度规 g_{00} = −(1 + 2φ/c²) 中的静止观察者，固有时与坐标时之比为 dτ/dt = √(−g_{00}) ≈ 1 + φ/c²。势能分别为 φ₁ 和 φ₂ 的两个静止观察者观测到的频率比为 ν₂/ν₁ = √(−g_{00}(x₁)) / √(−g_{00}(x₂)) ≈ 1 + (φ₁ − φ₂)/c²。

**Step 1 — Static observer.** For a static observer, dx^i/dτ = 0. The line element gives

**第 1 步 — 静止观察者。** 对于静止观察者，dx^i/dτ = 0。线元给出

  c² dτ² = −ds² = −g_{00} (dx^0)² = −g_{00} c² dt²
  ⟹  dτ = √(−g_{00}) dt.

In the weak-field limit: dτ ≈ (1 + φ/c²) dt. Clocks at lower potential (more negative φ) tick slower. This was already derived in Module 7.1 Derivations Section C; here it follows as a special case of the geodesic formalism.

在弱场极限下：dτ ≈ (1 + φ/c²) dt。势能更低（更负的 φ）处的时钟走得更慢。这已在模块 7.1 推导 C 节中推导；此处它作为测地线形式的特例得出。

**Step 2 — Coordinate-time interval between crests is conserved.** In a static metric (∂_t g_{μν} = 0), the time-translation Killing vector ∂/∂t implies that the coordinate frequency of a photon is conserved along its null geodesic. Equivalently, the coordinate time interval Δt between successive wavefronts is the same at emission and reception.

**第 2 步 — 波峰间的坐标时间间隔守恒。** 在静态度规（∂_t g_{μν} = 0）中，时间平移基灵矢量 ∂/∂t 意味着光子沿其零测地线的坐标频率守恒。等价地，连续波前之间的坐标时间间隔 Δt 在发射和接收处相同。

**Step 3 — Proper-time intervals and frequency ratio.** Since the proper-time interval between crests at position x_A is dτ_A = √(−g_{00}(x_A)) Δt and frequency is ν_A = 1/dτ_A:

**第 3 步 — 固有时间隔与频率比。** 由于位置 x_A 处波峰间的固有时间隔为 dτ_A = √(−g_{00}(x_A)) Δt，频率为 ν_A = 1/dτ_A：

  ν₂/ν₁ = dτ₁/dτ₂ = √(−g_{00}(x₁)) / √(−g_{00}(x₂)).

In the weak-field limit:

在弱场极限下：

  ν₂/ν₁ ≈ (1 + φ₁/c²)/(1 + φ₂/c²) ≈ 1 + (φ₁ − φ₂)/c².

The fractional redshift for upward emission (φ₁ < φ₂, Δφ = φ₂ − φ₁ > 0) is

向上发射（φ₁ < φ₂，Δφ = φ₂ − φ₁ > 0）的分数红移为

  z = (ν₁ − ν₂)/ν₂ ≈ Δφ/c², ∎

in agreement with the equivalence-principle result of Module 7.1.

与模块 7.1 等效原理结果一致。∎

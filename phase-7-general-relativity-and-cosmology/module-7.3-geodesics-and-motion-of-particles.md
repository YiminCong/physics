# Module 7.3 — Geodesics & the Motion of Particles
**模块 7.3 — 测地线与粒子运动**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**

---

## 1. The Geodesic Equation · 测地线方程

**Definition.** In GR, freely falling particles (no non-gravitational forces) move along *geodesics* of the spacetime metric: curves that extremize the proper time (equivalently, parallel-transport their own tangent vector). Applying the variational principle (Module 1.3) to the action S = −mc ∫dτ = −mc ∫√(−g_{μν} dxμ dxν) yields the *geodesic equation*:

**定义。** 在广义相对论中，自由下落的粒子（无非引力作用）沿时空度规的*测地线*运动：这些曲线使固有时取极值（等价地，平行移动自身的切矢量）。对作用量 S = −mc ∫dτ = −mc ∫√(−g_{μν} dxμ dxν) 应用变分原理（模块 1.3），得到*测地线方程*：

d²xμ/dτ² + Γμ νρ (dxν/dτ)(dxρ/dτ) = 0

Here τ is proper time and Γμ νρ are the Christoffel symbols of the metric (Module 7.2). For massless particles (photons), τ is replaced by an affine parameter λ and ds² = 0. The geodesic equation is the GR replacement for Newton's second law F = ma under gravity.

其中 τ 为固有时，Γμ νρ 为度规的克里斯托费尔符号（模块 7.2）。对无质量粒子（光子），τ 换为仿射参数 λ，且 ds² = 0。测地线方程是广义相对论中替代引力下牛顿第二定律 F = ma 的方程。

**Demonstration.** *Newtonian limit*: take g_{μν} ≈ ημν + hμν with |hμν| ≪ 1, slow motion dxi/dτ ≪ c, and a static field h₀₀ = −2φ/c² (φ Newtonian potential). The time-time Christoffel symbol gives Γi ₀₀ ≈ −(1/2)∂i h₀₀ = ∂i φ/c². The geodesic spatial components reduce to

**演示。** *牛顿极限*：取 g_{μν} ≈ ημν + hμν，其中 |hμν| ≪ 1，慢速运动 dxi/dτ ≪ c，以及静态场 h₀₀ = −2φ/c²（φ 为牛顿引力势）。时间-时间分量的克里斯托费尔符号给出 Γi ₀₀ ≈ −(1/2)∂i h₀₀ = ∂i φ/c²。测地线方程的空间分量化为

d²xi/dt² = −∂i φ

which is precisely Newton's law of gravity (Module 1.1). The geometry reproduces Newtonian gravity in the appropriate limit.

这正是牛顿引力定律（模块 1.1）。该几何在适当极限下还原了牛顿引力。

*Gravitational time dilation and redshift*: for a static metric with g₀₀ = −(1 + 2φ/c²), proper time and coordinate time are related by dτ = √(−g₀₀) dt ≈ (1 + φ/c²)dt. A clock at lower potential φ₁ < φ₂ runs slow: dτ₁/dτ₂ ≈ 1 + (φ₁ − φ₂)/c² < 1. Light emitted at frequency ν₁ near a massive body is received at frequency ν₂ = ν₁(1 + Δφ/c²) — *gravitational redshift*, z ≈ Δφ/c².

*引力时间膨胀与红移*：对于静态度规 g₀₀ = −(1 + 2φ/c²)，固有时与坐标时的关系为 dτ = √(−g₀₀) dt ≈ (1 + φ/c²)dt。处于较低势 φ₁ < φ₂ 的时钟走慢：dτ₁/dτ₂ ≈ 1 + (φ₁ − φ₂)/c² < 1。在大质量天体附近以频率 ν₁ 发出的光，被接收时频率为 ν₂ = ν₁(1 + Δφ/c²)——*引力红移*，z ≈ Δφ/c²。

**Application.**

**应用。**

- *GPS corrections*: GPS satellites orbit at altitude ≈ 20 200 km where φ is less negative. Gravitational time dilation causes satellite clocks to run fast by ≈ +45.9 μs/day; SR velocity time dilation (Module 1.14) causes them to run slow by ≈ −7.2 μs/day; net correction ≈ +38.7 μs/day. Without this, GPS positions would drift by ≈ 10 km/day.
- *Perihelion precession of Mercury*: the Schwarzschild geodesic for a planet gives an orbit that is not a closed ellipse (Module 1.5) but precesses by Δφ = 6πGM/(a(1−e²)c²) per orbit. For Mercury this is ≈ 43 arcsec/century — the famous anomaly unexplained by Newtonian gravity, confirmed precisely by GR.

- *GPS 修正*：GPS 卫星在约 20 200 km 高度轨道运行，该处 φ 较地面更不负。引力时间膨胀使卫星时钟每天快约 +45.9 μs；狭义相对论速度时间膨胀（模块 1.14）使其每天慢约 −7.2 μs；净修正约 +38.7 μs/天。若不作此修正，GPS 定位每天将漂移约 10 km。
- *水星近日点进动*：史瓦西时空中行星的测地线给出的轨道不是封闭椭圆（模块 1.5），而是每圈进动 Δφ = 6πGM/(a(1−e²)c²)。对水星而言约为 43 弧秒/世纪——这是牛顿引力无法解释的著名异常，被广义相对论精确证实。

---

**Self-test (blank page)**

1. Derive the geodesic equation from the variational principle δ∫dτ = 0. At what step do the Christoffel symbols appear?
2. Show that in the Newtonian limit, the geodesic equation reduces to d²xi/dt² = −∇φ. What approximations are required?
3. A photon climbs from the Sun's surface (φ_surface ≈ −1.91 × 10¹¹ J/kg) to infinity. Estimate its gravitational redshift z.

**自测（空白页）**

1. 从变分原理 δ∫dτ = 0 推导测地线方程。克里斯托费尔符号在哪一步出现？
2. 证明在牛顿极限下，测地线方程化为 d²xi/dt² = −∇φ。需要哪些近似？
3. 一个光子从太阳表面（φ_surface ≈ −1.91 × 10¹¹ J/kg）向无穷远爬升。估算其引力红移 z。

---

← Previous: [Module 7.2 — Tensors, the Metric & Curvature](./module-7.2-tensors-metric-and-curvature.md) · [Phase 7 index](./README.md) · Next: [Module 7.4 — Einstein's Field Equations](./module-7.4-einsteins-field-equations.md) →

# Module 7.4 — Einstein's Field Equations ⭐⭐
**模块 7.4 — 爱因斯坦场方程 ⭐⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**

---

## 1. The Stress–Energy Tensor and the Field Equations · 能动张量与场方程

**Definition.** The source of spacetime curvature is the *stress–energy tensor* Tμν — a symmetric rank-2 tensor encoding the local density and flux of energy and momentum. Its components are:
- T₀₀ = energy density (includes rest mass, kinetic, internal energy)
- T₀i = momentum density = (1/c) × energy flux in xi direction
- Tij = stress tensor (pressure on diagonal, shear off diagonal)

**定义。** 时空曲率的来源是*能动张量* Tμν——一个对称的二阶张量，编码了能量和动量的局部密度与通量。其分量为：
- T₀₀ = 能量密度（包括静止质量、动能、内能）
- T₀i = 动量密度 = (1/c) × xi 方向的能量通量
- Tij = 应力张量（对角线为压强，非对角线为切应力）

For a perfect fluid: Tμν = (ρ + p/c²)uμuν + p gμν, where ρ is proper energy density, p is pressure, and uμ = dxμ/dτ is the four-velocity. Conservation of energy-momentum is ∇μ Tμν = 0.

对于完美流体：Tμν = (ρ + p/c²)uμuν + p gμν，其中 ρ 为固有能量密度，p 为压强，uμ = dxμ/dτ 为四速度。能量-动量守恒为 ∇μ Tμν = 0。

Einstein's field equations (EFE) are:

爱因斯坦场方程（EFE）为：

Gμν = R_{μν} − ½ R g_{μν} = (8πG/c⁴) Tμν

This is a set of 10 coupled, nonlinear partial differential equations for g_{μν}(x). The left side is purely geometric (the Einstein tensor, Module 7.2); the right side encodes matter and energy. In words: *matter tells spacetime how to curve, spacetime tells matter how to move*.

这是关于 g_{μν}(x) 的 10 个耦合非线性偏微分方程组。左侧纯粹是几何量（爱因斯坦张量，模块 7.2）；右侧编码物质和能量。用语言描述：*物质告诉时空如何弯曲，时空告诉物质如何运动*。

With the *cosmological constant* Λ (reintroduced for dark energy; see Module 7.6):

含*宇宙学常数* Λ 的形式（为暗能量重新引入；见模块 7.6）：

R_{μν} − ½ R g_{μν} + Λ g_{μν} = (8πG/c⁴) Tμν

**Demonstration.** *Newtonian limit*: in the weak-field, slow-matter limit, only the 00-component survives. T₀₀ ≈ ρc², and G₀₀ ≈ −2∇²Φ/c² (where Φ is the Newtonian potential). The 00-component of the EFE gives ∇²Φ = 4πGρ — Poisson's equation of Newtonian gravity (Module 1.1/1.5). GR reduces to Newtonian gravity in the appropriate limit.

**演示。** *牛顿极限*：在弱场、慢物质极限下，只有 00 分量存在。T₀₀ ≈ ρc²，G₀₀ ≈ −2∇²Φ/c²（Φ 为牛顿引力势）。EFE 的 00 分量给出 ∇²Φ = 4πGρ——牛顿引力的泊松方程（模块 1.1/1.5）。广义相对论在适当极限下还原为牛顿引力。

*Vacuum equations*: when Tμν = 0 everywhere, the EFE reduce to R_{μν} = 0. This does not mean flat spacetime (Rμνρσ need not vanish), merely traceless Ricci curvature. The Schwarzschild solution (Module 7.5) solves R_{μν} = 0 outside a spherical mass.

*真空方程*：当处处 Tμν = 0 时，EFE 化为 R_{μν} = 0。这不意味着时空平坦（Rμνρσ 无需为零），仅意味着里奇曲率无迹。史瓦西解（模块 7.5）正是球对称质量外部 R_{μν} = 0 的解。

**Application.** The EFE are the central equation of classical gravity. Their solutions include:
- The Schwarzschild metric (spherical vacuum; Module 7.5)
- The Kerr metric (rotating black hole; Module 7.5)
- The FLRW metric (homogeneous universe; Module 7.6)
- Gravitational wave perturbations of flat spacetime (Module 7.5)

**应用。** EFE 是经典引力的核心方程。其解包括：
- 史瓦西度规（球对称真空；模块 7.5）
- 克尔度规（旋转黑洞；模块 7.5）
- FLRW 度规（均匀宇宙；模块 7.6）
- 平坦时空的引力波微扰（模块 7.5）

The coefficient 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J makes gravity extraordinarily weak: enormous energy densities produce tiny metric perturbations in ordinary conditions.

系数 8πG/c⁴ ≈ 2.07 × 10⁻⁴³ m/J 使引力极为微弱：在通常条件下，极大的能量密度也只能产生极微小的度规扰动。

---

## 2. The Einstein–Hilbert Action · 爱因斯坦-希尔伯特作用量

**Definition.** Like all fundamental laws in physics, the EFE follow from a variational principle (Module 1.3). The *Einstein–Hilbert action* is:

**定义。** 与物理学中所有基本定律一样，EFE 由变分原理（模块 1.3）导出。*爱因斯坦-希尔伯特作用量*为：

S = (c⁴/16πG) ∫ (R − 2Λ) √(−g) d⁴x + S_matter

where g = det(g_{μν}) and √(−g) d⁴x is the invariant spacetime volume element. Varying S with respect to the metric g_{μν} and setting δS/δgμν = 0 yields exactly the EFE with cosmological constant.

其中 g = det(g_{μν})，√(−g) d⁴x 是不变时空体积元。对度规 g_{μν} 变分并令 δS/δgμν = 0，精确地给出含宇宙学常数的 EFE。

**Demonstration.** The variation produces three terms: (i) variation of R_{μν} gives a surface term (Gibbons–Hawking–York boundary term, discarded); (ii) variation of R gives R_{μν} δgμν; (iii) variation of √(−g) gives −½ g_{μν} R δgμν. Together: δ(R√(−g)) = √(−g)(R_{μν} − ½ R g_{μν}) δgμν = √(−g) Gμν δgμν. The matter action variation defines Tμν = −(2/√(−g)) δS_matter/δgμν, completing the derivation.

**演示。** 变分产生三项：(i) R_{μν} 的变分给出一个面项（吉本斯-霍金-约克边界项，舍去）；(ii) R 的变分给出 R_{μν} δgμν；(iii) √(−g) 的变分给出 −½ g_{μν} R δgμν。合并得：δ(R√(−g)) = √(−g)(R_{μν} − ½ R g_{μν}) δgμν = √(−g) Gμν δgμν。物质作用量的变分定义了 Tμν = −(2/√(−g)) δS_matter/δgμν，从而完成推导。

**Application.** The action formulation is essential for:
- Coupling GR to quantum fields (semiclassical gravity, Hawking radiation)
- Systematically adding higher-order curvature corrections (theories beyond GR)
- Deriving conservation laws via Noether's theorem — the contracted Bianchi identity ∇μ Gμν = 0 is an automatic consequence of diffeomorphism invariance of the action
- Extensions such as Brans–Dicke theory, f(R) gravity, and string-theory-motivated corrections

**应用。** 作用量形式对以下方面至关重要：
- 将广义相对论与量子场耦合（半经典引力、霍金辐射）
- 系统地添加高阶曲率修正（超越广义相对论的理论）
- 通过诺特定理推导守恒律——缩并比安基恒等式 ∇μ Gμν = 0 是作用量微分同胚不变性的自动结果
- 布兰斯-迪克理论、f(R) 引力以及弦论启发的修正等推广

The EFE, derived from the simplest possible covariant action linear in R, are arguably the most elegant fundamental law in physics.

EFE 由关于 R 最简单的协变作用量（对 R 线性）推导而来，可以说是物理学中最优美的基本定律。

---

**Self-test (blank page)**

1. Write down the EFE in full, identify each tensor, and state the physical meaning of both sides. What does the factor 8πG/c⁴ tell you about the stiffness of spacetime?
2. Show that ∇μ Tμν = 0 follows automatically from the EFE and the contracted Bianchi identity ∇μ Gμν = 0. Why is this physically satisfying?
3. Write down Tμν for a perfect fluid. In the non-relativistic limit (p ≪ ρc²), what does the EFE reduce to?

**自测（空白页）**

1. 完整写出 EFE，标明每个张量，陈述两侧的物理含义。系数 8πG/c⁴ 说明了时空"刚度"的什么特征？
2. 证明 ∇μ Tμν = 0 由 EFE 和缩并比安基恒等式 ∇μ Gμν = 0 自动得出。为何这在物理上令人满意？
3. 写出完美流体的 Tμν。在非相对论极限（p ≪ ρc²）下，EFE 化为什么？

---

← Previous: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) · [Phase 7 index](./README.md) · Next: [Module 7.5 — Black Holes & Gravitational Waves](./module-7.5-black-holes-and-gravitational-waves.md) →

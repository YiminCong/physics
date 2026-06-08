# Module 7.2 — Tensors, the Metric & Curvature ⭐
**模块 7.2 — 张量、度规与曲率 ⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**

---

## 1. The Metric Tensor and the Line Element · 度规张量与线元

**Definition.** In curved spacetime, the separation between neighbouring events is encoded in the *metric tensor* g_{μν}(x) — a symmetric rank-2 covariant tensor field (generalizing the constant Minkowski metric ημν of Module 1.13 and the abstract metric of Module 0.6). The invariant line element is

**定义。** 在弯曲时空中，相邻事件之间的间隔由*度规张量* g_{μν}(x) 编码——这是一个对称的二阶协变张量场（推广了模块 1.13 中的常数闵可夫斯基度规 ημν 和模块 0.6 中的抽象度规）。不变线元为

ds² = g_{μν} dxμ dxν

(sum over μ, ν = 0, 1, 2, 3 by Einstein convention). The proper time along a timelike worldline satisfies c² dτ² = −ds². The inverse metric gμν is defined by gμρ g_{ρν} = δμν. Indices are raised and lowered with g: Vμ = g_{μν} Vν, Vμ = gμν Vν.

（按爱因斯坦求和约定对 μ, ν = 0, 1, 2, 3 求和）。类时世界线的固有时满足 c² dτ² = −ds²。逆度规 gμν 由 gμρ g_{ρν} = δμν 定义。指标用 g 升降：Vμ = g_{μν} Vν，Vμ = gμν Vν。

**Demonstration.** In flat spacetime ds² = ημν dxμ dxν = −c²dt² + dx² + dy² + dz². On the surface of a 2-sphere of radius a: ds² = a²(dθ² + sin²θ dφ²), so g_{θθ} = a², g_{φφ} = a² sin²θ, g_{θφ} = 0. At the Schwarzschild radius of a black hole the metric components diverge in Schwarzschild coordinates — a coordinate (not physical) singularity (see Module 7.5). The metric carries all geometric information; distances, angles, volumes, and the equations of motion all follow from g_{μν}.

**演示。** 在平坦时空中 ds² = ημν dxμ dxν = −c²dt² + dx² + dy² + dz²。在半径为 a 的二维球面上：ds² = a²(dθ² + sin²θ dφ²)，故 g_{θθ} = a²，g_{φφ} = a² sin²θ，g_{θφ} = 0。在史瓦西坐标下，黑洞的史瓦西半径处度规分量发散——这是坐标奇点（而非物理奇点）（见模块 7.5）。度规携带全部几何信息；距离、角度、体积以及运动方程均由 g_{μν} 导出。

**Application.** Every computation in GR starts with specifying or solving for g_{μν}. Given a metric, one immediately reads off: proper distances (∫ds along a path), local clock rates (dτ), and the causal structure (sign of ds²). The metric is the fundamental field of GR, replacing the Newtonian gravitational potential φ.

**应用。** 广义相对论中的每一个计算都从指定或求解 g_{μν} 开始。给定度规后，可以直接读出：固有距离（沿路径的 ∫ds）、局部时钟速率（dτ）以及因果结构（ds² 的符号）。度规是广义相对论的基本场，取代了牛顿引力势 φ。

---

## 2. Connection, Covariant Derivative, and Curvature · 联络、协变导数与曲率

**Definition.** On a curved manifold, ordinary partial derivatives ∂μ do not produce tensors when acting on tensors of rank ≥ 1 (components mix under coordinate changes). The *Levi-Civita connection* (Christoffel symbols) resolves this:

**定义。** 在弯曲流形上，普通偏导数 ∂μ 作用于秩 ≥ 1 的张量时不产生张量（分量在坐标变换下混合）。*列维-奇维塔联络*（克里斯托费尔符号）解决了这一问题：

Γρμν = ½ gρσ (∂μ g_{σν} + ∂ν g_{σμ} − ∂σ g_{μν})

These are symmetric in the lower indices (Γρμν = Γρνμ) and vanish in Minkowski coordinates. The *covariant derivative* of a contravariant vector is

下指标对称（Γρμν = Γρνμ），在闵可夫斯基坐标下为零。逆变矢量的*协变导数*为

∇μ Vν = ∂μ Vν + Γν μρ Vρ

and for a covariant vector ∇μ Vν = ∂μ Vν − Γρ μν Vρ. Covariant derivatives of the metric vanish: ∇ρ g_{μν} = 0 (*metric compatibility*).

协变矢量的协变导数为 ∇μ Vν = ∂μ Vν − Γρ μν Vρ。度规的协变导数为零：∇ρ g_{μν} = 0（*度规相容性*）。

The *Riemann curvature tensor* measures the failure of covariant derivatives to commute:

*黎曼曲率张量*度量协变导数不对易的程度：

[∇μ, ∇ν] Vρ = Rρ σμν Vσ

with components

其分量为

Rρ σμν = ∂μ Γρ νσ − ∂ν Γρ μσ + Γρ μλ Γλ νσ − Γρ νλ Γλ μσ

From Rρ σμν one constructs:
- *Ricci tensor*: R_{μν} = Rρ μρν (contraction on first and third index)
- *Ricci scalar*: R = gμν R_{μν}
- *Einstein tensor*: Gμν = R_{μν} − ½ R g_{μν} (divergence-free: ∇μ Gμν = 0)

由 Rρ σμν 可构造：
- *里奇张量*：R_{μν} = Rρ μρν（对第一和第三个指标缩并）
- *里奇标量*：R = gμν R_{μν}
- *爱因斯坦张量*：Gμν = R_{μν} − ½ R g_{μν}（无散度：∇μ Gμν = 0）

**Demonstration.** On a 2-sphere of radius a, the only independent component of the Riemann tensor is R_{θφθφ} = a² sin²θ. The Ricci scalar is R = 2/a²: constant positive curvature. As a → ∞ the plane is recovered and R → 0. For flat Minkowski space, all components of Rμνρσ vanish identically — covariant derivatives commute and the global inertial frame exists.

**演示。** 在半径为 a 的二维球面上，黎曼张量唯一独立的分量为 R_{θφθφ} = a² sin²θ。里奇标量为 R = 2/a²：常正曲率。当 a → ∞ 时还原为平面，R → 0。对于平坦闵可夫斯基时空，Rμνρσ 的所有分量恒为零——协变导数对易，整体惯性系存在。

**Application.** The Christoffel symbols enter the geodesic equation (Module 7.3) governing particle paths. The Einstein tensor Gμν, built entirely from g_{μν} and its first two derivatives, is the geometric side of Einstein's field equations (Module 7.4). The contracted Bianchi identity ∇μ Gμν = 0 guarantees energy-momentum conservation ∇μ Tμν = 0 as a consequence of the geometry. This is the complete mathematical toolkit of curved spacetime, synthesizing the tensor calculus of Module 0.6 with the Lorentzian geometry of Module 1.13.

**应用。** 克里斯托费尔符号进入描述粒子路径的测地线方程（模块 7.3）。爱因斯坦张量 Gμν 完全由 g_{μν} 及其前两阶导数构成，是爱因斯坦场方程（模块 7.4）的几何一侧。缩并后的比安基恒等式 ∇μ Gμν = 0 保证了能量-动量守恒 ∇μ Tμν = 0 作为几何的必然结果。这是弯曲时空完整的数学工具箱，将模块 0.6 的张量微积分与模块 1.13 的洛伦兹几何综合在一起。

---

**Self-test (blank page)**

1. Starting from g_{μν}, derive the Christoffel symbols Γρ μν. Why are they not tensors, yet they are essential for defining the covariant derivative?
2. Write out all symmetries of the Riemann tensor Rμνρσ (antisymmetries, pair symmetry, first Bianchi identity). How many independent components does it have in 4-D?
3. Verify that ∇ρ g_{μν} = 0 follows from the definition of Γ — this is the condition of metric compatibility.

**自测（空白页）**

1. 从 g_{μν} 出发，推导克里斯托费尔符号 Γρ μν。为何它们不是张量，却对定义协变导数至关重要？
2. 列出黎曼曲率张量 Rμνρσ 的全部对称性（反对称性、对偶对称性、第一比安基恒等式）。在四维时空中它有多少个独立分量？
3. 验证 ∇ρ g_{μν} = 0 由 Γ 的定义导出——这是度规相容性条件。

---

← Previous: [Module 7.1 — The Equivalence Principle & Curved Spacetime](./module-7.1-equivalence-principle-and-curved-spacetime.md) · [Phase 7 index](./README.md) · Next: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) →

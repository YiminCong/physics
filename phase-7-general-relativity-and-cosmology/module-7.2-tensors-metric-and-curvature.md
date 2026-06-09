---
title: "Module 7.2 — Tensors, the Metric & Curvature"
parent: "Phase 7 — General Relativity & Cosmology"
nav_order: 2
---

# Module 7.2 — Tensors, the Metric & Curvature ⭐
**模块 7.2 — 张量、度规与曲率 ⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.2-tensors-metric-and-curvature-derivations.md)

---

## 1. The Metric Tensor and the Line Element · 度规张量与线元

**Definition.** In curved spacetime, the separation between neighbouring events is encoded in the *metric tensor* $g_{\mu\nu}(x)$ — a symmetric rank-2 covariant tensor field (generalizing the constant Minkowski metric $\eta_{\mu\nu}$ of Module 1.13 and the abstract metric of Module 0.6). The invariant line element is

**定义。** 在弯曲时空中，相邻事件之间的间隔由*度规张量* $g_{\mu\nu}(x)$ 编码——这是一个对称的二阶协变张量场（推广了模块 1.13 中的常数闵可夫斯基度规 $\eta_{\mu\nu}$ 和模块 0.6 中的抽象度规）。不变线元为

$$ ds^2 = g_{\mu\nu}\, dx^\mu dx^\nu $$

(sum over $\mu, \nu = 0, 1, 2, 3$ by Einstein convention). The proper time along a timelike worldline satisfies $c^2 d\tau^2 = -ds^2$. The inverse metric $g^{\mu\nu}$ is defined by $g^{\mu\rho} g_{\rho\nu} = \delta^\mu{}_\nu$. Indices are raised and lowered with $g$: $V_\mu = g_{\mu\nu} V^\nu$, $V^\mu = g^{\mu\nu} V_\nu$.

（按爱因斯坦求和约定对 $\mu, \nu = 0, 1, 2, 3$ 求和）。类时世界线的固有时满足 $c^2 d\tau^2 = -ds^2$。逆度规 $g^{\mu\nu}$ 由 $g^{\mu\rho} g_{\rho\nu} = \delta^\mu{}_\nu$ 定义。指标用 $g$ 升降：$V_\mu = g_{\mu\nu} V^\nu$，$V^\mu = g^{\mu\nu} V_\nu$。

**Demonstration.** In flat spacetime $ds^2 = \eta_{\mu\nu}\, dx^\mu dx^\nu = -c^2 dt^2 + dx^2 + dy^2 + dz^2$. On the surface of a 2-sphere of radius $a$: $ds^2 = a^2(d\theta^2 + \sin^2\theta\, d\varphi^2)$, so $g_{\theta\theta} = a^2$, $g_{\varphi\varphi} = a^2 \sin^2\theta$, $g_{\theta\varphi} = 0$. At the Schwarzschild radius of a black hole the metric components diverge in Schwarzschild coordinates — a coordinate (not physical) singularity (see Module 7.5). The metric carries all geometric information; distances, angles, volumes, and the equations of motion all follow from $g_{\mu\nu}$.

**演示。** 在平坦时空中 $ds^2 = \eta_{\mu\nu}\, dx^\mu dx^\nu = -c^2 dt^2 + dx^2 + dy^2 + dz^2$。在半径为 $a$ 的二维球面上：$ds^2 = a^2(d\theta^2 + \sin^2\theta\, d\varphi^2)$，故 $g_{\theta\theta} = a^2$，$g_{\varphi\varphi} = a^2 \sin^2\theta$，$g_{\theta\varphi} = 0$。在史瓦西坐标下，黑洞的史瓦西半径处度规分量发散——这是坐标奇点（而非物理奇点）（见模块 7.5）。度规携带全部几何信息；距离、角度、体积以及运动方程均由 $g_{\mu\nu}$ 导出。

**Application.** Every computation in GR starts with specifying or solving for $g_{\mu\nu}$. Given a metric, one immediately reads off: proper distances ($\int ds$ along a path), local clock rates ($d\tau$), and the causal structure (sign of $ds^2$). The metric is the fundamental field of GR, replacing the Newtonian gravitational potential $\varphi$.

**应用。** 广义相对论中的每一个计算都从指定或求解 $g_{\mu\nu}$ 开始。给定度规后，可以直接读出：固有距离（沿路径的 $\int ds$）、局部时钟速率（$d\tau$）以及因果结构（$ds^2$ 的符号）。度规是广义相对论的基本场，取代了牛顿引力势 $\varphi$。

---

## 2. Connection, Covariant Derivative, and Curvature · 联络、协变导数与曲率

**Definition.** On a curved manifold, ordinary partial derivatives $\partial_\mu$ do not produce tensors when acting on tensors of rank $\geq 1$ (components mix under coordinate changes). The *Levi-Civita connection* (Christoffel symbols) resolves this:

**定义。** 在弯曲流形上，普通偏导数 $\partial_\mu$ 作用于秩 $\geq 1$ 的张量时不产生张量（分量在坐标变换下混合）。*列维-奇维塔联络*（克里斯托费尔符号）解决了这一问题：

$$ \Gamma^{\rho}{}_{\mu\nu} = \tfrac12\, g^{\rho\sigma} (\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}) $$

These are symmetric in the lower indices ($\Gamma^{\rho}{}_{\mu\nu} = \Gamma^{\rho}{}_{\nu\mu}$) and vanish in Minkowski coordinates. The *covariant derivative* of a contravariant vector is

下指标对称（$\Gamma^{\rho}{}_{\mu\nu} = \Gamma^{\rho}{}_{\nu\mu}$），在闵可夫斯基坐标下为零。逆变矢量的*协变导数*为

$$ \nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^{\nu}{}_{\mu\rho} V^\rho $$

and for a covariant vector $\nabla_\mu V_\nu = \partial_\mu V_\nu - \Gamma^{\rho}{}_{\mu\nu} V_\rho$. Covariant derivatives of the metric vanish: $\nabla_\rho g_{\mu\nu} = 0$ (*metric compatibility*).

协变矢量的协变导数为 $\nabla_\mu V_\nu = \partial_\mu V_\nu - \Gamma^{\rho}{}_{\mu\nu} V_\rho$。度规的协变导数为零：$\nabla_\rho g_{\mu\nu} = 0$（*度规相容性*）。

The *Riemann curvature tensor* measures the failure of covariant derivatives to commute:

*黎曼曲率张量*度量协变导数不对易的程度：

$$ [\nabla_\mu, \nabla_\nu] V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma $$

with components

其分量为

$$ R^{\rho}{}_{\sigma\mu\nu} = \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma} $$

From $R^{\rho}{}_{\sigma\mu\nu}$ one constructs:
- *Ricci tensor*: $R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu}$ (contraction on first and third index)
- *Ricci scalar*: $R = g^{\mu\nu} R_{\mu\nu}$
- *Einstein tensor*: $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$ (divergence-free: $\nabla_\mu G^{\mu\nu} = 0$)

由 $R^{\rho}{}_{\sigma\mu\nu}$ 可构造：
- *里奇张量*：$R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu}$（对第一和第三个指标缩并）
- *里奇标量*：$R = g^{\mu\nu} R_{\mu\nu}$
- *爱因斯坦张量*：$G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$（无散度：$\nabla_\mu G^{\mu\nu} = 0$）

**Demonstration.** On a 2-sphere of radius $a$, the only independent component of the Riemann tensor is $R_{\theta\varphi\theta\varphi} = a^2 \sin^2\theta$. The Ricci scalar is $R = 2/a^2$: constant positive curvature. As $a \to \infty$ the plane is recovered and $R \to 0$. For flat Minkowski space, all components of $R_{\mu\nu\rho\sigma}$ vanish identically — covariant derivatives commute and the global inertial frame exists.

**演示。** 在半径为 $a$ 的二维球面上，黎曼张量唯一独立的分量为 $R_{\theta\varphi\theta\varphi} = a^2 \sin^2\theta$。里奇标量为 $R = 2/a^2$：常正曲率。当 $a \to \infty$ 时还原为平面，$R \to 0$。对于平坦闵可夫斯基时空，$R_{\mu\nu\rho\sigma}$ 的所有分量恒为零——协变导数对易，整体惯性系存在。

**Application.** The Christoffel symbols enter the geodesic equation (Module 7.3) governing particle paths. The Einstein tensor $G_{\mu\nu}$, built entirely from $g_{\mu\nu}$ and its first two derivatives, is the geometric side of Einstein's field equations (Module 7.4). The contracted Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ guarantees energy-momentum conservation $\nabla_\mu T^{\mu\nu} = 0$ as a consequence of the geometry. This is the complete mathematical toolkit of curved spacetime, synthesizing the tensor calculus of Module 0.6 with the Lorentzian geometry of Module 1.13.

**应用。** 克里斯托费尔符号进入描述粒子路径的测地线方程（模块 7.3）。爱因斯坦张量 $G_{\mu\nu}$ 完全由 $g_{\mu\nu}$ 及其前两阶导数构成，是爱因斯坦场方程（模块 7.4）的几何一侧。缩并后的比安基恒等式 $\nabla_\mu G^{\mu\nu} = 0$ 保证了能量-动量守恒 $\nabla_\mu T^{\mu\nu} = 0$ 作为几何的必然结果。这是弯曲时空完整的数学工具箱，将模块 0.6 的张量微积分与模块 1.13 的洛伦兹几何综合在一起。

---

**Self-test (blank page)**

1. Starting from $g_{\mu\nu}$, derive the Christoffel symbols $\Gamma^{\rho}{}_{\mu\nu}$. Why are they not tensors, yet they are essential for defining the covariant derivative?
2. Write out all symmetries of the Riemann tensor $R_{\mu\nu\rho\sigma}$ (antisymmetries, pair symmetry, first Bianchi identity). How many independent components does it have in 4-D?
3. Verify that $\nabla_\rho g_{\mu\nu} = 0$ follows from the definition of $\Gamma$ — this is the condition of metric compatibility.

**自测（空白页）**

1. 从 $g_{\mu\nu}$ 出发，推导克里斯托费尔符号 $\Gamma^{\rho}{}_{\mu\nu}$。为何它们不是张量，却对定义协变导数至关重要？
2. 列出黎曼曲率张量 $R_{\mu\nu\rho\sigma}$ 的全部对称性（反对称性、对偶对称性、第一比安基恒等式）。在四维时空中它有多少个独立分量？
3. 验证 $\nabla_\rho g_{\mu\nu} = 0$ 由 $\Gamma$ 的定义导出——这是度规相容性条件。

---

← Previous: [Module 7.1 — The Equivalence Principle & Curved Spacetime](./module-7.1-equivalence-principle-and-curved-spacetime.md) · [Phase 7 index](./README.md) · Next: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) →

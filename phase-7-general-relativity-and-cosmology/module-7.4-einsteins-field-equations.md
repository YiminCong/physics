# Module 7.4 — Einstein's Field Equations ⭐⭐
**模块 7.4 — 爱因斯坦场方程 ⭐⭐**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.4-einsteins-field-equations-derivations.md)

---

## 1. The Stress–Energy Tensor and the Field Equations · 能动张量与场方程

**Definition.** The source of spacetime curvature is the *stress–energy tensor* $T_{\mu\nu}$ — a symmetric rank-2 tensor encoding the local density and flux of energy and momentum. Its components are:
- $T_{00}$ = energy density (includes rest mass, kinetic, internal energy)
- $T_{0i}$ = momentum density = $(1/c) \times$ energy flux in $x^i$ direction
- $T_{ij}$ = stress tensor (pressure on diagonal, shear off diagonal)

**定义。** 时空曲率的来源是*能动张量* $T_{\mu\nu}$——一个对称的二阶张量，编码了能量和动量的局部密度与通量。其分量为：
- $T_{00}$ = 能量密度（包括静止质量、动能、内能）
- $T_{0i}$ = 动量密度 = $(1/c) \times x^i$ 方向的能量通量
- $T_{ij}$ = 应力张量（对角线为压强，非对角线为切应力）

For a perfect fluid: $T_{\mu\nu} = (\rho + p/c^2)u_\mu u_\nu + p\, g_{\mu\nu}$, where $\rho$ is proper energy density, $p$ is pressure, and $u^\mu = dx^\mu/d\tau$ is the four-velocity. Conservation of energy-momentum is $\nabla_\mu T^{\mu\nu} = 0$.

对于完美流体：$T_{\mu\nu} = (\rho + p/c^2)u_\mu u_\nu + p\, g_{\mu\nu}$，其中 $\rho$ 为固有能量密度，$p$ 为压强，$u^\mu = dx^\mu/d\tau$ 为四速度。能量-动量守恒为 $\nabla_\mu T^{\mu\nu} = 0$。

Einstein's field equations (EFE) are:

爱因斯坦场方程（EFE）为：

$$ G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu} $$

This is a set of 10 coupled, nonlinear partial differential equations for $g_{\mu\nu}(x)$. The left side is purely geometric (the Einstein tensor, Module 7.2); the right side encodes matter and energy. In words: *matter tells spacetime how to curve, spacetime tells matter how to move*.

这是关于 $g_{\mu\nu}(x)$ 的 10 个耦合非线性偏微分方程组。左侧纯粹是几何量（爱因斯坦张量，模块 7.2）；右侧编码物质和能量。用语言描述：*物质告诉时空如何弯曲，时空告诉物质如何运动*。

With the *cosmological constant* $\Lambda$ (reintroduced for dark energy; see Module 7.6):

含*宇宙学常数* $\Lambda$ 的形式（为暗能量重新引入；见模块 7.6）：

$$ R_{\mu\nu} - \tfrac12 R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu} $$

**Demonstration.** *Newtonian limit*: in the weak-field, slow-matter limit, only the 00-component survives. $T_{00} \approx \rho c^2$, and $G_{00} \approx -2\nabla^2\Phi/c^2$ (where $\Phi$ is the Newtonian potential). The 00-component of the EFE gives $\nabla^2\Phi = 4\pi G\rho$ — Poisson's equation of Newtonian gravity (Module 1.1/1.5). GR reduces to Newtonian gravity in the appropriate limit.

**演示。** *牛顿极限*：在弱场、慢物质极限下，只有 00 分量存在。$T_{00} \approx \rho c^2$，$G_{00} \approx -2\nabla^2\Phi/c^2$（$\Phi$ 为牛顿引力势）。EFE 的 00 分量给出 $\nabla^2\Phi = 4\pi G\rho$——牛顿引力的泊松方程（模块 1.1/1.5）。广义相对论在适当极限下还原为牛顿引力。

*Vacuum equations*: when $T_{\mu\nu} = 0$ everywhere, the EFE reduce to $R_{\mu\nu} = 0$. This does not mean flat spacetime ($R_{\mu\nu\rho\sigma}$ need not vanish), merely traceless Ricci curvature. The Schwarzschild solution (Module 7.5) solves $R_{\mu\nu} = 0$ outside a spherical mass.

*真空方程*：当处处 $T_{\mu\nu} = 0$ 时，EFE 化为 $R_{\mu\nu} = 0$。这不意味着时空平坦（$R_{\mu\nu\rho\sigma}$ 无需为零），仅意味着里奇曲率无迹。史瓦西解（模块 7.5）正是球对称质量外部 $R_{\mu\nu} = 0$ 的解。

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

The coefficient $8\pi G/c^4 \approx 2.07 \times 10^{-43}$ m/J makes gravity extraordinarily weak: enormous energy densities produce tiny metric perturbations in ordinary conditions.

系数 $8\pi G/c^4 \approx 2.07 \times 10^{-43}$ m/J 使引力极为微弱：在通常条件下，极大的能量密度也只能产生极微小的度规扰动。

---

## 2. The Einstein–Hilbert Action · 爱因斯坦-希尔伯特作用量

**Definition.** Like all fundamental laws in physics, the EFE follow from a variational principle (Module 1.3). The *Einstein–Hilbert action* is:

**定义。** 与物理学中所有基本定律一样，EFE 由变分原理（模块 1.3）导出。*爱因斯坦-希尔伯特作用量*为：

$$ S = \frac{c^4}{16\pi G} \int (R - 2\Lambda) \sqrt{-g}\, d^4 x + S_\text{matter} $$

where $g = \det(g_{\mu\nu})$ and $\sqrt{-g}\, d^4 x$ is the invariant spacetime volume element. Varying $S$ with respect to the metric $g_{\mu\nu}$ and setting $\delta S/\delta g^{\mu\nu} = 0$ yields exactly the EFE with cosmological constant.

其中 $g = \det(g_{\mu\nu})$，$\sqrt{-g}\, d^4 x$ 是不变时空体积元。对度规 $g_{\mu\nu}$ 变分并令 $\delta S/\delta g^{\mu\nu} = 0$，精确地给出含宇宙学常数的 EFE。

**Demonstration.** The variation produces three terms: (i) variation of $R_{\mu\nu}$ gives a surface term (Gibbons–Hawking–York boundary term, discarded); (ii) variation of $R$ gives $R_{\mu\nu}\, \delta g^{\mu\nu}$; (iii) variation of $\sqrt{-g}$ gives $-\tfrac12 g_{\mu\nu} R\, \delta g^{\mu\nu}$. Together: $\delta(R\sqrt{-g}) = \sqrt{-g}(R_{\mu\nu} - \tfrac12 R g_{\mu\nu})\, \delta g^{\mu\nu} = \sqrt{-g}\, G_{\mu\nu}\, \delta g^{\mu\nu}$. The matter action variation defines $T_{\mu\nu} = -(2/\sqrt{-g})\, \delta S_\text{matter}/\delta g^{\mu\nu}$, completing the derivation.

**演示。** 变分产生三项：(i) $R_{\mu\nu}$ 的变分给出一个面项（吉本斯-霍金-约克边界项，舍去）；(ii) $R$ 的变分给出 $R_{\mu\nu}\, \delta g^{\mu\nu}$；(iii) $\sqrt{-g}$ 的变分给出 $-\tfrac12 g_{\mu\nu} R\, \delta g^{\mu\nu}$。合并得：$\delta(R\sqrt{-g}) = \sqrt{-g}(R_{\mu\nu} - \tfrac12 R g_{\mu\nu})\, \delta g^{\mu\nu} = \sqrt{-g}\, G_{\mu\nu}\, \delta g^{\mu\nu}$。物质作用量的变分定义了 $T_{\mu\nu} = -(2/\sqrt{-g})\, \delta S_\text{matter}/\delta g^{\mu\nu}$，从而完成推导。

**Application.** The action formulation is essential for:
- Coupling GR to quantum fields (semiclassical gravity, Hawking radiation)
- Systematically adding higher-order curvature corrections (theories beyond GR)
- Deriving conservation laws via Noether's theorem — the contracted Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ is an automatic consequence of diffeomorphism invariance of the action
- Extensions such as Brans–Dicke theory, $f(R)$ gravity, and string-theory-motivated corrections

**应用。** 作用量形式对以下方面至关重要：
- 将广义相对论与量子场耦合（半经典引力、霍金辐射）
- 系统地添加高阶曲率修正（超越广义相对论的理论）
- 通过诺特定理推导守恒律——缩并比安基恒等式 $\nabla_\mu G^{\mu\nu} = 0$ 是作用量微分同胚不变性的自动结果
- 布兰斯-迪克理论、$f(R)$ 引力以及弦论启发的修正等推广

The EFE, derived from the simplest possible covariant action linear in $R$, are arguably the most elegant fundamental law in physics.

EFE 由关于 $R$ 最简单的协变作用量（对 $R$ 线性）推导而来，可以说是物理学中最优美的基本定律。

## Key results · 核心结果

- $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \dfrac{8\pi G}{c^4} T_{\mu\nu}$ — Einstein's field equations (add $+\Lambda g_{\mu\nu}$ for dark energy) · 爱因斯坦场方程（含 $\Lambda$ 项）
- $\nabla_\mu T^{\mu\nu} = 0$ — local energy–momentum conservation, from the Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ · 由比安基恒等式给出的能动量守恒
- $S = \dfrac{c^4}{16\pi G} \int (R - 2\Lambda) \sqrt{-g}\, d^4 x + S_\text{matter}$ — Einstein–Hilbert action · 爱因斯坦–希尔伯特作用量
- *Matter tells spacetime how to curve; spacetime tells matter how to move.* · 物质告诉时空如何弯曲，时空告诉物质如何运动

---

**Self-test (blank page)**

1. Write down the EFE in full, identify each tensor, and state the physical meaning of both sides. What does the factor $8\pi G/c^4$ tell you about the stiffness of spacetime?
2. Show that $\nabla_\mu T^{\mu\nu} = 0$ follows automatically from the EFE and the contracted Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$. Why is this physically satisfying?
3. Write down $T_{\mu\nu}$ for a perfect fluid. In the non-relativistic limit ($p \ll \rho c^2$), what does the EFE reduce to?

**自测（空白页）**

1. 完整写出 EFE，标明每个张量，陈述两侧的物理含义。系数 $8\pi G/c^4$ 说明了时空"刚度"的什么特征？
2. 证明 $\nabla_\mu T^{\mu\nu} = 0$ 由 EFE 和缩并比安基恒等式 $\nabla_\mu G^{\mu\nu} = 0$ 自动得出。为何这在物理上令人满意？
3. 写出完美流体的 $T_{\mu\nu}$。在非相对论极限（$p \ll \rho c^2$）下，EFE 化为什么？

---

← Previous: [Module 7.3 — Geodesics & the Motion of Particles](./module-7.3-geodesics-and-motion-of-particles.md) · [Phase 7 index](./README.md) · Next: [Module 7.5 — Black Holes & Gravitational Waves](./module-7.5-black-holes-and-gravitational-waves.md) →

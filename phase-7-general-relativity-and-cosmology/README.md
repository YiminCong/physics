---
title: "Phase 7 — General Relativity & Cosmology"
nav_order: 8
has_children: true
---

# Phase 7 — General Relativity & Cosmology
**第 7 阶段 — 广义相对论与宇宙学**

General Relativity reframes gravity not as a force but as the curvature of spacetime, with matter and energy as its source. Starting from Einstein's equivalence principle, this phase builds the full mathematical machinery — metrics, connections, and curvature tensors — and arrives at Einstein's field equations, then applies them to the universe's most extreme objects (black holes, gravitational waves) and to the universe as a whole (the Big Bang, dark matter, dark energy). Each module follows the **Definition → Demonstration → Application** format for efficient revision.

广义相对论将引力重新诠释为时空的弯曲，而非一种力，物质和能量是其来源。从爱因斯坦的等效原理出发，本阶段构建完整的数学机制——度规、联络与曲率张量——推导爱因斯坦场方程，并将其应用于宇宙中最极端的天体（黑洞、引力波）以及宇宙整体（大爆炸、暗物质、暗能量）。每个模块遵循**定义 → 演示 → 应用**格式，便于高效复习。

## Prerequisites · 前置条件

- **Phase 1 Special Relativity** (Modules 1.13–1.15): Minkowski spacetime, four-vectors, proper time, the field tensor — the flat-spacetime foundation that GR generalizes.
- **第 1 阶段 狭义相对论**（模块 1.13–1.15）：闵可夫斯基时空、四维矢量、固有时、场张量——广义相对论加以推广的平坦时空基础。
- **Phase 0 tensors** (Module 0.6): index notation, metric tensors, and differential forms — the mathematical language used throughout.
- **第 0 阶段 张量**（模块 0.6）：指标符号、度规张量与微分形式——贯穿全程所用的数学语言。
- **Newtonian gravity** (Module 1.5): Kepler orbits, the gravitational potential $\varphi$, and Poisson's equation — the Newtonian limit that GR must reproduce.
- **牛顿引力**（模块 1.5）：开普勒轨道、引力势 $\varphi$ 与泊松方程——广义相对论必须能还原的牛顿极限。

## Modules · 模块

| Module | Title · 标题 | Stars |
|--------|-------------|-------|
| [7.1](./module-7.1-equivalence-principle-and-curved-spacetime.md) | The Equivalence Principle & Curved Spacetime · 等效原理与弯曲时空 | ⭐ |
| [7.2](./module-7.2-tensors-metric-and-curvature.md) | Tensors, the Metric & Curvature · 张量、度规与曲率 | ⭐ |
| [7.3](./module-7.3-geodesics-and-motion-of-particles.md) | Geodesics & the Motion of Particles · 测地线与粒子运动 | |
| [7.4](./module-7.4-einsteins-field-equations.md) | Einstein's Field Equations · 爱因斯坦场方程 | ⭐⭐ |
| [7.5](./module-7.5-black-holes-and-gravitational-waves.md) | Black Holes & Gravitational Waves · 黑洞与引力波 | ⭐ |
| [7.6](./module-7.6-cosmology.md) | Cosmology · 宇宙学 | |
| [7.7](./module-7.7-tests-of-gr-and-gravitational-wave-astronomy.md) | Tests of GR & Gravitational-Wave Astronomy · 广义相对论的检验与引力波天文学 | ⭐ |
| [7.8](./module-7.8-global-structure-and-singularity-theorems.md) | Global Structure & Singularity Theorems · 整体结构与奇点定理 | ⭐⭐ |

## Phase 7 Checkpoint (blank page)

1. State the strong equivalence principle and explain how it forces gravity to be described by a curved spacetime metric rather than a force field in flat spacetime.
2. Starting from the metric $g_{\mu\nu}$, construct the Christoffel symbols $\Gamma^{\rho}{}_{\mu\nu}$, the Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$, the Ricci tensor $R_{\mu\nu}$, and the Einstein tensor $G_{\mu\nu}$. What symmetries reduce the number of independent components at each step?
3. Write down the geodesic equation and show that it reduces to Newton's second law $d^2 x^i/dt^2 = -\partial^i \varphi$ in the appropriate limit. What three approximations are required?
4. Write down Einstein's field equations with cosmological constant. Identify every tensor. Explain why $\nabla_\mu T^{\mu\nu} = 0$ follows automatically, and what this means physically.
5. What is the Schwarzschild radius? Describe what happens — physically and mathematically — at $r = r_s$ and at $r = 0$ for the Schwarzschild solution. How does the Kerr metric differ?
6. Write down the FLRW metric and the two Friedmann equations. What energy components drive the current accelerated expansion? What observational evidence establishes the existence of dark matter and dark energy?
7. State the four classical tests of GR (perihelion precession, light deflection, gravitational redshift, Shapiro delay) and give the key numerical prediction for each. What is the Lense–Thirring effect and how was it measured?
8. Define the chirp mass $\mathcal{M}_c$ and show how it is extracted from the GW frequency evolution $df/dt$. Describe the multi-messenger significance of GW170817.
9. Define a trapped surface and state the three hypotheses of the Penrose singularity theorem. How does the Raychaudhuri equation force focusing?
10. Explain why the Schwarzschild singularity at $r = 2GM/c^2$ is a coordinate singularity while $r = 0$ is a genuine one. Describe the four regions of the Kruskal extension.

**自测（空白页）**

1. 陈述强等效原理，并解释它如何迫使引力须用弯曲时空度规而非平坦时空中的力场来描述。
2. 从度规张量 $g_{\mu\nu}$ 出发，构造克里斯托费尔符号 $\Gamma^{\rho}{}_{\mu\nu}$、黎曼曲率张量 $R^{\rho}{}_{\sigma\mu\nu}$、里奇张量 $R_{\mu\nu}$ 和爱因斯坦张量 $G_{\mu\nu}$。每一步哪些对称性减少了独立分量的数目？
3. 写出测地线方程，并证明在适当极限下它化为牛顿第二定律 $d^2 x^i/dt^2 = -\partial^i \varphi$。需要哪三个近似？
4. 写出含宇宙学常数的爱因斯坦场方程，标明每个张量，解释为何 $\nabla_\mu T^{\mu\nu} = 0$ 自动成立，以及其物理意义。
5. 史瓦西半径是什么？描述史瓦西解在 $r = r_s$ 和 $r = 0$ 处的物理与数学行为。克尔度规有何不同？
6. 写出 FLRW 度规和两个弗里德曼方程。哪些能量成分驱动当前的加速膨胀？哪些观测证据确立了暗物质和暗能量的存在？
7. 陈述广义相对论的四个经典检验（近日点进动、光线偏折、引力红移、夏皮罗延迟），并给出每个检验的关键数值预测。楞次–蒂林效应是什么，如何测量？
8. 定义啁啾质量 $\mathcal{M}_c$，并说明如何从引力波频率演化 $df/dt$ 中提取它。描述 GW170817 多信使观测的意义。
9. 定义囚禁面，陈述彭罗斯奇点定理的三个假设。雷乔杜里方程如何迫使测地线聚焦？
10. 解释为何史瓦西解在 $r = 2GM/c^2$ 处的奇点是坐标奇点，而 $r = 0$ 处的是真实奇点。描述克鲁斯卡尔延拓的四个区域。

---

→ Continue to **[Phase 8 — Particle Physics & the Standard Model](../phase-8-particle-physics-and-standard-model/)**.

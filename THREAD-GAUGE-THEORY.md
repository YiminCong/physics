# The Gauge Principle — A Thread Through the Curriculum
# 规范原理 — 贯穿课程的主线

One idea runs from 19th-century electromagnetism to the Standard Model: **demand that a
symmetry hold independently at every point of spacetime (a *local* symmetry), and a force
field is forced into existence to make it possible.** This document threads that single idea —
the **gauge principle** — through every module in the curriculum where it appears, so you can
read the storyline end to end. Each stage links to the module and its ✅-verified
`*-derivations.md` companion.

有一个思想从 19 世纪的电磁学一路贯穿到标准模型：**要求一个对称性在时空每一点独立成立
（*局域*对称性），便迫使一个力场存在以使之成为可能。** 本文档将这一思想——**规范原理**
——串联到课程中出现它的每一个模块，使你能从头到尾读懂这条故事线。每一阶段都链接到对应模块
及其 ✅ 已校验的 `*-derivations.md` 配套文件。

---

## The storyline at a glance · 故事线一览

| Stage · 阶段 | Symmetry / group · 对称性/群 | Force field that appears · 出现的力场 | Key equation · 关键方程 | Module |
|---|---|---|---|---|
| Math foundation · 数学基础 | Lie groups $U(1)$, $SU(N)$ | — | $[X, Y] = if^{abc}T^c$ | [0.7](./phase-0-mathematical-foundations/module-0.7-group-theory-and-lie-algebras.md) |
| Classical EM · 经典电磁 | $U(1)$, *global* phase | electromagnetic $A_\mu$ | $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ | [1.10](./phase-1-classical-physics/module-1.10-electrodynamics-maxwell-equations.md), [1.15](./phase-1-classical-physics/module-1.15-covariant-electromagnetism.md) |
| Quantum EM · 量子电磁 | $U(1)$ *local* phase | photon (gauged) | $D_\mu = \partial_\mu + ieA_\mu$ | [8.2](./phase-8-particle-physics-and-standard-model/module-8.2-quantum-electrodynamics.md) |
| The gauge principle · 规范原理 | local $U(1) \to SU(N)$ | Yang–Mills $A^a_\mu$ | $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$ | [8.1](./phase-8-particle-physics-and-standard-model/module-8.1-symmetries-and-gauge-theory.md) |
| Strong force · 强相互作用 | $SU(3)_\text{color}$ | 8 gluons (self-interacting) | $\beta(g) < 0 \to$ asymptotic freedom | [8.3](./phase-8-particle-physics-and-standard-model/module-8.3-quantum-chromodynamics.md) |
| Broken gauge symmetry · 破缺规范对称 | $SU(2)_L \times U(1)_Y \to U(1)_\text{em}$ | $W^\pm$, $Z^0$ get mass; photon massless | $m_W = \tfrac12 gv$, $m_Z = m_W/\cos\theta_W$ | [8.4](./phase-8-particle-physics-and-standard-model/module-8.4-electroweak-theory-and-higgs.md) |
| Condensed-matter sibling · 凝聚态对应 | local $U(1)$ (Cooper pairs) | photon gets mass *inside* a superconductor | Meissner: $\nabla^2 B = B/\lambda^2$ | [5.3](./phase-5-superconductivity/module-5.3-ginzburg-landau-theory.md) |
| Quantizing gauge fields · 规范场量子化 | BRST (residual rigid) | Faddeev–Popov ghosts | $s^2 = 0$, $\mathcal{L}_\text{gf+gh} = s\Psi$ | [8.1 §E](./phase-8-particle-physics-and-standard-model/module-8.1-derivations.md), [6.5](./phase-6-quantum-field-theory/module-6.5-canonical-quantization.md) |
| When symmetry fails quantally · 量子反常 | anomalous currents | triangle anomaly | $\partial_\mu j^{\mu 5} = (e^2/16\pi^2)\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | [6.9](./phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft.md) |
| Synthesis · 综合 | $SU(3) \times SU(2) \times U(1)$ | the Standard Model | one Lagrangian | [8.5](./phase-8-particle-physics-and-standard-model/module-8.5-standard-model-and-beyond.md) |

---

## 1. The mathematics: what a gauge group *is* · 数学：规范群是什么

Before physics, the objects. A **gauge group** is a Lie group whose elements can vary
from point to point. Module 0.7 builds $U(1)$ (phases $e^{i\alpha}$), $SU(2)$, $SU(3)$, their generators
$T^a$, the Lie algebra $[T^a, T^b] = if^{abc}T^c$, and the structure constants $f^{abc}$ that will
become the gluon self-coupling. Everything downstream is this algebra made local.

在物理之前，先有对象。**规范群**是一个其元素可逐点变化的李群。模块 0.7 构建 $U(1)$（相位
$e^{i\alpha}$）、$SU(2)$、$SU(3)$，它们的生成元 $T^a$、李代数 $[T^a, T^b] = if^{abc}T^c$，以及将成为
胶子自耦合的结构常数 $f^{abc}$。后续一切都是这套代数的局域化。

→ [Module 0.7 — Group Theory & Lie Algebras](./phase-0-mathematical-foundations/module-0.7-group-theory-and-lie-algebras.md) · [derivations](./phase-0-mathematical-foundations/module-0.7-group-theory-and-lie-algebras-derivations.md)

## 2. Classical electromagnetism = the original $U(1)$ gauge theory · 经典电磁学 = 最初的 $U(1)$ 规范理论

Maxwell's four equations, the potential $A_\mu = (\phi/c, \mathbf{A})$, the field tensor
$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, and the gauge freedom $A_\mu \to A_\mu + \partial_\mu\chi$ are the prototype. The
derivations show: (i) $F_{\mu\nu}$ packages **E** and **B** and is automatically gauge-invariant;
(ii) $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ reproduces Gauss + Ampère–Maxwell; (iii) — **newly added** — all of
this follows from a *single action* $S = \int(-\tfrac14 F_{\mu\nu}F^{\mu\nu}/\mu_0 - J^\mu A_\mu)\, d^4x$ by varying $A_\mu$,
with the homogeneous equations being the Bianchi identity of $F = dA$.

麦克斯韦四方程、势 $A_\mu = (\phi/c, \mathbf{A})$、场张量 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$，以及规范自由
$A_\mu \to A_\mu + \partial_\mu\chi$ 是原型。推导给出：(i) $F_{\mu\nu}$ 打包 **E** 与 **B** 且自动规范不变；
(ii) $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ 重现高斯 + 安培–麦克斯韦；(iii)——**新增**——这一切都来自*单一作用量*
$S = \int(-\tfrac14 F_{\mu\nu}F^{\mu\nu}/\mu_0 - J^\mu A_\mu)\, d^4x$ 对 $A_\mu$ 的变分，齐次方程即 $F = dA$ 的比安基恒等式。

→ [1.10 Maxwell Equations](./phase-1-classical-physics/module-1.10-electrodynamics-maxwell-equations.md) · [1.15 Covariant EM](./phase-1-classical-physics/module-1.15-covariant-electromagnetism.md) · [**derivations incl. action principle (§E)**](./phase-1-classical-physics/module-1.15-covariant-electromagnetism-derivations.md)

## 3. Gauging the phase: from global to local · 规范化相位：从整体到局域

A free Dirac field has a *global* $U(1)$ symmetry $\psi \to e^{i\alpha}\psi$ (Noether $\to$ conserved charge).
Promote $\alpha \to \alpha(x)$, and the kinetic term breaks — unless you introduce $A_\mu$ with the transform
$A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ and replace $\partial_\mu \to D_\mu = \partial_\mu + ieA_\mu$. **The photon is the price of local
phase invariance.** This is *minimal coupling*; its quantum theory is QED.

自由狄拉克场有*整体* $U(1)$ 对称性 $\psi \to e^{i\alpha}\psi$（诺特 $\to$ 守恒荷）。令 $\alpha \to \alpha(x)$，动能项破坏
——除非引入 $A_\mu$，其变换为 $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$，并将 $\partial_\mu \to D_\mu = \partial_\mu + ieA_\mu$。**光子是
局域相位不变性的代价。** 这就是*最小耦合*；其量子理论即 QED。

→ [8.1 §A–B ($U(1)$ gauging)](./phase-8-particle-physics-and-standard-model/module-8.1-derivations.md) · [8.2 QED](./phase-8-particle-physics-and-standard-model/module-8.2-quantum-electrodynamics.md)

## 4. Yang–Mills: the gauge principle for non-abelian groups · 杨–米尔斯：非阿贝尔群的规范原理

Repeat the construction with a non-abelian group $G = SU(N)$. The covariant derivative
$D_\mu = \partial_\mu - igA^a_\mu T^a$ and the field strength acquire an extra, *self-interaction* term:
$F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$. Because the gauge bosons carry the charge
they mediate, they couple to themselves — the three- and four-gluon vertices absent in
Maxwell. This single nonlinear term is the origin of asymptotic freedom and confinement.

用非阿贝尔群 $G = SU(N)$ 重复此构造。协变导数 $D_\mu = \partial_\mu - igA^a_\mu T^a$ 与场强获得一个额外的
*自相互作用*项：$F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$。由于规范玻色子携带它们
所传递的荷，它们与自身耦合——这是麦克斯韦中没有的三胶子与四胶子顶角。这个非线性项正是渐近
自由与禁闭的根源。

→ [**8.1 Symmetries & Gauge Theory**](./phase-8-particle-physics-and-standard-model/module-8.1-symmetries-and-gauge-theory.md) · [derivations §C (non-abelian)](./phase-8-particle-physics-and-standard-model/module-8.1-derivations.md)

## 5. QCD: $SU(3)$ in the real world · QCD：现实世界中的 $SU(3)$

Color $SU(3)$, eight gluons, the running coupling, and asymptotic freedom ($\beta_0 = 11 - 2n_f/3$).
The gluon self-coupling of Stage 4 makes the $\beta$ function negative — the coupling weakens at
high energy. This is where the **Faddeev–Popov ghosts** of Stage 7 first earn their keep:
their loops supply part of the $+11C_A/3$.

色 $SU(3)$、八个胶子、跑动耦合与渐近自由（$\beta_0 = 11 - 2n_f/3$）。第 4 阶段的胶子自耦合使 $\beta$
函数为负——耦合在高能下减弱。这正是第 7 阶段的**法捷耶夫–波波夫鬼粒子**首次发挥作用之处：
它们的圈为 $+11C_A/3$ 提供部分贡献。

→ [8.3 QCD](./phase-8-particle-physics-and-standard-model/module-8.3-quantum-chromodynamics.md) · [derivations ($\beta$ function)](./phase-8-particle-physics-and-standard-model/module-8.3-derivations.md)

## 6. Spontaneously broken gauge symmetry: mass without breaking gauge invariance · 自发破缺的规范对称性

A gauge boson is massless because a mass term $m^2 A_\mu A^\mu$ is not gauge-invariant. The **Higgs
mechanism** evades this: a scalar field with a nonzero vacuum value breaks $SU(2)_L \times U(1)_Y$
down to $U(1)_\text{em}$; the would-be Goldstone bosons become the longitudinal polarizations of $W^\pm$
and $Z^0$, which thereby gain mass, while the photon stays massless. Remarkably, the *same
physics* appears in condensed matter: inside a superconductor the photon is effectively
massive (Meissner effect, finite penetration depth $\lambda$) — the **Anderson–Higgs mechanism**,
described classically by Ginzburg–Landau theory.

规范玻色子无质量，因为质量项 $m^2 A_\mu A^\mu$ 非规范不变。**希格斯机制**规避了这一点：一个具有非零
真空值的标量场将 $SU(2)_L \times U(1)_Y$ 破缺至 $U(1)_\text{em}$；本应是戈德斯通玻色子的自由度变成 $W^\pm$ 和
$Z^0$ 的纵向极化，由此获得质量，而光子保持无质量。值得注意的是，*相同的物理*出现在凝聚态中：
超导体内部光子有效地获得质量（迈斯纳效应、有限穿透深度 $\lambda$）——即**安德森–希格斯机制**，由
金兹堡–朗道理论在经典层面描述。

→ [8.4 Electroweak & Higgs](./phase-8-particle-physics-and-standard-model/module-8.4-electroweak-theory-and-higgs.md) · condensed-matter sibling: [5.3 Ginzburg–Landau](./phase-5-superconductivity/module-5.3-ginzburg-landau-theory.md), [5.2 London](./phase-5-superconductivity/module-5.2-london-theory.md)

## 7. Quantizing gauge fields: Faddeev–Popov & BRST · 规范场量子化：法捷耶夫–波波夫与 BRST

Gauge redundancy makes the naive path integral ill-defined (infinite gauge-orbit volume,
non-invertible kinetic operator). Fixing the gauge introduces a gauge-fixing term
$-(1/2\xi)(\partial\cdot A)^2$ and the **Faddeev–Popov ghosts**. What survives is a single rigid fermionic
symmetry — **BRST symmetry**, nilpotent ($s^2 = 0$) — whose cohomology defines the physical
states, guarantees unitarity, and produces the Slavnov–Taylor identities that control
renormalization. **(Newly added: full Faddeev–Popov + BRST derivation in 8.1 §E.)**

规范冗余使朴素路径积分病态（无穷大的规范轨道体积、不可逆的动能算符）。固定规范引入规范固定项
$-(1/2\xi)(\partial\cdot A)^2$ 与**法捷耶夫–波波夫鬼粒子**。幸存下来的是单一刚性费米型对称性——**BRST 对称
性**，幂零（$s^2 = 0$）——其上同调定义物理态、保证幺正性，并产生控制重整化的斯拉夫诺夫–泰勒
恒等式。**（新增：8.1 §E 给出完整的法捷耶夫–波波夫 + BRST 推导。）**

→ [**8.1 §E (Faddeev–Popov + BRST)**](./phase-8-particle-physics-and-standard-model/module-8.1-derivations.md) · [6.5 Canonical Quantization](./phase-6-quantum-field-theory/module-6.5-canonical-quantization.md) · [6.4 Path Integrals](./phase-6-quantum-field-theory/module-6.4-path-integrals.md)

## 8. When a gauge symmetry fails quantum-mechanically: anomalies · 规范对称性的量子失效：反常

A symmetry of the classical action can be broken by quantization (the triangle diagram). A
*gauge* anomaly would be fatal — it destroys unitarity — so the Standard Model's fermion
content is precisely arranged for the gauge anomalies to cancel ($\sum$ charges $= 0$ per
generation). The surviving *global* anomaly ($\pi^0 \to \gamma\gamma$) is a triumph, not a problem.

经典作用量的对称性可被量子化破坏（三角图）。*规范*反常将是致命的——它破坏幺正性——所以标准
模型的费米子内容被精确安排使规范反常相消（每代 $\sum$ 荷 $= 0$）。幸存的*整体*反常（$\pi^0 \to \gamma\gamma$）是
成就而非问题。

→ [6.9 Anomalies & Nonperturbative QFT](./phase-6-quantum-field-theory/module-6.9-anomalies-and-nonperturbative-qft.md)

## 9. Synthesis: the Standard Model Lagrangian · 综合：标准模型拉格朗日量

$SU(3)_c \times SU(2)_L \times U(1)_Y$, one gauge-covariant derivative acting on every field, three
gauge couplings running toward (near-)unification, the Higgs giving mass — the entire
known particle content in one gauge-invariant Lagrangian.

$SU(3)_c \times SU(2)_L \times U(1)_Y$，一个作用于每个场的规范协变导数，三个朝向（近似）统一跑动的规范
耦合，希格斯赋予质量——全部已知粒子内容尽在一个规范不变的拉格朗日量中。

→ [8.5 The Standard Model & Beyond](./phase-8-particle-physics-and-standard-model/module-8.5-standard-model-and-beyond.md)

---

## Key equations of the whole thread · 整条主线的关键方程

| Concept · 概念 | Equation · 方程 |
|---|---|
| Covariant derivative (abelian) · 协变导数（阿贝尔） | $D_\mu = \partial_\mu + ieA_\mu$ |
| Covariant derivative (non-abelian) · 协变导数（非阿贝尔） | $D_\mu = \partial_\mu - igA^a_\mu T^a$ |
| Field strength (abelian) · 场强（阿贝尔） | $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ |
| Field strength (non-abelian) · 场强（非阿贝尔） | $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$ |
| Yang–Mills action · 杨–米尔斯作用量 | $S = -\tfrac14\int F^a_{\mu\nu}F^{a\mu\nu}\, d^4x$ |
| Equation of motion · 运动方程 | $D_\mu F^{a\mu\nu} = J^{a\nu}$ |
| Bianchi identity · 比安基恒等式 | $D_\mu \tilde{F}^{a\mu\nu} = 0$ |
| Gauge-fixed Lagrangian · 规范固定拉格朗日量 | $\mathcal{L} = -\tfrac14 F^2 - (1/2\xi)(\partial\cdot A)^2 + \bar{c}(-\partial\cdot D)c$ |
| BRST nilpotency · BRST 幂零性 | $s^2 = 0,\ \mathcal{L}_\text{gf+gh} = s\Psi$ |

---

## Suggested reading order · 建议阅读顺序

0.7 → 1.8 → 1.9 → 1.10 → 1.15 → 8.1 → 8.2 → 8.3 → 5.2 → 5.3 → 8.4 → 6.4 → 6.5 → 6.9 → 8.5.

The first five build classical and quantum $U(1)$; 8.1 generalizes the principle; 8.3 and 8.4
are the two non-abelian realizations (unbroken and broken); 5.2–5.3 give the condensed-matter
mirror; 6.x supplies the quantization machinery; 8.5 ties it together.

前五个建立经典与量子 $U(1)$；8.1 推广原理；8.3 与 8.4 是两种非阿贝尔实现（未破缺与破缺）；
5.2–5.3 给出凝聚态镜像；6.x 提供量子化机制；8.5 将其汇集。

---

*See also: [README](./README.md) · [GLOSSARY](./GLOSSARY.md) · [VERIFICATION](./VERIFICATION.md) · [ROADMAP-THOOFT](./ROADMAP-THOOFT.md)*

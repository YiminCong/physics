# Module 7.8 — Global Structure & Singularity Theorems
**模块 7.8 — 整体结构与奇点定理**

> **Phase 7 — [General Relativity & Cosmology](./README.md)** · Format: Definition → Demonstration → Application
> **第 7 阶段 — 广义相对论与宇宙学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-7.8-global-structure-and-singularity-theorems-derivations.md)

---

## 1. Causal Structure and the Maximal Extension of Schwarzschild · 因果结构与史瓦西解的极大延拓

**Definition.** The *causal structure* of a spacetime is determined by how light cones are arranged at each event. Two events are *causally connected* if a future-directed causal (timelike or null) curve links them; otherwise they are *spacelike separated*. In curved spacetime, light cones tip and squeeze due to curvature, potentially creating regions from which no signal can escape — *black holes* — or into which no signal can enter — *white holes*.

**定义。** 时空的*因果结构*由每个事件处光锥的排列方式决定。若两个事件之间存在面向未来的因果（类时或类光）曲线相连，则它们*因果相关*；否则为*类空分离*。在弯曲时空中，曲率使光锥倾斜和压缩，可能产生信号无法逃脱的区域——*黑洞*——或信号无法进入的区域——*白洞*。

**Demonstration — Penrose Diagrams.** A *conformal (Penrose) diagram* compresses the entire spacetime onto a finite page by a conformal rescaling g_{μν} → Ω² g_{μν} that preserves angles (and hence causal structure) but brings infinity to a finite location. In the resulting diagram, null geodesics always travel at ±45°, making the causal structure transparent.

**演示——彭罗斯图。** *共形（彭罗斯）图*通过共形重缩放 g_{μν} → Ω² g_{μν}（保持角度，从而保持因果结构，但将无穷远压缩到有限位置），将整个时空压缩到有限页面上。在所得图中，类光测地线始终沿 ±45° 传播，使因果结构一目了然。

Key features of Penrose diagrams:
- *Future null infinity* i⁺: where future-directed null geodesics end (massless particles escape to here).
- *Future timelike infinity* i⁺: where future-directed timelike geodesics end (massive particles at late times).
- *Spacelike infinity* i⁰: where spacelike hypersurfaces end.
- *Event horizon*: a null surface in the diagram; the boundary of the region from which signals can reach i⁺.
- *Apparent horizon*: a surface where outgoing null rays have zero expansion; defined quasi-locally (can differ from the event horizon in dynamic spacetimes).

彭罗斯图的关键特征：
- *未来类光无穷远* ℐ⁺：面向未来的类光测地线终止处（无质量粒子逃至此处）。
- *未来类时无穷远* i⁺：面向未来的类时测地线终止处（大质量粒子的晚期归宿）。
- *类空无穷远* i⁰：类空超曲面的终止处。
- *事件视界*：图中的类光曲面；信号能到达 ℐ⁺ 的区域之边界。
- *表观视界*：向外类光线膨胀率为零的曲面；准局域定义（在动态时空中可与事件视界不同）。

**Demonstration — Kruskal Extension of Schwarzschild.** The Schwarzschild metric has a coordinate singularity at r = 2GM/c² (the horizon). In Kruskal–Szekeres coordinates (T, X), defined by (see Derivations A):

**演示——史瓦西解的克鲁斯卡尔延拓。** 史瓦西度规在 r = 2GM/c²（视界）处有坐标奇点。克鲁斯卡尔–塞克雷斯坐标 (T, X)（见推导 A）定义为：

For r > 2GM/c²:   T = (r/r_s − 1)^{1/2} e^{r/(2r_s)} sinh(tc/(2r_s)),
                  X = (r/r_s − 1)^{1/2} e^{r/(2r_s)} cosh(tc/(2r_s))

For r < 2GM/c²:   T = (1 − r/r_s)^{1/2} e^{r/(2r_s)} cosh(tc/(2r_s)),
                  X = (1 − r/r_s)^{1/2} e^{r/(2r_s)} sinh(tc/(2r_s))

The metric becomes:

度规变为：

  ds² = (32G³M³/c⁶r) e^{−r c²/(2GM)} (−dT² + dX²) + r² dΩ²

This is manifestly regular at r = 2GM/c² (T² − X² = 0). The full Kruskal diagram reveals four regions:
- **Region I** (X > |T|): the original exterior r > r_s, where observers live.
- **Region II** (T > |X|): the black hole interior, r < r_s, with future singularity at r = 0 (T² − X² = 1).
- **Region III** (X < −|T|): a second exterior — a *parallel universe* with no causal connection to Region I.
- **Region IV** (T < −|X|): a white hole interior, r < r_s, with past singularity.

度规在 r = 2GM/c²（T² − X² = 0）处显然是正则的。完整的克鲁斯卡尔图揭示了四个区域：
- **区域 I**（X > |T|）：原始外部 r > r_s，观测者居于此处。
- **区域 II**（T > |X|）：黑洞内部，r < r_s，未来奇点在 r = 0（T² − X² = 1）处。
- **区域 III**（X < −|T|）：第二个外部——与区域 I 无因果联系的*平行宇宙*。
- **区域 IV**（T < −|X|）：白洞内部，r < r_s，过去奇点。

Regions III and IV are unphysical for realistic black holes (which form by gravitational collapse), but the Kruskal maximal extension shows the mathematical completeness of the Schwarzschild solution.

对于实际的黑洞（由引力坍缩形成），区域 III 和 IV 是非物理的，但克鲁斯卡尔极大延拓展示了史瓦西解的数学完备性。

**Demonstration — The Kerr Black Hole, Ergosphere, and Penrose Process.** The Kerr metric (Module 7.5) for a rotating black hole of mass M and spin parameter a = J/(Mc) has two key surfaces:

**演示——克尔黑洞、能层与彭罗斯过程。** 质量 M、自旋参数 a = J/(Mc) 的旋转黑洞的克尔度规（模块 7.5）有两个关键曲面：

- *Outer event horizon* at r_+ = GM/c² + √((GM/c²)² − a²): the boundary of no escape.
- *Ergosphere* (stationary limit surface) at r_erg = GM/c² + √((GM/c²)² − a² cos²θ): the surface inside which no observer can remain stationary (the metric component g_{tt} changes sign here, so ∂_t becomes spacelike).

- *外事件视界*：r_+ = GM/c² + √((GM/c²)² − a²)，无法逃脱的边界。
- *能层*（静止极限面）：r_erg = GM/c² + √((GM/c²)² − a² cos²θ)，在此面内没有观测者能保持静止（度规分量 g_{tt} 在此处变号，∂_t 变为类空矢量）。

The region between r_+ and r_erg is the *ergosphere*. In the ergosphere, the conserved energy E = −p_μ ξ^μ (where ξ^μ = (∂_t)^μ) can be *negative* for certain particle states, because ξ^μ is spacelike there (not a timelike Killing vector). The *Penrose process* exploits this (see Derivations B): a particle falls into the ergosphere, splits into two; one fragment has negative energy (absorbed by the hole, reducing its angular momentum), and the other escapes to infinity with *more* energy than the original particle. The maximum energy extractable is set by the irreducible mass:

r_+ 与 r_erg 之间的区域即*能层*。在能层中，守恒能量 E = −p_μ ξ^μ（ξ^μ = (∂_t)^μ）对某些粒子态可以为*负*，因为 ξ^μ 在那里是类空矢量（非类时基灵矢量）。*彭罗斯过程*利用了这一点（见推导 B）：粒子落入能层后分裂为两部分；一部分携带负能量被黑洞吸收（减少其角动量），另一部分以比原粒子*更多*的能量逃向无穷远。可提取能量的最大值由不可约质量决定：

  E_max / E_initial = a / (r_+ c²) × (ℓ_max for the absorbed fragment)

The maximum efficiency is η_max = 1 − 1/√2 ≈ 20.7% for a maximally rotating (extremal) Kerr black hole (a = GM/c²). The energy comes from the rotational kinetic energy of the hole; repeated Penrose processes (or the superradiance analog for waves) would spin the black hole down to a = 0.

对极端旋转（极值）克尔黑洞（a = GM/c²），最大效率为 η_max = 1 − 1/√2 ≈ 20.7%。能量来自黑洞的转动动能；反复进行彭罗斯过程（或波的超辐射类比）最终会使黑洞自旋降至 a = 0。

---

## 2. Singularity Theorems · 奇点定理

**Definition.** The *singularity theorems* of Penrose (1965) and Hawking–Penrose (1970) prove that, under physically reasonable conditions, spacetime must contain *incomplete causal geodesics* — the mathematical statement of a singularity. This is a theorem, not a conjecture: it shows that singularities are not an artifact of idealized symmetry (like the r = 0 point of Schwarzschild) but a generic feature of GR.

**定义。** 彭罗斯（1965 年）和霍金-彭罗斯（1970 年）的*奇点定理*证明，在物理上合理的条件下，时空必然包含*不完整的因果测地线*——奇点的数学表述。这是一个定理，而非猜想：它表明奇点不是理想化对称性的产物（如史瓦西解的 r = 0），而是广义相对论的普适特征。

**The ingredients:**

**定理的要素：**

**(1) Energy conditions.** The theorems require that matter focuses geodesics. The *null energy condition* (NEC) states R_{μν} k^μ k^ν ≥ 0 for all null vectors k^μ, which (via the Einstein equations) is equivalent to T_{μν} k^μ k^ν ≥ 0: the energy density seen by any null observer is non-negative. The *strong energy condition* (SEC) states R_{μν} u^μ u^ν ≥ 0 for all timelike u^μ (equivalent to (T_{μν} − ½T g_{μν}) u^μ u^ν ≥ 0). Both conditions hold for ordinary matter; they are violated by a cosmological constant (dark energy), which is why Λ > 0 allows an initially expanding universe to avoid a past singularity only in special cases.

**（1）能量条件。** 定理要求物质使测地线汇聚。*类光能量条件*（NEC）：对所有类光矢量 k^μ，R_{μν} k^μ k^ν ≥ 0，经爱因斯坦方程等价于 T_{μν} k^μ k^ν ≥ 0——任何类光观测者所见的能量密度非负。*强能量条件*（SEC）：对所有类时 u^μ，R_{μν} u^μ u^ν ≥ 0（等价于 (T_{μν} − ½T g_{μν}) u^μ u^ν ≥ 0）。普通物质满足这两个条件；宇宙学常数（暗能量）违反 SEC，这正是 Λ > 0 仅在特殊情况下允许初始膨胀宇宙避免过去奇点的原因。

**(2) Geodesic congruences and the Raychaudhuri equation.** A *congruence* is a family of geodesics filling a region of spacetime. For a timelike congruence with unit tangent u^μ, define the *expansion* θ = ∇_μ u^μ (the fractional rate of change of a volume element). The *Raychaudhuri equation* (see Derivations C) governs θ:

**（2）测地线汇聚与雷乔杜里方程。** *测地线族*是填充时空某区域的一族测地线。对单位切矢量为 u^μ 的类时测地线族，定义*膨胀率* θ = ∇_μ u^μ（体积元的分数变化率）。*雷乔杜里方程*（见推导 C）支配 θ：

  dθ/dτ = −θ²/3 − σ_{μν} σ^{μν} + ω_{μν} ω^{μν} − R_{μν} u^μ u^ν

where σ_{μν} is the shear (traceless symmetric part of ∇_ν u_μ) and ω_{μν} is the vorticity (antisymmetric part). Key implications:
- The −θ²/3 term means any converging congruence (θ < 0) accelerates toward a caustic (θ → −∞) — *focusing*.
- The −σ² term is always ≤ 0: shear enhances focusing.
- The +ω² term can oppose focusing, but ω_{μν} = 0 for hypersurface-orthogonal congruences (geodesics that are gradients of a function, e.g. in a spherically symmetric collapse).
- If the SEC holds, −R_{μν} u^μ u^ν ≤ 0: matter curves geodesics inward.

其中 σ_{μν} 为剪切（∇_ν u_μ 的无迹对称部分），ω_{μν} 为旋度（反对称部分）。关键含义：
- −θ²/3 项表示任何收缩的测地线族（θ < 0）加速趋向焦散面（θ → −∞）——*聚焦*。
- −σ² 项始终 ≤ 0：剪切增强聚焦。
- +ω² 项可抵抗聚焦，但对于超曲面正交测地线族（某函数的梯度，如球对称坍缩中），ω_{μν} = 0。
- 若 SEC 成立，则 −R_{μν} u^μ u^ν ≤ 0：物质使测地线向内弯曲。

**(3) Trapped surfaces.** A *trapped surface* is a compact, spacelike 2-surface on which both ingoing and outgoing null geodesics have negative expansion (θ < 0) — light is converging in both directions. For an ordinary sphere in flat space, outgoing light rays expand (θ > 0) and ingoing rays converge (θ < 0). A trapped surface signals that escape is impossible in both directions.

**（3）囚禁面。** *囚禁面*是紧致类空 2 维曲面，其上向内和向外的类光测地线都有负膨胀率（θ < 0）——光在两个方向都在汇聚。对平坦空间中的普通球面，向外的类光线膨胀（θ > 0），向内的汇聚（θ < 0）。囚禁面意味着两个方向都无法逃脱。

**Demonstration — The Penrose (1965) Singularity Theorem.** *If* (i) the NEC holds, (ii) a non-compact Cauchy surface exists (the spacetime is globally hyperbolic), and (iii) the spacetime contains a trapped surface, *then* the spacetime must contain a future-inextendible null geodesic — a singularity.

**演示——彭罗斯（1965 年）奇点定理。** *若*（i）NEC 成立，（ii）存在非紧致柯西超曲面（时空整体双曲），（iii）时空包含囚禁面，*则*时空必含面向未来不可延拓的类光测地线——奇点。

The proof uses the Raychaudhuri equation: once a null congruence has θ < 0 at some point, the NEC forces dθ/dτ ≤ −θ²/2 (null version), so θ → −∞ within affine time τ ≤ 2/(−θ₀). By global hyperbolicity, the boundary of the causal future J⁺(S) of the trapped surface S is compact. But if all null geodesics through S focus within finite affine time, that boundary must be compact — a contradiction with non-compactness, unless the geodesics are incomplete (a singularity).

证明利用雷乔杜里方程：一旦类光测地线族在某点有 θ < 0，NEC 迫使 dθ/dτ ≤ −θ²/2（类光版本），从而在仿射时间 τ ≤ 2/(−θ₀) 内 θ → −∞。由整体双曲性，囚禁面 S 的因果未来 J⁺(S) 的边界是紧致的。但若所有经过 S 的类光测地线在有限仿射时间内都聚焦，则该边界必须是紧致的——与非紧致性矛盾，除非测地线不完整（即奇点）。

**Demonstration — The Hawking–Penrose (1970) Theorem.** Extends Penrose's result to *timelike* geodesic incompleteness (relevant for cosmological singularities), requiring the SEC. Under the SEC plus the generic condition (every geodesic encounters some curvature) plus global hyperbolicity, the universe must contain a singularity — either in the future (if the universe starts collapsing) or in the past (the Big Bang). This proves that the Big Bang is not a coordinate artifact.

**演示——霍金-彭罗斯（1970 年）定理。** 将彭罗斯结果推广到*类时*测地线不完整（与宇宙学奇点相关），需要 SEC。在 SEC 加上一般性条件（每条测地线都遇到某种曲率）加整体双曲性的条件下，宇宙必然包含奇点——或在未来（若宇宙开始坍缩），或在过去（大爆炸）。这证明大爆炸不是坐标产物。

**Application — Cosmic Censorship Conjecture.** The singularity theorems prove singularities exist but say nothing about whether they are hidden behind event horizons. Penrose's *weak cosmic censorship conjecture* states that, for generic initial data, all singularities are hidden from distant observers (no *naked singularities*). The *strong* cosmic censorship conjecture states that the maximal Cauchy development of generic initial data is inextendible — no observer inside a black hole can see beyond the Cauchy horizon. Both remain unproven in full generality but are supported by extensive numerical evidence and perturbation theory.

**应用——宇宙审查猜想。** 奇点定理证明了奇点的存在，但对奇点是否隐藏于事件视界后面没有说明。彭罗斯的*弱宇宙审查猜想*指出，对一般初始数据，所有奇点对遥远观测者都是隐藏的（不存在*裸奇点*）。*强宇宙审查猜想*指出，一般初始数据的极大柯西发展是不可延拓的——黑洞内的观测者看不到柯西视界之外的内容。两个猜想在完整的一般性意义上均未被证明，但得到了大量数值证据和微扰理论的支持。

---

**Self-test (blank page)**

1. Define the event horizon and the apparent horizon. In which spacetimes do they coincide? Give an example of a dynamic spacetime where they differ.
2. State the Penrose singularity theorem: list its three hypotheses and sketch the key step in the proof using the Raychaudhuri equation.
3. Explain why the Kruskal coordinate transformation removes the coordinate singularity at r = 2GM/c². What is the physical singularity in the Kruskal diagram, and how is it represented?
4. Define the ergosphere of a Kerr black hole and describe the Penrose process. What is the maximum efficiency, and where does the extracted energy come from?
5. What is the strong energy condition? Give an example of a stress-energy tensor that satisfies it and one that violates it.

**自测（空白页）**

1. 定义事件视界和表观视界。在哪些时空中它们重合？给出一个动态时空中它们不同的例子。
2. 陈述彭罗斯奇点定理：列出其三个假设，并用雷乔杜里方程概述证明的关键步骤。
3. 解释克鲁斯卡尔坐标变换如何消除 r = 2GM/c² 处的坐标奇点。克鲁斯卡尔图中的物理奇点是什么，如何表示？
4. 定义克尔黑洞的能层并描述彭罗斯过程。最大效率是多少，提取的能量来自哪里？
5. 什么是强能量条件？各给出一个满足它和违反它的应力-能量张量的例子。

---

← Previous: [Module 7.7 — Tests of GR & Gravitational-Wave Astronomy](./module-7.7-tests-of-gr-and-gravitational-wave-astronomy.md) · [Phase 7 index](./README.md)

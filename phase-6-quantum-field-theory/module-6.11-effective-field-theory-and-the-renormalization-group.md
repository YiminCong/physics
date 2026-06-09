# Module 6.11 — Effective Field Theory & the Wilsonian Renormalization Group
**模块 6.11 — 有效场论与威尔逊重整化群**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.11-effective-field-theory-and-the-renormalization-group-derivations.md)

---

## 1. The Wilsonian Renormalization Group: Integrate Out, Rescale · 威尔逊重整化群：积掉、重标度

**Definition.** Module 6.6 introduced renormalization as the removal of UV divergences and defined the β-function and running couplings. The Wilsonian viewpoint reorganizes the same physics around a single physical operation: coarse-graining. Start from a path integral with a hard cutoff Λ on momenta, Z = ∫_{|k|<Λ} 𝒟φ e^{−S[φ]}. Split the field into high modes φ_H (Λ/b < |k| < Λ) and low modes φ_L (|k| < Λ/b), with b > 1. **Integrate out** the high modes: e^{−S'[φ_L]} = ∫ 𝒟φ_H e^{−S[φ_L+φ_H]}. This generates an effective action S'[φ_L] for the low modes, with a reduced cutoff Λ/b. Then **rescale** momenta k → bk and fields φ → ζ φ to restore the original cutoff Λ. The combined operation maps a theory with couplings {g_i} to a new theory {g_i′}: this is the **RG transformation** ℛ_b. Iterating it defines the **RG flow** in the space of couplings.

**定义。** 模块 6.6 将重整化引入为紫外发散的消除，并定义了 β 函数与跑动耦合。威尔逊观点围绕一个物理操作——粗粒化——重新组织同样的物理。从对动量带硬截断 Λ 的路径积分出发，Z = ∫_{|k|<Λ} 𝒟φ e^{−S[φ]}。将场分裂为高模 φ_H（Λ/b < |k| < Λ）与低模 φ_L（|k| < Λ/b），b > 1。**积掉**高模：e^{−S'[φ_L]} = ∫ 𝒟φ_H e^{−S[φ_L+φ_H]}。这为低模生成有效作用量 S'[φ_L]，截断降为 Λ/b。然后**重标度**动量 k → bk 与场 φ → ζ φ 以恢复原截断 Λ。这一组合操作将具有耦合 {g_i} 的理论映射为新理论 {g_i′}：这就是 **RG 变换** ℛ_b。迭代它在耦合空间中定义了 **RG 流**。

A **fixed point** g* satisfies g_i′ = g_i: the theory looks identical after coarse-graining, hence it is scale-invariant. The Gaussian (free) fixed point g* = 0 and interacting fixed points such as Wilson–Fisher (Module 6.6) are the organizing centers of the flow. The crucial conceptual gain over 6.6 is that the cutoff Λ is now physical — it is the scale below which the EFT is valid — rather than a regulator to be sent to infinity. Renormalizability becomes a statement about the IR behavior of trajectories, not about cancelling infinities.

**不动点** g* 满足 g_i′ = g_i：粗粒化后理论保持不变，因而是尺度不变的。高斯（自由）不动点 g* = 0 与相互作用不动点（如 Wilson–Fisher，模块 6.6）是流的组织中心。相比 6.6，关键的概念进展在于截断 Λ 现在是物理的——它是有效场论有效性的下界尺度——而非待趋于无穷的正规化参数。可重整性变成关于轨迹红外行为的陈述，而非关于消去无穷大的陈述。

**Demonstration.** Apply one RG step to scalar φ⁴ theory in d dimensions. Integrating out the high-momentum shell at one loop shifts the mass and quartic coupling: r → r + (corrections from the shell), u → u − (constant)·u²·(shell volume). After rescaling k → bk, the dimensionful parameters pick up factors of b set purely by dimensional analysis (r → b² r at tree level, the quadratic term being relevant), and the loop corrections add the nontrivial β-function pieces. Taking b = 1 + dℓ infinitesimally converts the discrete map into differential flow equations dg_i/dℓ = β_i({g}), recovering exactly the β-functions of 6.6 but now with a transparent geometric meaning: β_i is the velocity of the i-th coupling under coarse-graining, and −d/dℓ = −d/d(ln b) (see Derivation D).

**演示。** 对 d 维标量 φ⁴ 理论施加一步 RG。在单圈阶积掉高动量壳层使质量与四次耦合移动：r → r +（来自壳层的修正），u → u −（常数）·u²·（壳层体积）。重标度 k → bk 后，含量纲参数获得纯由量纲分析决定的 b 因子（树级时 r → b² r，二次项是相关的），圈修正则加入非平庸的 β 函数部分。取无穷小 b = 1 + dℓ 将离散映射转为微分流方程 dg_i/dℓ = β_i({g})，恰好复现 6.6 的 β 函数，但现在具有清晰的几何意义：β_i 是第 i 个耦合在粗粒化下的速度，且 −d/dℓ = −d/d(ln b)（见推导 D）。

**Application.** The Wilsonian picture explains *why* renormalization works. Low-energy observables are controlled by where trajectories end up in the IR, which is dominated by a fixed point and its few relevant directions. Microscopic details (the precise cutoff physics, the values of irrelevant couplings) are washed out by repeated coarse-graining. This is the modern justification for using simple Lagrangians: they are not fundamental, they are the IR-relevant remnants of whatever unknown physics sits at Λ. Wilson's 1971 papers and Kardar "Statistical Physics of Fields" Ch. 4–5 develop the momentum-shell RG in full; Peskin & Schroeder §12.1 gives the field-theory version.

**应用。** 威尔逊图像解释了重整化*为何*有效。低能可观测量由轨迹在红外的归宿控制，而后者由不动点及其少数相关方向主导。微观细节（精确的截断物理、无关耦合的取值）被反复粗粒化抹去。这是使用简单拉格朗日量的现代依据：它们并非基本的，而是位于 Λ 处的某种未知物理在红外的相关残留。Wilson 1971 年的论文与 Kardar 《Statistical Physics of Fields》第 4–5 章完整发展了动量壳层 RG；Peskin & Schroeder §12.1 给出场论版本。

---

## 2. Operator Scaling, Power Counting, and Relevant/Irrelevant Operators · 算符标度、幂次计数与相关/无关算符

**Definition.** Near the Gaussian fixed point the RG flow of each coupling is fixed by dimensional analysis. Write the action as S = ∫ d^d x [ (∂φ)²-type kinetic term + Σ_i g_i O_i ], where O_i is a local operator built from φ and its derivatives. Demanding the kinetic term ∫ d^d x (∂φ)² be invariant under k → bk fixes the field rescaling, giving the scalar field mass dimension [φ] = (d−2)/2. An operator O of total mass dimension Δ_O then carries a coupling of dimension [g] = d − Δ_O, and under one RG step the dimensionless coupling scales as

**定义。** 在高斯不动点附近，每个耦合的 RG 流由量纲分析决定。将作用量写为 S = ∫ d^d x [ (∂φ)² 型动能项 + Σ_i g_i O_i ]，其中 O_i 是由 φ 及其导数构成的局域算符。要求动能项 ∫ d^d x (∂φ)² 在 k → bk 下不变，确定场的重标度，给出标量场质量量纲 [φ] = (d−2)/2。质量量纲为 Δ_O 的算符 O 携带量纲为 [g] = d − Δ_O 的耦合，一步 RG 下无量纲耦合按下式标度

  **g → b^{d − Δ_O} g.**

This single formula classifies every operator. **Relevant** (d − Δ_O > 0): the coupling grows under coarse-graining, dominating the IR. **Marginal** (d − Δ_O = 0): unchanged at tree level; loop corrections decide. **Irrelevant** (d − Δ_O < 0): the coupling shrinks, dying out in the IR.

这一个公式分类了每个算符。**相关**（d − Δ_O > 0）：耦合在粗粒化下增长，主导红外。**边缘**（d − Δ_O = 0）：树级不变；由圈修正决定。**无关**（d − Δ_O < 0）：耦合收缩，在红外消亡。

**Demonstration.** With [φ] = (d−2)/2, the operator φⁿ has dimension Δ = n(d−2)/2, so its coupling g_n has dimension d − n(d−2)/2. In d = 4: [φ] = 1, so φ² (mass term) has Δ = 2 → relevant (dimension +2, the most relevant); φ⁴ has Δ = 4 → marginal (dimension 0); φ⁶ has Δ = 6 → irrelevant (dimension −2). The derivative operator (∂φ)² is marginal by construction. Thus in d = 4 there are **only finitely many** relevant and marginal scalar operators: φ², φ⁴, and (∂φ)². Every other operator — φ⁶, (∂φ)²φ², φ⁸, … — is irrelevant and suppressed in the IR. This is precisely the statement of **renormalizability as IR insensitivity**: a renormalizable theory keeps only the relevant and marginal operators, and the infinitely many irrelevant operators generated at the cutoff scale flow to zero, leaving a finite-parameter low-energy theory.

**演示。** 由 [φ] = (d−2)/2，算符 φⁿ 量纲为 Δ = n(d−2)/2，故其耦合 g_n 量纲为 d − n(d−2)/2。在 d = 4 中：[φ] = 1，故 φ²（质量项）Δ = 2 → 相关（量纲 +2，最相关）；φ⁴ 量纲 Δ = 4 → 边缘（量纲 0）；φ⁶ 量纲 Δ = 6 → 无关（量纲 −2）。导数算符 (∂φ)² 按构造为边缘。因此在 d = 4 中**只有有限个**相关与边缘标量算符：φ²、φ⁴ 与 (∂φ)²。其余每个算符——φ⁶、(∂φ)²φ²、φ⁸……——都是无关的，在红外被压制。这正是**可重整性即红外不敏感性**的陈述：可重整理论只保留相关与边缘算符，截断尺度生成的无穷多无关算符流向零，留下有限参数的低能理论。

**Application.** Predictivity follows immediately: because only finitely many relevant/marginal couplings survive into the IR, measuring that finite set fixes all low-energy predictions, independent of the unknown UV completion. This reframes the renormalizability requirement of 6.6 not as a fundamental law but as a low-energy accident — non-renormalizable (irrelevant) operators are present but suppressed by powers of E/Λ. It also explains *naturalness* puzzles: relevant couplings (the mass term, the cosmological constant) are sensitive to the cutoff and require fine-tuning, while marginal and irrelevant couplings are not. Polchinski's "Effective field theory and the Fermi surface" and Peskin & Schroeder §12.1 give the operator classification; the connection to critical phenomena appears in Module 2.3.

**应用。** 可预言性随之而来：由于只有有限个相关/边缘耦合存留到红外，测量这有限集合就确定了所有低能预言，与未知的紫外完备化无关。这将 6.6 的可重整性要求重新诠释为：它不是基本定律，而是低能巧合——不可重整（无关）算符存在但被 E/Λ 的幂次压制。这也解释了*自然性*难题：相关耦合（质量项、宇宙学常数）对截断敏感、需要微调，而边缘与无关耦合则不然。Polchinski 的 "Effective field theory and the Fermi surface" 与 Peskin & Schroeder §12.1 给出算符分类；与临界现象的联系见模块 2.3。

---

## 3. Effective Field Theory: Power Counting, Decoupling, and Fermi Theory · 有效场论：幂次计数、退耦与费米理论

**Definition.** An effective field theory (EFT) is the systematic low-energy description obtained by integrating out all physics above a scale Λ. Its Lagrangian is organized as an expansion in E/Λ,

**定义。** 有效场论（EFT）是积掉尺度 Λ 之上所有物理而得到的系统低能描述。其拉格朗日量按 E/Λ 展开组织，

  ℒ = Σ_i (c_i / Λ^{Δ_i − d}) O_i,

where O_i are all local operators consistent with the symmetries, Δ_i their mass dimensions, and c_i dimensionless **Wilson coefficients** of order one. Operators with Δ_i > d are higher-dimension (irrelevant); their effects on a process at energy E are suppressed by (E/Λ)^{Δ_i − d}. The **Appelquist–Carazzone decoupling theorem** guarantees that heavy fields of mass M ∼ Λ leave behind only such suppressed contact operators (plus renormalizations of the light couplings): heavy physics decouples, with corrections vanishing as powers of E/M. This is why we can do physics at all without knowing the theory at every scale.

其中 O_i 是与对称性相容的所有局域算符，Δ_i 为其质量量纲，c_i 为量级为一的无量纲 **威尔逊系数**。Δ_i > d 的算符是高维（无关）的；它们对能量 E 处过程的影响被 (E/Λ)^{Δ_i − d} 压制。**Appelquist–Carazzone 退耦定理**保证质量 M ∼ Λ 的重场只留下这类被压制的接触算符（加上轻耦合的重整化）：重物理退耦，修正按 E/M 的幂次消失。这正是我们无需知道每个尺度的理论就能做物理的原因。

**Demonstration.** The archetype is **Fermi's theory of the weak interaction** as the EFT of the electroweak Standard Model below the W mass. In the full theory a charged-current process such as muon decay proceeds by exchange of a W boson with propagator ∝ 1/(q² − m_W²). At low momentum transfer, q² ≪ m_W², expand

**演示。** 原型是**费米弱相互作用理论**，作为电弱标准模型在 W 质量以下的 EFT。在完整理论中，诸如 μ 衰变的带电流过程通过交换 W 玻色子进行，传播子 ∝ 1/(q² − m_W²)。在低动量转移 q² ≪ m_W² 时展开

  1/(q² − m_W²) = −(1/m_W²)·1/(1 − q²/m_W²) → −1/m_W²  (leading term).

The W propagator collapses to a constant, turning the exchange into a **four-fermion contact interaction** (J^μ J_μ)/m_W². Matching the coefficient gives the Fermi constant

W 传播子塌缩为常数，将交换变为**四费米接触相互作用** (J^μ J_μ)/m_W²。匹配系数给出费米常数

  **G_F/√2 = g²/(8 m_W²),  i.e. G_F ∝ 1/m_W².**

G_F is an irrelevant coupling of mass dimension −2 (four fermions, each of dimension 3/2, give Δ = 6 > 4 = d), suppressed by 1/Λ² with Λ = m_W. The neglected q²/m_W² terms are the higher-dimension corrections of the EFT expansion.

G_F 是质量量纲为 −2 的无关耦合（四个费米子各量纲 3/2，给出 Δ = 6 > 4 = d），被 1/Λ²（Λ = m_W）压制。被略去的 q²/m_W² 项是 EFT 展开的高维修正。

**Application.** EFT is the working language of modern physics. Fermi theory predicted weak decay rates for decades before the W was discovered; its breakdown at √s ∼ m_W (where the (E/Λ)^n expansion fails and amplitudes violate unitarity) correctly signalled new physics — the W boson itself (Module 8.4). The same logic gives chiral perturbation theory (pions as the EFT of QCD below the chiral scale), heavy-quark EFT, NRQED for atomic bound states, and the gravitational EFT used for post-Newtonian binary-inspiral waveforms. In every case one writes all symmetry-allowed operators, organizes by E/Λ, and fits the Wilson coefficients. Burgess "Introduction to Effective Field Theory" and Manohar's lectures are the standard references; the SM-as-UV-completion logic anticipates the gauge-coupling unification of Modules 8.3/8.5.

**应用。** EFT 是现代物理的工作语言。费米理论在 W 被发现前几十年就预言了弱衰变率；它在 √s ∼ m_W 处的失效（此处 (E/Λ)^n 展开失败、振幅破坏幺正性）正确地预示了新物理——W 玻色子本身（模块 8.4）。同样的逻辑给出手征微扰论（π 介子作为 QCD 在手征尺度以下的 EFT）、重夸克 EFT、用于原子束缚态的 NRQED，以及用于后牛顿双星旋进波形的引力 EFT。每种情形都写出所有对称性允许的算符、按 E/Λ 组织、拟合威尔逊系数。Burgess 《Introduction to Effective Field Theory》与 Manohar 的讲义是标准参考；标准模型作为紫外完备化的逻辑预示了模块 8.3/8.5 的规范耦合统一。

---

## Self-test (blank page) · 自测（空白页）

1. In the Wilsonian RG, describe the two operations (integrate out, rescale) that make up one RG step, and state what condition defines a fixed point.
2. Derive the mass dimension of a scalar field in d spacetime dimensions, then classify φ², φ⁴, and φ⁶ as relevant, marginal, or irrelevant in d = 4. Explain how "only finitely many relevant operators" leads to predictivity.
3. Starting from the W-boson propagator 1/(q² − m_W²), show how integrating out the W at low momentum produces Fermi's four-fermion interaction and the relation G_F ∝ 1/m_W². Why is G_F an irrelevant coupling?
4. Explain the Appelquist–Carazzone decoupling theorem and why higher-dimension operators are suppressed by powers of E/Λ. How did the breakdown of Fermi theory predict the W mass?

**自测（空白页）**

1. 在威尔逊 RG 中，描述构成一步 RG 的两个操作（积掉、重标度），并陈述定义不动点的条件。
2. 推导 d 维时空中标量场的质量量纲，然后在 d = 4 中将 φ²、φ⁴、φ⁶ 分类为相关、边缘或无关。解释"只有有限个相关算符"如何导致可预言性。
3. 从 W 玻色子传播子 1/(q² − m_W²) 出发，说明在低动量下积掉 W 如何产生费米四费米相互作用以及关系 G_F ∝ 1/m_W²。为何 G_F 是无关耦合？
4. 解释 Appelquist–Carazzone 退耦定理，以及为何高维算符被 E/Λ 的幂次压制。费米理论的失效如何预言了 W 质量？

---

← Previous: [Module 6.10 — Spontaneous Symmetry Breaking & Goldstone's Theorem](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md) · [Phase 6 index](./README.md) · Next: [Module 6.12 — Finite-Temperature Field Theory](./module-6.12-finite-temperature-field-theory.md) →

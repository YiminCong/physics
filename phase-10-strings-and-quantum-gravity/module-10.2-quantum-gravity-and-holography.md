# Module 10.2 — Quantum Gravity & Holography
**模块 10.2 — 量子引力与全息原理**

> **Phase 10 — [Strings & Quantum Gravity](./README.md)** · Format: Definition → Demonstration → Application
> **第 10 阶段 — 弦论与量子引力** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-10.2-derivations.md)

---

## 1. Why General Relativity and Quantum Mechanics Clash · 广义相对论与量子力学为何冲突

**Definition.** General relativity (GR) is a **classical field theory** of the spacetime metric g_μν. To quantize it in the standard way — treating metric fluctuations h_μν = g_μν − η_μν as a quantum field (the **graviton**) on a flat background — one expands the Einstein–Hilbert action in powers of h_μν and computes Feynman diagrams. The fundamental obstruction is that **gravity is perturbatively non-renormalizable**: the gravitational coupling κ = √(8πG/c⁴) has mass dimension [κ] = −1 in 4d (in natural units ℏ = c = 1). Each additional loop in a graviton Feynman diagram brings a factor of κ², introducing a new divergence that requires a new counterterm. At loop order L, counterterms of dimension 2+2L in the Riemann tensor appear; infinitely many counterterms are needed, destroying all predictive power (see Module 6.6 for the renormalization framework).

**定义。** 广义相对论（GR）是关于时空度规 g_μν 的**经典场论**。用标准方法将其量子化——将度规涨落 h_μν = g_μν − η_μν 视为平坦背景上的量子场（**引力子**）——需要将 Einstein–Hilbert 作用量按 h_μν 展开并计算费曼图。根本障碍在于**引力在微扰论中不可重整**：引力耦合常数 κ = √(8πG/c⁴) 在 4 维中的质量量纲为 [κ] = −1（自然单位 ℏ = c = 1）。引力子费曼图每增加一个圈就带来一个 κ² 因子，引入需要新抵消项的新发散。在 L 圈阶，出现 Riemann 张量中量纲为 2+2L 的抵消项；需要无穷多个抵消项，破坏了一切预测能力（重整化框架见模块 6.6）。

**Demonstration.** By dimensional analysis: Newton's constant G has dimensions [G] = [length²] (natural units), so the dimensionless expansion parameter for graviton loops at energy E is (Gℏ/c³)(E/ℏc)² = G E²/(ℏc⁵) = (E/E_Planck)². At energies E ≪ E_Planck ~ 10¹⁹ GeV, gravity is weak and GR works perfectly as an **effective field theory**. But near E ~ E_Planck the loop expansion breaks down completely: new physics — quantum gravity — must take over.

**演示。** 量纲分析：牛顿常数 G 具有量纲 [G] = [长度²]（自然单位），因此引力子圈在能量 E 处的无量纲展开参数为 (Gℏ/c³)(E/ℏc)² = G E²/(ℏc⁵) = (E/E_Planck)²。当 E ≪ E_Planck ∼ 10¹⁹ GeV 时，引力很弱，GR 作为**有效场论**完美成立。但在 E ∼ E_Planck 附近，圈展开完全失效：必须引入新物理——量子引力。

**Application.** Non-renormalizability does not mean GR is wrong; it means GR is **incomplete at the Planck scale**. Precision measurements of gravitational wave sources, the cosmic microwave background, and black-hole shadows all probe regimes where E ≪ E_Planck and the effective-field-theory description is excellent. The problem is purely theoretical: no consistent, predictive, UV-complete quantum theory of gravity is known from the conventional approach. This motivates both string theory (Module 10.1) and loop quantum gravity (§5), which take radically different routes.

**应用。** 不可重整性并不意味着 GR 错误；它意味着 GR 在普朗克尺度处**不完备**。引力波源、宇宙微波背景和黑洞阴影的精密测量，均探测 E ≪ E_Planck 的区域，有效场论描述在此优异。问题纯属理论：从传统方法出发，尚无已知的自洽、可预测的紫外完备量子引力理论。这推动了弦论（模块 10.1）和圈量子引力（第 5 节）的发展，二者采取了截然不同的路径。

---

## 2. The Planck Scale · 普朗克尺度

**Definition.** The **Planck units** are the unique combination of the fundamental constants G, ℏ, and c that form quantities with dimensions of length, mass, time, and temperature. They set the scale where quantum gravitational effects become O(1):

  ℓ_P = √(ℏG/c³) ≈ 1.616 × 10⁻³⁵ m  (Planck length)
  m_P = √(ℏc/G)  ≈ 2.176 × 10⁻⁸ kg  (Planck mass)
  t_P = √(ℏG/c⁵) ≈ 5.391 × 10⁻⁴⁴ s  (Planck time)
  T_P = m_P c²/k_B ≈ 1.417 × 10³² K  (Planck temperature)

**定义。** **普朗克单位**是由基本常数 G、ℏ 和 c 唯一构成的具有长度、质量、时间和温度量纲的量。它们设定了量子引力效应变为 O(1) 的尺度：

  ℓ_P = √(ℏG/c³) ≈ 1.616 × 10⁻³⁵ m  （普朗克长度）
  m_P = √(ℏc/G)  ≈ 2.176 × 10⁻⁸ kg  （普朗克质量）
  t_P = √(ℏG/c⁵) ≈ 5.391 × 10⁻⁴⁴ s  （普朗克时间）
  T_P = m_P c²/k_B ≈ 1.417 × 10³² K  （普朗克温度）

**Demonstration.** The derivation is pure dimensional analysis (proved in Module 10.2 Derivations §A): one writes ℓ_P = G^a ℏ^b c^d and solves for (a,b,d) from dimensional consistency. Remarkably, the Planck mass m_P c² ~ 10¹⁹ GeV is far beyond any foreseeable accelerator (the LHC reaches ~ 10⁴ GeV). The Planck length ℓ_P ~ 10⁻²⁰ × (proton radius) is the putative granularity of spacetime.

**演示。** 推导是纯量纲分析（在模块 10.2 推导第 §A 节中证明）：令 ℓ_P = G^a ℏ^b c^d，由量纲一致性求解 (a,b,d)。值得注意的是，普朗克质量 m_P c² ∼ 10¹⁹ GeV 远超任何可预见的加速器（LHC 达到约 10⁴ GeV）。普朗克长度 ℓ_P ∼ 10⁻²⁰ × （质子半径），是时空颗粒度的推测尺度。

**Application.** The Planck units appear naturally throughout quantum gravity. In black-hole thermodynamics (§3), entropy is measured in units of ℓ_P². In string theory, the string length ℓ_s ~ ℓ_P (though the precise ratio depends on the compactification and the string coupling). The Planck temperature T_P is the scale above which quantum-gravitational fluctuations of the thermal bath become significant — presumably the temperature at which the Big Bang singularity must be resolved by quantum gravity.

**应用。** 普朗克单位在整个量子引力中自然出现。在黑洞热力学（第 3 节）中，熵以 ℓ_P² 为单位度量。在弦论中，弦长 ℓ_s ∼ ℓ_P（精确比值取决于紧化和弦耦合）。普朗克温度 T_P 是热浴的量子引力涨落变得显著的尺度——可能是大爆炸奇点必须由量子引力消解的温度。

---

## 3. Black-Hole Thermodynamics · 黑洞热力学

**Definition.** The **laws of black-hole mechanics** mirror the laws of thermodynamics. For a Kerr–Newman black hole with mass M, charge Q, and angular momentum J:

- **Zeroth law:** The surface gravity κ is constant over the event horizon — analogous to thermal equilibrium (uniform temperature).
- **First law:** dM c² = (κ/8πG) dA + Ω dJ + Φ dQ — energy conservation with work terms.
- **Second law (Hawking):** The total horizon area A never decreases (classically).
- **Third law:** κ → 0 cannot be reached in a finite number of steps.

The **Bekenstein–Hawking entropy** identifies the black hole's thermodynamic entropy with its horizon area:

  **S = k_B A / (4 ℓ_P²) = k_B c³ A / (4 G ℏ)**.

**定义。** **黑洞力学定律**与热力学定律相对应。对质量 M、电荷 Q、角动量 J 的 Kerr–Newman 黑洞：

- **第零定律**：表面引力 κ 在视界上处处恒定——类比热平衡（均匀温度）。
- **第一定律**：dM c² = (κ/8πG) dA + Ω dJ + Φ dQ——带功项的能量守恒。
- **第二定律（霍金）**：总视界面积 A 经典上从不减少。
- **第三定律**：κ → 0 不能在有限步内达到。

**Bekenstein–Hawking 熵**将黑洞的热力学熵与其视界面积等同：

  **S = k_B A / (4 ℓ_P²) = k_B c³ A / (4 G ℏ)**。

**Demonstration.** For a **Schwarzschild black hole** of mass M, the horizon area is A = 4π r_s² = 16π G² M² / c⁴. The surface gravity is κ = c⁴ / (4GM). The **Hawking temperature** (derived via quantum field theory in curved spacetime, or more elegantly via Euclidean time periodicity — see Derivations §C) is:

  **T_H = ℏ κ / (2π c k_B) = ℏ c³ / (8π G M k_B)**.

This is an astonishing result: a black hole radiates thermally at temperature T_H, which is **inversely proportional to its mass**. A solar-mass black hole has T_H ~ 6 × 10⁻⁸ K — utterly negligible. A microscopic black hole of mass ~ 10¹² kg has T_H ~ 10¹¹ K and evaporates explosively. The entropy is S = k_B A / 4ℓ_P², giving for the Schwarzschild black hole:

  S = 4π k_B G M² / (ℏ c).

This grows as M², which is **enormously larger** than the ~ 10⁵⁷ k_B entropy of a star of the same mass — the black hole is the maximum-entropy object of a given size.

**演示。** 对质量 M 的**史瓦西黑洞**，视界面积为 A = 4π r_s² = 16π G² M² / c⁴，表面引力为 κ = c⁴ / (4GM)。**霍金温度**（通过弯曲时空中的量子场论导出，或更优雅地通过欧氏时间周期性——见推导第 §C 节）为：

  **T_H = ℏ κ / (2π c k_B) = ℏ c³ / (8π G M k_B)**。

这是惊人的结果：黑洞以温度 T_H 热辐射，该温度**与质量成反比**。太阳质量黑洞的 T_H ∼ 6 × 10⁻⁸ K——完全可忽略。质量约 10¹² kg 的微型黑洞的 T_H ∼ 10¹¹ K，并爆炸性蒸发。熵为 S = k_B A / 4ℓ_P²，对史瓦西黑洞给出：

  S = 4π k_B G M² / (ℏ c)。

它随 M² 增长，比同质量恒星的约 10⁵⁷ k_B 熵**大得多**——黑洞是给定尺寸中具有最大熵的对象。

**Application.** Black-hole thermodynamics raises the **information paradox**: if a black hole radiates purely thermally (Hawking's original calculation), the outgoing radiation carries no information about the in-fallen matter. When the black hole evaporates completely, the initial pure quantum state appears to have evolved to a mixed state — violating unitary evolution, the cornerstone of quantum mechanics. Whether information is truly lost (Hawking's original position, later retracted), encoded in subtle correlations of the Hawking radiation, or stored in remnants, is one of the deepest open problems in physics. The holographic principle (§4) and AdS/CFT offer a resolution: the dual CFT is unitary, so information must be preserved.

**应用。** 黑洞热力学提出了**信息悖论**：若黑洞纯粹热辐射（霍金原始计算），出射辐射不携带任何关于落入物质的信息。当黑洞完全蒸发后，初始纯量子态似乎演化为混合态——违反量子力学的基石单一性演化。信息是否真正丢失（霍金的原始立场，后来撤回）、编码在霍金辐射的微妙关联中，还是储存在残余物中，是物理学中最深刻的未解问题之一。全息原理（第 4 节）和 AdS/CFT 提供了解答：对偶 CFT 是单一的，因此信息必须守恒。

---

## 4. The Holographic Principle and AdS/CFT · 全息原理与 AdS/CFT

**Definition.** The **holographic principle** (t'Hooft 1993, Susskind 1994) states that the complete description of a physical system in a volume V is contained in the degrees of freedom on the **boundary** ∂V, with at most one degree of freedom per Planck area ℓ_P². Equivalently, the maximum entropy of a region bounded by area A is the Bekenstein–Hawking entropy S_max = k_B A / (4ℓ_P²). This is **radical**: it implies that the world is, in a precise sense, two-dimensional at its most fundamental level — a three-dimensional bulk has no more information than its two-dimensional boundary.

**定义。** **全息原理**（t'Hooft 1993，Susskind 1994）指出，体积 V 内物理系统的完整描述包含在**边界** ∂V 上的自由度中，每个普朗克面积 ℓ_P² 最多对应一个自由度。等价地，面积为 A 的区域的最大熵为 Bekenstein–Hawking 熵 S_max = k_B A / (4ℓ_P²)。这是**根本性的**：它意味着世界在最基本层次上，在精确意义下是二维的——三维体不比其二维边界包含更多信息。

**Demonstration.** The strongest realization of the holographic principle is the **AdS/CFT correspondence** (Maldacena 1997): a string theory on **Anti-de Sitter space** (AdS_{d+1}) is **exactly dual** to a conformal field theory (CFT_d) on the d-dimensional boundary. The canonical example is:

  **Type IIB string theory on AdS₅ × S⁵  ↔  N=4 super-Yang–Mills theory (SU(N)) in 4d**

in the limit of large N and large 't Hooft coupling λ = g_{YM}² N. In this limit the string-theory side reduces to **classical supergravity in AdS₅**, making computations tractable. The dictionary reads:

- Fields φ in the AdS bulk ↔ operators O in the CFT, with the boundary value φ_0 = lim_{z→0} φ(z, x) acting as a **source** for O in the generating functional.
- The **conformal dimension** Δ of O is related to the mass of φ: m²ℓ²_{AdS} = Δ(Δ − d).
- The **partition functions** agree: Z_{string}[φ_0] = ⟨exp(∫ φ_0 O)⟩_{CFT}.

**演示。** 全息原理最强的实现是 **AdS/CFT 对应**（Maldacena，1997 年）：**反德西特空间**（AdS_{d+1}）上的弦论与 d 维边界上的共形场论（CFT_d）**精确对偶**。典型例子是：

  **AdS₅ × S⁵ 上的 IIB 型弦论  ↔  4 维 N=4 超杨–Mills 理论（SU(N)）**

在大 N 和大 't Hooft 耦合 λ = g_{YM}² N 的极限下。此极限下弦论一侧化为 **AdS₅ 中的经典超引力**，使计算易于处理。字典为：

- AdS 体中的场 φ ↔ CFT 中的算符 O，边界值 φ_0 = lim_{z→0} φ(z, x) 在生成泛函中充当 O 的**源**。
- O 的**共形维数** Δ 与 φ 的质量相关：m²ℓ²_{AdS} = Δ(Δ − d)。
- **配分函数**相等：Z_{string}[φ_0] = ⟨exp(∫ φ_0 O)⟩_{CFT}。

**Application.** AdS/CFT is a **non-perturbative** duality: it works even when both the field theory and the gravitational theory are strongly coupled, and it relates strong-coupling physics on one side to weak-coupling physics on the other. Applications span:

1. **Quark–gluon plasma:** N=4 SYM at strong coupling ↔ AdS₅ black hole; transport coefficients (viscosity/entropy ratio η/s = ℏ/4πk_B) match RHIC data remarkably well.
2. **Condensed matter:** holographic superconductors, strange-metal transport, non-Fermi liquids.
3. **Quantum information:** the Ryu–Takayanagi formula S_entanglement = Area(minimal surface)/4Gℏ identifies entanglement entropy with a bulk minimal surface — a deep unification of geometry and quantum information.
4. **Information paradox:** in AdS/CFT the boundary CFT is manifestly unitary, implying the bulk (including black-hole evaporation) must be unitary too; recent progress on the "island formula" makes this precise.

**应用。** AdS/CFT 是一个**非微扰**对偶：即使场论和引力理论都处于强耦合区，它也成立，并将一侧的强耦合物理与另一侧的弱耦合物理相联系。应用涵盖：

1. **夸克–胶子等离子体**：强耦合 N=4 SYM ↔ AdS₅ 黑洞；输运系数（粘度/熵比 η/s = ℏ/4πk_B）与 RHIC 数据吻合极好。
2. **凝聚态**：全息超导体、奇异金属输运、非费米液体。
3. **量子信息**：Ryu–Takayanagi 公式 S_纠缠 = Area(最小曲面)/4Gℏ 将纠缠熵与体中的最小曲面等同——几何与量子信息的深刻统一。
4. **信息悖论**：在 AdS/CFT 中边界 CFT 显然是单一的，暗示体（包括黑洞蒸发）也必须是单一的；关于"岛公式"的近期进展使这一点精确化。

---

## 5. Loop Quantum Gravity: An Alternative Program · 圈量子引力：另一条路

**Definition.** **Loop quantum gravity (LQG)** is a non-perturbative, background-independent quantization of general relativity that does not invoke strings or extra dimensions. The starting point is the **Ashtekar variables** (1986): rewriting GR in terms of a connection A^i_a (analogous to a Yang–Mills connection for SU(2)) and a densitized triad Ẽ^a_i (analogous to an electric field). The Hilbert space of quantum geometry is spanned by **spin-network states**, which assign an SU(2) representation (spin j_e) to each edge e and an intertwiner to each node.

**定义。** **圈量子引力（LQG）**是广义相对论的非微扰、背景无关量子化，不引入弦或额外维度。出发点是 **Ashtekar 变量**（1986 年）：用联络 A^i_a（类比 SU(2) 杨–Mills 联络）和密化标架 Ẽ^a_i（类比电场）重写 GR。量子几何的 Hilbert 空间由**自旋网络态**张成，每条边 e 赋予 SU(2) 表示（自旋 j_e），每个节点赋予一个互扭子。

**Demonstration.** The key prediction of LQG is that **area and volume are quantized**: the area operator Â has eigenvalues:

  A = 8πγ ℓ_P² Σ_e √(j_e(j_e + 1)),

where γ (the Barbero–Immirzi parameter) is a free parameter of the theory. The minimum non-zero area eigenvalue is ~ 8πγ√3/2 · ℓ_P² ≈ ℓ_P² for γ ~ (ln 3)/(π√3). This **discreteness of spacetime** is a prediction without analogue in string theory (where spacetime is continuous at the string scale). LQG naturally reproduces the Bekenstein–Hawking entropy formula (with the Barbero–Immirzi parameter fixed by this requirement) and is free of the UV divergences that plague perturbative quantum gravity, because there is no continuum of arbitrarily short wavelengths.

**演示。** LQG 的关键预言是**面积和体积是量子化的**：面积算符 Â 的本征值为：

  A = 8πγ ℓ_P² Σ_e √(j_e(j_e + 1))，

其中 γ（Barbero–Immirzi 参数）是理论的自由参数。最小非零面积本征值约为 8πγ√3/2 · ℓ_P² ≈ ℓ_P²（当 γ ∼ (ln 3)/(π√3) 时）。这种**时空离散性**是弦论中没有类比的预言（弦论中时空在弦尺度仍连续）。LQG 自然地重现 Bekenstein–Hawking 熵公式（此要求固定 Barbero–Immirzi 参数），且不受困扰微扰量子引力的紫外发散的影响，因为不存在任意短波长的连续统。

**Application.** LQG and string theory represent the two dominant research programs in quantum gravity and differ fundamentally in their starting assumptions. LQG preserves background independence (a core feature of GR) but does not currently reproduce the Standard Model or provide a natural low-energy limit with GR plus matter. String theory naturally contains the Standard Model (through compactification and D-branes) and gravity but requires extra dimensions and (in most formulations) a fixed background. Neither theory has yet made a confirmed experimental prediction beyond the domain of effective field theory. The deep question — whether quantum gravity is unique, and whether it can be tested — remains open.

**应用。** LQG 和弦论代表量子引力研究的两大主流，在基本假设上根本不同。LQG 保留了背景无关性（GR 的核心特征），但目前尚未重现标准模型，也未提供包含 GR 加物质的自然低能极限。弦论通过紧化和 D 膜自然包含标准模型和引力，但需要额外维度并且（在大多数表述中）需要固定背景。两种理论目前都尚未做出超越有效场论范围的经证实的实验预言。量子引力是否唯一、是否可被检验，这个深刻问题仍悬而未决。

---

**Self-test (blank page)**

1. Explain in one paragraph why perturbative quantum gravity is non-renormalizable. What is the role of the Planck scale?
2. State the Bekenstein–Hawking entropy formula and the Hawking temperature formula for a Schwarzschild black hole. What happens to the temperature as the black hole evaporates?
3. What is the holographic principle? How does black-hole thermodynamics motivate it?
4. State the AdS/CFT correspondence (be specific about which theories are dual). Give one application to a system other than pure gravity.
5. Compare loop quantum gravity and string theory as approaches to quantum gravity: what does each take as its starting point, and what is a key prediction or feature of each?

**自测（空白页）**

1. 用一段话解释为何微扰量子引力不可重整。普朗克尺度的作用是什么？
2. 陈述史瓦西黑洞的 Bekenstein–Hawking 熵公式和霍金温度公式。黑洞蒸发时温度如何变化？
3. 全息原理是什么？黑洞热力学如何为其提供动机？
4. 陈述 AdS/CFT 对应（具体说明哪些理论对偶）。给出一个纯引力以外的系统的应用。
5. 比较圈量子引力与弦论作为量子引力方法的异同：各自的出发点是什么，各自的关键预言或特征是什么？

---

← Previous: [Module 10.1 — String Theory & Superstrings](./module-10.1-string-theory-and-superstrings.md) · [Phase 10 index](./README.md)

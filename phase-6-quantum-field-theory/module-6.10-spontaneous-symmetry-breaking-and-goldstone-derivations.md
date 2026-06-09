# Derivations — Module 6.10: Spontaneous Symmetry Breaking & Goldstone's Theorem
# 推导 — 模块 6.10：自发对称性破缺与戈德斯通定理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.10](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.10](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. SSB in a Real Scalar Theory: Vacuum and the Massive Field · 实标量理论中的自发对称性破缺：真空与有质量场

**Claim.** For ℒ = ½(∂φ)² − V(φ) with V(φ) = −½μ²φ² + ¼λφ⁴ (μ² > 0, λ > 0), the Z₂-symmetric point φ = 0 is a maximum, the vacuum is ⟨φ⟩ = v = ±√(μ²/λ), and the fluctuation about it has mass m_η² = 2μ² = 2λv².

**Step 1 — Stationary points.** A constant field minimizes the energy when it minimizes V (the gradient term ½(∂φ)² vanishes for constant φ). Compute V′(φ) = −μ²φ + λφ³ = φ(λφ² − μ²). Setting V′(φ) = 0 gives φ = 0 or φ² = μ²/λ, i.e. φ = ±v with v ≡ √(μ²/λ).

**Step 2 — Classify by curvature.** Compute V″(φ) = −μ² + 3λφ². At the symmetric point V″(0) = −μ² < 0, so φ = 0 is a **maximum**. At φ = ±v, V″(±v) = −μ² + 3λ(μ²/λ) = −μ² + 3μ² = 2μ² > 0, so φ = ±v are **minima**. The vacuum is therefore ⟨φ⟩ = v = √(μ²/λ) (choosing the + branch). Because the two minima are exchanged by φ → −φ, selecting one breaks Z₂: ℒ is symmetric, the vacuum is not.

**Step 3 — Expand and read off the mass.** Write φ = v + η with η the fluctuation. Then V(v + η) = V(v) + V′(v)η + ½V″(v)η² + …. Since V′(v) = 0 (minimum) and V″(v) = 2μ², the quadratic term is ½(2μ²)η² = ½ m_η² η² with

  m_η² = V″(v) = 2μ² = 2λv².

The negative mass-squared of the symmetric phase has become a positive mass once expanded about the true vacuum. The Z₂ broken here is discrete, so no massless mode arises. ∎

**Claim.** 对 ℒ = ½(∂φ)² − V(φ)，V(φ) = −½μ²φ² + ¼λφ⁴（μ² > 0，λ > 0），Z₂ 对称点 φ = 0 是极大值，真空为 ⟨φ⟩ = v = ±√(μ²/λ)，围绕它的涨落质量为 m_η² = 2μ² = 2λv²。

**第 1 步 — 稳定点。** 常数场极小化能量当且仅当它极小化 V（梯度项 ½(∂φ)² 对常数 φ 为零）。计算 V′(φ) = −μ²φ + λφ³ = φ(λφ² − μ²)。令 V′(φ) = 0 给出 φ = 0 或 φ² = μ²/λ，即 φ = ±v，v ≡ √(μ²/λ)。

**第 2 步 — 用曲率分类。** 计算 V″(φ) = −μ² + 3λφ²。对称点处 V″(0) = −μ² < 0，故 φ = 0 是**极大值**。在 φ = ±v 处，V″(±v) = −μ² + 3λ(μ²/λ) = −μ² + 3μ² = 2μ² > 0，故 φ = ±v 是**极小值**。真空因而为 ⟨φ⟩ = v = √(μ²/λ)（取 + 分支）。由于两个极小值被 φ → −φ 交换，选取其一即破缺 Z₂：ℒ 对称，真空不对称。

**第 3 步 — 展开并读出质量。** 写 φ = v + η，η 为涨落。则 V(v + η) = V(v) + V′(v)η + ½V″(v)η² + …。因 V′(v) = 0（极小值）且 V″(v) = 2μ²，二次项为 ½(2μ²)η² = ½ m_η² η²，其中

  m_η² = V″(v) = 2μ² = 2λv²。

对称相的负质量平方一旦围绕真实真空展开就变成正质量。这里破缺的 Z₂ 是离散的，故不出现无质量模。∎

---

## B. The Goldstone Boson from a Broken U(1) · 破缺 U(1) 给出的戈德斯通玻色子

**Claim.** For a complex scalar with ℒ = |∂φ|² − V, V = −μ²|φ|² + λ|φ|⁴ and global U(1) φ → e^{iα}φ, the vacuum ⟨φ⟩ = v/√2 with v = √(μ²/λ) breaks U(1); the radial mode h is massive with m_h² = 2μ² = 2λv², and the angular mode is exactly massless — the Goldstone boson.

**Step 1 — The circle of minima.** Write φ = ρ e^{iθ}/√2 so |φ|² = ½ρ². Then V = −½μ²ρ² + ¼λρ⁴, which is exactly the Section-A potential in the radial variable ρ. Minimizing in ρ gives ρ = v = √(μ²/λ), independent of θ. The minimum is therefore the entire circle |φ| = v/√2; V is *flat* along θ. The vacuum picks one point, say θ = 0, ⟨φ⟩ = v/√2, breaking the U(1).

**Step 2 — Parametrize the fluctuations.** Expand about the chosen vacuum in radial and angular fluctuations, φ = (v + h) e^{iθ/v}/√2 (the 1/v makes θ canonically normalized). To quadratic order this is equivalent to the linear parametrization φ = (v + h + iπ)/√2, where h is the radial (Higgs-like) field and π the angular (Goldstone) field.

**Step 3 — The potential to quadratic order.** With this parametrization |φ|² = ½[(v + h)² + π²] = ½[v² + 2vh + h² + π²]. Insert into V = −½μ²(2|φ|²) + ¼λ(2|φ|²)² and use μ² = λv²:

  V = −½μ²(v² + 2vh + h² + π²) + ¼λ(v² + 2vh + h² + π²)².

Expanding and collecting quadratic terms, the linear terms cancel (v is the minimum), and one finds the quadratic potential

  V₂ = ½(2λv²) h² + 0·π² = ½ m_h² h²,  m_h² = 2λv² = 2μ².

The h field is massive; the π field has **no** quadratic term, so m_π² = 0.

**Step 4 — Why π is massless: the flat direction.** The masslessness is geometry, not algebra. Adding a constant phase α to φ is exactly the U(1) transformation; it moves the field along the bottom of the "Mexican-hat" valley, where V is constant by Step 1. The angular fluctuation π is precisely a local displacement along this flat valley, so the restoring force — the curvature of V transverse to the valley floor along the angular direction — is zero. Hence m_π² = ∂²V/∂π²|_vac = 0 identically. The radial direction h climbs the walls (curvature 2λv²); the angular direction π is the flat valley floor (curvature 0). The massless π is the **Goldstone boson** of the broken U(1). ∎

**Claim.** 对复标量 ℒ = |∂φ|² − V，V = −μ²|φ|² + λ|φ|⁴，整体 U(1) φ → e^{iα}φ，真空 ⟨φ⟩ = v/√2（v = √(μ²/λ)）破缺 U(1)；径向模 h 有质量 m_h² = 2μ² = 2λv²，角向模严格无质量——戈德斯通玻色子。

**第 1 步 — 极小值圆。** 写 φ = ρ e^{iθ}/√2，则 |φ|² = ½ρ²。于是 V = −½μ²ρ² + ¼λρ⁴，正是 A 节的势在径向变量 ρ 中的形式。对 ρ 极小化给出 ρ = v = √(μ²/λ)，与 θ 无关。极小值因而是整个圆 |φ| = v/√2；V 沿 θ *平坦*。真空选取一点，设 θ = 0，⟨φ⟩ = v/√2，破缺 U(1)。

**第 2 步 — 参数化涨落。** 围绕选定真空以径向和角向涨落展开，φ = (v + h) e^{iθ/v}/√2（1/v 使 θ 正则归一化）。到二次阶，这等价于线性参数化 φ = (v + h + iπ)/√2，其中 h 是径向（类希格斯）场，π 是角向（戈德斯通）场。

**第 3 步 — 势到二次阶。** 用此参数化 |φ|² = ½[(v + h)² + π²] = ½[v² + 2vh + h² + π²]。代入 V = −½μ²(2|φ|²) + ¼λ(2|φ|²)² 并用 μ² = λv²：

  V = −½μ²(v² + 2vh + h² + π²) + ¼λ(v² + 2vh + h² + π²)²。

展开并收集二次项，线性项相消（v 为极小值），得到二次势

  V₂ = ½(2λv²) h² + 0·π² = ½ m_h² h²，m_h² = 2λv² = 2μ²。

h 场有质量；π 场**没有**二次项，故 m_π² = 0。

**第 4 步 — π 为何无质量：平坦方向。** 无质量性源于几何而非代数。给 φ 加上常数相位 α 正是 U(1) 变换；它使场沿"墨西哥帽"山谷底部移动，那里由第 1 步 V 为常数。角向涨落 π 恰是沿此平坦山谷的局部位移，故回复力——V 沿角向横越谷底的曲率——为零。因此 m_π² = ∂²V/∂π²|_真空 = 0 恒成立。径向方向 h 攀爬壁（曲率 2λv²）；角向方向 π 是平坦谷底（曲率 0）。无质量的 π 就是破缺 U(1) 的**戈德斯通玻色子**。∎

---

## C. Goldstone's Theorem in General & the Counting dim(G) − dim(H) · 一般的戈德斯通定理与计数 dim(G) − dim(H)

**Claim.** For every spontaneously broken continuous global symmetry generator (one with Q|0⟩ ≠ 0) of a Lorentz-invariant theory, there exists a massless particle. The number of such Goldstone bosons equals dim(G) − dim(H), where G is the symmetry group and H the unbroken subgroup that leaves the vacuum invariant.

**Step 1 — Broken charge and the order parameter.** A continuous symmetry has a conserved Noether current J^μ with ∂_μJ^μ = 0 and charge Q = ∫d³x J⁰. The symmetry is *spontaneously broken* when Q does not annihilate the vacuum: Q|0⟩ ≠ 0. Equivalently there exists a field operator Φ whose variation has nonzero vacuum expectation, ⟨0|[Q, Φ]|0⟩ = c ≠ 0; this c is the order parameter (e.g. c ∝ v in Sections A–B).

**Step 2 — Insert a complete set of states.** Write the order parameter using the current. Because J⁰ creates excitations from the vacuum, insert a complete set of momentum eigenstates |n⟩ between J⁰ and Φ in c = ⟨0|[∫d³x J⁰(x), Φ(0)]|0⟩. Translation invariance J^μ(x) = e^{iP·x}J^μ(0)e^{−iP·x} fixes the x-dependence; carrying out ∫d³x sets the spatial momentum of the intermediate states to zero. The nonvanishing of c then requires at least one intermediate state |n⟩ with ⟨0|J⁰(0)|n⟩ ≠ 0 and ⟨n|Φ(0)|0⟩ ≠ 0.

**Step 3 — The matrix element and current conservation.** By Lorentz covariance the matrix element of the broken current between the vacuum and the relevant one-particle state |π(p)⟩ must take the form

  ⟨0|J^μ(x)|π(p)⟩ = i f p^μ e^{−ip·x},

with a nonzero decay constant f (nonzero precisely because c ≠ 0 in Step 2 — the state is created by the broken current). Now impose current conservation:

  0 = ∂_μ⟨0|J^μ(x)|π(p)⟩ = ∂_μ(i f p^μ e^{−ip·x}) = f p_μ p^μ e^{−ip·x} = f p² e^{−ip·x}.

Since f ≠ 0 and the exponential is nonzero, this forces

  p² = 0.

A relativistic one-particle state with p² = 0 has zero rest mass: m² = p² = 0. Hence |π(p)⟩ is a **massless particle** — the Goldstone boson. ∎ (Step 1)

**Step 4 — The counting dim(G) − dim(H).** Each broken generator T_a (a = 1, …, dim G) gives a current J_a^μ and a candidate order-parameter relation ⟨0|[Q_a, Φ]|0⟩. Split the generators: those of the unbroken subgroup H annihilate the vacuum (Q_a|0⟩ = 0 for T_a ∈ H, giving f = 0 and no Goldstone), while the remaining dim(G) − dim(H) *broken* generators each satisfy Q_a|0⟩ ≠ 0 and, by Steps 1–3, each produce an independent massless boson. The broken generators span the coset G/H — the tangent space to the vacuum manifold (the "flat valley" of Section B) — so the number of flat directions equals dim(G/H) = dim(G) − dim(H). Therefore

  **# Goldstone bosons = dim(G) − dim(H).**

Examples: U(1) → {1} has dim G − dim H = 1 − 0 = 1 (one Goldstone, Section B); O(N) → O(N−1) has ½N(N−1) − ½(N−1)(N−2) = N − 1 Goldstones; chiral SU(2)_L × SU(2)_R → SU(2)_V has 3 + 3 − 3 = 3 Goldstones (the three pions, Module 8.7). ∎

**Claim.** 对洛伦兹不变理论中每个被自发破缺的连续整体对称性生成元（满足 Q|0⟩ ≠ 0），存在一个无质量粒子。此类戈德斯通玻色子的数目等于 dim(G) − dim(H)，其中 G 是对称群，H 是使真空不变的未破缺子群。

**第 1 步 — 破缺荷与序参量。** 连续对称性有守恒诺特流 J^μ，满足 ∂_μJ^μ = 0，荷 Q = ∫d³x J⁰。当 Q 不湮灭真空时对称性*自发破缺*：Q|0⟩ ≠ 0。等价地，存在场算符 Φ，其变分有非零真空期望，⟨0|[Q, Φ]|0⟩ = c ≠ 0；此 c 即序参量（如 A–B 节中 c ∝ v）。

**第 2 步 — 插入完备态。** 用流表示序参量。由于 J⁰ 从真空产生激发，在 c = ⟨0|[∫d³x J⁰(x), Φ(0)]|0⟩ 中于 J⁰ 与 Φ 之间插入完备动量本征态 |n⟩。平移不变性 J^μ(x) = e^{iP·x}J^μ(0)e^{−iP·x} 固定 x 依赖；执行 ∫d³x 使中间态的空间动量为零。c 不为零便要求至少一个中间态 |n⟩ 满足 ⟨0|J⁰(0)|n⟩ ≠ 0 且 ⟨n|Φ(0)|0⟩ ≠ 0。

**第 3 步 — 矩阵元与流守恒。** 由洛伦兹协变性，被破缺流在真空与相关单粒子态 |π(p)⟩ 之间的矩阵元必取形式

  ⟨0|J^μ(x)|π(p)⟩ = i f p^μ e^{−ip·x}，

衰变常数 f ≠ 0（非零恰因第 2 步中 c ≠ 0——该态由被破缺流产生）。现施加流守恒：

  0 = ∂_μ⟨0|J^μ(x)|π(p)⟩ = ∂_μ(i f p^μ e^{−ip·x}) = f p_μ p^μ e^{−ip·x} = f p² e^{−ip·x}。

由于 f ≠ 0 且指数因子非零，这强制

  p² = 0。

p² = 0 的相对论性单粒子态静止质量为零：m² = p² = 0。故 |π(p)⟩ 是**无质量粒子**——戈德斯通玻色子。∎（第 1 步）

**第 4 步 — 计数 dim(G) − dim(H)。** 每个破缺生成元 T_a（a = 1, …, dim G）给出流 J_a^μ 和候选序参量关系 ⟨0|[Q_a, Φ]|0⟩。将生成元分类：未破缺子群 H 的生成元湮灭真空（T_a ∈ H 时 Q_a|0⟩ = 0，给出 f = 0，无戈德斯通），而其余 dim(G) − dim(H) 个*破缺*生成元各满足 Q_a|0⟩ ≠ 0，由第 1–3 步各产生一个独立的无质量玻色子。破缺生成元张成陪集 G/H——真空流形（B 节"平坦山谷"）的切空间——故平坦方向数等于 dim(G/H) = dim(G) − dim(H)。因此

  **戈德斯通玻色子数 = dim(G) − dim(H)。**

例子：U(1) → {1} 有 dim G − dim H = 1 − 0 = 1（一个戈德斯通，B 节）；O(N) → O(N−1) 有 ½N(N−1) − ½(N−1)(N−2) = N − 1 个戈德斯通；手征 SU(2)_L × SU(2)_R → SU(2)_V 有 3 + 3 − 3 = 3 个戈德斯通（三个 π 介子，模块 8.7）。∎

---

## D. The Mermin–Wagner Theorem: No Breaking in Low Dimensions · Mermin–Wagner 定理：低维无破缺

**Claim.** A continuous symmetry cannot be spontaneously broken in d ≤ 2 spatial dimensions at finite temperature (or d ≤ 1 in the quantum/zero-temperature case): the would-be Goldstone fluctuations are infrared-divergent and destroy long-range order.

**Step 1 — The Goldstone is the soft mode.** Suppose, for contradiction, the symmetry breaks and a Goldstone field π exists. By Section B–C it is massless, so at low energy its effective action is purely the gradient term, S = ½ρ_s ∫d^dx (∇π)², where ρ_s is the stiffness (spin stiffness / superfluid density). The propagator of a massless field is ⟨π(k)π(−k)⟩ = 1/(ρ_s k²).

**Step 2 — IR power counting of the fluctuation.** The mean-square fluctuation of the order-parameter phase at a point is the propagator integrated over all momenta (with an IR cutoff L⁻¹ from finite system size and a UV cutoff Λ):

  ⟨π²⟩ = ∫ d^dk/(2π)^d · 1/(ρ_s k²)  ∝ ∫_{1/L}^{Λ} dk · k^{d−1}/k² = ∫_{1/L} dk · k^{d−3}.

Count the IR behavior as the lower limit 1/L → 0:
 • d = 3: ∫dk k⁰ converges at small k → ⟨π²⟩ finite → order survives.
 • d = 2: ∫dk k⁻¹ = ln(LΛ) → **logarithmically divergent** as L → ∞.
 • d = 1: ∫dk k⁻² ∝ L → **linearly divergent** as L → ∞.

**Step 3 — Divergence destroys order.** The order parameter is ⟨e^{iπ}⟩ ∼ e^{−½⟨π²⟩} (Gaussian fluctuations). In d ≤ 2 the divergent ⟨π²⟩ → ∞ drives e^{−½⟨π²⟩} → 0: the average order parameter vanishes in the thermodynamic limit. The infrared-divergent Goldstone fluctuations wash out the long-range order, so no symmetry breaking can occur. This is the **Mermin–Wagner (–Hohenberg–Coleman) theorem**. (Discrete symmetries are exempt — they have no Goldstone soft mode — which is why the 2D Ising model orders but the 2D Heisenberg model does not. The marginal d = 2 case admits the Berezinskii–Kosterlitz–Thouless transition with quasi-long-range order instead of true order.) ∎

**Claim.** 连续对称性在 d ≤ 2 空间维有限温度下（或量子/零温情形下 d ≤ 1）不能自发破缺：本应的戈德斯通涨落红外发散，破坏长程序。

**第 1 步 — 戈德斯通是软模。** 反证：设对称性破缺且存在戈德斯通场 π。由 B–C 节它无质量，故低能下其有效作用量纯为梯度项，S = ½ρ_s ∫d^dx (∇π)²，ρ_s 为劲度（自旋劲度/超流密度）。无质量场的传播子为 ⟨π(k)π(−k)⟩ = 1/(ρ_s k²)。

**第 2 步 — 涨落的红外幂计数。** 序参量相位在一点的均方涨落是传播子对全动量的积分（红外截断 L⁻¹ 来自有限系统尺寸，紫外截断 Λ）：

  ⟨π²⟩ = ∫ d^dk/(2π)^d · 1/(ρ_s k²)  ∝ ∫_{1/L}^{Λ} dk · k^{d−1}/k² = ∫_{1/L} dk · k^{d−3}。

考察下限 1/L → 0 时的红外行为：
 • d = 3：∫dk k⁰ 在小 k 收敛 → ⟨π²⟩ 有限 → 序保留。
 • d = 2：∫dk k⁻¹ = ln(LΛ) → 随 L → ∞ **对数发散**。
 • d = 1：∫dk k⁻² ∝ L → 随 L → ∞ **线性发散**。

**第 3 步 — 发散破坏序。** 序参量为 ⟨e^{iπ}⟩ ∼ e^{−½⟨π²⟩}（高斯涨落）。在 d ≤ 2 中发散的 ⟨π²⟩ → ∞ 使 e^{−½⟨π²⟩} → 0：热力学极限下平均序参量消失。红外发散的戈德斯通涨落抹去长程序，故不能发生对称性破缺。这就是 **Mermin–Wagner（–Hohenberg–Coleman）定理**。（离散对称性除外——它们无戈德斯通软模——这正是二维伊辛模型有序而二维海森堡模型无序的原因。边缘的 d = 2 情形允许 Berezinskii–Kosterlitz–Thouless 相变，呈准长程序而非真长程序。）∎

---

## E. Contrast with Gauge Theories: the Goldstone Is Eaten · 与规范理论的对比：戈德斯通被吞噬

**Claim.** When the spontaneously broken symmetry is *gauged* (local) rather than global, no physical massless Goldstone boson appears: the Goldstone degree of freedom becomes the longitudinal polarization of a gauge boson, which thereby acquires a mass. This is the Higgs mechanism.

**Step 1 — Gauge the U(1).** Promote the global U(1) of Section B to a local symmetry φ → e^{iα(x)}φ by introducing a gauge field A_μ with covariant derivative D_μφ = (∂_μ − ieA_μ)φ and A_μ → A_μ + (1/e)∂_μα. The Lagrangian is ℒ = −¼F_μνF^μν + |D_μφ|² − V(φ) with the same Mexican-hat V. The vacuum is still ⟨φ⟩ = v/√2.

**Step 2 — Counting the degrees of freedom.** Before breaking: a massless gauge field A_μ has 2 physical polarizations, and the complex scalar φ has 2 real components (h and the would-be Goldstone π) — total 4. The π is the flat-direction mode of Section B.

**Step 3 — The Goldstone is eaten.** Expand the kinetic term |D_μφ|² about the vacuum. The cross term contains, from D_μφ ⊃ (∂_μ − ieA_μ)(v/√2), a piece ∝ e v A_μ ∂^μπ — a kinetic mixing between A_μ and the Goldstone π. Use the local gauge freedom to choose the **unitary gauge**: pick α(x) to rotate away the phase of φ, i.e. set π → 0 everywhere. The Goldstone field is gauged away; it does not appear as an independent physical state. The remaining |D_μφ|² expanded with φ = (v + h)/√2 gives a mass term for the gauge field,

  |D_μφ|² ⊃ ½ e²v² A_μA^μ  ⟹  m_A² = e²v².

The gauge boson is now **massive**.

**Step 4 — The bookkeeping balances.** After breaking: a massive vector has 3 physical polarizations (2 transverse + 1 longitudinal), and the real scalar h remains (1) — total 4, matching Step 2. The one degree of freedom that was the massless Goldstone π has become the *longitudinal* polarization of the now-massive gauge boson: the gauge field "ate" the Goldstone. Hence in the gauged (Higgs) case there is **no physical massless Goldstone particle**, in sharp contrast to the global case (Sections B–C) where the Goldstone is a genuine massless physical state. The full non-abelian treatment, giving masses to the W and Z, is Module 8.4. ∎

**Claim.** 当被自发破缺的对称性是*规范*（局域）而非整体的时，不出现物理的无质量戈德斯通玻色子：戈德斯通自由度成为规范玻色子的纵向极化，规范玻色子因而获得质量。这就是希格斯机制。

**第 1 步 — 规范化 U(1)。** 将 B 节的整体 U(1) 提升为局域对称性 φ → e^{iα(x)}φ，引入规范场 A_μ，协变导数 D_μφ = (∂_μ − ieA_μ)φ，A_μ → A_μ + (1/e)∂_μα。拉格朗日量为 ℒ = −¼F_μνF^μν + |D_μφ|² − V(φ)，V 仍为墨西哥帽形。真空仍为 ⟨φ⟩ = v/√2。

**第 2 步 — 自由度计数。** 破缺前：无质量规范场 A_μ 有 2 个物理极化，复标量 φ 有 2 个实分量（h 与本应的戈德斯通 π）——共 4 个。π 是 B 节的平坦方向模。

**第 3 步 — 戈德斯通被吞噬。** 围绕真空展开动能项 |D_μφ|²。交叉项含有来自 D_μφ ⊃ (∂_μ − ieA_μ)(v/√2) 的一项 ∝ e v A_μ ∂^μπ——A_μ 与戈德斯通 π 之间的动能混合。用局域规范自由选取**幺正规范**：取 α(x) 旋转掉 φ 的相位，即处处令 π → 0。戈德斯通场被规范掉，不作为独立物理态出现。剩余的 |D_μφ|² 以 φ = (v + h)/√2 展开给出规范场的质量项，

  |D_μφ|² ⊃ ½ e²v² A_μA^μ  ⟹  m_A² = e²v²。

规范玻色子现在**有质量**。

**第 4 步 — 计数平衡。** 破缺后：有质量矢量有 3 个物理极化（2 横向 + 1 纵向），实标量 h 保留（1）——共 4 个，与第 2 步相符。曾是无质量戈德斯通 π 的那个自由度已成为如今有质量规范玻色子的*纵向*极化：规范场"吃掉"了戈德斯通。故在规范（希格斯）情形中**不存在物理的无质量戈德斯通粒子**，与整体情形（B–C 节）戈德斯通为真正无质量物理态形成鲜明对比。给 W 与 Z 赋予质量的完整非阿贝尔处理见模块 8.4。∎

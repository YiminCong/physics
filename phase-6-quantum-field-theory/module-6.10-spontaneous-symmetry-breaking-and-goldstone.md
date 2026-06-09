# Module 6.10 — Spontaneous Symmetry Breaking & Goldstone's Theorem
**模块 6.10 — 自发对称性破缺与戈德斯通定理**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.10-spontaneous-symmetry-breaking-and-goldstone-derivations.md)

---

## 1. Spontaneous Symmetry Breaking and the Vacuum · 自发对称性破缺与真空

**Definition.** A symmetry is *spontaneously broken* when the Lagrangian (or Hamiltonian) is invariant under a symmetry group G but the ground state — the vacuum — is not. The dynamics respect the symmetry; the chosen ground state does not. The diagnostic is the *order parameter*: a field whose vacuum expectation value ⟨φ⟩ would be forced to vanish by the symmetry, but which the dynamics drive to a nonzero value. Take a real scalar with ℒ = ½(∂φ)² − V(φ) and the "wrong-sign mass" potential V(φ) = −½μ²φ² + ¼λφ⁴ with μ² > 0, λ > 0. This ℒ is invariant under the discrete reflection Z₂: φ → −φ. The symmetric point φ = 0 is a *local maximum* of V (since V″(0) = −μ² < 0); the minima sit at ⟨φ⟩ = v = ±√(μ²/λ). The system must pick one of the two degenerate minima, and that choice breaks Z₂: the ground state is not symmetric even though ℒ is. This is the order parameter ⟨φ⟩ ≠ 0 of Landau theory (Module 2.3), now realized in a relativistic field theory.

**定义。** 当拉格朗日量（或哈密顿量）在对称群 G 下不变，但基态——真空——不在其下不变时，称对称性被*自发破缺*。动力学尊重对称性；被选中的基态却不。判据是*序参量*：一个本应被对称性强制为零的真空期望值 ⟨φ⟩，却被动力学驱动到非零值。取实标量 ℒ = ½(∂φ)² − V(φ)，势取"错号质量"形式 V(φ) = −½μ²φ² + ¼λφ⁴，其中 μ² > 0，λ > 0。该 ℒ 在离散反射 Z₂：φ → −φ 下不变。对称点 φ = 0 是 V 的*局部极大值*（因 V″(0) = −μ² < 0）；极小值位于 ⟨φ⟩ = v = ±√(μ²/λ)。系统必须从两个简并极小值中选一个，而这一选择破缺了 Z₂：尽管 ℒ 对称，基态却不对称。这正是朗道理论（模块 2.3）的序参量 ⟨φ⟩ ≠ 0，如今在相对论性场论中实现。

**Demonstration.** Minimize V: the stationarity condition V′(φ) = −μ²φ + λφ³ = φ(−μ² + λφ²) = 0 has roots φ = 0 and φ = ±√(μ²/λ) ≡ ±v. The curvature V″(φ) = −μ² + 3λφ² is negative at φ = 0 (a maximum) and positive at φ = v (a minimum). Expand the field about a chosen vacuum, φ = v + η, where η is the physical fluctuation. Substituting and collecting the quadratic term gives a *positive* mass: the η field has m_η² = V″(v) = −μ² + 3λv² = 2μ² = 2λv². The "tachyonic" −μ² of the symmetric phase has turned into a healthy positive mass once we expand about the true vacuum. There is no massless mode here because the broken symmetry Z₂ is *discrete*; a flat direction (and hence a massless particle) requires a *continuous* symmetry — the subject of Section 2.

**演示。** 将 V 极小化：稳定性条件 V′(φ) = −μ²φ + λφ³ = φ(−μ² + λφ²) = 0 有根 φ = 0 和 φ = ±√(μ²/λ) ≡ ±v。曲率 V″(φ) = −μ² + 3λφ² 在 φ = 0 处为负（极大值），在 φ = v 处为正（极小值）。围绕选定真空展开场，φ = v + η，其中 η 是物理涨落。代入并收集二次项给出*正*质量：η 场具有 m_η² = V″(v) = −μ² + 3λv² = 2μ² = 2λv²。对称相中"快子性"的 −μ² 一旦围绕真实真空展开就变成了健康的正质量。这里没有无质量模式，因为被破缺的对称性 Z₂ 是*离散*的；平坦方向（因而无质量粒子）需要*连续*对称性——这是第 2 节的主题。

**Application.** Spontaneous symmetry breaking is the organizing principle behind nearly every phase transition in physics. A ferromagnet below its Curie temperature picks a magnetization direction, breaking the rotational symmetry of the spin Hamiltonian (Module 4.6); a superconductor breaks the U(1) phase symmetry of the electromagnetic field (Module 5.3); the QCD vacuum breaks chiral symmetry, generating the bulk of the proton mass (Module 8.7); the Higgs field breaks electroweak SU(2)×U(1), giving masses to the W and Z (Module 8.4). The shape of V here — a symmetric double well in one dimension, a "Mexican hat" in two — is precisely the Landau–Ginzburg free energy of Module 2.3, with −μ² playing the role of (T − T_c) below the transition. Coleman's *Aspects of Symmetry* Ch. 5 and Peskin & Schroeder Ch. 11 give the field-theoretic treatment.

**应用。** 自发对称性破缺是物理学中几乎每一个相变背后的组织原则。居里温度以下的铁磁体选定一个磁化方向，破缺自旋哈密顿量的旋转对称性（模块 4.6）；超导体破缺电磁场的 U(1) 相位对称性（模块 5.3）；QCD 真空破缺手征对称性，产生质子质量的大部分（模块 8.7）；希格斯场破缺电弱 SU(2)×U(1)，赋予 W 与 Z 质量（模块 8.4）。这里 V 的形状——一维中的对称双阱、二维中的"墨西哥帽"——正是模块 2.3 的朗道–金兹堡自由能，其中 −μ² 在相变以下扮演 (T − T_c) 的角色。Coleman 的 *Aspects of Symmetry* 第 5 章和 Peskin & Schroeder 第 11 章给出场论处理。

---

## 2. Goldstone's Theorem · 戈德斯通定理

**Definition.** When a *continuous* global symmetry is spontaneously broken, **Goldstone's theorem** guarantees a massless particle — a *Goldstone boson* — for every broken generator. The cleanest model is a complex scalar φ with a global U(1) symmetry φ → e^{iα}φ and ℒ = |∂φ|² − V, V = −μ²|φ|² + λ|φ|⁴ (μ² > 0). The potential is minimized on the whole circle |φ| = v/√2 with v = √(μ²/λ); the vacuum picks one point on the circle, ⟨φ⟩ = v/√2, breaking U(1). Write the field in terms of its radial and angular fluctuations, φ = (v + h)e^{iθ/v}/√2 (equivalently φ = (v + h + iπ)/√2 to lowest order). The radial mode h climbs the walls of the "Mexican hat" — it is massive — while the angular mode θ moves *along* the flat valley at the bottom, costing no potential energy: it is exactly massless. That massless θ (or π) is the Goldstone boson. The general counting is **# Goldstone bosons = dim(G) − dim(H)**, where G is the symmetry group of ℒ and H ⊂ G is the unbroken subgroup that still leaves the vacuum invariant.

**定义。** 当*连续*整体对称性被自发破缺时，**戈德斯通定理**保证每个被破缺的生成元对应一个无质量粒子——*戈德斯通玻色子*。最简洁的模型是带整体 U(1) 对称性 φ → e^{iα}φ 的复标量 φ，ℒ = |∂φ|² − V，V = −μ²|φ|² + λ|φ|⁴（μ² > 0）。势在整个圆 |φ| = v/√2 上极小，v = √(μ²/λ)；真空选取圆上一点 ⟨φ⟩ = v/√2，破缺 U(1)。将场用其径向与角向涨落表示，φ = (v + h)e^{iθ/v}/√2（最低阶等价于 φ = (v + h + iπ)/√2）。径向模 h 沿"墨西哥帽"的壁攀爬——它有质量——而角向模 θ 沿底部平坦山谷*运动*，不消耗势能：它严格无质量。那个无质量的 θ（或 π）就是戈德斯通玻色子。一般计数为 **戈德斯通玻色子数 = dim(G) − dim(H)**，其中 G 是 ℒ 的对称群，H ⊂ G 是仍使真空不变的未破缺子群。

**Demonstration.** Substitute φ = (v + h + iπ)/√2 into V and expand: the radial fluctuation acquires m_h² = 2μ² = 2λv² (same massive "Higgs-like" mode as the η of Section 1), while the angular fluctuation π has *no* quadratic term — m_π² = 0 — because V is exactly constant along the angular direction. This flatness is not an accident: it is enforced by the symmetry. The model-independent proof (Section C of the derivations) uses current algebra: a spontaneously broken continuous symmetry has a Noether current J^μ with ∂_μJ^μ = 0 whose charge fails to annihilate the vacuum, Q|0⟩ ≠ 0. The matrix element of the broken current between the vacuum and a one-particle state is nonzero, ⟨0|J^μ(x)|π(p)⟩ = i f p^μ e^{−ip·x} with decay constant f ≠ 0; current conservation ∂_μJ^μ = 0 then forces p²·f = 0, so p² = 0 — the state |π(p)⟩ is exactly massless. One such massless boson appears for each broken generator, giving the counting dim(G) − dim(H).

**演示。** 将 φ = (v + h + iπ)/√2 代入 V 并展开：径向涨落获得 m_h² = 2μ² = 2λv²（与第 1 节的 η 相同的有质量"类希格斯"模），而角向涨落 π *没有*二次项——m_π² = 0——因为 V 沿角向严格为常数。这种平坦性并非偶然：它由对称性强制。与模型无关的证明（推导 C 节）使用流代数：自发破缺的连续对称性有一个满足 ∂_μJ^μ = 0 的诺特流 J^μ，其荷不湮灭真空，Q|0⟩ ≠ 0。被破缺流在真空与单粒子态之间的矩阵元非零，⟨0|J^μ(x)|π(p)⟩ = i f p^μ e^{−ip·x}，衰变常数 f ≠ 0；流守恒 ∂_μJ^μ = 0 随即强制 p²·f = 0，故 p² = 0——态 |π(p)⟩ 严格无质量。每个被破缺生成元对应一个这样的无质量玻色子，给出计数 dim(G) − dim(H)。

**Application.** Goldstone bosons appear wherever a continuous symmetry breaks. The pions are the (pseudo-)Goldstone bosons of spontaneously broken chiral SU(2)×SU(2) → SU(2) in QCD — light but not exactly massless because the quark masses break chiral symmetry explicitly (Module 8.7). Magnons (spin waves) are the Goldstone modes of the spin-rotation symmetry broken by a ferromagnet or antiferromagnet (Module 4.6); phonons are the Goldstones of broken translational symmetry in a crystal. The theorem has two important caveats: in low dimensions the would-be Goldstone modes fluctuate so violently that they *prevent* symmetry breaking altogether (the Mermin–Wagner theorem, Section D of the derivations), and when the broken symmetry is *gauged* rather than global, the Goldstone boson is eaten by the gauge field and there is no physical massless particle — the Higgs mechanism (Section E; fully derived in Module 8.4).

**应用。** 戈德斯通玻色子出现在任何连续对称性破缺之处。π 介子是 QCD 中自发破缺手征 SU(2)×SU(2) → SU(2) 的（赝）戈德斯通玻色子——轻但非严格无质量，因为夸克质量显式破缺手征对称性（模块 8.7）。磁振子（自旋波）是铁磁体或反铁磁体破缺的自旋旋转对称性的戈德斯通模（模块 4.6）；声子是晶体中破缺平移对称性的戈德斯通玻色子。该定理有两个重要的限定条件：在低维中，本应的戈德斯通模涨落如此剧烈以至于*完全阻止*对称性破缺（Mermin–Wagner 定理，推导 D 节），而当被破缺的对称性是*规范*的而非整体的时，戈德斯通玻色子被规范场吞噬，不存在物理的无质量粒子——希格斯机制（E 节；在模块 8.4 中完整推导）。

---

## Self-test (blank page) · 自测（空白页）

1. For V(φ) = −½μ²φ² + ¼λφ⁴ with μ² > 0, find the vacuum expectation value ⟨φ⟩ and the mass of the fluctuation about it. Why is φ = 0 not the ground state?
2. State Goldstone's theorem precisely. In the complex-scalar U(1) model, which combination of fields is massive and which is the massless Goldstone boson, and why is the angular direction flat?
3. Give the counting rule for the number of Goldstone bosons in a breaking pattern G → H. Apply it to (a) a single complex scalar with U(1), and (b) chiral SU(2)×SU(2) → SU(2).
4. Why does no physical massless Goldstone boson appear when the broken symmetry is gauged rather than global? What happens to the degree of freedom instead?

**自测（空白页）**

1. 对 V(φ) = −½μ²φ² + ¼λφ⁴（μ² > 0），求真空期望值 ⟨φ⟩ 及围绕它的涨落质量。为何 φ = 0 不是基态？
2. 精确陈述戈德斯通定理。在复标量 U(1) 模型中，哪个场组合有质量、哪个是无质量戈德斯通玻色子，角向方向为何平坦？
3. 给出破缺模式 G → H 中戈德斯通玻色子数目的计数规则。将其应用于（a）带 U(1) 的单个复标量，和（b）手征 SU(2)×SU(2) → SU(2)。
4. 当被破缺的对称性是规范的而非整体的时，为何不出现物理的无质量戈德斯通玻色子？取而代之，该自由度发生了什么？

---

← Previous: [Module 6.9 — Anomalies & Non-Perturbative QFT](./module-6.9-anomalies-and-nonperturbative-qft.md) · [Phase 6 index](./README.md) · Next: [Module 6.11 — Effective Field Theory & the Renormalization Group](./module-6.11-effective-field-theory-and-the-renormalization-group.md) →

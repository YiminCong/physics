# Derivations — Module 5.9: Unconventional & High-Tᶜ Superconductors
# 推导 — 模块 5.9：非常规与高温超导体

> Companion to [Module 5.9](./module-5.9-unconventional-and-high-tc-superconductors.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.9](./module-5.9-unconventional-and-high-tc-superconductors.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The d-wave Gap Function Δ(k) = Δ₀(cos k_x a − cos k_y a) · d 波能隙函数

**Claim.** For a square-lattice superconductor with nearest-neighbor pairing interaction, the gap function in the d_{x²−y²} channel is

  Δ(k) = Δ₀(cos k_x a − cos k_y a),

which belongs to the B₁g irreducible representation of the D₄h point group. This function has four nodes on the Fermi surface where Δ(k) = 0.

**命题。** 对于具有最近邻配对相互作用的方格子超导体，d_{x²−y²} 通道中的能隙函数为

  Δ(k) = Δ₀(cos k_x a − cos k_y a)，

它属于 D₄h 点群的 B₁g 不可约表示。该函数在费米面上有四个节点，使得 Δ(k) = 0。

**Step 1 — Gap equation in momentum space.** The BCS gap equation (Module 5.5) generalized to anisotropic pairing is:

  Δ(k) = − Σ_{k'} V(k, k') ⟨c_{−k'↓} c_{k'↑}⟩ = − Σ_{k'} V(k, k') Δ(k')/(2E_{k'}),

where V(k, k') is the pairing interaction and E_{k'} = √(ε_{k'}² + |Δ(k')|²) is the quasiparticle energy.

**第 1 步 — 动量空间中的能隙方程。** 推广到各向异性配对的 BCS 能隙方程（模块 5.5）为：

  Δ(k) = − Σ_{k'} V(k, k') ⟨c_{−k'↓} c_{k'↑}⟩ = − Σ_{k'} V(k, k') Δ(k')/(2E_{k'})，

其中 V(k, k') 为配对相互作用，E_{k'} = √(ε_{k'}² + |Δ(k')|²) 为准粒子能量。

**Step 2 — Symmetry decomposition of the interaction.** On the square lattice with nearest-neighbor (NN) hopping, the Brillouin zone has D₄h symmetry. Expand the pairing interaction in basis functions of the irreducible representations:

  - s-wave (A₁g): φ_s(k) = 1  (constant, isotropic)
  - extended s-wave (A₁g): φ_{s*}(k) = cos k_x a + cos k_y a
  - d_{x²−y²}-wave (B₁g): φ_d(k) = cos k_x a − cos k_y a
  - d_{xy}-wave (B₂g): φ_{d_{xy}}(k) = sin k_x a sin k_y a

Write V(k, k') = Σ_α V_α φ_α(k) φ_α(k'). If the dominant attractive channel is α = d, then V(k, k') ≈ −V_d φ_d(k) φ_d(k') with V_d > 0.

**第 2 步 — 相互作用的对称性分解。** 在具有最近邻（NN）跳跃的方格子上，布里渊区具有 D₄h 对称性。将配对相互作用展开为不可约表示的基函数：

  - s 波 (A₁g)：φ_s(k) = 1（常数，各向同性）
  - 扩展 s 波 (A₁g)：φ_{s*}(k) = cos k_x a + cos k_y a
  - d_{x²−y²} 波 (B₁g)：φ_d(k) = cos k_x a − cos k_y a
  - d_{xy} 波 (B₂g)：φ_{d_{xy}}(k) = sin k_x a sin k_y a

写 V(k, k') = Σ_α V_α φ_α(k) φ_α(k')。若主导吸引通道为 α = d，则 V(k, k') ≈ −V_d φ_d(k) φ_d(k')，其中 V_d > 0。

**Step 3 — Self-consistent solution.** Substituting the factored form of V into the gap equation:

  Δ(k) = V_d φ_d(k) Σ_{k'} φ_d(k') Δ(k')/(2E_{k'}).

The sum Σ_{k'} φ_d(k') Δ(k')/(2E_{k'}) is a number (call it C). Therefore

  Δ(k) = V_d C · φ_d(k) = Δ₀ φ_d(k) = Δ₀ (cos k_x a − cos k_y a),

where Δ₀ = V_d C is determined self-consistently. The gap function thus inherits the symmetry of the d-channel basis function.

**第 3 步 — 自洽解。** 将分解后的 V 代入能隙方程：

  Δ(k) = V_d φ_d(k) Σ_{k'} φ_d(k') Δ(k')/(2E_{k'})。

求和 Σ_{k'} φ_d(k') Δ(k')/(2E_{k'}) 为一个数（记为 C）。因此

  Δ(k) = V_d C · φ_d(k) = Δ₀ φ_d(k) = Δ₀ (cos k_x a − cos k_y a)，

其中 Δ₀ = V_d C 由自洽条件决定。能隙函数因此继承了 d 通道基函数的对称性。

**Step 4 — Contrast with s-wave.** For s-wave pairing (phonon-mediated BCS), V(k, k') ≈ −V_s (constant near the Fermi surface), giving Δ(k) = Δ₀ (constant), the isotropic s-wave gap. The key differences:

| Property | s-wave | d-wave (d_{x²−y²}) |
|---|---|---|
| Gap symmetry | fully gapped, Δ(k) = const > 0 | sign-changing, nodes at k_x = ±k_y |
| Order param. symmetry | A₁g (invariant under D₄h) | B₁g (changes sign under 90° rotation) |
| Time reversal | preserved | preserved |
| Low-T behavior | exponential (activated) | power-law |

**第 4 步 — 与 s 波对比。** 对于 s 波配对（声子媒介的 BCS），V(k, k') ≈ −V_s（费米面附近为常数），给出 Δ(k) = Δ₀（常数），即各向同性的 s 波能隙。主要区别：

| 性质 | s 波 | d 波 (d_{x²−y²}) |
|---|---|---|
| 能隙对称性 | 全能隙，Δ(k) = const > 0 | 变号，节线在 k_x = ±k_y |
| 序参量对称性 | A₁g（D₄h 下不变） | B₁g（90°旋转下变号） |
| 时间反演 | 守恒 | 守恒 |
| 低温行为 | 指数型（激活型） | 幂律型 |

---

## B. Nodes of the d-wave Gap · d 波能隙的节点

**Claim.** The gap Δ(k) = Δ₀(cos k_x a − cos k_y a) vanishes on the lines k_x = ±k_y in the Brillouin zone. These nodal lines intersect the Fermi surface at four nodal points, producing gapless excitations.

**命题。** 能隙 Δ(k) = Δ₀(cos k_x a − cos k_y a) 在布里渊区的直线 k_x = ±k_y 上为零。这些节线与费米面在四个节点处相交，产生无能隙激发。

**Step 1 — Locate the nodal lines.** Set Δ(k) = 0:

  cos k_x a − cos k_y a = 0    ⟹    cos k_x a = cos k_y a    ⟹    k_x a = ±k_y a + 2πn.

For the principal solution (n = 0): **k_x = k_y** and **k_x = −k_y**. These are the two diagonal lines in the Brillouin zone, at 45° to the reciprocal lattice vectors.

**第 1 步 — 定位节线。** 令 Δ(k) = 0：

  cos k_x a − cos k_y a = 0    ⟹    cos k_x a = cos k_y a    ⟹    k_x a = ±k_y a + 2πn。

主解（n = 0）：**k_x = k_y** 和 **k_x = −k_y**。这是布里渊区中与倒格矢成 45° 的两条对角线。

**Step 2 — Intersection with the Fermi surface.** The Fermi surface of the cuprates (in the simplest tight-binding model with dispersion ε_k = −2t(cos k_x a + cos k_y a) − μ) crosses the nodal lines k_x = ±k_y at four points, called the **nodal points**. At these k_F values:

  k_F ≈ (π/2a, π/2a), (−π/2a, π/2a), (π/2a, −π/2a), (−π/2a, −π/2a)

(and their equivalents modulo the reciprocal lattice). These are the Dirac-like points where both ε_k = 0 (on the Fermi surface) and Δ(k) = 0 simultaneously.

**第 2 步 — 与费米面的交叉点。** 铜氧化物费米面（在最简单的紧束缚模型中色散为 ε_k = −2t(cos k_x a + cos k_y a) − μ）在节线 k_x = ±k_y 处与四个**节点**相交，约为：

  k_F ≈ (π/2a, π/2a), (−π/2a, π/2a), (π/2a, −π/2a), (−π/2a, −π/2a)

（及其模倒格矢的等价点）。这些是 ε_k = 0（在费米面上）和 Δ(k) = 0 同时成立的类狄拉克点。

**Step 3 — Local expansion near a node.** Near a node at k₀ = (k_F, k_F) (taking a = 1 for brevity), write k = k₀ + q. Expand to first order in q = (q_x, q_y):

  ε_k ≈ v_F · q,    Δ(k) ≈ ∇_k Δ|_{k₀} · q,

where v_F = ∇_k ε|_{k₀} and the gradient of Δ at the node:

  ∂Δ/∂k_x|_{k₀} = −Δ₀ a sin(k_F a),    ∂Δ/∂k_y|_{k₀} = +Δ₀ a sin(k_F a).

At the node, |∇_k Δ| = √2 Δ₀ a sin(k_F a) = Δ₀ v_Δ where v_Δ = √2 a sin(k_F a) is the gap velocity. The local quasiparticle energy is

  E(q) = √(v_F² q_∥² + v_Δ² q_⊥²),

where q_∥ is the component along the Fermi surface and q_⊥ is perpendicular. This is a **2D Dirac dispersion** (linear in momentum).

**第 3 步 — 节点附近的局部展开。** 在节点 k₀ = (k_F, k_F) 附近（为简洁取 a = 1），令 k = k₀ + q，展开到 q = (q_x, q_y) 的一阶：

  ε_k ≈ v_F · q，    Δ(k) ≈ ∇_k Δ|_{k₀} · q，

其中 v_F = ∇_k ε|_{k₀}，节点处 Δ 的梯度：

  ∂Δ/∂k_x|_{k₀} = −Δ₀ a sin(k_F a)，    ∂Δ/∂k_y|_{k₀} = +Δ₀ a sin(k_F a)。

在节点处，|∇_k Δ| = √2 Δ₀ a sin(k_F a) = Δ₀ v_Δ，其中 v_Δ = √2 a sin(k_F a) 为能隙速度。局部准粒子能量为

  E(q) = √(v_F² q_∥² + v_Δ² q_⊥²)，

其中 q_∥ 沿费米面，q_⊥ 垂直费米面。这是**二维狄拉克色散**（动量的线性函数）。

---

## C. Low-Energy Density of States: N(E) ∝ E (linear) for d-wave · d 波低能态密度：N(E) ∝ E（线性）

**Claim.** Near E = 0, the quasiparticle density of states for a d-wave superconductor is linear:

  N(E) ∝ E/Δ₀    for E ≪ Δ₀,

in sharp contrast to the fully gapped s-wave case where N(E) = 0 for E < Δ₀.

**命题。** 在 E = 0 附近，d 波超导体的准粒子态密度是线性的：

  N(E) ∝ E/Δ₀    当 E ≪ Δ₀ 时，

这与全能隙 s 波情形（E < Δ₀ 时 N(E) = 0）形成鲜明对比。

**Step 1 — General formula for the DOS.** The quasiparticle DOS is defined as:

  N(E) = Σ_k δ(E − E_k) = ∫ (d²k/(2π)²) δ(E − √(ε_k² + Δ(k)²)).

**第 1 步 — 态密度的一般公式。** 准粒子态密度定义为：

  N(E) = Σ_k δ(E − E_k) = ∫ (d²k/(2π)²) δ(E − √(ε_k² + Δ(k)²))。

**Step 2 — Split the integral into nodal and antinodal contributions.** Near each node (there are 4, related by the D₄h symmetry), use the local linearized dispersion from Section B, Step 3. In rotated coordinates aligned with the Fermi surface tangent (q_∥) and normal (q_⊥) at the node:

  E(q) = √(v_F² q_⊥² + v_Δ² q_∥²).

The contribution to the DOS from one node (integrating over a patch around q = 0):

  N_node(E) = ∫ (dq_∥ dq_⊥/(2π)²) δ(E − √(v_F² q_⊥² + v_Δ² q_∥²)).

**第 2 步 — 将积分分为节点贡献和反节点贡献。** 在每个节点附近（共 4 个，由 D₄h 对称性联系），利用 B 节第 3 步的局部线性化色散。在与节点处费米面切向（q_∥）和法向（q_⊥）对齐的旋转坐标中：

  E(q) = √(v_F² q_⊥² + v_Δ² q_∥²)。

来自单个节点的 DOS 贡献（在 q = 0 附近的小块上积分）：

  N_node(E) = ∫ (dq_∥ dq_⊥/(2π)²) δ(E − √(v_F² q_⊥² + v_Δ² q_∥²))。

**Step 3 — Evaluate using the delta-function and scaling.** Change variables: let p_⊥ = v_F q_⊥ and p_∥ = v_Δ q_∥. The Jacobian is 1/(v_F v_Δ):

  N_node(E) = (1/v_F v_Δ) ∫ (dp_∥ dp_⊥/(2π)²) δ(E − √(p_⊥² + p_∥²)).

Convert to polar coordinates p = √(p_⊥² + p_∥²), angle θ:

  N_node(E) = (1/v_F v_Δ) ∫₀^∞ ∫₀^{2π} (p dp dθ/(2π)²) δ(E − p)
             = (1/v_F v_Δ) · (1/2π) ∫₀^∞ p dp δ(E − p)
             = (1/v_F v_Δ) · E/(2π).

**第 3 步 — 利用 delta 函数和尺度变换求值。** 换元：令 p_⊥ = v_F q_⊥，p_∥ = v_Δ q_∥，雅可比行列式为 1/(v_F v_Δ)：

  N_node(E) = (1/v_F v_Δ) ∫ (dp_∥ dp_⊥/(2π)²) δ(E − √(p_⊥² + p_∥²))。

转化为极坐标 p = √(p_⊥² + p_∥²)，角度 θ：

  N_node(E) = (1/v_F v_Δ) · (1/2π) ∫₀^∞ p dp δ(E − p)
             = (1/v_F v_Δ) · E/(2π)。

**Step 4 — Sum over all four nodes.** The total d-wave DOS at low energies (E ≪ Δ₀, before antinodal regions contribute) from all 4 nodes:

  N(E) = 4 × N_node(E) = 4 × E/(2π v_F v_Δ) = **2E/(π v_F v_Δ)**.

Since v_F and v_Δ are material parameters (fixed by the band structure and gap magnitude), this gives

  **N(E) ∝ E**    for E ≪ Δ₀.

This is the universal result for any 2D superconductor with nodal points where both ε_k and Δ(k) vanish linearly. ∎

**第 4 步 — 对四个节点求和。** 低能（E ≪ Δ₀，反节点区域尚未贡献）时所有 4 个节点的 d 波总 DOS：

  N(E) = 4 × N_node(E) = 4 × E/(2π v_F v_Δ) = **2E/(π v_F v_Δ)**。

由于 v_F 和 v_Δ 为材料参数（由能带结构和能隙大小确定），这给出

  **N(E) ∝ E**    当 E ≪ Δ₀ 时。

这是任何具有节点（ε_k 和 Δ(k) 同时线性为零）的二维超导体的普适结果。∎

---

## D. Physical Consequences of Linear DOS · 线性态密度的物理后果

**Step 1 — Specific heat.** The electronic specific heat c_e ~ ∫ E (dN/dE) dE ~ ∫ E · dE/Δ₀ ~ T²/Δ₀ at low temperatures (using E ~ k_BT). In contrast, s-wave gives c_e ∝ e^{−Δ₀/k_BT} (exponentially activated). The power-law T² behavior of the d-wave specific heat was confirmed in YBCO and other cuprates.

**第 1 步 — 比热。** 电子比热 c_e ~ ∫ E (dN/dE) dE ~ ∫ E · dE/Δ₀ ~ T²/Δ₀（在低温下取 E ~ k_BT）。相比之下，s 波给出 c_e ∝ e^{−Δ₀/k_BT}（指数激活）。d 波比热的幂律 T² 行为已在 YBCO 和其他铜氧化物中得到证实。

**Step 2 — London penetration depth.** The superfluid density n_s(T) enters the penetration depth as λ(T)⁻² ∝ n_s(T). In the d-wave case:

  δ[λ(0)⁻² − λ(T)⁻²] = δn_s(T) ∝ ∫₀^∞ dE N(E) (−∂f/∂E) ≈ N(0_+) k_BT ∝ T

since N(E) ≈ (2/πv_F v_Δ) E is linear and (−∂f/∂E) peaks at E = 0 with width ~k_BT. Thus

  δλ(T) = λ(T) − λ(0) ∝ T    (d-wave, linear in T),

versus λ(T) − λ(0) ∝ e^{−Δ₀/k_BT} for s-wave. The linear T dependence of λ was a landmark experimental signature of d-wave pairing in cuprates (Hardy et al., 1993).

**第 2 步 — 伦敦穿透深度。** 超流密度 n_s(T) 进入穿透深度的关系为 λ(T)⁻² ∝ n_s(T)。d 波情形：

  δ[λ(0)⁻² − λ(T)⁻²] = δn_s(T) ∝ ∫₀^∞ dE N(E) (−∂f/∂E) ≈ N(0_+) k_BT ∝ T，

因为 N(E) ≈ (2/πv_F v_Δ) E 是线性的，(−∂f/∂E) 在 E = 0 处有宽度约 k_BT 的峰。故

  δλ(T) = λ(T) − λ(0) ∝ T    （d 波，关于 T 线性），

而 s 波为 λ(T) − λ(0) ∝ e^{−Δ₀/k_BT}。穿透深度的线性 T 依赖性是铜氧化物 d 波配对的里程碑式实验特征（Hardy 等，1993 年）。

**Step 3 — NMR relaxation rate.** The nuclear spin-lattice relaxation rate 1/T₁ is proportional to ∫ N(E)² (-∂f/∂E) dE (Hebel–Slichter factor). For s-wave, the coherence peak gives a rise in 1/T₁ just below T_c (confirmed in conventional superconductors). For d-wave, the gap nodes mean N(E) ∝ E rather than having the van Hove singularity, so the coherence peak is **absent** and 1/T₁ ∝ T³ (power law) — directly observed in cuprates. This was crucial evidence against s-wave pairing.

**第 3 步 — NMR 弛豫率。** 核自旋晶格弛豫率 1/T₁ 正比于 ∫ N(E)² (-∂f/∂E) dE（赫贝尔–斯利克特因子）。s 波中相干峰在 T_c 以下使 1/T₁ 升高（在常规超导体中得到证实）。d 波中能隙节点意味着 N(E) ∝ E 而非范霍夫奇点，相干峰**不出现**，1/T₁ ∝ T³（幂律）——这在铜氧化物中直接观测到。这是反对 s 波配对的关键证据。

**Step 4 — ARPES and phase-sensitive experiments.** Angle-resolved photoemission spectroscopy (ARPES) directly maps E(k) on the Fermi surface, showing the nodal gap structure |Δ(k)| ∝ |cos k_x a − cos k_y a|. Phase-sensitive experiments (corner SQUID junctions, half-integer flux quantization in trijunctions) directly confirm the **sign change** of Δ(k) under 90° rotation — the hallmark of d-wave that distinguishes it from extended s-wave (which also has a momentum-dependent magnitude but no sign change). These experiments (Wollman, Van Harlingen, Tsuei, 1993–1994) were definitive. ∎

**第 4 步 — ARPES 和相位敏感实验。** 角分辨光电子能谱（ARPES）直接在费米面上绘制 E(k) 图，显示节点能隙结构 |Δ(k)| ∝ |cos k_x a − cos k_y a|。相位敏感实验（角形 SQUID 结、三结中的半整数磁通量子化）直接证实 Δ(k) 在 90° 旋转下**改变符号**——d 波的标志，这将其与扩展 s 波（也有动量依赖的幅度但无符号变化）区分开来。这些实验（Wollman、Van Harlingen、Tsuei，1993–1994 年）具有决定性意义。∎

---

## E. Why Phonons are Unlikely to Mediate d-wave Pairing · 声子不太可能媒介 d 波配对的原因

**Step 1 — BCS phonon kernel is attractive and peaked at small q.** The phonon-mediated interaction is V_{ph}(q) = −2|g_q|² ω_q/(ξ_k² − ω_q²) < 0 (attractive for |ξ_k| < ω_q). In real space this is nearly local (on-site or short-range), which in k-space corresponds to a nearly constant interaction independent of the direction of k. A constant attractive interaction V(k, k') = −V_s gives only s-wave pairing (the projection onto d-wave averages to zero over the Fermi surface).

**第 1 步 — BCS 声子核是吸引的且在小 q 处有峰值。** 声子媒介相互作用为 V_{ph}(q) = −2|g_q|² ω_q/(ξ_k² − ω_q²) < 0（|ξ_k| < ω_q 时为吸引）。实空间中几乎是局域的（格点或短程），在 k 空间对应于几乎与 k 方向无关的常数相互作用。常数吸引相互作用 V(k, k') = −V_s 只给出 s 波配对（费米面上对 d 波的投影平均为零）。

**Step 2 — Spin-fluctuation pairing gives d-wave.** The spin-fluctuation interaction (from antiferromagnetic fluctuations) is

  V_{sf}(q) = (3/2) g² χ(q, 0),

where χ(q, 0) is the static spin susceptibility, peaked at the antiferromagnetic wavevector Q = (π/a, π/a). This peak at Q connects the antinodal regions of the Fermi surface (near (π, 0) and (0, π)) to each other with a sign change:

  V(k, k + Q) = attractive (negative),    k at node,    k + Q at antinode.

The gap equation with this V has the self-consistent solution Δ(k + Q) = −Δ(k) — exactly what d_{x²−y²} symmetry provides (cos(k_x+π) − cos(k_y+π) = −(cos k_x − cos k_y) = −Δ(k)/Δ₀). The spin-fluctuation model thus naturally selects d-wave pairing over s-wave for a near-half-filled band.

**第 2 步 — 自旋涨落配对给出 d 波。** 自旋涨落相互作用（来自反铁磁涨落）为

  V_{sf}(q) = (3/2) g² χ(q, 0)，

其中 χ(q, 0) 为静态自旋磁化率，在反铁磁波矢 Q = (π/a, π/a) 处有峰值。在 Q 处的峰值将费米面的反节点区域（(π, 0) 和 (0, π) 附近）以符号变化相互连接：

  V(k, k + Q) = 吸引（负），    k 在节点，    k + Q 在反节点。

具有此 V 的能隙方程有自洽解 Δ(k + Q) = −Δ(k)——恰好是 d_{x²−y²} 对称性所提供的（cos(k_x+π) − cos(k_y+π) = −(cos k_x − cos k_y) = −Δ(k)/Δ₀）。自旋涨落模型因此对接近半满能带自然选择 d 波配对而非 s 波配对。∎

**Step 3 — The isotope effect.** In BCS, T_c ∝ ω_D ∝ M^{−1/2} (M = ion mass), giving isotope exponent α = 1/2 (replacing isotopes of the same element changes M and hence T_c). In cuprates, the oxygen isotope effect is anomalously small (α ≪ 1/2, and in some compounds α ≈ 0 for the optimal doping). This is inconsistent with phonon-dominated pairing, and supports a non-phonon (electronic/spin) mechanism. ∎

**第 3 步 — 同位素效应。** 在 BCS 中，T_c ∝ ω_D ∝ M^{−1/2}（M = 离子质量），给出同位素指数 α = 1/2（替换同种元素的同位素改变 M 从而改变 T_c）。在铜氧化物中，氧同位素效应异常小（α ≪ 1/2，某些化合物在最优掺杂时 α ≈ 0）。这与声子主导的配对不一致，支持非声子（电子/自旋）机制。∎

---

*Summary: the d-wave gap Δ(k) = Δ₀(cos k_x a − cos k_y a) is the self-consistent solution of the gap equation in the B₁g channel; its four nodal points on the Fermi surface produce linear quasiparticle DOS N(E) ∝ E via a 2D Dirac-cone calculation; this leads to power-law (not exponential) thermodynamics at low T, confirmed by specific heat, penetration depth, NMR, and ARPES. The sign change of Δ(k) is the defining fingerprint of d-wave pairing, confirmed by phase-sensitive SQUID experiments.*

*总结：d 波能隙 Δ(k) = Δ₀(cos k_x a − cos k_y a) 是 B₁g 通道能隙方程的自洽解；其在费米面上的四个节点通过二维狄拉克锥计算产生线性准粒子态密度 N(E) ∝ E；这导致低温下幂律（而非指数）热力学行为，已由比热、穿透深度、NMR 和 ARPES 证实。Δ(k) 的符号变化是 d 波配对的决定性特征，已由相位敏感 SQUID 实验证实。*

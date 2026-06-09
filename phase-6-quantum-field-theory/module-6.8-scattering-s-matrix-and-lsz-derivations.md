# Derivations — Module 6.8: Scattering, the S-Matrix & LSZ Reduction
# 推导 — 模块 6.8：散射、S 矩阵与 LSZ 约化

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.8](./module-6.8-scattering-s-matrix-and-lsz.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.8](./module-6.8-scattering-s-matrix-and-lsz.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. S = 1 + iT and the Definition of the Invariant Amplitude ℳ

**Claim.** The S-matrix can be written S = 1 + iT, where T carries all non-trivial scattering. By Lorentz invariance and four-momentum conservation the T-matrix elements factor as ⟨f|iT|i⟩ = (2π)⁴ δ⁴(p_f − p_i) · iℳ(i→f), where ℳ is the **Lorentz-invariant amplitude**.

**命题。** S 矩阵可写成 S = 1 + iT，其中 T 包含所有非平庸散射。由洛伦兹不变性与四动量守恒，T 矩阵元分解为 ⟨f|iT|i⟩ = (2π)⁴ δ⁴(p_f − p_i) · iℳ(i→f)，其中 ℳ 是**洛伦兹不变振幅**。

**Step 1 — Unitarity decomposition.** The S-matrix is unitary: S†S = SS† = 1. Write S = 1 + iT (the 1 represents no-interaction forward scattering of distinct free-particle states). Then

**第 1 步 — 幺正分解。** S 矩阵是幺正的：S†S = SS† = 1。写 S = 1 + iT（其中 1 表示不同自由粒子态之间无相互作用的前向散射）。则

  S†S = (1 − iT†)(1 + iT) = 1 + i(T − T†) + T†T = 1.

Hence i(T − T†) = −T†T, or equivalently i(T† − T) = T†T. This is the **optical theorem in operator form**, to be exploited in Section D below.

故 i(T − T†) = −T†T，即 i(T† − T) = T†T。这是**算符形式的光学定理**，将在下文 D 节中加以利用。

**Step 2 — Factoring out momentum conservation.** In a translationally invariant theory the Hamiltonian commutes with the total momentum operator: [P^μ, H] = 0. Consequently, if we denote in- and out-states by their momenta, the full S-matrix element ⟨f|S|i⟩ is zero unless the total four-momentum is conserved. We therefore write

**第 2 步 — 提取动量守恒。** 在平移不变的理论中，哈密顿量与总动量算符对易：[P^μ, H] = 0。因此，若用动量标记入态和出态，则全 S 矩阵元 ⟨f|S|i⟩ 在总四动量不守恒时为零。从而写

  ⟨f|iT|i⟩  =  (2π)⁴ δ⁴(Σp_f − Σp_i) · iℳ(i→f).

The factor (2π)⁴ is conventional (matching the Fourier-transform normalization of the propagators in Module 6.3). The remaining quantity iℳ is by construction Lorentz invariant and free of the trivial kinematic delta function; it is the object computed by Feynman diagrams.

因子 (2π)⁴ 是约定写法（与模块 6.3 中传播子的傅里叶变换归一化匹配）。剩余的量 iℳ 在构造上是洛伦兹不变的，且不含平庸的运动学 delta 函数；这正是费曼图所计算的对象。

**Step 3 — Normalization of states.** We use relativistically normalized single-particle states: ⟨p′|p⟩ = (2π)³ 2E_p δ³(p′ − p). The corresponding completeness relation (resolution of the identity) for a single species is

**第 3 步 — 态的归一化。** 我们使用相对论归一化的单粒子态：⟨p′|p⟩ = (2π)³ 2E_p δ³(p′ − p)。对应的单粒子完备性关系（单位分解）为

  1 = ∫ d³p / [(2π)³ 2E_p]  |p⟩⟨p|.

With this normalization, the identity operator in the vacuum and one-particle sectors is explicit. Multi-particle states are products. The relative factor of 2E_p between the covariant and non-covariant normalizations is responsible for the flux factors in cross-section formulae (Section B).

在此归一化下，真空和单粒子扇区的单位算符是显式的。多粒子态是乘积态。协变归一化与非协变归一化之间的相对因子 2E_p 正是截面公式中通量因子的来源（B 节）。 ∎

---

## B. |ℳ|² → Differential Cross Section dσ and Decay Rate dΓ

**Claim.** For a 2→n process in the centre-of-mass frame, dσ = (1/F)|ℳ|² dΦ_n, where F = 4E₁E₂|v₁ − v₂| is the Møller flux factor and dΦ_n is the Lorentz-invariant n-body phase space. For a 1→n decay, dΓ = (1/2M)|ℳ|² dΦ_n.

**命题。** 对质心系中的 2→n 过程，dσ = (1/F)|ℳ|² dΦ_n，其中 F = 4E₁E₂|v₁ − v₂| 为莫勒通量因子，dΦ_n 为洛伦兹不变的 n 体相空间。对 1→n 衰变，dΓ = (1/2M)|ℳ|² dΦ_n。

**Step 1 — Transition rate from Fermi's Golden Rule.** Working in a large box of volume V and time interval T, the S-matrix element for f ≠ i is

**第 1 步 — 从费米黄金规则得到跃迁率。** 在体积为 V、时间间隔为 T 的大盒子中，f ≠ i 时的 S 矩阵元为

  S_{fi} = (2π)⁴ δ⁴(p_f − p_i) · iℳ.

The transition probability per unit time and volume is |S_{fi}|²/(VT). The square of the delta function is handled by the replacement (2π)⁴ δ⁴(0) → VT, valid for large VT. Hence

单位时间、单位体积的跃迁概率为 |S_{fi}|²/(VT)。delta 函数的平方用大 VT 下的替换 (2π)⁴ δ⁴(0) → VT 处理。故

  dP/dT  =  (2π)⁴ δ⁴(Σp_f − Σp_i) · |ℳ|²  ·  Π_f [V d³p_f / (2π)³].

(The factor 1/(2E) per final particle from the relativistic normalization cancels against the 2E in the phase-space measure when assembling the Lorentz-invariant phase space element below.)

（每个末态粒子相对论归一化带来的 1/(2E) 因子，在组装下面的洛伦兹不变相空间元时与相空间测度中的 2E 相消。）

**Step 2 — Lorentz-invariant phase space.** Define the n-body LIPS (Lorentz-Invariant Phase Space):

**第 2 步 — 洛伦兹不变相空间。** 定义 n 体 LIPS（洛伦兹不变相空间）：

  dΦ_n(P; p₁,…,pₙ)  =  (2π)⁴ δ⁴(P − Σ_f p_f)  Π_{f=1}^{n}  [d³p_f / ((2π)³ 2E_f)].

Each factor d³p_f / ((2π)³ 2E_f) = d⁴p_f / (2π)³ · δ(p_f² − m_f²) θ(E_f) is manifestly Lorentz invariant. In terms of dΦ_n:

每个因子 d³p_f / ((2π)³ 2E_f) = d⁴p_f / (2π)³ · δ(p_f² − m_f²) θ(E_f) 是显式洛伦兹不变的。用 dΦ_n 表示：

  dP/dT  =  |ℳ|²  dΦ_n.

**Step 3 — Flux factor for 2→n scattering.** For two incoming particles (1, 2) in any frame, the flux (number of particles crossing unit area per unit time per unit volume) is

**第 3 步 — 2→n 散射的通量因子。** 对任意参考系中的两个入射粒子 (1, 2)，通量（单位体积、单位面积、单位时间内穿过的粒子数）为

  F  =  4 [(p₁·p₂)² − m₁²m₂²]^{1/2}.

In the CM frame with collinear momenta this reduces to F = 4E₁E₂|v₁ − v₂| = 4|p_cm| √s (where √s = E_cm). F is Lorentz-invariant under boosts along the beam axis. The cross section is

在质心系中，对共线动量，此式化为 F = 4E₁E₂|v₁ − v₂| = 4|p_cm| √s（其中 √s = E_cm）。F 在沿束流方向的洛伦兹变换下不变。截面为

  dσ  =  (1/F) |ℳ|² dΦ_n.

**Step 4 — Decay rate for 1→n.** For a single parent particle of mass M at rest (E = M), there is no flux factor — the "beam" is one particle per unit volume — so the denominator is simply the relativistic normalization factor 2M of the initial state. Hence

**第 4 步 — 1→n 衰变率。** 对静止的质量为 M 的单个母粒子 (E = M)，不存在通量因子——"束流"是单位体积内一个粒子——故分母仅为初态的相对论归一化因子 2M。因此

  dΓ  =  (1/2M) |ℳ|² dΦ_n.

**Step 5 — Two-body phase space in the CM frame (worked example).** For n = 2 with equal masses m in the CM frame, dΦ₂ = |p_f| dΩ / (16π² √s). Hence dσ/dΩ = |ℳ|²/(64π² s) · |p_f|/|p_i|, where p_i and p_f are CM momenta of initial and final states. This is the standard 2→2 formula used in Module 6.3 for tree-level cross sections. ∎

**第 5 步 — CM 系中的二体相空间（示例）。** 对 n = 2、CM 系中等质量 m 的情形，dΦ₂ = |p_f| dΩ / (16π² √s)。故 dσ/dΩ = |ℳ|²/(64π² s) · |p_f|/|p_i|，其中 p_i 和 p_f 分别为初末态的质心系动量。这是模块 6.3 中树图截面所用的标准 2→2 公式。∎

---

## C. Mandelstam Variables and the Constraint s + t + u = Σmᵢ²

**Claim.** For the 2→2 process 1+2→3+4, define s = (p₁+p₂)², t = (p₁−p₃)², u = (p₁−p₄)². These three invariants satisfy s + t + u = m₁² + m₂² + m₃² + m₄².

**命题。** 对 2→2 过程 1+2→3+4，定义 s = (p₁+p₂)²，t = (p₁−p₃)²，u = (p₁−p₄)²。这三个不变量满足 s + t + u = m₁² + m₂² + m₃² + m₄²。

**Step 1 — Expand each invariant.** Expand in Minkowski metric (+,−,−,−):

**第 1 步 — 展开每个不变量。** 在闵可夫斯基度规 (+,−,−,−) 下展开：

  s  =  (p₁+p₂)²  =  p₁² + 2p₁·p₂ + p₂²  =  m₁² + 2p₁·p₂ + m₂²,
  t  =  (p₁−p₃)²  =  p₁² − 2p₁·p₃ + p₃²  =  m₁² − 2p₁·p₃ + m₃²,
  u  =  (p₁−p₄)²  =  p₁² − 2p₁·p₄ + p₄²  =  m₁² − 2p₁·p₄ + m₄².

where we used pᵢ² = mᵢ² (on-shell, in the sense of asymptotic states whose mass is the physical pole mass).

其中用到了 pᵢ² = mᵢ²（在壳，即渐近态的质量为物理极点质量）。

**Step 2 — Sum.** Adding the three expressions:

**第 2 步 — 求和。** 将三式相加：

  s + t + u  =  3m₁² + m₂² + m₃² + m₄²  +  2p₁·(p₂ − p₃ − p₄).

**Step 3 — Apply momentum conservation.** Four-momentum conservation gives p₁ + p₂ = p₃ + p₄, so p₂ − p₃ − p₄ = −p₁. Therefore

**第 3 步 — 应用动量守恒。** 四动量守恒给出 p₁ + p₂ = p₃ + p₄，故 p₂ − p₃ − p₄ = −p₁。因此

  2p₁·(p₂ − p₃ − p₄)  =  2p₁·(−p₁)  =  −2p₁²  =  −2m₁².

**Step 4 — Conclude.** Substituting back:

**第 4 步 — 结论。** 代回：

  s + t + u  =  3m₁² + m₂² + m₃² + m₄²  −  2m₁²  =  m₁² + m₂² + m₃² + m₄².

This is the advertised identity. The three variables (s, t, u) are not independent — they lie on a plane in three-dimensional invariant space. For equal masses m, the constraint reads s + t + u = 4m². The physical regions of the s-, t-, and u-channels correspond to different corners of the Mandelstam plane, related by crossing symmetry (exchanging particle labels). ∎

这正是所述等式。三个变量 (s, t, u) 并不独立——它们位于三维不变量空间中的一个平面上。对等质量 m，约束为 s + t + u = 4m²。s、t、u 道的物理区域对应于曼德尔斯坦平面的不同角落，通过交叉对称性（互换粒子标记）相互联系。∎

---

## D. The Optical Theorem from Unitarity S†S = 1

**Claim.** Unitarity implies 2 Im ℳ(i→i, forward) = Σ_X ∫ dΠ_X |ℳ(i→X)|², where the sum runs over all accessible intermediate states X and dΠ_X is their Lorentz-invariant phase space.

**命题。** 幺正性蕴含 2 Im ℳ(i→i, 前向) = Σ_X ∫ dΠ_X |ℳ(i→X)|²，其中求和遍历所有可及中间态 X，dΠ_X 为其洛伦兹不变相空间。

**Step 1 — Operator identity from S†S = 1.** From Step 1 of Section A, S = 1 + iT gives

**第 1 步 — 由 S†S = 1 得算符恒等式。** 由 A 节第 1 步，S = 1 + iT 给出

  S†S  =  1     ⟹     i(T† − T)  =  T†T.

Take the matrix element of this identity between two copies of the initial state |i⟩:

对初态 |i⟩ 取此恒等式的矩阵元：

  i ⟨i|T† − T|i⟩  =  ⟨i|T†T|i⟩.

**Step 2 — Left side.** The left side involves

**第 2 步 — 左边。** 左边包含

  ⟨i|T†|i⟩  =  (⟨i|T|i⟩)*  =  ℳ*(i→i)   (up to the (2π)⁴δ⁴ factor, which equals (2π)⁴δ⁴(0) = VT for forward scattering in large-volume normalization).

  ⟨i|T†|i⟩  =  (⟨i|T|i⟩)*  =  ℳ*(i→i)（不计 (2π)⁴δ⁴ 因子，在大体积归一化下前向散射时 (2π)⁴δ⁴(0) = VT）。

Therefore the left side is i(ℳ* − ℳ) · (2π)⁴δ⁴(0) = 2 Im ℳ(i→i, forward) · (2π)⁴δ⁴(0).

因此左边为 i(ℳ* − ℳ) · (2π)⁴δ⁴(0) = 2 Im ℳ(i→i, 前向) · (2π)⁴δ⁴(0)。

**Step 3 — Right side: insert a complete set of states.** Insert 1 = Σ_X ∫ dΠ_X |X⟩⟨X| (summing over all multi-particle states X, with Lorentz-invariant measure dΠ_X):

**第 3 步 — 右边：插入完备态。** 插入 1 = Σ_X ∫ dΠ_X |X⟩⟨X|（对所有多粒子态 X 求和，采用洛伦兹不变测度 dΠ_X）：

  ⟨i|T†T|i⟩  =  Σ_X ∫ dΠ_X  ⟨i|T†|X⟩⟨X|T|i⟩  =  Σ_X ∫ dΠ_X  |⟨X|T|i⟩|².

Stripping the (2π)⁴δ⁴ factor as before, ⟨X|T|i⟩ = (2π)⁴δ⁴(p_X − p_i) · ℳ(i→X), so

提取 (2π)⁴δ⁴ 因子后，⟨X|T|i⟩ = (2π)⁴δ⁴(p_X − p_i) · ℳ(i→X)，故

  ⟨i|T†T|i⟩  =  (2π)⁴δ⁴(0) · Σ_X ∫ dΠ_X |ℳ(i→X)|².

**Step 4 — Equate and cancel the common factor.** Equating Steps 2 and 3 and cancelling the common factor of (2π)⁴δ⁴(0):

**第 4 步 — 等式两边相等并消去公因子。** 将第 2、3 步等式相等，消去公因子 (2π)⁴δ⁴(0)：

  2 Im ℳ(i→i, forward)  =  Σ_X ∫ dΠ_X |ℳ(i→X)|².

**Step 5 — Relation to the total cross section.** The right side is precisely the quantity that, after dividing by the flux F, gives the total cross section σ_tot = Σ_X σ(i→X). Hence

**第 5 步 — 与总截面的关系。** 右边除以通量 F 后正是总截面 σ_tot = Σ_X σ(i→X)。故

  Im ℳ(i→i, forward)  =  F · σ_tot / 2  =  2E_cm |p_cm| σ_tot   (in CM frame).

This is the standard form of the **optical theorem**: the imaginary part of the forward elastic amplitude equals (flux/2) times the total cross section. Intuitively, the probability removed from the forward beam by absorption (all inelastic processes) must equal the imaginary part of the forward amplitude by probability conservation — a direct consequence of unitarity. ∎

这是**光学定理**的标准形式：前向弹性振幅的虚部等于（通量/2）乘以总截面。直觉上，由吸收（所有非弹性过程）从前向束中移走的概率必须等于前向振幅的虚部，这是概率守恒——即幺正性——的直接结果。∎

---

## E. The LSZ Reduction Formula

**Claim (scalar field theory).** Let φ(x) be a scalar field with physical mass m and field-strength renormalization Z (so that ⟨0|φ(x)|p⟩ = √Z e^{ip·x}). The S-matrix element for n incoming particles (momenta p₁,…,pₙ) and m outgoing particles (momenta k₁,…,kₘ) is given by the **LSZ formula**:

**命题（标量场论）。** 设 φ(x) 为物理质量为 m、场强重整化为 Z 的标量场（使得 ⟨0|φ(x)|p⟩ = √Z e^{ip·x}）。n 个入射粒子（动量 p₁,…,pₙ）与 m 个出射粒子（动量 k₁,…,kₘ）的 S 矩阵元由 **LSZ 公式**给出：

  ⟨k₁…kₘ, out|p₁…pₙ, in⟩  =

    Π_{j=1}^{n}  [i(pⱼ²−m²) / √Z]  ·  Π_{l=1}^{m}  [i(kₗ²−m²) / √Z]

      ·  G̃^{(n+m)}(p₁,…,pₙ, −k₁,…,−kₘ)  |_{all legs on-shell},

where G̃^{(N)}(q₁,…,q_N) = ∫d⁴x₁…d⁴x_N e^{i(q₁·x₁+…+q_N·x_N)} ⟨0|T φ(x₁)…φ(x_N)|0⟩ is the full N-point momentum-space Green's function of the interacting theory (including all loops and self-energy corrections), and the on-shell limit pⱼ²→m², kₗ²→m² is taken.

其中 G̃^{(N)}(q₁,…,q_N) = ∫d⁴x₁…d⁴x_N e^{i(q₁·x₁+…+q_N·x_N)} ⟨0|T φ(x₁)…φ(x_N)|0⟩ 是相互作用理论中完整的 N 点动量空间格林函数（包含所有圈图和自能修正），并取在壳极限 pⱼ²→m²，kₗ²→m²。

**Step 1 — The interacting single-particle pole.** The exact propagator of the interacting theory is

**第 1 步 — 相互作用理论的单粒子极点。** 相互作用理论的精确传播子为

  G̃^{(2)}(p)  =  ∫ d⁴x e^{ip·x} ⟨0|T φ(x) φ(0)|0⟩.

By the **Källén–Lehmann spectral representation** (derived by inserting a complete set of states between the two fields), this has the form

由**凯伦–莱曼谱表示**（在两个场之间插入完备态集得到），其形式为

  G̃^{(2)}(p)  =  Z / (p² − m² + iε)  +  (terms regular at p² = m²  and  multi-particle continuum contributions for p² ≥ (2m)²).

The residue at the physical single-particle pole p² = m² is exactly Z; the bare-field contribution to this residue is 1, so the renormalization constant Z ≤ 1 (Z = 1 in a free theory). The physical mass m is the true pole of G̃^{(2)}, shifted from the bare mass m₀ by self-energy corrections.

物理单粒子极点 p² = m² 处的留数恰好是 Z；裸场对此留数的贡献为 1，故重整化常数 Z ≤ 1（自由理论中 Z = 1）。物理质量 m 是 G̃^{(2)} 的真实极点，由自能修正从裸质量 m₀ 移位而来。

**Step 2 — Derivation of the one-leg reduction.** We want to relate the in-state creation operators to the field φ. The **in-field** φ_in(x) is the free field that φ(x) asymptotically approaches for t→−∞ (in the weak sense on matrix elements); it creates/annihilates physical one-particle states. We have the asymptotic relation

**第 2 步 — 单腿约化的推导。** 我们希望把入态产生算符与场 φ 联系起来。**入场** φ_in(x) 是 φ(x) 在 t→−∞ 时渐近趋近的自由场（在矩阵元的弱意义下）；它产生/湮灭物理单粒子态。我们有渐近关系

  φ(x)  →  √Z φ_in(x)   as  t → −∞,    φ(x)  →  √Z φ_out(x)   as  t → +∞.

The factor √Z is fixed by the normalization ⟨0|φ(x)|p⟩ = √Z e^{ip·x} (single-particle matrix element of the full field). A free scalar field satisfies (∂² + m²)φ_in = 0 and its mode expansion gives the creation operator a†_in(p) by

因子 √Z 由归一化条件 ⟨0|φ(x)|p⟩ = √Z e^{ip·x}（完整场的单粒子矩阵元）确定。自由标量场满足 (∂² + m²)φ_in = 0，其模展开通过以下方式给出产生算符 a†_in(p)：

  a†_in(p)  =  −i ∫ d³x  e^{−ip·x} ↔∂_t  φ_in(x),

where f ↔∂_t g = f(∂_t g) − (∂_t f)g is the Klein–Gordon inner-product operator (the expression is independent of t for solutions of the KG equation).

其中 f ↔∂_t g = f(∂_t g) − (∂_t f)g 是克莱因–戈登内积算符（对 KG 方程的解，该表达式与 t 无关）。

**Step 3 — Express the in-state as a limit.** An in-state with one incoming particle of momentum p is |p, in⟩ = a†_in(p)|0⟩. Using the asymptotic relation and integrating by parts, one can replace a†_in(p) by an integral of φ:

**第 3 步 — 将入态表示为极限。** 动量为 p 的单个入射粒子态为 |p, in⟩ = a†_in(p)|0⟩。利用渐近关系并分部积分，可将 a†_in(p) 替换为 φ 的积分：

  a†_in(p)  =  lim_{t→−∞}  (−i/√Z) ∫ d³x  e^{−ip·x} ↔∂_t  φ(x).

Write this limit as a time integral of the time derivative: lim_{t→−∞} [·] = [·]|_{t=+∞} − ∫_{−∞}^{+∞} dt ∂_t [·]. The surface term at +∞ gives the out-state operator, which will become the out-state creation operator in the amplitude. The bulk integral ∫ dt ∂_t [e^{−ip·x} ↔∂_t φ] can be simplified by integration by parts:

将此极限写成对时间导数的时间积分：lim_{t→−∞} [·] = [·]|_{t=+∞} − ∫_{−∞}^{+∞} dt ∂_t [·]。+∞ 处的面项给出出态算符，它在振幅中成为出态产生算符。体积分 ∫ dt ∂_t [e^{−ip·x} ↔∂_t φ] 通过分部积分化简：

  ∂_t [e^{−ip·x} ↔∂_t φ]  =  e^{−ip·x}(∂_t² φ) − (∂_t² e^{−ip·x}) φ
                            =  e^{−ip·x}[(∂_t² − ∇² + m²)φ]  − φ[(∂_t² − ∇² + m²)e^{−ip·x}]
  (after adding and subtracting ∇² and m² terms, using ∇²e^{−ip·x} = −|p|² e^{−ip·x}  and  ∂_t² e^{−ip·x} = −E_p² e^{−ip·x})
  =  e^{−ip·x} [(□ + m²) φ].

(Here we used that e^{−ip·x} satisfies (□ + m²)e^{−ip·x} = 0 since p² = E_p² − |p|² = m².)

（此处用到 e^{−ip·x} 满足 (□ + m²)e^{−ip·x} = 0，因为 p² = E_p² − |p|² = m²。）

**Step 4 — The fully-reduced expression (one incoming leg).** Combining Steps 2 and 3 gives

**第 4 步 — 完全约化表达式（单个入射腿）。** 综合第 2、3 步得

  a†_in(p)  =  (i/√Z) ∫ d⁴x  e^{−ip·x} (□_x + m²) φ(x)  +  (out-state operator contribution).

The "out-state operator" term — the boundary term at t = +∞ — gives zero when acting to the right on the vacuum |0⟩ (since there are no out-state particles in the vacuum). Thus for a matrix element with one incoming particle:

"出态算符"项——t = +∞ 处的边界项——作用在真空态 |0⟩ 右侧时为零（因为真空中没有出态粒子）。因此对含一个入射粒子的矩阵元：

  ⟨f, out|p, in⟩  =  (i/√Z) ∫ d⁴x  e^{−ip·x} (□_x + m²) ⟨f, out|T φ(x) …|0⟩.

The operator (□_x + m²) acting on a momentum-space Green's function G̃(p,…) gives a factor −(p²−m²) (since □_x e^{ip·x} = −p² e^{ip·x} in Fourier space). We arrive at

算符 (□_x + m²) 作用于动量空间格林函数 G̃(p,…) 给出因子 −(p²−m²)（因为在傅里叶空间中 □_x e^{ip·x} = −p² e^{ip·x}）。我们得到

Combined with the explicit factor of i from the LSZ formula, the contribution per incoming leg is

加上 LSZ 公式中的显式因子 i，每条入射腿的贡献为

  i · (−(p² − m²)) / √Z  =  −i(p² − m²) / √Z.

As p²→m², the full propagator G̃^{(2)}(p) ≈ iZ/(p²−m²+iε), so the product [−i(p²−m²)/√Z] · [iZ/(p²−m²)] = Z/√Z = √Z is finite and non-zero. This is the **amputation**: the external propagator 1/(p²−m²) from the full Green's function is cancelled by the factor (p²−m²) from the LSZ reduction, leaving a finite residue √Z per external leg.

当 p²→m² 时，完整传播子 G̃^{(2)}(p) ≈ iZ/(p²−m²+iε)，故乘积 [−i(p²−m²)/√Z] · [iZ/(p²−m²)] = Z/√Z = √Z 是有限非零的。这正是**截去（摊开）**：完整格林函数中外腿的传播子 1/(p²−m²) 被 LSZ 约化中的因子 (p²−m²) 消掉，每条外腿留下有限留数 √Z。

**Step 5 — Generalization to all legs and final formula.** Repeating the argument for each of the n incoming and m outgoing legs (for outgoing legs the momentum flows out, so the Fourier phase is e^{+ik·x} and the Klein–Gordon operator similarly gives i(k²−m²)):

**第 5 步 — 推广至所有外腿与最终公式。** 对 n 条入射腿和 m 条出射腿重复上述论证（出射腿的动量流出，傅里叶相位为 e^{+ik·x}，克莱因–戈登算符类似地给出 i(k²−m²)）：

  ⟨k₁…kₘ, out|p₁…pₙ, in⟩  =

    Π_{j=1}^{n}  [i(pⱼ² − m²)/√Z]  ·  Π_{l=1}^{m}  [i(kₗ² − m²)/√Z]  ·  G̃^{(n+m)}(p₁,…,pₙ,−k₁,…,−kₘ).

The on-shell limit of each factor i(p²−m²)/√Z times the corresponding external propagator iZ/(p²−m²) gives √Z. The **amputated** Green's function G̃_amp is defined by stripping all n+m external propagators from G̃^{(n+m)}: G̃^{(n+m)} = Π_j [iZ/(pⱼ²−m²)] · Π_l [iZ/(kₗ²−m²)] · G̃_amp^{(n+m)}. Substituting:

每个因子 i(p²−m²)/√Z 乘以对应的外腿传播子 iZ/(p²−m²) 的在壳极限给出 √Z。**截去的**格林函数 G̃_amp 的定义是从 G̃^{(n+m)} 中剥去所有 n+m 条外腿传播子：G̃^{(n+m)} = Π_j [iZ/(pⱼ²−m²)] · Π_l [iZ/(kₗ²−m²)] · G̃_amp^{(n+m)}。代入：

  ⟨k₁…kₘ, out|p₁…pₙ, in⟩  =  (√Z)^{n+m}  ·  G̃_amp^{(n+m)}(on-shell).

In perturbation theory Z = 1 + O(ℏ) (loop corrections), so at tree level G̃_amp reduces to the sum of all connected, amputated Feynman diagrams, which is precisely the iℳ of the Feynman rules (Module 6.3). Beyond tree level, each external leg picks up a factor of √Z — the origin of wave-function renormalization. ∎

在微扰论中 Z = 1 + O(ℏ)（圈图修正），故在树图阶 G̃_amp 化为所有连通截去费曼图之和，这正是模块 6.3 费曼规则中的 iℳ。超出树图阶，每条外腿获得一个 √Z 因子——这正是波函数重整化的起源。∎

---

*Every calculation in QFT connects back to these five results. The S-matrix is unitary; ℳ is its kinematic skeleton; cross sections and decay rates are its modulus squared weighted by phase space; the Mandelstam variables parameterize the kinematics; the optical theorem is unitarity made explicit; and LSZ is the rigorous link between the correlators of the quantum field and the measurable amplitudes.*

*QFT 中的每一个计算都可追溯至这五个结果。S 矩阵是幺正的；ℳ 是其运动学骨架；截面和衰变率是其模平方乘以相空间；曼德尔斯坦变量参数化运动学；光学定理是幺正性的显式表达；LSZ 是量子场的关联函数与可测量振幅之间的严格桥梁。*

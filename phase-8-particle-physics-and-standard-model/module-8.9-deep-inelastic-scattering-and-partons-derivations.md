# Derivations — Module 8.9: Deep Inelastic Scattering & Partons
# 推导 — 模块 8.9：深度非弹性散射与部分子

> Companion to [Module 8.9](./module-8.9-deep-inelastic-scattering-and-partons.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.9](./module-8.9-deep-inelastic-scattering-and-partons.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. DIS Kinematics: Q², the Bjorken Variable x, and Its Range (0,1) · DIS 运动学：Q²、比约肯变量 x 及其范围 (0,1)

**Claim.** In the process e(k) + p(p) → e(k') + X, the virtuality of the exchanged photon is Q² = −q² > 0, the Bjorken variable is x = Q²/(2p·q), and kinematic constraints force x ∈ (0, 1).

**命题。** 在过程 e(k) + p(p) → e(k') + X 中，交换光子的虚度为 Q² = −q² > 0，比约肯变量为 x = Q²/(2p·q)，运动学约束迫使 x ∈ (0, 1)。

**Step 1 — Define the four-momenta.** Work in natural units ℏ = c = 1. Assign:

**第 1 步 — 定义四动量。** 在自然单位 ℏ = c = 1 下，令：

  k^μ = (E, k⃗)     — incoming lepton (electron) 4-momentum,
  k'^μ = (E', k⃗')   — outgoing lepton 4-momentum,
  p^μ = (M, 0⃗)     — proton 4-momentum (proton at rest in the lab frame, mass M ≈ 938 MeV),
  q^μ = k^μ − k'^μ  — 4-momentum transfer (carried by the virtual photon).

  k^μ = (E, k⃗)     — 入射轻子（电子）四动量，
  k'^μ = (E', k⃗')   — 出射轻子四动量，
  p^μ = (M, 0⃗)     — 质子四动量（质子在实验室系静止，质量 M ≈ 938 MeV），
  q^μ = k^μ − k'^μ  — 四动量转移（由虚光子携带）。

**Step 2 — Compute Q².** The invariant momentum transfer squared is:

**第 2 步 — 计算 Q²。** 不变动量转移的平方为：

  q² = (k − k')² = k² + k'² − 2k·k' = m_e² + m_e² − 2k·k' ≈ −2k·k'  (since m_e ≈ 0),

  q² = −2EE'(1 − cos θ),

where θ is the scattering angle of the lepton in the lab frame. Since 0 < θ < π for real scattering, (1 − cos θ) > 0, so **q² < 0**: the photon is **spacelike**. Define:

其中 θ 是轻子在实验室系中的散射角。由于实际散射 0 < θ < π，(1 − cos θ) > 0，故 **q² < 0**：光子是**类空的**。定义：

  **Q² ≡ −q² = 2EE'(1 − cos θ) > 0**.

This is a positive definite quantity measuring the hardness of the scattering. Large Q² means the photon probes short distances ∼ 1/√Q² ≪ 1 fm (proton radius), hence "deep" inelastic scattering.

这是正定量，衡量散射的硬度。大 Q² 意味着光子探测短距离 ∼ 1/√Q² ≪ 1 fm（质子半径），故称"深度"非弹性散射。

**Step 3 — The invariant ν and p·q.** Compute the proton-photon invariant:

**第 3 步 — 不变量 ν 与 p·q。** 计算质子-光子不变量：

  p·q = p·(k − k') = p·k − p·k' = ME − ME' = M(E − E') ≡ Mν,

where **ν = E − E'** is the energy loss of the lepton in the lab frame (the energy deposited into the target). So **p·q = Mν > 0** (since E > E' in DIS, energy is transferred from the lepton to the hadronic system).

其中 **ν = E − E'** 是轻子在实验室系中的能量损失（沉积到靶中的能量）。故 **p·q = Mν > 0**（DIS 中 E > E'，能量从轻子转移到强子系）。

**Step 4 — Define the Bjorken variable x.** The dimensionless ratio:

**第 4 步 — 定义比约肯变量 x。** 无量纲比值：

  **x ≡ Q²/(2p·q) = Q²/(2Mν)**.

This is Lorentz invariant (ratio of two Lorentz scalars), so x has the same value in any frame.

这是洛伦兹不变量（两个洛伦兹标量之比），故 x 在任何参考系中取相同值。

**Step 5 — Prove x ∈ (0, 1).** We need two bounds:

**第 5 步 — 证明 x ∈ (0, 1)。** 需要两个界：

*Lower bound x > 0:* Both Q² > 0 and p·q = Mν > 0, so x > 0. (x = 0 would require q = 0, i.e. no scattering.)

*下界 x > 0：* Q² > 0 且 p·q = Mν > 0，故 x > 0。（x = 0 意味着 q = 0，即无散射。）

*Upper bound x < 1:* Consider the invariant mass W of the hadronic final state X:

*上界 x < 1：* 考虑强子末态 X 的不变质量 W：

  W² = (p + q)² = p² + 2p·q + q² = M² + 2Mν − Q².

For the final state to be physical (W² ≥ M²: it must be at least as massive as the proton, since we need at least one baryon in the final state):

为使末态物理（W² ≥ M²：至少与质子一样重，因末态至少需要一个重子）：

  W² ≥ M²   ⟹   M² + 2Mν − Q² ≥ M²   ⟹   2Mν ≥ Q²   ⟹   x = Q²/(2Mν) ≤ 1.

Equality x = 1 corresponds to W² = M², i.e. **elastic scattering** (the proton stays intact, X = p). For inelastic scattering W > M, so **x < 1** strictly.

等号 x = 1 对应 W² = M²，即**弹性散射**（质子保持完整，X = p）。对于非弹性散射 W > M，故严格地 **x < 1**。

Combining: **0 < x ≤ 1**, with x = 1 being the elastic limit and x < 1 for all inelastic processes. In the DIS regime (truly inelastic, W ≫ M), x is a continuous variable in (0, 1). ∎

综合：**0 < x ≤ 1**，x = 1 是弹性极限，x < 1 对所有非弹性过程成立。在 DIS 区间（真正非弹性，W ≫ M），x 是 (0, 1) 中的连续变量。∎

---

## B. The Inclusive DIS Cross-Section in Terms of Structure Functions F₁, F₂ · 用结构函数 F₁、F₂ 表示的 DIS 包容截面

**Claim.** The most general Lorentz-invariant, gauge-invariant form for the inclusive DIS cross-section e + p → e + X, summed over all hadronic final states X, can be written in terms of only two independent structure functions F₁(x, Q²) and F₂(x, Q²).

**命题。** 对所有强子末态 X 求和后，e + p → e + X 包容 DIS 截面最一般的洛伦兹不变、规范不变形式只能用两个独立结构函数 F₁(x, Q²) 和 F₂(x, Q²) 写出。

**Step 1 — The hadronic tensor.** The cross-section factorizes as:

**第 1 步 — 强子张量。** 截面因子化为：

  dσ ∝ L^{μν}(k, k') · W_{μν}(p, q),

where L^{μν} is the **leptonic tensor** (calculable in QED) and W_{μν} is the **hadronic tensor** encoding all the unknown proton structure.

其中 L^{μν} 是**轻子张量**（在 QED 中可计算），W_{μν} 是编码所有未知质子结构的**强子张量**。

**Step 2 — The leptonic tensor.** For an unpolarized electron (averaging over initial spins, summing over final spins), the QED calculation gives:

**第 2 步 — 轻子张量。** 对非极化电子（对初态自旋取平均，对末态自旋求和），QED 计算给出：

  L^{μν} = 2(k^μ k'^ν + k'^μ k^ν − g^{μν} k·k').

(This follows from the standard trace technology: L^{μν} = Tr[γ^μ k̸ γ^ν k̸'] / 2, using Tr[γ^μ γ^α γ^ν γ^β] = 4(g^{μα}g^{νβ} − g^{μν}g^{αβ} + g^{μβ}g^{να}).)

（这源于标准迹技术：L^{μν} = Tr[γ^μ k̸ γ^ν k̸'] / 2，利用 Tr[γ^μ γ^α γ^ν γ^β] = 4(g^{μα}g^{νβ} − g^{μν}g^{αβ} + g^{μβ}g^{να})。）

**Step 3 — Constraints on the hadronic tensor.** W_{μν} must satisfy:
(i) **Current conservation** (Ward identity): q^μ W_{μν} = 0 and q^ν W_{μν} = 0.
(ii) **Lorentz covariance**: W_{μν} must be built from the available Lorentz tensors constructed from p^μ and q^μ (the only independent 4-vectors, since we sum over all final states X).
(iii) **Hermiticity**: W_{μν} = W_{νμ}^* (for real structure functions: W_{μν} = W_{νμ}).
(iv) **Time-reversal symmetry** (for parity-conserving electromagnetic interaction): W_{μν} is symmetric.

**第 3 步 — 强子张量的约束。** W_{μν} 必须满足：
(i) **流守恒**（沃德恒等式）：q^μ W_{μν} = 0 且 q^ν W_{μν} = 0。
(ii) **洛伦兹协变性**：W_{μν} 必须由可用的洛伦兹张量构造，即由 p^μ 和 q^μ（对所有末态 X 求和后仅有的独立四向量）构成。
(iii) **厄米性**：W_{μν} = W_{νμ}^*（对实结构函数：W_{μν} = W_{νμ}）。
(iv) **时间反演对称性**（对宇称守恒的电磁相互作用）：W_{μν} 是对称的。

**Step 4 — Most general symmetric tensor from p, q.** The symmetric rank-2 tensors constructible from p^μ, q^μ are: g^{μν}, p^μp^ν, q^μq^ν, p^μq^ν + q^μp^ν. Imposing q^μ W_{μν} = 0 eliminates the q^μq^ν and p^μq^ν terms (they don't vanish on their own but must combine to satisfy transversality). The transverse projector is:

**第 4 步 — 由 p、q 构造的最一般对称张量。** 由 p^μ、q^μ 可构造的对称二阶张量有：g^{μν}、p^μp^ν、q^μq^ν、p^μq^ν + q^μp^ν。施加 q^μ W_{μν} = 0 消除了 q^μq^ν 和 p^μq^ν 项（它们自身不消失，但必须组合以满足横向性条件）。横向投影算符为：

  T^{μν} = −g^{μν} + q^μq^ν/q²,
  P̃^μ = p^μ − (p·q/q²) q^μ   (transverse projection of p).

The most general transverse symmetric tensor is:

最一般的横向对称张量为：

  W^{μν} = W₁ (−g^{μν} + q^μq^ν/q²) + W₂/M² · (p^μ − p·q/q² · q^μ)(p^ν − p·q/q² · q^ν).

**Step 5 — Standard conventions.** Define the dimensionless structure functions:

**第 5 步 — 标准惯例。** 定义无量纲结构函数：

  F₁(x, Q²) ≡ M W₁(ν, Q²),
  F₂(x, Q²) ≡ ν W₂(ν, Q²).

(Conventions vary in the literature; these are the standard Bjorken–Paschos conventions.) The hadronic tensor becomes:

（文献中惯例有所不同；这是标准的比约肯–帕斯乔斯惯例。）强子张量变为：

  M W^{μν} = F₁ (−g^{μν} + q^μq^ν/q²) + F₂/(p·q) · (p^μ − p·q/q² · q^μ)(p^ν − p·q/q² · q^ν).

**Step 6 — The differential cross-section.** Contracting with L^{μν} and integrating, the double-differential cross-section is (in the lab frame):

**第 6 步 — 微分截面。** 与 L^{μν} 缩并并积分，实验室系中的双微分截面为：

  d²σ/(dE' dΩ) = (α²)/(4E²sin⁴(θ/2)) · [F₂ cos²(θ/2) + 2xF₁ · (2/M) sin²(θ/2) / ν].

This is the **Rosenbluth-like formula for DIS**, expressing the measurable cross-section in terms of the two structure functions F₁ and F₂. Separating longitudinal and transverse photon polarizations, one finds that F₁ couples to transversely polarized virtual photons and F₂ receives contributions from both transverse and longitudinal polarizations. ∎

这是 **DIS 的类罗森布鲁斯公式**，用两个结构函数 F₁ 和 F₂ 表达可测截面。将纵向和横向光子极化分离，可以发现 F₁ 与横向极化虚光子耦合，F₂ 接收横向和纵向极化的贡献。∎

---

## C. The Parton-Model Result F₂(x) = Σᵢ eᵢ² x fᵢ(x) · 部分子模型结果 F₂(x) = Σᵢ eᵢ² x fᵢ(x)

**Claim.** In the parton model (impulse approximation), the proton is composed of quasi-free pointlike constituents (partons) each carrying a fraction x of the proton's momentum. The photon scatters elastically off a single parton. The result is F₂(x) = Σᵢ eᵢ² x fᵢ(x), where fᵢ(x) dx is the probability of finding parton i with momentum fraction in (x, x+dx), and Bjorken scaling (independence of Q²) emerges automatically.

**命题。** 在部分子模型（冲量近似）中，质子由准自由点状组分（部分子）构成，每个部分子携带质子动量的分数 x。光子弹性散射于单个部分子上。结果为 F₂(x) = Σᵢ eᵢ² x fᵢ(x)，其中 fᵢ(x) dx 是找到携带动量分数在 (x, x+dx) 的部分子 i 的概率，比约肯标度（对 Q² 的独立性）自动出现。

**Step 1 — The impulse approximation.** In the Breit frame (infinite momentum frame), the proton moves with very large momentum P along the z-axis: p^μ = (P, 0, 0, P) with P → ∞. In this limit, the proton looks like a beam of non-interacting partons, each moving collinearly with the proton. The interactions between partons are slow (long time-scale) compared to the interaction time of the virtual photon (short time-scale ∼ 1/Q), and can be neglected during the scattering — this is the **impulse approximation**.

**第 1 步 — 冲量近似。** 在布雷特系（无限动量系）中，质子沿 z 轴以极大动量 P 运动：p^μ = (P, 0, 0, P)，P → ∞。在此极限下，质子看起来像是非相互作用部分子束，每个部分子沿质子方向共线运动。部分子间的相互作用（长时间尺度）相比虚光子的相互作用时间（短时间尺度 ∼ 1/Q）缓慢，在散射过程中可以忽略——这就是**冲量近似**。

**Step 2 — Parton kinematics.** Let parton i carry a fraction ξ of the proton's 4-momentum:

**第 2 步 — 部分子运动学。** 设部分子 i 携带质子四动量的分数 ξ：

  p_i^μ = ξ p^μ  (massless parton: p_i² = 0, since ξ²p² = ξ²M² → 0 for M/P → 0).

The photon scatters elastically off this parton: γ* + parton(ξp) → parton(p_i'). The final parton momentum is:

光子弹性散射于此部分子：γ* + 部分子(ξp) → 部分子(p_i')。末态部分子动量为：

  p_i'^μ = p_i^μ + q^μ = ξ p^μ + q^μ.

**Step 3 — Elastic constraint fixes ξ = x.** The scattered parton must remain on-shell (massless):

**第 3 步 — 弹性约束固定 ξ = x。** 散射部分子必须保持在质量壳上（无质量）：

  p_i'^2 = (ξ p + q)² = ξ²p² + 2ξ(p·q) + q² = 0 + 2ξ(p·q) − Q² = 0.

Solving: **ξ = Q²/(2p·q) = x**. The Bjorken variable x is precisely the momentum fraction of the struck parton. This is the kinematic identification of x.

求解：**ξ = Q²/(2p·q) = x**。比约肯变量 x 正是被打部分子的动量分数。这是 x 的运动学识别。

**Step 4 — Cross-section for scattering off a single parton.** Parton i with charge e_i (in units of e) is a pointlike Dirac particle. The QED cross-section for γ* + parton_i → parton_i (elastic, massless) has the same kinematic structure as γ* + e → e, giving hadronic tensor contributions:

**第 4 步 — 散射于单个部分子的截面。** 带电荷 e_i（以 e 为单位）的部分子 i 是点状狄拉克粒子。γ* + 部分子_i → 部分子_i（弹性，无质量）的 QED 截面具有与 γ* + e → e 相同的运动学结构，给出强子张量贡献：

  W_{μν}^{(i)}(parton) ∝ e_i² δ(p_i² + 2p_i·q + q²) · (sum of tensor structures).

The delta function δ(2ξ p·q − Q²) = δ(ξ − x)/(2p·q) enforces the elastic condition ξ = x.

δ 函数 δ(2ξ p·q − Q²) = δ(ξ − x)/(2p·q) 强制执行弹性条件 ξ = x。

**Step 5 — Integrate over parton distributions.** The total hadronic tensor is:

**第 5 步 — 对部分子分布积分。** 总强子张量为：

  W_{μν} = Σᵢ ∫₀¹ dξ fᵢ(ξ) · W_{μν}^{(i)}(ξ, q)

where fᵢ(ξ) is the **parton distribution function (PDF)**: fᵢ(ξ) dξ = probability that parton i has momentum fraction in (ξ, ξ+dξ).

其中 fᵢ(ξ) 是**部分子分布函数（PDF）**：fᵢ(ξ) dξ = 部分子 i 的动量分数在 (ξ, ξ+dξ) 内的概率。

The delta function δ(ξ − x) collapses the ξ integral, giving the hadronic tensor evaluated at ξ = x. Reading off the F₂ coefficient:

δ 函数 δ(ξ − x) 使 ξ 积分坍缩，给出在 ξ = x 处求值的强子张量。读出 F₂ 系数：

  **F₂(x) = Σᵢ eᵢ² x fᵢ(x)**,

where the sum runs over all parton species i (quarks of each flavor and, for charge-zero partons, gluons do not contribute directly since they have e_g = 0).

其中求和遍历所有部分子种类 i（每种味的夸克；对零电荷部分子，胶子由于 e_g = 0 不直接贡献）。

**Step 6 — Bjorken scaling.** In the pure parton model, the PDFs fᵢ(x) are functions of x alone — they do not depend on Q². Therefore F₂(x, Q²) = F₂(x) depends only on x, not on Q². This is **Bjorken scaling**. Physically, the photon is scattering off a pointlike, structureless parton — there is no scale in the problem (a pointlike particle has no size), so the cross-section cannot depend on Q². ∎

**第 6 步 — 比约肯标度。** 在纯部分子模型中，PDF fᵢ(x) 只是 x 的函数——不依赖 Q²。因此 F₂(x, Q²) = F₂(x) 只依赖 x，不依赖 Q²。这就是**比约肯标度**。物理上，光子散射于点状、无结构的部分子——问题中没有标度（点状粒子没有尺寸），截面不能依赖 Q²。∎

---

## D. The Callan–Gross Relation 2xF₁ = F₂ for Spin-½ Partons · 自旋-½ 部分子的卡兰–格罗斯关系 2xF₁ = F₂

**Claim.** For spin-½ (Dirac) partons, the two structure functions satisfy 2xF₁ = F₂. For spin-0 (scalar) partons, F₁ = 0. The experimental observation 2xF₁ ≈ F₂ (Bjorken–Paschos, SLAC 1969) therefore identifies the partons as spin-½ quarks.

**命题。** 对自旋-½（狄拉克）部分子，两个结构函数满足 2xF₁ = F₂。对自旋-0（标量）部分子，F₁ = 0。因此，2xF₁ ≈ F₂ 的实验观测（比约肯–帕斯乔斯，SLAC 1969）将部分子识别为自旋-½ 夸克。

**Step 1 — Virtual photon absorption cross-sections.** Introduce the longitudinal and transverse cross-sections for absorption of a virtual photon:

**第 1 步 — 虚光子吸收截面。** 引入虚光子吸收的纵向和横向截面：

  σ_T ∝ F₁  (transverse photon, helicity ±1),
  σ_L ∝ (1 + Q²/ν²) F₂/(2x) − F₁  (longitudinal photon, helicity 0).

Equivalently, R ≡ σ_L/σ_T measures the ratio of longitudinal to transverse cross-sections; R = 0 would imply 2xF₁ = F₂.

等价地，R ≡ σ_L/σ_T 衡量纵向与横向截面之比；R = 0 意味着 2xF₁ = F₂。

**Step 2 — Tensor structure for a spin-½ parton.** The elastic electromagnetic current of a massless spin-½ Dirac particle is j^μ = ē(p') γ^μ u(p). The squared matrix element summed over spins is:

**第 2 步 — 自旋-½ 部分子的张量结构。** 无质量自旋-½ 狄拉克粒子的弹性电磁流为 j^μ = ē(p') γ^μ u(p)。对自旋求和后的矩阵元平方为：

  Σ_{spins} |⟨p'|j^μ|p⟩|² = Tr[γ^μ p̸' γ^ν p̸] = 4(p'^μ p^ν + p'^ν p^μ − g^{μν} p'·p).

Using p = ξp_proton and p' = p + q (= ξp + q), the parton-level hadronic tensor is:

利用 p = ξp_质子 和 p' = p + q（= ξp + q），部分子级强子张量为：

  w^{μν}_{spin-1/2} = 2 δ(2ξ p·q − Q²) · (p^μ p'^ν + p'^μ p^ν − g^{μν} p·p').

After integrating with fᵢ(ξ) and using δ(ξ − x), one extracts:

对 fᵢ(ξ) 积分并利用 δ(ξ − x) 后，提取：

  W₁^{(i)} ∝ (1/2M) eᵢ² fᵢ(x),
  W₂^{(i)} ∝ (x²/Mν) eᵢ² fᵢ(x).

In terms of the standard structure functions F₁ = M W₁ and F₂ = ν W₂:

用标准结构函数 F₁ = M W₁ 和 F₂ = ν W₂ 表示：

  F₁ = (1/2) Σᵢ eᵢ² fᵢ(x),
  F₂ = x Σᵢ eᵢ² fᵢ(x) = 2x F₁.

Therefore: **2xF₁ = F₂**. This is the **Callan–Gross relation**.

因此：**2xF₁ = F₂**。这就是**卡兰–格罗斯关系**。

**Step 3 — Physical interpretation: helicity conservation.** For a massless spin-½ particle, helicity is conserved. A transverse (helicity ±1) photon can flip the helicity of the parton (spin-½ has helicity ±1/2, and the interaction via γ^μ preserves helicity for massless fermions). But a longitudinal (scalar) photon carries helicity 0 and cannot be absorbed by a massless spin-½ parton without violating angular momentum conservation along the beam axis. Therefore σ_L = 0 for massless spin-½ partons, which is equivalent to R = 0, i.e. **2xF₁ = F₂**.

**第 3 步 — 物理诠释：螺旋度守恒。** 对无质量自旋-½ 粒子，螺旋度守恒。横向（螺旋度 ±1）光子可翻转部分子的螺旋度（自旋-½ 螺旋度为 ±1/2，通过 γ^μ 的相互作用对无质量费米子守恒螺旋度）。但纵向（标量）光子携带螺旋度 0，不能被无质量自旋-½ 部分子吸收而不违反沿束流轴的角动量守恒。因此对无质量自旋-½ 部分子 σ_L = 0，等价于 R = 0，即 **2xF₁ = F₂**。

**Step 4 — Contrast with spin-0 partons.** For a spin-0 (scalar) charged particle with coupling φ* A^μ ∂_μ φ, the electromagnetic current is proportional to (p + p')^μ (no γ^μ). The elastic form factor squared is:

**第 4 步 — 与自旋-0 部分子的对比。** 对耦合为 φ* A^μ ∂_μ φ 的自旋-0（标量）带电粒子，电磁流正比于 (p + p')^μ（无 γ^μ）。弹性形状因子平方为：

  |j^μ|² ∝ (p + p')^μ (p + p')^ν.

The tensor structure is symmetric and of rank 2 in momenta, but contains no g^{μν} term. This means:

张量结构在动量中是对称的二阶张量，但不含 g^{μν} 项。这意味着：

  W₁^{spin-0} = 0   ⟹   **F₁ = 0**  (for scalar partons).

The transverse cross-section vanishes: σ_T = 0. Longitudinal photons do the scattering. So **R = σ_L/σ_T → ∞** for spin-0 partons.

横向截面消失：σ_T = 0。纵向光子完成散射。故对自旋-0 部分子 **R = σ_L/σ_T → ∞**。

**Step 5 — Experimental test (SLAC 1969).** The SLAC experiment measured F₂ and 2xF₁ separately by varying the beam energy and scattering angle at fixed x and Q². The ratio 2xF₁/F₂ was found to be close to 1 (i.e., R ≈ 0) over a wide range of x and Q², establishing that the partons are **spin-½** particles — identified with the quarks of the quark model (Module 8.8). ∎

**第 5 步 — 实验检验（SLAC 1969）。** SLAC 实验通过在固定 x 和 Q² 下改变束流能量和散射角，分别测量了 F₂ 和 2xF₁。在宽广的 x 和 Q² 范围内，比值 2xF₁/F₂ 接近 1（即 R ≈ 0），确立了部分子是**自旋-½** 粒子——与夸克模型（模块 8.8）的夸克等同。∎

---

## E. The Momentum Sum Rule and the ~50% Carried by Gluons · 动量求和规则与胶子携带的 ~50%

**Claim.** The momentum sum rule states Σᵢ ∫₀¹ x fᵢ(x) dx = 1 if all constituents are accounted for. Experimentally, quarks carry only ~50% of the proton momentum, implying that electrically neutral partons (gluons) carry the other ~50%.

**命题。** 动量求和规则陈述：若所有组分均被计入，则 Σᵢ ∫₀¹ x fᵢ(x) dx = 1。实验上，夸克只携带 ~50% 的质子动量，这意味着电中性部分子（胶子）携带另外 ~50%。

**Step 1 — Derive the sum rule.** In the infinite momentum frame, the total momentum of the proton is P (by definition). The momentum of all partons must sum to P:

**第 1 步 — 推导求和规则。** 在无限动量系中，质子的总动量按定义为 P。所有部分子的动量必须求和为 P：

  Σᵢ ⟨p_i⟩ = P,

where ⟨p_i⟩ = P ∫₀¹ ξ fᵢ(ξ) dξ (average momentum of partons of type i). Dividing by P:

其中 ⟨p_i⟩ = P ∫₀¹ ξ fᵢ(ξ) dξ（i 类部分子的平均动量）。除以 P：

  **Σᵢ ∫₀¹ x fᵢ(x) dx = 1**   (momentum sum rule).

The sum runs over all parton species: u, ū, d, d̄, s, s̄, ... (quarks and antiquarks) AND gluons g.

求和遍历所有部分子种类：u、ū、d、d̄、s、s̄、...（夸克和反夸克）以及胶子 g。

**Step 2 — What DIS measures.** Deep inelastic scattering is sensitive only to **charged** partons (the virtual photon couples to electric charge). The measured structure function F₂ gives:

**第 2 步 — DIS 测量什么。** 深度非弹性散射只对**带电**部分子灵敏（虚光子与电荷耦合）。测得的结构函数 F₂ 给出：

  ∫₀¹ F₂(x) dx = ∫₀¹ Σ_q e_q² x f_q(x) dx = Σ_q e_q² ∫₀¹ x f_q(x) dx.

For a proton with u, d, s quarks and their antiquarks, and using e_u = 2/3, e_d = e_s = −1/3:

对含 u、d、s 夸克及其反夸克的质子，利用 e_u = 2/3，e_d = e_s = −1/3：

  ∫₀¹ F₂^p(x) dx = (4/9)⟨xu + xū⟩ + (1/9)⟨xd + xd̄⟩ + (1/9)⟨xs + xs̄⟩,

where ⟨xq⟩ ≡ ∫₀¹ x f_q(x) dx.

其中 ⟨xq⟩ ≡ ∫₀¹ x f_q(x) dx。

**Step 3 — Experimental measurement.** At fixed Q² ≈ 10 GeV², early experiments (SLAC, CERN) measured:

**第 3 步 — 实验测量。** 在固定 Q² ≈ 10 GeV² 处，早期实验（SLAC、CERN）测量得到：

  ∫₀¹ F₂^p(x) dx ≈ 0.18,   ∫₀¹ F₂^n(x) dx ≈ 0.12.

(Here F₂^n is from neutrino scattering or deuterium targets to get neutron structure.) Using the quark model relations, one can solve for the individual momentum fractions. The result is that quarks (of all flavors, quarks + antiquarks) carry:

（此处 F₂^n 来自中微子散射或氘靶以获得中子结构。）利用夸克模型关系，可求解各动量分数。结果是所有味的夸克（夸克+反夸克）携带：

  Σ_q ∫₀¹ x f_q(x) dx ≈ 0.54   (quarks carry ~54% of the proton's momentum).

**Step 4 — The gluon fraction.** By the momentum sum rule, the remaining momentum is carried by gluons:

**第 4 步 — 胶子分数。** 由动量求和规则，剩余动量由胶子携带：

  ∫₀¹ x f_g(x) dx = 1 − Σ_q ∫₀¹ x f_q(x) dx ≈ 1 − 0.54 = 0.46 ≈ 50%.

This is the **gluon momentum fraction**: roughly half the proton's momentum is carried by electrically neutral gluons that DIS cannot directly see. This is direct evidence for the existence of gluons as real physical constituents of the proton, and confirms QCD (Module 8.3). ∎

这就是**胶子动量分数**：质子约一半的动量由 DIS 无法直接看到的电中性胶子携带。这是胶子作为质子真实物理组分存在的直接证据，证实了 QCD（模块 8.3）。∎

---

## F. Scaling Violations and the DGLAP Equations from Gluon Radiation · 胶子辐射导致的标度破坏与 DGLAP 方程

**Claim.** Pure Bjorken scaling (F₂ depends only on x, not Q²) is violated by QCD. As Q² increases, the virtual photon resolves more and more gluon-radiation substructure, causing partons to split and the PDFs to evolve. The evolution is governed by the **DGLAP equations** (Dokshitzer–Gribov–Lipatov–Altarelli–Parisi), whose physical origin is gluon emission from quarks and quark–antiquark pair production from gluons. The coupling α_s(Q²) runs to zero (asymptotic freedom), making the evolution calculable in perturbation theory.

**命题。** 纯比约肯标度（F₂ 只依赖 x，不依赖 Q²）被 QCD 所破坏。随着 Q² 增大，虚光子分辨越来越多的胶子辐射子结构，导致部分子劈裂和 PDF 演化。演化由 **DGLAP 方程**（多克希策–格里博夫–利帕托夫–阿尔塔雷利–帕里西）支配，其物理起源是来自夸克的胶子辐射和来自胶子的正反夸克对产生。跑动耦合 α_s(Q²) 趋向零（渐近自由），使得演化可在微扰论中计算。

**Step 1 — Physical picture of scaling violations.** At resolution scale Q, a photon probing a quark with momentum fraction x sees the quark as a pointlike object — if the quark has not radiated. But at higher resolution Q' > Q, the photon can resolve the fact that the quark previously emitted a gluon (which carries away some momentum), so what appeared to be a single quark is revealed to be a quark-plus-gluon system. The quark now carries less momentum than x, and there are more partons at smaller x values. Qualitatively:

**第 1 步 — 标度破坏的物理图像。** 在分辨尺度 Q 处，探测动量分数为 x 的夸克的光子将夸克视为点状物体——如果夸克没有辐射的话。但在更高分辨率 Q' > Q 处，光子可以分辨出夸克之前发射了一个胶子（携走一些动量），因此看似单个夸克实际上被揭示为夸克加胶子系统。夸克现在携带的动量少于 x，且在更小 x 值处有更多部分子。定性地：

  - F₂(x, Q²) decreases at large x as Q² increases (quarks radiate, losing momentum).
  - F₂(x, Q²) increases at small x as Q² increases (splittings populate the small-x region).

  - 随 Q² 增大，F₂(x, Q²) 在大 x 处减小（夸克辐射，损失动量）。
  - 随 Q² 增大，F₂(x, Q²) 在小 x 处增大（劈裂填充小 x 区域）。

**Step 2 — The splitting functions.** The probability for a quark with momentum fraction y to emit a gluon and become a quark with momentum fraction x = zy (z < 1) in a collinear splitting involves a **splitting function** P_{qq}(z). At leading order in α_s:

**第 2 步 — 劈裂函数。** 动量分数为 y 的夸克辐射胶子并成为动量分数为 x = zy（z < 1）的夸克的概率，在共线劈裂中涉及**劈裂函数** P_{qq}(z)。在 α_s 的领头阶：

  P_{qq}(z) = C_F · (1 + z²)/(1 − z)_+,    C_F = 4/3  (Casimir of SU(3) fundamental).
  P_{gq}(z) = C_F · (1 + (1−z)²)/z          (quark → gluon + quark).
  P_{qg}(z) = T_F · (z² + (1−z)²),           T_F = 1/2  (gluon → quark + antiquark).
  P_{gg}(z) = 2C_A · [z/(1−z)_+ + (1−z)/z + z(1−z)],   C_A = 3  (SU(3) adjoint Casimir).

Here the "plus" distribution (1/(1−z))_+ regulates the collinear singularity at z → 1.

此处"加"分布 (1/(1−z))_+ 正规化了 z → 1 处的共线奇点。

**Step 3 — Derive the DGLAP equations.** Consider the PDF fq(x, Q²). At scale Q², the probability of finding a quark with fraction x receives contributions from:

**第 3 步 — 推导 DGLAP 方程。** 考虑 PDF fq(x, Q²)。在标度 Q² 处，找到分数为 x 的夸克的概率接收以下贡献：

(a) A quark at fraction x that did not radiate (probability ~ 1 − α_s·correction).
(b) A quark at fraction y > x that radiated a gluon and ended up at x = zy: integrated over all y > x.
(c) A gluon at fraction y that split into a q q̄ pair with the quark at x.

(a) 分数为 x 的夸克未辐射（概率 ~ 1 − α_s·修正）。
(b) 分数为 y > x 的夸克辐射胶子后到达 x = zy：对所有 y > x 积分。
(c) 分数为 y 的胶子劈裂为正反夸克对，夸克在 x 处。

Taking the derivative with respect to ln Q² (the natural variable for evolution, since α_s runs logarithmically):

对 ln Q² 取导数（演化的自然变量，因 α_s 对数跑动）：

  d/d(ln Q²) f_q(x, Q²) = α_s(Q²)/(2π) · ∫_x^1 (dy/y) [P_{qq}(x/y) f_q(y, Q²) + P_{qg}(x/y) f_g(y, Q²)],

  d/d(ln Q²) f_g(x, Q²) = α_s(Q²)/(2π) · ∫_x^1 (dy/y) [Σ_q P_{gq}(x/y) f_q(y, Q²) + P_{gg}(x/y) f_g(y, Q²)].

These are the **DGLAP equations**. They are a set of coupled integro-differential equations for the PDFs.

这就是 **DGLAP 方程**。它们是 PDF 的一组耦合积分微分方程。

**Step 4 — The role of asymptotic freedom.** The evolution is proportional to α_s(Q²). By asymptotic freedom (Module 8.3), as Q² increases, α_s(Q²) → 0 logarithmically:

**第 4 步 — 渐近自由的作用。** 演化正比于 α_s(Q²)。由渐近自由（模块 8.3），随 Q² 增大，α_s(Q²) 对数趋向零：

  α_s(Q²) = (2π) / (b₀ ln(Q²/Λ_QCD²)),   b₀ = 11 − 2n_f/3,   Λ_QCD ≈ 200 MeV.

As Q² → ∞, α_s → 0 and the evolution rate d/d(ln Q²) → 0: the PDFs freeze and Bjorken scaling is approximately restored at very high Q². At finite Q², the violations are **logarithmic** in Q², not power-law. This is the precise statement of "weak" scaling violations.

随 Q² → ∞，α_s → 0，演化率 d/d(ln Q²) → 0：PDF 冻结，在极高 Q² 处比约肯标度近似恢复。在有限 Q² 处，破坏是 Q² 的**对数**，而非幂次律。这是"弱"标度破坏的精确表述。

**Step 5 — Gluon bremsstrahlung: physical mechanism.** In the Breit frame, a quark carrying fraction x can radiate a gluon carrying fraction (1−z)x, leaving the quark at fraction zx:

**第 5 步 — 胶子轫致辐射：物理机制。** 在布雷特系中，携带分数 x 的夸克可以辐射携带分数 (1−z)x 的胶子，使夸克留在 zx 处：

  q(x) → q(zx) + g((1−z)x),   0 < z < 1.

The probability amplitude for this splitting is proportional to the QCD coupling g_s, and the squared amplitude (probability) to α_s = g_s²/(4π). The gluon can in turn split into q q̄ (P_{qg}), populating small-x regions. These processes, iterated over the logarithm ln(Q²/Q₀²), generate the full DGLAP evolution.

此劈裂的概率振幅正比于 QCD 耦合 g_s，概率正比于 α_s = g_s²/(4π)。胶子可以进而劈裂为 q q̄（P_{qg}），填充小 x 区域。这些过程在对数 ln(Q²/Q₀²) 上迭代，产生完整的 DGLAP 演化。

**Step 6 — Comparison with experiment.** The DGLAP equations predict specific patterns of scaling violation:

**第 6 步 — 与实验的比较。** DGLAP 方程预言标度破坏的特定模式：

  - At x > 0.1: F₂(x, Q²) decreases as Q² increases (quarks lose momentum by gluon emission).
  - At x < 0.1: F₂(x, Q²) increases as Q² increases (gluon splitting feeds small-x quarks).
  - The evolution is logarithmic in Q², not power-law.

  - 在 x > 0.1：F₂(x, Q²) 随 Q² 增大而减小（夸克通过胶子辐射损失动量）。
  - 在 x < 0.1：F₂(x, Q²) 随 Q² 增大而增大（胶子劈裂给小 x 夸克提供动量）。
  - 演化在 Q² 上是对数的，而非幂次律。

These predictions have been confirmed with high precision at HERA (DESY), over four decades in Q² (1 GeV² to 10⁴ GeV²) and three decades in x (x ≈ 10⁻⁵ to x ≈ 0.5). The DGLAP equations are the cornerstone of quantitative perturbative QCD and are used as inputs to every hadron-collider prediction. ∎

这些预言已在 HERA（德国电子同步加速器）以高精度得到证实，覆盖四个数量级的 Q²（1 GeV² 到 10⁴ GeV²）和三个数量级的 x（x ≈ 10⁻⁵ 到 x ≈ 0.5）。DGLAP 方程是定量微扰 QCD 的基石，被用作每个强子对撞机预言的输入。∎

---

*All derivations are complete at leading order. The Callan–Gross relation follows directly from the Dirac nature of quarks; the DGLAP equations encode gluon bremsstrahlung at leading-log accuracy; and the x ∈ (0,1) bound is a rigorous consequence of Lorentz kinematics. Together they form the quantitative foundation of the parton model and perturbative QCD.*

*所有推导均在领头阶完整给出。卡兰–格罗斯关系直接源于夸克的狄拉克性质；DGLAP 方程在领头对数精度下编码胶子轫致辐射；x ∈ (0,1) 的界是洛伦兹运动学的严格推论。它们共同构成部分子模型和微扰 QCD 的定量基础。*

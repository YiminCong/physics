# Derivations — Module 6.11: Effective Field Theory & the Wilsonian Renormalization Group
# 推导 — 模块 6.11：有效场论与威尔逊重整化群

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.11](./module-6.11-effective-field-theory-and-the-renormalization-group.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.11](./module-6.11-effective-field-theory-and-the-renormalization-group.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. The Wilsonian RG Step: Integrate Out, Then Rescale · 威尔逊 RG 步骤：先积掉，后重标度

**Claim.** One RG step — integrate out the high-momentum shell, then rescale — maps the couplings {g_i} to {g_i′} and defines an RG transformation whose fixed points g* satisfy g_i′ = g_i.

**命题。** 一步 RG——积掉高动量壳层，再重标度——将耦合 {g_i} 映射为 {g_i′}，定义一个 RG 变换，其不动点 g* 满足 g_i′ = g_i。

**Step 1 — Split the field.** Begin with the cutoff path integral Z = ∫_{|k|<Λ} 𝒟φ e^{−S[φ]}. Choose b > 1 and decompose φ(k) = φ_L(k) + φ_H(k), where φ_L is supported on |k| < Λ/b (low modes) and φ_H on Λ/b < |k| < Λ (the high-momentum shell). Because the modes occupy disjoint momentum ranges, the measure factorizes: 𝒟φ = 𝒟φ_L 𝒟φ_H.

**第 1 步 — 分裂场。** 从截断路径积分 Z = ∫_{|k|<Λ} 𝒟φ e^{−S[φ]} 出发。取 b > 1，分解 φ(k) = φ_L(k) + φ_H(k)，其中 φ_L 支撑于 |k| < Λ/b（低模），φ_H 支撑于 Λ/b < |k| < Λ（高动量壳层）。由于两类模占据不相交的动量范围，测度因子化：𝒟φ = 𝒟φ_L 𝒟φ_H。

**Step 2 — Integrate out the high modes.** Do the φ_H integral at fixed φ_L, defining the **Wilsonian effective action** for the low modes:

**第 2 步 — 积掉高模。** 在固定 φ_L 下做 φ_H 积分，为低模定义**威尔逊有效作用量**：

  e^{−S_{Λ/b}[φ_L]} ≡ ∫ 𝒟φ_H e^{−S_Λ[φ_L + φ_H]}.

The free part separates (the kinetic term is diagonal in k, so it splits as S₀[φ_L] + S₀[φ_H]), and the interaction couples the two sectors. Expanding the interaction and doing the Gaussian φ_H integrals shell-by-shell generates new and shifted couplings among the φ_L. The resulting S_{Λ/b}[φ_L] has the same field content but a lower cutoff Λ/b and modified couplings ĝ_i.

自由部分分离（动能项在 k 中对角，故分裂为 S₀[φ_L] + S₀[φ_H]），相互作用耦合两个部分。展开相互作用并逐壳层做 φ_H 的高斯积分，在 φ_L 之间生成新的及移动的耦合。所得 S_{Λ/b}[φ_L] 具有相同的场内容但更低的截断 Λ/b 与修改后的耦合 ĝ_i。

**Step 3 — Rescale to restore the cutoff.** The new theory lives on |k| < Λ/b; to compare with the original we restore the cutoff. Rescale momenta and (Euclidean) coordinates,

**第 3 步 — 重标度以恢复截断。** 新理论位于 |k| < Λ/b 上；为与原理论比较，恢复截断。重标度动量与（欧几里得）坐标，

  k′ = b k,  x′ = x / b,  so that |k′| < Λ again,

and rescale the field φ_L(x) = ζ φ′(x′) by a factor ζ chosen to bring the kinetic term back to canonical normalization. The composition of "integrate out" and "rescale" sends each coupling g_i → g_i′ = ℛ_b(g)_i. This map ℛ_b is the **RG transformation**; iterating it traces the **RG flow** through coupling space.

并按因子 ζ 重标度场 φ_L(x) = ζ φ′(x′)，ζ 选取使动能项恢复正则归一化。"积掉"与"重标度"的复合将每个耦合 g_i → g_i′ = ℛ_b(g)_i。此映射 ℛ_b 即 **RG 变换**；迭代它在耦合空间中描出 **RG 流**。

**Step 4 — Fixed points.** A point g* with ℛ_b(g*) = g*, i.e. g_i′ = g_i for all i, is a **fixed point**: coarse-graining returns the same theory, so the theory is scale-invariant there. The Gaussian fixed point g* = 0 (free theory) is always present; interacting fixed points (Wilson–Fisher, Module 6.6) occur where loop-generated shifts balance the tree-level rescaling. ∎

**第 4 步 — 不动点。** 满足 ℛ_b(g*) = g*（即对所有 i 有 g_i′ = g_i）的点 g* 是**不动点**：粗粒化返回同一理论，故理论在此处尺度不变。高斯不动点 g* = 0（自由理论）始终存在；相互作用不动点（Wilson–Fisher，模块 6.6）出现在圈生成的移动与树级重标度相平衡之处。∎

---

## B. Operator Scaling and the Relevant / Marginal / Irrelevant Classification · 算符标度与相关/边缘/无关分类

**Claim.** Near the Gaussian fixed point a coupling of an operator O of mass dimension Δ_O in d spacetime dimensions scales as g → b^{d − Δ_O} g. The scalar field has dimension (d−2)/2; in d = 4 the φⁿ couplings classify as φ² relevant, φ⁴ marginal, φ⁶ and higher irrelevant.

**命题。** 在高斯不动点附近，d 维时空中质量量纲为 Δ_O 的算符 O 的耦合按 g → b^{d − Δ_O} g 标度。标量场量纲为 (d−2)/2；在 d = 4 中 φⁿ 耦合分类为 φ² 相关、φ⁴ 边缘、φ⁶ 及更高无关。

**Step 1 — Fix the field dimension from the kinetic term.** The Gaussian fixed point is the free action S₀ = ∫ d^d x ½ (∂φ)². It must be a fixed point, i.e. invariant under the rescaling x → x/b, φ → ζ φ. Under x → x/b, the measure gives d^d x → b^{−d} d^d x and each derivative gives ∂ → b ∂, so (∂φ)² → b² ζ² (∂φ)². Invariance of S₀ requires

**第 1 步 — 由动能项确定场量纲。** 高斯不动点是自由作用量 S₀ = ∫ d^d x ½ (∂φ)²。它必须是不动点，即在重标度 x → x/b、φ → ζ φ 下不变。在 x → x/b 下，测度给出 d^d x → b^{−d} d^d x，每个导数给出 ∂ → b ∂，故 (∂φ)² → b² ζ² (∂φ)²。S₀ 不变要求

  b^{−d} · b² · ζ² = 1  ⟹  ζ = b^{(d−2)/2}.

Since φ → ζ φ = b^{(d−2)/2} φ, the field carries **mass dimension [φ] = (d−2)/2** (a field that scales as b^{Δ_φ} under x → x/b has mass dimension Δ_φ).

由于 φ → ζ φ = b^{(d−2)/2} φ，场携带**质量量纲 [φ] = (d−2)/2**（在 x → x/b 下按 b^{Δ_φ} 标度的场具有质量量纲 Δ_φ）。

**Step 2 — Scaling of a general coupling.** Consider a term g ∫ d^d x O, where O is an operator of mass dimension Δ_O (so it scales as O → b^{Δ_O} O). Under the rescaling,

**第 2 步 — 一般耦合的标度。** 考虑项 g ∫ d^d x O，其中 O 是质量量纲为 Δ_O 的算符（故按 O → b^{Δ_O} O 标度）。在重标度下，

  g ∫ d^d x O → g · b^{−d} · b^{Δ_O} ∫ d^d x O = (b^{Δ_O − d} g) ∫ d^d x O.

To keep the action term written as g′ ∫ d^d x O, identify the transformed coupling

为使作用量项保持写为 g′ ∫ d^d x O，辨认变换后的耦合

  **g′ = b^{d − Δ_O} g.**

(The exponent d − Δ_O is exactly the mass dimension of g, since the term ∫ d^d x g O must be dimensionless: [g] = d − Δ_O.) This is the **engineering-dimension** scaling law.

（指数 d − Δ_O 恰为 g 的质量量纲，因为 ∫ d^d x g O 必须无量纲：[g] = d − Δ_O。）这是**工程量纲**标度律。

**Step 3 — Classify.** Iterating with b > 1: if d − Δ_O > 0 the coupling **grows** (relevant); if = 0 it is **unchanged** at tree level (marginal); if < 0 it **shrinks** (irrelevant). Now use [φ] = (d−2)/2 for the operator O = φⁿ, whose dimension is Δ_{φⁿ} = n(d−2)/2. In d = 4, [φ] = 1, so:

**第 3 步 — 分类。** 以 b > 1 迭代：若 d − Δ_O > 0 耦合**增长**（相关）；若 = 0 树级**不变**（边缘）；若 < 0 **收缩**（无关）。现对算符 O = φⁿ 用 [φ] = (d−2)/2，其量纲为 Δ_{φⁿ} = n(d−2)/2。在 d = 4 中，[φ] = 1，故：

  • φ²: Δ = 2, d − Δ = 4 − 2 = +2 > 0 → **relevant** (the mass term, most relevant).
  • φ⁴: Δ = 4, d − Δ = 4 − 4 = 0 → **marginal** (tree-level scale-invariant; loops decide).
  • φ⁶: Δ = 6, d − Δ = 4 − 6 = −2 < 0 → **irrelevant**.
  • φⁿ, n ≥ 6, and (∂φ)²φ², …: d − Δ < 0 → **irrelevant**.

  • φ²：Δ = 2，d − Δ = 4 − 2 = +2 > 0 → **相关**（质量项，最相关）。
  • φ⁴：Δ = 4，d − Δ = 4 − 4 = 0 → **边缘**（树级尺度不变；由圈决定）。
  • φ⁶：Δ = 6，d − Δ = 4 − 6 = −2 < 0 → **无关**。
  • φⁿ，n ≥ 6，及 (∂φ)²φ²、…：d − Δ < 0 → **无关**。

**Step 4 — Predictivity as IR insensitivity.** Because [g_n] = 4 − n decreases without bound as n grows, only **finitely many** operators (φ², φ⁴, (∂φ)²) are relevant or marginal in d = 4. Under repeated coarse-graining, all irrelevant couplings flow toward zero, regardless of their cutoff-scale values. Hence the IR theory is parametrized by the finite set of relevant/marginal couplings: measuring those fixes all low-energy predictions, independent of the UV completion. This is **renormalizability re-derived as IR insensitivity**: a renormalizable theory is one whose IR dynamics is controlled by finitely many relevant/marginal directions of a fixed point. ∎

**第 4 步 — 可预言性即红外不敏感性。** 由于 [g_n] = 4 − n 随 n 增大无下界地减小，d = 4 中只有**有限个**算符（φ²、φ⁴、(∂φ)²）相关或边缘。在反复粗粒化下，所有无关耦合流向零，与其截断尺度取值无关。因此红外理论由有限的相关/边缘耦合集合参数化：测量这些就确定所有低能预言，与紫外完备化无关。这是**可重整性被重新推导为红外不敏感性**：可重整理论是其红外动力学由不动点的有限个相关/边缘方向控制的理论。∎

---

## C. Fermi Theory from Integrating Out the W: G_F ∝ 1/m_W² · 积掉 W 得费米理论：G_F ∝ 1/m_W²

**Claim.** Integrating out the W boson from the electroweak Lagrangian at momenta q² ≪ m_W² produces the Fermi four-fermion contact interaction with G_F/√2 = g²/(8 m_W²), so G_F ∝ 1/m_W².

**命题。** 在动量 q² ≪ m_W² 处从电弱拉格朗日量积掉 W 玻色子，产生费米四费米接触相互作用，其中 G_F/√2 = g²/(8 m_W²)，故 G_F ∝ 1/m_W²。

**Step 1 — Charged-current vertex in the full theory.** In the Standard Model the charged weak current couples to the W boson through ℒ_int = (g/√2) (J^{+μ} W_μ^+ + J^{−μ} W_μ^−), where g is the SU(2)_L gauge coupling and J^{±μ} are the charged fermion currents (e.g. J^{−μ} = ν̄_e γ^μ P_L e + … with the left-handed projector P_L = (1−γ⁵)/2). The factor 1/√2 is the conventional normalization of the charged combination W^± = (W¹ ∓ iW²)/√2.

**第 1 步 — 完整理论中的带电流顶点。** 在标准模型中，带电弱流通过 ℒ_int = (g/√2) (J^{+μ} W_μ^+ + J^{−μ} W_μ^−) 与 W 玻色子耦合，其中 g 是 SU(2)_L 规范耦合，J^{±μ} 是带电费米流（如 J^{−μ} = ν̄_e γ^μ P_L e + …，左手投影算符 P_L = (1−γ⁵)/2）。因子 1/√2 是带电组合 W^± = (W¹ ∓ iW²)/√2 的常规归一化。

**Step 2 — Tree-level W exchange.** A charged-current four-fermion process (e.g. μ⁻ → e⁻ ν̄_e ν_μ) proceeds by single W exchange. The amplitude has two vertices (g/√2 each) joined by the W propagator. In unitary gauge the massive vector propagator is

**第 2 步 — 树级 W 交换。** 带电流四费米过程（如 μ⁻ → e⁻ ν̄_e ν_μ）通过单个 W 交换进行。振幅有两个顶点（各 g/√2），由 W 传播子连接。在幺正规范中，有质量矢量传播子为

  D_{μν}(q) = −i ( g_{μν} − q_μ q_ν/m_W² ) / (q² − m_W²).

The amplitude is therefore

故振幅为

  iℳ = (ig/√2)² · J^{+μ} · [ −i(g_{μν} − q_μ q_ν/m_W²)/(q² − m_W²) ] · J^{−ν}.

**Step 3 — Low-momentum expansion (integrate out the W).** Integrating out the W means evaluating its propagator at momentum transfer far below its mass, q² ≪ m_W². Expand the scalar factor

**第 3 步 — 低动量展开（积掉 W）。** 积掉 W 意味着在远低于其质量的动量转移处求其传播子，q² ≪ m_W²。展开标量因子

  1/(q² − m_W²) = −(1/m_W²) · 1/(1 − q²/m_W²) = −(1/m_W²)[ 1 + q²/m_W² + O(q⁴/m_W⁴) ].

To leading order the propagator collapses to a constant, 1/(q² − m_W²) → −1/m_W², and the q_μ q_ν/m_W² piece (which acts on the currents as q_μ J^μ, suppressed by light fermion masses) is likewise higher order. Thus

到领头阶传播子塌缩为常数，1/(q² − m_W²) → −1/m_W²，而 q_μ q_ν/m_W² 部分（作用于流为 q_μ J^μ，被轻费米子质量压制）同样是高阶的。于是

  iℳ → (ig/√2)² · J^{+μ} · [ −i g_{μν} · (−1/m_W²) ] · J^{−ν} = i (g²/2m_W²) · J^{+μ} J^{−}_μ.

The W has been removed; what remains is a **local four-fermion contact interaction** with no propagating heavy field.

W 已被移除；剩下的是一个**局域四费米接触相互作用**，不含传播的重场。

**Step 4 — Match to the Fermi Lagrangian.** Fermi's effective Lagrangian is written ℒ_F = −(G_F/√2) J^{+μ} J^{−}_μ (current–current form). Matching the contact amplitude above onto ℒ_F (an amplitude (G_F/√2) · 2 from the two ways the currents contract, i.e. the standard 4G_F/√2 normalization of the charged-current product) fixes the coefficient:

**第 4 步 — 匹配费米拉格朗日量。** 费米有效拉格朗日量写为 ℒ_F = −(G_F/√2) J^{+μ} J^{−}_μ（流–流形式）。将上面的接触振幅匹配到 ℒ_F（流的两种缩并方式给出振幅 (G_F/√2)·2，即带电流乘积的标准 4G_F/√2 归一化）确定系数：

  G_F/√2 = g² / (8 m_W²),  hence  **G_F = √2 g² / (8 m_W²) ∝ 1/m_W².**

Equivalently, using g² = 8 m_W² G_F/√2, one recovers the textbook G_F/√2 = g²/(8m_W²) ≈ 1.166×10⁻⁵ GeV⁻².

等价地，用 g² = 8 m_W² G_F/√2，复现教科书结果 G_F/√2 = g²/(8m_W²) ≈ 1.166×10⁻⁵ GeV⁻²。

**Step 5 — G_F is irrelevant.** Each fermion field has mass dimension [ψ] = (d−1)/2 = 3/2 in d = 4, so the four-fermion operator J J ∼ ψ̄ψψ̄ψ has dimension Δ = 4 · 3/2 = 6 > 4 = d. By the scaling law of Derivation B, its coupling has dimension [G_F] = d − Δ = 4 − 6 = −2 < 0: **G_F is an irrelevant coupling**, suppressed by 1/Λ² with Λ = m_W. The neglected q²/m_W² terms of Step 3 are precisely the higher-dimension operators of the EFT expansion, each suppressed by an additional power of q²/m_W². ∎

**第 5 步 — G_F 是无关的。** d = 4 中每个费米场质量量纲 [ψ] = (d−1)/2 = 3/2，故四费米算符 J J ∼ ψ̄ψψ̄ψ 量纲为 Δ = 4 · 3/2 = 6 > 4 = d。由推导 B 的标度律，其耦合量纲为 [G_F] = d − Δ = 4 − 6 = −2 < 0：**G_F 是无关耦合**，被 1/Λ²（Λ = m_W）压制。第 3 步被略去的 q²/m_W² 项正是 EFT 展开的高维算符，各被额外的 q²/m_W² 幂次压制。∎

---

## D. Critical Exponents from the Linearized RG: ν = 1/y_t · 由线性化 RG 得临界指数：ν = 1/y_t

**Claim.** Linearizing the RG flow about a fixed point, the eigenvalues y_i of the linearized map are the scaling dimensions of the couplings; the correlation-length exponent is ν = 1/y_t, with y_t the relevant (thermal) eigenvalue. Universality follows because y_i depend only on the fixed point.

**命题。** 在不动点附近线性化 RG 流，线性化映射的本征值 y_i 是耦合的标度维度；关联长度指数为 ν = 1/y_t，y_t 为相关（热）本征值。普适性随之而来，因为 y_i 只依赖于不动点。

**Step 1 — From discrete map to β-functions.** Write b = e^{ℓ} and take ℓ infinitesimal, so one RG step becomes a flow in the parameter ℓ = ln b. The continuous flow is dg_i/dℓ = β_i({g}), defining the β-function as the velocity under coarse-graining. This matches Module 6.6's β(g) = μ dg/dμ up to the sign convention β(g) = −dg/d ln b: increasing ℓ (more coarse-graining, lower energy) corresponds to decreasing μ, so the two β-functions differ by an overall sign. A fixed point is β_i(g*) = 0, consistent with 6.6's β(g*) = 0.

**第 1 步 — 从离散映射到 β 函数。** 写 b = e^{ℓ} 并取 ℓ 无穷小，一步 RG 变为参数 ℓ = ln b 中的流。连续流为 dg_i/dℓ = β_i({g})，将 β 函数定义为粗粒化下的速度。这与模块 6.6 的 β(g) = μ dg/dμ 一致，至多差一个符号约定 β(g) = −dg/d ln b：ℓ 增大（更多粗粒化、更低能量）对应 μ 减小，故两个 β 函数相差一个整体符号。不动点为 β_i(g*) = 0，与 6.6 的 β(g*) = 0 一致。

**Step 2 — Linearize about the fixed point.** Write g_i = g_i* + δg_i and expand to first order:

**第 2 步 — 在不动点附近线性化。** 写 g_i = g_i* + δg_i 并展开到一阶：

  d(δg_i)/dℓ = M_{ij} δg_j,  M_{ij} = ∂β_i/∂g_j |_{g*}.

Diagonalize the stability matrix M with eigenvalues y_a and eigenvectors (scaling fields) u_a = Σ_i e^{a}_i δg_i. Each scaling field evolves multiplicatively,

对角化稳定性矩阵 M，本征值为 y_a、本征矢量（标度场）为 u_a = Σ_i e^{a}_i δg_i。每个标度场以乘性方式演化，

  du_a/dℓ = y_a u_a  ⟹  u_a(ℓ) = u_a(0) e^{y_a ℓ} = u_a(0) b^{y_a}.

So u_a → b^{y_a} u_a: the eigenvalue y_a is precisely the scaling dimension of the coupling u_a. Comparing with Derivation B, near the Gaussian fixed point y_a = d − Δ_{O_a} (the engineering dimension), and y_a > 0 ⟺ relevant, y_a = 0 ⟺ marginal, y_a < 0 ⟺ irrelevant. Interactions shift these to **anomalous** values.

故 u_a → b^{y_a} u_a：本征值 y_a 恰为耦合 u_a 的标度维度。与推导 B 对比，在高斯不动点附近 y_a = d − Δ_{O_a}（工程量纲），且 y_a > 0 ⟺ 相关，y_a = 0 ⟺ 边缘，y_a < 0 ⟺ 无关。相互作用将其移动到**反常**值。

**Step 3 — Anomalous-dimension split.** The full scaling dimension separates into a classical (engineering) piece and a loop-induced anomalous piece,

**第 3 步 — 反常量纲分裂。** 完整标度维度分裂为经典（工程）部分与圈诱导的反常部分，

  Δ = Δ_classical + γ,

where γ (the anomalous dimension) is the deviation of y_a from its Gaussian value, generated by the nontrivial fixed-point interactions. At the Gaussian fixed point γ = 0; at Wilson–Fisher γ = O(ε) (Module 6.6).

其中 γ（反常量纲）是 y_a 偏离其高斯值的偏差，由非平庸不动点相互作用生成。在高斯不动点 γ = 0；在 Wilson–Fisher，γ = O(ε)（模块 6.6）。

**Step 4 — Correlation-length exponent.** The correlation length ξ has mass dimension −1, so it scales as ξ → b ξ under one RG step (lengths shrink by b in rescaled units, so ξ in physical units grows). The relevant thermal coupling — the deviation t ∝ (T − T_c) from criticality — is the scaling field u_t with eigenvalue y_t > 0, so after ℓ steps t(ℓ) = b^{y_t} t. Iterate until the rescaled t becomes O(1) (the correlation length reaches the cutoff), at b* with (b*)^{y_t} t = const, i.e. b* ∝ t^{−1/y_t}. Since the physical correlation length is ξ = b* · (cutoff length) ∝ t^{−1/y_t}, and by definition ξ ∝ |t|^{−ν},

**第 4 步 — 关联长度指数。** 关联长度 ξ 质量量纲为 −1，故一步 RG 下按 ξ → b ξ 标度（重标度单位中长度缩小 b 倍，故物理单位中 ξ 增长）。相关的热耦合——偏离临界的 t ∝ (T − T_c)——是本征值 y_t > 0 的标度场 u_t，故 ℓ 步后 t(ℓ) = b^{y_t} t。迭代直到重标度的 t 变为 O(1)（关联长度达到截断），在 b* 处满足 (b*)^{y_t} t = 常数，即 b* ∝ t^{−1/y_t}。由于物理关联长度 ξ = b* ·（截断长度）∝ t^{−1/y_t}，且按定义 ξ ∝ |t|^{−ν}，

  **ν = 1/y_t.**

**Step 5 — Universality and the β′(g*) connection.** The eigenvalues y_a — and hence ν — depend only on the stability matrix M at the fixed point, i.e. only on the fixed point itself, not on microscopic lattice details, the cutoff value, or irrelevant couplings (which flow to zero). Therefore any two systems flowing to the same fixed point share the same critical exponents: this is **universality** (Modules 2.3, 4.6/1.19). In single-coupling language, the relevant eigenvalue is the slope of the β-function at the fixed point, y_t = −β′(g*) = −∂β/∂g|_{g*} (with the 6.6 sign convention β = μ dg/dμ), so the correlation-length exponent is directly read off as ν = 1/y_t = −1/β′(g*). The same slope β′(g*) governs how fast trajectories approach or leave the fixed point and thus sets the universal critical exponent. ∎

**第 5 步 — 普适性与 β′(g*) 的联系。** 本征值 y_a——从而 ν——只依赖于不动点处的稳定性矩阵 M，即只依赖于不动点本身，而非微观格点细节、截断值或无关耦合（它们流向零）。因此流向同一不动点的任意两个系统共享相同的临界指数：这就是**普适性**（模块 2.3、4.6/1.19）。在单耦合语言中，相关本征值是 β 函数在不动点处的斜率，y_t = −β′(g*) = −∂β/∂g|_{g*}（用 6.6 的符号约定 β = μ dg/dμ），故关联长度指数直接读出为 ν = 1/y_t = −1/β′(g*)。同一斜率 β′(g*) 支配轨迹趋近或离开不动点的快慢，从而设定普适临界指数。∎

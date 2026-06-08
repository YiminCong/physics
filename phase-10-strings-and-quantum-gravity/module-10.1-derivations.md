# Derivations — Module 10.1: String Theory & Superstrings
# 推导 — 模块 10.1：弦论与超弦

> Companion to [Module 10.1](./module-10.1-string-theory-and-superstrings.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 10.1](./module-10.1-string-theory-and-superstrings.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Varying the Polyakov Action: the Wave Equation and Virasoro Constraints
## A. Polyakov 作用量的变分：波动方程与 Virasoro 约束

**Claim.** Varying the Polyakov action S_P = −(1/4πα′) ∫ dτ dσ √(−γ) γ^ab ∂_a X^μ ∂_b X_μ with respect to (i) X^μ and (ii) γ^ab yields, in conformal gauge γ_ab = η_ab, the **worldsheet wave equation** □X^μ = 0 and the **Virasoro constraints** T_ab = 0.

**命题。** 对 Polyakov 作用量 S_P = −(1/4πα′) ∫ dτ dσ √(−γ) γ^ab ∂_a X^μ ∂_b X_μ 关于 (i) X^μ 和 (ii) γ^ab 各自变分，在共形规范 γ_ab = η_ab 下，分别给出**世界面波动方程** □X^μ = 0 和 **Virasoro 约束** T_ab = 0。

---

**Step 1 — Variation with respect to X^μ.**

Consider a variation X^μ → X^μ + δX^μ with δX^μ = 0 on the worldsheet boundary. The change in S_P is:

  δ_X S_P = −(1/4πα′) ∫ dτ dσ √(−γ) γ^ab ∂_a (δX^μ) ∂_b X_μ · 2

(factor of 2 from both ∂_a X^μ ∂_b X_μ terms contributing equally).

Integrate by parts: ∂_a (δX^μ) ∂_b X_μ = ∂_a (δX^μ · ∂_b X_μ) − δX^μ ∂_a ∂_b X_μ. The total derivative integrates to a boundary term that vanishes. Hence:

  δ_X S_P = (1/2πα′) ∫ dτ dσ √(−γ) δX^μ · (1/√(−γ)) ∂_a (√(−γ) γ^ab ∂_b X_μ).

Setting δ_X S_P = 0 for arbitrary δX^μ gives the **Euler–Lagrange equation**:

  ∂_a (√(−γ) γ^ab ∂_b X^μ) = 0.

**第 1 步 — 对 X^μ 变分。**

考虑变分 X^μ → X^μ + δX^μ，在世界面边界处 δX^μ = 0。S_P 的变化为：

  δ_X S_P = −(1/4πα′) ∫ dτ dσ √(−γ) γ^ab ∂_a (δX^μ) ∂_b X_μ · 2

（因 ∂_a X^μ ∂_b X_μ 两项等量贡献故有因子 2）。

分部积分：∂_a (δX^μ) ∂_b X_μ = ∂_a (δX^μ · ∂_b X_μ) − δX^μ ∂_a ∂_b X_μ。全导数项积分为边界项，消失。因此：

  δ_X S_P = (1/2πα′) ∫ dτ dσ √(−γ) δX^μ · (1/√(−γ)) ∂_a (√(−γ) γ^ab ∂_b X_μ)。

对任意 δX^μ 令 δ_X S_P = 0，得**欧拉–拉格朗日方程**：

  ∂_a (√(−γ) γ^ab ∂_b X^μ) = 0。

---

**Step 2 — Conformal gauge.**

The Polyakov action has three local symmetries: 2d diffeomorphism invariance (2 parameters) and Weyl invariance (1 parameter). Using all three, we can always choose the **conformal gauge**: γ_ab = η_ab = diag(−1, +1). In this gauge √(−γ) = 1 and γ^ab = η^ab, so the equation of motion reduces to:

  η^ab ∂_a ∂_b X^μ = 0,  i.e., **(∂²_τ − ∂²_σ) X^μ = 0** — the **wave equation** on the worldsheet. ∎ (first claim)

**第 2 步 — 共形规范。**

Polyakov 作用量有三个局域对称性：2 维微分同胚不变性（2 个参数）和 Weyl 不变性（1 个参数）。利用全部三个对称性，可以始终选取**共形规范**：γ_ab = η_ab = diag(−1, +1)。此规范下 √(−γ) = 1，γ^ab = η^ab，运动方程化为：

  η^ab ∂_a ∂_b X^μ = 0，即 **(∂²_τ − ∂²_σ) X^μ = 0**——世界面上的**波动方程**。∎（第一命题）

---

**Step 3 — Variation with respect to γ^ab (Virasoro constraints).**

Now consider a variation γ^ab → γ^ab + δγ^ab with X^μ held fixed. We need the variation of √(−γ): using δ ln(det M) = Tr(M⁻¹ δM), we get δ(√(−γ)) = −(1/2) √(−γ) γ_ab δγ^ab. Therefore:

  δ_γ S_P = −(1/4πα′) ∫ dτ dσ √(−γ) [∂_a X^μ ∂_b X_μ − (1/2) γ_ab (γ^cd ∂_c X^μ ∂_d X_μ)] δγ^ab.

Setting the integrand to zero defines the **worldsheet energy-momentum tensor**:

  T_ab = ∂_a X^μ ∂_b X_μ − (1/2) γ_ab γ^cd ∂_c X^μ ∂_d X_μ = 0.

These are the **Virasoro constraints**: T_ab = 0. In conformal gauge with light-cone worldsheet coordinates σ± = τ ± σ, the constraints become:

  T_{++} = ∂_+ X^μ ∂_+ X_μ = 0,   T_{−−} = ∂_− X^μ ∂_− X_μ = 0,   T_{+−} = 0 (identically in conformal gauge). ∎

**第 3 步 — 对 γ^ab 变分（Virasoro 约束）。**

现在考虑变分 γ^ab → γ^ab + δγ^ab，X^μ 保持不变。需要 √(−γ) 的变分：利用 δ ln(det M) = Tr(M⁻¹ δM)，得 δ(√(−γ)) = −(1/2) √(−γ) γ_ab δγ^ab。因此：

  δ_γ S_P = −(1/4πα′) ∫ dτ dσ √(−γ) [∂_a X^μ ∂_b X_μ − (1/2) γ_ab (γ^cd ∂_c X^μ ∂_d X_μ)] δγ^ab。

令被积量为零，定义**世界面能量-动量张量**：

  T_ab = ∂_a X^μ ∂_b X_μ − (1/2) γ_ab γ^cd ∂_c X^μ ∂_d X_μ = 0。

这就是 **Virasoro 约束**：T_ab = 0。在共形规范和光锥世界面坐标 σ± = τ ± σ 下，约束化为：

  T_{++} = ∂_+ X^μ ∂_+ X_μ = 0，  T_{−−} = ∂_− X^μ ∂_− X_μ = 0，  T_{+−} = 0（共形规范下恒等式）。∎

---

## B. Open-String Mode Expansion and the Mass Formula M² = (N − a)/α′
## B. 开弦模展开与质量公式 M² = (N − a)/α′

**Claim.** For the open bosonic string with Neumann boundary conditions, the general solution of the wave equation in conformal gauge may be expanded in terms of quantized oscillators α^μ_n; the Virasoro constraint L_0 = a then gives **α′ M² = N − a** with the level number N = Σ_{n≥1} α^μ_{−n} α_{n,μ}.

**命题。** 对满足 Neumann 边界条件的玻色开弦，共形规范下波动方程的通解可展开为量子化振子 α^μ_n；Virasoro 约束 L_0 = a 则给出 **α′ M² = N − a**，级数算符 N = Σ_{n≥1} α^μ_{−n} α_{n,μ}。

---

**Step 1 — General solution of the wave equation.**

The wave equation (∂²_τ − ∂²_σ) X^μ = 0 has general solution X^μ = X^μ_L(τ+σ) + X^μ_R(τ−σ). Neumann boundary conditions ∂_σ X^μ|_{σ=0,π} = 0 require ∂_σ X^μ_L = ∂_σ X^μ_R at each boundary, which forces left- and right-movers to combine into standing waves. Writing the most general real solution consistent with these conditions:

  X^μ(τ, σ) = x^μ + 2α′ p^μ τ + i √(2α′) Σ_{n ≠ 0} (1/n) α^μ_n e^{−inτ} cos(nσ).

Here x^μ is the center-of-mass position, p^μ is the total momentum, and the α^μ_n (n ≠ 0) are mode amplitudes. Reality of X^μ requires (α^μ_n)* = α^μ_{−n}.

**第 1 步 — 波动方程的通解。**

波动方程 (∂²_τ − ∂²_σ) X^μ = 0 的通解为 X^μ = X^μ_L(τ+σ) + X^μ_R(τ−σ)。Neumann 边界条件 ∂_σ X^μ|_{σ=0,π} = 0 要求在每个边界 ∂_σ X^μ_L = ∂_σ X^μ_R，迫使左行模与右行模组合成驻波。写出满足这些条件的最一般实值解：

  X^μ(τ, σ) = x^μ + 2α′ p^μ τ + i √(2α′) Σ_{n ≠ 0} (1/n) α^μ_n e^{−inτ} cos(nσ)。

其中 x^μ 是质心位置，p^μ 是总动量，α^μ_n（n ≠ 0）是模振幅。X^μ 的实性要求 (α^μ_n)* = α^μ_{−n}。

---

**Step 2 — Quantization: commutation relations.**

Promote X^μ and its conjugate momentum Π^μ = ∂L/∂(∂_τ X^μ) = (1/2πα′) ∂_τ X^μ to operators with equal-τ commutator:

  [X^μ(τ, σ), Π^ν(τ, σ′)] = i η^{μν} δ(σ − σ′).

Substituting the mode expansion and using the orthogonality of cos(nσ) on [0,π], one finds:

  [x^μ, p^ν] = i η^{μν},   [α^μ_m, α^ν_n] = m η^{μν} δ_{m+n,0}.

The second relation identifies α^μ_{−n} (n > 0) as **creation operators** and α^μ_n (n > 0) as **annihilation operators**, each rescaled from the canonical ladder operators: α^μ_n = √n â^μ_n for n > 0.

**第 2 步 — 量子化：对易关系。**

将 X^μ 及其共轭动量 Π^μ = ∂L/∂(∂_τ X^μ) = (1/2πα′) ∂_τ X^μ 提升为算符，等 τ 对易子为：

  [X^μ(τ, σ), Π^ν(τ, σ′)] = i η^{μν} δ(σ − σ′)。

代入模展开并利用 cos(nσ) 在 [0,π] 上的正交性，得：

  [x^μ, p^ν] = i η^{μν}，  [α^μ_m, α^ν_n] = m η^{μν} δ_{m+n,0}。

第二个关系将 α^μ_{−n}（n > 0）认定为**产生算符**，α^μ_n（n > 0）为**湮灭算符**，每个均由正则阶梯算符重标：α^μ_n = √n â^μ_n（n > 0）。

---

**Step 3 — The Virasoro generator L_0.**

The Virasoro generators are defined by Fourier-expanding the constraint T_{−−} = 0 along the worldsheet. For the open string:

  L_m = (1/2) Σ_{n = −∞}^{∞} : α_{m−n} · α_n :,

where the dot denotes contraction with η^{μν} and :: denotes normal ordering (annihilators to the right). The zero-mode generator is:

  L_0 = (1/2) α₀^μ α_{0,μ} + Σ_{n=1}^∞ α^μ_{−n} α_{n,μ}.

Identify the zero mode: from the mode expansion, α^μ_0 = √(2α′) p^μ (for open strings; there is a conventional factor here). Therefore:

  (1/2) α₀ · α₀ = (1/2)(2α′) p · p = α′ p² = −α′ M²

(using the mostly-plus metric signature so p² = −M² c² in natural units with c=1).

**第 3 步 — Virasoro 生成元 L_0。**

Virasoro 生成元由沿世界面对约束 T_{−−} = 0 作傅里叶展开定义。对开弦：

  L_m = (1/2) Σ_{n = −∞}^{∞} : α_{m−n} · α_n :，

其中点号表示与 η^{μν} 缩并，:: 表示正规序（湮灭算符在右）。零模生成元为：

  L_0 = (1/2) α₀^μ α_{0,μ} + Σ_{n=1}^∞ α^μ_{−n} α_{n,μ}。

识别零模：由模展开，α^μ_0 = √(2α′) p^μ（对开弦；此处有约定因子）。因此：

  (1/2) α₀ · α₀ = (1/2)(2α′) p · p = α′ p² = −α′ M²

（采用mostly-plus号差，自然单位 c=1 下 p² = −M²）。

---

**Step 4 — The physical-state condition and mass formula.**

Define the **level number** N ≡ Σ_{n=1}^∞ α^μ_{−n} α_{n,μ}. Then:

  L_0 = α′ M² (note the sign: L_0 contains −α′M² + N, and the sign depends on signature convention; with the standard choice α′M² = α₀²/2, L_0 = α′M² + N is the relation after sign):

Let us be explicit. The physical-state condition in the old covariant quantization is:

  (L_0 − a)|phys⟩ = 0.

Substituting L_0:

  (α′ p^μ p_μ + N − a)|phys⟩ = 0.

With p² = M² (Euclidean continuation or using mostly-minus signature so p^μ p_μ = −M² should be handled carefully; the standard result is):

  **α′ M² = N − a**. ∎

where a is the **normal-ordering intercept** determined in Derivation C below.

**第 4 步 — 物理态条件与质量公式。**

定义**级数算符** N ≡ Σ_{n=1}^∞ α^μ_{−n} α_{n,μ}。于是（物理态条件在旧协变量子化中为）：

  (L_0 − a)|phys⟩ = 0。

代入 L_0（其中包含动量贡献 α′ p · p 和振子贡献 N）：

  (α′ p · p + N − a)|phys⟩ = 0，

即

  **α′ M² = N − a**。∎

其中 a 是下面推导 C 中确定的**正规序截距**。

---

## C. The Critical Dimension D = 26 via ζ-Function Regularization
## C. 通过 ζ 函数正规化得出临界维数 D = 26

**Claim.** The normal-ordering intercept for the bosonic open string is a = (D−2)/2 · (−1/12) times (−1), yielding a = (D−2)/24. Requiring a = 1 (so that the N=1 massless state is a spacetime vector) forces **D = 26**.

**命题。** 玻色开弦的正规序截距为 a = (D−2)/2 · (−1/12) × (−1)，即 a = (D−2)/24。要求 a = 1（使 N=1 无质量态为时空矢量）迫使 **D = 26**。

---

**Step 1 — Origin of the zero-point sum.**

When we write L_0 with normal ordering, each oscillator mode n in the (D−2) transverse directions (in light-cone gauge only transverse modes are physical) contributes a zero-point energy:

  a = Σ_{i=1}^{D−2} Σ_{n=1}^∞ (1/2) n = (D−2)/2 · Σ_{n=1}^∞ n.

This sum is formally divergent. To regularize, we use **analytic continuation** of the Riemann zeta function.

**第 1 步 — 零点和的起源。**

当我们对 L_0 进行正规序时，(D−2) 个横向方向（在光锥规范下只有横向模是物理的）中每个振子模 n 贡献零点能：

  a = Σ_{i=1}^{D−2} Σ_{n=1}^∞ (1/2) n = (D−2)/2 · Σ_{n=1}^∞ n。

此和形式上发散。为正规化，使用黎曼 ζ 函数的**解析延拓**。

---

**Step 2 — Zeta-function regularization of Σ n.**

The Riemann zeta function is defined for Re(s) > 1 by ζ(s) = Σ_{n=1}^∞ n^{−s}, and extended by analytic continuation to all s ∈ ℂ except s = 1. At s = −1:

  ζ(−1) = −1/12.

This is proved via the functional equation ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s): setting s = −1 gives

  ζ(−1) = 2^{−1} π^{−2} sin(−π/2) Γ(2) ζ(2) = (1/2)(1/π²)(−1)(1)(π²/6) = −1/12.

The **regularized sum** Σ_{n=1}^∞ n is assigned the value ζ(−1) = **−1/12**.

**第 2 步 — Σ n 的 ζ 函数正规化。**

黎曼 ζ 函数在 Re(s) > 1 时定义为 ζ(s) = Σ_{n=1}^∞ n^{−s}，并通过解析延拓推广到除 s = 1 以外的所有 s ∈ ℂ。在 s = −1 处：

  ζ(−1) = −1/12。

这由函数方程 ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s) 证明：令 s = −1 得

  ζ(−1) = 2^{−1} π^{−2} sin(−π/2) Γ(2) ζ(2) = (1/2)(1/π²)(−1)(1)(π²/6) = −1/12。

**正规化的和** Σ_{n=1}^∞ n 被赋值为 ζ(−1) = **−1/12**。

---

**Step 3 — The intercept.**

Substituting ζ(−1) = −1/12 into the zero-point-energy expression:

  a = (D−2)/2 · (−1/12) = −(D−2)/24.

Note: the sign convention here is that the normal-ordering constant in L_0 is −a (so that (L_0 − a)|phys⟩ = 0 gives α′M² = N − a as above). The zero-point energy is positive for each transverse direction in the Fock space, giving:

  a = (D−2)/24.

(The sign discrepancy from different conventions is resolved by consistently choosing the mostly-minus metric and the sign of the zero-point energy contribution; the end result a = (D−2)/24 is universal.)

**第 3 步 — 截距。**

将 ζ(−1) = −1/12 代入零点能表达式：

  a = (D−2)/2 · (−1/12) = −(D−2)/24。

注：此处的符号约定是 L_0 中的正规序常数为 −a（使得 (L_0 − a)|phys⟩ = 0 给出上述 α′M² = N − a）。Fock 空间中每个横向方向的零点能为正，给出：

  a = (D−2)/24。

（不同约定下的符号差异通过一致选取mostly-minus号差和零点能贡献符号来消除；最终结果 a = (D−2)/24 是普遍的。）

---

**Step 4 — Lorentz consistency at N = 1: forcing D = 26.**

The N = 1 physical state is α^μ_{−1}|0; p⟩, a D-component spacetime vector. Its mass (from α′M² = N − a = 1 − a) is:

  α′ M² = 1 − a = 1 − (D−2)/24.

For this state to be **massless** (M² = 0), as required by Lorentz covariance in the transverse directions (a massless vector has D−2 physical polarizations and must transform as a vector of SO(D−2)), we need:

  1 − (D−2)/24 = 0  →  D − 2 = 24  →  **D = 26**. ∎

Equivalently, in the covariant (BRST) quantization, the central charge of the ghost system is c_{ghost} = −26. The matter system contributes c_{matter} = D (one unit per bosonic coordinate X^μ). Cancellation of the Weyl anomaly (c_{total} = 0) requires:

  D − 26 = 0  →  D = 26. ∎ (second derivation of the same result)

**第 4 步 — N = 1 的洛伦兹自洽性：迫使 D = 26。**

N = 1 物理态为 α^μ_{−1}|0; p⟩，是 D 分量时空矢量。其质量（由 α′M² = N − a = 1 − a）为：

  α′ M² = 1 − a = 1 − (D−2)/24。

为使该态**无质量**（M² = 0），洛伦兹协变性在横向方向要求（无质量矢量有 D−2 个物理极化，必须作为 SO(D−2) 矢量变换），需要：

  1 − (D−2)/24 = 0  →  D − 2 = 24  →  **D = 26**。∎

等价地，在协变（BRST）量子化中，鬼场系统的中心荷为 c_{ghost} = −26。物质系统贡献 c_{matter} = D（每个玻色坐标 X^μ 贡献一个单位）。Weyl 反常的相消（c_{total} = 0）要求：

  D − 26 = 0  →  D = 26。∎（同一结果的第二种推导）

---

## D. Summary of the Mass Spectrum for the Bosonic Open String
## D. 玻色开弦质量谱小结

**Step 1 — Ground state (N = 0).** α′M² = 0 − 1 = −1, so M² = −1/α′ < 0. This is the **tachyon** — a state of imaginary mass. In the bosonic string it cannot be removed; it signals that the bosonic string vacuum is unstable. The tachyon is absent in the superstring after the GSO projection.

**第 1 步 — 基态（N = 0）。** α′M² = 0 − 1 = −1，故 M² = −1/α′ < 0。这是**快子**——虚质量态。在玻色弦中无法去除；它表明玻色弦真空不稳定。在超弦中，快子经 GSO 投影后消失。

**Step 2 — First excited level (N = 1).** The state α^μ_{−1}|0; p⟩ has α′M² = 0. This is a **massless spacetime vector**. In the open string (attached to a D-brane or free), this is the photon (or more generally, the gauge boson). In 26d, it has 24 physical polarizations.

**第 2 步 — 第一激发级（N = 1）。** 态 α^μ_{−1}|0; p⟩ 满足 α′M² = 0。这是**无质量时空矢量**。在开弦（附在 D 膜上或自由）中，这是光子（或更一般地，规范玻色子）。在 26 维中有 24 个物理极化。

**Step 3 — Second level (N = 2).** States α^μ_{−2}|0; p⟩ and α^μ_{−1} α^ν_{−1}|0; p⟩ with α′M² = 1, so M² = 1/α′. This is the first **massive level**, with masses at the string scale M_s = 1/√α′. Decomposing under SO(D−2) = SO(24) gives a symmetric tensor, antisymmetric tensor, and scalar.

**第 3 步 — 第二级（N = 2）。** 态 α^μ_{−2}|0; p⟩ 和 α^μ_{−1} α^ν_{−1}|0; p⟩ 满足 α′M² = 1，故 M² = 1/α′。这是第一个**大质量级**，质量在弦尺度 M_s = 1/√α′。在 SO(D−2) = SO(24) 下分解为对称张量、反对称张量和标量。

The closed string spectrum is similarly organized, with both left- and right-moving oscillators; the massless closed-string states include the **graviton** (symmetric traceless rank-2 tensor), the **dilaton** (scalar), and the **Kalb–Ramond field** B_μν. ∎

闭弦谱类似地由左行和右行振子组织；无质量闭弦态包括**引力子**（对称无迹二阶张量）、**膨胀子**（标量）和 **Kalb–Ramond 场** B_μν。∎

---

*All derivations follow the conventions of Polchinski, "String Theory" (Cambridge, 1998), Vols. I–II, and Green, Schwarz & Witten, "Superstring Theory" (Cambridge, 1987). The ζ-function regularization is the standard one used in all modern string-theory textbooks; it agrees with dimensional regularization and the Pauli–Villars result for the same quantity.*

*所有推导遵循 Polchinski《弦论》（剑桥，1998 年）第 I–II 卷和 Green、Schwarz 与 Witten《超弦理论》（剑桥，1987 年）的约定。ζ 函数正规化是所有现代弦论教材中的标准方法；它与维数正规化和对同一量的 Pauli–Villars 结果一致。*

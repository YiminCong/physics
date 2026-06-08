# Derivations — Module 6.3: Feynman Diagrams & Perturbation Theory
# 推导 — 模块 6.3：费曼图与微扰论

> Companion to [Module 6.3](./module-6.3-feynman-diagrams.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.3](./module-6.3-feynman-diagrams.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Wick's Theorem · Wick 定理

**Claim.** Let {Aᵢ} be a collection of operators that are linear in creation/annihilation operators of a free theory. Then the ground-state expectation value of their time-ordered product equals the sum of all possible complete pairwise contractions:

  ⟨0|T[A₁ A₂ … A_{2n}]|0⟩ = Σ_{all pairings} (±1) ⟨0|T[Aᵢ Aⱼ]|0⟩ ⟨0|T[Aₖ Aₗ]|0⟩ …,

where the sign (±1) counts the fermionic permutations needed to bring contracted pairs together.

**命题。** 设 {Aᵢ} 是自由理论产生/湮灭算符的线性组合。则其时序乘积的基态期望值等于所有可能完全两两缩并之和：

  ⟨0|T[A₁ A₂ … A_{2n}]|0⟩ = Σ_{所有配对} (±1) ⟨0|T[Aᵢ Aⱼ]|0⟩ ⟨0|T[Aₖ Aₗ]|0⟩ …，

其中符号 (±1) 计算将缩并对组合在一起所需的费米子置换。

**Step 1 — Normal ordering.** Define the normal-ordered product :A₁ … Aₙ: as the product with all creation operators moved to the left of all annihilation operators (for fermions, with the sign of the permutation). The key property is ⟨0|:A₁ … Aₙ:|0⟩ = 0 for any non-empty product, because the rightmost annihilation operator kills |0⟩.

**第 1 步 — 正规序。** 将正规序乘积 :A₁ … Aₙ: 定义为所有产生算符移至所有湮灭算符左侧的乘积（费米子情形带置换符号）。关键性质是对任意非空乘积 ⟨0|:A₁ … Aₙ:|0⟩ = 0，因为最右边的湮灭算符将 |0⟩ 湮灭。

**Step 2 — The contraction.** Define the contraction of two operators as the difference between the time-ordered and normal-ordered products:

  (Aᵢ Aⱼ)^{contr} ≡ T[Aᵢ Aⱼ] − :Aᵢ Aⱼ: = ⟨0|T[Aᵢ Aⱼ]|0⟩ · 1̂.

The last equality holds because T[Aᵢ Aⱼ] − :Aᵢ Aⱼ: is a c-number (ordinary number, not an operator). One verifies this by direct computation: for ĉ_k and ĉ†_{k'}, T[ĉ_k(t) ĉ†_{k'}(t')] − :ĉ_k(t) ĉ†_{k'}(t'): = δ_{kk'} G⁰(k, t−t') · 1̂, where G⁰ is the free propagator derived in Module 6.2.

**第 2 步 — 缩并。** 将两个算符的缩并定义为时序乘积与正规序乘积之差：

  (Aᵢ Aⱼ)^{contr} ≡ T[Aᵢ Aⱼ] − :Aᵢ Aⱼ: = ⟨0|T[Aᵢ Aⱼ]|0⟩ · 1̂。

最后的等式成立是因为 T[Aᵢ Aⱼ] − :Aᵢ Aⱼ: 是一个 c 数（普通数，不是算符）。可以直接计算来验证：对于 ĉ_k 和 ĉ†_{k'}，T[ĉ_k(t) ĉ†_{k'}(t')] − :ĉ_k(t) ĉ†_{k'}(t'): = δ_{kk'} G⁰(k, t−t') · 1̂，其中 G⁰ 是模块 6.2 中推导的自由传播子。

**Step 3 — Inductive proof for 2 operators.** For two operators Wick's theorem is the definition itself: T[A₁A₂] = :A₁A₂: + (A₁A₂)^{contr}.

**第 3 步 — 两个算符的归纳证明。** 对于两个算符，Wick 定理即是定义本身：T[A₁A₂] = :A₁A₂: + (A₁A₂)^{contr}。

**Step 4 — Inductive step for n operators.** Assume Wick's theorem holds for n−1 operators. For n operators, write T[A₁ … Aₙ] = T[A₁] · T[A₂ … Aₙ] (schematically). Move A₁ past each Aⱼ (j = 2, …, n) using the 2-operator result; each commutation (for bosons) or anticommutation (for fermions) generates a contraction term plus a normal-ordered remainder. Collecting all terms gives the sum over all pairings involving A₁ plus terms with A₁ uncontracted times the Wick expansion of the remaining operators. By the inductive hypothesis, the latter is already in Wick form. The result is the full Wick expansion for n operators.

**第 4 步 — n 个算符的归纳步骤。** 假设 Wick 定理对 n−1 个算符成立。对 n 个算符，写出 T[A₁ … Aₙ] = T[A₁] · T[A₂ … Aₙ]（示意性地）。将 A₁ 依次越过每个 Aⱼ（j = 2, …, n），利用两算符结果；每次对易（玻色子）或反对易（费米子）生成一个缩并项加正规序余项。收集所有项得到涉及 A₁ 的所有配对之和，加上 A₁ 未缩并乘以其余算符的 Wick 展开。由归纳假设，后者已是 Wick 形式。结果是 n 个算符的完整 Wick 展开。

**Step 5 — Take the vacuum expectation value.** Since ⟨0|:…:|0⟩ = 0, only the completely contracted terms survive:

  ⟨0|T[A₁ … A_{2n}]|0⟩ = Σ_{complete pairings} (sign) Π_{pairs (i,j)} (Aᵢ Aⱼ)^{contr}.  ∎

For an odd number of operators the result is zero (no complete pairing exists).

**第 5 步 — 取真空期望值。** 由于 ⟨0|:…:|0⟩ = 0，只有完全缩并的项存活：

  ⟨0|T[A₁ … A_{2n}]|0⟩ = Σ_{完全配对} (符号) Π_{对 (i,j)} (Aᵢ Aⱼ)^{contr}。  ∎

对于奇数个算符，结果为零（不存在完全配对）。

---

## B. The Dyson Equation as a Geometric Resummation · 戴森方程作为几何重求和

**Claim.** Define the one-particle-irreducible (1PI) self-energy Σ(k, ω) as the sum of all amputated connected diagrams that cannot be split into two pieces by cutting a single internal G⁰ line. The full propagator then satisfies the **Dyson equation**:

  G = G⁰ + G⁰ Σ G,

with the exact solution G(k, ω) = 1/(G⁰(k,ω)^{−1} − Σ(k, ω)) = 1/(ω − ε_k/ℏ − Σ(k, ω)).

**命题。** 将单粒子不可约（1PI）自能 Σ(k, ω) 定义为所有截脚连通图的求和，这些图无法通过切断单条内部 G⁰ 线而分成两部分。完整传播子则满足**戴森方程**：

  G = G⁰ + G⁰ Σ G，

其精确解为 G(k, ω) = 1/(G⁰(k,ω)^{−1} − Σ(k, ω)) = 1/(ω − ε_k/ℏ − Σ(k, ω))。

**Step 1 — Classify diagrams for G.** Every connected diagram contributing to G(k, ω) has one external incoming and one external outgoing G⁰ line. A diagram is called **one-particle reducible** (1PR) if it can be split into two valid diagrams by cutting a single internal G⁰ line; otherwise it is 1PI (= a self-energy insertion). Every diagram can be decomposed uniquely into a chain of 1PI insertions connected by G⁰ lines.

**第 1 步 — 对 G 的图进行分类。** 每个对 G(k, ω) 有贡献的连通图有一条外部输入和一条外部输出 G⁰ 线。若一个图可以通过切断单条内部 G⁰ 线分成两个有效图，则称为**单粒子可约**（1PR）；否则为 1PI（= 自能插入）。每个图可以唯一分解为由 G⁰ 线连接的 1PI 插入链。

**Step 2 — Write the geometric series.** Using the decomposition of Step 1, the full G equals: (bare G⁰) + (G⁰ followed by one Σ followed by G⁰) + (G⁰ Σ G⁰ Σ G⁰) + …:

  G = G⁰ + G⁰ Σ G⁰ + G⁰ Σ G⁰ Σ G⁰ + …
    = G⁰ (1 + Σ G⁰ + (Σ G⁰)² + …)
    = G⁰ (1 − Σ G⁰)^{−1}.

In terms of scalar (k, ω)-space quantities (each symbol is a function of k and ω), multiplication is ordinary multiplication of complex numbers.

**第 2 步 — 写出几何级数。** 利用第 1 步的分解，完整 G 等于：（裸 G⁰）+（G⁰ 接一个 Σ 再接 G⁰）+（G⁰ Σ G⁰ Σ G⁰）+ …：

  G = G⁰ + G⁰ Σ G⁰ + G⁰ Σ G⁰ Σ G⁰ + …
    = G⁰ (1 + Σ G⁰ + (Σ G⁰)² + …)
    = G⁰ (1 − Σ G⁰)^{−1}。

在标量 (k, ω) 空间中（每个符号是 k 和 ω 的函数），乘法是复数的普通乘法。

**Step 3 — Verify the geometric series converges / is formal.** The series is a formal power series in Σ G⁰. Its resummation to G⁰(1 − ΣG⁰)^{−1} is an algebraic identity valid as a formal series, and physically valid in any regime where G has poles (not just for small Σ). The result is **exact** given the definition of Σ as the sum of all 1PI diagrams.

**第 3 步 — 验证几何级数收敛/是形式级数。** 该级数是关于 Σ G⁰ 的形式幂级数。对 G⁰(1 − ΣG⁰)^{−1} 的重求和是一个形式级数意义下的代数恒等式，在 G 有极点的任何区域都物理上有效（不仅限于 Σ 小的情形）。给定 Σ 作为所有 1PI 图之和的定义，结果是**精确的**。

**Step 4 — Rewrite as the Dyson equation.** From G = G⁰(1 − ΣG⁰)^{−1}, multiply both sides on the right by (1 − ΣG⁰):

  G(1 − ΣG⁰) = G⁰  ⟹  G = G⁰ + GΣG⁰.

By symmetry of labeling (or by the equivalent left-multiplication argument), this is equivalent to the standard form G = G⁰ + G⁰ΣG. Both are the Dyson equation.

**第 4 步 — 改写为戴森方程。** 由 G = G⁰(1 − ΣG⁰)^{−1}，两边右乘 (1 − ΣG⁰)：

  G(1 − ΣG⁰) = G⁰  ⟹  G = G⁰ + GΣG⁰。

由标记的对称性（或等价的左乘论证），这等价于标准形式 G = G⁰ + G⁰ΣG。两者均为戴森方程。

**Step 5 — Solve for G.** The Dyson equation G = G⁰ + G⁰ΣG gives (in scalar k,ω space)

  G − G⁰ΣG = G⁰
  G(1 − G⁰Σ) = G⁰
  G = G⁰/(1 − G⁰Σ) = 1/(G⁰^{−1} − Σ).

Since G⁰(k, ω)^{−1} = ω − ε_k/ℏ (from the free propagator), the final result is

  **G(k, ω) = 1/(ω − ε_k/ℏ − Σ(k, ω))**.  ∎

**第 5 步 — 求解 G。** 戴森方程 G = G⁰ + G⁰ΣG 给出（在标量 k,ω 空间）

  G − G⁰ΣG = G⁰
  G(1 − G⁰Σ) = G⁰
  G = G⁰/(1 − G⁰Σ) = 1/(G⁰^{−1} − Σ)。

由于 G⁰(k, ω)^{−1} = ω − ε_k/ℏ（来自自由传播子），最终结果为

  **G(k, ω) = 1/(ω − ε_k/ℏ − Σ(k, ω))**。  ∎

---

## C. The RPA Bubble Sum and the Screened Interaction · RPA 气泡重求和与屏蔽相互作用

**Claim.** The Random Phase Approximation sums the geometric series of polarization-bubble insertions to give the screened interaction

  W(q, ω) = U(q) / (1 − U(q) Π⁰(q, ω)) = U(q) / ε(q, ω),

where ε(q, ω) is the dielectric function. The Lindhard function Π⁰(q, ω) is the free-electron polarization bubble.

**命题。** 随机相位近似对极化气泡插入的几何级数求和，给出屏蔽相互作用

  W(q, ω) = U(q) / (1 − U(q) Π⁰(q, ω)) = U(q) / ε(q, ω)，

其中 ε(q, ω) 是介电函数。Lindhard 函数 Π⁰(q, ω) 是自由电子极化气泡。

**Step 1 — Identify the bubble diagram.** In the diagrammatic expansion of the full interaction vertex W(q, ω) (the "dressed" or "screened" photon/Coulomb line), the lowest-order correction to the bare interaction U(q) is the insertion of a single particle-hole bubble. The bubble contributes a factor Π⁰(q, ω), the irreducible polarization:

  Π⁰(q, ω) = −2i ∫ d³k dε/(2π)⁴ G⁰(k+q, ε+ω) G⁰(k, ε),

where the factor 2 counts spin degeneracy. This is the Lindhard polarization function.

**第 1 步 — 识别气泡图。** 在完整相互作用顶点 W(q, ω)（"穿衣"或"屏蔽"光子/库仑线）的图展开中，对裸相互作用 U(q) 最低阶的修正是插入单个粒子-空穴气泡。气泡贡献因子 Π⁰(q, ω)，即不可约极化：

  Π⁰(q, ω) = −2i ∫ d³k dε/(2π)⁴ G⁰(k+q, ε+ω) G⁰(k, ε)，

其中因子 2 计算自旋简并。这就是 Lindhard 极化函数。

**Step 2 — Identify the class of diagrams being resummed.** The RPA keeps all diagrams that are chains of bubbles separated by bare interaction lines, and no crossing or vertex-correction diagrams. This is the dominant class in the high-density (r_s → 0) limit, where crossing diagrams are parametrically suppressed. The full series is:

  W = U + U Π⁰ U + U Π⁰ U Π⁰ U + …

**第 2 步 — 识别被重求和的图类。** RPA 保留所有由裸相互作用线分隔的气泡链构成的图，不含交叉图或顶点修正图。在高密度（r_s → 0）极限下，这是占主导地位的图类，交叉图在参数上被压制。完整级数为：

  W = U + U Π⁰ U + U Π⁰ U Π⁰ U + …

**Step 3 — Sum the geometric series.** This is the same algebraic structure as the Dyson equation, now for the bosonic interaction line instead of the fermionic propagator:

  W = U (1 + Π⁰ U + (Π⁰ U)² + …) = U · 1/(1 − Π⁰ U) = U/(1 − U Π⁰).

Note that Π⁰ U and U Π⁰ are equal for a local (momentum-diagonal) interaction, which is the case for screened Coulomb.

**第 3 步 — 对几何级数求和。** 这与戴森方程的代数结构相同，现在是针对玻色子相互作用线而非费米子传播子：

  W = U (1 + Π⁰ U + (Π⁰ U)² + …) = U · 1/(1 − Π⁰ U) = U/(1 − U Π⁰)。

注意对局域（动量对角）相互作用，Π⁰ U 和 U Π⁰ 相等，这对屏蔽库仑是满足的。

**Step 4 — Define the dielectric function.** Write W = U/ε where

  ε(q, ω) = 1 − U(q) Π⁰(q, ω).

This is the RPA dielectric function. In the static long-wavelength limit (q → 0, ω = 0), using Π⁰(q→0, 0) = −N(0) (density of states at the Fermi level) gives

  ε(q→0, 0) = 1 + U(q) N(0) = 1 + k²_{TF}/q²,

where k²_{TF} = e² N(0)/ε₀ is the Thomas–Fermi screening wave vector squared. Hence

  W(q→0, 0) = U(q)/(1 + k²_{TF}/q²) = e²/(ε₀(q² + k²_{TF})),

a finite-range (Yukawa) interaction.  ∎

**第 4 步 — 定义介电函数。** 写出 W = U/ε，其中

  ε(q, ω) = 1 − U(q) Π⁰(q, ω)。

这是 RPA 介电函数。在静态长波极限（q → 0，ω = 0）下，利用 Π⁰(q→0, 0) = −N(0)（费米面处的态密度），得到

  ε(q→0, 0) = 1 + U(q) N(0) = 1 + k²_{TF}/q²，

其中 k²_{TF} = e² N(0)/ε₀ 是 Thomas–Fermi 屏蔽波矢的平方。因此

  W(q→0, 0) = U(q)/(1 + k²_{TF}/q²) = e²/(ε₀(q² + k²_{TF}))，

是一个有限程（汤川型）相互作用。∎

**Step 5 — Plasmons as zeros of ε.** Poles of W(q, ω) occur where ε(q, ω) = 0, i.e. where 1 − U(q) Π⁰(q, ω) = 0. At q = 0, the Lindhard function gives Π⁰(0, ω) ≈ n e²/(m ω²) for ω ≫ v_F q (the high-frequency limit). Setting ε = 0:

  1 − (e²/ε₀q²)(−ne²/mω²) = 0  ⟹  ω² = ne²/(ε₀m) ≡ ω²_p.

The pole at ω = ω_p is the **plasmon** — a collective charge oscillation of the electron gas. It appears here as a direct consequence of the RPA resummation.

**第 5 步 — 等离激元作为 ε 的零点。** W(q, ω) 的极点出现在 ε(q, ω) = 0 处，即 1 − U(q) Π⁰(q, ω) = 0 处。在 q = 0 处，对于 ω ≫ v_F q（高频极限），Lindhard 函数给出 Π⁰(0, ω) ≈ −ne²/(mω²)。令 ε = 0：

  1 − (e²/ε₀q²)(−ne²/mω²) = 0  ⟹  ω² = ne²/(ε₀m) ≡ ω²_p。

ω = ω_p 处的极点就是**等离激元**——电子气的集体电荷振荡。它在这里作为 RPA 重求和的直接推论出现。

---

*These derivations show how Wick's theorem converts field-operator algebra into combinatorics, and how the Dyson and RPA equations arise as geometric resummations of infinite diagrammatic series — the same algebraic structure underlying the self-energy (fermionic) and the polarization (bosonic) channels.*

*上述推导表明，Wick 定理如何将场算符代数转化为组合数学，以及戴森方程和 RPA 方程如何作为无穷图级数的几何重求和而出现——这是费米子（自能）和玻色子（极化）通道背后相同的代数结构。*

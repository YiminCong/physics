# Derivations — Module 5.4: The Cooper Problem
# 推导 — 模块 5.4：库珀问题

> Companion to [Module 5.4](./module-5.4-the-cooper-problem.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.4](./module-5.4-the-cooper-problem.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Setting Up the Two-Electron Problem Above the Fermi Sea · 在费米海之上建立双电子问题

**Claim.** Two electrons added to a filled Fermi sea, interacting via a net attractive potential V(r − r′) < 0, can be placed in a zero-total-momentum pair state (k↑, −k↓). The pair wavefunction is expanded in plane waves above the Fermi surface, and the Schrödinger equation reduces to a linear algebraic equation for the expansion coefficients.

**命题。** 添加到填满费米海之上的两个电子，通过净吸引势 V(r − r′) < 0 相互作用，可以置于总动量为零的配对态 (k↑, −k↓) 中。配对波函数在费米面之上的平面波上展开，薛定谔方程化为展开系数的线性代数方程。

**Step 1 — State the problem.** The two added electrons have momenta k and −k (zero total momentum: chosen to maximize phase space for scattering) and opposite spins ↑, ↓ (spin singlet). The many-body Fermi sea is treated as a rigid background: all states with |k| ≤ k_F are filled and unavailable by the Pauli exclusion principle.

**第 1 步 — 陈述问题。** 两个添加的电子具有动量 k 和 −k（总动量为零：选此以最大化散射的相空间）和相反自旋 ↑，↓（自旋单态）。多体费米海被视为刚性背景：所有满足 |k| ≤ k_F 的态已被占据，由泡利不相容原理不可用。

**Step 2 — Pair wavefunction.** The relative-motion wavefunction (in spin-singlet form) is expanded in plane waves:

**第 2 步 — 配对波函数。** 相对运动波函数（自旋单态形式）在平面波上展开：

  ψ(r₁, r₂) = Σ_{k > k_F} g_k e^{ik·r₁} e^{−ik·r₂} · (↑↓ − ↓↑)/√2

            = Σ_{k > k_F} g_k e^{ik·(r₁−r₂)} · (singlet).

The sum is restricted to k > k_F (outside the Fermi sea). The two-electron Schrödinger equation Ĥψ = Eψ with Ĥ = Ĥ₁ + Ĥ₂ + V(r₁ − r₂) acts on this state.

求和限制在 k > k_F（费米海之外）。双电子薛定谔方程 Ĥψ = Eψ，Ĥ = Ĥ₁ + Ĥ₂ + V(r₁ − r₂) 作用于此态。

**Step 3 — Kinetic energy contribution.** Each electron k contributes kinetic energy ε_k = ℏ²k²/(2m) measured from the chemical potential μ ≈ E_F. The total kinetic energy of the pair is 2ε_k. So the Schrödinger equation acting on g_k e^{ik·(r₁−r₂)} gives

**第 3 步 — 动能贡献。** 每个电子 k 贡献从化学势 μ ≈ E_F 量起的动能 ε_k = ℏ²k²/(2m)。配对的总动能为 2ε_k。因此薛定谔方程作用于 g_k e^{ik·(r₁−r₂)} 给出

  (2ε_k − E) g_k + Σ_{k′ > k_F} V_{kk′} g_{k′} = 0,

where V_{kk′} = ⟨k|V|k′⟩ = (1/Ω) ∫ V(r) e^{i(k′−k)·r} d³r is the matrix element of the interaction, and Ω is the volume. Here E is measured from 2E_F (the energy of two free electrons at the Fermi surface). A bound state has E < 0.

其中 V_{kk′} = ⟨k|V|k′⟩ = (1/Ω) ∫ V(r) e^{i(k′−k)·r} d³r 是相互作用的矩阵元，Ω 是体积。这里 E 从 2E_F 量起（两个费米面上自由电子的能量）。束缚态有 E < 0。

---

## B. Contact Attraction and the Self-Consistency Equation · 接触吸引力与自洽方程

**Claim.** Using a separable contact (constant-matrix-element) approximation V_{kk′} = −g/Ω within a shell ℏω_D above E_F (and zero outside), the Schrödinger equation reduces to the self-consistency relation 1 = (g/Ω) Σ_{k} 1/(2ε_k − E), where the sum is over k_F < k < k_D.

**命题。** 在 E_F 以上厚度为 ℏω_D 的壳层内（外部为零）使用可分离接触（常数矩阵元）近似 V_{kk′} = −g/Ω，薛定谔方程化为自洽关系 1 = (g/Ω) Σ_{k} 1/(2ε_k − E)，求和范围为 k_F < k < k_D。

**Step 1 — Model the interaction.** Cooper used the "phonon window" approximation: the net electron–electron interaction is attractive (phonon overscreening of the Coulomb repulsion, as shown in Module 4.5) only for electrons within ℏω_D of the Fermi surface:

**第 1 步 — 对相互作用建模。** 库珀使用"声子窗口"近似：净电子–电子相互作用只在费米面 ℏω_D 范围内才是吸引的（声子对库仑排斥的过屏蔽，如模块 4.5 所示）：

  V_{kk′} = −g/Ω   if 0 < ε_k, ε_{k′} < ℏω_D  (above Fermi sea),
  V_{kk′} = 0       otherwise.

The negative sign makes it attractive; g > 0 is the coupling strength.

负号使其为吸引；g > 0 是耦合强度。

**Step 2 — Substitute into the Schrödinger equation.** From Step 3 of Section A:

**第 2 步 — 代入薛定谔方程。** 由 A 节第 3 步：

  (2ε_k − E) g_k = (g/Ω) Σ_{k′} g_{k′}   (sum over the shell).

Let C = Σ_{k′} g_{k′} (a constant, since the right side is k-independent). Then

设 C = Σ_{k′} g_{k′}（一个常数，因为右边与 k 无关）。则

  g_k = (g/Ω) C / (2ε_k − E).

**Step 3 — Close the self-consistency loop.** Sum both sides over k (within the shell):

**第 3 步 — 关闭自洽回路。** 两边对 k 求和（在壳层内）：

  C = Σ_k g_k = (g/Ω) C · Σ_k 1/(2ε_k − E).

Divide both sides by C ≠ 0 (assuming a nontrivial solution exists):

两边除以 C ≠ 0（假设存在非平凡解）：

  **1 = (g/Ω) Σ_k 1/(2ε_k − E).**

This is the **Cooper self-consistency equation** (gap equation for the two-body problem). ∎

这是**库珀自洽方程**（双体问题的能隙方程）。∎

---

## C. Converting to an Integral with the Density of States · 用态密度转化为积分

**Claim.** Replacing the k-sum by an integral over energy with density of states N(0) (assumed constant over the narrow phonon window), the self-consistency equation becomes 1 = g N(0) ∫₀^{ℏω_D} dε/(2ε − E).

**命题。** 将 k 求和替换为对能量的积分（态密度 N(0) 在窄声子窗口内视为常数），自洽方程变为 1 = g N(0) ∫₀^{ℏω_D} dε/(2ε − E)。

**Step 1 — Convert sum to integral.** For a macroscopic system, (1/Ω) Σ_k f(ε_k) → ∫ N(ε) f(ε) dε, where N(ε) is the density of states per unit volume per spin. Since we need both spins ↑ and ↓, the total DOS factor is 2N(ε). However, in the self-consistency sum each k labels a pair state (k↑, −k↓), so:

**第 1 步 — 将求和转化为积分。** 对于宏观系统，(1/Ω) Σ_k f(ε_k) → ∫ N(ε) f(ε) dε，其中 N(ε) 是单位体积每自旋的态密度。标准约定是令 N(0) 表示每自旋的费米面处 DOS；两个自旋方向的总 DOS 因子为 2N(ε)。然而在自洽求和中每个 k 标记一个配对态 (k↑, −k↓)，所以：

  (g/Ω) Σ_k  →  g · N(0) ∫₀^{ℏω_D} dε.

Here the integration variable ε = ε_k − E_F ≥ 0 runs over the phonon window 0 to ℏω_D above E_F, and N(0) is the single-spin DOS at the Fermi level (including both spins absorbed into the definition of g as a convention used here).

这里积分变量 ε = ε_k − E_F ≥ 0 在声子窗口 0 到 ℏω_D 的范围内积分，N(0) 是费米面处的单自旋 DOS（这里的约定将两个自旋方向吸收到 g 的定义中）。

**Step 2 — Write the integral equation.** The self-consistency equation becomes

**第 2 步 — 写出积分方程。** 自洽方程变为

  1 = g N(0) ∫₀^{ℏω_D} dε/(2ε − E).

Evaluate the integral (with E < 0 so 2ε − E > 0 for all ε ≥ 0):

计算积分（E < 0 故对所有 ε ≥ 0 有 2ε − E > 0）：

  ∫₀^{ℏω_D} dε/(2ε − E) = [½ ln(2ε − E)]₀^{ℏω_D} = ½ ln[(2ℏω_D − E)/(−E)].

**Step 3 — Solve for E.** Setting the right side equal to 1/[gN(0)]:

**第 3 步 — 求解 E。** 将右边置等于 1/[gN(0)]：

  ½ ln[(2ℏω_D − E)/(−E)] = 1/(gN(0)).

Exponentiate both sides:

两边取指数：

  (2ℏω_D − E)/(−E) = e^{2/(gN(0))}.

Let E = −|E| (bound state, E < 0):

令 E = −|E|（束缚态，E < 0）：

  (2ℏω_D + |E|)/|E| = e^{2/(gN(0))}   ⟹   2ℏω_D/|E| + 1 = e^{2/(gN(0))}.

  |E| = 2ℏω_D / (e^{2/(gN(0))} − 1).

**Step 4 — Weak-coupling limit.** In the weak-coupling regime gN(0) ≪ 1, e^{2/(gN(0))} ≫ 1, so e^{2/(gN(0))} − 1 ≈ e^{2/(gN(0))}:

**第 4 步 — 弱耦合极限。** 在弱耦合 gN(0) ≪ 1 区域，e^{2/(gN(0))} ≫ 1，故 e^{2/(gN(0))} − 1 ≈ e^{2/(gN(0))}：

  **|E| ≈ 2ℏω_D e^{−2/(gN(0))}**.

The binding energy is **E_binding = −2ℏω_D e^{−2/(gN(0))}** (measured from the pair-at-Fermi-surface energy 2E_F). ∎

束缚能为 **E_binding = −2ℏω_D e^{−2/(gN(0))}**（从费米面处的双电子能量 2E_F 量起）。∎

---

## D. Non-Analyticity and the Failure of Perturbation Theory · 非解析性与微扰论的失败

**Claim.** The binding energy E_binding ∝ e^{−2/(gN(0))} is a non-analytic function of the coupling g: all its Taylor coefficients around g = 0 vanish. Therefore, no finite order of perturbation theory in g can ever predict Cooper pairing — it is an intrinsically non-perturbative phenomenon.

**命题。** 束缚能 E_binding ∝ e^{−2/(gN(0))} 是耦合常数 g 的非解析函数：其在 g = 0 处的所有泰勒展开系数都为零。因此，对 g 的任何有限阶微扰论都永远无法预测库珀配对——这是一个本质上的非微扰现象。

**Step 1 — Taylor expansion of exp.** The function f(g) = e^{−2/(gN(0))} has the property that for g → 0⁺:

**第 1 步 — 指数的泰勒展开。** 函数 f(g) = e^{−2/(gN(0))} 具有这样的性质：当 g → 0⁺ 时：

  d^n f/dg^n |_{g=0} = 0   for all n = 0, 1, 2, …

This follows because e^{−1/g} → 0 faster than any power of g as g → 0⁺ (it is an essential singularity at g = 0). Explicitly: e^{−1/g}/g^n → 0 as g → 0⁺ for any n, by L'Hôpital's rule or change of variables t = 1/g.

这是因为当 g → 0⁺ 时 e^{−1/g} 比 g 的任何幂次趋向 0 更快（在 g = 0 处是本质奇点）。明确地：对任意 n，当 g → 0⁺ 时 e^{−1/g}/g^n → 0，通过洛必达法则或变量替换 t = 1/g 可验证。

**Step 2 — Physical consequence.** The n-th order term in perturbation theory in g would be proportional to g^n times some combination of N(0) and ℏω_D. A Taylor series in g would read

**第 2 步 — 物理后果。** 对 g 的微扰论中第 n 阶项正比于 g^n 乘以 N(0) 和 ℏω_D 的某种组合。g 的泰勒级数为

  E_binding = c₁ g + c₂ g² + c₃ g³ + …

But we just showed all Taylor coefficients c_n = 0. So **no finite-order perturbation series in g can produce a bound state**: the result is invisible to perturbation theory to every order.

但我们刚刚表明所有泰勒系数 c_n = 0。因此**对 g 的任何有限阶微扰论都无法得出束缚态**：结果对所有阶数的微扰论都是不可见的。

**Step 3 — Why a bound state exists for any g > 0.** In 3D, a weak potential does not generally produce a bound state (there is a threshold coupling). But here the Fermi sea plays a crucial role: it restricts the available states to a thin shell of energy ℏω_D and forces the effective density of states N(0) to be large (many states in the shell). This "dimensional reduction" to 1D-like kinematics (only states on the Fermi surface participate) is what allows a bound state for arbitrarily weak coupling. ∎

**第 3 步 — 为何对任意 g > 0 都存在束缚态。** 在三维中，弱势通常不能产生束缚态（有一个耦合阈值）。但这里费米海起关键作用：它将可用的态限制在能量 ℏω_D 的薄壳层中，并使有效态密度 N(0) 很大（壳层中有许多态）。这种向类一维运动学的"降维"（只有费米面上的态参与）使得任意弱耦合都能产生束缚态。∎

**Step 4 — Implication for the normal metal.** At any temperature, there are always two electrons at (k↑, −k↓) with ε_k just above E_F. The above calculation applies to them: they bind, regardless of how weak g is. This means the normal metallic state (Fermi sea without pairs) is **unstable** to Cooper pairing. The many-body ground state must reorganize — this is the subject of Module 5.5. ∎

**第 4 步 — 对正常金属的含义。** 在任何温度下，总存在处于 (k↑, −k↓) 的两个电子，其 ε_k 刚好在 E_F 以上。上述计算适用于它们：它们会结合，无论 g 多么弱。这意味着正常金属态（无配对的费米海）对库珀配对是**不稳定**的。多体基态必须重组——这是模块 5.5 的主题。∎

---

## E. Symmetry of the Pair State · 配对态的对称性

**Claim.** The choice (k↑, −k↓) with zero center-of-mass momentum, together with the antisymmetry of the fermionic wavefunction, forces the spin part to be a singlet if the spatial part is even (s-wave) or a triplet if spatial is odd. The BCS ground state uses s-wave singlets.

**命题。** 选择总质心动量为零的态 (k↑, −k↓)，加上费米子波函数的反对称性，若空间部分为偶（s 波）则自旋部分必为单态，若空间部分为奇则为三重态。BCS 基态使用 s 波单态。

**Step 1 — Antisymmetry under particle exchange.** The two-electron wavefunction must be antisymmetric: ψ(1, 2) = −ψ(2, 1). Writing ψ = ψ_spatial × ψ_spin:

**第 1 步 — 粒子交换下的反对称性。** 双电子波函数必须是反对称的：ψ(1, 2) = −ψ(2, 1)。写 ψ = ψ_spatial × ψ_spin：

  (symmetry of spatial) × (symmetry of spin) = antisymmetric = odd overall.

So: even spatial (s-wave, l = 0) × odd spin (singlet S = 0) — the BCS case. ∎

所以：偶空间（s 波，l = 0）× 奇自旋（单态 S = 0）——BCS 情况。∎

**Step 2 — Why zero total momentum?** Pairs with total momentum q ≠ 0 would have one electron at k + q/2 and the other at −k + q/2. The phase-space argument shows the density of k-states contributing to the sum in the self-consistency equation is maximized at q = 0, giving the most negative (most bound) energy. Finite-q pairs have reduced binding energy. At q = 0, both electrons occupy the same Fermi sphere shell, maximizing the number of available scattering partners. ∎

**第 2 步 — 为何总动量为零？** 总动量为 q ≠ 0 的对，一个电子在 k + q/2，另一个在 −k + q/2。相空间论证表明对自洽方程中的求和贡献的 k 态密度在 q = 0 时最大，给出最负（最强束缚）的能量。有限 q 的对束缚能降低。在 q = 0 时，两个电子占据相同的费米球壳层，最大化可用的散射伙伴数目。∎

---

*The Cooper problem solved here is the two-body prelude. The full many-body condensation — where all pairs form simultaneously and the gap Δ replaces E_binding — is treated in Module 5.5.*

*此处解决的库珀问题是双体前奏。所有对同时形成、能隙 Δ 取代 E_binding 的完整多体凝聚在模块 5.5 中处理。*

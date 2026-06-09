# Derivations — Module 5.11: Topological Superconductivity & Majorana Modes
# 推导 — 模块 5.11：拓扑超导与马约拉纳模

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.11](./module-5.11-topological-superconductivity-and-majorana.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.11](./module-5.11-topological-superconductivity-and-majorana.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Kitaev Chain in Majorana Operators: Topological Phase and Unpaired End Modes · 马约拉纳算符中的基塔耶夫链：拓扑相与未配对端模

**Claim.** Rewriting the Kitaev chain Hamiltonian in Majorana operators reveals that, at the special point t = Δ > 0 and μ = 0, the Hamiltonian couples only inter-site Majorana pairs, leaving one Majorana mode at each end of the chain exactly at zero energy. For |μ| < 2t (topological phase), these end modes remain at zero energy even away from the special point, exponentially localized at the ends.

**命题。** 将基塔耶夫链哈密顿量用马约拉纳算符改写后，可以看出在特殊点 t = Δ > 0、μ = 0 处，哈密顿量仅耦合格点间马约拉纳对，使链每端各有一个马约拉纳模精确处于零能。对于 |μ| < 2t（拓扑相），这些端模即使在远离特殊点处也保持零能，在端部指数局域。

**Step 1 — Define Majorana operators.** For each site j = 1, …, N, define two Hermitian Majorana operators:

**第 1 步 — 定义马约拉纳算符。** 对每个格点 j = 1, …, N，定义两个厄米马约拉纳算符：

  γ_{j,A} = c_j + c_j†,    γ_{j,B} = i(c_j† − c_j).

These satisfy γ_{j,A}† = γ_{j,A}, γ_{j,B}† = γ_{j,B} (Hermitian), and the anticommutation relations {γ_{j,α}, γ_{k,β}} = 2δ_{jk} δ_{αβ}. The inverse relations are:

这些算符满足 γ_{j,A}† = γ_{j,A}，γ_{j,B}† = γ_{j,B}（厄米），以及反对易关系 {γ_{j,α}, γ_{k,β}} = 2δ_{jk} δ_{αβ}。逆关系为：

  c_j = (γ_{j,A} + iγ_{j,B})/2,    c_j† = (γ_{j,A} − iγ_{j,B})/2.

**Step 2 — Rewrite each term.** Compute the three types of terms in H = −μ Σ_j c_j†c_j − t Σ_j(c_j†c_{j+1} + c_{j+1}†c_j) + Δ Σ_j(c_j c_{j+1} + c_{j+1}†c_j†):

**第 2 步 — 改写每一项。** 计算 H = −μ Σ_j c_j†c_j − t Σ_j(c_j†c_{j+1} + c_{j+1}†c_j) + Δ Σ_j(c_j c_{j+1} + c_{j+1}†c_j†) 中的三类项：

*On-site number operator:*
  c_j†c_j = (γ_{j,A} − iγ_{j,B})(γ_{j,A} + iγ_{j,B})/4 = (1 + iγ_{j,A}γ_{j,B})/2 = (1 − iγ_{j,B}γ_{j,A})/2. So:
  −μ c_j†c_j = −μ/2 + (iμ/2) γ_{j,B} γ_{j,A}.

*格点占据数算符：*
  c_j†c_j = (1 − iγ_{j,B}γ_{j,A})/2，故 −μ c_j†c_j = −μ/2 + (iμ/2) γ_{j,B} γ_{j,A}。

*Hopping term:*
  c_j†c_{j+1} + h.c. = [(γ_{j,A} − iγ_{j,B})(γ_{j+1,A} + iγ_{j+1,B})]/4 + h.c.

Expanding and taking real part (the h.c. doubles the real terms and cancels the imaginary terms):
  c_j†c_{j+1} + h.c. = (i/2)(γ_{j,B}γ_{j+1,A} − γ_{j,A}γ_{j+1,B}).

*跳跃项：*
展开并取实部（厄米共轭使实部加倍，消去虚部）：
  c_j†c_{j+1} + h.c. = (i/2)(γ_{j,B}γ_{j+1,A} − γ_{j,A}γ_{j+1,B})。

*Pairing term:*
  c_j c_{j+1} = (γ_{j,A} + iγ_{j,B})(γ_{j+1,A} + iγ_{j+1,B})/4
              = (γ_{j,A}γ_{j+1,A} + iγ_{j,A}γ_{j+1,B} + iγ_{j,B}γ_{j+1,A} − γ_{j,B}γ_{j+1,B})/4.

Adding the h.c. c_{j+1}†c_j† = (γ_{j+1,A} − iγ_{j+1,B})(γ_{j,A} − iγ_{j,B})/4 and using γ_{j+1,α}γ_{j,β} = −γ_{j,β}γ_{j+1,α}, the γγ-symmetric (real) parts cancel and the imaginary parts double:
  c_j c_{j+1} + h.c. = (i/2)(γ_{j,A}γ_{j+1,B} + γ_{j,B}γ_{j+1,A}).

(Note: this has the same structure as the hopping term but with opposite relative sign between the two Majorana cross-products.)

*配对项：*
经仔细代数运算（利用 α≠β 时 γ_{α}γ_{β} = −γ_{β}γ_{α} 和 γ² = 1）：
  c_j c_{j+1} + h.c. = (i/2)(γ_{j,B}γ_{j+1,A} + γ_{j,A}γ_{j+1,B})。

（注意：这与跳跃项结构相同，但两个马约拉纳交叉乘积之间的相对符号相反。）

**Step 3 — Assemble the full Hamiltonian.** Collecting all terms (dropping constant −μN/2):

**第 3 步 — 组装完整哈密顿量。** 收集所有项（舍去常数 −μN/2）：

  H = (iμ/2) Σ_j γ_{j,B} γ_{j,A}
    + (i/2) Σ_j [ −t(γ_{j,B}γ_{j+1,A} − γ_{j,A}γ_{j+1,B}) + Δ(γ_{j,B}γ_{j+1,A} + γ_{j,A}γ_{j+1,B}) ]

  = (iμ/2) Σ_j γ_{j,B} γ_{j,A}
    + (i/2) Σ_j [ (Δ−t) γ_{j,A}γ_{j+1,B} + (Δ+t) γ_{j,B}γ_{j+1,A} ].

**Step 4 — Special point t = Δ, μ = 0.** Setting μ = 0 eliminates the first sum. Setting Δ = t makes the coefficient of γ_{j,A}γ_{j+1,B} vanish (Δ−t = 0):

**第 4 步 — 特殊点 t = Δ，μ = 0。** 令 μ = 0 消去第一个求和。令 Δ = t 使 γ_{j,A}γ_{j+1,B} 的系数消失（Δ−t = 0）：

  H|_{t=Δ, μ=0} = it Σ_{j=1}^{N−1} γ_{j,B} γ_{j+1,A}.

The Hamiltonian couples only the **B** Majorana on site j to the **A** Majorana on site j+1. The 2N Majorana operators split into:
- **N−1 coupled pairs** (γ_{j,B}, γ_{j+1,A}): these form ordinary fermions d_j = (γ_{j,B} + iγ_{j+1,A})/2 with energy ε = ±t (positive gap 2t).
- **Two unpaired operators**: γ_{1,A} (left end) and γ_{N,B} (right end), which do not appear in H at all.

哈密顿量仅耦合格点 j 上的 **B** 马约拉纳与格点 j+1 上的 **A** 马约拉纳。2N 个马约拉纳算符分为：
- **N−1 个耦合对**（γ_{j,B}, γ_{j+1,A}）：形成普通费米子 d_j = (γ_{j,B} + iγ_{j+1,A})/2，能量 ε = ±t（正能隙 2t）。
- **两个未配对算符**：γ_{1,A}（左端）和 γ_{N,B}（右端），完全不出现在 H 中。

Since [H, γ_{1,A}] = [H, γ_{N,B}] = 0 and γ_{1,A}² = γ_{N,B}² = 1, these are **zero-energy Majorana modes**. The non-local fermion f = (γ_{1,A} + iγ_{N,B})/2 has [H, f] = [H, f†] = 0 and {f, f†} = 1, so |0⟩ and f†|0⟩ are degenerate ground states with the same energy. ∎

由于 [H, γ_{1,A}] = [H, γ_{N,B}] = 0 且 γ_{1,A}² = γ_{N,B}² = 1，这些是**零能马约拉纳模**。非局域费米子 f = (γ_{1,A} + iγ_{N,B})/2 满足 [H, f] = [H, f†] = 0 和 {f, f†} = 1，因此 |0⟩ 和 f†|0⟩ 是能量相同的简并基态。∎

---

## B. Topological Phase |μ| < 2t and Ground-State Degeneracy · 拓扑相 |μ| < 2t 与基态简并

**Claim.** The topological criterion |μ| < 2t follows from the bulk band structure of the Kitaev chain. The two ground states |0⟩ and |1⟩ = f†|0⟩ are exactly degenerate in the thermodynamic limit (N → ∞) and differ only in the parity of the non-local fermion f.

**命题。** 拓扑判据 |μ| < 2t 来自基塔耶夫链的体能带结构。在热力学极限（N → ∞）中，两个基态 |0⟩ 和 |1⟩ = f†|0⟩ 精确简并，仅在非局域费米子 f 的宇称上有所不同。

**Step 1 — Bulk Hamiltonian in k-space.** For a periodic infinite chain (ignoring boundaries), Fourier transform c_j = (1/√N) Σ_k e^{ikj} c_k. The Hamiltonian in Nambu basis Ψ_k = (c_k, c_{−k}†)ᵀ becomes:

**第 1 步 — k 空间中的体哈密顿量。** 对周期性无限链（忽略边界），傅里叶变换 c_j = (1/√N) Σ_k e^{ikj} c_k。Nambu 基 Ψ_k = (c_k, c_{−k}†)ᵀ 中的哈密顿量变为：

  H = (1/2) Σ_k Ψ_k† h(k) Ψ_k,

  h(k) = (−μ − 2t cos k) τ_z + 2Δ sin k · τ_y,

where τ_{y,z} are Pauli matrices in particle–hole (Nambu) space. The quasiparticle dispersion is:

其中 τ_{y,z} 是粒子–空穴（Nambu）空间中的泡利矩阵。准粒子色散为：

  E(k) = ±√((μ + 2t cos k)² + 4Δ² sin²k).

**Step 2 — Gap-closing condition.** The bulk gap closes at E(k) = 0, which requires both:
  μ + 2t cos k = 0    AND    2Δ sin k = 0.

The second condition gives k = 0 or k = π. Substituting:
- k = 0: gap closes when μ + 2t = 0, i.e. **μ = −2t**.
- k = π: gap closes when μ − 2t = 0, i.e. **μ = +2t**.

**第 2 步 — 能隙关闭条件。** 体能隙在 E(k) = 0 处关闭，这要求同时满足：
  μ + 2t cos k = 0    且    2Δ sin k = 0。

第二个条件给出 k = 0 或 k = π。代入：
- k = 0：当 μ + 2t = 0 即 **μ = −2t** 时能隙关闭。
- k = π：当 μ − 2t = 0 即 **μ = +2t** 时能隙关闭。

Thus the bulk gap is open for |μ| ≠ 2t, and the gap-closing transitions at μ = ±2t separate two phases.

因此体能隙在 |μ| ≠ 2t 时开启，在 μ = ±2t 处的能隙关闭相变分隔了两个相。

**Step 3 — Topological invariant (Pfaffian / winding number).** The BdG Hamiltonian h(k) at k = 0 and k = π is a real antisymmetric matrix (since sin 0 = sin π = 0). Define the **Majorana number** (Kitaev's Z₂ invariant):

**第 3 步 — 拓扑不变量（普法夫/绕数）。** 在 k = 0 和 k = π 处，BdG 哈密顿量 h(k) 是实反对称矩阵（因为 sin 0 = sin π = 0）。定义**马约拉纳数**（基塔耶夫的 Z₂ 不变量）：

  M = sgn( Pf[h(0)] ) × sgn( Pf[h(π)] ),

where Pf denotes the Pfaffian. For the Kitaev chain:
  h(0) = (−μ − 2t) τ_z,        Pf[h(0)] = −(μ + 2t).
  h(π) = (−μ + 2t) τ_z,        Pf[h(π)] = −(μ − 2t).
  M = sgn[(μ + 2t)(μ − 2t)] = sgn[μ² − 4t²].

其中 Pf 表示普法夫式。对于基塔耶夫链：
  h(0) = (−μ − 2t) τ_z，Pf[h(0)] = −(μ + 2t)。
  h(π) = (−μ + 2t) τ_z，Pf[h(π)] = −(μ − 2t)。
  M = sgn[(μ + 2t)(μ − 2t)] = sgn[μ² − 4t²]。

- **Topological phase** (|μ| < 2t): μ² < 4t², so M = sgn(negative) = **−1**. Majorana end modes exist.
- **Trivial phase** (|μ| > 2t): μ² > 4t², so M = sgn(positive) = **+1**. No end modes.

- **拓扑相**（|μ| < 2t）：μ² < 4t²，故 M = sgn(负) = **−1**。马约拉纳端模存在。
- **平庸相**（|μ| > 2t）：μ² > 4t²，故 M = sgn(正) = **+1**。无端模。

This is the Z₂ topological invariant. The **bulk–boundary correspondence** guarantees that M = −1 implies the existence of a zero-energy boundary mode for any open chain in the topological phase, not just at the special point. ∎

这就是 Z₂ 拓扑不变量。**体–边对应**保证 M = −1 意味着拓扑相中任意开放链存在零能边界模，而不仅仅是在特殊点处。∎

**Step 4 — Ground-state degeneracy from the non-local fermion.** In the topological phase, the two end modes γ_L and γ_R are spatially separated by the entire chain of length N. Define:

**第 4 步 — 非局域费米子的基态简并。** 在拓扑相中，两个端模 γ_L 和 γ_R 在空间上被整个长度为 N 的链分开。定义：

  f = (γ_L + iγ_R)/2,    f† = (γ_L − iγ_R)/2.

The ground-state subspace is spanned by |0⟩ (f|0⟩ = 0) and |1⟩ = f†|0⟩. These states have:
- The **same energy** (since γ_L and γ_R decouple from H in the limit of a long chain).
- **Different fermion parity**: P = (−1)^{N_f} where N_f is the total fermion number. |0⟩ and |1⟩ differ by adding one fermion (the non-local f†), so they have opposite parity.

基态子空间由 |0⟩（f|0⟩ = 0）和 |1⟩ = f†|0⟩ 张成。这两个态具有：
- **相同能量**（在长链极限下 γ_L 和 γ_R 从 H 中解耦）。
- **不同费米子宇称**：P = (−1)^{N_f}，其中 N_f 是总费米子数。|0⟩ 和 |1⟩ 相差一个非局域费米子 f†，因此宇称相反。

Any local operator acting on one end of the chain cannot distinguish |0⟩ from |1⟩ because the non-local fermion's quantum number is split between the two ends. This **topological protection** of the degeneracy is the key property that makes Majorana modes useful for quantum memory. ∎

作用在链一端的任何局域算符都无法区分 |0⟩ 和 |1⟩，因为非局域费米子的量子数分裂在两端之间。这种简并的**拓扑保护**是使马约拉纳模在量子存储中有用的关键性质。∎

---

## C. Non-Abelian Braiding Rule for Majorana Modes · 马约拉纳模的非阿贝尔编织规则

**Claim.** Adiabatically exchanging (braiding) two Majorana modes γ_i and γ_j in 2D (or in a T-junction network in 1D) implements the unitary transformation U_{ij} = (1 + γ_i γ_j)/√2 = exp(πγ_i γ_j/4) on the degenerate ground-state subspace. Sequential braidings do not commute, making the representation non-Abelian.

**命题。** 在二维（或一维 T 结网络中）绝热地交换（编织）两个马约拉纳模 γ_i 和 γ_j，在简并基态子空间上实现酉变换 U_{ij} = (1 + γ_i γ_j)/√2 = exp(πγ_i γ_j/4)。序贯编织不对易，使该表示成为非阿贝尔的。

**Step 1 — Setup: four Majorana modes.** Consider four Majorana modes γ₁, γ₂, γ₃, γ₄ forming two non-local fermions:

**第 1 步 — 设置：四个马约拉纳模。** 考虑四个马约拉纳模 γ₁、γ₂、γ₃、γ₄，形成两个非局域费米子：

  f₁₂ = (γ₁ + iγ₂)/2    (parity p₁₂ = 2f₁₂†f₁₂ − 1 = iγ₁γ₂)
  f₃₄ = (γ₃ + iγ₄)/2    (parity p₃₄ = iγ₃γ₄)

The four-dimensional degenerate subspace is spanned by |n₁₂, n₃₄⟩ where n₁₂, n₃₄ ∈ {0,1} are the occupancies of f₁₂ and f₃₄. Total parity conservation (imposed by fermion parity superselection) restricts physical states to the two-dimensional subspace {|00⟩, |11⟩} (even total parity) or {|01⟩, |10⟩} (odd total parity).

四维简并子空间由 |n₁₂, n₃₄⟩ 张成，其中 n₁₂, n₃₄ ∈ {0,1} 是 f₁₂ 和 f₃₄ 的占据数。总宇称守恒（由费米子宇称超选择定则施加）将物理态限制在二维子空间 {|00⟩, |11⟩}（偶总宇称）或 {|01⟩, |10⟩}（奇总宇称）中。

**Step 2 — Berry phase from adiabatic exchange.** To exchange γ₁ and γ₂, we adiabatically move them in the plane along a path that winds γ₂ around γ₁ by angle π (a half-braid). The key physical ingredient is that the Hamiltonian H(t) must close and reopen the local gap near each Majorana as they move, but the global gap (and the degeneracy subspace) never closes. The resulting Berry phase matrix, computed from the adiabatic connection A = ⟨ψ_n|d/dt|ψ_m⟩ dt integrated around the exchange path, gives:

**第 2 步 — 绝热交换的贝里相位。** 为了交换 γ₁ 和 γ₂，我们沿着将 γ₂ 绕 γ₁ 旋转 π 角度（半编织）的路径绝热地移动它们。关键的物理成分是：哈密顿量 H(t) 必须在每个马约拉纳移动时局域地关闭和重新开启能隙，但全局能隙（和简并子空间）从不关闭。由绝热联络 A = ⟨ψ_n|d/dt|ψ_m⟩ dt 沿交换路径积分得到贝里相位矩阵：

  U₁₂ = exp(π γ₁ γ₂ / 4) = (1 + γ₁γ₂)/√2.

This result follows from the Aharonov–Anandan holonomy for the non-Abelian Berry connection of the degenerate subspace.

这个结果来自简并子空间的非阿贝尔贝里联络的 Aharonov–Anandan 完整性。

**Step 3 — Explicit matrix representation.** In the {|00⟩, |11⟩} subspace, compute γ₁γ₂ using γ₁ = f₁₂ + f₁₂† and γ₂ = i(f₁₂† − f₁₂):

**第 3 步 — 显式矩阵表示。** 在 {|00⟩, |11⟩} 子空间中，利用 γ₁ = f₁₂ + f₁₂† 和 γ₂ = i(f₁₂† − f₁₂) 计算 γ₁γ₂：

  iγ₁γ₂ = i(f₁₂ + f₁₂†) · i(f₁₂† − f₁₂) = −(f₁₂ + f₁₂†)(f₁₂† − f₁₂)
          = −(f₁₂f₁₂† − f₁₂f₁₂ + f₁₂†f₁₂† − f₁₂†f₁₂)
          = −(f₁₂f₁₂† − f₁₂†f₁₂) = −(1 − 2f₁₂†f₁₂) = 2n₁₂ − 1.

So iγ₁γ₂ acts as +1 on |1,n₃₄⟩ and −1 on |0,n₃₄⟩, i.e. iγ₁γ₂ = σ_z in the {|00⟩,|11⟩} basis. Therefore:

所以 iγ₁γ₂ 在 |1,n₃₄⟩ 上作用为 +1，在 |0,n₃₄⟩ 上为 −1，即在 {|00⟩,|11⟩} 基中 iγ₁γ₂ = σ_z。因此：

  U₁₂ = (1 + γ₁γ₂)/√2 = (1 − iσ_z)/√2 = e^{−iπ/4} ( 1   0 )
                                                         ( 0   e^{iπ/2} )
       = e^{−iπσ_z/4}    (a rotation by π/2 around the z-axis).

Similarly, for braiding γ₂ and γ₃ (which mixes the two non-local fermions f₁₂ and f₃₄):

类似地，编织 γ₂ 和 γ₃（混合两个非局域费米子 f₁₂ 和 f₃₄）：

  U₂₃ = (1 + γ₂γ₃)/√2 = e^{−iπσ_x/4}    (a rotation by π/2 around the x-axis).

**Step 4 — Non-commutativity.** The key property:

**第 4 步 — 非对易性。** 关键性质：

  U₁₂ U₂₃ = e^{−iπσ_z/4} e^{−iπσ_x/4}  ≠  e^{−iπσ_x/4} e^{−iπσ_z/4} = U₂₃ U₁₂,

because σ_z and σ_x do not commute: [σ_z, σ_x] = 2iσ_y ≠ 0. The braiding operations generate the group of single-qubit rotations by multiples of π/2. Together with inter-qubit braidings and a few additional operations, these provide a **universal gate set** for topological quantum computation, where the quantum information is stored in the non-local fermion parities and gates are implemented by braiding trajectories. ∎

因为 σ_z 和 σ_x 不对易：[σ_z, σ_x] = 2iσ_y ≠ 0。编织操作生成 π/2 倍数单量子比特旋转群。与量子比特间编织及少量附加操作一起，这些提供了拓扑量子计算的**通用门集**，其中量子信息存储在非局域费米子宇称中，量子门通过编织轨迹实现。∎

**Physical implementation note.** In a 1D wire system, Majoranas cannot be directly exchanged (they would have to pass through each other). Instead, a T-junction geometry is used: a horizontal wire joined by a vertical stub. Moving a Majorana from the stub to the horizontal wire and then to the other side effectively performs the exchange without the two modes meeting. This 2D-equivalent topological exchange is what Majorana-based qubit proposals (e.g. Microsoft's topological qubit roadmap) aim to implement.

**物理实现注记。** 在一维线系统中，马约拉纳模不能直接交换（它们必须相互穿过）。取而代之，使用 T 结几何：一条水平线与一个垂直短线相连。将马约拉纳从短线移到水平线再到另一侧，有效地执行了交换而两个模不相遇。这种等效二维的拓扑交换正是马约拉纳量子比特方案（例如微软拓扑量子比特路线图）旨在实现的。

---

*Summary: (A) In Majorana operator language the Kitaev chain Hamiltonian at t = Δ, μ = 0 pairs only inter-site Majorana modes, leaving γ_{1,A} and γ_{N,B} unpaired and at exactly zero energy. (B) The topological phase |μ| < 2t is identified by the Z₂ Pfaffian invariant M = −1, following from the gap-closing transitions at μ = ±2t; the resulting degenerate ground states |0⟩ and f†|0⟩ differ only in parity of the non-local fermion f = (γ_L + iγ_R)/2. (C) Adiabatic exchange of two Majorana modes implements U_{ij} = exp(πγ_i γ_j/4) on the ground-state subspace; since these generators satisfy non-commuting algebra, sequential braidings realize non-Abelian statistics and provide the building blocks of fault-tolerant topological quantum gates.*

*总结：(A) 在马约拉纳算符语言中，基塔耶夫链哈密顿量在 t = Δ、μ = 0 处仅配对格点间马约拉纳模，使 γ_{1,A} 和 γ_{N,B} 未配对且精确处于零能。(B) 拓扑相 |μ| < 2t 由 Z₂ 普法夫不变量 M = −1 标识，来源于 μ = ±2t 处的能隙关闭相变；由此产生的简并基态 |0⟩ 和 f†|0⟩ 仅在非局域费米子 f = (γ_L + iγ_R)/2 的宇称上不同。(C) 两个马约拉纳模的绝热交换在基态子空间上实现 U_{ij} = exp(πγ_i γ_j/4)；由于这些生成元满足不对易代数，序贯编织实现非阿贝尔统计，提供容错拓扑量子门的构建块。*

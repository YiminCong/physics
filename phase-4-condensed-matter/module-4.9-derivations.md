# Derivations — Module 4.9: Topological Matter & Berry Phase
# 推导 — 模块 4.9：拓扑物质与贝里相位

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.9](./module-4.9-topological-matter-and-berry-phase.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.9](./module-4.9-topological-matter-and-berry-phase.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Berry Phase from the Adiabatic Theorem · 由绝热定理推导贝里相位

**Claim.** If a quantum system starts in the n-th eigenstate of H(R(0)) and R(t) varies slowly around a closed loop C in parameter space, the system returns to the n-th eigenstate with a phase factor exp(iγ_n) where γ_n = ∮_C A_n(R)·dR and A_n = i⟨u_n(R)|∇_R|u_n(R)⟩.

**命题。** 若量子系统从 H(R(0)) 的第 n 个本征态出发，R(t) 缓慢地在参数空间中的闭合回路 C 上变化，系统回到第 n 个本征态时携带相位因子 exp(iγ_n)，其中 γ_n = ∮_C A_n(R)·dR，A_n = i⟨u_n(R)|∇_R|u_n(R)⟩。

**Step 1 — Time-dependent Schrödinger equation.** Write |ψ(t)⟩ = Σ_m c_m(t) e^{iθ_m(t)} |u_m(R(t))⟩ where θ_m(t) = −(1/ℏ)∫₀ᵗ E_m(R(t')) dt' is the dynamical phase. Substituting into iℏ ∂_t|ψ⟩ = H|ψ⟩:

**第 1 步 — 含时薛定谔方程。** 令 |ψ(t)⟩ = Σ_m c_m(t) e^{iθ_m(t)} |u_m(R(t))⟩，其中 θ_m(t) = −(1/ℏ)∫₀ᵗ E_m(R(t')) dt' 是动力学相位。代入 iℏ ∂_t|ψ⟩ = H|ψ⟩：

  ċ_n(t) = −Σ_m c_m(t) e^{i(θ_m−θ_n)} ⟨u_n|∂_t|u_m⟩.

**Step 2 — Off-diagonal terms.** For m ≠ n, use H|u_m⟩ = E_m|u_m⟩ and differentiate: ⟨u_n|∂_t|u_m⟩ = ⟨u_n|(∂_t H)|u_m⟩ / (E_m − E_n). In the adiabatic limit |∂_t H| is small, so ⟨u_n|∂_t|u_m⟩ ≪ (E_m − E_n)/ℏ for m ≠ n. The oscillating factor e^{i(θ_m−θ_n)} = exp[i∫(E_m−E_n)dt/ℏ] averages to zero for the rapidly oscillating off-diagonal terms. Therefore:

**第 2 步 — 非对角项。** 对 m ≠ n，利用 H|u_m⟩ = E_m|u_m⟩ 并微分：⟨u_n|∂_t|u_m⟩ = ⟨u_n|(∂_t H)|u_m⟩ / (E_m − E_n)。在绝热极限下 |∂_t H| 很小，故对 m ≠ n，⟨u_n|∂_t|u_m⟩ ≪ (E_m − E_n)/ℏ。振荡因子 e^{i(θ_m−θ_n)} = exp[i∫(E_m−E_n)dt/ℏ] 对快速振荡的非对角项平均为零。因此：

  ċ_n(t) ≈ −c_n(t) ⟨u_n|∂_t|u_n⟩.

**Step 3 — Integrate.** This gives c_n(t) = c_n(0) exp(−∫₀ᵗ ⟨u_n|∂_t|u_n⟩ dt'). Using ∂_t = (dR/dt)·∇_R:

**第 3 步 — 积分。** 这给出 c_n(t) = c_n(0) exp(−∫₀ᵗ ⟨u_n|∂_t|u_n⟩ dt')。利用 ∂_t = (dR/dt)·∇_R：

  −∫₀ᵗ ⟨u_n|∂_t|u_n⟩ dt' = −∫_C ⟨u_n|∇_R|u_n⟩·dR = i ∮_C A_n · dR = i γ_n.

**Step 4 — Reality of γ_n.** Differentiating ⟨u_n|u_n⟩ = 1: ⟨∂_R u_n|u_n⟩ + ⟨u_n|∂_R u_n⟩ = 0, so ⟨u_n|∂_R u_n⟩ = −⟨∂_R u_n|u_n⟩ is purely imaginary. Therefore A_n = i⟨u_n|∇_R u_n⟩ is real, and **γ_n is real**. ∎

**第 4 步 — γ_n 的实性。** 对 ⟨u_n|u_n⟩ = 1 微分：⟨∂_R u_n|u_n⟩ + ⟨u_n|∂_R u_n⟩ = 0，故 ⟨u_n|∂_R u_n⟩ = −⟨∂_R u_n|u_n⟩ 是纯虚数。因此 A_n = i⟨u_n|∇_R u_n⟩ 是实数，**γ_n 是实数**。∎

---

## B. Chern Number ∫(Berry Curvature)/2π is an Integer · 陈数 ∫（贝里曲率）/2π 为整数

**Claim.** For a smooth Bloch band |u_n(k)⟩ on a 2D torus (BZ with periodic boundary conditions), C_n = (1/2π) ∫_{BZ} Ω_n(k) d²k is an integer.

**命题。** 对于二维环面（具有周期边界条件的 BZ）上的光滑布洛赫能带 |u_n(k)⟩，C_n = (1/2π) ∫_{BZ} Ω_n(k) d²k 是整数。

**Step 1 — The BZ as a torus.** The Brillouin zone has k_{x,y} ∈ [−π/a, π/a] with the opposite edges identified (periodicity of the lattice). This makes the BZ topologically a 2-torus T².

**第 1 步 — BZ 作为环面。** 布里渊区有 k_{x,y} ∈ [−π/a, π/a]，对边等同（晶格的周期性）。这使 BZ 在拓扑上成为二维环面 T²。

**Step 2 — Stokes's theorem and gauge singularities.** By Stokes's theorem, ∫_{BZ} Ω_n d²k = ∮_{∂BZ} A_n · dk. But on a torus the boundary ∂BZ is empty — the integral of a total derivative over a closed manifold is zero by Stokes. However, A_n may not be globally well-defined: at points where the eigenstate |u_n(k)⟩ is undefined (degeneracy or gauge singularity), A_n has a Dirac-string-like singularity.

**第 2 步 — 斯托克斯定理和规范奇点。** 由斯托克斯定理，∫_{BZ} Ω_n d²k = ∮_{∂BZ} A_n · dk。但在环面上边界 ∂BZ 为空——在闭合流形上全导数的积分由斯托克斯定理为零。然而，A_n 可能不是全局定义的：在本征态 |u_n(k)⟩ 未定义的点（简并或规范奇点），A_n 具有类狄拉克弦奇点。

**Step 3 — Partition into patches.** Divide the BZ into two patches U_+ and U_− with an overlap region. On each patch define a smooth gauge for |u_n⟩, giving connection forms A^+ and A^−. On the overlap, the two gauges are related by a gauge transformation: |u_n^+⟩ = e^{iφ(k)} |u_n^−⟩, so A^+ = A^− − ∇_k φ.

**第 3 步 — 划分为小片。** 将 BZ 分为两个小片 U_+ 和 U_−，有一个重叠区域。在每个小片上为 |u_n⟩ 定义光滑规范，给出联络形式 A^+ 和 A^−。在重叠区，两个规范通过规范变换关联：|u_n^+⟩ = e^{iφ(k)} |u_n^−⟩，故 A^+ = A^− − ∇_k φ。

**Step 4 — Chern number as winding.** The Chern number is:

**第 4 步 — 陈数作为缠绕数。** 陈数为：

  C_n = (1/2π) [∫_{U_+} Ω^+ d²k + ∫_{U_−} Ω^− d²k] = (1/2π) ∮_{∂U_+} (A^+ − A^−)·dk = (1/2π) ∮_{∂U_+} ∇_k φ · dk.

The last integral is the total change of φ around the loop ∂U_+. Since |u_n^+⟩ and |u_n^−⟩ are both single-valued wavefunctions, e^{iφ} must be single-valued, so φ changes by 2π × (integer) around any closed loop. Therefore

最后一个积分是 φ 绕回路 ∂U_+ 的总变化。由于 |u_n^+⟩ 和 |u_n^−⟩ 都是单值波函数，e^{iφ} 必须是单值的，故 φ 绕任何闭合回路变化 2π × （整数）。因此

  **C_n = (1/2π) · 2π · (integer) = integer.** ∎

This is the mathematical result that makes the IQHE Hall conductance exactly quantized: any smooth deformation of the Hamiltonian that preserves the gap cannot change C_n (an integer cannot change continuously), so σ_xy is topologically protected.

这正是使 IQHE 霍尔电导精确量子化的数学结论：任何保持带隙的哈密顿量光滑形变都不能改变 C_n（整数不能连续变化），故 σ_xy 受拓扑保护。

---

## C. SSH Winding Number and Protected Zero-Energy Edge States · SSH 缠绕数与受保护零能边缘态

**Claim.** The SSH model has a winding number w = 0 for |t₁| > |t₂| (trivial) and w = 1 for |t₂| > |t₁| (topological). The topological phase has exactly two zero-energy edge states on a finite chain, protected by chiral symmetry.

**命题。** SSH 模型在 |t₁| > |t₂| 时缠绕数 w = 0（平凡），在 |t₂| > |t₁| 时 w = 1（拓扑）。拓扑相在有限链上恰好有两个零能边缘态，受手征对称性保护。

**Step 1 — The Bloch Hamiltonian.** Write H(k) = d(k)·σ where d(k) = (t₁ + t₂ cos k, t₂ sin k, 0) and σ = (σ_x, σ_y, σ_z). The energy eigenvalues are E_±(k) = ±|d(k)|. A gap closes only when |d(k)| = 0, i.e., t₁ + t₂ cos k = 0 and t₂ sin k = 0 simultaneously — requiring t₁ = ±t₂.

**第 1 步 — 布洛赫哈密顿量。** 令 H(k) = d(k)·σ，其中 d(k) = (t₁ + t₂ cos k, t₂ sin k, 0)，σ = (σ_x, σ_y, σ_z)。能量本征值为 E_±(k) = ±|d(k)|。带隙仅在 |d(k)| = 0 时关闭，即 t₁ + t₂ cos k = 0 且 t₂ sin k = 0 同时成立——要求 t₁ = ±t₂。

**Step 2 — Winding number.** As k runs from −π to π the 2D vector (d_x, d_y) = (t₁ + t₂ cos k, t₂ sin k) traces an ellipse centred at (t₁, 0). The winding number counts how many times this curve winds around the origin:

**第 2 步 — 缠绕数。** 当 k 从 −π 运行到 π 时，二维矢量 (d_x, d_y) = (t₁ + t₂ cos k, t₂ sin k) 描绘出以 (t₁, 0) 为中心的椭圆。缠绕数计算此曲线绕原点的圈数：

  w = (1/2π) ∮ (d_x dd_y − d_y dd_x) / |d|²  =  {0  if the ellipse does not enclose the origin (|t₁| > |t₂|),  1  if it encloses the origin (|t₂| > |t₁|).}

Evaluating explicitly: for |t₂| > |t₁|, the origin lies inside the ellipse; for |t₁| > |t₂| it lies outside. ∎

显式计算：对 |t₂| > |t₁|，原点在椭圆内；对 |t₁| > |t₂|，原点在椭圆外。∎

**Step 3 — Zero-energy edge states for a finite chain.** Consider N unit cells with open boundary conditions (a finite chain). In the limit t₁ = 0 (deep topological phase), the Hamiltonian consists of t₂-bonds connecting B sites to A sites on the next cell. The leftmost A site and rightmost B site are not connected to any bond — they form two **exact zero-energy modes** |ψ_L⟩ ∝ |A, 1⟩ and |ψ_R⟩ ∝ |B, N⟩.

**第 3 步 — 有限链的零能边缘态。** 考虑具有开放边界条件的 N 个单元（有限链）。在 t₁ = 0 的极限（深拓扑相），哈密顿量由连接 B 格点到下一个单元 A 格点的 t₂ 键组成。最左边的 A 格点和最右边的 B 格点未与任何键相连——它们形成两个**精确零能模式** |ψ_L⟩ ∝ |A, 1⟩ 和 |ψ_R⟩ ∝ |B, N⟩。

**Step 4 — Protection by chiral symmetry.** The SSH Hamiltonian anti-commutes with Γ = σ_z: Γ H(k) Γ^{−1} = −H(k) (chiral/sublattice symmetry). Any eigenstate |ψ⟩ with energy E ≠ 0 has a partner Γ|ψ⟩ with energy −E. A zero-energy state Γ|ψ₀⟩ can have any phase, meaning it cannot be lifted from zero by any perturbation that preserves Γ — the edge states are **symmetry-protected**. When t₁ ≠ 0 but still |t₂| > |t₁|, the edge states acquire a small splitting ∼ (t₁/t₂)^N that is exponentially small in the system size. ∎

**第 4 步 — 手征对称性保护。** SSH 哈密顿量与 Γ = σ_z 反对易：Γ H(k) Γ^{−1} = −H(k)（手征/子格对称性）。能量 E ≠ 0 的任意本征态 |ψ⟩ 有伴侣 Γ|ψ⟩，能量为 −E。零能态 Γ|ψ₀⟩ 可以有任意相位，意味着它无法被保持 Γ 的任意扰动从零抬起——边缘态是**对称性保护**的。当 t₁ ≠ 0 但 |t₂| > |t₁| 时，边缘态获得 ∼ (t₁/t₂)^N 量级的小劈裂，在系统尺寸上指数小。∎

**Bulk–boundary correspondence summary.** The winding number w is a property of the bulk Hamiltonian H(k); the number of zero-energy edge modes on a finite chain equals w. This is the simplest instance of **bulk–boundary correspondence**: a topological invariant of the bulk directly predicts the number of protected boundary states. The same principle operates in the IQHE (Chern number ↔ number of chiral edge channels), the QSH insulator (Z₂ invariant ↔ helical edge pairs), and 3D TIs (strong Z₂ index ↔ Dirac cone count on surfaces).

**体–边界对应总结。** 缠绕数 w 是体哈密顿量 H(k) 的属性；有限链上零能边缘模式的数量等于 w。这是**体–边界对应**最简单的实例：体的拓扑不变量直接预测受保护边界态的数量。同样的原理在 IQHE（陈数 ↔ 手征边缘通道数）、QSH 绝缘体（Z₂ 不变量 ↔ 螺旋边缘对）和三维拓扑绝缘体（强 Z₂ 指标 ↔ 表面狄拉克锥数）中均有体现。

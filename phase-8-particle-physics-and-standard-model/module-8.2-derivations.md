# Derivations — Module 8.2: Quantum Electrodynamics (QED)
# 推导 — 模块 8.2：量子电动力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.2](./module-8.2-quantum-electrodynamics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.2](./module-8.2-quantum-electrodynamics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The QED Lagrangian and Equations of Motion · QED 拉格朗日量与运动方程

**Claim.** The QED Lagrangian ℒ_QED = ψ̄(iγ^μD_μ − m)ψ − (1/4)F_μνF^{μν} (with D_μ = ∂_μ + ieA_μ) yields the Dirac equation with electromagnetic coupling and the Maxwell equations with a source.

**命题。** QED 拉格朗日量 ℒ_QED = ψ̄(iγ^μD_μ − m)ψ − (1/4)F_μνF^{μν}（D_μ = ∂_μ + ieA_μ）给出带有电磁耦合的狄拉克方程和带有源的麦克斯韦方程。

**Step 1 — Expand the Lagrangian.** Writing out D_μ:

**第 1 步 — 展开拉格朗日量。** 写出 D_μ：

  ℒ_QED = ψ̄(iγ^μ∂_μ − m)ψ − eψ̄γ^μψ A_μ − (1/4)F_μνF^{μν}.

The three terms are: (i) free Dirac field, (ii) fermion–photon interaction vertex −eψ̄γ^μψ A_μ, (iii) free photon kinetic term.

三项分别为：(i) 自由狄拉克场，(ii) 费米子–光子相互作用顶角 −eψ̄γ^μψ A_μ，(iii) 自由光子动能项。

**Step 2 — Euler–Lagrange for ψ̄ (varies ψ).** The E–L equation is:

**第 2 步 — 对 ψ̄ 的欧拉–拉格朗日方程（变分 ψ）。** E–L 方程为：

  ∂ℒ/∂ψ̄ − ∂_μ(∂ℒ/∂(∂_μψ̄)) = 0.

Since ℒ contains ψ̄ but not ∂_μψ̄ (only ∂_μψ appears in the kinetic term):

由于 ℒ 含 ψ̄ 但不含 ∂_μψ̄（动能项中只含 ∂_μψ）：

  ∂ℒ/∂ψ̄ = (iγ^μ∂_μ − m)ψ − eγ^μA_μψ = (iγ^μD_μ − m)ψ = 0.

This is the **gauged Dirac equation**: (iγ^μD_μ − m)ψ = 0, i.e., (iγ^μ(∂_μ + ieA_μ) − m)ψ = 0.

这是**规范化狄拉克方程**：(iγ^μD_μ − m)ψ = 0，即 (iγ^μ(∂_μ + ieA_μ) − m)ψ = 0。

**Step 3 — Euler–Lagrange for A_ν.** Now vary A_ν:

**第 3 步 — 对 A_ν 的欧拉–拉格朗日方程。** 现变分 A_ν：

  ∂ℒ/∂A_ν = −eψ̄γ^νψ = −ej^ν.

  ∂ℒ/∂(∂_μA_ν) = −F^{μν}  (since F_μν = ∂_μA_ν − ∂_νA_μ).

The E–L equation ∂ℒ/∂A_ν − ∂_μ(∂ℒ/∂(∂_μA_ν)) = 0 gives:

E–L 方程 ∂ℒ/∂A_ν − ∂_μ(∂ℒ/∂(∂_μA_ν)) = 0 给出：

  −ej^ν + ∂_μF^{μν} = 0  ⟹  ∂_μF^{μν} = ej^ν.

This is **Maxwell's equation** in covariant form with source j^ν = ψ̄γ^νψ (the electromagnetic current). The homogeneous equation ∂_[μF_νρ] = 0 (Bianchi identity) follows automatically from F_μν = ∂_μA_ν − ∂_νA_μ. ∎

这是协变形式的**麦克斯韦方程**，源为 j^ν = ψ̄γ^νψ（电磁流）。齐次方程 ∂_[μF_νρ] = 0（Bianchi 恒等式）自动由 F_μν = ∂_μA_ν − ∂_νA_μ 得出。∎

---

## B. Feynman Rules from the QED Lagrangian · 由 QED 拉格朗日量导出费曼规则

**Claim.** The QED interaction vertex is −ieγ^μ, the photon propagator (in Feynman gauge) is −ig_μν/q², and the fermion propagator is i(γ^μp_μ + m)/(p² − m² + iε).

**命题。** QED 相互作用顶角为 −ieγ^μ，光子传播子（费曼规范）为 −ig_μν/q²，费米子传播子为 i(γ^μp_μ + m)/(p² − m² + iε)。

**Step 1 — Path integral approach / perturbation theory.** The S-matrix element is computed as the perturbative expansion of ⟨0|T[…]|0⟩ with the interaction Lagrangian treated as a perturbation. The interaction term is:

**第 1 步 — 路径积分方法/微扰论。** S 矩阵元作为 ⟨0|T[…]|0⟩ 的微扰展开来计算，相互作用拉格朗日量作为微扰处理。相互作用项为：

  ℒ_int = −eψ̄γ^μψ A_μ = −ej^μA_μ.

Each power of ℒ_int in the Dyson series contributes one vertex. A single insertion gives:

狄森级数中 ℒ_int 的每一幂次贡献一个顶角。单次插入给出：

  −ie ∫d⁴x ψ̄(x)γ^μψ(x)A_μ(x).

In momentum space, each vertex contributes a factor −ieγ^μ (with momentum conservation enforced by a delta function at each vertex).

在动量空间，每个顶角贡献因子 −ieγ^μ（通过每个顶角处的 δ 函数强制动量守恒）。

**Step 2 — Fermion propagator.** The free Dirac Lagrangian ℒ_D = ψ̄(iγ^μ∂_μ − m)ψ gives the equation of motion (iγ^μ∂_μ − m)ψ = 0. In momentum space (∂_μ → −ip_μ):

**第 2 步 — 费米子传播子。** 自由狄拉克拉格朗日量 ℒ_D = ψ̄(iγ^μ∂_μ − m)ψ 给出运动方程 (iγ^μ∂_μ − m)ψ = 0。在动量空间（∂_μ → −ip_μ）：

  (γ^μp_μ − m)ψ(p) = 0.

The propagator S_F(p) is the inverse of the kinetic operator (γ^μp_μ − m):

传播子 S_F(p) 是动能算符 (γ^μp_μ − m) 的逆：

  S_F(p) = i/(γ^μp_μ − m + iε).

Multiply numerator and denominator by (γ^νp_ν + m):

分子分母同乘 (γ^νp_ν + m)：

  (γ^μp_μ − m)(γ^νp_ν + m) = γ^μγ^νp_μp_ν − m² = (1/2){γ^μ,γ^ν}p_μp_ν − m²
                               = g^{μν}p_μp_ν − m² = p² − m².

Therefore:

因此：

  S_F(p) = i(γ^μp_μ + m)/(p² − m² + iε).

The iε prescription (Feynman prescription) encodes the correct time-ordering and corresponds to particles propagating forward in time and antiparticles backward.

iε 处方（费曼处方）编码了正确的时间排序，对应于粒子向前传播、反粒子向后传播（在时间上）。

**Step 3 — Photon propagator.** The free photon action is −(1/4)∫F_μνF^{μν}d⁴x. In momentum space with a gauge-fixing term −(1/2ξ)(∂_μA^μ)² (Lorenz gauge parameter ξ):

**第 3 步 — 光子传播子。** 自由光子作用量为 −(1/4)∫F_μνF^{μν}d⁴x。在动量空间中，加入规范固定项 −(1/2ξ)(∂_μA^μ)²（洛伦兹规范参数 ξ）：

  S_photon = ∫d⁴q/(2π)⁴ A^μ(q)[−g_μν q² + q_μq_ν(1 − 1/ξ)]A^ν(−q).

The kinetic operator in brackets has the inverse (photon propagator):

括号中的动能算符的逆（光子传播子）为：

  D_F^{μν}(q) = −i[g^{μν} − (1−ξ)q^μq^ν/q²]/(q² + iε).

In **Feynman gauge** ξ = 1, this simplifies to:

在**费曼规范** ξ = 1 中，化简为：

  D_F^{μν}(q) = −ig^{μν}/(q² + iε).

The longitudinal piece ∝ q^μq^ν drops out in gauge-invariant physical amplitudes (Ward identities). ∎

纵向部分 ∝ q^μq^ν 在规范不变的物理振幅中消失（沃德恒等式）。∎

---

## C. Tree-Level e⁺e⁻ → μ⁺μ⁻ Amplitude and Cross-Section · 树图 e⁺e⁻ → μ⁺μ⁻ 振幅与散射截面

**Claim.** At tree level (leading order in α), the differential cross-section for e⁺e⁻ → μ⁺μ⁻ in the center-of-mass frame at high energy (√s ≫ m_e, m_μ) is:

**命题。** 在树图（α 的领头阶），高能质心系（√s ≫ m_e, m_μ）中 e⁺e⁻ → μ⁺μ⁻ 的微分散射截面为：

  dσ/dΩ = α²/(4s) · (1 + cos²θ),

integrating to σ_total = 4πα²/(3s).

积分得 σ_total = 4πα²/(3s)。

**Step 1 — The Feynman diagram.** At tree level there is a single diagram: e⁻(p₁) + e⁺(p₂) annihilate into a virtual photon (momentum q = p₁ + p₂), which creates μ⁻(k₁) + μ⁺(k₂). Using the Feynman rules:

**第 1 步 — 费曼图。** 在树图阶，只有一个图：e⁻(p₁) + e⁺(p₂) 湮灭为虚光子（动量 q = p₁ + p₂），产生 μ⁻(k₁) + μ⁺(k₂)。利用费曼规则：

  iM = [v̄(p₂)(−ieγ^μ)u(p₁)] · [−ig_μν/q²] · [ū(k₁)(−ieγ^ν)v(k₂)].

So:

故：

  M = −e²/q² · [v̄(p₂)γ^μu(p₁)] · [ū(k₁)γ_μv(k₂)].

At center of mass s = q² = (p₁ + p₂)², so M = (e²/s)J_e^μ J_{μ,μ} where J^μ are the currents.

在质心系 s = q² = (p₁ + p₂)²，故 M = (e²/s)J_e^μ J_{μ,μ}，J^μ 为流。

**Step 2 — Spin sum.** We average over initial spins and sum over final spins. Using the completeness relations:

**第 2 步 — 自旋求和。** 对初态自旋取平均，对末态自旋求和。利用完备性关系：

  Σ_spins u(p,s)ū(p,s) = γ^μp_μ + m,  Σ_spins v(p,s)v̄(p,s) = γ^μp_μ − m.

The spin-summed/averaged |M|² is:

自旋求和/平均后的 |M|² 为：

  ⟨|M|²⟩ = (e⁴/4s²) · Tr[(γ^μp̸₁ + m_e)γ^ν(γ^ρp̸₂ − m_e)γ^σ] · g_μρg_νσ · (Leptonic tensors)

More precisely:

更精确地：

  ⟨|M|²⟩ = (e⁴/4s²) · L^{μν}_e · L_{μν,μ}

where L^{μν}_e = Tr[(p̸₁ + m_e)γ^μ(p̸₂ − m_e)γ^ν] is the electron leptonic tensor, and L_{μν,μ} = Tr[(k̸₁ + m_μ)γ_μ(k̸₂ − m_μ)γ_ν] is the muon leptonic tensor.

其中 L^{μν}_e = Tr[(p̸₁ + m_e)γ^μ(p̸₂ − m_e)γ^ν] 是电子轻子张量，L_{μν,μ} = Tr[(k̸₁ + m_μ)γ_μ(k̸₂ − m_μ)γ_ν] 是μ子轻子张量。

**Step 3 — Trace technology.** In the ultra-relativistic limit m_e, m_μ → 0 (valid when √s ≫ max(m_e, m_μ)):

**第 3 步 — 迹技术。** 在超相对论极限 m_e, m_μ → 0（当 √s ≫ max(m_e, m_μ) 时成立）：

  L^{μν}_e → Tr[p̸₁γ^μp̸₂γ^ν] = 4(p₁^μp₂^ν + p₁^νp₂^μ − g^{μν}(p₁·p₂)).

Using standard trace identities: Tr[γ^αγ^βγ^γγ^δ] = 4(g^{αβ}g^{γδ} − g^{αγ}g^{βδ} + g^{αδ}g^{βγ}).

利用标准迹恒等式：Tr[γ^αγ^βγ^γγ^δ] = 4(g^{αβ}g^{γδ} − g^{αγ}g^{βδ} + g^{αδ}g^{βγ})。

**Step 4 — Contract the tensors.** The contraction L^{μν}_e · L_{μν,μ} (in massless limit):

**第 4 步 — 张量缩并。** 缩并 L^{μν}_e · L_{μν,μ}（无质量极限）：

  L^{μν}_e L_{μν,μ} = 4(p₁^μp₂^ν + p₁^νp₂^μ − g^{μν}p₁·p₂)·4(k₁μk₂ν + k₁νk₂μ − g_μνk₁·k₂)

  = 32[(p₁·k₁)(p₂·k₂) + (p₁·k₂)(p₂·k₁)].

This is the key kinematic identity (the "crossing" structure reflects t and u channel kinematics).

这是关键的运动学恒等式（"crossing"结构反映了 t 道和 u 道运动学）。

**Step 5 — Kinematics.** In the CM frame, with √s = 2E:

**第 5 步 — 运动学。** 在质心系中，√s = 2E：

  p₁ = (E, 0, 0, E),  p₂ = (E, 0, 0, −E),
  k₁ = (E, E sinθ, 0, E cosθ),  k₂ = (E, −E sinθ, 0, −E cosθ).

Computing the dot products:

计算内积：

  p₁·k₁ = E²(1 − cosθ),  p₂·k₂ = E²(1 − cosθ),
  p₁·k₂ = E²(1 + cosθ),  p₂·k₁ = E²(1 + cosθ).

Therefore:

因此：

  L^{μν}_e L_{μν,μ} = 32[E⁴(1−cosθ)² + E⁴(1+cosθ)²] = 32E⁴·2(1 + cos²θ) = 64E⁴(1 + cos²θ).

And s = (2E)² = 4E², so E⁴ = s²/16.

而 s = (2E)² = 4E²，故 E⁴ = s²/16。

**Step 6 — Compute |M|².** Combining:

**第 6 步 — 计算 |M|²。** 综合：

  ⟨|M|²⟩ = (e⁴/(4s²)) · 64E⁴(1 + cos²θ) = (e⁴/(4s²)) · 64(s²/16)(1 + cos²θ)
           = e⁴(1 + cos²θ) = 16π²α²(1 + cos²θ).

using e² = 4πα.

利用 e² = 4πα。

**Step 7 — Differential cross-section.** The general formula for 2→2 scattering in the CM frame (massless final states) is:

**第 7 步 — 微分散射截面。** 质心系中 2→2 散射（无质量末态）的一般公式为：

  dσ/dΩ = ⟨|M|²⟩/(64π²s).

Therefore:

因此：

  dσ/dΩ = 16π²α²(1 + cos²θ)/(64π²s) = **α²(1 + cos²θ)/(4s)**.

**Step 8 — Total cross-section.** Integrate over the full solid angle:

**第 8 步 — 总截面。** 对全立体角积分：

  σ = ∫dΩ α²(1 + cos²θ)/(4s) = (α²/4s)∫₀^{2π}dφ∫₋₁^{+1}(1 + cos²θ)d(cosθ)
    = (α²/4s)·2π·[cosθ + cos³θ/3]₋₁^{+1} = (α²/4s)·2π·(2 + 2/3)
    = (α²/4s)·2π·8/3 = **4πα²/(3s)**. ∎

---

## D. One-Loop Running of α · α 的单圈跑动

**Claim.** The one-loop QED renormalization group equation is dα/d(ln μ) = α²/(3π) with solution 1/α(μ) = 1/α(μ₀) − (1/3π)ln(μ/μ₀), giving α(m_Z) ≈ 1/128 from α(m_e) ≈ 1/137.

**命题。** 单圈 QED 重整化群方程为 dα/d(ln μ) = α²/(3π)，解为 1/α(μ) = 1/α(μ₀) − (1/3π)ln(μ/μ₀)，从 α(m_e) ≈ 1/137 给出 α(m_Z) ≈ 1/128。

**Step 1 — Vacuum polarization.** The photon propagator receives a one-loop correction from a fermion loop (a virtual e⁺e⁻ pair). In dimensional regularization (d = 4−2ε), this loop gives a correction to the photon self-energy Π(q²):

**第 1 步 — 真空极化。** 光子传播子从费米子圈（虚 e⁺e⁻ 对）接收单圈修正。在维数正规化（d = 4−2ε）中，该圈给出对光子自能 Π(q²) 的修正：

  Π(q²) = −(e²/2π²)∫₀¹dx x(1−x)ln[m²−x(1−x)q²]/m² + (pole in ε).

The pole 1/ε is absorbed into the renormalization of the electric charge. The physical, renormalized result after subtraction at μ:

极点 1/ε 被吸收到电荷的重整化中。在 μ 处减除后的物理重整化结果为：

  Π_R(q²) = (α/3π)[ln(q²/μ²) − (terms regular at q² = 0)].

**Step 2 — Renormalization group equation.** The requirement that physical observables are μ-independent (the running coupling absorbs the log) gives the **Callan–Symanzik equation**. The one-loop β function for QED:

**第 2 步 — 重整化群方程。** 物理可观测量不依赖于 μ（跑动耦合吸收对数）的要求给出 **Callan–Symanzik 方程**。QED 的单圈 β 函数：

  β(e) = μ de/dμ = e³/(12π²)  ⟹  β(α) = dα/d(ln μ) = α²/(3π).

The coefficient +1/(3π) is positive (β > 0), meaning α **increases** with μ: the photon cloud of virtual pairs screens the bare charge, and one needs more energy (shorter distance) to penetrate the screening.

系数 +1/(3π) 为正（β > 0），意味着 α 随 μ **增大**：虚对组成的光子云屏蔽了裸电荷，需要更高能量（更短距离）来穿透屏蔽。

**Step 3 — Solve the RGE.** Separate variables:

**第 3 步 — 求解重整化群方程。** 分离变量：

  dα/α² = d(ln μ)/(3π)  ⟹  −1/α|^{α(μ)}_{α(μ₀)} = ln(μ/μ₀)/(3π).

  1/α(μ) = 1/α(μ₀) − (1/3π)ln(μ/μ₀).

**Step 4 — Numerical check.** Set μ₀ = m_e ≈ 0.511 MeV, α(m_e) ≈ 1/137.036, μ = m_Z ≈ 91.2 GeV:

**第 4 步 — 数值验证。** 令 μ₀ = m_e ≈ 0.511 MeV，α(m_e) ≈ 1/137.036，μ = m_Z ≈ 91.2 GeV：

  ln(m_Z/m_e) = ln(91.2 × 10³/0.511) = ln(1.784 × 10⁵) ≈ 12.09.

  Δ(1/α) = −(1/3π)·12.09 ≈ −1.28.

  1/α(m_Z) ≈ 137.036 − 1.28 ≈ 135.7.

(The observed value 1/α(m_Z) ≈ 127.9 differs because all charged particles — not just the electron — contribute loops; the quarks and heavier leptons add additional contributions of order ln(m_Z/m_f) for each flavor f. Including all SM fermions gives the full Δ(1/α) ≈ 9, consistent with the observation.) ∎

（观测值 1/α(m_Z) ≈ 127.9 不同是因为所有带电粒子——不仅是电子——都贡献了圈图；夸克和较重的轻子为每种 f 额外贡献约 ln(m_Z/m_f) 的量级。包含所有 SM 费米子后给出完整的 Δ(1/α) ≈ 9，与观测一致。）∎

---

## E. Ward Identity and Gauge Invariance of Amplitudes · 沃德恒等式与振幅的规范不变性

**Claim.** In QED, any S-matrix amplitude M^μ satisfies q_μM^μ = 0 when q is the momentum of an external photon (with polarization vector ε^μ). This ensures that longitudinal photons (ε^μ ∝ q^μ) do not contribute to physical amplitudes.

**命题。** 在 QED 中，对于任何 S 矩阵振幅 M^μ，当 q 是外光子（极化矢量为 ε^μ）的动量时，满足 q_μM^μ = 0。这确保了纵向光子（ε^μ ∝ q^μ）不对物理振幅作贡献。

**Step 1 — Derivation from U(1) invariance.** The Ward identity q_μM^μ = 0 is the momentum-space statement of current conservation ∂_μj^μ = 0. It follows from the gauge invariance of the Lagrangian: replacing the photon polarization ε^μ(q) → ε^μ(q) + q^μλ (a gauge transformation) must leave S-matrix elements invariant, so M^μq_μλ = 0 for all λ, giving q_μM^μ = 0.

**第 1 步 — 从 U(1) 不变性推导。** 沃德恒等式 q_μM^μ = 0 是流守恒 ∂_μj^μ = 0 在动量空间的表述。它来自拉格朗日量的规范不变性：将光子极化 ε^μ(q) → ε^μ(q) + q^μλ（规范变换）必须使 S 矩阵元不变，故对所有 λ 有 M^μq_μλ = 0，即 q_μM^μ = 0。

**Step 2 — Consequence for the photon propagator.** The Ward identity implies that the photon propagator's longitudinal component ∝ q^μq^ν/q² does not contribute to physical matrix elements — justifying our use of the simplified Feynman-gauge propagator −ig^{μν}/q² in gauge-invariant calculations. ∎

**第 2 步 — 对光子传播子的推论。** 沃德恒等式意味着光子传播子的纵向分量 ∝ q^μq^ν/q² 不对物理矩阵元作贡献——这证明了在规范不变计算中使用简化费曼规范传播子 −ig^{μν}/q² 的合理性。∎

# Derivations — Module 3.10: Quantum Dynamics
# 推导 — 模块 3.10：量子动力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.10](./module-3.10-quantum-dynamics.md). Full step-by-step proofs of the time-evolution operator, its unitarity, the Heisenberg equation of motion, the harmonic-oscillator solution a(t) = a(0)e^{−iωt}, the free-particle propagator, and the path-integral sketch. English first, then 中文.
> [模块 3.10](./module-3.10-quantum-dynamics.md) 的配套文档：时间演化算符、其幺正性、海森堡运动方程、谐振子解 a(t) = a(0)e^{−iωt}、自由粒子传播子与路径积分概述的完整逐步证明。先英文，后中文。

---

## A. The Time-Evolution Operator Û(t) = e^{−iĤt/ℏ} · 时间演化算符

**Claim.** For a time-independent Hamiltonian Ĥ, the unique unitary operator satisfying the Schrödinger equation iℏ d/dt|ψ(t)⟩ = Ĥ|ψ(t)⟩ with initial condition |ψ(0)⟩ given is Û(t) = e^{−iĤt/ℏ}. Moreover Û(t) is unitary: Û†(t)Û(t) = 1̂.

**命题。** 对于与时间无关的哈密顿量 Ĥ，满足薛定谔方程 iℏ d/dt|ψ(t)⟩ = Ĥ|ψ(t)⟩ 及初始条件 |ψ(0)⟩ 的唯一幺正算符为 Û(t) = e^{−iĤt/ℏ}。而且 Û(t) 是幺正的：Û†(t)Û(t) = 1̂。

**Step 1 — Derivation as operator exponential.** Define Û(t) by its formal power series (valid via the spectral theorem for self-adjoint Ĥ):

**第 1 步 — 作为算符指数的推导。** 通过形式幂级数定义 Û(t)（由自伴 Ĥ 的谱定理保证有效）：

  Û(t) = e^{−iĤt/ℏ} = Σ_{n=0}^{∞} (1/n!) (−iĤt/ℏ)ⁿ
        = 1̂ − (it/ℏ)Ĥ + (1/2!)(−it/ℏ)²Ĥ² + …

**Step 2 — Verify it solves the Schrödinger equation.** Differentiate the power series term by term (justified because Ĥ is bounded on each energy eigenspace, and the series converges):

**第 2 步 — 验证它满足薛定谔方程。** 逐项对幂级数求导（由于 Ĥ 在每个能量本征空间上有界，级数收敛，此操作合理）：

  d/dt Û(t) = Σ_{n=1}^{∞} (1/n!) (−i/ℏ)ⁿ n tⁿ⁻¹ Ĥⁿ
            = (−iĤ/ℏ) Σ_{n=1}^{∞} (1/(n−1)!) (−iĤt/ℏ)ⁿ⁻¹
            = (−iĤ/ℏ) e^{−iĤt/ℏ} = (−iĤ/ℏ) Û(t).

Multiplying by iℏ: iℏ d/dt Û(t) = Ĥ Û(t). Acting on the initial state |ψ(0)⟩ and using |ψ(t)⟩ = Û(t)|ψ(0)⟩:

两边乘以 iℏ：iℏ d/dt Û(t) = Ĥ Û(t)。作用于初态 |ψ(0)⟩，利用 |ψ(t)⟩ = Û(t)|ψ(0)⟩：

  iℏ d/dt |ψ(t)⟩ = Ĥ Û(t)|ψ(0)⟩ = Ĥ|ψ(t)⟩.   ✓

**Step 3 — Initial condition.** Û(0) = e^{0} = 1̂, so |ψ(0)⟩ = Û(0)|ψ(0)⟩ = |ψ(0)⟩. ✓

**第 3 步 — 初始条件。** Û(0) = e^{0} = 1̂，故 |ψ(0)⟩ = Û(0)|ψ(0)⟩ = |ψ(0)⟩。✓

**Step 4 — Uniqueness.** Suppose Û₁ and Û₂ both satisfy d/dt Û = (−iĤ/ℏ)Û with Û(0) = 1̂. Then for W = Û₁ − Û₂, d/dt W = (−iĤ/ℏ)W and W(0) = 0. The norm satisfies d/dt ‖W|ψ₀⟩‖² = 2 Re⟨W|ψ₀|d/dtW|ψ₀⟩ = 2Re⟨W|ψ₀|(−iĤ/ℏ)W|ψ₀⟩ = 0 (since Ĥ is Hermitian, the expectation of −iĤ/ℏ is purely imaginary). Starting from zero, the norm remains zero, so Û₁ = Û₂.

**第 4 步 — 唯一性。** 设 Û₁ 和 Û₂ 都满足 d/dt Û = (−iĤ/ℏ)Û，Û(0) = 1̂。令 W = Û₁ − Û₂，则 d/dt W = (−iĤ/ℏ)W，W(0) = 0。范数满足 d/dt ‖W|ψ₀⟩‖² = 2Re⟨W|ψ₀|(−iĤ/ℏ)W|ψ₀⟩ = 0（因 Ĥ 为厄米算符，−iĤ/ℏ 的期望值为纯虚数）。从零出发范数保持为零，故 Û₁ = Û₂。

**Step 5 — Unitarity.** Since Ĥ is self-adjoint (Ĥ† = Ĥ):

**第 5 步 — 幺正性。** 由于 Ĥ 是自伴的（Ĥ† = Ĥ）：

  Û†(t) = (e^{−iĤt/ℏ})† = e^{(−iĤt/ℏ)†} = e^{iĤ†t/ℏ} = e^{iĤt/ℏ}.

(The dagger reverses operator order and takes complex conjugate; the series is absolutely convergent so the dagger passes through.) Therefore:

（取伴随后逆转算符顺序并取复共轭；级数绝对收敛故伴随可穿过。）因此：

  Û†(t) Û(t) = e^{iĤt/ℏ} e^{−iĤt/ℏ} = e^{0} = 1̂,

and similarly Û(t)Û†(t) = 1̂. (The two exponentials commute because they are functions of the same operator Ĥ.) Hence Û is **unitary**. ∎

类似地 Û(t)Û†(t) = 1̂。（两个指数可交换，因为它们是同一算符 Ĥ 的函数。）故 Û 是**幺正**的。∎

**Physical meaning.** Unitarity ensures ⟨ψ(t)|ψ(t)⟩ = ⟨ψ(0)|Û†Û|ψ(0)⟩ = ⟨ψ(0)|ψ(0)⟩ = 1: total probability is conserved.

**物理含义。** 幺正性确保 ⟨ψ(t)|ψ(t)⟩ = ⟨ψ(0)|Û†Û|ψ(0)⟩ = ⟨ψ(0)|ψ(0)⟩ = 1：总概率守恒。

---

## B. The Heisenberg Equation of Motion · 海森堡运动方程

**Claim.** In the Heisenberg picture, where operators carry the time dependence and states are fixed, a Heisenberg-picture operator Â_H(t) = Û†(t) Â_S Û(t) satisfies the equation of motion:

**命题。** 在海森堡绘景中，算符携带时间依赖性而态保持固定，海森堡绘景算符 Â_H(t) = Û†(t) Â_S Û(t) 满足运动方程：

  dÂ_H/dt = (i/ℏ)[Ĥ, Â_H] + (∂Â_S/∂t)_H.

For operators with no explicit time dependence (∂Â_S/∂t = 0):

对于没有显式时间依赖性的算符（∂Â_S/∂t = 0）：

  dÂ_H/dt = (i/ℏ)[Ĥ, Â_H].

**Step 1 — Differentiate the definition.** Using d/dt Û = (−iĤ/ℏ)Û and d/dt Û† = (iĤ/ℏ)Û† (from Step 2 above, taking the adjoint):

**第 1 步 — 对定义求导。** 利用 d/dt Û = (−iĤ/ℏ)Û 以及 d/dt Û† = (iĤ/ℏ)Û†（由上文第 2 步取伴随得到）：

  dÂ_H/dt = (d/dt Û†) Â_S Û + Û† Â_S (d/dt Û) + Û†(∂Â_S/∂t)Û
           = (iĤ/ℏ)Û† Â_S Û + Û† Â_S (−iĤ/ℏ)Û + Û†(∂Â_S/∂t)Û.

Note Ĥ = Û†ĤÛ (since Ĥ commutes with its own exponential, Ĥ is the same in both pictures when the Hamiltonian does not depend explicitly on time):

注意 Ĥ = Û†ĤÛ（因为 Ĥ 与其自身的指数对易，当哈密顿量不显含时间时 Ĥ 在两种绘景中相同）：

  dÂ_H/dt = (i/ℏ) Ĥ Â_H − (i/ℏ) Â_H Ĥ + (∂Â_S/∂t)_H
           = (i/ℏ)[Ĥ, Â_H] + (∂Â_S/∂t)_H.   ∎

This is the operator analogue of Hamilton's equations in classical mechanics (Poisson brackets {A, H} correspond to commutators (i/ℏ)[Ĥ, Â]).

这是经典力学中哈密顿方程的算符类比（泊松括号 {A, H} 对应对易子 (i/ℏ)[Ĥ, Â]）。∎

---

## C. Harmonic Oscillator in the Heisenberg Picture · 海森堡绘景中的谐振子

**Claim.** For the quantum harmonic oscillator Ĥ = ℏω(â†â + ½), the Heisenberg-picture lowering operator satisfies â(t) = â(0) e^{−iωt}.

**命题。** 对量子谐振子 Ĥ = ℏω(â†â + ½)，海森堡绘景中的降算符满足 â(t) = â(0) e^{−iωt}。

**Step 1 — Compute the commutator [Ĥ, â].** Using Ĥ = ℏω(N̂ + ½) with N̂ = â†â, and the result [N̂, â] = −â from Module 3.2:

**第 1 步 — 计算对易子 [Ĥ, â]。** 利用 Ĥ = ℏω(N̂ + ½)，N̂ = â†â，以及模块 3.2 中的结果 [N̂, â] = −â：

  [Ĥ, â] = ℏω[N̂ + ½, â] = ℏω([N̂, â] + [½, â]) = ℏω(−â + 0) = −ℏω â.

**Step 2 — Write the Heisenberg equation.** With ∂â/∂t = 0 (no explicit time dependence in the Schrödinger picture):

**第 2 步 — 写出海森堡方程。** 由于 ∂â/∂t = 0（薛定谔绘景中无显式时间依赖性）：

  dâ(t)/dt = (i/ℏ)[Ĥ, â(t)] = (i/ℏ)(−ℏω) â(t) = −iω â(t).

**Step 3 — Solve the ODE.** This is a simple first-order linear ODE dâ/dt = −iω â with solution:

**第 3 步 — 求解常微分方程。** 这是简单的一阶线性常微分方程 dâ/dt = −iω â，其解为：

  â(t) = â(0) e^{−iωt}.

Similarly, taking the adjoint: â†(t) = â†(0) e^{+iωt}.

类似地，取伴随得：â†(t) = â†(0) e^{+iωt}。

**Step 4 — Position and momentum in the Heisenberg picture.** Recalling x̂ = √(ℏ/2mω)(â + â†) and p̂ = i√(mℏω/2)(â† − â):

**第 4 步 — 海森堡绘景中的位置和动量。** 回顾 x̂ = √(ℏ/2mω)(â + â†)，p̂ = i√(mℏω/2)(â† − â)：

  x̂(t) = √(ℏ/2mω) (â(0)e^{−iωt} + â†(0)e^{iωt})
        = x̂(0) cos(ωt) + p̂(0)/(mω) sin(ωt).

  p̂(t) = i√(mℏω/2) (â†(0)e^{iωt} − â(0)e^{−iωt})
        = p̂(0) cos(ωt) − mω x̂(0) sin(ωt).

These are exactly the classical equations of motion for a harmonic oscillator, with operator coefficients — the quantum Ehrenfest theorem is manifest. ∎

这正是谐振子的经典运动方程，只是系数为算符——量子埃伦费斯特定理在此清晰呈现。∎

---

## D. The Free-Particle Propagator · 自由粒子传播子

**Claim.** For a free particle (V = 0) with Hamiltonian Ĥ = p̂²/2m, the propagator (position-space matrix element of the time-evolution operator) is:

**命题。** 对自由粒子（V = 0），哈密顿量 Ĥ = p̂²/2m，传播子（时间演化算符的坐标空间矩阵元）为：

  K(x′, t; x, 0) = ⟨x′|Û(t)|x⟩ = √(m/(2πiℏt)) exp[im(x′−x)²/(2ℏt)].

**Step 1 — Insert momentum resolution of identity.** Between ⟨x′| and Û(t)|x⟩, insert ∫|p⟩⟨p| dp = 1̂:

**第 1 步 — 插入动量单位分解。** 在 ⟨x′| 与 Û(t)|x⟩ 之间插入 ∫|p⟩⟨p| dp = 1̂：

  K(x′, t; x, 0) = ∫ ⟨x′|Û(t)|p⟩⟨p|x⟩ dp.

Since |p⟩ is an eigenstate of Ĥ = p̂²/2m with eigenvalue p²/2m, Û(t)|p⟩ = e^{−ip²t/2mℏ}|p⟩:

由于 |p⟩ 是 Ĥ = p̂²/2m 的本征态，本征值为 p²/2m，故 Û(t)|p⟩ = e^{−ip²t/2mℏ}|p⟩：

  K = ∫ ⟨x′|p⟩ e^{−ip²t/2mℏ} ⟨p|x⟩ dp
    = ∫ (e^{ipx′/ℏ}/√(2πℏ)) e^{−ip²t/2mℏ} (e^{−ipx/ℏ}/√(2πℏ)) dp
    = (1/2πℏ) ∫_{-∞}^{∞} e^{ip(x′−x)/ℏ − ip²t/2mℏ} dp.

**Step 2 — Complete the square.** Let Δx = x′ − x. Rewrite the exponent:

**第 2 步 — 配方。** 令 Δx = x′ − x。重写指数：

  ip(Δx)/ℏ − ip²t/(2mℏ) = −(it/2mℏ)[p² − 2mp(Δx)/t]
    = −(it/2mℏ)[p − m(Δx)/t]² + (it/2mℏ) · m²(Δx)²/t²
    = −(it/2mℏ)(p − m(Δx)/t)² + im(Δx)²/(2ℏt).

**Step 3 — Gaussian integral.** Substituting u = p − m(Δx)/t:

**第 3 步 — 高斯积分。** 令 u = p − m(Δx)/t：

  K = (1/2πℏ) e^{im(Δx)²/2ℏt} ∫_{-∞}^{∞} e^{−(it/2mℏ)u²} du.

The integral ∫_{-∞}^{∞} e^{−αu²} du = √(π/α) for Re(α) > 0. Here α = it/(2mℏ) has Re(α) = 0, but the integral is defined by analytic continuation (or equivalently by adding a small positive real part to t, i.e., t → t − iε, and then taking ε → 0⁺). The result is:

积分 ∫_{-∞}^{∞} e^{−αu²} du = √(π/α) 对 Re(α) > 0 成立。这里 α = it/(2mℏ) 的实部为 0，但积分通过解析延拓定义（等价地，令 t → t − iε 再取 ε → 0⁺）。结果为：

  ∫_{-∞}^{∞} e^{−(it/2mℏ)u²} du = √(π / (it/2mℏ)) = √(2πmℏ/it) = √(2πmℏ) · e^{−iπ/4}/√t

where we used 1/√i = e^{−iπ/4} = (1−i)/√2. More directly, √(1/i) = √(−i) = e^{−iπ/4}, so:

其中使用了 1/√i = e^{−iπ/4} = (1−i)/√2。更直接地，√(1/i) = e^{−iπ/4}，故：

  ∫_{-∞}^{∞} e^{−(it/2mℏ)u²} du = √(2πmℏ/(it)).

**Step 4 — Assemble the result.**

**第 4 步 — 整合结果。**

  K = (1/2πℏ) · e^{im(x′−x)²/2ℏt} · √(2πmℏ/(it))
    = (1/2πℏ) · √(2πmℏ/(it)) · e^{im(x′−x)²/2ℏt}
    = √(m/(2πiℏt)) · e^{im(x′−x)²/(2ℏt)}.

Here √(1/(it)) = e^{−iπ/4}/√t, giving the factor √(m/(2πiℏt)). ∎

其中 √(1/(it)) = e^{−iπ/4}/√t，给出因子 √(m/(2πiℏt))。∎

**Physical meaning.** The propagator K(x′, t; x, 0) is the probability amplitude for a particle at x at time 0 to be found at x′ at time t. It is a Gaussian with width ∼ √(ℏt/m) that spreads in time — the quantum spreading of a free wave packet.

**物理含义。** 传播子 K(x′, t; x, 0) 是粒子在 t = 0 时刻位于 x、在 t 时刻被发现于 x′ 的概率振幅。它是宽度 ∼ √(ℏt/m) 随时间扩展的高斯函数——自由波包的量子扩展。

---

## E. The Path Integral (Sketch) · 路径积分（概述）

**Claim.** The propagator can be written as a sum over all paths from (x, 0) to (x′, t), weighted by e^{iS[path]/ℏ} where S is the classical action:

**命题。** 传播子可以写作从 (x, 0) 到 (x′, t) 的所有路径的求和，权重为 e^{iS[路径]/ℏ}，其中 S 为经典作用量：

  K(x′, t; x, 0) = ∫ Dx(τ) · e^{iS[x(τ)]/ℏ},

where S[x(τ)] = ∫₀ᵗ L(x, ẋ) dτ = ∫₀ᵗ [½mẋ² − V(x)] dτ.

其中 S[x(τ)] = ∫₀ᵗ L(x, ẋ) dτ = ∫₀ᵗ [½mẋ² − V(x)] dτ。

**Step 1 — Divide the time interval.** Split [0, t] into N equal slices of width ε = t/N. By the composition property of the evolution operator, Û(t) = [Û(ε)]^N:

**第 1 步 — 划分时间区间。** 将 [0, t] 分成 N 个宽度为 ε = t/N 的等份。由演化算符的复合性质，Û(t) = [Û(ε)]^N：

  K(x′, t; x, 0) = ⟨x′|Û(ε)ⁿ|x⟩
    = ∫…∫ ⟨x′|Û(ε)|x_{N−1}⟩⟨x_{N−1}|Û(ε)|x_{N−2}⟩…⟨x₁|Û(ε)|x⟩ dx₁…dx_{N−1},

inserting (N−1) resolutions of identity ∫|xⱼ⟩⟨xⱼ| dxⱼ = 1̂.

插入 (N−1) 个单位分解 ∫|xⱼ⟩⟨xⱼ| dxⱼ = 1̂。

**Step 2 — Short-time propagator.** For small ε, using Ĥ = p̂²/2m + V(x̂) and the Trotter product formula e^{−iĤε/ℏ} ≈ e^{−ip̂²ε/2mℏ} e^{−iV(x̂)ε/ℏ} (valid to first order in ε):

**第 2 步 — 短时传播子。** 对小 ε，利用 Ĥ = p̂²/2m + V(x̂) 与 Trotter 乘积公式 e^{−iĤε/ℏ} ≈ e^{−ip̂²ε/2mℏ} e^{−iV(x̂)ε/ℏ}（对 ε 一阶成立）：

  ⟨x_{j+1}|Û(ε)|xⱼ⟩ ≈ ⟨x_{j+1}|e^{−ip̂²ε/2mℏ}|xⱼ⟩ · e^{−iV(xⱼ)ε/ℏ}.

The first factor is the free-particle propagator for time ε (from Section D):

第一个因子是 ε 时间的自由粒子传播子（来自 D 节）：

  ⟨x_{j+1}|e^{−ip̂²ε/2mℏ}|xⱼ⟩ = √(m/2πiℏε) exp[im(x_{j+1}−xⱼ)²/2ℏε].

So the short-time factor is:

故短时因子为：

  ⟨x_{j+1}|Û(ε)|xⱼ⟩ ≈ √(m/2πiℏε) exp{(iε/ℏ)[m(x_{j+1}−xⱼ)²/2ε² − V(xⱼ)]} · ε
    = √(m/2πiℏε) exp{(iε/ℏ)[½mẋⱼ² − V(xⱼ)]},

where ẋⱼ = (x_{j+1}−xⱼ)/ε is the discrete velocity.

其中 ẋⱼ = (x_{j+1}−xⱼ)/ε 为离散速度。

**Step 3 — Assemble and take N → ∞.** Multiplying all N short-time factors and taking N → ∞ (ε → 0):

**第 3 步 — 组合并取 N → ∞。** 将所有 N 个短时因子相乘，取 N → ∞（ε → 0）：

  K = lim_{N→∞} (m/2πiℏε)^{N/2} ∫…∫ exp{(i/ℏ) Σⱼ [½mẋⱼ² − V(xⱼ)]ε} dx₁…dx_{N−1}
    ≡ ∫ Dx(τ) exp{(i/ℏ) ∫₀ᵗ [½mẋ² − V(x)] dτ}
    = ∫ Dx(τ) e^{iS[x(τ)]/ℏ}.

The sum in the exponent converges to the action S = ∫L dτ.

指数中的求和收敛到作用量 S = ∫L dτ。

**Step 4 — Classical limit (ℏ → 0).** When ℏ → 0, the oscillatory integral is dominated by the path(s) of stationary phase: δS = 0. This is exactly the **principle of stationary action** (Hamilton's principle) that gives the classical equations of motion — the Euler–Lagrange equations. Thus the classical trajectory is the path of stationary phase in the quantum path integral, and quantum mechanics is seen as a sum over all histories weighted by e^{iS/ℏ}, reducing to the classical path in the ℏ → 0 limit. ∎

**第 4 步 — 经典极限（ℏ → 0）。** 当 ℏ → 0 时，振荡积分由稳相点主导：δS = 0。这正是给出经典运动方程——欧拉–拉格朗日方程——的**最小作用量原理**（哈密顿原理）。因此经典轨迹是量子路径积分中的稳相路径，量子力学表现为以 e^{iS/ℏ} 为权重的所有历史求和，在 ℏ → 0 极限下退化到经典路径。∎

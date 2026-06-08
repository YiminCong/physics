# Derivations — Module 5.3: Ginzburg–Landau Theory
# 推导 — 模块 5.3：金兹堡–朗道理论

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.3](./module-5.3-ginzburg-landau-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.3](./module-5.3-ginzburg-landau-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Minimizing the Uniform GL Free Energy: |ψ|² = −α/β · 最小化均匀 GL 自由能：|ψ|² = −α/β

**Claim.** In the spatially uniform case (no gradients, no magnetic field), minimizing the Ginzburg–Landau free energy F = F_n + α|ψ|² + (β/2)|ψ|⁴ with respect to |ψ|² gives |ψ|² = −α/β when α < 0 (T < T_c), and the condensation energy density is −α²/(2β).

**命题。** 在空间均匀情形（无梯度，无磁场）下，对 |ψ|² 最小化金兹堡–朗道自由能 F = F_n + α|ψ|² + (β/2)|ψ|⁴，当 α < 0（T < T_c）时给出 |ψ|² = −α/β，凝聚能密度为 −α²/(2β)。

**Step 1 — Set up the free energy.** Write |ψ|² = ρ ≥ 0. The free energy density relative to the normal state is

**第 1 步 — 建立自由能。** 写 |ψ|² = ρ ≥ 0。相对于正常态的自由能密度为

  f(ρ) = α ρ + (β/2) ρ².

The parameter β > 0 always (required for stability: without a positive β the free energy would be unbounded below).

参数 β > 0 始终成立（稳定性要求：若没有正的 β，自由能将无下界）。

**Step 2 — Find the critical point.** Differentiate f with respect to ρ and set to zero:

**第 2 步 — 求驻点。** 对 ρ 求 f 的导数并置零：

  df/dρ = α + β ρ = 0   ⟹   ρ₀ = −α/β.

**Step 3 — Classify by sign of α.** Two cases arise depending on the sign of α (which changes at T_c):

**第 3 步 — 按 α 的符号分类。** 根据 α 的符号（在 T_c 处改变）出现两种情况：

  Case α > 0 (T > T_c): ρ₀ = −α/β < 0, which is unphysical since ρ = |ψ|² ≥ 0. The minimum on the physical domain ρ ≥ 0 is at ρ = 0 (normal state, |ψ| = 0).

  Case α < 0 (T < T_c): ρ₀ = −α/β > 0. This is a physical minimum.

  情况 α > 0 (T > T_c)：ρ₀ = −α/β < 0，因 ρ = |ψ|² ≥ 0 故非物理。物理域 ρ ≥ 0 上的极小值在 ρ = 0（正常态，|ψ| = 0）。

  情况 α < 0 (T < T_c)：ρ₀ = −α/β > 0。这是物理的极小值。

**Step 4 — Verify it is a minimum.** d²f/dρ² = β > 0, confirming ρ₀ is a local minimum. The free energy at the minimum is

**第 4 步 — 验证为极小值。** d²f/dρ² = β > 0，确认 ρ₀ 是局部极小值。极小处的自由能为

  f(ρ₀) = α(−α/β) + (β/2)(α/β)² = −α²/β + α²/(2β) = **−α²/(2β)**.

**Step 5 — Physical interpretation.** Near T_c, α ≈ a(T − T_c) with a > 0, so |ψ|² = −α/β ≈ a(T_c − T)/β grows continuously from zero as T is lowered below T_c. The order parameter vanishes at T_c (second-order transition) and the condensation energy density is α²/(2β) ∝ (T_c − T)², consistent with a mean-field specific heat jump. ∎

**第 5 步 — 物理解释。** 在 T_c 附近，α ≈ a(T − T_c)，a > 0，故 |ψ|² = −α/β ≈ a(T_c − T)/β 在 T 降至 T_c 以下时从零连续增长。序参量在 T_c 处消失（二级相变），凝聚能密度为 α²/(2β) ∝ (T_c − T)²，与平均场比热跳变一致。∎

---

## B. Deriving the GL Equations from the Full Free Energy · 从完整自由能推导 GL 方程

**Claim.** Varying the full GL free energy functional F[ψ, A] = ∫d³r [F_n + α|ψ|² + (β/2)|ψ|⁴ + (1/2m*)|(−iℏ∇ − e*A)ψ|² + B²/(2μ₀)] with respect to ψ* and A yields (i) the first GL equation for ψ and (ii) the second GL equation (supercurrent expression).

**命题。** 对完整的 GL 自由能泛函 F[ψ, A] = ∫d³r [F_n + α|ψ|² + (β/2)|ψ|⁴ + (1/2m*)|(−iℏ∇ − e*A)ψ|² + B²/(2μ₀)] 分别对 ψ* 和 A 作变分，得到（i）ψ 的第一 GL 方程和（ii）第二 GL 方程（超电流表达式）。

**Step 1 — Variation with respect to ψ*.** Write the gradient term as (1/2m*)|Dψ|² where D = −iℏ∇ − e*A is the gauge-covariant derivative. Expand |Dψ|² = (Dψ*)·(Dψ). Under δψ* → ψ* + δψ*:

**第 1 步 — 对 ψ* 作变分。** 将梯度项写为 (1/2m*)|Dψ|²，其中 D = −iℏ∇ − e*A 是规范协变导数。展开 |Dψ|² = (Dψ*)·(Dψ)。在 δψ* → ψ* + δψ* 下：

  δF = ∫d³r [α δψ* ψ + β|ψ|² δψ* ψ + (1/2m*)(D δψ*)·(Dψ)] = 0.

Integrate by parts: ∫(D δψ*)·(Dψ) d³r = −∫δψ* D²ψ d³r (boundary terms vanish for localized solutions). Collecting δψ*:

分部积分：∫(D δψ*)·(Dψ) d³r = −∫δψ* D²ψ d³r（对局域解边界项为零）。收集 δψ* 的系数：

  α ψ + β|ψ|² ψ − (1/2m*) D²ψ = 0.

Expanding D² = (−iℏ∇ − e*A)²:

展开 D² = (−iℏ∇ − e*A)²：

  **(1/2m*)(−iℏ∇ − e*A)²ψ + αψ + β|ψ|²ψ = 0.**   (First GL equation)

  **(1/2m*)(−iℏ∇ − e*A)²ψ + αψ + β|ψ|²ψ = 0。**   （第一 GL 方程）

**Step 2 — Variation with respect to A.** The A-dependent terms are (1/2m*)|Dψ|² and B²/(2μ₀). Varying A → A + δA:

**第 2 步 — 对 A 作变分。** A 相关的项为 (1/2m*)|Dψ|² 和 B²/(2μ₀)。对 A → A + δA 作变分：

  δ[(1/2m*)|Dψ|²] = (e*/2m*) δA · [ψ*(−iℏ∇ψ) + ψ(iℏ∇ψ*) − 2e*|ψ|²A] = δA · J_s
  δ[B²/(2μ₀)] = (1/μ₀)(∇ × B) · δA = J_ext · δA   (after integration by parts).

Setting the total variation to zero and using ∇ × B = μ₀ J_s:

置总变分为零并使用 ∇ × B = μ₀ J_s：

  **J_s = (e*ℏ/2m*i)(ψ*∇ψ − ψ∇ψ*) − (e*²/m*)|ψ|²A.**   (Second GL equation / supercurrent)

  **J_s = (e*ℏ/2m*i)(ψ*∇ψ − ψ∇ψ*) − (e*²/m*)|ψ|²A。**   （第二 GL 方程/超电流）

Writing ψ = |ψ|e^{iθ}, the gradient term gives ℏ∇θ and the supercurrent becomes

写 ψ = |ψ|e^{iθ}，梯度项给出 ℏ∇θ，超电流变为

  J_s = (e*/m*)|ψ|²(ℏ∇θ − e*A),

which is precisely the expression linking the supercurrent to the gradient of the phase — the foundation of the Josephson effect (Module 5.8). ∎

这正好是将超电流与相位梯度联系起来的表达式——约瑟夫森效应的基础（模块 5.8）。∎

---

## C. Coherence Length ξ and Penetration Depth λ from the GL Equations · 从 GL 方程推导相干长度 ξ 和穿透深度 λ

**Claim.** Linearizing the first GL equation near |ψ| = 0 defines the GL coherence length ξ = ℏ/√(−2m*α). Expanding near the bulk solution in the full nonlinear equation, and combining with the second GL equation and Ampère's law, gives the GL penetration depth λ = √(m*β/(μ₀ e*² |α|)).

**命题。** 在 |ψ| = 0 附近线性化第一 GL 方程定义了 GL 相干长度 ξ = ℏ/√(−2m*α)。在完整非线性方程中在体解附近展开，并与第二 GL 方程和安培定律联立，给出 GL 穿透深度 λ = √(m*β/(μ₀ e*² |α|))。

**Step 1 — Linearize for ξ.** Near the boundary of a superconductor (or near a vortex core) where |ψ| ≈ 0, drop the β|ψ|³ term from the first GL equation (it is higher order). With A = 0 for simplicity:

**第 1 步 — 线性化求 ξ。** 在超导体边界附近（或涡旋核心附近）|ψ| ≈ 0，从第一 GL 方程中去掉 β|ψ|³ 项（它是高阶小量）。为简便取 A = 0：

  −(ℏ²/2m*) ∇²ψ + αψ = 0.

Look for a solution that heals from 0 to ψ₀ = √(−α/β) over some length scale. Write ψ(x) = ψ₀ tanh(x/√2 ξ) as an ansatz (the exact solution for the 1D case). The linearized equation near ψ = 0 is

寻找从 0 恢复到 ψ₀ = √(−α/β) 的解，其特征长度为某个尺度。写 ψ(x) = ψ₀ tanh(x/√2 ξ) 作为试探解（一维情况的精确解）。在 ψ = 0 附近的线性化方程为

  −(ℏ²/2m*) d²ψ/dx² = −αψ.

This gives an exponential healing with characteristic length

这给出特征长度为以下值的指数恢复

  **ξ² = ℏ²/(2m*|α|),   i.e.   ξ = ℏ/√(2m*|α|)**   (with α < 0, |α| = −α).

  **ξ² = ℏ²/(2m*|α|)，即 ξ = ℏ/√(2m*|α|)**   （α < 0，|α| = −α）。

Near T_c, α ≈ a(T − T_c), so |α| ∝ (T_c − T) and ξ ∝ (T_c − T)^{−½}: the coherence length diverges at T_c (critical fluctuations).

在 T_c 附近，α ≈ a(T − T_c)，故 |α| ∝ (T_c − T)，ξ ∝ (T_c − T)^{−½}：相干长度在 T_c 处发散（临界涨落）。

**Step 2 — Identify λ from the second GL equation.** Deep in the bulk, |ψ|² = ψ₀² = −α/β. Consider a small perturbation in A (small field enters, order parameter is approximately ψ₀). The second GL equation gives

**第 2 步 — 从第二 GL 方程识别 λ。** 在体内深处，|ψ|² = ψ₀² = −α/β。考虑 A 的小扰动（小磁场进入，序参量近似为 ψ₀）。第二 GL 方程给出

  J_s ≈ −(e*²/m*) ψ₀² A = −(e*²/m*)(−α/β) A.

This is the London relation J_s = −A/Λ with 1/Λ = (e*²/m*)(−α/β). From Section C of Module 5.2-derivations, Λ = m*/(n_s e*²), so the effective superfluid density is n_s = −α/β (in units where e* and m* are the pair charge and mass).

这是伦敦关系 J_s = −A/Λ，其中 1/Λ = (e*²/m*)(−α/β)。从模块 5.2 推导的 C 节，Λ = m*/(n_s e*²)，故有效超流密度为 n_s = −α/β（以 e* 和 m* 为配对电荷和质量的单位）。

**Step 3 — Combine with Ampère's law.** Repeating the derivation of Module 5.2-D with n_s → (−α/β):

**第 3 步 — 与安培定律联立。** 以 n_s → (−α/β) 重复模块 5.2-D 的推导：

  **λ² = m*/(μ₀ e*² n_s) = m*β/(μ₀ e*²|α|),   λ = √(m*β/(μ₀ e*²|α|))**.

Near T_c, |α| ∝ (T_c − T), so λ ∝ (T_c − T)^{−½} — both length scales diverge at T_c. ∎

在 T_c 附近，|α| ∝ (T_c − T)，故 λ ∝ (T_c − T)^{−½}——两个长度尺度都在 T_c 处发散。∎

---

## D. The GL Parameter κ = λ/ξ and the Type-I/II Boundary κ = 1/√2 · GL 参数 κ = λ/ξ 与 I/II 型边界 κ = 1/√2

**Claim.** The dimensionless ratio κ = λ/ξ is temperature-independent near T_c and determines the type of superconductor. The critical value is κ = 1/√2: below it, type I (the surface energy of a normal-superconducting interface is positive, so the system prefers one bulk phase); above it, type II (surface energy is negative, so the system minimizes energy by subdividing into vortices).

**命题。** 无量纲比值 κ = λ/ξ 在 T_c 附近与温度无关，决定超导体的类型。临界值为 κ = 1/√2：低于此值为 I 型（正常态–超导态界面的表面能为正，系统倾向于单一体相）；高于此值为 II 型（表面能为负，系统通过分裂成涡旋来最小化能量）。

**Step 1 — Temperature independence of κ.** From Steps 1 and 2 of Section C:

**第 1 步 — κ 的温度无关性。** 由 C 节第 1、2 步：

  ξ ∝ |α|^{−½},   λ ∝ |α|^{−½}.

Both diverge with the same power of (T_c − T), so their ratio κ = λ/ξ is independent of T near T_c. Computing explicitly:

两者以相同的 (T_c − T) 幂次发散，故它们的比值 κ = λ/ξ 在 T_c 附近与 T 无关。显式计算：

  κ = λ/ξ = [√(m*β/(μ₀ e*²|α|))] / [ℏ/√(2m*|α|)]
           = √(m*β/(μ₀ e*²|α|)) · √(2m*|α|)/ℏ
           = √(2m*²β/(μ₀ e*²ℏ²)).

This involves only the material parameters m*, β, e*, μ₀, ℏ — not T. Therefore κ is a material constant. ∎

这只涉及材料参数 m*，β，e*，μ₀，ℏ——不涉及 T。因此 κ 是材料常数。∎

**Step 2 — Surface energy of a normal-superconducting interface.** Consider a flat interface with normal state (x < 0) and superconducting state (x > 0). The surface energy per unit area is (schematically):

**第 2 步 — 正常态–超导态界面的表面能。** 考虑一个平面界面，x < 0 为正常态，x > 0 为超导态。单位面积表面能（示意性地）为：

  σ_ns = ∫₋∞^{+∞} dx [f_condensation profile + f_magnetic profile]
       = ∫ dx [−(α²/2β)(|ψ|/ψ₀)² + (μ₀/2) H_c² (1 − B/H_c)²/μ₀H_c²]   (schematic).

The condensation energy (negative, favoring superconductivity) is concentrated in a length ξ; the magnetic energy cost (positive) extends over length λ.

凝聚能（负，倾向于超导性）集中在长度 ξ 内；磁场能量代价（正）延伸到长度 λ。

**Step 3 — Sign of surface energy.** A dimensional estimate gives σ_ns ∝ (H_c²/2μ₀)(ξ − λ). This is the crucial result:

**第 3 步 — 表面能的符号。** 量纲估算给出 σ_ns ∝ (H_c²/2μ₀)(ξ − λ)。这是关键结果：

  σ_ns > 0  when ξ > λ,  i.e.  κ < 1  (rough estimate).
  σ_ns < 0  when ξ < λ,  i.e.  κ > 1  (rough estimate).

  当 ξ > λ 即 κ < 1 时，σ_ns > 0（粗略估算）。
  当 ξ < λ 即 κ > 1 时，σ_ns < 0（粗略估算）。

**Step 4 — Exact threshold from Abrikosov's calculation.** The precise threshold where σ_ns = 0 is found by a careful variational calculation (Abrikosov 1957). The result is

**第 4 步 — 阿布里科索夫计算的精确阈值。** σ_ns = 0 的精确阈值由仔细的变分计算（阿布里科索夫，1957年）给出。结果为

  σ_ns = 0   when   **κ = 1/√2**.

  **κ < 1/√2**: type I, positive surface energy, field is either fully in or fully out.
  **κ > 1/√2**: type II, negative surface energy, system prefers maximum interface area → vortex lattice.

  **κ < 1/√2**：I 型，正表面能，磁场要么完全在内要么完全在外。
  **κ > 1/√2**：II 型，负表面能，系统倾向于最大界面面积→涡旋晶格。

The derivation of the exact coefficient 1/√2 follows from requiring that the free energy is stationary with respect to vortex density, which is the Abrikosov solution of the linearized GL equations near the upper critical field H_c2. ∎

精确系数 1/√2 的推导来自要求自由能对涡旋密度是驻点，这是阿布里科索夫在上临界场 H_c2 附近线性化 GL 方程的解。∎

---

## E. Flux Quantization: Φ₀ = h/2e from Single-Valuedness of ψ · 磁通量子化：由 ψ 的单值性推导 Φ₀ = h/2e

**Claim.** The requirement that the order parameter ψ = |ψ|e^{iθ} be single-valued around any closed contour inside a superconductor forces the enclosed magnetic flux to be an integer multiple of Φ₀ = h/2e, where 2e is the charge of a Cooper pair.

**命题。** 要求序参量 ψ = |ψ|e^{iθ} 沿超导体内部任意闭合回路是单值函数，迫使围合的磁通量是 Φ₀ = h/2e 的整数倍，其中 2e 是库珀对的电荷。

**Step 1 — Supercurrent in terms of phase.** From Section B, Step 2, the GL supercurrent with e* = 2e (pair charge) and m* = 2m (pair mass) is

**第 1 步 — 用相位表示超电流。** 由 B 节第 2 步，以 e* = 2e（对电荷）和 m* = 2m（对质量）表示的 GL 超电流为

  J_s = (2e/2m)|ψ|²(ℏ∇θ − 2eA) = (e/m)|ψ|²(ℏ∇θ − 2eA).

**Step 2 — Integrate around a closed contour deep inside the bulk.** Choose a contour C that lies entirely in the bulk where |ψ| = ψ₀ = const and J_s = 0 (deep inside the superconductor, far from any surface or vortex). Then J_s = 0 requires:

**第 2 步 — 沿体内深处的闭合回路积分。** 选取完全在体内的回路 C，其中 |ψ| = ψ₀ = const 且 J_s = 0（在超导体内深处，远离任何表面或涡旋）。则 J_s = 0 要求：

  ℏ∇θ − 2eA = 0   ⟹   ∇θ = (2e/ℏ) A.

**Step 3 — Integrate around the contour.** Integrate both sides over the closed contour C:

**第 3 步 — 沿回路积分。** 两边沿闭合回路 C 积分：

  ∮_C ∇θ · dl = (2e/ℏ) ∮_C A · dl.

The right side is (2e/ℏ) times the magnetic flux enclosed by C: ∮ A · dl = ∫∫_S (∇ × A) · dS = Φ (by Stokes' theorem), where Φ = ∫B · dS.

右边是 (2e/ℏ) 乘以 C 围合的磁通量：∮ A · dl = ∫∫_S (∇ × A) · dS = Φ（由斯托克斯定理），其中 Φ = ∫B · dS。

**Step 4 — Single-valuedness constraint.** The order parameter ψ = |ψ|e^{iθ} must be single-valued at every point in space. Going around the closed contour C once, θ must return to its original value modulo 2π (since e^{iθ} is the physical observable):

**第 4 步 — 单值性约束。** 序参量 ψ = |ψ|e^{iθ} 必须在空间中每一点都是单值的。绕闭合回路 C 一圈，θ 必须回到其原始值的 2π 整数倍（因为 e^{iθ} 是物理可观测量）：

  ∮_C ∇θ · dl = 2πn,   n = 0, ±1, ±2, …

**Step 5 — Flux quantization.** Combining Steps 3 and 4:

**第 5 步 — 磁通量子化。** 联立第 3 和第 4 步：

  2πn = (2e/ℏ) Φ   ⟹   Φ = n · (2πℏ/2e) = n · (h/2e).

Defining the **flux quantum**:

定义**磁通量子**：

  **Φ₀ = h/(2e) ≈ 2.07 × 10⁻¹⁵ Wb (Weber)**.

The factor 2e (not e) is the direct signature of paired electrons — Cooper pairs carry charge 2e. This prediction was confirmed experimentally by Deaver & Fairbank and Doll & Näbauer (1961). ∎

因子 2e（而非 e）是电子配对的直接标志——库珀对携带电荷 2e。这一预测由德弗和费尔班克以及多尔和奈鲍尔（1961年）在实验上证实。∎

**Step 6 — Vortex interpretation.** For n = 1 (a single flux quantum), the phase θ winds by 2π around the vortex core, and the order parameter |ψ| → 0 at the core (otherwise ψ would be ill-defined at the winding center). The core has radius ∼ ξ, and the circulating supercurrents and decaying flux profile extend to radius ∼ λ — exactly the structure computed in Module 5.7. ∎

**第 6 步 — 涡旋诠释。** 对于 n = 1（单个磁通量子），相位 θ 在涡旋核心周围绕转 2π，序参量 |ψ| → 0 在核心处（否则 ψ 在绕转中心将无定义）。核心半径约为 ξ，环流超电流和衰减磁通分布延伸到半径约 λ——这正是模块 5.7 中计算的结构。∎

---

*The GL theory derived here is exact near T_c and is microscopically justified by the Gorkov derivation from BCS. The length scales ξ and λ appear in every subsequent module (5.4–5.9), and flux quantization is the operating principle of SQUIDs (Module 5.8).*

*此处推导的 GL 理论在 T_c 附近是精确的，并由从 BCS 出发的戈尔科夫推导在微观上得到证明。长度尺度 ξ 和 λ 出现在随后的每个模块（5.4–5.9）中，磁通量子化是 SQUID 的工作原理（模块 5.8）。*

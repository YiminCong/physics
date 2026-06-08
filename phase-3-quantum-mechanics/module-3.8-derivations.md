# Derivations — Module 3.8: Time-Dependent Perturbation Theory & Scattering
# 推导 — 模块 3.8：含时微扰理论与散射

> Companion to [Module 3.8](./module-3.8-time-dependent-perturbation-theory-and-scattering.md). Full step-by-step proofs of the first-order transition amplitude, Fermi's golden rule, the Born approximation, and the differential cross section. English first, then 中文.
> [模块 3.8](./module-3.8-time-dependent-perturbation-theory-and-scattering.md) 的配套文档：一阶跃迁振幅、费米黄金定则、玻恩近似与微分散射截面的完整逐步证明。先英文，后中文。

---

## A. First-Order Transition Amplitude · 一阶跃迁振幅

**Claim.** Given a system initially in eigenstate |i⟩ of the unperturbed Hamiltonian Ĥ₀, subjected to a perturbation Ĥ′(t) switched on at t = 0, the first-order probability amplitude to find the system in a different eigenstate |f⟩ at time t is:

**命题。** 设系统初始处于无微扰哈密顿量 Ĥ₀ 的本征态 |i⟩，在 t = 0 时刻开始施加微扰 Ĥ′(t)，则在 t 时刻发现系统处于另一本征态 |f⟩ 的一阶概率振幅为：

  c_f^{(1)}(t) = (1/iℏ) ∫₀ᵗ ⟨f|Ĥ′(t′)|i⟩ e^{iω_{fi}t′} dt′,

where ω_{fi} = (E_f − E_i)/ℏ is the Bohr frequency.

其中 ω_{fi} = (E_f − E_i)/ℏ 为玻尔频率。

**Step 1 — Interaction picture.** Split the full Hamiltonian as Ĥ(t) = Ĥ₀ + Ĥ′(t). In the interaction picture, the state is

**第 1 步 — 相互作用绘景。** 将全哈密顿量分解为 Ĥ(t) = Ĥ₀ + Ĥ′(t)。在相互作用绘景中，态定义为

  |ψ_I(t)⟩ = e^{iĤ₀t/ℏ} |ψ_S(t)⟩,

which removes the "free" time evolution e^{−iĤ₀t/ℏ}. The Schrödinger equation for |ψ_S⟩ transforms to

它去除了"自由"演化因子 e^{−iĤ₀t/ℏ}。|ψ_S⟩ 的薛定谔方程变换为

  iℏ d/dt |ψ_I(t)⟩ = Ĥ_I′(t) |ψ_I(t)⟩,

where Ĥ_I′(t) = e^{iĤ₀t/ℏ} Ĥ′(t) e^{−iĤ₀t/ℏ} is the perturbation in the interaction picture.

其中 Ĥ_I′(t) = e^{iĤ₀t/ℏ} Ĥ′(t) e^{−iĤ₀t/ℏ} 为相互作用绘景中的微扰。

**Step 2 — Expand in the unperturbed basis.** Write |ψ_I(t)⟩ = Σₙ cₙ(t)|n⟩, where {|n⟩} are the orthonormal eigenstates of Ĥ₀ with Ĥ₀|n⟩ = Eₙ|n⟩. The initial condition is cₙ(0) = δₙᵢ (system starts in |i⟩). Substituting into the equation of motion:

**第 2 步 — 在无微扰基中展开。** 写 |ψ_I(t)⟩ = Σₙ cₙ(t)|n⟩，其中 {|n⟩} 为 Ĥ₀ 的正交归一本征态，Ĥ₀|n⟩ = Eₙ|n⟩。初始条件为 cₙ(0) = δₙᵢ（系统从 |i⟩ 出发）。代入运动方程：

  iℏ Σₙ ċₙ(t)|n⟩ = Ĥ_I′(t) Σₙ cₙ(t)|n⟩.

Project onto ⟨f|:

投影到 ⟨f|：

  iℏ ċ_f(t) = Σₙ ⟨f|Ĥ_I′(t)|n⟩ cₙ(t).

**Step 3 — Evaluate the matrix element.** Since Ĥ_I′(t) = e^{iĤ₀t/ℏ} Ĥ′(t) e^{−iĤ₀t/ℏ}, sandwiching between eigenstates gives

**第 3 步 — 计算矩阵元。** 由于 Ĥ_I′(t) = e^{iĤ₀t/ℏ} Ĥ′(t) e^{−iĤ₀t/ℏ}，夹在本征态之间得

  ⟨f|Ĥ_I′(t)|n⟩ = e^{iE_f t/ℏ} ⟨f|Ĥ′(t)|n⟩ e^{−iEₙt/ℏ} = ⟨f|Ĥ′(t)|n⟩ e^{i(E_f − Eₙ)t/ℏ}.

**Step 4 — First-order perturbation theory.** To zeroth order cₙ(t) ≈ δₙᵢ (no transition). Substituting this into the right-hand side gives the first-order equation:

**第 4 步 — 一阶微扰理论。** 零阶近似为 cₙ(t) ≈ δₙᵢ（无跃迁）。将此代入右端得一阶方程：

  iℏ ċ_f^{(1)}(t) = ⟨f|Ĥ′(t)|i⟩ e^{iω_{fi}t},

where ω_{fi} = (E_f − Eᵢ)/ℏ. Integrating from 0 to t with c_f^{(1)}(0) = 0 (f ≠ i):

其中 ω_{fi} = (E_f − Eᵢ)/ℏ。从 0 积分到 t，初始条件 c_f^{(1)}(0) = 0（f ≠ i）：

  c_f^{(1)}(t) = (1/iℏ) ∫₀ᵗ ⟨f|Ĥ′(t′)|i⟩ e^{iω_{fi}t′} dt′.   ∎

The transition probability is P_{i→f}(t) = |c_f^{(1)}(t)|².

跃迁概率为 P_{i→f}(t) = |c_f^{(1)}(t)|²。∎

---

## B. Fermi's Golden Rule · 费米黄金定则

**Claim.** For a constant (or slowly varying) perturbation Ĥ′ turned on at t = 0, the transition rate into a continuum of final states with density of states ρ(E_f) is:

**命题。** 对于在 t = 0 时接通的常数（或缓变）微扰 Ĥ′，跃迁到末态密度为 ρ(E_f) 的连续谱的速率为：

  Γ_{i→f} = (2π/ℏ) |⟨f|Ĥ′|i⟩|² ρ(E_f).

**Step 1 — Evaluate the integral for a constant perturbation.** Take Ĥ′(t) = Ĥ′ (time-independent). Then:

**第 1 步 — 对常数微扰计算积分。** 取 Ĥ′(t) = Ĥ′（与时间无关）。则：

  c_f^{(1)}(t) = (1/iℏ) ⟨f|Ĥ′|i⟩ ∫₀ᵗ e^{iω_{fi}t′} dt′
               = (1/iℏ) ⟨f|Ĥ′|i⟩ · [e^{iω_{fi}t} − 1] / (iω_{fi})
               = (⟨f|Ĥ′|i⟩/ℏ) · e^{iω_{fi}t/2} · [2 sin(ω_{fi}t/2) / ω_{fi}].

**Step 2 — Transition probability.** Taking the modulus squared:

**第 2 步 — 跃迁概率。** 取模平方：

  P_{i→f}(t) = |c_f^{(1)}(t)|²
             = (|⟨f|Ĥ′|i⟩|²/ℏ²) · 4 sin²(ω_{fi}t/2) / ω_{fi}²
             = (|⟨f|Ĥ′|i⟩|²/ℏ²) · t² · sinc²(ω_{fi}t/2),

where sinc(x) = sin(x)/x. Equivalently, using ω_{fi} = (E_f − Eᵢ)/ℏ:

其中 sinc(x) = sin(x)/x。等价地，利用 ω_{fi} = (E_f − Eᵢ)/ℏ：

  P_{i→f}(t) = (|⟨f|Ĥ′|i⟩|²/ℏ²) · [4 sin²((E_f − Eᵢ)t/2ℏ)] / (E_f − Eᵢ)²/ℏ²
             = (4|⟨f|Ĥ′|i⟩|²/ℏ²) · sin²((E_f − Eᵢ)t/2ℏ) / ((E_f − Eᵢ)/ℏ)².

**Step 3 — The sinc² → delta function limit.** The key identity is: for large t,

**第 3 步 — sinc² 趋向 δ 函数的极限。** 关键恒等式为：当 t → ∞ 时，

  (t/2π) · [4 sin²(ω t/2) / (ω t)²] = (t/π) · sin²(ωt/2) / (ωt/2)²  → δ(ω)   as t → ∞.

More precisely, (1/π) · sin²(xt)/x² → tδ(x) in the distributional sense as t → ∞ (it integrates to t and peaks sharply at x = 0 with width ∼ 1/t). Converting from ω to energy using δ(ω_{fi}) = ℏ δ(E_f − Eᵢ):

更精确地，(1/π) · sin²(xt)/x² 在分布意义下当 t → ∞ 时趋向 tδ(x)（其积分为 t，在 x = 0 处急剧峰化，宽度 ∼ 1/t）。利用 δ(ω_{fi}) = ℏ δ(E_f − Eᵢ) 将 ω 转化为能量：

  (4/ℏ²) sin²((E_f−Eᵢ)t/2ℏ) / (E_f−Eᵢ)²/ℏ²  →  (2πt/ℏ) δ(E_f − Eᵢ).

To see this explicitly: let x = (E_f − Eᵢ)/(2ℏ), so the factor is sin²(xt)/x², and

为明确起见：令 x = (E_f − Eᵢ)/(2ℏ)，则因子为 sin²(xt)/x²，且

  ∫_{-∞}^{∞} [sin²(xt)/x²] d(E_f/ℏ) = 2t ∫_{-∞}^{∞} [sin²(u)/u²] du/2 = 2t · (π/2) · (1/?) ...

Let us carry this out directly. We have

让我们直接进行。有

  ∫_{-∞}^{∞} 4sin²(ω_{fi}t/2)/ω_{fi}² · dω_{fi} = t · ∫_{-∞}^{∞} [sin(u)/u]² · 2 du = t · 2 · (π) · (1/2)... 

We use the standard result ∫_{-∞}^{∞} sin²(u)/u² du = π. Therefore

我们使用标准结果 ∫_{-∞}^{∞} sin²(u)/u² du = π。因此

  ∫_{-∞}^{∞} [4sin²(ω_{fi}t/2) / ω_{fi}²] dω_{fi}
     = t ∫_{-∞}^{∞} sin²(v)/(v²) · 2 dv   [substituting v = ω_{fi}t/2]
     = t · 2 · π/2 · 2 ... 

Let v = ω_{fi} t/2, so dω_{fi} = 2dv/t:

令 v = ω_{fi} t/2，则 dω_{fi} = 2dv/t：

  ∫_{-∞}^{∞} [4sin²(ω_{fi}t/2)/ω_{fi}²] dω_{fi}
     = ∫_{-∞}^{∞} [4sin²(v)/(2v/t)²] · (2dv/t)
     = ∫_{-∞}^{∞} [4sin²(v) · t²/(4v²)] · (2/t) dv
     = 2t ∫_{-∞}^{∞} [sin²(v)/v²] dv = 2t · π = 2πt.

Hence as a function of ω_{fi} the factor 4sin²(ω_{fi}t/2)/ω_{fi}² → 2πt · δ(ω_{fi}) as t → ∞, confirming

因此作为 ω_{fi} 的函数，当 t → ∞ 时 4sin²(ω_{fi}t/2)/ω_{fi}² → 2πt · δ(ω_{fi})，从而确认

  P_{i→f}(t) → (|⟨f|Ĥ′|i⟩|²/ℏ²) · 2πt · δ(ω_{fi}) = (2πt/ℏ) |⟨f|Ĥ′|i⟩|² · δ(E_f − Eᵢ).

**Step 4 — Integrate over the density of final states.** The total transition rate Γ = dP/dt sums over all accessible final states. For a continuous spectrum with density of states ρ(E_f) (number of states per unit energy near E_f), integrate:

**第 4 步 — 对末态密度积分。** 总跃迁速率 Γ = dP/dt 对所有可及末态求和。对于末态密度为 ρ(E_f) 的连续谱（每单位能量附近的态数），积分：

  Γ = dP_total/dt = (d/dt) ∫ P_{i→f}(t) ρ(E_f) dE_f
    = ∫ (2π/ℏ) |⟨f|Ĥ′|i⟩|² δ(E_f − Eᵢ) ρ(E_f) dE_f.

The delta function enforces energy conservation E_f = Eᵢ, so:

δ 函数强制能量守恒 E_f = Eᵢ，故：

  **Γ = (2π/ℏ) |⟨f|Ĥ′|i⟩|² ρ(Eᵢ).**

Here ρ(Eᵢ) is the density of final states evaluated at the initial energy — Fermi's golden rule. ∎

此处 ρ(Eᵢ) 为在初态能量处计算的末态密度——即费米黄金定则。∎

**Domain conditions.** The derivation requires: (i) the perturbation matrix element is approximately constant over the energy width ∼ ℏ/t that contributes, (ii) t is large enough that the sinc² peak is sharp compared to variations in |⟨f|Ĥ′|i⟩|² and ρ, but (iii) t is short enough that first-order perturbation theory remains valid: |c_f^{(1)}|² ≪ 1.

**定义域条件。** 推导需要：（i）在宽度约 ℏ/t 的能量范围内微扰矩阵元近似为常数；（ii）t 足够大使得 sinc² 峰相比 |⟨f|Ĥ′|i⟩|² 和 ρ 的变化是尖锐的；但（iii）t 足够小使得一阶微扰理论仍然有效：|c_f^{(1)}|² ≪ 1。

---

## C. The Born Approximation for Scattering · 散射的玻恩近似

**Claim.** For a particle of mass m scattered by a potential V(r) at wavevector k (incident plane wave e^{ik·r}), the first Born approximation gives the scattering amplitude:

**命题。** 质量为 m 的粒子以波矢 k 被势 V(r) 散射（入射平面波 e^{ik·r}），一阶玻恩近似给出散射振幅：

  f(θ) = −(m/2πℏ²) ∫ V(r) e^{iq·r} d³r = −(m/2πℏ²) Ṽ(q),

where q = k − k′ is the momentum transfer (with |k| = |k′| = k for elastic scattering) and Ṽ(q) is the Fourier transform of V.

其中 q = k − k′ 为动量转移（对弹性散射 |k| = |k′| = k），Ṽ(q) 为 V 的傅里叶变换。

**Step 1 — The Lippmann–Schwinger equation.** The full stationary scattering state satisfies

**第 1 步 — Lippmann–Schwinger 方程。** 完整的定态散射态满足

  (Ĥ₀ + V)|ψ⟩ = E|ψ⟩,   i.e.   (E − Ĥ₀)|ψ⟩ = V|ψ⟩.

The formal solution incorporating the incident plane wave |k⟩ (eigenstate of Ĥ₀ with eigenvalue E = ℏ²k²/2m) and an outgoing-wave boundary condition (Green's function with +iε prescription) is:

正式解（包含入射平面波 |k⟩，即 Ĥ₀ 的本征态，本征值 E = ℏ²k²/2m，以及出射波边界条件，+iε 格林函数）为：

  |ψ⁺⟩ = |k⟩ + (E − Ĥ₀ + iε)⁻¹ V |ψ⁺⟩.

In position space, the Green's function G₀⁺(r,r′) = ⟨r|(E − Ĥ₀ + iε)⁻¹|r′⟩ for the free particle equals

在坐标空间，自由粒子的格林函数 G₀⁺(r,r′) = ⟨r|(E − Ĥ₀ + iε)⁻¹|r′⟩ 等于

  G₀⁺(r,r′) = −(2m/ℏ²) · e^{ik|r−r′|} / (4π|r−r′|).

This is verified by acting (∇² + k²) on it: (∇² + k²)G₀⁺(r,r′) = −(2m/ℏ²)δ³(r − r′) (the defining equation for the Green's function of −ℏ²∇²/2m − E).

通过作用 (∇² + k²) 于其上可验证：(∇² + k²)G₀⁺(r,r′) = −(2m/ℏ²)δ³(r − r′)（即 −ℏ²∇²/2m − E 的格林函数的定义方程）。

**Step 2 — Position-space integral equation.** In coordinate representation:

**第 2 步 — 坐标空间积分方程。** 在坐标表象中：

  ψ(r) = e^{ik·r} − (m/2πℏ²) ∫ [e^{ik|r−r′|} / |r−r′|] V(r′) ψ(r′) d³r′.

**Step 3 — Far-field (large r) limit.** For r ≫ r′ (detector far from scattering center), expand:

**第 3 步 — 远场（大 r）极限。** 当 r ≫ r′（探测器远离散射中心），展开：

  |r − r′| = r√(1 − 2r·r′/r² + r′²/r²) ≈ r − r̂·r′ + O(r′²/r).

Hence e^{ik|r−r′|}/|r−r′| ≈ (e^{ikr}/r) e^{−ik′·r′}, where k′ = kr̂ is the scattered wavevector (pointing toward the detector). Substituting:

因此 e^{ik|r−r′|}/|r−r′| ≈ (e^{ikr}/r) e^{−ik′·r′}，其中 k′ = kr̂ 为指向探测器的散射波矢。代入：

  ψ(r) ≈ e^{ik·r} + f(θ) e^{ikr}/r,

where the scattering amplitude is

其中散射振幅为

  f(θ) = −(m/2πℏ²) ∫ e^{−ik′·r′} V(r′) ψ(r′) d³r′.

**Step 4 — First Born approximation.** In the Born approximation, ψ(r′) ≈ e^{ik·r′} (replace the full scattering state by the incident plane wave — valid when V is weak). Then:

**第 4 步 — 一阶玻恩近似。** 在玻恩近似中，用入射平面波替代完整散射态 ψ(r′) ≈ e^{ik·r′}（当 V 较弱时有效）。则：

  f(θ) = −(m/2πℏ²) ∫ e^{−ik′·r′} V(r′) e^{ik·r′} d³r′
        = −(m/2πℏ²) ∫ V(r′) e^{i(k−k′)·r′} d³r′
        = −(m/2πℏ²) ∫ V(r) e^{iq·r} d³r
        = −(m/2πℏ²) Ṽ(q),

where **q = k − k′** is the momentum transfer. For elastic scattering with |k| = |k′| = k, the magnitude is |q| = 2k sin(θ/2), where θ is the scattering angle. ∎

其中 **q = k − k′** 为动量转移。对弹性散射 |k| = |k′| = k，其大小为 |q| = 2k sin(θ/2)，θ 为散射角。∎

**Validity condition.** The Born approximation requires |V| ≪ ℏ²k²/2m = E (the potential energy is small compared to the kinetic energy) — more precisely, |(m/2πℏ²)∫ e^{i q·r} V(r)/|r| d³r| ≪ 1.

**有效条件。** 玻恩近似要求 |V| ≪ ℏ²k²/2m = E（势能远小于动能）——更精确地，|(m/2πℏ²)∫ e^{iq·r} V(r)/|r| d³r| ≪ 1。

---

## D. Differential Cross Section · 微分散射截面

**Claim.** The differential cross section is related to the scattering amplitude by:

**命题。** 微分散射截面与散射振幅的关系为：

  dσ/dΩ = |f(θ)|².

**Step 1 — Definition of cross section.** The differential cross section dσ/dΩ is defined such that the number of particles scattered per unit time into solid angle dΩ around direction (θ,φ) equals

**第 1 步 — 截面的定义。** 微分散射截面 dσ/dΩ 定义为：单位时间内散射到方向 (θ,φ) 的立体角 dΩ 中的粒子数等于

  dN = J_inc · (dσ/dΩ) dΩ,

where J_inc is the incident probability current (particles per unit area per unit time). For an incident plane wave ψ_inc = e^{ikz}, J_inc = ℏk/m.

其中 J_inc 为入射概率流（单位面积单位时间的粒子数）。对入射平面波 ψ_inc = e^{ikz}，J_inc = ℏk/m。

**Step 2 — Scattered probability current.** At large r the scattered wave is ψ_sc = f(θ) e^{ikr}/r. The radial component of its probability current is:

**第 2 步 — 散射概率流。** 在大 r 处散射波为 ψ_sc = f(θ) e^{ikr}/r。其概率流的径向分量为：

  J_sc = (ℏ/m) Im(ψ_sc* ∂ψ_sc/∂r)
       = (ℏ/m) Im((f*(θ)/r) e^{−ikr} · ik f(θ)/r e^{ikr})
       = (ℏk/m) |f(θ)|²/r².

**Step 3 — Count scattered particles.** The flux through the area element r² dΩ at distance r (which captures all particles scattered into dΩ) is:

**第 3 步 — 统计散射粒子。** 通过距离 r 处面积元 r² dΩ 的流量（捕获所有散射到 dΩ 中的粒子）为：

  dN/dt = J_sc · r² dΩ = (ℏk/m) |f(θ)|² dΩ.

**Step 4 — Divide by incident flux.**

**第 4 步 — 除以入射流量。**

  dσ/dΩ = (dN/dt) / (J_inc dΩ) = [(ℏk/m)|f(θ)|² dΩ] / [(ℏk/m) dΩ] = **|f(θ)|²**.   ∎

This result is exact (not a Born approximation): whatever f(θ) is (whether computed from Born, partial waves, or otherwise), dσ/dΩ = |f(θ)|².

此结果是精确的（不是玻恩近似）：无论 f(θ) 如何计算（玻恩、分波或其他方法），dσ/dΩ = |f(θ)|² 均成立。∎

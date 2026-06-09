# Derivations — Module 1.22: Retarded Potentials, Multipole Radiation & Radiation Reaction
# 推导 — 模块 1.22：推迟势、多极辐射与辐射阻尼

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.22](./module-1.22-retarded-potentials-radiation-reaction.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.22](./module-1.22-retarded-potentials-radiation-reaction.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Retarded Potentials from the Wave Equation · 从波动方程推导推迟势

**Claim.** In the Lorenz gauge ∂_μ A^μ = 0, the potentials satisfy □φ = −ρ/ε₀ and □A = −μ₀J (with □ = ∇² − (1/c²)∂²/∂t²). The causal solutions are the retarded potentials φ(r,t) = (1/4πε₀)∫ ρ(r',t_r)/|r−r'| d³r' and A(r,t) = (μ₀/4π)∫ J(r',t_r)/|r−r'| d³r', with t_r = t − |r−r'|/c.

**命题。** 在洛伦兹规范 ∂_μ A^μ = 0 下，势满足 □φ = −ρ/ε₀ 与 □A = −μ₀J（□ = ∇² − (1/c²)∂²/∂t²）。因果解为推迟势 φ(r,t) = (1/4πε₀)∫ ρ(r',t_r)/|r−r'| d³r' 与 A(r,t) = (μ₀/4π)∫ J(r',t_r)/|r−r'| d³r'，其中 t_r = t − |r−r'|/c。

**Step 1 — Reduce Maxwell's equations to wave equations.** Write the fields via potentials E = −∇φ − ∂A/∂t, B = ∇×A (Module 1.10). Gauss's law ∇·E = ρ/ε₀ becomes −∇²φ − ∂(∇·A)/∂t = ρ/ε₀, and Ampère–Maxwell ∇×B = μ₀J + (1/c²)∂E/∂t becomes ∇(∇·A) − ∇²A = μ₀J − (1/c²)∇(∂φ/∂t) − (1/c²)∂²A/∂t².

**第 1 步 — 将麦克斯韦方程化为波动方程。** 用势写出场 E = −∇φ − ∂A/∂t，B = ∇×A（模块 1.10）。高斯定律 ∇·E = ρ/ε₀ 化为 −∇²φ − ∂(∇·A)/∂t = ρ/ε₀，安培–麦克斯韦方程 ∇×B = μ₀J + (1/c²)∂E/∂t 化为 ∇(∇·A) − ∇²A = μ₀J − (1/c²)∇(∂φ/∂t) − (1/c²)∂²A/∂t²。

**Step 2 — Impose the Lorenz gauge.** Choosing ∇·A + (1/c²)∂φ/∂t = 0 (i.e. ∂_μ A^μ = 0) eliminates the cross terms. The two equations decouple into

**第 2 步 — 施加洛伦兹规范。** 选取 ∇·A + (1/c²)∂φ/∂t = 0（即 ∂_μ A^μ = 0）消去交叉项。两个方程解耦为

  ∇²φ − (1/c²)∂²φ/∂t² = −ρ/ε₀,   ∇²A − (1/c²)∂²A/∂t² = −μ₀J,

i.e. □φ = −ρ/ε₀ and □A = −μ₀J — four identical scalar wave equations with sources.

即 □φ = −ρ/ε₀ 与 □A = −μ₀J——四个形式相同的带源标量波动方程。

**Step 3 — Green's function of the d'Alembertian.** The retarded Green's function solves □G(r,t; r',t') = −δ³(r−r')δ(t−t') with purely outgoing (causal) boundary conditions. The standard result is

**第 3 步 — 达朗贝尔算子的格林函数。** 推迟格林函数满足 □G(r,t; r',t') = −δ³(r−r')δ(t−t')，具纯外向（因果）边界条件。标准结果为

  G(r,t; r',t') = δ(t' − [t − |r−r'|/c]) / (4π|r−r'|) = δ(t_r − t') / (4π|r−r'|),

where t_r = t − |r−r'|/c is the retarded time: the delta function fires only when t' equals the moment a signal leaving r' at speed c arrives at r at time t.

其中 t_r = t − |r−r'|/c 为推迟时刻：仅当 t' 等于从 r' 以速度 c 出发的信号在 t 时刻到达 r 的那一时刻时，δ 函数才作用。

**Step 4 — Convolve source with Green's function.** Since □φ = −ρ/ε₀, the particular solution is φ = (1/ε₀)∫ G ρ d³r' dt'. Insert G and integrate over t' using the delta function:

**第 4 步 — 源与格林函数的卷积。** 由 □φ = −ρ/ε₀，特解为 φ = (1/ε₀)∫ G ρ d³r' dt'。代入 G 并用 δ 函数对 t' 积分：

  φ(r,t) = (1/ε₀)∫ d³r' ∫ dt' [δ(t_r − t')/(4π|r−r'|)] ρ(r',t')
         = (1/4πε₀)∫ ρ(r', t_r)/|r−r'| d³r'.

The same convolution with □A = −μ₀J gives

对 □A = −μ₀J 作相同卷积给出

  A(r,t) = (μ₀/4π)∫ J(r', t_r)/|r−r'| d³r'.

**Step 5 — Causality fixes the retarded (not advanced) choice.** The wave operator also admits an advanced Green's function with t_a = t + |r−r'|/c, giving fields determined by the *future* of the source. Physical causality — effects follow causes — selects the retarded solution: the field at (r,t) depends only on the source at the earlier time t_r. ∎

**第 5 步 — 因果性选定推迟解（而非超前解）。** 波动算子也容许带 t_a = t + |r−r'|/c 的超前格林函数，给出由源的*未来*决定的场。物理因果性——果随因——选择推迟解：(r,t) 处的场只依赖于较早时刻 t_r 的源。∎

---

## B. The Liénard–Wiechert Potentials and the κ = 1 − n·β Factor · 李纳–维谢尔势与 κ = 1 − n·β 因子

**Claim.** For a point charge q moving on trajectory w(t), the retarded potentials evaluate to φ = (1/4πε₀) q/[κR]_ret and A = (μ₀/4π) qcβ/[κR]_ret = (β/c)φ, where R = |r − w(t_r)|, n = (r − w(t_r))/R, β = v(t_r)/c, and κ = 1 − n·β.

**命题。** 对沿轨迹 w(t) 运动的点电荷 q，推迟势计算为 φ = (1/4πε₀) q/[κR]_ret 与 A = (μ₀/4π) qcβ/[κR]_ret = (β/c)φ，其中 R = |r − w(t_r)|，n = (r − w(t_r))/R，β = v(t_r)/c，κ = 1 − n·β。

**Step 1 — Point-charge sources.** A point charge has ρ(r',t') = q δ³(r' − w(t')) and J(r',t') = q v(t') δ³(r' − w(t')), with v = ẇ. Substitute into the retarded potential, keeping the explicit time-delta form (before the t' integration is collapsed):

**第 1 步 — 点电荷源。** 点电荷有 ρ(r',t') = q δ³(r' − w(t')) 与 J(r',t') = q v(t') δ³(r' − w(t'))，v = ẇ。代入推迟势，保留显式时间 δ 形式（在折叠 t' 积分之前）：

  φ(r,t) = (1/4πε₀)∫ d³r' ∫ dt' [δ(t' − t + |r−r'|/c)/|r−r'|] q δ³(r' − w(t')).

**Step 2 — Do the space integral.** The δ³ sets r' = w(t'), so |r−r'| → |r − w(t')| ≡ R(t'):

**第 2 步 — 完成空间积分。** δ³ 令 r' = w(t')，故 |r−r'| → |r − w(t')| ≡ R(t')：

  φ(r,t) = (q/4πε₀)∫ dt' δ(t' − t + R(t')/c) / R(t').

**Step 3 — Do the time integral with the Jacobian.** The remaining δ is a function of t' through its argument g(t') = t' − t + R(t')/c. Using δ(g(t')) = δ(t' − t_r)/|g'(t_r)|, where t_r is the root g(t_r) = 0 (the retarded time), we need g'(t'):

**第 3 步 — 用雅可比因子完成时间积分。** 剩余 δ 通过其宗量 g(t') = t' − t + R(t')/c 依赖 t'。利用 δ(g(t')) = δ(t' − t_r)/|g'(t_r)|，其中 t_r 为根 g(t_r) = 0（推迟时刻），需要 g'(t')：

  g'(t') = 1 + (1/c) dR/dt'.

Now R = |r − w(t')|, so dR/dt' = −(r − w)·ẇ / |r − w| = −n·v, where n = (r − w)/R. Hence

现 R = |r − w(t')|，故 dR/dt' = −(r − w)·ẇ / |r − w| = −n·v，n = (r − w)/R。于是

  g'(t') = 1 − n·v/c = 1 − n·β ≡ κ.

**Step 4 — Assemble the scalar potential.** The time integral picks up the factor 1/|g'(t_r)| = 1/κ, evaluated at the retarded time:

**第 4 步 — 组装标量势。** 时间积分给出因子 1/|g'(t_r)| = 1/κ，在推迟时刻取值：

  φ(r,t) = (q/4πε₀) · 1/[R κ]_ret = **(1/4πε₀) q/[κR]_ret**,

with [⋯]_ret meaning all quantities evaluated at t_r. The κ = 1 − n·β factor is purely kinematic: it is the Jacobian of the map t' ↦ g(t'), encoding the **searchlight/Doppler compression** — while the charge moves a distance v dt' toward the observer, the retarded "now" surface sweeps less retarded volume, so a charge approaching the field point (n·β → 1) packs its retarded contribution into a thin shell and the potential is enhanced by 1/κ.

其中 [⋯]_ret 表示所有量在 t_r 取值。κ = 1 − n·β 因子纯粹是运动学的：它是映射 t' ↦ g(t') 的雅可比因子，编码了**探照灯/多普勒压缩**——当电荷朝观察者移动 v dt' 时，推迟"现在"面扫过的推迟体积更少，故趋近场点的电荷（n·β → 1）将其推迟贡献压入薄壳，势增强 1/κ 倍。

**Step 5 — Vector potential.** The current differs from the charge density only by the factor v(t') = c β(t'), which the space integral evaluates at r' = w(t'). The identical time integral then gives

**第 5 步 — 矢量势。** 电流与电荷密度仅相差因子 v(t') = c β(t')，空间积分在 r' = w(t') 处取值。相同的时间积分给出

  A(r,t) = (μ₀/4π) q v/[κR]_ret = **(μ₀/4π) qcβ/[κR]_ret = (β/c)φ**,

using μ₀ c = 1/(ε₀ c) so that (μ₀/4π) qc = (1/4πε₀)(q/c). Thus A and φ carry the same κR denominator and A = (v/c²)φ = (β/c)φ. ∎

利用 μ₀ c = 1/(ε₀ c)，得 (μ₀/4π) qc = (1/4πε₀)(q/c)。故 A 与 φ 含相同的 κR 分母，且 A = (v/c²)φ = (β/c)φ。∎

---

## C. Fields of a Point Charge: Velocity and Radiation (Acceleration) Fields · 点电荷的场：速度场与辐射（加速度）场

**Claim.** Differentiating the Liénard–Wiechert potentials gives E = E_vel + E_acc, where the velocity field E_vel ∝ (n − β)/(κ³R²) falls off as 1/R², and the **radiation field** E_acc = (q/4πε₀c²) [n × ((n − β) × a)]/(κ³R) falls off as 1/R, with B = (n × E)/c. Only E_acc carries energy to infinity.

**命题。** 对李纳–维谢尔势求导给出 E = E_vel + E_acc，其中速度场 E_vel ∝ (n − β)/(κ³R²) 按 1/R² 衰减，**辐射场** E_acc = (q/4πε₀c²) [n × ((n − β) × a)]/(κ³R) 按 1/R 衰减，B = (n × E)/c。只有 E_acc 将能量带到无穷远。

**Step 1 — Fields from potentials.** The fields are E = −∇φ − ∂A/∂t and B = ∇×A. The subtlety is that φ and A depend on r and t both explicitly and *through* the retarded time t_r(r,t), since R appears inside t_r = t − R(t_r)/c. Differentiating the implicit relation gives the building blocks

**第 1 步 — 由势求场。** 场为 E = −∇φ − ∂A/∂t 与 B = ∇×A。微妙之处在于 φ 与 A 既显式依赖 r 与 t，又*通过*推迟时刻 t_r(r,t) 依赖，因为 R 出现于 t_r = t − R(t_r)/c 中。对隐式关系求导给出基本关系

  ∂t_r/∂t = 1/κ,   ∇t_r = −n/(cκ),

which follow from differentiating t_r = t − R(t_r)/c and using dR/dt_r = −cn·β (Section B, Step 3).

它们来自对 t_r = t − R(t_r)/c 求导并使用 dR/dt_r = −cn·β（B 节第 3 步）。

**Step 2 — Carry out the differentiation.** Applying ∇ and ∂/∂t to φ = (q/4πε₀)/(κR) and A = (β/c)φ, and using the chain-rule factors from Step 1, the algebra (standard; e.g. Jackson, Griffiths) yields the exact field

**第 2 步 — 执行微分。** 将 ∇ 与 ∂/∂t 作用于 φ = (q/4πε₀)/(κR) 与 A = (β/c)φ，并使用第 1 步的链式因子，代数运算（标准；如 Jackson、Griffiths）给出精确场

  E(r,t) = (q/4πε₀) { (n − β)(1 − β²)/(κ³R²) + n × [(n − β) × a]/(c²κ³R) }_ret.

**Step 3 — Identify the two pieces.** The first term, E_vel ∝ (n − β)(1 − β²)/(κ³R²), is independent of acceleration and falls off as **1/R²**; it is the boosted Coulomb (generalized "velocity") field, reducing to q/(4πε₀R²) when β → 0. The second term,

**第 3 步 — 辨认两部分。** 第一项 E_vel ∝ (n − β)(1 − β²)/(κ³R²) 与加速度无关，按 **1/R²** 衰减；它是洛伦兹变换的库仑（广义"速度"）场，β → 0 时退化为 q/(4πε₀R²)。第二项，

  **E_acc = (q/4πε₀c²) [n × ((n − β) × a)] / (κ³R)**,

is linear in the acceleration a and falls off only as **1/R**. The magnetic field is exactly B = (n × E)/c.

正比于加速度 a，仅按 **1/R** 衰减。磁场精确为 B = (n × E)/c。

**Step 4 — Only the 1/R field radiates.** The Poynting flux is S = (1/μ₀)E×B, with |S| ∝ |E|². Through a sphere of radius R the power is ∮ S·dA ∝ |E|² R². The velocity field gives |E_vel|² R² ∝ R²/R⁴ = 1/R² → 0 as R → ∞: no net energy escapes. The acceleration field gives |E_acc|² R² ∝ R²/R² = const, a finite, R-independent flux. Hence **only the acceleration (radiation) field transports energy to infinity** — radiation requires acceleration. ∎

**第 4 步 — 只有 1/R 场辐射。** 坡印亭通量 S = (1/μ₀)E×B，|S| ∝ |E|²。穿过半径 R 球面的功率为 ∮ S·dA ∝ |E|² R²。速度场给出 |E_vel|² R² ∝ R²/R⁴ = 1/R² → 0（R → ∞）：无净能量逸出。加速度场给出 |E_acc|² R² ∝ R²/R² = 常数，给出有限、与 R 无关的通量。故**只有加速度（辐射）场将能量输运到无穷远**——辐射需要加速度。∎

---

## D. Electric-Dipole Radiation and Reduction to Larmor · 电偶极辐射及向拉莫尔公式的退化

**Claim.** For a localized oscillating source of dipole moment p(t), the radiated angular power is dP/dΩ = (μ₀ p̈²/16π²c) sin²θ and the total power is P = μ₀ p̈²/(6πc) = p̈²/(6πε₀c³). For a single charge (p = qd) this reduces to the Larmor formula P = μ₀q²a²/(6πc) of Module 1.11.

**命题。** 对偶极矩为 p(t) 的局域振荡源，辐射角功率为 dP/dΩ = (μ₀ p̈²/16π²c) sin²θ，总功率为 P = μ₀ p̈²/(6πc) = p̈²/(6πε₀c³)。对单个电荷（p = qd），它退化为模块 1.11 的拉莫尔公式 P = μ₀q²a²/(6πc)。

**Step 1 — Radiation field of a dipole.** In the radiation (far) zone of a slowly moving source (β ≪ 1), set β → 0 in the acceleration field of Section C and sum over the charges. With p(t) = ∫ r' ρ(r',t) d³r' so that p̈ = ∫ r' ρ̈ d³r' = Σ q a (the collective "qa"), the non-relativistic radiation field is

**第 1 步 — 偶极的辐射场。** 在缓变源（β ≪ 1）的辐射（远）区，将 C 节加速度场中 β → 0 并对电荷求和。设 p(t) = ∫ r' ρ(r',t) d³r'，故 p̈ = ∫ r' ρ̈ d³r' = Σ q a（集体的"qa"），非相对论辐射场为

  E_rad = (μ₀/4πr) [n × (n × p̈)]_ret,   B_rad = (n × E_rad)/c,

evaluated at the retarded time t_r = t − r/c. The magnitude is |E_rad| = (μ₀/4πr) p̈ sin θ, θ being the angle between n and p̈.

在推迟时刻 t_r = t − r/c 取值。其大小为 |E_rad| = (μ₀/4πr) p̈ sin θ，θ 为 n 与 p̈ 的夹角。

**Step 2 — Poynting flux.** The radiated power per unit area is |S| = |E_rad|²/(μ₀c) (since |E_rad×B_rad|/μ₀ = |E_rad|²/(μ₀c) for the orthogonal radiation fields):

**第 2 步 — 坡印亭通量。** 单位面积辐射功率为 |S| = |E_rad|²/(μ₀c)（因正交辐射场 |E_rad×B_rad|/μ₀ = |E_rad|²/(μ₀c)）：

  |S| = (1/μ₀c)(μ₀/4πr)² p̈² sin²θ = (μ₀/16π²c) p̈² sin²θ / r².

**Step 3 — Angular power.** Multiply by r² to get power per solid angle dΩ:

**第 3 步 — 角功率。** 乘以 r² 得单位立体角功率 dΩ：

  **dP/dΩ = r² |S| = (μ₀ p̈²/16π²c) sin²θ**.

This is the dipole doughnut: zero along the dipole axis (θ = 0, π), maximum broadside (θ = π/2).

这是偶极甜甜圈：沿偶极轴（θ = 0, π）为零，垂直方向（θ = π/2）最大。

**Step 4 — Integrate over the sphere.** With dΩ = sin θ dθ dφ:

**第 4 步 — 对球面积分。** 取 dΩ = sin θ dθ dφ：

  P = (μ₀ p̈²/16π²c) ∫₀^{2π} dφ ∫₀^π sin²θ · sin θ dθ = (μ₀ p̈²/16π²c) · 2π · (4/3),

using ∫₀^π sin³θ dθ = 4/3 (Module 1.11, Section D). Therefore

利用 ∫₀^π sin³θ dθ = 4/3（模块 1.11，D 节）。因此

  **P = μ₀ p̈²/(6πc)**,   equivalently   **P = p̈²/(6πε₀c³)** (using 1/ε₀ = μ₀c²).

**Step 5 — Reduction to Larmor.** A single point charge has dipole moment p = q d, where d(t) is its position; then ṗ = q ḋ = q v and p̈ = q v̇ = q a. Substituting p̈² = q² a²:

**第 5 步 — 退化为拉莫尔公式。** 单个点电荷的偶极矩为 p = q d，d(t) 为其位置；则 ṗ = q ḋ = q v，p̈ = q v̇ = q a。代入 p̈² = q² a²：

  P = μ₀ (qa)²/(6πc) = **μ₀ q² a²/(6πc)**,

exactly the **Larmor formula** of Module 1.11. The dipole result is the natural extension to an arbitrary localized source; we do not re-derive Larmor here but recover it as the one-charge special case. ∎

正是模块 1.11 的**拉莫尔公式**。偶极结果是向任意局域源的自然推广；此处不重新推导拉莫尔公式，而是将其作为单电荷特例重新得到。∎

---

## E. Radiation Reaction: the Abraham–Lorentz Force · 辐射阻尼：阿布拉罕–洛伦兹力

**Claim.** Energy conservation forces a self-force F_rad = (μ₀q²/6πc) ȧ = (q²/6πε₀c³) ȧ on a radiating charge, with characteristic time τ = μ₀q²/(6πmc) = q²/(6πε₀mc³). The resulting equation of motion exhibits runaway and pre-acceleration pathologies.

**命题。** 能量守恒迫使辐射电荷受自力 F_rad = (μ₀q²/6πc) ȧ = (q²/6πε₀c³) ȧ，特征时间 τ = μ₀q²/(6πmc) = q²/(6πε₀mc³)。由此得到的运动方程呈现失控与预加速病态。

**Step 1 — Energy-balance requirement.** The charge radiates Larmor power P = μ₀q²a²/(6πc) (Section D). By energy conservation this energy is drained from the particle's mechanical energy, so the self-force F_rad must do negative work at exactly this rate, on average over any interval where the motion is periodic (so the charge returns to its initial state):

**第 1 步 — 能量平衡要求。** 电荷辐射拉莫尔功率 P = μ₀q²a²/(6πc)（D 节）。由能量守恒，该能量从粒子的机械能中抽取，故自力 F_rad 必以恰好此速率做负功，在运动为周期（电荷回到初态）的任意区间上平均：

  ∫_{t₁}^{t₂} F_rad · v dt = − ∫_{t₁}^{t₂} (μ₀q²/6πc) a² dt.

**Step 2 — Rewrite a² via integration by parts.** Note a² = a·a = v̇·v̇ = (dv̇/dt is the jerk). Use the identity v̇·v̇ = d(v̇·v)/dt − v̈·v (since d(v̇·v)/dt = v̈·v + v̇·v̇). Integrate the right side:

**第 2 步 — 用分部积分改写 a²。** 注意 a² = a·a = v̇·v̇。利用恒等式 v̇·v̇ = d(v̇·v)/dt − v̈·v（因 d(v̇·v)/dt = v̈·v + v̇·v̇）。对右侧积分：

  ∫_{t₁}^{t₂} a² dt = ∫_{t₁}^{t₂} v̇·v̇ dt = [v̇·v]_{t₁}^{t₂} − ∫_{t₁}^{t₂} v̈·v dt.

For periodic (or otherwise vanishing-boundary) motion, the boundary term [v̇·v]_{t₁}^{t₂} = [a·v]_{t₁}^{t₂} vanishes, leaving

对周期（或边界项为零）的运动，边界项 [v̇·v]_{t₁}^{t₂} = [a·v]_{t₁}^{t₂} 消失，剩

  ∫_{t₁}^{t₂} a² dt = − ∫_{t₁}^{t₂} v̈·v dt = − ∫_{t₁}^{t₂} ȧ·v dt.

**Step 3 — Read off the force.** Substitute into the energy balance of Step 1:

**第 3 步 — 读出力。** 代入第 1 步的能量平衡：

  ∫_{t₁}^{t₂} F_rad · v dt = − (μ₀q²/6πc) ∫_{t₁}^{t₂} a² dt = + (μ₀q²/6πc) ∫_{t₁}^{t₂} ȧ·v dt.

This must hold for arbitrary periodic motion, so the integrands match (up to terms integrating to zero):

此须对任意周期运动成立，故被积函数匹配（至多差积分为零的项）：

  **F_rad = (μ₀q²/6πc) ȧ = (q²/6πε₀c³) ȧ**,

the **Abraham–Lorentz force**, proportional to the jerk ȧ (using 1/ε₀ = μ₀c² for the second form).

即**阿布拉罕–洛伦兹力**，正比于急动度 ȧ（第二种形式用 1/ε₀ = μ₀c²）。

**Step 4 — Characteristic time.** Write F_rad = mτ ȧ. Matching coefficients defines

**第 4 步 — 特征时间。** 写 F_rad = mτ ȧ。匹配系数定义

  **τ = μ₀q²/(6πmc) = q²/(6πε₀mc³)**.

For the electron, τ ≈ 6.3 × 10⁻²⁴ s — the time light takes to cross a classical electron radius. Newton's law with the self-force becomes m a = F_ext + mτ ȧ, i.e. **a − τ ȧ = F_ext/m** (the Abraham–Lorentz equation).

对电子，τ ≈ 6.3 × 10⁻²⁴ s——光穿过经典电子半径的时间。含自力的牛顿定律变为 m a = F_ext + mτ ȧ，即 **a − τ ȧ = F_ext/m**（阿布拉罕–洛伦兹方程）。

**Step 5 — Runaway and pre-acceleration pathologies.** With no external force (F_ext = 0), the equation a − τ ȧ = 0 has the solution a(t) = a(0) e^{t/τ}: the acceleration grows without bound — an unphysical **runaway**. Demanding a → 0 as t → ∞ instead forces the integral (acausal) solution

**第 5 步 — 失控与预加速病态。** 无外力（F_ext = 0）时，方程 a − τ ȧ = 0 有解 a(t) = a(0) e^{t/τ}：加速度无界增长——非物理的**失控**。改为要求 t → ∞ 时 a → 0 则迫使积分（非因果）解

  a(t) = (1/mτ) ∫_t^∞ e^{−(t'−t)/τ} F_ext(t') dt',

in which a(t) depends on the **future** force F_ext(t' > t): the charge begins to accelerate a time ~ τ *before* the force is applied — **pre-acceleration**. Both pathologies signal that the rigid point charge is an over-idealization; they are removed only in QED, where F_rad is the classical limit of the electron self-energy and the divergences are absorbed by mass renormalization (Modules 8.2 / 6.x). ∎

其中 a(t) 依赖于**未来**的力 F_ext(t' > t)：电荷在力施加*之前*约 τ 时间便开始加速——**预加速**。两种病态都表明刚性点电荷是过度理想化；它们只在量子电动力学中消除，其中 F_rad 是电子自能的经典极限，发散通过质量重整化被吸收（模块 8.2 / 6.x）。∎

---

*The retarded potentials and Liénard–Wiechert fields are the complete classical solution of radiation from moving charges; the dipole formula organizes the leading multipole emission; and the Abraham–Lorentz force — together with its runaway/pre-acceleration pathologies — marks the precise point at which the classical theory of the electron must yield to quantum electrodynamics.*

*推迟势与李纳–维谢尔场是运动电荷辐射的完整经典解；偶极公式组织领头多极发射；阿布拉罕–洛伦兹力——连同其失控/预加速病态——标志着电子的经典理论必须让位于量子电动力学的确切节点。*

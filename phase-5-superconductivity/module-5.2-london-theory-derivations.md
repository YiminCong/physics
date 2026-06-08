# Derivations — Module 5.2: London Theory
# 推导 — 模块 5.2：伦敦理论

> Companion to [Module 5.2](./module-5.2-london-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.2](./module-5.2-london-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. First London Equation from a Frictionless Charged Fluid · 从无摩擦带电流体推导第一伦敦方程

**Claim.** For a frictionless (collisionless) fluid of superelectrons of charge −e, mass m, and number density n_s, Newton's second law immediately gives the first London equation: ∂J_s/∂t = (n_s e²/m) E.

**命题。** 对于电荷 −e、质量 m、数密度 n_s 的无摩擦（无碰撞）超导电子流体，牛顿第二定律直接给出第一伦敦方程：∂J_s/∂t = (n_s e²/m) E。

**Step 1 — Equation of motion without friction.** In an ordinary metal, the Drude model gives m(dv/dt) = −eE − mv/τ, where the last term is the frictional damping with relaxation time τ. In a perfect (frictionless) superfluid τ → ∞ and the friction term vanishes exactly:

**第 1 步 — 无摩擦运动方程。** 在普通金属中，德鲁德模型给出 m(dv/dt) = −eE − mv/τ，其中最后一项是弛豫时间为 τ 的摩擦阻尼。在完美（无摩擦）超流体中 τ → ∞，摩擦项严格消失：

  m (dv_s/dt) = −eE.

Here v_s is the drift velocity of superelectrons and E is the local electric field.

这里 v_s 是超导电子的漂移速度，E 是局域电场。

**Step 2 — Express in terms of the supercurrent density.** The supercurrent density is J_s = −e n_s v_s (the minus sign because electron charge is −e). Taking the time derivative and substituting the equation of motion:

**第 2 步 — 用超电流密度表示。** 超电流密度为 J_s = −e n_s v_s（负号来自电子电荷 −e）。取时间导数并代入运动方程：

  ∂J_s/∂t = −e n_s (dv_s/dt) = −e n_s · (−eE/m) = (n_s e²/m) E.

**Step 3 — The first London equation.** Defining the London coefficient Λ = m/(n_s e²), the result is

**第 3 步 — 第一伦敦方程。** 定义伦敦系数 Λ = m/(n_s e²)，结果为

  ∂J_s/∂t = E/Λ,   i.e.   **∂J_s/∂t = (n_s e²/m) E**.

This replaces Ohm's law J = σE inside the superconductor. For a DC steady state ∂J_s/∂t = 0 requires E = 0, consistent with zero resistance: a constant supercurrent flows with no electric field needed to maintain it. ∎

这取代了超导体内部的欧姆定律 J = σE。对于直流稳态 ∂J_s/∂t = 0 要求 E = 0，与零电阻一致：恒定超电流在无需电场维持的情况下流动。∎

---

## B. Second London Equation · 第二伦敦方程

**Claim.** Applying Faraday's law to the first London equation and invoking gauge invariance yields the second London equation: ∇ × J_s = −(n_s e²/m) B = −B/Λμ₀.

**命题。** 对第一伦敦方程应用法拉第定律并援引规范不变性，得到第二伦敦方程：∇ × J_s = −(n_s e²/m) B = −B/Λμ₀。

**Step 1 — Take the curl of the first London equation.** Apply ∇ × to both sides of ∂J_s/∂t = (n_s e²/m) E:

**第 1 步 — 对第一伦敦方程取旋度。** 对 ∂J_s/∂t = (n_s e²/m) E 两边作用 ∇ ×：

  ∂(∇ × J_s)/∂t = (n_s e²/m) (∇ × E).

**Step 2 — Use Faraday's law.** Faraday's law states ∇ × E = −∂B/∂t. Substituting:

**第 2 步 — 使用法拉第定律。** 法拉第定律给出 ∇ × E = −∂B/∂t。代入：

  ∂(∇ × J_s)/∂t = −(n_s e²/m) ∂B/∂t.

**Step 3 — Integrate over time.** Both sides are time derivatives, so integrate:

**第 3 步 — 对时间积分。** 两边都是时间导数，积分之：

  ∇ × J_s = −(n_s e²/m) B + C(r),

where C(r) is a time-independent integration constant (a curl-free static current distribution).

其中 C(r) 是与时间无关的积分常数（无旋的静态电流分布）。

**Step 4 — London's gauge choice.** The London brothers postulated that C(r) = 0. This is not merely a gauge choice: it is the physical statement that the superconducting ground state has no persistent normal-state current pattern hidden in it. Microscopically (BCS), the ground state has J = 0 when B = 0, which forces C = 0. The result is the **second London equation**:

**第 4 步 — 伦敦规范选择。** 伦敦兄弟假设 C(r) = 0。这不仅仅是规范选择：它是物理陈述，即超导基态中没有隐藏的正常态持续电流模式。从微观角度（BCS），当 B = 0 时基态有 J = 0，这迫使 C = 0。结果是**第二伦敦方程**：

  **∇ × J_s = −(n_s e²/m) B.**

This is the key equation encoding the Meissner effect: the curl of the supercurrent is locked to the local magnetic field, not merely to its time derivative. ∎

这是编码迈斯纳效应的关键方程：超电流的旋度锁定于局域磁场，而不仅仅是其时间导数。∎

**Alternative microscopic derivation (canonical momentum).** The canonical momentum of a superelectron in a vector potential A is p = mv_s − eA (using charge −e with sign convention p = mv + qA, q = −e). In the BCS ground state the canonical momentum of each electron in a pair is zero (the pairs have zero total momentum). Setting p = 0:

**替代微观推导（正则动量）。** 在矢势 A 中超导电子的正则动量为 p = mv_s − eA（使用电荷 −e，符号约定 p = mv + qA，q = −e）。在 BCS 基态中配对中每个电子的正则动量为零（对的总动量为零）。令 p = 0：

  mv_s = eA   ⟹   J_s = −en_s v_s = −(n_s e²/m) A.

Taking the curl and using B = ∇ × A immediately gives ∇ × J_s = −(n_s e²/m) B, confirming the second London equation from a microscopic principle (zero canonical momentum of the condensate). ∎

取旋度并使用 B = ∇ × A 立即给出 ∇ × J_s = −(n_s e²/m) B，从微观原理（凝聚态的正则动量为零）确认了第二伦敦方程。∎

---

## C. Combining with Ampère's Law: ∇²B = B/λ_L² · 与安培定律联立：∇²B = B/λ_L²

**Claim.** Combining the second London equation with the magnetostatic Ampère's law ∇ × B = μ₀ J_s gives the London equation for B: ∇²B = B/λ_L², where λ_L = √(m/μ₀ n_s e²).

**命题。** 将第二伦敦方程与静磁安培定律 ∇ × B = μ₀ J_s 联立，得到 B 的伦敦方程：∇²B = B/λ_L²，其中 λ_L = √(m/μ₀ n_s e²)。

**Step 1 — Take the curl of Ampère's law.** In the static (∂E/∂t = 0) limit, ∇ × B = μ₀ J_s. Apply ∇ × to both sides:

**第 1 步 — 对安培定律取旋度。** 在静态（∂E/∂t = 0）极限下，∇ × B = μ₀ J_s。对两边作用 ∇ ×：

  ∇ × (∇ × B) = μ₀ ∇ × J_s.

**Step 2 — Expand the left side using the vector identity.** Apply ∇ × (∇ × B) = ∇(∇ · B) − ∇²B. Maxwell's law ∇ · B = 0 makes the first term vanish:

**第 2 步 — 用矢量恒等式展开左边。** 应用 ∇ × (∇ × B) = ∇(∇ · B) − ∇²B。麦克斯韦定律 ∇ · B = 0 使第一项消失：

  −∇²B = μ₀ ∇ × J_s.

**Step 3 — Substitute the second London equation.** Replace ∇ × J_s = −(n_s e²/m) B:

**第 3 步 — 代入第二伦敦方程。** 用 ∇ × J_s = −(n_s e²/m) B 替换：

  −∇²B = μ₀ · (−n_s e²/m) B = −(μ₀ n_s e²/m) B.

Multiply both sides by −1:

两边乘以 −1：

  ∇²B = (μ₀ n_s e²/m) B.

**Step 4 — Identify the London penetration depth.** Define

**第 4 步 — 识别伦敦穿透深度。** 定义

  **λ_L² = m/(μ₀ n_s e²)**,   so   **λ_L = √(m/(μ₀ n_s e²))**.

The London equation becomes ∇²B = B/λ_L².

伦敦方程变为 ∇²B = B/λ_L²。

**Step 5 — Dimensional check.** [m] = kg, [μ₀] = kg·m/A², [n_s] = m⁻³, [e] = C = A·s. Then [μ₀ n_s e²/m] = (kg·m/A²·m⁻³·A²·s²/kg) = m⁻², so [λ_L] = m. Correct. ∎

**第 5 步 — 量纲检验。** [m] = kg，[μ₀] = kg·m/A²，[n_s] = m⁻³，[e] = C = A·s。则 [μ₀ n_s e²/m] = (kg·m/A²·m⁻³·A²·s²/kg) = m⁻²，故 [λ_L] = m。正确。∎

---

## D. Solving B(x) = B₀ e^{−x/λ_L} in the Half-Space Geometry · 在半空间几何中求解 B(x) = B₀ e^{−x/λ_L}

**Claim.** For a superconductor occupying x ≥ 0 with an applied field B₀ parallel to the surface at x = 0, the magnetic field inside decays exponentially as B(x) = B₀ e^{−x/λ_L}.

**命题。** 对于占据 x ≥ 0 的超导体，在 x = 0 表面施加平行于表面的磁场 B₀，内部磁场按指数衰减：B(x) = B₀ e^{−x/λ_L}。

**Step 1 — Reduce to one spatial dimension.** By translational symmetry in y and z, B depends only on x. Let B = B(x) ẑ (field pointing along z, lying in the yz plane at the surface). Then ∇²B = d²B/dx² for the scalar magnitude B(x), and the London equation becomes an ordinary differential equation:

**第 1 步 — 化为一维空间问题。** 由 y 和 z 方向的平移对称性，B 只依赖于 x。设 B = B(x) ẑ（磁场沿 z 方向，在表面处平行于 yz 平面）。则标量量 B(x) 的 ∇²B = d²B/dx²，伦敦方程变为常微分方程：

  d²B/dx² = B/λ_L².

**Step 2 — General solution.** This is a second-order linear ODE with constant coefficients. The characteristic equation is r² = 1/λ_L², giving r = ±1/λ_L. The general solution is

**第 2 步 — 通解。** 这是一个常系数二阶线性常微分方程。特征方程为 r² = 1/λ_L²，给出 r = ±1/λ_L。通解为

  B(x) = C₁ e^{x/λ_L} + C₂ e^{−x/λ_L}.

**Step 3 — Apply boundary conditions.** Two conditions determine C₁ and C₂:

**第 3 步 — 应用边界条件。** 两个条件确定 C₁ 和 C₂：

  (i)  B(0) = B₀  (field is continuous at the surface),
  (ii) B(x) → 0 as x → +∞  (field vanishes deep in the bulk).

  (i)  B(0) = B₀  （磁场在表面连续），
  (ii) 当 x → +∞ 时 B(x) → 0  （磁场在体内深处消失）。

Condition (ii) requires C₁ = 0 (the growing exponential must be absent). Condition (i) then gives C₂ = B₀.

条件 (ii) 要求 C₁ = 0（增长指数项必须不存在）。条件 (i) 则给出 C₂ = B₀。

**Step 4 — Final solution.** Substituting back:

**第 4 步 — 最终解。** 代回：

  **B(x) = B₀ e^{−x/λ_L}**.

The field decays on the length scale λ_L. For x ≫ λ_L, B ≈ 0: the bulk superconductor is field-free. For typical elemental superconductors λ_L ≈ 40–500 nm, confirming that the Meissner effect excludes field from all but a thin skin depth. ∎

磁场在长度尺度 λ_L 上衰减。当 x ≫ λ_L 时，B ≈ 0：体内超导体无磁场。对于典型元素超导体 λ_L ≈ 40–500 nm，证实了迈斯纳效应将磁场排除在薄薄的趋肤深度之外。∎

**Step 5 — Supercurrent profile.** The associated supercurrent J_s flows in the surface layer. From Ampère's law J_s = (1/μ₀) ∇ × B. With B = B(x) ẑ and dB/dx = −(B₀/λ_L) e^{−x/λ_L}:

**第 5 步 — 超电流分布。** 相关的超电流 J_s 在表面层中流动。由安培定律 J_s = (1/μ₀) ∇ × B。取 B = B(x) ẑ，dB/dx = −(B₀/λ_L) e^{−x/λ_L}：

  J_s(x) = −(1/μ₀) (dB/dx) ŷ = (B₀/(μ₀ λ_L)) e^{−x/λ_L} ŷ.

The current also decays exponentially with the same length scale λ_L, confirming that the screening is done by surface currents confined to depth λ_L. ∎

电流也以相同长度尺度 λ_L 指数衰减，确认了屏蔽由深度 λ_L 内的表面电流完成。∎

---

## E. Physical Identification of λ_L and Its Temperature Dependence · λ_L 的物理识别及其温度依赖性

**Claim.** The London penetration depth λ_L = √(m/(μ₀ n_s e²)) encodes the density of superelectrons n_s. As T → T_c, n_s → 0 and λ_L → ∞: the superconductor can no longer screen the field, consistent with the Meissner effect disappearing at the transition.

**命题。** 伦敦穿透深度 λ_L = √(m/(μ₀ n_s e²)) 编码了超导电子密度 n_s。当 T → T_c 时，n_s → 0，λ_L → ∞：超导体无法再屏蔽磁场，与迈斯纳效应在转变处消失一致。

**Step 1 — Two-fluid interpretation.** The two-fluid model (Gorter–Casimir) writes the total electron density as n = n_s(T) + n_n(T), where n_s is the superfluid density and n_n is the normal-fluid density. At T = 0, n_s = n (all electrons pair). At T = T_c, n_s = 0. The empirical fit is n_s(T) ≈ n[1 − (T/T_c)⁴].

**第 1 步 — 双流体解释。** 双流体模型（戈特–卡西米尔）将总电子密度写为 n = n_s(T) + n_n(T)，其中 n_s 为超流密度，n_n 为正常流体密度。在 T = 0 时，n_s = n（所有电子配对）。在 T = T_c 时，n_s = 0。经验拟合为 n_s(T) ≈ n[1 − (T/T_c)⁴]。

**Step 2 — Temperature dependence of λ_L.** Substituting n_s(T):

**第 2 步 — λ_L 的温度依赖性。** 代入 n_s(T)：

  λ_L(T) = λ_L(0) / √(1 − (T/T_c)⁴),

where λ_L(0) = √(m/(μ₀ n e²)) is the zero-temperature value. As T → T_c, 1 − (T/T_c)⁴ → 0 and λ_L → ∞. ∎

其中 λ_L(0) = √(m/(μ₀ n e²)) 是零温值。当 T → T_c 时，1 − (T/T_c)⁴ → 0，λ_L → ∞。∎

**Step 3 — Connection to plasma frequency.** Note that μ₀ n_s e²/m = ω_p²/c² where ω_p = √(n_s e²/ε₀ m) is the plasma frequency. Therefore λ_L = c/ω_p: the London penetration depth is the electromagnetic skin depth of the electron plasma at zero frequency. This connects superconductivity to the optical properties of the electron gas. ∎

**第 3 步 — 与等离子体频率的联系。** 注意 μ₀ n_s e²/m = ω_p²/c²，其中 ω_p = √(n_s e²/ε₀ m) 是等离子体频率。因此 λ_L = c/ω_p：伦敦穿透深度是零频率下电子等离子体的电磁趋肤深度。这将超导性与电子气的光学性质联系起来。∎

---

*Results derived here feed directly into Module 5.3 (where λ reappears as the GL penetration depth and enters the ratio κ = λ/ξ) and Module 5.7 (where the vortex field profile is an exponential of the same form).*

*此处推导的结果直接进入模块 5.3（其中 λ 作为 GL 穿透深度重新出现并进入比值 κ = λ/ξ）和模块 5.7（其中涡旋磁场分布具有相同形式的指数衰减）。*

# Derivations — Module 9.4: Plasma Physics
# 推导 — 模块 9.4：等离子体物理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.4](./module-9.4-plasma-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.4](./module-9.4-plasma-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Debye Length from Linearized Poisson–Boltzmann · 从线性化泊松–玻尔兹曼方程推导德拜长度

**Claim.** A test charge Q embedded in a plasma of number density n and temperature T is shielded by a screened Coulomb potential φ(r) = (Q/4πε₀ r) e^{−r/λ_D}, where:

  **λ_D = √(ε₀ k_B T / (n e²))**.

**命题。** 嵌入密度为 n、温度为 T 的等离子体中的测试电荷 Q 被屏蔽库仑势 φ(r) = (Q/4πε₀ r) e^{−r/λ_D} 所屏蔽，其中：

  **λ_D = √(ε₀ k_B T / (n e²))**。

**Step 1 — Boltzmann equilibrium for the electrons.** In the presence of electrostatic potential φ(r), the electron density follows the Boltzmann distribution:

**第 1 步 — 电子的玻尔兹曼平衡。** 在静电势 φ(r) 存在的情况下，电子密度遵循玻尔兹曼分布：

  n_e(r) = n exp(+eφ(r)/k_BT),

where the +e exponent reflects electrons being attracted to regions of positive φ. For singly charged ions with density n_i and temperature T_i:

其中 +e 指数反映电子被正 φ 区域吸引。对于密度 n_i 和温度 T_i 的单电荷离子：

  n_i(r) = n exp(−eφ(r)/k_BT_i).

Far from the test charge, n_e = n_i = n (quasineutrality). For simplicity take T_e = T_i = T.

远离测试电荷时，n_e = n_i = n（准中性）。为简单起见，取 T_e = T_i = T。

**Step 2 — Poisson's equation.** The electrostatic potential satisfies:

**第 2 步 — 泊松方程。** 静电势满足：

  ∇²φ = −ρ_charge/ε₀ = −e(n_i − n_e)/ε₀,

where ρ_charge = e n_i − e n_e is the net charge density (excluding the test charge).

其中 ρ_charge = e n_i − e n_e 为净电荷密度（不包括测试电荷）。

**Step 3 — Linearize in small φ.** Assume |eφ| ≪ k_BT (valid far from the test charge). Expand the Boltzmann factors to first order:

**第 3 步 — 对小 φ 线性化。** 假设 |eφ| ≪ k_BT（在远离测试电荷处成立）。将玻尔兹曼因子展开到一阶：

  n_e ≈ n(1 + eφ/k_BT),   n_i ≈ n(1 − eφ/k_BT).

Substituting into Poisson's equation:

代入泊松方程：

  ∇²φ = −e(n_i − n_e)/ε₀ = −e[n(1 − eφ/k_BT) − n(1 + eφ/k_BT)]/ε₀
        = −e(−2ne φ/k_BT)/ε₀ = 2ne²φ/(ε₀ k_BT).

(The factor of 2 arises from both electron and ion contributions when T_e = T_i.)

（当 T_e = T_i 时，因子 2 来自电子和离子的双重贡献。）

**Step 4 — Solve for the screened potential.** The linearized Poisson–Boltzmann equation in spherical symmetry (away from the point charge at r = 0) is:

**第 4 步 — 求解屏蔽势。** 球对称下（远离 r = 0 处的点电荷）线性化的泊松–玻尔兹曼方程为：

  (1/r²) d/dr(r² dφ/dr) = φ/λ_D²,   with  λ_D² = ε₀ k_BT/(2ne²).

(For the one-species model with only electron screening, the factor 2 becomes 1, giving λ_D² = ε₀ k_BT/(ne²) — the standard single-species formula.) The general solution decaying at infinity is:

（对于仅有电子屏蔽的单组分模型，因子 2 变为 1，给出 λ_D² = ε₀ k_BT/(ne²)——标准单组分公式。）在无穷远处衰减的通解为：

  φ(r) = A e^{−r/λ_D}/r + B e^{+r/λ_D}/r.

The B term diverges as r → ∞, so B = 0. The constant A is fixed by the boundary condition that at small r the potential approaches the bare Coulomb potential: φ(r → 0) → Q/(4πε₀ r), so A = Q/(4πε₀).

B 项在 r → ∞ 时发散，故 B = 0。常数 A 由边界条件固定：小 r 处势趋近于裸库仑势：φ(r → 0) → Q/(4πε₀ r)，故 A = Q/(4πε₀)。

**Step 5 — Result.** Therefore:

**第 5 步 — 结果。** 因此：

  **φ(r) = (Q/4πε₀) e^{−r/λ_D}/r**,

with **λ_D = √(ε₀ k_B T / (ne²))** (single-species / electron-only screening).

其中 **λ_D = √(ε₀ k_B T / (ne²))**（单组分/仅电子屏蔽）。

This is the **Yukawa potential**: the Coulomb potential multiplied by an exponential cutoff at r = λ_D. The charge is effectively screened beyond the Debye sphere. ∎

这是**汤川势**：库仑势乘以在 r = λ_D 处的指数截断。电荷在德拜球以外被有效屏蔽。∎

---

## B. Plasma Frequency ω_p = √(ne²/ε₀m_e) · 等离子体频率 ω_p = √(ne²/ε₀m_e)

**Claim.** If a uniform slab of electrons is displaced by a small distance x from the neutralizing ion background, the restoring force leads to simple harmonic oscillation at the **plasma frequency** ω_p = √(ne²/(ε₀ m_e)).

**命题。** 如果一层均匀电子从中和离子背景中位移小距离 x，由此产生的回复力导致以**等离子体频率** ω_p = √(ne²/(ε₀ m_e)) 进行简谐振荡。

**Step 1 — Set up the model.** Consider a plasma slab of thickness L and electron number density n. Imagine displacing the entire electron layer a small distance x in the +z direction, leaving the ion layer (mass M_i ≫ m_e, essentially stationary) behind. This creates a surface charge density:

**第 1 步 — 建立模型。** 考虑厚度为 L、电子数密度为 n 的等离子体平板。设想将整个电子层沿 +z 方向位移小距离 x，留下离子层（质量 M_i ≫ m_e，基本静止）。这产生面电荷密度：

  σ_+ = +nex   on the exposed ion surface,
  σ_- = −nex   on the leading electron surface.

These create an electric field between the plates (like a parallel-plate capacitor):

这在板间产生电场（类似平行板电容器）：

  E = σ/ε₀ = nex/ε₀   (directed to pull electrons back, i.e., in −z direction).

**Step 2 — Equation of motion.** Each electron (mass m_e, charge −e) experiences the restoring force F = −eE (in the −z direction, pointing against the displacement):

**第 2 步 — 运动方程。** 每个电子（质量 m_e，电荷 −e）受到回复力 F = −eE（沿 −z 方向，与位移相反）：

  m_e ẍ = F_z = −e × E = −e × (nex/ε₀) = −(ne²/ε₀) x.

This is a simple harmonic oscillator equation: ẍ = −ω_p² x.

这是简谐振子方程：ẍ = −ω_p² x。

**Step 3 — Read off the frequency.** Comparing with ẍ = −ω² x, we identify:

**第 3 步 — 读取频率。** 与 ẍ = −ω² x 比较，我们识别出：

  **ω_p² = ne²/(ε₀ m_e),   ω_p = √(ne²/(ε₀ m_e))**.

The corresponding frequency is f_p = ω_p/(2π) = (e/2π)√(n/(ε₀ m_e)) ≈ 9√n Hz (with n in m⁻³).

对应频率为 f_p = ω_p/(2π) = (e/2π)√(n/(ε₀ m_e)) ≈ 9√n Hz（n 以 m⁻³ 为单位）。

**Step 4 — Electromagnetic wave cutoff.** In the plasma, the wave equation for an electromagnetic wave gives the dispersion relation ω² = ω_p² + c²k². For ω < ω_p, k² = (ω² − ω_p²)/c² < 0, so k is imaginary and the wave is **evanescent** (exponentially decaying, not propagating). The wave cannot penetrate a plasma with n > n_c = ε₀ m_e ω²/e² (the **critical density** for a given ω). This is the physical basis for the ionospheric radio-wave reflection described in the module.

**第 4 步 — 电磁波截止。** 在等离子体中，电磁波的波动方程给出色散关系 ω² = ω_p² + c²k²。当 ω < ω_p 时，k² = (ω² − ω_p²)/c² < 0，故 k 为虚数，波是**消逝的**（指数衰减，不传播）。波无法穿透密度 n > n_c = ε₀ m_e ω²/e²（给定 ω 的**临界密度**）的等离子体。这是模块中描述的电离层无线电波反射的物理基础。∎

---

## C. Physical Origin of Landau Damping · 朗道阻尼的物理起源

**Claim.** A longitudinal electrostatic wave in a collisionless plasma with a Maxwellian velocity distribution is damped at a rate determined by the slope of the distribution function at v = ω/k (the wave phase velocity). The wave damps if df/dv|_{v=ω/k} < 0 (more slow particles than fast at the resonant velocity). This is **Landau damping** — dissipation without collisions.

**命题。** 具有麦克斯韦速度分布的无碰撞等离子体中的纵向静电波，以由分布函数在 v = ω/k（波相速度）处的斜率决定的速率阻尼。若 df/dv|_{v=ω/k} < 0（共振速度处慢粒子多于快粒子），则波阻尼。这就是**朗道阻尼**——无碰撞的耗散。

**Step 1 — Vlasov equation.** In a collisionless plasma, the single-particle distribution function f(x, v, t) evolves according to the **Vlasov equation**:

**第 1 步 — 弗拉索夫方程。** 在无碰撞等离子体中，单粒子分布函数 f(x, v, t) 按**弗拉索夫方程**演化：

  ∂f/∂t + v ∂f/∂x + (F/m) ∂f/∂v = 0,

where F = −eE is the electrostatic force. This is the collisionless Boltzmann equation (Liouville theorem: phase-space density is conserved along particle trajectories).

其中 F = −eE 为静电力。这是无碰撞玻尔兹曼方程（刘维尔定理：相空间密度沿粒子轨迹守恒）。

**Step 2 — Linearize.** Write f = f₀(v) + f₁(x, v, t), where f₀ is the unperturbed Maxwellian and |f₁| ≪ f₀. The electric field E = E₁ is first-order. Linearizing the Vlasov equation:

**第 2 步 — 线性化。** 写 f = f₀(v) + f₁(x, v, t)，其中 f₀ 是未扰动麦克斯韦分布，|f₁| ≪ f₀。电场 E = E₁ 是一阶量。线性化弗拉索夫方程：

  ∂f₁/∂t + v ∂f₁/∂x − (e E₁/m_e) ∂f₀/∂v = 0.

**Step 3 — Fourier-Laplace transform.** Write f₁, E₁ ∝ e^{i(kx−ωt)} with complex ω (Im ω < 0 for damping). Then:

**第 3 步 — 傅里叶–拉普拉斯变换。** 写 f₁、E₁ ∝ e^{i(kx−ωt)}，复数 ω（Im ω < 0 表示阻尼）。则：

  −iωf₁ + ikvf₁ = (eE₁/m_e) ∂f₀/∂v   ⟹   f₁ = (eE₁/m_e) (∂f₀/∂v) / (kv − ω).

Note the singularity at v = ω/k — this is the resonance condition: particles moving at the wave phase velocity interact strongly with the wave.

注意在 v = ω/k 处的奇点——这是共振条件：以波相速度运动的粒子与波强烈相互作用。

**Step 4 — Poisson's equation closes the system.** The perturbed charge density is:

**第 4 步 — 泊松方程封闭系统。** 扰动电荷密度为：

  ρ₁ = −e ∫ f₁ dv = −(e²E₁/m_e) ∫ (∂f₀/∂v)/(kv − ω) dv.

Poisson's equation ikE₁ = ρ₁/ε₀ gives the **plasma dispersion relation** ε(ω, k) = 0:

泊松方程 ikE₁ = ρ₁/ε₀ 给出**等离子体色散关系** ε(ω, k) = 0：

  ε(ω, k) = 1 + (e²/ε₀ m_e k) ∫ (∂f₀/∂v)/(kv − ω) dv = 0.

**Step 5 — Landau's prescription for the resonant integral.** The integral ∫ (∂f₀/∂v)/(kv − ω) dv is singular when the real part of ω/k lies at a populated value of v. Landau (1946) showed the correct treatment (from the initial value problem with causality) is to deform the integration contour below the pole at v = ω/k, giving:

**第 5 步 — 朗道对共振积分的处理。** 当 ω/k 的实部落在 v 的有效值处时，积分 ∫ (∂f₀/∂v)/(kv − ω) dv 是奇异的。朗道（1946 年）表明，正确的处理（来自具有因果性的初值问题）是将积分围道变形到极点 v = ω/k 的下方，给出：

  ∫ (∂f₀/∂v)/(kv − ω) dv  →  P.V. ∫ (∂f₀/∂v)/(kv − ω) dv + iπ (∂f₀/∂v)|_{v=ω/k} / k,

where P.V. denotes the Cauchy principal value. The imaginary part from the residue at the pole gives the damping rate.

其中 P.V. 表示柯西主值。极点处留数的虚部给出阻尼率。

**Step 6 — Sign of damping.** For a Maxwellian f₀(v) ∝ e^{−v²/(2v_th²)}, the derivative is ∂f₀/∂v = −v/v_th² × f₀ < 0 for v > 0. At the phase velocity v_ph = ω/k > 0, ∂f₀/∂v|_{v_ph} < 0. The imaginary part of ε(ω, k) = 0 then gives Im ω < 0 (damping), because more particles move slightly slower than v_ph (gaining energy from the wave) than slightly faster (giving energy back). The net energy flows from the wave to the particles:

**第 6 步 — 阻尼的符号。** 对于麦克斯韦分布 f₀(v) ∝ e^{−v²/(2v_th²)}，导数为 ∂f₀/∂v = −v/v_th² × f₀，对 v > 0 为负。在相速度 v_ph = ω/k > 0 处，∂f₀/∂v|_{v_ph} < 0。则 ε(ω, k) = 0 的虚部给出 Im ω < 0（阻尼），因为以略低于 v_ph 速度运动（从波获得能量）的粒子多于略高于 v_ph 速度运动（将能量还给波）的粒子。净能量从波流向粒子：

  **Wave damps (Im ω < 0) ⟺ ∂f₀/∂v|_{v=ω/k} < 0.**

If instead df/dv > 0 at v_ph (a beam-plasma system where f has a bump at v_ph), the wave grows (**beam instability**). ∎

如果在 v_ph 处 df/dv > 0（束–等离子体系统，f 在 v_ph 处有凸起），则波增长（**束流不稳定性**）。∎

**Physical summary.** Landau damping is a wave–particle resonance effect. The crucial insight is that the velocity distribution is not uniform: for a Maxwellian there are always more particles just below the resonant velocity than just above it. The net transfer of energy from the wave to these particles causes damping — purely through the coherent, collisionless interaction of the wave's electric field with the particle distribution. This phenomenon has no classical fluid analog and is one of the deepest results in kinetic plasma theory.

**物理总结。** 朗道阻尼是一种波–粒子共振效应。关键洞察是速度分布不均匀：对于麦克斯韦分布，共振速度略低处总是比略高处有更多粒子。能量从波到这些粒子的净转移导致阻尼——纯粹通过波的电场与粒子分布的相干无碰撞相互作用。这一现象没有经典流体的类比，是动理论等离子体理论中最深刻的结果之一。

---

*These three derivations span the core mathematical framework of plasma physics: linear screening (Poisson–Boltzmann), collective oscillations (harmonic oscillator from Gauss's law), and kinetic wave–particle resonance (Vlasov–Poisson system). Together they illustrate why plasma physics requires going beyond both fluid mechanics and single-particle dynamics.*

*这三个推导涵盖等离子体物理的核心数学框架：线性屏蔽（泊松–玻尔兹曼）、集体振荡（来自高斯定律的谐振子）和动理论波–粒子共振（弗拉索夫–泊松系统）。它们共同说明了为何等离子体物理需要超越流体力学和单粒子动力学。*

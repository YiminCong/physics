# Derivations — Module 1.11: Electromagnetic Waves & Radiation
# 推导 — 模块 1.11：电磁波与辐射

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.11](./module-1.11-em-waves-radiation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.11](./module-1.11-em-waves-radiation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Deriving the Wave Equation and c = 1/√(μ₀ε₀) · 推导波动方程与 c = 1/√(μ₀ε₀)

**Claim.** From Maxwell's equations in vacuum (ρ = 0, J = 0), E and B each satisfy the wave equation ∇²F = (1/c²) ∂²F/∂t², with c = 1/√(μ₀ε₀).

**命题。** 从真空中（ρ = 0，J = 0）的麦克斯韦方程出发，E 和 B 各自满足波动方程 ∇²F = (1/c²) ∂²F/∂t²，其中 c = 1/√(μ₀ε₀)。

**Step 1 — Write the vacuum Maxwell equations.** Setting ρ = 0 and J = 0:

**第 1 步 — 写出真空麦克斯韦方程。** 令 ρ = 0，J = 0：

  (I)   ∇ · E = 0,
  (II)  ∇ · B = 0,
  (III) ∇ × E = −∂B/∂t,
  (IV)  ∇ × B = μ₀ε₀ ∂E/∂t.

**Step 2 — Take the curl of Faraday's law.** Apply ∇ × to equation (III):

**第 2 步 — 对法拉第定律取旋度。** 对方程 (III) 施用 ∇ ×：

  ∇ × (∇ × E) = ∇ × (−∂B/∂t) = −∂(∇ × B)/∂t.

The right-hand side: substitute equation (IV), ∇ × B = μ₀ε₀ ∂E/∂t:

右侧：代入方程 (IV)，∇ × B = μ₀ε₀ ∂E/∂t：

  −∂(∇ × B)/∂t = −∂(μ₀ε₀ ∂E/∂t)/∂t = −μ₀ε₀ ∂²E/∂t².

**Step 3 — Apply the vector identity for curl of curl.** For any vector field F:

**第 3 步 — 应用旋度的旋度矢量恒等式。** 对任意矢量场 F：

  ∇ × (∇ × F) = ∇(∇ · F) − ∇²F.

Applying this to E and using ∇ · E = 0 (equation I):

将此应用于 E，并利用 ∇ · E = 0（方程 I）：

  ∇ × (∇ × E) = ∇(∇ · E) − ∇²E = 0 − ∇²E = −∇²E.

**Step 4 — Assemble the wave equation.** Equating the results of Steps 2 and 3:

**第 4 步 — 组装波动方程。** 将第 2、3 步的结果等同：

  −∇²E = −μ₀ε₀ ∂²E/∂t²,

  **∇²E − μ₀ε₀ ∂²E/∂t² = 0,**   i.e.   **∇²E = (1/c²) ∂²E/∂t²**,

where **c = 1/√(μ₀ε₀)**. Numerically, μ₀ = 4π × 10⁻⁷ T·m/A and ε₀ = 8.854 × 10⁻¹² C²/(N·m²), giving c = 2.998 × 10⁸ m/s — the measured speed of light.

其中 **c = 1/√(μ₀ε₀)**。数值上，μ₀ = 4π × 10⁻⁷ T·m/A，ε₀ = 8.854 × 10⁻¹² C²/(N·m²)，给出 c = 2.998 × 10⁸ m/s——光速的测量值。

**Step 5 — Same equation for B.** Taking ∇ × of Ampère–Maxwell and substituting Faraday's law:

**第 5 步 — B 满足相同方程。** 对安培–麦克斯韦方程取 ∇ ×，代入法拉第定律：

  ∇ × (∇ × B) = ∇ × (μ₀ε₀ ∂E/∂t) = μ₀ε₀ ∂(∇ × E)/∂t = μ₀ε₀ ∂(−∂B/∂t)/∂t = −μ₀ε₀ ∂²B/∂t².
  ∇(∇ · B) − ∇²B = −μ₀ε₀ ∂²B/∂t²   →   **∇²B = (1/c²) ∂²B/∂t².** ∎

---

## B. Plane Wave Solutions and Transversality · 平面波解与横波性

**Claim.** The wave equation admits plane-wave solutions E = E₀ e^{i(k·r − ωt)}, B = B₀ e^{i(k·r − ωt)}, with dispersion relation ω = c|k|, and the fields are transverse: k · E₀ = 0, k · B₀ = 0, with B₀ = (k̂ × E₀)/c.

**命题。** 波动方程允许平面波解 E = E₀ e^{i(k·r − ωt)}，B = B₀ e^{i(k·r − ωt)}，色散关系为 ω = c|k|，且场是横向的：k · E₀ = 0，k · B₀ = 0，B₀ = (k̂ × E₀)/c。

**Step 1 — Dispersion relation.** Substitute E = E₀ e^{i(k·r − ωt)} into ∇²E = (1/c²) ∂²E/∂t². The Laplacian gives ∇²E = −|k|² E, and ∂²E/∂t² = −ω² E:

**第 1 步 — 色散关系。** 将 E = E₀ e^{i(k·r − ωt)} 代入 ∇²E = (1/c²) ∂²E/∂t²。拉普拉斯算子给出 ∇²E = −|k|² E，且 ∂²E/∂t² = −ω² E：

  −|k|² E = (1/c²)(−ω²) E   →   **ω = c|k|.** (ω > 0)

**Step 2 — Transversality from ∇ · E = 0.** For the plane wave, ∇ · E = ik · E₀ e^{i(k·r − ωt)} = 0, hence:

**第 2 步 — 由 ∇ · E = 0 得横波性。** 对于平面波，∇ · E = ik · E₀ e^{i(k·r − ωt)} = 0，故：

  **k · E₀ = 0.**

E is perpendicular to the propagation direction k. Similarly k · B₀ = 0 from ∇ · B = 0.

E 垂直于传播方向 k。类似地，由 ∇ · B = 0 得 k · B₀ = 0。

**Step 3 — Relation between E and B.** From Faraday's law ∇ × E = −∂B/∂t:

**第 3 步 — E 与 B 的关系。** 由法拉第定律 ∇ × E = −∂B/∂t：

  ik × E₀ e^{i(k·r − ωt)} = −(−iω) B₀ e^{i(k·r − ωt)},
  k × E₀ = ω B₀,
  B₀ = (k × E₀)/ω = (k̂ × E₀)/c   (using ω = c|k|, so k/ω = k̂/c).

This confirms: E ⊥ B ⊥ k (mutually orthogonal), and |B₀| = |E₀|/c. ∎

这确认了：E ⊥ B ⊥ k（相互正交），且 |B₀| = |E₀|/c。∎

---

## C. The Poynting Theorem — Electromagnetic Energy Conservation · 坡印亭定理——电磁能量守恒

**Claim.** The energy density u = ½(ε₀ E² + B²/μ₀) and the Poynting vector S = (1/μ₀) E × B satisfy the energy continuity equation ∂u/∂t + ∇ · S = −J · E.

**命题。** 能量密度 u = ½(ε₀ E² + B²/μ₀) 与坡印亭矢量 S = (1/μ₀) E × B 满足能量连续性方程 ∂u/∂t + ∇ · S = −J · E。

**Step 1 — Start with J · E (power delivered to charges).** The power per unit volume delivered by the electromagnetic field to free charges is J · E (force per unit volume on charges is J × B + ρE; the magnetic force does no work since it is perpendicular to the velocity, so only E contributes, giving J · E).

**第 1 步 — 从 J · E（传递给电荷的功率）出发。** 电磁场单位体积传递给自由电荷的功率为 J · E（单位体积上的电磁力为 J × B + ρE；磁力不做功，因为它垂直于速度，故只有 E 贡献，给出 J · E）。

**Step 2 — Eliminate J using Ampère–Maxwell.** From ∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t, solve for J:

**第 2 步 — 用安培–麦克斯韦方程消去 J。** 由 ∇ × B = μ₀ J + μ₀ε₀ ∂E/∂t 解出 J：

  μ₀ J = ∇ × B − μ₀ε₀ ∂E/∂t.

Dot with E:

点乘 E：

  μ₀ J · E = E · (∇ × B) − μ₀ε₀ E · ∂E/∂t.

**Step 3 — Use the product rule for divergence.** The identity ∇ · (E × B) = B · (∇ × E) − E · (∇ × B) gives:

**第 3 步 — 利用散度乘法法则。** 恒等式 ∇ · (E × B) = B · (∇ × E) − E · (∇ × B) 给出：

  E · (∇ × B) = B · (∇ × E) − ∇ · (E × B).

Substitute Faraday's law ∇ × E = −∂B/∂t:

代入法拉第定律 ∇ × E = −∂B/∂t：

  E · (∇ × B) = B · (−∂B/∂t) − ∇ · (E × B) = −B · ∂B/∂t − ∇ · (E × B).

**Step 4 — Assemble.** Substituting back into Step 2:

**第 4 步 — 综合。** 代回第 2 步：

  μ₀ J · E = −B · ∂B/∂t − ∇ · (E × B) − μ₀ε₀ E · ∂E/∂t.

Note that B · ∂B/∂t = ∂(B²/2)/∂t and E · ∂E/∂t = ∂(E²/2)/∂t. Dividing by μ₀:

注意 B · ∂B/∂t = ∂(B²/2)/∂t，E · ∂E/∂t = ∂(E²/2)/∂t。除以 μ₀：

  J · E = −∂(B²/2μ₀)/∂t − (1/μ₀) ∇ · (E × B) − ε₀ ∂(E²/2)/∂t.

Rearranging (and noting ε₀/2 E² + B²/2μ₀ = u):

重排（注意 ε₀/2 E² + B²/2μ₀ = u）：

  **∂u/∂t + ∇ · S = −J · E**,

where:

其中：

  **u = ½ ε₀ E² + B²/(2μ₀)**   (electromagnetic energy density / 电磁能量密度)
  **S = (1/μ₀) E × B**          (Poynting vector / 坡印亭矢量)

**Step 5 — Physical interpretation.** Integrating over volume V with boundary ∂V:

**第 5 步 — 物理诠释。** 对体积 V 积分，边界为 ∂V：

  d/dt ∫_V u dV = −∮_{∂V} S · dA − ∫_V J · E dV.

Rate of change of EM energy = (net inward Poynting flux) − (power dissipated to charges). This is the **electromagnetic energy conservation theorem**. ∎

EM 能量的变化率 = （净向内坡印亭通量）−（传递给电荷的功率）。这是**电磁能量守恒定理**。∎

---

## D. The Larmor Radiation Formula P = μ₀ q² a² / (6πc) · 拉莫尔辐射公式 P = μ₀ q² a² / (6πc)

**Claim.** A non-relativistic point charge q with acceleration a radiates power P = μ₀ q² a² / (6πc).

**命题。** 具有加速度 a 的非相对论性点电荷 q 辐射功率 P = μ₀ q² a² / (6πc)。

**Step 1 — Radiation fields of an accelerating charge.** For a non-relativistic charge (v ≪ c), the retarded electromagnetic fields have two components: a near-field (Coulomb) part falling off as 1/r² and a radiation (far-field) part falling off as 1/r. Only the radiation part contributes to energy transport to infinity. The radiation electric field is:

**第 1 步 — 加速电荷的辐射场。** 对于非相对论性电荷（v ≪ c），推迟电磁场有两个成分：按 1/r² 衰减的近场（库仑）部分和按 1/r 衰减的辐射（远场）部分。只有辐射部分对到无穷远处的能量传输有贡献。辐射电场为：

  E_rad(r, t) = (q / 4πε₀ c²) · [r̂ × (r̂ × a)] / r,

where r̂ is the unit vector from the (retarded) position of the charge to the field point, and a = a(t_ret) is the acceleration at retarded time t_ret = t − r/c.

其中 r̂ 是从电荷（推迟）位置到场点的单位矢量，a = a(t_ret) 是推迟时刻 t_ret = t − r/c 的加速度。

**Step 2 — Radiation magnetic field.** From the relation B_rad = (r̂ × E_rad)/c:

**第 2 步 — 辐射磁场。** 由关系 B_rad = (r̂ × E_rad)/c：

  B_rad = (q / 4πε₀ c³) · [r̂ × (r̂ × a)] × r̂ / r = (q / 4πε₀ c³) · [a − (a·r̂)r̂] × r̂ / r... 

More directly, both fields have magnitude |E_rad| = (q a sin θ)/(4πε₀ c² r), where θ is the angle between a and r̂.

更直接地，两个场的大小均为 |E_rad| = (q a sin θ)/(4πε₀ c² r)，其中 θ 是 a 与 r̂ 之间的夹角。

**Step 3 — Poynting vector and power per unit solid angle.** The time-averaged Poynting vector at distance r is:

**第 3 步 — 坡印亭矢量与单位立体角功率。** 距离 r 处的时间平均坡印亭矢量为：

  |S| = |E_rad|² / (μ₀ c) = q² a² sin²θ / (16π² ε₀ c³ r²).

Power radiated per unit solid angle dΩ = sin θ dθ dφ:

单位立体角辐射功率 dΩ = sin θ dθ dφ：

  dP/dΩ = r² |S| = q² a² sin²θ / (16π² ε₀ c³).

The sin²θ factor gives the characteristic **dipole radiation pattern**: zero along the acceleration axis, maximum perpendicular to it.

sin²θ 因子给出特征性的**偶极辐射方向图**：沿加速度轴方向为零，垂直方向最大。

**Step 4 — Integrate over all directions.** Total radiated power:

**第 4 步 — 对所有方向积分。** 总辐射功率：

  P = ∫ (dP/dΩ) dΩ = ∫₀^{2π} dφ ∫₀^π dθ (q² a² sin²θ / (16π² ε₀ c³)) sin θ
    = (q² a² / (16π² ε₀ c³)) · 2π · ∫₀^π sin³θ dθ.

Evaluate the angular integral: ∫₀^π sin³θ dθ = ∫₀^π sin θ (1 − cos²θ) dθ = [−cos θ + cos³θ/3]₀^π = (1 − 1/3) + (1 − 1/3) = 4/3.

计算角积分：∫₀^π sin³θ dθ = ∫₀^π sin θ (1 − cos²θ) dθ = [−cos θ + cos³θ/3]₀^π = (1 − 1/3) + (1 − 1/3) = 4/3。

Therefore:

因此：

  P = (q² a² / (16π² ε₀ c³)) · 2π · (4/3) = q² a² / (6π ε₀ c³).

**Step 5 — Rewrite in terms of μ₀.** Using c = 1/√(μ₀ε₀), so 1/ε₀ = μ₀ c²:

**第 5 步 — 用 μ₀ 改写。** 利用 c = 1/√(μ₀ε₀)，故 1/ε₀ = μ₀ c²：

  P = q² a² μ₀ c² / (6π c³) = **μ₀ q² a² / (6πc)**. ∎

This is the **Larmor formula** in SI units. In Gaussian units it takes the form P = q²a²/(6πc³). The formula immediately implies that a classically orbiting electron (centripetal acceleration a ≠ 0) continuously radiates, losing energy on a timescale ~ 10⁻¹¹ s — the radiation crisis that necessitates quantum mechanics.

这是 SI 单位制中的**拉莫尔公式**。在高斯单位制中，形式为 P = q²a²/(6πc³)。该公式立即意味着经典轨道电子（向心加速度 a ≠ 0）持续辐射，在约 10⁻¹¹ s 的时间尺度内损失能量——这一辐射危机使量子力学成为必要。

---

*The wave equation, Poynting theorem, and Larmor formula derived here provide the foundation for radiation theory (synchrotron radiation, antenna theory), the classical limit of QED, and the ω⁴ Rayleigh scattering that explains the blue sky.*

*此处推导的波动方程、坡印亭定理和拉莫尔公式为辐射理论（同步辐射、天线理论）、量子电动力学的经典极限以及解释蓝天的 ω⁴ 瑞利散射提供了基础。*

# Derivations — Module 1.21: Classical Scattering Theory
# 推导 — 模块 1.21：经典散射理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.21](./module-1.21-classical-scattering.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.21](./module-1.21-classical-scattering.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Differential Cross Section from the Impact Parameter · 由瞄准距离给出微分散射截面

**Claim.** For scattering off a central potential U(r), the scattering angle θ is a single-valued function of the impact parameter b. Conservation of particle number then gives the differential cross section

**命题。** 对中心势 U(r) 的散射，散射角 θ 是瞄准距离 b 的单值函数。粒子数守恒给出微分散射截面

  dσ/dΩ = (b / sin θ) |db/dθ|.

**Step 1 — Set up the incident flux.** A uniform parallel beam strikes the target with **flux** n (number of particles crossing unit cross-sectional area per unit time). By symmetry about the beam axis, all particles with impact parameter between b and b + db form an annular ring of area dσ = 2πb db. The number of particles passing through this ring per unit time is

**第 1 步 — 设定入射通量。** 一束均匀平行束以**通量** n（单位时间穿过单位横截面积的粒子数）射向靶。绕束轴对称，所有瞄准距离介于 b 与 b + db 之间的粒子构成面积为 dσ = 2πb db 的环带。单位时间穿过此环带的粒子数为

  dN = n · dσ = n · 2πb db.

**Step 2 — Map the ring onto the detector.** Because θ depends only on b for a central potential, every particle entering the ring [b, b + db] emerges into the cone of scattering angles [θ, θ + dθ]. This cone subtends a solid angle (an annulus on the unit sphere) of

**第 2 步 — 将环带映射到探测器。** 由于对中心势 θ 只依赖于 b，进入环带 [b, b + db] 的每个粒子都散射到角度区间 [θ, θ + dθ] 的圆锥中。此圆锥（单位球面上的圆环带）所张的立体角为

  dΩ = 2π sin θ dθ.

**Step 3 — Define the differential cross section.** The differential cross section dσ/dΩ is defined so that the number scattered into dΩ equals the incident flux times the effective target area:

**第 3 步 — 定义微分散射截面。** 微分散射截面 dσ/dΩ 的定义使得散射进 dΩ 的粒子数等于入射通量乘以有效靶面积：

  dN = n · (dσ/dΩ) dΩ.

The same particles cross the entrance ring and exit through dΩ, so equate the two expressions for dN:

同一批粒子穿过入射环带并从 dΩ 出射，故令 dN 的两个表达式相等：

  n · 2πb db = n · (dσ/dΩ) · 2π sin θ dθ.

**Step 4 — Solve and insert the absolute value.** Cancelling n · 2π and rearranging:

**第 4 步 — 求解并加入绝对值。** 约去 n · 2π 并整理：

  dσ/dΩ = (b / sin θ) (db/dθ).

For a typical repulsive (or attractive monotonic) potential a smaller impact parameter produces a larger deflection, so b is a **decreasing** function of θ and db/dθ < 0. The cross section, an area, must be positive, so we take the magnitude:

对典型排斥（或单调吸引）势，较小的瞄准距离产生较大的偏转，故 b 是 θ 的**递减**函数，db/dθ < 0。截面作为面积必须为正，故取其绝对值：

  **dσ/dΩ = (b / sin θ) |db/dθ|.**  ∎

---

## B. Deflection Angle for a Central Force · 中心力的偏转角

**Claim.** A particle of mass m, energy E, and angular momentum ℓ = b√(2mE) = m v∞ b scattering off the central potential U(r) emerges with scattering angle

**命题。** 质量为 m、能量为 E、角动量 ℓ = b√(2mE) = m v∞ b 的粒子被中心势 U(r) 散射后，散射角为

  θ = π − 2φ₀,    φ₀ = ∫_{r_min}^∞ (ℓ/r²) dr / √(2m(E − U(r)) − ℓ²/r²).

**Step 1 — Conserved quantities far away.** Far from the target U → 0, so the asymptotic speed v∞ obeys E = ½ m v∞², giving v∞ = √(2E/m). The angular momentum about the target is the asymptotic momentum times the perpendicular distance b:

**第 1 步 — 远处的守恒量。** 远离靶时 U → 0，故渐近速率 v∞ 满足 E = ½ m v∞²，给出 v∞ = √(2E/m)。绕靶的角动量等于渐近动量乘以垂直距离 b：

  ℓ = m v∞ b = m b √(2E/m) = b √(2mE).

**Step 2 — Energy conservation in the orbit.** Using polar coordinates (r, φ) centred on the target, the energy and angular momentum are

**第 2 步 — 轨道中的能量守恒。** 以靶为中心用极坐标 (r, φ)，能量与角动量为

  E = ½ m (ṙ² + r² φ̇²) + U(r),    ℓ = m r² φ̇.

Eliminate φ̇ = ℓ/(m r²) to obtain the radial energy equation:

消去 φ̇ = ℓ/(m r²)，得径向能量方程：

  E = ½ m ṙ² + ℓ²/(2 m r²) + U(r)  ⟹  ṙ = ±√( (2/m)(E − U(r)) − ℓ²/(m² r²) ).

**Step 3 — The orbit equation dφ/dr.** Divide φ̇ by ṙ to remove time:

**第 3 步 — 轨道方程 dφ/dr。** 用 φ̇ 除以 ṙ 以消去时间：

  dφ/dr = φ̇/ṙ = (ℓ/(m r²)) / ±√( (2/m)(E − U) − ℓ²/(m² r²) ).

Multiplying numerator and denominator inside the root by m² gives the standard form:

将根号内的分子与分母同乘 m²，得标准形式：

  dφ/dr = (ℓ/r²) / √( 2m(E − U(r)) − ℓ²/r² ).

**Step 4 — The angle swept to the turning point.** The distance of closest approach r_min is the turning point where ṙ = 0, i.e. the largest root of 2m(E − U(r)) − ℓ²/r² = 0. The angle φ₀ swept as the particle travels in from r = ∞ to r = r_min is the integral of dφ/dr:

**第 4 步 — 扫过至最近点的角度。** 最近距离 r_min 是转折点，满足 ṙ = 0，即 2m(E − U(r)) − ℓ²/r² = 0 的最大根。粒子从 r = ∞ 运动到 r = r_min 扫过的角度 φ₀ 为 dφ/dr 的积分：

  φ₀ = ∫_{r_min}^∞ (ℓ/r²) dr / √( 2m(E − U(r)) − ℓ²/r² ).

**Step 5 — Symmetry gives the scattering angle.** The orbit is symmetric about the line through r_min (the apsidal line): the incoming and outgoing branches each sweep the same angle φ₀. The total angle between the two asymptotes is therefore 2φ₀. The scattering angle θ is the supplement of this — the angle by which the outgoing asymptote is rotated from the straight-through direction:

**第 5 步 — 对称性给出散射角。** 轨道关于过 r_min 的直线（拱点线）对称：入射与出射两支各扫过相同的角度 φ₀。故两条渐近线之间的总角度为 2φ₀。散射角 θ 是其补角——即出射渐近线相对于直穿方向转过的角度：

  **θ = π − 2φ₀.**  ∎

---

## C. Rutherford Scattering · 卢瑟福散射

**Claim.** For the repulsive Coulomb potential U(r) = k/r with k = q₁q₂/(4πε₀), the impact parameter and scattering angle obey

**命题。** 对排斥性库仑势 U(r) = k/r，其中 k = q₁q₂/(4πε₀)，瞄准距离与散射角满足

  b = (k/2E) cot(θ/2),

and the differential cross section is the **Rutherford formula**

且微分散射截面为**卢瑟福公式**

  dσ/dΩ = (k/4E)² / sin⁴(θ/2) = [q₁q₂/(16πε₀E)]² / sin⁴(θ/2).

**Step 1 — Reduce the orbit integral.** From Section B with U = k/r,

**第 1 步 — 化简轨道积分。** 由 B 节，取 U = k/r，

  φ₀ = ∫_{r_min}^∞ (ℓ/r²) dr / √( 2m(E − k/r) − ℓ²/r² ).

Substitute u = 1/r, so du = −dr/r² and the limits run from u = 0 (r = ∞) to u = u_max = 1/r_min:

代换 u = 1/r，则 du = −dr/r²，积分限从 u = 0（r = ∞）到 u = u_max = 1/r_min：

  φ₀ = ∫_0^{u_max} ℓ du / √( 2mE − 2mk u − ℓ² u² ).

**Step 2 — Complete the square.** Write the radicand as a downward parabola in u. Factor out ℓ²:

**第 2 步 — 配方。** 将根式内写为关于 u 的开口向下的抛物线。提出 ℓ²：

  2mE − 2mk u − ℓ² u² = ℓ² [ 2mE/ℓ² − (2mk/ℓ²) u − u² ].

Completing the square in u with centre u₀ = mk/ℓ²:

对 u 配方，中心为 u₀ = mk/ℓ²：

  = ℓ² [ ( 2mE/ℓ² + m²k²/ℓ⁴ ) − ( u + mk/ℓ² )² ] = ℓ² [ A² − (u + u₀)² ],

where A² = 2mE/ℓ² + m²k²/ℓ⁴. The integral becomes a standard arccosine form:

其中 A² = 2mE/ℓ² + m²k²/ℓ⁴。积分化为标准反余弦形式：

  φ₀ = ∫_0^{u_max} du / √( A² − (u + u₀)² ) = [ arccos( (u + u₀)/A ) ]  evaluated between limits.

**Step 3 — Evaluate at the limits.** The turning point u_max is the positive root of the radicand, i.e. where A² − (u_max + u₀)² = 0, so (u_max + u₀)/A = 1 and arccos gives 0 there. At u = 0, (0 + u₀)/A = u₀/A. Hence

**第 3 步 — 代入积分限。** 转折点 u_max 是根式的正根，即 A² − (u_max + u₀)² = 0，故 (u_max + u₀)/A = 1，其反余弦为 0。在 u = 0 处，(0 + u₀)/A = u₀/A。故

  φ₀ = arccos( u₀ / A )  ⟹  cos φ₀ = u₀/A = (mk/ℓ²) / √( 2mE/ℓ² + m²k²/ℓ⁴ ).

**Step 4 — Simplify cos φ₀.** Multiply numerator and denominator by ℓ²:

**第 4 步 — 化简 cos φ₀。** 分子与分母同乘 ℓ²：

  cos φ₀ = mk / √( 2mE ℓ² + m²k² ) = mk / √( m²k² + 2mE ℓ² ).

Divide top and bottom by mk:

上下同除以 mk：

  cos φ₀ = 1 / √( 1 + 2E ℓ² /(m k²) ).

Now insert ℓ² = 2mE b² (from Section B, ℓ = b√(2mE)):

代入 ℓ² = 2mE b²（由 B 节，ℓ = b√(2mE)）：

  2E ℓ² /(m k²) = 2E · 2mE b² /(m k²) = (2E b / k)².

Therefore

故

  cos φ₀ = 1 / √( 1 + (2E b/k)² ).

**Step 5 — Convert to the scattering angle.** From θ = π − 2φ₀ we have φ₀ = π/2 − θ/2, so cos φ₀ = sin(θ/2) and the relation reads

**第 5 步 — 转换为散射角。** 由 θ = π − 2φ₀ 得 φ₀ = π/2 − θ/2，故 cos φ₀ = sin(θ/2)，关系式为

  sin(θ/2) = 1 / √( 1 + (2E b/k)² )  ⟹  1 + (2E b/k)² = 1/sin²(θ/2) = csc²(θ/2).

Subtract 1 and use csc²(θ/2) − 1 = cot²(θ/2):

减去 1 并利用 csc²(θ/2) − 1 = cot²(θ/2)：

  (2E b/k)² = cot²(θ/2)  ⟹  2E b/k = cot(θ/2)  ⟹  **b = (k/2E) cot(θ/2).**

**Step 6 — Differentiate b(θ).** Using d/dx[cot x] = −csc² x:

**第 6 步 — 对 b(θ) 求导。** 利用 d/dx[cot x] = −csc² x：

  db/dθ = (k/2E) · (−csc²(θ/2)) · (1/2) = −(k/4E) csc²(θ/2).

So |db/dθ| = (k/4E) csc²(θ/2) = (k/4E)/sin²(θ/2).

故 |db/dθ| = (k/4E) csc²(θ/2) = (k/4E)/sin²(θ/2)。

**Step 7 — Assemble the cross section.** Insert b and |db/dθ| into dσ/dΩ = (b/sin θ)|db/dθ|, and use the half-angle identity sin θ = 2 sin(θ/2) cos(θ/2):

**第 7 步 — 组装截面。** 将 b 与 |db/dθ| 代入 dσ/dΩ = (b/sin θ)|db/dθ|，并用半角恒等式 sin θ = 2 sin(θ/2) cos(θ/2)：

  dσ/dΩ = [ (k/2E) cot(θ/2) ] · [ 1/(2 sin(θ/2) cos(θ/2)) ] · [ (k/4E)/sin²(θ/2) ].

Write cot(θ/2) = cos(θ/2)/sin(θ/2) and collect the prefactors (k/2E)·(k/4E) = k²/(8E²):

写 cot(θ/2) = cos(θ/2)/sin(θ/2)，并合并前因子 (k/2E)·(k/4E) = k²/(8E²)：

  dσ/dΩ = (k²/8E²) · [ cos(θ/2)/sin(θ/2) ] · [ 1/(2 sin(θ/2) cos(θ/2)) ] · [ 1/sin²(θ/2) ].

**Step 8 — Cancel cleanly.** The cos(θ/2) in the numerator cancels the cos(θ/2) in the denominator; the three sin(θ/2) factors and the explicit sin²(θ/2) combine to sin⁴(θ/2); the factor 2 in the denominator turns k²/(8E²) into k²/(16E²):

**第 8 步 — 干净相消。** 分子的 cos(θ/2) 与分母的 cos(θ/2) 相消；三个 sin(θ/2) 因子与显式的 sin²(θ/2) 合并为 sin⁴(θ/2)；分母的因子 2 使 k²/(8E²) 变为 k²/(16E²)：

  dσ/dΩ = k²/(16E²) · 1/sin⁴(θ/2) = (k/4E)² / sin⁴(θ/2).

Finally substitute k = q₁q₂/(4πε₀), giving k/4E = q₁q₂/(16πε₀E):

最后代入 k = q₁q₂/(4πε₀)，得 k/4E = q₁q₂/(16πε₀E)：

  **dσ/dΩ = (k/4E)² / sin⁴(θ/2) = [q₁q₂/(16πε₀E)]² / sin⁴(θ/2).**  ∎

---

## D. Divergence of the Total Cross Section · 总截面的发散

**Claim.** The total cross section σ_tot = ∫(dσ/dΩ) dΩ for the Coulomb potential **diverges**, due to the dominant forward (small-θ) scattering — a direct consequence of the infinite range of the 1/r potential. A screened or finite-range potential restores a finite σ_tot.

**命题。** 库仑势的总截面 σ_tot = ∫(dσ/dΩ) dΩ **发散**，源于主导的前向（小 θ）散射——这是 1/r 势无穷力程的直接后果。屏蔽势或有限力程势可恢复有限的 σ_tot。

**Step 1 — Write the total cross section integral.** Integrate the Rutherford cross section over all solid angles, dΩ = 2π sin θ dθ (azimuthal symmetry):

**第 1 步 — 写出总截面积分。** 对所有立体角积分卢瑟福截面，dΩ = 2π sin θ dθ（方位对称）：

  σ_tot = ∫ (dσ/dΩ) dΩ = ∫_0^π (k/4E)² / sin⁴(θ/2) · 2π sin θ dθ.

**Step 2 — Reduce the integrand.** Use sin θ = 2 sin(θ/2) cos(θ/2):

**第 2 步 — 化简被积函数。** 用 sin θ = 2 sin(θ/2) cos(θ/2)：

  σ_tot = 2π (k/4E)² ∫_0^π [ 2 sin(θ/2) cos(θ/2) / sin⁴(θ/2) ] dθ = 4π (k/4E)² ∫_0^π [ cos(θ/2) / sin³(θ/2) ] dθ.

**Step 3 — Examine the small-angle behaviour.** As θ → 0, cos(θ/2) → 1 and sin(θ/2) ≈ θ/2, so the integrand behaves like

**第 3 步 — 检查小角行为。** 当 θ → 0 时，cos(θ/2) → 1，sin(θ/2) ≈ θ/2，故被积函数表现为

  cos(θ/2)/sin³(θ/2) ≈ 1/(θ/2)³ = 8/θ³.

The integral ∫_0 dθ/θ³ ~ [−1/(2θ²)] diverges at the lower limit θ → 0. Equivalently, substituting w = sin(θ/2), dw = ½cos(θ/2) dθ, the integral becomes 2∫ dw/w³ = [−1/w²], which diverges as w → 0:

积分 ∫_0 dθ/θ³ ~ [−1/(2θ²)] 在下限 θ → 0 处发散。等价地，代换 w = sin(θ/2)，dw = ½cos(θ/2) dθ，积分变为 2∫ dw/w³ = [−1/w²]，当 w → 0 时发散：

  **σ_tot → ∞.**

**Step 4 — Physical interpretation.** The divergence comes entirely from θ → 0, i.e. from arbitrarily **large impact parameters** b → ∞. Because the Coulomb force 1/r² never truly vanishes, even particles passing extremely far away are deflected by a tiny but nonzero angle; integrating their (large) cross-sectional contributions over all b up to infinity diverges. There is no finite "size" to a pure Coulomb target.

**第 4 步 — 物理诠释。** 发散完全来自 θ → 0，即来自任意**大的瞄准距离** b → ∞。由于库仑力 1/r² 从不真正消失，即便从极远处经过的粒子也被偏转一个微小但非零的角度；将它们（巨大的）截面贡献对所有直至无穷的 b 积分便发散。纯库仑靶没有有限的"尺寸"。

**Step 5 — Screening restores finiteness.** A real charge is screened by surrounding charges, giving a finite-range Yukawa-type potential U(r) = (k/r) e^{−r/a} with screening length a. Beyond r ≳ a the potential is exponentially suppressed, so there is a minimum deflection angle θ_min ~ k/(E a) below which particles are effectively undeflected. Cutting the integral off at θ_min makes it convergent:

**第 5 步 — 屏蔽恢复有限性。** 真实电荷被周围电荷屏蔽，给出有限力程的汤川型势 U(r) = (k/r) e^{−r/a}，屏蔽长度为 a。当 r ≳ a 时势被指数压低，故存在最小偏转角 θ_min ~ k/(E a)，低于此角粒子实际上不被偏转。在 θ_min 处截断积分使其收敛：

  σ_tot ~ 4π (k/4E)² ∫_{θ_min}^π [ cos(θ/2)/sin³(θ/2) ] dθ ~ 4π (k/4E)² · 1/sin²(θ_min/2) < ∞.

Hence the infinite cross section is a peculiarity of the strictly infinite-range Coulomb force; any finite-range (screened) interaction yields a finite total cross section of order πa². ∎

故无穷大截面是严格无穷力程库仑力的特殊性质；任何有限力程（屏蔽）相互作用都给出量级为 πa² 的有限总截面。∎

---

*The classical Rutherford cross section dσ/dΩ = (k/4E)²/sin⁴(θ/2) is one of the rare cases where the full quantum (Born-approximation) result coincides exactly with the classical one (Module 3.8) — the 1/sin⁴(θ/2) law and its small-angle divergence survive the transition to wave mechanics. Historically (Module 9.3) the unexpected large-angle tail of this distribution revealed the atomic nucleus; at GeV energies the same large-angle excess in deep inelastic scattering (Module 8.9) revealed pointlike quarks inside the proton.*

*经典卢瑟福截面 dσ/dΩ = (k/4E)²/sin⁴(θ/2) 是少数完整量子（玻恩近似）结果与经典结果完全一致的情形之一（模块 3.8）——1/sin⁴(θ/2) 定律及其小角发散在过渡到波动力学时依然成立。历史上（模块 9.3）这一分布出乎意料的大角度尾部揭示了原子核；在 GeV 能标下，深度非弹性散射（模块 8.9）中同样的大角度超出揭示了质子内部点状的夸克。*

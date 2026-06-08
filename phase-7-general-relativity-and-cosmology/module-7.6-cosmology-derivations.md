# Derivations — Module 7.6: Cosmology
# 推导 — 模块 7.6：宇宙学

> Companion to [Module 7.6](./module-7.6-cosmology.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.6](./module-7.6-cosmology.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Friedmann Equations from the Einstein Field Equations Applied to the FLRW Metric · 将爱因斯坦场方程应用于 FLRW 度规推导弗里德曼方程

**Claim.** Inserting the FLRW metric ds² = −c² dt² + a²(t)[dr²/(1−kr²) + r² dΩ²] and a perfect-fluid stress-energy tensor T_{μν} (with energy density ρ and pressure p) into the EFE G_{μν} = (8πG/c⁴) T_{μν} yields the two Friedmann equations:

  (ȧ/a)² = (8πG/3)ρ − kc²/a² + Λc²/3   (First Friedmann equation)
  ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3   (Acceleration equation / Second Friedmann equation)

**命题。** 将 FLRW 度规 ds² = −c² dt² + a²(t)[dr²/(1−kr²) + r² dΩ²] 和完美流体能动张量 T_{μν}（能量密度 ρ，压强 p）代入 EFE G_{μν} = (8πG/c⁴) T_{μν}，得到两个弗里德曼方程：

  (ȧ/a)² = (8πG/3)ρ − kc²/a² + Λc²/3   （第一弗里德曼方程）
  ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3   （加速方程/第二弗里德曼方程）

**Step 1 — Write down the FLRW metric components.** For the flat case (k = 0) for clarity, then generalize. The metric is diagonal:

**第 1 步 — 写出 FLRW 度规分量。** 为清晰起见先讨论平坦情形（k = 0），后推广。度规是对角的：

  g_{00} = −c²,   g_{11} = a²/(1−kr²),   g_{22} = a²r²,   g_{33} = a²r² sin²θ.

The inverse metric: g^{00} = −1/c², g^{11} = (1−kr²)/a², g^{22} = 1/(a²r²), g^{33} = 1/(a²r²sin²θ).

逆度规：g^{00} = −1/c²，g^{11} = (1−kr²)/a²，g^{22} = 1/(a²r²)，g^{33} = 1/(a²r²sin²θ)。

**Step 2 — Compute non-zero Christoffel symbols.** The only non-vanishing independent Christoffel symbols of the FLRW metric (denoting a dot for d/dt and using x^0 = ct):

**第 2 步 — 计算非零克里斯托费尔符号。** FLRW 度规唯一非零的独立克里斯托费尔符号（用点号表示 d/dt，并使用 x^0 = ct）：

  Γ^0_{ij} = (aȧ/c) g̃_{ij},   where g̃_{ij} is the spatial part metric,

  Γ^i_{0j} = (ȧ/a) δ^i_j / c,

  Γ^i_{jk} = ∂ terms from the spatial metric.

More explicitly (with Latin indices i,j running over spatial components, and spatial metric g̃_{ij} = a² γ_{ij} where γ_{ij} is the unit-curvature metric):

更明确地（拉丁指标 i,j 遍历空间分量，空间度规 g̃_{ij} = a² γ_{ij}，其中 γ_{ij} 是单位曲率度规）：

  Γ^0_{ij} = (aȧ/c) γ_{ij},   Γ^i_{0j} = (ȧ/(ac)) δ^i_j,

  Γ^1_{11} = kr/(1−kr²),   Γ^2_{12} = Γ^3_{13} = 1/r, etc. (spatial Christoffel symbols)

**Step 3 — Compute the Ricci tensor components.** By the high symmetry of the FLRW metric (homogeneous and isotropic), the only independent non-vanishing Ricci tensor components are R_{00} and R_{ij} = f(t) g̃_{ij}. Compute R_{00}:

**第 3 步 — 计算里奇张量分量。** 由于 FLRW 度规的高度对称性（均匀且各向同性），唯一独立的非零里奇张量分量为 R_{00} 和 R_{ij} = f(t) g̃_{ij}。计算 R_{00}：

  R_{00} = ∂_μ Γ^μ_{00} − ∂_0 Γ^μ_{μ0} + Γ^μ_{μλ} Γ^λ_{00} − Γ^μ_{0λ} Γ^λ_{μ0}.

Since the metric is diagonal and static in form (only time-varying through a(t)), Γ^μ_{00} = 0 for all μ. The dominant contribution is from the second term:

由于度规是对角的，Γ^μ_{00} = 0（对所有 μ）。主导贡献来自第二项：

  R_{00} = −∂_0 Γ^i_{i0} − (Γ^i_{0j})² · (\text{contracted})

Carefully, using x^0 = ct so ∂_0 = (1/c) d/dt:

仔细地，利用 x^0 = ct 故 ∂_0 = (1/c) d/dt：

  Γ^i_{0i} = 3ȧ/(ac),  ∂_0 Γ^i_{0i} = (1/c) d/dt (3ȧ/(ac)) = (3/c)(ä/(ac) − ȧ²/(a²c)) = 3ä/(ac²) − 3ȧ²/(a²c²).

  Γ^i_{0j} Γ^j_{i0} = 3(ȧ/(ac))² = 3ȧ²/(a²c²).

Therefore:

因此：

  R_{00} = −[3ä/(ac²) − 3ȧ²/(a²c²)] − 3ȧ²/(a²c²) = −3ä/(ac²).

For the spatial components R_{ij} we need the remaining Christoffel symbols. With x^0 = ct (so ∂_0 = (1/c)∂_t) and g_{ij} = a²(t)γ_{ij}, where γ_{ij} is the unit-curvature spatial metric:

对于空间分量 R_{ij}，我们需要其余的克里斯托费尔符号。取 x^0 = ct（故 ∂_0 = (1/c)∂_t）且 g_{ij} = a²(t)γ_{ij}，其中 γ_{ij} 为单位曲率空间度规：

  Γ^0_{ij} = (aȧ/c) γ_{ij},   Γ^i_{0j} = (ȧ/(ac)) δ^i_j,

and the purely spatial Christoffels Γ^k_{ij}[γ] are those of γ_{ij}, whose intrinsic Ricci tensor is R̃_{ij} = 2k γ_{ij} (a maximally symmetric 3-space of curvature k). Substituting into

而纯空间克里斯托费尔符号 Γ^k_{ij}[γ] 即 γ_{ij} 的克里斯托费尔符号，其内禀里奇张量为 R̃_{ij} = 2k γ_{ij}（曲率为 k 的极大对称三维空间）。代入

  R_{ij} = ∂_μ Γ^μ_{ij} − ∂_j Γ^μ_{iμ} + Γ^μ_{μλ} Γ^λ_{ij} − Γ^μ_{jλ} Γ^λ_{iμ}

and collecting the time-derivative and connection terms together with R̃_{ij} = 2k γ_{ij} gives the standard FLRW spatial Ricci tensor:

并将时间导数项、联络项与 R̃_{ij} = 2k γ_{ij} 合并，得到标准 FLRW 空间里奇张量：

  R_{ij} = [aä + 2ȧ² + 2kc²] γ_{ij}/c²,

with R_{00} = −3ä/(ac²) from above (g_{ij} = a² γ_{ij}).

其中 R_{00} = −3ä/(ac²) 由上文给出（g_{ij} = a² γ_{ij}）。

**Step 4 — Compute the Ricci scalar.** Contract with the inverse metric:

**第 4 步 — 计算里奇标量。** 与逆度规缩并：

With x^0 = ct the metric is g_{00} = −1 (so g^{00} = −1) and g^{ij} = γ^{ij}/a²:

取 x^0 = ct 时度规为 g_{00} = −1（故 g^{00} = −1），g^{ij} = γ^{ij}/a²：

  R = g^{00} R_{00} + g^{ij} R_{ij}
    = (−1)(−3ä/(ac²)) + (γ^{ij}/a²) · [aä + 2ȧ² + 2kc²] γ_{ij}/c²
    = 3ä/(ac²) + 3[aä + 2ȧ² + 2kc²]/(a²c²)
    = 3ä/(ac²) + 3ä/(ac²) + 6ȧ²/(a²c²) + 6k/a²
    = (6/c²)[ä/a + (ȧ/a)² + kc²/a²].

So R = 6[ä/a + (ȧ/a)² + kc²/a²]/c².

故 R = 6[ä/a + (ȧ/a)² + kc²/a²]/c²。

**Step 5 — Compute the Einstein tensor.** The algebra is cleanest in units c = 1 (we restore c in the final Friedmann equations by dimensional analysis). Setting c = 1 temporarily:

**第 5 步 — 计算爱因斯坦张量。** 在 c = 1 单位下代数最简洁（最后通过量纲分析在弗里德曼方程中恢复 c）。暂时令 c = 1：

  g_{00} = −1, g_{ij} = a² γ_{ij}.
  R_{00} = −3ä/a,  R_{ij} = (aä + 2ȧ² + 2k) γ_{ij}.
  R = 6(ä/a + (ȧ/a)² + k/a²).
  G_{00} = R_{00} − ½ g_{00} R = −3ä/a − ½(−1)(6(ä/a + ȧ²/a² + k/a²))
         = −3ä/a + 3(ä/a + ȧ²/a² + k/a²)
         = 3(ȧ²/a² + k/a²) = 3[(ȧ/a)² + k/a²].

For the spatial components:

对于空间分量：

  G_{ij} = R_{ij} − ½ g_{ij} R
         = (aä + 2ȧ² + 2k) γ_{ij} − ½ a² γ_{ij} · 6(ä/a + ȧ²/a² + k/a²)
         = γ_{ij} [(aä + 2ȧ² + 2k) − 3a²(ä/a + ȧ²/a² + k/a²)]
         = γ_{ij} [aä + 2ȧ² + 2k − 3aä − 3ȧ² − 3k]
         = γ_{ij} [−2aä − ȧ² − k].

**Step 6 — Perfect fluid stress-energy tensor.** For a comoving perfect fluid with 4-velocity u^μ = (1, 0, 0, 0) (in the cosmic rest frame, x^0 = t, c = 1):

**第 6 步 — 完美流体能动张量。** 对于共动完美流体，四速度 u^μ = (1, 0, 0, 0)（在宇宙静止系中，x^0 = t，c = 1）：

  T_{μν} = (ρ + p) u_μ u_ν + p g_{μν}.
  T_{00} = (ρ + p)(−1)² + p(−1) = ρ + p − p = ρ.
  T_{ij} = p g_{ij} = p a² γ_{ij}.

**Step 7 — First Friedmann equation (00-component of EFE).** G_{00} = 8πG T_{00} (in c = 1 units with κ = 8πG):

**第 7 步 — 第一弗里德曼方程（EFE 的 00 分量）。** G_{00} = 8πG T_{00}（c = 1 单位，κ = 8πG）：

  3[(ȧ/a)² + k/a²] = 8πGρ.

Restoring c (via k → kc², Λ → Λc², and recalling that in SI units G_{00} = (8πG/c⁴) T_{00} with T_{00} = ρc²):

恢复 c（通过 k → kc²，Λ → Λc²，并注意在国际单位制中 G_{00} = (8πG/c⁴) T_{00}，T_{00} = ρc²）：

  **(ȧ/a)² = (8πG/3)ρ − kc²/a² + Λc²/3.** ∎

**Step 8 — Second Friedmann equation (spatial components of EFE).** The ij-component of G_{μν} = 8πG T_{μν} (c = 1):

**第 8 步 — 第二弗里德曼方程（EFE 的空间分量）。** G_{μν} = 8πG T_{μν} 的 ij 分量（c = 1）：

  γ_{ij}(−2aä − ȧ² − k) = 8πG · p a² γ_{ij}.

Divide through by −a² γ_{ij}:

两边除以 −a² γ_{ij}：

  2ä/a + (ȧ/a)² + k/a² = −8πGp.

Subtract the first Friedmann equation (ȧ/a)² + k/a² = 8πGρ/3 from this (multiplied appropriately):

从此式减去第一弗里德曼方程（适当地）：

Using the first equation: (ȧ/a)² + k/a² = 8πGρ/3. Substituting:

利用第一方程 (ȧ/a)² + k/a² = 8πGρ/3，代入：

  2ä/a + 8πGρ/3 = −8πGp
  ä/a = −8πGp/2 − 4πGρ/3 = −4πG(p + ρ/3)... 

Let us redo: 2ä/a = −8πGp − (ȧ/a)² − k/a² = −8πGp − 8πGρ/3 (using first equation):

重新推导：2ä/a = −8πGp − (ȧ/a)² − k/a² = −8πGp − 8πGρ/3（利用第一方程）：

  2ä/a = −8πG(p + ρ/3)
  ä/a = −4πG(ρ + 3p)/3.

Restoring c factors (p → p/c², Λ contribution from the Λ g_{μν} term):

恢复 c 因子（p → p/c²，Λ 贡献来自 Λ g_{μν} 项）：

  **ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3.** ∎

---

## B. Fluid Equation and Density Scaling · 流体方程与密度标度关系

**Claim.** From the covariant conservation law ∇^μ T_{μν} = 0 applied to a comoving perfect fluid in FLRW spacetime, the continuity equation

  ρ̇ + 3(ȧ/a)(ρ + p/c²) = 0

follows, giving: ρ ∝ a^{−3} for pressureless matter (p = 0), ρ ∝ a^{−4} for radiation (p = ρc²/3), and ρ = const for a cosmological constant (p = −ρc²).

**命题。** 由协变守恒律 ∇^μ T_{μν} = 0 应用于 FLRW 时空中的共动完美流体，得到连续性方程

  ρ̇ + 3(ȧ/a)(ρ + p/c²) = 0，

从而：对无压物质（p = 0），ρ ∝ a^{−3}；对辐射（p = ρc²/3），ρ ∝ a^{−4}；对宇宙学常数（p = −ρc²），ρ = 常数。

**Step 1 — ν = 0 component of ∇^μ T_{μν} = 0.** For a perfect fluid T^{μν} = (ρ + p/c²) u^μ u^ν + (p/c²) g^{μν} in the cosmic rest frame (u^μ = (c, 0, 0, 0) with u^0 = c for x^0 = ct), the covariant conservation ∇_μ T^{μ0} = 0 reduces in the FLRW background to:

**第 1 步 — ∇^μ T_{μν} = 0 的 ν = 0 分量。** 对于宇宙静止系中的完美流体 T^{μν} = (ρ + p/c²) u^μ u^ν + (p/c²) g^{μν}（u^0 = c，x^0 = ct），在 FLRW 背景下协变守恒 ∇_μ T^{μ0} = 0 化为：

  ∂_μ T^{μ0} + Γ^μ_{μλ} T^{λ0} − Γ^0_{μλ} T^{μλ} = 0.

Only the time component is non-trivial (by homogeneity and isotropy):

由均匀性和各向同性，只有时间分量非平凡：

  ∂_0 T^{00} + Γ^μ_{μ0} T^{00} − Γ^0_{ij} T^{ij} = 0.

With T^{00} = ρ/c² (using c = 1 briefly: T^{00} = ρ), Γ^i_{i0} = 3ȧ/a (from Step 2 of Section A), and Γ^0_{ij} = aȧ γ_{ij}, T^{ij} = p g^{ij}/c² = p γ^{ij}/a²:

取 T^{00} = ρ（c = 1 单位），Γ^i_{i0} = 3ȧ/a，Γ^0_{ij} = aȧ γ_{ij}，T^{ij} = p γ^{ij}/a²：

  ρ̇ + 3(ȧ/a) ρ − aȧ γ_{ij} · p γ^{ij}/a² = 0
  ρ̇ + 3(ȧ/a) ρ − 3(ȧ/a) p = 0
  ρ̇ + 3(ȧ/a)(ρ + p) = 0  (c = 1).

Restoring c: **ρ̇ + 3(ȧ/a)(ρ + p/c²) = 0.** ∎

Note this equation is not independent: it can also be derived from the two Friedmann equations by differentiating the first and substituting the second.

注意此方程不是独立的：也可以通过对第一弗里德曼方程微分并代入第二方程得到。

**Step 2 — Dust (p = 0): matter scaling.** Setting p = 0:

**第 2 步 — 尘埃（p = 0）：物质标度。** 令 p = 0：

  ρ̇ = −3(ȧ/a) ρ   ⟹   dρ/ρ = −3 da/a   ⟹   ln ρ = −3 ln a + const

  **ρ_m ∝ a^{−3}**.

This is the dilution of a fixed number of non-relativistic particles in volume V ∝ a³: ρ = Nm/(V) ∝ 1/a³.

这是体积 V ∝ a³ 中固定数目的非相对论性粒子的稀释：ρ = Nm/V ∝ 1/a³。

**Step 3 — Radiation (p = ρc²/3): radiation scaling.** Setting p = ρc²/3 (the equation of state for a photon gas, from Module 2.6):

**第 3 步 — 辐射（p = ρc²/3）：辐射标度。** 令 p = ρc²/3（光子气体的状态方程，来自模块 2.6）：

  ρ̇ + 3(ȧ/a)(ρ + ρ/3) = 0
  ρ̇ + 4(ȧ/a) ρ = 0
  dρ/ρ = −4 da/a   ⟹   **ρ_r ∝ a^{−4}**.

Radiation dilutes one extra power of a relative to matter because of the cosmological redshift: each photon's energy E = hν ∝ 1/a (its wavelength stretches as a), so total photon energy density ∝ (number density ∝ a^{−3}) × (energy per photon ∝ a^{−1}) = a^{−4}.

辐射比物质多稀释一个 a 的幂次，原因是宇宙学红移：每个光子的能量 E = hν ∝ 1/a（波长随 a 伸展），故总光子能量密度 ∝ （数密度 ∝ a^{−3}）×（每个光子的能量 ∝ a^{−1}）= a^{−4}。

**Step 4 — Cosmological constant (p = −ρc²): Λ scaling.** Setting p = −ρc²:

**第 4 步 — 宇宙学常数（p = −ρc²）：Λ 标度。** 令 p = −ρc²：

  ρ̇ + 3(ȧ/a)(ρ − ρ) = 0   ⟹   ρ̇ = 0   ⟹   **ρ_Λ = const.**

This is consistent with the cosmological constant as vacuum energy: empty space has a fixed energy density regardless of expansion. ∎

这与作为真空能量的宇宙学常数一致：真空具有固定的能量密度，与膨胀无关。∎

---

## C. Cosmological Redshift: 1 + z = a₀/a · 宇宙学红移：1 + z = a₀/a

**Claim.** A photon emitted at scale factor a_e and received today at scale factor a₀ = 1 has its wavelength stretched by the factor a₀/a_e, giving a redshift z = (a₀ − a_e)/a_e = 1/a_e − 1, or equivalently

  1 + z = a₀/a_e.

**命题。** 在尺度因子 a_e 时发射、今天在 a₀ = 1 时接收的光子，其波长被拉伸因子 a₀/a_e，给出红移 z = (a₀ − a_e)/a_e = 1/a_e − 1，等价地

  1 + z = a₀/a_e。

**Step 1 — Set up the photon path.** A radial photon (dΩ = 0) travels on a null geodesic ds² = 0. For the FLRW metric:

**第 1 步 — 建立光子路径。** 径向光子（dΩ = 0）沿零测地线 ds² = 0 传播。对于 FLRW 度规：

  0 = −c² dt² + a²(t) dr²/(1−kr²)
  dr/dt = c√(1−kr²) / a(t).

For a photon emitted from comoving coordinate r_e at time t_e and received at r = 0 at time t_0:

对于从共动坐标 r_e 在时刻 t_e 发射、在 r = 0 在时刻 t_0 接收的光子：

  ∫₀^{r_e} dr/√(1−kr²) = ∫_{t_e}^{t_0} c dt/a(t)   ...(*)

**Step 2 — Consider two successive wavefronts.** The first crest is emitted at time t_e and received at t_0. The second crest is emitted at t_e + δt_e and received at t_0 + δt_0. The comoving coordinate r_e is the same for both crests (the source is at rest in comoving coordinates). Therefore the right-hand side integral (*) is the same for both crests:

**第 2 步 — 考虑两个连续波前。** 第一个波峰在时刻 t_e 发射，在 t_0 接收。第二个波峰在 t_e + δt_e 发射，在 t_0 + δt_0 接收。共动坐标 r_e 对两个波峰相同（源在共动坐标中静止）。因此积分 (*) 对两个波峰相同：

  ∫_{t_e}^{t_0} c dt/a(t) = ∫_{t_e+δt_e}^{t_0+δt_0} c dt/a(t).

Subtracting:

相减：

  ∫_{t_0}^{t_0+δt_0} c dt/a(t) = ∫_{t_e}^{t_e+δt_e} c dt/a(t).

For small intervals δt_e, δt_0 ≪ the Hubble time, a(t) is approximately constant over each interval:

对于小间隔 δt_e，δt_0 ≪ 哈勃时间，a(t) 在每个间隔上近似为常数：

  δt_0/a(t_0) = δt_e/a(t_e).

**Step 3 — Relate frequency to scale factor.** The emitted frequency is ν_e = 1/δt_e and the received frequency is ν_0 = 1/δt_0. Therefore:

**第 3 步 — 将频率与尺度因子联系起来。** 发射频率为 ν_e = 1/δt_e，接收频率为 ν_0 = 1/δt_0。因此：

  ν_0/ν_e = δt_e/δt_0 = a(t_e)/a(t_0).

**Step 4 — Define the redshift.** The cosmological redshift is z = (ν_e − ν_0)/ν_0 = (λ_0 − λ_e)/λ_e (λ ∝ 1/ν). So:

**第 4 步 — 定义红移。** 宇宙学红移为 z = (ν_e − ν_0)/ν_0 = (λ_0 − λ_e)/λ_e（λ ∝ 1/ν）。故：

  1 + z = ν_e/ν_0 = a(t_0)/a(t_e) = a_0/a_e.

With the conventional normalization a_0 = a(t_0) = 1:

使用约定归一化 a_0 = a(t_0) = 1：

  **1 + z = 1/a_e**,  or equivalently  a_e = 1/(1+z). ∎

This is purely kinematic — no gravitational redshift formula is needed; the stretching of photon wavelengths is a consequence of the expanding spatial metric. The scale factor at recombination a_rec = 1/(1 + 1100) ≈ 9 × 10⁻⁴ corresponds to a universe about 1100 times smaller than today.

这是纯运动学的——不需要引力红移公式；光子波长的拉伸是膨胀空间度规的结果。复合时代的尺度因子 a_rec = 1/(1 + 1100) ≈ 9 × 10⁻⁴ 对应于一个比今天小约 1100 倍的宇宙。

---

## D. Scale-factor Solutions and the Fate of the Universe · 尺度因子的解与宇宙的命运

**Claim.** For a spatially flat (k = 0) universe with Λ = 0 and a single fluid component with equation of state w = p/(ρc²), the first Friedmann equation gives a(t) ∝ t^{2/3(1+w)} for w ≠ −1. In particular:
- Matter dominated (w = 0): a(t) ∝ t^{2/3}
- Radiation dominated (w = 1/3): a(t) ∝ t^{1/2}
- Λ dominated (w = −1): a(t) ∝ e^{Ht} (de Sitter)

**命题。** 对于空间平坦（k = 0）、Λ = 0、含单一流体成分（状态方程 w = p/(ρc²)）的宇宙，第一弗里德曼方程给出 a(t) ∝ t^{2/3(1+w)}（当 w ≠ −1）。特别地：
- 物质主导（w = 0）：a(t) ∝ t^{2/3}
- 辐射主导（w = 1/3）：a(t) ∝ t^{1/2}
- Λ 主导（w = −1）：a(t) ∝ e^{Ht}（德西特）

**Step 1 — Use the density scaling.** From Section B, ρ ∝ a^{−3(1+w)} (combining the three cases: w = 0 gives a^{−3}, w = 1/3 gives a^{−4}, w = −1 gives a^0 = const).

**第 1 步 — 使用密度标度关系。** 由 B 节，ρ ∝ a^{−3(1+w)}（综合三种情形：w = 0 给出 a^{−3}，w = 1/3 给出 a^{−4}，w = −1 给出 a^0 = 常数）。

Write ρ = ρ_0 a^{−3(1+w)} (with ρ_0 the present density if a_0 = 1).

写出 ρ = ρ_0 a^{−3(1+w)}（ρ_0 为 a_0 = 1 时的当前密度）。

**Step 2 — Substitute into the first Friedmann equation (k = 0, Λ = 0).**

**第 2 步 — 代入第一弗里德曼方程（k = 0，Λ = 0）。**

  (ȧ/a)² = (8πG/3) ρ_0 a^{−3(1+w)}
  ȧ² = (8πG ρ_0/3) a^{−(1+3w)}.

For w ≠ −1, write ȧ = da/dt and separate variables:

对于 w ≠ −1，写出 ȧ = da/dt 并分离变量：

  a^{(1+3w)/2} da = √(8πG ρ_0/3) dt.

**Step 3 — Integrate.** Let n = (1+3w)/2, then:

**第 3 步 — 积分。** 令 n = (1+3w)/2，则：

  a^{n+1}/(n+1) = √(8πG ρ_0/3) · t + const.

With initial condition a(0) = 0 (Big Bang at t = 0), the constant is zero:

取初始条件 a(0) = 0（t = 0 时的大爆炸），常数为零：

  a^{n+1} ∝ t   ⟹   a ∝ t^{1/(n+1)} = t^{2/(3(1+w))}.

This confirms:

这证实：

- w = 0 (matter): a ∝ t^{2/(3·1)} = **t^{2/3}**
- w = 1/3 (radiation): a ∝ t^{2/(3·4/3)} = t^{2/2} = **t^{1/2}**

**Step 4 — De Sitter case (w = −1, Λ dominated).** For ρ_Λ = Λc²/(8πG) = const, the first Friedmann equation gives:

**第 4 步 — 德西特情形（w = −1，Λ 主导）。** 对于 ρ_Λ = Λc²/(8πG) = 常数，第一弗里德曼方程给出：

  (ȧ/a)² = Λc²/3 = H²   ⟹   ȧ = Ha

where H = c√(Λ/3) = const. The solution is:

其中 H = c√(Λ/3) = 常数。解为：

  **a(t) ∝ e^{Ht}**,

exponential expansion (de Sitter space). This is the late-time attractor of any Λ-dominated universe. ∎

指数膨胀（德西特空间）。这是任何 Λ 主导宇宙的晚时吸引子。∎

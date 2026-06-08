# Derivations — Module 2.7: Kinetic Theory & Transport
# 推导 — 模块 2.7：动理论与输运

> Companion to [Module 2.7](./module-2.7-kinetic-theory-and-transport.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.7](./module-2.7-kinetic-theory-and-transport.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Maxwell–Boltzmann Speed Distribution · 麦克斯韦–玻尔兹曼速率分布

**Claim.** For a classical ideal gas in equilibrium at temperature T, the distribution of molecular speeds v = |v| is

**命题。** 对于温度为 T 处于平衡态的经典理想气体，分子速率 v = |v| 的分布为

  f(v) = 4π n (m/2πk_BT)^{3/2} v² e^{−mv²/2k_BT},

where n = N/V is the number density.

其中 n = N/V 为数密度。

**Step 1 — Start from the 3D velocity distribution.** From the Boltzmann distribution, the probability density in velocity space is proportional to e^{−mv²/2k_BT} (since the kinetic energy is ½mv² = ½m(v_x² + v_y² + v_z²)). The normalized 3D velocity distribution is

**第 1 步 — 从三维速度分布出发。** 由玻尔兹曼分布，速度空间中的概率密度正比于 e^{−mv²/2k_BT}（因为动能为 ½mv² = ½m(v_x² + v_y² + v_z²)）。归一化的三维速度分布为

  f_3D(v_x, v_y, v_z) = (m/2πk_BT)^{3/2} e^{−m(v_x² + v_y² + v_z²)/2k_BT},

normalized so that ∫ f_3D d³v = 1.

归一化使得 ∫ f_3D d³v = 1。

**Step 2 — Convert from velocity components to speed.** The distribution in velocity space is isotropic (depends only on |v|). To find the speed distribution f(v), integrate over the angular part of the spherical shell in velocity space between v and v + dv:

**第 2 步 — 从速度分量转化为速率。** 速度空间中的分布是各向同性的（只依赖于 |v|）。为求速率分布 f(v)，对速度空间中 v 到 v + dv 之间球壳的角度部分积分：

  f(v) dv = f_3D(v_x, v_y, v_z) · 4πv² dv   [4πv² dv = surface area of shell × thickness]

  f(v) = 4πv² · (m/2πk_BT)^{3/2} e^{−mv²/2k_BT}.

Multiplying by n to get the number density per unit speed interval gives the Maxwell–Boltzmann speed distribution:

乘以 n 得到单位速率区间内的数密度：

  **f(v) = 4πn (m/2πk_BT)^{3/2} v² e^{−mv²/2k_BT}.** ∎

The v² factor (proportional to the surface area of the shell in velocity space) is responsible for the distribution being zero at v = 0 and having a peak at the most probable speed v_p = √(2k_BT/m).

v² 因子（正比于速度空间中球壳的表面积）使得分布在 v = 0 处为零，并在最概然速率 v_p = √(2k_BT/m) 处有峰值。

**Step 3 — Verify normalization and compute mean quantities.** Using Gaussian integrals ∫_0^∞ v^n e^{−av²} dv:

**第 3 步 — 验证归一化并计算平均量。** 利用高斯积分 ∫_0^∞ v^n e^{−av²} dv：

  ∫_0^∞ f(v)/n dv = 4π(m/2πk_BT)^{3/2} · (π^{1/2}/4)(2k_BT/m)^{3/2} = 1   ✓

  ⟨v⟩ = √(8k_BT/πm)   (mean speed)

  ⟨v²⟩ = 3k_BT/m  ⟹  v_rms = √(3k_BT/m)   (root-mean-square speed)

---

## B. Ideal Gas Pressure from Wall Momentum Flux · 从壁面动量通量推导理想气体压强

**Claim.** For N molecules of mass m in a box of volume V = L³ with the Maxwell–Boltzmann distribution, the pressure satisfies PV = Nk_BT.

**命题。** 对于体积 V = L³ 的箱中具有麦克斯韦–玻尔兹曼分布的 N 个质量为 m 的分子，压强满足 PV = Nk_BT。

**Step 1 — Compute the momentum transfer per collision.** Consider a molecule with velocity component v_x > 0 striking the right wall (perpendicular to the x-axis). The elastic collision reverses v_x, so the momentum transferred to the wall per collision is

**第 1 步 — 计算每次碰撞的动量传递。** 考虑速度 x 分量 v_x > 0 的分子撞击右壁（垂直于 x 轴）。弹性碰撞使 v_x 反向，每次碰撞传给壁面的动量为

  Δp = 2mv_x.

**Step 2 — Count collisions per unit time per unit area.** A molecule with speed v_x travels a distance v_x dt in time dt. All molecules within distance v_x dt from the wall (in a volume A v_x dt, where A is the wall area) will hit the wall in that time. The number of such molecules with speed component between v_x and v_x + dv_x is

**第 2 步 — 计算单位时间单位面积的碰撞次数。** 速度 v_x 的分子在时间 dt 内行进距离 v_x dt。在该时间内，所有距壁面距离小于 v_x dt 的分子（在体积 A v_x dt 中，A 为壁面面积）都会碰壁。速度分量在 v_x 到 v_x + dv_x 之间的此类分子数为

  dN_coll = (n/2) f_1D(v_x) A v_x dt dv_x,

where n/2 accounts for only molecules moving toward the wall, and f_1D(v_x) ∝ e^{−mv_x²/2k_BT} is the 1D Maxwell distribution (normalized to 1).

其中 n/2 仅计算向壁运动的分子，f_1D(v_x) ∝ e^{−mv_x²/2k_BT} 是一维麦克斯韦分布（归一化为 1）。

**Step 3 — Integrate to find total force per unit area.** The pressure is

**第 3 步 — 积分求单位面积总力。** 压强为

  P = (1/A) ∫_0^∞ (Δp/dt) (dN_coll/dt·A·dv_x) / A · A
    = n ∫_0^∞ m v_x² f_1D(v_x) dv_x = n m ⟨v_x²⟩ = n m · k_BT/m = n k_BT.

(Here we used ⟨v_x²⟩ = k_BT/m from the equipartition theorem and f_1D is the full 1D distribution so the integral over all v_x of mv_x² f_1D gives m⟨v_x²⟩ = k_BT.) Therefore

（这里利用了能均分定理 ⟨v_x²⟩ = k_BT/m，f_1D 是完整的一维分布，所以对所有 v_x 的积分 mv_x² f_1D 给出 m⟨v_x²⟩ = k_BT。）因此

  P = nk_BT = (N/V)k_BT,

which gives **PV = Nk_BT.** ∎

These steps more carefully: the pressure on the wall equals the momentum flux. For molecules with 1D speed distribution f_1D(v_x) = (m/2πk_BT)^{1/2} e^{−mv_x²/2k_BT}, integrating over v_x > 0:

这些步骤更仔细地说：壁面压强等于动量通量。对于具有一维速率分布 f_1D(v_x) = (m/2πk_BT)^{1/2} e^{−mv_x²/2k_BT} 的分子，对 v_x > 0 积分：

  P = n ∫_0^∞ mv_x · v_x · f_1D(v_x) dv_x = nm ∫_0^∞ v_x² f_1D(v_x) dv_x = nm · ½⟨v_x²⟩ · 2
    = nm⟨v_x²⟩ = nk_BT. ∎

---

## C. Mean Free Path · 平均自由程

**Claim.** The mean free path of a molecule in a gas of number density n with collision cross-section σ is ℓ = 1/(√2 nσ).

**命题。** 在数密度为 n、碰撞截面为 σ 的气体中，分子的平均自由程为 ℓ = 1/(√2 nσ)。

**Step 1 — Model collisions as hard-sphere scattering.** Two molecules of diameter d collide when their centers come within distance d. The collision cross-section is σ = πd².

**第 1 步 — 将碰撞建模为硬球散射。** 两个直径为 d 的分子当其中心距离小于 d 时发生碰撞。碰撞截面为 σ = πd²。

**Step 2 — Compute the collision rate for a single molecule moving through a gas.** A molecule moving with speed v sweeps out a cylinder of cross-sectional area σ per unit time. The collision rate (number of collisions per unit time) for a single molecule is

**第 2 步 — 计算单个分子在气体中运动的碰撞率。** 以速度 v 运动的分子每单位时间扫过横截面积为 σ 的柱体。单个分子的碰撞率（单位时间碰撞次数）为

  Γ = n σ v_rel,

where v_rel is the relative speed between the test molecule and the gas molecules it encounters. In a Maxwell–Boltzmann gas, the mean relative speed is

其中 v_rel 是被测分子与它遇到的气体分子之间的相对速率。在麦克斯韦–玻尔兹曼气体中，平均相对速率为

  ⟨v_rel⟩ = √2 ⟨v⟩,

since for two molecules drawn independently from the same Maxwell–Boltzmann distribution, the mean squared relative velocity is ⟨v_rel²⟩ = 2⟨v²⟩ (by the independence of velocities), giving ⟨v_rel⟩ ≈ √2 ⟨v⟩ (the precise result from integrating over the bivariate distribution). Therefore the collision rate is

因为对于从同一麦克斯韦–玻尔兹曼分布独立抽取的两个分子，平均相对速度平方为 ⟨v_rel²⟩ = 2⟨v²⟩（由速度的独立性），给出 ⟨v_rel⟩ ≈ √2 ⟨v⟩（对双变量分布积分的精确结果）。因此碰撞率为

  Γ = n σ √2 ⟨v⟩.

**Step 3 — Compute the mean free path.** The mean free path is the mean distance traveled between collisions: ℓ = ⟨v⟩/Γ:

**第 3 步 — 计算平均自由程。** 平均自由程是碰撞之间平均行进的距离：ℓ = ⟨v⟩/Γ：

  **ℓ = ⟨v⟩ / (√2 nσ ⟨v⟩) = 1/(√2 nσ).** ∎

For air at STP (n ≈ 2.7 × 10²⁵ m⁻³, σ ≈ 4 × 10⁻¹⁹ m²), ℓ ≈ 65 nm, much larger than molecular size but much smaller than macroscopic lengths — the condition for the fluid mechanics description (Knudsen number Kn = ℓ/L ≪ 1).

对于标准状态下的空气（n ≈ 2.7 × 10²⁵ m⁻³，σ ≈ 4 × 10⁻¹⁹ m²），ℓ ≈ 65 nm，远大于分子尺寸但远小于宏观长度——流体力学描述的条件（努森数 Kn = ℓ/L ≪ 1）。

---

## D. Drude Conductivity σ = ne²τ/m from the Relaxation-Time Boltzmann Equation · 从弛豫时间玻尔兹曼方程推导德鲁德电导率 σ = ne²τ/m

**Claim.** For a free electron gas in a uniform electric field E (along x̂) with relaxation time τ, the steady-state electrical conductivity is σ = ne²τ/m (in SI units, this is the Drude formula).

**命题。** 对于在均匀电场 E（沿 x̂ 方向）中弛豫时间为 τ 的自由电子气，稳态电导率为 σ = ne²τ/m（SI 单位，即德鲁德公式）。

**Step 1 — Write the Boltzmann transport equation.** The distribution function f(r, v, t) for electrons evolves according to

**第 1 步 — 写出玻尔兹曼输运方程。** 电子的分布函数 f(r, v, t) 按以下方程演化：

  ∂f/∂t + v · ∇_r f + (F/m) · ∇_v f = (∂f/∂t)_coll,

where F = −eE is the force on an electron (charge −e, e > 0) due to the electric field.

其中 F = −eE 是电场对电子（电荷 −e，e > 0）的作用力。

**Step 2 — Apply the relaxation-time approximation.** In the relaxation-time approximation, the collision term is

**第 2 步 — 应用弛豫时间近似。** 在弛豫时间近似中，碰撞项为

  (∂f/∂t)_coll = −(f − f₀)/τ,

where f₀ is the equilibrium (Fermi–Dirac or Maxwell–Boltzmann) distribution and τ is the mean time between collisions (treated as a constant here). This approximation says that collisions drive f back to f₀ exponentially with rate 1/τ.

其中 f₀ 是平衡（费米–狄拉克或麦克斯韦–玻尔兹曼）分布，τ 是碰撞间的平均时间（此处视为常数）。该近似表明碰撞以速率 1/τ 指数地将 f 驱回 f₀。

**Step 3 — Linearize for a weak field.** Write f = f₀ + f₁, where f₁ is the small deviation from equilibrium induced by E. In steady state (∂f/∂t = 0) and a spatially uniform system (∇_r f = 0), the Boltzmann equation reduces to

**第 3 步 — 对弱场线性化。** 写 f = f₀ + f₁，其中 f₁ 是由 E 引起的对平衡态的小偏差。在稳态（∂f/∂t = 0）和空间均匀系统（∇_r f = 0）中，玻尔兹曼方程化为

  (F/m) · ∇_v f₀ = −f₁/τ   (to first order in E, using ∇_v f₁ ≈ 0)
  f₁ = −τ (F/m) · ∇_v f₀ = (eτ/m) E · ∇_v f₀.

For a 1D field E = E x̂:

对于一维场 E = E x̂：

  f₁ = (eEτ/m) ∂f₀/∂v_x.

**Step 4 — Compute the current density.** The electrical current density is

**第 4 步 — 计算电流密度。** 电流密度为

  j_x = −e ∫ v_x f d³v = −e ∫ v_x (f₀ + f₁) d³v = −e ∫ v_x f₁ d³v,

where the f₀ term vanishes by symmetry (∫ v_x f₀ d³v = 0 since f₀ is even in v_x).

其中 f₀ 项由对称性为零（∫ v_x f₀ d³v = 0，因为 f₀ 关于 v_x 是偶函数）。

Substituting f₁:

代入 f₁：

  j_x = −e ∫ v_x · (eEτ/m) ∂f₀/∂v_x d³v = −(e²Eτ/m) ∫ v_x (∂f₀/∂v_x) d³v.

**Step 5 — Integrate by parts.** Integrate by parts in v_x (boundary terms vanish as f₀ → 0 for |v_x| → ∞):

**第 5 步 — 分部积分。** 对 v_x 进行分部积分（当 |v_x| → ∞ 时 f₀ → 0，边界项为零）：

  ∫ v_x ∂f₀/∂v_x dv_x = [v_x f₀]_{−∞}^{∞} − ∫ f₀ dv_x = −∫ f₀ dv_x.

Therefore:

因此：

  ∫ v_x ∂f₀/∂v_x d³v = −∫ f₀ d³v = −n   (total number density).

Substituting back:

代入：

  j_x = −(e²Eτ/m) · (−n) = (ne²τ/m) E.

**Step 6 — Identify the conductivity.** By Ohm's law j = σE:

**第 6 步 — 识别电导率。** 由欧姆定律 j = σE：

  **σ = ne²τ/m.** ∎

This is the Drude formula. For copper at room temperature, n ≈ 8.5 × 10²⁸ m⁻³, σ ≈ 6 × 10⁷ Ω⁻¹m⁻¹, m_e = 9.1 × 10⁻³¹ kg, e = 1.6 × 10⁻¹⁹ C, giving τ ≈ 25 fs. The same calculation applies to a quantum (Fermi–Dirac) electron gas, where the Fermi velocity v_F replaces the thermal velocity; the form σ = ne²τ/m is unchanged.

这就是德鲁德公式。对于室温铜，n ≈ 8.5 × 10²⁸ m⁻³，σ ≈ 6 × 10⁷ Ω⁻¹m⁻¹，m_e = 9.1 × 10⁻³¹ kg，e = 1.6 × 10⁻¹⁹ C，给出 τ ≈ 25 fs。同样的计算适用于量子（费米–狄拉克）电子气，其中费米速度 v_F 替代热速度；σ = ne²τ/m 的形式不变。

---

*The kinetic-theory results here — Maxwell speed distribution, PV = Nk_BT, mean free path, and Drude conductivity — form the microscopic derivations underlying the macroscopic transport equations (Navier–Stokes, Fourier's law, Fick's law, Ohm's law). The Boltzmann equation is the master tool connecting statistical mechanics to non-equilibrium phenomena, and appears again in electron and phonon transport in Phase 4.*

*此处的动理论结果——麦克斯韦速率分布、PV = Nk_BT、平均自由程和德鲁德电导率——构成宏观输运方程（纳维–斯托克斯方程、傅里叶定律、菲克定律、欧姆定律）的微观推导基础。玻尔兹曼方程是联系统计力学与非平衡现象的主要工具，并在第 4 阶段的电子和声子输运中再次出现。*

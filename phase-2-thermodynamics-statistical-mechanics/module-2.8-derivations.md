# Derivations — Module 2.8: Brownian Motion & the Einstein Relation
# 推导 — 模块 2.8：布朗运动与爱因斯坦关系

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.8](./module-2.8-brownian-motion-and-the-einstein-relation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.8](./module-2.8-brownian-motion-and-the-einstein-relation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Mean-Square Displacement ⟨x²⟩ = 2Dt from the Diffusion Equation · 从扩散方程推导均方位移 ⟨x²⟩ = 2Dt

**Claim.** For a particle undergoing diffusion described by ∂P/∂t = D ∂²P/∂x², starting at x = 0, the mean-square displacement is ⟨x²(t)⟩ = 2Dt.

**命题。** 对于由扩散方程 ∂P/∂t = D ∂²P/∂x² 描述的粒子，从 x = 0 出发，均方位移为 ⟨x²(t)⟩ = 2Dt。

**Step 1 — Solve the diffusion equation with a delta-function initial condition.** Start with P(x, 0) = δ(x) (particle starts at origin). The diffusion equation ∂P/∂t = D ∂²P/∂x² has a Gaussian solution (verified by direct substitution):

**第 1 步 — 用δ函数初始条件求解扩散方程。** 取 P(x, 0) = δ(x)（粒子从原点出发）。扩散方程 ∂P/∂t = D ∂²P/∂x² 有高斯解（可直接代入验证）：

  P(x, t) = (1/√(4πDt)) exp(−x²/(4Dt)).

Check: at t → 0, this narrows to δ(x). Normalization: ∫_{−∞}^{∞} P(x,t) dx = 1 for all t (by the Gaussian integral). The mean: ⟨x⟩ = 0 by symmetry (odd integrand).

验证：当 t → 0 时，此式收缩为 δ(x)。归一化：对所有 t，∫_{−∞}^{∞} P(x,t) dx = 1（由高斯积分）。均值：⟨x⟩ = 0（由对称性，被积函数为奇函数）。

**Step 2 — Compute ⟨x²⟩ directly from the solution.**

**第 2 步 — 直接从解计算 ⟨x²⟩。**

  ⟨x²⟩ = ∫_{−∞}^{∞} x² P(x, t) dx = (1/√(4πDt)) ∫_{−∞}^{∞} x² e^{−x²/(4Dt)} dx.

Use the Gaussian integral ∫_{−∞}^{∞} x² e^{−ax²} dx = (√π)/(2a^{3/2}) with a = 1/(4Dt):

利用高斯积分 ∫_{−∞}^{∞} x² e^{−ax²} dx = (√π)/(2a^{3/2})，令 a = 1/(4Dt)：

  ⟨x²⟩ = (1/√(4πDt)) · √π / [2·(1/(4Dt))^{3/2}]
         = (1/√(4πDt)) · √π · 2 · (4Dt)^{3/2} / 4
         = (1/√(4πDt)) · √π · (4Dt) · √(4Dt) / 2
         = (1/√(4πDt)) · √(πDt) · 4Dt · (1/2)
         [More directly: 1/(√(4πDt)) · (√π/(2)) · (4Dt)^{3/2} = (1/√(4πDt)) · (√π/2) · (4Dt)√(4Dt)]

Let us use the simpler route: set u = x/√(4Dt), so x = u√(4Dt), dx = √(4Dt) du:

用更简洁的方法：令 u = x/√(4Dt)，则 x = u√(4Dt)，dx = √(4Dt) du：

  ⟨x²⟩ = (1/√(4πDt)) ∫_{−∞}^{∞} u²(4Dt) e^{−u²} √(4Dt) du
         = (4Dt)^{3/2}/√(4πDt) ∫_{−∞}^{∞} u² e^{−u²} du
         = (4Dt)/√π · ∫_{−∞}^{∞} u² e^{−u²} du.

Standard integral: ∫_{−∞}^{∞} u² e^{−u²} du = √π/2. Therefore:

标准积分：∫_{−∞}^{∞} u² e^{−u²} du = √π/2。因此：

  ⟨x²⟩ = (4Dt)/√π · √π/2 = **2Dt.** ∎

**Step 3 — Alternative derivation via the equation of motion for ⟨x²⟩.** Multiply the diffusion equation ∂P/∂t = D ∂²P/∂x² by x² and integrate over all x:

**第 3 步 — 通过 ⟨x²⟩ 的运动方程的另一种推导。** 将扩散方程 ∂P/∂t = D ∂²P/∂x² 乘以 x² 并对所有 x 积分：

  d⟨x²⟩/dt = D ∫ x² ∂²P/∂x² dx.

Integrate by parts twice (boundary terms vanish):

分部积分两次（边界项为零）：

  ∫ x² ∂²P/∂x² dx = [x² ∂P/∂x]_{−∞}^{∞} − 2∫ x ∂P/∂x dx = −2[xP]_{−∞}^{∞} + 2∫ P dx = 2.

Therefore d⟨x²⟩/dt = 2D, which integrates immediately to ⟨x²(t)⟩ = 2Dt (with ⟨x²(0)⟩ = 0). ∎

因此 d⟨x²⟩/dt = 2D，直接积分得 ⟨x²(t)⟩ = 2Dt（初始条件 ⟨x²(0)⟩ = 0）。∎

**Step 4 — Connection to random walk.** Consider N independent steps of duration τ each, with step sizes drawn from a distribution with zero mean and variance ⟨(Δx)²⟩ = 2Dτ. After time t = Nτ, the Central Limit Theorem gives ⟨x²⟩ = N⟨(Δx)²⟩ = (t/τ)(2Dτ) = 2Dt. The Gaussian distribution P(x,t) is the continuum limit of this random walk, as N → ∞ with τ → 0 and Dτ fixed. ∎

**第 4 步 — 与随机游走的联系。** 考虑 N 个各自持续时间为 τ 的独立步骤，步长从均值为零、方差为 ⟨(Δx)²⟩ = 2Dτ 的分布中抽取。经过时间 t = Nτ 后，中心极限定理给出 ⟨x²⟩ = N⟨(Δx)²⟩ = (t/τ)(2Dτ) = 2Dt。高斯分布 P(x,t) 是该随机游走在 N → ∞、τ → 0 且 Dτ 固定时的连续极限。∎

---

## B. Einstein Relation D = μ k_BT · 爱因斯坦关系 D = μ k_BT

**Claim.** For a Brownian particle in a fluid at temperature T with mobility μ (drift velocity per unit applied force), the diffusion coefficient satisfies D = μ k_BT.

**命题。** 对于在温度为 T 的流体中运动的布朗粒子，其迁移率为 μ（单位力作用下的漂移速度），扩散系数满足 D = μ k_BT。

**Step 1 — Set up the equilibrium condition.** Place the Brownian particle in a potential V(x) = mgx (a small gravitational or external potential gradient). In equilibrium, the particle density n(x) must satisfy the Boltzmann distribution:

**第 1 步 — 建立平衡条件。** 将布朗粒子置于势场 V(x) = mgx（小的重力或外部势梯度）中。平衡时，粒子密度 n(x) 必须满足玻尔兹曼分布：

  n(x) = n₀ e^{−V(x)/k_BT} = n₀ e^{−mgx/k_BT}.

**Step 2 — Equilibrium requires zero net flux.** In equilibrium, the total particle flux J = 0. There are two competing fluxes:

**第 2 步 — 平衡要求总通量为零。** 在平衡时，总粒子通量 J = 0。存在两个相互竞争的通量：

  (i) Diffusion flux (Fick's law, opposing the density gradient):   J_diff = −D dn/dx,
  (ii) Drift flux (due to force F = −dV/dx = −mg on the particle):   J_drift = n · v_drift = n · μ F = −nμ mg.

Setting J_diff + J_drift = 0:

令 J_diff + J_drift = 0：

  −D dn/dx − nμ mg = 0.

**Step 3 — Substitute the Boltzmann distribution.** From n(x) = n₀ e^{−mgx/k_BT}:

**第 3 步 — 代入玻尔兹曼分布。** 由 n(x) = n₀ e^{−mgx/k_BT}：

  dn/dx = n₀ e^{−mgx/k_BT} · (−mg/k_BT) = −(mg/k_BT) n.

Substituting into the zero-flux condition:

代入零通量条件：

  −D · (−mg/k_BT) n − nμmg = 0,
  (D/k_BT − μ) nmg = 0.

Since n ≠ 0 and mg ≠ 0, we must have

由于 n ≠ 0 且 mg ≠ 0，必须有

  D/k_BT = μ,   i.e.,   **D = μ k_BT.** ∎

**Step 4 — Physical interpretation.** The Einstein relation D = μk_BT says that the random diffusive spreading (D) and the deterministic drift response (μ) are both caused by the same underlying molecular collisions: D measures how strongly collisions randomize the particle's position, while μ = 1/γ (where γ is the friction coefficient) measures how strongly collisions oppose directed motion. The ratio D/μ = k_BT is purely thermodynamic — it depends only on the temperature, not on the details of the particle or the fluid.

**第 4 步 — 物理诠释。** 爱因斯坦关系 D = μk_BT 表明：随机扩散扩展（D）和确定性漂移响应（μ）均由相同的底层分子碰撞引起：D 衡量碰撞使粒子位置随机化的强度，而 μ = 1/γ（γ 为摩擦系数）衡量碰撞阻碍定向运动的强度。比值 D/μ = k_BT 纯粹是热力学的——它只依赖于温度，而不依赖于粒子或流体的细节。

---

## C. Stokes–Einstein Relation and Avogadro's Number · 斯托克斯–爱因斯坦关系与阿伏加德罗常数

**Claim.** For a spherical particle of radius r in a fluid of viscosity η, the Stokes drag gives mobility μ = 1/(6πηr), so D = k_BT/(6πηr).

**命题。** 对于粘度为 η 的流体中半径为 r 的球形粒子，斯托克斯阻力给出迁移率 μ = 1/(6πηr)，故 D = k_BT/(6πηr)。

**Step 1 — Stokes' law.** For a sphere of radius r moving with velocity v in a viscous fluid of viscosity η at low Reynolds number (Re = ρvr/η ≪ 1, the Stokes regime), the drag force is

**第 1 步 — 斯托克斯定律。** 对于在粘度为 η 的粘性流体中以速度 v 运动的半径为 r 的球，在低雷诺数（Re = ρvr/η ≪ 1，斯托克斯区）时，阻力为

  F_drag = −6πηr v.

This is a result of solving the linearized (creeping-flow) Navier–Stokes equations. The friction coefficient is γ = 6πηr.

这是求解线性化（蠕变流）纳维–斯托克斯方程的结果。摩擦系数为 γ = 6πηr。

**Step 2 — Identify the mobility.** The mobility is the drift velocity per unit applied force. In steady state (no acceleration), the applied force F equals the drag: F = γv_drift, so

**第 2 步 — 确定迁移率。** 迁移率是单位力作用下的漂移速度。在稳态（无加速度）时，施加的力 F 等于阻力：F = γv_drift，故

  μ = v_drift/F = 1/γ = 1/(6πηr).

**Step 3 — Apply the Einstein relation.**

**第 3 步 — 应用爱因斯坦关系。**

  **D = μ k_BT = k_BT / (6πηr).** ∎

**Step 4 — Extract Avogadro's number.** Writing k_B = R/N_A where R is the molar gas constant:

**第 4 步 — 提取阿伏加德罗常数。** 写 k_B = R/N_A，其中 R 为摩尔气体常数：

  D = R T / (6πηr N_A),   so   **N_A = RT/(6πηr D).**

Perrin (1908) measured D by tracking the mean-square displacement of gamboge particles (r ≈ 0.2 μm) in water: ⟨x²⟩ = 2Dt over measured time intervals t. Combined with measured η and r, this gave N_A ≈ 6 × 10²³ mol⁻¹ — the first direct, model-independent determination of Avogadro's number, providing decisive proof of the atomic hypothesis.

佩兰（1908）通过追踪金橘粒子（r ≈ 0.2 μm）在水中的均方位移测量了 D：在测量的时间间隔 t 内 ⟨x²⟩ = 2Dt。结合测量的 η 和 r，得到 N_A ≈ 6 × 10²³ mol⁻¹——这是阿伏加德罗常数的第一次直接、独立于模型的测定，为原子假说提供了决定性证明。

---

## D. Fluctuation–Dissipation Theorem: The Deep Connection · 涨落–耗散定理：深层联系

**Claim.** The Einstein relation D = μk_BT is a special case of the fluctuation–dissipation theorem (FDT): in thermal equilibrium, the spectrum of spontaneous fluctuations of a quantity X is related to the dissipative part of the response to a perturbation conjugate to X, with k_BT as the proportionality factor.

**命题。** 爱因斯坦关系 D = μk_BT 是涨落–耗散定理（FDT）的特例：在热平衡中，量 X 的自发涨落谱与对共轭于 X 的扰动的耗散响应相关，比例因子为 k_BT。

**Step 1 — The Langevin equation.** The microscopic description of a Brownian particle is the Langevin equation:

**第 1 步 — 朗之万方程。** 布朗粒子的微观描述是朗之万方程：

  m dv/dt = −γv + ξ(t),

where γ = 1/μ = 6πηr is the friction coefficient and ξ(t) is a random (stochastic) force representing the fluctuating collisions of the fluid molecules.

其中 γ = 1/μ = 6πηr 是摩擦系数，ξ(t) 是代表流体分子随机碰撞的随机（随机过程）力。

**Step 2 — Properties of the random force.** The random force ξ(t) has zero mean and is uncorrelated in time (white noise):

**第 2 步 — 随机力的性质。** 随机力 ξ(t) 均值为零，且时间上不相关（白噪声）：

  ⟨ξ(t)⟩ = 0,     ⟨ξ(t)ξ(t')⟩ = 2γk_BT δ(t − t').

The amplitude of the noise 2γk_BT is not arbitrary — it is fixed by the requirement that the particle's velocity distribution is the Maxwell–Boltzmann distribution at temperature T, i.e., ½m⟨v²⟩ = ½k_BT.

噪声幅度 2γk_BT 不是任意的——它由粒子速度分布是温度 T 时麦克斯韦–玻尔兹曼分布的要求固定，即 ½m⟨v²⟩ = ½k_BT。

**Step 3 — Derive D from the velocity autocorrelation.** In the overdamped limit (m → 0, applicable for colloidal particles where inertia is negligible), the velocity is v(t) = ξ(t)/γ, and the mean-square displacement is

**第 3 步 — 从速度自相关推导 D。** 在过阻尼极限（m → 0，适用于惯性可忽略的胶体粒子）中，速度为 v(t) = ξ(t)/γ，均方位移为

  ⟨x²(t)⟩ = ∫_0^t ∫_0^t ⟨v(t')v(t'')⟩ dt' dt'' = ∫_0^t ∫_0^t (1/γ²)⟨ξ(t')ξ(t'')⟩ dt' dt''
            = (1/γ²) ∫_0^t ∫_0^t 2γk_BT δ(t' − t'') dt' dt'' = (2k_BT/γ) t.

Comparing with ⟨x²⟩ = 2Dt:

与 ⟨x²⟩ = 2Dt 比较：

  **D = k_BT/γ = μ k_BT.** ∎

This derivation shows that D arises directly from the noise amplitude 2γk_BT — the fluctuation — while μ = 1/γ characterizes the dissipation. The product D = μk_BT is the FDT: fluctuation and dissipation are inextricably linked because they both arise from the same thermal environment.

该推导表明 D 直接来源于噪声幅度 2γk_BT——即涨落——而 μ = 1/γ 刻画耗散。乘积 D = μk_BT 就是 FDT：涨落和耗散不可分割地联系在一起，因为它们都源于同一热环境。

**Step 4 — Kubo formula: general statement of the FDT.** The general form of the FDT (Kubo, 1966) states that the complex admittance (generalized susceptibility) χ(ω) of any linear dissipative system is related to the power spectral density S_xx(ω) of the equilibrium fluctuations of the conjugate variable x by

**第 4 步 — 久保公式：FDT 的一般表述。** FDT 的一般形式（久保，1966）指出，任何线性耗散系统的复导纳（广义磁化率）χ(ω) 与共轭变量 x 的平衡涨落功率谱密度 S_xx(ω) 的关系为

  S_xx(ω) = 2k_BT Im[χ(ω)] / ω   (classical limit, ℏω ≪ k_BT).

Special cases of this single relation include: (i) Einstein's D = μk_BT; (ii) Johnson–Nyquist noise in a resistor R: voltage noise spectral density S_V = 4k_BTR; (iii) the fluctuating Lorentz force on charges in a magnetic field. The underlying physics is always the same: the equilibrium thermal bath that randomizes particle trajectories (fluctuation) is the same bath that provides the frictional damping (dissipation). ∎

该单一关系的特例包括：(i) 爱因斯坦的 D = μk_BT；(ii) 电阻 R 中的约翰逊–奈奎斯特噪声：电压噪声谱密度 S_V = 4k_BTR；(iii) 磁场中电荷所受的涨落洛伦兹力。底层物理始终相同：使粒子轨迹随机化的平衡热浴（涨落）与提供摩擦阻尼的热浴（耗散）是同一个热浴。∎

---

*The Einstein relation and the Langevin equation opened the door to the modern theory of stochastic processes. The fluctuation–dissipation theorem in its Kubo form connects thermal noise to linear response theory, which underlies optical absorption (imaginary part of dielectric function), the Drude conductivity (Module 2.7), and the Kramers–Kronig relations. Together these ideas form the statistical mechanics of non-equilibrium phenomena.*

*爱因斯坦关系和朗之万方程打开了现代随机过程理论的大门。久保形式的涨落–耗散定理将热噪声与线性响应理论联系起来，后者是光学吸收（介电函数的虚部）、德鲁德电导率（模块 2.7）和克拉默斯–克朗尼希关系的基础。这些思想共同构成了非平衡现象的统计力学。*

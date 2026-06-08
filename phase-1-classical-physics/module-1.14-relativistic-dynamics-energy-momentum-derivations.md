# Derivations — Module 1.14: Relativistic Dynamics & E = mc²
# 推导 — 模块 1.14：相对论动力学与 E = mc²

> Companion to [Module 1.14](./module-1.14-relativistic-dynamics-energy-momentum.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.14](./module-1.14-relativistic-dynamics-energy-momentum.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Four-Velocity and Four-Momentum · 四速度与四动量

**Claim.** The four-velocity U^μ = dx^μ/dτ satisfies U^μ U_μ = c², and the four-momentum p^μ = mU^μ satisfies the invariant p^μ p_μ = (mc)², from which E² = (pc)² + (mc²)².

**命题。** 四速度 U^μ = dx^μ/dτ 满足 U^μ U_μ = c²，四动量 p^μ = mU^μ 满足不变量 p^μ p_μ = (mc)²，由此导出 E² = (pc)² + (mc²)²。

**Step 1 — Proper time and the Lorentz factor.** Consider a particle moving with coordinate velocity v = dx/dt in frame S. The proper time τ is the time elapsed on a clock moving with the particle. The spacetime interval for infinitesimal displacement is

**第 1 步 — 固有时与洛伦兹因子。** 考虑一个在参考系 S 中以坐标速度 v = dx/dt 运动的粒子。固有时 τ 是随粒子运动的时钟所经历的时间。无穷小位移的时空间隔为

  ds² = c² dt² − dx² − dy² − dz² = c² dt²(1 − v²/c²).

Since ds² is Lorentz-invariant and equals c² dτ² in the rest frame of the particle,

由于 ds² 是洛伦兹不变量，在粒子静止系中等于 c² dτ²，故

  dτ = dt √(1 − v²/c²) = dt/γ,   where γ = 1/√(1 − v²/c²).

**第 1 步结论：** dτ = dt/γ，其中洛伦兹因子 γ = (1 − v²/c²)^{−1/2}。

**Step 2 — Components of the four-velocity.** The four-velocity is U^μ = dx^μ/dτ. Using dτ = dt/γ:

**第 2 步 — 四速度的分量。** 四速度定义为 U^μ = dx^μ/dτ。利用 dτ = dt/γ：

  U^0 = dx^0/dτ = c dt/dτ = γc,
  U^i = dx^i/dτ = (dx^i/dt)(dt/dτ) = γv^i.

So U^μ = γ(c, v_x, v_y, v_z) = γ(c, **v**).

故 U^μ = γ(c, v_x, v_y, v_z) = γ(c, **v**)。

**Step 3 — The invariant U^μ U_μ.** Using the metric signature (+, −, −, −):

**第 3 步 — 不变量 U^μ U_μ。** 采用度规号差 (+, −, −, −)：

  U^μ U_μ = (U^0)² − (U^1)² − (U^2)² − (U^3)²
           = γ²c² − γ²v_x² − γ²v_y² − γ²v_z²
           = γ²(c² − |v|²)
           = γ² c²(1 − v²/c²)
           = γ² c² · γ^{−2}
           = c².

Hence **U^μ U_μ = c²** — a Lorentz scalar independent of the particle's speed.

故 **U^μ U_μ = c²**——与粒子速度无关的洛伦兹标量。

**Step 4 — Four-momentum and its invariant.** Define the four-momentum p^μ = mU^μ where m is the rest mass (a Lorentz scalar). Then

**第 4 步 — 四动量及其不变量。** 定义四动量 p^μ = mU^μ，其中 m 为静止质量（洛伦兹标量）。则

  p^μ p_μ = m² U^μ U_μ = m² c².

Writing out the components: p^0 = mγc = E/c (defining E ≡ γmc²), and p^i = mγv^i (the relativistic three-momentum). So

写出各分量：p^0 = mγc = E/c（定义 E ≡ γmc²），p^i = mγv^i（相对论三维动量）。于是

  p^μ p_μ = (E/c)² − |**p**|² = (mc)²,

which gives **E² = (pc)² + (mc²)²**. ∎

由此得 **E² = (pc)² + (mc²)²**。∎

---

## B. Relativistic Energy E = γmc² and its Low-Speed Expansion · 相对论能量 E = γmc² 及其低速展开

**Claim.** The time component of p^μ = mU^μ directly gives E = γmc², and for v ≪ c this expands as E ≈ mc² + ½mv².

**命题。** p^μ = mU^μ 的时间分量直接给出 E = γmc²，在 v ≪ c 时展开为 E ≈ mc² + ½mv²。

**Step 1 — Identify the energy component.** From Step 2 and Step 4 above, p^0 = mU^0 = mγc. The conventional identification is p^0 = E/c, so

**第 1 步 — 识别能量分量。** 由上面第 2 步和第 4 步，p^0 = mU^0 = mγc。按惯例 p^0 = E/c，故

  **E = γmc² = mc²/√(1 − v²/c²)**.

**Step 2 — Taylor expansion for v ≪ c.** Write β = v/c ≪ 1. Expand γ as a binomial series:

**第 2 步 — v ≪ c 时的泰勒展开。** 令 β = v/c ≪ 1。将 γ 展开为二项式级数：

  γ = (1 − β²)^{−1/2} = 1 + ½β² + ⅜β⁴ + …

Multiply by mc²:

乘以 mc²：

  E = mc²(1 + ½β² + ⅜β⁴ + …)
    = mc² + ½mc²β² + O(β⁴)
    = mc² + ½mv² + O(v⁴/c²).

The first term **mc²** is the rest energy, present even when the particle is at rest — with no classical counterpart. The second term **½mv²** is the familiar non-relativistic kinetic energy, recovered in the low-speed limit. Higher-order terms are negligible for v ≪ c.

第一项 **mc²** 是静止能量，即使粒子静止也存在——在经典力学中无对应物。第二项 **½mv²** 是熟悉的非相对论动能，在低速极限下恢复。高阶项在 v ≪ c 时可忽略。∎

---

## C. The Relativistic Doppler Shift · 相对论多普勒频移

**Claim.** A source emitting frequency f₀ in its rest frame, moving with velocity v relative to the observer along the line of sight, is observed at

**命题。** 光源在其静止系中发射频率 f₀，以速度 v 沿视线方向相对于观察者运动，观察到的频率为

  f = f₀ √((1 − β)/(1 + β))   (source receding),
  f = f₀ √((1 + β)/(1 − β))   (source approaching),

where β = v/c. This includes both the classical Doppler effect and a relativistic time-dilation correction.

其中 β = v/c。这包含经典多普勒效应和相对论时间膨胀修正两部分。

**Step 1 — Set up using four-wavevector.** Light has a four-wavevector k^μ = (ω/c)(1, n̂) where n̂ is the propagation direction and ω = 2πf. In the source rest frame S′, the four-wavevector is k′^μ = (ω₀/c)(1, 1, 0, 0) (light emitted in +x direction). In frame S the source moves at velocity −v along x (equivalently the observer is at rest and the source recedes in +x).

**第 1 步 — 利用四波矢建立方程。** 光具有四波矢 k^μ = (ω/c)(1, n̂)，其中 n̂ 为传播方向，ω = 2πf。在光源静止系 S′ 中，四波矢为 k′^μ = (ω₀/c)(1, 1, 0, 0)（沿 +x 方向发射）。在 S 系中，光源以 −v 沿 x 轴运动（等价地，观察者静止，光源沿 +x 方向远离）。

**Step 2 — Apply the Lorentz transformation.** The boost from S′ to S (source moving at +v in S, i.e. boost parameter −v) transforms the 0-component:

**第 2 步 — 应用洛伦兹变换。** 从 S′ 到 S 的变换（S 中光源以 +v 运动，即增强参数为 −v）作用于 0 分量：

  k^0 = γ(k′^0 + (v/c) k′^1) = γ(ω₀/c)(1 + β).

Wait — let us be careful about sign conventions. Let the source move in the +x direction away from the observer with speed v. In the source rest frame S′, light is emitted in the −x direction toward the observer: k′^μ = (ω₀/c)(1, −1, 0, 0). The Lorentz boost relating S′ (moving at +v relative to S) to S is

注意符号约定。设光源以速度 v 沿 +x 方向远离观察者。在光源静止系 S′ 中，光沿 −x 方向向观察者发射：k′^μ = (ω₀/c)(1, −1, 0, 0)。S′ 相对 S 以 +v 运动，洛伦兹变换为

  k^0 = γ(k′^0 − β k′^1) = γ(ω₀/c)(1 − (−β)) = γ(ω₀/c)(1 + β).

Hmm — that gives a blueshift for a receding source, which is wrong. Let us redo carefully. Let S be the observer frame; the source moves at velocity +v along +x (receding). The transformation from source frame S′ to observer frame S: the source moves at +v in S, so we boost with velocity +v:

重新仔细推导。设 S 为观察者系，光源以 +v 沿 +x 方向运动（远离）。从源系 S′ 变换到观察者系 S，光源在 S 中以 +v 运动，以 +v 做变换：

  k^0 = γ(k′^0 + β k′^1).

In S′ the source emits toward the observer (−x direction), so k′^1 = −ω₀/c and k′^0 = ω₀/c:

在 S′ 中光源向观察者（−x 方向）发射，故 k′^1 = −ω₀/c，k′^0 = ω₀/c：

  k^0 = γ(ω₀/c)(1 + β · (−1)) = γ(ω₀/c)(1 − β) = (ω₀/c) · (1 − β)/√(1 − β²)
      = (ω₀/c) · (1 − β)/√((1−β)(1+β)) = (ω₀/c) · √(1−β)/√(1+β).

Since ω = c k^0,

由于 ω = c k^0，

  **f = f₀ √((1 − β)/(1 + β))**   (source receding, redshift). ✓

For an approaching source (v in −x direction, β → −β):

对于接近的光源（v 沿 −x 方向，β → −β）：

  **f = f₀ √((1 + β)/(1 − β))**   (source approaching, blueshift). ✓

**Step 3 — Low-speed limit.** For β ≪ 1, expand √((1−β)/(1+β)) ≈ (1 − β)(1 + β)^{−1/2}(1 − β)^{1/2}/(1 − β)^{1/2}:

**第 3 步 — 低速极限。** 对 β ≪ 1，展开：

  √((1 − β)/(1 + β)) ≈ (1 − β)(1 + β/2 + …) ≈ 1 − β − β/2 + … ≈ 1 − β + O(β²).

More carefully: let u = β:

更仔细地：令 u = β，

  (1 − u)^{1/2}(1 + u)^{−1/2} = (1 − ½u − ⅛u² − …)(1 − ½u + ⅜u² − …) ≈ 1 − u + O(u²).

So f ≈ f₀(1 − β) = f₀(1 − v/c), the classical Doppler formula for a receding source. The relativistic formula adds a time-dilation factor of γ at higher order — even a source moving purely transversely (β along ⊥) shows a **transverse Doppler redshift** f = f₀/γ, with no classical analogue.

故 f ≈ f₀(1 − β) = f₀(1 − v/c)，即光源远离时的经典多普勒公式。相对论公式在高阶引入时间膨胀因子——即使光源纯横向运动（β 沿垂直方向）也会产生**横向多普勒红移** f = f₀/γ，这在经典力学中无对应物。∎

---

## D. Why E² = (pc)² + (mc²)² and Not E = pc + mc² · 为何是 E² 而非 E 的线性关系

**Step 1 — Contrapositive: consistency of the invariant.** The result p^μ p_μ = (mc)² is Lorentz-invariant by construction: each factor p^μ transforms as a four-vector, so the scalar product is unchanged by any boost. In the rest frame **v** = 0, so **p** = 0 and E = mc², giving p^μ p_μ = (mc)² − 0 = (mc)². Since this holds in the rest frame and the quantity is invariant, it holds in every frame.

**第 1 步 — 逆向验证：不变量的自洽性。** 结果 p^μ p_μ = (mc)² 由构造本身保证洛伦兹不变：每个 p^μ 因子按四矢量变换，故标量积在任何变换下不变。在静止系中 **v** = 0，故 **p** = 0，E = mc²，得 p^μ p_μ = (mc)² − 0 = (mc)²。由于在静止系中成立且该量是不变的，它在每个参考系中都成立。

**Step 2 — For a massless particle.** Setting m = 0: p^μ p_μ = 0, so (E/c)² = |**p**|² giving **E = pc** — the energy-momentum relation for a photon or any massless particle.

**第 2 步 — 对无质量粒子。** 取 m = 0：p^μ p_μ = 0，故 (E/c)² = |**p**|²，得 **E = pc**——光子或任何无质量粒子的能量-动量关系。∎

---

*All results are consequences of special relativity: the invariance of ds² = c²dt² − dx² − dy² − dz², the definition of proper time, and the Lorentz-covariant structure of four-vectors.*

*所有结果都是狭义相对论的推论：ds² = c²dt² − dx² − dy² − dz² 的不变性、固有时的定义以及四矢量的洛伦兹协变结构。*

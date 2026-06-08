# Derivations — Module 1.16: Mechanical Waves & Acoustics
# 推导 — 模块 1.16：机械波与声学

> Companion to [Module 1.16](./module-1.16-mechanical-waves-acoustics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.16](./module-1.16-mechanical-waves-acoustics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Wave Speed on a String: c = √(T/μ) · 弦上的波速推导

**Claim.** A string with tension T (N) and linear mass density μ (kg/m) supports transverse waves satisfying the wave equation ∂²y/∂t² = (T/μ) ∂²y/∂x², with wave speed c = √(T/μ).

**命题。** 张力为 T（N）、线质量密度为 μ（kg/m）的弦支持横波，满足波动方程 ∂²y/∂t² = (T/μ) ∂²y/∂x²，波速 c = √(T/μ)。

**Step 1 — Isolate a string element.** Consider a small element of the string between positions x and x + Δx. Its mass is Δm = μ Δx. Under the small-angle (small-displacement) approximation, the tension T acts along the string, so the magnitude of the tension force at both ends is approximately T. The transverse displacement is y(x, t).

**第 1 步 — 隔离弦元。** 考虑弦在 x 到 x + Δx 之间的小元。其质量为 Δm = μ Δx。在小角度（小位移）近似下，张力 T 沿弦方向作用，两端张力的大小近似为 T。横向位移为 y(x, t)。

**Step 2 — Compute the net transverse force.** The transverse component of the tension at the right end (at x + Δx) is

**第 2 步 — 计算净横向力。** 右端（x + Δx 处）张力的横向分量为

  F_right = T sin θ(x + Δx) ≈ T tan θ(x + Δx) = T (∂y/∂x)|_{x+Δx}

and at the left end (pointing leftward, hence negative for rightward net):

左端（向左，故取负）：

  F_left = −T sin θ(x) ≈ −T (∂y/∂x)|_x.

The net upward force on the element is

元素所受净向上的力为

  ΔF = T [(∂y/∂x)|_{x+Δx} − (∂y/∂x)|_x].

**Step 3 — Apply Newton's second law.** Newton's second law in the transverse direction for the element is

**第 3 步 — 应用牛顿第二定律。** 对元素在横向应用牛顿第二定律：

  Δm · ∂²y/∂t² = ΔF
  μ Δx · ∂²y/∂t² = T [(∂y/∂x)|_{x+Δx} − (∂y/∂x)|_x].

Divide both sides by Δx and take the limit Δx → 0:

两边除以 Δx，取极限 Δx → 0：

  μ ∂²y/∂t² = T · ∂/∂x(∂y/∂x) = T ∂²y/∂x².

**Step 4 — Read off the wave speed.** Rearranging:

**第 4 步 — 读出波速。**

  ∂²y/∂t² = (T/μ) ∂²y/∂x².

Comparing with the standard wave equation ∂²y/∂t² = c² ∂²y/∂x², we identify

与标准波动方程 ∂²y/∂t² = c² ∂²y/∂x² 比较，得

  **c = √(T/μ)**. ∎

**Dimensional check:** [T] = N = kg·m/s², [μ] = kg/m, so [T/μ] = (kg·m/s²)/(kg/m) = m²/s², and √(T/μ) has units of m/s. ✓

**量纲检验：** [T] = N = kg·m/s²，[μ] = kg/m，故 [T/μ] = m²/s²，√(T/μ) 的单位为 m/s。✓

---

## B. D'Alembert's General Solution · 达朗贝尔通解

**Claim.** The general solution to the 1D wave equation ∂²y/∂t² = c² ∂²y/∂x² is y(x, t) = f(x − ct) + g(x + ct), where f and g are arbitrary twice-differentiable functions determined by initial conditions.

**命题。** 一维波动方程 ∂²y/∂t² = c² ∂²y/∂x² 的通解为 y(x, t) = f(x − ct) + g(x + ct)，其中 f 和 g 为由初始条件决定的任意二次可微函数。

**Step 1 — Change of variables.** Introduce the characteristic coordinates

**第 1 步 — 变量替换。** 引入特征坐标

  ξ = x − ct,   η = x + ct.

Then ∂/∂x = ∂ξ/∂x · ∂/∂ξ + ∂η/∂x · ∂/∂η = ∂/∂ξ + ∂/∂η, and ∂/∂t = (∂ξ/∂t)∂/∂ξ + (∂η/∂t)∂/∂η = −c ∂/∂ξ + c ∂/∂η.

则 ∂/∂x = ∂/∂ξ + ∂/∂η，∂/∂t = −c ∂/∂ξ + c ∂/∂η。

**Step 2 — Transform the wave equation.** Compute the second derivatives:

**第 2 步 — 变换波动方程。** 计算二阶导数：

  ∂²y/∂t² = c²(∂²y/∂ξ² − 2∂²y/∂ξ∂η + ∂²y/∂η²),
  c²∂²y/∂x² = c²(∂²y/∂ξ² + 2∂²y/∂ξ∂η + ∂²y/∂η²).

Subtracting (wave equation ∂²y/∂t² − c²∂²y/∂x² = 0):

作差（波动方程 ∂²y/∂t² − c²∂²y/∂x² = 0）：

  c²(∂²y/∂ξ² − 2∂²y/∂ξ∂η + ∂²y/∂η²) − c²(∂²y/∂ξ² + 2∂²y/∂ξ∂η + ∂²y/∂η²) = 0
  −4c² ∂²y/∂ξ∂η = 0
  ∂²y/∂ξ∂η = 0.

**Step 3 — Integrate.** Integrate once with respect to ξ: ∂y/∂η = G(η) for some function G. Integrate with respect to η: y = g(η) + f(ξ), where g′(η) = G(η). Substituting back:

**第 3 步 — 积分。** 对 ξ 积分：∂y/∂η = G(η)。对 η 积分：y = g(η) + f(ξ)。代回：

  **y(x, t) = f(x − ct) + g(x + ct)**. ∎

**Step 4 — Physical interpretation.** f(x − ct) represents a waveform of arbitrary shape traveling to the right at speed c (the argument x − ct is constant for an observer moving at +c). g(x + ct) represents a left-moving wave. Any initial disturbance splits into equal right- and left-moving parts.

**第 4 步 — 物理诠释。** f(x − ct) 表示以速度 c 向右传播的任意形状波形（以 +c 运动的观察者看到 x − ct 为常数）。g(x + ct) 表示向左传播的波。任意初始扰动分裂为等量的向右和向左传播部分。

---

## C. Standing-Wave Quantization: fₙ = nc/2L · 驻波量子化

**Claim.** A string of length L fixed at both ends supports standing waves only at discrete frequencies fₙ = nc/(2L), n = 1, 2, 3, …

**命题。** 两端固定、长度为 L 的弦只支持离散频率 fₙ = nc/(2L)（n = 1, 2, 3, …）的驻波。

**Step 1 — Boundary conditions.** The string is fixed at x = 0 and x = L, so y(0, t) = y(L, t) = 0 for all t.

**第 1 步 — 边界条件。** 弦在 x = 0 和 x = L 处固定，故对所有 t 有 y(0, t) = y(L, t) = 0。

**Step 2 — Harmonic (normal mode) ansatz.** Try a separable solution y(x, t) = X(x) T(t). Substituting into the wave equation:

**第 2 步 — 谐波（简正模式）假设。** 尝试可分离解 y(x, t) = X(x) T(t)。代入波动方程：

  X T″ = c² X″ T   ⟹   T″/T = c² X″/X = −ω² (constant, negative for oscillatory solutions).

This gives two ODEs: T″ + ω²T = 0 and X″ + k²X = 0, where k = ω/c.

得到两个常微分方程：T″ + ω²T = 0，X″ + k²X = 0，其中 k = ω/c。

**Step 3 — Spatial solution and boundary conditions.** The general spatial solution is X(x) = A sin(kx) + B cos(kx). Applying X(0) = 0 gives B = 0. Applying X(L) = 0 gives A sin(kL) = 0. For A ≠ 0 (non-trivial solution): sin(kL) = 0, so kL = nπ, hence

**第 3 步 — 空间解与边界条件。** 空间通解为 X(x) = A sin(kx) + B cos(kx)。由 X(0) = 0 得 B = 0。由 X(L) = 0 得 A sin(kL) = 0。对于非平凡解（A ≠ 0）：sin(kL) = 0，故 kL = nπ，从而

  kₙ = nπ/L,   n = 1, 2, 3, …

**Step 4 — Frequencies.** From the dispersion relation ω = ck:

**第 4 步 — 频率。** 由色散关系 ω = ck：

  ωₙ = c kₙ = cnπ/L,   fₙ = ωₙ/(2π) = **nc/(2L)**. ∎

**Step 5 — Physical form.** The n-th normal mode is

**第 5 步 — 物理形式。** 第 n 个简正模式为

  yₙ(x, t) = Aₙ sin(nπx/L) cos(ωₙ t + φₙ),

which is a superposition of left- and right-moving waves: sin(nπx/L)cos(ωₙt) = ½[sin(kₙx − ωₙt) + sin(kₙx + ωₙt)].

即左右传播波的叠加：sin(nπx/L)cos(ωₙt) = ½[sin(kₙx − ωₙt) + sin(kₙx + ωₙt)]。

---

## D. Sound Speed in a Fluid: c = √(B/ρ) · 流体中的声速推导

**Claim.** A sound wave in a fluid of equilibrium density ρ₀ and bulk modulus B (= −V dP/dV, the resistance to compression) propagates at speed c = √(B/ρ₀).

**命题。** 在平衡密度为 ρ₀、体积模量为 B（= −V dP/dV，对压缩的阻力）的流体中，声波以速度 c = √(B/ρ₀) 传播。

**Step 1 — Set up small-amplitude perturbations.** Let the equilibrium state have density ρ₀, pressure P₀. Introduce small perturbations: density ρ = ρ₀ + ρ′, pressure P = P₀ + P′, and fluid velocity **u** (small). The perturbations satisfy |ρ′/ρ₀| ≪ 1 and |**u**| ≪ c.

**第 1 步 — 建立小振幅扰动。** 设平衡态密度为 ρ₀，压强为 P₀。引入小扰动：密度 ρ = ρ₀ + ρ′，压强 P = P₀ + P′，流速 **u**（小量）。扰动满足 |ρ′/ρ₀| ≪ 1，|**u**| ≪ c。

**Step 2 — Linearized continuity equation.** The continuity equation ∂ρ/∂t + ∇·(ρ**u**) = 0 linearized (dropping the product ρ′**u**, which is second order) gives

**第 2 步 — 线性化连续性方程。** 连续性方程 ∂ρ/∂t + ∇·(ρ**u**) = 0 线性化（略去 ρ′**u** 的二阶项）：

  ∂ρ′/∂t + ρ₀ ∇·**u** = 0.

**Step 3 — Linearized Euler equation.** For an inviscid fluid with no body forces, Euler's equation is ρ(∂**u**/∂t + **u**·∇**u**) = −∇P. Linearizing (dropping ρ′∂**u**/∂t and the convective term **u**·∇**u** as second-order small):

**第 3 步 — 线性化欧拉方程。** 对无粘无体力流体，欧拉方程为 ρ(∂**u**/∂t + **u**·∇**u**) = −∇P。线性化（略去 ρ′∂**u**/∂t 及对流项）：

  ρ₀ ∂**u**/∂t = −∇P′.

**Step 4 — Relate P′ to ρ′ via the bulk modulus.** The bulk modulus B is defined by P′ = B ρ′/ρ₀ (for adiabatic compression, B = γP₀; for isothermal, B = P₀). So ∇P′ = (B/ρ₀) ∇ρ′.

**第 4 步 — 用体积模量联系 P′ 与 ρ′。** 体积模量 B 定义使得 P′ = B ρ′/ρ₀（绝热压缩时 B = γP₀；等温时 B = P₀）。故 ∇P′ = (B/ρ₀) ∇ρ′。

**Step 5 — Derive the wave equation for ρ′.** Take ∂/∂t of the continuity equation:

**第 5 步 — 推导 ρ′ 的波动方程。** 对连续性方程取 ∂/∂t：

  ∂²ρ′/∂t² + ρ₀ ∂(∇·**u**)/∂t = 0.

Take ∇· of the Euler equation:

对欧拉方程取 ∇·：

  ρ₀ ∇·(∂**u**/∂t) = −∇²P′ = −(B/ρ₀) ∇²ρ′.

Substituting:

代入：

  ∂²ρ′/∂t² = (B/ρ₀) ∇²ρ′.

This is the wave equation with wave speed

这是波动方程，波速为

  **c = √(B/ρ₀)**. ∎

**For an ideal gas:** P = P₀(ρ/ρ₀)^γ (adiabatic), so B = γP₀ = γρ₀RT/M (using the ideal gas law), giving c = √(γRT/M), which at T = 293 K, γ = 1.4, M = 29 g/mol gives c ≈ 343 m/s. ✓

**对理想气体：** P = P₀(ρ/ρ₀)^γ（绝热），B = γP₀ = γρ₀RT/M，故 c = √(γRT/M)。在 T = 293 K，γ = 1.4，M = 29 g/mol 时，c ≈ 343 m/s。✓

---

## E. The Doppler Formula · 多普勒公式推导

**Claim.** When a source emits frequency f₀ and moves at speed v_s toward the observer, and the observer moves at speed v_o toward the source, through a medium in which sound speed is c, the observed frequency is

**命题。** 当声源以频率 f₀ 发声，以速度 v_s 向观察者运动，观察者以速度 v_o 向声源运动，介质中声速为 c，则观察到的频率为

  f = f₀ (c + v_o) / (c − v_s).

**Step 1 — Wavelength in the medium.** The source emits one period every T₀ = 1/f₀ seconds. In this time the source moves forward v_s T₀. The wavefront emitted one period earlier is now c T₀ ahead. The wavelength in the medium is the distance between consecutive wavefronts:

**第 1 步 — 介质中的波长。** 声源每 T₀ = 1/f₀ 秒发出一个周期。在此时间内声源向前移动 v_s T₀。一个周期前发出的波前此时已在 c T₀ 之前。介质中相邻波前间距（波长）为

  λ = cT₀ − v_s T₀ = (c − v_s)/f₀.

(For a receding source replace −v_s with +v_s.)

（对于远离的声源，将 −v_s 替换为 +v_s。）

**Step 2 — Rate of wavefront arrival at the observer.** The observer moves toward the source at v_o, so the relative speed at which wavefronts approach the observer is c + v_o (sum of wave speed and observer speed toward source). The observed frequency is the rate of wavefront arrival:

**第 2 步 — 波前到达观察者的速率。** 观察者以 v_o 向声源运动，波前接近观察者的相对速度为 c + v_o。观察到的频率为

  f = (c + v_o)/λ = (c + v_o) · f₀/(c − v_s) = f₀ **(c + v_o)/(c − v_s)**. ∎

**Sign conventions:** Use + in numerator when observer moves toward source, − when moving away. Use − in denominator when source moves toward observer, + when moving away.

**符号约定：** 分子取 + 当观察者向声源运动，取 − 当远离。分母取 − 当声源向观察者运动，取 + 当远离。

**Note:** This is the classical Doppler formula for sound waves in a medium; it distinguishes between source motion and observer motion (unlike the relativistic Doppler formula for light, which depends only on relative velocity and which we derived in Module 1.14-derivations Section C).

**注：** 这是声波在介质中的经典多普勒公式；它区分声源运动和观察者运动（与光的相对论多普勒公式不同，后者仅依赖相对速度，见模块 1.14 推导文档第 C 节）。

---

## F. Phase Velocity vs Group Velocity: v_g = dω/dk · 相速度与群速度

**Claim.** For a dispersive medium (where ω is not simply proportional to k), the phase velocity v_p = ω/k and the group velocity v_g = dω/dk are in general different. The group velocity governs the propagation of energy and wave packets.

**命题。** 在色散介质（ω 与 k 不成简单正比）中，相速度 v_p = ω/k 与群速度 v_g = dω/dk 一般不同。群速度支配能量和波包的传播。

**Step 1 — Superpose two nearby plane waves.** Consider two waves of slightly different frequencies and wavenumbers:

**第 1 步 — 叠加两列频率相近的平面波。** 考虑频率和波数略有不同的两列波：

  y₁ = A cos(k₁ x − ω₁ t),   y₂ = A cos(k₂ x − ω₂ t),

with k₁ = k + Δk, k₂ = k − Δk, ω₁ = ω + Δω, ω₂ = ω − Δω (so Δk, Δω ≪ k, ω).

其中 k₁ = k + Δk，k₂ = k − Δk，ω₁ = ω + Δω，ω₂ = ω − Δω（Δk，Δω ≪ k，ω）。

**Step 2 — Use sum-to-product identity.** The sum y₁ + y₂:

**第 2 步 — 和差化积。** 叠加 y₁ + y₂：

  y = 2A cos(Δk · x − Δω · t) · cos(kx − ωt).

This is a **carrier wave** cos(kx − ωt) modulated by a slowly varying **envelope** cos(Δk · x − Δω · t).

这是**载波** cos(kx − ωt) 被缓变**包络** cos(Δk · x − Δω · t) 调制。

**Step 3 — Identify the two velocities.** 

**第 3 步 — 识别两个速度。**

- The carrier moves at the **phase velocity** v_p = ω/k (the speed at which a constant phase kx − ωt = const propagates: dx/dt = ω/k).

- 载波以**相速度** v_p = ω/k 传播（等相面 kx − ωt = const 的传播速度：dx/dt = ω/k）。

- The envelope moves at the **group velocity** v_g = Δω/Δk → **dω/dk** in the limit Δk → 0 (the speed at which a constant envelope phase Δk · x − Δω · t = const propagates: dx/dt = Δω/Δk).

- 包络以**群速度** v_g = Δω/Δk → **dω/dk**（Δk → 0 极限）传播（等包络相 Δk · x − Δω · t = const 的传播速度）。

**Step 4 — Energy and information travel at the group velocity.** In a non-dispersive medium ω = ck, so dω/dk = c = ω/k: phase and group velocities coincide. In a dispersive medium (e.g. water waves, optical fiber, plasma), v_g ≠ v_p. The energy and signal velocity equal v_g (proved by calculating the energy flux: the Poynting-like flux is proportional to dω/dk). For deep-water gravity waves (ω = √(gk)), v_g = ½ v_p — the envelope moves at half the phase speed.

**第 4 步 — 能量和信息以群速度传播。** 在无色散介质中 ω = ck，故 dω/dk = c = ω/k：相速度与群速度相同。在色散介质（如水波、光纤、等离子体）中，v_g ≠ v_p。能量和信号速度等于 v_g（通过计算能量通量证明：类坡印亭通量正比于 dω/dk）。对于深水重力波（ω = √(gk)），v_g = ½ v_p——包络以相速度的一半传播。∎

**Step 5 — Relation to the dispersion relation.** Expanding ω(k) in a Taylor series about k₀:

**第 5 步 — 与色散关系的联系。** 在 k₀ 处将 ω(k) 展开为泰勒级数：

  ω(k) = ω₀ + (dω/dk)₀ (k − k₀) + ½(d²ω/dk²)₀ (k − k₀)² + …

The first-order term gives the group velocity; the second-order term (group velocity dispersion, GVD) causes the wave packet to spread. In optical fibers, GVD limits the bandwidth-distance product and is compensated by dispersion-shifted fiber.

一阶项给出群速度；二阶项（群速度色散，GVD）导致波包展宽。在光纤中，GVD 限制带宽-距离乘积，可通过色散位移光纤补偿。∎

---

*The wave equation, d'Alembert's solution, boundary quantization, and the phase/group velocity distinction are the universal tools of wave physics — appearing identically in acoustic, elastic, electromagnetic, plasma, and quantum-mechanical waves throughout the curriculum.*

*波动方程、达朗贝尔解、边界量子化和相/群速度的区别是波动物理学的通用工具——在整个课程的声波、弹性波、电磁波、等离子体波和量子力学波中同样出现。*

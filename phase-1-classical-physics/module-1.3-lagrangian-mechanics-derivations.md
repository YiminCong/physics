# Derivations — Module 1.3: Lagrangian Mechanics
# 推导 — 模块 1.3：拉格朗日力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.3](./module-1.3-lagrangian-mechanics.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.3](./module-1.3-lagrangian-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Euler–Lagrange Equations from δS = 0 · 从 δS = 0 推导欧拉–拉格朗日方程

**Claim.** For a system with generalised coordinates q(t) and Lagrangian L(q, q̇, t), requiring the action S = ∫_{t₁}^{t₂} L dt to be stationary under all variations δq that vanish at the endpoints (δq(t₁) = δq(t₂) = 0) yields the Euler–Lagrange equation:

  d/dt (∂L/∂q̇) − ∂L/∂q = 0.

(For brevity we treat a single degree of freedom; the multi-coordinate case follows by applying the argument independently to each qᵢ.)

**命题。** 对于广义坐标为 q(t)、拉格朗日量为 L(q, q̇, t) 的系统，要求作用量 S = ∫_{t₁}^{t₂} L dt 在所有端点处为零的变分 δq（δq(t₁) = δq(t₂) = 0）下取驻值，可得欧拉–拉格朗日方程：

  d/dt (∂L/∂q̇) − ∂L/∂q = 0。

（简洁起见，我们处理单自由度情形；多坐标情形通过对每个 qᵢ 独立应用同一论证得到。）

**Step 1 — Perturb the path.** Let q(t) be the physical trajectory and consider a one-parameter family of nearby paths:

**第 1 步 — 扰动路径。** 设 q(t) 为物理轨迹，考虑一族邻近路径：

  q_ε(t) = q(t) + ε η(t),

where ε is a small real parameter and η(t) is an arbitrary smooth function satisfying the boundary conditions η(t₁) = η(t₂) = 0.

其中 ε 是小实数参数，η(t) 是满足边界条件 η(t₁) = η(t₂) = 0 的任意光滑函数。

**Step 2 — Expand the action to first order in ε.** The action evaluated on q_ε is:

**第 2 步 — 将作用量展开至 ε 的一阶。** 在 q_ε 上计算的作用量为：

  S(ε) = ∫_{t₁}^{t₂} L(q + εη, q̇ + εη̇, t) dt.

Taylor-expanding the integrand to first order in ε:

将被积函数关于 ε 一阶泰勒展开：

  L(q + εη, q̇ + εη̇, t) = L(q, q̇, t) + ε (∂L/∂q · η + ∂L/∂q̇ · η̇) + O(ε²).

**Step 3 — Stationarity condition.** Stationarity of S requires dS/dε|_{ε=0} = 0:

**第 3 步 — 驻值条件。** S 取驻值要求 dS/dε|_{ε=0} = 0：

  δS = ∫_{t₁}^{t₂} (∂L/∂q · η + ∂L/∂q̇ · η̇) dt = 0.

**Step 4 — Integration by parts on the second term.** The second term involves η̇. Integrate by parts, using u = ∂L/∂q̇ and dv = η̇ dt:

**第 4 步 — 对第二项分部积分。** 第二项含 η̇。令 u = ∂L/∂q̇，dv = η̇ dt，分部积分：

  ∫_{t₁}^{t₂} (∂L/∂q̇) η̇ dt = [(∂L/∂q̇) η]_{t₁}^{t₂} − ∫_{t₁}^{t₂} d/dt(∂L/∂q̇) · η dt.

**Step 5 — Boundary terms vanish.** The boundary term [(∂L/∂q̇) η]_{t₁}^{t₂} = 0 because η(t₁) = η(t₂) = 0 by assumption.

**第 5 步 — 边界项消失。** 边界项 [(∂L/∂q̇) η]_{t₁}^{t₂} = 0，因为由假设 η(t₁) = η(t₂) = 0。

**Step 6 — Combine into a single integral.** Substituting back:

**第 6 步 — 合并为单一积分。** 代回得：

  δS = ∫_{t₁}^{t₂} (∂L/∂q − d/dt(∂L/∂q̇)) η dt = 0.

**Step 7 — Apply the fundamental lemma of the calculus of variations.** Since δS = 0 for every arbitrary smooth η, the integrand must vanish identically (if it were nonzero at some point, we could choose η to have the same sign there, making the integral nonzero — a contradiction):

**第 7 步 — 应用变分法基本引理。** 由于对任意光滑 η 均有 δS = 0，被积函数必须恒等于零（若在某点不为零，可选取 η 在该点与之同号，使积分不为零——矛盾）：

  **∂L/∂q − d/dt(∂L/∂q̇) = 0**, i.e. **d/dt(∂L/∂q̇) − ∂L/∂q = 0.** ∎

  **∂L/∂q − d/dt(∂L/∂q̇) = 0**，即 **d/dt(∂L/∂q̇) − ∂L/∂q = 0。** ∎

---

## B. Equivalence to Newton's Second Law for L = T − V · L = T − V 时与牛顿第二定律的等价性

**Claim.** For a particle in Cartesian coordinates with L = T − V = ½m ẋ² − V(x), the Euler–Lagrange equation is equivalent to Newton's second law m ẍ = −dV/dx.

**命题。** 对于笛卡尔坐标中的粒子，L = T − V = ½m ẋ² − V(x)，欧拉–拉格朗日方程等价于牛顿第二定律 m ẍ = −dV/dx。

**Step 1 — Compute the partial derivatives.** With L = ½mẋ² − V(x):

**第 1 步 — 计算偏导数。** 对于 L = ½mẋ² − V(x)：

  ∂L/∂ẋ = mẋ,   ∂L/∂x = −dV/dx.

**Step 2 — Apply the Euler–Lagrange equation.** The E-L equation d/dt(∂L/∂ẋ) − ∂L/∂x = 0 gives:

**第 2 步 — 应用欧拉–拉格朗日方程。** 欧拉–拉格朗日方程 d/dt(∂L/∂ẋ) − ∂L/∂x = 0 给出：

  d/dt(mẋ) − (−dV/dx) = 0   ⟹   mẍ + dV/dx = 0   ⟹   **mẍ = −dV/dx = F.** ∎

  d/dt(mẋ) − (−dV/dx) = 0   ⟹   mẍ + dV/dx = 0   ⟹   **mẍ = −dV/dx = F。** ∎

This confirms that the Euler–Lagrange equations are precisely Newton's equations in disguise when L = T − V.

这证实了当 L = T − V 时，欧拉–拉格朗日方程恰好是牛顿方程的另一种形式。

---

## C. The Simple Pendulum via Euler–Lagrange · 用欧拉–拉格朗日方程求解单摆

**Claim.** For a simple pendulum of length ℓ and mass m, the Euler–Lagrange equation with generalised coordinate θ gives the exact equation of motion ℓθ̈ + g sin θ = 0.

**命题。** 对于摆长为 ℓ、质量为 m 的单摆，以 θ 为广义坐标的欧拉–拉格朗日方程给出精确运动方程 ℓθ̈ + g sin θ = 0。

**Step 1 — Identify the kinetic and potential energies.** The bob moves on a circle of radius ℓ. Its speed is ℓθ̇, so:

**第 1 步 — 确定动能和势能。** 摆球在半径为 ℓ 的圆上运动，速度为 ℓθ̇，故：

  T = ½m(ℓθ̇)² = ½mℓ²θ̇².

Taking the pivot as the reference level, the height of the bob below the pivot is ℓ cos θ, so the height above the lowest point is ℓ(1 − cos θ):

以转轴为参考零点，摆球在最低点以上的高度为 ℓ(1 − cos θ)：

  V = mgℓ(1 − cos θ).

**Step 2 — Write the Lagrangian.** 

**第 2 步 — 写出拉格朗日量。**

  L = T − V = ½mℓ²θ̇² − mgℓ(1 − cos θ).

**Step 3 — Compute the required partial derivatives.**

**第 3 步 — 计算所需的偏导数。**

  ∂L/∂θ̇ = mℓ²θ̇,   d/dt(∂L/∂θ̇) = mℓ²θ̈.

  ∂L/∂θ = −mgℓ sin θ.

**Step 4 — Apply the Euler–Lagrange equation.** d/dt(∂L/∂θ̇) − ∂L/∂θ = 0 gives:

**第 4 步 — 应用欧拉–拉格朗日方程。** d/dt(∂L/∂θ̇) − ∂L/∂θ = 0 给出：

  mℓ²θ̈ − (−mgℓ sin θ) = 0   ⟹   mℓ²θ̈ + mgℓ sin θ = 0.

Dividing by mℓ:

除以 mℓ：

  **ℓθ̈ + g sin θ = 0.** ∎

  **ℓθ̈ + g sin θ = 0。** ∎

**Step 5 — Small-angle approximation.** For small θ, sin θ ≈ θ, giving ℓθ̈ + gθ = 0, i.e. θ̈ = −(g/ℓ)θ. This is simple harmonic motion with angular frequency ω₀ = √(g/ℓ) and period T = 2π√(ℓ/g), independent of mass and (for small amplitudes) of amplitude.

**第 5 步 — 小角近似。** 对于小 θ，sin θ ≈ θ，得 ℓθ̈ + gθ = 0，即 θ̈ = −(g/ℓ)θ。这是角频率 ω₀ = √(g/ℓ)、周期 T = 2π√(ℓ/g) 的简谐运动，与质量无关，（在小振幅下）与振幅无关。

---

## D. Cyclic Coordinates and Conserved Momenta · 循环坐标与守恒动量

**Claim.** If ∂L/∂qᵢ = 0 (coordinate qᵢ does not appear explicitly in L), then the conjugate momentum pᵢ = ∂L/∂q̇ᵢ is conserved: dpᵢ/dt = 0.

**命题。** 若 ∂L/∂qᵢ = 0（坐标 qᵢ 不显含于 L 中），则共轭动量 pᵢ = ∂L/∂q̇ᵢ 守恒：dpᵢ/dt = 0。

**Proof.** The Euler–Lagrange equation for qᵢ states:

**证明。** qᵢ 的欧拉–拉格朗日方程为：

  d/dt(∂L/∂q̇ᵢ) = ∂L/∂qᵢ.

If ∂L/∂qᵢ = 0, this becomes dpᵢ/dt = d/dt(∂L/∂q̇ᵢ) = 0, so pᵢ = const. ∎

若 ∂L/∂qᵢ = 0，则变为 dpᵢ/dt = d/dt(∂L/∂q̇ᵢ) = 0，故 pᵢ = 常数。∎

**Example.** For a particle in 2D polar coordinates (r, φ) with central potential V(r): L = ½m(ṙ² + r²φ̇²) − V(r). Since ∂L/∂φ = 0, the conjugate momentum pφ = ∂L/∂φ̇ = mr²φ̇ is conserved — this is the angular momentum L = mr²φ̇.

**例。** 对于极坐标 (r, φ) 中处于有心势 V(r) 的粒子：L = ½m(ṙ² + r²φ̇²) − V(r)。由于 ∂L/∂φ = 0，共轭动量 pφ = ∂L/∂φ̇ = mr²φ̇ 守恒——这就是角动量 L = mr²φ̇。

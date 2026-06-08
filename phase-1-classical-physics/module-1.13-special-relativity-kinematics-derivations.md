# Derivations — Module 1.13: Special Relativity — Kinematics
# 推导 — 模块 1.13：狭义相对论——运动学

> Companion to [Module 1.13](./module-1.13-special-relativity-kinematics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.13](./module-1.13-special-relativity-kinematics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Deriving the Lorentz Transformation from the Two Postulates · 从两个假设推导洛伦兹变换

**Claim.** From (1) the principle of relativity and (2) the constancy of c, together with the requirement of linearity (homogeneous flat spacetime), the unique coordinate transformation between two inertial frames S and S′ (with S′ moving at velocity v along the x-axis) is the Lorentz transformation:

**命题。** 从 (1) 相对性原理和 (2) 光速不变性，加上线性要求（均匀平直时空），两个惯性系 S 和 S′（S′ 沿 x 轴以速度 v 运动）之间的唯一坐标变换是洛伦兹变换：

  x′ = γ(x − vt),   t′ = γ(t − vx/c²),   y′ = y,   z′ = z,   γ = 1/√(1 − v²/c²).

**Step 1 — Linearity and the form of the transformation.** The principle of relativity requires that the transformation be linear (straight worldlines in one frame must appear straight in all frames; nonlinear transformations would imply a preferred point in spacetime). For motion along x, the transverse coordinates are unaffected by symmetry (y′ = y, z′ = z — if they were not equal, we could distinguish "moving left" from "moving right" by the sign of the transverse change, violating isotropy). The most general linear transformation is:

**第 1 步 — 线性与变换形式。** 相对性原理要求变换是线性的（一个参考系中的直世界线在所有参考系中必须显示为直线；非线性变换意味着时空中存在特殊点）。对于沿 x 方向的运动，横向坐标由对称性不受影响（y′ = y，z′ = z——若不相等，我们可以通过横向变化的符号区分"向左运动"与"向右运动"，违反各向同性）。最一般的线性变换为：

  x′ = A(x − vt),
  t′ = B t + C x,

for constants A, B, C to be determined. (The form x′ = A(x − vt) ensures that the origin of S′ (x′ = 0) moves at velocity v in S, as required.)

待定常数 A、B、C。（形式 x′ = A(x − vt) 确保 S′ 的原点（x′ = 0）在 S 中以速度 v 运动，符合要求。）

**Step 2 — Apply the constancy of c.** A light pulse emitted at the origin at t = 0 propagates as x = ct in S, and as x′ = ct′ in S′ (the speed of light is the same in both frames). Substituting into our ansatz:

**第 2 步 — 应用光速不变性。** 在 t = 0 时从原点发出的光脉冲，在 S 中传播为 x = ct，在 S′ 中传播为 x′ = ct′（光速在两个参考系中相同）。代入我们的假设：

  x′ = A(ct − vt) = A(c − v)t,
  t′ = Bt + C(ct) = (B + Cc)t.

For x′ = ct′:  A(c − v)t = c(B + Cc)t, so:

为使 x′ = ct′：A(c − v)t = c(B + Cc)t，故：

  A(c − v) = c(B + Cc).   ... (*)

Now apply the same condition for a pulse in the −x direction: x = −ct, x′ = −ct′. Substituting:

现在对 −x 方向的光脉冲应用相同条件：x = −ct，x′ = −ct′。代入：

  x′ = A(−ct − vt) = −A(c + v)t,
  t′ = Bt + C(−ct) = (B − Cc)t.

For x′ = −ct′:  −A(c + v)t = −c(B − Cc)t, so:

为使 x′ = −ct′：−A(c + v)t = −c(B − Cc)t，故：

  A(c + v) = c(B − Cc).   ... (**)

**Step 3 — Solve for B, C in terms of A.** Adding (*) and (**):

**第 3 步 — 用 A 解出 B、C。** 将 (*) 和 (**) 相加：

  2Ac = 2Bc   →   B = A.

Subtracting (**) from (*):

从 (*) 中减去 (**)：

  −2Av = 2Acc   →   C = −Av/c².

So the transformation reads:

故变换变为：

  x′ = A(x − vt),
  t′ = A(t − vx/c²).

**Step 4 — Determine A from the inverse transformation.** By the principle of relativity, the inverse transformation (from S′ to S) must have the same form with v → −v:

**第 4 步 — 由逆变换确定 A。** 由相对性原理，逆变换（从 S′ 到 S）必须具有相同形式，将 v 替换为 −v：

  x = A(x′ + vt′),
  t = A(t′ + vx′/c²).

Substitute x′ and t′ from Step 3 into the expression for x:

将第 3 步中的 x′ 和 t′ 代入 x 的表达式：

  x = A[A(x − vt) + v A(t − vx/c²)] = A²[x − vt + vt − v²x/c²] = A²[x(1 − v²/c²)].

For this to equal x for all x, we need A² (1 − v²/c²) = 1, i.e.:

为使这对所有 x 等于 x，需要 A² (1 − v²/c²) = 1，即：

  A = 1/√(1 − v²/c²) = γ.   (taking A > 0 for the identity to recover at v = 0)

（取 A > 0，使 v = 0 时还原为恒等变换。）

**Step 5 — The Lorentz transformation.** Substituting A = γ:

**第 5 步 — 洛伦兹变换。** 代入 A = γ：

  **x′ = γ(x − vt),   t′ = γ(t − vx/c²),   y′ = y,   z′ = z.**  ∎

When v ≪ c, γ → 1 and the transformation reduces to the Galilean x′ = x − vt, t′ = t, recovering Newtonian mechanics in the low-speed limit.

当 v ≪ c 时，γ → 1，变换退化为伽利略变换 x′ = x − vt，t′ = t，在低速极限下恢复牛顿力学。

---

## B. Time Dilation · 时间膨胀

**Claim.** A clock at rest in S′ measures a proper time interval Δτ between two events at the same spatial position in S′. In frame S, the time interval is Δt = γ Δτ ≥ Δτ.

**命题。** 静止在 S′ 中的时钟在 S′ 中同一空间位置的两个事件之间测量固有时间间隔 Δτ。在参考系 S 中，时间间隔为 Δt = γ Δτ ≥ Δτ。

**Step 1 — Two events at the same place in S′.** Let two events occur at x′ = 0 (the origin of S′, i.e., the location of the clock) at times t′₁ and t′₂. The proper time is Δτ = t′₂ − t′₁.

**第 1 步 — S′ 中同一地点的两个事件。** 设两个事件发生在 x′ = 0（S′ 的原点，即时钟所在处），时刻分别为 t′₁ 和 t′₂。固有时为 Δτ = t′₂ − t′₁。

**Step 2 — Find the corresponding times in S.** Use the inverse Lorentz transformation t = γ(t′ + vx′/c²). Since x′ = 0:

**第 2 步 — 求 S 中对应的时刻。** 利用逆洛伦兹变换 t = γ(t′ + vx′/c²)。由于 x′ = 0：

  t₁ = γ t′₁,   t₂ = γ t′₂.

Therefore: Δt = t₂ − t₁ = γ(t′₂ − t′₁) = **γ Δτ.** Since γ ≥ 1, Δt ≥ Δτ: moving clocks run slow. ∎

因此：Δt = t₂ − t₁ = γ(t′₂ − t′₁) = **γ Δτ。** 由于 γ ≥ 1，Δt ≥ Δτ：运动的时钟走得慢。∎

---

## C. Length Contraction · 长度收缩

**Claim.** A rod at rest in S′ has proper length L₀ (= x′₂ − x′₁ with the endpoints measured at the same t′). In frame S, the simultaneous measurement of the rod's endpoints gives length L = L₀/γ ≤ L₀.

**命题。** 静止在 S′ 中的杆具有固有长度 L₀（= x′₂ − x′₁，两端点在同一 t′ 时刻测量）。在参考系 S 中，同时测量杆的两端点给出长度 L = L₀/γ ≤ L₀。

**Step 1 — Simultaneous measurement in S.** To measure the length of a moving rod in S, one must record the positions of both ends at the same time t in S. Let the two endpoints be at (x₁, t) and (x₂, t) in S, so L = x₂ − x₁. The Lorentz transformation gives:

**第 1 步 — S 中的同时测量。** 要在 S 中测量运动杆的长度，必须在 S 中同一时刻 t 记录两端点的位置。设两端点在 S 中分别为 (x₁, t) 和 (x₂, t)，故 L = x₂ − x₁。洛伦兹变换给出：

  x′₁ = γ(x₁ − vt),   x′₂ = γ(x₂ − vt).

Subtracting: L₀ = x′₂ − x′₁ = γ(x₂ − x₁) = γ L.

相减：L₀ = x′₂ − x′₁ = γ(x₂ − x₁) = γ L。

Therefore: **L = L₀/γ.** Since γ ≥ 1, L ≤ L₀: moving rods contract along the direction of motion. ∎

因此：**L = L₀/γ。** 由于 γ ≥ 1，L ≤ L₀：运动的杆沿运动方向收缩。∎

Note: Contraction only occurs along the direction of motion; transverse dimensions are unchanged (y′ = y, z′ = z from Step 1 of Section A).

注意：收缩只发生在运动方向上；横向尺寸不变（由 A 节第 1 步 y′ = y，z′ = z）。

---

## D. Relativistic Velocity Addition · 相对论速度叠加

**Claim.** If an object moves with velocity u′ in frame S′ (along the x-axis), and S′ moves at velocity v relative to S, then the velocity of the object in S is:

**命题。** 若物体在参考系 S′ 中以速度 u′（沿 x 轴）运动，而 S′ 相对 S 以速度 v 运动，则物体在 S 中的速度为：

  u = (u′ + v) / (1 + u′v/c²).

**Step 1 — Express the object's coordinates using the Lorentz transformation.** In S′ the object has position x′ = u′ t′ (moving at velocity u′). We want u = dx/dt in S. Using the inverse transformation:

**第 1 步 — 用洛伦兹变换表示物体的坐标。** 在 S′ 中物体坐标为 x′ = u′ t′（以速度 u′ 运动）。我们想求 S 中的 u = dx/dt。利用逆变换：

  x = γ(x′ + vt′),   t = γ(t′ + vx′/c²).

Substituting x′ = u′t′:

代入 x′ = u′t′：

  x = γ(u′t′ + vt′) = γ(u′ + v)t′,
  t = γ(t′ + vu′t′/c²) = γ(1 + u′v/c²)t′.

**Step 2 — Divide to get u = dx/dt.** Dividing x by t (both are proportional to t′, which cancels):

**第 2 步 — 相除得 u = dx/dt。** 将 x 除以 t（两者都正比于 t′，约去）：

  u = x/t = γ(u′ + v)t′ / [γ(1 + u′v/c²)t′] = **(u′ + v) / (1 + u′v/c²).** ∎

**Step 3 — Check limiting cases.**
- (a) If u′ = c: u = (c + v)/(1 + v/c) = c(c + v)/(c + v) = **c**. Light always moves at c. ✓
- (b) If u′, v ≪ c: u ≈ u′ + v (Galilean velocity addition recovered). ✓
- (c) If u′ = v = 0.9c: u = (0.9c + 0.9c)/(1 + 0.81) = 1.8c/1.81 ≈ 0.994c < c. Superluminal speeds are impossible. ✓

**第 3 步 — 验证极限情形。**
- (a) 若 u′ = c：u = (c + v)/(1 + v/c) = c(c + v)/(c + v) = **c**。光总以 c 运动。✓
- (b) 若 u′, v ≪ c：u ≈ u′ + v（恢复伽利略速度叠加）。✓
- (c) 若 u′ = v = 0.9c：u = (0.9c + 0.9c)/(1 + 0.81) = 1.8c/1.81 ≈ 0.994c < c。超光速不可能。✓

---

## E. Invariance of the Spacetime Interval s² = (ct)² − x² · 时空间隔 s² = (ct)² − x² 的不变性

**Claim.** For any two events, the quantity s² = (c Δt)² − (Δx)² − (Δy)² − (Δz)² takes the same value in all inertial frames.

**命题。** 对任意两个事件，量 s² = (c Δt)² − (Δx)² − (Δy)² − (Δz)² 在所有惯性系中取相同值。

**Step 1 — Consider the interval in frame S.** For two events with separations Δx, Δt (setting Δy = Δz = 0 for simplicity):

**第 1 步 — 在参考系 S 中考察间隔。** 对于分隔为 Δx，Δt 的两个事件（为简单起见设 Δy = Δz = 0）：

  s² = (c Δt)² − (Δx)².

**Step 2 — Compute in frame S′ using the Lorentz transformation.** Applying the Lorentz transformation to the differences Δx′ = γ(Δx − v Δt) and Δt′ = γ(Δt − v Δx/c²):

**第 2 步 — 用洛伦兹变换在 S′ 中计算。** 将洛伦兹变换应用于差分 Δx′ = γ(Δx − v Δt)，Δt′ = γ(Δt − v Δx/c²)：

  (c Δt′)² − (Δx′)² = c² γ²(Δt − v Δx/c²)² − γ²(Δx − v Δt)².

**Step 3 — Expand and simplify.** Expand both squares:

**第 3 步 — 展开并化简。** 展开两个平方项：

  = γ²[c²(Δt)² − 2v Δx Δt + v²(Δx)²/c² − (Δx)² + 2v Δx Δt − v²(Δt)²]
  = γ²[c²(Δt)² + v²(Δx)²/c² − (Δx)² − v²(Δt)²]
  = γ²[c²(Δt)²(1 − v²/c²) − (Δx)²(1 − v²/c²)]
  = γ²(1 − v²/c²)[(c Δt)² − (Δx)²].

Since γ² = 1/(1 − v²/c²), we get γ²(1 − v²/c²) = 1. Therefore:

由于 γ² = 1/(1 − v²/c²)，故 γ²(1 − v²/c²) = 1。因此：

  **(c Δt′)² − (Δx′)² = (c Δt)² − (Δx)².** ∎

The spacetime interval s² is Lorentz-invariant. This is the Minkowski **metric**: every Lorentz transformation preserves s².

时空间隔 s² 是洛伦兹不变的。这是闵可夫斯基**度规**：每个洛伦兹变换都保持 s²。

**Step 4 — Physical consequences.** The sign of s² is invariant:
- s² > 0 (timelike): a frame exists where Δx′ = 0 (events at the same place); the interval is then purely temporal: s = c Δτ where Δτ = proper time. Causally connected.
- s² = 0 (lightlike / null): connected by a light signal; |Δx| = c|Δt| in all frames.
- s² < 0 (spacelike): a frame exists where Δt′ = 0 (simultaneous events); no causal connection.

**第 4 步 — 物理推论。** s² 的符号是不变量：
- s² > 0（类时）：存在一个参考系使 Δx′ = 0（事件在同一地点）；间隔此时纯为时间：s = c Δτ，Δτ = 固有时。有因果联系。
- s² = 0（类光/零）：由光信号相连；所有参考系中 |Δx| = c|Δt|。
- s² < 0（类空）：存在一个参考系使 Δt′ = 0（同时发生的事件）；无因果联系。

---

## F. Relativity of Simultaneity · 同时性的相对性

**Claim.** Two events that are simultaneous in S (Δt = 0) but spatially separated (Δx ≠ 0) are not simultaneous in S′: Δt′ = −γ v Δx/c² ≠ 0.

**命题。** 在 S 中同时（Δt = 0）但空间分隔（Δx ≠ 0）的两个事件，在 S′ 中不同时：Δt′ = −γ v Δx/c² ≠ 0。

**Step 1 — Apply the Lorentz time transformation.** With Δt = 0:

**第 1 步 — 应用洛伦兹时间变换。** 令 Δt = 0：

  Δt′ = γ(Δt − v Δx/c²) = γ(0 − v Δx/c²) = **−γ v Δx/c².** ∎

This is not zero unless Δx = 0 or v = 0. The order of events can even be reversed: if event A is before B in S, the sign of Δt′ depends on the sign of v Δx. For spacelike-separated events, the time ordering is frame-dependent. For timelike-separated events (where one can causally influence the other), the time ordering is preserved in all frames (since for timelike separation (c Δt)² > (Δx)², so Δt′ = γ(Δt − v Δx/c²) always has the same sign as Δt when |v| < c).

除非 Δx = 0 或 v = 0，否则此结果不为零。事件的顺序甚至可以颠倒：若在 S 中事件 A 先于 B，Δt′ 的符号取决于 v Δx 的符号。对于类空分隔的事件，时间顺序依赖于参考系。对于类时分隔的事件（其中一个可以因果影响另一个），时间顺序在所有参考系中保持不变（因为类时分隔有 (c Δt)² > (Δx)²，所以当 |v| < c 时 Δt′ = γ(Δt − v Δx/c²) 与 Δt 的符号始终相同）。

---

*The Lorentz transformation, invariant interval, and velocity addition derived here are the kinematic foundation for all relativistic physics: four-vector dynamics (Module 1.14), covariant electrodynamics (Module 1.15), and quantum field theory (Phase 6). The invariant s² generalises to the curved spacetime metric g_μν ds² in general relativity (Phase 7).*

*此处推导的洛伦兹变换、不变间隔和速度叠加是所有相对论物理的运动学基础：四矢量动力学（模块 1.14）、协变电动力学（模块 1.15）和量子场论（第 6 阶段）。不变量 s² 推广为广义相对论（第 7 阶段）中弯曲时空度规 g_μν ds²。*

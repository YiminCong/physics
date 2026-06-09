# Derivations — Module 1.19: Nonlinear Dynamics & Chaos
# 推导 — 模块 1.19：非线性动力学与混沌

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.19](./module-1.19-nonlinear-dynamics-chaos.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.19](./module-1.19-nonlinear-dynamics-chaos.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Linearization About a Fixed Point and Jacobian Classification · 不动点线性化与雅可比矩阵分类

**Claim.** For a smooth dynamical system ẋ = **F**(**x**) with a fixed point **x*** (F(**x***) = 0), the local stability is determined by the eigenvalues of the Jacobian matrix J_{ij} = ∂F_i/∂x_j evaluated at **x***. The classification depends on the eigenvalues λ₁, λ₂ (in 2D).

**命题。** 对于具有不动点 **x***（F(**x***) = 0）的光滑动力系统 ẋ = **F**(**x**)，局部稳定性由在 **x*** 处计算的雅可比矩阵 J_{ij} = ∂F_i/∂x_j 的特征值决定。分类依赖于特征值 λ₁, λ₂（二维情形）。

**Step 1 — Taylor expansion.** Let **x** = **x*** + **δx** where **δx** is a small perturbation. Taylor-expand **F** about **x***:

**第 1 步 — 泰勒展开。** 令 **x** = **x*** + **δx**，其中 **δx** 为小扰动。在 **x*** 处展开 **F**：

  ẋ = **F**(**x*** + **δx**) = **F**(**x***) + J **δx** + O(|**δx**|²) = J **δx** + O(|**δx**|²).

For small **δx**, drop the quadratic terms:

对小 **δx**，略去二次项：

  d(**δx**)/dt = J **δx**,   where J_{ij} = ∂F_i/∂x_j|_{**x***}.

This is the **linearized system**.

这就是**线性化方程组**。

**Step 2 — Solution of the linearized system.** The general solution is **δx**(t) = Σ_k c_k **v**_k e^{λ_k t}, where λ_k are eigenvalues and **v**_k are eigenvectors of J. The behavior as t → ∞ is determined by the eigenvalue with the largest real part.

**第 2 步 — 线性化方程组的解。** 通解为 **δx**(t) = Σ_k c_k **v**_k e^{λ_k t}，其中 λ_k 为 J 的特征值，**v**_k 为特征向量。当 t → ∞ 时，行为由实部最大的特征值决定。

**Step 3 — Classification in 2D.** For a 2D system with Jacobian J having eigenvalues λ₁, λ₂ (which may be complex), let τ = tr J = λ₁ + λ₂ and Δ = det J = λ₁ λ₂. Then λ = (τ ± √(τ² − 4Δ))/2.

**第 3 步 — 二维分类。** 对二维系统，雅可比矩阵 J 的特征值 λ₁, λ₂（可为复数），令 τ = tr J = λ₁ + λ₂，Δ = det J = λ₁ λ₂。则 λ = (τ ± √(τ² − 4Δ))/2。

The classification of the fixed point:

不动点的分类：

- **Δ < 0:** Eigenvalues real with opposite sign → **saddle point** (unstable in one direction, stable in the other; the invariant manifold structure creates heteroclinic/homoclinic orbits).

- **Δ < 0：** 特征值实数且异号 → **鞍点**（一方向不稳定，另一方向稳定；不变流形结构产生异宿/同宿轨道）。

- **Δ > 0, τ² > 4Δ:** Both eigenvalues real with the same sign → **node** (stable if τ < 0, unstable if τ > 0; trajectories approach/leave along straight lines).

- **Δ > 0，τ² > 4Δ：** 特征值均为实数且同号 → **结点**（τ < 0 稳定，τ > 0 不稳定；轨迹沿直线趋近/远离）。

- **Δ > 0, τ² < 4Δ:** Complex conjugate eigenvalues λ = α ± iβ → **spiral** (stable focus if α = τ/2 < 0, unstable focus if τ > 0; trajectories spiral in or out).

- **Δ > 0，τ² < 4Δ：** 复共轭特征值 λ = α ± iβ → **螺旋点**（τ/2 < 0 为稳定焦点，τ > 0 为不稳定焦点；轨迹螺旋进入或远离）。

- **τ = 0, Δ > 0:** Purely imaginary eigenvalues → **centre** (marginally stable; linearization cannot determine stability of the nonlinear system).

- **τ = 0，Δ > 0：** 纯虚特征值 → **中心**（边际稳定；线性化无法确定非线性系统的稳定性）。

**Step 4 — Example: damped pendulum.** For θ̈ + γθ̇ + ω₀² sin θ = 0, write as a system (θ̇ = v, v̇ = −γv − ω₀² sin θ). Fixed points: (0, 0) (bottom, stable) and (π, 0) (top, unstable).

**第 4 步 — 例：阻尼单摆。** 对 θ̈ + γθ̇ + ω₀² sin θ = 0，写为系统（θ̇ = v，v̇ = −γv − ω₀² sin θ）。不动点：(0, 0)（底部，稳定）和 (π, 0)（顶部，不稳定）。

At (0, 0): J = [[0, 1], [−ω₀², −γ]], τ = −γ < 0, Δ = ω₀² > 0 → stable spiral (if γ² < 4ω₀²) or stable node.

在 (0, 0)：J = [[0, 1], [−ω₀², −γ]]，τ = −γ < 0，Δ = ω₀² > 0 → 稳定螺旋（若 γ² < 4ω₀²）或稳定结点。

At (π, 0): J = [[0, 1], [+ω₀², −γ]], Δ = −ω₀² < 0 → **saddle point** (unstable). ∎

在 (π, 0)：J = [[0, 1], [+ω₀², −γ]]，Δ = −ω₀² < 0 → **鞍点**（不稳定）。∎

---

## B. The Logistic Map: Fixed Points, Period-Doubling, and Stability |f′| = 1 · 逻辑斯蒂映射：不动点、倍周期与稳定性条件

**Claim.** The logistic map xₙ₊₁ = f(xₙ) = r xₙ(1 − xₙ) has fixed points x* = 0 and x* = 1 − 1/r. Period-2 orbits emerge via a pitchfork bifurcation when |f′(x*)| = 1. The period-doubling cascade repeats at each subsequent bifurcation.

**命题。** 逻辑斯蒂映射 xₙ₊₁ = f(xₙ) = r xₙ(1 − xₙ) 有不动点 x* = 0 和 x* = 1 − 1/r。当 |f′(x*)| = 1 时，通过叉式分岔出现周期-2 轨道。倍周期级联在每个后续分岔处重复。

**Step 1 — Find the fixed points.** A fixed point satisfies x* = f(x*) = r x*(1 − x*):

**第 1 步 — 求不动点。** 不动点满足 x* = f(x*) = r x*(1 − x*)：

  x*(1 − r(1 − x*)) = 0  ⟹  x* = 0  or  1 = r(1 − x*)  ⟹  x* = 1 − 1/r.

So the non-trivial fixed point is **x* = (r − 1)/r**, existing for r > 1.

非平凡不动点为 **x* = (r − 1)/r**，在 r > 1 时存在。

**Step 2 — Stability of the fixed points.** For a map xₙ₊₁ = f(xₙ), a fixed point x* is **stable** if |f′(x*)| < 1 and **unstable** if |f′(x*)| > 1 (small deviations δₙ evolve as δₙ = (f′(x*))ⁿ δ₀, which decays iff |f′(x*)| < 1).

**第 2 步 — 不动点的稳定性。** 对映射 xₙ₊₁ = f(xₙ)，不动点 x* **稳定**当且仅当 |f′(x*)| < 1；**不稳定**当 |f′(x*)| > 1（小偏差 δₙ = (f′(x*))ⁿ δ₀，当 |f′(x*)| < 1 时衰减）。

Compute f′(x) = r(1 − 2x). At x* = 1 − 1/r:

计算 f′(x) = r(1 − 2x)。在 x* = 1 − 1/r 处：

  f′(x*) = r(1 − 2(1 − 1/r)) = r(−1 + 2/r) = 2 − r.

So the non-trivial fixed point is stable when |2 − r| < 1, i.e. **1 < r < 3**.

故非平凡不动点在 |2 − r| < 1 时稳定，即 **1 < r < 3**。

**Step 3 — Bifurcation at r = 3 (|f′| = 1 condition).** At r = 3, |f′(x*)| = |2 − 3| = 1: the fixed point loses stability. This is the condition for a **period-doubling bifurcation**. At this critical point a period-2 orbit (2-cycle) emerges from the fixed point.

**第 3 步 — r = 3 处的分岔（|f′| = 1 条件）。** 在 r = 3 处，|f′(x*)| = |2 − 3| = 1：不动点失去稳定性。这是**倍周期分岔**的条件。在此临界点，从不动点分叉出周期-2 轨道（2 环）。

**Step 4 — Period-2 orbits.** A period-2 orbit satisfies x = f(f(x)) ≡ f⁽²⁾(x) but x ≠ f(x). The fixed points of f⁽²⁾ include the fixed points of f plus the new 2-cycle points. Expanding f⁽²⁾(x) = r·f(x)·(1 − f(x)):

**第 4 步 — 周期-2 轨道。** 周期-2 轨道满足 x = f(f(x)) ≡ f⁽²⁾(x) 但 x ≠ f(x)。f⁽²⁾ 的不动点包括 f 的不动点以及新的 2 环点。展开 f⁽²⁾(x) = r·f(x)·(1 − f(x))，可求解 2 环点；解为

  p, q = ((r+1) ± √(r² − 2r − 3)) / (2r),

existing (real solutions) when r² − 2r − 3 > 0, i.e. (r−3)(r+1) > 0, i.e. **r > 3**. ✓

当 r² − 2r − 3 > 0，即 **r > 3** 时，解为实数。✓

**Step 5 — Stability of the 2-cycle.** The 2-cycle {p, q} is stable when |(f⁽²⁾)′(p)| = |f′(p)·f′(q)| < 1. By the chain rule. Computing |f′(p)·f′(q)| = |r(1−2p)·r(1−2q)| and substituting the values of p and q, one finds this product equals |4 + 2r − r²|. The 2-cycle is stable for 3 < r < 1 + √6 ≈ 3.449. At r = 1 + √6, |f′(p)·f′(q)| = 1 again, triggering the **next period-doubling** to a 4-cycle. The cascade continues, with each period-doubling occurring at a smaller interval Δr, converging geometrically with ratio **δ ≈ 4.669** (the Feigenbaum constant).

**第 5 步 — 2 环的稳定性。** 2 环 {p, q} 稳定当 |(f⁽²⁾)′(p)| = |f′(p)·f′(q)| < 1。计算 |r(1−2p)·r(1−2q)|，代入 p, q 的值，得此乘积等于 |4 + 2r − r²|。2 环在 3 < r < 1 + √6 ≈ 3.449 时稳定。在 r = 1 + √6 处，|f′(p)·f′(q)| = 1，触发**下一次倍周期分岔**，产生 4 环。级联持续，每次倍周期分岔发生在更小的 Δr 区间，以比值 **δ ≈ 4.669**（费根鲍姆常数）几何收敛。∎

---

## C. The Lyapunov Exponent · 李雅普诺夫指数

**Claim.** The Lyapunov exponent

**命题。** 李雅普诺夫指数

  λ = lim_{t→∞} (1/t) ln(‖δx(t)‖ / ‖δx(0)‖)

characterizes the average exponential rate of divergence of nearby trajectories. For the logistic map at parameter r, it can be computed as λ = lim_{N→∞} (1/N) Σ_{n=0}^{N−1} ln|f′(xₙ)|.

刻画了邻近轨迹的平均指数发散速率。对参数为 r 的逻辑斯蒂映射，可以计算为 λ = lim_{N→∞} (1/N) Σ_{n=0}^{N−1} ln|f′(xₙ)|。

**Step 1 — Definition from linearization.** Consider two nearby initial conditions x₀ and x₀ + δ₀. After N iterations:

**第 1 步 — 由线性化给出定义。** 考虑两个初始接近的条件 x₀ 和 x₀ + δ₀。经 N 次迭代：

  δN = xN + δN − xN ≈ δ₀ · (f⁽N⁾)′(x₀) = δ₀ · Π_{n=0}^{N−1} f′(xₙ),

by the chain rule for the N-fold composition f⁽N⁾. Taking logarithms:

由 N 次复合函数 f⁽N⁾ 的链式法则。取对数：

  ln|δN/δ₀| = Σ_{n=0}^{N−1} ln|f′(xₙ)|.

**Step 2 — Define the Lyapunov exponent.** The Lyapunov exponent is the long-time average:

**第 2 步 — 定义李雅普诺夫指数。** 李雅普诺夫指数为长时平均：

  **λ = lim_{N→∞} (1/N) Σ_{n=0}^{N−1} ln|f′(xₙ)|**.

By ergodicity (for typical initial conditions), this equals the spatial average ∫ ln|f′(x)| ρ(x) dx where ρ(x) is the invariant density.

由遍历性（对典型初始条件），此等于空间平均 ∫ ln|f′(x)| ρ(x) dx，其中 ρ(x) 为不变密度。

**Step 3 — Interpretation.** If λ > 0, nearby trajectories diverge exponentially → **chaos**. If λ < 0, trajectories converge → **stable periodic orbit**. If λ = 0, the system is at a bifurcation point (marginal stability).

**第 3 步 — 诠释。** 若 λ > 0，邻近轨迹指数发散 → **混沌**。若 λ < 0，轨迹收敛 → **稳定周期轨道**。若 λ = 0，系统处于分岔点（边际稳定）。

**Step 4 — Compute λ for the logistic map at r = 4.** At r = 4, the logistic map is conjugate to the **tent map** via the substitution xₙ = sin²(πθₙ/2):

**第 4 步 — 计算 r = 4 时逻辑斯蒂映射的 λ。** 当 r = 4 时，逻辑斯蒂映射通过代换 xₙ = sin²(πθₙ/2) 与**帐篷映射**共轭：

  xₙ₊₁ = 4xₙ(1 − xₙ) = 4 sin²(πθₙ/2)(1 − sin²(πθₙ/2)) = sin²(πθₙ) = sin²(π · 2θₙ/2).

So θₙ₊₁ = 2θₙ (mod 1), the **doubling map**. For this map |T′(θ)| = 2 everywhere (where T is the doubling map), so

故 θₙ₊₁ = 2θₙ（mod 1），即**倍增映射**。对此映射 |T′(θ)| = 2 处处成立，故

  λ_θ = ln 2.

Since the conjugacy h: θ → x = sin²(πθ/2) is a smooth diffeomorphism, the Lyapunov exponent is invariant under smooth conjugacy (up to a normalization): **λ = ln 2** for the logistic map at r = 4. This means on average nearby orbits separate by a factor of 2 per iteration — the maximum possible chaos for this family.

由于共轭映射 h: θ → x = sin²(πθ/2) 是光滑微分同胚，李雅普诺夫指数在光滑共轭下不变：**r = 4 时逻辑斯蒂映射的 λ = ln 2**。这意味着邻近轨道平均每次迭代分离 2 倍——这是该族映射的最大混沌程度。

**Step 5 — Explicit verification.** For r = 4: f′(x) = 4(1 − 2x), so |f′(x)| = 4|1 − 2x|. Using the invariant density ρ(x) = 1/(π√(x(1−x))) (the arcsine distribution for r = 4):

**第 5 步 — 显式验证。** r = 4 时：f′(x) = 4(1 − 2x)，|f′(x)| = 4|1 − 2x|。利用不变密度 ρ(x) = 1/(π√(x(1−x)))（r = 4 的反正弦分布）：

  λ = ∫₀¹ ln(4|1 − 2x|) · 1/(π√(x(1−x))) dx.

Split: λ = ln 4 + ∫₀¹ ln|1 − 2x| / (π√(x(1−x))) dx. The integral ∫₀¹ ln|1 − 2x| / (π√(x(1−x))) dx = −ln 2 (a known result via the substitution x = sin²(u/2) and using ∫₀^π ln|sin u| du = −π ln 2). Therefore:

分拆：λ = ln 4 + ∫₀¹ ln|1−2x|/(π√(x(1−x))) dx。已知 ∫₀^π ln|sin u| du = −π ln 2，积分结果为 −ln 2。因此：

  λ = ln 4 − ln 2 = ln 2. ✓ ∎

**Step 6 — Lyapunov exponent for continuous-time systems.** For an ODE ẋ = **F**(**x**), the definition generalizes to

**第 6 步 — 连续时间系统的李雅普诺夫指数。** 对常微分方程 ẋ = **F**(**x**)，定义推广为

  λ = lim_{t→∞} (1/t) ln(‖δ**x**(t)‖ / ‖δ**x**(0)‖),

where δ**x**(t) satisfies the **variational equation** dδ**x**/dt = J(**x**(t)) δ**x** (J is the Jacobian along the trajectory). A positive λ implies chaos; the number of positive Lyapunov exponents counts the number of "directions" along which trajectories diverge. ∎

其中 δ**x**(t) 满足**变分方程** dδ**x**/dt = J(**x**(t)) δ**x**（J 为沿轨迹的雅可比矩阵）。正 λ 意味着混沌；正李雅普诺夫指数的个数计算轨迹发散的"方向"数目。∎

---

## D. The Lorenz System · 洛伦兹系统

**Claim.** The Lorenz system ẋ = σ(y − x), ẏ = x(ρ − z) − y, ż = xy − βz (with parameters σ, ρ, β > 0) has three fixed points, and for parameter values near σ = 10, ρ = 28, β = 8/3 exhibits deterministic chaos on a **strange attractor** with a positive Lyapunov exponent.

**命题。** 洛伦兹系统 ẋ = σ(y − x)，ẏ = x(ρ − z) − y，ż = xy − βz（参数 σ, ρ, β > 0）有三个不动点，在 σ = 10，ρ = 28，β = 8/3 附近的参数值处，在具有正李雅普诺夫指数的**奇异吸引子**上表现出确定性混沌。

**Step 1 — Physical origin.** The Lorenz system is a 3-mode Galerkin truncation of the Boussinesq equations for thermal convection in a layer heated from below (Rayleigh–Bénard convection). x is proportional to the convective roll amplitude; y is the temperature difference between ascending and descending fluid; z is the deviation of the vertical temperature profile from linearity. σ = Prandtl number (viscosity/thermal diffusivity), ρ = Rayleigh number / critical Rayleigh number, β = geometric factor.

**第 1 步 — 物理起源。** 洛伦兹系统是从下方加热的流体层（瑞利–贝纳德对流）的布辛涅斯克方程的 3 模伽辽金截断。x 正比于对流卷振幅；y 为上升和下降流体之间的温差；z 为竖直温度分布与线性的偏差。σ = 普朗特数（粘度/热扩散率），ρ = 瑞利数/临界瑞利数，β = 几何因子。

**Step 2 — Fixed points.** Setting ẋ = ẏ = ż = 0:

**第 2 步 — 不动点。** 令 ẋ = ẏ = ż = 0：

  From ẋ = 0: y = x.
  From ż = 0: z = xy/β = x²/β.
  From ẏ = 0: x(ρ − z) − y = 0 → x(ρ − x²/β) − x = 0 → x(ρ − 1 − x²/β) = 0.

So x = 0 (giving the **origin** (0,0,0), the trivial fixed point representing no convection) or x² = β(ρ − 1), giving **two symmetric fixed points**:

故 x = 0（给出**原点** (0,0,0)，代表无对流）或 x² = β(ρ − 1)，给出**两个对称不动点**：

  C± = (±√(β(ρ−1)), ±√(β(ρ−1)), ρ−1),

existing for ρ > 1.

在 ρ > 1 时存在。

**Step 3 — Stability of the origin.** At (0,0,0), the Jacobian is

**第 3 步 — 原点的稳定性。** 在 (0,0,0) 处，雅可比矩阵为

  J₀ = ⎡ −σ    σ    0 ⎤
        ⎢  ρ   −1    0 ⎥
        ⎣  0    0   −β ⎦

Eigenvalues: λ = −β (from z-decoupling) and λ = ½[−(σ+1) ± √((σ+1)² + 4σ(ρ−1))]. For ρ < 1, both signs of the square root give λ < 0: origin is stable (all perturbations decay — pure conduction state). For ρ > 1, one eigenvalue becomes positive: the origin is an **unstable saddle**.

特征值：λ = −β（由 z 方程解耦）以及 λ = ½[−(σ+1) ± √((σ+1)² + 4σ(ρ−1))]。当 ρ < 1 时，两个根均为负：原点稳定（纯导热态）。当 ρ > 1 时，一个特征值变正：原点为**不稳定鞍点**。

**Step 4 — Stability of C±.** At ρ = 28, σ = 10, β = 8/3, the fixed points C± = (±6√2, ±6√2, 27) exist. The Jacobian at C+ is

**第 4 步 — C± 的稳定性。** 在 ρ = 28，σ = 10，β = 8/3 时，不动点 C± = (±6√2, ±6√2, 27) 存在。在 C+ 处的雅可比矩阵为

  J_{C+} = ⎡ −σ      σ     0  ⎤ = ⎡ −10    10    0  ⎤
            ⎢  1     −1    −x* ⎥   ⎢   1    −1  −6√2 ⎥
            ⎣ x*     x*    −β  ⎦   ⎣ 6√2   6√2  −8/3 ⎦

The characteristic polynomial is λ³ + (σ+β+1)λ² + β(σ+ρ)λ + 2σβ(ρ−1) = 0. For σ = 10, β = 8/3, ρ = 28, by Routh–Hurwitz analysis, C± are **unstable** (one eigenvalue has positive real part). The critical ρ at which C± lose stability is

特征多项式为 λ³ + (σ+β+1)λ² + β(σ+ρ)λ + 2σβ(ρ−1) = 0。在 σ = 10，β = 8/3，ρ = 28 处，由劳斯–赫尔维茨分析，C± **不稳定**。C± 失去稳定性的临界 ρ 为

  ρ_c = σ(σ + β + 3)/(σ − β − 1) = 10·(10 + 8/3 + 3)/(10 − 8/3 − 1) = 10·(47/3)/(19/3) = 10·47/19 = 470/19 ≈ 24.74.

For ρ > ρ_c ≈ 24.74, all three fixed points are unstable, yet bounded trajectories must go somewhere — they are attracted to the **Lorenz strange attractor**.

当 ρ > ρ_c ≈ 24.74 时，三个不动点均不稳定，但有界轨迹仍须趋向某处——即被吸引到**洛伦兹奇异吸引子**。

**Step 5 — The attractor is bounded (Lyapunov function).** Consider V = x² + y² + (z − σ − ρ)². Compute dV/dt along the Lorenz flow:

**第 5 步 — 吸引子有界性（李雅普诺夫函数）。** 考虑 V = x² + y² + (z − σ − ρ)²。沿洛伦兹流计算 dV/dt：

  dV/dt = 2x ẋ + 2y ẏ + 2(z−σ−ρ) ż
        = 2x·σ(y−x) + 2y·(x(ρ−z)−y) + 2(z−σ−ρ)·(xy − βz)
        = −2σx² − 2y² − 2βz² + 2β(σ+ρ)z.

All xy and xyz cross-terms cancel. Completing the square in z:

所有 xy 与 xyz 交叉项相消。对 z 配方：

  dV/dt = −2σx² − 2y² − 2β(z − (σ+ρ)/2)² + β(σ+ρ)²/2.

The first three terms are negative definite, so dV/dt < 0 whenever 2σx² + 2y² + 2β(z − (σ+ρ)/2)² > β(σ+ρ)²/2 — i.e. everywhere outside a bounded ellipsoid E. Hence every trajectory eventually enters E and never leaves it: the Lorenz attractor lies in a compact region. ∎

前三项负定，故只要在有界椭球 E 之外（2σx² + 2y² + 2β(z − (σ+ρ)/2)² > β(σ+ρ)²/2），便有 dV/dt < 0。因此每条轨迹最终进入 E 且不再离开：洛伦兹吸引子位于紧致区域内。∎

更明确地：dV/dt = −2(σx² + y² + β(z − (σ+ρ)/2)² − β(σ+ρ)²/4)。对大 |**x**|，负定项主导，故在紧集之外 dV/dt < 0。

**Step 6 — Volume contraction (dissipation).** The divergence of the Lorenz vector field is

**第 6 步 — 体积收缩（耗散性）。** 洛伦兹矢量场的散度为

  ∇·**F** = ∂ẋ/∂x + ∂ẏ/∂y + ∂ż/∂z = −σ − 1 − β = −(σ + 1 + β).

For σ = 10, β = 8/3: ∇·**F** = −(10 + 1 + 8/3) = −41/3 < 0. This is constant, so phase-space volumes contract at rate e^{−(σ+1+β)t} → 0. The attractor therefore has zero phase-space volume — it is a **fractal set of dimension** slightly above 2.

对 σ = 10，β = 8/3：∇·**F** = −41/3 < 0。这是常数，故相空间体积以 e^{−(σ+1+β)t} 的速率收缩趋于零。因此吸引子的相空间体积为零——它是**维数略高于 2 的分形集**。

**Step 7 — Sensitive dependence and butterfly attractor.** Despite all three fixed points being unstable and the attractor having zero volume, trajectories are bounded. They wind around C+ for a while, then switch to wind around C−, then back, in an unpredictable sequence — the **butterfly attractor**. The largest Lyapunov exponent for the standard parameters is λ₁ ≈ +0.906, confirming exponential divergence and deterministic chaos. The sum λ₁ + λ₂ + λ₃ = −(σ + 1 + β) = −41/3 (consistent with volume contraction). ∎

**第 7 步 — 初值敏感性与蝴蝶吸引子。** 尽管三个不动点均不稳定且吸引子体积为零，轨迹仍然有界。轨迹围绕 C+ 转动一段时间后，切换到围绕 C−，如此反复，顺序不可预测——**蝴蝶吸引子**。标准参数下最大李雅普诺夫指数 λ₁ ≈ +0.906，证实指数发散和确定性混沌。三个李雅普诺夫指数之和 λ₁ + λ₂ + λ₃ = −(σ + 1 + β) = −41/3（与体积收缩一致）。∎

---

*The transition from order to chaos via period-doubling is universal — the Feigenbaum constant δ ≈ 4.669 appears in all unimodal maps with a smooth maximum, from the logistic map to the driven pendulum to physical experiments. The Lorenz system demonstrates that three coupled ODEs are sufficient to produce infinite complexity and a fractal attractor.*

*通过倍周期分岔从有序到混沌的转变是普适的——费根鲍姆常数 δ ≈ 4.669 出现在所有具有光滑极大值的单峰映射中，从逻辑斯蒂映射到受驱单摆到物理实验。洛伦兹系统证明三个耦合常微分方程足以产生无限复杂性和分形吸引子。*

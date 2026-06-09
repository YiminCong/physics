# Derivations — Module 1.19: Nonlinear Dynamics & Chaos
# 推导 — 模块 1.19：非线性动力学与混沌

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.19](./module-1.19-nonlinear-dynamics-chaos.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.19](./module-1.19-nonlinear-dynamics-chaos.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Linearization About a Fixed Point and Jacobian Classification · 不动点线性化与雅可比矩阵分类

**Claim.** For a smooth dynamical system $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x})$ with a fixed point $\mathbf{x}^*$ ($\mathbf{F}(\mathbf{x}^*) = 0$), the local stability is determined by the eigenvalues of the Jacobian matrix $J_{ij} = \partial F_i/\partial x_j$ evaluated at $\mathbf{x}^*$. The classification depends on the eigenvalues $\lambda_1, \lambda_2$ (in 2D).

**命题。** 对于具有不动点 $\mathbf{x}^*$（$\mathbf{F}(\mathbf{x}^*) = 0$）的光滑动力系统 $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x})$，局部稳定性由在 $\mathbf{x}^*$ 处计算的雅可比矩阵 $J_{ij} = \partial F_i/\partial x_j$ 的特征值决定。分类依赖于特征值 $\lambda_1, \lambda_2$（二维情形）。

**Step 1 — Taylor expansion.** Let $\mathbf{x} = \mathbf{x}^* + \boldsymbol{\delta x}$ where $\boldsymbol{\delta x}$ is a small perturbation. Taylor-expand $\mathbf{F}$ about $\mathbf{x}^*$:

**第 1 步 — 泰勒展开。** 令 $\mathbf{x} = \mathbf{x}^* + \boldsymbol{\delta x}$，其中 $\boldsymbol{\delta x}$ 为小扰动。在 $\mathbf{x}^*$ 处展开 $\mathbf{F}$：

$$ \dot{\mathbf{x}} = \mathbf{F}(\mathbf{x}^* + \boldsymbol{\delta x}) = \mathbf{F}(\mathbf{x}^*) + J\,\boldsymbol{\delta x} + O(|\boldsymbol{\delta x}|^2) = J\,\boldsymbol{\delta x} + O(|\boldsymbol{\delta x}|^2). $$

For small $\boldsymbol{\delta x}$, drop the quadratic terms:

对小 $\boldsymbol{\delta x}$，略去二次项：

$$ \frac{d(\boldsymbol{\delta x})}{dt} = J\,\boldsymbol{\delta x}, \qquad \text{where } J_{ij} = \left.\frac{\partial F_i}{\partial x_j}\right|_{\mathbf{x}^*}. $$

This is the **linearized system**.

这就是**线性化方程组**。

**Step 2 — Solution of the linearized system.** The general solution is $\boldsymbol{\delta x}(t) = \sum_k c_k \mathbf{v}_k e^{\lambda_k t}$, where $\lambda_k$ are eigenvalues and $\mathbf{v}_k$ are eigenvectors of $J$. The behavior as $t \to \infty$ is determined by the eigenvalue with the largest real part.

**第 2 步 — 线性化方程组的解。** 通解为 $\boldsymbol{\delta x}(t) = \sum_k c_k \mathbf{v}_k e^{\lambda_k t}$，其中 $\lambda_k$ 为 $J$ 的特征值，$\mathbf{v}_k$ 为特征向量。当 $t \to \infty$ 时，行为由实部最大的特征值决定。

**Step 3 — Classification in 2D.** For a 2D system with Jacobian $J$ having eigenvalues $\lambda_1, \lambda_2$ (which may be complex), let $\tau = \operatorname{tr} J = \lambda_1 + \lambda_2$ and $\Delta = \det J = \lambda_1 \lambda_2$. Then $\lambda = (\tau \pm \sqrt{\tau^2 - 4\Delta})/2$.

**第 3 步 — 二维分类。** 对二维系统，雅可比矩阵 $J$ 的特征值 $\lambda_1, \lambda_2$（可为复数），令 $\tau = \operatorname{tr} J = \lambda_1 + \lambda_2$，$\Delta = \det J = \lambda_1 \lambda_2$。则 $\lambda = (\tau \pm \sqrt{\tau^2 - 4\Delta})/2$。

The classification of the fixed point:

不动点的分类：

- **$\Delta < 0$:** Eigenvalues real with opposite sign $\to$ **saddle point** (unstable in one direction, stable in the other; the invariant manifold structure creates heteroclinic/homoclinic orbits).

- **$\Delta < 0$：** 特征值实数且异号 $\to$ **鞍点**（一方向不稳定，另一方向稳定；不变流形结构产生异宿/同宿轨道）。

- **$\Delta > 0,\ \tau^2 > 4\Delta$:** Both eigenvalues real with the same sign $\to$ **node** (stable if $\tau < 0$, unstable if $\tau > 0$; trajectories approach/leave along straight lines).

- **$\Delta > 0,\ \tau^2 > 4\Delta$：** 特征值均为实数且同号 $\to$ **结点**（$\tau < 0$ 稳定，$\tau > 0$ 不稳定；轨迹沿直线趋近/远离）。

- **$\Delta > 0,\ \tau^2 < 4\Delta$:** Complex conjugate eigenvalues $\lambda = \alpha \pm i\beta$ $\to$ **spiral** (stable focus if $\alpha = \tau/2 < 0$, unstable focus if $\tau > 0$; trajectories spiral in or out).

- **$\Delta > 0,\ \tau^2 < 4\Delta$：** 复共轭特征值 $\lambda = \alpha \pm i\beta$ $\to$ **螺旋点**（$\tau/2 < 0$ 为稳定焦点，$\tau > 0$ 为不稳定焦点；轨迹螺旋进入或远离）。

- **$\tau = 0,\ \Delta > 0$:** Purely imaginary eigenvalues $\to$ **centre** (marginally stable; linearization cannot determine stability of the nonlinear system).

- **$\tau = 0,\ \Delta > 0$：** 纯虚特征值 $\to$ **中心**（边际稳定；线性化无法确定非线性系统的稳定性）。

**Step 4 — Example: damped pendulum.** For $\ddot{\theta} + \gamma\dot{\theta} + \omega_0^2 \sin\theta = 0$, write as a system ($\dot{\theta} = v$, $\dot{v} = -\gamma v - \omega_0^2 \sin\theta$). Fixed points: $(0, 0)$ (bottom, stable) and $(\pi, 0)$ (top, unstable).

**第 4 步 — 例：阻尼单摆。** 对 $\ddot{\theta} + \gamma\dot{\theta} + \omega_0^2 \sin\theta = 0$，写为系统（$\dot{\theta} = v$，$\dot{v} = -\gamma v - \omega_0^2 \sin\theta$）。不动点：$(0, 0)$（底部，稳定）和 $(\pi, 0)$（顶部，不稳定）。

At $(0, 0)$: $J = \begin{bmatrix} 0 & 1 \\ -\omega_0^2 & -\gamma \end{bmatrix}$, $\tau = -\gamma < 0$, $\Delta = \omega_0^2 > 0$ $\to$ stable spiral (if $\gamma^2 < 4\omega_0^2$) or stable node.

在 $(0, 0)$：$J = \begin{bmatrix} 0 & 1 \\ -\omega_0^2 & -\gamma \end{bmatrix}$，$\tau = -\gamma < 0$，$\Delta = \omega_0^2 > 0$ $\to$ 稳定螺旋（若 $\gamma^2 < 4\omega_0^2$）或稳定结点。

At $(\pi, 0)$: $J = \begin{bmatrix} 0 & 1 \\ +\omega_0^2 & -\gamma \end{bmatrix}$, $\Delta = -\omega_0^2 < 0$ $\to$ **saddle point** (unstable). $\blacksquare$

在 $(\pi, 0)$：$J = \begin{bmatrix} 0 & 1 \\ +\omega_0^2 & -\gamma \end{bmatrix}$，$\Delta = -\omega_0^2 < 0$ $\to$ **鞍点**（不稳定）。$\blacksquare$

---

## B. The Logistic Map: Fixed Points, Period-Doubling, and Stability $|f'| = 1$ · 逻辑斯蒂映射：不动点、倍周期与稳定性条件

**Claim.** The logistic map $x_{n+1} = f(x_n) = r x_n(1 - x_n)$ has fixed points $x^* = 0$ and $x^* = 1 - 1/r$. Period-2 orbits emerge via a pitchfork bifurcation when $|f'(x^*)| = 1$. The period-doubling cascade repeats at each subsequent bifurcation.

**命题。** 逻辑斯蒂映射 $x_{n+1} = f(x_n) = r x_n(1 - x_n)$ 有不动点 $x^* = 0$ 和 $x^* = 1 - 1/r$。当 $|f'(x^*)| = 1$ 时，通过叉式分岔出现周期-2 轨道。倍周期级联在每个后续分岔处重复。

**Step 1 — Find the fixed points.** A fixed point satisfies $x^* = f(x^*) = r x^*(1 - x^*)$:

**第 1 步 — 求不动点。** 不动点满足 $x^* = f(x^*) = r x^*(1 - x^*)$：

$$ x^*\,(1 - r(1 - x^*)) = 0 \implies x^* = 0 \quad\text{or}\quad 1 = r(1 - x^*) \implies x^* = 1 - 1/r. $$

So the non-trivial fixed point is $x^* = (r - 1)/r$, existing for $r > 1$.

非平凡不动点为 $x^* = (r - 1)/r$，在 $r > 1$ 时存在。

**Step 2 — Stability of the fixed points.** For a map $x_{n+1} = f(x_n)$, a fixed point $x^*$ is **stable** if $|f'(x^*)| < 1$ and **unstable** if $|f'(x^*)| > 1$ (small deviations $\delta_n$ evolve as $\delta_n = (f'(x^*))^n \delta_0$, which decays iff $|f'(x^*)| < 1$).

**第 2 步 — 不动点的稳定性。** 对映射 $x_{n+1} = f(x_n)$，不动点 $x^*$ **稳定**当且仅当 $|f'(x^*)| < 1$；**不稳定**当 $|f'(x^*)| > 1$（小偏差 $\delta_n = (f'(x^*))^n \delta_0$，当 $|f'(x^*)| < 1$ 时衰减）。

Compute $f'(x) = r(1 - 2x)$. At $x^* = 1 - 1/r$:

计算 $f'(x) = r(1 - 2x)$。在 $x^* = 1 - 1/r$ 处：

$$ f'(x^*) = r(1 - 2(1 - 1/r)) = r(-1 + 2/r) = 2 - r. $$

So the non-trivial fixed point is stable when $|2 - r| < 1$, i.e. $1 < r < 3$.

故非平凡不动点在 $|2 - r| < 1$ 时稳定，即 $1 < r < 3$。

**Step 3 — Bifurcation at $r = 3$ ($|f'| = 1$ condition).** At $r = 3$, $|f'(x^*)| = |2 - 3| = 1$: the fixed point loses stability. This is the condition for a **period-doubling bifurcation**. At this critical point a period-2 orbit (2-cycle) emerges from the fixed point.

**第 3 步 — $r = 3$ 处的分岔（$|f'| = 1$ 条件）。** 在 $r = 3$ 处，$|f'(x^*)| = |2 - 3| = 1$：不动点失去稳定性。这是**倍周期分岔**的条件。在此临界点，从不动点分叉出周期-2 轨道（2 环）。

**Step 4 — Period-2 orbits.** A period-2 orbit satisfies $x = f(f(x)) \equiv f^{(2)}(x)$ but $x \ne f(x)$. The fixed points of $f^{(2)}$ include the fixed points of $f$ plus the new 2-cycle points. Expanding $f^{(2)}(x) = r\cdot f(x)\cdot(1 - f(x))$:

**第 4 步 — 周期-2 轨道。** 周期-2 轨道满足 $x = f(f(x)) \equiv f^{(2)}(x)$ 但 $x \ne f(x)$。$f^{(2)}$ 的不动点包括 $f$ 的不动点以及新的 2 环点。展开 $f^{(2)}(x) = r\cdot f(x)\cdot(1 - f(x))$，可求解 2 环点；解为

$$ p, q = \frac{(r+1) \pm \sqrt{r^2 - 2r - 3}}{2r}, $$

existing (real solutions) when $r^2 - 2r - 3 > 0$, i.e. $(r-3)(r+1) > 0$, i.e. $r > 3$. ✓

当 $r^2 - 2r - 3 > 0$，即 $r > 3$ 时，解为实数。✓

**Step 5 — Stability of the 2-cycle.** The 2-cycle $\{p, q\}$ is stable when $|(f^{(2)})'(p)| = |f'(p)\cdot f'(q)| < 1$. By the chain rule. Computing $|f'(p)\cdot f'(q)| = |r(1-2p)\cdot r(1-2q)|$ and substituting the values of $p$ and $q$, one finds this product equals $|4 + 2r - r^2|$. The 2-cycle is stable for $3 < r < 1 + \sqrt{6} \approx 3.449$. At $r = 1 + \sqrt{6}$, $|f'(p)\cdot f'(q)| = 1$ again, triggering the **next period-doubling** to a 4-cycle. The cascade continues, with each period-doubling occurring at a smaller interval $\Delta r$, converging geometrically with ratio $\delta \approx 4.669$ (the Feigenbaum constant).

**第 5 步 — 2 环的稳定性。** 2 环 $\{p, q\}$ 稳定当 $|(f^{(2)})'(p)| = |f'(p)\cdot f'(q)| < 1$。计算 $|r(1-2p)\cdot r(1-2q)|$，代入 $p, q$ 的值，得此乘积等于 $|4 + 2r - r^2|$。2 环在 $3 < r < 1 + \sqrt{6} \approx 3.449$ 时稳定。在 $r = 1 + \sqrt{6}$ 处，$|f'(p)\cdot f'(q)| = 1$，触发**下一次倍周期分岔**，产生 4 环。级联持续，每次倍周期分岔发生在更小的 $\Delta r$ 区间，以比值 $\delta \approx 4.669$（费根鲍姆常数）几何收敛。$\blacksquare$

---

## C. The Lyapunov Exponent · 李雅普诺夫指数

**Claim.** The Lyapunov exponent

**命题。** 李雅普诺夫指数

$$ \lambda = \lim_{t\to\infty} \frac{1}{t} \ln\frac{\|\delta x(t)\|}{\|\delta x(0)\|} $$

characterizes the average exponential rate of divergence of nearby trajectories. For the logistic map at parameter $r$, it can be computed as $\lambda = \lim_{N\to\infty} \frac{1}{N} \sum_{n=0}^{N-1} \ln|f'(x_n)|$.

刻画了邻近轨迹的平均指数发散速率。对参数为 $r$ 的逻辑斯蒂映射，可以计算为 $\lambda = \lim_{N\to\infty} \frac{1}{N} \sum_{n=0}^{N-1} \ln|f'(x_n)|$。

**Step 1 — Definition from linearization.** Consider two nearby initial conditions $x_0$ and $x_0 + \delta_0$. After $N$ iterations:

**第 1 步 — 由线性化给出定义。** 考虑两个初始接近的条件 $x_0$ 和 $x_0 + \delta_0$。经 $N$ 次迭代：

$$ \delta_N = x_N + \delta_N - x_N \approx \delta_0 \cdot (f^{(N)})'(x_0) = \delta_0 \cdot \prod_{n=0}^{N-1} f'(x_n), $$

by the chain rule for the $N$-fold composition $f^{(N)}$. Taking logarithms:

由 $N$ 次复合函数 $f^{(N)}$ 的链式法则。取对数：

$$ \ln|\delta_N/\delta_0| = \sum_{n=0}^{N-1} \ln|f'(x_n)|. $$

**Step 2 — Define the Lyapunov exponent.** The Lyapunov exponent is the long-time average:

**第 2 步 — 定义李雅普诺夫指数。** 李雅普诺夫指数为长时平均：

$$ \lambda = \lim_{N\to\infty} \frac{1}{N} \sum_{n=0}^{N-1} \ln|f'(x_n)|. $$

By ergodicity (for typical initial conditions), this equals the spatial average $\int \ln|f'(x)|\, \rho(x)\, dx$ where $\rho(x)$ is the invariant density.

由遍历性（对典型初始条件），此等于空间平均 $\int \ln|f'(x)|\, \rho(x)\, dx$，其中 $\rho(x)$ 为不变密度。

**Step 3 — Interpretation.** If $\lambda > 0$, nearby trajectories diverge exponentially $\to$ **chaos**. If $\lambda < 0$, trajectories converge $\to$ **stable periodic orbit**. If $\lambda = 0$, the system is at a bifurcation point (marginal stability).

**第 3 步 — 诠释。** 若 $\lambda > 0$，邻近轨迹指数发散 $\to$ **混沌**。若 $\lambda < 0$，轨迹收敛 $\to$ **稳定周期轨道**。若 $\lambda = 0$，系统处于分岔点（边际稳定）。

**Step 4 — Compute $\lambda$ for the logistic map at $r = 4$.** At $r = 4$, the logistic map is conjugate to the **tent map** via the substitution $x_n = \sin^2(\pi\theta_n/2)$:

**第 4 步 — 计算 $r = 4$ 时逻辑斯蒂映射的 $\lambda$。** 当 $r = 4$ 时，逻辑斯蒂映射通过代换 $x_n = \sin^2(\pi\theta_n/2)$ 与**帐篷映射**共轭：

$$ x_{n+1} = 4x_n(1 - x_n) = 4 \sin^2(\pi\theta_n/2)(1 - \sin^2(\pi\theta_n/2)) = \sin^2(\pi\theta_n) = \sin^2(\pi \cdot 2\theta_n/2). $$

So $\theta_{n+1} = 2\theta_n \pmod 1$, the **doubling map**. For this map $|T'(\theta)| = 2$ everywhere (where $T$ is the doubling map), so

故 $\theta_{n+1} = 2\theta_n \pmod 1$，即**倍增映射**。对此映射 $|T'(\theta)| = 2$ 处处成立，故

$$ \lambda_\theta = \ln 2. $$

Since the conjugacy $h: \theta \to x = \sin^2(\pi\theta/2)$ is a smooth diffeomorphism, the Lyapunov exponent is invariant under smooth conjugacy (up to a normalization): $\lambda = \ln 2$ for the logistic map at $r = 4$. This means on average nearby orbits separate by a factor of 2 per iteration — the maximum possible chaos for this family.

由于共轭映射 $h: \theta \to x = \sin^2(\pi\theta/2)$ 是光滑微分同胚，李雅普诺夫指数在光滑共轭下不变：$r = 4$ 时逻辑斯蒂映射的 $\lambda = \ln 2$。这意味着邻近轨道平均每次迭代分离 2 倍——这是该族映射的最大混沌程度。

**Step 5 — Explicit verification.** For $r = 4$: $f'(x) = 4(1 - 2x)$, so $|f'(x)| = 4|1 - 2x|$. Using the invariant density $\rho(x) = 1/(\pi\sqrt{x(1-x)})$ (the arcsine distribution for $r = 4$):

**第 5 步 — 显式验证。** $r = 4$ 时：$f'(x) = 4(1 - 2x)$，$|f'(x)| = 4|1 - 2x|$。利用不变密度 $\rho(x) = 1/(\pi\sqrt{x(1-x)})$（$r = 4$ 的反正弦分布）：

$$ \lambda = \int_0^1 \ln(4|1 - 2x|) \cdot \frac{1}{\pi\sqrt{x(1-x)}}\, dx. $$

Split: $\lambda = \ln 4 + \int_0^1 \frac{\ln|1 - 2x|}{\pi\sqrt{x(1-x)}}\, dx$. The integral $\int_0^1 \frac{\ln|1 - 2x|}{\pi\sqrt{x(1-x)}}\, dx = -\ln 2$ (a known result via the substitution $x = \sin^2(u/2)$ and using $\int_0^\pi \ln|\sin u|\, du = -\pi \ln 2$). Therefore:

分拆：$\lambda = \ln 4 + \int_0^1 \frac{\ln|1-2x|}{\pi\sqrt{x(1-x)}}\, dx$。已知 $\int_0^\pi \ln|\sin u|\, du = -\pi \ln 2$，积分结果为 $-\ln 2$。因此：

$$ \lambda = \ln 4 - \ln 2 = \ln 2. \quad\text{✓}\quad \blacksquare $$

**Step 6 — Lyapunov exponent for continuous-time systems.** For an ODE $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x})$, the definition generalizes to

**第 6 步 — 连续时间系统的李雅普诺夫指数。** 对常微分方程 $\dot{\mathbf{x}} = \mathbf{F}(\mathbf{x})$，定义推广为

$$ \lambda = \lim_{t\to\infty} \frac{1}{t} \ln\frac{\|\delta\mathbf{x}(t)\|}{\|\delta\mathbf{x}(0)\|}, $$

where $\delta\mathbf{x}(t)$ satisfies the **variational equation** $d\delta\mathbf{x}/dt = J(\mathbf{x}(t))\,\delta\mathbf{x}$ ($J$ is the Jacobian along the trajectory). A positive $\lambda$ implies chaos; the number of positive Lyapunov exponents counts the number of "directions" along which trajectories diverge. $\blacksquare$

其中 $\delta\mathbf{x}(t)$ 满足**变分方程** $d\delta\mathbf{x}/dt = J(\mathbf{x}(t))\,\delta\mathbf{x}$（$J$ 为沿轨迹的雅可比矩阵）。正 $\lambda$ 意味着混沌；正李雅普诺夫指数的个数计算轨迹发散的"方向"数目。$\blacksquare$

---

## D. The Lorenz System · 洛伦兹系统

**Claim.** The Lorenz system $\dot{x} = \sigma(y - x)$, $\dot{y} = x(\rho - z) - y$, $\dot{z} = xy - \beta z$ (with parameters $\sigma, \rho, \beta > 0$) has three fixed points, and for parameter values near $\sigma = 10$, $\rho = 28$, $\beta = 8/3$ exhibits deterministic chaos on a **strange attractor** with a positive Lyapunov exponent.

**命题。** 洛伦兹系统 $\dot{x} = \sigma(y - x)$，$\dot{y} = x(\rho - z) - y$，$\dot{z} = xy - \beta z$（参数 $\sigma, \rho, \beta > 0$）有三个不动点，在 $\sigma = 10$，$\rho = 28$，$\beta = 8/3$ 附近的参数值处，在具有正李雅普诺夫指数的**奇异吸引子**上表现出确定性混沌。

**Step 1 — Physical origin.** The Lorenz system is a 3-mode Galerkin truncation of the Boussinesq equations for thermal convection in a layer heated from below (Rayleigh–Bénard convection). $x$ is proportional to the convective roll amplitude; $y$ is the temperature difference between ascending and descending fluid; $z$ is the deviation of the vertical temperature profile from linearity. $\sigma =$ Prandtl number (viscosity/thermal diffusivity), $\rho =$ Rayleigh number / critical Rayleigh number, $\beta =$ geometric factor.

**第 1 步 — 物理起源。** 洛伦兹系统是从下方加热的流体层（瑞利–贝纳德对流）的布辛涅斯克方程的 3 模伽辽金截断。$x$ 正比于对流卷振幅；$y$ 为上升和下降流体之间的温差；$z$ 为竖直温度分布与线性的偏差。$\sigma =$ 普朗特数（粘度/热扩散率），$\rho =$ 瑞利数/临界瑞利数，$\beta =$ 几何因子。

**Step 2 — Fixed points.** Setting $\dot{x} = \dot{y} = \dot{z} = 0$:

**第 2 步 — 不动点。** 令 $\dot{x} = \dot{y} = \dot{z} = 0$：

$$ \begin{aligned}
&\text{From } \dot{x} = 0:\ y = x. \\
&\text{From } \dot{z} = 0:\ z = xy/\beta = x^2/\beta. \\
&\text{From } \dot{y} = 0:\ x(\rho - z) - y = 0 \to x(\rho - x^2/\beta) - x = 0 \to x(\rho - 1 - x^2/\beta) = 0.
\end{aligned} $$

So $x = 0$ (giving the **origin** $(0,0,0)$, the trivial fixed point representing no convection) or $x^2 = \beta(\rho - 1)$, giving **two symmetric fixed points**:

故 $x = 0$（给出**原点** $(0,0,0)$，代表无对流）或 $x^2 = \beta(\rho - 1)$，给出**两个对称不动点**：

$$ C_\pm = \left(\pm\sqrt{\beta(\rho-1)},\ \pm\sqrt{\beta(\rho-1)},\ \rho-1\right), $$

existing for $\rho > 1$.

在 $\rho > 1$ 时存在。

**Step 3 — Stability of the origin.** At $(0,0,0)$, the Jacobian is

**第 3 步 — 原点的稳定性。** 在 $(0,0,0)$ 处，雅可比矩阵为

$$ J_0 = \begin{bmatrix} -\sigma & \sigma & 0 \\ \rho & -1 & 0 \\ 0 & 0 & -\beta \end{bmatrix}. $$

Eigenvalues: $\lambda = -\beta$ (from $z$-decoupling) and $\lambda = \tfrac12[-(\sigma+1) \pm \sqrt{(\sigma+1)^2 + 4\sigma(\rho-1)}]$. For $\rho < 1$, both signs of the square root give $\lambda < 0$: origin is stable (all perturbations decay — pure conduction state). For $\rho > 1$, one eigenvalue becomes positive: the origin is an **unstable saddle**.

特征值：$\lambda = -\beta$（由 $z$ 方程解耦）以及 $\lambda = \tfrac12[-(\sigma+1) \pm \sqrt{(\sigma+1)^2 + 4\sigma(\rho-1)}]$。当 $\rho < 1$ 时，两个根均为负：原点稳定（纯导热态）。当 $\rho > 1$ 时，一个特征值变正：原点为**不稳定鞍点**。

**Step 4 — Stability of $C_\pm$.** At $\rho = 28$, $\sigma = 10$, $\beta = 8/3$, the fixed points $C_\pm = (\pm 6\sqrt{2}, \pm 6\sqrt{2}, 27)$ exist. The Jacobian at $C_+$ is

**第 4 步 — $C_\pm$ 的稳定性。** 在 $\rho = 28$，$\sigma = 10$，$\beta = 8/3$ 时，不动点 $C_\pm = (\pm 6\sqrt{2}, \pm 6\sqrt{2}, 27)$ 存在。在 $C_+$ 处的雅可比矩阵为

$$ J_{C_+} = \begin{bmatrix} -\sigma & \sigma & 0 \\ 1 & -1 & -x^* \\ x^* & x^* & -\beta \end{bmatrix} = \begin{bmatrix} -10 & 10 & 0 \\ 1 & -1 & -6\sqrt{2} \\ 6\sqrt{2} & 6\sqrt{2} & -8/3 \end{bmatrix}. $$

The characteristic polynomial is $\lambda^3 + (\sigma+\beta+1)\lambda^2 + \beta(\sigma+\rho)\lambda + 2\sigma\beta(\rho-1) = 0$. For $\sigma = 10$, $\beta = 8/3$, $\rho = 28$, by Routh–Hurwitz analysis, $C_\pm$ are **unstable** (one eigenvalue has positive real part). The critical $\rho$ at which $C_\pm$ lose stability is

特征多项式为 $\lambda^3 + (\sigma+\beta+1)\lambda^2 + \beta(\sigma+\rho)\lambda + 2\sigma\beta(\rho-1) = 0$。在 $\sigma = 10$，$\beta = 8/3$，$\rho = 28$ 处，由劳斯–赫尔维茨分析，$C_\pm$ **不稳定**。$C_\pm$ 失去稳定性的临界 $\rho$ 为

$$ \rho_c = \frac{\sigma(\sigma + \beta + 3)}{\sigma - \beta - 1} = \frac{10\cdot(10 + 8/3 + 3)}{10 - 8/3 - 1} = \frac{10\cdot(47/3)}{19/3} = \frac{10\cdot 47}{19} = \frac{470}{19} \approx 24.74. $$

For $\rho > \rho_c \approx 24.74$, all three fixed points are unstable, yet bounded trajectories must go somewhere — they are attracted to the **Lorenz strange attractor**.

当 $\rho > \rho_c \approx 24.74$ 时，三个不动点均不稳定，但有界轨迹仍须趋向某处——即被吸引到**洛伦兹奇异吸引子**。

**Step 5 — The attractor is bounded (Lyapunov function).** Consider $V = x^2 + y^2 + (z - \sigma - \rho)^2$. Compute $dV/dt$ along the Lorenz flow:

**第 5 步 — 吸引子有界性（李雅普诺夫函数）。** 考虑 $V = x^2 + y^2 + (z - \sigma - \rho)^2$。沿洛伦兹流计算 $dV/dt$：

$$ \begin{aligned}
\frac{dV}{dt} &= 2x\,\dot{x} + 2y\,\dot{y} + 2(z-\sigma-\rho)\,\dot{z} \\
&= 2x\cdot\sigma(y-x) + 2y\cdot(x(\rho-z)-y) + 2(z-\sigma-\rho)\cdot(xy - \beta z) \\
&= -2\sigma x^2 - 2y^2 - 2\beta z^2 + 2\beta(\sigma+\rho)z.
\end{aligned} $$

All $xy$ and $xyz$ cross-terms cancel. Completing the square in $z$:

所有 $xy$ 与 $xyz$ 交叉项相消。对 $z$ 配方：

$$ \frac{dV}{dt} = -2\sigma x^2 - 2y^2 - 2\beta\left(z - \frac{\sigma+\rho}{2}\right)^2 + \frac{\beta(\sigma+\rho)^2}{2}. $$

The first three terms are negative definite, so $dV/dt < 0$ whenever $2\sigma x^2 + 2y^2 + 2\beta(z - (\sigma+\rho)/2)^2 > \beta(\sigma+\rho)^2/2$ — i.e. everywhere outside a bounded ellipsoid $E$. Hence every trajectory eventually enters $E$ and never leaves it: the Lorenz attractor lies in a compact region. $\blacksquare$

前三项负定，故只要在有界椭球 $E$ 之外（$2\sigma x^2 + 2y^2 + 2\beta(z - (\sigma+\rho)/2)^2 > \beta(\sigma+\rho)^2/2$），便有 $dV/dt < 0$。因此每条轨迹最终进入 $E$ 且不再离开：洛伦兹吸引子位于紧致区域内。$\blacksquare$

更明确地：$dV/dt = -2(\sigma x^2 + y^2 + \beta(z - (\sigma+\rho)/2)^2 - \beta(\sigma+\rho)^2/4)$。对大 $|\mathbf{x}|$，负定项主导，故在紧集之外 $dV/dt < 0$。

**Step 6 — Volume contraction (dissipation).** The divergence of the Lorenz vector field is

**第 6 步 — 体积收缩（耗散性）。** 洛伦兹矢量场的散度为

$$ \boldsymbol{\nabla}\cdot\mathbf{F} = \frac{\partial \dot{x}}{\partial x} + \frac{\partial \dot{y}}{\partial y} + \frac{\partial \dot{z}}{\partial z} = -\sigma - 1 - \beta = -(\sigma + 1 + \beta). $$

For $\sigma = 10$, $\beta = 8/3$: $\boldsymbol{\nabla}\cdot\mathbf{F} = -(10 + 1 + 8/3) = -41/3 < 0$. This is constant, so phase-space volumes contract at rate $e^{-(\sigma+1+\beta)t} \to 0$. The attractor therefore has zero phase-space volume — it is a **fractal set of dimension** slightly above 2.

对 $\sigma = 10$，$\beta = 8/3$：$\boldsymbol{\nabla}\cdot\mathbf{F} = -41/3 < 0$。这是常数，故相空间体积以 $e^{-(\sigma+1+\beta)t}$ 的速率收缩趋于零。因此吸引子的相空间体积为零——它是**维数略高于 2 的分形集**。

**Step 7 — Sensitive dependence and butterfly attractor.** Despite all three fixed points being unstable and the attractor having zero volume, trajectories are bounded. They wind around $C_+$ for a while, then switch to wind around $C_-$, then back, in an unpredictable sequence — the **butterfly attractor**. The largest Lyapunov exponent for the standard parameters is $\lambda_1 \approx +0.906$, confirming exponential divergence and deterministic chaos. The sum $\lambda_1 + \lambda_2 + \lambda_3 = -(\sigma + 1 + \beta) = -41/3$ (consistent with volume contraction). $\blacksquare$

**第 7 步 — 初值敏感性与蝴蝶吸引子。** 尽管三个不动点均不稳定且吸引子体积为零，轨迹仍然有界。轨迹围绕 $C_+$ 转动一段时间后，切换到围绕 $C_-$，如此反复，顺序不可预测——**蝴蝶吸引子**。标准参数下最大李雅普诺夫指数 $\lambda_1 \approx +0.906$，证实指数发散和确定性混沌。三个李雅普诺夫指数之和 $\lambda_1 + \lambda_2 + \lambda_3 = -(\sigma + 1 + \beta) = -41/3$（与体积收缩一致）。$\blacksquare$

---

*The transition from order to chaos via period-doubling is universal — the Feigenbaum constant $\delta \approx 4.669$ appears in all unimodal maps with a smooth maximum, from the logistic map to the driven pendulum to physical experiments. The Lorenz system demonstrates that three coupled ODEs are sufficient to produce infinite complexity and a fractal attractor.*

*通过倍周期分岔从有序到混沌的转变是普适的——费根鲍姆常数 $\delta \approx 4.669$ 出现在所有具有光滑极大值的单峰映射中，从逻辑斯蒂映射到受驱单摆到物理实验。洛伦兹系统证明三个耦合常微分方程足以产生无限复杂性和分形吸引子。*

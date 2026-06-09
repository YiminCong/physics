---
title: "Derivations — Module 6.4: Path Integrals & Field Theory"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 6.4: Path Integrals & Field Theory
# 推导 — 模块 6.4：路径积分与场论

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.4](./module-6.4-path-integrals.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.4](./module-6.4-path-integrals.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Derivation of the Feynman Path Integral by Time-Slicing · 通过时间切片推导费曼路径积分

**Claim.** The quantum amplitude for a particle to propagate from $x_i$ to $x_f$ in time $T$ is

$$ K(x_f, T; x_i, 0) = \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar}, $$

where $S[x] = \int_0^T dt\, [\tfrac12 m\dot x^2 - V(x)]$ is the classical action and $\mathcal{D}[x(t)]$ is the functional measure over all paths with $x(0) = x_i$, $x(T) = x_f$.

**命题。** 粒子在时间 $T$ 内从 $x_i$ 传播到 $x_f$ 的量子幅度为

$$ K(x_f, T; x_i, 0) = \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar}, $$

其中 $S[x] = \int_0^T dt\, [\tfrac12 m\dot x^2 - V(x)]$ 是经典作用量，$\mathcal{D}[x(t)]$ 是满足 $x(0) = x_i$、$x(T) = x_f$ 的所有路径的泛函测度。

**Step 1 — Slice the time interval.** Divide $[0, T]$ into $N$ equal subintervals of length $\varepsilon = T/N$. Write the propagator as a product of short-time propagators using the composition (semigroup) property of the evolution operator:

$$ e^{-i\hat H T/\hbar} = (e^{-i\hat H \varepsilon/\hbar})^N = e^{-i\hat H \varepsilon/\hbar} \cdot e^{-i\hat H \varepsilon/\hbar} \cdot \ldots \cdot e^{-i\hat H \varepsilon/\hbar} \quad (N \text{ factors}). $$

**第 1 步 — 切分时间区间。** 将 $[0, T]$ 划分为 $N$ 个等长子区间，每段长度 $\varepsilon = T/N$。利用演化算符的复合（半群）性质，将传播子写成短时传播子之积：

$$ e^{-i\hat H T/\hbar} = (e^{-i\hat H \varepsilon/\hbar})^N = e^{-i\hat H \varepsilon/\hbar} \cdot e^{-i\hat H \varepsilon/\hbar} \cdot \ldots \cdot e^{-i\hat H \varepsilon/\hbar} \quad (N \text{ 个因子}). $$

**Step 2 — Insert $N-1$ complete sets of position eigenstates.** Between each pair of adjacent factors, insert $1 = \int dx_j\, |x_j\rangle\langle x_j|$:

$$ \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int dx_1\, dx_2 \ldots dx_{N-1} \prod_{j=0}^{N-1} \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle, $$

where $x_0 \equiv x_i$ and $x_N \equiv x_f$.

**第 2 步 — 插入 $N-1$ 个完备位置本征态集。** 在每对相邻因子之间，插入 $1 = \int dx_j\, |x_j\rangle\langle x_j|$：

$$ \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int dx_1\, dx_2 \ldots dx_{N-1} \prod_{j=0}^{N-1} \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle, $$

其中 $x_0 \equiv x_i$，$x_N \equiv x_f$。

**Step 3 — Evaluate a single short-time matrix element.** For $\hat H = \hat p^2/2m + V(\hat x)$ and small $\varepsilon$, use the Trotter product formula $e^{-i\hat H \varepsilon/\hbar} \approx e^{-i\hat p^2\varepsilon/2m\hbar}\, e^{-iV(\hat x)\varepsilon/\hbar} + O(\varepsilon^2)$. Insert a resolution of the identity in momentum space $1 = \int \frac{dp}{2\pi\hbar}\, |p\rangle\langle p|$:

$$ \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle \approx \int \frac{dp}{2\pi\hbar}\, \langle x_{j+1}|p\rangle\, e^{-ip^2\varepsilon/2m\hbar}\, \langle p|x_j\rangle\, e^{-iV(x_j)\varepsilon/\hbar}. $$

Using $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$:

$$ = \int \frac{dp}{2\pi\hbar}\, e^{ip(x_{j+1} - x_j)/\hbar}\, e^{-ip^2\varepsilon/2m\hbar}\, e^{-iV(x_j)\varepsilon/\hbar}. $$

**第 3 步 — 计算单个短时矩阵元。** 对于 $\hat H = \hat p^2/2m + V(\hat x)$ 和小 $\varepsilon$，使用 Trotter 乘积公式 $e^{-i\hat H \varepsilon/\hbar} \approx e^{-i\hat p^2\varepsilon/2m\hbar}\, e^{-iV(\hat x)\varepsilon/\hbar} + O(\varepsilon^2)$。在动量空间插入单位分解 $1 = \int \frac{dp}{2\pi\hbar}\, |p\rangle\langle p|$：

$$ \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle \approx \int \frac{dp}{2\pi\hbar}\, \langle x_{j+1}|p\rangle\, e^{-ip^2\varepsilon/2m\hbar}\, \langle p|x_j\rangle\, e^{-iV(x_j)\varepsilon/\hbar}. $$

利用 $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$：

$$ = \int \frac{dp}{2\pi\hbar}\, e^{ip(x_{j+1} - x_j)/\hbar}\, e^{-ip^2\varepsilon/2m\hbar}\, e^{-iV(x_j)\varepsilon/\hbar}. $$

**Step 4 — Perform the Gaussian momentum integral.** The integral over $p$ is of the form $\int dp\, e^{ip\Delta x/\hbar - ip^2\varepsilon/2m\hbar}$ where $\Delta x = x_{j+1} - x_j$. Complete the square: let $p' = p - m\Delta x/\varepsilon$, so that

$$ ip\Delta x/\hbar - ip^2\varepsilon/2m\hbar = im(\Delta x)^2/2\hbar\varepsilon - ip'^2\varepsilon/2m\hbar. $$

The Gaussian integral $\int dp'\, e^{-ip'^2\varepsilon/2m\hbar} = \sqrt{2\pi m\hbar/i\varepsilon}$ (choosing the branch with $\mathrm{Im}(\sqrt{\,}) > 0$ for convergence). Therefore

$$ \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle \approx \sqrt{\frac{m}{2\pi i\hbar\varepsilon}}\, \exp\!\left(\frac{i\varepsilon}{\hbar}\left[\frac{m(\Delta x/\varepsilon)^2}{2} - V(x_j)\right]\right). $$

**第 4 步 — 执行高斯动量积分。** 对 $p$ 的积分形如 $\int dp\, e^{ip\Delta x/\hbar - ip^2\varepsilon/2m\hbar}$，其中 $\Delta x = x_{j+1} - x_j$。配方：令 $p' = p - m\Delta x/\varepsilon$，则

$$ ip\Delta x/\hbar - ip^2\varepsilon/2m\hbar = im(\Delta x)^2/2\hbar\varepsilon - ip'^2\varepsilon/2m\hbar. $$

高斯积分 $\int dp'\, e^{-ip'^2\varepsilon/2m\hbar} = \sqrt{2\pi m\hbar/i\varepsilon}$（选择 $\mathrm{Im}(\sqrt{\,}) > 0$ 的分支以保证收敛）。因此

$$ \langle x_{j+1}| e^{-i\hat H \varepsilon/\hbar} |x_j\rangle \approx \sqrt{\frac{m}{2\pi i\hbar\varepsilon}}\, \exp\!\left(\frac{i\varepsilon}{\hbar}\left[\frac{m(\Delta x/\varepsilon)^2}{2} - V(x_j)\right]\right). $$

**Step 5 — Recognize the discrete action and take $N \to \infty$.** The exponent is

$$ \frac{i}{\hbar} \sum_{j=0}^{N-1} \varepsilon\, [\tfrac12 m(\Delta x_j/\varepsilon)^2 - V(x_j)] \;\to\; iS[x]/\hbar \quad \text{as } \varepsilon \to 0, $$

where $S[x] = \int_0^T dt\, [\tfrac12 m\dot x^2 - V(x(t))]$ is the classical action. The product of prefactors $(\sqrt{m/2\pi i\hbar\varepsilon})^N$ defines the functional measure $\mathcal{D}[x(t)]$:

$$ \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar} \equiv \lim_{N\to\infty} (m/2\pi i\hbar\varepsilon)^{N/2} \int dx_1 \ldots dx_{N-1}\, e^{\frac{i}{\hbar} \sum_j \varepsilon\, L(x_j, \dot x_j)}. $$

The full result is

$$ \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar}. \qquad \blacksquare $$

**第 5 步 — 识别离散作用量并取 $N \to \infty$。** 指数为

$$ \frac{i}{\hbar} \sum_{j=0}^{N-1} \varepsilon\, [\tfrac12 m(\Delta x_j/\varepsilon)^2 - V(x_j)] \;\to\; iS[x]/\hbar \quad \text{当 } \varepsilon \to 0 \text{ 时}, $$

其中 $S[x] = \int_0^T dt\, [\tfrac12 m\dot x^2 - V(x(t))]$ 是经典作用量。前因子之积 $(\sqrt{m/2\pi i\hbar\varepsilon})^N$ 定义了泛函测度 $\mathcal{D}[x(t)]$：

$$ \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar} \equiv \lim_{N\to\infty} (m/2\pi i\hbar\varepsilon)^{N/2} \int dx_1 \ldots dx_{N-1}\, e^{\frac{i}{\hbar} \sum_j \varepsilon\, L(x_j, \dot x_j)}. $$

完整结果为

$$ \langle x_f| e^{-i\hat H T/\hbar} |x_i\rangle = \int \mathcal{D}[x(t)]\, e^{iS[x]/\hbar}. \qquad \blacksquare $$

---

## B. The Classical Limit and the Stationary-Phase Condition · 经典极限与驻相条件

**Claim.** In the limit $\hbar \to 0$, the path integral is dominated by the path $x_{cl}(t)$ that extremizes the action, i.e. the classical trajectory satisfying $\delta S[x_{cl}] = 0$ (Hamilton's principle, Module 1.3).

**命题。** 在 $\hbar \to 0$ 的极限下，路径积分由使作用量取极值的路径 $x_{cl}(t)$ 主导，即满足 $\delta S[x_{cl}] = 0$ 的经典轨迹（哈密顿原理，模块 1.3）。

**Step 1 — Expand $S$ around the classical path.** Write $x(t) = x_{cl}(t) + \eta(t)$, where $\eta(0) = \eta(T) = 0$ (fixed endpoints). Taylor expand:

$$ S[x_{cl} + \eta] = S[x_{cl}] + \delta S[x_{cl}](\eta) + \tfrac12 \delta^2 S[x_{cl}](\eta,\eta) + O(\eta^3). $$

The first-order term $\delta S[x_{cl}](\eta) = \int_0^T dt\, (\partial L/\partial x - \frac{d}{dt} \partial L/\partial\dot x)|_{x_{cl}}\, \eta(t)$ vanishes by the classical equation of motion (Euler–Lagrange equation, Module 1.3). The leading correction is the second-order (Gaussian) fluctuation.

**第 1 步 — 在经典路径附近展开 $S$。** 写出 $x(t) = x_{cl}(t) + \eta(t)$，其中 $\eta(0) = \eta(T) = 0$（固定端点）。泰勒展开：

$$ S[x_{cl} + \eta] = S[x_{cl}] + \delta S[x_{cl}](\eta) + \tfrac12 \delta^2 S[x_{cl}](\eta,\eta) + O(\eta^3). $$

一阶项 $\delta S[x_{cl}](\eta) = \int_0^T dt\, (\partial L/\partial x - \frac{d}{dt} \partial L/\partial\dot x)|_{x_{cl}}\, \eta(t)$ 由经典运动方程（欧拉–拉格朗日方程，模块 1.3）消失。领头修正是二阶（高斯）涨落。

**Step 2 — Stationary phase for oscillatory integrals.** In the path integral $\int \mathcal{D}[x]\, e^{iS[x]/\hbar}$, each path contributes a phase $e^{iS/\hbar}$. As $\hbar \to 0$, the phase oscillates rapidly for paths far from $x_{cl}$. These rapid oscillations produce cancellation among nearby paths (destructive interference). Only paths near $x_{cl}$, where the phase is stationary ($\delta S = 0$), contribute coherently (constructive interference). This is the stationary-phase (or saddle-point) approximation — the quantum-mechanical version of classical mechanics.

**第 2 步 — 振荡积分的驻相。** 在路径积分 $\int \mathcal{D}[x]\, e^{iS[x]/\hbar}$ 中，每条路径贡献相位 $e^{iS/\hbar}$。当 $\hbar \to 0$ 时，远离 $x_{cl}$ 的路径相位振荡剧烈。这些快速振荡导致邻近路径之间相消干涉。只有 $x_{cl}$ 附近相位驻定（$\delta S = 0$）的路径相长干涉。这是驻相（或鞍点）近似——经典力学的量子力学版本。

**Step 3 — Leading result and quantum corrections.** At lowest order in $\hbar$:

$$ K(x_f, T; x_i, 0) \approx C\, e^{iS[x_{cl}]/\hbar}, $$

where $C$ comes from the Gaussian integral over $\eta$ (the fluctuation determinant). The quantum corrections are suppressed by powers of $\hbar$. The classical limit $\hbar \to 0$ recovers Newton's second law and Hamilton's equations precisely because the stationary condition $\delta S = 0$ is Hamilton's principle. $\blacksquare$

**第 3 步 — 领头结果与量子修正。** 在 $\hbar$ 的最低阶：

$$ K(x_f, T; x_i, 0) \approx C\, e^{iS[x_{cl}]/\hbar}, $$

其中 $C$ 来自对 $\eta$ 的高斯积分（涨落行列式）。量子修正被 $\hbar$ 的幂次压制。经典极限 $\hbar \to 0$ 精确还原牛顿第二定律和哈密顿方程，正是因为驻定条件 $\delta S = 0$ 就是哈密顿原理。$\blacksquare$

---

## C. The Imaginary-Time Path Integral and the Partition Function · 虚时路径积分与配分函数

**Claim.** Under the Wick rotation $t \to -i\tau$ (imaginary time), the quantum partition function becomes a Euclidean functional integral:

$$ Z = \mathrm{Tr}\, e^{-\beta\hat H} = \int_{\text{periodic}} \mathcal{D}[\varphi]\, e^{-S_E[\varphi]/\hbar}, $$

where $S_E$ is the Euclidean action and the fields obey periodic (bosons) or antiperiodic (fermions) boundary conditions in $\tau \in [0, \hbar\beta]$.

**命题。** 在维克转动 $t \to -i\tau$（虚时间）下，量子配分函数变为欧几里得泛函积分：

$$ Z = \mathrm{Tr}\, e^{-\beta\hat H} = \int_{\text{periodic}} \mathcal{D}[\varphi]\, e^{-S_E[\varphi]/\hbar}, $$

其中 $S_E$ 是欧几里得作用量，场在 $\tau \in [0, \hbar\beta]$ 中满足周期（玻色子）或反周期（费米子）边界条件。

**Step 1 — Relate the partition function to the propagator.** The partition function is $Z = \mathrm{Tr}\, e^{-\beta\hat H} = \int dx\, \langle x|e^{-\beta\hat H}|x\rangle$. Comparing with the propagator $K(x_f, T; x_i, 0) = \langle x_f|e^{-i\hat H T/\hbar}|x_i\rangle$, we see that setting $T = -i\hbar\beta$ (i.e. $t \to -i\tau$ with $T \to \hbar\beta$) and integrating over $x_f = x_i = x$ gives

$$ Z = \int dx\, K(x, -i\hbar\beta; x, 0). $$

**第 1 步 — 将配分函数与传播子联系起来。** 配分函数为 $Z = \mathrm{Tr}\, e^{-\beta\hat H} = \int dx\, \langle x|e^{-\beta\hat H}|x\rangle$。与传播子 $K(x_f, T; x_i, 0) = \langle x_f|e^{-i\hat H T/\hbar}|x_i\rangle$ 比较，令 $T = -i\hbar\beta$（即 $t \to -i\tau$，$T \to \hbar\beta$），并对 $x_f = x_i = x$ 积分，得

$$ Z = \int dx\, K(x, -i\hbar\beta; x, 0). $$

**Step 2 — Wick rotate the time-slicing derivation.** In the time-slicing derivation (Section A), replace $t_j \to -i\tau_j$. The step size becomes $\varepsilon \to -i\Delta\tau$ (with $\Delta\tau = \hbar\beta/N > 0$). The Lagrangian changes:

$$ \begin{aligned} iS/\hbar &= \frac{i}{\hbar} \int dt\, [\tfrac12 m(dx/dt)^2 - V] \to \frac{i}{\hbar} \int (-id\tau)\, [\tfrac12 m(dx/d(-i\tau))^2 - V] \\ &= -\frac{1}{\hbar} \int_0^{\hbar\beta} d\tau\, [\tfrac12 m(dx/d\tau)^2 + V(x)] = -S_E[x]/\hbar, \end{aligned} $$

where $S_E[x] = \int_0^{\hbar\beta} d\tau\, [\tfrac12 m(dx/d\tau)^2 + V(x)]$ is the **Euclidean action**. The oscillatory weight $e^{iS/\hbar}$ becomes the real Boltzmann weight $e^{-S_E/\hbar}$.

**第 2 步 — 对时间切片推导进行维克转动。** 在时间切片推导（第 A 节）中，替换 $t_j \to -i\tau_j$。步长变为 $\varepsilon \to -i\Delta\tau$（$\Delta\tau = \hbar\beta/N > 0$）。拉格朗日量改变：

$$ \begin{aligned} iS/\hbar &= \frac{i}{\hbar} \int dt\, [\tfrac12 m(dx/dt)^2 - V] \to \frac{i}{\hbar} \int (-id\tau)\, [\tfrac12 m(dx/d(-i\tau))^2 - V] \\ &= -\frac{1}{\hbar} \int_0^{\hbar\beta} d\tau\, [\tfrac12 m(dx/d\tau)^2 + V(x)] = -S_E[x]/\hbar, \end{aligned} $$

其中 $S_E[x] = \int_0^{\hbar\beta} d\tau\, [\tfrac12 m(dx/d\tau)^2 + V(x)]$ 是**欧几里得作用量**。振荡权重 $e^{iS/\hbar}$ 变为实的玻尔兹曼权重 $e^{-S_E/\hbar}$。

**Step 3 — Impose boundary conditions for bosons.** The trace $\int dx\, \langle x|\ldots|x\rangle$ means $x(\hbar\beta) = x(0)$: the path closes on itself. In a field theory, the bosonic field satisfies $\varphi(x, \tau+\hbar\beta) = \varphi(x, \tau)$ — **periodic boundary conditions**. The Matsubara (imaginary-time) frequencies are $\omega_n = 2\pi n/(\hbar\beta)$ for bosons ($n \in \mathbb{Z}$), which quantize the frequency spectrum due to the periodicity. Therefore:

$$ Z = \int_{\varphi(\tau+\hbar\beta) = \varphi(\tau)} \mathcal{D}[\varphi]\, e^{-S_E[\varphi]/\hbar}. \qquad \blacksquare $$

**第 3 步 — 对玻色子施加边界条件。** 迹 $\int dx\, \langle x|\ldots|x\rangle$ 意味着 $x(\hbar\beta) = x(0)$：路径自身封闭。在场论中，玻色子场满足 $\varphi(x, \tau+\hbar\beta) = \varphi(x, \tau)$——**周期边界条件**。松原（虚时）频率对玻色子为 $\omega_n = 2\pi n/(\hbar\beta)$（$n \in \mathbb{Z}$），由周期性量子化频率谱。因此：

$$ Z = \int_{\varphi(\tau+\hbar\beta) = \varphi(\tau)} \mathcal{D}[\varphi]\, e^{-S_E[\varphi]/\hbar}. \qquad \blacksquare $$

**Step 4 — Antiperiodic boundary conditions for fermions.** Fermionic fields $\psi(\tau)$ are Grassmann-valued (anticommuting), and the trace involves an extra minus sign from the anticommutation: $\mathrm{Tr}\, e^{-\beta\hat H} = \int d\bar\psi\, d\psi\, \langle\psi|e^{-\beta\hat H}|-\psi\rangle$ (the coherent-state path integral). The minus sign in $|-\psi\rangle$ gives the **antiperiodic** boundary condition $\psi(\tau+\hbar\beta) = -\psi(\tau)$, and fermionic Matsubara frequencies $\omega_n = (2n+1)\pi/(\hbar\beta)$ ($n \in \mathbb{Z}$) — odd multiples of $\pi/\hbar\beta$. The partition function is

$$ Z = \int_{\psi(\tau+\hbar\beta) = -\psi(\tau)} \mathcal{D}[\bar\psi, \psi]\, e^{-S_E[\bar\psi,\psi]/\hbar}. $$

**第 4 步 — 费米子的反周期边界条件。** 费米子场 $\psi(\tau)$ 是 Grassmann 值的（反对易），迹涉及来自反对易的额外负号：$\mathrm{Tr}\, e^{-\beta\hat H} = \int d\bar\psi\, d\psi\, \langle\psi|e^{-\beta\hat H}|-\psi\rangle$（相干态路径积分）。$|-\psi\rangle$ 中的负号给出**反周期**边界条件 $\psi(\tau+\hbar\beta) = -\psi(\tau)$，以及费米子松原频率 $\omega_n = (2n+1)\pi/(\hbar\beta)$（$n \in \mathbb{Z}$）——$\pi/\hbar\beta$ 的奇数倍。配分函数为

$$ Z = \int_{\psi(\tau+\hbar\beta) = -\psi(\tau)} \mathcal{D}[\bar\psi, \psi]\, e^{-S_E[\bar\psi,\psi]/\hbar}. $$

**Step 5 — Physical interpretation.** The Euclidean path integral $Z = \int \mathcal{D}[\varphi]\, e^{-S_E/\hbar}$ is formally identical to a classical statistical mechanics partition function $Z_{cl} = \int \mathcal{D}[\varphi]\, e^{-\beta F[\varphi]}$ in $d+1$ dimensions, with $\hbar\beta$ playing the role of the inverse temperature times the $(d+1)$-th extent. This is the quantum-to-classical mapping: a $d$-dimensional quantum system at temperature $T$ is equivalent to a $(d+1)$-dimensional classical system. In particular, $T = 0$ gives an infinite imaginary-time extent and a $d+1$-dimensional classical system. $\blacksquare$

**第 5 步 — 物理诠释。** 欧几里得路径积分 $Z = \int \mathcal{D}[\varphi]\, e^{-S_E/\hbar}$ 在形式上与 $d+1$ 维的经典统计力学配分函数 $Z_{cl} = \int \mathcal{D}[\varphi]\, e^{-\beta F[\varphi]}$ 完全相同，$\hbar\beta$ 扮演逆温度乘以第 $(d+1)$ 方向范围的角色。这是量子到经典的映射：温度为 $T$ 的 $d$ 维量子系统等价于 $(d+1)$ 维经典系统。特别地，$T = 0$ 给出无限虚时范围和 $d+1$ 维经典系统。$\blacksquare$

---

*The time-slicing derivation shows that the path integral is not an ansatz but a theorem: it follows by repeated insertion of resolutions of identity, followed by a Gaussian momentum integral. The Wick rotation then reveals the deep formal identity between quantum statistical mechanics and classical statistical field theory.*

*时间切片推导表明，路径积分不是一个猜测，而是一个定理：它由反复插入单位分解、再进行高斯动量积分而得到。维克转动随即揭示了量子统计力学与经典统计场论之间深刻的形式等同性。*

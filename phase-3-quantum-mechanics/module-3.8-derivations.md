---
title: "Derivations — Module 3.8: Time-Dependent Perturbation Theory & Scattering"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.8: Time-Dependent Perturbation Theory & Scattering
# 推导 — 模块 3.8：含时微扰理论与散射

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.8](./module-3.8-time-dependent-perturbation-theory-and-scattering.md). Full step-by-step proofs of the first-order transition amplitude, Fermi's golden rule, the Born approximation, and the differential cross section. English first, then 中文.
> [模块 3.8](./module-3.8-time-dependent-perturbation-theory-and-scattering.md) 的配套文档：一阶跃迁振幅、费米黄金定则、玻恩近似与微分散射截面的完整逐步证明。先英文，后中文。

---

## A. First-Order Transition Amplitude · 一阶跃迁振幅

**Claim.** Given a system initially in eigenstate $|i\rangle$ of the unperturbed Hamiltonian $\hat{H}_0$, subjected to a perturbation $\hat{H}'(t)$ switched on at $t = 0$, the first-order probability amplitude to find the system in a different eigenstate $|f\rangle$ at time $t$ is:

**命题。** 设系统初始处于无微扰哈密顿量 $\hat{H}_0$ 的本征态 $|i\rangle$，在 $t = 0$ 时刻开始施加微扰 $\hat{H}'(t)$，则在 $t$ 时刻发现系统处于另一本征态 $|f\rangle$ 的一阶概率振幅为：

$$ c_f^{(1)}(t) = \frac{1}{i\hbar} \int_0^t \langle f|\hat{H}'(t')|i\rangle\, e^{i\omega_{fi}t'}\, dt', $$

where $\omega_{fi} = (E_f - E_i)/\hbar$ is the Bohr frequency.

其中 $\omega_{fi} = (E_f - E_i)/\hbar$ 为玻尔频率。

**Step 1 — Interaction picture.** Split the full Hamiltonian as $\hat{H}(t) = \hat{H}_0 + \hat{H}'(t)$. In the interaction picture, the state is

**第 1 步 — 相互作用绘景。** 将全哈密顿量分解为 $\hat{H}(t) = \hat{H}_0 + \hat{H}'(t)$。在相互作用绘景中，态定义为

$$ |\psi_I(t)\rangle = e^{i\hat{H}_0 t/\hbar} |\psi_S(t)\rangle, $$

which removes the "free" time evolution $e^{-i\hat{H}_0 t/\hbar}$. The Schrödinger equation for $|\psi_S\rangle$ transforms to

它去除了"自由"演化因子 $e^{-i\hat{H}_0 t/\hbar}$。$|\psi_S\rangle$ 的薛定谔方程变换为

$$ i\hbar \frac{d}{dt} |\psi_I(t)\rangle = \hat{H}_I'(t) |\psi_I(t)\rangle, $$

where $\hat{H}_I'(t) = e^{i\hat{H}_0 t/\hbar} \hat{H}'(t) e^{-i\hat{H}_0 t/\hbar}$ is the perturbation in the interaction picture.

其中 $\hat{H}_I'(t) = e^{i\hat{H}_0 t/\hbar} \hat{H}'(t) e^{-i\hat{H}_0 t/\hbar}$ 为相互作用绘景中的微扰。

**Step 2 — Expand in the unperturbed basis.** Write $|\psi_I(t)\rangle = \sum_n c_n(t)|n\rangle$, where $\{|n\rangle\}$ are the orthonormal eigenstates of $\hat{H}_0$ with $\hat{H}_0|n\rangle = E_n|n\rangle$. The initial condition is $c_n(0) = \delta_{ni}$ (system starts in $|i\rangle$). Substituting into the equation of motion:

**第 2 步 — 在无微扰基中展开。** 写 $|\psi_I(t)\rangle = \sum_n c_n(t)|n\rangle$，其中 $\{|n\rangle\}$ 为 $\hat{H}_0$ 的正交归一本征态，$\hat{H}_0|n\rangle = E_n|n\rangle$。初始条件为 $c_n(0) = \delta_{ni}$（系统从 $|i\rangle$ 出发）。代入运动方程：

$$ i\hbar \sum_n \dot{c}_n(t)|n\rangle = \hat{H}_I'(t) \sum_n c_n(t)|n\rangle. $$

Project onto $\langle f|$:

投影到 $\langle f|$：

$$ i\hbar\, \dot{c}_f(t) = \sum_n \langle f|\hat{H}_I'(t)|n\rangle\, c_n(t). $$

**Step 3 — Evaluate the matrix element.** Since $\hat{H}_I'(t) = e^{i\hat{H}_0 t/\hbar} \hat{H}'(t) e^{-i\hat{H}_0 t/\hbar}$, sandwiching between eigenstates gives

**第 3 步 — 计算矩阵元。** 由于 $\hat{H}_I'(t) = e^{i\hat{H}_0 t/\hbar} \hat{H}'(t) e^{-i\hat{H}_0 t/\hbar}$，夹在本征态之间得

$$ \langle f|\hat{H}_I'(t)|n\rangle = e^{iE_f t/\hbar} \langle f|\hat{H}'(t)|n\rangle\, e^{-iE_n t/\hbar} = \langle f|\hat{H}'(t)|n\rangle\, e^{i(E_f - E_n)t/\hbar}. $$

**Step 4 — First-order perturbation theory.** To zeroth order $c_n(t) \approx \delta_{ni}$ (no transition). Substituting this into the right-hand side gives the first-order equation:

**第 4 步 — 一阶微扰理论。** 零阶近似为 $c_n(t) \approx \delta_{ni}$（无跃迁）。将此代入右端得一阶方程：

$$ i\hbar\, \dot{c}_f^{(1)}(t) = \langle f|\hat{H}'(t)|i\rangle\, e^{i\omega_{fi}t}, $$

where $\omega_{fi} = (E_f - E_i)/\hbar$. Integrating from $0$ to $t$ with $c_f^{(1)}(0) = 0$ ($f \ne i$):

其中 $\omega_{fi} = (E_f - E_i)/\hbar$。从 $0$ 积分到 $t$，初始条件 $c_f^{(1)}(0) = 0$（$f \ne i$）：

$$ c_f^{(1)}(t) = \frac{1}{i\hbar} \int_0^t \langle f|\hat{H}'(t')|i\rangle\, e^{i\omega_{fi}t'}\, dt'. \qquad \blacksquare $$

The transition probability is $P_{i\to f}(t) = |c_f^{(1)}(t)|^2$.

跃迁概率为 $P_{i\to f}(t) = |c_f^{(1)}(t)|^2$。$\blacksquare$

---

## B. Fermi's Golden Rule · 费米黄金定则

**Claim.** For a constant (or slowly varying) perturbation $\hat{H}'$ turned on at $t = 0$, the transition rate into a continuum of final states with density of states $\rho(E_f)$ is:

**命题。** 对于在 $t = 0$ 时接通的常数（或缓变）微扰 $\hat{H}'$，跃迁到末态密度为 $\rho(E_f)$ 的连续谱的速率为：

$$ \Gamma_{i\to f} = \frac{2\pi}{\hbar} |\langle f|\hat{H}'|i\rangle|^2\, \rho(E_f). $$

**Step 1 — Evaluate the integral for a constant perturbation.** Take $\hat{H}'(t) = \hat{H}'$ (time-independent). Then:

**第 1 步 — 对常数微扰计算积分。** 取 $\hat{H}'(t) = \hat{H}'$（与时间无关）。则：

$$ \begin{aligned} c_f^{(1)}(t) &= \frac{1}{i\hbar} \langle f|\hat{H}'|i\rangle \int_0^t e^{i\omega_{fi}t'}\, dt' \\ &= \frac{1}{i\hbar} \langle f|\hat{H}'|i\rangle \cdot \frac{e^{i\omega_{fi}t} - 1}{i\omega_{fi}} \\ &= \frac{\langle f|\hat{H}'|i\rangle}{\hbar} \cdot e^{i\omega_{fi}t/2} \cdot \frac{2 \sin(\omega_{fi}t/2)}{\omega_{fi}}. \end{aligned} $$

**Step 2 — Transition probability.** Taking the modulus squared:

**第 2 步 — 跃迁概率。** 取模平方：

$$ \begin{aligned} P_{i\to f}(t) &= |c_f^{(1)}(t)|^2 \\ &= \frac{|\langle f|\hat{H}'|i\rangle|^2}{\hbar^2} \cdot \frac{4 \sin^2(\omega_{fi}t/2)}{\omega_{fi}^2} \\ &= \frac{|\langle f|\hat{H}'|i\rangle|^2}{\hbar^2} \cdot t^2 \cdot \operatorname{sinc}^2(\omega_{fi}t/2), \end{aligned} $$

where $\operatorname{sinc}(x) = \sin(x)/x$. Equivalently, using $\omega_{fi} = (E_f - E_i)/\hbar$:

其中 $\operatorname{sinc}(x) = \sin(x)/x$。等价地，利用 $\omega_{fi} = (E_f - E_i)/\hbar$：

$$ \begin{aligned} P_{i\to f}(t) &= \frac{|\langle f|\hat{H}'|i\rangle|^2}{\hbar^2} \cdot \frac{4 \sin^2((E_f - E_i)t/2\hbar)}{(E_f - E_i)^2/\hbar^2} \\ &= \frac{4|\langle f|\hat{H}'|i\rangle|^2}{\hbar^2} \cdot \frac{\sin^2((E_f - E_i)t/2\hbar)}{((E_f - E_i)/\hbar)^2}. \end{aligned} $$

**Step 3 — The $\operatorname{sinc}^2 \to$ delta function limit.** The key identity is: for large $t$,

**第 3 步 — $\operatorname{sinc}^2$ 趋向 $\delta$ 函数的极限。** 关键恒等式为：当 $t \to \infty$ 时，

$$ \frac{t}{2\pi} \cdot \frac{4 \sin^2(\omega t/2)}{(\omega t)^2} = \frac{t}{\pi} \cdot \frac{\sin^2(\omega t/2)}{(\omega t/2)^2} \to \delta(\omega) \quad \text{as } t \to \infty. $$

More precisely, $(1/\pi) \cdot \sin^2(xt)/x^2 \to t\delta(x)$ in the distributional sense as $t \to \infty$ (it integrates to $t$ and peaks sharply at $x = 0$ with width $\sim 1/t$). Converting from $\omega$ to energy using $\delta(\omega_{fi}) = \hbar\, \delta(E_f - E_i)$:

更精确地，$(1/\pi) \cdot \sin^2(xt)/x^2$ 在分布意义下当 $t \to \infty$ 时趋向 $t\delta(x)$（其积分为 $t$，在 $x = 0$ 处急剧峰化，宽度 $\sim 1/t$）。利用 $\delta(\omega_{fi}) = \hbar\, \delta(E_f - E_i)$ 将 $\omega$ 转化为能量：

$$ \frac{4}{\hbar^2} \frac{\sin^2((E_f - E_i)t/2\hbar)}{(E_f - E_i)^2/\hbar^2} \to \frac{2\pi t}{\hbar}\, \delta(E_f - E_i). $$

We evaluate the integral of this factor over all final-state frequencies. Substitute $v = \omega_{fi} t/2$, so $d\omega_{fi} = 2\,dv/t$:

我们对该因子在所有末态频率上积分。代入 $v = \omega_{fi} t/2$，则 $d\omega_{fi} = 2\,dv/t$：

$$ \begin{aligned} \int_{-\infty}^{\infty} \frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}\, d\omega_{fi} &= \int_{-\infty}^{\infty} \frac{4\sin^2(v)}{(2v/t)^2} \cdot \frac{2\,dv}{t} \\ &= \int_{-\infty}^{\infty} \frac{4\sin^2(v)\, t^2}{4v^2} \cdot \frac{2}{t}\, dv \\ &= 2t \int_{-\infty}^{\infty} \frac{\sin^2(v)}{v^2}\, dv = 2t \cdot \pi = 2\pi t, \end{aligned} $$

using the standard result $\int_{-\infty}^{\infty} \sin^2(v)/v^2\, dv = \pi$.

其中用到标准结果 $\int_{-\infty}^{\infty} \sin^2(v)/v^2\, dv = \pi$。

Hence as a function of $\omega_{fi}$ the factor $4\sin^2(\omega_{fi}t/2)/\omega_{fi}^2 \to 2\pi t \cdot \delta(\omega_{fi})$ as $t \to \infty$, confirming

因此作为 $\omega_{fi}$ 的函数，当 $t \to \infty$ 时 $4\sin^2(\omega_{fi}t/2)/\omega_{fi}^2 \to 2\pi t \cdot \delta(\omega_{fi})$，从而确认

$$ P_{i\to f}(t) \to \frac{|\langle f|\hat{H}'|i\rangle|^2}{\hbar^2} \cdot 2\pi t \cdot \delta(\omega_{fi}) = \frac{2\pi t}{\hbar} |\langle f|\hat{H}'|i\rangle|^2 \cdot \delta(E_f - E_i). $$

**Step 4 — Integrate over the density of final states.** The total transition rate $\Gamma = dP/dt$ sums over all accessible final states. For a continuous spectrum with density of states $\rho(E_f)$ (number of states per unit energy near $E_f$), integrate:

**第 4 步 — 对末态密度积分。** 总跃迁速率 $\Gamma = dP/dt$ 对所有可及末态求和。对于末态密度为 $\rho(E_f)$ 的连续谱（每单位能量附近的态数），积分：

$$ \begin{aligned} \Gamma = \frac{dP_\text{total}}{dt} &= \frac{d}{dt} \int P_{i\to f}(t)\, \rho(E_f)\, dE_f \\ &= \int \frac{2\pi}{\hbar} |\langle f|\hat{H}'|i\rangle|^2\, \delta(E_f - E_i)\, \rho(E_f)\, dE_f. \end{aligned} $$

The delta function enforces energy conservation $E_f = E_i$, so:

$\delta$ 函数强制能量守恒 $E_f = E_i$，故：

$$ \boxed{\, \Gamma = \frac{2\pi}{\hbar} |\langle f|\hat{H}'|i\rangle|^2\, \rho(E_i) \,} $$

Here $\rho(E_i)$ is the density of final states evaluated at the initial energy — Fermi's golden rule. $\blacksquare$

此处 $\rho(E_i)$ 为在初态能量处计算的末态密度——即费米黄金定则。$\blacksquare$

**Domain conditions.** The derivation requires: (i) the perturbation matrix element is approximately constant over the energy width $\sim \hbar/t$ that contributes, (ii) $t$ is large enough that the $\operatorname{sinc}^2$ peak is sharp compared to variations in $|\langle f|\hat{H}'|i\rangle|^2$ and $\rho$, but (iii) $t$ is short enough that first-order perturbation theory remains valid: $|c_f^{(1)}|^2 \ll 1$.

**定义域条件。** 推导需要：（i）在宽度约 $\hbar/t$ 的能量范围内微扰矩阵元近似为常数；（ii）$t$ 足够大使得 $\operatorname{sinc}^2$ 峰相比 $|\langle f|\hat{H}'|i\rangle|^2$ 和 $\rho$ 的变化是尖锐的；但（iii）$t$ 足够小使得一阶微扰理论仍然有效：$|c_f^{(1)}|^2 \ll 1$。

---

## C. The Born Approximation for Scattering · 散射的玻恩近似

**Claim.** For a particle of mass $m$ scattered by a potential $V(\mathbf{r})$ at wavevector $\mathbf{k}$ (incident plane wave $e^{i\mathbf{k}\cdot\mathbf{r}}$), the first Born approximation gives the scattering amplitude:

**命题。** 质量为 $m$ 的粒子以波矢 $\mathbf{k}$ 被势 $V(\mathbf{r})$ 散射（入射平面波 $e^{i\mathbf{k}\cdot\mathbf{r}}$），一阶玻恩近似给出散射振幅：

$$ f(\theta) = -\frac{m}{2\pi\hbar^2} \int V(\mathbf{r})\, e^{i\mathbf{q}\cdot\mathbf{r}}\, d^3r = -\frac{m}{2\pi\hbar^2} \tilde{V}(\mathbf{q}), $$

where $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ is the momentum transfer (with $|\mathbf{k}| = |\mathbf{k}'| = k$ for elastic scattering) and $\tilde{V}(\mathbf{q})$ is the Fourier transform of $V$.

其中 $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ 为动量转移（对弹性散射 $|\mathbf{k}| = |\mathbf{k}'| = k$），$\tilde{V}(\mathbf{q})$ 为 $V$ 的傅里叶变换。

**Step 1 — The Lippmann–Schwinger equation.** The full stationary scattering state satisfies

**第 1 步 — Lippmann–Schwinger 方程。** 完整的定态散射态满足

$$ (\hat{H}_0 + V)|\psi\rangle = E|\psi\rangle, \quad \text{i.e.} \quad (E - \hat{H}_0)|\psi\rangle = V|\psi\rangle. $$

The formal solution incorporating the incident plane wave $|\mathbf{k}\rangle$ (eigenstate of $\hat{H}_0$ with eigenvalue $E = \hbar^2 k^2/2m$) and an outgoing-wave boundary condition (Green's function with $+i\varepsilon$ prescription) is:

正式解（包含入射平面波 $|\mathbf{k}\rangle$，即 $\hat{H}_0$ 的本征态，本征值 $E = \hbar^2 k^2/2m$，以及出射波边界条件，$+i\varepsilon$ 格林函数）为：

$$ |\psi^+\rangle = |\mathbf{k}\rangle + (E - \hat{H}_0 + i\varepsilon)^{-1} V |\psi^+\rangle. $$

In position space, the Green's function $G_0^+(\mathbf{r},\mathbf{r}') = \langle\mathbf{r}|(E - \hat{H}_0 + i\varepsilon)^{-1}|\mathbf{r}'\rangle$ for the free particle equals

在坐标空间，自由粒子的格林函数 $G_0^+(\mathbf{r},\mathbf{r}') = \langle\mathbf{r}|(E - \hat{H}_0 + i\varepsilon)^{-1}|\mathbf{r}'\rangle$ 等于

$$ G_0^+(\mathbf{r},\mathbf{r}') = -\frac{2m}{\hbar^2} \cdot \frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|}. $$

This is verified by acting $(\nabla^2 + k^2)$ on it: $(\nabla^2 + k^2)G_0^+(\mathbf{r},\mathbf{r}') = -(2m/\hbar^2)\delta^3(\mathbf{r} - \mathbf{r}')$ (the defining equation for the Green's function of $-\hbar^2\nabla^2/2m - E$).

通过作用 $(\nabla^2 + k^2)$ 于其上可验证：$(\nabla^2 + k^2)G_0^+(\mathbf{r},\mathbf{r}') = -(2m/\hbar^2)\delta^3(\mathbf{r} - \mathbf{r}')$（即 $-\hbar^2\nabla^2/2m - E$ 的格林函数的定义方程）。

**Step 2 — Position-space integral equation.** In coordinate representation:

**第 2 步 — 坐标空间积分方程。** 在坐标表象中：

$$ \psi(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} - \frac{m}{2\pi\hbar^2} \int \frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|} V(\mathbf{r}')\, \psi(\mathbf{r}')\, d^3r'. $$

**Step 3 — Far-field (large $r$) limit.** For $r \gg r'$ (detector far from scattering center), expand:

**第 3 步 — 远场（大 $r$）极限。** 当 $r \gg r'$（探测器远离散射中心），展开：

$$ |\mathbf{r} - \mathbf{r}'| = r\sqrt{1 - 2\mathbf{r}\cdot\mathbf{r}'/r^2 + r'^2/r^2} \approx r - \hat{\mathbf{r}}\cdot\mathbf{r}' + O(r'^2/r). $$

Hence $e^{ik|\mathbf{r}-\mathbf{r}'|}/|\mathbf{r}-\mathbf{r}'| \approx (e^{ikr}/r)\, e^{-i\mathbf{k}'\cdot\mathbf{r}'}$, where $\mathbf{k}' = k\hat{\mathbf{r}}$ is the scattered wavevector (pointing toward the detector). Substituting:

因此 $e^{ik|\mathbf{r}-\mathbf{r}'|}/|\mathbf{r}-\mathbf{r}'| \approx (e^{ikr}/r)\, e^{-i\mathbf{k}'\cdot\mathbf{r}'}$，其中 $\mathbf{k}' = k\hat{\mathbf{r}}$ 为指向探测器的散射波矢。代入：

$$ \psi(\mathbf{r}) \approx e^{i\mathbf{k}\cdot\mathbf{r}} + f(\theta)\, \frac{e^{ikr}}{r}, $$

where the scattering amplitude is

其中散射振幅为

$$ f(\theta) = -\frac{m}{2\pi\hbar^2} \int e^{-i\mathbf{k}'\cdot\mathbf{r}'} V(\mathbf{r}')\, \psi(\mathbf{r}')\, d^3r'. $$

**Step 4 — First Born approximation.** In the Born approximation, $\psi(\mathbf{r}') \approx e^{i\mathbf{k}\cdot\mathbf{r}'}$ (replace the full scattering state by the incident plane wave — valid when $V$ is weak). Then:

**第 4 步 — 一阶玻恩近似。** 在玻恩近似中，用入射平面波替代完整散射态 $\psi(\mathbf{r}') \approx e^{i\mathbf{k}\cdot\mathbf{r}'}$（当 $V$ 较弱时有效）。则：

$$ \begin{aligned} f(\theta) &= -\frac{m}{2\pi\hbar^2} \int e^{-i\mathbf{k}'\cdot\mathbf{r}'} V(\mathbf{r}')\, e^{i\mathbf{k}\cdot\mathbf{r}'}\, d^3r' \\ &= -\frac{m}{2\pi\hbar^2} \int V(\mathbf{r}')\, e^{i(\mathbf{k}-\mathbf{k}')\cdot\mathbf{r}'}\, d^3r' \\ &= -\frac{m}{2\pi\hbar^2} \int V(\mathbf{r})\, e^{i\mathbf{q}\cdot\mathbf{r}}\, d^3r \\ &= -\frac{m}{2\pi\hbar^2} \tilde{V}(\mathbf{q}), \end{aligned} $$

where $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ is the momentum transfer. For elastic scattering with $|\mathbf{k}| = |\mathbf{k}'| = k$, the magnitude is $|\mathbf{q}| = 2k \sin(\theta/2)$, where $\theta$ is the scattering angle. $\blacksquare$

其中 $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ 为动量转移。对弹性散射 $|\mathbf{k}| = |\mathbf{k}'| = k$，其大小为 $|\mathbf{q}| = 2k \sin(\theta/2)$，$\theta$ 为散射角。$\blacksquare$

**Validity condition.** The Born approximation requires $|V| \ll \hbar^2 k^2/2m = E$ (the potential energy is small compared to the kinetic energy) — more precisely, $|(m/2\pi\hbar^2)\int e^{i\mathbf{q}\cdot\mathbf{r}} V(\mathbf{r})/|\mathbf{r}|\, d^3r| \ll 1$.

**有效条件。** 玻恩近似要求 $|V| \ll \hbar^2 k^2/2m = E$（势能远小于动能）——更精确地，$|(m/2\pi\hbar^2)\int e^{i\mathbf{q}\cdot\mathbf{r}} V(\mathbf{r})/|\mathbf{r}|\, d^3r| \ll 1$。

---

## D. Differential Cross Section · 微分散射截面

**Claim.** The differential cross section is related to the scattering amplitude by:

**命题。** 微分散射截面与散射振幅的关系为：

$$ \frac{d\sigma}{d\Omega} = |f(\theta)|^2. $$

**Step 1 — Definition of cross section.** The differential cross section $d\sigma/d\Omega$ is defined such that the number of particles scattered per unit time into solid angle $d\Omega$ around direction $(\theta,\phi)$ equals

**第 1 步 — 截面的定义。** 微分散射截面 $d\sigma/d\Omega$ 定义为：单位时间内散射到方向 $(\theta,\phi)$ 的立体角 $d\Omega$ 中的粒子数等于

$$ dN = J_\text{inc} \cdot \frac{d\sigma}{d\Omega}\, d\Omega, $$

where $J_\text{inc}$ is the incident probability current (particles per unit area per unit time). For an incident plane wave $\psi_\text{inc} = e^{ikz}$, $J_\text{inc} = \hbar k/m$.

其中 $J_\text{inc}$ 为入射概率流（单位面积单位时间的粒子数）。对入射平面波 $\psi_\text{inc} = e^{ikz}$，$J_\text{inc} = \hbar k/m$。

**Step 2 — Scattered probability current.** At large $r$ the scattered wave is $\psi_\text{sc} = f(\theta) e^{ikr}/r$. The radial component of its probability current is:

**第 2 步 — 散射概率流。** 在大 $r$ 处散射波为 $\psi_\text{sc} = f(\theta) e^{ikr}/r$。其概率流的径向分量为：

$$ \begin{aligned} J_\text{sc} &= \frac{\hbar}{m} \operatorname{Im}\!\Big(\psi_\text{sc}^* \frac{\partial\psi_\text{sc}}{\partial r}\Big) \\ &= \frac{\hbar}{m} \operatorname{Im}\!\Big(\frac{f^*(\theta)}{r} e^{-ikr} \cdot \frac{ik f(\theta)}{r} e^{ikr}\Big) \\ &= \frac{\hbar k}{m} \frac{|f(\theta)|^2}{r^2}. \end{aligned} $$

**Step 3 — Count scattered particles.** The flux through the area element $r^2\, d\Omega$ at distance $r$ (which captures all particles scattered into $d\Omega$) is:

**第 3 步 — 统计散射粒子。** 通过距离 $r$ 处面积元 $r^2\, d\Omega$ 的流量（捕获所有散射到 $d\Omega$ 中的粒子）为：

$$ \frac{dN}{dt} = J_\text{sc} \cdot r^2\, d\Omega = \frac{\hbar k}{m} |f(\theta)|^2\, d\Omega. $$

**Step 4 — Divide by incident flux.**

**第 4 步 — 除以入射流量。**

$$ \frac{d\sigma}{d\Omega} = \frac{dN/dt}{J_\text{inc}\, d\Omega} = \frac{(\hbar k/m)|f(\theta)|^2\, d\Omega}{(\hbar k/m)\, d\Omega} = \boxed{\, |f(\theta)|^2 \,}. \qquad \blacksquare $$

This result is exact (not a Born approximation): whatever $f(\theta)$ is (whether computed from Born, partial waves, or otherwise), $d\sigma/d\Omega = |f(\theta)|^2$.

此结果是精确的（不是玻恩近似）：无论 $f(\theta)$ 如何计算（玻恩、分波或其他方法），$d\sigma/d\Omega = |f(\theta)|^2$ 均成立。$\blacksquare$

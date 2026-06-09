---
title: "Derivations — Module 2.8: Brownian Motion & the Einstein Relation"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.8: Brownian Motion & the Einstein Relation
# 推导 — 模块 2.8：布朗运动与爱因斯坦关系

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.8](./module-2.8-brownian-motion-and-the-einstein-relation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.8](./module-2.8-brownian-motion-and-the-einstein-relation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Mean-Square Displacement $\langle x^2\rangle = 2Dt$ from the Diffusion Equation · 从扩散方程推导均方位移 $\langle x^2\rangle = 2Dt$

**Claim.** For a particle undergoing diffusion described by $\partial P/\partial t = D\, \partial^2 P/\partial x^2$, starting at $x = 0$, the mean-square displacement is $\langle x^2(t)\rangle = 2Dt$.

**命题。** 对于由扩散方程 $\partial P/\partial t = D\, \partial^2 P/\partial x^2$ 描述的粒子，从 $x = 0$ 出发，均方位移为 $\langle x^2(t)\rangle = 2Dt$。

**Step 1 — Solve the diffusion equation with a delta-function initial condition.** Start with $P(x, 0) = \delta(x)$ (particle starts at origin). The diffusion equation $\partial P/\partial t = D\, \partial^2 P/\partial x^2$ has a Gaussian solution (verified by direct substitution):

**第 1 步 — 用 $\delta$ 函数初始条件求解扩散方程。** 取 $P(x, 0) = \delta(x)$（粒子从原点出发）。扩散方程 $\partial P/\partial t = D\, \partial^2 P/\partial x^2$ 有高斯解（可直接代入验证）：

$$ P(x, t) = (1/\sqrt{4\pi Dt})\, \exp(-x^2/(4Dt)). $$

Check: at $t \to 0$, this narrows to $\delta(x)$. Normalization: $\int_{-\infty}^{\infty} P(x,t)\, dx = 1$ for all $t$ (by the Gaussian integral). The mean: $\langle x\rangle = 0$ by symmetry (odd integrand).

验证：当 $t \to 0$ 时，此式收缩为 $\delta(x)$。归一化：对所有 $t$，$\int_{-\infty}^{\infty} P(x,t)\, dx = 1$（由高斯积分）。均值：$\langle x\rangle = 0$（由对称性，被积函数为奇函数）。

**Step 2 — Compute $\langle x^2\rangle$ directly from the solution.**

**第 2 步 — 直接从解计算 $\langle x^2\rangle$。**

$$ \langle x^2\rangle = \int_{-\infty}^{\infty} x^2\, P(x, t)\, dx = (1/\sqrt{4\pi Dt}) \int_{-\infty}^{\infty} x^2\, e^{-x^2/(4Dt)}\, dx. $$

Use the Gaussian integral $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\, dx = (\sqrt{\pi})/(2a^{3/2})$ with $a = 1/(4Dt)$:

利用高斯积分 $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\, dx = (\sqrt{\pi})/(2a^{3/2})$，令 $a = 1/(4Dt)$：

$$ \begin{aligned} \langle x^2\rangle &= (1/\sqrt{4\pi Dt}) \cdot \sqrt{\pi} / [2\cdot(1/(4Dt))^{3/2}] \\ &= (1/\sqrt{4\pi Dt}) \cdot \sqrt{\pi} \cdot 2 \cdot (4Dt)^{3/2} / 4 \\ &= (1/\sqrt{4\pi Dt}) \cdot \sqrt{\pi} \cdot (4Dt) \cdot \sqrt{4Dt} / 2 \\ &= (1/\sqrt{4\pi Dt}) \cdot \sqrt{\pi Dt} \cdot 4Dt \cdot (1/2) \\ &\quad [\text{More directly: } 1/(\sqrt{4\pi Dt}) \cdot (\sqrt{\pi}/(2)) \cdot (4Dt)^{3/2} = (1/\sqrt{4\pi Dt}) \cdot (\sqrt{\pi}/2) \cdot (4Dt)\sqrt{4Dt}] \end{aligned} $$

Let us use the simpler route: set $u = x/\sqrt{4Dt}$, so $x = u\sqrt{4Dt}$, $dx = \sqrt{4Dt}\, du$:

用更简洁的方法：令 $u = x/\sqrt{4Dt}$，则 $x = u\sqrt{4Dt}$，$dx = \sqrt{4Dt}\, du$：

$$ \begin{aligned} \langle x^2\rangle &= (1/\sqrt{4\pi Dt}) \int_{-\infty}^{\infty} u^2(4Dt)\, e^{-u^2}\, \sqrt{4Dt}\, du \\ &= (4Dt)^{3/2}/\sqrt{4\pi Dt} \int_{-\infty}^{\infty} u^2\, e^{-u^2}\, du \\ &= (4Dt)/\sqrt{\pi} \cdot \int_{-\infty}^{\infty} u^2\, e^{-u^2}\, du. \end{aligned} $$

Standard integral: $\int_{-\infty}^{\infty} u^2 e^{-u^2}\, du = \sqrt{\pi}/2$. Therefore:

标准积分：$\int_{-\infty}^{\infty} u^2 e^{-u^2}\, du = \sqrt{\pi}/2$。因此：

$$ \langle x^2\rangle = (4Dt)/\sqrt{\pi} \cdot \sqrt{\pi}/2 = \boxed{\, 2Dt. \,} \qquad \blacksquare $$

**Step 3 — Alternative derivation via the equation of motion for $\langle x^2\rangle$.** Multiply the diffusion equation $\partial P/\partial t = D\, \partial^2 P/\partial x^2$ by $x^2$ and integrate over all $x$:

**第 3 步 — 通过 $\langle x^2\rangle$ 的运动方程的另一种推导。** 将扩散方程 $\partial P/\partial t = D\, \partial^2 P/\partial x^2$ 乘以 $x^2$ 并对所有 $x$ 积分：

$$ d\langle x^2\rangle/dt = D \int x^2\, \partial^2 P/\partial x^2\, dx. $$

Integrate by parts twice (boundary terms vanish):

分部积分两次（边界项为零）：

$$ \int x^2\, \partial^2 P/\partial x^2\, dx = [x^2\, \partial P/\partial x]_{-\infty}^{\infty} - 2\int x\, \partial P/\partial x\, dx = -2[xP]_{-\infty}^{\infty} + 2\int P\, dx = 2. $$

Therefore $d\langle x^2\rangle/dt = 2D$, which integrates immediately to $\langle x^2(t)\rangle = 2Dt$ (with $\langle x^2(0)\rangle = 0$). $\blacksquare$

因此 $d\langle x^2\rangle/dt = 2D$，直接积分得 $\langle x^2(t)\rangle = 2Dt$（初始条件 $\langle x^2(0)\rangle = 0$）。$\blacksquare$

**Step 4 — Connection to random walk.** Consider $N$ independent steps of duration $\tau$ each, with step sizes drawn from a distribution with zero mean and variance $\langle(\Delta x)^2\rangle = 2D\tau$. After time $t = N\tau$, the Central Limit Theorem gives $\langle x^2\rangle = N\langle(\Delta x)^2\rangle = (t/\tau)(2D\tau) = 2Dt$. The Gaussian distribution $P(x,t)$ is the continuum limit of this random walk, as $N \to \infty$ with $\tau \to 0$ and $D\tau$ fixed. $\blacksquare$

**第 4 步 — 与随机游走的联系。** 考虑 $N$ 个各自持续时间为 $\tau$ 的独立步骤，步长从均值为零、方差为 $\langle(\Delta x)^2\rangle = 2D\tau$ 的分布中抽取。经过时间 $t = N\tau$ 后，中心极限定理给出 $\langle x^2\rangle = N\langle(\Delta x)^2\rangle = (t/\tau)(2D\tau) = 2Dt$。高斯分布 $P(x,t)$ 是该随机游走在 $N \to \infty$、$\tau \to 0$ 且 $D\tau$ 固定时的连续极限。$\blacksquare$

---

## B. Einstein Relation $D = \mu k_B T$ · 爱因斯坦关系 $D = \mu k_B T$

**Claim.** For a Brownian particle in a fluid at temperature $T$ with mobility $\mu$ (drift velocity per unit applied force), the diffusion coefficient satisfies $D = \mu k_B T$.

**命题。** 对于在温度为 $T$ 的流体中运动的布朗粒子，其迁移率为 $\mu$（单位力作用下的漂移速度），扩散系数满足 $D = \mu k_B T$。

**Step 1 — Set up the equilibrium condition.** Place the Brownian particle in a potential $V(x) = mgx$ (a small gravitational or external potential gradient). In equilibrium, the particle density $n(x)$ must satisfy the Boltzmann distribution:

**第 1 步 — 建立平衡条件。** 将布朗粒子置于势场 $V(x) = mgx$（小的重力或外部势梯度）中。平衡时，粒子密度 $n(x)$ 必须满足玻尔兹曼分布：

$$ n(x) = n_0\, e^{-V(x)/k_B T} = n_0\, e^{-mgx/k_B T}. $$

**Step 2 — Equilibrium requires zero net flux.** In equilibrium, the total particle flux $J = 0$. There are two competing fluxes:

**第 2 步 — 平衡要求总通量为零。** 在平衡时，总粒子通量 $J = 0$。存在两个相互竞争的通量：

$$ \text{(i) Diffusion flux (Fick's law, opposing the density gradient):} \quad J_{\text{diff}} = -D\, dn/dx, $$
$$ \text{(ii) Drift flux (due to force } F = -dV/dx = -mg \text{ on the particle):} \quad J_{\text{drift}} = n \cdot v_{\text{drift}} = n \cdot \mu F = -n\mu mg. $$

Setting $J_{\text{diff}} + J_{\text{drift}} = 0$:

令 $J_{\text{diff}} + J_{\text{drift}} = 0$：

$$ -D\, dn/dx - n\mu mg = 0. $$

**Step 3 — Substitute the Boltzmann distribution.** From $n(x) = n_0\, e^{-mgx/k_B T}$:

**第 3 步 — 代入玻尔兹曼分布。** 由 $n(x) = n_0\, e^{-mgx/k_B T}$：

$$ dn/dx = n_0\, e^{-mgx/k_B T} \cdot (-mg/k_B T) = -(mg/k_B T)\, n. $$

Substituting into the zero-flux condition:

代入零通量条件：

$$ \begin{aligned} -D \cdot (-mg/k_B T)\, n - n\mu mg &= 0, \\ (D/k_B T - \mu)\, nmg &= 0. \end{aligned} $$

Since $n \ne 0$ and $mg \ne 0$, we must have

由于 $n \ne 0$ 且 $mg \ne 0$，必须有

$$ D/k_B T = \mu, \quad \text{i.e.,} \quad \boxed{\, D = \mu k_B T. \,} \qquad \blacksquare $$

**Step 4 — Physical interpretation.** The Einstein relation $D = \mu k_B T$ says that the random diffusive spreading ($D$) and the deterministic drift response ($\mu$) are both caused by the same underlying molecular collisions: $D$ measures how strongly collisions randomize the particle's position, while $\mu = 1/\gamma$ (where $\gamma$ is the friction coefficient) measures how strongly collisions oppose directed motion. The ratio $D/\mu = k_B T$ is purely thermodynamic — it depends only on the temperature, not on the details of the particle or the fluid.

**第 4 步 — 物理诠释。** 爱因斯坦关系 $D = \mu k_B T$ 表明：随机扩散扩展（$D$）和确定性漂移响应（$\mu$）均由相同的底层分子碰撞引起：$D$ 衡量碰撞使粒子位置随机化的强度，而 $\mu = 1/\gamma$（$\gamma$ 为摩擦系数）衡量碰撞阻碍定向运动的强度。比值 $D/\mu = k_B T$ 纯粹是热力学的——它只依赖于温度，而不依赖于粒子或流体的细节。

---

## C. Stokes–Einstein Relation and Avogadro's Number · 斯托克斯–爱因斯坦关系与阿伏加德罗常数

**Claim.** For a spherical particle of radius $r$ in a fluid of viscosity $\eta$, the Stokes drag gives mobility $\mu = 1/(6\pi\eta r)$, so $D = k_B T/(6\pi\eta r)$.

**命题。** 对于粘度为 $\eta$ 的流体中半径为 $r$ 的球形粒子，斯托克斯阻力给出迁移率 $\mu = 1/(6\pi\eta r)$，故 $D = k_B T/(6\pi\eta r)$。

**Step 1 — Stokes' law.** For a sphere of radius $r$ moving with velocity $v$ in a viscous fluid of viscosity $\eta$ at low Reynolds number ($\text{Re} = \rho vr/\eta \ll 1$, the Stokes regime), the drag force is

**第 1 步 — 斯托克斯定律。** 对于在粘度为 $\eta$ 的粘性流体中以速度 $v$ 运动的半径为 $r$ 的球，在低雷诺数（$\text{Re} = \rho vr/\eta \ll 1$，斯托克斯区）时，阻力为

$$ F_{\text{drag}} = -6\pi\eta r\, v. $$

This is a result of solving the linearized (creeping-flow) Navier–Stokes equations. The friction coefficient is $\gamma = 6\pi\eta r$.

这是求解线性化（蠕变流）纳维–斯托克斯方程的结果。摩擦系数为 $\gamma = 6\pi\eta r$。

**Step 2 — Identify the mobility.** The mobility is the drift velocity per unit applied force. In steady state (no acceleration), the applied force $F$ equals the drag: $F = \gamma v_{\text{drift}}$, so

**第 2 步 — 确定迁移率。** 迁移率是单位力作用下的漂移速度。在稳态（无加速度）时，施加的力 $F$ 等于阻力：$F = \gamma v_{\text{drift}}$，故

$$ \mu = v_{\text{drift}}/F = 1/\gamma = 1/(6\pi\eta r). $$

**Step 3 — Apply the Einstein relation.**

**第 3 步 — 应用爱因斯坦关系。**

$$ \boxed{\, D = \mu k_B T = k_B T / (6\pi\eta r). \,} \qquad \blacksquare $$

**Step 4 — Extract Avogadro's number.** Writing $k_B = R/N_A$ where $R$ is the molar gas constant:

**第 4 步 — 提取阿伏加德罗常数。** 写 $k_B = R/N_A$，其中 $R$ 为摩尔气体常数：

$$ D = R T / (6\pi\eta r N_A), \quad \text{so} \quad \boxed{\, N_A = RT/(6\pi\eta r D). \,} $$

Perrin (1908) measured $D$ by tracking the mean-square displacement of gamboge particles ($r \approx 0.2\ \mu\text{m}$) in water: $\langle x^2\rangle = 2Dt$ over measured time intervals $t$. Combined with measured $\eta$ and $r$, this gave $N_A \approx 6 \times 10^{23}\ \text{mol}^{-1}$ — the first direct, model-independent determination of Avogadro's number, providing decisive proof of the atomic hypothesis.

佩兰（1908）通过追踪金橘粒子（$r \approx 0.2\ \mu\text{m}$）在水中的均方位移测量了 $D$：在测量的时间间隔 $t$ 内 $\langle x^2\rangle = 2Dt$。结合测量的 $\eta$ 和 $r$，得到 $N_A \approx 6 \times 10^{23}\ \text{mol}^{-1}$——这是阿伏加德罗常数的第一次直接、独立于模型的测定，为原子假说提供了决定性证明。

---

## D. Fluctuation–Dissipation Theorem: The Deep Connection · 涨落–耗散定理：深层联系

**Claim.** The Einstein relation $D = \mu k_B T$ is a special case of the fluctuation–dissipation theorem (FDT): in thermal equilibrium, the spectrum of spontaneous fluctuations of a quantity $X$ is related to the dissipative part of the response to a perturbation conjugate to $X$, with $k_B T$ as the proportionality factor.

**命题。** 爱因斯坦关系 $D = \mu k_B T$ 是涨落–耗散定理（FDT）的特例：在热平衡中，量 $X$ 的自发涨落谱与对共轭于 $X$ 的扰动的耗散响应相关，比例因子为 $k_B T$。

**Step 1 — The Langevin equation.** The microscopic description of a Brownian particle is the Langevin equation:

**第 1 步 — 朗之万方程。** 布朗粒子的微观描述是朗之万方程：

$$ m\, dv/dt = -\gamma v + \xi(t), $$

where $\gamma = 1/\mu = 6\pi\eta r$ is the friction coefficient and $\xi(t)$ is a random (stochastic) force representing the fluctuating collisions of the fluid molecules.

其中 $\gamma = 1/\mu = 6\pi\eta r$ 是摩擦系数，$\xi(t)$ 是代表流体分子随机碰撞的随机（随机过程）力。

**Step 2 — Properties of the random force.** The random force $\xi(t)$ has zero mean and is uncorrelated in time (white noise):

**第 2 步 — 随机力的性质。** 随机力 $\xi(t)$ 均值为零，且时间上不相关（白噪声）：

$$ \langle \xi(t)\rangle = 0, \qquad \langle \xi(t)\xi(t')\rangle = 2\gamma k_B T\, \delta(t - t'). $$

The amplitude of the noise $2\gamma k_B T$ is not arbitrary — it is fixed by the requirement that the particle's velocity distribution is the Maxwell–Boltzmann distribution at temperature $T$, i.e., $\tfrac12 m\langle v^2\rangle = \tfrac12 k_B T$.

噪声幅度 $2\gamma k_B T$ 不是任意的——它由粒子速度分布是温度 $T$ 时麦克斯韦–玻尔兹曼分布的要求固定，即 $\tfrac12 m\langle v^2\rangle = \tfrac12 k_B T$。

**Step 3 — Derive $D$ from the velocity autocorrelation.** In the overdamped limit ($m \to 0$, applicable for colloidal particles where inertia is negligible), the velocity is $v(t) = \xi(t)/\gamma$, and the mean-square displacement is

**第 3 步 — 从速度自相关推导 $D$。** 在过阻尼极限（$m \to 0$，适用于惯性可忽略的胶体粒子）中，速度为 $v(t) = \xi(t)/\gamma$，均方位移为

$$ \begin{aligned} \langle x^2(t)\rangle &= \int_0^t \int_0^t \langle v(t')v(t'')\rangle\, dt'\, dt'' = \int_0^t \int_0^t (1/\gamma^2)\langle \xi(t')\xi(t'')\rangle\, dt'\, dt'' \\ &= (1/\gamma^2) \int_0^t \int_0^t 2\gamma k_B T\, \delta(t' - t'')\, dt'\, dt'' = (2k_B T/\gamma)\, t. \end{aligned} $$

Comparing with $\langle x^2\rangle = 2Dt$:

与 $\langle x^2\rangle = 2Dt$ 比较：

$$ \boxed{\, D = k_B T/\gamma = \mu k_B T. \,} \qquad \blacksquare $$

This derivation shows that $D$ arises directly from the noise amplitude $2\gamma k_B T$ — the fluctuation — while $\mu = 1/\gamma$ characterizes the dissipation. The product $D = \mu k_B T$ is the FDT: fluctuation and dissipation are inextricably linked because they both arise from the same thermal environment.

该推导表明 $D$ 直接来源于噪声幅度 $2\gamma k_B T$——即涨落——而 $\mu = 1/\gamma$ 刻画耗散。乘积 $D = \mu k_B T$ 就是 FDT：涨落和耗散不可分割地联系在一起，因为它们都源于同一热环境。

**Step 4 — Kubo formula: general statement of the FDT.** The general form of the FDT (Kubo, 1966) states that the complex admittance (generalized susceptibility) $\chi(\omega)$ of any linear dissipative system is related to the power spectral density $S_{xx}(\omega)$ of the equilibrium fluctuations of the conjugate variable $x$ by

**第 4 步 — 久保公式：FDT 的一般表述。** FDT 的一般形式（久保，1966）指出，任何线性耗散系统的复导纳（广义磁化率）$\chi(\omega)$ 与共轭变量 $x$ 的平衡涨落功率谱密度 $S_{xx}(\omega)$ 的关系为

$$ S_{xx}(\omega) = 2k_B T\, \text{Im}[\chi(\omega)] / \omega \quad (\text{classical limit, } \hbar\omega \ll k_B T). $$

Special cases of this single relation include: (i) Einstein's $D = \mu k_B T$; (ii) Johnson–Nyquist noise in a resistor $R$: voltage noise spectral density $S_V = 4k_B TR$; (iii) the fluctuating Lorentz force on charges in a magnetic field. The underlying physics is always the same: the equilibrium thermal bath that randomizes particle trajectories (fluctuation) is the same bath that provides the frictional damping (dissipation). $\blacksquare$

该单一关系的特例包括：(i) 爱因斯坦的 $D = \mu k_B T$；(ii) 电阻 $R$ 中的约翰逊–奈奎斯特噪声：电压噪声谱密度 $S_V = 4k_B TR$；(iii) 磁场中电荷所受的涨落洛伦兹力。底层物理始终相同：使粒子轨迹随机化的平衡热浴（涨落）与提供摩擦阻尼的热浴（耗散）是同一个热浴。$\blacksquare$

---

*The Einstein relation and the Langevin equation opened the door to the modern theory of stochastic processes. The fluctuation–dissipation theorem in its Kubo form connects thermal noise to linear response theory, which underlies optical absorption (imaginary part of dielectric function), the Drude conductivity (Module 2.7), and the Kramers–Kronig relations. Together these ideas form the statistical mechanics of non-equilibrium phenomena.*

*爱因斯坦关系和朗之万方程打开了现代随机过程理论的大门。久保形式的涨落–耗散定理将热噪声与线性响应理论联系起来，后者是光学吸收（介电函数的虚部）、德鲁德电导率（模块 2.7）和克拉默斯–克朗尼希关系的基础。这些思想共同构成了非平衡现象的统计力学。*

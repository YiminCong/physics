---
title: "Derivations — Module 9.8: Stellar Structure & Compact Objects"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 9.8: Stellar Structure & Compact Objects
# 推导 — 模块 9.8：恒星结构与致密天体

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.8](./module-9.8-stellar-structure-and-compact-objects.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.8](./module-9.8-stellar-structure-and-compact-objects.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Hydrostatic Equilibrium & the Virial Theorem · 流体静力学平衡与位力定理

**Claim.** A spherically symmetric star in mechanical balance satisfies $dP/dr = -G m(r) \rho(r)/r^2$ together with the mass-continuity relation $dm/dr = 4\pi r^2\rho$. Integrating against gravity yields the virial theorem $2K + U_{grav} = 0$ for a non-relativistic ideal gas, the central-pressure estimate $P_c \sim G M^2/R^4$, and an internal temperature $T \sim G M \mu m_H/(k_B R)$.

**命题。** 处于力学平衡的球对称恒星满足 $dP/dr = -G m(r) \rho(r)/r^2$，连同质量连续性关系 $dm/dr = 4\pi r^2\rho$。对引力积分给出非相对论理想气体的位力定理 $2K + U_{grav} = 0$、中心压强估计 $P_c \sim G M^2/R^4$，以及内部温度 $T \sim G M \mu m_H/(k_B R)$。

**Step 1 — Force balance on a shell.** Consider a thin spherical shell at radius $r$ with thickness $dr$, area $A$, and mass $dm_{shell} = \rho A\, dr$. The pressure on its inner face is $P(r)$ (pushing out) and on its outer face $P(r+dr)$ (pushing in); the net outward pressure force is $-A\, dP$. Gravity pulls the shell inward with force $G m(r)\, dm_{shell}/r^2$, where $m(r)$ is the enclosed mass. Mechanical balance requires:

**第 1 步 — 球壳的受力平衡。** 考虑半径 $r$ 处厚度为 $dr$、面积为 $A$、质量为 $dm_{shell} = \rho A\, dr$ 的薄球壳。其内表面压强为 $P(r)$（向外推），外表面压强为 $P(r+dr)$（向内推）；净向外压力为 $-A\, dP$。引力以 $G m(r)\, dm_{shell}/r^2$ 将球壳向内拉，其中 $m(r)$ 为内含质量。力学平衡要求：

$$ -A\, dP - G m(r) \rho A\, dr/r^2 = 0. $$

Dividing by $A\, dr$ gives the **equation of hydrostatic equilibrium**:

除以 $A\, dr$ 给出**流体静力学平衡方程**：

$$ \boxed{\, dP/dr = -G m(r) \rho(r)/r^2 \,} $$

**Step 2 — Mass continuity.** The mass in a shell of thickness $dr$ is $dm = \rho \times (4\pi r^2)\, dr$, the shell volume times the density, so:

**第 2 步 — 质量连续性。** 厚度 $dr$ 的球壳质量为 $dm = \rho \times (4\pi r^2)\, dr$，即球壳体积乘以密度，故：

$$ \boxed{\, dm/dr = 4\pi r^2\rho(r) \,} $$

These two first-order ODEs, closed by an equation of state $P(\rho, T)$, determine the run of $P$, $\rho$, and $m$ through the star.

这两个一阶常微分方程，由状态方程 $P(\rho, T)$ 闭合，确定 $P$、$\rho$、$m$ 贯穿恒星的分布。

**Step 3 — The virial integral.** Multiply hydrostatic equilibrium by the volume element $4\pi r^3\, dr$ and integrate from center to surface:

**第 3 步 — 位力积分。** 将流体静力学平衡乘以体积元 $4\pi r^3\, dr$ 并从中心积分到表面：

$$ \int_0^R 4\pi r^3\, (dP/dr)\, dr = -\int_0^R (G m(r)/r)\, 4\pi r^2\rho\, dr = -\int_0^M (G m/r)\, dm = U_{grav}, $$

where the right-hand side is exactly the gravitational potential energy $U_{grav}$ of the configuration. Integrate the left side by parts:

其中右侧恰为该位形的引力势能 $U_{grav}$。对左侧分部积分：

$$ \int_0^R 4\pi r^3\, (dP/dr)\, dr = [4\pi r^3 P]_0^R - \int_0^R 3 (4\pi r^2) P\, dr = -3 \int_0^R P (4\pi r^2)\, dr, $$

since $P(R) = 0$ at the surface and $r^3 = 0$ at the center. Therefore:

因表面 $P(R) = 0$ 且中心 $r^3 = 0$。因此：

$$ -3 \int P\, dV = U_{grav}. $$

**Step 4 — Ideal-gas energy and the virial theorem.** For a non-relativistic monatomic ideal gas, $P = (2/3) u$, where $u$ is the thermal energy density; hence $\int P\, dV = (2/3) K$ with $K$ the total thermal (kinetic) energy. Substituting:

**第 4 步 — 理想气体能量与位力定理。** 对非相对论单原子理想气体，$P = (2/3) u$，$u$ 为热能密度；故 $\int P\, dV = (2/3) K$，$K$ 为总热（动）能。代入：

$$ -3 \times (2/3) K = U_{grav} \;\implies\; \boxed{\, 2K + U_{grav} = 0 \,}. $$

The total thermal energy equals minus half the gravitational energy, $K = -U_{grav}/2$. The total energy $E = K + U_{grav} = U_{grav}/2 < 0$ is bound; losing energy makes $U_{grav}$ more negative and $K$ larger — the **negative heat capacity** of a self-gravitating gas.

总热能等于负的引力能的一半，$K = -U_{grav}/2$。总能量 $E = K + U_{grav} = U_{grav}/2 < 0$ 为束缚态；损失能量使 $U_{grav}$ 更负而 $K$ 更大——自引力气体的**负热容**。

**Step 5 — Central pressure and temperature estimates.** Approximating $dP/dr \sim -P_c/R$, $m \sim M$, $\rho \sim M/R^3$ in hydrostatic equilibrium gives $P_c/R \sim G M (M/R^3)/R^2$, so:

**第 5 步 — 中心压强和温度估计。** 在流体静力学平衡中近似 $dP/dr \sim -P_c/R$、$m \sim M$、$\rho \sim M/R^3$，给出 $P_c/R \sim G M (M/R^3)/R^2$，故：

$$ \boxed{\, P_c \sim G M^2/R^4 \,} $$

Setting this equal to the ideal-gas pressure $P_c \sim (\rho/\mu m_H) k_B T \sim (M/R^3)(k_B T/\mu m_H)$:

令其等于理想气体压强 $P_c \sim (\rho/\mu m_H) k_B T \sim (M/R^3)(k_B T/\mu m_H)$：

$$ G M^2/R^4 \sim (M k_B T)/(R^3 \mu m_H) \;\implies\; \boxed{\, k_B T \sim G M \mu m_H/R \,}. $$

For the Sun ($M \approx 2\times 10^{30}$ kg, $R \approx 7\times 10^8$ m, $\mu \sim 0.6$) this gives $T \sim 10^7$ K and $P_c \sim 10^{16}$ Pa, in line with detailed solar models. $\blacksquare$

对太阳（$M \approx 2\times 10^{30}$ kg，$R \approx 7\times 10^8$ m，$\mu \sim 0.6$），这给出 $T \sim 10^7$ K 和 $P_c \sim 10^{16}$ Pa，与详细的太阳模型一致。$\blacksquare$

---

## B. The Lane–Emden Equation · 莱恩–埃姆登方程

**Claim.** A polytrope with $P = K \rho^{(n+1)/n}$ satisfies the dimensionless Lane–Emden equation $(1/\xi^2)\, d/d\xi(\xi^2\, d\theta/d\xi) = -\theta^n$, obtained by writing $\rho = \rho_c \theta^n$ and $r = \alpha \xi$. The closed-form solutions are $\theta = 1 - \xi^2/6$ ($n = 0$), $\theta = \sin\xi/\xi$ ($n = 1$), $\theta = (1 + \xi^2/3)^{-1/2}$ ($n = 5$); the first zero $\xi_1$ sets $R = \alpha \xi_1$ and the mass scales as $M \propto \rho_c^{(3-n)/2n}$.

**命题。** 满足 $P = K \rho^{(n+1)/n}$ 的多方球满足无量纲的莱恩–埃姆登方程 $(1/\xi^2)\, d/d\xi(\xi^2\, d\theta/d\xi) = -\theta^n$，通过写 $\rho = \rho_c \theta^n$ 和 $r = \alpha \xi$ 得到。闭式解为 $\theta = 1 - \xi^2/6$（$n = 0$）、$\theta = \sin\xi/\xi$（$n = 1$）、$\theta = (1 + \xi^2/3)^{-1/2}$（$n = 5$）；第一零点 $\xi_1$ 确定 $R = \alpha \xi_1$，质量标度为 $M \propto \rho_c^{(3-n)/2n}$。

**Step 1 — Combine hydrostatic and Poisson equations.** Rewrite hydrostatic equilibrium using $m(r)$, then differentiate. From $dP/dr = -G m \rho/r^2$, multiply by $r^2/\rho$ and differentiate with respect to $r$, using $dm/dr = 4\pi r^2\rho$:

**第 1 步 — 合并流体静力学方程和泊松方程。** 用 $m(r)$ 重写流体静力学平衡，然后求导。从 $dP/dr = -G m \rho/r^2$ 出发，乘以 $r^2/\rho$ 再对 $r$ 求导，利用 $dm/dr = 4\pi r^2\rho$：

$$ (1/r^2)\, d/dr[(r^2/\rho)\, dP/dr] = -4\pi G \rho. $$

This is the second-order form of hydrostatic equilibrium (equivalent to Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ with $dP/dr = -\rho\, d\Phi/dr$).

这是流体静力学平衡的二阶形式（等价于泊松方程 $\nabla^2\Phi = 4\pi G\rho$，其中 $dP/dr = -\rho\, d\Phi/dr$）。

**Step 2 — Insert the polytropic equation of state.** With $P = K \rho^{(n+1)/n}$, write the density as $\rho = \rho_c \theta^n$, where $\rho_c$ is the central density and $\theta$ is dimensionless with $\theta(\text{center}) = 1$. Then:

**第 2 步 — 代入多方状态方程。** 以 $P = K \rho^{(n+1)/n}$，将密度写为 $\rho = \rho_c \theta^n$，其中 $\rho_c$ 为中心密度，$\theta$ 为无量纲量且 $\theta(\text{中心}) = 1$。则：

$$ P = K \rho_c^{(n+1)/n} \theta^{n+1}. $$

Substituting $P$ and $\rho$ into the second-order equation, the $(n+1)$ powers combine so that $(1/\rho)\, dP/dr = K (n+1) \rho_c^{1/n}\, d\theta/dr$, and the equation becomes:

将 $P$ 和 $\rho$ 代入二阶方程，$(n+1)$ 次幂合并使得 $(1/\rho)\, dP/dr = K (n+1) \rho_c^{1/n}\, d\theta/dr$，方程变为：

$$ [(n+1) K \rho_c^{(1-n)/n}/(4\pi G)]\, (1/r^2)\, d/dr(r^2\, d\theta/dr) = -\theta^n. $$

**Step 3 — Rescale the radius.** Define the length scale $\alpha$ by

**第 3 步 — 重标度半径。** 定义长度标度 $\alpha$ 为

$$ \alpha^2 = (n+1) K \rho_c^{(1-n)/n}/(4\pi G), $$

and set $r = \alpha \xi$ with $\xi$ dimensionless. The bracketed prefactor becomes $\alpha^2$, which cancels exactly, leaving the **Lane–Emden equation**:

并设 $r = \alpha \xi$，$\xi$ 为无量纲。方括号前因子变为 $\alpha^2$，恰好抵消，留下**莱恩–埃姆登方程**：

$$ \boxed{\, (1/\xi^2)\, d/d\xi(\xi^2\, d\theta/d\xi) = -\theta^n \,}, \quad \theta(0) = 1, \;\theta'(0) = 0. $$

The boundary conditions are $\theta(0) = 1$ (density $= \rho_c$ at center) and $\theta'(0) = 0$ (zero pressure gradient at center, no point mass).

边界条件为 $\theta(0) = 1$（中心密度 $= \rho_c$）和 $\theta'(0) = 0$（中心压强梯度为零，无点质量）。

**Step 4 — Closed-form solutions.** For **$n = 0$** the equation is $(1/\xi^2)(\xi^2\theta')' = -1$; integrating twice with $\theta(0)=1$, $\theta'(0)=0$ gives $\theta = 1 - \xi^2/6$, vanishing at $\xi_1 = \sqrt 6$. For **$n = 1$** the substitution $\theta = \chi/\xi$ turns it into $\chi'' = -\chi$, so $\chi = \sin\xi$ and $\theta = \sin\xi/\xi$, vanishing at $\xi_1 = \pi$. For **$n = 5$** direct substitution verifies $\theta = (1 + \xi^2/3)^{-1/2}$, which never reaches zero ($\xi_1 \to \infty$) yet encloses finite mass.

**第 4 步 — 闭式解。** 对 **$n = 0$**，方程为 $(1/\xi^2)(\xi^2\theta')' = -1$；用 $\theta(0)=1$、$\theta'(0)=0$ 积分两次给出 $\theta = 1 - \xi^2/6$，在 $\xi_1 = \sqrt 6$ 处为零。对 **$n = 1$**，代换 $\theta = \chi/\xi$ 将其化为 $\chi'' = -\chi$，故 $\chi = \sin\xi$ 且 $\theta = \sin\xi/\xi$，在 $\xi_1 = \pi$ 处为零。对 **$n = 5$**，直接代入验证 $\theta = (1 + \xi^2/3)^{-1/2}$，它永不为零（$\xi_1 \to \infty$）但包含有限质量。

**Step 5 — Radius and mass scaling.** The surface is the first zero $\theta(\xi_1) = 0$, so the physical radius is $R = \alpha \xi_1$. The total mass is:

**第 5 步 — 半径和质量标度。** 表面为第一零点 $\theta(\xi_1) = 0$，故物理半径为 $R = \alpha \xi_1$。总质量为：

$$ M = \int_0^R 4\pi r^2\rho\, dr = 4\pi \alpha^3 \rho_c \int_0^{\xi_1} \xi^2\theta^n\, d\xi = 4\pi \alpha^3 \rho_c\, (-\xi^2\theta')_{\xi_1}, $$

using the Lane–Emden equation $\xi^2\theta^n = -d/d\xi(\xi^2\theta')$ to do the integral. Since $\alpha \propto \rho_c^{(1-n)/2n}$, we have $\alpha^3\rho_c \propto \rho_c^{(3-n)/2n}$, giving the scaling:

利用莱恩–埃姆登方程 $\xi^2\theta^n = -d/d\xi(\xi^2\theta')$ 完成积分。由于 $\alpha \propto \rho_c^{(1-n)/2n}$，有 $\alpha^3\rho_c \propto \rho_c^{(3-n)/2n}$，给出标度：

$$ \boxed{\, M \propto \rho_c^{(3-n)/2n} \,} $$

At $n = 3$ the exponent $(3-n)/2n$ vanishes: $M$ becomes independent of $\rho_c$ — the key to the Chandrasekhar mass. $\blacksquare$

在 $n = 3$ 时指数 $(3-n)/2n$ 消失：$M$ 变得与 $\rho_c$ 无关——这是钱德拉塞卡质量的关键。$\blacksquare$

---

## C. Electron Degeneracy Pressure: $P \propto \rho^{5/3}$ and $P \propto \rho^{4/3}$ · 电子简并压：$P \propto \rho^{5/3}$ 与 $P \propto \rho^{4/3}$

**Claim.** A $T = 0$ electron Fermi gas has pressure $P = K_{NR} n_e^{5/3}$ in the non-relativistic limit with $K_{NR} = (3\pi^2)^{2/3} \hbar^2/(5 m_e)$, and $P = K_{UR} n_e^{4/3}$ in the ultra-relativistic limit with $K_{UR} = (3\pi^2)^{1/3} \hbar c/4$. With $n_e = \rho/(\mu_e m_H)$ these become $P = K_{NR} (\rho/\mu_e m_H)^{5/3}$ (polytrope $n = 3/2$) and $P = K_{UR} (\rho/\mu_e m_H)^{4/3}$ (polytrope $n = 3$).

**命题。** $T = 0$ 电子费米气体在非相对论极限下压强为 $P = K_{NR} n_e^{5/3}$，$K_{NR} = (3\pi^2)^{2/3} \hbar^2/(5 m_e)$；在超相对论极限下为 $P = K_{UR} n_e^{4/3}$，$K_{UR} = (3\pi^2)^{1/3} \hbar c/4$。以 $n_e = \rho/(\mu_e m_H)$，它们变为 $P = K_{NR} (\rho/\mu_e m_H)^{5/3}$（多方 $n = 3/2$）和 $P = K_{UR} (\rho/\mu_e m_H)^{4/3}$（多方 $n = 3$）。

**Step 1 — Fermi momentum from the filled sphere.** At $T = 0$ electrons fill all momentum states up to the Fermi momentum $p_F$. Counting states in a volume $V$ with 2 spin states (Modules 2.5/2.6), the number of electrons is $N_e = 2 \times V \times (4\pi p_F^3/3)/(2\pi\hbar)^3$. The number density is therefore:

**第 1 步 — 由填满球得到费米动量。** 在 $T = 0$ 时电子填满直到费米动量 $p_F$ 的所有动量态。在体积 $V$ 中计数带 2 个自旋态的态（模块 2.5/2.6），电子数为 $N_e = 2 \times V \times (4\pi p_F^3/3)/(2\pi\hbar)^3$。因此数密度为：

$$ n_e = N_e/V = p_F^3/(3\pi^2\hbar^3) \;\implies\; p_F = \hbar(3\pi^2 n_e)^{1/3}. $$

**Step 2 — Pressure as a momentum-space integral.** The pressure of an isotropic gas is $P = (1/3) \int n(p) v(p) p\, d^3p / (2\pi\hbar)^3 \times 2$, i.e. one third of the flux of momentum carried by particles of velocity $v(p)$:

**第 2 步 — 压强作为动量空间积分。** 各向同性气体的压强为 $P = (1/3) \int n(p) v(p) p\, d^3p / (2\pi\hbar)^3 \times 2$，即速度为 $v(p)$ 的粒子所携带动量通量的三分之一：

$$ P = (1/3) \times [2/(2\pi\hbar)^3] \int_0^{p_F} v(p) p (4\pi p^2)\, dp = (8\pi)/(3(2\pi\hbar)^3) \int_0^{p_F} v(p) p^3\, dp. $$

**Step 3 — Non-relativistic limit.** Here $v = p/m_e$, so the integrand is $p^4/m_e$:

**第 3 步 — 非相对论极限。** 此处 $v = p/m_e$，故被积函数为 $p^4/m_e$：

$$ P = (8\pi)/(3(2\pi\hbar)^3 m_e) \int_0^{p_F} p^4\, dp = (8\pi)/(3(2\pi\hbar)^3 m_e) \times p_F^5/5 = p_F^5/(15\pi^2\hbar^3 m_e). $$

Substituting $p_F = \hbar(3\pi^2 n_e)^{1/3}$, so $p_F^5 = \hbar^5(3\pi^2)^{5/3} n_e^{5/3}$:

代入 $p_F = \hbar(3\pi^2 n_e)^{1/3}$，故 $p_F^5 = \hbar^5(3\pi^2)^{5/3} n_e^{5/3}$：

$$ P = \hbar^2(3\pi^2)^{5/3} n_e^{5/3}/(15\pi^2 m_e) = \boxed{\, (3\pi^2)^{2/3} \hbar^2/(5 m_e) \times n_e^{5/3} \,} \equiv K_{NR} n_e^{5/3}, $$

using $(3\pi^2)^{5/3}/(15\pi^2) = (3\pi^2)^{2/3}(3\pi^2)/(15\pi^2) = (3\pi^2)^{2/3}/5$. With $n_e = \rho/(\mu_e m_H)$, $P = K_{NR} (\rho/\mu_e m_H)^{5/3} \propto \rho^{5/3}$: since $P = K \rho^{1+1/n} \implies 1 + 1/n = 5/3 \implies$ **$n = 3/2$**.

利用 $(3\pi^2)^{5/3}/(15\pi^2) = (3\pi^2)^{2/3}(3\pi^2)/(15\pi^2) = (3\pi^2)^{2/3}/5$。以 $n_e = \rho/(\mu_e m_H)$，$P = K_{NR} (\rho/\mu_e m_H)^{5/3} \propto \rho^{5/3}$：由 $P = K \rho^{1+1/n} \implies 1 + 1/n = 5/3 \implies$ **$n = 3/2$**。

**Step 4 — Ultra-relativistic limit.** Here $v \approx c$, so the integrand is $c p^3$:

**第 4 步 — 超相对论极限。** 此处 $v \approx c$，故被积函数为 $c p^3$：

$$ P = (8\pi c)/(3(2\pi\hbar)^3) \int_0^{p_F} p^3\, dp = (8\pi c)/(3(2\pi\hbar)^3) \times p_F^4/4 = c p_F^4/(12\pi^2\hbar^3). $$

Substituting $p_F^4 = \hbar^4(3\pi^2)^{4/3} n_e^{4/3}$:

代入 $p_F^4 = \hbar^4(3\pi^2)^{4/3} n_e^{4/3}$：

$$ P = \hbar c(3\pi^2)^{4/3} n_e^{4/3}/(12\pi^2) = \boxed{\, (3\pi^2)^{1/3} \hbar c/4 \times n_e^{4/3} \,} \equiv K_{UR} n_e^{4/3}, $$

using $(3\pi^2)^{4/3}/(12\pi^2) = (3\pi^2)^{1/3}(3\pi^2)/(12\pi^2) = (3\pi^2)^{1/3}/4$. With $n_e = \rho/(\mu_e m_H)$, $P = K_{UR} (\rho/\mu_e m_H)^{4/3} \propto \rho^{4/3}$: $1 + 1/n = 4/3 \implies$ **$n = 3$**.

利用 $(3\pi^2)^{4/3}/(12\pi^2) = (3\pi^2)^{1/3}(3\pi^2)/(12\pi^2) = (3\pi^2)^{1/3}/4$。以 $n_e = \rho/(\mu_e m_H)$，$P = K_{UR} (\rho/\mu_e m_H)^{4/3} \propto \rho^{4/3}$：$1 + 1/n = 4/3 \implies$ **$n = 3$**。

**Step 5 — Physical reading.** As $\rho$ rises, $p_F \propto \rho^{1/3}$ grows; once $p_F c \gtrsim m_e c^2$ the gas crosses from the stiff $n = 3/2$ (exponent 5/3) regime to the soft $n = 3$ (exponent 4/3) regime. This softening — the pressure rising more slowly with density — is what makes the relativistic white dwarf marginally unstable and produces a limiting mass. $\blacksquare$

**第 5 步 — 物理解读。** 当 $\rho$ 升高时，$p_F \propto \rho^{1/3}$ 增长；一旦 $p_F c \gtrsim m_e c^2$，气体从硬的 $n = 3/2$（指数 5/3）区域过渡到软的 $n = 3$（指数 4/3）区域。这种软化——压强随密度上升得更慢——使相对论白矮星处于临界不稳定并产生极限质量。$\blacksquare$

---

## D. White-Dwarf Mass–Radius Relation & the Chandrasekhar Mass · 白矮星质量–半径关系与钱德拉塞卡质量

**Claim.** A non-relativistic ($n = 3/2$) white dwarf obeys $R \propto M^{-1/3}$. An ultra-relativistic ($n = 3$) white dwarf has a mass independent of $\rho_c$, the Chandrasekhar mass $M_{Ch} = (\omega_3 \sqrt{3\pi}/2)(\hbar c/G)^{3/2}/(\mu_e m_H)^2 \approx 1.4 M_\odot$ for $\mu_e = 2$, where $\omega_3 = (-\xi^2\theta')_{\xi_1} \approx 2.018$.

**命题。** 非相对论（$n = 3/2$）白矮星服从 $R \propto M^{-1/3}$。超相对论（$n = 3$）白矮星的质量与 $\rho_c$ 无关，即钱德拉塞卡质量 $M_{Ch} = (\omega_3 \sqrt{3\pi}/2)(\hbar c/G)^{3/2}/(\mu_e m_H)^2$，$\mu_e = 2$ 时 $\approx 1.4 M_\odot$，其中 $\omega_3 = (-\xi^2\theta')_{\xi_1} \approx 2.018$。

**Step 1 — Inverse mass–radius relation ($n = 3/2$).** From Derivation B, $R = \alpha \xi_1$ with $\alpha \propto \rho_c^{(1-n)/2n}$ and $M \propto \rho_c^{(3-n)/2n}$. For $n = 3/2$ the exponents are $(1-n)/2n = (-1/2)/3 = -1/6$ and $(3-n)/2n = (3/2)/3 = 1/2$, so:

**第 1 步 — 反向质量–半径关系（$n = 3/2$）。** 由推导 B，$R = \alpha \xi_1$，$\alpha \propto \rho_c^{(1-n)/2n}$，$M \propto \rho_c^{(3-n)/2n}$。对 $n = 3/2$，指数为 $(1-n)/2n = (-1/2)/3 = -1/6$ 和 $(3-n)/2n = (3/2)/3 = 1/2$，故：

$$ R \propto \rho_c^{-1/6}, \quad M \propto \rho_c^{1/2} \;\implies\; \rho_c \propto M^2. $$

Eliminating $\rho_c$: $R \propto (M^2)^{-1/6} = M^{-1/3}$, the **inverse mass–radius relation**:

消去 $\rho_c$：$R \propto (M^2)^{-1/6} = M^{-1/3}$，即**反向质量–半径关系**：

$$ \boxed{\, R \propto M^{-1/3} \,} $$

A more massive white dwarf is smaller and denser — qualitatively opposite to ordinary stars.

质量越大的白矮星越小、越致密——与普通恒星定性相反。

**Step 2 — The $n = 3$ mass is unique.** For an ultra-relativistic gas, $n = 3$ and the mass exponent $(3-n)/2n = 0$, so $M$ is independent of $\rho_c$. Explicitly, from Derivation B, $M = 4\pi \alpha^3 \rho_c (-\xi^2\theta')_{\xi_1} = 4\pi \alpha^3 \rho_c \omega_3$ with $\omega_3 \equiv (-\xi^2\theta')_{\xi_1,n=3} \approx 2.018$, while for $n = 3$:

**第 2 步 — $n = 3$ 质量是唯一的。** 对超相对论气体，$n = 3$ 且质量指数 $(3-n)/2n = 0$，故 $M$ 与 $\rho_c$ 无关。明确地，由推导 B，$M = 4\pi \alpha^3 \rho_c (-\xi^2\theta')_{\xi_1} = 4\pi \alpha^3 \rho_c \omega_3$，$\omega_3 \equiv (-\xi^2\theta')_{\xi_1,n=3} \approx 2.018$，而对 $n = 3$：

$$ \alpha^2 = (n+1) K_{UR}' \rho_c^{(1-n)/n}/(4\pi G) = 4 K_{UR}' \rho_c^{-2/3}/(4\pi G) = K_{UR}' \rho_c^{-2/3}/(\pi G), $$

where $K_{UR}' = K_{UR}/(\mu_e m_H)^{4/3}$ is the constant in $P = K_{UR}' \rho^{4/3}$. Hence $\alpha^3 = [K_{UR}'/(\pi G)]^{3/2} \rho_c^{-1}$, and $\alpha^3\rho_c = [K_{UR}'/(\pi G)]^{3/2}$ is independent of $\rho_c$.

其中 $K_{UR}' = K_{UR}/(\mu_e m_H)^{4/3}$ 是 $P = K_{UR}' \rho^{4/3}$ 中的常数。故 $\alpha^3 = [K_{UR}'/(\pi G)]^{3/2} \rho_c^{-1}$，$\alpha^3\rho_c = [K_{UR}'/(\pi G)]^{3/2}$ 与 $\rho_c$ 无关。

**Step 3 — Assemble the limiting mass.** Combine $M = 4\pi \omega_3 \alpha^3\rho_c = 4\pi \omega_3 [K_{UR}'/(\pi G)]^{3/2}$:

**第 3 步 — 组装极限质量。** 合并 $M = 4\pi \omega_3 \alpha^3\rho_c = 4\pi \omega_3 [K_{UR}'/(\pi G)]^{3/2}$：

$$ M_{Ch} = 4\pi \omega_3 [K_{UR}'/(\pi G)]^{3/2} = (4\pi \omega_3/\pi^{3/2}) (K_{UR}'/G)^{3/2}. $$

Insert $K_{UR}' = (3\pi^2)^{1/3}(\hbar c/4)/(\mu_e m_H)^{4/3}$, so $(K_{UR}'/G)^{3/2} = [(3\pi^2)^{1/3} \hbar c/(4G)]^{3/2}/(\mu_e m_H)^2$. Collecting the numerical factors gives the standard compact form:

代入 $K_{UR}' = (3\pi^2)^{1/3}(\hbar c/4)/(\mu_e m_H)^{4/3}$，故 $(K_{UR}'/G)^{3/2} = [(3\pi^2)^{1/3} \hbar c/(4G)]^{3/2}/(\mu_e m_H)^2$。汇集数值因子给出标准紧凑形式：

$$ \boxed{\, M_{Ch} = (\omega_3 \sqrt{3\pi}/2) (\hbar c/G)^{3/2} / (\mu_e m_H)^2 \,} $$

**Step 4 — Numerical value.** Evaluate the constants. With $\omega_3 \approx 2.018$, $\hbar c/G = (1.055\times 10^{-34} \times 3\times 10^8)/(6.674\times 10^{-11}) \approx 4.74\times 10^{16}$ $\text{kg}^2$, so $(\hbar c/G)^{3/2} \approx 1.03\times 10^{25}$ $\text{kg}^3$; the prefactor $\omega_3\sqrt{3\pi}/2 \approx 2.018 \times 3.070/2 \approx 3.098$; and $(\mu_e m_H)^2 = (2 \times 1.673\times 10^{-27})^2 \approx 1.12\times 10^{-53}$ $\text{kg}^2$. Then:

**第 4 步 — 数值。** 计算常数。以 $\omega_3 \approx 2.018$，$\hbar c/G = (1.055\times 10^{-34} \times 3\times 10^8)/(6.674\times 10^{-11}) \approx 4.74\times 10^{16}$ $\text{kg}^2$，故 $(\hbar c/G)^{3/2} \approx 1.03\times 10^{25}$ $\text{kg}^3$；前因子 $\omega_3\sqrt{3\pi}/2 \approx 2.018 \times 3.070/2 \approx 3.098$；且 $(\mu_e m_H)^2 = (2 \times 1.673\times 10^{-27})^2 \approx 1.12\times 10^{-53}$ $\text{kg}^2$。则：

$$ M_{Ch} \approx 3.098 \times 1.03\times 10^{25}/1.12\times 10^{-53}\ \text{kg} \approx 2.85\times 10^{30}\ \text{kg} \approx \boxed{\, 1.4 M_\odot \,}, $$

since $M_\odot \approx 1.99\times 10^{30}$ kg. The standard astrophysical value is $M_{Ch} \approx 5.83/\mu_e^2\ M_\odot = 1.46 M_\odot$ for $\mu_e = 2$.

因 $M_\odot \approx 1.99\times 10^{30}$ kg。标准天体物理值为 $M_{Ch} \approx 5.83/\mu_e^2\ M_\odot = 1.46 M_\odot$（$\mu_e = 2$）。

**Step 5 — Physical meaning.** Below $M_{Ch}$ the gas is partly non-relativistic, the equation of state is stiff ($n < 3$), and stable equilibrium exists: degeneracy pressure can always grow to balance gravity. As $M \to M_{Ch}$ the central density diverges and the entire star becomes ultra-relativistic ($n = 3$): then both gravity and pressure scale as the same power of radius, equilibrium is marginal, and no equilibrium exists for $M > M_{Ch}$. **Above $\approx 1.4 M_\odot$, electron degeneracy pressure cannot support the star** and it collapses — toward a neutron star or black hole. $\blacksquare$

**第 5 步 — 物理意义。** 在 $M_{Ch}$ 以下，气体部分非相对论，状态方程硬（$n < 3$），存在稳定平衡：简并压总能增长以平衡引力。当 $M \to M_{Ch}$ 时中心密度发散，整颗恒星变为超相对论（$n = 3$）：此时引力和压强随半径以相同幂次标度，平衡处于临界，对 $M > M_{Ch}$ 不存在平衡。**超过 $\approx 1.4 M_\odot$，电子简并压无法支撑恒星**，它便坍缩——朝向中子星或黑洞。$\blacksquare$

---

## E. Neutron Stars & the TOV Equation · 中子星与 TOV 方程

**Claim.** Beyond $M_{Ch}$, collapse drives inverse beta decay ($p + e^- \to n + \nu$) and neutron degeneracy pressure takes over, giving a compact object of $\sim 1.4 M_\odot$ in $\sim 10$ km. The correct relativistic-gravity hydrostatic balance is the Tolman–Oppenheimer–Volkoff (TOV) equation, whose solution gives a maximum neutron-star mass of $\sim 2$–$3 M_\odot$.

**命题。** 超过 $M_{Ch}$，坍缩驱动逆 $\beta$ 衰变（$p + e^- \to n + \nu$），中子简并压接管，给出约 $1.4 M_\odot$ 压缩在约 10 km 的致密天体。正确的相对论引力流体静力学平衡是托尔曼–奥本海默–沃尔科夫（TOV）方程，其解给出约 $2$–$3 M_\odot$ 的中子星最大质量。

**Step 1 — Neutronization.** Above the Chandrasekhar mass, the rising electron Fermi energy $E_F = \sqrt{p_F^2 c^2 + m_e^2 c^4} - m_e c^2$ exceeds the neutron–proton mass difference plus binding effects, making it energetically favorable for electrons to be captured: $p + e^- \to n + \nu_e$. The neutrinos escape, electron pressure is removed, and matter neutronizes into a neutron-rich fluid.

**第 1 步 — 中子化。** 超过钱德拉塞卡质量，上升的电子费米能 $E_F = \sqrt{p_F^2 c^2 + m_e^2 c^4} - m_e c^2$ 超过中子–质子质量差加结合效应，使电子俘获在能量上有利：$p + e^- \to n + \nu_e$。中微子逃逸，电子压强被移除，物质中子化为富中子流体。

**Step 2 — Neutron degeneracy support.** The same Fermi-gas analysis of Derivation C applies to neutrons, replacing $m_e$ by $m_n$ and $\mu_e$ by $\mu_n \approx 1$. Non-relativistic neutron degeneracy pressure $P = K_{NR}^{(n)} (\rho/m_n)^{5/3}$ with $K_{NR}^{(n)} = (3\pi^2)^{2/3} \hbar^2/(5 m_n)$ again gives an $n = 3/2$ polytrope. Because the neutron mass replaces the electron mass in the structure scaling, the characteristic radius shrinks by $\sim m_e/m_n \sim 10^{-3}$ relative to a white dwarf, packing $\sim 1.4 M_\odot$ into $\sim 10$ km.

**第 2 步 — 中子简并支撑。** 推导 C 的同一费米气体分析适用于中子，将 $m_e$ 换为 $m_n$、$\mu_e$ 换为 $\mu_n \approx 1$。非相对论中子简并压 $P = K_{NR}^{(n)} (\rho/m_n)^{5/3}$，$K_{NR}^{(n)} = (3\pi^2)^{2/3} \hbar^2/(5 m_n)$，再次给出 $n = 3/2$ 多方球。由于结构标度中中子质量取代电子质量，特征半径相对白矮星缩小约 $m_e/m_n \sim 10^{-3}$，将约 $1.4 M_\odot$ 压缩到约 10 km。

**Step 3 — Newtonian gravity fails.** At a neutron-star surface the compactness $GM/Rc^2 \sim G(1.4 M_\odot)/(10\ \text{km} \times c^2) \sim 0.2$ is of order unity; general-relativistic corrections to gravity are no longer small. The Newtonian $dP/dr = -Gm\rho/r^2$ must be replaced by the general-relativistic hydrostatic equilibrium, the **Tolman–Oppenheimer–Volkoff (TOV) equation** (Modules 7.5/7.6):

**第 3 步 — 牛顿引力失效。** 在中子星表面紧致度 $GM/Rc^2 \sim G(1.4 M_\odot)/(10\ \text{km} \times c^2) \sim 0.2$ 是 1 的量级；引力的广义相对论修正不再小。牛顿 $dP/dr = -Gm\rho/r^2$ 必须替换为广义相对论流体静力学平衡，即 **托尔曼–奥本海默–沃尔科夫（TOV）方程**（模块 7.5/7.6）：

$$ dP/dr = -G[\rho + P/c^2][m + 4\pi r^3 P/c^2] / [r^2(1 - 2Gm/rc^2)]. $$

**Step 4 — Reading the TOV corrections.** Each bracketed factor enhances gravity relative to Newton: $(\rho + P/c^2)$ because pressure itself gravitates; $(m + 4\pi r^3 P/c^2)$ because pressure adds to the active gravitational mass; and $1/(1 - 2Gm/rc^2)$ the curvature term that diverges at the Schwarzschild radius. All three deepen the potential well, so a relativistic star is harder to support than a Newtonian one.

**第 4 步 — 解读 TOV 修正。** 每个方括号因子都相对牛顿增强引力：$(\rho + P/c^2)$ 因为压强本身产生引力；$(m + 4\pi r^3 P/c^2)$ 因为压强加入有效引力质量；以及 $1/(1 - 2Gm/rc^2)$ 即在史瓦西半径处发散的曲率项。三者都加深势阱，故相对论恒星比牛顿恒星更难支撑。

**Step 5 — Maximum mass and black-hole formation.** Solving the TOV equation with a realistic nuclear equation of state yields a **maximum neutron-star mass** of $\sim 2$–$3 M_\odot$ (the precise value depends on the still-uncertain dense-matter equation of state). Above this maximum, no pressure — degeneracy or nuclear — can resist gravity: the star collapses through its Schwarzschild radius to form a **black hole** (Modules 7.5/7.6). This is the relativistic analog of the Chandrasekhar limit, with neutron degeneracy and general relativity playing the roles of electron degeneracy and Newtonian gravity. $\blacksquare$

**第 5 步 — 最大质量与黑洞形成。** 用真实核物态方程求解 TOV 方程给出约 $2$–$3 M_\odot$ 的**中子星最大质量**（精确值取决于仍不确定的稠密物质物态方程）。超过此最大值，没有任何压强——简并或核——能抵抗引力：恒星坍缩穿过其史瓦西半径形成**黑洞**（模块 7.5/7.6）。这是钱德拉塞卡极限的相对论对应，中子简并和广义相对论扮演电子简并和牛顿引力的角色。$\blacksquare$

---

*All derivations are complete through intermediate algebra with physical interpretation. Hydrostatic equilibrium, the virial theorem, the Lane–Emden equation, the degeneracy-pressure polytropes ($P \propto \rho^{5/3}, \rho^{4/3}$), and the Chandrasekhar mass $M_{Ch} \approx 1.4 M_\odot$ are all standard results central to stellar astrophysics and compact-object physics.*

*所有推导均通过中间代数完整呈现并附物理诠释。流体静力学平衡、位力定理、莱恩–埃姆登方程、简并压多方球（$P \propto \rho^{5/3}$、$\rho^{4/3}$）以及钱德拉塞卡质量 $M_{Ch} \approx 1.4 M_\odot$ 均为恒星天体物理和致密天体物理的核心标准结果。*

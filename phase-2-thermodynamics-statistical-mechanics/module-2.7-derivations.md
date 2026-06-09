---
title: "Derivations — Module 2.7: Kinetic Theory & Transport"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.7: Kinetic Theory & Transport
# 推导 — 模块 2.7：动理论与输运

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.7](./module-2.7-kinetic-theory-and-transport.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.7](./module-2.7-kinetic-theory-and-transport.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Maxwell–Boltzmann Speed Distribution · 麦克斯韦–玻尔兹曼速率分布

**Claim.** For a classical ideal gas in equilibrium at temperature $T$, the distribution of molecular speeds $v = |\mathbf{v}|$ is

**命题。** 对于温度为 $T$ 处于平衡态的经典理想气体，分子速率 $v = |\mathbf{v}|$ 的分布为

$$ f(v) = 4\pi n\, (m/2\pi k_B T)^{3/2}\, v^2\, e^{-mv^2/2k_B T}, $$

where $n = N/V$ is the number density.

其中 $n = N/V$ 为数密度。

**Step 1 — Start from the 3D velocity distribution.** From the Boltzmann distribution, the probability density in velocity space is proportional to $e^{-mv^2/2k_B T}$ (since the kinetic energy is $\tfrac12 mv^2 = \tfrac12 m(v_x^2 + v_y^2 + v_z^2)$). The normalized 3D velocity distribution is

**第 1 步 — 从三维速度分布出发。** 由玻尔兹曼分布，速度空间中的概率密度正比于 $e^{-mv^2/2k_B T}$（因为动能为 $\tfrac12 mv^2 = \tfrac12 m(v_x^2 + v_y^2 + v_z^2)$）。归一化的三维速度分布为

$$ f_{3D}(v_x, v_y, v_z) = (m/2\pi k_B T)^{3/2}\, e^{-m(v_x^2 + v_y^2 + v_z^2)/2k_B T}, $$

normalized so that $\int f_{3D}\, d^3 v = 1$.

归一化使得 $\int f_{3D}\, d^3 v = 1$。

**Step 2 — Convert from velocity components to speed.** The distribution in velocity space is isotropic (depends only on $|\mathbf{v}|$). To find the speed distribution $f(v)$, integrate over the angular part of the spherical shell in velocity space between $v$ and $v + dv$:

**第 2 步 — 从速度分量转化为速率。** 速度空间中的分布是各向同性的（只依赖于 $|\mathbf{v}|$）。为求速率分布 $f(v)$，对速度空间中 $v$ 到 $v + dv$ 之间球壳的角度部分积分：

$$ f(v)\, dv = f_{3D}(v_x, v_y, v_z) \cdot 4\pi v^2\, dv \quad [4\pi v^2\, dv = \text{surface area of shell} \times \text{thickness}] $$

$$ f(v) = 4\pi v^2 \cdot (m/2\pi k_B T)^{3/2}\, e^{-mv^2/2k_B T}. $$

Multiplying by $n$ to get the number density per unit speed interval gives the Maxwell–Boltzmann speed distribution:

乘以 $n$ 得到单位速率区间内的数密度：

$$ \boxed{\, f(v) = 4\pi n\, (m/2\pi k_B T)^{3/2}\, v^2\, e^{-mv^2/2k_B T}. \,} \qquad \blacksquare $$

The $v^2$ factor (proportional to the surface area of the shell in velocity space) is responsible for the distribution being zero at $v = 0$ and having a peak at the most probable speed $v_p = \sqrt{2k_B T/m}$.

$v^2$ 因子（正比于速度空间中球壳的表面积）使得分布在 $v = 0$ 处为零，并在最概然速率 $v_p = \sqrt{2k_B T/m}$ 处有峰值。

**Step 3 — Verify normalization and compute mean quantities.** Using Gaussian integrals $\int_0^\infty v^n e^{-av^2}\, dv$:

**第 3 步 — 验证归一化并计算平均量。** 利用高斯积分 $\int_0^\infty v^n e^{-av^2}\, dv$：

$$ \int_0^\infty f(v)/n\, dv = 4\pi(m/2\pi k_B T)^{3/2} \cdot (\pi^{1/2}/4)(2k_B T/m)^{3/2} = 1 \quad \checkmark $$

$$ \langle v\rangle = \sqrt{8k_B T/\pi m} \quad \text{(mean speed)} $$

$$ \langle v^2\rangle = 3k_B T/m \implies v_{\text{rms}} = \sqrt{3k_B T/m} \quad \text{(root-mean-square speed)} $$

---

## B. Ideal Gas Pressure from Wall Momentum Flux · 从壁面动量通量推导理想气体压强

**Claim.** For $N$ molecules of mass $m$ in a box of volume $V = L^3$ with the Maxwell–Boltzmann distribution, the pressure satisfies $PV = Nk_B T$.

**命题。** 对于体积 $V = L^3$ 的箱中具有麦克斯韦–玻尔兹曼分布的 $N$ 个质量为 $m$ 的分子，压强满足 $PV = Nk_B T$。

**Step 1 — Compute the momentum transfer per collision.** Consider a molecule with velocity component $v_x > 0$ striking the right wall (perpendicular to the $x$-axis). The elastic collision reverses $v_x$, so the momentum transferred to the wall per collision is

**第 1 步 — 计算每次碰撞的动量传递。** 考虑速度 $x$ 分量 $v_x > 0$ 的分子撞击右壁（垂直于 $x$ 轴）。弹性碰撞使 $v_x$ 反向，每次碰撞传给壁面的动量为

$$ \Delta p = 2mv_x. $$

**Step 2 — Count collisions per unit time per unit area.** A molecule with speed $v_x$ travels a distance $v_x\, dt$ in time $dt$. All molecules within distance $v_x\, dt$ from the wall (in a volume $A v_x\, dt$, where $A$ is the wall area) will hit the wall in that time. The number of such molecules with speed component between $v_x$ and $v_x + dv_x$ is

**第 2 步 — 计算单位时间单位面积的碰撞次数。** 速度 $v_x$ 的分子在时间 $dt$ 内行进距离 $v_x\, dt$。在该时间内，所有距壁面距离小于 $v_x\, dt$ 的分子（在体积 $A v_x\, dt$ 中，$A$ 为壁面面积）都会碰壁。速度分量在 $v_x$ 到 $v_x + dv_x$ 之间的此类分子数为

$$ dN_{\text{coll}} = n\, f_{1D}(v_x)\, v_x\, A\, dt\, dv_x \quad (\text{for } v_x > 0), $$

where $n\, f_{1D}(v_x)\, dv_x$ is the number density of molecules with $x$-velocity in $[v_x, v_x + dv_x]$ — with $f_{1D}(v_x) \propto e^{-mv_x^2/2k_B T}$ the 1D Maxwell distribution normalized over all $v_x$ — and only molecules with $v_x > 0$ reach the wall.

其中 $n\, f_{1D}(v_x)\, dv_x$ 是 $x$ 速度在 $[v_x, v_x + dv_x]$ 内的分子数密度——$f_{1D}(v_x) \propto e^{-mv_x^2/2k_B T}$ 为对所有 $v_x$ 归一化的一维麦克斯韦分布——且只有 $v_x > 0$ 的分子到达壁面。

**Step 3 — Integrate to find the pressure.** The pressure is the momentum delivered to the wall per unit area per unit time. Each collision contributes $\Delta p = 2mv_x$, and the collision flux per unit area is $n\, f_{1D}(v_x)\, v_x\, dv_x$, so:

**第 3 步 — 积分求压强。** 压强是单位时间单位面积传给壁面的动量。每次碰撞贡献 $\Delta p = 2mv_x$，单位面积碰撞通量为 $n\, f_{1D}(v_x)\, v_x\, dv_x$，故：

$$ P = \int_0^\infty (2mv_x)(n\, f_{1D}(v_x)\, v_x)\, dv_x = 2mn \int_0^\infty v_x^2\, f_{1D}(v_x)\, dv_x. $$

Since $v_x^2\, f_{1D}$ is even, $\int_0^\infty v_x^2\, f_{1D}\, dv_x = \tfrac12\langle v_x^2\rangle$, and equipartition gives $\langle v_x^2\rangle = k_B T/m$:

由于 $v_x^2\, f_{1D}$ 是偶函数，$\int_0^\infty v_x^2\, f_{1D}\, dv_x = \tfrac12\langle v_x^2\rangle$，而能均分给出 $\langle v_x^2\rangle = k_B T/m$：

$$ P = 2mn \cdot \tfrac12\langle v_x^2\rangle = mn\langle v_x^2\rangle = mn \cdot (k_B T/m) = nk_B T = (N/V)k_B T \implies \boxed{\, PV = Nk_B T. \,} \qquad \blacksquare $$

---

## C. Mean Free Path · 平均自由程

**Claim.** The mean free path of a molecule in a gas of number density $n$ with collision cross-section $\sigma$ is $\ell = 1/(\sqrt{2}\, n\sigma)$.

**命题。** 在数密度为 $n$、碰撞截面为 $\sigma$ 的气体中，分子的平均自由程为 $\ell = 1/(\sqrt{2}\, n\sigma)$。

**Step 1 — Model collisions as hard-sphere scattering.** Two molecules of diameter $d$ collide when their centers come within distance $d$. The collision cross-section is $\sigma = \pi d^2$.

**第 1 步 — 将碰撞建模为硬球散射。** 两个直径为 $d$ 的分子当其中心距离小于 $d$ 时发生碰撞。碰撞截面为 $\sigma = \pi d^2$。

**Step 2 — Compute the collision rate for a single molecule moving through a gas.** A molecule moving with speed $v$ sweeps out a cylinder of cross-sectional area $\sigma$ per unit time. The collision rate (number of collisions per unit time) for a single molecule is

**第 2 步 — 计算单个分子在气体中运动的碰撞率。** 以速度 $v$ 运动的分子每单位时间扫过横截面积为 $\sigma$ 的柱体。单个分子的碰撞率（单位时间碰撞次数）为

$$ \Gamma = n\sigma\, v_{\text{rel}}, $$

where $v_{\text{rel}}$ is the relative speed between the test molecule and the gas molecules it encounters. In a Maxwell–Boltzmann gas, the mean relative speed is

其中 $v_{\text{rel}}$ 是被测分子与它遇到的气体分子之间的相对速率。在麦克斯韦–玻尔兹曼气体中，平均相对速率为

$$ \langle v_{\text{rel}}\rangle = \sqrt{2}\, \langle v\rangle, $$

since for two molecules drawn independently from the same Maxwell–Boltzmann distribution, the mean squared relative velocity is $\langle v_{\text{rel}}^2\rangle = 2\langle v^2\rangle$ (by the independence of velocities), giving $\langle v_{\text{rel}}\rangle \approx \sqrt{2}\, \langle v\rangle$ (the precise result from integrating over the bivariate distribution). Therefore the collision rate is

因为对于从同一麦克斯韦–玻尔兹曼分布独立抽取的两个分子，平均相对速度平方为 $\langle v_{\text{rel}}^2\rangle = 2\langle v^2\rangle$（由速度的独立性），给出 $\langle v_{\text{rel}}\rangle \approx \sqrt{2}\, \langle v\rangle$（对双变量分布积分的精确结果）。因此碰撞率为

$$ \Gamma = n\sigma\, \sqrt{2}\, \langle v\rangle. $$

**Step 3 — Compute the mean free path.** The mean free path is the mean distance traveled between collisions: $\ell = \langle v\rangle/\Gamma$:

**第 3 步 — 计算平均自由程。** 平均自由程是碰撞之间平均行进的距离：$\ell = \langle v\rangle/\Gamma$：

$$ \boxed{\, \ell = \langle v\rangle / (\sqrt{2}\, n\sigma\, \langle v\rangle) = 1/(\sqrt{2}\, n\sigma). \,} \qquad \blacksquare $$

For air at STP ($n \approx 2.7 \times 10^{25}\ \text{m}^{-3}$, $\sigma \approx 4 \times 10^{-19}\ \text{m}^2$), $\ell \approx 65\ \text{nm}$, much larger than molecular size but much smaller than macroscopic lengths — the condition for the fluid mechanics description (Knudsen number $\text{Kn} = \ell/L \ll 1$).

对于标准状态下的空气（$n \approx 2.7 \times 10^{25}\ \text{m}^{-3}$，$\sigma \approx 4 \times 10^{-19}\ \text{m}^2$），$\ell \approx 65\ \text{nm}$，远大于分子尺寸但远小于宏观长度——流体力学描述的条件（努森数 $\text{Kn} = \ell/L \ll 1$）。

---

## D. Drude Conductivity $\sigma = ne^2\tau/m$ from the Relaxation-Time Boltzmann Equation · 从弛豫时间玻尔兹曼方程推导德鲁德电导率 $\sigma = ne^2\tau/m$

**Claim.** For a free electron gas in a uniform electric field $\mathbf{E}$ (along $\hat{x}$) with relaxation time $\tau$, the steady-state electrical conductivity is $\sigma = ne^2\tau/m$ (in SI units, this is the Drude formula).

**命题。** 对于在均匀电场 $\mathbf{E}$（沿 $\hat{x}$ 方向）中弛豫时间为 $\tau$ 的自由电子气，稳态电导率为 $\sigma = ne^2\tau/m$（SI 单位，即德鲁德公式）。

**Step 1 — Write the Boltzmann transport equation.** The distribution function $f(\mathbf{r}, \mathbf{v}, t)$ for electrons evolves according to

**第 1 步 — 写出玻尔兹曼输运方程。** 电子的分布函数 $f(\mathbf{r}, \mathbf{v}, t)$ 按以下方程演化：

$$ \partial f/\partial t + \mathbf{v} \cdot \nabla_r f + (\mathbf{F}/m) \cdot \nabla_v f = (\partial f/\partial t)_{\text{coll}}, $$

where $\mathbf{F} = -e\mathbf{E}$ is the force on an electron (charge $-e$, $e > 0$) due to the electric field.

其中 $\mathbf{F} = -e\mathbf{E}$ 是电场对电子（电荷 $-e$，$e > 0$）的作用力。

**Step 2 — Apply the relaxation-time approximation.** In the relaxation-time approximation, the collision term is

**第 2 步 — 应用弛豫时间近似。** 在弛豫时间近似中，碰撞项为

$$ (\partial f/\partial t)_{\text{coll}} = -(f - f_0)/\tau, $$

where $f_0$ is the equilibrium (Fermi–Dirac or Maxwell–Boltzmann) distribution and $\tau$ is the mean time between collisions (treated as a constant here). This approximation says that collisions drive $f$ back to $f_0$ exponentially with rate $1/\tau$.

其中 $f_0$ 是平衡（费米–狄拉克或麦克斯韦–玻尔兹曼）分布，$\tau$ 是碰撞间的平均时间（此处视为常数）。该近似表明碰撞以速率 $1/\tau$ 指数地将 $f$ 驱回 $f_0$。

**Step 3 — Linearize for a weak field.** Write $f = f_0 + f_1$, where $f_1$ is the small deviation from equilibrium induced by $\mathbf{E}$. In steady state ($\partial f/\partial t = 0$) and a spatially uniform system ($\nabla_r f = 0$), the Boltzmann equation reduces to

**第 3 步 — 对弱场线性化。** 写 $f = f_0 + f_1$，其中 $f_1$ 是由 $\mathbf{E}$ 引起的对平衡态的小偏差。在稳态（$\partial f/\partial t = 0$）和空间均匀系统（$\nabla_r f = 0$）中，玻尔兹曼方程化为

$$ \begin{aligned} (\mathbf{F}/m) \cdot \nabla_v f_0 &= -f_1/\tau \quad (\text{to first order in } \mathbf{E}, \text{ using } \nabla_v f_1 \approx 0) \\ f_1 &= -\tau (\mathbf{F}/m) \cdot \nabla_v f_0 = (e\tau/m)\, \mathbf{E} \cdot \nabla_v f_0. \end{aligned} $$

For a 1D field $\mathbf{E} = E\, \hat{x}$:

对于一维场 $\mathbf{E} = E\, \hat{x}$：

$$ f_1 = (eE\tau/m)\, \partial f_0/\partial v_x. $$

**Step 4 — Compute the current density.** The electrical current density is

**第 4 步 — 计算电流密度。** 电流密度为

$$ j_x = -e \int v_x\, f\, d^3 v = -e \int v_x\, (f_0 + f_1)\, d^3 v = -e \int v_x\, f_1\, d^3 v, $$

where the $f_0$ term vanishes by symmetry ($\int v_x\, f_0\, d^3 v = 0$ since $f_0$ is even in $v_x$).

其中 $f_0$ 项由对称性为零（$\int v_x\, f_0\, d^3 v = 0$，因为 $f_0$ 关于 $v_x$ 是偶函数）。

Substituting $f_1$:

代入 $f_1$：

$$ j_x = -e \int v_x \cdot (eE\tau/m)\, \partial f_0/\partial v_x\, d^3 v = -(e^2 E\tau/m) \int v_x\, (\partial f_0/\partial v_x)\, d^3 v. $$

**Step 5 — Integrate by parts.** Integrate by parts in $v_x$ (boundary terms vanish as $f_0 \to 0$ for $|v_x| \to \infty$):

**第 5 步 — 分部积分。** 对 $v_x$ 进行分部积分（当 $|v_x| \to \infty$ 时 $f_0 \to 0$，边界项为零）：

$$ \int v_x\, \partial f_0/\partial v_x\, dv_x = [v_x f_0]_{-\infty}^{\infty} - \int f_0\, dv_x = -\int f_0\, dv_x. $$

Therefore:

因此：

$$ \int v_x\, \partial f_0/\partial v_x\, d^3 v = -\int f_0\, d^3 v = -n \quad \text{(total number density)}. $$

Substituting back:

代入：

$$ j_x = -(e^2 E\tau/m) \cdot (-n) = (ne^2\tau/m)\, E. $$

**Step 6 — Identify the conductivity.** By Ohm's law $\mathbf{j} = \sigma\mathbf{E}$:

**第 6 步 — 识别电导率。** 由欧姆定律 $\mathbf{j} = \sigma\mathbf{E}$：

$$ \boxed{\, \sigma = ne^2\tau/m. \,} \qquad \blacksquare $$

This is the Drude formula. For copper at room temperature, $n \approx 8.5 \times 10^{28}\ \text{m}^{-3}$, $\sigma \approx 6 \times 10^7\ \Omega^{-1}\text{m}^{-1}$, $m_e = 9.1 \times 10^{-31}\ \text{kg}$, $e = 1.6 \times 10^{-19}\ \text{C}$, giving $\tau \approx 25\ \text{fs}$. The same calculation applies to a quantum (Fermi–Dirac) electron gas, where the Fermi velocity $v_F$ replaces the thermal velocity; the form $\sigma = ne^2\tau/m$ is unchanged.

这就是德鲁德公式。对于室温铜，$n \approx 8.5 \times 10^{28}\ \text{m}^{-3}$，$\sigma \approx 6 \times 10^7\ \Omega^{-1}\text{m}^{-1}$，$m_e = 9.1 \times 10^{-31}\ \text{kg}$，$e = 1.6 \times 10^{-19}\ \text{C}$，给出 $\tau \approx 25\ \text{fs}$。同样的计算适用于量子（费米–狄拉克）电子气，其中费米速度 $v_F$ 替代热速度；$\sigma = ne^2\tau/m$ 的形式不变。

---

*The kinetic-theory results here — Maxwell speed distribution, $PV = Nk_B T$, mean free path, and Drude conductivity — form the microscopic derivations underlying the macroscopic transport equations (Navier–Stokes, Fourier's law, Fick's law, Ohm's law). The Boltzmann equation is the master tool connecting statistical mechanics to non-equilibrium phenomena, and appears again in electron and phonon transport in Phase 4.*

*此处的动理论结果——麦克斯韦速率分布、$PV = Nk_B T$、平均自由程和德鲁德电导率——构成宏观输运方程（纳维–斯托克斯方程、傅里叶定律、菲克定律、欧姆定律）的微观推导基础。玻尔兹曼方程是联系统计力学与非平衡现象的主要工具，并在第 4 阶段的电子和声子输运中再次出现。*

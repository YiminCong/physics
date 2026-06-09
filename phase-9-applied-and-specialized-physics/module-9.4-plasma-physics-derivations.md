---
title: "Derivations — Module 9.4: Plasma Physics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 9.4: Plasma Physics
# 推导 — 模块 9.4：等离子体物理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.4](./module-9.4-plasma-physics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.4](./module-9.4-plasma-physics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Debye Length from Linearized Poisson–Boltzmann · 从线性化泊松–玻尔兹曼方程推导德拜长度

**Claim.** A test charge $Q$ embedded in a plasma of number density $n$ and temperature $T$ is shielded by a screened Coulomb potential $\varphi(r) = (Q/4\pi\varepsilon_0 r)\, e^{-r/\lambda_D}$, where:

$$ \boxed{\, \lambda_D = \sqrt{\varepsilon_0 k_B T / (n e^2)} \,} $$

**命题。** 嵌入密度为 $n$、温度为 $T$ 的等离子体中的测试电荷 $Q$ 被屏蔽库仑势 $\varphi(r) = (Q/4\pi\varepsilon_0 r)\, e^{-r/\lambda_D}$ 所屏蔽，其中：

$$ \boxed{\, \lambda_D = \sqrt{\varepsilon_0 k_B T / (n e^2)} \,} $$

**Step 1 — Boltzmann equilibrium for the electrons.** In the presence of electrostatic potential $\varphi(r)$, the electron density follows the Boltzmann distribution:

**第 1 步 — 电子的玻尔兹曼平衡。** 在静电势 $\varphi(r)$ 存在的情况下，电子密度遵循玻尔兹曼分布：

$$ n_e(r) = n \exp(+e\varphi(r)/k_B T), $$

where the $+e$ exponent reflects electrons being attracted to regions of positive $\varphi$. For singly charged ions with density $n_i$ and temperature $T_i$:

其中 $+e$ 指数反映电子被正 $\varphi$ 区域吸引。对于密度 $n_i$ 和温度 $T_i$ 的单电荷离子：

$$ n_i(r) = n \exp(-e\varphi(r)/k_B T_i). $$

Far from the test charge, $n_e = n_i = n$ (quasineutrality). For simplicity take $T_e = T_i = T$.

远离测试电荷时，$n_e = n_i = n$（准中性）。为简单起见，取 $T_e = T_i = T$。

**Step 2 — Poisson's equation.** The electrostatic potential satisfies:

**第 2 步 — 泊松方程。** 静电势满足：

$$ \nabla^2\varphi = -\rho_{charge}/\varepsilon_0 = -e(n_i - n_e)/\varepsilon_0, $$

where $\rho_{charge} = e n_i - e n_e$ is the net charge density (excluding the test charge).

其中 $\rho_{charge} = e n_i - e n_e$ 为净电荷密度（不包括测试电荷）。

**Step 3 — Linearize in small $\varphi$.** Assume $|e\varphi| \ll k_B T$ (valid far from the test charge). Expand the Boltzmann factors to first order:

**第 3 步 — 对小 $\varphi$ 线性化。** 假设 $|e\varphi| \ll k_B T$（在远离测试电荷处成立）。将玻尔兹曼因子展开到一阶：

$$ n_e \approx n(1 + e\varphi/k_B T), \quad n_i \approx n(1 - e\varphi/k_B T). $$

Substituting into Poisson's equation:

代入泊松方程：

$$ \begin{aligned} \nabla^2\varphi = -e(n_i - n_e)/\varepsilon_0 &= -e[n(1 - e\varphi/k_B T) - n(1 + e\varphi/k_B T)]/\varepsilon_0 \\ &= -e(-2ne\varphi/k_B T)/\varepsilon_0 = 2ne^2\varphi/(\varepsilon_0 k_B T). \end{aligned} $$

(The factor of 2 arises from both electron and ion contributions when $T_e = T_i$.)

（当 $T_e = T_i$ 时，因子 2 来自电子和离子的双重贡献。）

**Step 4 — Solve for the screened potential.** The linearized Poisson–Boltzmann equation in spherical symmetry (away from the point charge at $r = 0$) is:

**第 4 步 — 求解屏蔽势。** 球对称下（远离 $r = 0$ 处的点电荷）线性化的泊松–玻尔兹曼方程为：

$$ (1/r^2)\, d/dr(r^2\, d\varphi/dr) = \varphi/\lambda_D^2, \quad\text{with}\quad \lambda_D^2 = \varepsilon_0 k_B T/(2ne^2). $$

(For the one-species model with only electron screening, the factor 2 becomes 1, giving $\lambda_D^2 = \varepsilon_0 k_B T/(ne^2)$ — the standard single-species formula.) The general solution decaying at infinity is:

（对于仅有电子屏蔽的单组分模型，因子 2 变为 1，给出 $\lambda_D^2 = \varepsilon_0 k_B T/(ne^2)$——标准单组分公式。）在无穷远处衰减的通解为：

$$ \varphi(r) = A e^{-r/\lambda_D}/r + B e^{+r/\lambda_D}/r. $$

The $B$ term diverges as $r \to \infty$, so $B = 0$. The constant $A$ is fixed by the boundary condition that at small $r$ the potential approaches the bare Coulomb potential: $\varphi(r \to 0) \to Q/(4\pi\varepsilon_0 r)$, so $A = Q/(4\pi\varepsilon_0)$.

$B$ 项在 $r \to \infty$ 时发散，故 $B = 0$。常数 $A$ 由边界条件固定：小 $r$ 处势趋近于裸库仑势：$\varphi(r \to 0) \to Q/(4\pi\varepsilon_0 r)$，故 $A = Q/(4\pi\varepsilon_0)$。

**Step 5 — Result.** Therefore:

**第 5 步 — 结果。** 因此：

$$ \boxed{\, \varphi(r) = (Q/4\pi\varepsilon_0)\, e^{-r/\lambda_D}/r \,}, $$

with $\boxed{\, \lambda_D = \sqrt{\varepsilon_0 k_B T / (ne^2)} \,}$ (single-species / electron-only screening).

其中 $\boxed{\, \lambda_D = \sqrt{\varepsilon_0 k_B T / (ne^2)} \,}$（单组分/仅电子屏蔽）。

This is the **Yukawa potential**: the Coulomb potential multiplied by an exponential cutoff at $r = \lambda_D$. The charge is effectively screened beyond the Debye sphere. $\blacksquare$

这是**汤川势**：库仑势乘以在 $r = \lambda_D$ 处的指数截断。电荷在德拜球以外被有效屏蔽。$\blacksquare$

---

## B. Plasma Frequency $\omega_p = \sqrt{ne^2/\varepsilon_0 m_e}$ · 等离子体频率 $\omega_p = \sqrt{ne^2/\varepsilon_0 m_e}$

**Claim.** If a uniform slab of electrons is displaced by a small distance $x$ from the neutralizing ion background, the restoring force leads to simple harmonic oscillation at the **plasma frequency** $\omega_p = \sqrt{ne^2/(\varepsilon_0 m_e)}$.

**命题。** 如果一层均匀电子从中和离子背景中位移小距离 $x$，由此产生的回复力导致以**等离子体频率** $\omega_p = \sqrt{ne^2/(\varepsilon_0 m_e)}$ 进行简谐振荡。

**Step 1 — Set up the model.** Consider a plasma slab of thickness $L$ and electron number density $n$. Imagine displacing the entire electron layer a small distance $x$ in the $+z$ direction, leaving the ion layer (mass $M_i \gg m_e$, essentially stationary) behind. This creates a surface charge density:

**第 1 步 — 建立模型。** 考虑厚度为 $L$、电子数密度为 $n$ 的等离子体平板。设想将整个电子层沿 $+z$ 方向位移小距离 $x$，留下离子层（质量 $M_i \gg m_e$，基本静止）。这产生面电荷密度：

$$ \begin{aligned} \sigma_+ &= +nex \quad\text{on the exposed ion surface}, \\ \sigma_- &= -nex \quad\text{on the leading electron surface}. \end{aligned} $$

These create an electric field between the plates (like a parallel-plate capacitor):

这在板间产生电场（类似平行板电容器）：

$$ E = \sigma/\varepsilon_0 = nex/\varepsilon_0 \quad\text{(directed to pull electrons back, i.e., in } -z \text{ direction)}. $$

**Step 2 — Equation of motion.** Each electron (mass $m_e$, charge $-e$) experiences the restoring force $F = -eE$ (in the $-z$ direction, pointing against the displacement):

**第 2 步 — 运动方程。** 每个电子（质量 $m_e$，电荷 $-e$）受到回复力 $F = -eE$（沿 $-z$ 方向，与位移相反）：

$$ m_e \ddot x = F_z = -e \times E = -e \times (nex/\varepsilon_0) = -(ne^2/\varepsilon_0)\, x. $$

This is a simple harmonic oscillator equation: $\ddot x = -\omega_p^2 x$.

这是简谐振子方程：$\ddot x = -\omega_p^2 x$。

**Step 3 — Read off the frequency.** Comparing with $\ddot x = -\omega^2 x$, we identify:

**第 3 步 — 读取频率。** 与 $\ddot x = -\omega^2 x$ 比较，我们识别出：

$$ \boxed{\, \omega_p^2 = ne^2/(\varepsilon_0 m_e), \quad \omega_p = \sqrt{ne^2/(\varepsilon_0 m_e)} \,} $$

The corresponding frequency is $f_p = \omega_p/(2\pi) = (e/2\pi)\sqrt{n/(\varepsilon_0 m_e)} \approx 9\sqrt n$ Hz (with $n$ in $\text{m}^{-3}$).

对应频率为 $f_p = \omega_p/(2\pi) = (e/2\pi)\sqrt{n/(\varepsilon_0 m_e)} \approx 9\sqrt n$ Hz（$n$ 以 $\text{m}^{-3}$ 为单位）。

**Step 4 — Electromagnetic wave cutoff.** In the plasma, the wave equation for an electromagnetic wave gives the dispersion relation $\omega^2 = \omega_p^2 + c^2 k^2$. For $\omega < \omega_p$, $k^2 = (\omega^2 - \omega_p^2)/c^2 < 0$, so $k$ is imaginary and the wave is **evanescent** (exponentially decaying, not propagating). The wave cannot penetrate a plasma with $n > n_c = \varepsilon_0 m_e \omega^2/e^2$ (the **critical density** for a given $\omega$). This is the physical basis for the ionospheric radio-wave reflection described in the module. $\blacksquare$

**第 4 步 — 电磁波截止。** 在等离子体中，电磁波的波动方程给出色散关系 $\omega^2 = \omega_p^2 + c^2 k^2$。当 $\omega < \omega_p$ 时，$k^2 = (\omega^2 - \omega_p^2)/c^2 < 0$，故 $k$ 为虚数，波是**消逝的**（指数衰减，不传播）。波无法穿透密度 $n > n_c = \varepsilon_0 m_e \omega^2/e^2$（给定 $\omega$ 的**临界密度**）的等离子体。这是模块中描述的电离层无线电波反射的物理基础。$\blacksquare$

---

## C. Physical Origin of Landau Damping · 朗道阻尼的物理起源

**Claim.** A longitudinal electrostatic wave in a collisionless plasma with a Maxwellian velocity distribution is damped at a rate determined by the slope of the distribution function at $v = \omega/k$ (the wave phase velocity). The wave damps if $df/dv|_{v=\omega/k} < 0$ (more slow particles than fast at the resonant velocity). This is **Landau damping** — dissipation without collisions.

**命题。** 具有麦克斯韦速度分布的无碰撞等离子体中的纵向静电波，以由分布函数在 $v = \omega/k$（波相速度）处的斜率决定的速率阻尼。若 $df/dv|_{v=\omega/k} < 0$（共振速度处慢粒子多于快粒子），则波阻尼。这就是**朗道阻尼**——无碰撞的耗散。

**Step 1 — Vlasov equation.** In a collisionless plasma, the single-particle distribution function $f(x, v, t)$ evolves according to the **Vlasov equation**:

**第 1 步 — 弗拉索夫方程。** 在无碰撞等离子体中，单粒子分布函数 $f(x, v, t)$ 按**弗拉索夫方程**演化：

$$ \partial f/\partial t + v\, \partial f/\partial x + (F/m)\, \partial f/\partial v = 0, $$

where $F = -eE$ is the electrostatic force. This is the collisionless Boltzmann equation (Liouville theorem: phase-space density is conserved along particle trajectories).

其中 $F = -eE$ 为静电力。这是无碰撞玻尔兹曼方程（刘维尔定理：相空间密度沿粒子轨迹守恒）。

**Step 2 — Linearize.** Write $f = f_0(v) + f_1(x, v, t)$, where $f_0$ is the unperturbed Maxwellian and $|f_1| \ll f_0$. The electric field $E = E_1$ is first-order. Linearizing the Vlasov equation:

**第 2 步 — 线性化。** 写 $f = f_0(v) + f_1(x, v, t)$，其中 $f_0$ 是未扰动麦克斯韦分布，$|f_1| \ll f_0$。电场 $E = E_1$ 是一阶量。线性化弗拉索夫方程：

$$ \partial f_1/\partial t + v\, \partial f_1/\partial x - (e E_1/m_e)\, \partial f_0/\partial v = 0. $$

**Step 3 — Fourier-Laplace transform.** Write $f_1, E_1 \propto e^{i(kx-\omega t)}$ with complex $\omega$ ($\operatorname{Im}\omega < 0$ for damping). Then:

**第 3 步 — 傅里叶–拉普拉斯变换。** 写 $f_1$、$E_1 \propto e^{i(kx-\omega t)}$，复数 $\omega$（$\operatorname{Im}\omega < 0$ 表示阻尼）。则：

$$ -i\omega f_1 + ikv f_1 = (eE_1/m_e)\, \partial f_0/\partial v \;\implies\; f_1 = (eE_1/m_e)\, (\partial f_0/\partial v) / (kv - \omega). $$

Note the singularity at $v = \omega/k$ — this is the resonance condition: particles moving at the wave phase velocity interact strongly with the wave.

注意在 $v = \omega/k$ 处的奇点——这是共振条件：以波相速度运动的粒子与波强烈相互作用。

**Step 4 — Poisson's equation closes the system.** The perturbed charge density is:

**第 4 步 — 泊松方程封闭系统。** 扰动电荷密度为：

$$ \rho_1 = -e \int f_1\, dv = -(e^2 E_1/m_e) \int (\partial f_0/\partial v)/(kv - \omega)\, dv. $$

Poisson's equation $ik E_1 = \rho_1/\varepsilon_0$ gives the **plasma dispersion relation** $\varepsilon(\omega, k) = 0$:

泊松方程 $ik E_1 = \rho_1/\varepsilon_0$ 给出**等离子体色散关系** $\varepsilon(\omega, k) = 0$：

$$ \varepsilon(\omega, k) = 1 + (e^2/\varepsilon_0 m_e k) \int (\partial f_0/\partial v)/(kv - \omega)\, dv = 0. $$

**Step 5 — Landau's prescription for the resonant integral.** The integral $\int (\partial f_0/\partial v)/(kv - \omega)\, dv$ is singular when the real part of $\omega/k$ lies at a populated value of $v$. Landau (1946) showed the correct treatment (from the initial value problem with causality) is to deform the integration contour below the pole at $v = \omega/k$, giving:

**第 5 步 — 朗道对共振积分的处理。** 当 $\omega/k$ 的实部落在 $v$ 的有效值处时，积分 $\int (\partial f_0/\partial v)/(kv - \omega)\, dv$ 是奇异的。朗道（1946 年）表明，正确的处理（来自具有因果性的初值问题）是将积分围道变形到极点 $v = \omega/k$ 的下方，给出：

$$ \int (\partial f_0/\partial v)/(kv - \omega)\, dv \;\to\; \text{P.V.} \int (\partial f_0/\partial v)/(kv - \omega)\, dv + i\pi\, (\partial f_0/\partial v)|_{v=\omega/k} / k, $$

where P.V. denotes the Cauchy principal value. The imaginary part from the residue at the pole gives the damping rate.

其中 P.V. 表示柯西主值。极点处留数的虚部给出阻尼率。

**Step 6 — Sign of damping.** For a Maxwellian $f_0(v) \propto e^{-v^2/(2v_{th}^2)}$, the derivative is $\partial f_0/\partial v = -v/v_{th}^2 \times f_0 < 0$ for $v > 0$. At the phase velocity $v_{ph} = \omega/k > 0$, $\partial f_0/\partial v|_{v_{ph}} < 0$. The imaginary part of $\varepsilon(\omega, k) = 0$ then gives $\operatorname{Im}\omega < 0$ (damping), because more particles move slightly slower than $v_{ph}$ (gaining energy from the wave) than slightly faster (giving energy back). The net energy flows from the wave to the particles:

**第 6 步 — 阻尼的符号。** 对于麦克斯韦分布 $f_0(v) \propto e^{-v^2/(2v_{th}^2)}$，导数为 $\partial f_0/\partial v = -v/v_{th}^2 \times f_0$，对 $v > 0$ 为负。在相速度 $v_{ph} = \omega/k > 0$ 处，$\partial f_0/\partial v|_{v_{ph}} < 0$。则 $\varepsilon(\omega, k) = 0$ 的虚部给出 $\operatorname{Im}\omega < 0$（阻尼），因为以略低于 $v_{ph}$ 速度运动（从波获得能量）的粒子多于略高于 $v_{ph}$ 速度运动（将能量还给波）的粒子。净能量从波流向粒子：

$$ \boxed{\, \text{Wave damps } (\operatorname{Im}\omega < 0) \iff \partial f_0/\partial v|_{v=\omega/k} < 0. \,} $$

If instead $df/dv > 0$ at $v_{ph}$ (a beam-plasma system where $f$ has a bump at $v_{ph}$), the wave grows (**beam instability**). $\blacksquare$

如果在 $v_{ph}$ 处 $df/dv > 0$（束–等离子体系统，$f$ 在 $v_{ph}$ 处有凸起），则波增长（**束流不稳定性**）。$\blacksquare$

**Physical summary.** Landau damping is a wave–particle resonance effect. The crucial insight is that the velocity distribution is not uniform: for a Maxwellian there are always more particles just below the resonant velocity than just above it. The net transfer of energy from the wave to these particles causes damping — purely through the coherent, collisionless interaction of the wave's electric field with the particle distribution. This phenomenon has no classical fluid analog and is one of the deepest results in kinetic plasma theory.

**物理总结。** 朗道阻尼是一种波–粒子共振效应。关键洞察是速度分布不均匀：对于麦克斯韦分布，共振速度略低处总是比略高处有更多粒子。能量从波到这些粒子的净转移导致阻尼——纯粹通过波的电场与粒子分布的相干无碰撞相互作用。这一现象没有经典流体的类比，是动理论等离子体理论中最深刻的结果之一。

---

*These three derivations span the core mathematical framework of plasma physics: linear screening (Poisson–Boltzmann), collective oscillations (harmonic oscillator from Gauss's law), and kinetic wave–particle resonance (Vlasov–Poisson system). Together they illustrate why plasma physics requires going beyond both fluid mechanics and single-particle dynamics.*

*这三个推导涵盖等离子体物理的核心数学框架：线性屏蔽（泊松–玻尔兹曼）、集体振荡（来自高斯定律的谐振子）和动理论波–粒子共振（弗拉索夫–泊松系统）。它们共同说明了为何等离子体物理需要超越流体力学和单粒子动力学。*

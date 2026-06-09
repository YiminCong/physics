---
title: "Derivations — Module 2.5: Quantum Statistics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.5: Quantum Statistics
# 推导 — 模块 2.5：量子统计

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.5](./module-2.5-quantum-statistics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.5](./module-2.5-quantum-statistics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Fermi–Dirac Distribution from the Grand Canonical Ensemble · 从巨正则系综推导费米–狄拉克分布

**Claim.** For a system of non-interacting fermions in thermal and diffusive contact with a reservoir at temperature $T$ and chemical potential $\mu$, the mean occupation number of a single-particle state with energy $\varepsilon$ is

**命题。** 对于与温度为 $T$、化学势为 $\mu$ 的热库处于热接触和粒子交换接触的非相互作用费米子系统，能量为 $\varepsilon$ 的单粒子态的平均占据数为

$$ n_{\text{FD}}(\varepsilon) = 1 / (e^{(\varepsilon - \mu)/k_B T} + 1). $$

**Step 1 — Identify the relevant ensemble and sub-system.** Since particle number is not fixed, we use the grand canonical ensemble. The key observation for non-interacting particles is that each single-particle state $\alpha$ is an independent sub-system that can be analyzed separately. The state of sub-system $\alpha$ is characterized solely by its occupation number $n_\alpha$.

**第 1 步 — 确定相关系综和子系统。** 由于粒子数不固定，我们使用巨正则系综。对于非相互作用粒子，关键观察是每个单粒子态 $\alpha$ 是一个可独立分析的子系统。子系统 $\alpha$ 的状态完全由其占据数 $n_\alpha$ 刻画。

**Step 2 — Pauli exclusion restricts $n_\alpha$ to 0 or 1.** Fermions obey the Pauli exclusion principle: no two fermions can occupy the same single-particle state. Therefore $n_\alpha \in \{0, 1\}$.

**第 2 步 — 泡利不相容原理将 $n_\alpha$ 限制为 0 或 1。** 费米子服从泡利不相容原理：不能有两个费米子占据同一单粒子态。因此 $n_\alpha \in \{0, 1\}$。

**Step 3 — Write the grand canonical partition function for state $\alpha$.** The grand canonical statistical weight for state $\alpha$ with occupation $n_\alpha$ is $e^{-\beta(\varepsilon_\alpha - \mu)n_\alpha}$, where $\beta = 1/(k_B T)$. Summing over the two allowed values:

**第 3 步 — 写出态 $\alpha$ 的巨正则配分函数。** 占据数为 $n_\alpha$ 的态 $\alpha$ 的巨正则统计权重为 $e^{-\beta(\varepsilon_\alpha - \mu)n_\alpha}$，其中 $\beta = 1/(k_B T)$。对两个允许值求和：

$$ z_\alpha = \sum_{n_\alpha=0}^{1} e^{-\beta(\varepsilon_\alpha - \mu)n_\alpha} = e^0 + e^{-\beta(\varepsilon_\alpha - \mu)} = 1 + e^{-\beta(\varepsilon_\alpha - \mu)}. $$

**Step 4 — Compute the mean occupation number.** Using the grand canonical average:

**第 4 步 — 计算平均占据数。** 使用巨正则平均：

$$ \begin{aligned} \langle n_\alpha\rangle &= \sum_{n=0}^{1} n \cdot e^{-\beta(\varepsilon_\alpha - \mu)n} / z_\alpha \\ &= [0 \cdot 1 + 1 \cdot e^{-\beta(\varepsilon_\alpha - \mu)}] / [1 + e^{-\beta(\varepsilon_\alpha - \mu)}] \\ &= e^{-\beta(\varepsilon_\alpha - \mu)} / [1 + e^{-\beta(\varepsilon_\alpha - \mu)}]. \end{aligned} $$

**Step 5 — Simplify by multiplying numerator and denominator by $e^{\beta(\varepsilon_\alpha - \mu)}$.**

**第 5 步 — 分子分母同乘 $e^{\beta(\varepsilon_\alpha - \mu)}$ 化简。**

$$ \langle n_\alpha\rangle = 1 / [e^{\beta(\varepsilon_\alpha - \mu)} + 1] = \boxed{\, 1 / (e^{(\varepsilon_\alpha - \mu)/k_B T} + 1) = n_{\text{FD}}(\varepsilon_\alpha). \,} \qquad \blacksquare $$

---

## B. Bose–Einstein Distribution from the Grand Canonical Ensemble · 从巨正则系综推导玻色–爱因斯坦分布

**Claim.** For non-interacting bosons, the mean occupation of a single-particle state with energy $\varepsilon$ is

**命题。** 对于非相互作用玻色子，能量为 $\varepsilon$ 的单粒子态的平均占据数为

$$ n_{\text{BE}}(\varepsilon) = 1 / (e^{(\varepsilon - \mu)/k_B T} - 1). $$

**Step 1 — Bosons have no restriction on occupation.** Unlike fermions, any number of bosons can occupy the same state: $n_\alpha \in \{0, 1, 2, 3, \dots\}$.

**第 1 步 — 玻色子对占据数无限制。** 与费米子不同，任意数目的玻色子可以占据同一态：$n_\alpha \in \{0, 1, 2, 3, \dots\}$。

**Step 2 — Write the grand canonical partition function.** Let $x = e^{-\beta(\varepsilon_\alpha - \mu)}$. The partition function is a geometric series:

**第 2 步 — 写出巨正则配分函数。** 令 $x = e^{-\beta(\varepsilon_\alpha - \mu)}$。配分函数是等比级数：

$$ z_\alpha = \sum_{n=0}^{\infty} e^{-\beta(\varepsilon_\alpha - \mu)n} = \sum_{n=0}^{\infty} x^n. $$

For convergence, we need $|x| < 1$, i.e., $e^{-\beta(\varepsilon_\alpha - \mu)} < 1$, i.e., $\varepsilon_\alpha > \mu$. This is why $\mu$ must be less than the ground-state energy for bosons (otherwise the series diverges and the theory breaks down). Summing the geometric series:

为使级数收敛，需要 $|x| < 1$，即 $e^{-\beta(\varepsilon_\alpha - \mu)} < 1$，即 $\varepsilon_\alpha > \mu$。这就是为什么玻色子的化学势必须小于基态能量的原因（否则级数发散，理论失效）。求等比级数之和：

$$ z_\alpha = 1/(1 - x) = 1/(1 - e^{-\beta(\varepsilon_\alpha - \mu)}). $$

**Step 3 — Compute the mean occupation.** Using $\langle n_\alpha\rangle = -(1/\beta)(\partial \ln z_\alpha/\partial\varepsilon_\alpha)$:

**第 3 步 — 计算平均占据数。** 利用 $\langle n_\alpha\rangle = -(1/\beta)(\partial \ln z_\alpha/\partial\varepsilon_\alpha)$：

$$ \begin{aligned} \ln z_\alpha &= -\ln(1 - e^{-\beta(\varepsilon_\alpha - \mu)}), \\ \partial \ln z_\alpha/\partial\varepsilon_\alpha &= -[-\beta e^{-\beta(\varepsilon_\alpha - \mu)}] / (1 - e^{-\beta(\varepsilon_\alpha - \mu)}) \\ &= \beta e^{-\beta(\varepsilon_\alpha - \mu)} / (1 - e^{-\beta(\varepsilon_\alpha - \mu)}). \end{aligned} $$

Therefore:

因此：

$$ \begin{aligned} \langle n_\alpha\rangle &= -(1/\beta) \cdot \beta e^{-\beta(\varepsilon_\alpha - \mu)} / (1 - e^{-\beta(\varepsilon_\alpha - \mu)}) \\ &= e^{-\beta(\varepsilon_\alpha - \mu)} / (1 - e^{-\beta(\varepsilon_\alpha - \mu)}). \end{aligned} $$

**Step 4 — Simplify.** Multiplying numerator and denominator by $e^{\beta(\varepsilon_\alpha - \mu)}$:

**第 4 步 — 化简。** 分子分母同乘 $e^{\beta(\varepsilon_\alpha - \mu)}$：

$$ \langle n_\alpha\rangle = 1 / (e^{\beta(\varepsilon_\alpha - \mu)} - 1) = \boxed{\, 1 / (e^{(\varepsilon_\alpha - \mu)/k_B T} - 1) = n_{\text{BE}}(\varepsilon_\alpha). \,} \qquad \blacksquare $$

**Step 5 — Compare the two distributions.** The Fermi–Dirac and Bose–Einstein distributions differ only in the sign in the denominator: $+1$ for fermions, $-1$ for bosons. Both reduce to the classical Maxwell–Boltzmann distribution $n \propto e^{-\beta(\varepsilon-\mu)}$ when $e^{\beta(\varepsilon-\mu)} \gg 1$, i.e., when $e^{\beta\mu} \ll 1$ (low fugacity, high temperature, or low density).

**第 5 步 — 比较两种分布。** 费米–狄拉克分布和玻色–爱因斯坦分布仅在分母的符号上不同：费米子为 $+1$，玻色子为 $-1$。当 $e^{\beta(\varepsilon-\mu)} \gg 1$ 时，即当 $e^{\beta\mu} \ll 1$（低逸度、高温或低密度），两者均退化为经典麦克斯韦–玻尔兹曼分布 $n \propto e^{-\beta(\varepsilon-\mu)}$。

---

## C. Chemical Potential and the Fermi Energy · 化学势与费米能

**Claim.** For a free electron gas in 3D at $T = 0$, the chemical potential equals the Fermi energy $E_F = (\hbar^2/2m)(3\pi^2 n)^{2/3}$, where $n = N/V$ is the electron number density.

**命题。** 对于三维自由电子气，$T = 0$ 时化学势等于费米能 $E_F = (\hbar^2/2m)(3\pi^2 n)^{2/3}$，其中 $n = N/V$ 为电子数密度。

**Step 1 — At $T = 0$, $n_{\text{FD}}$ is a step function.** The Fermi–Dirac distribution at $T = 0$ is

**第 1 步 — $T = 0$ 时，$n_{\text{FD}}$ 是阶跃函数。** $T = 0$ 时的费米–狄拉克分布为

$$ n_{\text{FD}}(\varepsilon) = 1 \text{ if } \varepsilon < \mu(T=0), \qquad n_{\text{FD}}(\varepsilon) = 0 \text{ if } \varepsilon > \mu(T=0). $$

The chemical potential at $T = 0$ is defined as the Fermi energy: $\mu(T=0) = E_F$.

$T = 0$ 时的化学势定义为费米能：$\mu(T=0) = E_F$。

**Step 2 — Count the states.** For free electrons in a box of volume $V$ with periodic boundary conditions, the allowed wave vectors are $\mathbf{k} = (2\pi/L)(n_x, n_y, n_z)$, giving a density of states in $k$-space of $V/(2\pi)^3$ per unit volume of $k$-space. Including the factor of 2 for electron spin, the total number of states with $|\mathbf{k}| \le k_F$ is

**第 2 步 — 计算状态数。** 对于体积为 $V$ 的箱中具有周期边界条件的自由电子，允许的波矢为 $\mathbf{k} = (2\pi/L)(n_x, n_y, n_z)$，在 $k$ 空间单位体积内的态密度为 $V/(2\pi)^3$。包含电子自旋的因子 2，$|\mathbf{k}| \le k_F$ 的总态数为

$$ N = 2 \cdot V/(2\pi)^3 \cdot (4\pi/3)\, k_F^3 = V k_F^3 / (3\pi^2). $$

**Step 3 — Solve for $k_F$ in terms of $n$.** From $n = N/V$:

**第 3 步 — 用 $n$ 求解 $k_F$。** 由 $n = N/V$：

$$ n = k_F^3/(3\pi^2) \implies k_F = (3\pi^2 n)^{1/3}. $$

**Step 4 — Compute $E_F$.** The Fermi energy is the kinetic energy at the Fermi wavevector:

**第 4 步 — 计算 $E_F$。** 费米能是费米波矢处的动能：

$$ \boxed{\, E_F = \hbar^2 k_F^2/(2m) = (\hbar^2/2m)(3\pi^2 n)^{2/3}. \,} \qquad \blacksquare $$

For copper with $n \approx 8.5 \times 10^{28}\ \text{m}^{-3}$, this gives $E_F \approx 7\ \text{eV}$, so $T_F = E_F/k_B \approx 81\,000\ \text{K}$, confirming that room-temperature electrons are deeply degenerate.

对于铜，$n \approx 8.5 \times 10^{28}\ \text{m}^{-3}$，由此给出 $E_F \approx 7\ \text{eV}$，故 $T_F = E_F/k_B \approx 81\,000\ \text{K}$，证实室温下电子是深度简并的。

---

## D. Classical Limit and the Maxwell–Boltzmann Distribution · 经典极限与麦克斯韦–玻尔兹曼分布

**Claim.** When $e^{\beta(\varepsilon-\mu)} \gg 1$ for all occupied states (high temperature or low density), both quantum distributions reduce to $n(\varepsilon) \approx e^{\beta\mu} e^{-\beta\varepsilon}$, recovering the Maxwell–Boltzmann distribution.

**命题。** 当所有占据态满足 $e^{\beta(\varepsilon-\mu)} \gg 1$（高温或低密度）时，两种量子分布均退化为 $n(\varepsilon) \approx e^{\beta\mu} e^{-\beta\varepsilon}$，回归麦克斯韦–玻尔兹曼分布。

**Step 1 — Taylor expand for large argument.** When $e^{\beta(\varepsilon-\mu)} \equiv y \gg 1$:

**第 1 步 — 对大参数进行泰勒展开。** 当 $e^{\beta(\varepsilon-\mu)} \equiv y \gg 1$ 时：

$$ \begin{aligned} n_{\text{FD}} &= 1/(y + 1) \approx 1/y = e^{-\beta(\varepsilon-\mu)} = e^{\beta\mu} e^{-\beta\varepsilon}, \\ n_{\text{BE}} &= 1/(y - 1) \approx 1/y = e^{-\beta(\varepsilon-\mu)} = e^{\beta\mu} e^{-\beta\varepsilon}. \end{aligned} $$

Both give the same classical result. The chemical potential $\mu$ is then determined by normalization $\sum_\varepsilon n(\varepsilon) = N$, giving $e^{\beta\mu} = N/z$ where $z$ is the single-particle partition function. $\blacksquare$

两者给出相同的经典结果。化学势 $\mu$ 由归一化条件 $\sum_\varepsilon n(\varepsilon) = N$ 确定，给出 $e^{\beta\mu} = N/z$，其中 $z$ 是单粒子配分函数。$\blacksquare$

---

*The grand canonical derivations here — summing over occupation numbers with the geometric series for bosons and the two-state sum for fermions — are reproduced identically in the derivations of the Planck distribution for photons (Module 2.6) and the BCS gap equation for superconductors (Module 5.1). The denominator sign $\pm 1$ carries all the physics of quantum statistics.*

*此处的巨正则推导——对玻色子用等比级数求和、对费米子用二态求和——在光子的普朗克分布（模块 2.6）和超导体的 BCS 能隙方程（模块 5.1）的推导中完全重现。分母的 $\pm 1$ 符号承载了量子统计的全部物理内涵。*

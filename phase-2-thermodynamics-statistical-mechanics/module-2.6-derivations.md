---
title: "Derivations — Module 2.6: Quantum Gases & Applications"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.6: Quantum Gases & Applications
# 推导 — 模块 2.6：量子气体与应用

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.6](./module-2.6-quantum-gases-applications.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.6](./module-2.6-quantum-gases-applications.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Planck Distribution and the Stefan–Boltzmann Law · 普朗克分布与斯特藩–玻尔兹曼定律

**Claim.** The mean energy per mode of frequency $\nu$ in a cavity at temperature $T$ is $\langle E_\nu\rangle = h\nu/(e^{h\nu/k_B T} - 1)$. Summing over all modes gives total radiated power per unit area $P = \sigma T^4$ with $\sigma = 2\pi^5 k_B^4/(15 h^3 c^2)$.

**命题。** 温度为 $T$ 的腔体中频率为 $\nu$ 的每个模式的平均能量为 $\langle E_\nu\rangle = h\nu/(e^{h\nu/k_B T} - 1)$。对所有模式求和给出单位面积总辐射功率 $P = \sigma T^4$，其中 $\sigma = 2\pi^5 k_B^4/(15 h^3 c^2)$。

**Step 1 — Quantize each electromagnetic mode.** Each mode of the electromagnetic field in a cavity behaves as a quantum harmonic oscillator with frequency $\nu$. Its energy levels are $E_n = n\hbar\omega = nh\nu$ (taking the ground-state energy $\tfrac12 h\nu$ as a reference offset that does not contribute to thermal properties). The mode is a boson mode with chemical potential $\mu = 0$ (photons are not conserved: they can be emitted and absorbed freely by the cavity walls).

**第 1 步 — 量子化每个电磁模式。** 腔体中电磁场的每个模式表现为频率为 $\nu$ 的量子谐振子。其能级为 $E_n = n\hbar\omega = nh\nu$（取基态能量 $\tfrac12 h\nu$ 作为不影响热性质的参考零点）。该模式是化学势 $\mu = 0$ 的玻色子模（光子不守恒：可被腔壁自由发射和吸收）。

**Step 2 — Apply the Bose–Einstein distribution with $\mu = 0$.** The mean photon occupation of a mode is

**第 2 步 — 应用 $\mu = 0$ 的玻色–爱因斯坦分布。** 一个模式的平均光子占据数为

$$ \langle n\rangle = 1/(e^{h\nu/k_B T} - 1). $$

The mean energy of the mode is

该模式的平均能量为

$$ \langle E_\nu\rangle = h\nu \cdot \langle n\rangle = \boxed{\, h\nu / (e^{h\nu/k_B T} - 1). \,} \qquad \blacksquare $$

This is Planck's formula for the mean energy per mode. The full Planck distribution is obtained by multiplying by the mode density.

这是每个模式平均能量的普朗克公式。完整普朗克分布通过乘以模式密度得到。

**Step 3 — Count the modes in a cavity.** For a cubic cavity of side $L$ (volume $V = L^3$), the allowed wave vectors satisfy periodic boundary conditions: $\mathbf{k} = (2\pi/L)(n_x, n_y, n_z)$. The number of modes with frequencies between $\nu$ and $\nu + d\nu$ is obtained from the $k$-space shell of thickness $dk$, multiplied by 2 polarizations:

**第 3 步 — 计算腔体中的模式数。** 对于边长为 $L$（体积 $V = L^3$）的立方腔体，允许的波矢满足周期边界条件：$\mathbf{k} = (2\pi/L)(n_x, n_y, n_z)$。频率在 $\nu$ 到 $\nu + d\nu$ 之间的模式数由 $k$ 空间球壳厚度 $dk$ 乘以 2 个偏振态得到：

$$ dN_{\text{modes}} = 2 \cdot [V/(2\pi)^3] \cdot 4\pi k^2\, dk. $$

Using $k = 2\pi\nu/c$ (so $dk = 2\pi\, d\nu/c$):

利用 $k = 2\pi\nu/c$（故 $dk = 2\pi\, d\nu/c$）：

$$ dN_{\text{modes}} = 2 \cdot [V/(2\pi)^3] \cdot 4\pi(2\pi\nu/c)^2 \cdot (2\pi/c)\, d\nu = (8\pi V/c^3)\, \nu^2\, d\nu. $$

The mode density per unit volume per unit frequency is $g(\nu) = 8\pi\nu^2/c^3$.

单位体积单位频率的模式密度为 $g(\nu) = 8\pi\nu^2/c^3$。

**Step 4 — Obtain the spectral energy density.** The energy per unit volume per unit frequency is

**第 4 步 — 得到谱能量密度。** 单位体积单位频率的能量为

$$ u(\nu, T) = g(\nu) \cdot \langle E_\nu\rangle = (8\pi\nu^2/c^3) \cdot h\nu/(e^{h\nu/k_B T} - 1) = \boxed{\, 8\pi h\nu^3/c^3 \cdot 1/(e^{h\nu/k_B T} - 1). \,} \qquad \blacksquare $$

This is the Planck spectral energy density. Note: some texts write the factor $8\pi h/c^3\, \nu^3/(e^{h\nu/kT} - 1)$.

这就是普朗克谱能量密度。

**Step 5 — Derive the Stefan–Boltzmann law.** Integrate $u(\nu, T)$ over all frequencies:

**第 5 步 — 推导斯特藩–玻尔兹曼定律。** 对所有频率积分 $u(\nu, T)$：

$$ u_{\text{total}} = \int_0^\infty (8\pi h/c^3)\, \nu^3/(e^{h\nu/k_B T} - 1)\, d\nu. $$

Substitute $x = h\nu/(k_B T)$, so $\nu = x k_B T/h$ and $d\nu = k_B T/h\, dx$:

令 $x = h\nu/(k_B T)$，则 $\nu = x k_B T/h$，$d\nu = k_B T/h\, dx$：

$$ u_{\text{total}} = (8\pi h/c^3)(k_B T/h)^4 \int_0^\infty x^3/(e^x - 1)\, dx. $$

The integral $\int_0^\infty x^3/(e^x - 1)\, dx = \pi^4/15$ (a standard result from Riemann zeta function: $= 6\zeta(4) = 6\cdot\pi^4/90 = \pi^4/15$). Therefore:

积分 $\int_0^\infty x^3/(e^x - 1)\, dx = \pi^4/15$（黎曼 $\zeta$ 函数的标准结果：$= 6\zeta(4) = 6\cdot\pi^4/90 = \pi^4/15$）。因此：

$$ u_{\text{total}} = (8\pi h/c^3)(k_B T/h)^4 \cdot (\pi^4/15) = (8\pi^5 k_B^4)/(15 h^3 c^3) \cdot T^4. $$

The total radiated power per unit area from a blackbody (using the relation $P = c\cdot u_{\text{total}}/4$):

黑体单位面积总辐射功率（利用 $P = c\cdot u_{\text{total}}/4$）：

$$ \boxed{\, P = \sigma T^4, \quad \sigma = 2\pi^5 k_B^4/(15 h^3 c^2). \,} \qquad \blacksquare $$

The numerical value is $\sigma \approx 5.67 \times 10^{-8}\ \text{W m}^{-2}\,\text{K}^{-4}$, the Stefan–Boltzmann constant.

数值为 $\sigma \approx 5.67 \times 10^{-8}\ \text{W m}^{-2}\,\text{K}^{-4}$，即斯特藩–玻尔兹曼常数。

---

## B. Degenerate Fermi Gas: Electronic Heat Capacity via Sommerfeld Expansion · 简并费米气体：通过索末菲展开推导电子热容

**Claim.** At low temperature $T \ll T_F$, the electronic heat capacity of a 3D free Fermi gas is $C_{\text{el}} = (\pi^2/3)k_B^2\, T\, g(E_F) \propto T$, where $g(E_F)$ is the density of states at the Fermi level.

**命题。** 在低温 $T \ll T_F$ 时，三维自由费米气体的电子热容为 $C_{\text{el}} = (\pi^2/3)k_B^2\, T\, g(E_F) \propto T$，其中 $g(E_F)$ 是费米能级处的态密度。

**Step 1 — Write the total energy as a Fermi–Dirac integral.** The total energy at temperature $T$ is

**第 1 步 — 将总能量写为费米–狄拉克积分。** 温度 $T$ 时的总能量为

$$ U(T) = \int_0^\infty \varepsilon\, g(\varepsilon)\, n_{\text{FD}}(\varepsilon)\, d\varepsilon, $$

where $g(\varepsilon) = (V/2\pi^2)(2m/\hbar^2)^{3/2}\, \varepsilon^{1/2} \propto \varepsilon^{1/2}$ is the 3D free-electron density of states.

其中 $g(\varepsilon) = (V/2\pi^2)(2m/\hbar^2)^{3/2}\, \varepsilon^{1/2} \propto \varepsilon^{1/2}$ 是三维自由电子的态密度。

**Step 2 — Sommerfeld expansion for a Fermi integral.** For any smooth function $h(\varepsilon)$, the Sommerfeld lemma gives (for $T \ll T_F$):

**第 2 步 — 费米积分的索末菲展开。** 对于任意光滑函数 $h(\varepsilon)$，索末菲引理给出（$T \ll T_F$ 时）：

$$ \int_0^\infty h(\varepsilon)\, n_{\text{FD}}(\varepsilon)\, d\varepsilon = \int_0^\mu h(\varepsilon)\, d\varepsilon + (\pi^2/6)(k_B T)^2\, h'(\mu) + O(T^4). $$

The proof uses the Euler–Maclaurin formula after substituting $t = \beta(\varepsilon - \mu)$, with the key integral $\int_{-\infty}^\infty t^2/(e^t + 1)(e^{-t} + 1)\, dt = \pi^2/3$.

证明利用代换 $t = \beta(\varepsilon - \mu)$ 后的欧拉–麦克劳林公式，关键积分为 $\int_{-\infty}^\infty t^2/(e^t + 1)(e^{-t} + 1)\, dt = \pi^2/3$。

**Step 3 — Apply the expansion to $U(T)$.** With $h(\varepsilon) = \varepsilon\, g(\varepsilon)$, so $h'(\varepsilon) = g(\varepsilon) + \varepsilon\, g'(\varepsilon)$, evaluated at $\varepsilon = \mu \approx E_F$ (since $\mu$ deviates from $E_F$ only at order $(k_B T/E_F)^2$, negligible to leading order):

**第 3 步 — 将展开应用于 $U(T)$。** 令 $h(\varepsilon) = \varepsilon\, g(\varepsilon)$，则 $h'(\varepsilon) = g(\varepsilon) + \varepsilon\, g'(\varepsilon)$，在 $\varepsilon = \mu \approx E_F$ 处求值（因为 $\mu$ 偏离 $E_F$ 仅为 $(k_B T/E_F)^2$ 量级，在领头阶可忽略）：

$$ \begin{aligned} U(T) &\approx \int_0^{E_F} \varepsilon\, g(\varepsilon)\, d\varepsilon + (\pi^2/6)(k_B T)^2\, [g(E_F) + E_F\, g'(E_F)] + \dots \\ &= U(0) + (\pi^2/6)(k_B T)^2\, g(E_F) + O(T^4). \end{aligned} $$

(The $E_F\, g'(E_F)$ term is absorbed into the correction to $\mu$ and cancels at this order.)

（$E_F\, g'(E_F)$ 项被吸收进 $\mu$ 的修正中，在此阶相消。）

**Step 4 — Differentiate to get $C_{\text{el}}$.**

**第 4 步 — 微分得 $C_{\text{el}}$。**

$$ C_{\text{el}} = dU/dT = (\pi^2/3)\, k_B^2\, T\, g(E_F) \propto T. \qquad \blacksquare $$

For the 3D free electron gas, $g(E_F) = 3N/(2E_F)$, giving $C_{\text{el}} = (\pi^2/2)(k_B T/E_F)N k_B$ — the standard Sommerfeld result. Compared to the classical value $(3/2)Nk_B$, the electronic heat capacity is suppressed by the factor $(\pi^2/3)(k_B T/E_F) \ll 1$.

对于三维自由电子气，$g(E_F) = 3N/(2E_F)$，给出 $C_{\text{el}} = (\pi^2/2)(k_B T/E_F)N k_B$——标准索末菲结果。与经典值 $(3/2)Nk_B$ 相比，电子热容被因子 $(\pi^2/3)(k_B T/E_F) \ll 1$ 压低。

---

## C. Debye $T^3$ Law for Lattice Heat Capacity · 晶格热容的德拜 $T^3$ 定律

**Claim.** In the Debye model, the lattice heat capacity at $T \ll T_D = \hbar\omega_D/k_B$ is $C_{\text{Debye}} = (12\pi^4/5)Nk_B(T/T_D)^3$.

**命题。** 在德拜模型中，$T \ll T_D = \hbar\omega_D/k_B$ 时晶格热容为 $C_{\text{Debye}} = (12\pi^4/5)Nk_B(T/T_D)^3$。

**Step 1 — Model phonons as bosons with linear dispersion.** The Debye model replaces the actual phonon dispersion with a linear approximation $\omega = v_s k$ for all $3N$ modes, where $v_s$ is the sound speed. The mode density in 3D is (per volume) $g(\omega) = 9N\omega^2/\omega_D^3$ for $\omega \le \omega_D$ and $0$ otherwise. The Debye cutoff $\omega_D$ is set by $\int_0^{\omega_D} g(\omega)\, d\omega = 3N$ (three modes per atom).

**第 1 步 — 将声子建模为具有线性色散的玻色子。** 德拜模型用线性近似 $\omega = v_s k$ 替代所有 $3N$ 个模式的实际声子色散，其中 $v_s$ 为声速。三维模式密度（每体积）为：$\omega \le \omega_D$ 时 $g(\omega) = 9N\omega^2/\omega_D^3$，否则为 0。德拜截止频率 $\omega_D$ 由 $\int_0^{\omega_D} g(\omega)\, d\omega = 3N$ 确定（每个原子三个模式）。

**Step 2 — Write the total phonon energy.** Each mode has mean energy $\hbar\omega/(e^{\beta\hbar\omega} - 1)$ (Planck distribution with $\mu = 0$):

**第 2 步 — 写出总声子能量。** 每个模式的平均能量为 $\hbar\omega/(e^{\beta\hbar\omega} - 1)$（$\mu = 0$ 的普朗克分布）：

$$ U = \int_0^{\omega_D} g(\omega) \cdot \hbar\omega/(e^{\beta\hbar\omega} - 1)\, d\omega = (9N\hbar/\omega_D^3) \int_0^{\omega_D} \omega^3/(e^{\beta\hbar\omega} - 1)\, d\omega. $$

**Step 3 — Change variables and take the low-$T$ limit.** Let $x = \beta\hbar\omega = \hbar\omega/(k_B T)$. Define $x_D = \hbar\omega_D/(k_B T) = T_D/T$. At $T \ll T_D$, $x_D \to \infty$ and the upper limit can be extended to $\infty$:

**第 3 步 — 换元并取低温极限。** 令 $x = \beta\hbar\omega = \hbar\omega/(k_B T)$。定义 $x_D = \hbar\omega_D/(k_B T) = T_D/T$。当 $T \ll T_D$ 时，$x_D \to \infty$，积分上限可延伸至 $\infty$：

$$ U \approx (9N\hbar/\omega_D^3)(k_B T/\hbar)^4 \int_0^\infty x^3/(e^x - 1)\, dx = 9N k_B T (T/T_D)^3 \cdot (\pi^4/15), $$

using the standard integral $\int_0^\infty x^3/(e^x - 1)\, dx = \pi^4/15$.

利用标准积分 $\int_0^\infty x^3/(e^x - 1)\, dx = \pi^4/15$。

$$ U \approx (9\pi^4/15)\, N k_B T (T/T_D)^3 = (3\pi^4/5)\, N k_B T^4/T_D^3. $$

**Step 4 — Differentiate to get $C_{\text{Debye}}$.**

**第 4 步 — 微分得 $C_{\text{Debye}}$。**

$$ C_{\text{Debye}} = dU/dT = (12\pi^4/5)\, N k_B (T/T_D)^3. \qquad \blacksquare $$

This $T^3$ law arises because (i) the linear phonon dispersion gives a mode density $\propto \omega^2$, (ii) at low $T$ only modes with $\hbar\omega \lesssim k_B T$ are thermally excited, so the number of active modes $\propto T^3$, and (iii) each active mode contributes $\sim k_B$ to the heat capacity by equipartition.

$T^3$ 定律的出现是因为：(i) 线性声子色散给出模式密度 $\propto \omega^2$；(ii) 低温时只有满足 $\hbar\omega \lesssim k_B T$ 的模式被热激活，故活跃模式数 $\propto T^3$；(iii) 每个活跃模式通过能均分定理对热容贡献 $\sim k_B$。

---

## D. Bose–Einstein Condensation: Condition and $T_{\text{BEC}}$ · 玻色–爱因斯坦凝聚：条件与 $T_{\text{BEC}}$

**Claim.** For $N$ non-interacting bosons in a 3D box at fixed density $n = N/V$, macroscopic occupation of the ground state (BEC) occurs below

**命题。** 对于三维箱中密度固定为 $n = N/V$ 的 $N$ 个非相互作用玻色子，宏观的基态占据（BEC）发生在以下温度以下：

$$ T_{\text{BEC}} = (2\pi\hbar^2/mk_B)(n/\zeta(3/2))^{2/3}, \qquad \zeta(3/2) \approx 2.612. $$

**Step 1 — The normal-phase saturates at $\mu \to 0$.** Above $T_{\text{BEC}}$, all $N$ particles are distributed among the excited states ($n \ge 1$). The number of bosons in excited states is

**第 1 步 — 正常相在 $\mu \to 0$ 时饱和。** 在 $T_{\text{BEC}}$ 以上，所有 $N$ 个粒子分布在激发态（$n \ge 1$）中。激发态中的玻色子数为

$$ N_{\text{ex}} = \int_0^\infty g(\varepsilon)\, n_{\text{BE}}(\varepsilon)\, d\varepsilon, $$

where $g(\varepsilon) \propto \varepsilon^{1/2}$ is the 3D density of states and $n_{\text{BE}}$ has $\mu \le 0$. As $T$ decreases, $\mu$ increases toward $0$. When $\mu \to 0$, the excited-state population reaches its maximum value:

其中 $g(\varepsilon) \propto \varepsilon^{1/2}$ 是三维态密度，$n_{\text{BE}}$ 有 $\mu \le 0$。随着 $T$ 降低，$\mu$ 增大趋向 $0$。当 $\mu \to 0$ 时，激发态粒子数达到最大值：

$$ N_{\text{ex}}^{\max}(T) = \int_0^\infty g(\varepsilon)/(e^{\beta\varepsilon} - 1)\, d\varepsilon. $$

**Step 2 — Evaluate the integral.** Using $g(\varepsilon) = (V/4\pi^2)(2m/\hbar^2)^{3/2}\, \varepsilon^{1/2}$ and $x = \beta\varepsilon$:

**第 2 步 — 求积分值。** 利用 $g(\varepsilon) = (V/4\pi^2)(2m/\hbar^2)^{3/2}\, \varepsilon^{1/2}$ 和 $x = \beta\varepsilon$：

$$ N_{\text{ex}}^{\max} = (V/4\pi^2)(2mk_B T/\hbar^2)^{3/2} \int_0^\infty x^{1/2}/(e^x - 1)\, dx. $$

The integral $\int_0^\infty x^{1/2}/(e^x - 1)\, dx = \Gamma(3/2)\, \zeta(3/2) = (\sqrt{\pi}/2)\, \zeta(3/2)$. With the thermal de Broglie wavelength $\lambda_{\text{th}} = h/\sqrt{2\pi mk_B T}$:

积分 $\int_0^\infty x^{1/2}/(e^x - 1)\, dx = \Gamma(3/2)\, \zeta(3/2) = (\sqrt{\pi}/2)\, \zeta(3/2)$。令热德布罗意波长 $\lambda_{\text{th}} = h/\sqrt{2\pi mk_B T}$：

$$ N_{\text{ex}}^{\max} = V\, \zeta(3/2)/\lambda_{\text{th}}^3. $$

**Step 3 — BEC condition: $N_{\text{ex}}^{\max} = N$.** BEC occurs when the normal states can no longer accommodate all $N$ particles, i.e., when $N_{\text{ex}}^{\max}(T) = N$:

**第 3 步 — BEC 条件：$N_{\text{ex}}^{\max} = N$。** 当正常态不能再容纳全部 $N$ 个粒子时，即 $N_{\text{ex}}^{\max}(T) = N$ 时，BEC 发生：

$$ \begin{aligned} N &= V\, \zeta(3/2)/\lambda_{\text{th}}^3(T_{\text{BEC}}), \\ n\, \lambda_{\text{th}}^3(T_{\text{BEC}}) &= \zeta(3/2). \end{aligned} $$

This is the phase-space density condition: BEC occurs when the inter-particle spacing $n^{-1/3}$ becomes comparable to the thermal de Broglie wavelength $\lambda_{\text{th}}$ (quantum wave-packets start to overlap).

这是相空间密度条件：当粒子间距 $n^{-1/3}$ 与热德布罗意波长 $\lambda_{\text{th}}$ 相当时（量子波包开始重叠），BEC 发生。

**Step 4 — Solve for $T_{\text{BEC}}$.** From $\lambda_{\text{th}} = h/\sqrt{2\pi mk_B T}$ and $n\, \lambda_{\text{th}}^3 = \zeta(3/2)$:

**第 4 步 — 求解 $T_{\text{BEC}}$。** 由 $\lambda_{\text{th}} = h/\sqrt{2\pi mk_B T}$ 和 $n\, \lambda_{\text{th}}^3 = \zeta(3/2)$：

$$ \begin{aligned} n\, [h/\sqrt{2\pi mk_B T_{\text{BEC}}}]^3 &= \zeta(3/2), \\ (2\pi mk_B T_{\text{BEC}}/h^2)^{3/2} &= n/\zeta(3/2), \end{aligned} $$

$$ \boxed{\, T_{\text{BEC}} = (2\pi\hbar^2/mk_B)(n/\zeta(3/2))^{2/3}. \,} \qquad \blacksquare $$

Below $T_{\text{BEC}}$, the condensate fraction is $N_0/N = 1 - (T/T_{\text{BEC}})^{3/2}$, since for a uniform 3D gas $N_{\text{ex}} \propto T^{3/2}$ and $N_{\text{ex}}(T_{\text{BEC}}) = N$. (A harmonic trap instead gives $N_{\text{ex}} \propto T^3$ and $N_0/N = 1 - (T/T_c)^3$.)

在 $T_{\text{BEC}}$ 以下，凝聚体分数为 $N_0/N = 1 - (T/T_{\text{BEC}})^{3/2}$，因为对均匀三维气体 $N_{\text{ex}} \propto T^{3/2}$ 且 $N_{\text{ex}}(T_{\text{BEC}}) = N$。（谐振子阱中则为 $N_{\text{ex}} \propto T^3$、$N_0/N = 1 - (T/T_c)^3$。）

---

*The common thread through A, B, C, D is the Bose–Einstein distribution with $\mu = 0$ applied to different systems: photons (Planck, Stefan–Boltzmann), phonons (Debye $T^3$), and conserved bosons (BEC). The Fermi parallel — Sommerfeld expansion for electrons — produces the linear-$T$ electronic heat capacity. Together these four results are the quantitative foundation of low-temperature physics.*

*A、B、C、D 的共同主线是将 $\mu = 0$ 的玻色–爱因斯坦分布应用于不同系统：光子（普朗克，斯特藩–玻尔兹曼）、声子（德拜 $T^3$）和守恒玻色子（BEC）。费米的对应物——电子的索末菲展开——给出线性 $T$ 电子热容。这四个结果合在一起构成低温物理的定量基础。*

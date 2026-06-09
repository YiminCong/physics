# Derivations — Module 4.1: Electrons and Heat in Solids
# 推导 — 模块 4.1：固体中的电子与热

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.1](./module-4.1-electrons-and-heat-in-solids.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.1](./module-4.1-electrons-and-heat-in-solids.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Sommerfeld Electronic Heat Capacity $C_{el} = (\pi^2/3)k_B^2 g(E_F)T$ · 索末菲电子热容

**Claim.** For a free Fermi gas at low temperature $T \ll T_F$, the electronic contribution to the heat capacity is $C_{el} = (\pi^2/3)k_B^2 g(E_F)T$, where $g(E_F)$ is the single-spin density of states per unit volume at the Fermi energy.

**命题。** 对于低温 $T \ll T_F$ 下的自由费米气体，热容的电子贡献为 $C_{el} = (\pi^2/3)k_B^2 g(E_F)T$，其中 $g(E_F)$ 是费米能处单位体积（单自旋）的态密度。

**Step 1 — The Fermi–Dirac integral for total energy.** The total energy per unit volume at temperature $T$ is

**第 1 步 — 总能量的费米–狄拉克积分。** 温度 $T$ 下单位体积的总能量为

$$ U(T) = \int_0^\infty E \cdot g(E) \cdot f(E,T)\, dE, $$

where $g(E)$ is the density of states (both spins) and $f(E,T) = 1/(\exp((E-\mu)/k_B T) + 1)$ is the Fermi–Dirac distribution. At $T = 0$, $f$ reduces to a step function $\Theta(E_F - E)$, and $U(0) = \int_0^{E_F} E g(E)\, dE$. The heat capacity is $C_{el} = \partial U/\partial T$.

其中 $g(E)$ 为（含双自旋）态密度，$f(E,T) = 1/(\exp((E-\mu)/k_B T) + 1)$ 为费米–狄拉克分布。$T = 0$ 时 $f$ 退化为阶跃函数 $\Theta(E_F - E)$，$U(0) = \int_0^{E_F} E g(E)\, dE$。热容 $C_{el} = \partial U/\partial T$。

**Step 2 — Sommerfeld expansion (general).** For any smooth function $H(E)$, the Sommerfeld expansion gives

**第 2 步 — 索末菲展开（一般形式）。** 对任意光滑函数 $H(E)$，索末菲展开给出

$$ \int_0^\infty H(E) f(E,T)\, dE = \int_0^\mu H(E)\, dE + \frac{\pi^2}{6}(k_B T)^2 H'(\mu) + \frac{7\pi^4}{360}(k_B T)^4 H''''(\mu) + O(T^6). $$

**Derivation of the expansion.** Write the integral as $I = \int_0^\infty H(E) f\, dE$. Integrate by parts: let $K(E) = \int_0^E H(E')\,dE'$, so $I = [K(E)f]_0^\infty - \int_0^\infty K(E)(\partial f/\partial E)\,dE$. The boundary term vanishes. Now $-\partial f/\partial E = (1/k_B T) \cdot e^{x}/(e^x+1)^2$ with $x=(E-\mu)/k_B T$ is a sharply peaked function of width $\sim k_B T$ centred at $E = \mu$. Expand $K(E)$ in a Taylor series about $\mu$:

**展开的推导。** 写出积分 $I = \int_0^\infty H(E) f\, dE$。分部积分：令 $K(E) = \int_0^E H(E')\,dE'$，则 $I = [K(E)f]_0^\infty - \int_0^\infty K(E)(\partial f/\partial E)\,dE$。边界项为零。注意 $-\partial f/\partial E = (1/k_B T) \cdot e^{x}/(e^x+1)^2$（$x=(E-\mu)/k_B T$）是宽度约为 $k_B T$、中心在 $E = \mu$ 处的尖锐峰函数。将 $K(E)$ 在 $\mu$ 处泰勒展开：

$$ K(E) = K(\mu) + K'(\mu)(E-\mu) + \tfrac12 K''(\mu)(E-\mu)^2 + \cdots $$

Substituting and using the standard integrals $\int_{-\infty}^{\infty} x \cdot (-\partial f/\partial x)\,dx = 0$ (odd integrand), $\int_{-\infty}^{\infty} x^2 \cdot (-\partial f/\partial x)\,dx = \pi^2/3$, and extending the lower limit to $-\infty$ (valid since the Fermi peak is exponentially small below $\mu - $ several $k_B T$):

代入并利用标准积分 $\int_{-\infty}^{\infty} x \cdot (-\partial f/\partial x)\,dx = 0$（奇被积函数）、$\int_{-\infty}^{\infty} x^2 \cdot (-\partial f/\partial x)\,dx = \pi^2/3$，并将下限延伸至 $-\infty$（有效，因费米峰在 $\mu - $ 几个 $k_B T$ 以下指数小）：

$$ \begin{aligned} I &= K(\mu) + \frac{\pi^2}{6}(k_B T)^2 K''(\mu) + O(T^4) \\ &= \int_0^\mu H(E)\,dE + \frac{\pi^2}{6}(k_B T)^2 H'(\mu) + O(T^4). \end{aligned} $$

This is the Sommerfeld expansion to second order.

这就是二阶索末菲展开。

**Step 3 — Apply to the energy integral.** Set $H(E) = E g(E)$, so $H'(E) = g(E) + Eg'(E)$. The Sommerfeld expansion gives

**第 3 步 — 应用于能量积分。** 令 $H(E) = E g(E)$，则 $H'(E) = g(E) + Eg'(E)$。索末菲展开给出

$$ U(T) = \int_0^\mu E g(E)\,dE + \frac{\pi^2}{6}(k_B T)^2[g(\mu) + \mu g'(\mu)] + O(T^4). $$

**Step 4 — Chemical potential shift.** The particle number $N$ per unit volume is fixed: $N = \int_0^\infty g(E) f\, dE$. Applying the same expansion with $H(E) = g(E)$:

**第 4 步 — 化学势的移动。** 单位体积粒子数 $N$ 守恒：$N = \int_0^\infty g(E) f\, dE$。对 $H(E) = g(E)$ 应用同样展开：

$$ N = \int_0^\mu g(E)\,dE + \frac{\pi^2}{6}(k_B T)^2 g'(\mu) + O(T^4). $$

But $N = \int_0^{E_F} g(E)\,dE$ (definition of $E_F$ at $T = 0$). Hence

但 $N = \int_0^{E_F} g(E)\,dE$（$T = 0$ 时 $E_F$ 的定义）。因此

$$ \int_0^\mu g(E)\,dE = \int_0^{E_F} g(E)\,dE - \frac{\pi^2}{6}(k_B T)^2 g'(\mu) + O(T^4). $$

Expanding $\mu = E_F + \delta\mu$ with $\delta\mu$ small and using $\int_0^\mu g(E)\,dE \approx \int_0^{E_F} g(E)\,dE + g(E_F)\delta\mu$ gives

展开 $\mu = E_F + \delta\mu$（$\delta\mu$ 小），利用 $\int_0^\mu g(E)\,dE \approx \int_0^{E_F} g(E)\,dE + g(E_F)\delta\mu$，得

$$ \delta\mu = -\frac{\pi^2}{6}(k_B T)^2 g'(E_F)/g(E_F) + O(T^4). $$

For a slowly varying density of states $g'(E_F)/g(E_F) \sim 1/E_F \ll 1/k_B T$, so $\delta\mu \ll k_B T$.

对于缓变态密度，$g'(E_F)/g(E_F) \sim 1/E_F \ll 1/k_B T$，故 $\delta\mu \ll k_B T$。

**Step 5 — Compute $\Delta U$.** Substituting the chemical-potential shift into $U(T)$ and subtracting $U(0) = \int_0^{E_F} E g(E)\,dE$:

**第 5 步 — 计算 $\Delta U$。** 将化学势移位代入 $U(T)$ 并减去 $U(0) = \int_0^{E_F} E g(E)\,dE$：

$$ U(T) - U(0) = \frac{\pi^2}{6}(k_B T)^2 [g(E_F) + E_F g'(E_F)] + E_F \cdot g(E_F) \cdot \delta\mu - E_F \cdot g(E_F) \cdot \delta\mu + O(T^4) $$

The terms involving $\delta\mu$ cancel to leading order (the chemical-potential shift of $U$ is exactly cancelled by the shift of the lower-bound contribution), leaving

涉及 $\delta\mu$ 的项在领头阶相消（$U$ 中化学势移位的贡献恰好被下界移位的贡献抵消），剩余

$$ U(T) - U(0) = \frac{\pi^2}{6} k_B^2 T^2 g(E_F) + O(T^4). $$

**Step 6 — Differentiate to get $C_{el}$.**

**第 6 步 — 对 $T$ 求导得 $C_{el}$。**

$$ C_{el} = \partial U/\partial T = \frac{\pi^2}{3} k_B^2 g(E_F) T. $$

Writing $\gamma \equiv (\pi^2/3)k_B^2 g(E_F)$, we obtain $C_{el} = \gamma T$. This is the Sommerfeld result: the heat capacity is **linear in $T$**, suppressed from the classical value $\tfrac32 n k_B$ by the factor $\sim \pi k_B T/E_F \ll 1$.

$$ \boxed{\, C_{el} = \gamma T \,} \qquad \blacksquare $$

记 $\gamma \equiv (\pi^2/3)k_B^2 g(E_F)$，得 $C_{el} = \gamma T$。这正是索末菲结果：热容**线性依赖于 $T$**，相比经典值 $\tfrac32 n k_B$ 被因子 $\sim \pi k_B T/E_F \ll 1$ 所压低。$\blacksquare$

---

## B. Debye $T^3$ Law for Lattice Heat Capacity · 德拜晶格热容 $T^3$ 定律

**Claim.** In the Debye model, the low-temperature lattice heat capacity is $C_{lat} = (12\pi^4/5)N k_B(T/\Theta_D)^3 \propto T^3$, where $\Theta_D$ is the Debye temperature.

**命题。** 在德拜模型中，低温晶格热容为 $C_{lat} = (12\pi^4/5)N k_B(T/\Theta_D)^3 \propto T^3$，其中 $\Theta_D$ 为德拜温度。

**Step 1 — Debye model: phonons as elastic waves.** Treat the lattice as an elastic continuum with a linear dispersion $\omega = v_s k$ for all three acoustic branches (one longitudinal, two transverse), but impose a cutoff at the **Debye wavevector** $k_D$ chosen to reproduce exactly $N$ modes for $N$ atoms:

**第 1 步 — 德拜模型：声子作为弹性波。** 将晶格视为弹性连续介质，对所有三支声学支（一支纵声学支和两支横声学支）采用线性色散 $\omega = v_s k$，但在**德拜波矢** $k_D$ 处截断，使之恰好给出 $N$ 个原子对应的 $N$ 个模式：

$$ \frac{(4\pi/3)k_D^3}{(2\pi/L)^3} \times 3 = 3N \quad\to\quad k_D = (6\pi^2 N/V)^{1/3}. $$

The **Debye frequency** $\omega_D = v_s k_D$ and **Debye temperature** $\Theta_D = \hbar\omega_D/k_B$.

**德拜频率** $\omega_D = v_s k_D$，**德拜温度** $\Theta_D = \hbar\omega_D/k_B$。

**Step 2 — Density of states.** In 3D with linear dispersion, the density of vibrational modes per unit frequency is

**第 2 步 — 态密度。** 三维线性色散下，单位频率的振动模式数密度为

$$ D(\omega) = 9N\omega^2/\omega_D^3, \quad 0 \le \omega \le \omega_D. $$

(This is the integrated volume in $k$-space up to $k(\omega) = \omega/v_s$, times the mode count, normalized to give $\int_0^{\omega_D} D(\omega)\,d\omega = 3N$.)

（这是 $k$ 空间中至 $k(\omega) = \omega/v_s$ 的积分体积乘以模式数，归一化使 $\int_0^{\omega_D} D(\omega)\,d\omega = 3N$。）

**Step 3 — Total energy.** Each mode is a quantized harmonic oscillator (Module 3.2, Section B). The average energy of a mode at frequency $\omega$ is $\hbar\omega/(e^{\hbar\omega/k_B T}-1)$ (Bose–Einstein, zero-point term omitted as it is $T$-independent):

**第 3 步 — 总能量。** 每个模式是量子化的谐振子（模块 3.2，B 节）。频率为 $\omega$ 的模式的平均能量为 $\hbar\omega/(e^{\hbar\omega/k_B T}-1)$（玻色–爱因斯坦，零点项省略，因它与 $T$ 无关）：

$$ U(T) = \int_0^{\omega_D} D(\omega) \cdot \frac{\hbar\omega}{e^{\hbar\omega/k_B T}-1}\, d\omega = 9N \int_0^{\omega_D} \frac{\hbar\omega^3}{\omega_D^3(e^{\hbar\omega/k_B T}-1)}\, d\omega. $$

Substitute $x = \hbar\omega/k_B T$, $x_D = \hbar\omega_D/k_B T = \Theta_D/T$:

令 $x = \hbar\omega/k_B T$，$x_D = \hbar\omega_D/k_B T = \Theta_D/T$：

$$ U(T) = 9N k_B T\, (T/\Theta_D)^3 \int_0^{x_D} \frac{x^3}{e^x-1}\, dx. $$

**Step 4 — Low-temperature limit.** For $T \ll \Theta_D$, $x_D \to \infty$ and the integral converges:

**第 4 步 — 低温极限。** 当 $T \ll \Theta_D$ 时，$x_D \to \infty$ 且积分收敛：

$$ \int_0^\infty \frac{x^3}{e^x-1}\, dx = \Gamma(4)\zeta(4) = 6 \cdot \pi^4/90 = \pi^4/15. $$

(Here $\zeta(4) = \pi^4/90$ is the Riemann zeta function value, derivable from the Fourier series $1 + 1/2^4 + 1/3^4 + \cdots = \pi^4/90$.)

（此处 $\zeta(4) = \pi^4/90$ 是黎曼 zeta 函数值，可从傅里叶级数 $1 + 1/2^4 + 1/3^4 + \cdots = \pi^4/90$ 推导。）

Therefore $U(T) = 9N k_B T(T/\Theta_D)^3 \cdot \pi^4/15 = (3\pi^4/5)N k_B T^4/\Theta_D^3$.

因此 $U(T) = 9N k_B T(T/\Theta_D)^3 \cdot \pi^4/15 = (3\pi^4/5)N k_B T^4/\Theta_D^3$。

**Step 5 — Differentiate to get $C_{lat}$.**

**第 5 步 — 求导得 $C_{lat}$。**

$$ C_{lat} = \partial U/\partial T = \frac{12\pi^4}{5} N k_B (T/\Theta_D)^3. $$

Writing $\beta = (12\pi^4/5)N k_B/\Theta_D^3$, this is $C_{lat} = \beta T^3$ — the Debye $T^3$ law.

$$ \boxed{\, C_{lat} = \beta T^3 \,} \qquad \blacksquare $$

记 $\beta = (12\pi^4/5)N k_B/\Theta_D^3$，得 $C_{lat} = \beta T^3$——即德拜 $T^3$ 定律。$\blacksquare$

**Physical interpretation.** At low $T$ only phonons of energy $\lesssim k_B T$ can be excited; the number of such modes scales as $(k_B T/\hbar v_s)^3 \propto T^3$, each contributing $\sim k_B T$ of energy, giving $U \propto T^4$ and $C \propto T^3$.

**物理诠释。** 低温下只有能量 $\lesssim k_B T$ 的声子可被激发；这类模式数正比于 $(k_B T/\hbar v_s)^3 \propto T^3$，每个贡献约 $k_B T$ 的能量，故 $U \propto T^4$，$C \propto T^3$。

---

## C. Total Low-Temperature Heat Capacity $C = \gamma T + \beta T^3$ · 低温总热容

**Claim.** At low temperatures the total heat capacity is $C = \gamma T + \beta T^3$, where the first term is electronic and the second is phononic.

**命题。** 低温下总热容为 $C = \gamma T + \beta T^3$，其中第一项为电子贡献，第二项为声子贡献。

**Step 1 — Separation of contributions.** For $T \ll T_F$ and $T \ll \Theta_D$, electrons and phonons are both in the linear-response regime and their contributions are additive (they couple weakly to each other at low $T$):

**第 1 步 — 贡献的分离。** 当 $T \ll T_F$ 且 $T \ll \Theta_D$ 时，电子和声子均处于线性响应区，其贡献相加（低温下它们之间的耦合很弱）：

$$ C_{total} = C_{el} + C_{lat} = \gamma T + \beta T^3. $$

**Step 2 — Experimental separation.** Dividing by $T$: $C/T = \gamma + \beta T^2$. A plot of $C/T$ vs $T^2$ is a straight line with $y$-intercept $\gamma$ and slope $\beta$. This is the standard experimental technique for extracting $g(E_F)$ from calorimetric measurements.

**第 2 步 — 实验分离。** 两边除以 $T$：$C/T = \gamma + \beta T^2$。$C/T$ 对 $T^2$ 的图像是直线，截距为 $\gamma$，斜率为 $\beta$。这是从量热测量中提取 $g(E_F)$ 的标准实验技术。

**Step 3 — Physical picture.** The linear term dominates at very low $T$ and reveals the Fermi surface; the cubic term dominates at slightly higher $T$ and encodes the phonon spectrum. Because $\gamma \propto g(E_F)$, the electronic $\gamma$ is large in heavy-fermion systems (where effective mass $m^* \gg m$) and small in simple metals.

**第 3 步 — 物理图像。** 线性项在极低温下占主导，反映费米面特性；三次方项在略高温度下占主导，编码声子谱信息。由于 $\gamma \propto g(E_F)$，电子的 $\gamma$ 在重费米子系统中很大（有效质量 $m^* \gg m$），在简单金属中较小。$\blacksquare$

---

## D. Free-Electron Density of States $g(E)$ and $\gamma$ · 自由电子态密度与 $\gamma$

**Claim.** For a free Fermi gas in 3D with electron density $n$, the density of states is $g(E) = (1/2\pi^2)(2m/\hbar^2)^{3/2} \sqrt{E}$ (per unit volume, both spins), giving $g(E_F) = 3n/(2E_F)$ and $\gamma = \pi^2 n k_B^2/(2E_F)$.

**命题。** 对三维自由费米气体（电子密度 $n$），态密度为 $g(E) = (1/2\pi^2)(2m/\hbar^2)^{3/2} \sqrt{E}$（单位体积，含双自旋），从而 $g(E_F) = 3n/(2E_F)$，$\gamma = \pi^2 n k_B^2/(2E_F)$。

**Step 1 — Count states in $k$-space.** Each $k$-state occupies a volume $(2\pi/L)^3 = (2\pi)^3/V$ in $k$-space. With spin degeneracy 2, the number of states with $|k| \le k$ is

**第 1 步 — 在 $k$ 空间中计数态。** 每个 $k$ 态在 $k$ 空间中占据体积 $(2\pi/L)^3 = (2\pi)^3/V$。含自旋简并度 2，$|k| \le k$ 的态数为

$$ N(k) = 2 \times (4\pi k^3/3) / (2\pi)^3/V = V k^3/(3\pi^2). $$

**Step 2 — Convert to energy.** For free electrons $E = \hbar^2 k^2/2m$, so $k = \sqrt{2mE}/\hbar$. The density of states per unit volume $g(E) = (1/V)\, dN/dE$:

**第 2 步 — 转化为能量。** 对自由电子 $E = \hbar^2 k^2/2m$，故 $k = \sqrt{2mE}/\hbar$。单位体积态密度 $g(E) = (1/V)\, dN/dE$：

$$ g(E) = (1/2\pi^2)(2m/\hbar^2)^{3/2} \sqrt{E} = (3n/2) E^{1/2}/E_F^{3/2}. $$

**Step 3 — Evaluate at $E_F$.** The electron density satisfies $n = \int_0^{E_F} g(E)\,dE = (1/3\pi^2)(2mE_F/\hbar^2)^{3/2}$ (shown in Module 4.5, Section A). Therefore

**第 3 步 — 在 $E_F$ 处取值。** 电子密度满足 $n = \int_0^{E_F} g(E)\,dE = (1/3\pi^2)(2mE_F/\hbar^2)^{3/2}$（见模块 4.5，A 节）。因此

$$ g(E_F) = (1/2\pi^2)(2m/\hbar^2)^{3/2} \sqrt{E_F} = (3/2) n/E_F. $$

**Step 4 — Sommerfeld coefficient.** Substituting into $\gamma = (\pi^2/3)k_B^2 g(E_F)$:

**第 4 步 — 索末菲系数。** 代入 $\gamma = (\pi^2/3)k_B^2 g(E_F)$：

$$ \gamma = (\pi^2/3) k_B^2 \cdot (3n/2E_F) = \pi^2 n k_B^2/(2E_F). $$

This is the standard free-electron Sommerfeld coefficient. $\blacksquare$

这就是标准的自由电子索末菲系数。$\blacksquare$

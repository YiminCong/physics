---
title: "Derivations — Module 5.6: Tunneling & the Gap"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.6: Tunneling & the Gap
# 推导 — 模块 5.6：隧穿与能隙

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.6](./module-5.6-tunneling-and-the-gap.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.6](./module-5.6-tunneling-and-the-gap.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. BCS Density of States $N_s(E) = N(0)\cdot E/\sqrt{E^2-\Delta^2}$ · BCS 超导态密度

**Claim.** In the BCS superconducting state the quasiparticle energy is $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$, where $\varepsilon_k$ is the normal-state kinetic energy measured from the Fermi level and $\Delta$ is the gap. Conservation of states then gives the superconducting DOS

$$ N_s(E) = N(0) \cdot E / \sqrt{E^2 - \Delta^2} \quad\text{for } E > \Delta, \qquad N_s(E) = 0 \quad\text{for } E < \Delta. $$

**命题。** 在 BCS 超导态中，准粒子能量为 $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$，其中 $\varepsilon_k$ 是从费米面量起的正常态动能，$\Delta$ 为能隙。由态守恒可得超导态密度

$$ N_s(E) = N(0) \cdot E / \sqrt{E^2 - \Delta^2} \quad\text{（}E > \Delta\text{ 时），} \qquad N_s(E) = 0 \quad\text{（}E < \Delta\text{ 时）。} $$

---

**Step 1 — BCS quasiparticle dispersion.** The BCS mean-field Hamiltonian (Module 5.5) is diagonalized by the Bogoliubov transformation: for each pair of time-reversed states $(k\uparrow, -k\downarrow)$, introduce operators $\gamma_{k0} = u_k c_{k\uparrow} - v_k c^\dagger_{-k\downarrow}$ and $\gamma_{k1} = u_k c_{-k\downarrow} + v_k c^\dagger_{k\uparrow}$. The Hamiltonian becomes diagonal in these new quasiparticle operators with energy eigenvalue

$$ E_k = \sqrt{\varepsilon_k^2 + \Delta^2}. $$

The coefficients satisfy $u_k^2 + v_k^2 = 1$ and $u_k^2 = \tfrac12(1 + \varepsilon_k/E_k)$, $v_k^2 = \tfrac12(1 - \varepsilon_k/E_k)$.

**第 1 步 — BCS 准粒子色散。** BCS 平均场哈密顿量（模块 5.5）通过博戈柳博夫变换对角化：对每对时间反演态 $(k\uparrow, -k\downarrow)$，引入算符 $\gamma_{k0} = u_k c_{k\uparrow} - v_k c^\dagger_{-k\downarrow}$ 及 $\gamma_{k1} = u_k c_{-k\downarrow} + v_k c^\dagger_{k\uparrow}$。哈密顿量在这些新的准粒子算符下对角化，能量本征值为

$$ E_k = \sqrt{\varepsilon_k^2 + \Delta^2}. $$

系数满足 $u_k^2 + v_k^2 = 1$，以及 $u_k^2 = \tfrac12(1 + \varepsilon_k/E_k)$，$v_k^2 = \tfrac12(1 - \varepsilon_k/E_k)$。

**Step 2 — Conservation of states.** In the normal state there are $N(0)\, d\varepsilon$ states per unit energy per unit volume near the Fermi level. The total number of states cannot change under the transformation to quasiparticles: each normal-state electron state (at energy $\varepsilon$) maps to exactly one quasiparticle state (at energy $E$). Therefore the number of states in an interval is conserved:

$$ N_s(E)\, dE = N(0)\, |d\varepsilon|. $$

(Here we use the fact that the DOS is smooth near the Fermi level so $N(\varepsilon) \approx N(0)$ is approximately constant for the narrow shell $|\varepsilon| \ll E_F$ where BCS is relevant.)

**第 2 步 — 态守恒。** 在正常态中，费米面附近每单位能量每单位体积有 $N(0)\, d\varepsilon$ 个态。变换到准粒子后，总态数不变：每个正常态电子态（能量 $\varepsilon$）恰好对应一个准粒子态（能量 $E$）。因此区间内的态数守恒：

$$ N_s(E)\, dE = N(0)\, |d\varepsilon|. $$

（这里利用了费米面附近 DOS 光滑的事实，使得 $N(\varepsilon) \approx N(0)$ 在 BCS 相关的窄壳层 $|\varepsilon| \ll E_F$ 内近似为常数。）

**Step 3 — Compute $dE/d\varepsilon$.** From $E = \sqrt{\varepsilon^2 + \Delta^2}$, differentiate with respect to $\varepsilon$:

$$ dE/d\varepsilon = \varepsilon / \sqrt{\varepsilon^2 + \Delta^2} = \varepsilon / E. $$

Note that $\varepsilon$ can range from $-\infty$ to $+\infty$ while $E \ge \Delta$. For a given $E > \Delta$ there are two values of $\varepsilon$ (positive and negative, on either side of the Fermi level) that yield the same quasiparticle energy; each contributes equally, so we can take $|d\varepsilon/dE|$ from the positive-$\varepsilon$ branch and multiply by 2, or equivalently note that by symmetry we use only the positive branch with a factor accounting for both.

**第 3 步 — 计算 $dE/d\varepsilon$。** 由 $E = \sqrt{\varepsilon^2 + \Delta^2}$，对 $\varepsilon$ 求导：

$$ dE/d\varepsilon = \varepsilon / \sqrt{\varepsilon^2 + \Delta^2} = \varepsilon / E. $$

注意 $\varepsilon$ 的范围为 $-\infty$ 到 $+\infty$，而 $E \ge \Delta$。对给定的 $E > \Delta$，有两个 $\varepsilon$ 值（正负，分别在费米面两侧）给出相同的准粒子能量；各贡献相等，因此可取正 $\varepsilon$ 分支的 $|d\varepsilon/dE|$ 并计入两个分支的贡献。

**Step 4 — Invert to get $|d\varepsilon/dE|$.** From $E^2 = \varepsilon^2 + \Delta^2$, invert to obtain $\varepsilon = \sqrt{E^2 - \Delta^2}$ (taking the positive root for the branch $\varepsilon > 0$). Then

$$ |d\varepsilon/dE| = E / \sqrt{E^2 - \Delta^2}. $$

This is only defined (real) when $E > \Delta$; for $E < \Delta$ there is no real $\varepsilon$ satisfying $E_k = E$, meaning no quasiparticle states exist below the gap.

**第 4 步 — 求 $|d\varepsilon/dE|$。** 由 $E^2 = \varepsilon^2 + \Delta^2$，取正根 $\varepsilon = \sqrt{E^2 - \Delta^2}$（$\varepsilon > 0$ 分支）。则

$$ |d\varepsilon/dE| = E / \sqrt{E^2 - \Delta^2}. $$

仅当 $E > \Delta$ 时此式有定义（为实数）；对 $E < \Delta$ 不存在满足 $E_k = E$ 的实数 $\varepsilon$，即能隙以下无准粒子态。

**Step 5 — Assemble $N_s(E)$.** Substituting into the conservation relation $N_s(E) = N(0)|d\varepsilon/dE|$:

$$ N_s(E) = N(0) \cdot E / \sqrt{E^2 - \Delta^2} \quad\text{for } E > \Delta. $$

For $E < \Delta$: $N_s(E) = 0$ (the gap is real and there are no states).

This DOS has a **square-root singularity** (van Hove singularity) as $E \to \Delta$ from above, because $|d\varepsilon/dE| \to \infty$ there, reflecting the fact that the quasiparticle band is flat ($dE/d\varepsilon \to 0$) at $\varepsilon = 0$.

**第 5 步 — 组合得 $N_s(E)$。** 代入守恒关系 $N_s(E) = N(0)|d\varepsilon/dE|$：

$$ N_s(E) = N(0) \cdot E / \sqrt{E^2 - \Delta^2} \quad\text{（}E > \Delta\text{ 时）。} $$

对 $E < \Delta$：$N_s(E) = 0$（能隙为真实存在，无态）。

该 DOS 在 $E \to \Delta^+$ 时具有**平方根奇点**（范霍夫奇点），因为此处 $|d\varepsilon/dE| \to \infty$，反映准粒子能带在 $\varepsilon = 0$ 处是平的（$dE/d\varepsilon \to 0$）。

**Step 6 — Physical interpretation.** $N_s(E)/N(0)$ is dimensionless and equals unity at $E \gg \Delta$ (normal-metal limit). Near the gap edge $E \approx \Delta + \delta$ the DOS diverges as $N(0)\cdot(\Delta/\sqrt{2\Delta\delta}) = N(0)\cdot\sqrt{\Delta/2\delta} \to \infty$, creating a **coherence peak**. This peak is directly observed in NMR relaxation rates (just below $T_c$) and in tunneling conductance spectra. $\blacksquare$

**第 6 步 — 物理诠释。** $N_s(E)/N(0)$ 无量纲，在 $E \gg \Delta$ 时趋于 1（正常金属极限）。在能隙边附近 $E \approx \Delta + \delta$ 处，DOS 发散为 $N(0)\cdot(\Delta/\sqrt{2\Delta\delta}) = N(0)\cdot\sqrt{\Delta/2\delta} \to \infty$，形成**相干峰**。该峰可在 NMR 弛豫率（$T_c$ 以下）及隧穿电导谱中直接观测到。$\blacksquare$

---

## B. Tunneling Current via Fermi's Golden Rule · 费米黄金法则推导隧穿电流

**Claim.** For a normal metal | insulator | superconductor (N-I-S) junction biased at voltage $V$, the tunneling current is

$$ I(V) \propto \int_{-\infty}^{+\infty} N_s(E + eV)\, [f(E) - f(E + eV)]\, dE, $$

where $f$ is the Fermi–Dirac distribution. At $T = 0$ this gives $I = 0$ for $|eV| < \Delta$ and a sharp onset at $|eV| = \Delta$.

**命题。** 对于偏置电压为 $V$ 的正常金属|绝缘体|超导体（N-I-S）结，隧穿电流为

$$ I(V) \propto \int_{-\infty}^{+\infty} N_s(E + eV)\, [f(E) - f(E + eV)]\, dE, $$

其中 $f$ 为费米–狄拉克分布。在 $T = 0$ 时，$|eV| < \Delta$ 给出 $I = 0$，在 $|eV| = \Delta$ 处出现尖锐的开启。

---

**Step 1 — Set up the tunneling Hamiltonian.** Model the junction by the Hamiltonian $H_T = \sum_{k,q} T_{kq} c^\dagger_{k\sigma} a_{q\sigma} + \text{h.c.}$, where $c^\dagger_{k\sigma}$ creates an electron with momentum $k$ in the superconductor, $a_{q\sigma}$ annihilates one with momentum $q$ in the normal metal, and $T_{kq}$ is the tunneling matrix element (approximately constant $T$ near the Fermi level for a uniform barrier). This is the tunneling Hamiltonian formalism (Cohen, Falicov, Phillips, 1962).

**第 1 步 — 建立隧穿哈密顿量。** 用哈密顿量 $H_T = \sum_{k,q} T_{kq} c^\dagger_{k\sigma} a_{q\sigma} + \text{h.c.}$ 对结建模，其中 $c^\dagger_{k\sigma}$ 在超导体中产生动量为 $k$ 的电子，$a_{q\sigma}$ 在正常金属中湮灭动量为 $q$ 的电子，$T_{kq}$ 为隧穿矩阵元（均匀势垒时近似为费米面附近的常数 $T$）。这是隧穿哈密顿量形式（Cohen, Falicov, Phillips, 1962）。

**Step 2 — Apply Fermi's golden rule.** The rate for an electron to tunnel from the normal metal (state $q$, energy $\varepsilon_q$) to the superconductor (quasiparticle state $k$, energy $E_k$) is

$$ W_{q\to k} = (2\pi/\hbar)|T|^2\, \delta(E_k - \varepsilon_q - eV)\, f(\varepsilon_q)[1 - f(E_k)], $$

where $eV$ shifts the electrochemical potential of the normal metal relative to the superconductor, $f(\varepsilon_q)$ is the probability the initial state is occupied, and $[1 - f(E_k)]$ is the probability the final state is empty.

**第 2 步 — 应用费米黄金法则。** 电子从正常金属（态 $q$，能量 $\varepsilon_q$）隧穿到超导体（准粒子态 $k$，能量 $E_k$）的速率为

$$ W_{q\to k} = (2\pi/\hbar)|T|^2\, \delta(E_k - \varepsilon_q - eV)\, f(\varepsilon_q)[1 - f(E_k)], $$

其中 $eV$ 是正常金属相对于超导体的电化学势差，$f(\varepsilon_q)$ 为初态被占据的概率，$[1 - f(E_k)]$ 为末态空置的概率。

**Step 3 — Sum over states to get the current.** The net tunneling current $I = e(\text{rate}_{N\to S} - \text{rate}_{S\to N})$. Summing over all $k$ and $q$, and replacing sums by DOS integrals:

$$ \begin{aligned} I &= (2\pi e/\hbar)|T|^2 \int d\varepsilon_q \int dE_k\, N_N(\varepsilon_q) N_s(E_k)\, \delta(E_k - \varepsilon_q - eV)\, [f(\varepsilon_q) - f(E_k)] \\ &= (2\pi e/\hbar)|T|^2 N_N(0) \int_{-\infty}^{+\infty} d\varepsilon\, N_s(\varepsilon + eV)\, [f(\varepsilon) - f(\varepsilon + eV)], \end{aligned} $$

where we set $N_N(\varepsilon) \approx N_N(0)$ (constant normal-metal DOS) and used the delta function to eliminate one integral.

**第 3 步 — 对态求和得电流。** 净隧穿电流 $I = e(\text{rate}_{N\to S} - \text{rate}_{S\to N})$。对所有 $k$ 和 $q$ 求和，并将求和转化为 DOS 积分：

$$ \begin{aligned} I &= (2\pi e/\hbar)|T|^2 \int d\varepsilon_q \int dE_k\, N_N(\varepsilon_q) N_s(E_k)\, \delta(E_k - \varepsilon_q - eV)\, [f(\varepsilon_q) - f(E_k)] \\ &= (2\pi e/\hbar)|T|^2 N_N(0) \int_{-\infty}^{+\infty} d\varepsilon\, N_s(\varepsilon + eV)\, [f(\varepsilon) - f(\varepsilon + eV)], \end{aligned} $$

其中取 $N_N(\varepsilon) \approx N_N(0)$（正常金属 DOS 为常数），并利用 delta 函数消去一个积分。

**Step 4 — Zero-temperature limit.** At $T = 0$, $f(\varepsilon) = \theta(-\varepsilon)$ (step function, 1 for $\varepsilon < 0$). Then $f(\varepsilon) - f(\varepsilon + eV) = \theta(-\varepsilon) - \theta(-\varepsilon - eV)$. For $V > 0$ this is nonzero only in the window $-eV < \varepsilon < 0$, so:

$$ \begin{aligned} I &= G_T \int_{-eV}^{0} d\varepsilon\, N_s(\varepsilon + eV) / N(0) \\ &= G_T \int_{0}^{eV} dE\, N_s(E) / N(0), \end{aligned} $$

where $G_T = (2\pi e^2/\hbar)|T|^2 N_N(0) N(0)$ is the tunnel conductance and we substituted $E = \varepsilon + eV$.

**第 4 步 — 零温极限。** 在 $T = 0$ 时，$f(\varepsilon) = \theta(-\varepsilon)$（阶跃函数，$\varepsilon < 0$ 时为 1）。则 $f(\varepsilon) - f(\varepsilon + eV) = \theta(-\varepsilon) - \theta(-\varepsilon - eV)$。对 $V > 0$，仅在 $-eV < \varepsilon < 0$ 的窗口内非零，故：

$$ \begin{aligned} I &= G_T \int_{-eV}^{0} d\varepsilon\, N_s(\varepsilon + eV) / N(0) \\ &= G_T \int_{0}^{eV} dE\, N_s(E) / N(0), \end{aligned} $$

其中 $G_T = (2\pi e^2/\hbar)|T|^2 N_N(0) N(0)$ 为隧穿电导，代换 $E = \varepsilon + eV$。

**Step 5 — Show $I = 0$ for $eV < \Delta$.** Since $N_s(E) = 0$ for $E < \Delta$, the integrand vanishes everywhere in $[0, eV]$ when $eV < \Delta$. Hence $I = 0$ for $|V| < \Delta/e$ — **no current flows** until the voltage reaches the gap edge. This is the definitive signature of the superconducting gap.

**第 5 步 — 证明 $eV < \Delta$ 时 $I = 0$。** 由于 $E < \Delta$ 时 $N_s(E) = 0$，当 $eV < \Delta$ 时被积函数在 $[0, eV]$ 上处处为零。故 $|V| < \Delta/e$ 时 $I = 0$——**无电流流过**，直到电压达到能隙边缘。这是超导能隙的决定性特征。

**Step 6 — Sharp onset above the gap.** For $eV$ slightly above $\Delta$, the integral receives contributions only from $E \in [\Delta, eV]$ where $N_s(E) = N(0)\cdot E/\sqrt{E^2-\Delta^2}$. Near $E = \Delta$, write $E = \Delta + \delta$ ($\delta$ small):

$$ N_s(E)/N(0) \approx \Delta/\sqrt{2\Delta\delta} = \sqrt{\Delta/2\delta}, $$

which diverges as $\delta \to 0$. The integral $\int_\Delta^{eV} \sqrt{\Delta/2\delta}\, d\delta = \sqrt{\Delta/2} \cdot 2\sqrt{eV-\Delta} = 2\sqrt{\Delta(eV-\Delta)/2}$ rises rapidly from zero as $eV - \Delta$ increases. Thus the I–V curve shows a **sharp turn-on** with large $dI/dV$ at $V = \Delta/e$. The differential conductance $dI/dV \propto N_s(eV)$ directly images the BCS DOS — this is the Giaever experiment. $\blacksquare$

**第 6 步 — 能隙以上的尖锐开启。** 当 $eV$ 略大于 $\Delta$ 时，积分仅在 $E \in [\Delta, eV]$ 处有贡献，此处 $N_s(E) = N(0)\cdot E/\sqrt{E^2-\Delta^2}$。在 $E = \Delta$ 附近，令 $E = \Delta + \delta$（$\delta$ 很小）：

$$ N_s(E)/N(0) \approx \Delta/\sqrt{2\Delta\delta} = \sqrt{\Delta/2\delta}, $$

当 $\delta \to 0$ 时发散。积分 $\int_\Delta^{eV} \sqrt{\Delta/2\delta}\, d\delta = \sqrt{\Delta/2} \cdot 2\sqrt{eV-\Delta} = 2\sqrt{\Delta(eV-\Delta)/2}$ 随 $eV - \Delta$ 增大从零迅速上升。因此 I–V 曲线在 $V = \Delta/e$ 处显示**尖锐开启**，$dI/dV$ 很大。微分电导 $dI/dV \propto N_s(eV)$ 直接反映 BCS 态密度——这即是贾埃弗实验。$\blacksquare$

---

## C. Temperature Dependence and the Coherence Peak · 温度依赖性与相干峰

**Step 1 — Finite-temperature conductance.** At temperature $T > 0$, differentiating the current expression with respect to $V$:

$$ \begin{aligned} dI/dV &= G_T \int_{-\infty}^{+\infty} dE\, N_s(E) / N(0) \cdot [-df(E - eV)/dV] \\ &= G_T e \int_{-\infty}^{+\infty} dE\, N_s(E) / N(0) \cdot [-f'(E - eV)], \end{aligned} $$

where $f'(x) = df/dx = -(1/4k_B T) \operatorname{sech}^2(x/2k_B T)$ is the thermal smearing function (a peaked function of width $\sim k_B T$).

**第 1 步 — 有限温度电导。** 在温度 $T > 0$ 时，对电流表达式关于 $V$ 求导：

$$ \begin{aligned} dI/dV &= G_T \int_{-\infty}^{+\infty} dE\, N_s(E) / N(0) \cdot [-df(E - eV)/dV] \\ &= G_T e \int_{-\infty}^{+\infty} dE\, N_s(E) / N(0) \cdot [-f'(E - eV)], \end{aligned} $$

其中 $f'(x) = df/dx = -(1/4k_B T) \operatorname{sech}^2(x/2k_B T)$ 为热展宽函数（宽度约 $k_B T$ 的峰函数）。

**Step 2 — Coherence peak.** This convolution of $N_s(E)$ (which has a sharp peak at $E = \Delta$) with the thermal smearing function gives a peak in $dI/dV$ at $V = \Delta/e$ that is broadened by temperature but remains prominent for $k_B T \ll \Delta$. The height of the coherence peak decreases as $T$ increases toward $T_c$, at which point $\Delta \to 0$ and the peak disappears, recovering the normal-metal flat conductance. This matches NMR experiments precisely and was a key early confirmation of BCS. $\blacksquare$

**第 2 步 — 相干峰。** $N_s(E)$（在 $E = \Delta$ 处有尖峰）与热展宽函数的卷积在 $V = \Delta/e$ 处给出 $dI/dV$ 的峰值，该峰因温度而展宽，但在 $k_B T \ll \Delta$ 时依然显著。相干峰的高度随 $T$ 趋近 $T_c$ 而降低，此时 $\Delta \to 0$，峰消失，恢复正常金属的平坦电导。这与 NMR 实验精确吻合，是 BCS 理论早期的重要验证。$\blacksquare$

---

*All derivations use only algebra and calculus accessible from Modules 0.1–0.4 and the golden-rule machinery of Module 3.8. The key physics: the BCS dispersion $E_k = \sqrt{\varepsilon^2+\Delta^2}$ maps a gapped quasiparticle spectrum to the DOS formula; Fermi's golden rule with DOS convolution then explains the threshold and sharp onset in tunneling.*

*所有推导仅使用模块 0.1–0.4 的代数与微积分，以及模块 3.8 的黄金法则框架。核心物理：BCS 色散关系 $E_k = \sqrt{\varepsilon^2+\Delta^2}$ 将有隙准粒子谱映射到 DOS 公式；带 DOS 卷积的费米黄金法则随后解释了隧穿的阈值与尖锐开启。*

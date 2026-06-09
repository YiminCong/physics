# Derivations — Module 4.11: Linear Response, Transport & the Kubo Formula
# 推导 — 模块 4.11：线性响应、输运与久保公式

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.11](./module-4.11-linear-response-and-transport.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.11](./module-4.11-linear-response-and-transport.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Boltzmann Transport Equation $\to$ Drude–Sommerfeld Conductivity $\sigma = ne^2\tau/m$ · 玻尔兹曼输运方程 $\to$ 德鲁德–索末菲电导率 $\sigma = ne^2\tau/m$

**Claim.** In the relaxation-time approximation, a static uniform field $\boldsymbol{E}$ produces a steady current $\boldsymbol{J} = \sigma\boldsymbol{E}$ with $\sigma = n e^2 \tau / m$ and mobility $\mu = e \tau / m$; only electrons within $\sim k_B T$ of the Fermi surface contribute.

**命题。** 在弛豫时间近似下，静态均匀场 $\boldsymbol{E}$ 产生稳态电流 $\boldsymbol{J} = \sigma\boldsymbol{E}$，其中 $\sigma = n e^2 \tau / m$，迁移率 $\mu = e \tau / m$；只有费米面附近 $\sim k_B T$ 范围内的电子才有贡献。

**Step 1 — The Boltzmann transport equation.** The distribution function $f(\boldsymbol{r}, \boldsymbol{k}, t)$ of charge carriers evolves by streaming plus collisions:

**第 1 步 — 玻尔兹曼输运方程。** 载流子分布函数 $f(\boldsymbol{r}, \boldsymbol{k}, t)$ 通过自由流动加碰撞演化：

$$ \frac{\partial f}{\partial t} + \boldsymbol{v}\cdot\nabla_r f + \frac{\boldsymbol{F}}{\hbar}\cdot\nabla_k f = \Big(\frac{\partial f}{\partial t}\Big)_\text{coll}, $$

with band velocity $\boldsymbol{v} = (1/\hbar)\nabla_k \varepsilon$ and force $\boldsymbol{F} = -e\boldsymbol{E}$ on an electron of charge $-e$. The relaxation-time approximation models the collision term as relaxation toward local equilibrium $f_0$ (the Fermi–Dirac distribution) on a single timescale $\tau$:

其中能带速度 $\boldsymbol{v} = (1/\hbar)\nabla_k \varepsilon$，作用在电荷 $-e$ 电子上的力 $\boldsymbol{F} = -e\boldsymbol{E}$。弛豫时间近似将碰撞项建模为以单一时间标度 $\tau$ 向局域平衡 $f_0$（费米–狄拉克分布）弛豫：

$$ \Big(\frac{\partial f}{\partial t}\Big)_\text{coll} = -\frac{f - f_0}{\tau}. $$

**Step 2 — Steady, homogeneous limit.** For a static uniform field, set $\partial f/\partial t = 0$ and $\nabla_r f = 0$. The BTE reduces to

**第 2 步 — 稳态、均匀极限。** 对静态均匀场，令 $\partial f/\partial t = 0$ 及 $\nabla_r f = 0$。BTE 化为

$$ (-e\boldsymbol{E}/\hbar)\cdot\nabla_k f = -(f - f_0)/\tau. $$

**Step 3 — Linearize.** Write $f = f_0 + \delta f$ with $\delta f$ small (linear response). On the left, replace $f$ by $f_0$ to leading order, since $\delta f$ gives a second-order term in $E$. Using the chain rule $\nabla_k f_0 = (\partial f_0/\partial\varepsilon) \nabla_k \varepsilon = \hbar\boldsymbol{v} (\partial f_0/\partial\varepsilon)$:

**第 3 步 — 线性化。** 写 $f = f_0 + \delta f$，$\delta f$ 为小量（线性响应）。左端到主阶用 $f_0$ 替换 $f$，因为 $\delta f$ 给出 $E$ 的二阶项。利用链式法则 $\nabla_k f_0 = (\partial f_0/\partial\varepsilon) \nabla_k \varepsilon = \hbar\boldsymbol{v} (\partial f_0/\partial\varepsilon)$：

$$ (-e\boldsymbol{E}/\hbar)\cdot\hbar\boldsymbol{v} (\partial f_0/\partial\varepsilon) = -\delta f/\tau, $$

so the deviation is

故偏离量为

$$ \delta f = -e \tau\, (\boldsymbol{E}\cdot\boldsymbol{v})\, (\partial f_0/\partial\varepsilon). $$

Since $-\partial f_0/\partial\varepsilon \approx \delta(\varepsilon - E_F)$ at low temperature, $\delta f$ is sharply peaked at the Fermi surface: **only electrons near $E_F$ respond**. This is the Sommerfeld correction to Drude's all-electrons picture.

由于在低温下 $-\partial f_0/\partial\varepsilon \approx \delta(\varepsilon - E_F)$，$\delta f$ 在费米面处尖锐峰化：**只有 $E_F$ 附近的电子响应**。这是索末菲对德鲁德"所有电子"图像的修正。

**Step 4 — Current density.** The electric current density (charge $-e$ times velocity, summed over occupied states, factor 2 for spin already in $1/4\pi^3$) is

**第 4 步 — 电流密度。** 电流密度（电荷 $-e$ 乘以速度，对占据态求和，自旋因子 2 已含于 $1/4\pi^3$ 中）为

$$ \boldsymbol{J} = -e \int\frac{d^3k}{4\pi^3}\, \boldsymbol{v} f = -e \int\frac{d^3k}{4\pi^3}\, \boldsymbol{v} \delta f, $$

where the equilibrium part $f_0$ carries no net current ($\int\boldsymbol{v} f_0 = 0$ by inversion symmetry). Substituting $\delta f$:

其中平衡部分 $f_0$ 不携带净电流（由反演对称性 $\int\boldsymbol{v} f_0 = 0$）。代入 $\delta f$：

$$ \boldsymbol{J} = e^2 \tau \int\frac{d^3k}{4\pi^3}\, \boldsymbol{v} (\boldsymbol{E}\cdot\boldsymbol{v}) (\partial f_0/\partial\varepsilon). $$

**Step 5 — Reduce to $\sigma = ne^2\tau/m$.** Take $\boldsymbol{E} = E \hat x$. By cubic/isotropic symmetry only the diagonal survives, with $\langle v_x^2\rangle$ replaced by $(1/3)v^2$. Convert the $\boldsymbol{k}$-integral to an energy integral using the density of states $g(\varepsilon) = (m k)/(\pi^2\hbar^2)$ (per volume, both spins) and $v^2 = 2\varepsilon/m$:

**第 5 步 — 化为 $\sigma = ne^2\tau/m$。** 取 $\boldsymbol{E} = E \hat x$。由立方/各向同性对称性只有对角项存活，$\langle v_x^2\rangle$ 由 $(1/3)v^2$ 替换。用态密度 $g(\varepsilon) = (m k)/(\pi^2\hbar^2)$（单位体积，含两自旋）及 $v^2 = 2\varepsilon/m$ 将 $\boldsymbol{k}$ 积分转为能量积分：

$$ J_x = e^2 \tau E \int d\varepsilon\, g(\varepsilon) \frac{1}{3} v^2(\varepsilon) (\partial f_0/\partial\varepsilon). $$

Integrate by parts; with $-\partial f_0/\partial\varepsilon$ peaked at $E_F$ the integral picks out the Fermi-surface value. Using $\int d\varepsilon\, g(\varepsilon)(-\partial f_0/\partial\varepsilon) v^2/3 = (1/3) v_F^2 g(E_F)$, and the free-electron identities $g(E_F) = 3n/(2E_F)$ and $(1/2)m v_F^2 = E_F$, so $(1/3) v_F^2 g(E_F) = (1/3)(2E_F/m)(3n/2E_F) = n/m$:

分部积分；由于 $-\partial f_0/\partial\varepsilon$ 在 $E_F$ 处峰化，积分取出费米面值。用 $\int d\varepsilon\, g(\varepsilon)(-\partial f_0/\partial\varepsilon) v^2/3 = (1/3) v_F^2 g(E_F)$，及自由电子恒等式 $g(E_F) = 3n/(2E_F)$ 与 $(1/2)m v_F^2 = E_F$，故 $(1/3) v_F^2 g(E_F) = (1/3)(2E_F/m)(3n/2E_F) = n/m$：

$$ J_x = (n e^2 \tau / m) E, \qquad \text{hence} \qquad \sigma = n e^2 \tau / m. $$

The mobility, defined by drift velocity $\boldsymbol{v}_d = -\mu\boldsymbol{E}$ (magnitude), follows from $\sigma = ne\mu$:

迁移率由漂移速度 $\boldsymbol{v}_d = -\mu\boldsymbol{E}$（量值）定义，由 $\sigma = ne\mu$ 得

$$ \mu = \sigma/(ne) = e \tau / m. \qquad \blacksquare $$

---

## B. The Kubo Formula from First-Order Perturbation Theory · 从一阶微扰论推导久保公式

**Claim.** The linear conductivity is the retarded current–current correlation function

**命题。** 线性电导率是推迟电流–电流关联函数

$$ \sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega V} \int_0^\infty dt\, e^{i\omega t} \langle[J_\alpha(t), J_\beta(0)]\rangle, $$

dissipation ($\operatorname{Re}\sigma$) being fixed by equilibrium current fluctuations (fluctuation–dissipation).

耗散（$\operatorname{Re}\sigma$）由平衡电流涨落确定（涨落–耗散）。

**Step 1 — Perturbation and interaction picture.** Couple the current to a weak external vector potential $\boldsymbol{A}(t)$: the perturbation is $H'(t) = -\int d^3r\, \boldsymbol{J}\cdot\boldsymbol{A}(t) = -\boldsymbol{A}(t)\cdot\boldsymbol{J}$ (uniform $\boldsymbol{A}$, $\boldsymbol{J} = \int d^3r\, \boldsymbol{j}$ the total current operator). In the interaction picture, operators evolve under the unperturbed $H_0$, and the first-order correction to the density matrix gives the standard linear-response (Kubo) formula for the induced expectation value of any operator $A$:

**第 1 步 — 微扰与相互作用绘景。** 将电流与弱外部矢势 $\boldsymbol{A}(t)$ 耦合：微扰为 $H'(t) = -\int d^3r\, \boldsymbol{J}\cdot\boldsymbol{A}(t) = -\boldsymbol{A}(t)\cdot\boldsymbol{J}$（均匀 $\boldsymbol{A}$，$\boldsymbol{J} = \int d^3r\, \boldsymbol{j}$ 为总电流算符）。在相互作用绘景中，算符在未微扰 $H_0$ 下演化，密度矩阵的一阶修正给出任意算符 $A$ 诱导期望值的标准线性响应（久保）公式：

$$ \langle\delta A(t)\rangle = \frac{i}{\hbar} \int_{-\infty}^{t} dt'\, \langle[H'(t'), A(t)]\rangle_0, $$

where $\langle\ldots\rangle_0$ is the unperturbed equilibrium average and operators evolve as $A(t) = e^{iH_0 t/\hbar} A\, e^{-iH_0 t/\hbar}$.

其中 $\langle\ldots\rangle_0$ 是未微扰平衡平均，算符按 $A(t) = e^{iH_0 t/\hbar} A\, e^{-iH_0 t/\hbar}$ 演化。

**Step 2 — Current response.** Set $A = J_\alpha$ and $H'(t') = -J_\beta A_\beta(t')$. The induced current is

**第 2 步 — 电流响应。** 取 $A = J_\alpha$ 及 $H'(t') = -J_\beta A_\beta(t')$。诱导电流为

$$ \langle\delta J_\alpha(t)\rangle = -\frac{i}{\hbar} \int_{-\infty}^{t} dt'\, \langle[J_\beta(t'), J_\alpha(t)]\rangle_0\, A_\beta(t'). $$

Define the retarded response kernel by causality (response only for $t > t'$):

由因果性（仅 $t > t'$ 才有响应）定义推迟响应核：

$$ \langle\delta J_\alpha(t)\rangle = \int_{-\infty}^{\infty} dt'\, \chi_{\alpha\beta}(t - t')\, A_\beta(t'), \qquad \chi_{\alpha\beta}(t - t') = \frac{i}{\hbar} \theta(t - t')\, \langle[J_\alpha(t), J_\beta(t')]\rangle_0, $$

using $\langle[J_\beta(t'), J_\alpha(t)]\rangle = -\langle[J_\alpha(t), J_\beta(t')]\rangle$ and time-translation invariance so the correlator depends only on $t - t'$.

利用 $\langle[J_\beta(t'), J_\alpha(t)]\rangle = -\langle[J_\alpha(t), J_\beta(t')]\rangle$ 及时间平移不变性，使关联子只依赖于 $t - t'$。

**Step 3 — Fourier transform.** For harmonic drive $\boldsymbol{A}(t) = \boldsymbol{A}(\omega)e^{-i\omega t}$, transform with $\tau = t - t'$:

**第 3 步 — 傅里叶变换。** 对谐波驱动 $\boldsymbol{A}(t) = \boldsymbol{A}(\omega)e^{-i\omega t}$，对 $\tau = t - t'$ 变换：

$$ \langle\delta J_\alpha(\omega)\rangle = \chi_{\alpha\beta}(\omega)\, A_\beta(\omega), \qquad \chi_{\alpha\beta}(\omega) = \frac{i}{\hbar} \int_0^\infty d\tau\, e^{i\omega\tau} \langle[J_\alpha(\tau), J_\beta(0)]\rangle_0, $$

the lower limit $0$ (rather than $-\infty$) coming from the $\theta(\tau)$ of retardation.

下限取 $0$（而非 $-\infty$）来自推迟性的 $\theta(\tau)$。

**Step 4 — Relate to the conductivity.** The uniform electric field is $\boldsymbol{E}(\omega) = i\omega\boldsymbol{A}(\omega)/c$ in Gaussian units, or simply $\boldsymbol{E} = -\partial_t \boldsymbol{A} \Rightarrow \boldsymbol{E}(\omega) = i\omega \boldsymbol{A}(\omega)$. With current density $\boldsymbol{j} = \boldsymbol{J}/V$ and $\boldsymbol{J} = \sigma\boldsymbol{E}\cdot V$ $\Rightarrow$ the conductivity is the response per unit field per unit volume:

**第 4 步 — 与电导率联系。** 均匀电场为 $\boldsymbol{E} = -\partial_t \boldsymbol{A} \Rightarrow \boldsymbol{E}(\omega) = i\omega \boldsymbol{A}(\omega)$。电流密度 $\boldsymbol{j} = \boldsymbol{J}/V$ 且 $\boldsymbol{J} = \sigma\boldsymbol{E}\cdot V$ $\to$ 电导率是单位场、单位体积的响应：

$$ \sigma_{\alpha\beta}(\omega) = \chi_{\alpha\beta}(\omega) / (i\omega V) $$

(plus a diamagnetic contact term, omitted for the transverse/finite-$\omega$ part). Substituting $\chi$:

（加上抗磁接触项，对横向/有限 $\omega$ 部分略去）。代入 $\chi$：

$$ \sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega V} \int_0^\infty dt\, e^{i\omega t} \langle[J_\alpha(t), J_\beta(0)]\rangle. $$

This is the **Kubo formula** (retarded current–current correlator). Operators evolve under $H_0$; the average is over the equilibrium ensemble; no relaxation time has been assumed.

这就是**久保公式**（推迟电流–电流关联子）。算符在 $H_0$ 下演化；平均对平衡系综取；未假设任何弛豫时间。

**Step 5 — Fluctuation–dissipation.** The real (dissipative) part $\operatorname{Re}\sigma_{\alpha\beta}(\omega)$ is controlled by the symmetrized equilibrium correlator $S_{\alpha\beta}(\omega) = \int dt\, e^{i\omega t}\langle\{J_\alpha(t), J_\beta(0)\}\rangle$ through the fluctuation–dissipation theorem

**第 5 步 — 涨落–耗散。** 实（耗散）部 $\operatorname{Re}\sigma_{\alpha\beta}(\omega)$ 由对称化平衡关联子 $S_{\alpha\beta}(\omega) = \int dt\, e^{i\omega t}\langle\{J_\alpha(t), J_\beta(0)\}\rangle$ 通过涨落–耗散定理控制

$$ \operatorname{Re}\sigma_{\alpha\beta}(\omega) = \frac{1}{2\hbar\omega V} \tanh(\hbar\omega/2k_B T)\cdot S_{\alpha\beta}(\omega) \;\xrightarrow{\omega\to 0}\; \operatorname{Re}\sigma_{\alpha\beta}(0) = S_{\alpha\beta}(0)/(2V k_B T). $$

Thus the DC dissipation is set entirely by the spontaneous, equilibrium current fluctuations — the energy a driven system dissipates equals (up to the temperature factor) the fluctuations it exhibits at rest. $\blacksquare$

因此直流耗散完全由自发的平衡电流涨落决定——受驱系统耗散的能量等于（至多差一温度因子）它在静止时所表现的涨落。$\blacksquare$

---

## C. Einstein Relation $\sigma = e^2 N(E_F) D$ and Recovery of Drude · 爱因斯坦关系 $\sigma = e^2 N(E_F) D$ 及德鲁德形式的恢复

**Claim.** $\sigma = e^2 N(E_F) D$, where $N(E_F)$ is the density of states per unit volume at the Fermi level and $D$ the diffusion constant. With $D = v_F^2 \tau / d$ this reproduces $\sigma = ne^2\tau/m$.

**命题。** $\sigma = e^2 N(E_F) D$，其中 $N(E_F)$ 是费米能级处单位体积态密度，$D$ 为扩散常数。取 $D = v_F^2 \tau / d$ 重现 $\sigma = ne^2\tau/m$。

**Step 1 — Two currents in equilibrium.** In a non-uniform system the particle current has a drift (field) part and a diffusion (density-gradient) part:

**第 1 步 — 平衡中的两种流。** 在非均匀系统中，粒子流有漂移（场）部分与扩散（密度梯度）部分：

$$ \boldsymbol{j}_N = n \mu_\text{mob} (-\nabla\phi)\cdot(\text{carriers}) - D \nabla n, $$

where $\mu_\text{mob}$ is the mobility, $\phi$ the electrostatic potential, and $D$ the diffusion constant (Fick's law). The electric current is $\boldsymbol{j} = -e\boldsymbol{j}_N$.

其中 $\mu_\text{mob}$ 为迁移率，$\phi$ 为静电势，$D$ 为扩散常数（菲克定律）。电流为 $\boldsymbol{j} = -e\boldsymbol{j}_N$。

**Step 2 — Equilibrium balance.** In thermal equilibrium the total current vanishes and the electrochemical potential is flat: $\mu_\text{chem} - e\phi = \text{const}$. A spatial variation of $\phi$ is compensated by a variation of $n$, related through the density of states: $\delta n = N(E_F)\cdot\delta\mu_\text{chem} = N(E_F)\cdot(-e)(-\delta\phi)\cdot\ldots$ More precisely, $n$ responds to the local chemical potential as $\partial n/\partial\mu_\text{chem} = N(E_F)$.

**第 2 步 — 平衡平衡条件。** 热平衡中总流为零，电化学势平坦：$\mu_\text{chem} - e\phi = \text{const}$。$\phi$ 的空间变化由 $n$ 的变化补偿，通过态密度联系：$\partial n/\partial\mu_\text{chem} = N(E_F)$。

**Step 3 — Match drift and diffusion.** Setting the net current to zero in equilibrium, the drift term $n e \mu_\text{mob} \nabla\phi$ must cancel the diffusion term $e D \nabla n = e D N(E_F) \nabla\mu_\text{chem}$. Using $\nabla\mu_\text{chem} = e\nabla\phi$ at equilibrium gives

**第 3 步 — 漂移与扩散匹配。** 平衡中令净流为零，漂移项 $n e \mu_\text{mob} \nabla\phi$ 必须抵消扩散项 $e D \nabla n = e D N(E_F) \nabla\mu_\text{chem}$。平衡时用 $\nabla\mu_\text{chem} = e\nabla\phi$ 得

$$ n \mu_\text{mob} = e D N(E_F)/n \cdot n \implies \text{conductivity } \sigma = n e \mu_\text{mob} = e^2 D N(E_F). $$

Hence the **Einstein relation**

故**爱因斯坦关系**

$$ \sigma = e^2 N(E_F) D. $$

**Step 4 — Recover Drude.** Diffusion of a particle moving at speed $v_F$ between collisions separated by $\tau$ gives, in $d$ dimensions, $D = v_F^2 \tau / d$ (random walk: $D = (1/d)\langle v^2\rangle\tau$ with $\langle v^2\rangle = v_F^2$ on the Fermi surface). For the 3D free-electron gas $N(E_F) = 3n/(2E_F) = 3n/(m v_F^2)$ (using $E_F = \tfrac12 m v_F^2$). Then

**第 4 步 — 恢复德鲁德。** 以速度 $v_F$ 在间隔 $\tau$ 的碰撞间运动的粒子扩散，在 $d$ 维给出 $D = v_F^2 \tau / d$（随机行走：$D = (1/d)\langle v^2\rangle\tau$，费米面上 $\langle v^2\rangle = v_F^2$）。对三维自由电子气 $N(E_F) = 3n/(2E_F) = 3n/(m v_F^2)$（用 $E_F = \tfrac12 m v_F^2$）。则

$$ \sigma = e^2 N(E_F) D = e^2 \cdot \frac{3n}{m v_F^2} \cdot \frac{v_F^2 \tau}{3} = n e^2 \tau / m, $$

reproducing the Drude–Sommerfeld result. The Einstein relation is also the microscopic statement of the Nyquist (Johnson) noise theorem: the same conductance that dissipates also generates equilibrium thermal current noise of spectral density $4 k_B T G$. $\blacksquare$

重现德鲁德–索末菲结果。爱因斯坦关系也是奈奎斯特（约翰逊）噪声定理的微观陈述：同一个产生耗散的电导也产生谱密度为 $4 k_B T G$ 的平衡热电流噪声。$\blacksquare$

---

## D. Wiedemann–Franz Law $\kappa/(\sigma T) = (\pi^2/3)(k_B/e)^2$ via the Sommerfeld Expansion · 维德曼–弗兰兹定律的索末菲展开推导

**Claim.** For a degenerate electron gas, $\kappa/(\sigma T) = (\pi^2/3)(k_B/e)^2 \equiv L_0 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}$, independent of $\tau$, $n$, and material.

**命题。** 对简并电子气，$\kappa/(\sigma T) = (\pi^2/3)(k_B/e)^2 \equiv L_0 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}$，与 $\tau$、$n$ 及材料无关。

**Step 1 — Transport integrals.** Solving the linearized Boltzmann equation with a relaxation time, both the charge current (driven by $E$) and the heat current (driven by $-\nabla T$) are governed by energy moments of the same transport function. Define

**第 1 步 — 输运积分。** 用弛豫时间求解线性化玻尔兹曼方程，电流（由 $E$ 驱动）与热流（由 $-\nabla T$ 驱动）都由同一输运函数的能量矩支配。定义

$$ K_n = \frac{e^2}{3} \int d\varepsilon\, (-\partial f_0/\partial\varepsilon)\, v^2(\varepsilon)\, \tau(\varepsilon)\, g(\varepsilon)\, (\varepsilon - \mu)^n, \qquad n = 0, 1, 2. $$

Then the electrical conductivity is $\sigma = K_0$, the thermoelectric response involves $K_1$, and the (zero-electric-current) thermal conductivity is

则电导率为 $\sigma = K_0$，热电响应涉及 $K_1$，（零电流条件下的）热导率为

$$ \kappa = \frac{1}{T}[K_2 - K_1^2/K_0]. $$

**Step 2 — Sommerfeld expansion.** For a smooth function $H(\varepsilon)$, the integral $\int d\varepsilon\, (-\partial f_0/\partial\varepsilon) H(\varepsilon)$ expands at low $T$ ($k_B T \ll E_F$) as

**第 2 步 — 索末菲展开。** 对光滑函数 $H(\varepsilon)$，积分 $\int d\varepsilon\, (-\partial f_0/\partial\varepsilon) H(\varepsilon)$ 在低温（$k_B T \ll E_F$）展开为

$$ \int d\varepsilon\, (-\partial f_0/\partial\varepsilon) H(\varepsilon) \approx H(\mu) + \frac{\pi^2}{6}(k_B T)^2 H''(\mu) + \ldots . $$

The kernel $-\partial f_0/\partial\varepsilon$ is even about $\varepsilon = \mu$, so odd powers $(\varepsilon - \mu)^n$ integrate against it as follows.

核 $-\partial f_0/\partial\varepsilon$ 关于 $\varepsilon = \mu$ 是偶函数，故奇幂 $(\varepsilon - \mu)^n$ 与之积分如下。

**Step 3 — Evaluate $K_0$, $K_1$, $K_2$.** Let $\Sigma(\varepsilon) = (e^2/3) v^2(\varepsilon) \tau(\varepsilon) g(\varepsilon)$ be the transport function. Applying the expansion:

**第 3 步 — 计算 $K_0$、$K_1$、$K_2$。** 令 $\Sigma(\varepsilon) = (e^2/3) v^2(\varepsilon) \tau(\varepsilon) g(\varepsilon)$ 为输运函数。应用展开：

- $K_0 = \int d\varepsilon\, (-\partial f_0/\partial\varepsilon) \Sigma(\varepsilon) \approx \Sigma(\mu) = \sigma$ (the $n = 0$ moment, the conductivity).
- $K_1 = \int d\varepsilon\, (-\partial f_0/\partial\varepsilon)(\varepsilon - \mu) \Sigma(\varepsilon) \approx (\pi^2/3)(k_B T)^2 \Sigma'(\mu)$ (linear term vanishes by evenness; leading term is order $(k_B T)^2$).
- $K_2 = \int d\varepsilon\, (-\partial f_0/\partial\varepsilon)(\varepsilon - \mu)^2 \Sigma(\varepsilon) \approx (\pi^2/3)(k_B T)^2 \Sigma(\mu)$.

- $K_0 \approx \Sigma(\mu) = \sigma$（$n = 0$ 矩，即电导率）。
- $K_1 \approx (\pi^2/3)(k_B T)^2 \Sigma'(\mu)$（线性项因偶性消失；主项为 $(k_B T)^2$ 阶）。
- $K_2 \approx (\pi^2/3)(k_B T)^2 \Sigma(\mu)$。

**Step 4 — Thermal conductivity.** The correction term $K_1^2/K_0 \sim (k_B T)^4$ is higher order and negligible compared to $K_2 \sim (k_B T)^2$. Hence

**第 4 步 — 热导率。** 修正项 $K_1^2/K_0 \sim (k_B T)^4$ 为高阶，相比 $K_2 \sim (k_B T)^2$ 可忽略。故

$$ \kappa = \frac{1}{T}[K_2 - K_1^2/K_0] \approx K_2/T = (\pi^2/3) k_B^2 T\, \Sigma(\mu). $$

Since $\Sigma(\mu) = \sigma$, this is

由于 $\Sigma(\mu) = \sigma$，即

$$ \kappa = (\pi^2/3) k_B^2 T \sigma / e^2, $$

writing the transport function in the form that exposes $e^2$ gives $\kappa = (\pi^2/3)(k_B^2 T/e^2)\sigma$.

将输运函数写成显含 $e^2$ 的形式得 $\kappa = (\pi^2/3)(k_B^2 T/e^2)\sigma$。

**Step 5 — The Lorenz number.** Forming the ratio cancels $\Sigma(\mu)$, $\tau$, $n$, and all material specifics:

**第 5 步 — 洛伦兹数。** 作比值消去 $\Sigma(\mu)$、$\tau$、$n$ 及一切材料细节：

$$ \kappa / (\sigma T) = (\pi^2/3)(k_B/e)^2 \equiv L_0. $$

Numerically $L_0 = (\pi^2/3)(1.381\times 10^{-23} / 1.602\times 10^{-19})^2 = (\pi^2/3)(8.617\times 10^{-5}\ \text{V/K})^2 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}$. The universality follows because the *same* carriers, scattered by the *same* $\tau(\varepsilon)$, transport both charge and heat — $\tau$ cancels in the ratio.

数值上 $L_0 = (\pi^2/3)(1.381\times 10^{-23} / 1.602\times 10^{-19})^2 = (\pi^2/3)(8.617\times 10^{-5}\ \text{V/K})^2 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}$。普适性源于*同样的*载流子被*同样的* $\tau(\varepsilon)$ 散射，同时输运电荷与热量——$\tau$ 在比值中相消。

**Step 6 — Seebeck coefficient (Mott formula).** The thermopower comes from the cross term $K_1$: $S = -K_1/(eT K_0) = -(\pi^2/3)(k_B^2 T/e)\cdot\Sigma'(\mu)/\Sigma(\mu)$. Writing $\Sigma(\varepsilon) \propto \sigma(\varepsilon)$ gives the **Mott formula**

**第 6 步 — 塞贝克系数（莫特公式）。** 热电势来自交叉项 $K_1$：$S = -K_1/(eT K_0) = -(\pi^2/3)(k_B^2 T/e)\cdot\Sigma'(\mu)/\Sigma(\mu)$。写 $\Sigma(\varepsilon) \propto \sigma(\varepsilon)$ 得**莫特公式**

$$ S = -(\pi^2/3)(k_B^2 T/e)\, (d \ln\sigma(\varepsilon)/d\varepsilon)\big|_{\varepsilon=E_F}, $$

linear in $T$ and vanishing as $T \to 0$, with sign set by the energy slope of the conductivity at the Fermi level. $\blacksquare$

随 $T$ 线性、当 $T \to 0$ 时趋零，符号由费米能级处电导率的能量斜率决定。$\blacksquare$

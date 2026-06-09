# Derivations — Module 4.10: Landau Fermi-Liquid Theory
# 推导 — 模块 4.10：朗道费米液体理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 4.10](./module-4.10-landau-fermi-liquid-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 4.10](./module-4.10-landau-fermi-liquid-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Quasiparticle Lifetime: $1/\tau \propto (\varepsilon - \varepsilon_F)^2$ · 准粒子寿命：$1/\tau \propto (\varepsilon - \varepsilon_F)^2$

**Claim.** A quasiparticle at energy $\varepsilon$ just above the Fermi surface decays by particle–hole creation at a rate $1/\tau \propto (\varepsilon - \varepsilon_F)^2$, which at finite temperature becomes $1/\tau \propto (k_B T)^2$. Hence its level width vanishes faster than its energy, and quasiparticles are sharply defined as $\varepsilon \to \varepsilon_F$.

**命题。** 费米面上方能量 $\varepsilon$ 处的准粒子通过产生粒子–空穴对衰变，速率为 $1/\tau \propto (\varepsilon - \varepsilon_F)^2$，在有限温度下变为 $1/\tau \propto (k_B T)^2$。因此其能级宽度比其能量衰减得更快，故 $\varepsilon \to \varepsilon_F$ 时准粒子是锐利定义的。

**Step 1 — The decay process.** Label the energy measured from the Fermi level, $\xi \equiv \varepsilon - \varepsilon_F > 0$. The quasiparticle (state 1, energy $\xi_1 > 0$) scatters off a filled state below the sea (state 2, energy $\xi_2 < 0$, i.e. a hole is created), producing two states above the sea (states $1'$, $2'$ with $\xi_1', \xi_2' > 0$). Energy conservation requires $\xi_1 + \xi_2 = \xi_1' + \xi_2'$.

**第 1 步 — 衰变过程。** 用相对费米能级测量的能量记 $\xi \equiv \varepsilon - \varepsilon_F > 0$。准粒子（态 1，能量 $\xi_1 > 0$）散射一个海面下的占据态（态 2，能量 $\xi_2 < 0$，即产生一个空穴），产生海面上的两个态（态 $1'$、$2'$，$\xi_1'$、$\xi_2' > 0$）。能量守恒要求 $\xi_1 + \xi_2 = \xi_1' + \xi_2'$。

**Step 2 — Phase-space (Pauli-blocking) counting.** The rate is given by Fermi's golden rule summed over the allowed final states. Two independent energy integrals remain after energy conservation removes one ($\xi_2$ and $\xi_1'$, with $\xi_2'$ fixed by conservation):

**第 2 步 — 相空间（泡利阻塞）计数。** 速率由对允许末态求和的费米黄金法则给出。能量守恒消去一个变量后，剩两个独立能量积分（$\xi_2$ 与 $\xi_1'$，$\xi_2'$ 由守恒固定）：

$$ 1/\tau \propto \int d\xi_2 \int d\xi_1'\; [\text{occupation/blocking factors}]. $$

**Step 3 — Identify the integration limits.** Pauli blocking imposes three constraints near $T = 0$: the hole state 2 must be *occupied* ($\xi_2 < 0$); the final states $1'$ and $2'$ must be *empty* ($\xi_1' > 0$ and $\xi_2' = \xi_1 + \xi_2 - \xi_1' > 0$). Combining $\xi_2 < 0$ with $\xi_2' > 0$ forces $|\xi_2| < \xi_1$, so $\xi_2$ ranges over a window of width $\xi_1$. For each $\xi_2$, the constraint $0 < \xi_1' < \xi_1 + \xi_2$ leaves a window of width $(\xi_1 + \xi_2)$ for $\xi_1'$.

**第 3 步 — 确定积分限。** 在 $T = 0$ 附近泡利阻塞施加三个约束：空穴态 2 必须*占据*（$\xi_2 < 0$）；末态 $1'$、$2'$ 必须*空*（$\xi_1' > 0$ 且 $\xi_2' = \xi_1 + \xi_2 - \xi_1' > 0$）。将 $\xi_2 < 0$ 与 $\xi_2' > 0$ 结合迫使 $|\xi_2| < \xi_1$，故 $\xi_2$ 在宽度为 $\xi_1$ 的窗口内变化。对每个 $\xi_2$，约束 $0 < \xi_1' < \xi_1 + \xi_2$ 给 $\xi_1'$ 留下宽度为 $(\xi_1 + \xi_2)$ 的窗口。

**Step 4 — Do the integral.** Treating the density of states and matrix element as constants near $E_F$ (they vary on the scale $\varepsilon_F \gg \xi_1$), the available phase space is

**第 4 步 — 计算积分。** 将态密度与矩阵元在 $E_F$ 附近视为常数（它们在 $\varepsilon_F \gg \xi_1$ 的尺度上变化），可用相空间为

$$ 1/\tau \propto \int_{-\xi_1}^0 d\xi_2\, (\xi_1 + \xi_2) = \int_0^{\xi_1} du \cdot u = \xi_1^2/2, $$

where $u = \xi_1 + \xi_2$ runs from $0$ to $\xi_1$. Therefore

其中 $u = \xi_1 + \xi_2$ 从 $0$ 跑到 $\xi_1$。因此

$$ 1/\tau \propto \xi_1^2 = (\varepsilon - \varepsilon_F)^2. $$

**Step 5 — Finite temperature and the sharpness conclusion.** At temperature $T$ with the quasiparticle within $k_B T$ of $E_F$, the two phase-space windows are each set by the thermal width $k_B T$, so the same counting gives $1/\tau \propto (k_B T)^2$. The level width is $\hbar/\tau \propto (\varepsilon - \varepsilon_F)^2$. Compared to the excitation energy itself,

**第 5 步 — 有限温度与锐利性结论。** 在温度 $T$ 下，当准粒子位于 $E_F$ 的 $k_B T$ 范围内时，两个相空间窗口各由热宽度 $k_B T$ 决定，故相同计数给出 $1/\tau \propto (k_B T)^2$。能级宽度为 $\hbar/\tau \propto (\varepsilon - \varepsilon_F)^2$。与激发能本身相比，

$$ (\hbar/\tau)/(\varepsilon - \varepsilon_F) \propto (\varepsilon - \varepsilon_F) \to 0 \quad \text{as } \varepsilon \to \varepsilon_F. $$

The width-to-energy ratio vanishes at the Fermi surface, so the quasiparticle is an arbitrarily sharp, long-lived excitation there. This self-consistency is what makes the entire quasiparticle picture valid. $\blacksquare$

宽度与能量之比在费米面处消失，故准粒子在那里是任意锐利、长寿命的激发。正是这一自洽性使整个准粒子图像成立。$\blacksquare$

---

## B. The Landau Energy Functional & Landau Parameters · 朗道能量泛函与朗道参数

**Claim.** The interaction energy of the quasiparticle liquid is a quadratic functional of $\delta n_k$ controlled by the $f$-function $f_{k\sigma,k'\sigma'} = f^s(\theta) + f^a(\theta)\, \boldsymbol{\sigma}\cdot\boldsymbol{\sigma'}$, whose Legendre components define the dimensionless Landau parameters $F_l^{s,a} = N(0) f_l^{s,a}$.

**命题。** 准粒子液体的相互作用能是 $\delta n_k$ 的二次泛函，由 $f$ 函数 $f_{k\sigma,k'\sigma'} = f^s(\theta) + f^a(\theta)\, \boldsymbol{\sigma}\cdot\boldsymbol{\sigma'}$ 控制，其勒让德分量定义无量纲朗道参数 $F_l^{s,a} = N(0) f_l^{s,a}$。

**Step 1 — Energy as a functional.** Excitations only redistribute occupation by $\delta n_k = n_k - n_k^0$. Expanding the total energy $E[n]$ about the ground state $n^0$ to second order in $\delta n$:

**第 1 步 — 能量作为泛函。** 激发只通过 $\delta n_k = n_k - n_k^0$ 重新分配占据。将总能量 $E[n]$ 在基态 $n^0$ 附近对 $\delta n$ 展开到二阶：

$$ E = E_0 + \sum_k \frac{\delta E}{\delta n_k}\Big|_0 \delta n_k + \frac{1}{2} \sum_{k k'} \frac{\delta^2 E}{\delta n_k\, \delta n_{k'}}\Big|_0 \delta n_k\, \delta n_{k'}. $$

Identify the first functional derivative as the bare quasiparticle energy $\varepsilon_k^0 \equiv (\delta E/\delta n_k)|_0$ and the second as the $f$-function, $f_{k k'} \equiv V (\delta^2 E/\delta n_k\, \delta n_{k'})|_0$ (the volume $V$ makes $f$ intensive):

将一阶泛函导数辨认为裸准粒子能量 $\varepsilon_k^0 \equiv (\delta E/\delta n_k)|_0$，二阶导数辨认为 $f$ 函数，$f_{k k'} \equiv V (\delta^2 E/\delta n_k\, \delta n_{k'})|_0$（体积 $V$ 使 $f$ 为强度量）：

$$ E = E_0 + \sum_k \varepsilon_k^0 \delta n_k + \frac{1}{2V} \sum_{k k'} f_{k k'} \delta n_k\, \delta n_{k'}. $$

**Step 2 — Local quasiparticle energy.** Differentiating, the energy to add one more quasiparticle in the presence of the others is the **dressed** energy

**第 2 步 — 局域准粒子能量。** 求导后，在其他准粒子存在下增加一个准粒子的能量是**穿衣**能量

$$ \varepsilon_k = \frac{\delta E}{\delta n_k} = \varepsilon_k^0 + \frac{1}{V} \sum_{k'} f_{k k'} \delta n_{k'}. $$

This molecular-field term is what drives both the effective mass (Section C) and zero sound (Section E).

这个分子场项是有效质量（C 节）与零声（E 节）二者的驱动来源。

**Step 3 — Spin decomposition.** Rotational invariance in spin space allows only a scalar and a $\boldsymbol{\sigma}\cdot\boldsymbol{\sigma'}$ term:

**第 3 步 — 自旋分解。** 自旋空间的转动不变性只允许一个标量项与一个 $\boldsymbol{\sigma}\cdot\boldsymbol{\sigma'}$ 项：

$$ f_{k\sigma,k'\sigma'} = f^s_{kk'} + f^a_{kk'}\, \boldsymbol{\sigma}\cdot\boldsymbol{\sigma'}. $$

The symmetric part $f^s$ acts in the density (charge) channel; the antisymmetric part $f^a$ acts in the spin channel.

对称部分 $f^s$ 作用于密度（电荷）通道；反对称部分 $f^a$ 作用于自旋通道。

**Step 4 — Restrict to the Fermi surface and expand.** Since only $|k| \approx |k'| \approx k_F$ matters, $f^{s,a}$ depends only on the angle $\theta$ between $\boldsymbol{k}$ and $\boldsymbol{k'}$. Expand in Legendre polynomials:

**第 4 步 — 限制到费米面并展开。** 由于只有 $|k| \approx |k'| \approx k_F$ 重要，$f^{s,a}$ 只依赖于 $\boldsymbol{k}$ 与 $\boldsymbol{k'}$ 的夹角 $\theta$。用勒让德多项式展开：

$$ f^{s,a}(\theta) = \sum_l f_l^{s,a} P_l(\cos\theta). $$

**Step 5 — Make dimensionless.** Multiply by the density of states at the Fermi level $N(0)$ (Module 4.1; $N(0) \propto m k_F/\pi^2\hbar^2$ in 3D) to form the **Landau parameters**:

**第 5 步 — 无量纲化。** 乘以费米能级处的态密度 $N(0)$（模块 4.1；三维中 $N(0) \propto m k_F/\pi^2\hbar^2$）以构成**朗道参数**：

$$ F_l^{s,a} = N(0) f_l^{s,a}. $$

These pure numbers, of which only $F_0^s$, $F_1^s$, $F_0^a$ are needed for the leading thermodynamics, parametrize the entire low-energy physics. $\blacksquare$

这些纯数（领头阶热力学只需 $F_0^s$、$F_1^s$、$F_0^a$）参数化了整个低能物理。$\blacksquare$

---

## C. Effective Mass from Galilean Invariance: $m^*/m = 1 + F_1^s/3$ · 伽利略不变性给出有效质量：$m^*/m = 1 + F_1^s/3$

**Claim.** Galilean invariance forces the quasiparticle effective mass to satisfy $m^*/m = 1 + F_1^s/3$.

**命题。** 伽利略不变性迫使准粒子有效质量满足 $m^*/m = 1 + F_1^s/3$。

**Step 1 — Two expressions for the momentum current.** In a Galilean-invariant system the momentum density equals the mass-current density, because the bare mass $m$ is the same operator for both. The total momentum carried when the distribution is shifted must therefore equal $m$ times the particle current. The quasiparticle, however, carries current through its **group velocity** $\nabla_k \varepsilon_k$, *plus* a backflow current induced in all the other quasiparticles through the $f$-function. Equating "bare momentum" with "group velocity + backflow" is the content of the constraint.

**第 1 步 — 动量流的两个表达式。** 在伽利略不变系统中，动量密度等于质量流密度，因为裸质量 $m$ 对二者是同一算符。因此分布平移时携带的总动量必须等于 $m$ 乘以粒子流。然而准粒子通过其**群速度** $\nabla_k \varepsilon_k$ 携带电流，*外加*通过 $f$ 函数在所有其他准粒子中诱导的回流电流。将"裸动量"与"群速度 + 回流"相等即为约束的内容。

**Step 2 — Bare momentum = current of dressed energies.** The exact (bare) velocity of a state $\boldsymbol{k}$ is $\boldsymbol{k}/m$ (mass $m$, $\hbar = 1$). The quasiparticle velocity is the gradient of the *dressed* energy, $\nabla_k \varepsilon_k$. Using $\varepsilon_k = \varepsilon_k^0 + (1/V) \sum_{k'} f_{kk'} \delta n_{k'}$ and taking the gradient,

**第 2 步 — 裸动量 = 穿衣能量之流。** 状态 $\boldsymbol{k}$ 的精确（裸）速度为 $\boldsymbol{k}/m$（质量 $m$，$\hbar = 1$）。准粒子速度是*穿衣*能量的梯度 $\nabla_k \varepsilon_k$。利用 $\varepsilon_k = \varepsilon_k^0 + (1/V) \sum_{k'} f_{kk'} \delta n_{k'}$ 并取梯度，

$$ \boldsymbol{k}/m = \nabla_k \varepsilon_k^0 + \frac{1}{V} \sum_{k'} f_{kk'} \nabla_{k'} n_{k'}^0. $$

The first term is the quasiparticle group velocity with $\boldsymbol{k}/m^* = \nabla_k \varepsilon_k^0$ at the Fermi surface; the second is the backflow, where $\nabla_{k'} n_{k'}^0 = -\boldsymbol{\hat v}_{k'} \delta(\xi_{k'})$ is sharply peaked on the Fermi surface (the ground-state occupation is a step, so its gradient is a $\delta$-function normal to the surface).

第一项是准粒子群速度，费米面上 $\boldsymbol{k}/m^* = \nabla_k \varepsilon_k^0$；第二项是回流，其中 $\nabla_{k'} n_{k'}^0 = -\boldsymbol{\hat v}_{k'} \delta(\xi_{k'})$ 在费米面上尖锐峰化（基态占据是台阶函数，故其梯度是法向 $\delta$ 函数）。

**Step 3 — Evaluate on the Fermi surface.** Take the component of the equation along $\boldsymbol{\hat k}$ at $|k| = k_F$. The group-velocity term has magnitude $|\nabla_k \varepsilon_k^0| = k_F/m^*$. In the backflow term the $\delta$-function collapses the $k'$ sum onto the Fermi surface, $(1/V) \sum_{k'} \to N(0) \int (d\Omega'/4\pi)$, and the backflow velocity has magnitude $v_F^* = k_F/m^*$; projecting it onto $\boldsymbol{\hat k}$ supplies a factor $\cos\theta = \boldsymbol{\hat k}\cdot\boldsymbol{\hat k'}$. Only the spin-symmetric part $f^s$ survives the spin sum, so the $\boldsymbol{\hat k}$-component reads

**第 3 步 — 在费米面上求值。** 在 $|k| = k_F$ 处取方程沿 $\boldsymbol{\hat k}$ 的分量。群速度项大小为 $|\nabla_k \varepsilon_k^0| = k_F/m^*$。回流项中 $\delta$ 函数将 $k'$ 求和坍缩到费米面上，$(1/V) \sum_{k'} \to N(0) \int (d\Omega'/4\pi)$，且回流速度大小为 $v_F^* = k_F/m^*$；将其投影到 $\boldsymbol{\hat k}$ 给出因子 $\cos\theta = \boldsymbol{\hat k}\cdot\boldsymbol{\hat k'}$。只有自旋对称部分 $f^s$ 在自旋求和中存活，故 $\boldsymbol{\hat k}$ 分量为

$$ k_F/m = k_F/m^* + N(0) \int \frac{d\Omega'}{4\pi}\, f^s(\theta) \cos\theta \cdot (k_F/m^*). $$

**Step 4 — Legendre projection picks out $l = 1$.** The angular integral of $f^s(\theta)$ weighted by $\cos\theta = P_1(\cos\theta)$ selects the $l = 1$ component by orthogonality of Legendre polynomials, $\int (d\Omega'/4\pi) P_l P_1 = \delta_{l1}/3$:

**第 4 步 — 勒让德投影挑出 $l = 1$。** $f^s(\theta)$ 以 $\cos\theta = P_1(\cos\theta)$ 加权的角积分，凭勒让德多项式正交性 $\int (d\Omega'/4\pi) P_l P_1 = \delta_{l1}/3$ 挑出 $l = 1$ 分量：

$$ N(0) \int \frac{d\Omega'}{4\pi}\, f^s(\theta) \cos\theta = N(0) f_1^s / 3 = F_1^s/3. $$

**Step 5 — Assemble.** Substituting the Step-4 result into the Step-3 equation and dividing through by $k_F/m^*$:

**第 5 步 — 组合。** 将第 4 步结果代入第 3 步方程并整体除以 $k_F/m^*$：

$$ k_F/m = (k_F/m^*)(1 + F_1^s/3) \implies (k_F/m)\cdot(m^*/k_F) = 1 + F_1^s/3, $$

so the effective mass is fixed entirely by the $l = 1$ symmetric Landau parameter:

故有效质量完全由 $l = 1$ 对称朗道参数决定：

$$ m^*/m = 1 + F_1^s/3. $$

Equivalently, the effective-mass enhancement is the $l = 1$ forward-scattering amplitude on the Fermi surface; strong forward interactions (large $F_1^s$) make the quasiparticle heavy. $\blacksquare$

等价地，有效质量增强即费米面上 $l = 1$ 前向散射振幅；强前向相互作用（大 $F_1^s$）使准粒子变重。$\blacksquare$

---

## D. Thermodynamic Renormalizations · 热力学重整化

**Claim.** $C_V = (m^*/m) C_V^{\text{free}}$; the compressibility $\kappa \propto N^*(0)/(1 + F_0^s)$; the spin susceptibility $\chi \propto N^*(0)/(1 + F_0^a)$, with $N^*(0) = (m^*/m) N(0)$. The vanishing of $1 + F_0^a$ marks the ferromagnetic instability.

**命题。** $C_V = (m^*/m) C_V^{\text{free}}$；压缩率 $\kappa \propto N^*(0)/(1 + F_0^s)$；自旋磁化率 $\chi \propto N^*(0)/(1 + F_0^a)$，其中 $N^*(0) = (m^*/m) N(0)$。$1 + F_0^a$ 消失标志铁磁不稳定性。

**Step 1 — Renormalized density of states.** In 3D the free DOS at $E_F$ is $N(0) = m k_F/(\pi^2 \hbar^2) \propto m$. Replacing $m \to m^*$ gives the quasiparticle DOS

**第 1 步 — 重整化态密度。** 三维中 $E_F$ 处自由态密度为 $N(0) = m k_F/(\pi^2 \hbar^2) \propto m$。将 $m \to m^*$ 给出准粒子态密度

$$ N^*(0) = (m^*/m) N(0). $$

**Step 2 — Specific heat.** The entropy of the quasiparticle gas is the *same combinatorial functional* of the occupations $n_k$ as for free fermions (quasiparticles are still fermions with one state per $\boldsymbol{k}$, $\sigma$). The Sommerfeld derivation (Module 4.1) therefore carries over verbatim with the single change $N(0) \to N^*(0)$:

**第 2 步 — 比热。** 准粒子气体的熵是占据数 $n_k$ 的*相同组合泛函*（准粒子仍是费米子，每个 $(\boldsymbol{k}, \sigma)$ 一个态）。因此索末菲推导（模块 4.1）原样保留，只需将 $N(0) \to N^*(0)$：

$$ C_V = \frac{\pi^2}{3} k_B^2 T\, N^*(0) = (m^*/m) \cdot \frac{\pi^2}{3} k_B^2 T\, N(0), $$

$$ C_V = (m^*/m) C_V^{\text{free}}, \qquad \gamma = (m^*/m) \gamma_{\text{free}}. $$

The $f$-interaction does **not** appear: at fixed $T$ the leading entropy depends only on the number of thermally accessible states, i.e. on $N^*(0)$. This is why a heavy effective mass directly inflates the measured $\gamma$ — the experimental signature of heavy fermions.

$f$ 相互作用**不**出现：固定 $T$ 下领头熵只依赖于热可及态数目，即 $N^*(0)$。这就是为何重的有效质量直接放大测得的 $\gamma$——重费米子的实验标志。

**Step 3 — Susceptibility setup.** Apply a magnetic field $H$. Two effects shift the up/down energies: (i) the bare Zeeman coupling $-(1/2) g \mu_B \sigma H$, and (ii) the molecular field from the spin-antisymmetric $f^a$, because polarizing the liquid changes $\delta n_\uparrow - \delta n_\downarrow$ and hence feeds back through $f^a$. The dressed energy of a quasiparticle of spin $\sigma$ is

**第 3 步 — 磁化率设置。** 加磁场 $H$。两个效应移动上/下自旋能量：(i) 裸塞曼耦合 $-(1/2) g \mu_B \sigma H$，(ii) 来自自旋反对称 $f^a$ 的分子场，因为极化液体改变 $\delta n_\uparrow - \delta n_\downarrow$ 从而经 $f^a$ 反馈。自旋 $\sigma$ 准粒子的穿衣能量为

$$ \delta\varepsilon_{k\sigma} = -\frac{1}{2} g \mu_B \sigma H + \frac{1}{V} \sum_{k'\sigma'} f^a_{kk'} \sigma\sigma' \delta n_{k'\sigma'}. $$

**Step 4 — Self-consistent polarization.** Let the magnetization correspond to a population imbalance characterized by an effective field. Only the $l = 0$ (isotropic) component of $f^a$ contributes to a uniform magnetization, giving $F_0^a$. The free-fermion (Pauli) response $\chi_0 = \mu_B^2 N^*(0)$ is reduced by the feedback factor: solving the self-consistency $\delta n \propto \chi_0 (H_\text{eff})$, with $H_\text{eff} = H - (F_0^a/N(0)) \delta(\text{magnetization})/\mu_B$, yields

**第 4 步 — 自洽极化。** 令磁化对应于由有效场刻画的布居失衡。只有 $f^a$ 的 $l = 0$（各向同性）分量贡献于均匀磁化，给出 $F_0^a$。自由费米子（泡利）响应 $\chi_0 = \mu_B^2 N^*(0)$ 被反馈因子削减：求解自洽 $\delta n \propto \chi_0 (H_\text{eff})$，其中 $H_\text{eff} = H - (F_0^a/N(0)) \delta(\text{磁化})/\mu_B$，得到

$$ \chi = \mu_B^2 N^*(0) / (1 + F_0^a). $$

The denominator is the Fermi-liquid Stoner factor. As $F_0^a \to -1^+$ the susceptibility diverges: an arbitrarily small field produces a finite polarization — the **ferromagnetic (Stoner) instability**.

分母是费米液体的斯通纳因子。当 $F_0^a \to -1^+$ 时磁化率发散：任意小的场产生有限极化——**铁磁（斯通纳）不稳定性**。

**Step 5 — Compressibility (density channel).** The identical argument in the spin-*symmetric*, $l = 0$ channel applies to a uniform density change. The restoring molecular field comes from $f^s_0 \to F_0^s$, screening the response:

**第 5 步 — 压缩率（密度通道）。** 在自旋*对称*、$l = 0$ 通道中的相同论证适用于均匀密度变化。恢复分子场来自 $f^s_0 \to F_0^s$，屏蔽响应：

$$ \kappa \propto N^*(0) / (1 + F_0^s). $$

(The full Galilean-invariant form is $\kappa = [N^*(0)/n^2]/(1 + F_0^s)$; here $n$ is the density.) $F_0^s \to -1^+$ would mark a density (compressibility) instability. $\blacksquare$

（完整伽利略不变形式为 $\kappa = [N^*(0)/n^2]/(1 + F_0^s)$；此处 $n$ 为密度。）$F_0^s \to -1^+$ 将标志密度（压缩率）不稳定性。$\blacksquare$

---

## E. Zero Sound from the Landau Kinetic Equation · 朗道动理学方程给出零声

**Claim.** In the collisionless regime $\omega\tau \gg 1$ the linearized Landau transport equation supports an undamped collective mode (zero sound) with phase velocity $s = \omega/(q v_F) > 1$ obeying (keeping only $F_0^s$): $(s/2) \ln[(s+1)/(s-1)] - 1 = 1/F_0^s$. This is physically distinct from collisional first sound ($\omega\tau \ll 1$).

**命题。** 在无碰撞区 $\omega\tau \gg 1$ 中，线性化朗道输运方程支持一个无阻尼集体模式（零声），其相速度 $s = \omega/(q v_F) > 1$ 满足（只保留 $F_0^s$）：$(s/2) \ln[(s+1)/(s-1)] - 1 = 1/F_0^s$。这与碰撞性的第一声（$\omega\tau \ll 1$）在物理上不同。

**Step 1 — Linearized kinetic equation.** The quasiparticle distribution $\delta n_k(\boldsymbol{r},t)$ obeys a Boltzmann equation. The dressed energy $\varepsilon_k$ includes the molecular field, so the driving force on each quasiparticle has a self-consistent piece. Linearizing about equilibrium and dropping the collision term (collisionless limit $\omega\tau \gg 1$):

**第 1 步 — 线性化动理学方程。** 准粒子分布 $\delta n_k(\boldsymbol{r},t)$ 服从玻尔兹曼方程。穿衣能量 $\varepsilon_k$ 含分子场，故每个准粒子受的驱动力有一个自洽部分。在平衡附近线性化并丢弃碰撞项（无碰撞极限 $\omega\tau \gg 1$）：

$$ \frac{\partial\delta n_k}{\partial t} + \boldsymbol{v}_k \cdot \nabla_r \delta n_k - \boldsymbol{v}_k \cdot \nabla_r \Big(\frac{\partial n^0}{\partial\varepsilon_k}\Big)\cdot\frac{1}{V}\sum_{k'} f_{kk'} \delta n_{k'} = 0. $$

**Step 2 — Plane-wave ansatz.** Seek a mode $\delta n_k \propto e^{i(\boldsymbol{q}\cdot\boldsymbol{r} - \omega t)}$. Write $\delta n_k = -(\partial n^0/\partial\varepsilon)\, \nu(\theta)$, where $\nu(\theta)$ is the deformation of the Fermi surface as a function of the angle $\theta$ between $\boldsymbol{v}_k$ ($\parallel \boldsymbol{\hat k}$) and $\boldsymbol{q}$. With $\boldsymbol{v}_k\cdot\boldsymbol{q} = q v_F \cos\theta$ and $s \equiv \omega/(q v_F)$:

**第 2 步 — 平面波拟设。** 寻找模式 $\delta n_k \propto e^{i(\boldsymbol{q}\cdot\boldsymbol{r} - \omega t)}$。写 $\delta n_k = -(\partial n^0/\partial\varepsilon)\, \nu(\theta)$，其中 $\nu(\theta)$ 是费米面的形变，为 $\boldsymbol{v}_k$（$\parallel \boldsymbol{\hat k}$）与 $\boldsymbol{q}$ 夹角 $\theta$ 的函数。以 $\boldsymbol{v}_k\cdot\boldsymbol{q} = q v_F \cos\theta$ 与 $s \equiv \omega/(q v_F)$：

$$ (s - \cos\theta)\, \nu(\theta) = \cos\theta \cdot \int \frac{d\Omega'}{4\pi}\, F^s(\theta,\theta')\, \nu(\theta'). $$

Here $F^s = N(0) f^s$ is the dimensionless symmetric interaction (spin channel decouples for zero sound).

此处 $F^s = N(0) f^s$ 是无量纲对称相互作用（零声中自旋通道解耦）。

**Step 3 — Keep only $F_0^s$.** Retain the s-wave interaction $F^s(\theta,\theta') = F_0^s$ (a constant). Then the right side is $\cos\theta \cdot F_0^s \cdot \langle\nu\rangle$, where $\langle\nu\rangle \equiv \int (d\Omega'/4\pi) \nu(\theta')$ is an angular average. Solve for $\nu$:

**第 3 步 — 只保留 $F_0^s$。** 保留 s 波相互作用 $F^s(\theta,\theta') = F_0^s$（常数）。则右端为 $\cos\theta \cdot F_0^s \cdot \langle\nu\rangle$，其中 $\langle\nu\rangle \equiv \int (d\Omega'/4\pi) \nu(\theta')$ 是角平均。解出 $\nu$：

$$ \nu(\theta) = F_0^s \langle\nu\rangle \cdot \frac{\cos\theta}{s - \cos\theta}. $$

**Step 4 — Self-consistency (dispersion relation).** Insert $\nu(\theta)$ back into the definition of $\langle\nu\rangle$ and cancel the common factor $\langle\nu\rangle$ (nonzero for a genuine mode):

**第 4 步 — 自洽（色散关系）。** 将 $\nu(\theta)$ 代回 $\langle\nu\rangle$ 的定义并消去公因子 $\langle\nu\rangle$（真实模式时非零）：

$$ 1 = F_0^s \int_{-1}^1 \frac{dx}{2}\, \frac{x}{s - x}, \qquad x \equiv \cos\theta. $$

The integral is $\int_{-1}^1 (dx/2)\, x/(s - x) = (s/2) \ln[(s+1)/(s-1)] - 1$. Hence

该积分为 $\int_{-1}^1 (dx/2)\, x/(s - x) = (s/2) \ln[(s+1)/(s-1)] - 1$。因此

$$ (s/2) \ln[(s+1)/(s-1)] - 1 = 1/F_0^s. $$

**Step 5 — Solutions and physical interpretation.** For $s > 1$ the logarithm is real, so the mode is **undamped** — it lies outside the particle–hole continuum (which occupies $s < 1$, where $\boldsymbol{v}_k\cdot\boldsymbol{q}$ can match $\omega$ and Landau-damp the mode). The left side increases from $0$ to $\infty$ as $s$ decreases from $\infty$ to $1$, so a real root $s_0 > 1$ exists for any $F_0^s > 0$: **zero sound**, a coherent Fermi-surface oscillation propagating slightly faster than $v_F$, sustained by the molecular field rather than by collisions.

**第 5 步 — 解与物理诠释。** 当 $s > 1$ 时对数为实，故模式**无阻尼**——它位于粒子–空穴连续谱之外（连续谱占 $s < 1$，那里 $\boldsymbol{v}_k\cdot\boldsymbol{q}$ 可匹配 $\omega$ 而朗道阻尼该模式）。当 $s$ 从 $\infty$ 减到 $1$ 时左端从 $0$ 增到 $\infty$，故对任意 $F_0^s > 0$ 存在实根 $s_0 > 1$：**零声**，一个比 $v_F$ 略快传播的相干费米面振荡，由分子场而非碰撞维持。

**Step 6 — Contrast with first sound.** First sound is the $\omega\tau \ll 1$ hydrodynamic limit: frequent collisions enforce local equilibrium, and ordinary sound propagates at $c_1 = v_F \sqrt{(1 + F_0^s)(1 + F_1^s/3)/3}$ (the compressibility and effective-mass factors of Section D). Zero sound ($\omega\tau \gg 1$) and first sound ($\omega\tau \ll 1$) are *different modes with different speeds*; observing the crossover as temperature lowers $\omega\tau$ through $1$ (since $1/\tau \propto T^2$) is the classic experimental confirmation of Landau theory in liquid ${}^3\text{He}$. $\blacksquare$

**第 6 步 — 与第一声对比。** 第一声是 $\omega\tau \ll 1$ 的流体力学极限：频繁碰撞强制局域平衡，普通声以 $c_1 = v_F \sqrt{(1 + F_0^s)(1 + F_1^s/3)/3}$ 传播（D 节的压缩率与有效质量因子）。零声（$\omega\tau \gg 1$）与第一声（$\omega\tau \ll 1$）是*速度不同的不同模式*；当温度降低使 $\omega\tau$ 越过 $1$ 时（因 $1/\tau \propto T^2$）观测到的交叉，是朗道理论在液态 ${}^3\text{He}$ 中的经典实验确认。$\blacksquare$

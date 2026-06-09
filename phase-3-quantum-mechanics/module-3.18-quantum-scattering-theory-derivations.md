# Derivations — Module 3.18: Quantum Scattering Theory
# 推导 — 模块 3.18：量子散射理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.18](./module-3.18-quantum-scattering-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.18](./module-3.18-quantum-scattering-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Scattering Amplitude and the Differential Cross Section · 散射振幅与微分截面

**Claim.** A stationary scattering state with asymptotic form $\psi \to e^{ikz} + f(\theta)\, e^{ikr}/r$ produces a differential cross section $d\sigma/d\Omega = |f(\theta)|^2$, obtained as the ratio of outgoing scattered flux to incident flux.

**命题。** 渐近形式为 $\psi \to e^{ikz} + f(\theta)\, e^{ikr}/r$ 的定态散射态给出微分截面 $d\sigma/d\Omega = |f(\theta)|^2$，它是出射散射通量与入射通量之比。

**Step 1 — The probability current.** For a wavefunction $\psi$ the quantum probability current is

**第 1 步 — 概率流。** 对波函数 $\psi$，量子概率流为

$$ \mathbf{j} = \frac{\hbar}{m}\, \mathrm{Im}(\psi^* \nabla\psi) = \frac{\hbar}{2mi}(\psi^* \nabla\psi - \psi \nabla\psi^*). $$

The differential cross section is defined operationally as

微分截面的操作性定义为

$$ \frac{d\sigma}{d\Omega} = \frac{\text{(number scattered into } d\Omega \text{ per unit time)}}{\text{(incident flux)}} = \frac{j_\text{scatt}\cdot r^2}{j_\text{inc}}, $$

since the number entering detector area $r^2\, d\Omega$ per unit time is the radial scattered flux times that area.

因为单位时间进入探测器面元 $r^2\, d\Omega$ 的粒子数等于径向散射通量乘以该面积。

**Step 2 — Incident flux.** The incident wave is $\psi_\text{inc} = e^{ikz}$, a momentum eigenstate with $\nabla\psi_\text{inc} = ik\, \hat{z}\, \psi_\text{inc}$. Then

**第 2 步 — 入射通量。** 入射波为 $\psi_\text{inc} = e^{ikz}$，是动量本征态，$\nabla\psi_\text{inc} = ik\, \hat{z}\, \psi_\text{inc}$。于是

$$ \mathbf{j}_\text{inc} = \frac{\hbar}{m}\, \mathrm{Im}(e^{-ikz}\, ik\, \hat{z}\, e^{ikz}) = \frac{\hbar}{m}\, \mathrm{Im}(ik\, \hat{z}) = \frac{\hbar k}{m}\, \hat{z}, $$

so the incident flux magnitude is $j_\text{inc} = \hbar k/m$ (probability per unit area per unit time, with $|\psi_\text{inc}|^2 = 1$).

故入射通量大小为 $j_\text{inc} = \hbar k/m$（单位面积单位时间的概率，因 $|\psi_\text{inc}|^2 = 1$）。

**Step 3 — Scattered flux.** The scattered wave is $\psi_\text{sc} = f(\theta)\, e^{ikr}/r$. Its dominant component at large $r$ is radial; using $\partial/\partial r$ acting on $e^{ikr}/r$ and keeping only the leading $1/r$ term (the $1/r^2$ piece of the derivative is subdominant),

**第 3 步 — 散射通量。** 散射波为 $\psi_\text{sc} = f(\theta)\, e^{ikr}/r$。大 $r$ 处其主导分量为径向；用 $\partial/\partial r$ 作用于 $e^{ikr}/r$ 并只保留首阶 $1/r$ 项（导数中的 $1/r^2$ 部分为次主导），

$$ \frac{\partial\psi_\text{sc}}{\partial r} = f(\theta)\Big(ik\, \frac{e^{ikr}}{r} - \frac{e^{ikr}}{r^2}\Big) \to ik\, f(\theta)\, \frac{e^{ikr}}{r}. $$

The radial current is

径向流为

$$ j_\text{scatt} = \frac{\hbar}{m}\, \mathrm{Im}\Big(\psi_\text{sc}^* \frac{\partial\psi_\text{sc}}{\partial r}\Big) = \frac{\hbar}{m}\, \mathrm{Im}\Big(\frac{|f|^2}{r^2}\cdot ik\Big) = \frac{\hbar k}{m}\, \frac{|f(\theta)|^2}{r^2}. $$

**Step 4 — Take the ratio.** Substituting into the definition,

**第 4 步 — 取比值。** 代入定义，

$$ \frac{d\sigma}{d\Omega} = \frac{j_\text{scatt}\cdot r^2}{j_\text{inc}} = \frac{(\hbar k/m)|f|^2/r^2 \cdot r^2}{\hbar k/m} = |f(\theta)|^2. $$

The factors $\hbar k/m$ and $r^2$ cancel exactly. The interference cross term between incident and scattered waves contributes only in the exact forward direction and integrates to the optical theorem (Derivation C), not to $d\sigma/d\Omega$ at finite $\theta$. Hence

$\hbar k/m$ 与 $r^2$ 因子精确相消。入射波与散射波的干涉交叉项仅在严格前向有贡献，积分后给出光学定理（推导 C），而非有限 $\theta$ 处的 $d\sigma/d\Omega$。故

$$ \frac{d\sigma}{d\Omega} = |f(\theta)|^2, \qquad \sigma = \int |f(\theta)|^2\, d\Omega. \qquad \blacksquare $$

---

## B. Partial-Wave Expansion, Phase Shifts, and the Cross Section · 分波展开、相移与截面

**Claim.** For a central potential the scattering amplitude is $f(\theta) = (1/k) \sum_{\ell=0}^\infty (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell(\cos\theta)$, and the total cross section is $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$.

**命题。** 对中心势，散射振幅为 $f(\theta) = (1/k) \sum_{\ell=0}^\infty (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell(\cos\theta)$，总截面为 $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$。

**Step 1 — Separation and the radial equation.** A central potential $V(r)$ conserves angular momentum, so $\psi = \sum_\ell R_\ell(r)\, P_\ell(\cos\theta)$ (azimuthal symmetry about the beam means only $m = 0$ appears, and $Y_\ell^0 \propto P_\ell$). Writing $u_\ell(r) = r R_\ell(r)$, the radial equation is

**第 1 步 — 分离变量与径向方程。** 中心势 $V(r)$ 守恒角动量，故 $\psi = \sum_\ell R_\ell(r)\, P_\ell(\cos\theta)$（关于束流的方位对称性意味着只出现 $m = 0$，且 $Y_\ell^0 \propto P_\ell$）。令 $u_\ell(r) = r R_\ell(r)$，径向方程为

$$ u_\ell'' + \Big[\, k^2 - \frac{\ell(\ell+1)}{r^2} - \frac{2mV}{\hbar^2} \,\Big] u_\ell = 0. $$

Outside the range of $V$ the free solution is a combination of spherical Bessel functions; its asymptotic form defines the phase shift $\delta_\ell$:

在 $V$ 射程外，自由解是球贝塞尔函数的组合，其渐近形式定义相移 $\delta_\ell$：

$$ u_\ell(r) \to \sin(kr - \ell\pi/2 + \delta_\ell), \quad\text{as } r \to \infty. $$

**Step 2 — Asymptotics of the plane wave.** The free plane wave has the Rayleigh expansion $e^{ikz} = \sum_\ell (2\ell+1)\, i^\ell\, j_\ell(kr)\, P_\ell(\cos\theta)$, and the spherical Bessel function has the large-$r$ form $j_\ell(kr) \to \sin(kr - \ell\pi/2)/(kr)$. Therefore

**第 2 步 — 平面波渐近。** 自由平面波有瑞利展开 $e^{ikz} = \sum_\ell (2\ell+1)\, i^\ell\, j_\ell(kr)\, P_\ell(\cos\theta)$，球贝塞尔函数的大 $r$ 形式为 $j_\ell(kr) \to \sin(kr - \ell\pi/2)/(kr)$。因此

$$ e^{ikz} \to \sum_\ell (2\ell+1)\, i^\ell\, [\sin(kr - \ell\pi/2)/(kr)]\, P_\ell(\cos\theta). $$

Writing $\sin x = (e^{ix} - e^{-ix})/2i$ and using $i^\ell = e^{i\ell\pi/2}$ so that $i^\ell e^{\mp i\ell\pi/2} = 1$ or $e^{-i\ell\pi}$, the plane wave splits into incoming ($e^{-ikr}$) and outgoing ($e^{+ikr}$) spherical waves:

将 $\sin x = (e^{ix} - e^{-ix})/2i$，并用 $i^\ell = e^{i\ell\pi/2}$（使 $i^\ell e^{\mp i\ell\pi/2}$ 为 $1$ 或 $e^{-i\ell\pi}$），平面波分裂为入射（$e^{-ikr}$）与出射（$e^{+ikr}$）球面波：

$$ e^{ikz} \to \sum_\ell \frac{2\ell+1}{2ikr}\, [e^{ikr} - (-1)^\ell e^{-ikr}]\, P_\ell. $$

**Step 3 — Asymptotics of the full state.** The complete scattering state is $\psi = \sum_\ell A_\ell\, [u_\ell(r)/r]\, P_\ell$. With $u_\ell \to \sin(kr - \ell\pi/2 + \delta_\ell)$ and absorbing the phase, its outgoing/incoming decomposition is

**第 3 步 — 完整态的渐近。** 完整散射态为 $\psi = \sum_\ell A_\ell\, [u_\ell(r)/r]\, P_\ell$。以 $u_\ell \to \sin(kr - \ell\pi/2 + \delta_\ell)$ 并吸收相位，其出射/入射分解为

$$ \psi \to \sum_\ell \frac{A_\ell}{2ikr}\, [e^{i\delta_\ell} e^{ikr} - (-1)^\ell e^{-i\delta_\ell} e^{-ikr}]\, P_\ell. $$

**Step 4 — Match incoming waves.** Physically the scatterer only modifies the outgoing wave; the incoming wave must coincide with that of the plane wave alone (nothing produces extra inward flux). Equating the coefficients of the incoming $e^{-ikr}/r$ term in $\psi$ and in $e^{ikz}$,

**第 4 步 — 匹配入射波。** 物理上散射体只修改出射波；入射波必须与单独平面波的入射波一致（没有东西产生额外的向内通量）。令 $\psi$ 与 $e^{ikz}$ 中入射项 $e^{-ikr}/r$ 的系数相等，

$$ A_\ell\, (-1)^\ell e^{-i\delta_\ell} = (2\ell+1)(-1)^\ell \quad\implies\quad A_\ell = (2\ell+1)\, e^{i\delta_\ell}. $$

**Step 5 — Extract $f(\theta)$.** The scattered amplitude is the difference between the outgoing parts of $\psi$ and $e^{ikz}$, since $\psi = e^{ikz} + f(\theta)e^{ikr}/r$. The outgoing coefficient of $\psi$ is $A_\ell e^{i\delta_\ell}/(2ik) = (2\ell+1)e^{2i\delta_\ell}/(2ik)$; that of $e^{ikz}$ is $(2\ell+1)/(2ik)$. Their difference gives $f(\theta)\, e^{ikr}/r = \sum_\ell [(2\ell+1)/(2ik)](e^{2i\delta_\ell} - 1)\, P_\ell \cdot e^{ikr}/r$, hence

**第 5 步 — 提取 $f(\theta)$。** 由 $\psi = e^{ikz} + f(\theta)e^{ikr}/r$，散射振幅是 $\psi$ 与 $e^{ikz}$ 出射部分之差。$\psi$ 的出射系数为 $A_\ell e^{i\delta_\ell}/(2ik) = (2\ell+1)e^{2i\delta_\ell}/(2ik)$，$e^{ikz}$ 的为 $(2\ell+1)/(2ik)$。两者之差给出 $f(\theta)\, e^{ikr}/r = \sum_\ell [(2\ell+1)/(2ik)](e^{2i\delta_\ell} - 1)\, P_\ell \cdot e^{ikr}/r$，故

$$ f(\theta) = \frac{1}{2ik} \sum_\ell (2\ell+1)(e^{2i\delta_\ell} - 1)\, P_\ell(\cos\theta). $$

Using $e^{2i\delta_\ell} - 1 = 2i\, e^{i\delta_\ell} \sin\delta_\ell$ (since $e^{2i\delta} - 1 = e^{i\delta}(e^{i\delta} - e^{-i\delta}) = e^{i\delta}\cdot 2i \sin\delta$),

利用 $e^{2i\delta_\ell} - 1 = 2i\, e^{i\delta_\ell} \sin\delta_\ell$（因 $e^{2i\delta} - 1 = e^{i\delta}(e^{i\delta} - e^{-i\delta}) = e^{i\delta}\cdot 2i \sin\delta$），

$$ f(\theta) = \frac{1}{k} \sum_{\ell=0}^\infty (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell(\cos\theta). $$

**Step 6 — Total cross section.** Integrate $|f|^2$ over solid angle. With $f = (1/k) \sum_\ell (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell$,

**第 6 步 — 总截面。** 对 $|f|^2$ 作立体角积分。以 $f = (1/k) \sum_\ell (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell\, P_\ell$，

$$ \sigma = \int|f|^2\, d\Omega = \frac{1}{k^2} \sum_\ell \sum_{\ell'} (2\ell+1)(2\ell'+1)\, e^{i(\delta_\ell-\delta_{\ell'})} \sin\delta_\ell \sin\delta_{\ell'} \int P_\ell P_{\ell'}\, d\Omega. $$

The Legendre orthogonality $\int P_\ell P_{\ell'}\, d\Omega = [4\pi/(2\ell+1)]\, \delta_{\ell\ell'}$ kills the cross terms ($\ell = \ell'$ forces $e^{i\cdot 0} = 1$):

勒让德正交性 $\int P_\ell P_{\ell'}\, d\Omega = [4\pi/(2\ell+1)]\, \delta_{\ell\ell'}$ 消去交叉项（$\ell = \ell'$ 迫使 $e^{i\cdot 0} = 1$）：

$$ \sigma = \frac{1}{k^2} \sum_\ell (2\ell+1)^2 \sin^2\delta_\ell \cdot \frac{4\pi}{2\ell+1} = \frac{4\pi}{k^2} \sum_\ell (2\ell+1) \sin^2\delta_\ell. \qquad \blacksquare $$

---

## C. The Optical Theorem · 光学定理

**Claim.** The total cross section is related to the imaginary part of the forward scattering amplitude by $\sigma_\text{tot} = (4\pi/k)\, \mathrm{Im}\, f(0)$.

**命题。** 总截面与前向散射振幅的虚部相关：$\sigma_\text{tot} = (4\pi/k)\, \mathrm{Im}\, f(0)$。

**Step 1 — Forward amplitude.** Evaluate $f(\theta)$ at $\theta = 0$. Every Legendre polynomial satisfies $P_\ell(1) = 1$, so

**第 1 步 — 前向振幅。** 在 $\theta = 0$ 处计算 $f(\theta)$。每个勒让德多项式满足 $P_\ell(1) = 1$，故

$$ f(0) = \frac{1}{k} \sum_\ell (2\ell+1)\, e^{i\delta_\ell} \sin\delta_\ell. $$

**Step 2 — Take the imaginary part.** Since $e^{i\delta_\ell} = \cos\delta_\ell + i\sin\delta_\ell$, we have $\mathrm{Im}(e^{i\delta_\ell} \sin\delta_\ell) = \sin\delta_\ell \cdot \sin\delta_\ell = \sin^2\delta_\ell$. Therefore

**第 2 步 — 取虚部。** 由 $e^{i\delta_\ell} = \cos\delta_\ell + i\sin\delta_\ell$，得 $\mathrm{Im}(e^{i\delta_\ell} \sin\delta_\ell) = \sin\delta_\ell \cdot \sin\delta_\ell = \sin^2\delta_\ell$。因此

$$ \mathrm{Im}\, f(0) = \frac{1}{k} \sum_\ell (2\ell+1) \sin^2\delta_\ell. $$

**Step 3 — Compare with $\sigma$.** From Derivation B, $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$. The sum $\sum_\ell (2\ell+1) \sin^2\delta_\ell$ is common to both, so substitute it:

**第 3 步 — 与 $\sigma$ 比较。** 由推导 B，$\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$。求和 $\sum_\ell (2\ell+1) \sin^2\delta_\ell$ 为两者共有，代入之：

$$ \sum_\ell (2\ell+1) \sin^2\delta_\ell = k\cdot \mathrm{Im}\, f(0) \quad\text{and}\quad \sum_\ell (2\ell+1) \sin^2\delta_\ell = \frac{k^2}{4\pi}\, \sigma. $$

Equating the two right-hand sides, $k\, \mathrm{Im}\, f(0) = (k^2/4\pi)\, \sigma$, hence

令两式右端相等，$k\, \mathrm{Im}\, f(0) = (k^2/4\pi)\, \sigma$，故

$$ \sigma_\text{tot} = \frac{4\pi}{k}\, \mathrm{Im}\, f(0). $$

This expresses flux conservation: the imaginary part of the forward amplitude measures the destructive interference that removes probability from the forward beam, which must equal the total flux scattered into all directions. $\blacksquare$

这表达了通量守恒：前向振幅的虚部度量从前向束流中移除概率的相消干涉，它必须等于散射至所有方向的总通量。$\blacksquare$

---

## D. Low-Energy s-Wave Scattering and the Scattering Length · 低能 s 波散射与散射长度

**Claim.** As $k \to 0$ only the $\ell = 0$ wave survives; defining the scattering length by $\delta_0 \to -ka$ gives $f \to -a$ and $\sigma \to 4\pi a^2$, and $a$ is the intercept of the extrapolated zero-energy wavefunction $u_0 \propto (r - a)$.

**命题。** 当 $k \to 0$ 只有 $\ell = 0$ 波存活；以 $\delta_0 \to -ka$ 定义散射长度得 $f \to -a$ 与 $\sigma \to 4\pi a^2$，且 $a$ 是外推零能波函数 $u_0 \propto (r - a)$ 的截距。

**Step 1 — Why only $\ell = 0$ survives.** Outside a potential of range $b$ the centrifugal barrier $\ell(\ell+1)/r^2$ keeps the $\ell \ge 1$ waves out: the low-energy phase shifts obey the threshold law $\delta_\ell \propto (kb)^{2\ell+1}$. Thus for $kb \ll 1$, $\delta_1, \delta_2, \ldots$ vanish faster than $\delta_0$, and the s-wave dominates.

**第 1 步 — 为何只有 $\ell = 0$ 存活。** 在射程为 $b$ 的势外，离心势垒 $\ell(\ell+1)/r^2$ 将 $\ell \ge 1$ 波挡在外面：低能相移服从阈值定律 $\delta_\ell \propto (kb)^{2\ell+1}$。故当 $kb \ll 1$ 时，$\delta_1$、$\delta_2$、$\ldots$ 比 $\delta_0$ 更快趋零，s 波主导。

**Step 2 — Define the scattering length.** For $\ell = 0$ the low-energy phase shift is linear in $k$. Define the scattering length $a$ by

**第 2 步 — 定义散射长度。** 对 $\ell = 0$，低能相移随 $k$ 线性。以下式定义散射长度 $a$：

$$ \delta_0(k) \to -ka, \quad\text{as } k \to 0. $$

**Step 3 — Amplitude and cross section.** Keep only $\ell = 0$ in $f$. Since $P_0 = 1$,

**第 3 步 — 振幅与截面。** 在 $f$ 中只保留 $\ell = 0$。因 $P_0 = 1$，

$$ f \to \frac{1}{k}\, e^{i\delta_0} \sin\delta_0 \to \frac{1}{k} \sin\delta_0 \quad (e^{i\delta_0} \to 1 \text{ as } \delta_0 \to 0). $$

With $\delta_0 = -ka$, $\sin\delta_0 \to \delta_0 = -ka$, so $f \to (1/k)(-ka) = -a$. The cross section is

以 $\delta_0 = -ka$，$\sin\delta_0 \to \delta_0 = -ka$，故 $f \to (1/k)(-ka) = -a$。截面为

$$ \sigma = 4\pi|f|^2 \to 4\pi a^2. $$

The scattering is isotropic ($f$ is angle-independent) and the cross section is four times the geometric disc $\pi a^2$.

散射各向同性（$f$ 与角度无关），截面是几何圆盘 $\pi a^2$ 的四倍。

**Step 4 — Geometric meaning of $a$.** At exactly $E = 0$ the free radial equation outside the potential is $u_0'' = 0$, whose solution is linear:

**第 4 步 — $a$ 的几何意义。** 在 $E = 0$ 处，势外自由径向方程为 $u_0'' = 0$，其解为线性：

$$ u_0(r) \propto (r - a), \quad\text{for } r > b. $$

This is the $k \to 0$ limit of $u_0 \propto \sin(kr + \delta_0)/k \to r + \delta_0/k = r - a$, confirming $a = -\delta_0/k$. The straight line crosses zero at $r = a$: $a$ is the intercept of the extrapolated external wavefunction. A node outside the range ($a > 0$) signals an effectively repulsive interaction or a bound state just below threshold; $a < 0$ signals a weakly attractive (virtual) state. $\blacksquare$

这是 $u_0 \propto \sin(kr + \delta_0)/k \to r + \delta_0/k = r - a$ 的 $k \to 0$ 极限，证实 $a = -\delta_0/k$。该直线在 $r = a$ 处过零：$a$ 是外推外部波函数的截距。节点在射程外（$a > 0$）表示等效排斥相互作用或刚好低于阈值的束缚态；$a < 0$ 表示弱吸引（虚）态。$\blacksquare$

---

## E. Resonances and the Breit–Wigner Formula · 共振与 Breit–Wigner 公式

**Claim.** Near a resonance at energy $E_R$ of width $\Gamma$, the partial cross section is the Breit–Wigner form $\sigma_\ell = (4\pi/k^2)(2\ell+1)(\Gamma/2)^2/[(E - E_R)^2 + (\Gamma/2)^2]$, peaking at the unitarity limit $\sigma_\ell^\text{max} = (4\pi/k^2)(2\ell+1)$.

**命题。** 在能量 $E_R$、宽度 $\Gamma$ 的共振附近，分波截面取 Breit–Wigner 形式 $\sigma_\ell = (4\pi/k^2)(2\ell+1)(\Gamma/2)^2/[(E - E_R)^2 + (\Gamma/2)^2]$，峰值达到幺正极限 $\sigma_\ell^\text{max} = (4\pi/k^2)(2\ell+1)$。

**Step 1 — Partial cross section.** Picking out the single resonant channel $\ell$ from $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$,

**第 1 步 — 分波截面。** 从 $\sigma = (4\pi/k^2) \sum_\ell (2\ell+1) \sin^2\delta_\ell$ 中取出单一共振通道 $\ell$，

$$ \sigma_\ell = \frac{4\pi}{k^2}(2\ell+1) \sin^2\delta_\ell. $$

**Step 2 — Resonant phase passage.** At a resonance $\delta_\ell$ rises rapidly through $\pi/2$ as $E$ passes $E_R$. The standard parameterization that captures this is

**第 2 步 — 共振相位通过。** 在共振处，当 $E$ 经过 $E_R$ 时 $\delta_\ell$ 迅速通过 $\pi/2$。捕捉此行为的标准参数化为

$$ \cot\delta_\ell(E) = \frac{E_R - E}{\Gamma/2}, $$

so that at $E = E_R$, $\cot\delta_\ell = 0 \implies \delta_\ell = \pi/2$, and the sign of $(E_R - E)$ drives $\delta_\ell$ from just below to just above $\pi/2$ as $E$ increases through $E_R$.

故在 $E = E_R$ 处，$\cot\delta_\ell = 0 \implies \delta_\ell = \pi/2$，且 $(E_R - E)$ 的符号在 $E$ 增大经过 $E_R$ 时驱使 $\delta_\ell$ 从略低于到略高于 $\pi/2$。

**Step 3 — Convert to $\sin^2\delta_\ell$.** Use the identity $\sin^2\delta = 1/(1 + \cot^2\delta)$. Substituting $\cot\delta_\ell = (E_R - E)/(\Gamma/2)$,

**第 3 步 — 转换为 $\sin^2\delta_\ell$。** 用恒等式 $\sin^2\delta = 1/(1 + \cot^2\delta)$。代入 $\cot\delta_\ell = (E_R - E)/(\Gamma/2)$，

$$ \sin^2\delta_\ell = \frac{1}{1 + (E_R - E)^2/(\Gamma/2)^2} = \frac{(\Gamma/2)^2}{(E - E_R)^2 + (\Gamma/2)^2}. $$

**Step 4 — Breit–Wigner cross section.** Substitute into $\sigma_\ell$:

**第 4 步 — Breit–Wigner 截面。** 代入 $\sigma_\ell$：

$$ \sigma_\ell = \frac{4\pi}{k^2}(2\ell+1) \cdot \frac{(\Gamma/2)^2}{(E - E_R)^2 + (\Gamma/2)^2}. $$

This is a Lorentzian in energy of full width at half maximum $\Gamma$, centred at $E_R$.

这是能量上中心在 $E_R$、半高全宽为 $\Gamma$ 的洛伦兹线型。

**Step 5 — Peak and unitarity limit.** At $E = E_R$ the bracket equals $(\Gamma/2)^2$, so the ratio is $1$ (equivalently $\sin^2\delta_\ell = 1$ at $\delta_\ell = \pi/2$). The cross section reaches its maximum

**第 5 步 — 峰值与幺正极限。** 在 $E = E_R$ 处方括号等于 $(\Gamma/2)^2$，故比值为 $1$（等价地 $\delta_\ell = \pi/2$ 处 $\sin^2\delta_\ell = 1$）。截面达到最大值

$$ \sigma_\ell^\text{max} = \frac{4\pi}{k^2}(2\ell+1). $$

This is the **unitarity limit** — the largest possible contribution of a single partial wave, set by $|\sin\delta_\ell| \le 1$, which itself follows from S-matrix unitarity $|e^{2i\delta_\ell}| = 1$. A resonance saturates this bound at $E = E_R$. $\blacksquare$

这是**幺正极限**——单一分波可能的最大贡献，由 $|\sin\delta_\ell| \le 1$ 设定，而后者源于 S 矩阵幺正性 $|e^{2i\delta_\ell}| = 1$。共振在 $E = E_R$ 处饱和此上界。$\blacksquare$

---

*Partial waves and the Born approximation are complementary: the Born series (Module 3.8) excels for weak potentials and high energy, where many $\ell$ contribute and the perturbative Fourier-transform picture is efficient; phase shifts excel at low energy, where only a few $\ell$ matter and $\delta_\ell$ is computed exactly. Both must agree where they overlap, and both feed into the unitary S-matrix that governs all of scattering — from cold atoms to the relativistic high-energy collisions of Modules 6.8 and 8.9.*

*分波与玻恩近似互补：玻恩级数（模块 3.8）在弱势、高能下表现优异，此时多个 $\ell$ 有贡献，微扰傅里叶变换图像高效；相移在低能下表现优异，此时只有少数 $\ell$ 重要，且 $\delta_\ell$ 可精确计算。两者在重叠处必须一致，且都汇入支配全部散射的幺正 S 矩阵——从冷原子到模块 6.8 与 8.9 的相对论高能碰撞。*

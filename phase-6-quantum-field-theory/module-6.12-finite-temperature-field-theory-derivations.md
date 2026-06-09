# Derivations — Module 6.12: Finite-Temperature Field Theory
# 推导 — 模块 6.12：有限温度场论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.12](./module-6.12-finite-temperature-field-theory.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.12](./module-6.12-finite-temperature-field-theory.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. Partition Function as a Euclidean Path Integral · 配分函数作为欧几里得路径积分

**Claim.** $Z = \mathrm{Tr}\, e^{-\beta H} = \oint D\varphi\, e^{-S_E[\varphi]}$ with $S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E$, where bosonic fields are periodic, $\varphi(\tau+\beta) = \varphi(\tau)$, and fermionic fields are antiperiodic, $\psi(\tau+\beta) = -\psi(\tau)$.

**Claim.** $Z = \mathrm{Tr}\, e^{-\beta H} = \oint D\varphi\, e^{-S_E[\varphi]}$，$S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E$，其中玻色场周期，$\varphi(\tau+\beta) = \varphi(\tau)$，费米场反周期，$\psi(\tau+\beta) = -\psi(\tau)$。

**Step 1 — Recognize $e^{-\beta H}$ as imaginary-time evolution.** The Schrödinger propagator is $U(t) = e^{-iHt}$. Set $t = -i\tau$; then $e^{-iHt} = e^{-H\tau}$, and at $\tau = \beta$ this is exactly the Boltzmann operator $e^{-\beta H}$. Thus the thermal weight is the amplitude for evolution through a Euclidean time interval of length $\beta$.

**第 1 步 — 将 $e^{-\beta H}$ 视为虚时间演化。** 薛定谔传播子为 $U(t) = e^{-iHt}$。令 $t = -i\tau$；则 $e^{-iHt} = e^{-H\tau}$，在 $\tau = \beta$ 处恰为玻尔兹曼算符 $e^{-\beta H}$。故热权重就是经过长度为 $\beta$ 的欧几里得时间区间的演化振幅。

**Step 2 — Insert the field-eigenstate resolution.** For a single bosonic field $\hat\varphi(x)$ with eigenstates $\hat\varphi|\varphi\rangle = \varphi|\varphi\rangle$ and completeness $\int D\varphi\, |\varphi\rangle\langle\varphi| = 1$, the matrix element $\langle\varphi_b| e^{-\beta H} |\varphi_a\rangle$ is built by slicing $\beta$ into $N$ steps $\tau_j = j\beta/N$ and inserting a resolution of identity at each slice. The standard coherent-state / configuration-space derivation (Module 6.4) turns each matrix element into a Gaussian integral over the conjugate momentum, leaving a path integral over field histories $\varphi(\tau, x)$:

$$ \langle\varphi_b| e^{-\beta H} |\varphi_a\rangle = \int_{\varphi(0)=\varphi_a}^{\varphi(\beta)=\varphi_b} D\varphi\, \exp\Big(-\int_0^\beta d\tau \int d^3x\, \mathcal{L}_E\Big), $$

with the Euclidean Lagrangian $\mathcal{L}_E = \tfrac12(\partial_\tau\varphi)^2 + \tfrac12(\nabla\varphi)^2 + V(\varphi)$ obtained from the Wick rotation $t \to -i\tau$ (the kinetic term flips sign so that $S_E$ is real and bounded below).

**第 2 步 — 插入场本征态分解。** 对单个玻色场 $\hat\varphi(x)$，本征态 $\hat\varphi|\varphi\rangle = \varphi|\varphi\rangle$，完备性 $\int D\varphi\, |\varphi\rangle\langle\varphi| = 1$，矩阵元 $\langle\varphi_b| e^{-\beta H} |\varphi_a\rangle$ 通过把 $\beta$ 切成 $N$ 段 $\tau_j = j\beta/N$、在每段插入单位分解构建。标准的相干态/位形空间推导（模块 6.4）将每个矩阵元化为对共轭动量的高斯积分，留下对场历史 $\varphi(\tau, x)$ 的路径积分：

$$ \langle\varphi_b| e^{-\beta H} |\varphi_a\rangle = \int_{\varphi(0)=\varphi_a}^{\varphi(\beta)=\varphi_b} D\varphi\, \exp\Big(-\int_0^\beta d\tau \int d^3x\, \mathcal{L}_E\Big), $$

欧几里得拉格朗日量 $\mathcal{L}_E = \tfrac12(\partial_\tau\varphi)^2 + \tfrac12(\nabla\varphi)^2 + V(\varphi)$ 由 Wick 转动 $t \to -i\tau$ 得到（动能项变号，使 $S_E$ 实且下有界）。

**Step 3 — Take the trace (boson $\to$ periodic).** The trace sets $\varphi_a = \varphi_b = \varphi$ and integrates: $Z = \mathrm{Tr}\, e^{-\beta H} = \int D\varphi\, \langle\varphi| e^{-\beta H} |\varphi\rangle$. Setting the final configuration equal to the initial one identifies $\varphi(\beta) = \varphi(0)$, i.e. the field is **periodic** in Euclidean time, $\varphi(\tau+\beta) = \varphi(\tau)$. The path integral therefore runs over closed field histories on a circle of circumference $\beta$:

$$ \boxed{\, Z = \oint D\varphi\, e^{-S_E[\varphi]}, \qquad S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E \,} $$

**第 3 步 — 求迹（玻色 $\to$ 周期）。** 求迹令 $\varphi_a = \varphi_b = \varphi$ 并积分：$Z = \mathrm{Tr}\, e^{-\beta H} = \int D\varphi\, \langle\varphi| e^{-\beta H} |\varphi\rangle$。令末位形等于初位形即 $\varphi(\beta) = \varphi(0)$，即场在欧几里得时间中**周期**，$\varphi(\tau+\beta) = \varphi(\tau)$。故路径积分跑遍周长为 $\beta$ 的圆周上的闭合场历史：

$$ \boxed{\, Z = \oint D\varphi\, e^{-S_E[\varphi]}, \qquad S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E \,} $$

**Step 4 — Fermions (antiperiodic).** For a fermion the field-eigenstates are Grassmann coherent states $|\psi\rangle$ with $\hat\psi|\psi\rangle = \psi|\psi\rangle$, where $\psi$ is an anticommuting (Grassmann) number. The resolution of identity is $\int d\bar\psi\, d\psi\, e^{-\bar\psi\psi}\, |\psi\rangle\langle\psi| = 1$, and a Grassmann-diagonal operator has $\langle\psi| \hat A |\psi'\rangle$ overlaps governed by $e^{\bar\psi\psi'}$. The trace of a *bosonic* operator (even in fermions) is $\mathrm{Tr}\, \hat A = \int d\bar\psi\, d\psi\, e^{-\bar\psi\psi}\, \langle-\psi| \hat A |\psi\rangle$ — the sign flip $-\psi$ in the bra is forced because moving the Grassmann state through the trace past the $e^{-\bar\psi\psi}$ measure anticommutes it. Hence the boundary configuration at $\tau = \beta$ is **minus** the one at $\tau = 0$:

$$ \psi(\tau+\beta) = -\psi(\tau) \quad (\textbf{antiperiodic}). $$

This single Grassmann minus sign is the origin of Fermi–Dirac statistics in the path integral. $\blacksquare$

**第 4 步 — 费米子（反周期）。** 对费米子，场本征态是格拉斯曼相干态 $|\psi\rangle$，$\hat\psi|\psi\rangle = \psi|\psi\rangle$，其中 $\psi$ 是反对易（格拉斯曼）数。单位分解为 $\int d\bar\psi\, d\psi\, e^{-\bar\psi\psi}\, |\psi\rangle\langle\psi| = 1$，格拉斯曼对角算符的交叠 $\langle\psi| \hat A |\psi'\rangle$ 由 $e^{\bar\psi\psi'}$ 支配。一个*玻色型*算符（费米子的偶次）的迹为 $\mathrm{Tr}\, \hat A = \int d\bar\psi\, d\psi\, e^{-\bar\psi\psi}\, \langle-\psi| \hat A |\psi\rangle$——括号中的符号翻转 $-\psi$ 是被强制的，因为把格拉斯曼态穿过迹、越过 $e^{-\bar\psi\psi}$ 测度会使其反对易。故 $\tau = \beta$ 处的边界位形为 $\tau = 0$ 处的**负值**：

$$ \psi(\tau+\beta) = -\psi(\tau) \quad (\textbf{反周期}). $$

这个唯一的格拉斯曼负号正是路径积分中费米–狄拉克统计的来源。$\blacksquare$

---

## B. Matsubara Frequencies · 松原频率

**Claim.** The (anti)periodic boundary conditions discretize the Euclidean frequency: bosons $\omega_n = 2\pi n T$, fermions $\omega_n = (2n+1)\pi T$, $n \in \mathbb{Z}$.

**Claim.**（反）周期性边界条件将欧几里得频率离散化：玻色 $\omega_n = 2\pi n T$，费米 $\omega_n = (2n+1)\pi T$，$n \in \mathbb{Z}$。

**Step 1 — Fourier series on the circle.** A function on the $\tau$-circle of circumference $\beta$ is expanded as a Fourier series (not a transform). Write

$$ \varphi(\tau) = T \sum_n e^{-i\omega_n \tau} \varphi(\omega_n), $$

with the sum over integers $n$. The factor $T = 1/\beta$ is the natural normalization so that, as $\beta \to \infty$, $T \sum_n \to \int d\omega/2\pi$ reproduces the zero-temperature continuum.

**第 1 步 — 圆周上的傅里叶级数。** 周长为 $\beta$ 的 $\tau$ 圆周上的函数展开为傅里叶级数（非变换）。写

$$ \varphi(\tau) = T \sum_n e^{-i\omega_n \tau} \varphi(\omega_n), $$

求和遍历整数 $n$。因子 $T = 1/\beta$ 是自然归一化，使得 $\beta \to \infty$ 时 $T \sum_n \to \int d\omega/2\pi$ 重现零温连续谱。

**Step 2 — Impose the boson boundary condition.** Periodicity $\varphi(\tau+\beta) = \varphi(\tau)$ requires each mode to satisfy $e^{-i\omega_n(\tau+\beta)} = e^{-i\omega_n \tau}$, i.e. $e^{-i\omega_n \beta} = 1$. Hence $\omega_n \beta = 2\pi n$, giving

$$ \boxed{\, \omega_n = 2\pi n/\beta = 2\pi n T \quad (\text{bosons}) \,} $$

**第 2 步 — 施加玻色边界条件。** 周期性 $\varphi(\tau+\beta) = \varphi(\tau)$ 要求每个模式满足 $e^{-i\omega_n(\tau+\beta)} = e^{-i\omega_n \tau}$，即 $e^{-i\omega_n \beta} = 1$。故 $\omega_n \beta = 2\pi n$，给出

$$ \boxed{\, \omega_n = 2\pi n/\beta = 2\pi n T \quad (\text{玻色}) \,} $$

**Step 3 — Impose the fermion boundary condition.** Antiperiodicity $\psi(\tau+\beta) = -\psi(\tau)$ requires $e^{-i\omega_n \beta} = -1$, i.e. $\omega_n \beta = (2n+1)\pi$. Hence

$$ \boxed{\, \omega_n = (2n+1)\pi/\beta = (2n+1)\pi T \quad (\text{fermions}) \,} $$

The free Euclidean propagator follows from inverting the quadratic action $(-\partial_\tau^2 - \nabla^2 + m^2)$ in Fourier space: $G(\omega_n, k) = 1/(\omega_n^2 + k^2 + m^2) = 1/(\omega_n^2 + E_k^2)$. $\blacksquare$

**第 3 步 — 施加费米边界条件。** 反周期性 $\psi(\tau+\beta) = -\psi(\tau)$ 要求 $e^{-i\omega_n \beta} = -1$，即 $\omega_n \beta = (2n+1)\pi$。故

$$ \boxed{\, \omega_n = (2n+1)\pi/\beta = (2n+1)\pi T \quad (\text{费米}) \,} $$

自由欧几里得传播子由在傅里叶空间反转二次作用量 $(-\partial_\tau^2 - \nabla^2 + m^2)$ 得到：$G(\omega_n, k) = 1/(\omega_n^2 + k^2 + m^2) = 1/(\omega_n^2 + E_k^2)$。$\blacksquare$

---

## C. Matsubara Frequency Sums · 松原频率求和

**Claim.** $T \sum_n 1/(\omega_n^2 + E^2) = (1/2E) \coth(\beta E/2) = (1/2E)[1 + 2 n_B(E)]$ for bosons ($\omega_n = 2\pi n T$), and the fermionic analogue ($\omega_n = (2n+1)\pi T$) gives $(1/2E) \tanh(\beta E/2) = (1/2E)[1 - 2 n_F(E)]$.

**Claim.** 玻色（$\omega_n = 2\pi n T$）：$T \sum_n 1/(\omega_n^2 + E^2) = (1/2E) \coth(\beta E/2) = (1/2E)[1 + 2 n_B(E)]$；费米（$\omega_n = (2n+1)\pi T$）给出 $(1/2E) \tanh(\beta E/2) = (1/2E)[1 - 2 n_F(E)]$。

**Step 1 — A weighting function with poles at the Matsubara frequencies.** Seek a function whose poles, in the complex frequency plane, sit exactly at $\omega = i\omega_n$. For bosons, $\coth(\beta\omega/2)$ has simple poles where $\beta\omega/2 = i\pi n$, i.e. $\omega = 2\pi i n T = i\omega_n$, each with residue (computed from $\coth z \approx 1/z$ near its poles) equal to $2/\beta = 2T$. Therefore, for any function $f(\omega)$ analytic at $\omega = i\omega_n$,

$$ T \sum_n f(i\omega_n) = \frac{1}{2\pi i} \oint_C d\omega \cdot (\tfrac12 \coth(\beta\omega/2))\, f(\omega), $$

where the contour $C$ encircles the imaginary axis (all the poles of $\coth$). The $\tfrac12$ compensates the residue $2T$ against the prefactor $T$ so that the sum is reproduced.

**第 1 步 — 极点位于松原频率的加权函数。** 寻找一个在复频率平面上极点恰位于 $\omega = i\omega_n$ 的函数。对玻色子，$\coth(\beta\omega/2)$ 在 $\beta\omega/2 = i\pi n$ 即 $\omega = 2\pi i n T = i\omega_n$ 处有单极点，每个留数（由极点附近 $\coth z \approx 1/z$ 算得）为 $2/\beta = 2T$。故对任何在 $\omega = i\omega_n$ 解析的 $f(\omega)$，

$$ T \sum_n f(i\omega_n) = \frac{1}{2\pi i} \oint_C d\omega \cdot (\tfrac12 \coth(\beta\omega/2))\, f(\omega), $$

其中围道 $C$ 环绕虚轴（$\coth$ 的全部极点）。因子 $\tfrac12$ 使留数 $2T$ 与前因子 $T$ 抵消，从而重现求和。

**Step 2 — Deform the contour onto the propagator poles.** Take $f(\omega) = 1/(-\omega^2 + E^2)$ so that $f(i\omega_n) = 1/(\omega_n^2 + E^2)$. The integrand $(\tfrac12) \coth(\beta\omega/2)/(E^2 - \omega^2)$ decays at infinity, so the contour wrapping the imaginary axis can be deformed to wrap instead the two poles of $f$ at $\omega = \pm E$. By Cauchy's theorem (with the orientation sign from swapping which poles are enclosed),

$$ T \sum_n 1/(\omega_n^2 + E^2) = - \sum_{\omega=\pm E} \mathrm{Res}\, [(\tfrac12 \coth(\beta\omega/2)) / (E^2 - \omega^2)]. $$

The residue of $1/(E^2 - \omega^2)$ at $\omega = +E$ is $-1/(2E)$, at $\omega = -E$ is $+1/(2E)$. Using $\coth$ even-ness $\coth(-\beta E/2) = -\coth(\beta E/2)$:

$$ T \sum_n 1/(\omega_n^2 + E^2) = (\tfrac12 \coth(\beta E/2))\cdot(1/2E) + (\tfrac12 \coth(\beta E/2))\cdot(1/2E) = \boxed{(1/2E) \coth(\beta E/2)}. $$

**第 2 步 — 将围道变形到传播子极点上。** 取 $f(\omega) = 1/(-\omega^2 + E^2)$，使 $f(i\omega_n) = 1/(\omega_n^2 + E^2)$。被积量 $(\tfrac12) \coth(\beta\omega/2)/(E^2 - \omega^2)$ 在无穷远衰减，故环绕虚轴的围道可变形为环绕 $f$ 在 $\omega = \pm E$ 处的两个极点。由柯西定理（符号来自所围极点的互换）：

$$ T \sum_n 1/(\omega_n^2 + E^2) = - \sum_{\omega=\pm E} \mathrm{Res}\, [(\tfrac12 \coth(\beta\omega/2)) / (E^2 - \omega^2)]. $$

$1/(E^2 - \omega^2)$ 在 $\omega = +E$ 处留数为 $-1/(2E)$，在 $\omega = -E$ 处为 $+1/(2E)$。用 $\coth$ 的奇性 $\coth(-\beta E/2) = -\coth(\beta E/2)$：

$$ T \sum_n 1/(\omega_n^2 + E^2) = (\tfrac12 \coth(\beta E/2))\cdot(1/2E) + (\tfrac12 \coth(\beta E/2))\cdot(1/2E) = \boxed{(1/2E) \coth(\beta E/2)}. $$

**Step 3 — Extract the Bose–Einstein occupation.** Use the identity $\coth(x) = 1 + 2/(e^{2x} - 1)$. With $x = \beta E/2$,

$$ \coth(\beta E/2) = 1 + 2/(e^{\beta E} - 1) = 1 + 2 n_B(E), \qquad n_B(E) = 1/(e^{\beta E} - 1). $$

Hence

$$ \boxed{\, T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 + 2 n_B(E)] \,} $$

The "1" is the zero-point (vacuum) contribution; the "$2 n_B$" is the thermal occupation. The Bose–Einstein distribution was never assumed — it dropped out of the pole structure of $\coth$.

**第 3 步 — 提取玻色–爱因斯坦占据数。** 用恒等式 $\coth(x) = 1 + 2/(e^{2x} - 1)$。取 $x = \beta E/2$：

$$ \coth(\beta E/2) = 1 + 2/(e^{\beta E} - 1) = 1 + 2 n_B(E), \qquad n_B(E) = 1/(e^{\beta E} - 1). $$

故

$$ \boxed{\, T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 + 2 n_B(E)] \,} $$

其中“1”是零点（真空）贡献；“$2 n_B$”是热占据。玻色–爱因斯坦分布从未被假设——它从 $\coth$ 的极点结构中自然落出。

**Step 4 — Fermionic analogue.** For fermions the weighting function with poles at the *odd* frequencies $\omega = i(2n+1)\pi T$ is $\tanh(\beta\omega/2)$ (its poles sit at $\beta\omega/2 = i(2n+1)\pi/2$, residue $2T$). Repeating Steps 2–3,

$$ T \sum_n 1/(\omega_n^2 + E^2) = (1/2E) \tanh(\beta E/2), \qquad \tanh(x) = 1 - 2/(e^{2x} + 1), $$

so with $x = \beta E/2$,

$$ \boxed{\, T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 - 2 n_F(E)], \qquad n_F(E) = 1/(e^{\beta E} + 1) \,} $$

The Fermi–Dirac distribution emerges the same way, with the crucial $e^{\beta E} + 1$ fixed by the odd frequencies (antiperiodic boundary condition). $\blacksquare$

**第 4 步 — 费米类比。** 对费米子，极点位于*奇*频率 $\omega = i(2n+1)\pi T$ 的加权函数是 $\tanh(\beta\omega/2)$（其极点在 $\beta\omega/2 = i(2n+1)\pi/2$，留数 $2T$）。重复第 2–3 步：

$$ T \sum_n 1/(\omega_n^2 + E^2) = (1/2E) \tanh(\beta E/2), \qquad \tanh(x) = 1 - 2/(e^{2x} + 1), $$

故取 $x = \beta E/2$：

$$ \boxed{\, T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 - 2 n_F(E)], \qquad n_F(E) = 1/(e^{\beta E} + 1) \,} $$

费米–狄拉克分布以同样方式涌现，关键的 $e^{\beta E} + 1$ 由奇频率（反周期边界条件）固定。$\blacksquare$

---

## D. Free Energy of the Ideal Bose Gas and Stefan–Boltzmann · 理想玻色气体自由能与斯特藩–玻尔兹曼

**Claim.** $F/V = \int d^3k/(2\pi)^3\, [\tfrac12 E_k + T \ln(1 - e^{-\beta E_k})]$, and for massless bosons $F/V = -(\pi^2/90)\, g T^4$, $P = (\pi^2/90)\, g T^4$.

**Claim.** $F/V = \int d^3k/(2\pi)^3\, [\tfrac12 E_k + T \ln(1 - e^{-\beta E_k})]$，对无质量玻色子 $F/V = -(\pi^2/90)\, g T^4$，$P = (\pi^2/90)\, g T^4$。

**Step 1 — Gaussian path integral.** For a free scalar the Euclidean action is quadratic, $S_E = \tfrac12 \sum_n \int d^3k/(2\pi)^3\, (\omega_n^2 + E_k^2)\, |\varphi(\omega_n,k)|^2\, V$. The Gaussian integral gives $Z = \prod_{n,k} (\omega_n^2 + E_k^2)^{-1/2}$ (times a $\varphi$-independent constant), so

$$ \ln Z = -\tfrac12 V \sum_n \int \frac{d^3k}{(2\pi)^3}\, \ln(\omega_n^2 + E_k^2), \qquad F = -T \ln Z. $$

**第 1 步 — 高斯路径积分。** 对自由标量场，欧几里得作用量是二次的，$S_E = \tfrac12 \sum_n \int d^3k/(2\pi)^3\, (\omega_n^2 + E_k^2)\, |\varphi(\omega_n,k)|^2\, V$。高斯积分给出 $Z = \prod_{n,k} (\omega_n^2 + E_k^2)^{-1/2}$（乘一个与 $\varphi$ 无关的常数），故

$$ \ln Z = -\tfrac12 V \sum_n \int \frac{d^3k}{(2\pi)^3}\, \ln(\omega_n^2 + E_k^2), \qquad F = -T \ln Z. $$

**Step 2 — Do the Matsubara sum $\sum_n \ln(\omega_n^2 + E^2)$.** Differentiate the sum with respect to $E^2$ to remove the logarithm and reuse Section C:

$$ \frac{\partial}{\partial E^2}\, [T \sum_n \ln(\omega_n^2 + E^2)] = T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 + 2 n_B(E)] = (1/2E) \coth(\beta E/2). $$

Now integrate back over $E^2$. Using $d(\beta E)/dE^2 = \beta/(2E)$ and $\int \coth(u)\, du = \ln\sinh(u)$, one finds (dropping an $E$-independent constant absorbed into the normalization)

$$ T \sum_n \ln(\omega_n^2 + E^2) = E + 2T \ln(1 - e^{-\beta E}). $$

A direct check: the right-hand side has $\partial/\partial E = 1 + 2/(e^{\beta E}-1) = \coth(\beta E/2)$, and $\partial E/\partial E^2 = 1/2E$, reproducing the line above. The two terms are the zero-point energy $E$ ($= 2\cdot\tfrac12 E$ for the contribution counted here) and the thermal log.

**第 2 步 — 完成松原求和 $\sum_n \ln(\omega_n^2 + E^2)$。** 对 $E^2$ 求导以消去对数并复用第 C 节：

$$ \frac{\partial}{\partial E^2}\, [T \sum_n \ln(\omega_n^2 + E^2)] = T \sum_n 1/(\omega_n^2 + E^2) = (1/2E)[1 + 2 n_B(E)] = (1/2E) \coth(\beta E/2). $$

现对 $E^2$ 积回。用 $d(\beta E)/dE^2 = \beta/(2E)$ 与 $\int \coth(u)\, du = \ln\sinh(u)$，得（略去被归一化吸收的与 $E$ 无关常数）

$$ T \sum_n \ln(\omega_n^2 + E^2) = E + 2T \ln(1 - e^{-\beta E}). $$

直接验证：右边对 $E$ 求导得 $1 + 2/(e^{\beta E}-1) = \coth(\beta E/2)$，又 $\partial E/\partial E^2 = 1/2E$，重现上一行。两项分别是零点能 $E$（即此处计入贡献的 $2\cdot\tfrac12 E$）与热对数项。

**Step 3 — Assemble the free-energy density.** Insert into $F = -T \ln Z = (T/2) V \sum_n \int d^3k/(2\pi)^3\, \ln(\omega_n^2+E_k^2)$, so $F/V = \tfrac12 \int d^3k/(2\pi)^3\, [E_k + 2T \ln(1 - e^{-\beta E_k})]$, i.e.

$$ \boxed{\, F/V = \int \frac{d^3k}{(2\pi)^3}\, [\tfrac12 E_k + T \ln(1 - e^{-\beta E_k})] \,} $$

The $\tfrac12 E_k$ is the divergent zero-point (vacuum) energy, removed by renormalization; the second term is the finite Bose–Einstein thermal free energy.

**第 3 步 — 组装自由能密度。** 代入 $F = -T \ln Z = (T/2) V \sum_n \int d^3k/(2\pi)^3\, \ln(\omega_n^2+E_k^2)$，故 $F/V = \tfrac12 \int d^3k/(2\pi)^3\, [E_k + 2T \ln(1 - e^{-\beta E_k})]$，即

$$ \boxed{\, F/V = \int \frac{d^3k}{(2\pi)^3}\, [\tfrac12 E_k + T \ln(1 - e^{-\beta E_k})] \,} $$

$\tfrac12 E_k$ 是发散的零点（真空）能，由重整化去除；第二项是有限的玻色–爱因斯坦热自由能。

**Step 4 — Massless limit and the Stefan–Boltzmann law.** Drop the vacuum term, set $E_k = k$ (massless), and include $g$ internal degrees of freedom:

$$ F/V = g T \int \frac{d^3k}{(2\pi)^3}\, \ln(1 - e^{-\beta k}) = \frac{g T}{2\pi^2} \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}). $$

Integrate by parts ($u = \ln(1-e^{-\beta k})$, $dv = k^2 dk$):

$$ \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}) = -\frac{\beta}{3} \int_0^\infty dk\, \frac{k^3 e^{-\beta k}}{1 - e^{-\beta k}} = -\frac{1}{3\beta^3} \int_0^\infty dx\, \frac{x^3}{e^x - 1}, $$

with $x = \beta k$. The standard integral $\int_0^\infty dx\, x^3/(e^x - 1) = \Gamma(4)\zeta(4) = 6\cdot(\pi^4/90) = \pi^4/15$. Therefore

$$ F/V = \frac{g T}{2\pi^2}\cdot\Big(-\frac{1}{3\beta^3}\Big)\cdot\frac{\pi^4}{15}. $$

Collecting the constants, $T\cdot(1/\beta^3) = T^4$ and $(1/2\pi^2)(1/3)(\pi^4/15) = \pi^2/90$:

$$ \boxed{\, F/V = -(\pi^2/90)\, g T^4 \,} $$

The pressure is $P = -(\partial F/\partial V)|_T = -F/V$ (since $F$ is extensive, $F = (F/V)V$):

$$ \boxed{\, P = (\pi^2/90)\, g T^4, \qquad \rho = -F/V + Ts = 3P = (\pi^2/30)\, g T^4 \,} $$

For $g = 2$ (photon polarizations) this is the Stefan–Boltzmann law for blackbody radiation; the $T^4$ scaling and the coefficient match the result of Modules 2.5/2.6, now derived directly from the Matsubara path integral. $\blacksquare$

**第 4 步 — 无质量极限与斯特藩–玻尔兹曼定律。** 丢弃真空项，令 $E_k = k$（无质量），并计入 $g$ 个内部自由度：

$$ F/V = g T \int \frac{d^3k}{(2\pi)^3}\, \ln(1 - e^{-\beta k}) = \frac{g T}{2\pi^2} \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}). $$

分部积分（$u = \ln(1-e^{-\beta k})$，$dv = k^2 dk$）：

$$ \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}) = -\frac{\beta}{3} \int_0^\infty dk\, \frac{k^3 e^{-\beta k}}{1 - e^{-\beta k}} = -\frac{1}{3\beta^3} \int_0^\infty dx\, \frac{x^3}{e^x - 1}, $$

其中 $x = \beta k$。标准积分 $\int_0^\infty dx\, x^3/(e^x - 1) = \Gamma(4)\zeta(4) = 6\cdot(\pi^4/90) = \pi^4/15$。故

$$ F/V = \frac{g T}{2\pi^2}\cdot\Big(-\frac{1}{3\beta^3}\Big)\cdot\frac{\pi^4}{15}, $$

合并常数 $T\cdot(1/\beta^3) = T^4$ 与 $(1/2\pi^2)(1/3)(\pi^4/15) = \pi^2/90$：

$$ \boxed{\, F/V = -(\pi^2/90)\, g T^4 \,} $$

压强 $P = -(\partial F/\partial V)|_T = -F/V$（因 $F$ 是广延量，$F = (F/V)V$）：

$$ \boxed{\, P = (\pi^2/90)\, g T^4, \qquad \rho = 3P = (\pi^2/30)\, g T^4 \,} $$

取 $g = 2$（光子偏振）即得黑体辐射的斯特藩–玻尔兹曼定律；$T^4$ 标度与系数与模块 2.5/2.6 的结果一致，此处直接由松原路径积分推导。$\blacksquare$

---

## E. Physical Scope: KMS, Equilibrium, and the Real-Time Alternative · 物理适用范围：KMS、平衡与实时替代

**Claim.** The (anti)periodicity of imaginary-time Green's functions is equivalent to thermal equilibrium (the KMS condition); the Matsubara formalism underlies finite-T QFT, the quark–gluon plasma, the electroweak phase transition, and condensed-matter many-body theory, with real-time Keldysh as the out-of-equilibrium alternative.

**Claim.** 虚时间格林函数的（反）周期性等价于热平衡（KMS 条件）；松原形式是有限温度 QFT、夸克–胶子等离子体、电弱相变与凝聚态多体理论的基础，实时 Keldysh 是非平衡替代方案。

**Step 1 — The KMS condition.** Consider the thermal two-point function $G(\tau) = \langle T_\tau \varphi(\tau) \varphi(0)\rangle = Z^{-1} \mathrm{Tr}[e^{-\beta H} T_\tau \varphi(\tau)\varphi(0)]$. For $0 < \tau < \beta$, using the cyclicity of the trace and $\varphi(\tau) = e^{H\tau} \varphi\, e^{-H\tau}$,

$$ G(\tau - \beta) = Z^{-1} \mathrm{Tr}[e^{-\beta H} \varphi(\tau-\beta) \varphi(0)] = Z^{-1} \mathrm{Tr}[\varphi(\tau) e^{-\beta H} \varphi(0)] = \pm Z^{-1} \mathrm{Tr}[e^{-\beta H} \varphi(0) \varphi(\tau)] = \pm G(\tau), $$

where the upper sign holds for bosons and the lower for fermions (from reordering the operators inside the trace). This is the **Kubo–Martin–Schwinger (KMS) condition**: $G(\tau-\beta) = \pm G(\tau)$, i.e. periodicity (bosons) / antiperiodicity (fermions) of thermal Green's functions is *equivalent to* the state being the equilibrium Gibbs state $e^{-\beta H}/Z$ at temperature $T$. It is the rigorous, formalism-independent definition of thermal equilibrium, and it is exactly what forces the Matsubara boundary conditions of Section A.

**第 1 步 — KMS 条件。** 考虑热两点函数 $G(\tau) = \langle T_\tau \varphi(\tau) \varphi(0)\rangle = Z^{-1} \mathrm{Tr}[e^{-\beta H} T_\tau \varphi(\tau)\varphi(0)]$。对 $0 < \tau < \beta$，用迹的循环性与 $\varphi(\tau) = e^{H\tau} \varphi\, e^{-H\tau}$：

$$ G(\tau - \beta) = Z^{-1} \mathrm{Tr}[e^{-\beta H} \varphi(\tau-\beta) \varphi(0)] = Z^{-1} \mathrm{Tr}[\varphi(\tau) e^{-\beta H} \varphi(0)] = \pm Z^{-1} \mathrm{Tr}[e^{-\beta H} \varphi(0) \varphi(\tau)] = \pm G(\tau), $$

上符号对玻色子、下符号对费米子（来自迹内算符重排）。这就是 **久保–马丁–施温格（KMS）条件**：$G(\tau-\beta) = \pm G(\tau)$，即热格林函数的周期（玻色）/反周期（费米）性*等价于*态为温度 $T$ 的平衡吉布斯态 $e^{-\beta H}/Z$。它是热平衡的严格、不依赖于形式的定义，正是它强制了第 A 节的松原边界条件。

**Step 2 — Where the formalism applies.** The imaginary-time (Matsubara) construction computes any equilibrium thermodynamic quantity: it gives the equation of state of the quark–gluon plasma probed in heavy-ion collisions, the finite-temperature effective potential whose minimum shifts as $T$ rises (driving high-$T$ symmetry restoration and the electroweak phase transition of the early universe, Module 8.6), and the Matsubara Green's functions of condensed-matter many-body theory (Module 6.2) — including the temperature dependence of the BCS gap $\Delta(T)$ (Module 5.5). It is the same Matsubara technology throughout; only the action and the degrees of freedom change.

**第 2 步 — 形式的适用范围。** 虚时间（松原）构造可计算任何平衡热力学量：给出重离子碰撞中探测的夸克–胶子等离子体物态方程、随 $T$ 升高极小移动的有限温度有效势（驱动高温对称性恢复与早期宇宙电弱相变，模块 8.6），以及凝聚态多体理论的松原格林函数（模块 6.2）——包括 BCS 能隙 $\Delta(T)$ 的温度依赖（模块 5.5）。全程是同一套松原技术；只有作用量与自由度改变。

**Step 3 — The out-of-equilibrium alternative.** The Matsubara formalism is intrinsically a *static, equilibrium* construction — imaginary time has no dynamics. For genuinely time-dependent, out-of-equilibrium problems (transport, thermalization, driven systems) one uses the real-time **Keldysh (closed-time-path)** formalism, where fields live on a contour that runs forward then backward in real time (and optionally down to $-i\beta$). At equilibrium Keldysh results reduce, via analytic continuation $i\omega_n \to \omega + i0^+$, to the Matsubara ones — the two formalisms agree where their domains overlap. $\blacksquare$

**第 3 步 — 非平衡替代方案。** 松原形式本质上是*静态、平衡*构造——虚时间没有动力学。对真正含时、非平衡的问题（输运、热化、驱动系统），使用实时的 **Keldysh（闭合时间路径）**形式，其中场居于实时间中先正向后反向（并可向下延伸到 $-i\beta$）的围道上。在平衡处，Keldysh 结果经解析延拓 $i\omega_n \to \omega + i0^+$ 化为松原结果——两种形式在其定义域重叠处一致。$\blacksquare$

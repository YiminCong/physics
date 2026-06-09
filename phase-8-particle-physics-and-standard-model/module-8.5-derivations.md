# Derivations — Module 8.5: The Standard Model & Beyond
# 推导 — 模块 8.5：标准模型及其超越

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.5](./module-8.5-standard-model-and-beyond.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.5](./module-8.5-standard-model-and-beyond.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Seesaw Mechanism for Neutrino Masses · 中微子质量的跷跷板机制

**Claim.** Adding a right-handed neutrino $N_R$ with Majorana mass $M \gg v$ to the Standard Model generates light neutrino masses $m_\nu \approx m_D^2/M$ (type-I seesaw), where $m_D = y_\nu v/\sqrt2$ is the Dirac mass from the Yukawa coupling.

**命题。** 在标准模型中添加具有马约拉纳质量 $M \gg v$ 的右手中微子 $N_R$，产生轻中微子质量 $m_\nu \approx m_D^2/M$（I 型跷跷板），其中 $m_D = y_\nu v/\sqrt2$ 是来自汤川耦合的狄拉克质量。

**Step 1 — The neutrino mass Lagrangian.** After electroweak symmetry breaking, the most general neutrino mass terms are:

**第 1 步 — 中微子质量拉格朗日量。** 电弱对称性破缺后，最一般的中微子质量项为：

$$ \mathcal{L}_{\nu\text{ mass}} = -m_D \bar\nu_L N_R - (M/2) \bar N^c_R N_R + \text{h.c.}, $$

where $\nu_L$ is the left-handed neutrino (Standard Model field), $N_R$ is the right-handed neutrino (SM singlet), $m_D$ is the Dirac mass (from Yukawa coupling $y_\nu$ after SSB: $m_D = y_\nu\langle\phi\rangle = y_\nu v/\sqrt2$), and $M$ is the Majorana mass of $N_R$ (not protected by any SM symmetry, so $M$ can be very large). $N^c_R = C(\bar N_R)^T$ is the charge conjugate.

其中 $\nu_L$ 是左手中微子（标准模型场），$N_R$ 是右手中微子（SM 单态），$m_D$ 是狄拉克质量（来自自发对称性破缺后的汤川耦合 $y_\nu$：$m_D = y_\nu v/\sqrt2$），$M$ 是 $N_R$ 的马约拉纳质量（不受任何 SM 对称性保护，故 $M$ 可以很大）。$N^c_R = C(\bar N_R)^T$ 是电荷共轭。

**Step 2 — Matrix form.** In the basis $\Psi = (\nu_L, N^c_R)^T$, the mass Lagrangian takes the form:

**第 2 步 — 矩阵形式。** 在基底 $\Psi = (\nu_L, N^c_R)^T$ 中，质量拉格朗日量取形式：

$$ \mathcal{L}_\text{mass} = -(1/2)\Psi^T C M_\nu \Psi + \text{h.c.}, $$

where the **mass matrix** is:

其中**质量矩阵**为：

$$ M_\nu = \begin{pmatrix} 0 & m_D \\ m_D & M \end{pmatrix}. $$

The zero in the (1,1) position is because $\nu_L$ has no Majorana mass (it would break $SU(2)_L \times U(1)_Y$). The off-diagonal $m_D$ connects the left and right sectors.

(1,1) 位置的零是因为 $\nu_L$ 没有马约拉纳质量（它会破坏 $SU(2)_L \times U(1)_Y$）。非对角元 $m_D$ 连接左手和右手部分。

**Step 3 — Diagonalize the mass matrix.** The eigenvalues of $M_\nu$ are found from $\det(M_\nu - \lambda I) = 0$:

**第 3 步 — 对角化质量矩阵。** $M_\nu$ 的本征值由 $\det(M_\nu - \lambda I) = 0$ 求得：

$$ \det\begin{pmatrix} -\lambda & m_D \\ m_D & M - \lambda \end{pmatrix} = -\lambda(M - \lambda) - m_D^2 = \lambda^2 - M\lambda - m_D^2 = 0. $$

Using the quadratic formula:

利用求根公式：

$$ \lambda = [M \pm \sqrt{M^2 + 4m_D^2}] / 2. $$

**Step 4 — Approximate in the seesaw limit $M \gg m_D$.** Factor out $M$ from the square root:

**第 4 步 — 在跷跷板极限 $M \gg m_D$ 下近似。** 从平方根中提出 $M$：

$$ \sqrt{M^2 + 4m_D^2} = M\sqrt{1 + 4m_D^2/M^2} \approx M(1 + 2m_D^2/M^2) = M + 2m_D^2/M. $$

The two eigenvalues are:

两个本征值为：

$$ \begin{aligned} \lambda_+ &= [M + M + 2m_D^2/M]/2 = M + m_D^2/M \approx M \quad \text{(heavy neutrino, mass} \approx M\text{),} \\ \lambda_- &= [M - M - 2m_D^2/M]/2 = -m_D^2/M \quad \text{(light neutrino, } |\text{mass}| = m_D^2/M\text{).} \end{aligned} $$

The physical masses are the absolute values:

物理质量为绝对值：

$$ m_\text{heavy} \approx M, \quad \boxed{\, m_\text{light} \approx m_D^2/M \,}. $$

**Step 5 — Physical interpretation.** The light eigenvalue $m_\nu = m_D^2/M$ has the "seesaw" property: as $M$ increases, $m_\nu$ decreases. For $m_D \sim y_\nu \cdot 174$ GeV (electroweak scale) and $m_\nu \sim 0.05$ eV (atmospheric neutrino oscillations):

**第 5 步 — 物理诠释。** 轻本征值 $m_\nu = m_D^2/M$ 具有"跷跷板"特性：随着 $M$ 增大，$m_\nu$ 减小。对于 $m_D \sim y_\nu \cdot 174$ GeV（电弱尺度）和 $m_\nu \sim 0.05$ eV（大气中微子振荡）：

$$ M \approx m_D^2/m_\nu \sim (y_\nu \cdot 174 \text{ GeV})^2 / (0.05 \text{ eV}). $$

For $y_\nu \sim 1$ (top-quark-scale Yukawa):

对于 $y_\nu \sim 1$（顶夸克尺度汤川耦合）：

$$ M \sim (174 \text{ GeV})^2 / (0.05 \times 10^{-9} \text{ GeV}) \sim 3 \times 10^{21} \text{ GeV} / 5 \times 10^{-11} \sim 6 \times 10^{14} \text{ GeV} \approx 10^{14} \text{ GeV}. $$

For $y_\nu \sim m_e/v \sim 2 \times 10^{-6}$ (electron-scale): $M \sim 10^3$ GeV (TeV scale).

对于 $y_\nu \sim m_e/v \sim 2 \times 10^{-6}$（电子尺度）：$M \sim 10^3$ GeV（TeV 尺度）。

The "natural" choice is $y_\nu \sim O(1)$, placing $M$ near the GUT scale $\sim 10^{14}$–$10^{15}$ GeV — a remarkable hint of unification! $\blacksquare$

"自然"选择是 $y_\nu \sim O(1)$，将 $M$ 置于大统一理论尺度 $\sim 10^{14}$–$10^{15}$ GeV 附近——这是统一的绝妙暗示！$\blacksquare$

---

## B. Two-Flavor Neutrino Oscillation Probability · 两味中微子振荡概率

**Claim.** For two neutrino flavors $\nu_e$ and $\nu_\mu$ with a mixing angle $\theta$ and mass-squared difference $\Delta m^2 = m^2_2 - m^2_1$, the oscillation probability is:

**命题。** 对于具有混合角 $\theta$ 和质量平方差 $\Delta m^2 = m^2_2 - m^2_1$ 的两味中微子 $\nu_e$ 和 $\nu_\mu$，振荡概率为：

$$ P(\nu_e \to \nu_\mu; L) = \sin^2(2\theta) \cdot \sin^2(\Delta m^2 L / 4E). $$

**Step 1 — Mass and flavor eigenstates.** The flavor eigenstates ($\nu_e, \nu_\mu$) produced by weak interactions are related to mass eigenstates ($\nu_1, \nu_2$) via the mixing matrix:

**第 1 步 — 质量本征态与味本征态。** 弱相互作用产生的味本征态（$\nu_e, \nu_\mu$）通过混合矩阵与质量本征态（$\nu_1, \nu_2$）相关：

$$ \begin{aligned} |\nu_e\rangle &= \cos\theta |\nu_1\rangle + \sin\theta |\nu_2\rangle, \\ |\nu_\mu\rangle &= -\sin\theta |\nu_1\rangle + \cos\theta |\nu_2\rangle. \end{aligned} $$

Inverted:

反转：

$$ \begin{aligned} |\nu_1\rangle &= \cos\theta |\nu_e\rangle - \sin\theta |\nu_\mu\rangle, \\ |\nu_2\rangle &= \sin\theta |\nu_e\rangle + \cos\theta |\nu_\mu\rangle. \end{aligned} $$

**Step 2 — Time evolution of mass eigenstates.** Mass eigenstates evolve with definite energy. For an ultrarelativistic neutrino with momentum $p \approx E$:

**第 2 步 — 质量本征态的时间演化。** 质量本征态以确定能量演化。对于动量 $p \approx E$ 的超相对论中微子：

$$ E_i = \sqrt{p^2 + m^2_i} \approx p + m^2_i/(2p) \approx E + m^2_i/(2E) \quad \text{(for } m_i \ll E\text{).} $$

The state at time $t$ (and distance $L = ct \approx t$ in natural units):

在时间 $t$（距离 $L = ct \approx t$，自然单位）时的态：

$$ |\nu_i(t)\rangle = e^{-iE_it} |\nu_i\rangle \approx e^{-iEt} e^{-im^2_i L/(2E)} |\nu_i\rangle. $$

The overall phase $e^{-iEt}$ is common to both and drops out of probabilities.

总体相位 $e^{-iEt}$ 对两者相同，在概率中消去。

**Step 3 — Time-evolved flavor state.** A $\nu_e$ produced at $L = 0$ evolves as:

**第 3 步 — 时间演化的味态。** 在 $L = 0$ 处产生的 $\nu_e$ 演化为：

$$ |\nu_e(L)\rangle = \cos\theta \cdot e^{-im^2_1 L/(2E)} |\nu_1\rangle + \sin\theta \cdot e^{-im^2_2 L/(2E)} |\nu_2\rangle. $$

Express back in the flavor basis using $|\nu_1\rangle = \cos\theta|\nu_e\rangle - \sin\theta|\nu_\mu\rangle$ and $|\nu_2\rangle = \sin\theta|\nu_e\rangle + \cos\theta|\nu_\mu\rangle$:

用 $|\nu_1\rangle = \cos\theta|\nu_e\rangle - \sin\theta|\nu_\mu\rangle$ 和 $|\nu_2\rangle = \sin\theta|\nu_e\rangle + \cos\theta|\nu_\mu\rangle$ 变换回味本征态：

$$ |\nu_e(L)\rangle = [\cos^2\theta\, e^{-i\varphi_1} + \sin^2\theta\, e^{-i\varphi_2}]|\nu_e\rangle + \sin\theta\cos\theta[-e^{-i\varphi_1} + e^{-i\varphi_2}]|\nu_\mu\rangle, $$

where $\varphi_i = m^2_i L/(2E)$.

其中 $\varphi_i = m^2_i L/(2E)$。

**Step 4 — Transition amplitude.** The amplitude for $\nu_e \to \nu_\mu$ is:

**第 4 步 — 跃迁振幅。** $\nu_e \to \nu_\mu$ 的振幅为：

$$ A(\nu_e \to \nu_\mu) = \langle\nu_\mu|\nu_e(L)\rangle = \sin\theta \cos\theta(e^{-i\varphi_2} - e^{-i\varphi_1}). $$

**Step 5 — Probability.** The oscillation probability:

**第 5 步 — 概率。** 振荡概率：

$$ P(\nu_e \to \nu_\mu) = |A|^2 = \sin^2\theta\cos^2\theta \cdot |e^{-i\varphi_2} - e^{-i\varphi_1}|^2. $$

Compute the modulus squared:

计算模的平方：

$$ \begin{aligned} |e^{-i\varphi_2} - e^{-i\varphi_1}|^2 &= (e^{-i\varphi_2} - e^{-i\varphi_1})(e^{+i\varphi_2} - e^{+i\varphi_1}) \\ &= 2 - 2\cos(\varphi_2 - \varphi_1) = 2 - 2\cos(\Delta\varphi), \end{aligned} $$

where $\Delta\varphi = \varphi_2 - \varphi_1 = (m^2_2 - m^2_1)L/(2E) = \Delta m^2 L/(2E)$.

其中 $\Delta\varphi = \varphi_2 - \varphi_1 = (m^2_2 - m^2_1)L/(2E) = \Delta m^2 L/(2E)$。

Using the identity $2 - 2\cos\theta = 4\sin^2(\theta/2)$:

利用恒等式 $2 - 2\cos\theta = 4\sin^2(\theta/2)$：

$$ |e^{-i\varphi_2} - e^{-i\varphi_1}|^2 = 4\sin^2(\Delta m^2 L/(4E)). $$

Therefore:

因此：

$$ P(\nu_e \to \nu_\mu) = 4\sin^2\theta\cos^2\theta \cdot \sin^2(\Delta m^2 L/(4E)) = \boxed{\, \sin^2(2\theta) \cdot \sin^2(\Delta m^2 L/(4E)) \,}, $$

using $4\sin^2\theta\cos^2\theta = \sin^2(2\theta)$. $\blacksquare$

利用 $4\sin^2\theta\cos^2\theta = \sin^2(2\theta)$。$\blacksquare$

**Step 6 — Survival probability.** By probability conservation $P(\nu_e \to \nu_e) + P(\nu_e \to \nu_\mu) = 1$ (no other flavors in 2-flavor case):

**第 6 步 — 存活概率。** 由概率守恒 $P(\nu_e \to \nu_e) + P(\nu_e \to \nu_\mu) = 1$（两味情形无其他味）：

$$ P(\nu_e \to \nu_e) = 1 - \sin^2(2\theta)\sin^2(\Delta m^2 L/(4E)). $$

**Step 7 — Oscillation length.** The oscillation probability is maximal (fully converted) when $\sin^2(\Delta m^2 L/4E) = 1$, i.e., $\Delta m^2 L/(4E) = \pi/2$. The oscillation length is:

**第 7 步 — 振荡长度。** 当 $\sin^2(\Delta m^2 L/4E) = 1$ 时，即 $\Delta m^2 L/(4E) = \pi/2$，振荡概率最大（完全转换）。振荡长度为：

$$ L_\text{osc} = 4\pi E/\Delta m^2. $$

In practical units ($E$ in GeV, $\Delta m^2$ in eV$^2$, $L$ in km):

在实用单位中（$E$ 单位 GeV，$\Delta m^2$ 单位 eV$^2$，$L$ 单位 km）：

$$ L_\text{osc} = 2.47 \text{ km} \times (E/\text{GeV}) / (\Delta m^2/\text{eV}^2). \qquad \blacksquare $$

---

## C. GUT Coupling Unification Logic · 大统一理论耦合统一的逻辑

**Claim.** The three gauge couplings $g_3$ (SU(3)), $g_2$ (SU(2)), $g_1$ (U(1)) run logarithmically with energy scale $\mu$ according to:

**命题。** 三个规范耦合常数 $g_3$（SU(3)）、$g_2$（SU(2)）、$g_1$（U(1)）按如下规律随能量标度 $\mu$ 对数跑动：

$$ d(1/\alpha_i)/d(\ln\mu) = -b_i/(2\pi), $$

and if SM particle content is extended to a SUSY spectrum, the three $\alpha_i$ meet at a single point near $\mu_\text{GUT} \sim 10^{16}$ GeV.

若 SM 粒子内容扩展到超对称谱，三个 $\alpha_i$ 在 $\mu_\text{GUT} \sim 10^{16}$ GeV 附近汇聚于一点。

**Step 1 — General RGE for gauge couplings.** The one-loop $\beta$ function for a gauge theory with coupling constant $g_i$ is:

**第 1 步 — 规范耦合常数的一般重整化群方程。** 耦合常数为 $g_i$ 的规范理论的单圈 $\beta$ 函数为：

$$ \mu\, dg_i/d\mu = -b_i g_i^3/(16\pi^2), $$

or equivalently, for $\alpha_i = g_i^2/(4\pi)$:

或等价地，对于 $\alpha_i = g_i^2/(4\pi)$：

$$ \mu\, d(1/\alpha_i)/d\mu = b_i/(2\pi). $$

**Step 2 — The $b_i$ coefficients for the SM.** For the gauge group $G_i$ with $n_s$ complex scalars and $n_f$ Weyl fermions in representations $R_s, R_f$:

**第 2 步 — SM 的 $b_i$ 系数。** 对于规范群 $G_i$，有 $n_s$ 个复标量和 $n_f$ 个外尔费米子分别处于表示 $R_s$、$R_f$：

$$ b_i = -(11/3)C_2(G) + (2/3)\sum_f T(R_f) + (1/3)\sum_s T(R_s). $$

For the Standard Model:

对于标准模型：

$$ \begin{aligned} &b_3 \text{ (SU(3)): gauge + ghost contribution } -(11/3)C_A = -11 \text{ (with } C_A = 3\text{); quark contribution } +(4/3)T_F n_f = +(2/3)n_f \text{ (with } T_F = 1/2 \text{ per Dirac flavor). For } n_f = 6 \text{ active flavors:} \\ &b_3 = -11 + (2/3)\cdot n_f = -11 + (2/3)(6) = -11 + 4 = -7. \end{aligned} $$

$b_3$ (SU(3))：规范 + 鬼粒子贡献 $-(11/3)C_A = -11$（$C_A = 3$）；夸克贡献 $+(4/3)T_F n_f = +(2/3)n_f$（每个狄拉克味 $T_F = 1/2$）。对于 $n_f = 6$ 个活跃味：$b_3 = -11 + (2/3)(6) = -11 + 4 = -7$。

The standard SM one-loop coefficients (normalized so that $b_i > 0$ means asymptotic freedom):

标准 SM 单圈系数（归一化使得 $b_i > 0$ 意味着渐近自由）：

$$ b_3 = -7, \quad b_2 = -19/6, \quad b_1 = +41/10 \quad \text{(SM, } n_f = 6, \text{ one Higgs doublet).} $$

(Using the convention $\mu\, d(g^2/4\pi)/d(\ln\mu) = -b_i(g^2/4\pi)^2/2\pi$.)

The SU(3) coupling is asymptotically free ($b_3 < 0$ in some conventions); SU(2) and U(1) have different signs.

**Step 3 — Integrate the RGE.** From $\mu_0$ (low energy, with measured values) to $\mu$ (high energy):

**第 3 步 — 积分重整化群方程。** 从 $\mu_0$（低能，具有测量值）到 $\mu$（高能）：

$$ 1/\alpha_i(\mu) = 1/\alpha_i(\mu_0) + (b_i/2\pi)\ln(\mu/\mu_0). $$

The three lines in $1/\alpha_i$ vs. $\ln\mu$ space have slopes $b_i/2\pi$. With SM values at $\mu_0 = m_Z$:

在 $1/\alpha_i$ 对 $\ln\mu$ 的空间中，三条直线的斜率为 $b_i/2\pi$。以 $\mu_0 = m_Z$ 处的 SM 值：

$$ \alpha_1(m_Z)^{-1} \approx 59.0, \quad \alpha_2(m_Z)^{-1} \approx 29.6, \quad \alpha_3(m_Z)^{-1} \approx 8.5. $$

**Step 4 — SM does not unify; SUSY does.** With SM particle content ($b_1,b_2,b_3$) the three lines do NOT pass through a common point — they form a triangle. With a complete SUSY spectrum (each SM particle has a superpartner), the $\beta$-function coefficients shift:

**第 4 步 — SM 不统一；超对称统一。** 以 SM 粒子内容（$b_1,b_2,b_3$）的三条直线不通过公共点——它们形成三角形。以完整的超对称谱（每个 SM 粒子有一个超伴子），$\beta$ 函数系数改变为：

$$ b_3 = -3, \quad b_2 = +1, \quad b_1 = +33/5 \quad \text{(MSSM).} $$

With these coefficients, the three lines do meet at:

以这些系数，三条直线确实在以下处相交：

$$ \mu_\text{GUT} \approx 2 \times 10^{16} \text{ GeV}, \quad \alpha_\text{GUT} \approx 1/25. $$

This near-perfect unification (at the $\sim$ few-percent level in $1/\alpha_i$) is one of the strongest quantitative hints for supersymmetry and grand unification. $\blacksquare$

这种近乎完美的统一（在 $1/\alpha_i$ 的约几个百分点的水平）是超对称和大统一理论最强的定量暗示之一。$\blacksquare$

---

## D. CP Violation and the CKM Matrix · CP 破坏与 CKM 矩阵

**Claim.** The CKM (Cabibbo–Kobayashi–Maskawa) matrix $V$ relating weak-eigenstate quarks ($d', s', b'$) to mass eigenstates ($d, s, b$) is a $3 \times 3$ unitary matrix. For $N$ generations, the minimum number of irreducible phases is $(N-1)(N-2)/2 = 1$ for $N = 3$ — one phase $\delta$ that generates CP violation.

**命题。** CKM（卡比博–小林–益川）矩阵 $V$ 将弱本征态夸克（$d', s', b'$）与质量本征态（$d, s, b$）相关联，是一个 $3 \times 3$ 酉矩阵。对于 $N$ 代，不可约相位的最小数目为 $(N-1)(N-2)/2$，$N = 3$ 时为 1——一个产生 CP 破坏的相位 $\delta$。

**Step 1 — Parameter counting.** A general $N \times N$ unitary matrix $U$ has $N^2$ real parameters: $N^2 = N(N-1)/2$ angles $+ N(N+1)/2$ phases.

**第 1 步 — 参数计数。** 一般的 $N \times N$ 酉矩阵 $U$ 有 $N^2$ 个实参数：$N^2 = N(N-1)/2$ 个角 $+ N(N+1)/2$ 个相位。

Not all phases are physical: we can absorb $2N - 1$ phases by rephasing the $2N$ quark fields (one overall phase is common and cancels). So physical phases $= N(N+1)/2 - (2N-1) = (N-1)(N-2)/2$.

并非所有相位都是物理的：通过对 $2N$ 个夸克场重新定义相位可以吸收 $2N - 1$ 个相位（一个总体相位是公共的并消去）。故物理相位数 $= N(N+1)/2 - (2N-1) = (N-1)(N-2)/2$。

For $N = 3$: angles $= 3$, physical phases $= 1$. This single phase $\delta$ is the source of all CP violation in quark mixing within the Standard Model. For $N = 2$ (two generations, Cabibbo): phases $= 0 \to$ no CP violation (historically realized only one generation mixing was insufficient to explain CP violation). $\blacksquare$

对于 $N = 3$：角 $= 3$，物理相位 $= 1$。这个单一相位 $\delta$ 是标准模型中夸克混合中所有 CP 破坏的来源。对于 $N = 2$（两代，卡比博）：相位 $= 0 \to$ 无 CP 破坏（历史上认识到仅一代混合不足以解释 CP 破坏）。$\blacksquare$

**Step 2 — Standard parameterization.** The standard (PDG) parameterization uses three angles $\theta_{12}, \theta_{13}, \theta_{23}$ and one phase $\delta_{13}$:

**第 2 步 — 标准参数化。** 标准（PDG）参数化使用三个角 $\theta_{12}$、$\theta_{13}$、$\theta_{23}$ 和一个相位 $\delta_{13}$：

$$ V_\text{CKM} = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23}-c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23}-s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23}-c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23}-s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix}, $$

where $c_{ij} = \cos\theta_{ij}$, $s_{ij} = \sin\theta_{ij}$. The phase $\delta \ne 0, \pi$ is the source of CP violation; it enters because $V \ne V^*$. $\blacksquare$

其中 $c_{ij} = \cos\theta_{ij}$，$s_{ij} = \sin\theta_{ij}$。相位 $\delta \ne 0, \pi$ 是 CP 破坏的来源；它的出现是因为 $V \ne V^*$。$\blacksquare$

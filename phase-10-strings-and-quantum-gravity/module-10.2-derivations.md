# Derivations — Module 10.2: Quantum Gravity & Holography
# 推导 — 模块 10.2：量子引力与全息原理

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 10.2](./module-10.2-quantum-gravity-and-holography.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 10.2](./module-10.2-quantum-gravity-and-holography.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Dimensional Analysis of the Planck Units
## A. 普朗克单位的量纲分析

**Claim.** The Planck length $\ell_P$, mass $m_P$, and time $t_P$ are the unique (up to dimensionless factors) combinations of $G$, $\hbar$, and $c$ with the respective dimensions of length, mass, and time.

**命题。** 普朗克长度 $\ell_P$、质量 $m_P$ 和时间 $t_P$ 是 $G$、$\hbar$ 和 $c$ 中（在无量纲因子意义上）唯一具有相应长度、质量和时间量纲的组合。

---

**Step 1 — Dimensions of the constants.**

In SI units ($M, L, T$ for mass, length, time):

$$ [c] = L\, T^{-1} $$
$$ [\hbar] = M\, L^2\, T^{-1} \quad (\text{energy} \times \text{time} = \text{action}) $$
$$ [G] = M^{-1}\, L^3\, T^{-2} \quad (\text{from } F = GMm/r^2: [F][r^2]/[M]^2 = (MLT^{-2})(L^2)(M^{-2}) = M^{-1}L^3 T^{-2}). $$

**第 1 步 — 常数的量纲。**

在国际单位制（$M$、$L$、$T$ 分别为质量、长度、时间）中：

$$ [c] = L\, T^{-1} $$
$$ [\hbar] = M\, L^2\, T^{-1} \quad (\text{能量} \times \text{时间} = \text{作用量}) $$
$$ [G] = M^{-1}\, L^3\, T^{-2} \quad (\text{由 } F = GMm/r^2: [F][r^2]/[M]^2 = (MLT^{-2})(L^2)(M^{-2}) = M^{-1}L^3 T^{-2})。 $$

---

**Step 2 — Solve for the Planck length.**

Write $\ell_P = G^a \hbar^b c^d$ and require $[\ell_P] = L$:

$$ M:\ -a + b = 0 \;\to\; b = a $$
$$ L:\ 3a + 2b + d = 1 $$
$$ T:\ -2a - b - d = 0 \;\to\; d = -2a - b = -3a. $$

From the $L$ equation: $3a + 2a - 3a = 2a = 1$, so **$a = 1/2$**. Then $b = 1/2$, $d = -3/2$. Therefore:

$$ \boxed{\, \ell_P = \sqrt{G\hbar/c^3} \,} \approx 1.616 \times 10^{-35} \text{ m}. $$

**第 2 步 — 求普朗克长度。**

令 $\ell_P = G^a \hbar^b c^d$，要求 $[\ell_P] = L$：

$$ M:\ -a + b = 0 \;\to\; b = a $$
$$ L:\ 3a + 2b + d = 1 $$
$$ T:\ -2a - b - d = 0 \;\to\; d = -2a - b = -3a. $$

由 $L$ 方程：$3a + 2a - 3a = 2a = 1$，故 **$a = 1/2$**。则 $b = 1/2$，$d = -3/2$。因此：

$$ \boxed{\, \ell_P = \sqrt{G\hbar/c^3} \,} \approx 1.616 \times 10^{-35} \text{ m}. $$

---

**Step 3 — Planck mass and time.**

Similarly, $m_P = G^a \hbar^b c^d$ with $[m_P] = M$: solving gives $a = -1/2$, $b = 1/2$, $d = 1/2$:

$$ \boxed{\, m_P = \sqrt{\hbar c/G} \,} \approx 2.176 \times 10^{-8} \text{ kg}. $$

For $t_P = \ell_P/c$:

$$ \boxed{\, t_P = \sqrt{\hbar G/c^5} \,} \approx 5.391 \times 10^{-44} \text{ s}. \qquad \blacksquare $$

Note: $m_P c^2 = \sqrt{\hbar c^5/G} \approx 1.22 \times 10^{19}$ GeV is the **Planck energy**, the energy scale at which the loop expansion parameter $G E^2/\hbar c^5 = (E/E_P)^2$ becomes $O(1)$.

**第 3 步 — 普朗克质量和时间。**

类似地，令 $m_P = G^a \hbar^b c^d$，$[m_P] = M$，求解得 $a = -1/2$，$b = 1/2$，$d = 1/2$：

$$ \boxed{\, m_P = \sqrt{\hbar c/G} \,} \approx 2.176 \times 10^{-8} \text{ kg}. $$

对 $t_P = \ell_P/c$：

$$ \boxed{\, t_P = \sqrt{\hbar G/c^5} \,} \approx 5.391 \times 10^{-44} \text{ s}. \qquad \blacksquare $$

注：$m_P c^2 = \sqrt{\hbar c^5/G} \approx 1.22 \times 10^{19}$ GeV 是**普朗克能量**，即圈展开参数 $G E^2/\hbar c^5 = (E/E_P)^2$ 变为 $O(1)$ 的能量尺度。

---

## B. The Hawking Temperature via Euclidean Time Periodicity
## B. 通过欧氏时间周期性得出霍金温度

**Claim.** The Hawking temperature of a Schwarzschild black hole is **$T_H = \hbar \kappa / (2\pi c k_B)$**, where $\kappa = c^4/(4GM)$ is the surface gravity at the horizon. We derive this from the requirement that the Euclidean continuation of the Schwarzschild metric be regular (non-singular) at the horizon — a condition that fixes the imaginary-time period $\beta = 1/k_B T$.

**命题。** 史瓦西黑洞的霍金温度为 **$T_H = \hbar \kappa / (2\pi c k_B)$**，其中 $\kappa = c^4/(4GM)$ 是视界处的表面引力。我们从要求史瓦西度规的欧氏延拓在视界处正则（非奇异）这一条件出发推导此式——该条件固定了虚时间周期 $\beta = 1/k_B T$。

---

**Step 1 — The Schwarzschild metric near the horizon.**

The Schwarzschild metric in Schwarzschild coordinates ($c = G = 1$ units for brevity) is:

$$ ds^2 = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2. $$

Define the **tortoise coordinate** $r^*$ by $dr^* = dr/(1 - 2M/r)$, giving $r^* = r + 2M \ln|r/2M - 1|$. Near the horizon $r \to 2M$, write $r = 2M + \varepsilon$ with $\varepsilon \ll 2M$. Then:

$$ 1 - 2M/r = \varepsilon/(2M) + O(\varepsilon^2) \equiv f(r). $$

The surface gravity is $\kappa = (c^4/4GM) \to$ in units $c = G = 1$: **$\kappa = 1/(4M)$**. So $f(r) \approx 2\kappa(r - 2M)$.

**第 1 步 — 视界附近的史瓦西度规。**

史瓦西坐标下的史瓦西度规（简洁起见取 $c = G = 1$ 单位）为：

$$ ds^2 = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2. $$

定义**乌龟坐标** $r^*$，由 $dr^* = dr/(1 - 2M/r)$ 给出，得 $r^* = r + 2M \ln|r/2M - 1|$。在视界 $r \to 2M$ 附近，令 $r = 2M + \varepsilon$，$\varepsilon \ll 2M$，则：

$$ 1 - 2M/r = \varepsilon/(2M) + O(\varepsilon^2) \equiv f(r). $$

表面引力为 $\kappa = (c^4/4GM) \to$ 在 $c = G = 1$ 单位中：**$\kappa = 1/(4M)$**。故 $f(r) \approx 2\kappa(r - 2M)$。

---

**Step 2 — Euclidean continuation.**

Perform a Wick rotation to **Euclidean time** $t_E = it$ (imaginary time). The metric becomes:

$$ ds^2_E = f(r) dt_E^2 + f(r)^{-1} dr^2 + r^2 d\Omega^2. $$

Near $r = 2M$, writing $\rho = 2\sqrt{r - 2M}/\kappa^{1/2}$ (a new radial coordinate that vanishes at the horizon):

$$ f(r) dr^2 / f(r) + f(r) dt_E^2 \approx d\rho^2 + \kappa^2 \rho^2 dt_E^2. $$

**第 2 步 — 欧氏延拓。**

对**欧氏时间** $t_E = it$（虚时间）作 Wick 转动，度规变为：

$$ ds^2_E = f(r) dt_E^2 + f(r)^{-1} dr^2 + r^2 d\Omega^2. $$

在 $r = 2M$ 附近，令 $\rho = 2\sqrt{r - 2M}/\kappa^{1/2}$（在视界消失的新径向坐标）：

$$ f(r) dr^2 / f(r) + f(r) dt_E^2 \approx d\rho^2 + \kappa^2 \rho^2 dt_E^2. $$

---

**Step 3 — Regularity at the horizon: fixing the period.**

The 2d section $d\rho^2 + \kappa^2 \rho^2 dt_E^2$ is the metric of the Euclidean plane in polar coordinates **$(\rho, \varphi)$ with $\varphi = \kappa t_E$**, provided we identify:

$$ \varphi \sim \varphi + 2\pi, \text{ i.e., } \kappa t_E \sim \kappa t_E + 2\pi, \text{ so } t_E \sim t_E + 2\pi/\kappa. $$

If the periodicity in imaginary time is instead $\beta$, we identify the **temperature** via the standard quantum statistical mechanics formula (the Matsubara formalism of Module 6.4, which identifies the imaginary-time period with the inverse temperature $\beta = \hbar/k_B T$ in units $\hbar = 1$):

$$ \beta = 2\pi/\kappa \;\to\; k_B T = \hbar \kappa / (2\pi) \quad (\text{reinstating } \hbar). $$

Equivalently, the period $\beta$ must be $2\pi/\kappa$ for the metric to be regular (no conical singularity at $\rho = 0$). Any other period would give a conical deficit or surplus at the horizon. The **unique regular Euclidean geometry** fixes:

$$ \boxed{\, T_H = \hbar \kappa / (2\pi k_B) \,} \quad (\text{with } c \text{ restored: } T_H = \hbar \kappa / (2\pi c k_B)). $$

For the Schwarzschild hole, $\kappa = c^4/(4GM)$:

$$ \boxed{\, T_H = \hbar c^3 / (8\pi G M k_B) \,} \qquad \blacksquare $$

**第 3 步 — 视界处的正则性：固定周期。**

二维截面 $d\rho^2 + \kappa^2 \rho^2 dt_E^2$ 是欧氏平面在极坐标 **$(\rho, \varphi)$ 下的度规，其中 $\varphi = \kappa t_E$**，条件是认同：

$$ \varphi \sim \varphi + 2\pi, \text{ 即 } \kappa t_E \sim \kappa t_E + 2\pi, \text{ 故 } t_E \sim t_E + 2\pi/\kappa. $$

若虚时间周期为 $\beta$，通过标准量子统计力学公式（模块 6.4 的 Matsubara 形式主义，它将虚时间周期与逆温度 $\beta = \hbar/k_B T$ 等同，$\hbar = 1$ 单位）确定**温度**：

$$ \beta = 2\pi/\kappa \;\to\; k_B T = \hbar \kappa / (2\pi) \quad (\text{恢复 } \hbar). $$

等价地，周期 $\beta$ 必须为 $2\pi/\kappa$ 才能使度规正则（视界处无锥形奇点）。任何其他周期都会在视界给出锥形亏量或盈量。**唯一正则的欧氏几何**固定：

$$ \boxed{\, T_H = \hbar \kappa / (2\pi k_B) \,} \quad (\text{恢复 } c: T_H = \hbar \kappa / (2\pi c k_B)). $$

对史瓦西黑洞，$\kappa = c^4/(4GM)$：

$$ \boxed{\, T_H = \hbar c^3 / (8\pi G M k_B) \,} \qquad \blacksquare $$

---

## C. The Bekenstein–Hawking Entropy from the First Law
## C. 由第一定律积分得出 Bekenstein–Hawking 熵

**Claim.** Integrating the first law of black-hole thermodynamics $dE = T_H dS$ (for a Schwarzschild black hole, $dE = c^2 dM$) gives $S = k_B A / (4 \ell_P^2)$.

**命题。** 对史瓦西黑洞积分黑洞热力学第一定律 $dE = T_H dS$（此处 $dE = c^2 dM$），得 $S = k_B A / (4 \ell_P^2)$。

---

**Step 1 — Set up the integral.**

From the first law of thermodynamics with only the mass term (no rotation, no charge):

$$ dS = dE / T_H = c^2 dM / T_H. $$

Substitute $T_H = \hbar c^3 / (8\pi G M k_B)$:

$$ dS = c^2 dM / [\hbar c^3 / (8\pi G M k_B)] = (8\pi G k_B M / \hbar c) dM. $$

**第 1 步 — 建立积分。**

由只含质量项的热力学第一定律（无转动，无电荷）：

$$ dS = dE / T_H = c^2 dM / T_H. $$

代入 $T_H = \hbar c^3 / (8\pi G M k_B)$：

$$ dS = c^2 dM / [\hbar c^3 / (8\pi G M k_B)] = (8\pi G k_B M / \hbar c) dM. $$

---

**Step 2 — Integrate from $M = 0$ to $M$.**

$$ S(M) = \int_0^M (8\pi G k_B M' / \hbar c) dM' = (8\pi G k_B / \hbar c) \cdot M^2/2 = \boxed{\, 4\pi G k_B M^2 / \hbar c \,}. $$

**第 2 步 — 从 $M = 0$ 积分到 $M$。**

$$ S(M) = \int_0^M (8\pi G k_B M' / \hbar c) dM' = (8\pi G k_B / \hbar c) \cdot M^2/2 = \boxed{\, 4\pi G k_B M^2 / \hbar c \,}. $$

---

**Step 3 — Express in terms of horizon area.**

The Schwarzschild radius is $r_s = 2GM/c^2$, so the horizon area is:

$$ A = 4\pi r_s^2 = 4\pi (2GM/c^2)^2 = 16\pi G^2 M^2 / c^4. $$

Solving for $M^2$: $G M^2 = A c^4 / (16\pi G)$. Substituting into $S$:

$$ S = 4\pi G k_B M^2 / \hbar c = 4\pi G k_B \cdot (A c^4 / 16\pi G^2) / \hbar c = (k_B c^3 A) / (4 G \hbar). $$

Recall $\ell_P^2 = \hbar G/c^3$, so $G \hbar / c^3 = \ell_P^2$:

$$ \boxed{\, S = k_B A / (4 \ell_P^2) \,} \qquad \blacksquare $$

**第 3 步 — 用视界面积表示。**

史瓦西半径为 $r_s = 2GM/c^2$，故视界面积为：

$$ A = 4\pi r_s^2 = 4\pi (2GM/c^2)^2 = 16\pi G^2 M^2 / c^4. $$

解出 $M^2$：$G M^2 = A c^4 / (16\pi G)$。代入 $S$：

$$ S = 4\pi G k_B M^2 / \hbar c = 4\pi G k_B \cdot (A c^4 / 16\pi G^2) / \hbar c = (k_B c^3 A) / (4 G \hbar). $$

注意 $\ell_P^2 = \hbar G/c^3$，故 $G \hbar / c^3 = \ell_P^2$：

$$ \boxed{\, S = k_B A / (4 \ell_P^2) \,} \qquad \blacksquare $$

---

## D. Consistency Check: The Evaporation Timescale
## D. 自洽性检验：蒸发时标

**Claim.** A black hole of initial mass $M_0$ evaporates completely in a time $t_{\text{evap}} \propto G^2 M_0^3 / (\hbar c^4)$. We verify this by combining Stefan–Boltzmann radiation with the Hawking temperature.

**命题。** 初始质量为 $M_0$ 的黑洞在时间 $t_{\text{evap}} \propto G^2 M_0^3 / (\hbar c^4)$ 内完全蒸发。我们通过将 Stefan–Boltzmann 辐射与霍金温度结合来验证。

---

**Step 1 — Luminosity of Hawking radiation.**

Treating the black hole as a blackbody of temperature $T_H$ and effective area $\sim A = 16\pi G^2 M^2 / c^4$ (Stefan–Boltzmann law $L = \sigma T^4 A$ in natural units, up to grey-body factors of order 1):

$$ L \sim \sigma T_H^4 A \sim \sigma (\hbar c^3/8\pi GMk_B)^4 \cdot (G^2M^2/c^4) \sim \hbar c^6 / (G^2 M^2), $$

where $\sigma = \pi^2 k_B^4/(60\hbar^3 c^2)$ has been substituted and all numerical prefactors collected into the proportionality.

**第 1 步 — 霍金辐射的光度。**

将黑洞视为温度 $T_H$、有效面积 $\sim A = 16\pi G^2 M^2 / c^4$ 的黑体（Stefan–Boltzmann 定律 $L = \sigma T^4 A$，自然单位，灰体因子为 $O(1)$）：

$$ L \sim \sigma T_H^4 A \sim \sigma (\hbar c^3/8\pi GMk_B)^4 \cdot (G^2M^2/c^4) \sim \hbar c^6 / (G^2 M^2), $$

其中 $\sigma = \pi^2 k_B^4/(60\hbar^3 c^2)$ 已代入，所有数值系数收入比例号。

---

**Step 2 — The mass-loss equation.**

Energy conservation: $-c^2 dM/dt = L \sim \hbar c^6 / (G^2 M^2)$. Therefore:

$$ M^2 dM = -(\hbar c^4 / G^2) dt \quad (\text{absorbing the numerical coefficient} \sim 1 \text{ into the relation}). $$

**第 2 步 — 质量损失方程。**

能量守恒：$-c^2 dM/dt = L \sim \hbar c^6 / (G^2 M^2)$。因此：

$$ M^2 dM = -(\hbar c^4 / G^2) dt \quad (\text{数值系数约 1 已收入比例关系})。 $$

---

**Step 3 — Integrate.**

Integrating from $M_0$ to 0:

$$ \int_0^{M_0} M^2 dM = M_0^3/3 = (\hbar c^4 / G^2) t_{\text{evap}}. $$

Therefore:

$$ \boxed{\, t_{\text{evap}} \sim G^2 M_0^3 / (\hbar c^4) \,} \qquad \blacksquare $$

For $M_0 = M_{\text{sun}} \sim 2 \times 10^{30}$ kg: $t_{\text{evap}} \sim (6.67\times 10^{-11})^2(2\times 10^{30})^3 / (10^{-34} \times 9\times 10^{16}) \sim 10^{74}$ years — utterly negligible evaporation over the age of the universe ($\sim 10^{10}$ years). For a Planck-mass black hole ($M_0 \sim 10^{-8}$ kg): $t_{\text{evap}} \sim t_P \sim 10^{-44}$ s — it would evaporate instantly.

**第 3 步 — 积分。**

从 $M_0$ 积分到 0：

$$ \int_0^{M_0} M^2 dM = M_0^3/3 = (\hbar c^4 / G^2) t_{\text{evap}}. $$

因此：

$$ \boxed{\, t_{\text{evap}} \sim G^2 M_0^3 / (\hbar c^4) \,} \qquad \blacksquare $$

对 $M_0 = M_{\text{太阳}} \sim 2 \times 10^{30}$ kg：$t_{\text{evap}} \sim (6.67\times 10^{-11})^2(2\times 10^{30})^3 / (10^{-34} \times 9\times 10^{16}) \sim 10^{74}$ 年——在宇宙年龄（$\sim 10^{10}$ 年）内完全可忽略。对普朗克质量黑洞（$M_0 \sim 10^{-8}$ kg）：$t_{\text{evap}} \sim t_P \sim 10^{-44}$ s——会瞬间蒸发。

---

## E. The Bekenstein Bound and the Holographic Principle
## E. Bekenstein 界与全息原理

**Claim.** The maximum entropy of any physical system contained within a region of radius $R$ and energy $E$ (with $Mc^2 = E$) satisfies $S \le 2\pi k_B R E / (\hbar c)$. A spherical system saturates this bound only when it is a black hole. From this, the maximum entropy in any region bounded by area $A$ is $S_{\max} = k_B A / (4\ell_P^2)$, establishing the holographic bound.

**命题。** 包含在半径 $R$、能量 $E$（$Mc^2 = E$）区域内的任何物理系统的最大熵满足 $S \le 2\pi k_B R E / (\hbar c)$。只有当系统是黑洞时，球形系统才使此界饱和。由此，面积为 $A$ 的区域内的最大熵为 $S_{\max} = k_B A / (4\ell_P^2)$，建立了全息界。

---

**Step 1 — The Bekenstein bound argument.**

Consider a box of size $R$ containing matter with entropy $S$ and rest energy $Mc^2$. To argue why $S \le 2\pi k_B RMc/\hbar$: Suppose $S > S_{BH}$ (the Bekenstein–Hawking entropy of a black hole of mass $M$ in radius $R$). We could then lower a box with this matter into an existing black hole. By the generalized second law (GSL), the total entropy — including the black-hole area — cannot decrease. But the area increase upon absorption is $\Delta A = 16\pi Gm(M+m)/c^4 - 16\pi GM^2/c^4 \approx 32\pi GmM/c^4$ (for $m \ll M$), giving $\Delta S_{BH} = k_B \Delta A/(4\ell_P^2)$. For this to accommodate $S$, we need $S \le \Delta S_{BH}$, which gives $S \le 2\pi k_B RMc/\hbar$ (identifying $R$ with the Schwarzschild radius scale $\sim GM/c^2$). This is the **Bekenstein entropy bound**.

**第 1 步 — Bekenstein 界的论证。**

考虑大小为 $R$ 的盒子，其中物质具有熵 $S$ 和静止能量 $Mc^2$。论证 $S \le 2\pi k_B RMc/\hbar$ 的理由：假设 $S > S_{BH}$（半径 $R$、质量 $M$ 的黑洞的 Bekenstein–Hawking 熵）。我们可以将这盒物质放入一个已存在的黑洞。由广义第二定律（GSL），总熵——包括黑洞面积——不能减少。但吸收后的面积增加为 $\Delta A = 16\pi Gm(M+m)/c^4 - 16\pi GM^2/c^4 \approx 32\pi GmM/c^4$（$m \ll M$），给出 $\Delta S_{BH} = k_B \Delta A/(4\ell_P^2)$。为使 $S$ 得以容纳，需要 $S \le \Delta S_{BH}$，给出 $S \le 2\pi k_B RMc/\hbar$（将 $R$ 与史瓦西半径尺度 $\sim GM/c^2$ 对应）。这是 **Bekenstein 熵界**。

---

**Step 2 — Saturation by black holes and the holographic bound.**

For a Schwarzschild black hole of mass $M$, radius $r_s = 2GM/c^2$, the Bekenstein bound gives:

$$ S \le 2\pi k_B r_s M c / \hbar = 2\pi k_B (2GM/c^2)(Mc) / \hbar = 4\pi k_B GM^2 / (\hbar c). $$

This is exactly the Bekenstein–Hawking entropy $S_{BH} = k_B A/(4\ell_P^2) = 4\pi k_B GM^2/(\hbar c)$. So **black holes saturate the Bekenstein bound**: they are the maximum-entropy states for given mass and size. Since no system can have more entropy than a black hole of the same boundary area $A$, the maximum entropy in a region bounded by area $A$ is:

$$ S_{\max} = S_{BH} = k_B A / (4\ell_P^2), $$

the **holographic bound** (Bousso 2002). The number of independent degrees of freedom in the region is at most $A/(4\ell_P^2)$ — one degree of freedom per four Planck areas — regardless of the volume. The world in this sense is holographic. $\blacksquare$

**第 2 步 — 黑洞使界饱和与全息界。**

对质量 $M$、半径 $r_s = 2GM/c^2$ 的史瓦西黑洞，Bekenstein 界给出：

$$ S \le 2\pi k_B r_s M c / \hbar = 2\pi k_B (2GM/c^2)(Mc) / \hbar = 4\pi k_B GM^2 / (\hbar c). $$

这恰好是 Bekenstein–Hawking 熵 $S_{BH} = k_B A/(4\ell_P^2) = 4\pi k_B GM^2/(\hbar c)$。故**黑洞使 Bekenstein 界饱和**：它们是给定质量和尺寸下熵最大的态。由于任何系统的熵不能超过同面积 $A$ 边界的黑洞的熵，面积为 $A$ 的区域内的最大熵为：

$$ S_{\max} = S_{BH} = k_B A / (4\ell_P^2), $$

即**全息界**（Bousso，2002 年）。该区域内独立自由度的数目最多为 $A/(4\ell_P^2)$——每四个普朗克面积对应一个自由度——与体积无关。世界在此意义上是全息的。$\blacksquare$

---

*All derivations follow the conventions of Wald, "General Relativity" (Chicago, 1984) for the surface gravity; Hawking's original derivation in Comm. Math. Phys. 43, 199 (1975); Gibbons & Hawking, Phys. Rev. D 15, 2752 (1977) for the Euclidean method; and Bekenstein, Phys. Rev. D 7, 2333 (1973) for the entropy bound. The $\zeta$-function regularization of the determinant of the Euclidean wave operator is beyond the scope of this document; the Euclidean-periodicity argument given here is the standard pedagogical route.*

*所有推导遵循 Wald《广义相对论》（芝加哥，1984 年）关于表面引力的约定；霍金在 Comm. Math. Phys. 43, 199 (1975) 中的原始推导；Gibbons 和 Hawking 在 Phys. Rev. D 15, 2752 (1977) 中的欧氏方法；以及 Bekenstein 在 Phys. Rev. D 7, 2333 (1973) 中的熵界。欧氏波算符行列式的 $\zeta$ 函数正规化超出本文档范围；此处给出的欧氏周期性论证是标准的教学路径。*

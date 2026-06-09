# Derivations — Module 0.4: Complex Analysis
# 推导 — 模块 0.4：复分析

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.4](./module-0.4-complex-analysis.md). Full step-by-step proofs of every non-trivial result stated there: Euler's formula from the Taylor series; the Cauchy–Riemann equations as necessary conditions for analyticity; the residue theorem for a simple pole, including the key integral $\oint dz/(z-z_0) = 2\pi i$; and evaluation of a real integral by residues. English first, then 中文.
> [模块 0.4](./module-0.4-complex-analysis.md) 的配套文档：对该模块所引用的每一个非平凡结果进行完整逐步证明：从泰勒级数推导欧拉公式；柯西–黎曼方程是解析性的必要条件；简单极点的留数定理（包括关键积分 $\oint dz/(z-z_0) = 2\pi i$）；以及用留数定理计算实数积分。先英文，后中文。

---

## A. Euler's Formula from the Taylor Series · 从泰勒级数推导欧拉公式

**Claim.** For any real $\theta$, $e^{i\theta} = \cos \theta + i \sin \theta$.

**命题。** 对任意实数 $\theta$，$e^{i\theta} = \cos \theta + i \sin \theta$。

**Step 1 — Substitute $i\theta$ into the exponential series.** From Module 0.1 the Taylor series for $e^x$ converges absolutely for all $x \in \mathbb{C}$ (the ratio test gives the same bound). Setting $x = i\theta$:

**第 1 步 — 将 $i\theta$ 代入指数级数。** 由模块 0.1，$e^x$ 的泰勒级数对所有 $x \in \mathbb{C}$ 绝对收敛（比值审敛法给出相同界）。令 $x = i\theta$：

$$ e^{i\theta} = \sum_{n=0}^{\infty} \frac{(i\theta)^n}{n!} = \sum_{n=0}^{\infty} \frac{i^n \theta^n}{n!}. $$

**Step 2 — Separate even and odd terms.** The powers of $i$ cycle with period 4: $i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, … Split the sum into even ($n = 2m$) and odd ($n = 2m+1$) terms:

**第 2 步 — 分离偶数项与奇数项。** $i$ 的幂次以 4 为周期循环：$i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, …。将级数拆分为偶数项（$n = 2m$）和奇数项（$n = 2m+1$）：

$$ \begin{aligned} \text{Even terms:} &\quad \sum_{m=0}^{\infty} \frac{i^{2m} \theta^{2m}}{(2m)!} = \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m}}{(2m)!}, \\ \text{Odd terms:} &\quad \sum_{m=0}^{\infty} \frac{i^{2m+1} \theta^{2m+1}}{(2m+1)!} = i \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+1}}{(2m+1)!}. \end{aligned} $$

$$ \begin{aligned} \text{偶数项：} &\quad \sum_{m=0}^{\infty} \frac{i^{2m} \theta^{2m}}{(2m)!} = \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m}}{(2m)!}, \\ \text{奇数项：} &\quad \sum_{m=0}^{\infty} \frac{i^{2m+1} \theta^{2m+1}}{(2m+1)!} = i \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+1}}{(2m+1)!}. \end{aligned} $$

**Step 3 — Recognize the cosine and sine series.** Comparing with the series from Module 0.1:

**第 3 步 — 识别余弦和正弦级数。** 与模块 0.1 的级数对照：

$$ \cos \theta = \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m}}{(2m)!}, \qquad \sin \theta = \sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+1}}{(2m+1)!}. $$

Therefore:

因此：

$$ \boxed{\, e^{i\theta} = \cos \theta + i \sin \theta. \,} \qquad \blacksquare $$

**Corollary 1 — Polar form.** Any complex number $z = a + bi$ can be written $z = r e^{i\theta}$ where $r = |z| = \sqrt{a^2 + b^2}$ and $\theta = \arg(z) = \arctan(b/a)$. Multiplication adds phases: $(r_1 e^{i\theta_1})(r_2 e^{i\theta_2}) = r_1 r_2 e^{i(\theta_1+\theta_2)}$.

**推论 1 — 极坐标形式。** 任意复数 $z = a + bi$ 可写成 $z = r e^{i\theta}$，其中 $r = |z| = \sqrt{a^2 + b^2}$，$\theta = \arg(z) = \arctan(b/a)$。乘法叠加相位：$(r_1 e^{i\theta_1})(r_2 e^{i\theta_2}) = r_1 r_2 e^{i(\theta_1+\theta_2)}$。

**Corollary 2 — Euler's identity.** Setting $\theta = \pi$: $e^{i\pi} = \cos \pi + i \sin \pi = -1 + 0 = -1$, i.e., $\boldsymbol{e^{i\pi} + 1 = 0}$.

**推论 2 — 欧拉恒等式。** 令 $\theta = \pi$：$e^{i\pi} = \cos \pi + i \sin \pi = -1 + 0 = -1$，即 $\boldsymbol{e^{i\pi} + 1 = 0}$。

**Corollary 3 — Inverse relations.** Adding and subtracting $e^{i\theta} = \cos \theta + i \sin \theta$ and $e^{-i\theta} = \cos \theta - i \sin \theta$:

**推论 3 — 逆关系。** 将 $e^{i\theta} = \cos \theta + i \sin \theta$ 与 $e^{-i\theta} = \cos \theta - i \sin \theta$ 相加减：

$$ \cos \theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \qquad \sin \theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}. $$

These are the standard complex representations of the real trigonometric functions, central to Fourier analysis.

这是实三角函数的标准复数表示，是傅里叶分析的核心。

---

## B. The Cauchy–Riemann Equations as Necessary Conditions for Analyticity · 柯西–黎曼方程是解析性的必要条件

**Claim.** If $f(z) = u(x, y) + i v(x, y)$ is complex-differentiable at $z_0 = x_0 + iy_0$, then at that point:

**命题。** 若 $f(z) = u(x, y) + i v(x, y)$ 在 $z_0 = x_0 + iy_0$ 处复可微，则在该点：

$$ \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}. $$

**Step 1 — Definition of complex differentiability.** $f$ is complex-differentiable at $z_0$ if the limit

**第 1 步 — 复可微性的定义。** $f$ 在 $z_0$ 处复可微是指以下极限存在：

$$ f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z} $$

exists and is the same regardless of the direction in which $\Delta z \to 0$ in $\mathbb{C}$.

且该极限与 $\Delta z \to 0$ 在 $\mathbb{C}$ 中的趋近方向无关。

**Step 2 — Approach along the real axis.** Let $\Delta z = \Delta x$ (real), so $\Delta z \to 0$ means $\Delta x \to 0$:

**第 2 步 — 沿实轴趋近。** 令 $\Delta z = \Delta x$（实数），则 $\Delta z \to 0$ 等价于 $\Delta x \to 0$：

$$ \begin{aligned} f'(z_0) &= \lim_{\Delta x \to 0} \frac{u(x_0+\Delta x, y_0) - u(x_0,y_0)}{\Delta x} + i \lim_{\Delta x \to 0} \frac{v(x_0+\Delta x, y_0) - v(x_0,y_0)}{\Delta x} \\ &= \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x}. \end{aligned} $$

**Step 3 — Approach along the imaginary axis.** Let $\Delta z = i \Delta y$ (purely imaginary), so $\Delta z \to 0$ means $\Delta y \to 0$:

**第 3 步 — 沿虚轴趋近。** 令 $\Delta z = i \Delta y$（纯虚数），则 $\Delta z \to 0$ 等价于 $\Delta y \to 0$：

$$ \begin{aligned} f'(z_0) &= \lim_{\Delta y \to 0} \frac{u(x_0, y_0+\Delta y) - u(x_0,y_0)}{i\Delta y} + i \lim_{\Delta y \to 0} \frac{v(x_0, y_0+\Delta y) - v(x_0,y_0)}{i\Delta y} \\ &= \frac{1}{i} \frac{\partial u}{\partial y} + \frac{i}{i} \frac{\partial v}{\partial y} \\ &= -i \frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}. \end{aligned} $$

(Using $1/i = -i$.)

（利用 $1/i = -i$。）

**Step 4 — Equate real and imaginary parts.** Since $f'(z_0)$ must be the same from both approaches, set the two expressions equal:

**第 4 步 — 令实部和虚部相等。** 由于 $f'(z_0)$ 从两个方向趋近必须相同，令两式相等：

$$ \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i \frac{\partial u}{\partial y}. $$

Equating real parts: $\boldsymbol{\partial u/\partial x = \partial v/\partial y}$. Equating imaginary parts: $\boldsymbol{\partial v/\partial x = -\partial u/\partial y}$. $\blacksquare$

比较实部：$\boldsymbol{\partial u/\partial x = \partial v/\partial y}$。比较虚部：$\boldsymbol{\partial v/\partial x = -\partial u/\partial y}$。$\blacksquare$

**Remark — Sufficient conditions.** The Cauchy–Riemann equations are necessary but not sufficient on their own. If additionally $u$ and $v$ have continuous first partial derivatives in a neighborhood of $z_0$ (which holds for all analytic functions), then the Cauchy–Riemann equations are also sufficient for complex differentiability there.

**说明——充分条件。** 柯西–黎曼方程是必要条件但本身不充分。若 $u$ 和 $v$ 在 $z_0$ 的某邻域内还具有连续一阶偏导数（这对所有解析函数均成立），则柯西–黎曼方程也是该点复可微的充分条件。

**Corollary — Both $u$ and $v$ are harmonic.** From the C–R equations, $\partial^2 u/\partial x^2 = \frac{\partial}{\partial x}(\partial v/\partial y) = \frac{\partial}{\partial y}(\partial v/\partial x) = -\partial^2 u/\partial y^2$ (if second partials exist and are continuous), so $\partial^2 u/\partial x^2 + \partial^2 u/\partial y^2 = 0$. Hence $\nabla^2 u = 0$ — $u$ is harmonic, and similarly for $v$. Every analytic function generates a pair of harmonic conjugates, a fact used extensively in electrostatics (Module 1.8).

**推论——$u$ 和 $v$ 均为调和函数。** 由柯西–黎曼方程，$\partial^2 u/\partial x^2 = \frac{\partial}{\partial x}(\partial v/\partial y) = \frac{\partial}{\partial y}(\partial v/\partial x) = -\partial^2 u/\partial y^2$（若二阶偏导数存在且连续），故 $\partial^2 u/\partial x^2 + \partial^2 u/\partial y^2 = 0$，即 $\nabla^2 u = 0$——$u$ 是调和函数，$v$ 同理。每个解析函数生成一对调和共轭，这一事实在静电学（模块 1.8）中被广泛使用。

---

## C. The Fundamental Integral $\oint dz/(z - z_0) = 2\pi i$ · 基本积分 $\oint dz/(z - z_0) = 2\pi i$

**Claim.** Let $C$ be a simple closed contour traversed counterclockwise that encloses the point $z_0$. Then

**命题。** 设 $C$ 是沿逆时针方向绕行的简单闭合围道，包围点 $z_0$。则

$$ \oint_C \frac{dz}{z - z_0} = 2\pi i. $$

**Step 1 — Parametrize $C$ by a circle.** Because the integrand $1/(z - z_0)$ is analytic everywhere except at $z_0$, and by Cauchy's deformation theorem the integral is unchanged if we deform $C$ to any other simple closed contour enclosing $z_0$, we may take $C$ to be the circle of radius $\varepsilon > 0$ centered at $z_0$:

**第 1 步 — 用圆来参数化 $C$。** 由于被积函数 $1/(z - z_0)$ 除 $z_0$ 外处处解析，由柯西变形定理，将 $C$ 变形为包围 $z_0$ 的任意简单闭合围道时积分不变，故可取 $C$ 为以 $z_0$ 为圆心、半径为 $\varepsilon > 0$ 的圆：

$$ z(\theta) = z_0 + \varepsilon e^{i\theta}, \quad \theta \in [0, 2\pi]. $$

**Step 2 — Compute $dz$.** Differentiating:

**第 2 步 — 计算 $dz$。** 求导：

$$ dz = i\varepsilon e^{i\theta}\,d\theta. $$

**Step 3 — Substitute.**

**第 3 步 — 代入。**

$$ \oint_C \frac{dz}{z - z_0} = \int_0^{2\pi} \frac{1}{\varepsilon e^{i\theta}} \cdot i\varepsilon e^{i\theta}\,d\theta = \int_0^{2\pi} i\,d\theta = i \cdot 2\pi = \boldsymbol{2\pi i}. \qquad \blacksquare $$

The factors $\varepsilon e^{i\theta}$ cancel exactly, so the result is independent of the radius $\varepsilon$. This is the fundamental reason why residues (which capture the behavior near a pole) control contour integrals.

因子 $\varepsilon e^{i\theta}$ 恰好约去，故结果与半径 $\varepsilon$ 无关。这正是留数（捕捉极点附近行为）控制围道积分的根本原因。

---

## D. The Residue Theorem for a Simple Pole · 简单极点的留数定理

**Setup.** Let $f(z)$ have a simple pole at $z_0$ (meaning $f(z) = g(z)/(z - z_0)$ where $g$ is analytic in a neighborhood of $z_0$ with $g(z_0) \ne 0$). The **residue** of $f$ at $z_0$ is defined as

**准备工作。** 设 $f(z)$ 在 $z_0$ 处有简单极点（即 $f(z) = g(z)/(z - z_0)$，其中 $g$ 在 $z_0$ 的某邻域内解析且 $g(z_0) \ne 0$）。$f$ 在 $z_0$ 处的**留数**定义为

$$ \operatorname{Res}(f, z_0) = \lim_{z \to z_0} (z - z_0) f(z) = g(z_0). $$

**Claim (Residue Theorem — simple pole version).** Let $C$ be a simple closed counterclockwise contour enclosing only the simple pole at $z_0$. Then

**命题（留数定理——简单极点版本）。** 设 $C$ 是逆时针方向的简单闭合围道，仅包围 $z_0$ 处的简单极点。则

$$ \oint_C f(z)\,dz = 2\pi i \cdot \operatorname{Res}(f, z_0). $$

**Step 1 — Laurent expansion.** Since $g(z)$ is analytic at $z_0$, it has a Taylor series: $g(z) = g(z_0) + g'(z_0)(z - z_0) + \cdots$. Therefore

**第 1 步 — 洛朗展开。** 由于 $g(z)$ 在 $z_0$ 处解析，它有泰勒展开：$g(z) = g(z_0) + g'(z_0)(z - z_0) + \cdots$。因此

$$ \begin{aligned} f(z) &= \frac{g(z_0)}{z - z_0} + g'(z_0) + \frac{g''(z_0)(z-z_0)}{2!} + \cdots \\ &= \frac{\operatorname{Res}(f,z_0)}{z - z_0} + h(z), \end{aligned} $$

where $h(z) = g'(z_0) + g''(z_0)(z-z_0)/2! + \cdots$ is analytic at $z_0$.

其中 $h(z) = g'(z_0) + g''(z_0)(z-z_0)/2! + \cdots$ 在 $z_0$ 处解析。

**Step 2 — Integrate term by term.** Split the contour integral:

**第 2 步 — 逐项积分。** 拆分围道积分：

$$ \oint_C f(z)\,dz = \operatorname{Res}(f,z_0) \oint_C \frac{dz}{z - z_0} + \oint_C h(z)\,dz. $$

**Step 3 — Apply Cauchy's theorem to the analytic part.** Since $h(z)$ is analytic everywhere inside and on $C$ (it has no pole), Cauchy's integral theorem gives $\oint_C h(z)\,dz = 0$.

**第 3 步 — 对解析部分应用柯西定理。** 由于 $h(z)$ 在 $C$ 内部及其上处处解析（无极点），柯西积分定理给出 $\oint_C h(z)\,dz = 0$。

**Step 4 — Apply the fundamental integral.** From Section C, $\oint_C dz/(z - z_0) = 2\pi i$. Therefore:

**第 4 步 — 应用基本积分。** 由 C 节，$\oint_C dz/(z - z_0) = 2\pi i$。因此：

$$ \boldsymbol{\oint_C f(z)\,dz = \operatorname{Res}(f, z_0) \cdot 2\pi i = 2\pi i \cdot g(z_0).} \qquad \blacksquare $$

**General statement.** If $C$ encloses finitely many poles $z_1, z_2, \ldots, z_n$, by summing the contributions from each and applying Cauchy's theorem to the remaining analytic part:

**一般陈述。** 若 $C$ 包围有限个极点 $z_1, z_2, \ldots, z_n$，对每个极点的贡献求和，并对其余解析部分应用柯西定理：

$$ \oint_C f(z)\,dz = 2\pi i \sum_k \operatorname{Res}(f, z_k). $$

---

## E. Evaluating $\oint dz/z = 2\pi i$ Directly · 直接计算 $\oint dz/z = 2\pi i$

**Claim.** $\oint_C dz/z = 2\pi i$ where $C$ is any simple closed counterclockwise contour enclosing the origin.

**命题。** $\oint_C dz/z = 2\pi i$，其中 $C$ 是任意包围原点的逆时针简单闭合围道。

This is the case $z_0 = 0$ of Section C (set $g(z) = 1$, $\operatorname{Res}(1/z, 0) = 1$), so the result follows immediately. Alternatively, by direct parametrization with $z = e^{i\theta}$, $dz = ie^{i\theta}\,d\theta$:

这是 C 节中 $z_0 = 0$ 的特例（令 $g(z) = 1$，$\operatorname{Res}(1/z, 0) = 1$），结果立即得到。另外，直接用 $z = e^{i\theta}$，$dz = ie^{i\theta}\,d\theta$ 参数化：

$$ \oint \frac{dz}{z} = \int_0^{2\pi} \frac{ie^{i\theta}}{e^{i\theta}}\,d\theta = i \int_0^{2\pi} d\theta = \boldsymbol{2\pi i}. \qquad \blacksquare $$

**Contrast with $\oint z^n\,dz$ for $n \ne -1$.** Parametrizing with $z = \varepsilon e^{i\theta}$:

**与 $n \ne -1$ 时的 $\oint z^n\,dz$ 对比。** 用 $z = \varepsilon e^{i\theta}$ 参数化：

$$ \oint z^n\,dz = \int_0^{2\pi} \varepsilon^n e^{in\theta} \cdot i\varepsilon e^{i\theta}\,d\theta = i\varepsilon^{n+1} \int_0^{2\pi} e^{i(n+1)\theta}\,d\theta. $$

For integer $n \ne -1$, $e^{i(n+1)\theta}$ completes a whole number of full cycles over $[0, 2\pi]$, so the integral is zero. This is the reason why only the $1/(z-z_0)$ term in the Laurent expansion contributes — the residue.

对整数 $n \ne -1$，$e^{i(n+1)\theta}$ 在 $[0, 2\pi]$ 上完成整数圈，故积分为零。这就是为什么洛朗展开中只有 $1/(z-z_0)$ 项有贡献——即留数。

---

## F. A Real Integral by Residues · 用留数定理计算实数积分

**Claim.** $\int_{-\infty}^{\infty} dx/(1 + x^2) = \pi$.

**命题。** $\int_{-\infty}^{\infty} dx/(1 + x^2) = \pi$。

**Step 1 — Identify the complex function.** Consider $f(z) = 1/(1 + z^2) = 1/[(z + i)(z - i)]$. The poles are at $z = \pm i$.

**第 1 步 — 确定复变函数。** 考虑 $f(z) = 1/(1 + z^2) = 1/[(z + i)(z - i)]$，极点在 $z = \pm i$。

**Step 2 — Choose a contour.** Take $C_R = [-R, R] \cup \Gamma_R$, where $\Gamma_R$ is the semicircle of radius $R$ in the upper half-plane ($\operatorname{Im}(z) \ge 0$), traversed counterclockwise. For large $R$ this encloses the pole at $z = +i$ but not $z = -i$.

**第 2 步 — 选择围道。** 取 $C_R = [-R, R] \cup \Gamma_R$，其中 $\Gamma_R$ 是上半平面（$\operatorname{Im}(z) \ge 0$）中半径为 $R$ 的半圆弧，逆时针绕行。对大 $R$，此围道包围极点 $z = +i$，但不包围 $z = -i$。

**Step 3 — Compute the residue at $z = i$.** Since the pole is simple:

**第 3 步 — 计算 $z = i$ 处的留数。** 由于是简单极点：

$$ \operatorname{Res}(f, i) = \lim_{z \to i} (z - i) \cdot \frac{1}{(z+i)(z-i)} = \frac{1}{i + i} = \frac{1}{2i}. $$

**Step 4 — Residue theorem gives the contour integral.**

**第 4 步 — 留数定理给出围道积分。**

$$ \oint_{C_R} f(z)\,dz = 2\pi i \cdot \operatorname{Res}(f, i) = 2\pi i \cdot \frac{1}{2i} = \pi. $$

**Step 5 — Show the semicircle arc vanishes as $R \to \infty$.** On $\Gamma_R$, $z = Re^{i\theta}$, $|z| = R$, so $|f(z)| = |1/(1+z^2)| \le 1/(R^2 - 1) \to 0$. The length of $\Gamma_R$ is $\pi R$. By the ML inequality ($|\int_\Gamma f\,dz| \le \max|f| \cdot \text{length}$):

**第 5 步 — 证明半圆弧在 $R \to \infty$ 时趋于零。** 在 $\Gamma_R$ 上，$z = Re^{i\theta}$，$|z| = R$，故 $|f(z)| = |1/(1+z^2)| \le 1/(R^2 - 1) \to 0$。$\Gamma_R$ 的长度为 $\pi R$。由 ML 不等式（$|\int_\Gamma f\,dz| \le \max|f| \cdot \text{长度}$）：

$$ \left|\int_{\Gamma_R} f(z)\,dz\right| \le \frac{\pi R}{R^2 - 1} \to 0 \quad \text{as } R \to \infty. $$

**Step 6 — Conclude.**

**第 6 步 — 结论。**

$$ \pi = \oint_{C_R} f(z)\,dz = \int_{-R}^{R} \frac{dx}{1+x^2} + \int_{\Gamma_R} f(z)\,dz. $$

Taking $R \to \infty$:

令 $R \to \infty$：

$$ \boxed{\, \int_{-\infty}^{\infty} \frac{dx}{1 + x^2} = \pi. \,} \qquad \blacksquare $$

**Verification.** By elementary calculus, $\int dx/(1+x^2) = \arctan(x) + C$, and $\arctan(+\infty) - \arctan(-\infty) = \pi/2 - (-\pi/2) = \pi$. ✓ The residue method and elementary methods agree.

**验证。** 用初等微积分，$\int dx/(1+x^2) = \arctan(x) + C$，而 $\arctan(+\infty) - \arctan(-\infty) = \pi/2 - (-\pi/2) = \pi$。✓ 留数法与初等方法结果一致。

**Physical context.** Integrals of this type — integrals of rational functions over the entire real line — appear in response functions, Green's functions, and Kramers–Kronig dispersion relations (Phase 6), where the poles in the complex plane encode causal structure and physical resonances.

**物理背景。** 这类积分——有理函数在整个实轴上的积分——出现在响应函数、格林函数和克喇末–克朗尼希色散关系中（第 6 阶段），其中复平面上的极点编码了因果结构和物理共振。

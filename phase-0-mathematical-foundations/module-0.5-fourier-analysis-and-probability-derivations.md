# Derivations — Module 0.5: Fourier Analysis & Probability
# 推导 — 模块 0.5：傅里叶分析与概率

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.5](./module-0.5-fourier-analysis-and-probability.md). Full step-by-step proofs of every non-trivial result: derivation of Fourier coefficients via orthogonality; the Fourier transform of a Gaussian is a Gaussian (completing the square); the convolution theorem; the Dirac delta as a Fourier representation; $\operatorname{Var} = \langle x^2\rangle - \langle x\rangle^2$; and the central limit theorem via characteristic functions. English first, then 中文.
> [模块 0.5](./module-0.5-fourier-analysis-and-probability.md) 的配套文档：对每一个非平凡结果进行完整逐步证明：通过正交性推导傅里叶系数；高斯函数的傅里叶变换仍是高斯函数（配方法）；卷积定理；狄拉克 delta 函数的傅里叶表示；$\operatorname{Var} = \langle x^2\rangle - \langle x\rangle^2$；以及通过特征函数的中心极限定理。先英文，后中文。

---

## A. Fourier Coefficients from Orthogonality · 从正交性推导傅里叶系数

**Claim.** For a periodic function $f(x)$ of period $L$, the Fourier coefficients in the expansion $f(x) = \sum_{n=-\infty}^{\infty} c_n e^{i2\pi nx/L}$ are given by

**命题。** 对于周期为 $L$ 的周期函数 $f(x)$，展开式 $f(x) = \sum_{n=-\infty}^{\infty} c_n e^{i2\pi nx/L}$ 中的傅里叶系数为

$$ c_n = \frac{1}{L} \int_0^L f(x) e^{-i2\pi nx/L}\,dx. $$

**Step 1 — Orthogonality of the exponential basis.** The key is the integral

**第 1 步 — 指数基的正交性。** 关键是以下积分

$$ \int_0^L e^{i2\pi mx/L} e^{-i2\pi nx/L}\,dx = \int_0^L e^{i2\pi (m-n)x/L}\,dx. $$

For $m = n$: the integrand is $e^0 = 1$, so the integral equals $L$.

当 $m = n$ 时：被积函数为 $e^0 = 1$，故积分等于 $L$。

For $m \ne n$: let $k = m - n \ne 0$. Then

当 $m \ne n$ 时：令 $k = m - n \ne 0$，则

$$ \int_0^L e^{i2\pi kx/L}\,dx = \frac{L}{i2\pi k} e^{i2\pi kx/L} \Big|_0^L = \frac{L}{i2\pi k}(e^{i2\pi k} - 1) = \frac{L}{i2\pi k}(1 - 1) = 0. $$

(Here we used $e^{i2\pi k} = 1$ for integer $k$.)

（此处用到整数 $k$ 满足 $e^{i2\pi k} = 1$。）

In summary: $\int_0^L e^{i2\pi mx/L} e^{-i2\pi nx/L}\,dx = L \delta_{mn}$.

综上：$\int_0^L e^{i2\pi mx/L} e^{-i2\pi nx/L}\,dx = L \delta_{mn}$。

**Step 2 — Extract $c_n$.** Multiply both sides of $f(x) = \sum_m c_m e^{i2\pi mx/L}$ by $e^{-i2\pi nx/L}$ and integrate over one period:

**第 2 步 — 提取 $c_n$。** 将 $f(x) = \sum_m c_m e^{i2\pi mx/L}$ 两端乘以 $e^{-i2\pi nx/L}$，并对一个周期积分：

$$ \int_0^L f(x) e^{-i2\pi nx/L}\,dx = \sum_m c_m \int_0^L e^{i2\pi (m-n)x/L}\,dx = \sum_m c_m \cdot L \delta_{mn} = L c_n. $$

(Interchange of sum and integral justified by uniform convergence of the Fourier series on $L^2$.)

（求和与积分的交换由傅里叶级数在 $L^2$ 上的一致收敛性保证。）

**Step 3 — Solve for $c_n$.**

**第 3 步 — 解出 $c_n$。**

$$ \boxed{\, c_n = \frac{1}{L} \int_0^L f(x) e^{-i2\pi nx/L}\,dx. \,} \qquad \blacksquare $$

**Physical interpretation.** The coefficient $c_n$ is the "projection" of $f$ onto the $n$-th mode $e^{i2\pi nx/L}$, measuring how much of the frequency $2\pi n/L$ is present in $f$. In quantum mechanics, the same orthogonality argument gives the expansion coefficients of a state in any orthonormal basis.

**物理解释。** 系数 $c_n$ 是 $f$ 在第 $n$ 个模式 $e^{i2\pi nx/L}$ 上的"投影"，衡量 $f$ 中频率 $2\pi n/L$ 的含量。在量子力学中，同样的正交性论证给出态在任意正交归一基下的展开系数。

---

## B. The Fourier Transform of a Gaussian Is a Gaussian · 高斯函数的傅里叶变换仍是高斯函数

**Claim.** For $f(x) = e^{-x^2/(2\sigma^2)}$ (a Gaussian with width $\sigma$), the Fourier transform is

**命题。** 对 $f(x) = e^{-x^2/(2\sigma^2)}$（宽度为 $\sigma$ 的高斯函数），傅里叶变换为

$$ \tilde f(k) = \int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2)} e^{-ikx}\,dx = \sigma\sqrt{2\pi}\, e^{-\sigma^2 k^2/2}. $$

**Step 1 — Write the integral.** We need to evaluate

**第 1 步 — 写出积分。** 需要计算

$$ \tilde f(k) = \int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2) - ikx}\,dx. $$

**Step 2 — Complete the square in the exponent.** The exponent is

**第 2 步 — 对指数配方。** 指数为

$$ -\frac{x^2}{2\sigma^2} - ikx = -\frac{1}{2\sigma^2}\left[x^2 + 2i\sigma^2 kx\right]. $$

Complete the square inside the bracket:

对方括号内配方：

$$ x^2 + 2i\sigma^2 kx = (x + i\sigma^2 k)^2 - (i\sigma^2 k)^2 = (x + i\sigma^2 k)^2 + \sigma^4 k^2. $$

So the exponent becomes:

故指数变为：

$$ -\frac{1}{2\sigma^2}\left[(x + i\sigma^2 k)^2 + \sigma^4 k^2\right] = -\frac{(x + i\sigma^2 k)^2}{2\sigma^2} - \frac{\sigma^2 k^2}{2}. $$

**Step 3 — Factor out the $k$-dependent term.**

**第 3 步 — 提取 $k$ 相关项。**

$$ \tilde f(k) = e^{-\sigma^2 k^2/2} \int_{-\infty}^{\infty} e^{-(x + i\sigma^2 k)^2/(2\sigma^2)}\,dx. $$

**Step 4 — Shift the contour.** Let $u = x + i\sigma^2 k$ (a shift by the purely imaginary constant $i\sigma^2 k$). Then $du = dx$, and as $x$ ranges over $\mathbb{R}$, $u$ ranges over the horizontal line $\operatorname{Im}(u) = \sigma^2 k$ in $\mathbb{C}$. By Cauchy's theorem, since $e^{-u^2/(2\sigma^2)}$ is analytic everywhere, the integral along this shifted line equals the integral along the real axis:

**第 4 步 — 平移围道。** 令 $u = x + i\sigma^2 k$（平移纯虚常数 $i\sigma^2 k$）。则 $du = dx$，当 $x$ 遍历 $\mathbb{R}$ 时，$u$ 遍历 $\mathbb{C}$ 中虚部为 $\sigma^2 k$ 的水平线。由柯西定理，由于 $e^{-u^2/(2\sigma^2)}$ 处处解析，沿此平移直线的积分等于沿实轴的积分：

$$ \int_{-\infty+i\sigma^2 k}^{\infty+i\sigma^2 k} e^{-u^2/(2\sigma^2)}\,du = \int_{-\infty}^{\infty} e^{-u^2/(2\sigma^2)}\,du. $$

(The vertical pieces of the rectangular contour $[-R, R] \to [-R+i\sigma^2 k, R+i\sigma^2 k]$ vanish as $R \to \infty$ because the Gaussian decays faster than any polynomial in $\operatorname{Re}(u)$.)

（矩形围道的竖直段 $[-R, R] \to [-R+i\sigma^2 k, R+i\sigma^2 k]$ 在 $R \to \infty$ 时趋于零，因为高斯函数随 $\operatorname{Re}(u)$ 的增长衰减速度超过任何多项式。）

**Step 5 — Evaluate the Gaussian integral.** Substituting $v = u/\sigma\sqrt2$ (so that $u^2/(2\sigma^2) = v^2$):

**第 5 步 — 计算高斯积分。** 令 $v = u/\sigma\sqrt2$（使 $u^2/(2\sigma^2) = v^2$）：

$$ \int_{-\infty}^{\infty} e^{-u^2/(2\sigma^2)}\,du = \sigma\sqrt2 \int_{-\infty}^{\infty} e^{-v^2}\,dv = \sigma\sqrt2 \cdot \sqrt\pi = \sigma\sqrt{2\pi}. $$

(Using the Gaussian integral $\int e^{-v^2}\,dv = \sqrt\pi$ from Module 0.1.)

（利用模块 0.1 中的高斯积分 $\int e^{-v^2}\,dv = \sqrt\pi$。）

**Step 6 — Assemble the result.**

**第 6 步 — 组合结果。**

$$ \boxed{\, \tilde f(k) = e^{-\sigma^2 k^2/2} \cdot \sigma\sqrt{2\pi} = \sigma\sqrt{2\pi}\, e^{-\sigma^2 k^2/2}. \,} \qquad \blacksquare $$

The result is indeed a Gaussian in $k$ with width $1/\sigma$: as $\sigma$ increases (broad $x$-distribution), the $k$-distribution narrows, and vice versa. Setting $\sigma_k = 1/\sigma_x$, we get the **uncertainty product** $\sigma_x \cdot \sigma_k = 1$. With $k = p/\hbar$ this becomes $\Delta x \cdot \Delta p = \hbar$, the Heisenberg uncertainty principle.

结果确实是 $k$ 中宽度为 $1/\sigma$ 的高斯函数：随着 $\sigma$ 增大（$x$ 分布变宽），$k$ 分布变窄，反之亦然。令 $\sigma_k = 1/\sigma_x$，得**不确定积** $\sigma_x \cdot \sigma_k = 1$。令 $k = p/\hbar$，即得 $\Delta x \cdot \Delta p = \hbar$，即海森堡不确定性原理。

---

## C. The Convolution Theorem · 卷积定理

**Claim.** If $(f * g)(x) = \int_{-\infty}^{\infty} f(y) g(x - y)\,dy$ is the convolution of $f$ and $g$, and $\tilde f, \tilde g$ are their Fourier transforms, then

**命题。** 若 $(f * g)(x) = \int_{-\infty}^{\infty} f(y) g(x - y)\,dy$ 是 $f$ 与 $g$ 的卷积，$\tilde f, \tilde g$ 是它们的傅里叶变换，则

$$ \boldsymbol{\operatorname{FT}[f * g](k) = \tilde f(k) \cdot \tilde g(k).} $$

**Step 1 — Write the Fourier transform of the convolution.**

**第 1 步 — 写出卷积的傅里叶变换。**

$$ \operatorname{FT}[f*g](k) = \int_{-\infty}^{\infty} (f*g)(x) e^{-ikx}\,dx = \int_{-\infty}^{\infty} \left[\int_{-\infty}^{\infty} f(y) g(x-y)\,dy\right] e^{-ikx}\,dx. $$

**Step 2 — Interchange the order of integration.** (Justified by absolute integrability — Fubini's theorem, valid when $f, g \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.)

**第 2 步 — 交换积分次序。**（由绝对可积性——Fubini 定理保证，当 $f, g \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ 时成立。）

$$ \operatorname{FT}[f*g](k) = \int_{-\infty}^{\infty} f(y) \left[\int_{-\infty}^{\infty} g(x-y) e^{-ikx}\,dx\right] dy. $$

**Step 3 — Shift the inner integral.** Let $u = x - y$ (so $x = u + y$, $dx = du$):

**第 3 步 — 对内层积分做平移。** 令 $u = x - y$（则 $x = u + y$，$dx = du$）：

$$ \int_{-\infty}^{\infty} g(x-y) e^{-ikx}\,dx = \int_{-\infty}^{\infty} g(u) e^{-ik(u+y)}\,du = e^{-iky} \int_{-\infty}^{\infty} g(u) e^{-iku}\,du = e^{-iky} \tilde g(k). $$

**Step 4 — Reassemble.**

**第 4 步 — 重新组合。**

$$ \operatorname{FT}[f*g](k) = \int_{-\infty}^{\infty} f(y) e^{-iky} \tilde g(k)\,dy = \tilde g(k) \int_{-\infty}^{\infty} f(y) e^{-iky}\,dy = \tilde g(k) \cdot \tilde f(k). $$

Therefore $\boldsymbol{\operatorname{FT}[f * g] = \tilde f \cdot \tilde g}$. $\blacksquare$

因此 $\boldsymbol{\operatorname{FT}[f * g] = \tilde f \cdot \tilde g}$。$\blacksquare$

**Inverse direction.** By taking the inverse Fourier transform: $\operatorname{FT}^{-1}[\tilde f \cdot \tilde g] = f * g$. So convolution in real space $\leftrightarrow$ pointwise multiplication in frequency space. This duality is extremely powerful: convolutions that are hard to compute directly become simple multiplications in Fourier space.

**逆方向。** 取逆傅里叶变换：$\operatorname{FT}^{-1}[\tilde f \cdot \tilde g] = f * g$。即实空间中的卷积 $\leftrightarrow$ 频率空间中的逐点乘积。这种对偶性极为有用：直接计算困难的卷积在傅里叶空间中变为简单的乘法。

**Physical applications.** In quantum mechanics, the probability of measuring a system in a particular state after preparation is a convolution of the apparatus resolution function with the state's probability distribution — the convolution theorem explains spectral line broadening. In signal processing, filtering is multiplication in frequency space (convolution in time domain).

**物理应用。** 在量子力学中，制备后测量系统处于特定态的概率是仪器分辨函数与态的概率分布的卷积——卷积定理解释了谱线展宽。在信号处理中，滤波是频率空间中的乘法（时域中的卷积）。

---

## D. The Dirac Delta as a Fourier Representation · 狄拉克 Delta 函数的傅里叶表示

**Claim.** The Dirac delta satisfies

**命题。** 狄拉克 delta 函数满足

$$ \delta(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{ikx}\,dk. $$

**Step 1 — Compute the Fourier transform of $\delta$.** Using the defining property $\int \delta(x) e^{-ikx}\,dx = e^{-ik\cdot 0} = 1$:

**第 1 步 — 计算 $\delta$ 的傅里叶变换。** 利用定义性质 $\int \delta(x) e^{-ikx}\,dx = e^{-ik\cdot 0} = 1$：

$$ \tilde\delta(k) = \int_{-\infty}^{\infty} \delta(x) e^{-ikx}\,dx = \boldsymbol{1}. $$

The Dirac delta transforms to the constant function 1 — it contains all frequencies with equal amplitude (a "white noise" in frequency space).

狄拉克 delta 变换为常数函数 1——它以相同振幅包含所有频率（频率空间中的"白噪声"）。

**Step 2 — Apply the inverse Fourier transform.** The inverse transform pair reads $f(x) = \frac{1}{2\pi} \int \tilde f(k) e^{ikx}\,dk$. Applying this to $\tilde f(k) = 1$:

**第 2 步 — 应用逆傅里叶变换。** 逆变换对为 $f(x) = \frac{1}{2\pi} \int \tilde f(k) e^{ikx}\,dk$。对 $\tilde f(k) = 1$ 应用此公式：

$$ \delta(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} 1 \cdot e^{ikx}\,dk = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{ikx}\,dk. \qquad \blacksquare $$

**Rigorous interpretation.** The integral $\frac{1}{2\pi}\int e^{ikx}\,dk$ does not converge in the ordinary sense (the integrand has modulus 1 everywhere). It must be interpreted as a limit:

**严格解释。** 积分 $\frac{1}{2\pi}\int e^{ikx}\,dk$ 在通常意义下不收敛（被积函数的模处处为 1）。必须理解为极限：

$$ \delta(x) = \lim_{K\to\infty} \frac{1}{2\pi} \int_{-K}^{K} e^{ikx}\,dk = \lim_{K\to\infty} \frac{\sin(Kx)}{\pi x}. $$

This is the **Dirichlet kernel**, which concentrates at $x = 0$ and has unit area for all $K$. In the theory of distributions (generalized functions), $\delta(x)$ is defined as a linear functional $\delta[f] = f(0)$, and the representation $\frac{1}{2\pi}\int e^{ikx}\,dk$ is an identity in the distributional sense.

这是**狄利克雷核**，它在 $x = 0$ 处集中，对所有 $K$ 面积为 1。在广义函数理论中，$\delta(x)$ 定义为线性泛函 $\delta[f] = f(0)$，而表达式 $\frac{1}{2\pi}\int e^{ikx}\,dk$ 是广义函数意义下的恒等式。

**Step 3 — Verify the sifting property.** Using the representation:

**第 3 步 — 验证筛选性质。** 利用上述表示：

$$ \begin{aligned} \int \delta(x-a) f(x)\,dx &= \int \left[\frac{1}{2\pi} \int e^{ik(x-a)}\,dk\right] f(x)\,dx \\ &= \frac{1}{2\pi} \int e^{-ika} \left[\int f(x) e^{ikx}\,dx\right] dk \\ &= \frac{1}{2\pi} \int e^{-ika} \tilde f(-k)\,dk = f(a). \quad\checkmark \end{aligned} $$

The last step uses the inverse Fourier transform evaluated at $x = a$.

最后一步利用逆傅里叶变换在 $x = a$ 处的取值。

---

## E. Variance Formula: $\operatorname{Var}(x) = \langle x^2\rangle - \langle x\rangle^2$ · 方差公式

**Claim.** For a random variable with probability density $p(x)$,

**命题。** 对于概率密度为 $p(x)$ 的随机变量，

$$ \sigma^2 \equiv \langle (x - \langle x\rangle)^2\rangle = \langle x^2\rangle - \langle x\rangle^2. $$

**Step 1 — Expand the square.**

**第 1 步 — 展开平方。**

$$ \sigma^2 = \langle (x - \langle x\rangle)^2\rangle = \int (x - \langle x\rangle)^2 p(x)\,dx = \int \left[x^2 - 2x\langle x\rangle + \langle x\rangle^2\right] p(x)\,dx. $$

**Step 2 — Distribute the integral.** Using linearity of the integral:

**第 2 步 — 分配积分。** 利用积分的线性性：

$$ \sigma^2 = \int x^2 p(x)\,dx - 2\langle x\rangle \int x p(x)\,dx + \langle x\rangle^2 \int p(x)\,dx. $$

**Step 3 — Identify the terms.** By definition, $\int x^2 p(x)\,dx = \langle x^2\rangle$, $\int x p(x)\,dx = \langle x\rangle$, and $\int p(x)\,dx = 1$ (normalization):

**第 3 步 — 识别各项。** 由定义，$\int x^2 p(x)\,dx = \langle x^2\rangle$，$\int x p(x)\,dx = \langle x\rangle$，$\int p(x)\,dx = 1$（归一化）：

$$ \sigma^2 = \langle x^2\rangle - 2\langle x\rangle \cdot \langle x\rangle + \langle x\rangle^2 \cdot 1 = \langle x^2\rangle - 2\langle x\rangle^2 + \langle x\rangle^2 = \boxed{\,\langle x^2\rangle - \langle x\rangle^2\,}. \qquad \blacksquare $$

**Physical significance.** In quantum mechanics with $|\psi(x)|^2$ as the probability density, this gives $\Delta x^2 = \langle x^2\rangle - \langle x\rangle^2$, the quantum uncertainty in position. The same formula applies to momentum: $\Delta p^2 = \langle p^2\rangle - \langle p\rangle^2$. Together these satisfy the Heisenberg uncertainty principle $\Delta x \cdot \Delta p \ge \hbar/2$.

**物理意义。** 在量子力学中以 $|\psi(x)|^2$ 为概率密度，此式给出 $\Delta x^2 = \langle x^2\rangle - \langle x\rangle^2$，即位置的量子不确定度。同样的公式适用于动量：$\Delta p^2 = \langle p^2\rangle - \langle p\rangle^2$。二者共同满足海森堡不确定性原理 $\Delta x \cdot \Delta p \ge \hbar/2$。

**Non-negativity.** Since $\sigma^2 = \langle x^2\rangle - \langle x\rangle^2$ and also $\sigma^2 = \langle (x-\langle x\rangle)^2\rangle \ge 0$ (as the integral of a non-negative function times a non-negative density), we have $\boldsymbol{\langle x^2\rangle \ge \langle x\rangle^2}$ — the Cauchy–Schwarz inequality for probability theory.

**非负性。** 由于 $\sigma^2 = \langle x^2\rangle - \langle x\rangle^2$，同时 $\sigma^2 = \langle (x-\langle x\rangle)^2\rangle \ge 0$（非负函数乘以非负密度的积分），故 $\boldsymbol{\langle x^2\rangle \ge \langle x\rangle^2}$——这是概率论中的柯西–施瓦茨不等式。

---

## F. The Central Limit Theorem via Characteristic Functions · 通过特征函数的中心极限定理

**Claim.** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2 < \infty$. Define the standardized sum

**命题。** 设 $X_1, X_2, \ldots, X_n$ 是具有均值 $\mu$ 和有限方差 $\sigma^2$ 的独立同分布随机变量。定义标准化和

$$ Z_n = \frac{X_1 + X_2 + \cdots + X_n - n\mu}{\sigma\sqrt n}. $$

Then as $n \to \infty$, $Z_n$ converges in distribution to the standard normal $N(0,1)$:

当 $n \to \infty$ 时，$Z_n$ 在分布意义上收敛于标准正态分布 $N(0,1)$：

$$ P(Z_n \le z) \to \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-t^2/2}\,dt. $$

**Step 1 — Define the characteristic function.** For a random variable $X$ with density $p(x)$, the **characteristic function** (Fourier transform of $p$) is

**第 1 步 — 定义特征函数。** 对具有密度 $p(x)$ 的随机变量 $X$，**特征函数**（$p$ 的傅里叶变换）为

$$ \varphi_X(t) = \langle e^{itX}\rangle = \int e^{itx} p(x)\,dx. $$

Note: $\varphi_X(t) = \tilde p(-t)$ in the Fourier convention of Module 0.5.

注：在模块 0.5 的傅里叶约定下，$\varphi_X(t) = \tilde p(-t)$。

**Step 2 — Characteristic function of a sum.** For independent $X_1, X_2$, the density of $X_1 + X_2$ is the convolution $p_1 * p_2$. By the convolution theorem (Section C):

**第 2 步 — 和的特征函数。** 对独立的 $X_1, X_2$，$X_1 + X_2$ 的密度是卷积 $p_1 * p_2$。由卷积定理（C 节）：

$$ \varphi_{X_1+X_2}(t) = \varphi_{X_1}(t) \cdot \varphi_{X_2}(t). $$

More generally, for a sum of $n$ i.i.d. copies: $\varphi_{\sum X_i}(t) = [\varphi_X(t)]^n$.

更一般地，对 $n$ 个独立同分布副本之和：$\varphi_{\sum X_i}(t) = [\varphi_X(t)]^n$。

**Step 3 — Characteristic function of the centered, scaled variable.** Define $Y = (X - \mu)/\sigma$, so $Y$ has mean 0 and variance 1. Then $Z_n = (Y_1 + \cdots + Y_n)/\sqrt n$, and

**第 3 步 — 中心化、缩放变量的特征函数。** 定义 $Y = (X - \mu)/\sigma$，则 $Y$ 的均值为 0，方差为 1。则 $Z_n = (Y_1 + \cdots + Y_n)/\sqrt n$，

$$ \varphi_{Z_n}(t) = \varphi_{\sum Y_i/\sqrt n}(t) = \varphi_{\sum Y_i}(t/\sqrt n) = [\varphi_Y(t/\sqrt n)]^n. $$

**Step 4 — Expand $\varphi_Y$ for small argument.** Using the Taylor expansion of $e^{itY}$:

**第 4 步 — 展开小参数处的 $\varphi_Y$。** 利用 $e^{itY}$ 的泰勒展开：

$$ \varphi_Y(s) = \langle e^{isY}\rangle = \langle 1 + isY + (isY)^2/2! + \cdots\rangle = 1 + is\langle Y\rangle + (is)^2\langle Y^2\rangle/2 + O(s^3). $$

Since $\langle Y\rangle = 0$ and $\langle Y^2\rangle = \operatorname{Var}(Y) = 1$ (by construction):

由于 $\langle Y\rangle = 0$，$\langle Y^2\rangle = \operatorname{Var}(Y) = 1$（由构造）：

$$ \varphi_Y(s) = 1 - s^2/2 + O(s^3). $$

**Step 5 — Take the $n$-th power with $s = t/\sqrt n$.**

**第 5 步 — 令 $s = t/\sqrt n$ 并取 $n$ 次幂。**

$$ \varphi_{Z_n}(t) = [\varphi_Y(t/\sqrt n)]^n = \left[1 - \frac{t^2}{2n} + O(n^{-3/2})\right]^n. $$

**Step 6 — Take $n \to \infty$.** Using the standard limit $\lim_{n\to\infty} (1 + a/n)^n = e^a$ with $a = -t^2/2$:

**第 6 步 — 令 $n \to \infty$。** 利用标准极限 $\lim_{n\to\infty} (1 + a/n)^n = e^a$，其中 $a = -t^2/2$：

$$ \lim_{n\to\infty} \varphi_{Z_n}(t) = \lim_{n\to\infty} \left[1 - \frac{t^2}{2n}\right]^n = \boldsymbol{e^{-t^2/2}}. $$

**Step 7 — Identify the limit.** The function $e^{-t^2/2}$ is exactly the characteristic function of the standard normal distribution $N(0,1)$ — by Section B, the Fourier transform of $\frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is $e^{-t^2/2}$ (with $\sigma = 1$). Since convergence of characteristic functions implies convergence in distribution (Lévy's continuity theorem):

**第 7 步 — 识别极限。** 函数 $e^{-t^2/2}$ 恰好是标准正态分布 $N(0,1)$ 的特征函数——由 B 节，$\frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ 的傅里叶变换为 $e^{-t^2/2}$（$\sigma = 1$）。由于特征函数的收敛等价于分布的收敛（Lévy 连续性定理）：

$$ \boldsymbol{Z_n \to N(0,1) \text{ in distribution.}} \qquad \blacksquare $$

**Physical significance.** The CLT explains why Gaussian distributions are ubiquitous in physics:
- **Thermal fluctuations**: energy of a macroscopic system is a sum of contributions from $\sim 10^{23}$ microscopic degrees of freedom — by the CLT, the fluctuations are Gaussian.
- **Quantum ground states**: the harmonic oscillator ground state $\psi_0 \propto e^{-m\omega x^2/2\hbar}$ is Gaussian because the oscillator potential is the simplest smooth potential and the Gaussian is the "minimum uncertainty" state (it saturates the Heisenberg bound $\Delta x\, \Delta p = \hbar/2$).
- **Measurement noise**: any detector output that aggregates many small independent errors follows the CLT $\to$ Gaussian noise.

**物理意义。** 中心极限定理解释了高斯分布在物理学中普遍存在的原因：
- **热涨落**：宏观系统的能量是约 $10^{23}$ 个微观自由度贡献之和——由中心极限定理，涨落是高斯型的。
- **量子基态**：谐振子基态 $\psi_0 \propto e^{-m\omega x^2/2\hbar}$ 是高斯型的，因为谐振子势是最简单的光滑势，而高斯态是"最小不确定性"态（它饱和海森堡界 $\Delta x\, \Delta p = \hbar/2$）。
- **测量噪声**：任何聚合许多小的独立误差的探测器输出均遵循中心极限定理 $\to$ 高斯噪声。

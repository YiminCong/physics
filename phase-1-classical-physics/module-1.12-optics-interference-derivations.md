# Derivations — Module 1.12: Optics & Interference
# 推导 — 模块 1.12：光学与干涉

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.12](./module-1.12-optics-interference.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.12](./module-1.12-optics-interference.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Snell's Law from Fermat's Principle of Least Time · 从费马最短时间原理推导斯涅尔定律

**Claim.** For a ray travelling from point A in medium 1 (speed $v_1$) to point B in medium 2 (speed $v_2$), Fermat's principle (the actual path minimises travel time) yields Snell's law $n_1\sin\theta_1 = n_2\sin\theta_2$, where $n = c/v$ is the refractive index.

**命题。** 对于从介质 1（速度 $v_1$）中点 A 到介质 2（速度 $v_2$）中点 B 的光线，费马原理（实际路径使传播时间最短）给出斯涅尔定律 $n_1\sin\theta_1 = n_2\sin\theta_2$，其中 $n = c/v$ 为折射率。

**Step 1 — Set up the geometry.** Let the interface be horizontal at $y = 0$. Place A at $(0, y_1)$ in medium 1 (perpendicular distance $y_1$ above the interface) and B at $(d, -y_2)$ in medium 2 (perpendicular distance $y_2$ below), with $y_1, y_2, d > 0$. The ray crosses the interface at $P = (x, 0)$, where $x$ is the free parameter to optimise; the angles $\theta_1$ (incidence) and $\theta_2$ (refraction) are measured from the normal (the $y$-axis). The path lengths in each medium are:

**第 1 步 — 建立几何关系。** 设界面水平位于 $y = 0$。令 A 在介质 1 中位于 $(0, y_1)$（界面上方垂直距离 $y_1$），B 在介质 2 中位于 $(d, -y_2)$（界面下方垂直距离 $y_2$），$y_1, y_2, d > 0$。光线在 $P = (x, 0)$ 穿过界面，$x$ 为待优化的自由参数；入射角 $\theta_1$ 与折射角 $\theta_2$ 从法线（$y$ 轴）量起。各介质中的路径长度为：

$$ \begin{aligned}
l_1 &= \sqrt{x^2 + y_1^2} && \text{(in medium 1)}, \\
l_2 &= \sqrt{(d-x)^2 + y_2^2} && \text{(in medium 2)}.
\end{aligned} $$

**Step 2 — Write the travel time.** The total travel time is:

**第 2 步 — 写出传播时间。** 总传播时间为：

$$ T(x) = \frac{l_1}{v_1} + \frac{l_2}{v_2} = \frac{1}{v_1}\sqrt{x^2 + y_1^2} + \frac{1}{v_2}\sqrt{(d-x)^2 + y_2^2}. $$

**Step 3 — Minimise by setting $dT/dx = 0$.** Differentiating:

**第 3 步 — 令 $dT/dx = 0$ 求极值。** 对 $x$ 微分：

$$ \frac{dT}{dx} = \frac{x}{v_1\sqrt{x^2 + y_1^2}} + \frac{(-1)(d-x)}{v_2\sqrt{(d-x)^2 + y_2^2}} = 0. $$

Identify the geometric terms: the angle of incidence $\theta_1$ satisfies $\sin\theta_1 = x/\sqrt{x^2 + y_1^2}$, and the angle of refraction $\theta_2$ satisfies $\sin\theta_2 = (d-x)/\sqrt{(d-x)^2 + y_2^2}$. Therefore:

识别几何项：入射角 $\theta_1$ 满足 $\sin\theta_1 = x/\sqrt{x^2 + y_1^2}$，折射角 $\theta_2$ 满足 $\sin\theta_2 = (d-x)/\sqrt{(d-x)^2 + y_2^2}$。因此：

$$ \frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}. $$

**Step 4 — Write in terms of refractive indices.** Using $n = c/v$, so $1/v = n/c$:

**第 4 步 — 用折射率表示。** 利用 $n = c/v$，故 $1/v = n/c$：

$$ \frac{n_1\sin\theta_1}{c} = \frac{n_2\sin\theta_2}{c} \;\to\; \boxed{\,n_1\sin\theta_1 = n_2\sin\theta_2\,} \qquad \blacksquare $$

**Step 5 — Verify it is a minimum (not maximum).** The second derivative $d^2T/dx^2 > 0$ at the stationary point (the calculation shows $d^2T/dx^2 = y_1^2/(v_1 l_1^3) + y_2^2/(v_2 l_2^3) > 0$), confirming the path is indeed a minimum time, consistent with Fermat's principle. (For reflection, the analogous calculation gives the law of reflection: $\theta_i = \theta_r$.)

**第 5 步 — 验证是极小值（而非极大值）。** 在驻点处二阶导数 $d^2T/dx^2 > 0$（计算表明 $d^2T/dx^2 = y_1^2/(v_1 l_1^3) + y_2^2/(v_2 l_2^3) > 0$），确认路径确实是最短时间，与费马原理一致。（对于反射，类似计算给出反射定律：$\theta_i = \theta_r$。）

---

## B. Two-Slit Interference — Constructive Maxima at $d\sin\theta = m\lambda$ · 双缝干涉——$d\sin\theta = m\lambda$ 处的相长极大

**Claim.** For two coherent slits separated by $d$, illuminated at normal incidence by wavelength $\lambda$, the intensity at angle $\theta$ is $I(\theta) = 4I_0\cos^2(\pi d\sin\theta/\lambda)$, with maxima at $d\sin\theta = m\lambda$, $m = 0, \pm 1, \pm 2, \dots$

**命题。** 对于间距为 $d$ 的两个相干缝，波长 $\lambda$ 法线入射，角度 $\theta$ 处的强度为 $I(\theta) = 4I_0\cos^2(\pi d\sin\theta/\lambda)$，极大值在 $d\sin\theta = m\lambda$，$m = 0, \pm 1, \pm 2, \dots$

**Step 1 — Path difference.** Let the two slits be at $y = +d/2$ and $y = -d/2$. For a distant observation point P at angle $\theta$ (Fraunhofer limit: screen distance $L\gg d$), the path difference between the two rays is:

**第 1 步 — 路程差。** 设两缝分别在 $y = +d/2$ 和 $y = -d/2$。对于角度 $\theta$ 处的远处观察点 P（夫琅禾费极限：屏幕距离 $L\gg d$），两条光线之间的路程差为：

$$ \Delta = d\sin\theta. $$

(The derivation: the extra path length from slit 2 to P compared with slit 1 is the perpendicular distance from slit 1 to the ray from slit 2, which is $d\sin\theta$ by simple geometry.)

（推导：从缝 2 到 P 与从缝 1 到 P 相比的额外路程，是从缝 1 到缝 2 射线的垂直距离，由简单几何关系为 $d\sin\theta$。）

**Step 2 — Phase difference and wave superposition.** The corresponding phase difference is:

**第 2 步 — 相位差与波叠加。** 相应的相位差为：

$$ \delta = \frac{2\pi\Delta}{\lambda} = \frac{2\pi d\sin\theta}{\lambda}. $$

The two coherent waves at P have equal amplitude $E_0$ and a relative phase $\delta$. Their superposition (using complex notation and taking the real part):

P 处两列相干波振幅相等均为 $E_0$，相对相位差为 $\delta$。它们的叠加（用复数表示并取实部）：

$$ E_\text{total} = E_0\, e^{i\omega t} + E_0\, e^{i(\omega t + \delta)} = E_0\, e^{i\omega t}(1 + e^{i\delta}) = E_0\, e^{i\omega t}\, e^{i\delta/2}\cdot 2\cos(\delta/2). $$

The amplitude of the resulting wave is $2E_0\cos(\delta/2)$, and the intensity $I\propto|\text{amplitude}|^2$:

所得波的振幅为 $2E_0\cos(\delta/2)$，强度 $I\propto|\text{振幅}|^2$：

$$ I(\theta) = 4I_0\cos^2(\delta/2) = 4I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right), $$

where $I_0 = \epsilon_0 c E_0^2/2$ is the intensity from a single slit.

其中 $I_0 = \epsilon_0 c E_0^2/2$ 是单缝强度。

**Step 3 — Maxima and minima.** Maxima: $\cos^2(\pi d\sin\theta/\lambda) = 1$, i.e. $\pi d\sin\theta/\lambda = m\pi$:

**第 3 步 — 极大值与极小值。** 极大值：$\cos^2(\pi d\sin\theta/\lambda) = 1$，即 $\pi d\sin\theta/\lambda = m\pi$：

$$ \boxed{\,d\sin\theta = m\lambda\,}, \qquad m = 0, \pm 1, \pm 2, \dots \quad \text{(constructive interference / 相长干涉)} $$

Minima: $\cos^2(\pi d\sin\theta/\lambda) = 0$, i.e. $\pi d\sin\theta/\lambda = (m + \tfrac12)\pi$:

极小值：$\cos^2(\pi d\sin\theta/\lambda) = 0$，即 $\pi d\sin\theta/\lambda = (m + \tfrac12)\pi$：

$$ \boxed{\,d\sin\theta = (m + \tfrac12)\lambda\,}, \qquad m = 0, \pm 1, \pm 2, \dots \quad \text{(destructive interference / 相消干涉)} $$

**Step 4 — Fringe spacing on a screen.** For small angles ($\sin\theta\approx\theta\approx y/L$, where $y$ is the position on a screen at distance $L$):

**第 4 步 — 屏幕上的条纹间距。** 对于小角度（$\sin\theta\approx\theta\approx y/L$，其中 $y$ 是距离 $L$ 处屏幕上的位置）：

$$ y_m = \frac{m\lambda L}{d}, \qquad \text{fringe spacing}\ \Delta y = \frac{\lambda L}{d}. \qquad \blacksquare $$

---

## C. Single-Slit Diffraction as the Fourier Transform of the Aperture · 单缝衍射作为孔径的傅里叶变换

**Claim.** The far-field (Fraunhofer) diffraction amplitude from a slit of width $a$ is proportional to the Fourier transform of the aperture function, giving intensity $I(\theta) = I_0\,\mathrm{sinc}^2(a\sin\theta/\lambda)$.

**命题。** 宽度为 $a$ 的缝的远场（夫琅禾费）衍射振幅正比于孔径函数的傅里叶变换，给出强度 $I(\theta) = I_0\,\mathrm{sinc}^2(a\sin\theta/\lambda)$。

**Step 1 — Huygens-Fresnel integral.** By Huygens' principle, each infinitesimal element $dy'$ of the slit at position $y'\in[-a/2, +a/2]$ acts as a secondary source of wavelets. At a distant point P at angle $\theta$, the path from position $y'$ is longer (or shorter) by $y'\sin\theta$ compared with the path from the centre ($y' = 0$). The total complex amplitude at P is the integral of these contributions:

**第 1 步 — 惠更斯–菲涅耳积分。** 由惠更斯原理，缝在位置 $y'\in[-a/2, +a/2]$ 处的每个无穷小元 $dy'$ 都是子波的次级波源。在角度 $\theta$ 处的远处点 P，位置 $y'$ 处的路径比中心（$y' = 0$）处的路径长（或短）$y'\sin\theta$。P 处的总复振幅是这些贡献的积分：

$$ E(\theta) = \frac{E_0}{a}\int_{-a/2}^{a/2} e^{i(2\pi/\lambda)y'\sin\theta}\,dy'. $$

**Step 2 — This integral is a Fourier transform.** Define the spatial frequency $k_x = (2\pi/\lambda)\sin\theta$ (the component of the wavevector along the slit direction). The aperture function for a uniform slit is $f(y') = 1$ for $y'\in[-a/2, a/2]$ and $0$ elsewhere. Then:

**第 2 步 — 此积分是傅里叶变换。** 定义空间频率 $k_x = (2\pi/\lambda)\sin\theta$（波矢量沿缝方向的分量）。均匀缝的孔径函数为 $f(y') = 1$（$y'\in[-a/2, a/2]$），其他处为 $0$。则：

$$ E(k_x)\propto\int_{-\infty}^{\infty} f(y')\, e^{i k_x y'}\,dy' = \tilde{F}(k_x), $$

the Fourier transform of the aperture function $f$. The far-field diffraction pattern is the squared modulus of the Fourier transform of the aperture: $I\propto|\tilde{F}(k_x)|^2$.

孔径函数 $f$ 的傅里叶变换。远场衍射图样是孔径傅里叶变换的模的平方：$I\propto|\tilde{F}(k_x)|^2$。

**Step 3 — Evaluate the transform.** For the uniform slit:

**第 3 步 — 计算变换。** 对于均匀缝：

$$ \begin{aligned}
E(\theta) &\propto \int_{-a/2}^{a/2} e^{i k_x y'}\,dy' = \left[\frac{e^{i k_x y'}}{i k_x}\right]_{-a/2}^{a/2} \\
&= \frac{e^{i k_x a/2} - e^{-i k_x a/2}}{i k_x} \\
&= \frac{2\sin(k_x a/2)}{k_x} \\
&= a\cdot\mathrm{sinc}\!\left(\frac{k_x a}{2\pi}\right) \quad \text{where}\ \mathrm{sinc}(u) = \frac{\sin(\pi u)}{\pi u}.
\end{aligned} $$

Substituting $k_x = (2\pi/\lambda)\sin\theta$:

代入 $k_x = (2\pi/\lambda)\sin\theta$：

$$ E(\theta)\propto a\,\mathrm{sinc}\!\left(\frac{a\sin\theta}{\lambda}\right) = a\,\frac{\sin(\pi a\sin\theta/\lambda)}{\pi a\sin\theta/\lambda}. $$

Define $\beta = \pi a\sin\theta/\lambda$. Then $E\propto\sin(\beta)/\beta$ and:

定义 $\beta = \pi a\sin\theta/\lambda$。则 $E\propto\sin(\beta)/\beta$，且：

$$ \boxed{\,I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2 = I_0\,\mathrm{sinc}^2\!\left(\frac{a\sin\theta}{\lambda}\right),\quad \mathrm{sinc}(u) = \frac{\sin(\pi u)}{\pi u}\,} \qquad \blacksquare $$

**Step 4 — Features of the pattern.** Central maximum at $\theta = 0$ ($\beta\to 0$, $\mathrm{sinc}\to 1$). First zeros at $\beta = \pm\pi$, i.e. $\sin\theta = \pm\lambda/a$: the central maximum has half-angular width $\lambda/a$ (full width $2\lambda/a$). Secondary maxima at $\beta\approx\pm 3\pi/2, \pm 5\pi/2, \dots$ with intensities approximately $I_0/(3\pi/2)^2\approx 0.045\, I_0$, $I_0/(5\pi/2)^2\approx 0.016\, I_0$, $\dots$ — progressively weaker, consistent with the spreading of Fourier components.

**第 4 步 — 图样的特征。** $\theta = 0$ 处中央极大（$\beta\to 0$，$\mathrm{sinc}\to 1$）。第一零点在 $\beta = \pm\pi$，即 $\sin\theta = \pm\lambda/a$：中央极大的半角宽度为 $\lambda/a$（全宽 $2\lambda/a$）。次极大在 $\beta\approx\pm 3\pi/2, \pm 5\pi/2, \dots$ 处，强度约为 $I_0/(3\pi/2)^2\approx 0.045\, I_0$，$I_0/(5\pi/2)^2\approx 0.016\, I_0$，$\dots$——逐渐减弱，与傅里叶分量扩展一致。

---

## D. Diffraction Grating Condition · 衍射光栅条件

**Claim.** A grating of $N$ slits with spacing $d$ produces sharp principal maxima at $d\sin\theta = m\lambda$, $m = 0, \pm 1, \pm 2, \dots$, with intensity $I = N^2 I_0$ at the maxima.

**命题。** 间距为 $d$ 的 $N$ 缝光栅在 $d\sin\theta = m\lambda$，$m = 0, \pm 1, \pm 2, \dots$ 处产生尖锐主极大，极大处强度为 $I = N^2 I_0$。

**Step 1 — Sum of $N$ coherent waves.** The $N$ slits contribute waves with equal amplitudes but with successive phase differences $\delta = 2\pi d\sin\theta/\lambda$ (the phase accumulated per slit spacing). Using the geometric series sum:

**第 1 步 — $N$ 列相干波之和。** $N$ 个缝贡献等振幅但依次相差相位 $\delta = 2\pi d\sin\theta/\lambda$（每个缝间距积累的相位）的波。利用等比级数求和：

$$ E_\text{total} = E_0\sum_{n=0}^{N-1} e^{i n\delta} = E_0\,\frac{1 - e^{iN\delta}}{1 - e^{i\delta}}. $$

**Step 2 — Compute the intensity.** Taking the modulus squared:

**第 2 步 — 计算强度。** 取模的平方：

$$ I = |E_\text{total}|^2 = I_0\,\frac{|1 - e^{iN\delta}|^2}{|1 - e^{i\delta}|^2} = I_0\,\frac{[\sin(N\delta/2)]^2}{[\sin(\delta/2)]^2}. $$

Using the identity $|1 - e^{i\phi}|^2 = 4\sin^2(\phi/2)$:

利用恒等式 $|1 - e^{i\phi}|^2 = 4\sin^2(\phi/2)$：

$$ \boxed{\,I(\theta) = I_0\,\frac{[\sin(N\pi d\sin\theta/\lambda)]^2}{[\sin(\pi d\sin\theta/\lambda)]^2}\,} $$

**Step 3 — Principal maxima.** When $d\sin\theta = m\lambda$ ($m$ integer), the denominator $\sin(\pi d\sin\theta/\lambda) = \sin(m\pi) = 0$. By L'Hôpital's rule (or by the small-angle limit), the ratio $\to N^2$, so:

**第 3 步 — 主极大。** 当 $d\sin\theta = m\lambda$（$m$ 为整数）时，分母 $\sin(\pi d\sin\theta/\lambda) = \sin(m\pi) = 0$。由洛必达法则（或小角近似），比值 $\to N^2$，故：

$$ I_\text{max} = N^2 I_0. $$

These are the **principal maxima** (grating condition): $\boxed{\,d\sin\theta = m\lambda\,}$ $\blacksquare$

这些是**主极大**（光栅条件）：$\boxed{\,d\sin\theta = m\lambda\,}$ $\blacksquare$

**Step 4 — Resolving power.** Between successive principal maxima there are $N - 1$ zeros and $N - 2$ secondary maxima. The angular width of a principal maximum is $\Delta\theta\approx\lambda/(Nd\cos\theta)$. The minimum resolvable wavelength difference (Rayleigh criterion: the principal maximum of $\lambda + \Delta\lambda$ falls on the first zero of $\lambda$) gives the resolving power:

**第 4 步 — 分辨本领。** 相邻主极大之间有 $N - 1$ 个零点和 $N - 2$ 个次极大。主极大的角宽度为 $\Delta\theta\approx\lambda/(Nd\cos\theta)$。最小可分辨波长差（瑞利判据：$\lambda + \Delta\lambda$ 的主极大落在 $\lambda$ 的第一零点上）给出分辨本领：

$$ R = \frac{\lambda}{\Delta\lambda} = mN. $$

Higher grating orders $m$ and more slits $N$ both increase resolution.

更高的光栅阶次 $m$ 和更多的缝数 $N$ 都能提高分辨率。

---

*The Fourier connection established in Section C is the unifying theme: every diffraction and interference phenomenon is a Fourier analysis of the spatial distribution of sources. This connects to Fourier methods in Module 0.5, the quantum-mechanical interpretation of momentum eigenstates, and crystallographic structure determination.*

*C 节建立的傅里叶联系是统一主题：每一个衍射和干涉现象都是对波源空间分布的傅里叶分析。这与模块 0.5 的傅里叶方法、量子力学对动量本征态的诠释以及晶体结构测定相联系。*

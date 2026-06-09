# Derivations — Module 1.16: Mechanical Waves & Acoustics
# 推导 — 模块 1.16：机械波与声学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.16](./module-1.16-mechanical-waves-acoustics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.16](./module-1.16-mechanical-waves-acoustics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Wave Speed on a String: $c = \sqrt{T/\mu}$ · 弦上的波速推导

**Claim.** A string with tension $T$ ($\mathrm{N}$) and linear mass density $\mu$ ($\mathrm{kg/m}$) supports transverse waves satisfying the wave equation $\partial^2 y/\partial t^2 = (T/\mu)\,\partial^2 y/\partial x^2$, with wave speed $c = \sqrt{T/\mu}$.

**命题。** 张力为 $T$（$\mathrm{N}$）、线质量密度为 $\mu$（$\mathrm{kg/m}$）的弦支持横波，满足波动方程 $\partial^2 y/\partial t^2 = (T/\mu)\,\partial^2 y/\partial x^2$，波速 $c = \sqrt{T/\mu}$。

**Step 1 — Isolate a string element.** Consider a small element of the string between positions $x$ and $x + \Delta x$. Its mass is $\Delta m = \mu\,\Delta x$. Under the small-angle (small-displacement) approximation, the tension $T$ acts along the string, so the magnitude of the tension force at both ends is approximately $T$. The transverse displacement is $y(x, t)$.

**第 1 步 — 隔离弦元。** 考虑弦在 $x$ 到 $x + \Delta x$ 之间的小元。其质量为 $\Delta m = \mu\,\Delta x$。在小角度（小位移）近似下，张力 $T$ 沿弦方向作用，两端张力的大小近似为 $T$。横向位移为 $y(x, t)$。

**Step 2 — Compute the net transverse force.** The transverse component of the tension at the right end (at $x + \Delta x$) is

**第 2 步 — 计算净横向力。** 右端（$x + \Delta x$ 处）张力的横向分量为

$$ F_{\text{right}} = T\sin\theta(x + \Delta x) \approx T\tan\theta(x + \Delta x) = T\,(\partial y/\partial x)|_{x+\Delta x} $$

and at the left end (pointing leftward, hence negative for rightward net):

左端（向左，故取负）：

$$ F_{\text{left}} = -T\sin\theta(x) \approx -T\,(\partial y/\partial x)|_x. $$

The net upward force on the element is

元素所受净向上的力为

$$ \Delta F = T\,[(\partial y/\partial x)|_{x+\Delta x} - (\partial y/\partial x)|_x]. $$

**Step 3 — Apply Newton's second law.** Newton's second law in the transverse direction for the element is

**第 3 步 — 应用牛顿第二定律。** 对元素在横向应用牛顿第二定律：

$$ \begin{aligned}
\Delta m \cdot \partial^2 y/\partial t^2 &= \Delta F \\
\mu\,\Delta x \cdot \partial^2 y/\partial t^2 &= T\,[(\partial y/\partial x)|_{x+\Delta x} - (\partial y/\partial x)|_x].
\end{aligned} $$

Divide both sides by $\Delta x$ and take the limit $\Delta x \to 0$:

两边除以 $\Delta x$，取极限 $\Delta x \to 0$：

$$ \mu\,\partial^2 y/\partial t^2 = T \cdot \partial/\partial x(\partial y/\partial x) = T\,\partial^2 y/\partial x^2. $$

**Step 4 — Read off the wave speed.** Rearranging:

**第 4 步 — 读出波速。**

$$ \partial^2 y/\partial t^2 = (T/\mu)\,\partial^2 y/\partial x^2. $$

Comparing with the standard wave equation $\partial^2 y/\partial t^2 = c^2\,\partial^2 y/\partial x^2$, we identify

与标准波动方程 $\partial^2 y/\partial t^2 = c^2\,\partial^2 y/\partial x^2$ 比较，得

$$ \boxed{\, c = \sqrt{T/\mu} \,} \qquad \blacksquare $$

**Dimensional check:** $[T] = \mathrm{N} = \mathrm{kg\cdot m/s^2}$, $[\mu] = \mathrm{kg/m}$, so $[T/\mu] = (\mathrm{kg\cdot m/s^2})/(\mathrm{kg/m}) = \mathrm{m^2/s^2}$, and $\sqrt{T/\mu}$ has units of $\mathrm{m/s}$. $\checkmark$

**量纲检验：** $[T] = \mathrm{N} = \mathrm{kg\cdot m/s^2}$，$[\mu] = \mathrm{kg/m}$，故 $[T/\mu] = \mathrm{m^2/s^2}$，$\sqrt{T/\mu}$ 的单位为 $\mathrm{m/s}$。$\checkmark$

---

## B. D'Alembert's General Solution · 达朗贝尔通解

**Claim.** The general solution to the 1D wave equation $\partial^2 y/\partial t^2 = c^2\,\partial^2 y/\partial x^2$ is $y(x, t) = f(x - ct) + g(x + ct)$, where $f$ and $g$ are arbitrary twice-differentiable functions determined by initial conditions.

**命题。** 一维波动方程 $\partial^2 y/\partial t^2 = c^2\,\partial^2 y/\partial x^2$ 的通解为 $y(x, t) = f(x - ct) + g(x + ct)$，其中 $f$ 和 $g$ 为由初始条件决定的任意二次可微函数。

**Step 1 — Change of variables.** Introduce the characteristic coordinates

**第 1 步 — 变量替换。** 引入特征坐标

$$ \xi = x - ct, \qquad \eta = x + ct. $$

Then $\partial/\partial x = (\partial\xi/\partial x)\,\partial/\partial\xi + (\partial\eta/\partial x)\,\partial/\partial\eta = \partial/\partial\xi + \partial/\partial\eta$, and $\partial/\partial t = (\partial\xi/\partial t)\partial/\partial\xi + (\partial\eta/\partial t)\partial/\partial\eta = -c\,\partial/\partial\xi + c\,\partial/\partial\eta$.

则 $\partial/\partial x = \partial/\partial\xi + \partial/\partial\eta$，$\partial/\partial t = -c\,\partial/\partial\xi + c\,\partial/\partial\eta$。

**Step 2 — Transform the wave equation.** Compute the second derivatives:

**第 2 步 — 变换波动方程。** 计算二阶导数：

$$ \begin{aligned}
\partial^2 y/\partial t^2 &= c^2(\partial^2 y/\partial\xi^2 - 2\,\partial^2 y/\partial\xi\partial\eta + \partial^2 y/\partial\eta^2), \\
c^2\,\partial^2 y/\partial x^2 &= c^2(\partial^2 y/\partial\xi^2 + 2\,\partial^2 y/\partial\xi\partial\eta + \partial^2 y/\partial\eta^2).
\end{aligned} $$

Subtracting (wave equation $\partial^2 y/\partial t^2 - c^2\,\partial^2 y/\partial x^2 = 0$):

作差（波动方程 $\partial^2 y/\partial t^2 - c^2\,\partial^2 y/\partial x^2 = 0$）：

$$ \begin{aligned}
c^2(\partial^2 y/\partial\xi^2 - 2\,\partial^2 y/\partial\xi\partial\eta + \partial^2 y/\partial\eta^2) - c^2(\partial^2 y/\partial\xi^2 + 2\,\partial^2 y/\partial\xi\partial\eta + \partial^2 y/\partial\eta^2) &= 0 \\
-4c^2\,\partial^2 y/\partial\xi\partial\eta &= 0 \\
\partial^2 y/\partial\xi\partial\eta &= 0.
\end{aligned} $$

**Step 3 — Integrate.** Integrate once with respect to $\xi$: $\partial y/\partial\eta = G(\eta)$ for some function $G$. Integrate with respect to $\eta$: $y = g(\eta) + f(\xi)$, where $g'(\eta) = G(\eta)$. Substituting back:

**第 3 步 — 积分。** 对 $\xi$ 积分：$\partial y/\partial\eta = G(\eta)$。对 $\eta$ 积分：$y = g(\eta) + f(\xi)$。代回：

$$ \boxed{\, y(x, t) = f(x - ct) + g(x + ct) \,} \qquad \blacksquare $$

**Step 4 — Physical interpretation.** $f(x - ct)$ represents a waveform of arbitrary shape traveling to the right at speed $c$ (the argument $x - ct$ is constant for an observer moving at $+c$). $g(x + ct)$ represents a left-moving wave. Any initial disturbance splits into equal right- and left-moving parts.

**第 4 步 — 物理诠释。** $f(x - ct)$ 表示以速度 $c$ 向右传播的任意形状波形（以 $+c$ 运动的观察者看到 $x - ct$ 为常数）。$g(x + ct)$ 表示向左传播的波。任意初始扰动分裂为等量的向右和向左传播部分。

---

## C. Standing-Wave Quantization: $f_n = nc/2L$ · 驻波量子化

**Claim.** A string of length $L$ fixed at both ends supports standing waves only at discrete frequencies $f_n = nc/(2L)$, $n = 1, 2, 3, \ldots$

**命题。** 两端固定、长度为 $L$ 的弦只支持离散频率 $f_n = nc/(2L)$（$n = 1, 2, 3, \ldots$）的驻波。

**Step 1 — Boundary conditions.** The string is fixed at $x = 0$ and $x = L$, so $y(0, t) = y(L, t) = 0$ for all $t$.

**第 1 步 — 边界条件。** 弦在 $x = 0$ 和 $x = L$ 处固定，故对所有 $t$ 有 $y(0, t) = y(L, t) = 0$。

**Step 2 — Harmonic (normal mode) ansatz.** Try a separable solution $y(x, t) = X(x)\,T(t)$. Substituting into the wave equation:

**第 2 步 — 谐波（简正模式）假设。** 尝试可分离解 $y(x, t) = X(x)\,T(t)$。代入波动方程：

$$ X T'' = c^2 X'' T \implies T''/T = c^2 X''/X = -\omega^2 \quad\text{(constant, negative for oscillatory solutions).} $$

This gives two ODEs: $T'' + \omega^2 T = 0$ and $X'' + k^2 X = 0$, where $k = \omega/c$.

得到两个常微分方程：$T'' + \omega^2 T = 0$，$X'' + k^2 X = 0$，其中 $k = \omega/c$。

**Step 3 — Spatial solution and boundary conditions.** The general spatial solution is $X(x) = A\sin(kx) + B\cos(kx)$. Applying $X(0) = 0$ gives $B = 0$. Applying $X(L) = 0$ gives $A\sin(kL) = 0$. For $A \ne 0$ (non-trivial solution): $\sin(kL) = 0$, so $kL = n\pi$, hence

**第 3 步 — 空间解与边界条件。** 空间通解为 $X(x) = A\sin(kx) + B\cos(kx)$。由 $X(0) = 0$ 得 $B = 0$。由 $X(L) = 0$ 得 $A\sin(kL) = 0$。对于非平凡解（$A \ne 0$）：$\sin(kL) = 0$，故 $kL = n\pi$，从而

$$ k_n = n\pi/L, \qquad n = 1, 2, 3, \ldots $$

**Step 4 — Frequencies.** From the dispersion relation $\omega = ck$:

**第 4 步 — 频率。** 由色散关系 $\omega = ck$：

$$ \omega_n = c k_n = cn\pi/L, \qquad f_n = \omega_n/(2\pi) = \boxed{\, nc/(2L) \,} \qquad \blacksquare $$

**Step 5 — Physical form.** The $n$-th normal mode is

**第 5 步 — 物理形式。** 第 $n$ 个简正模式为

$$ y_n(x, t) = A_n \sin(n\pi x/L)\cos(\omega_n t + \varphi_n), $$

which is a superposition of left- and right-moving waves: $\sin(n\pi x/L)\cos(\omega_n t) = \tfrac12[\sin(k_n x - \omega_n t) + \sin(k_n x + \omega_n t)]$.

即左右传播波的叠加：$\sin(n\pi x/L)\cos(\omega_n t) = \tfrac12[\sin(k_n x - \omega_n t) + \sin(k_n x + \omega_n t)]$。

---

## D. Sound Speed in a Fluid: $c = \sqrt{B/\rho}$ · 流体中的声速推导

**Claim.** A sound wave in a fluid of equilibrium density $\rho_0$ and bulk modulus $B$ ($= -V\,dP/dV$, the resistance to compression) propagates at speed $c = \sqrt{B/\rho_0}$.

**命题。** 在平衡密度为 $\rho_0$、体积模量为 $B$（$= -V\,dP/dV$，对压缩的阻力）的流体中，声波以速度 $c = \sqrt{B/\rho_0}$ 传播。

**Step 1 — Set up small-amplitude perturbations.** Let the equilibrium state have density $\rho_0$, pressure $P_0$. Introduce small perturbations: density $\rho = \rho_0 + \rho'$, pressure $P = P_0 + P'$, and fluid velocity $\mathbf{u}$ (small). The perturbations satisfy $|\rho'/\rho_0| \ll 1$ and $|\mathbf{u}| \ll c$.

**第 1 步 — 建立小振幅扰动。** 设平衡态密度为 $\rho_0$，压强为 $P_0$。引入小扰动：密度 $\rho = \rho_0 + \rho'$，压强 $P = P_0 + P'$，流速 $\mathbf{u}$（小量）。扰动满足 $|\rho'/\rho_0| \ll 1$，$|\mathbf{u}| \ll c$。

**Step 2 — Linearized continuity equation.** The continuity equation $\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{u}) = 0$ linearized (dropping the product $\rho'\mathbf{u}$, which is second order) gives

**第 2 步 — 线性化连续性方程。** 连续性方程 $\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{u}) = 0$ 线性化（略去 $\rho'\mathbf{u}$ 的二阶项）：

$$ \partial\rho'/\partial t + \rho_0\,\nabla\cdot\mathbf{u} = 0. $$

**Step 3 — Linearized Euler equation.** For an inviscid fluid with no body forces, Euler's equation is $\rho(\partial\mathbf{u}/\partial t + \mathbf{u}\cdot\nabla\mathbf{u}) = -\nabla P$. Linearizing (dropping $\rho'\partial\mathbf{u}/\partial t$ and the convective term $\mathbf{u}\cdot\nabla\mathbf{u}$ as second-order small):

**第 3 步 — 线性化欧拉方程。** 对无粘无体力流体，欧拉方程为 $\rho(\partial\mathbf{u}/\partial t + \mathbf{u}\cdot\nabla\mathbf{u}) = -\nabla P$。线性化（略去 $\rho'\partial\mathbf{u}/\partial t$ 及对流项）：

$$ \rho_0\,\partial\mathbf{u}/\partial t = -\nabla P'. $$

**Step 4 — Relate $P'$ to $\rho'$ via the bulk modulus.** The bulk modulus $B$ is defined by $P' = B\,\rho'/\rho_0$ (for adiabatic compression, $B = \gamma P_0$; for isothermal, $B = P_0$). So $\nabla P' = (B/\rho_0)\,\nabla\rho'$.

**第 4 步 — 用体积模量联系 $P'$ 与 $\rho'$。** 体积模量 $B$ 定义使得 $P' = B\,\rho'/\rho_0$（绝热压缩时 $B = \gamma P_0$；等温时 $B = P_0$）。故 $\nabla P' = (B/\rho_0)\,\nabla\rho'$。

**Step 5 — Derive the wave equation for $\rho'$.** Take $\partial/\partial t$ of the continuity equation:

**第 5 步 — 推导 $\rho'$ 的波动方程。** 对连续性方程取 $\partial/\partial t$：

$$ \partial^2\rho'/\partial t^2 + \rho_0\,\partial(\nabla\cdot\mathbf{u})/\partial t = 0. $$

Take $\nabla\cdot$ of the Euler equation:

对欧拉方程取 $\nabla\cdot$：

$$ \rho_0\,\nabla\cdot(\partial\mathbf{u}/\partial t) = -\nabla^2 P' = -(B/\rho_0)\,\nabla^2\rho'. $$

Substituting:

代入：

$$ \partial^2\rho'/\partial t^2 = (B/\rho_0)\,\nabla^2\rho'. $$

This is the wave equation with wave speed

这是波动方程，波速为

$$ \boxed{\, c = \sqrt{B/\rho_0} \,} \qquad \blacksquare $$

**For an ideal gas:** $P = P_0(\rho/\rho_0)^\gamma$ (adiabatic), so $B = \gamma P_0 = \gamma\rho_0 RT/M$ (using the ideal gas law), giving $c = \sqrt{\gamma RT/M}$, which at $T = 293\ \mathrm{K}$, $\gamma = 1.4$, $M = 29\ \mathrm{g/mol}$ gives $c \approx 343\ \mathrm{m/s}$. $\checkmark$

**对理想气体：** $P = P_0(\rho/\rho_0)^\gamma$（绝热），$B = \gamma P_0 = \gamma\rho_0 RT/M$，故 $c = \sqrt{\gamma RT/M}$。在 $T = 293\ \mathrm{K}$，$\gamma = 1.4$，$M = 29\ \mathrm{g/mol}$ 时，$c \approx 343\ \mathrm{m/s}$。$\checkmark$

---

## E. The Doppler Formula · 多普勒公式推导

**Claim.** When a source emits frequency $f_0$ and moves at speed $v_s$ toward the observer, and the observer moves at speed $v_o$ toward the source, through a medium in which sound speed is $c$, the observed frequency is

**命题。** 当声源以频率 $f_0$ 发声，以速度 $v_s$ 向观察者运动，观察者以速度 $v_o$ 向声源运动，介质中声速为 $c$，则观察到的频率为

$$ f = f_0\,\frac{c + v_o}{c - v_s}. $$

**Step 1 — Wavelength in the medium.** The source emits one period every $T_0 = 1/f_0$ seconds. In this time the source moves forward $v_s T_0$. The wavefront emitted one period earlier is now $c T_0$ ahead. The wavelength in the medium is the distance between consecutive wavefronts:

**第 1 步 — 介质中的波长。** 声源每 $T_0 = 1/f_0$ 秒发出一个周期。在此时间内声源向前移动 $v_s T_0$。一个周期前发出的波前此时已在 $c T_0$ 之前。介质中相邻波前间距（波长）为

$$ \lambda = c T_0 - v_s T_0 = (c - v_s)/f_0. $$

(For a receding source replace $-v_s$ with $+v_s$.)

（对于远离的声源，将 $-v_s$ 替换为 $+v_s$。）

**Step 2 — Rate of wavefront arrival at the observer.** The observer moves toward the source at $v_o$, so the relative speed at which wavefronts approach the observer is $c + v_o$ (sum of wave speed and observer speed toward source). The observed frequency is the rate of wavefront arrival:

**第 2 步 — 波前到达观察者的速率。** 观察者以 $v_o$ 向声源运动，波前接近观察者的相对速度为 $c + v_o$。观察到的频率为

$$ f = (c + v_o)/\lambda = (c + v_o) \cdot f_0/(c - v_s) = f_0\,\boxed{\,\frac{c + v_o}{c - v_s}\,} \qquad \blacksquare $$

**Sign conventions:** Use $+$ in numerator when observer moves toward source, $-$ when moving away. Use $-$ in denominator when source moves toward observer, $+$ when moving away.

**符号约定：** 分子取 $+$ 当观察者向声源运动，取 $-$ 当远离。分母取 $-$ 当声源向观察者运动，取 $+$ 当远离。

**Note:** This is the classical Doppler formula for sound waves in a medium; it distinguishes between source motion and observer motion (unlike the relativistic Doppler formula for light, which depends only on relative velocity and which we derived in Module 1.14-derivations Section C).

**注：** 这是声波在介质中的经典多普勒公式；它区分声源运动和观察者运动（与光的相对论多普勒公式不同，后者仅依赖相对速度，见模块 1.14 推导文档第 C 节）。

---

## F. Phase Velocity vs Group Velocity: $v_g = d\omega/dk$ · 相速度与群速度

**Claim.** For a dispersive medium (where $\omega$ is not simply proportional to $k$), the phase velocity $v_p = \omega/k$ and the group velocity $v_g = d\omega/dk$ are in general different. The group velocity governs the propagation of energy and wave packets.

**命题。** 在色散介质（$\omega$ 与 $k$ 不成简单正比）中，相速度 $v_p = \omega/k$ 与群速度 $v_g = d\omega/dk$ 一般不同。群速度支配能量和波包的传播。

**Step 1 — Superpose two nearby plane waves.** Consider two waves of slightly different frequencies and wavenumbers:

**第 1 步 — 叠加两列频率相近的平面波。** 考虑频率和波数略有不同的两列波：

$$ y_1 = A\cos(k_1 x - \omega_1 t), \qquad y_2 = A\cos(k_2 x - \omega_2 t), $$

with $k_1 = k + \Delta k$, $k_2 = k - \Delta k$, $\omega_1 = \omega + \Delta\omega$, $\omega_2 = \omega - \Delta\omega$ (so $\Delta k, \Delta\omega \ll k, \omega$).

其中 $k_1 = k + \Delta k$，$k_2 = k - \Delta k$，$\omega_1 = \omega + \Delta\omega$，$\omega_2 = \omega - \Delta\omega$（$\Delta k, \Delta\omega \ll k, \omega$）。

**Step 2 — Use sum-to-product identity.** The sum $y_1 + y_2$:

**第 2 步 — 和差化积。** 叠加 $y_1 + y_2$：

$$ y = 2A\cos(\Delta k \cdot x - \Delta\omega \cdot t) \cdot \cos(kx - \omega t). $$

This is a **carrier wave** $\cos(kx - \omega t)$ modulated by a slowly varying **envelope** $\cos(\Delta k \cdot x - \Delta\omega \cdot t)$.

这是**载波** $\cos(kx - \omega t)$ 被缓变**包络** $\cos(\Delta k \cdot x - \Delta\omega \cdot t)$ 调制。

**Step 3 — Identify the two velocities.** 

**第 3 步 — 识别两个速度。**

- The carrier moves at the **phase velocity** $v_p = \omega/k$ (the speed at which a constant phase $kx - \omega t = \text{const}$ propagates: $dx/dt = \omega/k$).

- 载波以**相速度** $v_p = \omega/k$ 传播（等相面 $kx - \omega t = \text{const}$ 的传播速度：$dx/dt = \omega/k$）。

- The envelope moves at the **group velocity** $v_g = \Delta\omega/\Delta k \to d\omega/dk$ in the limit $\Delta k \to 0$ (the speed at which a constant envelope phase $\Delta k \cdot x - \Delta\omega \cdot t = \text{const}$ propagates: $dx/dt = \Delta\omega/\Delta k$).

- 包络以**群速度** $v_g = \Delta\omega/\Delta k \to d\omega/dk$（$\Delta k \to 0$ 极限）传播（等包络相 $\Delta k \cdot x - \Delta\omega \cdot t = \text{const}$ 的传播速度）。

**Step 4 — Energy and information travel at the group velocity.** In a non-dispersive medium $\omega = ck$, so $d\omega/dk = c = \omega/k$: phase and group velocities coincide. In a dispersive medium (e.g. water waves, optical fiber, plasma), $v_g \ne v_p$. The energy and signal velocity equal $v_g$ (proved by calculating the energy flux: the Poynting-like flux is proportional to $d\omega/dk$). For deep-water gravity waves ($\omega = \sqrt{gk}$), $v_g = \tfrac12 v_p$ — the envelope moves at half the phase speed.

**第 4 步 — 能量和信息以群速度传播。** 在无色散介质中 $\omega = ck$，故 $d\omega/dk = c = \omega/k$：相速度与群速度相同。在色散介质（如水波、光纤、等离子体）中，$v_g \ne v_p$。能量和信号速度等于 $v_g$（通过计算能量通量证明：类坡印亭通量正比于 $d\omega/dk$）。对于深水重力波（$\omega = \sqrt{gk}$），$v_g = \tfrac12 v_p$——包络以相速度的一半传播。$\blacksquare$

**Step 5 — Relation to the dispersion relation.** Expanding $\omega(k)$ in a Taylor series about $k_0$:

**第 5 步 — 与色散关系的联系。** 在 $k_0$ 处将 $\omega(k)$ 展开为泰勒级数：

$$ \omega(k) = \omega_0 + (d\omega/dk)_0\,(k - k_0) + \tfrac12(d^2\omega/dk^2)_0\,(k - k_0)^2 + \cdots $$

The first-order term gives the group velocity; the second-order term (group velocity dispersion, GVD) causes the wave packet to spread. In optical fibers, GVD limits the bandwidth-distance product and is compensated by dispersion-shifted fiber.

一阶项给出群速度；二阶项（群速度色散，GVD）导致波包展宽。在光纤中，GVD 限制带宽-距离乘积，可通过色散位移光纤补偿。$\blacksquare$

---

*The wave equation, d'Alembert's solution, boundary quantization, and the phase/group velocity distinction are the universal tools of wave physics — appearing identically in acoustic, elastic, electromagnetic, plasma, and quantum-mechanical waves throughout the curriculum.*

*波动方程、达朗贝尔解、边界量子化和相/群速度的区别是波动物理学的通用工具——在整个课程的声波、弹性波、电磁波、等离子体波和量子力学波中同样出现。*

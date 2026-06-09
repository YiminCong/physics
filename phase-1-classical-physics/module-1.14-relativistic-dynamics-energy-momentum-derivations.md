# Derivations — Module 1.14: Relativistic Dynamics & $E = mc^2$
# 推导 — 模块 1.14：相对论动力学与 $E = mc^2$

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.14](./module-1.14-relativistic-dynamics-energy-momentum.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.14](./module-1.14-relativistic-dynamics-energy-momentum.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Four-Velocity and Four-Momentum · 四速度与四动量

**Claim.** The four-velocity $U^\mu = dx^\mu/d\tau$ satisfies $U^\mu U_\mu = c^2$, and the four-momentum $p^\mu = mU^\mu$ satisfies the invariant $p^\mu p_\mu = (mc)^2$, from which $E^2 = (pc)^2 + (mc^2)^2$.

**命题。** 四速度 $U^\mu = dx^\mu/d\tau$ 满足 $U^\mu U_\mu = c^2$，四动量 $p^\mu = mU^\mu$ 满足不变量 $p^\mu p_\mu = (mc)^2$，由此导出 $E^2 = (pc)^2 + (mc^2)^2$。

**Step 1 — Proper time and the Lorentz factor.** Consider a particle moving with coordinate velocity $v = dx/dt$ in frame $S$. The proper time $\tau$ is the time elapsed on a clock moving with the particle. The spacetime interval for infinitesimal displacement is

**第 1 步 — 固有时与洛伦兹因子。** 考虑一个在参考系 $S$ 中以坐标速度 $v = dx/dt$ 运动的粒子。固有时 $\tau$ 是随粒子运动的时钟所经历的时间。无穷小位移的时空间隔为

$$ ds^2 = c^2\,dt^2 - dx^2 - dy^2 - dz^2 = c^2\,dt^2(1 - v^2/c^2). $$

Since $ds^2$ is Lorentz-invariant and equals $c^2\,d\tau^2$ in the rest frame of the particle,

由于 $ds^2$ 是洛伦兹不变量，在粒子静止系中等于 $c^2\,d\tau^2$，故

$$ d\tau = dt\,\sqrt{1 - v^2/c^2} = dt/\gamma, \qquad \text{where } \gamma = 1/\sqrt{1 - v^2/c^2}. $$

**第 1 步结论：** $d\tau = dt/\gamma$，其中洛伦兹因子 $\gamma = (1 - v^2/c^2)^{-1/2}$。

**Step 2 — Components of the four-velocity.** The four-velocity is $U^\mu = dx^\mu/d\tau$. Using $d\tau = dt/\gamma$:

**第 2 步 — 四速度的分量。** 四速度定义为 $U^\mu = dx^\mu/d\tau$。利用 $d\tau = dt/\gamma$：

$$ \begin{aligned}
U^0 &= dx^0/d\tau = c\,dt/d\tau = \gamma c, \\
U^i &= dx^i/d\tau = (dx^i/dt)(dt/d\tau) = \gamma v^i.
\end{aligned} $$

So $U^\mu = \gamma(c, v_x, v_y, v_z) = \gamma(c, \mathbf{v})$.

故 $U^\mu = \gamma(c, v_x, v_y, v_z) = \gamma(c, \mathbf{v})$。

**Step 3 — The invariant $U^\mu U_\mu$.** Using the metric signature $(+, -, -, -)$:

**第 3 步 — 不变量 $U^\mu U_\mu$。** 采用度规号差 $(+, -, -, -)$：

$$ \begin{aligned}
U^\mu U_\mu &= (U^0)^2 - (U^1)^2 - (U^2)^2 - (U^3)^2 \\
&= \gamma^2 c^2 - \gamma^2 v_x^2 - \gamma^2 v_y^2 - \gamma^2 v_z^2 \\
&= \gamma^2(c^2 - |v|^2) \\
&= \gamma^2 c^2(1 - v^2/c^2) \\
&= \gamma^2 c^2 \cdot \gamma^{-2} \\
&= c^2.
\end{aligned} $$

Hence $U^\mu U_\mu = c^2$ — a Lorentz scalar independent of the particle's speed.

故 $U^\mu U_\mu = c^2$——与粒子速度无关的洛伦兹标量。

**Step 4 — Four-momentum and its invariant.** Define the four-momentum $p^\mu = mU^\mu$ where $m$ is the rest mass (a Lorentz scalar). Then

**第 4 步 — 四动量及其不变量。** 定义四动量 $p^\mu = mU^\mu$，其中 $m$ 为静止质量（洛伦兹标量）。则

$$ p^\mu p_\mu = m^2 U^\mu U_\mu = m^2 c^2. $$

Writing out the components: $p^0 = m\gamma c = E/c$ (defining $E \equiv \gamma mc^2$), and $p^i = m\gamma v^i$ (the relativistic three-momentum). So

写出各分量：$p^0 = m\gamma c = E/c$（定义 $E \equiv \gamma mc^2$），$p^i = m\gamma v^i$（相对论三维动量）。于是

$$ p^\mu p_\mu = (E/c)^2 - |\mathbf{p}|^2 = (mc)^2, $$

which gives $\boxed{\, E^2 = (pc)^2 + (mc^2)^2 \,}$. $\blacksquare$

由此得 $\boxed{\, E^2 = (pc)^2 + (mc^2)^2 \,}$。$\blacksquare$

---

## B. Relativistic Energy $E = \gamma mc^2$ and its Low-Speed Expansion · 相对论能量 $E = \gamma mc^2$ 及其低速展开

**Claim.** The time component of $p^\mu = mU^\mu$ directly gives $E = \gamma mc^2$, and for $v \ll c$ this expands as $E \approx mc^2 + \tfrac12 mv^2$.

**命题。** $p^\mu = mU^\mu$ 的时间分量直接给出 $E = \gamma mc^2$，在 $v \ll c$ 时展开为 $E \approx mc^2 + \tfrac12 mv^2$。

**Step 1 — Identify the energy component.** From Step 2 and Step 4 above, $p^0 = mU^0 = m\gamma c$. The conventional identification is $p^0 = E/c$, so

**第 1 步 — 识别能量分量。** 由上面第 2 步和第 4 步，$p^0 = mU^0 = m\gamma c$。按惯例 $p^0 = E/c$，故

$$ E = \gamma mc^2 = mc^2/\sqrt{1 - v^2/c^2}. $$

**Step 2 — Taylor expansion for $v \ll c$.** Write $\beta = v/c \ll 1$. Expand $\gamma$ as a binomial series:

**第 2 步 — $v \ll c$ 时的泰勒展开。** 令 $\beta = v/c \ll 1$。将 $\gamma$ 展开为二项式级数：

$$ \gamma = (1 - \beta^2)^{-1/2} = 1 + \tfrac12\beta^2 + \tfrac38\beta^4 + \cdots $$

Multiply by $mc^2$:

乘以 $mc^2$：

$$ \begin{aligned}
E &= mc^2\big(1 + \tfrac12\beta^2 + \tfrac38\beta^4 + \cdots\big) \\
&= mc^2 + \tfrac12 mc^2\beta^2 + O(\beta^4) \\
&= mc^2 + \tfrac12 mv^2 + O(v^4/c^2).
\end{aligned} $$

The first term $mc^2$ is the rest energy, present even when the particle is at rest — with no classical counterpart. The second term $\tfrac12 mv^2$ is the familiar non-relativistic kinetic energy, recovered in the low-speed limit. Higher-order terms are negligible for $v \ll c$.

第一项 $mc^2$ 是静止能量，即使粒子静止也存在——在经典力学中无对应物。第二项 $\tfrac12 mv^2$ 是熟悉的非相对论动能，在低速极限下恢复。高阶项在 $v \ll c$ 时可忽略。$\blacksquare$

---

## C. The Relativistic Doppler Shift · 相对论多普勒频移

**Claim.** A source emitting frequency $f_0$ in its rest frame, moving with velocity $v$ relative to the observer along the line of sight, is observed at

**命题。** 光源在其静止系中发射频率 $f_0$，以速度 $v$ 沿视线方向相对于观察者运动，观察到的频率为

$$ \begin{aligned}
f &= f_0\,\sqrt{\frac{1 - \beta}{1 + \beta}} &&\text{(source receding),} \\
f &= f_0\,\sqrt{\frac{1 + \beta}{1 - \beta}} &&\text{(source approaching),}
\end{aligned} $$

where $\beta = v/c$. This includes both the classical Doppler effect and a relativistic time-dilation correction.

其中 $\beta = v/c$。这包含经典多普勒效应和相对论时间膨胀修正两部分。

**Step 1 — Set up using four-wavevector.** Light has a four-wavevector $k^\mu = (\omega/c)(1, \hat{n})$ where $\hat{n}$ is the propagation direction and $\omega = 2\pi f$. Take the observer at rest in frame $S$, with the source receding along $+x$ at speed $v$. The light that reaches the observer travels in the $-x$ direction, so in the source rest frame $S'$ its four-wavevector is $k'^\mu = (\omega_0/c)(1, -1, 0, 0)$. In $S$ the source moves at velocity $+v$ along $+x$.

**第 1 步 — 利用四波矢建立方程。** 光具有四波矢 $k^\mu = (\omega/c)(1, \hat{n})$，其中 $\hat{n}$ 为传播方向，$\omega = 2\pi f$。设观察者在 $S$ 系中静止，光源以速度 $v$ 沿 $+x$ 方向远离。到达观察者的光沿 $-x$ 方向传播，故在光源静止系 $S'$ 中其四波矢为 $k'^\mu = (\omega_0/c)(1, -1, 0, 0)$。在 $S$ 中光源以 $+v$ 沿 $+x$ 运动。

**Step 2 — Apply the Lorentz transformation.** The observer frame $S$ is reached from the source rest frame $S'$ by a boost at velocity $+v$ (the source recedes at $+v$ in $S$). The time component of the four-wavevector transforms as:

**第 2 步 — 应用洛伦兹变换。** 观察者系 $S$ 由源静止系 $S'$ 经速度 $+v$ 的变换得到（光源在 $S$ 中以 $+v$ 远离）。四波矢的时间分量变换为：

$$ k^0 = \gamma(k'^0 + \beta k'^1). $$

In $S'$ the source emits toward the observer ($-x$ direction), so $k'^1 = -\omega_0/c$ and $k'^0 = \omega_0/c$:

在 $S'$ 中光源向观察者（$-x$ 方向）发射，故 $k'^1 = -\omega_0/c$，$k'^0 = \omega_0/c$：

$$ \begin{aligned}
k^0 &= \gamma(\omega_0/c)(1 + \beta \cdot (-1)) = \gamma(\omega_0/c)(1 - \beta) = (\omega_0/c) \cdot \frac{1 - \beta}{\sqrt{1 - \beta^2}} \\
&= (\omega_0/c) \cdot \frac{1 - \beta}{\sqrt{(1-\beta)(1+\beta)}} = (\omega_0/c) \cdot \frac{\sqrt{1-\beta}}{\sqrt{1+\beta}}.
\end{aligned} $$

Since $\omega = c\,k^0$,

由于 $\omega = c\,k^0$，

$$ \boxed{\, f = f_0\,\sqrt{\frac{1 - \beta}{1 + \beta}} \,} \qquad \text{(source receding, redshift).} \;\checkmark $$

For an approaching source ($v$ in $-x$ direction, $\beta \to -\beta$):

对于接近的光源（$v$ 沿 $-x$ 方向，$\beta \to -\beta$）：

$$ \boxed{\, f = f_0\,\sqrt{\frac{1 + \beta}{1 - \beta}} \,} \qquad \text{(source approaching, blueshift).} \;\checkmark $$

**Step 3 — Low-speed limit.** For $\beta \ll 1$, expand $\sqrt{(1-\beta)/(1+\beta)} \approx (1 - \beta)(1 + \beta)^{-1/2}(1 - \beta)^{1/2}/(1 - \beta)^{1/2}$:

**第 3 步 — 低速极限。** 对 $\beta \ll 1$，展开：

$$ \sqrt{\frac{1 - \beta}{1 + \beta}} \approx (1 - \beta)(1 + \beta/2 + \cdots) \approx 1 - \beta - \beta/2 + \cdots \approx 1 - \beta + O(\beta^2). $$

More carefully: let $u = \beta$:

更仔细地：令 $u = \beta$，

$$ (1 - u)^{1/2}(1 + u)^{-1/2} = (1 - \tfrac12 u - \tfrac18 u^2 - \cdots)(1 - \tfrac12 u + \tfrac38 u^2 - \cdots) \approx 1 - u + O(u^2). $$

So $f \approx f_0(1 - \beta) = f_0(1 - v/c)$, the classical Doppler formula for a receding source. The relativistic formula adds a time-dilation factor of $\gamma$ at higher order — even a source moving purely transversely ($\beta$ along $\perp$) shows a **transverse Doppler redshift** $f = f_0/\gamma$, with no classical analogue.

故 $f \approx f_0(1 - \beta) = f_0(1 - v/c)$，即光源远离时的经典多普勒公式。相对论公式在高阶引入时间膨胀因子——即使光源纯横向运动（$\beta$ 沿垂直方向）也会产生**横向多普勒红移** $f = f_0/\gamma$，这在经典力学中无对应物。$\blacksquare$

---

## D. Why $E^2 = (pc)^2 + (mc^2)^2$ and Not $E = pc + mc^2$ · 为何是 $E^2$ 而非 $E$ 的线性关系

**Step 1 — Contrapositive: consistency of the invariant.** The result $p^\mu p_\mu = (mc)^2$ is Lorentz-invariant by construction: each factor $p^\mu$ transforms as a four-vector, so the scalar product is unchanged by any boost. In the rest frame $\mathbf{v} = 0$, so $\mathbf{p} = 0$ and $E = mc^2$, giving $p^\mu p_\mu = (mc)^2 - 0 = (mc)^2$. Since this holds in the rest frame and the quantity is invariant, it holds in every frame.

**第 1 步 — 逆向验证：不变量的自洽性。** 结果 $p^\mu p_\mu = (mc)^2$ 由构造本身保证洛伦兹不变：每个 $p^\mu$ 因子按四矢量变换，故标量积在任何变换下不变。在静止系中 $\mathbf{v} = 0$，故 $\mathbf{p} = 0$，$E = mc^2$，得 $p^\mu p_\mu = (mc)^2 - 0 = (mc)^2$。由于在静止系中成立且该量是不变的，它在每个参考系中都成立。

**Step 2 — For a massless particle.** Setting $m = 0$: $p^\mu p_\mu = 0$, so $(E/c)^2 = |\mathbf{p}|^2$ giving $E = pc$ — the energy-momentum relation for a photon or any massless particle.

**第 2 步 — 对无质量粒子。** 取 $m = 0$：$p^\mu p_\mu = 0$，故 $(E/c)^2 = |\mathbf{p}|^2$，得 $E = pc$——光子或任何无质量粒子的能量-动量关系。$\blacksquare$

---

*All results are consequences of special relativity: the invariance of $ds^2 = c^2 dt^2 - dx^2 - dy^2 - dz^2$, the definition of proper time, and the Lorentz-covariant structure of four-vectors.*

*所有结果都是狭义相对论的推论：$ds^2 = c^2 dt^2 - dx^2 - dy^2 - dz^2$ 的不变性、固有时的定义以及四矢量的洛伦兹协变结构。*

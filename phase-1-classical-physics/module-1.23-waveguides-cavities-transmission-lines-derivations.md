---
title: "Derivations — Module 1.23: Waveguides, Cavity Resonators & Transmission Lines"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.23: Waveguides, Cavity Resonators & Transmission Lines
# 推导 — 模块 1.23：波导、谐振腔与传输线

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.23](./module-1.23-waveguides-cavities-transmission-lines.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.23](./module-1.23-waveguides-cavities-transmission-lines.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Guided-Wave Separation and Mode Classification · 导波分离与模式分类

**Claim.** For monochromatic fields $\propto e^{i(k_z z - \omega t)}$ inside a hollow conductor, Maxwell's equations reduce to a 2-D transverse Helmholtz equation $(\nabla_t^2 + \gamma^2)\psi = 0$ with $\gamma^2 = \omega^2/c^2 - k_z^2$, where $\psi$ stands for $E_z$ or $B_z$. Modes split into TE ($E_z = 0$), TM ($B_z = 0$), and TEM ($E_z = B_z = 0$); a single hollow conductor supports no TEM mode.

**命题。** 对空心导体内 $\propto e^{i(k_z z - \omega t)}$ 的单色场，麦克斯韦方程组化为二维横向亥姆霍兹方程 $(\nabla_t^2 + \gamma^2)\psi = 0$，其中 $\gamma^2 = \omega^2/c^2 - k_z^2$，$\psi$ 代表 $E_z$ 或 $B_z$。模式分为 TE（$E_z = 0$）、TM（$B_z = 0$）和 TEM（$E_z = B_z = 0$）；单一空心导体不支持 TEM 模式。

**Step 1 — Source-free wave equation.** Inside a perfect hollow conductor the fields satisfy the source-free Maxwell equations (Module 1.10). Taking the curl of Faraday's law and using Ampère's law gives the vacuum wave equation for each Cartesian field component:

**第 1 步 — 无源波动方程。** 在理想空心导体内，场满足无源麦克斯韦方程（模块 1.10）。对法拉第定律取旋度并用安培定律，得每个笛卡尔场分量的真空波动方程：

$$ \left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\mathbf{E} = 0, \qquad \left(\nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\mathbf{B} = 0. $$

**Step 2 — Insert the propagating ansatz.** Write every field component as $F(x, y, z, t) = f(x, y) e^{i(k_z z - \omega t)}$. Then $\partial^2/\partial z^2 \to -k_z^2$, $\partial^2/\partial t^2 \to -\omega^2$, and the Laplacian splits as $\nabla^2 = \nabla_t^2 + \partial^2/\partial z^2$, where $\nabla_t^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2$ is the transverse Laplacian. Substituting:

**第 2 步 — 代入传播拟设。** 将每个场分量写为 $F(x, y, z, t) = f(x, y) e^{i(k_z z - \omega t)}$。则 $\partial^2/\partial z^2 \to -k_z^2$，$\partial^2/\partial t^2 \to -\omega^2$，拉普拉斯算子分裂为 $\nabla^2 = \nabla_t^2 + \partial^2/\partial z^2$，其中 $\nabla_t^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2$ 为横向拉普拉斯算子。代入：

$$ \left(\nabla_t^2 - k_z^2 + \omega^2/c^2\right) f = 0 \implies (\nabla_t^2 + \gamma^2) f = 0, \qquad \gamma^2 \equiv \omega^2/c^2 - k_z^2. $$

In particular the longitudinal components satisfy $(\nabla_t^2 + \gamma^2)E_z = 0$ and $(\nabla_t^2 + \gamma^2)B_z = 0$. This is the **transverse Helmholtz equation** (a 2-D eigenvalue problem, Module 1.8).

特别地，纵向分量满足 $(\nabla_t^2 + \gamma^2)E_z = 0$ 与 $(\nabla_t^2 + \gamma^2)B_z = 0$。这就是**横向亥姆霍兹方程**（二维本征值问题，模块 1.8）。

**Step 3 — Transverse fields follow from $E_z, B_z$.** The two curl equations, written component-by-component with $\partial_z \to ik_z$ and $\partial_t \to -i\omega$, let the four transverse field components be expressed algebraically in terms of the longitudinal ones. Solving the coupled pair gives

**第 3 步 — 横向场由 $E_z$、$B_z$ 决定。** 两个旋度方程逐分量写出（$\partial_z \to ik_z$，$\partial_t \to -i\omega$），可将四个横向场分量用纵向分量代数地表示。求解耦合对得

$$ \mathbf{E}_t = \frac{i}{\gamma^2}(k_z \boldsymbol{\nabla}_t E_z - \omega\,\hat{\mathbf{z}} \times \boldsymbol{\nabla}_t B_z), \qquad \mathbf{B}_t = \frac{i}{\gamma^2}\left(k_z \boldsymbol{\nabla}_t B_z + \frac{\omega}{c^2}\hat{\mathbf{z}} \times \boldsymbol{\nabla}_t E_z\right). $$

Thus once $E_z$ and $B_z$ are known, the entire field is determined — provided $\gamma^2 \ne 0$. The boundary conditions on a perfect conductor are $E_z = 0$ on the wall (tangential $\mathbf{E}$ vanishes) and $\partial B_z/\partial n = 0$ on the wall (normal $\mathbf{B}$ vanishes).

故一旦 $E_z$ 与 $B_z$ 已知，全部场即被确定——前提是 $\gamma^2 \ne 0$。理想导体上的边界条件为壁面上 $E_z = 0$（切向 $\mathbf{E}$ 为零）与壁面上 $\partial B_z/\partial n = 0$（法向 $\mathbf{B}$ 为零）。

**Step 4 — Mode classification.** Because the transverse fields are built from $E_z$ and $B_z$, modes are classified by which longitudinal component is nonzero:

**第 4 步 — 模式分类。** 由于横向场由 $E_z$ 与 $B_z$ 构造，模式按哪个纵向分量非零来分类：

- **TM (transverse magnetic):** $B_z = 0$, $E_z \ne 0$. Solve $(\nabla_t^2 + \gamma^2)E_z = 0$ with $E_z = 0$ on the wall (Dirichlet).
- **TE (transverse electric):** $E_z = 0$, $B_z \ne 0$. Solve $(\nabla_t^2 + \gamma^2)B_z = 0$ with $\partial B_z/\partial n = 0$ on the wall (Neumann).
- **TEM (transverse electromagnetic):** $E_z = B_z = 0$.

- **TM（横磁）：** $B_z = 0$，$E_z \ne 0$。在壁面 $E_z = 0$（狄利克雷）下解 $(\nabla_t^2 + \gamma^2)E_z = 0$。
- **TE（横电）：** $E_z = 0$，$B_z \ne 0$。在壁面 $\partial B_z/\partial n = 0$（诺伊曼）下解 $(\nabla_t^2 + \gamma^2)B_z = 0$。
- **TEM（横电磁）：** $E_z = B_z = 0$。

**Step 5 — A single hollow conductor has no TEM mode.** For a TEM mode $E_z = B_z = 0$, so the transverse-field relations above are satisfied only if $\gamma^2 = 0$, i.e. $k_z = \omega/c$ (waves travel at the speed of light, dispersionless). With $\gamma^2 = 0$ the transverse Helmholtz equation becomes Laplace's equation $\nabla_t^2\psi = 0$ for the transverse potential, since $\mathbf{E}_t = -\boldsymbol{\nabla}_t\Phi$ is curl-free and divergence-free in the transverse plane.

**第 5 步 — 单一空心导体没有 TEM 模式。** 对 TEM 模式 $E_z = B_z = 0$，故上述横向场关系仅当 $\gamma^2 = 0$（即 $k_z = \omega/c$，波以光速无色散传播）时成立。当 $\gamma^2 = 0$ 时，横向亥姆霍兹方程化为横向势的拉普拉斯方程 $\nabla_t^2\Phi = 0$，因横向场 $\mathbf{E}_t = -\boldsymbol{\nabla}_t\Phi$ 在横向平面内无旋且无散。

A single hollow conductor has a single closed boundary curve, on which $\Phi$ is constant (the wall is an equipotential). By the uniqueness theorem for Laplace's equation (Module 1.8), a harmonic function that is constant on the entire boundary of a simply connected region is constant everywhere inside, so $\boldsymbol{\nabla}_t\Phi = 0$ and $\mathbf{E}_t = 0$: the TEM field vanishes identically. To support a nonzero TEM potential difference one needs **two separate conductors** (e.g. inner and outer of a coaxial cable) held at different potentials. $\blacksquare$

单一空心导体只有一条闭合边界曲线，$\Phi$ 在其上为常数（壁为等势面）。由拉普拉斯方程的唯一性定理（模块 1.8），在单连通区域整个边界上为常数的调和函数在内部处处为该常数，故 $\boldsymbol{\nabla}_t\Phi = 0$ 且 $\mathbf{E}_t = 0$：TEM 场恒为零。要支持非零的 TEM 电势差，需要**两个分离的导体**（如同轴电缆的内外导体）处于不同电位。$\blacksquare$

---

## B. Rectangular Waveguide: Cutoff, Dispersion, and Velocities · 矩形波导：截止、色散与速度

**Claim.** For a rectangular guide with walls at $x = 0, a$ and $y = 0, b$, the $\text{TE}_{mn}$ modes have $\gamma^2_{mn} = (m\pi/a)^2 + (n\pi/b)^2$ and cutoff frequency $\omega_c = c\pi\sqrt{(m/a)^2 + (n/b)^2}$. The dispersion relation is $k_z = \sqrt{\omega^2 - \omega_c^2}/c$. The phase and group velocities satisfy $v_p = c/\sqrt{1 - (\omega_c/\omega)^2} > c$, $v_g = c\sqrt{1 - (\omega_c/\omega)^2} < c$, and $v_p v_g = c^2$.

**命题。** 对壁在 $x = 0, a$ 与 $y = 0, b$ 的矩形波导，$\text{TE}_{mn}$ 模有 $\gamma^2_{mn} = (m\pi/a)^2 + (n\pi/b)^2$，截止频率 $\omega_c = c\pi\sqrt{(m/a)^2 + (n/b)^2}$。色散关系为 $k_z = \sqrt{\omega^2 - \omega_c^2}/c$。相速度与群速度满足 $v_p = c/\sqrt{1 - (\omega_c/\omega)^2} > c$，$v_g = c\sqrt{1 - (\omega_c/\omega)^2} < c$，且 $v_p v_g = c^2$。

**Step 1 — Separate the transverse Helmholtz equation.** For TE modes solve $(\partial^2/\partial x^2 + \partial^2/\partial y^2 + \gamma^2)B_z = 0$. Separate variables $B_z(x, y) = X(x)Y(y)$ (Module 1.8):

**第 1 步 — 分离横向亥姆霍兹方程。** 对 TE 模解 $(\partial^2/\partial x^2 + \partial^2/\partial y^2 + \gamma^2)B_z = 0$。分离变量 $B_z(x, y) = X(x)Y(y)$（模块 1.8）：

$$ X''/X + Y''/Y + \gamma^2 = 0 \implies X''/X = -k_x^2, \quad Y''/Y = -k_y^2, \quad \text{with } k_x^2 + k_y^2 = \gamma^2. $$

The general solution is $X = A\cos(k_x x) + B\sin(k_x x)$, $Y = C\cos(k_y y) + D\sin(k_y y)$.

通解为 $X = A\cos(k_x x) + B\sin(k_x x)$，$Y = C\cos(k_y y) + D\sin(k_y y)$。

**Step 2 — Apply the Neumann boundary conditions.** For TE modes $\partial B_z/\partial n = 0$ on the walls. On $x = 0$ and $x = a$: $\partial B_z/\partial x = 0$. This requires the sine term to vanish ($B = 0$) and $\sin(k_x a) = 0$, so $k_x = m\pi/a$, $m = 0, 1, 2, \dots$ Likewise on $y = 0, b$: $k_y = n\pi/b$, $n = 0, 1, 2, \dots$ Hence

**第 2 步 — 应用诺伊曼边界条件。** 对 TE 模壁面上 $\partial B_z/\partial n = 0$。在 $x = 0$ 与 $x = a$：$\partial B_z/\partial x = 0$，要求正弦项消失（$B = 0$）且 $\sin(k_x a) = 0$，故 $k_x = m\pi/a$，$m = 0, 1, 2, \dots$；同样在 $y = 0, b$：$k_y = n\pi/b$，$n = 0, 1, 2, \dots$。故

$$ B_z(x, y) = B_0 \cos(m\pi x/a)\cos(n\pi y/b), \qquad \gamma^2_{mn} = (m\pi/a)^2 + (n\pi/b)^2. $$

(The mode $m = n = 0$ gives a constant $B_z$ with zero transverse fields and is excluded; the lowest nontrivial TE mode is $\text{TE}_{10}$.)

（$m = n = 0$ 模给出常数 $B_z$、横向场为零，被排除；最低非平凡 TE 模为 $\text{TE}_{10}$。）

**Step 3 — Cutoff frequency.** Recall $\gamma^2 = \omega^2/c^2 - k_z^2$. Solving for $k_z$:

**第 3 步 — 截止频率。** 回忆 $\gamma^2 = \omega^2/c^2 - k_z^2$。解出 $k_z$：

$$ k_z^2 = \omega^2/c^2 - \gamma^2_{mn} = \omega^2/c^2 - [(m\pi/a)^2 + (n\pi/b)^2]. $$

Real propagation ($k_z$ real) requires $\omega^2/c^2 > \gamma^2_{mn}$. The threshold $\omega$ at which $k_z = 0$ defines the **cutoff frequency**:

实传播（$k_z$ 实）要求 $\omega^2/c^2 > \gamma^2_{mn}$。$k_z = 0$ 处的临界 $\omega$ 定义**截止频率**：

$$ \omega_c^2/c^2 = \gamma^2_{mn} = (m\pi/a)^2 + (n\pi/b)^2 \implies \boxed{\, \omega_c = c\pi\sqrt{(m/a)^2 + (n/b)^2} \,}. $$

For the lowest mode $\text{TE}_{10}$ ($m = 1, n = 0$): $\omega_c = c\pi/a$.

对最低模 $\text{TE}_{10}$（$m = 1, n = 0$）：$\omega_c = c\pi/a$。

**Step 4 — Dispersion relation.** Substituting $\gamma^2_{mn} = \omega_c^2/c^2$ into $k_z^2 = \omega^2/c^2 - \gamma^2_{mn}$:

**第 4 步 — 色散关系。** 将 $\gamma^2_{mn} = \omega_c^2/c^2$ 代入 $k_z^2 = \omega^2/c^2 - \gamma^2_{mn}$：

$$ k_z^2 = (\omega^2 - \omega_c^2)/c^2 \implies \boxed{\, k_z = \sqrt{\omega^2 - \omega_c^2}/c \,} \quad (\omega > \omega_c). $$

For $\omega < \omega_c$, $k_z$ is imaginary: the wave decays as $e^{-|k_z|z}$ (evanescent, no propagation). The guide is a high-pass filter.

对 $\omega < \omega_c$，$k_z$ 为虚数：波按 $e^{-|k_z|z}$ 衰减（消逝，不传播）。波导是高通滤波器。

**Step 5 — Phase velocity.** The phase velocity is $v_p = \omega/k_z$. Using $k_z = \sqrt{\omega^2 - \omega_c^2}/c$:

**第 5 步 — 相速度。** 相速度 $v_p = \omega/k_z$。用 $k_z = \sqrt{\omega^2 - \omega_c^2}/c$：

$$ v_p = \frac{\omega}{\sqrt{\omega^2 - \omega_c^2}/c} = \frac{c\omega}{\sqrt{\omega^2 - \omega_c^2}} = \frac{c}{\sqrt{1 - (\omega_c/\omega)^2}} > c. $$

The phase velocity exceeds $c$ (no signal travels this fast — no information is carried at $v_p$).

相速度超过 $c$（无信号以此速度传播——$v_p$ 不携带信息）。

**Step 6 — Group velocity.** The group velocity is $v_g = d\omega/dk_z$. Differentiate $k_z^2 c^2 = \omega^2 - \omega_c^2$ (with $\omega_c$ fixed for a given mode): $2c^2 k_z\,dk_z = 2\omega\,d\omega$, so

**第 6 步 — 群速度。** 群速度 $v_g = d\omega/dk_z$。对 $k_z^2 c^2 = \omega^2 - \omega_c^2$（给定模式 $\omega_c$ 固定）求微分：$2c^2 k_z\,dk_z = 2\omega\,d\omega$，故

$$ v_g = \frac{d\omega}{dk_z} = \frac{c^2 k_z}{\omega} = c^2 \cdot \frac{\sqrt{\omega^2 - \omega_c^2}/c}{\omega} = \frac{c\sqrt{\omega^2 - \omega_c^2}}{\omega} = c\sqrt{1 - (\omega_c/\omega)^2} < c. $$

The group velocity — the speed of energy and information — is below $c$, as required by relativity.

群速度——能量与信息的传播速度——低于 $c$，符合相对论要求。

**Step 7 — Product of velocities.** Multiply the two results:

**第 7 步 — 速度之积。** 将两结果相乘：

$$ v_p v_g = \frac{c}{\sqrt{1 - (\omega_c/\omega)^2}} \cdot c\sqrt{1 - (\omega_c/\omega)^2} = \boxed{\, c^2 \,}. $$

This identity holds for any single mode and reflects the hyperbolic dispersion $\omega^2 = \omega_c^2 + c^2 k_z^2$. $\blacksquare$

此恒等式对任意单一模式成立，反映双曲色散 $\omega^2 = \omega_c^2 + c^2 k_z^2$。$\blacksquare$

---

## C. Cavity Resonator: Resonant Frequencies and Quality Factor · 谐振腔：谐振频率与品质因数

**Claim.** Closing a rectangular guide with conducting walls at $z = 0$ and $z = d$ quantizes $k_z = p\pi/d$, giving discrete resonant frequencies $\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$. The quality factor $Q = \omega\cdot(\text{energy stored})/(\text{power lost})$ scales as $Q \approx (V/S)\cdot(1/\delta_{\text{skin}})$.

**命题。** 用 $z = 0$ 与 $z = d$ 处的导电壁封闭矩形波导，使 $k_z = p\pi/d$ 量子化，得离散谐振频率 $\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$。品质因数 $Q = \omega\cdot(\text{储存能量})/(\text{损耗功率})$ 正比于 $Q \approx (V/S)\cdot(1/\delta_{\text{skin}})$。

**Step 1 — Standing wave from two counter-propagating modes.** A wave $e^{ik_z z}$ reflecting off a conductor at $z = d$ combines with its reflection $e^{-ik_z z}$ to form a standing wave. The tangential electric field must vanish on both end walls $z = 0$ and $z = d$. The $z$-dependence of the transverse $\mathbf{E}$-field is therefore proportional to $\sin(k_z z)$, which vanishes at $z = 0$ automatically and at $z = d$ provided

**第 1 步 — 两反向传播模构成驻波。** 波 $e^{ik_z z}$ 在 $z = d$ 处的导体反射，与其反射 $e^{-ik_z z}$ 合成驻波。切向电场须在两端壁 $z = 0$ 与 $z = d$ 处为零。故横向 $\mathbf{E}$ 场的 $z$ 依赖正比于 $\sin(k_z z)$，它在 $z = 0$ 自动为零，在 $z = d$ 处为零的条件为

$$ \sin(k_z d) = 0 \implies \boxed{\, k_z = p\pi/d \,}, \quad p = 0, 1, 2, \dots $$

The axial wavenumber is quantized just like a vibrating string fixed at both ends.

轴向波数被量子化，正如两端固定的振动弦。

**Step 2 — Resonant frequencies.** The guide already quantized the transverse wavenumbers as $k_x = m\pi/a$, $k_y = n\pi/b$ (Section B). The full dispersion $\omega^2/c^2 = k_x^2 + k_y^2 + k_z^2$ now becomes

**第 2 步 — 谐振频率。** 波导已将横向波数量子化为 $k_x = m\pi/a$，$k_y = n\pi/b$（B 节）。完整色散 $\omega^2/c^2 = k_x^2 + k_y^2 + k_z^2$ 现变为

$$ \omega^2_{mnp}/c^2 = (m\pi/a)^2 + (n\pi/b)^2 + (p\pi/d)^2. $$

Taking the square root gives the discrete cavity resonances:

取平方根得离散腔谐振：

$$ \boxed{\, \omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2} \,}. $$

Only certain frequencies fit standing waves into the box; the cavity is a 3-D analogue of a box of standing sound modes.

只有特定频率能将驻波装入腔体；谐振腔是三维驻波声模箱的类比。

**Step 3 — Definition of the quality factor.** A real cavity loses energy to ohmic heating in the walls. With stored energy $U$ and time-averaged dissipated power $P_{\text{loss}}$, the energy decays as $dU/dt = -P_{\text{loss}}$. Defining

**第 3 步 — 品质因数定义。** 真实腔体通过壁面欧姆加热损耗能量。设储存能量 $U$、时间平均耗散功率 $P_{\text{loss}}$，能量衰减为 $dU/dt = -P_{\text{loss}}$。定义

$$ \boxed{\, Q \equiv \omega\,U/P_{\text{loss}} \,}, $$

we get $dU/dt = -(\omega/Q)U$, so $U(t) = U_0 e^{-\omega t/Q}$: the field rings for $\sim Q/2\pi$ oscillation periods. A high $Q$ means a sharp, long-lived resonance of fractional width $\Delta\omega/\omega \approx 1/Q$.

得 $dU/dt = -(\omega/Q)U$，故 $U(t) = U_0 e^{-\omega t/Q}$：场振荡约 $Q/2\pi$ 个周期。高 $Q$ 意味着尖锐、长寿命的谐振，相对宽度 $\Delta\omega/\omega \approx 1/Q$。

**Step 4 — $Q$ scaling from skin depth.** The stored energy is distributed throughout the cavity volume: $U \sim u\cdot V$, where $u$ is the energy density and $V$ the volume. Ohmic loss occurs only within a skin layer of depth $\delta_{\text{skin}}$ at the conducting walls (Module 1.11), where surface currents flow. The dissipated power therefore scales with the wall area $S$ and the skin depth:

**第 4 步 — 由趋肤深度给出 $Q$ 标度。** 储存能量分布于整个腔体体积：$U \sim u\cdot V$，$u$ 为能量密度，$V$ 为体积。欧姆损耗只发生在导电壁趋肤深度 $\delta_{\text{skin}}$ 的薄层内（模块 1.11），那里有表面电流流动。故耗散功率正比于壁面积 $S$ 与趋肤深度：

$$ P_{\text{loss}} \sim \frac{R_s}{2}\int|\mathbf{H}_\parallel|^2\,dS \propto S\cdot u\cdot(\omega\delta_{\text{skin}}), $$

with surface resistance $R_s = 1/(\sigma\delta_{\text{skin}}) \propto \omega\delta_{\text{skin}}$. Forming the ratio (keeping only the geometric and skin-depth scaling):

其中表面电阻 $R_s = 1/(\sigma\delta_{\text{skin}}) \propto \omega\delta_{\text{skin}}$。作比值（仅保留几何与趋肤深度标度）：

$$ Q = \omega U/P_{\text{loss}} \propto \frac{\omega\cdot(u V)}{S\cdot u\cdot\omega\delta_{\text{skin}}} = \boxed{\, \frac{V}{S}\cdot\frac{1}{\delta_{\text{skin}}} \,}. $$

A larger volume-to-surface ratio stores proportionally more energy per unit lossy area, and a thinner skin layer (higher conductivity, lower frequency) dissipates less — hence the famous result that $Q$ is of order (linear cavity size)/(skin depth). For a copper cavity at GHz frequencies $\delta_{\text{skin}} \sim 1\ \mu\mathrm{m}$ and a cm-scale size give $Q \sim 10^4$. $\blacksquare$

更大的体积–表面比意味着每单位损耗面积储存更多能量，更薄的趋肤层（更高电导率、更低频率）耗散更少——故有著名结果：$Q$ 量级为 (腔线尺寸)/(趋肤深度)。对 GHz 频率下的铜腔，$\delta_{\text{skin}} \sim 1\ \mu\mathrm{m}$、cm 量级尺寸给出 $Q \sim 10^4$。$\blacksquare$

---

## D. Telegrapher's Equations, Wave Speed, Impedance, and Reflection · 电报方程、波速、阻抗与反射

**Claim.** A transmission line with per-unit-length inductance $L$ and capacitance $C$ obeys the telegrapher's equations $\partial V/\partial x = -L\,\partial I/\partial t$ and $\partial I/\partial x = -C\,\partial V/\partial t$, which combine into $\partial^2 V/\partial x^2 = LC\,\partial^2 V/\partial t^2$ with wave speed $v = 1/\sqrt{LC}$ and characteristic impedance $Z_0 = \sqrt{L/C}$. At a load $Z_L$ the reflection coefficient is $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$.

**命题。** 单位长度电感 $L$、电容 $C$ 的传输线服从电报方程 $\partial V/\partial x = -L\,\partial I/\partial t$ 与 $\partial I/\partial x = -C\,\partial V/\partial t$，二者合并为 $\partial^2 V/\partial x^2 = LC\,\partial^2 V/\partial t^2$，波速 $v = 1/\sqrt{LC}$，特征阻抗 $Z_0 = \sqrt{L/C}$。负载 $Z_L$ 处反射系数为 $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$。

**Step 1 — Voltage drop across a line element (Faraday/inductance).** Consider a segment of length $\Delta x$ with series inductance $L\Delta x$. The voltage drop across it equals the back-emf of the time-varying current through that inductance (Module 9.1):

**第 1 步 — 线元上的电压降（法拉第/电感）。** 考虑长 $\Delta x$ 的线段，串联电感 $L\Delta x$。其上的电压降等于流过该电感的时变电流的反电动势（模块 9.1）：

$$ V(x + \Delta x) - V(x) = -(L\Delta x)\,\partial I/\partial t. $$

Dividing by $\Delta x$ and letting $\Delta x \to 0$:

除以 $\Delta x$ 并令 $\Delta x \to 0$：

$$ \boxed{\, \partial V/\partial x = -L\,\partial I/\partial t \,} \qquad \text{(telegrapher's equation 1)} $$

**Step 2 — Current loss into shunt capacitance (charge conservation).** The two conductors of the segment form a shunt capacitance $C\Delta x$. Charge conservation says the current that does not continue forward charges this capacitor:

**第 2 步 — 流入并联电容的电流（电荷守恒）。** 线段的两导体构成并联电容 $C\Delta x$。电荷守恒指出未继续前行的电流为此电容充电：

$$ I(x + \Delta x) - I(x) = -(C\Delta x)\,\partial V/\partial t. $$

Dividing by $\Delta x$ and letting $\Delta x \to 0$:

除以 $\Delta x$ 并令 $\Delta x \to 0$：

$$ \boxed{\, \partial I/\partial x = -C\,\partial V/\partial t \,} \qquad \text{(telegrapher's equation 2)} $$

**Step 3 — Combine into a wave equation.** Differentiate equation 1 with respect to $x$ and equation 2 with respect to $t$:

**第 3 步 — 合并为波动方程。** 将方程 1 对 $x$ 求导、方程 2 对 $t$ 求导：

$$ \partial^2 V/\partial x^2 = -L\,\partial^2 I/\partial x\partial t, \qquad \partial^2 I/\partial t\partial x = -C\,\partial^2 V/\partial t^2. $$

Since the mixed partials of $I$ are equal, substitute the second into the first:

由于 $I$ 的混合偏导相等，将第二式代入第一式：

$$ \partial^2 V/\partial x^2 = -L(-C\,\partial^2 V/\partial t^2) = LC\,\partial^2 V/\partial t^2 \implies \boxed{\, \partial^2 V/\partial x^2 = LC\,\partial^2 V/\partial t^2 \,}. $$

This is the 1-D wave equation $\partial^2 V/\partial x^2 = (1/v^2)\partial^2 V/\partial t^2$ with

这是一维波动方程 $\partial^2 V/\partial x^2 = (1/v^2)\partial^2 V/\partial t^2$，其中

$$ \boxed{\, v = 1/\sqrt{LC} \,}. $$

The same equation holds for $I$.

$I$ 满足同一方程。

**Step 4 — Characteristic impedance.** Consider a single forward-traveling wave $V(x, t) = V_0 f(x - vt)$, $I(x, t) = I_0 f(x - vt)$. Insert into telegrapher's equation 1: $\partial V/\partial x = V_0 f'$ and $\partial I/\partial t = -v I_0 f'$, so $V_0 f' = -L(-v I_0 f') = Lv I_0 f'$, giving $V_0 = Lv I_0$. Hence the ratio of voltage to current of a forward wave is

**第 4 步 — 特征阻抗。** 考虑单一前行波 $V(x, t) = V_0 f(x - vt)$，$I(x, t) = I_0 f(x - vt)$。代入电报方程 1：$\partial V/\partial x = V_0 f'$，$\partial I/\partial t = -v I_0 f'$，故 $V_0 f' = -L(-v I_0 f') = Lv I_0 f'$，得 $V_0 = Lv I_0$。故前行波的电压与电流之比为

$$ Z_0 \equiv V_0/I_0 = Lv = L/\sqrt{LC} = \boxed{\, \sqrt{L/C} \,}. $$

A backward-traveling wave $g(x + vt)$ carries $V/I = -Z_0$ (the current reverses for the same voltage polarity).

后行波 $g(x + vt)$ 带有 $V/I = -Z_0$（同电压极性下电流反向）。

**Step 5 — Reflection at a load.** Write the total field on the line ($x < 0$, load at $x = 0$) as a superposition of an incident forward wave and a reflected backward wave:

**第 5 步 — 负载处的反射。** 将线上总场（$x < 0$，负载在 $x = 0$）写为入射前行波与反射后行波的叠加：

$$ V(x, t) = V_i e^{i(kx - \omega t)} + V_r e^{i(-kx - \omega t)}, \qquad I(x, t) = \frac{V_i}{Z_0} e^{i(kx - \omega t)} - \frac{V_r}{Z_0} e^{i(-kx - \omega t)}, $$

using $V/I = +Z_0$ for the forward part and $-Z_0$ for the reflected part. The reflection coefficient is defined as $\Gamma \equiv V_r/V_i$.

前行部分用 $V/I = +Z_0$，反射部分用 $-Z_0$。反射系数定义为 $\Gamma \equiv V_r/V_i$。

**Step 6 — Apply the load boundary condition.** At the load $x = 0$ the line voltage and current must satisfy Ohm's law for the load, $V(0, t) = Z_L I(0, t)$. Evaluating both fields at $x = 0$:

**第 6 步 — 应用负载边界条件。** 在负载 $x = 0$ 处，线电压与电流须满足负载的欧姆定律 $V(0, t) = Z_L I(0, t)$。在 $x = 0$ 处计算两场：

$$ V_i + V_r = Z_L \cdot (V_i - V_r)/Z_0. $$

Multiply through by $Z_0$ and group:

两边乘 $Z_0$ 并整理：

$$ Z_0(V_i + V_r) = Z_L(V_i - V_r) \implies V_r(Z_0 + Z_L) = V_i(Z_L - Z_0). $$

Therefore

故

$$ \boxed{\, \Gamma = V_r/V_i = (Z_L - Z_0)/(Z_L + Z_0) \,}. $$

**Step 7 — Special cases and matching.** Read off the limits:

**第 7 步 — 特殊情形与匹配。** 读出极限：

- **Matched, $Z_L = Z_0$:** $\Gamma = 0$ — no reflection; all incident power is absorbed by the load.
- **Short circuit, $Z_L = 0$:** $\Gamma = (0 - Z_0)/(0 + Z_0) = -1$ — full reflection with inverted voltage.
- **Open circuit, $Z_L \to \infty$:** $\Gamma \to (Z_L)/(Z_L) = +1$ — full reflection with same-sign voltage.

- **匹配，$Z_L = Z_0$：** $\Gamma = 0$——无反射；全部入射功率被负载吸收。
- **短路，$Z_L = 0$：** $\Gamma = (0 - Z_0)/(0 + Z_0) = -1$——电压反相的全反射。
- **开路，$Z_L \to \infty$：** $\Gamma \to +1$——同号电压的全反射。

The power delivered to the load is $P_L = P_{\text{inc}}(1 - |\Gamma|^2)$, maximized ($|\Gamma| = 0$) exactly when $Z_L = Z_0$. This is the **impedance-matching** condition for maximum power transfer and zero standing waves — the design rule behind 50-$\Omega$ coaxial systems. $\blacksquare$

向负载传递的功率为 $P_L = P_{\text{inc}}(1 - |\Gamma|^2)$，当且仅当 $Z_L = Z_0$（$|\Gamma| = 0$）时最大。这就是最大功率传输与零驻波的**阻抗匹配**条件——50 $\Omega$ 同轴系统背后的设计准则。$\blacksquare$

---

*From a single transverse Helmholtz equation flow all three structures: hollow guides (one boundary, no TEM, cutoff dispersion), closed cavities (three quantized wavenumbers, discrete resonances and Q), and two-conductor lines (TEM at all frequencies, telegrapher's equations, impedance matching). The same boundary-value machinery of Module 1.8 and the wave physics of Modules 1.10–1.11 and 1.16 underlie every microwave and high-speed circuit.*

*从单一横向亥姆霍兹方程导出全部三种结构：空心波导（单一边界、无 TEM、截止色散）、封闭谐振腔（三个量子化波数、离散谐振与 Q）以及双导体线（任意频率的 TEM、电报方程、阻抗匹配）。模块 1.8 的同一边值方法以及模块 1.10–1.11 与 1.16 的波动物理支撑着每个微波与高速电路。*

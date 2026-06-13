# Module 1.23 — Waveguides, Cavity Resonators & Transmission Lines
**模块 1.23 — 波导、谐振腔与传输线**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.23-waveguides-cavities-transmission-lines-derivations.md)

---

## 1. Waveguides & Cutoff · 波导与截止

**Definition.** A **waveguide** is a hollow (or filled) conductor that confines and guides electromagnetic waves. Seeking solutions $\propto e^{i(k_z z - \omega t)}$ inside the guide reduces Maxwell's equations (Module 1.10) to a 2-D transverse Helmholtz problem $(\nabla_t^2 + \gamma^2)\psi = 0$ with $\gamma^2 = \omega^2/c^2 - k_z^2$. Modes are classified as **TE** ($E_z = 0$), **TM** ($B_z = 0$), or **TEM** ($E_z = B_z = 0$). Each mode has a **cutoff frequency** $\omega_c$: only waves with $\omega > \omega_c$ propagate, since $k_z = \sqrt{\omega^2 - \omega_c^2}/c$ becomes imaginary (evanescent) below cutoff.

**定义。** **波导**是约束并引导电磁波的空心（或填充）导体。在波导内寻求 $\propto e^{i(k_z z - \omega t)}$ 的解，可将麦克斯韦方程组（模块 1.10）化为二维横向亥姆霍兹问题 $(\nabla_t^2 + \gamma^2)\psi = 0$，其中 $\gamma^2 = \omega^2/c^2 - k_z^2$。模式分为 **TE**（$E_z = 0$）、**TM**（$B_z = 0$）或 **TEM**（$E_z = B_z = 0$）。每个模式有一个**截止频率 $\omega_c$**：只有 $\omega > \omega_c$ 的波才能传播，因为在截止频率以下 $k_z = \sqrt{\omega^2 - \omega_c^2}/c$ 变为虚数（消逝波）。

**Demonstration.** A single hollow pipe supports no TEM mode: a TEM field would require a transverse static potential satisfying Laplace's equation with a constant boundary value, forcing $\psi = \text{const}$ and zero field. A **TEM mode therefore needs two conductors** (coaxial cable, parallel wires). For a hollow rectangular guide of sides $a, b$, the lowest propagating mode is $\text{TE}_{10}$ with cutoff $\omega_c = c\pi/a$ — set entirely by the larger transverse dimension.

**演示。** 单一空心管不支持 TEM 模式：TEM 场要求横向静电势满足拉普拉斯方程且边界值为常数，迫使 $\psi = \text{常数}$、场为零。**因此 TEM 模式需要两个导体**（同轴电缆、平行导线）。对于边长为 $a, b$ 的空心矩形波导，最低传播模式为 $\text{TE}_{10}$，截止频率 $\omega_c = c\pi/a$——完全由较大的横向尺寸决定。

**Application.** Waveguides carry high-power microwaves with low loss in radar, satellite links, and particle accelerators, where coaxial cables would break down or dissipate. The cutoff acts as a built-in high-pass filter, and the dispersion of guided waves (Module 1.16) sets the bandwidth of every microwave channel.

**应用。** 波导在雷达、卫星链路和粒子加速器中以低损耗传输大功率微波，在这些场合同轴电缆会击穿或耗散。截止频率充当内建的高通滤波器，导波的色散（模块 1.16）决定每个微波信道的带宽。

## 2. Cavity Resonators & Q · 谐振腔与品质因数

**Definition.** Closing a waveguide with conducting end walls a distance $d$ apart produces a **cavity resonator**: the guided wave reflects back and forth, and only standing waves with $k_z = p\pi/d$ survive. The result is a discrete set of **resonant frequencies**; for a rectangular box of sides $a, b, d$, $\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$. The **quality factor** $Q = \omega\cdot(\text{energy stored})/(\text{power dissipated})$ measures how sharply the cavity resonates.

**定义。** 用相距 $d$ 的导电端壁封闭波导，产生**谐振腔**：导波来回反射，只有满足 $k_z = p\pi/d$ 的驻波存留。结果是一组离散的**谐振频率**；对边长为 $a, b, d$ 的矩形腔，$\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$。**品质因数** $Q = \omega\cdot(\text{储存能量})/(\text{耗散功率})$ 衡量谐振的尖锐程度。

**Demonstration.** Because ohmic losses occur only in a thin surface layer of skin depth $\delta_\text{skin}$ (Module 1.11), the dissipated power scales with surface area while the stored energy scales with volume. Hence $Q \approx (V/S)\cdot(1/\delta_\text{skin})$: larger cavities and smaller skin depth give sharper resonances. A copper microwave cavity routinely reaches $Q \sim 10^4$, and superconducting cavities reach $Q \sim 10^{10}$.

**演示。** 由于欧姆损耗只发生在厚度为趋肤深度 $\delta_\text{skin}$ 的薄表面层（模块 1.11），耗散功率正比于表面积，而储存能量正比于体积。故 $Q \approx (V/S)\cdot(1/\delta_\text{skin})$：更大的腔体和更小的趋肤深度给出更尖锐的谐振。铜微波腔通常达到 $Q \sim 10^4$，超导腔达到 $Q \sim 10^{10}$。

**Application.** Cavity resonators define frequency standards (atomic clocks), drive klystrons and magnetrons, and accelerate beams in linacs and synchrotrons. The same physics fixes the modes of a laser cavity and the resonant frequencies of every musical wind instrument — boundaries quantize a wave field.

**应用。** 谐振腔定义频率标准（原子钟），驱动速调管和磁控管，并在直线加速器和同步加速器中加速束流。同样的物理原理决定激光腔的模式以及每件管乐器的谐振频率——边界使波场量子化。

## 3. Transmission Lines & the Telegrapher's Equations · 传输线与电报方程

**Definition.** A **transmission line** (coaxial cable, twin lead, microstrip) is modeled by a distributed inductance $L$ and capacitance $C$ per unit length. Charge conservation and Faraday's law on an infinitesimal segment give the **telegrapher's equations** $\partial V/\partial x = -L\, \partial I/\partial t$ and $\partial I/\partial x = -C\, \partial V/\partial t$, which combine into a wave equation with signal speed $v = 1/\sqrt{LC}$ and **characteristic impedance** $Z_0 = \sqrt{L/C}$ (the ratio $V/I$ of a forward-traveling wave).

**定义。** **传输线**（同轴电缆、双线、微带）用单位长度的分布电感 $L$ 和电容 $C$ 建模。在无穷小段上应用电荷守恒和法拉第定律给出**电报方程** $\partial V/\partial x = -L\, \partial I/\partial t$ 和 $\partial I/\partial x = -C\, \partial V/\partial t$，二者结合为波动方程，信号速度 $v = 1/\sqrt{LC}$，**特征阻抗 $Z_0 = \sqrt{L/C}$**（前行波的 $V/I$ 之比）。

**Demonstration.** A wave reaching a load $Z_L$ is partly reflected with **reflection coefficient** $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$. A matched load $Z_L = Z_0$ gives $\Gamma = 0$ (no reflection); a short circuit $Z_L = 0$ gives $\Gamma = -1$; an open circuit $Z_L \to \infty$ gives $\Gamma = +1$. Maximum power is delivered to the load precisely when it is matched, $Z_L = Z_0$.

**演示。** 到达负载 $Z_L$ 的波被部分反射，**反射系数 $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$**。匹配负载 $Z_L = Z_0$ 给出 $\Gamma = 0$（无反射）；短路 $Z_L = 0$ 给出 $\Gamma = -1$；开路 $Z_L \to \infty$ 给出 $\Gamma = +1$。当且仅当匹配 $Z_L = Z_0$ 时，向负载传递的功率最大。

**Application.** Impedance matching is the central design rule of every RF and high-speed digital system (Module 9.1): a 50 $\Omega$ cable feeding a 50 $\Omega$ antenna reflects nothing, while a mismatch produces standing waves, signal echoes, and lost power. The telegrapher's equations are the engineering face of the same wave physics that governs waveguides and optics.

**应用。** 阻抗匹配是每个射频与高速数字系统（模块 9.1）的核心设计准则：50 $\Omega$ 电缆馈送 50 $\Omega$ 天线时无反射，而失配产生驻波、信号回波和功率损失。电报方程是支配波导与光学的同一波动物理的工程表现形式。

## Key results · 核心结果

- Transverse fields obey $(\nabla_t^2+\gamma^2)\psi=0$; a single hollow conductor has no TEM mode · 横向场方程,单导体无 TEM
- $\text{TE}_{mn}$ cutoff $\omega_c$; $v_p v_g=c^2$ · 截止频率,$v_p v_g=c^2$
- Cavity resonances; $Q\propto(V/S)/\delta_\text{skin}$ · 腔模与品质因数
- Telegrapher's equations; reflection $\Gamma=\dfrac{Z_L-Z_0}{Z_L+Z_0}$ · 电报方程与反射系数

---

**Self-test (blank page)**

1. Starting from Maxwell's equations for fields $\propto e^{i(k_z z - \omega t)}$, show that the transverse fields satisfy $(\nabla_t^2 + \gamma^2)\psi = 0$, and explain why a single hollow conductor has no TEM mode.
2. Derive the cutoff frequency $\omega_c$ of the $\text{TE}_{mn}$ mode of a rectangular guide, and show that $v_p v_g = c^2$.
3. Write down the resonant frequencies of a rectangular cavity and explain physically why $Q$ scales as $(\text{volume}/\text{surface})\cdot(1/\delta_\text{skin})$.
4. Derive the telegrapher's equations and the reflection coefficient $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$; state the values of $\Gamma$ for a matched, shorted, and open line.

**自测（空白页）**

1. 从 $\propto e^{i(k_z z - \omega t)}$ 场的麦克斯韦方程组出发，证明横向场满足 $(\nabla_t^2 + \gamma^2)\psi = 0$，并解释为何单一空心导体没有 TEM 模式。
2. 推导矩形波导 $\text{TE}_{mn}$ 模式的截止频率 $\omega_c$，并证明 $v_p v_g = c^2$。
3. 写出矩形腔的谐振频率，并从物理上解释为何 $Q$ 正比于 $(\text{体积}/\text{表面积})\cdot(1/\delta_\text{skin})$。
4. 推导电报方程和反射系数 $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$；给出匹配、短路和开路情形下 $\Gamma$ 的值。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** For fields $\propto e^{i(k_z z-\omega t)}$, Maxwell's equations reduce the transverse parts to $(\nabla_t^2+\gamma^2)\psi=0$ with $\gamma^2=\omega^2/c^2-k_z^2$. A single hollow conductor supports no TEM mode (a TEM field needs two conductors; the one-boundary transverse Laplace problem has only the trivial solution). · 横向场方程;单导体无 TEM。
**2.** $\gamma^2=(m\pi/a)^2+(n\pi/b)^2$, cutoff $\omega_c=c\sqrt{(m\pi/a)^2+(n\pi/b)^2}$; with $v_p=\omega/k_z>c$ and $v_g=d\omega/dk_z<c$, $v_p v_g=c^2$. · 截止频率与 $v_pv_g=c^2$。
**3.** $\omega_{lmn}=c\pi\sqrt{(l/a)^2+(m/b)^2+(n/d)^2}$; $Q\propto$ stored/loss $\propto(V/S)/\delta_\text{skin}$ because losses live in surface currents within a skin depth. · 腔频率与 $Q\propto(V/S)/\delta$。
**4.** Telegrapher's: $\partial_z V=-L\partial_t I$, $\partial_z I=-C\partial_t V$, with $Z_0=\sqrt{L/C}$. $\Gamma=(Z_L-Z_0)/(Z_L+Z_0)$: matched $\Gamma=0$, shorted $\Gamma=-1$, open $\Gamma=+1$. · 电报方程;反射系数三种情形。

</details>

---

← Previous: [Module 1.22 — Retarded Potentials & Radiation Reaction](./module-1.22-retarded-potentials-radiation-reaction.md) · [Phase 1 index](./README.md) · Next: [Phase 2 — Thermodynamics & Statistical Mechanics](../phase-2-thermodynamics-statistical-mechanics/README.md) →

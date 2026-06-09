# Module 1.23 — Waveguides, Cavity Resonators & Transmission Lines
**模块 1.23 — 波导、谐振腔与传输线**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.23-waveguides-cavities-transmission-lines-derivations.md)

---

## 1. Waveguides & Cutoff · 波导与截止

**Definition.** A **waveguide** is a hollow (or filled) conductor that confines and guides electromagnetic waves. Seeking solutions ∝ e^{i(k_z z − ωt)} inside the guide reduces Maxwell's equations (Module 1.10) to a 2-D transverse Helmholtz problem (∇_t² + γ²)ψ = 0 with γ² = ω²/c² − k_z². Modes are classified as **TE** (E_z = 0), **TM** (B_z = 0), or **TEM** (E_z = B_z = 0). Each mode has a **cutoff frequency ω_c**: only waves with ω > ω_c propagate, since k_z = √(ω² − ω_c²)/c becomes imaginary (evanescent) below cutoff.

**定义。** **波导**是约束并引导电磁波的空心（或填充）导体。在波导内寻求 ∝ e^{i(k_z z − ωt)} 的解，可将麦克斯韦方程组（模块 1.10）化为二维横向亥姆霍兹问题 (∇_t² + γ²)ψ = 0，其中 γ² = ω²/c² − k_z²。模式分为 **TE**（E_z = 0）、**TM**（B_z = 0）或 **TEM**（E_z = B_z = 0）。每个模式有一个**截止频率 ω_c**：只有 ω > ω_c 的波才能传播，因为在截止频率以下 k_z = √(ω² − ω_c²)/c 变为虚数（消逝波）。

**Demonstration.** A single hollow pipe supports no TEM mode: a TEM field would require a transverse static potential satisfying Laplace's equation with a constant boundary value, forcing ψ = const and zero field. A **TEM mode therefore needs two conductors** (coaxial cable, parallel wires). For a hollow rectangular guide of sides a, b, the lowest propagating mode is TE₁₀ with cutoff ω_c = cπ/a — set entirely by the larger transverse dimension.

**演示。** 单一空心管不支持 TEM 模式：TEM 场要求横向静电势满足拉普拉斯方程且边界值为常数，迫使 ψ = 常数、场为零。**因此 TEM 模式需要两个导体**（同轴电缆、平行导线）。对于边长为 a、b 的空心矩形波导，最低传播模式为 TE₁₀，截止频率 ω_c = cπ/a——完全由较大的横向尺寸决定。

**Application.** Waveguides carry high-power microwaves with low loss in radar, satellite links, and particle accelerators, where coaxial cables would break down or dissipate. The cutoff acts as a built-in high-pass filter, and the dispersion of guided waves (Module 1.16) sets the bandwidth of every microwave channel.

**应用。** 波导在雷达、卫星链路和粒子加速器中以低损耗传输大功率微波，在这些场合同轴电缆会击穿或耗散。截止频率充当内建的高通滤波器，导波的色散（模块 1.16）决定每个微波信道的带宽。

## 2. Cavity Resonators & Q · 谐振腔与品质因数

**Definition.** Closing a waveguide with conducting end walls a distance d apart produces a **cavity resonator**: the guided wave reflects back and forth, and only standing waves with k_z = pπ/d survive. The result is a discrete set of **resonant frequencies**; for a rectangular box of sides a, b, d, ω_{mnp} = cπ√((m/a)² + (n/b)² + (p/d)²). The **quality factor** Q = ω·(energy stored)/(power dissipated) measures how sharply the cavity resonates.

**定义。** 用相距 d 的导电端壁封闭波导，产生**谐振腔**：导波来回反射，只有满足 k_z = pπ/d 的驻波存留。结果是一组离散的**谐振频率**；对边长为 a、b、d 的矩形腔，ω_{mnp} = cπ√((m/a)² + (n/b)² + (p/d)²)。**品质因数** Q = ω·(储存能量)/(耗散功率) 衡量谐振的尖锐程度。

**Demonstration.** Because ohmic losses occur only in a thin surface layer of skin depth δ_skin (Module 1.11), the dissipated power scales with surface area while the stored energy scales with volume. Hence Q ≈ (V/S)·(1/δ_skin): larger cavities and smaller skin depth give sharper resonances. A copper microwave cavity routinely reaches Q ~ 10⁴, and superconducting cavities reach Q ~ 10¹⁰.

**演示。** 由于欧姆损耗只发生在厚度为趋肤深度 δ_skin 的薄表面层（模块 1.11），耗散功率正比于表面积，而储存能量正比于体积。故 Q ≈ (V/S)·(1/δ_skin)：更大的腔体和更小的趋肤深度给出更尖锐的谐振。铜微波腔通常达到 Q ~ 10⁴，超导腔达到 Q ~ 10¹⁰。

**Application.** Cavity resonators define frequency standards (atomic clocks), drive klystrons and magnetrons, and accelerate beams in linacs and synchrotrons. The same physics fixes the modes of a laser cavity and the resonant frequencies of every musical wind instrument — boundaries quantize a wave field.

**应用。** 谐振腔定义频率标准（原子钟），驱动速调管和磁控管，并在直线加速器和同步加速器中加速束流。同样的物理原理决定激光腔的模式以及每件管乐器的谐振频率——边界使波场量子化。

## 3. Transmission Lines & the Telegrapher's Equations · 传输线与电报方程

**Definition.** A **transmission line** (coaxial cable, twin lead, microstrip) is modeled by a distributed inductance L and capacitance C per unit length. Charge conservation and Faraday's law on an infinitesimal segment give the **telegrapher's equations** ∂V/∂x = −L ∂I/∂t and ∂I/∂x = −C ∂V/∂t, which combine into a wave equation with signal speed v = 1/√(LC) and **characteristic impedance Z₀ = √(L/C)** (the ratio V/I of a forward-traveling wave).

**定义。** **传输线**（同轴电缆、双线、微带）用单位长度的分布电感 L 和电容 C 建模。在无穷小段上应用电荷守恒和法拉第定律给出**电报方程** ∂V/∂x = −L ∂I/∂t 和 ∂I/∂x = −C ∂V/∂t，二者结合为波动方程，信号速度 v = 1/√(LC)，**特征阻抗 Z₀ = √(L/C)**（前行波的 V/I 之比）。

**Demonstration.** A wave reaching a load Z_L is partly reflected with **reflection coefficient Γ = (Z_L − Z₀)/(Z_L + Z₀)**. A matched load Z_L = Z₀ gives Γ = 0 (no reflection); a short circuit Z_L = 0 gives Γ = −1; an open circuit Z_L → ∞ gives Γ = +1. Maximum power is delivered to the load precisely when it is matched, Z_L = Z₀.

**演示。** 到达负载 Z_L 的波被部分反射，**反射系数 Γ = (Z_L − Z₀)/(Z_L + Z₀)**。匹配负载 Z_L = Z₀ 给出 Γ = 0（无反射）；短路 Z_L = 0 给出 Γ = −1；开路 Z_L → ∞ 给出 Γ = +1。当且仅当匹配 Z_L = Z₀ 时，向负载传递的功率最大。

**Application.** Impedance matching is the central design rule of every RF and high-speed digital system (Module 9.1): a 50 Ω cable feeding a 50 Ω antenna reflects nothing, while a mismatch produces standing waves, signal echoes, and lost power. The telegrapher's equations are the engineering face of the same wave physics that governs waveguides and optics.

**应用。** 阻抗匹配是每个射频与高速数字系统（模块 9.1）的核心设计准则：50 Ω 电缆馈送 50 Ω 天线时无反射，而失配产生驻波、信号回波和功率损失。电报方程是支配波导与光学的同一波动物理的工程表现形式。

---

**Self-test (blank page)**

1. Starting from Maxwell's equations for fields ∝ e^{i(k_z z − ωt)}, show that the transverse fields satisfy (∇_t² + γ²)ψ = 0, and explain why a single hollow conductor has no TEM mode.
2. Derive the cutoff frequency ω_c of the TE_mn mode of a rectangular guide, and show that v_p v_g = c².
3. Write down the resonant frequencies of a rectangular cavity and explain physically why Q scales as (volume/surface)·(1/δ_skin).
4. Derive the telegrapher's equations and the reflection coefficient Γ = (Z_L − Z₀)/(Z_L + Z₀); state the values of Γ for a matched, shorted, and open line.

**自测（空白页）**

1. 从 ∝ e^{i(k_z z − ωt)} 场的麦克斯韦方程组出发，证明横向场满足 (∇_t² + γ²)ψ = 0，并解释为何单一空心导体没有 TEM 模式。
2. 推导矩形波导 TE_mn 模式的截止频率 ω_c，并证明 v_p v_g = c²。
3. 写出矩形腔的谐振频率，并从物理上解释为何 Q 正比于 (体积/表面积)·(1/δ_skin)。
4. 推导电报方程和反射系数 Γ = (Z_L − Z₀)/(Z_L + Z₀)；给出匹配、短路和开路情形下 Γ 的值。

---

← Previous: [Module 1.22 — Retarded Potentials & Radiation Reaction](./module-1.22-retarded-potentials-radiation-reaction.md) · [Phase 1 index](./README.md) · Next: [Phase 2 — Thermodynamics & Statistical Mechanics](../phase-2-thermodynamics-statistical-mechanics/README.md) →

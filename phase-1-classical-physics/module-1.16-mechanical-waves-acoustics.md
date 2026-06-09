---
title: "Module 1.16 — Mechanical Waves & Acoustics"
parent: "Phase 1 — Classical Physics"
nav_order: 16
---

# Module 1.16 — Mechanical Waves & Acoustics
**模块 1.16 — 机械波与声学**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.16-mechanical-waves-acoustics-derivations.md)

---

## 1. The Wave Equation · 波动方程

**Definition.** A **mechanical wave** is a disturbance that propagates through a medium, transporting energy and momentum without net transport of matter. Small disturbances obey the **wave equation** $\partial^2 u/\partial t^2 = c^2 \partial^2 u/\partial x^2$ (or $\partial^2 u/\partial t^2 = c^2 \nabla^2 u$ in 3D), a PDE solved by separation of variables (Module 0.3). Its general 1D solution is **d'Alembert's form** $u(x,t) = f(x - ct) + g(x + ct)$: arbitrary right- and left-moving profiles at speed $c$.

**定义。** **机械波**是在介质中传播、输运能量和动量而不净输运物质的扰动。小扰动满足**波动方程** $\partial^2 u/\partial t^2 = c^2 \partial^2 u/\partial x^2$（三维为 $\partial^2 u/\partial t^2 = c^2 \nabla^2 u$），这是一个用分离变量法（模块 0.3）求解的偏微分方程。其一维通解是**达朗贝尔形式** $u(x,t) = f(x - ct) + g(x + ct)$：以速度 $c$ 向右和向左传播的任意波形。

**Demonstration.** A string of tension $T$ and linear density $\mu$ supports transverse waves with $c = \sqrt{T/\mu}$. A continuous chain of masses and springs (the continuum limit of the coupled oscillators of Module 1.6) reproduces exactly this equation — the wave is the collective normal mode of infinitely many oscillators. Harmonic solutions $u = A \cos(kx - \omega t)$ give the **dispersion relation** $\omega = ck$, with wavelength $\lambda = 2\pi/k$ and frequency $f = \omega/2\pi$.

**演示。** 张力为 $T$、线密度为 $\mu$ 的弦支持横波，$c = \sqrt{T/\mu}$。质量和弹簧的连续链（模块 1.6 耦合振子的连续极限）精确重现这一方程——波是无穷多振子的集体简正模式。谐波解 $u = A \cos(kx - \omega t)$ 给出**色散关系** $\omega = ck$，波长 $\lambda = 2\pi/k$，频率 $f = \omega/2\pi$。

**Application.** Any superposition of normal modes is itself a solution; decomposing a disturbance into its harmonic components is **Fourier analysis** (Module 0.5). Standing waves on a bounded string quantize into harmonics $f_n = n c/2L$ — the same boundary-value logic that quantizes energy in the infinite square well (Module 3.2).

**应用。** 简正模式的任意叠加本身就是解；将扰动分解为谐波分量是**傅里叶分析**（模块 0.5）。有界弦上的驻波量子化为谐波 $f_n = n c/2L$——这与无限方势阱（模块 3.2）中量子化能量的边值逻辑相同。

## 2. Sound, Energy & Wave Phenomena · 声音、能量与波动现象

**Definition.** **Sound** is a longitudinal pressure wave in a fluid, with speed $c = \sqrt{B/\rho}$ ($B$ = bulk modulus, $\rho$ = density). Waves carry energy flux (intensity $\propto$ amplitude$^2$) and exhibit **reflection, refraction, interference, and diffraction**; a moving source or observer produces the **Doppler shift** $f' = f\,(c \pm v_\text{obs})/(c \mp v_\text{src})$.

**定义。** **声音**是流体中的纵向压力波，速度为 $c = \sqrt{B/\rho}$（$B$ = 体积模量，$\rho$ = 密度）。波携带能量通量（强度 $\propto$ 振幅$^2$），并表现出**反射、折射、干涉和衍射**；运动的声源或观察者产生**多普勒频移** $f' = f\,(c \pm v_\text{obs})/(c \mp v_\text{src})$。

**Demonstration.** Two waves of nearby frequency superpose into **beats** at frequency $|f_1 - f_2|$; a wave meeting a boundary partially reflects with a phase flip at a fixed end. Group velocity $v_g = d\omega/dk$ governs how a wave *packet* (and its energy) actually travels when the medium is dispersive.

**演示。** 频率相近的两列波叠加产生频率为 $|f_1 - f_2|$ 的**拍**；波遇到边界时部分反射，在固定端有相位翻转。群速度 $v_g = d\omega/dk$ 决定波*包*（及其能量）在色散介质中实际传播的方式。

**Application.** Acoustics underlies musical instruments, ultrasound imaging, sonar, and seismology. The wave equation and its dispersion/group-velocity machinery carry over directly to electromagnetic waves (Module 1.11), lattice waves and phonons (Module 4.3), and the matter waves of quantum mechanics (Module 3.1).

**应用。** 声学是乐器、超声波成像、声纳和地震学的基础。波动方程及其色散/群速度机制直接延伸到电磁波（模块 1.11）、晶格波和声子（模块 4.3）以及量子力学的物质波（模块 3.1）。

---

**Self-test (blank page)**

1. Derive $c = \sqrt{T/\mu}$ for a string from Newton's second law applied to a small element.
2. Write d'Alembert's solution and use it to describe a pulse reflecting off a fixed end.
3. A 1 m string fixed at both ends has c = 200 m/s. Find its three lowest standing-wave frequencies.
4. Explain the difference between phase velocity and group velocity, and when they differ.

**自测（空白页）**

1. 对弦的小微元应用牛顿第二定律，推导 $c = \sqrt{T/\mu}$。
2. 写出达朗贝尔解，并用它描述一个脉冲在固定端的反射。
3. 一根两端固定、长 1 m 的弦，c = 200 m/s。求其最低的三个驻波频率。
4. 解释相速度和群速度的区别，以及它们何时不同。

---

← Previous: [Module 1.15 — Covariant Electromagnetism](./module-1.15-covariant-electromagnetism.md) · [Phase 1 index](./README.md) · Next: [Module 1.17 — Fluid Mechanics](./module-1.17-fluid-mechanics.md) →

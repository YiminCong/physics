# Module 6.12 — Finite-Temperature Field Theory (the Matsubara Formalism)
**模块 6.12 — 有限温度场论（松原形式）**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.12-finite-temperature-field-theory-derivations.md)

---

## 1. The Partition Function as a Euclidean Path Integral · 配分函数作为欧几里得路径积分

**Definition.** Statistical mechanics at temperature $T$ is governed by the thermal partition function $Z = \operatorname{Tr} e^{-\beta H}$, with $\beta = 1/T$ (units $\hbar = k_B = 1$). Every equilibrium observable follows from it: free energy $F = -T \ln Z$, energy $\langle H\rangle = -\partial \ln Z/\partial\beta$, entropy $S = -\partial F/\partial T$. The operator $e^{-\beta H}$ is formally the time-evolution operator $e^{-iHt}$ continued to imaginary time $t = -i\tau$ with $\tau$ running from $0$ to $\beta$. The trace then identifies the initial and final field configurations, so the quantum partition function of a field theory becomes a path integral over fields defined on a *Euclidean time circle* of circumference $\beta$:

$$ Z = \oint \mathcal{D}\varphi\, e^{-S_E[\varphi]}, \qquad S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E, $$

where $\mathcal{L}_E$ is the Euclidean Lagrangian density ($\mathcal{L}_E = \tfrac12(\partial_\tau\varphi)^2 + \tfrac12(\nabla\varphi)^2 + V(\varphi)$ for a scalar). The circle $\oint$ means the field obeys a periodicity condition in $\tau$.

**定义。** 温度 $T$ 下的统计力学由热配分函数 $Z = \operatorname{Tr} e^{-\beta H}$ 支配，$\beta = 1/T$（取 $\hbar = k_B = 1$）。一切平衡可观测量都由它给出：自由能 $F = -T \ln Z$、能量 $\langle H\rangle = -\partial \ln Z/\partial\beta$、熵 $S = -\partial F/\partial T$。算符 $e^{-\beta H}$ 在形式上是时间演化算符 $e^{-iHt}$ 解析延拓到虚时间 $t = -i\tau$（$\tau$ 从 $0$ 跑到 $\beta$）的结果。求迹将初末场位形等同起来，于是场论的量子配分函数变成定义在周长为 $\beta$ 的*欧几里得时间圆周*上的场的路径积分：

$$ Z = \oint \mathcal{D}\varphi\, e^{-S_E[\varphi]}, \qquad S_E = \int_0^\beta d\tau \int d^3x\, \mathcal{L}_E, $$

其中 $\mathcal{L}_E$ 是欧几里得拉格朗日密度（标量情形 $\mathcal{L}_E = \tfrac12(\partial_\tau\varphi)^2 + \tfrac12(\nabla\varphi)^2 + V(\varphi)$）。圆周 $\oint$ 表示场在 $\tau$ 方向满足周期性条件。

**Demonstration.** The boundary conditions in $\tau$ are not a choice — they are forced by the trace. For a *boson* the trace $\int d\varphi\, \langle\varphi| e^{-\beta H} |\varphi\rangle$ identifies the configuration at $\tau = \beta$ with that at $\tau = 0$, giving **periodic** boundary conditions $\varphi(\tau + \beta) = \varphi(\tau)$. For a *fermion* the trace must be taken with Grassmann coherent states; the cyclic property of the trace combined with the anticommuting nature of the Grassmann variables flips a sign, forcing **antiperiodic** boundary conditions $\psi(\tau + \beta) = -\psi(\tau)$. These two boundary conditions are the single physical input that distinguishes Bose from Fermi statistics in the path integral, and everything thermal follows from them.

**演示。** $\tau$ 方向的边界条件不是人为选择——它们由求迹强制给出。对*玻色子*，迹 $\int d\varphi\, \langle\varphi| e^{-\beta H} |\varphi\rangle$ 将 $\tau = \beta$ 处的位形与 $\tau = 0$ 处等同，给出**周期性**边界条件 $\varphi(\tau + \beta) = \varphi(\tau)$。对*费米子*，必须用格拉斯曼相干态求迹；迹的循环性与格拉斯曼变量的反对易性结合翻转一个符号，强制给出**反周期性**边界条件 $\psi(\tau + \beta) = -\psi(\tau)$。这两个边界条件是路径积分中区分玻色与费米统计的唯一物理输入，所有热学结果都由它们而来。

**Application.** This single formula unifies quantum statistical mechanics with field theory. The same Feynman-diagram and path-integral machinery developed for vacuum QFT (Module 6.4) now computes thermodynamic quantities, with the only change being the compactified Euclidean time. It is the foundation of finite-temperature QCD (the quark–gluon plasma), the electroweak phase transition in the early universe (Module 8.6), and the Matsubara Green's-function methods of condensed-matter many-body theory (Module 6.2). Kapusta & Gale "Finite-Temperature Field Theory" and Le Bellac "Thermal Field Theory" are standard references.

**应用。** 这一个公式将量子统计力学与场论统一起来。为真空 QFT 发展的同一套费曼图与路径积分机器（模块 6.4）现在用来计算热力学量，唯一的改变是欧几里得时间的紧致化。它是有限温度 QCD（夸克–胶子等离子体）、早期宇宙电弱相变（模块 8.6）以及凝聚态多体理论的松原格林函数方法（模块 6.2）的基础。Kapusta & Gale 的 "Finite-Temperature Field Theory" 与 Le Bellac 的 "Thermal Field Theory" 是标准参考书。

---

## 2. Matsubara Frequencies and Frequency Sums · 松原频率与频率求和

**Definition.** Because Euclidean time lives on a circle of circumference $\beta$, the Fourier transform in $\tau$ is a *Fourier series*, not an integral, and the frequencies are discrete. Writing $\varphi(\tau) = T \sum_n e^{-i\omega_n \tau} \varphi(\omega_n)$, the (anti)periodic boundary conditions quantize $\omega_n$ into the **Matsubara frequencies**:

$$ \text{bosons: } \omega_n = 2\pi n T, \qquad \text{fermions: } \omega_n = (2n+1)\pi T, \qquad n \in \mathbb{Z}. $$

The free Euclidean propagator becomes $G(\omega_n, k) = 1/(\omega_n^2 + E_k^2)$ for a scalar (with $E_k^2 = k^2 + m^2$), and analogous forms for fermions and gauge fields. Loop integrals $\int d^4k/(2\pi)^4$ are replaced by $T \sum_n \int d^3k/(2\pi)^3$: the energy integral becomes a sum over Matsubara modes.

**定义。** 由于欧几里得时间居于周长为 $\beta$ 的圆周上，$\tau$ 方向的傅里叶变换是*傅里叶级数*而非积分，频率是离散的。写 $\varphi(\tau) = T \sum_n e^{-i\omega_n \tau} \varphi(\omega_n)$，（反）周期性边界条件将 $\omega_n$ 量子化为**松原频率**：

$$ \text{玻色子：} \omega_n = 2\pi n T, \qquad \text{费米子：} \omega_n = (2n+1)\pi T, \qquad n \in \mathbb{Z}. $$

自由欧几里得传播子对标量变为 $G(\omega_n, k) = 1/(\omega_n^2 + E_k^2)$（$E_k^2 = k^2 + m^2$），费米子与规范场有类似形式。圈积分 $\int d^4k/(2\pi)^4$ 被替换为 $T \sum_n \int d^3k/(2\pi)^3$：能量积分变成对松原模式的求和。

**Demonstration.** The central technical step in any finite-$T$ calculation is performing the discrete sum over $n$. The basic bosonic sum is

$$ T \sum_n \frac{1}{\omega_n^2 + E^2} = \frac{1}{2E} \coth\!\frac{\beta E}{2} = \frac{1}{2E}[1 + 2 n_B(E)], \qquad n_B(E) = \frac{1}{e^{\beta E} - 1}. $$

The trick: convert the sum into a contour integral of a weighting function whose poles sit exactly at the Matsubara frequencies. For bosons $\coth(\beta\omega/2)$ has simple poles at $\omega = i\omega_n = 2\pi i n T$ with residue $2T$; for fermions $\tanh(\beta\omega/2)$ has poles at the fermionic frequencies. Deforming the contour to wrap the poles of $1/(\omega^2 + E^2)$ at $\omega = \pm E$ and reading off the residues produces $\coth(\beta E/2)$ (bosons) or $\tanh(\beta E/2)$ (fermions). The hyperbolic functions, re-expressed via $\coth(x) = 1 + 2/(e^{2x}-1)$ and $\tanh(x) = 1 - 2/(e^{2x}+1)$, deliver exactly the **Bose–Einstein** $n_B$ and **Fermi–Dirac** $n_F$ occupation numbers. The thermal distributions are not assumed — they emerge automatically from the Matsubara sum.

**演示。** 任何有限温度计算的核心技术步骤是完成对 $n$ 的离散求和。基本的玻色求和为

$$ T \sum_n \frac{1}{\omega_n^2 + E^2} = \frac{1}{2E} \coth\!\frac{\beta E}{2} = \frac{1}{2E}[1 + 2 n_B(E)], \qquad n_B(E) = \frac{1}{e^{\beta E} - 1}. $$

技巧：把求和转化为一个加权函数的围道积分，其极点恰好位于松原频率处。对玻色子，$\coth(\beta\omega/2)$ 在 $\omega = i\omega_n = 2\pi i n T$ 处有单极点，留数为 $2T$；对费米子，$\tanh(\beta\omega/2)$ 在费米频率处有极点。将围道变形以环绕 $1/(\omega^2 + E^2)$ 在 $\omega = \pm E$ 处的极点并读取留数，得到 $\coth(\beta E/2)$（玻色）或 $\tanh(\beta E/2)$（费米）。再用 $\coth(x) = 1 + 2/(e^{2x}-1)$ 与 $\tanh(x) = 1 - 2/(e^{2x}+1)$ 改写双曲函数，恰好给出**玻色–爱因斯坦** $n_B$ 与**费米–狄拉克** $n_F$ 占据数。热分布不是被假设的——它们从松原求和中自动涌现。

**Application.** Matsubara sums are the workhorse of every thermal-field-theory computation: thermal masses, the pressure of the quark–gluon plasma, Debye screening, and the finite-temperature effective potential that drives cosmological phase transitions. The very same $n_B$ and $n_F$ that appear here are the equilibrium distributions of Modules 2.5 and 2.6 — finite-$T$ QFT *derives* the statistical-mechanics input rather than postulating it. The technique is identical to the Matsubara Green's-function method introduced for many-body systems in Module 6.2.

**应用。** 松原求和是每一项热场论计算的主力：热质量、夸克–胶子等离子体的压强、德拜屏蔽，以及驱动宇宙学相变的有限温度有效势。这里出现的 $n_B$ 与 $n_F$ 正是模块 2.5 与 2.6 的平衡分布——有限温度 QFT *推导出*统计力学的输入而非假设它。该技术与模块 6.2 为多体系统引入的松原格林函数方法完全相同。

---

## 3. The Ideal Bose Gas and Stefan–Boltzmann · 理想玻色气体与斯特藩–玻尔兹曼

**Definition.** As a fully worked example, consider a free relativistic scalar field with dispersion $E_k = \sqrt{k^2 + m^2}$. Its free energy is $F = -T \ln Z$. Carrying out the Gaussian path integral, $\ln Z = -\tfrac12 \sum_n \int d^3k/(2\pi)^3\, \ln(\omega_n^2 + E_k^2) \cdot V$ (up to a constant), so the entire thermodynamics reduces to the Matsubara sum $\sum_n \ln(\omega_n^2 + E_k^2)$. Performing it (by integrating the frequency-sum identity of Section 2 with respect to $E$) gives the free-energy density

$$ \frac{F}{V} = \int \frac{d^3k}{(2\pi)^3}\, \Big[\, \tfrac12 E_k + T \ln(1 - e^{-\beta E_k})\, \Big]. $$

The first term is the temperature-independent zero-point (vacuum) energy; the second is the Bose–Einstein thermal contribution.

**定义。** 作为完整的范例，考虑色散关系为 $E_k = \sqrt{k^2 + m^2}$ 的自由相对论标量场。其自由能为 $F = -T \ln Z$。完成高斯路径积分，$\ln Z = -\tfrac12 \sum_n \int d^3k/(2\pi)^3\, \ln(\omega_n^2 + E_k^2) \cdot V$（差一个常数），故全部热力学归结为松原求和 $\sum_n \ln(\omega_n^2 + E_k^2)$。完成该求和（对第 2 节的频率求和恒等式关于 $E$ 积分）给出自由能密度

$$ \frac{F}{V} = \int \frac{d^3k}{(2\pi)^3}\, \Big[\, \tfrac12 E_k + T \ln(1 - e^{-\beta E_k})\, \Big]. $$

第一项是与温度无关的零点（真空）能量；第二项是玻色–爱因斯坦热贡献。

**Demonstration.** Drop the vacuum piece (it is renormalized away) and take the massless limit $E_k = |k| = k$, relevant for photons and other massless bosons. Then

$$ \frac{F}{V} = T \int \frac{d^3k}{(2\pi)^3}\, \ln(1 - e^{-\beta k}) = \frac{T}{2\pi^2} \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}). $$

Substituting $x = \beta k$ and integrating by parts reduces the integral to a Riemann zeta value, $\int_0^\infty dx\, x^3/(e^x - 1) = \pi^4/15$, yielding

$$ \frac{F}{V} = -\frac{\pi^2}{90} g T^4, \qquad P = -\frac{F}{V} = \frac{\pi^2}{90} g T^4, $$

where $g$ counts the internal (polarization/spin) degrees of freedom ($g = 2$ for the photon). This is the **Stefan–Boltzmann law**: the radiation pressure and energy density ($\rho = 3P = (\pi^2/30)g T^4$) scale as $T^4$, recovered here directly from the Matsubara formalism.

**演示。** 丢弃真空项（它被重整化吸收）并取无质量极限 $E_k = |k| = k$，适用于光子及其他无质量玻色子。则

$$ \frac{F}{V} = T \int \frac{d^3k}{(2\pi)^3}\, \ln(1 - e^{-\beta k}) = \frac{T}{2\pi^2} \int_0^\infty dk\, k^2 \ln(1 - e^{-\beta k}). $$

代入 $x = \beta k$ 并分部积分，将积分化为黎曼 $\zeta$ 值 $\int_0^\infty dx\, x^3/(e^x - 1) = \pi^4/15$，得到

$$ \frac{F}{V} = -\frac{\pi^2}{90} g T^4, \qquad P = -\frac{F}{V} = \frac{\pi^2}{90} g T^4, $$

其中 $g$ 计入内部（偏振/自旋）自由度（光子 $g = 2$）。这就是**斯特藩–玻尔兹曼定律**：辐射压强与能量密度（$\rho = 3P = (\pi^2/30)g T^4$）按 $T^4$ 标度，这里直接由松原形式重新得到。

**Application.** The KMS (Kubo–Martin–Schwinger) condition states that the (anti)periodicity of thermal Green's functions in imaginary time is *equivalent to* the system being in thermal equilibrium at temperature T — it is the rigorous definition of equilibrium in this formalism. The imaginary-time (Matsubara) formalism underlies finite-T QFT, the equation of state of the quark–gluon plasma probed in heavy-ion collisions, and high-temperature symmetry restoration driving the electroweak phase transition in the early universe (Module 8.6); the same $T^4$ scaling governs early-universe thermodynamics. In condensed matter it is the Matsubara Green's-function machinery of Module 6.2, and it determines the temperature dependence of the BCS gap (Module 5.5). For genuinely out-of-equilibrium problems the imaginary-time formalism is replaced by the real-time **Keldysh (closed-time-path)** formalism.

**应用。** KMS（久保–马丁–施温格）条件表明：热格林函数在虚时间中的（反）周期性*等价于*系统处于温度 T 的热平衡——它是此形式中平衡的严格定义。虚时间（松原）形式是有限温度 QFT、重离子碰撞中探测的夸克–胶子等离子体物态方程，以及驱动早期宇宙电弱相变的高温对称性恢复（模块 8.6）的基础；同样的 $T^4$ 标度支配早期宇宙热力学。在凝聚态中它就是模块 6.2 的松原格林函数机器，并决定 BCS 能隙的温度依赖（模块 5.5）。对真正的非平衡问题，虚时间形式被实时的 **Keldysh（闭合时间路径）**形式取代。

## Key results · 核心结果

- $Z=\text{Tr}\,e^{-\beta H}$ → Euclidean path integral on a $\tau$-circle of length $\beta$ · 欧氏时间圆
- Bosons periodic, fermions antiperiodic in $\tau$ · 玻色周期、费米反周期
- Matsubara frequencies: $\omega_n=2\pi nT$ (boson), $(2n+1)\pi T$ (fermion) · 松原频率
- Massless gas $F/V=-(\pi^2/90)gT^4$ (Stefan–Boltzmann) · 无质量气体自由能

---

## Self-test (blank page) · 自测（空白页）

1. Starting from $Z = \operatorname{Tr} e^{-\beta H}$, explain why the field-theory partition function becomes a path integral over a Euclidean time circle of circumference $\beta$. Why are bosonic fields periodic and fermionic fields antiperiodic in $\tau$?
2. Derive the bosonic and fermionic Matsubara frequencies from the (anti)periodic boundary conditions. Why are the frequencies discrete rather than continuous?
3. State the result of the bosonic Matsubara sum $T \sum_n 1/(\omega_n^2 + E^2)$. How do the Bose–Einstein and Fermi–Dirac occupation numbers emerge from $\coth$ and $\tanh$?
4. For a massless boson gas, derive $F/V = -(\pi^2/90) g T^4$ from the free energy. What is the KMS condition, and what is the real-time alternative to the Matsubara formalism?

**自测（空白页）**

1. 从 $Z = \operatorname{Tr} e^{-\beta H}$ 出发，解释为何场论配分函数变成在周长为 $\beta$ 的欧几里得时间圆周上的路径积分。为何玻色场在 $\tau$ 中周期、费米场反周期？
2. 从（反）周期性边界条件推导玻色与费米松原频率。为何频率是离散而非连续的？
3. 写出玻色松原求和 $T \sum_n 1/(\omega_n^2 + E^2)$ 的结果。玻色–爱因斯坦与费米–狄拉克占据数如何从 $\coth$ 与 $\tanh$ 中涌现？
4. 对无质量玻色气体，从自由能推导 $F/V = -(\pi^2/90) g T^4$。KMS 条件是什么？松原形式的实时替代方案是什么？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $Z=\text{Tr}\,e^{-\beta H}$ is a path integral with $\tau\in[0,\beta]$ whose trace identifies the endpoints → a circle of circumference $\beta$. The trace makes bosons periodic, while anticommuting (Grassmann) fermions are antiperiodic, $\psi(\beta)=-\psi(0)$. · 迹使玻色周期、费米反周期。
**2.** (Anti)periodicity quantizes the frequencies: bosons $\omega_n=2\pi nT$, fermions $\omega_n=(2n+1)\pi T$. Discrete because the $\tau$-direction is a finite compact circle (Fourier series). · 边界条件给离散松原频率。
**3.** $T\sum_n\frac1{\omega_n^2+E^2}=\frac1{2E}\coth\frac{E}{2T}=\frac1{2E}(1+2n_B(E))$; the $\coth$/$\tanh$ generate the Bose–Einstein / Fermi–Dirac occupations. · 松原求和给出 BE/FD 占据数。
**4.** Massless boson gas $F/V=-(\pi^2/90)gT^4$ ($g$ = degrees of freedom), the Stefan–Boltzmann result. KMS: thermal correlators are (anti)periodic in imaginary time. Real-time alternative: the Schwinger–Keldysh (closed-time-path) formalism. · 自由能;KMS 条件与施温格–凯尔迪什形式。

</details>

---

← Previous: [Module 6.11 — Effective Field Theory & the Renormalization Group](./module-6.11-effective-field-theory-and-the-renormalization-group.md) · Next: [Module 6.13 — Conformal Field Theory](./module-6.13-conformal-field-theory.md) · [Phase 6 index](./README.md)

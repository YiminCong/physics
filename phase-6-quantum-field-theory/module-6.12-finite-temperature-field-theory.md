# Module 6.12 — Finite-Temperature Field Theory (the Matsubara Formalism)
**模块 6.12 — 有限温度场论（松原形式）**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.12-finite-temperature-field-theory-derivations.md)

---

## 1. The Partition Function as a Euclidean Path Integral · 配分函数作为欧几里得路径积分

**Definition.** Statistical mechanics at temperature T is governed by the thermal partition function Z = Tr e^{−βH}, with β = 1/T (units ℏ = k_B = 1). Every equilibrium observable follows from it: free energy F = −T ln Z, energy ⟨H⟩ = −∂ ln Z/∂β, entropy S = −∂F/∂T. The operator e^{−βH} is formally the time-evolution operator e^{−iHt} continued to imaginary time t = −iτ with τ running from 0 to β. The trace then identifies the initial and final field configurations, so the quantum partition function of a field theory becomes a path integral over fields defined on a *Euclidean time circle* of circumference β:

  **Z = ∮ Dφ e^{−S_E[φ]},  S_E = ∫₀^β dτ ∫ d³x ℒ_E,**

where ℒ_E is the Euclidean Lagrangian density (ℒ_E = ½(∂_τφ)² + ½(∇φ)² + V(φ) for a scalar). The circle ∮ means the field obeys a periodicity condition in τ.

**定义。** 温度 T 下的统计力学由热配分函数 Z = Tr e^{−βH} 支配，β = 1/T（取 ℏ = k_B = 1）。一切平衡可观测量都由它给出：自由能 F = −T ln Z、能量 ⟨H⟩ = −∂ ln Z/∂β、熵 S = −∂F/∂T。算符 e^{−βH} 在形式上是时间演化算符 e^{−iHt} 解析延拓到虚时间 t = −iτ（τ 从 0 跑到 β）的结果。求迹将初末场位形等同起来，于是场论的量子配分函数变成定义在周长为 β 的*欧几里得时间圆周*上的场的路径积分：

  **Z = ∮ Dφ e^{−S_E[φ]},  S_E = ∫₀^β dτ ∫ d³x ℒ_E,**

其中 ℒ_E 是欧几里得拉格朗日密度（标量情形 ℒ_E = ½(∂_τφ)² + ½(∇φ)² + V(φ)）。圆周 ∮ 表示场在 τ 方向满足周期性条件。

**Demonstration.** The boundary conditions in τ are not a choice — they are forced by the trace. For a *boson* the trace ∫ dφ ⟨φ| e^{−βH} |φ⟩ identifies the configuration at τ = β with that at τ = 0, giving **periodic** boundary conditions φ(τ + β) = φ(τ). For a *fermion* the trace must be taken with Grassmann coherent states; the cyclic property of the trace combined with the anticommuting nature of the Grassmann variables flips a sign, forcing **antiperiodic** boundary conditions ψ(τ + β) = −ψ(τ). These two boundary conditions are the single physical input that distinguishes Bose from Fermi statistics in the path integral, and everything thermal follows from them.

**演示。** τ 方向的边界条件不是人为选择——它们由求迹强制给出。对*玻色子*，迹 ∫ dφ ⟨φ| e^{−βH} |φ⟩ 将 τ = β 处的位形与 τ = 0 处等同，给出**周期性**边界条件 φ(τ + β) = φ(τ)。对*费米子*，必须用格拉斯曼相干态求迹；迹的循环性与格拉斯曼变量的反对易性结合翻转一个符号，强制给出**反周期性**边界条件 ψ(τ + β) = −ψ(τ)。这两个边界条件是路径积分中区分玻色与费米统计的唯一物理输入，所有热学结果都由它们而来。

**Application.** This single formula unifies quantum statistical mechanics with field theory. The same Feynman-diagram and path-integral machinery developed for vacuum QFT (Module 6.4) now computes thermodynamic quantities, with the only change being the compactified Euclidean time. It is the foundation of finite-temperature QCD (the quark–gluon plasma), the electroweak phase transition in the early universe (Module 8.6), and the Matsubara Green's-function methods of condensed-matter many-body theory (Module 6.2). Kapusta & Gale "Finite-Temperature Field Theory" and Le Bellac "Thermal Field Theory" are standard references.

**应用。** 这一个公式将量子统计力学与场论统一起来。为真空 QFT 发展的同一套费曼图与路径积分机器（模块 6.4）现在用来计算热力学量，唯一的改变是欧几里得时间的紧致化。它是有限温度 QCD（夸克–胶子等离子体）、早期宇宙电弱相变（模块 8.6）以及凝聚态多体理论的松原格林函数方法（模块 6.2）的基础。Kapusta & Gale 的 "Finite-Temperature Field Theory" 与 Le Bellac 的 "Thermal Field Theory" 是标准参考书。

---

## 2. Matsubara Frequencies and Frequency Sums · 松原频率与频率求和

**Definition.** Because Euclidean time lives on a circle of circumference β, the Fourier transform in τ is a *Fourier series*, not an integral, and the frequencies are discrete. Writing φ(τ) = T Σ_n e^{−iω_n τ} φ(ω_n), the (anti)periodic boundary conditions quantize ω_n into the **Matsubara frequencies**:

  **bosons: ω_n = 2πnT,  fermions: ω_n = (2n+1)πT,  n ∈ ℤ.**

The free Euclidean propagator becomes G(ω_n, k) = 1/(ω_n² + E_k²) for a scalar (with E_k² = k² + m²), and analogous forms for fermions and gauge fields. Loop integrals ∫ d⁴k/(2π)⁴ are replaced by T Σ_n ∫ d³k/(2π)³: the energy integral becomes a sum over Matsubara modes.

**定义。** 由于欧几里得时间居于周长为 β 的圆周上，τ 方向的傅里叶变换是*傅里叶级数*而非积分，频率是离散的。写 φ(τ) = T Σ_n e^{−iω_n τ} φ(ω_n)，（反）周期性边界条件将 ω_n 量子化为**松原频率**：

  **玻色子：ω_n = 2πnT，  费米子：ω_n = (2n+1)πT，  n ∈ ℤ。**

自由欧几里得传播子对标量变为 G(ω_n, k) = 1/(ω_n² + E_k²)（E_k² = k² + m²），费米子与规范场有类似形式。圈积分 ∫ d⁴k/(2π)⁴ 被替换为 T Σ_n ∫ d³k/(2π)³：能量积分变成对松原模式的求和。

**Demonstration.** The central technical step in any finite-T calculation is performing the discrete sum over n. The basic bosonic sum is

  **T Σ_n 1/(ω_n² + E²) = (1/2E) coth(βE/2) = (1/2E)[1 + 2 n_B(E)],  n_B(E) = 1/(e^{βE} − 1).**

The trick: convert the sum into a contour integral of a weighting function whose poles sit exactly at the Matsubara frequencies. For bosons coth(βω/2) has simple poles at ω = iω_n = 2πinT with residue 2T; for fermions tanh(βω/2) has poles at the fermionic frequencies. Deforming the contour to wrap the poles of 1/(ω² + E²) at ω = ±E and reading off the residues produces coth(βE/2) (bosons) or tanh(βE/2) (fermions). The hyperbolic functions, re-expressed via coth(x) = 1 + 2/(e^{2x}−1) and tanh(x) = 1 − 2/(e^{2x}+1), deliver exactly the **Bose–Einstein** n_B and **Fermi–Dirac** n_F occupation numbers. The thermal distributions are not assumed — they emerge automatically from the Matsubara sum.

**演示。** 任何有限温度计算的核心技术步骤是完成对 n 的离散求和。基本的玻色求和为

  **T Σ_n 1/(ω_n² + E²) = (1/2E) coth(βE/2) = (1/2E)[1 + 2 n_B(E)],  n_B(E) = 1/(e^{βE} − 1)。**

技巧：把求和转化为一个加权函数的围道积分，其极点恰好位于松原频率处。对玻色子，coth(βω/2) 在 ω = iω_n = 2πinT 处有单极点，留数为 2T；对费米子，tanh(βω/2) 在费米频率处有极点。将围道变形以环绕 1/(ω² + E²) 在 ω = ±E 处的极点并读取留数，得到 coth(βE/2)（玻色）或 tanh(βE/2)（费米）。再用 coth(x) = 1 + 2/(e^{2x}−1) 与 tanh(x) = 1 − 2/(e^{2x}+1) 改写双曲函数，恰好给出**玻色–爱因斯坦** n_B 与**费米–狄拉克** n_F 占据数。热分布不是被假设的——它们从松原求和中自动涌现。

**Application.** Matsubara sums are the workhorse of every thermal-field-theory computation: thermal masses, the pressure of the quark–gluon plasma, Debye screening, and the finite-temperature effective potential that drives cosmological phase transitions. The very same n_B and n_F that appear here are the equilibrium distributions of Modules 2.5 and 2.6 — finite-T QFT *derives* the statistical-mechanics input rather than postulating it. The technique is identical to the Matsubara Green's-function method introduced for many-body systems in Module 6.2.

**应用。** 松原求和是每一项热场论计算的主力：热质量、夸克–胶子等离子体的压强、德拜屏蔽，以及驱动宇宙学相变的有限温度有效势。这里出现的 n_B 与 n_F 正是模块 2.5 与 2.6 的平衡分布——有限温度 QFT *推导出*统计力学的输入而非假设它。该技术与模块 6.2 为多体系统引入的松原格林函数方法完全相同。

---

## 3. The Ideal Bose Gas and Stefan–Boltzmann · 理想玻色气体与斯特藩–玻尔兹曼

**Definition.** As a fully worked example, consider a free relativistic scalar field with dispersion E_k = √(k² + m²). Its free energy is F = −T ln Z. Carrying out the Gaussian path integral, ln Z = −½ Σ_n ∫ d³k/(2π)³ ln(ω_n² + E_k²) · V (up to a constant), so the entire thermodynamics reduces to the Matsubara sum Σ_n ln(ω_n² + E_k²). Performing it (by integrating the frequency-sum identity of Section 2 with respect to E) gives the free-energy density

  **F/V = ∫ d³k/(2π)³ [ ½ E_k + T ln(1 − e^{−βE_k}) ].**

The first term is the temperature-independent zero-point (vacuum) energy; the second is the Bose–Einstein thermal contribution.

**定义。** 作为完整的范例，考虑色散关系为 E_k = √(k² + m²) 的自由相对论标量场。其自由能为 F = −T ln Z。完成高斯路径积分，ln Z = −½ Σ_n ∫ d³k/(2π)³ ln(ω_n² + E_k²) · V（差一个常数），故全部热力学归结为松原求和 Σ_n ln(ω_n² + E_k²)。完成该求和（对第 2 节的频率求和恒等式关于 E 积分）给出自由能密度

  **F/V = ∫ d³k/(2π)³ [ ½ E_k + T ln(1 − e^{−βE_k}) ]。**

第一项是与温度无关的零点（真空）能量；第二项是玻色–爱因斯坦热贡献。

**Demonstration.** Drop the vacuum piece (it is renormalized away) and take the massless limit E_k = |k| = k, relevant for photons and other massless bosons. Then

  F/V = T ∫ d³k/(2π)³ ln(1 − e^{−βk}) = (T/2π²) ∫₀^∞ dk k² ln(1 − e^{−βk}).

Substituting x = βk and integrating by parts reduces the integral to a Riemann zeta value, ∫₀^∞ dx x³/(e^x − 1) = π⁴/15, yielding

  **F/V = −(π²/90) g T⁴,  P = −F/V = (π²/90) g T⁴,**

where g counts the internal (polarization/spin) degrees of freedom (g = 2 for the photon). This is the **Stefan–Boltzmann law**: the radiation pressure and energy density (ρ = 3P = (π²/30)g T⁴) scale as T⁴, recovered here directly from the Matsubara formalism.

**演示。** 丢弃真空项（它被重整化吸收）并取无质量极限 E_k = |k| = k，适用于光子及其他无质量玻色子。则

  F/V = T ∫ d³k/(2π)³ ln(1 − e^{−βk}) = (T/2π²) ∫₀^∞ dk k² ln(1 − e^{−βk})。

代入 x = βk 并分部积分，将积分化为黎曼 ζ 值 ∫₀^∞ dx x³/(e^x − 1) = π⁴/15，得到

  **F/V = −(π²/90) g T⁴,  P = −F/V = (π²/90) g T⁴,**

其中 g 计入内部（偏振/自旋）自由度（光子 g = 2）。这就是**斯特藩–玻尔兹曼定律**：辐射压强与能量密度（ρ = 3P = (π²/30)g T⁴）按 T⁴ 标度，这里直接由松原形式重新得到。

**Application.** The KMS (Kubo–Martin–Schwinger) condition states that the (anti)periodicity of thermal Green's functions in imaginary time is *equivalent to* the system being in thermal equilibrium at temperature T — it is the rigorous definition of equilibrium in this formalism. The imaginary-time (Matsubara) formalism underlies finite-T QFT, the equation of state of the quark–gluon plasma probed in heavy-ion collisions, and high-temperature symmetry restoration driving the electroweak phase transition in the early universe (Module 8.6); the same T⁴ scaling governs early-universe thermodynamics. In condensed matter it is the Matsubara Green's-function machinery of Module 6.2, and it determines the temperature dependence of the BCS gap (Module 5.5). For genuinely out-of-equilibrium problems the imaginary-time formalism is replaced by the real-time **Keldysh (closed-time-path)** formalism.

**应用。** KMS（久保–马丁–施温格）条件表明：热格林函数在虚时间中的（反）周期性*等价于*系统处于温度 T 的热平衡——它是此形式中平衡的严格定义。虚时间（松原）形式是有限温度 QFT、重离子碰撞中探测的夸克–胶子等离子体物态方程，以及驱动早期宇宙电弱相变的高温对称性恢复（模块 8.6）的基础；同样的 T⁴ 标度支配早期宇宙热力学。在凝聚态中它就是模块 6.2 的松原格林函数机器，并决定 BCS 能隙的温度依赖（模块 5.5）。对真正的非平衡问题，虚时间形式被实时的 **Keldysh（闭合时间路径）**形式取代。

---

## Self-test (blank page) · 自测（空白页）

1. Starting from Z = Tr e^{−βH}, explain why the field-theory partition function becomes a path integral over a Euclidean time circle of circumference β. Why are bosonic fields periodic and fermionic fields antiperiodic in τ?
2. Derive the bosonic and fermionic Matsubara frequencies from the (anti)periodic boundary conditions. Why are the frequencies discrete rather than continuous?
3. State the result of the bosonic Matsubara sum T Σ_n 1/(ω_n² + E²). How do the Bose–Einstein and Fermi–Dirac occupation numbers emerge from coth and tanh?
4. For a massless boson gas, derive F/V = −(π²/90) g T⁴ from the free energy. What is the KMS condition, and what is the real-time alternative to the Matsubara formalism?

**自测（空白页）**

1. 从 Z = Tr e^{−βH} 出发，解释为何场论配分函数变成在周长为 β 的欧几里得时间圆周上的路径积分。为何玻色场在 τ 中周期、费米场反周期？
2. 从（反）周期性边界条件推导玻色与费米松原频率。为何频率是离散而非连续的？
3. 写出玻色松原求和 T Σ_n 1/(ω_n² + E²) 的结果。玻色–爱因斯坦与费米–狄拉克占据数如何从 coth 与 tanh 中涌现？
4. 对无质量玻色气体，从自由能推导 F/V = −(π²/90) g T⁴。KMS 条件是什么？松原形式的实时替代方案是什么？

---

← Previous: [Module 6.11 — Effective Field Theory & the Renormalization Group](./module-6.11-effective-field-theory-and-the-renormalization-group.md) · [Phase 6 index](./README.md)

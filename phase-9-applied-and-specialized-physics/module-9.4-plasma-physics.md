# Module 9.4 — Plasma Physics
**模块 9.4 — 等离子体物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.4-plasma-physics-derivations.md)

---

## 1. The Plasma State & Quasineutrality · 等离子体状态与准中性

**Definition.** A **plasma** is a partially or fully ionized gas in which collective electromagnetic effects dominate over binary collisions. It is often called the fourth state of matter. A plasma satisfies three conditions: (i) the Debye length λ_D (Section 2) is much smaller than the system size L; (ii) the number of particles in a Debye sphere N_D = (4π/3)nλ_D³ ≫ 1; (iii) the collision frequency is much less than the plasma oscillation frequency. On scales larger than λ_D the plasma is **quasineutral**: the net charge density is negligibly small, n_e ≈ Zn_i.

**定义。** **等离子体**是一种部分或完全电离的气体，其中集体电磁效应主导于二体碰撞。它通常被称为物质的第四态。等离子体满足三个条件：(i) 德拜长度 λ_D（第 2 节）远小于系统尺寸 L；(ii) 德拜球中的粒子数 N_D = (4π/3)nλ_D³ ≫ 1；(iii) 碰撞频率远小于等离子体振荡频率。在大于 λ_D 的尺度上，等离子体是**准中性的**：净电荷密度可以忽略不计，n_e ≈ Zn_i。

**Demonstration.** The Sun's corona (T ~ 10⁶ K, n ~ 10¹⁴ m⁻³) and the solar wind, laboratory fusion plasmas (T ~ 10⁸ K, n ~ 10²⁰ m⁻³), fluorescent lights, lightning, and the ionosphere all satisfy the plasma conditions. Ordinary air at room temperature is not a plasma; a candle flame is marginally so.

**演示。** 太阳日冕（T ~ 10⁶ K，n ~ 10¹⁴ m⁻³）、太阳风、实验室聚变等离子体（T ~ 10⁸ K，n ~ 10²⁰ m⁻³）、荧光灯、闪电和电离层都满足等离子体条件。室温下的普通空气不是等离子体；蜡烛火焰勉强算是。

**Application.** Plasmas constitute over 99% of the visible matter in the universe. Understanding plasma behavior is essential for magnetic confinement fusion (tokamaks), astrophysical jets, space weather prediction, and plasma processing in semiconductor manufacturing.

**应用。** 等离子体构成宇宙中超过 99% 的可见物质。理解等离子体行为对于磁约束聚变（托卡马克）、天体物理喷流、太空天气预测和半导体制造中的等离子体处理至关重要。

---

## 2. Debye Shielding · 德拜屏蔽

**Definition.** A test charge Q placed in a plasma is shielded by a cloud of oppositely charged particles that redistribute thermally. The electrostatic potential falls off as:

  φ(r) = (Q/4πε₀ r) e^{−r/λ_D},

where the **Debye shielding length** is:

  λ_D = √(ε₀ k_B T / (n e²))   (for singly charged electrons, T_e = T_i = T).

The derivation from linearized Poisson–Boltzmann theory is given in the Derivations file.

**定义。** 置于等离子体中的测试电荷 Q 被热再分布的反号电荷云屏蔽。静电势按如下规律衰减：

  φ(r) = (Q/4πε₀ r) e^{−r/λ_D}，

其中**德拜屏蔽长度**为：

  λ_D = √(ε₀ k_B T / (n e²))   （对于单电荷电子，T_e = T_i = T）。

从线性化泊松–玻尔兹曼理论的推导见推导文件。

**Demonstration.** For a hydrogen plasma with n = 10¹⁹ m⁻³ and T = 10⁴ K (a laboratory glow discharge):

  λ_D = √(8.85 × 10⁻¹² × 1.38 × 10⁻²³ × 10⁴ / (10¹⁹ × (1.6 × 10⁻¹⁹)²)) ≈ 69 μm.

The number of particles in the Debye sphere N_D = (4π/3) × 10¹⁹ × (69 × 10⁻⁶)³ ≈ 1400 ≫ 1, confirming this is a valid plasma.

**演示。** 对于 n = 10¹⁹ m⁻³、T = 10⁴ K 的氢等离子体（实验室辉光放电）：

  λ_D = √(8.85 × 10⁻¹² × 1.38 × 10⁻²³ × 10⁴ / (10¹⁹ × (1.6 × 10⁻¹⁹)²)) ≈ 69 μm。

德拜球中的粒子数 N_D = (4π/3) × 10¹⁹ × (69 × 10⁻⁶)³ ≈ 1400 ≫ 1，确认这是有效的等离子体。

**Application.** Debye shielding sets the scale for collective behavior versus binary interactions. It enters the Coulomb logarithm ln Λ ≈ ln(λ_D/b_min) that governs collisional transport in plasmas, and explains why long-range Coulomb forces are effectively short-ranged within a plasma.

**应用。** 德拜屏蔽设定集体行为与二体相互作用的尺度。它出现在支配等离子体碰撞输运的库仑对数 ln Λ ≈ ln(λ_D/b_min) 中，并解释了为何长程库仑力在等离子体内有效地变为短程的。

---

## 3. The Plasma (Langmuir) Frequency · 等离子体（朗缪尔）频率

**Definition.** If a slab of electrons is displaced from a uniform ion background by a distance x, the resulting electric field drives them back, causing oscillations. The **plasma frequency** is:

  ω_p = √(n e² / (ε₀ m_e)),

where n is the electron density, e the electron charge, and m_e the electron mass. This is the natural oscillation frequency of the electron fluid; electromagnetic waves with ω < ω_p are reflected (evanescent) inside the plasma. The derivation is in the Derivations file.

**定义。** 若一层电子从均匀离子背景中位移距离 x，由此产生的电场将其推回，引起振荡。**等离子体频率**为：

  ω_p = √(n e² / (ε₀ m_e))，

其中 n 为电子密度，e 为电子电荷，m_e 为电子质量。这是电子流体的固有振荡频率；ω < ω_p 的电磁波在等离子体内被反射（消逝）。推导见推导文件。

**Demonstration.** The ionosphere has n ~ 10¹¹ m⁻³, giving ω_p/2π ≈ 2.8 MHz. AM radio (0.5–1.6 MHz) is reflected by the ionosphere; FM radio and TV (87–800 MHz) pass through. This is why AM broadcasts propagate far around the Earth at night (the ionosphere is denser), while FM is line-of-sight.

**演示。** 电离层的 n ~ 10¹¹ m⁻³，给出 ω_p/2π ≈ 2.8 MHz。AM 广播（0.5–1.6 MHz）被电离层反射；FM 广播和电视（87–800 MHz）穿透电离层。这解释了为何 AM 广播在夜间（电离层更致密）可在地球上远距离传播，而 FM 广播是视距传输。

**Application.** The plasma frequency sets the cutoff frequency for plasma diagnostics (microwave interferometry measures n), and determines the critical density above which a laser pulse cannot propagate — crucial for inertial confinement fusion and laser–plasma interactions.

**应用。** 等离子体频率设定等离子体诊断的截止频率（微波干涉仪测量 n），并决定激光脉冲无法传播的临界密度——对惯性约束聚变和激光–等离子体相互作用至关重要。

---

## 4. Single-Particle Drifts: E×B · 单粒子漂移：E×B

**Definition.** A charged particle in perpendicular electric field E and magnetic field B undergoes a **drift** of its guiding center perpendicular to both fields:

  v_{E×B} = E × B / B²,

independent of the particle's charge, mass, and velocity. This is the **E×B drift**. Other drifts arise from a magnetic field gradient (∇B drift: v_∇B = (mv_⊥²/2eB³)(B × ∇B)) and magnetic curvature (v_curv).

**定义。** 在互相垂直的电场 E 和磁场 B 中的带电粒子，其引导中心沿垂直于两场方向发生**漂移**：

  v_{E×B} = E × B / B²，

与粒子的电荷、质量和速度无关。这是 **E×B 漂移**。其他漂移来自磁场梯度（∇B 漂移：v_∇B = (mv_⊥²/2eB³)(B × ∇B)）和磁曲率（v_curv）。

**Demonstration.** In a tokamak, the toroidal magnetic curvature creates a ∇B drift that separates ions (drifting up) and electrons (drifting down), building up a charge separation electric field E. The resulting E×B drift is radially outward for all species — the origin of toroidal drift. This is why a simple torus does not confine plasma: poloidal field coils (or the twist of field lines in a tokamak) are required to short-circuit the drift.

**演示。** 在托卡马克中，环形磁场曲率产生 ∇B 漂移，使离子（向上漂移）和电子（向下漂移）分离，积累电荷分离电场 E。由此产生的 E×B 漂移对所有粒子都径向向外——环形漂移的起源。这就是为什么简单环面无法约束等离子体：需要极向场线圈（或托卡马克中磁力线的扭曲）来短路漂移。

**Application.** E×B drifts appear in magnetospheric physics (radiation belt particle motion), Hall thrusters for spacecraft propulsion, and are responsible for plasma instabilities in confinement devices.

**应用。** E×B 漂移出现在磁层物理（辐射带粒子运动）、航天器推进的霍尔推进器中，并且是约束装置中等离子体不稳定性的根源。

---

## 5. Magnetohydrodynamics (MHD) Basics · 磁流体力学（MHD）基础

**Definition.** **Magnetohydrodynamics (MHD)** treats a plasma as a single conducting fluid, combining the Navier–Stokes equation with Maxwell's equations under the assumption that the fluid is a perfect conductor (zero resistivity). The key equations are:

  ρ(∂v/∂t + v·∇v) = −∇p + J × B   (momentum equation),
  ∂ρ/∂t + ∇·(ρv) = 0               (continuity),
  ∂B/∂t = ∇ × (v × B)              (ideal induction equation, from Faraday + Ohm E = −v×B),
  ∇ × B = μ₀ J                      (Ampère's law, low-frequency limit).

The **frozen-in flux theorem**: in ideal MHD, magnetic field lines are "frozen into" the fluid — a fluid element carries its magnetic flux with it as it moves.

**定义。** **磁流体力学（MHD）**将等离子体视为单一导电流体，在假设流体为完美导体（零电阻率）的条件下将纳维–斯托克斯方程与麦克斯韦方程结合。关键方程为：

  ρ(∂v/∂t + v·∇v) = −∇p + J × B   （动量方程），
  ∂ρ/∂t + ∇·(ρv) = 0               （连续性），
  ∂B/∂t = ∇ × (v × B)              （理想感应方程，来自法拉第 + 欧姆 E = −v×B），
  ∇ × B = μ₀ J                      （安培定律，低频极限）。

**磁通量冻结定理**：在理想 MHD 中，磁力线"冻结"在流体中——流体元素运动时携带其磁通量。

**Demonstration.** MHD supports three wave modes: Alfvén waves (transverse, v_A = B/√(μ₀ρ)), fast and slow magnetosonic waves (compressional). For a tokamak magnetic field B = 5 T and plasma density ρ = 10⁻⁶ kg/m³, the Alfvén speed v_A ≈ 5/√(4π×10⁻⁷ × 10⁻⁶) ≈ 4.5 × 10⁶ m/s ~ 1.5% c.

**演示。** MHD 支持三种波模式：阿尔芬波（横波，v_A = B/√(μ₀ρ)），快慢磁声波（压缩波）。对于托卡马克磁场 B = 5 T 和等离子体密度 ρ = 10⁻⁶ kg/m³，阿尔芬速度 v_A ≈ 5/√(4π×10⁻⁷ × 10⁻⁶) ≈ 4.5 × 10⁶ m/s ~ 1.5% c。

**Application.** MHD describes solar flares and coronal mass ejections (Alfvénic disturbances propagating along field lines), the geodynamo (Earth's magnetic field generated by conducting fluid flow in the outer core), and macroscopic stability/instability of tokamak plasmas (kink and sausage modes).

**应用。** MHD 描述太阳耀斑和日冕物质抛射（沿磁力线传播的阿尔芬扰动）、地球发电机（地球外核导电流体流动产生的地磁场），以及托卡马克等离子体的宏观稳定性/不稳定性（扭曲和腊肠模式）。

---

## 6. Collisionless Landau Damping · 无碰撞朗道阻尼

**Definition.** **Landau damping** is the attenuation of a plasma wave (Langmuir wave) in a collisionless plasma. It arises because particles with velocities near the wave phase velocity v_ph = ω/k exchange energy with the wave: slightly slower particles gain energy from the wave (are accelerated — the wave damps), while slightly faster particles lose energy to the wave (are decelerated — the wave grows). For a Maxwellian distribution the slower particles outnumber the faster ones at v_ph, so the net effect is wave damping. The damping rate is:

  γ ≈ −√(π/8) (ω_p/|k|³λ_D³) exp(−1/(2k²λ_D²) − 3/2)   (for kλ_D ≪ 1).

**定义。** **朗道阻尼**是无碰撞等离子体中等离子体波（朗缪尔波）的衰减。它产生于速度接近波相速度 v_ph = ω/k 的粒子与波交换能量：稍慢的粒子从波中获得能量（被加速——波阻尼），而稍快的粒子将能量交给波（被减速——波增长）。对于麦克斯韦分布，在 v_ph 处较慢粒子的数量多于较快粒子，因此净效果是波阻尼。阻尼率为：

  γ ≈ −√(π/8) (ω_p/|k|³λ_D³) exp(−1/(2k²λ_D²) − 3/2)   （对于 kλ_D ≪ 1）。

**Demonstration.** Landau damping was predicted theoretically by Lev Landau in 1946, decades before it was directly observed. Its existence proved that dissipation can occur in a collisionless system — a profound departure from fluid intuition. It was verified in careful laboratory experiments by Malmberg and Wharton (1964). The physical origin (wave–particle resonance) is in the Derivations file.

**演示。** 朗道阻尼由列夫·朗道于 1946 年从理论上预言，在被直接观测到之前几十年。它的存在证明了耗散可以在无碰撞系统中发生——与流体直觉的深刻背离。它由马尔姆伯格和华顿（1964 年）在精心设计的实验室实验中得到验证。物理起源（波–粒子共振）见推导文件。

**Application.** Landau damping governs the absorption of lower-hybrid and electron-cyclotron waves used for plasma heating in tokamaks. It is responsible for the damping of electrostatic fluctuations in the solar wind and determines the stability of beam–plasma systems and the Weibel instability in astrophysical shocks.

**应用。** 朗道阻尼支配托卡马克中用于等离子体加热的低杂波和电子回旋波的吸收。它负责太阳风中静电涨落的阻尼，并决定束–等离子体系统的稳定性和天体物理激波中的魏贝尔不稳定性。

---

**Self-test (blank page)**

1. State the three conditions a gas must satisfy to be called a plasma; give one example of a natural plasma and one laboratory plasma.
2. Derive or state the Debye length formula; what does it measure physically? How does λ_D change if the temperature doubles at fixed density?
3. Derive or state the plasma frequency; explain why electromagnetic waves with ω < ω_p cannot propagate inside the plasma.
4. Explain the E×B drift: why is it charge-independent? Why does this cause outward drift in a simple torus?
5. Describe in words (no formulas) the physical mechanism of Landau damping and why it requires a distribution of particle velocities.

**自测（空白页）**

1. 陈述气体被称为等离子体必须满足的三个条件；给出一个自然等离子体和一个实验室等离子体的例子。
2. 推导或陈述德拜长度公式；它从物理上测量什么？在密度固定时温度加倍，λ_D 如何变化？
3. 推导或陈述等离子体频率；解释为何 ω < ω_p 的电磁波无法在等离子体内传播。
4. 解释 E×B 漂移：为何它与电荷无关？为何这在简单环面中造成向外漂移？
5. 用文字（不用公式）描述朗道阻尼的物理机制，以及为何它需要粒子速度的分布。

---

← Previous: [Module 9.3 — Nuclear Physics](./module-9.3-nuclear-physics.md) · [Phase 9 index](./README.md) · Next: [Module 9.5 — Nuclear Reactions & Astrophysics](./module-9.5-nuclear-reactions-and-astrophysics.md) →

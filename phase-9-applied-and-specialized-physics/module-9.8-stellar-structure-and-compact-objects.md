# Module 9.8 — Stellar Structure & Compact Objects
**模块 9.8 — 恒星结构与致密天体**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.8-stellar-structure-and-compact-objects-derivations.md)

---

## 1. Hydrostatic Equilibrium & the Virial Theorem · 流体静力学平衡与位力定理

**Definition.** A star is a self-gravitating gas ball that maintains itself by balancing the inward pull of gravity against the outward push of pressure. The condition of **hydrostatic equilibrium** for a spherically symmetric star is

  dP/dr = −G m(r) ρ(r)/r²,   with   dm/dr = 4πr²ρ(r),

where P(r) is the pressure, ρ(r) the mass density, and m(r) the mass enclosed within radius r. The **virial theorem** relates the time-averaged kinetic (thermal) energy K to the gravitational potential energy U_grav of a bound system: for a non-relativistic ideal gas, 2K + U_grav = 0, i.e. the total thermal energy equals minus one half of the (negative) gravitational energy. Cross-references: Module 1.5 (Newtonian gravitation), Module 9.5 (the pressure source on the main sequence is nuclear fusion).

**定义。** 恒星是一个自引力气体球，通过平衡向内的引力与向外的压力来维持自身。球对称恒星的**流体静力学平衡**条件为

  dP/dr = −G m(r) ρ(r)/r²，   其中   dm/dr = 4πr²ρ(r)，

其中 P(r) 为压强，ρ(r) 为质量密度，m(r) 为半径 r 内包含的质量。**位力定理**将束缚系统的时间平均动能（热能）K 与引力势能 U_grav 联系起来：对于非相对论理想气体，2K + U_grav = 0，即总热能等于负的引力能（为负值）的一半。交叉引用：模块 1.5（牛顿引力）、模块 9.5（主序上的压力源是核聚变）。

**Demonstration.** Integrating the equilibrium equation gives an order-of-magnitude estimate of the central pressure. Replacing m(r) → M, r → R, and ρ → M/R³ in dP/dr ~ −GMρ/r² and integrating across the star gives P_c ~ G M²/R⁴. For the Sun this is ~10¹⁶ Pa. The virial theorem then fixes the typical internal temperature: equating the thermal energy per particle ~ kT to the gravitational energy per particle ~ GM m_H/R gives kT ~ GM m_H/R, hence T_c ~ G M m_H/(k R) ~ 10⁷ K for the Sun — hot enough to ignite hydrogen fusion.

**演示。** 积分平衡方程给出中心压强的数量级估计。在 dP/dr ~ −GMρ/r² 中将 m(r) → M、r → R、ρ → M/R³ 代入并对全星积分，给出 P_c ~ G M²/R⁴。对太阳约为 ~10¹⁶ Pa。位力定理随后确定典型内部温度：令每个粒子的热能 ~ kT 等于每个粒子的引力能 ~ GM m_H/R，给出 kT ~ GM m_H/R，故 T_c ~ G M m_H/(k R) ~ 10⁷ K（对太阳）——足够热以点燃氢聚变。

**Application.** Hydrostatic equilibrium is the master equation of stellar structure; combined with an equation of state, energy transport, and nuclear energy generation it determines a star's entire structure. The virial theorem explains why contracting protostars heat up (half the released gravitational energy goes into heat, half is radiated) and why stars are stable: a perturbation that overheats the core raises pressure and re-expands it. It is the conceptual bridge to Module 8.6 (cosmology, the virial mass of galaxy clusters).

**应用。** 流体静力学平衡是恒星结构的主方程；结合物态方程、能量输运和核能产生，它决定恒星的整个结构。位力定理解释了为何收缩的原恒星会升温（释放的引力能一半变为热能，一半被辐射掉），以及为何恒星是稳定的：使核心过热的扰动会提高压强并使其重新膨胀。它是通向模块 8.6（宇宙学，星系团的位力质量）的概念桥梁。

---

## 2. Polytropes & the Lane–Emden Equation · 多方球与莱恩–埃姆登方程

**Definition.** A **polytrope** is a self-gravitating gas whose pressure and density obey a power-law equation of state

  P = K ρ^{(n+1)/n},

where K is a constant and n is the **polytropic index**. Substituting this into hydrostatic equilibrium and Poisson's equation, and writing the density as ρ = ρ_c θ^n (where ρ_c is the central density and θ is a dimensionless function of the scaled radius ξ), reduces the structure to the dimensionless **Lane–Emden equation**

  (1/ξ²) d/dξ(ξ² dθ/dξ) = −θ^n,

with boundary conditions θ(0) = 1 and θ'(0) = 0. Cross-reference: the degeneracy equations of state of Section 3 are exactly polytropic, which is why this model dominates compact-object physics.

**定义。** **多方球**是一种自引力气体，其压强与密度服从幂律物态方程

  P = K ρ^{(n+1)/n}，

其中 K 为常数，n 为**多方指数**。将其代入流体静力学平衡和泊松方程，并将密度写为 ρ = ρ_c θ^n（其中 ρ_c 为中心密度，θ 为标度半径 ξ 的无量纲函数），把恒星结构化为无量纲的**莱恩–埃姆登方程**

  (1/ξ²) d/dξ(ξ² dθ/dξ) = −θ^n，

边界条件为 θ(0) = 1 和 θ'(0) = 0。交叉引用：第 3 节的简并物态方程恰好是多方的，这正是该模型主导致密天体物理的原因。

**Demonstration.** Three indices admit closed-form solutions: for n = 0 (incompressible), θ = 1 − ξ²/6; for n = 1, θ = sin ξ/ξ; and for n = 5, θ = (1 + ξ²/3)^{−1/2}. The surface of the star is the **first zero** ξ₁ where θ(ξ₁) = 0 (so n = 0 gives ξ₁ = √6, n = 1 gives ξ₁ = π; the n = 5 polytrope has infinite radius but finite mass). The physical radius is R = α ξ₁ and the total mass is M = 4π α³ ρ_c (−ξ²θ')_{ξ₁}, where α is the length scale set by K, ρ_c, and G. Eliminating ρ_c gives the key scaling M ∝ ρ_c^{(3−n)/2n}.

**演示。** 三个指数有闭式解：对 n = 0（不可压缩），θ = 1 − ξ²/6；对 n = 1，θ = sin ξ/ξ；对 n = 5，θ = (1 + ξ²/3)^{−1/2}。恒星表面是 θ(ξ₁) = 0 处的**第一零点** ξ₁（故 n = 0 给出 ξ₁ = √6，n = 1 给出 ξ₁ = π；n = 5 多方球半径无限但质量有限）。物理半径为 R = α ξ₁，总质量为 M = 4π α³ ρ_c (−ξ²θ')_{ξ₁}，其中 α 是由 K、ρ_c 和 G 设定的长度标度。消去 ρ_c 给出关键标度关系 M ∝ ρ_c^{(3−n)/2n}。

**Application.** Polytropes provide analytic stellar models without solving the full set of structure equations. The n = 3 polytrope (the "Eddington standard model") describes both a radiation-pressure-dominated main-sequence star and an ultra-relativistic degenerate gas; its special property — that M is independent of ρ_c — is precisely what produces the Chandrasekhar limiting mass (Section 4). The n = 3/2 polytrope describes fully convective stars and non-relativistic white dwarfs.

**应用。** 多方球在不求解完整结构方程组的情况下提供解析恒星模型。n = 3 多方球（"爱丁顿标准模型"）既描述辐射压主导的主序星，也描述超相对论简并气体；其特殊性质——M 与 ρ_c 无关——正是产生钱德拉塞卡极限质量的原因（第 4 节）。n = 3/2 多方球描述完全对流恒星和非相对论白矮星。

---

## 3. Electron Degeneracy Pressure · 电子简并压

**Definition.** When matter is compressed to high density, the electrons form a degenerate Fermi gas: by the Pauli exclusion principle they fill momentum states up to the Fermi momentum p_F even at T = 0, producing a pressure independent of temperature — the **degeneracy pressure**. From the T = 0 Fermi gas (Modules 2.5/2.6) the electron pressure takes two limiting forms. In the **non-relativistic** limit (p_F ≪ m_e c),

  P = K_NR (ρ/μ_e m_H)^{5/3},   K_NR = (3π²)^{2/3} ℏ²/(5 m_e),

a polytrope of index n = 3/2. In the **ultra-relativistic** limit (p_F ≫ m_e c),

  P = K_UR (ρ/μ_e m_H)^{4/3},   K_UR = (3π²)^{1/3} ℏc/4,

a polytrope of index n = 3. Here n_e = ρ/(μ_e m_H) is the electron number density and μ_e is the mean molecular weight per electron (μ_e ≈ 2 for fully ionized helium, carbon, or oxygen).

**定义。** 当物质被压缩到高密度时，电子形成简并费米气体：由泡利不相容原理，即使在 T = 0 时它们也填满直到费米动量 p_F 的动量态，产生一个与温度无关的压强——**简并压**。由 T = 0 费米气体（模块 2.5/2.6），电子压强有两个极限形式。在**非相对论**极限（p_F ≪ m_e c）下，

  P = K_NR (ρ/μ_e m_H)^{5/3}，   K_NR = (3π²)^{2/3} ℏ²/(5 m_e)，

是指数 n = 3/2 的多方球。在**超相对论**极限（p_F ≫ m_e c）下，

  P = K_UR (ρ/μ_e m_H)^{4/3}，   K_UR = (3π²)^{1/3} ℏc/4，

是指数 n = 3 的多方球。这里 n_e = ρ/(μ_e m_H) 为电子数密度，μ_e 为每个电子的平均分子量（对完全电离的氦、碳或氧，μ_e ≈ 2）。

**Demonstration.** The two exponents follow directly from the energy–momentum relation. The number density fixes p_F via n_e = p_F³/(3π²ℏ³), so p_F ∝ n_e^{1/3} ∝ ρ^{1/3}. Non-relativistic electrons have kinetic energy ε ∝ p², and the pressure (energy density scale) gives P ∝ n_e p_F² ∝ ρ^{5/3}. Ultra-relativistic electrons have ε ≈ pc, giving P ∝ n_e p_F ∝ ρ^{4/3}. The softening of the exponent from 5/3 to 4/3 as electrons turn relativistic is the seed of gravitational instability and the Chandrasekhar limit.

**演示。** 两个指数直接来自能量–动量关系。数密度通过 n_e = p_F³/(3π²ℏ³) 确定 p_F，故 p_F ∝ n_e^{1/3} ∝ ρ^{1/3}。非相对论电子的动能 ε ∝ p²，压强（能量密度标度）给出 P ∝ n_e p_F² ∝ ρ^{5/3}。超相对论电子的 ε ≈ pc，给出 P ∝ n_e p_F ∝ ρ^{4/3}。当电子变为相对论性时，指数从 5/3 软化到 4/3，这是引力不稳定性和钱德拉塞卡极限的根源。

**Application.** Electron degeneracy pressure supports white dwarfs (the end state of stars below ~8 M_⊙) against gravity, independent of their (cooling) temperature. The same degeneracy physics governs the electron gas in metals (Module 2.6) and the onset of the helium flash in red giants, where a degenerate helium core ignites explosively because degeneracy pressure does not respond to the temperature rise.

**应用。** 电子简并压支撑白矮星（约 8 M_⊙ 以下恒星的终态）抵抗引力，与其（冷却的）温度无关。同样的简并物理支配金属中的电子气（模块 2.6）以及红巨星中氦闪的发生，在那里简并的氦核爆发性点火，因为简并压不响应温度升高。

---

## 4. White Dwarfs & the Chandrasekhar Mass · 白矮星与钱德拉塞卡质量

**Definition.** A **white dwarf** is a compact object supported by non-relativistic electron degeneracy pressure, modeled as an n = 3/2 polytrope. The mass–radius scaling M ∝ ρ_c^{(3−n)/2n} with n = 3/2 gives the famous **inverse mass–radius relation**

  R ∝ M^{−1/3},

so a more massive white dwarf is smaller and denser. As M increases the central density rises, the electrons become ultra-relativistic, and the star approaches an n = 3 polytrope, whose mass is independent of ρ_c. This singles out a unique limiting mass, the **Chandrasekhar mass**

  M_Ch = (ω₃ √(3π)/2) (ℏc/G)^{3/2} / (μ_e m_H)² ≈ 1.4 M_⊙   (for μ_e = 2),

where ω₃ = (−ξ²θ')_{ξ₁} ≈ 2.018 is the n = 3 Lane–Emden mass constant.

**定义。** **白矮星**是由非相对论电子简并压支撑的致密天体，建模为 n = 3/2 多方球。质量–半径标度 M ∝ ρ_c^{(3−n)/2n}（n = 3/2）给出著名的**反向质量–半径关系**

  R ∝ M^{−1/3}，

故质量越大的白矮星越小、越致密。随着 M 增大，中心密度上升，电子变为超相对论性，恒星趋于 n = 3 多方球，其质量与 ρ_c 无关。这确定了一个唯一的极限质量，即**钱德拉塞卡质量**

  M_Ch = (ω₃ √(3π)/2) (ℏc/G)^{3/2} / (μ_e m_H)² ≈ 1.4 M_⊙   （对 μ_e = 2），

其中 ω₃ = (−ξ²θ')_{ξ₁} ≈ 2.018 为 n = 3 莱恩–埃姆登质量常数。

**Demonstration.** The physical meaning is dramatic: the n = 3 polytrope mass M = 4π α³ ρ_c ω₃ has its ρ_c dependence cancel exactly (α ∝ ρ_c^{−1/3} so α³ρ_c is constant), leaving M fixed by fundamental constants alone. The numerical value follows from inserting K_UR, ω₃ ≈ 2.018, and μ_e = 2: M_Ch ≈ 5.83/μ_e² M_⊙ ≈ 1.46 M_⊙ ≈ 1.4 M_⊙. Above this mass, ultra-relativistic degeneracy pressure (P ∝ ρ^{4/3}) scales with radius exactly as gravity does, so it can never win: no equilibrium exists and the star must collapse.

**演示。** 物理意义是戏剧性的：n = 3 多方球质量 M = 4π α³ ρ_c ω₃ 的 ρ_c 依赖性恰好抵消（α ∝ ρ_c^{−1/3} 故 α³ρ_c 为常数），M 仅由基本常数确定。数值由代入 K_UR、ω₃ ≈ 2.018 和 μ_e = 2 得到：M_Ch ≈ 5.83/μ_e² M_⊙ ≈ 1.46 M_⊙ ≈ 1.4 M_⊙。超过此质量，超相对论简并压（P ∝ ρ^{4/3}）随半径的标度方式与引力完全相同，故永远无法取胜：不存在平衡，恒星必然坍缩。

**Application.** The Chandrasekhar mass is one of the most important numbers in astrophysics. A white dwarf accreting matter from a binary companion that crosses M_Ch ignites runaway carbon fusion and explodes as a **Type Ia supernova** — the near-uniform M_Ch makes these "standard candles" that measured the accelerating expansion of the universe (Module 8.6). Above M_Ch, electron degeneracy fails and collapse proceeds toward a neutron star (Section 5).

**应用。** 钱德拉塞卡质量是天体物理中最重要的数字之一。从双星伴星吸积物质并越过 M_Ch 的白矮星会引发失控的碳聚变，作为 **Ia 型超新星**爆发——近乎均匀的 M_Ch 使其成为"标准烛光"，用以测量宇宙的加速膨胀（模块 8.6）。超过 M_Ch，电子简并失效，坍缩朝中子星进行（第 5 节）。

---

## 5. Neutron Stars & the TOV Equation · 中子星与 TOV 方程

**Definition.** When collapse pushes a stellar core beyond the Chandrasekhar mass, electrons are forced into protons by **inverse beta decay** (p + e⁻ → n + ν_e), neutronizing the matter. Collapse halts when **neutron degeneracy pressure** — the same Fermi-gas physics of Section 3 but with neutrons (mass m_n ≫ m_e) — becomes large enough to support the star. The result is a **neutron star**: roughly 1.4 M_⊙ packed into a radius of ~10 km, with central density exceeding nuclear density (~10¹⁷ kg/m³). Cross-references: Modules 7.5/7.6 (general relativity, compact objects, black holes).

**定义。** 当坍缩将恒星核心推过钱德拉塞卡质量时，电子通过**逆 β 衰变**（p + e⁻ → n + ν_e）被压入质子，使物质中子化。当**中子简并压**——与第 3 节相同的费米气体物理但换成中子（质量 m_n ≫ m_e）——变得足够大以支撑恒星时，坍缩停止。结果是**中子星**：约 1.4 M_⊙ 被压入 ~10 km 的半径，中心密度超过核密度（~10¹⁷ kg/m³）。交叉引用：模块 7.5/7.6（广义相对论、致密天体、黑洞）。

**Demonstration.** A neutron star is so compact that Newtonian hydrostatic equilibrium is inadequate; the correct treatment uses the **Tolman–Oppenheimer–Volkoff (TOV) equation**, the general-relativistic generalization of dP/dr = −Gmρ/r²:

  dP/dr = −G[ρ + P/c²][m + 4πr³P/c²]/[r²(1 − 2Gm/rc²)].

Each general-relativistic correction factor (in brackets) exceeds unity, making gravity stronger than Newtonian and lowering the maximum supportable mass. Solving the TOV equation with a realistic nuclear equation of state yields a **maximum neutron-star mass** of ~2–3 M_⊙ (the Tolman–Oppenheimer–Volkoff limit).

**演示。** 中子星如此致密，以致牛顿流体静力学平衡不再适用；正确的处理使用 **托尔曼–奥本海默–沃尔科夫（TOV）方程**，即 dP/dr = −Gmρ/r² 的广义相对论推广：

  dP/dr = −G[ρ + P/c²][m + 4πr³P/c²]/[r²(1 − 2Gm/rc²)]。

每个广义相对论修正因子（方括号内）都大于 1，使引力强于牛顿引力，从而降低可支撑的最大质量。用真实核物态方程求解 TOV 方程给出 ~2–3 M_⊙ 的**最大中子星质量**（托尔曼–奥本海默–沃尔科夫极限）。

**Application.** Neutron stars are observed as **pulsars** (rotating magnetized neutron stars beaming radio pulses) and in X-ray binaries. Above the TOV maximum mass, no known pressure can resist gravity and the object collapses to a **black hole** (Modules 7.5/7.6). The merger of two neutron stars produces gravitational waves and a kilonova, and the nuclear equation of state — still uncertain — is now being constrained by gravitational-wave tidal measurements and pulsar mass–radius data.

**应用。** 中子星被观测为**脉冲星**（旋转的磁化中子星发出射电脉冲）和 X 射线双星。超过 TOV 最大质量，没有已知的压力能抵抗引力，天体坍缩为**黑洞**（模块 7.5/7.6）。两颗中子星的并合产生引力波和千新星，而核物态方程——仍不确定——正在被引力波潮汐测量和脉冲星质量–半径数据约束。

---

**Self-test (blank page)**

1. Derive the equation of hydrostatic equilibrium from force balance on a thin shell, and use it to estimate the central pressure and temperature of the Sun via the virial theorem.
2. Starting from P = K ρ^{(n+1)/n} and ρ = ρ_c θ^n, derive the Lane–Emden equation. State the closed-form solutions for n = 0, 1, 5 and explain how ξ₁ fixes the stellar radius.
3. From the T = 0 Fermi gas, derive both the non-relativistic (P ∝ ρ^{5/3}) and ultra-relativistic (P ∝ ρ^{4/3}) electron degeneracy pressures, and identify the corresponding polytropic indices.
4. Explain why a non-relativistic white dwarf obeys R ∝ M^{−1/3} and why the ultra-relativistic limit produces a unique mass M_Ch ≈ 1.4 M_⊙ independent of central density.

**自测（空白页）**

1. 从薄壳上的力平衡推导流体静力学平衡方程，并用它通过位力定理估计太阳的中心压强和温度。
2. 从 P = K ρ^{(n+1)/n} 和 ρ = ρ_c θ^n 出发，推导莱恩–埃姆登方程。陈述 n = 0、1、5 的闭式解，并解释 ξ₁ 如何确定恒星半径。
3. 从 T = 0 费米气体推导非相对论（P ∝ ρ^{5/3}）和超相对论（P ∝ ρ^{4/3}）电子简并压，并指出对应的多方指数。
4. 解释为何非相对论白矮星服从 R ∝ M^{−1/3}，以及为何超相对论极限产生唯一的、与中心密度无关的质量 M_Ch ≈ 1.4 M_⊙。

---

← Previous: [Module 9.7 — Atoms in External Fields & Precision Spectroscopy](./module-9.7-atoms-in-external-fields.md) · [Phase 9 index](./README.md)

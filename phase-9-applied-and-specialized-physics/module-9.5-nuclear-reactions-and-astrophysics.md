# Module 9.5 — Nuclear Reactions & Astrophysics
**模块 9.5 — 核反应与天体物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.5-nuclear-reactions-and-astrophysics-derivations.md)

---

## 1. Nuclear Reaction Kinematics & the Q-Value · 核反应运动学与 Q 值

**Definition.** A two-body nuclear reaction a + A → b + B is characterized by its **Q-value**, the energy released (Q > 0, exothermic) or absorbed (Q < 0, endothermic) in the reaction:

  Q = (m_a + m_A − m_b − m_B) c²,

where masses are nuclear rest masses. In the lab frame (A at rest), the minimum kinetic energy of projectile a needed to make the reaction go (when Q < 0) is the **threshold kinetic energy**:

  T_th = −Q (m_a + m_A + m_b + m_B) / (2 m_A),

which exceeds |Q| because some kinetic energy is unavoidably consumed in the center-of-mass motion. The full derivation appears in the Derivations file.

**定义。** 两体核反应 a + A → b + B 的特征量是其 **Q 值**——反应释放（Q > 0，放热）或吸收（Q < 0，吸热）的能量：

  Q = (m_a + m_A − m_b − m_B) c²，

其中质量为核静止质量。在实验室系（A 静止）中，使反应发生所需的入射粒子 a 的最小动能（当 Q < 0 时）为**阈动能**：

  T_th = −Q (m_a + m_A + m_b + m_B) / (2 m_A)，

它超过 |Q|，因为部分动能不可避免地消耗于质心运动。完整推导见推导文件。

**Demonstration.** Consider the reaction p + ⁷Li → ⁴He + ⁴He. The Q-value uses nuclear masses: Q = (m_p + m(⁷Li) − 2 m(⁴He))c² ≈ (1.007825 + 7.016003 − 2 × 4.002602) u × 931.5 MeV/u ≈ 17.3 MeV. Since Q > 0 there is no threshold: even a thermal proton (keV) can initiate this reaction once it overcomes the Coulomb barrier (the dominant obstacle at low energies).

**演示。** 考虑反应 p + ⁷Li → ⁴He + ⁴He。Q 值用核质量计算：Q = (m_p + m(⁷Li) − 2 m(⁴He))c² ≈ (1.007825 + 7.016003 − 2 × 4.002602) u × 931.5 MeV/u ≈ 17.3 MeV。因 Q > 0，没有阈值：即使是热质子（keV 量级）一旦克服库仑势垒（低能量下的主要障碍）也能引发此反应。

**Application.** Q-values determine whether a reaction is energetically favorable: they set the energy balance in stellar fusion chains (Section 4), in nuclear reactors, and in the production of medical radioisotopes. The threshold formula is used to design accelerator experiments that cannot be performed below a minimum beam energy.

**应用。** Q 值决定反应在能量上是否可行：它们设定恒星聚变链（第 4 节）、核反应堆及医用放射性同位素生产中的能量平衡。阈值公式用于设计不能低于最低束能运行的加速器实验。

---

## 2. Nuclear Cross-Sections: Compound Nucleus vs Direct Reactions · 核截面：复合核与直接反应

**Definition.** The **cross-section** σ(E) quantifies the probability of a nuclear reaction: dN_reactions/dt = σ n_target v_rel per projectile, with σ having units of area (barn = 10⁻²⁸ m²). Two qualitatively different mechanisms operate:

**Compound-nucleus (Breit–Wigner) reactions.** At certain resonance energies E_r, the projectile is captured to form a long-lived intermediate nucleus that subsequently decays. The resonance cross-section is given by the **Breit–Wigner formula**:

  σ(E) = σ_r Γ² / [(E − E_r)² + Γ²/4],

where σ_r = π λ-bar² (2J_r + 1)/[(2J_a + 1)(2J_A + 1)] is the peak cross-section at resonance (λ-bar = ℏ/p the reduced de Broglie wavelength), and **Γ is the total width** (related to the resonance lifetime by Γ = ℏ/τ). The full derivation from the S-matrix is in the Derivations file.

**Direct reactions.** At higher energies (or with loosely bound projectiles), the reaction involves only a few nucleons — a nucleon is stripped (stripping reaction) or picked up (pick-up reaction) in a single fast encounter (t ~ 10⁻²² s vs 10⁻¹⁶ s for the compound nucleus). Cross-sections vary smoothly with energy and can be factored into a spectroscopic factor times a single-particle cross-section.

**定义。** **截面** σ(E) 量化核反应的概率：dN_reactions/dt = σ n_target v_rel（每入射粒子），σ 的单位为面积（靶 = 10⁻²⁸ m²）。有两种本质上不同的机制：

**复合核（布雷特–维格纳）反应。** 在某些共振能量 E_r 处，入射粒子被俘获形成长寿命的中间核，随后衰变。共振截面由**布雷特–维格纳公式**给出：

  σ(E) = σ_r Γ² / [(E − E_r)² + Γ²/4]，

其中 σ_r = π λ-bar² (2J_r + 1)/[(2J_a + 1)(2J_A + 1)] 是共振峰值截面（λ-bar = ℏ/p 为约化德布罗意波长），**Γ 为总宽度**（通过 Γ = ℏ/τ 与共振寿命相关）。从 S 矩阵出发的完整推导见推导文件。

**直接反应。** 在较高能量（或使用松散束缚的入射粒子）时，反应仅涉及少数核子——在一次快速相遇中剥离（剥离反应）或拾取（拾取反应）一个核子（t ~ 10⁻²² s，对比复合核的 10⁻¹⁶ s）。截面随能量平滑变化，可分解为谱因子乘以单粒子截面。

**Demonstration.** Neutron absorption in ²³⁸U displays famous low-energy resonances (the first at E_r ≈ 6.67 eV, Γ ≈ 0.027 eV) that dominate the cross-section there. The peak value σ_r ~ 10⁴ barn is some 10⁵ times larger than the geometrical cross-section πR² ~ 0.17 barn, a direct consequence of the de Broglie wavelength λ-bar ≫ R at such low energies.

**演示。** ²³⁸U 中的中子吸收在低能区呈现著名的共振（第一个共振在 E_r ≈ 6.67 eV，Γ ≈ 0.027 eV），主导该能区的截面。峰值 σ_r ~ 10⁴ 靶远大于几何截面 πR² ~ 0.17 靶约 10⁵ 倍，这是该低能量下德布罗意波长 λ-bar ≫ R 的直接结果。

**Application.** Breit–Wigner resonances are used to engineer reactor moderators and shielding materials (by matching neutron energies to absorption resonances), and are the mechanism behind the Mössbauer effect. Direct reactions (such as (d, p) stripping) are precision spectroscopic tools that measure the single-particle occupancy of nuclear levels — directly probing the shell structure of Module 9.3.

**应用。** 布雷特–维格纳共振用于设计反应堆慢化剂和屏蔽材料（通过使中子能量与吸收共振匹配），也是穆斯堡尔效应背后的机制。直接反应（如 (d, p) 剥离反应）是精密谱学工具，测量核能级的单粒子占据——直接探测模块 9.3 的壳层结构。

---

## 3. Beyond the Shell Model: Collective Nuclear Structure · 超越壳层模型：集体核结构

**Definition.** The shell model (Module 9.3) works well near closed shells. Away from them, nuclei are **deformed** and exhibit collective motions of many nucleons acting together: rotations and vibrations of the nuclear shape.

**Rotational bands.** A deformed nucleus with moment of inertia ℐ rotates as a quantum symmetric top. Angular momentum is quantized in integer steps, and the spectrum of a **ground-state rotational band** is:

  E_J = ℏ² J(J+1) / (2ℐ),   J = 0, 2, 4, 6, …  (for even–even nuclei),

where only even J appear because of the left–right symmetry of the nuclear shape. The derivation from the rigid-rotor Hamiltonian is in the Derivations file.

**Vibrational states.** Near a spherical equilibrium the nuclear surface vibrates at a set of normal-mode frequencies ω_λ (multipole vibrations: λ = 2 quadrupole, λ = 3 octupole, …). Each mode is quantized as a harmonic oscillator, with phonon excitations at energies ℏω_λ, 2ℏω_λ, … The **collective model** (Bohr–Mottelson) unifies rotation and vibration in a single Hamiltonian for the surface shape variables α_λμ.

**定义。** 壳层模型（模块 9.3）在闭壳层附近运行良好。远离闭壳层时，核是**形变的**，表现出许多核子共同运动的集体运动：核形状的转动和振动。

**转动带。** 具有转动惯量 ℐ 的形变核像量子对称陀螺一样转动。角动量以整数步量子化，**基态转动带**的谱为：

  E_J = ℏ² J(J+1) / (2ℐ)，   J = 0, 2, 4, 6, …（对偶–偶核），

由于核形状的左右对称性，仅出现偶数 J。从刚性转子哈密顿量出发的推导见推导文件。

**振动态。** 在球形平衡附近，核表面以一组本征频率 ω_λ 振动（多极振动：λ = 2 四极，λ = 3 八极，……）。每种模式像谐振子一样量子化，声子激发能量为 ℏω_λ, 2ℏω_λ, …… **集体模型**（玻尔–莫特尔森）将转动和振动统一在关于核表面形状变量 α_λμ 的单一哈密顿量中。

**Demonstration.** In ¹⁵²Sm (a rare-earth nucleus well away from closed shells), the observed 2⁺ level is at 121.8 keV and the 4⁺ level at 366.5 keV. The rigid-rotor formula predicts E(4⁺)/E(2⁺) = [4·5]/[2·3] = 10/3 = 3.33. The measured ratio is 366.5/121.8 ≈ 3.01, close to the rotational limit (deviations signal the non-rigidity of the nucleus). Compare ⁵²Cr near a closed shell: E(4⁺)/E(2⁺) ≈ 2.1, close to the vibrational limit of 2.

**演示。** 在 ¹⁵²Sm（远离闭壳层的稀土核）中，观测到的 2⁺ 能级在 121.8 keV，4⁺ 能级在 366.5 keV。刚性转子公式预测 E(4⁺)/E(2⁺) = [4·5]/[2·3] = 10/3 = 3.33。实测比值为 366.5/121.8 ≈ 3.01，接近转动极限（偏差表征核的非刚性）。对比靠近闭壳层的 ⁵²Cr：E(4⁺)/E(2⁺) ≈ 2.1，接近振动极限 2。

**Application.** Rotational and vibrational spectra are measured by gamma-ray spectroscopy following nuclear reactions. The collective model is essential for understanding the giant dipole resonance (a collective oscillation of all protons against all neutrons), nuclear fission dynamics (deformation path to the saddle point), and octupole correlations near the atomic number Z = 88 relevant to searches for a permanent atomic electric dipole moment.

**应用。** 转动和振动谱通过核反应后的 γ 射线谱学测量。集体模型对于理解巨偶极共振（所有质子相对所有中子的集体振荡）、核裂变动力学（向鞍点的形变路径）以及与寻找永久原子电偶极矩相关的 Z = 88 附近的八极关联至关重要。

---

## 4. Stellar Fusion: the p–p Chain and the CNO Cycle · 恒星聚变：pp 链与 CNO 循环

**Definition.** Stars generate energy by fusing hydrogen to helium. In the **proton–proton (p–p) chain** (dominant in stars with core temperature T < ~1.5 × 10⁷ K, including the Sun):

  p + p → ²H + e⁺ + ν_e         (weak interaction, very slow; rate-limiting step)
  p + ²H → ³He + γ
  ³He + ³He → ⁴He + 2p

Net: 4p → ⁴He + 2e⁺ + 2ν_e + 2γ,   Q_net ≈ 26.7 MeV (after subtracting annihilation energy).

In the **CNO cycle** (dominant for T > 1.5 × 10⁷ K, as in massive stars), carbon, nitrogen, and oxygen nuclei act as catalysts, and the net reaction is also 4p → ⁴He + 2e⁺ + 2ν_e but with different temperature dependence (rate ∝ T^20 vs T^4 for pp). The CNO cycle is responsible for most of the Sun's energy production in the core where T is highest, and dominates in stars more than 1.3 M_⊙.

**定义。** 恒星通过将氢聚变为氦来产生能量。在**质子–质子（pp）链**中（在核温度 T < ~1.5 × 10⁷ K 的恒星，包括太阳中占主导地位）：

  p + p → ²H + e⁺ + ν_e         （弱相互作用，极慢；限速步骤）
  p + ²H → ³He + γ
  ³He + ³He → ⁴He + 2p

净反应：4p → ⁴He + 2e⁺ + 2ν_e + 2γ，Q_net ≈ 26.7 MeV（减去湮没能量后）。

在 **CNO 循环**中（在 T > 1.5 × 10⁷ K 时占主导地位，如大质量恒星），碳、氮、氧核作为催化剂，净反应也是 4p → ⁴He + 2e⁺ + 2ν_e，但温度依赖性不同（速率 ∝ T²⁰，对比 pp 链的 T⁴）。CNO 循环负责太阳核心温度最高处的大部分能量产生，并在质量超过 1.3 M_⊙ 的恒星中占主导地位。

**Demonstration.** The Sun luminosity L_⊙ ≈ 3.85 × 10²⁶ W and the energy per pp-chain completion Q ≈ 26.7 MeV ≈ 4.28 × 10⁻¹² J imply a reaction rate of L_⊙/Q ≈ 9 × 10³⁷ s⁻¹. Each cycle converts 4 proton masses to one alpha particle plus energy; the mass deficit per cycle is ≈ 0.7% of the input mass. The Sun converts ≈ 4.3 × 10⁹ kg of mass to energy every second. Solar neutrinos (2 per pp completion) carry away ≈ 2% of the energy and have been detected at Kamiokande, SNO, and Borexino — directly confirming the pp chain is the Sun's energy source.

**演示。** 太阳光度 L_⊙ ≈ 3.85 × 10²⁶ W 和每次 pp 链完成的能量 Q ≈ 26.7 MeV ≈ 4.28 × 10⁻¹² J 意味着反应速率为 L_⊙/Q ≈ 9 × 10³⁷ s⁻¹。每个循环将 4 个质子质量转化为一个 α 粒子加能量；每个循环的质量亏损约为输入质量的 0.7%。太阳每秒将约 4.3 × 10⁹ kg 质量转化为能量。太阳中微子（每次 pp 完成产生 2 个）携带约 2% 的能量，已在神冈、SNO 和 Borexino 探测到——直接证实了 pp 链是太阳的能量来源。

**Application.** The pp chain rate is calibrated to the solar neutrino flux (the "solar neutrino problem" led to the discovery of neutrino oscillations — Module 8.5 context). CNO-cycle measurement in the Sun's core (recent Borexino data) constrains the solar metallicity. The temperature dependence of these cycles determines the main-sequence lifetime of stars and their evolutionary tracks in the Hertzsprung–Russell diagram.

**应用。** pp 链速率通过太阳中微子通量校准（"太阳中微子问题"导致发现了中微子振荡——模块 8.5 背景）。太阳核心 CNO 循环的测量（近期 Borexino 数据）限制了太阳金属度。这些循环的温度依赖性决定主序星的寿命及其在赫罗图中的演化轨迹。

---

## 5. The Gamow Peak & Thermonuclear Reaction Rates · 伽莫夫峰与热核反应速率

**Definition.** The **thermonuclear reaction rate** per pair of fusing nuclei at temperature T is the thermal average:

  ⟨σv⟩ = ∫₀^∞ σ(E) v f(E) dE,

where f(E) is the Maxwell–Boltzmann energy distribution ∝ E^{1/2} exp(−E/k_B T) (the thermal tail). The cross-section for charged-particle fusion vanishes exponentially at low energies because of Coulomb tunnelling (derived in Module 9.3 — the Gamow factor):

  σ(E) ∝ (1/E) exp(−2πη),   with  η = Z_a Z_A e²/(ℏv) = Z_a Z_A α √(μc²/(2E)),

where μ is the reduced mass. The product of the decreasing MB tail and the increasing tunnelling factor peaks sharply at the **Gamow peak energy**:

  E_0 = (π α Z_a Z_A √(μc²/2) k_B T)^{2/3} / (2^{1/3})

  E_0 ≈ 1.22 (Z_a² Z_A² μ/m_u)^{1/3} (T/10⁷ K)^{2/3}   keV,

with a width Δ ∝ E_0^{1/2} (k_B T)^{1/2}. The full derivation is in the Derivations file.

**定义。** 温度 T 下每对聚变核的**热核反应速率**是热平均：

  ⟨σv⟩ = ∫₀^∞ σ(E) v f(E) dE，

其中 f(E) 是麦克斯韦–玻尔兹曼能量分布 ∝ E^{1/2} exp(−E/k_B T)（热尾）。带电粒子聚变的截面在低能量处因库仑隧穿而指数衰减（在模块 9.3 中推导——伽莫夫因子）：

  σ(E) ∝ (1/E) exp(−2πη)，其中 η = Z_a Z_A e²/(ℏv) = Z_a Z_A α √(μc²/(2E))，

μ 为约化质量。MB 尾（递减）与隧穿因子（递增）的乘积在**伽莫夫峰能量**处急剧达到峰值：

  E_0 = (π α Z_a Z_A √(μc²/2) k_B T)^{2/3} / (2^{1/3})

  E_0 ≈ 1.22 (Z_a² Z_A² μ/m_u)^{1/3} (T/10⁷ K)^{2/3}   keV，

宽度 Δ ∝ E_0^{1/2} (k_B T)^{1/2}。完整推导见推导文件。

**Demonstration.** For p + p fusion at the solar core temperature T_c ≈ 1.57 × 10⁷ K: the thermal energy k_B T ≈ 1.35 keV, but E_0 ≈ 6 keV. The reaction occurs in a narrow window far above the thermal peak. The probability is dominated by the factor exp(−2πη) ≈ exp(−31) ~ 10⁻¹³ — which is why the pp rate is extremely slow (each proton fuses on a timescale of ~10¹⁰ years) and the Sun is long-lived.

**演示。** 对于太阳核心温度 T_c ≈ 1.57 × 10⁷ K 下的 p + p 聚变：热能 k_B T ≈ 1.35 keV，但 E_0 ≈ 6 keV。反应发生在远高于热峰的狭窄窗口内。概率由因子 exp(−2πη) ≈ exp(−31) ~ 10⁻¹³ 主导——这就是 pp 速率极慢（每个质子聚变的时间尺度约 10¹⁰ 年）以及太阳寿命长的原因。

**Application.** The Gamow peak governs all thermonuclear reaction rates. It is the reason stellar burning temperatures are so high: stars must reach T ~ 10⁷–10⁹ K to achieve measurable Gamow-peak tunnelling rates. When a Breit–Wigner resonance (Section 2) falls inside the Gamow window, the stellar rate is hugely enhanced — a **stellar resonance**. The famous 7.65 MeV ³⁺ state in ¹²C (predicted by Hoyle and found experimentally) is one such resonance, making carbon synthesis possible (Section 6).

**应用。** 伽莫夫峰支配所有热核反应速率。它是恒星燃烧温度如此之高的原因：恒星必须达到 T ~ 10⁷–10⁹ K 才能实现可测量的伽莫夫峰隧穿速率。当布雷特–维格纳共振（第 2 节）落在伽莫夫窗口内时，恒星速率被大幅增强——**恒星共振**。¹²C 中著名的 7.65 MeV 3⁺ 态（由霍伊尔预言并由实验发现）就是这样一个共振态，使碳合成成为可能（第 6 节）。

---

## 6. The Triple-Alpha Process & Nucleosynthesis · 三 α 过程与核合成

**Definition.** When core hydrogen is exhausted, stars contract, heat up, and begin **helium burning** via the **triple-alpha process**:

  ⁴He + ⁴He ↔ ⁸Be*   (resonance, T½ = 8.2 × 10⁻¹⁷ s — quasi-equilibrium),
  ⁸Be* + ⁴He → ¹²C* (7.65 MeV 0⁺₂ Hoyle state) → ¹²C + 2γ,

with Q ≈ 7.27 MeV. The Hoyle state, nearly resonant with the three-alpha threshold, makes this rate ~10²⁶ times faster than without it — Hoyle's 1954 prediction of its existence, confirmed experimentally by Cook et al., is one of the great predictions in nuclear astrophysics.

**Nucleosynthesis of the elements** was codified by Burbidge, Burbidge, Fowler & Hoyle (B²FH, 1957):

- **s-process (slow neutron capture):** Neutrons are captured on timescales much longer than beta-decay lifetimes, so the nucleus has time to beta-decay to the stability valley after each capture. The reaction path closely follows the valley of stability. Occurs in AGB stars, producing elements up to Bi (A ≈ 209).
- **r-process (rapid neutron capture):** Neutron fluxes are so intense that many successive captures occur before any beta decay. The reaction path runs far from stability, toward very neutron-rich nuclei, and terminates when nuclei become unstable to fission. Requires extreme environments: neutron star mergers (confirmed by kilonova GW170817) and core-collapse supernovae. Produces ~half of all nuclei heavier than iron, including gold, platinum, and uranium.

**定义。** 当核心氢耗尽时，恒星收缩、升温，并通过**三 α 过程**开始**氦燃烧**：

  ⁴He + ⁴He ↔ ⁸Be*   （共振，T½ = 8.2 × 10⁻¹⁷ s——准平衡），
  ⁸Be* + ⁴He → ¹²C*（7.65 MeV 0⁺₂ 霍伊尔态）→ ¹²C + 2γ，

Q ≈ 7.27 MeV。霍伊尔态与三 α 阈值几乎共振，使此速率比没有它时快约 10²⁶ 倍——霍伊尔 1954 年对其存在的预言，由库克等人通过实验证实，是核天体物理中最伟大的预言之一。

**元素核合成**由伯比奇、伯比奇、福勒和霍伊尔（B²FH，1957 年）系统化：

- **s 过程（慢中子俘获）：** 中子俘获的时间尺度远长于 β 衰变寿命，因此核在每次俘获后有时间 β 衰变到稳定性谷。反应路径紧随稳定性谷。发生在 AGB 星中，产生直至 Bi（A ≈ 209）的元素。
- **r 过程（快中子俘获）：** 中子通量如此之强，以至于在任何 β 衰变之前就发生了许多连续俘获。反应路径偏离稳定区很远，走向极富中子的核，并在核对裂变不稳定时终止。需要极端环境：中子星并合（由千新星 GW170817 证实）和核塌缩超新星。产生铁以上约一半的所有核，包括金、铂和铀。

**Demonstration.** The mass abundances of the s-process elements (Sr, Ba, Pb) reflect the neutron-capture cross-section times the stellar flux — nuclei with magic neutron numbers (50, 82, 126) have very small cross-sections and pile up as s-process peaks in the abundance distribution. The r-process peaks are displaced by ~8–10 mass units below the s-process peaks (the path runs through more neutron-rich nuclei that beta-decay back toward stability after the r-process). Observation of freshly synthesized r-process elements (Eu, Au, Pt) in the kilonova AT2017gfo confirmed neutron star mergers as a primary r-process site.

**演示。** s 过程元素（Sr、Ba、Pb）的质量丰度反映了中子俘获截面乘以恒星通量——具有幻数中子数（50、82、126）的核截面极小，在丰度分布中积聚为 s 过程峰。r 过程峰在丰度分布中位于 s 过程峰以下约 8–10 个质量单位（路径经过更富中子的核，在 r 过程结束后 β 衰变回稳定区）。在千新星 AT2017gfo 中观测到新鲜合成的 r 过程元素（Eu、Au、Pt）证实了中子星并合是主要的 r 过程场所。

**Application.** The B²FH framework explains the cosmic abundance pattern of all elements heavier than hydrogen and helium — "we are all made of stardust" has a quantitative meaning. The nuclear data entering nucleosynthesis calculations (reaction rates, masses far from stability, beta-decay lifetimes) are active frontiers of nuclear physics at facilities such as ISOLDE, RIKEN RIBF, and FRIB.

**应用。** B²FH 框架解释了比氢和氦重的所有元素的宇宙丰度模式——"我们都由星尘构成"有定量意义。进入核合成计算的核数据（反应速率、远离稳定区的质量、β 衰变寿命）是核物理的活跃前沿，在 ISOLDE、RIKEN RIBF 和 FRIB 等装置上开展研究。

---

**Self-test (blank page)**

1. Define the Q-value of a nuclear reaction. For what sign of Q is a threshold kinetic energy required, and why does T_th exceed |Q|?
2. State the Breit–Wigner resonance formula. What is the physical meaning of the width Γ? How does the cross-section behave far from resonance?
3. Write the rotational-band energy spectrum for a deformed even–even nucleus. Why do only even J appear? How does the ratio E(4⁺)/E(2⁺) distinguish rotational from vibrational nuclei?
4. Explain in words why the thermonuclear reaction rate peaks at the Gamow energy E_0, which is between the thermal energy k_B T and the Coulomb barrier height. What happens to E_0 if the temperature doubles?
5. Describe the key difference between the s-process and r-process in nucleosynthesis. What astrophysical sites are associated with each?

**自测（空白页）**

1. 定义核反应的 Q 值。Q 取何符号时需要阈动能？为何 T_th 超过 |Q|？
2. 陈述布雷特–维格纳共振公式。宽度 Γ 的物理意义是什么？截面在远离共振处如何表现？
3. 写出形变偶–偶核的转动带能谱。为何只出现偶数 J？E(4⁺)/E(2⁺) 的比值如何区分转动核与振动核？
4. 用文字解释为何热核反应速率在伽莫夫能量 E_0 处达到峰值，E_0 介于热能 k_B T 与库仑势垒高度之间。若温度加倍，E_0 如何变化？
5. 描述核合成中 s 过程与 r 过程的关键区别。每种过程与哪些天体物理场所相关？

---

← Previous: [Module 9.4 — Plasma Physics](./module-9.4-plasma-physics.md) · [Phase 9 index](./README.md) · Next: [Module 9.6 — Quantum Optics & Laser Physics](./module-9.6-quantum-optics-and-lasers.md) →

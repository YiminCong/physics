# Module 9.5 — Nuclear Reactions & Astrophysics
**模块 9.5 — 核反应与天体物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.5-nuclear-reactions-and-astrophysics-derivations.md)

---

## 1. Nuclear Reaction Kinematics & the Q-Value · 核反应运动学与 Q 值

**Definition.** A two-body nuclear reaction $a + A \to b + B$ is characterized by its **Q-value**, the energy released ($Q > 0$, exothermic) or absorbed ($Q < 0$, endothermic) in the reaction:

$$ Q = (m_a + m_A - m_b - m_B)\, c^2, $$

where masses are nuclear rest masses. In the lab frame ($A$ at rest), the minimum kinetic energy of projectile $a$ needed to make the reaction go (when $Q < 0$) is the **threshold kinetic energy**:

$$ T_\text{th} = -Q\, \frac{m_a + m_A + m_b + m_B}{2 m_A}, $$

which exceeds $|Q|$ because some kinetic energy is unavoidably consumed in the center-of-mass motion. The full derivation appears in the Derivations file.

**定义。** 两体核反应 $a + A \to b + B$ 的特征量是其 **Q 值**——反应释放（$Q > 0$，放热）或吸收（$Q < 0$，吸热）的能量：

$$ Q = (m_a + m_A - m_b - m_B)\, c^2, $$

其中质量为核静止质量。在实验室系（$A$ 静止）中，使反应发生所需的入射粒子 $a$ 的最小动能（当 $Q < 0$ 时）为**阈动能**：

$$ T_\text{th} = -Q\, \frac{m_a + m_A + m_b + m_B}{2 m_A}, $$

它超过 $|Q|$，因为部分动能不可避免地消耗于质心运动。完整推导见推导文件。

**Demonstration.** Consider the reaction $p + {}^7\text{Li} \to {}^4\text{He} + {}^4\text{He}$. The Q-value uses nuclear masses: $Q = (m_p + m({}^7\text{Li}) - 2\, m({}^4\text{He}))c^2 \approx (1.007825 + 7.016003 - 2 \times 4.002602)\ \text{u} \times 931.5\ \text{MeV/u} \approx 17.3$ MeV. Since $Q > 0$ there is no threshold: even a thermal proton (keV) can initiate this reaction once it overcomes the Coulomb barrier (the dominant obstacle at low energies).

**演示。** 考虑反应 $p + {}^7\text{Li} \to {}^4\text{He} + {}^4\text{He}$。Q 值用核质量计算：$Q = (m_p + m({}^7\text{Li}) - 2\, m({}^4\text{He}))c^2 \approx (1.007825 + 7.016003 - 2 \times 4.002602)\ \text{u} \times 931.5\ \text{MeV/u} \approx 17.3$ MeV。因 $Q > 0$，没有阈值：即使是热质子（keV 量级）一旦克服库仑势垒（低能量下的主要障碍）也能引发此反应。

**Application.** Q-values determine whether a reaction is energetically favorable: they set the energy balance in stellar fusion chains (Section 4), in nuclear reactors, and in the production of medical radioisotopes. The threshold formula is used to design accelerator experiments that cannot be performed below a minimum beam energy.

**应用。** Q 值决定反应在能量上是否可行：它们设定恒星聚变链（第 4 节）、核反应堆及医用放射性同位素生产中的能量平衡。阈值公式用于设计不能低于最低束能运行的加速器实验。

---

## 2. Nuclear Cross-Sections: Compound Nucleus vs Direct Reactions · 核截面：复合核与直接反应

**Definition.** The **cross-section** $\sigma(E)$ quantifies the probability of a nuclear reaction: $dN_\text{reactions}/dt = \sigma\, n_\text{target}\, v_\text{rel}$ per projectile, with $\sigma$ having units of area ($\text{barn} = 10^{-28}\ \text{m}^2$). Two qualitatively different mechanisms operate:

**Compound-nucleus (Breit–Wigner) reactions.** At certain resonance energies $E_r$, the projectile is captured to form a long-lived intermediate nucleus that subsequently decays. The resonance cross-section is given by the **Breit–Wigner formula**:

$$ \sigma(E) = \sigma_r\, \frac{\Gamma^2}{(E - E_r)^2 + \Gamma^2/4}, $$

where $\sigma_r = \pi \bar{\lambda}^2 (2J_r + 1)/[(2J_a + 1)(2J_A + 1)]$ is the peak cross-section at resonance ($\bar{\lambda} = \hbar/p$ the reduced de Broglie wavelength), and **$\Gamma$ is the total width** (related to the resonance lifetime by $\Gamma = \hbar/\tau$). The full derivation from the S-matrix is in the Derivations file.

**Direct reactions.** At higher energies (or with loosely bound projectiles), the reaction involves only a few nucleons — a nucleon is stripped (stripping reaction) or picked up (pick-up reaction) in a single fast encounter ($t \sim 10^{-22}$ s vs $10^{-16}$ s for the compound nucleus). Cross-sections vary smoothly with energy and can be factored into a spectroscopic factor times a single-particle cross-section.

**定义。** **截面** $\sigma(E)$ 量化核反应的概率：$dN_\text{reactions}/dt = \sigma\, n_\text{target}\, v_\text{rel}$（每入射粒子），$\sigma$ 的单位为面积（靶 $= 10^{-28}\ \text{m}^2$）。有两种本质上不同的机制：

**复合核（布雷特–维格纳）反应。** 在某些共振能量 $E_r$ 处，入射粒子被俘获形成长寿命的中间核，随后衰变。共振截面由**布雷特–维格纳公式**给出：

$$ \sigma(E) = \sigma_r\, \frac{\Gamma^2}{(E - E_r)^2 + \Gamma^2/4}, $$

其中 $\sigma_r = \pi \bar{\lambda}^2 (2J_r + 1)/[(2J_a + 1)(2J_A + 1)]$ 是共振峰值截面（$\bar{\lambda} = \hbar/p$ 为约化德布罗意波长），**$\Gamma$ 为总宽度**（通过 $\Gamma = \hbar/\tau$ 与共振寿命相关）。从 S 矩阵出发的完整推导见推导文件。

**直接反应。** 在较高能量（或使用松散束缚的入射粒子）时，反应仅涉及少数核子——在一次快速相遇中剥离（剥离反应）或拾取（拾取反应）一个核子（$t \sim 10^{-22}$ s，对比复合核的 $10^{-16}$ s）。截面随能量平滑变化，可分解为谱因子乘以单粒子截面。

**Demonstration.** Neutron absorption in ${}^{238}\text{U}$ displays famous low-energy resonances (the first at $E_r \approx 6.67$ eV, $\Gamma \approx 0.027$ eV) that dominate the cross-section there. The peak value $\sigma_r \sim 10^4$ barn is some $10^5$ times larger than the geometrical cross-section $\pi R^2 \sim 0.17$ barn, a direct consequence of the de Broglie wavelength $\bar{\lambda} \gg R$ at such low energies.

**演示。** ${}^{238}\text{U}$ 中的中子吸收在低能区呈现著名的共振（第一个共振在 $E_r \approx 6.67$ eV，$\Gamma \approx 0.027$ eV），主导该能区的截面。峰值 $\sigma_r \sim 10^4$ 靶远大于几何截面 $\pi R^2 \sim 0.17$ 靶约 $10^5$ 倍，这是该低能量下德布罗意波长 $\bar{\lambda} \gg R$ 的直接结果。

**Application.** Breit–Wigner resonances are used to engineer reactor moderators and shielding materials (by matching neutron energies to absorption resonances), and are the mechanism behind the Mössbauer effect. Direct reactions (such as (d, p) stripping) are precision spectroscopic tools that measure the single-particle occupancy of nuclear levels — directly probing the shell structure of Module 9.3.

**应用。** 布雷特–维格纳共振用于设计反应堆慢化剂和屏蔽材料（通过使中子能量与吸收共振匹配），也是穆斯堡尔效应背后的机制。直接反应（如 (d, p) 剥离反应）是精密谱学工具，测量核能级的单粒子占据——直接探测模块 9.3 的壳层结构。

---

## 3. Beyond the Shell Model: Collective Nuclear Structure · 超越壳层模型：集体核结构

**Definition.** The shell model (Module 9.3) works well near closed shells. Away from them, nuclei are **deformed** and exhibit collective motions of many nucleons acting together: rotations and vibrations of the nuclear shape.

**Rotational bands.** A deformed nucleus with moment of inertia $\mathcal{I}$ rotates as a quantum symmetric top. Angular momentum is quantized in integer steps, and the spectrum of a **ground-state rotational band** is:

$$ E_J = \frac{\hbar^2 J(J+1)}{2\mathcal{I}}, \quad J = 0, 2, 4, 6, \ldots \ \text{(for even–even nuclei)}, $$

where only even $J$ appear because of the left–right symmetry of the nuclear shape. The derivation from the rigid-rotor Hamiltonian is in the Derivations file.

**Vibrational states.** Near a spherical equilibrium the nuclear surface vibrates at a set of normal-mode frequencies $\omega_\lambda$ (multipole vibrations: $\lambda = 2$ quadrupole, $\lambda = 3$ octupole, …). Each mode is quantized as a harmonic oscillator, with phonon excitations at energies $\hbar\omega_\lambda, 2\hbar\omega_\lambda, \ldots$ The **collective model** (Bohr–Mottelson) unifies rotation and vibration in a single Hamiltonian for the surface shape variables $\alpha_{\lambda\mu}$.

**定义。** 壳层模型（模块 9.3）在闭壳层附近运行良好。远离闭壳层时，核是**形变的**，表现出许多核子共同运动的集体运动：核形状的转动和振动。

**转动带。** 具有转动惯量 $\mathcal{I}$ 的形变核像量子对称陀螺一样转动。角动量以整数步量子化，**基态转动带**的谱为：

$$ E_J = \frac{\hbar^2 J(J+1)}{2\mathcal{I}}, \quad J = 0, 2, 4, 6, \ldots\ \text{（对偶–偶核）}, $$

由于核形状的左右对称性，仅出现偶数 $J$。从刚性转子哈密顿量出发的推导见推导文件。

**振动态。** 在球形平衡附近，核表面以一组本征频率 $\omega_\lambda$ 振动（多极振动：$\lambda = 2$ 四极，$\lambda = 3$ 八极，……）。每种模式像谐振子一样量子化，声子激发能量为 $\hbar\omega_\lambda, 2\hbar\omega_\lambda, \ldots$ **集体模型**（玻尔–莫特尔森）将转动和振动统一在关于核表面形状变量 $\alpha_{\lambda\mu}$ 的单一哈密顿量中。

**Demonstration.** In ${}^{152}\text{Sm}$ (a rare-earth nucleus well away from closed shells), the observed $2^+$ level is at 121.8 keV and the $4^+$ level at 366.5 keV. The rigid-rotor formula predicts $E(4^+)/E(2^+) = [4\cdot 5]/[2\cdot 3] = 10/3 = 3.33$. The measured ratio is $366.5/121.8 \approx 3.01$, close to the rotational limit (deviations signal the non-rigidity of the nucleus). Compare ${}^{52}\text{Cr}$ near a closed shell: $E(4^+)/E(2^+) \approx 2.1$, close to the vibrational limit of 2.

**演示。** 在 ${}^{152}\text{Sm}$（远离闭壳层的稀土核）中，观测到的 $2^+$ 能级在 121.8 keV，$4^+$ 能级在 366.5 keV。刚性转子公式预测 $E(4^+)/E(2^+) = [4\cdot 5]/[2\cdot 3] = 10/3 = 3.33$。实测比值为 $366.5/121.8 \approx 3.01$，接近转动极限（偏差表征核的非刚性）。对比靠近闭壳层的 ${}^{52}\text{Cr}$：$E(4^+)/E(2^+) \approx 2.1$，接近振动极限 2。

**Application.** Rotational and vibrational spectra are measured by gamma-ray spectroscopy following nuclear reactions. The collective model is essential for understanding the giant dipole resonance (a collective oscillation of all protons against all neutrons), nuclear fission dynamics (deformation path to the saddle point), and octupole correlations near the atomic number $Z = 88$ relevant to searches for a permanent atomic electric dipole moment.

**应用。** 转动和振动谱通过核反应后的 $\gamma$ 射线谱学测量。集体模型对于理解巨偶极共振（所有质子相对所有中子的集体振荡）、核裂变动力学（向鞍点的形变路径）以及与寻找永久原子电偶极矩相关的 $Z = 88$ 附近的八极关联至关重要。

---

## 4. Stellar Fusion: the p–p Chain and the CNO Cycle · 恒星聚变：pp 链与 CNO 循环

**Definition.** Stars generate energy by fusing hydrogen to helium. In the **proton–proton (p–p) chain** (dominant in stars with core temperature $T < \sim 1.5 \times 10^7$ K, including the Sun):

$$ \begin{aligned}
&p + p \to {}^2\text{H} + e^+ + \nu_e &&\text{(weak interaction, very slow; rate-limiting step)} \\
&p + {}^2\text{H} \to {}^3\text{He} + \gamma \\
&{}^3\text{He} + {}^3\text{He} \to {}^4\text{He} + 2p
\end{aligned} $$

Net: $4p \to {}^4\text{He} + 2e^+ + 2\nu_e + 2\gamma$, $Q_\text{net} \approx 26.7$ MeV (after subtracting annihilation energy).

In the **CNO cycle** (dominant for $T > 1.5 \times 10^7$ K, as in massive stars), carbon, nitrogen, and oxygen nuclei act as catalysts, and the net reaction is also $4p \to {}^4\text{He} + 2e^+ + 2\nu_e$ but with different temperature dependence (rate $\propto T^{20}$ vs $T^4$ for pp). The CNO cycle is responsible for most of the Sun's energy production in the core where $T$ is highest, and dominates in stars more than $1.3\, M_\odot$.

**定义。** 恒星通过将氢聚变为氦来产生能量。在**质子–质子（pp）链**中（在核温度 $T < \sim 1.5 \times 10^7$ K 的恒星，包括太阳中占主导地位）：

$$ \begin{aligned}
&p + p \to {}^2\text{H} + e^+ + \nu_e &&\text{（弱相互作用，极慢；限速步骤）} \\
&p + {}^2\text{H} \to {}^3\text{He} + \gamma \\
&{}^3\text{He} + {}^3\text{He} \to {}^4\text{He} + 2p
\end{aligned} $$

净反应：$4p \to {}^4\text{He} + 2e^+ + 2\nu_e + 2\gamma$，$Q_\text{net} \approx 26.7$ MeV（减去湮没能量后）。

在 **CNO 循环**中（在 $T > 1.5 \times 10^7$ K 时占主导地位，如大质量恒星），碳、氮、氧核作为催化剂，净反应也是 $4p \to {}^4\text{He} + 2e^+ + 2\nu_e$，但温度依赖性不同（速率 $\propto T^{20}$，对比 pp 链的 $T^4$）。CNO 循环负责太阳核心温度最高处的大部分能量产生，并在质量超过 $1.3\, M_\odot$ 的恒星中占主导地位。

**Demonstration.** The Sun luminosity $L_\odot \approx 3.85 \times 10^{26}$ W and the energy per pp-chain completion $Q \approx 26.7\ \text{MeV} \approx 4.28 \times 10^{-12}$ J imply a reaction rate of $L_\odot/Q \approx 9 \times 10^{37}\ \text{s}^{-1}$. Each cycle converts 4 proton masses to one alpha particle plus energy; the mass deficit per cycle is $\approx 0.7\%$ of the input mass. The Sun converts $\approx 4.3 \times 10^9$ kg of mass to energy every second. Solar neutrinos (2 per pp completion) carry away $\approx 2\%$ of the energy and have been detected at Kamiokande, SNO, and Borexino — directly confirming the pp chain is the Sun's energy source.

**演示。** 太阳光度 $L_\odot \approx 3.85 \times 10^{26}$ W 和每次 pp 链完成的能量 $Q \approx 26.7\ \text{MeV} \approx 4.28 \times 10^{-12}$ J 意味着反应速率为 $L_\odot/Q \approx 9 \times 10^{37}\ \text{s}^{-1}$。每个循环将 4 个质子质量转化为一个 $\alpha$ 粒子加能量；每个循环的质量亏损约为输入质量的 0.7%。太阳每秒将约 $4.3 \times 10^9$ kg 质量转化为能量。太阳中微子（每次 pp 完成产生 2 个）携带约 2% 的能量，已在神冈、SNO 和 Borexino 探测到——直接证实了 pp 链是太阳的能量来源。

**Application.** The pp chain rate is calibrated to the solar neutrino flux (the "solar neutrino problem" led to the discovery of neutrino oscillations — Module 8.5 context). CNO-cycle measurement in the Sun's core (recent Borexino data) constrains the solar metallicity. The temperature dependence of these cycles determines the main-sequence lifetime of stars and their evolutionary tracks in the Hertzsprung–Russell diagram.

**应用。** pp 链速率通过太阳中微子通量校准（"太阳中微子问题"导致发现了中微子振荡——模块 8.5 背景）。太阳核心 CNO 循环的测量（近期 Borexino 数据）限制了太阳金属度。这些循环的温度依赖性决定主序星的寿命及其在赫罗图中的演化轨迹。

---

## 5. The Gamow Peak & Thermonuclear Reaction Rates · 伽莫夫峰与热核反应速率

**Definition.** The **thermonuclear reaction rate** per pair of fusing nuclei at temperature $T$ is the thermal average:

$$ \langle\sigma v\rangle = \int_0^\infty \sigma(E)\, v\, f(E)\, dE, $$

where $f(E)$ is the Maxwell–Boltzmann energy distribution $\propto E^{1/2} \exp(-E/k_B T)$ (the thermal tail). The cross-section for charged-particle fusion vanishes exponentially at low energies because of Coulomb tunnelling (derived in Module 9.3 — the Gamow factor):

$$ \sigma(E) \propto \frac{1}{E} \exp(-2\pi\eta), \quad \text{with } \eta = \frac{Z_a Z_A e^2}{\hbar v} = Z_a Z_A \alpha \sqrt{\frac{\mu c^2}{2E}}, $$

where $\mu$ is the reduced mass. The product of the decreasing MB tail and the increasing tunnelling factor peaks sharply at the **Gamow peak energy**:

$$ \begin{aligned}
E_0 &= \frac{\left(\pi \alpha Z_a Z_A \sqrt{\mu c^2/2}\, k_B T\right)^{2/3}}{2^{1/3}} \\
E_0 &\approx 1.22 \left(Z_a^2 Z_A^2 \frac{\mu}{m_u}\right)^{1/3} \left(\frac{T}{10^7\ \text{K}}\right)^{2/3}\ \text{keV},
\end{aligned} $$

with a width $\Delta \propto E_0^{1/2} (k_B T)^{1/2}$. The full derivation is in the Derivations file.

**定义。** 温度 $T$ 下每对聚变核的**热核反应速率**是热平均：

$$ \langle\sigma v\rangle = \int_0^\infty \sigma(E)\, v\, f(E)\, dE, $$

其中 $f(E)$ 是麦克斯韦–玻尔兹曼能量分布 $\propto E^{1/2} \exp(-E/k_B T)$（热尾）。带电粒子聚变的截面在低能量处因库仑隧穿而指数衰减（在模块 9.3 中推导——伽莫夫因子）：

$$ \sigma(E) \propto \frac{1}{E} \exp(-2\pi\eta), \quad \text{其中 } \eta = \frac{Z_a Z_A e^2}{\hbar v} = Z_a Z_A \alpha \sqrt{\frac{\mu c^2}{2E}}, $$

$\mu$ 为约化质量。MB 尾（递减）与隧穿因子（递增）的乘积在**伽莫夫峰能量**处急剧达到峰值：

$$ \begin{aligned}
E_0 &= \frac{\left(\pi \alpha Z_a Z_A \sqrt{\mu c^2/2}\, k_B T\right)^{2/3}}{2^{1/3}} \\
E_0 &\approx 1.22 \left(Z_a^2 Z_A^2 \frac{\mu}{m_u}\right)^{1/3} \left(\frac{T}{10^7\ \text{K}}\right)^{2/3}\ \text{keV},
\end{aligned} $$

宽度 $\Delta \propto E_0^{1/2} (k_B T)^{1/2}$。完整推导见推导文件。

**Demonstration.** For p + p fusion at the solar core temperature $T_c \approx 1.57 \times 10^7$ K: the thermal energy $k_B T \approx 1.35$ keV, but $E_0 \approx 6$ keV. The reaction occurs in a narrow window far above the thermal peak. The probability is dominated by the factor $\exp(-2\pi\eta) \approx \exp(-31) \sim 10^{-13}$ — which is why the pp rate is extremely slow (each proton fuses on a timescale of $\sim 10^{10}$ years) and the Sun is long-lived.

**演示。** 对于太阳核心温度 $T_c \approx 1.57 \times 10^7$ K 下的 p + p 聚变：热能 $k_B T \approx 1.35$ keV，但 $E_0 \approx 6$ keV。反应发生在远高于热峰的狭窄窗口内。概率由因子 $\exp(-2\pi\eta) \approx \exp(-31) \sim 10^{-13}$ 主导——这就是 pp 速率极慢（每个质子聚变的时间尺度约 $10^{10}$ 年）以及太阳寿命长的原因。

**Application.** The Gamow peak governs all thermonuclear reaction rates. It is the reason stellar burning temperatures are so high: stars must reach $T \sim 10^7\text{–}10^9$ K to achieve measurable Gamow-peak tunnelling rates. When a Breit–Wigner resonance (Section 2) falls inside the Gamow window, the stellar rate is hugely enhanced — a **stellar resonance**. The famous 7.65 MeV $3^+$ state in ${}^{12}\text{C}$ (predicted by Hoyle and found experimentally) is one such resonance, making carbon synthesis possible (Section 6).

**应用。** 伽莫夫峰支配所有热核反应速率。它是恒星燃烧温度如此之高的原因：恒星必须达到 $T \sim 10^7\text{–}10^9$ K 才能实现可测量的伽莫夫峰隧穿速率。当布雷特–维格纳共振（第 2 节）落在伽莫夫窗口内时，恒星速率被大幅增强——**恒星共振**。${}^{12}\text{C}$ 中著名的 7.65 MeV $3^+$ 态（由霍伊尔预言并由实验发现）就是这样一个共振态，使碳合成成为可能（第 6 节）。

---

## 6. The Triple-Alpha Process & Nucleosynthesis · 三 $\alpha$ 过程与核合成

**Definition.** When core hydrogen is exhausted, stars contract, heat up, and begin **helium burning** via the **triple-alpha process**:

$$ \begin{aligned}
&{}^4\text{He} + {}^4\text{He} \leftrightarrow {}^8\text{Be}^* &&\text{(resonance, } T_{1/2} = 8.2 \times 10^{-17}\ \text{s — quasi-equilibrium)}, \\
&{}^8\text{Be}^* + {}^4\text{He} \to {}^{12}\text{C}^* \ (7.65\ \text{MeV } 0^+_2\ \text{Hoyle state}) \to {}^{12}\text{C} + 2\gamma,
\end{aligned} $$

with $Q \approx 7.27$ MeV. The Hoyle state, nearly resonant with the three-alpha threshold, makes this rate $\sim 10^{26}$ times faster than without it — Hoyle's 1954 prediction of its existence, confirmed experimentally by Cook et al., is one of the great predictions in nuclear astrophysics.

**Nucleosynthesis of the elements** was codified by Burbidge, Burbidge, Fowler & Hoyle ($\text{B}^2\text{FH}$, 1957):

- **s-process (slow neutron capture):** Neutrons are captured on timescales much longer than beta-decay lifetimes, so the nucleus has time to beta-decay to the stability valley after each capture. The reaction path closely follows the valley of stability. Occurs in AGB stars, producing elements up to Bi ($A \approx 209$).
- **r-process (rapid neutron capture):** Neutron fluxes are so intense that many successive captures occur before any beta decay. The reaction path runs far from stability, toward very neutron-rich nuclei, and terminates when nuclei become unstable to fission. Requires extreme environments: neutron star mergers (confirmed by kilonova GW170817) and core-collapse supernovae. Produces $\sim$half of all nuclei heavier than iron, including gold, platinum, and uranium.

**定义。** 当核心氢耗尽时，恒星收缩、升温，并通过**三 $\alpha$ 过程**开始**氦燃烧**：

$$ \begin{aligned}
&{}^4\text{He} + {}^4\text{He} \leftrightarrow {}^8\text{Be}^* &&\text{（共振，} T_{1/2} = 8.2 \times 10^{-17}\ \text{s——准平衡）}, \\
&{}^8\text{Be}^* + {}^4\text{He} \to {}^{12}\text{C}^* \ (7.65\ \text{MeV } 0^+_2\ \text{霍伊尔态}) \to {}^{12}\text{C} + 2\gamma,
\end{aligned} $$

$Q \approx 7.27$ MeV。霍伊尔态与三 $\alpha$ 阈值几乎共振，使此速率比没有它时快约 $10^{26}$ 倍——霍伊尔 1954 年对其存在的预言，由库克等人通过实验证实，是核天体物理中最伟大的预言之一。

**元素核合成**由伯比奇、伯比奇、福勒和霍伊尔（$\text{B}^2\text{FH}$，1957 年）系统化：

- **s 过程（慢中子俘获）：** 中子俘获的时间尺度远长于 $\beta$ 衰变寿命，因此核在每次俘获后有时间 $\beta$ 衰变到稳定性谷。反应路径紧随稳定性谷。发生在 AGB 星中，产生直至 Bi（$A \approx 209$）的元素。
- **r 过程（快中子俘获）：** 中子通量如此之强，以至于在任何 $\beta$ 衰变之前就发生了许多连续俘获。反应路径偏离稳定区很远，走向极富中子的核，并在核对裂变不稳定时终止。需要极端环境：中子星并合（由千新星 GW170817 证实）和核塌缩超新星。产生铁以上约一半的所有核，包括金、铂和铀。

**Demonstration.** The mass abundances of the s-process elements (Sr, Ba, Pb) reflect the neutron-capture cross-section times the stellar flux — nuclei with magic neutron numbers (50, 82, 126) have very small cross-sections and pile up as s-process peaks in the abundance distribution. The r-process peaks are displaced by $\sim 8\text{–}10$ mass units below the s-process peaks (the path runs through more neutron-rich nuclei that beta-decay back toward stability after the r-process). Observation of freshly synthesized r-process elements (Eu, Au, Pt) in the kilonova AT2017gfo confirmed neutron star mergers as a primary r-process site.

**演示。** s 过程元素（Sr、Ba、Pb）的质量丰度反映了中子俘获截面乘以恒星通量——具有幻数中子数（50、82、126）的核截面极小，在丰度分布中积聚为 s 过程峰。r 过程峰在丰度分布中位于 s 过程峰以下约 8–10 个质量单位（路径经过更富中子的核，在 r 过程结束后 $\beta$ 衰变回稳定区）。在千新星 AT2017gfo 中观测到新鲜合成的 r 过程元素（Eu、Au、Pt）证实了中子星并合是主要的 r 过程场所。

**Application.** The $\text{B}^2\text{FH}$ framework explains the cosmic abundance pattern of all elements heavier than hydrogen and helium — "we are all made of stardust" has a quantitative meaning. The nuclear data entering nucleosynthesis calculations (reaction rates, masses far from stability, beta-decay lifetimes) are active frontiers of nuclear physics at facilities such as ISOLDE, RIKEN RIBF, and FRIB.

**应用。** $\text{B}^2\text{FH}$ 框架解释了比氢和氦重的所有元素的宇宙丰度模式——"我们都由星尘构成"有定量意义。进入核合成计算的核数据（反应速率、远离稳定区的质量、$\beta$ 衰变寿命）是核物理的活跃前沿，在 ISOLDE、RIKEN RIBF 和 FRIB 等装置上开展研究。

## Key results · 核心结果

- Q-value $=(m_i-m_f)c^2$; endothermic ($Q<0$) needs a threshold · 反应 Q 值与阈能
- Breit–Wigner resonance, width $\Gamma=\hbar/\tau$ · 布雷特–维格纳共振
- Rotational band $E_J=\hbar^2 J(J+1)/2I$ · 转动能带
- Gamow peak $E_0$ between $k_BT$ and the Coulomb barrier · 伽莫夫峰

---

**Self-test (blank page)**

1. Define the Q-value of a nuclear reaction. For what sign of $Q$ is a threshold kinetic energy required, and why does $T_\text{th}$ exceed $|Q|$?
2. State the Breit–Wigner resonance formula. What is the physical meaning of the width $\Gamma$? How does the cross-section behave far from resonance?
3. Write the rotational-band energy spectrum for a deformed even–even nucleus. Why do only even $J$ appear? How does the ratio $E(4^+)/E(2^+)$ distinguish rotational from vibrational nuclei?
4. Explain in words why the thermonuclear reaction rate peaks at the Gamow energy $E_0$, which is between the thermal energy $k_B T$ and the Coulomb barrier height. What happens to $E_0$ if the temperature doubles?
5. Describe the key difference between the s-process and r-process in nucleosynthesis. What astrophysical sites are associated with each?

**自测（空白页）**

1. 定义核反应的 Q 值。$Q$ 取何符号时需要阈动能？为何 $T_\text{th}$ 超过 $|Q|$？
2. 陈述布雷特–维格纳共振公式。宽度 $\Gamma$ 的物理意义是什么？截面在远离共振处如何表现？
3. 写出形变偶–偶核的转动带能谱。为何只出现偶数 $J$？$E(4^+)/E(2^+)$ 的比值如何区分转动核与振动核？
4. 用文字解释为何热核反应速率在伽莫夫能量 $E_0$ 处达到峰值，$E_0$ 介于热能 $k_B T$ 与库仑势垒高度之间。若温度加倍，$E_0$ 如何变化？
5. 描述核合成中 s 过程与 r 过程的关键区别。每种过程与哪些天体物理场所相关？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $Q=(m_i-m_f)c^2$ = energy released; $Q<0$ (endothermic) requires a threshold, and $T_\text{th}>|Q|$ because momentum conservation reserves some kinetic energy for centre-of-mass motion: $T_\text{th}=|Q|(1+m/M)$. · 吸热反应需阈能,$T_\text{th}>|Q|$。
**2.** Breit–Wigner $\sigma\propto\Gamma^2/[(E-E_R)^2+\Gamma^2/4]$; $\Gamma=\hbar/\tau$ is the resonance width (inverse lifetime). Far off resonance $\sigma\sim1/(E-E_R)^2$. · 共振宽度;远离共振 $1/(E-E_R)^2$。
**3.** $E_J=\hbar^2 J(J+1)/2I$; only even $J$ for even–even nuclei (reflection/$K=0$ symmetry). $E(4^+)/E(2^+)=10/3\approx3.33$ for a rigid rotor vs $\approx2$ for a vibrator. · 转动能带;比值区分转动与振动核。
**4.** The rate is the product of the falling Maxwell–Boltzmann tail $e^{-E/k_BT}$ and the rising tunneling factor $e^{-\sqrt{E_G/E}}$; their product peaks at the Gamow energy $E_0$ between $k_BT$ and the barrier. Doubling $T$ raises $E_0$ ($E_0\propto T^{2/3}$). · 伽莫夫峰为两因子乘积的极大;$E_0\propto T^{2/3}$。

</details>

---

← Previous: [Module 9.4 — Plasma Physics](./module-9.4-plasma-physics.md) · [Phase 9 index](./README.md) · Next: [Module 9.6 — Quantum Optics & Laser Physics](./module-9.6-quantum-optics-and-lasers.md) →

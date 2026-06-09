# Module 8.6 — Particle Physics & Cosmology
**模块 8.6 — 粒子物理与宇宙学**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.6-derivations.md)

---

## 1. The Hot Early Universe as a Particle-Physics Laboratory · 早期热宇宙作为粒子物理实验室

**Definition.** In the hot Big Bang, the temperature of the universe decreases as $T \propto 1/a(t)$ (where $a(t)$ is the scale factor, Module 7.6). At early times, $T$ is high enough that thermal energies $k_B T$ exceed the rest-mass thresholds of successively heavier particles, so all Standard Model particles are produced in thermal equilibrium. The history of the universe is therefore a sequence of **phase transitions** and **freeze-outs**: at $T \sim 100$ GeV the electroweak symmetry is broken (the Higgs transition); at $T \sim 150$ MeV quarks and gluons condense into hadrons (**QCD confinement transition**, quark-gluon plasma to hadron gas); at $T \sim 1$ MeV neutrinos decouple and Big Bang nucleosynthesis (BBN) begins, fusing protons and neutrons into light nuclei ($^4$He, D, Li) in proportions that depend sensitively on the baryon-to-photon ratio $\eta \approx 6 \times 10^{-10}$.

**定义。** 在热大爆炸中，宇宙温度随标度因子变化为 $T \propto 1/a(t)$（其中 $a(t)$ 为标度因子，模块 7.6）。在早期，$T$ 足够高，热能 $k_B T$ 超过了越来越重的粒子的静止质量阈值，因此所有标准模型粒子都在热平衡中被产生。宇宙的历史因此是一系列**相变**和**冻结**的过程：在 $T \sim 100$ GeV 时电弱对称性破缺（希格斯相变）；在 $T \sim 150$ MeV 时夸克和胶子凝聚为强子（**量子色动力学禁闭相变**，夸克–胶子等离子体转变为强子气体）；在 $T \sim 1$ MeV 时中微子退耦，大爆炸核合成（BBN）开始，质子和中子聚变为轻核（$^4$He、D、Li），其比例对重子–光子比 $\eta \approx 6 \times 10^{-10}$ 极为敏感。

**Demonstration.** The **Boltzmann equation** for a species with number density $n$ in an expanding universe is $dn/dt + 3Hn = -\langle\sigma v\rangle(n^2 - n_\text{eq}^2)$, where $H$ is the Hubble rate and $\langle\sigma v\rangle$ is the thermally averaged annihilation cross-section. When $\langle\sigma v\rangle n < H$ (the interaction rate falls below the expansion rate), the species **freezes out** and its comoving number density is fixed. For relativistic species (neutrinos, photons) this occurs early; for non-relativistic massive particles (dark matter candidates, heavy baryons) it occurs later. The relic abundance of a thermal dark matter particle (a WIMP) is $\Omega_\text{DM} h^2 \approx 0.1\text{ pb}/\langle\sigma v\rangle$ — remarkably close to the observed $\Omega_\text{DM} \approx 0.26$ for weak-scale cross-sections $\sim 1$ pb, the **WIMP miracle**.

**演示。** 在膨胀宇宙中，数密度为 $n$ 的粒子种类的**玻尔兹曼方程**为 $dn/dt + 3Hn = -\langle\sigma v\rangle(n^2 - n_\text{eq}^2)$，其中 $H$ 为哈勃速率，$\langle\sigma v\rangle$ 为热平均湮灭截面。当 $\langle\sigma v\rangle n < H$（相互作用速率低于膨胀速率）时，该物种**冻结**，其共动数密度固定。对于相对论性物种（中微子、光子），这发生得较早；对于非相对论性的大质量粒子（暗物质候选者、重重子），这发生得较晚。热暗物质粒子（WIMP）的遗迹丰度为 $\Omega_\text{DM} h^2 \approx 0.1\text{ pb}/\langle\sigma v\rangle$——对于弱力尺度的截面 $\sim 1$ pb，这与观测到的 $\Omega_\text{DM} \approx 0.26$ 惊人地接近，即**WIMP 奇迹**。

**Application.** BBN is one of the most powerful probes of early-universe physics: the predicted $^4$He mass fraction $Y_p \approx 0.247$ and $\text{D/H} \approx 2.5 \times 10^{-5}$ match observations to percent-level accuracy, confirming the Standard Model at temperatures up to $\sim 10$ MeV. Deviations would signal new light particles contributing to the effective number of relativistic degrees of freedom $g_*(T)$. The QCD transition, although a crossover rather than a sharp phase transition at $\mu_B \approx 0$, is reproduced by heavy-ion collisions at RHIC and the LHC, which create quark-gluon plasma at $T \sim 300$ MeV.

**应用。** 大爆炸核合成是探测早期宇宙物理最有力的手段之一：预言的 $^4$He 质量分数 $Y_p \approx 0.247$ 以及 $\text{D/H} \approx 2.5 \times 10^{-5}$ 与观测值的符合精度达百分之几，在高达 $\sim 10$ MeV 的温度下确认了标准模型。偏差将预示有新的轻粒子对有效相对论性自由度数 $g_*(T)$ 作出贡献。量子色动力学相变在 $\mu_B \approx 0$ 处是一个连续过渡而非尖锐相变，RHIC 和大型强子对撞机的重离子碰撞在 $T \sim 300$ MeV 下重现了夸克–胶子等离子体。

---

## 2. Baryogenesis, Dark Matter, and Inflation · 重子生成、暗物质与暴胀

**Definition.** The observed universe contains matter but negligible antimatter — a baryon asymmetry $\eta \equiv (n_b - n_{\bar b})/n_\gamma \approx 6 \times 10^{-10}$. Sakharov (1967) identified three necessary conditions for generating this asymmetry dynamically: (1) **baryon number violation**, (2) **C and CP violation**, (3) departure from **thermal equilibrium**. The Standard Model satisfies all three in principle (baryon violation via electroweak sphalerons, CP violation via the CKM phase, and the electroweak phase transition) but quantitatively falls short. **Leptogenesis** offers an attractive extension: heavy right-handed neutrinos (seesaw mechanism, Module 8.5) decay out of equilibrium with CP-violating rates, generating a lepton asymmetry that is converted to a baryon asymmetry by sphalerons. **Dark matter** makes up 27% of the total energy density. Leading candidates are: WIMPs (weakly interacting massive particles with $m \sim 100$ GeV, motivated by the WIMP miracle), **axions** (light pseudoscalar particles introduced to solve the strong CP problem — why $\theta_\text{QCD} \lesssim 10^{-10}$), and sterile neutrinos. **Inflation** (a period of accelerated expansion at $T \gtrsim 10^{15}$ GeV) solves the horizon and flatness problems (Module 7.6) and generates the primordial density perturbations ($\delta\rho/\rho \sim 10^{-5}$) that seed all large-scale structure; it requires a scalar field (inflaton) whose particle-physics identity remains unknown.

**定义。** 观测到的宇宙含有物质但几乎没有反物质——重子不对称性 $\eta \equiv (n_b - n_{\bar b})/n_\gamma \approx 6 \times 10^{-10}$。萨哈罗夫（1967 年）指出动态产生这一不对称性的三个必要条件：（1）**重子数不守恒**，（2）**C 和 CP 破坏**，（3）偏离**热平衡**。标准模型原则上满足所有三个条件（通过电弱热子实现重子数破坏，通过 CKM 相位实现 CP 破坏，以及电弱相变），但在数量上不足。**轻子生成**提供了一个有吸引力的扩展：重右手中微子（跷跷板机制，模块 8.5）在偏离平衡的状态下以 CP 破坏的速率衰变，产生轻子不对称性，再由热子转化为重子不对称性。**暗物质**占总能量密度的 27%。主要候选者包括：WIMP（弱相互作用大质量粒子，$m \sim 100$ GeV，受 WIMP 奇迹的启示）、**轴子**（为解决强 CP 问题——为何 $\theta_\text{QCD} \lesssim 10^{-10}$——而引入的轻赝标量粒子）以及惰性中微子。**暴胀**（$T \gtrsim 10^{15}$ GeV 时的加速膨胀阶段）解决了视界问题和平坦性问题（模块 7.6），并产生了播种所有大尺度结构的原初密度扰动（$\delta\rho/\rho \sim 10^{-5}$）；它需要一个标量场（暴胀子），其粒子物理本质至今未知。

**Demonstration.** A WIMP of mass $m_\chi \sim 100$ GeV freezes out when $T_f \sim m_\chi/20 \approx 5$ GeV. The Boltzmann equation gives a relic density $\Omega_\chi h^2 \approx (3 \times 10^{-27}\text{ cm}^3\text{ s}^{-1})/\langle\sigma v\rangle$. For $\langle\sigma v\rangle$ set by the weak force ($\sim \alpha^2/m_\chi^2 \sim 10^{-26}\text{ cm}^3\text{ s}^{-1}$), one gets $\Omega_\chi h^2 \approx 0.1$ — in striking agreement with the measured $\Omega_\text{DM} h^2 \approx 0.12$ from CMB data (Planck satellite). The axion mass and coupling are related by $m_a f_a \approx m_\pi f_\pi$, giving $m_a \sim 1\text{–}100\ \mu\text{eV}$ for the cosmologically relevant window; axion dark matter would be detectable by microwave-cavity experiments (e.g., ADMX).

**演示。** 质量为 $m_\chi \sim 100$ GeV 的 WIMP 在 $T_f \sim m_\chi/20 \approx 5$ GeV 时冻结。玻尔兹曼方程给出遗迹密度 $\Omega_\chi h^2 \approx (3 \times 10^{-27}\text{ cm}^3\text{ s}^{-1})/\langle\sigma v\rangle$。对于由弱力决定的 $\langle\sigma v\rangle$（$\sim \alpha^2/m_\chi^2 \sim 10^{-26}\text{ cm}^3\text{ s}^{-1}$），得到 $\Omega_\chi h^2 \approx 0.1$——与来自宇宙微波背景数据（普朗克卫星）的测量值 $\Omega_\text{DM} h^2 \approx 0.12$ 惊人地吻合。轴子质量与耦合常数的关系为 $m_a f_a \approx m_\pi f_\pi$，在宇宙学相关窗口内给出 $m_a \sim 1\text{–}100\ \mu\text{eV}$；轴子暗物质可被微波腔实验（如 ADMX）探测。

**Application.** The connection between the smallest (particle physics) and largest (cosmology, Module 7.6) scales is the frontier of physics: the same Standard Model Lagrangian that describes collider experiments governs the thermal history of the universe, BBN, and the dark matter relic abundance. Open questions — the identity of dark matter, the origin of the baryon asymmetry, the nature of inflation — are simultaneously cosmological and particle-physics problems, and their resolution will almost certainly require physics beyond the Standard Model (Module 8.5). The next generation of experiments (CMB-S4, Euclid, LZ, XENONnT, ADMX, SKA) will probe this frontier on multiple fronts.

**应用。** 最小尺度（粒子物理）与最大尺度（宇宙学，模块 7.6）之间的联系是物理学的前沿：同一个描述对撞机实验的标准模型拉格朗日量，支配着宇宙的热演化历史、大爆炸核合成以及暗物质遗迹丰度。未解之谜——暗物质的本质、重子不对称性的起源、暴胀的性质——既是宇宙学问题，也是粒子物理问题，它们的解答几乎必然需要超越标准模型的物理（模块 8.5）。下一代实验（CMB-S4、欧几里得卫星、LZ、XENONnT、ADMX、SKA）将从多个方向探测这一前沿。

---

## Self-test (blank page)

1. State Sakharov's three conditions for baryogenesis and explain which ingredient of the Standard Model satisfies each. Why is the Standard Model electroweak baryogenesis insufficient?
2. Derive the WIMP miracle estimate: why does a particle with weak-scale interactions naturally produce $\Omega_\text{DM} \approx 0.26$? What makes the axion a qualitatively different dark matter candidate?
3. How does BBN provide a particle-physics test of the early universe? What would an extra light neutrino species do to the predicted $^4$He abundance?

**自测（空白页）**

1. 陈述萨哈罗夫的三个重子生成条件，并解释标准模型的哪个成分满足每个条件。为何标准模型的电弱重子生成不足以解释观测？
2. 推导 WIMP 奇迹估算：为何具有弱力尺度相互作用的粒子自然地产生 $\Omega_\text{DM} \approx 0.26$？轴子作为暗物质候选者在质上有何不同？
3. 大爆炸核合成如何提供对早期宇宙的粒子物理检验？一种额外的轻中微子物种对预言的 $^4$He 丰度有何影响？

---

← Previous: [Module 8.5 — The Standard Model & Beyond](./module-8.5-standard-model-and-beyond.md) · [Phase 8 index](./README.md) · Next: [Module 8.7 — Parity Violation & the Weak Interaction (Lee–Yang)](./module-8.7-parity-violation-and-the-weak-interaction.md) →

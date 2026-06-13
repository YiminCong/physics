# Module 8.10 — Neutrino Physics & Experimental Particle Physics
**模块 8.10 — 中微子物理与实验粒子物理**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.10-neutrino-physics-and-experiment-derivations.md)

---

## 1. Neutrino Oscillations & Mass · 中微子振荡与质量

**Definition.** The Standard Model originally assumed neutrinos to be **massless**, one for each lepton generation: the electron neutrino $\nu_e$, the muon neutrino $\nu_\mu$, and the tau neutrino $\nu_\tau$. These are the **flavor eigenstates** — the states that couple to $W$ bosons in charged-current weak interactions. If neutrinos have mass, these flavor eigenstates are **not** the same as the **mass eigenstates** $\nu_1, \nu_2, \nu_3$ (states with definite masses $m_1, m_2, m_3$). The two bases are related by the **Pontecorvo–Maki–Nakagawa–Sakata (PMNS) mixing matrix** $U$:

$$ |\nu_\alpha\rangle = \sum_i U^*_{\alpha i}\, |\nu_i\rangle, \qquad \alpha = e, \mu, \tau; \quad i = 1, 2, 3. $$

$U$ is a $3\times 3$ unitary matrix conventionally parametrized by three mixing angles $\theta_{12}, \theta_{13}, \theta_{23}$ and one $CP$-violating phase $\delta$ (plus two Majorana phases if neutrinos are their own antiparticles — see below). **Neutrino oscillation** is the quantum-mechanical consequence: a neutrino created as flavor $\alpha$ evolves in time into a superposition of flavors, so the probability of detecting it as flavor $\beta$ oscillates with the propagation distance $L$ and energy $E$.

**定义。** 标准模型最初假设中微子是**无质量**的，每代轻子对应一种：电子中微子 $\nu_e$、渺子中微子 $\nu_\mu$ 和陶子中微子 $\nu_\tau$。这些是**味本征态**——在带电流弱相互作用中与 $W$ 玻色子耦合的态。若中微子有质量，这些味本征态就**不同于****质量本征态** $\nu_1$、$\nu_2$、$\nu_3$（具有确定质量 $m_1$、$m_2$、$m_3$ 的态）。两组基通过**庞特克沃–牧–中川–坂田（PMNS）混合矩阵** $U$ 联系：

$$ |\nu_\alpha\rangle = \sum_i U^*_{\alpha i}\, |\nu_i\rangle, \qquad \alpha = e, \mu, \tau; \quad i = 1, 2, 3. $$

$U$ 是 $3\times 3$ 酉矩阵，通常用三个混合角 $\theta_{12}$、$\theta_{13}$、$\theta_{23}$ 和一个 $CP$ 破坏相位 $\delta$ 参数化（若中微子是自身的反粒子，还需加上两个马约拉纳相位——见下文）。**中微子振荡**是量子力学的直接结果：以味 $\alpha$ 产生的中微子随时间演化为多种味的叠加，因此探测到味 $\beta$ 的概率随传播距离 $L$ 和能量 $E$ 振荡。

**Demonstration — the solar and atmospheric neutrino problems.** Two foundational anomalies established oscillations experimentally.

*The solar neutrino problem (1968–2002).* The Sun produces electron neutrinos via pp-chain and CNO-cycle reactions. Calculations by John Bahcall (Standard Solar Model) predicted a flux at Earth; the Homestake chlorine detector (Davis, 1968) measured only $\sim 1/3$ as many. This deficit persisted across multiple experiments (GALLEX, SAGE, Super-Kamiokande). Resolution came from the **Sudbury Neutrino Observatory (SNO)** in 2001–2002: SNO could measure both the $\nu_e$-only flux (via the charged-current reaction $\nu_e + d \to p + p + e^-$) and the **total** neutrino flux of all flavors (via the neutral-current reaction $\nu + d \to p + n + \nu$, equally sensitive to all flavors). SNO found that the total flux matched the solar model prediction — the "missing" $\nu_e$ had oscillated into $\nu_\mu$ and $\nu_\tau$. The solar neutrino problem was solved: **neutrinos have mass and mix**.

*The atmospheric neutrino problem (1998).* Cosmic rays hitting the upper atmosphere produce pions that decay: $\pi^+ \to \mu^+ + \nu_\mu$ followed by $\mu^+ \to e^+ + \nu_e + \bar{\nu}_\mu$. The ratio $\nu_\mu/\nu_e$ should be approximately 2. Super-Kamiokande (1998) found a deficit of $\nu_\mu$ that depended on the **zenith angle** — i.e., on the distance $L$ traveled through the Earth. This $L/E$ dependence is the unambiguous signature of oscillation. Super-Kamiokande established $\nu_\mu \to \nu_\tau$ oscillations with near-maximal mixing ($\theta_{23} \approx 45^\circ$) and $\Delta m^2_{23} \approx 2.5 \times 10^{-3}\ \text{eV}^2$. Davis and Koshiba (Super-K) shared the 2002 Nobel Prize.

**演示 — 太阳中微子问题与大气中微子问题。** 两个奠基性异常从实验上确立了振荡现象。

*太阳中微子问题（1968–2002）。* 太阳通过质子–质子链和 CNO 循环产生电子中微子。约翰·巴考尔（标准太阳模型）预言了到达地球的流量；霍姆斯特克氯探测器（戴维斯，1968 年）只测到约 1/3。这一亏缺在多个实验（GALLEX、SAGE、Super-K）中持续出现。答案来自**萨德伯里中微子观测站（SNO）**（2001–2002 年）：SNO 能分别测量仅 $\nu_e$ 的流量（通过带电流反应 $\nu_e + d \to p + p + e^-$）和**所有味**的总流量（通过中性流反应 $\nu + d \to p + n + \nu$，对所有味同等灵敏）。SNO 发现总流量与太阳模型预言一致——"消失的" $\nu_e$ 已振荡为 $\nu_\mu$ 和 $\nu_\tau$。太阳中微子问题得到解决：**中微子有质量并发生混合**。

*大气中微子问题（1998 年）。* 宇宙射线打在高层大气产生 $\pi$ 介子衰变：$\pi^+ \to \mu^+ + \nu_\mu$，随后 $\mu^+ \to e^+ + \nu_e + \bar{\nu}_\mu$。$\nu_\mu/\nu_e$ 的比值应约为 2。Super-Kamiokande（1998 年）发现 $\nu_\mu$ 亏缺，且依赖于**天顶角**——即穿越地球的距离 $L$。这种 $L/E$ 依赖性是振荡的明确特征。Super-K 确立了接近最大混合（$\theta_{23} \approx 45^\circ$）的 $\nu_\mu \to \nu_\tau$ 振荡，$\Delta m^2_{23} \approx 2.5 \times 10^{-3}\ \text{eV}^2$。戴维斯和小柴昌俊（Super-K）共享了 2002 年诺贝尔物理学奖。

**Application — the MSW matter effect.** In matter, neutrinos experience an **effective potential** from forward scattering. Only $\nu_e$ can scatter via the charged-current $W$-exchange diagram (off electrons), while all flavors scatter via neutral $Z$-exchange. The $\nu_e$-specific extra potential shifts the effective mass matrix and can cause **resonant flavor conversion**: at a critical density $n_e^{\text{res}} = \Delta m^2 \cos(2\theta) / (2\sqrt{2}\, G_F E)$, the effective mixing angle in matter becomes $45^\circ$, leading to complete flavor conversion. This **MSW effect** (Mikheyev–Smirnov–Wolfenstein) explains why the solar mixing angle $\theta_{12} \approx 34^\circ$ in vacuum still produces nearly complete $\nu_e \to \nu_\mu/\nu_\tau$ conversion inside the Sun. The resonance occurs in the solar interior as the neutrino propagates outward through decreasing density.

**应用 — MSW 物质效应。** 在物质中，中微子通过前向散射获得**有效势能**。只有 $\nu_e$ 能通过带电流 $W$ 交换费曼图（与电子）散射，而所有味都通过中性 $Z$ 交换散射。$\nu_e$ 特有的额外势能改变了有效质量矩阵，可引起**共振味转换**：在临界密度 $n_e^{\text{res}} = \Delta m^2 \cos(2\theta) / (2\sqrt{2}\, G_F E)$ 处，物质中的有效混合角变为 $45^\circ$，导致完全的味转换。这一 **MSW 效应**（米哈耶夫–斯米尔诺夫–沃芬斯坦）解释了为何真空混合角 $\theta_{12} \approx 34^\circ$ 仍能在太阳内部产生近乎完全的 $\nu_e \to \nu_\mu/\nu_\tau$ 转换。随着中微子向外传播穿过密度递减的太阳内部，共振便在其中发生。

**Mass ordering, Dirac vs. Majorana, and neutrinoless double-beta decay.** Oscillations measure only **mass-squared differences**: $\Delta m^2_{12} \approx 7.4 \times 10^{-5}\ \text{eV}^2$ (solar) and $|\Delta m^2_{31}| \approx 2.5 \times 10^{-3}\ \text{eV}^2$ (atmospheric). We know $m_1 \neq m_2 \neq m_3$ but not the absolute scale. Two orderings are possible: **normal ordering** ($m_1 < m_2 < m_3$) and **inverted ordering** ($m_3 < m_1 < m_2$). Cosmological bounds (CMB + large-scale structure) give $\sum m_i < \sim 0.12\ \text{eV}$.

A deeper question: are neutrinos **Dirac fermions** (particle $\neq$ antiparticle, like the electron) or **Majorana fermions** (particle $=$ antiparticle, $\nu = \bar{\nu}$)? The see-saw mechanism (Module 8.5) naturally produces Majorana neutrino masses: introducing a heavy right-handed Majorana mass $M_R$ alongside the Dirac Yukawa coupling generates a light left-handed mass $m_\nu \approx m_D^2/M_R$ — making neutrino masses small because $M_R \gg m_D$. If neutrinos are Majorana, **neutrinoless double-beta decay** ($0\nu\beta\beta$: $(A,Z) \to (A,Z+2) + 2e^-$, with no neutrinos emitted) is allowed, since the anti-neutrino emitted at one vertex can be absorbed as a neutrino at the other. The rate is proportional to $|m_{\beta\beta}|^2$, the effective Majorana mass. Experiments (GERDA, KamLAND-Zen, nEXO) search for this process; its discovery would simultaneously confirm the Majorana nature, provide the absolute mass scale, and support the see-saw picture.

**质量顺序、狄拉克 vs. 马约拉纳与无中微子双 $\beta$ 衰变。** 振荡只能测量**质量平方差**：$\Delta m^2_{12} \approx 7.4 \times 10^{-5}\ \text{eV}^2$（太阳）和 $|\Delta m^2_{31}| \approx 2.5 \times 10^{-3}\ \text{eV}^2$（大气）。我们知道 $m_1 \neq m_2 \neq m_3$，但不知道绝对质量尺度。有两种可能的顺序：**正常顺序**（$m_1 < m_2 < m_3$）和**反转顺序**（$m_3 < m_1 < m_2$）。宇宙学约束（CMB + 大尺度结构）给出 $\sum m_i < \sim 0.12\ \text{eV}$。

更深层的问题：中微子是**狄拉克费米子**（粒子 $\neq$ 反粒子，如电子）还是**马约拉纳费米子**（粒子 $=$ 反粒子，$\nu = \bar{\nu}$）？跷跷板机制（模块 8.5）自然地产生马约拉纳中微子质量：引入重右手马约拉纳质量 $M_R$ 与狄拉克汤川耦合，生成轻左手质量 $m_\nu \approx m_D^2/M_R$——使中微子质量因 $M_R \gg m_D$ 而很小。若中微子是马约拉纳粒子，**无中微子双 $\beta$ 衰变**（$0\nu\beta\beta$：$(A,Z) \to (A,Z+2) + 2e^-$，无中微子发射）便是允许的，因为在一个顶点发射的反中微子可以在另一个顶点作为中微子被吸收。衰变率正比于 $|m_{\beta\beta}|^2$，即有效马约拉纳质量。实验（GERDA、KamLAND-Zen、nEXO）正在搜寻这一过程；其发现将同时证实马约拉纳本性、确定绝对质量尺度，并支持跷跷板图像。

---

## 2. Experimental Particle Physics · 实验粒子物理

**Definition.** Particle physics is empirical: every theoretical prediction must eventually confront experiment. Modern experiments rest on two pillars — **accelerators** that produce particles at high energy, and **detectors** that reconstruct what happened.

*Accelerators.* A **synchrotron** accelerates charged particles around a circular ring, using RF cavities to boost energy and bending magnets to keep particles on track. The energy is limited by synchrotron radiation (energy loss per turn $\propto E^4/R$ for leptons, much smaller for protons of the same energy). The **Large Hadron Collider (LHC)** at CERN is a proton–proton synchrotron with a 27 km circumference, reaching $\sqrt{s} = 13\text{–}14\ \text{TeV}$ center-of-mass energy. Colliding beams (rather than a fixed target) maximize the available center-of-mass energy: for two beams each of energy $E_\text{beam}$, $\sqrt{s} = 2E_\text{beam}$, whereas for a beam hitting a fixed target $\sqrt{s} = \sqrt{2m_p E_\text{beam}} \ll E_\text{beam}$ at high energy.

**定义。** 粒子物理学是实证性的：每一个理论预言最终都必须面对实验检验。现代实验依赖两大支柱——产生高能粒子的**加速器**和重建物理过程的**探测器**。

*加速器。* **同步加速器**将带电粒子在圆形环中加速，用射频腔增加能量，用偏转磁铁维持粒子轨道。能量受同步辐射限制（轻子每圈能量损失 $\propto E^4/R$，相同能量质子的损失要小得多）。CERN 的**大型强子对撞机（LHC）**是周长 27 km 的质子–质子同步加速器，质心系能量达 $\sqrt{s} = 13\text{–}14\ \text{TeV}$。对撞束（而非固定靶）最大化了可用质心能：两束能量各为 $E_\text{beam}$ 时，$\sqrt{s} = 2E_\text{beam}$；而束打固定靶时，在高能下 $\sqrt{s} = \sqrt{2m_p E_\text{beam}} \ll E_\text{beam}$。

**Demonstration — principal detector elements.** A modern multipurpose detector (ATLAS, CMS) is built in concentric shells around the interaction point.

*Tracking.* Silicon pixel and strip detectors and drift chambers surround the interaction vertex, embedded in a solenoidal magnetic field $B$. Charged particles follow helical paths; measuring the curvature radius $r$ gives the momentum $p = qBr$. Tracking reconstructs vertices, identifies displaced secondary vertices from long-lived particles (b-tagging), and measures charge.

*Calorimetry.* Calorimeters measure **energy** by stopping particles. An **electromagnetic calorimeter (ECAL)** — dense crystal or lead-glass — stops electrons and photons via bremsstrahlung and pair production cascades; the shower depth scales as the radiation length $X_0$. A **hadronic calorimeter (HCAL)** — iron/scintillator sandwich — stops hadrons via nuclear interactions; shower depth scales as the hadronic interaction length $\lambda_I \gg X_0$. Missing transverse energy (MET) — imbalance in the vector sum of all calorimeter deposits — signals invisible particles (neutrinos, dark matter candidates).

*Particle identification.* Cherenkov detectors (RICH counters) measure the angle of Cherenkov radiation $\theta_C = \arccos(1/\beta n)$, combining with a momentum measurement to give the mass and hence the particle species. Time-of-flight and transition radiation detectors also contribute. Muons, being minimally ionizing, penetrate all inner layers and are identified in muon spectrometers outside the calorimeters.

**演示 — 主要探测器元件。** 现代多用途探测器（ATLAS、CMS）围绕相互作用点呈同心层状结构构建。

*径迹探测。* 硅像素/条形探测器和漂移室包围相互作用顶点，嵌入螺线管磁场 $B$ 中。带电粒子走螺旋轨迹；测量曲率半径 $r$ 给出动量 $p = qBr$。径迹重建能重构顶点、识别长寿命粒子的次级顶点（b 标记），并测量电荷。

*量能器。* 量能器通过使粒子停止来测量**能量**。**电磁量能器（ECAL）**——致密晶体或铅玻璃——通过轫致辐射和对产生级联使电子和光子停止；簇射深度以辐射长度 $X_0$ 为标度。**强子量能器（HCAL）**——铁/闪烁体三明治——通过核相互作用使强子停止；簇射深度以强子相互作用长度 $\lambda_I \gg X_0$ 为标度。横向缺失能量（MET）——所有量能器沉积的矢量和的失衡——标志着不可见粒子（中微子、暗物质候选者）。

*粒子鉴别。* 切伦科夫探测器（RICH 计数器）测量切伦科夫辐射角 $\theta_C = \arccos(1/\beta n)$，与动量测量结合给出质量进而确定粒子种类。飞行时间探测器和渡越辐射探测器也有贡献。$\mu$ 子作为最低电离粒子，穿透所有内层，在量能器外部的 $\mu$ 子谱仪中被识别。

**Application — luminosity, event rates, and discovery logic.** The number of events of a given process produced in a collider experiment is

$$ N = L_\text{int} \cdot \sigma, $$

where $\sigma$ is the process **cross-section** (with dimensions of area; $1\ \text{fb}^{-1}$ of luminosity with $1\ \text{fb}$ cross-section gives 1 event) and $L_\text{int} = \int L\, dt$ is the **integrated luminosity**, the time-integral of the instantaneous luminosity $L = (n_1 n_2 f)/A$, with $n$ the bunch populations, $f$ the revolution frequency, and $A$ the beam cross-sectional area. The LHC delivered $\sim 140\ \text{fb}^{-1}$ of integrated luminosity in Runs 1+2. Every search for a new particle or process defines a signal cross-section times branching ratio times acceptance, and counts events above background.

**Discovery via invariant-mass peaks.** If a short-lived resonance $X$ with mass $M$ and width $\Gamma$ is produced and decays to final state particles $p_1, p_2, \ldots$, the decay products carry the four-momentum of the parent. The **invariant mass**

$$ M^2_\text{inv} = \Big(\sum_i p_i\Big)^2 = \Big(\sum_i E_i\Big)^2 - \Big|\sum_i \mathbf{p}_i\Big|^2 \quad (\text{in } c=1 \text{ units}) $$

reconstructed from all decay products equals $M^2$ at the resonance. A **Breit–Wigner peak** appears in the $M_\text{inv}$ distribution at $M$ with width $\propto \Gamma$, sitting above a smooth QCD background. The **$Z$ boson** was discovered this way at the SPS in 1983 (decaying to $e^+e^-$ and $\mu^+\mu^-$); the **Higgs boson** (Module 8.4) was discovered at the LHC in 2012 as a peak at $125\ \text{GeV}$ in both the $\gamma\gamma$ and $ZZ^* \to 4\ell$ invariant-mass distributions.

**应用 — 亮度、事例率与发现逻辑。** 对撞机实验中某一物理过程的事例数为

$$ N = L_\text{int} \cdot \sigma, $$

其中 $\sigma$ 是过程的**截面**（量纲为面积；$1\ \text{fb}^{-1}$ 亮度乘以 $1\ \text{fb}$ 截面给出 1 个事例），$L_\text{int} = \int L\, dt$ 是**积分亮度**，即瞬时亮度 $L = (n_1 n_2 f)/A$ 对时间的积分，$n$ 为束团粒子数，$f$ 为回旋频率，$A$ 为束流横截面面积。LHC 在第 1+2 次运行期间积累了约 $140\ \text{fb}^{-1}$ 的积分亮度。每项寻找新粒子或新过程的实验都定义了信号截面乘以分支比再乘以探测器接受度，并在本底之上计数事例。

**通过不变质量峰发现粒子。** 若质量为 $M$、宽度为 $\Gamma$ 的短寿命共振态 $X$ 被产生并衰变到末态粒子 $p_1$、$p_2$、…，则衰变产物携带母粒子的四动量。从所有衰变产物重建的**不变质量**

$$ M^2_\text{inv} = \Big(\sum_i p_i\Big)^2 = \Big(\sum_i E_i\Big)^2 - \Big|\sum_i \mathbf{p}_i\Big|^2 \quad (c=1 \text{ 单位制}) $$

在共振处等于 $M^2$。**布莱特–维格纳峰**出现在 $M_\text{inv}$ 分布中，位于 $M$ 处，宽度正比于 $\Gamma$，叠加在光滑的 QCD 本底之上。**$Z$ 玻色子**就是以这种方式在 1983 年于 SPS 被发现的（衰变到 $e^+e^-$ 和 $\mu^+\mu^-$）；**希格斯玻色子**（模块 8.4）于 2012 年在 LHC 以 $\gamma\gamma$ 和 $ZZ^* \to 4\ell$ 不变质量分布中 $125\ \text{GeV}$ 处的峰值被发现。

## Key results · 核心结果

- Flavor vs mass eigenstates; PMNS matrix (3 angles + CP phase) · 味与质量本征态;PMNS 矩阵
- SNO resolved the solar neutrino problem via NC + CC reactions · SNO 实验
- MSW matter effect; resonant flavor conversion · MSW 效应
- Dirac vs Majorana; $0\nu\beta\beta$; seesaw · 狄拉克/马约拉纳与无中微子双 β 衰变

---

**Self-test (blank page)**

1. Define flavor eigenstate and mass eigenstate for neutrinos. What is the PMNS matrix and what physical parameters does it contain?
2. Describe the SNO experiment: what two reactions did it use, and why could it resolve the solar neutrino problem when earlier experiments could not?
3. What is the MSW effect, and what is the resonance condition? Why is it important for solar neutrino propagation?
4. What is the difference between Dirac and Majorana neutrinos? How does neutrinoless double-beta decay test this distinction, and how does the see-saw mechanism predict small neutrino masses?
5. Define integrated luminosity and explain the relation $N = L_\text{int} \cdot \sigma$. What is the unit $\text{fb}^{-1}$ and what order-of-magnitude cross-sections does the LHC probe?
6. Explain how a new particle is discovered via an invariant-mass peak. Write down $M^2_\text{inv}$ in terms of the decay-product four-momenta and explain why this quantity peaks at the parent mass.

**自测（空白页）**

1. 定义中微子的味本征态与质量本征态。PMNS 矩阵是什么，它包含哪些物理参数？
2. 描述 SNO 实验：它使用了哪两种反应？为何早期实验无法解决太阳中微子问题，而 SNO 能够做到？
3. MSW 效应是什么，共振条件是什么？为何它对太阳中微子传播很重要？
4. 狄拉克中微子与马约拉纳中微子的区别是什么？无中微子双 $\beta$ 衰变如何检验这一区别，跷跷板机制如何预言小的中微子质量？
5. 定义积分亮度并解释关系式 $N = L_\text{int} \cdot \sigma$。$\text{fb}^{-1}$ 的单位是什么，LHC 探测的截面量级是多少？
6. 解释如何通过不变质量峰发现新粒子。用衰变产物四动量写出 $M^2_\text{inv}$，并解释为何该量在母粒子质量处出现峰值。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Flavor eigenstates $(\nu_e,\nu_\mu,\nu_\tau)$ couple to charged leptons; mass eigenstates $(\nu_1,\nu_2,\nu_3)$ propagate. The PMNS matrix relates them, with 3 mixing angles $(\theta_{12},\theta_{23},\theta_{13})$ and 1 Dirac CP phase (+2 Majorana phases). · 味↔质量本征态;PMNS 含 3 角 + CP 相位。
**2.** SNO used charged-current ($\nu_e$ only) and neutral-current (all flavors) reactions on deuterium. The NC total matched the solar-model flux while the CC was $\sim1/3$ — proving $\nu_e$ oscillate into $\nu_{\mu,\tau}$, resolving the solar neutrino problem. · SNO 用 NC + CC 证明味转换。
**3.** MSW: matter (electron density) shifts $\nu_e$ oscillations via coherent forward scattering; resonance when $2\sqrt2 G_F n_e E=\Delta m^2\cos2\theta$, driving efficient flavor conversion in the Sun's varying density. · MSW 共振条件。
**4.** Dirac: $\nu\neq\bar\nu$ (lepton number conserved). Majorana: $\nu=\bar\nu$ (its own antiparticle, $L$ violated). Neutrinoless double-beta decay occurs only for Majorana neutrinos — observing it proves their nature. The seesaw ($m_\nu\sim m_D^2/M_R$) explains their tiny masses. · 狄拉克/马约拉纳;$0\nu\beta\beta$ 与跷跷板。

</details>

---

← Previous: [Module 8.9 — Deep Inelastic Scattering & Partons](./module-8.9-deep-inelastic-scattering-and-partons.md) · [Phase 8 index](./README.md)

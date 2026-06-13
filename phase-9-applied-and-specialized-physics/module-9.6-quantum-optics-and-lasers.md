# Module 9.6 — Quantum Optics & Laser Physics
**模块 9.6 — 量子光学与激光物理**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.6-quantum-optics-and-lasers-derivations.md)

---

## 1. Einstein A & B Coefficients · 爱因斯坦 A 与 B 系数

**Definition.** Einstein (1917) described the interaction of a two-level atom (energies $E_1 < E_2$, degeneracies $g_1, g_2$, transition frequency $\nu = (E_2-E_1)/h$) with a thermal radiation field of spectral energy density $u(\nu)$ by three rates. **Absorption** lifts atoms from level 1 to level 2 at rate $B_{12}\, u(\nu)\, N_1$. **Stimulated emission** drives $2 \to 1$ at rate $B_{21}\, u(\nu)\, N_2$, producing a photon coherent with the driving field. **Spontaneous emission** drives $2 \to 1$ at rate $A_{21} N_2$ independent of the field. Demanding thermal equilibrium with the Planck law forces two universal relations: $g_1 B_{12} = g_2 B_{21}$ and $A_{21}/B_{21} = 8\pi h\nu^3/c^3$.

**定义。** 爱因斯坦（1917）用三个速率描述了二能级原子（能量 $E_1 < E_2$，简并度 $g_1$、$g_2$，跃迁频率 $\nu = (E_2-E_1)/h$）与谱能量密度为 $u(\nu)$ 的热辐射场的相互作用。**吸收**以速率 $B_{12}\, u(\nu)\, N_1$ 将原子从能级 1 提升到能级 2。**受激发射**以速率 $B_{21}\, u(\nu)\, N_2$ 驱动 $2 \to 1$，产生与驱动场相干的光子。**自发发射**以与场无关的速率 $A_{21} N_2$ 驱动 $2 \to 1$。要求与普朗克定律热平衡，强制给出两个普适关系：$g_1 B_{12} = g_2 B_{21}$ 与 $A_{21}/B_{21} = 8\pi h\nu^3/c^3$。

**Demonstration.** In steady state the upward and downward rates balance: $B_{12}\, u\, N_1 = A_{21} N_2 + B_{21}\, u\, N_2$. Solving for $u(\nu)$ and inserting the Boltzmann ratio $N_2/N_1 = (g_2/g_1)e^{-h\nu/kT}$ reproduces the Planck spectrum only if the two coefficient relations hold; the full algebra is in Derivation A. The ratio $A_{21}/B_{21} \propto \nu^3$ means spontaneous emission grows steeply with frequency relative to the stimulated process.

**演示。** 稳态下向上与向下速率平衡：$B_{12}\, u\, N_1 = A_{21} N_2 + B_{21}\, u\, N_2$。解出 $u(\nu)$ 并代入玻尔兹曼比 $N_2/N_1 = (g_2/g_1)e^{-h\nu/kT}$，仅当两个系数关系成立时才重现普朗克谱；完整代数见推导 A。比值 $A_{21}/B_{21} \propto \nu^3$ 意味着自发发射相对受激过程随频率陡峭增长。

**Application.** The $\nu^3$ scaling explains why coherent light sources are easy in the microwave (masers, 1954) but hard in the X-ray and $\gamma$-ray: at high frequency spontaneous emission rapidly depopulates the upper level before stimulated emission can build up a coherent field. The A/B relation also underlies the radiative lifetime $\tau = 1/A_{21}$ that sets natural linewidths and is the QED rate computed in Modules 6.1/8.2.

**应用。** $\nu^3$ 标度解释了为何相干光源在微波段容易实现（脉泽，1954），而在 X 射线和 $\gamma$ 射线段困难：在高频下，自发发射在受激发射能建立相干场之前迅速耗尽上能级。A/B 关系还给出辐射寿命 $\tau = 1/A_{21}$，它确定了自然线宽，即模块 6.1/8.2 中计算的 QED 速率。

---

## 2. Population Inversion & Laser Gain · 粒子数反转与激光增益

**Definition.** When radiation of density $u(\nu)$ passes through the medium, the net rate of photons added to the field by the $2 \leftrightarrow 1$ transition is proportional to $N_2 B_{21} - N_1 B_{12} = B_{21}(N_2 - (g_2/g_1)N_1)$. Amplification (net stimulated emission exceeding absorption) therefore requires a **population inversion**: $N_2/g_2 > N_1/g_1$. The beam grows as $I(z) = I(0)\, e^{\gamma(\nu)z}$ with **gain coefficient** $\gamma(\nu) \propto (N_2 - (g_2/g_1)N_1)$. Lasing starts when the round-trip gain exceeds the round-trip cavity loss (the **threshold condition**).

**定义。** 当密度为 $u(\nu)$ 的辐射通过介质时，$2 \leftrightarrow 1$ 跃迁向场净增添光子的速率正比于 $N_2 B_{21} - N_1 B_{12} = B_{21}(N_2 - (g_2/g_1)N_1)$。因此放大（净受激发射超过吸收）要求**粒子数反转**：$N_2/g_2 > N_1/g_1$。光束按 $I(z) = I(0)\, e^{\gamma(\nu)z}$ 增长，**增益系数** $\gamma(\nu) \propto (N_2 - (g_2/g_1)N_1)$。当往返增益超过往返腔损耗时起振（**阈值条件**）。

**Demonstration.** Using the Einstein relation $g_1 B_{12} = g_2 B_{21}$, the net stimulated power per atom is $\propto B_{21}(N_2 - (g_2/g_1)N_1)$. In a closed two-level system pumped by radiation alone, equilibrium can at best saturate to $N_2/g_2 = N_1/g_1$ (transparency) but never invert, because the same field that pumps up also stimulates down — shown in Derivation B. Inversion therefore requires auxiliary levels: a three-level scheme (ruby) or a four-level scheme (Nd:YAG, He-Ne) where fast non-radiative decay keeps the lower laser level nearly empty.

**演示。** 利用爱因斯坦关系 $g_1 B_{12} = g_2 B_{21}$，每个原子的净受激功率 $\propto B_{21}(N_2 - (g_2/g_1)N_1)$。在仅由辐射泵浦的封闭二能级系统中，平衡最多饱和到 $N_2/g_2 = N_1/g_1$（透明）而永不反转，因为泵浦向上的同一场也受激向下——见推导 B。因此反转需要辅助能级：三能级方案（红宝石）或四能级方案（Nd:YAG、He-Ne），其中快速非辐射衰变使下激光能级几乎为空。

**Application.** The threshold condition $\gamma(\nu)L \geq$ loss per pass fixes the minimum pump power of every laser. Four-level lasers reach threshold far more easily than three-level lasers because the lower level starts empty, so even a small upper-level population gives inversion. This logic — pump, invert, place in a resonant cavity above threshold — is the operating principle of every laser from laboratory diode lasers to fusion-driver glass amplifiers.

**应用。** 阈值条件 $\gamma(\nu)L \geq$ 每程损耗确定了每台激光器的最小泵浦功率。四能级激光器比三能级激光器更易达到阈值，因为下能级初始为空，故即使很小的上能级布居也能给出反转。这一逻辑——泵浦、反转、置于阈值以上的谐振腔中——是从实验室二极管激光器到聚变驱动玻璃放大器的每台激光器的工作原理。

---

## 3. Coherent States & the Quantized Light Field · 相干态与量子化光场

**Definition.** Quantizing a single field mode gives a harmonic oscillator with number states $|n\rangle$, raising/lowering operators $a^\dagger, a$, and Hamiltonian $H = \hbar\omega(a^\dagger a + \tfrac12)$. The **coherent state** $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_n \frac{\alpha^n}{\sqrt{n!}} |n\rangle$ is the eigenstate of the annihilation operator, $a|\alpha\rangle = \alpha|\alpha\rangle$, and is the quantum state that most closely behaves like a classical monochromatic wave of complex amplitude $\alpha$. Its photon number is **Poisson-distributed**, $P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$, with $\langle n\rangle = |\alpha|^2$ and variance $\Delta n^2 = |\alpha|^2$, and it saturates the **minimum-uncertainty** bound $\Delta x\, \Delta p = \hbar/2$.

**定义。** 量子化单个场模式给出一个具有数态 $|n\rangle$、升降算符 $a^\dagger$、$a$ 以及哈密顿量 $H = \hbar\omega(a^\dagger a + \tfrac12)$ 的谐振子。**相干态** $|\alpha\rangle = e^{-|\alpha|^2/2} \sum_n \frac{\alpha^n}{\sqrt{n!}} |n\rangle$ 是湮灭算符的本征态，$a|\alpha\rangle = \alpha|\alpha\rangle$，是最接近经典复振幅为 $\alpha$ 的单色波行为的量子态。其光子数服从**泊松分布**，$P(n) = e^{-|\alpha|^2}|\alpha|^{2n}/n!$，$\langle n\rangle = |\alpha|^2$，方差 $\Delta n^2 = |\alpha|^2$，且饱和**最小不确定**界 $\Delta x\, \Delta p = \hbar/2$。

**Demonstration.** Acting with $a$ on the series and shifting the summation index confirms $a|\alpha\rangle = \alpha|\alpha\rangle$; reading off $|\langle n|\alpha\rangle|^2$ gives the Poisson law, from which $\langle n\rangle = |\alpha|^2$ and $\Delta n^2 = |\alpha|^2$ follow immediately, so the relative fluctuation $\Delta n/\langle n\rangle = 1/\sqrt{\langle n\rangle}$ vanishes in the bright-field limit (Derivation D). Writing the quadratures $x \propto (a + a^\dagger)$, $p \propto (a - a^\dagger)/i$ shows each has the vacuum variance, giving $\Delta x\, \Delta p = \hbar/2$. A **squeezed state** redistributes this product, pushing one quadrature variance below the vacuum value $\tfrac12$ at the expense of the other.

**演示。** 用 $a$ 作用于级数并移动求和指标确认 $a|\alpha\rangle = \alpha|\alpha\rangle$；读出 $|\langle n|\alpha\rangle|^2$ 给出泊松定律，由此立即得到 $\langle n\rangle = |\alpha|^2$ 与 $\Delta n^2 = |\alpha|^2$，故相对涨落 $\Delta n/\langle n\rangle = 1/\sqrt{\langle n\rangle}$ 在亮场极限下趋于零（推导 D）。写出正交分量 $x \propto (a + a^\dagger)$、$p \propto (a - a^\dagger)/i$，表明每个都具有真空方差，给出 $\Delta x\, \Delta p = \hbar/2$。**压缩态**重新分配这一乘积，将一个正交分量的方差压到真空值 $\tfrac12$ 以下，以另一个为代价。

**Application.** A laser well above threshold emits a coherent state, so the $\sqrt{\langle n\rangle}$ Poisson noise is the **shot noise** limiting all classical optical measurements. Squeezed light beats this limit and is injected into LIGO/Virgo to improve gravitational-wave strain sensitivity. The single-mode field coupled to one atom is described by the Jaynes–Cummings model (Derivation E), whose vacuum Rabi splitting $2g$ is the defining signature of cavity quantum electrodynamics.

**应用。** 远高于阈值的激光器发射相干态，故 $\sqrt{\langle n\rangle}$ 泊松噪声是限制所有经典光学测量的**散粒噪声**。压缩光突破此极限，被注入 LIGO/Virgo 以提高引力波应变灵敏度。耦合到单个原子的单模场由杰恩斯–卡明斯模型描述（推导 E），其真空拉比劈裂 $2g$ 是腔量子电动力学的标志性特征。

## Key results · 核心结果

- Einstein $A,B$ coefficients; $g_1 B_{12}=g_2 B_{21}$, $A_{21}/B_{21}=8\pi h\nu^3/c^3$ · 爱因斯坦系数
- Population inversion required to lase; need 3- or 4-level schemes · 粒子数反转
- Rabi oscillations $P_e=\sin^2(\Omega t/2)$; $\pi$-pulse inverts · 拉比振荡
- Coherent state $|\alpha\rangle$: Poissonian photons, $\Delta n=\sqrt{\langle n\rangle}$ · 相干态

---

**Self-test (blank page)**

1. Write the three Einstein rate processes and derive both coefficient relations $g_1 B_{12} = g_2 B_{21}$ and $A_{21}/B_{21} = 8\pi h\nu^3/c^3$ by imposing the Planck law. Why does the $\nu^3$ factor make X-ray lasers hard?
2. State the population-inversion condition and explain why a purely radiatively pumped two-level system can never lase. How do three- and four-level schemes fix this?
3. For a two-level atom driven on resonance, sketch $P_e(t)$. What is a $\pi$-pulse and what does it do to the population?
4. Define the coherent state $|\alpha\rangle$, prove it is an eigenstate of $a$, and derive its photon-number statistics, $\langle n\rangle$, and $\Delta n^2$.

**自测（空白页）**

1. 写出三个爱因斯坦速率过程，并通过施加普朗克定律推导两个系数关系 $g_1 B_{12} = g_2 B_{21}$ 与 $A_{21}/B_{21} = 8\pi h\nu^3/c^3$。为何 $\nu^3$ 因子使 X 射线激光器困难？
2. 陈述粒子数反转条件，并解释为何纯辐射泵浦的二能级系统永不能激射。三能级与四能级方案如何解决此问题？
3. 对共振驱动的二能级原子，画出 $P_e(t)$。什么是 $\pi$ 脉冲，它对布居做什么？
4. 定义相干态 $|\alpha\rangle$，证明它是 $a$ 的本征态，并推导其光子数统计、$\langle n\rangle$ 和 $\Delta n^2$。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Absorption ($B_{12}$), stimulated emission ($B_{21}$), spontaneous emission ($A_{21}$). Detailed balance + Planck law give $g_1 B_{12}=g_2 B_{21}$ and $A_{21}/B_{21}=8\pi h\nu^3/c^3$. The $\nu^3$ makes spontaneous emission dominate at high $\nu$ → hard to sustain inversion → X-ray lasers are difficult. · 三过程与系数关系;$\nu^3$ 使 X 射线激光困难。
**2.** Need $N_2>N_1$. A radiatively pumped two-level system can at best reach $N_1=N_2$ (since $B_{12}=B_{21}$), never invert; three-/four-level schemes use a fast-decaying pump band and a metastable upper laser level to build inversion. · 二能级无法反转,需三/四能级。
**3.** $P_e(t)=\sin^2(\Omega t/2)$ (resonant Rabi flopping). A $\pi$-pulse ($\Omega t=\pi$) fully transfers population ground → excited. · 拉比振荡;$\pi$ 脉冲完全反转。
**4.** $|\alpha\rangle=e^{-|\alpha|^2/2}\sum_n\frac{\alpha^n}{\sqrt{n!}}|n\rangle$ satisfies $a|\alpha\rangle=\alpha|\alpha\rangle$; the photon number is Poissonian with $\langle n\rangle=|\alpha|^2$ and $\Delta n^2=|\alpha|^2=\langle n\rangle$. · 相干态;泊松光子统计。

</details>

---

← Previous: [Module 9.5 — Nuclear Reactions & Astrophysics](./module-9.5-nuclear-reactions-and-astrophysics.md) · [Phase 9 index](./README.md) · Next: [Module 9.7 — Atoms in External Fields & Precision Spectroscopy](./module-9.7-atoms-in-external-fields.md) →

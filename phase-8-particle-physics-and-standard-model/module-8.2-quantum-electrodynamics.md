# Module 8.2 — Quantum Electrodynamics (QED) ⭐
**模块 8.2 — 量子电动力学 ⭐**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.2-derivations.md)

---

## 1. The U(1) Gauge Theory of Light and Matter · 光与物质的 U(1) 规范理论

**Definition.** **Quantum Electrodynamics** is the quantum field theory of electrons (and other charged leptons) interacting via photons. Its Lagrangian is the one derived in Module 8.1 by demanding local $U(1)$ invariance: $\mathcal{L}_\text{QED} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - \tfrac14 F_{\mu\nu}F^{\mu\nu}$, where $D_\mu = \partial_\mu - ieA_\mu$. The single free parameter is the electric charge $e$, equivalently the **fine-structure constant** $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$ at low energies. The theory was completed by Feynman, Schwinger, and Tomonaga in the late 1940s using the renormalization procedure developed systematically in Module 6.6.

**定义。** **量子电动力学**是描述电子（及其他带电轻子）通过光子相互作用的量子场论。其拉格朗日量正是模块 8.1 中通过要求局域 $U(1)$ 不变性推导得到的：$\mathcal{L}_\text{QED} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - \tfrac14 F_{\mu\nu}F^{\mu\nu}$，其中 $D_\mu = \partial_\mu - ieA_\mu$。唯一的自由参数是电荷 $e$，等价地为低能下的**精细结构常数** $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$。该理论由费曼、施温格和朝永振一郎在 20 世纪 40 年代末，利用模块 6.6 中系统发展的重整化方法最终完成。

**Demonstration.** The Feynman rules of QED reduce every $S$-matrix element to a sum over diagrams. Each internal photon line contributes a propagator $-ig_{\mu\nu}/q^2$, each electron line $i(\gamma^\mu p_\mu + m)/(p^2 - m^2)$, and each electron–photon **vertex** contributes $-ie\gamma^\mu$ — the fundamental three-point interaction where a fermion emits or absorbs a photon. At tree level (no loops), the cross-section for **$e^+e^- \to \mu^+\mu^-$** through a virtual photon is $\sigma = (4\pi\alpha^2)/(3s)$, where $s = (2E)^2$ is the center-of-mass energy squared. This is the flagship QED prediction for lepton colliders and agrees with experiment to better than 1%.

**演示。** 量子电动力学的费曼规则将每个 $S$ 矩阵元归结为对费曼图的求和。每条内线光子贡献传播子 $-ig_{\mu\nu}/q^2$，每条电子线贡献 $i(\gamma^\mu p_\mu + m)/(p^2 - m^2)$，每个电子–光子**顶角**贡献 $-ie\gamma^\mu$——这是费米子发射或吸收光子的基本三点相互作用。在树图水平（无圈），通过虚光子的 **$e^+e^- \to \mu^+\mu^-$** 散射截面为 $\sigma = (4\pi\alpha^2)/(3s)$，其中 $s = (2E)^2$ 是质心系能量平方。这是量子电动力学对轻子对撞机的标志性预言，与实验的符合优于 1%。

**Application.** QED is the **most precisely tested theory in physics**. The anomalous magnetic moment of the electron, $g - 2$, has been calculated through five-loop QED ($\sim$10 000 Feynman diagrams) and measured to 13 significant figures; theory and experiment agree. The Lamb shift in hydrogen (splitting of $2S_{1/2}$ and $2P_{1/2}$) was the first triumph of renormalization and is reproduced to parts per million. These precision tests also probe for new physics: any discrepancy would signal physics beyond the Standard Model.

**应用。** 量子电动力学是**物理学中经过最精确检验的理论**。电子反常磁矩 $g - 2$ 已经过五圈量子电动力学计算（约 10 000 个费曼图）并测量至 13 位有效数字，理论与实验完全吻合。氢的兰姆位移（$2S_{1/2}$ 与 $2P_{1/2}$ 的分裂）是重整化理论的第一个胜利，精确到百万分之一的量级。这些精密检验也探索新物理：任何偏差都将预示超出标准模型的物理现象。

---

## 2. Running Coupling and the Limits of QED · 跑动耦合常数与量子电动力学的适用范围

**Definition.** The coupling $\alpha$ is not truly constant: loop corrections (vacuum polarization — virtual $e^+e^-$ pairs screening the bare charge) make it **energy-dependent**. This is the running of the coupling, derived in Module 6.6. In QED $\alpha$ increases logarithmically with energy: $\alpha(m_Z) \approx 1/128$, compared to $\alpha(0) \approx 1/137$ at atomic energies. The energy scale at which $\alpha$ formally diverges (the **Landau pole**) is $\sim 10^{286}$ eV — far beyond any physics, so QED is self-consistent up to any accessible scale. This running is the opposite of QCD (Module 8.3), where the coupling decreases at high energy.

**定义。** 耦合常数 $\alpha$ 并非真正的常数：圈图修正（真空极化——虚 $e^+e^-$ 对屏蔽裸电荷）使其**依赖于能量**。这就是耦合常数的跑动，模块 6.6 中已对此推导。在量子电动力学中，$\alpha$ 随能量对数增长：$\alpha(m_Z) \approx 1/128$，而在原子能量下 $\alpha(0) \approx 1/137$。$\alpha$ 正式发散的能量尺度（**朗道极点**）约为 $\sim 10^{286}$ eV——远超任何物理范围，因此量子电动力学在任何可访问的尺度上都是自洽的。这与量子色动力学（模块 8.3）相反，后者的耦合常数在高能下减小。

**Demonstration.** The one-loop renormalization group equation for QED is $d\alpha/d(\ln\mu) = \alpha^2/(3\pi)$, with $\beta$-function coefficient $+1/3\pi > 0$ (the positive sign means the coupling grows with scale — **screening**). Integrating gives $1/\alpha(\mu) = 1/\alpha(\mu_0) - (1/3\pi)\ln(\mu/\mu_0)$. Setting $\mu_0 = m_e$ reproduces the measured values: at $\mu = m_Z \approx 91$ GeV, $\ln(m_Z/m_e) \approx 12.5$, giving $\Delta(1/\alpha) \approx -1.4$, consistent with the observed change from 137 to $\approx 128$.

**演示。** 量子电动力学的单圈重整化群方程为 $d\alpha/d(\ln\mu) = \alpha^2/(3\pi)$，$\beta$ 函数系数为 $+1/3\pi > 0$（正号意味着耦合随能量标度增长——**屏蔽**）。积分得 $1/\alpha(\mu) = 1/\alpha(\mu_0) - (1/3\pi)\ln(\mu/\mu_0)$。令 $\mu_0 = m_e$ 可重现测量值：在 $\mu = m_Z \approx 91$ GeV 处，$\ln(m_Z/m_e) \approx 12.5$，给出 $\Delta(1/\alpha) \approx -1.4$，与从 137 变化至约 128 的观测结果一致。

**Application.** The running coupling is the prototype for understanding all gauge-theory couplings. In the Standard Model, the three coupling constants of $SU(3)\times SU(2)\times U(1)$ run with energy and — if extended to a supersymmetric spectrum — meet at a single point near $10^{16}$ GeV, the tantalizing hint of **grand unification** (Module 8.5). The precision of this meeting depends on the accuracy of $\alpha$ measured by QED tests.

**应用。** 跑动耦合常数是理解所有规范理论耦合常数的原型。在标准模型中，$SU(3)\times SU(2)\times U(1)$ 的三个耦合常数随能量跑动，若推广到超对称谱，它们在 $10^{16}$ GeV 附近汇聚于一点，这是**大统一**的诱人迹象（模块 8.5）。这一汇聚的精确性依赖于量子电动力学检验所测定的 $\alpha$ 的精度。

---

## Self-test (blank page)

1. Write the QED Lagrangian and identify the gauge-invariant kinetic term, the fermion mass term, and the interaction vertex. What is the Feynman rule for the vertex?
2. Derive the tree-level cross-section for $e^+e^- \to \mu^+\mu^-$ in terms of $\alpha$ and $s$ using dimensional analysis or the known result; explain physically why it falls as $1/s$.
3. Explain the physical origin of the running of $\alpha$ in QED. Why does $\alpha$ increase with energy (screening), and how does this differ from QCD?

**自测（空白页）**

1. 写出量子电动力学拉格朗日量，并指出规范不变的动能项、费米子质量项和相互作用顶角。顶角的费曼规则是什么？
2. 用量纲分析或已知结果，以 $\alpha$ 和 $s$ 推导 $e^+e^- \to \mu^+\mu^-$ 的树图截面；从物理上解释为何它随 $1/s$ 下降。
3. 解释量子电动力学中 $\alpha$ 跑动的物理起源。为何 $\alpha$ 随能量增大（屏蔽），这与量子色动力学有何不同？

---

← Previous: [Module 8.1 — Symmetries & Gauge Theory](./module-8.1-symmetries-and-gauge-theory.md) · [Phase 8 index](./README.md) · Next: [Module 8.3 — The Strong Interaction (QCD)](./module-8.3-quantum-chromodynamics.md) →

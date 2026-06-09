# Module 8.4 — Electroweak Theory & the Higgs ⭐⭐
**模块 8.4 — 电弱理论与希格斯机制 ⭐⭐**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.4-derivations.md)

---

## 1. Unifying Electromagnetism and the Weak Force · 统一电磁力与弱力

**Definition.** The **electroweak theory** (Glashow, Salam, Weinberg, 1967–68) unifies electromagnetism and the weak nuclear force in a single gauge theory with group $SU(2)_L \times U(1)_Y$. The $SU(2)_L$ factor acts only on left-handed fermion doublets (e.g., $(\nu_e, e)_L$ and $(u, d)_L$), with three gauge fields $W_\mu^{1,2,3}$. The $U(1)_Y$ factor introduces a single field $B_\mu$ associated with **weak hypercharge** $Y$. These four gauge fields mix: the physical mass eigenstates are the charged $W^\pm = (W_\mu^1 \mp iW_\mu^2)/\sqrt2$, the neutral $Z^0 = W_\mu^3 \cos\theta_W - B_\mu \sin\theta_W$, and the photon $A_\mu = W_\mu^3 \sin\theta_W + B_\mu \cos\theta_W$, where $\theta_W \approx 28.7^\circ$ is the **Weinberg angle**. The electric charge is $e = g \sin\theta_W = g' \cos\theta_W$, with $g, g'$ the $SU(2)$ and $U(1)$ couplings. Without additional ingredients the symmetry is exact and all gauge bosons are massless — contradicting the observed short range of the weak force.

**定义。** **电弱理论**（格拉肖、萨拉姆、温伯格，1967–68 年）在规范群 $SU(2)_L \times U(1)_Y$ 的单一规范理论框架内统一了电磁力与弱核力。$SU(2)_L$ 因子仅作用于左手费米子双重态（如 $(\nu_e, e)_L$ 和 $(u, d)_L$），具有三个规范场 $W_\mu^{1,2,3}$。$U(1)_Y$ 因子引入与**弱超荷** $Y$ 相关的单一场 $B_\mu$。这四个规范场发生混合：物理质量本征态为带电的 $W^\pm = (W_\mu^1 \mp iW_\mu^2)/\sqrt2$，中性的 $Z^0 = W_\mu^3 \cos\theta_W - B_\mu \sin\theta_W$，以及光子 $A_\mu = W_\mu^3 \sin\theta_W + B_\mu \cos\theta_W$，其中 $\theta_W \approx 28.7^\circ$ 为**温伯格角**。电荷为 $e = g \sin\theta_W = g' \cos\theta_W$，$g$、$g'$ 分别为 $SU(2)$ 和 $U(1)$ 的耦合常数。若无额外成分，对称性严格成立，所有规范玻色子无质量——这与弱力的观测短程性相矛盾。

**Demonstration.** The weak force is mediated by $W^\pm$ (charge-changing, e.g., $n \to p + e^- + \bar\nu_e$ in $\beta$-decay) and $Z^0$ (neutral-current, e.g., $\nu_\mu e^- \to \nu_\mu e^-$). At low energies $q^2 \ll m_W^2$, the $W$ propagator reduces to a contact interaction with Fermi constant $G_F/\sqrt2 = g^2/(8m_W^2) \approx 1.17 \times 10^{-5}$ GeV$^{-2}$. The short range $r \sim \hbar/(m_W c) \sim 10^{-18}$ m follows directly from the large $W$ mass ($m_W \approx 80.4$ GeV, $m_Z \approx 91.2$ GeV). These masses must be generated without breaking gauge invariance — the job of the Higgs mechanism.

**演示。** 弱力由 $W^\pm$（改变电荷，例如 $\beta$ 衰变中的 $n \to p + e^- + \bar\nu_e$）和 $Z^0$（中性流，例如 $\nu_\mu e^- \to \nu_\mu e^-$）传递。在低能量 $q^2 \ll m_W^2$ 下，$W$ 传播子退化为接触相互作用，费米常数 $G_F/\sqrt2 = g^2/(8m_W^2) \approx 1.17 \times 10^{-5}$ GeV$^{-2}$。短程 $r \sim \hbar/(m_W c) \sim 10^{-18}$ m 直接源于 $W$ 玻色子的大质量（$m_W \approx 80.4$ GeV，$m_Z \approx 91.2$ GeV）。这些质量必须在不破坏规范不变性的前提下产生——这正是希格斯机制的任务。

**Application.** The $SU(2) \times U(1)$ structure unifies two of the four fundamental forces: at energies well above $m_Z$ the electromagnetic and weak interactions have comparable strength. The $W^\pm$ and $Z^0$ bosons were discovered at CERN in 1983 with precisely the predicted masses. The electroweak sector of the Standard Model is tested to sub-percent precision at LEP and the LHC, making it as well-confirmed as QED.

**应用。** $SU(2) \times U(1)$ 结构统一了四种基本力中的两种：在远超 $m_Z$ 的能量下，电磁相互作用与弱相互作用具有相当的强度。$W^\pm$ 和 $Z^0$ 玻色子于 1983 年在欧洲核子研究中心被发现，质量与预言完全一致。标准模型电弱部分在大型正负电子对撞机和大型强子对撞机上的检验精度优于百分之一，其确认程度堪比量子电动力学。

---

## 2. Spontaneous Symmetry Breaking and the Higgs Mechanism · 自发对称性破缺与希格斯机制

**Definition.** The **Higgs mechanism** is spontaneous symmetry breaking (Module 2.3) applied to the gauge symmetry of the electroweak vacuum. A complex scalar doublet $\phi = (\phi^+, \phi^0)$ with $SU(2)_L \times U(1)_Y$ quantum numbers is added to the theory with a **Mexican-hat potential** $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$. For $\mu^2 > 0$ the minimum is at $|\phi|^2 = v^2/2$ with $v = \sqrt{\mu^2/\lambda} \approx 246$ GeV — the **vacuum expectation value**. The vacuum picks a direction $\langle\phi\rangle = (0, v/\sqrt2)$, spontaneously breaking $SU(2)_L \times U(1)_Y$ down to $U(1)_\text{EM}$. This is identical in mathematics to the Ginzburg–Landau free energy (Module 5.3) and the Anderson mechanism in superconductors (Module 5.3): the photon acquires a mass inside a superconductor; here the $W^\pm$ and $Z^0$ acquire mass in the vacuum of the universe.

**定义。** **希格斯机制**是将自发对称性破缺（模块 2.3）应用于电弱真空的规范对称性。向理论中添加一个具有 $SU(2)_L \times U(1)_Y$ 量子数的复标量双重态 $\phi = (\phi^+, \phi^0)$，并赋予其**墨西哥帽势** $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$。当 $\mu^2 > 0$ 时，极小值位于 $|\phi|^2 = v^2/2$，其中 $v = \sqrt{\mu^2/\lambda} \approx 246$ GeV——即**真空期望值**。真空选择方向 $\langle\phi\rangle = (0, v/\sqrt2)$，将 $SU(2)_L \times U(1)_Y$ 自发破缺至 $U(1)_\text{EM}$。这在数学上与金兹堡–朗道自由能（模块 5.3）和超导体中的安德森机制（模块 5.3）完全相同：光子在超导体内部获得质量；而在这里，$W^\pm$ 和 $Z^0$ 在宇宙的真空中获得质量。

**Demonstration.** Expanding $\phi$ around the minimum, $\phi = (0, (v + h)/\sqrt2)$, and inserting into the gauge-kinetic term $|D_\mu\phi|^2$, the terms quadratic in the gauge fields produce masses: $m_W = gv/2$ and $m_Z = \sqrt{g^2 + g'^2}\, v/2 = m_W/\cos\theta_W$. The three Goldstone modes (would-be massless scalars from the broken $SU(2)$ directions) are absorbed as the longitudinal polarizations of $W^\pm$ and $Z^0$ — the gauge-boson degrees of freedom increase from 2 (transverse) to 3 (transverse + longitudinal) each, accounting for the "eaten" scalars. One real scalar degree of freedom remains: the **Higgs boson $h$**, with mass $m_h = \sqrt{2\mu^2} = \sqrt{2\lambda}\, v$. Fermion masses arise from Yukawa couplings $\mathcal{L}_\text{Yukawa} = -y_f \bar\psi_L \phi \psi_R + \text{h.c.}$, giving $m_f = y_f v/\sqrt2$ after symmetry breaking; the top quark has $y_t \approx 1$.

**演示。** 将 $\phi$ 在极小值附近展开，$\phi = (0, (v + h)/\sqrt2)$，代入规范动能项 $|D_\mu\phi|^2$，规范场的二次项产生质量：$m_W = gv/2$，$m_Z = \sqrt{g^2 + g'^2}\, v/2 = m_W/\cos\theta_W$。三个戈德斯通模式（来自破缺 $SU(2)$ 方向的原本无质量的标量）被吸收为 $W^\pm$ 和 $Z^0$ 的纵向极化——每个规范玻色子的自由度从 2（横向）增加到 3（横向 + 纵向），恰好对应于被"吃掉"的标量。剩下一个实标量自由度：**希格斯玻色子 $h$**，质量为 $m_h = \sqrt{2\mu^2} = \sqrt{2\lambda}\, v$。费米子质量来自汤川耦合 $\mathcal{L}_\text{Yukawa} = -y_f \bar\psi_L \phi \psi_R + \text{h.c.}$，对称性破缺后给出 $m_f = y_f v/\sqrt2$；顶夸克的汤川耦合常数 $y_t \approx 1$。

**Application.** The Higgs boson was discovered at CERN's LHC in 2012 (ATLAS and CMS), with mass $m_h \approx 125$ GeV — a triumph of the Standard Model developed 45 years earlier. Its couplings to $W$, $Z$, and fermions scale with mass exactly as predicted. The Higgs mechanism is the single most elegant cross-link in the curriculum: the same spontaneous-symmetry-breaking mathematics that explains the Meissner effect in a superconductor (Phase 5) explains why the weak force is short-ranged and why all elementary particles have mass.

**应用。** 希格斯玻色子于 2012 年在欧洲核子研究中心大型强子对撞机（ATLAS 和 CMS 实验）上被发现，质量 $m_h \approx 125$ GeV——这是 45 年前建立的标准模型的巨大胜利。它与 $W$、$Z$ 及费米子的耦合随质量的缩放完全符合预言。希格斯机制是课程中最优美的单一交叉联系：同一套自发对称性破缺数学，既解释了超导体中的迈斯纳效应（第 5 阶段），也解释了为何弱力是短程的以及为何所有基本粒子都有质量。

---

## Self-test (blank page)

1. Explain why a non-zero vacuum expectation value $\langle\phi\rangle = v/\sqrt2$ gives masses to the $W^\pm$ and $Z^0$ but leaves the photon massless. Which symmetry is preserved?
2. Draw the Mexican-hat potential. Identify the Goldstone modes and the Higgs direction. Explain where the longitudinal polarizations of the $W$ and $Z$ come from.
3. Write the Yukawa coupling for the top quark and show how it generates a Dirac mass $m_t = y_t v/\sqrt2$. Why is the top mass large compared to the electron mass in this framework?

**自测（空白页）**

1. 解释为何非零真空期望值 $\langle\phi\rangle = v/\sqrt2$ 赋予 $W^\pm$ 和 $Z^0$ 质量而使光子保持无质量。哪个对称性被保留？
2. 画出墨西哥帽势。指出戈德斯通模式和希格斯方向。解释 $W$ 和 $Z$ 的纵向极化从何而来。
3. 写出顶夸克的汤川耦合，并证明它如何产生狄拉克质量 $m_t = y_t v/\sqrt2$。在此框架下，为何顶夸克质量相比电子质量如此之大？

---

← Previous: [Module 8.3 — The Strong Interaction (QCD)](./module-8.3-quantum-chromodynamics.md) · [Phase 8 index](./README.md) · Next: [Module 8.5 — The Standard Model & Beyond](./module-8.5-standard-model-and-beyond.md) →

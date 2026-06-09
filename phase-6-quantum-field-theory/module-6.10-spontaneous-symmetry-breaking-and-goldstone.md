# Module 6.10 — Spontaneous Symmetry Breaking & Goldstone's Theorem
**模块 6.10 — 自发对称性破缺与戈德斯通定理**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.10-spontaneous-symmetry-breaking-and-goldstone-derivations.md)

---

## 1. Spontaneous Symmetry Breaking and the Vacuum · 自发对称性破缺与真空

**Definition.** A symmetry is *spontaneously broken* when the Lagrangian (or Hamiltonian) is invariant under a symmetry group G but the ground state — the vacuum — is not. The dynamics respect the symmetry; the chosen ground state does not. The diagnostic is the *order parameter*: a field whose vacuum expectation value $\langle\varphi\rangle$ would be forced to vanish by the symmetry, but which the dynamics drive to a nonzero value. Take a real scalar with $\mathcal{L} = \tfrac12(\partial\varphi)^2 - V(\varphi)$ and the "wrong-sign mass" potential $V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$ with $\mu^2 > 0$, $\lambda > 0$. This $\mathcal{L}$ is invariant under the discrete reflection $Z_2$: $\varphi \to -\varphi$. The symmetric point $\varphi = 0$ is a *local maximum* of $V$ (since $V''(0) = -\mu^2 < 0$); the minima sit at $\langle\varphi\rangle = v = \pm\sqrt{\mu^2/\lambda}$. The system must pick one of the two degenerate minima, and that choice breaks $Z_2$: the ground state is not symmetric even though $\mathcal{L}$ is. This is the order parameter $\langle\varphi\rangle \neq 0$ of Landau theory (Module 2.3), now realized in a relativistic field theory.

**定义。** 当拉格朗日量（或哈密顿量）在对称群 G 下不变，但基态——真空——不在其下不变时，称对称性被*自发破缺*。动力学尊重对称性；被选中的基态却不。判据是*序参量*：一个本应被对称性强制为零的真空期望值 $\langle\varphi\rangle$，却被动力学驱动到非零值。取实标量 $\mathcal{L} = \tfrac12(\partial\varphi)^2 - V(\varphi)$，势取"错号质量"形式 $V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$，其中 $\mu^2 > 0$，$\lambda > 0$。该 $\mathcal{L}$ 在离散反射 $Z_2$：$\varphi \to -\varphi$ 下不变。对称点 $\varphi = 0$ 是 $V$ 的*局部极大值*（因 $V''(0) = -\mu^2 < 0$）；极小值位于 $\langle\varphi\rangle = v = \pm\sqrt{\mu^2/\lambda}$。系统必须从两个简并极小值中选一个，而这一选择破缺了 $Z_2$：尽管 $\mathcal{L}$ 对称，基态却不对称。这正是朗道理论（模块 2.3）的序参量 $\langle\varphi\rangle \neq 0$，如今在相对论性场论中实现。

**Demonstration.** Minimize $V$: the stationarity condition $V'(\varphi) = -\mu^2\varphi + \lambda\varphi^3 = \varphi(-\mu^2 + \lambda\varphi^2) = 0$ has roots $\varphi = 0$ and $\varphi = \pm\sqrt{\mu^2/\lambda} \equiv \pm v$. The curvature $V''(\varphi) = -\mu^2 + 3\lambda\varphi^2$ is negative at $\varphi = 0$ (a maximum) and positive at $\varphi = v$ (a minimum). Expand the field about a chosen vacuum, $\varphi = v + \eta$, where $\eta$ is the physical fluctuation. Substituting and collecting the quadratic term gives a *positive* mass: the $\eta$ field has $m_\eta^2 = V''(v) = -\mu^2 + 3\lambda v^2 = 2\mu^2 = 2\lambda v^2$. The "tachyonic" $-\mu^2$ of the symmetric phase has turned into a healthy positive mass once we expand about the true vacuum. There is no massless mode here because the broken symmetry $Z_2$ is *discrete*; a flat direction (and hence a massless particle) requires a *continuous* symmetry — the subject of Section 2.

**演示。** 将 $V$ 极小化：稳定性条件 $V'(\varphi) = -\mu^2\varphi + \lambda\varphi^3 = \varphi(-\mu^2 + \lambda\varphi^2) = 0$ 有根 $\varphi = 0$ 和 $\varphi = \pm\sqrt{\mu^2/\lambda} \equiv \pm v$。曲率 $V''(\varphi) = -\mu^2 + 3\lambda\varphi^2$ 在 $\varphi = 0$ 处为负（极大值），在 $\varphi = v$ 处为正（极小值）。围绕选定真空展开场，$\varphi = v + \eta$，其中 $\eta$ 是物理涨落。代入并收集二次项给出*正*质量：$\eta$ 场具有 $m_\eta^2 = V''(v) = -\mu^2 + 3\lambda v^2 = 2\mu^2 = 2\lambda v^2$。对称相中"快子性"的 $-\mu^2$ 一旦围绕真实真空展开就变成了健康的正质量。这里没有无质量模式，因为被破缺的对称性 $Z_2$ 是*离散*的；平坦方向（因而无质量粒子）需要*连续*对称性——这是第 2 节的主题。

**Application.** Spontaneous symmetry breaking is the organizing principle behind nearly every phase transition in physics. A ferromagnet below its Curie temperature picks a magnetization direction, breaking the rotational symmetry of the spin Hamiltonian (Module 4.6); a superconductor breaks the $U(1)$ phase symmetry of the electromagnetic field (Module 5.3); the QCD vacuum breaks chiral symmetry, generating the bulk of the proton mass (Module 8.7); the Higgs field breaks electroweak $SU(2)\times U(1)$, giving masses to the W and Z (Module 8.4). The shape of $V$ here — a symmetric double well in one dimension, a "Mexican hat" in two — is precisely the Landau–Ginzburg free energy of Module 2.3, with $-\mu^2$ playing the role of $(T - T_c)$ below the transition. Coleman's *Aspects of Symmetry* Ch. 5 and Peskin & Schroeder Ch. 11 give the field-theoretic treatment.

**应用。** 自发对称性破缺是物理学中几乎每一个相变背后的组织原则。居里温度以下的铁磁体选定一个磁化方向，破缺自旋哈密顿量的旋转对称性（模块 4.6）；超导体破缺电磁场的 $U(1)$ 相位对称性（模块 5.3）；QCD 真空破缺手征对称性，产生质子质量的大部分（模块 8.7）；希格斯场破缺电弱 $SU(2)\times U(1)$，赋予 W 与 Z 质量（模块 8.4）。这里 $V$ 的形状——一维中的对称双阱、二维中的"墨西哥帽"——正是模块 2.3 的朗道–金兹堡自由能，其中 $-\mu^2$ 在相变以下扮演 $(T - T_c)$ 的角色。Coleman 的 *Aspects of Symmetry* 第 5 章和 Peskin & Schroeder 第 11 章给出场论处理。

---

## 2. Goldstone's Theorem · 戈德斯通定理

**Definition.** When a *continuous* global symmetry is spontaneously broken, **Goldstone's theorem** guarantees a massless particle — a *Goldstone boson* — for every broken generator. The cleanest model is a complex scalar $\varphi$ with a global $U(1)$ symmetry $\varphi \to e^{i\alpha}\varphi$ and $\mathcal{L} = |\partial\varphi|^2 - V$, $V = -\mu^2|\varphi|^2 + \lambda|\varphi|^4$ ($\mu^2 > 0$). The potential is minimized on the whole circle $|\varphi| = v/\sqrt{2}$ with $v = \sqrt{\mu^2/\lambda}$; the vacuum picks one point on the circle, $\langle\varphi\rangle = v/\sqrt{2}$, breaking $U(1)$. Write the field in terms of its radial and angular fluctuations, $\varphi = (v + h)e^{i\theta/v}/\sqrt{2}$ (equivalently $\varphi = (v + h + i\pi)/\sqrt{2}$ to lowest order). The radial mode $h$ climbs the walls of the "Mexican hat" — it is massive — while the angular mode $\theta$ moves *along* the flat valley at the bottom, costing no potential energy: it is exactly massless. That massless $\theta$ (or $\pi$) is the Goldstone boson. The general counting is **# Goldstone bosons $= \dim(G) - \dim(H)$**, where $G$ is the symmetry group of $\mathcal{L}$ and $H \subset G$ is the unbroken subgroup that still leaves the vacuum invariant.

**定义。** 当*连续*整体对称性被自发破缺时，**戈德斯通定理**保证每个被破缺的生成元对应一个无质量粒子——*戈德斯通玻色子*。最简洁的模型是带整体 $U(1)$ 对称性 $\varphi \to e^{i\alpha}\varphi$ 的复标量 $\varphi$，$\mathcal{L} = |\partial\varphi|^2 - V$，$V = -\mu^2|\varphi|^2 + \lambda|\varphi|^4$（$\mu^2 > 0$）。势在整个圆 $|\varphi| = v/\sqrt{2}$ 上极小，$v = \sqrt{\mu^2/\lambda}$；真空选取圆上一点 $\langle\varphi\rangle = v/\sqrt{2}$，破缺 $U(1)$。将场用其径向与角向涨落表示，$\varphi = (v + h)e^{i\theta/v}/\sqrt{2}$（最低阶等价于 $\varphi = (v + h + i\pi)/\sqrt{2}$）。径向模 $h$ 沿"墨西哥帽"的壁攀爬——它有质量——而角向模 $\theta$ 沿底部平坦山谷*运动*，不消耗势能：它严格无质量。那个无质量的 $\theta$（或 $\pi$）就是戈德斯通玻色子。一般计数为 **戈德斯通玻色子数 $= \dim(G) - \dim(H)$**，其中 $G$ 是 $\mathcal{L}$ 的对称群，$H \subset G$ 是仍使真空不变的未破缺子群。

**Demonstration.** Substitute $\varphi = (v + h + i\pi)/\sqrt{2}$ into $V$ and expand: the radial fluctuation acquires $m_h^2 = 2\mu^2 = 2\lambda v^2$ (same massive "Higgs-like" mode as the $\eta$ of Section 1), while the angular fluctuation $\pi$ has *no* quadratic term — $m_\pi^2 = 0$ — because $V$ is exactly constant along the angular direction. This flatness is not an accident: it is enforced by the symmetry. The model-independent proof (Section C of the derivations) uses current algebra: a spontaneously broken continuous symmetry has a Noether current $J^\mu$ with $\partial_\mu J^\mu = 0$ whose charge fails to annihilate the vacuum, $Q|0\rangle \neq 0$. The matrix element of the broken current between the vacuum and a one-particle state is nonzero, $\langle 0|J^\mu(x)|\pi(p)\rangle = i f p^\mu e^{-ip\cdot x}$ with decay constant $f \neq 0$; current conservation $\partial_\mu J^\mu = 0$ then forces $p^2\cdot f = 0$, so $p^2 = 0$ — the state $|\pi(p)\rangle$ is exactly massless. One such massless boson appears for each broken generator, giving the counting $\dim(G) - \dim(H)$.

**演示。** 将 $\varphi = (v + h + i\pi)/\sqrt{2}$ 代入 $V$ 并展开：径向涨落获得 $m_h^2 = 2\mu^2 = 2\lambda v^2$（与第 1 节的 $\eta$ 相同的有质量"类希格斯"模），而角向涨落 $\pi$ *没有*二次项——$m_\pi^2 = 0$——因为 $V$ 沿角向严格为常数。这种平坦性并非偶然：它由对称性强制。与模型无关的证明（推导 C 节）使用流代数：自发破缺的连续对称性有一个满足 $\partial_\mu J^\mu = 0$ 的诺特流 $J^\mu$，其荷不湮灭真空，$Q|0\rangle \neq 0$。被破缺流在真空与单粒子态之间的矩阵元非零，$\langle 0|J^\mu(x)|\pi(p)\rangle = i f p^\mu e^{-ip\cdot x}$，衰变常数 $f \neq 0$；流守恒 $\partial_\mu J^\mu = 0$ 随即强制 $p^2\cdot f = 0$，故 $p^2 = 0$——态 $|\pi(p)\rangle$ 严格无质量。每个被破缺生成元对应一个这样的无质量玻色子，给出计数 $\dim(G) - \dim(H)$。

**Application.** Goldstone bosons appear wherever a continuous symmetry breaks. The pions are the (pseudo-)Goldstone bosons of spontaneously broken chiral $SU(2)\times SU(2) \to SU(2)$ in QCD — light but not exactly massless because the quark masses break chiral symmetry explicitly (Module 8.7). Magnons (spin waves) are the Goldstone modes of the spin-rotation symmetry broken by a ferromagnet or antiferromagnet (Module 4.6); phonons are the Goldstones of broken translational symmetry in a crystal. The theorem has two important caveats: in low dimensions the would-be Goldstone modes fluctuate so violently that they *prevent* symmetry breaking altogether (the Mermin–Wagner theorem, Section D of the derivations), and when the broken symmetry is *gauged* rather than global, the Goldstone boson is eaten by the gauge field and there is no physical massless particle — the Higgs mechanism (Section E; fully derived in Module 8.4).

**应用。** 戈德斯通玻色子出现在任何连续对称性破缺之处。$\pi$ 介子是 QCD 中自发破缺手征 $SU(2)\times SU(2) \to SU(2)$ 的（赝）戈德斯通玻色子——轻但非严格无质量，因为夸克质量显式破缺手征对称性（模块 8.7）。磁振子（自旋波）是铁磁体或反铁磁体破缺的自旋旋转对称性的戈德斯通模（模块 4.6）；声子是晶体中破缺平移对称性的戈德斯通玻色子。该定理有两个重要的限定条件：在低维中，本应的戈德斯通模涨落如此剧烈以至于*完全阻止*对称性破缺（Mermin–Wagner 定理，推导 D 节），而当被破缺的对称性是*规范*的而非整体的时，戈德斯通玻色子被规范场吞噬，不存在物理的无质量粒子——希格斯机制（E 节；在模块 8.4 中完整推导）。

---

## Self-test (blank page) · 自测（空白页）

1. For $V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$ with $\mu^2 > 0$, find the vacuum expectation value $\langle\varphi\rangle$ and the mass of the fluctuation about it. Why is $\varphi = 0$ not the ground state?
2. State Goldstone's theorem precisely. In the complex-scalar $U(1)$ model, which combination of fields is massive and which is the massless Goldstone boson, and why is the angular direction flat?
3. Give the counting rule for the number of Goldstone bosons in a breaking pattern $G \to H$. Apply it to (a) a single complex scalar with $U(1)$, and (b) chiral $SU(2)\times SU(2) \to SU(2)$.
4. Why does no physical massless Goldstone boson appear when the broken symmetry is gauged rather than global? What happens to the degree of freedom instead?

**自测（空白页）**

1. 对 $V(\varphi) = -\tfrac12\mu^2\varphi^2 + \tfrac14\lambda\varphi^4$（$\mu^2 > 0$），求真空期望值 $\langle\varphi\rangle$ 及围绕它的涨落质量。为何 $\varphi = 0$ 不是基态？
2. 精确陈述戈德斯通定理。在复标量 $U(1)$ 模型中，哪个场组合有质量、哪个是无质量戈德斯通玻色子，角向方向为何平坦？
3. 给出破缺模式 $G \to H$ 中戈德斯通玻色子数目的计数规则。将其应用于（a）带 $U(1)$ 的单个复标量，和（b）手征 $SU(2)\times SU(2) \to SU(2)$。
4. 当被破缺的对称性是规范的而非整体的时，为何不出现物理的无质量戈德斯通玻色子？取而代之，该自由度发生了什么？

---

← Previous: [Module 6.9 — Anomalies & Non-Perturbative QFT](./module-6.9-anomalies-and-nonperturbative-qft.md) · [Phase 6 index](./README.md) · Next: [Module 6.11 — Effective Field Theory & the Renormalization Group](./module-6.11-effective-field-theory-and-the-renormalization-group.md) →

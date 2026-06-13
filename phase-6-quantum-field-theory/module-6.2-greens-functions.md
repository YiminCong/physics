# Module 6.2 — Green's Functions & Propagators ⭐
**模块 6.2 — 格林函数与传播子 ⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.2-greens-functions-derivations.md)

---

## 1. The Single-Particle Green's Function · 单粒子格林函数

**Definition.** The retarded single-particle Green's function is $G^R(x,t; x',t') = -i\, \theta(t-t')\, \langle\{\psi(x,t), \psi^\dagger(x',t')\}\rangle$, where $\psi(x,t)$ is the field operator in the Heisenberg picture (Module 3.10), $\theta$ is the Heaviside step, and the average is over the ground state ($T = 0$) or the thermal ensemble. In momentum-frequency space for a translationally invariant system, $G^R(k,\omega)$ encodes everything about single-particle excitations: its poles locate quasiparticle energies, and its imaginary part gives the quasiparticle lifetime.

**定义。** 推迟单粒子格林函数为 $G^R(x,t; x',t') = -i\, \theta(t-t')\, \langle\{\psi(x,t), \psi^\dagger(x',t')\}\rangle$，其中 $\psi(x,t)$ 是海森堡绘景中的场算符（模块 3.10），$\theta$ 是 Heaviside 阶跃函数，平均取自基态（$T = 0$）或热系综。对于平移不变系统，动量-频率空间中的 $G^R(k,\omega)$ 编码了单粒子激发的全部信息：其极点定位准粒子能量，虚部给出准粒子寿命。

For a free Fermi gas, $G^0(k,\omega) = 1/(\omega - \varepsilon_k/\hbar + i\eta)$ where $\eta \to 0^+$ ensures causality (retarded boundary condition). The pole at $\omega = \varepsilon_k/\hbar$ is a sharp quasiparticle. Interactions broaden it: the self-energy $\Sigma(k,\omega)$ (Module 6.3) shifts and smears the pole.

对于自由费米气体，$G^0(k,\omega) = 1/(\omega - \varepsilon_k/\hbar + i\eta)$，其中 $\eta \to 0^+$ 保证因果性（推迟边界条件）。$\omega = \varepsilon_k/\hbar$ 处的极点是一个尖锐准粒子。相互作用使其展宽：自能 $\Sigma(k,\omega)$（模块 6.3）移动并模糊该极点。

**Demonstration.** The spectral function $A(k,\omega) = -(1/\pi)\, \mathrm{Im}\, G^R(k,\omega)$ is a real, positive-definite density of states in $(k,\omega)$ space. For the free gas, $A(k,\omega) = \delta(\omega - \varepsilon_k/\hbar)$: a delta function on the bare dispersion. With interactions, $A(k,\omega)$ acquires a Lorentzian width $\Gamma = \mathrm{Im}\, \Sigma/\hbar$ — the inverse quasiparticle lifetime. The spectral sum rule $\int d\omega\, A(k,\omega) = 1$ (per spin) is exact and provides a consistency check.

**演示。** 谱函数 $A(k,\omega) = -(1/\pi)\, \mathrm{Im}\, G^R(k,\omega)$ 是 $(k,\omega)$ 空间中实的、正定的态密度。对于自由气体，$A(k,\omega) = \delta(\omega - \varepsilon_k/\hbar)$：裸色散关系上的一个 $\delta$ 函数。加入相互作用后，$A(k,\omega)$ 获得洛伦兹宽度 $\Gamma = \mathrm{Im}\, \Sigma/\hbar$——即准粒子寿命的倒数。谱函数求和规则 $\int d\omega\, A(k,\omega) = 1$（每个自旋）是精确的，可作为一致性检验。

The analytic structure follows from causality (Module 0.4): $G^R(k,\omega)$ is analytic in the upper half $\omega$-plane. The Kramers–Kronig relations then link $\mathrm{Re}\, G^R$ and $\mathrm{Im}\, G^R$: $\mathrm{Re}\, G^R(k,\omega) = (1/\pi)\, \mathcal{P} \int d\omega'\, \mathrm{Im}\, G^R(k,\omega')/(\omega'-\omega)$, directly analogous to the dielectric function dispersions encountered in electrodynamics. These relations are a consequence of causality alone, not of any specific model.

解析结构源于因果性（模块 0.4）：$G^R(k,\omega)$ 在 $\omega$ 平面的上半平面解析。克喇末–克朗尼希关系将 $\mathrm{Re}\, G^R$ 与 $\mathrm{Im}\, G^R$ 联系起来：$\mathrm{Re}\, G^R(k,\omega) = (1/\pi)\, \mathcal{P} \int d\omega'\, \mathrm{Im}\, G^R(k,\omega')/(\omega'-\omega)$，与电动力学中遇到的介电函数色散关系直接类比。这些关系仅是因果性的推论，与具体模型无关。

**Application.** Angle-resolved photoemission spectroscopy (ARPES) directly images $A(k,\omega)$: a photon ejects an electron with momentum $k$ and energy $\omega$, and the intensity is proportional to $A(k,\omega)\, f(\omega)$ where $f$ is the Fermi function. ARPES data on cuprate superconductors and Fermi liquids are interpreted almost entirely via $G(k,\omega)$.

**应用。** 角分辨光电子能谱（ARPES）直接成像谱函数 $A(k,\omega)$：一个光子将动量为 $k$、能量为 $\omega$ 的电子弹出，强度正比于 $A(k,\omega)\, f(\omega)$，其中 $f$ 是费米函数。铜氧化物超导体和费米液体的 ARPES 数据几乎完全通过 $G(k,\omega)$ 来解释。

---

## 2. Nambu–Gor'kov Green's Function and BCS · Nambu–Gor'kov 格林函数与 BCS

**Definition.** For a superconductor, a single Green's function is insufficient because the BCS ground state mixes particles and holes via the anomalous average $F(k) = \langle c_{-k\downarrow}c_{k\uparrow}\rangle \neq 0$. Nambu and Gor'kov (following Fetter & Walecka) promote the spinor $\Psi_k = (c_{k\uparrow}, c^\dagger_{-k\downarrow})^T$ and define the $2\times 2$ matrix Green's function $\hat{G}(k,\omega) = -i \langle T \Psi_k(t) \Psi^\dagger_k(0)\rangle$. Its diagonal elements are the normal $G(k,\omega)$, and its off-diagonal elements are the anomalous $F(k,\omega)$ which carry the pairing information.

**定义。** 对于超导体，单个格林函数是不够的，因为 BCS 基态通过反常平均值 $F(k) = \langle c_{-k\downarrow}c_{k\uparrow}\rangle \neq 0$ 将粒子与空穴混合。Nambu 和 Gor'kov（参照 Fetter & Walecka）引入旋量 $\Psi_k = (c_{k\uparrow}, c^\dagger_{-k\downarrow})^T$，并定义 $2\times 2$ 矩阵格林函数 $\hat{G}(k,\omega) = -i \langle T \Psi_k(t) \Psi^\dagger_k(0)\rangle$。其对角元为正常格林函数 $G(k,\omega)$，非对角元为携带配对信息的反常格林函数 $F(k,\omega)$。

**Demonstration.** Inverting the Dyson equation (Module 6.3) in Nambu space gives $\hat{G}(k,\omega) = (\omega - \xi_k \tau_z - \Delta \tau_x)^{-1}$ where $\tau$ are Pauli matrices in particle-hole space, $\xi_k = \varepsilon_k - \mu$, and $\Delta$ is the BCS gap. The poles of $\det \hat{G} = 0$ give $\omega = \pm E_k$, $E_k = \sqrt{\xi^2_k + \Delta^2}$ — the Bogoliubov quasiparticle spectrum derived here from Green's function poles rather than the canonical Bogoliubov transformation.

**演示。** 在 Nambu 空间中对戴森方程（模块 6.3）求逆，得到 $\hat{G}(k,\omega) = (\omega - \xi_k \tau_z - \Delta \tau_x)^{-1}$，其中 $\tau$ 是粒子-空穴空间中的泡利矩阵，$\xi_k = \varepsilon_k - \mu$，$\Delta$ 是 BCS 能隙。$\det \hat{G} = 0$ 的极点给出 $\omega = \pm E_k$，$E_k = \sqrt{\xi^2_k + \Delta^2}$——这里从格林函数极点而非正则 Bogoliubov 变换推导出了 Bogoliubov 准粒子谱。

**Application.** The Nambu–Gor'kov formalism is the foundation of modern superconductivity theory: it allows systematic diagrammatic calculation of $\Delta$ (self-consistently), the density of states $N(\omega) \propto |\omega|/\sqrt{\omega^2-\Delta^2}$ (measured by tunneling spectroscopy), and the response functions needed for transport. It generalizes cleanly to unconventional superconductors (d-wave, etc.) and to Nambu spinors in topological systems.

**应用。** Nambu–Gor'kov 形式主义是现代超导理论的基础：它允许系统地用图的方法自洽地计算 $\Delta$、态密度 $N(\omega) \propto |\omega|/\sqrt{\omega^2-\Delta^2}$（由隧道谱测量）以及输运所需的响应函数。它可以直接推广到非常规超导体（d 波等）和拓扑系统中的 Nambu 旋量。

## Key results · 核心结果

- $G^0(k,\omega) = \dfrac{1}{\omega - \varepsilon_k/\hbar + i\eta}$ — free propagator; poles give excitation energies · 自由格林函数,极点即激发能
- The spectral function $A(k,\omega)$ encodes the measurable excitation spectrum · 谱函数给出可测激发谱
- Self-energy $\Sigma$ dresses bare particles into quasiparticles · 自能将裸粒子修饰为准粒子
- Nambu–Gor'kov anomalous propagator encodes BCS pairing · Nambu–Gor'kov 反常传播子编码 BCS 配对

---

## Self-test (blank page) · 自测（空白页）

1. Write down $G^0(k,\omega)$ for a free Fermi gas. Where are its poles? How does switching on an interaction $\Sigma(k,\omega)$ move or broaden them?
2. State the Kramers–Kronig relation for $G^R(k,\omega)$ and explain which physical principle it encodes.
3. What is the anomalous Green's function $F(k,\omega)$ and why is it zero in a normal metal but nonzero in a BCS superconductor?

**自测（空白页）**

1. 写出自由费米气体的 $G^0(k,\omega)$。其极点在哪里？引入相互作用 $\Sigma(k,\omega)$ 后，极点如何移动或展宽？
2. 陈述 $G^R(k,\omega)$ 的克喇末–克朗尼希关系，并解释它编码了哪条物理原理。
3. 反常格林函数 $F(k,\omega)$ 是什么？为什么它在正常金属中为零，而在 BCS 超导体中不为零？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $G^0(k,\omega)=\dfrac1{\omega-\varepsilon_k/\hbar+i\eta}$, a sharp pole at $\omega=\varepsilon_k/\hbar$. An interaction $\Sigma$ shifts the pole to $\omega=\varepsilon_k/\hbar+\text{Re}\,\Sigma$ (renormalized energy) and broadens it by $\text{Im}\,\Sigma$ (finite quasiparticle lifetime). · 极点在 $\omega=\varepsilon_k/\hbar$;自能移动并展宽之。

**2.** $\text{Re}\,G^R(\omega)=\dfrac1\pi\mathcal P\!\int\dfrac{\text{Im}\,G^R(\omega')}{\omega'-\omega}d\omega'$. It encodes **causality** ($G^R$ is analytic in the upper half-plane: no response before the cause). · 克喇末–克朗尼希关系编码因果性。

**3.** $F(k,\omega)\sim\langle T\,c_{k\uparrow}c_{-k\downarrow}\rangle$ is the anomalous propagator. It vanishes in a normal metal (particle number conserved, $\langle cc\rangle=0$) but is nonzero in BCS, where the condensate breaks $U(1)$ and $\langle cc\rangle\neq0$. · 反常格林函数在正常金属为零,BCS 中非零(破缺 $U(1)$)。

</details>

---

← Previous: [Module 6.1 — Second Quantization & the Many-Body Problem](./module-6.1-second-quantization.md) · [Phase 6 index](./README.md) · Next: [Module 6.3 — Feynman Diagrams & Perturbation Theory](./module-6.3-feynman-diagrams.md) →

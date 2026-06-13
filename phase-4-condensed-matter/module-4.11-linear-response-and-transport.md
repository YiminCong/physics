# Module 4.11 — Linear Response, Transport & the Kubo Formula
**模块 4.11 — 线性响应、输运与久保公式**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.11-linear-response-and-transport-derivations.md)

---

## 1. Semiclassical Transport: the Boltzmann Equation & Drude Conductivity · 半经典输运：玻尔兹曼方程与德鲁德电导率

**Definition.** Charge transport in a metal is governed by the non-equilibrium electron distribution $f(\mathbf{r}, \mathbf{k}, t)$. Its evolution obeys the **Boltzmann transport equation (BTE)**:

$$ \frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla_r f + \frac{\mathbf{F}}{\hbar}\cdot\nabla_k f = \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} $$

where $\mathbf{v} = (1/\hbar)\nabla_k \varepsilon$ is the band velocity, $\mathbf{F} = -e\mathbf{E}$ the electromagnetic force, and the right-hand side is the collision integral. In the **relaxation-time approximation (RTA)** the collisions drive $f$ back to local equilibrium $f_0$ on a timescale $\tau$:

$$ \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} = -\frac{f - f_0}{\tau}. $$

This single phenomenological time $\tau$ encapsulates all scattering (impurities, phonons, other electrons). It builds on the kinetic-theory framework of Module 2.7 and the Drude/Sommerfeld picture of Module 4.1.

**定义。** 金属中的电荷输运由非平衡电子分布 $f(\mathbf{r}, \mathbf{k}, t)$ 支配。其演化服从**玻尔兹曼输运方程（BTE）**：

$$ \frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla_r f + \frac{\mathbf{F}}{\hbar}\cdot\nabla_k f = \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} $$

其中 $\mathbf{v} = (1/\hbar)\nabla_k \varepsilon$ 为能带速度，$\mathbf{F} = -e\mathbf{E}$ 为电磁力，右端为碰撞积分。在**弛豫时间近似（RTA）**中，碰撞以时间标度 $\tau$ 将 $f$ 驱回局域平衡 $f_0$：

$$ \left(\frac{\partial f}{\partial t}\right)_{\text{coll}} = -\frac{f - f_0}{\tau}. $$

这个唯象时间 $\tau$ 概括了所有散射（杂质、声子、其他电子）。它建立在模块 2.7 的动理论框架以及模块 4.1 的德鲁德/索末菲图像之上。

**Demonstration.** For a static, uniform electric field $\mathbf{E}$ and a spatially homogeneous, steady state ($\partial f/\partial t = 0$, $\nabla_r f = 0$), the BTE collapses to $(-e\mathbf{E}/\hbar)\cdot\nabla_k f = -(f - f_0)/\tau$. Linearizing $f = f_0 + \delta f$ and noting $\nabla_k f_0 = \hbar\mathbf{v}(\partial f_0/\partial\varepsilon)$, the deviation is (see Derivations A)

$$ \delta f = -e\tau\,(\mathbf{E}\cdot\mathbf{v})\,(\partial f_0/\partial\varepsilon). $$

Because $-\partial f_0/\partial\varepsilon$ is sharply peaked at the Fermi energy $E_F$, **only electrons within $\sim k_B T$ of the Fermi surface contribute** — the key correction Sommerfeld made to Drude's classical picture. The current density follows by summing the group velocity over occupied states, $\mathbf{J} = -e \int(d^3k/4\pi^3)\,\mathbf{v}\,\delta f$, which yields the **Drude–Sommerfeld conductivity**

$$ \sigma = \frac{n e^2 \tau}{m}, \qquad \text{with mobility } \mu = \frac{e\tau}{m}, \qquad \mathbf{J} = \sigma\mathbf{E}. $$

**演示。** 对于静态、均匀电场 $\mathbf{E}$ 及空间均匀的稳态（$\partial f/\partial t = 0$，$\nabla_r f = 0$），BTE 化为 $(-e\mathbf{E}/\hbar)\cdot\nabla_k f = -(f - f_0)/\tau$。线性化 $f = f_0 + \delta f$ 并注意 $\nabla_k f_0 = \hbar\mathbf{v}(\partial f_0/\partial\varepsilon)$，偏离量为（见推导 A）

$$ \delta f = -e\tau\,(\mathbf{E}\cdot\mathbf{v})\,(\partial f_0/\partial\varepsilon). $$

由于 $-\partial f_0/\partial\varepsilon$ 在费米能 $E_F$ 处尖锐峰化，**只有费米面附近 $\sim k_B T$ 范围内的电子才有贡献**——这是索末菲对德鲁德经典图像所作的关键修正。电流密度由群速度对占据态求和得到，$\mathbf{J} = -e \int(d^3k/4\pi^3)\,\mathbf{v}\,\delta f$，给出**德鲁德–索末菲电导率**

$$ \sigma = \frac{n e^2 \tau}{m}, \qquad \text{迁移率 } \mu = \frac{e\tau}{m}, \qquad \mathbf{J} = \sigma\mathbf{E}. $$

**Application — resistivity, the mean free path, and the Hall effect.** Resistivity $\rho = 1/\sigma = m/(ne^2\tau)$; measuring $\rho(T)$ yields $\tau(T)$ and the **mean free path** $\ell = v_F \tau$. In a magnetic field the velocity term acquires the Lorentz force, and solving the BTE gives the Hall coefficient $R_H = -1/(ne)$, a standard probe of carrier density and sign. The same $\tau$ governs the optical (AC) response $\sigma(\omega) = \sigma_0/(1 - i\omega\tau)$, the Drude peak observed in reflectivity. This semiclassical scheme underpins device modeling in Module 9.1.

**应用——电阻率、平均自由程与霍尔效应。** 电阻率 $\rho = 1/\sigma = m/(ne^2\tau)$；测量 $\rho(T)$ 给出 $\tau(T)$ 及**平均自由程** $\ell = v_F \tau$。在磁场中速度项引入洛伦兹力，求解 BTE 给出霍尔系数 $R_H = -1/(ne)$，是载流子密度和符号的标准探针。同一 $\tau$ 还支配光学（交流）响应 $\sigma(\omega) = \sigma_0/(1 - i\omega\tau)$，即反射率中观测到的德鲁德峰。此半经典方案支撑模块 9.1 中的器件建模。

---

## 2. The Kubo Formula & Fluctuation–Dissipation · 久保公式与涨落–耗散

**Definition.** Linear response asks: given a weak perturbation $H'(t) = -\int d^3r\,\mathbf{J}\cdot\mathbf{A}(t)$ coupling the current $\mathbf{J}$ to an external vector potential $\mathbf{A}$, what is the induced current to first order? The exact quantum answer is the **Kubo formula**, expressing a transport coefficient as an equilibrium correlation function of the operator it couples to. For the conductivity, the response is the current–current correlation function evaluated in the *unperturbed* equilibrium ensemble. No relaxation time is assumed: $\tau$ emerges only when scattering is put in by hand.

**定义。** 线性响应问的是：给定弱微扰 $H'(t) = -\int d^3r\,\mathbf{J}\cdot\mathbf{A}(t)$，将电流 $\mathbf{J}$ 与外部矢势 $\mathbf{A}$ 耦合，一阶诱导电流是多少？精确的量子答案是**久保公式**，它将输运系数表示为所耦合算符在平衡态下的关联函数。对电导率而言，响应即在*未微扰*平衡系综中求得的电流–电流关联函数。其中不假设弛豫时间：只有人为引入散射时 $\tau$ 才出现。

**Demonstration.** First-order time-dependent perturbation theory (interaction picture) gives the induced expectation value of an operator $A$ as $\langle\delta A(t)\rangle = (i/\hbar)\int_{-\infty}^{t} dt'\,\langle[H'(t'), A(t)]\rangle_0$ (see Derivations B). Specializing to current response and extracting the conductivity tensor yields the **Kubo formula**

$$ \sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega V} \int_0^\infty dt\, e^{i\omega t}\, \langle[J_\alpha(t), J_\beta(0)]\rangle $$

(the retarded current–current correlation function, with operators evolving under the unperturbed Hamiltonian and the average over the equilibrium ensemble). Equivalently it is written via the retarded correlator $\Pi_{\alpha\beta}^R(\omega)$ as $\sigma_{\alpha\beta}(\omega) = \Pi_{\alpha\beta}^R(\omega)/(i\omega)$. The imaginary part of the correlator — i.e. $\operatorname{Re}\sigma$, the dissipative part — is fixed by the equilibrium current fluctuations, the content of the **fluctuation–dissipation theorem**: dissipation in a driven system is determined by the spontaneous fluctuations of the same system at equilibrium.

**演示。** 一阶含时微扰论（相互作用绘景）给出算符 $A$ 的诱导期望值 $\langle\delta A(t)\rangle = (i/\hbar)\int_{-\infty}^{t} dt'\,\langle[H'(t'), A(t)]\rangle_0$（见推导 B）。特化到电流响应并提取电导率张量，给出**久保公式**

$$ \sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega V} \int_0^\infty dt\, e^{i\omega t}\, \langle[J_\alpha(t), J_\beta(0)]\rangle $$

（推迟电流–电流关联函数，算符在未微扰哈密顿量下演化，并对平衡系综取平均）。等价地可用推迟关联子 $\Pi_{\alpha\beta}^R(\omega)$ 写为 $\sigma_{\alpha\beta}(\omega) = \Pi_{\alpha\beta}^R(\omega)/(i\omega)$。关联子的虚部——即 $\operatorname{Re}\sigma$，耗散部分——由平衡电流涨落确定，这正是**涨落–耗散定理**的内容：受驱系统中的耗散由该系统在平衡时的自发涨落决定。

**Application — why Kubo matters.** The Kubo formula is exact and microscopic: it requires no quasiparticles, no $\tau$, and applies to disordered, interacting, and strongly correlated systems where Boltzmann theory fails. It is the starting point for diagrammatic conductivity calculations (the bubble diagram plus vertex corrections), for the quantized Hall conductance of Modules 4.8/4.9 (where $\sigma_{xy}$ becomes a topological invariant), and for the Fermi-liquid transport of Module 4.10. Whenever a clean derivation of a transport coefficient is needed, one starts from Kubo and recovers Drude as the weak-scattering limit.

**应用——久保公式的重要性。** 久保公式是精确且微观的：它不需要准粒子、不需要 $\tau$，并适用于玻尔兹曼理论失效的无序、相互作用及强关联系统。它是图解电导率计算（泡泡图加顶角修正）的出发点，是模块 4.8/4.9 量子化霍尔电导（其中 $\sigma_{xy}$ 成为拓扑不变量）的基础，也用于模块 4.10 的费米液体输运。每当需要对输运系数作干净推导时，都从久保公式出发，并在弱散射极限下恢复德鲁德结果。

---

## 3. Einstein Relation, Thermoelectricity & Localization · 爱因斯坦关系、热电效应与局域化

**Definition.** Conduction can be viewed as diffusion of charge down a gradient. The **Einstein relation** connects the conductivity to the diffusion constant $D$ and the density of states at the Fermi level $N(E_F)$:

$$ \sigma = e^2\, N(E_F)\, D. $$

With the diffusion constant $D = v_F^2 \tau / d$ in $d$ dimensions, this reproduces the Drude form (Derivations C), and is the microscopic content of the Nyquist/fluctuation–dissipation relation between conductance and thermal noise. Thermal and electrical transport are coupled: an electric field and a temperature gradient both drive charge and heat currents, defining electrical conductivity $\sigma$, thermal conductivity $\kappa$, and thermoelectric (Seebeck) coefficient $S$.

**定义。** 传导可视为电荷沿梯度的扩散。**爱因斯坦关系**将电导率与扩散常数 $D$ 及费米能级态密度 $N(E_F)$ 联系起来：

$$ \sigma = e^2\, N(E_F)\, D. $$

取 $d$ 维下的扩散常数 $D = v_F^2 \tau / d$，这重现德鲁德形式（推导 C），并且是电导与热噪声之间奈奎斯特/涨落–耗散关系的微观内容。热输运与电输运是耦合的：电场与温度梯度都驱动电荷流与热流，定义了电导率 $\sigma$、热导率 $\kappa$ 及热电（塞贝克）系数 $S$。

**Demonstration — the Wiedemann–Franz law.** Solving the coupled Boltzmann equations for a degenerate electron gas and applying the Sommerfeld expansion (Derivations D), the electronic thermal conductivity is $\kappa = (\pi^2/3)(k_B^2 T/e^2)\sigma$. The ratio of thermal to electrical conductivity is therefore universal — independent of $\tau$, $n$, and material details:

$$ \frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \equiv L_0 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}. $$

This is the **Wiedemann–Franz law**, with $L_0$ the **Lorenz number**. It holds because the *same* electrons, scattered by the *same* mechanism, carry both charge and heat. The Seebeck coefficient follows from the energy-dependence of $\sigma$ via the **Mott formula** $S = -(\pi^2/3)(k_B^2 T/e)\,(d\ln\sigma(\varepsilon)/d\varepsilon)|_{E_F}$, vanishing linearly as $T \to 0$.

**演示——维德曼–弗兰兹定律。** 对简并电子气求解耦合玻尔兹曼方程并应用索末菲展开（推导 D），电子热导率为 $\kappa = (\pi^2/3)(k_B^2 T/e^2)\sigma$。因此热导率与电导率之比是普适的——与 $\tau$、$n$ 及材料细节无关：

$$ \frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \equiv L_0 \approx 2.44 \times 10^{-8}\ \text{W}\,\Omega\,\text{K}^{-2}. $$

这就是**维德曼–弗兰兹定律**，$L_0$ 为**洛伦兹数**。它成立的原因是*同样的*电子、被*同样的*机制散射，同时携带电荷与热量。塞贝克系数由 $\sigma$ 对能量的依赖通过**莫特公式** $S = -(\pi^2/3)(k_B^2 T/e)\,(d\ln\sigma(\varepsilon)/d\varepsilon)|_{E_F}$ 给出，随 $T \to 0$ 线性趋零。

**Application — disorder, residual resistivity & Anderson localization.** Independent scattering channels add their rates: $1/\tau = 1/\tau_{\text{imp}} + 1/\tau_{\text{phonon}} + \ldots$, so resistivities add — **Matthiessen's rule** $\rho = \rho_{\text{imp}} + \rho_{\text{phonon}}(T)$. Impurities give a temperature-independent **residual resistivity** $\rho_{\text{imp}}$ surviving as $T \to 0$. Strong disorder, however, breaks the semiclassical picture entirely: quantum interference of scattered electron waves can halt diffusion. The **scaling theory of localization** predicts that in **$d \leq 2$ all states localize** for any nonzero disorder (no true metal), while in **$d = 3$ a mobility edge** separates extended (metallic) from localized (insulating) states — the **Anderson metal–insulator transition**. Even in the weakly disordered metal, coherent backscattering produces the **weak-localization** quantum correction $\Delta\sigma < 0$, a precursor of localization measurable in magnetoresistance. This connects scattering (Module 4.5) and Fermi-liquid theory (Module 4.10) to the breakdown of conventional transport.

**应用——无序、剩余电阻率与安德森局域化。** 独立散射道的速率相加：$1/\tau = 1/\tau_{\text{imp}} + 1/\tau_{\text{phonon}} + \ldots$，故电阻率相加——**马蒂森定则** $\rho = \rho_{\text{imp}} + \rho_{\text{phonon}}(T)$。杂质给出与温度无关的**剩余电阻率** $\rho_{\text{imp}}$，在 $T \to 0$ 时残留。然而强无序会彻底破坏半经典图像：散射电子波的量子干涉可使扩散停止。**局域化标度理论**预言，在 **$d \leq 2$ 中任意非零无序下所有态都局域化**（无真正金属），而在 **$d = 3$ 中存在迁移率边**，将扩展（金属）态与局域（绝缘）态分开——即**安德森金属–绝缘体转变**。即便在弱无序金属中，相干背散射也产生 **弱局域化**量子修正 $\Delta\sigma < 0$，是可在磁电阻中测量的局域化先兆。这将散射（模块 4.5）与费米液体理论（模块 4.10）同常规输运的崩溃联系起来。

## Key results · 核心结果

- Boltzmann equation + relaxation time; $\delta f=-e\tau(\mathbf E\cdot\mathbf v)\partial f_0/\partial\varepsilon$ · 玻尔兹曼方程与弛豫时间
- Drude $\sigma=ne^2\tau/m$, mobility $\mu=e\tau/m$ · 德鲁德电导率
- Kubo: $\sigma$ from a current–current correlation (fluctuation–dissipation) · 久保公式
- Wiedemann–Franz $\kappa/\sigma T=L_0=\pi^2 k_B^2/3e^2$ · 维德曼–弗兰兹定律

---

**Self-test (blank page)**

1. Write the Boltzmann transport equation and the relaxation-time approximation. Linearize it for a static uniform field and derive $\sigma = ne^2\tau/m$, explaining why only electrons near $E_F$ contribute.
2. State the Kubo formula for the conductivity as a current–current correlation function. What does the fluctuation–dissipation theorem say about $\operatorname{Re}\sigma$?
3. State the Einstein relation $\sigma = e^2 N(E_F)D$ and use $D = v_F^2\tau/d$ to recover the Drude conductivity in three dimensions.
4. State and physically justify the Wiedemann–Franz law; give the value of the Lorenz number $L_0$ and explain its universality.

**自测（空白页）**

1. 写出玻尔兹曼输运方程与弛豫时间近似。对静态均匀场将其线性化并推导 $\sigma = ne^2\tau/m$，解释为何只有 $E_F$ 附近的电子才有贡献。
2. 写出电导率作为电流–电流关联函数的久保公式。涨落–耗散定理对 $\operatorname{Re}\sigma$ 有何陈述？
3. 写出爱因斯坦关系 $\sigma = e^2 N(E_F)D$，并用 $D = v_F^2\tau/d$ 恢复三维中的德鲁德电导率。
4. 陈述并从物理上论证维德曼–弗兰兹定律；给出洛伦兹数 $L_0$ 的数值并解释其普适性。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $\partial_t f+\mathbf v\cdot\nabla_r f+\tfrac{\mathbf F}{\hbar}\cdot\nabla_k f=-(f-f_0)/\tau$. Static uniform field: $\delta f=-e\tau(\mathbf E\cdot\mathbf v)\partial f_0/\partial\varepsilon$, and $\mathbf J=-e\int\mathbf v\,\delta f$ gives $\sigma=ne^2\tau/m$. Only $E_F$ electrons contribute since $\partial f_0/\partial\varepsilon\approx-\delta(\varepsilon-E_F)$. · 线性化得 $\sigma=ne^2\tau/m$。
**2.** Kubo: $\sigma\sim\int\langle J(t)J(0)\rangle\,dt$. Fluctuation–dissipation: $\text{Re}\,\sigma$ (dissipation) is fixed by the equilibrium current-fluctuation spectrum. · 久保:电导=电流关联;涨落–耗散。
**3.** Einstein $\sigma=e^2 N(E_F)D$ with $D=v_F^2\tau/3$ (3D) recovers $\sigma=ne^2\tau/m$. · 爱因斯坦关系回到德鲁德。
**4.** Wiedemann–Franz $\kappa/\sigma T=L_0=\pi^2 k_B^2/3e^2\approx2.44\times10^{-8}\ \text{W}\,\Omega/\text{K}^2$ — universal because the same electrons carry both charge and heat, so $\tau$ cancels. · WF 定律,$L_0$ 普适($\tau$ 相消)。

</details>

---

← Previous: [Module 4.10 — Landau Fermi-Liquid Theory](./module-4.10-landau-fermi-liquid-theory.md) · [Phase 4 index](./README.md) · Next: [Module 4.12 — The Hubbard Model & Mott Insulators](./module-4.12-hubbard-model-and-mott-insulators.md) →

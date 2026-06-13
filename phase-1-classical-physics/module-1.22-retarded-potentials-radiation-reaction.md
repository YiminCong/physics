# Module 1.22 — Retarded Potentials, Multipole Radiation & Radiation Reaction
**模块 1.22 — 推迟势、多极辐射与辐射阻尼**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.22-retarded-potentials-radiation-reaction-derivations.md)

---

## 1. Retarded Potentials & the Liénard–Wiechert Fields · 推迟势与李纳–维谢尔场

**Definition.** In the **Lorenz gauge** $\partial_\mu A^\mu = 0$ (Module 1.15), Maxwell's equations (Module 1.10) collapse to two decoupled wave equations $\Box\varphi = -\rho/\varepsilon_0$, $\Box\mathbf{A} = -\mu_0\mathbf{J}$. Their causal solutions are the **retarded potentials**: each source element contributes at the **retarded time** $t_r = t - |\mathbf{r} - \mathbf{r}'|/c$, the instant a light signal must leave $\mathbf{r}'$ to arrive at $\mathbf{r}$ at time $t$. For a single point charge $q$ on a trajectory $\mathbf{w}(t)$, evaluating these integrals gives the **Liénard–Wiechert potentials** $\varphi = (1/4\pi\varepsilon_0)\, q/[\kappa R]_\text{ret}$, $\mathbf{A} = (\boldsymbol{\beta}/c)\varphi$, where $R = |\mathbf{r} - \mathbf{w}(t_r)|$, $\mathbf{n} = (\mathbf{r} - \mathbf{w})/R$, $\boldsymbol{\beta} = \mathbf{v}/c$, and $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$.

**定义。** 在**洛伦兹规范** $\partial_\mu A^\mu = 0$（模块 1.15）下，麦克斯韦方程（模块 1.10）退化为两个解耦的波动方程 $\Box\varphi = -\rho/\varepsilon_0$，$\Box\mathbf{A} = -\mu_0\mathbf{J}$。它们的因果解是**推迟势**：每个源元在**推迟时刻** $t_r = t - |\mathbf{r} - \mathbf{r}'|/c$ 作出贡献，即光信号必须从 $\mathbf{r}'$ 出发以在 $t$ 时刻到达 $\mathbf{r}$ 的那一瞬间。对沿轨迹 $\mathbf{w}(t)$ 运动的单个点电荷 $q$，计算这些积分给出**李纳–维谢尔势** $\varphi = (1/4\pi\varepsilon_0)\, q/[\kappa R]_\text{ret}$，$\mathbf{A} = (\boldsymbol{\beta}/c)\varphi$，其中 $R = |\mathbf{r} - \mathbf{w}(t_r)|$，$\mathbf{n} = (\mathbf{r} - \mathbf{w})/R$，$\boldsymbol{\beta} = \mathbf{v}/c$，$\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$。

**Demonstration.** The factor $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ is the heart of the result: as a source moves toward the field point, the retarded volume of charge "seen" at one instant is compressed (the searchlight/Doppler effect), enhancing the potential by $1/\kappa$. A charge moving directly at the observer ($\mathbf{n}\cdot\boldsymbol{\beta} \to 1$) produces a potential that diverges as $\kappa \to 0$ — the same compression that beams synchrotron radiation forward.

**演示。** 因子 $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ 是结果的核心：当源向场点运动时，某一瞬间"看到"的推迟电荷体积被压缩（探照灯/多普勒效应），使势增强 $1/\kappa$ 倍。直接朝观察者运动的电荷（$\mathbf{n}\cdot\boldsymbol{\beta} \to 1$）产生的势在 $\kappa \to 0$ 时发散——正是这种压缩使同步辐射前向聚束。

**Application.** Retarded potentials are the working tool for every radiation calculation — antennas, synchrotrons, pulsars. The Liénard–Wiechert potentials give the *exact* fields of an arbitrarily moving point charge and are the starting point for relativistic beam physics and for the radiation reaction of Section 3.

**应用。** 推迟势是每个辐射计算的实用工具——天线、同步加速器、脉冲星。李纳–维谢尔势给出任意运动点电荷的*精确*场，是相对论性束流物理以及第 3 节辐射阻尼的出发点。

## 2. Electric-Dipole Radiation · 电偶极辐射

**Definition.** A localized, slowly varying source is characterized by its **electric dipole moment** $\mathbf{p}(t) = \int \mathbf{r}'\, \rho(\mathbf{r}', t)\, d^3r'$. To leading order in the multipole expansion, the radiation fields are those of an oscillating dipole, and the **angular power** is $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c) \sin^2\theta$ ($\theta$ measured from the dipole axis), integrating to the total radiated power $P = \mu_0 \ddot{p}^2/(6\pi c) = \ddot{p}^2/(6\pi\varepsilon_0 c^3)$.

**定义。** 局域、缓变的源由其**电偶极矩** $\mathbf{p}(t) = \int \mathbf{r}'\, \rho(\mathbf{r}', t)\, d^3r'$ 刻画。在多极展开的领头阶，辐射场即振荡偶极子的场，**角功率**为 $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c) \sin^2\theta$（$\theta$ 从偶极轴量起），积分给出总辐射功率 $P = \mu_0 \ddot{p}^2/(6\pi c) = \ddot{p}^2/(6\pi\varepsilon_0 c^3)$。

**Demonstration.** For a single charge with $\mathbf{p} = q\mathbf{d}$, one has $\ddot{\mathbf{p}} = q\ddot{\mathbf{d}} = q\mathbf{a}$, so the dipole formula reduces to $P = \mu_0 q^2 a^2/(6\pi c)$ — exactly the **Larmor formula** derived in Module 1.11. The dipole formula is thus the general (extended-source) form of Larmor's result, with the same $\sin^2\theta$ doughnut pattern: no radiation along the oscillation axis, maximum broadside.

**演示。** 对单个电荷 $\mathbf{p} = q\mathbf{d}$，有 $\ddot{\mathbf{p}} = q\ddot{\mathbf{d}} = q\mathbf{a}$，故偶极公式退化为 $P = \mu_0 q^2 a^2/(6\pi c)$——正是模块 1.11 推导的**拉莫尔公式**。偶极公式因此是拉莫尔结果的一般（扩展源）形式，具有相同的 $\sin^2\theta$ 甜甜圈方向图：沿振荡轴无辐射，垂直方向最大。

**Application.** Electric-dipole radiation governs antennas, atomic/molecular emission (dipole selection rules), and Rayleigh scattering — the $\ddot{p}^2 \propto \omega^4$ scaling is why the sky is blue. Higher multipoles (magnetic dipole, electric quadrupole) appear when the dipole moment vanishes or is forbidden, and dominate forbidden atomic transitions.

**应用。** 电偶极辐射支配天线、原子/分子发射（偶极选择定则）与瑞利散射——$\ddot{p}^2 \propto \omega^4$ 标度正是天空呈蓝色的原因。当偶极矩为零或被禁戒时出现高阶多极（磁偶极、电四极），并主导原子的禁戒跃迁。

## 3. Radiation Reaction (Abraham–Lorentz) · 辐射阻尼（阿布拉罕–洛伦兹）

**Definition.** A radiating charge loses energy to its field, so it must feel a recoil **self-force**. Energy balance over a period gives the **Abraham–Lorentz force** $\mathbf{F}_\text{rad} = (\mu_0 q^2/6\pi c)\, \dot{\mathbf{a}} = (q^2/6\pi\varepsilon_0 c^3)\, \dot{\mathbf{a}}$, proportional to the *jerk* $\dot{\mathbf{a}}$ (the rate of change of acceleration). The associated **characteristic time** is $\tau = \mu_0 q^2/(6\pi m c) = q^2/(6\pi\varepsilon_0 m c^3)$, an extraordinarily short time ($\approx 6 \times 10^{-24}$ s for an electron).

**定义。** 辐射电荷将能量损失给其场，故必感受到反冲**自力**。对一个周期的能量平衡给出**阿布拉罕–洛伦兹力** $\mathbf{F}_\text{rad} = (\mu_0 q^2/6\pi c)\, \dot{\mathbf{a}} = (q^2/6\pi\varepsilon_0 c^3)\, \dot{\mathbf{a}}$，正比于*加加速度*（急动度）$\dot{\mathbf{a}}$（加速度的变化率）。相应的**特征时间**为 $\tau = \mu_0 q^2/(6\pi m c) = q^2/(6\pi\varepsilon_0 m c^3)$，是极短的时间（电子约 $6 \times 10^{-24}$ s）。

**Demonstration.** The force is fixed by demanding that the work it does over a cycle equal minus the Larmor energy radiated: $\int \mathbf{F}_\text{rad}\cdot\mathbf{v}\, dt = -\int (\mu_0 q^2 a^2/6\pi c)\, dt$. An integration by parts converts $a^2$ into $-\dot{\mathbf{a}}\cdot\mathbf{v}$ (boundary terms vanishing for periodic motion), forcing $\mathbf{F}_\text{rad} \propto \dot{\mathbf{a}}$. The equation of motion $m\dot{\mathbf{v}} = \mathbf{F}_\text{ext} + m\tau\dot{\mathbf{a}}$ admits unphysical **runaway** solutions ($a \propto e^{t/\tau}$) and **pre-acceleration** — symptoms that the classical point charge is an idealization repaired only by QED.

**演示。** 该力由要求其一个周期内做的功等于拉莫尔辐射能量的负值确定：$\int \mathbf{F}_\text{rad}\cdot\mathbf{v}\, dt = -\int (\mu_0 q^2 a^2/6\pi c)\, dt$。分部积分将 $a^2$ 转化为 $-\dot{\mathbf{a}}\cdot\mathbf{v}$（周期运动的边界项消失），迫使 $\mathbf{F}_\text{rad} \propto \dot{\mathbf{a}}$。运动方程 $m\dot{\mathbf{v}} = \mathbf{F}_\text{ext} + m\tau\dot{\mathbf{a}}$ 容许非物理的**失控**解（$a \propto e^{t/\tau}$）与**预加速**——表明经典点电荷是一种理想化，只有量子电动力学才能修复。

**Application.** Radiation reaction sets the damping of driven oscillators (natural linewidth of spectral lines), limits the energy of charges in storage rings and lasers, and matters in ultra-intense laser–electron interactions. Conceptually it is the classical shadow of the electron **self-energy**, treated consistently only in QED (Modules 8.2 / 6.x), where the divergences are absorbed by renormalization.

**应用。** 辐射阻尼设定受驱振子的阻尼（谱线的自然线宽），限制储存环与激光中电荷的能量，并在超强激光–电子相互作用中至关重要。概念上它是电子**自能**的经典影子，只有在量子电动力学（模块 8.2 / 6.x）中才能自洽处理，其中发散通过重整化被吸收。

## Key results · 核心结果

- Retarded potentials evaluated at $t_r=t-|\mathbf r-\mathbf r'|/c$ · 推迟势
- Liénard–Wiechert potentials; the $\kappa=1-\mathbf n\cdot\boldsymbol\beta$ factor · 李纳–维谢尔势
- Dipole radiation power → Larmor formula · 偶极辐射→拉莫尔
- Abraham–Lorentz force $\mathbf F=m\tau\dot{\mathbf a}$, $\tau=q^2/6\pi\epsilon_0 mc^3$ · 阿布拉罕–洛伦兹力

---

**Self-test (blank page)**

1. Write down the retarded potentials and explain the meaning of the retarded time $t_r$; why is the *advanced* solution discarded?
2. Derive the $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ factor in the Liénard–Wiechert potentials and explain its physical origin.
3. Starting from $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c) \sin^2\theta$, integrate to get the total dipole power, and show it reduces to the Larmor formula for $\mathbf{p} = q\mathbf{d}$.
4. State the Abraham–Lorentz force, derive it from energy balance, and explain the runaway/pre-acceleration pathologies and the value of $\tau$.

**自测（空白页）**

1. 写出推迟势并解释推迟时刻 $t_r$ 的含义；为何舍弃*超前*解？
2. 推导李纳–维谢尔势中的 $\kappa = 1 - \mathbf{n}\cdot\boldsymbol{\beta}$ 因子，并解释其物理起源。
3. 从 $dP/d\Omega = (\mu_0 \ddot{p}^2/16\pi^2 c) \sin^2\theta$ 出发积分得到偶极总功率，并说明在 $\mathbf{p} = q\mathbf{d}$ 时退化为拉莫尔公式。
4. 写出阿布拉罕–洛伦兹力，由能量平衡推导它，并解释失控/预加速病态及 $\tau$ 的数值。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Sources are evaluated at the retarded time $t_r=t-|\mathbf r-\mathbf r'|/c$ (signals travel at $c$). The advanced solution ($t+|\mathbf r-\mathbf r'|/c$) violates causality (effect before cause) and is discarded. · 推迟时间;舍去超前解(违因果)。
**2.** $\kappa=1-\mathbf n\cdot\boldsymbol\beta$ arises because the source moves during emission, compressing the retarded contribution along the direction of motion (relativistic beaming). · 源运动使推迟贡献沿运动方向压缩。
**3.** $\int\sin^2\theta\,d\Omega=8\pi/3$, so $P=\mu_0\ddot p^2/6\pi c$; with $\mathbf p=q\mathbf d$, $\ddot{\mathbf p}=q\mathbf a$ gives $P=q^2 a^2/6\pi\epsilon_0 c^3$ (Larmor). · 积分得拉莫尔公式。
**4.** $\mathbf F_\text{AL}=m\tau\dot{\mathbf a}$, $\tau=q^2/6\pi\epsilon_0 mc^3$ (from energy balance). It has runaway ($a\propto e^{t/\tau}$) and pre-acceleration pathologies — the breakdown of classical point-charge electrodynamics. · 阿布拉罕–洛伦兹力及其病态。

</details>

---

← Previous: [Module 1.21 — Classical Scattering Theory](./module-1.21-classical-scattering.md) · [Phase 1 index](./README.md) · Next: [Module 1.23 — Waveguides, Cavities & Transmission Lines](./module-1.23-waveguides-cavities-transmission-lines.md) →

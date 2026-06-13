# Module 3.15 — Relativistic Quantum Mechanics
**模块 3.15 — 相对论量子力学**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.15-relativistic-quantum-mechanics-derivations.md)

---

## 1. The Klein–Gordon and Dirac Equations · 克莱因–戈登方程与狄拉克方程

**Definition.** Starting from the relativistic energy–momentum relation $E^2 = (pc)^2 + (mc^2)^2$, replacing $E \to i\hbar\, \partial/\partial t$ and $p \to -i\hbar\nabla$ yields the **Klein–Gordon (KG) equation**:

$$ \frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2} - \nabla^2\psi + \left(\frac{mc}{\hbar}\right)^2 \psi = 0, \qquad \text{or in covariant notation} \qquad \left(\Box + \left(\frac{mc}{\hbar}\right)^2\right) \psi = 0, $$

where $\Box = \partial_\mu \partial^\mu = (1/c^2)\partial^2/\partial t^2 - \nabla^2$ is the d'Alembertian. The KG equation is Lorentz-covariant and has plane-wave solutions, but it has two severe problems: (1) The **probability density** $\rho = (i\hbar/2mc^2)(\psi^* \partial\psi/\partial t - \psi\, \partial\psi^*/\partial t)$ derived from it can be **negative** (it is not positive-definite), making a single-particle probabilistic interpretation untenable. (2) It admits **negative-energy solutions** $E = -\sqrt{(pc)^2 + (mc^2)^2}$ with no lower bound.

**定义。** 从相对论能量–动量关系 $E^2 = (pc)^2 + (mc^2)^2$ 出发，令 $E \to i\hbar\, \partial/\partial t$，$p \to -i\hbar\nabla$，得到**克莱因–戈登（KG）方程**：

$$ \frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2} - \nabla^2\psi + \left(\frac{mc}{\hbar}\right)^2 \psi = 0, \qquad \text{或协变形式} \qquad \left(\Box + \left(\frac{mc}{\hbar}\right)^2\right) \psi = 0, $$

其中 $\Box = \partial_\mu \partial^\mu = (1/c^2)\partial^2/\partial t^2 - \nabla^2$ 是达朗贝尔算符。KG 方程是洛伦兹协变的，有平面波解，但有两个严重问题：(1) 由它导出的**概率密度** $\rho = (i\hbar/2mc^2)(\psi^* \partial\psi/\partial t - \psi\, \partial\psi^*/\partial t)$ 可以**为负**（非正定），使单粒子概率诠释不成立。(2) 它允许**负能解** $E = -\sqrt{(pc)^2 + (mc^2)^2}$，没有下界。

**Definition.** **Dirac (1928)** sought a first-order equation in both space and time, so the probability density would be positive definite. He required that the equation, when applied twice, yields the KG equation for each component. This forces the coefficients to be matrices satisfying the **Clifford algebra**. The resulting **Dirac equation** is:

$$ (i\hbar\, \gamma^\mu \partial_\mu - mc)\, \psi = 0, $$

where the **gamma matrices** $\gamma^\mu$ ($\mu = 0,1,2,3$) are $4\times 4$ matrices satisfying $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu} I_4$ (with metric signature $(+,-,-,-)$). The wavefunction $\psi$ is a **4-component Dirac spinor**. The conserved current $j^\mu = \bar\psi \gamma^\mu \psi$ (where $\bar\psi = \psi^\dagger \gamma^0$ is the Dirac adjoint) satisfies $\partial_\mu j^\mu = 0$, and the time component $j^0 = \psi^\dagger\psi$ is **positive definite** — fixing the probability problem.

**定义。** **狄拉克（1928 年）**寻求在时间和空间上均为一阶的方程，使得概率密度正定。他要求该方程作用两次后对每个分量给出 KG 方程。这迫使系数为满足**Clifford 代数**的矩阵。由此得到的**狄拉克方程**为：

$$ (i\hbar\, \gamma^\mu \partial_\mu - mc)\, \psi = 0, $$

其中 **$\gamma$ 矩阵** $\gamma^\mu$（$\mu = 0,1,2,3$）是满足 $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu} I_4$ 的 $4\times 4$ 矩阵（度规符号为 $(+,-,-,-)$）。波函数 $\psi$ 是 **4 分量狄拉克旋量**。守恒流 $j^\mu = \bar\psi \gamma^\mu \psi$（其中 $\bar\psi = \psi^\dagger \gamma^0$ 是狄拉克共轭）满足 $\partial_\mu j^\mu = 0$，时间分量 $j^0 = \psi^\dagger\psi$ **正定**——从而解决了概率问题。

**Demonstration — Antiparticles.** The Dirac equation still has negative-energy solutions. Dirac's interpretation (the **Dirac sea**): all negative-energy states are filled by electrons in the ground state of the vacuum. A hole in the Dirac sea — a missing negative-energy, negative-charge electron — behaves as a positive-energy, positive-charge particle: the **positron**. Predicted by Dirac in 1930 and discovered by Anderson in 1932, this was the first prediction and discovery of **antimatter**. In modern quantum field theory the Dirac sea picture is replaced by the reinterpretation of negative-frequency solutions as **antiparticle** creation operators (Module 6.5), but the physical content is the same.

**演示——反粒子。** 狄拉克方程仍有负能解。狄拉克的诠释（**狄拉克海**）：真空基态中所有负能态均被电子填满。狄拉克海中的空穴——缺少一个负能、负电荷的电子——表现为一个正能、正电荷的粒子：**正电子**。狄拉克于 1930 年预言，安德森于 1932 年发现，这是**反物质**的首次预言与发现。在现代量子场论中，狄拉克海图像被负频解重新诠释为**反粒子**产生算符（模块 6.5）所取代，但物理内容相同。

---

## 2. Consequences: Spin, $g = 2$, and Fine Structure · 推论：自旋、$g = 2$ 与精细结构

**Definition.** The spin-$\tfrac12$ nature of the electron and its **g-factor $g = 2$** are not put in by hand in the Dirac theory — they emerge automatically. In an external magnetic field $\mathbf{B}$, the Dirac equation in the non-relativistic limit yields the **Pauli equation**:

$$ i\hbar\, \frac{\partial\psi}{\partial t} = \left[ \frac{p^2}{2m} - \frac{e\mathbf{A}\cdot\mathbf{p}}{m} + \frac{e^2 A^2}{2m} + V - \frac{e\hbar}{2m}\, \boldsymbol{\sigma}\cdot\mathbf{B} \right] \psi_2, $$

where $\psi_2$ is the two-component (upper, large) spinor and $\boldsymbol{\sigma}$ are the Pauli matrices. The magnetic moment coupling is $-\boldsymbol{\mu}\cdot\mathbf{B}$ with **$\boldsymbol{\mu} = (e\hbar/2m)\, \boldsymbol{\sigma}$**, giving the **g-factor $g = 2$** exactly: the magnetic moment is twice what one would expect from orbital motion alone.

**定义。** 电子的自旋-$\tfrac12$ 性质及其 **$g$ 因子 $g = 2$** 在狄拉克理论中不是人为引入的——它们自动涌现。在外磁场 $\mathbf{B}$ 中，狄拉克方程取非相对论极限得到**泡利方程**：

$$ i\hbar\, \frac{\partial\psi}{\partial t} = \left[ \frac{p^2}{2m} - \frac{e\mathbf{A}\cdot\mathbf{p}}{m} + \frac{e^2 A^2}{2m} + V - \frac{e\hbar}{2m}\, \boldsymbol{\sigma}\cdot\mathbf{B} \right] \psi_2, $$

其中 $\psi_2$ 是两分量（上、大）旋量，$\boldsymbol{\sigma}$ 是泡利矩阵。磁矩耦合为 $-\boldsymbol{\mu}\cdot\mathbf{B}$，**$\boldsymbol{\mu} = (e\hbar/2m)\, \boldsymbol{\sigma}$**，精确给出 **$g$ 因子 $g = 2$**：磁矩是仅由轨道运动所预期值的两倍。

**Demonstration — Spin–Orbit Coupling and Fine Structure.** Carrying the non-relativistic expansion to the next order in $v^2/c^2$ (via the Foldy–Wouthuysen transformation), the Dirac hydrogen atom yields three corrections to the Schrödinger energy: (1) the **relativistic kinetic energy** correction $-p^4/(8m^3 c^2)$; (2) the **spin–orbit coupling**

$$ H_\text{SO} = \frac{\hbar}{2m^2 c^2}\, \frac{1}{r}\, \frac{dV}{dr}\, \mathbf{S}\cdot\mathbf{L}, $$

where $V(r) = -e^2/(4\pi\varepsilon_0 r)$ for hydrogen; (3) the **Darwin term** $(\hbar^2/8m^2 c^2)\, \nabla^2 V$ (non-zero only for $l = 0$). Together these give the **hydrogen fine structure** (Module 3.6) with the exact relativistic energy formula:

$$ E_{nj} = m_e c^2 \left[ 1 + \left( \frac{\alpha}{n - (j+\tfrac12) + \sqrt{(j+\tfrac12)^2 - \alpha^2}} \right)^2 \right]^{-1/2} - m_e c^2, $$

where $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$ is the fine-structure constant and $j$ is the total angular momentum quantum number. Expanding in powers of $\alpha$ reproduces the Bohr levels plus the fine-structure shifts $-\dfrac{m_e c^2 \alpha^4}{2n^3}\left(\dfrac{1}{j+\tfrac12} - \dfrac{3}{4n}\right)$.

**演示——自旋–轨道耦合与精细结构。** 将非相对论展开推进到 $v^2/c^2$ 的下一阶（通过 Foldy–Wouthuysen 变换），狄拉克氢原子给出对薛定谔能量的三个修正：(1) **相对论动能**修正 $-p^4/(8m^3 c^2)$；(2) **自旋–轨道耦合**

$$ H_\text{SO} = \frac{\hbar}{2m^2 c^2}\, \frac{1}{r}\, \frac{dV}{dr}\, \mathbf{S}\cdot\mathbf{L}, $$

其中对氢原子 $V(r) = -e^2/(4\pi\varepsilon_0 r)$；(3) **达尔文项** $(\hbar^2/8m^2 c^2)\, \nabla^2 V$（仅对 $l = 0$ 非零）。这些共同给出**氢原子精细结构**（模块 3.6），精确相对论能量公式为：

$$ E_{nj} = m_e c^2 \left[ 1 + \left( \frac{\alpha}{n - (j+\tfrac12) + \sqrt{(j+\tfrac12)^2 - \alpha^2}} \right)^2 \right]^{-1/2} - m_e c^2, $$

其中 $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$ 是精细结构常数，$j$ 是总角动量量子数。对 $\alpha$ 展开，还原玻尔能级加上精细结构修正 $-\dfrac{m_e c^2 \alpha^4}{2n^3}\left(\dfrac{1}{j+\tfrac12} - \dfrac{3}{4n}\right)$。

**Application.** The Dirac equation is the single-particle foundation underlying **quantum electrodynamics (QED)** and the entire Standard Model. Its field-theoretic generalisation (Module 6.5) replaces the wavefunction with a quantum field, automatically incorporating particle creation, annihilation, and the full machinery of renormalisation. The spin–orbit coupling derived here is the relativistic origin of the fine structure observed in atomic spectra, the **Lamb shift** (a QED correction beyond Dirac), and the spin–orbit interaction responsible for **band inversions** in topological insulators (Phase 4). The $g = 2$ result is corrected to $g = 2 + \alpha/\pi + \cdots$ by QED loop diagrams — the most precisely tested prediction in physics.

**应用。** 狄拉克方程是**量子电动力学（QED）**及整个标准模型的单粒子基础。其场论推广（模块 6.5）用量子场替换波函数，自动纳入粒子的产生、湮灭及完整的重整化机制。此处推导的自旋–轨道耦合是原子光谱中观测到的精细结构的相对论起源，**兰姆位移**（超越狄拉克的 QED 修正），以及拓扑绝缘体（第 4 阶段）中**能带反转**背后的自旋–轨道相互作用。$g = 2$ 的结果经 QED 圈图修正为 $g = 2 + \alpha/\pi + \cdots$——这是物理学中检验最精确的预言。

## Key results · 核心结果

- Klein–Gordon $(\Box + (mc/\hbar)^2)\psi = 0$ — relativistic scalar wave equation · 克莱因–戈登方程
- Dirac $(i\hbar\,\gamma^\mu\partial_\mu - mc)\psi = 0$ — first-order, requires 4-spinors · 狄拉克方程
- Predicts spin-$\tfrac12$, $g = 2$, and antiparticles · 预言自旋、$g=2$ 与反粒子
- Non-relativistic limit gives spin–orbit coupling and fine structure · 非相对论极限给出自旋–轨道耦合与精细结构

---

**Self-test (blank page)**

1. Write the Klein–Gordon equation and state its two physical problems.
2. Write the Dirac equation in covariant notation; identify $\bar\psi$ and the form of the current $j^\mu$.
3. State the Clifford algebra condition on the gamma matrices and explain why it is needed.
4. Explain the Dirac sea interpretation of antiparticles.
5. Show how $g = 2$ emerges from the non-relativistic limit of the Dirac equation.
6. Write the spin–orbit coupling term from the Dirac expansion and state the quantum numbers in $E_{nj}$.
7. What does the Dirac equation predict about the Lamb shift, and what corrects it?

**自测（空白页）**

1. 写出克莱因–戈登方程，并陈述其两个物理问题。
2. 用协变符号写出狄拉克方程；指明 $\bar\psi$ 及流 $j^\mu$ 的形式。
3. 陈述 $\gamma$ 矩阵的 Clifford 代数条件，并解释为何需要它。
4. 解释反粒子的狄拉克海诠释。
5. 说明 $g = 2$ 如何从狄拉克方程的非相对论极限中涌现。
6. 写出狄拉克展开中的自旋–轨道耦合项，并陈述 $E_{nj}$ 中的量子数。
7. 狄拉克方程对兰姆位移有何预言，什么修正了它？

---

← Previous: [Module 3.14 — Density Matrix & Open Quantum Systems](./module-3.14-density-matrix-and-open-quantum-systems.md) · [Phase 3 index](./README.md) · Next: [Module 3.16 — Quantum Computation & Information](./module-3.16-quantum-computation-and-information.md) →

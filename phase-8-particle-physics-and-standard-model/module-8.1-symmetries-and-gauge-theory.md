# Module 8.1 — Symmetries & Gauge Theory ⭐
**模块 8.1 — 对称性与规范理论 ⭐**

> **Phase 8 — [Particle Physics & the Standard Model](./README.md)** · Format: Definition → Demonstration → Application
> **第 8 阶段 — 粒子物理与标准模型 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-8.1-derivations.md)

---

## 1. Global and Local Symmetry · 全局对称性与局域对称性

**Definition.** A **global symmetry** transforms every point in spacetime by the same phase or group element: e.g., $\psi \to e^{i\alpha}\psi$ with $\alpha$ constant. A **local (gauge) symmetry** promotes $\alpha$ to an arbitrary function $\alpha(x)$ of position and time. Demanding that the Lagrangian remain invariant under this $x$-dependent transformation forces the introduction of a **gauge field** — a connection $A_\mu(x)$ — whose job is to compensate the extra derivative term $\partial_\mu\alpha$ that would otherwise spoil invariance. The gauge field transforms as $A_\mu \to A_\mu + \partial_\mu\alpha$ (for $U(1)$), exactly matching the covariant EM potential rule derived in Module 1.15.

**定义。** **全局对称性**以同一相位或群元素对时空中每一点进行变换：例如，$\psi \to e^{i\alpha}\psi$，其中 $\alpha$ 为常数。**局域（规范）对称性**将 $\alpha$ 提升为位置和时间的任意函数 $\alpha(x)$。要求拉格朗日量在这种依赖于 $x$ 的变换下保持不变，迫使引入一个**规范场**——联络 $A_\mu(x)$——其作用是补偿额外的导数项 $\partial_\mu\alpha$，否则不变性将被破坏。规范场的变换为 $A_\mu \to A_\mu + \partial_\mu\alpha$（对于 $U(1)$），与模块 1.15 中推导的协变电磁势规则完全一致。

**Demonstration.** Start with the free Dirac Lagrangian $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$, which is globally $U(1)$-invariant. Under $\psi \to e^{i\alpha(x)}\psi$ the derivative picks up $\bar\psi\gamma^\mu(\partial_\mu\alpha)\psi$ — a failure of local invariance. Replace $\partial_\mu \to D_\mu = \partial_\mu - ieA_\mu$ (the **covariant derivative**); then $D_\mu\psi \to e^{i\alpha(x)}D_\mu\psi$ and the Lagrangian is restored. Adding the kinetic term $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ for the gauge field, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, yields the full QED Lagrangian. The same logic applied to a non-abelian group $G$ replaces $A_\mu$ with a Lie-algebra-valued field $A_\mu = A_\mu^a T^a$ (generators $T^a$), and produces self-interacting gauge bosons (Yang–Mills theory, 1954).

**演示。** 从自由狄拉克拉格朗日量 $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ 出发，它具有全局 $U(1)$ 不变性。在 $\psi \to e^{i\alpha(x)}\psi$ 变换下，导数项引入了 $\bar\psi\gamma^\mu(\partial_\mu\alpha)\psi$——局域不变性遭到破坏。将 $\partial_\mu$ 替换为 $D_\mu = \partial_\mu - ieA_\mu$（**协变导数**）；则 $D_\mu\psi \to e^{i\alpha(x)}D_\mu\psi$，拉格朗日量得以恢复。为规范场添加动能项 $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$，其中 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$，即得到完整的量子电动力学拉格朗日量。将同样的逻辑应用于非阿贝尔群 $G$，以李代数值场 $A_\mu = A_\mu^a T^a$（生成元 $T^a$）替换 $A_\mu$，产生自相互作用的规范玻色子（杨–米尔斯理论，1954）。

**Application.** This "gauge principle" is the architectural rule of the Standard Model. Every fundamental force corresponds to demanding local invariance under a group: $U(1) \to$ electromagnetism, $SU(2) \to$ weak force, $SU(3) \to$ strong force. Noether's theorem (Module 1.4) ties each continuous symmetry to a conserved current; gauge invariance specifically ties global conservation laws (charge, color, weak isospin) to the existence of force-carrier bosons.

**应用。** 这一"规范原理"是标准模型的构架法则。每种基本力都对应于要求在某群下的局域不变性：$U(1) \to$ 电磁力，$SU(2) \to$ 弱力，$SU(3) \to$ 强力。诺特定理（模块 1.4）将每个连续对称性与一个守恒流联系起来；规范不变性特别地将全局守恒律（电荷、色荷、弱同位旋）与力载体玻色子的存在联系起来。

---

## 2. Yang–Mills Theory and Non-Abelian Gauge Groups · 杨–米尔斯理论与非阿贝尔规范群

**Definition.** In **Yang–Mills theory** the gauge group $G$ is non-abelian ($SU(N)$ for $N \geq 2$). The field-strength tensor generalizes to $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c$, where $f^{abc}$ are the structure constants of the Lie algebra and $g$ is the coupling. The cubic and quartic terms in $f^{abc}$ mean gauge bosons carry their own charge — they self-interact, unlike photons. This self-interaction has dramatic physical consequences: asymptotic freedom (QCD) and the non-perturbative vacuum structure that drives confinement.

**定义。** 在**杨–米尔斯理论**中，规范群 $G$ 是非阿贝尔的（$N \geq 2$ 时为 $SU(N)$）。场强张量推广为 $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c$，其中 $f^{abc}$ 是李代数的结构常数，$g$ 是耦合常数。$f^{abc}$ 中的三次项和四次项意味着规范玻色子携带自身的荷——它们相互作用，与光子不同。这种自相互作用具有深刻的物理后果：渐近自由（量子色动力学）以及驱动夸克禁闭的非微扰真空结构。

**Demonstration.** For $G = SU(2)$ there are three generators $T^a = \sigma^a/2$ (Pauli matrices) and three gauge fields $W_\mu^a$. The field strength picks up the commutator term $[A_\mu, A_\nu] \propto \varepsilon^{abc}W_\mu^b W_\nu^c$. The resulting equations of motion are non-linear: $\partial^\nu F_{\mu\nu}^a + gf^{abc}A^{\nu b} F_{\mu\nu}^c = j_\mu^a$. Even in vacuum ($j_\mu = 0$) the equations are non-trivial; they admit topological solutions (instantons) absent in abelian theory.

**演示。** 对于 $G = SU(2)$，有三个生成元 $T^a = \sigma^a/2$（泡利矩阵）和三个规范场 $W_\mu^a$。场强中出现对易子项 $[A_\mu, A_\nu] \propto \varepsilon^{abc}W_\mu^b W_\nu^c$。所得的运动方程是非线性的：$\partial^\nu F_{\mu\nu}^a + gf^{abc}A^{\nu b} F_{\mu\nu}^c = j_\mu^a$。即使在真空中（$j_\mu = 0$），方程也是非平凡的；它们存在阿贝尔理论中没有的拓扑解（瞬子）。

**Application.** Yang–Mills theory underpins both QCD ($SU(3)$) and the electroweak sector ($SU(2)\times U(1)$). The self-coupling of gluons is responsible for confinement and for the bulk of visible mass via the QCD vacuum energy. The same mathematical framework describes every force except gravity — and even gravity has a gauge-theory interpretation (diffeomorphism invariance), connecting back to Phase 7.

**应用。** 杨–米尔斯理论是量子色动力学（$SU(3)$）和电弱理论（$SU(2)\times U(1)$）的基础。胶子的自耦合通过量子色动力学真空能负责夸克禁闭和可见质量的主要来源。同样的数学框架描述了除引力之外的所有力——甚至引力也有规范理论的诠释（微分同胚不变性），从而与第 7 阶段相联系。

## Key results · 核心结果

- Promoting a global symmetry $\psi \to e^{i\alpha}\psi$ to a local one $\alpha(x)$ **forces** a gauge field via $D_\mu = \partial_\mu - igA_\mu$ · 局域化对称性必然引入规范场
- Field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu (- ig[A_\mu,A_\nu])$ · 场强张量
- Yang–Mills: non-Abelian groups give self-interacting gauge bosons · 杨–米尔斯规范玻色子自相互作用
- The gauge principle builds QED, QCD, and the electroweak theory · 规范原理构建整个标准模型

---

## Self-test (blank page)

1. Starting from the free Dirac Lagrangian, show step by step why local $U(1)$ invariance requires a gauge field and derive its transformation law.
2. Explain what Noether's theorem (Module 1.4) says about the conserved current associated with global $U(1)$ symmetry. What is the analogous statement for color $SU(3)$?
3. What new interaction terms appear in the Yang–Mills Lagrangian that are absent in Maxwell theory, and what physical consequence do they have?

**自测（空白页）**

1. 从自由狄拉克拉格朗日量出发，逐步说明为何局域 $U(1)$ 不变性需要引入规范场，并推导其变换律。
2. 解释诺特定理（模块 1.4）关于全局 $U(1)$ 对称性所对应守恒流的论述。对于色 $SU(3)$，类似的陈述是什么？
3. 杨–米尔斯拉格朗日量中出现了哪些麦克斯韦理论中没有的新相互作用项，它们有什么物理后果？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $\mathcal L=\bar\psi(i\gamma^\mu\partial_\mu-m)\psi$. Under $\psi\to e^{i\alpha(x)}\psi$ the derivative picks up $i\partial_\mu\alpha$, breaking invariance. Introduce $A_\mu$ with $D_\mu=\partial_\mu+ieA_\mu$ and require $A_\mu\to A_\mu-\tfrac1e\partial_\mu\alpha$; then $D_\mu\psi\to e^{i\alpha}D_\mu\psi$ and $\mathcal L$ is invariant. · 局域 $U(1)$ 迫使引入 $A_\mu$,$A_\mu\to A_\mu-\tfrac1e\partial_\mu\alpha$。

**2.** Global $U(1)$ gives the conserved current $j^\mu=\bar\psi\gamma^\mu\psi$ with $\partial_\mu j^\mu=0$ (charge conservation). For color $SU(3)$ there are eight currents $j^\mu_a=\bar\psi\gamma^\mu T_a\psi$, covariantly conserved $D_\mu j^\mu_a=0$. · 诺特流 $j^\mu=\bar\psi\gamma^\mu\psi$;$SU(3)$ 有八条色流。

**3.** The Yang–Mills field strength $F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu$ has a quadratic/cubic $A$ term, giving **gauge-boson self-interactions** (3- and 4-gluon vertices) absent in Maxwell — gluons carry color, leading to confinement and asymptotic freedom. · 杨–米尔斯含规范玻色子自相互作用,导致禁闭与渐近自由。

</details>

---

← [Phase 8 index](./README.md) · Next: [Module 8.2 — Quantum Electrodynamics (QED)](./module-8.2-quantum-electrodynamics.md) →

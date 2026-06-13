# Module 3.14 — Density Matrix & Open Quantum Systems
**模块 3.14 — 密度矩阵与开放量子系统**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.14-density-matrix-and-open-quantum-systems-derivations.md)

---

## 1. The Density Operator: Pure vs Mixed States · 密度算符：纯态与混态

**Definition.** The **density operator** (density matrix) generalises the state vector to handle both quantum superpositions and classical statistical ignorance. If a system is prepared in state $|\psi_i\rangle$ with probability $p_i$, the density operator is

**定义。** **密度算符**（密度矩阵）将态矢量推广，以同时处理量子叠加与经典统计不确定性。若系统以概率 $p_i$ 处于态 $|\psi_i\rangle$，则密度算符为

$$ \rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|, \qquad \sum_i p_i = 1, \quad p_i \geq 0. $$

$\rho$ is **Hermitian** ($\rho^\dagger = \rho$), has unit trace ($\text{Tr}\,\rho = 1$), and is **positive semi-definite** ($\langle\phi|\rho|\phi\rangle \geq 0$ for all $|\phi\rangle$). A state is **pure** if and only if $\rho^2 = \rho$ (equivalently $\text{Tr}\,\rho^2 = 1$); otherwise it is **mixed** ($\text{Tr}\,\rho^2 < 1$). A pure state arises from a single preparation $|\psi\rangle$: $\rho = |\psi\rangle\langle\psi|$. A mixed state cannot be represented by any single ket.

$\rho$ 是**厄米算符**（$\rho^\dagger = \rho$），具有单位迹（$\text{Tr}\,\rho = 1$），且是**半正定**的（对所有 $|\phi\rangle$ 有 $\langle\phi|\rho|\phi\rangle \geq 0$）。当且仅当 $\rho^2 = \rho$（等价地 $\text{Tr}\,\rho^2 = 1$）时，态为**纯态**；否则为**混态**（$\text{Tr}\,\rho^2 < 1$）。纯态来自单一制备 $|\psi\rangle$：$\rho = |\psi\rangle\langle\psi|$。混态不能用任何单一右矢表示。

**Demonstration.** The expectation value of any observable $A$ is

**演示。** 任意可观测量 $A$ 的期望值为

$$ \langle A\rangle = \text{Tr}(\rho A). $$

For a pure state $\rho = |\psi\rangle\langle\psi|$, this reduces to $\langle\psi|A|\psi\rangle$ as expected. For a mixed state, it is the probability-weighted average of the individual quantum expectations. This single formula replaces the two-step "pick a state, then compute an expectation value" procedure and is the starting point for all statistical quantum mechanics.

对于纯态 $\rho = |\psi\rangle\langle\psi|$，这回归为通常的 $\langle\psi|A|\psi\rangle$。对于混态，它是各量子期望值的概率加权平均。这一公式取代了"先选态再计算期望值"的两步过程，是所有统计量子力学的出发点。

**Application.** The density matrix is essential whenever the full quantum state is inaccessible — thermal equilibrium ($\rho \propto e^{-\beta\hat{H}}$), subsystems of entangled pairs, decoherence, and quantum information. It unifies quantum and classical probability in a single mathematical object.

**应用。** 只要完整量子态不可获取，密度矩阵就是必需的——热平衡（$\rho \propto e^{-\beta\hat{H}}$）、纠缠对的子系统、退相干以及量子信息。它将量子与经典概率统一在单一数学对象中。

---

## 2. The Reduced Density Matrix & von Neumann Entropy · 约化密度矩阵与冯·诺依曼熵

**Definition.** For a bipartite system AB with joint state $\rho_{AB}$, the **reduced density matrix** of subsystem A is obtained by a **partial trace** over B:

**定义。** 对于联合态为 $\rho_{AB}$ 的二分系统 AB，子系统 A 的**约化密度矩阵**通过对 B 求**偏迹**得到：

$$ \rho_A = \text{Tr}_B(\rho_{AB}) = \sum_j \langle b_j|\rho_{AB}|b_j\rangle, $$

where $\{|b_j\rangle\}$ is any orthonormal basis for B. The reduced density matrix contains all measurable information about A alone. The key result: if AB is in a **pure entangled** state, then $\rho_A$ is a **non-trivial mixed state**. Entanglement with B destroys the purity of A.

其中 $\{|b_j\rangle\}$ 是 B 的任意正交归一基。约化密度矩阵包含关于 A 的所有可测信息。关键结论：若 AB 处于**纯纠缠态**，则 $\rho_A$ 是**非平凡混态**。与 B 的纠缠破坏了 A 的纯度。

**Definition.** The **von Neumann entropy** is

**定义。** **冯·诺依曼熵**为

$$ S(\rho) = -\text{Tr}(\rho \ln \rho) = -\sum_i \lambda_i \ln \lambda_i, $$

where $\lambda_i$ are the eigenvalues of $\rho$. For a pure state $S = 0$; for a maximally mixed $d\times d$ state $S = \ln d$. For a bipartite pure state, $S(\rho_A) = S(\rho_B)$ is the **entanglement entropy**, a measure of how strongly A and B are entangled (Module 3.13).

其中 $\lambda_i$ 是 $\rho$ 的本征值。纯态时 $S = 0$；$d\times d$ 最大混态时 $S = \ln d$。对于纯二分态，$S(\rho_A) = S(\rho_B)$ 是**纠缠熵**，衡量 A 与 B 纠缠的强度（模块 3.13）。

**Demonstration.** For the Bell state $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$, the reduced density matrix of qubit A is $\rho_A = \tfrac12 I$ (the maximally mixed state), with $S(\rho_A) = \ln 2$. This is the maximum possible entanglement for a two-qubit system.

**演示。** 对于贝尔态 $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$，量子比特 A 的约化密度矩阵为 $\rho_A = \tfrac12 I$（最大混态），$S(\rho_A) = \ln 2$。这是两量子比特系统的最大可能纠缠。

**Application.** Entanglement entropy characterises quantum phase transitions (diverges at critical points), quantifies the resource value of entangled states in quantum protocols, and — in the context of the holographic principle — connects to the area of surfaces in AdS geometry (Ryu–Takayanagi formula).

**应用。** 纠缠熵表征量子相变（在临界点发散），量化量子协议中纠缠态的资源价值，并在全息原理的背景下与 AdS 几何中曲面的面积相联系（Ryu–高柳公式）。

---

## 3. Open Systems & the Lindblad Master Equation · 开放系统与 Lindblad 主方程

**Definition.** A **closed** quantum system evolves unitarily: $d\rho/dt = -(i/\hbar)[\hat{H}, \rho]$ (the **von Neumann equation**, the density-matrix analogue of the Schrödinger equation). An **open** system S is coupled to an environment (bath) E. Tracing over E yields a non-unitary evolution for $\rho_S$. The most general Markovian (memory-less) master equation that preserves the positivity and trace of $\rho$ is the **Lindblad (GKSL) master equation**:

**定义。** **封闭**量子系统幺正演化：$d\rho/dt = -(i/\hbar)[\hat{H}, \rho]$（**冯·诺依曼方程**，薛定谔方程的密度矩阵类比）。**开放**系统 S 与环境（热浴）E 耦合。对 E 求迹得到 $\rho_S$ 的非幺正演化。保持 $\rho$ 正定性和迹的最一般马尔可夫（无记忆）主方程是 **Lindblad（GKSL）主方程**：

$$ \frac{d\rho}{dt} = -\frac{i}{\hbar}[\hat{H}, \rho] + \sum_k \gamma_k \left( L_k \rho L_k^\dagger - \tfrac12 L_k^\dagger L_k \rho - \tfrac12 \rho L_k^\dagger L_k \right), $$

where the **Lindblad operators** (jump operators) $L_k$ encode the system–environment coupling channels and $\gamma_k \geq 0$ are the corresponding decay rates. The first term is coherent (Hamiltonian) evolution; the second term is the **dissipator** $\mathcal{D}[\rho]$, describing incoherent processes such as spontaneous emission, dephasing, and thermalisation.

其中**林德布拉德算符**（跃迁算符）$L_k$ 编码系统–环境耦合通道，$\gamma_k \geq 0$ 为对应的衰减率。第一项是相干（哈密顿量）演化；第二项是**耗散子** $\mathcal{D}[\rho]$，描述非相干过程，如自发辐射、退相位和热化。

**Demonstration — Decoherence.** Consider a two-level system with basis $\{|0\rangle, |1\rangle\}$ subject to pure dephasing: $L = |1\rangle\langle 1|$, rate $\gamma$. The off-diagonal element $\rho_{01}(t) = \rho_{01}(0)\, e^{-\gamma t}$. The diagonal (population) elements are unchanged. Coherences decay exponentially with **dephasing time $T_2 = 1/\gamma$**, while populations are unaffected — a hallmark of decoherence without energy relaxation. More generally, $T_1$ is the energy relaxation time and $1/T_2 = 1/(2T_1) + 1/T_2^*$ for additional pure dephasing.

**演示——退相干。** 考虑受纯退相位作用的二能级系统，基为 $\{|0\rangle, |1\rangle\}$：$L = |1\rangle\langle 1|$，速率 $\gamma$。非对角元 $\rho_{01}(t) = \rho_{01}(0)\, e^{-\gamma t}$。对角（布居）元不变。相干度以**退相位时间 $T_2 = 1/\gamma$** 指数衰减，而布居数不受影响——这是无能量弛豫的退相干的标志。更一般地，$T_1$ 是能量弛豫时间，$1/T_2 = 1/(2T_1) + 1/T_2^*$（附加纯退相位）。

**Application.** Decoherence explains the quantum-to-classical transition: environmental entanglement suppresses off-diagonal elements in the pointer basis, making macroscopic superpositions effectively unobservable. This connects the density matrix formalism directly to quantum measurement theory (Module 3.3) and to entanglement (Module 3.13) — decoherence is entanglement between the system and uncontrolled environmental degrees of freedom. In quantum computing, decoherence is the principal source of error; quantum error correction codes are designed to counteract it.

**应用。** 退相干解释了从量子到经典的转变：环境纠缠抑制了指针基下的非对角元，使宏观叠加态在实际上不可观测。这将密度矩阵形式主义直接联系到量子测量理论（模块 3.3）和纠缠（模块 3.13）——退相干就是系统与不受控环境自由度之间的纠缠。在量子计算中，退相干是误差的主要来源；量子纠错码正是为对抗它而设计的。

## Key results · 核心结果

- $\rho = \sum_i p_i|\psi_i\rangle\langle\psi_i|$, $\langle A\rangle = \text{Tr}(\rho A)$ — pure ($\rho^2=\rho$) vs mixed states · 密度算符
- $\rho_A = \text{Tr}_B(\rho_{AB})$ — reduced density matrix for a subsystem · 约化密度矩阵
- $S(\rho) = -\text{Tr}(\rho\ln\rho)$ — von Neumann entropy (entanglement measure) · 冯·诺依曼熵
- $\dot\rho = -\tfrac{i}{\hbar}[\hat{H},\rho] + \sum_k\gamma_k(L_k\rho L_k^\dagger - \tfrac12\{L_k^\dagger L_k,\rho\})$ — Lindblad master equation · Lindblad 主方程

---

**Self-test (blank page)**

1. State the three defining properties of a density matrix and give the criterion distinguishing pure from mixed states.
2. Write the expectation value formula for an observable $A$ in terms of $\rho$, and show it reduces to the usual formula for a pure state.
3. Define the partial trace and compute $\rho_A$ for the Bell state $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$. What is $S(\rho_A)$?
4. Write the Lindblad master equation, identify each term, and explain what "Markovian" means.
5. For pure dephasing of a qubit with rate $\gamma$, solve for $\rho_{01}(t)$ and define $T_2$.

**自测（空白页）**

1. 陈述密度矩阵的三个定义性质，并给出区分纯态与混态的判据。
2. 用 $\rho$ 写出可观测量 $A$ 的期望值公式，并证明其对纯态回归为通常的公式。
3. 定义偏迹，并对贝尔态 $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ 计算 $\rho_A$。$S(\rho_A)$ 是多少？
4. 写出 Lindblad 主方程，指明各项，并解释"马尔可夫"的含义。
5. 对速率为 $\gamma$ 的量子比特纯退相位，求解 $\rho_{01}(t)$ 并定义 $T_2$。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $\rho$ is (i) Hermitian, (ii) positive semidefinite ($\rho\ge0$), (iii) unit trace ($\text{Tr}\,\rho=1$). Pure iff $\rho^2=\rho$ (equivalently $\text{Tr}\,\rho^2=1$); mixed if $\text{Tr}\,\rho^2<1$. · 厄米、半正定、迹为 1;纯态 $\rho^2=\rho$,否则混态。

**2.** $\langle A\rangle=\text{Tr}(\rho A)$. For a pure state $\rho=|\psi\rangle\langle\psi|$: $\text{Tr}(|\psi\rangle\langle\psi|A)=\langle\psi|A|\psi\rangle$, the usual formula. · $\langle A\rangle=\text{Tr}(\rho A)$,纯态退化为 $\langle\psi|A|\psi\rangle$。

**3.** $\rho_A=\text{Tr}_B\rho_{AB}=\sum_j\langle b_j|\rho_{AB}|b_j\rangle$. For $|\Phi^+\rangle=\tfrac1{\sqrt2}(|00\rangle+|11\rangle)$: $\rho_A=\tfrac12(|0\rangle\langle0|+|1\rangle\langle1|)=\tfrac12\mathbb{1}$, so $S(\rho_A)=\ln2$ — maximally entangled (1 bit). · 约化得 $\rho_A=\tfrac12\mathbb 1$,$S=\ln2$,最大纠缠。

**4.** $\dot\rho=-\tfrac{i}{\hbar}[\hat{H},\rho]+\sum_k\gamma_k\big(L_k\rho L_k^\dagger-\tfrac12\{L_k^\dagger L_k,\rho\}\big)$: the commutator is unitary evolution; the dissipator gives decoherence/dissipation through jump operators $L_k$ at rates $\gamma_k$. "Markovian" = memoryless (bath correlations decay fast compared with the system's dynamics). · 第一项幺正演化,第二项耗散;马尔可夫即无记忆。

**5.** Pure dephasing gives $\dot\rho_{01}=-\gamma\rho_{01}$, so $\rho_{01}(t)=\rho_{01}(0)e^{-\gamma t}$; the coherence time is $T_2=1/\gamma$. · 纯退相干 $\rho_{01}(t)=\rho_{01}(0)e^{-\gamma t}$,$T_2=1/\gamma$。

</details>

---

← Previous: [Module 3.13 — Entanglement, EPR & Bell's Theorem](./module-3.13-entanglement-epr-and-bell.md) · [Phase 3 index](./README.md) · Next: [Module 3.15 — Relativistic Quantum Mechanics](./module-3.15-relativistic-quantum-mechanics.md) →

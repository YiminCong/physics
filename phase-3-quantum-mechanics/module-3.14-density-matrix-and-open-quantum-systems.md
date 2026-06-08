# Module 3.14 — Density Matrix & Open Quantum Systems
**模块 3.14 — 密度矩阵与开放量子系统**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.14-density-matrix-and-open-quantum-systems-derivations.md)

---

## 1. The Density Operator: Pure vs Mixed States · 密度算符：纯态与混态

**Definition.** The **density operator** (density matrix) generalises the state vector to handle both quantum superpositions and classical statistical ignorance. If a system is prepared in state |ψ_i⟩ with probability p_i, the density operator is

**定义。** **密度算符**（密度矩阵）将态矢量推广，以同时处理量子叠加与经典统计不确定性。若系统以概率 p_i 处于态 |ψ_i⟩，则密度算符为

  ρ = Σ_i p_i |ψ_i⟩⟨ψ_i|,    Σ_i p_i = 1,  p_i ≥ 0.

ρ is **Hermitian** (ρ† = ρ), has unit trace (Tr ρ = 1), and is **positive semi-definite** (⟨φ|ρ|φ⟩ ≥ 0 for all |φ⟩). A state is **pure** if and only if ρ² = ρ (equivalently Tr ρ² = 1); otherwise it is **mixed** (Tr ρ² < 1). A pure state arises from a single preparation |ψ⟩: ρ = |ψ⟩⟨ψ|. A mixed state cannot be represented by any single ket.

ρ 是**厄米算符**（ρ† = ρ），具有单位迹（Tr ρ = 1），且是**半正定**的（对所有 |φ⟩ 有 ⟨φ|ρ|φ⟩ ≥ 0）。当且仅当 ρ² = ρ（等价地 Tr ρ² = 1）时，态为**纯态**；否则为**混态**（Tr ρ² < 1）。纯态来自单一制备 |ψ⟩：ρ = |ψ⟩⟨ψ|。混态不能用任何单一右矢表示。

**Demonstration.** The expectation value of any observable A is

**演示。** 任意可观测量 A 的期望值为

  ⟨A⟩ = Tr(ρA).

For a pure state ρ = |ψ⟩⟨ψ|, this reduces to ⟨ψ|A|ψ⟩ as expected. For a mixed state, it is the probability-weighted average of the individual quantum expectations. This single formula replaces the two-step "pick a state, then compute an expectation value" procedure and is the starting point for all statistical quantum mechanics.

对于纯态 ρ = |ψ⟩⟨ψ|，这回归为通常的 ⟨ψ|A|ψ⟩。对于混态，它是各量子期望值的概率加权平均。这一公式取代了"先选态再计算期望值"的两步过程，是所有统计量子力学的出发点。

**Application.** The density matrix is essential whenever the full quantum state is inaccessible — thermal equilibrium (ρ ∝ e^{−βĤ}), subsystems of entangled pairs, decoherence, and quantum information. It unifies quantum and classical probability in a single mathematical object.

**应用。** 只要完整量子态不可获取，密度矩阵就是必需的——热平衡（ρ ∝ e^{−βĤ}）、纠缠对的子系统、退相干以及量子信息。它将量子与经典概率统一在单一数学对象中。

---

## 2. The Reduced Density Matrix & von Neumann Entropy · 约化密度矩阵与冯·诺依曼熵

**Definition.** For a bipartite system AB with joint state ρ_AB, the **reduced density matrix** of subsystem A is obtained by a **partial trace** over B:

**定义。** 对于联合态为 ρ_AB 的二分系统 AB，子系统 A 的**约化密度矩阵**通过对 B 求**偏迹**得到：

  ρ_A = Tr_B(ρ_AB) = Σ_j ⟨b_j|ρ_AB|b_j⟩,

where {|b_j⟩} is any orthonormal basis for B. The reduced density matrix contains all measurable information about A alone. The key result: if AB is in a **pure entangled** state, then ρ_A is a **non-trivial mixed state**. Entanglement with B destroys the purity of A.

其中 {|b_j⟩} 是 B 的任意正交归一基。约化密度矩阵包含关于 A 的所有可测信息。关键结论：若 AB 处于**纯纠缠态**，则 ρ_A 是**非平凡混态**。与 B 的纠缠破坏了 A 的纯度。

**Definition.** The **von Neumann entropy** is

**定义。** **冯·诺依曼熵**为

  S(ρ) = −Tr(ρ ln ρ) = −Σ_i λ_i ln λ_i,

where λ_i are the eigenvalues of ρ. For a pure state S = 0; for a maximally mixed d×d state S = ln d. For a bipartite pure state, S(ρ_A) = S(ρ_B) is the **entanglement entropy**, a measure of how strongly A and B are entangled (Module 3.13).

其中 λ_i 是 ρ 的本征值。纯态时 S = 0；d×d 最大混态时 S = ln d。对于纯二分态，S(ρ_A) = S(ρ_B) 是**纠缠熵**，衡量 A 与 B 纠缠的强度（模块 3.13）。

**Demonstration.** For the Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2, the reduced density matrix of qubit A is ρ_A = ½I (the maximally mixed state), with S(ρ_A) = ln 2. This is the maximum possible entanglement for a two-qubit system.

**演示。** 对于贝尔态 |Φ+⟩ = (|00⟩ + |11⟩)/√2，量子比特 A 的约化密度矩阵为 ρ_A = ½I（最大混态），S(ρ_A) = ln 2。这是两量子比特系统的最大可能纠缠。

**Application.** Entanglement entropy characterises quantum phase transitions (diverges at critical points), quantifies the resource value of entangled states in quantum protocols, and — in the context of the holographic principle — connects to the area of surfaces in AdS geometry (Ryu–Takayanagi formula).

**应用。** 纠缠熵表征量子相变（在临界点发散），量化量子协议中纠缠态的资源价值，并在全息原理的背景下与 AdS 几何中曲面的面积相联系（Ryu–高柳公式）。

---

## 3. Open Systems & the Lindblad Master Equation · 开放系统与 Lindblad 主方程

**Definition.** A **closed** quantum system evolves unitarily: dρ/dt = −(i/ℏ)[Ĥ, ρ] (the **von Neumann equation**, the density-matrix analogue of the Schrödinger equation). An **open** system S is coupled to an environment (bath) E. Tracing over E yields a non-unitary evolution for ρ_S. The most general Markovian (memory-less) master equation that preserves the positivity and trace of ρ is the **Lindblad (GKSL) master equation**:

**定义。** **封闭**量子系统幺正演化：dρ/dt = −(i/ℏ)[Ĥ, ρ]（**冯·诺依曼方程**，薛定谔方程的密度矩阵类比）。**开放**系统 S 与环境（热浴）E 耦合。对 E 求迹得到 ρ_S 的非幺正演化。保持 ρ 正定性和迹的最一般马尔可夫（无记忆）主方程是 **Lindblad（GKSL）主方程**：

  dρ/dt = −(i/ℏ)[Ĥ, ρ] + Σ_k γ_k ( L_k ρ L_k† − ½ L_k†L_k ρ − ½ ρ L_k†L_k ),

where the **Lindblad operators** (jump operators) L_k encode the system–environment coupling channels and γ_k ≥ 0 are the corresponding decay rates. The first term is coherent (Hamiltonian) evolution; the second term is the **dissipator** D[ρ], describing incoherent processes such as spontaneous emission, dephasing, and thermalisation.

其中**林德布拉德算符**（跃迁算符）L_k 编码系统–环境耦合通道，γ_k ≥ 0 为对应的衰减率。第一项是相干（哈密顿量）演化；第二项是**耗散子** D[ρ]，描述非相干过程，如自发辐射、退相位和热化。

**Demonstration — Decoherence.** Consider a two-level system with basis {|0⟩, |1⟩} subject to pure dephasing: L = |1⟩⟨1|, rate γ. The off-diagonal element ρ_{01}(t) = ρ_{01}(0) e^{−γt}. The diagonal (population) elements are unchanged. Coherences decay exponentially with **dephasing time T₂ = 1/γ**, while populations are unaffected — a hallmark of decoherence without energy relaxation. More generally, T₁ is the energy relaxation time and 1/T₂ = 1/(2T₁) + 1/T₂* for additional pure dephasing.

**演示——退相干。** 考虑受纯退相位作用的二能级系统，基为 {|0⟩, |1⟩}：L = |1⟩⟨1|，速率 γ。非对角元 ρ_{01}(t) = ρ_{01}(0) e^{−γt}。对角（布居）元不变。相干度以**退相位时间 T₂ = 1/γ** 指数衰减，而布居数不受影响——这是无能量弛豫的退相干的标志。更一般地，T₁ 是能量弛豫时间，1/T₂ = 1/(2T₁) + 1/T₂*（附加纯退相位）。

**Application.** Decoherence explains the quantum-to-classical transition: environmental entanglement suppresses off-diagonal elements in the pointer basis, making macroscopic superpositions effectively unobservable. This connects the density matrix formalism directly to quantum measurement theory (Module 3.3) and to entanglement (Module 3.13) — decoherence is entanglement between the system and uncontrolled environmental degrees of freedom. In quantum computing, decoherence is the principal source of error; quantum error correction codes are designed to counteract it.

**应用。** 退相干解释了从量子到经典的转变：环境纠缠抑制了指针基下的非对角元，使宏观叠加态在实际上不可观测。这将密度矩阵形式主义直接联系到量子测量理论（模块 3.3）和纠缠（模块 3.13）——退相干就是系统与不受控环境自由度之间的纠缠。在量子计算中，退相干是误差的主要来源；量子纠错码正是为对抗它而设计的。

---

**Self-test (blank page)**

1. State the three defining properties of a density matrix and give the criterion distinguishing pure from mixed states.
2. Write the expectation value formula for an observable A in terms of ρ, and show it reduces to the usual formula for a pure state.
3. Define the partial trace and compute ρ_A for the Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2. What is S(ρ_A)?
4. Write the Lindblad master equation, identify each term, and explain what "Markovian" means.
5. For pure dephasing of a qubit with rate γ, solve for ρ_{01}(t) and define T₂.

**自测（空白页）**

1. 陈述密度矩阵的三个定义性质，并给出区分纯态与混态的判据。
2. 用 ρ 写出可观测量 A 的期望值公式，并证明其对纯态回归为通常的公式。
3. 定义偏迹，并对贝尔态 |Φ+⟩ = (|00⟩ + |11⟩)/√2 计算 ρ_A。S(ρ_A) 是多少？
4. 写出 Lindblad 主方程，指明各项，并解释"马尔可夫"的含义。
5. 对速率为 γ 的量子比特纯退相位，求解 ρ_{01}(t) 并定义 T₂。

---

← Previous: [Module 3.13 — Entanglement, EPR & Bell's Theorem](./module-3.13-entanglement-epr-and-bell.md) · [Phase 3 index](./README.md) · Next: [Module 3.15 — Relativistic Quantum Mechanics](./module-3.15-relativistic-quantum-mechanics.md) →

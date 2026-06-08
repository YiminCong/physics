# Module 3.16 — Quantum Computation & Information
**模块 3.16 — 量子计算与量子信息**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.16-quantum-computation-and-information-derivations.md)

---

## 1. Qubits, Gates, and Quantum Circuits · 量子比特、量子门与量子电路

**Definition.** A **qubit** is the quantum analogue of a classical bit. Where a classical bit is either 0 or 1, a qubit is a unit vector in a two-dimensional complex Hilbert space:

  |ψ⟩ = α|0⟩ + β|1⟩,   |α|² + |β|² = 1,   α, β ∈ ℂ.

The computational basis states |0⟩ = (1, 0)ᵀ and |1⟩ = (0, 1)ᵀ are chosen conventions. The superposition principle (Module 3.1) gives the qubit its power: before measurement it is genuinely in both states simultaneously, with |α|² and |β|² being the probabilities of outcomes 0 and 1.

**定义。** **量子比特（qubit）**是经典比特的量子类比。经典比特非 0 即 1，而量子比特是二维复 Hilbert 空间中的单位向量：

  |ψ⟩ = α|0⟩ + β|1⟩，   |α|² + |β|² = 1，   α, β ∈ ℂ。

计算基矢 |0⟩ = (1, 0)ᵀ 与 |1⟩ = (0, 1)ᵀ 是约定的选择。叠加原理（模块 3.1）赋予量子比特其强大能力：测量前它同时处于两种状态，|α|² 与 |β|² 分别是输出 0 和 1 的概率。

**Definition.** The **Bloch sphere** provides a complete geometric picture of a single-qubit pure state. Writing α = cos(θ/2) and β = e^{iφ} sin(θ/2) (global phase irrelevant), the state is parameterized by the point (θ, φ) on the unit sphere:

  |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩,   0 ≤ θ ≤ π,   0 ≤ φ < 2π.

The north pole (θ = 0) is |0⟩; the south pole (θ = π) is |1⟩; the equator contains equal superpositions such as |+⟩ = (|0⟩ + |1⟩)/√2 (at φ = 0). A single-qubit gate is a **rotation of the Bloch sphere**, i.e., an element of SU(2).

**定义。** **布洛赫球**为单量子比特纯态提供了完整的几何图像。令 α = cos(θ/2)，β = e^{iφ} sin(θ/2)（全局相位无关紧要），状态由单位球面上的点 (θ, φ) 参数化：

  |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩，   0 ≤ θ ≤ π，   0 ≤ φ < 2π。

北极点 (θ = 0) 对应 |0⟩，南极点 (θ = π) 对应 |1⟩，赤道包含诸如 |+⟩ = (|0⟩ + |1⟩)/√2（φ = 0 处）的等权叠加。单量子比特门即**布洛赫球的旋转**，即 SU(2) 的元素。

**Definition.** The fundamental **single-qubit gates** in matrix form (computational basis {|0⟩, |1⟩}):

  Pauli-X (bit flip):   X = [[0, 1], [1, 0]]   — π rotation about x-axis; X|0⟩ = |1⟩, X|1⟩ = |0⟩.

  Pauli-Y:              Y = [[0, −i], [i, 0]]  — π rotation about y-axis.

  Pauli-Z (phase flip):  Z = [[1, 0], [0, −1]]  — π rotation about z-axis; Z|0⟩ = |0⟩, Z|1⟩ = −|1⟩.

  Hadamard:             H = (1/√2) [[1, 1], [1, −1]]  — π rotation about the (x+z)/√2 axis; maps |0⟩ ↔ |+⟩.

  Phase gate:           S = [[1, 0], [0, i]]    — π/2 rotation about z-axis; S² = Z.

  T gate (π/8 gate):    T = [[1, 0], [0, e^{iπ/4}]]  — π/4 rotation about z-axis; T² = S.

All are **unitary** (UU† = I) and **reversible**. H creates superposition from a basis state; S and T introduce non-trivial phases needed for universality.

**定义。** 基本**单量子比特门**的矩阵形式（计算基 {|0⟩, |1⟩}）：

  泡利-X（比特翻转）：  X = [[0, 1], [1, 0]]   — 绕 x 轴旋转 π；X|0⟩ = |1⟩，X|1⟩ = |0⟩。

  泡利-Y：              Y = [[0, −i], [i, 0]]  — 绕 y 轴旋转 π。

  泡利-Z（相位翻转）：  Z = [[1, 0], [0, −1]]  — 绕 z 轴旋转 π；Z|0⟩ = |0⟩，Z|1⟩ = −|1⟩。

  Hadamard：            H = (1/√2) [[1, 1], [1, −1]]  — 绕 (x+z)/√2 轴旋转 π；|0⟩ ↔ |+⟩。

  相位门：              S = [[1, 0], [0, i]]    — 绕 z 轴旋转 π/2；S² = Z。

  T 门（π/8 门）：      T = [[1, 0], [0, e^{iπ/4}]]  — 绕 z 轴旋转 π/4；T² = S。

所有门均为**酉的**（UU† = I）且**可逆**。H 从基矢产生叠加态；S 和 T 引入普适性所需的非平凡相位。

**Definition.** The **CNOT gate** (controlled-NOT) is the canonical two-qubit gate. It acts on a control qubit (c) and a target qubit (t):

  CNOT|c, t⟩ = |c, c ⊕ t⟩,

where ⊕ is addition mod 2. In matrix form on the basis {|00⟩, |01⟩, |10⟩, |11⟩}:

  CNOT = [[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]].

CNOT flips the target if and only if the control is |1⟩. Together with single-qubit gates, the CNOT generates **entanglement**: applying CNOT after H on the control maps |00⟩ → (|00⟩ + |11⟩)/√2, the Bell state Φ⁺ (Module 3.13).

**定义。** **CNOT 门**（受控非门）是典型的双量子比特门，作用于控制量子比特 (c) 和目标量子比特 (t)：

  CNOT|c, t⟩ = |c, c ⊕ t⟩，

其中 ⊕ 是模 2 加法。在基 {|00⟩, |01⟩, |10⟩, |11⟩} 上的矩阵形式：

  CNOT = [[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]。

CNOT 当且仅当控制位为 |1⟩ 时翻转目标位。与单量子比特门结合，CNOT 可**产生纠缠**：对控制位施加 H 后再施加 CNOT，将 |00⟩ 映射到 (|00⟩ + |11⟩)/√2，即贝尔态 Φ⁺（模块 3.13）。

**Definition.** A gate set is **universal** if arbitrary n-qubit unitary operations can be approximated to any desired accuracy using finite sequences of gates from the set. The Solovay–Kitaev theorem guarantees that {H, T, CNOT} (or equivalently {H, S, T, CNOT}) is universal: any unitary U(2ⁿ) can be decomposed into O(n² 4ⁿ) single-qubit and CNOT gates. Intuitively, H and T together generate a dense subset of SU(2) via irrational rotations, while CNOT provides the entangling power to reach arbitrary multi-qubit operations.

**定义。** 若一组门能以任意精度近似任意 n 量子比特的酉操作，则称该门集**普适（universal）**。Solovay–Kitaev 定理保证 {H, T, CNOT}（或等价的 {H, S, T, CNOT}）是普适的：任何 U(2ⁿ) 酉矩阵可分解为 O(n² 4ⁿ) 个单量子比特门与 CNOT 门的序列。直观上，H 与 T 通过无理旋转在 SU(2) 中生成稠密子集，而 CNOT 提供产生任意多量子比特操作所需的纠缠能力。

**Definition.** A **quantum circuit** is a directed acyclic graph of quantum gates applied to an initial state (typically |0⟩^{⊗n}), followed by measurements. Wires represent qubits; boxes represent gates applied left-to-right in time order. The circuit model is the standard framework for quantum algorithms (Module 3.17).

**定义。** **量子电路**是施加于初态（通常为 |0⟩^{⊗n}）的量子门的有向无环图，最终进行测量。导线代表量子比特；方框代表按从左到右的时间顺序施加的门。电路模型是量子算法（模块 3.17）的标准框架。

**Definition.** The **no-cloning theorem** states: there is no unitary operation U such that U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for all quantum states |ψ⟩. Cloning an arbitrary unknown state is impossible. The proof (see Derivations) uses the linearity of quantum mechanics: if U clones two orthogonal states |0⟩ and |1⟩, then by linearity it acts on their superposition as U(α|0⟩+β|1⟩)|0⟩ = α|00⟩+β|11⟩, which is not (α|0⟩+β|1⟩)⊗(α|0⟩+β|1⟩) = α²|00⟩+αβ|01⟩+αβ|10⟩+β²|11⟩ for general α, β. Contradiction.

**定义。** **不可克隆定理**：不存在酉操作 U 使得对所有量子态 |ψ⟩ 成立 U|ψ⟩|0⟩ = |ψ⟩|ψ⟩。复制任意未知量子态是不可能的。证明（见推导）利用量子力学的线性性：若 U 克隆两个正交态 |0⟩ 和 |1⟩，则由线性性，U 对它们的叠加态的作用为 U(α|0⟩+β|1⟩)|0⟩ = α|00⟩+β|11⟩，这对一般的 α, β 不等于 (α|0⟩+β|1⟩)⊗(α|0⟩+β|1⟩) = α²|00⟩+αβ|01⟩+αβ|10⟩+β²|11⟩，矛盾。

---

## 2. Quantum Protocols · 量子协议

**Definition.** **Quantum teleportation** transfers an unknown qubit state |ψ⟩ = α|0⟩+β|1⟩ from Alice to Bob using a pre-shared **Bell pair** (entanglement as a resource, Module 3.13) and two classical bits. No quantum channel is needed after the initial entanglement distribution. The protocol:

  1. Alice holds qubit 1 (the state |ψ⟩ to teleport) and qubit 2 (her half of the Bell pair (|00⟩+|11⟩)/√2).
  2. Bob holds qubit 3 (his half of the Bell pair).
  3. Alice performs a **Bell measurement** on qubits 1 and 2, obtaining one of four outcomes (00, 01, 10, 11), each with probability 1/4.
  4. Alice sends her 2 classical bits to Bob.
  5. Bob applies a correction unitary (I, X, Z, or XZ depending on the classical bits) to qubit 3.
  6. Qubit 3 is now in state |ψ⟩ = α|0⟩+β|1⟩, identical to the original.

The state |ψ⟩ is transferred exactly; no information travels faster than light (the 2 classical bits are needed). The original qubit 1 is destroyed (consistent with no-cloning).

**定义。** **量子隐形传态**利用预先共享的**贝尔对**（纠缠作为资源，模块 3.13）和两个经典比特，将未知量子比特态 |ψ⟩ = α|0⟩+β|1⟩ 从 Alice 传送到 Bob。初始纠缠分发后无需量子信道。协议步骤：

  1. Alice 持有量子比特 1（待传送态 |ψ⟩）和量子比特 2（贝尔对 (|00⟩+|11⟩)/√2 的 Alice 端）。
  2. Bob 持有量子比特 3（贝尔对的 Bob 端）。
  3. Alice 对量子比特 1 和 2 进行**贝尔测量**，得到四个结果之一（00、01、10、11），各以概率 1/4 出现。
  4. Alice 将 2 个经典比特发送给 Bob。
  5. Bob 根据经典比特施加修正酉操作（I、X、Z 或 XZ）于量子比特 3。
  6. 量子比特 3 现处于态 |ψ⟩ = α|0⟩+β|1⟩，与原态完全一致。

态 |ψ⟩ 被精确传输；信息不超光速传播（需要 2 个经典比特）。原始量子比特 1 被破坏（与不可克隆定理一致）。

**Demonstration.** The step-by-step algebra of teleportation (see Derivations) shows that after Alice's Bell measurement the three-qubit state collapses to one of four branches. In each branch, qubit 3 is already in a state that differs from |ψ⟩ by at most a Pauli correction. Bob's single correction restores |ψ⟩ exactly. The key resource consumed is one Bell pair (one ebit) per teleported qubit; the classical communication cost is 2 bits per qubit.

**演示。** 隐形传态的逐步代数（见推导）表明，Alice 贝尔测量后三量子比特态坍缩到四个分支之一。在每个分支中，量子比特 3 已处于至多差一个泡利修正的 |ψ⟩ 态。Bob 的单次修正精确恢复 |ψ⟩。每传送一个量子比特消耗一个贝尔对（一个 ebit），经典通信代价为每量子比特 2 比特。

**Definition.** **Superdense coding** is the reverse information flow: Alice can transmit 2 **classical** bits to Bob by sending just **1 qubit**, using a pre-shared Bell pair. The protocol:

  1. Alice and Bob share the Bell state |Φ⁺⟩ = (|00⟩+|11⟩)/√2; Alice holds qubit 1, Bob qubit 2.
  2. Alice encodes 2 bits (a, b) by applying one of four Pauli operations to her qubit:
       (0,0) → I;   (0,1) → X;   (1,0) → Z;   (1,1) → iY.
     This maps |Φ⁺⟩ to one of the four orthogonal Bell states {|Φ⁺⟩, |Ψ⁺⟩, |Φ⁻⟩, |Ψ⁻⟩}.
  3. Alice sends her qubit to Bob (1 qubit transmitted).
  4. Bob performs a Bell measurement on both qubits and recovers (a, b) perfectly.

Superdense coding achieves 2 classical bits per qubit sent, exceeding the classical 1 bit per physical bit. The entanglement enables this super-classical capacity.

**定义。** **超密编码**是反向信息流：利用预先共享的贝尔对，Alice 仅需发送 **1 个量子比特**即可向 Bob 传输 2 个**经典**比特。协议：

  1. Alice 与 Bob 共享贝尔态 |Φ⁺⟩ = (|00⟩+|11⟩)/√2；Alice 持有量子比特 1，Bob 持有量子比特 2。
  2. Alice 通过对她的量子比特施加四个泡利操作之一来编码 2 比特 (a, b)：
       (0,0) → I；  (0,1) → X；  (1,0) → Z；  (1,1) → iY。
     这将 |Φ⁺⟩ 映射到四个正交贝尔态 {|Φ⁺⟩, |Ψ⁺⟩, |Φ⁻⟩, |Ψ⁻⟩} 之一。
  3. Alice 将她的量子比特发送给 Bob（传输 1 个量子比特）。
  4. Bob 对两个量子比特进行贝尔测量，完美恢复 (a, b)。

超密编码每发送一个量子比特传输 2 个经典比特，超越了经典的每物理比特 1 比特的容量。纠缠使这种超经典容量成为可能。

**Application.** Quantum teleportation and superdense coding illustrate a deep duality: teleportation converts 1 ebit + 2 classical bits → 1 qubit of quantum communication; superdense coding converts 1 ebit + 1 qubit → 2 classical bits. Together they show that **entanglement is a resource** that can substitute for or amplify communication. The **density matrix formalism** (Module 3.14) describes what Bob holds before he receives Alice's classical bits: a maximally mixed state ρ = I/2, consistent with the no-signaling condition. Once the 2 bits arrive, Bob's state collapses to a pure state — the state projection is captured exactly by the partial trace and conditional density matrix.

**应用。** 量子隐形传态与超密编码揭示了一种深刻的对偶性：隐形传态将 1 ebit + 2 经典比特转换为 1 量子比特的量子通信；超密编码将 1 ebit + 1 量子比特转换为 2 经典比特。两者共同表明**纠缠是一种资源**，可以替代或放大通信。**密度矩阵形式体系**（模块 3.14）描述 Bob 在收到 Alice 经典比特前所持有的状态：最大混合态 ρ = I/2，与无信号条件一致。经典比特到达后，Bob 的态坍缩为纯态——态投影精确由偏迹和条件密度矩阵描述。

---

**Self-test (blank page)**

1. Write a general single-qubit state; identify the Bloch sphere angles θ and φ.
2. Give the matrix forms of X, Z, H, and T; verify each is unitary.
3. State the action of CNOT on all four computational basis states.
4. Apply H then CNOT to |00⟩ and show the result is a Bell state.
5. State the no-cloning theorem and sketch the linearity-based proof.
6. List the five steps of quantum teleportation and state what resource it consumes.
7. Explain superdense coding: how many classical bits per qubit sent, and why is entanglement essential?
8. Why does teleportation not violate special relativity?

**自测（空白页）**

1. 写出一般单量子比特态；指明布洛赫球角度 θ 与 φ。
2. 给出 X、Z、H 和 T 的矩阵形式；验证每个均为酉矩阵。
3. 陈述 CNOT 对所有四个计算基矢的作用。
4. 对 |00⟩ 依次施加 H 和 CNOT，证明结果是贝尔态。
5. 陈述不可克隆定理并概述基于线性性的证明。
6. 列出量子隐形传态的五个步骤，并说明它消耗什么资源。
7. 解释超密编码：每个量子比特发送多少经典比特，为何纠缠必不可少？
8. 为何隐形传态不违反狭义相对论？

---

← Previous: [Module 3.15 — Relativistic Quantum Mechanics](./module-3.15-relativistic-quantum-mechanics.md) · [Phase 3 index](./README.md) · Next: [Module 3.17 — Quantum Algorithms & Error Correction](./module-3.17-quantum-algorithms-and-error-correction.md) →

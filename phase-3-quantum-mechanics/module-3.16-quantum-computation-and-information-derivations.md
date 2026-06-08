# Derivations — Module 3.16: Quantum Computation & Information
# 推导 — 模块 3.16：量子计算与量子信息

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.16](./module-3.16-quantum-computation-and-information.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.16](./module-3.16-quantum-computation-and-information.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Quantum Teleportation: Full Circuit Analysis · 量子隐形传态：完整电路分析

**Claim.** The teleportation circuit transmits the unknown state |ψ⟩ = α|0⟩ + β|1⟩ from Alice to Bob perfectly using one Bell pair and two classical bits, without violating no-cloning.

**命题。** 隐形传态电路利用一对贝尔对和两个经典比特，将未知态 |ψ⟩ = α|0⟩ + β|1⟩ 从 Alice 完美传输给 Bob，且不违反不可克隆定理。

**Setup.** Label the qubits 1 (Alice's unknown), 2 (Alice's Bell qubit), 3 (Bob's Bell qubit). The shared Bell pair is |Φ⁺⟩₂₃ = (|00⟩ + |11⟩)/√2.

**设置。** 标记量子比特 1（Alice 的未知态），2（Alice 的贝尔量子比特），3（Bob 的贝尔量子比特）。共享贝尔对为 |Φ⁺⟩₂₃ = (|00⟩ + |11⟩)/√2。

**Step 1 — Initial state.** The full three-qubit state is:

**第 1 步 — 初态。** 完整三量子比特态为：

  |Ψ₀⟩ = |ψ⟩₁ ⊗ |Φ⁺⟩₂₃
       = (α|0⟩₁ + β|1⟩₁) ⊗ (|00⟩ + |11⟩)₂₃ / √2
       = (1/√2)(α|000⟩ + α|011⟩ + β|100⟩ + β|111⟩)₁₂₃.

**Step 2 — Apply CNOT₁₂ (qubit 1 is control, qubit 2 is target).**

**第 2 步 — 施加 CNOT₁₂（量子比特 1 为控制，量子比特 2 为目标）。**

  CNOT₁₂ flips qubit 2 when qubit 1 = |1⟩:

  |Ψ₁⟩ = (1/√2)(α|000⟩ + α|011⟩ + β|110⟩ + β|101⟩)₁₂₃.

**Step 3 — Apply H₁ (Hadamard on qubit 1).** Using H|0⟩ = (|0⟩+|1⟩)/√2 and H|1⟩ = (|0⟩−|1⟩)/√2:

**第 3 步 — 施加 H₁（在量子比特 1 上作用哈达玛门）。** 利用 H|0⟩ = (|0⟩+|1⟩)/√2 和 H|1⟩ = (|0⟩−|1⟩)/√2：

  |Ψ₂⟩ = (1/2)[ α(|0⟩+|1⟩)|00⟩ + α(|0⟩+|1⟩)|11⟩ + β(|0⟩−|1⟩)|10⟩ + β(|0⟩−|1⟩)|01⟩ ]₁₂₃

       = (1/2)[ |00⟩(α|0⟩ + β|1⟩) + |01⟩(α|1⟩ + β|0⟩) + |10⟩(α|0⟩ − β|1⟩) + |11⟩(α|1⟩ − β|0⟩) ]₁₂,₃.

**Step 4 — Rewrite in terms of Bob's corrections.** Identify the four branches by Alice's measurement outcome (m₁m₂):

**第 4 步 — 用 Bob 的修正重写。** 按 Alice 的测量结果（m₁m₂）识别四个分支：

  m₁m₂ = 00:   Bob's state is α|0⟩ + β|1⟩ = |ψ⟩.   Correction: I.
  m₁m₂ = 01:   Bob's state is α|1⟩ + β|0⟩ = X|ψ⟩.   Correction: X.
  m₁m₂ = 10:   Bob's state is α|0⟩ − β|1⟩ = Z|ψ⟩.   Correction: Z.
  m₁m₂ = 11:   Bob's state is α|1⟩ − β|0⟩ = ZX|ψ⟩.   Correction: ZX.

Each outcome has probability 1/4, independent of α and β: Alice learns nothing about |ψ⟩ from her measurement.

每种结果的概率均为 1/4，与 α 和 β 无关：Alice 从测量中对 |ψ⟩ 一无所知。

**Step 5 — Bob applies the correction.** Alice sends m₁ and m₂ (2 classical bits) to Bob. Bob applies the corresponding gate (I, X, Z, or ZX) to qubit 3. In all four cases he recovers |ψ⟩₃ = α|0⟩ + β|1⟩. ∎

**第 5 步 — Bob 施加修正。** Alice 将 m₁ 和 m₂（2 个经典比特）发送给 Bob。Bob 对量子比特 3 施加相应的门（I、X、Z 或 ZX）。在所有四种情况下，他均恢复 |ψ⟩₃ = α|0⟩ + β|1⟩。∎

**Why no-cloning is not violated.** Before Alice's measurement, Bob's reduced density matrix is Tr₁₂(|Ψ₂⟩⟨Ψ₂|) = (1/2)I — the maximally mixed state, independent of |ψ⟩. After Alice's measurement, qubit 1 is in a definite classical outcome state (not |ψ⟩ itself), and qubit 3 holds a version of |ψ⟩ only after the classical correction. The original state on qubit 1 has been destroyed (measured), so there is never a moment when two copies of |ψ⟩ coexist.

**为何不违反不可克隆定理。** 在 Alice 测量之前，Bob 的约化密度矩阵为 Tr₁₂(|Ψ₂⟩⟨Ψ₂|) = (1/2)I——最大混合态，与 |ψ⟩ 无关。Alice 测量后，量子比特 1 处于确定的经典结果态（而非 |ψ⟩ 本身），量子比特 3 只有在经典修正之后才持有 |ψ⟩ 的版本。量子比特 1 上的原始态已被销毁（测量），因此从不存在 |ψ⟩ 的两个副本同时存在的时刻。

---

## B. Superdense Coding: Full Protocol · 超密编码：完整协议

**Claim.** One qubit of quantum communication, assisted by a pre-shared Bell pair, can convey 2 classical bits.

**命题。** 一个量子比特的量子通信，在预共享贝尔对的辅助下，可以传递 2 个经典比特。

**Setup.** Alice and Bob share |Φ⁺⟩ = (|00⟩ + |11⟩)/√2, with Alice holding qubit 1.

**设置。** Alice 和 Bob 共享 |Φ⁺⟩ = (|00⟩ + |11⟩)/√2，Alice 持有量子比特 1。

**Step 1 — Alice's encoding.** Alice applies one of four operations to her qubit:

**第 1 步 — Alice 的编码。** Alice 对其量子比特施加四种操作之一：

  bits 00 → apply I:   (I ⊗ I)|Φ⁺⟩ = |Φ⁺⟩ = (|00⟩ + |11⟩)/√2.
  bits 01 → apply X:   (X ⊗ I)|Φ⁺⟩ = |Ψ⁺⟩ = (|10⟩ + |01⟩)/√2.
  bits 10 → apply Z:   (Z ⊗ I)|Φ⁺⟩ = |Φ⁻⟩ = (|00⟩ − |11⟩)/√2.
  bits 11 → apply ZX:  (ZX ⊗ I)|Φ⁺⟩ = |Ψ⁻⟩ = (|10⟩ − |01⟩)/√2.

The four operations map |Φ⁺⟩ to the four Bell states {|Φ⁺⟩, |Ψ⁺⟩, |Φ⁻⟩, |Ψ⁻⟩}, which are orthonormal and hence perfectly distinguishable.

四种操作将 |Φ⁺⟩ 映射到四个贝尔态 {|Φ⁺⟩, |Ψ⁺⟩, |Φ⁻⟩, |Ψ⁻⟩}，这四个态正交归一，因此可以完美区分。

**Step 2 — Alice sends qubit 1 to Bob.** Bob now holds both qubits of the Bell state.

**第 2 步 — Alice 将量子比特 1 发送给 Bob。** Bob 现在持有贝尔态的两个量子比特。

**Step 3 — Bob's Bell measurement.** Bob applies CNOT₁₂ (qubit 1 control, qubit 2 target) then H₁:

**第 3 步 — Bob 的贝尔测量。** Bob 施加 CNOT₁₂（量子比特 1 为控制，量子比特 2 为目标），然后 H₁：

  |Φ⁺⟩ = (|00⟩+|11⟩)/√2  →CNOT→  (|00⟩+|10⟩)/√2 = |+⟩|0⟩  →H⊗I→  |00⟩.
  |Ψ⁺⟩ = (|10⟩+|01⟩)/√2  →CNOT→  (|11⟩+|01⟩)/√2 = |+⟩|1⟩  →H⊗I→  |01⟩.
  |Φ⁻⟩ = (|00⟩−|11⟩)/√2  →CNOT→  (|00⟩−|10⟩)/√2 = |−⟩|0⟩  →H⊗I→  |10⟩.
  |Ψ⁻⟩ = (|10⟩−|01⟩)/√2  →CNOT→  (|11⟩−|01⟩)/√2 = |−⟩|1⟩  →H⊗I→  |11⟩.

Bob measures in the computational basis and reads Alice's 2 bits exactly. ∎

Bob 在计算基中测量，精确读出 Alice 的 2 个比特。∎

**Duality with teleportation.** Teleportation uses 1 ebit + 2 cbits to send 1 qubit; superdense coding uses 1 ebit + 1 qubit to send 2 cbits. Swapping the roles of quantum channel and classical channel, and of sender and receiver, converts one protocol into the other.

**与隐形传态的对偶性。** 隐形传态使用 1 ebit + 2 个经典比特发送 1 个量子比特；超密编码使用 1 ebit + 1 个量子比特发送 2 个经典比特。交换量子信道和经典信道的角色，以及发送方和接收方，可将一个协议转换为另一个。

---

## C. The No-Cloning Theorem: Proof by Linearity and by Unitarity · 不可克隆定理：线性性证明与酉性证明

**Claim.** There is no unitary U such that U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for all |ψ⟩.

**命题。** 不存在酉算符 U，使得对所有 |ψ⟩ 均有 U|ψ⟩|0⟩ = |ψ⟩|ψ⟩。

### C.1 Proof by Linearity · 线性性证明

**Step 1.** Suppose U works for two specific states |0⟩ and |1⟩:

**第 1 步。** 假设 U 对两个特定态 |0⟩ 和 |1⟩ 有效：

  U|0⟩|0⟩ = |0⟩|0⟩,
  U|1⟩|0⟩ = |1⟩|1⟩.

**Step 2.** Consider the superposition |ψ⟩ = (|0⟩ + |1⟩)/√2. By linearity of U:

**第 2 步。** 考虑叠加态 |ψ⟩ = (|0⟩ + |1⟩)/√2。由 U 的线性性：

  U|ψ⟩|0⟩ = U (|0⟩+|1⟩)/√2 ⊗ |0⟩
           = (U|0⟩|0⟩ + U|1⟩|0⟩)/√2
           = (|00⟩ + |11⟩)/√2.

**Step 3.** But the cloning condition requires:

**第 3 步。** 但克隆条件要求：

  U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ = (|0⟩+|1⟩)/√2 ⊗ (|0⟩+|1⟩)/√2
           = (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2.

**Step 4 — Contradiction.** The results of Steps 2 and 3 are different:

**第 4 步——矛盾。** 第 2 步和第 3 步的结果不同：

  (|00⟩ + |11⟩)/√2  ≠  (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2.

Therefore no linear (and hence no unitary) operator can clone an arbitrary quantum state. ∎

因此，没有线性（从而也没有酉）算符能克隆任意量子态。∎

### C.2 Proof by Unitarity (inner product argument) · 酉性证明（内积论证）

**Step 1.** Suppose U clones: U|φ⟩|0⟩ = |φ⟩|φ⟩ and U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ for arbitrary |φ⟩ and |ψ⟩.

**第 1 步。** 假设 U 可克隆：U|φ⟩|0⟩ = |φ⟩|φ⟩ 且 U|ψ⟩|0⟩ = |ψ⟩|ψ⟩ 对任意 |φ⟩ 和 |ψ⟩ 成立。

**Step 2.** Take the inner product of the two cloned states. Since U is unitary it preserves inner products:

**第 2 步。** 对两个克隆态取内积。因为 U 是酉的，它保持内积：

  ⟨φ|ψ⟩ · ⟨0|0⟩ = ⟨φ|ψ⟩²,

so  ⟨φ|ψ⟩ = ⟨φ|ψ⟩².

**Step 3.** The equation z = z² (with z = ⟨φ|ψ⟩ ∈ ℂ, |z| ≤ 1) has only two solutions: z = 0 or z = 1.

**第 3 步。** 方程 z = z²（其中 z = ⟨φ|ψ⟩ ∈ ℂ，|z| ≤ 1）只有两个解：z = 0 或 z = 1。

**Step 4 — Conclusion.** This means U can only clone pairs of states that are either orthogonal (⟨φ|ψ⟩ = 0) or identical (⟨φ|ψ⟩ = 1). It cannot clone an arbitrary unknown state drawn from a continuous family. ∎

**第 4 步——结论。** 这意味着 U 只能克隆正交（⟨φ|ψ⟩ = 0）或相同（⟨φ|ψ⟩ = 1）的态对。它不能克隆来自连续族的任意未知态。∎

**Physical interpretation.** The no-cloning theorem has a direct security application: in the BB84 protocol (Module 3.17), an eavesdropper cannot copy the transmitted qubits without disturbing them — the disturbance is detectable. The theorem also implies **no-broadcasting** for mixed states and **no-deleting** (by time-reversal symmetry), forming the basis of quantum information theory.

**物理诠释。** 不可克隆定理有直接的安全应用：在 BB84 协议（模块 3.17）中，窃听者无法在不干扰的情况下复制传输的量子比特——干扰是可检测的。该定理还蕴含混合态的**不可广播**定理和**不可删除**定理（通过时间反演对称性），构成量子信息理论的基础。

---

*Derivation document for Module 3.16. All proofs are complete, bilingual, and include the physical interpretation of each result.*

*模块 3.16 的推导文档。所有证明完整、双语，并包含每个结果的物理诠释。*

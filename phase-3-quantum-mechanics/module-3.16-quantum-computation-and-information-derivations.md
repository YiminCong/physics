---
title: "Derivations — Module 3.16: Quantum Computation & Information"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.16: Quantum Computation & Information
# 推导 — 模块 3.16：量子计算与量子信息

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.16](./module-3.16-quantum-computation-and-information.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.16](./module-3.16-quantum-computation-and-information.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Quantum Teleportation: Full Circuit Analysis · 量子隐形传态：完整电路分析

**Claim.** The teleportation circuit transmits the unknown state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ from Alice to Bob perfectly using one Bell pair and two classical bits, without violating no-cloning.

**命题。** 隐形传态电路利用一对贝尔对和两个经典比特，将未知态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 从 Alice 完美传输给 Bob，且不违反不可克隆定理。

**Setup.** Label the qubits 1 (Alice's unknown), 2 (Alice's Bell qubit), 3 (Bob's Bell qubit). The shared Bell pair is $|\Phi^+\rangle_{23} = (|00\rangle + |11\rangle)/\sqrt{2}$.

**设置。** 标记量子比特 1（Alice 的未知态），2（Alice 的贝尔量子比特），3（Bob 的贝尔量子比特）。共享贝尔对为 $|\Phi^+\rangle_{23} = (|00\rangle + |11\rangle)/\sqrt{2}$。

**Step 1 — Initial state.** The full three-qubit state is:

**第 1 步 — 初态。** 完整三量子比特态为：

$$ \begin{aligned} |\Psi_0\rangle &= |\psi\rangle_1 \otimes |\Phi^+\rangle_{23} \\ &= (\alpha|0\rangle_1 + \beta|1\rangle_1) \otimes (|00\rangle + |11\rangle)_{23} / \sqrt{2} \\ &= \tfrac{1}{\sqrt{2}}(\alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle)_{123}. \end{aligned} $$

**Step 2 — Apply $\text{CNOT}_{12}$ (qubit 1 is control, qubit 2 is target).**

**第 2 步 — 施加 $\text{CNOT}_{12}$（量子比特 1 为控制，量子比特 2 为目标）。**

$\text{CNOT}_{12}$ flips qubit 2 when qubit 1 $= |1\rangle$:

$$ |\Psi_1\rangle = \tfrac{1}{\sqrt{2}}(\alpha|000\rangle + \alpha|011\rangle + \beta|110\rangle + \beta|101\rangle)_{123}. $$

**Step 3 — Apply $H_1$ (Hadamard on qubit 1).** Using $H|0\rangle = (|0\rangle+|1\rangle)/\sqrt{2}$ and $H|1\rangle = (|0\rangle-|1\rangle)/\sqrt{2}$:

**第 3 步 — 施加 $H_1$（在量子比特 1 上作用哈达玛门）。** 利用 $H|0\rangle = (|0\rangle+|1\rangle)/\sqrt{2}$ 和 $H|1\rangle = (|0\rangle-|1\rangle)/\sqrt{2}$：

$$ \begin{aligned} |\Psi_2\rangle &= \tfrac{1}{2}[\, \alpha(|0\rangle+|1\rangle)|00\rangle + \alpha(|0\rangle+|1\rangle)|11\rangle + \beta(|0\rangle-|1\rangle)|10\rangle + \beta(|0\rangle-|1\rangle)|01\rangle \,]_{123} \\ &= \tfrac{1}{2}[\, |00\rangle(\alpha|0\rangle + \beta|1\rangle) + |01\rangle(\alpha|1\rangle + \beta|0\rangle) + |10\rangle(\alpha|0\rangle - \beta|1\rangle) + |11\rangle(\alpha|1\rangle - \beta|0\rangle) \,]_{12,3}. \end{aligned} $$

**Step 4 — Rewrite in terms of Bob's corrections.** Identify the four branches by Alice's measurement outcome ($m_1 m_2$):

**第 4 步 — 用 Bob 的修正重写。** 按 Alice 的测量结果（$m_1 m_2$）识别四个分支：

$$ \begin{aligned} m_1 m_2 = 00:&\quad \text{Bob's state is } \alpha|0\rangle + \beta|1\rangle = |\psi\rangle.\quad \text{Correction: } I. \\ m_1 m_2 = 01:&\quad \text{Bob's state is } \alpha|1\rangle + \beta|0\rangle = X|\psi\rangle.\quad \text{Correction: } X. \\ m_1 m_2 = 10:&\quad \text{Bob's state is } \alpha|0\rangle - \beta|1\rangle = Z|\psi\rangle.\quad \text{Correction: } Z. \\ m_1 m_2 = 11:&\quad \text{Bob's state is } \alpha|1\rangle - \beta|0\rangle = ZX|\psi\rangle.\quad \text{Correction: } ZX. \end{aligned} $$

Each outcome has probability $1/4$, independent of $\alpha$ and $\beta$: Alice learns nothing about $|\psi\rangle$ from her measurement.

每种结果的概率均为 $1/4$，与 $\alpha$ 和 $\beta$ 无关：Alice 从测量中对 $|\psi\rangle$ 一无所知。

**Step 5 — Bob applies the correction.** Alice sends $m_1$ and $m_2$ (2 classical bits) to Bob. Bob applies the corresponding gate ($I$, $X$, $Z$, or $ZX$) to qubit 3. In all four cases he recovers $|\psi\rangle_3 = \alpha|0\rangle + \beta|1\rangle$. $\blacksquare$

**第 5 步 — Bob 施加修正。** Alice 将 $m_1$ 和 $m_2$（2 个经典比特）发送给 Bob。Bob 对量子比特 3 施加相应的门（$I$、$X$、$Z$ 或 $ZX$）。在所有四种情况下，他均恢复 $|\psi\rangle_3 = \alpha|0\rangle + \beta|1\rangle$。$\blacksquare$

**Why no-cloning is not violated.** Before Alice's measurement, Bob's reduced density matrix is $\mathrm{Tr}_{12}(|\Psi_2\rangle\langle\Psi_2|) = \tfrac12 I$ — the maximally mixed state, independent of $|\psi\rangle$. After Alice's measurement, qubit 1 is in a definite classical outcome state (not $|\psi\rangle$ itself), and qubit 3 holds a version of $|\psi\rangle$ only after the classical correction. The original state on qubit 1 has been destroyed (measured), so there is never a moment when two copies of $|\psi\rangle$ coexist.

**为何不违反不可克隆定理。** 在 Alice 测量之前，Bob 的约化密度矩阵为 $\mathrm{Tr}_{12}(|\Psi_2\rangle\langle\Psi_2|) = \tfrac12 I$——最大混合态，与 $|\psi\rangle$ 无关。Alice 测量后，量子比特 1 处于确定的经典结果态（而非 $|\psi\rangle$ 本身），量子比特 3 只有在经典修正之后才持有 $|\psi\rangle$ 的版本。量子比特 1 上的原始态已被销毁（测量），因此从不存在 $|\psi\rangle$ 的两个副本同时存在的时刻。

---

## B. Superdense Coding: Full Protocol · 超密编码：完整协议

**Claim.** One qubit of quantum communication, assisted by a pre-shared Bell pair, can convey 2 classical bits.

**命题。** 一个量子比特的量子通信，在预共享贝尔对的辅助下，可以传递 2 个经典比特。

**Setup.** Alice and Bob share $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$, with Alice holding qubit 1.

**设置。** Alice 和 Bob 共享 $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$，Alice 持有量子比特 1。

**Step 1 — Alice's encoding.** Alice applies one of four operations to her qubit:

**第 1 步 — Alice 的编码。** Alice 对其量子比特施加四种操作之一：

$$ \begin{aligned} \text{bits } 00 \to \text{apply } I:&\quad (I \otimes I)|\Phi^+\rangle = |\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}. \\ \text{bits } 01 \to \text{apply } X:&\quad (X \otimes I)|\Phi^+\rangle = |\Psi^+\rangle = (|10\rangle + |01\rangle)/\sqrt{2}. \\ \text{bits } 10 \to \text{apply } Z:&\quad (Z \otimes I)|\Phi^+\rangle = |\Phi^-\rangle = (|00\rangle - |11\rangle)/\sqrt{2}. \\ \text{bits } 11 \to \text{apply } ZX:&\quad (ZX \otimes I)|\Phi^+\rangle = |\Psi^-\rangle = (|10\rangle - |01\rangle)/\sqrt{2}. \end{aligned} $$

The four operations map $|\Phi^+\rangle$ to the four Bell states $\{|\Phi^+\rangle, |\Psi^+\rangle, |\Phi^-\rangle, |\Psi^-\rangle\}$, which are orthonormal and hence perfectly distinguishable.

四种操作将 $|\Phi^+\rangle$ 映射到四个贝尔态 $\{|\Phi^+\rangle, |\Psi^+\rangle, |\Phi^-\rangle, |\Psi^-\rangle\}$，这四个态正交归一，因此可以完美区分。

**Step 2 — Alice sends qubit 1 to Bob.** Bob now holds both qubits of the Bell state.

**第 2 步 — Alice 将量子比特 1 发送给 Bob。** Bob 现在持有贝尔态的两个量子比特。

**Step 3 — Bob's Bell measurement.** Bob applies $\text{CNOT}_{12}$ (qubit 1 control, qubit 2 target) then $H_1$:

**第 3 步 — Bob 的贝尔测量。** Bob 施加 $\text{CNOT}_{12}$（量子比特 1 为控制，量子比特 2 为目标），然后 $H_1$：

$$ \begin{aligned} |\Phi^+\rangle = (|00\rangle+|11\rangle)/\sqrt{2} &\xrightarrow{\text{CNOT}} (|00\rangle+|10\rangle)/\sqrt{2} = |+\rangle|0\rangle \xrightarrow{H\otimes I} |00\rangle. \\ |\Psi^+\rangle = (|10\rangle+|01\rangle)/\sqrt{2} &\xrightarrow{\text{CNOT}} (|11\rangle+|01\rangle)/\sqrt{2} = |+\rangle|1\rangle \xrightarrow{H\otimes I} |01\rangle. \\ |\Phi^-\rangle = (|00\rangle-|11\rangle)/\sqrt{2} &\xrightarrow{\text{CNOT}} (|00\rangle-|10\rangle)/\sqrt{2} = |-\rangle|0\rangle \xrightarrow{H\otimes I} |10\rangle. \\ |\Psi^-\rangle = (|10\rangle-|01\rangle)/\sqrt{2} &\xrightarrow{\text{CNOT}} (|11\rangle-|01\rangle)/\sqrt{2} = |-\rangle|1\rangle \xrightarrow{H\otimes I} |11\rangle. \end{aligned} $$

Bob measures in the computational basis and reads Alice's 2 bits exactly. $\blacksquare$

Bob 在计算基中测量，精确读出 Alice 的 2 个比特。$\blacksquare$

**Duality with teleportation.** Teleportation uses 1 ebit + 2 cbits to send 1 qubit; superdense coding uses 1 ebit + 1 qubit to send 2 cbits. Swapping the roles of quantum channel and classical channel, and of sender and receiver, converts one protocol into the other.

**与隐形传态的对偶性。** 隐形传态使用 1 ebit + 2 个经典比特发送 1 个量子比特；超密编码使用 1 ebit + 1 个量子比特发送 2 个经典比特。交换量子信道和经典信道的角色，以及发送方和接收方，可将一个协议转换为另一个。

---

## C. The No-Cloning Theorem: Proof by Linearity and by Unitarity · 不可克隆定理：线性性证明与酉性证明

**Claim.** There is no unitary $U$ such that $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for all $|\psi\rangle$.

**命题。** 不存在酉算符 $U$，使得对所有 $|\psi\rangle$ 均有 $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$。

### C.1 Proof by Linearity · 线性性证明

**Step 1.** Suppose $U$ works for two specific states $|0\rangle$ and $|1\rangle$:

**第 1 步。** 假设 $U$ 对两个特定态 $|0\rangle$ 和 $|1\rangle$ 有效：

$$ U|0\rangle|0\rangle = |0\rangle|0\rangle, \qquad U|1\rangle|0\rangle = |1\rangle|1\rangle. $$

**Step 2.** Consider the superposition $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. By linearity of $U$:

**第 2 步。** 考虑叠加态 $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$。由 $U$ 的线性性：

$$ U|\psi\rangle|0\rangle = U (|0\rangle+|1\rangle)/\sqrt{2} \otimes |0\rangle = (U|0\rangle|0\rangle + U|1\rangle|0\rangle)/\sqrt{2} = (|00\rangle + |11\rangle)/\sqrt{2}. $$

**Step 3.** But the cloning condition requires:

**第 3 步。** 但克隆条件要求：

$$ U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle = (|0\rangle+|1\rangle)/\sqrt{2} \otimes (|0\rangle+|1\rangle)/\sqrt{2} = (|00\rangle + |01\rangle + |10\rangle + |11\rangle)/2. $$

**Step 4 — Contradiction.** The results of Steps 2 and 3 are different:

**第 4 步——矛盾。** 第 2 步和第 3 步的结果不同：

$$ (|00\rangle + |11\rangle)/\sqrt{2} \ne (|00\rangle + |01\rangle + |10\rangle + |11\rangle)/2. $$

Therefore no linear (and hence no unitary) operator can clone an arbitrary quantum state. $\blacksquare$

因此，没有线性（从而也没有酉）算符能克隆任意量子态。$\blacksquare$

### C.2 Proof by Unitarity (inner product argument) · 酉性证明（内积论证）

**Step 1.** Suppose $U$ clones: $U|\varphi\rangle|0\rangle = |\varphi\rangle|\varphi\rangle$ and $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for arbitrary $|\varphi\rangle$ and $|\psi\rangle$.

**第 1 步。** 假设 $U$ 可克隆：$U|\varphi\rangle|0\rangle = |\varphi\rangle|\varphi\rangle$ 且 $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ 对任意 $|\varphi\rangle$ 和 $|\psi\rangle$ 成立。

**Step 2.** Take the inner product of the two cloned states. Since $U$ is unitary it preserves inner products:

**第 2 步。** 对两个克隆态取内积。因为 $U$ 是酉的，它保持内积：

$$ \langle\varphi|\psi\rangle \cdot \langle 0|0\rangle = \langle\varphi|\psi\rangle^2, $$

so $\langle\varphi|\psi\rangle = \langle\varphi|\psi\rangle^2$.

**Step 3.** The equation $z = z^2$ (with $z = \langle\varphi|\psi\rangle \in \mathbb{C}$, $|z| \le 1$) has only two solutions: $z = 0$ or $z = 1$.

**第 3 步。** 方程 $z = z^2$（其中 $z = \langle\varphi|\psi\rangle \in \mathbb{C}$，$|z| \le 1$）只有两个解：$z = 0$ 或 $z = 1$。

**Step 4 — Conclusion.** This means $U$ can only clone pairs of states that are either orthogonal ($\langle\varphi|\psi\rangle = 0$) or identical ($\langle\varphi|\psi\rangle = 1$). It cannot clone an arbitrary unknown state drawn from a continuous family. $\blacksquare$

**第 4 步——结论。** 这意味着 $U$ 只能克隆正交（$\langle\varphi|\psi\rangle = 0$）或相同（$\langle\varphi|\psi\rangle = 1$）的态对。它不能克隆来自连续族的任意未知态。$\blacksquare$

**Physical interpretation.** The no-cloning theorem has a direct security application: in the BB84 protocol (Module 3.17), an eavesdropper cannot copy the transmitted qubits without disturbing them — the disturbance is detectable. The theorem also implies **no-broadcasting** for mixed states and **no-deleting** (by time-reversal symmetry), forming the basis of quantum information theory.

**物理诠释。** 不可克隆定理有直接的安全应用：在 BB84 协议（模块 3.17）中，窃听者无法在不干扰的情况下复制传输的量子比特——干扰是可检测的。该定理还蕴含混合态的**不可广播**定理和**不可删除**定理（通过时间反演对称性），构成量子信息理论的基础。

---

*Derivation document for Module 3.16. All proofs are complete, bilingual, and include the physical interpretation of each result.*

*模块 3.16 的推导文档。所有证明完整、双语，并包含每个结果的物理诠释。*

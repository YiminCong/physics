# Module 3.17 — Quantum Algorithms & Error Correction
**模块 3.17 — 量子算法与量子纠错**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.17-quantum-algorithms-and-error-correction-derivations.md)

---

## 1. Quantum Algorithms · 量子算法

**Definition.** **Quantum parallelism** is the ability of a quantum computer to evaluate a function $f$ on all $n$-bit inputs simultaneously by preparing the superposition $(1/\sqrt{2^n}) \sum_x |x\rangle|0\rangle$ and applying the unitary $U_f: |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$. After $U_f$, the register holds $(1/\sqrt{2^n}) \sum_x |x\rangle|f(x)\rangle$ — all function values are encoded simultaneously. However, a single measurement collapses this to one outcome; the art of quantum algorithm design is to use **quantum interference** to amplify the probability of the desired answer.

**定义。** **量子并行性**是量子计算机通过制备叠加态 $(1/\sqrt{2^n}) \sum_x |x\rangle|0\rangle$ 并施加酉算符 $U_f: |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle$，同时对所有 $n$ 比特输入求值函数 $f$ 的能力。$U_f$ 作用后，寄存器持有 $(1/\sqrt{2^n}) \sum_x |x\rangle|f(x)\rangle$——所有函数值同时编码。然而，单次测量会将其坍缩到一个结果；量子算法设计的艺术在于利用**量子干涉**来放大期望答案的概率。

**Definition.** The **Deutsch–Jozsa algorithm** (1992) solves the following problem in one query: given a function $f: \{0,1\}^n \to \{0,1\}$ promised to be either **constant** (same output for all inputs) or **balanced** (exactly half of inputs map to 0, half to 1), determine which. Classically, $2^{n-1} + 1$ queries are needed in the worst case. The quantum algorithm uses one application of $U_f$ and is the simplest demonstration of exponential quantum speed-up (for a promise problem). See Derivations for the full circuit analysis.

**定义。** **Deutsch–Jozsa 算法**（1992 年）用一次查询解决以下问题：给定函数 $f: \{0,1\}^n \to \{0,1\}$，已知其要么是**常数**（对所有输入给出相同输出）要么是**平衡**的（恰好一半输入映射到 0，一半到 1），判断是哪种情况。经典情况下，最坏情况需要 $2^{n-1} + 1$ 次查询。量子算法只用一次 $U_f$，是指数级量子加速（对于承诺问题）最简单的演示。完整电路分析见推导文档。

**Definition.** **Grover's search algorithm** (1996) searches an unstructured database of $N$ items for a marked item in $O(\sqrt{N})$ queries — a quadratic speed-up over the classical $O(N)$. It works by iterating the **Grover operator** $G = (2|s\rangle\langle s| - I)(2|w\rangle\langle w| - I)$, where $|s\rangle = (1/\sqrt{N}) \sum_x |x\rangle$ is the uniform superposition and $|w\rangle$ is the marked state. Each Grover iteration geometrically rotates the state vector in the two-dimensional subspace spanned by $|s\rangle$ and $|w\rangle$ by an angle $2\theta$ where $\sin\theta = 1/\sqrt{N}$. After $\sim\pi/(4\theta) \approx (\pi/4)\sqrt{N}$ iterations, the amplitude on $|w\rangle$ is close to 1. This is **provably optimal**: no quantum algorithm can search an unstructured database in fewer than $O(\sqrt{N})$ queries (BBBV theorem).

**定义。** **Grover 搜索算法**（1996 年）在 $O(\sqrt{N})$ 次查询内搜索 $N$ 个未标记项的数据库中的目标项——比经典 $O(N)$ 有平方级加速。其工作原理是迭代 **Grover 算符** $G = (2|s\rangle\langle s| - I)(2|w\rangle\langle w| - I)$，其中 $|s\rangle = (1/\sqrt{N}) \sum_x |x\rangle$ 是均匀叠加态，$|w\rangle$ 是目标态。每次 Grover 迭代在 $|s\rangle$ 和 $|w\rangle$ 张成的二维子空间中将态矢量几何旋转角度 $2\theta$，其中 $\sin\theta = 1/\sqrt{N}$。经过约 $\pi/(4\theta) \approx (\pi/4)\sqrt{N}$ 次迭代后，$|w\rangle$ 上的振幅接近 1。这是**可证明最优的**：没有量子算法能在少于 $O(\sqrt{N})$ 次查询内搜索无结构数据库（BBBV 定理）。

**Definition.** The **Quantum Fourier Transform (QFT)** on $n$ qubits maps $|j\rangle \to (1/\sqrt{2^n}) \sum_k e^{2\pi i jk/2^n} |k\rangle$. It is the quantum analogue of the discrete Fourier transform but implemented with $O(n^2)$ gates instead of the classical $O(n\cdot 2^n)$ — an exponential improvement in gate count. The QFT is the key subroutine in **Shor's factoring algorithm** (1994), which factors an integer $N$ in $O((\log N)^3)$ time (polynomial) compared to the best known classical algorithm which runs in sub-exponential time $O(\exp((\log N)^{1/3} (\log\log N)^{2/3}))$. Shor's algorithm reduces factoring to **order finding**: given $a \in \mathbb{Z}_N^*$ coprime to $N$, find the period $r$ of the function $f(x) = a^x \bmod N$. The QFT extracts $r$ from the periodic superposition created by the modular exponentiation step. The period $r$ satisfying $a^r \equiv 1 \pmod{N}$ reveals the factors via $\gcd(a^{r/2} \pm 1, N)$.

**定义。** $n$ 个量子比特上的**量子傅里叶变换（QFT）**将 $|j\rangle$ 映射到 $(1/\sqrt{2^n}) \sum_k e^{2\pi i jk/2^n} |k\rangle$。它是离散傅里叶变换的量子类比，但用 $O(n^2)$ 个门实现，而非经典的 $O(n\cdot 2^n)$——门数的指数级改进。QFT 是**Shor 因式分解算法**（1994 年）的关键子程序，该算法在 $O((\log N)^3)$ 时间内（多项式时间）对整数 $N$ 进行因式分解，而已知最佳经典算法的时间为亚指数级 $O(\exp((\log N)^{1/3} (\log\log N)^{2/3}))$。Shor 算法将因式分解归约为**阶的求解**：给定与 $N$ 互素的 $a \in \mathbb{Z}_N^*$，求函数 $f(x) = a^x \bmod N$ 的周期 $r$。QFT 从模幂运算步骤创建的周期叠加态中提取 $r$。满足 $a^r \equiv 1 \pmod{N}$ 的周期 $r$ 通过 $\gcd(a^{r/2} \pm 1, N)$ 揭示因子。

**Definition.** **BB84** (Bennett & Brassard 1984) is the first quantum key distribution protocol. Alice sends qubits prepared in one of four states: $|0\rangle$, $|1\rangle$, $|+\rangle$, $|-\rangle$ (two bases: $Z = \{|0\rangle,|1\rangle\}$ and $X = \{|+\rangle,|-\rangle\}$). She randomly chooses the basis for each qubit; Bob randomly chooses a measurement basis. After transmission, they publicly announce their bases (not results) and keep only the bits where bases matched ($\approx 50\%$). Any eavesdropper (Eve) who measures in the wrong basis disturbs the state; her presence is detected by a higher error rate ($\geq 25\%$ if Eve measures all qubits). Security is guaranteed by the no-cloning theorem (Module 3.16) and the uncertainty principle (Module 3.3).

**定义。** **BB84**（Bennett & Brassard，1984 年）是第一个量子密钥分发协议。Alice 以四种态之一发送量子比特：$|0\rangle$、$|1\rangle$、$|+\rangle$、$|-\rangle$（两个基：$Z = \{|0\rangle,|1\rangle\}$ 和 $X = \{|+\rangle,|-\rangle\}$）。她为每个量子比特随机选择基；Bob 随机选择测量基。传输后，他们公开宣布各自的基（非结果）并只保留基匹配的比特（约 $50\%$）。任何以错误基测量的窃听者（Eve）都会扰动态；她的存在通过更高的错误率（若 Eve 测量所有量子比特则 $\geq 25\%$）被检测到。安全性由不可克隆定理（模块 3.16）和不确定性原理（模块 3.3）保证。

---

## 2. Quantum Error Correction · 量子纠错

**Definition.** **Decoherence** (Module 3.14) is the primary obstacle to quantum computation: interaction of the qubit with its environment causes the density matrix to lose off-diagonal coherences, converting pure states into mixed states. A qubit subject to decoherence undergoes: bit-flip errors ($|0\rangle \to |1\rangle$, equivalent to $X$), phase-flip errors ($|+\rangle \to |-\rangle$, equivalent to $Z$), or combinations ($Y = iXZ$). Quantum error correction (QEC) must protect against a continuous set of errors; the key insight is that **measuring the error syndrome** (not the logical qubit) discretises the error set, reducing it to the Pauli group.

**定义。** **退相干**（模块 3.14）是量子计算的主要障碍：量子比特与环境的相互作用导致密度矩阵失去非对角相干性，将纯态转变为混合态。受退相干影响的量子比特会经历：比特翻转错误（$|0\rangle \to |1\rangle$，等效于 $X$）、相位翻转错误（$|+\rangle \to |-\rangle$，等效于 $Z$），或组合（$Y = iXZ$）。量子纠错（QEC）必须防护连续的错误集；关键洞见是**测量错误症状**（而非逻辑量子比特）将错误集离散化，将其归约为泡利群。

**Definition.** The **3-qubit bit-flip code** encodes one logical qubit $|\psi_L\rangle$ into three physical qubits:

$$ |0_L\rangle = |000\rangle, \qquad |1_L\rangle = |111\rangle, $$

so $|\psi_L\rangle = \alpha|000\rangle + \beta|111\rangle$. If a single bit-flip error occurs on qubit $i$, the syndrome — obtained by measuring the **stabilizers** $Z_1 Z_2$ and $Z_2 Z_3$ — identifies which qubit flipped without revealing $\alpha$ or $\beta$. The measurement outcomes (eigenvalues $\pm 1$) form the syndrome table:

- No error: $Z_1 Z_2 = +1$, $Z_2 Z_3 = +1$.
- Flip on 1: $Z_1 Z_2 = -1$, $Z_2 Z_3 = +1$.
- Flip on 2: $Z_1 Z_2 = -1$, $Z_2 Z_3 = -1$.
- Flip on 3: $Z_1 Z_2 = +1$, $Z_2 Z_3 = -1$.

The correction is to apply $X$ to the identified qubit, restoring $|\psi_L\rangle$. The syndrome measurement does not collapse the logical qubit because $Z_1 Z_2$ and $Z_2 Z_3$ commute with the logical operators $X_L = X_1 X_2 X_3$ and $Z_L = Z_1$. See Derivations for the full syndrome analysis.

**定义。** **3 量子比特比特翻转码**将一个逻辑量子比特 $|\psi_L\rangle$ 编码为三个物理量子比特：

$$ |0_L\rangle = |000\rangle, \qquad |1_L\rangle = |111\rangle, $$

因此 $|\psi_L\rangle = \alpha|000\rangle + \beta|111\rangle$。若在量子比特 $i$ 上发生单次比特翻转错误，通过测量**稳定子** $Z_1 Z_2$ 和 $Z_2 Z_3$ 获得的症状——可以在不泄露 $\alpha$ 或 $\beta$ 的情况下识别翻转的量子比特。测量结果（本征值 $\pm 1$）构成症状表：

- 无错误：$Z_1 Z_2 = +1$，$Z_2 Z_3 = +1$。
- 量子比特 1 翻转：$Z_1 Z_2 = -1$，$Z_2 Z_3 = +1$。
- 量子比特 2 翻转：$Z_1 Z_2 = -1$，$Z_2 Z_3 = -1$。
- 量子比特 3 翻转：$Z_1 Z_2 = +1$，$Z_2 Z_3 = -1$。

修正方法是对识别出的量子比特施加 $X$，恢复 $|\psi_L\rangle$。症状测量不会坍缩逻辑量子比特，因为 $Z_1 Z_2$ 和 $Z_2 Z_3$ 与逻辑算符 $X_L = X_1 X_2 X_3$ 和 $Z_L = Z_1$ 对易。完整症状分析见推导文档。

**Definition.** The **Shor 9-qubit code** (1995) corrects all single-qubit errors (bit-flip, phase-flip, and combinations). It concatenates the 3-qubit bit-flip code with the 3-qubit phase-flip code:

$$ |0_L\rangle = (|000\rangle+|111\rangle)^{\otimes 3} / 2\sqrt{2}, \qquad |1_L\rangle = (|000\rangle-|111\rangle)^{\otimes 3} / 2\sqrt{2}. $$

The inner code protects against $X$ (bit-flip) errors; the outer code protects against $Z$ (phase-flip) errors; since $\{X, Y, Z\}$ spans all single-qubit errors, arbitrary single-qubit errors are corrected. The Shor code uses 9 physical qubits to encode 1 logical qubit, with distance $d = 3$ (corrects any 1 error).

**定义。** **Shor 9 量子比特码**（1995 年）纠正所有单量子比特错误（比特翻转、相位翻转及其组合）。它将 3 量子比特比特翻转码与 3 量子比特相位翻转码串联：

$$ |0_L\rangle = (|000\rangle+|111\rangle)^{\otimes 3} / 2\sqrt{2}, \qquad |1_L\rangle = (|000\rangle-|111\rangle)^{\otimes 3} / 2\sqrt{2}. $$

内码防护 $X$（比特翻转）错误；外码防护 $Z$（相位翻转）错误；因为 $\{X, Y, Z\}$ 张成所有单量子比特错误，任意单量子比特错误均可被纠正。Shor 码使用 9 个物理量子比特编码 1 个逻辑量子比特，距离 $d = 3$（纠正任意 1 个错误）。

**Definition.** The **stabilizer formalism** (Gottesman 1997) provides a compact framework: a stabilizer code is defined by an abelian subgroup $S$ of the $n$-qubit Pauli group, and the code space is the simultaneous $+1$ eigenspace of all elements of $S$. The logical operators are Pauli operators that commute with $S$ but are not in $S$. The error syndromes are the eigenvalues of the generators of $S$, which can be measured without disturbing the encoded information. CSS codes (Calderbank–Shor–Steane) form an important sub-family constructed from classical linear codes. The **$[[n,k,d]]$ notation** describes $n$ physical qubits encoding $k$ logical qubits with distance $d$ (correcting $\lfloor (d-1)/2 \rfloor$ errors).

**定义。** **稳定子形式**（Gottesman，1997 年）提供了一个简洁的框架：稳定子码由 $n$ 量子比特泡利群的一个阿贝尔子群 $S$ 定义，码空间是 $S$ 所有元素的同时 $+1$ 本征空间。逻辑算符是与 $S$ 对易但不属于 $S$ 的泡利算符。错误症状是 $S$ 的生成元的本征值，可以在不干扰编码信息的情况下测量。CSS 码（Calderbank–Shor–Steane）由经典线性码构造，是一个重要的子族。**$[[n,k,d]]$ 记号**描述了用 $n$ 个物理量子比特编码 $k$ 个逻辑量子比特、距离为 $d$（纠正 $\lfloor (d-1)/2 \rfloor$ 个错误）的码。

**Definition.** The **fault-tolerance threshold theorem** states that, provided the physical error rate $p$ is below a threshold $p_\text{th}$ (typically $10^{-2}$ to $10^{-3}$ for realistic codes), a quantum computation of arbitrary length can be performed reliably by concatenating error correction layers. Each level of concatenation reduces the logical error rate from $p$ to $\sim (p/p_\text{th})^{2^L}$ for concatenation level $L$. The surface code (a 2D topological stabilizer code) achieves the highest known threshold $p_\text{th} \approx 1\%$ under circuit-level noise and requires $O(d^2)$ physical qubits for a distance-$d$ logical qubit, with $d \sim 20\text{–}50$ for practical fault tolerance.

**定义。** **容错阈值定理**指出，只要物理错误率 $p$ 低于阈值 $p_\text{th}$（对于实际的码，通常为 $10^{-2}$ 到 $10^{-3}$），通过串联错误纠正层，任意长度的量子计算都可以可靠地执行。串联级别 $L$ 的每一层将逻辑错误率从 $p$ 降低到约 $(p/p_\text{th})^{2^L}$。表面码（二维拓扑稳定子码）在电路级噪声下实现了已知最高的阈值 $p_\text{th} \approx 1\%$，距离为 $d$ 的逻辑量子比特需要 $O(d^2)$ 个物理量子比特，实际容错通常需要 $d \sim 20\text{–}50$。

**Application — Physical platforms.** Current quantum hardware platforms each trade off different error sources and connectivity. **Superconducting qubits** (see Module 5.8) operate at millikelvin temperatures; their fast gate times ($\sim 10\text{–}100$ ns) and compatibility with lithographic fabrication make them the leading platform for near-term processors (Google, IBM), but their decoherence times $T_1, T_2 \sim 10\text{–}500$ µs require efficient error correction. **Trapped-ion qubits** ($^{171}\text{Yb}^+$, $^{40}\text{Ca}^+$) exploit narrow optical transitions for long coherence times ($> 1$ s) and high-fidelity two-qubit gates ($> 99.9\%$), but slower gate rates ($\sim 1$ µs–1 ms) and scalability challenges. **Topological qubits** (see Module 5.11) — based on non-Abelian anyons such as Majorana zero modes in topological superconductors — store quantum information non-locally, making them intrinsically protected from local errors; hardware demonstration remains an active research frontier.

**应用——物理平台。** 当前的量子硬件平台各自在不同的错误来源和连接性之间进行权衡。**超导量子比特**（见模块 5.8）在毫开尔文温度下工作；其快速门操作时间（约 10–100 ns）和与光刻制造的兼容性使其成为近期处理器（Google、IBM）的领先平台，但其退相干时间 $T_1$、$T_2 \sim 10\text{–}500$ µs 需要高效的纠错。**囚禁离子量子比特**（$^{171}\text{Yb}^+$、$^{40}\text{Ca}^+$）利用窄光学跃迁获得长相干时间（$> 1$ 秒）和高保真双量子比特门（$> 99.9\%$），但门操作速率较慢（约 1 µs–1 ms）且面临可扩展性挑战。**拓扑量子比特**（见模块 5.11）——基于拓扑超导体中 Majorana 零模等非阿贝尔任意子——非局域地存储量子信息，使其本征地受到局域错误的保护；硬件演示仍是一个活跃的研究前沿。

## Key results · 核心结果

- Deutsch–Jozsa: one quantum query decides constant vs balanced · 多伊奇–约萨
- Grover search $\sim\tfrac{\pi}{4}\sqrt N$ iterations · 格罗弗搜索
- QFT gate complexity $O(n^2)$ · 量子傅里叶变换
- Shor: factoring = period finding (QFT) · 秀尔算法
- 3-qubit code $|0_L\rangle=|000\rangle$, $|1_L\rangle=|111\rangle$ · 三比特纠错码

---

**Self-test (blank page)**

1. State the Deutsch–Jozsa problem and explain why one quantum query suffices.
2. Describe the Grover operator $G$ geometrically on the Bloch sphere and state the number of iterations for $N$ items.
3. What is the QFT and what is its gate complexity compared to the classical FFT?
4. Explain how Shor's algorithm reduces factoring to period finding.
5. Describe the BB84 protocol: what bases are used, how is the key extracted, and how is an eavesdropper detected?
6. Define decoherence and explain why it is the main obstacle to quantum computation (link to Module 3.14).
7. Write the logical codewords of the 3-qubit bit-flip code and describe how the syndrome identifies the error without measuring the logical qubit.
8. How does the Shor 9-qubit code protect against phase-flip errors in addition to bit-flip errors?
9. State the fault-tolerance threshold theorem and give a typical value of $p_\text{th}$ for the surface code.
10. Compare superconducting and trapped-ion qubits as quantum computing platforms.

**自测（空白页）**

1. 陈述 Deutsch–Jozsa 问题，并解释为何一次量子查询就足够。
2. 在布洛赫球上几何描述 Grover 算符 $G$，并给出 $N$ 个项所需的迭代次数。
3. 什么是 QFT？与经典 FFT 相比，其门复杂度如何？
4. 解释 Shor 算法如何将因式分解归约为周期求解。
5. 描述 BB84 协议：使用什么基，如何提取密钥，如何检测窃听者？
6. 定义退相干并解释为何它是量子计算的主要障碍（联系模块 3.14）。
7. 写出 3 量子比特比特翻转码的逻辑码字，并描述症状如何在不测量逻辑量子比特的情况下识别错误。
8. Shor 9 量子比特码如何在防护比特翻转错误之外还防护相位翻转错误？
9. 陈述容错阈值定理，并给出表面码的典型 $p_\text{th}$ 值。
10. 从量子计算平台角度比较超导量子比特和囚禁离子量子比特。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Deutsch–Jozsa decides whether $f$ is constant or balanced. A superposition queries all inputs at once and interference exposes the global property in one query (vs $2^{n-1}+1$ classically). · 一次量子查询足够。
**2.** $G$ = reflection about the mean followed by reflection about the target — a rotation toward the marked state by $2\theta$ in a 2D plane; it needs $\sim\tfrac\pi4\sqrt N$ iterations. · 几何上为旋转,$\sim\tfrac\pi4\sqrt N$ 次。
**3.** The quantum Fourier transform has gate complexity $O(n^2)$ for $n$ qubits, versus the classical FFT's $O(n2^n)$ on $2^n$ amplitudes. · QFT 复杂度 $O(n^2)$。
**4.** Shor reduces factoring $N$ to finding the period $r$ of $f(x)=a^x\bmod N$; the QFT extracts $r$, then $\gcd(a^{r/2}\pm1,N)$ yields a factor. · 因数分解化为求周期。

</details>

---

← Previous: [Module 3.16 — Quantum Computation & Information](./module-3.16-quantum-computation-and-information.md) · [Phase 3 index](./README.md) · Next: [Module 3.18 — Quantum Scattering Theory](./module-3.18-quantum-scattering-theory.md) →

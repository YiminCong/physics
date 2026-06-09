---
title: "Derivations — Module 3.17: Quantum Algorithms & Error Correction"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.17: Quantum Algorithms & Error Correction
# 推导 — 模块 3.17：量子算法与量子纠错

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.17](./module-3.17-quantum-algorithms-and-error-correction.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.17](./module-3.17-quantum-algorithms-and-error-correction.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Deutsch–Jozsa Algorithm: One Query Distinguishes Constant from Balanced · Deutsch–Jozsa 算法：一次查询区分常数函数与平衡函数

**Claim.** The $n$-qubit Deutsch–Jozsa circuit outputs $|0\rangle^{\otimes n}$ if and only if $f$ is constant, and a state orthogonal to $|0\rangle^{\otimes n}$ if $f$ is balanced.

**命题。** $n$ 量子比特 Deutsch–Jozsa 电路当且仅当 $f$ 是常数函数时输出 $|0\rangle^{\otimes n}$，若 $f$ 是平衡函数则输出与 $|0\rangle^{\otimes n}$ 正交的态。

**Setup.** The circuit uses $n + 1$ qubits. The query register starts as $|0\rangle^{\otimes n}$ and the ancilla as $|1\rangle$. The oracle $U_f$ acts as $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$.

**设置。** 电路使用 $n + 1$ 个量子比特。查询寄存器初态为 $|0\rangle^{\otimes n}$，辅助量子比特初态为 $|1\rangle$。神谕 $U_f$ 的作用为 $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$。

**Step 1 — Prepare the ancilla in the $|-\rangle$ state.** Apply $H$ to the ancilla qubit:

**第 1 步 — 将辅助量子比特制备为 $|-\rangle$ 态。** 对辅助量子比特施加 $H$：

$$ H|1\rangle = (|0\rangle - |1\rangle)/\sqrt{2} = |-\rangle. $$

**Step 2 — Create uniform superposition of inputs.** Apply $H^{\otimes n}$ to the query register:

**第 2 步 — 创建输入的均匀叠加。** 对查询寄存器施加 $H^{\otimes n}$：

$$ H^{\otimes n}|0\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle. $$

Full state: $\dfrac{1}{\sqrt{2^n}} \sum_x |x\rangle \otimes |-\rangle$.

**Step 3 — Apply oracle $U_f$. Phase kickback.** For the ancilla in state $|-\rangle$, note that:

**第 3 步 — 施加神谕 $U_f$。相位反冲。** 当辅助量子比特处于态 $|-\rangle$ 时，注意：

$$ U_f|x\rangle|-\rangle = |x\rangle (|f(x)\oplus 0\rangle - |f(x)\oplus 1\rangle)/\sqrt{2} = (-1)^{f(x)} |x\rangle|-\rangle. $$

The phase $(-1)^{f(x)}$ **kicks back** onto the query register. After $U_f$:

相位 $(-1)^{f(x)}$ **反冲**到查询寄存器上。$U_f$ 作用后：

$$ |\Psi_1\rangle = \frac{1}{\sqrt{2^n}} \sum_x (-1)^{f(x)} |x\rangle \otimes |-\rangle. $$

The ancilla is unchanged and can be ignored.

辅助量子比特不变，可以忽略。

**Step 4 — Apply $H^{\otimes n}$ to query register.** Use $H^{\otimes n}|x\rangle = \dfrac{1}{\sqrt{2^n}} \sum_z (-1)^{x\cdot z} |z\rangle$ where $x\cdot z = \sum_i x_i z_i$ (mod 2) is the binary inner product. Then:

**第 4 步 — 对查询寄存器施加 $H^{\otimes n}$。** 利用 $H^{\otimes n}|x\rangle = \dfrac{1}{\sqrt{2^n}} \sum_z (-1)^{x\cdot z} |z\rangle$，其中 $x\cdot z = \sum_i x_i z_i$（mod 2）是二进制内积。则：

$$ |\Psi_2\rangle = H^{\otimes n} \frac{1}{\sqrt{2^n}} \sum_x (-1)^{f(x)} |x\rangle = \frac{1}{2^n} \sum_z \Big[\, \sum_x (-1)^{f(x)+x\cdot z} \,\Big] |z\rangle. $$

**Step 5 — Measure and analyse.** The amplitude of $|0\rangle^{\otimes n}$ (i.e. $z = 0$) is:

**第 5 步 — 测量与分析。** $|0\rangle^{\otimes n}$（即 $z = 0$）的振幅为：

$$ A(z=0) = \frac{1}{2^n} \sum_x (-1)^{f(x)}. $$

**Case 1: $f$ constant.** If $f(x) = c$ for all $x$, then $A(z=0) = (1/2^n) \cdot 2^n \cdot (-1)^c = (-1)^c$, which has magnitude $1$. The output is $|0\rangle^{\otimes n}$ with certainty (global phase $(-1)^c$ is unobservable).

**情况 1：$f$ 为常数函数。** 若对所有 $x$ 有 $f(x) = c$，则 $A(z=0) = (1/2^n) \cdot 2^n \cdot (-1)^c = (-1)^c$，模为 $1$。输出以确定性为 $|0\rangle^{\otimes n}$（全局相位 $(-1)^c$ 不可观测）。

**Case 2: $f$ balanced.** Exactly $2^n/2 = 2^{n-1}$ inputs give $f(x) = 0$ and $2^{n-1}$ give $f(x) = 1$. Then:

**情况 2：$f$ 为平衡函数。** 恰好 $2^n/2 = 2^{n-1}$ 个输入给出 $f(x) = 0$，$2^{n-1}$ 个给出 $f(x) = 1$。则：

$$ A(z=0) = \frac{1}{2^n}[\, 2^{n-1} \cdot (+1) + 2^{n-1} \cdot (-1) \,] = 0. $$

The output is orthogonal to $|0\rangle^{\otimes n}$: a measurement never gives all-zeros.

输出与 $|0\rangle^{\otimes n}$ 正交：测量永远不会给出全零。

**Conclusion.** Measuring all $n$ qubits: outcome $00\ldots0 \leftrightarrow f$ constant; any other outcome $\leftrightarrow f$ balanced. **One oracle call determines the answer.** $\blacksquare$

**结论。** 测量所有 $n$ 个量子比特：结果 $00\ldots0 \leftrightarrow f$ 为常数；任何其他结果 $\leftrightarrow f$ 为平衡。**一次神谕调用确定答案。** $\blacksquare$

---

## B. Grover's Algorithm: One Iteration as a Geometric Reflection Giving the $\sqrt{N}$ Speed-up · Grover 算法：一次迭代作为几何反射给出 $\sqrt{N}$ 加速

**Claim.** Each Grover iteration rotates the state by angle $2\theta$ ($\sin\theta = 1/\sqrt{N}$) toward the target $|w\rangle$, so after $O(\pi/(4\theta)) = O(\sqrt{N})$ iterations, the target is found with high probability.

**命题。** 每次 Grover 迭代将态向目标 $|w\rangle$ 旋转角度 $2\theta$（$\sin\theta = 1/\sqrt{N}$），因此经过 $O(\pi/(4\theta)) = O(\sqrt{N})$ 次迭代后，以高概率找到目标。

**Setup.** Let $N = 2^n$. Define the uniform superposition $|s\rangle = (1/\sqrt{N}) \sum_x |x\rangle$ and the marked state $|w\rangle$. The complement superposition is $|s'\rangle = (|s\rangle - (1/\sqrt{N})|w\rangle)/\sqrt{1-1/N}$ (the uniform state over unmarked items, normalised). The two-dimensional subspace spanned by $|w\rangle$ and $|s'\rangle$ captures all the action.

**设置。** 令 $N = 2^n$。定义均匀叠加态 $|s\rangle = (1/\sqrt{N}) \sum_x |x\rangle$ 和目标态 $|w\rangle$。补充叠加态为 $|s'\rangle = (|s\rangle - (1/\sqrt{N})|w\rangle)/\sqrt{1-1/N}$（非目标项的均匀态，已归一化）。由 $|w\rangle$ 和 $|s'\rangle$ 张成的二维子空间捕获了所有动态。

**Step 1 — Initial state in the 2D subspace.** Write $|s\rangle$ in terms of $|w\rangle$ and $|s'\rangle$:

**第 1 步 — 二维子空间中的初态。** 用 $|w\rangle$ 和 $|s'\rangle$ 写出 $|s\rangle$：

$$ |s\rangle = \sin\theta\, |w\rangle + \cos\theta\, |s'\rangle, $$

where $\sin\theta = \langle w|s\rangle = 1/\sqrt{N}$ (so $\theta \approx 1/\sqrt{N}$ for large $N$).

其中 $\sin\theta = \langle w|s\rangle = 1/\sqrt{N}$（对大 $N$，$\theta \approx 1/\sqrt{N}$）。

**Step 2 — The oracle $O_w$ as a reflection.** The oracle $O_w|x\rangle = (-1)^{\delta_{x,w}}|x\rangle$ flips the sign of $|w\rangle$:

**第 2 步 — 神谕 $O_w$ 作为反射。** 神谕 $O_w|x\rangle = (-1)^{\delta_{x,w}}|x\rangle$ 翻转 $|w\rangle$ 的符号：

$$ O_w = I - 2|w\rangle\langle w|. $$

Geometrically, this **reflects** the state vector about the hyperplane perpendicular to $|w\rangle$ (i.e., the $|s'\rangle$ axis). In the 2D subspace, it maps:

在几何上，这将态矢量关于垂直于 $|w\rangle$ 的超平面（即 $|s'\rangle$ 轴）进行**反射**。在二维子空间中，它将：

$$ \sin\theta\, |w\rangle + \cos\theta\, |s'\rangle \to -\sin\theta\, |w\rangle + \cos\theta\, |s'\rangle. $$

The angle with $|w\rangle$ goes from $\theta$ to $(\pi/2 - \theta)$ measured from $|w\rangle$.

与 $|w\rangle$ 的角度从 $\theta$ 变为从 $|w\rangle$ 量起的 $(\pi/2 - \theta)$。

**Step 3 — The diffusion operator $D_s$ as a reflection.** The diffusion operator $D_s = 2|s\rangle\langle s| - I$ reflects about $|s\rangle$:

**第 3 步 — 扩散算符 $D_s$ 作为反射。** 扩散算符 $D_s = 2|s\rangle\langle s| - I$ 关于 $|s\rangle$ 进行反射：

In the 2D subspace, starting after $O_w$ (state at angle $\pi/2 - \theta$ from $|w\rangle$, measured in the $|w\rangle, |s'\rangle$ plane), $D_s$ reflects about the line to $|s\rangle$ (angle $\theta$ from $|s'\rangle$ axis, or equivalently $\pi/2 - \theta$ from $|w\rangle$ axis). After the two reflections ($O_w$ then $D_s$), the net rotation is:

在二维子空间中，在 $O_w$ 作用后（态在 $|w\rangle, |s'\rangle$ 平面中距 $|w\rangle$ 为 $\pi/2 - \theta$），$D_s$ 关于 $|s\rangle$ 方向（距 $|s'\rangle$ 轴 $\theta$，或等价地距 $|w\rangle$ 轴 $\pi/2 - \theta$）反射。两次反射（先 $O_w$ 后 $D_s$）的净旋转为：

$$ \text{net rotation angle} = 2 \times \theta = 2\theta \quad (\text{toward } |w\rangle). $$

This is a theorem of plane geometry: the composition of two reflections is a rotation by twice the angle between the mirror lines.

这是平面几何定理：两次反射的合成是以两镜面线夹角两倍旋转。

**Step 4 — Counting iterations.** Starting from angle $\theta$ with $|w\rangle$, after $k$ iterations the angle with $|w\rangle$ is $(2k+1)\theta$. To maximise the probability of measuring $|w\rangle$, we need $(2k+1)\theta \approx \pi/2$, giving:

**第 4 步 — 计算迭代次数。** 从与 $|w\rangle$ 成角 $\theta$ 出发，$k$ 次迭代后与 $|w\rangle$ 的角度为 $(2k+1)\theta$。为最大化测量 $|w\rangle$ 的概率，需要 $(2k+1)\theta \approx \pi/2$，得：

$$ k \approx \frac{\pi}{4\theta} - \frac12 \approx \frac{\pi}{4}\sqrt{N}. $$

The success probability is $\sin^2((2k+1)\theta) \ge 1 - 1/N$. $\blacksquare$

成功概率为 $\sin^2((2k+1)\theta) \ge 1 - 1/N$。$\blacksquare$

**Step 5 — Lower bound (why classical needs $O(N)$).** Classically, each query tests one item; after $k$ queries, the probability of finding the marked item is at most $k/N$. To achieve success probability $\ge 1/2$ classically requires $k \ge N/2 = O(N)$. The quantum algorithm achieves this in $O(\sqrt{N})$, a quadratic improvement.

**第 5 步 — 下界（为何经典需要 $O(N)$）。** 经典情况下，每次查询测试一个项；$k$ 次查询后，找到目标项的概率至多为 $k/N$。经典上达到成功概率 $\ge 1/2$ 需要 $k \ge N/2 = O(N)$。量子算法在 $O(\sqrt{N})$ 内实现，是平方级改进。

---

## C. The 3-Qubit Bit-Flip Code: Encoding, Syndrome Measurement, and Correction · 3 量子比特比特翻转码：编码、症状测量与修正

**Claim.** The 3-qubit encoding $\alpha|000\rangle + \beta|111\rangle$ corrects any single bit-flip error. The syndrome measurement identifies the error qubit without disturbing the logical state $\alpha|0_L\rangle + \beta|1_L\rangle$.

**命题。** 3 量子比特编码 $\alpha|000\rangle + \beta|111\rangle$ 纠正任意单量子比特翻转错误。症状测量在不扰动逻辑态 $\alpha|0_L\rangle + \beta|1_L\rangle$ 的情况下识别错误量子比特。

**Step 1 — Encoding circuit.** The encoder maps:

**第 1 步 — 编码电路。** 编码器将：

$$ \alpha|0\rangle + \beta|1\rangle \to \alpha|000\rangle + \beta|111\rangle. $$

This is achieved by $\text{CNOT}_{12}$ (qubit 1 control, qubit 2 target) followed by $\text{CNOT}_{13}$, starting with qubits 2 and 3 in state $|0\rangle$:

通过 $\text{CNOT}_{12}$（量子比特 1 为控制，2 为目标）然后 $\text{CNOT}_{13}$ 实现，量子比特 2 和 3 初态为 $|0\rangle$：

$$ (\alpha|0\rangle + \beta|1\rangle)|00\rangle \xrightarrow{\text{CNOT}_{12}} \alpha|000\rangle + \beta|110\rangle \xrightarrow{\text{CNOT}_{13}} \alpha|000\rangle + \beta|111\rangle. \quad \checkmark $$

**Step 2 — Error model.** A single bit-flip error on qubit $j$ applies $X_j$, mapping the codeword to one of:

**第 2 步 — 错误模型。** 量子比特 $j$ 上的单次比特翻转错误施加 $X_j$，将码字映射到以下之一：

$$ \begin{aligned} \text{No error:}&\quad \alpha|000\rangle + \beta|111\rangle. \\ \text{Error on 1:}&\quad \alpha|100\rangle + \beta|011\rangle. \\ \text{Error on 2:}&\quad \alpha|010\rangle + \beta|101\rangle. \\ \text{Error on 3:}&\quad \alpha|001\rangle + \beta|110\rangle. \end{aligned} $$

**Step 3 — Syndrome measurement.** Measure the two stabilizer observables $Z_1 Z_2$ and $Z_2 Z_3$. These are simultaneously diagonalised in the computational basis. Calculate their eigenvalues for each error case:

**第 3 步 — 症状测量。** 测量两个稳定子可观测量 $Z_1 Z_2$ 和 $Z_2 Z_3$。这两个量在计算基中同时对角化。计算每种错误情况下它们的本征值：

$$ \begin{aligned} \text{State } \alpha|000\rangle + \beta|111\rangle:&\quad Z_1 Z_2 \text{ eigenvalue} = (+1)(+1) = +1;\ Z_2 Z_3 = +1.\ \text{Syndrome } (++). \\ \text{State } \alpha|100\rangle + \beta|011\rangle:&\quad Z_1 Z_2:\ \text{qubit 1 is flipped} \to (-1)(+1) = -1;\ Z_2 Z_3 = +1.\ \text{Syndrome } (-+). \\ \text{State } \alpha|010\rangle + \beta|101\rangle:&\quad Z_1 Z_2:\ \text{qubit 2 is flipped} \to (-1)(-1) = +1?\ \text{No.} \end{aligned} $$

Let us compute explicitly. For $Z_1 Z_2$ acting on basis states:

让我们明确计算。$Z_1 Z_2$ 作用于基态：

$$ Z_1 Z_2|000\rangle = (+1)(+1)|000\rangle = +|000\rangle; \qquad Z_1 Z_2|111\rangle = (-1)(-1)|111\rangle = +|111\rangle. $$

So $\alpha|000\rangle+\beta|111\rangle$ is a $+1$ eigenstate of $Z_1 Z_2$. After error on qubit 2:

所以 $\alpha|000\rangle+\beta|111\rangle$ 是 $Z_1 Z_2$ 的 $+1$ 本征态。量子比特 2 出错后：

$$ Z_1 Z_2|010\rangle = (+1)(-1)|010\rangle = -|010\rangle; \qquad Z_1 Z_2|101\rangle = (-1)(+1)|101\rangle = -|101\rangle. $$

So $\alpha|010\rangle+\beta|101\rangle$ is a $-1$ eigenstate of $Z_1 Z_2$. Full syndrome table:

所以 $\alpha|010\rangle+\beta|101\rangle$ 是 $Z_1 Z_2$ 的 $-1$ 本征态。完整症状表：

$$ \begin{aligned} \text{No error:}&\quad Z_1 Z_2 = +1,\ Z_2 Z_3 = +1. \\ \text{Error on 1:}&\quad Z_1 Z_2 = -1,\ Z_2 Z_3 = +1. \\ \text{Error on 2:}&\quad Z_1 Z_2 = -1,\ Z_2 Z_3 = -1. \\ \text{Error on 3:}&\quad Z_1 Z_2 = +1,\ Z_2 Z_3 = -1. \end{aligned} $$

The four syndromes are distinct; the error qubit is uniquely identified.

四个症状不同；错误量子比特被唯一识别。

**Step 4 — Why the syndrome measurement does not collapse the logical qubit.** The key point is that $Z_1 Z_2$ and $Z_2 Z_3$ commute with the logical operators $Z_L = Z_1$ and $X_L = X_1 X_2 X_3$. More concretely: the syndrome operators act the same way on both terms of each codeword:

**第 4 步 — 为何症状测量不坍缩逻辑量子比特。** 关键在于 $Z_1 Z_2$ 和 $Z_2 Z_3$ 与逻辑算符 $Z_L = Z_1$ 和 $X_L = X_1 X_2 X_3$ 对易。更具体地：症状算符对每个码字的两项作用相同：

For error on qubit 1: both $\alpha|100\rangle$ and $\beta|011\rangle$ give $Z_1 Z_2 = -1$, $Z_2 Z_3 = +1$.

The syndrome measurement collapses the error sector (which error occurred) but not the logical sector (the ratio $\alpha/\beta$). After measuring syndrome $(-+)$, the post-measurement state is $\alpha|100\rangle + \beta|011\rangle$ — the coefficients $\alpha$ and $\beta$ are preserved. Applying $X_1$ recovers $\alpha|000\rangle + \beta|111\rangle$. $\blacksquare$

症状测量坍缩了错误扇区（发生了哪种错误），但不坍缩逻辑扇区（比例 $\alpha/\beta$）。测量症状（$-+$）后，测量后态为 $\alpha|100\rangle + \beta|011\rangle$——系数 $\alpha$ 和 $\beta$ 得以保留。施加 $X_1$ 恢复 $\alpha|000\rangle + \beta|111\rangle$。$\blacksquare$

**Step 5 — Generalization.** The 3-qubit code only corrects $X$ errors. For a code that corrects all single-qubit errors, one must also handle $Z$ (phase-flip) errors — this requires the full Shor $[[9,1,3]]$ code or a CSS code that corrects both types simultaneously. The stabilizer formalism generalizes this syndrome logic: stabilizer generators commute with all logical operators, so measuring them reveals the error without touching the encoded information.

**第 5 步 — 推广。** 3 量子比特码只纠正 $X$ 错误。若要纠正所有单量子比特错误，还必须处理 $Z$（相位翻转）错误——这需要完整的 Shor $[[9,1,3]]$ 码或同时纠正两种类型的 CSS 码。稳定子形式推广了这种症状逻辑：稳定子生成元与所有逻辑算符对易，因此测量它们可以在不触碰编码信息的情况下揭示错误。

---

*Derivation document for Module 3.17. All proofs are complete, bilingual, and include the physical interpretation of each result.*

*模块 3.17 的推导文档。所有证明完整、双语，并包含每个结果的物理诠释。*

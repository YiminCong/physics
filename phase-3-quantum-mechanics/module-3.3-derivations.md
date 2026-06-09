---
title: "Derivations — Module 3.3: Formalism"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.3: Formalism
# 推导 — 模块 3.3：形式化框架

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.3](./module-3.3-formalism.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.3](./module-3.3-formalism.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Canonical Commutator: $[\hat{x}, \hat{p}] = i\hbar$ · 正则对易子：$[\hat{x}, \hat{p}] = i\hbar$

**Claim.** The operators $\hat{x}$ (multiply by $x$) and $\hat{p} = -i\hbar\,\partial/\partial x$ satisfy $[\hat{x}, \hat{p}] = i\hbar$.

**命题。** 算符 $\hat{x}$（乘以 $x$）与 $\hat{p} = -i\hbar\,\partial/\partial x$ 满足 $[\hat{x}, \hat{p}] = i\hbar$。

**Step 1 — Definition of the commutator.** $[\hat{x}, \hat{p}]$ is the operator defined by its action on an arbitrary test function $f(x)$:

**第 1 步 — 对易子的定义。** $[\hat{x}, \hat{p}]$ 是通过其对任意测试函数 $f(x)$ 的作用来定义的算符：

$$ [\hat{x}, \hat{p}]\,f(x) = \hat{x}(\hat{p}\,f) - \hat{p}(\hat{x}\,f). $$

**Step 2 — Compute each term.**

**第 2 步 — 计算每一项。**

$$ \hat{p}\,f = -i\hbar\,\partial f/\partial x = -i\hbar\,f', \qquad \hat{x}(\hat{p}\,f) = x\cdot(-i\hbar\,f') = -i\hbar\,x f'. $$

$$ \hat{x}\,f = x f, \qquad \hat{p}(\hat{x}\,f) = -i\hbar\,\partial(xf)/\partial x = -i\hbar\,(f + x f') = -i\hbar\,f - i\hbar\,x f'. $$

**Step 3 — Subtract.**

**第 3 步 — 相减。**

$$ \begin{aligned} [\hat{x}, \hat{p}]\,f &= (-i\hbar\,x f') - (-i\hbar\,f - i\hbar\,x f') \\ &= -i\hbar\,x f' + i\hbar\,f + i\hbar\,x f' \\ &= i\hbar\,f. \end{aligned} $$

Since this holds for all $f$, $[\hat{x}, \hat{p}] = i\hbar$ as an operator identity. $\blacksquare$

由于对所有 $f$ 成立，作为算符恒等式 $[\hat{x}, \hat{p}] = i\hbar$。$\blacksquare$

---

## B. Hermitian Operators: Real Eigenvalues and Orthogonal Eigenstates · 厄米算符：实本征值与正交本征态

**Claim.** If $\hat{A}$ is Hermitian ($\langle\varphi|\hat{A}\psi\rangle = \langle\hat{A}\varphi|\psi\rangle$ for all $\varphi, \psi$ in the domain), then (i) all eigenvalues of $\hat{A}$ are real, and (ii) eigenstates corresponding to distinct eigenvalues are orthogonal.

**命题。** 若 $\hat{A}$ 是厄米的（对定义域内所有 $\varphi$、$\psi$ 有 $\langle\varphi|\hat{A}\psi\rangle = \langle\hat{A}\varphi|\psi\rangle$），则 (i) $\hat{A}$ 的所有本征值为实数，(ii) 对应不同本征值的本征态互相正交。

**Step 1 — Reality of eigenvalues.** Let $\hat{A}|a\rangle = a|a\rangle$ with $|a\rangle \ne 0$. Compute $\langle a|\hat{A}|a\rangle$ two ways. First:

**第 1 步 — 本征值的实性。** 设 $\hat{A}|a\rangle = a|a\rangle$，$|a\rangle \ne 0$。用两种方法计算 $\langle a|\hat{A}|a\rangle$。首先：

$$ \langle a|\hat{A}|a\rangle = \langle a|(a|a\rangle) = a\langle a|a\rangle. $$

Second, using Hermiticity $\langle a|\hat{A} = \langle\hat{A}^\dagger a| = \langle\hat{A}a| = a^*\langle a|$:

其次，利用厄米性 $\langle a|\hat{A} = \langle\hat{A}^\dagger a| = \langle\hat{A}a| = a^*\langle a|$：

$$ \langle a|\hat{A}|a\rangle = (\langle a|\hat{A}^\dagger)|a\rangle = a^*\langle a|a\rangle. $$

Equating: $a\langle a|a\rangle = a^*\langle a|a\rangle$. Since $|a\rangle \ne 0$, we have $\langle a|a\rangle > 0$, so:

令二者相等：$a\langle a|a\rangle = a^*\langle a|a\rangle$。因 $|a\rangle \ne 0$，$\langle a|a\rangle > 0$，故：

$$ a = a^*, \quad \text{i.e., } a \text{ is real.} \qquad \blacksquare $$

**Step 2 — Orthogonality of eigenstates.** Let $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A}|b\rangle = b|b\rangle$ with $a \ne b$ (both real by Step 1). Consider the inner product $\langle a|\hat{A}|b\rangle$:

**第 2 步 — 本征态的正交性。** 设 $\hat{A}|a\rangle = a|a\rangle$ 且 $\hat{A}|b\rangle = b|b\rangle$，$a \ne b$（由第 1 步均为实数）。考虑内积 $\langle a|\hat{A}|b\rangle$：

From the right: $\langle a|\hat{A}|b\rangle = \langle a|(b|b\rangle) = b\langle a|b\rangle$.

从右边：$\langle a|\hat{A}|b\rangle = \langle a|(b|b\rangle) = b\langle a|b\rangle$。

From the left (using Hermiticity): $\langle a|\hat{A}|b\rangle = \langle\hat{A}a|b\rangle = a^*\langle a|b\rangle = a\langle a|b\rangle$.

从左边（利用厄米性）：$\langle a|\hat{A}|b\rangle = \langle\hat{A}a|b\rangle = a^*\langle a|b\rangle = a\langle a|b\rangle$（因 $a$ 为实数）。

Equating: $b\langle a|b\rangle = a\langle a|b\rangle$, so $(a - b)\langle a|b\rangle = 0$. Since $a \ne b$:

令二者相等：$b\langle a|b\rangle = a\langle a|b\rangle$，故 $(a - b)\langle a|b\rangle = 0$。因 $a \ne b$：

$$ \langle a|b\rangle = 0 \quad \text{— the eigenstates are orthogonal.} \qquad \blacksquare $$

$$ \langle a|b\rangle = 0 \quad \text{——本征态互相正交。} \qquad \blacksquare $$

---

## C. Spectral Expansion: $|\psi\rangle = \sum c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$ · 谱展开：$|\psi\rangle = \sum c_n|n\rangle$ 与 $c_n = \langle n|\psi\rangle$

**Claim.** If $\{|n\rangle\}$ is a complete orthonormal basis of the Hilbert space ($\sum_n|n\rangle\langle n| = \hat{1}$, $\langle m|n\rangle = \delta_{mn}$), then any state $|\psi\rangle$ can be expanded as $|\psi\rangle = \sum_n c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$, and $\sum_n|c_n|^2 = 1$ (normalization).

**命题。** 若 $\{|n\rangle\}$ 是希尔伯特空间的完备正交归一基（$\sum_n|n\rangle\langle n| = \hat{1}$，$\langle m|n\rangle = \delta_{mn}$），则任意态 $|\psi\rangle$ 可展开为 $|\psi\rangle = \sum_n c_n|n\rangle$，其中 $c_n = \langle n|\psi\rangle$，且 $\sum_n|c_n|^2 = 1$（归一化）。

**Step 1 — Insert the resolution of the identity.** The completeness relation $\sum_n|n\rangle\langle n| = \hat{1}$ means that for any $|\psi\rangle$:

**第 1 步 — 插入单位分解。** 完备性关系 $\sum_n|n\rangle\langle n| = \hat{1}$ 意味着对任意 $|\psi\rangle$：

$$ |\psi\rangle = \hat{1}|\psi\rangle = \Big(\sum_n|n\rangle\langle n|\Big)|\psi\rangle = \sum_n|n\rangle\langle n|\psi\rangle = \sum_n c_n|n\rangle, $$

where $c_n = \langle n|\psi\rangle$.

其中 $c_n = \langle n|\psi\rangle$。

**Step 2 — Normalization.** Take $\langle\psi|\psi\rangle = 1$:

**第 2 步 — 归一化。** 取 $\langle\psi|\psi\rangle = 1$：

$$ 1 = \langle\psi|\psi\rangle = \langle\psi|\Big(\sum_n c_n|n\rangle\Big) = \sum_n c_n\langle\psi|n\rangle = \sum_n c_n c_n^* = \boxed{\,\sum_n|c_n|^2\,}. \qquad \blacksquare $$

**Step 3 — Probability interpretation.** When the observable $\hat{A}$ with eigenvalues $a_n$ and eigenstates $|n\rangle$ is measured, the probability of obtaining $a_n$ is:

**第 3 步 — 概率诠释。** 当测量本征值为 $a_n$、本征态为 $|n\rangle$ 的可观测量 $\hat{A}$ 时，得到 $a_n$ 的概率为：

$$ P(a_n) = |\langle n|\psi\rangle|^2 = |c_n|^2. $$

Completeness ensures $\sum_n P(a_n) = 1$ — some outcome always occurs. $\blacksquare$

完备性确保 $\sum_n P(a_n) = 1$——某个结果必然发生。$\blacksquare$

---

## D. Generalized Uncertainty Principle: $\Delta A\,\Delta B \ge \tfrac12|\langle[\hat{A},\hat{B}]\rangle|$ · 广义不确定性关系

**Claim.** For any two Hermitian observables $\hat{A}$ and $\hat{B}$ in state $|\psi\rangle$:

**命题。** 对任意态 $|\psi\rangle$ 中的两个厄米可观测量 $\hat{A}$ 和 $\hat{B}$：

$$ \boxed{\,\Delta A\,\Delta B \ge \tfrac12|\langle[\hat{A}, \hat{B}]\rangle|\,}. $$

**Step 1 — Define shifted operators.** Let $\alpha = \langle\hat{A}\rangle$ and $\beta = \langle\hat{B}\rangle$. Define:

**第 1 步 — 定义移位算符。** 令 $\alpha = \langle\hat{A}\rangle$，$\beta = \langle\hat{B}\rangle$。定义：

$$ \tilde{A} = \hat{A} - \alpha, \qquad \tilde{B} = \hat{B} - \beta. $$

Both $\tilde{A}$ and $\tilde{B}$ are Hermitian (subtracting a real number from a Hermitian operator preserves Hermiticity). Also:

$\tilde{A}$ 和 $\tilde{B}$ 均为厄米的（从厄米算符减去实数保持厄米性）。还有：

$$ \Delta A^2 = \langle\tilde{A}^2\rangle = \langle\psi|\tilde{A}^2|\psi\rangle = \|\tilde{A}|\psi\rangle\|^2, \qquad \Delta B^2 = \langle\tilde{B}^2\rangle = \|\tilde{B}|\psi\rangle\|^2. $$

Note also $[\tilde{A}, \tilde{B}] = [\hat{A}, \hat{B}]$ (constants commute with everything).

注意 $[\tilde{A}, \tilde{B}] = [\hat{A}, \hat{B}]$（常数与所有算符对易）。

**Step 2 — Apply the Cauchy–Schwarz inequality.** For any two vectors $|f\rangle$ and $|g\rangle$ in a Hilbert space, the Cauchy–Schwarz inequality states:

**第 2 步 — 应用柯西–施瓦茨不等式。** 对希尔伯特空间中任意两个向量 $|f\rangle$ 和 $|g\rangle$，柯西–施瓦茨不等式表明：

$$ \langle f|f\rangle\cdot\langle g|g\rangle \ge |\langle f|g\rangle|^2. $$

Set $|f\rangle = \tilde{A}|\psi\rangle$ and $|g\rangle = \tilde{B}|\psi\rangle$. Then:

取 $|f\rangle = \tilde{A}|\psi\rangle$，$|g\rangle = \tilde{B}|\psi\rangle$。则：

$$ \|\tilde{A}|\psi\rangle\|^2\cdot\|\tilde{B}|\psi\rangle\|^2 \ge |\langle\tilde{A}\psi|\tilde{B}\psi\rangle|^2, $$

$$ \Delta A^2\cdot\Delta B^2 \ge |\langle\psi|\tilde{A}\tilde{B}|\psi\rangle|^2. \qquad (*) $$

**Step 3 — Decompose $\tilde{A}\tilde{B}$ into Hermitian and anti-Hermitian parts.** Write:

**第 3 步 — 将 $\tilde{A}\tilde{B}$ 分解为厄米与反厄米部分。** 写成：

$$ \tilde{A}\tilde{B} = \tfrac12(\tilde{A}\tilde{B} + \tilde{B}\tilde{A}) + \tfrac12(\tilde{A}\tilde{B} - \tilde{B}\tilde{A}). $$

The first part is the **anticommutator** $\{\tilde{A}, \tilde{B}\}/2$ — a Hermitian operator (its expectation is real). The second part involves the **commutator** $[\tilde{A}, \tilde{B}]/2 = [\hat{A}, \hat{B}]/2$. Since $\tilde{A}$ and $\tilde{B}$ are Hermitian, $[\tilde{A}, \tilde{B}]$ is anti-Hermitian (satisfies $([\tilde{A},\tilde{B}])^\dagger = [\tilde{B}^\dagger,\tilde{A}^\dagger] = [\tilde{B},\tilde{A}] = -[\tilde{A},\tilde{B}]$), so its expectation value is purely imaginary (or zero).

第一部分是**反对易子** $\{\tilde{A}, \tilde{B}\}/2$——厄米算符（其期望值为实数）。第二部分涉及**对易子** $[\tilde{A}, \tilde{B}]/2 = [\hat{A}, \hat{B}]/2$。由于 $\tilde{A}$ 和 $\tilde{B}$ 是厄米的，$[\tilde{A}, \tilde{B}]$ 是反厄米的（满足 $([\tilde{A},\tilde{B}])^\dagger = [\tilde{B}^\dagger,\tilde{A}^\dagger] = [\tilde{B},\tilde{A}] = -[\tilde{A},\tilde{B}]$），故其期望值为纯虚数（或零）。

Therefore $\langle\tilde{A}\tilde{B}\rangle = (\text{real part}) + i(\text{imaginary part})$, and:

因此 $\langle\tilde{A}\tilde{B}\rangle = (\text{实部}) + i(\text{虚部})$，且：

$$ |\langle\tilde{A}\tilde{B}\rangle|^2 = |\mathrm{Re}\langle\tilde{A}\tilde{B}\rangle|^2 + |\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle|^2 \ge |\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle|^2. $$

Now $\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle = \mathrm{Im}[\tfrac12\langle\{\tilde{A},\tilde{B}\}\rangle + \tfrac12\langle[\hat{A},\hat{B}]\rangle]$. The anticommutator term is real, so it contributes nothing to the imaginary part:

现在 $\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle = \mathrm{Im}[\tfrac12\langle\{\tilde{A},\tilde{B}\}\rangle + \tfrac12\langle[\hat{A},\hat{B}]\rangle]$。反对易子项为实数，对虚部无贡献：

$$ \mathrm{Im}\langle\tilde{A}\tilde{B}\rangle = \tfrac12\,\mathrm{Im}\langle[\hat{A},\hat{B}]\rangle. $$

But $[\hat{A},\hat{B}]$ is anti-Hermitian, so $\langle[\hat{A},\hat{B}]\rangle$ is purely imaginary: $\langle[\hat{A},\hat{B}]\rangle = i\cdot K$ for some real $K$. Therefore $\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle = K/2$, and:

但 $[\hat{A},\hat{B}]$ 是反厄米的，故 $\langle[\hat{A},\hat{B}]\rangle$ 为纯虚数：$\langle[\hat{A},\hat{B}]\rangle = i\cdot K$，$K$ 为实数。因此 $\mathrm{Im}\langle\tilde{A}\tilde{B}\rangle = K/2$，且：

$$ |\langle\tilde{A}\tilde{B}\rangle|^2 \ge (K/2)^2 = \tfrac14|\langle[\hat{A},\hat{B}]\rangle|^2. $$

**Step 4 — Assemble the inequality.** Substituting back into $(*)$:

**第 4 步 — 组合不等式。** 代回 $(*)$：

$$ \Delta A^2\cdot\Delta B^2 \ge \tfrac14|\langle[\hat{A},\hat{B}]\rangle|^2. $$

Taking the positive square root ($\Delta A, \Delta B \ge 0$):

取正平方根（$\Delta A$、$\Delta B \ge 0$）：

$$ \boxed{\,\Delta A\cdot\Delta B \ge \tfrac12|\langle[\hat{A},\hat{B}]\rangle|\,}. \qquad \blacksquare $$

---

## E. Position–Momentum Uncertainty: $\Delta x\cdot\Delta p \ge \hbar/2$ · 位置–动量不确定性

**Claim.** For $\hat{x}$ and $\hat{p}$, the generalized uncertainty relation gives $\Delta x\cdot\Delta p \ge \hbar/2$.

**命题。** 对 $\hat{x}$ 和 $\hat{p}$，广义不确定性关系给出 $\Delta x\cdot\Delta p \ge \hbar/2$。

**Step 1.** From Section A, $[\hat{x}, \hat{p}] = i\hbar$.

**第 1 步。** 由第 A 节，$[\hat{x}, \hat{p}] = i\hbar$。

**Step 2.** $\langle[\hat{x}, \hat{p}]\rangle = \langle i\hbar\rangle = i\hbar$ (since $i\hbar$ is a scalar, its expectation value in any state is $i\hbar$).

**第 2 步。** $\langle[\hat{x}, \hat{p}]\rangle = \langle i\hbar\rangle = i\hbar$（因为 $i\hbar$ 是标量，在任何态中其期望值均为 $i\hbar$）。

**Step 3.** Apply the generalized uncertainty relation:

**第 3 步。** 应用广义不确定性关系：

$$ \Delta x\cdot\Delta p \ge \tfrac12|\langle[\hat{x}, \hat{p}]\rangle| = \tfrac12|i\hbar| = \boxed{\,\hbar/2\,}. \qquad \blacksquare $$

The equality $\Delta x\cdot\Delta p = \hbar/2$ is saturated when the Cauchy–Schwarz inequality is an equality ($|f\rangle \propto |g\rangle$) and the real part of $\langle f|g\rangle$ vanishes. These conditions together force $\psi$ to be a Gaussian, confirming the result of Module 3.1 Derivation D.

当柯西–施瓦茨不等式取等（$|f\rangle \propto |g\rangle$）且 $\langle f|g\rangle$ 的实部为零时，等号 $\Delta x\cdot\Delta p = \hbar/2$ 成立。这两个条件共同迫使 $\psi$ 为高斯函数，与模块 3.1 推导 D 的结果一致。$\blacksquare$

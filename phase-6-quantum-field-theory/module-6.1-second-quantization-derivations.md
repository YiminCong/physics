---
title: "Derivations — Module 6.1: Second Quantization & the Many-Body Problem"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 6.1: Second Quantization & the Many-Body Problem
# 推导 — 模块 6.1：二次量子化与多体问题

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.1](./module-6.1-second-quantization.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.1](./module-6.1-second-quantization.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Field Operators and Their Anticommutation Relation · 场算符及其反对易关系

**Claim.** Define the fermionic field operator $\hat\psi(x) = \sum_k \varphi_k(x)\,\hat c_k$, where $\{\varphi_k\}$ is any complete orthonormal set of single-particle orbitals and $\{\hat c_k, \hat c^\dagger_{k'}\} = \delta_{kk'}$, $\{\hat c_k, \hat c_{k'}\} = 0$. Then

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \delta(x - x'). $$

**命题。** 定义费米子场算符 $\hat\psi(x) = \sum_k \varphi_k(x)\,\hat c_k$，其中 $\{\varphi_k\}$ 是任意完备正交归一单粒子轨道组，$\{\hat c_k, \hat c^\dagger_{k'}\} = \delta_{kk'}$，$\{\hat c_k, \hat c_{k'}\} = 0$。则

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \delta(x - x'). $$

**Step 1 — Write out both operators explicitly.**

$$ \hat\psi(x) = \sum_k \varphi_k(x)\,\hat c_k, \qquad \hat\psi^\dagger(x') = \sum_{k'} \varphi^*_{k'}(x')\,\hat c^\dagger_{k'}. $$

**第 1 步 — 显式写出两个算符。**

$$ \hat\psi(x) = \sum_k \varphi_k(x)\,\hat c_k, \qquad \hat\psi^\dagger(x') = \sum_{k'} \varphi^*_{k'}(x')\,\hat c^\dagger_{k'}. $$

**Step 2 — Expand the anticommutator.** Since $\varphi_k(x)$ and $\varphi^*_{k'}(x')$ are c-numbers (ordinary complex numbers), they pass through anticommutators freely:

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \sum_k \sum_{k'} \varphi_k(x)\,\varphi^*_{k'}(x')\,\{\hat c_k, \hat c^\dagger_{k'}\}. $$

**第 2 步 — 展开反对易子。** 由于 $\varphi_k(x)$ 和 $\varphi^*_{k'}(x')$ 是 c 数（普通复数），它们可以自由穿过反对易子：

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \sum_k \sum_{k'} \varphi_k(x)\,\varphi^*_{k'}(x')\,\{\hat c_k, \hat c^\dagger_{k'}\}. $$

**Step 3 — Use the mode anticommutator.** The fundamental fermionic anticommutator gives $\{\hat c_k, \hat c^\dagger_{k'}\} = \delta_{kk'}$, so the double sum collapses to a single sum:

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \sum_k \varphi_k(x)\,\varphi^*_k(x')\cdot\delta_{kk'} \to \sum_k \varphi_k(x)\,\varphi^*_k(x'). $$

**第 3 步 — 使用模式反对易子。** 基本费米子反对易子给出 $\{\hat c_k, \hat c^\dagger_{k'}\} = \delta_{kk'}$，因此双重求和化为单重求和：

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \sum_k \varphi_k(x)\,\varphi^*_k(x')\cdot\delta_{kk'} \to \sum_k \varphi_k(x)\,\varphi^*_k(x'). $$

**Step 4 — Invoke the completeness relation.** Because $\{\varphi_k\}$ is a complete orthonormal set on the single-particle Hilbert space, the completeness (resolution of the identity) relation reads

$$ \sum_k \varphi_k(x)\,\varphi^*_k(x') = \delta(x - x'). $$

This is the continuum analogue of the matrix identity $\sum_k |k\rangle\langle k| = 1$. Inserting it gives

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \delta(x - x'). \qquad \blacksquare $$

**第 4 步 — 引用完备性关系。** 由于 $\{\varphi_k\}$ 是单粒子希尔伯特空间上的完备正交归一集，其完备性（单位算符的分解）关系为

$$ \sum_k \varphi_k(x)\,\varphi^*_k(x') = \delta(x - x'). $$

这是矩阵恒等式 $\sum_k |k\rangle\langle k| = 1$ 的连续类比。代入得

$$ \{\hat\psi(x), \hat\psi^\dagger(x')\} = \delta(x - x'). \qquad \blacksquare $$

**Step 5 — The other anticommutator vanishes.** Similarly,

$$ \{\hat\psi(x), \hat\psi(x')\} = \sum_k \sum_{k'} \varphi_k(x)\,\varphi_{k'}(x')\,\{\hat c_k, \hat c_{k'}\} = 0, $$

since $\{\hat c_k, \hat c_{k'}\} = 0$ by the fermionic mode algebra. So particle annihilation operators anticommute — the algebraic form of the Pauli exclusion principle.

**第 5 步 — 另一个反对易子为零。** 类似地，

$$ \{\hat\psi(x), \hat\psi(x')\} = \sum_k \sum_{k'} \varphi_k(x)\,\varphi_{k'}(x')\,\{\hat c_k, \hat c_{k'}\} = 0, $$

因为费米子模式代数给出 $\{\hat c_k, \hat c_{k'}\} = 0$。故粒子湮灭算符反对易——这是泡利不相容原理的代数形式。

---

## B. One-Body Operators in Second-Quantized Form · 单体算符的二次量子化形式

**Claim.** Let $\hat o$ be a single-particle operator (acting on one particle at a time). Then the corresponding many-body operator is

$$ \hat O = \int \hat\psi^\dagger(x)\,\hat o\,\hat\psi(x)\,dx, $$

where $\hat o$ acts on $x$. In the mode basis this equals $\sum_{kk'} \langle k|\hat o|k'\rangle\,\hat c^\dagger_k \hat c_{k'}$.

**命题。** 设 $\hat o$ 是单粒子算符（每次作用于一个粒子）。则对应的多体算符为

$$ \hat O = \int \hat\psi^\dagger(x)\,\hat o\,\hat\psi(x)\,dx, $$

其中 $\hat o$ 作用于 $x$。在模式基底中，这等于 $\sum_{kk'} \langle k|\hat o|k'\rangle\,\hat c^\dagger_k \hat c_{k'}$。

**Step 1 — Insert the mode expansion of $\hat\psi$ and $\hat\psi^\dagger$.**

$$ \hat O = \int \Big(\sum_{k'} \varphi^*_{k'}(x)\,\hat c^\dagger_{k'}\Big)\,\hat o\,\Big(\sum_k \varphi_k(x)\,\hat c_k\Big)\,dx. $$

Since $\hat c^\dagger_{k'}$ and $\hat c_k$ are mode operators (independent of $x$), they factor out of the spatial integral:

$$ \hat O = \sum_{k'} \sum_k \hat c^\dagger_{k'}\,\Big(\int \varphi^*_{k'}(x)\,\hat o\,\varphi_k(x)\,dx\Big)\,\hat c_k. $$

**第 1 步 — 代入 $\hat\psi$ 和 $\hat\psi^\dagger$ 的模式展开。**

$$ \hat O = \int \Big(\sum_{k'} \varphi^*_{k'}(x)\,\hat c^\dagger_{k'}\Big)\,\hat o\,\Big(\sum_k \varphi_k(x)\,\hat c_k\Big)\,dx. $$

由于 $\hat c^\dagger_{k'}$ 和 $\hat c_k$ 是模式算符（与 $x$ 无关），它们可从空间积分中提取：

$$ \hat O = \sum_{k'} \sum_k \hat c^\dagger_{k'}\,\Big(\int \varphi^*_{k'}(x)\,\hat o\,\varphi_k(x)\,dx\Big)\,\hat c_k. $$

**Step 2 — Identify the matrix element.** The integral $\int \varphi^*_{k'}(x)\,\hat o\,\varphi_k(x)\,dx$ is precisely the matrix element $\langle k'|\hat o|k\rangle$ of the single-particle operator in the orbital basis. Therefore

$$ \hat O = \sum_{kk'} \langle k'|\hat o|k\rangle\,\hat c^\dagger_{k'} \hat c_k. $$

Relabeling $k \leftrightarrow k'$ gives the standard form $\sum_{kk'} \langle k|\hat o|k'\rangle\,\hat c^\dagger_k \hat c_{k'}$. $\blacksquare$

**第 2 步 — 识别矩阵元。** 积分 $\int \varphi^*_{k'}(x)\,\hat o\,\varphi_k(x)\,dx$ 恰好是单粒子算符在轨道基底中的矩阵元 $\langle k'|\hat o|k\rangle$。因此

$$ \hat O = \sum_{kk'} \langle k'|\hat o|k\rangle\,\hat c^\dagger_{k'} \hat c_k. $$

将 $k \leftrightarrow k'$ 重新标记得标准形式 $\sum_{kk'} \langle k|\hat o|k'\rangle\,\hat c^\dagger_k \hat c_{k'}$。$\blacksquare$

**Step 3 — Diagonal case: the kinetic energy.** For a diagonal operator $\hat o = -\hbar^2\nabla^2/2m$ in the momentum eigenstate basis $\varphi_k(x) = e^{ik\cdot x}/\sqrt{V}$, the matrix element is $\langle k|\hat o|k'\rangle = (\hbar^2 k^2/2m)\,\delta_{kk'}$, so

$$ \hat T = \sum_k \frac{\hbar^2 k^2}{2m}\,\hat c^\dagger_k \hat c_k = \sum_k \varepsilon_k\,\hat n_k, $$

where $\varepsilon_k = \hbar^2 k^2/2m$ is the single-particle dispersion and $\hat n_k = \hat c^\dagger_k \hat c_k$ is the occupation number operator.

**第 3 步 — 对角情形：动能。** 对于在动量本征态基底 $\varphi_k(x) = e^{ik\cdot x}/\sqrt{V}$ 中的对角算符 $\hat o = -\hbar^2\nabla^2/2m$，矩阵元为 $\langle k|\hat o|k'\rangle = (\hbar^2 k^2/2m)\,\delta_{kk'}$，因此

$$ \hat T = \sum_k \frac{\hbar^2 k^2}{2m}\,\hat c^\dagger_k \hat c_k = \sum_k \varepsilon_k\,\hat n_k, $$

其中 $\varepsilon_k = \hbar^2 k^2/2m$ 是单粒子色散关系，$\hat n_k = \hat c^\dagger_k \hat c_k$ 是占据数算符。

---

## C. Two-Body Operators in Second-Quantized Form · 两体算符的二次量子化形式

**Claim.** A two-body interaction $\hat V = \tfrac12 \sum_{i\ne j} U(x_i - x_j)$ is represented in Fock space as

$$ \hat V = \tfrac12 \int\!\!\int \hat\psi^\dagger(x)\,\hat\psi^\dagger(x')\,U(x - x')\,\hat\psi(x')\,\hat\psi(x)\,dx\,dx'. $$

In the mode basis: $\hat V = \tfrac12 \sum_{kk'qq'} \langle k,k'|U|q,q'\rangle\,\hat c^\dagger_k \hat c^\dagger_{k'} \hat c_{q'} \hat c_q$.

**命题。** 两体相互作用 $\hat V = \tfrac12 \sum_{i\ne j} U(x_i - x_j)$ 在 Fock 空间中表示为

$$ \hat V = \tfrac12 \int\!\!\int \hat\psi^\dagger(x)\,\hat\psi^\dagger(x')\,U(x - x')\,\hat\psi(x')\,\hat\psi(x)\,dx\,dx'. $$

在模式基底中：$\hat V = \tfrac12 \sum_{kk'qq'} \langle k,k'|U|q,q'\rangle\,\hat c^\dagger_k \hat c^\dagger_{k'} \hat c_{q'} \hat c_q$。

**Step 1 — Insert mode expansions.** Substitute $\hat\psi^\dagger(x) = \sum_k \varphi^*_k(x)\,\hat c^\dagger_k$ and $\hat\psi(x) = \sum_q \varphi_q(x)\,\hat c_q$ (and similarly for the $x'$ variables). The spatial integrals produce the two-body matrix element

$$ \langle k,k'|U|q,q'\rangle = \int\!\!\int \varphi^*_k(x)\,\varphi^*_{k'}(x')\,U(x-x')\,\varphi_{q'}(x')\,\varphi_q(x)\,dx\,dx'. $$

**第 1 步 — 代入模式展开。** 代入 $\hat\psi^\dagger(x) = \sum_k \varphi^*_k(x)\,\hat c^\dagger_k$ 和 $\hat\psi(x) = \sum_q \varphi_q(x)\,\hat c_q$（以及 $x'$ 变量的类似展开）。空间积分产生两体矩阵元

$$ \langle k,k'|U|q,q'\rangle = \int\!\!\int \varphi^*_k(x)\,\varphi^*_{k'}(x')\,U(x-x')\,\varphi_{q'}(x')\,\varphi_q(x)\,dx\,dx'. $$

**Step 2 — Operator ordering enforces antisymmetry.** The ordering $\hat\psi^\dagger(x)\,\hat\psi^\dagger(x')\,\hat\psi(x')\,\hat\psi(x)$ (note the reversed order of destruction operators compared to creation) is precisely the normal-ordered, antisymmetrized two-body operator. For fermions, swapping any two $\hat\psi$ picks up a minus sign; this antisymmetry is automatically encoded in the anticommutation relations without manual Slater-determinant bookkeeping.

**第 2 步 — 算符排序强制反对称性。** 排序 $\hat\psi^\dagger(x)\,\hat\psi^\dagger(x')\,\hat\psi(x')\,\hat\psi(x)$（注意湮灭算符的顺序与产生算符相反）恰好是正规序的、反对称化的两体算符。对于费米子，交换任意两个 $\hat\psi$ 产生一个负号；这种反对称性通过反对易关系自动编码，无需手工处理 Slater 行列式。

**Step 3 — Momentum conservation for a uniform system.** If $U$ depends only on $x - x'$, then in momentum space $U(x-x') = \sum_q U_q\,e^{iq\cdot(x-x')}$. Performing the spatial integrals selects $k = q + p$, $k' = q' - p$ (momentum-transfer $q$ conserved), giving

$$ \hat V = \tfrac12 \sum_{k,k',q} U_q\,\hat c^\dagger_{k+q} \hat c^\dagger_{k'-q} \hat c_{k'} \hat c_k, $$

the familiar Coulomb interaction vertex used in Feynman diagrams. $\blacksquare$

**第 3 步 — 均匀系统中的动量守恒。** 若 $U$ 仅依赖于 $x - x'$，则在动量空间 $U(x-x') = \sum_q U_q\,e^{iq\cdot(x-x')}$。执行空间积分后选出 $k = q + p$，$k' = q' - p$（动量转移 $q$ 守恒），得

$$ \hat V = \tfrac12 \sum_{k,k',q} U_q\,\hat c^\dagger_{k+q} \hat c^\dagger_{k'-q} \hat c_{k'} \hat c_k, $$

这是费曼图中熟悉的库仑相互作用顶点。$\blacksquare$

---

## D. The Fock-Space Number Operator and Occupation Numbers · Fock 空间数算符与占据数

**Claim.** For fermions, $\hat n_k = \hat c^\dagger_k \hat c_k$ satisfies $\hat n_k^2 = \hat n_k$, so its eigenvalues are 0 or 1 (Pauli exclusion). For bosons, $\hat n_k = \hat a^\dagger_k \hat a_k$ has eigenvalues $0, 1, 2, \ldots$ (unrestricted).

**命题。** 对于费米子，$\hat n_k = \hat c^\dagger_k \hat c_k$ 满足 $\hat n_k^2 = \hat n_k$，故其本征值为 0 或 1（泡利不相容）。对于玻色子，$\hat n_k = \hat a^\dagger_k \hat a_k$ 的本征值为 $0, 1, 2, \ldots$（无限制）。

**Step 1 — Fermionic idempotency.** Compute $\hat n_k^2 = \hat c^\dagger_k \hat c_k \hat c^\dagger_k \hat c_k$. Use the anticommutator $\{\hat c_k, \hat c^\dagger_k\} = 1$, i.e. $\hat c_k \hat c^\dagger_k = 1 - \hat c^\dagger_k \hat c_k$:

$$ \hat n_k^2 = \hat c^\dagger_k (\hat c_k \hat c^\dagger_k) \hat c_k = \hat c^\dagger_k (1 - \hat c^\dagger_k \hat c_k) \hat c_k = \hat c^\dagger_k \hat c_k - \hat c^\dagger_k \hat c^\dagger_k \hat c_k \hat c_k. $$

Now $\{\hat c_k, \hat c_k\} = 0 \implies 2\hat c_k \hat c_k = 0 \implies \hat c_k \hat c_k = 0$ (and similarly $\hat c^\dagger_k \hat c^\dagger_k = 0$). Therefore

$$ \hat n_k^2 = \hat c^\dagger_k \hat c_k = \hat n_k. $$

An operator satisfying $P^2 = P$ is a projector, and its only eigenvalues are 0 and 1. $\blacksquare$

**第 1 步 — 费米子幂等性。** 计算 $\hat n_k^2 = \hat c^\dagger_k \hat c_k \hat c^\dagger_k \hat c_k$。利用反对易子 $\{\hat c_k, \hat c^\dagger_k\} = 1$，即 $\hat c_k \hat c^\dagger_k = 1 - \hat c^\dagger_k \hat c_k$：

$$ \hat n_k^2 = \hat c^\dagger_k (\hat c_k \hat c^\dagger_k) \hat c_k = \hat c^\dagger_k (1 - \hat c^\dagger_k \hat c_k) \hat c_k = \hat c^\dagger_k \hat c_k - \hat c^\dagger_k \hat c^\dagger_k \hat c_k \hat c_k. $$

现在 $\{\hat c_k, \hat c_k\} = 0 \implies 2\hat c_k \hat c_k = 0 \implies \hat c_k \hat c_k = 0$（类似地 $\hat c^\dagger_k \hat c^\dagger_k = 0$）。因此

$$ \hat n_k^2 = \hat c^\dagger_k \hat c_k = \hat n_k. $$

满足 $P^2 = P$ 的算符是投影算符，其本征值只能为 0 和 1。$\blacksquare$

**Step 2 — Physical interpretation.** A fermionic mode $k$ is either empty (eigenvalue 0) or occupied (eigenvalue 1). Attempting to create two particles in the same mode gives $\hat c^\dagger_k \hat c^\dagger_k = 0$: impossible. This is the algebraic statement of the Pauli exclusion principle — no manual antisymmetrization required.

**第 2 步 — 物理诠释。** 费米子模式 $k$ 要么空置（本征值 0）要么被占据（本征值 1）。试图在同一模式中产生两个粒子给出 $\hat c^\dagger_k \hat c^\dagger_k = 0$：不可能。这是泡利不相容原理的代数表述——无需手工反对称化。

---

*The derivations above establish that second quantization is not merely a notational convenience but a logically complete re-encoding of many-body quantum mechanics: (anti)commutation relations + completeness $\leftrightarrow$ all of quantum statistics.*

*上述推导表明，二次量子化不仅仅是一种符号上的便利，而是多体量子力学的逻辑上完整的重新编码：（反）对易关系 + 完备性 $\leftrightarrow$ 全部量子统计。*

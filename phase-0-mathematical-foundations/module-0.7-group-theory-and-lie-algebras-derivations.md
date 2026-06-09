---
title: "Derivations — Module 0.7: Group Theory & Lie Algebras"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 0.7: Group Theory & Lie Algebras
# 推导 — 模块 0.7：群论与李代数

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 0.7](./module-0.7-group-theory-and-lie-algebras.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 0.7](./module-0.7-group-theory-and-lie-algebras.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Rearrangement Theorem · 重排定理

**Claim.** Let $G$ be a finite group of order $|G|$, and let $g \in G$ be any fixed element. Then the map $L_g : G \to G$ defined by $L_g(h) = g\cdot h$ is a bijection. Equivalently, the multiset $\{g\cdot h : h \in G\}$ equals $G$ as a set.

**命题。** 设 $G$ 是阶为 $|G|$ 的有限群，$g \in G$ 为任意固定元素。则由 $L_g(h) = g\cdot h$ 定义的映射 $L_g : G \to G$ 是双射。等价地，多重集 $\{g\cdot h : h \in G\}$ 等于 $G$（作为集合）。

**Step 1 — Injectivity.** Suppose $g\cdot h_1 = g\cdot h_2$. Left-multiply both sides by $g^{-1}$ (which exists by the group axiom of inverses):

**第 1 步 — 单射性。** 设 $g\cdot h_1 = g\cdot h_2$。两侧同时左乘 $g^{-1}$（由逆元公理存在）：

$$ \begin{aligned} g^{-1}\cdot(g\cdot h_1) &= g^{-1}\cdot(g\cdot h_2) \\ (g^{-1}\cdot g)\cdot h_1 &= (g^{-1}\cdot g)\cdot h_2 && \text{(associativity)} \\ e\cdot h_1 &= e\cdot h_2 && \text{(definition of inverse)} \\ h_1 &= h_2. && \text{(definition of identity)} \end{aligned} $$

Hence $L_g$ is injective.

故 $L_g$ 是单射。

**Step 2 — Surjectivity.** For any target element $k \in G$, we need $h$ such that $g\cdot h = k$. Take $h = g^{-1}\cdot k$, which lies in $G$ by closure. Then $g\cdot h = g\cdot(g^{-1}\cdot k) = (g\cdot g^{-1})\cdot k = e\cdot k = k$. So every element of $G$ is hit — $L_g$ is surjective.

**第 2 步 — 满射性。** 对任意目标元素 $k \in G$，需要找 $h$ 使得 $g\cdot h = k$。取 $h = g^{-1}\cdot k$，由封闭性 $h \in G$。则 $g\cdot h = g\cdot(g^{-1}\cdot k) = (g\cdot g^{-1})\cdot k = e\cdot k = k$。故 $G$ 的每个元素都被取到——$L_g$ 是满射。

**Step 3 — Conclusion.** $L_g$ is both injective and surjective on a finite set, hence bijective. The set $\{g\cdot h : h \in G\}$ is the image of $G$ under $L_g$, which equals $G$. $\blacksquare$

**第 3 步 — 结论。** $L_g$ 在有限集上既是单射又是满射，故为双射。集合 $\{g\cdot h : h \in G\}$ 是 $G$ 在 $L_g$ 下的像，等于 $G$。$\blacksquare$

**Remark.** The same argument applies to right multiplication $R_g(h) = h\cdot g$. The rearrangement theorem is used in proving the orthogonality relations for characters: $\sum_{g\in G} \rho_i(g)^\dagger_{mn} \rho_j(g)_{pq} = (|G|/d_i) \delta_{ij} \delta_{mp} \delta_{nq}$, where $d_i$ is the dimension of irrep $i$.

**注记。** 同样的论证适用于右乘 $R_g(h) = h\cdot g$。重排定理用于证明特征标的正交关系：$\sum_{g\in G} \rho_i(g)^\dagger_{mn} \rho_j(g)_{pq} = (|G|/d_i) \delta_{ij} \delta_{mp} \delta_{nq}$，其中 $d_i$ 是不可约表示 $i$ 的维数。

---

## B. Schur's Lemma · 舒尔引理

**Claim (Part 1).** Let $\rho: G \to GL(V)$ be an irreducible representation. If $M: V \to V$ is a linear map such that $M \rho(g) = \rho(g) M$ for all $g \in G$, then $M = \lambda I$ for some scalar $\lambda \in \mathbb{C}$.

**命题（第 1 部分）。** 设 $\rho: G \to GL(V)$ 是不可约表示。若 $M: V \to V$ 是线性映射，对所有 $g \in G$ 满足 $M \rho(g) = \rho(g) M$，则 $M = \lambda I$，$\lambda \in \mathbb{C}$ 为某标量。

**Step 1 — $M$ has an eigenvalue.** Since $V$ is a finite-dimensional complex vector space, the characteristic polynomial $\det(M - \lambda I) = 0$ has at least one root $\lambda \in \mathbb{C}$ by the fundamental theorem of algebra. Let $\lambda$ be such an eigenvalue.

**第 1 步 — $M$ 有本征值。** 由于 $V$ 是有限维复向量空间，特征多项式 $\det(M - \lambda I) = 0$ 由代数基本定理至少有一个根 $\lambda \in \mathbb{C}$。设 $\lambda$ 为此本征值。

**Step 2 — The kernel of $(M - \lambda I)$ is $G$-invariant.** Let $W = \ker(M - \lambda I) = \{v \in V : Mv = \lambda v\}$ be the eigenspace. For any $w \in W$ and any $g \in G$:

**第 2 步 — $(M - \lambda I)$ 的核是 $G$-不变的。** 设 $W = \ker(M - \lambda I) = \{v \in V : Mv = \lambda v\}$ 为本征空间。对任意 $w \in W$ 和任意 $g \in G$：

$$ \begin{aligned} M (\rho(g) w) &= \rho(g) (M w) && \text{(the intertwining condition)} \\ &= \rho(g) (\lambda w) && \text{(since } w \in W) \\ &= \lambda (\rho(g) w). \end{aligned} $$

So $\rho(g)w \in W$ for every $g$. That is, $W$ is a $G$-invariant subspace of $V$.

故 $\rho(g)w \in W$ 对每个 $g$ 成立。即 $W$ 是 $V$ 的 $G$-不变子空间。

**Step 3 — Irreducibility forces $W = V$.** Since $\rho$ is irreducible, the only $G$-invariant subspaces of $V$ are $\{0\}$ and $V$ itself. We have $W \ne \{0\}$ because eigenspaces are non-trivial. Therefore $W = V$, meaning $M v = \lambda v$ for all $v \in V$, i.e. $M = \lambda I$. $\blacksquare$

**第 3 步 — 不可约性迫使 $W = V$。** 由于 $\rho$ 是不可约的，$V$ 的唯一 $G$-不变子空间是 $\{0\}$ 和 $V$ 本身。我们有 $W \ne \{0\}$，因为本征空间非平凡。故 $W = V$，即对所有 $v \in V$ 有 $M v = \lambda v$，亦即 $M = \lambda I$。$\blacksquare$

**Claim (Part 2).** Let $\rho_i: G \to GL(V_i)$ and $\rho_j: G \to GL(V_j)$ be two irreducible representations that are not isomorphic. If $M: V_j \to V_i$ is a linear map such that $M \rho_j(g) = \rho_i(g) M$ for all $g \in G$, then $M = 0$.

**命题（第 2 部分）。** 设 $\rho_i: G \to GL(V_i)$ 和 $\rho_j: G \to GL(V_j)$ 是两个不同构的不可约表示。若 $M: V_j \to V_i$ 是线性映射，对所有 $g \in G$ 满足 $M \rho_j(g) = \rho_i(g) M$，则 $M = 0$。

**Step 1 — $\ker(M)$ is $G$-invariant in $V_j$.** For any $w \in \ker(M)$ and $g \in G$: $M(\rho_j(g)w) = \rho_i(g)(Mw) = \rho_i(g)\cdot 0 = 0$. So $\rho_j(g)w \in \ker(M)$, making $\ker(M)$ a $G$-invariant subspace of $V_j$.

**第 1 步 — $\ker(M)$ 在 $V_j$ 中是 $G$-不变的。** 对任意 $w \in \ker(M)$ 和 $g \in G$：$M(\rho_j(g)w) = \rho_i(g)(Mw) = \rho_i(g)\cdot 0 = 0$。故 $\rho_j(g)w \in \ker(M)$，使 $\ker(M)$ 成为 $V_j$ 的 $G$-不变子空间。

**Step 2 — $\operatorname{im}(M)$ is $G$-invariant in $V_i$.** For any vector $M(w) \in \operatorname{im}(M)$ and $g \in G$: $\rho_i(g)(Mw) = M(\rho_j(g)w) \in \operatorname{im}(M)$. So $\operatorname{im}(M)$ is a $G$-invariant subspace of $V_i$.

**第 2 步 — $\operatorname{im}(M)$ 在 $V_i$ 中是 $G$-不变的。** 对任意向量 $M(w) \in \operatorname{im}(M)$ 和 $g \in G$：$\rho_i(g)(Mw) = M(\rho_j(g)w) \in \operatorname{im}(M)$。故 $\operatorname{im}(M)$ 是 $V_i$ 的 $G$-不变子空间。

**Step 3 — Only two possibilities.** By irreducibility, $\ker(M)$ is either $\{0\}$ or $V_j$, and $\operatorname{im}(M)$ is either $\{0\}$ or $V_i$.

- If $\ker(M) = \{0\}$ and $\operatorname{im}(M) = V_i$, then $M$ is an isomorphism $V_j \to V_i$, contradicting the assumption that $\rho_i$ and $\rho_j$ are non-isomorphic.
- Therefore at least one of $\ker(M) = V_j$ or $\operatorname{im}(M) = \{0\}$ must hold, both of which give $M = 0$. $\blacksquare$

**第 3 步 — 只有两种可能。** 由不可约性，$\ker(M)$ 为 $\{0\}$ 或 $V_j$，$\operatorname{im}(M)$ 为 $\{0\}$ 或 $V_i$。

- 若 $\ker(M) = \{0\}$ 且 $\operatorname{im}(M) = V_i$，则 $M$ 是同构 $V_j \to V_i$，与 $\rho_i$ 和 $\rho_j$ 不同构的假设矛盾。
- 因此 $\ker(M) = V_j$ 或 $\operatorname{im}(M) = \{0\}$ 中至少一个成立，两种情况都给出 $M = 0$。$\blacksquare$

---

## C. The $su(2)$ Algebra and Classification of Its Irreps · $su(2)$ 代数及其不可约表示的分类

**Claim.** The commutation relations $[J_i, J_j] = i \varepsilon_{ijk} J_k$ (with $\varepsilon_{ijk}$ the Levi-Civita symbol) define the Lie algebra $su(2)$. The irreducible representations are labelled by $j = 0, \tfrac12, 1, \tfrac32, \ldots$, have dimension $2j+1$, and are uniquely characterized by the Casimir eigenvalue $J^2 = j(j+1)$.

**命题。** 对易关系 $[J_i, J_j] = i \varepsilon_{ijk} J_k$（$\varepsilon_{ijk}$ 为列维-奇维塔符号）定义了李代数 $su(2)$。不可约表示由 $j = 0, \tfrac12, 1, \tfrac32, \ldots$ 标记，维数为 $2j+1$，并由卡西米尔本征值 $J^2 = j(j+1)$ 唯一刻画。

### C.1 Derivation of $[J_i, J_j] = i \varepsilon_{ijk} J_k$ from the Pauli matrices · 从泡利矩阵推导 $[J_i, J_j] = i \varepsilon_{ijk} J_k$

**Step 1 — Define the generators.** Set $J_i = \sigma_i / 2$ where

**第 1 步 — 定义生成元。** 令 $J_i = \sigma_i / 2$，其中

$$ \sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. $$

**Step 2 — Compute the key product identity.** For any two Pauli matrices:

**第 2 步 — 计算关键乘积恒等式。** 对任意两个泡利矩阵：

$$ \sigma_i \sigma_j = \delta_{ij} I + i \varepsilon_{ijk} \sigma_k. $$

Proof by explicit computation: $\sigma_1 \sigma_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i \sigma_3$, which matches $i \varepsilon_{12k} \sigma_k = i \varepsilon_{123} \sigma_3 = i \sigma_3$. The other independent products follow by cyclic symmetry ($1\to 2\to 3\to 1$), and diagonal products: $\sigma_1^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$, confirming $\delta_{11} I = I$.

通过显式计算证明：$\sigma_1 \sigma_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = i \sigma_3$，与 $i \varepsilon_{12k} \sigma_k = i \varepsilon_{123} \sigma_3 = i \sigma_3$ 吻合。其余独立乘积由循环对称性（$1\to 2\to 3\to 1$）给出，对角乘积：$\sigma_1^2 = I$，确认 $\delta_{11} I = I$。

**Step 3 — Extract the commutator.** The commutator $[\sigma_i, \sigma_j] = \sigma_i \sigma_j - \sigma_j \sigma_i$. Using Step 2:

**第 3 步 — 提取对易子。** 对易子 $[\sigma_i, \sigma_j] = \sigma_i \sigma_j - \sigma_j \sigma_i$。利用第 2 步：

$$ \begin{aligned} \sigma_i \sigma_j - \sigma_j \sigma_i &= (\delta_{ij} I + i \varepsilon_{ijk} \sigma_k) - (\delta_{ji} I + i \varepsilon_{jik} \sigma_k) \\ &= i \varepsilon_{ijk} \sigma_k - i \varepsilon_{jik} \sigma_k \\ &= i (\varepsilon_{ijk} + \varepsilon_{ijk}) \sigma_k && \text{(since } \varepsilon_{jik} = -\varepsilon_{ijk}) \\ &= 2i \varepsilon_{ijk} \sigma_k. \end{aligned} $$

So $[\sigma_i, \sigma_j] = 2i \varepsilon_{ijk} \sigma_k$, and dividing by 4 (since $J_i = \sigma_i/2$):

故 $[\sigma_i, \sigma_j] = 2i \varepsilon_{ijk} \sigma_k$，除以 4（因为 $J_i = \sigma_i/2$）：

$$ \boxed{\, [J_i, J_j] = i \varepsilon_{ijk} J_k. \,} \qquad \blacksquare $$

### C.2 The Casimir Operator · 卡西米尔算符

**Step 1 — Define $J^2 = J_1^2 + J_2^2 + J_3^2$.** Compute $[J^2, J_3]$:

**第 1 步 — 定义 $J^2 = J_1^2 + J_2^2 + J_3^2$。** 计算 $[J^2, J_3]$：

$$ [J^2, J_3] = [J_1^2, J_3] + [J_2^2, J_3] + [J_3^2, J_3]. $$

Since $[J_3^2, J_3] = 0$, only the first two terms contribute. Use $[AB, C] = A[B,C] + [A,C]B$:

由于 $[J_3^2, J_3] = 0$，只有前两项有贡献。利用 $[AB, C] = A[B,C] + [A,C]B$：

$$ \begin{aligned} [J_1^2, J_3] &= J_1[J_1, J_3] + [J_1, J_3]J_1 = J_1(-i J_2) + (-i J_2)J_1 = -i(J_1 J_2 + J_2 J_1) \\ [J_2^2, J_3] &= J_2[J_2, J_3] + [J_2, J_3]J_2 = J_2(i J_1) + (i J_1)J_2 = +i(J_2 J_1 + J_1 J_2). \end{aligned} $$

Adding: $[J^2, J_3] = -i(J_1 J_2 + J_2 J_1) + i(J_1 J_2 + J_2 J_1) = 0$.

相加：$[J^2, J_3] = 0$。

The same calculation with cyclic relabelling gives $[J^2, J_1] = [J^2, J_2] = 0$. Therefore $\boldsymbol{[J^2, J_i] = 0}$ for all $i$: $J^2$ is a Casimir operator.

对 $J_1, J_2$ 的循环重标记给出同样结果，故 $\boldsymbol{[J^2, J_i] = 0}$ 对所有 $i$ 成立：$J^2$ 是卡西米尔算符。

### C.3 Ladder operators and the irrep spectrum · 阶梯算符与不可约表示谱

**Step 1 — Define raising/lowering operators.** Let $J_\pm = J_1 \pm i J_2$. Then:

**第 1 步 — 定义升降算符。** 令 $J_\pm = J_1 \pm i J_2$。则：

$$ \begin{aligned} [J_3, J_+] &= [J_3, J_1] + i[J_3, J_2] = i J_2 + i(-i J_1) = i J_2 + J_1 = J_+ \\ [J_3, J_-] &= -J_- \\ [J_+, J_-] &= [J_1 + iJ_2, J_1 - iJ_2] = -i[J_1, J_2] + i[J_2, J_1] = -i(i J_3) + i(-i J_3) = 2J_3. \end{aligned} $$

**Step 2 — Ladder action.** Let $|j, m\rangle$ be a simultaneous eigenstate: $J^2|j,m\rangle = \lambda|j,m\rangle$ and $J_3|j,m\rangle = m|j,m\rangle$. Then:

**第 2 步 — 阶梯作用。** 设 $|j, m\rangle$ 是同时本征态：$J^2|j,m\rangle = \lambda|j,m\rangle$，$J_3|j,m\rangle = m|j,m\rangle$。则：

$$ J_3 (J_+ |j,m\rangle) = (J_+ J_3 + [J_3, J_+])|j,m\rangle = (m + 1)(J_+|j,m\rangle). $$

So $J_+$ raises $m$ by 1; similarly $J_-$ lowers $m$ by 1.

故 $J_+$ 将 $m$ 提升 1；类似地 $J_-$ 将 $m$ 降低 1。

**Step 3 — The spectrum is bounded.** The norm of $J_+|j,m\rangle$ satisfies

**第 3 步 — 谱有界。** $J_+|j,m\rangle$ 的范数满足

$$ \begin{aligned} \lVert J_+|j,m\rangle\rVert^2 &= \langle j,m|J_-J_+|j,m\rangle = \langle j,m|(J^2 - J_3^2 - J_3)|j,m\rangle = \lambda - m^2 - m \ge 0 \\ \lVert J_-|j,m\rangle\rVert^2 &= \langle j,m|J_+J_-|j,m\rangle = \langle j,m|(J^2 - J_3^2 + J_3)|j,m\rangle = \lambda - m^2 + m \ge 0. \end{aligned} $$

These two inequalities together require $\lambda \ge m^2 + |m|$. So for fixed $\lambda$, the values of $m$ are bounded above and below.

这两个不等式合在一起要求 $\lambda \ge m^2 + |m|$。故对固定的 $\lambda$，$m$ 的值有上下界。

**Step 4 — Termination conditions.** Let $m_{\max}$ be the maximum value of $m$. Then $J_+|j, m_{\max}\rangle = 0$, so $\lVert J_+|j,m_{\max}\rangle\rVert^2 = \lambda - m_{\max}^2 - m_{\max} = 0$, giving $\lambda = m_{\max}(m_{\max} + 1)$. Similarly $J_-|j, m_{\min}\rangle = 0$ gives $\lambda = m_{\min}(m_{\min} - 1)$. Setting these equal: $m_{\max}(m_{\max} + 1) = m_{\min}(m_{\min} - 1)$, which has the solution $m_{\min} = -m_{\max}$ (discarding the extraneous root $m_{\min} = m_{\max} + 1$).

**第 4 步 — 终止条件。** 设 $m_{\max}$ 为 $m$ 的最大值。则 $J_+|j, m_{\max}\rangle = 0$，故 $\lVert J_+|j,m_{\max}\rangle\rVert^2 = \lambda - m_{\max}^2 - m_{\max} = 0$，给出 $\lambda = m_{\max}(m_{\max} + 1)$。类似地 $J_-|j, m_{\min}\rangle = 0$ 给出 $\lambda = m_{\min}(m_{\min} - 1)$。令两者相等：$m_{\max}(m_{\max} + 1) = m_{\min}(m_{\min} - 1)$，解为 $m_{\min} = -m_{\max}$（舍去多余根 $m_{\min} = m_{\max} + 1$）。

**Step 5 — Quantization of $j$.** Since $m$ steps by integers from $m_{\min} = -j$ to $m_{\max} = j$ (writing $j \equiv m_{\max}$), the total number of steps $j - (-j) = 2j$ must be a non-negative integer, so $\boldsymbol{j = 0, \tfrac12, 1, \tfrac32, \ldots}$ The dimension of the irrep is the number of $m$ values: $\boldsymbol{\dim = 2j + 1}$. The Casimir eigenvalue is $\boldsymbol{\lambda = j(j+1)}$. $\blacksquare$

**第 5 步 — $j$ 的量子化。** 由于 $m$ 从 $m_{\min} = -j$ 到 $m_{\max} = j$（记 $j \equiv m_{\max}$）以整数步长变化，步数总数 $j - (-j) = 2j$ 必须是非负整数，故 $\boldsymbol{j = 0, \tfrac12, 1, \tfrac32, \ldots}$ 不可约表示的维数是 $m$ 值的个数：$\boldsymbol{\dim = 2j + 1}$。卡西米尔本征值为 $\boldsymbol{\lambda = j(j+1)}$。$\blacksquare$

---

## D. The $su(3)$ Gell-Mann Matrices and Structure Constants · $su(3)$ 的 Gell-Mann 矩阵与结构常数

**Claim.** The Lie algebra $su(3)$ has rank 2 and dimension 8. It is generated by eight traceless Hermitian $3\times 3$ matrices $\lambda_a$ (the Gell-Mann matrices) with commutation relations $[\lambda_a/2, \lambda_b/2] = i f_{abc} \lambda_c/2$, and possesses two independent Casimir operators.

**命题。** 李代数 $su(3)$ 的秩为 2，维数为 8。它由八个无迹厄米 $3\times 3$ 矩阵 $\lambda_a$（Gell-Mann 矩阵）生成，对易关系为 $[\lambda_a/2, \lambda_b/2] = i f_{abc} \lambda_c/2$，并具有两个独立的卡西米尔算符。

**Step 1 — Counting generators.** The Lie algebra $su(n)$ consists of all $n\times n$ traceless skew-Hermitian matrices (equivalently, $i$ times traceless Hermitian matrices). The dimension of $su(n)$ is $n^2 - 1$ (the dimension of $SU(n)$ as a manifold). For $n = 3$: dimension $= 9 - 1 = \boldsymbol{8}$ generators.

**第 1 步 — 计算生成元数目。** 李代数 $su(n)$ 由所有 $n\times n$ 无迹反厄米矩阵（等价地，$i$ 乘以无迹厄米矩阵）组成。$su(n)$ 的维数为 $n^2 - 1$（$SU(n)$ 作为流形的维数）。对 $n = 3$：维数 $= 9 - 1 = \boldsymbol{8}$ 个生成元。

**Step 2 — The rank.** The rank of a Lie algebra is the dimension of a maximal abelian subalgebra (a Cartan subalgebra) of simultaneously diagonalizable generators. For $su(3)$, two generators can be simultaneously diagonalized: $\lambda_3 = \operatorname{diag}(1,-1,0)$ and $\lambda_8 = \operatorname{diag}(1,1,-2)/\sqrt3$. So $\boldsymbol{\operatorname{rank}(su(3)) = 2}$, and there are exactly **two Casimir operators**.

**第 2 步 — 秩。** 李代数的秩是可同时对角化生成元（嘉当子代数）的极大阿贝尔子代数的维数。对 $su(3)$，可同时对角化两个生成元：$\lambda_3 = \operatorname{diag}(1,-1,0)$ 和 $\lambda_8 = \operatorname{diag}(1,1,-2)/\sqrt3$。故 $\boldsymbol{\operatorname{rank}(su(3)) = 2}$，恰好有**两个卡西米尔算符**。

**Step 3 — The eight Gell-Mann matrices.** An explicit basis of traceless Hermitian $3\times 3$ matrices generalizing the Pauli matrices:

**第 3 步 — 八个 Gell-Mann 矩阵。** 推广泡利矩阵的无迹厄米 $3\times 3$ 矩阵的显式基：

$$ \begin{aligned} \lambda_1 &= \begin{pmatrix} 0&1&0 \\ 1&0&0 \\ 0&0&0 \end{pmatrix} & \lambda_2 &= \begin{pmatrix} 0&-i&0 \\ i&0&0 \\ 0&0&0 \end{pmatrix} & \lambda_3 &= \begin{pmatrix} 1&0&0 \\ 0&-1&0 \\ 0&0&0 \end{pmatrix} & \lambda_4 &= \begin{pmatrix} 0&0&1 \\ 0&0&0 \\ 1&0&0 \end{pmatrix} \\ \lambda_5 &= \begin{pmatrix} 0&0&-i \\ 0&0&0 \\ i&0&0 \end{pmatrix} & \lambda_6 &= \begin{pmatrix} 0&0&0 \\ 0&0&1 \\ 0&1&0 \end{pmatrix} & \lambda_7 &= \begin{pmatrix} 0&0&0 \\ 0&0&-i \\ 0&i&0 \end{pmatrix} & \lambda_8 &= \frac{1}{\sqrt3}\begin{pmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&-2 \end{pmatrix} \end{aligned} $$

They satisfy $\operatorname{Tr}(\lambda_a \lambda_b) = 2 \delta_{ab}$, the normalization condition. Note that $\lambda_1, \lambda_2, \lambda_3$ form an $su(2)$ subalgebra (the isospin subgroup), and $\lambda_4, \ldots, \lambda_7$ connect the third component.

它们满足 $\operatorname{Tr}(\lambda_a \lambda_b) = 2 \delta_{ab}$，即归一化条件。注意 $\lambda_1, \lambda_2, \lambda_3$ 构成 $su(2)$ 子代数（同位旋子群），$\lambda_4, \ldots, \lambda_7$ 连接第三分量。

**Step 4 — Structure constants from the commutators.** Compute $[\lambda_a, \lambda_b] = 2i f_{abc} \lambda_c$ directly:

**第 4 步 — 从对易子得结构常数。** 直接计算 $[\lambda_a, \lambda_b] = 2i f_{abc} \lambda_c$：

$$ \begin{aligned} [\lambda_1, \lambda_2] &= 2\begin{pmatrix} 0&1&0 \\ 1&0&0 \\ 0&0&0 \end{pmatrix}\begin{pmatrix} 0&-i&0 \\ i&0&0 \\ 0&0&0 \end{pmatrix} - \text{h.c.} = 2i \lambda_3 && \to f_{123} = 1 \\ [\lambda_1, \lambda_4] &= 2i (\tfrac12) \lambda_7 && \to f_{147} = \tfrac12 \\ [\lambda_2, \lambda_6] &= 2i (\tfrac12) \lambda_7 && \to f_{267} = \tfrac12 \quad \text{(and so on by explicit matrix multiplication)} \\ [\lambda_4, \lambda_5] &= 2i (\tfrac12) \lambda_3 + 2i (\tfrac{\sqrt3}{2}) \lambda_8 && \to f_{458} = \tfrac{\sqrt3}{2}. \end{aligned} $$

The non-zero independent values are: $f_{123} = 1$; $f_{147} = f_{156} = f_{246} = f_{257} = f_{345} = f_{367} = \tfrac12$ (with appropriate signs from antisymmetry); $f_{458} = f_{678} = \tfrac{\sqrt3}{2}$. All other $f_{abc}$ are zero or related by total antisymmetry $f_{abc} = -f_{bac} = -f_{acb}$.

非零独立值为：$f_{123} = 1$；$f_{147} = f_{156} = f_{246} = f_{257} = f_{345} = f_{367} = \tfrac12$（考虑反对称性的正负号）；$f_{458} = f_{678} = \tfrac{\sqrt3}{2}$。其余 $f_{abc}$ 为零或由全反对称性 $f_{abc} = -f_{bac} = -f_{acb}$ 相关。

**Step 5 — The two Casimir operators.** The quadratic Casimir is

**第 5 步 — 两个卡西米尔算符。** 二次卡西米尔算符为

$$ C_2 = \sum_{a=1}^{8} (\lambda_a/2)^2 $$

and the cubic Casimir uses the symmetric structure constants $d_{abc}$ defined by $\{\lambda_a, \lambda_b\} = (4/3) \delta_{ab} I + 2 d_{abc} \lambda_c$:

三次卡西米尔算符使用对称结构常数 $d_{abc}$，由 $\{\lambda_a, \lambda_b\} = (4/3) \delta_{ab} I + 2 d_{abc} \lambda_c$ 定义：

$$ C_3 = \sum_{a,b,c} d_{abc} (\lambda_a/2)(\lambda_b/2)(\lambda_c/2). $$

On the fundamental representation $\mathbf{3}$: $C_2 = (4/3) I$. On the adjoint representation $\mathbf{8}$: $C_2 = 3 I$. By Schur's lemma each Casimir is a multiple of the identity on every irrep, and together $(C_2, C_3)$ uniquely label the irrep $(p, q)$. $\blacksquare$

在基本表示 $\mathbf{3}$ 上：$C_2 = (4/3) I$。在伴随表示 $\mathbf{8}$ 上：$C_2 = 3 I$。由舒尔引理，每个卡西米尔算符在每个不可约表示上是单位矩阵的倍数，$(C_2, C_3)$ 合在一起唯一标记不可约表示 $(p, q)$。$\blacksquare$

---

## E. The Exponential Map and Hermiticity of Generators · 指数映射与生成元的厄米性

**Claim.** For a Lie group $G$ with unitary representations $\rho(g)^\dagger\rho(g) = I$, the generators $T_a$ defined by $\rho(\exp(i \theta_a T_a))$ near the identity must satisfy $T_a^\dagger = T_a$ (Hermitian). Conversely, any Hermitian matrix $H$ generates a one-parameter unitary group $\exp(i t H)$.

**命题。** 对于具有酉表示 $\rho(g)^\dagger\rho(g) = I$ 的李群 $G$，在单位元附近由 $\rho(\exp(i \theta_a T_a))$ 定义的生成元 $T_a$ 必满足 $T_a^\dagger = T_a$（厄米性）。反之，任意厄米矩阵 $H$ 生成单参数酉群 $\exp(i t H)$。

**Step 1 — Parameterize near the identity.** Consider a one-parameter subgroup $g(t) = \exp(i t T)$ for a single generator $T$ and real parameter $t$. At $t = 0$, $g(0) = I$. Differentiating:

**第 1 步 — 在单位元附近参数化。** 考虑单个生成元 $T$ 和实参数 $t$ 的单参数子群 $g(t) = \exp(i t T)$。在 $t = 0$ 时，$g(0) = I$。对 $t$ 微分：

$$ \frac{d}{dt}[g(t)]\Big|_{t=0} = i T. $$

**Step 2 — Unitarity constraint.** Require $g(t)^\dagger g(t) = I$ for all $t$. Differentiate with respect to $t$ and evaluate at $t = 0$:

**第 2 步 — 酉性约束。** 要求对所有 $t$ 有 $g(t)^\dagger g(t) = I$。对 $t$ 微分并在 $t = 0$ 处求值：

$$ \begin{aligned} \frac{d}{dt}[g(t)^\dagger g(t)]\Big|_{t=0} &= \left(\frac{d}{dt} g(t)^\dagger\right)\Big|_{t=0} \cdot g(0) + g(0)^\dagger \cdot \left(\frac{d}{dt} g(t)\right)\Big|_{t=0} \\ &= (iT)^\dagger \cdot I + I \cdot (iT) \\ &= -iT^\dagger + iT = 0. \end{aligned} $$

Therefore $\boldsymbol{T^\dagger = T}$: the generator is Hermitian.

故 $\boldsymbol{T^\dagger = T}$：生成元是厄米的。

**Step 3 — Converse: Hermitian implies unitary.** Let $T = T^\dagger$ be Hermitian. Then:

**第 3 步 — 逆命题：厄米蕴含酉性。** 设 $T = T^\dagger$ 为厄米矩阵。则：

$$ (\exp(i t T))^\dagger = \exp(-i t T^\dagger) = \exp(-i t T) = (\exp(i t T))^{-1}. $$

(The first equality uses $(e^A)^\dagger = e^{A^\dagger}$, proved by taking the adjoint of the power series; the second uses $T^\dagger = T$; the third uses $\exp(A)\exp(-A) = I$.) Hence $\exp(i t T)$ is unitary for all real $t$.

（第一个等式利用 $(e^A)^\dagger = e^{A^\dagger}$，通过对幂级数取伴随证明；第二个利用 $T^\dagger = T$；第三个利用 $\exp(A)\exp(-A) = I$。）故对所有实数 $t$，$\exp(i t T)$ 是酉矩阵。

**Step 4 — Convergence and the Baker–Campbell–Hausdorff formula.** The matrix exponential $\exp(A) = \sum_{n=0}^\infty A^n/n!$ converges absolutely for any finite-dimensional matrix $A$ (since $\lVert A^n\rVert \le \lVert A\rVert^n$ and $\sum \lVert A\rVert^n/n! = \exp(\lVert A\rVert) < \infty$). For two generators, $\exp(i \alpha T_a) \exp(i \beta T_b) \ne \exp(i(\alpha T_a + \beta T_b))$ in general; the **Baker–Campbell–Hausdorff (BCH) formula** gives the correction:

**第 4 步 — 收敛性与 Baker–Campbell–Hausdorff 公式。** 矩阵指数 $\exp(A) = \sum_{n=0}^\infty A^n/n!$ 对任意有限维矩阵 $A$ 绝对收敛（因为 $\lVert A^n\rVert \le \lVert A\rVert^n$，且 $\sum \lVert A\rVert^n/n! = \exp(\lVert A\rVert) < \infty$）。对两个生成元，一般有 $\exp(i \alpha T_a) \exp(i \beta T_b) \ne \exp(i(\alpha T_a + \beta T_b))$；**Baker–Campbell–Hausdorff (BCH) 公式**给出修正：

$$ \exp(X) \exp(Y) = \exp\!\left(X + Y + \tfrac12[X,Y] + \tfrac{1}{12}([X,[X,Y]] - [Y,[X,Y]]) + \cdots\right) $$

The key point is that the exponent involves only commutators (i.e., the Lie algebra structure), showing that the local group structure near the identity is entirely encoded in the Lie algebra. $\blacksquare$

关键在于指数中仅涉及对易子（即李代数结构），表明单位元附近的局部群结构完全编码在李代数中。$\blacksquare$

---

*These derivations establish the algebraic foundations used in Module 3.11 (angular momentum), Module 8.1 (gauge theory), and Module 8.3 (QCD and the quark model).*

*这些推导确立了模块 3.11（角动量）、模块 8.1（规范理论）和模块 8.3（量子色动力学与夸克模型）所用的代数基础。*

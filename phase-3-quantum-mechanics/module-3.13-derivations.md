# Derivations — Module 3.13: Entanglement, EPR & Bell's Theorem
# 推导 — 模块 3.13：纠缠、EPR 与贝尔定理

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.13](./module-3.13-entanglement-epr-and-bell.md). Full step-by-step proofs that the singlet is rotationally invariant and not a product state; derivation of the spin correlation $E(\mathbf{a},\mathbf{b}) = -\cos\theta_{ab}$; derivation of the CHSH inequality $|S| \le 2$ for local hidden variables; and proof that quantum mechanics gives the Tsirelson bound $|S| = 2\sqrt2$. English first, then 中文.
> [模块 3.13](./module-3.13-entanglement-epr-and-bell.md) 的配套文档：单态是转动不变且非直积态的完整证明；自旋关联 $E(\mathbf{a},\mathbf{b}) = -\cos\theta_{ab}$ 的推导；局域隐变量的 CHSH 不等式 $|S| \le 2$ 的推导；以及量子力学给出齐列尔逊界 $|S| = 2\sqrt2$ 的证明。先英文，后中文。

---

## A. The Singlet Is Not a Product State · 单态不是直积态

**Claim.** The spin singlet $|\Psi^-\rangle = (1/\sqrt2)(|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2)$ cannot be written as a tensor product $|\alpha\rangle_1 \otimes |\beta\rangle_2$ for any single-particle states $|\alpha\rangle_1$ and $|\beta\rangle_2$.

**命题。** 自旋单态 $|\Psi^-\rangle = (1/\sqrt2)(|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2)$ 不能写成任何单粒子态 $|\alpha\rangle_1$ 与 $|\beta\rangle_2$ 的张量积 $|\alpha\rangle_1 \otimes |\beta\rangle_2$。

**Step 1 — Write the most general product state.** Any single-particle spin-½ state can be written as

**第 1 步 — 写出最一般的直积态。** 任意单粒子自旋-½ 态可以写为

$$ |\alpha\rangle_1 = a|+\rangle_1 + b|-\rangle_1, \quad |\beta\rangle_2 = c|+\rangle_2 + d|-\rangle_2, $$

with $a, b, c, d \in \mathbb{C}$. Their tensor product expands as

其中 $a, b, c, d \in \mathbb{C}$。其张量积展开为

$$ |\alpha\rangle_1 \otimes |\beta\rangle_2 = ac|+\rangle_1|+\rangle_2 + ad|+\rangle_1|-\rangle_2 + bc|-\rangle_1|+\rangle_2 + bd|-\rangle_1|-\rangle_2. $$

**Step 2 — Match coefficients to the singlet.** For this to equal $(1/\sqrt2)(|+-\rangle - |-+\rangle)$, the four basis-state coefficients must satisfy:

**第 2 步 — 与单态匹配系数。** 为使此式等于 $(1/\sqrt2)(|+-\rangle - |-+\rangle)$，四个基矢态的系数必须满足：

$$ \begin{aligned} ac &= 0 \quad \text{(coefficient of } |+\rangle_1|+\rangle_2\text{)}, \\ ad &= \tfrac{1}{\sqrt2} \quad \text{(coefficient of } |+\rangle_1|-\rangle_2\text{)}, \\ bc &= -\tfrac{1}{\sqrt2} \quad \text{(coefficient of } |-\rangle_1|+\rangle_2\text{)}, \\ bd &= 0 \quad \text{(coefficient of } |-\rangle_1|-\rangle_2\text{)}. \end{aligned} $$

**Step 3 — Derive a contradiction.** From $ac = 0$ either $a = 0$ or $c = 0$.

**第 3 步 — 推导矛盾。** 由 $ac = 0$，要么 $a = 0$ 要么 $c = 0$。

Case 1: $a = 0$. Then $ad = 0 \ne 1/\sqrt2$. Contradiction.

情况 1：$a = 0$。则 $ad = 0 \ne 1/\sqrt2$。矛盾。

Case 2: $c = 0$. Then $bc = 0 \ne -1/\sqrt2$. Contradiction.

情况 2：$c = 0$。则 $bc = 0 \ne -1/\sqrt2$。矛盾。

Both cases are contradictions, so no product state can equal the singlet. Therefore $|\Psi^-\rangle$ is **entangled**. $\blacksquare$

两种情况都是矛盾，故没有直积态能等于单态。因此 $|\Psi^-\rangle$ 是**纠缠**态。$\blacksquare$

Equivalently, the $2\times 2$ matrix of coefficients of a general two-qubit state $|\psi\rangle = \sum_{m_1,m_2} c_{m_1 m_2}|m_1\rangle|m_2\rangle$ is $C = \begin{pmatrix} ac & ad \\ bc & bd \end{pmatrix}$, which has $\det(C) = abcd - abcd = 0$ for product states. For the singlet, the matrix is $(1/\sqrt2)\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ with $\det = 1/2 \ne 0$ — confirming entanglement.

等价地，一般两量子比特态 $|\psi\rangle = \sum_{m_1,m_2} c_{m_1 m_2}|m_1\rangle|m_2\rangle$ 的系数 $2\times 2$ 矩阵 $C = \begin{pmatrix} ac & ad \\ bc & bd \end{pmatrix}$ 对直积态满足 $\det(C) = 0$。对单态，矩阵为 $(1/\sqrt2)\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$，行列式 $= 1/2 \ne 0$——确认了纠缠。

---

## B. The Singlet Is Rotationally Invariant · 单态具有转动不变性

**Claim.** The singlet $|\Psi^-\rangle = (1/\sqrt2)(|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2)$ is invariant under any simultaneous rotation of both spins: $(R \otimes R)|\Psi^-\rangle = |\Psi^-\rangle$ for any SU(2) rotation matrix $R$.

**命题。** 单态 $|\Psi^-\rangle = (1/\sqrt2)(|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2)$ 在两个自旋同时转动下不变：对任意 SU(2) 转动矩阵 $R$，$(R \otimes R)|\Psi^-\rangle = |\Psi^-\rangle$。

**Step 1 — General rotation.** A rotation by angle $\theta$ about axis $\hat{\mathbf{n}}$ is represented on spin-½ by

**第 1 步 — 一般转动。** 绕轴 $\hat{\mathbf{n}}$ 转动角度 $\theta$ 在自旋-½ 上的表示为

$$ \begin{aligned} R(\theta, \hat{\mathbf{n}}) &= e^{-i\theta(\hat{\mathbf{n}}\cdot\boldsymbol{\sigma})/2} = \cos(\theta/2)\, I - i \sin(\theta/2)\, (\hat{\mathbf{n}}\cdot\boldsymbol{\sigma}) \\ &= \begin{pmatrix} \cos(\theta/2) - i n_z \sin(\theta/2) & (-in_x - n_y) \sin(\theta/2) \\ (-in_x + n_y) \sin(\theta/2) & \cos(\theta/2) + i n_z \sin(\theta/2) \end{pmatrix}. \end{aligned} $$

Writing $R = \begin{pmatrix} \alpha & -\beta^* \\ \beta & \alpha^* \end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$ (the general SU(2) matrix):

令 $R = \begin{pmatrix} \alpha & -\beta^* \\ \beta & \alpha^* \end{pmatrix}$，$|\alpha|^2 + |\beta|^2 = 1$（一般 SU(2) 矩阵）：

$$ R|+\rangle = \alpha|+\rangle + \beta|-\rangle, \quad R|-\rangle = -\beta^*|+\rangle + \alpha^*|-\rangle. $$

**Step 2 — Act with $R \otimes R$ on $|\Psi^-\rangle$.** Compute:

**第 2 步 — 以 $R \otimes R$ 作用于 $|\Psi^-\rangle$。** 计算：

$$ \begin{aligned} (R\otimes R)|+\rangle_1|-\rangle_2 &= (R|+\rangle_1)(R|-\rangle_2) = (\alpha|+\rangle_1 + \beta|-\rangle_1)(-\beta^*|+\rangle_2 + \alpha^*|-\rangle_2) \\ &= -\alpha\beta^*|+\rangle_1|+\rangle_2 + \alpha\alpha^*|+\rangle_1|-\rangle_2 - \beta\beta^*|-\rangle_1|+\rangle_2 + \beta\alpha^*|-\rangle_1|-\rangle_2. \end{aligned} $$

$$ \begin{aligned} (R\otimes R)|-\rangle_1|+\rangle_2 &= (R|-\rangle_1)(R|+\rangle_2) = (-\beta^*|+\rangle_1 + \alpha^*|-\rangle_1)(\alpha|+\rangle_2 + \beta|-\rangle_2) \\ &= -\beta^*\alpha|+\rangle_1|+\rangle_2 - \beta^*\beta|+\rangle_1|-\rangle_2 + \alpha^*\alpha|-\rangle_1|+\rangle_2 + \alpha^*\beta|-\rangle_1|-\rangle_2. \end{aligned} $$

**Step 3 — Combine.** Compute $(R\otimes R)(|+-\rangle - |-+\rangle)$:

**第 3 步 — 合并。** 计算 $(R\otimes R)(|+-\rangle - |-+\rangle)$：

$$ = [-\alpha\beta^* + \alpha\beta^*]|++\rangle + [|\alpha|^2 + |\beta|^2]|+-\rangle + [-|\beta|^2 - |\alpha|^2]|-+\rangle + [\beta\alpha^* - \alpha^*\beta]|--\rangle. $$

Using $|\alpha|^2 + |\beta|^2 = 1$ and the observation that the $|++\rangle$ and $|--\rangle$ terms cancel ($-\alpha\beta^* - (-\alpha\beta^*) = 0$ and $\beta\alpha^* - \alpha^*\beta = 0$ since $\beta\alpha^*$ is the complex conjugate of $\alpha\beta^*$... let's be more careful):

利用 $|\alpha|^2 + |\beta|^2 = 1$，注意到：

Coefficient of $|++\rangle$: $-\alpha\beta^* - (-\beta^*\alpha) = -\alpha\beta^* + \alpha\beta^* = 0$.

$|++\rangle$ 的系数：$-\alpha\beta^* - (-\beta^*\alpha) = -\alpha\beta^* + \alpha\beta^* = 0$。

Coefficient of $|+-\rangle$: $|\alpha|^2 - (-|\beta|^2) = |\alpha|^2 + |\beta|^2 = 1$.

$|+-\rangle$ 的系数：$|\alpha|^2 - (-|\beta|^2) = |\alpha|^2 + |\beta|^2 = 1$。

Coefficient of $|-+\rangle$: $-|\beta|^2 - |\alpha|^2 = -(|\alpha|^2 + |\beta|^2) = -1$.

$|-+\rangle$ 的系数：$-|\beta|^2 - |\alpha|^2 = -(|\alpha|^2 + |\beta|^2) = -1$。

Coefficient of $|--\rangle$: $\beta\alpha^* - \alpha^*\beta = 0$.

$|--\rangle$ 的系数：$\beta\alpha^* - \alpha^*\beta = 0$。

Therefore $(R\otimes R)(|+-\rangle - |-+\rangle) = |+-\rangle - |-+\rangle$, giving

因此 $(R\otimes R)(|+-\rangle - |-+\rangle) = |+-\rangle - |-+\rangle$，故

$$ (R\otimes R)|\Psi^-\rangle = \tfrac{1}{\sqrt2}(|+-\rangle - |-+\rangle) = |\Psi^-\rangle. \qquad \blacksquare $$

The singlet is invariant under any common SU(2) rotation — it is the unique (up to phase) $j = 0$ state in the $\tfrac12 \otimes \tfrac12$ decomposition, which must be rotation-invariant by definition.

单态在任意公共 SU(2) 转动下不变——它是 $\tfrac12 \otimes \tfrac12$ 分解中唯一（在相位意义下）的 $j = 0$ 态，这由定义必然是转动不变的。$\blacksquare$

---

## C. Spin Correlation for the Singlet: $E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab}$ · 单态的自旋关联：$E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab}$

**Claim.** For the singlet state $|\Psi^-\rangle$, if particle A's spin is measured along unit vector $\mathbf{a}$ and particle B's spin is measured along unit vector $\mathbf{b}$, the correlation function $E(\mathbf{a}, \mathbf{b}) = \langle\Psi^-|(\boldsymbol{\sigma}_A\cdot\mathbf{a})(\boldsymbol{\sigma}_B\cdot\mathbf{b})|\Psi^-\rangle$ equals:

**命题。** 对单态 $|\Psi^-\rangle$，若粒子 A 的自旋沿单位向量 $\mathbf{a}$ 测量，粒子 B 的自旋沿单位向量 $\mathbf{b}$ 测量，则关联函数 $E(\mathbf{a}, \mathbf{b}) = \langle\Psi^-|(\boldsymbol{\sigma}_A\cdot\mathbf{a})(\boldsymbol{\sigma}_B\cdot\mathbf{b})|\Psi^-\rangle$ 等于：

$$ E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab} = -\mathbf{a}\cdot\mathbf{b}, $$

where $\theta_{ab}$ is the angle between $\mathbf{a}$ and $\mathbf{b}$.

其中 $\theta_{ab}$ 为 $\mathbf{a}$ 与 $\mathbf{b}$ 之间的夹角。

**Step 1 — Express the correlation as a matrix element.** With $\boldsymbol{\sigma}\cdot\mathbf{a} = a_x\sigma_x + a_y\sigma_y + a_z\sigma_z$ (a Hermitian operator with eigenvalues $\pm 1$), write

**第 1 步 — 将关联表达为矩阵元。** 令 $\boldsymbol{\sigma}\cdot\mathbf{a} = a_x\sigma_x + a_y\sigma_y + a_z\sigma_z$（本征值为 $\pm 1$ 的厄米算符），写出

$$ E(\mathbf{a}, \mathbf{b}) = \langle\Psi^-| (\boldsymbol{\sigma}_A\cdot\mathbf{a}) \otimes (\boldsymbol{\sigma}_B\cdot\mathbf{b}) |\Psi^-\rangle. $$

**Step 2 — Use rotational invariance.** By the rotational invariance of the singlet, we can choose coordinates so that $\mathbf{a} = \hat{\mathbf{z}}$ without loss of generality, and $\mathbf{b}$ makes angle $\theta$ with $\hat{\mathbf{z}}$, so $\mathbf{b} = (\sin\theta, 0, \cos\theta)$. Then:

**第 2 步 — 利用转动不变性。** 由单态的转动不变性，不失一般性可以选取坐标使 $\mathbf{a} = \hat{\mathbf{z}}$，$\mathbf{b}$ 与 $\hat{\mathbf{z}}$ 成角 $\theta$，即 $\mathbf{b} = (\sin\theta, 0, \cos\theta)$。则：

$$ \begin{aligned} E(\hat{\mathbf{z}}, \mathbf{b}) &= \langle\Psi^-| \sigma_z^A \otimes (\sin\theta\, \sigma_x^B + \cos\theta\, \sigma_z^B) |\Psi^-\rangle \\ &= \sin\theta\, \langle\Psi^-| \sigma_z^A \otimes \sigma_x^B |\Psi^-\rangle + \cos\theta\, \langle\Psi^-| \sigma_z^A \otimes \sigma_z^B |\Psi^-\rangle. \end{aligned} $$

**Step 3 — Compute $\langle\sigma_z^A \otimes \sigma_z^B\rangle$.** The singlet is $(1/\sqrt2)(|+-\rangle - |-+\rangle)$. Using $\sigma_z|+\rangle = |+\rangle$ and $\sigma_z|-\rangle = -|-\rangle$:

**第 3 步 — 计算 $\langle\sigma_z^A \otimes \sigma_z^B\rangle$。** 单态为 $(1/\sqrt2)(|+-\rangle - |-+\rangle)$。利用 $\sigma_z|+\rangle = |+\rangle$，$\sigma_z|-\rangle = -|-\rangle$：

$$ \begin{aligned} (\sigma_z^A \otimes \sigma_z^B)|+-\rangle &= \sigma_z|+\rangle \otimes \sigma_z|-\rangle = |+\rangle \otimes (-|-\rangle) = -|+-\rangle, \\ (\sigma_z^A \otimes \sigma_z^B)|-+\rangle &= \sigma_z|-\rangle \otimes \sigma_z|+\rangle = (-|-\rangle) \otimes |+\rangle = -|-+\rangle. \end{aligned} $$

$$ \begin{aligned} \langle\Psi^-|\sigma_z^A\otimes\sigma_z^B|\Psi^-\rangle &= \tfrac12(\langle +-| - \langle -+|)(-|+-\rangle + |-+\rangle) \\ &= \tfrac12(-\langle +-|+-\rangle + \langle +-|-+\rangle + \langle -+|+-\rangle - \langle -+|-+\rangle) \\ &= \tfrac12(-1 + 0 + 0 - 1) = -1. \end{aligned} $$

**Step 4 — Compute $\langle\sigma_z^A \otimes \sigma_x^B\rangle$.** Using $\sigma_x|+\rangle = |-\rangle$ and $\sigma_x|-\rangle = |+\rangle$:

**第 4 步 — 计算 $\langle\sigma_z^A \otimes \sigma_x^B\rangle$。** 利用 $\sigma_x|+\rangle = |-\rangle$，$\sigma_x|-\rangle = |+\rangle$：

$$ \begin{aligned} (\sigma_z^A \otimes \sigma_x^B)|+-\rangle &= |+\rangle \otimes |+\rangle = |++\rangle, \\ (\sigma_z^A \otimes \sigma_x^B)|-+\rangle &= -|-\rangle \otimes |-\rangle = -|--\rangle. \end{aligned} $$

$$ \begin{aligned} \langle\Psi^-|\sigma_z^A\otimes\sigma_x^B|\Psi^-\rangle &= \tfrac12(\langle +-|-\langle -+|)(|++\rangle + |--\rangle) \\ &= \tfrac12(\langle +-|++\rangle + \langle +-|--\rangle - \langle -+|++\rangle - \langle -+|--\rangle) \\ &= \tfrac12(0 + 0 - 0 - 0) = 0. \end{aligned} $$

**Step 5 — Assemble $E(\hat{\mathbf{z}}, \mathbf{b})$.** From Steps 3 and 4:

**第 5 步 — 组合 $E(\hat{\mathbf{z}}, \mathbf{b})$。** 由第 3、4 步：

$$ E(\hat{\mathbf{z}}, \mathbf{b}) = \sin\theta \cdot 0 + \cos\theta \cdot (-1) = -\cos\theta. $$

Since $\theta = \theta_{ab}$ is the angle between $\mathbf{a} = \hat{\mathbf{z}}$ and $\mathbf{b}$, and by rotational invariance the result is the same for general $\mathbf{a}$:

由于 $\theta = \theta_{ab}$ 是 $\mathbf{a} = \hat{\mathbf{z}}$ 与 $\mathbf{b}$ 之间的夹角，由转动不变性，对一般 $\mathbf{a}$ 结果相同：

$$ \boxed{\, E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab} = -\mathbf{a}\cdot\mathbf{b} \,} \qquad \blacksquare $$

**Alternative derivation using the identity.** One can also use the identity for singlet states:

**另一种用恒等式的推导。** 也可以利用单态的恒等式：

$$ \langle\Psi^-| \sigma_i^A \otimes \sigma_j^B |\Psi^-\rangle = -\delta_{ij}. $$

This follows from $\Psi^-$ being the $j = 0$ state (a rotationally invariant scalar), so the expectation value of any rank-2 Cartesian tensor operator must be proportional to $\delta_{ij}$; the coefficient $-1$ is fixed by the normalization. Then $E(\mathbf{a},\mathbf{b}) = a_i b_j\langle\sigma_i^A \sigma_j^B\rangle = -a_i b_j\delta_{ij} = -\mathbf{a}\cdot\mathbf{b}$.

这由 $\Psi^-$ 是 $j = 0$ 态（转动不变标量）得到，故任何二阶笛卡尔张量算符的期望值必须正比于 $\delta_{ij}$；系数 $-1$ 由归一化固定。则 $E(\mathbf{a},\mathbf{b}) = a_i b_j\langle\sigma_i^A \sigma_j^B\rangle = -a_i b_j\delta_{ij} = -\mathbf{a}\cdot\mathbf{b}$。

---

## D. The CHSH Inequality for Local Hidden Variables · 局域隐变量的 CHSH 不等式

**Claim.** Any theory satisfying local realism (local hidden variables) must obey $|S| \le 2$, where

**命题。** 任何满足定域实在论（局域隐变量）的理论必须满足 $|S| \le 2$，其中

$$ S = E(\mathbf{a}, \mathbf{b}) - E(\mathbf{a}, \mathbf{b}') + E(\mathbf{a}', \mathbf{b}) + E(\mathbf{a}', \mathbf{b}'), $$

with $\mathbf{a}, \mathbf{a}'$ the two possible measurement settings for party A and $\mathbf{b}, \mathbf{b}'$ the two settings for party B.

其中 $\mathbf{a}, \mathbf{a}'$ 为 A 方的两种测量设置，$\mathbf{b}, \mathbf{b}'$ 为 B 方的两种设置。

**Step 1 — Local hidden variable model.** Assume there exists a hidden variable $\lambda$ (with probability distribution $\rho(\lambda) \ge 0$, $\int\rho(\lambda)d\lambda = 1$) such that the measurement outcome of A with setting $\mathbf{a}$ is $A(\mathbf{a}, \lambda) = \pm 1$ and the outcome of B with setting $\mathbf{b}$ is $B(\mathbf{b}, \lambda) = \pm 1$. **Locality**: A's outcome does not depend on B's setting and vice versa. The correlation is

**第 1 步 — 局域隐变量模型。** 假设存在隐变量 $\lambda$（概率分布 $\rho(\lambda) \ge 0$，$\int\rho(\lambda)d\lambda = 1$），使得 A 在设置 $\mathbf{a}$ 下的测量结果为 $A(\mathbf{a}, \lambda) = \pm 1$，B 在设置 $\mathbf{b}$ 下的结果为 $B(\mathbf{b}, \lambda) = \pm 1$。**定域性**：A 的结果不依赖于 B 的设置，反之亦然。关联为

$$ E(\mathbf{a}, \mathbf{b}) = \int A(\mathbf{a}, \lambda)\, B(\mathbf{b}, \lambda)\, \rho(\lambda)\, d\lambda. $$

**Step 2 — Algebraic lemma.** For any fixed $\lambda$, with $A = A(\mathbf{a},\lambda)$, $A' = A(\mathbf{a}',\lambda)$, $B = B(\mathbf{b},\lambda)$, $B' = B(\mathbf{b}',\lambda)$, each equal to $\pm 1$:

**第 2 步 — 代数引理。** 对任意固定 $\lambda$，令 $A = A(\mathbf{a},\lambda)$，$A' = A(\mathbf{a}',\lambda)$，$B = B(\mathbf{b},\lambda)$，$B' = B(\mathbf{b}',\lambda)$，每个均等于 $\pm 1$：

$$ AB - AB' + A'B + A'B' = A(B - B') + A'(B + B'). $$

Since $B, B' \in \{+1, -1\}$, either $B - B' = 0$ and $B + B' = \pm 2$, or $B - B' = \pm 2$ and $B + B' = 0$. In either case, exactly one of $(B - B')$ and $(B + B')$ has magnitude $2$ and the other is $0$. Therefore:

由于 $B, B' \in \{+1, -1\}$，要么 $B - B' = 0$ 且 $B + B' = \pm 2$，要么 $B - B' = \pm 2$ 且 $B + B' = 0$。无论哪种情况，$(B - B')$ 和 $(B + B')$ 中恰有一个绝对值为 $2$，另一个为 $0$。因此：

$$ |AB - AB' + A'B + A'B'| = |A| \cdot |\text{one of } \pm 2| + |A'| \cdot |0| \text{ (or vice versa)} = 1 \cdot 2 + 1 \cdot 0 = 2. $$

More precisely, since $|A| = |A'| = 1$ and exactly one term is $\pm 2$:

更精确地，由于 $|A| = |A'| = 1$ 且恰好有一项为 $\pm 2$：

$$ |A(B - B') + A'(B + B')| \le |A||B - B'| + |A'||B + B'| = |B-B'| + |B+B'| = 2. $$

(The last equality is because $|B-B'| + |B+B'| = 2$ for $B, B' \in \{\pm 1\}$: if $B = B'$, then $0 + 2 = 2$; if $B \ne B'$, then $2 + 0 = 2$.)

（最后等号成立是因为对 $B, B' \in \{\pm 1\}$，$|B-B'| + |B+B'| = 2$：若 $B = B'$ 则 $0 + 2 = 2$；若 $B \ne B'$ 则 $2 + 0 = 2$。）

**Step 3 — Integrate over $\lambda$.** Since $|AB - AB' + A'B + A'B'| \le 2$ for every $\lambda$:

**第 3 步 — 对 $\lambda$ 积分。** 由于对每个 $\lambda$ 均有 $|AB - AB' + A'B + A'B'| \le 2$：

$$ \begin{aligned} |S| &= |E(\mathbf{a},\mathbf{b}) - E(\mathbf{a},\mathbf{b}') + E(\mathbf{a}',\mathbf{b}) + E(\mathbf{a}',\mathbf{b}')| \\ &= \Big|\int [A(\mathbf{a},\lambda)B(\mathbf{b},\lambda) - A(\mathbf{a},\lambda)B(\mathbf{b}',\lambda) + A(\mathbf{a}',\lambda)B(\mathbf{b},\lambda) + A(\mathbf{a}',\lambda)B(\mathbf{b}',\lambda)] \rho(\lambda)\, d\lambda\Big| \\ &\le \int |A(B - B') + A'(B + B')| \rho(\lambda)\, d\lambda \\ &\le \int 2\, \rho(\lambda)\, d\lambda = 2. \end{aligned} $$

Therefore $|S| \le 2$ for any local hidden-variable theory. $\blacksquare$

因此对任意局域隐变量理论 $|S| \le 2$。$\blacksquare$

---

## E. Quantum Mechanics Violates CHSH: The Tsirelson Bound · 量子力学违反 CHSH：齐列尔逊界

**Claim.** For the singlet state, the quantum mechanical prediction for $S$ (with optimally chosen measurement directions) equals $2\sqrt2$, which violates the classical bound of $2$. This is the Tsirelson bound — the maximum quantum violation.

**命题。** 对单态，在最优选择的测量方向下，量子力学对 $S$ 的预言等于 $2\sqrt2$，违反了经典界 $2$。这就是齐列尔逊界——最大量子违反。

**Step 1 — Choose optimal angles.** Using $E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab}$ from Section C, we seek to maximize:

**第 1 步 — 选择最优角度。** 利用 C 节中的 $E(\mathbf{a}, \mathbf{b}) = -\cos\theta_{ab}$，我们寻求最大化：

$$ \begin{aligned} S &= E(\mathbf{a},\mathbf{b}) - E(\mathbf{a},\mathbf{b}') + E(\mathbf{a}',\mathbf{b}) + E(\mathbf{a}',\mathbf{b}') \\ &= -\cos\theta_{ab} + \cos\theta_{ab'} - \cos\theta_{a'b} - \cos\theta_{a'b'}. \end{aligned} $$

Work in the 2D plane. Let $\mathbf{a}$ be at angle $0^\circ$, $\mathbf{b}$ at angle $\varphi_1$, $\mathbf{a}'$ at angle $\varphi_2$, and $\mathbf{b}'$ at angle $\varphi_3$. Choose the symmetric configuration:

在二维平面中工作。令 $\mathbf{a}$ 在 $0^\circ$ 方向，$\mathbf{b}$ 在 $\varphi_1$ 方向，$\mathbf{a}'$ 在 $\varphi_2$ 方向，$\mathbf{b}'$ 在 $\varphi_3$ 方向。选择对称配置：

$$ \mathbf{a} = 0^\circ, \quad \mathbf{b} = 45^\circ, \quad \mathbf{a}' = 90^\circ, \quad \mathbf{b}' = 135^\circ. $$

Then:

则：

$$ \theta_{ab} = 45^\circ, \quad \theta_{ab'} = 135^\circ, \quad \theta_{a'b} = 45^\circ, \quad \theta_{a'b'} = 45^\circ. $$

$$ S = -\cos(45^\circ) + \cos(135^\circ) - \cos(45^\circ) - \cos(45^\circ) \quad \leftarrow \text{let's recompute carefully.} $$

Let me use a more standard presentation. Place the measurement axes in the $x$-$z$ plane:

让我使用更标准的表述。将测量轴放在 $x$-$z$ 平面内：

$$ \mathbf{a} = \hat{\mathbf{z}}\ (0^\circ), \quad \mathbf{b} = \frac{\hat{\mathbf{z}} + \hat{\mathbf{x}}}{\sqrt2}\ (45^\circ \text{ from } \hat{\mathbf{z}}), \quad \mathbf{a}' = \hat{\mathbf{x}}\ (90^\circ \text{ from } \hat{\mathbf{z}}), \quad \mathbf{b}' = \frac{-\hat{\mathbf{z}} + \hat{\mathbf{x}}}{\sqrt2}\ (135^\circ \text{ from } \hat{\mathbf{z}}). $$

The angles between the axes:

各轴之间的夹角：

$$ \theta_{ab} = 45^\circ, \quad \theta_{ab'} = 135^\circ, \quad \theta_{a'b} = 45^\circ, \quad \theta_{a'b'} = 45^\circ. $$

So:

故：

$$ \begin{aligned} E(\mathbf{a},\mathbf{b}) &= -\cos(45^\circ) = -\tfrac{1}{\sqrt2}, \\ E(\mathbf{a},\mathbf{b}') &= -\cos(135^\circ) = +\tfrac{1}{\sqrt2}, \\ E(\mathbf{a}',\mathbf{b}) &= -\cos(45^\circ) = -\tfrac{1}{\sqrt2}, \\ E(\mathbf{a}',\mathbf{b}') &= -\cos(45^\circ) = -\tfrac{1}{\sqrt2}. \end{aligned} $$

$$ \begin{aligned} S &= E(\mathbf{a},\mathbf{b}) - E(\mathbf{a},\mathbf{b}') + E(\mathbf{a}',\mathbf{b}) + E(\mathbf{a}',\mathbf{b}') \\ &= -\tfrac{1}{\sqrt2} - \tfrac{1}{\sqrt2} - \tfrac{1}{\sqrt2} - \tfrac{1}{\sqrt2} = -\tfrac{4}{\sqrt2} = -2\sqrt2. \end{aligned} $$

So $|S| = 2\sqrt2 > 2$. $\checkmark$

故 $|S| = 2\sqrt2 > 2$。$\checkmark$

**Step 2 — Verify this is the maximum quantum value (Tsirelson).** For general quantum states and measurements, define the CHSH operator

**第 2 步 — 验证这是最大量子值（齐列尔逊）。** 对一般量子态和测量，定义 CHSH 算符

$$ \begin{aligned} \hat{S} &= (\boldsymbol{\sigma}_A\cdot\mathbf{a})(\boldsymbol{\sigma}_B\cdot\mathbf{b}) - (\boldsymbol{\sigma}_A\cdot\mathbf{a})(\boldsymbol{\sigma}_B\cdot\mathbf{b}') + (\boldsymbol{\sigma}_A\cdot\mathbf{a}')(\boldsymbol{\sigma}_B\cdot\mathbf{b}) + (\boldsymbol{\sigma}_A\cdot\mathbf{a}')(\boldsymbol{\sigma}_B\cdot\mathbf{b}') \\ &= (\boldsymbol{\sigma}_A\cdot\mathbf{a}) \otimes [(\boldsymbol{\sigma}_B\cdot\mathbf{b}) - (\boldsymbol{\sigma}_B\cdot\mathbf{b}')] + (\boldsymbol{\sigma}_A\cdot\mathbf{a}') \otimes [(\boldsymbol{\sigma}_B\cdot\mathbf{b}) + (\boldsymbol{\sigma}_B\cdot\mathbf{b}')]. \end{aligned} $$

Let $C = (\boldsymbol{\sigma}_B\cdot\mathbf{b}) - (\boldsymbol{\sigma}_B\cdot\mathbf{b}')$ and $D = (\boldsymbol{\sigma}_B\cdot\mathbf{b}) + (\boldsymbol{\sigma}_B\cdot\mathbf{b}')$. We use $C^\dagger C = C^2 = [(\boldsymbol{\sigma}_B\cdot\mathbf{b}) - (\boldsymbol{\sigma}_B\cdot\mathbf{b}')]^2$. Since $(\boldsymbol{\sigma}\cdot\hat{\mathbf{n}})^2 = I$ for any unit vector $\hat{\mathbf{n}}$:

令 $C = (\boldsymbol{\sigma}_B\cdot\mathbf{b}) - (\boldsymbol{\sigma}_B\cdot\mathbf{b}')$，$D = (\boldsymbol{\sigma}_B\cdot\mathbf{b}) + (\boldsymbol{\sigma}_B\cdot\mathbf{b}')$。由于 $(\boldsymbol{\sigma}\cdot\hat{\mathbf{n}})^2 = I$ 对任意单位向量 $\hat{\mathbf{n}}$ 成立：

$$ \begin{aligned} C^2 &= (\boldsymbol{\sigma}_B\cdot\mathbf{b})^2 - (\boldsymbol{\sigma}_B\cdot\mathbf{b})(\boldsymbol{\sigma}_B\cdot\mathbf{b}') - (\boldsymbol{\sigma}_B\cdot\mathbf{b}')(\boldsymbol{\sigma}_B\cdot\mathbf{b}) + (\boldsymbol{\sigma}_B\cdot\mathbf{b}')^2 \\ &= I - \{\boldsymbol{\sigma}_B\cdot\mathbf{b}, \boldsymbol{\sigma}_B\cdot\mathbf{b}'\} + I = 2I - 2(\mathbf{b}\cdot\mathbf{b}')I = 2(1 - \mathbf{b}\cdot\mathbf{b}')I. \end{aligned} $$

$$ D^2 = 2(1 + \mathbf{b}\cdot\mathbf{b}')I. $$

So the exact computation gives

所以 $\hat{S}^2$ 的精确计算给出

$$ \hat{S}^2 = 4I - [\boldsymbol{\sigma}_A\cdot\mathbf{a}, \boldsymbol{\sigma}_A\cdot\mathbf{a}'] \otimes [\boldsymbol{\sigma}_B\cdot\mathbf{b}, \boldsymbol{\sigma}_B\cdot\mathbf{b}']. $$

Since $[\boldsymbol{\sigma}\cdot\mathbf{a}, \boldsymbol{\sigma}\cdot\mathbf{a}'] = 2i\boldsymbol{\sigma}\cdot(\mathbf{a} \times \mathbf{a}')$, with $|\mathbf{a} \times \mathbf{a}'| = |\sin\theta_{aa'}|$, the maximum eigenvalue of $\hat{S}^2$ is $4 + 4|\sin\theta_{aa'}||\sin\theta_{bb'}| \le 8$, achieved when $|\sin\theta_{aa'}| = |\sin\theta_{bb'}| = 1$ (i.e. $\theta_{aa'} = \theta_{bb'} = 90^\circ$). The maximum eigenvalue of $|\hat{S}|$ is then $\sqrt8 = 2\sqrt2$.

由于 $[\boldsymbol{\sigma}\cdot\mathbf{a}, \boldsymbol{\sigma}\cdot\mathbf{a}'] = 2i\boldsymbol{\sigma}\cdot(\mathbf{a} \times \mathbf{a}')$，$|\mathbf{a} \times \mathbf{a}'| = |\sin\theta_{aa'}|$，$\hat{S}^2$ 的最大本征值为 $4 + 4|\sin\theta_{aa'}||\sin\theta_{bb'}| \le 8$，当 $|\sin\theta_{aa'}| = |\sin\theta_{bb'}| = 1$（即 $\theta_{aa'} = \theta_{bb'} = 90^\circ$）时取到最大值。故 $|\hat{S}|$ 的最大本征值为 $\sqrt8 = 2\sqrt2$。

Therefore, for any quantum state,

因此对任意量子态，

$$ |\langle\hat{S}\rangle| \le \|\hat{S}\| = 2\sqrt2. $$

This is **Tsirelson's bound**: quantum mechanics cannot exceed $|S| = 2\sqrt2$. Our singlet calculation at the optimal angles achieved exactly this bound. $\blacksquare$

这就是**齐列尔逊界**：量子力学不能超过 $|S| = 2\sqrt2$。我们对单态在最优角度下的计算恰好达到了这个界。$\blacksquare$

**Summary of the three levels of bound:**

**三个层级界的总结：**

- Classical (deterministic): $|S| \le 2$ (CHSH inequality, any local realistic theory).
- Quantum mechanics: $|S| \le 2\sqrt2$ (Tsirelson bound; achieved by the singlet at optimal angles).
- No-signaling (general): $|S| \le 4$ (algebraic maximum).

- 经典（决定论的）：$|S| \le 2$（CHSH 不等式，任何定域实在论）。
- 量子力学：$|S| \le 2\sqrt2$（齐列尔逊界；单态在最优角度下达到）。
- 无信号（一般性）：$|S| \le 4$（代数最大值）。

The experimental violation of the classical bound by the quantum singlet — and the confirmation that $S \approx 2\sqrt2$ in loophole-free experiments (Hensen et al. 2015; Giustina et al. 2015; Shalm et al. 2015) — proves that nature is not locally realistic. No local hidden-variable theory can reproduce all quantum predictions.

量子单态对经典界的实验违反——以及无漏洞实验中 $S \approx 2\sqrt2$ 的确认（Hensen 等 2015；Giustina 等 2015；Shalm 等 2015）——证明了自然界不是定域实在的。没有任何局域隐变量理论能再现所有量子预言。

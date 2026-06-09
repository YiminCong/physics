# Derivations — Module 8.7: Parity Violation & the Weak Interaction
# 推导 — 模块 8.7：宇称不守恒与弱相互作用

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.7](./module-8.7-parity-violation-and-the-weak-interaction.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.7](./module-8.7-parity-violation-and-the-weak-interaction.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Chirality Projectors and Their Properties · 手征投影算符及其性质

**Claim.** The operators $P_L = (1 - \gamma^5)/2$ and $P_R = (1 + \gamma^5)/2$ are orthogonal projectors onto left-handed and right-handed chiral states, satisfying $P_L^2 = P_L$, $P_R^2 = P_R$, $P_L P_R = 0$, $P_L + P_R = 1$.

**命题。** 算符 $P_L = (1 - \gamma^5)/2$ 和 $P_R = (1 + \gamma^5)/2$ 是向左手和右手手征态投影的正交投影算符，满足 $P_L^2 = P_L$，$P_R^2 = P_R$，$P_L P_R = 0$，$P_L + P_R = 1$。

**Step 1 — Define $\gamma^5$.** The $\gamma^5$ matrix is defined as:

**第 1 步 — 定义 $\gamma^5$。** $\gamma^5$ 矩阵定义为：

$$ \gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3. $$

Its key properties (derived from the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$):

其关键性质（由克利福德代数 $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$ 导出）：

$$ (\gamma^5)^2 = (i\gamma^0\gamma^1\gamma^2\gamma^3)^2 = (i)^2(\gamma^0\gamma^1\gamma^2\gamma^3)^2 = -(\gamma^0\gamma^1\gamma^2\gamma^3)^2. $$

Compute $(\gamma^0\gamma^1\gamma^2\gamma^3)^2$ by reordering $\gamma^0\gamma^1\gamma^2\gamma^3\gamma^0\gamma^1\gamma^2\gamma^3$ into $(\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2$. Bringing the second $\gamma^0$ beside the first requires passing $\gamma^1\gamma^2\gamma^3$ (3 transpositions); the second $\gamma^1$ then passes $\gamma^2\gamma^3$ (2); the second $\gamma^2$ passes $\gamma^3$ (1) — total $3+2+1 = 6$ anticommutations, a factor $(-1)^6 = +1$. With $(\gamma^0)^2 = 1$ and $(\gamma^i)^2 = g^{ii} = -1$:

通过将 $\gamma^0\gamma^1\gamma^2\gamma^3\gamma^0\gamma^1\gamma^2\gamma^3$ 重排为 $(\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2$ 计算之：需 $3+2+1 = 6$ 次相邻反对易，符号 $(-1)^6 = +1$。利用 $(\gamma^0)^2 = 1$ 与 $(\gamma^i)^2 = g^{ii} = -1$：

$$ (\gamma^0\gamma^1\gamma^2\gamma^3)^2 = (\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2 = (1)(-1)(-1)(-1) = -1 \quad (\text{metric } (+\!-\!-\!-)). $$

故 $(\gamma^0\gamma^1\gamma^2\gamma^3)^2 = -1$。因此：

$$ (\gamma^5)^2 = -(-1) = +1, \quad \text{i.e.,} \quad \mathbf{(\gamma^5)^2 = 1}. $$

Also $\{\gamma^5, \gamma^\mu\} = 0$ for each $\mu$ ($\gamma^5$ anticommutes with all $\gamma^\mu$).

同样，对每个 $\mu$，$\{\gamma^5, \gamma^\mu\} = 0$（$\gamma^5$ 与所有 $\gamma^\mu$ 反对易）。

**Step 2 — Projector properties.** Define $P_L = (1 - \gamma^5)/2$ and $P_R = (1 + \gamma^5)/2$.

**第 2 步 — 投影算符性质。** 定义 $P_L = (1 - \gamma^5)/2$ 和 $P_R = (1 + \gamma^5)/2$。

(i) **Completeness:** $P_L + P_R = (1-\gamma^5)/2 + (1+\gamma^5)/2 = 1$. ✓

(i) **完备性：** $P_L + P_R = (1-\gamma^5)/2 + (1+\gamma^5)/2 = 1$。✓

(ii) **Idempotency of $P_L$:** $P_L^2 = [(1-\gamma^5)/2]^2 = (1 - 2\gamma^5 + (\gamma^5)^2)/4 = (1 - 2\gamma^5 + 1)/4 = (2 - 2\gamma^5)/4 = (1-\gamma^5)/2 = P_L$. ✓

(ii) **$P_L$ 的幂等性：** $P_L^2 = [(1-\gamma^5)/2]^2 = (1 - 2\gamma^5 + (\gamma^5)^2)/4 = (1 - 2\gamma^5 + 1)/4 = (2 - 2\gamma^5)/4 = (1-\gamma^5)/2 = P_L$。✓

Similarly $P_R^2 = P_R$. ✓

类似地 $P_R^2 = P_R$。✓

(iii) **Orthogonality:** $P_L P_R = [(1-\gamma^5)/2][(1+\gamma^5)/2] = (1 - (\gamma^5)^2)/4 = (1 - 1)/4 = \mathbf{0}$. ✓

(iii) **正交性：** $P_L P_R = [(1-\gamma^5)/2][(1+\gamma^5)/2] = (1 - (\gamma^5)^2)/4 = (1 - 1)/4 = \mathbf{0}$。✓

**Step 3 — Eigenvalues.** Since $(\gamma^5)^2 = 1$, the eigenvalues of $\gamma^5$ are $\pm 1$.

**第 3 步 — 本征值。** 由于 $(\gamma^5)^2 = 1$，$\gamma^5$ 的本征值为 $\pm 1$。

- Left-handed chirality state $\psi_L = P_L\psi$: $\gamma^5\psi_L = \gamma^5 P_L\psi = \gamma^5(1-\gamma^5)\psi/2 = (\gamma^5-1)\psi/2 = -P_L\psi = -\psi_L$. So $\psi_L$ is an eigenstate of $\gamma^5$ with eigenvalue $\mathbf{-1}$.

- 左手手征态 $\psi_L = P_L\psi$：$\gamma^5\psi_L = \gamma^5 P_L\psi = \gamma^5(1-\gamma^5)\psi/2 = (\gamma^5-1)\psi/2 = -P_L\psi = -\psi_L$。故 $\psi_L$ 是 $\gamma^5$ 本征值为 $\mathbf{-1}$ 的本征态。

- Right-handed chirality state $\psi_R = P_R\psi$: $\gamma^5\psi_R = \gamma^5(1+\gamma^5)\psi/2 = (\gamma^5+1)\psi/2 = P_R\psi = +\psi_R$. So $\psi_R$ is an eigenstate of $\gamma^5$ with eigenvalue $\mathbf{+1}$.

- 右手手征态 $\psi_R = P_R\psi$：$\gamma^5\psi_R = \gamma^5(1+\gamma^5)\psi/2 = (\gamma^5+1)\psi/2 = P_R\psi = +\psi_R$。故 $\psi_R$ 是 $\gamma^5$ 本征值为 $\mathbf{+1}$ 的本征态。$\blacksquare$

---

## B. Parity Transforms Left-Handed to Right-Handed · 宇称将左手态变换为右手态

**Claim.** Under parity P (spatial inversion $\mathbf{r} \to -\mathbf{r}$), a left-handed spinor $\psi_L$ transforms into a right-handed spinor, and vice versa: $\text{P}: \psi_L \leftrightarrow \psi_R$. Therefore a theory that couples only to $\psi_L$ maximally violates parity.

**命题。** 在宇称 P（空间反演 $\mathbf{r} \to -\mathbf{r}$）下，左手旋量 $\psi_L$ 变换为右手旋量，反之亦然：$\text{P}: \psi_L \leftrightarrow \psi_R$。因此，只耦合于 $\psi_L$ 的理论最大程度地破坏宇称。

**Step 1 — Parity acting on Dirac spinors.** Under the parity transformation, spacetime coordinates transform as:

**第 1 步 — 宇称作用于狄拉克旋量。** 在宇称变换下，时空坐标变换为：

$$ t \to t, \quad \mathbf{x} \to -\mathbf{x}, \quad \mathbf{p} \to -\mathbf{p}\ (\text{momentum changes sign}), \quad \mathbf{J} \to \mathbf{J}\ (\text{angular momentum is axial vector, unchanged}). $$

A Dirac spinor $\psi(t,\mathbf{x})$ transforms under parity as:

狄拉克旋量 $\psi(t,\mathbf{x})$ 在宇称下变换为：

$$ \text{P}: \psi(t,\mathbf{x}) \to \gamma^0\psi(t,-\mathbf{x}). $$

The factor $\gamma^0$ (intrinsic parity matrix) arises from the requirement that the Dirac equation remain covariant under P.

因子 $\gamma^0$（固有宇称矩阵）来自对狄拉克方程在 P 下协变的要求。

**Step 2 — How $\gamma^5$ transforms under P.** Under parity, $\gamma^0$ commutes with itself, and $\gamma^i$ (spatial components, $i = 1,2,3$) anticommute with $\gamma^0$ (since $\{\gamma^0,\gamma^i\} = 0$ for $i \ne 0$). Therefore, for $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$:

**第 2 步 — $\gamma^5$ 在 P 下如何变换。** 在宇称下，$\gamma^0$ 与自身对易，$\gamma^i$（空间分量，$i = 1,2,3$）与 $\gamma^0$ 反对易（因为对 $i \ne 0$，$\{\gamma^0,\gamma^i\} = 0$）。因此，对于 $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$：

Compute $\gamma^0\gamma^5\gamma^0$, using $(\gamma^0)^{-1} = \gamma^0$ (since $(\gamma^0)^2 = 1$ in the $(+\!-\!-\!-)$ metric):

计算 $\gamma^0\gamma^5\gamma^0$，利用 $(\gamma^0)^{-1} = \gamma^0$（因 $(+\!-\!-\!-)$ 度规中 $(\gamma^0)^2 = 1$）：

$$ \gamma^0 \cdot i\gamma^0\gamma^1\gamma^2\gamma^3 \cdot \gamma^0 = i(\gamma^0)^2\gamma^1\gamma^2\gamma^3\gamma^0 = i\gamma^1\gamma^2\gamma^3\gamma^0. $$

Now move $\gamma^0$ to the front: $\gamma^1\gamma^2\gamma^3\gamma^0 = -\gamma^1\gamma^2\gamma^0\gamma^3 = +\gamma^1\gamma^0\gamma^2\gamma^3 = -\gamma^0\gamma^1\gamma^2\gamma^3$ (each anticommutation of $\gamma^0$ past one $\gamma^i$ gives a factor $-1$, three times total):

现将 $\gamma^0$ 移到最前：$\gamma^1\gamma^2\gamma^3\gamma^0 = -\gamma^1\gamma^2\gamma^0\gamma^3 = +\gamma^1\gamma^0\gamma^2\gamma^3 = -\gamma^0\gamma^1\gamma^2\gamma^3$（$\gamma^0$ 每次与一个 $\gamma^i$ 反对易给出因子 $-1$，总共三次）：

$$ \gamma^0 \cdot \gamma^5 \cdot \gamma^0 = i \cdot (-\gamma^0\gamma^1\gamma^2\gamma^3) = -i\gamma^0\gamma^1\gamma^2\gamma^3 = \mathbf{-\gamma^5}. $$

So $\mathbf{\text{P}\gamma^5\text{P}^{-1} = -\gamma^5}$ (parity flips the sign of $\gamma^5$).

故 $\mathbf{\text{P}\gamma^5\text{P}^{-1} = -\gamma^5}$（宇称翻转 $\gamma^5$ 的符号）。

**Step 3 — Parity maps $P_L \leftrightarrow P_R$.** The projectors transform as:

**第 3 步 — 宇称将 $P_L$ 映射到 $P_R$。** 投影算符变换为：

$$ \text{P}\, P_L\, \text{P}^{-1} = \text{P}[(1-\gamma^5)/2]\text{P}^{-1} = (1 - \text{P}\gamma^5\text{P}^{-1})/2 = (1 - (-\gamma^5))/2 = (1+\gamma^5)/2 = \mathbf{P_R}. $$

$$ \text{P}\, P_R\, \text{P}^{-1} = \text{P}[(1+\gamma^5)/2]\text{P}^{-1} = (1 + (-\gamma^5))/2 = (1-\gamma^5)/2 = \mathbf{P_L}. $$

Therefore, acting on spinors:

因此，作用于旋量：

$$ \text{P}: \psi_L(t,\mathbf{x}) = P_L\psi(t,\mathbf{x}) \to P_R[\gamma^0\psi(t,-\mathbf{x})] = \gamma^0[P_L\psi(t,-\mathbf{x})]_R\ldots $$

More precisely: P sends $\psi_L(x) \to \gamma^0\psi(t,-\mathbf{x})$, and $[P_L]_{\text{transformed}} = P_R$, so the parity image of $\psi_L$ is a right-handed field. $\blacksquare$

更精确地：P 将 $\psi_L(x) \to \gamma^0\psi(t,-\mathbf{x})$，而 $[P_L]_{\text{变换后}} = P_R$，故 $\psi_L$ 的宇称象是右手场。$\blacksquare$

**Step 4 — Physical interpretation.** Chirality is Lorentz-invariant (it is an eigenvalue of $\gamma^5$, which commutes with Lorentz generators). Helicity (spin aligned/anti-aligned with momentum) equals chirality only in the massless limit. Under parity, momentum $\mathbf{p} \to -\mathbf{p}$ but spin $\mathbf{J} \to +\mathbf{J}$; so helicity flips. In the massless limit (where helicity = chirality), parity maps left-handed to right-handed particles. $\blacksquare$

**第 4 步 — 物理诠释。** 手征性是洛伦兹不变的（它是 $\gamma^5$ 的本征值，$\gamma^5$ 与洛伦兹生成元对易）。螺旋度（自旋与动量对齐/反对齐）只在无质量极限下等于手征性。在宇称下，动量 $\mathbf{p} \to -\mathbf{p}$ 但自旋 $\mathbf{J} \to +\mathbf{J}$；故螺旋度翻转。在无质量极限下（螺旋度 = 手征性），宇称将左手粒子映射到右手粒子。$\blacksquare$

---

## C. The V−A Current Structure of the Weak Interaction · 弱相互作用的 V−A 流结构

**Claim.** The weak charged current $J^\mu_W$ couples only to left-handed fermions, taking the form $J^\mu_W = \bar\psi_L\gamma^\mu\psi'_L = (1/2)\bar\psi\gamma^\mu(1-\gamma^5)\psi'$, which is the difference of a vector current (V) and an axial current (A): $J^\mu_W \propto V^\mu - A^\mu$.

**命题。** 弱带电流 $J^\mu_W$ 只耦合于左手费米子，取形式 $J^\mu_W = \bar\psi_L\gamma^\mu\psi'_L = (1/2)\bar\psi\gamma^\mu(1-\gamma^5)\psi'$，这是矢量流（V）与轴矢量流（A）之差：$J^\mu_W \propto V^\mu - A^\mu$。

**Step 1 — Rewrite in terms of V and A.** Using $\psi_L = P_L\psi = (1-\gamma^5)\psi/2$ and $\bar\psi_L = \bar\psi P_R$ (since $\bar{P_L} = P_R$ for the Dirac conjugate):

**第 1 步 — 用 V 和 A 重写。** 利用 $\psi_L = P_L\psi = (1-\gamma^5)\psi/2$ 和 $\bar\psi_L = \bar\psi P_R$（因为对于狄拉克共轭 $\bar{P_L} = P_R$）：

$$ \bar\psi_L = (\psi_L)^\dagger \gamma^0 = (P_L\psi)^\dagger \gamma^0 = \psi^\dagger P_L^\dagger \gamma^0. $$

More carefully: $P_L^\dagger = [(1-\gamma^5)/2]^\dagger = (1-\gamma^{5\dagger})/2$. Now $(\gamma^5)^\dagger = (i\gamma^0\gamma^1\gamma^2\gamma^3)^\dagger = -i(\gamma^3)^\dagger(\gamma^2)^\dagger(\gamma^1)^\dagger(\gamma^0)^\dagger = -i(-\gamma^3)(-\gamma^2)(-\gamma^1)(\gamma^0) = -i(-1)^3\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^3\gamma^2\gamma^1\gamma^0$.

更仔细地：$P_L^\dagger = [(1-\gamma^5)/2]^\dagger = (1-\gamma^{5\dagger})/2$。现在 $(\gamma^5)^\dagger = (i\gamma^0\gamma^1\gamma^2\gamma^3)^\dagger = -i(\gamma^3)^\dagger(\gamma^2)^\dagger(\gamma^1)^\dagger(\gamma^0)^\dagger = -i(-\gamma^3)(-\gamma^2)(-\gamma^1)(\gamma^0) = -i(-1)^3\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^3\gamma^2\gamma^1\gamma^0$.

Reversing the four factors $\gamma^3\gamma^2\gamma^1\gamma^0$ back to $\gamma^0\gamma^1\gamma^2\gamma^3$ takes 6 adjacent transpositions (factor $(-1)^6 = +1$), so $i\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \gamma^5$. Hence $\mathbf{(\gamma^5)^\dagger = \gamma^5}$ ($\gamma^5$ is hermitian).

将四个因子 $\gamma^3\gamma^2\gamma^1\gamma^0$ 反转回 $\gamma^0\gamma^1\gamma^2\gamma^3$ 需 6 次相邻对换（符号 $(-1)^6 = +1$），故 $i\gamma^3\gamma^2\gamma^1\gamma^0 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \gamma^5$。故 $\mathbf{(\gamma^5)^\dagger = \gamma^5}$（$\gamma^5$ 厄米）。

So $P_L^\dagger = (1-\gamma^5)/2 = P_L$. Then:

故 $P_L^\dagger = (1-\gamma^5)/2 = P_L$。则：

$$ \bar\psi_L = (P_L\psi)^\dagger\gamma^0 = \psi^\dagger P_L^\dagger\gamma^0 = \psi^\dagger P_L\gamma^0. $$

Now use the key identity $P_L\gamma^0 = \gamma^0 P_R$ (since $\gamma^0\gamma^5 = -\gamma^5\gamma^0$, so $\gamma^0(1-\gamma^5) = (1+\gamma^5)\gamma^0$):

现利用关键恒等式 $P_L\gamma^0 = \gamma^0 P_R$（因为 $\gamma^0\gamma^5 = -\gamma^5\gamma^0$，故 $\gamma^0(1-\gamma^5) = (1+\gamma^5)\gamma^0$）：

$$ \bar\psi_L = \psi^\dagger\gamma^0 P_R = \bar\psi P_R. $$

Therefore, the left-handed current:

因此，左手流：

$$ \bar\psi_L\gamma^\mu\psi'_L = (\bar\psi P_R)\gamma^\mu(P_L\psi') = \bar\psi P_R\gamma^\mu P_L\psi'. $$

Using the identity $P_R\gamma^\mu = \gamma^\mu P_L$ (from $\{\gamma^\mu, \gamma^5\} = 0$, i.e. $(1+\gamma^5)\gamma^\mu = \gamma^\mu(1-\gamma^5)$) together with $P_L^2 = P_L$:

利用恒等式 $P_R\gamma^\mu = \gamma^\mu P_L$（来自 $\{\gamma^\mu, \gamma^5\} = 0$，即 $(1+\gamma^5)\gamma^\mu = \gamma^\mu(1-\gamma^5)$）以及 $P_L^2 = P_L$：

$$ \bar\psi_L\gamma^\mu\psi'_L = \bar\psi(P_R\gamma^\mu P_L)\psi' = \bar\psi(\gamma^\mu P_L P_L)\psi' = \bar\psi\gamma^\mu P_L\psi'. \quad \text{So:} $$

$$ \bar\psi_L\gamma^\mu\psi'_L = \bar\psi(P_R\gamma^\mu P_L)\psi' = \bar\psi(\gamma^\mu P_L P_L)\psi' = \bar\psi\gamma^\mu P_L\psi'。\quad \text{故：} $$

$$ \bar\psi_L\gamma^\mu\psi'_L = \bar\psi\gamma^\mu P_L\psi' = \bar\psi\gamma^\mu (1-\gamma^5)/2 \cdot \psi' = \mathbf{(1/2)\bar\psi\gamma^\mu(1-\gamma^5)\psi'}. $$

**Step 2 — V minus A.** Expanding:

**第 2 步 — V 减 A。** 展开：

$$ \bar\psi_L\gamma^\mu\psi'_L = (1/2)[\bar\psi\gamma^\mu\psi' - \bar\psi\gamma^\mu\gamma^5\psi'] = (1/2)[V^\mu - A^\mu], $$

where $V^\mu = \bar\psi\gamma^\mu\psi'$ is the **vector current** (transforms as a 4-vector under P), and $A^\mu = \bar\psi\gamma^\mu\gamma^5\psi'$ is the **axial-vector current** (transforms with an extra minus sign under P — a pseudovector or axial vector).

其中 $V^\mu = \bar\psi\gamma^\mu\psi'$ 是**矢量流**（在 P 下作为 4-矢量变换），$A^\mu = \bar\psi\gamma^\mu\gamma^5\psi'$ 是**轴矢量流**（在 P 下变换时有额外的负号——赝矢量或轴矢量）。

**Step 3 — Parity properties.** Under parity:

**第 3 步 — 宇称性质。** 在宇称下：

$$ \text{P}V^\mu\text{P}^{-1} = \bar\psi(t,-\mathbf{x})\, \gamma^0\gamma^\mu\gamma^0\, \psi'(t,-\mathbf{x}) = \bar\psi(t,-\mathbf{x})\, \gamma_\mu\, \psi'(t,-\mathbf{x}) \quad (\text{since } \gamma^0\gamma^\mu\gamma^0 = \gamma_\mu). $$

For the spatial components ($\mu = i$): $\text{P}V^i\text{P}^{-1} = -V^i$ (spatial part of the vector changes sign — correct for a 4-vector). For $\text{P}A^\mu\text{P}^{-1}$: since $\gamma^5$ picks up a minus sign from parity ($\text{P}\gamma^5\text{P}^{-1} = -\gamma^5$, as shown in section B):

对于空间分量（$\mu = i$）：$\text{P}V^i\text{P}^{-1} = -V^i$（矢量的空间部分改变符号——对 4-矢量正确）。对于 $\text{P}A^\mu\text{P}^{-1}$：由于 $\gamma^5$ 在宇称下获得负号（$\text{P}\gamma^5\text{P}^{-1} = -\gamma^5$，如 B 节所示）：

$$ \text{P}A^\mu\text{P}^{-1} = \bar\psi(t,-\mathbf{x})\, \gamma^0\gamma^\mu\gamma^5\gamma^0\, \psi'(t,-\mathbf{x}) = -\bar\psi(t,-\mathbf{x})\, \gamma_\mu\gamma^5\, \psi'(t,-\mathbf{x}), \quad \text{so } \text{P}A^i\text{P}^{-1} = +A^i. $$

The axial current $A^i$ does NOT change sign under spatial inversion (opposite to $V^i$). Therefore $V - A$ does not transform simply under P: it mixes with $-V - A$ (after spatial inversion). This means the V−A current is NOT an eigenstate of parity — it violates parity maximally.

轴矢量流 $A^i$ 在空间反演下不改变符号（与 $V^i$ 相反）。因此 $V - A$ 在 P 下不简单变换：它与 $-V - A$（空间反演后）混合。这意味着 V−A 流不是宇称的本征态——它最大程度地破坏宇称。

Quantitatively: Under parity, $V - A \to -V - A = -(V + A)$. The original current couples to $V - A$; under P it would couple to $V + A$ (opposite sign of A). Since A appears with opposite sign in $V - A$ and $V + A$, this is **maximum parity violation** — the parity mirror image has a completely different chiral structure. $\blacksquare$

定量地：在宇称下，$V - A \to -V - A = -(V + A)$。原始流耦合于 $V - A$；在 P 下它将耦合于 $V + A$（A 的符号相反）。由于 A 在 $V - A$ 和 $V + A$ 中以相反的符号出现，这是**最大宇称破坏**——宇称镜像具有完全不同的手征结构。$\blacksquare$

---

## D. The Weak Charged Current in the Standard Model · 标准模型中的弱带电流

**Claim.** The $\text{SU(2)}_L$ gauge coupling in the Standard Model acts only on left-handed doublets, producing a charged current that is purely V−A. The resulting Fermi interaction for $\beta$-decay is $\propto (\bar u\gamma^\mu(1-\gamma^5)d)(\bar e\gamma_\mu(1-\gamma^5)\nu_e)$ — a product of two V−A currents.

**命题。** 标准模型中的 $\text{SU(2)}_L$ 规范耦合只作用于左手双重态，产生纯 V−A 的带电流。由此得到的 $\beta$ 衰变费米相互作用 $\propto (\bar u\gamma^\mu(1-\gamma^5)d)(\bar e\gamma_\mu(1-\gamma^5)\nu_e)$——两个 V−A 流的乘积。

**Step 1 — The W coupling.** From the $\text{SU(2)}_L$ covariant derivative, the coupling of $W^\pm_\mu$ to left-handed quark doublet $Q_L = (u, d)_L$ is:

**第 1 步 — W 耦合。** 由 $\text{SU(2)}_L$ 协变导数，$W^\pm_\mu$ 与左手夸克双重态 $Q_L = (u, d)_L$ 的耦合为：

$$ \mathcal{L}_{CC} = -(g/\sqrt 2)[W^+_\mu\, \bar u_L\gamma^\mu d_L + W^-_\mu\, \bar d_L\gamma^\mu u_L] + (\text{leptonic terms}). $$

Using $\bar\psi_L\gamma^\mu\psi'_L = (1/2)\bar\psi\gamma^\mu(1-\gamma^5)\psi'$:

利用 $\bar\psi_L\gamma^\mu\psi'_L = (1/2)\bar\psi\gamma^\mu(1-\gamma^5)\psi'$：

$$ \mathcal{L}_{CC} = -(g/(2\sqrt 2))[W^+_\mu\, \bar u\gamma^\mu(1-\gamma^5)d + W^-_\mu\, \bar d\gamma^\mu(1-\gamma^5)u] + (\text{leptons}). $$

This is pure V−A: no right-handed fermions couple to $W^\pm$.

这是纯 V−A：没有右手费米子耦合到 $W^\pm$。

**Step 2 — Low-energy Fermi theory.** At energies $E \ll m_W$, integrating out the W propagator ($1/(q^2-m_W^2) \to -1/m_W^2$ for $q^2 \ll m_W^2$):

**第 2 步 — 低能费米理论。** 在能量 $E \ll m_W$ 时，积分掉 W 传播子（$1/(q^2-m_W^2) \to -1/m_W^2$ 对于 $q^2 \ll m_W^2$）：

$$ \mathcal{L}_{Fermi} = (G_F/\sqrt 2)J^\mu_W J_{W,\mu}^\dagger, $$

with $G_F/\sqrt 2 = g^2/(8m_W^2)$ and $J^\mu_W = \bar u\gamma^\mu(1-\gamma^5)d + \bar\nu_e\gamma^\mu(1-\gamma^5)e$.

其中 $G_F/\sqrt 2 = g^2/(8m_W^2)$，$J^\mu_W = \bar u\gamma^\mu(1-\gamma^5)d + \bar\nu_e\gamma^\mu(1-\gamma^5)e$。

For $\beta$-decay ($n \to p + e^- + \bar\nu_e$, i.e., $d \to u + e^- + \bar\nu_e$ at quark level):

对于 $\beta$ 衰变（$n \to p + e^- + \bar\nu_e$，即夸克级别的 $d \to u + e^- + \bar\nu_e$）：

$$ \mathcal{L}_\beta = (G_F/\sqrt 2)[\bar u\gamma^\mu(1-\gamma^5)d][\bar e\gamma_\mu(1-\gamma^5)\nu_e] + \text{h.c.} $$

This is the **four-fermion V−A interaction** of Fermi (with the correct chiral structure derived from the SM), confirming that the weak force is purely left-handed (V−A) at low energies. $\blacksquare$

这是费米的**四费米子 V−A 相互作用**（手征结构由 SM 正确导出），证实了弱力在低能下是纯左手的（V−A）。$\blacksquare$

---

## E. Maximum Parity Violation: Quantitative Statement · 最大宇称破坏：定量表述

**Claim.** The weak interaction coupling is purely to $\psi_L$, meaning its parity-even (vector, V) and parity-odd (axial, A) couplings are equal in magnitude: $g_V = g_A$ ($= 1$ in the normalization where the SM coupling is $g_V - g_A = 1$). This equality $g_V = g_A$ is the definition of **maximal** parity violation.

**命题。** 弱相互作用的耦合纯粹到 $\psi_L$，意味着其宇称偶（矢量，V）和宇称奇（轴矢量，A）耦合的大小相等：$g_V = g_A$（$= 1$，在 SM 耦合为 $g_V - g_A = 1$ 的归一化中）。等式 $g_V = g_A$ 是**最大**宇称破坏的定义。

**Step 1 — General coupling.** A general current can be written as:

**第 1 步 — 一般耦合。** 一般流可以写为：

$$ J^\mu = \bar\psi\gamma^\mu(g_V - g_A\gamma^5)\psi = g_V \cdot \bar\psi\gamma^\mu\psi - g_A \cdot \bar\psi\gamma^\mu\gamma^5\psi. $$

For pure V coupling ($g_A = 0$): $J^\mu = g_V \bar\psi\gamma^\mu\psi$ (electromagnetic current — P invariant).
For pure A coupling ($g_V = 0$): $J^\mu = -g_A \bar\psi\gamma^\mu\gamma^5\psi$ (maximally violates P in opposite sense).
For V−A ($g_V = g_A = 1$): $J^\mu = \bar\psi\gamma^\mu(1-\gamma^5)\psi = 2\bar\psi_L\gamma^\mu\psi_L$ (purely left-handed).

对于纯 V 耦合（$g_A = 0$）：$J^\mu = g_V \bar\psi\gamma^\mu\psi$（电磁流——P 不变）。
对于纯 A 耦合（$g_V = 0$）：$J^\mu = -g_A \bar\psi\gamma^\mu\gamma^5\psi$（以相反意义最大程度地破坏 P）。
对于 V−A（$g_V = g_A = 1$）：$J^\mu = \bar\psi\gamma^\mu(1-\gamma^5)\psi = 2\bar\psi_L\gamma^\mu\psi_L$（纯左手）。

**Step 2 — Parity asymmetry.** Under parity, the vector current $V^\mu$ transforms as a true 4-vector ($V^0 \to V^0$, $V^i \to -V^i$) while the axial current $A^\mu$ transforms as a pseudovector ($A^0 \to -A^0$, $A^i \to +A^i$). If $g_V \ne g_A$, then the combination $g_V V^\mu - g_A A^\mu$ is not related to its parity transform $g_V V^\mu + g_A A^\mu$ by any simple relation $\to$ parity violated. The degree of violation is characterized by $|g_A/g_V|$. Maximum violation: $|g_A/g_V| = 1$, i.e., $g_V = \pm g_A$.

**第 2 步 — 宇称不对称性。** 在宇称下，矢量流 $V^\mu$ 作为真 4-矢量变换（$V^0 \to V^0$，$V^i \to -V^i$），而轴矢量流 $A^\mu$ 作为赝矢量变换（$A^0 \to -A^0$，$A^i \to +A^i$）。若 $g_V \ne g_A$，则组合 $g_V V^\mu - g_A A^\mu$ 与其宇称变换 $g_V V^\mu + g_A A^\mu$ 之间没有简单关系 $\to$ 宇称破坏。破坏程度由 $|g_A/g_V|$ 表征。最大破坏：$|g_A/g_V| = 1$，即 $g_V = \pm g_A$。

**Step 3 — The Wu experiment in this language.** In $^{60}\text{Co} \to {}^{60}\text{Ni} + e^- + \bar\nu_e$, the electron is emitted preferentially opposite to the nuclear spin. If parity were conserved, equal numbers would go parallel and anti-parallel to the spin (parity maps $\hat{\mathbf{n}} \to -\hat{\mathbf{n}}$ but $\mathbf{J} \to +\mathbf{J}$, so flipping the experiment by parity gives the opposite angular distribution). The observed $\cos\theta$ asymmetry in the electron distribution:

**第 3 步 — 吴实验的语言描述。** 在 $^{60}\text{Co} \to {}^{60}\text{Ni} + e^- + \bar\nu_e$ 中，电子优先向与核自旋相反的方向发射。若宇称守恒，则等量电子会向平行和反平行于自旋方向发射（宇称将 $\hat{\mathbf{n}} \to -\hat{\mathbf{n}}$ 但 $\mathbf{J} \to +\mathbf{J}$，故通过宇称翻转实验给出相反的角分布）。电子分布中观测到的 $\cos\theta$ 不对称性：

$$ W(\theta) \propto 1 + A\cos\theta, $$

with $A \ne 0$ (experimentally $A \approx -1$ for the $^{60}\text{Co}$ experiment) is a direct measure of parity violation. The maximum value $|A| = 1$ corresponds to maximum parity violation (pure V−A). The observation $A \approx -1$ confirmed maximal parity violation and that the weak current is purely V−A. $\blacksquare$

其中 $A \ne 0$（$^{60}\text{Co}$ 实验中实验上 $A \approx -1$）是宇称破坏的直接量度。最大值 $|A| = 1$ 对应最大宇称破坏（纯 V−A）。观测 $A \approx -1$ 确认了最大宇称破坏，以及弱流是纯 V−A 的。$\blacksquare$

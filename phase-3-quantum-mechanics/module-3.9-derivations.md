# Derivations — Module 3.9: Fundamental Concepts (Sakurai)
# 推导 — 模块 3.9：基本概念（樱井）

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.9](./module-3.9-fundamental-concepts.md). Full step-by-step proofs of the spin-½ measurement probabilities, the $S_z/S_x$ basis change, the momentum eigenfunction $\langle x|p\rangle$, and the Fourier-transform connection between position and momentum representations. English first, then 中文.
> [模块 3.9](./module-3.9-fundamental-concepts.md) 的配套文档：自旋-½ 测量概率、$S_z/S_x$ 基变换、动量本征函数 $\langle x|p\rangle$、以及位置与动量表象之间傅里叶变换关系的完整逐步证明。先英文，后中文。

---

## A. Spin-½ Sequential Measurement Probabilities · 自旋-½ 序列测量概率

**Claim.** For a spin-½ particle prepared in the $S_z$ eigenstate $|+z\rangle$, the probability that a subsequent measurement of $S_x$ yields $+\hbar/2$ is $1/2$. Moreover, if after that $S_x$ measurement the particle is in $|+x\rangle$ and $S_z$ is measured again, the probability of finding $+\hbar/2$ is again $1/2$ — the $S_z$ information has been destroyed.

**命题。** 对于制备在 $S_z$ 本征态 $|+z\rangle$ 的自旋-½ 粒子，随后测量 $S_x$ 得到 $+\hbar/2$ 的概率为 $1/2$。而且，若在 $S_x$ 测量后粒子处于 $|+x\rangle$，再次测量 $S_z$，得到 $+\hbar/2$ 的概率仍为 $1/2$——$S_z$ 的信息已被破坏。

**Step 1 — Establish the $S_z$ eigenstates.** The eigenstates of $\hat{S}_z$ are defined by

**第 1 步 — 建立 $S_z$ 本征态。** $\hat{S}_z$ 的本征态定义为

$$ \hat{S}_z |+z\rangle = +\frac{\hbar}{2}|+z\rangle, \qquad \hat{S}_z |-z\rangle = -\frac{\hbar}{2}|-z\rangle. $$

In the $\{|+z\rangle, |-z\rangle\}$ basis, using the Pauli matrices $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$:

在 $\{|+z\rangle, |-z\rangle\}$ 基中，利用泡利矩阵 $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$：

$$ \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}. $$

So $|+z\rangle = [1, 0]^\mathsf{T}$ and $|-z\rangle = [0, 1]^\mathsf{T}$ in column-vector notation.

故在列向量记号中 $|+z\rangle = [1, 0]^\mathsf{T}$，$|-z\rangle = [0, 1]^\mathsf{T}$。

**Step 2 — Find the $S_x$ eigenstates.** Diagonalize $\sigma_x$:

**第 2 步 — 求 $S_x$ 本征态。** 对角化 $\sigma_x$：

$$ \det(\sigma_x - \lambda I) = \lambda^2 - 1 = 0 \quad \implies \quad \lambda = \pm 1. $$

For $\lambda = +1$: $(\sigma_x - I)v = 0$ gives $[-1, 1; 1, -1]v = 0$, so $v_1 = v_2$, normalized: $|+x\rangle = (1/\sqrt2)[1, 1]^\mathsf{T} = (1/\sqrt2)(|+z\rangle + |-z\rangle)$.

对 $\lambda = +1$：$(\sigma_x - I)v = 0$ 给出 $[-1,1;1,-1]v = 0$，故 $v_1 = v_2$，归一化后：$|+x\rangle = (1/\sqrt2)[1,1]^\mathsf{T} = (1/\sqrt2)(|+z\rangle + |-z\rangle)$。

For $\lambda = -1$: similarly $v_1 = -v_2$, giving $|-x\rangle = (1/\sqrt2)[1, -1]^\mathsf{T} = (1/\sqrt2)(|+z\rangle - |-z\rangle)$.

对 $\lambda = -1$：类似地 $v_1 = -v_2$，得 $|-x\rangle = (1/\sqrt2)[1,-1]^\mathsf{T} = (1/\sqrt2)(|+z\rangle - |-z\rangle)$。

**Step 3 — Probability of $S_x = +\hbar/2$.** The Born rule gives

**第 3 步 — $S_x = +\hbar/2$ 的概率。** 玻恩定则给出

$$ \begin{aligned} P(S_x = +\hbar/2 \mid \text{prepared in } |+z\rangle) &= |\langle +x|+z\rangle|^2 \\ &= |(1/\sqrt2)([1,1] \cdot [1,0])|^2 = |(1/\sqrt2) \cdot 1|^2 = \tfrac12. \end{aligned} $$

Similarly $P(S_x = -\hbar/2 \mid |+z\rangle) = |\langle -x|+z\rangle|^2 = |(1/\sqrt2)|^2 = 1/2$.

类似地 $P(S_x = -\hbar/2 \mid |+z\rangle) = |\langle -x|+z\rangle|^2 = |(1/\sqrt2)|^2 = 1/2$。

Both outcomes are equally likely — confirming maximal uncertainty in $S_x$ for a $S_z$ eigenstate.

两种结果等可能——确认了 $S_z$ 本征态中 $S_x$ 的最大不确定性。

**Step 4 — Post-measurement state and renewed $S_z$ measurement.** After the $S_x$ measurement yields $+\hbar/2$, the state collapses to $|+x\rangle = (1/\sqrt2)(|+z\rangle + |-z\rangle)$. Now measuring $S_z$:

**第 4 步 — 测量后状态及再次测量 $S_z$。** $S_x$ 测量结果为 $+\hbar/2$ 后，态塌缩为 $|+x\rangle = (1/\sqrt2)(|+z\rangle + |-z\rangle)$。现在测量 $S_z$：

$$ \begin{aligned} P(S_z = +\hbar/2 \mid |+x\rangle) &= |\langle +z|+x\rangle|^2 = |1/\sqrt2|^2 = \tfrac12, \\ P(S_z = -\hbar/2 \mid |+x\rangle) &= |\langle -z|+x\rangle|^2 = |1/\sqrt2|^2 = \tfrac12. \end{aligned} $$

The original $S_z$ information is completely destroyed. This is the quantum manifestation of the incompatibility $[\hat{S}_z, \hat{S}_x] \ne 0$. $\blacksquare$

原来的 $S_z$ 信息被完全破坏。这是不相容性 $[\hat{S}_z, \hat{S}_x] \ne 0$ 的量子体现。$\blacksquare$

**Physical meaning.** There is no state that simultaneously has definite $S_z$ and definite $S_x$. Measuring one observable in a complete eigenstate of the other maximally randomizes the measured result.

**物理含义。** 不存在同时具有确定 $S_z$ 和确定 $S_x$ 的态。在另一个可观测量的完全本征态中测量一个可观测量，会使测量结果最大程度地随机化。

---

## B. Change of Basis: $S_z$ Eigenstates $\leftrightarrow$ $S_x$ Eigenstates · 基变换：$S_z$ 本征态 $\leftrightarrow$ $S_x$ 本征态

**Claim.** The $S_x$ eigenstates in the $S_z$ basis are $|\pm x\rangle = (1/\sqrt2)(|+z\rangle \pm |-z\rangle)$, and conversely the $S_z$ eigenstates in the $S_x$ basis are $|\pm z\rangle = (1/\sqrt2)(|+x\rangle \pm |-x\rangle)$.

**命题。** $S_x$ 本征态在 $S_z$ 基中为 $|\pm x\rangle = (1/\sqrt2)(|+z\rangle \pm |-z\rangle)$，反之 $S_z$ 本征态在 $S_x$ 基中为 $|\pm z\rangle = (1/\sqrt2)(|+x\rangle \pm |-x\rangle)$。

**Step 1 — Operator in $S_z$ basis.** From $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$ with $\sigma_x$ given above, $\hat{S}_x$ acts as

**第 1 步 — $S_z$ 基中的算符。** 由 $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$ 及上述 $\sigma_x$，$\hat{S}_x$ 的作用为

$$ \hat{S}_x |+z\rangle = \frac{\hbar}{2}|-z\rangle, \qquad \hat{S}_x |-z\rangle = \frac{\hbar}{2}|+z\rangle. $$

This follows from $(\hbar/2)\sigma_x \cdot [1,0]^\mathsf{T} = (\hbar/2)[0,1]^\mathsf{T}$ and $(\hbar/2)\sigma_x \cdot [0,1]^\mathsf{T} = (\hbar/2)[1,0]^\mathsf{T}$.

由 $(\hbar/2)\sigma_x \cdot [1,0]^\mathsf{T} = (\hbar/2)[0,1]^\mathsf{T}$ 及 $(\hbar/2)\sigma_x \cdot [0,1]^\mathsf{T} = (\hbar/2)[1,0]^\mathsf{T}$ 可得。

**Step 2 — Eigenvalue equation for $\hat{S}_x$.** For the eigenvalue equation $\hat{S}_x|\alpha\rangle = (\hbar/2)|\alpha\rangle$, write $|\alpha\rangle = a|+z\rangle + b|-z\rangle$:

**第 2 步 — $\hat{S}_x$ 的本征值方程。** 对本征值方程 $\hat{S}_x|\alpha\rangle = (\hbar/2)|\alpha\rangle$，令 $|\alpha\rangle = a|+z\rangle + b|-z\rangle$：

$$ \hat{S}_x|\alpha\rangle = \frac{\hbar}{2}(b|+z\rangle + a|-z\rangle) = \frac{\hbar}{2}(a|+z\rangle + b|-z\rangle). $$

Matching coefficients: $b = a$ and $a = b$, so $a = b$. Normalization $|a|^2 + |b|^2 = 1$ gives $a = b = 1/\sqrt2$:

对应系数：$b = a$，$a = b$，故 $a = b$。归一化 $|a|^2 + |b|^2 = 1$ 给出 $a = b = 1/\sqrt2$：

$$ |+x\rangle = \frac{1}{\sqrt2}(|+z\rangle + |-z\rangle). $$

For eigenvalue $-\hbar/2$: $b = -a$, giving $|-x\rangle = (1/\sqrt2)(|+z\rangle - |-z\rangle)$.

对本征值 $-\hbar/2$：$b = -a$，给出 $|-x\rangle = (1/\sqrt2)(|+z\rangle - |-z\rangle)$。

**Step 3 — Invert the basis change.** Adding and subtracting the relations:

**第 3 步 — 反转基变换。** 将两个关系式相加和相减：

$$ \begin{aligned} |+x\rangle + |-x\rangle &= \tfrac{1}{\sqrt2}(|+z\rangle+|-z\rangle) + \tfrac{1}{\sqrt2}(|+z\rangle-|-z\rangle) = \tfrac{2}{\sqrt2}|+z\rangle = \sqrt2\, |+z\rangle, \\ |+x\rangle - |-x\rangle &= \tfrac{1}{\sqrt2}(|+z\rangle+|-z\rangle) - \tfrac{1}{\sqrt2}(|+z\rangle-|-z\rangle) = \tfrac{2}{\sqrt2}|-z\rangle = \sqrt2\, |-z\rangle. \end{aligned} $$

Hence $|+z\rangle = (1/\sqrt2)(|+x\rangle + |-x\rangle)$ and $|-z\rangle = (1/\sqrt2)(|+x\rangle - |-x\rangle)$. The change-of-basis matrix is the Hadamard matrix $H = (1/\sqrt2)\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, which is its own inverse ($H^2 = I$). $\blacksquare$

故 $|+z\rangle = (1/\sqrt2)(|+x\rangle + |-x\rangle)$，$|-z\rangle = (1/\sqrt2)(|+x\rangle - |-x\rangle)$。基变换矩阵为阿达马矩阵 $H = (1/\sqrt2)\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$，它是自身的逆（$H^2 = I$）。$\blacksquare$

---

## C. The Momentum Eigenfunction $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$ · 动量本征函数

**Claim.** The position-basis representation of a momentum eigenstate $|p\rangle$ (satisfying $\hat{p}|p\rangle = p|p\rangle$) is

**命题。** 动量本征态 $|p\rangle$（满足 $\hat{p}|p\rangle = p|p\rangle$）的坐标基表象为

$$ \langle x|p\rangle = \frac{e^{ipx/\hbar}}{\sqrt{2\pi\hbar}}. $$

**Step 1 — Position representation of $\hat{p}$.** Recall that in the position representation, the momentum operator acts as

**第 1 步 — $\hat{p}$ 的坐标表象。** 回顾在坐标表象中，动量算符的作用为

$$ \hat{p} \mapsto -i\hbar \frac{d}{dx} \quad \text{(acting on wavefunctions } \psi(x) = \langle x|\psi\rangle\text{)}. $$

This is derived from the canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$: the unique (up to unitary equivalence) representation of this relation on $L^2(\mathbb{R})$ has $\hat{x} =$ multiplication by $x$ and $\hat{p} = -i\hbar\, d/dx$ (Stone–von Neumann theorem).

这由正则对易关系 $[\hat{x}, \hat{p}] = i\hbar$ 推导得到：该关系在 $L^2(\mathbb{R})$ 上的唯一（在幺正等价意义下）表示为 $\hat{x} =$ 乘以 $x$，$\hat{p} = -i\hbar\, d/dx$（Stone–von Neumann 定理）。

**Step 2 — Eigenvalue equation in position space.** Acting $\langle x|$ on the eigenvalue equation $\hat{p}|p\rangle = p|p\rangle$:

**第 2 步 — 坐标空间中的本征值方程。** 对本征值方程 $\hat{p}|p\rangle = p|p\rangle$ 作用 $\langle x|$：

$$ \begin{aligned} \langle x|\hat{p}|p\rangle &= p\, \langle x|p\rangle, \\ -i\hbar \frac{d}{dx} \langle x|p\rangle &= p\, \langle x|p\rangle. \end{aligned} $$

This is a first-order ODE: $d\varphi/dx = (ip/\hbar)\varphi$ where $\varphi(x) = \langle x|p\rangle$.

这是一阶常微分方程：$d\varphi/dx = (ip/\hbar)\varphi$，其中 $\varphi(x) = \langle x|p\rangle$。

**Step 3 — Solve the ODE.** The general solution is $\varphi(x) = C e^{ipx/\hbar}$ for a constant $C$.

**第 3 步 — 求解常微分方程。** 通解为 $\varphi(x) = C e^{ipx/\hbar}$，$C$ 为常数。

**Step 4 — Fix the normalization by the Dirac-delta condition.** Momentum eigenstates satisfy the continuous orthonormality condition $\langle p|p'\rangle = \delta(p - p')$. Compute:

**第 4 步 — 由狄拉克 $\delta$ 条件确定归一化。** 动量本征态满足连续正交归一条件 $\langle p|p'\rangle = \delta(p - p')$。计算：

$$ \begin{aligned} \langle p|p'\rangle &= \int_{-\infty}^{\infty} \langle p|x\rangle \langle x|p'\rangle\, dx = \int_{-\infty}^{\infty} \varphi^*(x)\, \varphi'(x)\, dx \\ &= |C|^2 \int_{-\infty}^{\infty} e^{-ipx/\hbar} e^{ip'x/\hbar}\, dx \\ &= |C|^2 \int_{-\infty}^{\infty} e^{i(p'-p)x/\hbar}\, dx. \end{aligned} $$

Using the Fourier representation of the delta function:

利用 $\delta$ 函数的傅里叶表示：

$$ \int_{-\infty}^{\infty} e^{i(p'-p)x/\hbar}\, dx = 2\pi\hbar\, \delta(p' - p) = 2\pi\hbar\, \delta(p - p'). $$

Therefore $|C|^2 \cdot 2\pi\hbar = 1$, giving $|C| = 1/\sqrt{2\pi\hbar}$. Choosing the conventional phase $C = 1/\sqrt{2\pi\hbar}$:

因此 $|C|^2 \cdot 2\pi\hbar = 1$，给出 $|C| = 1/\sqrt{2\pi\hbar}$。选取惯用相位 $C = 1/\sqrt{2\pi\hbar}$：

$$ \boxed{\, \langle x|p\rangle = \frac{e^{ipx/\hbar}}{\sqrt{2\pi\hbar}} \,} \qquad \blacksquare $$

**Physical meaning.** A momentum eigenstate has a completely defined wavelength $\lambda = h/p$ (de Broglie) but is completely delocalized in position — consistent with the uncertainty principle $\Delta x\, \Delta p \ge \hbar/2$, with $\Delta x = \infty$ and $\Delta p = 0$.

**物理含义。** 动量本征态具有完全确定的波长 $\lambda = h/p$（德布罗意），但在位置上完全弥散——与不确定性原理 $\Delta x\, \Delta p \ge \hbar/2$ 一致（$\Delta x = \infty$，$\Delta p = 0$）。

---

## D. Position and Momentum Representations as Fourier Transforms · 位置表象与动量表象互为傅里叶变换

**Claim.** The wavefunction in position space $\psi(x) = \langle x|\psi\rangle$ and the wavefunction in momentum space $\varphi(p) = \langle p|\psi\rangle$ are related by the Fourier transform pair:

**命题。** 坐标空间波函数 $\psi(x) = \langle x|\psi\rangle$ 与动量空间波函数 $\varphi(p) = \langle p|\psi\rangle$ 通过傅里叶变换对联系：

$$ \begin{aligned} \varphi(p) &= \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \psi(x)\, e^{-ipx/\hbar}\, dx, \\ \psi(x) &= \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \varphi(p)\, e^{ipx/\hbar}\, dp. \end{aligned} $$

**Step 1 — Insert the momentum resolution of identity.** The completeness relation for momentum eigenstates (continuous spectrum) is

**第 1 步 — 插入动量单位分解。** 动量本征态的完备性关系（连续谱）为

$$ \int_{-\infty}^{\infty} |p\rangle\langle p|\, dp = \hat{1}. $$

Insert this between $\langle x|$ and $|\psi\rangle$:

将其插入 $\langle x|$ 与 $|\psi\rangle$ 之间：

$$ \psi(x) = \langle x|\psi\rangle = \langle x| \Big(\int|p\rangle\langle p|\, dp\Big) |\psi\rangle = \int \langle x|p\rangle \langle p|\psi\rangle\, dp = \int \frac{e^{ipx/\hbar}}{\sqrt{2\pi\hbar}} \varphi(p)\, dp. $$

This is exactly the inverse Fourier transform (with the convention $k = p/\hbar$):

这正是傅里叶逆变换（约定 $k = p/\hbar$）：

$$ \psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \varphi(p)\, e^{ipx/\hbar}\, dp. $$

**Step 2 — The forward transform.** Similarly, insert the position resolution of identity $\int|x\rangle\langle x|\, dx = \hat{1}$ between $\langle p|$ and $|\psi\rangle$:

**第 2 步 — 正变换。** 类似地，将位置单位分解 $\int|x\rangle\langle x|\, dx = \hat{1}$ 插入 $\langle p|$ 与 $|\psi\rangle$ 之间：

$$ \varphi(p) = \langle p|\psi\rangle = \int \langle p|x\rangle \langle x|\psi\rangle\, dx = \int \frac{e^{-ipx/\hbar}}{\sqrt{2\pi\hbar}} \psi(x)\, dx. $$

Hence $\varphi(p) = (1/\sqrt{2\pi\hbar}) \int \psi(x)\, e^{-ipx/\hbar}\, dx$, the Fourier transform of $\psi(x)$.

故 $\varphi(p) = (1/\sqrt{2\pi\hbar}) \int \psi(x)\, e^{-ipx/\hbar}\, dx$，即 $\psi(x)$ 的傅里叶变换。

**Step 3 — Self-consistency: Parseval's theorem.** The probability interpretation requires both $\int|\psi(x)|^2\, dx = 1$ and $\int|\varphi(p)|^2\, dp = 1$. That both hold simultaneously follows from Parseval's theorem for Fourier transforms:

**第 3 步 — 自洽性：帕塞瓦尔定理。** 概率诠释要求 $\int|\psi(x)|^2\, dx = 1$ 和 $\int|\varphi(p)|^2\, dp = 1$ 同时成立。这两者同时成立来自傅里叶变换的帕塞瓦尔定理：

$$ \int_{-\infty}^{\infty} |\varphi(p)|^2\, dp = \int_{-\infty}^{\infty} |\psi(x)|^2\, dx. $$

Proof: $\int|\varphi(p)|^2\, dp = \int\int\int \psi^*(x)\, \psi(x')\, (1/2\pi\hbar)\, e^{ip(x-x')/\hbar}\, dx\, dx'\, dp$. The $p$-integral gives $(1/2\pi\hbar)\cdot 2\pi\hbar\, \delta(x-x') = \delta(x-x')$, so the result is $\int|\psi(x)|^2\, dx$. $\blacksquare$

证明：$\int|\varphi(p)|^2\, dp = \int\int\int \psi^*(x)\psi(x')(1/2\pi\hbar)e^{ip(x-x')/\hbar}\, dx\, dx'\, dp$。对 $p$ 积分给出 $(1/2\pi\hbar)\cdot 2\pi\hbar\, \delta(x-x') = \delta(x-x')$，故结果为 $\int|\psi(x)|^2\, dx$。$\blacksquare$

**Step 4 — Momentum operator in position space (rederived).** The action of $\hat{p}$ in position space follows directly:

**第 4 步 — 坐标空间中的动量算符（重新推导）。** $\hat{p}$ 在坐标空间中的作用直接由此得到：

$$ \begin{aligned} \langle x|\hat{p}|\psi\rangle &= \int \langle x|\hat{p}|p\rangle\, \varphi(p)\, dp = \int p\, \langle x|p\rangle\, \varphi(p)\, dp \\ &= \int p\, \frac{e^{ipx/\hbar}}{\sqrt{2\pi\hbar}}\, \varphi(p)\, dp \\ &= -i\hbar \frac{d}{dx} \int \frac{e^{ipx/\hbar}}{\sqrt{2\pi\hbar}}\, \varphi(p)\, dp \\ &= -i\hbar \frac{d\psi}{dx}. \end{aligned} $$

Thus the abstract equation $\hat{p}|\psi\rangle$ becomes the differential operator $-i\hbar\, d/dx$ in position space, confirming the result of Step 1 in Section C above. $\blacksquare$

因此抽象方程 $\hat{p}|\psi\rangle$ 在坐标空间中变为微分算符 $-i\hbar\, d/dx$，确认了上文 C 节第 1 步的结果。$\blacksquare$

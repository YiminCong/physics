# Derivations — Module 3.4: Quantum Mechanics in 3D
# 推导 — 模块 3.4：三维量子力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.4](./module-3.4-quantum-mechanics-in-3d.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.4](./module-3.4-quantum-mechanics-in-3d.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. Separation of Variables in 3D Schrödinger Equation (Spherical Coordinates) · 三维薛定谔方程的球坐标分离变量

**Claim.** For a central potential $V = V(r)$, the 3D time-independent Schrödinger equation (TISE) $-(\hbar^2/2m)\nabla^2\psi + V(r)\psi = E\psi$ separates in spherical coordinates $(r, \theta, \varphi)$ into an angular equation and a radial equation, with the angular part solved by spherical harmonics $Y_\ell^m(\theta,\varphi)$.

**命题。** 对于中心势 $V = V(r)$，三维定态薛定谔方程 $-(\hbar^2/2m)\nabla^2\psi + V(r)\psi = E\psi$ 在球坐标 $(r, \theta, \varphi)$ 中分离为角向方程与径向方程，角向部分由球谐函数 $Y_\ell^m(\theta,\varphi)$ 求解。

**Step 1 — Laplacian in spherical coordinates.** The Laplacian in spherical coordinates is:

**第 1 步 — 球坐标中的拉普拉斯算符。** 球坐标中的拉普拉斯算符为：

$$ \nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial}{\partial r}\Big) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}. $$

The angular part is related to the orbital angular momentum operator $\hat{L}^2$ by:

角向部分与轨道角动量算符 $\hat{L}^2$ 的关系为：

$$ -\hbar^2\Lambda^2 \equiv \hat{L}^2, \qquad \text{where } \Lambda^2 = \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}. $$

So: $\nabla^2 = (1/r^2)\,\partial/\partial r\,(r^2\,\partial/\partial r) - \hat{L}^2/(\hbar^2 r^2)$.

因此：$\nabla^2 = (1/r^2)\,\partial/\partial r\,(r^2\,\partial/\partial r) - \hat{L}^2/(\hbar^2 r^2)$。

**Step 2 — Write the TISE.** The TISE becomes:

**第 2 步 — 写出定态薛定谔方程。** 定态薛定谔方程变为：

$$ -\frac{\hbar^2}{2m}\Big[\frac{1}{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial\psi}{\partial r}\Big) - \frac{\hat{L}^2\psi}{\hbar^2 r^2}\Big] + V(r)\psi = E\psi. $$

Multiply through by $-2m/\hbar^2$:

两边乘以 $-2m/\hbar^2$：

$$ \frac{1}{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial\psi}{\partial r}\Big) - \frac{\hat{L}^2\psi}{\hbar^2 r^2} + \frac{2m}{\hbar^2}(E - V)\psi = 0. \qquad \text{(TISE)} $$

**Step 3 — Separate variables.** Try $\psi(r,\theta,\varphi) = R(r)\cdot Y(\theta,\varphi)$. Substitute:

**第 3 步 — 分离变量。** 尝试 $\psi(r,\theta,\varphi) = R(r)\cdot Y(\theta,\varphi)$。代入：

$$ Y\,\frac{1}{r^2}\frac{d}{dr}(r^2 R') + R\Big[-\frac{\hat{L}^2 Y}{\hbar^2 r^2}\Big] + \frac{2m}{\hbar^2}(E-V)RY = 0. $$

Divide by $RY/r^2$:

除以 $RY/r^2$：

$$ \frac{1}{R}\frac{d}{dr}(r^2 R') + \frac{2m}{\hbar^2}(E-V)r^2 = \frac{1}{Y}\frac{\hat{L}^2 Y}{\hbar^2}. $$

The left side depends only on $r$; the right side only on angles. Both must equal a constant — call it $\ell(\ell+1)$:

左边仅依赖于 $r$；右边仅依赖于角度。两边必须等于同一个常数——记为 $\ell(\ell+1)$：

**Angular equation:** $\hat{L}^2 Y = \hbar^2\ell(\ell+1)\,Y$. … (AE)

**角向方程：** $\hat{L}^2 Y = \hbar^2\ell(\ell+1)\,Y$。 … (角)

**Radial equation:** $(1/r^2)\,d/dr(r^2\,dR/dr) + [2m/\hbar^2(E-V) - \ell(\ell+1)/r^2]R = 0$. … (RE)

**径向方程：** $(1/r^2)\,d/dr(r^2\,dR/dr) + [2m/\hbar^2(E-V) - \ell(\ell+1)/r^2]R = 0$。 … (径)

**Step 4 — Further separation of the angular equation.** Set $Y(\theta,\varphi) = \Theta(\theta)\Phi(\varphi)$. The $\varphi$-dependence in $\hat{L}^2$ is just $\partial^2/\partial\varphi^2$, so $\hat{L}_z = -i\hbar\,\partial/\partial\varphi$ gives:

**第 4 步 — 角向方程的进一步分离。** 令 $Y(\theta,\varphi) = \Theta(\theta)\Phi(\varphi)$。$\hat{L}^2$ 中的 $\varphi$ 依赖仅为 $\partial^2/\partial\varphi^2$，$\hat{L}_z = -i\hbar\,\partial/\partial\varphi$ 给出：

$$ d^2\Phi/d\varphi^2 = -m^2\Phi, \qquad \text{solution: } \Phi(\varphi) = e^{im\varphi}. $$

Single-valuedness $\Phi(\varphi + 2\pi) = \Phi(\varphi)$ requires **$m$ integer**. The remaining $\theta$-equation (with $\hat{L}^2$ including the $-m^2/\sin^2\theta$ term from $-\Phi''/\Phi$) is the **associated Legendre equation**, whose normalizable solutions exist only for $\ell = 0, 1, 2, \ldots$ and $-\ell \le m \le \ell$.

单值性条件 $\Phi(\varphi + 2\pi) = \Phi(\varphi)$ 要求 **$m$ 为整数**。剩余的 $\theta$ 方程（$\hat{L}^2$ 包含来自 $-\Phi''/\Phi$ 的 $-m^2/\sin^2\theta$ 项）是**连带勒让德方程**，其可归一化的解仅在 $\ell = 0, 1, 2, \ldots$ 且 $-\ell \le m \le \ell$ 时存在。

The normalized solutions $Y_\ell^m(\theta,\varphi) = N\cdot P_\ell^m(\cos\theta)\,e^{im\varphi}$ are the **spherical harmonics**. They satisfy (AE) by construction. $\blacksquare$

归一化解 $Y_\ell^m(\theta,\varphi) = N\cdot P_\ell^m(\cos\theta)\,e^{im\varphi}$ 是**球谐函数**。由构造它们满足（角）方程。$\blacksquare$

---

## B. Angular Momentum Algebra: $\hat{L}^2$ and $\hat{L}_z$ Eigenvalues · 角动量代数：$\hat{L}^2$ 与 $\hat{L}_z$ 的本征值

**Claim.** From the fundamental commutation relations $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ (and cyclic permutations) and $[\hat{L}^2, \hat{L}_i] = 0$, the simultaneous eigenvalues of $\hat{L}^2$ and $\hat{L}_z$ are $\hbar^2\ell(\ell+1)$ and $m\hbar$ respectively, with $\ell = 0, 1, 2, \ldots$ and $m = -\ell, \ldots, +\ell$.

**命题。** 由基本对易关系 $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$（及其轮换），以及 $[\hat{L}^2, \hat{L}_i] = 0$，$\hat{L}^2$ 与 $\hat{L}_z$ 的同时本征值分别为 $\hbar^2\ell(\ell+1)$ 和 $m\hbar$，其中 $\ell = 0, 1, 2, \ldots$，$m = -\ell, \ldots, +\ell$。

**Step 1 — Commutation relations.** In 3D, $\hat{L} = \hat{r}\times\hat{p}$, so $\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y$, etc. Using $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$:

**第 1 步 — 对易关系。** 在三维中，$\hat{L} = \hat{r}\times\hat{p}$，故 $\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y$ 等。利用 $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$：

$$ \begin{aligned} [\hat{L}_x, \hat{L}_y] &= [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y,\, \hat{z}\hat{p}_x - \hat{x}\hat{p}_z] \\ &= \hat{y}\hat{p}_x[\hat{p}_z, \hat{z}] + \hat{x}\hat{p}_y[\hat{z}, \hat{p}_z] \\ &= \hat{y}\hat{p}_x(-i\hbar) + \hat{x}\hat{p}_y(i\hbar) \\ &= i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\hat{L}_z. \end{aligned} $$

Similarly: $[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$, $[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$.

类似地：$[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$，$[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$。

From these: $[\hat{L}^2, \hat{L}_z] = 0$ (and similarly $[\hat{L}^2, \hat{L}_x] = [\hat{L}^2, \hat{L}_y] = 0$), since:

由此：$[\hat{L}^2, \hat{L}_z] = 0$（同理 $[\hat{L}^2, \hat{L}_x] = [\hat{L}^2, \hat{L}_y] = 0$），因为：

$$ \begin{aligned} [\hat{L}^2, \hat{L}_z] &= [\hat{L}_x^2+\hat{L}_y^2+\hat{L}_z^2, \hat{L}_z] = \hat{L}_x[\hat{L}_x,\hat{L}_z]+[\hat{L}_x,\hat{L}_z]\hat{L}_x + \hat{L}_y[\hat{L}_y,\hat{L}_z]+[\hat{L}_y,\hat{L}_z]\hat{L}_y \\ &= \hat{L}_x(-i\hbar\hat{L}_y)+(-i\hbar\hat{L}_y)\hat{L}_x + \hat{L}_y(i\hbar\hat{L}_x)+(i\hbar\hat{L}_x)\hat{L}_y = 0. \end{aligned} $$

Therefore $\hat{L}^2$ and $\hat{L}_z$ have simultaneous eigenstates $|\ell,m\rangle$.

因此 $\hat{L}^2$ 和 $\hat{L}_z$ 有同时本征态 $|\ell,m\rangle$。

**Step 2 — Define ladder operators.** Let $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$. Key commutators:

**第 2 步 — 定义升降算符。** 令 $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$。关键对易子：

$$ [\hat{L}_z, \hat{L}_\pm] = [\hat{L}_z, \hat{L}_x] \pm i[\hat{L}_z, \hat{L}_y] = i\hbar\hat{L}_y \pm i(-i\hbar\hat{L}_x) = \pm\hbar\hat{L}_\pm. $$

$$ [\hat{L}^2, \hat{L}_\pm] = 0. $$

**Step 3 — Ladder action on eigenstates.** Let $\hat{L}^2|\ell,m\rangle = \lambda|\ell,m\rangle$ and $\hat{L}_z|\ell,m\rangle = m\hbar|\ell,m\rangle$. From $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$:

**第 3 步 — 升降算符对本征态的作用。** 设 $\hat{L}^2|\ell,m\rangle = \lambda|\ell,m\rangle$，$\hat{L}_z|\ell,m\rangle = m\hbar|\ell,m\rangle$。由 $[\hat{L}_z, \hat{L}_+] = \hbar\hat{L}_+$：

$$ \hat{L}_z(\hat{L}_+|\ell,m\rangle) = (\hat{L}_+\hat{L}_z + \hbar\hat{L}_+)|\ell,m\rangle = (m\hbar + \hbar)(\hat{L}_+|\ell,m\rangle) = (m+1)\hbar\,(\hat{L}_+|\ell,m\rangle). $$

So $\hat{L}_+|\ell,m\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $(m+1)\hbar$. Similarly $\hat{L}_-|\ell,m\rangle$ has eigenvalue $(m-1)\hbar$. Also $[\hat{L}^2, \hat{L}_\pm] = 0$ confirms that $\hat{L}_\pm|\ell,m\rangle$ still has $\hat{L}^2$ eigenvalue $\lambda$.

故 $\hat{L}_+|\ell,m\rangle$ 是 $\hat{L}_z$ 的本征态，本征值为 $(m+1)\hbar$。类似地 $\hat{L}_-|\ell,m\rangle$ 的本征值为 $(m-1)\hbar$。还有 $[\hat{L}^2, \hat{L}_\pm] = 0$ 确认 $\hat{L}_\pm|\ell,m\rangle$ 仍有 $\hat{L}^2$ 本征值 $\lambda$。

**Step 4 — Bound on $m$.** The operator $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$ is a sum of squares of Hermitian operators:

**第 4 步 — $m$ 的上下界。** 算符 $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$ 是厄米算符的平方和：

$$ \langle\ell,m|\hat{L}^2-\hat{L}_z^2|\ell,m\rangle = \langle\ell,m|\hat{L}_x^2+\hat{L}_y^2|\ell,m\rangle \ge 0. $$

$$ \implies \lambda - m^2\hbar^2 \ge 0 \implies |m| \le \sqrt{\lambda}/\hbar. $$

So $m$ is bounded. Let $m_{\max}$ be the maximum value. Since $\hat{L}_+|\ell,m_{\max}\rangle$ must be zero (no higher $m$ exists):

故 $m$ 有界。设 $m_{\max}$ 为最大值。由于 $\hat{L}_+|\ell,m_{\max}\rangle$ 必须为零（不存在更高的 $m$）：

$$ \hat{L}_-\hat{L}_+|\ell,m_{\max}\rangle = 0. $$

Expand $\hat{L}_-\hat{L}_+ = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z$ (using $\hat{L}_\pm\hat{L}_\mp = \hat{L}^2 - \hat{L}_z^2 \mp \hbar\hat{L}_z$):

展开 $\hat{L}_-\hat{L}_+ = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z$（利用 $\hat{L}_\pm\hat{L}_\mp = \hat{L}^2 - \hat{L}_z^2 \mp \hbar\hat{L}_z$）：

$$ (\hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z)|\ell,m_{\max}\rangle = (\lambda - m_{\max}^2\hbar^2 - m_{\max}\hbar^2)|\ell,m_{\max}\rangle = 0. $$

$$ \lambda = m_{\max}(m_{\max} + 1)\hbar^2. $$

Set $m_{\max} = \ell$: $\lambda = \hbar^2\ell(\ell+1)$. Similarly, with $\hat{L}_-|\ell,m_{\min}\rangle = 0$: $\lambda = m_{\min}(m_{\min} - 1)\hbar^2$, giving $m_{\min} = -\ell$. The ladder from $m_{\min}$ to $m_{\max}$ takes integer steps, so $\ell$ must be a non-negative integer or half-integer (orbital: integer; spin: half-integer). For orbital angular momentum, single-valuedness of $Y_\ell^m$ fixes $\ell = 0, 1, 2, \ldots$ and $m = -\ell, -\ell+1, \ldots, \ell$. $\blacksquare$

令 $m_{\max} = \ell$：$\lambda = \hbar^2\ell(\ell+1)$。类似地，由 $\hat{L}_-|\ell,m_{\min}\rangle = 0$ 得 $\lambda = m_{\min}(m_{\min} - 1)\hbar^2$，给出 $m_{\min} = -\ell$。从 $m_{\min}$ 到 $m_{\max}$ 的阶梯以整数步进，故 $\ell$ 必须是非负整数或半整数（轨道：整数；自旋：半整数）。对于轨道角动量，$Y_\ell^m$ 的单值性限制 $\ell = 0, 1, 2, \ldots$ 且 $m = -\ell, -\ell+1, \ldots, \ell$。$\blacksquare$

---

## C. Hydrogen Atom Radial Solution and $E_n = -13.6\ \text{eV} / n^2$ · 氢原子径向解与 $E_n = -13.6\ \text{eV} / n^2$

**Claim.** For the hydrogen atom $V(r) = -k_e e^2/r$, the radial Schrödinger equation (RE from Section A) with $E < 0$ has normalizable solutions only for energies $E_n = -m k_e^2 e^4/(2\hbar^2 n^2) = -13.6\ \text{eV}/n^2$, $n = 1, 2, 3, \ldots$, with $n \ge \ell+1$.

**命题。** 对于氢原子 $V(r) = -k_e e^2/r$，径向薛定谔方程（第 A 节的径向方程）在 $E < 0$ 时有可归一化解仅当 $E_n = -m k_e^2 e^4/(2\hbar^2 n^2) = -13.6\ \text{eV}/n^2$，$n = 1, 2, 3, \ldots$，$n \ge \ell+1$。

**Step 1 — Radial equation for hydrogen.** Substitute $V = -k_e e^2/r$ into (RE) and let $u(r) = r R(r)$ to remove the first-derivative term:

**第 1 步 — 氢原子的径向方程。** 将 $V = -k_e e^2/r$ 代入（径向方程），令 $u(r) = r R(r)$ 以消去一阶导数项：

$$ d^2 u/dr^2 + [2m/\hbar^2(E + k_e e^2/r) - \ell(\ell+1)/r^2]u = 0. $$

**Step 2 — Asymptotic analysis.** For $E < 0$, let $\kappa = \sqrt{-2mE}/\hbar > 0$. As $r \to \infty$ the equation approaches $d^2 u/dr^2 \approx \kappa^2 u$, giving $u \sim e^{\pm\kappa r}$. Normalizability requires $u \sim e^{-\kappa r}$.

**第 2 步 — 渐近分析。** 对于 $E < 0$，令 $\kappa = \sqrt{-2mE}/\hbar > 0$。当 $r \to \infty$ 时方程趋近于 $d^2 u/dr^2 \approx \kappa^2 u$，给出 $u \sim e^{\pm\kappa r}$。可归一化要求 $u \sim e^{-\kappa r}$。

As $r \to 0$ with $\ell \ge 1$: the $\ell(\ell+1)/r^2$ term dominates, giving $u \sim r^{\ell+1}$ or $r^{-\ell}$. Normalizability requires $u \sim r^{\ell+1}$.

当 $r \to 0$ 且 $\ell \ge 1$ 时：$\ell(\ell+1)/r^2$ 项主导，给出 $u \sim r^{\ell+1}$ 或 $r^{-\ell}$。可归一化要求 $u \sim r^{\ell+1}$。

**Step 3 — Power series / Laguerre polynomial solution.** Factor out the asymptotic behavior: $u(r) = r^{\ell+1} e^{-\kappa r} v(r)$. Substituting into the equation gives a differential equation for $v(r)$ that, in terms of the variable $\rho = 2\kappa r$, becomes the **associated Laguerre equation**:

**第 3 步 — 幂级数/拉盖尔多项式解。** 提取渐近行为：$u(r) = r^{\ell+1} e^{-\kappa r} v(r)$。代入方程，用变量 $\rho = 2\kappa r$，得到关于 $v(r)$ 的**连带拉盖尔方程**：

$$ \rho v'' + (2\ell+2-\rho) v' + [n-(\ell+1)] v = 0, $$

where $n$ is defined by $n = k_e e^2 m/(\hbar^2\kappa)$ (this is the parameter). The series solution for $v$ terminates (giving a polynomial) if and only if $n - (\ell+1) = n_r$ is a non-negative integer ($n_r = 0, 1, 2, \ldots$ is the radial quantum number). When the series does not terminate, $v$ grows like $e^\rho$, making $u$ non-normalizable.

其中 $n$ 由 $n = k_e e^2 m/(\hbar^2\kappa)$ 定义（这是参数）。$v$ 的级数解终止（给出多项式）当且仅当 $n - (\ell+1) = n_r$ 为非负整数（$n_r = 0, 1, 2, \ldots$ 是径向量子数）。当级数不终止时，$v$ 的增长如 $e^\rho$，使 $u$ 不可归一化。

**Step 4 — Energy quantization.** From $n = k_e e^2 m/(\hbar^2\kappa)$ and $\kappa = \sqrt{-2mE}/\hbar$:

**第 4 步 — 能量量子化。** 由 $n = k_e e^2 m/(\hbar^2\kappa)$ 和 $\kappa = \sqrt{-2mE}/\hbar$：

$$ \kappa = m k_e e^2/(n\hbar^2), $$

$$ E = -\hbar^2\kappa^2/(2m) = -\hbar^2/(2m)\cdot m^2 k_e^2 e^4/(n^2\hbar^4) = \boxed{\,-m k_e^2 e^4/(2n^2\hbar^2)\,}. $$

Numerically: $E_n = -13.6\ \text{eV} / n^2$, $n = 1, 2, 3, \ldots$ The constraint $n \ge \ell+1$ means: for $n = 1$, only $\ell = 0$; for $n = 2$, $\ell = 0$ or $1$; etc. This gives the degeneracy $g(n) = \sum_{\ell=0}^{n-1}(2\ell+1) = n^2$. $\blacksquare$

数值上：$E_n = -13.6\ \text{eV} / n^2$，$n = 1, 2, 3, \ldots$。约束 $n \ge \ell+1$ 意味着：$n = 1$ 时只有 $\ell = 0$；$n = 2$ 时 $\ell = 0$ 或 $1$；等等。这给出简并度 $g(n) = \sum_{\ell=0}^{n-1}(2\ell+1) = n^2$。$\blacksquare$

---

## D. Spin-$\tfrac12$: Pauli Matrices and $S_z$ Eigenvalues · 自旋-$\tfrac12$：泡利矩阵与 $S_z$ 本征值

**Claim.** For a spin-$\tfrac12$ particle, the spin operators $\hat{S}_i = (\hbar/2)\sigma_i$ satisfy the angular-momentum algebra $[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z$ (etc.), and $S_z$ has eigenvalues $\pm\hbar/2$ with eigenstates $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$.

**命题。** 对自旋-$\tfrac12$ 粒子，自旋算符 $\hat{S}_i = (\hbar/2)\sigma_i$ 满足角动量代数 $[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z$（等），$S_z$ 的本征值为 $\pm\hbar/2$，本征态为 $|\!\uparrow\rangle$ 和 $|\!\downarrow\rangle$。

**Step 1 — General spin-$\tfrac12$ state space.** By the angular-momentum algebra of Section B (which applies equally to half-integer spin), for $s = \tfrac12$ we have $S^2$ eigenvalue $\hbar^2\cdot\tfrac12\cdot(\tfrac12+1) = 3\hbar^2/4$, and $m_s = \pm\tfrac12$. The state space is 2-dimensional; choose basis $\{|\!\uparrow\rangle, |\!\downarrow\rangle\} = \{|s=\tfrac12,m=+\tfrac12\rangle, |s=\tfrac12,m=-\tfrac12\rangle\}$.

**第 1 步 — 一般自旋-$\tfrac12$ 态空间。** 由第 B 节的角动量代数（同样适用于半整数自旋），对 $s = \tfrac12$ 有 $S^2$ 本征值 $\hbar^2\cdot\tfrac12\cdot(\tfrac12+1) = 3\hbar^2/4$，$m_s = \pm\tfrac12$。态空间是二维的；选取基 $\{|\!\uparrow\rangle, |\!\downarrow\rangle\} = \{|s=\tfrac12,m=+\tfrac12\rangle, |s=\tfrac12,m=-\tfrac12\rangle\}$。

**Step 2 — Matrix representations.** In this basis, the matrix elements of $S_z$ are diagonal (since these are eigenstates):

**第 2 步 — 矩阵表示。** 在此基中，$S_z$ 的矩阵元是对角的（因为这些是本征态）：

$$ S_z = \frac{\hbar}{2}\,(|\!\uparrow\rangle\langle\uparrow\!| - |\!\downarrow\rangle\langle\downarrow\!|) = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. $$

For $S_\pm$, from Section B: $\hat{S}_+|\!\downarrow\rangle = \hbar|\!\uparrow\rangle$, $\hat{S}_+|\!\uparrow\rangle = 0$; $\hat{S}_-|\!\uparrow\rangle = \hbar|\!\downarrow\rangle$, $\hat{S}_-|\!\downarrow\rangle = 0$. (Norm factor: $\sqrt{s(s+1)-m(m\pm1)} = \sqrt{3/4-(-1/2)(1/2)} = 1$ for $\ell=\tfrac12$ states.) Therefore:

对于 $S_\pm$，由第 B 节：$\hat{S}_+|\!\downarrow\rangle = \hbar|\!\uparrow\rangle$，$\hat{S}_+|\!\uparrow\rangle = 0$；$\hat{S}_-|\!\uparrow\rangle = \hbar|\!\downarrow\rangle$，$\hat{S}_-|\!\downarrow\rangle = 0$。因此：

$$ S_x = (S_+ + S_-)/2 = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad S_y = (S_+ - S_-)/(2i) = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}. $$

**Step 3 — Pauli matrices.** Define $\sigma_i$ by $\hat{S}_i = (\hbar/2)\sigma_i$:

**第 3 步 — 泡利矩阵。** 由 $\hat{S}_i = (\hbar/2)\sigma_i$ 定义 $\sigma_i$：

$$ \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. $$

**Step 4 — Verify the algebra.** $[\hat{S}_x, \hat{S}_y] = (\hbar^2/4)[\sigma_x, \sigma_y]$:

**第 4 步 — 验证代数关系。** $[\hat{S}_x, \hat{S}_y] = (\hbar^2/4)[\sigma_x, \sigma_y]$：

$$ \begin{aligned} [\sigma_x, \sigma_y] &= \sigma_x\sigma_y - \sigma_y\sigma_x \\ &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} - \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \\ &= \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} - \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \\ &= \begin{pmatrix} 2i & 0 \\ 0 & -2i \end{pmatrix} = 2i\,\sigma_z. \end{aligned} $$

Therefore $[\hat{S}_x, \hat{S}_y] = (\hbar^2/4)\cdot2i\sigma_z = i\hbar\cdot(\hbar/2)\sigma_z = i\hbar\hat{S}_z$. $\checkmark$

因此 $[\hat{S}_x, \hat{S}_y] = (\hbar^2/4)\cdot2i\sigma_z = i\hbar\cdot(\hbar/2)\sigma_z = i\hbar\hat{S}_z$。$\checkmark$

**Step 5 — $S_z$ eigenvalues.** $S_z = (\hbar/2)\sigma_z$ has eigenvalues $(\hbar/2)\cdot(\pm1) = \pm\hbar/2$, with eigenvectors $\begin{pmatrix} 1 \\ 0 \end{pmatrix} = |\!\uparrow\rangle$ (eigenvalue $+\hbar/2$, "spin up") and $\begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle$ (eigenvalue $-\hbar/2$, "spin down"). $\blacksquare$

**第 5 步 — $S_z$ 本征值。** $S_z = (\hbar/2)\sigma_z$ 的本征值为 $(\hbar/2)\cdot(\pm1) = \pm\hbar/2$，本征向量分别为 $\begin{pmatrix} 1 \\ 0 \end{pmatrix} = |\!\uparrow\rangle$（本征值 $+\hbar/2$，"自旋向上"）和 $\begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle$（本征值 $-\hbar/2$，"自旋向下"）。$\blacksquare$

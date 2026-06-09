---
title: "Derivations — Module 1.20: Canonical Transformations, Hamilton–Jacobi & Action–Angle"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 1.20: Canonical Transformations, Hamilton–Jacobi & Action–Angle
# 推导 — 模块 1.20：正则变换、哈密顿–雅可比与作用量–角变量

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.20](./module-1.20-canonical-transformations-hamilton-jacobi.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.20](./module-1.20-canonical-transformations-hamilton-jacobi.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Generating Functions and the Four Types · 生成函数与四种类型

**Claim.** A transformation $(q, p) \to (Q, P)$ is canonical iff it preserves the form of Hamilton's equations, which is guaranteed by requiring $p\,dq - H\,dt = P\,dQ - K\,dt + dF$ for some generating function $F$. The type-1 function $F_1(q, Q, t)$ gives $p = \partial F_1/\partial q$, $P = -\partial F_1/\partial Q$, $K = H + \partial F_1/\partial t$; the type-2 function $F_2(q, P, t) = F_1 + QP$ gives $p = \partial F_2/\partial q$, $Q = \partial F_2/\partial P$, $K = H + \partial F_2/\partial t$. The choice $F_2 = qP$ generates the identity transformation.

**命题。** 变换 $(q, p) \to (Q, P)$ 是正则的，当且仅当它保持哈密顿方程的形式不变；这由要求 $p\,dq - H\,dt = P\,dQ - K\,dt + dF$（$F$ 为某生成函数）保证。第一类函数 $F_1(q, Q, t)$ 给出 $p = \partial F_1/\partial q$，$P = -\partial F_1/\partial Q$，$K = H + \partial F_1/\partial t$；第二类函数 $F_2(q, P, t) = F_1 + QP$ 给出 $p = \partial F_2/\partial q$，$Q = \partial F_2/\partial P$，$K = H + \partial F_2/\partial t$。取 $F_2 = qP$ 生成恒等变换。

**Step 1 — The variational principle fixes the integrand up to a total differential.** Hamilton's equations for $(q, p)$ with Hamiltonian $H$ follow from the modified Hamilton's principle (Module 1.3) $\delta\int(p\dot{q} - H)\,dt = 0$. For the new coordinates $(Q, P)$ to obey Hamilton's equations with a new Hamiltonian $K$, we likewise need $\delta\int(P\dot{Q} - K)\,dt = 0$. Both variational principles hold simultaneously iff the two integrands differ by the total time derivative of a function $F$, since an endpoint-fixed total derivative contributes nothing to the variation:

**第 1 步 — 变分原理把被积函数确定到一个全微分。** 以哈密顿量 $H$ 描述 $(q, p)$ 的哈密顿方程来自修正的哈密顿原理（模块 1.3）$\delta\int(p\dot{q} - H)\,dt = 0$。要使新坐标 $(Q, P)$ 服从以新哈密顿量 $K$ 描述的哈密顿方程，同样需要 $\delta\int(P\dot{Q} - K)\,dt = 0$。两个变分原理同时成立，当且仅当两被积函数相差某函数 $F$ 的全时间导数——因为端点固定的全导数对变分无贡献：

$$ p\dot{q} - H = P\dot{Q} - K + \frac{dF}{dt}. $$

Multiplying by $dt$ gives the differential form

两边乘 $dt$ 得微分形式

$$ p\,dq - H\,dt = P\,dQ - K\,dt + dF. $$

**Step 2 — Type 1: $F = F_1(q, Q, t)$.** Choose the independent variables to be the old and new coordinates $(q, Q)$. Then $dF_1 = (\partial F_1/\partial q)\,dq + (\partial F_1/\partial Q)\,dQ + (\partial F_1/\partial t)\,dt$. Substituting into the form from Step 1 and rearranging:

**第 2 步 — 第一类：$F = F_1(q, Q, t)$。** 取独立变量为新旧坐标 $(q, Q)$。则 $dF_1 = (\partial F_1/\partial q)\,dq + (\partial F_1/\partial Q)\,dQ + (\partial F_1/\partial t)\,dt$。代入第 1 步的形式并整理：

$$ p\,dq - P\,dQ + (K - H)\,dt = \frac{\partial F_1}{\partial q}\,dq + \frac{\partial F_1}{\partial Q}\,dQ + \frac{\partial F_1}{\partial t}\,dt. $$

Since $q, Q, t$ are independent, the coefficients of $dq, dQ, dt$ must match separately:

由于 $q$、$Q$、$t$ 独立，$dq$、$dQ$、$dt$ 的系数必须分别相等：

$$ p = \frac{\partial F_1}{\partial q}, \qquad P = -\frac{\partial F_1}{\partial Q}, \qquad K = H + \frac{\partial F_1}{\partial t}. $$

The first two relations, solved together, express $(Q, P)$ in terms of $(q, p)$: $F_1$ generates the transformation.

前两个关系联立求解，把 $(Q, P)$ 用 $(q, p)$ 表示：$F_1$ 生成该变换。

**Step 3 — Type 2 by Legendre transform: $F_2(q, P, t) = F_1 + QP$.** When the natural variables are $(q, P)$ rather than $(q, Q)$, pass to a new generator by a Legendre transform in the pair $(Q, P)$. Define $F_2 = F_1 + QP$. Then

**第 3 步 — 由勒让德变换得第二类：$F_2(q, P, t) = F_1 + QP$。** 当自然变量为 $(q, P)$ 而非 $(q, Q)$ 时，对 $(Q, P)$ 这一对作勒让德变换得到新生成函数。定义 $F_2 = F_1 + QP$。则

$$ dF_2 = dF_1 + Q\,dP + P\,dQ. $$

Using $dF_1 = p\,dq - P\,dQ + (K - H)\,dt$ from Step 2, the $P\,dQ$ terms cancel:

利用第 2 步的 $dF_1 = p\,dq - P\,dQ + (K - H)\,dt$，$P\,dQ$ 项相消：

$$ dF_2 = p\,dq + Q\,dP + (K - H)\,dt. $$

Reading off the coefficients of $dq, dP, dt$:

读出 $dq$、$dP$、$dt$ 的系数：

$$ p = \frac{\partial F_2}{\partial q}, \qquad Q = \frac{\partial F_2}{\partial P}, \qquad K = H + \frac{\partial F_2}{\partial t}. $$

**Step 4 — $F_2 = qP$ generates the identity.** Take $F_2(q, P) = qP$ (no explicit $t$). Apply the Step 3 relations:

**第 4 步 — $F_2 = qP$ 生成恒等变换。** 取 $F_2(q, P) = qP$（不显含 $t$）。应用第 3 步关系：

$$ p = \frac{\partial F_2}{\partial q} = P, \qquad Q = \frac{\partial F_2}{\partial P} = q, \qquad K = H + 0 = H. $$

Hence $Q = q$ and $P = p$ with $K = H$: the **identity transformation**. This confirms the bookkeeping of the relations is internally consistent. (More generally $F_2 = \sum_k f_k(q) P_k$ gives $Q_k = f_k(q)$, an arbitrary point transformation of configuration space, with momenta transforming contragrediently.) $\blacksquare$

故 $Q = q$、$P = p$ 且 $K = H$：即**恒等变换**。这验证了上述关系的记账是自洽的。（更一般地 $F_2 = \sum_k f_k(q) P_k$ 给出 $Q_k = f_k(q)$，即位形空间的任意点变换，动量按逆变方式变换。）$\blacksquare$

---

## B. Symplectic Condition and Poisson-Bracket Invariance · 辛条件与泊松括号不变性

**Claim.** Collect the phase-space coordinates into a column $\xi = (q_1,\dots,q_n, p_1,\dots,p_n)^{\mathsf T}$ and let $J$ be the $2n\times 2n$ symplectic matrix $J = \begin{bmatrix} 0 & I \\ -I & 0 \end{bmatrix}$. A (time-independent) transformation $\xi \to \eta(\xi)$ is canonical iff its Jacobian $M_{ij} = \partial\eta_i/\partial\xi_j$ satisfies the **symplectic condition** $M^{\mathsf T} J M = J$. Equivalently, the fundamental Poisson brackets are preserved: $\{Q_i, P_j\} = \delta_{ij}$, $\{Q_i, Q_j\} = \{P_i, P_j\} = 0$. Poisson brackets of any pair of functions are canonical invariants.

**命题。** 将相空间坐标排成列 $\xi = (q_1,\dots,q_n, p_1,\dots,p_n)^{\mathsf T}$，令 $J$ 为 $2n\times 2n$ 辛矩阵 $J = \begin{bmatrix} 0 & I \\ -I & 0 \end{bmatrix}$。一个（不含时）变换 $\xi \to \eta(\xi)$ 是正则的，当且仅当其雅可比矩阵 $M_{ij} = \partial\eta_i/\partial\xi_j$ 满足**辛条件** $M^{\mathsf T} J M = J$。等价地，基本泊松括号保持不变：$\{Q_i, P_j\} = \delta_{ij}$，$\{Q_i, Q_j\} = \{P_i, P_j\} = 0$。任意一对函数的泊松括号都是正则不变量。

**Step 1 — Hamilton's equations in symplectic form.** With $\xi = (q, p)^{\mathsf T}$, Hamilton's equations $\dot{q}_i = \partial H/\partial p_i$, $\dot{p}_i = -\partial H/\partial q_i$ collapse to the single compact equation

**第 1 步 — 辛形式的哈密顿方程。** 以 $\xi = (q, p)^{\mathsf T}$，哈密顿方程 $\dot{q}_i = \partial H/\partial p_i$，$\dot{p}_i = -\partial H/\partial q_i$ 收缩为单一紧凑方程

$$ \dot{\xi} = J\,\frac{\partial H}{\partial\xi}, $$

where $\partial H/\partial\xi$ is the gradient column $(\partial H/\partial q, \partial H/\partial p)^{\mathsf T}$. One checks the upper block gives $\dot{q} = +\partial H/\partial p$ and the lower block gives $\dot{p} = -\partial H/\partial q$, matching Hamilton's equations.

其中 $\partial H/\partial\xi$ 是梯度列 $(\partial H/\partial q, \partial H/\partial p)^{\mathsf T}$。验证上块给出 $\dot{q} = +\partial H/\partial p$，下块给出 $\dot{p} = -\partial H/\partial q$，与哈密顿方程一致。

**Step 2 — Transform the equations of motion.** Let $\eta = \eta(\xi)$ with Jacobian $M_{ij} = \partial\eta_i/\partial\xi_j$. By the chain rule $\dot{\eta} = M\dot{\xi} = M J\,\partial H/\partial\xi$. The gradient transforms as $\partial H/\partial\xi = M^{\mathsf T}\,\partial H/\partial\eta$ (since $\partial H/\partial\xi_j = \sum_i (\partial\eta_i/\partial\xi_j)(\partial H/\partial\eta_i) = (M^{\mathsf T}\,\partial H/\partial\eta)_j$). Therefore

**第 2 步 — 变换运动方程。** 令 $\eta = \eta(\xi)$，雅可比 $M_{ij} = \partial\eta_i/\partial\xi_j$。由链式法则 $\dot{\eta} = M\dot{\xi} = M J\,\partial H/\partial\xi$。梯度变换为 $\partial H/\partial\xi = M^{\mathsf T}\,\partial H/\partial\eta$（因 $\partial H/\partial\xi_j = \sum_i (\partial\eta_i/\partial\xi_j)(\partial H/\partial\eta_i) = (M^{\mathsf T}\,\partial H/\partial\eta)_j$）。故

$$ \dot{\eta} = M J M^{\mathsf T}\,\frac{\partial H}{\partial\eta}. $$

**Step 3 — The symplectic condition.** The new variables obey Hamilton's equations with the same Hamiltonian, $\dot{\eta} = J\,\partial H/\partial\eta$, for **every** $H$ iff $M J M^{\mathsf T} = J$. This is equivalent to the standard form $M^{\mathsf T} J M = J$: multiply $M J M^{\mathsf T} = J$ on the left by $M^{-1}$ and on the right by $(M^{\mathsf T})^{-1}$ to get $J = M^{-1} J (M^{\mathsf T})^{-1}$, then invert using $J^{-1} = -J = J^{\mathsf T}$ to recover $M^{\mathsf T} J M = J$.

**第 3 步 — 辛条件。** 新变量对**每个** $H$ 都服从以同一哈密顿量描述的哈密顿方程 $\dot{\eta} = J\,\partial H/\partial\eta$，当且仅当 $M J M^{\mathsf T} = J$。这等价于标准形式 $M^{\mathsf T} J M = J$：把 $M J M^{\mathsf T} = J$ 左乘 $M^{-1}$、右乘 $(M^{\mathsf T})^{-1}$ 得 $J = M^{-1} J (M^{\mathsf T})^{-1}$，再用 $J^{-1} = -J = J^{\mathsf T}$ 求逆即得 $M^{\mathsf T} J M = J$。

$$ M^{\mathsf T} J M = J \qquad \text{(symplectic condition).} $$

A matrix satisfying this is called symplectic; the transformation it generates is canonical.

满足此条件的矩阵称为辛矩阵；它生成的变换是正则的。

**Step 4 — Equivalence with fundamental Poisson brackets.** The Poisson bracket of two phase-space functions $f, g$ is $\{f, g\} = \sum_i (\partial f/\partial q_i\,\partial g/\partial p_i - \partial f/\partial p_i\,\partial g/\partial q_i)$, which in symplectic notation is $\{f, g\} = (\partial f/\partial\xi)^{\mathsf T} J (\partial g/\partial\xi)$ (Module 1.4). Apply this to the new coordinates $\eta = (Q, P)$ as functions of $\xi$. Their matrix of mutual brackets is

**第 4 步 — 与基本泊松括号的等价性。** 两个相空间函数 $f$、$g$ 的泊松括号为 $\{f, g\} = \sum_i (\partial f/\partial q_i\,\partial g/\partial p_i - \partial f/\partial p_i\,\partial g/\partial q_i)$，用辛记号即 $\{f, g\} = (\partial f/\partial\xi)^{\mathsf T} J (\partial g/\partial\xi)$（模块 1.4）。把它用于作为 $\xi$ 的函数的新坐标 $\eta = (Q, P)$。它们相互括号的矩阵为

$$ \{\eta_i, \eta_j\} = \sum_{k,l} \frac{\partial\eta_i}{\partial\xi_k} J_{kl} \frac{\partial\eta_j}{\partial\xi_l} = (M J M^{\mathsf T})_{ij}. $$

By Step 3 the transformation is canonical iff $M J M^{\mathsf T} = J$, i.e. iff $\{\eta_i, \eta_j\} = J_{ij}$. Reading off the blocks of $J$, this is precisely

由第 3 步，变换正则当且仅当 $M J M^{\mathsf T} = J$，即 $\{\eta_i, \eta_j\} = J_{ij}$。读出 $J$ 的分块，这恰为

$$ \{Q_i, P_j\} = \delta_{ij}, \qquad \{Q_i, Q_j\} = 0, \qquad \{P_i, P_j\} = 0. $$

**Step 5 — Poisson brackets are canonical invariants.** Let $f, g$ be any functions and compute their bracket in the new variables. Using $\{f, g\}_\eta = (\partial f/\partial\eta)^{\mathsf T} J (\partial g/\partial\eta)$ and the chain rule $\partial f/\partial\xi = M^{\mathsf T}\,\partial f/\partial\eta$:

**第 5 步 — 泊松括号是正则不变量。** 设 $f$、$g$ 为任意函数，在新变量下计算其括号。用 $\{f, g\}_\eta = (\partial f/\partial\eta)^{\mathsf T} J (\partial g/\partial\eta)$ 及链式法则 $\partial f/\partial\xi = M^{\mathsf T}\,\partial f/\partial\eta$：

$$ \{f, g\}_\xi = \left(\frac{\partial f}{\partial\xi}\right)^{\mathsf T} J \frac{\partial g}{\partial\xi} = \left(\frac{\partial f}{\partial\eta}\right)^{\mathsf T} M J M^{\mathsf T} \frac{\partial g}{\partial\eta} = \left(\frac{\partial f}{\partial\eta}\right)^{\mathsf T} J \frac{\partial g}{\partial\eta} = \{f, g\}_\eta, $$

where the middle equality used $M J M^{\mathsf T} = J$. Hence the Poisson bracket of any two functions is the same computed in $(q, p)$ or in $(Q, P)$: it is a **canonical invariant**. This bracket structure is exactly what survives quantization, $\{q, p\} = 1 \to [\hat{q}, \hat{p}] = i\hbar$ (Module 3.3). $\blacksquare$

其中中间等式用了 $M J M^{\mathsf T} = J$。故任意两函数的泊松括号在 $(q, p)$ 与 $(Q, P)$ 下计算结果相同：它是**正则不变量**。这一括号结构正是量子化后保留下来的部分，$\{q, p\} = 1 \to [\hat{q}, \hat{p}] = i\hbar$（模块 3.3）。$\blacksquare$

---

## C. The Hamilton–Jacobi Equation · 哈密顿–雅可比方程

**Claim.** Seek a type-2 generating function $F_2 = S(q, P, t)$ that makes the new Hamiltonian $K \equiv 0$. Then $p = \partial S/\partial q$ and $S$ satisfies the **Hamilton–Jacobi equation** $H(q, \partial S/\partial q, t) + \partial S/\partial t = 0$. $S$ is Hamilton's principal function and equals the action. For time-independent $H$ the ansatz $S = W(q, \alpha) - Et$ separates the equation into the time-independent HJ equation $H(q, \partial W/\partial q) = E$, with $W$ Hamilton's characteristic function. The new constant momenta $\alpha$ are conserved, and the equations $\beta = \partial S/\partial\alpha = \text{const}$ determine the trajectory.

**命题。** 寻求一个第二类生成函数 $F_2 = S(q, P, t)$ 使新哈密顿量 $K \equiv 0$。则 $p = \partial S/\partial q$，且 $S$ 满足**哈密顿–雅可比方程** $H(q, \partial S/\partial q, t) + \partial S/\partial t = 0$。$S$ 是哈密顿主函数，等于作用量。对不含时 $H$，拟设 $S = W(q, \alpha) - Et$ 把方程分离为不含时 HJ 方程 $H(q, \partial W/\partial q) = E$，其中 $W$ 为哈密顿特征函数。新的常数动量 $\alpha$ 守恒，方程 $\beta = \partial S/\partial\alpha = \text{常数}$ 确定轨迹。

**Step 1 — Demand $K = 0$.** Use a type-2 generator $S(q, P, t)$. From Section A the type-2 relations are $p = \partial S/\partial q$, $Q = \partial S/\partial P$, and $K = H + \partial S/\partial t$. Impose the strongest possible simplification: choose $S$ so that the new Hamiltonian vanishes identically,

**第 1 步 — 要求 $K = 0$。** 使用第二类生成函数 $S(q, P, t)$。由 A 节，第二类关系为 $p = \partial S/\partial q$，$Q = \partial S/\partial P$，$K = H + \partial S/\partial t$。施加最强的简化：选取 $S$ 使新哈密顿量恒等于零，

$$ K = H(q, p, t) + \frac{\partial S}{\partial t} = 0. $$

**Step 2 — Substitute $p = \partial S/\partial q$.** Replacing every momentum $p$ by $\partial S/\partial q$ turns $K = 0$ into a first-order PDE for the single function $S(q, P, t)$:

**第 2 步 — 代入 $p = \partial S/\partial q$。** 把每个动量 $p$ 替换为 $\partial S/\partial q$，$K = 0$ 变为关于单一函数 $S(q, P, t)$ 的一阶偏微分方程：

$$ H\!\left(q, \frac{\partial S}{\partial q}, t\right) + \frac{\partial S}{\partial t} = 0 \qquad \text{(Hamilton–Jacobi equation).} $$

A complete integral $S(q, \alpha_1,\dots,\alpha_n, t)$ depends on $n$ independent constants $\alpha$ (identified with the new constant momenta $P = \alpha$). The new Hamiltonian being zero means, via Hamilton's equations, $\dot{P} = -\partial K/\partial Q = 0$ and $\dot{Q} = +\partial K/\partial P = 0$: **both** the new momenta $\alpha = P$ and the new coordinates $\beta = Q$ are constants of the motion.

完全积分 $S(q, \alpha_1,\dots,\alpha_n, t)$ 依赖 $n$ 个独立常数 $\alpha$（与新常数动量 $P = \alpha$ 等同）。新哈密顿量为零意味着由哈密顿方程 $\dot{P} = -\partial K/\partial Q = 0$、$\dot{Q} = +\partial K/\partial P = 0$：新动量 $\alpha = P$ 与新坐标 $\beta = Q$ **都**是运动常数。

**Step 3 — $S$ equals the action.** Along an actual trajectory compute the total time derivative of $S(q, \alpha, t)$:

**第 3 步 — $S$ 等于作用量。** 沿真实轨迹计算 $S(q, \alpha, t)$ 的全时间导数：

$$ \frac{dS}{dt} = \frac{\partial S}{\partial q}\cdot\dot{q} + \frac{\partial S}{\partial t} = p\dot{q} + \frac{\partial S}{\partial t}. $$

By the HJ equation $\partial S/\partial t = -H$, so $dS/dt = p\dot{q} - H = L$, the Lagrangian (Module 1.3). Integrating,

由 HJ 方程 $\partial S/\partial t = -H$，故 $dS/dt = p\dot{q} - H = L$，即拉格朗日量（模块 1.3）。积分得

$$ S = \int L\,dt + \text{const}, $$

so $S$ is exactly the classical **action** evaluated along the trajectory — Hamilton's principal function.

故 $S$ 正是沿轨迹计算的经典**作用量**——哈密顿主函数。

**Step 4 — Separation of time for time-independent $H$.** If $H$ does not depend explicitly on $t$, the $t$-dependence of $S$ separates additively. Try the ansatz

**第 4 步 — 不含时 $H$ 的时间分离。** 若 $H$ 不显含 $t$，则 $S$ 的 $t$ 依赖以相加方式分离。试拟设

$$ S(q, \alpha, t) = W(q, \alpha) - E t, $$

where $E$ is one of the constants $\alpha$ (say $\alpha_1 = E$). Then $\partial S/\partial t = -E$ and $\partial S/\partial q = \partial W/\partial q$, so the HJ equation $H(q, \partial S/\partial q) - E = 0$ becomes the **time-independent Hamilton–Jacobi equation**

其中 $E$ 为常数 $\alpha$ 之一（设 $\alpha_1 = E$）。则 $\partial S/\partial t = -E$、$\partial S/\partial q = \partial W/\partial q$，HJ 方程 $H(q, \partial S/\partial q) - E = 0$ 化为**不含时哈密顿–雅可比方程**

$$ H\!\left(q, \frac{\partial W}{\partial q}\right) = E, $$

with $W(q, \alpha)$ **Hamilton's characteristic function**. The constant $E$ is the conserved energy ($H$ is time-independent, hence conserved).

其中 $W(q, \alpha)$ 为**哈密顿特征函数**。常数 $E$ 是守恒能量（$H$ 不含时，故守恒）。

**Step 5 — The constants $\alpha$ are conserved and the $\beta = \partial S/\partial\alpha$ give the trajectory.** Because $K = 0$, the conjugate coordinates are $\beta_i = Q_i = \partial S/\partial P_i = \partial S/\partial\alpha_i$, and Hamilton's equations give $\dot{\beta}_i = \partial K/\partial P_i = 0$, so each $\beta_i$ is a constant. The $n$ equations

**第 5 步 — 常数 $\alpha$ 守恒，$\beta = \partial S/\partial\alpha$ 给出轨迹。** 由于 $K = 0$，共轭坐标 $\beta_i = Q_i = \partial S/\partial P_i = \partial S/\partial\alpha_i$，哈密顿方程给出 $\dot{\beta}_i = \partial K/\partial P_i = 0$，故每个 $\beta_i$ 为常数。这 $n$ 个方程

$$ \beta_i = \frac{\partial S}{\partial\alpha_i} = \text{const} $$

are then solved algebraically for $q(t; \alpha, \beta)$. In particular the energy-conjugate equation $\beta_1 = \partial S/\partial E = \partial W/\partial E - t = \text{const}$ gives $t + \text{const} = \partial W/\partial E$, fixing the time dependence; the remaining $\beta_i = \partial W/\partial\alpha_i = \text{const}$ fix the orbit shape. Once $S$ (or $W$) is known, the entire motion follows by differentiation and algebraic inversion — no further integration of the equations of motion is needed. $\blacksquare$

随后代数地解出 $q(t; \alpha, \beta)$。特别地，能量共轭方程 $\beta_1 = \partial S/\partial E = \partial W/\partial E - t = \text{常数}$ 给出 $t + \text{常数} = \partial W/\partial E$，确定时间依赖；其余 $\beta_i = \partial W/\partial\alpha_i = \text{常数}$ 确定轨道形状。一旦 $S$（或 $W$）已知，全部运动由求导和代数反演得到——无需进一步积分运动方程。$\blacksquare$

---

## D. Action–Angle Variables and the Harmonic Oscillator · 作用量–角变量与谐振子

**Claim.** For a 1-D system with bounded periodic motion, define the **action** $J = \oint p\,dq$ (integral over one closed orbit). Using the characteristic function $W(q, J)$ with $J$ as the new (constant) momentum, the conjugate **angle** is $\theta = \partial W/\partial J$, and Hamilton's equation gives $\dot{\theta} = \partial H/\partial J \equiv \omega(J) = \text{const}$, so $\theta$ advances linearly. Over one period $\Delta\theta = 2\pi$, hence the frequency is $\nu = \omega/2\pi = \partial H/\partial J$. For the harmonic oscillator $H = p^2/2m + \tfrac12 m\omega^2 q^2$, the action is $J = \oint p\,dq = 2\pi E/\omega$, so $E = (\omega/2\pi)J$ and $\nu = \partial E/\partial J = \omega/2\pi$.

**命题。** 对作有界周期运动的一维系统，定义**作用量** $J = \oint p\,dq$（沿一条闭轨道的积分）。用以 $J$ 为新（常数）动量的特征函数 $W(q, J)$，共轭**角变量**为 $\theta = \partial W/\partial J$，哈密顿方程给出 $\dot{\theta} = \partial H/\partial J \equiv \omega(J) = \text{常数}$，故 $\theta$ 线性推进。一个周期内 $\Delta\theta = 2\pi$，故频率 $\nu = \omega/2\pi = \partial H/\partial J$。对谐振子 $H = p^2/2m + \tfrac12 m\omega^2 q^2$，作用量 $J = \oint p\,dq = 2\pi E/\omega$，故 $E = (\omega/2\pi)J$，$\nu = \partial E/\partial J = \omega/2\pi$。

**Step 1 — Define the action and use it as the new momentum.** For a 1-D time-independent system the orbit in phase space lies on the curve $H(q, p) = E$. Solving for momentum, $p = p(q, E)$, and the **action** is the loop integral (the enclosed phase-space area, Module 2.4)

**第 1 步 — 定义作用量并以其为新动量。** 对一维不含时系统，相空间轨道位于曲线 $H(q, p) = E$ 上。解出动量 $p = p(q, E)$，**作用量**为环积分（所围相空间面积，模块 2.4）

$$ J = \oint p\,dq = \oint p(q, E)\,dq. $$

This is a monotonic function $J(E)$, invertible to give $E = H(J)$. Take $J$ as the new constant momentum ($P = J$) and use the characteristic function $W(q, J)$ from Section C as the type-2 generator, with $H(q, \partial W/\partial q) = E(J)$.

这是 $E$ 的单调函数 $J(E)$，可逆得到 $E = H(J)$。取 $J$ 作新常数动量（$P = J$），用 C 节的特征函数 $W(q, J)$ 作第二类生成函数，满足 $H(q, \partial W/\partial q) = E(J)$。

**Step 2 — The conjugate angle advances at constant rate.** The coordinate conjugate to $J$ is the **angle** $\theta = \partial W/\partial J$. Since the new Hamiltonian is just $E(J)$ (independent of $\theta$), Hamilton's equation for $\theta$ reads

**第 2 步 — 共轭角以常速率推进。** 与 $J$ 共轭的坐标是**角变量** $\theta = \partial W/\partial J$。由于新哈密顿量就是 $E(J)$（与 $\theta$ 无关），$\theta$ 的哈密顿方程为

$$ \dot{\theta} = \frac{\partial E}{\partial J} \equiv \omega(J) = \text{const}, $$

a constant because $E$ depends only on $J$, not on $\theta$. Integrating, $\theta(t) = \omega t + \theta_0$: the angle increases **linearly** in time.

由于 $E$ 仅依赖 $J$ 而不依赖 $\theta$，此为常数。积分得 $\theta(t) = \omega t + \theta_0$：角随时间**线性**增加。

**Step 3 — One period gives $\Delta\theta = 2\pi$ and fixes the frequency.** Compute the change in $\theta$ as $q$ traverses one complete cycle of the orbit. Since $\theta = \partial W/\partial J$ and $\partial W/\partial q = p$,

**第 3 步 — 一个周期给出 $\Delta\theta = 2\pi$ 并确定频率。** 计算 $q$ 走完一整圈轨道时 $\theta$ 的变化。由 $\theta = \partial W/\partial J$ 及 $\partial W/\partial q = p$，

$$ \Delta\theta = \oint \frac{\partial\theta}{\partial q}\,dq = \oint \frac{\partial^2 W}{\partial q\,\partial J}\,dq = \frac{d}{dJ}\oint \frac{\partial W}{\partial q}\,dq = \frac{d}{dJ}\oint p\,dq = \frac{dJ}{dJ} = 1. $$

With the standard normalization in which the angle is measured in cycles, $J = \oint p\,dq$ is conjugate to an angle that advances by $\Delta\theta = 1$ per period; equivalently, defining the angle in radians ($\theta \to 2\pi\theta$) the convention $J = \oint p\,dq$ gives $\Delta\theta = 2\pi$ per period. Either way the per-period advance is fixed by $J = \oint p\,dq$ alone. Equating the two ways of expressing the period $T$,

由 $\theta = \partial W/\partial J$ 交换求导与环积分次序：每周期角的推进量完全由 $J = \oint p\,dq$ 固定，归一化为 $\Delta\theta = 1$（以圈计）或等价地 $\Delta\theta = 2\pi$（以弧度计，$\theta \to 2\pi\theta$）。把表达周期 $T$ 的两种方式相等，

$$ \Delta\theta = \omega T = 2\pi \implies T = 2\pi/\omega, \qquad \nu = 1/T = \omega/2\pi = \partial E/\partial J. $$

The oscillation frequency is obtained directly from $E(J)$ by differentiation — without ever solving for $q(t)$.

振荡频率直接由 $E(J)$ 求导得到——完全不必解出 $q(t)$。

**Step 4 — Worked example: the harmonic oscillator.** Take $H = p^2/2m + \tfrac12 m\omega^2 q^2 = E$. Solve for the momentum on the energy curve:

**第 4 步 — 算例：谐振子。** 取 $H = p^2/2m + \tfrac12 m\omega^2 q^2 = E$。在能量曲线上解出动量：

$$ p = \pm\sqrt{2m(E - \tfrac12 m\omega^2 q^2)} = \pm\sqrt{2mE}\,\sqrt{1 - q^2/q_{\max}^2}, \qquad q_{\max} = \sqrt{2E/(m\omega^2)}. $$

The orbit is an ellipse in the $(q, p)$ plane with semi-axes $q_{\max} = \sqrt{2E}/(\omega\sqrt{m})$ along $q$ and $p_{\max} = \sqrt{2mE}$ along $p$. The action equals the enclosed area of this ellipse, $\oint p\,dq = \pi \cdot (\text{semi-axis}_q) \cdot (\text{semi-axis}_p)$:

轨道是 $(q, p)$ 平面内的椭圆，沿 $q$ 半轴 $q_{\max} = \sqrt{2E}/(\omega\sqrt{m})$，沿 $p$ 半轴 $p_{\max} = \sqrt{2mE}$。作用量等于该椭圆的所围面积，$\oint p\,dq = \pi \cdot (q\text{ 半轴}) \cdot (p\text{ 半轴})$：

$$ J = \oint p\,dq = \pi \cdot q_{\max} \cdot p_{\max} = \pi \cdot \frac{\sqrt{2E}}{\omega\sqrt{m}} \cdot \sqrt{2mE} = \pi \cdot \frac{2E}{\omega} = \frac{2\pi E}{\omega}. $$

So $J = 2\pi E/\omega$. ✓

故 $J = 2\pi E/\omega$。✓

**Step 5 — Invert to get $E(J)$ and the frequency.** Solving $J = 2\pi E/\omega$ for the energy,

**第 5 步 — 反解得 $E(J)$ 与频率。** 由 $J = 2\pi E/\omega$ 解出能量，

$$ E = \frac{\omega}{2\pi} J. $$

Differentiate with respect to $J$ to obtain the frequency:

对 $J$ 求导得频率：

$$ \nu = \frac{\partial E}{\partial J} = \frac{\omega}{2\pi}, $$

exactly the familiar oscillator frequency $\omega/2\pi$, recovered purely from the enclosed elliptical area without integrating the equations of motion. ✓ $\blacksquare$

正是熟悉的振子频率 $\omega/2\pi$，纯由所围椭圆面积重现，无需积分运动方程。✓ $\blacksquare$

---

## E. Adiabatic Invariance of the Action · 作用量的绝热不变性

**Claim.** If a parameter $\lambda(t)$ of the Hamiltonian varies slowly compared with the orbital period (the **adiabatic** limit: timescale $\tau = \lambda/\dot{\lambda} \gg T = 2\pi/\omega$), then the action $J = \oint p\,dq$ is an **adiabatic invariant**: its time-averaged rate of change vanishes to first order, $dJ/dt \to 0$. For the oscillator this means $E/\omega = J/2\pi$ is conserved as $\omega(t)$ slowly varies, so the amplitude scales as $\omega^{-1/2}$.

**命题。** 若哈密顿量的参数 $\lambda(t)$ 相对于轨道周期缓慢变化（**绝热**极限：时标 $\tau = \lambda/\dot{\lambda} \gg T = 2\pi/\omega$），则作用量 $J = \oint p\,dq$ 是**绝热不变量**：其时间平均变化率到一阶为零，$dJ/dt \to 0$。对振子这意味着随 $\omega(t)$ 缓变 $E/\omega = J/2\pi$ 守恒，故振幅按 $\omega^{-1/2}$ 标度。

**Step 1 — Slow variation defines the adiabatic regime.** Let $H = H(q, p; \lambda(t))$ with $\lambda$ changing on a timescale $\tau = \lambda/|\dot{\lambda}|$ much longer than the orbital period $T = 2\pi/\omega$. The small parameter is $\varepsilon = T/\tau \ll 1$. Over a single period the parameter is nearly constant, so the orbit is, to leading order, a closed curve of the instantaneous (frozen-$\lambda$) system, with a well-defined instantaneous action $J(\lambda) = \oint p\,dq$.

**第 1 步 — 缓变定义绝热区域。** 设 $H = H(q, p; \lambda(t))$，$\lambda$ 在时标 $\tau = \lambda/|\dot{\lambda}|$ 上变化，远长于轨道周期 $T = 2\pi/\omega$。小参数为 $\varepsilon = T/\tau \ll 1$。在单个周期内参数近似不变，故轨道到主导阶是瞬时（冻结 $\lambda$）系统的闭曲线，具有确定的瞬时作用量 $J(\lambda) = \oint p\,dq$。

**Step 2 — Average rate of change of $J$.** Pass to angle–action variables for the frozen system; the generating function $W(q, J; \lambda)$ now depends on $\lambda$ through the Hamiltonian. With slow $\dot{\lambda}$, the action evolves under the extra $\partial/\partial t$ coming from $\dot{\lambda}\,\partial/\partial\lambda$. Its rate of change averaged over one cycle is

**第 2 步 — $J$ 的平均变化率。** 转到冻结系统的角–作用量变量；生成函数 $W(q, J; \lambda)$ 现通过哈密顿量依赖 $\lambda$。在缓变 $\dot{\lambda}$ 下，作用量在来自 $\dot{\lambda}\,\partial/\partial\lambda$ 的额外 $\partial/\partial t$ 下演化。其在一个周期上平均的变化率为

$$ \left\langle\frac{dJ}{dt}\right\rangle = -\dot{\lambda}\left\langle\frac{\partial^2 W}{\partial\theta\,\partial\lambda}\right\rangle_\theta = -\dot{\lambda} \cdot \frac{1}{2\pi}\oint \frac{\partial}{\partial\lambda}\!\left(\frac{\partial W}{\partial\theta}\right) d\theta. $$

The integrand is a total derivative in $\theta$ of a periodic function ($\partial W/\partial\lambda$ returns to its value after $\Delta\theta = 2\pi$), so the loop integral vanishes:

被积函数是周期函数关于 $\theta$ 的全导数（$\partial W/\partial\lambda$ 在 $\Delta\theta = 2\pi$ 后回到原值），故环积分为零：

$$ \left\langle\frac{dJ}{dt}\right\rangle = 0 + O(\varepsilon^2). $$

Thus to first order in the slowness $\varepsilon$, the action is conserved: **$J$ is an adiabatic invariant**, $dJ/dt \to 0$ as $\varepsilon \to 0$. The corrections are exponentially small in $1/\varepsilon$ for analytic, smooth variation.

故在缓变 $\varepsilon$ 的一阶，作用量守恒：**$J$ 是绝热不变量**，当 $\varepsilon \to 0$ 时 $dJ/dt \to 0$。对解析、光滑的变化，修正项在 $1/\varepsilon$ 上指数地小。

**Step 3 — Physical motivation.** Over each fast period the system completes a near-closed loop enclosing area $J$. The slow drift of $\lambda$ deforms the orbit, but the enclosed phase-space area is robust: the part of the loop integral that grows during half the cycle is cancelled by the part that shrinks during the other half, because the deformation is correlated with the (periodic) phase. Only a net secular change would alter $J$, and that is precisely the $O(\varepsilon^2)$ term shown to vanish at first order. This is the dynamical analogue of Liouville's theorem (Module 2.4): phase-space area is preserved under the Hamiltonian flow, and here also under slow parameter drift.

**第 3 步 — 物理动机。** 在每个快周期内系统完成一个近闭合的环，所围面积为 $J$。$\lambda$ 的缓慢漂移使轨道变形，但所围相空间面积是稳健的：环积分在半个周期内增大的部分被另半周期内减小的部分抵消，因为变形与（周期性的）相位相关。只有净的长期变化才会改变 $J$，而那正是已证在一阶消失的 $O(\varepsilon^2)$ 项。这是刘维尔定理（模块 2.4）的动力学类比：相空间面积在哈密顿流下守恒，此处在缓慢参数漂移下亦然。

**Step 4 — The oscillator: $E/\omega$ conserved, amplitude $\propto \omega^{-1/2}$.** For the harmonic oscillator with slowly varying $\omega(t)$, Section D gives $J = 2\pi E/\omega$. Adiabatic invariance of $J$ means

**第 4 步 — 振子：$E/\omega$ 守恒，振幅 $\propto \omega^{-1/2}$。** 对缓变 $\omega(t)$ 的谐振子，D 节给出 $J = 2\pi E/\omega$。$J$ 的绝热不变性意味着

$$ J = 2\pi E/\omega = \text{const} \implies E/\omega = J/2\pi = \text{const}. $$

So the energy tracks the frequency: if $\omega$ is slowly doubled, the energy doubles. The amplitude follows from $E = \tfrac12 m\omega^2 A^2$ (turning-point energy with $q_{\max} = A$), giving

故能量随频率变化：若 $\omega$ 缓慢翻倍，能量翻倍。振幅由 $E = \tfrac12 m\omega^2 A^2$（转折点能量，$q_{\max} = A$）得到

$$ A = \sqrt{2E/(m\omega^2)} = \sqrt{2(J/2\pi)\cdot\omega/(m\omega^2)} = \sqrt{J/(\pi m\omega)} \propto \omega^{-1/2}. $$

A slowly shortened pendulum (rising $\omega$) therefore gains energy in proportion to its frequency while its amplitude shrinks as $\omega^{-1/2}$ — the classic adiabatic result, and the historical seed of the Bohr–Sommerfeld quantization rule $\oint p\,dq = nh$ that bridges to canonical quantization (Module 3.3). $\blacksquare$

因此缓慢缩短的单摆（$\omega$ 上升）其能量按频率成比例增加，而振幅按 $\omega^{-1/2}$ 收缩——经典的绝热结果，也是玻尔–索末菲量子化规则 $\oint p\,dq = nh$ 的历史种子，该规则通往正则量子化（模块 3.3）。$\blacksquare$

---

*Canonical transformations expose the symplectic skeleton of mechanics: the Poisson bracket, not the coordinates, is the invariant object — and it is exactly this bracket that becomes the quantum commutator. Hamilton–Jacobi theory turns dynamics into a single PDE for the action, the same action whose phase governs the semiclassical wavefunction; action–angle variables and adiabatic invariants then carry this structure into integrable systems, perturbation theory, and the old quantum theory.*

*正则变换揭示力学的辛骨架：不变的对象是泊松括号而非坐标——而正是这一括号成为量子对易子。哈密顿–雅可比理论把动力学化为关于作用量的单一偏微分方程，正是这同一作用量的相位支配半经典波函数；作用量–角变量与绝热不变量随后把这一结构带入可积系统、微扰理论与旧量子论。*

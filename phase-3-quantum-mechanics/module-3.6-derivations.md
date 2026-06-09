---
title: "Derivations — Module 3.6: Time-Independent Perturbation Theory"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.6: Time-Independent Perturbation Theory
# 推导 — 模块 3.6：定态微扰理论

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.6](./module-3.6-time-independent-perturbation-theory.md). Full step-by-step proofs of every non-trivial result quoted there. English first, then 中文.
> [模块 3.6](./module-3.6-time-independent-perturbation-theory.md) 的配套文档：对该模块所引用每个非平凡结果的完整逐步证明。先英文，后中文。

---

## A. First-Order Energy Correction: $E_n^{(1)} = \langle n|\hat{H}'|n\rangle$ · 一阶能量修正

**Claim.** For the Hamiltonian $\hat{H} = \hat{H}_0 + \lambda\hat{H}'$ ($\lambda$ small), the first-order correction to the non-degenerate energy level $E_n^{(0)}$ is $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$.

**命题。** 对哈密顿量 $\hat{H} = \hat{H}_0 + \lambda\hat{H}'$（$\lambda$ 为小量），非简并能级 $E_n^{(0)}$ 的一阶修正为 $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$。

**Step 1 — Expand energies and states in powers of $\lambda$.** Write the exact eigenvalue problem $(\hat{H}_0 + \lambda\hat{H}')|n\rangle = E_n|n\rangle$ with:

**第 1 步 — 将能量和态按 $\lambda$ 幂次展开。** 将精确本征值方程 $(\hat{H}_0 + \lambda\hat{H}')|n\rangle = E_n|n\rangle$ 写成：

$$ E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots $$

$$ |n\rangle = |n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \lambda^2|n^{(2)}\rangle + \cdots $$

where $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$ (known exactly). The states $|m^{(0)}\rangle$ form a complete orthonormal set: $\langle m^{(0)}|n^{(0)}\rangle = \delta_{mn}$.

其中 $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$（精确已知）。态 $|m^{(0)}\rangle$ 构成完备正交归一组：$\langle m^{(0)}|n^{(0)}\rangle = \delta_{mn}$。

**Step 2 — Substitute into the eigenvalue equation and collect by powers of $\lambda$.** Substituting and expanding:

**第 2 步 — 代入本征值方程并按 $\lambda$ 幂次整理。** 代入展开：

$$ (\hat{H}_0 + \lambda\hat{H}')(|n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \cdots) = (E_n^{(0)} + \lambda E_n^{(1)} + \cdots)(|n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \cdots). $$

**Order $\lambda^0$:** $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$. $\checkmark$ (satisfied by assumption)

**$\lambda^0$ 阶：** $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$。$\checkmark$（由假设满足）

**Order $\lambda^1$:**

**$\lambda^1$ 阶：**

$$ \hat{H}_0|n^{(1)}\rangle + \hat{H}'|n^{(0)}\rangle = E_n^{(0)}|n^{(1)}\rangle + E_n^{(1)}|n^{(0)}\rangle. \qquad (*) $$

**Step 3 — Project onto $\langle n^{(0)}|$.** Take the inner product of $(*)$ with $\langle n^{(0)}|$:

**第 3 步 — 投影到 $\langle n^{(0)}|$。** 将 $(*)$ 与 $\langle n^{(0)}|$ 取内积：

$$ \langle n^{(0)}|\hat{H}_0|n^{(1)}\rangle + \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle + E_n^{(1)}\langle n^{(0)}|n^{(0)}\rangle. $$

Since $\hat{H}_0$ is Hermitian: $\langle n^{(0)}|\hat{H}_0|n^{(1)}\rangle = \langle\hat{H}_0 n^{(0)}|n^{(1)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle$. The $E_n^{(0)}$ terms cancel:

由 $\hat{H}_0$ 的厄米性：$\langle n^{(0)}|\hat{H}_0|n^{(1)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle$。$E_n^{(0)}$ 项消去：

$$ \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle = E_n^{(1)}\cdot 1. $$

Therefore:

因此：

$$ \boxed{\,E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle\,}. \qquad \blacksquare $$

**Physical interpretation.** The first-order energy shift is simply the expectation value of the perturbation in the unperturbed state — the diagonal matrix element. It is the classical-style average of the perturbation over the unperturbed probability distribution.

**物理诠释。** 一阶能量移动就是微扰在无微扰态中的期望值——即对角矩阵元。它是微扰在无微扰概率分布上的经典式平均。

---

## B. First-Order State Correction · 一阶态修正

**Claim.** The first-order correction to the state $|n^{(0)}\rangle$ is:

**命题。** 态 $|n^{(0)}\rangle$ 的一阶修正为：

$$ |n^{(1)}\rangle = \sum_{m\ne n} \frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle. $$

**Step 1 — Project the $\lambda^1$ equation onto $\langle m^{(0)}|$ for $m \ne n$.** From equation $(*)$ of Section A, take the inner product with $\langle m^{(0)}|$ ($m \ne n$):

**第 1 步 — 将 $\lambda^1$ 方程投影到 $\langle m^{(0)}|$（$m \ne n$）。** 从第 A 节方程 $(*)$ 出发，与 $\langle m^{(0)}|$ 取内积（$m \ne n$）：

$$ \langle m^{(0)}|\hat{H}_0|n^{(1)}\rangle + \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle = E_n^{(0)}\langle m^{(0)}|n^{(1)}\rangle + E_n^{(1)}\langle m^{(0)}|n^{(0)}\rangle. $$

$$ E_m^{(0)}\langle m^{(0)}|n^{(1)}\rangle + \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle = E_n^{(0)}\langle m^{(0)}|n^{(1)}\rangle + 0. $$

(The last term vanishes because $\langle m^{(0)}|n^{(0)}\rangle = \delta_{mn} = 0$ for $m \ne n$.)

（最后一项消失，因为对 $m \ne n$ 有 $\langle m^{(0)}|n^{(0)}\rangle = \delta_{mn} = 0$。）

**Step 2 — Solve for $\langle m^{(0)}|n^{(1)}\rangle$.**

**第 2 步 — 求解 $\langle m^{(0)}|n^{(1)}\rangle$。**

$$ (E_n^{(0)} - E_m^{(0)})\,\langle m^{(0)}|n^{(1)}\rangle = \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle. $$

Since $E_n^{(0)} \ne E_m^{(0)}$ (non-degenerate case):

由于 $E_n^{(0)} \ne E_m^{(0)}$（非简并情形）：

$$ \langle m^{(0)}|n^{(1)}\rangle = \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle / (E_n^{(0)} - E_m^{(0)}). $$

**Step 3 — Reconstruct $|n^{(1)}\rangle$ from its expansion coefficients.** By completeness, $|n^{(1)}\rangle = \sum_m \langle m^{(0)}|n^{(1)}\rangle\,|m^{(0)}\rangle$. The $m = n$ term can be chosen zero (corresponding to the choice of normalization $\langle n^{(0)}|n\rangle = 1$ to all orders):

**第 3 步 — 从展开系数重建 $|n^{(1)}\rangle$。** 由完备性，$|n^{(1)}\rangle = \sum_m \langle m^{(0)}|n^{(1)}\rangle\,|m^{(0)}\rangle$。$m = n$ 项可选为零（对应于归一化选择 $\langle n^{(0)}|n\rangle = 1$ 对所有阶成立）：

$$ \boxed{\,|n^{(1)}\rangle = \sum_{m\ne n} \frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle\,}. \qquad \blacksquare $$

**Note on validity.** This expression is valid when the perturbation is small relative to the level spacings: $|\langle m|\hat{H}'|n\rangle| \ll |E_n^{(0)} - E_m^{(0)}|$ for all $m \ne n$. When this breaks down near a degeneracy, degenerate perturbation theory (Section D) must be used.

**有效性注记。** 当微扰相对于能级间距很小时此表达式有效：对所有 $m \ne n$ 有 $|\langle m|\hat{H}'|n\rangle| \ll |E_n^{(0)} - E_m^{(0)}|$。当接近简并时失效，必须使用简并微扰理论（第 D 节）。

---

## C. Second-Order Energy Correction: $E_n^{(2)} = \sum_{m\ne n}|\langle m|\hat{H}'|n\rangle|^2/(E_n^{(0)} - E_m^{(0)})$ · 二阶能量修正

**Claim.** The second-order energy correction is:

**命题。** 二阶能量修正为：

$$ E_n^{(2)} = \sum_{m\ne n} \frac{|\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}. $$

**Step 1 — Collect terms at order $\lambda^2$.** Expanding the eigenvalue equation to order $\lambda^2$:

**第 1 步 — 整理 $\lambda^2$ 阶项。** 将本征值方程展开到 $\lambda^2$ 阶：

$$ \hat{H}_0|n^{(2)}\rangle + \hat{H}'|n^{(1)}\rangle = E_n^{(0)}|n^{(2)}\rangle + E_n^{(1)}|n^{(1)}\rangle + E_n^{(2)}|n^{(0)}\rangle. \qquad (**) $$

**Step 2 — Project onto $\langle n^{(0)}|$.** Take the inner product with $\langle n^{(0)}|$:

**第 2 步 — 投影到 $\langle n^{(0)}|$。** 与 $\langle n^{(0)}|$ 取内积：

$$ \langle n^{(0)}|\hat{H}_0|n^{(2)}\rangle + \langle n^{(0)}|\hat{H}'|n^{(1)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(2)}\rangle + E_n^{(1)}\langle n^{(0)}|n^{(1)}\rangle + E_n^{(2)}\langle n^{(0)}|n^{(0)}\rangle. $$

Using $\langle n^{(0)}|\hat{H}_0 = E_n^{(0)}\langle n^{(0)}|$ (Hermiticity of $\hat{H}_0$), the first terms on each side cancel:

利用 $\langle n^{(0)}|\hat{H}_0 = E_n^{(0)}\langle n^{(0)}|$（$\hat{H}_0$ 的厄米性），两边第一项消去：

$$ \langle n^{(0)}|\hat{H}'|n^{(1)}\rangle = E_n^{(1)}\langle n^{(0)}|n^{(1)}\rangle + E_n^{(2)}. $$

With the normalization convention $\langle n^{(0)}|n^{(1)}\rangle = 0$ (from Section B, the $m = n$ coefficient of $|n^{(1)}\rangle$ is zero):

取归一化约定 $\langle n^{(0)}|n^{(1)}\rangle = 0$（由第 B 节，$|n^{(1)}\rangle$ 的 $m = n$ 系数为零）：

$$ E_n^{(2)} = \langle n^{(0)}|\hat{H}'|n^{(1)}\rangle. $$

**Step 3 — Substitute the expansion of $|n^{(1)}\rangle$.** From Section B:

**第 3 步 — 代入 $|n^{(1)}\rangle$ 的展开。** 由第 B 节：

$$ \begin{aligned} E_n^{(2)} &= \langle n^{(0)}|\hat{H}'\cdot\sum_{m\ne n} \frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle \\ &= \sum_{m\ne n} \frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\cdot\langle n^{(0)}|\hat{H}'|m^{(0)}\rangle. \end{aligned} $$

Now $\langle n^{(0)}|\hat{H}'|m^{(0)}\rangle = (\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle)^*$ (since $\hat{H}'$ is Hermitian). Therefore:

现在 $\langle n^{(0)}|\hat{H}'|m^{(0)}\rangle = (\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle)^*$（因为 $\hat{H}'$ 是厄米的）。因此：

$$ \boxed{\,E_n^{(2)} = \sum_{m\ne n} \frac{|\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}\,}. \qquad \blacksquare $$

**Step 4 — Sign of $E_n^{(2)}$ for the ground state.** For the ground state $n = 0$, all denominators $E_n^{(0)} - E_m^{(0)}$ are negative (since $E_m^{(0)} > E_0^{(0)}$ for all $m > 0$), and all numerators are non-negative. Therefore:

**第 4 步 — 基态 $E_n^{(2)}$ 的符号。** 对基态 $n = 0$，所有分母 $E_n^{(0)} - E_m^{(0)}$ 为负（因为对所有 $m > 0$ 有 $E_m^{(0)} > E_0^{(0)}$），所有分子为非负。因此：

$$ E_0^{(2)} \le 0: \quad \textbf{the second-order correction always lowers the ground-state energy}. \qquad \blacksquare $$

$$ E_0^{(2)} \le 0: \quad \textbf{二阶修正总是降低基态能量}. \qquad \blacksquare $$

---

## D. Degenerate Perturbation Theory: Diagonalize $\hat{H}'$ in the Degenerate Subspace · 简并微扰理论：在简并子空间内对角化 $\hat{H}'$

**Claim.** When $E_n^{(0)}$ is $g$-fold degenerate ($g$ degenerate states $|n^{(0)},\alpha\rangle$, $\alpha = 1,\ldots,g$ spanning the subspace $V_n$), the first-order energy corrections and good zeroth-order states are found by diagonalizing the $g\times g$ perturbation matrix $W_{\alpha\beta} = \langle n^{(0)},\alpha|\hat{H}'|n^{(0)},\beta\rangle$ within $V_n$. The eigenvalues of $W$ give $E_n^{(1)}$, and the eigenvectors give the good zeroth-order states.

**命题。** 当 $E_n^{(0)}$ 是 $g$ 重简并时（$g$ 个简并态 $|n^{(0)},\alpha\rangle$，$\alpha = 1,\ldots,g$ 张成子空间 $V_n$），一阶能量修正和"好"的零阶态通过在 $V_n$ 内对角化 $g\times g$ 微扰矩阵 $W_{\alpha\beta} = \langle n^{(0)},\alpha|\hat{H}'|n^{(0)},\beta\rangle$ 来求得。$W$ 的本征值给出 $E_n^{(1)}$，本征向量给出好的零阶态。

**Step 1 — Why non-degenerate theory fails.** In non-degenerate perturbation theory, the first-order state correction has denominators $E_n^{(0)} - E_m^{(0)}$. If $E_m^{(0)} = E_n^{(0)}$ for some $m \ne n$ (degenerate states in $V_n$), these denominators vanish, making the expression diverge. The expansion breaks down.

**第 1 步 — 非简并理论为何失效。** 在非简并微扰理论中，一阶态修正有分母 $E_n^{(0)} - E_m^{(0)}$。若对某些 $m \ne n$（$V_n$ 中的简并态）有 $E_m^{(0)} = E_n^{(0)}$，则这些分母为零，使表达式发散。展开失效。

**Step 2 — Set up the problem correctly.** Let the good zeroth-order states within $V_n$ (yet to be determined) be:

**第 2 步 — 正确建立问题。** 设 $V_n$ 内的好零阶态（待确定）为：

$$ |n^{(0)}\rangle = \sum_{\alpha=1}^g c_\alpha\,|n^{(0)},\alpha\rangle. $$

The first-order eigenvalue equation (from Section A Step 2, at order $\lambda^1$) within the degenerate subspace is:

简并子空间内的一阶本征值方程（来自第 A 节第 2 步，$\lambda^1$ 阶）为：

$$ (\hat{H}_0 + \lambda\hat{H}')|n\rangle = E_n|n\rangle \quad \text{projected onto } V_n \text{ at first order.} $$

**Step 3 — Project onto $V_n$.** Take the inner product of the order $\lambda^1$ equation with $\langle n^{(0)},\beta|$ for each $\beta$. The $\hat{H}_0$ terms on both sides cancel (as in Section A Step 3), leaving:

**第 3 步 — 投影到 $V_n$。** 将 $\lambda^1$ 阶方程对每个 $\beta$ 与 $\langle n^{(0)},\beta|$ 取内积。两边的 $\hat{H}_0$ 项消去（如第 A 节第 3 步），留下：

$$ \sum_\alpha \langle n^{(0)},\beta|\hat{H}'|n^{(0)},\alpha\rangle\,c_\alpha = E_n^{(1)} c_\beta. $$

In matrix form with $W_{\beta\alpha} = \langle n^{(0)},\beta|\hat{H}'|n^{(0)},\alpha\rangle$:

用矩阵形式，$W_{\beta\alpha} = \langle n^{(0)},\beta|\hat{H}'|n^{(0)},\alpha\rangle$：

$$ W c = E_n^{(1)} c. $$

This is a $g\times g$ eigenvalue equation.

这是一个 $g\times g$ 本征值方程。

**Step 4 — Solve the eigenvalue equation.** The eigenvalues $E^{(1)}_1, E^{(1)}_2, \ldots, E^{(1)}_g$ of the Hermitian matrix $W$ are real (Section B of Module 3.3). The perturbation lifts (some or all of) the degeneracy: the original $g$-fold degenerate level splits into levels with first-order corrections $E^{(1)}_1, \ldots, E^{(1)}_g$ (some may remain degenerate if $W$ has repeated eigenvalues).

**第 4 步 — 求解本征值方程。** 厄米矩阵 $W$ 的本征值 $E^{(1)}_1, E^{(1)}_2, \ldots, E^{(1)}_g$ 均为实数（模块 3.3 第 B 节）。微扰解除（部分或全部）简并：原来的 $g$ 重简并能级分裂为具有一阶修正 $E^{(1)}_1, \ldots, E^{(1)}_g$ 的能级（若 $W$ 有重复本征值，某些简并可能保留）。

**Step 5 — Good zeroth-order states.** The eigenvectors $c^{(k)}$ of $W$ give the **good zeroth-order states**:

**第 5 步 — 好的零阶态。** $W$ 的本征向量 $c^{(k)}$ 给出**好的零阶态**：

$$ |n^{(0)};k\rangle = \sum_\alpha c^{(k)}_\alpha\,|n^{(0)},\alpha\rangle, \qquad k = 1,\ldots,g. $$

These are the correct zeroth-order starting states such that the non-degenerate formulas for higher-order corrections are well-defined (the dangerous cross-terms between degenerate states in the denominators of state corrections now vanish because the perturbation matrix is diagonal in this basis).

这些是正确的零阶起始态，使得高阶修正的非简并公式定义良好（态修正分母中简并态之间的危险交叉项现在在此基底中消失，因为微扰矩阵在此基底中是对角的）。

**Step 6 — Summary.** The total first-order corrected energy levels are:

**第 6 步 — 汇总。** 总的一阶修正能级为：

$$ E_{n,k} = E_n^{(0)} + \lambda E^{(1)}_k, \qquad k = 1, \ldots, g, $$

where $E^{(1)}_k$ are the eigenvalues of $W = (\langle n^{(0)},\alpha|\hat{H}'|n^{(0)},\beta\rangle)$. Once the good states are identified, second-order corrections follow from the non-degenerate formula of Section C, now with denominators $E_{n,k} - E_m^{(0)}$ ($m$ outside $V_n$) which are nonzero. $\blacksquare$

其中 $E^{(1)}_k$ 是 $W = (\langle n^{(0)},\alpha|\hat{H}'|n^{(0)},\beta\rangle)$ 的本征值。一旦确定了好的态，二阶修正就可以用第 C 节的非简并公式计算，现在分母 $E_{n,k} - E_m^{(0)}$（$m$ 在 $V_n$ 之外）非零。$\blacksquare$

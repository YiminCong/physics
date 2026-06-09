# Derivations — Module 3.11: Angular Momentum (Addition & Spin)
# 推导 — 模块 3.11：角动量（合成与自旋）

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.11](./module-3.11-angular-momentum-advanced.md). Full step-by-step proofs of the angular momentum commutation relations, the ladder-operator spectrum, the explicit $\tfrac12\otimes\tfrac12$ Clebsch–Gordan decomposition, and the Clebsch–Gordan table. English first, then 中文.
> [模块 3.11](./module-3.11-angular-momentum-advanced.md) 的配套文档：角动量对易关系、梯形算符谱、显式 $\tfrac12\otimes\tfrac12$ Clebsch–Gordan 分解与系数表的完整逐步证明。先英文，后中文。

---

## A. Angular Momentum Commutation Relations · 角动量对易关系

**Claim.** The angular momentum operators $\hat{J}_x, \hat{J}_y, \hat{J}_z$ (defined abstractly or as orbital $\mathbf{r} \times \mathbf{p}$) satisfy $[\hat{J}_i, \hat{J}_j] = i\hbar\, \varepsilon_{ijk}\, \hat{J}_k$, i.e.

**命题。** 角动量算符 $\hat{J}_x, \hat{J}_y, \hat{J}_z$（抽象定义或作为轨道 $\mathbf{r} \times \mathbf{p}$）满足 $[\hat{J}_i, \hat{J}_j] = i\hbar\, \varepsilon_{ijk}\, \hat{J}_k$，即

$$ [\hat{J}_x, \hat{J}_y] = i\hbar\, \hat{J}_z, \quad [\hat{J}_y, \hat{J}_z] = i\hbar\, \hat{J}_x, \quad [\hat{J}_z, \hat{J}_x] = i\hbar\, \hat{J}_y. $$

**Step 1 — Definition of orbital angular momentum.** For orbital angular momentum $\hat{\mathbf{L}} = \hat{\mathbf{r}} \times \hat{\mathbf{p}}$:

**第 1 步 — 轨道角动量的定义。** 对轨道角动量 $\hat{\mathbf{L}} = \hat{\mathbf{r}} \times \hat{\mathbf{p}}$：

$$ \hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \quad \hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z, \quad \hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x. $$

**Step 2 — Compute $[\hat{L}_x, \hat{L}_y]$.** Expand using the canonical commutation relations $[\hat{x}_i, \hat{p}_j] = i\hbar\, \delta_{ij}$ and $[\hat{x}_i, \hat{x}_j] = 0$, $[\hat{p}_i, \hat{p}_j] = 0$:

**第 2 步 — 计算 $[\hat{L}_x, \hat{L}_y]$。** 利用正则对易关系 $[\hat{x}_i, \hat{p}_j] = i\hbar\, \delta_{ij}$，$[\hat{x}_i, \hat{x}_j] = 0$，$[\hat{p}_i, \hat{p}_j] = 0$ 展开：

$$ [\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y,\ \hat{z}\hat{p}_x - \hat{x}\hat{p}_z]. $$

Expand using bilinearity of the commutator:

利用对易子的双线性展开：

$$ = [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] - [\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] - [\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] + [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z]. $$

Evaluate each term using $[AB, CD] = A[B,C]D + AC[B,D] + [A,C]DB + C[A,D]B$:

用 $[AB, CD] = A[B,C]D + AC[B,D] + [A,C]DB + C[A,D]B$ 逐项计算：

$$ \begin{aligned} [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] &= \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x + \hat{y}\hat{z}[\hat{p}_z, \hat{p}_x] + [\hat{y}, \hat{z}]\hat{p}_z\hat{p}_x + \hat{z}[\hat{y}, \hat{p}_x]\hat{p}_z \\ &= \hat{y}(-i\hbar)\hat{p}_x + 0 + 0 + 0 = -i\hbar\, \hat{y}\hat{p}_x. \end{aligned} $$

$$ \begin{aligned} [\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] &= \hat{y}[\hat{p}_z, \hat{x}]\hat{p}_z + \hat{y}\hat{x}[\hat{p}_z, \hat{p}_z] + [\hat{y}, \hat{x}]\hat{p}_z^2 + \hat{x}[\hat{y}, \hat{p}_z]\hat{p}_z \\ &= 0 + 0 + 0 + 0 = 0. \quad \text{(all cross-commutators vanish)} \end{aligned} $$

$$ [\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] = \hat{z}[\hat{p}_y, \hat{z}]\hat{p}_x + 0 + 0 + 0 = \hat{z}\cdot 0\cdot\hat{p}_x = 0. \quad \text{($\hat{p}_y$ and $\hat{z}$ commute)} $$

$$ \begin{aligned} [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z] &= \hat{z}[\hat{p}_y, \hat{x}]\hat{p}_z + \hat{z}\hat{x}[\hat{p}_y, \hat{p}_z] + [\hat{z}, \hat{x}]\hat{p}_y\hat{p}_z + \hat{x}[\hat{z}, \hat{p}_z]\hat{p}_y \\ &= 0 + 0 + 0 + \hat{x}(i\hbar)\hat{p}_y = i\hbar\, \hat{x}\hat{p}_y. \end{aligned} $$

Adding all contributions:

将所有贡献相加：

$$ [\hat{L}_x, \hat{L}_y] = -i\hbar\, \hat{y}\hat{p}_x - 0 - 0 + i\hbar\, \hat{x}\hat{p}_y = i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\, \hat{L}_z. $$

The other two relations follow by cyclic permutation $x \to y \to z \to x$. $\blacksquare$

其余两个关系由循环置换 $x \to y \to z \to x$ 得到。$\blacksquare$

**Note for spin and general angular momentum.** For spin operators defined by $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$ with Pauli matrices, one verifies $[\hat{S}_x, \hat{S}_y] = i\hbar\, \hat{S}_z$ directly from the Pauli matrix algebra: $\sigma_x \sigma_y - \sigma_y \sigma_x = 2i\sigma_z$ (multiply $2\times 2$ matrices explicitly). The abstract angular momentum algebra is then the defining relation for any generator of rotations (by Noether's theorem and the Lie algebra $\mathfrak{so}(3) \cong \mathfrak{su}(2)$).

**关于自旋和一般角动量的注记。** 对由泡利矩阵定义的自旋算符 $\hat{\mathbf{S}} = (\hbar/2)\boldsymbol{\sigma}$，直接由泡利矩阵代数验证 $[\hat{S}_x, \hat{S}_y] = i\hbar\, \hat{S}_z$：$\sigma_x \sigma_y - \sigma_y \sigma_x = 2i\sigma_z$（显式相乘 $2\times 2$ 矩阵）。抽象角动量代数于是成为任意转动生成元的定义关系（由诺特定理与李代数 $\mathfrak{so}(3) \cong \mathfrak{su}(2)$）。

---

## B. Ladder Operators and the $J$ Spectrum · 梯形算符与 $J$ 谱

**Claim.** For an angular momentum operator satisfying the commutation relations above, with $\hat{J}^2 = \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2$, and ladder operators $\hat{J}_\pm = \hat{J}_x \pm i\hat{J}_y$:

**命题。** 对满足上述对易关系的角动量算符，令 $\hat{J}^2 = \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2$，梯形算符 $\hat{J}_\pm = \hat{J}_x \pm i\hat{J}_y$：

(i) $[\hat{J}^2, \hat{J}_i] = 0$ for $i = x, y, z$ ($\hat{J}^2$ is a Casimir operator).

(ii) The simultaneous eigenstates $|j, m\rangle$ of $\hat{J}^2$ and $\hat{J}_z$ satisfy $\hat{J}^2|j,m\rangle = j(j+1)\hbar^2|j,m\rangle$ and $\hat{J}_z|j,m\rangle = m\hbar|j,m\rangle$, with $j = 0, \tfrac12, 1, 3/2, \dots$ and $m = -j, -j+1, \dots, j-1, j$.

(iii) $\hat{J}_\pm|j,m\rangle = \hbar\sqrt{j(j+1) - m(m\pm 1)}\, |j, m\pm 1\rangle$.

**Step 1 — Prove $[\hat{J}^2, \hat{J}_z] = 0$.** Write $\hat{J}^2 = \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2$:

**第 1 步 — 证明 $[\hat{J}^2, \hat{J}_z] = 0$。** 令 $\hat{J}^2 = \hat{J}_x^2 + \hat{J}_y^2 + \hat{J}_z^2$：

$$ [\hat{J}^2, \hat{J}_z] = [\hat{J}_x^2, \hat{J}_z] + [\hat{J}_y^2, \hat{J}_z] + [\hat{J}_z^2, \hat{J}_z]. $$

The last term is zero. For the first:

最后一项为零。对第一项：

$$ [\hat{J}_x^2, \hat{J}_z] = \hat{J}_x[\hat{J}_x, \hat{J}_z] + [\hat{J}_x, \hat{J}_z]\hat{J}_x = \hat{J}_x(-i\hbar\hat{J}_y) + (-i\hbar\hat{J}_y)\hat{J}_x = -i\hbar(\hat{J}_x\hat{J}_y + \hat{J}_y\hat{J}_x). $$

For the second:

对第二项：

$$ [\hat{J}_y^2, \hat{J}_z] = \hat{J}_y[\hat{J}_y, \hat{J}_z] + [\hat{J}_y, \hat{J}_z]\hat{J}_y = \hat{J}_y(i\hbar\hat{J}_x) + (i\hbar\hat{J}_x)\hat{J}_y = i\hbar(\hat{J}_y\hat{J}_x + \hat{J}_x\hat{J}_y). $$

Adding: $[\hat{J}^2, \hat{J}_z] = -i\hbar(\hat{J}_x\hat{J}_y + \hat{J}_y\hat{J}_x) + i\hbar(\hat{J}_y\hat{J}_x + \hat{J}_x\hat{J}_y) = 0$. $\blacksquare$ (Cyclic permutation gives $[\hat{J}^2, \hat{J}_x] = [\hat{J}^2, \hat{J}_y] = 0$ similarly.)

相加：$[\hat{J}^2, \hat{J}_z] = 0$。$\blacksquare$（循环置换类似地给出 $[\hat{J}^2, \hat{J}_x] = [\hat{J}^2, \hat{J}_y] = 0$。）

**Step 2 — Ladder operator commutators.** Compute $[\hat{J}_z, \hat{J}_\pm]$:

**第 2 步 — 梯形算符对易子。** 计算 $[\hat{J}_z, \hat{J}_\pm]$：

$$ \begin{aligned} [\hat{J}_z, \hat{J}_+] &= [\hat{J}_z, \hat{J}_x + i\hat{J}_y] = [\hat{J}_z, \hat{J}_x] + i[\hat{J}_z, \hat{J}_y] \\ &= i\hbar\hat{J}_y + i(-i\hbar\hat{J}_x) = i\hbar\hat{J}_y + \hbar\hat{J}_x = \hbar(\hat{J}_x + i\hat{J}_y) = \hbar\hat{J}_+. \end{aligned} $$

Similarly $[\hat{J}_z, \hat{J}_-] = -\hbar\hat{J}_-$. Also $[\hat{J}_+, \hat{J}_-] = 2\hbar\hat{J}_z$ (verified by direct expansion).

类似地 $[\hat{J}_z, \hat{J}_-] = -\hbar\hat{J}_-$。同样 $[\hat{J}_+, \hat{J}_-] = 2\hbar\hat{J}_z$（直接展开验证）。

**Step 3 — Ladder action.** If $\hat{J}_z|j,m\rangle = m\hbar|j,m\rangle$, then:

**第 3 步 — 梯形作用。** 若 $\hat{J}_z|j,m\rangle = m\hbar|j,m\rangle$，则：

$$ \hat{J}_z (\hat{J}_+|j,m\rangle) = (\hat{J}_+ \hat{J}_z + [\hat{J}_z, \hat{J}_+])|j,m\rangle = (\hat{J}_+ m\hbar + \hbar\hat{J}_+)|j,m\rangle = (m+1)\hbar\, (\hat{J}_+|j,m\rangle). $$

So $\hat{J}_+|j,m\rangle$ is an eigenstate of $\hat{J}_z$ with eigenvalue $(m+1)\hbar$ — it raises $m$ by $1$. Similarly $\hat{J}_-$ lowers $m$ by $1$.

故 $\hat{J}_+|j,m\rangle$ 是 $\hat{J}_z$ 的本征态，本征值为 $(m+1)\hbar$——它将 $m$ 升高 $1$。类似地 $\hat{J}_-$ 将 $m$ 降低 $1$。

**Step 4 — Spectrum is bounded.** The eigenvalue of $\hat{J}^2$ is at least $\hbar^2$ times the square of any component's eigenvalue. Formally, for any state $\langle\hat{J}^2\rangle \ge \langle\hat{J}_z^2\rangle$, hence $j(j+1) \ge m^2$. This bounds $|m| \le j$. The ladder must terminate: there exist states $|j, m_\text{max}\rangle$ and $|j, m_\text{min}\rangle$ with

**第 4 步 — 谱有界。** $\hat{J}^2$ 的本征值至少是任意分量本征值平方的 $\hbar^2$ 倍。形式上，对任意态 $\langle\hat{J}^2\rangle \ge \langle\hat{J}_z^2\rangle$，故 $j(j+1) \ge m^2$。这限制了 $|m| \le j$。梯形必须终止：存在态 $|j, m_\text{max}\rangle$ 和 $|j, m_\text{min}\rangle$ 满足

$$ \hat{J}_+|j, m_\text{max}\rangle = 0, \quad \hat{J}_-|j, m_\text{min}\rangle = 0. $$

**Step 5 — Determine $m_\text{max}$ and $m_\text{min}$.** Using $\hat{J}_-\hat{J}_+ = \hat{J}^2 - \hat{J}_z^2 - \hbar\hat{J}_z$:

**第 5 步 — 确定 $m_\text{max}$ 和 $m_\text{min}$。** 利用 $\hat{J}_-\hat{J}_+ = \hat{J}^2 - \hat{J}_z^2 - \hbar\hat{J}_z$：

$$ \langle j, m_\text{max}|\hat{J}_-\hat{J}_+|j, m_\text{max}\rangle = \|\hat{J}_+|j, m_\text{max}\rangle\|^2 = 0 $$

$$ \implies [j(j+1) - m_\text{max}^2 - m_\text{max}]\hbar^2 = 0 \implies j(j+1) = m_\text{max}(m_\text{max} + 1) \implies m_\text{max} = j. $$

Similarly, using $\hat{J}_+\hat{J}_- = \hat{J}^2 - \hat{J}_z^2 + \hbar\hat{J}_z$, the termination of the lower ladder gives $m_\text{min} = -j$.

类似地，利用 $\hat{J}_+\hat{J}_- = \hat{J}^2 - \hat{J}_z^2 + \hbar\hat{J}_z$，下梯形终止给出 $m_\text{min} = -j$。

**Step 6 — Allowed values.** The integer steps from $m_\text{min} = -j$ to $m_\text{max} = j$ require $2j$ to be a non-negative integer, so $j = 0, \tfrac12, 1, 3/2, 2, \dots$ and $m = -j, -j+1, \dots, j-1, j$.

**第 6 步 — 允许值。** 从 $m_\text{min} = -j$ 到 $m_\text{max} = j$ 整数步长要求 $2j$ 为非负整数，故 $j = 0, \tfrac12, 1, 3/2, 2, \dots$，$m = -j, -j+1, \dots, j-1, j$。

**Step 7 — Normalize the ladder action.** Compute $\|\hat{J}_+|j,m\rangle\|^2$:

**第 7 步 — 归一化梯形作用。** 计算 $\|\hat{J}_+|j,m\rangle\|^2$：

$$ \begin{aligned} \|\hat{J}_+|j,m\rangle\|^2 &= \langle j,m|\hat{J}_-\hat{J}_+|j,m\rangle = \langle j,m|(\hat{J}^2 - \hat{J}_z^2 - \hbar\hat{J}_z)|j,m\rangle \\ &= [j(j+1) - m^2 - m]\hbar^2 = [j(j+1) - m(m+1)]\hbar^2. \end{aligned} $$

Since $\hat{J}_+|j,m\rangle$ is proportional to $|j, m+1\rangle$ (proven to be an eigenstate in Step 3), writing $\hat{J}_+|j,m\rangle = c|j, m+1\rangle$ and using $\|c|j,m+1\rangle\|^2 = |c|^2$:

由于 $\hat{J}_+|j,m\rangle$ 正比于 $|j, m+1\rangle$（第 3 步已证），令 $\hat{J}_+|j,m\rangle = c|j, m+1\rangle$，利用 $\|c|j,m+1\rangle\|^2 = |c|^2$：

$$ |c|^2 = [j(j+1) - m(m+1)]\hbar^2, \quad \text{choosing $c$ real and positive: } c = \hbar\sqrt{j(j+1)-m(m+1)}. $$

Therefore:

因此：

$$ \boxed{\, \hat{J}_+|j,m\rangle = \hbar\sqrt{j(j+1) - m(m+1)}\, |j, m+1\rangle \,} $$

For $\hat{J}_-$, by the same method (using $\|\hat{J}_-|j,m\rangle\|^2 = [j(j+1)-m(m-1)]\hbar^2$):

对 $\hat{J}_-$，用相同方法（利用 $\|\hat{J}_-|j,m\rangle\|^2 = [j(j+1)-m(m-1)]\hbar^2$）：

$$ \boxed{\, \hat{J}_-|j,m\rangle = \hbar\sqrt{j(j+1) - m(m-1)}\, |j, m-1\rangle \,} \qquad \blacksquare $$

These two formulas can be unified as $\hat{J}_\pm|j,m\rangle = \hbar\sqrt{j(j+1) - m(m\pm 1)}\, |j, m\pm 1\rangle$.

这两个公式可以统一为 $\hat{J}_\pm|j,m\rangle = \hbar\sqrt{j(j+1) - m(m\pm 1)}\, |j, m\pm 1\rangle$。$\blacksquare$

---

## C. Addition of Two Spin-½'s: Singlet and Triplet · 两个自旋-½ 的合成：单态与三重态

**Claim.** The tensor product space of two spin-½ particles (dimension $2\otimes 2 = 4$) decomposes under the total angular momentum $\hat{\mathbf{J}} = \hat{\mathbf{S}}_1 + \hat{\mathbf{S}}_2$ into a triplet ($j = 1$, three states) and a singlet ($j = 0$, one state):

**命题。** 两个自旋-½ 粒子的张量积空间（维数 $2\otimes 2 = 4$）在总角动量 $\hat{\mathbf{J}} = \hat{\mathbf{S}}_1 + \hat{\mathbf{S}}_2$ 下分解为三重态（$j = 1$，三个态）和单态（$j = 0$，一个态）：

$$ \begin{aligned} \text{Triplet:} \quad |1,+1\rangle &= |+\rangle|+\rangle, \\ |1, 0\rangle &= \tfrac{1}{\sqrt2}(|+\rangle|-\rangle + |-\rangle|+\rangle), \\ |1,-1\rangle &= |-\rangle|-\rangle. \end{aligned} $$

$$ \text{Singlet:} \quad |0, 0\rangle = \tfrac{1}{\sqrt2}(|+\rangle|-\rangle - |-\rangle|+\rangle). $$

$$ \begin{aligned} \text{三重态：} \quad |1,+1\rangle &= |+\rangle|+\rangle, \\ |1, 0\rangle &= \tfrac{1}{\sqrt2}(|+\rangle|-\rangle + |-\rangle|+\rangle), \\ |1,-1\rangle &= |-\rangle|-\rangle. \end{aligned} $$

$$ \text{单态：} \quad |0, 0\rangle = \tfrac{1}{\sqrt2}(|+\rangle|-\rangle - |-\rangle|+\rangle). $$

Here $|+\rangle \equiv |s=\tfrac12, m=+\tfrac12\rangle$ and $|-\rangle \equiv |s=\tfrac12, m=-\tfrac12\rangle$.

此处 $|+\rangle \equiv |s=\tfrac12, m=+\tfrac12\rangle$，$|-\rangle \equiv |s=\tfrac12, m=-\tfrac12\rangle$。

**Step 1 — Identify the highest-weight state.** The state of maximum total $m$ is $m = m_1 + m_2 = \tfrac12 + \tfrac12 = 1$. The only product state with $m = 1$ is $|+\rangle_1|+\rangle_2$. Since $m = 1$ implies $j \ge 1$, and the total angular momentum of the combined system can be at most $j = 1$ (since each spin is $\tfrac12$), this must be $|j = 1, m = 1\rangle$:

**第 1 步 — 确定最高权态。** 最大总 $m$ 为 $m = m_1 + m_2 = \tfrac12 + \tfrac12 = 1$。$m = 1$ 的唯一直积态为 $|+\rangle_1|+\rangle_2$。由于 $m = 1$ 意味着 $j \ge 1$，而合并系统的总角动量最大为 $j = 1$（每个自旋为 $\tfrac12$），故这必须是 $|j=1, m=1\rangle$：

$$ |1, +1\rangle = |+\rangle_1|+\rangle_2. $$

**Step 2 — Apply $\hat{J}_-$ to get $|1, 0\rangle$.** The total lowering operator is $\hat{J}_- = \hat{S}_{1-} \otimes \hat{1}_2 + \hat{1}_1 \otimes \hat{S}_{2-}$. Using $\hat{J}_-|j,m\rangle = \hbar\sqrt{j(j+1)-m(m-1)}|j,m-1\rangle$ with $j = m = 1$:

**第 2 步 — 作用 $\hat{J}_-$ 得 $|1, 0\rangle$。** 总降算符为 $\hat{J}_- = \hat{S}_{1-} \otimes \hat{1}_2 + \hat{1}_1 \otimes \hat{S}_{2-}$。利用 $\hat{J}_-|j,m\rangle = \hbar\sqrt{j(j+1)-m(m-1)}|j,m-1\rangle$，取 $j = m = 1$：

$$ \hat{J}_-|1,+1\rangle = \hbar\sqrt{1\cdot 2 - 1\cdot 0}|1, 0\rangle = \hbar\sqrt2\, |1, 0\rangle. $$

The left-hand side acts on the product state:

左端作用于直积态：

$$ \hat{J}_-|+\rangle_1|+\rangle_2 = (\hat{S}_{1-}|+\rangle_1)|+\rangle_2 + |+\rangle_1(\hat{S}_{2-}|+\rangle_2). $$

Using $\hat{S}_-|+\rangle = \hbar\sqrt{\tfrac12\cdot 3/2 - \tfrac12(\tfrac12-1)}|-\rangle = \hbar\sqrt{\tfrac34-(-\tfrac14)}|-\rangle = \hbar\sqrt1\, |-\rangle = \hbar|-\rangle$:

利用 $\hat{S}_-|+\rangle = \hbar\sqrt{\tfrac12\cdot 3/2 - \tfrac12\cdot(\tfrac12-1)}|-\rangle = \hbar|-\rangle$：

$$ \hat{J}_-|+\rangle_1|+\rangle_2 = \hbar|-\rangle_1|+\rangle_2 + \hbar|+\rangle_1|-\rangle_2. $$

Setting equal: $\hbar\sqrt2\, |1, 0\rangle = \hbar(|-\rangle_1|+\rangle_2 + |+\rangle_1|-\rangle_2)$, so

令两端相等：$\hbar\sqrt2\, |1,0\rangle = \hbar(|-\rangle_1|+\rangle_2 + |+\rangle_1|-\rangle_2)$，故

$$ |1, 0\rangle = \tfrac{1}{\sqrt2}(|+\rangle_1|-\rangle_2 + |-\rangle_1|+\rangle_2). $$

**Step 3 — Apply $\hat{J}_-$ again to get $|1, -1\rangle$.** Apply $\hat{J}_-$ to $|1, 0\rangle$: $\hat{J}_-|1,0\rangle = \hbar\sqrt{2-0}|1,-1\rangle = \hbar\sqrt2|1,-1\rangle$.

**第 3 步 — 再次作用 $\hat{J}_-$ 得 $|1, -1\rangle$。** 对 $|1,0\rangle$ 作用 $\hat{J}_-$：$\hat{J}_-|1,0\rangle = \hbar\sqrt{2-0}|1,-1\rangle = \hbar\sqrt2|1,-1\rangle$。

$$ \begin{aligned} &\hat{J}_-\Big(\tfrac{1}{\sqrt2}(|+\rangle_1|-\rangle_2 + |-\rangle_1|+\rangle_2)\Big) \\ &\quad = \tfrac{1}{\sqrt2}[(\hat{S}_{1-}|+\rangle_1)|-\rangle_2 + |+\rangle_1(\hat{S}_{2-}|-\rangle_2) + (\hat{S}_{1-}|-\rangle_1)|+\rangle_2 + |-\rangle_1(\hat{S}_{2-}|+\rangle_2)] \\ &\quad = \tfrac{1}{\sqrt2}[\hbar|-\rangle_1|-\rangle_2 + 0 + 0 + \hbar|-\rangle_1|-\rangle_2] \\ &\quad = \tfrac{2\hbar}{\sqrt2}|-\rangle_1|-\rangle_2 = \hbar\sqrt2\, |-\rangle_1|-\rangle_2. \end{aligned} $$

(Using $\hat{S}_-|-\rangle = 0$ since $|-\rangle$ is already the lowest state.) Hence:

（利用 $\hat{S}_-|-\rangle = 0$，因为 $|-\rangle$ 已是最低态。）故：

$$ |1, -1\rangle = |-\rangle_1|-\rangle_2. $$

**Step 4 — Find the singlet by orthogonality.** The remaining state in the $m = 0$ subspace must be orthogonal to $|1, 0\rangle$. The general $m = 0$ state is $\alpha|+\rangle_1|-\rangle_2 + \beta|-\rangle_1|+\rangle_2$. Requiring orthogonality to $|1,0\rangle = (1/\sqrt2)(|+-\rangle + |-+\rangle)$:

**第 4 步 — 由正交性求单态。** $m = 0$ 子空间中剩余的态必须与 $|1,0\rangle$ 正交。一般 $m = 0$ 态为 $\alpha|+\rangle_1|-\rangle_2 + \beta|-\rangle_1|+\rangle_2$。要求与 $|1,0\rangle = (1/\sqrt2)(|+-\rangle + |-+\rangle)$ 正交：

$$ \langle 1,0|(\alpha|+-\rangle + \beta|-+\rangle) = \tfrac{1}{\sqrt2}(\alpha + \beta) = 0 \implies \beta = -\alpha. $$

Normalizing: $|\alpha|^2 + |\beta|^2 = 2|\alpha|^2 = 1$, so $|\alpha| = 1/\sqrt2$. Choosing $\alpha = 1/\sqrt2$:

归一化：$|\alpha|^2 + |\beta|^2 = 2|\alpha|^2 = 1$，故 $|\alpha| = 1/\sqrt2$。取 $\alpha = 1/\sqrt2$：

$$ |0, 0\rangle = \tfrac{1}{\sqrt2}(|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2). $$

**Step 5 — Verify $|0,0\rangle$ is a $j = 0$ state.** Check $\hat{J}_+|0,0\rangle = 0$:

**第 5 步 — 验证 $|0,0\rangle$ 是 $j = 0$ 的态。** 验证 $\hat{J}_+|0,0\rangle = 0$：

$$ \begin{aligned} &\hat{J}_+\tfrac{1}{\sqrt2}(|+-\rangle - |-+\rangle) \\ &\quad = \tfrac{1}{\sqrt2}[(\hat{S}_{1+}|+\rangle_1)|-\rangle_2 + |+\rangle_1(\hat{S}_{2+}|-\rangle_2) - (\hat{S}_{1+}|-\rangle_1)|+\rangle_2 - |-\rangle_1(\hat{S}_{2+}|+\rangle_2)] \\ &\quad = \tfrac{1}{\sqrt2}[0 + \hbar|+\rangle_1|+\rangle_2 - \hbar|+\rangle_1|+\rangle_2 - 0] = 0. \quad \checkmark \end{aligned} $$

Also $\hat{J}_z|0,0\rangle = 0$ (since both terms have total $m = 0$). And $\hat{J}^2|0,0\rangle = 0$ can be confirmed from $\hat{J}^2 = (\hat{J}_+\hat{J}_- + \hat{J}_-\hat{J}_+)/2 + \hat{J}_z^2$ acting term by term, giving $0$. $\blacksquare$

同样 $\hat{J}_z|0,0\rangle = 0$（因为两项的总 $m = 0$）。$\hat{J}^2|0,0\rangle = 0$ 可由 $\hat{J}^2 = (\hat{J}_+\hat{J}_- + \hat{J}_-\hat{J}_+)/2 + \hat{J}_z^2$ 逐项作用确认，结果为 $0$。$\blacksquare$

---

## D. Clebsch–Gordan Table for $\tfrac12 \otimes \tfrac12$ · $\tfrac12 \otimes \tfrac12$ 的 Clebsch–Gordan 系数表

The Clebsch–Gordan coefficients $\langle j_1, m_1; j_2, m_2 | J, M\rangle$ for $j_1 = j_2 = \tfrac12$ read off from the decomposition above:

从上述分解中读出的 $j_1 = j_2 = \tfrac12$ 的 Clebsch–Gordan 系数 $\langle j_1, m_1; j_2, m_2 | J, M\rangle$：

$$ \begin{aligned} |J = 1, M = +1\rangle: &\quad \langle +\tfrac12, +\tfrac12 | 1, +1\rangle = 1. \\ |J = 1, M = 0\rangle: &\quad \langle +\tfrac12, -\tfrac12 | 1, 0\rangle = \tfrac{1}{\sqrt2}, \quad \langle -\tfrac12, +\tfrac12 | 1, 0\rangle = \tfrac{1}{\sqrt2}. \\ |J = 1, M = -1\rangle: &\quad \langle -\tfrac12, -\tfrac12 | 1, -1\rangle = 1. \\ |J = 0, M = 0\rangle: &\quad \langle +\tfrac12, -\tfrac12 | 0, 0\rangle = \tfrac{1}{\sqrt2}, \quad \langle -\tfrac12, +\tfrac12 | 0, 0\rangle = -\tfrac{1}{\sqrt2}. \end{aligned} $$

All other coefficients vanish (since the tensor product state must have $m_1 + m_2 = M$).

所有其他系数为零（因为张量积态必须满足 $m_1 + m_2 = M$）。

**Physical meaning.** The singlet $(1/\sqrt2)(|+-\rangle - |-+\rangle)$ is antisymmetric under exchange of the two particles' spin states, while all three triplet states are symmetric. This antisymmetric singlet is the building block of Cooper pairs in BCS superconductivity (two electrons with opposite spins and momenta).

**物理含义。** 单态 $(1/\sqrt2)(|+-\rangle - |-+\rangle)$ 在交换两粒子自旋态下是反对称的，而三个三重态均为对称的。这个反对称单态是 BCS 超导中库珀对的基本结构（两个自旋和动量相反的电子）。

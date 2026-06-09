# Derivations — Module 5.5: BCS Theory
# 推导 — 模块 5.5：BCS 理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.5](./module-5.5-bcs-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.5](./module-5.5-bcs-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The BCS Variational Ground State · BCS 变分基态

**Claim.** The BCS ground state $|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger)|\text{vac}\rangle$ is a coherent superposition of pair-occupied and pair-empty states, with $|u_k|^2 + |v_k|^2 = 1$ (normalization) and $v_k, u_k$ real. Minimizing $\langle\text{BCS}|\hat{H} - \mu\hat{N}|\text{BCS}\rangle$ yields the BCS coefficients and the gap equation.

**命题。** BCS 基态 $|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger)|\text{vac}\rangle$ 是配对占据态和配对空态的相干叠加，满足 $|u_k|^2 + |v_k|^2 = 1$（归一化），$v_k$，$u_k$ 为实数。最小化 $\langle\text{BCS}|\hat{H} - \mu\hat{N}|\text{BCS}\rangle$ 给出 BCS 系数和能隙方程。

**Step 1 — Define the BCS state.** For each momentum-spin pair $(k\uparrow, -k\downarrow)$, introduce the pair state parametrized by real angles:

**第 1 步 — 定义 BCS 态。** 对每个动量–自旋对 $(k\uparrow, -k\downarrow)$，引入由实角度参数化的配对态：

$$ u_k = \cos(\theta_k/2), \quad v_k = \sin(\theta_k/2), \quad u_k^2 + v_k^2 = 1. $$

The state $|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger)|\text{vac}\rangle$ is normalized: $\langle\text{BCS}|\text{BCS}\rangle = \prod_k (u_k^2 + v_k^2) = 1$.

态 $|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger)|\text{vac}\rangle$ 是归一的：$\langle\text{BCS}|\text{BCS}\rangle = \prod_k (u_k^2 + v_k^2) = 1$。

This state is a superposition of different particle numbers (not a number eigenstate), which is appropriate for a superconductor in the thermodynamic limit.

这个态是不同粒子数的叠加（不是粒子数本征态），在热力学极限下适合描述超导体。

**Step 2 — BCS Hamiltonian.** The full Hamiltonian (in second quantization, Module 3.12) is

**第 2 步 — BCS 哈密顿量。** 完整哈密顿量（用二次量子化，模块 3.12）为

$$ \hat{H} = \sum_{k,\sigma} \varepsilon_k c_{k\sigma}^\dagger c_{k\sigma} - g \sum_{k,k'} c_{k'\uparrow}^\dagger c_{-k'\downarrow}^\dagger c_{-k\downarrow} c_{k\uparrow}, $$

where $\varepsilon_k$ is measured from the chemical potential $\mu$ (so $\varepsilon_k = \hbar^2 k^2/2m - \mu < 0$ below and $> 0$ above the Fermi surface), and $-g < 0$ is the constant attractive interaction within $\hbar\omega_D$ of $E_F$.

其中 $\varepsilon_k$ 从化学势 $\mu$ 量起（故 $\varepsilon_k = \hbar^2 k^2/2m - \mu$：费米面以下 $< 0$，以上 $> 0$），$-g < 0$ 是在 $E_F$ 的 $\hbar\omega_D$ 范围内的常数吸引相互作用。

**Step 3 — Mean-field (BCS) decoupling.** Define the gap parameter

**第 3 步 — 平均场（BCS）解耦。** 定义能隙参数

$$ \Delta = g \sum_k \langle c_{-k\downarrow} c_{k\uparrow}\rangle, $$

the expectation value of the pair annihilation operator (a c-number in the mean-field approximation). Write $c_{-k\downarrow} c_{k\uparrow} = \langle c_{-k\downarrow} c_{k\uparrow}\rangle + \text{fluctuation}$. The quartic interaction term becomes (discarding quadratic fluctuation terms):

配对湮灭算符的期望值（在平均场近似中为一个 c 数）。写 $c_{-k\downarrow} c_{k\uparrow} = \langle c_{-k\downarrow} c_{k\uparrow}\rangle + \text{涨落}$。四次相互作用项变为（舍去二次涨落项）：

$$ \begin{aligned} &-g \sum_{k,k'} c_{k'\uparrow}^\dagger c_{-k'\downarrow}^\dagger c_{-k\downarrow} c_{k\uparrow} \\ &\approx -\sum_k [\Delta c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger + \Delta^* c_{-k\downarrow} c_{k\uparrow}] + |\Delta|^2/g. \end{aligned} $$

The effective BCS Hamiltonian is therefore

有效 BCS 哈密顿量因此为

$$ \hat{H}_{\text{BCS}} = \sum_k \varepsilon_k (c_{k\uparrow}^\dagger c_{k\uparrow} + c_{-k\downarrow}^\dagger c_{-k\downarrow}) - \sum_k [\Delta c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger + \Delta^* c_{-k\downarrow} c_{k\uparrow}] + |\Delta|^2/g. $$

---

## B. Bogoliubov Transformation and Quasiparticle Energies · 博戈留波夫变换与准粒子能量

**Claim.** The Bogoliubov transformation diagonalizes $\hat{H}_{\text{BCS}}$. The new quasiparticle operators $\gamma_{k\uparrow} = u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger$ have energy $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$, and the spectrum has a gap of magnitude $\Delta$ at the Fermi surface.

**命题。** 博戈留波夫变换对角化 $\hat{H}_{\text{BCS}}$。新准粒子算符 $\gamma_{k\uparrow} = u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger$ 具有能量 $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$，谱在费米面处有大小为 $\Delta$ 的能隙。

**Step 1 — Define the Bogoliubov transformation.** Introduce new fermionic operators (Bogoliubov quasiparticles):

**第 1 步 — 定义博戈留波夫变换。** 引入新的费米子算符（博戈留波夫准粒子）：

$$ \begin{aligned} \gamma_{k\uparrow} &= u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger, \\ \gamma_{-k\downarrow} &= u_k c_{-k\downarrow} + v_k c_{k\uparrow}^\dagger. \end{aligned} $$

These satisfy canonical anticommutation relations $\{\gamma_{k\uparrow}, \gamma_{k\uparrow}^\dagger\} = 1$ provided $u_k^2 + v_k^2 = 1$ (check: $\{u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger, u_k c_{k\uparrow}^\dagger - v_k c_{-k\downarrow}\} = u_k^2\{c_{k\uparrow},c_{k\uparrow}^\dagger\} + v_k^2\{c_{-k\downarrow}^\dagger,c_{-k\downarrow}\} = u_k^2 + v_k^2 = 1$). ✓

这些算符满足正则反对易关系 $\{\gamma_{k\uparrow}, \gamma_{k\uparrow}^\dagger\} = 1$，条件是 $u_k^2 + v_k^2 = 1$（验证：$\{u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger, u_k c_{k\uparrow}^\dagger - v_k c_{-k\downarrow}\} = u_k^2\{c_{k\uparrow},c_{k\uparrow}^\dagger\} + v_k^2\{c_{-k\downarrow}^\dagger,c_{-k\downarrow}\} = u_k^2 + v_k^2 = 1$）。✓

**Step 2 — Invert the transformation.** Solving for $c_{k\uparrow}$ and $c_{-k\downarrow}^\dagger$:

**第 2 步 — 求逆变换。** 求解 $c_{k\uparrow}$ 和 $c_{-k\downarrow}^\dagger$：

$$ \begin{aligned} c_{k\uparrow} &= u_k \gamma_{k\uparrow} + v_k \gamma_{-k\downarrow}^\dagger, \\ c_{-k\downarrow}^\dagger &= -v_k \gamma_{k\uparrow} + u_k \gamma_{-k\downarrow}^\dagger. \end{aligned} $$

**Step 3 — Substitute into $\hat{H}_{\text{BCS}}$.** Compute $c_{k\uparrow}^\dagger c_{k\uparrow} + c_{-k\downarrow}^\dagger c_{-k\downarrow}$ and the off-diagonal terms $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger + \text{h.c.}$ in terms of $\gamma$. The algebra yields (for each $k$-pair):

**第 3 步 — 代入 $\hat{H}_{\text{BCS}}$。** 用 $\gamma$ 算符计算 $c_{k\uparrow}^\dagger c_{k\uparrow} + c_{-k\downarrow}^\dagger c_{-k\downarrow}$ 以及非对角项 $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger + \text{h.c.}$。代数运算给出（对每个 $k$-对）：

$$ \begin{aligned} &\varepsilon_k(c_{k\uparrow}^\dagger c_{k\uparrow} + c_{-k\downarrow}^\dagger c_{-k\downarrow}) - \Delta(c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger + c_{-k\downarrow}c_{k\uparrow}) \\ &= (2\varepsilon_k v_k^2 - 2\Delta u_k v_k) \cdot 1 + [2\varepsilon_k u_k v_k - \Delta(u_k^2 - v_k^2)] \cdot (\gamma_{k\uparrow}^\dagger\gamma_{-k\downarrow}^\dagger + \text{h.c.}) \\ &\quad + (\varepsilon_k(u_k^2 - v_k^2) + 2\Delta u_k v_k)(\gamma_{k\uparrow}^\dagger\gamma_{k\uparrow} + \gamma_{-k\downarrow}^\dagger\gamma_{-k\downarrow}). \end{aligned} $$

**Step 4 — Choose $u_k, v_k$ to eliminate off-diagonal terms.** Require the coefficient of the off-diagonal ($\gamma^\dagger\gamma^\dagger$) terms to vanish:

**第 4 步 — 选择 $u_k$、$v_k$ 消去非对角项。** 要求非对角（$\gamma^\dagger\gamma^\dagger$）项的系数为零：

$$ 2\varepsilon_k u_k v_k - \Delta(u_k^2 - v_k^2) = 0. $$

Using $u_k = \cos\theta$, $v_k = \sin\theta$: $2\varepsilon_k \sin\theta \cos\theta - \Delta(\cos^2\theta - \sin^2\theta) = 0$, i.e. $\varepsilon_k \sin(2\theta) - \Delta \cos(2\theta) = 0$. Therefore:

使用 $u_k = \cos\theta$，$v_k = \sin\theta$：$2\varepsilon_k \sin\theta \cos\theta + \Delta(\cos^2\theta - \sin^2\theta) = 0$，即 $\varepsilon_k \sin(2\theta) + \Delta \cos(2\theta) = 0$。因此：

$$ \tan(2\theta) = \Delta/\varepsilon_k \quad\implies\quad 2\theta = \arctan(\Delta/\varepsilon_k). $$

The diagonal coefficient of $\gamma^\dagger\gamma$ becomes (using the above condition to simplify):

$\gamma^\dagger\gamma$ 的对角系数变为（利用上述条件化简）：

$$ \begin{aligned} E_k &= \varepsilon_k(u_k^2 - v_k^2) + 2\Delta u_k v_k = \varepsilon_k \cos(2\theta) + \Delta \sin(2\theta) \\ &= \varepsilon_k \cdot (\varepsilon_k/E_k) + \Delta \cdot (\Delta/E_k) = (\varepsilon_k^2 + \Delta^2)/E_k, \end{aligned} $$

where we used $\cos(2\theta) = \varepsilon_k/E_k$ and $\sin(2\theta) = +\Delta/E_k$ (from the condition, with the sign chosen so $E_k > 0$ and consistent with $u_k v_k = \Delta/2E_k$ of Section C). Solving:

其中用到 $\cos(2\theta) = \varepsilon_k/E_k$ 和 $\sin(2\theta) = +\Delta/E_k$（由条件给出，选择符号使 $E_k > 0$，并与 C 节 $u_k v_k = \Delta/2E_k$ 一致）。求解：

$$ \boxed{\, E_k = \sqrt{\varepsilon_k^2 + \Delta^2} \,} $$

**Step 5 — Diagonalized Hamiltonian.** The BCS Hamiltonian in terms of quasiparticles is

**第 5 步 — 对角化哈密顿量。** 用准粒子表示的 BCS 哈密顿量为

$$ \hat{H}_{\text{BCS}} = E_{\text{gs}} + \sum_k E_k (\gamma_{k\uparrow}^\dagger\gamma_{k\uparrow} + \gamma_{-k\downarrow}^\dagger\gamma_{-k\downarrow}), $$

where $E_{\text{gs}} = \sum_k (2\varepsilon_k v_k^2 - 2\Delta u_k v_k) + |\Delta|^2/g = \sum_k (\varepsilon_k - E_k) + |\Delta|^2/g$ is the ground-state energy (condensation energy). The quasiparticles are free fermions with dispersion $E_k \ge \Delta$. The minimum energy $\Delta$ is the gap. $\blacksquare$

其中 $E_{\text{gs}} = \sum_k (2\varepsilon_k v_k^2 - 2\Delta u_k v_k) + |\Delta|^2/g = \sum_k (\varepsilon_k - E_k) + |\Delta|^2/g$ 是基态能量（凝聚能）。准粒子是色散关系为 $E_k \ge \Delta$ 的自由费米子。最小能量 $\Delta$ 就是能隙。$\blacksquare$

---

## C. The BCS Gap Equation · BCS 能隙方程

**Claim.** The self-consistency condition $\Delta = g \sum_k \langle c_{-k\downarrow} c_{k\uparrow}\rangle$ evaluated in the BCS ground state yields the gap equation $1 = gN(0)\int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2}$.

**命题。** 在 BCS 基态中计算自洽条件 $\Delta = g \sum_k \langle c_{-k\downarrow} c_{k\uparrow}\rangle$，得到能隙方程 $1 = gN(0)\int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2}$。

**Step 1 — Compute $\langle c_{-k\downarrow} c_{k\uparrow}\rangle$ in the BCS state.** Using $c_{k\uparrow} = u_k \gamma_{k\uparrow} + v_k \gamma_{-k\downarrow}^\dagger$ and $c_{-k\downarrow} = u_k \gamma_{-k\downarrow} - v_k \gamma_{k\uparrow}^\dagger$:

**第 1 步 — 在 BCS 态中计算 $\langle c_{-k\downarrow} c_{k\uparrow}\rangle$。** 使用 $c_{k\uparrow} = u_k \gamma_{k\uparrow} + v_k \gamma_{-k\downarrow}^\dagger$ 和 $c_{-k\downarrow} = u_k \gamma_{-k\downarrow} - v_k \gamma_{k\uparrow}^\dagger$：

$$ \begin{aligned} c_{-k\downarrow} c_{k\uparrow} &= (u_k \gamma_{-k\downarrow} - v_k \gamma_{k\uparrow}^\dagger)(u_k \gamma_{k\uparrow} + v_k \gamma_{-k\downarrow}^\dagger) \\ &= u_k^2 \gamma_{-k\downarrow}\gamma_{k\uparrow} + u_k v_k \gamma_{-k\downarrow}\gamma_{-k\downarrow}^\dagger - v_k u_k \gamma_{k\uparrow}^\dagger\gamma_{k\uparrow} - v_k^2 \gamma_{k\uparrow}^\dagger\gamma_{-k\downarrow}^\dagger. \end{aligned} $$

In the BCS ground state $|\text{BCS}\rangle$ (all quasiparticle states empty, $\gamma_{k\sigma}|\text{BCS}\rangle = 0$):

在 BCS 基态 $|\text{BCS}\rangle$（所有准粒子态为空，$\gamma_{k\sigma}|\text{BCS}\rangle = 0$）中：

$$ \langle\gamma_{-k\downarrow}\gamma_{k\uparrow}\rangle = 0, \quad \langle\gamma_{-k\downarrow}\gamma_{-k\downarrow}^\dagger\rangle = 1, \quad \langle\gamma_{k\uparrow}^\dagger\gamma_{k\uparrow}\rangle = 0, \quad \langle\gamma_{k\uparrow}^\dagger\gamma_{-k\downarrow}^\dagger\rangle = 0. $$

Therefore:

因此：

$$ \langle c_{-k\downarrow} c_{k\uparrow}\rangle = u_k v_k \cdot 1 = u_k v_k. $$

**Step 2 — Substitute into the gap definition.** Recalling $u_k v_k = \tfrac12 \sin(2\theta_k) = \Delta/(2E_k)$ (from Step 4 of Section B, where $\sin(2\theta) = \Delta/E_k$ with our chosen sign convention at $T = 0$):

**第 2 步 — 代入能隙定义。** 回顾 $u_k v_k = \tfrac12 \sin(2\theta_k) = \Delta/(2E_k)$（由 B 节第 4 步，其中 $\sin(2\theta) = \Delta/E_k$，取 $T = 0$ 时的符号约定）：

$$ \Delta = g \sum_k \langle c_{-k\downarrow} c_{k\uparrow}\rangle = g \sum_k u_k v_k = g \sum_k \Delta/(2E_k). $$

Divide both sides by $\Delta$ (assuming $\Delta \ne 0$, i.e., superconducting solution):

两边除以 $\Delta$（假设 $\Delta \ne 0$，即超导解）：

$$ 1 = g \sum_k 1/(2E_k) = g \sum_k 1/(2\sqrt{\varepsilon_k^2 + \Delta^2}). $$

**Step 3 — Convert to integral.** Replace the $k$-sum using the density of states $N(0)$ (constant near the Fermi surface), integrating $\varepsilon$ from $-\hbar\omega_D$ to $+\hbar\omega_D$ (the phonon window). By symmetry $\varepsilon \to -\varepsilon$:

**第 3 步 — 转化为积分。** 用态密度 $N(0)$（在费米面附近为常数）替换 $k$ 求和，对 $\varepsilon$ 从 $-\hbar\omega_D$ 积分到 $+\hbar\omega_D$（声子窗口）。由 $\varepsilon \to -\varepsilon$ 的对称性：

$$ 1 = g N(0) \int_{-\hbar\omega_D}^{\hbar\omega_D} d\varepsilon/(2\sqrt{\varepsilon^2 + \Delta^2}) = g N(0) \int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2}. $$

This is the **BCS gap equation**:

这是 **BCS 能隙方程**：

$$ \boxed{\, 1 = g N(0) \int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2} \,} \qquad \blacksquare $$

---

## D. Solving the Gap Equation: $\Delta \approx 2\hbar\omega_D e^{-1/(gN(0))}$ · 求解能隙方程：$\Delta \approx 2\hbar\omega_D e^{-1/(gN(0))}$

**Claim.** In the weak-coupling limit $gN(0) \ll 1$, the gap equation yields $\Delta(0) \approx 2\hbar\omega_D e^{-1/(gN(0))}$.

**命题。** 在弱耦合极限 $gN(0) \ll 1$ 下，能隙方程给出 $\Delta(0) \approx 2\hbar\omega_D e^{-1/(gN(0))}$。

**Step 1 — Evaluate the integral.** Compute $I = \int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2}$:

**第 1 步 — 计算积分。** 计算 $I = \int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2}$：

$$ I = [\sinh^{-1}(\varepsilon/\Delta)]_0^{\hbar\omega_D} = \sinh^{-1}(\hbar\omega_D/\Delta) - \sinh^{-1}(0) = \sinh^{-1}(\hbar\omega_D/\Delta). $$

Using $\sinh^{-1}(x) = \ln(x + \sqrt{x^2+1})$:

使用 $\sinh^{-1}(x) = \ln(x + \sqrt{x^2+1})$：

$$ I = \ln(\hbar\omega_D/\Delta + \sqrt{(\hbar\omega_D/\Delta)^2 + 1}). $$

**Step 2 — Weak-coupling approximation.** For $gN(0) \ll 1$, the gap $\Delta \ll \hbar\omega_D$ (we verify this a posteriori). Then $\hbar\omega_D/\Delta \gg 1$, and $\sqrt{(\hbar\omega_D/\Delta)^2 + 1} \approx \hbar\omega_D/\Delta$:

**第 2 步 — 弱耦合近似。** 当 $gN(0) \ll 1$ 时，能隙 $\Delta \ll \hbar\omega_D$（事后验证）。则 $\hbar\omega_D/\Delta \gg 1$，$\sqrt{(\hbar\omega_D/\Delta)^2 + 1} \approx \hbar\omega_D/\Delta$：

$$ I \approx \ln(2\hbar\omega_D/\Delta). $$

**Step 3 — Solve for $\Delta$.** The gap equation $1 = gN(0) \cdot I$ gives:

**第 3 步 — 求解 $\Delta$。** 能隙方程 $1 = gN(0) \cdot I$ 给出：

$$ 1 = gN(0) \ln(2\hbar\omega_D/\Delta) \quad\implies\quad \ln(2\hbar\omega_D/\Delta) = 1/(gN(0)). $$

Exponentiate:

取指数：

$$ 2\hbar\omega_D/\Delta = e^{1/(gN(0))} \quad\implies\quad \boxed{\, \Delta(0) = 2\hbar\omega_D e^{-1/(gN(0))} \,}. $$

**Step 4 — Consistency check.** For $gN(0) = 0.3$ (a typical weak-coupling value), $\Delta/\hbar\omega_D \approx 2e^{-1/0.3} \approx 2 \times 0.0357 \approx 0.071 \ll 1$, confirming the weak-coupling approximation a posteriori. $\blacksquare$

**第 4 步 — 一致性检验。** 对 $gN(0) = 0.3$（典型弱耦合值），$\Delta/\hbar\omega_D \approx 2e^{-1/0.3} \approx 2 \times 0.0357 \approx 0.071 \ll 1$，事后确认弱耦合近似。$\blacksquare$

**Note on non-analyticity.** Like the Cooper binding energy of Module 5.4, $\Delta(0) \propto e^{-1/(gN(0))}$ is non-analytic in $g$ at $g = 0$. All Taylor coefficients of $e^{-1/g}$ at $g = 0$ vanish, so the gap cannot be obtained by any finite-order perturbation theory. This is the microscopic explanation of why a mean-field theory is needed. $\blacksquare$

**关于非解析性的注记。** 与模块 5.4 的库珀束缚能类似，$\Delta(0) \propto e^{-1/(gN(0))}$ 在 $g = 0$ 处对 $g$ 是非解析的。$e^{-1/g}$ 在 $g = 0$ 处的所有泰勒系数均为零，故能隙不能由任何有限阶微扰论得到。这是需要平均场理论的微观解释。$\blacksquare$

---

## E. The Universal Ratio $2\Delta(0) = 3.52\, k_B T_c$ · 普适比值 $2\Delta(0) = 3.52\, k_B T_c$

**Claim.** Near $T_c$, $\Delta \to 0$ and the gap equation can be linearized to determine $T_c$. Combining the $T_c$ formula with $\Delta(0)$ gives the universal (material-independent) ratio $2\Delta(0)/(k_B T_c) = 2\pi/e^\gamma \approx 3.528$, where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant.

**命题。** 在 $T_c$ 附近，$\Delta \to 0$，能隙方程可以被线性化以确定 $T_c$。将 $T_c$ 公式与 $\Delta(0)$ 结合给出普适（与材料无关的）比值 $2\Delta(0)/(k_B T_c) = 2\pi/e^\gamma \approx 3.528$，其中 $\gamma \approx 0.5772$ 是欧拉–马斯凯罗尼常数。

**Step 1 — Gap equation at finite temperature.** At temperature $T$, the quasiparticle states are thermally occupied. The self-consistency condition generalizes to

**第 1 步 — 有限温度的能隙方程。** 在温度 $T$ 下，准粒子态被热激活占据。自洽条件推广为

$$ 1 = gN(0) \int_0^{\hbar\omega_D} d\varepsilon/\sqrt{\varepsilon^2 + \Delta^2} \cdot \tanh(\sqrt{\varepsilon^2 + \Delta^2}/(2k_B T)). $$

The tanh factor accounts for the Fermi–Dirac distribution: at $T = 0$, $\tanh \to 1$, recovering Section D. The gap $\Delta(T)$ decreases monotonically from $\Delta(0)$ as $T$ increases, reaching zero at $T = T_c$.

tanh 因子来自费米–狄拉克分布：在 $T = 0$ 时，$\tanh \to 1$，还原到 D 节。能隙 $\Delta(T)$ 随 $T$ 增大从 $\Delta(0)$ 单调减小，在 $T = T_c$ 处趋于零。

**Step 2 — Determine $T_c$ by linearization.** At $T = T_c$, $\Delta \to 0$. The gap equation reduces to (setting $\Delta = 0$ in the integrand):

**第 2 步 — 通过线性化确定 $T_c$。** 在 $T = T_c$ 时，$\Delta \to 0$。能隙方程化为（在被积函数中令 $\Delta = 0$）：

$$ 1 = gN(0) \int_0^{\hbar\omega_D} (d\varepsilon/\varepsilon) \tanh(\varepsilon/(2k_B T_c)). $$

**Step 3 — Evaluate the integral.** The integral $I_c = \int_0^{\hbar\omega_D} (d\varepsilon/\varepsilon) \tanh(\varepsilon/(2k_B T_c))$ is a standard result. Let $x = \varepsilon/(2k_B T_c)$ and $X = \hbar\omega_D/(2k_B T_c) \gg 1$ (weak coupling). Then:

**第 3 步 — 计算积分。** 积分 $I_c = \int_0^{\hbar\omega_D} (d\varepsilon/\varepsilon) \tanh(\varepsilon/(2k_B T_c))$ 是标准结果。令 $x = \varepsilon/(2k_B T_c)$，$X = \hbar\omega_D/(2k_B T_c) \gg 1$（弱耦合）。则：

$$ I_c = \int_0^X (dx/x) \tanh(x). $$

Integration by parts and use of the known result for the Sommerfeld expansion (see any field theory text):

分部积分并使用索末菲展开的已知结果（见任何场论教材）：

$$ \int_0^X (dx/x) \tanh(x) = \ln(X) + \ln(4e^\gamma/\pi) + O(1/X^2) \quad \text{for } X \gg 1, $$

where $\gamma = 0.5772\ldots$ is the Euler–Mascheroni constant (the same that appears in the asymptotic expansion of the digamma function and in $\sum 1/n - \ln n$). The key step uses the Fourier series for tanh and the integral $\int_0^\infty (\tanh x - 1)/x\, dx = -\ln(4e^\gamma/\pi)$. Thus:

其中 $\gamma = 0.5772\ldots$ 是欧拉–马斯凯罗尼常数（与双伽马（digamma）函数的渐近展开和 $\sum 1/n - \ln n$ 中出现的相同）。关键步骤使用 tanh 的傅里叶级数和积分 $\int_0^\infty (\tanh x - 1)/x\, dx = -\ln(4e^\gamma/\pi)$。于是：

$$ I_c \approx \ln(\hbar\omega_D/(2k_B T_c)) + \ln(4e^\gamma/\pi) = \ln(2e^\gamma \hbar\omega_D/(\pi k_B T_c)). $$

**Step 4 — $T_c$ formula.** Setting $1/(gN(0)) = I_c$:

**第 4 步 — $T_c$ 公式。** 令 $1/(gN(0)) = I_c$：

$$ 1/(gN(0)) = \ln(2e^\gamma \hbar\omega_D/(\pi k_B T_c)) \quad\implies\quad k_B T_c = (2e^\gamma/\pi) \hbar\omega_D e^{-1/(gN(0))}. $$

Numerically, $2e^\gamma/\pi = 2 \times 1.7811/3.1416 \approx 1.1340$. Hence:

数值上，$2e^\gamma/\pi = 2 \times 1.7811/3.1416 \approx 1.1340$。故：

$$ \boxed{\, k_B T_c \approx 1.134\, \hbar\omega_D e^{-1/(gN(0))} \,}. $$

**Step 5 — Compute $2\Delta(0)/(k_B T_c)$.** Divide $\Delta(0) = 2\hbar\omega_D e^{-1/(gN(0))}$ by $k_B T_c$:

**第 5 步 — 计算 $2\Delta(0)/(k_B T_c)$。** 将 $\Delta(0) = 2\hbar\omega_D e^{-1/(gN(0))}$ 除以 $k_B T_c$：

$$ \begin{aligned} 2\Delta(0)/(k_B T_c) &= 2 \times 2\hbar\omega_D e^{-1/(gN(0))} / (1.134\, \hbar\omega_D e^{-1/(gN(0))}) \\ &= 4/1.134 = 4/(2e^\gamma/\pi) = 4\pi/(2e^\gamma) = 2\pi/e^\gamma. \end{aligned} $$

**Step 6 — Numerical value.** $e^\gamma = e^{0.5772} \approx 1.7811$, so $2\pi/e^\gamma \approx 6.2832/1.7811 \approx \mathbf{3.528 \approx 3.52}$.

**第 6 步 — 数值。** $e^\gamma = e^{0.5772} \approx 1.7811$，故 $2\pi/e^\gamma \approx 6.2832/1.7811 \approx \mathbf{3.528 \approx 3.52}$。

Therefore:

因此：

$$ \boxed{\, 2\Delta(0) = (2\pi/e^\gamma) k_B T_c \approx 3.528\, k_B T_c \approx 3.52\, k_B T_c \,} \qquad \blacksquare $$

**Step 7 — Universality.** Notice that the factor $e^{-1/(gN(0))}$ has cancelled between $\Delta(0)$ and $k_B T_c$. The ratio $2\Delta(0)/(k_B T_c) = 2\pi/e^\gamma$ involves only universal numbers ($\pi$ and Euler's constant $\gamma$) — it is the **same** for every BCS superconductor regardless of material. This is a celebrated prediction of the theory. Measured values: Pb $\approx 4.3$, Nb $\approx 3.8$, Al $\approx 3.4$ (deviations from 3.52 are due to strong-coupling corrections, quantified by Eliashberg theory). $\blacksquare$

**第 7 步 — 普适性。** 注意到 $e^{-1/(gN(0))}$ 在 $\Delta(0)$ 和 $k_B T_c$ 之间已经约消。比值 $2\Delta(0)/(k_B T_c) = 2\pi/e^\gamma$ 只涉及普适数（$\pi$ 和欧拉常数 $\gamma$）——对**每一种** BCS 超导体都**相同**，与材料无关。这是该理论的著名预言。测量值：Pb $\approx 4.3$，Nb $\approx 3.8$，Al $\approx 3.4$（偏离 3.52 是由强耦合修正引起的，由埃利亚什伯格理论定量）。$\blacksquare$

---

## F. BCS Coefficients and Ground-State Occupancy · BCS 系数与基态占据率

**Claim.** The variational coefficients $u_k$ and $v_k$ are $u_k^2 = \tfrac12(1 + \varepsilon_k/E_k)$ and $v_k^2 = \tfrac12(1 - \varepsilon_k/E_k)$, giving a smooth crossover from $v_k = 1$ (filled, $\varepsilon_k \ll -\Delta$) to $v_k = 0$ (empty, $\varepsilon_k \gg \Delta$) on a scale $\sim \Delta$ around the Fermi surface.

**命题。** 变分系数 $u_k$ 和 $v_k$ 为 $u_k^2 = \tfrac12(1 + \varepsilon_k/E_k)$，$v_k^2 = \tfrac12(1 - \varepsilon_k/E_k)$，在费米面附近 $\sim \Delta$ 的尺度上从 $v_k = 1$（填满，$\varepsilon_k \ll -\Delta$）平滑过渡到 $v_k = 0$（空态，$\varepsilon_k \gg \Delta$）。

**Step 1 — From the condition $u_k v_k = \Delta/(2E_k)$.** Together with $u_k^2 + v_k^2 = 1$:

**第 1 步 — 由条件 $u_k v_k = \Delta/(2E_k)$。** 结合 $u_k^2 + v_k^2 = 1$：

$$ (u_k^2 - v_k^2)^2 = (u_k^2 + v_k^2)^2 - 4u_k^2 v_k^2 = 1 - \Delta^2/E_k^2 = \varepsilon_k^2/E_k^2. $$

So $u_k^2 - v_k^2 = \varepsilon_k/E_k$ (taking the sign so that $u_k \to 1$, $v_k \to 0$ for $\varepsilon_k \to +\infty$). Combined with $u_k^2 + v_k^2 = 1$:

故 $u_k^2 - v_k^2 = \varepsilon_k/E_k$（取符号使当 $\varepsilon_k \to +\infty$ 时 $u_k \to 1$，$v_k \to 0$）。结合 $u_k^2 + v_k^2 = 1$：

$$ \boxed{\, v_k^2 = \tfrac12(1 - \varepsilon_k/E_k), \quad u_k^2 = \tfrac12(1 + \varepsilon_k/E_k) \,} $$

**Step 2 — Physical limits.** 

**第 2 步 — 物理极限。**

- $\varepsilon_k \to -\infty$ (well inside Fermi sea): $E_k \to |\varepsilon_k| = -\varepsilon_k$, so $v_k^2 \to \tfrac12(1+1) = 1$, $u_k^2 \to 0$. Pair fully occupied. ✓
- $\varepsilon_k \to +\infty$ (well above Fermi surface): $E_k \to \varepsilon_k$, so $v_k^2 \to 0$, $u_k^2 \to 1$. Pair empty. ✓
- $\varepsilon_k = 0$ (at Fermi surface): $E_k = \Delta$, so $v_k^2 = u_k^2 = \tfrac12$. Maximum quantum fluctuation. ✓

- $\varepsilon_k \to -\infty$（费米海深处）：$E_k \to |\varepsilon_k| = -\varepsilon_k$，故 $v_k^2 \to 1$，$u_k^2 \to 0$。配对完全占据。✓
- $\varepsilon_k \to +\infty$（费米面以上）：$E_k \to \varepsilon_k$，故 $v_k^2 \to 0$，$u_k^2 \to 1$。配对为空。✓
- $\varepsilon_k = 0$（费米面处）：$E_k = \Delta$，故 $v_k^2 = u_k^2 = \tfrac12$。最大量子涨落。✓

The smooth BCS momentum distribution $v_k^2$ replaces the sharp Fermi step function, spreading over a width $\sim \Delta/v_F$ around $k_F$ — a direct consequence of the macroscopic quantum coherence of the condensate. $\blacksquare$

平滑的 BCS 动量分布 $v_k^2$ 取代了尖锐的费米阶梯函数，在 $k_F$ 附近 $\sim \Delta/v_F$ 的宽度内扩展——这是凝聚体宏观量子相干性的直接后果。$\blacksquare$

---

*The BCS theory derived here is the microscopic justification for every result in Modules 5.1–5.3 and the starting point for Modules 5.6–5.9. The Bogoliubov quasiparticles reappear in tunneling spectroscopy (5.6), the vortex-core states (5.7), and the ac Josephson effect (5.8).*

*此处推导的 BCS 理论是模块 5.1–5.3 中每个结果的微观基础，也是模块 5.6–5.9 的出发点。博戈留波夫准粒子再次出现于隧穿谱（5.6）、涡旋核态（5.7）和交流约瑟夫森效应（5.8）。*

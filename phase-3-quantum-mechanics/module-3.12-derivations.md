# Derivations — Module 3.12: Second Quantization
# 推导 — 模块 3.12：二次量子化

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.12](./module-3.12-second-quantization.md). Full step-by-step proofs. English first, then 中文.
> [模块 3.12](./module-3.12-second-quantization.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. Fock Space and the (Anti)commutation Algebra · 福克空间与（反）对易代数

**Step 1 — Occupation-number states.** Label single-particle modes by $k$. A many-body basis state is specified by the occupation numbers $|n_1, n_2, \dots\rangle$, with $n_k$ the number of particles in mode $k$. The **vacuum** $|0\rangle$ has all $n_k = 0$. Creation/annihilation operators act as $\hat{a}_k^\dagger|\dots n_k\dots\rangle \propto |\dots n_k+1\dots\rangle$ and $\hat{a}_k|\dots n_k\dots\rangle \propto |\dots n_k-1\dots\rangle$.

**第 1 步 — 占据数态。** 用 $k$ 标记单粒子模式。多体基态由占据数 $|n_1, n_2, \dots\rangle$ 指定，$n_k$ 为模式 $k$ 中的粒子数。**真空** $|0\rangle$ 满足所有 $n_k = 0$。产生/湮灭算符的作用为 $\hat{a}_k^\dagger|\dots n_k\dots\rangle \propto |\dots n_k+1\dots\rangle$ 与 $\hat{a}_k|\dots n_k\dots\rangle \propto |\dots n_k-1\dots\rangle$。

**Step 2 — Bosons (one oscillator per mode).** Postulate, by analogy with the harmonic oscillator of Module 3.2, the **commutation relations**

**第 2 步 — 玻色子（每个模式一个振子）。** 类比模块 3.2 的谐振子，假设**对易关系**

$$ [\hat{a}_k, \hat{a}_{k'}^\dagger] = \delta_{kk'}, \quad [\hat{a}_k, \hat{a}_{k'}] = 0, \quad [\hat{a}_k^\dagger, \hat{a}_{k'}^\dagger] = 0. $$

The number operator $\hat{n}_k = \hat{a}_k^\dagger\hat{a}_k$ then has, by exactly the ladder argument of Module 3.2, eigenvalues $n_k = 0, 1, 2, \dots$ (unbounded), with $\hat{a}_k^\dagger|n_k\rangle = \sqrt{n_k+1}|n_k+1\rangle$ and $\hat{a}_k|n_k\rangle = \sqrt{n_k}\, |n_k-1\rangle$. Bosons may pile up without limit.

数算符 $\hat{n}_k = \hat{a}_k^\dagger\hat{a}_k$ 由模块 3.2 的阶梯论证，本征值为 $n_k = 0, 1, 2, \dots$（无上界），且 $\hat{a}_k^\dagger|n_k\rangle = \sqrt{n_k+1}|n_k+1\rangle$、$\hat{a}_k|n_k\rangle = \sqrt{n_k}\, |n_k-1\rangle$。玻色子可无限堆积。

**Step 3 — Fermions.** For fermions, replace commutators by **anticommutators** $\{\hat{A},\hat{B}\} \equiv \hat{A}\hat{B} + \hat{B}\hat{A}$:

**第 3 步 — 费米子。** 对费米子，将对易子换成**反对易子** $\{\hat{A},\hat{B}\} \equiv \hat{A}\hat{B} + \hat{B}\hat{A}$：

$$ \{\hat{c}_k, \hat{c}_{k'}^\dagger\} = \delta_{kk'}, \quad \{\hat{c}_k, \hat{c}_{k'}\} = 0, \quad \{\hat{c}_k^\dagger, \hat{c}_{k'}^\dagger\} = 0. $$

---

## B. Anticommutation Enforces the Pauli Principle · 反对易强制泡利原理

**Step 1 — Nilpotency.** Set $k = k'$ in $\{\hat{c}_k^\dagger, \hat{c}_{k'}^\dagger\} = 0$: $2(\hat{c}_k^\dagger)^2 = 0$, hence $(\hat{c}_k^\dagger)^2 = 0$. You cannot create two fermions in the same mode — the **Pauli exclusion principle**, now an algebraic identity.

**第 1 步 — 幂零性。** 在 $\{\hat{c}_k^\dagger, \hat{c}_{k'}^\dagger\} = 0$ 中令 $k = k'$：$2(\hat{c}_k^\dagger)^2 = 0$，故 $(\hat{c}_k^\dagger)^2 = 0$。无法在同一模式产生两个费米子——**泡利不相容原理**，此处成为一个代数恒等式。

**Step 2 — Number operator has eigenvalues 0 and 1.** Let $\hat{n}_k = \hat{c}_k^\dagger\hat{c}_k$. Then

**第 2 步 — 数算符本征值只能是 0 和 1。** 令 $\hat{n}_k = \hat{c}_k^\dagger\hat{c}_k$。则

$$ \hat{n}_k^2 = \hat{c}_k^\dagger\hat{c}_k\hat{c}_k^\dagger\hat{c}_k = \hat{c}_k^\dagger(1 - \hat{c}_k^\dagger\hat{c}_k)\hat{c}_k = \hat{c}_k^\dagger\hat{c}_k - (\hat{c}_k^\dagger)^2\hat{c}_k^2 = \hat{c}_k^\dagger\hat{c}_k = \hat{n}_k, $$

using $\{\hat{c}_k, \hat{c}_k^\dagger\} = 1 \Rightarrow \hat{c}_k\hat{c}_k^\dagger = 1 - \hat{c}_k^\dagger\hat{c}_k$ and $(\hat{c}_k^\dagger)^2 = 0$. So $\hat{n}_k^2 = \hat{n}_k$, whose only eigenvalues are $n_k = 0$ or $1$. Each mode is empty or singly occupied — exactly the Pauli principle again.

其中用到 $\{\hat{c}_k, \hat{c}_k^\dagger\} = 1 \Rightarrow \hat{c}_k\hat{c}_k^\dagger = 1 - \hat{c}_k^\dagger\hat{c}_k$ 及 $(\hat{c}_k^\dagger)^2 = 0$。故 $\hat{n}_k^2 = \hat{n}_k$，本征值只能是 $n_k = 0$ 或 $1$。每个模式或空或单占——再次正是泡利原理。

**Step 3 — Antisymmetry of many-body states.** Build a two-fermion state $|\Psi\rangle = \hat{c}_1^\dagger\hat{c}_2^\dagger|0\rangle$. Exchanging the two creation operators uses $\{\hat{c}_1^\dagger, \hat{c}_2^\dagger\} = 0 \Rightarrow \hat{c}_1^\dagger\hat{c}_2^\dagger = -\hat{c}_2^\dagger\hat{c}_1^\dagger$, so

**第 3 步 — 多体态的反对称性。** 构造两费米子态 $|\Psi\rangle = \hat{c}_1^\dagger\hat{c}_2^\dagger|0\rangle$。交换两个产生算符时用 $\{\hat{c}_1^\dagger, \hat{c}_2^\dagger\} = 0 \Rightarrow \hat{c}_1^\dagger\hat{c}_2^\dagger = -\hat{c}_2^\dagger\hat{c}_1^\dagger$，故

$$ \hat{c}_1^\dagger\hat{c}_2^\dagger|0\rangle = -\hat{c}_2^\dagger\hat{c}_1^\dagger|0\rangle. $$

The state changes sign under particle exchange — it is **automatically antisymmetric**, reproducing the Slater determinant of Module 3.5 without bookkeeping. $\blacksquare$

该态在粒子交换下变号——**自动反对称**，无需额外记账即重现模块 3.5 的斯莱特行列式。$\blacksquare$

---

## C. Field Operators and Second-Quantized Hamiltonians · 场算符与二次量子化哈密顿量

**Step 1 — Field operators.** Define $\hat{\psi}(x) = \sum_k \varphi_k(x)\, \hat{c}_k$, where $\{\varphi_k\}$ is a single-particle basis. From the mode (anti)commutators and completeness $\sum_k \varphi_k(x)\varphi_k^*(x') = \delta(x-x')$, one gets the local relation $\{\hat{\psi}(x), \hat{\psi}^\dagger(x')\} = \delta(x-x')$ (fermions) or the commutator version (bosons).

**第 1 步 — 场算符。** 定义 $\hat{\psi}(x) = \sum_k \varphi_k(x)\, \hat{c}_k$，其中 $\{\varphi_k\}$ 为单粒子基。由模式（反）对易关系与完备性 $\sum_k \varphi_k(x)\varphi_k^*(x') = \delta(x-x')$，得到局域关系 $\{\hat{\psi}(x), \hat{\psi}^\dagger(x')\} = \delta(x-x')$（费米子）或对易子形式（玻色子）。

**Step 2 — One- and two-body operators.** A one-body operator $\hat{O}_1 = \sum_i \hat{o}(x_i)$ becomes $\int \hat{\psi}^\dagger(x)\, \hat{o}(x)\, \hat{\psi}(x)\, dx = \sum_{kl} \langle k|\hat{o}|l\rangle\, \hat{c}_k^\dagger\hat{c}_l$; a two-body interaction $V$ becomes $\tfrac12 \sum \langle kl|V|mn\rangle\, \hat{c}_k^\dagger\hat{c}_l^\dagger\hat{c}_n\hat{c}_m$. Particle number is automatically handled by the operators.

**第 2 步 — 单体与两体算符。** 单体算符 $\hat{O}_1 = \sum_i \hat{o}(x_i)$ 变为 $\int \hat{\psi}^\dagger(x)\, \hat{o}(x)\, \hat{\psi}(x)\, dx = \sum_{kl} \langle k|\hat{o}|l\rangle\, \hat{c}_k^\dagger\hat{c}_l$；两体相互作用 $V$ 变为 $\tfrac12 \sum \langle kl|V|mn\rangle\, \hat{c}_k^\dagger\hat{c}_l^\dagger\hat{c}_n\hat{c}_m$。粒子数由算符自动处理。

**Step 3 — Why this is the key tool.** The BCS Hamiltonian (Module 5.5) $H = \sum_k \varepsilon_k\, \hat{c}_k^\dagger\hat{c}_k - g \sum \hat{c}_{k'\uparrow}^\dagger\hat{c}_{-k'\downarrow}^\dagger\hat{c}_{-k\downarrow}\hat{c}_{k\uparrow}$ is written entirely in this language; the pair operator is $\hat{c}_{k\uparrow}^\dagger\hat{c}_{-k\downarrow}^\dagger$, and all of condensed-matter field theory (Phase 6) is built on these (anti)commutators. $\blacksquare$

**第 3 步 — 为何这是关键工具。** BCS 哈密顿量（模块 5.5）$H = \sum_k \varepsilon_k\, \hat{c}_k^\dagger\hat{c}_k - g \sum \hat{c}_{k'\uparrow}^\dagger\hat{c}_{-k'\downarrow}^\dagger\hat{c}_{-k\downarrow}\hat{c}_{k\uparrow}$ 完全用此语言书写；对算符为 $\hat{c}_{k\uparrow}^\dagger\hat{c}_{-k\downarrow}^\dagger$，而全部凝聚态场论（第 6 阶段）都建立在这些（反）对易关系之上。$\blacksquare$

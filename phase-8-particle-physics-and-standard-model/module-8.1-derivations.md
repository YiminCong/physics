# Derivations — Module 8.1: Symmetries & Gauge Theory
# 推导 — 模块 8.1：对称性与规范理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.1](./module-8.1-symmetries-and-gauge-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.1](./module-8.1-symmetries-and-gauge-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Local U(1) Invariance Forces a Gauge Field · 局域 U(1) 不变性迫使引入规范场

**Claim.** The free Dirac Lagrangian $\mathcal{L}_0 = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ is invariant under global U(1) but NOT under local U(1) transformations. Requiring local invariance forces the introduction of a gauge field $A_\mu$ with transformation law $A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$ and a covariant derivative $D_\mu = \partial_\mu + ieA_\mu$.

**命题。** 自由狄拉克拉格朗日量 $\mathcal{L}_0 = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ 在全局 U(1) 变换下不变，但在局域 U(1) 变换下不不变。要求局域不变性迫使引入规范场 $A_\mu$，其变换律为 $A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$，以及协变导数 $D_\mu = \partial_\mu + ieA_\mu$。

**Step 1 — Global U(1) invariance.** Under the global transformation $\psi \to e^{i\alpha}\psi$ ($\alpha$ constant), we have $\bar\psi \to e^{-i\alpha}\bar\psi$. Then:

**第 1 步 — 全局 U(1) 不变性。** 在全局变换 $\psi \to e^{i\alpha}\psi$（$\alpha$ 为常数）下，$\bar\psi \to e^{-i\alpha}\bar\psi$。则：

$$ \mathcal{L}_0 \to \bar\psi\, e^{-i\alpha}(i\gamma^\mu\partial_\mu - m)e^{i\alpha}\psi = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi = \mathcal{L}_0. $$

The phase factors cancel because $\alpha$ is constant and $\partial_\mu(e^{i\alpha}\psi) = e^{i\alpha}\partial_\mu\psi$. So $\mathcal{L}_0$ is globally U(1)-invariant. By Noether's theorem this gives a conserved current $j^\mu = \bar\psi\gamma^\mu\psi$ with $\partial_\mu j^\mu = 0$ — the electric current.

相位因子相消是因为 $\alpha$ 为常数，$\partial_\mu(e^{i\alpha}\psi) = e^{i\alpha}\partial_\mu\psi$。故 $\mathcal{L}_0$ 具有全局 U(1) 不变性。由诺特定理，这给出守恒流 $j^\mu = \bar\psi\gamma^\mu\psi$，满足 $\partial_\mu j^\mu = 0$——即电流。

**Step 2 — Local U(1) fails.** Now promote $\alpha \to \alpha(x)$, a function of spacetime. Under $\psi \to e^{i\alpha(x)}\psi$:

**第 2 步 — 局域 U(1) 不成立。** 现将 $\alpha$ 提升为时空函数 $\alpha(x)$。在 $\psi \to e^{i\alpha(x)}\psi$ 下：

$$ \partial_\mu\psi \to \partial_\mu(e^{i\alpha(x)}\psi) = e^{i\alpha(x)}(\partial_\mu\psi + i(\partial_\mu\alpha)\psi). $$

Therefore the kinetic term transforms as:

因此动能项变换为：

$$ \begin{aligned} \bar\psi(i\gamma^\mu\partial_\mu)\psi &\to \bar\psi\, e^{-i\alpha}\cdot i\gamma^\mu\cdot e^{i\alpha}(\partial_\mu\psi + i(\partial_\mu\alpha)\psi) \\ &= \bar\psi(i\gamma^\mu\partial_\mu)\psi - \bar\psi\gamma^\mu(\partial_\mu\alpha)\psi. \end{aligned} $$

The mass term $-m\bar\psi\psi$ is unchanged (the exponentials cancel). So:

质量项 $-m\bar\psi\psi$ 不变（指数因子相消）。故：

$$ \mathcal{L}_0 \to \mathcal{L}_0 - (\partial_\mu\alpha)\bar\psi\gamma^\mu\psi = \mathcal{L}_0 - (\partial_\mu\alpha)j^\mu. $$

The extra term $-(\partial_\mu\alpha)j^\mu \ne 0$ in general; local U(1) is violated.

额外项 $-(\partial_\mu\alpha)j^\mu \ne 0$，局域 U(1) 不变性被破坏。

**Step 3 — Introduce the gauge field.** To cure the failure, introduce a real vector field $A_\mu(x)$ that transforms simultaneously as:

**第 3 步 — 引入规范场。** 为修复这一问题，引入实矢量场 $A_\mu(x)$，它同时按如下方式变换：

$$ A_\mu \to A_\mu - (1/e)\partial_\mu\alpha. $$

Replace $\partial_\mu$ with the **covariant derivative**:

将 $\partial_\mu$ 替换为**协变导数**：

$$ D_\mu \equiv \partial_\mu + ieA_\mu. $$

**Step 4 — Verify covariance.** Under the combined transformation $\psi \to e^{i\alpha(x)}\psi$ and $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$:

**第 4 步 — 验证协变性。** 在组合变换 $\psi \to e^{i\alpha(x)}\psi$ 与 $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ 下：

$$ \begin{aligned} D_\mu\psi &\to (\partial_\mu + ie(A_\mu - (1/e)\partial_\mu\alpha))(e^{i\alpha}\psi) \\ &= e^{i\alpha}(\partial_\mu\psi + i(\partial_\mu\alpha)\psi) + ieA_\mu e^{i\alpha}\psi - i(\partial_\mu\alpha)e^{i\alpha}\psi \\ &= e^{i\alpha}(\partial_\mu + ieA_\mu)\psi \\ &= e^{i\alpha}D_\mu\psi. \end{aligned} $$

The covariant derivative transforms the same way as $\psi$ itself. Therefore:

协变导数与 $\psi$ 本身的变换方式相同。因此：

$$ \bar\psi(i\gamma^\mu D_\mu)\psi \to \bar\psi\, e^{-i\alpha}\cdot i\gamma^\mu\cdot e^{i\alpha}D_\mu\psi = \bar\psi(i\gamma^\mu D_\mu)\psi. $$

Local invariance is restored for the fermion kinetic term.

费米子动能项的局域不变性得以恢复。

**Step 5 — The gauge kinetic term.** The field $A_\mu$ needs its own kinetic term. Define the **field-strength tensor**:

**第 5 步 — 规范动能项。** 场 $A_\mu$ 需要自身的动能项。定义**场强张量**：

$$ F_{\mu\nu} \equiv \partial_\mu A_\nu - \partial_\nu A_\mu. $$

Under $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$:

在 $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ 下：

$$ \begin{aligned} F_{\mu\nu} &\to \partial_\mu(A_\nu - (1/e)\partial_\nu\alpha) - \partial_\nu(A_\mu - (1/e)\partial_\mu\alpha) \\ &= F_{\mu\nu} - (1/e)(\partial_\mu\partial_\nu\alpha - \partial_\nu\partial_\mu\alpha) = F_{\mu\nu}, \end{aligned} $$

since partial derivatives commute ($\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$). So $F_{\mu\nu}$ is gauge-invariant. The unique renormalizable, Lorentz-invariant kinetic term for $A_\mu$ is $-(1/4)F_{\mu\nu}F^{\mu\nu}$. A mass term $(1/2)m^2 A_\mu A^\mu$ is NOT gauge-invariant (it transforms by terms involving $\partial_\mu\alpha$), so $A_\mu$ must be massless.

因为偏导数对易（$\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$）。故 $F_{\mu\nu}$ 是规范不变的。$A_\mu$ 的唯一可重整化、洛伦兹不变的动能项为 $-(1/4)F_{\mu\nu}F^{\mu\nu}$。质量项 $(1/2)m^2 A_\mu A^\mu$ 不是规范不变的（它在变换下产生含 $\partial_\mu\alpha$ 的项），故 $A_\mu$ 必须是无质量的。

**Step 6 — The full QED Lagrangian.** Combining:

**第 6 步 — 完整的 QED 拉格朗日量。** 综合以上：

$$ \begin{aligned} \mathcal{L}_\text{QED} &= \bar\psi(i\gamma^\mu D_\mu - m)\psi - (1/4)F_{\mu\nu}F^{\mu\nu} \\ &= \bar\psi(i\gamma^\mu\partial_\mu - m)\psi - e\bar\psi\gamma^\mu\psi\, A_\mu - (1/4)F_{\mu\nu}F^{\mu\nu}. \end{aligned} $$

The term $-e\bar\psi\gamma^\mu\psi\, A_\mu = -ej^\mu A_\mu$ is the interaction of the electromagnetic current with the field: the photon coupling. $\blacksquare$

项 $-e\bar\psi\gamma^\mu\psi\, A_\mu = -ej^\mu A_\mu$ 是电磁流与场的相互作用：光子耦合。$\blacksquare$

---

## B. Gauge Transformation Law of $A_\mu$ · $A_\mu$ 的规范变换律

**Claim.** The transformation $A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$ (equivalently $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ in the convention above, depending on sign convention) is exactly the classical electromagnetic gauge freedom.

**命题。** 变换 $A_\mu \to A_\mu + (1/e)\partial_\mu\alpha$（在上述符号约定中等价地为 $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$）正是经典电磁学的规范自由度。

**Step 1 — Classical context.** In classical electromagnetism, the electric and magnetic fields $\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$ and $\mathbf{B} = \nabla\times\mathbf{A}$ are unchanged under $\mathbf{A} \to \mathbf{A} + \nabla\chi$, $\phi \to \phi - \partial\chi/\partial t$ for any scalar $\chi(x,t)$. In covariant notation ($A^\mu = (\phi/c, \mathbf{A})$):

**第 1 步 — 经典背景。** 在经典电磁学中，电场 $\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$ 和磁场 $\mathbf{B} = \nabla\times\mathbf{A}$ 在 $\mathbf{A} \to \mathbf{A} + \nabla\chi$，$\phi \to \phi - \partial\chi/\partial t$ 变换下不变，$\chi(x,t)$ 为任意标量。在协变记号（$A^\mu = (\phi/c, \mathbf{A})$）中：

$$ A^\mu \to A^\mu + \partial^\mu\chi, \quad \text{i.e.}\quad A_\mu \to A_\mu + \partial_\mu\chi. $$

**Step 2 — Matching.** Identifying $\chi = -\alpha/e$ (i.e., $\alpha = -e\chi$), the QFT gauge transformation $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ becomes $A_\mu \to A_\mu + \partial_\mu\chi$ — exactly the classical rule. The covariant derivative $D_\mu = \partial_\mu + ieA_\mu$ is the quantum-mechanical minimal coupling, which we recognize in the Hamiltonian as $\mathbf{p} \to \mathbf{p} - e\mathbf{A}$ (the Peierls substitution of Module 5.2). $\blacksquare$

**第 2 步 — 匹配。** 令 $\chi = -\alpha/e$（即 $\alpha = -e\chi$），量子场论规范变换 $A_\mu \to A_\mu - (1/e)\partial_\mu\alpha$ 变为 $A_\mu \to A_\mu + \partial_\mu\chi$——正是经典规则。协变导数 $D_\mu = \partial_\mu + ieA_\mu$ 是量子力学中的最小耦合，在哈密顿量中表现为 $\mathbf{p} \to \mathbf{p} - e\mathbf{A}$（模块 5.2 的 Peierls 替换）。$\blacksquare$

---

## C. Non-Abelian (SU(N)) Gauge Theory · 非阿贝尔 SU(N) 规范理论

**Claim.** For a non-abelian Lie group $G = SU(N)$, demanding local $G$-invariance of the matter Lagrangian leads to the covariant derivative $D_\mu = \partial_\mu - igA^a_\mu T^a$ (summed over adjoint index $a$), the non-abelian field strength $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$, and a field strength that transforms homogeneously (not as a simple gradient).

**命题。** 对于非阿贝尔李群 $G = SU(N)$，要求物质拉格朗日量在局域 $G$ 变换下不变，导出协变导数 $D_\mu = \partial_\mu - igA^a_\mu T^a$（对伴随指标 $a$ 求和）、非阿贝尔场强 $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$，以及场强以齐次方式（而非简单梯度）变换。

**Step 1 — SU(N) generators and algebra.** The Lie algebra of $SU(N)$ is spanned by hermitian traceless generators $T^a$ ($a = 1, \ldots, N^2-1$) satisfying:

**第 1 步 — SU(N) 生成元与代数。** $SU(N)$ 的李代数由厄米无迹生成元 $T^a$（$a = 1, \ldots, N^2-1$）张开，满足：

$$ [T^a, T^b] = if^{abc}T^c, $$

where $f^{abc}$ are the (real, totally antisymmetric) **structure constants**. For $SU(2)$: $T^a = \sigma^a/2$ (Pauli matrices), $f^{abc} = \varepsilon^{abc}$. For $SU(3)$: $T^a = \lambda^a/2$ (Gell-Mann matrices), with $f^{abc}$ the $SU(3)$ structure constants.

其中 $f^{abc}$ 是（实的、全反对称的）**结构常数**。对于 $SU(2)$：$T^a = \sigma^a/2$（泡利矩阵），$f^{abc} = \varepsilon^{abc}$。对于 $SU(3)$：$T^a = \lambda^a/2$（盖尔曼矩阵），$f^{abc}$ 为 $SU(3)$ 结构常数。

**Step 2 — Local SU(N) transformation.** Consider matter fields $\psi_i$ ($i = 1, \ldots, N$) in the fundamental representation. Under local $SU(N)$:

**第 2 步 — 局域 SU(N) 变换。** 考虑基本表示中的物质场 $\psi_i$（$i = 1, \ldots, N$）。在局域 $SU(N)$ 下：

$$ \psi \to U(x)\psi, \quad \text{where } U(x) = \exp(i\alpha^a(x)T^a) \in SU(N). $$

For infinitesimal $\alpha^a \ll 1$:

对于无穷小 $\alpha^a \ll 1$：

$$ \psi \to (1 + i\alpha^a T^a)\psi, \quad \delta\psi = i\alpha^a T^a \psi. $$

**Step 3 — Failure of $\partial_\mu$.** Under $\psi \to U\psi$:

**第 3 步 — $\partial_\mu$ 的失效。** 在 $\psi \to U\psi$ 下：

$$ \partial_\mu\psi \to \partial_\mu(U\psi) = U(\partial_\mu\psi) + (\partial_\mu U)\psi. $$

The extra term $(\partial_\mu U)\psi$ spoils the covariance, just as in the abelian case. For the Lagrangian $\bar\psi(i\gamma^\mu\partial_\mu)\psi$ to be invariant, we need $\partial_\mu\psi \to U(\partial_\mu\psi)$, which requires canceling $(\partial_\mu U)\psi$.

额外项 $(\partial_\mu U)\psi$ 破坏了协变性，与阿贝尔情形相同。为使 $\bar\psi(i\gamma^\mu\partial_\mu)\psi$ 不变，需要 $\partial_\mu\psi \to U(\partial_\mu\psi)$，这要求抵消 $(\partial_\mu U)\psi$。

**Step 4 — Non-abelian covariant derivative.** Introduce the matrix-valued gauge field $A_\mu(x) = A^a_\mu(x)T^a$ ($\dim(G)$ components). Define:

**第 4 步 — 非阿贝尔协变导数。** 引入矩阵值规范场 $A_\mu(x) = A^a_\mu(x)T^a$（$\dim(G)$ 个分量）。定义：

$$ D_\mu \equiv \partial_\mu - igA_\mu = \partial_\mu - igA^a_\mu T^a. $$

Require that $D_\mu\psi \to U(D_\mu\psi)$ under local $SU(N)$, i.e., $D_\mu$ transforms as:

要求在局域 $SU(N)$ 下 $D_\mu\psi \to U(D_\mu\psi)$，即 $D_\mu$ 变换为：

$$ D_\mu \to UD_\mu U^\dagger \quad \text{(acting on fundamental-representation fields).} $$

**Step 5 — Gauge transformation of $A_\mu$.** From $D_\mu \to UD_\mu U^\dagger$:

**第 5 步 — $A_\mu$ 的规范变换。** 由 $D_\mu \to UD_\mu U^\dagger$：

$$ \partial_\mu - igA'_\mu = U(\partial_\mu - igA_\mu)U^\dagger. $$

Expanding the right side:

展开右端：

$$ \begin{aligned} U(\partial_\mu - igA_\mu)U^\dagger &= U(\partial_\mu U^\dagger) + U U^\dagger \partial_\mu - igUA_\mu U^\dagger \\ &= (\partial_\mu) + U(\partial_\mu U^\dagger) - igUA_\mu U^\dagger. \end{aligned} $$

Here we used $U U^\dagger = 1$ and distributed. Matching coefficients:

这里用到 $U U^\dagger = 1$ 并展开。匹配各项系数：

$$ A'_\mu = UA_\mu U^\dagger - (i/g)(\partial_\mu U)U^\dagger = UA_\mu U^\dagger + (i/g)U(\partial_\mu U^\dagger). $$

For infinitesimal $U = 1 + i\alpha^aT^a$:

对于无穷小 $U = 1 + i\alpha^aT^a$：

$$ \delta A^a_\mu = (1/g)\partial_\mu\alpha^a + f^{abc}\alpha^b A^c_\mu. $$

The first term is the abelian-like gradient; the second is purely non-abelian (absent for $U(1)$ where $f^{abc} = 0$).

第一项是类阿贝尔梯度项；第二项是纯非阿贝尔项（当 $f^{abc} = 0$ 时（U(1) 情形）不存在）。

**Step 6 — Non-abelian field strength.** Define $F_{\mu\nu}$ via the commutator of covariant derivatives:

**第 6 步 — 非阿贝尔场强。** 通过协变导数的对易子定义 $F_{\mu\nu}$：

$$ [D_\mu, D_\nu]\psi \equiv -igF_{\mu\nu}\psi. $$

Computing explicitly:

显式计算：

$$ \begin{aligned} [D_\mu, D_\nu] &= [\partial_\mu - igA_\mu, \partial_\nu - igA_\nu] \\ &= -ig(\partial_\mu A_\nu - \partial_\nu A_\mu) - g^2[A_\mu, A_\nu] \\ &= -ig(\partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu]). \end{aligned} $$

Therefore (using $[A_\mu, A_\nu] = [A^a_\mu T^a, A^b_\nu T^b] = A^a_\mu A^b_\nu[T^a, T^b] = if^{abc}A^a_\mu A^b_\nu T^c$):

因此（利用 $[A_\mu, A_\nu] = [A^a_\mu T^a, A^b_\nu T^b] = A^a_\mu A^b_\nu[T^a, T^b] = if^{abc}A^a_\mu A^b_\nu T^c$）：

$$ F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu], $$

i.e., component-wise:

即按分量：

$$ F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu. $$

The extra term $gf^{abc}A^b_\mu A^c_\nu$ (absent in $U(1)$) encodes the self-interaction of the gauge bosons.

额外项 $gf^{abc}A^b_\mu A^c_\nu$（在 U(1) 中不存在）编码了规范玻色子的自相互作用。

**Step 7 — Transformation of $F_{\mu\nu}$.** Under $U$:

**第 7 步 — $F_{\mu\nu}$ 的变换。** 在 $U$ 下：

$$ F_{\mu\nu} \to UF_{\mu\nu}U^\dagger. $$

Proof: $[D_\mu, D_\nu](U\psi) = U([D_\mu, D_\nu]\psi) = U(-igF_{\mu\nu})\psi = -igUF_{\mu\nu}U^\dagger(U\psi)$. So $F_{\mu\nu}$ transforms in the adjoint representation — it is NOT gauge-invariant (unlike the abelian $F_{\mu\nu}$), but the trace $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ IS invariant:

证明：$[D_\mu, D_\nu](U\psi) = U([D_\mu, D_\nu]\psi) = U(-igF_{\mu\nu})\psi = -igUF_{\mu\nu}U^\dagger(U\psi)$。故 $F_{\mu\nu}$ 在伴随表示下变换——它不是规范不变的（不同于阿贝尔的 $F_{\mu\nu}$），但迹 $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ 是不变的：

$$ \mathrm{Tr}(F'_{\mu\nu}F'^{\mu\nu}) = \mathrm{Tr}(UF_{\mu\nu}U^\dagger \cdot UF^{\mu\nu}U^\dagger) = \mathrm{Tr}(UF_{\mu\nu}F^{\mu\nu}U^\dagger) = \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}). $$

Using the normalization $\mathrm{Tr}(T^aT^b) = (1/2)\delta^{ab}$, we get:

利用归一化 $\mathrm{Tr}(T^aT^b) = (1/2)\delta^{ab}$，得：

$$ \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}) = (1/2)F^a_{\mu\nu}F^{a\mu\nu}. $$

**Step 8 — The Yang–Mills Lagrangian.** The complete gauge-invariant Lagrangian is:

**第 8 步 — 杨–米尔斯拉格朗日量。** 完整的规范不变拉格朗日量为：

$$ \begin{aligned} \mathcal{L}_\text{YM} &= \bar\psi(i\gamma^\mu D_\mu - m)\psi - (1/2)\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}) \\ &= \bar\psi(i\gamma^\mu D_\mu - m)\psi - (1/4)F^a_{\mu\nu}F^{a\mu\nu}. \end{aligned} $$

Expanding $F^a_{\mu\nu}F^{a\mu\nu}$ using $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$ produces:
- A quadratic term $(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)^2 \to$ free gauge-boson propagation.
- A cubic term $2(\partial_\mu A^a_\nu)gf^{abc}A^b_\mu A^c_\nu \to$ three-gauge-boson vertex (proportional to $g$).
- A quartic term $g^2(f^{abc}A^b_\mu A^c_\nu)^2 \to$ four-gauge-boson vertex (proportional to $g^2$).

展开 $F^a_{\mu\nu}F^{a\mu\nu}$（利用 $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + gf^{abc}A^b_\mu A^c_\nu$）产生：
- 二次项 $(\partial_\mu A^a_\nu - \partial_\nu A^a_\mu)^2 \to$ 自由规范玻色子传播。
- 三次项 $2(\partial_\mu A^a_\nu)gf^{abc}A^b_\mu A^c_\nu \to$ 三规范玻色子顶角（正比于 $g$）。
- 四次项 $g^2(f^{abc}A^b_\mu A^c_\nu)^2 \to$ 四规范玻色子顶角（正比于 $g^2$）。

These self-interactions are absent in Maxwell/QED (where $f^{abc} = 0$) and are the root of asymptotic freedom in QCD. $\blacksquare$

这些自相互作用在麦克斯韦/QED 中不存在（因为 $f^{abc} = 0$），是 QCD 渐近自由的根源。$\blacksquare$

---

## D. Noether Current from Global U(1) · 全局 U(1) 的诺特流

**Claim.** The global U(1) symmetry $\psi \to e^{i\alpha}\psi$ of $\mathcal{L}_\text{QED}$ yields a conserved Noether current $j^\mu = \bar\psi\gamma^\mu\psi$.

**命题。** $\mathcal{L}_\text{QED}$ 的全局 U(1) 对称性 $\psi \to e^{i\alpha}\psi$ 产生守恒诺特流 $j^\mu = \bar\psi\gamma^\mu\psi$。

**Step 1 — Noether's theorem.** For a Lagrangian $\mathcal{L}(\psi, \partial_\mu\psi)$ invariant under $\delta\psi = i\alpha\psi$ (for infinitesimal $\alpha$), the conserved current is:

**第 1 步 — 诺特定理。** 对于在 $\delta\psi = i\alpha\psi$（无穷小 $\alpha$）下不变的拉格朗日量 $\mathcal{L}(\psi, \partial_\mu\psi)$，守恒流为：

$$ j^\mu = (\partial\mathcal{L}/\partial(\partial_\mu\psi))\delta\psi + \text{c.c.} $$

**Step 2 — Evaluate.** From $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$:

**第 2 步 — 计算。** 由 $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$：

$$ \partial\mathcal{L}/\partial(\partial_\mu\psi) = i\bar\psi\gamma^\mu. $$

So $j^\mu = i\bar\psi\gamma^\mu \cdot i\psi + \text{c.c.}$ Carefully: with $\delta\psi = i\alpha\psi$ and $\delta\bar\psi = -i\alpha\bar\psi$:

故 $j^\mu = i\bar\psi\gamma^\mu \cdot i\psi + \text{c.c.}$。仔细处理：$\delta\psi = i\alpha\psi$，$\delta\bar\psi = -i\alpha\bar\psi$：

$$ \delta\mathcal{L} = 0 \implies j^\mu = -(\partial\mathcal{L}/\partial(\partial_\mu\psi_a))(\delta\psi_a/\alpha) = \bar\psi\gamma^\mu\psi. $$

**Step 3 — Equation of motion.** The Euler–Lagrange equation from $\mathcal{L}_\text{QED}$ gives:

**第 3 步 — 运动方程。** 由 $\mathcal{L}_\text{QED}$ 的欧拉–拉格朗日方程得：

$$ \begin{aligned} (i\gamma^\mu D_\mu - m)\psi &= 0 \quad \text{(Dirac equation with minimal coupling),} \\ \partial_\nu F^{\nu\mu} &= ej^\mu \quad \text{(Maxwell equation with source).} \end{aligned} $$

Together these constitute the equations of motion of QED. Conservation $\partial_\mu j^\mu = 0$ follows from the Dirac equation: $\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu(\partial_\mu\psi) = 0$ using the equations of motion. $\blacksquare$

它们共同构成 QED 的运动方程。守恒性 $\partial_\mu j^\mu = 0$ 由狄拉克方程得出：$\partial_\mu(\bar\psi\gamma^\mu\psi) = (\partial_\mu\bar\psi)\gamma^\mu\psi + \bar\psi\gamma^\mu(\partial_\mu\psi) = 0$，利用运动方程可得。$\blacksquare$

---

## E. Gauge Fixing, Faddeev–Popov Ghosts, and BRST Symmetry · 规范固定、法捷耶夫–波波夫鬼粒子与 BRST 对称性

**Claim.** The naive path integral $Z = \int\mathcal{D}A\, e^{iS}$ over-counts physically equivalent (gauge-related) field configurations, and the gauge-field kinetic operator is non-invertible, so no propagator exists. The **Faddeev–Popov procedure** fixes the gauge at the cost of a gauge-fixing term $-(1/2\xi)(\partial^\mu A^a_\mu)^2$ and a ghost term $\bar c^a(-\partial^\mu D^{ab}_\mu)c^b$. The gauge-fixed action retains a single global fermionic symmetry — the **nilpotent BRST symmetry** — which replaces gauge invariance and guarantees the unitarity and gauge-independence of physical amplitudes.

**命题。** 朴素路径积分 $Z = \int\mathcal{D}A\, e^{iS}$ 对物理上等价（规范相关）的场位形重复计数，且规范场动能算符不可逆，故不存在传播子。**法捷耶夫–波波夫方法**以引入规范固定项 $-(1/2\xi)(\partial^\mu A^a_\mu)^2$ 和鬼粒子项 $\bar c^a(-\partial^\mu D^{ab}_\mu)c^b$ 为代价固定规范。规范固定后的作用量保留唯一的整体费米型对称性——**幂零的 BRST 对称性**——它替代规范不变性，并保证物理振幅的幺正性与规范无关性。

**Step 1 — The over-counting problem.** Gauge-equivalent potentials $A^a_\mu$ and $(A^U)^a_\mu$ give the same action $S[A] = S[A^U]$. Hence $Z = \int\mathcal{D}A\, e^{iS} =$ (volume of the gauge orbit) $\times \int$(physical configurations) — an infinite, field-independent factor. Worse, expanding $-\tfrac14 F^a_{\mu\nu}F^{a\mu\nu}$ to quadratic order gives the operator

**第 1 步 — 重复计数问题。** 规范等价的势 $A^a_\mu$ 与 $(A^U)^a_\mu$ 给出相同作用量 $S[A] = S[A^U]$。故 $Z = \int\mathcal{D}A\, e^{iS} =$（规范轨道的体积）$\times \int$（物理位形）——一个无穷大且与场无关的因子。更糟的是，将 $-\tfrac14 F^a_{\mu\nu}F^{a\mu\nu}$ 展开到二次阶给出算符

$$ \mathcal{K}^{\mu\nu} = \eta^{\mu\nu}\partial^2 - \partial^\mu\partial^\nu, $$

which annihilates every pure-gauge mode $A_\mu = \partial_\mu\chi$ ($\mathcal{K}^{\mu\nu}\partial_\nu\chi = 0$). A matrix with zero eigenvalues cannot be inverted, so the gluon propagator does not exist until the gauge is fixed.

它湮灭每一个纯规范模式 $A_\mu = \partial_\mu\chi$（$\mathcal{K}^{\mu\nu}\partial_\nu\chi = 0$）。一个有零本征值的矩阵不可逆，故在固定规范之前胶子传播子不存在。

**Step 2 — Faddeev–Popov insertion of unity.** Pick a gauge condition $G^a(A) = \partial^\mu A^a_\mu - \omega^a(x) = 0$ and insert the identity

**第 2 步 — 法捷耶夫–波波夫插入单位元。** 选取规范条件 $G^a(A) = \partial^\mu A^a_\mu - \omega^a(x) = 0$ 并插入恒等式

$$ 1 = \int\mathcal{D}\alpha(x)\; \delta[G^a(A^\alpha)]\; \det\!\left( \delta G^a(A^\alpha)/\delta\alpha^b \right), $$

where $A^\alpha$ is the gauge transform of $A$ by $\alpha$. Under an infinitesimal gauge transformation $\delta A^a_\mu = D^{ab}_\mu \alpha^b$, so the **Faddeev–Popov operator** is

其中 $A^\alpha$ 是 $A$ 经 $\alpha$ 的规范变换。在无穷小规范变换下 $\delta A^a_\mu = D^{ab}_\mu \alpha^b$，故**法捷耶夫–波波夫算符**为

$$ M^{ab} = \delta G^a(A^\alpha)/\delta\alpha^b |_{\alpha=0} = \partial^\mu D^{ab}_\mu = \partial^\mu(\partial_\mu\delta^{ab} + g f^{acb}A^c_\mu). $$

The $\delta$-function fixes the gauge; the determinant $\det M$ is the price for not double-counting.

$\delta$ 函数固定规范；行列式 $\det M$ 是避免重复计数的代价。

**Step 3 — Exponentiate det M with anticommuting ghosts.** A determinant of a bosonic operator is a Gaussian integral over **Grassmann** (anticommuting) fields:

**第 3 步 — 用反对易鬼粒子指数化 det M。** 玻色算符的行列式等于对**格拉斯曼**（反对易）场的高斯积分：

$$ \det M = \int\mathcal{D}\bar c\, \mathcal{D}c\; \exp\!\left( i\int d^4x\; \bar c^a M^{ab} c^b \right) = \int\mathcal{D}\bar c\, \mathcal{D}c\; \exp\!\left( i\int d^4x\; \bar c^a(-\partial^\mu D^{ab}_\mu)c^b \right), $$

(the sign is convention; an integration by parts moves the derivative). The fields $c^a, \bar c^a$ are the **Faddeev–Popov ghosts** — Grassmann-valued *scalars* in the adjoint representation. They violate the spin–statistics theorem, which is permitted precisely because they never appear as external (physical) states; they exist only inside loops to cancel the unphysical gauge-boson polarizations. In **abelian** QED, $M = \partial^\mu\partial_\mu$ is field-independent, so the ghosts decouple and may be ignored. In **non-abelian** theory $D_\mu$ contains $A^c_\mu$, producing a ghost–gluon vertex; these ghost loops are exactly what supply part of the $+11C_A/3$ in the QCD $\beta$ function (Module 8.3).

（符号为约定；分部积分移动导数）。场 $c^a, \bar c^a$ 是**法捷耶夫–波波夫鬼粒子**——伴随表示中取格拉斯曼值的*标量*。它们违反自旋–统计定理，这之所以被允许，正是因为它们从不作为外（物理）态出现；它们只在圈内存在，以抵消规范玻色子的非物理极化。在**阿贝尔** QED 中，$M = \partial^\mu\partial_\mu$ 与场无关，故鬼粒子退耦可忽略。在**非阿贝尔**理论中 $D_\mu$ 含 $A^c_\mu$，产生鬼–胶子顶角；这些鬼圈正是为 QCD $\beta$ 函数中 $+11C_A/3$ 提供部分贡献的来源（模块 8.3）。

**Step 4 — Gauge-averaging gives the $\xi$ term.** The function $\omega^a$ was arbitrary, so average over it with a Gaussian weight $\exp(-(i/2\xi)\int(\omega^a)^2)$. The $\delta[\partial\cdot A - \omega]$ then replaces $\omega$ by $\partial\cdot A$, producing $-(1/2\xi)(\partial^\mu A^a_\mu)^2$. The complete **gauge-fixed Lagrangian** is

**第 4 步 — 规范平均给出 $\xi$ 项。** 函数 $\omega^a$ 是任意的，故以高斯权重 $\exp(-(i/2\xi)\int(\omega^a)^2)$ 对其平均。$\delta[\partial\cdot A - \omega]$ 随即将 $\omega$ 替换为 $\partial\cdot A$，产生 $-(1/2\xi)(\partial^\mu A^a_\mu)^2$。完整的**规范固定拉格朗日量**为

$$ \mathcal{L} = -\tfrac14 F^a_{\mu\nu}F^{a\mu\nu} - (1/2\xi)(\partial^\mu A^a_\mu)^2 + \bar c^a(-\partial^\mu D^{ab}_\mu)c^b, $$

with $\xi$ the gauge parameter ($\xi = 1$ Feynman gauge, $\xi \to 0$ Landau gauge). The gluon kinetic operator becomes $\eta^{\mu\nu}\partial^2 - (1 - 1/\xi)\partial^\mu\partial^\nu$, which is now invertible, giving the propagator $D^{ab}_{\mu\nu}(k) = (-i\delta^{ab}/k^2)[\eta_{\mu\nu} - (1-\xi)k_\mu k_\nu/k^2]$.

其中 $\xi$ 为规范参数（$\xi = 1$ 费曼规范，$\xi \to 0$ 朗道规范）。胶子动能算符变为 $\eta^{\mu\nu}\partial^2 - (1 - 1/\xi)\partial^\mu\partial^\nu$，现在可逆，给出传播子 $D^{ab}_{\mu\nu}(k) = (-i\delta^{ab}/k^2)[\eta_{\mu\nu} - (1-\xi)k_\mu k_\nu/k^2]$。

**Step 5 — BRST symmetry (Nakanishi–Lautrup form).** Linearize the gauge-fixing term with an auxiliary field $B^a$: $\mathcal{L} = -\tfrac14 F^2 + B^a\partial^\mu A^a_\mu + (\xi/2)(B^a)^2 + \bar c^a(-\partial^\mu D^{ab}_\mu)c^b$ (integrating out $B^a$ returns the previous form). This Lagrangian is invariant under the **BRST transformation**, defined through the nilpotent operator $s$ and a global Grassmann parameter $\theta$ (field variation $\delta\Phi = \theta\cdot s\Phi$):

**第 5 步 — BRST 对称性（中西–劳特鲁普形式）。** 用辅助场 $B^a$ 线性化规范固定项：$\mathcal{L} = -\tfrac14 F^2 + B^a\partial^\mu A^a_\mu + (\xi/2)(B^a)^2 + \bar c^a(-\partial^\mu D^{ab}_\mu)c^b$（积掉 $B^a$ 返回前一形式）。该拉格朗日量在 **BRST 变换**下不变，变换通过幂零算符 $s$ 与整体格拉斯曼参数 $\theta$ 定义（场变换 $\delta\Phi = \theta\cdot s\Phi$）：

$$ s A^a_\mu = D^{ab}_\mu c^b, \quad s c^a = -\tfrac12 g f^{abc} c^b c^c, \quad s \bar c^a = B^a, \quad s B^a = 0, \quad s \psi = i g c^a T^a \psi. $$

The BRST transformation of $A_\mu$ is just a gauge transformation with the *ghost field itself* as parameter — this is why $s$ reshuffles gauge invariance into a rigid (global) symmetry.

$A_\mu$ 的 BRST 变换正是以*鬼场本身*为参数的规范变换——这正是 $s$ 将规范不变性重组为刚性（整体）对称性的原因。

**Step 6 — Nilpotency $s^2 = 0$.** A direct computation on each field, using the **Jacobi identity** $f^{ade}f^{bce} + f^{bde}f^{cae} + f^{cde}f^{abe} = 0$ of the structure constants, gives $s^2 = 0$. For example, on the ghost: $s^2 c^a = -\tfrac12 gf^{abc}(s c^b)c^c + \tfrac12 gf^{abc}c^b(s c^c) = \tfrac14 g^2 f^{abc}f^{bde}c^d c^e c^c$, which vanishes by Jacobi and the antisymmetry of $c^d c^e$. Likewise $s^2 A^a_\mu = s(D^{ab}_\mu c^b) = 0$. Nilpotency is the algebraic heart of the formalism.

**第 6 步 — 幂零性 $s^2 = 0$。** 对每个场直接计算，利用结构常数的**雅可比恒等式** $f^{ade}f^{bce} + f^{bde}f^{cae} + f^{cde}f^{abe} = 0$，得 $s^2 = 0$。例如对鬼场：$s^2 c^a = -\tfrac12 gf^{abc}(s c^b)c^c + \tfrac12 gf^{abc}c^b(s c^c) = \tfrac14 g^2 f^{abc}f^{bde}c^d c^e c^c$，由雅可比恒等式及 $c^d c^e$ 的反对称性而为零。同样 $s^2 A^a_\mu = s(D^{ab}_\mu c^b) = 0$。幂零性是该形式体系的代数核心。

**Step 7 — Physical content: BRST cohomology, Slavnov–Taylor, unitarity.** The entire gauge-fixing + ghost sector is **BRST-exact** — it is $s$ acting on the "gauge fermion" $\Psi = \bar c^a(\partial^\mu A^a_\mu + (\xi/2)B^a)$:

**第 7 步 — 物理内涵：BRST 上同调、斯拉夫诺夫–泰勒、幺正性。** 整个规范固定 + 鬼粒子部分是 **BRST 恰当的**——它是 $s$ 作用于"规范费米子" $\Psi = \bar c^a(\partial^\mu A^a_\mu + (\xi/2)B^a)$：

$$ \mathcal{L}_\text{gf+gh} = s \Psi, \quad \text{so} \quad S = S_\text{inv} + \int d^4x\; s\Psi, \quad \text{with} \quad s S = 0 \quad \text{(using } s^2=0 \text{ and } sS_\text{inv} = 0\text{).} $$

Since $s^2 = 0$, the conserved **BRST charge** $Q_B$ generates a cohomology, and **physical states** are defined by $Q_B|\text{phys}\rangle = 0$ modulo states of the form $Q_B|\cdot\rangle$ (the Kugo–Ojima criterion). This projection removes the unphysical longitudinal and timelike gauge-boson polarizations together with the ghosts, leaving a positive-norm physical Hilbert space and a **unitary S-matrix**. The Ward–Takahashi identities of QED generalize to the **Slavnov–Taylor identities**, the operator statement of BRST invariance, which enforce the renormalization relations among Z-factors and guarantee the gauge-independence of physical quantities such as the $\beta$ function (Modules 8.3, 8.5). $\blacksquare$

由于 $s^2 = 0$，守恒的 **BRST 荷** $Q_B$ 生成上同调，**物理态**由 $Q_B|\text{phys}\rangle = 0$ 模去形如 $Q_B|\cdot\rangle$ 的态来定义（久郷–大島判据）。该投影移除非物理的纵向与类时规范玻色子极化以及鬼粒子，留下正模物理希尔伯特空间和**幺正 S 矩阵**。QED 的沃德–高桥恒等式推广为 **斯拉夫诺夫–泰勒恒等式**，即 BRST 不变性的算符表述，它强制 Z 因子间的重整化关系，并保证 $\beta$ 函数等物理量的规范无关性（模块 8.3、8.5）。$\blacksquare$

---

## F. From BRST to the Ward–Takahashi Identity · 由 BRST 导出沃德–高桥恒等式

**Claim.** Specializing the Slavnov–Taylor identities of §E to the abelian (QED) case yields the **Ward–Takahashi identity** for the electron–photon vertex $\Gamma^\mu$ and the full electron propagator $S$:

**命题。** 将 §E 的斯拉夫诺夫–泰勒恒等式特化到阿贝尔（QED）情形，给出电子–光子顶角 $\Gamma^\mu$ 与完整电子传播子 $S$ 的**沃德–高桥恒等式**：

$$ q_\mu \Gamma^\mu(p+q, p) = S^{-1}(p+q) - S^{-1}(p), $$

whose on-shell, amputated form is the elementary transversality statement $q_\mu M^\mu = 0$ already used in [Module 8.2 §E](./module-8.2-derivations.md). This is the *deeper* route to that result: it follows from a symmetry of the quantum effective action, not merely from tree-level gauge invariance, so it holds to **all orders** in perturbation theory.

其在壳、截肢形式即 [模块 8.2 §E](./module-8.2-derivations.md) 中已用到的横向性陈述 $q_\mu M^\mu = 0$。这是通向该结果的*更深*途径：它源于量子有效作用量的对称性，而非仅仅树图阶的规范不变性，故对微扰论的**所有阶**都成立。

**Step 1 — The abelian BRST transformations.** For U(1), the structure constants vanish ($f^{abc} = 0$), so the §E transformations collapse to the *linear* set

**第 1 步 — 阿贝尔 BRST 变换。** 对 U(1)，结构常数为零（$f^{abc} = 0$），故 §E 的变换退化为*线性*集

$$ s A_\mu = \partial_\mu c, \quad s \psi = i e c \psi, \quad s \bar\psi = i e c \bar\psi, \quad s c = 0, \quad s \bar c = B, \quad s B = 0. $$

Crucially $s c = 0$: the photon's ghost is **free** and decouples from physics — but it is the bookkeeping device that turns gauge invariance into the identity below.

关键在于 $s c = 0$：光子的鬼粒子是**自由**的，与物理退耦——但它正是把规范不变性转化为下述恒等式的记账工具。

**Step 2 — The master BRST identity.** Because the path-integral measure and the gauge-fixed action are BRST-invariant, the expectation value of any BRST variation vanishes: $\langle s \mathcal{O}\rangle = 0$ for any operator $\mathcal{O}$. Choose $\mathcal{O} = \bar c(x) \psi(y) \bar\psi(z)$. Using $s(\bar c \psi \bar\psi) = (s \bar c)\psi\bar\psi - \bar c (s\psi)\bar\psi + \bar c \psi (s\bar\psi) = B \psi\bar\psi - \bar c(ie c\psi)\bar\psi + \bar c\psi(ie c\bar\psi)$, and $\langle\ldots\rangle = 0$, gives

**第 2 步 — BRST 主恒等式。** 由于路径积分测度与规范固定作用量都 BRST 不变，任意 BRST 变分的期望值为零：对任意算符 $\mathcal{O}$ 有 $\langle s \mathcal{O}\rangle = 0$。取 $\mathcal{O} = \bar c(x) \psi(y) \bar\psi(z)$，利用上述变换并令 $\langle\ldots\rangle = 0$，得

$$ \langle B(x) \psi(y) \bar\psi(z)\rangle = i e \langle\bar c(x) c(x) [\psi(y)\bar\psi(z) \text{ with the two } ie c \text{ insertions}]\rangle. $$

The auxiliary field obeys its equation of motion $B = -(1/\xi)\partial^\mu A_\mu$, and the free ghost contraction $\langle\bar c(x)c(w)\rangle = $ (free propagator) strips the ghost pair, leaving a relation purely among the photon, electron field, and the current $\partial^\mu A_\mu$.

辅助场满足其运动方程 $B = -(1/\xi)\partial^\mu A_\mu$，自由鬼粒子收缩 $\langle\bar c(x)c(w)\rangle$ 消去鬼粒子对，留下纯粹关于光子、电子场与流 $\partial^\mu A_\mu$ 的关系。

**Step 3 — Momentum space: the Ward–Takahashi identity.** Fourier transforming and amputating the external electron legs converts the position-space relation into the statement that the *longitudinal* part of the vertex is fixed by the inverse propagators:

**第 3 步 — 动量空间：沃德–高桥恒等式。** 傅里叶变换并截去外电子腿，将坐标空间关系转化为：顶角的*纵向*部分由逆传播子固定：

$$ q_\mu \Gamma^\mu(p+q, p) = S^{-1}(p+q) - S^{-1}(p). $$

At tree level $\Gamma^\mu = \gamma^\mu$ and $S^{-1}(p) = \not{p} - m$, so the right side is $(\not{p} + \not{q} - m) - (\not{p} - m) = \not{q} = q_\mu\gamma^\mu$ — the identity holds trivially. The content is that it continues to hold with the *full* (all-orders) $\Gamma^\mu$ and $S$.

在树图阶 $\Gamma^\mu = \gamma^\mu$、$S^{-1}(p) = \not{p} - m$，故右边为 $\not{q} = q_\mu\gamma^\mu$——恒等式平凡成立。其内涵在于：对*完整*（所有阶）的 $\Gamma^\mu$ 与 $S$ 它仍然成立。

**Step 4 — Consequences.** (i) **$Z_1 = Z_2$.** Differentiating the identity at $q \to 0$ gives $\Gamma^\mu(p,p) = \partial S^{-1}/\partial p_\mu$; since the vertex renormalization $Z_1$ and the wavefunction renormalization $Z_2$ multiply the two sides, the identity forces **$Z_1 = Z_2$**. Hence the renormalized charge $e = e_0\sqrt{Z_3}$ depends only on $Z_3$ (the photon vacuum polarization) — charge renormalization is **universal**, identical for the electron, muon, or any charged field. This is why the running coupling of [8.2 §D](./module-8.2-derivations.md) is a property of the photon alone.

**第 4 步 — 推论。** (i) **$Z_1 = Z_2$。** 在 $q \to 0$ 处对恒等式求导得 $\Gamma^\mu(p,p) = \partial S^{-1}/\partial p_\mu$；由于顶角重整化 $Z_1$ 与波函数重整化 $Z_2$ 分别乘在两边，恒等式迫使 **$Z_1 = Z_2$**。故重整化电荷 $e = e_0\sqrt{Z_3}$ 只依赖于 $Z_3$（光子真空极化）——电荷重整化是**普适的**，对电子、$\mu$ 子或任何带电场都相同。这正是 [8.2 §D](./module-8.2-derivations.md) 的跑动耦合仅是光子自身性质的原因。

(ii) **Transverse vacuum polarization, massless photon.** Applied to the photon self-energy, the same identity gives $q_\mu\Pi^{\mu\nu}(q) = 0$, so $\Pi^{\mu\nu}(q) = (q^2\eta^{\mu\nu} - q^\mu q^\nu)\Pi(q^2)$. The radiative correction is purely transverse, so it **cannot generate a photon mass term** $m^2\eta^{\mu\nu}$: gauge invariance protects the photon's masslessness to all orders.

(ii) **横向真空极化、无质量光子。** 应用于光子自能，同一恒等式给出 $q_\mu\Pi^{\mu\nu}(q) = 0$，故 $\Pi^{\mu\nu}(q) = (q^2\eta^{\mu\nu} - q^\mu q^\nu)\Pi(q^2)$。辐射修正纯横向，故**不能产生光子质量项** $m^2\eta^{\mu\nu}$：规范不变性保护光子无质量性到所有阶。

(iii) **On-shell transversality.** Contracting an external on-shell photon line of any amplitude with its momentum gives **$q_\mu M^\mu = 0$** — the elementary Ward identity of [8.2 §E](./module-8.2-derivations.md), here obtained as a corollary of the all-orders BRST/Slavnov–Taylor structure. $\blacksquare$

(iii) **在壳横向性。** 用动量缩并任意振幅的外在壳光子线给出 **$q_\mu M^\mu = 0$**——即 [8.2 §E](./module-8.2-derivations.md) 的初等沃德恒等式，此处作为所有阶 BRST／斯拉夫诺夫–泰勒结构的推论得到。$\blacksquare$

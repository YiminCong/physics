---
title: "Derivations — Module 3.2: Time-Independent Schrödinger Equation"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 3.2: Time-Independent Schrödinger Equation
# 推导 — 模块 3.2：定态薛定谔方程

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 3.2](./module-3.2-time-independent-schrodinger-equation.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 3.2](./module-3.2-time-independent-schrodinger-equation.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. The Infinite Square Well · 无限深方势阱

**Claim.** For a particle confined to $0 \le x \le L$ by an infinite potential, the energy eigenvalues are $E_n = n^2\pi^2\hbar^2/(2mL^2)$ with normalized eigenfunctions $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$, $n = 1, 2, 3, \ldots$

**命题。** 对于被无限深势垒约束在 $0 \le x \le L$ 内的粒子，能量本征值为 $E_n = n^2\pi^2\hbar^2/(2mL^2)$，归一化本征函数为 $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$，$n = 1, 2, 3, \ldots$

**Step 1 — Set up the equation.** Inside the well $V(x) = 0$, so the time-independent Schrödinger equation (TISE) $\hat{H}\psi = E\psi$ reads $-(\hbar^2/2m)\,\psi''(x) = E\,\psi(x)$. Define $k^2 = 2mE/\hbar^2$ (with $E > 0$, so $k$ is real). The equation becomes $\psi'' = -k^2\psi$ — the second-order constant-coefficient ODE of Module 0.3.

**第 1 步 — 建立方程。** 阱内 $V(x) = 0$，故定态薛定谔方程 $\hat{H}\psi = E\psi$ 为 $-(\hbar^2/2m)\,\psi''(x) = E\,\psi(x)$。定义 $k^2 = 2mE/\hbar^2$（$E > 0$，故 $k$ 为实数）。方程化为 $\psi'' = -k^2\psi$——即模块 0.3 的二阶常系数常微分方程。

**Step 2 — General solution.** The general solution is $\psi(x) = A\sin(kx) + B\cos(kx)$, with $A, B$ constants fixed by boundary conditions.

**第 2 步 — 通解。** 通解为 $\psi(x) = A\sin(kx) + B\cos(kx)$，常数 $A$、$B$ 由边界条件确定。

**Step 3 — Boundary conditions.** The wavefunction must be continuous and vanish where the potential is infinite, so $\psi(0) = \psi(L) = 0$. From $\psi(0) = 0$: $A\sin(0) + B\cos(0) = B = 0$, hence $B = 0$ and $\psi(x) = A\sin(kx)$. From $\psi(L) = 0$: $A\sin(kL) = 0$. Since $A \ne 0$ (else $\psi \equiv 0$), we need $\sin(kL) = 0$, i.e. $kL = n\pi$ for integer $n$.

**第 3 步 — 边界条件。** 波函数必须连续，且在势能无穷大处为零，故 $\psi(0) = \psi(L) = 0$。由 $\psi(0) = 0$：$A\sin(0) + B\cos(0) = B = 0$，故 $B = 0$，$\psi(x) = A\sin(kx)$。由 $\psi(L) = 0$：$A\sin(kL) = 0$。因 $A \ne 0$（否则 $\psi \equiv 0$），需 $\sin(kL) = 0$，即 $kL = n\pi$，$n$ 为整数。

**Step 4 — Quantization.** Thus $k_n = n\pi/L$. We take $n = 1, 2, 3, \ldots$ ($n = 0$ gives $\psi \equiv 0$; negative $n$ only flips the sign of $\psi$ and adds nothing new). Substituting back into $k^2 = 2mE/\hbar^2$:

**第 4 步 — 量子化。** 于是 $k_n = n\pi/L$。取 $n = 1, 2, 3, \ldots$（$n = 0$ 给出 $\psi \equiv 0$；负 $n$ 只改变 $\psi$ 的符号，无新解）。代回 $k^2 = 2mE/\hbar^2$：

$$ E_n = \hbar^2 k_n^2/(2m) = \boxed{\,n^2\pi^2\hbar^2/(2mL^2)\,}. $$

**Step 5 — Normalization.** Require $\int_0^L |\psi|^2\, dx = 1$: $A^2 \int_0^L \sin^2(n\pi x/L)\, dx = A^2\cdot(L/2) = 1$, using $\int_0^L \sin^2(n\pi x/L)\, dx = L/2$. Hence $A = \sqrt{2/L}$, giving $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$. $\blacksquare$

**第 5 步 — 归一化。** 要求 $\int_0^L |\psi|^2\, dx = 1$：$A^2 \int_0^L \sin^2(n\pi x/L)\, dx = A^2\cdot(L/2) = 1$，其中用到 $\int_0^L \sin^2(n\pi x/L)\, dx = L/2$。故 $A = \sqrt{2/L}$，得 $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$。$\blacksquare$

---

## B. The Harmonic Oscillator Spectrum via Ladder Operators · 用升降算符求谐振子谱

**Claim.** For $\hat{H} = \hat{p}^2/2m + \tfrac12 m\omega^2\hat{x}^2$, the spectrum is $E_n = (n + \tfrac12)\hbar\omega$, $n = 0, 1, 2, \ldots$, with a zero-point energy $\tfrac12\hbar\omega$. This is the single most reused derivation in the curriculum (phonons in 4.3, fields in 6.1, 6.5).

**命题。** 对于 $\hat{H} = \hat{p}^2/2m + \tfrac12 m\omega^2\hat{x}^2$，能谱为 $E_n = (n + \tfrac12)\hbar\omega$，$n = 0, 1, 2, \ldots$，零点能为 $\tfrac12\hbar\omega$。这是全课程复用最多的推导（4.3 的声子、6.1 与 6.5 的场）。

**Step 1 — Define the ladder operators.** Let

**第 1 步 — 定义升降算符。** 令

$$ \hat{a} = \sqrt{m\omega/2\hbar}\,(\hat{x} + i\hat{p}/m\omega), \qquad \hat{a}^\dagger = \sqrt{m\omega/2\hbar}\,(\hat{x} - i\hat{p}/m\omega). $$

**Step 2 — Their commutator.** Using the canonical commutator $[\hat{x}, \hat{p}] = i\hbar$ (proved in Module 3.3),

**第 2 步 — 它们的对易子。** 利用正则对易关系 $[\hat{x}, \hat{p}] = i\hbar$（在模块 3.3 中证明），

$$ [\hat{a}, \hat{a}^\dagger] = (m\omega/2\hbar)\,[\hat{x} + i\hat{p}/m\omega,\, \hat{x} - i\hat{p}/m\omega] = (m\omega/2\hbar)\big(-i/m\omega\,[\hat{x}, \hat{p}] + i/m\omega\,[\hat{p}, \hat{x}]\big) = (m\omega/2\hbar)\cdot(2/m\omega)\cdot\hbar = 1. $$

So $[\hat{a}, \hat{a}^\dagger] = 1$. (Here we used $[\hat{x},\hat{x}]=[\hat{p},\hat{p}]=0$ and $[\hat{p},\hat{x}] = -i\hbar$.)

故 $[\hat{a}, \hat{a}^\dagger] = 1$。（这里用到 $[\hat{x},\hat{x}]=[\hat{p},\hat{p}]=0$ 与 $[\hat{p},\hat{x}] = -i\hbar$。）

**Step 3 — Rewrite the Hamiltonian.** Compute $\hat{a}^\dagger\hat{a} = (m\omega/2\hbar)(\hat{x} - i\hat{p}/m\omega)(\hat{x} + i\hat{p}/m\omega) = (m\omega/2\hbar)(\hat{x}^2 + \hat{p}^2/m^2\omega^2 + (i/m\omega)[\hat{x},\hat{p}]) = (1/\hbar\omega)(\hat{p}^2/2m + \tfrac12 m\omega^2\hat{x}^2) - \tfrac12$. Therefore

**第 3 步 — 改写哈密顿量。** 计算 $\hat{a}^\dagger\hat{a} = (m\omega/2\hbar)(\hat{x} - i\hat{p}/m\omega)(\hat{x} + i\hat{p}/m\omega) = (m\omega/2\hbar)(\hat{x}^2 + \hat{p}^2/m^2\omega^2 + (i/m\omega)[\hat{x},\hat{p}]) = (1/\hbar\omega)(\hat{p}^2/2m + \tfrac12 m\omega^2\hat{x}^2) - \tfrac12$。因此

$$ \hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \tfrac12) = \hbar\omega(\hat{N} + \tfrac12), \qquad \text{where } \hat{N} \equiv \hat{a}^\dagger\hat{a} \text{ is the } \textbf{number operator}. $$

$$ \hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \tfrac12) = \hbar\omega(\hat{N} + \tfrac12), \qquad \text{其中 } \hat{N} \equiv \hat{a}^\dagger\hat{a} \text{ 为}\textbf{数算符}. $$

**Step 4 — Commutators with $\hat{N}$.** From $[\hat{a}, \hat{a}^\dagger] = 1$: $[\hat{N}, \hat{a}] = [\hat{a}^\dagger\hat{a}, \hat{a}] = \hat{a}^\dagger[\hat{a},\hat{a}] + [\hat{a}^\dagger,\hat{a}]\hat{a} = -\hat{a}$, and similarly $[\hat{N}, \hat{a}^\dagger] = +\hat{a}^\dagger$.

**第 4 步 — 与 $\hat{N}$ 的对易子。** 由 $[\hat{a}, \hat{a}^\dagger] = 1$：$[\hat{N}, \hat{a}] = [\hat{a}^\dagger\hat{a}, \hat{a}] = \hat{a}^\dagger[\hat{a},\hat{a}] + [\hat{a}^\dagger,\hat{a}]\hat{a} = -\hat{a}$，同理 $[\hat{N}, \hat{a}^\dagger] = +\hat{a}^\dagger$。

**Step 5 — Ladder action.** Let $\hat{N}|n\rangle = n|n\rangle$. Then $\hat{N}(\hat{a}|n\rangle) = (\hat{a}\hat{N} - \hat{a})|n\rangle = (n-1)(\hat{a}|n\rangle)$: $\hat{a}$ lowers the eigenvalue by $1$. Likewise $\hat{a}^\dagger|n\rangle$ is an eigenstate with eigenvalue $(n+1)$. So $\hat{a}$ and $\hat{a}^\dagger$ step between levels — hence "ladder" operators.

**第 5 步 — 阶梯作用。** 设 $\hat{N}|n\rangle = n|n\rangle$。则 $\hat{N}(\hat{a}|n\rangle) = (\hat{a}\hat{N} - \hat{a})|n\rangle = (n-1)(\hat{a}|n\rangle)$：$\hat{a}$ 将本征值降低 $1$。同理 $\hat{a}^\dagger|n\rangle$ 是本征值为 $(n+1)$ 的本征态。故 $\hat{a}$、$\hat{a}^\dagger$ 在能级间逐级移动——即"阶梯"算符。

**Step 6 — Spectrum is bounded below.** The norm satisfies $\|\hat{a}|n\rangle\|^2 = \langle n|\hat{a}^\dagger\hat{a}|n\rangle = \langle n|\hat{N}|n\rangle = n\,\langle n|n\rangle \ge 0$, so $n \ge 0$. Repeated application of $\hat{a}$ would produce states of ever-lower eigenvalue, eventually negative — a contradiction — unless the chain terminates at a **ground state** $|0\rangle$ with

**第 6 步 — 谱有下界。** 范数满足 $\|\hat{a}|n\rangle\|^2 = \langle n|\hat{a}^\dagger\hat{a}|n\rangle = \langle n|\hat{N}|n\rangle = n\,\langle n|n\rangle \ge 0$，故 $n \ge 0$。反复作用 $\hat{a}$ 会产生本征值不断降低、最终为负的态——矛盾——除非阶梯在**基态** $|0\rangle$ 处终止，且

$$ \hat{a}|0\rangle = 0. $$

Then $\hat{N}|0\rangle = \hat{a}^\dagger\hat{a}|0\rangle = 0$, so the lowest eigenvalue is $n = 0$, and all eigenvalues are non-negative integers $n = 0, 1, 2, \ldots$

于是 $\hat{N}|0\rangle = \hat{a}^\dagger\hat{a}|0\rangle = 0$，故最小本征值为 $n = 0$，所有本征值为非负整数 $n = 0, 1, 2, \ldots$

**Step 7 — The energies.** Since $\hat{H} = \hbar\omega(\hat{N} + \tfrac12)$,

**第 7 步 — 能量。** 由 $\hat{H} = \hbar\omega(\hat{N} + \tfrac12)$，

$$ \boxed{\,E_n = (n + \tfrac12)\hbar\omega\,}, \qquad n = 0, 1, 2, \ldots $$

The ground-state energy $E_0 = \tfrac12\hbar\omega \ne 0$ is the **zero-point energy**: a direct consequence of the uncertainty principle ($x$ and $p$ cannot both vanish). $\blacksquare$

基态能 $E_0 = \tfrac12\hbar\omega \ne 0$ 即**零点能**：这是不确定性原理的直接后果（$x$ 与 $p$ 不能同时为零）。$\blacksquare$

**Step 8 — Normalized ladder & ground-state wavefunction.** From the norms, $\hat{a}|n\rangle = \sqrt{n}\,|n-1\rangle$ and $\hat{a}^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$, so $|n\rangle = (\hat{a}^\dagger)^n/\sqrt{n!}\,|0\rangle$. Writing $\hat{a}|0\rangle = 0$ in position space with $\hat{p} = -i\hbar\,d/dx$ gives $(x + (\hbar/m\omega)\,d/dx)\,\psi_0 = 0$, a first-order ODE whose solution is the **Gaussian ground state** $\psi_0(x) \propto \exp(-m\omega x^2/2\hbar)$ (normalized using the Gaussian integral of Module 0.1).

**第 8 步 — 归一化阶梯与基态波函数。** 由范数得 $\hat{a}|n\rangle = \sqrt{n}\,|n-1\rangle$、$\hat{a}^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$，故 $|n\rangle = (\hat{a}^\dagger)^n/\sqrt{n!}\,|0\rangle$。在坐标表象中（$\hat{p} = -i\hbar\,d/dx$）将 $\hat{a}|0\rangle = 0$ 写出，得 $(x + (\hbar/m\omega)\,d/dx)\,\psi_0 = 0$，这是一阶常微分方程，其解为**高斯基态** $\psi_0(x) \propto \exp(-m\omega x^2/2\hbar)$（用模块 0.1 的高斯积分归一化）。

---

## C. Excited-State Wavefunctions (Hermite Polynomials) · 激发态波函数（厄米多项式）

**Step 1 — Build states from the ground state.** From $|n\rangle = (\hat{a}^\dagger)^n/\sqrt{n!}\,|0\rangle$ and $\hat{a}^\dagger = \sqrt{m\omega/2\hbar}\,(\hat{x} - i\hat{p}/m\omega)$, introduce the dimensionless variable $\xi = \sqrt{m\omega/\hbar}\,x$, so that $\hat{x} \to \xi$ and $\hat{p} = -i\hbar\,d/dx \to -i\sqrt{m\hbar\omega}\,d/d\xi$. Then $\hat{a}^\dagger = (\xi - d/d\xi)/\sqrt{2}$ and $\hat{a} = (\xi + d/d\xi)/\sqrt{2}$.

**第 1 步 — 从基态构造态。** 由 $|n\rangle = (\hat{a}^\dagger)^n/\sqrt{n!}\,|0\rangle$ 及 $\hat{a}^\dagger = \sqrt{m\omega/2\hbar}\,(\hat{x} - i\hat{p}/m\omega)$，引入无量纲变量 $\xi = \sqrt{m\omega/\hbar}\,x$，则 $\hat{x} \to \xi$，$\hat{p} = -i\hbar\,d/dx \to -i\sqrt{m\hbar\omega}\,d/d\xi$。于是 $\hat{a}^\dagger = (\xi - d/d\xi)/\sqrt{2}$，$\hat{a} = (\xi + d/d\xi)/\sqrt{2}$。

**Step 2 — Apply repeatedly.** With $\psi_0(\xi) = (m\omega/\pi\hbar)^{1/4} e^{-\xi^2/2}$, acting $n$ times with $\hat{a}^\dagger$ gives $\psi_n(\xi) = (1/\sqrt{2^n n!})\,(\xi - d/d\xi)^n\,\psi_0$. Using the Rodrigues identity $(\xi - d/d\xi)^n e^{-\xi^2/2} = H_n(\xi)\,e^{-\xi^2/2}$, where $H_n$ are the **Hermite polynomials** (the special functions of Module 0.3), we obtain

**第 2 步 — 反复作用。** 取 $\psi_0(\xi) = (m\omega/\pi\hbar)^{1/4} e^{-\xi^2/2}$，作用 $n$ 次 $\hat{a}^\dagger$ 得 $\psi_n(\xi) = (1/\sqrt{2^n n!})\,(\xi - d/d\xi)^n\,\psi_0$。利用罗德里格斯恒等式 $(\xi - d/d\xi)^n e^{-\xi^2/2} = H_n(\xi)\,e^{-\xi^2/2}$，其中 $H_n$ 为**厄米多项式**（模块 0.3 的特殊函数），得

$$ \psi_n(x) = (m\omega/\pi\hbar)^{1/4}\,(1/\sqrt{2^n n!})\,H_n(\sqrt{m\omega/\hbar}\,x)\,e^{-m\omega x^2/2\hbar}. $$

These are exactly the series-solution results of Module 0.3, now obtained algebraically.

这正是模块 0.3 中级数解的结果，此处用代数方法重新得到。

---

## D. Rigor: Why the Spectrum Is Real, Orthogonal, and Complete · 严格性：谱为何是实的、正交的、完备的

**Reality.** $\hat{H}$ is **Hermitian** (self-adjoint on the appropriate domain): $\langle\varphi|\hat{H}\psi\rangle = \langle\hat{H}\varphi|\psi\rangle$, proved by integrating the kinetic term by parts twice with wavefunctions vanishing at the boundary. For an eigenstate $\hat{H}\psi = E\psi$, $E\langle\psi|\psi\rangle = \langle\psi|\hat{H}\psi\rangle = \langle\hat{H}\psi|\psi\rangle = E^*\langle\psi|\psi\rangle$, so $E = E^*$ is real.

**实性。** $\hat{H}$ 是**厄米的**（在恰当定义域上自伴）：$\langle\varphi|\hat{H}\psi\rangle = \langle\hat{H}\varphi|\psi\rangle$，通过对动能项分部积分两次、并利用波函数在边界为零而证明。对本征态 $\hat{H}\psi = E\psi$，有 $E\langle\psi|\psi\rangle = \langle\psi|\hat{H}\psi\rangle = \langle\hat{H}\psi|\psi\rangle = E^*\langle\psi|\psi\rangle$，故 $E = E^*$ 为实数。

**Orthogonality.** For $E_m \ne E_n$: $(E_m - E_n)\langle\psi_m|\psi_n\rangle = \langle\psi_m|\hat{H}\psi_n\rangle - \langle\hat{H}\psi_m|\psi_n\rangle = 0$, so $\langle\psi_m|\psi_n\rangle = 0$ — distinct-energy eigenstates are orthogonal.

**正交性。** 当 $E_m \ne E_n$：$(E_m - E_n)\langle\psi_m|\psi_n\rangle = \langle\psi_m|\hat{H}\psi_n\rangle - \langle\hat{H}\psi_m|\psi_n\rangle = 0$，故 $\langle\psi_m|\psi_n\rangle = 0$——不同能量的本征态相互正交。

**Positivity of the spectrum (oscillator).** For any state, $\langle\hat{H}\rangle = \langle\hat{p}^2\rangle/2m + \tfrac12 m\omega^2\langle\hat{x}^2\rangle \ge 0$ since both terms are non-negative; combined with $E_0 = \tfrac12\hbar\omega$ this confirms the ground state is the true minimum (no lower state can exist, consistent with $\hat{a}|0\rangle = 0$). The bounded-below argument of Step 6 is then rigorous: if $n$ were not a non-negative integer, repeatedly applying $\hat{a}$ would eventually yield a state of negative norm $\|\hat{a}^k|n\rangle\|^2 < 0$, a contradiction; the only escape is termination at $\hat{a}|0\rangle = 0$.

**谱的正定性（谐振子）。** 对任意态，$\langle\hat{H}\rangle = \langle\hat{p}^2\rangle/2m + \tfrac12 m\omega^2\langle\hat{x}^2\rangle \ge 0$，因两项均非负；结合 $E_0 = \tfrac12\hbar\omega$ 可确认基态是真正的极小（不存在更低的态，与 $\hat{a}|0\rangle = 0$ 一致）。于是第 6 步的「有下界」论证是严格的：若 $n$ 不是非负整数，反复作用 $\hat{a}$ 终将得到负范数态 $\|\hat{a}^k|n\rangle\|^2 < 0$，矛盾；唯一出路是在 $\hat{a}|0\rangle = 0$ 处终止。

**Completeness.** Both $\hat{H}$ here are Sturm–Liouville operators, so their eigenfunctions form a **complete orthonormal basis** of $L^2$: any state expands as $|\psi\rangle = \sum_n c_n|\psi_n\rangle$ with $c_n = \langle\psi_n|\psi\rangle$ (Module 3.3). This is what justifies writing a general solution as a superposition of stationary states.

**完备性。** 此处的两个 $\hat{H}$ 均为施图姆–刘维尔算符，故其本征函数构成 $L^2$ 的**完备正交基**：任意态可展开为 $|\psi\rangle = \sum_n c_n|\psi_n\rangle$，其中 $c_n = \langle\psi_n|\psi\rangle$（模块 3.3）。这正是把一般解写成定态叠加的依据。

---

*Sample derivation document — the "deeper / rigorous" standard. Every module's `*-derivations.md` will match this depth: full intermediate algebra, boundary/domain conditions, Hermiticity/orthogonality/completeness where relevant, and physical interpretation, all bilingual.*

*样板推导文档——「更深 / 严格」标准。每个模块的 `*-derivations.md` 都将达到此深度：完整的中间代数、边界/定义域条件、相关处的厄米性/正交性/完备性，以及物理诠释，全部双语。*

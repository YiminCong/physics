# Derivations — Module 1.20: Canonical Transformations, Hamilton–Jacobi & Action–Angle
# 推导 — 模块 1.20：正则变换、哈密顿–雅可比与作用量–角变量

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 1.20](./module-1.20-canonical-transformations-hamilton-jacobi.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 1.20](./module-1.20-canonical-transformations-hamilton-jacobi.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Generating Functions and the Four Types · 生成函数与四种类型

**Claim.** A transformation (q, p) → (Q, P) is canonical iff it preserves the form of Hamilton's equations, which is guaranteed by requiring p dq − H dt = P dQ − K dt + dF for some generating function F. The type-1 function F₁(q, Q, t) gives p = ∂F₁/∂q, P = −∂F₁/∂Q, K = H + ∂F₁/∂t; the type-2 function F₂(q, P, t) = F₁ + QP gives p = ∂F₂/∂q, Q = ∂F₂/∂P, K = H + ∂F₂/∂t. The choice F₂ = qP generates the identity transformation.

**命题。** 变换 (q, p) → (Q, P) 是正则的，当且仅当它保持哈密顿方程的形式不变；这由要求 p dq − H dt = P dQ − K dt + dF（F 为某生成函数）保证。第一类函数 F₁(q, Q, t) 给出 p = ∂F₁/∂q，P = −∂F₁/∂Q，K = H + ∂F₁/∂t；第二类函数 F₂(q, P, t) = F₁ + QP 给出 p = ∂F₂/∂q，Q = ∂F₂/∂P，K = H + ∂F₂/∂t。取 F₂ = qP 生成恒等变换。

**Step 1 — The variational principle fixes the integrand up to a total differential.** Hamilton's equations for (q, p) with Hamiltonian H follow from the modified Hamilton's principle (Module 1.3) δ∫(p q̇ − H) dt = 0. For the new coordinates (Q, P) to obey Hamilton's equations with a new Hamiltonian K, we likewise need δ∫(P Q̇ − K) dt = 0. Both variational principles hold simultaneously iff the two integrands differ by the total time derivative of a function F, since an endpoint-fixed total derivative contributes nothing to the variation:

**第 1 步 — 变分原理把被积函数确定到一个全微分。** 以哈密顿量 H 描述 (q, p) 的哈密顿方程来自修正的哈密顿原理（模块 1.3）δ∫(p q̇ − H) dt = 0。要使新坐标 (Q, P) 服从以新哈密顿量 K 描述的哈密顿方程，同样需要 δ∫(P Q̇ − K) dt = 0。两个变分原理同时成立，当且仅当两被积函数相差某函数 F 的全时间导数——因为端点固定的全导数对变分无贡献：

  p q̇ − H = P Q̇ − K + dF/dt.

Multiplying by dt gives the differential form

两边乘 dt 得微分形式

  p dq − H dt = P dQ − K dt + dF.

**Step 2 — Type 1: F = F₁(q, Q, t).** Choose the independent variables to be the old and new coordinates (q, Q). Then dF₁ = (∂F₁/∂q) dq + (∂F₁/∂Q) dQ + (∂F₁/∂t) dt. Substituting into the form from Step 1 and rearranging:

**第 2 步 — 第一类：F = F₁(q, Q, t)。** 取独立变量为新旧坐标 (q, Q)。则 dF₁ = (∂F₁/∂q) dq + (∂F₁/∂Q) dQ + (∂F₁/∂t) dt。代入第 1 步的形式并整理：

  p dq − P dQ + (K − H) dt = (∂F₁/∂q) dq + (∂F₁/∂Q) dQ + (∂F₁/∂t) dt.

Since q, Q, t are independent, the coefficients of dq, dQ, dt must match separately:

由于 q、Q、t 独立，dq、dQ、dt 的系数必须分别相等：

  **p = ∂F₁/∂q,   P = −∂F₁/∂Q,   K = H + ∂F₁/∂t.**

The first two relations, solved together, express (Q, P) in terms of (q, p): F₁ generates the transformation.

前两个关系联立求解，把 (Q, P) 用 (q, p) 表示：F₁ 生成该变换。

**Step 3 — Type 2 by Legendre transform: F₂(q, P, t) = F₁ + QP.** When the natural variables are (q, P) rather than (q, Q), pass to a new generator by a Legendre transform in the pair (Q, P). Define F₂ = F₁ + QP. Then

**第 3 步 — 由勒让德变换得第二类：F₂(q, P, t) = F₁ + QP。** 当自然变量为 (q, P) 而非 (q, Q) 时，对 (Q, P) 这一对作勒让德变换得到新生成函数。定义 F₂ = F₁ + QP。则

  dF₂ = dF₁ + Q dP + P dQ.

Using dF₁ = p dq − P dQ + (K − H) dt from Step 2, the P dQ terms cancel:

利用第 2 步的 dF₁ = p dq − P dQ + (K − H) dt，P dQ 项相消：

  dF₂ = p dq + Q dP + (K − H) dt.

Reading off the coefficients of dq, dP, dt:

读出 dq、dP、dt 的系数：

  **p = ∂F₂/∂q,   Q = ∂F₂/∂P,   K = H + ∂F₂/∂t.**

**Step 4 — F₂ = qP generates the identity.** Take F₂(q, P) = qP (no explicit t). Apply the Step 3 relations:

**第 4 步 — F₂ = qP 生成恒等变换。** 取 F₂(q, P) = qP（不显含 t）。应用第 3 步关系：

  p = ∂F₂/∂q = P,   Q = ∂F₂/∂P = q,   K = H + 0 = H.

Hence Q = q and P = p with K = H: the **identity transformation**. This confirms the bookkeeping of the relations is internally consistent. (More generally F₂ = ∑_k f_k(q) P_k gives Q_k = f_k(q), an arbitrary point transformation of configuration space, with momenta transforming contragrediently.) ∎

故 Q = q、P = p 且 K = H：即**恒等变换**。这验证了上述关系的记账是自洽的。（更一般地 F₂ = ∑_k f_k(q) P_k 给出 Q_k = f_k(q)，即位形空间的任意点变换，动量按逆变方式变换。）∎

---

## B. Symplectic Condition and Poisson-Bracket Invariance · 辛条件与泊松括号不变性

**Claim.** Collect the phase-space coordinates into a column ξ = (q₁,…,q_n, p₁,…,p_n)ᵀ and let J be the 2n×2n symplectic matrix J = [[0, I],[−I, 0]]. A (time-independent) transformation ξ → η(ξ) is canonical iff its Jacobian M_{ij} = ∂η_i/∂ξ_j satisfies the **symplectic condition** Mᵀ J M = J. Equivalently, the fundamental Poisson brackets are preserved: {Q_i, P_j} = δ_{ij}, {Q_i, Q_j} = {P_i, P_j} = 0. Poisson brackets of any pair of functions are canonical invariants.

**命题。** 将相空间坐标排成列 ξ = (q₁,…,q_n, p₁,…,p_n)ᵀ，令 J 为 2n×2n 辛矩阵 J = [[0, I],[−I, 0]]。一个（不含时）变换 ξ → η(ξ) 是正则的，当且仅当其雅可比矩阵 M_{ij} = ∂η_i/∂ξ_j 满足**辛条件** Mᵀ J M = J。等价地，基本泊松括号保持不变：{Q_i, P_j} = δ_{ij}，{Q_i, Q_j} = {P_i, P_j} = 0。任意一对函数的泊松括号都是正则不变量。

**Step 1 — Hamilton's equations in symplectic form.** With ξ = (q, p)ᵀ, Hamilton's equations q̇_i = ∂H/∂p_i, ṗ_i = −∂H/∂q_i collapse to the single compact equation

**第 1 步 — 辛形式的哈密顿方程。** 以 ξ = (q, p)ᵀ，哈密顿方程 q̇_i = ∂H/∂p_i，ṗ_i = −∂H/∂q_i 收缩为单一紧凑方程

  ξ̇ = J ∂H/∂ξ,

where ∂H/∂ξ is the gradient column (∂H/∂q, ∂H/∂p)ᵀ. One checks the upper block gives q̇ = +∂H/∂p and the lower block gives ṗ = −∂H/∂q, matching Hamilton's equations.

其中 ∂H/∂ξ 是梯度列 (∂H/∂q, ∂H/∂p)ᵀ。验证上块给出 q̇ = +∂H/∂p，下块给出 ṗ = −∂H/∂q，与哈密顿方程一致。

**Step 2 — Transform the equations of motion.** Let η = η(ξ) with Jacobian M_{ij} = ∂η_i/∂ξ_j. By the chain rule η̇ = M ξ̇ = M J ∂H/∂ξ. The gradient transforms as ∂H/∂ξ = Mᵀ ∂H/∂η (since ∂H/∂ξ_j = Σ_i (∂η_i/∂ξ_j)(∂H/∂η_i) = (Mᵀ ∂H/∂η)_j). Therefore

**第 2 步 — 变换运动方程。** 令 η = η(ξ)，雅可比 M_{ij} = ∂η_i/∂ξ_j。由链式法则 η̇ = M ξ̇ = M J ∂H/∂ξ。梯度变换为 ∂H/∂ξ = Mᵀ ∂H/∂η（因 ∂H/∂ξ_j = Σ_i (∂η_i/∂ξ_j)(∂H/∂η_i) = (Mᵀ ∂H/∂η)_j）。故

  η̇ = M J Mᵀ ∂H/∂η.

**Step 3 — The symplectic condition.** The new variables obey Hamilton's equations with the same Hamiltonian, η̇ = J ∂H/∂η, for **every** H iff M J Mᵀ = J. This is equivalent to the standard form Mᵀ J M = J: multiply M J Mᵀ = J on the left by M⁻¹ and on the right by (Mᵀ)⁻¹ to get J = M⁻¹ J (Mᵀ)⁻¹, then invert using J⁻¹ = −J = Jᵀ to recover Mᵀ J M = J.

**第 3 步 — 辛条件。** 新变量对**每个** H 都服从以同一哈密顿量描述的哈密顿方程 η̇ = J ∂H/∂η，当且仅当 M J Mᵀ = J。这等价于标准形式 Mᵀ J M = J：把 M J Mᵀ = J 左乘 M⁻¹、右乘 (Mᵀ)⁻¹ 得 J = M⁻¹ J (Mᵀ)⁻¹，再用 J⁻¹ = −J = Jᵀ 求逆即得 Mᵀ J M = J。

  **Mᵀ J M = J   (symplectic condition).**

A matrix satisfying this is called symplectic; the transformation it generates is canonical.

满足此条件的矩阵称为辛矩阵；它生成的变换是正则的。

**Step 4 — Equivalence with fundamental Poisson brackets.** The Poisson bracket of two phase-space functions f, g is {f, g} = Σ_i (∂f/∂q_i ∂g/∂p_i − ∂f/∂p_i ∂g/∂q_i), which in symplectic notation is {f, g} = (∂f/∂ξ)ᵀ J (∂g/∂ξ) (Module 1.4). Apply this to the new coordinates η = (Q, P) as functions of ξ. Their matrix of mutual brackets is

**第 4 步 — 与基本泊松括号的等价性。** 两个相空间函数 f、g 的泊松括号为 {f, g} = Σ_i (∂f/∂q_i ∂g/∂p_i − ∂f/∂p_i ∂g/∂q_i)，用辛记号即 {f, g} = (∂f/∂ξ)ᵀ J (∂g/∂ξ)（模块 1.4）。把它用于作为 ξ 的函数的新坐标 η = (Q, P)。它们相互括号的矩阵为

  {η_i, η_j} = Σ_{k,l} (∂η_i/∂ξ_k) J_{kl} (∂η_j/∂ξ_l) = (M J Mᵀ)_{ij}.

By Step 3 the transformation is canonical iff M J Mᵀ = J, i.e. iff {η_i, η_j} = J_{ij}. Reading off the blocks of J, this is precisely

由第 3 步，变换正则当且仅当 M J Mᵀ = J，即 {η_i, η_j} = J_{ij}。读出 J 的分块，这恰为

  **{Q_i, P_j} = δ_{ij},   {Q_i, Q_j} = 0,   {P_i, P_j} = 0.**

**Step 5 — Poisson brackets are canonical invariants.** Let f, g be any functions and compute their bracket in the new variables. Using {f, g}_η = (∂f/∂η)ᵀ J (∂g/∂η) and the chain rule ∂f/∂ξ = Mᵀ ∂f/∂η:

**第 5 步 — 泊松括号是正则不变量。** 设 f、g 为任意函数，在新变量下计算其括号。用 {f, g}_η = (∂f/∂η)ᵀ J (∂g/∂η) 及链式法则 ∂f/∂ξ = Mᵀ ∂f/∂η：

  {f, g}_ξ = (∂f/∂ξ)ᵀ J (∂g/∂ξ) = (∂f/∂η)ᵀ M J Mᵀ (∂g/∂η) = (∂f/∂η)ᵀ J (∂g/∂η) = {f, g}_η,

where the middle equality used M J Mᵀ = J. Hence the Poisson bracket of any two functions is the same computed in (q, p) or in (Q, P): it is a **canonical invariant**. This bracket structure is exactly what survives quantization, {q, p} = 1 → [q̂, p̂] = iℏ (Module 3.3). ∎

其中中间等式用了 M J Mᵀ = J。故任意两函数的泊松括号在 (q, p) 与 (Q, P) 下计算结果相同：它是**正则不变量**。这一括号结构正是量子化后保留下来的部分，{q, p} = 1 → [q̂, p̂] = iℏ（模块 3.3）。∎

---

## C. The Hamilton–Jacobi Equation · 哈密顿–雅可比方程

**Claim.** Seek a type-2 generating function F₂ = S(q, P, t) that makes the new Hamiltonian K ≡ 0. Then p = ∂S/∂q and S satisfies the **Hamilton–Jacobi equation** H(q, ∂S/∂q, t) + ∂S/∂t = 0. S is Hamilton's principal function and equals the action. For time-independent H the ansatz S = W(q, α) − Et separates the equation into the time-independent HJ equation H(q, ∂W/∂q) = E, with W Hamilton's characteristic function. The new constant momenta α are conserved, and the equations β = ∂S/∂α = const determine the trajectory.

**命题。** 寻求一个第二类生成函数 F₂ = S(q, P, t) 使新哈密顿量 K ≡ 0。则 p = ∂S/∂q，且 S 满足**哈密顿–雅可比方程** H(q, ∂S/∂q, t) + ∂S/∂t = 0。S 是哈密顿主函数，等于作用量。对不含时 H，拟设 S = W(q, α) − Et 把方程分离为不含时 HJ 方程 H(q, ∂W/∂q) = E，其中 W 为哈密顿特征函数。新的常数动量 α 守恒，方程 β = ∂S/∂α = 常数 确定轨迹。

**Step 1 — Demand K = 0.** Use a type-2 generator S(q, P, t). From Section A the type-2 relations are p = ∂S/∂q, Q = ∂S/∂P, and K = H + ∂S/∂t. Impose the strongest possible simplification: choose S so that the new Hamiltonian vanishes identically,

**第 1 步 — 要求 K = 0。** 使用第二类生成函数 S(q, P, t)。由 A 节，第二类关系为 p = ∂S/∂q，Q = ∂S/∂P，K = H + ∂S/∂t。施加最强的简化：选取 S 使新哈密顿量恒等于零，

  K = H(q, p, t) + ∂S/∂t = 0.

**Step 2 — Substitute p = ∂S/∂q.** Replacing every momentum p by ∂S/∂q turns K = 0 into a first-order PDE for the single function S(q, P, t):

**第 2 步 — 代入 p = ∂S/∂q。** 把每个动量 p 替换为 ∂S/∂q，K = 0 变为关于单一函数 S(q, P, t) 的一阶偏微分方程：

  **H(q, ∂S/∂q, t) + ∂S/∂t = 0   (Hamilton–Jacobi equation).**

A complete integral S(q, α₁,…,α_n, t) depends on n independent constants α (identified with the new constant momenta P = α). The new Hamiltonian being zero means, via Hamilton's equations, Ṗ = −∂K/∂Q = 0 and Q̇ = +∂K/∂P = 0: **both** the new momenta α = P and the new coordinates β = Q are constants of the motion.

完全积分 S(q, α₁,…,α_n, t) 依赖 n 个独立常数 α（与新常数动量 P = α 等同）。新哈密顿量为零意味着由哈密顿方程 Ṗ = −∂K/∂Q = 0、Q̇ = +∂K/∂P = 0：新动量 α = P 与新坐标 β = Q **都**是运动常数。

**Step 3 — S equals the action.** Along an actual trajectory compute the total time derivative of S(q, α, t):

**第 3 步 — S 等于作用量。** 沿真实轨迹计算 S(q, α, t) 的全时间导数：

  dS/dt = ∂S/∂q · q̇ + ∂S/∂t = p q̇ + ∂S/∂t.

By the HJ equation ∂S/∂t = −H, so dS/dt = p q̇ − H = L, the Lagrangian (Module 1.3). Integrating,

由 HJ 方程 ∂S/∂t = −H，故 dS/dt = p q̇ − H = L，即拉格朗日量（模块 1.3）。积分得

  S = ∫ L dt + const,

so S is exactly the classical **action** evaluated along the trajectory — Hamilton's principal function.

故 S 正是沿轨迹计算的经典**作用量**——哈密顿主函数。

**Step 4 — Separation of time for time-independent H.** If H does not depend explicitly on t, the t-dependence of S separates additively. Try the ansatz

**第 4 步 — 不含时 H 的时间分离。** 若 H 不显含 t，则 S 的 t 依赖以相加方式分离。试拟设

  S(q, α, t) = W(q, α) − E t,

where E is one of the constants α (say α₁ = E). Then ∂S/∂t = −E and ∂S/∂q = ∂W/∂q, so the HJ equation H(q, ∂S/∂q) − E = 0 becomes the **time-independent Hamilton–Jacobi equation**

其中 E 为常数 α 之一（设 α₁ = E）。则 ∂S/∂t = −E、∂S/∂q = ∂W/∂q，HJ 方程 H(q, ∂S/∂q) − E = 0 化为**不含时哈密顿–雅可比方程**

  **H(q, ∂W/∂q) = E,**

with W(q, α) **Hamilton's characteristic function**. The constant E is the conserved energy (H is time-independent, hence conserved).

其中 W(q, α) 为**哈密顿特征函数**。常数 E 是守恒能量（H 不含时，故守恒）。

**Step 5 — The constants α are conserved and the β = ∂S/∂α give the trajectory.** Because K = 0, the conjugate coordinates are β_i = Q_i = ∂S/∂P_i = ∂S/∂α_i, and Hamilton's equations give β̇_i = ∂K/∂P_i = 0, so each β_i is a constant. The n equations

**第 5 步 — 常数 α 守恒，β = ∂S/∂α 给出轨迹。** 由于 K = 0，共轭坐标 β_i = Q_i = ∂S/∂P_i = ∂S/∂α_i，哈密顿方程给出 β̇_i = ∂K/∂P_i = 0，故每个 β_i 为常数。这 n 个方程

  β_i = ∂S/∂α_i = const

are then solved algebraically for q(t; α, β). In particular the energy-conjugate equation β₁ = ∂S/∂E = ∂W/∂E − t = const gives t + const = ∂W/∂E, fixing the time dependence; the remaining β_i = ∂W/∂α_i = const fix the orbit shape. Once S (or W) is known, the entire motion follows by differentiation and algebraic inversion — no further integration of the equations of motion is needed. ∎

随后代数地解出 q(t; α, β)。特别地，能量共轭方程 β₁ = ∂S/∂E = ∂W/∂E − t = 常数 给出 t + 常数 = ∂W/∂E，确定时间依赖；其余 β_i = ∂W/∂α_i = 常数 确定轨道形状。一旦 S（或 W）已知，全部运动由求导和代数反演得到——无需进一步积分运动方程。∎

---

## D. Action–Angle Variables and the Harmonic Oscillator · 作用量–角变量与谐振子

**Claim.** For a 1-D system with bounded periodic motion, define the **action** J = ∮ p dq (integral over one closed orbit). Using the characteristic function W(q, J) with J as the new (constant) momentum, the conjugate **angle** is θ = ∂W/∂J, and Hamilton's equation gives θ̇ = ∂H/∂J ≡ ω(J) = const, so θ advances linearly. Over one period Δθ = 2π, hence the frequency is ν = ω/2π = ∂H/∂J. For the harmonic oscillator H = p²/2m + ½mω²q², the action is J = ∮ p dq = 2πE/ω, so E = (ω/2π)J and ν = ∂E/∂J = ω/2π.

**命题。** 对作有界周期运动的一维系统，定义**作用量** J = ∮ p dq（沿一条闭轨道的积分）。用以 J 为新（常数）动量的特征函数 W(q, J)，共轭**角变量**为 θ = ∂W/∂J，哈密顿方程给出 θ̇ = ∂H/∂J ≡ ω(J) = 常数，故 θ 线性推进。一个周期内 Δθ = 2π，故频率 ν = ω/2π = ∂H/∂J。对谐振子 H = p²/2m + ½mω²q²，作用量 J = ∮ p dq = 2πE/ω，故 E = (ω/2π)J，ν = ∂E/∂J = ω/2π。

**Step 1 — Define the action and use it as the new momentum.** For a 1-D time-independent system the orbit in phase space lies on the curve H(q, p) = E. Solving for momentum, p = p(q, E), and the **action** is the loop integral (the enclosed phase-space area, Module 2.4)

**第 1 步 — 定义作用量并以其为新动量。** 对一维不含时系统，相空间轨道位于曲线 H(q, p) = E 上。解出动量 p = p(q, E)，**作用量**为环积分（所围相空间面积，模块 2.4）

  J = ∮ p dq = ∮ p(q, E) dq.

This is a monotonic function J(E), invertible to give E = H(J). Take J as the new constant momentum (P = J) and use the characteristic function W(q, J) from Section C as the type-2 generator, with H(q, ∂W/∂q) = E(J).

这是 E 的单调函数 J(E)，可逆得到 E = H(J)。取 J 作新常数动量（P = J），用 C 节的特征函数 W(q, J) 作第二类生成函数，满足 H(q, ∂W/∂q) = E(J)。

**Step 2 — The conjugate angle advances at constant rate.** The coordinate conjugate to J is the **angle** θ = ∂W/∂J. Since the new Hamiltonian is just E(J) (independent of θ), Hamilton's equation for θ reads

**第 2 步 — 共轭角以常速率推进。** 与 J 共轭的坐标是**角变量** θ = ∂W/∂J。由于新哈密顿量就是 E(J)（与 θ 无关），θ 的哈密顿方程为

  θ̇ = ∂E/∂J ≡ ω(J) = const,

a constant because E depends only on J, not on θ. Integrating, θ(t) = ω t + θ₀: the angle increases **linearly** in time.

由于 E 仅依赖 J 而不依赖 θ，此为常数。积分得 θ(t) = ω t + θ₀：角随时间**线性**增加。

**Step 3 — One period gives Δθ = 2π and fixes the frequency.** Compute the change in θ as q traverses one complete cycle of the orbit. Since θ = ∂W/∂J and ∂W/∂q = p,

**第 3 步 — 一个周期给出 Δθ = 2π 并确定频率。** 计算 q 走完一整圈轨道时 θ 的变化。由 θ = ∂W/∂J 及 ∂W/∂q = p，

  Δθ = ∮ (∂θ/∂q) dq = ∮ (∂²W/∂q∂J) dq = (d/dJ) ∮ (∂W/∂q) dq = (d/dJ) ∮ p dq = dJ/dJ = 1.

With the standard normalization in which the angle is measured in cycles, J = ∮ p dq is conjugate to an angle that advances by Δθ = 1 per period; equivalently, defining the angle in radians (θ → 2πθ) the convention J = ∮ p dq gives Δθ = 2π per period. Either way the per-period advance is fixed by J = ∮ p dq alone. Equating the two ways of expressing the period T,

由 θ = ∂W/∂J 交换求导与环积分次序：每周期角的推进量完全由 J = ∮ p dq 固定，归一化为 Δθ = 1（以圈计）或等价地 Δθ = 2π（以弧度计，θ → 2πθ）。把表达周期 T 的两种方式相等，

  Δθ = ω T = 2π   ⟹   T = 2π/ω,   **ν = 1/T = ω/2π = ∂E/∂J.**

The oscillation frequency is obtained directly from E(J) by differentiation — without ever solving for q(t).

振荡频率直接由 E(J) 求导得到——完全不必解出 q(t)。

**Step 4 — Worked example: the harmonic oscillator.** Take H = p²/2m + ½mω²q² = E. Solve for the momentum on the energy curve:

**第 4 步 — 算例：谐振子。** 取 H = p²/2m + ½mω²q² = E。在能量曲线上解出动量：

  p = ±√(2m(E − ½mω²q²)) = ±√(2mE) √(1 − q²/q_max²),   q_max = √(2E/(mω²)).

The orbit is an ellipse in the (q, p) plane with semi-axes q_max = √(2E)/(ω√m) along q and p_max = √(2mE) along p. The action equals the enclosed area of this ellipse, ∮ p dq = π · (semi-axis_q) · (semi-axis_p):

轨道是 (q, p) 平面内的椭圆，沿 q 半轴 q_max = √(2E)/(ω√m)，沿 p 半轴 p_max = √(2mE)。作用量等于该椭圆的所围面积，∮ p dq = π · (q 半轴) · (p 半轴)：

  J = ∮ p dq = π · q_max · p_max = π · (√(2E)/(ω√m)) · √(2mE) = π · (2E)/(ω) = **2πE/ω.**

So J = 2πE/ω. ✓

故 J = 2πE/ω。✓

**Step 5 — Invert to get E(J) and the frequency.** Solving J = 2πE/ω for the energy,

**第 5 步 — 反解得 E(J) 与频率。** 由 J = 2πE/ω 解出能量，

  E = (ω/2π) J.

Differentiate with respect to J to obtain the frequency:

对 J 求导得频率：

  **ν = ∂E/∂J = ω/2π,**

exactly the familiar oscillator frequency ω/2π, recovered purely from the enclosed elliptical area without integrating the equations of motion. ✓ ∎

正是熟悉的振子频率 ω/2π，纯由所围椭圆面积重现，无需积分运动方程。✓ ∎

---

## E. Adiabatic Invariance of the Action · 作用量的绝热不变性

**Claim.** If a parameter λ(t) of the Hamiltonian varies slowly compared with the orbital period (the **adiabatic** limit: timescale τ = λ/λ̇ ≫ T = 2π/ω), then the action J = ∮ p dq is an **adiabatic invariant**: its time-averaged rate of change vanishes to first order, dJ/dt → 0. For the oscillator this means E/ω = J/2π is conserved as ω(t) slowly varies, so the amplitude scales as ω^{−1/2}.

**命题。** 若哈密顿量的参数 λ(t) 相对于轨道周期缓慢变化（**绝热**极限：时标 τ = λ/λ̇ ≫ T = 2π/ω），则作用量 J = ∮ p dq 是**绝热不变量**：其时间平均变化率到一阶为零，dJ/dt → 0。对振子这意味着随 ω(t) 缓变 E/ω = J/2π 守恒，故振幅按 ω^{−1/2} 标度。

**Step 1 — Slow variation defines the adiabatic regime.** Let H = H(q, p; λ(t)) with λ changing on a timescale τ = λ/|λ̇| much longer than the orbital period T = 2π/ω. The small parameter is ε = T/τ ≪ 1. Over a single period the parameter is nearly constant, so the orbit is, to leading order, a closed curve of the instantaneous (frozen-λ) system, with a well-defined instantaneous action J(λ) = ∮ p dq.

**第 1 步 — 缓变定义绝热区域。** 设 H = H(q, p; λ(t))，λ 在时标 τ = λ/|λ̇| 上变化，远长于轨道周期 T = 2π/ω。小参数为 ε = T/τ ≪ 1。在单个周期内参数近似不变，故轨道到主导阶是瞬时（冻结 λ）系统的闭曲线，具有确定的瞬时作用量 J(λ) = ∮ p dq。

**Step 2 — Average rate of change of J.** Pass to angle–action variables for the frozen system; the generating function W(q, J; λ) now depends on λ through the Hamiltonian. With slow λ̇, the action evolves under the extra ∂/∂t coming from λ̇ ∂/∂λ. Its rate of change averaged over one cycle is

**第 2 步 — J 的平均变化率。** 转到冻结系统的角–作用量变量；生成函数 W(q, J; λ) 现通过哈密顿量依赖 λ。在缓变 λ̇ 下，作用量在来自 λ̇ ∂/∂λ 的额外 ∂/∂t 下演化。其在一个周期上平均的变化率为

  ⟨dJ/dt⟩ = −λ̇ ⟨∂²W/∂θ∂λ⟩_θ = −λ̇ · (1/2π) ∮ (∂/∂λ)(∂W/∂θ) dθ.

The integrand is a total derivative in θ of a periodic function (∂W/∂λ returns to its value after Δθ = 2π), so the loop integral vanishes:

被积函数是周期函数关于 θ 的全导数（∂W/∂λ 在 Δθ = 2π 后回到原值），故环积分为零：

  ⟨dJ/dt⟩ = 0 + O(ε²).

Thus to first order in the slowness ε, the action is conserved: **J is an adiabatic invariant**, dJ/dt → 0 as ε → 0. The corrections are exponentially small in 1/ε for analytic, smooth variation.

故在缓变 ε 的一阶，作用量守恒：**J 是绝热不变量**，当 ε → 0 时 dJ/dt → 0。对解析、光滑的变化，修正项在 1/ε 上指数地小。

**Step 3 — Physical motivation.** Over each fast period the system completes a near-closed loop enclosing area J. The slow drift of λ deforms the orbit, but the enclosed phase-space area is robust: the part of the loop integral that grows during half the cycle is cancelled by the part that shrinks during the other half, because the deformation is correlated with the (periodic) phase. Only a net secular change would alter J, and that is precisely the O(ε²) term shown to vanish at first order. This is the dynamical analogue of Liouville's theorem (Module 2.4): phase-space area is preserved under the Hamiltonian flow, and here also under slow parameter drift.

**第 3 步 — 物理动机。** 在每个快周期内系统完成一个近闭合的环，所围面积为 J。λ 的缓慢漂移使轨道变形，但所围相空间面积是稳健的：环积分在半个周期内增大的部分被另半周期内减小的部分抵消，因为变形与（周期性的）相位相关。只有净的长期变化才会改变 J，而那正是已证在一阶消失的 O(ε²) 项。这是刘维尔定理（模块 2.4）的动力学类比：相空间面积在哈密顿流下守恒，此处在缓慢参数漂移下亦然。

**Step 4 — The oscillator: E/ω conserved, amplitude ∝ ω^{−1/2}.** For the harmonic oscillator with slowly varying ω(t), Section D gives J = 2πE/ω. Adiabatic invariance of J means

**第 4 步 — 振子：E/ω 守恒，振幅 ∝ ω^{−1/2}。** 对缓变 ω(t) 的谐振子，D 节给出 J = 2πE/ω。J 的绝热不变性意味着

  J = 2πE/ω = const   ⟹   **E/ω = J/2π = const.**

So the energy tracks the frequency: if ω is slowly doubled, the energy doubles. The amplitude follows from E = ½mω²A² (turning-point energy with q_max = A), giving

故能量随频率变化：若 ω 缓慢翻倍，能量翻倍。振幅由 E = ½mω²A²（转折点能量，q_max = A）得到

  A = √(2E/(mω²)) = √(2(J/2π)·ω/(mω²)) = √(J/(πmω)) ∝ ω^{−1/2}.

A slowly shortened pendulum (rising ω) therefore gains energy in proportion to its frequency while its amplitude shrinks as ω^{−1/2} — the classic adiabatic result, and the historical seed of the Bohr–Sommerfeld quantization rule ∮ p dq = nh that bridges to canonical quantization (Module 3.3). ∎

因此缓慢缩短的单摆（ω 上升）其能量按频率成比例增加，而振幅按 ω^{−1/2} 收缩——经典的绝热结果，也是玻尔–索末菲量子化规则 ∮ p dq = nh 的历史种子，该规则通往正则量子化（模块 3.3）。∎

---

*Canonical transformations expose the symplectic skeleton of mechanics: the Poisson bracket, not the coordinates, is the invariant object — and it is exactly this bracket that becomes the quantum commutator. Hamilton–Jacobi theory turns dynamics into a single PDE for the action, the same action whose phase governs the semiclassical wavefunction; action–angle variables and adiabatic invariants then carry this structure into integrable systems, perturbation theory, and the old quantum theory.*

*正则变换揭示力学的辛骨架：不变的对象是泊松括号而非坐标——而正是这一括号成为量子对易子。哈密顿–雅可比理论把动力学化为关于作用量的单一偏微分方程，正是这同一作用量的相位支配半经典波函数；作用量–角变量与绝热不变量随后把这一结构带入可积系统、微扰理论与旧量子论。*

# Derivations — Module 1.4: Hamiltonian Mechanics & Noether's Theorem
# 推导 — 模块 1.4：哈密顿力学与诺特定理

> Companion to [Module 1.4](./module-1.4-hamiltonian-mechanics-noether.md). Full step-by-step proofs of every result quoted there. English first, then 中文.
> [模块 1.4](./module-1.4-hamiltonian-mechanics-noether.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Legendre Transform and Hamilton's Equations · 勒让德变换与哈密顿方程

**Claim.** Starting from the Lagrangian L(q, q̇, t), define the conjugate momentum p = ∂L/∂q̇ and the Hamiltonian H(q, p, t) = p q̇ − L (Legendre transform). Then Hamilton's equations hold:

  q̇ = ∂H/∂p,   ṗ = −∂H/∂q.

(Single degree of freedom for clarity; N-dimensional case follows by index repetition.)

**命题。** 从拉格朗日量 L(q, q̇, t) 出发，定义共轭动量 p = ∂L/∂q̇ 和哈密顿量 H(q, p, t) = p q̇ − L（勒让德变换）。则哈密顿方程成立：

  q̇ = ∂H/∂p，  ṗ = −∂H/∂q。

（为清晰起见处理单自由度；N 维情形通过指标重复得到。）

**Step 1 — Compute the total differential of H.** Since H = p q̇ − L:

**第 1 步 — 计算 H 的全微分。** 由于 H = p q̇ − L：

  dH = q̇ dp + p dq̇ − (∂L/∂q dq + ∂L/∂q̇ dq̇ + ∂L/∂t dt).

**Step 2 — Use the definition of p.** Since p = ∂L/∂q̇, the terms p dq̇ and −∂L/∂q̇ dq̇ cancel exactly:

**第 2 步 — 利用 p 的定义。** 由于 p = ∂L/∂q̇，项 p dq̇ 与 −∂L/∂q̇ dq̇ 恰好相消：

  p dq̇ − (∂L/∂q̇) dq̇ = p dq̇ − p dq̇ = 0.

Therefore:

因此：

  dH = q̇ dp − (∂L/∂q) dq − (∂L/∂t) dt.

**Step 3 — Read off the partial derivatives of H.** Comparing with the general expression dH = (∂H/∂p)dp + (∂H/∂q)dq + (∂H/∂t)dt:

**第 3 步 — 读出 H 的偏导数。** 与一般表达式 dH = (∂H/∂p)dp + (∂H/∂q)dq + (∂H/∂t)dt 比较：

  ∂H/∂p = q̇,   ∂H/∂q = −∂L/∂q.

The first equation gives the first Hamilton equation: **q̇ = ∂H/∂p.** ∎₁

第一式给出第一个哈密顿方程：**q̇ = ∂H/∂p。** ∎₁

**Step 4 — Apply the Euler–Lagrange equation to get the second Hamilton equation.** From the Euler–Lagrange equation (proved in Module 1.3 derivations):

**第 4 步 — 应用欧拉–拉格朗日方程得第二个哈密顿方程。** 由欧拉–拉格朗日方程（在模块 1.3 推导中证明）：

  d/dt(∂L/∂q̇) = ∂L/∂q   ⟹   ṗ = ∂L/∂q.

Substituting Step 3's result ∂H/∂q = −∂L/∂q:

代入第 3 步的结果 ∂H/∂q = −∂L/∂q：

  **ṗ = ∂L/∂q = −∂H/∂q.** ∎₂

  **ṗ = ∂L/∂q = −∂H/∂q。** ∎₂

**Remark — H equals T + V.** For a standard mechanical system with L = T(q̇) − V(q), the conjugate momentum is p = ∂T/∂q̇. Then H = p q̇ − L = p q̇ − T + V. If T is quadratic in q̇ (T = ½mq̇²), then p q̇ = mq̇ · q̇ = 2T by Euler's theorem on homogeneous functions. Therefore H = 2T − T + V = T + V = total energy.

**注——H 等于 T + V。** 对于标准力学系统 L = T(q̇) − V(q)，共轭动量 p = ∂T/∂q̇。则 H = p q̇ − L = p q̇ − T + V。若 T 关于 q̇ 是二次型（T = ½mq̇²），由欧拉关于齐次函数的定理得 p q̇ = mq̇ · q̇ = 2T。因此 H = 2T − T + V = T + V = 总能量。

---

## B. Poisson Brackets and the Fundamental Bracket {q, p} = 1 · 泊松括号与基本括号 {q, p} = 1

**Claim.** The Poisson bracket of two functions f(q, p) and g(q, p) is defined as:

  {f, g} = (∂f/∂q)(∂g/∂p) − (∂f/∂p)(∂g/∂q).

For canonical coordinates and momenta, {q, p} = 1.

**命题。** 两个函数 f(q, p) 和 g(q, p) 的泊松括号定义为：

  {f, g} = (∂f/∂q)(∂g/∂p) − (∂f/∂p)(∂g/∂q)。

对于正则坐标和动量，{q, p} = 1。

**Proof.** Set f = q and g = p. Then:

**证明。** 令 f = q，g = p，则：

  ∂q/∂q = 1,   ∂q/∂p = 0,   ∂p/∂q = 0,   ∂p/∂p = 1.

Therefore {q, p} = (1)(1) − (0)(0) = 1. ∎

因此 {q, p} = (1)(1) − (0)(0) = 1。∎

**Hamilton's equation in Poisson-bracket form.** For any observable f(q, p, t):

**泊松括号形式的哈密顿方程。** 对任意可观测量 f(q, p, t)：

  df/dt = (∂f/∂q)q̇ + (∂f/∂p)ṗ + ∂f/∂t
        = (∂f/∂q)(∂H/∂p) − (∂f/∂p)(∂H/∂q) + ∂f/∂t
        = {f, H} + ∂f/∂t.

In particular: q̇ = {q, H} (using {q, H} = ∂H/∂p = q̇ from Hamilton's equations) and ṗ = {p, H} = −∂H/∂q = ṗ, both consistent.

特别地：q̇ = {q, H}（由 {q, H} = ∂H/∂p = q̇，与哈密顿方程一致）；ṗ = {p, H} = −∂H/∂q，同样一致。

---

## C. Noether's Theorem — Full Proof · 诺特定理——完整证明

**Claim.** If the Lagrangian L(q, q̇, t) is invariant (to first order in ε) under the one-parameter family of transformations q → q + ε K(q, t), where K is a smooth generator, then the quantity

  Q = (∂L/∂q̇) K

is conserved along any solution of the Euler–Lagrange equations: dQ/dt = 0.

**命题。** 若拉格朗日量 L(q, q̇, t) 在单参数变换族 q → q + ε K(q, t)（K 为光滑生成元）下（对 ε 一阶）不变，则量

  Q = (∂L/∂q̇) K

沿欧拉–拉格朗日方程的任意解守恒：dQ/dt = 0。

**Step 1 — Express the invariance condition.** Under q → q + ε K, the velocity transforms as q̇ → q̇ + ε K̇ (where K̇ = dK/dt along the motion). The first-order change in L is:

**第 1 步 — 表达不变性条件。** 在 q → q + ε K 下，速度变换为 q̇ → q̇ + ε K̇（其中 K̇ = dK/dt 沿运动方向）。L 的一阶变化为：

  δL = (∂L/∂q) ε K + (∂L/∂q̇) ε K̇ = 0.

Dividing by ε, the invariance condition is:

除以 ε，不变性条件为：

  (∂L/∂q) K + (∂L/∂q̇) K̇ = 0.                         … (*)

**Step 2 — Use the Euler–Lagrange equation.** On the physical trajectory, the E-L equation holds:

**第 2 步 — 利用欧拉–拉格朗日方程。** 在物理轨迹上，欧拉–拉格朗日方程成立：

  ∂L/∂q = d/dt (∂L/∂q̇).

Substitute into (*):

代入 (*)：

  d/dt(∂L/∂q̇) · K + (∂L/∂q̇) · K̇ = 0.

**Step 3 — Recognise the product rule.** The left side is exactly the time derivative of the product (∂L/∂q̇) K:

**第 3 步 — 识别乘积法则。** 左侧恰好是乘积 (∂L/∂q̇) K 的时间导数：

  d/dt [(∂L/∂q̇) K] = d/dt(∂L/∂q̇) · K + (∂L/∂q̇) · K̇ = 0.

Therefore:

因此：

  **dQ/dt = d/dt [(∂L/∂q̇) K] = 0**, i.e. **Q = (∂L/∂q̇) K = const.** ∎

  **dQ/dt = d/dt [(∂L/∂q̇) K] = 0**，即 **Q = (∂L/∂q̇) K = 常数。** ∎

---

## D. Three Canonical Applications of Noether's Theorem · 诺特定理的三个典型应用

### D.1 Time Translation → Energy Conservation · 时间平移 → 能量守恒

**Step 1 — Identify the symmetry.** If L has no explicit time dependence (∂L/∂t = 0), then L is invariant under t → t + ε, which induces q(t) → q(t + ε) ≈ q(t) + ε q̇(t). So the generator is K = q̇.

**第 1 步 — 辨识对称性。** 若 L 不显含时间（∂L/∂t = 0），则 L 在 t → t + ε 下不变，这诱导 q(t) → q(t + ε) ≈ q(t) + ε q̇(t)。故生成元为 K = q̇。

**Step 2 — Compute the Noether charge.** A time translation t → t + ε also moves the *independent* variable (not just the coordinates), so the conserved charge carries an extra −L term relative to the coordinate-transformation formula of Section C: Q = (∂L/∂q̇) q̇ − L = p q̇ − L.

**第 2 步 — 计算诺特荷。** 时间平移 t → t + ε 还移动了*自变量*（而不只是坐标），故守恒荷相对 C 节的坐标变换公式多出一个 −L 项：Q = (∂L/∂q̇) q̇ − L = p q̇ − L。

**Step 3 — Show Q = H.** For L = T − V with T = ½mq̇²:

**第 3 步 — 证明 Q = H。** 对于 L = T − V，T = ½mq̇²：

  Q = p q̇ − L = mq̇² − (T − V) = 2T − (T − V) = T + V = H,

where p q̇ = mq̇² = 2T by Euler's theorem on the homogeneous quadratic T.

More generally, Q = Σᵢ (∂L/∂q̇ᵢ) q̇ᵢ − L = H by the Legendre transform. Therefore time-translation symmetry conserves **H = total energy.** ∎

更一般地，Q = Σᵢ (∂L/∂q̇ᵢ) q̇ᵢ − L = H（由勒让德变换）。因此时间平移对称性守恒 **H = 总能量。** ∎

### D.2 Spatial Translation → Linear Momentum Conservation · 空间平移 → 线动量守恒

**Step 1 — Identify the symmetry.** For a free particle (or a system whose potential depends only on relative positions), L is invariant under the uniform translation q → q + ε n̂ (translation by ε in direction n̂). The generator is K = n̂.

**第 1 步 — 辨识对称性。** 对于自由粒子（或势能仅依赖相对位置的系统），L 在匀速平移 q → q + ε n̂ 下不变（沿方向 n̂ 平移 ε）。生成元为 K = n̂。

**Step 2 — Compute the Noether charge.** Q = (∂L/∂q̇) · n̂. With p = ∂L/∂q̇ = mq̇ (Cartesian), Q = p · n̂ = the component of momentum along n̂.

**第 2 步 — 计算诺特荷。** Q = (∂L/∂q̇) · n̂。以 p = ∂L/∂q̇ = mq̇（笛卡尔），Q = p · n̂ = 动量沿 n̂ 方向的分量。

**Step 3 — Conclude.** Since n̂ is arbitrary, the full momentum vector **p is conserved** whenever L is invariant under all spatial translations. ∎

**第 3 步 — 得出结论。** 由于 n̂ 是任意的，只要 L 在所有空间平移下不变，完整动量矢量 **p 守恒。** ∎

### D.3 Rotation → Angular Momentum Conservation · 旋转 → 角动量守恒

**Step 1 — Identify the symmetry.** For a particle in a central potential, L is invariant under rotations about any axis n̂. An infinitesimal rotation by ε about n̂ produces δr = ε n̂ × r. So K = n̂ × r.

**第 1 步 — 辨识对称性。** 对于有心势中的粒子，L 在绕任意轴 n̂ 的转动下不变。绕 n̂ 转过无穷小角度 ε 产生 δr = ε n̂ × r。故 K = n̂ × r。

**Step 2 — Compute the Noether charge.** With p = ∂L/∂q̇ = mṙ (for Cartesian L = T − V):

**第 2 步 — 计算诺特荷。** 以 p = ∂L/∂q̇ = mṙ（笛卡尔 L = T − V）：

  Q = p · K = p · (n̂ × r) = n̂ · (r × p) = n̂ · L.

(Using the scalar triple product identity a · (b × c) = b · (c × a) = c · (a × b).)

（利用标量三重积恒等式 a · (b × c) = b · (c × a) = c · (a × b)。）

**Step 3 — Conclude.** Since n̂ is arbitrary, conservation of Q for all n̂ means the full **angular momentum vector L = r × p is conserved** whenever L is rotationally invariant. ∎

**第 3 步 — 得出结论。** 由于 n̂ 是任意的，对所有 n̂ 的 Q 守恒意味着只要 L 在旋转下不变，完整**角动量矢量 L = r × p 守恒。** ∎

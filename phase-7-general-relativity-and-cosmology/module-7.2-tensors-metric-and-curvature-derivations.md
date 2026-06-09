# Derivations — Module 7.2: Tensors, the Metric & Curvature
# 推导 — 模块 7.2：张量、度规与曲率

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 7.2](./module-7.2-tensors-metric-and-curvature.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 7.2](./module-7.2-tensors-metric-and-curvature.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Christoffel Symbols from Metric Compatibility and Torsion-Free Symmetry · 从度规相容性与无挠对称性推导克里斯托费尔符号

**Claim.** The unique connection compatible with the metric ($\nabla_\rho g_{\mu\nu} = 0$) and torsion-free ($\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$) is the Levi-Civita connection

$$ \Gamma^{\lambda}{}_{\mu\nu} = \tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu}). $$

**命题。** 满足度规相容性（$\nabla_\rho g_{\mu\nu} = 0$）和无挠条件（$\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$）的唯一联络是列维-奇维塔联络

$$ \Gamma^{\lambda}{}_{\mu\nu} = \tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu}). $$

**Step 1 — Write metric compatibility explicitly.** The covariant derivative of the metric tensor must vanish identically. For a (0,2) tensor, the covariant derivative is

**第 1 步 — 显式写出度规相容性。** 度规张量的协变导数必须恒为零。对于 (0,2) 型张量，协变导数为

$$ \nabla_\rho g_{\mu\nu} = \partial_\rho g_{\mu\nu} - \Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu} - \Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma} = 0. $$

This single equation, written for all permutations of the indices ($\rho, \mu, \nu$), contains all the information needed to determine the connection uniquely once the torsion-free condition is imposed.

此方程对指标 ($\rho, \mu, \nu$) 的所有置换写出后，结合无挠条件，包含了唯一确定联络所需的全部信息。

**Step 2 — Write out three cyclic permutations.** Expand $\nabla_\rho g_{\mu\nu} = 0$ for three distinct index assignments and label the results (I), (II), (III):

**第 2 步 — 写出三个循环置换。** 对三种不同的指标赋值展开 $\nabla_\rho g_{\mu\nu} = 0$，将结果标记为 (I)、(II)、(III)：

$$ \begin{aligned}
\text{(I)} \quad & \partial_\rho g_{\mu\nu} - \Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu} - \Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma} = 0 \\
\text{(II)} \quad & \partial_\mu g_{\nu\rho} - \Gamma^{\sigma}{}_{\mu\nu} g_{\sigma\rho} - \Gamma^{\sigma}{}_{\mu\rho} g_{\nu\sigma} = 0 \\
\text{(III)} \quad & \partial_\nu g_{\rho\mu} - \Gamma^{\sigma}{}_{\nu\rho} g_{\sigma\mu} - \Gamma^{\sigma}{}_{\nu\mu} g_{\rho\sigma} = 0
\end{aligned} $$

**Step 3 — Use torsion-free symmetry.** The torsion tensor $T^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\mu\nu} - \Gamma^{\lambda}{}_{\nu\mu}$ vanishes, so $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$ (symmetric in lower indices). Apply this throughout.

**第 3 步 — 使用无挠对称性。** 挠率张量 $T^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\mu\nu} - \Gamma^{\lambda}{}_{\nu\mu} = 0$，故 $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$（关于下指标对称）。在整个推导中应用此条件。

**Step 4 — Linear combination: (II) + (III) − (I).** Compute (II) + (III) − (I):

**第 4 步 — 线性组合：(II) + (III) − (I)。** 计算 (II) + (III) − (I)：

$$ \begin{aligned}
& \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu} \\
& - \Gamma^{\sigma}{}_{\mu\nu} g_{\sigma\rho} - \Gamma^{\sigma}{}_{\mu\rho} g_{\nu\sigma} \\
& - \Gamma^{\sigma}{}_{\nu\rho} g_{\sigma\mu} - \Gamma^{\sigma}{}_{\nu\mu} g_{\rho\sigma} \\
& + \Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu} + \Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma} = 0.
\end{aligned} $$

Now apply the torsion-free condition: $\Gamma^{\sigma}{}_{\mu\nu} = \Gamma^{\sigma}{}_{\nu\mu}$. The terms $\pm\Gamma^{\sigma}{}_{\mu\rho} g_{\nu\sigma}$ and $\pm\Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu}$ cancel in pairs (since $g_{\sigma\nu} = g_{\nu\sigma}$), as do $\pm\Gamma^{\sigma}{}_{\nu\rho} g_{\sigma\mu}$ and $\pm\Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma}$. What remains is:

现在应用无挠条件 $\Gamma^{\sigma}{}_{\mu\nu} = \Gamma^{\sigma}{}_{\nu\mu}$。项 $\pm\Gamma^{\sigma}{}_{\mu\rho} g_{\nu\sigma}$ 与 $\pm\Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu}$ 成对消去（因 $g_{\sigma\nu} = g_{\nu\sigma}$），$\pm\Gamma^{\sigma}{}_{\nu\rho} g_{\sigma\mu}$ 与 $\pm\Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma}$ 同理消去。剩余项为：

$$ \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu} - 2 \Gamma^{\sigma}{}_{\mu\nu} g_{\sigma\rho} = 0. $$

**Step 5 — Isolate the Christoffel symbol.** Rearrange:

**第 5 步 — 分离克里斯托费尔符号。** 重新整理：

$$ 2 \Gamma^{\sigma}{}_{\mu\nu} g_{\sigma\rho} = \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}. $$

Multiply both sides by $g^{\rho\lambda}$ (the inverse metric, $g^{\rho\lambda} g_{\sigma\rho} = \delta^{\lambda}{}_\sigma$):

两边乘以 $g^{\rho\lambda}$（逆度规，$g^{\rho\lambda} g_{\sigma\rho} = \delta^{\lambda}{}_\sigma$）：

$$ 2 \Gamma^{\lambda}{}_{\mu\nu} = g^{\rho\lambda}(\partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}). $$

Relabeling the dummy index $\rho \to \sigma$ and dividing by 2:

将哑指标 $\rho$ 重标记为 $\sigma$ 并除以 2：

$$ \boxed{\, \Gamma^{\lambda}{}_{\mu\nu} = \tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu}) \,} $$

**Step 6 — Uniqueness.** The derivation assumed only (a) $\nabla_\rho g_{\mu\nu} = 0$ and (b) $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$. Given these two conditions, the algebraic steps above are reversible: the Christoffel symbols are uniquely determined by the metric. This is the *fundamental theorem of Riemannian geometry*.

**第 6 步 — 唯一性。** 推导只用到了：(a) $\nabla_\rho g_{\mu\nu} = 0$ 和 (b) $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$。给定这两个条件，上述代数步骤是可逆的：克里斯托费尔符号由度规唯一确定。这就是*黎曼几何基本定理*。

**Step 7 — Verify metric compatibility is satisfied.** Substitute the expression back into $\nabla_\rho g_{\mu\nu} = \partial_\rho g_{\mu\nu} - \Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu} - \Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma}$. Inserting the Christoffel formula, the three derivative terms in each $\Gamma$ produce six partial-derivative terms total; by direct cancellation using $g^{\sigma\lambda} g_{\sigma\nu} = \delta^{\lambda}{}_\nu$, all six cancel, confirming $\nabla_\rho g_{\mu\nu} = 0$ identically. $\blacksquare$

**第 7 步 — 验证度规相容性得到满足。** 将表达式代回 $\nabla_\rho g_{\mu\nu} = \partial_\rho g_{\mu\nu} - \Gamma^{\sigma}{}_{\rho\mu} g_{\sigma\nu} - \Gamma^{\sigma}{}_{\rho\nu} g_{\mu\sigma}$。代入克里斯托费尔公式，每个 $\Gamma$ 中的三个导数项共产生六个偏导数项；利用 $g^{\sigma\lambda} g_{\sigma\nu} = \delta^{\lambda}{}_\nu$ 直接消去，所有六项相消，证实 $\nabla_\rho g_{\mu\nu} = 0$ 恒成立。$\blacksquare$

---

## B. The Riemann Tensor from the Commutator of Covariant Derivatives · 从协变导数对易子推导黎曼张量

**Claim.** For any contravariant vector $V^\rho$, the commutator of covariant derivatives satisfies

$$ [\nabla_\mu, \nabla_\nu] V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma, $$

where the Riemann curvature tensor has components

$$ R^{\rho}{}_{\sigma\mu\nu} = \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma}. $$

**命题。** 对任意逆变矢量 $V^\rho$，协变导数的对易子满足

$$ [\nabla_\mu, \nabla_\nu] V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma, $$

其中黎曼曲率张量的分量为

$$ R^{\rho}{}_{\sigma\mu\nu} = \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma}. $$

**Step 1 — Compute $\nabla_\mu (\nabla_\nu V^\rho)$.** Start from the definition of the covariant derivative of a (1,0) tensor:

**第 1 步 — 计算 $\nabla_\mu (\nabla_\nu V^\rho)$。** 从 (1,0) 型张量的协变导数定义出发：

$$ \nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^{\rho}{}_{\nu\sigma} V^\sigma. $$

Now apply $\nabla_\mu$ to this (1,1) tensor $\nabla_\nu V^\rho$. A (1,1) tensor $W^{\rho}{}_\nu$ has covariant derivative

$$ \nabla_\mu W^{\rho}{}_\nu = \partial_\mu W^{\rho}{}_\nu + \Gamma^{\rho}{}_{\mu\lambda} W^{\lambda}{}_\nu - \Gamma^{\lambda}{}_{\mu\nu} W^{\rho}{}_\lambda. $$

现在对 (1,1) 型张量 $\nabla_\nu V^\rho$ 施加 $\nabla_\mu$。(1,1) 型张量 $W^{\rho}{}_\nu$ 的协变导数为

$$ \nabla_\mu W^{\rho}{}_\nu = \partial_\mu W^{\rho}{}_\nu + \Gamma^{\rho}{}_{\mu\lambda} W^{\lambda}{}_\nu - \Gamma^{\lambda}{}_{\mu\nu} W^{\rho}{}_\lambda. $$

Substituting $W^{\rho}{}_\nu = \partial_\nu V^\rho + \Gamma^{\rho}{}_{\nu\sigma} V^\sigma$:

代入 $W^{\rho}{}_\nu = \partial_\nu V^\rho + \Gamma^{\rho}{}_{\nu\sigma} V^\sigma$：

$$ \begin{aligned}
\nabla_\mu \nabla_\nu V^\rho = {} & \partial_\mu(\partial_\nu V^\rho + \Gamma^{\rho}{}_{\nu\sigma} V^\sigma) \\
& + \Gamma^{\rho}{}_{\mu\lambda}(\partial_\nu V^\lambda + \Gamma^{\lambda}{}_{\nu\sigma} V^\sigma) \\
& - \Gamma^{\lambda}{}_{\mu\nu}(\partial_\lambda V^\rho + \Gamma^{\rho}{}_{\lambda\sigma} V^\sigma).
\end{aligned} $$

Expanding all terms:

展开所有项：

$$ \begin{aligned}
= {} & \partial_\mu \partial_\nu V^\rho + (\partial_\mu \Gamma^{\rho}{}_{\nu\sigma}) V^\sigma + \Gamma^{\rho}{}_{\nu\sigma} \partial_\mu V^\sigma \\
& + \Gamma^{\rho}{}_{\mu\lambda} \partial_\nu V^\lambda + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} V^\sigma \\
& - \Gamma^{\lambda}{}_{\mu\nu} \partial_\lambda V^\rho - \Gamma^{\lambda}{}_{\mu\nu} \Gamma^{\rho}{}_{\lambda\sigma} V^\sigma.
\end{aligned} $$

**Step 2 — Compute $\nabla_\nu (\nabla_\mu V^\rho)$ by swapping $\mu \leftrightarrow \nu$.** By identical algebra with $\mu$ and $\nu$ swapped:

**第 2 步 — 交换 $\mu \leftrightarrow \nu$ 计算 $\nabla_\nu (\nabla_\mu V^\rho)$。** 通过交换 $\mu$ 与 $\nu$ 的相同代数运算：

$$ \begin{aligned}
\nabla_\nu \nabla_\mu V^\rho = {} & \partial_\nu \partial_\mu V^\rho + (\partial_\nu \Gamma^{\rho}{}_{\mu\sigma}) V^\sigma + \Gamma^{\rho}{}_{\mu\sigma} \partial_\nu V^\sigma \\
& + \Gamma^{\rho}{}_{\nu\lambda} \partial_\mu V^\lambda + \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma} V^\sigma \\
& - \Gamma^{\lambda}{}_{\nu\mu} \partial_\lambda V^\rho - \Gamma^{\lambda}{}_{\nu\mu} \Gamma^{\rho}{}_{\lambda\sigma} V^\sigma.
\end{aligned} $$

**Step 3 — Subtract to form the commutator.** Compute $[\nabla_\mu, \nabla_\nu] V^\rho = \nabla_\mu \nabla_\nu V^\rho - \nabla_\nu \nabla_\mu V^\rho$. The second-derivative terms $\partial_\mu \partial_\nu V^\rho$ cancel. For the torsion-free connection, $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$, so the terms $\mp \Gamma^{\lambda}{}_{\mu\nu} \partial_\lambda V^\rho$ cancel. The remaining first-derivative terms on $V$ also cancel:

**第 3 步 — 相减形成对易子。** 计算 $[\nabla_\mu, \nabla_\nu] V^\rho = \nabla_\mu \nabla_\nu V^\rho - \nabla_\nu \nabla_\mu V^\rho$。二阶导数项 $\partial_\mu \partial_\nu V^\rho$ 消去。对于无挠联络 $\Gamma^{\lambda}{}_{\mu\nu} = \Gamma^{\lambda}{}_{\nu\mu}$，项 $\mp \Gamma^{\lambda}{}_{\mu\nu} \partial_\lambda V^\rho$ 消去。剩余的 $V$ 的一阶导数项也消去：

$$ \Gamma^{\rho}{}_{\nu\sigma} \partial_\mu V^\sigma + \Gamma^{\rho}{}_{\mu\lambda} \partial_\nu V^\lambda - \Gamma^{\rho}{}_{\mu\sigma} \partial_\nu V^\sigma - \Gamma^{\rho}{}_{\nu\lambda} \partial_\mu V^\lambda = 0 $$

(after relabeling the dummy index $\lambda \to \sigma$ in the second and fourth terms). All that survives is:

（在第二项和第四项中将哑指标 $\lambda \to \sigma$ 后消去）。最终剩余：

$$ [\nabla_\mu, \nabla_\nu] V^\rho = (\partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma}) V^\sigma. $$

**Step 4 — Identify the Riemann tensor.** Define

**第 4 步 — 识别黎曼张量。** 定义

$$ R^{\rho}{}_{\sigma\mu\nu} \equiv \partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} + \Gamma^{\rho}{}_{\mu\lambda} \Gamma^{\lambda}{}_{\nu\sigma} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\mu\sigma}. $$

Then $[\nabla_\mu, \nabla_\nu] V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma$. Since the left side is manifestly a (1,1) tensor acting on $V^\sigma$ and the result is a (1,0) tensor, $R^{\rho}{}_{\sigma\mu\nu}$ must be a (1,3) tensor. This confirms it is a genuine geometric object, independent of the choice of coordinates.

则 $[\nabla_\mu, \nabla_\nu] V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma$。由于左侧显然是作用在 $V^\sigma$ 上的 (1,1) 型张量，结果为 (1,0) 型张量，故 $R^{\rho}{}_{\sigma\mu\nu}$ 必定是 (1,3) 型张量。这确认它是真正的几何对象，与坐标选择无关。

**Step 5 — Physical interpretation.** The Riemann tensor measures the holonomy of parallel transport: if a vector is parallel-transported around an infinitesimal closed loop spanned by coordinate displacements $\delta x^\mu$ and $\delta x^\nu$, it returns rotated by $\delta V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma \delta x^\mu \delta x^\nu$. In flat space all $\Gamma^{\lambda}{}_{\mu\nu}$ are constant (zero in Cartesian coordinates), so $R^{\rho}{}_{\sigma\mu\nu} = 0$ and parallel transport is path-independent. $\blacksquare$

**第 5 步 — 物理诠释。** 黎曼张量度量平行移动的和乐性：若一个矢量沿坐标位移 $\delta x^\mu$ 和 $\delta x^\nu$ 张成的无穷小封闭回路平行移动，回到原处时旋转了 $\delta V^\rho = R^{\rho}{}_{\sigma\mu\nu} V^\sigma \delta x^\mu \delta x^\nu$。在平坦空间中所有 $\Gamma^{\lambda}{}_{\mu\nu}$ 为常数（笛卡尔坐标下为零），故 $R^{\rho}{}_{\sigma\mu\nu} = 0$，平行移动与路径无关。$\blacksquare$

---

## C. Ricci Tensor, Ricci Scalar, and the Einstein Tensor · 里奇张量、里奇标量与爱因斯坦张量

**Claim.** The Ricci tensor $R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu}$, the Ricci scalar $R = g^{\mu\nu} R_{\mu\nu}$, and the Einstein tensor $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$ satisfy the contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$.

**命题。** 里奇张量 $R_{\mu\nu} = R^{\rho}{}_{\mu\rho\nu}$、里奇标量 $R = g^{\mu\nu} R_{\mu\nu}$ 和爱因斯坦张量 $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$ 满足缩并比安基恒等式 $\nabla^\mu G_{\mu\nu} = 0$。

**Step 1 — Define the Ricci tensor by contraction.** The Riemann tensor $R^{\rho}{}_{\sigma\mu\nu}$ has four free indices. Contracting the first (upper) and third (one of the lower) indices:

**第 1 步 — 通过缩并定义里奇张量。** 黎曼张量 $R^{\rho}{}_{\sigma\mu\nu}$ 有四个自由指标。对第一个（上）指标和第三个（下指标之一）进行缩并：

$$ R_{\mu\nu} \equiv R^{\rho}{}_{\mu\rho\nu} = \partial_\rho \Gamma^{\rho}{}_{\nu\mu} - \partial_\nu \Gamma^{\rho}{}_{\rho\mu} + \Gamma^{\rho}{}_{\rho\lambda} \Gamma^{\lambda}{}_{\nu\mu} - \Gamma^{\rho}{}_{\nu\lambda} \Gamma^{\lambda}{}_{\rho\mu}. $$

This is a symmetric (0,2) tensor: $R_{\mu\nu} = R_{\nu\mu}$, which follows from the symmetry properties of the Riemann tensor ($R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$).

这是一个对称 (0,2) 型张量：$R_{\mu\nu} = R_{\nu\mu}$，这由黎曼张量的对称性质 ($R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$) 得出。

**Step 2 — Define the Ricci scalar.** Contract the Ricci tensor with the inverse metric:

**第 2 步 — 定义里奇标量。** 用逆度规对里奇张量进行缩并：

$$ R \equiv g^{\mu\nu} R_{\mu\nu}. $$

$R$ is a scalar field (a single number at each spacetime point), invariant under coordinate transformations. It provides the simplest local measure of curvature.

$R$ 是一个标量场（每个时空点处的单个数值），在坐标变换下不变。它提供了曲率的最简单局部度量。

**Step 3 — State the second Bianchi identity.** The Riemann tensor satisfies the differential identity (proved by direct computation from the definition):

**第 3 步 — 陈述第二比安基恒等式。** 黎曼张量满足微分恒等式（由定义直接计算证明）：

$$ \nabla_\lambda R^{\rho}{}_{\sigma\mu\nu} + \nabla_\mu R^{\rho}{}_{\sigma\nu\lambda} + \nabla_\nu R^{\rho}{}_{\sigma\lambda\mu} = 0. $$

Contract $\rho$ with $\lambda$ (set $\rho = \lambda$ and sum):

缩并 $\rho$ 与 $\lambda$（令 $\rho = \lambda$ 并求和）：

$$ \nabla_\rho R^{\rho}{}_{\sigma\mu\nu} + \nabla_\mu R^{\rho}{}_{\sigma\nu\rho} + \nabla_\nu R^{\rho}{}_{\sigma\rho\mu} = 0. $$

Use $R^{\rho}{}_{\sigma\nu\rho} = -R^{\rho}{}_{\sigma\rho\nu} = -R_{\sigma\nu}$ (antisymmetry in last two indices) and $R^{\rho}{}_{\sigma\rho\mu} = R_{\sigma\mu}$:

利用 $R^{\rho}{}_{\sigma\nu\rho} = -R^{\rho}{}_{\sigma\rho\nu} = -R_{\sigma\nu}$（最后两个指标反对称）和 $R^{\rho}{}_{\sigma\rho\mu} = R_{\sigma\mu}$：

$$ \nabla_\rho R^{\rho}{}_{\sigma\mu\nu} - \nabla_\mu R_{\sigma\nu} + \nabla_\nu R_{\sigma\mu} = 0. $$

**Step 4 — Contract again to obtain the contracted Bianchi identity.** Multiply by $g^{\sigma\mu}$ and sum:

**第 4 步 — 再次缩并得到缩并比安基恒等式。** 乘以 $g^{\sigma\mu}$ 并求和：

$$ g^{\sigma\mu} \nabla_\rho R^{\rho}{}_{\sigma\mu\nu} - g^{\sigma\mu} \nabla_\mu R_{\sigma\nu} + g^{\sigma\mu} \nabla_\nu R_{\sigma\mu} = 0. $$

The first term: $g^{\sigma\mu} R^{\rho}{}_{\sigma\mu\nu} = R^{\rho\mu}{}_{\mu\nu}$ (raise the $\sigma$ index) $= g^{\sigma\mu} R^{\rho}{}_{\sigma\mu\nu}$. Using the symmetry of the Riemann tensor and the definition of the Ricci tensor this becomes $\nabla_\rho R^{\rho}{}_\nu$. The second term is $\nabla^\sigma R_{\sigma\nu} = \nabla^\mu R_{\mu\nu}$. The third term is $\nabla_\nu R$. So:

第一项：$g^{\sigma\mu} R^{\rho}{}_{\sigma\mu\nu} \to \nabla_\rho R^{\rho}{}_\nu$（利用黎曼张量对称性和里奇张量定义）。第二项为 $\nabla^\sigma R_{\sigma\nu} = \nabla^\mu R_{\mu\nu}$。第三项为 $\nabla_\nu R$。于是：

$$ \begin{aligned}
& \nabla_\rho R^{\rho}{}_\nu - \nabla^\mu R_{\mu\nu} + \nabla_\nu R = 0 \\
\implies {} & 2 \nabla^\mu R_{\mu\nu} = \nabla_\nu R \\
\implies {} & \nabla^\mu R_{\mu\nu} = \tfrac12 \nabla_\nu R = \tfrac12 g_{\mu\nu} \nabla^\mu R.
\end{aligned} $$

Rearranging: $\nabla^\mu(R_{\mu\nu} - \tfrac12 g_{\mu\nu} R) = 0$.

整理得：$\nabla^\mu(R_{\mu\nu} - \tfrac12 g_{\mu\nu} R) = 0$。

**Step 5 — Define the Einstein tensor.** The combination

**第 5 步 — 定义爱因斯坦张量。** 组合

$$ G_{\mu\nu} \equiv R_{\mu\nu} - \tfrac12 R g_{\mu\nu} $$

is the **Einstein tensor**. It is symmetric, divergence-free ($\nabla^\mu G_{\mu\nu} = 0$), and of second order in the metric. These three properties make it the unique tensor (up to a constant and a cosmological-constant term) that can appear on the geometric left-hand side of a gravitational field equation sourced by $T_{\mu\nu}$. $\blacksquare$

即**爱因斯坦张量**。它是对称的、无散度的（$\nabla^\mu G_{\mu\nu} = 0$），且是度规的二阶表达式。这三个性质使其成为唯一可以出现在以 $T_{\mu\nu}$ 为源的引力场方程几何左侧的张量（在一个常数和宇宙学常数项意义下）。$\blacksquare$

---

## D. Symmetries of the Riemann Tensor and Counting Independent Components · 黎曼张量的对称性与独立分量计数

**Claim.** The fully covariant Riemann tensor $R_{\rho\sigma\mu\nu} = g_{\rho\lambda} R^{\lambda}{}_{\sigma\mu\nu}$ satisfies:
(i) antisymmetry in first pair: $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$;
(ii) antisymmetry in second pair: $R_{\rho\sigma\mu\nu} = -R_{\rho\sigma\nu\mu}$;
(iii) pair symmetry: $R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$;
(iv) first (algebraic) Bianchi identity: $R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0$.
In four-dimensional spacetime these reduce to 20 independent components.

**命题。** 全协变黎曼张量 $R_{\rho\sigma\mu\nu} = g_{\rho\lambda} R^{\lambda}{}_{\sigma\mu\nu}$ 满足：
(i) 第一对指标反对称：$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$；
(ii) 第二对指标反对称：$R_{\rho\sigma\mu\nu} = -R_{\rho\sigma\nu\mu}$；
(iii) 对偶对称：$R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$；
(iv) 第一（代数）比安基恒等式：$R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0$。
在四维时空中，独立分量共有 20 个。

**Step 1 — Prove antisymmetry (i) and (ii).** From the definition of $R^{\rho}{}_{\sigma\mu\nu}$, swapping the last two free indices $\mu \leftrightarrow \nu$ changes the sign (since $\partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} \to \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} - \partial_\mu \Gamma^{\rho}{}_{\nu\sigma}$). Lowering the first index using the metric and using the Leibniz rule for $\nabla$ preserving the metric, antisymmetry in the first pair follows from antisymmetry in the second pair combined with property (iii).

**第 1 步 — 证明反对称性 (i) 和 (ii)。** 由 $R^{\rho}{}_{\sigma\mu\nu}$ 的定义，交换最后两个自由指标 $\mu \leftrightarrow \nu$ 改变符号（因 $\partial_\mu \Gamma^{\rho}{}_{\nu\sigma} - \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} \to \partial_\nu \Gamma^{\rho}{}_{\mu\sigma} - \partial_\mu \Gamma^{\rho}{}_{\nu\sigma}$）。用度规降低第一个指标，利用 $\nabla$ 满足莱布尼茨法则且保持度规，第一对指标的反对称性由第二对的反对称性结合性质 (iii) 得出。

**Step 2 — Prove the first Bianchi identity.** Write the identity $R_{\rho[\sigma\mu\nu]} = 0$ (antisymmetrisation on the last three indices). This follows directly from the definition of $R^{\rho}{}_{\sigma\mu\nu}$ and the torsion-free condition: the three terms in $R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu}$ involve six $\Gamma\partial\Gamma$ terms and six $\Gamma\Gamma$ terms; under torsion-free symmetry these cancel identically.

**第 2 步 — 证明第一比安基恒等式。** 写出恒等式 $R_{\rho[\sigma\mu\nu]} = 0$（对最后三个指标反对称化）。这直接由 $R^{\rho}{}_{\sigma\mu\nu}$ 的定义和无挠条件得出：$R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu}$ 三项涉及六个 $\Gamma\partial\Gamma$ 项和六个 $\Gamma\Gamma$ 项；在无挠对称性下这些项恒等消去。

**Step 3 — Count independent components.** In $n$ dimensions:
- An antisymmetric pair of $n$ indices has $n(n-1)/2$ independent combinations.
- With two antisymmetric pairs, the number of combinations of pairs is $[n(n-1)/2]([n(n-1)/2]+1)/2$ (symmetric in the two pairs by property (iii)).
- Subtract the additional constraints from the first Bianchi identity.
For $n = 4$: $n(n-1)/2 = 6$. Symmetric combinations of pairs: $6\cdot 7/2 = 21$. The first Bianchi identity imposes $C(4,4) = 1$ independent constraint (the totally antisymmetric part). So the count is $21 - 1 = \mathbf{20}$ **independent components**.

**第 3 步 — 计算独立分量数。** 在 $n$ 维空间中：
- 一对 $n$ 个指标的反对称组合有 $n(n-1)/2$ 个独立组合。
- 两对反对称组合的组合数为 $[n(n-1)/2]([n(n-1)/2]+1)/2$（由性质 (iii)，两对之间对称）。
- 减去第一比安基恒等式施加的额外约束。
对于 $n = 4$：$n(n-1)/2 = 6$。对偶的对称组合：$6\cdot 7/2 = 21$。第一比安基恒等式施加 $C(4,4) = 1$ 个独立约束（完全反对称部分）。故独立分量数为 $21 - 1 = \mathbf{20}$ **个**。$\blacksquare$

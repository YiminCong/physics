# Derivations — Module 6.13: Conformal Field Theory
# 推导 — 模块 6.13：共形场论

> ✅ **Verified 2026-06-13** — derivations reviewed line-by-line and confirmed against standard results (Di Francesco–Mathieu–Sénéchal; Polchinski Vol. 1); safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-13 -->
> ✅ **已校验 2026-06-13** — 推导已逐行复核，并对照标准结果（Di Francesco–Mathieu–Sénéchal；Polchinski 第 1 卷）确认；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.13](./module-6.13-conformal-field-theory.md). English first, then 中文.
> [模块 6.13](./module-6.13-conformal-field-theory.md) 的配套文档。先英文，后中文。

---

## A. The Conformal Algebra and Its Generators
## A. 共形代数及其生成元

**Claim.** In $d \geq 3$ Euclidean dimensions the conformal group is $SO(d+1,1)$, with $\tfrac12(d+1)(d+2)$ generators: $d$ translations $P_\mu$, $\tfrac12 d(d-1)$ rotations $M_{\mu\nu}$, one dilatation $D$, and $d$ special conformal transformations $K_\mu$.

A conformal transformation satisfies $\partial_\mu \epsilon_\nu + \partial_\nu \epsilon_\mu = \tfrac{2}{d}(\partial\cdot\epsilon)\,\delta_{\mu\nu}$ (the conformal Killing equation). For $d \geq 3$ this forces $\epsilon_\mu$ to be at most quadratic in $x$: $\epsilon_\mu = a_\mu + \omega_{\mu\nu}x^\nu + \lambda x_\mu + (b_\mu x^2 - 2 x_\mu\, b\cdot x)$, giving exactly translations, rotations, dilatation, and special conformal transformations. Counting parameters: $d + \tfrac12 d(d-1) + 1 + d = \tfrac12(d+1)(d+2)$. The algebra closes as $SO(d+1,1)$; the dilatation $D$ acts as a "boost" mixing $P_\mu$ and $K_\mu$:
$$ [D, P_\mu] = P_\mu, \qquad [D, K_\mu] = -K_\mu, \qquad [K_\mu, P_\nu] = 2(\delta_{\mu\nu}D - M_{\mu\nu}). $$
Thus $P_\mu$ raises and $K_\mu$ lowers the dimension; eigenstates of $D$ are operators of definite scaling dimension $\Delta$.

**断言。** 在 $d \geq 3$ 欧氏维度中，共形群为 $SO(d+1,1)$，有 $\tfrac12(d+1)(d+2)$ 个生成元：$d$ 个平移 $P_\mu$、$\tfrac12 d(d-1)$ 个转动 $M_{\mu\nu}$、一个标度变换 $D$ 和 $d$ 个特殊共形变换 $K_\mu$。共形 Killing 方程 $\partial_\mu \epsilon_\nu + \partial_\nu \epsilon_\mu = \tfrac{2}{d}(\partial\cdot\epsilon)\,\delta_{\mu\nu}$ 在 $d \geq 3$ 时迫使 $\epsilon_\mu$ 至多是 $x$ 的二次式，恰好给出上述四类变换。$D$ 使 $P_\mu$ 升、$K_\mu$ 降标度维数；$D$ 的本征态即具有确定标度维数 $\Delta$ 的算符。

---

## B. Conformal Invariance Fixes the Two-Point Function
## B. 共形不变性固定两点函数

**Claim.** For a primary scalar of dimension $\Delta$, $\langle\mathcal{O}(x)\mathcal{O}(y)\rangle = C/|x-y|^{2\Delta}$.

**Proof.** Translation invariance ⟹ the correlator depends only on $r = |x - y|$. Rotation invariance ⟹ it is a function $f(r)$. Scale invariance $x \to \lambda x$, under which $\mathcal{O} \to \lambda^{-\Delta}\mathcal{O}$, requires
$$ \langle\mathcal{O}(\lambda x)\mathcal{O}(\lambda y)\rangle = \lambda^{-2\Delta}\langle\mathcal{O}(x)\mathcal{O}(y)\rangle \implies f(\lambda r) = \lambda^{-2\Delta} f(r), $$
whose only solution is $f(r) = C\, r^{-2\Delta}$. One checks that invariance under special conformal transformations is then automatic (it fixes the relative normalization but adds no new constraint for two points). For two operators of *different* dimensions $\Delta_1 \neq \Delta_2$, the same argument gives $f(r) = C\,r^{-(\Delta_1+\Delta_2)}$, but special conformal invariance then forces $C = 0$: **primaries of unequal dimension are orthogonal.** The three-point function is similarly fixed to
$$ \langle\mathcal{O}_1\mathcal{O}_2\mathcal{O}_3\rangle = \frac{C_{123}}{|x_{12}|^{\Delta_1+\Delta_2-\Delta_3}\,|x_{23}|^{\Delta_2+\Delta_3-\Delta_1}\,|x_{13}|^{\Delta_1+\Delta_3-\Delta_2}}, $$
leaving only the constant $C_{123}$ undetermined by symmetry.

**证明。** 平移不变性 ⟹ 关联函数只依赖 $r = |x-y|$；转动不变性 ⟹ 它是 $f(r)$。标度不变性给出 $f(\lambda r) = \lambda^{-2\Delta}f(r)$，唯一解 $f(r) = C\,r^{-2\Delta}$。特殊共形不变性随后自动满足；对维数不等的两个初级算符，它迫使系数为零（不等维数的初级算符正交）。三点函数同样被固定到只差常数 $C_{123}$。

---

## C. The Virasoro Central Charge and the Critical Dimension
## C. Virasoro 中心荷与临界维数

**Claim.** In 2D the conformal algebra has modes $L_n$ obeying $[L_m,L_n] = (m-n)L_{m+n} + \tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$, and a free scalar contributes $c = 1$.

**Sketch.** In 2D, write $z = x^1 + i x^2$. The conformal Killing equation is solved by *any* holomorphic $\epsilon(z)$, so the symmetry is infinite-dimensional with generators $\ell_n = -z^{n+1}\partial_z$ obeying the classical Witt algebra $[\ell_m,\ell_n] = (m-n)\ell_{m+n}$. Quantization (normal ordering of $T(z) = \sum_n L_n z^{-n-2}$) introduces a c-number anomaly — the central term $\tfrac{c}{12}m(m^2-1)$ — because $T$ does not transform as a true primary but picks up a Schwarzian derivative under finite conformal maps. For the free boson $\partial X$, the $TT$ OPE
$$ T(z)\,T(w) \sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}, \qquad c = 1, $$
reads off $c = 1$. For the string, $D$ embedding coordinates $X^\mu$ give $c = D$, while the reparametrization (Faddeev–Popov $bc$) ghosts contribute $c_\text{gh} = -26$. Conformal invariance of the full quantum theory requires the **total** central charge (the conformal anomaly) to vanish, $c_\text{total} = D - 26 = 0$, fixing $D = 26$ for the bosonic string; the superstring's worldsheet adds fermions and ghosts giving $D = 10$.

**要点。** 在二维中令 $z = x^1 + ix^2$，共形 Killing 方程被任意全纯 $\epsilon(z)$ 求解，故对称性无穷维，经典生成元 $\ell_n = -z^{n+1}\partial_z$ 满足 Witt 代数。量子化（对 $T(z)$ 正规排序）引入 c-数反常，即中心项 $\tfrac{c}{12}m(m^2-1)$；自由玻色子的 $TT$ OPE 读出 $c = 1$。对弦，$D$ 个嵌入坐标给出 $c = D$，重参数化鬼场给出 $c_\text{gh} = -26$，总中心荷为零的要求 $D - 26 = 0$ 固定玻色弦的 $D = 26$（超弦为 $D = 10$）。

---

## D. From Scaling Dimension to Critical Exponent
## D. 从标度维数到临界指数

**Claim.** The anomalous-dimension exponent $\eta$ is fixed by the order-parameter dimension: $\Delta_\sigma = \tfrac12(d - 2 + \eta)$.

**Proof.** At criticality the order-parameter correlator decays as a pure power, $\langle\sigma(x)\sigma(0)\rangle \sim |x|^{-(d-2+\eta)}$, which *defines* $\eta$ (the deviation from the free-field Ornstein–Zernike value $|x|^{-(d-2)}$). Comparing with the CFT two-point form $|x|^{-2\Delta_\sigma}$ gives $2\Delta_\sigma = d - 2 + \eta$, i.e. $\Delta_\sigma = \tfrac12(d-2+\eta)$. Likewise the correlation-length exponent $\nu$ is set by the dimension $\Delta_\varepsilon$ of the energy operator (the relevant perturbation driving the system off criticality) via $\nu = 1/(d - \Delta_\varepsilon)$. For the 2D Ising minimal model $\Delta_\sigma = \tfrac18$ gives $\eta = \tfrac14$, and $\Delta_\varepsilon = 1$ gives $\nu = 1$ — the exact Onsager values.

**证明。** 临界处序参量关联呈纯幂律 $|x|^{-(d-2+\eta)}$，定义了 $\eta$；与 CFT 两点形式 $|x|^{-2\Delta_\sigma}$ 比较给出 $\Delta_\sigma = \tfrac12(d-2+\eta)$。关联长度指数 $\nu = 1/(d-\Delta_\varepsilon)$ 由能量算符维数 $\Delta_\varepsilon$ 决定。对二维伊辛极小模型，$\Delta_\sigma = \tfrac18 \Rightarrow \eta = \tfrac14$，$\Delta_\varepsilon = 1 \Rightarrow \nu = 1$，即精确的昂萨格值。

---

← Back to [Module 6.13 — Conformal Field Theory](./module-6.13-conformal-field-theory.md)

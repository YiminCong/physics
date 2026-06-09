# Derivations — Module 6.8: Scattering, the S-Matrix & LSZ Reduction
# 推导 — 模块 6.8：散射、S 矩阵与 LSZ 约化

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.8](./module-6.8-scattering-s-matrix-and-lsz.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 6.8](./module-6.8-scattering-s-matrix-and-lsz.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. $S = 1 + iT$ and the Definition of the Invariant Amplitude $\mathcal{M}$

**Claim.** The S-matrix can be written $S = 1 + iT$, where $T$ carries all non-trivial scattering. By Lorentz invariance and four-momentum conservation the T-matrix elements factor as $\langle f|iT|i\rangle = (2\pi)^4\, \delta^4(p_f - p_i) \cdot i\mathcal{M}(i\to f)$, where $\mathcal{M}$ is the **Lorentz-invariant amplitude**.

**命题。** S 矩阵可写成 $S = 1 + iT$，其中 $T$ 包含所有非平庸散射。由洛伦兹不变性与四动量守恒，T 矩阵元分解为 $\langle f|iT|i\rangle = (2\pi)^4\, \delta^4(p_f - p_i) \cdot i\mathcal{M}(i\to f)$，其中 $\mathcal{M}$ 是**洛伦兹不变振幅**。

**Step 1 — Unitarity decomposition.** The S-matrix is unitary: $S^\dagger S = S S^\dagger = 1$. Write $S = 1 + iT$ (the $1$ represents no-interaction forward scattering of distinct free-particle states). Then

**第 1 步 — 幺正分解。** S 矩阵是幺正的：$S^\dagger S = S S^\dagger = 1$。写 $S = 1 + iT$（其中 $1$ 表示不同自由粒子态之间无相互作用的前向散射）。则

$$ S^\dagger S = (1 - iT^\dagger)(1 + iT) = 1 + i(T - T^\dagger) + T^\dagger T = 1. $$

Hence $i(T - T^\dagger) = -T^\dagger T$, or equivalently $i(T^\dagger - T) = T^\dagger T$. This is the **optical theorem in operator form**, to be exploited in Section D below.

故 $i(T - T^\dagger) = -T^\dagger T$，即 $i(T^\dagger - T) = T^\dagger T$。这是**算符形式的光学定理**，将在下文 D 节中加以利用。

**Step 2 — Factoring out momentum conservation.** In a translationally invariant theory the Hamiltonian commutes with the total momentum operator: $[P^\mu, H] = 0$. Consequently, if we denote in- and out-states by their momenta, the full S-matrix element $\langle f|S|i\rangle$ is zero unless the total four-momentum is conserved. We therefore write

**第 2 步 — 提取动量守恒。** 在平移不变的理论中，哈密顿量与总动量算符对易：$[P^\mu, H] = 0$。因此，若用动量标记入态和出态，则全 S 矩阵元 $\langle f|S|i\rangle$ 在总四动量不守恒时为零。从而写

$$ \langle f|iT|i\rangle = (2\pi)^4\, \delta^4\Big(\textstyle\sum p_f - \sum p_i\Big) \cdot i\mathcal{M}(i\to f). $$

The factor $(2\pi)^4$ is conventional (matching the Fourier-transform normalization of the propagators in Module 6.3). The remaining quantity $i\mathcal{M}$ is by construction Lorentz invariant and free of the trivial kinematic delta function; it is the object computed by Feynman diagrams.

因子 $(2\pi)^4$ 是约定写法（与模块 6.3 中传播子的傅里叶变换归一化匹配）。剩余的量 $i\mathcal{M}$ 在构造上是洛伦兹不变的，且不含平庸的运动学 delta 函数；这正是费曼图所计算的对象。

**Step 3 — Normalization of states.** We use relativistically normalized single-particle states: $\langle p'|p\rangle = (2\pi)^3\, 2E_p\, \delta^3(p' - p)$. The corresponding completeness relation (resolution of the identity) for a single species is

**第 3 步 — 态的归一化。** 我们使用相对论归一化的单粒子态：$\langle p'|p\rangle = (2\pi)^3\, 2E_p\, \delta^3(p' - p)$。对应的单粒子完备性关系（单位分解）为

$$ 1 = \int \frac{d^3p}{(2\pi)^3\, 2E_p}\, |p\rangle\langle p|. $$

With this normalization, the identity operator in the vacuum and one-particle sectors is explicit. Multi-particle states are products. The relative factor of $2E_p$ between the covariant and non-covariant normalizations is responsible for the flux factors in cross-section formulae (Section B).

在此归一化下，真空和单粒子扇区的单位算符是显式的。多粒子态是乘积态。协变归一化与非协变归一化之间的相对因子 $2E_p$ 正是截面公式中通量因子的来源（B 节）。 $\blacksquare$

---

## B. $|\mathcal{M}|^2 \to$ Differential Cross Section $d\sigma$ and Decay Rate $d\Gamma$

**Claim.** For a $2\to n$ process in the centre-of-mass frame, $d\sigma = (1/F)|\mathcal{M}|^2\, d\Phi_n$, where $F = 4E_1 E_2 |v_1 - v_2|$ is the Møller flux factor and $d\Phi_n$ is the Lorentz-invariant $n$-body phase space. For a $1\to n$ decay, $d\Gamma = (1/2M)|\mathcal{M}|^2\, d\Phi_n$.

**命题。** 对质心系中的 $2\to n$ 过程，$d\sigma = (1/F)|\mathcal{M}|^2\, d\Phi_n$，其中 $F = 4E_1 E_2 |v_1 - v_2|$ 为莫勒通量因子，$d\Phi_n$ 为洛伦兹不变的 $n$ 体相空间。对 $1\to n$ 衰变，$d\Gamma = (1/2M)|\mathcal{M}|^2\, d\Phi_n$。

**Step 1 — Transition rate from Fermi's Golden Rule.** Working in a large box of volume $V$ and time interval $T$, the S-matrix element for $f \ne i$ is

**第 1 步 — 从费米黄金规则得到跃迁率。** 在体积为 $V$、时间间隔为 $T$ 的大盒子中，$f \ne i$ 时的 S 矩阵元为

$$ S_{fi} = (2\pi)^4\, \delta^4(p_f - p_i) \cdot i\mathcal{M}. $$

The transition probability per unit time and volume is $|S_{fi}|^2/(VT)$. The square of the delta function is handled by the replacement $(2\pi)^4\, \delta^4(0) \to VT$, valid for large $VT$. Hence

单位时间、单位体积的跃迁概率为 $|S_{fi}|^2/(VT)$。delta 函数的平方用大 $VT$ 下的替换 $(2\pi)^4\, \delta^4(0) \to VT$ 处理。故

$$ \frac{dP}{dT} = (2\pi)^4\, \delta^4\Big(\textstyle\sum p_f - \sum p_i\Big) \cdot |\mathcal{M}|^2 \cdot \prod_f \frac{V\, d^3p_f}{(2\pi)^3}. $$

(The factor $1/(2E)$ per final particle from the relativistic normalization cancels against the $2E$ in the phase-space measure when assembling the Lorentz-invariant phase space element below.)

（每个末态粒子相对论归一化带来的 $1/(2E)$ 因子，在组装下面的洛伦兹不变相空间元时与相空间测度中的 $2E$ 相消。）

**Step 2 — Lorentz-invariant phase space.** Define the $n$-body LIPS (Lorentz-Invariant Phase Space):

**第 2 步 — 洛伦兹不变相空间。** 定义 $n$ 体 LIPS（洛伦兹不变相空间）：

$$ d\Phi_n(P; p_1,\ldots,p_n) = (2\pi)^4\, \delta^4\Big(P - \textstyle\sum_f p_f\Big) \prod_{f=1}^{n} \frac{d^3p_f}{(2\pi)^3\, 2E_f}. $$

Each factor $d^3p_f / ((2\pi)^3\, 2E_f) = d^4p_f / (2\pi)^3 \cdot \delta(p_f^2 - m_f^2)\, \theta(E_f)$ is manifestly Lorentz invariant. In terms of $d\Phi_n$:

每个因子 $d^3p_f / ((2\pi)^3\, 2E_f) = d^4p_f / (2\pi)^3 \cdot \delta(p_f^2 - m_f^2)\, \theta(E_f)$ 是显式洛伦兹不变的。用 $d\Phi_n$ 表示：

$$ \frac{dP}{dT} = |\mathcal{M}|^2\, d\Phi_n. $$

**Step 3 — Flux factor for $2\to n$ scattering.** For two incoming particles (1, 2) in any frame, the flux (number of particles crossing unit area per unit time per unit volume) is

**第 3 步 — $2\to n$ 散射的通量因子。** 对任意参考系中的两个入射粒子 (1, 2)，通量（单位体积、单位面积、单位时间内穿过的粒子数）为

$$ F = 4\, [(p_1\cdot p_2)^2 - m_1^2 m_2^2]^{1/2}. $$

In the CM frame with collinear momenta this reduces to $F = 4E_1 E_2 |v_1 - v_2| = 4|p_{\rm cm}|\sqrt{s}$ (where $\sqrt{s} = E_{\rm cm}$). $F$ is Lorentz-invariant under boosts along the beam axis. The cross section is

在质心系中，对共线动量，此式化为 $F = 4E_1 E_2 |v_1 - v_2| = 4|p_{\rm cm}|\sqrt{s}$（其中 $\sqrt{s} = E_{\rm cm}$）。$F$ 在沿束流方向的洛伦兹变换下不变。截面为

$$ d\sigma = \frac{1}{F}\, |\mathcal{M}|^2\, d\Phi_n. $$

**Step 4 — Decay rate for $1\to n$.** For a single parent particle of mass $M$ at rest ($E = M$), there is no flux factor — the "beam" is one particle per unit volume — so the denominator is simply the relativistic normalization factor $2M$ of the initial state. Hence

**第 4 步 — $1\to n$ 衰变率。** 对静止的质量为 $M$ 的单个母粒子 ($E = M$)，不存在通量因子——"束流"是单位体积内一个粒子——故分母仅为初态的相对论归一化因子 $2M$。因此

$$ d\Gamma = \frac{1}{2M}\, |\mathcal{M}|^2\, d\Phi_n. $$

**Step 5 — Two-body phase space in the CM frame (worked example).** For $n = 2$ with equal masses $m$ in the CM frame, $d\Phi_2 = |p_f|\, d\Omega / (16\pi^2 \sqrt{s})$. Hence $d\sigma/d\Omega = |\mathcal{M}|^2/(64\pi^2 s) \cdot |p_f|/|p_i|$, where $p_i$ and $p_f$ are CM momenta of initial and final states. This is the standard $2\to 2$ formula used in Module 6.3 for tree-level cross sections. $\blacksquare$

**第 5 步 — CM 系中的二体相空间（示例）。** 对 $n = 2$、CM 系中等质量 $m$ 的情形，$d\Phi_2 = |p_f|\, d\Omega / (16\pi^2 \sqrt{s})$。故 $d\sigma/d\Omega = |\mathcal{M}|^2/(64\pi^2 s) \cdot |p_f|/|p_i|$，其中 $p_i$ 和 $p_f$ 分别为初末态的质心系动量。这是模块 6.3 中树图截面所用的标准 $2\to 2$ 公式。$\blacksquare$

---

## C. Mandelstam Variables and the Constraint $s + t + u = \sum m_i^2$

**Claim.** For the $2\to 2$ process $1+2\to 3+4$, define $s = (p_1+p_2)^2$, $t = (p_1-p_3)^2$, $u = (p_1-p_4)^2$. These three invariants satisfy $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$.

**命题。** 对 $2\to 2$ 过程 $1+2\to 3+4$，定义 $s = (p_1+p_2)^2$，$t = (p_1-p_3)^2$，$u = (p_1-p_4)^2$。这三个不变量满足 $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$。

**Step 1 — Expand each invariant.** Expand in Minkowski metric $(+,-,-,-)$:

**第 1 步 — 展开每个不变量。** 在闵可夫斯基度规 $(+,-,-,-)$ 下展开：

$$ \begin{aligned}
s &= (p_1+p_2)^2 = p_1^2 + 2p_1\cdot p_2 + p_2^2 = m_1^2 + 2p_1\cdot p_2 + m_2^2, \\
t &= (p_1-p_3)^2 = p_1^2 - 2p_1\cdot p_3 + p_3^2 = m_1^2 - 2p_1\cdot p_3 + m_3^2, \\
u &= (p_1-p_4)^2 = p_1^2 - 2p_1\cdot p_4 + p_4^2 = m_1^2 - 2p_1\cdot p_4 + m_4^2.
\end{aligned} $$

where we used $p_i^2 = m_i^2$ (on-shell, in the sense of asymptotic states whose mass is the physical pole mass).

其中用到了 $p_i^2 = m_i^2$（在壳，即渐近态的质量为物理极点质量）。

**Step 2 — Sum.** Adding the three expressions:

**第 2 步 — 求和。** 将三式相加：

$$ s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 + 2p_1\cdot(p_2 - p_3 - p_4). $$

**Step 3 — Apply momentum conservation.** Four-momentum conservation gives $p_1 + p_2 = p_3 + p_4$, so $p_2 - p_3 - p_4 = -p_1$. Therefore

**第 3 步 — 应用动量守恒。** 四动量守恒给出 $p_1 + p_2 = p_3 + p_4$，故 $p_2 - p_3 - p_4 = -p_1$。因此

$$ 2p_1\cdot(p_2 - p_3 - p_4) = 2p_1\cdot(-p_1) = -2p_1^2 = -2m_1^2. $$

**Step 4 — Conclude.** Substituting back:

**第 4 步 — 结论。** 代回：

$$ \boxed{\, s + t + u = 3m_1^2 + m_2^2 + m_3^2 + m_4^2 - 2m_1^2 = m_1^2 + m_2^2 + m_3^2 + m_4^2 \,} \qquad \blacksquare $$

This is the advertised identity. The three variables $(s, t, u)$ are not independent — they lie on a plane in three-dimensional invariant space. For equal masses $m$, the constraint reads $s + t + u = 4m^2$. The physical regions of the $s$-, $t$-, and $u$-channels correspond to different corners of the Mandelstam plane, related by crossing symmetry (exchanging particle labels). $\blacksquare$

这正是所述等式。三个变量 $(s, t, u)$ 并不独立——它们位于三维不变量空间中的一个平面上。对等质量 $m$，约束为 $s + t + u = 4m^2$。$s$、$t$、$u$ 道的物理区域对应于曼德尔斯坦平面的不同角落，通过交叉对称性（互换粒子标记）相互联系。$\blacksquare$

---

## D. The Optical Theorem from Unitarity $S^\dagger S = 1$

**Claim.** Unitarity implies $2\, \mathrm{Im}\, \mathcal{M}(i\to i, \text{forward}) = \sum_X \int d\Pi_X\, |\mathcal{M}(i\to X)|^2$, where the sum runs over all accessible intermediate states $X$ and $d\Pi_X$ is their Lorentz-invariant phase space.

**命题。** 幺正性蕴含 $2\, \mathrm{Im}\, \mathcal{M}(i\to i, \text{前向}) = \sum_X \int d\Pi_X\, |\mathcal{M}(i\to X)|^2$，其中求和遍历所有可及中间态 $X$，$d\Pi_X$ 为其洛伦兹不变相空间。

**Step 1 — Operator identity from $S^\dagger S = 1$.** From Step 1 of Section A, $S = 1 + iT$ gives

**第 1 步 — 由 $S^\dagger S = 1$ 得算符恒等式。** 由 A 节第 1 步，$S = 1 + iT$ 给出

$$ S^\dagger S = 1 \implies i(T^\dagger - T) = T^\dagger T. $$

Take the matrix element of this identity between two copies of the initial state $|i\rangle$:

对初态 $|i\rangle$ 取此恒等式的矩阵元：

$$ i\, \langle i|T^\dagger - T|i\rangle = \langle i|T^\dagger T|i\rangle. $$

**Step 2 — Left side.** The left side involves

**第 2 步 — 左边。** 左边包含

$$ \langle i|T^\dagger|i\rangle = (\langle i|T|i\rangle)^* = \mathcal{M}^*(i\to i) \quad (\text{up to the } (2\pi)^4\delta^4 \text{ factor, which equals } (2\pi)^4\delta^4(0) = VT \text{ for forward scattering in large-volume normalization}). $$

$$ \langle i|T^\dagger|i\rangle = (\langle i|T|i\rangle)^* = \mathcal{M}^*(i\to i) \quad (\text{不计 } (2\pi)^4\delta^4 \text{ 因子，在大体积归一化下前向散射时 } (2\pi)^4\delta^4(0) = VT)\text{。} $$

Therefore the left side is $i(\mathcal{M}^* - \mathcal{M}) \cdot (2\pi)^4\delta^4(0) = 2\, \mathrm{Im}\, \mathcal{M}(i\to i, \text{forward}) \cdot (2\pi)^4\delta^4(0)$.

因此左边为 $i(\mathcal{M}^* - \mathcal{M}) \cdot (2\pi)^4\delta^4(0) = 2\, \mathrm{Im}\, \mathcal{M}(i\to i, \text{前向}) \cdot (2\pi)^4\delta^4(0)$。

**Step 3 — Right side: insert a complete set of states.** Insert $1 = \sum_X \int d\Pi_X\, |X\rangle\langle X|$ (summing over all multi-particle states $X$, with Lorentz-invariant measure $d\Pi_X$):

**第 3 步 — 右边：插入完备态。** 插入 $1 = \sum_X \int d\Pi_X\, |X\rangle\langle X|$（对所有多粒子态 $X$ 求和，采用洛伦兹不变测度 $d\Pi_X$）：

$$ \langle i|T^\dagger T|i\rangle = \sum_X \int d\Pi_X\, \langle i|T^\dagger|X\rangle\langle X|T|i\rangle = \sum_X \int d\Pi_X\, |\langle X|T|i\rangle|^2. $$

Stripping the $(2\pi)^4\delta^4$ factor as before, $\langle X|T|i\rangle = (2\pi)^4\delta^4(p_X - p_i) \cdot \mathcal{M}(i\to X)$, so

提取 $(2\pi)^4\delta^4$ 因子后，$\langle X|T|i\rangle = (2\pi)^4\delta^4(p_X - p_i) \cdot \mathcal{M}(i\to X)$，故

$$ \langle i|T^\dagger T|i\rangle = (2\pi)^4\delta^4(0) \cdot \sum_X \int d\Pi_X\, |\mathcal{M}(i\to X)|^2. $$

**Step 4 — Equate and cancel the common factor.** Equating Steps 2 and 3 and cancelling the common factor of $(2\pi)^4\delta^4(0)$:

**第 4 步 — 等式两边相等并消去公因子。** 将第 2、3 步等式相等，消去公因子 $(2\pi)^4\delta^4(0)$：

$$ 2\, \mathrm{Im}\, \mathcal{M}(i\to i, \text{forward}) = \sum_X \int d\Pi_X\, |\mathcal{M}(i\to X)|^2. $$

**Step 5 — Relation to the total cross section.** The right side is precisely the quantity that, after dividing by the flux $F$, gives the total cross section $\sigma_{\rm tot} = \sum_X \sigma(i\to X)$. Hence

**第 5 步 — 与总截面的关系。** 右边除以通量 $F$ 后正是总截面 $\sigma_{\rm tot} = \sum_X \sigma(i\to X)$。故

$$ \mathrm{Im}\, \mathcal{M}(i\to i, \text{forward}) = F \cdot \sigma_{\rm tot} / 2 = 2E_{\rm cm}\, |p_{\rm cm}|\, \sigma_{\rm tot} \quad (\text{in CM frame}). $$

This is the standard form of the **optical theorem**: the imaginary part of the forward elastic amplitude equals (flux/2) times the total cross section. Intuitively, the probability removed from the forward beam by absorption (all inelastic processes) must equal the imaginary part of the forward amplitude by probability conservation — a direct consequence of unitarity. $\blacksquare$

这是**光学定理**的标准形式：前向弹性振幅的虚部等于（通量/2）乘以总截面。直觉上，由吸收（所有非弹性过程）从前向束中移走的概率必须等于前向振幅的虚部，这是概率守恒——即幺正性——的直接结果。$\blacksquare$

---

## E. The LSZ Reduction Formula

**Claim (scalar field theory).** Let $\varphi(x)$ be a scalar field with physical mass $m$ and field-strength renormalization $Z$ (so that $\langle 0|\varphi(x)|p\rangle = \sqrt{Z}\, e^{ip\cdot x}$). The S-matrix element for $n$ incoming particles (momenta $p_1,\ldots,p_n$) and $m$ outgoing particles (momenta $k_1,\ldots,k_m$) is given by the **LSZ formula**:

**命题（标量场论）。** 设 $\varphi(x)$ 为物理质量为 $m$、场强重整化为 $Z$ 的标量场（使得 $\langle 0|\varphi(x)|p\rangle = \sqrt{Z}\, e^{ip\cdot x}$）。$n$ 个入射粒子（动量 $p_1,\ldots,p_n$）与 $m$ 个出射粒子（动量 $k_1,\ldots,k_m$）的 S 矩阵元由 **LSZ 公式**给出：

$$ \langle k_1\ldots k_m, \text{out}|p_1\ldots p_n, \text{in}\rangle = \prod_{j=1}^{n} \frac{i(p_j^2-m^2)}{\sqrt{Z}} \cdot \prod_{l=1}^{m} \frac{i(k_l^2-m^2)}{\sqrt{Z}} \cdot \tilde G^{(n+m)}(p_1,\ldots,p_n, -k_1,\ldots,-k_m)\Big|_{\text{all legs on-shell}}, $$

where $\tilde G^{(N)}(q_1,\ldots,q_N) = \int d^4x_1\ldots d^4x_N\, e^{i(q_1\cdot x_1+\ldots+q_N\cdot x_N)}\, \langle 0|T\, \varphi(x_1)\ldots\varphi(x_N)|0\rangle$ is the full $N$-point momentum-space Green's function of the interacting theory (including all loops and self-energy corrections), and the on-shell limit $p_j^2\to m^2$, $k_l^2\to m^2$ is taken.

其中 $\tilde G^{(N)}(q_1,\ldots,q_N) = \int d^4x_1\ldots d^4x_N\, e^{i(q_1\cdot x_1+\ldots+q_N\cdot x_N)}\, \langle 0|T\, \varphi(x_1)\ldots\varphi(x_N)|0\rangle$ 是相互作用理论中完整的 $N$ 点动量空间格林函数（包含所有圈图和自能修正），并取在壳极限 $p_j^2\to m^2$，$k_l^2\to m^2$。

**Step 1 — The interacting single-particle pole.** The exact propagator of the interacting theory is

**第 1 步 — 相互作用理论的单粒子极点。** 相互作用理论的精确传播子为

$$ \tilde G^{(2)}(p) = \int d^4x\, e^{ip\cdot x}\, \langle 0|T\, \varphi(x)\, \varphi(0)|0\rangle. $$

By the **Källén–Lehmann spectral representation** (derived by inserting a complete set of states between the two fields), this has the form

由**凯伦–莱曼谱表示**（在两个场之间插入完备态集得到），其形式为

$$ \tilde G^{(2)}(p) = \frac{Z}{p^2 - m^2 + i\varepsilon} + (\text{terms regular at } p^2 = m^2 \text{ and multi-particle continuum contributions for } p^2 \ge (2m)^2). $$

The residue at the physical single-particle pole $p^2 = m^2$ is exactly $Z$; the bare-field contribution to this residue is $1$, so the renormalization constant $Z \le 1$ ($Z = 1$ in a free theory). The physical mass $m$ is the true pole of $\tilde G^{(2)}$, shifted from the bare mass $m_0$ by self-energy corrections.

物理单粒子极点 $p^2 = m^2$ 处的留数恰好是 $Z$；裸场对此留数的贡献为 $1$，故重整化常数 $Z \le 1$（自由理论中 $Z = 1$）。物理质量 $m$ 是 $\tilde G^{(2)}$ 的真实极点，由自能修正从裸质量 $m_0$ 移位而来。

**Step 2 — Derivation of the one-leg reduction.** We want to relate the in-state creation operators to the field $\varphi$. The **in-field** $\varphi_{\rm in}(x)$ is the free field that $\varphi(x)$ asymptotically approaches for $t\to-\infty$ (in the weak sense on matrix elements); it creates/annihilates physical one-particle states. We have the asymptotic relation

**第 2 步 — 单腿约化的推导。** 我们希望把入态产生算符与场 $\varphi$ 联系起来。**入场** $\varphi_{\rm in}(x)$ 是 $\varphi(x)$ 在 $t\to-\infty$ 时渐近趋近的自由场（在矩阵元的弱意义下）；它产生/湮灭物理单粒子态。我们有渐近关系

$$ \varphi(x) \to \sqrt{Z}\, \varphi_{\rm in}(x) \quad \text{as } t \to -\infty, \qquad \varphi(x) \to \sqrt{Z}\, \varphi_{\rm out}(x) \quad \text{as } t \to +\infty. $$

The factor $\sqrt{Z}$ is fixed by the normalization $\langle 0|\varphi(x)|p\rangle = \sqrt{Z}\, e^{ip\cdot x}$ (single-particle matrix element of the full field). A free scalar field satisfies $(\partial^2 + m^2)\varphi_{\rm in} = 0$ and its mode expansion gives the creation operator $a^\dagger_{\rm in}(p)$ by

因子 $\sqrt{Z}$ 由归一化条件 $\langle 0|\varphi(x)|p\rangle = \sqrt{Z}\, e^{ip\cdot x}$（完整场的单粒子矩阵元）确定。自由标量场满足 $(\partial^2 + m^2)\varphi_{\rm in} = 0$，其模展开通过以下方式给出产生算符 $a^\dagger_{\rm in}(p)$：

$$ a^\dagger_{\rm in}(p) = -i \int d^3x\, e^{-ip\cdot x}\, \overleftrightarrow{\partial_t}\, \varphi_{\rm in}(x), $$

where $f \overleftrightarrow{\partial_t} g = f(\partial_t g) - (\partial_t f)g$ is the Klein–Gordon inner-product operator (the expression is independent of $t$ for solutions of the KG equation).

其中 $f \overleftrightarrow{\partial_t} g = f(\partial_t g) - (\partial_t f)g$ 是克莱因–戈登内积算符（对 KG 方程的解，该表达式与 $t$ 无关）。

**Step 3 — Express the in-state as a limit.** An in-state with one incoming particle of momentum $p$ is $|p, \text{in}\rangle = a^\dagger_{\rm in}(p)|0\rangle$. Using the asymptotic relation and integrating by parts, one can replace $a^\dagger_{\rm in}(p)$ by an integral of $\varphi$:

**第 3 步 — 将入态表示为极限。** 动量为 $p$ 的单个入射粒子态为 $|p, \text{in}\rangle = a^\dagger_{\rm in}(p)|0\rangle$。利用渐近关系并分部积分，可将 $a^\dagger_{\rm in}(p)$ 替换为 $\varphi$ 的积分：

$$ a^\dagger_{\rm in}(p) = \lim_{t\to-\infty}\, \frac{-i}{\sqrt{Z}} \int d^3x\, e^{-ip\cdot x}\, \overleftrightarrow{\partial_t}\, \varphi(x). $$

Write this limit as a time integral of the time derivative: $\lim_{t\to-\infty} [\cdot] = [\cdot]\big|_{t=+\infty} - \int_{-\infty}^{+\infty} dt\, \partial_t [\cdot]$. The surface term at $+\infty$ gives the out-state operator, which will become the out-state creation operator in the amplitude. The bulk integral $\int dt\, \partial_t [e^{-ip\cdot x}\, \overleftrightarrow{\partial_t}\, \varphi]$ can be simplified by integration by parts:

将此极限写成对时间导数的时间积分：$\lim_{t\to-\infty} [\cdot] = [\cdot]\big|_{t=+\infty} - \int_{-\infty}^{+\infty} dt\, \partial_t [\cdot]$。$+\infty$ 处的面项给出出态算符，它在振幅中成为出态产生算符。体积分 $\int dt\, \partial_t [e^{-ip\cdot x}\, \overleftrightarrow{\partial_t}\, \varphi]$ 通过分部积分化简：

$$ \begin{aligned}
\partial_t [e^{-ip\cdot x}\, \overleftrightarrow{\partial_t}\, \varphi] &= e^{-ip\cdot x}(\partial_t^2 \varphi) - (\partial_t^2 e^{-ip\cdot x})\, \varphi \\
&= e^{-ip\cdot x}[(\partial_t^2 - \nabla^2 + m^2)\varphi] - \varphi[(\partial_t^2 - \nabla^2 + m^2)e^{-ip\cdot x}] \\
&= e^{-ip\cdot x}\, [(\Box + m^2)\, \varphi],
\end{aligned} $$

(after adding and subtracting $\nabla^2$ and $m^2$ terms, using $\nabla^2 e^{-ip\cdot x} = -|p|^2\, e^{-ip\cdot x}$ and $\partial_t^2 e^{-ip\cdot x} = -E_p^2\, e^{-ip\cdot x}$).

(Here we used that $e^{-ip\cdot x}$ satisfies $(\Box + m^2)e^{-ip\cdot x} = 0$ since $p^2 = E_p^2 - |p|^2 = m^2$.)

（此处用到 $e^{-ip\cdot x}$ 满足 $(\Box + m^2)e^{-ip\cdot x} = 0$，因为 $p^2 = E_p^2 - |p|^2 = m^2$。其中在加减 $\nabla^2$ 与 $m^2$ 项后，用到 $\nabla^2 e^{-ip\cdot x} = -|p|^2\, e^{-ip\cdot x}$ 与 $\partial_t^2 e^{-ip\cdot x} = -E_p^2\, e^{-ip\cdot x}$。）

**Step 4 — The fully-reduced expression (one incoming leg).** Combining Steps 2 and 3 gives

**第 4 步 — 完全约化表达式（单个入射腿）。** 综合第 2、3 步得

$$ a^\dagger_{\rm in}(p) = \frac{i}{\sqrt{Z}} \int d^4x\, e^{-ip\cdot x}\, (\Box_x + m^2)\, \varphi(x) + (\text{out-state operator contribution}). $$

The "out-state operator" term — the boundary term at $t = +\infty$ — gives zero when acting to the right on the vacuum $|0\rangle$ (since there are no out-state particles in the vacuum). Thus for a matrix element with one incoming particle:

"出态算符"项——$t = +\infty$ 处的边界项——作用在真空态 $|0\rangle$ 右侧时为零（因为真空中没有出态粒子）。因此对含一个入射粒子的矩阵元：

$$ \langle f, \text{out}|p, \text{in}\rangle = \frac{i}{\sqrt{Z}} \int d^4x\, e^{-ip\cdot x}\, (\Box_x + m^2)\, \langle f, \text{out}|T\, \varphi(x)\, \ldots|0\rangle. $$

The operator $(\Box_x + m^2)$ acting on a momentum-space Green's function $\tilde G(p,\ldots)$ gives a factor $-(p^2-m^2)$ (since $\Box_x e^{ip\cdot x} = -p^2 e^{ip\cdot x}$ in Fourier space). We arrive at

算符 $(\Box_x + m^2)$ 作用于动量空间格林函数 $\tilde G(p,\ldots)$ 给出因子 $-(p^2-m^2)$（因为在傅里叶空间中 $\Box_x e^{ip\cdot x} = -p^2 e^{ip\cdot x}$）。我们得到

Combined with the explicit factor of $i$ from the LSZ formula, the contribution per incoming leg is

加上 LSZ 公式中的显式因子 $i$，每条入射腿的贡献为

$$ i \cdot (-(p^2 - m^2)) / \sqrt{Z} = -i(p^2 - m^2) / \sqrt{Z}. $$

As $p^2\to m^2$, the full propagator $\tilde G^{(2)}(p) \approx iZ/(p^2-m^2+i\varepsilon)$, so the product $[-i(p^2-m^2)/\sqrt{Z}] \cdot [iZ/(p^2-m^2)] = Z/\sqrt{Z} = \sqrt{Z}$ is finite and non-zero. This is the **amputation**: the external propagator $1/(p^2-m^2)$ from the full Green's function is cancelled by the factor $(p^2-m^2)$ from the LSZ reduction, leaving a finite residue $\sqrt{Z}$ per external leg.

当 $p^2\to m^2$ 时，完整传播子 $\tilde G^{(2)}(p) \approx iZ/(p^2-m^2+i\varepsilon)$，故乘积 $[-i(p^2-m^2)/\sqrt{Z}] \cdot [iZ/(p^2-m^2)] = Z/\sqrt{Z} = \sqrt{Z}$ 是有限非零的。这正是**截去（摊开）**：完整格林函数中外腿的传播子 $1/(p^2-m^2)$ 被 LSZ 约化中的因子 $(p^2-m^2)$ 消掉，每条外腿留下有限留数 $\sqrt{Z}$。

**Step 5 — Generalization to all legs and final formula.** Repeating the argument for each of the $n$ incoming and $m$ outgoing legs (for outgoing legs the momentum flows out, so the Fourier phase is $e^{+ik\cdot x}$ and the Klein–Gordon operator similarly gives $i(k^2-m^2)$):

**第 5 步 — 推广至所有外腿与最终公式。** 对 $n$ 条入射腿和 $m$ 条出射腿重复上述论证（出射腿的动量流出，傅里叶相位为 $e^{+ik\cdot x}$，克莱因–戈登算符类似地给出 $i(k^2-m^2)$）：

$$ \langle k_1\ldots k_m, \text{out}|p_1\ldots p_n, \text{in}\rangle = \prod_{j=1}^{n} \frac{i(p_j^2 - m^2)}{\sqrt{Z}} \cdot \prod_{l=1}^{m} \frac{i(k_l^2 - m^2)}{\sqrt{Z}} \cdot \tilde G^{(n+m)}(p_1,\ldots,p_n,-k_1,\ldots,-k_m). $$

The on-shell limit of each factor $i(p^2-m^2)/\sqrt{Z}$ times the corresponding external propagator $iZ/(p^2-m^2)$ gives $\sqrt{Z}$. The **amputated** Green's function $\tilde G_{\rm amp}$ is defined by stripping all $n+m$ external propagators from $\tilde G^{(n+m)}$: $\tilde G^{(n+m)} = \prod_j [iZ/(p_j^2-m^2)] \cdot \prod_l [iZ/(k_l^2-m^2)] \cdot \tilde G_{\rm amp}^{(n+m)}$. Substituting:

每个因子 $i(p^2-m^2)/\sqrt{Z}$ 乘以对应的外腿传播子 $iZ/(p^2-m^2)$ 的在壳极限给出 $\sqrt{Z}$。**截去的**格林函数 $\tilde G_{\rm amp}$ 的定义是从 $\tilde G^{(n+m)}$ 中剥去所有 $n+m$ 条外腿传播子：$\tilde G^{(n+m)} = \prod_j [iZ/(p_j^2-m^2)] \cdot \prod_l [iZ/(k_l^2-m^2)] \cdot \tilde G_{\rm amp}^{(n+m)}$。代入：

$$ \boxed{\, \langle k_1\ldots k_m, \text{out}|p_1\ldots p_n, \text{in}\rangle = (\sqrt{Z})^{n+m} \cdot \tilde G_{\rm amp}^{(n+m)}(\text{on-shell}) \,} \qquad \blacksquare $$

In perturbation theory $Z = 1 + O(\hbar)$ (loop corrections), so at tree level $\tilde G_{\rm amp}$ reduces to the sum of all connected, amputated Feynman diagrams, which is precisely the $i\mathcal{M}$ of the Feynman rules (Module 6.3). Beyond tree level, each external leg picks up a factor of $\sqrt{Z}$ — the origin of wave-function renormalization. $\blacksquare$

在微扰论中 $Z = 1 + O(\hbar)$（圈图修正），故在树图阶 $\tilde G_{\rm amp}$ 化为所有连通截去费曼图之和，这正是模块 6.3 费曼规则中的 $i\mathcal{M}$。超出树图阶，每条外腿获得一个 $\sqrt{Z}$ 因子——这正是波函数重整化的起源。$\blacksquare$

---

*Every calculation in QFT connects back to these five results. The S-matrix is unitary; $\mathcal{M}$ is its kinematic skeleton; cross sections and decay rates are its modulus squared weighted by phase space; the Mandelstam variables parameterize the kinematics; the optical theorem is unitarity made explicit; and LSZ is the rigorous link between the correlators of the quantum field and the measurable amplitudes.*

*QFT 中的每一个计算都可追溯至这五个结果。S 矩阵是幺正的；$\mathcal{M}$ 是其运动学骨架；截面和衰变率是其模平方乘以相空间；曼德尔斯坦变量参数化运动学；光学定理是幺正性的显式表达；LSZ 是量子场的关联函数与可测量振幅之间的严格桥梁。*

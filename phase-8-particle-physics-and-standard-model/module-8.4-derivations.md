---
title: "Derivations — Module 8.4: Electroweak Theory & the Higgs"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 8.4: Electroweak Theory & the Higgs
# 推导 — 模块 8.4：电弱理论与希格斯机制

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 8.4](./module-8.4-electroweak-theory-and-higgs.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 8.4](./module-8.4-electroweak-theory-and-higgs.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. $SU(2)\times U(1)$ Gauge Fields and the Weinberg Angle · $SU(2)\times U(1)$ 规范场与温伯格角

**Claim.** The four gauge fields $W^{1,2,3}_\mu$ ($SU(2)_L$) and $B_\mu$ ($U(1)_Y$) mix to form the mass eigenstates $W^\pm_\mu$, $Z^0_\mu$, $A_\mu$ via the Weinberg angle $\theta_W$, with the electric charge satisfying $e = g\sin\theta_W = g'\cos\theta_W$.

**命题。** 四个规范场 $W^{1,2,3}_\mu$（$SU(2)_L$）和 $B_\mu$（$U(1)_Y$）通过温伯格角 $\theta_W$ 混合形成质量本征态 $W^\pm_\mu$、$Z^0_\mu$、$A_\mu$，电荷满足 $e = g\sin\theta_W = g'\cos\theta_W$。

**Step 1 — The gauge structure.** The electroweak gauge group is $SU(2)_L \times U(1)_Y$ with gauge fields $W^a_\mu$ ($a = 1,2,3$) for $SU(2)_L$ (coupling $g$) and $B_\mu$ for $U(1)_Y$ (coupling $g'$). The covariant derivative acting on a left-handed doublet $L = (\nu_L, e_L)$ with weak hypercharge $Y_L = -1/2$ is:

**第 1 步 — 规范结构。** 电弱规范群为 $SU(2)_L \times U(1)_Y$，规范场为 $SU(2)_L$ 的 $W^a_\mu$（$a = 1,2,3$，耦合常数 $g$）和 $U(1)_Y$ 的 $B_\mu$（耦合常数 $g'$）。作用于弱超荷 $Y_L = -1/2$ 的左手双重态 $L = (\nu_L, e_L)$ 的协变导数为：

$$ D_\mu L = (\partial_\mu - ig(\sigma^a/2)W^a_\mu - ig'Y_L B_\mu)L = (\partial_\mu - ig(\sigma^a/2)W^a_\mu + (ig'/2)B_\mu)L. $$

For right-handed singlets (e.g., $e_R$ with $Y = -1$): $D_\mu e_R = (\partial_\mu + ig'B_\mu)e_R$.

对于右手单态（例如 $Y = -1$ 的 $e_R$）：$D_\mu e_R = (\partial_\mu + ig'B_\mu)e_R$。

**Step 2 — Charged gauge bosons.** The charged vector bosons $W^\pm$ couple to the raising/lowering generators $T^\pm = (T^1 \pm iT^2)/\sqrt2 = (\sigma^1 \pm i\sigma^2)/(2\sqrt2)$. Explicitly:

**第 2 步 — 带电规范玻色子。** 带电矢量玻色子 $W^\pm$ 耦合于升/降算符 $T^\pm = (T^1 \pm iT^2)/\sqrt2 = (\sigma^1 \pm i\sigma^2)/(2\sqrt2)$。显式地：

$$ gW^a_\mu T^a = g[(W^1_\mu\sigma^1 + W^2_\mu\sigma^2)/2 + W^3_\mu\sigma^3/2]. $$

Define:

定义：

$$ W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt2. $$

Then:

则：

$$ g(W^1_\mu T^1 + W^2_\mu T^2) = (g/\sqrt2)[W^+_\mu T^+ + W^-_\mu T^-], $$

where $T^\pm = (\sigma^1 \pm i\sigma^2)/2$ are the SU(2) raising/lowering operators. These are the physical W boson fields.

其中 $T^\pm = (\sigma^1 \pm i\sigma^2)/2$ 是 SU(2) 升/降算符。这些是物理 W 玻色子场。

**Step 3 — Neutral gauge boson mixing.** The neutral sector involves $W^3_\mu$ and $B_\mu$. Define the rotation:

**第 3 步 — 中性规范玻色子混合。** 中性部分涉及 $W^3_\mu$ 和 $B_\mu$。定义旋转：

$$ \begin{aligned} Z_\mu &= W^3_\mu \cos\theta_W - B_\mu \sin\theta_W \quad \text{(massive } Z^0 \text{ boson),} \\ A_\mu &= W^3_\mu \sin\theta_W + B_\mu \cos\theta_W \quad \text{(massless photon).} \end{aligned} $$

This is an orthogonal rotation in $(W^3, B)$ space by angle $\theta_W$ (the Weinberg/weak mixing angle).

这是在 $(W^3, B)$ 空间中的正交旋转，旋转角为 $\theta_W$（温伯格/弱混合角）。

**Step 4 — Condition on the electric charge.** The electromagnetic coupling to the electron (charge $-e$) must emerge correctly. The electron's coupling to $W^3_\mu$ and $B_\mu$ (from the covariant derivative with $I^3 = -1/2$ for $e_L$ and $Y = -1/2$ for $L$):

**第 4 步 — 电荷条件。** 到电子的电磁耦合（电荷 $-e$）必须正确涌现。电子到 $W^3_\mu$ 和 $B_\mu$ 的耦合（来自协变导数，$e_L$ 的 $I^3 = -1/2$，$L$ 的 $Y = -1/2$）：

$$ \begin{aligned} &\text{Coupling of } e_L \text{ to } W^3_\mu: \quad gI^3 = g\cdot(-1/2) = -g/2 \quad \text{(from the covariant-derivative term } gI^3 W^3_\mu, \text{ with } I^3 = -1/2 \text{ for } e_L\text{).} \\ &\text{Coupling of } e_L \text{ to } B_\mu: \quad g'Y = g'\cdot(-1/2) = -g'/2. \end{aligned} $$

In the rotated $(A, Z)$ basis, the photon $A_\mu = W^3_\mu\sin\theta_W + B_\mu\cos\theta_W$ couples to $e_L$ with:

在旋转的 $(A, Z)$ 基中，光子 $A_\mu = W^3_\mu\sin\theta_W + B_\mu\cos\theta_W$ 与 $e_L$ 的耦合为：

$$ e_L \text{ coupling to } A_\mu = (gI^3)\sin\theta_W + (g'Y)\cos\theta_W = -(g/2)\sin\theta_W - (g'/2)\cos\theta_W. $$

Requiring the photon to couple to every field as $eQ = e(I^3 + Y)$ (so that $e_L$, with $Q = -1$, has coupling $-e$), the $I^3$ and $Y$ pieces must match *separately* (not just their sum for $e_L$):

要求光子对每个场的耦合为 $eQ = e(I^3 + Y)$（使得 $Q = -1$ 的 $e_L$ 耦合为 $-e$），$I^3$ 与 $Y$ 两部分必须*分别*相等（而非仅对 $e_L$ 的和相等）：

$$ g\sin\theta_W = e \quad \text{(coefficient of } I^3\text{)}, \quad g'\cos\theta_W = e \quad \text{(coefficient of } Y\text{).} $$

But the electric charge is $Q = I^3 + Y$, so for $e_L$: $Q = -1/2 + (-1/2) = -1$. The photon coupling is:

但电荷为 $Q = I^3 + Y$，故对 $e_L$：$Q = -1/2 + (-1/2) = -1$。光子耦合为：

$$ e_L\text{–}A \text{ coupling} = (g\sin\theta_W)I^3 + (g'\cos\theta_W)Y = e(I^3 + Y) = eQ. $$

For this to work with $Q = I^3 + Y$ for all particles, we need:

为使此对所有粒子（$Q = I^3 + Y$）均成立，需要：

$$ \boxed{\, g\sin\theta_W = g'\cos\theta_W = e \,} $$

This is the fundamental relation of the electroweak theory. It determines $\theta_W$: $\tan\theta_W = g'/g$. $\blacksquare$

这是电弱理论的基本关系。它确定了 $\theta_W$：$\tan\theta_W = g'/g$。$\blacksquare$

---

## B. Higgs Potential, VEV, and Spontaneous Symmetry Breaking · 希格斯势、VEV 与自发对称性破缺

**Claim.** The Higgs potential $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$ (with $\mu^2 > 0$, $\lambda > 0$) has a minimum at $|\phi|^2 = v^2/2$ with $v = \sqrt{\mu^2/\lambda}$, and the vacuum $\langle\phi\rangle = (0, v/\sqrt2)$ spontaneously breaks $SU(2)_L \times U(1)_Y \to U(1)_\text{EM}$.

**命题。** 希格斯势 $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$（$\mu^2 > 0$，$\lambda > 0$）的极小值在 $|\phi|^2 = v^2/2$ 处，$v = \sqrt{\mu^2/\lambda}$，真空 $\langle\phi\rangle = (0, v/\sqrt2)$ 将 $SU(2)_L \times U(1)_Y$ 自发破缺至 $U(1)_\text{EM}$。

**Step 1 — Minimize the potential.** Writing $\rho = \phi^\dagger\phi \ge 0$:

**第 1 步 — 极小化势。** 令 $\rho = \phi^\dagger\phi \ge 0$：

$$ \begin{aligned} V &= -\mu^2\rho + \lambda\rho^2. \\ dV/d\rho &= -\mu^2 + 2\lambda\rho = 0 \implies \rho_\text{min} = \mu^2/(2\lambda). \\ d^2V/d\rho^2 &= 2\lambda > 0 \quad \text{(minimum, not maximum, since } \lambda > 0\text{).} \end{aligned} $$

So the minimum is at $\phi^\dagger\phi = \mu^2/(2\lambda) = v^2/2$, where $v \equiv \sqrt{\mu^2/\lambda}$.

故极小值在 $\phi^\dagger\phi = \mu^2/(2\lambda) = v^2/2$ 处，其中 $v \equiv \sqrt{\mu^2/\lambda}$。

**Step 2 — Degeneracy: the Mexican hat.** The condition $\phi^\dagger\phi = v^2/2$ defines a circle (or higher-dimensional sphere) of degenerate minima. The potential has a U(1)-symmetric "Mexican hat" shape: flat along the orbit of minima, with a curvature upward in the radial direction.

**第 2 步 — 简并性：墨西哥帽。** 条件 $\phi^\dagger\phi = v^2/2$ 定义了一个简并极小值的圆（或更高维球面）。势具有 U(1) 对称的"墨西哥帽"形状：沿极小值轨道方向平坦，在径向方向向上弯曲。

**Step 3 — Choosing the vacuum.** By $SU(2)_L \times U(1)_Y$ gauge freedom, we can always rotate $\phi$ so that:

**第 3 步 — 选择真空。** 利用 $SU(2)_L \times U(1)_Y$ 规范自由度，我们总可以将 $\phi$ 旋转至：

$$ \langle\phi\rangle = (0, v/\sqrt2), \quad \text{i.e., } \langle\phi^+\rangle = 0, \langle\phi^0\rangle = v/\sqrt2. $$

This choice preserves the $U(1)_\text{EM}$ symmetry: the generator $Q = I^3 + Y$ acting on $\langle\phi\rangle$ gives $Q\langle\phi\rangle = (I^3 + Y)\langle\phi\rangle = (-1/2 + 1/2)\langle\phi\rangle = 0$. So the photon remains massless.

这一选择保留了 $U(1)_\text{EM}$ 对称性：作用于 $\langle\phi\rangle$ 的生成元 $Q = I^3 + Y$ 给出 $Q\langle\phi\rangle = (I^3 + Y)\langle\phi\rangle = (-1/2 + 1/2)\langle\phi\rangle = 0$。故光子保持无质量。

The three generators that do NOT annihilate $\langle\phi\rangle$ are $T^1$, $T^2$, and $(T^3 - Y)$, corresponding to $W^1$, $W^2$, and $Z$ — these become massive.

不湮灭 $\langle\phi\rangle$ 的三个生成元是 $T^1$、$T^2$ 和 $(T^3 - Y)$，对应于 $W^1$、$W^2$ 和 $Z$——这些获得质量。

**Step 4 — Goldstone boson counting.** The original $SU(2)_L \times U(1)_Y$ has $3 + 1 = 4$ generators. The residual $U(1)_\text{EM}$ has 1 generator. So $4 - 1 = $ **3 Goldstone bosons** are generated — exactly absorbed as the longitudinal modes of $W^+$, $W^-$, $Z^0$. $\blacksquare$

**第 4 步 — 戈德斯通玻色子计数。** 原始的 $SU(2)_L \times U(1)_Y$ 有 $3 + 1 = 4$ 个生成元。剩余 $U(1)_\text{EM}$ 有 1 个生成元。故产生 $4 - 1 = $ **3 个戈德斯通玻色子**——正好被吸收为 $W^+$、$W^-$、$Z^0$ 的纵向模式。$\blacksquare$

---

## C. Gauge Boson Masses from the Higgs Mechanism · 由希格斯机制获得规范玻色子质量

**Claim.** Inserting $\phi = (0, (v+h)/\sqrt2)$ into $|D_\mu\phi|^2$, one obtains masses $m_W = gv/2$ and $m_Z = \sqrt{g^2+g'^2}\,v/2 = m_W/\cos\theta_W$, with the photon remaining massless.

**命题。** 将 $\phi = (0, (v+h)/\sqrt2)$ 代入 $|D_\mu\phi|^2$，得到质量 $m_W = gv/2$ 和 $m_Z = \sqrt{g^2+g'^2}\,v/2 = m_W/\cos\theta_W$，光子保持无质量。

**Step 1 — Expand around the vacuum.** Write the Higgs field as a perturbation around the vacuum, in unitary gauge (Goldstone bosons set to zero):

**第 1 步 — 在真空附近展开。** 在幺正规范（戈德斯通玻色子设为零）中将希格斯场写为真空附近的扰动：

$$ \phi = (0, (v+h)/\sqrt2), \quad \text{where } h(x) \text{ is the physical Higgs boson field.} $$

**Step 2 — Gauge kinetic term.** Compute $D_\mu\phi$ with $D_\mu = \partial_\mu - ig(\sigma^a/2)W^a_\mu - ig'YB_\mu$ ($Y_\phi = +1/2$ for the Higgs doublet):

**第 2 步 — 规范动能项。** 用 $D_\mu = \partial_\mu - ig(\sigma^a/2)W^a_\mu - ig'YB_\mu$（希格斯双重态的 $Y_\phi = +1/2$）计算 $D_\mu\phi$：

$$ D_\mu\phi = \partial_\mu\phi - ig(\sigma^a/2)W^a_\mu\phi - (ig'/2)B_\mu\phi. $$

At zeroth order in $h$ (setting $h = 0$ to find mass terms, then $h$ enters as interactions):

在 $h$ 的零阶（令 $h = 0$ 找到质量项，$h$ 之后进入相互作用）：

$$ D_\mu\langle\phi\rangle = -ig(\sigma^a/2)W^a_\mu(0, v/\sqrt2) - (ig'/2)B_\mu(0, v/\sqrt2). $$

**Step 3 — Compute $\sigma^a$ acting on $\langle\phi\rangle$.** Using the Pauli matrices:

**第 3 步 — 计算 $\sigma^a$ 作用于 $\langle\phi\rangle$。** 利用泡利矩阵：

For the doublet $\phi = (\phi^+, \phi^0) = (0, v/\sqrt2)$:

对于双重态 $\phi = (\phi^+, \phi^0) = (0, v/\sqrt2)$：

$$ \begin{aligned} \sigma^1\phi &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 \\ v/\sqrt2 \end{pmatrix} = \begin{pmatrix} v/\sqrt2 \\ 0 \end{pmatrix}, \quad \text{so } (\sigma^1/2)\phi = \begin{pmatrix} v/(2\sqrt2) \\ 0 \end{pmatrix}, \\ \sigma^2\phi &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 \\ v/\sqrt2 \end{pmatrix} = \begin{pmatrix} -iv/\sqrt2 \\ 0 \end{pmatrix}, \quad \text{so } (\sigma^2/2)\phi = \begin{pmatrix} -iv/(2\sqrt2) \\ 0 \end{pmatrix}, \\ \sigma^3\phi &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 \\ v/\sqrt2 \end{pmatrix} = \begin{pmatrix} 0 \\ -v/\sqrt2 \end{pmatrix}, \quad \text{so } (\sigma^3/2)\phi = \begin{pmatrix} 0 \\ -v/(2\sqrt2) \end{pmatrix}. \end{aligned} $$

Therefore:

因此：

$$ D_\mu\langle\phi\rangle = -ig\left[W^1_\mu\begin{pmatrix} v/(2\sqrt2) \\ 0 \end{pmatrix} + W^2_\mu\begin{pmatrix} -iv/(2\sqrt2) \\ 0 \end{pmatrix} + W^3_\mu\begin{pmatrix} 0 \\ -v/(2\sqrt2) \end{pmatrix}\right] - (ig'/2)B_\mu\begin{pmatrix} 0 \\ v/\sqrt2 \end{pmatrix}. $$

**Step 4 — $|D_\mu\phi|^2$ at zeroth order in $h$.** The mass terms come from $|(D_\mu\langle\phi\rangle)|^2$:

**第 4 步 — $|D_\mu\phi|^2$ 的 $h$ 零阶。** 质量项来自 $|(D_\mu\langle\phi\rangle)|^2$：

Introduce the charged W bosons $W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt2$. Inverting:

引入带电 W 玻色子 $W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt2$。反解：

$$ W^1_\mu = (W^+_\mu + W^-_\mu)/\sqrt2, \quad W^2_\mu = i(W^+_\mu - W^-_\mu)/\sqrt2. $$

Upper component of $D_\mu\langle\phi\rangle$:

$D_\mu\langle\phi\rangle$ 的上分量：

$$ = -ig/(2\sqrt2) \cdot (W^1_\mu - iW^2_\mu) \cdot v = -ig/(2\sqrt2) \cdot \sqrt2\, W^+_\mu \cdot v = -igv W^+_\mu/2. $$

Lower component:

下分量：

$$ \begin{aligned} &= -ig(-v/(2\sqrt2))W^3_\mu - (ig'/2)(v/\sqrt2)B_\mu = (igv/2\sqrt2)W^3_\mu - ig'v/(2\sqrt2)B_\mu \\ &= (iv/(2\sqrt2))(gW^3_\mu - g'B_\mu). \end{aligned} $$

Magnitude squared:

模的平方：

Compute it term by term. The upper component squared:

逐项计算。上分量的平方：

$$ |\text{upper}|^2 = (g^2v^2/4)|W^+_\mu|^2 = (g^2v^2/4)W^+_\mu W^{-\mu}. $$

This gives a mass term $(g^2v^2/4)W^+W^-$, identifying:

这给出质量项 $(g^2v^2/4)W^+W^-$，从而：

$$ \mathcal{L}_\text{mass} \supset (g^2v^2/4)W^+_\mu W^{-\mu} = m^2_W W^+_\mu W^{-\mu} \implies \boxed{\, m_W = gv/2 \,}. $$

The lower component squared:

下分量的平方：

$$ |\text{lower}|^2 = (v^2/8)(gW^3_\mu - g'B_\mu)^2. $$

The combination $gW^3_\mu - g'B_\mu = \sqrt{g^2+g'^2}\, Z_\mu$ (the Weinberg rotation $Z_\mu = (gW^3_\mu - g'B_\mu)/\sqrt{g^2+g'^2}$), so $|\text{lower}|^2 = (v^2/8)(g^2+g'^2) Z_\mu Z^\mu$.

组合 $gW^3_\mu - g'B_\mu = \sqrt{g^2+g'^2}\, Z_\mu$（温伯格旋转 $Z_\mu = (gW^3_\mu - g'B_\mu)/\sqrt{g^2+g'^2}$），故 $|\text{lower}|^2 = (v^2/8)(g^2+g'^2) Z_\mu Z^\mu$。

$$ \mathcal{L}_\text{mass} \supset (v^2/8)(g^2+g'^2)Z_\mu Z^\mu = (1/2)m^2_Z Z_\mu Z^\mu \implies \boxed{\, m_Z = v\sqrt{g^2+g'^2}/2 \,}. $$

The orthogonal combination $A_\mu = (g'W^3_\mu + gB_\mu)/\sqrt{g^2+g'^2}$ does NOT appear in $|D_\mu\langle\phi\rangle|^2 \to$ **$m_A = 0$** (massless photon). $\blacksquare$

正交组合 $A_\mu = (g'W^3_\mu + gB_\mu)/\sqrt{g^2+g'^2}$ 不出现在 $|D_\mu\langle\phi\rangle|^2$ 中 $\to$ **$m_A = 0$**（无质量光子）。$\blacksquare$

**Step 5 — Weinberg angle and mass ratio.** From the definitions:

**第 5 步 — 温伯格角与质量比。** 由定义：

$$ \cos\theta_W = g/\sqrt{g^2+g'^2}, \quad \sin\theta_W = g'/\sqrt{g^2+g'^2}. $$

Therefore:

因此：

$$ m_Z = v\sqrt{g^2+g'^2}/2 = v\cdot g/(2\cos\theta_W) = m_W/\cos\theta_W. $$

And $e = g\sin\theta_W$: At tree level, the **$\rho$ parameter** $\rho = m^2_W/(m^2_Z \cos^2\theta_W) = 1$ (exactly), a tree-level prediction of the Standard Model. Experimentally $\rho \approx 1.0004$ (the small deviation comes from loop corrections). $\blacksquare$

而 $e = g\sin\theta_W$：在树图阶，**$\rho$ 参数** $\rho = m^2_W/(m^2_Z \cos^2\theta_W) = 1$（精确地），这是标准模型的树图预言。实验上 $\rho \approx 1.0004$（小偏差来自圈图修正）。$\blacksquare$

---

## D. The Higgs Boson Mass · 希格斯玻色子质量

**Claim.** Expanding $\phi = (0, (v+h)/\sqrt2)$ and substituting into $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$, the physical Higgs boson has mass $m_h = \sqrt{2\mu^2} = \sqrt{2\lambda}\cdot v$.

**命题。** 展开 $\phi = (0, (v+h)/\sqrt2)$ 并代入 $V(\phi) = -\mu^2\phi^\dagger\phi + \lambda(\phi^\dagger\phi)^2$，物理希格斯玻色子的质量为 $m_h = \sqrt{2\mu^2} = \sqrt{2\lambda}\cdot v$。

**Step 1 — Expand V around the minimum.** With $\phi^\dagger\phi = (v+h)^2/2$:

**第 1 步 — 在极小值附近展开 V。** 以 $\phi^\dagger\phi = (v+h)^2/2$：

$$ V = -\mu^2(v+h)^2/2 + \lambda(v+h)^4/4. $$

Expand $(v+h)^2 = v^2 + 2vh + h^2$ and $(v+h)^4 = v^4 + 4v^3h + 6v^2h^2 + 4vh^3 + h^4$:

展开 $(v+h)^2 = v^2 + 2vh + h^2$ 和 $(v+h)^4 = v^4 + 4v^3h + 6v^2h^2 + 4vh^3 + h^4$：

$$ V = -(\mu^2/2)(v^2 + 2vh + h^2) + (\lambda/4)(v^4 + 4v^3h + 6v^2h^2 + 4vh^3 + h^4). $$

**Step 2 — Vacuum energy (constant term).** The $h$-independent part:

**第 2 步 — 真空能（常数项）。** $h$ 无关的部分：

Using $v^2 = \mu^2/\lambda$:

$$ V_0 = -\mu^2v^2/2 + \lambda v^4/4 = -\mu^4/(2\lambda) + \mu^4/(4\lambda) = -\mu^4/(4\lambda) < 0 \quad \text{(the Mexican-hat bottom is below zero).} $$

利用 $v^2 = \mu^2/\lambda$：$V_0 = -\mu^2v^2/2 + \lambda v^4/4 = -\mu^4/(2\lambda) + \mu^4/(4\lambda) = -\mu^4/(4\lambda) < 0$（墨西哥帽底部低于零）。

**Step 3 — Linear term (must vanish at minimum).** The coefficient of $h$:

**第 3 步 — 线性项（在极小值处必须消失）。** $h$ 的系数：

$$ V_\text{linear} = h(-\mu^2v + \lambda v^3) = hv(-\mu^2 + \lambda v^2) = 0, $$

since $v^2 = \mu^2/\lambda$. Good — confirms $v$ is the minimum.

因为 $v^2 = \mu^2/\lambda$。很好——确认 $v$ 是极小值。

**Step 4 — Quadratic term $\to$ Higgs mass.** The coefficient of $h^2/2$:

**第 4 步 — 二次项 $\to$ 希格斯质量。** $h^2/2$ 的系数：

$$ V_\text{quadratic} = (h^2/2)(-\mu^2 + 3\lambda v^2) = (h^2/2)(-\mu^2 + 3\mu^2) = (h^2/2)(2\mu^2) = \mu^2h^2. $$

The mass is identified from $\mathcal{L} \supset -(1/2)m^2_h h^2$:

质量由 $\mathcal{L} \supset -(1/2)m^2_h h^2$ 辨识：

$$ m^2_h = 2\mu^2 = 2\lambda v^2 \implies \boxed{\, m_h = \sqrt{2\mu^2} = \sqrt{2\lambda}\cdot v \,}. \qquad \blacksquare $$

**Step 5 — Cubic and quartic terms.** These give the Higgs self-interactions:

**第 5 步 — 三次项和四次项。** 这些给出希格斯自相互作用：

$$ V \supset \lambda vh^3 + (\lambda/4)h^4. $$

The trilinear coupling $\lambda v = m^2_h/(2v)$ and quartic coupling $\lambda = m^2_h/(2v^2)$ are fully determined by $m_h$ and $v$ — a key prediction of the SM Higgs sector, tested at the LHC. $\blacksquare$

三线耦合 $\lambda v = m^2_h/(2v)$ 和四次耦合 $\lambda = m^2_h/(2v^2)$ 完全由 $m_h$ 和 $v$ 确定——这是标准模型希格斯部分的关键预言，在大型强子对撞机上接受检验。$\blacksquare$

---

## E. Goldstone Modes Are Eaten · 戈德斯通模式被"吃掉"

**Claim.** The three Goldstone bosons (massless modes from SSB) are absorbed as the longitudinal polarizations of $W^\pm$, $Z^0$ — the degrees of freedom are conserved.

**命题。** 三个戈德斯通玻色子（来自自发对称性破缺的无质量模式）被吸收为 $W^\pm$、$Z^0$ 的纵向极化——自由度守恒。

**Step 1 — General parameterization.** Before fixing unitary gauge, write the four-component Higgs doublet in the most general way:

**第 1 步 — 一般参数化。** 在固定幺正规范之前，以最一般的方式写出四分量希格斯双重态：

$$ \phi(x) = \exp(i\pi^a(x)\sigma^a/(2v)) \cdot (0, (v+h(x))/\sqrt2). $$

Here $\pi^a(x)$ ($a = 1,2,3$) are the three Goldstone fields (the angular directions in field space), and $h(x)$ is the radial Higgs field.

这里 $\pi^a(x)$（$a = 1,2,3$）是三个戈德斯通场（场空间中的角向方向），$h(x)$ 是径向希格斯场。

**Step 2 — Goldstones as longitudinal modes.** Under a $SU(2)_L$ gauge transformation $U(x) = \exp(i\alpha^a(x)\sigma^a/2)$:

**第 2 步 — 戈德斯通玻色子作为纵向模式。** 在 $SU(2)_L$ 规范变换 $U(x) = \exp(i\alpha^a(x)\sigma^a/2)$ 下：

$$ \phi \to U\phi = \exp(i(\pi^a+\alpha^a)\sigma^a/(2v))\cdot(0, (v+h)/\sqrt2). $$

By choosing $\alpha^a(x) = -\pi^a(x)/v$, we can set the Goldstone fields to zero (unitary gauge). In this gauge, $\phi = (0, (v+h)/\sqrt2)$.

通过选择 $\alpha^a(x) = -\pi^a(x)/v$，我们可以将戈德斯通场设为零（幺正规范）。在此规范中，$\phi = (0, (v+h)/\sqrt2)$。

**Step 3 — Degree of freedom count.**

**第 3 步 — 自由度计数。**

Before SSB: $\phi$ has 4 real degrees of freedom. The 4 gauge bosons ($W^1, W^2, W^3, B$) each have 2 transverse polarizations $\to 4 \times 2 = 8$ degrees of freedom. Total: $4 + 8 = 12$.

自发对称性破缺前：$\phi$ 有 4 个实自由度。4 个规范玻色子（$W^1$、$W^2$、$W^3$、$B$）各有 2 个横向极化 $\to 4 \times 2 = 8$ 个自由度。总计：$4 + 8 = 12$。

After SSB: $W^\pm$ and $Z^0$ each have 3 polarizations (massive: 2 transverse + 1 longitudinal) $\to 3 \times 3 = 9$. The photon has 2 transverse. The Higgs $h$ has 1. Total: $9 + 2 + 1 = 12$. $\blacksquare$

自发对称性破缺后：$W^\pm$ 和 $Z^0$ 各有 3 个极化（有质量：2 横向 + 1 纵向）$\to 3 \times 3 = 9$。光子有 2 个横向。希格斯 $h$ 有 1 个。总计：$9 + 2 + 1 = 12$。$\blacksquare$

---

## F. Fermion Masses from Yukawa Couplings · 由汤川耦合获得费米子质量

**Claim.** The Yukawa coupling $\mathcal{L}_Y = -y_f(\bar\psi_L\phi\psi_R + \text{h.c.})$ generates a fermion mass $m_f = y_f v/\sqrt2$ after spontaneous symmetry breaking.

**命题。** 汤川耦合 $\mathcal{L}_Y = -y_f(\bar\psi_L\phi\psi_R + \text{h.c.})$ 在自发对称性破缺后产生费米子质量 $m_f = y_f v/\sqrt2$。

**Step 1 — The Yukawa term.** For the electron, $L = (\nu_e, e)_L$ and $R = e_R$:

**第 1 步 — 汤川项。** 对于电子，$L = (\nu_e, e)_L$，$R = e_R$：

$$ \begin{aligned} \mathcal{L}_Y &= -y_e(\bar L\phi e_R + \text{h.c.}) = -y_e[(\bar\nu_L, \bar e_L)\cdot(0; (v+h)/\sqrt2)\cdot e_R + \text{h.c.}] \\ &= -y_e[(v+h)/\sqrt2]\bar e_L e_R + \text{h.c.} \end{aligned} $$

**Step 2 — Mass term.** At zeroth order in $h$ (replacing $h \to 0$):

**第 2 步 — 质量项。** 在 $h$ 的零阶（令 $h \to 0$）：

$$ \mathcal{L}_Y \supset -y_e v/\sqrt2 \cdot \bar e_L e_R + \text{h.c.} = -m_e(\bar e_L e_R + \bar e_R e_L) = -m_e\bar e e, $$

with **$m_e = y_e v/\sqrt2$** (Dirac mass). The Yukawa coupling $y_e$ is a free parameter; $m_e$ is not predicted by the SM.

其中 **$m_e = y_e v/\sqrt2$**（狄拉克质量）。汤川耦合常数 $y_e$ 是自由参数；$m_e$ 不被标准模型预言。

**Step 3 — Higgs coupling to fermions.** The $h$-dependent part gives:

**第 3 步 — 希格斯对费米子的耦合。** $h$ 依赖部分给出：

$$ \mathcal{L}_Y \supset -(y_e/\sqrt2)h\cdot\bar e e = -(m_e/v)h\cdot\bar e e. $$

The coupling of the Higgs to each fermion is $m_f/v$ — proportional to mass. This is the key prediction: heavier fermions couple more strongly to the Higgs. For the top quark ($m_t \approx 173$ GeV, $v \approx 246$ GeV): $y_t = m_t\sqrt2/v \approx 1$. $\blacksquare$

希格斯对每种费米子的耦合为 $m_f/v$——正比于质量。这是关键预言：较重的费米子与希格斯的耦合更强。对于顶夸克（$m_t \approx 173$ GeV，$v \approx 246$ GeV）：$y_t = m_t\sqrt2/v \approx 1$。$\blacksquare$

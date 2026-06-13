# Module 6.13 — Conformal Field Theory
**模块 6.13 — 共形场论**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.13-conformal-field-theory-derivations.md)

---

## 1. Scale Invariance and the Conformal Group · 标度不变性与共形群

**Definition.** A **conformal field theory (CFT)** is a quantum field theory invariant under **conformal transformations** — coordinate changes that preserve angles, rescaling the metric by a local factor $g_{\mu\nu}(x) \to \Omega^2(x)\, g_{\mu\nu}(x)$. Conformal symmetry contains the Poincaré group plus **dilatations** $x^\mu \to \lambda x^\mu$ and **special conformal transformations**. A theory becomes conformal exactly when it has **no scale**: this happens at a **renormalization-group fixed point** $\beta(g^*) = 0$ (Module 6.6, 6.11), where the running coupling stops flowing and all memory of microscopic length scales is erased. In $d \geq 3$ the conformal group is $SO(d+1,1)$ with $\tfrac12(d+1)(d+2)$ generators; in $d = 2$ it is enhanced to the **infinite-dimensional Virasoro algebra**.

**定义。** **共形场论（CFT）**是在**共形变换**下不变的量子场论——共形变换是保持角度的坐标变换，它将度规乘以一个局域因子 $g_{\mu\nu}(x) \to \Omega^2(x)\, g_{\mu\nu}(x)$。共形对称性包含庞加莱群，外加**标度变换** $x^\mu \to \lambda x^\mu$ 和**特殊共形变换**。一个理论恰好在**没有标度**时成为共形的：这发生在**重整化群不动点** $\beta(g^*) = 0$ 处（模块 6.6、6.11），此时跑动耦合停止流动，所有微观长度尺度的记忆都被抹去。在 $d \geq 3$ 中，共形群为 $SO(d+1,1)$，有 $\tfrac12(d+1)(d+2)$ 个生成元；在 $d = 2$ 中，它被增强为**无穷维的 Virasoro 代数**。

**Demonstration.** Conformal symmetry is so restrictive that it fixes the form of correlation functions. A **primary operator** $\mathcal{O}$ of **scaling dimension** $\Delta$ transforms as $\mathcal{O}(x) \to |\partial x'/\partial x|^{\Delta/d}\,\mathcal{O}(x')$. Invariance then forces the two-point function to be
$$ \langle \mathcal{O}(x)\,\mathcal{O}(0)\rangle = \frac{1}{|x|^{2\Delta}}, $$
and the three-point function to be fixed up to a single constant $C_{ijk}$. There are no free functions — only a list of dimensions $\{\Delta_i\}$ and coefficients $\{C_{ijk}\}$, the **CFT data**.

**演示。** 共形对称性极为严格，足以固定关联函数的形式。一个标度维数为 $\Delta$ 的**初级算符** $\mathcal{O}$ 按 $\mathcal{O}(x) \to |\partial x'/\partial x|^{\Delta/d}\,\mathcal{O}(x')$ 变换。不变性随即迫使两点函数为
$$ \langle \mathcal{O}(x)\,\mathcal{O}(0)\rangle = \frac{1}{|x|^{2\Delta}}, $$
而三点函数被固定到只差一个常数 $C_{ijk}$。这里没有任意函数——只有一组维数 $\{\Delta_i\}$ 和系数 $\{C_{ijk}\}$，即 **CFT 数据**。

**Application.** This is the deep reason behind **universality** (Module 2.3, 6.6). At a continuous phase transition the correlation length diverges, the system loses its scale, and the long-distance physics is governed by a CFT. The **critical exponents** are simply the scaling dimensions of the relevant operators: e.g. the order-parameter correlator $\langle \sigma(x)\sigma(0)\rangle \sim |x|^{-(d-2+\eta)}$ gives $\Delta_\sigma = (d-2+\eta)/2$. The 3D Ising exponents — measured in real magnets and liquid–gas critical points — are now pinned to four-decimal precision by the **conformal bootstrap**, which solves the CFT purely from symmetry and consistency of the operator product expansion.

**应用。** 这正是**普适性**（模块 2.3、6.6）背后的深层原因。在连续相变处，关联长度发散，系统失去其标度，长距离物理由一个 CFT 支配。**临界指数**正是相关算符的标度维数：例如序参量关联 $\langle \sigma(x)\sigma(0)\rangle \sim |x|^{-(d-2+\eta)}$ 给出 $\Delta_\sigma = (d-2+\eta)/2$。三维伊辛指数——在真实磁体和气液临界点中测得——如今已由**共形自举**钉定到小数点后四位，该方法纯粹从对称性和算符乘积展开的自洽性求解 CFT。

---

## 2. The Operator Product Expansion, Central Charge & Two Dimensions · 算符乘积展开、中心荷与二维

**Definition.** The **operator product expansion (OPE)** states that two operators brought close together can be replaced by a sum over local operators,
$$ \mathcal{O}_i(x)\,\mathcal{O}_j(0) = \sum_k C_{ijk}\,|x|^{\Delta_k - \Delta_i - \Delta_j}\,\mathcal{O}_k(0), $$
which converges in a CFT (not just asymptotically). The **stress–energy tensor** $T_{\mu\nu}$ is the conserved current of conformal symmetry; its self-OPE defines the **central charge** $c$, a number that counts the effective degrees of freedom. In $d = 2$, writing $T(z)$ in a complex coordinate, the modes $L_n$ obey the **Virasoro algebra**
$$ [L_m, L_n] = (m - n)\,L_{m+n} + \frac{c}{12}\,m(m^2 - 1)\,\delta_{m+n,0}. $$

**定义。** **算符乘积展开（OPE）**指出，两个相互靠近的算符可以用局域算符之和来替代，
$$ \mathcal{O}_i(x)\,\mathcal{O}_j(0) = \sum_k C_{ijk}\,|x|^{\Delta_k - \Delta_i - \Delta_j}\,\mathcal{O}_k(0), $$
它在 CFT 中收敛（不只是渐近）。**能动张量** $T_{\mu\nu}$ 是共形对称性的守恒流；它与自身的 OPE 定义了**中心荷** $c$，一个计数有效自由度的数。在 $d = 2$ 中，用复坐标写出 $T(z)$，其模式 $L_n$ 满足 **Virasoro 代数**
$$ [L_m, L_n] = (m - n)\,L_{m+n} + \frac{c}{12}\,m(m^2 - 1)\,\delta_{m+n,0}. $$

**Demonstration.** The central charge labels the CFT. The free boson has $c = 1$; the **2D Ising model** at criticality is the **minimal model** with $c = \tfrac12$ (a single free Majorana fermion), whose primaries are exactly the identity, the spin $\sigma$ ($\Delta = \tfrac18$), and the energy $\varepsilon$ ($\Delta = 1$) — reproducing the known Ising exponents. Zamolodchikov's **c-theorem** shows that $c$ decreases monotonically along any RG flow, $c_\text{UV} \geq c_\text{IR}$: it is an irreversible measure of degrees of freedom integrated out, making precise the intuition that coarse-graining loses information.

**演示。** 中心荷标记了 CFT。自由玻色子有 $c = 1$；临界处的**二维伊辛模型**是 $c = \tfrac12$ 的**极小模型**（单个自由马约拉纳费米子），其初级算符恰为恒等算符、自旋 $\sigma$（$\Delta = \tfrac18$）和能量 $\varepsilon$（$\Delta = 1$）——重现了已知的伊辛指数。Zamolodchikov 的 **c-定理**表明 $c$ 沿任意 RG 流单调减小，$c_\text{UV} \geq c_\text{IR}$：它是被积掉的自由度的不可逆度量，使「粗粒化丢失信息」的直觉变得精确。

**Application.** Two-dimensional CFT is the engine of two further chapters of this curriculum. It is the theory living on the **string worldsheet** (Module 10.1): the Polyakov action is a 2D CFT of the embedding fields $X^\mu$, and the requirement that the conformal anomaly cancel ($c = 0$ total) fixes the critical dimension $D = 26$ (bosonic) or $D = 10$ (superstring). It is also one half of the **holographic duality** (Module 10.3): a $d$-dimensional CFT is dual to gravity in $(d+1)$-dimensional anti-de Sitter space, with the conformal symmetry of the boundary realized as the isometries of the bulk. Conformal field theory is thus the precise meeting point of critical phenomena, string theory, and quantum gravity.

**应用。** 二维共形场论是本课程后续两章的引擎。它是生活在**弦世界面**上的理论（模块 10.1）：Polyakov 作用量是嵌入场 $X^\mu$ 的二维 CFT，而共形反常相消的要求（总 $c = 0$）固定了临界维数 $D = 26$（玻色弦）或 $D = 10$（超弦）。它也是**全息对偶**的一半（模块 10.3）：一个 $d$ 维 CFT 对偶于 $(d+1)$ 维反德西特空间中的引力，边界的共形对称性实现为体的等距对称性。因此，共形场论正是临界现象、弦论与量子引力的精确交汇点。

---

## Key results · 核心结果

- A CFT is a QFT at an RG fixed point ($\beta = 0$) — scale invariance enhanced to conformal invariance · CFT 即 RG 不动点上的量子场论
- Symmetry fixes correlators: $\langle\mathcal{O}(x)\mathcal{O}(0)\rangle = |x|^{-2\Delta}$; CFT data $= \{\Delta_i, C_{ijk}\}$ · 对称性固定关联函数
- Critical exponents are operator scaling dimensions $\Delta$ — the origin of universality · 临界指数即标度维数
- OPE $\mathcal{O}_i\mathcal{O}_j = \sum_k C_{ijk}|x|^{\Delta_k-\Delta_i-\Delta_j}\mathcal{O}_k$; central charge $c$ counts degrees of freedom · 算符乘积展开与中心荷
- 2D: Virasoro algebra; Ising minimal model $c = \tfrac12$; the worldsheet & boundary of holography · 二维 Virasoro,通往弦世界面与全息

---

**Self-test (blank page)**

1. Define a conformal transformation and explain why a renormalization-group fixed point ($\beta(g^*) = 0$) is automatically a conformal field theory. Why does a non-zero scale (a mass, a correlation length) break conformal invariance?
2. Using scale and rotational invariance, show that the two-point function of a primary operator of dimension $\Delta$ must take the form $\langle\mathcal{O}(x)\mathcal{O}(0)\rangle \propto |x|^{-2\Delta}$. What is fixed about the three-point function?
3. State the operator product expansion and explain what the CFT data $\{\Delta_i, C_{ijk}\}$ consists of. In what sense does "solving" a CFT mean determining this data?
4. Write the Virasoro algebra and identify the central charge $c$. Give the value of $c$ for the free boson and for the critical 2D Ising model, and state the c-theorem.
5. Explain two roles 2D CFT plays elsewhere in the curriculum: the string worldsheet (and how $c$ fixes the critical dimension) and the boundary of AdS/CFT holography.

**自测（空白页）**

1. 定义共形变换，并解释为何重整化群不动点（$\beta(g^*) = 0$）自动是一个共形场论。为何非零标度（质量、关联长度）会破坏共形不变性？
2. 利用标度与转动不变性，证明维数为 $\Delta$ 的初级算符的两点函数必取 $\langle\mathcal{O}(x)\mathcal{O}(0)\rangle \propto |x|^{-2\Delta}$ 的形式。三点函数被固定到何种程度？
3. 陈述算符乘积展开，并解释 CFT 数据 $\{\Delta_i, C_{ijk}\}$ 由什么组成。在何种意义上「求解」一个 CFT 就是确定这组数据？
4. 写出 Virasoro 代数并指出中心荷 $c$。给出自由玻色子和临界二维伊辛模型的 $c$ 值，并陈述 c-定理。
5. 解释二维 CFT 在课程其他部分的两个角色：弦世界面（以及 $c$ 如何固定临界维数）与 AdS/CFT 全息的边界。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** A conformal transformation preserves angles (rescales the metric by a local factor). At an RG fixed point $\beta(g^*)=0$ the coupling stops running, so there is no scale — scale invariance, which together with locality and unitarity enhances to full conformal invariance. A mass or correlation length is a fixed scale and breaks it. · 不动点无标度,标度不变性增强为共形不变;质量/关联长度破坏之。

**2.** Translation + rotation make it $f(r)$; scale invariance $f(\lambda r)=\lambda^{-2\Delta}f(r)$ forces $f\propto r^{-2\Delta}$. The three-point function is fixed up to a single constant $C_{ijk}$. · 标度不变给 $r^{-2\Delta}$;三点函数定到常数 $C_{ijk}$。

**3.** OPE: $\mathcal O_i(x)\mathcal O_j(0)=\sum_k C_{ijk}|x|^{\Delta_k-\Delta_i-\Delta_j}\mathcal O_k(0)$. The CFT data are the dimensions $\{\Delta_i\}$ and OPE coefficients $\{C_{ijk}\}$; "solving" a CFT means determining this data (e.g. by the bootstrap) — all correlators follow. · CFT 数据 $\{\Delta_i,C_{ijk}\}$;求解即定出它们。

**4.** $[L_m,L_n]=(m-n)L_{m+n}+\tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$; $c$ = central charge. Free boson $c=1$, critical 2D Ising $c=\tfrac12$. c-theorem: $c$ decreases monotonically under RG flow, $c_\text{UV}\ge c_\text{IR}$. · Virasoro 代数;$c=1$/$\tfrac12$;c-定理。

**5.** (i) The string worldsheet is a 2D CFT; cancelling the conformal anomaly (total $c=0$, ghosts contribute $-26$) fixes $D=26$ (bosonic) or $D=10$ (super). (ii) In AdS/CFT a $d$-dimensional CFT is the holographic boundary dual of $(d{+}1)$-dimensional AdS gravity. · 弦世界面($c$ 定临界维数)与 AdS/CFT 边界。

</details>

---

← Previous: [Module 6.12 — Finite-Temperature Field Theory (Matsubara)](./module-6.12-finite-temperature-field-theory.md) · Next: [Phase 7 — General Relativity & Cosmology](../phase-7-general-relativity-and-cosmology/) · Related: [Module 10.3 — AdS/CFT & Black-Hole Information](../phase-10-strings-and-quantum-gravity/module-10.3-ads-cft-and-black-hole-information.md) · [Phase 6 index](./README.md)

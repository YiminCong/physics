---
title: "Module 6.3 — Feynman Diagrams & Perturbation Theory"
parent: "Phase 6 — Quantum Field Theory & Many-Body Physics"
nav_order: 3
---

# Module 6.3 — Feynman Diagrams & Perturbation Theory
**模块 6.3 — 费曼图与微扰论**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.3-feynman-diagrams-derivations.md)

---

## 1. Wick's Theorem and the Diagrammatic Expansion · Wick 定理与图展开

**Definition.** Perturbation theory for the interacting Green's function $G$ starts from the interaction picture, expanding the S-matrix in powers of the interaction $H_\text{int}$. The key tool is Wick's theorem: a time-ordered product of operators in the free vacuum equals a sum over all possible pairwise contractions. A contraction of $\psi(x)$ with $\psi^\dagger(x')$ is precisely the free Green's function $G^0(x,x')$. Wick's theorem thus converts operator algebra into combinatorics.

**定义。** 相互作用格林函数 $G$ 的微扰论从相互作用绘景出发，将 S 矩阵按相互作用 $H_\text{int}$ 的幂次展开。关键工具是 Wick 定理：自由真空中算符的时序乘积等于所有可能两两缩并之和。$\psi(x)$ 与 $\psi^\dagger(x')$ 的缩并恰好是自由格林函数 $G^0(x,x')$。Wick 定理因此将算符代数转化为组合数学。

Each term in the expansion is labeled by a Feynman diagram: a directed line represents $G^0(k,\omega)$, a wavy or dashed line represents the interaction vertex $U(q)$, and the rules for reading off the algebraic value of a diagram are the Feynman rules. The diagrammatic expansion is an organized, pictorial bookkeeping for the infinite perturbative series.

展开中的每一项由一个费曼图标记：有向线代表 $G^0(k,\omega)$，波浪线或虚线代表相互作用顶点 $U(q)$，从图中读出代数值的规则就是费曼规则。图展开是对无穷微扰级数的有组织的、直观的记账方式。

**Demonstration.** Consider electrons interacting via a two-body potential $U(q)$ (e.g., screened Coulomb). At first order, the Hartree diagram contributes a constant energy shift (tadpole: a loop closed on itself) and the Fock (exchange) diagram contributes the exchange self-energy $\Sigma_F(k) = -\sum_q U(q) G^0(k-q)$. These correct the single-particle dispersion already at first order. Crucially, the linked-cluster theorem guarantees that all disconnected (vacuum) diagrams cancel in ratios like $G = \langle T \psi \psi^\dagger\rangle / \langle 0|S|0\rangle$, so only connected diagrams contribute to physical quantities.

**演示。** 考虑电子通过两体势 $U(q)$（如屏蔽库仑势）相互作用。在一阶，Hartree 图贡献一个常数能量移动（蝌蚪图：一个自身闭合的圈），Fock（交换）图贡献交换自能 $\Sigma_F(k) = -\sum_q U(q) G^0(k-q)$。这些在一阶就修正了单粒子色散关系。关键地，连通集团定理保证所有不连通（真空）图在 $G = \langle T \psi \psi^\dagger\rangle / \langle 0|S|0\rangle$ 之类的比值中相消，因此只有连通图对物理量有贡献。

**Application.** The self-energy $\Sigma(k,\omega)$ collects all one-particle-irreducible (1PI) insertions — diagrams that cannot be split by cutting a single $G^0$ line. The Dyson equation then resums the entire perturbative series exactly: $G(k,\omega) = G^0(k,\omega) + G^0(k,\omega) \Sigma(k,\omega) G(k,\omega)$, which solves to $G(k,\omega) = 1/(\omega - \varepsilon_k/\hbar - \Sigma(k,\omega))$. This is the master equation linking the diagrammatic expansion to measurable quasiparticle properties (Module 6.2).

**应用。** 自能 $\Sigma(k,\omega)$ 收集所有单粒子不可约（1PI）插入——即无法通过切断单条 $G^0$ 线来分割的图。戴森方程随即精确地对整个微扰级数重求和：$G(k,\omega) = G^0(k,\omega) + G^0(k,\omega) \Sigma(k,\omega) G(k,\omega)$，其解为 $G(k,\omega) = 1/(\omega - \varepsilon_k/\hbar - \Sigma(k,\omega))$。这是将图展开与可测准粒子性质（模块 6.2）联系起来的主方程。

---

## 2. Screening and the Random-Phase Approximation · 屏蔽与随机相位近似

**Definition.** The bare Coulomb interaction $U(q) = e^2/\varepsilon_0 q^2$ is long-ranged and its direct use in perturbation theory gives logarithmically divergent results at every order. Screening — the rearrangement of the electron gas to reduce the effective interaction — must be summed to all orders in a class of diagrams. The random-phase approximation (RPA) sums the infinite series of bubble diagrams: one interaction line, then one interaction line with a particle-hole bubble inserted, then two bubbles, and so on.

**定义。** 裸库仑相互作用 $U(q) = e^2/\varepsilon_0 q^2$ 是长程的，直接用于微扰论在每阶都给出对数发散的结果。屏蔽——电子气重排以降低有效相互作用——必须在一类图中对所有阶求和。随机相位近似（RPA）对无穷系列气泡图求和：一条相互作用线，然后插入一个粒子-空穴气泡的相互作用线，再两个气泡，依此类推。

**Demonstration.** Each bubble (polarization insertion) contributes a factor of $\Pi^0(q,\omega) = -2i \int dk\, d\varepsilon/(2\pi)^4\, G^0(k+q,\omega+\varepsilon)G^0(k,\varepsilon)$, the Lindhard function (factor of 2 for spin). The geometric series gives the RPA-screened interaction $W(q,\omega) = U(q) / (1 - U(q)\Pi^0(q,\omega)) = U(q)/\varepsilon(q,\omega)$ where $\varepsilon(q,\omega)$ is the dielectric function. At $q \to 0$, $\omega = 0$, this gives static Thomas–Fermi screening: $W(q\to 0) \approx e^2/(\varepsilon_0(q^2 + k^2_\text{TF}))$ with $k_\text{TF}$ the Thomas–Fermi screening wave vector, a finite-range interaction.

**演示。** 每个气泡（极化插入）贡献因子 $\Pi^0(q,\omega) = -2i \int dk\, d\varepsilon/(2\pi)^4\, G^0(k+q,\omega+\varepsilon)G^0(k,\varepsilon)$，即 Lindhard 函数（自旋因子 2）。几何级数给出 RPA 屏蔽相互作用 $W(q,\omega) = U(q) / (1 - U(q)\Pi^0(q,\omega)) = U(q)/\varepsilon(q,\omega)$，其中 $\varepsilon(q,\omega)$ 是介电函数。在 $q \to 0$，$\omega = 0$ 时，这给出静态 Thomas–Fermi 屏蔽：$W(q\to 0) \approx e^2/(\varepsilon_0(q^2 + k^2_\text{TF}))$，$k_\text{TF}$ 为 Thomas–Fermi 屏蔽波矢，是有限程相互作用。

**Application.** The RPA is simultaneously the simplest consistent approximation for the interacting electron gas and the derivation of plasmons: poles of $W(q,\omega)$ at $\varepsilon(q,\omega) = 0$ are collective charge oscillations. The same diagrammatic logic — identify the relevant class of diagrams, sum them, read off the physics — is the everyday currency of condensed matter and particle physics. Altland & Simons "Condensed Matter Field Theory" builds much of the second half of the book on exactly this framework.

**应用。** RPA 既是相互作用电子气最简单的一致近似，也是等离激元的推导：$W(q,\omega)$ 在 $\varepsilon(q,\omega) = 0$ 处的极点是集体电荷振荡。同样的图逻辑——确定相关图类、对其求和、读出物理——是凝聚态和粒子物理的日常货币。Altland & Simons 的 "Condensed Matter Field Theory" 用这一框架构建了该书后半部分的大量内容。

---

## Self-test (blank page) · 自测（空白页）

1. State Wick's theorem. Why does it allow operator expectation values to be expressed as sums over free Green's functions?
2. Draw and label the Hartree and Fock self-energy diagrams. Write the algebraic expression for the Fock self-energy $\Sigma_F(k)$ in terms of $U(q)$ and $G^0$.
3. Write the Dyson equation $G = G^0 + G^0 \Sigma G$ and solve it for $G(k,\omega)$. What does a large $\mathrm{Im}\, \Sigma$ imply for the quasiparticle?

**自测（空白页）**

1. 陈述 Wick 定理。为什么它允许将算符期望值表达为自由格林函数的求和？
2. 画出并标注 Hartree 和 Fock 自能图。用 $U(q)$ 和 $G^0$ 写出 Fock 自能 $\Sigma_F(k)$ 的代数表达式。
3. 写出戴森方程 $G = G^0 + G^0 \Sigma G$ 并求解 $G(k,\omega)$。$\mathrm{Im}\, \Sigma$ 较大对准粒子意味着什么？

---

← Previous: [Module 6.2 — Green's Functions & Propagators](./module-6.2-greens-functions.md) · [Phase 6 index](./README.md) · Next: [Module 6.4 — Path Integrals & Field Theory](./module-6.4-path-integrals.md) →

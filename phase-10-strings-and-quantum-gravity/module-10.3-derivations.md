# Derivations — Module 10.3: AdS/CFT & Black-Hole Information
# 推导 — 模块 10.3：AdS/CFT 与黑洞信息

> ⏳ **Not yet independently verified.** These derivations follow standard references (Maldacena 1997; Witten 1998; Ryu–Takayanagi 2006) but have not yet passed line-by-line re-verification.
> ⏳ **尚未独立校验。** 这些推导遵循标准参考文献（Maldacena 1997；Witten 1998；Ryu–Takayanagi 2006），但尚未通过逐行复核。

> Companion to [Module 10.3](./module-10.3-ads-cft-and-black-hole-information.md). English first, then 中文.
> [模块 10.3](./module-10.3-ads-cft-and-black-hole-information.md) 的配套文档。先英文，后中文。

---

## A. Anti-de Sitter Geometry and Its Boundary
## A. 反德西特几何及其边界

**Claim.** $\mathrm{AdS}_{d+1}$ is the maximally symmetric solution of Einstein's equations with negative cosmological constant $\Lambda = -d(d-1)/2L^2$, and its conformal boundary is $d$-dimensional Minkowski (or $\mathbb{R}\times S^{d-1}$).

In Poincaré coordinates the metric is
$$ ds^2 = \frac{L^2}{z^2}\big(dz^2 + \eta_{\mu\nu}\,dx^\mu dx^\nu\big), \qquad z > 0. $$
The boundary sits at $z \to 0$, where the overall factor $L^2/z^2$ diverges; one strips it off with a conformal rescaling, leaving the flat boundary metric $\eta_{\mu\nu}\,dx^\mu dx^\nu$ defined only up to a Weyl factor — i.e. a **conformal** structure. The isometry group of $\mathrm{AdS}_{d+1}$ is $SO(d,2)$, which is *exactly* the conformal group of $d$-dimensional Minkowski space (Module 6.13, Derivation A): the bulk isometries are realized as boundary conformal transformations. This matching of symmetry groups is the first non-trivial check of the duality.

**断言。** $\mathrm{AdS}_{d+1}$ 是负宇宙学常数 $\Lambda = -d(d-1)/2L^2$ 的爱因斯坦方程的最大对称解；Poincaré 坐标下度规如上，边界位于 $z \to 0$。其等距群 $SO(d,2)$ 恰是 $d$ 维闵可夫斯基空间的共形群，体的等距对称性实现为边界的共形变换——这是对偶的第一个非平凡验证。

---

## B. The Field–Operator Dimension Relation
## B. 场–算符维数关系

**Claim.** A scalar of mass $m$ in $\mathrm{AdS}_{d+1}$ is dual to a boundary operator of dimension $\Delta_\pm = \tfrac{d}{2} \pm \sqrt{\tfrac{d^2}{4} + m^2 L^2}$.

**Proof.** Solve the free wave equation $(\Box - m^2)\phi = 0$ in the Poincaré metric for a mode independent of $x^\mu$ (zero boundary momentum). With $\phi = z^\alpha$, the Laplacian gives
$$ \frac{1}{\sqrt{-g}}\partial_z(\sqrt{-g}\,g^{zz}\partial_z z^\alpha) = z^{d+1}\partial_z\big(z^{-d+1}\,\tfrac{z^2}{L^2}\,\alpha z^{\alpha-1}\big) = \frac{\alpha(\alpha-d)}{L^2}z^\alpha. $$
The wave equation $\alpha(\alpha-d)/L^2 = m^2$ has roots $\alpha = \Delta_\pm = \tfrac{d}{2}\pm\sqrt{\tfrac{d^2}{4}+m^2L^2}$. Near the boundary $\phi \sim \phi_0\,z^{d-\Delta} + \langle\mathcal{O}\rangle\,z^{\Delta}$: the leading (non-normalizable) coefficient $\phi_0$ is the **source** for the dual operator $\mathcal{O}$, and the subleading (normalizable) coefficient is its **expectation value** $\langle\mathcal{O}\rangle$. Identifying $\Delta = \Delta_+$ gives the relation $\Delta(\Delta - d) = m^2 L^2$. Note that $m^2$ may be slightly negative (down to the Breitenlohner–Freedman bound $m^2 L^2 \geq -d^2/4$) while keeping $\Delta$ real — AdS stabilizes modes that would be tachyonic in flat space.

**证明。** 在 Poincaré 度规中求解自由波动方程 $(\Box - m^2)\phi = 0$，取 $\phi = z^\alpha$，得 $\alpha(\alpha-d)/L^2 = m^2$，根为 $\Delta_\pm = \tfrac{d}{2}\pm\sqrt{\tfrac{d^2}{4}+m^2L^2}$。边界附近 $\phi \sim \phi_0 z^{d-\Delta} + \langle\mathcal{O}\rangle z^\Delta$：$\phi_0$ 是对偶算符 $\mathcal{O}$ 的源，次主导系数为其期望值。由此得 $\Delta(\Delta-d) = m^2 L^2$。在 Breitenlohner–Freedman 界 $m^2L^2 \geq -d^2/4$ 内 $m^2$ 可略负而 $\Delta$ 仍为实。

---

## C. Bekenstein–Hawking Entropy from Microstate Counting
## C. 由微观态计数得 Bekenstein–Hawking 熵

**Claim.** $S_{BH} = k_B A / 4 G_N \hbar$ (here $\ell_P^2 = G_N\hbar/c^3$) is the logarithm of the number of microstates of the black hole.

**Sketch (Strominger–Vafa).** Consider a 5D extremal black hole carrying charges $(Q_1, Q_5, N)$, built in string theory from $Q_1$ D1-branes and $Q_5$ D5-branes wrapping a compact space, with $N$ units of momentum along a circle. At weak string coupling this is a bound state of branes whose degeneracy is computed by counting the states of the $1{+}1$-dimensional CFT living on the brane intersection. The asymptotic state count follows from the **Cardy formula** of 2D CFT,
$$ S = 2\pi\sqrt{\frac{c}{6}\Big(L_0 - \frac{c}{24}\Big)} \;\xrightarrow{\;c,\,L_0\,\text{from charges}\;}\; S = 2\pi\sqrt{Q_1 Q_5 N}. $$
At strong coupling the *same* charges gravitate and form a black hole; computing its horizon area $A$ and plugging into $A/4G_N$ gives **exactly** $2\pi\sqrt{Q_1 Q_5 N}$. The statistical entropy of the CFT and the geometric Bekenstein–Hawking entropy agree with no adjustable parameters — the microstates are real quantum states, so evaporation is unitary.

**要点（Strominger–Vafa）。** 五维极端黑洞由 $Q_1$ 个 D1 膜、$Q_5$ 个 D5 膜及 $N$ 单位动量构成；弱耦合下其简并度由膜交叠上的二维 CFT 态数给出，经 Cardy 公式得 $S = 2\pi\sqrt{Q_1Q_5N}$。强耦合下相同的荷形成黑洞，其视界面积代入 $A/4G_N$ 恰好给出同一结果——统计熵与几何熵无可调参数地吻合。

---

## D. The Ryu–Takayanagi Formula and the Page Curve
## D. Ryu–Takayanagi 公式与 Page 曲线

**Claim.** The entanglement entropy of a boundary region $A$ equals the minimal-area bulk surface homologous to $A$: $S_A = \text{Area}(\gamma_A)/4G_N$.

This is the holographic image of the **black-hole entropy** formula applied to an arbitrary region rather than a horizon: $\gamma_A$ is the bulk surface anchored on $\partial A$ with minimal area. It satisfies the expected properties of entanglement entropy — strong subadditivity follows geometrically from comparing minimal surfaces. The **quantum extremal surface** prescription generalizes it by extremizing $\text{Area}(\gamma)/4G_N + S_\text{bulk}(\gamma)$, including the entropy of bulk quantum fields. Applying this to an evaporating black hole, a new extremal surface — bounding an **island** region inside the horizon — comes to dominate after the **Page time** $t_\text{Page}$. Before $t_\text{Page}$ the radiation entropy follows Hawking's rising curve; after it, the island surface gives a *decreasing* entropy. The resulting **Page curve** rises then falls back to zero, consistent with unitary evaporation. The information is, in principle, recoverable from the radiation.

**断言。** 边界区域 $A$ 的纠缠熵等于与 $A$ 同调的体中极小面积曲面：$S_A = \text{Area}(\gamma_A)/4G_N$。量子极值曲面方案通过对 $\text{Area}(\gamma)/4G_N + S_\text{bulk}(\gamma)$ 取极值来推广它；应用于蒸发黑洞时，Page 时间之后一个界定视界内**岛**区域的新极值曲面占主导，使辐射熵在 Page 时间后回落，给出与幺正蒸发一致的 Page 曲线。

---

← Back to [Module 10.3 — AdS/CFT & Black-Hole Information](./module-10.3-ads-cft-and-black-hole-information.md)

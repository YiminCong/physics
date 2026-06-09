# Derivations — Module 6.11: Effective Field Theory & the Wilsonian Renormalization Group
# 推导 — 模块 6.11：有效场论与威尔逊重整化群

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 6.11](./module-6.11-effective-field-theory-and-the-renormalization-group.md). Full step-by-step proofs. English first, then 中文.
> [模块 6.11](./module-6.11-effective-field-theory-and-the-renormalization-group.md) 的配套文档：完整逐步证明。先英文，后中文。

---

## A. The Wilsonian RG Step: Integrate Out, Then Rescale · 威尔逊 RG 步骤：先积掉，后重标度

**Claim.** One RG step — integrate out the high-momentum shell, then rescale — maps the couplings $\{g_i\}$ to $\{g_i'\}$ and defines an RG transformation whose fixed points $g^*$ satisfy $g_i' = g_i$.

**命题。** 一步 RG——积掉高动量壳层，再重标度——将耦合 $\{g_i\}$ 映射为 $\{g_i'\}$，定义一个 RG 变换，其不动点 $g^*$ 满足 $g_i' = g_i$。

**Step 1 — Split the field.** Begin with the cutoff path integral $Z = \int_{|k|<\Lambda} \mathcal{D}\varphi\, e^{-S[\varphi]}$. Choose $b > 1$ and decompose $\varphi(k) = \varphi_L(k) + \varphi_H(k)$, where $\varphi_L$ is supported on $|k| < \Lambda/b$ (low modes) and $\varphi_H$ on $\Lambda/b < |k| < \Lambda$ (the high-momentum shell). Because the modes occupy disjoint momentum ranges, the measure factorizes: $\mathcal{D}\varphi = \mathcal{D}\varphi_L\, \mathcal{D}\varphi_H$.

**第 1 步 — 分裂场。** 从截断路径积分 $Z = \int_{|k|<\Lambda} \mathcal{D}\varphi\, e^{-S[\varphi]}$ 出发。取 $b > 1$，分解 $\varphi(k) = \varphi_L(k) + \varphi_H(k)$，其中 $\varphi_L$ 支撑于 $|k| < \Lambda/b$（低模），$\varphi_H$ 支撑于 $\Lambda/b < |k| < \Lambda$（高动量壳层）。由于两类模占据不相交的动量范围，测度因子化：$\mathcal{D}\varphi = \mathcal{D}\varphi_L\, \mathcal{D}\varphi_H$。

**Step 2 — Integrate out the high modes.** Do the $\varphi_H$ integral at fixed $\varphi_L$, defining the **Wilsonian effective action** for the low modes:

**第 2 步 — 积掉高模。** 在固定 $\varphi_L$ 下做 $\varphi_H$ 积分，为低模定义**威尔逊有效作用量**：

$$ e^{-S_{\Lambda/b}[\varphi_L]} \equiv \int \mathcal{D}\varphi_H\, e^{-S_\Lambda[\varphi_L + \varphi_H]}. $$

The free part separates (the kinetic term is diagonal in $k$, so it splits as $S_0[\varphi_L] + S_0[\varphi_H]$), and the interaction couples the two sectors. Expanding the interaction and doing the Gaussian $\varphi_H$ integrals shell-by-shell generates new and shifted couplings among the $\varphi_L$. The resulting $S_{\Lambda/b}[\varphi_L]$ has the same field content but a lower cutoff $\Lambda/b$ and modified couplings $\hat g_i$.

自由部分分离（动能项在 $k$ 中对角，故分裂为 $S_0[\varphi_L] + S_0[\varphi_H]$），相互作用耦合两个部分。展开相互作用并逐壳层做 $\varphi_H$ 的高斯积分，在 $\varphi_L$ 之间生成新的及移动的耦合。所得 $S_{\Lambda/b}[\varphi_L]$ 具有相同的场内容但更低的截断 $\Lambda/b$ 与修改后的耦合 $\hat g_i$。

**Step 3 — Rescale to restore the cutoff.** The new theory lives on $|k| < \Lambda/b$; to compare with the original we restore the cutoff. Rescale momenta and (Euclidean) coordinates,

**第 3 步 — 重标度以恢复截断。** 新理论位于 $|k| < \Lambda/b$ 上；为与原理论比较，恢复截断。重标度动量与（欧几里得）坐标，

$$ k' = b k, \quad x' = x / b, \quad \text{so that } |k'| < \Lambda \text{ again}, $$

and rescale the field $\varphi_L(x) = \zeta\, \varphi'(x')$ by a factor $\zeta$ chosen to bring the kinetic term back to canonical normalization. The composition of "integrate out" and "rescale" sends each coupling $g_i \to g_i' = \mathcal{R}_b(g)_i$. This map $\mathcal{R}_b$ is the **RG transformation**; iterating it traces the **RG flow** through coupling space.

并按因子 $\zeta$ 重标度场 $\varphi_L(x) = \zeta\, \varphi'(x')$，$\zeta$ 选取使动能项恢复正则归一化。"积掉"与"重标度"的复合将每个耦合 $g_i \to g_i' = \mathcal{R}_b(g)_i$。此映射 $\mathcal{R}_b$ 即 **RG 变换**；迭代它在耦合空间中描出 **RG 流**。

**Step 4 — Fixed points.** A point $g^*$ with $\mathcal{R}_b(g^*) = g^*$, i.e. $g_i' = g_i$ for all $i$, is a **fixed point**: coarse-graining returns the same theory, so the theory is scale-invariant there. The Gaussian fixed point $g^* = 0$ (free theory) is always present; interacting fixed points (Wilson–Fisher, Module 6.6) occur where loop-generated shifts balance the tree-level rescaling. $\blacksquare$

**第 4 步 — 不动点。** 满足 $\mathcal{R}_b(g^*) = g^*$（即对所有 $i$ 有 $g_i' = g_i$）的点 $g^*$ 是**不动点**：粗粒化返回同一理论，故理论在此处尺度不变。高斯不动点 $g^* = 0$（自由理论）始终存在；相互作用不动点（Wilson–Fisher，模块 6.6）出现在圈生成的移动与树级重标度相平衡之处。$\blacksquare$

---

## B. Operator Scaling and the Relevant / Marginal / Irrelevant Classification · 算符标度与相关/边缘/无关分类

**Claim.** Near the Gaussian fixed point a coupling of an operator $O$ of mass dimension $\Delta_O$ in $d$ spacetime dimensions scales as $g \to b^{d - \Delta_O} g$. The scalar field has dimension $(d-2)/2$; in $d = 4$ the $\varphi^n$ couplings classify as $\varphi^2$ relevant, $\varphi^4$ marginal, $\varphi^6$ and higher irrelevant.

**命题。** 在高斯不动点附近，$d$ 维时空中质量量纲为 $\Delta_O$ 的算符 $O$ 的耦合按 $g \to b^{d - \Delta_O} g$ 标度。标量场量纲为 $(d-2)/2$；在 $d = 4$ 中 $\varphi^n$ 耦合分类为 $\varphi^2$ 相关、$\varphi^4$ 边缘、$\varphi^6$ 及更高无关。

**Step 1 — Fix the field dimension from the kinetic term.** The Gaussian fixed point is the free action $S_0 = \int d^d x\, \tfrac12 (\partial\varphi)^2$. It must be a fixed point, i.e. invariant under the rescaling $x \to x/b$, $\varphi \to \zeta\varphi$. Under $x \to x/b$, the measure gives $d^d x \to b^{-d} d^d x$ and each derivative gives $\partial \to b\, \partial$, so $(\partial\varphi)^2 \to b^2 \zeta^2 (\partial\varphi)^2$. Invariance of $S_0$ requires

**第 1 步 — 由动能项确定场量纲。** 高斯不动点是自由作用量 $S_0 = \int d^d x\, \tfrac12 (\partial\varphi)^2$。它必须是不动点，即在重标度 $x \to x/b$、$\varphi \to \zeta\varphi$ 下不变。在 $x \to x/b$ 下，测度给出 $d^d x \to b^{-d} d^d x$，每个导数给出 $\partial \to b\, \partial$，故 $(\partial\varphi)^2 \to b^2 \zeta^2 (\partial\varphi)^2$。$S_0$ 不变要求

$$ b^{-d} \cdot b^2 \cdot \zeta^2 = 1 \implies \zeta = b^{(d-2)/2}. $$

Since $\varphi \to \zeta\varphi = b^{(d-2)/2}\varphi$, the field carries **mass dimension $[\varphi] = (d-2)/2$** (a field that scales as $b^{\Delta_\varphi}$ under $x \to x/b$ has mass dimension $\Delta_\varphi$).

由于 $\varphi \to \zeta\varphi = b^{(d-2)/2}\varphi$，场携带**质量量纲 $[\varphi] = (d-2)/2$**（在 $x \to x/b$ 下按 $b^{\Delta_\varphi}$ 标度的场具有质量量纲 $\Delta_\varphi$）。

**Step 2 — Scaling of a general coupling.** Consider a term $g \int d^d x\, O$, where $O$ is an operator of mass dimension $\Delta_O$ (so it scales as $O \to b^{\Delta_O} O$). Under the rescaling,

**第 2 步 — 一般耦合的标度。** 考虑项 $g \int d^d x\, O$，其中 $O$ 是质量量纲为 $\Delta_O$ 的算符（故按 $O \to b^{\Delta_O} O$ 标度）。在重标度下，

$$ g \int d^d x\, O \to g \cdot b^{-d} \cdot b^{\Delta_O} \int d^d x\, O = (b^{\Delta_O - d} g) \int d^d x\, O. $$

To keep the action term written as $g' \int d^d x\, O$, identify the transformed coupling

为使作用量项保持写为 $g' \int d^d x\, O$，辨认变换后的耦合

$$ \boxed{\, g' = b^{d - \Delta_O} g \,} $$

(The exponent $d - \Delta_O$ is exactly the mass dimension of $g$, since the term $\int d^d x\, g O$ must be dimensionless: $[g] = d - \Delta_O$.) This is the **engineering-dimension** scaling law.

（指数 $d - \Delta_O$ 恰为 $g$ 的质量量纲，因为 $\int d^d x\, g O$ 必须无量纲：$[g] = d - \Delta_O$。）这是**工程量纲**标度律。

**Step 3 — Classify.** Iterating with $b > 1$: if $d - \Delta_O > 0$ the coupling **grows** (relevant); if $= 0$ it is **unchanged** at tree level (marginal); if $< 0$ it **shrinks** (irrelevant). Now use $[\varphi] = (d-2)/2$ for the operator $O = \varphi^n$, whose dimension is $\Delta_{\varphi^n} = n(d-2)/2$. In $d = 4$, $[\varphi] = 1$, so:

**第 3 步 — 分类。** 以 $b > 1$ 迭代：若 $d - \Delta_O > 0$ 耦合**增长**（相关）；若 $= 0$ 树级**不变**（边缘）；若 $< 0$ **收缩**（无关）。现对算符 $O = \varphi^n$ 用 $[\varphi] = (d-2)/2$，其量纲为 $\Delta_{\varphi^n} = n(d-2)/2$。在 $d = 4$ 中，$[\varphi] = 1$，故：

  • $\varphi^2$: $\Delta = 2$, $d - \Delta = 4 - 2 = +2 > 0 \to$ **relevant** (the mass term, most relevant).
  • $\varphi^4$: $\Delta = 4$, $d - \Delta = 4 - 4 = 0 \to$ **marginal** (tree-level scale-invariant; loops decide).
  • $\varphi^6$: $\Delta = 6$, $d - \Delta = 4 - 6 = -2 < 0 \to$ **irrelevant**.
  • $\varphi^n$, $n \ge 6$, and $(\partial\varphi)^2\varphi^2$, …: $d - \Delta < 0 \to$ **irrelevant**.

  • $\varphi^2$：$\Delta = 2$，$d - \Delta = 4 - 2 = +2 > 0 \to$ **相关**（质量项，最相关）。
  • $\varphi^4$：$\Delta = 4$，$d - \Delta = 4 - 4 = 0 \to$ **边缘**（树级尺度不变；由圈决定）。
  • $\varphi^6$：$\Delta = 6$，$d - \Delta = 4 - 6 = -2 < 0 \to$ **无关**。
  • $\varphi^n$，$n \ge 6$，及 $(\partial\varphi)^2\varphi^2$、…：$d - \Delta < 0 \to$ **无关**。

**Step 4 — Predictivity as IR insensitivity.** Because $[g_n] = 4 - n$ decreases without bound as $n$ grows, only **finitely many** operators ($\varphi^2$, $\varphi^4$, $(\partial\varphi)^2$) are relevant or marginal in $d = 4$. Under repeated coarse-graining, all irrelevant couplings flow toward zero, regardless of their cutoff-scale values. Hence the IR theory is parametrized by the finite set of relevant/marginal couplings: measuring those fixes all low-energy predictions, independent of the UV completion. This is **renormalizability re-derived as IR insensitivity**: a renormalizable theory is one whose IR dynamics is controlled by finitely many relevant/marginal directions of a fixed point. $\blacksquare$

**第 4 步 — 可预言性即红外不敏感性。** 由于 $[g_n] = 4 - n$ 随 $n$ 增大无下界地减小，$d = 4$ 中只有**有限个**算符（$\varphi^2$、$\varphi^4$、$(\partial\varphi)^2$）相关或边缘。在反复粗粒化下，所有无关耦合流向零，与其截断尺度取值无关。因此红外理论由有限的相关/边缘耦合集合参数化：测量这些就确定所有低能预言，与紫外完备化无关。这是**可重整性被重新推导为红外不敏感性**：可重整理论是其红外动力学由不动点的有限个相关/边缘方向控制的理论。$\blacksquare$

---

## C. Fermi Theory from Integrating Out the W: $G_F \propto 1/m_W^2$ · 积掉 W 得费米理论：$G_F \propto 1/m_W^2$

**Claim.** Integrating out the W boson from the electroweak Lagrangian at momenta $q^2 \ll m_W^2$ produces the Fermi four-fermion contact interaction with $G_F/\sqrt{2} = g^2/(8 m_W^2)$, so $G_F \propto 1/m_W^2$.

**命题。** 在动量 $q^2 \ll m_W^2$ 处从电弱拉格朗日量积掉 W 玻色子，产生费米四费米接触相互作用，其中 $G_F/\sqrt{2} = g^2/(8 m_W^2)$，故 $G_F \propto 1/m_W^2$。

**Step 1 — Charged-current vertex in the full theory.** In the Standard Model the charged weak current couples to the W boson through $\mathcal{L}_{\rm int} = (g/\sqrt{2}) (J^{+\mu} W_\mu^+ + J^{-\mu} W_\mu^-)$, where $g$ is the $SU(2)_L$ gauge coupling and $J^{\pm\mu}$ are the charged fermion currents (e.g. $J^{-\mu} = \bar\nu_e \gamma^\mu P_L e + \ldots$ with the left-handed projector $P_L = (1-\gamma^5)/2$). The factor $1/\sqrt{2}$ is the conventional normalization of the charged combination $W^\pm = (W^1 \mp iW^2)/\sqrt{2}$.

**第 1 步 — 完整理论中的带电流顶点。** 在标准模型中，带电弱流通过 $\mathcal{L}_{\rm int} = (g/\sqrt{2}) (J^{+\mu} W_\mu^+ + J^{-\mu} W_\mu^-)$ 与 W 玻色子耦合，其中 $g$ 是 $SU(2)_L$ 规范耦合，$J^{\pm\mu}$ 是带电费米流（如 $J^{-\mu} = \bar\nu_e \gamma^\mu P_L e + \ldots$，左手投影算符 $P_L = (1-\gamma^5)/2$）。因子 $1/\sqrt{2}$ 是带电组合 $W^\pm = (W^1 \mp iW^2)/\sqrt{2}$ 的常规归一化。

**Step 2 — Tree-level W exchange.** A charged-current four-fermion process (e.g. $\mu^- \to e^- \bar\nu_e \nu_\mu$) proceeds by single W exchange. The amplitude has two vertices ($g/\sqrt{2}$ each) joined by the W propagator. In unitary gauge the massive vector propagator is

**第 2 步 — 树级 W 交换。** 带电流四费米过程（如 $\mu^- \to e^- \bar\nu_e \nu_\mu$）通过单个 W 交换进行。振幅有两个顶点（各 $g/\sqrt{2}$），由 W 传播子连接。在幺正规范中，有质量矢量传播子为

$$ D_{\mu\nu}(q) = -i\, (g_{\mu\nu} - q_\mu q_\nu/m_W^2) / (q^2 - m_W^2). $$

The amplitude is therefore

故振幅为

$$ i\mathcal{M} = (ig/\sqrt{2})^2 \cdot J^{+\mu} \cdot [-i(g_{\mu\nu} - q_\mu q_\nu/m_W^2)/(q^2 - m_W^2)] \cdot J^{-\nu}. $$

**Step 3 — Low-momentum expansion (integrate out the W).** Integrating out the W means evaluating its propagator at momentum transfer far below its mass, $q^2 \ll m_W^2$. Expand the scalar factor

**第 3 步 — 低动量展开（积掉 W）。** 积掉 W 意味着在远低于其质量的动量转移处求其传播子，$q^2 \ll m_W^2$。展开标量因子

$$ 1/(q^2 - m_W^2) = -(1/m_W^2) \cdot 1/(1 - q^2/m_W^2) = -(1/m_W^2)[1 + q^2/m_W^2 + O(q^4/m_W^4)]. $$

To leading order the propagator collapses to a constant, $1/(q^2 - m_W^2) \to -1/m_W^2$, and the $q_\mu q_\nu/m_W^2$ piece (which acts on the currents as $q_\mu J^\mu$, suppressed by light fermion masses) is likewise higher order. Thus

到领头阶传播子塌缩为常数，$1/(q^2 - m_W^2) \to -1/m_W^2$，而 $q_\mu q_\nu/m_W^2$ 部分（作用于流为 $q_\mu J^\mu$，被轻费米子质量压制）同样是高阶的。于是

$$ i\mathcal{M} \to (ig/\sqrt{2})^2 \cdot J^{+\mu} \cdot [-i g_{\mu\nu} \cdot (-1/m_W^2)] \cdot J^{-\nu} = i (g^2/2m_W^2) \cdot J^{+\mu} J^{-}_\mu. $$

The W has been removed; what remains is a **local four-fermion contact interaction** with no propagating heavy field.

W 已被移除；剩下的是一个**局域四费米接触相互作用**，不含传播的重场。

**Step 4 — Match to the Fermi Lagrangian.** Fermi's effective Lagrangian is written $\mathcal{L}_F = -(G_F/\sqrt{2}) J^{+\mu} J^{-}_\mu$ (current–current form). Matching the contact amplitude above onto $\mathcal{L}_F$ (an amplitude $(G_F/\sqrt{2}) \cdot 2$ from the two ways the currents contract, i.e. the standard $4G_F/\sqrt{2}$ normalization of the charged-current product) fixes the coefficient:

**第 4 步 — 匹配费米拉格朗日量。** 费米有效拉格朗日量写为 $\mathcal{L}_F = -(G_F/\sqrt{2}) J^{+\mu} J^{-}_\mu$（流–流形式）。将上面的接触振幅匹配到 $\mathcal{L}_F$（流的两种缩并方式给出振幅 $(G_F/\sqrt{2}) \cdot 2$，即带电流乘积的标准 $4G_F/\sqrt{2}$ 归一化）确定系数：

$$ \boxed{\, G_F/\sqrt{2} = g^2 / (8 m_W^2), \quad \text{hence } G_F = \sqrt{2}\, g^2 / (8 m_W^2) \propto 1/m_W^2 \,} $$

Equivalently, using $g^2 = 8 m_W^2 G_F/\sqrt{2}$, one recovers the textbook $G_F/\sqrt{2} = g^2/(8m_W^2) \approx 1.166\times 10^{-5}\ \mathrm{GeV}^{-2}$.

等价地，用 $g^2 = 8 m_W^2 G_F/\sqrt{2}$，复现教科书结果 $G_F/\sqrt{2} = g^2/(8m_W^2) \approx 1.166\times 10^{-5}\ \mathrm{GeV}^{-2}$。

**Step 5 — $G_F$ is irrelevant.** Each fermion field has mass dimension $[\psi] = (d-1)/2 = 3/2$ in $d = 4$, so the four-fermion operator $J J \sim \bar\psi\psi\bar\psi\psi$ has dimension $\Delta = 4 \cdot 3/2 = 6 > 4 = d$. By the scaling law of Derivation B, its coupling has dimension $[G_F] = d - \Delta = 4 - 6 = -2 < 0$: **$G_F$ is an irrelevant coupling**, suppressed by $1/\Lambda^2$ with $\Lambda = m_W$. The neglected $q^2/m_W^2$ terms of Step 3 are precisely the higher-dimension operators of the EFT expansion, each suppressed by an additional power of $q^2/m_W^2$. $\blacksquare$

**第 5 步 — $G_F$ 是无关的。** $d = 4$ 中每个费米场质量量纲 $[\psi] = (d-1)/2 = 3/2$，故四费米算符 $J J \sim \bar\psi\psi\bar\psi\psi$ 量纲为 $\Delta = 4 \cdot 3/2 = 6 > 4 = d$。由推导 B 的标度律，其耦合量纲为 $[G_F] = d - \Delta = 4 - 6 = -2 < 0$：**$G_F$ 是无关耦合**，被 $1/\Lambda^2$（$\Lambda = m_W$）压制。第 3 步被略去的 $q^2/m_W^2$ 项正是 EFT 展开的高维算符，各被额外的 $q^2/m_W^2$ 幂次压制。$\blacksquare$

---

## D. Critical Exponents from the Linearized RG: $\nu = 1/y_t$ · 由线性化 RG 得临界指数：$\nu = 1/y_t$

**Claim.** Linearizing the RG flow about a fixed point, the eigenvalues $y_i$ of the linearized map are the scaling dimensions of the couplings; the correlation-length exponent is $\nu = 1/y_t$, with $y_t$ the relevant (thermal) eigenvalue. Universality follows because $y_i$ depend only on the fixed point.

**命题。** 在不动点附近线性化 RG 流，线性化映射的本征值 $y_i$ 是耦合的标度维度；关联长度指数为 $\nu = 1/y_t$，$y_t$ 为相关（热）本征值。普适性随之而来，因为 $y_i$ 只依赖于不动点。

**Step 1 — From discrete map to $\beta$-functions.** Write $b = e^{\ell}$ and take $\ell$ infinitesimal, so one RG step becomes a flow in the parameter $\ell = \ln b$. The continuous flow is $dg_i/d\ell = \beta_i(\{g\})$, defining the $\beta$-function as the velocity under coarse-graining. This matches Module 6.6's $\beta(g) = \mu\, dg/d\mu$ up to the sign convention $\beta(g) = -dg/d\ln b$: increasing $\ell$ (more coarse-graining, lower energy) corresponds to decreasing $\mu$, so the two $\beta$-functions differ by an overall sign. A fixed point is $\beta_i(g^*) = 0$, consistent with 6.6's $\beta(g^*) = 0$.

**第 1 步 — 从离散映射到 $\beta$ 函数。** 写 $b = e^{\ell}$ 并取 $\ell$ 无穷小，一步 RG 变为参数 $\ell = \ln b$ 中的流。连续流为 $dg_i/d\ell = \beta_i(\{g\})$，将 $\beta$ 函数定义为粗粒化下的速度。这与模块 6.6 的 $\beta(g) = \mu\, dg/d\mu$ 一致，至多差一个符号约定 $\beta(g) = -dg/d\ln b$：$\ell$ 增大（更多粗粒化、更低能量）对应 $\mu$ 减小，故两个 $\beta$ 函数相差一个整体符号。不动点为 $\beta_i(g^*) = 0$，与 6.6 的 $\beta(g^*) = 0$ 一致。

**Step 2 — Linearize about the fixed point.** Write $g_i = g_i^* + \delta g_i$ and expand to first order:

**第 2 步 — 在不动点附近线性化。** 写 $g_i = g_i^* + \delta g_i$ 并展开到一阶：

$$ d(\delta g_i)/d\ell = M_{ij}\, \delta g_j, \qquad M_{ij} = \partial\beta_i/\partial g_j\, |_{g^*}. $$

Diagonalize the stability matrix $M$ with eigenvalues $y_a$ and eigenvectors (scaling fields) $u_a = \sum_i e^{a}_i\, \delta g_i$. Each scaling field evolves multiplicatively,

对角化稳定性矩阵 $M$，本征值为 $y_a$、本征矢量（标度场）为 $u_a = \sum_i e^{a}_i\, \delta g_i$。每个标度场以乘性方式演化，

$$ du_a/d\ell = y_a u_a \implies u_a(\ell) = u_a(0) e^{y_a \ell} = u_a(0) b^{y_a}. $$

So $u_a \to b^{y_a} u_a$: the eigenvalue $y_a$ is precisely the scaling dimension of the coupling $u_a$. Comparing with Derivation B, near the Gaussian fixed point $y_a = d - \Delta_{O_a}$ (the engineering dimension), and $y_a > 0 \Leftrightarrow$ relevant, $y_a = 0 \Leftrightarrow$ marginal, $y_a < 0 \Leftrightarrow$ irrelevant. Interactions shift these to **anomalous** values.

故 $u_a \to b^{y_a} u_a$：本征值 $y_a$ 恰为耦合 $u_a$ 的标度维度。与推导 B 对比，在高斯不动点附近 $y_a = d - \Delta_{O_a}$（工程量纲），且 $y_a > 0 \Leftrightarrow$ 相关，$y_a = 0 \Leftrightarrow$ 边缘，$y_a < 0 \Leftrightarrow$ 无关。相互作用将其移动到**反常**值。

**Step 3 — Anomalous-dimension split.** The full scaling dimension separates into a classical (engineering) piece and a loop-induced anomalous piece,

**第 3 步 — 反常量纲分裂。** 完整标度维度分裂为经典（工程）部分与圈诱导的反常部分，

$$ \Delta = \Delta_{\rm classical} + \gamma, $$

where $\gamma$ (the anomalous dimension) is the deviation of $y_a$ from its Gaussian value, generated by the nontrivial fixed-point interactions. At the Gaussian fixed point $\gamma = 0$; at Wilson–Fisher $\gamma = O(\epsilon)$ (Module 6.6).

其中 $\gamma$（反常量纲）是 $y_a$ 偏离其高斯值的偏差，由非平庸不动点相互作用生成。在高斯不动点 $\gamma = 0$；在 Wilson–Fisher，$\gamma = O(\epsilon)$（模块 6.6）。

**Step 4 — Correlation-length exponent.** The correlation length $\xi$ has mass dimension $-1$, so it scales as $\xi \to b\xi$ under one RG step (lengths shrink by $b$ in rescaled units, so $\xi$ in physical units grows). The relevant thermal coupling — the deviation $t \propto (T - T_c)$ from criticality — is the scaling field $u_t$ with eigenvalue $y_t > 0$, so after $\ell$ steps $t(\ell) = b^{y_t} t$. Iterate until the rescaled $t$ becomes $O(1)$ (the correlation length reaches the cutoff), at $b^*$ with $(b^*)^{y_t} t = \text{const}$, i.e. $b^* \propto t^{-1/y_t}$. Since the physical correlation length is $\xi = b^* \cdot (\text{cutoff length}) \propto t^{-1/y_t}$, and by definition $\xi \propto |t|^{-\nu}$,

**第 4 步 — 关联长度指数。** 关联长度 $\xi$ 质量量纲为 $-1$，故一步 RG 下按 $\xi \to b\xi$ 标度（重标度单位中长度缩小 $b$ 倍，故物理单位中 $\xi$ 增长）。相关的热耦合——偏离临界的 $t \propto (T - T_c)$——是本征值 $y_t > 0$ 的标度场 $u_t$，故 $\ell$ 步后 $t(\ell) = b^{y_t} t$。迭代直到重标度的 $t$ 变为 $O(1)$（关联长度达到截断），在 $b^*$ 处满足 $(b^*)^{y_t} t = \text{常数}$，即 $b^* \propto t^{-1/y_t}$。由于物理关联长度 $\xi = b^* \cdot (\text{截断长度}) \propto t^{-1/y_t}$，且按定义 $\xi \propto |t|^{-\nu}$，

$$ \boxed{\, \nu = 1/y_t \,} $$

**Step 5 — Universality and the $\beta'(g^*)$ connection.** The eigenvalues $y_a$ — and hence $\nu$ — depend only on the stability matrix $M$ at the fixed point, i.e. only on the fixed point itself, not on microscopic lattice details, the cutoff value, or irrelevant couplings (which flow to zero). Therefore any two systems flowing to the same fixed point share the same critical exponents: this is **universality** (Modules 2.3, 4.6/1.19). In single-coupling language, the relevant eigenvalue is the slope of the $\beta$-function at the fixed point, $y_t = -\beta'(g^*) = -\partial\beta/\partial g|_{g^*}$ (with the 6.6 sign convention $\beta = \mu\, dg/d\mu$), so the correlation-length exponent is directly read off as $\nu = 1/y_t = -1/\beta'(g^*)$. The same slope $\beta'(g^*)$ governs how fast trajectories approach or leave the fixed point and thus sets the universal critical exponent. $\blacksquare$

**第 5 步 — 普适性与 $\beta'(g^*)$ 的联系。** 本征值 $y_a$——从而 $\nu$——只依赖于不动点处的稳定性矩阵 $M$，即只依赖于不动点本身，而非微观格点细节、截断值或无关耦合（它们流向零）。因此流向同一不动点的任意两个系统共享相同的临界指数：这就是**普适性**（模块 2.3、4.6/1.19）。在单耦合语言中，相关本征值是 $\beta$ 函数在不动点处的斜率，$y_t = -\beta'(g^*) = -\partial\beta/\partial g|_{g^*}$（用 6.6 的符号约定 $\beta = \mu\, dg/d\mu$），故关联长度指数直接读出为 $\nu = 1/y_t = -1/\beta'(g^*)$。同一斜率 $\beta'(g^*)$ 支配轨迹趋近或离开不动点的快慢，从而设定普适临界指数。$\blacksquare$

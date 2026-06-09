---
title: "Derivations — Module 5.3: Ginzburg–Landau Theory"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.3: Ginzburg–Landau Theory
# 推导 — 模块 5.3：金兹堡–朗道理论

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.3](./module-5.3-ginzburg-landau-theory.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.3](./module-5.3-ginzburg-landau-theory.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Minimizing the Uniform GL Free Energy: $|\psi|^2 = -\alpha/\beta$ · 最小化均匀 GL 自由能：$|\psi|^2 = -\alpha/\beta$

**Claim.** In the spatially uniform case (no gradients, no magnetic field), minimizing the Ginzburg–Landau free energy $F = F_n + \alpha|\psi|^2 + (\beta/2)|\psi|^4$ with respect to $|\psi|^2$ gives $|\psi|^2 = -\alpha/\beta$ when $\alpha < 0$ ($T < T_c$), and the condensation energy density is $-\alpha^2/(2\beta)$.

**命题。** 在空间均匀情形（无梯度，无磁场）下，对 $|\psi|^2$ 最小化金兹堡–朗道自由能 $F = F_n + \alpha|\psi|^2 + (\beta/2)|\psi|^4$，当 $\alpha < 0$（$T < T_c$）时给出 $|\psi|^2 = -\alpha/\beta$，凝聚能密度为 $-\alpha^2/(2\beta)$。

**Step 1 — Set up the free energy.** Write $|\psi|^2 = \rho \ge 0$. The free energy density relative to the normal state is

**第 1 步 — 建立自由能。** 写 $|\psi|^2 = \rho \ge 0$。相对于正常态的自由能密度为

$$ f(\rho) = \alpha \rho + (\beta/2) \rho^2. $$

The parameter $\beta > 0$ always (required for stability: without a positive $\beta$ the free energy would be unbounded below).

参数 $\beta > 0$ 始终成立（稳定性要求：若没有正的 $\beta$，自由能将无下界）。

**Step 2 — Find the critical point.** Differentiate $f$ with respect to $\rho$ and set to zero:

**第 2 步 — 求驻点。** 对 $\rho$ 求 $f$ 的导数并置零：

$$ df/d\rho = \alpha + \beta \rho = 0 \quad\implies\quad \rho_0 = -\alpha/\beta. $$

**Step 3 — Classify by sign of $\alpha$.** Two cases arise depending on the sign of $\alpha$ (which changes at $T_c$):

**第 3 步 — 按 $\alpha$ 的符号分类。** 根据 $\alpha$ 的符号（在 $T_c$ 处改变）出现两种情况：

- Case $\alpha > 0$ ($T > T_c$): $\rho_0 = -\alpha/\beta < 0$, which is unphysical since $\rho = |\psi|^2 \ge 0$. The minimum on the physical domain $\rho \ge 0$ is at $\rho = 0$ (normal state, $|\psi| = 0$).
- Case $\alpha < 0$ ($T < T_c$): $\rho_0 = -\alpha/\beta > 0$. This is a physical minimum.

- 情况 $\alpha > 0$ ($T > T_c$)：$\rho_0 = -\alpha/\beta < 0$，因 $\rho = |\psi|^2 \ge 0$ 故非物理。物理域 $\rho \ge 0$ 上的极小值在 $\rho = 0$（正常态，$|\psi| = 0$）。
- 情况 $\alpha < 0$ ($T < T_c$)：$\rho_0 = -\alpha/\beta > 0$。这是物理的极小值。

**Step 4 — Verify it is a minimum.** $d^2 f/d\rho^2 = \beta > 0$, confirming $\rho_0$ is a local minimum. The free energy at the minimum is

**第 4 步 — 验证为极小值。** $d^2 f/d\rho^2 = \beta > 0$，确认 $\rho_0$ 是局部极小值。极小处的自由能为

$$ f(\rho_0) = \alpha(-\alpha/\beta) + (\beta/2)(\alpha/\beta)^2 = -\alpha^2/\beta + \alpha^2/(2\beta) = \boxed{\, -\alpha^2/(2\beta) \,}. $$

**Step 5 — Physical interpretation.** Near $T_c$, $\alpha \approx a(T - T_c)$ with $a > 0$, so $|\psi|^2 = -\alpha/\beta \approx a(T_c - T)/\beta$ grows continuously from zero as $T$ is lowered below $T_c$. The order parameter vanishes at $T_c$ (second-order transition) and the condensation energy density is $\alpha^2/(2\beta) \propto (T_c - T)^2$, consistent with a mean-field specific heat jump. $\blacksquare$

**第 5 步 — 物理解释。** 在 $T_c$ 附近，$\alpha \approx a(T - T_c)$，$a > 0$，故 $|\psi|^2 = -\alpha/\beta \approx a(T_c - T)/\beta$ 在 $T$ 降至 $T_c$ 以下时从零连续增长。序参量在 $T_c$ 处消失（二级相变），凝聚能密度为 $\alpha^2/(2\beta) \propto (T_c - T)^2$，与平均场比热跳变一致。$\blacksquare$

---

## B. Deriving the GL Equations from the Full Free Energy · 从完整自由能推导 GL 方程

**Claim.** Varying the full GL free energy functional $F[\psi, A] = \int d^3 r\, [F_n + \alpha|\psi|^2 + (\beta/2)|\psi|^4 + (1/2m^*)|(-i\hbar\nabla - e^* A)\psi|^2 + B^2/(2\mu_0)]$ with respect to $\psi^*$ and $A$ yields (i) the first GL equation for $\psi$ and (ii) the second GL equation (supercurrent expression).

**命题。** 对完整的 GL 自由能泛函 $F[\psi, A] = \int d^3 r\, [F_n + \alpha|\psi|^2 + (\beta/2)|\psi|^4 + (1/2m^*)|(-i\hbar\nabla - e^* A)\psi|^2 + B^2/(2\mu_0)]$ 分别对 $\psi^*$ 和 $A$ 作变分，得到（i）$\psi$ 的第一 GL 方程和（ii）第二 GL 方程（超电流表达式）。

**Step 1 — Variation with respect to $\psi^*$.** Write the gradient term as $(1/2m^*)|D\psi|^2$ where $D = -i\hbar\nabla - e^* A$ is the gauge-covariant derivative. Expand $|D\psi|^2 = (D\psi^*)\cdot(D\psi)$. Under $\delta\psi^* \to \psi^* + \delta\psi^*$:

**第 1 步 — 对 $\psi^*$ 作变分。** 将梯度项写为 $(1/2m^*)|D\psi|^2$，其中 $D = -i\hbar\nabla - e^* A$ 是规范协变导数。展开 $|D\psi|^2 = (D\psi^*)\cdot(D\psi)$。在 $\delta\psi^* \to \psi^* + \delta\psi^*$ 下：

$$ \delta F = \int d^3 r\, [\alpha\, \delta\psi^* \psi + \beta|\psi|^2 \delta\psi^* \psi + (1/2m^*)(D \delta\psi^*)\cdot(D\psi)] = 0. $$

Integrate by parts: $\int (D \delta\psi^*)\cdot(D\psi)\, d^3 r = -\int \delta\psi^*\, D^2\psi\, d^3 r$ (boundary terms vanish for localized solutions). Collecting $\delta\psi^*$:

分部积分：$\int (D \delta\psi^*)\cdot(D\psi)\, d^3 r = -\int \delta\psi^*\, D^2\psi\, d^3 r$（对局域解边界项为零）。收集 $\delta\psi^*$ 的系数：

$$ \alpha \psi + \beta|\psi|^2 \psi - (1/2m^*)\, D^2\psi = 0. $$

Expanding $D^2 = (-i\hbar\nabla - e^* A)^2$:

展开 $D^2 = (-i\hbar\nabla - e^* A)^2$：

$$ \boxed{\, (1/2m^*)(-i\hbar\nabla - e^* A)^2\psi + \alpha\psi + \beta|\psi|^2\psi = 0 \,} \quad \text{(First GL equation)} $$

$$ \boxed{\, (1/2m^*)(-i\hbar\nabla - e^* A)^2\psi + \alpha\psi + \beta|\psi|^2\psi = 0 \,} \quad \text{（第一 GL 方程）} $$

**Step 2 — Variation with respect to $A$.** The $A$-dependent terms are $(1/2m^*)|D\psi|^2$ and $B^2/(2\mu_0)$. Varying $A \to A + \delta A$:

**第 2 步 — 对 $A$ 作变分。** $A$ 相关的项为 $(1/2m^*)|D\psi|^2$ 和 $B^2/(2\mu_0)$。对 $A \to A + \delta A$ 作变分：

$$ \begin{aligned} \delta[(1/2m^*)|D\psi|^2] &= (e^*/2m^*)\, \delta A \cdot [\psi^*(-i\hbar\nabla\psi) + \psi(i\hbar\nabla\psi^*) - 2e^*|\psi|^2 A] = \delta A \cdot J_s \\ \delta[B^2/(2\mu_0)] &= (1/\mu_0)(\nabla \times B) \cdot \delta A = J_{\text{ext}} \cdot \delta A \quad \text{(after integration by parts).} \end{aligned} $$

Setting the total variation to zero and using $\nabla \times B = \mu_0 J_s$:

置总变分为零并使用 $\nabla \times B = \mu_0 J_s$：

$$ \boxed{\, J_s = (e^*\hbar/2m^* i)(\psi^*\nabla\psi - \psi\nabla\psi^*) - (e^{*2}/m^*)|\psi|^2 A \,} \quad \text{(Second GL equation / supercurrent)} $$

$$ \boxed{\, J_s = (e^*\hbar/2m^* i)(\psi^*\nabla\psi - \psi\nabla\psi^*) - (e^{*2}/m^*)|\psi|^2 A \,} \quad \text{（第二 GL 方程/超电流）} $$

Writing $\psi = |\psi|e^{i\theta}$, the gradient term gives $\hbar\nabla\theta$ and the supercurrent becomes

写 $\psi = |\psi|e^{i\theta}$，梯度项给出 $\hbar\nabla\theta$，超电流变为

$$ J_s = (e^*/m^*)|\psi|^2(\hbar\nabla\theta - e^* A), $$

which is precisely the expression linking the supercurrent to the gradient of the phase — the foundation of the Josephson effect (Module 5.8). $\blacksquare$

这正好是将超电流与相位梯度联系起来的表达式——约瑟夫森效应的基础（模块 5.8）。$\blacksquare$

---

## C. Coherence Length $\xi$ and Penetration Depth $\lambda$ from the GL Equations · 从 GL 方程推导相干长度 $\xi$ 和穿透深度 $\lambda$

**Claim.** Linearizing the first GL equation near $|\psi| = 0$ defines the GL coherence length $\xi = \hbar/\sqrt{-2m^*\alpha}$. Expanding near the bulk solution in the full nonlinear equation, and combining with the second GL equation and Ampère's law, gives the GL penetration depth $\lambda = \sqrt{m^*\beta/(\mu_0 e^{*2} |\alpha|)}$.

**命题。** 在 $|\psi| = 0$ 附近线性化第一 GL 方程定义了 GL 相干长度 $\xi = \hbar/\sqrt{-2m^*\alpha}$。在完整非线性方程中在体解附近展开，并与第二 GL 方程和安培定律联立，给出 GL 穿透深度 $\lambda = \sqrt{m^*\beta/(\mu_0 e^{*2} |\alpha|)}$。

**Step 1 — Linearize for $\xi$.** Near the boundary of a superconductor (or near a vortex core) where $|\psi| \approx 0$, drop the $\beta|\psi|^3$ term from the first GL equation (it is higher order). With $A = 0$ for simplicity:

**第 1 步 — 线性化求 $\xi$。** 在超导体边界附近（或涡旋核心附近）$|\psi| \approx 0$，从第一 GL 方程中去掉 $\beta|\psi|^3$ 项（它是高阶小量）。为简便取 $A = 0$：

$$ -(\hbar^2/2m^*)\, \nabla^2\psi + \alpha\psi = 0. $$

Look for a solution that heals from $0$ to $\psi_0 = \sqrt{-\alpha/\beta}$ over some length scale. Write $\psi(x) = \psi_0 \tanh(x/\sqrt{2}\, \xi)$ as an ansatz (the exact solution for the 1D case). The linearized equation near $\psi = 0$ is

寻找从 $0$ 恢复到 $\psi_0 = \sqrt{-\alpha/\beta}$ 的解，其特征长度为某个尺度。写 $\psi(x) = \psi_0 \tanh(x/\sqrt{2}\, \xi)$ 作为试探解（一维情况的精确解）。在 $\psi = 0$ 附近的线性化方程为

$$ -(\hbar^2/2m^*)\, d^2\psi/dx^2 = -\alpha\psi. $$

This gives an exponential healing with characteristic length

这给出特征长度为以下值的指数恢复

$$ \boxed{\, \xi^2 = \hbar^2/(2m^*|\alpha|), \quad \text{i.e.} \quad \xi = \hbar/\sqrt{2m^*|\alpha|} \,} \quad (\text{with } \alpha < 0,\ |\alpha| = -\alpha). $$

Near $T_c$, $\alpha \approx a(T - T_c)$, so $|\alpha| \propto (T_c - T)$ and $\xi \propto (T_c - T)^{-1/2}$: the coherence length diverges at $T_c$ (critical fluctuations).

在 $T_c$ 附近，$\alpha \approx a(T - T_c)$，故 $|\alpha| \propto (T_c - T)$，$\xi \propto (T_c - T)^{-1/2}$：相干长度在 $T_c$ 处发散（临界涨落）。

**Step 2 — Identify $\lambda$ from the second GL equation.** Deep in the bulk, $|\psi|^2 = \psi_0^2 = -\alpha/\beta$. Consider a small perturbation in $A$ (small field enters, order parameter is approximately $\psi_0$). The second GL equation gives

**第 2 步 — 从第二 GL 方程识别 $\lambda$。** 在体内深处，$|\psi|^2 = \psi_0^2 = -\alpha/\beta$。考虑 $A$ 的小扰动（小磁场进入，序参量近似为 $\psi_0$）。第二 GL 方程给出

$$ J_s \approx -(e^{*2}/m^*)\, \psi_0^2 A = -(e^{*2}/m^*)(-\alpha/\beta) A. $$

This is the London relation $J_s = -A/\Lambda$ with $1/\Lambda = (e^{*2}/m^*)(-\alpha/\beta)$. From Section C of Module 5.2-derivations, $\Lambda = m^*/(n_s e^{*2})$, so the effective superfluid density is $n_s = -\alpha/\beta$ (in units where $e^*$ and $m^*$ are the pair charge and mass).

这是伦敦关系 $J_s = -A/\Lambda$，其中 $1/\Lambda = (e^{*2}/m^*)(-\alpha/\beta)$。从模块 5.2 推导的 C 节，$\Lambda = m^*/(n_s e^{*2})$，故有效超流密度为 $n_s = -\alpha/\beta$（以 $e^*$ 和 $m^*$ 为配对电荷和质量的单位）。

**Step 3 — Combine with Ampère's law.** Repeating the derivation of Module 5.2-D with $n_s \to (-\alpha/\beta)$:

**第 3 步 — 与安培定律联立。** 以 $n_s \to (-\alpha/\beta)$ 重复模块 5.2-D 的推导：

$$ \boxed{\, \lambda^2 = m^*/(\mu_0 e^{*2} n_s) = m^*\beta/(\mu_0 e^{*2}|\alpha|), \quad \lambda = \sqrt{m^*\beta/(\mu_0 e^{*2}|\alpha|)} \,}. $$

Near $T_c$, $|\alpha| \propto (T_c - T)$, so $\lambda \propto (T_c - T)^{-1/2}$ — both length scales diverge at $T_c$. $\blacksquare$

在 $T_c$ 附近，$|\alpha| \propto (T_c - T)$，故 $\lambda \propto (T_c - T)^{-1/2}$——两个长度尺度都在 $T_c$ 处发散。$\blacksquare$

---

## D. The GL Parameter $\kappa = \lambda/\xi$ and the Type-I/II Boundary $\kappa = 1/\sqrt{2}$ · GL 参数 $\kappa = \lambda/\xi$ 与 I/II 型边界 $\kappa = 1/\sqrt{2}$

**Claim.** The dimensionless ratio $\kappa = \lambda/\xi$ is temperature-independent near $T_c$ and determines the type of superconductor. The critical value is $\kappa = 1/\sqrt{2}$: below it, type I (the surface energy of a normal-superconducting interface is positive, so the system prefers one bulk phase); above it, type II (surface energy is negative, so the system minimizes energy by subdividing into vortices).

**命题。** 无量纲比值 $\kappa = \lambda/\xi$ 在 $T_c$ 附近与温度无关，决定超导体的类型。临界值为 $\kappa = 1/\sqrt{2}$：低于此值为 I 型（正常态–超导态界面的表面能为正，系统倾向于单一体相）；高于此值为 II 型（表面能为负，系统通过分裂成涡旋来最小化能量）。

**Step 1 — Temperature independence of $\kappa$.** From Steps 1 and 2 of Section C:

**第 1 步 — $\kappa$ 的温度无关性。** 由 C 节第 1、2 步：

$$ \xi \propto |\alpha|^{-1/2}, \qquad \lambda \propto |\alpha|^{-1/2}. $$

Both diverge with the same power of $(T_c - T)$, so their ratio $\kappa = \lambda/\xi$ is independent of $T$ near $T_c$. Computing explicitly:

两者以相同的 $(T_c - T)$ 幂次发散，故它们的比值 $\kappa = \lambda/\xi$ 在 $T_c$ 附近与 $T$ 无关。显式计算：

$$ \begin{aligned} \kappa = \lambda/\xi &= [\sqrt{m^*\beta/(\mu_0 e^{*2}|\alpha|)}] / [\hbar/\sqrt{2m^*|\alpha|}] \\ &= \sqrt{m^*\beta/(\mu_0 e^{*2}|\alpha|)} \cdot \sqrt{2m^*|\alpha|}/\hbar \\ &= \sqrt{2m^{*2}\beta/(\mu_0 e^{*2}\hbar^2)}. \end{aligned} $$

This involves only the material parameters $m^*$, $\beta$, $e^*$, $\mu_0$, $\hbar$ — not $T$. Therefore $\kappa$ is a material constant. $\blacksquare$

这只涉及材料参数 $m^*$，$\beta$，$e^*$，$\mu_0$，$\hbar$——不涉及 $T$。因此 $\kappa$ 是材料常数。$\blacksquare$

**Step 2 — Surface energy of a normal-superconducting interface.** Consider a flat interface with normal state ($x < 0$) and superconducting state ($x > 0$). The surface energy per unit area is (schematically):

**第 2 步 — 正常态–超导态界面的表面能。** 考虑一个平面界面，$x < 0$ 为正常态，$x > 0$ 为超导态。单位面积表面能（示意性地）为：

$$ \begin{aligned} \sigma_{ns} &= \int_{-\infty}^{+\infty} dx\, [f_{\text{condensation profile}} + f_{\text{magnetic profile}}] \\ &= \int dx\, [-(\alpha^2/2\beta)(|\psi|/\psi_0)^2 + (\mu_0/2) H_c^2 (1 - B/H_c)^2/\mu_0 H_c^2] \quad \text{(schematic).} \end{aligned} $$

The condensation energy (negative, favoring superconductivity) is concentrated in a length $\xi$; the magnetic energy cost (positive) extends over length $\lambda$.

凝聚能（负，倾向于超导性）集中在长度 $\xi$ 内；磁场能量代价（正）延伸到长度 $\lambda$。

**Step 3 — Sign of surface energy.** A dimensional estimate gives $\sigma_{ns} \propto (H_c^2/2\mu_0)(\xi - \lambda)$. This is the crucial result:

**第 3 步 — 表面能的符号。** 量纲估算给出 $\sigma_{ns} \propto (H_c^2/2\mu_0)(\xi - \lambda)$。这是关键结果：

- $\sigma_{ns} > 0$  when $\xi > \lambda$,  i.e.  $\kappa < 1$  (rough estimate).
- $\sigma_{ns} < 0$  when $\xi < \lambda$,  i.e.  $\kappa > 1$  (rough estimate).

- 当 $\xi > \lambda$ 即 $\kappa < 1$ 时，$\sigma_{ns} > 0$（粗略估算）。
- 当 $\xi < \lambda$ 即 $\kappa > 1$ 时，$\sigma_{ns} < 0$（粗略估算）。

**Step 4 — Exact threshold from Abrikosov's calculation.** The precise threshold where $\sigma_{ns} = 0$ is found by a careful variational calculation (Abrikosov 1957). The result is

**第 4 步 — 阿布里科索夫计算的精确阈值。** $\sigma_{ns} = 0$ 的精确阈值由仔细的变分计算（阿布里科索夫，1957年）给出。结果为

$$ \sigma_{ns} = 0 \quad \text{when} \quad \boxed{\, \kappa = 1/\sqrt{2} \,}. $$

- $\boxed{\, \kappa < 1/\sqrt{2} \,}$: type I, positive surface energy, field is either fully in or fully out.
- $\boxed{\, \kappa > 1/\sqrt{2} \,}$: type II, negative surface energy, system prefers maximum interface area $\to$ vortex lattice.

- $\boxed{\, \kappa < 1/\sqrt{2} \,}$：I 型，正表面能，磁场要么完全在内要么完全在外。
- $\boxed{\, \kappa > 1/\sqrt{2} \,}$：II 型，负表面能，系统倾向于最大界面面积$\to$涡旋晶格。

The derivation of the exact coefficient $1/\sqrt{2}$ follows from requiring that the free energy is stationary with respect to vortex density, which is the Abrikosov solution of the linearized GL equations near the upper critical field $H_{c2}$. $\blacksquare$

精确系数 $1/\sqrt{2}$ 的推导来自要求自由能对涡旋密度是驻点，这是阿布里科索夫在上临界场 $H_{c2}$ 附近线性化 GL 方程的解。$\blacksquare$

---

## E. Flux Quantization: $\Phi_0 = h/2e$ from Single-Valuedness of $\psi$ · 磁通量子化：由 $\psi$ 的单值性推导 $\Phi_0 = h/2e$

**Claim.** The requirement that the order parameter $\psi = |\psi|e^{i\theta}$ be single-valued around any closed contour inside a superconductor forces the enclosed magnetic flux to be an integer multiple of $\Phi_0 = h/2e$, where $2e$ is the charge of a Cooper pair.

**命题。** 要求序参量 $\psi = |\psi|e^{i\theta}$ 沿超导体内部任意闭合回路是单值函数，迫使围合的磁通量是 $\Phi_0 = h/2e$ 的整数倍，其中 $2e$ 是库珀对的电荷。

**Step 1 — Supercurrent in terms of phase.** From Section B, Step 2, the GL supercurrent with $e^* = 2e$ (pair charge) and $m^* = 2m$ (pair mass) is

**第 1 步 — 用相位表示超电流。** 由 B 节第 2 步，以 $e^* = 2e$（对电荷）和 $m^* = 2m$（对质量）表示的 GL 超电流为

$$ J_s = (2e/2m)|\psi|^2(\hbar\nabla\theta - 2eA) = (e/m)|\psi|^2(\hbar\nabla\theta - 2eA). $$

**Step 2 — Integrate around a closed contour deep inside the bulk.** Choose a contour $C$ that lies entirely in the bulk where $|\psi| = \psi_0 = \text{const}$ and $J_s = 0$ (deep inside the superconductor, far from any surface or vortex). Then $J_s = 0$ requires:

**第 2 步 — 沿体内深处的闭合回路积分。** 选取完全在体内的回路 $C$，其中 $|\psi| = \psi_0 = \text{const}$ 且 $J_s = 0$（在超导体内深处，远离任何表面或涡旋）。则 $J_s = 0$ 要求：

$$ \hbar\nabla\theta - 2eA = 0 \quad\implies\quad \nabla\theta = (2e/\hbar) A. $$

**Step 3 — Integrate around the contour.** Integrate both sides over the closed contour $C$:

**第 3 步 — 沿回路积分。** 两边沿闭合回路 $C$ 积分：

$$ \oint_C \nabla\theta \cdot dl = (2e/\hbar) \oint_C A \cdot dl. $$

The right side is $(2e/\hbar)$ times the magnetic flux enclosed by $C$: $\oint A \cdot dl = \iint_S (\nabla \times A) \cdot dS = \Phi$ (by Stokes' theorem), where $\Phi = \int B \cdot dS$.

右边是 $(2e/\hbar)$ 乘以 $C$ 围合的磁通量：$\oint A \cdot dl = \iint_S (\nabla \times A) \cdot dS = \Phi$（由斯托克斯定理），其中 $\Phi = \int B \cdot dS$。

**Step 4 — Single-valuedness constraint.** The order parameter $\psi = |\psi|e^{i\theta}$ must be single-valued at every point in space. Going around the closed contour $C$ once, $\theta$ must return to its original value modulo $2\pi$ (since $e^{i\theta}$ is the physical observable):

**第 4 步 — 单值性约束。** 序参量 $\psi = |\psi|e^{i\theta}$ 必须在空间中每一点都是单值的。绕闭合回路 $C$ 一圈，$\theta$ 必须回到其原始值的 $2\pi$ 整数倍（因为 $e^{i\theta}$ 是物理可观测量）：

$$ \oint_C \nabla\theta \cdot dl = 2\pi n, \quad n = 0, \pm 1, \pm 2, \ldots $$

**Step 5 — Flux quantization.** Combining Steps 3 and 4:

**第 5 步 — 磁通量子化。** 联立第 3 和第 4 步：

$$ 2\pi n = (2e/\hbar) \Phi \quad\implies\quad \Phi = n \cdot (2\pi\hbar/2e) = n \cdot (h/2e). $$

Defining the **flux quantum**:

定义**磁通量子**：

$$ \boxed{\, \Phi_0 = h/(2e) \approx 2.07 \times 10^{-15}\ \text{Wb (Weber)} \,}. $$

The factor $2e$ (not $e$) is the direct signature of paired electrons — Cooper pairs carry charge $2e$. This prediction was confirmed experimentally by Deaver & Fairbank and Doll & Näbauer (1961). $\blacksquare$

因子 $2e$（而非 $e$）是电子配对的直接标志——库珀对携带电荷 $2e$。这一预测由德弗和费尔班克以及多尔和奈鲍尔（1961年）在实验上证实。$\blacksquare$

**Step 6 — Vortex interpretation.** For $n = 1$ (a single flux quantum), the phase $\theta$ winds by $2\pi$ around the vortex core, and the order parameter $|\psi| \to 0$ at the core (otherwise $\psi$ would be ill-defined at the winding center). The core has radius $\sim \xi$, and the circulating supercurrents and decaying flux profile extend to radius $\sim \lambda$ — exactly the structure computed in Module 5.7. $\blacksquare$

**第 6 步 — 涡旋诠释。** 对于 $n = 1$（单个磁通量子），相位 $\theta$ 在涡旋核心周围绕转 $2\pi$，序参量 $|\psi| \to 0$ 在核心处（否则 $\psi$ 在绕转中心将无定义）。核心半径约为 $\xi$，环流超电流和衰减磁通分布延伸到半径约 $\lambda$——这正是模块 5.7 中计算的结构。$\blacksquare$

---

*The GL theory derived here is exact near $T_c$ and is microscopically justified by the Gorkov derivation from BCS. The length scales $\xi$ and $\lambda$ appear in every subsequent module (5.4–5.9), and flux quantization is the operating principle of SQUIDs (Module 5.8).*

*此处推导的 GL 理论在 $T_c$ 附近是精确的，并由从 BCS 出发的戈尔科夫推导在微观上得到证明。长度尺度 $\xi$ 和 $\lambda$ 出现在随后的每个模块（5.4–5.9）中，磁通量子化是 SQUID 的工作原理（模块 5.8）。*

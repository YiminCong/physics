---
title: "Derivations — Module 2.2: Thermodynamic Potentials & Maxwell Relations"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 2.2: Thermodynamic Potentials & Maxwell Relations
# 推导 — 模块 2.2：热力学势与麦克斯韦关系

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.2](./module-2.2-thermodynamic-potentials.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.2](./module-2.2-thermodynamic-potentials.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Legendre Transforms: Deriving H, F, and G from U · 勒让德变换：从 U 推导 H、F 和 G

**Claim.** Starting from the fundamental relation $dU = T\, dS - P\, dV$, the enthalpy $H$, Helmholtz free energy $F$, and Gibbs free energy $G$ are obtained by Legendre transforms that swap natural variables while preserving all thermodynamic information.

**命题。** 从基本关系 $dU = T\, dS - P\, dV$ 出发，通过勒让德变换——在保留所有热力学信息的同时交换自然变量——得到焓 $H$、亥姆霍兹自由能 $F$ 和吉布斯自由能 $G$。

**Step 1 — Identify the natural variables of $U$.** The relation $dU = T\, dS - P\, dV$ shows that $U$ is a natural function of $(S, V)$: the partial derivatives read off immediately as

**第 1 步 — 确定 $U$ 的自然变量。** 关系式 $dU = T\, dS - P\, dV$ 表明 $U$ 是 $(S, V)$ 的自然函数，偏导数可直接读出：

$$ (\partial U/\partial S)_V = T, \qquad (\partial U/\partial V)_S = -P. $$

**Step 2 — Derive enthalpy $H$ by replacing $V$ with $P$.** Define $H = U + PV$. Then

**第 2 步 — 通过以 P 替换 V 推导焓 H。** 定义 $H = U + PV$，则

$$ dH = dU + P\, dV + V\, dP = (T\, dS - P\, dV) + P\, dV + V\, dP = T\, dS + V\, dP. $$

So $H$ is a natural function of $(S, P)$, with $(\partial H/\partial S)_P = T$ and $(\partial H/\partial P)_S = V$. The sign change in the $P$-term is the hallmark of a Legendre transform: we have traded the extensive variable $V$ for its conjugate intensive variable $P$.

故 $H$ 是 $(S, P)$ 的自然函数，$(\partial H/\partial S)_P = T$，$(\partial H/\partial P)_S = V$。$P$ 项的符号变化是勒让德变换的标志：我们用共轭强度变量 $P$ 替换了广延变量 $V$。

**Step 3 — Derive Helmholtz free energy $F$ by replacing $S$ with $T$.** Define $F = U - TS$. Then

**第 3 步 — 通过以 T 替换 S 推导亥姆霍兹自由能 F。** 定义 $F = U - TS$，则

$$ dF = dU - T\, dS - S\, dT = (T\, dS - P\, dV) - T\, dS - S\, dT = -S\, dT - P\, dV. $$

So $F$ is a natural function of $(T, V)$, with $(\partial F/\partial T)_V = -S$ and $(\partial F/\partial V)_T = -P$.

故 $F$ 是 $(T, V)$ 的自然函数，$(\partial F/\partial T)_V = -S$，$(\partial F/\partial V)_T = -P$。

**Step 4 — Derive Gibbs free energy $G$ by replacing both $S\to T$ and $V\to P$.** Define $G = U - TS + PV = H - TS = F + PV$. Then

**第 4 步 — 同时以 $S\to T$ 和 $V\to P$ 推导吉布斯自由能 G。** 定义 $G = U - TS + PV = H - TS = F + PV$，则

$$ \begin{aligned} dG &= dU - T\, dS - S\, dT + P\, dV + V\, dP \\ &= (T\, dS - P\, dV) - T\, dS - S\, dT + P\, dV + V\, dP \\ &= -S\, dT + V\, dP. \end{aligned} $$

So $G$ is a natural function of $(T, P)$, with $(\partial G/\partial T)_P = -S$ and $(\partial G/\partial P)_T = V$. $\blacksquare$

故 $G$ 是 $(T, P)$ 的自然函数，$(\partial G/\partial T)_P = -S$，$(\partial G/\partial P)_T = V$。$\blacksquare$

**Step 5 — Which potential is minimized under which constraint?** The Second Law in the form $dS \ge \delta Q/T$, combined with the First Law $dU = \delta Q - P\, dV$, determines the appropriate equilibrium condition for each set of constraints:

**第 5 步 — 哪个热力学势在何种约束下取极小值？** 第二定律的形式 $dS \ge \delta Q/T$ 与第一定律 $dU = \delta Q - P\, dV$ 相结合，确定了每组约束条件下的适当平衡条件：

- Fixed $(S, V)$: $dU \le 0$ at equilibrium $\to$ **U is minimized**.
- Fixed $(S, P)$: $dH \le 0$ at equilibrium $\to$ **H is minimized**.
- Fixed $(T, V)$: $dF \le 0$ at equilibrium $\to$ **F is minimized** (since $dF = dU - T\, dS - S\, dT$ and at fixed $T$, $dF = dU - T\, dS \le 0$ from $dU \le T\, dS$ when no work is done).
- Fixed $(T, P)$: $dG \le 0$ at equilibrium $\to$ **G is minimized** (the most common laboratory condition: constant temperature and pressure). $\blacksquare$

- 固定 $(S, V)$：平衡时 $dU \le 0$ $\to$ **U 取极小值**。
- 固定 $(S, P)$：平衡时 $dH \le 0$ $\to$ **H 取极小值**。
- 固定 $(T, V)$：平衡时 $dF \le 0$ $\to$ **F 取极小值**（因为 $dF = dU - T\, dS - S\, dT$，在固定 $T$ 时 $dF = dU - T\, dS \le 0$，由无功时 $dU \le T\, dS$ 得出）。
- 固定 $(T, P)$：平衡时 $dG \le 0$ $\to$ **G 取极小值**（最常见的实验室条件：恒温恒压）。$\blacksquare$

---

## B. The Four Maxwell Relations from Exactness of Mixed Partials · 从混合偏导数相等推导四个麦克斯韦关系

**Claim.** Since $U, H, F, G$ are each exact differentials (state functions), the equality of mixed second partial derivatives (Schwarz's theorem) applied to each yields one Maxwell relation. There are four such relations.

**命题。** 由于 $U$、$H$、$F$、$G$ 均为恰当微分（态函数），对每一个应用混合二阶偏导数相等（施瓦茨定理）可得一个麦克斯韦关系，共得四个关系。

**Step 1 — Maxwell relation from $U$.** We have $dU = T\, dS - P\, dV$, so $(\partial U/\partial S)_V = T$ and $(\partial U/\partial V)_S = -P$. Schwarz's theorem requires

**第 1 步 — 由 U 得麦克斯韦关系。** $dU = T\, dS - P\, dV$，故 $(\partial U/\partial S)_V = T$，$(\partial U/\partial V)_S = -P$。施瓦茨定理要求

$$ \partial/\partial V\,[(\partial U/\partial S)_V]_S = \partial/\partial S\,[(\partial U/\partial V)_S]_V, $$
$$ \text{i.e., } (\partial T/\partial V)_S = (\partial(-P)/\partial S)_V, $$

giving the first Maxwell relation:

由此得第一个麦克斯韦关系：

$$ \boxed{\, (\partial T/\partial V)_S = -(\partial P/\partial S)_V. \,} $$

**Step 2 — Maxwell relation from $H$.** We have $dH = T\, dS + V\, dP$, so $(\partial H/\partial S)_P = T$ and $(\partial H/\partial P)_S = V$. Schwarz's theorem gives

**第 2 步 — 由 H 得麦克斯韦关系。** $dH = T\, dS + V\, dP$，故 $(\partial H/\partial S)_P = T$，$(\partial H/\partial P)_S = V$。施瓦茨定理给出

$$ \partial/\partial P\,[(\partial H/\partial S)_P]_S = \partial/\partial S\,[(\partial H/\partial P)_S]_P, $$
$$ \text{i.e., } (\partial T/\partial P)_S = (\partial V/\partial S)_P, $$

giving the second Maxwell relation:

由此得第二个麦克斯韦关系：

$$ \boxed{\, (\partial T/\partial P)_S = (\partial V/\partial S)_P. \,} $$

**Step 3 — Maxwell relation from $F$.** We have $dF = -S\, dT - P\, dV$, so $(\partial F/\partial T)_V = -S$ and $(\partial F/\partial V)_T = -P$. Schwarz's theorem gives

**第 3 步 — 由 F 得麦克斯韦关系。** $dF = -S\, dT - P\, dV$，故 $(\partial F/\partial T)_V = -S$，$(\partial F/\partial V)_T = -P$。施瓦茨定理给出

$$ \partial/\partial V\,[(\partial F/\partial T)_V]_T = \partial/\partial T\,[(\partial F/\partial V)_T]_V, $$
$$ \text{i.e., } (\partial(-S)/\partial V)_T = (\partial(-P)/\partial T)_V, $$

giving the third Maxwell relation:

由此得第三个麦克斯韦关系：

$$ \boxed{\, (\partial S/\partial V)_T = (\partial P/\partial T)_V. \,} $$

**Step 4 — Maxwell relation from $G$.** We have $dG = -S\, dT + V\, dP$, so $(\partial G/\partial T)_P = -S$ and $(\partial G/\partial P)_T = V$. Schwarz's theorem gives

**第 4 步 — 由 G 得麦克斯韦关系。** $dG = -S\, dT + V\, dP$，故 $(\partial G/\partial T)_P = -S$，$(\partial G/\partial P)_T = V$。施瓦茨定理给出

$$ \partial/\partial P\,[(\partial G/\partial T)_P]_T = \partial/\partial T\,[(\partial G/\partial P)_T]_P, $$
$$ \text{i.e., } (\partial(-S)/\partial P)_T = (\partial V/\partial T)_P, $$

giving the fourth Maxwell relation:

由此得第四个麦克斯韦关系：

$$ \boxed{\, (\partial S/\partial P)_T = -(\partial V/\partial T)_P. \,} \qquad \blacksquare $$

**Step 5 — Physical use of the Maxwell relations.** The power of the Maxwell relations is converting thermodynamically inaccessible derivatives into measurable ones. Consider $(\partial S/\partial P)_T = -(\partial V/\partial T)_P$. The left side is the change in entropy with pressure at fixed temperature — entropy cannot be measured directly. The right side is $-V\alpha$, where $\alpha = (1/V)(\partial V/\partial T)_P$ is the thermal expansion coefficient, a standard tabulated quantity. Therefore

**第 5 步 — 麦克斯韦关系的物理用途。** 麦克斯韦关系的强大之处在于将热力学上不可直接测量的偏导数转化为可测量量。考虑 $(\partial S/\partial P)_T = -(\partial V/\partial T)_P$。左侧是在固定温度下熵随压强的变化——熵无法直接测量。右侧为 $-V\alpha$，其中 $\alpha = (1/V)(\partial V/\partial T)_P$ 是热膨胀系数，是标准的可查表量。因此

$$ dS = (\partial S/\partial T)_P\, dT + (\partial S/\partial P)_T\, dP = (C_P/T)\, dT - V\alpha\, dP, $$

making every entropy change computable from $C_P$ and $\alpha$ — both measurable calorimetrically and dilatometrically. $\blacksquare$

使得每个熵变都可以由 $C_P$ 和 $\alpha$ 计算——两者均可通过量热法和膨胀测量法直接测量。$\blacksquare$

---

## C. Clausius–Clapeyron Equation from G · 从 G 推导克劳修斯–克拉珀龙方程

**Claim.** Along a phase coexistence curve in the $(T, P)$ plane, the slope is $dP/dT = L/(T\, \Delta V)$, where $L$ is the latent heat and $\Delta V$ is the volume change on crossing the phase boundary.

**命题。** 沿 $(T, P)$ 平面中的相共存曲线，斜率为 $dP/dT = L/(T\, \Delta V)$，其中 $L$ 为潜热，$\Delta V$ 为穿越相界面时的体积变化。

**Step 1 — Equilibrium condition.** Two phases $\alpha$ and $\beta$ coexist when their chemical potentials (molar Gibbs free energies) are equal:

**第 1 步 — 平衡条件。** 两相 $\alpha$ 和 $\beta$ 共存当且仅当其化学势（摩尔吉布斯自由能）相等：

$$ G_\alpha(T, P) = G_\beta(T, P). $$

**Step 2 — Differentiate along the coexistence curve.** Differentiating both sides along the coexistence curve where $dG_\alpha = dG_\beta$:

**第 2 步 — 沿共存曲线微分。** 沿共存曲线微分，其中 $dG_\alpha = dG_\beta$：

$$ -S_\alpha\, dT + V_\alpha\, dP = -S_\beta\, dT + V_\beta\, dP. $$

**Step 3 — Rearrange.** Collecting terms:

**第 3 步 — 整理。** 整理各项：

$$ (V_\alpha - V_\beta)\, dP = (S_\alpha - S_\beta)\, dT, $$
$$ dP/dT = (S_\alpha - S_\beta)/(V_\alpha - V_\beta) = \Delta S/\Delta V. $$

**Step 4 — Express $\Delta S$ in terms of latent heat.** The latent heat absorbed when transitioning from $\beta$ to $\alpha$ at temperature $T$ is $L = T\, \Delta S$, so $\Delta S = L/T$. Substituting:

**第 4 步 — 用潜热表示 $\Delta S$。** 在温度 $T$ 从 $\beta$ 相转变为 $\alpha$ 相时吸收的潜热为 $L = T\, \Delta S$，故 $\Delta S = L/T$。代入：

$$ \boxed{\, dP/dT = L / (T\, \Delta V). \,} \qquad \blacksquare $$

This is the Clausius–Clapeyron equation. For the liquid–gas transition, $\Delta V \approx k_B T/P$ (ideal gas approximation for the vapor), giving $dP/dT \approx LP/(k_B T^2)$, which integrates to $P \propto e^{-L/k_B T}$ — the Arrhenius-type vapor-pressure formula.

这就是克劳修斯–克拉珀龙方程。对于液–气相变，$\Delta V \approx k_B T/P$（蒸气的理想气体近似），给出 $dP/dT \approx LP/(k_B T^2)$，积分得 $P \propto e^{-L/k_B T}$——即阿伦尼乌斯型蒸气压公式。

---

*The Legendre transform machinery, the four Maxwell relations, and the Clausius–Clapeyron equation together constitute the complete formal apparatus of equilibrium classical thermodynamics. Every subsequent module — quantum statistics (2.5), phase transitions (2.3), transport (2.7) — takes these as established tools.*

*勒让德变换机制、四个麦克斯韦关系以及克劳修斯–克拉珀龙方程共同构成了平衡经典热力学的完整形式体系。此后每个模块——量子统计（2.5）、相变（2.3）、输运（2.7）——均将这些作为既定工具使用。*

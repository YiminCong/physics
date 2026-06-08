# Derivations — Module 2.2: Thermodynamic Potentials & Maxwell Relations
# 推导 — 模块 2.2：热力学势与麦克斯韦关系

> Companion to [Module 2.2](./module-2.2-thermodynamic-potentials.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.2](./module-2.2-thermodynamic-potentials.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Legendre Transforms: Deriving H, F, and G from U · 勒让德变换：从 U 推导 H、F 和 G

**Claim.** Starting from the fundamental relation dU = T dS − P dV, the enthalpy H, Helmholtz free energy F, and Gibbs free energy G are obtained by Legendre transforms that swap natural variables while preserving all thermodynamic information.

**命题。** 从基本关系 dU = T dS − P dV 出发，通过勒让德变换——在保留所有热力学信息的同时交换自然变量——得到焓 H、亥姆霍兹自由能 F 和吉布斯自由能 G。

**Step 1 — Identify the natural variables of U.** The relation dU = T dS − P dV shows that U is a natural function of (S, V): the partial derivatives read off immediately as

**第 1 步 — 确定 U 的自然变量。** 关系式 dU = T dS − P dV 表明 U 是 (S, V) 的自然函数，偏导数可直接读出：

  (∂U/∂S)_V = T,     (∂U/∂V)_S = −P.

**Step 2 — Derive enthalpy H by replacing V with P.** Define H = U + PV. Then

**第 2 步 — 通过以 P 替换 V 推导焓 H。** 定义 H = U + PV，则

  dH = dU + P dV + V dP = (T dS − P dV) + P dV + V dP = T dS + V dP.

So H is a natural function of (S, P), with (∂H/∂S)_P = T and (∂H/∂P)_S = V. The sign change in the P-term is the hallmark of a Legendre transform: we have traded the extensive variable V for its conjugate intensive variable P.

故 H 是 (S, P) 的自然函数，(∂H/∂S)_P = T，(∂H/∂P)_S = V。P 项的符号变化是勒让德变换的标志：我们用共轭强度变量 P 替换了广延变量 V。

**Step 3 — Derive Helmholtz free energy F by replacing S with T.** Define F = U − TS. Then

**第 3 步 — 通过以 T 替换 S 推导亥姆霍兹自由能 F。** 定义 F = U − TS，则

  dF = dU − T dS − S dT = (T dS − P dV) − T dS − S dT = −S dT − P dV.

So F is a natural function of (T, V), with (∂F/∂T)_V = −S and (∂F/∂V)_T = −P.

故 F 是 (T, V) 的自然函数，(∂F/∂T)_V = −S，(∂F/∂V)_T = −P。

**Step 4 — Derive Gibbs free energy G by replacing both S→T and V→P.** Define G = U − TS + PV = H − TS = F + PV. Then

**第 4 步 — 同时以 S→T 和 V→P 推导吉布斯自由能 G。** 定义 G = U − TS + PV = H − TS = F + PV，则

  dG = dU − T dS − S dT + P dV + V dP
     = (T dS − P dV) − T dS − S dT + P dV + V dP
     = −S dT + V dP.

So G is a natural function of (T, P), with (∂G/∂T)_P = −S and (∂G/∂P)_T = V. ∎

故 G 是 (T, P) 的自然函数，(∂G/∂T)_P = −S，(∂G/∂P)_T = V。∎

**Step 5 — Which potential is minimized under which constraint?** The Second Law in the form dS ≥ δQ/T, combined with the First Law dU = δQ − P dV, determines the appropriate equilibrium condition for each set of constraints:

**第 5 步 — 哪个热力学势在何种约束下取极小值？** 第二定律的形式 dS ≥ δQ/T 与第一定律 dU = δQ − P dV 相结合，确定了每组约束条件下的适当平衡条件：

  - Fixed (S, V): dU ≤ 0 at equilibrium → **U is minimized**.
  - Fixed (S, P): dH ≤ 0 at equilibrium → **H is minimized**.
  - Fixed (T, V): dF ≤ 0 at equilibrium → **F is minimized** (since dF = dU − T dS − S dT and at fixed T, dF = dU − T dS ≤ 0 from dU ≤ T dS when no work is done).
  - Fixed (T, P): dG ≤ 0 at equilibrium → **G is minimized** (the most common laboratory condition: constant temperature and pressure). ∎

  - 固定 (S, V)：平衡时 dU ≤ 0 → **U 取极小值**。
  - 固定 (S, P)：平衡时 dH ≤ 0 → **H 取极小值**。
  - 固定 (T, V)：平衡时 dF ≤ 0 → **F 取极小值**（因为 dF = dU − T dS − S dT，在固定 T 时 dF = dU − T dS ≤ 0，由无功时 dU ≤ T dS 得出）。
  - 固定 (T, P)：平衡时 dG ≤ 0 → **G 取极小值**（最常见的实验室条件：恒温恒压）。∎

---

## B. The Four Maxwell Relations from Exactness of Mixed Partials · 从混合偏导数相等推导四个麦克斯韦关系

**Claim.** Since U, H, F, G are each exact differentials (state functions), the equality of mixed second partial derivatives (Schwarz's theorem) applied to each yields one Maxwell relation. There are four such relations.

**命题。** 由于 U、H、F、G 均为恰当微分（态函数），对每一个应用混合二阶偏导数相等（施瓦茨定理）可得一个麦克斯韦关系，共得四个关系。

**Step 1 — Maxwell relation from U.** We have dU = T dS − P dV, so (∂U/∂S)_V = T and (∂U/∂V)_S = −P. Schwarz's theorem requires

**第 1 步 — 由 U 得麦克斯韦关系。** dU = T dS − P dV，故 (∂U/∂S)_V = T，(∂U/∂V)_S = −P。施瓦茨定理要求

  ∂/∂V [(∂U/∂S)_V]_S = ∂/∂S [(∂U/∂V)_S]_V,
  i.e., (∂T/∂V)_S = (∂(−P)/∂S)_V,

giving the first Maxwell relation:

由此得第一个麦克斯韦关系：

  **(∂T/∂V)_S = −(∂P/∂S)_V.**

**Step 2 — Maxwell relation from H.** We have dH = T dS + V dP, so (∂H/∂S)_P = T and (∂H/∂P)_S = V. Schwarz's theorem gives

**第 2 步 — 由 H 得麦克斯韦关系。** dH = T dS + V dP，故 (∂H/∂S)_P = T，(∂H/∂P)_S = V。施瓦茨定理给出

  ∂/∂P [(∂H/∂S)_P]_S = ∂/∂S [(∂H/∂P)_S]_P,
  i.e., (∂T/∂P)_S = (∂V/∂S)_P,

giving the second Maxwell relation:

由此得第二个麦克斯韦关系：

  **(∂T/∂P)_S = (∂V/∂S)_P.**

**Step 3 — Maxwell relation from F.** We have dF = −S dT − P dV, so (∂F/∂T)_V = −S and (∂F/∂V)_T = −P. Schwarz's theorem gives

**第 3 步 — 由 F 得麦克斯韦关系。** dF = −S dT − P dV，故 (∂F/∂T)_V = −S，(∂F/∂V)_T = −P。施瓦茨定理给出

  ∂/∂V [(∂F/∂T)_V]_T = ∂/∂T [(∂F/∂V)_T]_V,
  i.e., (∂(−S)/∂V)_T = (∂(−P)/∂T)_V,

giving the third Maxwell relation:

由此得第三个麦克斯韦关系：

  **(∂S/∂V)_T = (∂P/∂T)_V.**

**Step 4 — Maxwell relation from G.** We have dG = −S dT + V dP, so (∂G/∂T)_P = −S and (∂G/∂P)_T = V. Schwarz's theorem gives

**第 4 步 — 由 G 得麦克斯韦关系。** dG = −S dT + V dP，故 (∂G/∂T)_P = −S，(∂G/∂P)_T = V。施瓦茨定理给出

  ∂/∂P [(∂G/∂T)_P]_T = ∂/∂T [(∂G/∂P)_T]_P,
  i.e., (∂(−S)/∂P)_T = (∂V/∂T)_P,

giving the fourth Maxwell relation:

由此得第四个麦克斯韦关系：

  **(∂S/∂P)_T = −(∂V/∂T)_P.** ∎

**Step 5 — Physical use of the Maxwell relations.** The power of the Maxwell relations is converting thermodynamically inaccessible derivatives into measurable ones. Consider (∂S/∂P)_T = −(∂V/∂T)_P. The left side is the change in entropy with pressure at fixed temperature — entropy cannot be measured directly. The right side is −V α, where α = (1/V)(∂V/∂T)_P is the thermal expansion coefficient, a standard tabulated quantity. Therefore

**第 5 步 — 麦克斯韦关系的物理用途。** 麦克斯韦关系的强大之处在于将热力学上不可直接测量的偏导数转化为可测量量。考虑 (∂S/∂P)_T = −(∂V/∂T)_P。左侧是在固定温度下熵随压强的变化——熵无法直接测量。右侧为 −V α，其中 α = (1/V)(∂V/∂T)_P 是热膨胀系数，是标准的可查表量。因此

  dS = (∂S/∂T)_P dT + (∂S/∂P)_T dP = (C_P/T) dT − V α dP,

making every entropy change computable from C_P and α — both measurable calorimetrically and dilatometrically. ∎

使得每个熵变都可以由 C_P 和 α 计算——两者均可通过量热法和膨胀测量法直接测量。∎

---

## C. Clausius–Clapeyron Equation from G · 从 G 推导克劳修斯–克拉珀龙方程

**Claim.** Along a phase coexistence curve in the (T, P) plane, the slope is dP/dT = L/(T ΔV), where L is the latent heat and ΔV is the volume change on crossing the phase boundary.

**命题。** 沿 (T, P) 平面中的相共存曲线，斜率为 dP/dT = L/(T ΔV)，其中 L 为潜热，ΔV 为穿越相界面时的体积变化。

**Step 1 — Equilibrium condition.** Two phases α and β coexist when their chemical potentials (molar Gibbs free energies) are equal:

**第 1 步 — 平衡条件。** 两相 α 和 β 共存当且仅当其化学势（摩尔吉布斯自由能）相等：

  G_α(T, P) = G_β(T, P).

**Step 2 — Differentiate along the coexistence curve.** Differentiating both sides along the coexistence curve where dG_α = dG_β:

**第 2 步 — 沿共存曲线微分。** 沿共存曲线微分，其中 dG_α = dG_β：

  −S_α dT + V_α dP = −S_β dT + V_β dP.

**Step 3 — Rearrange.** Collecting terms:

**第 3 步 — 整理。** 整理各项：

  (V_α − V_β) dP = (S_α − S_β) dT,
  dP/dT = (S_α − S_β)/(V_α − V_β) = ΔS/ΔV.

**Step 4 — Express ΔS in terms of latent heat.** The latent heat absorbed when transitioning from β to α at temperature T is L = T ΔS, so ΔS = L/T. Substituting:

**第 4 步 — 用潜热表示 ΔS。** 在温度 T 从 β 相转变为 α 相时吸收的潜热为 L = T ΔS，故 ΔS = L/T。代入：

  **dP/dT = L / (T ΔV).** ∎

This is the Clausius–Clapeyron equation. For the liquid–gas transition, ΔV ≈ k_BT/P (ideal gas approximation for the vapor), giving dP/dT ≈ LP/(k_BT²), which integrates to P ∝ e^{−L/k_BT} — the Arrhenius-type vapor-pressure formula.

这就是克劳修斯–克拉珀龙方程。对于液–气相变，ΔV ≈ k_BT/P（蒸气的理想气体近似），给出 dP/dT ≈ LP/(k_BT²)，积分得 P ∝ e^{−L/k_BT}——即阿伦尼乌斯型蒸气压公式。

---

*The Legendre transform machinery, the four Maxwell relations, and the Clausius–Clapeyron equation together constitute the complete formal apparatus of equilibrium classical thermodynamics. Every subsequent module — quantum statistics (2.5), phase transitions (2.3), transport (2.7) — takes these as established tools.*

*勒让德变换机制、四个麦克斯韦关系以及克劳修斯–克拉珀龙方程共同构成了平衡经典热力学的完整形式体系。此后每个模块——量子统计（2.5）、相变（2.3）、输运（2.7）——均将这些作为既定工具使用。*

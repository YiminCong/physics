# Derivations — Module 9.1: Electronics
# 推导 — 模块 9.1：电子学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.1](./module-9.1-electronics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.1](./module-9.1-electronics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. RLC Resonance Frequency and Quality Factor · RLC 谐振频率与品质因数

**Claim.** For a series RLC circuit driven at angular frequency ω, the resonance frequency is ω₀ = 1/√(LC) and the quality factor is Q = ω₀L/R = (1/R)√(L/C).

**命题。** 对于在角频率 ω 下驱动的串联 RLC 电路，谐振频率为 ω₀ = 1/√(LC)，品质因数为 Q = ω₀L/R = (1/R)√(L/C)。

**Step 1 — Write the circuit equation.** Apply KVL around the loop with applied EMF V(t) = V₀ e^{iωt}:

**第 1 步 — 写出电路方程。** 对施加 EMF V(t) = V₀ e^{iωt} 的回路应用 KVL：

  L dI/dt + RI + Q/C = V₀ e^{iωt},  with  I = dQ/dt.

Substituting the phasor ansatz I = Ĩ e^{iωt}:

代入相量假设 I = Ĩ e^{iωt}：

  (iωL + R + 1/(iωC)) Ĩ = V₀.

**Step 2 — Identify the total impedance.** The complex impedance is:

**第 2 步 — 识别总阻抗。** 复数阻抗为：

  Z(ω) = R + i(ωL − 1/(ωC)).

The imaginary part is called the **reactance** X(ω) = ωL − 1/(ωC). The current amplitude |Ĩ| = V₀/|Z| = V₀/√(R² + X²) is maximized when X = 0.

虚部称为**电抗** X(ω) = ωL − 1/(ωC)。电流幅值 |Ĩ| = V₀/|Z| = V₀/√(R² + X²) 在 X = 0 时取最大值。

**Step 3 — Find the resonance frequency.** Setting X(ω₀) = 0:

**第 3 步 — 求谐振频率。** 令 X(ω₀) = 0：

  ω₀L = 1/(ω₀C)  ⟹  ω₀² = 1/(LC)  ⟹  **ω₀ = 1/√(LC)**.

At this frequency Z(ω₀) = R (purely real) and |Ĩ| = V₀/R, the maximum possible current for a given V₀.

在此频率下 Z(ω₀) = R（纯实数），|Ĩ| = V₀/R，是给定 V₀ 下可能的最大电流。

**Step 4 — Derive the bandwidth.** The **half-power points** ω₁, ω₂ are where |Z|² = 2R² (power is halved relative to resonance):

**第 4 步 — 推导带宽。** **半功率点** ω₁、ω₂ 是 |Z|² = 2R²（功率相对于谐振减半）处：

  R² + (ωL − 1/(ωC))² = 2R²  ⟹  ωL − 1/(ωC) = ±R.

For the positive root: ω₂L − 1/(ω₂C) = +R. For the negative root: ω₁L − 1/(ω₁C) = −R. Subtracting (and using ω₁ω₂ ≈ ω₀² for narrow resonances): Δω = ω₂ − ω₁ = R/L.

对正根：ω₂L − 1/(ω₂C) = +R。对负根：ω₁L − 1/(ω₁C) = −R。相减（对窄谐振使用 ω₁ω₂ ≈ ω₀²）：Δω = ω₂ − ω₁ = R/L。

**Step 5 — Define Q.** The quality factor is the ratio of resonance frequency to bandwidth:

**第 5 步 — 定义 Q。** 品质因数是谐振频率与带宽之比：

  **Q = ω₀/Δω = ω₀L/R**.

Substituting ω₀ = 1/√(LC):

代入 ω₀ = 1/√(LC)：

  **Q = (1/R)√(L/C)**.

Q also equals 2π times the ratio of energy stored to energy dissipated per cycle: Q = 2π × (½LI₀²) / (½RI₀² · 2π/ω₀) = ω₀L/R, consistent. ∎

Q 还等于 2π 乘以每周期储存能量与耗散能量之比：Q = 2π × (½LI₀²) / (½RI₀² · 2π/ω₀) = ω₀L/R，结果一致。∎

---

## B. Shockley Diode Equation from the Depletion Region · 从耗尽区推导肖克利二极管方程

**Claim.** For an ideal abrupt p–n junction with applied voltage V, the current is I = I_s(e^{eV/k_BT} − 1), where I_s = Aeni²(D_p/(L_p N_D) + D_n/(L_n N_A)) and A is the junction area, n_i the intrinsic carrier density, D_p, D_n the minority-carrier diffusivities, L_p, L_n their diffusion lengths, N_D and N_A the donor and acceptor concentrations.

**命题。** 对于施加电压 V 的理想突变 p-n 结，电流为 I = I_s(e^{eV/k_BT} − 1)，其中 I_s = Aeni²(D_p/(L_p N_D) + D_n/(L_n N_A))，A 为结面积，n_i 为本征载流子密度，D_p、D_n 为少数载流子扩散系数，L_p、L_n 为扩散长度，N_D、N_A 为施主和受主浓度。

**Step 1 — Equilibrium depletion region.** In thermal equilibrium, diffusion current (driven by concentration gradient) balances drift current (driven by the built-in field E_bi). The built-in potential satisfies:

**第 1 步 — 平衡耗尽区。** 在热平衡中，扩散电流（由浓度梯度驱动）与漂移电流（由内建电场 E_bi 驱动）平衡。内建电势满足：

  e V_bi = k_BT ln(N_A N_D / n_i²).

This follows from setting the net electron (or hole) current to zero: J_n = eμ_n n E + eD_n dn/dx = 0, integrating across the depletion region with the Einstein relation D_n = μ_n k_BT/e.

这由将净电子（或空穴）电流设为零得到：J_n = eμ_n n E + eD_n dn/dx = 0，利用爱因斯坦关系 D_n = μ_n k_BT/e 在耗尽区积分。

**Step 2 — Applied voltage shifts the barrier.** A forward bias V reduces the electrostatic barrier to e(V_bi − V), while reverse bias V < 0 increases it. The majority carrier density at the depletion-region edge on the n-side is n_n ≈ N_D; using the Boltzmann factor for the minority holes on the n-side:

**第 2 步 — 外加电压改变势垒。** 正向偏置 V 将静电势垒降低至 e(V_bi − V)，而反向偏置 V < 0 则使其增大。n 侧耗尽区边缘的多数载流子密度为 n_n ≈ N_D；利用玻尔兹曼因子得 n 侧少数空穴为：

  p_n(V) = p_{n0} e^{eV/k_BT},

where p_{n0} = n_i²/N_D is the equilibrium minority hole density. This is the **law of the junction** (or boundary condition for minority carriers).

其中 p_{n0} = n_i²/N_D 为平衡少数空穴密度。这是**结定律**（少数载流子的边界条件）。

**Step 3 — Minority-carrier diffusion in the neutral regions.** In the neutral n-region (x > x_n), excess minority holes Δp(x) = p_n(x) − p_{n0} satisfy the steady-state minority-carrier diffusion equation:

**第 3 步 — 中性区少数载流子扩散。** 在中性 n 区（x > x_n），过剩少数空穴 Δp(x) = p_n(x) − p_{n0} 满足稳态少数载流子扩散方程：

  D_p d²(Δp)/dx² − Δp/τ_p = 0,

where τ_p is the minority hole lifetime. This is solved by Δp(x) ∝ e^{−(x−x_n)/L_p} with diffusion length L_p = √(D_p τ_p). Applying the junction boundary condition at x = x_n (Step 2) and Δp → 0 as x → ∞:

其中 τ_p 为少数空穴寿命。解为 Δp(x) ∝ e^{−(x−x_n)/L_p}，扩散长度 L_p = √(D_p τ_p)。在 x = x_n 处应用结边界条件（第 2 步），并利用 x → ∞ 时 Δp → 0：

  Δp(x) = p_{n0}(e^{eV/k_BT} − 1) e^{−(x−x_n)/L_p}.

**Step 4 — Compute the hole current.** The hole diffusion current at the edge x = x_n is:

**第 4 步 — 计算空穴电流。** 在 x = x_n 处的空穴扩散电流为：

  J_p = −eD_p d(Δp)/dx |_{x=x_n} = (eD_p p_{n0}/L_p)(e^{eV/k_BT} − 1).

A symmetric calculation for electron current injected into the p-side gives J_n = (eD_n n_{p0}/L_n)(e^{eV/k_BT} − 1), with n_{p0} = n_i²/N_A.

对注入 p 侧的电子电流进行对称计算给出 J_n = (eD_n n_{p0}/L_n)(e^{eV/k_BT} − 1)，其中 n_{p0} = n_i²/N_A。

**Step 5 — Total current.** The total current density J = J_p + J_n; multiplying by junction area A:

**第 5 步 — 总电流。** 总电流密度 J = J_p + J_n；乘以结面积 A：

  **I = I_s (e^{eV/k_BT} − 1)**,

with **I_s = Ae n_i² (D_p/(L_p N_D) + D_n/(L_n N_A))**.

其中 **I_s = Ae n_i² (D_p/(L_p N_D) + D_n/(L_n N_A))**。

For V ≫ k_BT/e the exponential dominates (forward conduction); for V ≪ 0 the current saturates at −I_s (reverse saturation). ∎

当 V ≫ k_BT/e 时指数项占主导（正向导通）；当 V ≪ 0 时电流饱和于 −I_s（反向饱和）。∎

---

## C. Inverting Op-Amp Gain −R_f/R_in · 反相运放增益 −R_f/R_in

**Claim.** For an inverting op-amp configuration with input resistor R_in (connecting v_in to the inverting terminal) and feedback resistor R_f (connecting the output back to the inverting terminal), the closed-loop voltage gain is v_out/v_in = −R_f/R_in.

**命题。** 对于带输入电阻 R_in（连接 v_in 到反相端）和反馈电阻 R_f（连接输出到反相端）的反相运放配置，闭环电压增益为 v_out/v_in = −R_f/R_in。

**Step 1 — Set up the ideal op-amp rules.** The two golden rules for an ideal op-amp with negative feedback are:
(i) The differential input voltage v₊ − v₋ = 0 (virtual short: the output adjusts via feedback to equalize the inputs).
(ii) No current flows into either input terminal (infinite input impedance).

**第 1 步 — 建立理想运放规则。** 带负反馈的理想运放的两条黄金法则为：
(i) 差分输入电压 v₊ − v₋ = 0（虚短：输出通过反馈调节以使两输入端电压相等）。
(ii) 没有电流流入任何输入端（输入阻抗无穷大）。

**Step 2 — Identify the virtual ground.** The non-inverting input v₊ is connected to ground, so v₊ = 0. By golden rule (i), v₋ = v₊ = 0. The inverting input node is therefore a **virtual ground**: it sits at 0 V but no physical connection to ground exists there.

**第 2 步 — 确认虚地。** 同相输入端 v₊ 接地，故 v₊ = 0。由黄金法则 (i)，v₋ = v₊ = 0。因此反相输入节点是**虚地**：它保持 0 V，但那里没有物理接地连接。

**Step 3 — Apply KCL at the inverting node.** Since v₋ = 0 and no current enters the op-amp input, all current through R_in must flow through R_f:

**第 3 步 — 在反相节点应用 KCL。** 由于 v₋ = 0 且没有电流流入运放输入端，通过 R_in 的所有电流必须流过 R_f：

  i₁ = (v_in − v₋)/R_in = v_in/R_in,

  i_f = (v₋ − v_out)/R_f = −v_out/R_f.

KCL: i₁ = i_f (since no current is lost into the op-amp input):

KCL：i₁ = i_f（因为没有电流流入运放输入端）：

  v_in/R_in = −v_out/R_f.

**Step 4 — Solve for the gain.** Rearranging:

**第 4 步 — 求解增益。** 整理得：

  **v_out/v_in = −R_f/R_in**.

The negative sign reflects the phase inversion: a positive v_in produces a negative v_out. The gain magnitude is R_f/R_in and is set entirely by passive components, independent of the open-loop gain A (provided A ≫ R_f/R_in, which is easily satisfied since A ~ 10⁵ for real op-amps). ∎

负号反映了相位反转：正的 v_in 产生负的 v_out。增益幅值为 R_f/R_in，完全由无源元件决定，与开环增益 A 无关（只要 A ≫ R_f/R_in，对实际运放 A ~ 10⁵ 很容易满足）。∎

---

*All three derivations follow the standard depth: complete intermediate algebra, physical interpretation of each step, and sign/limiting-case checks.*

*以上三个推导均遵循标准深度：完整的中间代数、每步的物理诠释，以及符号/极限情况核验。*

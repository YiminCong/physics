---
title: "Derivations — Module 9.1: Electronics"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 9.1: Electronics
# 推导 — 模块 9.1：电子学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 9.1](./module-9.1-electronics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 9.1](./module-9.1-electronics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. RLC Resonance Frequency and Quality Factor · RLC 谐振频率与品质因数

**Claim.** For a series RLC circuit driven at angular frequency $\omega$, the resonance frequency is $\omega_0 = 1/\sqrt{LC}$ and the quality factor is $Q = \omega_0 L/R = (1/R)\sqrt{L/C}$.

**命题。** 对于在角频率 $\omega$ 下驱动的串联 RLC 电路，谐振频率为 $\omega_0 = 1/\sqrt{LC}$，品质因数为 $Q = \omega_0 L/R = (1/R)\sqrt{L/C}$。

**Step 1 — Write the circuit equation.** Apply KVL around the loop with applied EMF $V(t) = V_0 e^{i\omega t}$:

**第 1 步 — 写出电路方程。** 对施加 EMF $V(t) = V_0 e^{i\omega t}$ 的回路应用 KVL：

$$ L\,dI/dt + RI + Q/C = V_0 e^{i\omega t}, \quad \text{with} \quad I = dQ/dt. $$

Substituting the phasor ansatz $I = \tilde{I} e^{i\omega t}$:

代入相量假设 $I = \tilde{I} e^{i\omega t}$：

$$ (i\omega L + R + 1/(i\omega C))\,\tilde{I} = V_0. $$

**Step 2 — Identify the total impedance.** The complex impedance is:

**第 2 步 — 识别总阻抗。** 复数阻抗为：

$$ Z(\omega) = R + i(\omega L - 1/(\omega C)). $$

The imaginary part is called the **reactance** $X(\omega) = \omega L - 1/(\omega C)$. The current amplitude $|\tilde{I}| = V_0/|Z| = V_0/\sqrt{R^2 + X^2}$ is maximized when $X = 0$.

虚部称为**电抗** $X(\omega) = \omega L - 1/(\omega C)$。电流幅值 $|\tilde{I}| = V_0/|Z| = V_0/\sqrt{R^2 + X^2}$ 在 $X = 0$ 时取最大值。

**Step 3 — Find the resonance frequency.** Setting $X(\omega_0) = 0$:

**第 3 步 — 求谐振频率。** 令 $X(\omega_0) = 0$：

$$ \omega_0 L = 1/(\omega_0 C) \implies \omega_0^2 = 1/(LC) \implies \boxed{\,\omega_0 = 1/\sqrt{LC}\,}. $$

At this frequency $Z(\omega_0) = R$ (purely real) and $|\tilde{I}| = V_0/R$, the maximum possible current for a given $V_0$.

在此频率下 $Z(\omega_0) = R$（纯实数），$|\tilde{I}| = V_0/R$，是给定 $V_0$ 下可能的最大电流。

**Step 4 — Derive the bandwidth.** The **half-power points** $\omega_1, \omega_2$ are where $|Z|^2 = 2R^2$ (power is halved relative to resonance):

**第 4 步 — 推导带宽。** **半功率点** $\omega_1$、$\omega_2$ 是 $|Z|^2 = 2R^2$（功率相对于谐振减半）处：

$$ R^2 + (\omega L - 1/(\omega C))^2 = 2R^2 \implies \omega L - 1/(\omega C) = \pm R. $$

For the positive root: $\omega_2 L - 1/(\omega_2 C) = +R$. For the negative root: $\omega_1 L - 1/(\omega_1 C) = -R$. Subtracting (and using $\omega_1\omega_2 \approx \omega_0^2$ for narrow resonances): $\Delta\omega = \omega_2 - \omega_1 = R/L$.

对正根：$\omega_2 L - 1/(\omega_2 C) = +R$。对负根：$\omega_1 L - 1/(\omega_1 C) = -R$。相减（对窄谐振使用 $\omega_1\omega_2 \approx \omega_0^2$）：$\Delta\omega = \omega_2 - \omega_1 = R/L$。

**Step 5 — Define Q.** The quality factor is the ratio of resonance frequency to bandwidth:

**第 5 步 — 定义 Q。** 品质因数是谐振频率与带宽之比：

$$ \boxed{\, Q = \omega_0/\Delta\omega = \omega_0 L/R \,}. $$

Substituting $\omega_0 = 1/\sqrt{LC}$:

代入 $\omega_0 = 1/\sqrt{LC}$：

$$ \boxed{\, Q = (1/R)\sqrt{L/C} \,}. $$

$Q$ also equals $2\pi$ times the ratio of energy stored to energy dissipated per cycle: $Q = 2\pi \times (\tfrac12 L I_0^2) / (\tfrac12 R I_0^2 \cdot 2\pi/\omega_0) = \omega_0 L/R$, consistent. $\blacksquare$

$Q$ 还等于 $2\pi$ 乘以每周期储存能量与耗散能量之比：$Q = 2\pi \times (\tfrac12 L I_0^2) / (\tfrac12 R I_0^2 \cdot 2\pi/\omega_0) = \omega_0 L/R$，结果一致。$\blacksquare$

---

## B. Shockley Diode Equation from the Depletion Region · 从耗尽区推导肖克利二极管方程

**Claim.** For an ideal abrupt p–n junction with applied voltage $V$, the current is $I = I_s(e^{eV/k_BT} - 1)$, where $I_s = Aen_i^2(D_p/(L_p N_D) + D_n/(L_n N_A))$ and $A$ is the junction area, $n_i$ the intrinsic carrier density, $D_p, D_n$ the minority-carrier diffusivities, $L_p, L_n$ their diffusion lengths, $N_D$ and $N_A$ the donor and acceptor concentrations.

**命题。** 对于施加电压 $V$ 的理想突变 p-n 结，电流为 $I = I_s(e^{eV/k_BT} - 1)$，其中 $I_s = Aen_i^2(D_p/(L_p N_D) + D_n/(L_n N_A))$，$A$ 为结面积，$n_i$ 为本征载流子密度，$D_p$、$D_n$ 为少数载流子扩散系数，$L_p$、$L_n$ 为扩散长度，$N_D$、$N_A$ 为施主和受主浓度。

**Step 1 — Equilibrium depletion region.** In thermal equilibrium, diffusion current (driven by concentration gradient) balances drift current (driven by the built-in field $E_{bi}$). The built-in potential satisfies:

**第 1 步 — 平衡耗尽区。** 在热平衡中，扩散电流（由浓度梯度驱动）与漂移电流（由内建电场 $E_{bi}$ 驱动）平衡。内建电势满足：

$$ e V_{bi} = k_BT \ln(N_A N_D / n_i^2). $$

This follows from setting the net electron (or hole) current to zero: $J_n = e\mu_n n E + eD_n\, dn/dx = 0$, integrating across the depletion region with the Einstein relation $D_n = \mu_n k_BT/e$.

这由将净电子（或空穴）电流设为零得到：$J_n = e\mu_n n E + eD_n\, dn/dx = 0$，利用爱因斯坦关系 $D_n = \mu_n k_BT/e$ 在耗尽区积分。

**Step 2 — Applied voltage shifts the barrier.** A forward bias $V$ reduces the electrostatic barrier to $e(V_{bi} - V)$, while reverse bias $V < 0$ increases it. The majority carrier density at the depletion-region edge on the n-side is $n_n \approx N_D$; using the Boltzmann factor for the minority holes on the n-side:

**第 2 步 — 外加电压改变势垒。** 正向偏置 $V$ 将静电势垒降低至 $e(V_{bi} - V)$，而反向偏置 $V < 0$ 则使其增大。n 侧耗尽区边缘的多数载流子密度为 $n_n \approx N_D$；利用玻尔兹曼因子得 n 侧少数空穴为：

$$ p_n(V) = p_{n0}\, e^{eV/k_BT}, $$

where $p_{n0} = n_i^2/N_D$ is the equilibrium minority hole density. This is the **law of the junction** (or boundary condition for minority carriers).

其中 $p_{n0} = n_i^2/N_D$ 为平衡少数空穴密度。这是**结定律**（少数载流子的边界条件）。

**Step 3 — Minority-carrier diffusion in the neutral regions.** In the neutral n-region ($x > x_n$), excess minority holes $\Delta p(x) = p_n(x) - p_{n0}$ satisfy the steady-state minority-carrier diffusion equation:

**第 3 步 — 中性区少数载流子扩散。** 在中性 n 区（$x > x_n$），过剩少数空穴 $\Delta p(x) = p_n(x) - p_{n0}$ 满足稳态少数载流子扩散方程：

$$ D_p\, d^2(\Delta p)/dx^2 - \Delta p/\tau_p = 0, $$

where $\tau_p$ is the minority hole lifetime. This is solved by $\Delta p(x) \propto e^{-(x-x_n)/L_p}$ with diffusion length $L_p = \sqrt{D_p \tau_p}$. Applying the junction boundary condition at $x = x_n$ (Step 2) and $\Delta p \to 0$ as $x \to \infty$:

其中 $\tau_p$ 为少数空穴寿命。解为 $\Delta p(x) \propto e^{-(x-x_n)/L_p}$，扩散长度 $L_p = \sqrt{D_p \tau_p}$。在 $x = x_n$ 处应用结边界条件（第 2 步），并利用 $x \to \infty$ 时 $\Delta p \to 0$：

$$ \Delta p(x) = p_{n0}(e^{eV/k_BT} - 1)\, e^{-(x-x_n)/L_p}. $$

**Step 4 — Compute the hole current.** The hole diffusion current at the edge $x = x_n$ is:

**第 4 步 — 计算空穴电流。** 在 $x = x_n$ 处的空穴扩散电流为：

$$ J_p = -eD_p\, d(\Delta p)/dx\,|_{x=x_n} = (eD_p p_{n0}/L_p)(e^{eV/k_BT} - 1). $$

A symmetric calculation for electron current injected into the p-side gives $J_n = (eD_n n_{p0}/L_n)(e^{eV/k_BT} - 1)$, with $n_{p0} = n_i^2/N_A$.

对注入 p 侧的电子电流进行对称计算给出 $J_n = (eD_n n_{p0}/L_n)(e^{eV/k_BT} - 1)$，其中 $n_{p0} = n_i^2/N_A$。

**Step 5 — Total current.** The total current density $J = J_p + J_n$; multiplying by junction area $A$:

**第 5 步 — 总电流。** 总电流密度 $J = J_p + J_n$；乘以结面积 $A$：

$$ \boxed{\, I = I_s (e^{eV/k_BT} - 1) \,}, $$

with $\boxed{\, I_s = Ae\, n_i^2 (D_p/(L_p N_D) + D_n/(L_n N_A)) \,}$.

其中 $\boxed{\, I_s = Ae\, n_i^2 (D_p/(L_p N_D) + D_n/(L_n N_A)) \,}$。

For $V \gg k_BT/e$ the exponential dominates (forward conduction); for $V \ll 0$ the current saturates at $-I_s$ (reverse saturation). $\blacksquare$

当 $V \gg k_BT/e$ 时指数项占主导（正向导通）；当 $V \ll 0$ 时电流饱和于 $-I_s$（反向饱和）。$\blacksquare$

---

## C. Inverting Op-Amp Gain $-R_f/R_{in}$ · 反相运放增益 $-R_f/R_{in}$

**Claim.** For an inverting op-amp configuration with input resistor $R_{in}$ (connecting $v_{in}$ to the inverting terminal) and feedback resistor $R_f$ (connecting the output back to the inverting terminal), the closed-loop voltage gain is $v_{out}/v_{in} = -R_f/R_{in}$.

**命题。** 对于带输入电阻 $R_{in}$（连接 $v_{in}$ 到反相端）和反馈电阻 $R_f$（连接输出到反相端）的反相运放配置，闭环电压增益为 $v_{out}/v_{in} = -R_f/R_{in}$。

**Step 1 — Set up the ideal op-amp rules.** The two golden rules for an ideal op-amp with negative feedback are:
(i) The differential input voltage $v_+ - v_- = 0$ (virtual short: the output adjusts via feedback to equalize the inputs).
(ii) No current flows into either input terminal (infinite input impedance).

**第 1 步 — 建立理想运放规则。** 带负反馈的理想运放的两条黄金法则为：
(i) 差分输入电压 $v_+ - v_- = 0$（虚短：输出通过反馈调节以使两输入端电压相等）。
(ii) 没有电流流入任何输入端（输入阻抗无穷大）。

**Step 2 — Identify the virtual ground.** The non-inverting input $v_+$ is connected to ground, so $v_+ = 0$. By golden rule (i), $v_- = v_+ = 0$. The inverting input node is therefore a **virtual ground**: it sits at 0 V but no physical connection to ground exists there.

**第 2 步 — 确认虚地。** 同相输入端 $v_+$ 接地，故 $v_+ = 0$。由黄金法则 (i)，$v_- = v_+ = 0$。因此反相输入节点是**虚地**：它保持 0 V，但那里没有物理接地连接。

**Step 3 — Apply KCL at the inverting node.** Since $v_- = 0$ and no current enters the op-amp input, all current through $R_{in}$ must flow through $R_f$:

**第 3 步 — 在反相节点应用 KCL。** 由于 $v_- = 0$ 且没有电流流入运放输入端，通过 $R_{in}$ 的所有电流必须流过 $R_f$：

$$ i_1 = (v_{in} - v_-)/R_{in} = v_{in}/R_{in}, $$

$$ i_f = (v_- - v_{out})/R_f = -v_{out}/R_f. $$

KCL: $i_1 = i_f$ (since no current is lost into the op-amp input):

KCL：$i_1 = i_f$（因为没有电流流入运放输入端）：

$$ v_{in}/R_{in} = -v_{out}/R_f. $$

**Step 4 — Solve for the gain.** Rearranging:

**第 4 步 — 求解增益。** 整理得：

$$ \boxed{\, v_{out}/v_{in} = -R_f/R_{in} \,}. $$

The negative sign reflects the phase inversion: a positive $v_{in}$ produces a negative $v_{out}$. The gain magnitude is $R_f/R_{in}$ and is set entirely by passive components, independent of the open-loop gain $A$ (provided $A \gg R_f/R_{in}$, which is easily satisfied since $A \sim 10^5$ for real op-amps). $\blacksquare$

负号反映了相位反转：正的 $v_{in}$ 产生负的 $v_{out}$。增益幅值为 $R_f/R_{in}$，完全由无源元件决定，与开环增益 $A$ 无关（只要 $A \gg R_f/R_{in}$，对实际运放 $A \sim 10^5$ 很容易满足）。$\blacksquare$

---

*All three derivations follow the standard depth: complete intermediate algebra, physical interpretation of each step, and sign/limiting-case checks.*

*以上三个推导均遵循标准深度：完整的中间代数、每步的物理诠释，以及符号/极限情况核验。*

# Derivations — Module 2.1: The Laws of Thermodynamics
# 推导 — 模块 2.1：热力学定律

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.1](./module-2.1-laws-of-thermodynamics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.1](./module-2.1-laws-of-thermodynamics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Carnot Efficiency $\eta = 1 - T_c/T_h$ · 卡诺效率 $\eta = 1 - T_c/T_h$

**Claim.** For any reversible heat engine operating between a hot reservoir at temperature $T_h$ and a cold reservoir at $T_c$, the efficiency is $\eta = 1 - T_c/T_h$, and no real engine can do better.

**命题。** 对于在高温热源 $T_h$ 与低温热源 $T_c$ 之间工作的任何可逆热机，效率为 $\eta = 1 - T_c/T_h$，且任何实际热机均不能超过此值。

**Step 1 — Define the Carnot cycle.** The Carnot engine executes four quasi-static strokes on a working substance (modelled below as an ideal gas, but the result is universal):

**第 1 步 — 定义卡诺循环。** 卡诺热机对工质执行四个准静态过程（以下以理想气体为例，但结果是普遍的）：

- ($A \to B$) Isothermal expansion at $T_h$: the gas absorbs heat $Q_h$ from the hot reservoir.
- ($B \to C$) Adiabatic (isentropic) expansion: the gas cools from $T_h$ to $T_c$, doing work with no heat exchange.
- ($C \to D$) Isothermal compression at $T_c$: the gas releases heat $Q_c$ to the cold reservoir.
- ($D \to A$) Adiabatic compression: the gas returns to $T_h$.

- ($A \to B$) 在 $T_h$ 下等温膨胀：气体从高温热源吸热 $Q_h$。
- ($B \to C$) 绝热（等熵）膨胀：气体从 $T_h$ 冷却至 $T_c$，对外做功，无热量交换。
- ($C \to D$) 在 $T_c$ 下等温压缩：气体向低温热源放热 $Q_c$。
- ($D \to A$) 绝热压缩：气体返回 $T_h$。

**Step 2 — Apply the First Law to the cycle.** Over one complete cycle the working substance returns to its initial state, so $\Delta U_{\text{cycle}} = 0$. Therefore the net work output is

**第 2 步 — 对循环应用热力学第一定律。** 经过一个完整循环后工质回到初态，故 $\Delta U_{\text{cycle}} = 0$。因此净功输出为

$$ W_{\text{net}} = Q_h - Q_c. $$

**Step 3 — Reversibility requires zero net entropy change.** Each stroke of the Carnot cycle is reversible by construction. The adiabatic strokes contribute zero entropy change ($\delta Q = 0$). The isothermal strokes contribute:

**第 3 步 — 可逆性要求净熵变为零。** 卡诺循环的每个过程在构造上均是可逆的。绝热过程的熵变为零（$\delta Q = 0$）。等温过程的贡献为：

$$ \Delta S_h = Q_h / T_h \quad \text{(absorbed by gas from hot reservoir)} $$
$$ \Delta S_c = -Q_c / T_c \quad \text{(released to cold reservoir; sign negative for gas)} $$

$$ \Delta S_h = Q_h / T_h \quad \text{（气体从高温热源吸热）} $$
$$ \Delta S_c = -Q_c / T_c \quad \text{（气体向低温热源放热；对气体取负号）} $$

For a reversible cycle the total entropy change of the gas (a state function, returning to its initial state) is zero:

对于可逆循环，气体（一个返回初态的态函数）的总熵变为零：

$$ \Delta S_{\text{total}} = Q_h/T_h - Q_c/T_c = 0, $$

which immediately gives $Q_c/Q_h = T_c/T_h$.

由此立即得到 $Q_c/Q_h = T_c/T_h$。

**Step 4 — Compute the efficiency.**

**第 4 步 — 计算效率。**

$$ \eta = W_{\text{net}}/Q_h = (Q_h - Q_c)/Q_h = 1 - Q_c/Q_h = \boxed{\, 1 - T_c/T_h \,} \qquad \blacksquare $$

$$ \eta = W_{\text{net}}/Q_h = (Q_h - Q_c)/Q_h = 1 - Q_c/Q_h = \boxed{\, 1 - T_c/T_h \,} \qquad \blacksquare $$

**Step 5 — Proof that no engine can exceed $\eta_{\text{Carnot}}$ (the Carnot theorem).** Suppose an irreversible engine I operating between the same reservoirs achieves $\eta_I > \eta_{\text{Carnot}}$. Run the Carnot engine in reverse as a refrigerator, driven by I's output. The combined system extracts a net quantity of heat from the cold reservoir and converts it entirely to work — a violation of the Second Law (Kelvin–Planck statement). Contradiction; therefore $\eta_I \le \eta_{\text{Carnot}}$ for any engine.

**第 5 步 — 证明没有热机能超过 $\eta_{\text{Carnot}}$（卡诺定理）。** 假设在相同两热源间工作的不可逆热机 I 实现了 $\eta_I > \eta_{\text{Carnot}}$。将卡诺热机反向运行为制冷机，由 I 的输出驱动。合并后的系统从冷源净提取热量并将其完全转化为功——这违反了热力学第二定律（开尔文-普朗克表述）。矛盾；因此对于任何热机均有 $\eta_I \le \eta_{\text{Carnot}}$。

---

## B. Entropy as a State Function: the Clausius Inequality · 熵是态函数：克劳修斯不等式

**Claim.** For any cyclic process, $\oint \delta Q/T \le 0$, with equality if and only if the cycle is reversible. From this the entropy $S$, defined by $dS = \delta Q_{\text{rev}}/T$, is a well-defined state function.

**命题。** 对于任何循环过程，$\oint \delta Q/T \le 0$，等号成立当且仅当循环是可逆的。由此定义的熵 $S$（通过 $dS = \delta Q_{\text{rev}}/T$）是一个良定义的态函数。

**Step 1 — Decompose any cycle into Carnot cycles.** Any reversible cycle in $(P,V)$ space can be approximated arbitrarily closely by a mesh of infinitesimal Carnot cycles whose adiabatic sides cancel in pairs; in the limit the approximation becomes exact. It suffices therefore to prove the inequality for a single Carnot-like element and then sum.

**第 1 步 — 将任意循环分解为卡诺小循环。** $(P,V)$ 空间中的任何可逆循环都可以用无穷小卡诺循环网格任意精确地逼近，其绝热边成对抵消；在极限下逼近变为精确。因此只需对单个卡诺元素证明不等式，然后求和即可。

**Step 2 — Prove the inequality for an arbitrary engine.** Consider any engine operating between reservoirs $T_h$ and $T_c$. By the Carnot theorem (Step 5 above), its efficiency $\eta \le 1 - T_c/T_h$, which gives

**第 2 步 — 对任意热机证明不等式。** 考虑在热源 $T_h$ 和 $T_c$ 之间工作的任意热机。由卡诺定理（上述第 5 步），其效率 $\eta \le 1 - T_c/T_h$，由此得

$$ \begin{aligned} (Q_h - Q_c)/Q_h &\le 1 - T_c/T_h \\ \implies\; Q_c/Q_h &\ge T_c/T_h \\ \implies\; Q_h/T_h - Q_c/T_c &\le 0. \end{aligned} $$

With the sign convention that $\delta Q > 0$ means heat absorbed by the working substance at temperature $T$, summing over all infinitesimal elements of the cycle gives:

以 $\delta Q > 0$ 表示工质在温度 $T$ 处吸热的符号约定，对循环所有无穷小元素求和得：

$$ \oint \delta Q/T \le 0, $$

with equality for a reversible cycle. This is the **Clausius inequality**.

等号对可逆循环成立。这就是**克劳修斯不等式**。

**Step 3 — Show $dS$ is an exact differential.** Let R be a fixed reference state. For any two states A and B connected by reversible path 1 forward and path 2 backward, the combined path is a reversible cycle, so

**第 3 步 — 证明 $dS$ 是恰当微分。** 设 R 为固定参考态。对于通过可逆路径 1（正向）和路径 2（反向）连接的任意两态 A 和 B，合并路径构成可逆循环，故

$$ \oint \delta Q_{\text{rev}}/T = \int_{A,\text{path1}}^{B} \delta Q_{\text{rev}}/T + \int_{B,\text{path2}}^{A} \delta Q_{\text{rev}}/T = 0. $$

Rearranging:

整理得：

$$ \int_{A,\text{path1}}^{B} \delta Q_{\text{rev}}/T = -\int_{B,\text{path2}}^{A} \delta Q_{\text{rev}}/T = \int_{A,\text{path2}}^{B} \delta Q_{\text{rev}}/T. $$

The line integral $\int_A^B \delta Q_{\text{rev}}/T$ is **path-independent**: it depends only on the endpoints A and B. Therefore it defines a **state function** $S$ via

线积分 $\int_A^B \delta Q_{\text{rev}}/T$ **与路径无关**：它仅取决于端点 A 和 B。因此它通过以下方式定义了一个**态函数** $S$：

$$ S(B) - S(A) = \int_A^B (\delta Q/T)_{\text{rev}}, \quad \text{i.e.,} \quad \boxed{\, dS = \delta Q_{\text{rev}}/T \,} \qquad \blacksquare $$

$$ S(B) - S(A) = \int_A^B (\delta Q/T)_{\text{rev}}, \quad \text{即} \quad \boxed{\, dS = \delta Q_{\text{rev}}/T \,} \qquad \blacksquare $$

**Step 4 — Entropy of the universe never decreases.** For an irreversible process taking the system from A to B, construct a reversible return path from B to A. The combined cycle is irreversible, so by Clausius:

**第 4 步 — 宇宙的熵永不减少。** 对于将系统从 A 带到 B 的不可逆过程，构造从 B 到 A 的可逆返回路径。合并循环是不可逆的，故由克劳修斯不等式：

$$ \begin{aligned} \int_{A,\text{irrev}}^{B} \delta Q/T + \int_{B,\text{rev}}^{A} \delta Q_{\text{rev}}/T &< 0 \\ \implies\; \int_{A,\text{irrev}}^{B} \delta Q/T &< -\int_{B,\text{rev}}^{A} \delta Q_{\text{rev}}/T = S(B) - S(A). \end{aligned} $$

Hence $dS \ge \delta Q/T$, with equality for reversible processes. For an isolated system $\delta Q = 0$, so $\boxed{\, dS \ge 0 \,}$: entropy can only increase or remain constant, giving the arrow of time. $\blacksquare$

因此 $dS \ge \delta Q/T$，等号对可逆过程成立。对于孤立系统 $\delta Q = 0$，故 $\boxed{\, dS \ge 0 \,}$：熵只能增加或保持不变，赋予时间一个箭头。$\blacksquare$

---

## C. Ideal Gas Entropy Change in Irreversible Free Expansion · 理想气体不可逆自由膨胀的熵变

**Claim.** When $N$ molecules of an ideal gas expand irreversibly from volume $V$ to $2V$ in an isolated box, $\Delta S = N k_B \ln 2 > 0$.

**命题。** 当 $N$ 个理想气体分子在孤立盒中从体积 $V$ 不可逆膨胀至 $2V$ 时，$\Delta S = N k_B \ln 2 > 0$。

**Step 1 — Identify the process.** In free expansion into a vacuum, $\delta Q = 0$ (isolated) and $\delta W = 0$ (no opposing pressure). By the First Law $\Delta U = 0$, so for an ideal gas ($U$ depends only on $T$) the temperature is unchanged: $T_f = T_i = T$.

**第 1 步 — 确定过程。** 在向真空的自由膨胀中，$\delta Q = 0$（孤立）且 $\delta W = 0$（无对抗压强）。由第一定律 $\Delta U = 0$，故对于理想气体（$U$ 仅取决于 $T$），温度不变：$T_f = T_i = T$。

**Step 2 — Choose a reversible path between the same states.** Since $S$ is a state function, $\Delta S$ is the same for any path connecting $(T, V)$ to $(T, 2V)$. Choose a quasi-static isothermal expansion at temperature $T$. Along this path $\delta Q_{\text{rev}} = P\, dV = (N k_B T/V)\, dV$.

**第 2 步 — 在相同初末态之间选择可逆路径。** 由于 $S$ 是态函数，连接 $(T, V)$ 和 $(T, 2V)$ 的任何路径的 $\Delta S$ 相同。选择在温度 $T$ 下的准静态等温膨胀。沿此路径 $\delta Q_{\text{rev}} = P\, dV = (N k_B T/V)\, dV$。

**Step 3 — Integrate.**

**第 3 步 — 积分。**

$$ \Delta S = \int_V^{2V} (N k_B T/V)\, dV / T = N k_B \int_V^{2V} dV/V = N k_B \ln(2V/V) = \boxed{\, N k_B \ln 2 > 0 \,} \qquad \blacksquare $$

$$ \Delta S = \int_V^{2V} (N k_B T/V)\, dV / T = N k_B \int_V^{2V} dV/V = N k_B \ln(2V/V) = \boxed{\, N k_B \ln 2 > 0 \,} \qquad \blacksquare $$

This positive entropy increase occurs even though $\delta Q = 0$ for the actual process, confirming that entropy is not "heat divided by temperature" in general, but a state function computed via a reversible path.

即使实际过程中 $\delta Q = 0$，熵也会增加，这证实了熵并非一般意义上的"热量除以温度"，而是通过可逆路径计算的态函数。

---

*All results here are exact consequences of the two empirical laws. The Clausius inequality and the state-function nature of $S$ form the logical bridge between the macroscopic Second Law and the microscopic counting of Module 2.4 ($S = k_B \ln \Omega$).*

*此处所有结果均是两条经验定律的精确推论。克劳修斯不等式和 $S$ 的态函数性质构成了宏观第二定律与模块 2.4 微观计数（$S = k_B \ln \Omega$）之间的逻辑桥梁。*

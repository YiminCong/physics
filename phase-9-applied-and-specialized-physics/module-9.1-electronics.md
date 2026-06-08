# Module 9.1 — Electronics: Circuits, Semiconductors & Amplifiers
**模块 9.1 — 电子学：电路、半导体与放大器**

> **Phase 9 — [Applied & Specialized Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 9 阶段 — 应用与专门物理** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-9.1-electronics-derivations.md)

---

## 1. Kirchhoff's Laws · 基尔霍夫定律

**Definition.** Two conservation laws govern every circuit. **Kirchhoff's Current Law (KCL)** states that the algebraic sum of currents entering any node is zero (charge conservation). **Kirchhoff's Voltage Law (KVL)** states that the algebraic sum of voltage drops around any closed loop is zero (energy conservation, equivalent to Faraday's law in the magnetostatic limit).

**定义。** 两条守恒定律支配所有电路。**基尔霍夫电流定律（KCL）**指出，进入任意节点的电流代数和为零（电荷守恒）。**基尔霍夫电压定律（KVL）**指出，沿任意闭合回路的电压降代数和为零（能量守恒，等价于静磁极限下的法拉第定律）。

**Demonstration.** For a simple RC series circuit driven by a step voltage V₀, KVL gives V₀ = V_R + V_C = IR + Q/C. Writing I = dQ/dt yields the first-order ODE dQ/dt + Q/(RC) = V₀/R, with solution Q(t) = CV₀(1 − e^{−t/RC}). The characteristic time τ = RC is the **RC time constant**.

**演示。** 对于阶跃电压 V₀ 驱动的简单 RC 串联电路，KVL 给出 V₀ = V_R + V_C = IR + Q/C。令 I = dQ/dt 得一阶常微分方程 dQ/dt + Q/(RC) = V₀/R，解为 Q(t) = CV₀(1 − e^{−t/RC})。特征时间 τ = RC 即 **RC 时间常数**。

**Application.** RC transients determine the speed of digital logic gates and the frequency response of filters. The RL circuit analog gives τ = L/R; in both cases the stored energy relaxes exponentially toward its equilibrium value.

**应用。** RC 瞬态决定数字逻辑门的速度和滤波器的频率响应。RL 电路的类似量为 τ = L/R；两种情况下储存的能量都以指数方式弛豫到平衡值。

---

## 2. AC Impedance & Complex Phasors · 交流阻抗与复相量

**Definition.** For a sinusoidal drive V(t) = V₀ cos(ωt) = Re[V₀ e^{iωt}], define the **phasor** Ṽ = V₀ e^{iφ}. Each element has a complex **impedance** Z relating phasor voltage to phasor current Ṽ = ZĨ: for a resistor Z_R = R, a capacitor Z_C = 1/(iωC), and an inductor Z_L = iωL. Impedances combine like resistances (series: Z_tot = ΣZ_k; parallel: 1/Z_tot = Σ1/Z_k).

**定义。** 对于正弦驱动 V(t) = V₀ cos(ωt) = Re[V₀ e^{iωt}]，定义**相量** Ṽ = V₀ e^{iφ}。每个元件具有复数**阻抗** Z，通过 Ṽ = ZĨ 将相量电压与相量电流联系起来：电阻 Z_R = R，电容 Z_C = 1/(iωC)，电感 Z_L = iωL。阻抗的组合方式与电阻相同（串联：Z_tot = ΣZ_k；并联：1/Z_tot = Σ1/Z_k）。

**Demonstration.** For a series RLC circuit the total impedance is Z = R + iωL + 1/(iωC) = R + i(ωL − 1/(ωC)). The magnitude |Z| = √(R² + (ωL − 1/(ωC))²) is minimized when ωL = 1/(ωC), giving the **resonance frequency ω₀ = 1/√(LC)**. At resonance |Z| = R and the current amplitude is maximized.

**演示。** 对于串联 RLC 电路，总阻抗为 Z = R + iωL + 1/(iωC) = R + i(ωL − 1/(ωC))。幅值 |Z| = √(R² + (ωL − 1/(ωC))²) 在 ωL = 1/(ωC) 时取最小值，给出**谐振频率 ω₀ = 1/√(LC)**。谐振时 |Z| = R，电流幅值最大。

**Application.** The **quality factor Q = ω₀L/R = (1/R)√(L/C)** measures the sharpness of resonance: Q = ω₀/(Δω) where Δω is the half-power bandwidth. High-Q LC circuits are used in radio tuners and oscillators; low-Q (overdamped) circuits avoid unwanted ringing in signal paths.

**应用。** **品质因数 Q = ω₀L/R = (1/R)√(L/C)** 衡量谐振的尖锐程度：Q = ω₀/(Δω)，其中 Δω 为半功率带宽。高 Q 值 LC 电路用于无线电调谐器和振荡器；低 Q 值（过阻尼）电路避免信号路径中不希望的振铃。

---

## 3. The p–n Junction Diode · p-n 结二极管

**Definition.** A **p–n junction** is formed at the interface of p-type (acceptor-doped) and n-type (donor-doped) semiconductor. Carrier diffusion creates a **depletion region** devoid of mobile charges, establishing a built-in electric field and contact potential V_bi. The Shockley (ideal diode) equation relates current to applied voltage V:

  I = I_s (e^{eV/k_BT} − 1)

where I_s is the reverse saturation current, e is the electron charge, k_B Boltzmann's constant, and T the temperature. The thermal voltage V_T = k_BT/e ≈ 26 mV at room temperature.

**定义。** **p-n 结**形成于 p 型（受主掺杂）与 n 型（施主掺杂）半导体的界面。载流子扩散产生一个不含自由电荷的**耗尽区**，建立内建电场和接触电势 V_bi。肖克利（理想二极管）方程将电流与外加电压 V 联系起来：

  I = I_s (e^{eV/k_BT} − 1)

其中 I_s 为反向饱和电流，e 为电子电荷，k_B 为玻尔兹曼常数，T 为温度。热电压 V_T = k_BT/e 在室温下约为 26 mV。

**Demonstration.** Forward bias (V > 0) lowers the depletion barrier, flooding the junction with minority carriers that recombine and produce exponentially growing current. Reverse bias (V < 0) widens the depletion region; only the tiny drift current I_s flows until avalanche breakdown. The diode is a rectifier: it passes current strongly in one direction only.

**演示。** 正向偏置（V > 0）降低耗尽区势垒，向结区注入少数载流子，它们复合并产生指数增长的电流。反向偏置（V < 0）加宽耗尽区，仅有微小的漂移电流 I_s 流过，直至雪崩击穿。二极管是整流器：仅在一个方向强烈导通。

**Application.** Diodes are used in AC rectification (power supplies), signal clipping, and light emission (LEDs). The exponential I–V law also underlies the operation of the BJT transistor below. The full derivation of I_s from diffusion equations appears in the Derivations file.

**应用。** 二极管用于交流整流（电源）、信号削波和发光（LED）。指数 I–V 定律也是下文 BJT 晶体管工作原理的基础。I_s 由扩散方程推导的全过程见推导文件。

---

## 4. Transistors as Amplifiers and Switches · 晶体管作为放大器和开关

**Definition.** A **bipolar junction transistor (BJT)** has three terminals — emitter, base, collector — with two back-to-back p–n junctions. In the active (amplifying) region the emitter–base junction is forward-biased and the base–collector junction is reverse-biased. A small base current I_B controls a much larger collector current I_C = β I_B, where β ≈ 50–300 is the **current gain**. A **field-effect transistor (FET)** controls current via a gate voltage rather than gate current; the MOSFET is the dominant device in digital logic.

**定义。** **双极结型晶体管（BJT）**有三个端口——发射极、基极、集电极——包含两个背靠背的 p-n 结。在有源（放大）区，发射极–基极结正向偏置，基极–集电极结反向偏置。小基极电流 I_B 控制大得多的集电极电流 I_C = β I_B，其中 β ≈ 50–300 为**电流增益**。**场效应晶体管（FET）**通过栅极电压而非栅极电流来控制电流；MOSFET 是数字逻辑的主导器件。

**Demonstration.** In a common-emitter amplifier, an AC input signal v_in superimposed on the DC bias at the base produces an amplified, phase-inverted output at the collector: v_out = −g_m R_C v_in, where g_m = I_C/V_T is the transconductance and R_C is the collector load resistance. The voltage gain magnitude |A_v| = g_m R_C can be 100 or more.

**演示。** 在共射极放大器中，叠加在基极直流偏置上的交流输入信号 v_in 在集电极产生放大且相位反转的输出：v_out = −g_m R_C v_in，其中 g_m = I_C/V_T 为跨导，R_C 为集电极负载电阻。电压增益幅值 |A_v| = g_m R_C 可达 100 或更大。

**Application.** As a switch, the BJT or MOSFET is driven between saturation (fully ON, I_C limited by the circuit) and cutoff (fully OFF, I_C ≈ 0), implementing digital logic. As an amplifier it forms the heart of audio amplifiers, RF circuits, and analog signal processing.

**应用。** 作为开关，BJT 或 MOSFET 在饱和（完全导通，I_C 受电路限制）和截止（完全关断，I_C ≈ 0）之间切换，实现数字逻辑。作为放大器，它是音频放大器、射频电路和模拟信号处理的核心。

---

## 5. The Operational Amplifier · 运算放大器

**Definition.** An **operational amplifier (op-amp)** is a high-gain differential amplifier with very high input impedance and very low output impedance. The **ideal op-amp** model asserts: (i) infinite open-loop voltage gain A → ∞; (ii) infinite input impedance (zero input currents); (iii) zero output impedance. With negative feedback these idealizations lead to simple, exact gain expressions.

**定义。** **运算放大器（op-amp）**是一种高增益差分放大器，具有极高的输入阻抗和极低的输出阻抗。**理想运放**模型假设：(i) 开环电压增益无穷大 A → ∞；(ii) 输入阻抗无穷大（输入电流为零）；(iii) 输出阻抗为零。在负反馈下，这些理想化条件给出简单、精确的增益表达式。

**Demonstration.** For the **inverting amplifier** configuration, the non-inverting input is grounded. The ideal op-amp condition forces the inverting input to a **virtual ground** (v₋ ≈ 0). KCL at the inverting node: v_in/R_in + v_out/R_f = 0, giving the **ideal inverting gain**:

  v_out/v_in = −R_f/R_in.

The gain is set entirely by the ratio of external resistors, independent of the op-amp's internal parameters.

**演示。** 对于**反相放大器**配置，同相输入端接地。理想运放条件迫使反相输入端成为**虚地**（v₋ ≈ 0）。对反相节点应用 KCL：v_in/R_in + v_out/R_f = 0，给出**理想反相增益**：

  v_out/v_in = −R_f/R_in。

增益完全由外部电阻的比值决定，与运放的内部参数无关。

**Application.** Op-amps implement integrators, differentiators, summing amplifiers, comparators, and active filters — the building blocks of analog computing and signal conditioning. The non-inverting amplifier gives gain +(1 + R_f/R_in); the voltage follower (R_f = 0, R_in → ∞) gives unity gain and serves as an impedance buffer.

**应用。** 运放实现积分器、微分器、求和放大器、比较器和有源滤波器——这些是模拟计算和信号调理的基本模块。同相放大器给出增益 +(1 + R_f/R_in)；电压跟随器（R_f = 0，R_in → ∞）给出单位增益，用作阻抗缓冲器。

---

**Self-test (blank page)**

1. State KCL and KVL. Solve for Q(t) in a series RC circuit charged from zero through a resistor by a battery V₀.
2. Write the impedance of R, L, C in phasor notation; find the resonance frequency and Q-factor of a series RLC circuit.
3. Sketch the I–V curve of an ideal diode; explain the physical origin of the exponential dependence.
4. In a common-emitter amplifier, derive the voltage gain v_out/v_in in terms of g_m and R_C.
5. Using the virtual-ground rule, derive the gain of an inverting op-amp with feedback resistor R_f and input resistor R_in.

**自测（空白页）**

1. 陈述 KCL 和 KVL。求从零开始通过电阻由电池 V₀ 充电的串联 RC 电路的 Q(t)。
2. 用相量符号写出 R、L、C 的阻抗；求串联 RLC 电路的谐振频率和品质因数。
3. 画出理想二极管的 I–V 曲线；解释指数依赖关系的物理起源。
4. 在共射极放大器中，用 g_m 和 R_C 推导电压增益 v_out/v_in。
5. 利用虚地规则，推导带反馈电阻 R_f 和输入电阻 R_in 的反相运放的增益。

---

[Phase 9 index](./README.md) · Next: [Module 9.2 — Atomic & Molecular Physics](./module-9.2-atomic-and-molecular-physics.md) →

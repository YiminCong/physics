# Module 5.8 — Josephson Effects ⭐
**模块 5.8 — 约瑟夫森效应 ⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.8-josephson-effects-derivations.md)

---

## 1. Coherent Pair Tunneling · 相干对隧穿

**Definition.** Two superconductors separated by a thin barrier form a **Josephson junction**, across which Cooper pairs tunnel coherently. Two effects follow:
- **DC Josephson effect:** a supercurrent $I = I_c \sin(\Delta\phi)$ flows at **zero voltage**, set by the phase difference $\Delta\phi$ across the junction.
- **AC Josephson effect:** a constant voltage $V$ produces an **oscillating** current at frequency $f = 2eV/h$.

**定义。** 由薄势垒隔开的两个超导体构成**约瑟夫森结**，库珀对在其间相干隧穿。由此产生两种效应：
- **直流约瑟夫森效应：** 超电流 $I = I_c \sin(\Delta\phi)$ 在**零电压**下流动，由结两端的相位差 $\Delta\phi$ 决定。
- **交流约瑟夫森效应：** 恒定电压 $V$ 产生频率为 $f = 2eV/h$ 的**振荡**电流。

**Demonstration.** The controlling variable is the **phase $\phi$** of the order parameter (Module 0.4) — superconductivity makes a quantum phase macroscopically observable. A **SQUID** (two junctions in a loop) turns phase interference into the most sensitive magnetometer known.

**演示。** 控制变量是序参量的**相位 $\phi$**（模块 0.4）——超导性使量子相位在宏观上可观测。**SQUID**（回路中的两个结）将相位干涉转变为已知最灵敏的磁强计。

**Application.** SQUIDs (brain/heart magnetic imaging, geophysics), the **Josephson voltage standard**, and **superconducting qubits** — the leading hardware platform for quantum computing — all run on these effects.

**应用。** SQUID（脑/心磁成像、地球物理学）、**约瑟夫森电压标准**以及**超导量子比特**——量子计算的领先硬件平台——都基于这些效应运行。

## Key results · 核心结果

- DC Josephson $I = I_c\sin(\Delta\phi)$ — supercurrent with zero voltage · 直流约瑟夫森效应
- AC Josephson $\hbar\,\dfrac{d(\Delta\phi)}{dt} = 2eV$ — voltage drives an oscillating current · 交流约瑟夫森效应
- The macroscopic phase $\phi$ is a real, measurable observable · 宏观相位是可测量
- Basis of SQUIDs and superconducting qubits · SQUID 与超导量子比特的基础

---

**Self-test (blank page)**

1. State the DC Josephson relation $I = I_c \sin(\Delta\phi)$ and the AC Josephson relation $df/dt = 2eV/h$. What physical quantity is $\Delta\phi$, and why does the DC effect require zero voltage across the junction?
2. A constant voltage $V$ is applied across a Josephson junction. Compute the frequency of the resulting AC supercurrent. Numerically, what frequency (in GHz) corresponds to $V = 1\ \mu\text{V}$?
3. A SQUID consists of two Josephson junctions in a superconducting loop. Explain how the total critical current of the SQUID depends on the magnetic flux threading the loop, and why this makes a SQUID an ultra-sensitive magnetometer.
4. The Josephson effects arise from the macroscopic quantum phase of the order parameter. How does the phase difference $\Delta\phi$ change with time when $V \neq 0$, and what does this say about the quantum mechanics of the condensate?

**自测（空白页）**

1. 写出直流约瑟夫森关系 $I = I_c \sin(\Delta\phi)$ 和交流约瑟夫森关系 $df/dt = 2eV/h$。$\Delta\phi$ 是什么物理量？为何直流效应要求结两端电压为零？
2. 在约瑟夫森结两端施加恒定电压 $V$。计算所产生的交流超电流的频率。数值上，$V = 1\ \mu\text{V}$ 对应的频率是多少 GHz？
3. SQUID 由超导回路中的两个约瑟夫森结组成。解释 SQUID 的总临界电流如何依赖于穿过回路的磁通量，以及为何这使 SQUID 成为超灵敏磁强计。
4. 约瑟夫森效应源于序参量的宏观量子相位。当 $V \neq 0$ 时，相位差 $\Delta\phi$ 如何随时间变化？这对凝聚态的量子力学说明了什么？

---

← Previous: [Module 5.7 — Type II Superconductors & Vortices](./module-5.7-type-ii-superconductors-and-vortices.md) · [Phase 5 index](./README.md) · Next: [Module 5.9 — Unconventional & High-Tᶜ Superconductors](./module-5.9-unconventional-and-high-tc-superconductors.md) →

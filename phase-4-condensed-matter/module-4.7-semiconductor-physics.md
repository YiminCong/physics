# Module 4.7 — Semiconductor Physics
**模块 4.7 — 半导体物理**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.7-derivations.md)

---

## 1. Bands, Holes & Effective Mass · 能带、空穴与有效质量

**Definition.** A **semiconductor** is a crystalline solid with a **band gap** $E_g$ (typically 0.1-3 eV) separating a completely filled **valence band** from an empty **conduction band** at $T = 0$. The material is an insulator at absolute zero but carriers are thermally excited across the gap at finite temperature. The distinction from an insulator is quantitative ($E_g \lesssim 3$ eV for semiconductors vs $E_g > 5$ eV for insulators) — not qualitative.

**定义。** **半导体**是一种晶态固体，具有**带隙** $E_g$（通常为 0.1-3 eV），将完全填满的**价带**与 $T = 0$ 时空的**导带**分开。材料在绝对零度时是绝缘体，但有限温度下载流子被热激发越过带隙。与绝缘体的区别是定量的（半导体 $E_g \lesssim 3$ eV，绝缘体 $E_g > 5$ eV），而非定性的。

**Demonstration.** Near a band extremum the energy dispersion is parabolic: $E(k) \approx E_\text{edge} + \hbar^2 k^2/(2m^*)$. The **effective mass** $m^*$ is defined by

**演示。** 在能带极值附近，能量色散为抛物线形：$E(k) \approx E_\text{edge} + \hbar^2 k^2/(2m^*)$。**有效质量** $m^*$ 定义为

$$ \frac{1}{m^*} = \frac{1}{\hbar^2}\frac{d^2 E}{dk^2} $$

and encodes all the effects of the crystal potential into a renormalized inertia. $m^*$ can be lighter than the free-electron mass $m_e$ (fast response) or heavier (sluggish carriers). A **hole** is the absence of an electron from the valence band. Treating the filled-band-minus-one-electron as a positive charge carrier of mass $m_h^* = -m_e^*(\text{valence top})$ (positive because the valence band curves downward) gives a powerful single-particle description of conduction in both bands.

它将晶体势的所有效应编码为重整化的惯性。$m^*$ 可以轻于自由电子质量 $m_e$（响应快）或重于 $m_e$（载流子迟钝）。**空穴**是价带中缺少一个电子的状态。将填满的能带减去一个电子视为质量为 $m_h^* = -m_e^*$（价带顶部）的正电荷载流子（正号源于价带向下弯曲），给出了描述两个能带中导电的强大单粒子图像。

**Application.** In a **pure (intrinsic) semiconductor** thermal excitation across $E_g$ creates equal numbers of electrons and holes. The **intrinsic carrier density** is

**应用。** 在**纯（本征）半导体**中，热激发越过 $E_g$ 产生等量的电子和空穴。**本征载流子浓度**为

$$ n_i = \sqrt{N_c N_v}\cdot \exp\!\left(-\frac{E_g}{2k_B T}\right) $$

where $N_c \propto (m_e^*)^{3/2} T^{3/2}$ and $N_v \propto (m_h^*)^{3/2} T^{3/2}$ are the effective densities of states (derived in the derivations file). The exponential Boltzmann factor $\exp(-E_g / 2k_B T)$ makes $n_i$ extremely sensitive to $T$ and to $E_g$.

其中 $N_c \propto (m_e^*)^{3/2} T^{3/2}$，$N_v \propto (m_h^*)^{3/2} T^{3/2}$ 是有效态密度（在推导文件中导出）。指数玻尔兹曼因子 $\exp(-E_g / 2k_B T)$ 使 $n_i$ 对温度 $T$ 和带隙 $E_g$ 极为敏感。

**Doping** introduces impurity atoms with one extra (**donor**, n-type: electron given to conduction band) or one fewer (**acceptor**, p-type: hole given to valence band) valence electron relative to the host. Donors create shallow levels just below the conduction band edge, ionised at room temperature; acceptors create shallow levels just above the valence band edge. Controlled doping is the technological foundation of all semiconductor devices: it can shift $n_i$ by many orders of magnitude and place the Fermi level precisely within the gap.

**掺杂**引入相对于主体材料多一个（**施主**，n 型：电子给入导带）或少一个（**受主**，p 型：空穴给入价带）价电子的杂质原子。施主在导带底稍下方产生浅能级，室温下电离；受主在价带顶稍上方产生浅能级。可控掺杂是所有半导体器件的技术基础：它可以将 $n_i$ 改变许多数量级，并将费米能级精确放置在带隙中。

---

## 2. The p–n Junction & Devices · p–n 结与器件

**Definition.** A **p–n junction** is formed where p-type and n-type semiconductor are brought into contact. In equilibrium, electrons diffuse from n to p and holes from p to n, creating a region depleted of mobile carriers — the **depletion region** (width $W$) — and a built-in electric potential difference $V_\text{bi}$ (the **built-in voltage**), which opposes further diffusion. The Fermi level is uniform across the junction at equilibrium.

**定义。** **p–n 结**在 p 型与 n 型半导体接触处形成。在平衡状态下，电子从 n 侧扩散到 p 侧，空穴从 p 侧扩散到 n 侧，形成一个缺乏移动载流子的区域——**耗尽区**（宽度 $W$）——以及阻止进一步扩散的内建电势差 $V_\text{bi}$（**内建电压**）。平衡态时费米能级在整个结中是均匀的。

**Demonstration.** Applying an external forward bias $V$ reduces the barrier to $V_\text{bi} - V$, exponentially increasing the current of minority carriers injected across the junction. Reverse bias increases the barrier and allows only a small (near-saturation) leakage current. The resulting **diode equation** (ideal Shockley model) is

**演示。** 施加外部正向偏压 $V$ 将势垒降低到 $V_\text{bi} - V$，指数级增加越过结注入的少数载流子电流。反向偏压增大势垒，只允许一个小的（近饱和）漏电流。由此得到的**二极管方程**（理想肖克利模型）为

$$ I = I_0\left(\exp\!\left(\frac{eV}{k_B T}\right) - 1\right) $$

where $I_0$ is the reverse saturation current. The exponential rectification is a direct consequence of the Boltzmann distribution of thermally activated carriers over the junction barrier.

其中 $I_0$ 是反向饱和电流。指数整流特性是热激发载流子越过结势垒的玻尔兹曼分布的直接结果。

**Application.** The p–n junction is the building block of modern electronics:

**应用。** p–n 结是现代电子学的基本构件：

- **Bipolar junction transistor (BJT):** two junctions (n–p–n or p–n–p) allow a small base current to control a large collector current — amplification.
- **双极结型晶体管（BJT）：** 两个结（n–p–n 或 p–n–p）使小的基极电流控制大的集电极电流——放大。
- **MOSFET:** a gate voltage modulates the carrier density in a channel between source and drain — the basis of CMOS logic.
- **MOSFET：** 栅极电压调制源极和漏极之间沟道中的载流子密度——CMOS 逻辑的基础。
- **Optoelectronics:** forward-biased junctions in direct-gap semiconductors (GaAs, InGaN) recombine electrons and holes to emit photons — the **LED** and **laser diode**. Reverse-biased junctions absorb photons and generate electron–hole pairs — the **photodiode** and **solar cell**. These applications connect to the photon–matter interaction discussed in Module 9.1.
- **光电器件：** 直接带隙半导体（GaAs、InGaN）中正向偏置结中电子与空穴复合发射光子——**LED** 和**激光二极管**。反向偏置结吸收光子产生电子–空穴对——**光电二极管**和**太阳能电池**。这些应用与模块 9.1 中讨论的光子–物质相互作用相关。

---

**Self-test (blank page)**

1. Define the effective mass $m^*$ in terms of the band curvature. Why can $m^*$ be negative, and what does a negative curvature imply for the sign of the carrier?
2. Write down the intrinsic carrier density formula $n_i \propto T^{3/2} \exp(-E_g / 2k_B T)$ and explain the origin of each factor.
3. Explain what happens at a p–n junction in equilibrium: draw the band diagram, label the depletion region and $V_\text{bi}$.
4. Derive or state the Shockley diode equation and explain the physical reason for its exponential form.
5. Distinguish n-type from p-type doping and explain how each shifts the Fermi level within the gap.

**自测（空白页）**

1. 用能带曲率定义有效质量 $m^*$。为什么 $m^*$ 可以为负，负曲率对载流子符号意味着什么？
2. 写出本征载流子浓度公式 $n_i \propto T^{3/2} \exp(-E_g / 2k_B T)$ 并解释每个因子的来源。
3. 解释平衡态 p–n 结发生了什么：画出能带图，标出耗尽区和 $V_\text{bi}$。
4. 推导或陈述肖克利二极管方程，并解释其指数形式的物理原因。
5. 区分 n 型和 p 型掺杂，并解释每种掺杂如何将费米能级移动到带隙内。

---

← Previous: [Module 4.6 — Magnetism & Spin Waves](./module-4.6-magnetism-and-spin-waves.md) · [Phase 4 index](./README.md) · Next: [Module 4.8 — Quantum Hall Effect](./module-4.8-quantum-hall-effect.md) →

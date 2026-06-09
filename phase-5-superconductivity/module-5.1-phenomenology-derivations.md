---
title: "Derivations — Module 5.1: Phenomenology of Superconductivity"
nav_exclude: true
search_exclude: false
---

# Derivations — Module 5.1: Phenomenology of Superconductivity
# 推导 — 模块 5.1：超导现象学

> ✅ **Verified 2026-06-09** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-09 -->
> ✅ **已校验 2026-06-09** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 5.1](./module-5.1-phenomenology.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.1](./module-5.1-phenomenology.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Perfect Conductor vs. Superconductor: The Field-Cooled Argument · 完美导体与超导体：场冷论证

**Claim.** A perfect conductor ($\sigma \to \infty$ but otherwise normal) traps magnetic flux when cooled in a field, whereas a superconductor expels the field regardless of cooling history. The two phenomena are physically distinct and the difference is embodied in the condition $B = 0$ inside a superconductor rather than merely $dB/dt = 0$.

**命题。** 一个完美导体（$\sigma \to \infty$，但其他方面与正常金属相同）在磁场中冷却时会困住磁通量，而超导体无论冷却历史如何都会排出磁场。这两种现象在物理上是截然不同的，区别体现在超导体内部满足 $B = 0$，而不仅仅是 $dB/dt = 0$。

**Step 1 — Faraday's law inside a perfect conductor.** Maxwell's equation $\partial B/\partial t = -\nabla \times E$ holds in all media. Ohm's law in its resistive form is $J = \sigma E$. In the limit $\sigma \to \infty$ any finite $J$ requires $E \to 0$; conversely, a nonzero $E$ would drive an infinite current, which is unphysical. Therefore inside a perfect conductor $E = 0$ everywhere, and Faraday's law gives

**第 1 步 — 完美导体内的法拉第定律。** 麦克斯韦方程 $\partial B/\partial t = -\nabla \times E$ 在所有介质中都成立。电阻形式的欧姆定律为 $J = \sigma E$。在 $\sigma \to \infty$ 的极限下，任何有限的 $J$ 都要求 $E \to 0$；反之，非零的 $E$ 将驱动无限大的电流，这在物理上是不允许的。因此，在完美导体内部 $E = 0$ 处处成立，法拉第定律给出

$$ \frac{\partial B}{\partial t} = -\nabla \times E = -\nabla \times 0 = 0. $$

So **B is frozen** — the magnetic field is constant in time inside a perfect conductor and cannot change after the material becomes perfectly conducting.

故 **B 被冻结** — 磁场在完美导体内部随时间不变，材料变为完美导体后磁场无法改变。

**Step 2 — Field-cooled scenario for a perfect conductor.** Apply an external field $H$ above the transition, then cool. When the material becomes a perfect conductor with the field already present, $B$ inside takes whatever value it had at the moment of the transition. From that moment onward $\partial B/\partial t = 0$, so $B$ is permanently frozen at that nonzero value. The flux is **trapped**.

**第 2 步 — 完美导体的场冷情形。** 在转变温度以上施加外磁场 $H$，然后冷却。当材料变为完美导体时，磁场已经存在，内部 $B$ 取转变时刻的值。从那一刻起 $\partial B/\partial t = 0$，所以 $B$ 永久冻结在该非零值。磁通量被**困住**。

**Step 3 — Zero-field-cooled scenario for a perfect conductor.** Cool below the transition first with no external field (so $B = 0$ inside at the transition). Then apply $H$. Now the condition $\partial B/\partial t = 0$ holds from the moment of transition: any attempt by the new external field to change $B$ inside is prevented. The field is **excluded**, but only because it was never let in. The exclusion here is a passive consequence of the prior $B = 0$ state.

**第 3 步 — 完美导体的零场冷情形。** 先在无外场的情况下冷却（转变时内部 $B = 0$），然后施加 $H$。现在从转变时刻起 $\partial B/\partial t = 0$：外场试图改变内部 $B$ 的任何企图都被阻止。磁场被**排斥**，但仅仅是因为它从未进入过。这里的排斥是先前 $B = 0$ 状态的被动结果。

**Step 4 — The Meissner observation contradicts a perfect conductor.** Meissner and Ochsenfeld (1933) found that when a real superconductor is cooled in a field, the field is **actively expelled** — $B$ inside drops to zero even though the material had $B \ne 0$ just before crossing $T_c$. This is impossible for a perfect conductor (Step 2 showed $B$ would be frozen). The expulsion requires an active mechanism: the superconductor develops screening currents that create a field exactly canceling the external field in the interior. This is a new thermodynamic state, not merely perfect conductivity.

**第 4 步 — 迈斯纳观测与完美导体相矛盾。** 迈斯纳和奥克森菲尔德（1933年）发现，当真正的超导体在磁场中冷却时，磁场被**主动排出** — 即使材料在穿越 $T_c$ 前内部 $B \ne 0$，之后内部 $B$ 降为零。这对完美导体来说是不可能的（第 2 步表明 $B$ 会被冻结）。磁场排斥需要主动机制：超导体产生屏蔽电流，在内部产生恰好抵消外磁场的磁场。这是一个新的热力学态，而不仅仅是完美导电性。

**Step 5 — Summary of the logical structure.** The two conditions are:

**第 5 步 — 逻辑结构总结。** 两个条件分别是：

$$ \begin{aligned} \text{Perfect conductor:}&\quad \frac{\partial B}{\partial t} = 0 \quad (B \text{ frozen at whatever value it had}) \\ \text{Superconductor:}&\quad B = 0 \quad (B \text{ expelled, regardless of history}) \end{aligned} $$

$$ \begin{aligned} \text{完美导体：}&\quad \frac{\partial B}{\partial t} = 0 \quad (B \text{ 冻结在已有值}) \\ \text{超导体：}&\quad B = 0 \quad (B \text{ 被排出，与历史无关}) \end{aligned} $$

The superconductor condition is strictly stronger. $B = 0$ implies $\partial B/\partial t = 0$ trivially, but $\partial B/\partial t = 0$ does not imply $B = 0$. The Meissner effect is therefore an independent experimental signature that defines a new state of matter. $\blacksquare$

超导体条件严格更强。$B = 0$ 显然蕴含 $\partial B/\partial t = 0$，但 $\partial B/\partial t = 0$ 不蕴含 $B = 0$。因此迈斯纳效应是定义物质新态的独立实验特征。$\blacksquare$

---

## B. Isotope Effect: Deriving $T_c \propto M^{-1/2}$ · 同位素效应：推导 $T_c \propto M^{-1/2}$

**Claim.** When the ionic mass of a superconductor is varied isotopically (same element, different neutron number), the critical temperature scales as $T_c \propto M^{-1/2}$. This follows because $T_c$ is set by the Debye frequency $\omega_D$, which itself scales as $M^{-1/2}$ from lattice dynamics.

**命题。** 当超导体的离子质量通过同位素替换改变时（同一元素，不同中子数），临界温度的标度为 $T_c \propto M^{-1/2}$。这是因为 $T_c$ 由德拜频率 $\omega_D$ 决定，而 $\omega_D$ 本身由晶格动力学给出 $M^{-1/2}$ 的标度。

**Step 1 — Simple harmonic lattice model.** Model each ion of mass $M$ as a harmonic oscillator in the crystal potential well. The restoring force constant $K$ is set by the Coulomb interactions between ions and electrons and depends on the electronic charge distribution — it does not change when $M$ changes (changing isotope swaps neutrons, not electrons, so the electronic potential is unchanged to excellent approximation). The angular frequency of oscillation is

**第 1 步 — 简单谐振晶格模型。** 将质量为 $M$ 的每个离子建模为晶体势阱中的谐振子。恢复力常数 $K$ 由离子与电子之间的库仑相互作用决定，取决于电子电荷分布——当 $M$ 改变时它不变（同位素替换交换中子而非电子，所以电子势到很好的近似是不变的）。振荡角频率为

$$ \omega = \sqrt{K/M}. $$

**Step 2 — Debye frequency.** The Debye model characterizes phonon spectra by a cutoff frequency $\omega_D$ proportional to the maximum lattice vibration frequency. For a monatomic lattice of mass $M$ and spring constant $K$, the dispersion relation at the Brillouin zone boundary gives a frequency $\propto \sqrt{K/M}$. The precise prefactor and Brillouin-zone geometry only introduce a numerical constant that does not depend on $M$, so

**第 2 步 — 德拜频率。** 德拜模型用截止频率 $\omega_D$ 来表征声子谱，$\omega_D$ 正比于晶格振动的最大频率。对于质量为 $M$、弹簧常数为 $K$ 的单原子晶格，布里渊区边界处的色散关系给出正比于 $\sqrt{K/M}$ 的频率。精确的预因子和布里渊区几何只引入不依赖于 $M$ 的数值常数，因此

$$ \omega_D \propto \sqrt{K/M} \propto M^{-1/2} \quad (K \text{ fixed for isotopes}). $$

$$ \omega_D \propto \sqrt{K/M} \propto M^{-1/2} \quad (\text{对同位素 } K \text{ 固定}). $$

**Step 3 — Link between $T_c$ and $\omega_D$ from BCS.** The full BCS gap equation (derived in Module 5.5) gives, in the weak-coupling limit,

**第 3 步 — BCS 给出的 $T_c$ 与 $\omega_D$ 的联系。** 完整的 BCS 能隙方程（在模块 5.5 中推导）在弱耦合极限下给出

$$ \Delta(0) \approx 2 \hbar\omega_D \exp(-1/(g N(0))), $$

and the universal ratio $2\Delta(0) = 3.52\, k_B T_c$ (derived in Module 5.5). These together yield

以及普适比值 $2\Delta(0) = 3.52\, k_B T_c$（在模块 5.5 中推导）。两者合并给出

$$ k_B T_c \approx 1.13\, \hbar\omega_D \exp(-1/(g N(0))). $$

The exponential factor $\exp(-1/(g N(0)))$ and the density of states $N(0)$ and coupling $g$ are electronic properties that do not depend on the isotope mass $M$. Only $\omega_D$ carries $M$ dependence.

指数因子 $\exp(-1/(g N(0)))$ 以及态密度 $N(0)$ 和耦合常数 $g$ 都是不依赖于同位素质量 $M$ 的电子性质。只有 $\omega_D$ 携带 $M$ 的依赖关系。

**Step 4 — Extract the scaling.** Taking $M \to M'$ with all electronic quantities fixed:

**第 4 步 — 提取标度关系。** 令 $M \to M'$，保持所有电子量不变：

$$ T_c(M')/T_c(M) = \omega_D(M')/\omega_D(M) = \sqrt{M/M'}. $$

Equivalently, **$T_c \propto \omega_D \propto M^{-1/2}$**. This is the isotope effect exponent $\alpha = 1/2$ in the general form $T_c \propto M^{-\alpha}$.

等价地，**$T_c \propto \omega_D \propto M^{-1/2}$**。这是一般形式 $T_c \propto M^{-\alpha}$ 中的同位素效应指数 $\alpha = 1/2$。

**Step 5 — Physical interpretation and experimental verification.** The result $\alpha = 1/2$ was measured by Maxwell (1950) and Reynolds et al. (1950) in mercury, confirming that lattice vibrations — phonons — are essential to the pairing mechanism. If the pairing were purely electronic (no phonon involvement), $K$ and $\omega_D$ would be irrelevant and $T_c$ would be independent of $M$ ($\alpha = 0$). The observed $\alpha \approx 1/2$ is direct evidence that phonons mediate the Cooper pairing. Deviations from $\alpha = 1/2$ seen in transition metals (due to Coulomb pseudopotential corrections and band-structure effects) are quantitatively explained by Eliashberg theory. $\blacksquare$

**第 5 步 — 物理解释与实验验证。** 指数 $\alpha = 1/2$ 由麦克斯韦（1950年）和雷诺兹等人（1950年）在汞中测量得到，证实了晶格振动——声子——对配对机制的关键作用。如果配对纯粹是电子的（不涉及声子），$K$ 和 $\omega_D$ 将无关紧要，$T_c$ 将与 $M$ 无关（$\alpha = 0$）。观测到的 $\alpha \approx 1/2$ 是声子介导库珀配对的直接证据。在过渡金属中观察到的偏离 $\alpha = 1/2$ 的现象（由于库仑赝势修正和能带结构效应）可由埃利亚什伯格理论定量解释。$\blacksquare$

---

## C. Thermodynamic Argument: Meissner State as an Equilibrium Phase · 热力学论证：迈斯纳态作为平衡相

**Claim.** Because the Meissner effect is reversible (switching the field on and off cycles the system between normal and superconducting states without hysteresis for a type-I superconductor), the superconducting state is a true thermodynamic equilibrium phase, and the transition is characterized by a thermodynamic critical field $H_c(T)$.

**命题。** 由于迈斯纳效应是可逆的（对 I 型超导体，磁场的开关使系统在正常态和超导态之间循环而无磁滞），超导态是真正的热力学平衡相，该转变由热力学临界磁场 $H_c(T)$ 表征。

**Step 1 — Free energy of the Meissner state.** The superconductor expels $B$ completely ($B = 0$ inside). The energy cost of expelling a field $H$ from a volume $V$ is the magnetic field energy that must be stored in the surrounding space:

**第 1 步 — 迈斯纳态的自由能。** 超导体完全排斥 $B$（内部 $B = 0$）。将磁场 $H$ 从体积 $V$ 中排出所需的能量代价是必须储存在周围空间的磁场能量：

$$ \Delta F_{\text{magnetic}} = \frac{\mu_0}{2} H^2 \quad \text{per unit volume}. $$

**Step 2 — Critical field from free-energy balance.** The condensation energy (the energy gained by going superconducting) must equal the magnetic expulsion cost at the transition. At the critical field $H_c(T)$, the normal and superconducting free energies are equal:

**第 2 步 — 自由能平衡确定临界场。** 凝聚能（超导化获得的能量）必须等于转变时磁场排斥的代价。在临界场 $H_c(T)$ 处，正常态和超导态的自由能相等：

$$ F_n(T) = F_s(T) + \frac{\mu_0}{2} H_c^2(T). $$

Hence the condensation free energy density is

故凝聚自由能密度为

$$ F_n - F_s = \frac{\mu_0}{2} H_c^2(T). $$

**Step 3 — Temperature dependence of $H_c$.** Empirically $H_c(T) \approx H_c(0)\, [1 - (T/T_c)^2]$, consistent with the BCS prediction. At $T = T_c$, $H_c = 0$, confirming the transition is continuous (second-order in zero field). This thermodynamic framework shows the Meissner state is a genuine new phase with lower free energy than the normal state for $T < T_c$ and $H < H_c(T)$. $\blacksquare$

**第 3 步 — $H_c$ 的温度依赖性。** 经验上 $H_c(T) \approx H_c(0)\, [1 - (T/T_c)^2]$，与 BCS 预测一致。在 $T = T_c$ 处，$H_c = 0$，确认转变是连续的（零场中的二级相变）。这个热力学框架表明迈斯纳态是一个真正的新相，对于 $T < T_c$ 且 $H < H_c(T)$，其自由能低于正常态。$\blacksquare$

---

*All results here are elaborated microscopically in Modules 5.2–5.5.*
*此处所有结果均在模块 5.2–5.5 中从微观角度详细阐述。*

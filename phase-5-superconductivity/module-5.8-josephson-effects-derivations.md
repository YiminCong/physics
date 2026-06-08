# Derivations — Module 5.8: Josephson Effects
# 推导 — 模块 5.8：约瑟夫森效应

> Companion to [Module 5.8](./module-5.8-josephson-effects.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 5.8](./module-5.8-josephson-effects.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. DC Josephson Effect: I = I_c sin(Δφ) · 直流约瑟夫森效应

**Claim.** For two superconductors separated by a thin weak link (insulator, normal metal, or constriction), the supercurrent tunneling through the barrier is

  I = I_c sin(φ₁ − φ₂) ≡ I_c sin(Δφ),

where φ₁, φ₂ are the macroscopic phases of the two condensates and I_c is the critical current of the junction.

**命题。** 对由薄弱连接（绝缘体、正常金属或收缩）隔开的两个超导体，穿过势垒的超电流为

  I = I_c sin(φ₁ − φ₂) ≡ I_c sin(Δφ)，

其中 φ₁、φ₂ 为两个凝聚体的宏观相位，I_c 为结的临界电流。

---

**Step 1 — Coupled condensate equations (Feynman approach).** Model each condensate by a macroscopic wavefunction (order parameter) Ψ_j = √n_j e^{iφ_j} (j = 1, 2), where n_j is the Cooper-pair density. Across the thin barrier, the condensates are weakly coupled with strength K (the tunneling amplitude for pairs). The Schrödinger-like equations for the two condensates (treating the barrier as a weak perturbation) are:

  iℏ ∂Ψ₁/∂t = μ₁ Ψ₁ + K Ψ₂,
  iℏ ∂Ψ₂/∂t = μ₂ Ψ₂ + K Ψ₁,

where μ₁ and μ₂ are the chemical potentials of the two sides (related to the voltage by μ₁ − μ₂ = 2eV for Cooper pairs of charge 2e).

**第 1 步 — 耦合凝聚体方程（费曼方法）。** 用宏观波函数（序参量）Ψ_j = √n_j e^{iφ_j}（j = 1, 2）对每个凝聚体建模，n_j 为库珀对密度。在薄势垒两侧，凝聚体以强度 K（对的隧穿振幅）弱耦合。两凝聚体的类薛定谔方程（将势垒作为弱微扰处理）为：

  iℏ ∂Ψ₁/∂t = μ₁ Ψ₁ + K Ψ₂，
  iℏ ∂Ψ₂/∂t = μ₂ Ψ₂ + K Ψ₁，

其中 μ₁、μ₂ 为两侧化学势（对于电荷 2e 的库珀对，与电压的关系为 μ₁ − μ₂ = 2eV）。

**Step 2 — Substitute Ψ_j = √n_j e^{iφ_j} and separate real/imaginary parts.** Writing Ψ₁ = √n₁ e^{iφ₁} and differentiating:

  iℏ (ṅ₁/(2√n₁) + i√n₁ φ̇₁) e^{iφ₁} = μ₁ √n₁ e^{iφ₁} + K √n₂ e^{iφ₂}.

Multiply both sides by e^{−iφ₁}/√n₁:

  iℏ (ṅ₁/(2n₁) + iφ̇₁) = μ₁ + K √(n₂/n₁) e^{i(φ₂−φ₁)}.

Let Δφ = φ₂ − φ₁. Separating real and imaginary parts:

  Real:    −ℏ φ̇₁ = μ₁ + K √(n₂/n₁) cos(Δφ),
  Imag:    ℏ ṅ₁/(2n₁) = K √(n₂/n₁) sin(Δφ).

**第 2 步 — 代入 Ψ_j = √n_j e^{iφ_j} 并分离实虚部。** 写 Ψ₁ = √n₁ e^{iφ₁} 并求导，乘以 e^{−iφ₁}/√n₁：

  iℏ (ṅ₁/(2n₁) + iφ̇₁) = μ₁ + K √(n₂/n₁) e^{i(φ₂−φ₁)}。

令 Δφ = φ₂ − φ₁，分离实虚部：

  实部：    −ℏ φ̇₁ = μ₁ + K √(n₂/n₁) cos(Δφ)，
  虚部：    ℏ ṅ₁/(2n₁) = K √(n₂/n₁) sin(Δφ)。

**Step 3 — The supercurrent is proportional to sin(Δφ).** The imaginary part gives ṅ₁ ∝ sin(Δφ). Since ṅ₁ is the rate of change of Cooper-pair density on side 1, and each pair carries charge 2e, the electric current flowing from side 2 to side 1 is

  I = 2e A ṅ₁ = (2eA · 2n₁K√(n₂/n₁)/ℏ) sin(Δφ) ≡ I_c sin(Δφ),

where A is the junction area and I_c = (2eA · 2K√(n₁n₂)/ℏ) absorbs all the prefactors. For a symmetric junction n₁ = n₂ = n, I_c = 4eAKn/ℏ.

**第 3 步 — 超电流正比于 sin(Δφ)。** 虚部给出 ṅ₁ ∝ sin(Δφ)。由于 ṅ₁ 是第 1 侧库珀对密度的变化率，每对携带电荷 2e，从第 2 侧流向第 1 侧的电流为

  I = 2e A ṅ₁ = (2eA · 2n₁K√(n₂/n₁)/ℏ) sin(Δφ) ≡ I_c sin(Δφ)，

其中 A 为结面积，I_c = (2eA · 2K√(n₁n₂)/ℏ) 吸收了所有前置因子。对对称结 n₁ = n₂ = n，I_c = 4eAKn/ℏ。

**Step 4 — Physical content of the DC effect.** When V = 0 (no voltage applied), μ₁ = μ₂ and the phase difference Δφ is constant (time-independent). The junction then carries a steady supercurrent I = I_c sin(Δφ) with no dissipation. The value of Δφ adjusts to whatever is needed to carry the external current, up to I_c. This is the DC Josephson effect: **supercurrent flows at zero voltage.** ∎

**第 4 步 — 直流效应的物理内涵。** 当 V = 0（无外加电压）时，μ₁ = μ₂，相位差 Δφ 为常数（与时间无关）。结携带稳定的超电流 I = I_c sin(Δφ) 而无耗散。Δφ 自动调整以承载外部电流，最大可达 I_c。这就是直流约瑟夫森效应：**超电流在零电压下流动。**∎

---

## B. AC Josephson Effect: d(Δφ)/dt = 2eV/ℏ · 交流约瑟夫森效应

**Claim.** When a constant voltage V is applied across the junction, the phase difference evolves as d(Δφ)/dt = 2eV/ℏ, leading to an oscillating supercurrent at the Josephson frequency f_J = 2eV/h.

**命题。** 当恒定电压 V 加在结两端时，相位差按 d(Δφ)/dt = 2eV/ℏ 演化，导致超电流以约瑟夫森频率 f_J = 2eV/h 振荡。

**Step 1 — Phase evolution equation from chemical potential difference.** From the real-part equation of Step 2 above (and its counterpart for side 2), the phases evolve as:

  ℏ φ̇₁ = −μ₁ + (small coupling terms),
  ℏ φ̇₂ = −μ₂ + (small coupling terms).

Subtracting (and dropping the coupling terms, which are small for a tunnel junction with K ≪ Δ):

  ℏ d(Δφ)/dt = ℏ(φ̇₂ − φ̇₁) = μ₁ − μ₂.

**第 1 步 — 由化学势差得相位演化方程。** 由上面第 2 步实部方程（及第 2 侧对应方程），相位演化为：

  ℏ φ̇₁ = −μ₁ + （小耦合项），
  ℏ φ̇₂ = −μ₂ + （小耦合项）。

相减（对于 K ≪ Δ 的隧道结，略去小耦合项）：

  ℏ d(Δφ)/dt = ℏ(φ̇₂ − φ̇₁) = μ₁ − μ₂。

**Step 2 — Connect chemical potential to voltage.** The electrochemical potential difference across the junction is the voltage times the pair charge:

  μ₁ − μ₂ = 2eV    (Cooper pairs carry charge 2e).

Hence

  d(Δφ)/dt = 2eV/ℏ.

This is the **Josephson phase-voltage relation** (also called the second Josephson relation).

**第 2 步 — 将化学势与电压相联系。** 结两端的电化学势差等于电压乘以对电荷：

  μ₁ − μ₂ = 2eV    （库珀对携带电荷 2e）。

故

  d(Δφ)/dt = 2eV/ℏ。

这是**约瑟夫森相位–电压关系**（也称第二约瑟夫森关系）。

**Step 3 — Integration to find Δφ(t).** For constant V, integrate:

  Δφ(t) = Δφ(0) + (2eV/ℏ) t = Δφ(0) + 2π (2eV/h) t = Δφ(0) + 2π f_J t,

where the **Josephson frequency** is

  f_J = 2eV/h ≈ (483.6 MHz/μV) × V.

**第 3 步 — 积分求 Δφ(t)。** 对恒定 V 积分：

  Δφ(t) = Δφ(0) + (2eV/ℏ) t = Δφ(0) + 2π (2eV/h) t = Δφ(0) + 2π f_J t，

其中**约瑟夫森频率**为

  f_J = 2eV/h ≈ (483.6 MHz/μV) × V。

**Step 4 — Oscillating supercurrent.** Substituting into I = I_c sin(Δφ):

  I(t) = I_c sin(Δφ(0) + 2π f_J t).

This is an **AC supercurrent** oscillating at frequency f_J. The amplitude is I_c and the frequency is exactly 2eV/h — it contains no material constants, only fundamental constants e and h. This means the Josephson junction is a quantum-mechanical frequency standard: measuring f_J and V gives e/h to extraordinary precision (the basis of the Josephson voltage standard, with 1 V defined via 2e/h). ∎

**第 4 步 — 振荡超电流。** 代入 I = I_c sin(Δφ)：

  I(t) = I_c sin(Δφ(0) + 2π f_J t)。

这是以频率 f_J 振荡的**交流超电流**。振幅为 I_c，频率恰好为 2eV/h——仅包含基本常数 e 和 h，不含材料常数。这意味着约瑟夫森结是量子力学频率标准：测量 f_J 和 V 可以极高精度确定 e/h（约瑟夫森电压标准的基础，1 V 通过 2e/h 定义）。∎

---

## C. The SQUID Interference Pattern: I_max = 2I_c |cos(πΦ/Φ₀)| · SQUID 干涉图样

**Claim.** A DC-SQUID consists of two Josephson junctions connected in parallel in a superconducting loop. The maximum supercurrent is

  I_max(Φ) = 2I_c |cos(πΦ/Φ₀)|,

where Φ is the magnetic flux threading the loop and Φ₀ = h/2e. This is a direct quantum interference effect analogous to a double-slit experiment in optics.

**命题。** 直流 SQUID 由超导回路中并联的两个约瑟夫森结组成。最大超电流为

  I_max(Φ) = 2I_c |cos(πΦ/Φ₀)|，

其中 Φ 为穿过回路的磁通量，Φ₀ = h/2e。这是类似于光学双缝实验的直接量子干涉效应。

**Step 1 — Phase differences across each junction.** Label the two junctions as A and B with phase differences δ_A and δ_B. The total current is

  I = I_c sin(δ_A) + I_c sin(δ_B)    (assuming equal critical currents).

We need to determine the relationship between δ_A and δ_B imposed by the topology of the loop.

**第 1 步 — 每个结上的相位差。** 将两个结标记为 A 和 B，相位差分别为 δ_A 和 δ_B。总电流为

  I = I_c sin(δ_A) + I_c sin(δ_B)    （假设临界电流相等）。

我们需要确定由回路拓扑强加的 δ_A 与 δ_B 的关系。

**Step 2 — Fluxoid quantization around the loop.** Deep inside the superconducting arms of the loop, J_s = 0 (the screening currents die away from the junctions). The fluxoid quantization condition (from Appendix A, Section A, with the contour running through the superconducting bulk of both arms and crossing each junction once):

  (δ_A − δ_B) + (2e/ℏ) Φ = 2πn,    n ∈ ℤ.

Here (2e/ℏ) Φ = 2π Φ/Φ₀ is the gauge contribution from the enclosed flux, and δ_A − δ_B accounts for the phase change through each junction. For n = 0 (single fluxoid quantum):

  δ_A − δ_B = −2πΦ/Φ₀.

**第 2 步 — 回路的磁通量子化条件。** 在回路超导臂的深处，J_s = 0（屏蔽电流从结处消失）。磁通量子化条件（来自附录 A 第 A 节，回路穿过两臂超导体并各通过一次结）：

  (δ_A − δ_B) + (2e/ℏ) Φ = 2πn，    n ∈ ℤ。

这里 (2e/ℏ) Φ = 2π Φ/Φ₀ 是封闭磁通的规范贡献，δ_A − δ_B 计入了穿过每个结的相位变化。取 n = 0（单磁通量子）：

  δ_A − δ_B = −2πΦ/Φ₀。

**Step 3 — Parametrize with sum and difference.** Let the average phase difference be δ̄ = (δ_A + δ_B)/2. Then from Step 2:

  δ_A = δ̄ + πΦ/Φ₀ (taking the sign convention δ_A − δ_B = −2πΦ/Φ₀, swap sign with convention):

Let us use the symmetric parametrization:

  δ_A = δ̄ − πΦ/Φ₀,    δ_B = δ̄ + πΦ/Φ₀.

These satisfy δ_A − δ_B = −2πΦ/Φ₀ as required.

**第 3 步 — 用和与差参数化。** 令平均相位差 δ̄ = (δ_A + δ_B)/2。对称参数化：

  δ_A = δ̄ − πΦ/Φ₀，    δ_B = δ̄ + πΦ/Φ₀。

这满足所需的 δ_A − δ_B = −2πΦ/Φ₀。

**Step 4 — Sum the currents using sum-to-product identity.** The total current:

  I = I_c [sin(δ̄ − πΦ/Φ₀) + sin(δ̄ + πΦ/Φ₀)].

Apply the sum-to-product identity sin(A − B) + sin(A + B) = 2 sin A cos B with A = δ̄ and B = πΦ/Φ₀:

  I = 2 I_c cos(πΦ/Φ₀) sin(δ̄).

**第 4 步 — 用积化和差公式求和。** 总电流：

  I = I_c [sin(δ̄ − πΦ/Φ₀) + sin(δ̄ + πΦ/Φ₀)]。

应用积化和差公式 sin(A − B) + sin(A + B) = 2 sin A cos B，其中 A = δ̄，B = πΦ/Φ₀：

  I = 2 I_c cos(πΦ/Φ₀) sin(δ̄)。

**Step 5 — Maximize over the free phase δ̄.** The average phase δ̄ is the free variable that the circuit adjusts to carry whatever current is demanded. The maximum current (over all δ̄) is achieved at sin(δ̄) = 1:

  I_max(Φ) = 2 I_c |cos(πΦ/Φ₀)|.

The absolute value accounts for both signs of cos. ∎

**第 5 步 — 对自由相位 δ̄ 取最大值。** 平均相位 δ̄ 是电路自动调整以承载所需电流的自由变量。对所有 δ̄ 的最大电流在 sin(δ̄) = 1 时取得：

  I_max(Φ) = 2 I_c |cos(πΦ/Φ₀)|。

绝对值考虑到了 cos 的正负两种情况。∎

**Step 6 — Physical interpretation and sensitivity.** The SQUID interference pattern I_max(Φ) = 2I_c|cos(πΦ/Φ₀)| oscillates with period Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb. Measuring the change in I_max by a fraction of I_c resolves a fraction of Φ₀. Modern SQUIDs achieve flux noise below 10⁻⁶ Φ₀/√Hz, corresponding to magnetic field sensitivities below 1 fT/√Hz — orders of magnitude better than any classical magnetometer. This is used for MEG (magnetoencephalography), SQUID microscopy, and searches for dark matter axions. ∎

**第 6 步 — 物理诠释与灵敏度。** SQUID 干涉图样 I_max(Φ) = 2I_c|cos(πΦ/Φ₀)| 以 Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb 为周期振荡。将 I_max 的变化测量到 I_c 的几分之一即可分辨 Φ₀ 的几分之一。现代 SQUID 的磁通噪声低于 10⁻⁶ Φ₀/√Hz，对应磁场灵敏度低于 1 fT/√Hz——比任何经典磁强计高出数个数量级。这用于脑磁图（MEG）、SQUID 显微镜及暗物质轴子搜索。∎

---

## D. Josephson Relations from the Tunneling Hamiltonian (Alternative Derivation) · 从隧穿哈密顿量推导约瑟夫森关系（另一推导）

**Step 1 — Setup.** In the tunneling Hamiltonian formalism (Cohen–Falicov–Phillips, also used in Module 5.6), the Hamiltonian for two superconductors coupled by a barrier is H = H₁ + H₂ + H_T, where H_T = Σ_{k,q} T_{kq} c†_k d_q + h.c. transfers single electrons, and c†_k, d_q create/annihilate electrons on the two sides.

**第 1 步 — 准备。** 在隧穿哈密顿量形式（Cohen–Falicov–Phillips，模块 5.6 中也用到）中，两个通过势垒耦合的超导体的哈密顿量为 H = H₁ + H₂ + H_T，其中 H_T = Σ_{k,q} T_{kq} c†_k d_q + h.c. 传递单个电子，c†_k、d_q 在两侧分别产生/湮灭电子。

**Step 2 — Pair tunneling at second order.** To lowest order in T, only single-electron transfer is present (this is the Giaever tunneling of Module 5.6). However, for Cooper-pair tunneling, we must go to **second order in T**: two simultaneous single-electron tunneling events constitute one pair transfer. The effective pair tunneling Hamiltonian at second order is

  H_pair ∝ Σ_{k,q} (T_{kq})² (c†_{k↑}c†_{−k↓})(d_{−q↓}d_{q↑}) + h.c.,

which, in BCS language, involves the anomalous averages ⟨c†_{k↑}c†_{−k↓}⟩ = u_k v_k e^{iφ₁} and ⟨d_{q↓}d_{−q↑}⟩ = u_q v_q e^{iφ₂}. Evaluating expectation values:

  ⟨H_pair⟩ ∝ |Δ₁||Δ₂| sin(φ₁ − φ₂)·(−1) = −E_J cos(Δφ),

where E_J ∝ |Δ₁||Δ₂|/R_T is the Josephson coupling energy and R_T is the tunnel resistance.

**第 2 步 — 二阶对隧穿。** 在 T 的最低阶，仅有单电子转移（模块 5.6 的贾埃弗隧穿）。然而对于库珀对隧穿，必须到 **T 的二阶**：两个同时发生的单电子隧穿事件构成一次对转移。二阶有效对隧穿哈密顿量为

  H_pair ∝ Σ_{k,q} (T_{kq})² (c†_{k↑}c†_{−k↓})(d_{−q↓}d_{q↑}) + h.c.，

用 BCS 语言，涉及反常平均 ⟨c†_{k↑}c†_{−k↓}⟩ = u_k v_k e^{iφ₁} 和 ⟨d_{q↓}d_{−q↑}⟩ = u_q v_q e^{iφ₂}。取期望值：

  ⟨H_pair⟩ ∝ |Δ₁||Δ₂| sin(φ₁ − φ₂)·(−1) = −E_J cos(Δφ)，

其中 E_J ∝ |Δ₁||Δ₂|/R_T 为约瑟夫森耦合能，R_T 为隧穿电阻。

**Step 3 — Current from the energy.** The supercurrent is the derivative of the total energy with respect to the phase (this follows from the general relation I = (2e/ℏ) ∂E/∂(Δφ), the supercurrent–phase relation in thermodynamics):

  I = (2e/ℏ) ∂(−E_J cos Δφ)/∂(Δφ) = (2e/ℏ) E_J sin(Δφ) ≡ I_c sin(Δφ),

where I_c = 2eE_J/ℏ. This confirms the Feynman result and relates I_c to the microscopic tunneling matrix element. The **Ambegaokar–Baratoff formula** (1963) gives explicitly:

  I_c R_T = (π/2e) Δ(T) tanh(Δ(T)/2k_BT),

at T = 0: I_c R_T = πΔ/(2e). ∎

**第 3 步 — 由能量得电流。** 超电流是总能量对相位的导数（由热力学中的一般关系 I = (2e/ℏ) ∂E/∂(Δφ) 得到，即超电流–相位关系）：

  I = (2e/ℏ) ∂(−E_J cos Δφ)/∂(Δφ) = (2e/ℏ) E_J sin(Δφ) ≡ I_c sin(Δφ)，

其中 I_c = 2eE_J/ℏ。这证实了费曼结果，并将 I_c 与微观隧穿矩阵元联系起来。**安贝加尔–巴拉托夫公式**（1963）给出明确形式：

  I_c R_T = (π/2e) Δ(T) tanh(Δ(T)/2k_BT)，

T = 0 时：I_c R_T = πΔ/(2e)。∎

---

*Summary of Josephson physics: the DC relation I = I_c sin(Δφ) emerges from the coherent coupling between macroscopic quantum phases; the AC relation d(Δφ)/dt = 2eV/ℏ follows from the energy difference between condensates at different chemical potentials; the SQUID result I_max = 2I_c|cos(πΦ/Φ₀)| is a direct application of fluxoid quantization plus the sum-to-product identity. All three are macroscopic quantum effects.*

*约瑟夫森物理总结：直流关系 I = I_c sin(Δφ) 来自宏观量子相位之间的相干耦合；交流关系 d(Δφ)/dt = 2eV/ℏ 来自不同化学势下凝聚体间的能量差；SQUID 结果 I_max = 2I_c|cos(πΦ/Φ₀)| 是磁通量子化条件与积化和差公式的直接应用。三者均为宏观量子效应。*

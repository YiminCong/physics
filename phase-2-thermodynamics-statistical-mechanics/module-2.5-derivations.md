# Derivations — Module 2.5: Quantum Statistics
# 推导 — 模块 2.5：量子统计

> Companion to [Module 2.5](./module-2.5-quantum-statistics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.5](./module-2.5-quantum-statistics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Fermi–Dirac Distribution from the Grand Canonical Ensemble · 从巨正则系综推导费米–狄拉克分布

**Claim.** For a system of non-interacting fermions in thermal and diffusive contact with a reservoir at temperature T and chemical potential μ, the mean occupation number of a single-particle state with energy ε is

**命题。** 对于与温度为 T、化学势为 μ 的热库处于热接触和粒子交换接触的非相互作用费米子系统，能量为 ε 的单粒子态的平均占据数为

  n_FD(ε) = 1 / (e^{(ε − μ)/k_BT} + 1).

**Step 1 — Identify the relevant ensemble and sub-system.** Since particle number is not fixed, we use the grand canonical ensemble. The key observation for non-interacting particles is that each single-particle state α is an independent sub-system that can be analyzed separately. The state of sub-system α is characterized solely by its occupation number n_α.

**第 1 步 — 确定相关系综和子系统。** 由于粒子数不固定，我们使用巨正则系综。对于非相互作用粒子，关键观察是每个单粒子态 α 是一个可独立分析的子系统。子系统 α 的状态完全由其占据数 n_α 刻画。

**Step 2 — Pauli exclusion restricts n_α to 0 or 1.** Fermions obey the Pauli exclusion principle: no two fermions can occupy the same single-particle state. Therefore n_α ∈ {0, 1}.

**第 2 步 — 泡利不相容原理将 n_α 限制为 0 或 1。** 费米子服从泡利不相容原理：不能有两个费米子占据同一单粒子态。因此 n_α ∈ {0, 1}。

**Step 3 — Write the grand canonical partition function for state α.** The grand canonical statistical weight for state α with occupation n_α is e^{−β(ε_α − μ)n_α}, where β = 1/(k_BT). Summing over the two allowed values:

**第 3 步 — 写出态 α 的巨正则配分函数。** 占据数为 n_α 的态 α 的巨正则统计权重为 e^{−β(ε_α − μ)n_α}，其中 β = 1/(k_BT)。对两个允许值求和：

  z_α = Σ_{n_α=0}^{1} e^{−β(ε_α − μ)n_α} = e^0 + e^{−β(ε_α − μ)} = 1 + e^{−β(ε_α − μ)}.

**Step 4 — Compute the mean occupation number.** Using the grand canonical average:

**第 4 步 — 计算平均占据数。** 使用巨正则平均：

  ⟨n_α⟩ = Σ_{n=0}^{1} n · e^{−β(ε_α − μ)n} / z_α
          = [0 · 1 + 1 · e^{−β(ε_α − μ)}] / [1 + e^{−β(ε_α − μ)}]
          = e^{−β(ε_α − μ)} / [1 + e^{−β(ε_α − μ)}].

**Step 5 — Simplify by multiplying numerator and denominator by e^{β(ε_α − μ)}.**

**第 5 步 — 分子分母同乘 e^{β(ε_α − μ)} 化简。**

  ⟨n_α⟩ = 1 / [e^{β(ε_α − μ)} + 1] = **1 / (e^{(ε_α − μ)/k_BT} + 1) = n_FD(ε_α).** ∎

---

## B. Bose–Einstein Distribution from the Grand Canonical Ensemble · 从巨正则系综推导玻色–爱因斯坦分布

**Claim.** For non-interacting bosons, the mean occupation of a single-particle state with energy ε is

**命题。** 对于非相互作用玻色子，能量为 ε 的单粒子态的平均占据数为

  n_BE(ε) = 1 / (e^{(ε − μ)/k_BT} − 1).

**Step 1 — Bosons have no restriction on occupation.** Unlike fermions, any number of bosons can occupy the same state: n_α ∈ {0, 1, 2, 3, …}.

**第 1 步 — 玻色子对占据数无限制。** 与费米子不同，任意数目的玻色子可以占据同一态：n_α ∈ {0, 1, 2, 3, …}。

**Step 2 — Write the grand canonical partition function.** Let x = e^{−β(ε_α − μ)}. The partition function is a geometric series:

**第 2 步 — 写出巨正则配分函数。** 令 x = e^{−β(ε_α − μ)}。配分函数是等比级数：

  z_α = Σ_{n=0}^{∞} e^{−β(ε_α − μ)n} = Σ_{n=0}^{∞} x^n.

For convergence, we need |x| < 1, i.e., e^{−β(ε_α − μ)} < 1, i.e., ε_α > μ. This is why μ must be less than the ground-state energy for bosons (otherwise the series diverges and the theory breaks down). Summing the geometric series:

为使级数收敛，需要 |x| < 1，即 e^{−β(ε_α − μ)} < 1，即 ε_α > μ。这就是为什么玻色子的化学势必须小于基态能量的原因（否则级数发散，理论失效）。求等比级数之和：

  z_α = 1/(1 − x) = 1/(1 − e^{−β(ε_α − μ)}).

**Step 3 — Compute the mean occupation.** Using ⟨n_α⟩ = −(1/β)(∂ ln z_α/∂ε_α):

**第 3 步 — 计算平均占据数。** 利用 ⟨n_α⟩ = −(1/β)(∂ ln z_α/∂ε_α)：

  ln z_α = −ln(1 − e^{−β(ε_α − μ)}),
  ∂ ln z_α/∂ε_α = −[−β e^{−β(ε_α − μ)}] / (1 − e^{−β(ε_α − μ)})
                 = β e^{−β(ε_α − μ)} / (1 − e^{−β(ε_α − μ)}).

Therefore:

因此：

  ⟨n_α⟩ = −(1/β) · β e^{−β(ε_α − μ)} / (1 − e^{−β(ε_α − μ)})
          = e^{−β(ε_α − μ)} / (1 − e^{−β(ε_α − μ)}).

**Step 4 — Simplify.** Multiplying numerator and denominator by e^{β(ε_α − μ)}:

**第 4 步 — 化简。** 分子分母同乘 e^{β(ε_α − μ)}：

  ⟨n_α⟩ = 1 / (e^{β(ε_α − μ)} − 1) = **1 / (e^{(ε_α − μ)/k_BT} − 1) = n_BE(ε_α).** ∎

**Step 5 — Compare the two distributions.** The Fermi–Dirac and Bose–Einstein distributions differ only in the sign in the denominator: +1 for fermions, −1 for bosons. Both reduce to the classical Maxwell–Boltzmann distribution n ∝ e^{−β(ε−μ)} when e^{β(ε−μ)} ≫ 1, i.e., when e^{βμ} ≪ 1 (low fugacity, high temperature, or low density).

**第 5 步 — 比较两种分布。** 费米–狄拉克分布和玻色–爱因斯坦分布仅在分母的符号上不同：费米子为 +1，玻色子为 −1。当 e^{β(ε−μ)} ≫ 1 时，即当 e^{βμ} ≪ 1（低逸度、高温或低密度），两者均退化为经典麦克斯韦–玻尔兹曼分布 n ∝ e^{−β(ε−μ)}。

---

## C. Chemical Potential and the Fermi Energy · 化学势与费米能

**Claim.** For a free electron gas in 3D at T = 0, the chemical potential equals the Fermi energy E_F = (ℏ²/2m)(3π²n)^{2/3}, where n = N/V is the electron number density.

**命题。** 对于三维自由电子气，T = 0 时化学势等于费米能 E_F = (ℏ²/2m)(3π²n)^{2/3}，其中 n = N/V 为电子数密度。

**Step 1 — At T = 0, n_FD is a step function.** The Fermi–Dirac distribution at T = 0 is

**第 1 步 — T = 0 时，n_FD 是阶跃函数。** T = 0 时的费米–狄拉克分布为

  n_FD(ε) = 1 if ε < μ(T=0),   n_FD(ε) = 0 if ε > μ(T=0).

The chemical potential at T = 0 is defined as the Fermi energy: μ(T=0) = E_F.

T = 0 时的化学势定义为费米能：μ(T=0) = E_F。

**Step 2 — Count the states.** For free electrons in a box of volume V with periodic boundary conditions, the allowed wave vectors are k = (2π/L)(n_x, n_y, n_z), giving a density of states in k-space of V/(2π)³ per unit volume of k-space. Including the factor of 2 for electron spin, the total number of states with |k| ≤ k_F is

**第 2 步 — 计算状态数。** 对于体积为 V 的箱中具有周期边界条件的自由电子，允许的波矢为 k = (2π/L)(n_x, n_y, n_z)，在 k 空间单位体积内的态密度为 V/(2π)³。包含电子自旋的因子 2，|k| ≤ k_F 的总态数为

  N = 2 · V/(2π)³ · (4π/3) k_F³ = V k_F³ / (3π²).

**Step 3 — Solve for k_F in terms of n.** From n = N/V:

**第 3 步 — 用 n 求解 k_F。** 由 n = N/V：

  n = k_F³/(3π²)  ⟹  k_F = (3π²n)^{1/3}.

**Step 4 — Compute E_F.** The Fermi energy is the kinetic energy at the Fermi wavevector:

**第 4 步 — 计算 E_F。** 费米能是费米波矢处的动能：

  **E_F = ℏ²k_F²/(2m) = (ℏ²/2m)(3π²n)^{2/3}.** ∎

For copper with n ≈ 8.5 × 10²⁸ m⁻³, this gives E_F ≈ 7 eV, so T_F = E_F/k_B ≈ 81 000 K, confirming that room-temperature electrons are deeply degenerate.

对于铜，n ≈ 8.5 × 10²⁸ m⁻³，由此给出 E_F ≈ 7 eV，故 T_F = E_F/k_B ≈ 81 000 K，证实室温下电子是深度简并的。

---

## D. Classical Limit and the Maxwell–Boltzmann Distribution · 经典极限与麦克斯韦–玻尔兹曼分布

**Claim.** When e^{β(ε−μ)} ≫ 1 for all occupied states (high temperature or low density), both quantum distributions reduce to n(ε) ≈ e^{βμ} e^{−βε}, recovering the Maxwell–Boltzmann distribution.

**命题。** 当所有占据态满足 e^{β(ε−μ)} ≫ 1（高温或低密度）时，两种量子分布均退化为 n(ε) ≈ e^{βμ} e^{−βε}，回归麦克斯韦–玻尔兹曼分布。

**Step 1 — Taylor expand for large argument.** When e^{β(ε−μ)} ≡ y ≫ 1:

**第 1 步 — 对大参数进行泰勒展开。** 当 e^{β(ε−μ)} ≡ y ≫ 1 时：

  n_FD = 1/(y + 1) ≈ 1/y = e^{−β(ε−μ)} = e^{βμ} e^{−βε},
  n_BE = 1/(y − 1) ≈ 1/y = e^{−β(ε−μ)} = e^{βμ} e^{−βε}.

Both give the same classical result. The chemical potential μ is then determined by normalization Σ_ε n(ε) = N, giving e^{βμ} = N/z where z is the single-particle partition function. ∎

两者给出相同的经典结果。化学势 μ 由归一化条件 Σ_ε n(ε) = N 确定，给出 e^{βμ} = N/z，其中 z 是单粒子配分函数。∎

---

*The grand canonical derivations here — summing over occupation numbers with the geometric series for bosons and the two-state sum for fermions — are reproduced identically in the derivations of the Planck distribution for photons (Module 2.6) and the BCS gap equation for superconductors (Module 5.1). The denominator sign ± 1 carries all the physics of quantum statistics.*

*此处的巨正则推导——对玻色子用等比级数求和、对费米子用二态求和——在光子的普朗克分布（模块 2.6）和超导体的 BCS 能隙方程（模块 5.1）的推导中完全重现。分母的 ±1 符号承载了量子统计的全部物理内涵。*

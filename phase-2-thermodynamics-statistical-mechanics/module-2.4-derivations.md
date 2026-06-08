# Derivations — Module 2.4: Classical Statistical Mechanics
# 推导 — 模块 2.4：经典统计力学

> ✅ **Verified 2026-06-08** — derivations reviewed line-by-line and confirmed (or corrected) against standard results; safe to skip on re-verification unless this file changes after the date above. <!-- verified:2026-06-08 -->
> ✅ **已校验 2026-06-08** — 推导已逐行复核，并对照标准结果确认（或更正）；除非本文件在上述日期之后被修改，否则再次校验时可跳过。

> Companion to [Module 2.4](./module-2.4-classical-statistical-mechanics.md). Full step-by-step proofs of the results quoted there. English first, then 中文.
> [模块 2.4](./module-2.4-classical-statistical-mechanics.md) 的配套文档：对该模块所引用结果的完整逐步证明。先英文，后中文。

---

## A. Boltzmann Distribution from Maximum Entropy · 从最大熵推导玻尔兹曼分布

**Claim.** For a system in thermal contact with a reservoir at temperature T, the equilibrium probability of microstate i with energy E_i is p_i = e^{−βE_i}/Z, where β = 1/(k_BT) and Z = Σ_i e^{−βE_i}.

**命题。** 对于与温度为 T 的热库热接触的系统，能量为 E_i 的微观态 i 的平衡概率为 p_i = e^{−βE_i}/Z，其中 β = 1/(k_BT)，Z = Σ_i e^{−βE_i}。

**Step 1 — Set up the constrained maximization.** We seek the probability distribution {p_i} that maximizes the Gibbs–Boltzmann entropy

**第 1 步 — 建立约束极大化问题。** 我们寻找使吉布斯–玻尔兹曼熵极大的概率分布 {p_i}

  S[{p_i}] = −k_B Σ_i p_i ln p_i,

subject to two constraints:

在两个约束条件下：

  (1) Normalization:   Σ_i p_i = 1,
  (2) Fixed mean energy:   Σ_i p_i E_i = U   (fixed by reservoir temperature T).

**Step 2 — Introduce Lagrange multipliers.** Form the Lagrangian

**第 2 步 — 引入拉格朗日乘子。** 构造拉格朗日量

  L = −k_B Σ_i p_i ln p_i − λ (Σ_i p_i − 1) − β k_B (Σ_i p_i E_i − U),

where λ and β are undetermined multipliers for the two constraints.

其中 λ 和 β 是两个约束条件对应的待定乘子。

**Step 3 — Differentiate with respect to p_j and set to zero.** For each j:

**第 3 步 — 对 p_j 微分并令其为零。** 对每个 j：

  ∂L/∂p_j = −k_B (ln p_j + 1) − λ − β k_B E_j = 0.

Solving for p_j:

求解 p_j：

  ln p_j = −1 − λ/k_B − β E_j,
  p_j = exp(−1 − λ/k_B) · exp(−β E_j) = C · e^{−β E_j},

where C = e^{−1 − λ/k_B} is a constant.

其中 C = e^{−1 − λ/k_B} 是常数。

**Step 4 — Fix the constant via normalization.** Applying Σ_j p_j = 1:

**第 4 步 — 通过归一化确定常数。** 应用 Σ_j p_j = 1：

  C Σ_j e^{−β E_j} = 1  ⟹  C = 1/Z,   where  Z = Σ_j e^{−β E_j}.

Therefore the Boltzmann distribution is

因此玻尔兹曼分布为

  **p_j = e^{−β E_j} / Z.** ∎

**Step 5 — Identify β with temperature.** To connect β to the thermodynamic temperature T, compute the entropy:

**第 5 步 — 将 β 与温度对应。** 为将 β 与热力学温度 T 联系起来，计算熵：

  S = −k_B Σ_j p_j ln p_j = −k_B Σ_j p_j (−β E_j − ln Z)
    = k_B β Σ_j p_j E_j + k_B ln Z = k_B β U + k_B ln Z.

From thermodynamics, dS/dU = 1/T (at fixed V), so

由热力学，dS/dU = 1/T（固定 V），故

  ∂S/∂U = k_B β = 1/T  ⟹  **β = 1/(k_BT).** ∎

---

## B. Partition Function, Free Energy, and Average Energy · 配分函数、自由能与平均能量

**Claim.** With Z = Σ_i e^{−βE_i}, the Helmholtz free energy is F = −k_BT ln Z and the mean energy is U = −∂(ln Z)/∂β.

**命题。** 令 Z = Σ_i e^{−βE_i}，则亥姆霍兹自由能为 F = −k_BT ln Z，平均能量为 U = −∂(ln Z)/∂β。

**Step 1 — Derive F = −k_BT ln Z.** From Step 5 above, S = k_B β U + k_B ln Z. Now F = U − TS:

**第 1 步 — 推导 F = −k_BT ln Z。** 由上述第 5 步，S = k_B β U + k_B ln Z。现在 F = U − TS：

  F = U − T(k_B β U + k_B ln Z) = U − k_BT · (U/k_BT) − k_BT ln Z = U − U − k_BT ln Z,

  **F = −k_BT ln Z.** ∎

**Step 2 — Derive U = −∂(ln Z)/∂β.** The mean energy is

**第 2 步 — 推导 U = −∂(ln Z)/∂β。** 平均能量为

  U = Σ_i p_i E_i = Σ_i (e^{−βE_i}/Z) E_i = (1/Z) Σ_i E_i e^{−βE_i}.

Observe that ∂/∂β [e^{−βE_i}] = −E_i e^{−βE_i}, so Σ_i E_i e^{−βE_i} = −∂Z/∂β. Therefore

注意到 ∂/∂β [e^{−βE_i}] = −E_i e^{−βE_i}，故 Σ_i E_i e^{−βE_i} = −∂Z/∂β。因此

  U = (1/Z)(−∂Z/∂β) = −(1/Z)(∂Z/∂β) = **−∂(ln Z)/∂β.** ∎

**Step 3 — Derive S from F.** Using S = −(∂F/∂T)_V = ∂(k_BT ln Z)/∂T:

**第 3 步 — 从 F 推导 S。** 利用 S = −(∂F/∂T)_V = ∂(k_BT ln Z)/∂T：

  S = k_B ln Z + k_BT (∂ ln Z/∂T)_V = k_B ln Z + k_B β U = k_B(ln Z + β U). ∎

This confirms the consistency with the result from Step 5 of section A.

这与第 A 节第 5 步的结果一致，验证了自洽性。

---

## C. Equipartition Theorem: ⟨½mv²⟩ = (3/2)k_BT · 能均分定理：⟨½mv²⟩ = (3/2)k_BT

**Claim.** For a classical system whose Hamiltonian contains a term ½m v_x² (or any term of the form ½ A q² for a generalized coordinate q with constant A), the thermal average of that term is ½ k_BT. For a free particle in 3D, ⟨½m|v|²⟩ = ½m(⟨v_x²⟩ + ⟨v_y²⟩ + ⟨v_z²⟩) = (3/2)k_BT.

**命题。** 对于哈密顿量中含有 ½m v_x²（或任何形如 ½ A q² 的项，q 为广义坐标，A 为常数）的经典系统，该项的热平均值为 ½ k_BT。对于三维自由粒子，⟨½m|v|²⟩ = ½m(⟨v_x²⟩ + ⟨v_y²⟩ + ⟨v_z²⟩) = (3/2)k_BT。

**Step 1 — Write the Boltzmann average for one degree of freedom.** For one Cartesian velocity component v_x, the probability density is proportional to e^{−βm v_x²/2}, and the canonical average is

**第 1 步 — 对一个自由度写出玻尔兹曼平均。** 对于一个笛卡尔速度分量 v_x，概率密度正比于 e^{−βm v_x²/2}，正则平均为

  ⟨½m v_x²⟩ = ∫_{−∞}^{∞} ½m v_x² e^{−βm v_x²/2} dv_x / ∫_{−∞}^{∞} e^{−βm v_x²/2} dv_x.

**Step 2 — Evaluate using Gaussian integrals.** Using the standard Gaussian integrals (with a = βm/2 > 0):

**第 2 步 — 用高斯积分求值。** 利用标准高斯积分（a = βm/2 > 0）：

  ∫_{−∞}^{∞} e^{−av²} dv = √(π/a),
  ∫_{−∞}^{∞} v² e^{−av²} dv = (1/2)√(π/a³)   [by differentiation: −d/da of the first integral].

Therefore the denominator is √(π/a) and the numerator is ½m · (1/2)√(π/a³):

因此分母为 √(π/a)，分子为 ½m · (1/2)√(π/a³)：

  ⟨½m v_x²⟩ = [½m · (1/2)√(π/a³)] / √(π/a)
             = (m/4) · (1/a) = (m/4) · (2/βm) = 1/(2β) = **½ k_BT.** ∎

**Step 3 — Sum over three dimensions.** By isotropy, ⟨v_x²⟩ = ⟨v_y²⟩ = ⟨v_z²⟩, so

**第 3 步 — 对三维求和。** 由各向同性，⟨v_x²⟩ = ⟨v_y²⟩ = ⟨v_z²⟩，故

  ⟨½m|v|²⟩ = ½m(⟨v_x²⟩ + ⟨v_y²⟩ + ⟨v_z²⟩) = 3 · ½ k_BT = **(3/2)k_BT.** ∎

**Step 4 — General statement of equipartition.** More generally, for any term of the form H_i = ½ A q_i² in the Hamiltonian where q_i ranges from −∞ to ∞ and A is independent of q_i:

**第 4 步 — 能均分定理的一般表述。** 更一般地，对于哈密顿量中任何形如 H_i = ½ A q_i² 的项，其中 q_i 从 −∞ 到 ∞，A 与 q_i 无关：

  ⟨½ A q_i²⟩ = ½ k_BT.

Proof: ⟨½ A q²⟩ = ∫ ½Aq² e^{−β·½Aq²} dq / ∫ e^{−β·½Aq²} dq. With a = βA/2, this equals (1/4a)(A) = A/(4βA/2) = 1/(2β) = ½ k_BT, by the same Gaussian integral calculation as above. This applies equally to kinetic energy terms (½mv²) and harmonic potential energy terms (½kx²). ∎

证明：⟨½ A q²⟩ = ∫ ½Aq² e^{−β·½Aq²} dq / ∫ e^{−β·½Aq²} dq。令 a = βA/2，等于 (1/4a)(A) = A/(4βA/2) = 1/(2β) = ½ k_BT，与上述高斯积分计算相同。这同样适用于动能项（½mv²）和谐振势能项（½kx²）。∎

**Step 5 — Failure of equipartition and the quantum correction.** Equipartition requires that (i) the degree of freedom is classical, (ii) the energy is quadratic, and (iii) the variable ranges over all reals. It fails when ℏω ≫ k_BT (quantum freeze-out): a harmonic oscillator with quantum spacing ℏω has average energy ⟨E⟩ = ℏω/(e^{βℏω} − 1) → k_BT only when k_BT ≫ ℏω. This is why vibrational modes of molecules and phonons at low T contribute less than equipartition predicts.

**第 5 步 — 能均分定理的失效与量子修正。** 能均分定理要求：(i) 自由度是经典的，(ii) 能量是二次型，(iii) 变量遍历所有实数。当 ℏω ≫ k_BT 时失效（量子冻结）：量子间距为 ℏω 的谐振子具有平均能量 ⟨E⟩ = ℏω/(e^{βℏω} − 1) → k_BT 仅当 k_BT ≫ ℏω 时。这就是为什么分子的振动模式和低温声子的贡献小于能均分定理预测值的原因。

---

## D. Boltzmann's Relation S = k_B ln Ω from the Canonical Ensemble · 从正则系综推导玻尔兹曼关系 S = k_B ln Ω

**Claim.** In the microcanonical ensemble (isolated system), the thermodynamic entropy S equals k_B ln Ω, where Ω is the number of accessible microstates.

**命题。** 在微正则系综（孤立系统）中，热力学熵 S 等于 k_B ln Ω，其中 Ω 为可及微观态数目。

**Step 1 — Maximum entropy principle in the microcanonical ensemble.** In an isolated system with fixed E, V, N, all Ω microstates are equally probable (fundamental postulate). The Gibbs entropy is

**第 1 步 — 微正则系综中的最大熵原理。** 在能量 E、体积 V、粒子数 N 固定的孤立系统中，所有 Ω 个微观态等概率出现（基本假设）。吉布斯熵为

  S = −k_B Σ_{i=1}^{Ω} p_i ln p_i = −k_B Σ_{i=1}^{Ω} (1/Ω) ln(1/Ω) = −k_B · Ω · (1/Ω)·(−ln Ω) = **k_B ln Ω.** ∎

**Step 2 — Consistency with the canonical result.** In the canonical ensemble, S = k_B(ln Z + βU). For a macroscopic system with sharp energy distribution (relative fluctuation σ_E/U ~ 1/√N → 0), the sum Z ≈ Ω(U) e^{−βU} (where Ω(U) is the density of states at energy U times the energy window). Then

**第 2 步 — 与正则结果的一致性。** 在正则系综中，S = k_B(ln Z + βU)。对于具有尖锐能量分布（相对涨落 σ_E/U ~ 1/√N → 0）的宏观系统，Z ≈ Ω(U) e^{−βU}（其中 Ω(U) 是能量 U 处的态密度乘以能量窗口），则

  ln Z ≈ ln Ω(U) − βU,
  S ≈ k_B(ln Ω(U) − βU + βU) = k_B ln Ω(U). ∎

The two ensembles agree in the thermodynamic limit, justifying using whichever ensemble is most convenient for a given calculation.

两种系综在热力学极限下一致，这为在给定计算中使用最方便的系综提供了依据。

---

*The derivations here — maximum entropy with Lagrange multipliers, Gaussian integrals, and ensemble equivalence — are the three core technical tools of classical statistical mechanics. They recur verbatim in quantum statistics (Module 2.5) and in the path-integral formulation of quantum field theory (Module 6.1).*

*此处的推导——带拉格朗日乘子的最大熵、高斯积分和系综等价——是经典统计力学的三个核心技术工具。它们在量子统计（模块 2.5）和量子场论的路径积分表述（模块 6.1）中逐字重现。*

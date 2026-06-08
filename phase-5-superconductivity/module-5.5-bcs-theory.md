# Module 5.5 — BCS Theory ⭐⭐
**模块 5.5 — BCS 理论 ⭐⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.5-bcs-theory-derivations.md)

---

## 1. The Microscopic Theory · 微观理论

**Definition.** Bardeen–Cooper–Schrieffer: the **phonon-mediated attraction** (Module 4.5) binds Cooper pairs, and the ground state is a coherent quantum superposition in which all pairs occupy a single macroscopic wavefunction. An **energy gap Δ** opens at the Fermi surface; the elementary excitations are **Bogoliubov quasiparticles** with energy E_k = √(ε_k² + Δ²).

**定义。** 巴丁–库珀–施里弗：**声子介导的吸引力**（模块 4.5）将库珀对束缚在一起，基态是所有对占据同一宏观波函数的相干量子叠加态。费米面处打开一个**能隙 Δ**；基本激发为**博戈留波夫准粒子**，能量为 E_k = √(ε_k² + Δ²)。

## 2. The Hamiltonian and the Gap Equation · 哈密顿量与能隙方程

**Demonstration.** In second quantization (Module 3.12) the **BCS Hamiltonian** is

  H = Σ_k ε_k c_k† c_k − g Σ_{k,k′} c_{k′↑}† c_{−k′↓}† c_{−k↓} c_{k↑},

with the **pair creation operator** c_{k↑}† c_{−k↓}†. Self-consistency yields the **gap equation**, whose weak-coupling solution is

  Δ ≈ 2 ℏω_D e^{−1/(g N(0))},

and the famous universal ratio **2Δ(0) ≈ 3.5 k_B T_c**, plus a characteristic jump in heat capacity at T_c.

**演示。** 用二次量子化（模块 3.12）写出 **BCS 哈密顿量**：

  H = Σ_k ε_k c_k† c_k − g Σ_{k,k′} c_{k′↑}† c_{−k′↓}† c_{−k↓} c_{k↑},

其中 **对产生算符**为 c_{k↑}† c_{−k↓}†。自洽求解给出**能隙方程**，其弱耦合解为

  Δ ≈ 2 ℏω_D e^{−1/(g N(0))},

以及著名的普适比值 **2Δ(0) ≈ 3.5 k_B T_c**，以及在 T_c 处热容的特征跳变。

**Application.** This is the triumph that ties the whole curriculum together: it explains zero resistance, the gap, the isotope effect, and the thermodynamics — and it uses *every* load-bearing module (second quantization, Fermi surface, phonons, free energy, singlet pairing). If you understand the gap equation, you understand conventional superconductivity.

**应用。** 这是将整个课程贯穿起来的成就：它解释了零电阻、能隙、同位素效应和热力学——并使用了*每一个*关键模块（二次量子化、费米面、声子、自由能、单态配对）。如果你理解了能隙方程，就理解了常规超导性。

---

← Previous: [Module 5.4 — The Cooper Problem](./module-5.4-the-cooper-problem.md) · [Phase 5 index](./README.md) · Next: [Module 5.6 — Tunneling & the Gap](./module-5.6-tunneling-and-the-gap.md) →

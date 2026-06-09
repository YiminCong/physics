# Module 5.5 — BCS Theory ⭐⭐
**模块 5.5 — BCS 理论 ⭐⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.5-bcs-theory-derivations.md)

---

## 1. The Microscopic Theory · 微观理论

**Definition.** Bardeen–Cooper–Schrieffer: the **phonon-mediated attraction** (Module 4.5) binds Cooper pairs, and the ground state is a coherent quantum superposition in which all pairs occupy a single macroscopic wavefunction. An **energy gap $\Delta$** opens at the Fermi surface; the elementary excitations are **Bogoliubov quasiparticles** with energy $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$.

**定义。** 巴丁–库珀–施里弗：**声子介导的吸引力**（模块 4.5）将库珀对束缚在一起，基态是所有对占据同一宏观波函数的相干量子叠加态。费米面处打开一个**能隙 $\Delta$**；基本激发为**博戈留波夫准粒子**，能量为 $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$。

## 2. The Hamiltonian and the Gap Equation · 哈密顿量与能隙方程

**Demonstration.** In second quantization (Module 3.12) the **BCS Hamiltonian** is

$$ H = \sum_k \varepsilon_k\, c_k^\dagger c_k - g \sum_{k,k'} c_{k'\uparrow}^\dagger c_{-k'\downarrow}^\dagger c_{-k\downarrow} c_{k\uparrow}, $$

with the **pair creation operator** $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$. Self-consistency yields the **gap equation**, whose weak-coupling solution is

$$ \Delta \approx 2\, \hbar\omega_D\, e^{-1/(g N(0))}, $$

and the famous universal ratio $2\Delta(0) \approx 3.5\, k_B T_c$, plus a characteristic jump in heat capacity at $T_c$.

**演示。** 用二次量子化（模块 3.12）写出 **BCS 哈密顿量**：

$$ H = \sum_k \varepsilon_k\, c_k^\dagger c_k - g \sum_{k,k'} c_{k'\uparrow}^\dagger c_{-k'\downarrow}^\dagger c_{-k\downarrow} c_{k\uparrow}, $$

其中 **对产生算符**为 $c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger$。自洽求解给出**能隙方程**，其弱耦合解为

$$ \Delta \approx 2\, \hbar\omega_D\, e^{-1/(g N(0))}, $$

以及著名的普适比值 $2\Delta(0) \approx 3.5\, k_B T_c$，以及在 $T_c$ 处热容的特征跳变。

**Application.** This is the triumph that ties the whole curriculum together: it explains zero resistance, the gap, the isotope effect, and the thermodynamics — and it uses *every* load-bearing module (second quantization, Fermi surface, phonons, free energy, singlet pairing). If you understand the gap equation, you understand conventional superconductivity.

**应用。** 这是将整个课程贯穿起来的成就：它解释了零电阻、能隙、同位素效应和热力学——并使用了*每一个*关键模块（二次量子化、费米面、声子、自由能、单态配对）。如果你理解了能隙方程，就理解了常规超导性。

**Self-test (blank page)**

1. Write the BCS gap equation in the weak-coupling limit and show that its solution is $\Delta \approx 2\hbar\omega_D\, e^{-1/(g N(0))}$. What is the physical meaning of the Debye frequency $\omega_D$ appearing here?
2. State the universal BCS ratio $2\Delta(0) \approx 3.5\, k_B T_c$. Derive it qualitatively or explain its origin. Is this ratio material-dependent in BCS theory?
3. Write the Bogoliubov quasiparticle energy $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$. What is the minimum energy to create an excitation, and what does the gap $\Delta$ mean for the tunneling conductance?
4. Describe the characteristic jump in electronic heat capacity at $T_c$ predicted by BCS. How does the size of this jump, relative to the normal-state value $\gamma T_c$, test the theory?

**自测（空白页）**

1. 写出弱耦合极限下的 BCS 能隙方程，并说明其解为 $\Delta \approx 2\hbar\omega_D\, e^{-1/(g N(0))}$。方程中出现的德拜频率 $\omega_D$ 的物理意义是什么？
2. 写出普适 BCS 比值 $2\Delta(0) \approx 3.5\, k_B T_c$。定性推导或解释其来源。在 BCS 理论中，这个比值与材料有关吗？
3. 写出博戈留波夫准粒子能量 $E_k = \sqrt{\varepsilon_k^2 + \Delta^2}$。产生一个激发所需的最小能量是多少？能隙 $\Delta$ 对隧穿电导意味着什么？
4. 描述 BCS 理论预言的在 $T_c$ 处电子热容的特征跳变。相对于正常态值 $\gamma T_c$，跳变的大小如何检验该理论？

---

← Previous: [Module 5.4 — The Cooper Problem](./module-5.4-the-cooper-problem.md) · [Phase 5 index](./README.md) · Next: [Module 5.6 — Tunneling & the Gap](./module-5.6-tunneling-and-the-gap.md) →

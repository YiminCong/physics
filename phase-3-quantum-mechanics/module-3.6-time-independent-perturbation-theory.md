# Module 3.6 — Time-Independent Perturbation Theory
**模块 3.6 — 定态微扰理论**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.6-derivations.md)

---

## 1. Corrections to Energies and States · 能量与态的修正

**Definition.** Split $\hat{H} = \hat{H}_0 + \hat{H}'$ where $\hat{H}_0$ is solvable and $\hat{H}'$ is small. First-order energy shift: **$E_n^{(1)} = \langle n|\hat{H}'|n\rangle$**. Second-order: $E_n^{(2)} = \sum_{m\neq n} |\langle m|\hat{H}'|n\rangle|^2 / (E_n^{(0)} - E_m^{(0)})$. **Degenerate** case: diagonalize $\hat{H}'$ within the degenerate subspace first.

**定义。** 将 $\hat{H} = \hat{H}_0 + \hat{H}'$ 分拆，其中 $\hat{H}_0$ 可精确求解，$\hat{H}'$ 为小量。一阶能量修正：**$E_n^{(1)} = \langle n|\hat{H}'|n\rangle$**。二阶修正：$E_n^{(2)} = \sum_{m\neq n} |\langle m|\hat{H}'|n\rangle|^2 / (E_n^{(0)} - E_m^{(0)})$。**简并**情形：先在简并子空间内对角化 $\hat{H}'$。

**Demonstration.** A small linear perturbation on the oscillator, or the **fine structure** of hydrogen (relativistic + spin–orbit corrections), and the **Zeeman effect** (energy splitting in a magnetic field) are all computed this way.

**演示。** 谐振子的小线性微扰，或氢原子的**精细结构**（相对论修正 + 自旋-轨道修正），以及**塞曼效应**（磁场中的能级分裂），都用此方法计算。

**Application.** Almost no real system is exactly solvable; perturbation theory is the universal first approximation, used to estimate level shifts, gaps, and responses throughout the curriculum.

**应用。** 几乎没有实际系统可以精确求解；微扰理论是普适的一阶近似，贯穿整个课程用于估算能级移动、能隙和响应。

---

**Self-test (blank page)**

1. Write the first-order energy correction $E_n^{(1)}$ and the second-order correction $E_n^{(2)}$ for a non-degenerate state $|n\rangle$ due to a perturbation $\hat{H}'$. What sign must $E_n^{(2)}$ have for the ground state?
2. Explain the degenerate case: why does ordinary non-degenerate perturbation theory break down, and what is the correct procedure?
3. Describe one physical example where perturbation theory is applied to hydrogen (e.g. fine structure or the Zeeman effect), naming the perturbation $\hat{H}'$ and the resulting energy splitting.

**自测（空白页）**

1. 写出非简并态 $|n\rangle$ 在微扰 $\hat{H}'$ 下的一阶能量修正 $E_n^{(1)}$ 和二阶能量修正 $E_n^{(2)}$。基态的二阶修正符号如何？
2. 解释简并情形：为何普通非简并微扰理论会失效？正确的处理方法是什么？
3. 描述一个将微扰理论应用于氢原子的物理例子（如精细结构或塞曼效应），指出微扰 $\hat{H}'$ 的形式和所得能级分裂。

---

← Previous: [Module 3.5 — Identical Particles](./module-3.5-identical-particles.md) · [Phase 3 index](./README.md) · Next: [Module 3.7 — Variational & WKB Methods](./module-3.7-variational-and-wkb-methods.md) →

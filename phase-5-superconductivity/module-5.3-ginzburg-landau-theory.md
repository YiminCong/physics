# Module 5.3 — Ginzburg–Landau Theory ⭐⭐
**模块 5.3 — 金兹堡–朗道理论 ⭐⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**

---

## 1. The Order Parameter & Free Energy · 序参量与自由能

**Definition.** Near T_c, describe the superconductor by a **complex order parameter** ψ, with |ψ|² = density of superconducting carriers. Expand the free energy (Module 2.3) in powers of ψ:

**定义。** 在 T_c 附近，用**复数序参量** ψ 描述超导体，其中 |ψ|² 为超导载流子密度。将自由能（模块 2.3）按 ψ 的幂次展开：

  F = F_n + α|ψ|² + (β/2)|ψ|⁴ + (1/2m*)|(−iℏ∇ − e*A)ψ|² + B²/2μ₀.

Minimizing F (the variational idea of Module 1.3) gives the **Ginzburg–Landau equations**.

对 F 求极小值（模块 1.3 的变分思想）给出**金兹堡–朗道方程**。

## 2. Length Scales, Types, and Flux Quantization · 长度尺度、类型与磁通量子化

**Demonstration.** In the uniform case, minimizing over ψ gives |ψ|² = −α/β when α < 0 (i.e. below T_c). Two length scales emerge: the **coherence length** ξ (over which ψ varies) and the **penetration depth** λ. Their ratio is the **GL parameter κ = λ/ξ**:
- κ < 1/√2 → **type I**,
- κ > 1/√2 → **type II**.

Requiring ψ to be single-valued forces magnetic flux to come in quanta **Φ₀ = h/2e** — and that **2e** is a fingerprint of electron *pairs*.

**演示。** 在均匀情形下，对 ψ 求极小值，当 α < 0（即低于 T_c）时给出 |ψ|² = −α/β。由此出现两个长度尺度：**相干长度** ξ（ψ 在其上变化的尺度）和**穿透深度** λ。二者之比为 **GL 参数 κ = λ/ξ**：
- κ < 1/√2 → **I 型**，
- κ > 1/√2 → **II 型**。

要求 ψ 为单值函数，迫使磁通量以量子 **Φ₀ = h/2e** 的形式出现——而这里的 **2e** 正是电子*配对*的指纹。

**Application.** GL is the powerful macroscopic theory: it predicts critical fields, the type-I/II distinction, and the vortex state (5.7), all from free-energy minimization plus the complex phase (Module 0.4). It was later shown to emerge from BCS near T_c.

**应用。** 金兹堡–朗道理论是强大的宏观理论：它从自由能极小化加上复数相位（模块 0.4）出发，预言了临界磁场、I 型/II 型区别以及涡旋态（5.7）。后来证明它可以在 T_c 附近由 BCS 理论导出。

---

← Previous: [Module 5.2 — London Theory](./module-5.2-london-theory.md) · [Phase 5 index](./README.md) · Next: [Module 5.4 — The Cooper Problem](./module-5.4-the-cooper-problem.md) →

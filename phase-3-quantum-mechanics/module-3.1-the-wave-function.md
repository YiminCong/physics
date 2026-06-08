# Module 3.1 — The Wave Function
**模块 3.1 — 波函数**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.1-derivations.md)

---

## 1. State, the Born Rule & the Schrödinger Equation · 态、玻恩定则与薛定谔方程

**Definition.** A particle's state is a complex **wave function** ψ(x,t). The **Born rule**: |ψ(x,t)|² is the probability *density* of finding the particle at x, so ∫|ψ|² dx = 1 (normalization). Evolution obeys the **Schrödinger equation** iℏ ∂ψ/∂t = Ĥψ, with Ĥ = −(ℏ²/2m)∂²/∂x² + V(x). Operators: x̂ = x, p̂ = −iℏ∂/∂x.

**定义。** 粒子的态是一个复数**波函数** ψ(x,t)。**玻恩定则**：|ψ(x,t)|² 是在 x 处找到粒子的概率*密度*，因此 ∫|ψ|² dx = 1（归一化）。演化遵从**薛定谔方程** iℏ ∂ψ/∂t = Ĥψ，其中 Ĥ = −(ℏ²/2m)∂²/∂x² + V(x)。算符：x̂ = x，p̂ = −iℏ∂/∂x。

## 2. Expectation Values & Uncertainty · 期望值与不确定性

**Definition.** ⟨Q⟩ = ∫ ψ* Q̂ ψ dx; spread ΔQ = √(⟨Q²⟩ − ⟨Q⟩²).

**定义。** ⟨Q⟩ = ∫ ψ* Q̂ ψ dx；散布 ΔQ = √(⟨Q²⟩ − ⟨Q⟩²)。

**Demonstration.** For a Gaussian packet, the position/momentum integrals (Module 0.1) give Δx·Δp = ℏ/2 — saturating the **Heisenberg uncertainty principle** Δx·Δp ≥ ℏ/2.

**演示。** 对于高斯波包，位置/动量积分（模块 0.1）给出 Δx·Δp = ℏ/2——达到**海森堡不确定性原理** Δx·Δp ≥ ℏ/2 的下限。

**Application.** The probabilistic layer of all QM; expectation/uncertainty are just the mean/variance of Module 0.5 applied to |ψ|².

**应用。** 所有量子力学的概率层；期望值/不确定性就是模块 0.5 中的均值/方差应用于 |ψ|²。

---

**Self-test (blank page)**

1. State the Born rule: what physical quantity does |ψ(x,t)|² represent, and what normalization condition must ψ satisfy?
2. Write down the time-dependent Schrödinger equation and identify the kinetic-energy and potential-energy terms in the Hamiltonian Ĥ for a particle in one dimension.
3. Define the expectation value ⟨Q⟩ of an observable Q̂ and the associated uncertainty ΔQ in terms of ψ. Then state the Heisenberg uncertainty principle for position and momentum.

**自测（空白页）**

1. 陈述玻恩定则：|ψ(x,t)|² 代表什么物理量？波函数 ψ 必须满足怎样的归一化条件？
2. 写出含时薛定谔方程，并指出一维粒子哈密顿量 Ĥ 中的动能项和势能项。
3. 用 ψ 定义可观测量 Q̂ 的期望值 ⟨Q⟩ 及其不确定度 ΔQ，再陈述位置与动量的海森堡不确定性原理。

---

← Previous: [Module 3.0 — Old Quantum Theory & the Photoelectric Effect](./module-3.0-old-quantum-theory-and-photoelectric-effect.md) · [Phase 3 index](./README.md) · Next: [Module 3.2 — Time-Independent Schrödinger Equation](./module-3.2-time-independent-schrodinger-equation.md) →

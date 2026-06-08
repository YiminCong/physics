# Module 3.2 — Time-Independent Schrödinger Equation ⭐
**模块 3.2 — 定态薛定谔方程 ⭐**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.2-derivations.md)

---

## 1. Stationary States · 定态

**Definition.** Separating variables ψ(x,t) = ψ(x)e^{−iEt/ℏ} turns the Schrödinger equation into the **time-independent Schrödinger equation (TISE)** Ĥψ = Eψ — an eigenvalue problem (Module 0.2). Solutions ψₙ are stationary states; general states are superpositions Σ cₙ ψₙ e^{−iEₙt/ℏ}.

**定义。** 分离变量 ψ(x,t) = ψ(x)e^{−iEt/ℏ} 将薛定谔方程转化为**定态薛定谔方程（TISE）** Ĥψ = Eψ——一个本征值问题（模块 0.2）。解 ψₙ 称为定态；一般态为叠加态 Σ cₙ ψₙ e^{−iEₙt/ℏ}。

## 2. The Canonical Solvable Systems · 典型可解系统

**Demonstration.**
- **Infinite square well** (width L): ψₙ = √(2/L) sin(nπx/L), **Eₙ = n²π²ℏ²/(2mL²)** — energy is quantized by boundary conditions.
- **Harmonic oscillator**, solved with **ladder operators** a = √(mω/2ℏ)(x̂ + ip̂/mω) and a†: the spectrum is **Eₙ = (n + ½)ℏω**, with a† raising and a lowering the state. Note the zero-point energy ½ℏω.
- **Barrier**: a particle can **tunnel** through a region where E < V, with exponentially small transmission.

**演示。**
- **无限深方势阱**（宽度 L）：ψₙ = √(2/L) sin(nπx/L)，**Eₙ = n²π²ℏ²/(2mL²)**——能量由边界条件量子化。
- **谐振子**，用**梯形算符** a = √(mω/2ℏ)(x̂ + ip̂/mω) 和 a† 求解：能谱为 **Eₙ = (n + ½)ℏω**，a† 升态，a 降态。注意零点能 ½ℏω。
- **势垒**：粒子可以**隧穿**过 E < V 的区域，透射率指数级小。

**Application.** The oscillator ladder operators reappear *verbatim* as phonon operators (Phase 4) and in the BCS Hamiltonian (Phase 5). Quantized levels and tunneling are the bread and butter of all that follows.

**应用。** 谐振子梯形算符*原封不动地*作为声子算符重现于第 4 阶段，并出现在 BCS 哈密顿量（第 5 阶段）中。量子化能级和隧穿效应是后续所有内容的基础。

---

**Self-test (blank page)**

1. Explain separation of variables for the Schrödinger equation: what form does ψ(x,t) take, and what eigenvalue equation does the spatial part satisfy?
2. State the energy eigenvalues Eₙ and normalized eigenfunctions ψₙ for the infinite square well of width L.
3. Define the ladder operators a and a† for the harmonic oscillator and state the energy spectrum Eₙ. Why is the zero-point energy ½ℏω physically significant?
4. Describe quantum tunneling qualitatively: how can a particle penetrate a barrier where E < V, and what determines the transmission probability?

**自测（空白页）**

1. 解释薛定谔方程的分离变量法：ψ(x,t) 取什么形式？空间部分满足什么本征值方程？
2. 写出宽度为 L 的无限深方势阱的能量本征值 Eₙ 和归一化本征函数 ψₙ。
3. 定义谐振子的梯形算符 a 和 a†，并写出能谱 Eₙ。为什么零点能 ½ℏω 在物理上有重要意义？
4. 定性描述量子隧穿：粒子如何能穿透 E < V 的势垒区域？什么决定透射概率？

---

← Previous: [Module 3.1 — The Wave Function](./module-3.1-the-wave-function.md) · [Phase 3 index](./README.md) · Next: [Module 3.3 — Formalism](./module-3.3-formalism.md) →

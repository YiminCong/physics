# Module 3.8 — Time-Dependent Perturbation Theory & Scattering
**模块 3.8 — 含时微扰理论与散射**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.8-derivations.md)

---

## 1. Transitions and Fermi's Golden Rule · 跃迁与费米黄金定则

**Definition.** A time-dependent perturbation $\hat{H}'(t)$ drives transitions between states. To first order, the transition rate into a continuum is **Fermi's golden rule**: $\Gamma_{i\to f} = (2\pi/\hbar)|\langle f|\hat{H}'|i\rangle|^2\, \rho(E_f)$, where $\rho$ is the density of final states.

**定义。** 含时微扰 $\hat{H}'(t)$ 驱动态之间的跃迁。一阶近似下，跃迁至连续谱的速率由**费米黄金定则**给出：$\Gamma_{i\to f} = (2\pi/\hbar)|\langle f|\hat{H}'|i\rangle|^2\, \rho(E_f)$，其中 $\rho$ 为末态密度。

**Demonstration.** Applied to an oscillating electric field, the golden rule yields the rates of **absorption and stimulated emission** of radiation (selection rules follow from the matrix element).

**演示。** 应用于振荡电场时，黄金定则给出辐射的**吸收和受激辐射**速率（选择定则由矩阵元决定）。

## 2. Scattering · 散射

**Definition.** Cross sections quantify scattering probability; the **Born approximation** gives the amplitude as a Fourier transform of the potential; **partial-wave analysis** decomposes by angular momentum.

**定义。** 散射截面量化散射概率；**玻恩近似**将散射幅度表示为势的傅里叶变换；**分波分析**按角动量分解。

**Application.** Transition rates govern optical properties and decay; in superconductivity, the golden rule with the BCS density of states gives the **tunneling current** that measures the gap (Phase 5).

**应用。** 跃迁速率决定光学性质和衰变；在超导性中，结合 BCS 态密度的黄金定则给出测量能隙的**隧道电流**（第 5 阶段）。

## Key results · 核心结果

- Fermi's golden rule $\Gamma_{i\to f}=\dfrac{2\pi}{\hbar}|\langle f|\hat H'|i\rangle|^2\rho(E_f)$ · 费米黄金定则
- Electric-dipole selection rules $\Delta\ell=\pm1$, $\Delta m=0,\pm1$ · 偶极选择定则
- Born approximation $f(\theta)\propto$ Fourier transform of $V(r)$ · 玻恩近似
- $\rho(E_f)$ = density of available final states · 末态密度

---

**Self-test (blank page)**

1. State Fermi's golden rule: write the transition rate $\Gamma_{i\to f}$ and identify each factor. What does the density of final states $\rho(E_f)$ represent?
2. Apply the golden rule to a monochromatic oscillating perturbation: what selection rule governs which transitions are allowed by an electric-dipole interaction?
3. State the Born approximation for the scattering amplitude $f(\theta)$: how is it related to the Fourier transform of the scattering potential $V(r)$?

**自测（空白页）**

1. 陈述费米黄金定则：写出跃迁速率 $\Gamma_{i\to f}$ 并说明每个因子的含义。末态密度 $\rho(E_f)$ 代表什么？
2. 将黄金定则应用于单色振荡微扰：电偶极跃迁受到什么选择定则的制约？
3. 写出玻恩近似的散射振幅 $f(\theta)$：它与散射势 $V(r)$ 的傅里叶变换有何关系？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $\Gamma_{i\to f}=\tfrac{2\pi}{\hbar}|\langle f|\hat H'|i\rangle|^2\rho(E_f)$: matrix element (coupling), and $\rho(E_f)$ = number of final states per unit energy available to decay into. · 矩阵元与末态密度。
**2.** A dipole interaction $\hat H'\propto\mathbf E\cdot\mathbf r$ gives the selection rules $\Delta\ell=\pm1$, $\Delta m=0,\pm1$ (photon parity + angular momentum). · 偶极选择定则。
**3.** Born: $f(\theta)=-\tfrac{m}{2\pi\hbar^2}\int e^{-i\mathbf q\cdot\mathbf r}V(r)\,d^3r$ — proportional to the Fourier transform of $V$ at momentum transfer $\mathbf q$. · 散射振幅是势的傅里叶变换。

</details>

---

← Previous: [Module 3.7 — Variational & WKB Methods](./module-3.7-variational-and-wkb-methods.md) · [Phase 3 index](./README.md) · Next: [Module 3.9 — Fundamental Concepts](./module-3.9-fundamental-concepts.md) →

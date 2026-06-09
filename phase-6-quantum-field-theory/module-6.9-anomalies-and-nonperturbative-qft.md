# Module 6.9 — Anomalies & Non-Perturbative QFT
**模块 6.9 — 反常与非微扰量子场论**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-6.9-anomalies-and-nonperturbative-qft-derivations.md)

---

## 1. Anomalies · 反常

**Definition.** An **anomaly** is a symmetry of the classical action that is broken by quantization (the path-integral measure is not invariant, Module 6.4). The prototype is the **chiral (Adler–Bell–Jackiw) anomaly**: the classically conserved axial current acquires a quantum divergence

**定义。** **反常**是指经典作用量的某个对称性被量子化破坏(路径积分测度不变,模块 6.4)。其原型是**手征(Adler–Bell–Jackiw)反常**:经典守恒的轴矢流获得量子散度

$$ \partial_\mu j^{\mu 5} = \frac{e^2}{16\pi^2} \epsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}. $$

**Demonstration.** The anomaly comes from the **triangle diagram** (one axial + two vector vertices), whose regularization cannot preserve both vector and axial currents. It fixes the **$\pi^0 \to \gamma\gamma$** decay rate quantitatively — a striking experimental confirmation. In the Standard Model, **anomaly cancellation** between quarks and leptons constrains the hypercharges and *requires complete generations* (Module 8.5).

**演示。** 反常源自**三角图**(一个轴矢顶点 + 两个矢量顶点),其正规化无法同时保持矢量流与轴矢流守恒。它定量确定了 **$\pi^0 \to \gamma\gamma$** 衰变率——一个引人注目的实验验证。在标准模型中,夸克与轻子之间的**反常相消**约束了超荷,并*要求各代完整*(模块 8.5)。

## 2. Non-Perturbative QFT · 非微扰量子场论

**Definition.** Beyond Feynman-diagram perturbation theory (Module 6.3) lie genuinely **non-perturbative** phenomena. **Instantons** are finite-action solutions of the Euclidean field equations describing quantum tunnelling between degenerate vacua (the $\theta$-vacuum). **Lattice gauge theory** (Wilson) discretizes spacetime, defining QFT non-perturbatively and making it computable by Monte Carlo.

**定义。** 在费曼图微扰论(模块 6.3)之外,存在真正的**非微扰**现象。**瞬子**是欧几里得场方程的有限作用量解,描述简并真空之间的量子隧穿($\theta$ 真空)。**格点规范理论**(威尔逊)将时空离散化,在非微扰层面定义 QFT,并可用蒙特卡罗方法计算。

**Application.** **Lattice QCD** computes hadron masses and the confinement string tension from first principles (complementing Modules 8.3, 8.8). Instantons underlie the **strong CP problem** — why the allowed $\theta$-term $\theta(g^2/32\pi^2)G\cdot\tilde{G}$ is unobservably small — whose leading solution, the **axion**, is a dark-matter candidate (Module 8.6). Confinement itself is an inherently non-perturbative statement.

**应用。** **格点 QCD** 从第一性原理计算强子质量和禁闭弦张力(补充模块 8.3、8.8)。瞬子是**强 CP 问题**的根源——为何允许的 $\theta$ 项 $\theta(g^2/32\pi^2)G\cdot\tilde{G}$ 小到不可观测——其主要解 **轴子** 是暗物质候选者(模块 8.6)。禁闭本身就是一个本质上非微扰的陈述。

---

**Self-test (blank page)**

1. What is an anomaly? Write the chiral-anomaly divergence $\partial_\mu j^{\mu 5}$ and name the diagram responsible.
2. How does anomaly cancellation constrain the Standard Model's particle content?
3. What is an instanton, and what is the $\theta$-vacuum?
4. What does lattice QCD compute that perturbation theory cannot, and how does the strong CP problem lead to the axion?

**自测（空白页）**

1. 什么是反常?写出手征反常散度 $\partial_\mu j^{\mu 5}$ 并指出对应的图。
2. 反常相消如何约束标准模型的粒子内容?
3. 什么是瞬子?什么是 $\theta$ 真空?
4. 格点 QCD 能计算微扰论无法计算的什么?强 CP 问题如何导出轴子?

---

← Previous: [Module 6.8 — Scattering, the S-Matrix & LSZ Reduction](./module-6.8-scattering-s-matrix-and-lsz.md) · [Phase 6 index](./README.md) · Next: [Module 6.10 — Spontaneous Symmetry Breaking & Goldstone's Theorem](./module-6.10-spontaneous-symmetry-breaking-and-goldstone.md) →

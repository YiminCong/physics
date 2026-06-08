# Module 3.15 — Relativistic Quantum Mechanics
**模块 3.15 — 相对论量子力学**

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 3 阶段 — 量子力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-3.15-relativistic-quantum-mechanics-derivations.md)

---

## 1. The Klein–Gordon and Dirac Equations · 克莱因–戈登方程与狄拉克方程

**Definition.** Starting from the relativistic energy–momentum relation E² = (pc)² + (mc²)², replacing E → iℏ ∂/∂t and p → −iℏ∇ yields the **Klein–Gordon (KG) equation**:

  (1/c²) ∂²ψ/∂t² − ∇²ψ + (mc/ℏ)² ψ = 0,   or in covariant notation   (□ + (mc/ℏ)²) ψ = 0,

where □ = ∂_μ ∂^μ = (1/c²)∂²/∂t² − ∇² is the d'Alembertian. The KG equation is Lorentz-covariant and has plane-wave solutions, but it has two severe problems: (1) The **probability density** ρ = (iℏ/2mc²)(ψ* ∂ψ/∂t − ψ ∂ψ*/∂t) derived from it can be **negative** (it is not positive-definite), making a single-particle probabilistic interpretation untenable. (2) It admits **negative-energy solutions** E = −√((pc)² + (mc²)²) with no lower bound.

**定义。** 从相对论能量–动量关系 E² = (pc)² + (mc²)² 出发，令 E → iℏ ∂/∂t，p → −iℏ∇，得到**克莱因–戈登（KG）方程**：

  (1/c²) ∂²ψ/∂t² − ∇²ψ + (mc/ℏ)² ψ = 0，   或协变形式   (□ + (mc/ℏ)²) ψ = 0，

其中 □ = ∂_μ ∂^μ = (1/c²)∂²/∂t² − ∇² 是达朗贝尔算符。KG 方程是洛伦兹协变的，有平面波解，但有两个严重问题：(1) 由它导出的**概率密度** ρ = (iℏ/2mc²)(ψ* ∂ψ/∂t − ψ ∂ψ*/∂t) 可以**为负**（非正定），使单粒子概率诠释不成立。(2) 它允许**负能解** E = −√((pc)² + (mc²)²)，没有下界。

**Definition.** **Dirac (1928)** sought a first-order equation in both space and time, so the probability density would be positive definite. He required that the equation, when applied twice, yields the KG equation for each component. This forces the coefficients to be matrices satisfying the **Clifford algebra**. The resulting **Dirac equation** is:

  (iℏ γ^μ ∂_μ − mc) ψ = 0,

where the **gamma matrices** γ^μ (μ = 0,1,2,3) are 4×4 matrices satisfying {γ^μ, γ^ν} = 2g^{μν} I₄ (with metric signature (+,−,−,−)). The wavefunction ψ is a **4-component Dirac spinor**. The conserved current j^μ = ψ̄ γ^μ ψ (where ψ̄ = ψ† γ^0 is the Dirac adjoint) satisfies ∂_μ j^μ = 0, and the time component j^0 = ψ†ψ is **positive definite** — fixing the probability problem.

**定义。** **狄拉克（1928 年）**寻求在时间和空间上均为一阶的方程，使得概率密度正定。他要求该方程作用两次后对每个分量给出 KG 方程。这迫使系数为满足**Clifford 代数**的矩阵。由此得到的**狄拉克方程**为：

  (iℏ γ^μ ∂_μ − mc) ψ = 0，

其中 **γ 矩阵** γ^μ（μ = 0,1,2,3）是满足 {γ^μ, γ^ν} = 2g^{μν} I₄ 的 4×4 矩阵（度规符号为 (+,−,−,−)）。波函数 ψ 是 **4 分量狄拉克旋量**。守恒流 j^μ = ψ̄ γ^μ ψ（其中 ψ̄ = ψ† γ^0 是狄拉克共轭）满足 ∂_μ j^μ = 0，时间分量 j^0 = ψ†ψ **正定**——从而解决了概率问题。

**Demonstration — Antiparticles.** The Dirac equation still has negative-energy solutions. Dirac's interpretation (the **Dirac sea**): all negative-energy states are filled by electrons in the ground state of the vacuum. A hole in the Dirac sea — a missing negative-energy, negative-charge electron — behaves as a positive-energy, positive-charge particle: the **positron**. Predicted by Dirac in 1930 and discovered by Anderson in 1932, this was the first prediction and discovery of **antimatter**. In modern quantum field theory the Dirac sea picture is replaced by the reinterpretation of negative-frequency solutions as **antiparticle** creation operators (Module 6.5), but the physical content is the same.

**演示——反粒子。** 狄拉克方程仍有负能解。狄拉克的诠释（**狄拉克海**）：真空基态中所有负能态均被电子填满。狄拉克海中的空穴——缺少一个负能、负电荷的电子——表现为一个正能、正电荷的粒子：**正电子**。狄拉克于 1930 年预言，安德森于 1932 年发现，这是**反物质**的首次预言与发现。在现代量子场论中，狄拉克海图像被负频解重新诠释为**反粒子**产生算符（模块 6.5）所取代，但物理内容相同。

---

## 2. Consequences: Spin, g = 2, and Fine Structure · 推论：自旋、g = 2 与精细结构

**Definition.** The spin-½ nature of the electron and its **g-factor g = 2** are not put in by hand in the Dirac theory — they emerge automatically. In an external magnetic field B, the Dirac equation in the non-relativistic limit yields the **Pauli equation**:

  iℏ ∂ψ/∂t = [ p²/2m − eA·p/m + e²A²/2m + V − (eℏ/2m) σ·B ] ψ_2,

where ψ_2 is the two-component (upper, large) spinor and σ are the Pauli matrices. The magnetic moment coupling is −μ·B with **μ = (eℏ/2m) σ**, giving the **g-factor g = 2** exactly: the magnetic moment is twice what one would expect from orbital motion alone.

**定义。** 电子的自旋-½ 性质及其 **g 因子 g = 2** 在狄拉克理论中不是人为引入的——它们自动涌现。在外磁场 B 中，狄拉克方程取非相对论极限得到**泡利方程**：

  iℏ ∂ψ/∂t = [ p²/2m − eA·p/m + e²A²/2m + V − (eℏ/2m) σ·B ] ψ_2，

其中 ψ_2 是两分量（上、大）旋量，σ 是泡利矩阵。磁矩耦合为 −μ·B，**μ = (eℏ/2m) σ**，精确给出 **g 因子 g = 2**：磁矩是仅由轨道运动所预期值的两倍。

**Demonstration — Spin–Orbit Coupling and Fine Structure.** Carrying the non-relativistic expansion to the next order in v²/c² (via the Foldy–Wouthuysen transformation), the Dirac hydrogen atom yields three corrections to the Schrödinger energy: (1) the **relativistic kinetic energy** correction −p⁴/(8m³c²); (2) the **spin–orbit coupling**

  H_SO = (ℏ/2m²c²)(1/r)(dV/dr) S·L,

where V(r) = −e²/(4πε₀r) for hydrogen; (3) the **Darwin term** (ℏ²/8m²c²) ∇²V (non-zero only for l = 0). Together these give the **hydrogen fine structure** (Module 3.6) with the exact relativistic energy formula:

  E_{nj} = m_e c² [ 1 + (α/(n − (j+½) + √((j+½)² − α²)))² ]^{−½} − m_e c²,

where α = e²/(4πε₀ℏc) ≈ 1/137 is the fine-structure constant and j is the total angular momentum quantum number. Expanding in powers of α reproduces the Bohr levels plus the fine-structure shifts −(m_e c² α⁴)/(2n³) (1/(j+½) − 3/(4n)).

**演示——自旋–轨道耦合与精细结构。** 将非相对论展开推进到 v²/c² 的下一阶（通过 Foldy–Wouthuysen 变换），狄拉克氢原子给出对薛定谔能量的三个修正：(1) **相对论动能**修正 −p⁴/(8m³c²)；(2) **自旋–轨道耦合**

  H_SO = (ℏ/2m²c²)(1/r)(dV/dr) S·L，

其中对氢原子 V(r) = −e²/(4πε₀r)；(3) **达尔文项** (ℏ²/8m²c²) ∇²V（仅对 l = 0 非零）。这些共同给出**氢原子精细结构**（模块 3.6），精确相对论能量公式为：

  E_{nj} = m_e c² [ 1 + (α/(n − (j+½) + √((j+½)² − α²)))² ]^{−½} − m_e c²，

其中 α = e²/(4πε₀ℏc) ≈ 1/137 是精细结构常数，j 是总角动量量子数。对 α 展开，还原玻尔能级加上精细结构修正 −(m_e c² α⁴)/(2n³) (1/(j+½) − 3/(4n))。

**Application.** The Dirac equation is the single-particle foundation underlying **quantum electrodynamics (QED)** and the entire Standard Model. Its field-theoretic generalisation (Module 6.5) replaces the wavefunction with a quantum field, automatically incorporating particle creation, annihilation, and the full machinery of renormalisation. The spin–orbit coupling derived here is the relativistic origin of the fine structure observed in atomic spectra, the **Lamb shift** (a QED correction beyond Dirac), and the spin–orbit interaction responsible for **band inversions** in topological insulators (Phase 4). The g = 2 result is corrected to g = 2 + α/π + … by QED loop diagrams — the most precisely tested prediction in physics.

**应用。** 狄拉克方程是**量子电动力学（QED）**及整个标准模型的单粒子基础。其场论推广（模块 6.5）用量子场替换波函数，自动纳入粒子的产生、湮灭及完整的重整化机制。此处推导的自旋–轨道耦合是原子光谱中观测到的精细结构的相对论起源，**兰姆位移**（超越狄拉克的 QED 修正），以及拓扑绝缘体（第 4 阶段）中**能带反转**背后的自旋–轨道相互作用。g = 2 的结果经 QED 圈图修正为 g = 2 + α/π + …——这是物理学中检验最精确的预言。

---

**Self-test (blank page)**

1. Write the Klein–Gordon equation and state its two physical problems.
2. Write the Dirac equation in covariant notation; identify ψ̄ and the form of the current j^μ.
3. State the Clifford algebra condition on the gamma matrices and explain why it is needed.
4. Explain the Dirac sea interpretation of antiparticles.
5. Show how g = 2 emerges from the non-relativistic limit of the Dirac equation.
6. Write the spin–orbit coupling term from the Dirac expansion and state the quantum numbers in E_{nj}.
7. What does the Dirac equation predict about the Lamb shift, and what corrects it?

**自测（空白页）**

1. 写出克莱因–戈登方程，并陈述其两个物理问题。
2. 用协变符号写出狄拉克方程；指明 ψ̄ 及流 j^μ 的形式。
3. 陈述 γ 矩阵的 Clifford 代数条件，并解释为何需要它。
4. 解释反粒子的狄拉克海诠释。
5. 说明 g = 2 如何从狄拉克方程的非相对论极限中涌现。
6. 写出狄拉克展开中的自旋–轨道耦合项，并陈述 E_{nj} 中的量子数。
7. 狄拉克方程对兰姆位移有何预言，什么修正了它？

---

← Previous: [Module 3.14 — Density Matrix & Open Quantum Systems](./module-3.14-density-matrix-and-open-quantum-systems.md) · [Phase 3 index](./README.md) · Next: [Module 3.16 — Quantum Computation & Information](./module-3.16-quantum-computation-and-information.md) →

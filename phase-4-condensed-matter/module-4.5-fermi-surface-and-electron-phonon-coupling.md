# Module 4.5 — Fermi Surface & Electron–Phonon Coupling ⭐
**模块 4.5 — 费米面与电子–声子耦合 ⭐**

> **Phase 4 — [Condensed Matter / Solid State](./README.md)** · Format: Definition → Demonstration → Application
> **第 4 阶段 — 凝聚态 / 固体物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-4.5-derivations.md)

---

## 1. The Fermi Surface · 费米面

**Definition.** At $T = 0$, electrons fill all states up to $E_F$; the **Fermi surface** is the constant-energy surface in $\mathbf{k}$-space dividing filled from empty states. The **density of states at the Fermi level**, $g(E_F)$, controls electronic heat capacity, magnetic response, and transport.

**定义。** 在 $T = 0$ 时，电子填满所有直至 $E_F$ 的态；**费米面**是 $\mathbf{k}$ 空间中分隔已填充态与空态的等能面。**费米能级处的态密度** $g(E_F)$ 控制着电子热容、磁响应和输运性质。

**Demonstration.** For free electrons the Fermi surface is a sphere of radius $k_F$ set by the electron density. In real crystals the bands (4.4) distort it into more complex shapes. Only electrons within $\sim kT$ of this surface participate in low-energy physics.

**演示。** 对于自由电子，费米面是由电子密度决定的半径为 $k_F$ 的球面。在真实晶体中，能带（4.4）将其扭曲成更复杂的形状。只有费米面附近约 $\sim kT$ 范围内的电子参与低能物理过程。

## 2. The Electron–Phonon Interaction · 电子–声子相互作用

**Definition.** A moving electron distorts the positively charged lattice; that distortion (a cloud of phonons) attracts a second electron. Net effect: an **effective attraction between electrons** near the Fermi surface, mediated by phonons.

**定义。** 运动中的电子使带正电的晶格发生形变；该形变（一团声子云）吸引第二个电子。净效果：费米面附近电子之间产生**由声子媒介的有效吸引力**。

**Application.** This is the immediate trigger for superconductivity. Because **only electrons near the Fermi surface can pair**, and the **phonon-mediated attraction** can overcome the screened Coulomb repulsion, two electrons form a **Cooper pair** (Phase 5, Module 5.4). The density of states $g(E_F)$ enters the **BCS gap equation** directly — a larger $g(E_F)$ and stronger coupling give a higher $T_c$.

**应用。** 这是超导的直接触发机制。因为**只有费米面附近的电子才能配对**，且**声子媒介的吸引力**能够克服屏蔽库仑排斥，两个电子形成**库珀对**（第 5 阶段，模块 5.4）。态密度 $g(E_F)$ 直接进入 **BCS 能隙方程**——更大的 $g(E_F)$ 和更强的耦合给出更高的 $T_c$。

## Key results · 核心结果

- The Fermi surface (constant-energy surface at $E_F$) controls transport and thermodynamics · 费米面主宰输运与热力学
- Low-energy excitations and heat capacity scale with $g(E_F)$ · 低能激发与热容正比于 $g(E_F)$
- Electron–phonon coupling gives an effective electron–electron attraction · 电子–声子耦合给出有效吸引
- That attraction is the microscopic seed of Cooper pairing (5.4, 5.5) · 这正是库珀配对的微观起点

---

**Self-test (blank page)**

1. Define the Fermi surface. For free electrons in 3D with electron density $n$, derive the Fermi wavevector $k_F$ and the Fermi energy $E_F$ in terms of $n$.
2. Why do only electrons within $\sim kT$ of the Fermi surface participate in low-energy phenomena? How does this explain the smallness of the electronic heat capacity?
3. Describe qualitatively the phonon-mediated attraction between two electrons near the Fermi surface. Why is the net interaction attractive even though electrons repel each other via Coulomb forces?
4. How does the density of states $g(E_F)$ enter the BCS gap equation, and what does a larger $g(E_F)$ imply for $T_c$?

**自测（空白页）**

1. 定义费米面。对于三维自由电子（电子密度为 $n$），推导费米波矢 $k_F$ 和费米能 $E_F$ 关于 $n$ 的表达式。
2. 为何只有费米面附近约 $\sim kT$ 范围内的电子参与低能现象？这如何解释电子热容的数值较小？
3. 定性描述费米面附近两个电子之间由声子介导的吸引力。尽管电子之间存在库仑排斥，为何净相互作用可以是吸引的？
4. 态密度 $g(E_F)$ 如何进入 BCS 能隙方程？更大的 $g(E_F)$ 对 $T_c$ 意味着什么？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** The Fermi surface is the constant-energy surface at $E_F$. Filling states to $E_F$: $k_F=(3\pi^2 n)^{1/3}$, $E_F=\hbar^2 k_F^2/2m=\dfrac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$. · 费米面;$k_F=(3\pi^2n)^{1/3}$,$E_F=\tfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$。

**2.** States below $E_F$ are Pauli-blocked; only those within $\sim k_BT$ of $E_F$ have empty neighbours to scatter into. The fraction $\sim k_BT/E_F$ explains the small heat capacity $C\propto T$. · 仅费米面附近 $\sim k_BT$ 的电子参与,故 $C\propto T$。

**3.** One electron distorts the lattice, leaving a transient region of excess positive (ionic) charge; a second electron is attracted to it. This retarded, phonon-mediated attraction can beat the screened Coulomb repulsion for electrons near $E_F$ with opposite momenta. · 电子畸变晶格留下正电区吸引另一电子(声子介导,推迟)。

**4.** The gap is $\Delta\approx2\hbar\omega_D e^{-1/gN(0)}$: a larger $g(E_F)$ enlarges the exponent, raising $\Delta$ and $T_c$ exponentially. · $g(E_F)$ 越大,$\Delta$、$T_c$ 指数升高。

</details>

---

← Previous: [Module 4.4 — Electrons in a Periodic Potential](./module-4.4-electrons-in-a-periodic-potential.md) · [Phase 4 index](./README.md) · Next: [Module 4.6 — Magnetism & Spin Waves](./module-4.6-magnetism-and-spin-waves.md) →

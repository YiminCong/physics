# Module 10.3 — The AdS/CFT Correspondence & Black-Hole Information
**模块 10.3 — AdS/CFT 对应与黑洞信息**

> **Phase 10 — [Strings & Quantum Gravity](./README.md)** · Format: Definition → Demonstration → Application
> **第 10 阶段 — 弦论与量子引力** · 格式：定义 → 演示 → 应用
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-10.3-derivations.md)

---

## 1. The Holographic Dictionary · 全息字典

**Definition.** The **AdS/CFT correspondence** (Maldacena, 1997) is an exact duality: **quantum gravity** (string theory) in a $(d+1)$-dimensional **anti-de Sitter** spacetime $\mathrm{AdS}_{d+1}$ is *the same theory* as a **conformal field theory** (Module 6.13) living on its $d$-dimensional boundary. The original example states that type IIB string theory on $\mathrm{AdS}_5 \times S^5$ is dual to $\mathcal{N}=4$ supersymmetric $SU(N)$ Yang–Mills theory in four dimensions. It is a concrete realization of the **holographic principle** (Module 10.2): a gravitational theory in a volume is fully encoded by a non-gravitational theory on its boundary, with one fewer dimension.

**定义。** **AdS/CFT 对应**（Maldacena，1997）是一个精确对偶：$(d+1)$ 维**反德西特**时空 $\mathrm{AdS}_{d+1}$ 中的**量子引力**（弦论）与生活在其 $d$ 维边界上的**共形场论**（模块 6.13）是*同一个理论*。最初的例子指出，$\mathrm{AdS}_5 \times S^5$ 上的 IIB 型弦论对偶于四维的 $\mathcal{N}=4$ 超对称 $SU(N)$ 杨–米尔斯理论。它是**全息原理**（模块 10.2）的具体实现：一个体积内的引力理论由其边界上维数少一的非引力理论完全编码。

**Demonstration.** The duality is made quantitative by the **GKP–Witten relation**, which equates the two partition functions,
$$ Z_\text{gravity}\big[\phi(x,z)\big|_{z\to 0} = \phi_0(x)\big] = \Big\langle \exp\!\int_{\partial} d^dx\; \phi_0(x)\,\mathcal{O}(x) \Big\rangle_\text{CFT}. $$
Every bulk field $\phi$ is dual to a boundary operator $\mathcal{O}$; the field's boundary value $\phi_0$ is the source coupling to $\mathcal{O}$. A field of mass $m$ in $\mathrm{AdS}_{d+1}$ maps to an operator of dimension $\Delta(\Delta - d) = m^2 L^2$ ($L$ = AdS radius). Crucially the duality is a **strong–weak** correspondence: when the CFT coupling is *strong* (and ordinary Feynman diagrams fail), the dual geometry is *weakly curved* and classical Einstein gravity applies. This turns intractable strongly-coupled field-theory problems into solvable gravity problems.

**演示。** 该对偶由 **GKP–Witten 关系**定量化，它令两个配分函数相等（如上式）：每个体场 $\phi$ 对偶于一个边界算符 $\mathcal{O}$，场的边界值 $\phi_0$ 是耦合到 $\mathcal{O}$ 的源。$\mathrm{AdS}_{d+1}$ 中质量为 $m$ 的场映射到维数满足 $\Delta(\Delta - d) = m^2 L^2$ 的算符。关键在于该对偶是**强–弱**对应：当 CFT 耦合*强*（普通费曼图失效）时，对偶几何*弱弯曲*，经典爱因斯坦引力适用。这把棘手的强耦合场论问题转化为可解的引力问题。

**Application.** Holography has become a calculational tool far beyond string theory. The **Ryu–Takayanagi formula** computes the entanglement entropy of a boundary region $A$ as the area of a minimal bulk surface $\gamma_A$ anchored on its edge,
$$ S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}, $$
geometrizing quantum entanglement (Module 3.13) as a literal surface in a curved spacetime — entanglement *builds* the geometry. Holographic methods give the shear-viscosity-to-entropy ratio $\eta/s = \hbar/4\pi k_B$ of the quark–gluon plasma seen at RHIC and the LHC, and are applied to strange-metal transport in condensed matter (Phase 4). A field theory with no gravity at all is solved by doing geometry in one higher dimension.

**应用。** 全息已成为远超弦论的计算工具。**Ryu–Takayanagi 公式**将边界区域 $A$ 的纠缠熵计算为锚定在其边缘上的体中极小曲面 $\gamma_A$ 的面积（如上式），把量子纠缠（模块 3.13）几何化为弯曲时空中的一张实在曲面——纠缠*构建*了几何。全息方法给出在 RHIC 和 LHC 观测到的夸克–胶子等离子体的剪切黏度–熵比 $\eta/s = \hbar/4\pi k_B$，并被应用于凝聚态中的奇异金属输运（第 4 阶段）。一个完全没有引力的场论，靠在高一维做几何就被求解了。

---

## 2. The Black-Hole Information Paradox · 黑洞信息悖论

**Definition.** Hawking showed (Module 10.2) that a black hole radiates a **thermal** spectrum at temperature $T_H = \hbar c^3/8\pi G M k_B$. Taken at face value, a black hole formed from a *pure* quantum state would evaporate into *thermal* (maximally mixed) radiation — a non-unitary $\text{pure} \to \text{mixed}$ evolution that destroys information and contradicts quantum mechanics. This is the **information paradox**. Its sharpest form is the **Page curve**: if evaporation is unitary, the entanglement entropy of the emitted radiation must rise, then *turn over* and fall back to zero at the **Page time**, rather than rising forever as Hawking's calculation implies.

**定义。** 霍金证明（模块 10.2）黑洞以温度 $T_H = \hbar c^3/8\pi G M k_B$ 辐射**热**谱。照字面理解，由*纯*量子态形成的黑洞会蒸发为*热的*（最大混合）辐射——一个破坏信息、违背量子力学的非幺正 $\text{纯态} \to \text{混合态}$ 演化。这就是**信息悖论**。其最尖锐的形式是 **Page 曲线**：若蒸发是幺正的，发出辐射的纠缠熵必须先上升，然后在 **Page 时间**处*反转*并回落到零，而非如霍金计算所暗示的那样永远上升。

**Demonstration.** AdS/CFT resolves the paradox in principle: a black hole in AdS is dual to a **thermal state** of the boundary CFT, and CFT time evolution is **manifestly unitary**. Information cannot be lost, because the dual description never involves a horizon. Concretely, the **Bekenstein–Hawking entropy** $S = k_B A/4\ell_P^2$ is reproduced by *counting microstates*: for certain supersymmetric black holes, Strominger and Vafa (1996) counted the D-brane bound states with the same charges and found exactly $\log(\text{states}) = A/4G_N$ — the entropy is ordinary statistical entropy of a vast but finite set of quantum states. Recent work recovers the full Page curve from gravity itself, by including new saddle points — **replica wormholes** — and the **quantum extremal surface** prescription that generalizes Ryu–Takayanagi.

**演示。** AdS/CFT 原则上解决了悖论：AdS 中的黑洞对偶于边界 CFT 的**热态**，而 CFT 的时间演化**显然幺正**。信息不会丢失，因为对偶描述从不涉及视界。具体地，**Bekenstein–Hawking 熵** $S = k_B A/4\ell_P^2$ 通过*计数微观态*重现：对某些超对称黑洞，Strominger 与 Vafa（1996）计数了具有相同荷的 D 膜束缚态，恰好得到 $\log(\text{态数}) = A/4G_N$——熵就是一个巨大但有限的量子态集合的普通统计熵。近期工作通过纳入新的鞍点——**复制虫洞**——以及推广 Ryu–Takayanagi 的**量子极值曲面**方案，从引力本身重现了完整的 Page 曲线。

**Application.** The information paradox and its holographic resolution have reframed quantum gravity around **quantum information**. The lesson "**entanglement builds spacetime**" — that the connectivity of a smooth geometry reflects entanglement in the dual state (ER = EPR: an Einstein–Rosen bridge is an entangled pair) — is now a guiding principle in the search for a full theory of quantum gravity. It closes the arc of this curriculum: the same entanglement entropy $S = -\text{Tr}\,\rho\ln\rho$ introduced for a two-qubit system (Module 3.14) reappears, via the Ryu–Takayanagi formula, as the area of a surface inside a black hole — quantum information and gravitation turn out to be two views of one structure.

**应用。** 信息悖论及其全息解决方案将量子引力重新围绕**量子信息**来组织。「**纠缠构建时空**」这一教益——光滑几何的连通性反映对偶态中的纠缠（ER = EPR：爱因斯坦–罗森桥即一对纠缠粒子）——如今是寻找完整量子引力理论的指导原则。它闭合了本课程的弧线：为两量子比特系统引入的同一个纠缠熵 $S = -\text{Tr}\,\rho\ln\rho$（模块 3.14），经由 Ryu–Takayanagi 公式，重新出现为黑洞内部一张曲面的面积——量子信息与引力原来是同一结构的两种视角。

---

## Key results · 核心结果

- AdS/CFT: gravity in $\mathrm{AdS}_{d+1}$ $=$ a CFT on the $d$-dimensional boundary (holography made exact) · 全息精确化
- GKP–Witten $Z_\text{grav}[\phi_0] = \langle e^{\int\phi_0\mathcal{O}}\rangle_\text{CFT}$; bulk mass ↔ operator dimension $\Delta(\Delta-d)=m^2L^2$ · 全息字典
- Strong–weak duality: strongly-coupled CFT ↔ weakly-curved classical gravity · 强–弱对偶
- Ryu–Takayanagi $S_A = \text{Area}(\gamma_A)/4G_N$ — entanglement as geometry · 纠缠熵即极小曲面面积
- Information paradox resolved: black hole $=$ unitary thermal CFT state; $S_{BH} = A/4$ counts microstates; Page curve · 信息悖论与微观态计数

---

**Self-test (blank page)**

1. State the AdS/CFT correspondence precisely, including the dimensions of the two sides and the original $\mathrm{AdS}_5 \times S^5$ example. In what sense is it a realization of the holographic principle?
2. Write the GKP–Witten relation and explain the role of the bulk field's boundary value $\phi_0$. What is the field–operator map between a bulk mass $m$ and a boundary scaling dimension $\Delta$?
3. Explain why AdS/CFT is a "strong–weak" duality and why that makes it a powerful computational tool. Give one physical application (e.g. $\eta/s$).
4. State the Ryu–Takayanagi formula and explain what it means to say "entanglement builds spacetime."
5. State the black-hole information paradox and the form of the Page curve. Explain how the unitarity of the boundary CFT, and the microstate counting $S = A/4G_N$, resolve it in principle.

**自测（空白页）**

1. 精确陈述 AdS/CFT 对应，包括两侧的维数以及最初的 $\mathrm{AdS}_5 \times S^5$ 例子。它在何种意义上实现了全息原理？
2. 写出 GKP–Witten 关系，并解释体场边界值 $\phi_0$ 的作用。体质量 $m$ 与边界标度维数 $\Delta$ 之间的场–算符映射是什么？
3. 解释为何 AdS/CFT 是「强–弱」对偶，以及为何这使它成为强大的计算工具。给出一个物理应用（如 $\eta/s$）。
4. 陈述 Ryu–Takayanagi 公式，并解释「纠缠构建时空」的含义。
5. 陈述黑洞信息悖论与 Page 曲线的形状。解释边界 CFT 的幺正性以及微观态计数 $S = A/4G_N$ 如何在原则上解决它。

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Gravity (string theory) in $(d{+}1)$-dimensional anti-de Sitter space equals a CFT on its $d$-dimensional boundary. Original example: type IIB strings on $\mathrm{AdS}_5\times S^5$ ↔ $\mathcal N=4$ $SU(N)$ super-Yang–Mills in 4D. It realizes holography — a $(d{+}1)$-dim gravitational theory fully encoded by a $d$-dim non-gravitational one. · AdS/CFT;$\mathrm{AdS}_5\times S^5\leftrightarrow\mathcal N=4$ SYM,全息原理的实现。

**2.** $Z_\text{grav}[\phi_0]=\langle\exp\!\int\phi_0\mathcal O\rangle_\text{CFT}$: the bulk field's boundary value $\phi_0$ is the **source** for the dual operator $\mathcal O$. Field–operator map: $\Delta(\Delta-d)=m^2L^2$ (bulk mass $m$ ↔ boundary dimension $\Delta$). · GKP–Witten;$\phi_0$ 为源,$\Delta(\Delta-d)=m^2L^2$。

**3.** It is strong–weak: when the CFT coupling is strong, the dual geometry is weakly curved and classical gravity applies — so hard strongly-coupled field-theory problems become tractable gravity problems. Application: the viscosity-to-entropy ratio $\eta/s=\hbar/4\pi k_B$ of the quark–gluon plasma. · 强–弱对偶;应用如 $\eta/s=\hbar/4\pi k_B$。

**4.** $S_A=\text{Area}(\gamma_A)/4G_N$, with $\gamma_A$ the minimal bulk surface anchored on $\partial A$. "Entanglement builds spacetime": the bulk's geometry and connectivity reflect entanglement in the boundary state — remove the entanglement and the geometry pinches apart. · RT 公式;纠缠构建时空几何。

**5.** Paradox: Hawking radiation looks thermal, suggesting pure→mixed (non-unitary) evolution and information loss. The Page curve says the radiation entropy should rise then fall back to zero. Resolution: the boundary CFT evolves unitarily (no horizon there), so information is preserved, and $S=A/4G_N$ counts a finite set of microstates (Strominger–Vafa) — a black hole is an ordinary quantum system. · 信息悖论与 Page 曲线;边界 CFT 幺正 + 微观态计数解决之。

</details>

---

← Previous: [Module 10.2 — Quantum Gravity & Holography](./module-10.2-quantum-gravity-and-holography.md) · Related: [Module 6.13 — Conformal Field Theory](../phase-6-quantum-field-theory/module-6.13-conformal-field-theory.md) · [Phase 10 index](./README.md)

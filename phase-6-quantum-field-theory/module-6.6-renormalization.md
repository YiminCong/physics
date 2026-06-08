# Module 6.6 — Renormalization & the Renormalization Group ⭐⭐
**模块 6.6 — 重整化与重整化群 ⭐⭐**

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 6 阶段 — 量子场论与多体物理 · 格式：定义 → 演示 → 应用**

---

## 1. Ultraviolet Divergences, Regularization, and Renormalization · 紫外发散、正规化与重整化

**Definition.** Loop diagrams in QFT involve integrals over all internal momenta k, including arbitrarily large k (short distances). These integrals typically diverge: the electron self-energy in QED, ∫ d⁴k G⁰(k+p) G^{photon}(k), diverges logarithmically in the ultraviolet (UV). This is not a failure of the theory but a symptom of naively using a theory at energy scales beyond its domain of validity. Regularization introduces a parameter that makes the integrals finite: dimensional regularization replaces d⁴k → d^d k with d = 4 − ε (ε → 0 at the end), making divergences appear as poles in 1/ε; a hard momentum cutoff Λ makes them appear as powers of Λ.

**定义。** QFT 中的圈图涉及对所有内部动量 k 的积分，包括任意大的 k（短距离）。这些积分通常发散：QED 中的电子自能 ∫ d⁴k G⁰(k+p) G^{photon}(k) 在紫外（UV）对数发散。这不是理论的失败，而是在超出其有效范围的能量尺度上朴素使用理论的症状。正规化引入一个使积分有限的参数：维度正规化将 d⁴k → d^d k，其中 d = 4 − ε（最后令 ε → 0），使发散以 1/ε 的极点形式出现；硬动量截断 Λ 使其以 Λ 的幂次出现。

Renormalization absorbs divergences into redefinitions of the physical parameters (mass, charge, field normalization). Write the bare Lagrangian parameters (m₀, e₀, φ₀) in terms of renormalized parameters (m, e, φ) plus counterterms δm, δe, δZ chosen order by order in perturbation theory to cancel the 1/ε poles (or Λ-dependences). A theory is renormalizable if only finitely many distinct counterterms are needed — equivalently, if all divergences can be absorbed into the parameters already present in L. QED and the Standard Model are renormalizable; gravity (as a quantum field theory) is not.

重整化将发散吸收进物理参数（质量、电荷、场归一化）的重定义中。将裸拉格朗日量参数（m₀、e₀、φ₀）用重整化参数（m、e、φ）加上抵消项 δm、δe、δZ 来表示，这些抵消项逐阶在微扰论中选取以消去 1/ε 极点（或 Λ 依赖性）。若只需有限个不同的抵消项，则理论是可重整的——等价地，若所有发散都能被 L 中已有参数吸收。QED 和标准模型是可重整的；引力（作为量子场论）则不是。

**Demonstration.** In QED at one loop, the photon propagator acquires a self-energy correction Π(q²) that is logarithmically divergent. After regularization and renormalization, the physical (renormalized) charge e(μ) depends on the renormalization scale μ: e²(μ) = e²(μ₀)/(1 − (e²(μ₀)/6π²) ln(μ/μ₀) + …). This is the running coupling. As μ increases (shorter distances, higher energies), e(μ) increases — QED is asymptotically free in the IR, with the coupling growing toward a Landau pole at exponentially large energies (well beyond any physical scale). In QCD the sign flips (non-Abelian gauge field), giving asymptotic freedom: e_s(μ) decreases at high μ, justifying perturbation theory at collider energies.

**演示。** 在 QED 一圈阶，光子传播子获得对数发散的自能修正 Π(q²)。正规化和重整化后，物理（重整化）电荷 e(μ) 依赖于重整化尺度 μ：e²(μ) = e²(μ₀)/(1 − (e²(μ₀)/6π²) ln(μ/μ₀) + …)。这是跑动耦合常数。随着 μ 增大（更短距离、更高能量），e(μ) 增大——QED 在红外是渐近自由的，耦合趋向于指数大能量处的朗道极点（远超任何物理尺度）。在 QCD 中符号翻转（非阿贝尔规范场），给出渐近自由：e_s(μ) 在高 μ 时减小，为对撞机能量下的微扰论提供依据。

**Application.** After renormalization, QED yields finite, unambiguous predictions at every order in e². The electron anomalous magnetic moment a_e = (g−2)/2 = α/2π − 0.328 α²/π² + … computed to four loops matches experiment at the level of one part in 10¹², making it the most precisely tested prediction in all of science. The procedure is systematic and algorithmic; Peskin & Schroeder "Introduction to Quantum Field Theory" works through it in full detail.

**应用。** 重整化后，QED 在 e² 的每一阶给出有限、明确的预言。电子反常磁矩 a_e = (g−2)/2 = α/2π − 0.328 α²/π² + … 计算到四圈，与实验在 10¹² 分之一的水平上吻合，使其成为科学史上经受检验最精确的预言。该程序是系统的、算法性的；Peskin & Schroeder 的 "Introduction to Quantum Field Theory" 详细完整地阐述了这一过程。

---

## 2. The Renormalization Group and Universality · 重整化群与普适性

**Definition.** The renormalization group (RG) is not a group in the strict sense but a semigroup of scale transformations: physical observables must be independent of the arbitrary renormalization scale μ, so μ d/dμ G^{(n)} = 0 gives the Callan–Symanzik equation. The beta function β(g) = μ dg/dμ encodes how a coupling g flows with scale. Fixed points β(g*) = 0 are the universal, scale-invariant theories: free field theory (g* = 0, UV fixed point of asymptotically free theories) and interacting Wilson–Fisher fixed points (in d = 4 − ε dimensions, g* = O(ε)).

**定义。** 重整化群（RG）严格意义上并非群，而是尺度变换的半群：物理可观测量必须独立于任意重整化尺度 μ，因此 μ d/dμ G^{(n)} = 0 给出卡兰–西曼兹克方程。β 函数 β(g) = μ dg/dμ 编码耦合常数 g 随尺度的流动方式。不动点 β(g*) = 0 是普适的、尺度不变的理论：自由场论（g* = 0，渐近自由理论的紫外不动点）和相互作用的 Wilson–Fisher 不动点（在 d = 4 − ε 维中，g* = O(ε)）。

Near a fixed point, perturbations grow as (μ/μ₀)^{Δ} where Δ is a critical exponent. Relevant perturbations (Δ > 0) dominate at long distances (IR); irrelevant perturbations (Δ < 0) are suppressed. Only finitely many relevant and marginal operators matter for long-distance physics — this is the deep reason why diverse microscopic models sharing the same relevant operators flow to the same fixed point and therefore exhibit the same critical exponents. This is universality.

在不动点附近，扰动按 (μ/μ₀)^{Δ} 增长，其中 Δ 是临界指数。相关扰动（Δ > 0）在长距离（红外）占主导；无关扰动（Δ < 0）被压制。只有有限个相关和边缘算符对长距离物理有影响——这正是各种具有相同相关算符的微观模型流向同一不动点、因而表现出相同临界指数的深层原因。这就是普适性。

**Demonstration.** The Landau–Ginzburg free energy F = ∫ d^d x [½(∇φ)² + ½r φ² + u φ⁴] (Module 2.3) is a QFT in Euclidean space. Running u and r with the RG scale gives the Wilson–Fisher fixed point at u* = ε/6 + O(ε²) in d = 4 − ε. Expanding around the fixed point, the correlation length exponent is ν = ½ + ε/12 + O(ε²) and η = ε²/54 + O(ε³). These are universal — they apply to the liquid-gas critical point, the Ising ferromagnet, the superfluid transition in ⁴He, and any other system in the same universality class (same symmetry, dimension, and number of order-parameter components). The same RG framework applied to the Ginzburg–Landau theory of superconductivity (Module 5.3) gives the exponents for the superconducting phase transition; fluctuation corrections move it away from mean-field values.

**演示。** 朗道–金兹堡自由能 F = ∫ d^d x [½(∇φ)² + ½r φ² + u φ⁴]（模块 2.3）是欧几里得空间中的一个 QFT。随重整化群尺度跑动 u 和 r，在 d = 4 − ε 维中给出 Wilson–Fisher 不动点 u* = ε/6 + O(ε²)。在不动点附近展开，关联长度指数为 ν = ½ + ε/12 + O(ε²)，η = ε²/54 + O(ε³)。这些是普适的——适用于液-气临界点、伊辛铁磁体、⁴He 中的超流相变以及同一普适类中的任何其他系统（相同的对称性、维度和序参量分量数）。同样的重整化群框架应用于超导的金兹堡–朗道理论（模块 5.3），给出超导相变的临界指数；涨落修正使其偏离平均场值。

**Application.** The RG unifies four apparently unrelated ideas: (i) the removal of UV divergences in QFT, (ii) the emergence of universal critical exponents in statistical mechanics, (iii) the concept of effective field theory (at energy E, integrate out degrees of freedom at scales ≫ E; the result is a renormalized EFT valid below E), and (iv) the running of coupling constants measured at colliders. It explains why QED predictions are finite and precise, why an Ising magnet and a liquid near its critical point have identical exponents, and why the large-scale universe can be described without knowing the details of Planck-scale physics. Altland & Simons Ch. 8 and Coleman "Introduction to Many-Body Physics" Ch. 15–16 give complementary condensed-matter treatments; Peskin & Schroeder Part II gives the QFT treatment.

**应用。** 重整化群统一了四个表面上无关的思想：（i）QFT 中紫外发散的消除，（ii）统计力学中普适临界指数的涌现，（iii）有效场论的概念（在能量 E 处，积掉尺度 ≫ E 的自由度；结果是在 E 以下有效的重整化有效场论），以及（iv）对撞机测量的耦合常数的跑动。它解释了为什么 QED 预言是有限且精确的，为什么伊辛磁体和临界点附近的液体具有相同的临界指数，以及为什么宏观宇宙可以在不了解普朗克尺度物理细节的情况下加以描述。Altland & Simons 第 8 章和 Coleman 的 "Introduction to Many-Body Physics" 第 15–16 章给出互补的凝聚态处理；Peskin & Schroeder 第 II 部分给出 QFT 处理。

---

## Self-test (blank page) · 自测（空白页）

1. What is the difference between regularization and renormalization? Give one example of each.
2. Define the beta function β(g). What does β(g) > 0 versus β(g) < 0 imply about the behavior of the coupling at high energies? Give a physical example of each sign.
3. Two systems — a uniaxial ferromagnet and a liquid near its liquid-gas critical point — have the same critical exponents despite completely different microscopic physics. Explain this universality using the language of RG fixed points and relevant operators.

**自测（空白页）**

1. 正规化与重整化的区别是什么？各举一个例子。
2. 定义 β 函数 β(g)。β(g) > 0 与 β(g) < 0 分别对高能下耦合常数的行为意味着什么？各给出一个物理例子。
3. 两个系统——单轴铁磁体和液-气临界点附近的液体——尽管微观物理完全不同，却具有相同的临界指数。用重整化群不动点和相关算符的语言解释这种普适性。

---

← Previous: [Module 6.5 — Canonical Quantization of Fields](./module-6.5-canonical-quantization.md) · [Phase 6 index](./README.md) · Next: [Module 6.7 — Exactly Solvable Models & Long-Range Order](./module-6.7-exactly-solvable-models-and-long-range-order.md) →

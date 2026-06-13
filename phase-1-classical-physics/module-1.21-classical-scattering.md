# Module 1.21 — Classical Scattering Theory
**模块 1.21 — 经典散射理论**

> **Phase 1 — [Classical Physics](./README.md)** · Format: Definition → Demonstration → Application
> **第 1 阶段 — 经典物理 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-1.21-classical-scattering-derivations.md)

---

## 1. Cross Section, Impact Parameter & the Scattering Angle · 截面、瞄准距离与散射角

**Definition.** In a scattering experiment a uniform beam of particles, each of energy $E$, is fired at a fixed central potential $U(r)$. A particle's trajectory is labelled by its **impact parameter** $b$ — the perpendicular distance from the target of the incoming asymptote. The interaction deflects it by a **scattering angle** $\theta$. The **differential cross section** $d\sigma/d\Omega$ is defined so that $(d\sigma/d\Omega)\,d\Omega$ is the effective target area sending particles into solid angle $d\Omega$ about $\theta$. For a central potential the angle depends only on $b$, and conservation of particle number gives $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$ (Module 1.5 supplies the central-force orbits behind $b(\theta)$).

**定义。** 在散射实验中，一束均匀的、每个粒子能量为 $E$ 的粒子，射向固定的中心势 $U(r)$。粒子轨迹由其**瞄准距离** $b$ 标记——入射渐近线到靶点的垂直距离。相互作用使其偏转一个**散射角** $\theta$。**微分散射截面** $d\sigma/d\Omega$ 的定义使得 $(d\sigma/d\Omega)\,d\Omega$ 是把粒子送入 $\theta$ 附近立体角 $d\Omega$ 的有效靶面积。对中心势，角度只依赖于 $b$，粒子数守恒给出 $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$（模块 1.5 提供了 $b(\theta)$ 背后的中心力轨道）。

**Demonstration.** A ring of incident area $d\sigma = 2\pi b\,db$ maps onto an annulus of solid angle $d\Omega = 2\pi \sin\theta\,d\theta$ on the detector sphere. Equating the particle flux through both (the beam flux is uniform) gives $d\sigma = (b/\sin\theta)|db/d\theta|\,d\Omega$; the absolute value appears because a more central particle (smaller $b$) typically scatters through a larger angle, so $db/d\theta < 0$. Knowing the function $b(\theta)$ for a given $U(r)$ thus fixes the entire angular distribution.

**演示。** 入射面积为 $d\sigma = 2\pi b\,db$ 的环，映射到探测球面上立体角为 $d\Omega = 2\pi \sin\theta\,d\theta$ 的圆环带。令穿过两者的粒子通量相等（束流通量均匀），得 $d\sigma = (b/\sin\theta)|db/d\theta|\,d\Omega$；绝对值的出现是因为更靠中心的粒子（较小的 $b$）通常散射到更大的角度，故 $db/d\theta < 0$。因此，对给定 $U(r)$ 知道函数 $b(\theta)$ 就确定了整个角分布。

**Application.** The cross section is the bridge between the unobservable microscopic potential and the measurable count rate $dN/d\Omega = (\text{incident flux}) \times (d\sigma/d\Omega)$. Inverting measured angular distributions to infer the underlying force is the working principle of every scattering experiment, from Rutherford's gold foil to the LHC. The quantum version (Module 3.8, Born approximation) keeps the very same definition of $d\sigma/d\Omega$.

**应用。** 散射截面是不可观测的微观势与可测的计数率 $dN/d\Omega = (\text{入射通量})\times(d\sigma/d\Omega)$ 之间的桥梁。把测得的角分布反演以推断背后的作用力，是从卢瑟福金箔到大型强子对撞机的每个散射实验的工作原理。量子版本（模块 3.8，玻恩近似）保留了完全相同的 $d\sigma/d\Omega$ 定义。

## 2. The Rutherford Formula · 卢瑟福公式

**Definition.** For the repulsive Coulomb potential $U(r) = k/r$ with $k = q_1 q_2/(4\pi\varepsilon_0)$, the central-force orbit is a hyperbola, and the impact parameter relates to the scattering angle by $b = (k/2E) \cot(\theta/2)$. Substituting into $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$ yields the **Rutherford differential cross section**: $d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2) = [q_1 q_2/(16\pi\varepsilon_0 E)]^2/\sin^4(\theta/2)$.

**定义。** 对排斥性库仑势 $U(r) = k/r$，其中 $k = q_1 q_2/(4\pi\varepsilon_0)$，中心力轨道是双曲线，瞄准距离与散射角的关系为 $b = (k/2E) \cot(\theta/2)$。代入 $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$ 给出**卢瑟福微分散射截面**：$d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2) = [q_1 q_2/(16\pi\varepsilon_0 E)]^2/\sin^4(\theta/2)$。

**Demonstration.** Differentiating $b = (k/2E) \cot(\theta/2)$ gives $db/d\theta = -(k/4E) \csc^2(\theta/2)$. With $\sin\theta = 2 \sin(\theta/2) \cos(\theta/2)$, the product $(b/\sin\theta)|db/d\theta|$ collapses cleanly: the $\cot(\theta/2)$ and the two $\sin(\theta/2) \cos(\theta/2)$ factors combine into $1/\sin^4(\theta/2)$, leaving the prefactor $(k/4E)^2$. The cross section diverges as $\theta \to 0$ ($\sin^4(\theta/2) \to 0$), so the **total cross section** $\int(d\sigma/d\Omega)\,d\Omega$ **is infinite** — a direct fingerprint of the infinite range of the Coulomb force; a screened or finite-range potential restores a finite total cross section.

**演示。** 对 $b = (k/2E) \cot(\theta/2)$ 求导得 $db/d\theta = -(k/4E) \csc^2(\theta/2)$。利用 $\sin\theta = 2 \sin(\theta/2) \cos(\theta/2)$，乘积 $(b/\sin\theta)|db/d\theta|$ 干净地化简：$\cot(\theta/2)$ 与两个 $\sin(\theta/2) \cos(\theta/2)$ 因子合并为 $1/\sin^4(\theta/2)$，剩下前因子 $(k/4E)^2$。当 $\theta \to 0$（$\sin^4(\theta/2) \to 0$）时截面发散，故**总截面 $\int(d\sigma/d\Omega)\,d\Omega$ 无穷大**——这是库仑力无穷力程的直接印记；屏蔽势或有限力程势可恢复有限的总截面。

**Application.** Rutherford's 1911 analysis of $\alpha$-particles scattered off gold foil (Module 9.3) revealed the rare large-angle deflections that demanded a tiny massive nucleus, overturning the plum-pudding atom. Remarkably the **quantum** calculation (Module 3.8, Born approximation) gives the *identical* formula — the $1/\sin^4(\theta/2)$ law survives the transition to wave mechanics. The same logic, scaled to GeV energies, underlies deep inelastic scattering (Module 8.9), whose large-angle excess revealed pointlike quarks inside the proton.

**应用。** 卢瑟福 1911 年对 $\alpha$ 粒子散射金箔（模块 9.3）的分析揭示了罕见的大角度偏转，这要求存在一个微小而致密的原子核，推翻了枣糕模型原子。值得注意的是，**量子**计算（模块 3.8，玻恩近似）给出*完全相同*的公式——$1/\sin^4(\theta/2)$ 定律在过渡到波动力学时依然成立。同样的逻辑放大到 GeV 能标，构成了深度非弹性散射（模块 8.9）的基础，其大角度的超出揭示了质子内部点状的夸克。

## Key results · 核心结果

- Impact parameter $b$; differential cross section $\dfrac{d\sigma}{d\Omega}=\dfrac{b}{\sin\theta}\left|\dfrac{db}{d\theta}\right|$ · 碰撞参数与微分截面
- Rutherford $\dfrac{d\sigma}{d\Omega}=\left(\dfrac{k}{4E}\right)^2\dfrac1{\sin^4(\theta/2)}$ · 卢瑟福散射
- Total cross section by integrating over solid angle · 总截面
- Coulomb total $\sigma$ diverges (infinite range); screening makes it finite · 库仑总截面发散

---

**Self-test (blank page)**

1. Define the impact parameter and the differential cross section, and derive $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$ from number conservation.
2. Explain physically why $db/d\theta < 0$ for a repulsive potential and why the absolute value is needed.
3. Starting from $b = (k/2E) \cot(\theta/2)$, reproduce the Rutherford cross section $d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2)$.
4. Why does the Coulomb total cross section diverge, and what changes for a screened (finite-range) potential?

**自测（空白页）**

1. 定义瞄准距离和微分散射截面，并由粒子数守恒推导 $d\sigma/d\Omega = (b/\sin\theta)|db/d\theta|$。
2. 从物理上解释为何排斥势下 $db/d\theta < 0$，以及为何需要绝对值。
3. 从 $b = (k/2E) \cot(\theta/2)$ 出发，复现卢瑟福截面 $d\sigma/d\Omega = (k/4E)^2/\sin^4(\theta/2)$。
4. 为何库仑总截面发散？对屏蔽（有限力程）势又有何变化？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** Number conservation: particles in the ring $2\pi b\,db$ scatter into $d\Omega=2\pi\sin\theta\,d\theta$, so $\dfrac{d\sigma}{d\Omega}=\dfrac{b}{\sin\theta}\left|\dfrac{db}{d\theta}\right|$. · 由粒子数守恒导出。
**2.** For a repulsive potential a larger $b$ gives a smaller deflection $\theta$, so $db/d\theta<0$; the absolute value keeps the cross section positive. · 排斥势 $db/d\theta<0$。
**3.** $b=\dfrac{k}{2E}\cot(\theta/2)$, $db/d\theta=-\dfrac{k}{4E}\csc^2(\theta/2)$, giving $\dfrac{d\sigma}{d\Omega}=\left(\dfrac{k}{4E}\right)^2\dfrac1{\sin^4(\theta/2)}$. · 得卢瑟福公式。
**4.** $\sigma=\int d\sigma$ diverges because $1/\sin^4(\theta/2)$ blows up at small $\theta$ — the $1/r$ potential never vanishes. Screening cuts off small-angle (large-$b$) scattering, making $\sigma$ finite. · 库仑发散;屏蔽给有限截面。

</details>

---

← Previous: [Module 1.20 — Canonical Transformations & Hamilton–Jacobi](./module-1.20-canonical-transformations-hamilton-jacobi.md) · [Phase 1 index](./README.md) · Next: [Module 1.22 — Retarded Potentials & Radiation Reaction](./module-1.22-retarded-potentials-radiation-reaction.md) →

# Module 5.4 — The Cooper Problem ⭐
**模块 5.4 — 库珀问题 ⭐**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.4-the-cooper-problem-derivations.md)

---

## 1. Instability of the Fermi Sea · 费米海的不稳定性

**Definition.** Cooper's result: two electrons added just above a filled Fermi sea, interacting through **any** arbitrarily weak attraction, form a **bound pair** — a **Cooper pair**. The normal metal is therefore unstable to pairing.

**定义。** 库珀的结论：在填满的费米海之上刚刚加入的两个电子，通过**任意**弱小的吸引力相互作用，即可形成**束缚对**——即**库珀对**。因此，正常金属对于配对是不稳定的。

**Demonstration.** Setting up the two-electron problem for a pair in states $(k\uparrow, -k\downarrow)$ and solving for the bound state gives a binding energy that is **non-analytic** in the coupling $g$, of the form $\propto e^{-1/(g \cdot N(0))}$ ($N(0) = $ density of states at the Fermi level, Module 4.5). Because it's non-analytic, **no order of perturbation theory could ever produce it** — pairing is intrinsically collective.

**演示。** 对处于态 $(k\uparrow, -k\downarrow)$ 的对建立双电子问题并求解束缚态，得到的结合能对耦合常数 $g$ 是**非解析**的，形式为 $\propto e^{-1/(g \cdot N(0))}$（$N(0)$ 为费米面处的态密度，模块 4.5）。由于是非解析的，**任何阶的微扰论都无法得出它**——配对本质上是集体行为。

**Application.** This proves the normal state must reorganize into a paired state, motivating the full BCS many-body treatment (5.5). The pairing $(k\uparrow, -k\downarrow)$ is exactly the **spin singlet** of Module 3.11, written with the operators of Module 3.12.

**应用。** 这证明了正常态必定重组为配对态，从而为完整的 BCS 多体处理（5.5）提供了动机。配对 $(k\uparrow, -k\downarrow)$ 正是模块 3.11 中的**自旋单态**，用模块 3.12 的算符写出。

## Key results · 核心结果

- Two electrons above a filled Fermi sea bind for *any* attractive interaction · 费米海之上任意吸引都能成对
- Binding energy $\propto e^{-1/(g\,N(0))}$ — non-perturbative in the coupling $g$ · 结合能对耦合非微扰
- The Fermi sea is unstable to pair formation — the gateway to BCS · 费米海对配对不稳定,通往 BCS
- Pairing is between $(\mathbf{k}\uparrow, -\mathbf{k}\downarrow)$ · 配对发生于 $(\mathbf{k}\uparrow,-\mathbf{k}\downarrow)$

---

**Self-test (blank page)**

1. State Cooper's theorem: two electrons just above a filled Fermi sea, subject to any arbitrarily weak attraction, form a bound pair. Why is the filled Fermi sea essential — would the same argument work in vacuum?
2. The Cooper pair binding energy has the form $\propto e^{-1/(g \cdot N(0))}$. Explain why this non-analytic dependence on the coupling $g$ means no finite order of perturbation theory can ever predict pairing.
3. Why do Cooper pairs form in the $(k\uparrow, -k\downarrow)$ channel? What symmetry arguments — time reversal and the Pauli principle — favour this combination over, say, $(k\uparrow, k'\uparrow)$?
4. If the density of states at the Fermi level $N(0)$ doubles (e.g. by changing the material), how does the Cooper pair binding energy change? Does $T_c$ increase or decrease, and by how much according to the exponential formula?

**自测（空白页）**

1. 写出库珀定理：在填满的费米海上方刚加入的两个电子，受任意弱小吸引力的作用即可形成束缚对。为何填满的费米海是必要条件——同样的论证在真空中能成立吗？
2. 库珀对结合能的形式为 $\propto e^{-1/(g \cdot N(0))}$。解释为何这种对耦合常数 $g$ 的非解析依赖意味着任意有限阶微扰论都无法预言配对。
3. 为何库珀对在 $(k\uparrow, -k\downarrow)$ 通道中形成？哪些对称性论证——时间反演和泡利原理——支持这种组合而非例如 $(k\uparrow, k'\uparrow)$？
4. 若费米能级处的态密度 $N(0)$ 加倍（例如通过更换材料），库珀对结合能如何变化？根据指数公式，$T_c$ 增大还是减小，变化量级是多少？

---

← Previous: [Module 5.3 — Ginzburg–Landau Theory](./module-5.3-ginzburg-landau-theory.md) · [Phase 5 index](./README.md) · Next: [Module 5.5 — BCS Theory](./module-5.5-bcs-theory.md) →

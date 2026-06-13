# Module 5.6 — Tunneling & the Gap
**模块 5.6 — 隧穿与能隙**

> **Phase 5 — [Superconductivity](./README.md)** · Format: Definition → Demonstration → Application
> **第 5 阶段 — 超导 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-5.6-tunneling-and-the-gap-derivations.md)

---

## 1. Measuring the Gap Directly · 直接测量能隙

**Definition.** In **single-particle (Giaever) tunneling**, electrons tunnel across a thin insulator between a normal metal and a superconductor; the current maps out the superconducting density of states.

**定义。** 在**单粒子（贾埃弗）隧穿**中，电子穿过正常金属与超导体之间的薄绝缘层隧穿；电流描绘出超导态密度的轮廓。

**Demonstration.** The BCS density of states is $N_s(E) = N(0) \cdot E/\sqrt{E^2 - \Delta^2}$ for $E > \Delta$ and **zero inside the gap**. So the tunneling I–V shows **no current until $eV$ exceeds $\Delta$**, then a sharp rise — a direct readout of the gap (computed via the golden rule and DOS of Modules 3.8 and 4.5).

**演示。** BCS 态密度为 $N_s(E) = N(0) \cdot E/\sqrt{E^2 - \Delta^2}$（$E > \Delta$ 时），**能隙内为零**。因此隧穿 I–V 曲线显示**直到 $eV$ 超过 $\Delta$ 时才有电流**，随后急剧上升——这是对能隙的直接读出（通过模块 3.8 和 4.5 的黄金法则与态密度计算得出）。

**Application.** This was decisive experimental confirmation of BCS, and it's the conceptual basis for the Josephson junction (5.8).

**应用。** 这是对 BCS 理论决定性的实验验证，也是约瑟夫森结（5.8）的概念基础。

## Key results · 核心结果

- BCS DOS $N_s(E)=N(0)\,E/\sqrt{E^2-\Delta^2}$ for $E>\Delta$, zero inside the gap · BCS 态密度
- NIS tunneling current onsets at $eV=\Delta$ — a direct gap measurement · 隧穿在 $eV=\Delta$ 开启
- Giaever tunneling maps $N_s(E)$ via $dI/dV$ · 贾埃弗隧穿
- As $T\to T_c$, $\Delta(T)\to0$ · 能隙随温度消失

---

**Self-test (blank page)**

1. Write the BCS quasiparticle density of states $N_s(E) = N(0) \cdot E/\sqrt{E^2 - \Delta^2}$ for $E > \Delta$, and state its value for $E < \Delta$. Sketch the shape and explain the divergence just above $\Delta$.
2. In a normal-metal/insulator/superconductor tunnel junction, explain why no single-particle current flows until the bias voltage satisfies $eV \geq \Delta$. How does this provide a direct measurement of the gap?
3. The Giaever tunneling experiment is computed using Fermi's golden rule (Module 3.8) and the BCS density of states. What is the role of the normal-metal DOS in simplifying the result, and what does the I–V characteristic look like?
4. How does the tunneling spectrum change as temperature rises toward $T_c$? What happens to the gap edge feature as $\Delta(T) \to 0$, and how does this confirm the temperature dependence of the BCS gap?

**自测（空白页）**

1. 写出 $E > \Delta$ 时的 BCS 准粒子态密度 $N_s(E) = N(0) \cdot E/\sqrt{E^2 - \Delta^2}$，并给出 $E < \Delta$ 时的值。画出其形状并解释紧靠 $\Delta$ 上方的发散性。
2. 在正常金属/绝缘体/超导体隧道结中，解释为何在偏压满足 $eV \geq \Delta$ 之前没有单粒子电流流动。这如何提供对能隙的直接测量？
3. 贾埃弗隧穿实验通过费米黄金法则（模块 3.8）和 BCS 态密度计算得出。正常金属态密度在简化结果中起什么作用？I–V 特性曲线是什么形状？
4. 当温度升高趋近 $T_c$ 时，隧穿谱如何变化？随着 $\Delta(T) \to 0$，能隙边缘特征发生什么变化？这如何证实 BCS 能隙的温度依赖性？

<details>
<summary><strong>Answer key · 参考答案</strong></summary>

**1.** $N_s(E)=N(0)E/\sqrt{E^2-\Delta^2}$ for $E>\Delta$, and $0$ for $|E|<\Delta$. States expelled from the gap pile up at the edge, giving the divergent coherence peak just above $\Delta$. · 能隙内为零,边缘发散。
**2.** With no states in the gap, single-particle tunneling needs $eV\ge\Delta$ to reach the first quasiparticle states → current onset at $eV=\Delta$, directly measuring $\Delta$. · $eV=\Delta$ 开启,直接测能隙。
**3.** The normal metal's flat DOS near $E_F$ means $dI/dV$ directly maps $N_s(eV)$; the I–V is flat until $eV=\Delta$, then rises. · 正常金属平 DOS 使 $dI/dV$ 映射 $N_s$。
**4.** As $T\to T_c$, $\Delta(T)\to0$: the gap edge moves to zero bias and the I–V becomes ohmic — confirming the BCS $\Delta(T)$. · $\Delta(T)\to0$,I–V 趋欧姆。

</details>

---

← Previous: [Module 5.5 — BCS Theory](./module-5.5-bcs-theory.md) · [Phase 5 index](./README.md) · Next: [Module 5.7 — Type II Superconductors & Vortices](./module-5.7-type-ii-superconductors-and-vortices.md) →

# Module 2.1 — The Laws of Thermodynamics
**模块 2.1 — 热力学定律**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**
>
> 📐 **Full step-by-step proofs:** [Derivations · 推导](./module-2.1-derivations.md)

---

## 1. The Four Laws and Their Physical Content · 四条定律及其物理内涵

**Definition.** Thermodynamics rests on four empirical laws. The **Zeroth Law** establishes temperature as a transitive property: if systems A and B are each in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. The **First Law** is conservation of energy for thermodynamic systems: the change in internal energy $U$ equals heat absorbed minus work done by the system,

**定义。** 热力学建立在四条经验定律之上。**热力学第零定律**将温度确立为一种传递性属性：若系统 A 和 B 分别与 C 处于热平衡，则 A 与 B 之间也处于热平衡。**热力学第一定律**是热力学系统的能量守恒：内能 $U$ 的变化等于系统吸收的热量减去系统对外做的功，

$$ dU = \delta Q - \delta W, $$

where $\delta Q$ and $\delta W$ are path-dependent (inexact differentials). For a gas, $\delta W = P\, dV$. The **Second Law** states that the entropy $S$ of an isolated system never decreases; for a reversible process, $dS = \delta Q/T$, and for an irreversible process, $dS > \delta Q/T$. The **Third Law** (Nernst theorem) states that $S \to 0$ as $T \to 0$ for a perfect crystal, making absolute entropy well defined.

其中 $\delta Q$ 和 $\delta W$ 是路径依赖的（非恰当微分）。对于气体，$\delta W = P\, dV$。**热力学第二定律**指出，孤立系统的熵 $S$ 永不减少；对于可逆过程，$dS = \delta Q/T$；对于不可逆过程，$dS > \delta Q/T$。**热力学第三定律**（能斯特定理）指出，对于完美晶体，当 $T \to 0$ 时 $S \to 0$，使得绝对熵有明确定义。

**Demonstration.** The Carnot cycle is the ideal reversible heat engine operating between a hot reservoir at $T_H$ and a cold reservoir at $T_C$. It consists of two isothermal and two adiabatic (isentropic) strokes. Because every step is reversible, the total entropy change of the universe is zero. The efficiency is

**演示。** 卡诺循环是在高温热源 $T_H$ 和低温热源 $T_C$ 之间运行的理想可逆热机。它由两个等温过程和两个绝热（等熵）过程组成。由于每一步都是可逆的，宇宙的总熵变为零。效率为

$$ \eta = W_\text{net} / Q_H = 1 - T_C / T_H. $$

No engine operating between the same two reservoirs can exceed this efficiency — any attempt to do so would require net entropy decrease, violating the Second Law.

在相同两个热源之间工作的任何热机都不能超过此效率——任何试图超越的努力都需要净熵减少，从而违反第二定律。

**Application.** The inequality $\eta \le 1 - T_C/T_H$ is an absolute engineering ceiling: a power plant with a combustion temperature of 800 K exhausting to 300 K cannot exceed 62.5% efficiency, regardless of mechanical ingenuity. More deeply, the Second Law gives time an arrow — spontaneous processes increase total entropy, distinguishing past from future. The First Law prevents perpetual-motion machines of the first kind (creating energy); the Second Law prevents those of the second kind (converting heat entirely to work in a cycle).

**应用。** 不等式 $\eta \le 1 - T_C/T_H$ 是工程上的绝对上限：一座燃烧温度为 800 K、向 300 K 散热的发电厂无论机械设计多么精妙，效率都不能超过 62.5%。更深层地，第二定律赋予时间一个箭头——自发过程增加总熵，从而区分过去与未来。第一定律阻止第一类永动机（凭空创造能量）；第二定律阻止第二类永动机（在循环中将热量全部转化为功）。

---

## 2. Entropy and Reversibility · 熵与可逆性

**Definition.** For any process taking a system from state A to state B, the Clausius inequality gives $\oint \delta Q/T \le 0$ around a cycle, with equality only for a reversible cycle. The state function entropy is defined via a reversible path:

**定义。** 对于将系统从状态 A 带到状态 B 的任意过程，克劳修斯不等式给出 $\oint \delta Q/T \le 0$（沿循环），仅在可逆循环时取等号。态函数熵通过可逆路径定义：

$$ \Delta S = \int_A^B (\delta Q/T)_\text{rev}. $$

**Demonstration.** For the free expansion of an ideal gas into a vacuum (an irreversible process), $\delta Q = 0$ and $\delta W = 0$, so $\Delta U = 0$ and $T$ is unchanged. Yet the volume doubles, and the entropy increases by $\Delta S = n k_B \ln 2$ per molecule — calculated by imagining a reversible isothermal expansion between the same states. The universe's entropy rises even though the gas itself does all the work of increasing disorder.

**演示。** 对于理想气体向真空的自由膨胀（不可逆过程），$\delta Q = 0$ 且 $\delta W = 0$，故 $\Delta U = 0$，温度不变。然而体积翻倍，每个分子的熵增加 $\Delta S = n k_B \ln 2$——这是通过假想一个连接相同初末态的可逆等温膨胀来计算的。即便是气体自身完成了所有增加无序度的"工作"，宇宙的熵仍然升高了。

**Application.** Entropy is the link between macroscopic thermodynamics and the microscopic world. Boltzmann's relation $S = k_B \ln \Omega$ (where $\Omega$ is the number of accessible microstates) will be derived from statistical mechanics in Module 2.4 and underpins quantum statistics in Module 2.5.

**应用。** 熵是宏观热力学与微观世界之间的纽带。玻尔兹曼关系 $S = k_B \ln \Omega$（其中 $\Omega$ 为可及微观态数目）将在模块 2.4 中从统计力学推导出来，并支撑模块 2.5 中的量子统计。

---

## Self-test (blank page) · 自测（空白页）

1. State each of the four laws in one sentence. What physical quantity does each law introduce or constrain?
2. Derive the Carnot efficiency $\eta = 1 - T_C/T_H$ using only the condition that the cycle is reversible ($\Delta S_\text{universe} = 0$).
3. A refrigerator moves heat from $T_C = 250$ K to $T_H = 300$ K. What is the minimum work required per joule of heat extracted from the cold reservoir?
4. Why is $dU$ an exact differential while $\delta Q$ and $\delta W$ individually are not? Give a concrete example showing path-dependence of $\delta Q$.

**自测（空白页）**

1. 各用一句话陈述四条热力学定律。每条定律引入或约束了哪个物理量？
2. 仅利用循环可逆（$\Delta S_\text{universe} = 0$）的条件，推导卡诺效率 $\eta = 1 - T_C/T_H$。
3. 一台冰箱将热量从 $T_C = 250$ K 传输到 $T_H = 300$ K。从冷源取出每焦耳热量所需的最小功是多少？
4. 为什么 $dU$ 是恰当微分，而 $\delta Q$ 和 $\delta W$ 单独来看不是？给出一个具体例子说明 $\delta Q$ 的路径依赖性。

---

← [Phase 2 index](./README.md) · Next: [Module 2.2 — Thermodynamic Potentials & Maxwell Relations](./module-2.2-thermodynamic-potentials.md) →

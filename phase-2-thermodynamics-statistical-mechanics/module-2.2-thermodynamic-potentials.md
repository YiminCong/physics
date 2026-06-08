# Module 2.2 — Thermodynamic Potentials & Maxwell Relations
**模块 2.2 — 热力学势与麦克斯韦关系**

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application
> **第 2 阶段 — 热力学与统计力学 · 格式：定义 → 演示 → 应用**

---

## 1. The Four Potentials and Legendre Transforms · 四个热力学势与勒让德变换

**Definition.** Starting from the fundamental relation dU = T dS − P dV (for a simple compressible system with no particle exchange), we obtain three further potentials by Legendre transforms — replacing an extensive variable by its conjugate intensive one as the natural independent variable:

**定义。** 从基本关系 dU = T dS − P dV 出发（对于无粒子交换的简单可压缩系统），通过勒让德变换——以共轭强度变量替代广延变量作为自然独立变量——得到另外三个热力学势：

- **Internal energy** U(S, V): dU = T dS − P dV
- **Enthalpy** H = U + PV, so dH = T dS + V dP; natural variables (S, P)
- **Helmholtz free energy** F = U − TS, so dF = −S dT − P dV; natural variables (T, V)
- **Gibbs free energy** G = U − TS + PV = H − TS, so dG = −S dT + V dP; natural variables (T, P)

Each potential is minimized at equilibrium under its corresponding natural constraints: F is minimized at fixed T and V; G is minimized at fixed T and P (the most common laboratory condition).

- **内能** U(S, V)：dU = T dS − P dV
- **焓** H = U + PV，故 dH = T dS + V dP；自然变量为 (S, P)
- **亥姆霍兹自由能** F = U − TS，故 dF = −S dT − P dV；自然变量为 (T, V)
- **吉布斯自由能** G = U − TS + PV = H − TS，故 dG = −S dT + V dP；自然变量为 (T, P)

每个热力学势在其对应的自然约束下于平衡时取极小值：F 在固定 T 和 V 时极小；G 在固定 T 和 P 时极小（这是最常见的实验室条件）。

**Demonstration.** From dF = −S dT − P dV, reading off partial derivatives gives

**演示。** 由 dF = −S dT − P dV，读出偏导数为

(∂F/∂T)_V = −S     and     (∂F/∂V)_T = −P.

Taking the cross-partial ∂²F/∂V∂T in both orders and equating (Schwarz's theorem, valid whenever F is smooth) yields the Maxwell relation

对 ∂²F/∂V∂T 以两种顺序求混合偏导并令其相等（施瓦茨定理，在 F 光滑时成立），得到麦克斯韦关系

(∂S/∂V)_T = (∂P/∂T)_V.

Applying the same logic to each potential generates four Maxwell relations in total:

对每个热力学势应用同样的逻辑，共得到四个麦克斯韦关系：

- From U:   (∂T/∂V)_S = −(∂P/∂S)_V
- From H:   (∂T/∂P)_S =  (∂V/∂S)_P
- From F:   (∂S/∂V)_T =  (∂P/∂T)_V
- From G:   (∂S/∂P)_T = −(∂V/∂T)_P

**Application.** The Maxwell relations convert unmeasurable derivatives into measurable ones. For example, (∂S/∂P)_T = −(∂V/∂T)_P means that the entropy change with pressure (impossible to measure directly) equals minus the thermal expansivity α = (1/V)(∂V/∂T)_P times V — a table quantity. This machinery underlies all equations of state and is used wherever thermodynamic identities are needed in condensed-matter physics.

**应用。** 麦克斯韦关系将无法直接测量的偏导数转化为可测量的量。例如，(∂S/∂P)_T = −(∂V/∂T)_P 意味着熵随压强的变化（无法直接测量）等于负的热膨胀系数 α = (1/V)(∂V/∂T)_P 乘以 V——这是一个可查表的量。这套机制是所有状态方程的基础，也在凝聚态物理中凡需热力学恒等式之处广泛应用。

---

## 2. Equilibrium Conditions and Chemical Potential · 平衡条件与化学势

**Definition.** When particle exchange is allowed, the fundamental relation gains a term μ dN, where μ = (∂U/∂N)_{S,V} is the **chemical potential**. The full relation becomes

**定义。** 当允许粒子交换时，基本关系增加一项 μ dN，其中 μ = (∂U/∂N)_{S,V} 为**化学势**。完整关系变为

dU = T dS − P dV + μ dN,

and correspondingly dG = −S dT + V dP + μ dN, so μ = (∂G/∂N)_{T,P}. At equilibrium between two phases or subsystems, T, P, and μ must all be equal.

相应地 dG = −S dT + V dP + μ dN，故 μ = (∂G/∂N)_{T,P}。两相或两子系统之间达到平衡时，T、P 和 μ 必须全部相等。

**Demonstration.** For an ideal gas, G = N k_B T ln(P/P₀) + N g₀(T), so μ = k_B T ln(P/P₀) + g₀(T). Two phases coexist when μ_liquid(T, P) = μ_gas(T, P), which traces out the liquid–gas coexistence curve — the Clausius–Clapeyron equation dP/dT = L T / (T ΔV) follows directly from this equality and the Maxwell relation from G.

**演示。** 对于理想气体，G = N k_B T ln(P/P₀) + N g₀(T)，故 μ = k_B T ln(P/P₀) + g₀(T)。当 μ_liquid(T, P) = μ_gas(T, P) 时两相共存，这描绘出液–气共存曲线——克劳修斯–克拉珀龙方程 dP/dT = L T / (T ΔV) 直接由该等式与 G 的麦克斯韦关系推出。

**Application.** The chemical potential is the central quantity in quantum statistics (Module 2.5): it sets the Fermi energy E_F in a metal and controls Bose–Einstein condensation. The condition G minimized at fixed T, P is also the foundation for understanding phase transitions in Module 2.3, where G (or F) is expanded in an order parameter.

**应用。** 化学势是量子统计（模块 2.5）中的核心量：它确定金属中的费米能 E_F，并控制玻色–爱因斯坦凝聚。在固定 T、P 条件下 G 极小的条件也是理解模块 2.3 中相变的基础，在那里 G（或 F）被展开为序参量的幂级数。

---

## Self-test (blank page) · 自测（空白页）

1. Write down dU, dH, dF, and dG and state the natural variables of each potential.
2. Derive the Maxwell relation (∂S/∂P)_T = −(∂V/∂T)_P from the Gibbs free energy.
3. Explain in one sentence why G is the relevant potential for chemical reactions carried out at constant temperature and pressure.
4. Using the Maxwell relation from F, show that for an ideal gas (PV = Nk_BT) the internal energy U does not depend on volume at fixed T.

**自测（空白页）**

1. 写出 dU、dH、dF 和 dG，并陈述每个热力学势的自然变量。
2. 从吉布斯自由能推导麦克斯韦关系 (∂S/∂P)_T = −(∂V/∂T)_P。
3. 用一句话解释为什么 G 是在恒温恒压下进行的化学反应的相关热力学势。
4. 利用 F 的麦克斯韦关系，证明对于理想气体（PV = Nk_BT），内能 U 在固定 T 时不依赖于体积。

---

← Previous: [Module 2.1 — The Laws of Thermodynamics](./module-2.1-laws-of-thermodynamics.md) · [Phase 2 index](./README.md) · Next: [Module 2.3 — Free Energy & Phase Transitions](./module-2.3-free-energy-phase-transitions.md) →

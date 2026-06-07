# Module 2.1 — The Laws of Thermodynamics

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Four Laws and Their Physical Content

**Definition.** Thermodynamics rests on four empirical laws. The **Zeroth Law** establishes temperature as a transitive property: if systems A and B are each in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. The **First Law** is conservation of energy for thermodynamic systems: the change in internal energy U equals heat absorbed minus work done by the system,

dU = δQ − δW,

where δQ and δW are path-dependent (inexact differentials). For a gas, δW = P dV. The **Second Law** states that the entropy S of an isolated system never decreases; for a reversible process, dS = δQ/T, and for an irreversible process, dS > δQ/T. The **Third Law** (Nernst theorem) states that S → 0 as T → 0 for a perfect crystal, making absolute entropy well defined.

**Demonstration.** The Carnot cycle is the ideal reversible heat engine operating between a hot reservoir at T_H and a cold reservoir at T_C. It consists of two isothermal and two adiabatic (isentropic) strokes. Because every step is reversible, the total entropy change of the universe is zero. The efficiency is

η = W_net / Q_H = 1 − T_C / T_H.

No engine operating between the same two reservoirs can exceed this efficiency — any attempt to do so would require net entropy decrease, violating the Second Law.

**Application.** The inequality η ≤ 1 − T_C/T_H is an absolute engineering ceiling: a power plant with a combustion temperature of 800 K exhausting to 300 K cannot exceed 62.5% efficiency, regardless of mechanical ingenuity. More deeply, the Second Law gives time an arrow — spontaneous processes increase total entropy, distinguishing past from future. The First Law prevents perpetual-motion machines of the first kind (creating energy); the Second Law prevents those of the second kind (converting heat entirely to work in a cycle).

---

## 2. Entropy and Reversibility

**Definition.** For any process taking a system from state A to state B, the Clausius inequality gives ∮ δQ/T ≤ 0 around a cycle, with equality only for a reversible cycle. The state function entropy is defined via a reversible path:

ΔS = ∫_A^B (δQ/T)_rev.

**Demonstration.** For the free expansion of an ideal gas into a vacuum (an irreversible process), δQ = 0 and δW = 0, so ΔU = 0 and T is unchanged. Yet the volume doubles, and the entropy increases by ΔS = n k_B ln 2 per molecule — calculated by imagining a reversible isothermal expansion between the same states. The universe's entropy rises even though the gas itself does all the work of increasing disorder.

**Application.** Entropy is the link between macroscopic thermodynamics and the microscopic world. Boltzmann's relation S = k_B ln Ω (where Ω is the number of accessible microstates) will be derived from statistical mechanics in Module 2.4 and underpins quantum statistics in Module 2.5.

---

## Self-test (blank page)

1. State each of the four laws in one sentence. What physical quantity does each law introduce or constrain?
2. Derive the Carnot efficiency η = 1 − T_C/T_H using only the condition that the cycle is reversible (ΔS_universe = 0).
3. A refrigerator moves heat from T_C = 250 K to T_H = 300 K. What is the minimum work required per joule of heat extracted from the cold reservoir?
4. Why is dU an exact differential while δQ and δW individually are not? Give a concrete example showing path-dependence of δQ.

---

← [Phase 2 index](./README.md) · Next: [Module 2.2 — Thermodynamic Potentials & Maxwell Relations](./module-2.2-thermodynamic-potentials.md) →

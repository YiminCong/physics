# Module 2.2 — Thermodynamic Potentials & Maxwell Relations

> **Phase 2 — [Thermodynamics & Statistical Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. The Four Potentials and Legendre Transforms

**Definition.** Starting from the fundamental relation dU = T dS − P dV (for a simple compressible system with no particle exchange), we obtain three further potentials by Legendre transforms — replacing an extensive variable by its conjugate intensive one as the natural independent variable:

- **Internal energy** U(S, V): dU = T dS − P dV
- **Enthalpy** H = U + PV, so dH = T dS + V dP; natural variables (S, P)
- **Helmholtz free energy** F = U − TS, so dF = −S dT − P dV; natural variables (T, V)
- **Gibbs free energy** G = U − TS + PV = H − TS, so dG = −S dT + V dP; natural variables (T, P)

Each potential is minimized at equilibrium under its corresponding natural constraints: F is minimized at fixed T and V; G is minimized at fixed T and P (the most common laboratory condition).

**Demonstration.** From dF = −S dT − P dV, reading off partial derivatives gives

(∂F/∂T)_V = −S     and     (∂F/∂V)_T = −P.

Taking the cross-partial ∂²F/∂V∂T in both orders and equating (Schwarz's theorem, valid whenever F is smooth) yields the Maxwell relation

(∂S/∂V)_T = (∂P/∂T)_V.

Applying the same logic to each potential generates four Maxwell relations in total:

- From U:   (∂T/∂V)_S = −(∂P/∂S)_V
- From H:   (∂T/∂P)_S =  (∂V/∂S)_P
- From F:   (∂S/∂V)_T =  (∂P/∂T)_V
- From G:   (∂S/∂P)_T = −(∂V/∂T)_P

**Application.** The Maxwell relations convert unmeasurable derivatives into measurable ones. For example, (∂S/∂P)_T = −(∂V/∂T)_P means that the entropy change with pressure (impossible to measure directly) equals minus the thermal expansivity α = (1/V)(∂V/∂T)_P times V — a table quantity. This machinery underlies all equations of state and is used wherever thermodynamic identities are needed in condensed-matter physics.

---

## 2. Equilibrium Conditions and Chemical Potential

**Definition.** When particle exchange is allowed, the fundamental relation gains a term μ dN, where μ = (∂U/∂N)_{S,V} is the **chemical potential**. The full relation becomes

dU = T dS − P dV + μ dN,

and correspondingly dG = −S dT + V dP + μ dN, so μ = (∂G/∂N)_{T,P}. At equilibrium between two phases or subsystems, T, P, and μ must all be equal.

**Demonstration.** For an ideal gas, G = N k_B T ln(P/P₀) + N g₀(T), so μ = k_B T ln(P/P₀) + g₀(T). Two phases coexist when μ_liquid(T, P) = μ_gas(T, P), which traces out the liquid–gas coexistence curve — the Clausius–Clapeyron equation dP/dT = L T / (T ΔV) follows directly from this equality and the Maxwell relation from G.

**Application.** The chemical potential is the central quantity in quantum statistics (Module 2.5): it sets the Fermi energy E_F in a metal and controls Bose–Einstein condensation. The condition G minimized at fixed T, P is also the foundation for understanding phase transitions in Module 2.3, where G (or F) is expanded in an order parameter.

---

## Self-test (blank page)

1. Write down dU, dH, dF, and dG and state the natural variables of each potential.
2. Derive the Maxwell relation (∂S/∂P)_T = −(∂V/∂T)_P from the Gibbs free energy.
3. Explain in one sentence why G is the relevant potential for chemical reactions carried out at constant temperature and pressure.
4. Using the Maxwell relation from F, show that for an ideal gas (PV = Nk_BT) the internal energy U does not depend on volume at fixed T.

---

← Previous: [Module 2.1 — The Laws of Thermodynamics](./module-2.1-laws-of-thermodynamics.md) · [Phase 2 index](./README.md) · Next: [Module 2.3 — Free Energy & Phase Transitions](./module-2.3-free-energy-phase-transitions.md) →

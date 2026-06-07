# Module 3.12 — Symmetry, Identical Particles & Second Quantization ⭐⭐

> **Phase 3 — [Quantum Mechanics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Discrete Symmetries

**Definition.** Beyond continuous symmetries (Module 1.4), discrete ones matter: **parity** (spatial inversion) and **time reversal** classify states and constrain dynamics.

## 2. Second Quantization — the key tool for what's ahead

**Definition.** Instead of tracking labeled particles, track **occupation numbers** of single-particle states. Introduce **creation/annihilation operators**: bosons aₖ†, aₖ with [aₖ, aₖ′†] = δₖₖ′; fermions cₖ†, cₖ with the **anticommutator** {cₖ, cₖ′†} = δₖₖ′. The number operator is n̂ₖ = cₖ†cₖ.

**Demonstration.** A many-fermion state is built by acting creation operators on the vacuum: |Ψ⟩ = c₁† c₂† … |0⟩. The anticommutation {c₁†, c₂†} = 0 automatically enforces antisymmetry and the Pauli principle — c²† = 0 means you can't create two fermions in the same state. This is just the harmonic-oscillator ladder algebra (3.2) promoted to "one oscillator per mode."

**Application.** **This is the single most important tool to carry into superconductivity.** The BCS Hamiltonian (Phase 5) is written entirely in terms of cₖ† and cₖ; Cooper pairing is the operator c_{k↑}† c_{−k↓}†; and the whole machinery of condensed-matter field theory (Phase 6) is second quantization. If only one module of Phase 3 must be airtight, make it this one (alongside 3.2 and 3.5, which it builds on).

---

← Previous: [Module 3.11 — Angular Momentum, Advanced](./module-3.11-angular-momentum-advanced.md) · *Phase 3 index: [Quantum Mechanics](./README.md)*

# Module 6.1 — Second Quantization & the Many-Body Problem ⭐

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Creation, Annihilation, and Field Operators

**Definition.** Second quantization (introduced in Module 3.12) re-expresses quantum mechanics in occupation-number (Fock) space, where the fundamental objects are creation and annihilation operators rather than many-particle wave functions. For bosons, [a_k, a†_k'] = δ_{kk'}; for fermions, {c_k, c†_k'} = δ_{kk'} with {c_k, c_k'} = 0 (Pauli exclusion built in algebraically). A state with n_1 particles in mode 1, n_2 in mode 2, … is written |n_1, n_2, …⟩ — the Fock state. The full Fock space F = ⊕_{N=0}^∞ H_N accommodates any particle number.

**Field operators** assemble the mode operators into a position-space object: ψ(x) = Σ_k φ_k(x) c_k, where φ_k(x) are single-particle orbitals. ψ†(x) creates a particle at x; ψ(x) destroys one. Their (anti)commutators inherit from the mode operators: {ψ(x), ψ†(x')} = δ(x − x') for fermions.

**Demonstration.** A generic one-body Hamiltonian H₁ = Σ_{ij} t_{ij} c†_i c_j, or in field form H₁ = ∫ dx ψ†(x) [−ℏ²∇²/2m + V(x)] ψ(x). A two-body interaction (e.g., Coulomb) becomes H₂ = ½ ∫ dx dx' ψ†(x) ψ†(x') U(x−x') ψ(x') ψ(x). No symmetrization is needed by hand: operator ordering plus (anti)commutation relations enforce it automatically. For N ~ 10²³ particles, writing an antisymmetrized N-particle wave function is computationally hopeless; the Fock-space formalism converts the problem to algebra on a manageable operator algebra.

**Application.** Every subsequent module in Phase 6 is written in this language. The BCS Hamiltonian (Module 5.5) H_BCS = Σ_k ξ_k (c†_{k↑}c_{k↑} + c†_{−k↓}c_{−k↓}) − Σ_{kk'} V_{kk'} c†_{k↑}c†_{−k↓}c_{−k'↓}c_{k'↑} is second-quantized from the start: the pairing correlator ⟨c_{−k↓}c_{k↑}⟩ ≠ 0 signals the condensate. The formalism is also the starting point for Green's functions (Module 6.2) and Feynman diagrams (Module 6.3).

---

## 2. Why Fock Space is the Only Sane Bookkeeping

**Definition.** At fixed N, an N-boson or N-fermion wave function lives in the symmetrized or antisymmetrized tensor product of N single-particle Hilbert spaces. For N = 10²³ this object has an astronomical number of degrees of freedom and cannot be written down. Fock space instead labels states by occupation numbers {n_k}, which are integers (bosons) or 0/1 (fermions). The entire physics is encoded in how operators act on these labels.

**Demonstration.** The number operator N̂ = Σ_k c†_k c_k commutes with any number-conserving Hamiltonian, so energy eigenstates carry a good quantum number N. When particle number is not conserved — open systems, superconductors, relativistic QFT — Fock space allows superpositions of different N, essential for describing the BCS ground state |BCS⟩ = Π_k (u_k + v_k c†_{k↑}c†_{−k↓})|0⟩ which is a superposition of states with 0, 2, 4, … Cooper pairs.

**Application.** Fock space is the universal arena: non-relativistic condensed matter (Phases 4–5), relativistic QFT (Module 6.5 and Phase 8), and finite-temperature field theory (Module 6.4). Coleman "Introduction to Many-Body Physics" and Fetter & Walecka "Quantum Theory of Many-Particle Systems" both open with this formalism for exactly this reason.

---

## Self-test (blank page)

1. Write the anticommutation relations for fermionic field operators ψ(x) and ψ†(x'). Derive them from the mode-operator anticommutators {c_k, c†_{k'}} = δ_{kk'}.
2. Express the kinetic-energy operator T = Σ_i p²_i/2m in second-quantized form using field operators in momentum space. What does the occupation-number state |n_{k₁}, n_{k₂}, …⟩ represent physically?
3. Why does the BCS ground state require Fock space (rather than fixed-N Hilbert space) for its natural description?

---

← [Phase 6 index](./README.md) · Next: [Module 6.2 — Green's Functions & Propagators](./module-6.2-greens-functions.md) →

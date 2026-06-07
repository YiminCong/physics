# Module 6.4 — Path Integrals & Field Theory ⭐

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Feynman's Sum Over Histories

**Definition.** The Feynman path integral (introduced in Module 3.10) expresses the quantum amplitude for a particle to travel from x_i to x_f in time T as a sum over every classical path: ⟨x_f|e^{−iĤT/ℏ}|x_i⟩ = ∫ D[x(t)] e^{iS[x]/ℏ}, where S[x] = ∫₀^T dt L(x, ẋ) is the classical action (Module 1.3) and D[x(t)] denotes the functional measure — integration over the infinite-dimensional space of all paths. Each path carries a phase e^{iS/ℏ}; paths near the classical trajectory (δS = 0) interfere constructively and dominate in the ℏ → 0 limit, recovering classical mechanics.

Passing to a field theory, x(t) is replaced by a field configuration φ(x,t). The quantum amplitude becomes a functional integral ∫ Dφ e^{iS[φ]/ℏ} over all field histories. This is the foundation of modern quantum field theory and of the field-theoretic formulation of statistical mechanics.

**Demonstration.** Performing a Wick rotation t → −iτ (imaginary time, τ ∈ [0, ℏβ] where β = 1/k_B T) converts the oscillatory factor e^{iS/ℏ} → e^{−S_E/ℏ}, where S_E is the Euclidean action. The quantum partition function becomes Z = Tr e^{−βĤ} = ∫_{periodic} Dφ e^{−S_E[φ]/ℏ} with fields obeying periodic (bosons) or antiperiodic (fermions) boundary conditions in τ. This is formally identical to a classical statistical mechanics partition function in d+1 dimensions with inverse temperature β playing the role of the imaginary-time extent. The analogy is exact and powerful: finite-temperature QFT and classical statistical field theory are the same mathematical object.

**Application.** The effective action Γ[φ_cl] is defined as the Legendre transform of ln Z with respect to an external source J: it is the generating functional for one-particle-irreducible (1PI) diagrams, and its saddle point δΓ/δφ_cl = 0 reproduces the classical equations of motion at the quantum level. Expanding Γ around a uniform saddle recovers Landau–Ginzburg theory (Module 2.3 and Module 5.3) as the leading approximation; loop corrections give quantum and thermal fluctuations. Altland & Simons "Condensed Matter Field Theory" develops this connection systematically throughout.

---

## 2. Field Integrals for Fermions and Bosons

**Definition.** Fermionic field integrals require Grassmann variables — anticommuting numbers η, η̄ with {η_i, η_j} = 0 — because ordinary c-numbers cannot satisfy fermionic statistics. The Gaussian Grassmann integral ∫ Dη̄ Dη e^{−η̄ A η} = det A (note: determinant in the numerator, not denominator as for bosons where ∫ Dφ* Dφ e^{−φ* A φ} = (det A)^{−1}). This sign reversal is the path-integral avatar of Fermi statistics and underlies the fermion determinant in lattice gauge theory and condensed matter calculations. Boson coherent-state path integrals use ordinary complex fields φ, φ*.

**Demonstration.** For free fermions, integrating out the fermionic fields produces a factor det[∂_τ − H] = exp Tr ln[∂_τ − H], which upon expanding Tr ln in powers of H generates exactly the linked-cluster expansion of connected Green's functions — the same combinatorics encoded in Feynman diagrams (Module 6.3) but derived here from a single Gaussian integral. The connection is not coincidental: Wick's theorem is the statement that a Gaussian functional integral has only pairwise contractions.

**Application.** The path-integral language is the shared vocabulary of condensed matter and particle physics. In condensed matter: the Hubbard–Stratonovich transformation decouples four-fermion interactions (like BCS pairing) by introducing a bosonic auxiliary field Δ(x,τ), and the saddle point of the resulting bosonic action recovers the BCS gap equation; fluctuations around the saddle give Goldstone modes and the Ginzburg–Landau effective theory (Module 5.3). In particle physics: the path integral over gauge fields defines QED and the Standard Model (Phase 8), and the Fadeev–Popov procedure handles gauge redundancy.

---

## Self-test (blank page)

1. Write the path-integral expression for ⟨x_f|e^{−iĤT/ℏ}|x_i⟩ and explain why the classical path dominates in the ℏ → 0 limit.
2. Perform a Wick rotation t → −iτ. Show that the quantum partition function Z = Tr e^{−βĤ} becomes a Euclidean functional integral. What boundary conditions do bosonic and fermionic fields obey?
3. Why must Grassmann variables be used in the fermionic path integral? How does the Gaussian Grassmann integral differ in sign from the bosonic case, and what physical principle does this reflect?

---

← Previous: [Module 6.3 — Feynman Diagrams & Perturbation Theory](./module-6.3-feynman-diagrams.md) · [Phase 6 index](./README.md) · Next: [Module 6.5 — Canonical Quantization of Fields](./module-6.5-canonical-quantization.md) →

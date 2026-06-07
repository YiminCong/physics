# Module 6.6 — Renormalization & the Renormalization Group ⭐⭐

> **Phase 6 — [Quantum Field Theory & Many-Body Physics](./README.md)** · Format: Definition → Demonstration → Application

---

## 1. Ultraviolet Divergences, Regularization, and Renormalization

**Definition.** Loop diagrams in QFT involve integrals over all internal momenta k, including arbitrarily large k (short distances). These integrals typically diverge: the electron self-energy in QED, ∫ d⁴k G⁰(k+p) G^{photon}(k), diverges logarithmically in the ultraviolet (UV). This is not a failure of the theory but a symptom of naively using a theory at energy scales beyond its domain of validity. Regularization introduces a parameter that makes the integrals finite: dimensional regularization replaces d⁴k → d^d k with d = 4 − ε (ε → 0 at the end), making divergences appear as poles in 1/ε; a hard momentum cutoff Λ makes them appear as powers of Λ.

Renormalization absorbs divergences into redefinitions of the physical parameters (mass, charge, field normalization). Write the bare Lagrangian parameters (m₀, e₀, φ₀) in terms of renormalized parameters (m, e, φ) plus counterterms δm, δe, δZ chosen order by order in perturbation theory to cancel the 1/ε poles (or Λ-dependences). A theory is renormalizable if only finitely many distinct counterterms are needed — equivalently, if all divergences can be absorbed into the parameters already present in L. QED and the Standard Model are renormalizable; gravity (as a quantum field theory) is not.

**Demonstration.** In QED at one loop, the photon propagator acquires a self-energy correction Π(q²) that is logarithmically divergent. After regularization and renormalization, the physical (renormalized) charge e(μ) depends on the renormalization scale μ: e²(μ) = e²(μ₀)/(1 − (e²(μ₀)/6π²) ln(μ/μ₀) + …). This is the running coupling. As μ increases (shorter distances, higher energies), e(μ) increases — QED is asymptotically free in the IR, with the coupling growing toward a Landau pole at exponentially large energies (well beyond any physical scale). In QCD the sign flips (non-Abelian gauge field), giving asymptotic freedom: e_s(μ) decreases at high μ, justifying perturbation theory at collider energies.

**Application.** After renormalization, QED yields finite, unambiguous predictions at every order in e². The electron anomalous magnetic moment a_e = (g−2)/2 = α/2π − 0.328 α²/π² + … computed to four loops matches experiment at the level of one part in 10¹², making it the most precisely tested prediction in all of science. The procedure is systematic and algorithmic; Peskin & Schroeder "Introduction to Quantum Field Theory" works through it in full detail.

---

## 2. The Renormalization Group and Universality

**Definition.** The renormalization group (RG) is not a group in the strict sense but a semigroup of scale transformations: physical observables must be independent of the arbitrary renormalization scale μ, so μ d/dμ G^{(n)} = 0 gives the Callan–Symanzik equation. The beta function β(g) = μ dg/dμ encodes how a coupling g flows with scale. Fixed points β(g*) = 0 are the universal, scale-invariant theories: free field theory (g* = 0, UV fixed point of asymptotically free theories) and interacting Wilson–Fisher fixed points (in d = 4 − ε dimensions, g* = O(ε)).

Near a fixed point, perturbations grow as (μ/μ₀)^{Δ} where Δ is a critical exponent. Relevant perturbations (Δ > 0) dominate at long distances (IR); irrelevant perturbations (Δ < 0) are suppressed. Only finitely many relevant and marginal operators matter for long-distance physics — this is the deep reason why diverse microscopic models sharing the same relevant operators flow to the same fixed point and therefore exhibit the same critical exponents. This is universality.

**Demonstration.** The Landau–Ginzburg free energy F = ∫ d^d x [½(∇φ)² + ½r φ² + u φ⁴] (Module 2.3) is a QFT in Euclidean space. Running u and r with the RG scale gives the Wilson–Fisher fixed point at u* = ε/6 + O(ε²) in d = 4 − ε. Expanding around the fixed point, the correlation length exponent is ν = ½ + ε/12 + O(ε²) and η = ε²/54 + O(ε³). These are universal — they apply to the liquid-gas critical point, the Ising ferromagnet, the superfluid transition in ⁴He, and any other system in the same universality class (same symmetry, dimension, and number of order-parameter components). The same RG framework applied to the Ginzburg–Landau theory of superconductivity (Module 5.3) gives the exponents for the superconducting phase transition; fluctuation corrections move it away from mean-field values.

**Application.** The RG unifies four apparently unrelated ideas: (i) the removal of UV divergences in QFT, (ii) the emergence of universal critical exponents in statistical mechanics, (iii) the concept of effective field theory (at energy E, integrate out degrees of freedom at scales ≫ E; the result is a renormalized EFT valid below E), and (iv) the running of coupling constants measured at colliders. It explains why QED predictions are finite and precise, why an Ising magnet and a liquid near its critical point have identical exponents, and why the large-scale universe can be described without knowing the details of Planck-scale physics. Altland & Simons Ch. 8 and Coleman "Introduction to Many-Body Physics" Ch. 15–16 give complementary condensed-matter treatments; Peskin & Schroeder Part II gives the QFT treatment.

---

## Self-test (blank page)

1. What is the difference between regularization and renormalization? Give one example of each.
2. Define the beta function β(g). What does β(g) > 0 versus β(g) < 0 imply about the behavior of the coupling at high energies? Give a physical example of each sign.
3. Two systems — a uniaxial ferromagnet and a liquid near its liquid-gas critical point — have the same critical exponents despite completely different microscopic physics. Explain this universality using the language of RG fixed points and relevant operators.

---

← Previous: [Module 6.5 — Canonical Quantization of Fields](./module-6.5-canonical-quantization.md) · [Phase 6 index](./README.md) · Next: [Module 6.7 — Exactly Solvable Models & Long-Range Order](./module-6.7-exactly-solvable-models-and-long-range-order.md) →

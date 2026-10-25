# Project Progress: Distributions in Practice

**Last updated:** 2026-10-25
**Current phase:** Phase 3: Discrete block
**Current step:** Choose next discrete distribution (Poisson or Negative Binomial) and build Section 1

## Completed
- [x] Phase 0: Setup
- [x] Phase 1: Foundations
- [x] Phase 2: Gold-standard notebook (`notebooks/01_binomial.ipynb`)
- [ ] Phase 3: Discrete block (Bernoulli [x], Geometric [x], Poisson [ ], Negative Binomial [ ])
- [ ] Phase 4: Continuous block (Uniform, Normal, Exponential, Gamma, Beta, Log-normal, Weibull)
- [ ] Phase 5: Sampling distributions (Chi-square, t, F)
- [ ] Phase 6: Capstone notebooks
- [ ] Phase 7: Streamlit app
- [ ] Phase 8: Polish and publish

## In progress
- Phase 3: Discrete distribution block (Bernoulli and Geometric finished; Poisson and Negative Binomial remaining)

## Next step
- Select next discrete distribution (recommendation: Poisson for event count rates over time/space, or Negative Binomial to generalize Geometric to r successes)

## Decisions made
- Defined unified visual palette (`PALETTE`) and styling in `utils/plotting.py`.
- Implemented `plot_pmf`, `plot_pdf`, `plot_cdf`, and `plot_sample_vs_theory`.
- Generated 8-section notebook template `notebooks/_template.ipynb`.
- Completed Gold-standard notebook `notebooks/01_binomial.ipynb` covering all 8 sections (QC acceptance sampling applied use case, analytical + numerical MLE, and Poisson approximation).
- Completed Bernoulli notebook `notebooks/02_bernoulli.ipynb` (A/B testing sample size determination use case, binary cross-entropy connection, MLE, and Bernoulli-to-Binomial construction).
- Completed Geometric notebook `notebooks/03_geometric.ipynb` (API retry SLA use case, memoryless property proof, 1/k_bar MLE derivation, and Exponential distribution limit connection).

## Concepts to revisit
- None yet

## Notes / issues
- None

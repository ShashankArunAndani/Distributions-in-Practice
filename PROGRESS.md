# Project Progress: Distributions in Practice

**Last updated:** 2026-10-25
**Current phase:** Phase 4: Continuous block
**Current step:** Build Section 1 (Intuition & Motivation) for Normal distribution

## Completed
- [x] Phase 0: Setup
- [x] Phase 1: Foundations
- [x] Phase 2: Gold-standard notebook (`notebooks/01_binomial.ipynb`)
- [x] Phase 3: Discrete block (Bernoulli, Geometric, Poisson, Negative Binomial)
- [ ] Phase 4: Continuous block (Uniform [x], Normal [ ], Exponential [ ], Gamma [ ], Beta [ ], Log-normal [ ], Weibull [ ])
- [ ] Phase 5: Sampling distributions (Chi-square, t, F)
- [ ] Phase 6: Capstone notebooks
- [ ] Phase 7: Streamlit app
- [ ] Phase 8: Polish and publish

## In progress
- Phase 4: Continuous distribution block (Uniform finished; Normal, Exponential, Gamma, Beta, Log-normal, Weibull remaining)

## Next step
- Build `notebooks/07_normal.ipynb` (the central pillar of continuous probability)

## Decisions made
- Defined unified visual palette (`PALETTE`) and styling in `utils/plotting.py`.
- Implemented `plot_pmf`, `plot_pdf`, `plot_cdf`, and `plot_sample_vs_theory`.
- Generated 8-section notebook template `notebooks/_template.ipynb`.
- Completed Gold-standard notebook `notebooks/01_binomial.ipynb` covering all 8 sections (QC acceptance sampling applied use case, analytical + numerical MLE, and Poisson approximation).
- Completed Bernoulli notebook `notebooks/02_bernoulli.ipynb` (A/B testing sample size determination use case, binary cross-entropy connection, MLE, and Bernoulli-to-Binomial construction).
- Completed Geometric notebook `notebooks/03_geometric.ipynb` (API retry SLA use case, memoryless property proof, 1/k_bar MLE derivation, and Exponential distribution limit connection).
- Completed Poisson notebook `notebooks/04_poisson.ipynb` (cloud server capacity/DDoS alerting use case, dual mean-variance LLN convergence, analytical + numerical MLE, and Normal approximation).
- Completed Negative Binomial notebook `notebooks/05_negative_binomial.ipynb` (customer purchase overdispersion use case, 2D MLE surface optimization, and Poisson convergence limit).
- Completed Continuous Uniform notebook `notebooks/06_uniform.ipynb` (digital quantization noise Bennett's model, German Tank Problem MVUE, and Inverse Transform Sampling).

## Concepts to revisit
- None yet

## Notes / issues
- None

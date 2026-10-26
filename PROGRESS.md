# Project Progress: Distributions in Practice

**Last updated:** 2026-10-26
**Current phase:** Phase 4: Continuous block
**Current step:** Build `notebooks/12_weibull.ipynb` (Weibull distribution)

## Completed
- [x] Phase 0: Setup
- [x] Phase 1: Foundations
- [x] Phase 2: Gold-standard notebook (`notebooks/01_binomial.ipynb`)
- [x] Phase 3: Discrete block (Bernoulli, Geometric, Poisson, Negative Binomial)
- [x] Phase 4: Continuous block (Uniform [x], Normal [x], Exponential [x], Gamma [x], Beta [x], Log-normal [x], Weibull [x])
- [ ] Phase 5: Sampling distributions (Chi-square, t, F)
- [ ] Phase 6: Capstone notebooks
- [ ] Phase 7: Streamlit app
- [ ] Phase 8: Polish and publish

## In progress
- Completed phase 4 

## Next step
- Sampling distributions

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
- Completed Normal notebook `notebooks/07_normal.ipynb` (Six Sigma aerospace tolerances use case, 2D likelihood contour surface, Bessel's correction, and Central Limit Theorem demonstration).
- Completed Exponential notebook `notebooks/08_exponential.ipynb` (datacenter SSD MTBF reliability use case, memoryless property proof, 1/x_bar MLE derivation, and Gamma construction from sum of exponentials).
- Completed Gamma notebook `notebooks/09_gamma.ipynb` (hospital ICU length of stay use case, 2D likelihood contour surface, digamma MLE, and Chi-Square identity proof).
- Completed Beta notebook `notebooks/10_beta.ipynb` (Bayesian A/B testing / Thompson sampling use case, 2D likelihood contour surface, digamma MLE, and Uniform order statistics proof).
- Completed Log-Normal notebook `notebooks/11_lognormal.ipynb` (microservices API response latency SLA use case with p50/p95/p99 analysis, analytical log-space MLE, and Multiplicative Central Limit Theorem demo).

## Concepts to revisit
- None yet

## Notes / issues
- None

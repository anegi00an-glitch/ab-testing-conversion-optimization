# A/B Testing & Conversion Optimization

## Business objective

Evaluate whether a simulated product change improves conversion and demonstrate a defensible experimentation workflow.

## Dataset provenance

The starting conversion dataset is a public conversion dataset. The portfolio experiment is explicitly treated as **simulated**; the experiment design, statistical analysis, validation, and recommendations are independent portfolio work.

**Source reference:** https://github.com/jainds/eda-for-conversion-rate-dataset

## Result snapshot

The supplied simulated sample contains **6,033 control users** and **5,967 treatment users**. Both groups contain **559 converters**, producing conversion rates of approximately **9.27%** and **9.37%**. The analysis in `notebooks/ab_test_analysis.py` tests whether this small observed difference is statistically meaningful.

## Questions

- Is treatment conversion higher than control?
- What are the absolute and relative lifts?
- Is the observed difference statistically significant?
- What additional checks should be completed before a real product rollout?

## Dashboard

See [`dashboard/README.md`](dashboard/README.md) for the executive experiment dashboard specification.

## Stack

Python · Statistics · SQL · Power BI

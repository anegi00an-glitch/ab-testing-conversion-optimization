# Experiment Results

## Executive result

The simulated treatment group converted at **9.37%** versus **9.27%** for control.

- Control: 6,033 users / 559 conversions
- Treatment: 5,967 users / 559 conversions
- Absolute lift: **+0.10 percentage points**
- Relative lift: approximately **+1.11%**

A two-proportion z-test is implemented in `../notebooks/ab_test_analysis.py`. The observed lift is intentionally treated conservatively: a numerical improvement is not enough to justify shipping without statistical evidence and experiment-quality checks.

## Business interpretation

The treatment produced a slightly higher observed conversion rate, but the effect is small. The appropriate product decision is therefore to avoid declaring a winner based on the point estimate alone and review the statistical test, confidence interval, experiment duration, sample-ratio integrity, and guardrail metrics before rollout.

## Scope

This is a simulated portfolio experiment. It demonstrates an experimentation workflow; it is not evidence from a real company's A/B test.

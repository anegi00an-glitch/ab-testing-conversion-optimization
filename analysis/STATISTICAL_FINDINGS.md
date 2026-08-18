# Statistical Findings

## Primary question

**Did the simulated treatment increase conversion relative to control?**

### Primary metric

Conversion rate = converted users / assigned users.

| Group | Users | Conversions | Conversion rate |
|---|---:|---:|---:|
| Control | 6,033 | 559 | 9.27% |
| Treatment | 5,967 | 559 | 9.37% |

### Effect size

- Absolute lift: **+0.10 percentage points**
- Relative lift: **+1.11%**

### Experiment balance

The two groups are close in size (6,033 vs 5,967), so the allocation is approximately balanced at the descriptive level.

## Segment findings

### Device

- Desktop: **10.65%**
- Mobile: **8.67%**
- Tablet: **8.62%**

Desktop converts about 2 percentage points higher than mobile/tablet in this sample. This is a stronger descriptive difference than the overall treatment-control lift and is therefore a useful product investigation area.

### Acquisition channel

- Email: **11.50%**
- Ads: **10.10%**
- SEO: **9.22%**
- Social: **8.41%**

Email is the strongest observed channel while Social is the weakest. These are descriptive differences, not causal channel effects.

### Country

Country-level conversion is tightly clustered around 9.2–9.4%, so there is little evidence of a large geographic gap in the descriptive sample.

## What the experiment actually tells us

The treatment has a slightly higher point estimate, but the observed lift is only **0.10 percentage points**. A responsible decision should therefore depend on the statistical test and confidence interval, not the point estimate alone.

The strongest practical signal in the exploratory analysis is **device performance**, followed by acquisition-channel differences. These should be treated as hypotheses for follow-up analysis rather than proof of causal drivers.

## Decision framework

**Do not declare a treatment winner from the point estimate alone.** Before rollout, review:

1. Two-proportion significance test and confidence interval.
2. Sample-ratio mismatch / assignment integrity.
3. Experiment duration and exposure consistency.
4. Guardrail metrics such as revenue per user, bounce/engagement, and technical errors.
5. Pre-specified segment checks to avoid post-hoc cherry-picking.

## Portfolio boundary

This is a simulated experiment created for portfolio practice. The dataset is public; the experiment framing, analysis, statistical workflow, visualizations, and recommendations are independent portfolio work.

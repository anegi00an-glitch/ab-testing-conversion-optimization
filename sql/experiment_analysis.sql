-- A/B testing analysis for the simulated experiment

WITH experiment AS (
    SELECT
        experiment_group,
        COUNT(DISTINCT user_id) AS users,
        COUNT(DISTINCT CASE WHEN converted = 1 THEN user_id END) AS converters
    FROM conversion_events
    GROUP BY experiment_group
)
SELECT
    experiment_group,
    users,
    converters,
    ROUND(100.0 * converters / NULLIF(users, 0), 2) AS conversion_rate_pct
FROM experiment
ORDER BY experiment_group;

-- Segment-level diagnostic view
SELECT
    country,
    device,
    channel,
    experiment_group,
    COUNT(DISTINCT user_id) AS users,
    COUNT(DISTINCT CASE WHEN converted = 1 THEN user_id END) AS converters,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN converted = 1 THEN user_id END)
        / NULLIF(COUNT(DISTINCT user_id), 0),
        2
    ) AS conversion_rate_pct
FROM conversion_events
GROUP BY country, device, channel, experiment_group
HAVING COUNT(DISTINCT user_id) >= 50
ORDER BY country, device, channel, experiment_group;

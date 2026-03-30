-- Step: Sessionize web traffic and link to successful conversions
WITH user_journey AS (
    SELECT 
        u.user_id,
        t.channel,
        t.timestamp AS touchpoint_time,
        s.created_at AS conversion_time,
        -- Rank touches per user leading up to conversion
        ROW_NUMBER() OVER(PARTITION BY u.user_id ORDER BY t.timestamp ASC) as touch_rank_asc,
        ROW_NUMBER() OVER(PARTITION BY u.user_id ORDER BY t.timestamp DESC) as touch_rank_desc
    FROM `replit.web_traffic` t
    JOIN `replit.users` u ON t.anonymous_id = u.anonymous_id
    JOIN `replit.subscriptions` s ON u.user_id = s.user_id
    WHERE t.timestamp <= s.created_at
)
SELECT 
    channel,
    -- First Touch: Credit goes to the first interaction
    COUNT(CASE WHEN touch_rank_asc = 1 THEN 1 END) AS first_touch_conversions,
    -- Last Touch: Credit goes to the final interaction before paying
    COUNT(CASE WHEN touch_rank_desc = 1 THEN 1 END) AS last_touch_conversions
FROM user_journey
GROUP BY 1;

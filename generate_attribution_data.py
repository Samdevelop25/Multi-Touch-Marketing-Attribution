import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_attribution_data(n_users=2000):
    np.random.seed(42)
    channels = ['Google Search', 'Twitter/X', 'YouTube Tutorial', 'Direct', 'Reddit']
    traffic_records = []
    conversion_records = []

    for i in range(n_users):
        # Simulate 1-4 touches before a potential conversion
        n_touches = np.random.randint(1, 5)
        base_date = datetime(2026, 1, 1)
        
        user_touches = []
        for t in range(n_touches):
            touch_time = base_date + timedelta(days=np.random.randint(0, 30), hours=np.random.randint(0, 24))
            channel = np.random.choice(channels, p=[0.3, 0.2, 0.25, 0.15, 0.1])
            traffic_records.append({'user_id': i, 'channel': channel, 'timestamp': touch_time})
            user_touches.append({'channel': channel, 'timestamp': touch_time})
        
        # Logic: If they touched a 'YouTube Tutorial', they are 60% likely to convert
        has_youtube = any(touch['channel'] == 'YouTube Tutorial' for touch in user_touches)
        conv_prob = 0.6 if has_youtube else 0.1
        
        if np.random.random() < conv_prob:
            last_touch = max(user_touches, key=lambda x: x['timestamp'])
            conv_time = last_touch['timestamp'] + timedelta(hours=np.random.randint(1, 48))
            conversion_records.append({
                'user_id': i, 
                'conversion_time': conv_time, 
                'revenue': 20.00 # Replit Core price
            })

    pd.DataFrame(traffic_records).to_csv('data/web_traffic.csv', index=False)
    pd.DataFrame(conversion_records).to_csv('data/conversions.csv', index=False)
    print("Attribution data generated in /data folder.")

if __name__ == "__main__":
    generate_attribution_data()

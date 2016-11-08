import os
import json
from watson_developer_cloud.personality_insights_v3 import PersonalityInsightsV3 as PI


personality_insights = PI(
    version = '2016-10-20',
    username = os.environ['BIG5_USER'],
    password = os.environ['BIG5_PW']
)

with open('sample.json') as profile_json:
    profile = personality_insights.profile(
        profile_json.read(), 
        content_type = 'application/json',
        raw_scores=True,
        consumption_preferences=True)

print(json.dumps(profile,indent=2))
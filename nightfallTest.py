
# import os

from nightfall import Confidence, DetectionRule, Detector, LogicalOp, Nightfall

# nightfall = Nightfall(os.environ['NIGHTFALL_API_KEY'])

with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

nightfall = Nightfall(api_key)

detection_rule_uuid = '9a134234-d8e1-43b5-b861-ddbfa5f84097'

payload = [
    "My credit card number is 4916-6734-7572-5015"
]

result, _ = nightfall.scan_text(
        payload,
        detection_rule_uuids=[detection_rule_uuid]
    )

print(result)
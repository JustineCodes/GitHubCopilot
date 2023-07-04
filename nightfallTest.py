
import os

from nightfall import Confidence, DetectionRule, Detector, LogicalOp, Nightfall

# nightfall = Nightfall(os.environ['NIGHTFALL_API_KEY'])

with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

nightfall = Nightfall(api_key)

detection_rule_uuid = ('f3ffa560-4565-4555-bdc8-3dc42fb6ea0f')

payload = [
    "The customer social security number is 458-02-6124",
    "No PII in this string",
    "My credit card number is 4916-6734-7572-5015"
]

result, _ = nightfall.scan_text(
        payload,
        detection_rule_uuids=[detection_rule_uuid]
    )
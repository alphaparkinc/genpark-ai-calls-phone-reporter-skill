from client import AiCallsPhoneReporterClient
client = AiCallsPhoneReporterClient()
result = client.simulate_call("Downtown Dental Clinic", ["opening_hours", "accepts_insurance", "new_patients_welcome"])
print(f"AI disclosed: {result['ai_disclosed']}")
for field, value in result['call_summary']['data'].items():
    print(f"  {field}: {value}")

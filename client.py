class AiCallsPhoneReporterClient:
    def simulate_call(self, business_name: str, query_fields: list) -> dict:
        collected = {field: f"[Collected via AI call: {field} for {business_name}]" for field in query_fields}
        return {
            "call_summary": {"business": business_name, "data": collected},
            "ai_disclosed": True
        }

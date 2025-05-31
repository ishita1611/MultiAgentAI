import json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, json_input):
        # Assume json_input is a dict (already parsed JSON)
        required_fields = ["id", "date", "customer", "items", "total_amount"]
        missing_fields = [f for f in required_fields if f not in json_input]

        result = {
            "valid": len(missing_fields) == 0,
            "missing_fields": missing_fields,
            "formatted_data": {}
        }

        if not result["valid"]:
            print(f"⚠️ JSON Agent Warning: Missing fields {missing_fields}")
            return result

        # Example: reformat to your target schema
        formatted = {
            "invoice_id": json_input["id"],
            "invoice_date": json_input["date"],
            "customer_name": json_input["customer"],
            "line_items": json_input["items"],
            "total": json_input["total_amount"]
        }

        result["formatted_data"] = formatted

        # Save to shared memory for traceability
        self.memory.log("json_data", formatted)

        print(f"📄 JSON AGENT SAYS: {formatted}")

        return result

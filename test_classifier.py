from agents.classifier_agent import ClassifierAgent

email_input = """
Subject: Request for Quotation  
Hi team,  
Please send me a quote for the following products...
"""

json_input = {
    "type": "invoice",
    "amount": 1200,
    "customer": "Queen I"
}

classifier = ClassifierAgent()

print("\nTesting Email:")
classifier.process(email_input, source_id="email-queen")

print("\nTesting JSON:")
classifier.process(json_input, source_id="json-queen")


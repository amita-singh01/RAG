from services.rag_service import answer_question

query = (
    "My neighbour occupied my land and is not vacating it."
)

result = answer_question(query)

print("Detected Type:")
print(result["case_type"])

print("\nAnswer:")
print(result["answer"])
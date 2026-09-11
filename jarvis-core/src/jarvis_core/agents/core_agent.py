from langchain_nvidia_ai_endpoints import ChatNVIDIA

API_KEY = ""

client = ChatNVIDIA(
    model="google/gemma-4-31b-it",
    api_key=API_KEY,
    temperature=0.5,

    top_p=1,

    max_completion_tokens=1024,
)

lc_messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "What is 17 * 23?",
    },
]

response = client.invoke(lc_messages)
if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
    print(response.additional_kwargs["reasoning_content"])
print(response.content)
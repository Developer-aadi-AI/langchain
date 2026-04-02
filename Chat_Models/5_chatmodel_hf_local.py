from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace


llm = HuggingFacePipeline(model_id="mistralai/Mistral-7B-Instruct-v0.2",
                          task = "text-generation",pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100))

model = ChatHuggingFace(llm)

result = model.invoke("What is the capital of India?")

print(result.content)
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

base_url = "http://localhost:11434"
model = "llama3.2"

llm = ChatOllama(
    base_url=base_url,
    model=model,
    temperature=0.2,
    num_predict=500
)

class Review(BaseModel):

    key_themes : list[str] = Field(description = "Write down all the key themes discussed in the Review in a list")
    summary : str = Field(description="Generate a summary of 30 words.") 
    sentiment : Literal["Positive", "Negative", "Neutral"] = Field(description="Return sentiment of the review")
    pros : Optional[list[str]] = Field(default=None,description= "write the pros inside a list")
    cons : Optional[list[str]] = Field(default=None,description= "write the cons inside a list")

model = llm.with_structured_output(Review)

result = model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                      
The S-Pen integration is a great touch for note-taking and quick sketches though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality. 
                      
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
                      
Pros:
Insanely powerful processor (great for gaming and productivity)
tunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UT
Expensive compared to competitor""")

print(result.key_themes)
print(result.summary)
print(result.pros)
print(result.cons)
print(result.sentiment)
print("-----------------")
print(result)
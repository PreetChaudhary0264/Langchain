from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):
    # summary:str
    summary:str = Field(description="A brief summary of the review")
    sentiment:Literal["pos","neg"] = Field(description="Return sentiment of the review either negative or positive or neutral")

    pros:Optional[list[str]] = Field(default=None, description="write down all the pros in a list")
    key_themes:list[str] = Field(description="write all the key themes discussed in the review in a list")
    
#with_structured_output will only work for openAI or anthropic

structuredOutput = model.with_structured_output(Review)

result = structuredOutput.invoke("the hardware is great but the software feels bolated.there are too many preinstalled apps that i cant remove.hoping for a software update to fix this...")
print(result)
print(result.name)
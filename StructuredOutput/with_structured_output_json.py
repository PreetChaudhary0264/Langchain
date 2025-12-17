from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI()
//oh no
#schema
json_schema = {
    "title":"Review",
    "type":"object",
    "properties":{
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":"Write down all the key themes"
        },
        "summary":{
            "type":"string",
            "description":"A brief summary of the review"
        },
        "sentiment":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Return sentiment of the review either positive or negative"
        },
         "pros":{
             "type":["array","null"],
             "items":{
                "type":"string"
             },
             "description":"Write down all the pros inside a list"
         }
    }
}

    
#with_structured_output will only work for openAI or anthropic

structuredOutput = model.with_structured_output(json_schema)

result = structuredOutput.invoke("the hardware is great but the software feels bolated.there are too many preinstalled apps that i cant remove.hoping for a software update to fix this...")
print(result)
print(result.name)

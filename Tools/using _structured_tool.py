from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True,description="The first number to add")
    b: int = Field(required=True,description="The Second number to add")
    
def multiply(a,b):
    return a + b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a":3,"b":4})
print(result)
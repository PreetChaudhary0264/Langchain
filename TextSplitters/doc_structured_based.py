from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
     
     def greet_user(name):
    print(f"Hello, {name}! Welcome to the dummy program.")

def add_numbers(a, b):
    return a + b

def main():
    greet_user("Preet")
    x = 10
    y = 20
    result = add_numbers(x, y)
    print(f"The sum of {x} and {y} is {result}")
    
    for i in range(3):
        print(f"Loop iteration {i+1}")

if __name__ == "__main__":
    main()

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(len(result))
print(result)
import ollama
import transformers
def merge(obj1:str,obj2:str)->str:
    """generate a real life object by merging obj1 and obj2"""
    pass
answer = ollama.chat("llama3.2",tools=[merge],messages=[{"role":"user","content":"merge a diamond and an emerald"}])
print(answer)


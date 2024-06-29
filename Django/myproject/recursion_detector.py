Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import ast
... 
... class RecursionDetector(ast.NodeVisitor):
...     def __init__(self):
...         self.functions = {}
...         self.recursive_calls = []
... 
...     def visit_FunctionDef(self, node):
...         self.functions[node.name] = node
...         self.generic_visit(node)
... 
...     def visit_Call(self, node):
...         if isinstance(node.func, ast.Name):
...             function_name = node.func.id
...             if function_name in self.functions:
...                 if self.functions[function_name] is node:
...                     self.recursive_calls.append(function_name)
...         self.generic_visit(node)
... 
... def find_recursive_functions(source_code):
...     tree = ast.parse(source_code)
...     detector = RecursionDetector()
...     detector.visit(tree)
...     return detector.recursive_calls

# 示例用法
if __name__ == "__main__":
    with open('your_django_view_file.py', 'r') as file:
        source_code = file.read()
    
    recursive_functions = find_recursive_functions(source_code)
    print(f"Recursive functions detected: {recursive_functions}")

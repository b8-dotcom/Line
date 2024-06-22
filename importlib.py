import importlib

# 假設模塊名為 your_projec_line.settings
module_name = 'your_projec_line.settings'

# 使用 importlib.reload 重新加載模塊
try:
    module = importlib.import_module(module_name)
    importlib.reload(module)
    print(f"Successfully reloaded module '{module_name}'")
except ModuleNotFoundError:
    print(f"Module '{module_name}' not found")
except Exception as e:
    print(f"Failed to reload module '{module_name}': {e}")

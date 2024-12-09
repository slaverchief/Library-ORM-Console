import os
import pkgutil


modules = [name for _, name, _ in pkgutil.iter_modules([os.path.dirname(__file__)])]

for module_name in modules:
    exec(f"from .{module_name} import *")
import os
import shareData
import sys
# os.environ["TESTE"] = "DEBUG" # não funcionou
# shareData.CreateData("TESTE", "DEBUG") # funcionou 😎

print(sys.argv)
print(os.environ)
print(os.environ["ENVIRONMENT_VARIABLE_NAME"])
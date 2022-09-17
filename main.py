import os
import shareData
import sys
from dotenv import load_dotenv
from pathlib import Path

path = os.environ["GITHUB_ENV"]
dotenv_path = Path(path)
load_dotenv(dotenv_path=dotenv_path)
# os.environ["TESTE"] = "DEBUG" # não funcionou
# shareData.CreateData("TESTE", "DEBUG") # funcionou 😎

# print(sys.argv)
print(os.environ)
# print(os.environ["MINHA_CHAVE"])
# print("-",os.environ["JESSE"])
# print(os.environ["ENV"])


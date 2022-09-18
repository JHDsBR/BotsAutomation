import loadEnv 

import os
import shareData
import sys
import Notify

Notify.SendEmail("TESTE", "1234")

# os.environ["TESTE"] = "DEBUG" # não funcionou
# shareData.CreateData("TESTE", "DEBUG") # funcionou 😎

# print(sys.argv)
# print(os.environ)
# print(os.environ["MINHA_CHAVE"])
# print("-",os.environ["JESSE"])
# print(os.environ["ENV"])


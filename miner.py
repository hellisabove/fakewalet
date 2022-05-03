import string
import colorama
from colorama import *
import random
import time

def main():
    address=input("Enter your Bitcoin address: ")
    print("OK")
    characters=string.ascii_lowercase+string.digits
    for _ in range(100000):
        print(Fore.RED + "> %s | 0.00000 BTC" % "".join(random.sample(characters,32)))
    time.sleep(0.5)
    print(Fore.GREEN + "> %s | 1.23838 BTC" % "".join(random.sample(characters,32)))
    time.sleep(0.5)
    print(Fore.WHITE + "> Attempting to transfer to your wallet...")
    time.sleep(3)
    print(Fore.WHITE + "> Done transfering BTC to wallet!")
main()

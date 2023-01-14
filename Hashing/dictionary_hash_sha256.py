import hashlib
import time

counter = 1

sha256_hash = input("SHA 256 Hash : ")
pwdfile = input('Wordlist Path (example "E:\wordlist.dic") : ')

try:
    pwdfile = open(pwdfile,"r",errors="ignore")
except:
    print("\nFile not found!")
    quit()

start = time.time()
for password in pwdfile:
    sha256 = hashlib.sha256()
    sha256.update(password.strip().encode('utf-8'))
    print("Try Password %d: %s" % (counter, password.strip()))

    counter += 1

    if sha256_hash.strip() == sha256.hexdigest():
        print("\nPassword found!")
        print("Password is : %s" % password.strip())
        print("Total Time  : %.1f" % total_time, "second.")
        time.sleep(10)
        break
    else:
        print("\nPassword not found T-T")

    end = time.time()
    total_time = end - start
import requests
import hashlib
import os
import sys

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA' #requires first 5 of sha1 hash
'''
k anonimity
use first 5 vals of sha1 hash
res is a list of all passwords with those first 5 values
'''
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char #requires first 5 of sha1 hash
    res = requests.get(url) #400 means not authorized
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check API and try again")
    return res

def read_res(res):
    print(res.text) #returns a text of all passwords that match first 5,  and their respective counts
    
def get_pass_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count    
    return 0
'''
Check password if it exists in API response
pwd: actual password
'''
def pwned_api_check(pwd):
    sha1pd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pd[:5], sha1pd[5:]
    res = request_api_data(first5_char)
    return get_pass_count(res, tail)

def check_pass():
    while True:
        pwd = input("Please enter the password you'd like to check: ")
        if os.name != 'nt':
            print("\x1B[F\x1B[2K", end="") #clears the previous line in the terminal
        
        count = pwned_api_check(pwd)
        if count:
            print(f"Your password was found {count} times")
        else:
            print("Your password is secure!")
        pwd = input('Check another password? y/n...')
        if pwd == 'n':
            break
    return 'Thanks for your time!'
            

def main():
    print(check_pass())
    
if __name__ == '__main__':
    sys.exit(main())
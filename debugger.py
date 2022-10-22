def dec2bin(number: int):
    ans = ""
    if ( number == 0 ):
        return 0
    while ( number ):
        ans += str(number&1)
        number = number >> 1
     
    ans = ans[::-1]
 
    return ans
 
 
def main():
    number = 60
    print(f"The binary of the number {number} is {dec2bin(number)}")
 
 
# driver code
if __name__ == "__main__":
    main()

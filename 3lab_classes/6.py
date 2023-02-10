nums=[int(a) for a in input().split()]
primes=[]
class Prime():
    def prime(self,nums):
        for num in nums:
            bool=True
            for i in range(2,num-1):
                if num%i==0:
                    bool=False
                    break
            if bool==True and num!=1:
                primes.append(num)
        return primes

cn=Prime()
print(cn.prime(nums))
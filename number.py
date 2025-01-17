class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value %2 !=0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value %2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        if self < 2:
            return False
        for i in range(2, int(self ** 0.5) + 1):
            if self % i == 0:
                return False
        return True
        
    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divs = []
        for i in range(1, self +1):
            if self % i == 0:
                divs.append(i)
            return divs

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        digits = str(self.value)
        sum = 0
        for i in digits:
            sum += int(i)
        return sum


    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        # d = self.get_digits()
        # n = len(d)
        # if n%2==0:
        #     return d[:n//2] == d[n//2:,-1]
        # else:
        #     return d[:n//2-1] == d[n//2+1:,-1]

        return str(self.value) == str(self.value)[::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return self.get_digits()[::-1] 

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.value)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.value)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [min(map(int,str(self.value))), max(map(int,str(self.value)))]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        
    

# Create a new instance of Number
number = Number(3)

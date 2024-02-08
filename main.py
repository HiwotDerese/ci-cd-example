def main():
    

    def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number
    # print("Hello, " + name + "Docker is running")
    number = input("Please enter a number: ")
    print(fizzbuzz(int(number)))

if __name__ == "__main__":
    main()
    
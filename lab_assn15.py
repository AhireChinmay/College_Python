def main():
    s = input("\n Enter string: ")
    while (1):
        print("\n1.Length \n2.Reverse \n3.Equality \nt.Check palindrome \ns.Check Substring") 
        choice=int(input("Enter your choise: "))

    if choice == 1:
        print(f"Length of string is: {len(s)}")
    elif choice == 2:
        print("Reverse string is ", s[::-1])
    elif choice == 3:
        s2= input("\nEnter string to compare :")
        if s == s2:
            print("\nstrings are equal")
        else:
            print("\nstrings are not equal")
    elif choice==4:
        if s == s[::-1]:
            print("\nits a palindrome string") 
    elif choice==5:
        s2=input("\nEnter substring to check:\n")
        if s2 in s:
            print("substring is present")
        else:
            print("\nSubstring is absent")
    else:
        print("Invalid choice")
if __name__ =='__main__':
    main()

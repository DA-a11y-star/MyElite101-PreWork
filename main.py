def main():
  print("Welcom to the Elite 101 Chatbot!")
  name = input("Please enter your name: ")
  age = int(input(f'Nice to meet you, {name}! How old are you? '))
  if age <= 27:
    print(f'Welcome {name}! Oh, to be {age} again! How can I help you today?')
  elif age >= 27 and age <=50:
    print(f'Welcome {name}! {age} some of the best years of life! How can I help you?')
  else: 
    print(f'Welcome {name}! {age} a very wise age! How can I help you?')
  print("""
1. Get Your Drivers Discence Issued
2. Get Your Permit
3. Talk to Customer Service
4. Exit the Conversation""")
  response1 = int(input("Enter the number of your choice: "))
  if response1 == 1:
    test = input("Have you taken your test yet: ")
  elif response1 == 1:
    course = input("Have you bought the Drivers Ed course: ")
  elif response1 == 1:
    print("Unfortunately Customer Service is unavailable today.")
  print(f"Have a wonderful rest of your day and come back again sometime!")

if __name__ == "__main__":
    main()
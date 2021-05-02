numbers = input().split()
answers = input().split()

print(all(num in set(numbers) for num in set(answers)) and all(num in set(answers) for num in set(numbers)))

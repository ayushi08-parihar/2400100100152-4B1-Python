#Write a Python program that prints numbers from 1 to 30, but skips numbers divisible by 3 using the continue statement.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i ,end="   ")    
nvows, ncons = 0, 0
message = "Super"
for ch in message:
    if ch in "aeiou":
        print(ch, "is a vowel.")
        nvows += 1
    else:
        print(ch, "is a consonant.")
        ncons += 1
print("%d vowels and %d consonants." % (nvows, ncons)) 

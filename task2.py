# job eligibility portal

print(" 🚀 WELCOME TO OUR ELIGIBILITY PORTAL! 🚀 ".center(60, "#"))
print("Please answer the following questions:")
goodAtPython = input("Are you good at python? (y/n) 🐍\n> ") in ("y","true", "yes", "oui")
yearsOfExperience = int(input("How many years of experience? "))
haveCertificate = input("Do you have a university certificate\n(or at least participated in a programming bootcamp) ? (y/n) 🎓\n>") in ("y","true", "yes", "oui")
if haveCertificate or yearsOfExperience >= 2:
    isAccepted = True # for future compatability
    print("🎉 CONGRATULATIONS! You've been accepted for the next phase!\nYour qualifications meet the requirements.")
else:
    isAccepted = False
    print("😢 Sorry, your current qualifications don't match the job requirements.\nTry improving your skills or gaining more experience!")

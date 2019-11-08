
hex = "0123456789abcdef"
modhex = "cbdefghijklnrtuv"

OTP = "ikgdijihfrtnvjddjlgcbgthriicgdkf"
translated = ""

for x in range(len(OTP)):
    translated = translated + hex[modhex.find(OTP[x])]

print(translated)

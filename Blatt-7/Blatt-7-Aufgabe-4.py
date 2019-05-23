

hex = "0123456789abcdef"
modhex = "cbdefghijklnrtuv"

OTP = "ifetelhljgejlrrjggnijdgukkevitkc"
translated = ""

for x in range(len(OTP)):
    translated = translated + hex[modhex.find(OTP[x])]

print(translated)

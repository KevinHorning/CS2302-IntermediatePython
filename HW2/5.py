#7.21

def safeInput():
    try:
        input()
    except KeyboardInterrupt:
        safeInput()

safeInput()

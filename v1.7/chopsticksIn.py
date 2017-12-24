# speech input from user
import speech_recognition as sr

def getIn():
    numbers = "zero one two three four five six seven eight nine".split(" ")
    # get audio from the microphone
    r = sr.Recognizer()
    res = []
    with sr.Microphone() as source:
        while True:# breaks on good input
            res = []
            print("Speak:")
            try:
                audio = r.listen(source, timeout = 0.5)
                try:
                    out = r.recognize_google(audio).lower()
                    print("You said " + out)

                    for string in out.split(" "):
                        try:
                            res.append(int(string))
                        except:
                            if string in numbers:
                                res.append(numbers.index(string))

                    if len(res) == 2:
                        if "hit" in out:
                            return [res, "hit"]
                        elif "switch" in out or "split" in out:
                            return [res, "switch"]

                    elif len(res) == 4:
                        return [res, "absolute"]

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))


            except sr.WaitTimeoutError:
                print("hurry up man")

    print(res)


def parseGetIn(state, mod=5):
    res = [[-1, -1, -1, -1], "na"]
    while res[0] == [-1, -1, -1, -1]:
        inputPrompt()
        res = getIn()
        print("CHECKING")
        if res[1] == "hit":
            for i in range(0, 2):
                for j in range(2, 4):
                    if res[0][0] == state[i]:
                        if res[0][1] == state[j]:
                            res[0] = state[:]
                            res[0][j] = (state[i] + state[j]) % mod
        elif res[1] == "switch":
            res[0] = [res[0][0], res[0][1], state[2], state[3]]

    return res[0]

def inputPrompt():
    print("Please tell me your move")
    print("You have 3 options for input")
    print("1. say [switch to] then your hands new arrangement")
    print("2. say hand [hits] hand to have that happen")
    print("3. say [change to] and then the new 4 hands")

# print("1")
# parseGetIn([1,1,1,1])
# print("2")
# parseGetIn([2,2,2,3])

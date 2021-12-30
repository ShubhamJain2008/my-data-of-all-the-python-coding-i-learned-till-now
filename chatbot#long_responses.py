import random

R_EATING = "I don't like eating anything because I'm a bot !"
R_ADVICE = "If I were you, I would like to become a resource for my nation!"
R_BDayReminder = "Your birthday will be on 29 decemebr"
R_rps = "yeah sure but not now"



def unknown():
    response = ["I don't understand.(its unrelated) ",
                "pls write proper text",
                "Sounds about right.",
                "pls add the response in long_responses.py cause i m not made with machine learning ai or deep learning"][
        random.randrange(4)]
    return response

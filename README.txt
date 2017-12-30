This is a project where we attempt to make a cool chopsticks player

Outline:

v0.0 - most basic possible player playing against player or computer. Records all player moves.

v1.0 - Records player moves. Windows only open picture, breaks on other os.
v1.1 - i/o from voice and microphone. Incredibly Windows only breaks on other os.
v1.2 - brokenish tkinter attempt
v1.3 - cross platform speech, and pictures.

v2.0 - genetic strategy updating (no graphics or audio)
v2.1 - genetic seeded with human data
v2.2 - recursion delver
v2.3 - genetic facing recursion delver
v2.4 - my own speech
v2.5 - my own speech recognition
v2.6 - explore hyper parameters for genetic with grid search or something

v3.0 - mod n

v4.0 - genetic mod n

v5.0 - suicide option

v6.0 - preservation option

v7.0 - pip installable program with basic features and a good AI
v7.1 - pip installable with ALL features

Conventions:


A state is an array with
state = [ player_hand1, player_hand2, enemy_hand1, enemy_hand2 ]
Note different players will observe this differently



It would be nice if we had a representation of states that did not have an "order" to it
1 1 2 0 is identical to 1 1 0 2
but it is hard to see this as it stands

- first just build a function that checks equality not by == but non discriminant like this


Specific problems:

Better nextMove function
validMove is flawed, fix it the next time you notice
Add my speech recognition and cooler speaking with NNs
better strategy

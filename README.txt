This is a project where we attempt to make a cool chopsticks player

Outline:
v0 - most basic possible player playing against palyer or computer
v1 - basic player strategy copying
v1.5 - v1 with i/o from voice and microphone
v1.8 - cross platform speech, no pictures though
v2 - genetic strategy updating

v3 - v1.5 with mod n
v4 - genetic mod n

v5 - suicide option
v6 - preservation option

v7 - online option (Django/Flask)

Conventions:


A state is an array with
state = [ player_hand1, player_hand2, enemy_hand1, enemy_hand2 ]
Note different players will observe this differently



It would be nice if we had a representation of states that did not have an "order" to it
1 1 2 0 is identical to 1 1 0 2
but it is hard to see this as it stands

- first just build a function that checks equality not by == but non discriminant like this

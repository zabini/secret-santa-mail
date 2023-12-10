# Secret Santa Mail

Draw a Secret Santa from a given list of participants and email them individually

## Draw a game and send to the emails
Read participants file `./data/participants.csv`, draw a game, save game encrypted on `./data/game.txt` and send it to emails
```bash
python app.py
```

## Resend all emails from last game
The previous drawn game keep encrypted on `./data/game.txt`. The command read, decrypt and resend the emails
```bash
python resend.py
```

## Resend one emails from last game to specific participant
Like command above, read a existing game. But this time, send just a specific participant email by a given name.
The participant email is optional

Long option:
```bash
python resend_one.py --name="Paticipan Name"
```
Short option:
```bash
python resend_one.py -n "Paticipan Name"
```

If the participant email has change, you can send to a new one.

Long option:
```bash
python resend_one.py --name="Paticipan Name" --email="New Participant email"
```
Short option:
```bash
python resend_one.py -n "Paticipan Name" -e "New Participant email"
```

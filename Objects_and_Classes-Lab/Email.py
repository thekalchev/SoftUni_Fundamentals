class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return (f'{self.sender} says to {self.receiver}: {self.content}.'
                f' Sent: {self.is_sent}')


final_emails = []
info = input()
while info != 'Stop':
    sender, receiver, content = info.split()
    # razdelqme si infoto na trite nujni danni i vseki pyt syzdaveme nov obekt
    # chast ot klasa Email, koito ima sender receiver content
    email_info = Email(sender, receiver, content)
    # syzdavame nov obekt pri poluchavaneto na vsqko novo info, za da mojem
    # za tozi obekt da izpratim mail-a (syhranqvame go v prazen list)
    final_emails.append(email_info)
    info = input()
indexes = [int(index) for index in input().split(', ')]
for index in indexes:
    final_emails[index].send()
    # minavame prez obektite na indexite i za syotvetniq obekt izpylnqvame
    # metoda send - koeto pravi is_sent ot False na True
for current_email in final_emails:
    print(current_email.get_info())
    # nakraq iterirame prez spisyka s obekti i vmesto sent izpylva getinfo

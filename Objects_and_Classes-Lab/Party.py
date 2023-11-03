class Party:
    def __init__(self):
        self.people = []


party = Party()  # party e obekt, Party e klasyt
name = input()
while name != 'End':
    party.people.append(name)  # appendvame inputa v people
    name = input()
print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')

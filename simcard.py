class SimCard:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, name, contact):
        if not isinstance(name, str): return
        if isinstance(contact, int):
            telephone = contact
            email = None
        elif isinstance(contact, str):
            email = contact
            telephone = None

        user = {
            "name": name,
            "telephone": telephone,
            "email": email
        }

        self.contacts.append(user)

    def show_contacts(self):
        for contact in self.contacts:
            print(contact)


user_1 = SimCard()
user_1.add_contact("Arek", "arek@wp.pl")
user_1.add_contact("Ewa", "ewa@wp.pl")
user_1.add_contact("Kasia", "kasia@wp.pl")
user_1.add_contact("Arek", 123456789)
user_1.add_contact("Arek", 123456789)
user_1.add_contact("Arek", 123456789)

# user_1.show_contacts()

print(type(user_1))

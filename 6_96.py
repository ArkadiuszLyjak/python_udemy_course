# def printUser(name, country="unknown", email="example@wp.pl"):
#     print("Name: " + name)
#     print("Email: " + email)
#     print("Country: " + country)
#     print()


# printUser(country="Poland", name="Arek", email="arek@wp.pl")
# printUser("Arek", country="Chiny")
# printUser(country="chinyLudowe", name="Arek", email="arek@wp.pl")
# printUser("Arek", country="chinyLudowe", email="arek@wp.pl")
# printUser("Arek", email="arek@wp.pl", country="chinyLudowe")


def bookTickets(band: str, number_of_tickets: int, /, *, ticket_type="normal", section="biedaszyby"):
    print("Band: " + band)
    print("Number of tickets: " + str(number_of_tickets))
    print("Ticket type: " + ticket_type)
    print("Section: " + section)


# bookTickets("Metallica", 4, ticket_type="vip", section="vip")
bookTickets("Metallica", 4, ticket_type="vip")

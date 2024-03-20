import Pyro4
from pprint import pprint

server_uri = "PYRONAME:HotelMarcodaIzaReserve.server"
server = Pyro4.Proxy(server_uri)

username = input("Digit your name: ")

while True:
    choice = int(input('1 - Consult the MarcodaIza\'s Hotel reserves\n2 - Reserve a room\n3 - Cancel a reserve\nSelect one:'))
    match choice:
        case 1:
            pprint(server.consult_reserves())
        case 2:
            room_to_reserve = input("Choose the floor and the room to reserve: Ex: \"7, 4\"").split(',')
            print(server.do_reserve(room_to_reserve[0], room_to_reserve[1], username))
        case 3:
            room_to_cancel = input("Choose the floor and the room to reserve: Ex: \"7, 4\"").split(',')
            print(server.cancel_reserve(room_to_reserve[0], room_to_reserve[1], username))
        case _:
            print('Invalid choice')

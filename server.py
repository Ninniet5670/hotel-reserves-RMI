import Pyro4

@Pyro4.expose
class HotelMarcodaizaReserve:
    def __init__(self):
        self.reserves = {i: {j: None for j in range(5)} for i in range(10)}

    def consult_reserves(self):
        return (self.reserves)

    def do_reserve(self, floor:str, room:str, name:str):
        floor, room = floor.strip(), room.strip() 
        print(self.reserves[floor][room])
        try:
            desired_room = self.reserves[floor][room]
        except Exception as e:
            return ('Could not find thy room to reserve')

        if desired_room == None:
            desired_room = name
            return ('Reserverd thy room')
        elif desired_room == name:
            return ('You already own this room')
        else:
            return ('This room is already reserved')

    def cancel_reserve(self, floor:str, room:str, name:str):
        floor, room = floor.strip(), room.strip() 
        try:
            desired_room = self.reserves[floor][room]
        except Exception as e:
            return ('Could not find thy room to cancel')

        if desired_room == None:
            return ('Not any reserves to cancel')
        elif desired_room == name:
            desired_room = None
            return ('Reserve canceled')
        else:
            return ('You do not have permission to cancel other person reserve')

daemon = Pyro4.Daemon()
server = HotelMarcodaizaReserve()
uri = daemon.register(server)

print("server URI:", uri)

ns = Pyro4.locateNS()
ns.register("HotelMarcodaIzaReserve.server", uri)

print("Server ready.")

daemon.requestLoop()

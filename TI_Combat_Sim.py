import random
def SpaceCom(Dreadnought = 0, DredMod = 0, Cruiser = 0,CruMod = 0, Destroyer = 0, DestMod = 0, WarSun = 0, WarMod = 0, Carrier = 0, CarMod = 0, Fighter = 0, FightMod = 0,PDS = 0, PMod = 0):
    hits = 0
    for n in range(int(Dreadnought)):
        roll = random.randint(1,10) + int(DredMod)
        if roll >= 5:
            hits += 1
    for n in range(int(Cruiser)):
        roll = random.randint(1,10) + int(CruMod)
        if roll >= 7:
            hits += 1
    for n in range(int(Destroyer)):
        roll = random.randint(1,10) + int(DestMod)
        if roll >= 9:
            hits += 1
    for n in range(int(WarSun) * 3):
        roll = random.randint(1,10) + int(WarMod)
        if roll >= 3:
            hits += 1
    for n in range(int(Carrier)):
        roll = random.randint(1,10) + int(CarMod)
        if roll >= 9:
            hits += 1
    for n in range(int(Fighter)):
        roll = random.randint(1,10) + int(FightMod)
        if roll >= 9:
            hits += 1
    for n in range(int(PDS)):
        roll = random.randint(1,10) + int(PMod)
        if roll >= 6:
            hits += 1
    return hits

def GroundCom(GroundForces = 0, GroundMod = 0, MechUnit = 0, MechMod = 0):
    hits = 0
    for n in range(int(GroundForces)):
        roll = random.randint(1,10) + int(GroundMod)
        if roll >= 8:
            hits += 1
    for n in range(int(MechUnit) * 2):
        roll = random.randint(1,10) + int(MechMod)
        if roll >= 6:
            hits += 1
    return hits

Dreadnought = input('Dreadnoughts: ')
DredMod = input('modifiers: ')
Cruiser = input('Cruisers: ')
CruMod = input('modifiers: ')
Destroyer = input('Destroyers: ')
DestMod = input('modifiers: ')
WarSun = input('War Suns: ')
WarMod = input('modifiers: ')
Carrier = input('Carriers: ')
CarMod = input('modifiers: ')
Fighter = input('Fighters: ')
FightMod = input('modifiers: ')
PDS = input('PDS: ')
PMod = input('modifiers: ')
print('you got',SpaceCom(Dreadnought = Dreadnought, DredMod = DredMod, Cruiser = Cruiser,CruMod = CruMod, Destroyer = Destroyer, DestMod = DestMod, WarSun = WarSun, WarMod = WarMod, Carrier = Carrier, CarMod = CarMod, Fighter = Fighter, FightMod = FightMod,PDS = PDS, PMod = PMod),'hits')

GroundForces = input('GroundForces: ')
GroundMod = input('GroundMod: ')
MechUnit = input('MechUnit: ')
MechMod = input('MechMod: ')
print('you got', GroundCom(GroundForces = GroundForces, GroundMod = GroundMod, MechUnit = MechUnit, MechMod = MechMod), 'hits')
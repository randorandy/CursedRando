from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 1
)) 

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy))  >= 14
))
hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun7 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))


missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 10
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 20
))

super4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 4
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 6
))
super12 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 12
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 30
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb6 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb8 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 5
))
powerBomb12 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 6
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and #modified for yfaster
    (PowerBomb in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout)
))
canHighSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout) and
    (HiJump in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout) or
    ( #springball blue
        (Morph in loadout) and
        (Springball in loadout)
    )
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canSpeedOrFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout) or
    (SpeedBooster in loadout)
))

canHop = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (Springball in loadout)
    )
))
greenBrin = LogicShortcut(lambda loadout: (
    (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Morph in loadout)
    ) or
    ( #left of ship speed route
        (
            (SpeedBooster in loadout) or
            (canSBJ in loadout)
        ) and
        (Morph in loadout)
        #or uncursed morph
    )
))
aboveKraid = LogicShortcut(lambda loadout: (
    (Super in loadout) and
    (
        (greenBrin in loadout) or
        (Morph in loadout) or
        (SpeedBooster in loadout) or
        (
            (HiJump in loadout) and
            (Morph in loadout)
        )
    ) 
))
beatSpore = LogicShortcut(lambda loadout: (
    (aboveKraid in loadout) and
    (Morph in loadout) and
    (Ice in loadout)
))
pastSpazer = LogicShortcut(lambda loadout: (
    (aboveKraid in loadout) and
    (Morph in loadout) and
    (
        (Spazer in loadout) or
        (Plasma in loadout)
    )
))
phantoonEntry = LogicShortcut(lambda loadout: (
    (
        (greenBrin in loadout) and
        (canUsePB in loadout) 
    ) or
    (pastSpazer in loadout) or
    (beatSpore in loadout)
))
phantoonInside = LogicShortcut(lambda loadout: (
    (phantoonEntry in loadout) and
    (
        ( #top route
            (canSBJ in loadout) and
            (canUsePB in loadout) and
            (SpaceJump in loadout) and
            (energy400 in loadout)
        ) or
        ( #bottom route
            (canUsePB in loadout) and
            (Plasma in loadout) and
            (energy400 in loadout)
        )
    )
))
bugRun = LogicShortcut(lambda loadout: (
    (Missile in loadout) and
    (Morph in loadout) and
    (Energy in loadout) and
    (
        (Ice in loadout) or
        (Charge in loadout) or
        (energy300 in loadout)
    )
))
morphRight = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (pinkDoor in loadout) and
    (
        (canUsePB in loadout) or
        (Springball in loadout) or
        (HiJump in loadout)
    )
))
direDireNW = LogicShortcut(lambda loadout: (
    (bugRun in loadout) or
    (morphRight in loadout)
    #morph implied
))
maridiaTube = LogicShortcut(lambda loadout: (
    (direDireNW in loadout) and
    (
        (SpeedBooster in loadout) or
        (canSBJ in loadout) or
        (HiJump in loadout)
        #morph implied
    )
))
iceTrippers = LogicShortcut(lambda loadout: (
    (greenBrin in loadout) and
    (
        (Ice in loadout) or
        (Grapple in loadout)
    )
))
southernCross = LogicShortcut(lambda loadout: (
    (greenBrin in loadout) and
    (pinkDoor in loadout) and
    (Varia in loadout) and
    (Morph in loadout) and 
    (energy500 in loadout) #idk
))
gtArea = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (
        (energy800 in loadout) or
        (
            (SpaceJump in loadout) and
            (HiJump in loadout)
        )
    )

))
crateriaMain = LogicShortcut(lambda loadout: (
    (gtArea in loadout) or
    (
        (southernCross in loadout) and
        (
            (Xray in loadout) or
            (
                (SpaceJump in loadout) and
                (Screw in loadout)
            ) or
            #morph implied
            (HiJump in loadout) or
            (canSBJ in loadout)
        )
    ) or
    (
        (maridiaTube in loadout) and
        #morph implied
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (GravitySuit in loadout) or
            (canSBJ in loadout)
        )
    )
))
plasmaPit = LogicShortcut(lambda loadout: (
    (crateriaMain in loadout) and
    (
        (SpaceJump in loadout) or
        (Screw in loadout) or
        (canSBJ in loadout) or
        (HiJump in loadout)
    ) and
    (Plasma in loadout)
    #morph implied
))
draygonFront = LogicShortcut(lambda loadout: (
    (crateriaMain in loadout)
))
draygonInside = LogicShortcut(lambda loadout: (
    (draygonFront in loadout) and
    (
        (SpaceJump in loadout) or
        (GravitySuit in loadout) or
        (canSBJ in loadout)
    )
))
lnWest = LogicShortcut(lambda loadout: (
    (greenBrin in loadout) and
    (Morph in loadout) and
    (Super in loadout) and
    (Varia in loadout) and
    (energy600 in loadout) and
    (
        (Grapple in loadout) or
        (Screw in loadout) or
        (canSBJ in loadout) 
    )
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}



location_logic: LocationLogicType = {
    "Morph Ball": lambda loadout: (
        True
    ),
    "First Energy Tank 72": lambda loadout: (
        (Morph in loadout)
    ),
    "Alpha Missile 1": lambda loadout: (
        (Morph in loadout)
    ),
    "Bombs": lambda loadout: (
        (
            (canUseBombs in loadout) or
            (canSBJ in loadout)
        ) and
        (pinkDoor in loadout)
    ),
    "GT Power Bomb 43": lambda loadout: (
        (gtArea in loadout) and
        (Super in loadout) and
        (energy300 in loadout) and
        (
            (
                (Screw in loadout) and
                (SpaceJump in loadout)
            ) or
            (energy800 in loadout)
        )
    ),
    "Charge Beam 8": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Alpha Super Missile 9": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Varia Suit 30": lambda loadout: (
        (iceTrippers in loadout)
    ),
    "Gravity Suit 57": lambda loadout: (
        (maridiaTube in loadout) and
        (
            (SpaceJump in loadout) or
            (HiJump in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Ice Beam 22": lambda loadout: (
        (beatSpore in loadout)
    ),
    "Hellway Missile 74": lambda loadout: (
        (greenBrin in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Attic Missile 4": lambda loadout: (
        (canBreakBlocks in loadout) and
        (
            (canUseBombs in loadout) or
            (canSBJ in loadout)
        )
    ),
    "Below Ship Blessed Orb 5": lambda loadout: (
        (canBreakBlocks in loadout) and
        (Morph in loadout)
    ),
    "Big Jump Energy Tank 6": lambda loadout: (
        (
            (canBreakBlocks in loadout) and
            (pinkDoor in loadout)
        ) or
        (
            (greenBrin in loadout) and
            (Morph in loadout)
        )
    ),
    "Gates Missile 10": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Crater Missile 2": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Morph Fall Missile 82": lambda loadout: (
        (HiJump in loadout) or
        (
            (Morph in loadout) and
            (Springball in loadout)
        )
    ),
    "First Robot Missile 3": lambda loadout: (
        True
    ),
    "Reo Hive Missile 73": lambda loadout: (
        (canBreakBlocks in loadout)
    ),
    "Ship Conveyor Missile 11": lambda loadout: (
        (greenBrin in loadout)
        #or uncursed morph
    ),
    "Gauntlet Missile 79": lambda loadout: (
        (Morph in loadout) and
        (
            (Super in loadout) or
            (
                (Missile in loadout) and
                (
                    (HiJump in loadout) or
                    (SpeedBooster in loadout) or
                    (canSBJ in loadout) or
                    (SpaceJump in loadout)
                )
            )

        )
    ),
    "Ice Trippers Power Bomb 88": lambda loadout: (
        (iceTrippers in loadout) and
        (canUsePB in loadout)
    ),
    "Ice Trippers Climb Missile 29": lambda loadout: (
        (iceTrippers in loadout)
    ),
    "Fireball Hill Super Missile 77": lambda loadout: (
        (iceTrippers in loadout) and
        (
            (Ice in loadout) or
            (Super in loadout)
        )
        #heat?
    ),
    "West Norfair Rubble Energy Tank 89": lambda loadout: (
        (iceTrippers in loadout) and
        (pinkDoor in loadout)
    ),
    "Cathedral Missile 28": lambda loadout: (
        (greenBrin in loadout) and
        (Varia in loadout) #?
        #more due to lava and heat?
    ),
    "LN West Entry Missile 48": lambda loadout: (
        (greenBrin in loadout) and
        (Super in loadout)
        #more?
    ),
    "LN Crabs Energy Tank 83": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout)
    ),
    "LN South Pit Missile 45": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #?
    ),
    "LN South Sky Missile 93": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #?
    ),
    "Grapple Beam 47": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #?
    ),
    "LN South Power Bomb 46": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout) and
        (Varia in loadout) #?
    ),
    "Red Water Super Missile 44": lambda loadout: (
        (greenBrin in loadout) and
        (canUsePB in loadout)
    ),
    "Grabber Missile 75": lambda loadout: (
        (aboveKraid in loadout) and
        (Morph in loadout)
    ),
    "Above Spazer Energy Tank 12": lambda loadout: (
        (aboveKraid in loadout)
    ),
    "Spazer 25": lambda loadout: (
        (pastSpazer in loadout)
    ),
    "Trapped Metroid Missile 27": lambda loadout: (
        (phantoonEntry in loadout)
    ),
    "Spazer Secret Missile 76": lambda loadout: (
        (aboveKraid in loadout)
    ),
    "North Brinstar Super Missile 21": lambda loadout: (
        (aboveKraid in loadout)
    ),
    "Ice Area Energy Tank 23": lambda loadout: (
        (aboveKraid in loadout)
    ),
    "Spore Spawn Prize Missile 24": lambda loadout: (
        (beatSpore in loadout)
    ),
    "North Brinstar Hidden Missile 20": lambda loadout: (
        (aboveKraid in loadout)
    ),
    "Bug Hell Missile 80": lambda loadout: (
        (bugRun in loadout)
    ),
    "Dire Dire Northwest Super Missile 13": lambda loadout: (
        (bugRun in loadout) and
        (
            (Spazer in loadout) or
            (Plasma in loadout) or
            (Charge in loadout)
        )
        #bug run or the other way
        #defeat an oum
    ),
    "Snail Missile 15": lambda loadout: (
        (direDireNW in loadout) and
        (Super in loadout)
    ),
    "Snail Energy Tank 14": lambda loadout: (
        (
            (bugRun in loadout) and
            (Super in loadout)
        ) or
        (morphRight in loadout)
    ),
    "HiJump 16": lambda loadout: (
        (direDireNW in loadout) and
        (Charge in loadout)
    ),
    "Dire Dire Covern Energy Tank 17": lambda loadout: (
        (maridiaTube in loadout) and
        (
            (GravitySuit in loadout) or
            (SpaceJump in loadout) or
            (canSBJ in loadout)
        )
    ),
    "Speed Pit Missile 55": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Dire Dire Northeast Hidden Missile 18": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Speed Booster 98": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Tube Blessed Orb 58": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Gravity Area Super Missile 56": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Outside Gravity Missile 54": lambda loadout: (
        (maridiaTube in loadout)
    ),
    "Draygon Front Door Missile 59": lambda loadout: (
        (draygonFront in loadout)
    ),
    "Draygon Power Bomb 61": lambda loadout: (
        (draygonInside in loadout)
    ),
    "Maridia Elevator From Crateria Missile 95": lambda loadout: (
        (draygonFront in loadout)
    ),
    "Crateria Hidden Pillars Energy Tank 38": lambda loadout: (
        (crateriaMain in loadout)
    ),
    "Crateria Pirate Foot Missile 91": lambda loadout: (
        (crateriaMain in loadout) and
        (
            (Plasma in loadout) or
            (canSBJ in loadout) or
            (HiJump in loadout) or
            (Charge in loadout)
        )
    ),
    "Wave Beam 39": lambda loadout: (
        (crateriaMain in loadout) and
        (Wave in loadout)
    ),
    "Plasma Beam 67": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "Sand Pit Low Missile 153": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "Sand Pit Power Bomb 84": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "Shaktool Energy Tank 66": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "GT Entry Blocks Missile 41": lambda loadout: (
        (gtArea in loadout)
    ),
    "GT Entry Ceiling Missile 40": lambda loadout: (
        (gtArea in loadout)
    ),
    "GT Entry Energy Tank 42": lambda loadout: (
        (gtArea in loadout)
    ),
    "Frog Den Power Bomb 68": lambda loadout: (
        (phantoonInside in loadout)
    ),
    "Nice Grabbers Over Acid Missile 69": lambda loadout: (
        (phantoonInside in loadout)
    ),
    "Space Jump 71": lambda loadout: (
        (phantoonInside in loadout) and
        (Missile in loadout) and
        (SpaceJump in loadout)
    ),
    "Phantoon Climb Missile 70": lambda loadout: (
        (phantoonInside in loadout)
    ),
    "Ridley Super Missile 49": lambda loadout: (
        (lnWest in loadout) and
        (
            (
                (Grapple in loadout) and
                (
                    (canBreakBlocks in loadout) or
                    (HiJump in loadout)
                )
            ) or
            (canSBJ in loadout)
        )
    ),
    "Ridley Energy Tank 50": lambda loadout: (
        (lnWest in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Ridley Power Bomb 51": lambda loadout: (
        (lnWest in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Ridley Missile 52": lambda loadout: (
        (lnWest in loadout)
    ),
    "Ridley Bangs Missile 97": lambda loadout: (
        (lnWest in loadout)
    ),
    "Southern Cross Main Missile 32": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Main Blessed Orb 31": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Lower Missile 33": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Bangs Missile 90": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Alcoon Ripper Missile 34": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Left Super Missile 36": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Right Energy Tank 37": lambda loadout: (
        (southernCross in loadout)
    ),
    "Southern Cross Right Super Missile 87": lambda loadout: (
        (southernCross in loadout)
    ),
    "Draygon Lower Maze Missile 53": lambda loadout: (
        (draygonInside in loadout) and
        (canUsePB in loadout)
    ),
    "Draygon Lower Attic Missile 62": lambda loadout: (
        (draygonInside in loadout) and
        (canUsePB in loadout)
    ),
    "Draygon Frogs Hidden Missile 99": lambda loadout: (
        (draygonInside in loadout) and
        (canUsePB in loadout)
    ),
    "Draygon Upper Maze Missile 63": lambda loadout: (
        (draygonInside in loadout) and
        (canUsePB in loadout)
    ),
    "Screw Attack 64": lambda loadout: (
        #defeat draygon
        (draygonInside in loadout) and
        (canUsePB in loadout) and
        (energy500 in loadout) and
        (
            (missile20 in loadout) or
            (canSBJ in loadout)
        )
    ),
    "Sand Pit Blessed Orb? 65": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "Springball? 78": lambda loadout: (
        (lnWest in loadout) and
        (energy800 in loadout) and
        (
            (Plasma in loadout) or
            (canSBJ in loadout) or
            (HiJump in loadout)
        )
    ),
    "Southern Cross GT Transfer Super Missile? 92": lambda loadout: (
        (gtArea in loadout)
    ),
    "Phantoon Metroid Floor Missile? 96": lambda loadout: (
        (phantoonInside in loadout)
    ),
    "Draygon Energy Tank? 60": lambda loadout: (
        (draygonInside in loadout)
    ),
    "Wave Bangs Super Missile? 19": lambda loadout: (
        (crateriaMain in loadout)
    ),
    "Botwoon Missile? 81": lambda loadout: (
        (direDireNW in loadout) and
        (Screw in loadout)
        #hopefully there is another good way
    ),
    "Xray? 35": lambda loadout: (
        (southernCross in loadout) and
        (
            (Charge in loadout) or
            (missile10 in loadout)
        )
    ),
    "Wave Pit? 86": lambda loadout: (
        (crateriaMain in loadout) and
        (canUsePB in loadout)
    ),
    "Sand Pit Super Missile? 85": lambda loadout: (
        (plasmaPit in loadout)
    ),
    "Below Spazer Blessed Orb? 26": lambda loadout: (
        (pastSpazer in loadout) or
        (beatSpore in loadout)
    ),



}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True

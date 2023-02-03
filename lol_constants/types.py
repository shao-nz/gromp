# League of Legends Types
QUEUES = {
    "Ranked Flex": "RANKED_FLEX_SR",
    "Ranked Solo/Duo": "RANKED_SOLO_5x5",
}

LOL_EMOJI = {
    # Summoner Spells
    1: "<:Cleanse:1050072357978513550>",
    3: "<:Exhaust:1050072363741491290>",
    4: "<:Flash:1050072365566021742>",
    5: "<:Backtrack:1050072356074307718>",
    6: "<:Ghost:1050072413347512503>",
    7: "<:Heal:1050072415402741810>",
    11: "<:Smite:1050072418854649867>",
    12: "<:Teleport:1050072421283147848>",
    13: "<:Clarity:1050072426769301516>",
    14: "<:Ignite:1050072424466620468>",
    21: "<:Barrier:1050072422730182678>",
    30: "<:ToTheKing:1050072354270756894>",
    31: "<:PoroToss:1050072431840198657>",
    32: "<:Mark:1050072417348886558>",
    39: "<:Mark:1050072417348886558>",
    50: "<:Resuscitate:1050072430426722415>",
    51: "<:Ghost:1050072413347512503>",
    52: "<:Warp:1050072428463788034>",
    54: "<:Empty:1050072359870136330>",
    55: "<:EmptySmite:1050072362109907005>",
    4294967295: "<:RedSmite:1050072348516163626>",
    4294967295: "<:BlueSmite:1050072350340694099>",
    4294967295: "<:GreenSmite:1050072352408469674>",

    # Runes
    "runes": "<:RunesIcon:1050111329995853874>",
    5008: "<:StatsAdaptiveForce:1050113315550003230>",
    5002: "<:StatsArmour:1050113317462622218>",
    5005: "<:StatsAttackSpeed:1050113319538790541>",
    5007: "<:StatsAbilityHaste:1050113321845674167>",
    5001: "<:StatsHealthScaling:1050113323812790382>",
    5003: "<:StatsMagicResist:1050113325503107133>",
    # Precision
    8000: "<:Precision:1050110501188812820>",
    8005: "<:PressTheAttack:1050095896982982656>",
    8008: "<:LethalTempo:1050095890196611232>",
    8021: "<:FleetFootwork:1050095880096718868>",
    8010: "<:Conqueror:1050095872173690900>",
    9101: "<:Overheal:1050095891496833127>",
    9111: "<:Triumph:1050095898698461255>",
    8009: "<:PresenceOfMind:1050095894109900841>",
    9104: "<:LegendAlacrity:1050095883624124586>",
    9105: "<:LegendTenacity:1050095887319306252>",
    9103: "<:LegendBloodline:1050095885486411877>",
    8014: "<:CoupDeGrace:1050095874107265204>",
    8017: "<:Cutdown:1050095875843702854>",
    8299: "<:LastStand:1050095881975767090>",

    # Domination
    8100: "<:Domination:1050110499037130783>",
    8112: "<:Electrocute:1050084737873629214>",
    8124: "<:Predator:1050095755530076240>",
    8128: "<:DarkHarvest:1050084735008903168>",
    9923: "<:HailOfBlades:1050095750685659228>",
    8126: "<:CheapShot:1050084730806218783>",
    8139: "<:TasteOfBlood:1050095762899468379>",
    8143: "<:SuddenImpact:1050095761016238100>",
    8136: "<:ZombieWard:1050095768565977200>",
    8120: "<:GhostPoro:1050095747011461140>",
    8138: "<:EyeballCollection:1050095745094656010>",
    8135: "<:TreasureHunter:1050095764812087356>",
    8134: "<:IngeniousHunter:1050095752686342155>",
    8105: "<:RelentlessHunter:1050095759342719066>",
    8106: "<:UltimateHunter:1050095766254919782>",

    # Sorcery
    8200: "<:Sorcery:1050110502895878275>",
    8214: "<:SummonAery:1050096703639928832>",
    8229: "<:ArcaneComet:1050096685759606895>",
    8230: "<:PhaseRush:1050096698992644106>",
    8224: "<:NullifyingOrb:1050096696127914114>",
    8226: "<:ManaflowBand:1050096692294328391>",
    8275: "<:NimbusCloak:1050096694290817034>",
    8210: "<:Transcendence:1050096705326039132>",
    8234: "<:Celerity:1050096688494301226>",
    8233: "<:AbsoluteFocus:1050096684056711290>",
    8237: "<:Scorch:1050096700536143945>",
    8232: "<:Waterwalking:1050096707079245955>",
    8236: "<:GatheringStorm:1050096690440458291>",

    # Resolve
    8400: "<:Resolve:1050110507354439701>",
    8437: "<:GraspOfTheUndying:1050096567119519844>",
    8439: "<:Aftershock:1050096555480326345>",
    8465: "<:Guardian:1050096570151993375>",
    8446: "<:Demolish:1050096561083916288>",
    8463: "<:FontOfLife:1050096562937802802>",
    8401: "<:ShieldBash:1050096577370406922>",
    8429: "<:Conditioning:1050096558978388088>",
    8444: "<:SecondWind:1050096575537479820>",
    8473: "<:BonePlating:1050096557195804692>",
    8451: "<:Overgrowth:1050096571955564544>",
    8453: "<:Revitalize:1050096573780066386>",
    8242: "<:Unflinching:1050096579152986232>",

    # Inspiration
    8300: "<:Inspiration:1050110504720408617>",
    8351: "<:GlacialAugment:1050096265628749884>",
    8360: "<:UnsealedSpellbook:1050096277351841823>",
    8369: "<:FirstStrike:1050096260704645152>",
    8306: "<:HextechFlashtraption:1050096267163865159>",
    8304: "<:MagicalFootwear:1050096269005160528>",
    8313: "<:PerfectTiming:1050096272218005566>",
    8321: "<:FuturesMarket:1050096262688542801>",
    8316: "<:MinionDematerializer:1050096270859042896>",
    8345: "<:BiscuitDelivery:1050096255323349032>",
    8347: "<:CosmicInsight:1050096257038819438>",
    8410: "<:ApproachVelocity:1050096253679177848>",
    8352: "<:TimeWarpTonic:1050096274403233842>",
}

LOL_RUNE_PATHS = {
    8000: "Precision",
    8100: "Domination",
    8200: "Sorcery",
    8400: "Resolve",
    8300: "Inspiration",
}

# Discord Emojis
DISCORD_EMOJI = {
    "blue_square": "<:blue_square:1050054413353492562>",
    "red_square": "<:red_square:1050054413353492562>"
}
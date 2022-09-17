from __future__ import annotations
from enum import IntEnum
from typing import List

class Civs(IntEnum):
    @staticmethod
    def all(exclude_gaia: bool = True) -> List[Civs]:
        return ([] if exclude_gaia else [Civs.GAIA]) + [
            Civs.AZT, Civs.BEN, Civs.BER, Civs.BOH, Civs.BRI, Civs.BUL, Civs.BRG, Civs.BRM, Civs.BYZ, Civs.CEL, Civs.CHI, Civs.CUM, Civs.DRA, Civs.FRA,
            Civs.ETH, Civs.GOT, Civs.GUR, Civs.HUN, Civs.INC, Civs.HIN, Civs.ITA, Civs.JPN, Civs.KHM, Civs.KOR, Civs.LIT, Civs.MAG, Civs.MLY, Civs.MLI, 
            Civs.MAY, Civs.MON, Civs.PER, Civs.POL, Civs.POR, Civs.SAR, Civs.SIC, Civs.SLA, Civs.SPA, Civs.TAT, Civs.TEU, Civs.TUR, Civs.VIE, Civs.VIK,
        ]

    # Sorted by Advanced Genie Editor (A.G.E) in Civilization Tab
    GAIA = 0
    BRI = 1
    FRA = 2
    GOT = 3
    TEU = 4
    JPN = 5
    CHI = 6
    BYZ = 7
    PER = 8
    SAR = 9
    TUR = 10
    VIK = 11
    MON = 12
    CEL = 13
    SPA = 14
    AZT = 15
    MAY = 16
    HUN = 17
    KOR = 18
    ITA = 19
    HIN = 20
    INC = 21
    MAG = 22
    SLA = 23
    POR = 24
    ETH = 25
    MLI = 26
    BER = 27
    KHM = 28
    MLY = 29
    BRM = 30
    VIE = 31
    BUL = 32
    TAT = 33
    CUM = 34
    LIT = 35
    BRG = 36
    SIC = 37
    POL = 38
    BOH = 39
    DRA = 40
    BEN = 41
    GUR = 42
    RE_GAIA = 0
    RE_BRI = 529
    RE_FRA = 530
    RE_GOT = 531
    RE_TEU = 532
    RE_JPN = 533
    RE_CHI = 534
    RE_BYZ = 535
    RE_PER = 536
    RE_SAR = 537
    RE_TUR = 538
    RE_VIK = 539
    RE_MON = 540
    RE_CEL = 541
    RE_SPA = 542
    RE_AZT = 543
    RE_MAY = 544
    RE_HUN = 545
    RE_KOR = 546
    RE_ITA = 547
    RE_HIN = 548
    RE_INC = 549
    RE_MAG = 550
    RE_SLA = 551
    RE_POR = 580
    RE_ETH = 581
    RE_MLI = 582
    RE_BER = 583
    RE_KHM = 650
    RE_MLY = 651
    RE_BRM = 652
    RE_VIE = 653
    RE_BUL = 673
    RE_TAT = 674
    RE_CUM = 675
    RE_LIT = 676
    RE_BRG = 748
    RE_SIC = 749
    RE_POL = 776
    RE_BOH = 777
    RE_DRA = 822
    RE_BEN = 823
    RE_GUR = 824
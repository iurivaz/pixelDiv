from django.db import models

class Canvas(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    sq0 = models.IntegerField(default=0)
    sq1 = models.IntegerField(default=0)
    sq2 = models.IntegerField(default=0)
    sq3 = models.IntegerField(default=0)
    sq4 = models.IntegerField(default=0)
    sq5 = models.IntegerField(default=0)
    sq6 = models.IntegerField(default=0)
    sq7 = models.IntegerField(default=0)
    sq8 = models.IntegerField(default=0)
    sq9 = models.IntegerField(default=0)
    sq10 = models.IntegerField(default=0)
    sq11 = models.IntegerField(default=0)
    sq12 = models.IntegerField(default=0)
    sq13 = models.IntegerField(default=0)
    sq14 = models.IntegerField(default=0)
    sq15 = models.IntegerField(default=0)
    sq16 = models.IntegerField(default=0)
    sq17 = models.IntegerField(default=0)
    sq18 = models.IntegerField(default=0)
    sq19 = models.IntegerField(default=0)
    sq20 = models.IntegerField(default=0)
    sq21 = models.IntegerField(default=0)
    sq22 = models.IntegerField(default=0)
    sq23 = models.IntegerField(default=0)
    sq24 = models.IntegerField(default=0)
    sq25 = models.IntegerField(default=0)
    sq26 = models.IntegerField(default=0)
    sq27 = models.IntegerField(default=0)
    sq28 = models.IntegerField(default=0)
    sq29 = models.IntegerField(default=0)
    sq30 = models.IntegerField(default=0)
    sq31 = models.IntegerField(default=0)
    sq32 = models.IntegerField(default=0)
    sq33 = models.IntegerField(default=0)
    sq34 = models.IntegerField(default=0)
    sq35 = models.IntegerField(default=0)
    sq36 = models.IntegerField(default=0)
    sq37 = models.IntegerField(default=0)
    sq38 = models.IntegerField(default=0)
    sq39 = models.IntegerField(default=0)
    sq40 = models.IntegerField(default=0)
    sq41 = models.IntegerField(default=0)
    sq42 = models.IntegerField(default=0)
    sq43 = models.IntegerField(default=0)
    sq44 = models.IntegerField(default=0)
    sq45 = models.IntegerField(default=0)
    sq46 = models.IntegerField(default=0)
    sq47 = models.IntegerField(default=0)
    sq48 = models.IntegerField(default=0)
    sq49 = models.IntegerField(default=0)
    sq50 = models.IntegerField(default=0)
    sq51 = models.IntegerField(default=0)
    sq52 = models.IntegerField(default=0)
    sq53 = models.IntegerField(default=0)
    sq54 = models.IntegerField(default=0)
    sq55 = models.IntegerField(default=0)
    sq56 = models.IntegerField(default=0)
    sq57 = models.IntegerField(default=0)
    sq58 = models.IntegerField(default=0)
    sq59 = models.IntegerField(default=0)
    sq60 = models.IntegerField(default=0)
    sq61 = models.IntegerField(default=0)
    sq62 = models.IntegerField(default=0)
    sq63 = models.IntegerField(default=0)
    sq64 = models.IntegerField(default=0)
    sq65 = models.IntegerField(default=0)
    sq66 = models.IntegerField(default=0)
    sq67 = models.IntegerField(default=0)
    sq68 = models.IntegerField(default=0)
    sq69 = models.IntegerField(default=0)
    sq70 = models.IntegerField(default=0)
    sq71 = models.IntegerField(default=0)
    sq72 = models.IntegerField(default=0)
    sq73 = models.IntegerField(default=0)
    sq74 = models.IntegerField(default=0)
    sq75 = models.IntegerField(default=0)
    sq76 = models.IntegerField(default=0)
    sq77 = models.IntegerField(default=0)
    sq78 = models.IntegerField(default=0)
    sq79 = models.IntegerField(default=0)
    sq80 = models.IntegerField(default=0)
    sq81 = models.IntegerField(default=0)
    sq82 = models.IntegerField(default=0)
    sq83 = models.IntegerField(default=0)
    sq84 = models.IntegerField(default=0)
    sq85 = models.IntegerField(default=0)
    sq86 = models.IntegerField(default=0)
    sq87 = models.IntegerField(default=0)
    sq88 = models.IntegerField(default=0)
    sq89 = models.IntegerField(default=0)
    sq90 = models.IntegerField(default=0)
    sq91 = models.IntegerField(default=0)
    sq92 = models.IntegerField(default=0)
    sq93 = models.IntegerField(default=0)
    sq94 = models.IntegerField(default=0)
    sq95 = models.IntegerField(default=0)
    sq96 = models.IntegerField(default=0)
    sq97 = models.IntegerField(default=0)
    sq98 = models.IntegerField(default=0)
    sq99 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def getUpdate(self):
        return {
            "sq0":self.sq0,
            "sq1":self.sq1,
            "sq2":self.sq2,
            "sq3":self.sq3,
            "sq4":self.sq4,
            "sq5":self.sq5,
            "sq6":self.sq6,
            "sq7":self.sq7,
            "sq8":self.sq8,
            "sq9":self.sq9,
            "sq10":self.sq10,
            "sq11":self.sq11,
            "sq12":self.sq12,
            "sq13":self.sq13,
            "sq14":self.sq14,
            "sq15":self.sq15,
            "sq16":self.sq16,
            "sq17":self.sq17,
            "sq18":self.sq18,
            "sq19":self.sq19,
            "sq20":self.sq20,
            "sq21":self.sq21,
            "sq22":self.sq22,
            "sq23":self.sq23,
            "sq24":self.sq24,
            "sq25":self.sq25,
            "sq26":self.sq26,
            "sq27":self.sq27,
            "sq28":self.sq28,
            "sq29":self.sq29,
            "sq30":self.sq30,
            "sq31":self.sq31,
            "sq32":self.sq32,
            "sq33":self.sq33,
            "sq34":self.sq34,
            "sq35":self.sq35,
            "sq36":self.sq36,
            "sq37":self.sq37,
            "sq38":self.sq38,
            "sq39":self.sq39,
            "sq40":self.sq40,
            "sq41":self.sq41,
            "sq42":self.sq42,
            "sq43":self.sq43,
            "sq44":self.sq44,
            "sq45":self.sq45,
            "sq46":self.sq46,
            "sq47":self.sq47,
            "sq48":self.sq48,
            "sq49":self.sq49,
            "sq50":self.sq50,
            "sq51":self.sq51,
            "sq52":self.sq52,
            "sq53":self.sq53,
            "sq54":self.sq54,
            "sq55":self.sq55,
            "sq56":self.sq56,
            "sq57":self.sq57,
            "sq58":self.sq58,
            "sq59":self.sq59,
            "sq60":self.sq60,
            "sq61":self.sq61,
            "sq62":self.sq62,
            "sq63":self.sq63,
            "sq64":self.sq64,
            "sq65":self.sq65,
            "sq66":self.sq66,
            "sq67":self.sq67,
            "sq68":self.sq68,
            "sq69":self.sq69,
            "sq70":self.sq70,
            "sq71":self.sq71,
            "sq72":self.sq72,
            "sq73":self.sq73,
            "sq74":self.sq74,
            "sq75":self.sq75,
            "sq76":self.sq76,
            "sq77":self.sq77,
            "sq78":self.sq78,
            "sq79":self.sq79,
            "sq80":self.sq80,
            "sq81":self.sq81,
            "sq82":self.sq82,
            "sq83":self.sq83,
            "sq84":self.sq84,
            "sq85":self.sq85,
            "sq86":self.sq86,
            "sq87":self.sq87,
            "sq88":self.sq88,
            "sq89":self.sq89,
            "sq90":self.sq90,
            "sq91":self.sq91,
            "sq92":self.sq92,
            "sq93":self.sq93,
            "sq94":self.sq94,
            "sq95":self.sq95,
            "sq96":self.sq96,
            "sq97":self.sq97,
            "sq98":self.sq98,
            "sq99":self.sq99
        }

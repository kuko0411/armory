from django.db import models
from item.models import Item

from common.utils import *
from enum import Enum
from achievement.models import *

class Slot(ChoiceEnum):
    WEAPON = 1
    ARMOR  = 3
    GLOVES = 4
    BOOTS  = 5

    LEFT_EARING  = 6
    RIGHT_EARING = 7
    LEFT_RING    = 8
    RIGHT_RING   = 9
    NECKLACE     = 10

    INNERWEAR = 11
    CIRCLET   = 12
    BELT      = 19
    BROOCH    = 20

class Race(ChoiceEnum):
    HUMAN       = 0
    HIGH_ELF    = 1
    AMAN        = 2
    CASTANIC    = 3
    POPORI      = 4
    BARAKA      = 5
    ELIN        = 6

class Gender(ChoiceEnum):
    FEMALE  = 0
    MALE    = 1

class Klass(ChoiceEnum):
    WARRIOR     = 1
    LANCER      = 2
    SLAYER      = 3
    BERSERKER   = 4
    SORCERER    = 5
    ARCHER      = 6
    PRIEST      = 7
    MYSTIC      = 8
    REAPER      = 9
    GUNNER      = 10
    BRAWLER     = 11
    NINJA       = 12
    VALKYRIE    = 13


# This is a hack and I know it

@make_model
@add_enum_field(Slot, lambda enum: models.ForeignKey(Item, related_name=enum.name.lower(), null=True))
class Gear:
    timestamp = models.DateField(auto_now=True)

    def __getitem__(self, x):
        return getattr(self, x.name.lower())

    def __setitem__(self, x, value):
        return setattr(self, x.name.lower(), value)

    def all(self):
        for x in Slot.all():
            yield (x, self[x])


    positions = {
        Slot.WEAPON:       (69, 93),
        Slot.ARMOR:        (338, 93),
        Slot.BOOTS:        (69, 178),
        Slot.GLOVES:       (338, 178),
        Slot.NECKLACE:     (160, 80),
        Slot.INNERWEAR:    (203, 151),
        Slot.BELT:         (203, 224),
        Slot.LEFT_RING:    (58, 263),
        Slot.RIGHT_RING:   (349, 263),
        Slot.LEFT_EARING:  (58, 9),
        Slot.RIGHT_EARING: (349, 9),
        Slot.BROOCH:       (247, 80),
        Slot.CIRCLET:      (137, 9),
    }

    crystal_positions = {
        Slot.WEAPON:        ((8, 72), (8, 118), (8, 164), (8, 210)),
        Slot.ARMOR:         ((410, 72), (410, 118), (410, 164), (410, 210)),
        Slot.RIGHT_EARING:  ((410, 8),),
        Slot.LEFT_EARING:   ((8, 8),),
        Slot.RIGHT_RING:    ((410, 274),),
        Slot.LEFT_RING:     ((8, 274),),
    }

class Server(models.Model):
    id = models.IntegerField(primary_key=True)
    name   = models.CharField(max_length=30)
    region = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Player(models.Model):
    pid    = models.IntegerField()
    name   = models.CharField(max_length=30)
    server = models.ForeignKey(Server, models.CASCADE)

    race   = EnumField(Race, null=True)
    gender = EnumField(Gender, null=True)
    klass  = EnumField(Klass, null=True)

    gearsets     = models.ManyToManyField(Gear)
    achievements = models.ManyToManyField(AchievementData, through=Achievement)

    def __str__(self):
        return self.name


    # make a custom field I guess later
    class Display:
        def __init__(self, parent):
            self.parent = parent

        @property 
        def race(self):
            race = Race(self.parent.race)

            if race == Race.POPORI and Gender(self.parent.gender) == Gender.FEMALE:
                return "Elin"

            return race.display_name()

        @property
        def gender(self):
            print(self.parent.gender)
            return Gender(self.parent.gender).display_name()

        @property
        def klass(self):
            return Klass(self.parent.klass).display_name()

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.display = Player.Display(self)


    def getAchievements(self):
        completed = {}

        for ach in Achievement.objects.filter(player=self):
            completed[ach.data.id] = ach.completed

        main = Category.objects.get(id=42)

        cats = []

        for cat in main.subcategories.all():
            cat.subs = []

            for sub in cat.subcategories.all():
                sub.achievements = []

                for ach in sub.achievementdata_set.all():
                    if ach.id in completed:
                        ach.completed = completed[ach.id]

                    sub.achievements += [ach]

                cat.subs += [sub]

            cats += [cat]

        return cats


    def compareAchievements(self, other):
        completed = {}

        for ach in Achievement.objects.filter(player=other):
            completed[ach.data.id] = ach.completed

        comparison = self.getAchievements()

        for cat in comparison:
            for sub in cat.subs:
                for ach in sub.achievements:
                    if ach.id in completed:
                        ach.completedOther = completed[ach.id]

        return comparison





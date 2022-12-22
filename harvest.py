############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # adds pairing from parameter into pairings list created in __init__
        self.pairings.append(pairing)
            

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        #calling code -> adding new_code
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon",)
    all_melon_types.append(musk)
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    all_melon_types.append(casaba)
    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    all_melon_types.append(crenshaw)
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    all_melon_types.append(yellow_watermelon)

    musk.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")

    return all_melon_types

list_of_melons = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        # for pairing in melon.pairings:
        pair = "\n-".join(melon.pairings)
        print(f"{melon.name} pairs with\n-{pair}")

# print(print_pairing_info(make_melon_types()))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}
    for melon in melon_types:
        if melon.code not in melon_dictionary.keys():
            melon_dictionary[melon.code] = melon.name
        else:
            melon_dictionary[melon.code] += melon.name
    return melon_dictionary

# print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    # Needs __init__ 
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    #  needs is_sellable methods

    def is_sellable(self):
        #shape rate > 5 && color rate > 5 && not from field 3
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else: 
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Shelia')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')    
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Shelia')

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]
    
    return melons

melons = make_melons(list_of_melons)
# print("these are melons")
# print(melons)
# print("these are all melon types")
# print(all_melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    #turns the following four lines of code into one if possible
    # condition of sale:
    for item in melons:
        sell_option = "CAN BE SOLD" if item.is_sellable() == True else "NOT SELLABLE"
        print(f"Harvested by {item.harvested_by} from FIELD {item.harvested_from} ({sell_option})")

# get_sellability_report(melons)
#chained invocations
get_sellability_report(make_melons(make_melon_types()))
import dataclasses


@dataclasses.dataclass
class WeedStrain:
    """
    Contains information about the strain
    """
    description: str = None
    name: str = None,
    good_effects: list = [],
    bad_effects: list = [],
    taste: list = [],

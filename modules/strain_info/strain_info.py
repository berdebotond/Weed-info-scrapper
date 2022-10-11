import qrcode

from modules.models.strain import WeedStrain


class StrainInfo:
    """
    StrainInfo class contains function for strain data, after we scrap the data we can format it, and create qrcode
    """
    def __init__(self, strain: WeedStrain):
        self.strain= strain

    def to_string(self):
        """
        Format strain into a string
        :return:str
        """
        return f"""
STRAIN NAME: {self.strain.name}\n
---------------------------------\n
Description: {self.strain.description}\n
Good effects: {" ".join(self.strain.good_effects)}\n
Taste effects: {" ".join(self.strain.taste)}\n
Bad effects: {" ".join(self.strain.bad_effects)}\n
        """

    def print_strain_info(self):
        """
        Print STrain info
        :return:None
        """
        print(self.to_string())

    def save_qr_code(self, path: str = None):
        """
        Save strain data into qr, the name will be the <strain_name>.png
        :param path: str path to save imges
        :return:None
        """
        img = qrcode.make(self.to_string())
        if path == None:
            img.save(self.strain.name + ".png")
        else:
            img.save(path + "/" + self.strain.name + ".png")
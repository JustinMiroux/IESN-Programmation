"""
This is the model for the basic elements
"""

class MyExeption(Exception):
    """
    This class is used when an Error should occur.
    """

    def __init__(self, msg):
        self.msg = msg


class OS:
    """
    This class limits the choice of OS and set their size accordingly
    Raises UnknownOSError when name isn't equal to available choices.
    """

    def __init__(self, name):

        name_lowered = name.lower()

        if name_lowered == "linux":
            self.name = name_lowered
            self.size = 2

        elif name_lowered == "windows":
            self.name = name_lowered
            self.size = 10

        elif name_lowered == "vmware":
            self.name = name_lowered
            self.size = 5

        else:
            raise MyExeption(f"{name} isn't a valid operating system : E-001")


class Disk:
    """
    This class is used to define disk propreties such as size, type, and os.
    """

    def __init__(self, total_size, occupied_size, disk_type):

        self.total_size = total_size
        self.occupied_size = occupied_size
        type_uppered = disk_type.upper()

        if type_uppered == "SSD":
            self.type = type_uppered

        elif type_uppered == "HDD":
            self.type = type_uppered

        elif type_uppered == "VD":
            self.type = type_uppered

        else:
            raise MyExeption(f"{disk_type} isn't a valid disk type : E-002")

    def install_os(self, os_name):
        """
        This is the function that checks if the os can be installed on the disk.
        """

        os = OS(os_name)

        if self.occupied_size <= os.size:
            raise MyExeption(f"{os} is too big and cannot fit on the disk : E-003")

class DB_Connection:
    __instance = None

    @staticmethod
    def get_instance():
        """
        if instance present return that 
        else create one and return that
        """
        if DB_Connection.__instance == None:
            DB_Connection() #calling constructor
        return DB_Connection.__instance
        
    def __init__(self):
        if DB_Connection.__instance == None:
            DB_Connection.__instance = self
        else:
            raise Exception("Cannot Create Another Instance")
"""
If there is no instance, it will create one, with help of get_instance() staticmethod
else it will return existing previous instance
"""
obj1 = DB_Connection.get_instance()
obj2 = DB_Connection.get_instance()
print(obj1 is obj2)
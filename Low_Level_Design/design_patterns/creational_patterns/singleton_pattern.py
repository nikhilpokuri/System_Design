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
            raise Exception('Cannot Create Another Instance')

"""
If there is no instance, it will create one, with help of get_instance() staticmethod
else it will return existing previous instance when use get_instance() statixmethod
But it will not raise exception nor return same instance when use __new__ method to create instance
"""
obj1 = DB_Connection()
obj2 = DB_Connection.get_instance()
obj3 = DB_Connection.get_instance()
obj4 = DB_Connection.__new__(DB_Connection) #this will create new instance
print('\nMethod-01 Output:',obj1, obj2, obj3, obj4, sep='\n')
# DB_Connection() #raise exeption 'cannot create another instance'


#----------------------------------METHOD-02------------------------------------------------
class DB_Connection1:
    __instance1 = None

    @staticmethod
    def get_instance1():
        """
        if instance present return that 
        else create one and return that
        """
        if DB_Connection1.__instance1 == None:
            DB_Connection1() #calling constructor
        return DB_Connection1.__instance1
        
    def __new__(cls):
        """
        Kind of __init__ method/constructor
        this will restrict to create instance using __new__ method
        """
        if DB_Connection1.__instance1 == None:
            DB_Connection1.__instance1 = super(DB_Connection1,cls).__new__(cls)
        return DB_Connection1.__instance1

"""
this will return first created instance to every new request for instance
below are the methods of creating instances
"""
obj1 = DB_Connection1.get_instance1()
obj2 = DB_Connection1.get_instance1()
obj3 = DB_Connection1.__new__(DB_Connection1)
obj4 = DB_Connection1()
print('\nMethod-02 Output:',obj1, obj2, obj3, obj4, sep='\n')

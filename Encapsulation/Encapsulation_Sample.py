
#   ENCAPSULATION IS THE PROCESS OF WRAPPING THE VARIABLE(FIELDS) AND THE METHODS(FUNCTION)

#    WE USE ACCESS SPECIFIERS LIKE PUBLIC, PRIVATE, AND PROTECTED FOR ENCAPSULATION

class MainClass:

    def __init__(self, publicVariable, ProtectedVariable, PrivateVariable):
        self.publicVariable = publicVariable
        self._protectedVariable = ProtectedVariable
        self.__privateVariable = PrivateVariable

    def UsingAllVariables(self):
        return self.publicVariable * self._protectedVariable * self.__privateVariable

    ''' ALL THE VARIABLES(PUBLIC PRIVATE AND PROTECTED VARIABLE ) CAN BE ACCESSED INSIDE THE CLASS AND IN ANY METHODS '''

class SubClass(MainClass):

    def UsingProtectedVariable(self):
        return self.publicVariable * self._protectedVariable

    # PROTECTED VARIABLE CAN BE ACCESSED IN THE DERIVED CLASS BUT WHEN IT IS NOT INHERITED, IT CANNOT BE ACCESSED
    # THE PRIVATE VARIABLE CAN BE ACCESSED ONLY IN THE MAIN CLASS WHERE IT IS DECLARED

su = SubClass(23, 34, 45)
print(su.UsingAllVariables())
print(su.UsingProtectedVariable())
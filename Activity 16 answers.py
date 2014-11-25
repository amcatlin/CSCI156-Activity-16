__author__ = 'Alicia'


class InvalidSocial(ValueError):
    pass


class Employee:
    pass


def validatess(employee_class):
    try:
        AAA, GG, SSSS = employee_class.ss.split('-')
        e, v, i, l = SSSS[0:4]
        area = int(AAA)
        group = int(GG)
        serial = int(SSSS)
        if len(AAA) == 3 and len(GG) == 2 and len(SSSS) == 4:
            if AAA == '078' and GG == '05' and SSSS == '1120':
                raise InvalidSocial
            elif (e == '6' and v == '6' and i == '6') or (v == '6' and i == '6' and l == '6'):
                raise InvalidSocial
            elif 1 <= area < 900 and area != 666:
                if 1 <= group <= 99:
                    if 1 <= serial <= 9999:
                        employee_class.ss = AAA, GG, SSSS
                    else:
                        raise InvalidSocial
                else:
                    raise InvalidSocial
            else:
                raise InvalidSocial
        else:
            raise InvalidSocial
    except ValueError:
        raise InvalidSocial

    #check that employee_class.ss is valid
    #Anywhere that you find the ss is invalid raise InvalidSocial


def getsocial(employee_class):
    employee_class.ss = input("Social: ").strip()
    try:
        validatess(employee_class)
    except InvalidSocial:
        print("Invalid SS, please try again\n")
        getsocial(employee_class)

emp = Employee()
getsocial(emp)
print(emp.ss)
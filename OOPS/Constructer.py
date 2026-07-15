class Company:

    Total_employee = 50
    Company_name = 'Jio'
    Contact = 1234565

darshan = Company()
rahul = Company()
sahil = Company()


def object_members(obj_name,id_no,salary,performance,bank):
    obj_name.ID_NO = id_no
    obj_name.SALARY = salary
    obj_name.PERFORMANCE = performance
    obj_name.BANK = bank

object_members(darshan,1,50000,'great','SBI')
print(darshan.ID_NO,darshan.SALARY,darshan.PERFORMANCE,darshan.BANK)

object_members(rahul,2,40000,'good','ICIC')
print(rahul.ID_NO,rahul.SALARY,rahul.PERFORMANCE,rahul.BANK)

object_members(sahil,3,30000,'bad','BARODA')
print(sahil.ID_NO,sahil.SALARY,sahil.PERFORMANCE,sahil.BANK)
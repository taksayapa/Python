#ใบงานที่5.1
def addnisit() :
    global name,sex,school_year,department,province
    print('---------------------------เเนะนำตัว---------------------------')
    addnisit = input('ชื่อ-สกุล : เพศ : ชั้นปีการศึกษา : สาขาวิชา : จังหวัด: ') 
    addnisit1 = addnisit.split('/')
    name = addnisit1[0]
    sex = addnisit1[1]
    school_year = addnisit1[2]
    department = addnisit1[3]
    province = addnisit1[4]

class nisit :
    def __init__(self,name,sex,school_year,department,province) :
        self.name = name
        self.sex = sex
        self.school_year = school_year
        self.department = department
        self.province = province
    def shownisit(self):
        print('สวัสดี ฉันชื่อ '+self.name+' เพศ '+self.sex+' ชั้นปีการศึกษาที่ '+self.school_year+' สาขาวิชา '+self.department+' มาจากจังหวัด '+self.province)

addnisit()
x = nisit (name,sex,school_year,department,province)
x.shownisit()



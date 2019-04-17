'''#学生信息包括 
#学号（唯一）  姓名  性别  年龄  寝室（一间寝室最多安排4人）
#寝室编号 男生（100 101 102） 女生（200 201 202）
#功能包括：
#1. 可以录入学生信息
#2. 录入过程中可以为其分配寝室（可选自动分配或手动分配，手动分配的话如果选择的寝室人员已满，提示重新分配）
#3. 可以打印各寝室人员列表（做到表格打印是加分项）
#4. 可以用学号索引打印特定学生信息，可以打印所有学生信息（做到表格打印是加分项）
#5. 可以为学生调整寝室（一人调整到其他寝室，两人交换寝室等，自由发挥）
#6. 可以将所有信息存入文件（json格式）
#7. 程序启动时，将文件中的学生信息自动导入系统

'''
stud = {}
dorMitory = {}
studImformation = []
#显示界面
def showInfo():
        print('-'*30)
        print('    学生宿舍管理系统   V3.1  ')
        print("1.添加学生信息")
        print('2.打印寝室人员列表')
        print('3.使用学号查找学生信息')
        print('4.调整寝室')
        print('5.打印所有学生信息')
        print('6.保存信息到文件')
        print('7.退出系统')
        print('-'*30)
#获取用户输入的序号
def getxuhao():
        xuhao = input('请输入你想选择的序号:')
        print('你选择执行的操作是：' + xuhao)
        return  int(xuhao)
#分别判断男女的房间是否已经满了
def judge():
        global dormitory
        if sex == '男':
                dormitory = int(input('请为该男生分配寝室到101到103:'))  #只能让男生分配去101和103
                if 101<= dormitory<= 103:
                        judge1()
                else:
                        print("请重新为该男生分配101-103之间的寝室")
                        judge()
        else:
                dormitory = int(input('请为该女生分配寝室到201到203:'))  #只能让女生去201和203
                if 201<= dormitory<= 203:
                        judge1()
                else:
                        print("请重新为该女生分配201-203之间的寝室")
                        judge()
def judge1():
        if dormitory in dorMitory.keys():
                if len(dorMitory.setdefault(dormitory,[]))>3:           #长度大于三，说明已经满员了
                        print('该寝室已经满员，请重新为该学生分配寝室\n')
                        judge()                                         #重新分配，重新输入该学生的寝室
                else:
                        print('已为你成功分配寝室:')
                        print(dorMitory.setdefault(dormitory,[]))
        else:
                print('成功分配寝室:')
                print(dorMitory.setdefault(dormitory,[]))
#输入学生的个人信息
def shuruxinxi():
        global iD
        global name
        global sex
        studImformation = []        #存放除了学号之外的学生信息
        while True:
                iD = int(input('请输入学生的学号：'))
                if iD in stud.keys():
                        print('该学号已经存在')
                else:
                        break

        name = input('请输入该学生的姓名:')
        sex  = input('请输入该学生的性别:')
        judge()
        studImformation.append(name)
        studImformation.append(sex)
        stud[iD] = studImformation
        dorMitory.setdefault(dormitory,[]).append(iD)
        studImformation.append(dormitory)
        print(dorMitory.setdefault(dormitory,[]))
#按照学号查询学生信息
def findstud():
        global findiD   
        findiD = int(input('请输入你想要查询的学号：'))
        if findiD in stud.keys():
                print('='*23)
                print('学生信息如下：')
                print('='*23)
                print('姓名    性别    寝室号')
                print('='*23)
                print("%s    %s    %d"%(stud[findiD][0],stud[findiD][1],stud[findiD][2]))
        else:
                print('无此学生信息，查询失败')
#输入寝室号打印寝室内所有人的信息
def printAllhouse():
        house = int(input('请输入你想要打印的寝室号：'))
        if house in dorMitory.keys():
                studid = []
                studid = dorMitory[house]       #将该寝室号内的学号全部取出来
                print("====================================")
                print('学号     姓名    性别    寝室号')
                for eachiD in studid:
                        print("%s       %s      %s      %d"%(eachiD,stud[eachiD][0],stud[eachiD][1],stud[eachiD][2]))
#打印所有学生信息
def findAllstud():
        global studiD
        print('='*40)
        print('学生信息如下：')
        print('='*40)
        print('学号     姓名    性别    寝室号')
        print('='*40)
        for studiD in stud.keys():
                print("%s\t%s\t%s\t%d\t"%(studiD,stud[studiD][0],stud[studiD][1],stud[studiD][2]))
#按学号与性别调换寝室
def changeapartment():      
        changesex = input('请输入性别：')
        twomethods = int(input('请选择你需要调换寝室的方式，互换寝室请输入1，单独要求换寝室请输入2：'))
        #第一种情况
        if twomethods == 1:
                if changesex == '男':
                        print("请分别输入两位男生的学号以及宿舍号码，宿舍号码在101-103范围内：")
                        changehousechoice1()      #开始分配的操作
                else:
                        print("请分别输入两位女生的学号以及宿舍号码，宿舍号码在201-203范围内：")
                        changehousechoice1()
        #第二种情况
        elif twomethods == 2:
                if changesex == '男':
                        print("可以调换的寝室有下：\t")
                        print("=====================")
                        for house in dorMitory.keys():
                                if  len(dorMitory[house])<4 and 101<=house<=103:
                                        print(house)
                                        changehousechoice2()  #开始分配的操作
                        
                else:
                        print("可以调换的寝室有下：\t")
                        print("=====================")
                        for house in dorMitory.keys():
                                if  len(dorMitory[house])<4 and 201<=house<=203:
                                        print(house)
                                        changehousechoice2()
def changehousechoice1():
        global changehousea
        global changehouseb
        global changeiDa
        global changeiDb
        #宿global changeida舍号码
        temp = 0
        temp1= 0
        changeiDa=int(input('请输入其中一个人的学号：'))
        changeiDb=int(input('请输入其中一个人的学号：'))
        changehousea = int(input('请输入其中一个人的现在的宿舍号码：'))
        changehouseb = int(input('请输入另外一个人的现在的宿舍号码：'))
        temp1=stud[changeiDb][2]
        stud[changeiDb][2]=stud[changeiDa][2]
        stud[changeiDa][2]=temp1
        temp=dorMitory[changehouseb]
        dorMitory[changehouseb]=dorMitory[changehousea]
        dorMitory[changehousea]=temp
        print('已成功调换')

        ''' del stud[changeiDa][2]
        del stud[changeiDb][2]
        stud[changeiDa].append(num2)
        stud[changeiDb].append(num1)
        dorMitory[changehousea].remove(changeiDa)
        dorMitory[changehouseb].remove(changeiDb)
        dorMitory[changehousea].append(changeiDb)
        dorMitory[changehouseb].append(changeiDa) '''   
def changehousechoice2():
        changehousea = int(input("请输入你目前住的寝室："))
        changehouseb = int(input("请输入你想要调换的寝室："))
        changeiDa = int(input('请输入你的学号：'))
        #将原来的信息删除，新的信息加进去
        stud[changeiDa].remove(changehousea)
        stud[changeiDa].append(changehouseb)
        dorMitory[changehousea].remove(changeiDa)      
        dorMitory[changehouseb].append(changeiDa)                    
#从文件中提取信息
def recover():
        global  dorMitory
        global  stud
        f = open("f1.txt",'r')
        t = open("t1.txt",'r')
        content1 = f.read()
        content2 = t.read()
        stud= eval(content1)
        dorMitory = eval(content2)
        f.close ()
        t.close ()
#保存文件信息
def save():  
        f=open("f1.txt",'w')
        t=open('t1.txt','w')
        f.write(str(stud))
        t.write(str(dorMitory))
        f.close()
        t.close()
#主函数
def main():
        j = 0
        while j < 1:
                showInfo()
                key = getxuhao()
                if key == 1:
                        shuruxinxi()
                elif key == 2:
                        printAllhouse()
                elif key ==3:
                        findstud()
                elif key == 4:
                        changeapartment()
                elif key == 5:
                        findAllstud()
                elif key == 6:
                        save()
                elif key == 7:
                        print('退出系统')
                        break
                else:
                        print('输入有误，请重新输入')    
recover（）
print(stud)
print(dorMitory)
main()  
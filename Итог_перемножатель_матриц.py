import random
 
 #перемножение матриц
def matrixmult(matrix1,matrix2):
    s=0     #сумма
    temporary_matrix=[]    #временная матрица
    matrix3=[]   #конечная матрица
    if len(matrix2)!=len(matrix1[0]):
        print("Матрицы не могут быть перемножены")        
    else:
        row1=len(matrix1)      #количество строк в первой матрице
        column1=len(matrix1[0])   #Количество столбцов в первой матрице   
        row2=column1           #и строк во второй матрице
        column2=len(matrix2[0])   #количество столбцов во второй матрице
        for z in range(0,row1):
            for j in range(0,column2):
                for i in range(0,column1):
                   s=s+matrix1[z][i]*matrix2[i][j]
                temporary_matrix.append(s)
                s=0
            matrix3.append(temporary_matrix)
            temporary_matrix=[]           
    return matrix3
 
#умножение матрицы на число
def matrixnum(x,matrix):
    for i in range(len(matrix)):   
        for j in range(len(matrix[i])):
            matrix[i][j]=matrix[i][j]*x
    return matrix

#ввод размерностей
def rowcolumn():
    flag=0
    while flag==0:
        print("Кол-во столбцов первой матрицы должно быть = кол-ву строк второй матрицы. Если Вы хотите умножить матрицу на число, то в полях кол-во строк и кол-во столбцов введите 1.")
        
        row1=input('Введите кол-во строк для первой матрицы > ')
        row1=int(row1)
            
        column1=input('Введите кол-во столбцов для первой матрицы > ')
        column1=int(column1)
            
        row2=input('Введите кол-во строк для второй матрицы > ')
        row2=int(row2)
        
            
        column2=input('Введите кол-во столбцов для второй матрицы > ')
        column2=int(column2)
            
        if row1 <= 0 or column1 <= 0 or row2 <= 0 or column2 <= 0:
            flag=0
            print('Дружок-пирожок, ты ввел отрицательные данные. Количество строк и столбцов не может быть меньше или равно 0. Попробуй-ка еще раз!')
        else:
            flag=1

    return row1, column1, row2, column2

#взаимодействие с пользователем
def accept():
    flag=3
    while flag!=0 and flag!=1 and flag!=2:
            flag=input()
            flag=int(flag)
            if flag!=0 and flag!=1 and flag!=2:
                print('Вы ввели значение отличное от 0, 1 или 2')
    return flag

 #создание матриц
def creatematrix(row,column):
    print('Введите 0 чтобы матрица была создана функцией Random, 1 чтобы ввести ее ПОСТРОЧНО или 2 чтобы ввести ее ПОЭЛЕМЕНТНО > ')
    flag=accept()
    if flag==0:
        temporary_matrix=[]
        matrix=[]
        for i in range(0,row):
            for j in range(0,column):
                temporary_matrix.append(random.randint(1,10))
            matrix.append(temporary_matrix)
            temporary_matrix=[]
        print("")
    if flag==1:
        print('Введите каждую строку матрицы в формате "число пробел число" (если Вы умножаете на число, то введите только одно число без пробела)')
        temporary_matrix=[]
        matrix=[]
        for i in range(0,row):
            print("Введите строку номер", i+1, "в матрицу")
            s=input()        
            s=s.split()               
            for j in range(0,column):
                temporary_matrix.append(int(s[j]))
            matrix.append(temporary_matrix)
            temporary_matrix=[]
        print("")
    if flag==2:
        print('Введите каждый элемент матрицы слева направо, сверху вниз.')
        temporary_matrix=[]
        matrix=[]
        for i in range(0,row):
            print("Введите строку номер", i+1, "в матрицу")            
            for j in range(0,column):
                print("Введите элемент номер", j+1, "строки номер ", i+1)
                s=input()  
                temporary_matrix.append(int(s))
            matrix.append(temporary_matrix)
            temporary_matrix=[]
            print("")
    return matrix

# выводим матрицу на экран
def printmatr(matrix):
    for i in range(len(matrix)):   
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

# Транспонирование матрицы
def transpose(matrix):
    n=len(matrix)
    m=len(matrix[0])
    temporary_matrix=[]
    matrix0=[]
    for i in range(0,m):        
        for j in range(0,n):
            temporary_matrix.append(matrix[j][i])
        matrix0.append(temporary_matrix)
        temporary_matrix=[]
    return matrix0

# Условия транспонирования
def conditions( n1, m1, n2, m2, matrix1, matrix2):
    flag=0 
    mnog=0
    matrix0=[]
    if n1==1 and m1==1 and (n2!=1 or m2!=1):
       print("Первая матрица представлена единственным числом")
       print("Введите 0 для отказа, 1 или 2 чтобы помножить вторую матрицу на это число > " )
       flag0=accept()
       if flag0==1 or flag0==2:
           mnog=2
    if n2==1 and m2==1 and (n1!=1 or m1!=1):
       print("Вторая матрица представлена единственным числом")
       print("Введите 0 для отказа, 1 или 2 чтобы помножить первую матрицу на это число > " )
       flag0=accept()
       if flag0==1 or flag0==2:
           mnog=3
    if n1==1 and m1==1 and n2==1 and m2==1:
       print("Обе матрицы представлены единственным числом")
       print("Введите 0 для отказа, 1 или 2 чтобы перемножить эти числа > " )
       flag0=accept()
       if flag0==1 or flag0==2:
           mnog=4
    if mnog==0:
        if m1==n2:
            flag=1
        else:
           if n1==m2:
               flag=2
           else:
               if n1==n2 and m1==m2:
                   flag=3
               else:
                   if n1==n2 and m1!=m2:
                       flag=4
                   else:
                       if n1!=n2 and m1==m2:
                           flag=5
    if  flag==1:
        print('Введенные матрицы корректны для перемножения')
        mnog=1
    if flag==2:
        print("Введенные матрицы непригодны для перемножения, НО вы можете их преобразовать, чтобы перемножить")
        print("Введите 0 чтобы не преобразовывать, 1 чтобы ТРАНСПОНИРОВАТЬ обе матрицы, 2 чтобы ПОМЕНЯТЬ матрицы МЕСТАМИ > " )
        flag2=accept()
        if flag2==1:
            matrix1=transpose(matrix1)
            print('\nТранспонированная Первая матрица:')
            printmatr(matrix1)
            matrix2=transpose(matrix2)
            print('\nТранспонированная Вторая матрица:')
            printmatr(matrix2) 
            mnog=1
        else:
            if flag2==2:
                matrix0=matrix1
                matrix1=matrix2
                matrix2=matrix0
                mnog=1
    if flag==3:
        print("Введенные матрицы непригодны для перемножения, НО вы можете их преобразовать, чтобы перемножить")
        print("Введите 0 чтобы не преобразовывать, 1 чтобы транспонировать ПЕРВУЮ матрицу, 2 чтобы транспонировать ВТОРУЮ матрицу > ")
        flag3=accept()
        if flag3==1:
            matrix1=transpose(matrix1)
            print('\nТранспонированная Первая матрица:')
            printmatr(matrix1)
            mnog=1
        else:
            if flag3==2:
                matrix2=transpose(matrix2)
                print('\nТранспонированная Вторая матрица:')
                printmatr(matrix2) 
                mnog=1
    if flag==4:
        print("Введенные матрицы непригодны для перемножения, НО вы можете их преобразовать, чтобы перемножить")
        print("Введите 0 чтобы не преобразовывать, 1 или 2 чтобы транспонировать первую матрицу > ")
        flag4=accept()
        if flag4==1 or flag4==2:
            matrix1=transpose(matrix1)
            print('\nТранспонированная Первая матрица:')
            printmatr(matrix1)
            mnog=1
    if flag==5:
        print("Введенные матрицы непригодны для перемножения, НО вы можете их преобразовать, чтобы перемножить")
        print("Введите 0 чтобы не преобразовывать, 1 или 2 чтобы транспонировать вторую матрицу > ")
        flag5=accept()
        if flag5==1 or flag5==2:
            matrix2=transpose(matrix2)
            print('\nТранспонированная Вторая матрица:')
            printmatr(matrix2)
            mnog=1
    return mnog,matrix1,matrix2


 #main
def main():
    
    row1, column1, row2, column2 = rowcolumn()
 
    matrix1= creatematrix(row1,column1)
    matrix2= creatematrix(row2,column2)
    
    print('\nПервая матрица:')
    printmatr(matrix1)
    print('\nВторая матрица:')
    printmatr(matrix2) 
    print("")

    flag,matrix1,matrix2=conditions(row1, column1, row2, column2, matrix1, matrix2)
    if flag==0:
        print("Перемножение отменено или невозможно")
    else:
        if flag==2:
            matrix3=matrixnum(matrix1[0][0],matrix2)
        if flag==3:
            matrix3=matrixnum(matrix2[0][0],matrix1)
        if flag==4:
            matrix3=matrix1[0][0]*matrix2[0][0]
        if flag==1:
            matrix3=matrixmult(matrix1,matrix2)
        print('\nПолучившаяся матрица:')
        printmatr(matrix3)

if __name__ == '__main__':
    main()

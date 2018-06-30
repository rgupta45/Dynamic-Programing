
class dynamic_proggramming():
    def create_matrix(self,row_count,column_count):
        matrix = [0] * column_count
        for m in range(column_count):
            matrix[m] = [0] * row_count
        print('matrix row: ',len(matrix),'  matrix column :',len(matrix[1]))
        return (matrix)

    def minimum_edit_distance(self,str1,str2):
        operations=[]
        row_size= len(str1)+1
        column_size = len(str2)+1
        diff = abs(row_size-column_size)
        matrix = self.create_matrix(row_size,column_size)
        for i in range(len(matrix)):
            if i== 0:
                for j in range(len(matrix[i])):
                    matrix[i][j]= j
            else:
                matrix[i][0]=i
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if str2[i-1] == str1[j-1]:
                    matrix[i][j]= matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) +1

        self._parent_pointer_MED(matrix,column_size-1,row_size-1,operations,str1,str2)
        print('The operation needed to convert string 1 to string 2 are: ',matrix[len(matrix)-1][len(matrix[0])-1])
        print('operations are :',operations)

    def _parent_pointer_MED(self,mat,row,column,op,str1,str2):
        if mat[row]==0:
            return
        elif mat[row][column] == mat[row - 1][column - 1] and str1[column-1]== str2[row-1]:
            op.append([str1[column-1], 'no cost'])
            row = row -1
            column = column -1
            self._parent_pointer_MED(mat, row,column,op,str1,str2)
        elif mat[row][column] ==  mat[row][column - 1] +1:
            op.append([str1[column - 1], 'cost of delete'])
            column = column - 1
            row =row
            self._parent_pointer_MED(mat, row, column, op, str1,str2)
        elif mat[row][column] == mat[row - 1][column - 1] + 1:
            op.append([str1[column - 1], 'cost of replace'])
            row = row - 1
            column = column - 1
            self._parent_pointer_MED(mat, row, column, op, str1,str2)
        elif mat[row][column] == mat[row-1][column] + 1:
            op.append([str1[column - 1], 'cost of insert'])
            row = row - 1
            column =column
            self._parent_pointer_MED(mat, row, column, op, str1,str2)

    def longest_palindrome_subsequence(self,str):
        position=[]
        row = len(str)
        col = row
        matrix= self.create_matrix(row,col)
        for i in range(len(matrix)):
            matrix[i][i]=1
        for i in range(1,len(matrix)+1):
            self._longest_palindrome_subsequence(str,i,matrix,pos=0)
        self._parent_pointer_LPS(matrix,str,position,row=0,column=len(str)-1)
        def lastcheck(s):
            return s[-1]
        print(matrix)
        print(sorted(position,key=lastcheck))
        print('The longest Palindromic sequence is ',matrix[0][len(str)-1])

    def _longest_palindrome_subsequence(self,str,i,mat,pos):
        if pos +i == len(str):
            return
        value= str[pos:pos+i+1]
        if value[0] != value[-1]:
            mat[pos][pos+i]=max(mat[pos][pos+i-1],mat[pos+1][pos+i])
        else:
            mat[pos][pos + i]= 2 + mat[pos+1][pos+i-1]
        pos = pos+1
        self._longest_palindrome_subsequence(str, i, mat, pos)

    def _parent_pointer_LPS(self,mat,str,position,row,column):
        if mat[row][column-1]==0 and mat[row+1][column-1]==0 and mat[row+1][column]==0:
            if row == column:
                position.append([str[row],row])
            return
        if mat[row][column] == max(mat[row][column-1],mat[row+1][column]):
            if mat[row][column-1] > mat[row+1][column]:
                row=row
                column=column-1
            else:
                row= row+1
                column=column
            self._parent_pointer_LPS(mat, str, position, row, column)
        elif mat[row][column]== 2+ mat[row+1][column-1]:
            position.append([str[row],row])
            position.append([str[column],column])
            row=row+1
            column=column-1
            self._parent_pointer_LPS(mat,str,position,row,column)

    def matrix_chain_multiplication(self,lists):
        position ={}
        row = len(lists)
        col = row
        matrix = self.create_matrix(row,col)
        for i in range(1,len(lists)):
            self._matrix_chain_multiplication(position,lists,i,matrix)
        print(matrix)
        print(position)


    def _matrix_chain_multiplication(self,position,lists,length,mat,pos=0):
        if pos + length == len(lists):
            return
        value=lists[pos:pos+length+1]
        min_list=[]
        if length==1:
            mat[pos][pos+length]= lists[pos][0]*lists[pos][1]*lists[pos+length][1]
            position[(pos,pos+length)]=(pos,pos+length)
            pos +=1
            self._matrix_chain_multiplication(position,lists,length,mat,pos)
        else:
            for k in range(length):
                mat_value= mat[pos][pos+k]+ mat[pos+k+1][pos+length] + lists[pos][0] * lists[pos+k][1] * lists[pos+length][1]
                min_list.append(mat_value)
            mat[pos][pos + length] = min(min_list)
            index = min_list.index(min(min_list))
            position[((pos,index)),((pos+2)-pos,pos+2)]= (pos,pos + length)
            pos +=1
            self._matrix_chain_multiplication(position, lists, length, mat, pos)


#-- minimum edit distance problem implementation.
#a= 'abcdef'
#b='azced'
#x= dynamic_proggramming()
#x.minimum_edit_distance(a,b)

#--------longest palendrome subsequence
#a='12612211792121'
#print(a[0:2])
#x= dynamic_proggramming()
#x.longest_palindrome_subsequence(a)

#------------- fastest matrix chain multiplication----

a =[[2,3],[3,6],[6,4],[4,5]]
x= dynamic_proggramming()
x.matrix_chain_multiplication(a)
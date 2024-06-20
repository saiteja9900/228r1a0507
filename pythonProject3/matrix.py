def read_mat(A, r, c):
    for i in range(r):
        t = []
        for j in range(c):
            val = int(input(f"Enter the A[{i}][{j}] value: "))
            t.append(val)
        A.append(t)

def disp_mat(A):
    for row in A:
        print(row)

mat_A = []
read_mat(mat_A, 2, 2)
print("Matrix A:")
disp_mat(mat_A)

mat_B = []
read_mat(mat_B, 2, 2)
print("Matrix B:")
disp_mat(mat_B)

# Assuming you want to create a new matrix c by adding mat_A and mat_B
c = []
for i in range(2):
    t = []
    for j in range(2):
        val = mat_A[i][j] + mat_B[i][j]
        t.append(val)
    c.append(t)

print("Resultant Matrix C (A + B):")
disp_mat(c)
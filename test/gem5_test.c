/*
 * Hussain Khajanchi
 * Simple GEMM implementation to test Gem5
 */

#include <stdio.h>
#include <stdlib.h>

void init_mat (int* mat, int n) {

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                    *(mat + i*n + j) = rand();
            }
        }

        return;
}
void matrix_mult (int n) {

        int* mat0 = (int*)malloc(n*n*sizeof(int));
        int* mat1 = (int*)malloc(n*n*sizeof(int));
        int* mat2 = (int*)malloc(n*n*sizeof(int));
        int sum;

        printf ("Initializing Matrices..\n");
        init_mat(mat0, n);
        init_mat(mat1, n);
        init_mat(mat2, n);
        printf ("Finished Initializing Matrices\n");

        printf ("Starting Computation \n");
        for (int i = 0; i < n; ++i)  {

                for (int j = 0; j < n; ++j) {
                sum = 0;

                 for (int k = 0; k < n; ++k) {
                   sum += *(mat0 + i*n + k) * *(mat1 + k*n + j) ;
                 }

              *(mat2 + i*n + j) = sum;

            }

        }
        printf ("Finished Computation \n");

        return;

}


int main(int argc, char* argv []) {

        int n = atoi(argv[1]);
        printf("Running Matrix Multiplication of Size %d x %d \n", n, n);
        matrix_mult(n);
        return 0;
}

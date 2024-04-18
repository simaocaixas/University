// Second auxiliar file, contains 4 auxiliar functions  

#include <stdio.h>
#include <stdlib.h>  
#include <string.h>

#define DATE 20

void swap(char **a, char **b) {
    /*
    Function swap receives two double pointers to char and swaps the addresses 
    they point to.
    
    */

    char *temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(char *arr[], int n) {
    /*
    Function bubbleSort runs a bubble sort in the array introduced, integer n
    is the number of elements in the array
    */
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (strcmp(arr[j], arr[j+1]) > 0) {
                swap(&arr[j], &arr[j+1]);
            }
        }
    }
}

void bubbleSortFloat(float arr[], int n) {
    /*
    Function bubbleSortFloat runs a bubble sort in the array of floats introduced, 
    integer n is the number of elements in the array of floats.
    */
    int i, j;
    float temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void bubbleSortDates(char dates_to_order[][DATE], int n) {
    /*
    Function bubbleSortDates runs a bubble sort in the array of arrays (2 dimensional), 
    integer n is the number of elements in the array of floats.
    */
   
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            int day1, month1, year1;
            int day2, month2, year2;
            sscanf(dates_to_order[j], "%d-%d-%d", &day1, &month1, &year1);
            sscanf(dates_to_order[j+1], "%d-%d-%d", &day2, &month2, &year2);
            
            if (year1 > year2 || (year1 == year2 && month1 > month2) || (year1 == year2 && month1 == month2 && day1 > day2)) {
                char temp[11];
                strcpy(temp, dates_to_order[j]);
                strcpy(dates_to_order[j], dates_to_order[j+1]);
                strcpy(dates_to_order[j+1], temp);
            }
        }
    }
}


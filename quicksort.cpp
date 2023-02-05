#include <iostream>

//void printArray(int array[], int sizeOfArray) {
//    for (int i = 0; i < sizeOfArray; i++) {
//        std::cout << array[i] << " ";
//    }
//    std::cout << std::endl;
//}

int partition(int array[], int left, int right, int sizeOfArray) {
    int pivot = array[left];
    int l_p = left - 1;
    int r_p = right + 1;
    while (true) {
        while (true) {
            l_p++;
            if (array[l_p] >= pivot)
                break;
        }
        while (true) {
            r_p--;
            if (array[r_p] <= pivot)
                break;
        }
        if (l_p < r_p) {
            int reml_p = array[l_p];
            array[l_p] = array[r_p];
            array[r_p] = reml_p;
        }
        else {
            return r_p;
        }
    }
}

void quickSort(int array[], int left, int right, int sizeOfArray) {
    if (left < right) {
        int q = partition(array, left, right, sizeOfArray);
        quickSort(array, left, q, sizeOfArray);
        quickSort(array, q + 1, right, sizeOfArray);
    }
}

int main() {
    //int array[] = {85,52,23,15,34,69,16,77,59,67,41,45,37,51,96,68,92,61,55,27,53,85,64,83,16,47,72,4,51,69,59,21,49,65,86,15,30,67,62,29,20,53,84,8,59,48,19,71,32,63};
    int array[] = { 85,52,23,79,34,69,16,12,14,15,18,19 };
    int sizeArr = sizeof(array) / sizeof(array[0]);
    quickSort(array, 0, sizeArr - 1, sizeArr);
}
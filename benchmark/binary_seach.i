
int BinarySearch(int arr[], int n,int size) { 

    int fst = 0;
    int lst = size - 1; 
    while (fst <= lst) { 
        int mid = (fst + lst) / 2;
        if (arr[mid] < n) fst = mid + 1; 
        else if (arr[mid] == n) break; 
        else lst = mid - 1; } 
    return mid; 
}
// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
        vector<Pair> mergeSort(vector<Pair>& pairs) {
        int n = pairs.size() - 1;
        divide(pairs, 0, n);
        return pairs;
    }

    void divide(vector<Pair>& pairs, int start, int end){
        if (end - start + 1 <= 1){
            return;
        }
        int middle = start + (end - start) / 2;
        divide(pairs, start, middle);
        divide(pairs, middle + 1, end);
        merge(pairs, start, middle, end);
    }

    void merge(vector<Pair>& arr, int start, int middle, int end){
        vector<Pair> left(arr.begin() + start, arr.begin() + middle + 1);
        vector<Pair> right(arr.begin() + middle + 1, arr.begin() + end + 1);

        int l = 0;      // left arr index
        int r = 0;      // right arr index
        int i = start;  // 'arr' index

        while (l < left.size() && r < right.size()){
            if (left[l].key <= right[r].key){
                arr[i] = left[l];
                ++l;
            }
            else{
                arr[i] = right[r];
                ++r;
            }
            ++i;
        }

        while (l < left.size()){
            arr[i] = left[l];
            ++l;
            ++i;
        }

        while (r < right.size()){
            arr[i] = right[r];
            ++r;
            ++i;
        }
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> res;

        for(int num : nums){
            res[num]++;
        }
        
        vector<pair<int,int>> arr;

        for(const auto& pair : res){
            arr.push_back({pair.second, pair.first});
        }
        sort(arr.rbegin(), arr.rend());

        vector<int> result;
        for(int i=0; i<k ;i++){
            result.push_back(arr[i].second);
        }
        

        return result;
    }
};

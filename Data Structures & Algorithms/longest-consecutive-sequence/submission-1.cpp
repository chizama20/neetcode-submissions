class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0){ return 0; }

        sort(nums.begin(), nums.end());
        int count = 1;
        int longest = 1;
        for(int i{0}; i<nums.size(); i++){
            if(nums[i+1] == nums[i]){
                continue;
            }else if(nums[i+1] - nums[i] == 1){
                count++;
            }else{
                longest = max(count, longest);
                count = 1;
            }
        }
        return max(longest, count);
    }
};

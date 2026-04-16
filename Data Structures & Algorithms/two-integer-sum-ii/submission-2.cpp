class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int l=0;
        int r=nums.size() -1;

        while(l<r){
            int curSum = nums[l] + nums[r];
            if(curSum<target){
                l++;
            }else if(curSum>target){
                r--;
            }else{
                return {l+1 , r+1};
            }
        }
    }

};

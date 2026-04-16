class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> con;
        for(auto& s : strs){
            string ss = s;
            sort(ss.begin(), ss.end());    
            con[ss].push_back(s);
        }

        vector<vector<string>> res;

        for (auto& c : con){
            res.push_back(c.second);
        }

        return res;
        
    }
};

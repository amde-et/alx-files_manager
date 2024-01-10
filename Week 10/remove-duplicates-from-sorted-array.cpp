class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    set<int> s; 
        for(int i =0; i<nums.size(); i++)
        {
            s.insert(nums[i]);
        }
        
        int ans = s.size();
        nums.clear();
        for(auto i:s)
        {
           //int k = *i;
           nums.push_back(i);
        }
        return ans;
    }
};
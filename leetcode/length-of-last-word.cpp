class Solution {
public:
    int lengthOfLastWord(string s) {
        std::vector<std::string> result; 
        std::istringstream splt(s); 
        int l = 0;
        for(std::string s; splt >> s; ) 
            l = s.length();
        return l;
    }
};

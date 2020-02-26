class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        # Converting string to list for making the operation mutable
        str_ = list(s)
        self.m = {}
        # Storing all the swapping piars in dictionary
        for i,row in enumerate(pairs):
            if row[0] not in self.m:
                self.m[row[0]] = [row[1]]
            else:
                self.m[row[0]].append(row[1])
            if row[1] not in self.m:
                self.m[row[1]] = [row[0]]
            else:
                self.m[row[1]].append(row[0])
        # Dictinary to check all the visited nodes
        self.vis = {key:False for key in self.m.keys()}
        
        # store the traversed path in sorted order 
        comp_op = []
        for key in self.vis.keys():
            if self.vis[key] == False:
                self.comp = []
                # DFS for the nodes
                def dfs(key,vis):
                    if self.vis[key] == True:
                        return
                    else:
                        self.vis[key] = True
                        self.comp.append(key)
                        for child in self.m[key]:
                            dfs(child,self.vis)
                dfs(key,self.vis)
                # Storing Indexes in sorted manner
                self.comp.sort()
                comp_op.append(self.comp)
        
        # Sorting the alphabets lexicographically and replacing in list and returning the string
        for i in range(len(comp_op)):
            x = list(map(lambda h:str_[h],comp_op[i]))
            x.sort(key = lambda h:h)
            
            for j in range(len(comp_op[i])):
                
                str_[comp_op[i][j]] = x[j]
        return "".join(str_)







# driver example
ans = Solution()
print(ans.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)

        for path in paths:
            root, *contents = path.split()
           
            for content in contents:
                file_path = content.split("(")
                file_st = file_path[1][:-1] 
                full_path = root + "/" + file_path[0]

                content_dict[file_st].append(full_path)

        res = []
        for full_dirs in content_dict.values():
            if len(full_dirs) > 1:
                res.append(full_dirs)

        return res

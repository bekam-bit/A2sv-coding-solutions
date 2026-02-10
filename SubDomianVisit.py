class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cntpdomains=[domain.split() for domain in cpdomains]

        cntpdomains_dict=defaultdict(int)
        
        for pairs in cntpdomains:
            d_list=pairs[1].split(".")
            n=len(d_list)

            for i in range(n):
                d_str=".".join(d_list[i:])
                if d_str in cntpdomains_dict:
                    cntpdomains_dict[d_str] += int(pairs[0])
                else:
                    cntpdomains_dict[d_str] = int(pairs[0])
                    
        res=[]

        for visit, dom in cntpdomains_dict.items():
            domain = str(dom)
            new_dom=" ".join([domain,visit])
            res.append(new_dom)

        return res

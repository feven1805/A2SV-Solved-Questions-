class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        myDict = {}
        for parts in cpdomains:
            count, domain = parts.split(" ")
            count = int(count)
            domain2 = domain.split(".")

            for i in range(len(domain2)):
                word = domain2[i:]
                subDomain = ".".join(word)
                if subDomain in myDict:
                    myDict[subDomain] += count
                else:
                    myDict[subDomain] = count
        output = []
        for subDomain, count in myDict.items():
            word = "{} {}".format(count, subDomain)
            output.append(word)
            
        return(output)
        

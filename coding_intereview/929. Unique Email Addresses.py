class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for i in emails:
            local = i.split('@')[0]
            domain = i.split('@')[1]
            local = local.split('+')[0].replace('.', '')
            s = local + '@' + domain
            result.add(s)
        return len(result)

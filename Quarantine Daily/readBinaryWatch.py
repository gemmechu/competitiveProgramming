class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def get_bitcount(hour, minute):
            hour = bin(hour)
            minute = bin(minute)
            result =hour.count('1') + minute.count('1')
            return result
        def get_string(hour, minute):

            h = str(hour)
            if(minute< 10):
                m = '0'+str(minute)
            else:
                m = str(minute)
            return h +':' + m
            
        result = []
        for hour in range(12):
            for minute in range(60):
                count = get_bitcount(hour, minute)
                if(count == num):
                    temp = get_string(hour, minute)
                    result.append(temp)
        return result

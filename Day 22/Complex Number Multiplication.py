class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def multiply_complex(param, param1):
            if 'i' in param or 'i' in param1:
                if('i' in param and 'i' in param1):
                    param = param.replace('i', '')
                    if (param == "" or param == "-"):
                        param += "1"
                    if (param1 == "" or param1 == "-"):
                        param1 += "1"
                    param1 = param1.replace('i', '')
                    return str(int(param) * int(param1) * (-1))
                else:
                    if( 'i' in param):

                        param = param.replace('i', '')
                        if (param == ""  or param == "-" ):
                            param += "1"
                    if('i' in param1):
                        param1 = param1.replace('i', '')
                        if(param1 == "" or param1 == "-" ):
                            param1 +="1"
                    return str(int(param) * int(param1))+'i'

            else:
                return str(int(param) * int(param1))
            pass
        a = a.split('+')
        b = b.split('+')
        result = ""
        result +=multiply_complex(a[0], b[0])+'+'
        result += multiply_complex(a[0], b[1]) + '+'
        result += multiply_complex(a[1], b[0]) + '+'
        result += multiply_complex(a[1], b[1])

        result = result.split('+')
        final =[0,0]
        for i in range(len(result)):
            if 'i' in result[i]:
                final[1] +=int(result[i].replace('i', ''))
            else:
                final[0] += int(result[i])

        result = str(final[0]) + "+" +str(final[1])+"i"

        return result
main = Solution()
main.complexNumberMultiply("2+5", "1+1i")
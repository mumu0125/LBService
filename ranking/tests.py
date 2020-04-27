from django.test import TestCase

# Create your tests here.

def compare_version(version1, version2,count=1):
    L1 = len(version1)
    L2 = len(version2)
    version1 = version1.split('.')
    version2 = version2.split('.')
    i = 0
    if L1 >= 1 and L2 >= 1:
        if int(version1[i]) > int(version2[i]):
            # print('1')
            return '1'
        elif int(version1[i]) < int(version2[i]):
            # print('-1')
            return '-1'
        else:
            if int(version1[i]) == int(version2[i]):
                # print(len(version1[i]),len(version2[i]))
                if len(version1[i]) != len(version2[i]):
                    # print('0 解释：忽略前导零，"%s" 和 "%s" 表示相同的数字"%s"' % (version1[i],version2[i], int(version1[i])))
                    message = '0 解释：忽略前导零，"%s" 和 "%s" 表示相同的数字"%s"' % (version1[i],version2[i], int(version1[i]))
                    return message
                else:
                    if L1 ==1:
                        if L2 == 1:
                            print('0')
                            return '0'
                        else:
                            # print('0,解释：version1 没有第%s级修订号，这意味着它的第%s级修订号默认为 “0”。' % (count+1,count+1))
                            return '0,解释：version1 没有第%s级修订号，这意味着它的第%s级修订号默认为 “0”。' % (count+1,count+1)
                    else:
                        version1 = '.'.join(version1[i+1::])
                        version2 = '.'.join(version2[i+1::])
                        return compare_version(version1,version2,count+1)
    elif L1 == 0:
        # print('0,解释：version1 没有第%s级修订号，这意味着它的第%s级修订号默认为 “0”。' % (count,count))
        return '0,解释：version1 没有第%s级修订号，这意味着它的第%s级修订号默认为 “0”。' % (count,count)
    else:
        while i<L1-1:
            if version1[i] == '1':
                return '1'
            i += 1
        return '0'
if __name__ == '__main__':

    print(compare_version('0.1', '1.1'))
    print(compare_version('1.0.1', '1'))
    print(compare_version('7.5.2.4', '7.5.3'))
    print(compare_version('1.01', '1.001'))
    print(compare_version('1.0', '1.0.0'))
    print(compare_version('1.0.0', '1.0'))


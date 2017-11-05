'''
merge fregments and parameters into a netlist.
'''

fragment1   =   """
write the first fregment,
follow the first parameter """
fragment2   =   """ write the first fregment, 
follow the first parameter"""
fragment3   =   """ write the first fregment,
follow the first parameter  """




def writeNetList(listName,parameter1,parameter2='',parameter3=''):
    f = open(listName,'w')
    f.write(fragment1)
    f.write(parameter1)
    f.write(fragment2)
    f.write(parameter2)
    f.write(fragment3)
    f.write(parameter3)
    f.close()
if __name__ == "__main__":
    writeNetList('netList','one--------','12345785432')


import mc_data
import mc_net

tox    =   mc_data.variation('tox', 5.50000E-09, 0.5e-9, 200) 
h0      =   mc_data.variation('h0', 83413, 1000, 200)

pair_t_h = mc_data.column_stack(tox, h0)

logfile = open("mc.log", 'w')
logfile.write(tox.name + '\n')
logfile.write('inputMean:' + str(tox.mean)+ '\n')
logfile.write("relmaen:"+ str(tox.relmean)+ '\n')
logfile.write("relmedian" + str(tox.relmedian)+ '\n')
logfile.write('inputSTD:' + str(tox.std)+ '\n')
logfile.write('relSTD:' + str(tox.relstd)+ '\n')
logfile.write('toxSize:' + str(tox.size)+ '\n')

logfile.write(h0.name + '\n')
logfile.write('inputMean:' + str(h0.mean)+ '\n')
logfile.write("relmaen:"+ str(h0.relmean)+ '\n')
logfile.write("relmedian" + str(h0.relmedian)+ '\n')
logfile.write('inputSTD:' + str(h0.std)+ '\n')
logfile.write('relSTD:' + str(h0.relstd)+ '\n')
logfile.write('h0Size:' + str(h0.size)+ '\n')

logfile.write('corrcoef:' + str(mc_data.corrcoef(tox, h0))+ '\n')

logfile.close()
print(tox.data)

mc_data.write2file(tox.data, 'tox.data')
mc_data.write2file(h0.data, 'h0.data')
mc_data.write2file(pair_t_h, 'tox_and_h0.data')
mc_net.writeNetList('netList', 'one--------',' 12345785432')

mc_net.writeNxNnetList('outNetList', tox.data, h0.data)


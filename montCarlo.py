import mc_data
import mc_net

toxe    =   mc_data.variation('toxe',2.73e-9, 0.5e-9, 500)
h0      =   mc_data.variation('h0',2.73e-9, 0.5e-9, 500)

pair_t_h = mc_data.column_stack(toxe, h0)

print(toxe.name)
print(toxe.mean)
print("relmaen:",toxe.relmean)
print(toxe.relmedian)

print(toxe.std)
print(toxe.relstd)

print(toxe.size)
print(toxe.data)

print(mc_data.corrcoef(toxe,h0))


mc_data.write2file(toxe.data,'toxe.data')
mc_data.write2file(h0.data,'h0.data')
mc_data.write2file(pair_t_h,'toxe_and_h0.data')
mc_net.writeNetList('netList','one--------','12345785432')




m = float(input('insira um valor em metros:'))
KM = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
c = m*100
mm = c*100
print('KM: \033[31;1m{:.4f}\033[m'
      '\nhm: \033[31;1m{:.3f}\033[m'
      '\ndam: \033[31;1m{:.2f}\033[m'
      '\ndm: \033[31;1m{:.0f}\033[m'
      '\ncentímetros:  \033[31;1m{:.0f}\033[m'
      '\nmilímetros: \033[31;1m{:.0f}\033[m'.format(KM, hm, dam, dm, c, mm))
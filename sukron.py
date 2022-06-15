class _toko():
    def __init__(alfamart, indomart, basmalah, homastas, harga_penjualan,):
        self.alfamart = alfamart
        self.indomart = indomart
        self.basmalah = basmalah
        self.homastas = homastas
        self.harga_penjualan= harga_penjualan
   

    def _get (self):
        print('alfamart  : ' + self.alfamart)
        print('indomart      : ' + self.indomart + ', ' +  self.indomart)
        if self.basmalah in ['basmalah']:
            basmalah = 'basmalah'
        else:
            homastas = 'homastas'
        print('homastas     :' + homastas)

        if self.harga_penjualan >90:
            print('harga_penjualan normal')
        else:
            if self.harga_penjualan >90:
                print('harga_penjualan normal')
            else:
                if self.harga_penjualan <90:
                    print('harga_penjualan normal')

print('=====================================')
print('     PROGRAM TOKO TERLARIS      ')
print('=====================================')

alfamart     = input('alfamart        :')
indomart   = input('indomart        :')
basmalah   = input('basmalah       :')
homastas    = input('homastas         :')
harga_penjualan  = float(input('Masukkan harga_penjualan :'))

print('======================================')

proses = _toko(alfamart,indomart,basmalah,homastas,harga_penjualan)
print (proses._get())
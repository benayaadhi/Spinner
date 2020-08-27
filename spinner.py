# Function Initialization
def counterClockwise(List): #buat fungsi ada parameterny dinamakan List
    putarbalik = [] #buat tempat penyimpanan yg nanti akan di append
    for i in range(len(List[0]), 0, -1): #buat fungsi i dg jarak dr length parameter list,0 dan step -1 (jadi i 3 2 1 karna turun)
        putarbalik.append(list(map(lambda x: x[i-1], List))) #menggunakan append dan fungsi lambda. map digunakan karna iterasi. list harus ditulis kalo tidak nanti jd call objekny saja 
        #bkin vriable x yg fungsiny membaca index i-1 dr list. List adalah dia baca dr parameter fungsi counterClock
        #nanti dia akan mengambil setiap angka terakhir dr list jd 3,6,9 dulu 
    return putarbalik #kembali ke putarbalik pengganti print
List_awal = [[1,2,3]
            ,[4,5,6]
            ,[7,8,9]]
# Use the Function
print(counterClockwise(List_awal)) #cetak fungsi counterclock dengan parameter List_awal yg sudah di tentukan

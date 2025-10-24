import random

def generateNumber(jumlah_data):
    data = []
    for index in range(jumlah_data):
        value = random.randint(0,100)
        data.append(value)
    return data

def bubbleSort(data):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        for value in range(0,jumlah_data - index - 1):
            # ASC (Ascending) pengurutan dari kecil ke besar (A ~ Z)
            # DSC (Descending)pengurutan dari besar ke kecil (Z ~ A)
            if (data[value] > data[value + 1]):
                # ini cara buruk
                temp = data[value]
                data[value] = data[value+1]
                data[value+1] = temp
                
def selectionSort(data):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        min_index = index
        for value in range(index+1,jumlah_data):
            if data[value] < data[min_index]:
                min_index = value
                
        data[index],data[min_index] = data[min_index],data[index]
def insertionSort(data):
    for index in range(1,len(data)):
        temp_value = data[index]
        value = index - 1
        while value >= 0 and temp_value < data[value]:
            data[value + 1] = data[value]
            value -= 1
        data[value + 1] = temp_value

def mergeSort(data):
    # recukursif
    # pemanggilan dirinya sendiri sehingga akan menimbulkan infintiy loop (paradox)
    if len(data) > 1 :
        nilai_tengah_jumlah_data = len(data) // 2
        data_bagian_kiri = data[:nilai_tengah_jumlah_data]
        data_bagian_kanan = data[nilai_tengah_jumlah_data:]
        
        # recursif
        mergeSort(data_bagian_kiri)
        mergeSort(data_bagian_kanan)
        
        # index = 0
        # value = 0
        # real_data = 0
        index = value = real = 0
        
        while index < len(data_bagian_kiri) and value < len(data_bagian_kanan):
            if data_bagian_kiri[index] < data_bagian_kanan[value]:
                data[real] = data_bagian_kiri[index]
                index += 1
            else:
                data[real] = data_bagian_kanan[value]
                value += 1
            real += 1
        
        while index < len(data_bagian_kiri):
            data[real] = data_bagian_kiri[index]
            index += 1
            real += 1
        while value < len(data_bagian_kanan):
            data[real] = data_bagian_kanan[value]
            value += 1
            real += 1

def main():
    jumlah_data = int(input("Jumlah data yang anda inginkan : "))
    data = generateNumber(jumlah_data)
    # cetak nilainya
    print("data asli:")
    print(data)
    input("please push enter to next step...............")
    print("data setelah di shorting")
    # bubbleSort(data)
    # selectionSort(data)
    # insertionSort(data)
    mergeSort(data)
    print(data)

if __name__ == "__main__":
    main()
class Sortings:
    def bubbleSort(listToSort):
        for loop in range(len(listToSort)):
            for i, j in zip(range(len(listToSort)), range(1, len(listToSort))):
                if listToSort[i] > listToSort[j]: listToSort[j], listToSort[i] = listToSort[i], listToSort[j]
        return listToSort
    
    def selectionSort(listToSort):
        for i in range(len(listToSort)): # i
            minIndex = listToSort[i]
            for j in range(i + 1, len(listToSort)): # j
                print(j)
                if listToSort[j] < minIndex: 
                    minIndex = listToSort[j]
                    listToSort[j], listToSort[i] = listToSort[i], listToSort[j]
        return listToSort
    
    def insertionSort(listToSort):
        for i in range(1, len(listToSort)): 
            k, j = listToSort[i], i - 1 # KEY
            while j >= 0 and k < listToSort[j]:
                listToSort[j + 1] = listToSort[j]
                j -= 1
            listToSort[j + 1] = k
        return listToSort
    
    def quickSort(listToSort):
        lt, eq, gt = [], [], []
        if len(listToSort) > 1:
            pv = listToSort[0]
            #EXEC
            for j in range(len(listToSort)):
                item = listToSort[j]
                if item < pv: 
                    lt.append(item)
                elif item == pv: 
                    eq.append(item)
                elif item > pv: 
                    gt.append(item)
            return Sortings.quickSort(lt) + Sortings.quickSort(eq) + Sortings.quickSort(gt)
        else: return listToSort

def main():
    lista = [6, 1, 5, 3, 2, 4]
    print(Sortings.mergeSort(lista))

if __name__ == main():
    main()
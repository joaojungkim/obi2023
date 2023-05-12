dimensao1area1 = int(input())
dimensao2area1 = int(input())
dimensao1area2 = int(input())
dimensao2area2 = int(input())
area1 = dimensao1area1 * dimensao2area1
area2 = dimensao1area2 * dimensao2area2
if area1 <= area2:
    print(area2)
else:
    print(area1)
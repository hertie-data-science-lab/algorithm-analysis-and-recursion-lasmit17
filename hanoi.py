def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    #If there's only one disk, you can move it directly to the final rod and be done
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
    else:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print(f"Move disk {n} from {from_rod} to {to_rod}")
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    #If n is greater than 1, the function will stop once the else statement reduces n to 1

TowerOfHanoi(3, 'A', 'C', 'B')  
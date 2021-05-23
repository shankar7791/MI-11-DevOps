import array as arry
def divide(arr, start, end) :
  pivot = arr[start]
  lh = start + 1
  rh = end
  print(arr)
  while True:
    while lh <= rh and arr[rh] >= pivot :
      rh = rh - 1
	
    while lh <= rh and arr[lh] <= pivot :
      lh = lh + 1
		
    if lh <= rh :
      arr[lh], arr[rh] = arr[rh], arr[lh]
    else :
      break
  arr[start], arr[rh] = arr[rh], arr[start]
	
  return rh

def quicksort(arr, start, end) :
  if start >= end :
    return
  p = divide(arr ,start, end)
  quicksort(arr, start, p-1)
  quicksort(arr, p+1, end)

arr = arry.array("i", [14, 46, 43, 27, 57, 41, 45, 21, 70])
quicksort(arr, 0, len(arr)-1)
print(arr)


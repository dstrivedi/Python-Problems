#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

def maximumProduct(list):
  n = len(list);
  product = [];
  list.sort(reverse=True);
  min1 = list[n - 1];
  min2 = list[n -2 ];
  max0 = list[0];
  max1 = list[1];
  max2 = list[2];
  product1 = min1*min2*max0;
  product2 = max0*max1*max2;
  product.insert(0,product1);
  product.insert(1,product2);
  maxProduct = max(product);
  print(maxProduct);
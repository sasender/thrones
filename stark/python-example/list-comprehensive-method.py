list_genaral_method = []

for i in range(0,25):
    list_genaral_method.append(i)

print (list_genaral_method)


#############################################

#list-comprehesion-method
#############################--------------------------------


sasender = []

sasender = [i for i in range(0,25)]

print (sasender)

####################################################
# print odd-methods

list_odd_methods = [i for i in range(1,15, 2)]

print (list_odd_methods)

################################################
list_odd_method1 = [i for i in range(0,15,3)]

print (list_odd_method1)

##################################################

list_odd_method = [i for i in range(0,15) if i % 2 == 1]

print (list_odd_method)

list_even_method = [i for i in range(0,15) if i % 2 == 0]

print (list_even_method)

############################################################

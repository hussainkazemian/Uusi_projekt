def print_city(city3):  #(parametria)
    #lokaali muuttuja, arvo käytössä vain funktion sisällä (local scope)
    city= "Espoo"

    #added
    city2 = "Vatnaa"
    print(city)
    print(city2)
    print(city3) #myös funktion parametria eitelty muttuja on lokaali
def print_city_v2():
        print(city) #tulostaa globaalin muuttuja arvon
# globaali muuttuja, arvo käytössä koko ohjelman laajuisesti (global scope)
city = "Helsinki"
print_city("lähti")
print_city("kirkkonumi")  #tulosta edellen city
print(city)
print_city_v2()
#tässä on kaksi eri asioita,#global scope and local scope

"""def list_sum(nums): #jos on shadow error. kannaatta vaihtaa toinen nimi.
    print("lasketaan allaolevan listan alkioiden summa")
    print(nums)
    result = 0
    for num in nums:
        result = result + num
    return result
numbers = [1, 2, 5, 8]
print(list_sum(numbers))

#print(sum(numbers)) löytyy myös sisäärakennerruna, mutta toteutetaan nyt ite

numbers_sum = list_sum([1, 2, -5])
print(numbers_sum)


#tehtävä_4
numbers = [1, 2, 5, 8]
print(sum(numbers))
"""
def list_reset (nums):
    print("nollataan kaikki lista alkiot")
    print(nums)
    #nums = nums.copy() #listasta voidaan luoda uusi uniikki kopio.copy ()- metodilla kopionti
    for i in range(5):
        nums[i] = 0

    return nums
numbers = [10, 22, 5, 7, 9]

#numbers2 = numbers.copy()
print(list_reset(numbers))
print(numbers) # myös alkup, lista on muuttunut, koska funktiota syötetty parametrina viittaus

"""def numbers_to_list(num1, num2, num3, ): #(nums)
    my_list = [num1, num2, num3, ]
    return my_list
print(numbers_to_list(5, 8, 22,))
"""
def numbers_to_list(*nums): #(nums)
    for num in nums: return nums
print(numbers_to_list(5, 7, 5, 12, 11))
#monikko eli tuple, kuin lista joita ei voi muokata
numbers= (22,55,84,30)
print(numbers[2])
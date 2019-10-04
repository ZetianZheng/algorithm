# l = list(map(int,input("input value:").strip().split()))
# initialize a city and some indicators :
building = [0,1,0,2,1,0,1,3,2,1,2,1]
buildingnumber = len(building)
watersum = 0
cleft = 0 # index of current building on the left
# hleft = 0 # index of  relative high building on the left
cright = buildingnumber-1 # index of current building on the right
# hright = buildingnumber-1 # index of relative high building on the right
Lleft = 0 #water line on the left
Lright = 0 #water line on the right

# initialize water line
Lleft = building[cleft]
Lright = building[cright]

# this algorithm will stop when two sides converged, meanwhile they will stop on the highest building of all buildings
while cright != cleft:
	# if water line on the left bigger than that on the right, move right one and update waterline on the right and calculate trapped water on the right
	if Lleft > Lright:
		cright -= 1
		print ('cright', cright)
		if building[cright] - building[cright+1] < 0: # if height of the building comes down there is a water trapped
				watersum = watersum + Lright - building[cright]
		else: # height of building comes up or stay
			if Lright > building[cright]:#current height isn`t reach the water line, there is a water trapped
				watersum = watersum + Lright - building[cright]
			else:#update water line when current height reach the water line on the right
				Lright = building[cright]


	# if water line on the right bigger than that on the left, move left one and update waterline on the left and calculate trapped water on the left

	if Lleft < Lright:
		cleft += 1
		print ('cleft', cleft)
		if building[cleft] - building[cleft-1] < 0:
			watersum = watersum + Lleft - building[cleft]
		else:
			if Lleft > building[cleft]:
				watersum = watersum + Lleft - building[cleft]
			else:
				Lleft = building[cleft]
	# if water line on the left and right are the same, move whatever right or left one(here moves left)
	if Lleft == Lright:
		if cleft == cright:
			break
		else:
			cleft += 1
			print ('cleft', cleft)
			if building[cleft] - building[cleft-1] < 0:
				watersum = watersum + Lleft - building[cleft]
			else:
				if Lleft > building[cleft]:
					watersum = watersum + Lleft - building[cleft]
				else:
					Lleft = building[cleft]
print (watersum)



def node_type(arg1):


	arg1=int(arg1)

	class MyNode:
	
	    	def __init__(self, id, type):
			self.id = id
	       		self.type = type
	
	#global Nodelist
	Nodelist = []

	for i in range(40):
	    Nodelist.append(MyNode(i+1, 'NaN'))


	for ii in range(1, 41):

	    if     Nodelist[ii-1].id== 3 or Nodelist[ii-1].id== 4 or Nodelist[ii-1].id== 6 \
		or Nodelist[ii-1].id== 7 or Nodelist[ii-1].id== 8 or Nodelist[ii-1].id== 9 \
		or Nodelist[ii-1].id== 13 or Nodelist[ii-1].id== 14 or Nodelist[ii-1].id== 16 \
		or Nodelist[ii-1].id== 17 or Nodelist[ii-1].id== 18 or Nodelist[ii-1].id== 23 \
		or Nodelist[ii-1].id== 24 or Nodelist[ii-1].id== 25 or Nodelist[ii-1].id== 27 \
		or Nodelist[ii-1].id== 28 or Nodelist[ii-1].id== 32 or Nodelist[ii-1].id== 33 \
		or Nodelist[ii-1].id== 34 or Nodelist[ii-1].id== 35 or Nodelist[ii-1].id== 37 \
		or Nodelist[ii-1].id== 38 :

		Nodelist[ii-1].type = 'USRP'

	    elif   Nodelist[ii-1].id== 2 or Nodelist[ii-1].id== 5 or Nodelist[ii-1].id== 10 \
		or Nodelist[ii-1].id== 12 or Nodelist[ii-1].id== 15 or Nodelist[ii-1].id== 20 \
		or Nodelist[ii-1].id== 21 or Nodelist[ii-1].id== 26 or Nodelist[ii-1].id== 29 \
		or Nodelist[ii-1].id== 31 or Nodelist[ii-1].id== 36 or Nodelist[ii-1].id== 39 :

		Nodelist[ii-1].type = 'Pico2x2' 

	    elif   Nodelist[ii-1].id== 1 or Nodelist[ii-1].id== 19 or Nodelist[ii-1].id== 22 \
		or Nodelist[ii-1].id== 40 :

		Nodelist[ii-1].type = 'Pico4x4'

	#print ("Node%d : " %Nodelist[arg1-1].id) + Nodelist[arg1-1].type

	#print Nodelist[arg1-1].type

	return Nodelist[arg1-1].type




#if __name__ == "__main__":
#	main(sys.argv[1])		#Allows iput arguments



#for i in range(0,40) :
#    print ("Node %d -> " %Nodelist[i].id) + Nodelist[i].type





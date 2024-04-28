import stats

def main():
	x=0

	list=[]
	while len(list)<11:
	    y=input()
	    if y.isdigit():
	        list.append(int(y))
	    else:
	        print("NOT A NUMBER")
	        continue
	print(stats.mode(list))
	
if __name__ == "__main__":
	main()

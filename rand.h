int boundedRand(int min,int max){
	int distance, anyRandom, x;
	distance = max - min;
	x = anyRandom % distance;
	return(x*min);

}

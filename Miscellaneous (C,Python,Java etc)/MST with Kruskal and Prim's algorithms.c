#include <stdio.h>  
#include <stdbool.h> 
 

//finds thevertex
int find_vert(int i,int dis_sets[]) 
{ 
	while (dis_sets[i] != i) 
		i = dis_sets[i]; 
	
  return i; 
} 

// Union 
void Union(int i, int j,int dis_sets[]) 
{ 
	int a = find_vert(i,dis_sets); 
	int b = find_vert(j,dis_sets); 
	
  dis_sets[a] = b; 
} 

// Kruskal's algorithm 
void kruskalMST(unsigned long num,int adj[num][num]) 
{ 
  int totalweight = 0;  
  int dis_sets[num];

	for (int i = 0; i < num; i++){ //initialize disjoint sets 
		dis_sets[i] = i;
  }

  printf("USING KRUSKAL'S ALGORITHM \n"); 


	// Include minimum weights 
	int edges = 0; 
	while (edges < num - 1) { 
		int min = 9999999, a = 0, b = 0; 
		for (int i = 0; i < num; i++) { 
			for (int j = 0; j < num; j++) { 
				if (find_vert(i,dis_sets) != find_vert(j,dis_sets) && adj[i][j] < min && adj[i][j] != -1) { 
					min = adj[i][j]; 
					a = i; 
					b = j; 
				} 
			} 
		} 
    
		Union(a, b,dis_sets);
    a++,b++; 
		printf("(%d , %d , %d) \n", a, b, min);
    edges++; 
		totalweight = totalweight + min; 
	} 
	printf("\n");
  printf("Total weight= %d \n", totalweight); 
} 


//find and return minimum weight's vertex
int minWeight(int weight[], bool inMST[],unsigned long num) 
{ 
	int min = 9999999;
  int min_vert; 

	for (int i = 0; i < num; i++) 
		if (inMST[i] == false && weight[i] < min) {
			min = weight[i];
      min_vert = i; 
    }
	return min_vert; 
} 

//////////////////////////////////////////////////////

void primMST(unsigned long num,int adj[num][num]) {  
	int MST[num]; 
	//store weight 
	int weight[num]; 
	//to check if value already in MST 
	bool inMST[num]; 

	for (int i = 0; i < num; i++) {
		weight[i] = 9999999;
    inMST[i] = false; 
  }
	
  // initiate starting vertex  
	weight[0] = 0; //weight 0 to make it first element
	MST[0] = -1; //root of tree,start

	
	for (int p = 0; p < num - 1; p++) { 

    //take the smallest weight's vertex;check from all the vertices not yet in MST 
		int i = minWeight(weight, inMST,num);  
		inMST[i] = true; //insert in MST and update inMST


    //updadate the adjacent vetices weights;check the vertices which are not yet in MST
		for (int j = 0; j < num; j++) 
      //update the weight only if adj[i][j] is smaller than weight 
			if (adj[i][j] != -1 && inMST[j] == false && adj[i][j] < weight[j]){ 
				MST[j] = i;
        weight[j] = adj[i][j]; 
	}   }

	int sum = 0;  //print
  printf("USING PRIM'S ALGORITHM \n"); 
	for (int k = 1; k < num; k++){ 
		printf("(%d , %d , %d) \n", MST[k]+1, k+1, adj[k][MST[k]]);
    sum =  adj[k][MST[k]] + sum;
  }
  printf("\n");
  printf("Total weight = %d",sum); 
  printf("\n\n");
}

int main(void) {
    unsigned long num;
    //int vertices = 0;
    

    printf("Enter the number of vertices: ");
    scanf("%lu", &num);
    int adj[num][num];
    //int sqr[num][num];

    printf("Enter the adj matrix:\n");
    for (int i = 0; i < num; ++i)
        for (int j = 0; j < num; ++j)
            scanf("%d", &adj[i][j]);

    printf("\nThe original graph is:\n");
    for (int i = 0; i < num; ++i) {
        for (int j = 0; j < num; ++j) {
            printf("%d ", adj[i][j]);
            //sqr[i][j] = adj[i][j];
        }
        printf("\n");
    }

    printf("\n");

    primMST(num,adj);
    kruskalMST(num,adj);


    
    
    
    return 0;
}


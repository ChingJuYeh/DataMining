#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define TRAIN_COUNT 567
#define CHARACTERISTIC_COUNT 8 
#define TEST_COUNT 201

typedef struct Check
{
	int SICK;
	float characteristic[CHARACTERISTIC_COUNT];
	float distance;
}Check;
Check ch_train[TRAIN_COUNT],ch_test[TEST_COUNT];
int correct_outcome[TEST_COUNT];

void load_train_txt();
void load_test_txt();
void Euclidean_Distance(Check *ch);
void Bubble_sort();
int KNN(int num);

int main()
{
	int i, j, k, l;
	Check *ptr;
	
	load_train_txt();
	load_test_txt();
	for(k=1;k<301;k++){
	
	for(i=0; i<TEST_COUNT; i++) {
		ptr = &ch_test[i];
		Euclidean_Distance(ptr);
		Bubble_sort();
		l = KNN(k);
		ch_test[i].SICK = l;
	}
	float count=0;
	for (i=0; i<TEST_COUNT; i++){
		if(correct_outcome[i]==ch_test[i].SICK){
			count++;
		}		
	}
	printf("k=%d , 正確率 : %f%%\n",k,(count/TEST_COUNT)*100);
		}
	 return 0;
}
void load_train_txt()
{
	int i, j;
	FILE *fp = fopen("train_data.txt", "r");
	
	if(!fp)
    	printf("Unable to open the FILE !\n");
    
    for (i=0; i<TRAIN_COUNT; i++) {   	
    	for (j=0; j<CHARACTERISTIC_COUNT; j++) {
    		fscanf(fp, "%f ", &ch_train[i].characteristic[j]);
		}
		fscanf(fp, "%d ", &ch_train[i].SICK);
    }
    fclose(fp);
    float all=0,count=0,ave;
    for (i=0; i<TRAIN_COUNT; i++) {   	
    	for (j=1; j<CHARACTERISTIC_COUNT; j++) {
    		if(ch_train[i].characteristic[j]!=0){
    			all=all+ch_train[i].characteristic[j];
    			count++;
			}
		}		
    }
    ave=all/count;
    for (i=0; i<TRAIN_COUNT; i++) {   	
    	for (j=1; j<CHARACTERISTIC_COUNT; j++) {
    		if(ch_train[i].characteristic[j]==0){
    		ch_train[i].characteristic[j]=ave;
			}
		}		
    }
}
void load_test_txt()
{
	int i, j;
	FILE *fp = fopen("test_data.txt", "r");
	if(!fp)
    	printf("Unable to open the FILE !\n");
    
    for (i=0; i<TEST_COUNT; i++) {
    	for (j=0; j<CHARACTERISTIC_COUNT; j++) {
    		fscanf(fp, "%f ", &ch_test[i].characteristic[j]);
		}
		fscanf(fp, "%d ", &correct_outcome[i]);
    }
    fclose(fp);
    
    float all=0,count=0,ave;
    for (i=0; i<TEST_COUNT; i++) {   	
    	for (j=1; j<CHARACTERISTIC_COUNT; j++) {
    		if(ch_test[i].characteristic[j]!=0){
    			all=all+ch_test[i].characteristic[j];
    			count++;
			}
		}		
    }
    ave=all/count;
    for (i=0; i<TEST_COUNT; i++) {   	
    	for (j=1; j<CHARACTERISTIC_COUNT; j++) {
    		if(ch_test[i].characteristic[j]==0){
    		ch_test[i].characteristic[j]=ave;
			}
		}		
    }
}
void Euclidean_Distance(Check *ch)
{
    int i, j;
    float eu=0.0;
    
    for(i=0; i<TRAIN_COUNT; i++) {
        for(j=0; j<CHARACTERISTIC_COUNT; j++) {
            eu += ((ch_train[i].characteristic[j]-(*ch).characteristic[j]) * (ch_train[i].characteristic[j]-(*ch).characteristic[j]));
        }
        ch_train[i].distance = sqrt(eu);

        eu=0.0; //Reset.
    }
}
void Bubble_sort()
{
	int i, j;
	Check tmp;
	
    for(i=0; i<TRAIN_COUNT-1; i++) {
        for(j=i+1; j<TRAIN_COUNT; j++) {
            if(ch_train[i].distance > ch_train[j].distance) {
            	tmp = ch_train[i];
               	ch_train[i] = ch_train[j];
               	ch_train[j] = tmp;
            }
        }
    }
}
int KNN(int num)
{
    int i, j, max = 0;
    int type[2]; //1:SICK  0:not sick
    
    for(i=0; i<2; i++) //Set array '0'
        type[i] = 0;
 
    for(i=0; i<num; i++) {
        if(ch_train[i].SICK == 0)
        	type[0] ++;
        else if(ch_train[i].SICK == 1)
        	type[1] ++;
    }
 
    max = 0;
    for(i=0; i<2; i++)
    {
        if(type[i] > max) {
        	max = type[i];
        	j = i; //find the most
		}
    }
    return j;
}

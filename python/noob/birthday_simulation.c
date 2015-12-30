#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <getopt.h>
#include <string.h>
#include <math.h>
#include <sys/time.h>

int compare(const void *a, const void *b)
{
	const int *da = (const int *) a;
	const int *db = (const int *) b;
	return (*da > *db) - (*da < db);
    
    
}

void sort_ints(int *a, size_t n)
{
    qsort(a, n, sizeof(int), compare);
}

bool has_duplicates(int *a) {
	size_t length = sizeof(a)/sizeof(int);
	int i;

	sort_ints(a, length);

	for (i = 0; i < length; i++) {
		if (a[i] == a[i+1]) return true;
	}

	return false;
}

bool has_duplicates_brutal(int *a) {
	int count = sizeof(a)/sizeof(int);
	int i,j;

	for (i = 0; i< count; i++) {
		for (j = i+1; j< count; j++) {
			if (a[i] == a[j]) return true;
		}
	}
	return false;
}

int main (int argc, char *argv[])
{
	struct timeval start,end;
	gettimeofday(&start, NULL);

	int seed = time(NULL);
	int num_birthdays = 10;
	int num_trials = 1000;
	long total_overlaps = 0;
	long total_birthdays = 0;
	int i, j, lineno;
	double perc;

	srand(seed);

/*	while ((lineno = getopt(argc, argv, "n::t::")) != 1)
	{
		
		switch (lineno)
		{
		case 0:
			break;
		break;
		
		case 't':
			num_trials = atoi(optarg);
		break;
		case 'n':
			num_birthdays = atoi(optarg);
		break;
		default: ;
		
		}
	}*/
	
	printf("FUCK THIS SHIT %d", (rand() % 365) + 1);
	printf("Enter # of birthdays: ");
	scanf("%d", &num_birthdays);
	printf("\nEnter # of trials: ");
	scanf("%d", &num_trials);

	for (i = 0; i < num_trials; i++) {
	        int *birthdays = (int*)malloc(sizeof(int) * num_birthdays);

		total_birthdays += num_birthdays;

		for (j=0;j<num_birthdays;j++) {
			birthdays[j] = (int) (rand() % 365) + 1;
		}
		
		if (has_duplicates_brutal(birthdays)) total_overlaps++;

		free(birthdays);
	}	

	perc = (double) total_overlaps / total_birthdays;

	gettimeofday(&end, NULL);
	double time_taken = (double) ((end.tv_usec - start.tv_usec) / 1000000); // + (end.tv_sec - start.tv_sec);

	printf("Total Birthdays: %d, Total Overlaps: %d, Percentage: %f \nTime Taken: %f\n", total_birthdays, total_overlaps, ((double) total_overlaps / total_birthdays * 100), time_taken);

	return 0;
}

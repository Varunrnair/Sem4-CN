#include <stdio.h>
#include <stdbool.h>

#define MAX_NODES 100
#define INF 1000000

int main()
{
    int c[MAX_NODES][MAX_NODES] = {
        {0, 6, 5, 5, INF, INF, INF},
        {INF, 0, INF, INF, -1, INF, INF},
        {INF, -2, 0, INF, 1, INF, INF},
        {INF, INF, -2, 0, INF, -1, INF},
        {INF, INF, INF, INF, 0, INF, 3},
        {INF, INF, INF, INF, INF, 0, 3},
        {INF, INF, INF, INF, INF, INF, 0}
    };
    int d[MAX_NODES], pi[MAX_NODES], n, i, j, k, val, l;
    bool negative_cycle = false;

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        d[i] = c[0][i];
        if (i != 0) {
            pi[i] = 1;
        }
    }
    pi[0] = 0;

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                val = d[j] + c[j][k];
                if (d[k] > val) {
                    d[k] = val;
                    pi[k] = j + 1;
                }
            }
        }
        for (l = 0; l < n; l++) {
            printf("\nd%d = %d", l, d[l]);
            printf("\tp%d = %d", l, pi[l]);
        }
        printf("\n");
    }

    // Check for negative cycles
    for (j = 0; j < n; j++) {
        for (k = 0; k < n; k++) {
            val = d[j] + c[j][k];
            if (d[k] > val) {
                negative_cycle = true;
                break;
            }
        }
        if (negative_cycle)
            break;
    }

    if (negative_cycle) {
        printf("\nGraph contains a negative cycle\n");
    } else {
        for (i = 0; i < n; i++) {
            printf("\nd%d = %d", i, d[i]);
            printf("\tp%d = %d", i, pi[i]);
        }
    }
    return 0;
}
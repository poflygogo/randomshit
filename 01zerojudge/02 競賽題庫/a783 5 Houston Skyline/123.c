#pragma warning (disable:4996)

#include <stdio.h>
#define MAXW 50
#define MAXH 20
char skyline[MAXH + 17][MAXW + 2];
int heightList[MAXW + 1];

inline void initialize();
int main() {
	int n, startX, width, height, maxHeight;

	while (~scanf("%d", &n)) {
		initialize();
		maxHeight = 0;

		while (n--) {
			scanf("%d %d %d", &startX, &width, &height);

			if (height == 0)
				continue;

			if (height + 1 > maxHeight)
				maxHeight = height + 1;

			for (int x = startX; x <= MAXW && x <= width + startX + 1; ++x) {
				if (heightList[x - 1] < height + 1)
					heightList[x - 1] = height + 1;
			}
		}

		// 每個位置的最高點都標記為 '-'
		for (int x = 0; x < MAXW; ++x)
			skyline[heightList[x]][x] = '-';

		// 標記轉角和垂直的陰影
		for (int x = 0; x < MAXW; ++x) {
			if (heightList[x] < heightList[x + 1]) {
				for (int y = heightList[x] + 1; y < heightList[x + 1]; ++y)
					skyline[y][x + 1] = '|';
				skyline[heightList[x]][x + 1] = '+';
				skyline[heightList[x + 1]][x + 1] = '+';
			}
			else if (heightList[x] > heightList[x + 1]) {
				for (int y = heightList[x] - 1; y > heightList[x + 1]; --y)
					skyline[y][x] = '|';
				skyline[heightList[x]][x] = '+';
				skyline[heightList[x + 1]][x] = '+';
			}
		}

		// 邊際條件處理
		if (heightList[0] > 0) {
			for (int y = 1; y < heightList[0]; ++y)
				skyline[y][0] = '|';
			skyline[0][0] = '+';
			skyline[heightList[0]][0] = '+';
		}

		// 輸出結果
		for (int y = maxHeight; y >= 0; --y) {
			for (int x = 0; x < MAXW; ++x)
				printf("%c", skyline[y][x]);
			puts("");
		}
		for (int k = 1; k <= 50; ++k)
			printf("%d", k % 10);
		puts("");
	}

	return 0;
}

inline void initialize() {
	for (int k = 0; k <= MAXH; ++k) {
		for (int j = 0; j <= MAXW; ++j)
			heightList[j] = 0,
			skyline[k][j] = ' ';
		skyline[k][MAXW] = '\0';
	}

	return;
}